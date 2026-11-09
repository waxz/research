#!/usr/bin/env python3
"""Worked examples for the Control Systems Engineering Cookbook.

Every number quoted under "Worked example" in COOKBOOK.md comes from a function
here. Requires only NumPy.

    python3 examples.py          # run all recipes
    python3 examples.py h09      # run recipes whose name contains "h09"
"""
import sys

import numpy as np

np.set_printoptions(precision=4, suppress=True)


# ================================================================== I. physics and mechanics
def h01_motion_profile_to_torque():
    m, l, Jm = 2.0, 0.3, 0.01                 # 2 kg at 0.3 m on a joint with 0.01 kg m^2 of rotor+gear inertia
    J = Jm + m * l * l
    T, th0, th1 = 0.5, -np.pi / 2, 0.0        # swing from hanging (-90 deg) to horizontal in 0.5 s
    t = np.linspace(0, T, 5001); s = t / T
    th = th0 + (th1 - th0) * (10 * s**3 - 15 * s**4 + 6 * s**5)          # minimum-jerk profile
    w = np.gradient(th, t); a = np.gradient(w, t)
    tau = J * a + m * 9.81 * l * np.cos(th)
    P = tau * w
    print(f"peak torque {np.abs(tau).max():.2f} N m; RMS torque {np.sqrt(np.mean(tau**2)):.2f} N m; "
          f"peak speed {w.max():.2f} rad/s; peak mechanical power {P.max():.1f} W")
    print(f"holding horizontal afterwards needs {m*9.81*l:.2f} N m continuously: size the motor on RMS and holding torque, the drive on peak")


def h02_gear_ratio_and_reflected_inertia():
    Jm, JL, tau_m = 6e-5, 0.05, 0.5            # rotor inertia, load inertia (kg m^2), motor torque (N m)
    N_opt = np.sqrt(JL / Jm)
    for N in [5, 10, N_opt, 50, 100]:
        acc = N * tau_m / (JL + N * N * Jm)    # load acceleration
        print(f"gear ratio {N:6.1f}: reflected rotor inertia {N*N*Jm:.4f} kg m^2, load acceleration {acc:6.1f} rad/s^2")
    print(f"optimum N* = sqrt(JL/Jm) = {N_opt:.1f}: reflected rotor inertia equals load inertia")
    m, lead = 20.0, 0.01                      # ball screw: 20 kg table, 10 mm lead
    print(f"ball screw, 10 mm lead: a 20 kg table reflects {m*(lead/(2*np.pi))**2:.2e} kg m^2 to the motor; "
          f"1 N m gives {2*np.pi*0.9/lead:.0f} N of thrust at 90% efficiency")


def h03_two_mass_resonance():
    Jm, JL, k = 2e-4, 2e-3, 50.0               # motor and load inertia, shaft or belt stiffness (N m/rad)
    w_ar = np.sqrt(k / JL); w_r = np.sqrt(k * (Jm + JL) / (Jm * JL))
    c = 2 * 0.05 * w_r * Jm * JL / (Jm + JL)   # 5% structural damping of the resonant mode
    f_ar = w_ar / 2 / np.pi
    print(f"anti-resonance {f_ar:.1f} Hz, resonance {w_r/2/np.pi:.1f} Hz")

    def sim(bw_hz, side, T=0.8, dt=2e-6):
        wc = 2 * np.pi * bw_hz
        kp, ki = wc * (Jm + JL), wc * (Jm + JL) * wc / 5      # velocity PI tuned on the rigid-body model
        thm = thl = wm = wl = integ = 0.0; ws = []
        for _ in range(int(T / dt)):
            e = 1.0 - (wl if side == "load" else wm); integ += e * dt
            tau = kp * e + ki * integ
            ts = k * (thm - thl) + c * (wm - wl)
            wm += (tau - ts) / Jm * dt; wl += ts / JL * dt
            thm += wm * dt; thl += wl * dt; ws.append(wl)
            if abs(wl) > 1e3:
                return None
        return 100 * (max(ws) - 1)
    for side, label in [("motor", "motor encoder (collocated)"), ("load", "load encoder (non-collocated)")]:
        for frac in [0.2, 0.5, 1.0]:
            r = sim(f_ar * frac, side)
            print(f"  {label:30s} velocity loop {f_ar*frac:5.1f} Hz ({frac:.1f} x anti-resonance): "
                  + ("UNSTABLE" if r is None else f"load-speed overshoot {r:.0f}%"))


