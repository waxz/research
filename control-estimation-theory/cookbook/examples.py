#!/usr/bin/env python3
"""Worked examples for the Control and Estimation Theory Cookbook.

Every number quoted under "Worked example" in COOKBOOK.md comes from a function
here. Requires only NumPy.

    python3 examples.py          # run all recipes
    python3 examples.py c03      # run recipes whose name contains "c03"
"""
import sys

import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(7)


def freq_resp(num, den, w):
    s = 1j * w
    return np.polyval(num, s) / np.polyval(den, s)


def dare(A, B, Q, R, iters=5000):
    P = Q.copy()
    for _ in range(iters):
        P = Q + A.T @ P @ A - A.T @ P @ B @ np.linalg.solve(R + B.T @ P @ B, B.T @ P @ A)
    return P, np.linalg.solve(R + B.T @ P @ B, B.T @ P @ A)


def simulate_lti(num, den, u, dt):
    """Simulate a strictly proper SISO transfer function in controllable canonical form (RK4)."""
    n = len(den) - 1
    a = np.array(den[1:], float) / den[0]
    b = np.zeros(n); b[n - len(num):] = np.array(num, float) / den[0]
    A = np.zeros((n, n)); A[:-1, 1:] = np.eye(n - 1); A[-1] = -a[::-1]
    Bv = np.zeros(n); Bv[-1] = 1.0
    C = b[::-1]
    x = np.zeros(n); y = []
    for uk in u:
        f = lambda xx: A @ xx + Bv * uk
        k1 = f(x); k2 = f(x + dt / 2 * k1); k3 = f(x + dt / 2 * k2); k4 = f(x + dt * k3)
        x = x + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y.append(C @ x)
    return np.array(y)


# ---------------- classical and modern control ----------------

def c01_feedback_basics():
    for K in [1.0, 10.0, 100.0]:
        print(f"L(s)=K/(s+1), K={K:>5}: closed-loop DC gain {K / (1 + K):.3f}, steady-state error {1 / (1 + K):.3f}, "
              f"closed-loop bandwidth {1 + K:.0f} rad/s")


def c02_routh_critical_gain():
    # plant 1/((s+1)(s+2)(s+3)) with proportional gain K: s^3 + 6 s^2 + 11 s + 6 + K
    for K in [10.0, 59.0, 61.0]:
        r = np.roots([1, 6, 11, 6 + K])
        print(f"K={K:>4}: max real part of closed-loop poles {r.real.max():+.3f} -> {'stable' if r.real.max() < 0 else 'UNSTABLE'}")
    print("Routh-Hurwitz: stable iff 6*11 > 6+K, i.e. K < 60; at K=60 poles at +-j*sqrt(11) =", round(np.sqrt(11), 3))


def c03_pid_ziegler_nichols():
    # plant G = 1/(s+1)^3: ultimate gain Ku = 8 at wu = sqrt(3)
    Ku, wu = 8.0, np.sqrt(3.0)
    Tu = 2 * np.pi / wu
    for name, Kp, Ti, Td in [("Ziegler-Nichols PID", 0.6 * Ku, Tu / 2, Tu / 8), ("softer PI (Kp=1, Ti=2)", 1.0, 2.0, 0.0)]:
        dt, T = 0.002, 30.0
        n = int(T / dt)
        x = np.zeros(3); integ = 0.0; y_prev = 0.0; ys = []; dfilt = 0.0
        for k in range(n):
            y = x[2]
            e = 1.0 - y
            integ += e * dt
            dy = (y - y_prev) / dt; y_prev = y
            dfilt += dt / 0.05 * (dy - dfilt)  # derivative on measurement with a 50 ms filter
            u = Kp * (e + integ / Ti - Td * dfilt)
            # three cascaded first-order lags
            x[0] += dt * (-x[0] + u); x[1] += dt * (-x[1] + x[0]); x[2] += dt * (-x[2] + x[1])
            ys.append(y)
        ys = np.array(ys)
        settle = next((k * dt for k in range(n - 1, -1, -1) if abs(ys[k] - 1) > 0.02), 0.0)
        print(f"{name:24s}: Kp={Kp:.2f} Ti={Ti:.2f} Td={Td:.3f} -> overshoot {100 * (ys.max() - 1):.0f}%, 2% settling {settle:.1f} s")
    print(f"ultimate gain Ku={Ku}, ultimate period Tu={Tu:.2f} s")


