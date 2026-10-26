#!/usr/bin/env python3
"""Worked examples for the SLAM and Localization Cookbook.

Every number quoted under "Worked example" in COOKBOOK.md comes from a function
here. Requires only NumPy.

    python3 examples.py          # run all recipes
    python3 examples.py s02      # run recipes whose name contains "s02"
"""
import sys

import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(1)
G = 9.80665


def skew(v):
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def so3_exp(w):
    th = np.linalg.norm(w)
    if th < 1e-12:
        return np.eye(3) + skew(w)
    K = skew(w / th)
    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * K @ K


def so3_log(R):
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if th < 1e-12:
        return np.zeros(3)
    return th / (2 * np.sin(th)) * np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]])


def s01_lie_groups():
    w = np.array([0.0, 0.0, np.deg2rad(90)])
    R = so3_exp(w)
    print("exp([0,0,90deg]) =\n", R)
    print("log back ->", np.rad2deg(so3_log(R)), "deg")
    R2 = so3_exp(np.array([np.deg2rad(10), 0, 0])) @ R
    print("composition then log: angle", np.rad2deg(np.linalg.norm(so3_log(R2))).round(2), "deg")


def s02_imu_error_growth():
    for name, ba in [("consumer MEMS, 10 mg", 10e-3 * G), ("industrial MEMS, 1 mg", 1e-3 * G), ("navigation grade, 25 ug", 25e-6 * G)]:
        out = []
        for t in [10, 60, 600]:
            out.append(0.5 * ba * t ** 2)
        print(f"{name:26s}: position error from uncompensated accel bias after 10 s / 60 s / 600 s = "
              + " / ".join(f"{e:,.1f} m" for e in out))
    for name, bg_deg_h in [("MEMS gyro, 10 deg/h", 10.0), ("tactical, 1 deg/h", 1.0), ("navigation, 0.01 deg/h", 0.01)]:
        th = np.deg2rad(bg_deg_h / 3600)  # rad/s
        t = 60.0
        tilt = th * t
        pos = G * th * t ** 3 / 6  # tilt error x gravity, integrated twice
        print(f"{name:24s}: heading/tilt drift {np.rad2deg(tilt) * 60:.3f} arcmin after 60 s; gravity leakage position error {pos:.3f} m")


def s03_schuler():
    R_e = 6.371e6
    T = 2 * np.pi * np.sqrt(R_e / G)
    print(f"Schuler period 2*pi*sqrt(R/g) = {T / 60:.1f} min")


def s04_gnss_least_squares():
    # 6 satellites, receiver at origin-ish, solve x, y, z, clock bias by Gauss-Newton
    sats = np.array([[15600e3, 7540e3, 20140e3], [18760e3, 2750e3, 18610e3], [17610e3, 14630e3, 13480e3],
                     [19170e3, 610e3, 18390e3], [-5000e3, 18000e3, 19000e3], [10000e3, -15000e3, 20000e3]])
    truth = np.array([0.0, 0.0, 6370e3]); cb_true = 150.0  # clock bias in metres
    rho = np.linalg.norm(sats - truth, axis=1) + cb_true + rng.normal(0, 3.0, len(sats))
    x = np.array([0.0, 0.0, 6.0e6, 0.0])
    for _ in range(8):
        d = np.linalg.norm(sats - x[:3], axis=1)
        H = np.c_[-(sats - x[:3]) / d[:, None], np.ones(len(sats))]
        dx = np.linalg.lstsq(H, rho - (d + x[3]), rcond=None)[0]
        x += dx
    Q = np.linalg.inv(H.T @ H)
    print(f"position error {np.linalg.norm(x[:3] - truth):.2f} m, clock bias {x[3]:.1f} m (true 150), "
          f"PDOP {np.sqrt(np.trace(Q[:3, :3])):.2f}, GDOP {np.sqrt(np.trace(Q)):.2f}")


