#!/usr/bin/env python3
"""Worked examples for the Stability Analysis Cookbook.

Every number quoted under "Worked example" in COOKBOOK.md comes from a function
here. Requires only NumPy.

    python3 examples.py          # run all recipes
    python3 examples.py s05      # run recipes whose name contains "s05"
"""
import sys

import numpy as np

np.set_printoptions(precision=4, suppress=True)


def rk4(f, x, dt):
    k1 = f(x); k2 = f(x + dt / 2 * k1); k3 = f(x + dt / 2 * k2); k4 = f(x + dt * k3)
    return x + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def lyap(A, Q):
    """Solve A^T P + P A = -Q by vectorisation (fine for small systems)."""
    n = A.shape[0]
    M = np.kron(np.eye(n), A.T) + np.kron(A.T, np.eye(n))
    return np.linalg.solve(M, -Q.reshape(-1)).reshape(n, n)


# ------------------------------------------------------------------ classical
def s01_linearization():
    m, l, g, b = 1.0, 1.0, 9.81, 0.1          # inverted pendulum, upright is theta = 0
    for kp, kd in [(5.0, 2.0), (20.0, 5.0)]:
        A = np.array([[0, 1], [g / l - kp / (m * l * l), -(b + kd) / (m * l * l)]])
        eig = np.linalg.eigvals(A)
        c1, c0 = (b + kd) / (m * l * l), kp / (m * l * l) - g / l   # s^2 + c1 s + c0
        print(f"Kp={kp:4.1f} Kd={kd:3.1f}: eigenvalues {np.round(eig, 3)} -> "
              f"{'stable' if eig.real.max() < 0 else 'UNSTABLE'}; Routh coefficients c1={c1:.2f}, c0={c0:.2f}")


def s02_lyapunov_equation():
    m, l, g, b, kp, kd = 1.0, 1.0, 9.81, 0.1, 20.0, 5.0
    A = np.array([[0, 1], [g / l - kp, -(b + kd)]])
    P = lyap(A, np.eye(2))
    lp = np.linalg.eigvalsh(P)
    rate = 1 / lp.max()           # dV/dt = -x^T x <= -(1/lambda_max(P)) V
    print("P =", np.round(P, 4).tolist(), f" eigenvalues {np.round(lp, 4)} (positive -> V = x^T P x is a Lyapunov function)")
    print(f"guaranteed decay: V(t) <= V(0) exp(-{rate:.3f} t), so |x| decays at least as exp(-{rate/2:.3f} t);"
          f" true slowest rate {-np.linalg.eigvals(A).real.max():.3f}")


def s03_lasalle():
    m, l, g, b = 1.0, 1.0, 9.81, 0.5           # hanging damped pendulum
    f = lambda x: np.array([x[1], -g / l * np.sin(x[0]) - b / (m * l * l) * x[1]])
    E = lambda x: 0.5 * m * l * l * x[1] ** 2 + m * g * l * (1 - np.cos(x[0]))
    x, dt, Es = np.array([2.5, 0.0]), 1e-3, []
    for _ in range(20000):
        Es.append(E(x)); x = rk4(f, x, dt)
    Es = np.array(Es)
    print(f"energy: {Es[0]:.3f} -> {Es[-1]:.2e} J over 20 s; never increases: {bool(np.all(np.diff(Es) <= 1e-12))}")
    print(f"dE/dt = -b*omega^2 is zero whenever omega = 0, yet LaSalle gives convergence: final state {np.round(x, 5)}")