def c04_margins():
    # L(s) = K e^{-theta s} / (tau s + 1)
    K, tau, theta = 4.0, 1.0, 0.2
    w = np.logspace(-2, 2, 200000)
    mag = K / np.sqrt(1 + (tau * w) ** 2)
    ph = -np.arctan(tau * w) - theta * w
    wc = w[np.argmin(abs(mag - 1))]
    pm = 180 + np.rad2deg(-np.arctan(tau * wc) - theta * wc)
    w180 = w[np.argmin(abs(ph + np.pi))]
    gm = 1 / (K / np.sqrt(1 + (tau * w180) ** 2))
    print(f"L = 4 e^(-0.2 s)/(s+1): crossover {wc:.2f} rad/s, phase margin {pm:.1f} deg, gain margin {20 * np.log10(gm):.1f} dB, "
          f"delay margin {np.deg2rad(pm) / wc:.3f} s")


def c05_pole_placement():
    # double integrator, place poles at -2 +- 2j via Ackermann
    A = np.array([[0, 1.0], [0, 0]]); B = np.array([[0], [1.0]])
    Ctrb = np.c_[B, A @ B]
    desired = np.poly([-2 + 2j, -2 - 2j]).real
    phiA = desired[0] * A @ A + desired[1] * A + desired[2] * np.eye(2)
    K = np.array([[0, 1.0]]) @ np.linalg.inv(Ctrb) @ phiA
    print("controllability matrix rank", np.linalg.matrix_rank(Ctrb), "| Ackermann gain K =", K.ravel(),
          "| closed-loop poles", np.linalg.eigvals(A - B @ K).round(3))


def c06_lqr_vs_lqg_margins():
    # continuous LQR on a SISO plant has gain margin [1/2, inf) and phase margin >= 60 deg: check numerically
    A = np.array([[0, 1.0], [-1.0, -0.2]]); B = np.array([[0], [1.0]]); Q = np.diag([10.0, 1.0]); R = np.array([[1.0]])
    # solve CARE via the Hamiltonian
    H = np.block([[A, -B @ np.linalg.inv(R) @ B.T], [-Q, -A.T]])
    ev, V = np.linalg.eig(H)
    Vs = V[:, ev.real < 0]
    P = np.real(Vs[2:] @ np.linalg.inv(Vs[:2]))
    K = np.linalg.inv(R) @ B.T @ P
    w = np.logspace(-3, 3, 200000)
    Lw = np.array([(K @ np.linalg.solve(1j * wi * np.eye(2) - A, B))[0, 0] for wi in w[::50]])
    Ms = np.max(1 / np.abs(1 + Lw))
    idx = np.argmin(abs(np.abs(Lw) - 1))
    pm = 180 + np.rad2deg(np.angle(Lw[idx]))
    print(f"LQR gain K={K.ravel().round(3)}; loop-transfer peak sensitivity |S|max={Ms:.3f} (<=1 for LQR); phase margin {pm:.1f} deg (>=60 guaranteed)")
    print("LQG (Kalman filter in the loop) has no such guarantee: Doyle 1978, abstract 'There are none.'")


def c07_minimum_time():
    # double integrator from x=1, v=0 to origin with |u|<=1: bang-bang, switch at half way
    x, v, dt, t = 1.0, 0.0, 1e-4, 0.0
    while abs(x) > 1e-3 or abs(v) > 1e-3:
        s = x + 0.5 * v * abs(v)  # switching function
        u = -np.sign(s) if abs(s) > 1e-9 else -np.sign(v)
        v += u * dt; x += v * dt; t += dt
        if t > 5:
            break
    print(f"minimum-time bang-bang transfer: {t:.3f} s (analytic 2*sqrt(x0) = 2.000 s); switching curve x = -v|v|/2")


