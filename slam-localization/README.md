# SLAM and localization: lasers, LiDAR, cameras, IMUs and encoders

How mobile robots, self-driving cars and spacecraft know where they are. The spacecraft range from Apollo and the Space Shuttle to Mars landers, rovers and the Mars helicopter. The analysis uses the same format as the other collections in this repository.

## Start here

| Read | What it covers |
|---|---|
| [REPORT.md](REPORT.md) | Definitions; the sensors (encoders, IMU grades, 2D laser, 3D LiDAR, cameras, GNSS, star trackers, navaids); platform-by-platform sensor suites and estimators; why the problem is hard; model-based vs learning vs map-based methods; map-based localization vs SLAM; fusion architectures; which method for which task; year-by-year breakthroughs from the Kalman filter (1960) to MASt3R-SLAM (2025); quick-start textbooks |
| [cookbook/COOKBOOK.md](cookbook/COOKBOOK.md) | 21 math recipes (S1–S21): Lie groups, IMU and encoder error growth, strapdown INS and the Schuler period, GNSS and DOP, error-state GNSS/INS filter, camera models and stereo, epipolar geometry and RANSAC, bundle adjustment, scale and observability, IMU preintegration, MSCKF, point-to-plane ICP / NDT / LOAM, 2D laser SLAM, factor graphs, loop closure and robust kernels, map-based localization and integrity, degeneracy, calibration and time sync, spacecraft attitude and terrain-relative navigation, learned SLAM, evaluation metrics |
| [CATALOG.md](CATALOG.md) | 49 papers, reports and texts in 9 categories, each with a DOI, arXiv or NASA link; 9 open-access PDFs saved locally |

The rendered pages in [`html/`](html/) show equations and diagrams; download them and open in a browser. Every worked example is reproduced by [`cookbook/examples.py`](cookbook/examples.py) (NumPy only; `python3 cookbook/examples.py s05`).

## Layout

```
slam-localization/
├── README.md
├── REPORT.md                 analysis report (source)
├── CATALOG.md / catalog.csv  generated catalog
├── catalog.json              source of truth for the catalog
├── cookbook/
│   ├── COOKBOOK.md           math recipes S1–S21 (source)
│   └── examples.py           runnable worked examples
├── html/                     rendered report.html and cookbook.html
├── papers/<category>/        open-access PDFs
└── tools/                    build_catalog.py, render_md.py
```

To rebuild: `python3 tools/build_catalog.py --download`, then `python3 tools/render_md.py REPORT.md html/report.html "SLAM and Localization"`. Do the same for `cookbook/COOKBOOK.md`.

## Notes on sources

- **PDF links.** In each catalog, **PDF** is a copy stored in this repository and **PDF ↗** opens the paper's PDF online. Every arXiv entry links its arXiv PDF; journal, NASA and conference papers link an open PDF where one was found and checked. To add one, set `pdf_url` in `catalog.json`; `python3 tools/build_catalog.py --check` verifies non-arXiv PDF links.
- DOIs were resolved through Crossref and arXiv IDs checked against the arXiv API on 26 Oct 2026. NASA facts come from NTRS reports and NASA SP-504.
- The Space Shuttle's GPS transition (four missions in 2006–07, then an all-GPS flight) comes from a NASA-sourced excerpt; check the original before formal citation.
- Accuracy figures are the authors' own: Levinson & Thrun's 10 cm range, Wan et al.'s 5–10 cm, ORB-SLAM3's 2–5×. Fit ratings and the task map are a synthesis, not measurements.