def h04_friction_stick_slip():
    m, k, Fc, Fs, vs, b = 1.0, 100.0, 4.0, 6.0, 0.01, 0.5    # Stribeck: static 6 N, Coulomb 4 N
    def run(v_pull, T=6.0, dt=1e-5):
        x = v = 0.0; xs = []
        for i in range(int(T / dt)):
            F = k * (v_pull * i * dt - x)
            if abs(v) < 1e-6 and abs(F) <= Fs:       # stuck
                v = 0.0
            else:
                fr = (Fc + (Fs - Fc) * np.exp(-(v / vs) ** 2)) * np.sign(v if abs(v) > 1e-6 else F) + b * v
                v += (F - fr) / m * dt
            x += v * dt; xs.append(v)
        vv = np.array(xs[int(3 / dt):])
        return vv.max() - vv.min(), np.mean(np.abs(vv) < 1e-6)
    for vp in [0.05, 2.0]:
        sw, stuck = run(vp)
        print(f"pull speed {vp:4.2f} m/s: block-speed swing {sw:.3f} m/s, stuck {stuck:.0%} of the time "
              f"-> {'STICK-SLIP' if stuck > 0.05 else 'smooth sliding'}")


def h05_backlash_hunting():
    Jm, JL, kc, gap, Fc = 1e-3, 1e-2, 200.0, 0.02, 0.05   # backlash of 0.02 rad, load Coulomb friction 0.05 N m
    def run(ki, kd, kp=2.0, T=10.0, dt=2e-5):
        qm = vm = ql = vl = integ = 0.0; qs = []
        for _ in range(int(T / dt)):
            e = 0.5 - ql; integ += e * dt
            tau = kp * e + ki * integ - kd * vm          # position from the load encoder, damping from the motor encoder
            d = qm - ql                                   # contact only when the gap is closed
            tc = kc * (d - np.sign(d) * gap / 2) if abs(d) > gap / 2 else 0.0
            fr = Fc * np.sign(vl) if abs(vl) > 1e-4 else np.clip(tc, -Fc, Fc)
            vm += (tau - tc) / Jm * dt; vl += (tc - fr) / JL * dt
            qm += vm * dt; ql += vl * dt; qs.append(ql)
        qq = np.array(qs[int(6 / dt):])
        return np.abs(qq - 0.5).max(), qq.max() - qq.min()
    for ki, kd, name in [(0.0, 0.1, "PD"), (1.0, 0.05, "PID, light damping"), (2.0, 0.1, "PID, more damping")]:
        err, sw = run(ki, kd)
        print(f"{name:19s}: error in the last 4 s up to {err*1e3:5.1f} mrad, oscillation {sw*1e3:4.1f} mrad "
              f"(backlash {gap*1e3:.0f} mrad)")


# ================================================================== II. electrical
MOTOR = dict(R=0.5, L=0.2e-3, kt=0.05, J=2e-5, b=1e-6, V=24.0)   # small brushed DC motor


def h06_motor_time_constants():
    R, L, kt, J, b, V = (MOTOR[k] for k in "R L kt J b V".split())
    te, tm = L / R, J * R / kt**2
    print(f"electrical time constant L/R = {te*1e3:.2f} ms; mechanical time constant JR/kt^2 = {tm*1e3:.1f} ms; ratio {tm/te:.0f}")
    i = w = 0.0; dt = 1e-6; ipk = 0.0; t63 = None; wss = V / kt * kt**2 / (kt**2 + R * b)
    for k in range(int(0.05 / dt)):
        di = (V - R * i - kt * w) / L; dw = (kt * i - b * w) / J
        i += di * dt; w += dw * dt; ipk = max(ipk, i)
        if t63 is None and w > 0.632 * wss:
            t63 = k * dt
    print(f"24 V step: current peaks at {ipk:.1f} A (stall current V/R = {V/R:.0f} A); speed reaches 63% at {t63*1e3:.1f} ms; "
          f"no-load speed {w:.0f} rad/s")


