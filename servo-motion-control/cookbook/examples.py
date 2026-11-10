#!/usr/bin/env python3
"""Worked examples for the Servo and Motion Control Cookbook.

Every number quoted under "Worked example" in COOKBOOK.md comes from a function
here. Requires only NumPy.

    python3 examples.py          # run all recipes
    python3 examples.py v09      # run recipes whose name contains "v09"
"""
import sys

import numpy as np

np.set_printoptions(precision=4, suppress=True)

def expm(M):
    """Matrix exponential by scaling and squaring with a Taylor series (NumPy only)."""
    n = max(0, int(np.ceil(np.log2(max(np.abs(M).sum(1).max(), 1e-16)))) + 1)
    A = M / 2 ** n; E = np.eye(len(M)); T = np.eye(len(M))
    for k in range(1, 20):
        T = T @ A / k; E = E + T
    for _ in range(n):
        E = E @ E
    return E


def c2d(A, B, dt):
    """Exact zero-order-hold discretization."""
    n, m = A.shape[0], B.shape[1]
    M = np.zeros((n + m, n + m)); M[:n, :n] = A; M[:n, n:] = B
    E = expm(M * dt)
    return E[:n, :n], E[:n, n:]


# a small surface-mounted PMSM used in Part I
PM = dict(R=0.2, L=0.5e-3, lam=0.01, p=7, Vdc=48.0)


# ================================================================== I. inside the drive: FOC
def v01_dq_current_decoupling():
    R, L, lam, p = PM["R"], PM["L"], PM["lam"], PM["p"]
    we = p * 300.0                               # 300 rad/s mechanical, 2100 rad/s electrical
    fs = 20e3; Ts = 1 / fs; wc = 2 * np.pi * 500
    kp, ki = L * wc, R * wc
    for decouple in [False, True]:
        idq = np.zeros(2); integ = np.zeros(2); hist = [np.zeros(2)]
        ref = np.array([0.0, 10.0]); peak_id = 0.0; t_iq = None
        sub = 20; dt = Ts / sub
        for k in range(int(0.02 / Ts)):
            e = ref - idq; integ += e * Ts
            v = kp * e + ki * integ
            if decouple:                           # cancel the cross-coupling and back-EMF terms
                v += np.array([-we * L * idq[1], we * L * idq[0] + we * lam])
            hist.append(v); va = hist.pop(0)       # one-sample computation delay
            for _ in range(sub):
                did = (va[0] - R * idq[0] + we * L * idq[1]) / L
                diq = (va[1] - R * idq[1] - we * L * idq[0] - we * lam) / L
                idq += dt * np.array([did, diq])
            peak_id = max(peak_id, abs(idq[0]))
            if t_iq is None and idq[1] > 9.0:
                t_iq = (k + 1) * Ts
        print(f"{'with decoupling feedforward' if decouple else 'PI only                    '}: peak |id| {peak_id:5.2f} A during a 10 A iq step at 2100 rad/s electrical; "
              f"iq reaches 90% after {t_iq*1e3:.2f} ms")


