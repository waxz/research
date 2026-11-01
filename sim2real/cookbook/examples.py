#!/usr/bin/env python3
"""Worked examples for the Sim-to-Real Cookbook.

Every number quoted under "Worked example" in COOKBOOK.md comes from a function
here. Requires only NumPy.

    python3 examples.py          # run all recipes
    python3 examples.py g02      # run recipes whose name contains "g02"
"""
import sys

import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(11)


def g01_motor_torque_speed():
    # DC / BLDC motor + gearbox: V = R i + k_e w_m ; tau_out = N * eta * k_t * i ; w_m = N * w_joint
    R, kt, V, N, eta, i_max = 0.2, 0.08, 24.0, 9.0, 0.9, 40.0
    ke = kt
    for w_joint in [0.0, 10.0, 20.0, 30.0, 33.0]:
        w_m = N * w_joint
        i = min(i_max, max(0.0, (V - ke * w_m) / R))
        print(f"joint speed {w_joint:5.1f} rad/s: max torque {N * eta * kt * i:6.1f} Nm")
    print(f"no-load joint speed {V / ke / N:.1f} rad/s; an 'ideal torque source' model would allow {N * eta * kt * i_max:.1f} Nm at every speed")


def simulate_pd(delay_steps, Kp=400.0, Kd=4.0, J=0.05, dt=0.001, T=0.6, tau_max=None, friction=0.0):
    q, qd = 0.0, 0.0
    buf = [0.0] * (delay_steps + 1)
    qs = []
    for _ in range(int(T / dt)):
        tau_cmd = Kp * (1.0 - q) - Kd * qd
        buf.append(tau_cmd)
        tau = buf.pop(0)
        if tau_max is not None:
            tau = np.clip(tau, -tau_max, tau_max)
        tau -= friction * np.sign(qd) if abs(qd) > 1e-6 else np.clip(tau, -friction, friction)
        qdd = tau / J
        qd += qdd * dt; q += qd * dt
        qs.append(q)
    return np.array(qs)


def g02_latency():
    for ms in [0, 5, 10, 20]:
        qs = simulate_pd(ms)
        osc = np.max(np.abs(qs[-100:] - 1.0))
        if osc > 1.0:
            print(f"actuation delay {ms:2d} ms: UNSTABLE (oscillation grows without bound)")
        else:
            print(f"actuation delay {ms:2d} ms: overshoot {100 * (qs.max() - 1):5.1f}%, residual oscillation over the last 0.1 s {osc:.3f} rad")


def g03_friction_deadband():
    for fr in [0.0, 1.0, 3.0]:
        q, qd, dt = 0.0, 0.0, 0.001
        for _ in range(2000):
            tau = 50.0 * (0.05 - q) - 2.0 * qd  # small 0.05 rad step, low gains (policy-style PD)
            if abs(qd) < 1e-4 and abs(tau) <= fr:
                qd = 0.0; continue  # stiction holds
            tau -= fr * np.sign(qd if abs(qd) > 1e-4 else tau)
            qd += tau / 0.05 * dt; q += qd * dt
        print(f"Coulomb friction {fr:.0f} Nm: final error on a 0.05 rad step {abs(0.05 - q):.4f} rad (deadband = friction/Kp = {fr / 50:.3f} rad)")


def g04_actuator_net():
    # "true" actuator: 8 ms delay, torque saturation at 20 Nm, Coulomb friction 1.5 Nm, plus noise
    n, d = 6000, 8
    err = np.cumsum(rng.normal(0, 0.02, n)); err -= np.convolve(err, np.ones(50) / 50, "same")
    vel = np.gradient(err) / 0.001 * 0.02
    cmd = 60.0 * err - 1.0 * vel
    true = np.clip(np.r_[np.zeros(d), cmd[:-d]], -20, 20) - 1.5 * np.tanh(vel / 0.5) + rng.normal(0, 0.3, n)
    # ideal model: torque = command
    ideal_rmse = np.sqrt(np.mean((cmd - true) ** 2))
    # learned model: features = history of commands (as in Hwangbo et al., history of errors and velocities)
    H = 12
    X = np.array([np.r_[cmd[k - H:k + 1], np.tanh(cmd[k - H:k + 1] / 20.0), np.tanh(vel[k] / 0.5), 1.0] for k in range(H, n)])
    y = true[H:]
    tr, te = slice(0, 4000), slice(4000, None)
    w = np.linalg.lstsq(X[tr], y[tr], rcond=None)[0]
    learned_rmse = np.sqrt(np.mean((X[te] @ w - y[te]) ** 2))
    print(f"torque prediction RMSE on held-out data: ideal 'torque = command' model {ideal_rmse:.2f} Nm, learned history model {learned_rmse:.2f} Nm")


def g05_soft_contact_stiffness():
    m, g = 10.0, 9.81
    for k in [1e4, 1e5, 1e6]:
        pen = m * g / k
        w = np.sqrt(k / m)
        print(f"contact stiffness {k:.0e} N/m: static penetration {1000 * pen:.2f} mm, contact natural frequency {w:.0f} rad/s -> "
              f"explicit-Euler stability needs dt < {2 / w * 1000:.2f} ms")