def c08_robust_sensitivity():
    # sensitivity peak Ms bounds margins: GM >= Ms/(Ms-1), PM >= 2 arcsin(1/(2 Ms))
    for Ms in [1.4, 2.0]:
        print(f"Ms={Ms}: guaranteed gain margin >= {20 * np.log10(Ms / (Ms - 1)):.1f} dB, phase margin >= {np.rad2deg(2 * np.arcsin(1 / (2 * Ms))):.1f} deg")
    # H-infinity norm of S for the ZN-tuned loop vs the PI loop from c03, plant 1/(s+1)^3
    w = np.logspace(-3, 2, 20000)
    G = 1 / (1j * w + 1) ** 3
    for name, Kp, Ti, Td in [("ZN PID", 4.8, 1.81, 0.453), ("soft PI", 1.0, 2.0, 0.0)]:
        C = Kp * (1 + 1 / (1j * w * Ti) + Td * 1j * w / (1 + 0.05 * 1j * w))
        S = 1 / (1 + G * C)
        print(f"{name:7s}: ||S||_inf = Ms = {np.abs(S).max():.2f}")


def c09_mrac():
    # plant y' = -a y + b u with unknown b; reference model ym' = -2 ym + 2 r; adapt feedforward gain theta (u = theta r)
    a, b = 2.0, 0.5
    dt, T = 1e-3, 40.0
    for gamma in [0.5, 2.0]:
        y = ym = 0.0; th = 0.0
        errs = []
        for k in range(int(T / dt)):
            r = 1.0 if (k * dt) % 20 < 10 else -1.0
            u = th * r
            e = y - ym
            th += -gamma * e * r * np.sign(b) * dt  # Lyapunov-based adaptation law
            y += dt * (-a * y + b * u); ym += dt * (-2 * ym + 2 * r)
            errs.append(abs(e))
        print(f"adaptation gain {gamma}: final theta {th:.3f} (ideal 2/b = {2 / b:.1f}); mean |tracking error| last 10 s {np.mean(errs[-10000:]):.4f}")


def c10_sliding_mode():
    # x'' = u + d(t), |d| <= 0.5; sliding surface s = xdot + 2 x; u = -2 xdot - k sat(s/phi)
    for phi in [1e-6, 0.05]:
        x, v, dt = 1.0, 0.0, 1e-4
        sw = 0; u_prev = 0.0
        for k in range(int(6 / dt)):
            d = 0.5 * np.sin(3 * k * dt)
            s = v + 2 * x
            u = -2 * v - 1.0 * np.clip(s / phi, -1, 1)
            if np.sign(u) != np.sign(u_prev):
                sw += 1
            u_prev = u
            v += (u + d) * dt; x += v * dt
        print(f"boundary layer phi={phi:g}: |x(6 s)| = {abs(x):.4f}, control sign changes {sw} (chattering when phi -> 0)")


def c11_mpc_vs_saturated_lqr():
    # double integrator, |u| <= 0.5, start at x=5: MPC with input constraints (projected gradient QP) vs clipped LQR
    dt = 0.1
    A = np.array([[1, dt], [0, 1.0]]); B = np.array([[0.5 * dt ** 2], [dt]])
    Q = np.diag([1.0, 0.1]); R = np.array([[0.1]]); umax = 0.5; N = 40
    P, K = dare(A, B, Q, R)
    # condensed prediction matrices
    Sx = np.vstack([np.linalg.matrix_power(A, i + 1) for i in range(N)])
    Su = np.zeros((2 * N, N))
    for i in range(N):
        for j in range(i + 1):
            Su[2 * i:2 * i + 2, j] = (np.linalg.matrix_power(A, i - j) @ B).ravel()
    Qb = np.kron(np.eye(N), Q); Qb[-2:, -2:] = P
    Hm = Su.T @ Qb @ Su + np.kron(np.eye(N), R)
    step = 1 / np.linalg.eigvalsh(Hm).max()
    def run(policy):
        x = np.array([5.0, 0.0]); cost = 0.0; xs = []
        for _ in range(150):
            u = policy(x)
            cost += x @ Q @ x + R[0, 0] * u ** 2
            x = A @ x + (B * u).ravel(); xs.append(x[0])
        xs = np.abs(np.array(xs))
        settle = (len(xs) - np.argmax(xs[::-1] > 0.05)) * dt  # last time |x| exceeds 5 cm
        return cost, settle
    def mpc(x):
        f = Su.T @ Qb @ Sx @ x
        U = np.zeros(N)
        for _ in range(400):
            U = np.clip(U - step * (Hm @ U + f), -umax, umax)
        return U[0]
    lqr_clip = lambda x: float(np.clip(-(K @ x)[0], -umax, umax))
    def overshoot(policy):
        x = np.array([5.0, 0.0]); mn = 0.0
        for _ in range(150):
            x = A @ x + (B * policy(x)).ravel(); mn = min(mn, x[0])
        return -mn
    for name, pol in [("clipped LQR", lqr_clip), ("constrained MPC", mpc)]:
        c, ts = run(pol)
        print(f"{name:16s}: cost {c:7.1f}, overshoot past the target {overshoot(pol):.3f} m, settles within 5 cm at {ts:.1f} s")