def s04_region_of_attraction():
    # reversed-time Van der Pol: stable origin, region of attraction bounded by an unstable limit cycle
    f = lambda x: np.array([-x[1], x[0] + (x[0] ** 2 - 1) * x[1]])
    A = np.array([[0.0, -1.0], [1.0, -1.0]])
    P = lyap(A, np.eye(2))
    xs = np.linspace(-3, 3, 241)
    X1, X2 = np.meshgrid(xs, xs)
    pts = np.stack([X1.ravel(), X2.ravel()], 1)
    V = np.einsum("ni,ij,nj->n", pts, P, pts)
    F = np.stack([-pts[:, 1], pts[:, 0] + (pts[:, 0] ** 2 - 1) * pts[:, 1]], 1)
    Vdot = 2 * np.einsum("ni,ij,nj->n", pts, P, F)
    bad = (Vdot >= 0) & (np.linalg.norm(pts, axis=1) > 1e-6)
    c = V[bad].min()                                  # largest level set with dV/dt < 0 inside
    est = V < c
    conv = np.zeros(len(pts), bool)                   # true region of attraction by simulation
    x = pts.T.copy()
    for _ in range(1500):
        k1 = np.array(f(x)); k2 = np.array(f(x + 0.005 * k1)); k3 = np.array(f(x + 0.005 * k2)); k4 = np.array(f(x + 0.01 * k3))
        x = x + 0.01 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x = np.clip(x, -50, 50)
    conv = np.linalg.norm(x, axis=0) < 1e-2
    cell = (xs[1] - xs[0]) ** 2
    print(f"quadratic Lyapunov estimate: V < {c:.3f}; area {est.sum()*cell:.2f}; all its points converge: {bool(conv[est].all())}")
    print(f"true region of attraction (simulated) area {conv.sum()*cell:.2f}: the estimate covers {est.sum()/conv.sum():.0%} of it")


def s05_margins_and_delay():
    J, b, kp, kd = 0.01, 0.05, 10.0, 0.3              # joint: J qdd + b qd = tau, PD feedback
    w = np.logspace(-1, 4, 200000)
    L = (kd * 1j * w + kp) / (J * (1j * w) ** 2 + b * 1j * w)
    i = np.argmin(np.abs(np.abs(L) - 1))
    wc, pm = w[i], np.pi + np.angle(L[i])
    td = pm / wc
    print(f"crossover {wc:.1f} rad/s, phase margin {np.degrees(pm):.1f} deg, delay margin PM/wc = {1e3*td:.2f} ms")

    for frac in [0.8, 1.2]:
        dly = frac * td
        dt, T = 1e-5, 1.5
        d = int(round(dly / dt))
        qh, vh = [0.0] * (d + 1), [0.0] * (d + 1)
        q = v = 0.0
        late = 0.0
        for k in range(int(T / dt)):
            tau = kp * (0.1 - qh[0]) - kd * vh[0]   # controller sees measurements `delay` old
            v += (tau - b * v) / J * dt; q += v * dt
            qh.append(q); qh.pop(0); vh.append(v); vh.pop(0)
            if k * dt > T - 0.3:
                late = max(late, abs(q - 0.1))
        print(f"  simulated with delay {1e3*dly:.2f} ms ({frac:.1f} x margin): error in last 0.3 s {late:.2e} rad "
              f"-> {'settles' if late < 1e-3 else 'OSCILLATES / DIVERGES'}")


# ------------------------------------------------------------------ robust and nonlinear
def s06_circle_criterion():
    w = np.logspace(-3, 3, 400000)
    G1 = 1 / ((1j * w + 1) * (1j * w + 2) * (1j * w + 3))
    kmax_circle = -1 / G1.real.min()        # sector [0,1] nonlinearity (saturation): need Re K*G1 > -1
    kmax_linear = 60.0                        # Routh: s^3 + 6 s^2 + 11 s + 6 + K stable for K < 60
    # Popov: exists q >= 0 with Re[(1 + j w q) K G1] > -1 for all w; search q on a grid
    best = 0.0
    for q in np.linspace(0, 5, 501):
        m = ((1 + 1j * w * q) * G1).real.min()
        best = max(best, -1 / m if m < 0 else np.inf)
    print(f"loop gain K with a saturation (sector [0,1]): circle criterion certifies K < {kmax_circle:.1f}; "
          f"Popov certifies K < {min(best, kmax_linear):.1f}; the linear loop is stable for K < {kmax_linear:.0f}")

    def sat_loop(K, x0, T=150.0, dt=1e-3):
        A = np.array([[0, 1, 0], [0, 0, 1], [-6, -11, -6]], float); B = np.array([0, 0, 1.0])
        x = np.array(x0, float)
        for _ in range(int(T / dt)):
            y = x[0]; u = -K * np.clip(y, -1, 1)
            x = x + dt * (A @ x + B * u)
        return np.abs(x).max()
    for K in [kmax_circle * 0.95, 50.0]:
        print(f"  K={K:5.1f}, large initial state: final |x| {sat_loop(K, [5, 0, 0]):.2e}")