def h07_torque_speed_power():
    R, kt, V = MOTOR["R"], MOTOR["kt"], MOTOR["V"]
    tau_stall, w0 = kt * V / R, V / kt
    tau = np.linspace(0, tau_stall, 1001); w = w0 * (1 - tau / tau_stall)
    P = tau * w; eta = P / (V * tau / kt + 1e-12)
    i = np.argmax(P); j = np.argmax(eta[1:-1]) + 1
    print(f"stall torque {tau_stall:.2f} N m, no-load speed {w0:.0f} rad/s; max output power {P[i]:.0f} W at "
          f"{tau[i]:.2f} N m (half stall)")
    print(f"efficiency there {eta[i]:.0%}; ideal-model efficiency rises toward light load, where friction (ignored here) takes over")


def h08_thermal_derating():
    R0, alpha, Rth, Cth, Ta, Tmax = 0.5, 0.00393, 4.0, 60.0, 25.0, 120.0   # copper tempco; K/W; J/K
    # continuous current: steady state with resistance rising with temperature
    I = np.sqrt((Tmax - Ta) / (Rth * R0 * (1 + alpha * (Tmax - Ta))))
    print(f"thermal time constant {Rth*Cth:.0f} s; continuous current {I:.2f} A for {Tmax:.0f} C "
          f"(winding resistance {R0*(1+alpha*(Tmax-Ta)):.3f} ohm when hot, +{alpha*(Tmax-Ta):.0%})")
    for mult in [1.5, 2.0, 3.0]:
        T, t, dt = Ta, 0.0, 0.05
        while T < Tmax and t < 3600:
            P = (mult * I) ** 2 * R0 * (1 + alpha * (T - 25.0))
            T += (P - (T - Ta) / Rth) / Cth * dt; t += dt
        print(f"  {mult:.1f} x continuous current: winding hits {Tmax:.0f} C after {t:.0f} s -> the drive must derate or trip")


def h09_pwm_ripple():
    V, L, R = 24.0, MOTOR["L"], MOTOR["R"]
    for f in [4e3, 20e3, 80e3]:
        D = 0.5
        ripple_formula = V * D * (1 - D) / (L * f)
        i, dt, n = 0.0, 1 / f / 200, 0; Ts = 1 / f; ii = []
        for k in range(int(0.02 / dt)):
            t = k * dt
            v = V if (t % Ts) < D * Ts else 0.0   # unipolar switching, back-EMF taken as 0 (stalled)
            i += (v - R * i) / L * dt
            if t > 0.015:
                ii.append(i)
        print(f"PWM {f/1e3:4.0f} kHz, 50% duty: current ripple {max(ii)-min(ii):.2f} A peak-to-peak "
              f"(formula V D(1-D)/(L f) = {ripple_formula:.2f} A); mean {np.mean(ii):.1f} A")
    print("ripple falls as 1/f; switching losses rise with f (silicon ~20 kHz above hearing, GaN 50-100 kHz)")


