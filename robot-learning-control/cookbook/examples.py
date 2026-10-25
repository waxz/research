#!/usr/bin/env python3
"""Worked examples for the Control-to-Learning Math Cookbook.

Every number quoted in COOKBOOK.md under "Worked example" is produced by a
function in this file. Requires only NumPy.

    python3 examples.py          # run all recipes
    python3 examples.py lqr      # run the recipes whose name contains "lqr"
"""
import sys
import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(0)


def r04_gradient_descent_vs_newton():
    # f(x) = 0.5 x^T A x - b^T x, minimum at A^{-1} b
    A = np.array([[3.0, 0.5], [0.5, 1.0]])
    b = np.array([1.0, 2.0])
    x_star = np.linalg.solve(A, b)
    x = np.zeros(2)
    lr = 0.3
    for _ in range(50):
        x = x - lr * (A @ x - b)
    x_newton = np.zeros(2) - np.linalg.solve(A, A @ np.zeros(2) - b)
    print("x* =", x_star, "| GD after 50 steps =", x, "| Newton after 1 step =", x_newton)
    print("eigenvalues of A:", np.linalg.eigvalsh(A), "-> GD converges iff lr < 2/lambda_max =", 2 / np.linalg.eigvalsh(A).max())


def r05_discretize_double_integrator():
    dt = 0.1
    A = np.array([[0.0, 1.0], [0.0, 0.0]])
    B = np.array([[0.0], [1.0]])
    Ad_euler = np.eye(2) + dt * A
    Bd_euler = dt * B
    Ad_zoh = np.array([[1.0, dt], [0.0, 1.0]])
    Bd_zoh = np.array([[0.5 * dt**2], [dt]])
    print("Euler Ad =\n", Ad_euler, "\nEuler Bd =", Bd_euler.ravel())
    print("ZOH   Ad =\n", Ad_zoh, "\nZOH   Bd =", Bd_zoh.ravel())


def r06_pendulum_linearization():
    g, l = 9.81, 1.0
    # theta'' = -(g/l) sin(theta); state x = [theta, theta_dot]
    A_down = np.array([[0, 1], [-g / l, 0]])  # about theta = 0 (hanging)
    A_up = np.array([[0, 1], [g / l, 0]])     # about theta = pi (inverted)
    print("hanging eigenvalues:", np.linalg.eigvals(A_down), "(marginally stable, oscillates)")
    print("inverted eigenvalues:", np.linalg.eigvals(A_up), "(one positive -> unstable)")


def r07_pd_step_response():
    # unit inertia joint, tau = Kp (q_ref - q) - Kd q_dot
    for Kp, Kd in [(100.0, 20.0), (100.0, 5.0)]:
        wn, zeta = np.sqrt(Kp), Kd / (2 * np.sqrt(Kp))
        q, qd, dt, peak = 0.0, 0.0, 1e-3, 0.0
        for _ in range(3000):
            tau = Kp * (1.0 - q) - Kd * qd
            qd += dt * tau
            q += dt * qd
            peak = max(peak, q)
        print(f"Kp={Kp:.0f} Kd={Kd:.0f}: omega_n={wn:.1f} rad/s zeta={zeta:.2f} overshoot={max(0.0, 100 * (peak - 1)):.1f}%")


def dlqr(A, B, Q, R, iters=2000):
    P = Q.copy()
    for _ in range(iters):
        K = np.linalg.solve(R + B.T @ P @ B, B.T @ P @ A)
        P = Q + A.T @ P @ (A - B @ K)
    return K, P


def r08_lqr_double_integrator():
    dt = 0.1
    A = np.array([[1.0, dt], [0.0, 1.0]])
    B = np.array([[0.5 * dt**2], [dt]])
    Q = np.diag([1.0, 0.1])
    R = np.array([[0.01]])
    K, P = dlqr(A, B, Q, R)
    print("LQR gain K =", K.ravel(), "closed-loop eigenvalues:", np.linalg.eigvals(A - B @ K))
    x = np.array([1.0, 0.0])
    traj = []
    for k in range(30):
        u = -K @ x
        x = A @ x + B @ u
        traj.append(x[0])
    print("position after 1 s, 2 s, 3 s:", np.round([traj[9], traj[19], traj[29]], 4))