def s07_describing_function():
    K, M = 6.0, 1.0                            # relay of height M in feedback with K / (s (s+1) (s+2))
    w180 = np.sqrt(2.0)
    gain = K / (w180 * np.sqrt(w180 ** 2 + 1) * np.sqrt(w180 ** 2 + 4))
    A_pred, T_pred = 4 * M * gain / np.pi, 2 * np.pi / w180
    print(f"describing function predicts a limit cycle: amplitude {A_pred:.3f}, period {T_pred:.3f} s")
    A = np.array([[0, 1, 0], [0, 0, 1], [0, -2, -3]], float); B = np.array([0, 0, K])
    x, dt, ys = np.array([0.1, 0, 0]), 1e-4, []
    for _ in range(int(60 / dt)):
        u = -M * np.sign(x[0])
        x = x + dt * (A @ x + B * u); ys.append(x[0])
    y = np.array(ys[int(40 / dt):])
    zc = np.where((y[:-1] < 0) & (y[1:] >= 0))[0]
    print(f"simulation: amplitude {y.max():.3f}, period {np.diff(zc).mean()*dt:.3f} s")


def _arm(q, dq, tau):
    # planar two-link arm, unit masses at link ends, lengths 1, gravity in -y
    m1 = m2 = 1.0; l1 = l2 = 1.0; g = 9.81
    c2, s2 = np.cos(q[1]), np.sin(q[1])
    M = np.array([[(m1 + m2) * l1 ** 2 + m2 * l2 ** 2 + 2 * m2 * l1 * l2 * c2, m2 * l2 ** 2 + m2 * l1 * l2 * c2],
                  [m2 * l2 ** 2 + m2 * l1 * l2 * c2, m2 * l2 ** 2]])
    h = m2 * l1 * l2 * s2
    C = np.array([[-h * dq[1], -h * (dq[0] + dq[1])], [h * dq[0], 0.0]])
    G = np.array([(m1 + m2) * g * l1 * np.cos(q[0]) + m2 * g * l2 * np.cos(q[0] + q[1]), m2 * g * l2 * np.cos(q[0] + q[1])])
    return M, C, G


def s08_passivity_pd_gravity():
    qd = np.array([0.8, -0.5]); Kp, Kd = np.diag([60.0, 40.0]), np.diag([12.0, 8.0])
    for comp in [True, False]:
        q, dq, dt, Vs = np.zeros(2), np.zeros(2), 1e-3, []
        for _ in range(8000):
            M, C, G = _arm(q, dq, None)
            e = q - qd
            tau = -Kp @ e - Kd @ dq + (G if comp else 0)
            ddq = np.linalg.solve(M, tau - C @ dq - G)
            if comp:
                Vs.append(0.5 * dq @ M @ dq + 0.5 * e @ Kp @ e)
            dq = dq + dt * ddq; q = q + dt * dq
        msg = f"with gravity compensation: V falls {Vs[0]:.2f} -> {Vs[-1]:.1e}, never rises by more than {max(np.diff(Vs).max(), 0):.1e} (integration error)" if comp else "without gravity compensation"
        print(f"{msg}; final joint error {np.round(q - qd, 4)} rad")


def s09_iss_bounded_residual():
    J, kp, kd = 0.01, 10.0, 0.3
    A = np.array([[0, 1], [-kp / J, -kd / J]]); B = np.array([0, 1 / J])
    P = lyap(A, np.eye(2)); lmin, lmax = np.linalg.eigvalsh(P)[[0, -1]]
    theta = 0.99
    dt = 1e-5
    t = np.arange(0, 3.0, dt)                  # impulse response from residual torque to joint error
    x, hs = B.copy(), []
    for _ in t:
        hs.append(x[0]); x = x + dt * (A @ x)
    hs = np.array(hs)
    l1 = np.abs(hs).sum() * dt                  # peak-to-peak gain: exact worst case for |r| <= delta
    for delta in [0.05, 0.2]:                   # residual torque bound (N m)
        ub = 2 * np.linalg.norm(P @ B) * delta / theta * np.sqrt(lmax / lmin)
        # worst-case residual: r(t) = delta * sign(h(T - t)) drives e(T) to l1 * delta
        r = delta * np.sign(hs[::-1])
        x, worst = np.zeros(2), 0.0
        for rk in r:
            x = x + dt * (A @ x + B * rk); worst = max(worst, abs(x[0]))
        print(f"|residual| <= {delta:.2f} N m: Lyapunov (ISS) bound on |e| {ub:.3f} rad; "
              f"tight L1 bound {l1*delta:.4f} rad; worst-case residual reaches {worst:.4f} rad")
    print("both bounds grow linearly with delta: an unbounded residual gives no bound on the error")


