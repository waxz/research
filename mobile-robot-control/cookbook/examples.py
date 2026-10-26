#!/usr/bin/env python3
"""Worked examples for the Mobile Robot Control Cookbook (forklifts, AGVs, AMRs).

Every number quoted under "Worked example" in COOKBOOK.md comes from a function
here. Requires only NumPy.

    python3 examples.py          # run all recipes
    python3 examples.py m15      # run recipes whose name contains "m15"
"""
import heapq
import itertools
import sys

import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(0)


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def m01_se2_composition():
    def compose(p, d):  # p, d = (x, y, theta); d expressed in p's frame
        x, y, t = p
        return np.array([x + d[0] * np.cos(t) - d[1] * np.sin(t), y + d[0] * np.sin(t) + d[1] * np.cos(t), wrap(t + d[2])])
    p = np.array([2.0, 1.0, np.pi / 2])
    d = np.array([1.0, 0.0, -np.pi / 2])
    print("robot at (2, 1, 90deg) moves 1 m forward then turns -90deg ->", compose(p, d))


def m02_diff_drive():
    r, b = 0.1, 0.5  # wheel radius, track width (m)
    wl, wr = 8.0, 10.0  # rad/s
    v, w = r * (wr + wl) / 2, r * (wr - wl) / b
    print(f"wheel speeds L={wl} R={wr} rad/s -> v={v:.2f} m/s, omega={w:.2f} rad/s, turn radius={v / w:.2f} m")
    # inverse
    v_cmd, w_cmd = 1.0, 0.5
    print(f"command v={v_cmd}, omega={w_cmd} -> wheel L={(v_cmd - w_cmd * b / 2) / r:.2f}, R={(v_cmd + w_cmd * b / 2) / r:.2f} rad/s")


def m04_forklift_tricycle():
    L = 1.6  # wheelbase: steered drive wheel to load-axle midpoint (m)
    for deg in [30, 60, 85]:
        d = np.deg2rad(deg)
        print(f"steer {deg:>2} deg -> turn radius about load axle {L / np.tan(d):.2f} m, yaw rate per m/s {np.sin(d) / L:.3f} rad/s, forward speed of reference point {np.cos(d):.3f} x drive speed")


def m05_mecanum():
    r, lx, ly = 0.076, 0.25, 0.2
    k = lx + ly
    Jinv = (1 / r) * np.array([[1, -1, -k], [1, 1, k], [1, 1, -k], [1, -1, k]])
    for cmd in [(0.5, 0, 0), (0, 0.5, 0), (0, 0, 1.0)]:
        print(f"body (vx, vy, w)={cmd} -> wheels FL,FR,RL,RR = {Jinv @ np.array(cmd)} rad/s")


def m06_odometry_drift():
    # each 1 m of travel adds independent heading noise sigma_theta and wheel-scale error
    sig_th = np.deg2rad(0.5)
    N = 2000
    ends = []
    for _ in range(N):
        x = y = th = 0.0
        for _ in range(50):  # 50 m straight run in 1 m steps
            th += sig_th * rng.standard_normal()
            x += np.cos(th); y += np.sin(th)
        ends.append(y)
    print(f"0.5 deg heading noise per metre, 50 m run: lateral std {np.std(ends):.2f} m (grows ~ distance^1.5)")
    scale_err = 0.005
    print(f"0.5% wheel-diameter mismatch on a 0.5 m track: heading error {scale_err / 0.5:.3f} rad per metre = {np.rad2deg(scale_err / 0.5):.2f} deg/m")