def h10_foc_transforms():
    p, lam = 14, 0.008                        # pole pairs, flux linkage (Wb)
    iq_ref, id_ref = 10.0, 0.0
    th_m = np.linspace(0, 2 * np.pi / p, 50); th_e = p * th_m
    ia = -iq_ref * np.sin(th_e); ib = -iq_ref * np.sin(th_e - 2 * np.pi / 3); ic = -iq_ref * np.sin(th_e + 2 * np.pi / 3)
    al = (2 / 3) * (ia - 0.5 * ib - 0.5 * ic); be = (2 / 3) * (np.sqrt(3) / 2) * (ib - ic)     # Clarke
    def park(th):
        return al * np.cos(th) + be * np.sin(th), -al * np.sin(th) + be * np.cos(th)
    d, q = park(th_e)
    print(f"Clarke + Park of balanced phase currents: id = {d.mean():+.3f} A, iq = {q.mean():+.3f} A (constant; "
          f"phase-current peak {np.abs(ia).max():.1f} A)")
    print(f"torque = 1.5 p lambda iq = {1.5*p*lam*iq_ref:.2f} N m")
    for err_mech_deg in [0.5, 1.0, 3.0]:
        e = np.radians(err_mech_deg) * p
        d2, q2 = park(th_e + e)
        print(f"  encoder offset {err_mech_deg:.1f} deg mechanical = {np.degrees(e):.0f} deg electrical: "
              f"torque-producing current {q2.mean():.2f} A ({q2.mean()/iq_ref:.1%}), stray id {d2.mean():+.2f} A")


def h11_current_loop_design():
    R, L = MOTOR["R"], MOTOR["L"]
    fs = 20e3; Ts = 1 / fs
    for fc in [1000, 2500, 4500]:
        wc = 2 * np.pi * fc
        pm = 90 - np.degrees(wc * 1.5 * Ts)          # 1 sample compute + half-sample PWM delay
        kp, ki = L * wc, R * wc                      # PI zero cancels the electrical pole
        i, integ, hist, peak = 0.0, 0.0, [0.0], 0.0
        sub = 50; dt = Ts / sub
        for k in range(int(0.01 / Ts)):
            e = 1.0 - i; integ += e * Ts
            hist.append(kp * e + ki * integ); v = hist.pop(0)   # applied one sample late
            for _ in range(sub):
                i += (v - R * i) / L * dt
            peak = max(peak, i)
        res = "UNSTABLE" if peak > 10 else f"step overshoot {100*(peak-1):4.1f}%"
        print(f"current-loop bandwidth {fc:4d} Hz at 20 kHz sampling (delay 1.5 samples): phase margin {pm:5.1f} deg -> {res}")


# ================================================================== III. sensing and signals
def h12_encoder_velocity():
    rng = np.random.default_rng(1)
    cpr, fs, w_true = 4096, 10e3, 2.0          # 12-bit encoder, 10 kHz loop, slow 2 rad/s
    t = np.arange(0, 1.0, 1 / fs)
    q = w_true * t + 0.3 * np.sin(2 * np.pi * 1 * t) / (2 * np.pi)
    wt = w_true + 0.3 * np.cos(2 * np.pi * 1 * t)
    qm = np.floor(q / (2 * np.pi / cpr)) * (2 * np.pi / cpr)
    lsb = 2 * np.pi / cpr * fs
    d = np.diff(qm, prepend=qm[0]) * fs
    n = 100; avg = np.convolve(d, np.ones(n) / n, "same")
    # tracking observer (PLL): second-order, bandwidth 50 Hz
    wn = 2 * np.pi * 50; qh = wh = 0.0; obs = []
    for z in qm:
        e = z - qh; qh += (wh + 2 * wn * e) / fs; wh += wn * wn * e / fs; obs.append(wh)
    obs = np.array(obs)
    sl = slice(2000, -200)
    print(f"velocity quantum of plain differencing: {lsb:.1f} rad/s (true speed {w_true} rad/s)")
    for name, est, lag in [("differencing", d, 0.05), (f"{n}-sample average", avg, 0.0), ("tracking observer 50 Hz", obs, 1 / (2 * np.pi * 50) * 2)]:
        print(f"  {name:24s}: RMS error {np.sqrt(np.mean((est[sl]-wt[sl])**2)):.3f} rad/s")
    print("averaging over a centred window looks good offline but adds half the window (5 ms) of delay online")