def s10_small_gain_lipschitz():
    rng = np.random.default_rng(3)
    W1, W2 = rng.normal(0, 0.5, (32, 1)), rng.normal(0, 0.5, (1, 32))
    phi = lambda y: W2 @ np.maximum(W1 @ y, 0)
    L_upper = np.linalg.norm(W1, 2) * np.linalg.norm(W2, 2)       # product of spectral norms
    ys = np.linspace(-5, 5, 200001)[None, :]
    out = phi(ys)[0]
    L_emp = np.abs(np.diff(out) / np.diff(ys[0])).max()
    w = np.logspace(-3, 3, 100000)
    for a in [20.0, 5.0]:
        Pinf = np.abs(1 / (1j * w + a)).max()
        print(f"plant 1/(s+{a:.0f}): H-inf norm {Pinf:.2f}; NN Lipschitz bound {L_upper:.2f} (true {L_emp:.2f}); "
              f"small-gain product {Pinf*L_upper:.2f} -> {'certified stable' if Pinf*L_upper < 1 else 'NOT certified'}"
              f" (with the true constant {Pinf*L_emp:.2f})")


# ------------------------------------------------------------------ CLF, CBF, hybrid
def s11_clf_sontag():
    P = np.array([[np.sqrt(3), 1], [1, np.sqrt(3)]])       # LQR Riccati solution for x1'=x2, x2'=u, Q=I, R=1
    K = np.array([1.0, np.sqrt(3)])
    def sontag(x):
        a = 2 * x @ P @ np.array([x[1], 0.0]); bb = 2 * (x @ P)[1]
        return 0.0 if abs(bb) < 1e-12 else -(a + np.sqrt(a * a + bb ** 4)) / bb
    for name, law in [("LQR u=-Kx", lambda x: -K @ x), ("Sontag formula", sontag)]:
        x, dt, t, umax = np.array([1.0, 0.0]), 1e-3, None, 0.0
        for k in range(int(20 / dt)):
            u = law(x); umax = max(umax, abs(u))
            x = x + dt * np.array([x[1], u])
            if t is None and np.linalg.norm(x) < 0.01:
                t = k * dt
        print(f"{name:15s}: |x| < 0.01 after {t:.2f} s, peak |u| {umax:.2f}")


def s12_cbf_joint_limit():
    qmax, a1, a2 = 1.0, 5.0, 5.0              # joint q'' = u, limit q <= qmax
    kp, kd, target = 100.0, 10.0, 1.5         # nominal controller drives past the limit
    for filt in [False, True]:
        q, v, dt, peak, active = 0.0, 0.0, 1e-4, 0.0, 0
        for _ in range(int(3 / dt)):
            u = kp * (target - q) - kd * v
            if filt:
                ubar = -(a1 + a2) * v + a1 * a2 * (qmax - q)   # second-order CBF: h'' + (a1+a2) h' + a1 a2 h >= 0
                if u > ubar:
                    u, active = ubar, active + 1
            v += u * dt; q += v * dt; peak = max(peak, q)
        print(f"{'with CBF filter' if filt else 'nominal PD     '}: peak q = {peak:.4f} (limit {qmax}); "
              f"filter active {active*dt:.2f} s of 3 s" if filt else f"nominal PD     : peak q = {peak:.4f} (limit {qmax})")


def s13_poincare_rimless_wheel():
    g, l, alpha, gamma = 9.81, 1.0, np.pi / 8, 0.08
    c = np.cos(2 * alpha) ** 2
    k = 4 * g / l * np.sin(alpha) * np.sin(gamma)
    step = lambda w: np.sqrt(c * w * w + k)              # pre-impact speed to next pre-impact speed
    w_star = np.sqrt(k / (1 - c))
    slope = c * w_star / step(w_star)                    # derivative of the Poincare map at the fixed point
    w_min = np.sqrt(2 * g / l * (1 - np.cos(alpha - gamma)))   # post-impact speed needed to vault over
    print(f"fixed point omega* = {w_star:.3f} rad/s; map slope {slope:.3f} (< 1: stable gait); "
          f"post-impact speed {np.sqrt(c)*w_star:.3f} > {w_min:.3f} needed to keep rolling")
    for w0 in [0.6, 3.0]:
        w = [w0]
        for _ in range(8):
            w.append(step(w[-1]))
        print(f"  start {w0:.1f} rad/s -> {np.round(w[1:6], 3)} ...")