def m07_ekf_reflector():
    # one reflector at known (5, 0); robot prior (0, 0.2, 0) with covariance; measure range and bearing
    x = np.array([0.0, 0.2, 0.0]); P = np.diag([0.04, 0.04, np.deg2rad(2) ** 2])
    lm = np.array([5.0, 0.0]); R = np.diag([0.02 ** 2, np.deg2rad(0.5) ** 2])
    true = np.array([0.0, 0.0, 0.0])
    def h(s):
        dx, dy = lm - s[:2]
        return np.array([np.hypot(dx, dy), wrap(np.arctan2(dy, dx) - s[2])])
    z = h(true)
    dx, dy = lm - x[:2]; q = dx ** 2 + dy ** 2; sq = np.sqrt(q)
    H = np.array([[-dx / sq, -dy / sq, 0], [dy / q, -dx / q, -1]])
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    innov = z - h(x); innov[1] = wrap(innov[1])
    x2 = x + K @ innov; P2 = (np.eye(3) - K @ H) @ P
    print("prior", x, "-> posterior", x2)
    print("std before", np.sqrt(np.diag(P)), "after", np.sqrt(np.diag(P2)))


def m08_particle_filter_1d():
    # corridor with doors at 2, 4, 9 m; robot at 4 m senses "door"
    doors = np.array([2.0, 4.0, 9.0])
    parts = rng.uniform(0, 12, 5000)
    def door_like(p):
        return np.exp(-np.min(np.abs(p[:, None] - doors[None, :]), axis=1) ** 2 / (2 * 0.3 ** 2))
    w = 0.02 + door_like(parts); w /= w.sum()
    parts = parts[rng.choice(len(parts), len(parts), p=w)]
    hist1 = np.histogram(parts, bins=[0, 3, 6, 12])[0] / len(parts)
    # move +2 m (noise 0.1) and sense "no door" at 6 m
    parts = parts + 2.0 + 0.1 * rng.standard_normal(len(parts))
    w = 1.0 - 0.98 * door_like(parts); w /= w.sum()
    parts = parts[rng.choice(len(parts), len(parts), p=w)]
    # move +3 m and sense "door" (true position 9)
    parts = parts + 3.0 + 0.1 * rng.standard_normal(len(parts))
    w = 0.02 + door_like(parts); w /= w.sum()
    parts = parts[rng.choice(len(parts), len(parts), p=w)]
    print("after first 'door' reading, mass in [0,3),[3,6),[6,12):", np.round(hist1, 2))
    near = np.mean(np.abs(parts - 9.0) < 0.5)
    print(f"after move+sense x2: {100 * near:.0f}% of particles within 0.5 m of the true 9.0 m; median {np.median(parts):.2f} m")


def m09_icp_svd():
    th, t = np.deg2rad(10), np.array([0.3, -0.2])
    Rt = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    P = rng.uniform(-5, 5, (40, 2))
    Q = P @ Rt.T + t + 0.01 * rng.standard_normal((40, 2))
    mp, mq = P.mean(0), Q.mean(0)
    U, _, Vt = np.linalg.svd((P - mp).T @ (Q - mq))
    Rh = Vt.T @ U.T
    if np.linalg.det(Rh) < 0:
        Vt[-1] *= -1; Rh = Vt.T @ U.T
    th_hat = np.rad2deg(np.arctan2(Rh[1, 0], Rh[0, 0])); t_hat = mq - Rh @ mp
    print(f"true rotation 10.00 deg, t=(0.30,-0.20); estimated {th_hat:.2f} deg, t=({t_hat[0]:.3f},{t_hat[1]:.3f})")


def m10_log_odds():
    l0, l_occ, l_free = 0.0, np.log(0.7 / 0.3), np.log(0.4 / 0.6)
    l = l0
    for z in ["hit", "hit", "miss", "hit"]:
        l += l_occ if z == "hit" else l_free
        print(f"after {z:4s}: p(occupied) = {1 - 1 / (1 + np.exp(l)):.3f}")