def h13_sampling_aliasing_adc():
    fs = 1000.0
    t = np.arange(0, 1, 1 / fs)
    x = np.sin(2 * np.pi * 1100 * t)
    f = np.fft.rfftfreq(len(t), 1 / fs); X = np.abs(np.fft.rfft(x))
    print(f"1100 Hz interference sampled at 1 kHz appears at {f[np.argmax(X)]:.0f} Hz")
    for fc in [300.0, 100.0]:
        att = 1 / np.sqrt(1 + (1100 / fc) ** 2)
        att2 = 1 / (1 + (1100 / fc) ** 2)
        print(f"  RC anti-alias filter at {fc:.0f} Hz: 1100 Hz attenuated to {att:.1%} (1st order), {att2:.2%} (2nd order); "
              f"phase lag at 30 Hz {np.degrees(np.arctan(30/fc)):.1f} deg (1st order)")
    rng = np.random.default_rng(0)
    for bits in [10, 12, 16]:
        s = 0.99 * np.sin(2 * np.pi * 13.7 * np.arange(200000) / 20000)
        q = np.round(s * 2 ** (bits - 1)) / 2 ** (bits - 1)
        snr = 10 * np.log10(np.mean(s**2) / np.mean((q - s) ** 2))
        print(f"  {bits}-bit ADC: measured SNR {snr:.1f} dB (rule 6.02N + 1.76 = {6.02*bits+1.76:.1f} dB)")


def h14_filter_noise_vs_lag():
    rng = np.random.default_rng(2)
    fs, fcross = 10e3, 30.0
    noise = rng.normal(0, 1, 200000)
    for fc in [1000, 200, 50]:
        a = 1 - np.exp(-2 * np.pi * fc / fs)
        y = np.zeros_like(noise); acc = 0.0
        for i, v in enumerate(noise):
            acc += a * (v - acc); y[i] = acc
        lag = np.degrees(np.arctan(fcross / fc))
        print(f"low-pass {fc:5d} Hz: noise RMS {y[1000:].std():.3f} (input 1.000); phase lag at the {fcross:.0f} Hz crossover {lag:4.1f} deg "
              f"(= {lag/360/fcross*1e3:.2f} ms of delay)")


# ================================================================== IV. embedded real-time
def h15_discretization():
    wc_hz = 50.0
    for Ts in [1e-3, 1e-4]:
        print(f"Ts = {Ts*1e3:.1f} ms: zero-order hold adds Ts/2 delay -> phase loss {np.degrees(2*np.pi*wc_hz*Ts/2):.1f} deg "
              f"at a {wc_hz:.0f} Hz crossover")
    a = 2 * np.pi * 200.0                       # discretize the low-pass a/(s+a) at Ts = 1 ms
    Ts = 1e-3; w = 2 * np.pi * 100.0
    z = np.exp(1j * w * Ts)
    H = a / (1j * w + a)
    Hf = a * Ts / (z - 1 + a * Ts)                         # forward Euler s -> (z-1)/Ts
    Hb = a * Ts * z / (z * (1 + a * Ts) - 1)               # backward Euler s -> (z-1)/(z Ts)
    Ht = a / (2 / Ts * (z - 1) / (z + 1) + a)               # Tustin
    p = np.exp(-a * Ts); Hz = (1 - p) / (z - p)             # zero-order-hold equivalent
    for name, Hd in [("forward Euler", Hf), ("backward Euler", Hb), ("Tustin", Ht), ("ZOH equivalent*", Hz)]:
        print(f"  200 Hz low-pass at 1 kHz, response at 100 Hz: {name:15s} gain error {abs(Hd)/abs(H)-1:+.1%}, "
              f"phase error {np.degrees(np.angle(Hd/H)):+.1f} deg")
    print("  * the ZOH equivalent is exact at the sampling instants; its extra phase is the hold's real Ts/2 delay")
    for fc in [200.0, 400.0]:
        aa = 2 * np.pi * fc
        print(f"  forward Euler pole for a {fc:.0f} Hz filter at 1 kHz: {1-aa*Ts:+.3f} -> {'stable' if abs(1-aa*Ts) < 1 else 'UNSTABLE'}")