def s14_contraction():
    rng = np.random.default_rng(5)
    W0 = rng.normal(0, 1, (4, 4))
    cases = [("random W, ||W|| = 0.6", W0 / np.linalg.norm(W0, 2) * 0.6), ("W = 2.5 I", 2.5 * np.eye(4))]
    for name, W in cases:
        f = lambda x, t: -x + np.tanh(W @ x) + np.array([0.3 * np.sin(t), 0, 0, 0])
        xa, xb, dt = np.array([2.0, 1.0, -1.0, 0.5]), np.array([-2.0, -1.0, 1.0, -0.5]), 1e-3
        d0 = np.linalg.norm(xa - xb)
        for k in range(int(10 / dt)):
            t = k * dt
            xa = xa + dt * f(xa, t); xb = xb + dt * f(xb, t)
        rate = 1 - np.linalg.norm(W, 2)
        print(f"{name}: contraction rate bound {rate:+.1f}; distance between two trajectories "
              f"{d0:.2f} -> {np.linalg.norm(xa-xb):.2e} after 10 s"
              + (f" (guaranteed <= {d0*np.exp(-rate*10):.2e})" if rate > 0 else " (not contracting: two stable states)"))


# ------------------------------------------------------------------ learning and verification
def s15_learned_lyapunov_cegis():
    """Learner + falsifier: fit V = mu|x|^2 + |L^T z(x)|^2 so that dV/dt <= -eps V on [-2,2]^2."""
    f = lambda X: np.stack([X[:, 1], -np.sin(X[:, 0]) - X[:, 1]], 1)         # damped pendulum
    def feats(X):
        x1, x2 = X[:, 0], X[:, 1]
        z = np.stack([x1, x2, x1 * x1, x1 * x2, x2 * x2], 1)
        J = np.zeros((len(X), 5, 2))
        J[:, 0, 0] = 1; J[:, 1, 1] = 1; J[:, 2, 0] = 2 * x1; J[:, 3, 0] = x2; J[:, 3, 1] = x1; J[:, 4, 1] = 2 * x2
        return z, J
    mu, eps = 0.1, 0.05
    def vdot_terms(L, X):
        z, J = feats(X); F = f(X)
        g = np.einsum("nij,nj->ni", J, F)
        Lz, Lg = z @ L, g @ L
        V = mu * (X * X).sum(1) + (Lz * Lz).sum(1)
        Vd = 2 * mu * (X * F).sum(1) + 2 * (Lz * Lg).sum(1)
        return V, Vd, z, g
    rng = np.random.default_rng(0)
    L = rng.normal(0, 0.3, (5, 5))
    train = rng.uniform(-2, 2, (400, 2))
    g1 = np.linspace(-2, 2, 161); G = np.stack(np.meshgrid(g1, g1), -1).reshape(-1, 2)
    G = G[np.linalg.norm(G, axis=1) > 0.05]
    for rnd in range(30):
        for _ in range(300):                                      # learner: hinge loss on the samples
            V, Vd, z, g = vdot_terms(L, train)
            viol = Vd + eps * V
            act = viol > -1e-3
            if not act.any():
                break
            zA, gA = z[act], g[act]
            grad = 2 * (np.einsum("ni,nj->ij", zA, gA @ L) + np.einsum("ni,nj->ij", gA, zA @ L)) + 2 * eps * np.einsum("ni,nj->ij", zA, zA @ L)
            L -= 0.02 * grad / len(train)
        V, Vd, _, _ = vdot_terms(L, G)                            # falsifier: dense grid search
        cex = G[Vd + eps * V > 0]
        if len(cex) == 0:
            break
        train = np.vstack([train, cex[rng.choice(len(cex), min(50, len(cex)), replace=False)]])
    print(f"CEGIS rounds: {rnd+1}; training points {len(train)}; grid counterexamples left: {len(cex)}")
    print(f"a plain quadratic V = |x|^2 violates dV/dt <= -{eps}V at {(2*(G*f(G)).sum(1) + eps*(G*G).sum(1) > 0).mean():.0%} of the grid")
    print("note: a grid check is a falsifier, not a proof; S16 shows how bounds make it rigorous")


