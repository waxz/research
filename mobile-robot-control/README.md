# Mobile robot control: forklifts, AGVs and AMRs

How wheeled industrial robots are controlled, analysed the same way as the humanoid collection in [`../robot-learning-control`](../robot-learning-control/). It covers model-based control, self-exploration reinforcement learning, and reference/imitation methods, plus the math behind them, with a paper catalog.

## Start here

| Read | What it covers |
|---|---|
| [REPORT.md](REPORT.md) | The analysis: vehicle families, the layered control stack, why control is hard, model-based vs RL vs reference methods, reference-based vs self-exploration, which method fits which task, year-by-year breakthroughs, safety standards, and quick-start textbooks |
| [cookbook/COOKBOOK.md](cookbook/COOKBOOK.md) | 22 math recipes (M1–M22): kinematics (differential drive, forklift tricycle, mecanum), odometry, EKF reflector localization, AMCL, ICP and pose-graph SLAM, costmaps, A* and Hybrid A*, speed profiles and safety fields, pure pursuit / Stanley / Kanayama / MPC / MPPI, DWA, docking, forklift tip-over stability, fleet management, RL navigation with safety filters, navigation foundation models |
| [CATALOG.md](CATALOG.md) | 49 papers, surveys and standards in 8 categories, each with a DOI or arXiv link; 8 open-access PDFs saved locally |

The rendered pages in [`html/`](html/) show equations and diagrams; download them and open in a browser. Every worked example is reproduced by [`cookbook/examples.py`](cookbook/examples.py) (NumPy only; `python3 cookbook/examples.py m19`).

## Layout

```
mobile-robot-control/
├── README.md
├── REPORT.md                 analysis report (source)
├── CATALOG.md / catalog.csv  generated paper catalog
├── catalog.json              source of truth for the catalog
├── cookbook/
│   ├── COOKBOOK.md           math recipes M1–M22 (source)
│   └── examples.py           runnable worked examples
├── html/
│   ├── report.html           rendered REPORT.md
│   └── cookbook.html         rendered COOKBOOK.md
├── papers/<category>/        open-access PDFs
└── tools/
    ├── build_catalog.py      regenerates CATALOG.md / catalog.csv, downloads PDFs
    └── render_md.py          renders any Markdown file (math + mermaid) to HTML
```

To rebuild after editing: `python3 tools/build_catalog.py --download`, then `python3 tools/render_md.py REPORT.md html/report.html "Forklift, AGV and AMR Control"`. For the cookbook, run the same renderer on `cookbook/COOKBOOK.md`.

## Notes on sources

- **PDF links.** In each catalog, **PDF** is a copy stored in this repository and **PDF ↗** opens the paper's PDF online. Every arXiv entry links its arXiv PDF; journal, NASA and conference papers link an open PDF where one was found and checked. To add one, set `pdf_url` in `catalog.json`; `python3 tools/build_catalog.py --check` verifies non-arXiv PDF links.
- All DOIs were resolved through Crossref, and all arXiv IDs checked against the arXiv API, on 26 Oct 2026. Journal papers and standards are linked, not copied.
- Industry figures are company-reported: Kiva's productivity "factor of two or more", Amazon's DeepFleet 10% travel-efficiency aim. The report labels them that way.
- Sources disagree on the date (1953 vs 1954) and wire placement of Barrett's first driverless tow tractor; the report says so.
- Fit ratings and the task map are a synthesis of the surveys, not measured results.