def h16_fixed_point():
    a = 0.001                                   # slow low-pass y += a (x - y)
    x = 0.5
    for name, frac in [("float", None), ("Q15", 15), ("Q31", 31)]:
        y = 0.0
        if frac is None:
            for _ in range(20000):
                y += a * (x - y)
        else:
            A = int(round(a * 2**frac)); X = int(x * 2**frac); Y = 0
            for _ in range(20000):
                Y += (A * (X - Y)) >> frac         # truncating multiply, as on a fixed-point DSP
            y = Y / 2**frac
        print(f"{name:5s}: coefficient {a if frac is None else round(a*2**frac)/2**frac:.6f}; output after 20000 steps "
              f"{y:.6f} (target 0.5, error {abs(0.5-y):.2e})")
    print("Q15 stalls once a*(x-y) drops below one LSB: the filter output gets stuck short of the target")


def h17_cascade_loops():
    J = 1e-3
    def run(sep):
        wp = 2 * np.pi * 5.0; wv = wp * sep; wi = wv * sep          # position, velocity and current bandwidths
        kv, kiv = J * wv, J * wv * wv / 4
        q = v = tau = integ = 0.0; dt = 1e-5; qs = []
        for _ in range(int(1.0 / dt)):
            vref = wp * (1.0 - q)
            e = vref - v; integ += e * dt
            tref = kv * e + kiv * integ
            tau += wi * (tref - tau) * dt                           # current loop as a first-order lag
            v += tau / J * dt; q += v * dt; qs.append(q)
        qs = np.array(qs)
        return max(0.0, 100 * (qs.max() - 1)), np.argmax(qs > 0.98) * dt
    for sep in [8, 4, 2]:
        os_, t98 = run(sep)
        print(f"bandwidth separation {sep} x per loop: position overshoot {os_:5.1f}%, reaches 98% at {t98*1e3:.0f} ms")


def h18_anti_windup():
    J, tmax = 1e-3, 0.2
    kp, ki = 0.05, 2.0
    for mode in ["none", "clamping", "back-calculation"]:
        v = integ = 0.0; dt = 1e-4; vs = []
        for _ in range(int(1.0 / dt)):
            e = 100.0 - v
            u = kp * e + ki * integ
            us = np.clip(u, -tmax, tmax)
            if mode == "none":
                integ += e * dt
            elif mode == "clamping":
                if u == us or np.sign(e) != np.sign(u):
                    integ += e * dt
            else:
                integ += (e + (us - u) / (kp * 0.5)) * dt
            v += us / J * dt; vs.append(v)
        vs = np.array(vs)
        print(f"{mode:16s}: overshoot {vs.max()-100:5.1f} rad/s on a 100 rad/s step with torque limited to {tmax} N m")


def h19_rate_monotonic():
    tasks = [("current loop", 50e-6, 15e-6), ("velocity loop", 250e-6, 40e-6), ("position loop", 1e-3, 120e-6),
             ("communication", 1e-3, 200e-6), ("logging", 10e-3, 900e-6)]
    U = sum(c / T for _, T, c in tasks); n = len(tasks)
    bound = n * (2 ** (1 / n) - 1)
    print(f"utilization {U:.3f}; Liu-Layland bound for {n} tasks {bound:.3f} -> {'schedulable by the bound' if U <= bound else 'bound inconclusive'}")
    order = sorted(tasks, key=lambda t: t[1])
    for i, (name, T, c) in enumerate(order):                   # exact response-time analysis
        R = c
        while True:
            Rn = c + sum(np.ceil(R / Tj) * cj for _, Tj, cj in order[:i])
            if Rn == R or Rn > T:
                break
            R = Rn
        print(f"  {name:13s}: period {T*1e6:6.0f} us, worst-case response {Rn*1e6:6.0f} us -> {'OK' if Rn <= T else 'MISSES DEADLINE'}")