def s05_gnss_ins_kf():
    # 1-D error-state filter. INS integrates a biased accelerometer; GNSS gives position at 1 Hz (sigma 2 m).
    # Error state d = [ins_pos - true_pos, ins_vel - true_vel, accel_bias]; d' = [d_v, b, 0].
    dt, T = 0.01, 120.0
    n = int(T / dt)
    ba = 0.05  # m/s^2, unknown to the filter
    x_true = np.zeros(2); x_ins = np.zeros(2)
    d = np.zeros(3); P = np.diag([1.0, 0.1, 0.1 ** 2])
    F = np.array([[1, dt, 0], [0, 1, dt], [0, 0, 1.0]])
    Qd = np.diag([0, (0.01 ** 2) * dt, (1e-4) ** 2 * dt])
    H = np.array([[1.0, 0, 0]]); R = 4.0
    free, fused = [], []
    for k in range(n):
        a = 0.2 * np.sin(0.1 * k * dt)
        x_true += dt * np.array([x_true[1], a])
        x_ins += dt * np.array([x_ins[1], a + ba])
        d = F @ d; P = F @ P @ F.T + Qd
        if k % 100 == 0:
            z = x_ins[0] - (x_true[0] + rng.normal(0, 2.0))  # observed INS position error
            K = (P @ H.T) / (H @ P @ H.T + R)
            d = d + (K * (z - d[0])).ravel()
            P = (np.eye(3) - K @ H) @ P
        if (k + 1) % 3000 == 0:
            free.append(abs(x_ins[0] - x_true[0])); fused.append(abs(x_ins[0] - d[0] - x_true[0]))
    print("INS-only position error at 30/60/90/120 s:", np.round(free, 1), "m")
    print("GNSS/INS position error at 30/60/90/120 s:", np.round(fused, 2), f"m; estimated accel bias {d[2]:.4f} m/s^2 (true 0.05)")


def s06_stereo_depth():
    f, b, dd = 700.0, 0.12, 0.25  # focal length px, baseline m, disparity noise px
    for z in [2.0, 10.0, 30.0]:
        d = f * b / z
        print(f"z={z:>4} m: disparity {d:6.2f} px, depth std {z ** 2 * dd / (f * b):.3f} m")
    K = np.array([[700, 0, 320], [0, 700, 240], [0, 0, 1.0]])
    P = np.array([0.5, -0.2, 4.0])
    u = K @ P; print("pinhole projection of (0.5,-0.2,4.0) ->", (u[:2] / u[2]).round(2), "px")


def s07_ransac_iterations():
    for s, name in [(8, "8-point E"), (5, "5-point E"), (3, "P3P"), (2, "2-point (IMU-aided)")]:
        for w in [0.5]:
            N = np.log(1 - 0.99) / np.log(1 - w ** s)
            print(f"{name:20s}: inlier ratio {w}, 99% confidence -> {int(np.ceil(N))} iterations")


def s08_triangulation():
    K = np.array([[500, 0, 320], [0, 500, 240], [0, 0, 1.0]])
    X = np.array([0.3, 0.2, 5.0, 1.0])
    P1 = K @ np.c_[np.eye(3), np.zeros(3)]
    P2 = K @ np.c_[np.eye(3), np.array([-0.5, 0, 0])]
    x1 = P1 @ X; x1 = x1[:2] / x1[2] + rng.normal(0, 0.5, 2)
    x2 = P2 @ X; x2 = x2[:2] / x2[2] + rng.normal(0, 0.5, 2)
    A = np.array([x1[0] * P1[2] - P1[0], x1[1] * P1[2] - P1[1], x2[0] * P2[2] - P2[0], x2[1] * P2[2] - P2[1]])
    Xh = np.linalg.svd(A)[2][-1]; Xh = Xh[:3] / Xh[3]
    print("true point (0.3, 0.2, 5.0); triangulated (DLT, 0.5 px noise):", Xh.round(3))


def s09_mono_scale():
    # monocular VO gives the trajectory up to an unknown scale; align with Umeyama (sim3)
    t = np.linspace(0, 10, 50)
    gt = np.c_[t, np.sin(t), 0 * t]
    est = 0.37 * (gt @ so3_exp(np.array([0, 0, 0.3])).T) + np.array([2.0, -1.0, 0.5]) + rng.normal(0, 0.01, gt.shape)
    mu_e, mu_g = est.mean(0), gt.mean(0)
    E, Gc = est - mu_e, gt - mu_g
    U, S, Vt = np.linalg.svd(Gc.T @ E / len(t))
    D = np.eye(3); D[2, 2] = np.sign(np.linalg.det(U @ Vt))
    R = U @ D @ Vt
    s = np.trace(np.diag(S) @ D) / (E ** 2).sum(1).mean()
    tr = mu_g - s * R @ mu_e
    ate = np.sqrt(np.mean(np.sum((s * est @ R.T + tr - gt) ** 2, 1)))
    print(f"recovered scale {s:.3f} (true 1/0.37 = {1 / 0.37:.3f}); ATE after sim(3) alignment {ate:.3f} m")