def c12_system_id():
    # identify y[k] = a y[k-1] + b u[k-1] + noise by least squares (ARX)
    a, b, n = 0.9, 0.5, 400
    u = rng.choice([-1.0, 1.0], n)  # persistently exciting
    y = np.zeros(n)
    for k in range(1, n):
        y[k] = a * y[k - 1] + b * u[k - 1] + 0.05 * rng.standard_normal()
    Phi = np.c_[y[:-1], u[:-1]]
    th = np.linalg.lstsq(Phi, y[1:], rcond=None)[0]
    # constant input with the output already at steady state: y = 5 u, so the two regressor columns are proportional
    yc = np.full(n, b / (1 - a)); uc = np.ones(n)
    rank = np.linalg.matrix_rank(np.c_[yc[:-1], uc[:-1]])
    print(f"ARX least squares with a random +-1 input: a={th[0]:.3f} (true 0.9), b={th[1]:.3f} (true 0.5)")
    print(f"with a constant input at steady state the regressor matrix has rank {rank} of 2 -> a and b are not identifiable")


# ---------------- estimation ----------------

def e01_recursive_least_squares():
    # track a parameter that jumps from 1.0 to 2.0 at k=200, forgetting factor 1.0 vs 0.95
    for lam in [1.0, 0.95]:
        th, P = 0.0, 100.0
        for k in range(400):
            truth = 1.0 if k < 200 else 2.0
            phi = rng.standard_normal()
            yk = truth * phi + 0.1 * rng.standard_normal()
            K = P * phi / (lam + phi * P * phi)
            th += K * (yk - phi * th)
            P = (P - K * phi * P) / lam
            if k in (199, 230, 399):
                print(f"forgetting {lam}: k={k + 1:3d} estimate {th:.3f} (true {truth})")


def e03_kalman_steady_state_and_duality():
    dt = 0.1
    A = np.array([[1, dt], [0, 1.0]]); H = np.array([[1.0, 0]])
    Qn = np.diag([0.0, 0.01]); Rn = np.array([[0.25]])
    # dual DARE: P = A P A^T - A P H^T (H P H^T + R)^-1 H P A^T + Q
    P = np.eye(2)
    for _ in range(5000):
        Pm = A @ P @ A.T + Qn
        K = Pm @ H.T @ np.linalg.inv(H @ Pm @ H.T + Rn)
        P = (np.eye(2) - K @ H) @ Pm
    # same answer from the control DARE on (A^T, H^T)
    Pc, _ = dare(A.T, H.T, Qn, Rn)
    Kd = Pc @ H.T @ np.linalg.inv(H @ Pc @ H.T + Rn)
    print("steady-state Kalman gain", K.ravel().round(4), "| from the dual LQR Riccati equation", Kd.ravel().round(4))
    print("steady-state position std", np.sqrt(P[0, 0]).round(4), "m vs measurement std 0.5 m")


