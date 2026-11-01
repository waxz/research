# Sim-to-real: the reality gap in reinforcement learning

Why policies trained in simulation fail on real robots, and what fixes them. Covers actuator and contact modelling, system identification, domain randomization, adaptation, residual and learned models, real-to-sim reconstruction, how to measure the gap, and the latest achievements and trends. The format matches the other collections in this repository.

## Start here

| Read | What it covers |
|---|---|
| [REPORT.md](REPORT.md) | Sources of the gap; how simulators model contact and where it breaks; actuator modelling levels; nine strategy families compared; close-the-gap vs design-around-it; measuring the gap; which approach for which task; breakthroughs from 1995 to 2026; latest trends; a practical checklist; quick-start reading and tools |
| [cookbook/COOKBOOK.md](cookbook/COOKBOOK.md) | 16 math recipes (G1–G16): motor torque–speed limits, latency and stability, friction dead bands, learned actuator models, soft-contact stiffness and time step, friction-cone linearization, restitution, least-squares and Bayesian identification, domain randomization and its range trade-off, automatic DR, online adaptation, delta-action models, sim-vs-real correlation, integrators |
| [CATALOG.md](CATALOG.md) | 55 papers in 8 categories, each with an arXiv ID or DOI; PDF links online for every arXiv entry; 16 PDFs saved locally |

The rendered pages in [`html/`](html/) show equations and diagrams; download them and open in a browser. Every worked example is reproduced by [`cookbook/examples.py`](cookbook/examples.py) (NumPy only; `python3 cookbook/examples.py g02`).

## Layout

```
sim2real/
├── README.md
├── REPORT.md                 analysis report (source)
├── CATALOG.md / catalog.csv  generated catalog
├── catalog.json              source of truth for the catalog
├── cookbook/
│   ├── COOKBOOK.md           math recipes G1–G16 (source)
│   └── examples.py           runnable worked examples
├── html/                     rendered report.html and cookbook.html
├── papers/<category>/        open-access PDFs
└── tools/                    build_catalog.py, render_md.py
```

To rebuild: `python3 tools/build_catalog.py --download --check`, then `python3 tools/render_md.py REPORT.md html/report.html "Sim-to-Real Gap"`. Do the same for `cookbook/COOKBOOK.md`.

## Notes on sources

- **PDF links.** In the catalog, **PDF** is a copy stored in this repository and **PDF ↗** opens the paper's PDF online. To add one, set `pdf_url` in `catalog.json`.
- All arXiv IDs were checked against the arXiv API, and all DOIs through Crossref, on 1 Nov 2026. Quoted results come from the papers' abstracts.
- The cookbook's numbers are illustrative models, not measurements of specific robots.
- Fit ratings and the task map are a synthesis, not measurements.