def g06_friction_pyramid():
    mu = 0.8
    for ang in [0, 22.5, 45]:
        a = np.deg2rad(ang)
        # 4-sided pyramid inscribed in the cone: |fx| + |fy| <= mu fn ... use the common box form |fx|,|fy| <= mu fn / sqrt(2)
        lim_inscribed = mu / np.sqrt(2) / max(abs(np.cos(a)), abs(np.sin(a)))
        lim_box = mu / max(abs(np.cos(a)), abs(np.sin(a)))
        print(f"tangential direction {ang:4.1f} deg: cone allows {mu:.3f} fn; inscribed box pyramid {lim_inscribed:.3f} fn; circumscribed box {lim_box:.3f} fn")


def g07_restitution():
    for e in [0.0, 0.3, 0.6]:
        h0 = 0.5
        hs = [h0 * e ** (2 * k) for k in range(1, 4)]
        print(f"restitution {e:.1f}: bounce heights after a 0.5 m drop {np.round(hs, 3)} m")


def g08_least_squares_sysid():
    # joint: tau = J qdd + b qd + c sign(qd) + m g l sin(q); identify J, b, c, mgl from a chirp
    J, b, c, mgl = 0.12, 0.35, 0.8, 2.5
    t = np.arange(0, 10, 0.002)
    q = 0.8 * np.sin(2 * np.pi * (0.2 + 0.25 * t) * t)
    qd = np.gradient(q, t); qdd = np.gradient(qd, t)
    tau = J * qdd + b * qd + c * np.sign(qd) + mgl * np.sin(q) + rng.normal(0, 0.05, len(t))
    Phi = np.c_[qdd, qd, np.sign(qd), np.sin(q)]
    th = np.linalg.lstsq(Phi, tau, rcond=None)[0]
    print(f"identified J={th[0]:.3f} (0.12), b={th[1]:.3f} (0.35), Coulomb={th[2]:.3f} (0.8), mgl={th[3]:.3f} (2.5)")
    # same experiment with a poor input: a slow, small sine barely excites inertia or friction
    qs = 0.1 * np.sin(2 * np.pi * 0.2 * t); qsd = np.gradient(qs, t); qsdd = np.gradient(qsd, t)
    taus = J * qsdd + b * qsd + c * np.sign(qsd) + mgl * np.sin(qs) + rng.normal(0, 0.05, len(t))
    ths = np.linalg.lstsq(np.c_[qsdd, qsd, np.sign(qsd), np.sin(qs)], taus, rcond=None)[0]
    print(f"with a slow 0.1 rad sine instead: J={ths[0]:.3f}, b={ths[1]:.3f}, Coulomb={ths[2]:.3f}, mgl={ths[3]:.3f} (inertia poorly excited)")


def g09_bayesian_friction():
    # block pushed with known force; measure acceleration; posterior over friction coefficient mu (grid Bayes)
    m, g, true_mu = 2.0, 9.81, 0.42
    F = rng.uniform(12, 20, 8)
    acc = (F - true_mu * m * g) / m + rng.normal(0, 0.15, 8)
    grid = np.linspace(0.1, 0.9, 801)
    logp = np.zeros_like(grid)  # uniform prior over [0.1, 0.9]
    for f, a in zip(F, acc):
        logp += -0.5 * ((a - (f - grid * m * g) / m) / 0.15) ** 2
    p = np.exp(logp - logp.max()); p /= p.sum()
    mean = (grid * p).sum(); std = np.sqrt(((grid - mean) ** 2 * p).sum())
    print(f"posterior over friction after 8 pushes: mean {mean:.3f} (true 0.42), std {std:.4f}; randomize mu ~ N({mean:.2f}, {std:.3f}) instead of U[0.1, 0.9]")


def cost_of_gain(K, m, dt=0.01, T=3.0, delay=2):
    # point mass with force u = -K (x - 1) - D v, D tuned for the nominal mass 1 kg; 20 ms delay
    D = 2 * np.sqrt(K * 1.0)
    x, v, buf, c = 0.0, 0.0, [0.0] * delay, 0.0
    for _ in range(int(T / dt)):
        buf.append(-K * (x - 1) - D * v); u = buf.pop(0)
        v += u / m * dt; x += v * dt
        c += (x - 1) ** 2 * dt
        if abs(x) > 1e3:
            return 1e3
    return c


def fmt(c):
    return "UNSTABLE" if c > 10 else f"{c:.3f}"


def g10_domain_randomization():
    gains = np.linspace(5, 300, 60)
    nominal = gains[np.argmin([cost_of_gain(K, 1.0) for K in gains])]
    masses = np.linspace(0.3, 1.0, 8)  # randomize mass (the real robot carries less or more payload)
    dr = gains[np.argmin([np.mean([cost_of_gain(K, mm) for mm in masses]) for K in gains])]
    for name, K in [("tuned on nominal sim (1.0 kg)", nominal), ("domain-randomized (0.3-1.0 kg)", dr)]:
        print(f"{name:32s}: gain {K:6.1f}; cost on the real 0.35 kg system {fmt(cost_of_gain(K, 0.35))}, on nominal {fmt(cost_of_gain(K, 1.0))}")