def m11_astar_grid():
    grid = np.zeros((6, 8), dtype=int)
    grid[1:5, 3] = 1  # wall
    start, goal = (2, 0), (2, 7)
    def h(a):
        return abs(a[0] - goal[0]) + abs(a[1] - goal[1])
    for name, heur in [("Dijkstra", lambda a: 0), ("A* (Manhattan)", h)]:
        openq, g, seen, expanded = [(heur(start), 0, start)], {start: 0}, set(), 0
        while openq:
            f, gc, u = heapq.heappop(openq)
            if u in seen:
                continue
            seen.add(u); expanded += 1
            if u == goal:
                break
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                v = (u[0] + d[0], u[1] + d[1])
                if 0 <= v[0] < 6 and 0 <= v[1] < 8 and not grid[v] and gc + 1 < g.get(v, 1e9):
                    g[v] = gc + 1
                    heapq.heappush(openq, (gc + 1 + heur(v), gc + 1, v))
        print(f"{name:15s}: path cost {g[goal]}, nodes expanded {expanded}")


def m12_min_turn():
    for v, alat in [(1.0, 0.5), (2.0, 0.5)]:
        R = v ** 2 / alat
        print(f"speed {v} m/s with lateral-acceleration limit {alat} m/s^2 -> minimum radius {R:.1f} m")


def m14_speed_profile_and_fields():
    # curvature speed limit and stopping distance / protective field length
    for kappa in [0.2, 1.0]:
        print(f"curvature {kappa} 1/m, a_lat 0.5 m/s^2 -> v_max {np.sqrt(0.5 / kappa):.2f} m/s")
    for v in [1.0, 2.0]:
        t_r, a, margin = 0.3, 1.0, 0.1  # reaction (scanner + controller + brake engage), braking decel, margin
        d = v * t_r + v ** 2 / (2 * a) + margin
        print(f"v={v} m/s: stopping distance {v * t_r + v ** 2 / (2 * a):.2f} m -> protective field >= {d:.2f} m")


def m15_tracking_controllers():
    # pure pursuit curvature, Stanley steering, and a Kanayama controller simulation
    Ld, alpha = 1.5, np.deg2rad(20)
    print(f"pure pursuit: lookahead {Ld} m, target at {np.rad2deg(alpha):.0f} deg -> curvature {2 * np.sin(alpha) / Ld:.3f} 1/m")
    k, e, psi, v = 1.0, 0.3, np.deg2rad(5), 1.0
    print(f"Stanley: heading error 5 deg, cross-track 0.3 m, v=1 -> steer {np.rad2deg(psi + np.arctan2(k * e, v)):.1f} deg")
    # Kanayama: track straight line y=0 at v_r=1 from offset y=0.5, heading 0
    x, y, th, dt = 0.0, 0.5, 0.0, 0.02
    kx, ky, kth = 1.0, 4.0, 4.0
    for i in range(500):
        xr, yr, thr = (i * dt) * 1.0, 0.0, 0.0
        ex = np.cos(th) * (xr - x) + np.sin(th) * (yr - y)
        ey = -np.sin(th) * (xr - x) + np.cos(th) * (yr - y)
        eth = wrap(thr - th)
        v = 1.0 * np.cos(eth) + kx * ex
        w = 0.0 + 1.0 * (ky * ey + kth * np.sin(eth))
        x += v * np.cos(th) * dt; y += v * np.sin(th) * dt; th += w * dt
        if i in (49, 99, 249):
            print(f"Kanayama t={(i + 1) * dt:.0f} s: lateral error {y:.4f} m, heading {np.rad2deg(th):.2f} deg")


def m16_mppi_weights():
    costs = np.array([10.0, 11.0, 15.0, 30.0])
    for lam in [1.0, 5.0]:
        w = np.exp(-(costs - costs.min()) / lam); w /= w.sum()
        print(f"MPPI lambda={lam}: rollout costs {costs} -> weights {np.round(w, 3)}")


