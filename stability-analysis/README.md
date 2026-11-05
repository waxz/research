# Stability analysis: from Lyapunov to neural-network control

How to show that a closed loop is stable, and how those methods carry over to learned and neural-network controllers. It covers Lyapunov's method, margins and delay, absolute stability, passivity, ISS and small gain, control Lyapunov and barrier functions, Poincaré maps for gaits, contraction, learned certificates and neural-network verification. The format matches the other collections in this repository.

## Start here

| Read | What it covers |
|---|---|
| [REPORT.md](REPORT.md) | Definitions of stability; method families compared; why neural controllers are hard to certify; which method for which task; breakthroughs from 1868 to 2026; latest trends; limitations; a practical checklist; quick-start reading and tools; the link to sim-to-real actuator models |
| [cookbook/COOKBOOK.md](cookbook/COOKBOOK.md) | 17 math recipes (S1–S17), each with a quick-start reading list per part: linearization, Lyapunov equation, LaSalle, regions of attraction, gain/phase/delay margins, circle and Popov criteria, describing functions, passivity, ISS and bounded residuals, small gain with network Lipschitz bounds, control Lyapunov functions, control barrier functions, Poincaré maps, contraction, learned Lyapunov functions, bound propagation, Lyapunov-checked policy updates |
| [CATALOG.md](CATALOG.md) | 61 entries in 7 categories, each with an arXiv ID, DOI or stable URL; PDF links online for every arXiv entry; 14 PDFs saved locally |

The rendered pages in [`html/`](html/) show equations and diagrams; download them and open in a browser. Every worked example is reproduced by [`cookbook/examples.py`](cookbook/examples.py) (NumPy only; `python3 cookbook/examples.py s05`).

## Layout

```
stability-analysis/
├── README.md
├── REPORT.md                 analysis report (source)
├── CATALOG.md / catalog.csv  generated catalog
├── catalog.json              source of truth for the catalog
├── cookbook/
│   ├── COOKBOOK.md           math recipes S1–S17 (source)
│   └── examples.py           runnable worked examples
├── html/                     rendered report.html and cookbook.html
├── papers/<category>/        open-access PDFs
└── tools/                    build_catalog.py, render_md.py
```

To rebuild: `python3 tools/build_catalog.py --download --check`, then `python3 tools/render_md.py REPORT.md html/report.html "Stability Analysis"`. Do the same for `cookbook/COOKBOOK.md`.

## Related collections

- [control-estimation-theory/](../control-estimation-theory/): PID to optimal, robust, adaptive and learning-based control and estimation.
- [sim2real/](../sim2real/): actuator models and the sim-to-real gap; recipe S9 gives the stability argument for bounded learned residuals.

## Notes on sources

- **PDF links.** In the catalog, **PDF** is a copy stored in this repository and **PDF ↗** opens the paper's PDF online. To add one, set `pdf_url` in `catalog.json`.
- **Verification.** All arXiv IDs were checked against the arXiv API, and all DOIs through Crossref, on 5 Nov 2026. Quoted results come from the papers' abstracts.
- **Venues.** Venues of arXiv papers without a journal reference on arXiv are given as recalled; check before citing.
- **Synthesis.** The cookbook's numbers come from small illustrative systems. The fit ratings and task map are a synthesis, not measurements.