def g11_range_tradeoff():
    gains = np.linspace(5, 300, 60)
    for lo in [0.9, 0.6, 0.3, 0.15]:
        masses = np.linspace(lo, 1.0, 8)
        K = gains[np.argmin([np.mean([cost_of_gain(k, mm) for mm in masses]) for k in gains])]
        worst = max(cost_of_gain(K, mm) for mm in np.linspace(0.15, 1.0, 12))
        print(f"randomize mass over [{lo:.2f}, 1.0] kg: chosen gain {K:6.1f}, nominal cost {fmt(cost_of_gain(K, 1.0))}, worst case over [0.15, 1.0] {fmt(worst)}")


def g12_adr_schedule():
    lo, hi, step = 0.95, 1.05, 0.05
    hist = []
    for it in range(40):
        # pretend success probability falls as the range widens past what the policy can handle (width ~1.0)
        width = hi - lo
        succ = 1.0 / (1 + np.exp(8 * (width - 0.9 - 0.02 * it)))  # policy improves with training
        if succ > 0.8:
            lo, hi = max(0.05, lo - step / 2), hi + step / 2
        elif succ < 0.4:
            lo, hi = lo + step / 4, hi - step / 4
        if it in (0, 9, 19, 39):
            hist.append((it + 1, round(lo, 3), round(hi, 3), round(succ, 2)))
    for it, a, b, s in hist:
        print(f"ADR iteration {it:2d}: friction range [{a}, {b}], measured success {s}")


def g13_online_adaptation():
    # estimate an unknown payload mass online from force and acceleration with RLS (the 'adaptation module' idea)
    true_m = 1.0
    th, P, lam = 0.5, 10.0, 0.98
    for k in range(400):
        if k == 200:
            true_m = 1.6  # payload added
        u = 3 * np.sin(0.05 * k) + rng.normal(0, 1)
        a = u / true_m + rng.normal(0, 0.05)
        phi = a  # model: u = m * a
        K = P * phi / (lam + phi * P * phi); th += K * (u - phi * th); P = (P - K * phi * P) / lam
        if k in (20, 199, 230, 399):
            print(f"step {k + 1:3d}: estimated mass {th:.3f} kg (true {true_m})")


def g14_delta_action():
    # sim: x+ = x + u dt ; real: x+ = x + (0.8 u - 0.1) dt (weaker, biased actuator). Learn delta action from real data.
    dt = 0.05
    def real_step(x, u): return x + (0.8 * u - 0.1) * dt
    U = rng.uniform(-2, 2, 300); X = rng.uniform(-1, 1, 300)
    # delta action: find du so that sim(x, u + du) = real(x, u)  ->  du = -0.2 u - 0.1 ; fit du = a u + b
    du = (real_step(X, U) - X) / dt - U + rng.normal(0, 0.01, 300)
    a, b = np.linalg.lstsq(np.c_[U, np.ones_like(U)], du, rcond=None)[0]
    print(f"learned delta action du = {a:.3f} u + {b:.3f}  (true -0.2 u - 0.1)")
    def track(policy_in_sim_with_delta):
        x, err = 0.0, 0.0
        for k in range(100):
            target = np.sin(0.1 * k)
            u_sim = (target - x) / dt * 0.5
            u = (u_sim - b) / (1 + a) if policy_in_sim_with_delta else u_sim  # policy fine-tuned in the corrected sim
            x = real_step(x, u); err += (x - target) ** 2
        return np.sqrt(err / 100)
    print(f"real-world tracking RMSE: policy from the plain sim {track(False):.3f}, after delta-action fine-tuning {track(True):.3f}")


def g15_srcc():
    sim = np.array([0.95, 0.91, 0.88, 0.86, 0.80, 0.78, 0.74, 0.70, 0.62])
    real_bad = np.array([0.40, 0.62, 0.35, 0.58, 0.55, 0.30, 0.50, 0.45, 0.42])
    real_good = sim - 0.15 + rng.normal(0, 0.03, 9)
    for name, r in [("sim with exploitable collisions", real_bad), ("tuned sim", real_good)]:
        print(f"{name:32s}: sim-vs-real correlation (SRCC) {np.corrcoef(sim, r)[0, 1]:.2f}")


def g16_integrator():
    k, m, dt, n = 1e4, 1.0, 0.005, 400
    for name in ["explicit Euler", "semi-implicit Euler"]:
        x, v = 0.01, 0.0
        E0 = 0.5 * k * x * x
        for _ in range(n):
            if name == "explicit Euler":
                x, v = x + v * dt, v - k / m * x * dt
            else:
                v = v - k / m * x * dt; x = x + v * dt
        E = 0.5 * k * x * x + 0.5 * m * v * v
        print(f"{name:20s}: energy after {n} steps of a stiff contact spring = {E / E0:.3g} x initial")


RECIPES = {name: fn for name, fn in globals().items() if name.startswith("g") and name[1:3].isdigit()}

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, fn in RECIPES.items():
        if pattern in name:
            print(f"\n=== {name} ===")
            fn()