def e04_e05_ekf_vs_ukf():
    # polar -> Cartesian: r ~ N(1, 0.02^2), theta ~ N(90 deg, sigma^2); y = r sin(theta)
    for sig_deg in [5.0, 15.0, 30.0]:
        st = np.deg2rad(sig_deg)
        mc_r = 1 + 0.02 * rng.standard_normal(1_000_000); mc_t = np.pi / 2 + st * rng.standard_normal(1_000_000)
        y_mc = (mc_r * np.sin(mc_t)).mean()
        y_lin = 1.0 * np.sin(np.pi / 2)  # linearization: f(mean)
        # unscented transform, n=2, alpha=1, beta=2, kappa=1  (lambda = alpha^2 (n+kappa) - n = 1)
        n, lam = 2, 1.0
        mean = np.array([1.0, np.pi / 2]); Pm = np.diag([0.02 ** 2, st ** 2])
        Sq = np.linalg.cholesky((n + lam) * Pm)
        pts = [mean] + [mean + Sq[:, i] for i in range(n)] + [mean - Sq[:, i] for i in range(n)]
        Wm = np.r_[lam / (n + lam), np.full(2 * n, 1 / (2 * (n + lam)))]
        y_ut = sum(w * p[0] * np.sin(p[1]) for w, p in zip(Wm, pts))
        print(f"bearing std {sig_deg:>4} deg: true mean y {y_mc:.4f} | EKF/linearized {y_lin:.4f} | UKF {y_ut:.4f} | analytic e^(-s^2/2) {np.exp(-st ** 2 / 2):.4f}")


def e06_particle_degeneracy():
    w = np.exp(-0.5 * ((rng.standard_normal(1000) * 3) ** 2)); w /= w.sum()
    print(f"1000 particles, sharp likelihood: effective sample size {1 / np.sum(w ** 2):.0f} -> resample when ESS < N/2")
    u = np.ones(1000) / 1000
    print(f"uniform weights: ESS {1 / np.sum(u ** 2):.0f}")


def e07_rts_smoother():
    # random walk x_k = x_{k-1} + w, z_k = x_k + v; filter vs RTS smoother variance in the middle of a 41-step window
    q, r, n = 0.01, 1.0, 41
    P = 1.0; Pf, Pp = [], []
    for k in range(n):
        Ppred = P + q if k else P
        K = Ppred / (Ppred + r); P = (1 - K) * Ppred
        Pp.append(Ppred); Pf.append(P)
    Ps = Pf[:]
    for k in range(n - 2, -1, -1):
        C = Pf[k] / Pp[k + 1]
        Ps[k] = Pf[k] + C ** 2 * (Ps[k + 1] - Pp[k + 1])
    m = n // 2
    print(f"step {m}: filter variance {Pf[m]:.4f}, RTS smoothed variance {Ps[m]:.4f} ({Pf[m] / Ps[m]:.2f}x smaller)")


def e08_consistency_tests():
    def chi2_quantile(p, k):  # Wilson-Hilferty approximation
        from math import sqrt
        z = {0.025: -1.95996, 0.975: 1.95996}[p]
        return k * (1 - 2 / (9 * k) + z * sqrt(2 / (9 * k))) ** 3
    k, N = 2, 50
    lo, hi = chi2_quantile(0.025, k * N) / N, chi2_quantile(0.975, k * N) / N
    print(f"average NIS over {N} steps of a 2-D measurement should lie in [{lo:.2f}, {hi:.2f}] (95%)")
    for scale, name in [(1.0, "correct R"), (0.25, "R 4x too small (overconfident)")]:
        nis = []
        for _ in range(N):
            nu = rng.standard_normal(2)
            nis.append(nu @ nu / scale)
        print(f"{name:32s}: average NIS {np.mean(nis):.2f} -> {'consistent' if lo <= np.mean(nis) <= hi else 'INCONSISTENT'}")


# ---------------- learning-based ----------------

def l01_sindy():
    # recover x' = -2 x + 0.5 x^3 from simulated data with sequential thresholded least squares
    dt = 0.001; t = np.arange(0, 2, dt)
    X = []
    for x0 in [-1.8, -1.0, 0.5, 1.5, 1.9]:
        x = x0; xs = []
        for _ in t:
            xs.append(x); x += dt * (-2 * x + 0.5 * x ** 3)
        X.append(np.array(xs))
    x = np.concatenate([xx[:-1] for xx in X]); dx = np.concatenate([np.diff(xx) / dt for xx in X])
    Theta = np.c_[np.ones_like(x), x, x ** 2, x ** 3, x ** 4, x ** 5]
    xi = np.linalg.lstsq(Theta, dx, rcond=None)[0]
    for _ in range(10):
        small = np.abs(xi) < 0.05; xi[small] = 0
        big = ~small; xi[big] = np.linalg.lstsq(Theta[:, big], dx, rcond=None)[0]
    print("SINDy library [1, x, x^2, x^3, x^4, x^5] coefficients:", xi.round(3), "(true 0, -2, 0, 0.5, 0, 0)")