def s10_preintegration():
    # integrate 200 Hz IMU for 0.1 s with constant rotation rate and accel; compare preintegrated dR, dv, dp
    dt, n = 0.005, 20
    w = np.array([0.0, 0.0, 1.0]); a = np.array([1.0, 0.0, 0.0])
    dR, dv, dp = np.eye(3), np.zeros(3), np.zeros(3)
    for _ in range(n):
        dp = dp + dv * dt + 0.5 * dR @ a * dt ** 2
        dv = dv + dR @ a * dt
        dR = dR @ so3_exp(w * dt)
    print(f"over 0.1 s: dtheta {np.rad2deg(np.linalg.norm(so3_log(dR))):.2f} deg, dv {dv.round(4)}, dp {dp.round(5)}")
    print("these deltas do not depend on the starting pose or velocity, so they are computed once per keyframe pair")


def s12_point_to_plane():
    # lidar scan registration: three orthogonal planes, solve 6-DoF update by linearized point-to-plane least squares
    pts, nrm = [], []
    for nvec, off in [((1, 0, 0), 5.0), ((0, 1, 0), 4.0), ((0, 0, 1), 0.0)]:
        nvec = np.array(nvec, float)
        for _ in range(100):
            p = rng.uniform(-3, 3, 3); p = p - (p @ nvec - off) * nvec
            pts.append(p); nrm.append(nvec)
    pts, nrm = np.array(pts), np.array(nrm)
    d = np.array([n @ p for n, p in zip(nrm, pts)])
    w_true, t_true = np.array([0.01, -0.02, 0.05]), np.array([0.2, -0.1, 0.05])
    src = (pts - t_true) @ so3_exp(w_true)  # source points = model transformed by inverse
    x = np.zeros(6)
    for _ in range(5):
        Rk, tk = so3_exp(x[:3]), x[3:]
        q = src @ Rk.T + tk
        r = np.einsum("ij,ij->i", nrm, q) - d
        J = np.c_[-np.einsum("ij,ijk->ik", nrm, np.array([skew(v) for v in (q - tk)])), nrm]
        dx = np.linalg.lstsq(J, -r, rcond=None)[0]
        x[:3] = so3_log(so3_exp(dx[:3]) @ Rk); x[3:] = tk + dx[3:]
    print("recovered rotation (deg):", np.rad2deg(x[:3]).round(3), "true", np.rad2deg(w_true).round(3))
    print("recovered translation (m):", x[3:].round(4), "true", t_true)


def s14_pose_graph_1d():
    # robot drives 10 steps of 1 m around a loop back to start; odometry biased +2%, one loop closure says x10 = x0
    n = 10
    odo = np.full(n, 1.02)
    truth_end = 0.0
    x_odo = np.r_[0, np.cumsum(odo)]
    # build linear least squares: prior x0=0, odometry x_{i+1}-x_i = odo_i (sigma .05), loop x10 - x0 = 10 (sigma .01) meaning back at start after 10 m loop
    A, b, w = [], [], []
    row = np.zeros(n + 1); row[0] = 1; A.append(row); b.append(0); w.append(1e3)
    for i in range(n):
        row = np.zeros(n + 1); row[i + 1] = 1; row[i] = -1; A.append(row); b.append(odo[i]); w.append(1 / 0.05)
    row = np.zeros(n + 1); row[n] = 1; row[0] = -1; A.append(row); b.append(10.0); w.append(1 / 0.01)
    A, b, W = np.array(A), np.array(b), np.diag(w) ** 2
    x = np.linalg.solve(A.T @ W @ A, A.T @ W @ b)
    print(f"odometry-only end position {x_odo[-1]:.2f} m along the loop (should be 10.00); after loop closure {x[-1]:.3f} m")
    print("error spread back over the trajectory: corrections", np.round(x - x_odo, 3)[1::3])


