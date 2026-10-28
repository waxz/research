# Control and estimation theory: from PID to learning

A history and analysis of automatic control and state estimation. On the control side it runs from Maxwell's governor and PID through frequency-domain, state-space, optimal, robust, adaptive, nonlinear and predictive control. On the estimation side it runs from least squares through the Wiener, Kalman, extended, unscented and particle filters to smoothing and moving-horizon estimation. Both end with today's learning-based control and estimation. The format matches the other collections in this repository.

## Start here

| Read | What it covers |
|---|---|
| [REPORT.md](REPORT.md) | The control/estimation duality; eras and what pushed each one; control and estimation methods compared; where learning helps (ten patterns); physics-first vs data-first; which method for which application; breakthroughs from 1795 to 2026; recurring lessons; quick-start textbooks |
| [cookbook/COOKBOOK.md](cookbook/COOKBOOK.md) | 26 math recipes. **C1–C12:** feedback, stability, PID and Ziegler–Nichols, margins, pole placement, LQR vs LQG, dynamic programming and the maximum principle, robust control, MRAC, sliding mode, MPC, system ID. **E1–E8:** RLS, Wiener, Kalman and duality, EKF, UKF, particle filters, RTS and MHE, NEES/NIS. **L1–L6:** SINDy and Koopman, RL vs Riccati, DeePC, safe learning, KalmanNet-style learned gains, differentiable control |
| [CATALOG.md](CATALOG.md) | 49 papers, from Maxwell (1868) to KalmanNet (2022), in 9 categories, each with a DOI or arXiv link; 10 open-access PDFs saved locally |

The rendered pages in [`html/`](html/) show equations and diagrams; download them and open in a browser. Every worked example is reproduced by [`cookbook/examples.py`](cookbook/examples.py) (NumPy only; `python3 cookbook/examples.py c11`).

## Layout

```
control-estimation-theory/
├── README.md
├── REPORT.md                 analysis report (source)
├── CATALOG.md / catalog.csv  generated catalog
├── catalog.json              source of truth for the catalog
├── cookbook/
│   ├── COOKBOOK.md           math recipes C1–C12, E1–E8, L1–L6 (source)
│   └── examples.py           runnable worked examples
├── html/                     rendered report.html and cookbook.html
├── papers/<category>/        open-access PDFs
└── tools/                    build_catalog.py, render_md.py
```

To rebuild: `python3 tools/build_catalog.py --download`, then `python3 tools/render_md.py REPORT.md html/report.html "From PID to Learning"`. Do the same for `cookbook/COOKBOOK.md`.

## Notes on sources

- **PDF links.** In each catalog, **PDF** is a copy stored in this repository and **PDF ↗** opens the paper's PDF online. Every arXiv entry links its arXiv PDF; journal, NASA and conference papers link an open PDF where one was found and checked. To add one, set `pdf_url` in `catalog.json`; `python3 tools/build_catalog.py --check` verifies non-arXiv PDF links.
- Every DOI was resolved through Crossref and every arXiv ID checked against the arXiv API on 27 Oct 2026.
- **PID share:** "about 90% of loops are PID" comes from Åström & Hägglund (2001). The often-quoted "more than 95% in process control" comes from their later book. In the IFAC industry survey, 91% of respondents rated PID's current impact as high.
- **X-15 accident:** the account is summarized from NASA history pages. The authoritative analysis is NASA/TM-2014-218538, which I did not retrieve.
- **Synthesis:** fit ratings and the application map are a synthesis of the surveys, not measurements.