def r09_kalman_1d():
    # estimate a constant position 2.0 m from noisy measurements (std 0.5)
    x_true, R_meas, Q_proc = 2.0, 0.25, 1e-4
    x_hat, P = 0.0, 1.0
    zs = x_true + 0.5 * rng.standard_normal(20)
    for k, z in enumerate(zs):
        P = P + Q_proc
        K = P / (P + R_meas)
        x_hat = x_hat + K * (z - x_hat)
        P = (1 - K) * P
        if k in (0, 4, 19):
            print(f"after {k + 1:2d} measurements: x_hat={x_hat:.3f} P={P:.4f} K={K:.3f}")


def r10_friction_cone():
    mu = 0.6
    for f in [np.array([10.0, 0.0, 30.0]), np.array([25.0, 0.0, 30.0]), np.array([5.0, 0.0, -2.0])]:
        ok = f[2] >= 0 and np.hypot(f[0], f[1]) <= mu * f[2]
        print(f"contact force {f} -> {'inside' if ok else 'outside'} the friction cone (mu={mu})")


def r13_lipm_capture_point():
    g, z = 9.81, 0.8
    w = np.sqrt(g / z)
    for x, xd in [(0.0, 0.5), (0.05, 1.0)]:
        print(f"COM x={x} m, xdot={xd} m/s -> omega={w:.2f} 1/s, capture point = {x + xd / w:.3f} m")


def r14_least_squares():
    X = np.c_[np.ones(50), rng.uniform(-1, 1, 50)]
    w_true = np.array([0.5, -2.0])
    y = X @ w_true + 0.1 * rng.standard_normal(50)
    w_ls = np.linalg.solve(X.T @ X, X.T @ y)
    lam = 1.0
    w_ridge = np.linalg.solve(X.T @ X + lam * np.eye(2), X.T @ y)
    print("true w =", w_true, "least squares =", w_ls, "ridge(lambda=1) =", w_ridge)


def r15_bce():
    for p, y in [(0.9, 1), (0.6, 1), (0.1, 1), (0.1, 0)]:
        print(f"predicted p={p}, label y={y} -> BCE = {-(y * np.log(p) + (1 - y) * np.log(1 - p)):.3f}")


def r18_backprop_check():
    # 2-layer MLP, scalar output, squared loss; compare backprop to finite differences
    W1, b1 = rng.standard_normal((3, 2)), np.zeros(3)
    W2, b2 = rng.standard_normal((1, 3)), np.zeros(1)
    x, y = np.array([0.5, -1.0]), np.array([0.3])

    def loss(W1_):
        h = np.tanh(W1_ @ x + b1)
        return 0.5 * np.sum((W2 @ h + b2 - y) ** 2)

    z1 = W1 @ x + b1
    h = np.tanh(z1)
    yhat = W2 @ h + b2
    d_yhat = yhat - y
    d_h = W2.T @ d_yhat
    d_z1 = d_h * (1 - h**2)
    dW1 = np.outer(d_z1, x)
    eps, num = 1e-6, np.zeros_like(W1)
    for i in range(3):
        for j in range(2):
            E = np.zeros_like(W1); E[i, j] = eps
            num[i, j] = (loss(W1 + E) - loss(W1 - E)) / (2 * eps)
    print("max |backprop - finite difference| =", np.abs(dW1 - num).max())


def r19_adam_first_steps():
    # minimise f(x) = x^2 from x=1 with Adam (lr=0.1); first step size is ~lr regardless of gradient scale
    for scale in [1.0, 1000.0]:
        x, m, v, b1, b2, lr = 1.0, 0.0, 0.0, 0.9, 0.999, 0.1
        for t in range(1, 4):
            g = scale * 2 * x
            m = b1 * m + (1 - b1) * g
            v = b2 * v + (1 - b2) * g**2
            mh, vh = m / (1 - b1**t), v / (1 - b2**t)
            x -= lr * mh / (np.sqrt(vh) + 1e-8)
        print(f"gradient scale {scale:>6}: x after 3 Adam steps = {x:.4f}")


def r21_bptt_jacobian_products():
    for rho in [0.9, 1.0, 1.1]:
        print(f"spectral radius {rho}: gain after 8 steps {rho**8:.3f}, 32 steps {rho**32:.3f}, 128 steps {rho**128:.3g}")