def v02_voltage_limit_svpwm():
    R, L, lam, p, Vdc = PM["R"], PM["L"], PM["lam"], PM["p"], PM["Vdc"]
    iq = 15.0
    for name, vmax in [("sine PWM", Vdc / 2), ("space-vector PWM", Vdc / np.sqrt(3))]:
        # |v|^2 = (R iq + we lam)^2 + (we L iq)^2 = vmax^2, solve for we
        a = lam ** 2 + (L * iq) ** 2; b = 2 * R * iq * lam; c = (R * iq) ** 2 - vmax ** 2
        we = (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
        print(f"{name:16s}: peak phase voltage {vmax:5.2f} V -> base speed at {iq:.0f} A: {we/p:6.0f} rad/s mechanical "
              f"({we/p*60/2/np.pi:5.0f} rpm)")
    print(f"space-vector PWM gives {2/np.sqrt(3)-1:.1%} more voltage, and so more speed, from the same DC bus")


def v03_field_weakening_mtpa():
    L, lam, p, Vdc = PM["L"], PM["lam"], PM["p"], PM["Vdc"]
    Imax, Vmax = 20.0, Vdc / np.sqrt(3)
    def max_torque(wm, fw):
        we = p * wm; best = 0.0
        for idv in (np.linspace(-Imax, 0, 401) if fw else [0.0]):
            iq_lim_I = np.sqrt(max(Imax ** 2 - idv ** 2, 0))
            # voltage circle (R neglected): (lam + L id)^2 + (L iq)^2 <= (Vmax/we)^2
            rhs = (Vmax / we) ** 2 - (lam + L * idv) ** 2
            if rhs < 0:
                continue
            iq = min(iq_lim_I, np.sqrt(rhs) / L)
            best = max(best, 1.5 * p * lam * iq)
        return best
    for wm in [200, 400, 600, 800]:
        print(f"  {wm:3d} rad/s: max torque {max_torque(wm, False):.2f} N m with id = 0, {max_torque(wm, True):.2f} N m with field weakening")
    Ld, Lq, lam2 = 0.3e-3, 0.6e-3, 0.01        # interior-magnet motor: reluctance torque available
    I = 20.0; ang = np.linspace(0, np.pi / 2, 9001)
    idv, iqv = -I * np.sin(ang), I * np.cos(ang)
    T = 1.5 * p * (lam2 * iqv + (Ld - Lq) * idv * iqv)
    i = np.argmax(T)
    print(f"interior-magnet motor at {I:.0f} A: id = 0 gives {T[0]:.3f} N m; MTPA (current angle {np.degrees(ang[i]):.1f} deg, "
          f"id {idv[i]:.1f} A) gives {T[i]:.3f} N m (+{T[i]/T[0]-1:.1%})")


def v04_dead_time():
    Vdc, f, td, R, L = PM["Vdc"], 20e3, 1e-6, PM["R"], PM["L"]
    dV = Vdc * td * f
    print(f"dead time 1 us at 20 kHz on a 48 V bus: average voltage error {dV:.2f} V per phase, opposing the current")
    for Vamp in [1.0, 10.0]:
        w = 2 * np.pi * 5.0; dt = 1e-5; t = np.arange(0, 1.0, dt)
        res = {}
        for comp in [False, True]:
            i = 0.0; out = []
            iref_sign = np.sign(np.sin(w * t - np.arctan(w * L / R)))
            for k, tk in enumerate(t):
                v = Vamp * np.sin(w * tk) - dV * np.sign(i) + (dV * iref_sign[k] if comp else 0.0)
                i += (v - R * i) / L * dt; out.append(i)
            out = np.array(out)[len(t) // 2:]
            ideal = Vamp / np.hypot(R, w * L) * np.sin(w * t[len(t) // 2:] - np.arctan(w * L / R))
            res[comp] = np.sqrt(np.mean((out - ideal) ** 2)) / (np.abs(ideal).max() / np.sqrt(2))
        print(f"  {Vamp:4.1f} V command ({'low speed' if Vamp < 5 else 'higher speed'}): current error {res[False]:.1%} of RMS uncompensated, "
              f"{res[True]:.1%} with dead-time compensation")


def v05_sensorless_low_speed():
    rng = np.random.default_rng(0)
    R, L, lam, p = PM["R"], PM["L"], PM["lam"], PM["p"]
    for wm in [2.0, 20.0, 200.0]:
        we = p * wm; t = np.arange(0, 0.5, 1e-4); th = we * t
        iq = 5.0
        i_ab = iq * np.stack([-np.sin(th), np.cos(th)])                 # current on the q axis
        e_ab = we * lam * np.stack([-np.sin(th), np.cos(th)])           # back-EMF
        v_ab = R * i_ab + e_ab + we * L * iq * np.stack([-np.cos(th), -np.sin(th)])
        v_meas = v_ab + rng.normal(0, 0.05, v_ab.shape) + 0.05          # noise and offset on the voltage estimate
        e_hat = v_meas - 1.2 * R * i_ab - we * L * iq * np.stack([-np.cos(th), -np.sin(th)])   # resistance off by 20%
        th_hat = np.arctan2(-e_hat[0], e_hat[1])
        err = np.degrees(np.angle(np.exp(1j * (th_hat - th))))
        rms = np.sqrt(np.mean(err**2))
        print(f"{wm:5.0f} rad/s: back-EMF {we*lam:5.2f} V; electrical angle error RMS {rms:5.1f} deg "
              f"-> {'FAILS (angle unusable)' if rms > 30 else 'usable'}")


# ================================================================== II. one axis: cascaded loops
J0, B0 = 2e-4, 1e-4                          # motor + load inertia (kg m^2), viscous friction


def _speed_loop_sim(J_true, bw_hz, T=0.1, dt=1e-5, wi=2 * np.pi * 1000, step=100.0, load=None, dob=None):
    ws = 2 * np.pi * bw_hz
    kp, ki = J0 * ws, J0 * ws * ws / 4
    w = tau = integ = dhat = qf = 0.0; out = []
    for k in range(int(T / dt)):
        t = k * dt
        e = step - w; integ += e * dt
        tcmd = kp * e + ki * integ + (dhat if dob else 0.0)
        tau += wi * (tcmd - tau) * dt                     # current loop as a first-order lag
        d = load(t) if load else 0.0
        acc = (tau - B0 * w - d) / J_true
        if dob:                                           # disturbance observer with nominal inertia J0
            qf += dob * ((tau - J0 * acc) - qf) * dt      # Q-filter on (tau - J0 * accel) estimates the load
            dhat = qf
        w += acc * dt; out.append(w)
    return np.array(out)


def v06_speed_loop_design():
    for ratio in [1 / 3, 1.0, 3.0]:
        y = _speed_loop_sim(J0 * ratio, 50.0)
        ts = np.where(np.abs(y - 100) > 2)[0]; ts = (ts[-1] + 1) * 1e-5 if len(ts) else 0
        print(f"actual inertia {ratio:4.2f} x nominal: overshoot {max(0, y.max()-100):4.1f}%, 2% settling {ts*1e3:5.1f} ms "
              f"(designed for 50 Hz)")


def v07_identify_inertia_friction():
    rng = np.random.default_rng(3)
    J, b, Fc = 2e-4, 1e-4, 0.01
    dt = 1e-4; t = np.arange(0, 2, dt)
    tau = 0.05 * np.sign(np.sin(2 * np.pi * 1.0 * t)) + 0.02 * np.sin(2 * np.pi * 7 * t)
    w = np.zeros_like(t)
    for k in range(1, len(t)):
        a = (tau[k - 1] - b * w[k - 1] - Fc * np.sign(w[k - 1])) / J
        w[k] = w[k - 1] + a * dt
    wm = w + rng.normal(0, 0.05, w.shape)
    n = 20; wf = np.convolve(wm, np.ones(n) / n, "same")             # smooth before differentiating
    acc = np.gradient(wf, dt)
    sl = slice(200, -200); m = np.abs(wf[sl]) > 1.0                   # avoid the stiction region
    Y = np.stack([acc[sl], wf[sl], np.sign(wf[sl])], 1)[m]
    th = np.linalg.lstsq(Y, tau[sl][m], rcond=None)[0]
    print(f"least squares from a 2 s torque test: J = {th[0]:.2e} (true 2.0e-4), b = {th[1]:.2e} (true 1.0e-4), "
          f"Fc = {th[2]:.4f} N m (true 0.0100)")


def v08_disturbance_observer():
    step = lambda t: 0.05 if t > 0.05 else 0.0       # 0.05 N m load torque step
    for name, dob, Jt in [("PI only (20 Hz)", None, J0), ("PI + DOB, Q at 300 Hz", 2 * np.pi * 300, J0),
                          ("PI + DOB, inertia off by 30%", 2 * np.pi * 300, 1.3 * J0)]:
        y = _speed_loop_sim(Jt, 20.0, T=0.2, step=0.0, load=step, dob=dob)
        print(f"{name:28s}: speed dip {abs(y.min()):.3f} rad/s after a 0.05 N m load step")


def _quintic(T, dt, dist=1.0):
    t = np.arange(0, T + 0.1, dt); s = np.clip(t / T, 0, 1)
    q = dist * (10 * s**3 - 15 * s**4 + 6 * s**5)
    v = dist / T * (30 * s**2 - 60 * s**3 + 30 * s**4) * (t <= T)
    a = dist / T**2 * (60 * s - 180 * s**2 + 120 * s**3) * (t <= T)
    return t, q, v, a


def v09_position_feedforward():
    t, qr, vr, ar = _quintic(0.2, 1e-5)
    Fc = 0.005
    for name, kv_ff, ka_ff in [("P position + PI speed", 0, 0), ("+ velocity feedforward", 1, 0), ("+ acceleration (torque) feedforward", 1, 1)]:
        kpp = 2 * np.pi * 15; ws = 2 * np.pi * 80; kp, ki = J0 * ws, J0 * ws * ws / 4
        q = w = tau = integ = 0.0; err = []
        for k in range(len(t)):
            wref = kpp * (qr[k] - q) + kv_ff * vr[k]
            e = wref - w; integ += e * 1e-5
            tcmd = kp * e + ki * integ + ka_ff * (J0 * ar[k] + B0 * vr[k] + Fc * np.sign(vr[k]))
            tau += 2 * np.pi * 1000 * (tcmd - tau) * 1e-5
            acc = (tau - B0 * w - Fc * np.sign(w)) / J0
            w += acc * 1e-5; q += w * 1e-5; err.append(qr[k] - q)
        print(f"{name:37s}: peak following error {np.abs(err).max()*1e3:6.2f} mrad on a 1 rad, 0.2 s move")


def v10_trapezoid_vs_scurve():
    zeta, T, dt = 0.01, 0.2, 1e-4
    t = np.arange(0, 1.5, dt); s = np.clip(t / T, 0, 1)
    A = 1 / (T * T * 2 / 9)
    a_trap = np.where(t < T / 3, A, 0.0) + np.where((t >= 2 * T / 3) & (t < T), -A, 0.0)
    a_quin = (60 * s - 180 * s**2 + 120 * s**3) / T**2 * (t <= T)
    def residual(a, f):
        wn = 2 * np.pi * f; x = v = 0.0; out = []
        for ak in a:                              # load deflection driven by the base acceleration
            v += (-ak - 2 * zeta * wn * v - wn * wn * x) * dt; x += v * dt; out.append(x)
        return np.abs(np.array(out)[int(T / dt) + 1:]).max() * 1e3
    print(f"1 rad in 0.2 s; peak acceleration: trapezoidal {np.abs(a_trap).max():.0f}, quintic (jerk-limited) {np.abs(a_quin).max():.0f} rad/s^2")
    print("  worst residual vibration over each band of mode frequencies (a mode's exact frequency is rarely known):")
    for lo, hi in [(5, 10), (10, 20), (20, 40), (40, 80)]:
        fs_ = np.linspace(lo, hi, 21)
        rt = max(residual(a_trap, f) for f in fs_); rq = max(residual(a_quin, f) for f in fs_)
        print(f"  modes {lo:2d}-{hi:2d} Hz: trapezoidal {rt:7.3f} mrad, jerk-limited {rq:7.3f} mrad")


def _two_mass(Jm=2e-4, JL=6e-4, k=30.0, c=2e-4):
    return Jm, JL, k, c


def v11_frequency_response():
    rng = np.random.default_rng(4)
    Jm, JL, k, c = _two_mass()
    fs = 5000.0; dt = 1 / fs; t = np.arange(0, 20.0, dt)
    f0, f1 = 2.0, 400.0                       # logarithmic chirp: equal time per octave
    Tc = t[-1]; kk = np.log(f1 / f0)
    u = 0.02 * np.sin(2 * np.pi * f0 * Tc / kk * (np.exp(kk * t / Tc) - 1))
    x = np.zeros(4); y = []
    A = np.array([[0, 1, 0, 0], [-k / Jm, -c / Jm, k / Jm, c / Jm], [0, 0, 0, 1], [k / JL, c / JL, -k / JL, -c / JL]])
    Ad, Bd = c2d(A, np.array([[0], [1 / Jm], [0], [0]]), dt)
    for uk in u:
        x = Ad @ x + Bd[:, 0] * uk
        y.append(x[1])
    y = np.array(y) + rng.normal(0, 0.02, len(y))
    n = 4096; win = np.hanning(n); Suu = Syu = 0
    for s0 in range(0, len(u) - n, n // 2):
        U = np.fft.rfft(win * u[s0:s0 + n]); Y = np.fft.rfft(win * (y[s0:s0 + n] - y[s0:s0 + n].mean()))
        Suu = Suu + np.abs(U) ** 2; Syu = Syu + Y * np.conj(U)
    H = Syu / Suu; f = np.fft.rfftfreq(n, dt)
    band = (f > 5) & (f < 300)
    mag = np.abs(H[band]); fb = f[band]
    i_r = np.argmax(mag * fb); i_ar = np.argmin(mag * fb)       # speed FRF ~ 1/(J s): remove the integrator trend
    true_ar = np.sqrt(k / JL) / 2 / np.pi; true_r = np.sqrt(k * (Jm + JL) / (Jm * JL)) / 2 / np.pi
    print(f"log chirp 2-400 Hz, 20 s, noisy speed: anti-resonance {fb[i_ar]:.1f} Hz (true {true_ar:.1f}), "
          f"resonance {fb[i_r]:.1f} Hz (true {true_r:.1f})")


def v12_notch_filter():
    Jm, JL = 2e-4, 1e-3                                    # stiff coupling: lightly damped mode near 400 Hz
    wr0 = 2 * np.pi * 400; k = wr0 ** 2 * Jm * JL / (Jm + JL); c = 2 * 0.01 * wr0 * Jm * JL / (Jm + JL)
    Jt = Jm + JL; Ts = 1 / 8000.0
    A = np.array([[0, 1, 0, 0], [-k / Jm, -c / Jm, k / Jm, c / Jm], [0, 0, 0, 1], [k / JL, c / JL, -k / JL, -c / JL]])
    Ad, Bd = c2d(A, np.array([[0], [1 / Jm], [0], [0]]), Ts)
    wr = np.sqrt(k * (Jm + JL) / (Jm * JL))
    # notch (s^2 + 2 z1 wr s + wr^2)/(s^2 + 2 z2 wr s + wr^2), Tustin with prewarping
    z1, z2 = 0.02, 0.5; K = wr / np.tan(wr * Ts / 2)
    b0, b1, b2 = K * K + 2 * z1 * wr * K + wr * wr, 2 * (wr * wr - K * K), K * K - 2 * z1 * wr * K + wr * wr
    a0, a1, a2 = K * K + 2 * z2 * wr * K + wr * wr, 2 * (wr * wr - K * K), K * K - 2 * z2 * wr * K + wr * wr
    ai = 1 - np.exp(-2 * np.pi * 1000 * Ts)                # 1 kHz current loop as a first-order lag
    def settles(bw, use_notch, T=0.6):
        ws = 2 * np.pi * bw; kp, ki = Jt * ws, Jt * ws * ws / 4
        x = np.zeros(4); tau = integ = 0.0; cmd_prev = 0.0; xin = [0.0, 0.0]; yout = [0.0, 0.0]; w = []
        for n in range(int(T / Ts)):
            e = 1.0 - x[1]; integ += e * Ts
            u = kp * e + ki * integ
            if use_notch:
                y = (b0 * u + b1 * xin[0] + b2 * xin[1] - a1 * yout[0] - a2 * yout[1]) / a0
                xin = [u, xin[0]]; yout = [y, yout[0]]; u = y
            tau += ai * (cmd_prev - tau); cmd_prev = u        # one-sample computation delay, then current loop
            x = Ad @ x + Bd[:, 0] * tau; w.append(x[1])
            if abs(x[1]) > 1e3:
                return False
        late = np.array(w[int(0.45 / Ts):])
        return late.max() - late.min() < 0.02
    for use in [False, True]:
        best = max([bw for bw in range(10, 610, 10) if settles(bw, use)] + [0])
        print(f"{'with notch at the resonance' if use else 'no notch                   '}: highest speed-loop bandwidth that settles "
              f"{best} Hz (resonance {wr/2/np.pi:.1f} Hz, 8 kHz sampling)")


# ================================================================== III. high-precision servos
def v13_inverse_feedforward():
    t, qr, vr, ar = _quintic(0.05, 1e-5, dist=0.01)        # 10 mm in 50 ms on a direct-drive stage
    m, b = 2.0, 5.0
    for name, ff, merr in [("feedback only (PD, 100 Hz)", False, 1.0), ("+ mass/damping feedforward, exact", True, 1.0),
                           ("+ feedforward, mass 10% wrong", True, 1.1), ("+ feedforward, mass 30% wrong", True, 1.3)]:
        wn = 2 * np.pi * 100; kp, kd = m * wn * wn, 2 * 0.7 * m * wn
        x = v = 0.0; err = []
        for k in range(len(t)):
            F = kp * (qr[k] - x) + kd * (vr[k] - v) + ((merr * m) * ar[k] + b * vr[k] if ff else 0)
            v += (F - b * v) / m * 1e-5; x += v * 1e-5; err.append(qr[k] - x)
        print(f"{name:34s}: peak tracking error {np.abs(err).max()*1e6:7.2f} um")


def v14_zpetc():
    N = 400; k = np.arange(N); s_ = np.clip((k - 50) / 200, 0, 1)
    yd = 10 * s_**3 - 15 * s_**4 + 6 * s_**5                     # smooth 0 -> 1 reference, at rest at both ends
    # plant: A(q^-1) y = q^-1 K (1 - 1.2 q^-1) u, A = 1 - 1.7 q^-1 + 0.72 q^-2; zero at 1.2 (non-minimum phase), DC gain 1
    K = -0.1
    def plant(u):
        y = np.zeros(N)
        for i in range(2, N):
            y[i] = 1.7 * y[i - 1] - 0.72 * y[i - 2] + K * (u[i - 1] - 1.2 * u[i - 2])
        return y
    ydx = np.concatenate([yd, np.full(3, yd[-1])])           # the reference holds its final value (preview beyond the end)
    Ay = np.array([ydx[j] - 1.7 * ydx[j - 1] + 0.72 * ydx[j - 2] if j >= 2 else 0.0 for j in range(N + 3)])
    Ayf = lambda j: Ay[j]
    u = np.zeros(N)                               # (a) exact causal inverse: unstable recursion
    for i in range(1, N - 1):
        u[i] = Ayf(i + 1) / K + 1.2 * u[i - 1]
    print(f"exact causal inverse: |u| grows to {np.abs(u).max():.1e} -> unusable (zero outside the unit circle)")
    u = np.array([Ayf(i + 1) / (K * (1 - 1.2)) for i in range(N)])        # (b) ignore the zero, match DC gain
    e_ignore = np.abs(plant(u) - yd).max()
    Bu1 = K * (1 - 1.2)                           # (c) ZPETC: A(q^-1) Bu(q) / Bu(1)^2, one extra step of preview
    u = np.array([K * (Ayf(i + 1) - 1.2 * Ayf(i + 2)) / Bu1 ** 2 for i in range(N)])
    e_z = np.abs(plant(u) - yd).max()
    print(f"invert the poles only, ignore the zero: peak error {e_ignore:.4f} (reference moves 1.0)")
    print(f"ZPETC (zero phase error tracking):      peak error {e_z:.4f}")


def v15_iterative_learning():
    rng = np.random.default_rng(5)
    N = 300; k = np.arange(N); s = np.clip((k - 20) / 200, 0, 1)
    r = 10 * s**3 - 15 * s**4 + 6 * s**5
    # closed-loop servo (reference -> output), discrete second order with a repeating disturbance
    a1, a2, b1 = 1.6, -0.68, 0.08
    h = np.zeros(N); h[1] = b1
    for i in range(2, N):
        h[i] = a1 * h[i - 1] + a2 * h[i - 2]
    Jl = np.array([[h[i - j] if i >= j else 0 for j in range(N)] for i in range(N)])   # lifted system
    d = 0.02 * np.sin(2 * np.pi * k / 60)                         # repeating disturbance (e.g. cogging)
    f = np.zeros(N); out = []
    Lg = np.linalg.solve(Jl.T @ Jl + 1e-4 * np.eye(N), Jl.T)      # regularized inverse learning filter
    for it in range(11):
        y = Jl @ (r + f) + d + rng.normal(0, 1e-4, N)
        e = r - y
        out.append(np.sqrt(np.mean(e ** 2)))
        f = f + 0.5 * Lg @ e
    print("RMS tracking error per trial: " + ", ".join(f"{x:.1e}" for x in out))
    print(f"error falls {out[0]/out[-1]:.0f}x in 10 trials and stops near the non-repeating noise (1e-4)")


def v16_cogging_compensation():
    J, amp, nper = J0, 0.005, 12                 # cogging 0.005 N m, 12 periods per revolution
    def run(speed, bw, table=None, T=8.0, dt=1e-4):
        ws = 2 * np.pi * bw; kp, ki = J * ws, J * ws * ws / 4
        th = w = integ = 0.0; out = []
        for k_ in range(int(T / dt)):
            e = speed - w; integ += e * dt
            tc = kp * e + ki * integ
            if table is not None:
                tc += np.interp(th % (2 * np.pi), table[0], table[1], period=2 * np.pi)
            w += (tc - amp * np.sin(nper * th) - B0 * w) / J * dt; th += w * dt
            if k_ * dt > 3:
                out.append((w, tc, th % (2 * np.pi)))
        return np.array(out)
    base = run(2.0, 10.0)
    ident = run(0.5, 100.0, T=20.0)              # slow, stiff identification run
    bins = np.linspace(0, 2 * np.pi, 181); idx = np.digitize(ident[:, 2], bins) - 1
    tab = np.array([ident[idx == i, 1].mean() for i in range(180)]); tab -= tab.mean()
    comp = run(2.0, 10.0, (0.5 * (bins[1:] + bins[:-1]), tab))
    rip = lambda r: r[:, 0].max() - r[:, 0].min()
    print(f"2 rad/s with a 10 Hz speed loop, cogging 0.005 N m x 12 per rev: speed ripple {rip(base):.3f} rad/s; "
          f"with an angle table learned in a slow stiff run {rip(comp):.3f} rad/s ({rip(base)/rip(comp):.0f}x lower)")


def _xy_circle(R=0.01, T=2.0, comp=False, kx=60.0, ky=60.0, ccc=0.0, vff=True, Fc=1.0, dt=1e-5):
    m, b = 5.0, 20.0
    t = np.arange(0, T, dt); w = 2 * np.pi / 1.0                 # one revolution per second
    rx, ry = R * np.cos(w * t), R * np.sin(w * t)
    vx, vy = -R * w * np.sin(w * t), R * w * np.cos(w * t)
    ax, ay = -R * w * w * np.cos(w * t), -R * w * w * np.sin(w * t)
    x, y, xv, yv = R, 0.0, 0.0, R * w
    ix = iy = 0.0; rad = []
    for k in range(len(t)):
        ex, ey = rx[k] - x, ry[k] - y
        if ccc:                                       # cross-coupled: push along the radial (contour-normal) direction
            nx, ny = np.cos(w * t[k]), np.sin(w * t[k]); en = ex * nx + ey * ny
            ex += ccc * en * nx; ey += ccc * en * ny
        vxr = kx * ex + (vx[k] if vff else 0); vyr = ky * ey + (vy[k] if vff else 0)
        ix += (vxr - xv) * dt; iy += (vyr - yv) * dt
        Fx = 400 * (vxr - xv) + 4e4 * ix + (m * ax[k] + b * vx[k] if vff else 0)
        Fy = 400 * (vyr - yv) + 4e4 * iy + (m * ay[k] + b * vy[k] if vff else 0)
        if comp:
            Fx += Fc * np.sign(vx[k]); Fy += Fc * np.sign(vy[k])
        xv += (Fx - b * xv - Fc * np.sign(xv)) / m * dt; yv += (Fy - b * yv - Fc * np.sign(yv)) / m * dt
        x += xv * dt; y += yv * dt
        rad.append(np.hypot(x, y) - R)
    return np.array(rad)[len(t) // 2:]                # second revolution only


def v17_quadrant_glitch():
    for comp in [False, True]:
        r = _xy_circle(comp=comp)
        print(f"{'friction feedforward at reversals' if comp else 'no friction compensation         '}: peak radial error "
              f"{np.abs(r).max()*1e6:6.2f} um on a 10 mm circle at 1 rev/s (Coulomb friction 1 N per axis)")


def v18_contouring():
    for name, kw in [("matched position gains 60/60, no feedforward", dict(kx=60, ky=60, vff=False)),
                     ("mismatched gains 60/40, no feedforward", dict(kx=60, ky=40, vff=False)),
                     ("mismatched 60/40 + cross-coupled contour gain", dict(kx=60, ky=40, vff=False, ccc=2.0)),
                     ("mismatched 60/40 + feedforward", dict(kx=60, ky=40, vff=True))]:
        r = _xy_circle(Fc=0.0, **kw)
        print(f"{name:46s}: radial error {r.mean()*1e6:+7.1f} um mean, {(r.max()-r.min())*1e6:6.1f} um out-of-round")


# ================================================================== IV. multi-axis robot arms
def _arm2(q, dq, m2=1.0):
    m1 = 1.0; l1 = l2 = 0.5; lc1 = lc2 = 0.25; I1 = I2 = 0.02; g = 9.81
    c2, s2 = np.cos(q[1]), np.sin(q[1])
    M = np.array([[I1 + I2 + m1 * lc1**2 + m2 * (l1**2 + lc2**2 + 2 * l1 * lc2 * c2), I2 + m2 * (lc2**2 + l1 * lc2 * c2)],
                  [I2 + m2 * (lc2**2 + l1 * lc2 * c2), I2 + m2 * lc2**2]])
    h = m2 * l1 * lc2 * s2
    C = np.array([[-h * dq[1], -h * (dq[0] + dq[1])], [h * dq[0], 0.0]])
    G = np.array([(m1 * lc1 + m2 * l1) * g * np.cos(q[0]) + m2 * lc2 * g * np.cos(q[0] + q[1]), m2 * lc2 * g * np.cos(q[0] + q[1])])
    return M, C, G


def v19_reflected_inertia():
    q2 = np.linspace(-np.pi, np.pi, 361)
    M11 = np.array([_arm2(np.array([0, a]), np.zeros(2))[0][0, 0] for a in q2])
    Jm = 1e-4
    for N in [1, 10, 50, 160]:
        Jmot = Jm + M11 / N**2                          # inertia seen at the motor
        print(f"gear ratio {N:4d}: joint-1 inertia seen by the motor varies {Jmot.max()/Jmot.min():5.2f}x with the elbow angle")
    print(f"(link-side inertia alone varies {M11.max()/M11.min():.2f}x)")


def v20_computed_torque():
    T, dt = 1.0, 1e-4; t = np.arange(0, T, dt)
    q0, q1 = np.array([0.0, 0.5]), np.array([1.2, -0.8])
    s = np.clip(t / 0.6, 0, 1)
    sh = 10 * s**3 - 15 * s**4 + 6 * s**5; sd = (30 * s**2 - 60 * s**3 + 30 * s**4) / 0.6; sdd = (60 * s - 180 * s**2 + 120 * s**3) / 0.36
    Kp, Kd = np.diag([400.0, 400.0]), np.diag([40.0, 40.0])
    for name, mode, m2_true in [("PD per joint", "pd", 1.0), ("PD + gravity compensation", "pdg", 1.0),
                                ("computed torque", "ct", 1.0), ("computed torque, payload +0.5 kg unmodelled", "ct", 1.5)]:
        q, dq = q0.copy(), np.zeros(2); err = []
        for k in range(len(t)):
            qr = q0 + (q1 - q0) * sh[k]; vr = (q1 - q0) * sd[k]; ar = (q1 - q0) * sdd[k]
            M, C, G = _arm2(q, dq, 1.0)                    # controller's model (nominal payload)
            e, de = qr - q, vr - dq
            if mode == "pd":
                tau = Kp @ e + Kd @ de
            elif mode == "pdg":
                tau = Kp @ e + Kd @ de + G
            else:
                tau = M @ (ar + Kp @ e + Kd @ de) + C @ dq + G
            Mt, Ct, Gt = _arm2(q, dq, m2_true)
            ddq = np.linalg.solve(Mt, tau - Ct @ dq - Gt)
            dq = dq + dt * ddq; q = q + dt * dq; err.append(np.abs(e).max())
        print(f"{name:44s}: peak joint error {max(err)*1e3:7.2f} mrad, final {err[-1]*1e3:6.2f} mrad")


def v21_input_shaping():
    f, zeta = 8.0, 0.02
    wn = 2 * np.pi * f; wd = wn * np.sqrt(1 - zeta**2); Td = 2 * np.pi / wd
    K = np.exp(-zeta * np.pi / np.sqrt(1 - zeta**2))
    shapers = {"unshaped": [(1.0, 0.0)],
               "ZV": [(1 / (1 + K), 0.0), (K / (1 + K), Td / 2)],
               "ZVD": [(1 / (1 + K)**2, 0.0), (2 * K / (1 + K)**2, Td / 2), (K**2 / (1 + K)**2, Td)]}
    def residual(imp, f_true):
        w = 2 * np.pi * f_true; dt = 1e-4; t = np.arange(0, 2.0, dt)
        u = sum(a * (t >= tt) for a, tt in imp)          # shaped step command for the motor position
        x = v = 0.0; out = []
        for k in range(len(t)):                          # link = motor command + flexible deflection
            v += (w * w * (u[k] - x) - 2 * zeta * w * v) * dt; x += v * dt; out.append(x)
        out = np.array(out); end = max(tt for _, tt in imp)
        return np.abs(out[int((end + 0.05) / dt):] - 1).max()
    for name, imp in shapers.items():
        print(f"{name:9s}: delay {max(tt for _, tt in imp)*1e3:5.1f} ms; residual vibration {residual(imp, f):.4f} "
              f"(mode right), {residual(imp, 1.2*f):.4f} (mode 20% higher)")


def v22_dynamic_identification():
    rng = np.random.default_rng(6)
    def regress(q, dq, ddq):
        # base parameters of the planar 2-link arm: tau = Y(q, dq, ddq) theta
        c2, s2 = np.cos(q[1]), np.sin(q[1]); g = 9.81
        y1 = [ddq[0], c2 * (2 * ddq[0] + ddq[1]) - s2 * (dq[1]**2 + 2 * dq[0] * dq[1]), ddq[1], g * np.cos(q[0]), g * np.cos(q[0] + q[1])]
        y2 = [0.0, c2 * ddq[0] + s2 * dq[0]**2, ddq[0] + ddq[1], 0.0, g * np.cos(q[0] + q[1])]
        return np.array([y1, y2])
    m1 = m2 = 1.0; l1 = 0.5; lc1 = lc2 = 0.25; I1 = I2 = 0.02
    theta = np.array([I1 + m1 * lc1**2 + m2 * l1**2, m2 * l1 * lc2, I2 + m2 * lc2**2, m1 * lc1 + m2 * l1, m2 * lc2])
    for name, wfreqs in [("slow single sine", [0.3]), ("Fourier excitation (5 harmonics)", [0.3, 0.6, 0.9, 1.2, 1.5])]:
        t = np.linspace(0, 10, 2001); Ys, taus = [], []
        for tk in t:
            q = np.array([sum(0.6 / (i + 1) * np.sin(2 * np.pi * f * tk + i) for i, f in enumerate(wfreqs)),
                          sum(0.5 / (i + 1) * np.cos(2 * np.pi * f * tk + 2 * i) for i, f in enumerate(wfreqs))])
            dq = np.array([sum(0.6 / (i + 1) * 2 * np.pi * f * np.cos(2 * np.pi * f * tk + i) for i, f in enumerate(wfreqs)),
                           sum(-0.5 / (i + 1) * 2 * np.pi * f * np.sin(2 * np.pi * f * tk + 2 * i) for i, f in enumerate(wfreqs))])
            ddq = np.array([sum(-0.6 / (i + 1) * (2 * np.pi * f)**2 * np.sin(2 * np.pi * f * tk + i) for i, f in enumerate(wfreqs)),
                            sum(-0.5 / (i + 1) * (2 * np.pi * f)**2 * np.cos(2 * np.pi * f * tk + 2 * i) for i, f in enumerate(wfreqs))])
            Y = regress(q, dq, ddq); Ys.append(Y); taus.append(Y @ theta + rng.normal(0, 0.05, 2))
        Y = np.vstack(Ys); tau = np.concatenate(taus)
        th = np.linalg.lstsq(Y, tau, rcond=None)[0]
        sd = 0.05 * np.sqrt(np.diag(np.linalg.inv(Y.T @ Y))) / np.abs(theta)   # predicted relative standard error
        print(f"{name:33s}: worst predicted std. error {sd.max():.1%}; worst actual parameter error {np.abs(th/theta-1).max():.1%}")


def v23_collision_detection():
    rng = np.random.default_rng(7)
    J, mgl, dt = 0.5, 4.0, 1e-3                   # one joint: J qdd = tau - mgl cos q + tau_ext
    K = 50.0; q = dq = 0.0; integ = 0.0; r = 0.0; rs = []
    for k in range(3000):
        t = k * dt
        qref = 0.5 * np.sin(2 * np.pi * 0.5 * t)
        tau = 200 * (qref - q) - 20 * dq + mgl * np.cos(q)
        text = 3.0 if 1.5 <= t < 1.7 else 0.0     # 3 N m collision lasting 0.2 s
        ddq = (tau - mgl * np.cos(q) + text - 0.3 * np.sign(dq)) / J      # unmodelled friction 0.3 N m
        dq += ddq * dt; q += dq * dt
        p_hat = 1.1 * J * (dq + rng.normal(0, 0.002))                     # inertia model 10% off, noisy velocity
        integ += (tau - mgl * np.cos(q) + r) * dt
        r = K * (p_hat - integ - 1.1 * J * 0.0)
        rs.append(r)
    rs = np.array(rs); thr = 1.0
    pre = np.abs(rs[100:1500]).max(); det = np.argmax(np.abs(rs[1500:]) > thr) * dt
    print(f"momentum observer (gain {K:.0f}/s): residual before contact up to {pre:.2f} N m (model error, friction, noise); "
          f"threshold {thr} N m detects the 3 N m collision after {det*1e3:.0f} ms; peak residual {np.abs(rs[1500:1700]).max():.2f} N m")


def v24_impedance_control():
    m, k_env, x_wall = 2.0, 1e5, 0.0
    for name, K, D in [("stiff position control", 2e5, 1200.0), ("impedance control", 500.0, 60.0)]:
        x, v, dt = -0.02, 0.0, 1e-5; F = []
        for k in range(int(1.0 / dt)):
            xr = min(-0.02 + 0.05 * k * dt, 0.005)       # reference moves 5 mm into the wall
            f_env = k_env * (x - x_wall) if x > x_wall else 0.0
            u = K * (xr - x) - D * v
            v += (u - f_env) / m * dt; x += v * dt; F.append(f_env)
        F = np.array(F)
        print(f"{name:24s}: contact force peak {F.max():7.1f} N, steady {F[-1]:7.1f} N")


def v25_iso9283():
    rng = np.random.default_rng(8)
    cmd = np.array([800.0, 200.0, 600.0])           # commanded position, mm
    for name, bias in [("uncalibrated (kinematic error 0.4 mm)", np.array([0.3, -0.2, 0.18])), ("after calibration", np.array([0.02, -0.01, 0.01]))]:
        P = cmd + bias + rng.normal(0, 0.008, (30, 3))
        bar = P.mean(0)
        AP = np.linalg.norm(bar - cmd)
        l = np.linalg.norm(P - bar, axis=1); RP = l.mean() + 3 * l.std(ddof=1)
        print(f"{name:38s}: pose accuracy AP {AP:.3f} mm, pose repeatability RP {RP:.3f} mm (30 cycles)")


RECIPES = {name: fn for name, fn in globals().items() if name.startswith("v") and name[1:3].isdigit()}

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, fn in RECIPES.items():
        if pattern in name:
            print(f"\n=== {name} ===")
            fn()