def h20_bus_budget():
    joints, rate = 12, 1000.0
    can_bits = 135                               # worst-case standard-ID CAN frame with 8 data bytes, incl. stuffing
    can_max = 1e6 / can_bits
    need = 2 * joints * rate                     # one command and one feedback frame per joint per cycle
    print(f"CAN 1 Mbit/s: at most {can_max:.0f} frames/s; {joints} joints x 2 frames x {rate:.0f} Hz = {need:.0f} frames/s "
          f"-> {need/can_max:.0%} load ({'feasible' if need/can_max < 0.7 else 'needs several buses'})")
    for buses in [2, 4]:
        print(f"  split over {buses} buses: {need/buses/can_max:.0%} load each")
    fd_bits = 29 + 64 * 8 / 5 + 40                # arbitration ~29 bits at 1 Mbit/s, data phase at 5 Mbit/s (approximate)
    fd_time = (29 + 40) / 1e6 + 64 * 8 / 5e6
    print(f"CAN FD (64 bytes, 5 Mbit/s data phase): about {fd_time*1e6:.0f} us per frame, carrying all 12 joints' commands in one frame")
    payload, overhead, per_slave_us = joints * 32, 38 + 2 + 12, 1.0   # bytes; Ethernet + EtherCAT header; assumed forwarding delay
    cyc = (payload + overhead) * 8 / 100e6 + joints * per_slave_us * 1e-6
    print(f"EtherCAT 100 Mbit/s: one frame for {joints} x 32 bytes takes about {cyc*1e6:.0f} us round trip "
          f"(assuming {per_slave_us:.0f} us per slave) -> cycle times of 100-250 us are routine")


# ================================================================== V. software engineering and safety
STATES = ["NOT_READY", "SWITCH_ON_DISABLED", "READY", "SWITCHED_ON", "OPERATION_ENABLED", "QUICK_STOP", "FAULT"]
TRANS = {("NOT_READY", "boot_ok"): "SWITCH_ON_DISABLED", ("SWITCH_ON_DISABLED", "shutdown"): "READY",
         ("READY", "switch_on"): "SWITCHED_ON", ("SWITCHED_ON", "enable"): "OPERATION_ENABLED",
         ("OPERATION_ENABLED", "disable"): "SWITCHED_ON", ("OPERATION_ENABLED", "quick_stop"): "QUICK_STOP",
         ("QUICK_STOP", "stopped"): "SWITCH_ON_DISABLED", ("FAULT", "fault_reset"): "SWITCH_ON_DISABLED",
         ("SWITCHED_ON", "shutdown"): "READY", ("READY", "disable_voltage"): "SWITCH_ON_DISABLED"}


def _drive_step(state, event, watchdog_ms):
    if event in ("overcurrent", "overtemp", "encoder_lost"):
        return "FAULT"
    if state == "OPERATION_ENABLED" and watchdog_ms > 5:          # no command for 5 ms: stop safely
        return "QUICK_STOP"
    return TRANS.get((state, event), state)


def h21_drive_state_machine():
    seq = ["boot_ok", "shutdown", "switch_on", "enable", "tick", "tick", "comm_loss", "stopped", "enable", "overtemp", "enable", "fault_reset"]
    s, wd = "NOT_READY", 0
    trace = []
    for ev in seq:
        wd = wd + 3 if ev == "comm_loss" else (wd + 1 if ev == "tick" else 0)
        if ev == "comm_loss":
            wd = 6
        s = _drive_step(s, ev, wd); trace.append(f"{ev}->{s}")
    print("scripted run: " + ", ".join(trace))
    rng = np.random.default_rng(0)
    events = ["boot_ok", "shutdown", "switch_on", "enable", "disable", "quick_stop", "stopped", "fault_reset",
              "disable_voltage", "overcurrent", "overtemp", "encoder_lost", "tick", "comm_loss"]
    violations = enabled_from_fault = 0
    for _ in range(10000):                                        # property-based test with random event sequences
        s, wd, prev = "NOT_READY", 0, None
        for ev in rng.choice(events, 40):
            wd = 6 if ev == "comm_loss" else (wd + 1 if ev == "tick" else 0)
            prev, s = s, _drive_step(s, ev, wd)
            torque_allowed = s == "OPERATION_ENABLED"
            if torque_allowed and ev in ("overcurrent", "overtemp", "encoder_lost"):
                violations += 1
            if prev == "FAULT" and s == "OPERATION_ENABLED":
                enabled_from_fault += 1
    print(f"10,000 random sequences x 40 events: torque enabled during a fault event {violations} times; "
          f"FAULT -> OPERATION_ENABLED without a reset {enabled_from_fault} times")