def l02_learn_lqr_by_random_search():
    # scalar x+ = 1.1 x + u, cost sum x^2 + u^2; learn u = -k x by two-point random search (no model)
    a, b = 1.1, 1.0
    P = 1.0
    for _ in range(1000):
        P = 1 + a * a * P - (a * b * P) ** 2 / (1 + b * b * P)
    k_star = a * b * P / (1 + b * b * P)
    def J(k):
        x, c = 1.0, 0.0
        for _ in range(60):
            u = -k * x; c += x * x + u * u; x = a * x + b * u
        return c
    k, alpha, delta = 0.5, 0.02, 0.05
    for it in range(300):
        s = rng.choice([-1.0, 1.0])
        g = (J(k + delta * s) - J(k - delta * s)) / (2 * delta) * s
        k -= alpha * g
    print(f"Riccati optimal gain {k_star:.4f}; model-free random search after 300 iterations (600 rollouts) {k:.4f}")


def l03_deepc_prediction():
    # Willems' fundamental lemma: a Hankel matrix of one rich trajectory spans all trajectories of an unknown LTI system
    A = np.array([[0.9, 0.2], [-0.1, 0.8]]); B = np.array([0.0, 1.0]); C = np.array([1.0, 0.0])
    T = 120; L = 12; Tini = 4
    u = rng.standard_normal(T); x = np.zeros(2); y = []
    for k in range(T):
        y.append(C @ x); x = A @ x + B * u[k]
    y = np.array(y)
    Hu = np.array([u[i:i + L] for i in range(T - L + 1)]).T
    Hy = np.array([y[i:i + L] for i in range(T - L + 1)]).T
    # new experiment: past Tini samples + planned future input; predict future output from data only
    u_new = np.sin(0.3 * np.arange(L)); x = np.array([0.5, -0.3]); y_new = []
    for k in range(L):
        y_new.append(C @ x); x = A @ x + B * u_new[k]
    y_new = np.array(y_new)
    M = np.vstack([Hu, Hy[:Tini]])
    g = np.linalg.lstsq(M, np.r_[u_new, y_new[:Tini]], rcond=None)[0]
    y_pred = Hy[Tini:] @ g
    print(f"data-driven (Hankel) prediction of the next {L - Tini} outputs: max error {np.abs(y_pred - y_new[Tini:]).max():.2e} (no model identified)")


def l05_learned_kalman_gain():
    # learn a steady-state gain from (innovation -> state error) data, as KalmanNet-style learned gains do; compare with Riccati
    dt = 0.1
    A = np.array([[1, dt], [0, 1.0]]); H = np.array([[1.0, 0]]); Qn = np.diag([1e-4, 0.01]); Rn = 0.25
    P = np.eye(2)
    for _ in range(3000):
        Pm = A @ P @ A.T + Qn; K = Pm @ H.T / (H @ Pm @ H.T + Rn); P = (np.eye(2) - K @ H) @ Pm
    # generate training data with a decent prior estimator, then regress truth - prediction on innovation
    xs, xh = np.zeros(2), np.zeros(2); Xi, Er = [], []
    Kc = K.copy()
    for k in range(20000):
        xs = A @ xs + rng.multivariate_normal([0, 0], Qn)
        z = H @ xs + np.sqrt(Rn) * rng.standard_normal(1)
        pred = A @ xh
        nu = z - H @ pred
        Xi.append(nu[0]); Er.append(xs - pred)
        xh = pred + (Kc @ nu)
    Xi, Er = np.array(Xi), np.array(Er)
    K_learned = (Xi @ Er) / (Xi @ Xi)
    print("Riccati Kalman gain", K.ravel().round(4), "| gain learned by regression from data", K_learned.round(4))


RECIPES = {name: fn for name, fn in globals().items() if name[0] in "cel" and name[1:3].isdigit()}

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, fn in RECIPES.items():
        if pattern in name:
            print(f"\n=== {name} ===")
            fn()