def m17_dwa_score():
    # score candidate (v, w) by heading to goal, clearance, speed
    goal = np.array([5.0, 0.0]); obs = np.array([[1.2, 0.0]])  # obstacle straight ahead on the way to the goal
    best, rows = None, []
    for v, w in itertools.product([0.3, 0.6, 0.9], [-0.6, 0.0, 0.6]):
        x = y = th = 0.0
        clear = 9.0
        for _ in range(30):  # 3 s horizon
            x += v * np.cos(th) * 0.1; y += v * np.sin(th) * 0.1; th += w * 0.1
            clear = min(clear, np.min(np.hypot(obs[:, 0] - x, obs[:, 1] - y)))
        if clear < 0.4:
            rows.append((v, w, None)); continue
        heading = np.pi - abs(wrap(np.arctan2(goal[1] - y, goal[0] - x) - th))
        score = 0.5 * heading + 1.0 * min(clear, 1.0) + 0.3 * v
        rows.append((v, w, score))
        if best is None or score > best[0]:
            best = (score, v, w)
    rejected = [(v, w) for v, w, sc in rows if sc is None]
    print(f"rejected (would pass within 0.4 m of the obstacle): {rejected}")
    print(f"DWA picks v={best[1]} m/s, omega={best[2]} rad/s (score {best[0]:.3f})")


def m19_forklift_stability():
    g = 9.81
    m_t, d_t = 3000.0, 0.9   # truck mass (kg), its CoG behind front axle (m)
    for m_l, c in [(1500.0, 0.5), (2200.0, 0.6), (2500.0, 0.8)]:
        d_l = 0.45 + c  # front axle to fork face 0.45 m + load centre c
        ok = m_l * d_l <= m_t * d_t
        print(f"load {m_l:.0f} kg at load centre {c} m: load moment {m_l * d_l:.0f} vs truck moment {m_t * d_t:.0f} kg*m -> {'stable' if ok else 'TIPS FORWARD'}")
    cap = m_t * d_t / (0.45 + 0.5)
    print(f"rated capacity at 0.5 m load centre = {cap:.0f} kg; at 0.8 m it derates to {m_t * d_t / 1.25:.0f} kg")
    # braking with a raised load: extra overturning moment m*a*h
    m_l, h, a = 1500.0, 3.0, 1.5
    print(f"braking at {a} m/s^2 with {m_l:.0f} kg raised {h} m adds {m_l * a * h / g:.0f} kg*m equivalent forward moment")
    # lateral tip in a turn: v_max = sqrt(g * b_eff * R / h_cg)
    b_eff, h_cg, R = 0.35, 1.2, 2.0
    print(f"lateral: CoG {h_cg} m high, effective half-base {b_eff} m, radius {R} m -> v_tip {np.sqrt(g * b_eff * R / h_cg):.2f} m/s")


def m20_fleet():
    cost = np.array([[1, 2, 8], [2, 9, 9], [8, 9, 3]])  # robot x task travel times (min)
    best = min(itertools.permutations(range(3)), key=lambda p: sum(cost[i, p[i]] for i in range(3)))
    free, greedy = set(range(3)), []
    for i in range(3):  # each robot in turn grabs its nearest free task
        j = min(free, key=lambda j: cost[i, j]); free.remove(j); greedy.append(j)
    print("greedy robot->task", tuple(greedy), "total", sum(cost[i, greedy[i]] for i in range(3)), "min;",
          "optimal", best, "total", sum(cost[i, best[i]] for i in range(3)), "min")
    lam, W = 120 / 60, 6.0  # 120 jobs/hour, 6 min average cycle
    print(f"Little's law: {lam * 60:.0f} jobs/h x {W} min cycle -> {lam * W:.0f} robots busy on average; at 85% target utilization -> {np.ceil(lam * W / 0.85):.0f} robots")


def m21_rl_reward():
    d_prev, d_now, collided, reached = 3.2, 3.05, False, False
    r = 10 * (d_prev - d_now) - 0.01 - (20 if collided else 0) + (20 if reached else 0)
    print(f"progress reward: {d_prev}->{d_now} m to goal -> r = {r:.2f}")


RECIPES = {name: fn for name, fn in globals().items() if name.startswith("m") and name[1:3].isdigit()}

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, fn in RECIPES.items():
        if pattern in name:
            print(f"\n=== {name} ===")
            fn()