def h22_safety_numbers():
    lam_d, DC, beta, T = 2e-6, 0.90, 0.02, 8760.0        # dangerous failure rate /h, diagnostic coverage, common cause, proof test interval
    lam_du = lam_d * (1 - DC)
    pfh_1oo1 = lam_du
    pfh_1oo2 = 2 * ((1 - beta) * lam_du) ** 2 * T / 2 + beta * lam_du
    pfh_1oo2_nocc = 2 * (lam_du) ** 2 * T / 2
    def band(p):
        pl = "e (highest)" if p < 1e-7 else "d" if p < 1e-6 else "c" if p < 3e-6 else "b" if p < 1e-5 else "a"
        sil = ("SIL 4 band" if p < 1e-8 else "SIL 3 band" if p < 1e-7 else "SIL 2 band" if p < 1e-6
               else "SIL 1 band" if p < 1e-5 else "below SIL 1")
        return pl, sil
    print(f"single channel: MTTFd {1/lam_d/8760:.0f} years, DC {DC:.0%} -> PFH {pfh_1oo1:.1e}/h -> PL {band(pfh_1oo1)[0]}, {band(pfh_1oo1)[1]}")
    print(f"two channels (1oo2), beta {beta:.0%}: PFH {pfh_1oo2:.1e}/h -> PL {band(pfh_1oo2)[0]}, {band(pfh_1oo2)[1]}; "
          f"common cause contributes {beta*lam_du/pfh_1oo2:.0%}")
    print("  (simplified formulas; a SIL claim also needs architectural constraints and systematic capability)")
    print(f"  without common cause the same pair would reach {pfh_1oo2_nocc:.1e}/h: diversity and separation matter more than adding channels")


def _pi_float(e, st, kp=0.8, ki=40.0, lim=1.0, dt=1e-3):
    i = st + ki * e * dt
    u = kp * e + i
    if abs(u) > lim:
        i = st                                    # clamping anti-windup
        u = np.clip(kp * e + i, -lim, lim)
    return u, i


def _pi_fixed(e, st, bug=False, kp=0.8, ki=40.0, lim=1.0, dt=1e-3, Q=24):
    S = 2 ** Q
    rnd = lambda x: (x + (1 << (Q - 1))) >> Q     # rounding (not truncating) multiply
    E, I = int(round(e * S)), st
    KP, KIDT = int(round(kp * S)), int(round(ki * dt * S))
    I2 = I + rnd(KIDT * E)
    U = rnd(KP * E) + I2
    L = int(lim * S)
    if abs(U) > L:
        I2 = I if not bug else I2 + 0        # injected bug: anti-windup removed
        U = max(-L, min(L, rnd(KP * E) + I2))
    return U / S, I2


def h23_back_to_back_test():
    rng = np.random.default_rng(4)
    worst = {False: 0.0, True: 0.0}
    for bug in [False, True]:
        for _ in range(200):                      # 200 random test vectors of 500 samples
            e_seq = np.cumsum(rng.normal(0, 0.05, 500)); e_seq = np.clip(e_seq, -0.99, 0.99)
            sf, sx = 0.0, 0
            for e in e_seq:
                uf, sf = _pi_float(e, sf)
                ux, sx = _pi_fixed(e, sx, bug=bug)
                worst[bug] = max(worst[bug], abs(uf - ux))
    tol = 1e-3
    for bug in [False, True]:
        print(f"{'Q24 build with anti-windup removed' if bug else 'Q24 build (correct)               '}: "
              f"max deviation from the float model {worst[bug]:.2e} -> {'FAIL' if worst[bug] > tol else 'pass'} (tolerance {tol})")


RECIPES = {name: fn for name, fn in globals().items() if name.startswith("h") and name[1:3].isdigit()}

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, fn in RECIPES.items():
        if pattern in name:
            print(f"\n=== {name} ===")
            fn()
