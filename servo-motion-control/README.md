# Servo and motion control: from FOC to industrial robot arms

How electric motion is controlled, layer by layer:
- field-oriented control inside the drive;
- cascaded current, speed and position PID loops on one axis;
- the techniques high-precision servos add;
- how industrial and collaborative robot arms coordinate many servo axes.

The format matches the other collections in this repository.

## Start here

| Read | What it covers |
|---|---|
| [REPORT.md](REPORT.md) | The control hierarchy and loop rates; FOC elements; cascaded PID structures and a tuning workflow; a precision error budget with fixes; robot-arm control functions; how problems scale from one motor to a robot; which method for which task; breakthroughs 1929–2026; trends; a commissioning checklist; reading |
| [cookbook/COOKBOOK.md](cookbook/COOKBOOK.md) | 25 recipes (V1–V25), with a reading list for each part:<br>• **FOC:** dq decoupling, voltage limits and SVPWM, field weakening and MTPA, dead time, sensorless limits<br>• **One axis:** speed-loop design, inertia and friction identification, disturbance observer, feedforward, motion profiles, frequency-response measurement, notch filters<br>• **Precision:** inverse feedforward, ZPETC, ILC, cogging tables, quadrant glitch, contouring<br>• **Robot arms:** reflected inertia, computed torque, input shaping, dynamic identification, collision detection, impedance control, ISO 9283 |
| [CATALOG.md](CATALOG.md) | 40 entries in 6 categories, each with a DOI, arXiv ID or official page; 8 PDFs saved locally |

The rendered pages in [`html/`](html/) show equations and diagrams; download them and open in a browser. Every worked example is reproduced by [`cookbook/examples.py`](cookbook/examples.py) (NumPy only; `python3 cookbook/examples.py v09`).

## Layout

```
servo-motion-control/
├── README.md
├── REPORT.md                 analysis report (source)
├── CATALOG.md / catalog.csv  generated catalog
├── catalog.json              source of truth for the catalog
├── cookbook/
│   ├── COOKBOOK.md           recipes V1–V25 (source)
│   └── examples.py           runnable worked examples
├── html/                     rendered report.html and cookbook.html
├── papers/<category>/        open-access PDFs
└── tools/                    build_catalog.py, render_md.py
```

To rebuild: `python3 tools/build_catalog.py --download --check`, then `python3 tools/render_md.py REPORT.md html/report.html "Servo and Motion Control"`. Do the same for `cookbook/COOKBOOK.md`.

## Related collections

- [control-systems-engineering/](../control-systems-engineering/): motors, PWM, encoders, sampling, real-time computing, buses, safety and testing.
- [stability-analysis/](../stability-analysis/): margins, describing functions, passivity and certificates.
- [sim2real/](../sim2real/): what a simulated actuator model must reproduce of these servo loops.
- [control-estimation-theory/](../control-estimation-theory/): PID, optimal, robust and predictive control in general form.

## Notes on sources

- **Verification.** All DOIs were checked through Crossref, and all arXiv IDs against the arXiv API, on 10 Nov 2026. Quoted results come from the papers' abstracts.
- **Synthesis.** The cookbook's numbers come from small illustrative systems with plausible values; some compensations are idealized. Typical loop rates, bandwidths and accuracies, and the task-map ratings, reflect common practice, not product data.
