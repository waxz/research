# Perception: object detection and tracking from ResNet to YOLO to VLMs

How robots and vehicles detect and track objects in camera images and LiDAR point clouds. The analysis runs from hand-crafted detectors and ResNet backbones through the R-CNN and YOLO families and DETR transformers, then 3D point-cloud and bird's-eye-view (BEV) detection and multi-object tracking, to open-vocabulary detectors and vision-language models. The format matches the other collections in this repository.

## Start here

| Read | What it covers |
|---|---|
| [REPORT.md](REPORT.md) | Tasks, metrics and sensors; eras and what pushed each one; why perception is hard; 2D detector families, 3D representations and tracking paradigms compared; hand-engineered vs supervised vs foundation models; which method for which task; breakthroughs from 2001 to 2026; deployment practice; quick-start courses and tooling |
| [cookbook/COOKBOOK.md](cookbook/COOKBOOK.md) | 20 math recipes (P1–P20): convolution arithmetic, residual learning, IoU/GIoU, box encoding, NMS, focal loss, AP/mAP, dense vs sparse prediction, attention cost, Hungarian matching (DETR), CLIP and open-vocabulary scoring, PointNet, voxels and pillars, lidar–camera projection, lifting images to BEV, Kalman box tracking, ByteTrack association, MOTA/IDF1/HOTA, nuScenes NDS, latency budgets |
| [CATALOG.md](CATALOG.md) | 84 papers, datasets and tools in 11 categories, each with an arXiv ID or DOI; 20 open-access PDFs saved locally |

The rendered pages in [`html/`](html/) show equations and diagrams; download them and open in a browser. Every worked example is reproduced by [`cookbook/examples.py`](cookbook/examples.py) (NumPy only; `python3 cookbook/examples.py p17`).

## Layout

```
perception-detection-tracking/
├── README.md
├── REPORT.md                 analysis report (source)
├── CATALOG.md / catalog.csv  generated catalog
├── catalog.json              source of truth for the catalog
├── cookbook/
│   ├── COOKBOOK.md           math recipes P1–P20 (source)
│   └── examples.py           runnable worked examples
├── html/                     rendered report.html and cookbook.html
├── papers/<category>/        open-access PDFs
└── tools/                    build_catalog.py, render_md.py
```

To rebuild: `python3 tools/build_catalog.py --download`, then `python3 tools/render_md.py REPORT.md html/report.html "Detection and Tracking"`. Do the same for `cookbook/COOKBOOK.md`.

## Notes on sources

- **PDF links.** In each catalog, **PDF** is a copy stored in this repository and **PDF ↗** opens the paper's PDF online. Every arXiv entry links its arXiv PDF; journal, NASA and conference papers link an open PDF where one was found and checked. To add one, set `pdf_url` in `catalog.json`; `python3 tools/build_catalog.py --check` verifies non-arXiv PDF links.
- All arXiv IDs were checked against the arXiv API, and all DOIs through Crossref, on 28 Oct 2026. Quoted results come from the papers' abstracts, on the authors' hardware.
- YOLOv5, YOLOv8 and YOLO11 (Ultralytics) have no peer-reviewed papers and are cited by their documentation.
- The 51 MB YOLO review is linked rather than stored, to stay under GitHub's large-file warning.
- Fit ratings and the task map are a synthesis, not measurements.