def s16_interval_bound_propagation():
    rng = np.random.default_rng(1)
    Ws = [rng.normal(0, 0.8, (16, 2)), rng.normal(0, 0.5, (16, 16)), rng.normal(0, 0.5, (1, 16))]
    bs = [rng.normal(0, 0.1, 16), rng.normal(0, 0.1, 16), np.zeros(1)]
    def net(X):
        h = X
        for i, (W, b) in enumerate(zip(Ws, bs)):
            h = h @ W.T + b
            if i < 2:
                h = np.maximum(h, 0)
        return h[:, 0]
    def ibp(lo, hi):
        for i, (W, b) in enumerate(zip(Ws, bs)):
            c, r = (lo + hi) / 2, (hi - lo) / 2
            c, r = W @ c + b, np.abs(W) @ r
            lo, hi = c - r, c + r
            if i < 2:
                lo, hi = np.maximum(lo, 0), np.maximum(hi, 0)
        return lo[0], hi[0]
    S = rng.uniform(-1, 1, (200000, 2)); y = net(S)
    print(f"sampled controller output on [-1,1]^2: [{y.min():.3f}, {y.max():.3f}]")
    for n in [1, 4, 16, 64]:
        e = np.linspace(-1, 1, n + 1); lo_all, hi_all = np.inf, -np.inf
        for i in range(n):
            for j in range(n):
                lo, hi = ibp(np.array([e[i], e[j]]), np.array([e[i + 1], e[j + 1]]))
                lo_all, hi_all = min(lo_all, lo), max(hi_all, hi)
        print(f"  interval bounds with {n*n:4d} boxes: [{lo_all:.3f}, {hi_all:.3f}] (width {hi_all-lo_all:.3f})")


STEP = 6.0  # deliberately large normalised step on the gain matrix


def s17_lyapunov_safe_policy_update():
    A = np.array([[1.0, 0.1], [0.0, 1.0]]); B = np.array([[0.0], [0.1]])  # discrete double integrator
    Q, R = np.eye(2), np.array([[0.1]])
    def cost(K):
        Acl = A - B @ K
        if max(abs(np.linalg.eigvals(Acl))) >= 1:
            return np.inf
        Pk = np.eye(2)
        for _ in range(3000):                    # cost-to-go matrix: Pk = Q + K'RK + Acl' Pk Acl
            Pk = Q + K.T @ R @ K + Acl.T @ Pk @ Acl
        return np.trace(Pk)
    def grad(K, h=1e-5):
        g = np.zeros_like(K)
        for i in range(K.size):
            d = np.zeros_like(K); d.flat[i] = h
            g.flat[i] = (cost(K + d) - cost(K - d)) / (2 * h)
        return g
    for safe in [False, True]:
        K, unstable, rejected, first = np.array([[1.0, 1.5]]), 0, 0, None
        for it in range(25):
            g = grad(K); step = STEP
            Kn = K - step * g / max(np.linalg.norm(g), 1e-9)
            if safe:                             # accept only if the new closed loop keeps a Lyapunov decrease
                while max(abs(np.linalg.eigvals(A - B @ Kn))) >= 1 or cost(Kn) > cost(K):
                    step /= 2; rejected += 1
                    Kn = K - step * g / max(np.linalg.norm(g), 1e-9)
            if max(abs(np.linalg.eigvals(A - B @ Kn))) >= 1:
                unstable += 1; first = first or it + 1
            K = Kn if np.isfinite(cost(Kn)) or not safe else K
            if not np.isfinite(cost(K)):
                break
        print(f"{'Lyapunov-checked steps' if safe else 'plain gradient steps  '}: "
              + (f"closed loop went UNSTABLE at step {first} (spectral radius >= 1)" if unstable else f"stable throughout, final cost {cost(K):.3f}")
              + (f"; steps shortened {rejected} times" if safe else ""))


RECIPES = {name: fn for name, fn in globals().items() if name.startswith("s") and name[1:3].isdigit()}

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, fn in RECIPES.items():
        if pattern in name:
            print(f"\n=== {name} ===")
            fn()