def r23_effective_horizon():
    for gamma, hz in [(0.99, 50), (0.95, 50), (0.999, 1000)]:
        n = 1 / (1 - gamma)
        print(f"gamma={gamma}: effective horizon {n:.0f} steps = {n / hz:.2f} s at {hz} Hz")


def r24_value_iteration_chain():
    # 5-state chain, actions left/right, reward 1 on entering the rightmost state, gamma 0.9
    n, gamma = 5, 0.9
    V = np.zeros(n)
    for _ in range(100):
        Vn = np.zeros(n)
        for s in range(n):
            if s == n - 1:
                continue  # terminal
            q = []
            for a in (-1, 1):
                s2 = min(max(s + a, 0), n - 1)
                r = 1.0 if s2 == n - 1 else 0.0
                q.append(r + gamma * (0 if s2 == n - 1 else V[s2]))
            Vn[s] = max(q)
        V = Vn
    print("V* =", V, "(equals gamma^(distance-1))")


def r26_score_vs_pathwise():
    # J(theta) = E_{a ~ N(theta, sigma^2)} [ -(a - 2)^2 ];  true gradient = -2 (theta - 2)
    theta, sigma, N = 0.0, 0.5, 100_000
    eps = rng.standard_normal(N)
    a = theta + sigma * eps
    f = -(a - 2) ** 2
    score = (a - theta) / sigma**2 * f
    score_b = (a - theta) / sigma**2 * (f - f.mean())
    pathwise = -2 * (a - 2)
    print(f"true gradient {-2 * (theta - 2):.3f}")
    for name, g in [("score function", score), ("score + baseline", score_b), ("pathwise", pathwise)]:
        print(f"  {name:17s} mean {g.mean():7.3f}  per-sample std {g.std():7.3f}")


def r27_gae():
    gamma, lam = 0.99, 0.95
    r = np.array([1.0, 1.0, 1.0, 0.0])
    V = np.array([2.5, 2.0, 1.2, 0.5, 0.0])  # V(s_0..s_4), s_4 terminal
    delta = r + gamma * V[1:] - V[:-1]
    A = np.zeros(4)
    run = 0.0
    for t in reversed(range(4)):
        run = delta[t] + gamma * lam * run
        A[t] = run
    print("TD errors delta =", delta)
    print("GAE advantages  =", A)


def r28_ppo_clip():
    eps = 0.2
    for ratio, adv in [(1.1, 1.0), (1.5, 1.0), (0.5, 1.0), (0.5, -1.0), (1.5, -1.0)]:
        obj = min(ratio * adv, np.clip(ratio, 1 - eps, 1 + eps) * adv)
        grad = "zero (clipped)" if obj != ratio * adv else "passes"
        print(f"ratio={ratio}, A={adv:+.0f}: objective {obj:+.2f}, gradient {grad}")


def r32_bc_vs_dagger_bound():
    eps = 0.01
    for T in [50, 500]:
        print(f"T={T}, per-step error {eps}: BC bound ~ T^2 eps = {T**2 * eps:.0f}, DAgger bound ~ T eps = {T * eps:.1f}")


def r35_rotation_error():
    def rotz(a):
        c, s = np.cos(a), np.sin(a)
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    R_des, R = rotz(np.deg2rad(30)), rotz(np.deg2rad(10))
    E = R_des @ R.T
    angle = np.arccos(np.clip((np.trace(E) - 1) / 2, -1, 1))
    print(f"||log(R_des R^T)|| = {angle:.4f} rad = {np.rad2deg(angle):.1f} deg")


def r36_tracking_reward():
    for err, sigma in [(0.05, 0.3), (0.15, 0.3), (0.30, 0.3), (0.60, 0.3)]:
        print(f"position error {err} m, sigma {sigma} m -> reward {np.exp(-err**2 / sigma**2):.3f}")


def r38_return_based_reset():
    G = np.array([0.95, 0.90, 0.40, 0.92])  # normalized discounted return per motion bin
    w_soft = np.exp(-25 * G); w_soft /= w_soft.sum()
    p = 0.5 * np.full(4, 0.25) + 0.4 * w_soft + 0.1 * np.full(4, 0.25)  # last term: historical weights, uniform here
    print("bin returns", G, "-> reset probabilities", p)


RECIPES = {name: fn for name, fn in globals().items() if name.startswith("r") and name[1:3].isdigit()}

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, fn in RECIPES.items():
        if pattern in name:
            print(f"\n=== {name} ===")
            fn()
