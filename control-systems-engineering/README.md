# Control systems engineering: from physics to software

The mechanical, electrical, embedded and software background that every automatic control system rests on. It goes from the physical laws, through transmissions, motors, power electronics and sensors, to real-time computing, communication buses, software architecture, functional safety and testing. The format matches the other collections in this repository.

## Start here

| Read | What it covers |
|---|---|
| [REPORT.md](REPORT.md) | The layers of a control system and what each adds to the loop; the physics underneath; mechanical and electrical design choices compared; embedded and real-time computing; software engineering practices; safety standards; which choices for which application; breakthroughs from 1687 to 2025; trends; a 14-step checklist; quick-start books, courses and documentation |
| [cookbook/COOKBOOK.md](cookbook/COOKBOOK.md) | 23 recipes (H1–H23), with a reading list for each part:<br>• **Mechanics:** torque sizing, gear ratio and reflected inertia, two-mass resonance, friction and stick-slip, backlash<br>• **Electrical:** DC-motor time constants, torque–speed, thermal derating, PWM ripple, FOC and encoder offset, current-loop design<br>• **Sensing:** encoder velocity estimation, aliasing and ADCs, filter delay<br>• **Embedded:** discretization, fixed point, cascaded loops, anti-windup, real-time scheduling, CAN/CAN FD/EtherCAT budgets<br>• **Software and safety:** drive state machines with property-based tests, safety-integrity numbers, back-to-back testing |
| [CATALOG.md](CATALOG.md) | 55 entries in 7 categories: papers with DOIs or arXiv IDs, free books and courses, standards and documentation; 9 PDFs saved locally |

The rendered pages in [`html/`](html/) show equations and diagrams; download them and open in a browser. Every worked example is reproduced by [`cookbook/examples.py`](cookbook/examples.py) (NumPy only; `python3 cookbook/examples.py h09`).

## Layout

```
control-systems-engineering/
├── README.md
├── REPORT.md                 analysis report (source)
├── CATALOG.md / catalog.csv  generated catalog
├── catalog.json              source of truth for the catalog
├── cookbook/
│   ├── COOKBOOK.md           recipes H1–H23 (source)
│   └── examples.py           runnable worked examples
├── html/                     rendered report.html and cookbook.html
├── papers/<category>/        open-access PDFs
└── tools/                    build_catalog.py, render_md.py
```

To rebuild: `python3 tools/build_catalog.py --download --check`, then `python3 tools/render_md.py REPORT.md html/report.html "Control Systems Engineering"`. Do the same for `cookbook/COOKBOOK.md`.

## Related collections

- [control-estimation-theory/](../control-estimation-theory/): the control and estimation laws these layers implement.
- [stability-analysis/](../stability-analysis/): delay margins, describing functions, anti-windup and bounded-residual arguments used here.
- [sim2real/](../sim2real/): which of these hardware effects a simulation actuator model must reproduce.
- [mobile-robot-control/](../mobile-robot-control/): AGV and AMR control, and the ISO 3691-4 safety standard.

## Notes on sources

- **Verification.** All DOIs were checked through Crossref, and all arXiv IDs against the arXiv API, on 9 Nov 2026. Quoted results come from the papers' abstracts.
- **Standards.** Standards are paywalled; the catalog links to their official pages.
- **PDF links.** **PDF** is a copy stored in this repository and **PDF ↗** opens it online. The ROS 2 review (17 MB) is linked, not stored.
- **Synthesis.** The cookbook's numbers come from small illustrative systems with plausible values. The fit ratings and loop-rate tables reflect common practice, not survey data.