def s15_place_recognition_pr():
    tp, fp, fn = 180, 4, 36
    print(f"loop-closure detector: precision {tp / (tp + fp):.3f}, recall {tp / (tp + fn):.3f}")
    print("one false positive with weight 100x an odometry edge can drag the map; robust kernel weight at 10 sigma (Cauchy):",
          round(1 / (1 + 10 ** 2), 4))


def s17_degeneracy():
    # 2D point-to-line ICP in a corridor (two parallel walls along x) vs a room (walls along x and y)
    def hessian(normals, pts):
        J = np.c_[normals, pts[:, 0] * normals[:, 1] - pts[:, 1] * normals[:, 0]]  # [nx, ny, (p x n)_z]
        return J.T @ J
    xs = np.linspace(-10, 10, 200)
    corr_pts = np.r_[np.c_[xs, np.full(200, 1.0)], np.c_[xs, np.full(200, -1.0)]]
    corr_n = np.r_[np.tile([0, -1.0], (200, 1)), np.tile([0, 1.0], (200, 1))]
    room_pts = np.r_[corr_pts, np.c_[np.full(200, 5.0), np.linspace(-1, 1, 200)]]
    room_n = np.r_[corr_n, np.tile([-1.0, 0], (200, 1))]
    for name, Hh in [("corridor", hessian(corr_n, corr_pts)), ("corridor + end wall", hessian(room_n, room_pts))]:
        ev = np.linalg.eigvalsh(Hh)
        print(f"{name:20s}: eigenvalues of J^T J {ev.round(2)} -> condition {ev[-1] / max(ev[0], 1e-12):.3g}")


def s18_time_sync():
    for v, dt_ms in [(1.0, 10), (20.0, 10), (30.0, 50)]:
        print(f"{v:>4} m/s with {dt_ms} ms timestamp offset -> {v * dt_ms / 1000:.2f} m position error")
    w, dt, r = 1.0, 0.01, 50.0
    print(f"rotating at {w} rad/s with 10 ms offset -> {np.rad2deg(w * dt):.2f} deg, i.e. {r * w * dt:.2f} m error for a point {r:.0f} m away")


def s19_wahba_triad():
    # two vector observations (sun and magnetic field / two stars) -> attitude by TRIAD and SVD (Wahba)
    R_true = so3_exp(np.deg2rad(np.array([20.0, -10.0, 35.0])))
    r1, r2 = np.array([1.0, 0, 0]), np.array([0, 0.6, 0.8])
    b1 = R_true.T @ r1 + rng.normal(0, 1e-3, 3); b2 = R_true.T @ r2 + rng.normal(0, 1e-2, 3)
    b1 /= np.linalg.norm(b1); b2 /= np.linalg.norm(b2)
    B = 1.0 * np.outer(r1, b1) + 0.01 * np.outer(r2, b2)  # weights ~ 1/sigma^2 (relative)
    U, _, Vt = np.linalg.svd(B)
    R = U @ np.diag([1, 1, np.linalg.det(U) * np.linalg.det(Vt)]) @ Vt
    err = np.rad2deg(np.linalg.norm(so3_log(R.T @ R_true)))
    print(f"Wahba/SVD attitude error {err * 3600:.0f} arcsec ({err:.4f} deg) from two noisy vectors")
    for fov_deg, px, ac in [(20, 1024, 0.1)]:
        ifov = fov_deg * 3600 / px
        print(f"star tracker: {fov_deg} deg FOV on {px} px -> {ifov:.0f} arcsec/px; centroid to {ac} px -> ~{ifov * ac:.0f} arcsec per star")


def s21_metrics():
    gt = np.c_[np.linspace(0, 100, 101), np.zeros(101)]
    est = gt.copy(); est[:, 1] = 0.01 * gt[:, 0]  # 1% lateral drift
    ate = np.sqrt(np.mean(np.sum((est - gt) ** 2, 1)))
    rpe = np.sqrt(np.mean(np.sum(((est[10:] - est[:-10]) - (gt[10:] - gt[:-10])) ** 2, 1)))
    print(f"1% lateral drift over 100 m: ATE (no alignment) {ate:.3f} m, RPE over 10 m segments {rpe:.3f} m, end drift {100 * np.linalg.norm(est[-1] - gt[-1]) / 100:.2f}%")


RECIPES = {name: fn for name, fn in globals().items() if name.startswith("s") and name[1:3].isdigit()}

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, fn in RECIPES.items():
        if pattern in name:
            print(f"\n=== {name} ===")
            fn()
