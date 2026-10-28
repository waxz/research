# Seeing objects: detection and tracking from ResNet to YOLO to VLMs

*An analysis of perception algorithms that detect and track objects in images and point clouds, written in the same format as the other collections in this repository. It runs from hand-crafted detectors through ResNet backbones, the R-CNN and YOLO families, DETR transformers and LiDAR/BEV 3D detection to multi-object tracking and open-vocabulary detectors and vision-language models. Equations are derived in the companion [cookbook](cookbook/COOKBOOK.md) (recipes P1–P20), and every source is in the [catalog](CATALOG.md). Numbers come from the papers' own abstracts, checked on 28 Oct 2026.*

## Summary

- **Three shifts define the field:**
  1. **Learned features** replaced hand-crafted ones. AlexNet (2012) and ResNet (2015) made deep CNN backbones the foundation; ResNet's 152-layer residual nets won ILSVRC and COCO 2015.
  2. **Detection became one network.** It went from proposals-plus-classifier (R-CNN, Faster R-CNN) to single-shot regression (YOLO, 45 FPS in 2016) to set prediction without NMS or anchors (DETR 2020, RT-DETR 53.1 AP at 108 FPS in 2024).
  3. **Language replaced fixed label sets.** CLIP (2021) learned from 400M image-text pairs and matched ResNet-50 on ImageNet zero-shot. Grounding DINO detects whatever a text prompt names (52.5 AP zero-shot on COCO), YOLO-World does it in real time (35.4 AP on LVIS at 52 FPS), and VLMs (Florence-2, Qwen-VL, PaliGemma) output boxes as tokens.
- **Point clouds followed a parallel path.** PointNet (2017) handled raw unordered points. Voxel, pillar and centre-based detectors (VoxelNet, PointPillars at 62 Hz, CenterPoint at 65.5 NDS) made lidar detection fast and accurate. Camera-only BEV methods closed much of the gap (BEVFormer, 56.9 NDS, on par with lidar baselines), and BEV fusion combines both (BEVFusion).
- **Tracking stayed surprisingly classical.** The dominant recipe is still SORT's Kalman filter plus Hungarian assignment (2016, 260 Hz), refined by appearance features (DeepSORT), by keeping low-score boxes (ByteTrack: 80.3 MOTA, 77.3 IDF1, 63.1 HOTA on MOT17 at 30 FPS), and by occlusion handling (OC-SORT, BoT-SORT). End-to-end transformer trackers (MOTR) and promptable video segmentation (SAM 2) are the learned alternatives.
- **In robots and cars, the fast closed-set detector is still the workhorse.** That means a YOLO or RT-DETR in 2D and a CenterPoint- or BEV-style detector in 3D, feeding a classical tracker. Open-vocabulary detectors and VLMs add understanding of new objects and instructions at lower rates, and certified safety sensors remain separate (see the mobile-robot collection).

---

## 1. Tasks, outputs and sensors

| Task | Output | Typical metric |
|---|---|---|
| Image classification | Label | Top-1 / top-5 accuracy |
| 2D object detection | Boxes $(x_1,y_1,x_2,y_2)$ + class + score | AP@0.5 (VOC), AP@[0.5:0.95] (COCO) |
| Instance segmentation | Per-object masks | Mask AP |
| 3D object detection | Oriented 3D boxes $(x,y,z,l,w,h,\theta)$, often velocity | 3D/BEV AP (KITTI), mAP + NDS (nuScenes) |
| Multi-object tracking | Boxes with persistent identities over time | MOTA, IDF1, HOTA; AMOTA in 3D |
| Open-vocabulary / grounded detection | Boxes for classes or phrases given as text | Zero-shot AP (COCO, LVIS), RefCOCO accuracy |

| Sensor | Gives | Lacks | Typical detector input |
|---|---|---|---|
| Camera | Dense colour and texture, cheap, long range for recognition | Depth (monocular), robustness in dark, glare and weather | Image tensor; multi-camera to BEV |
| LiDAR | Accurate 3D geometry, lighting-independent | Colour and texture; sparse at range; rain and fog | Points, voxels, pillars, range images |
| Radar | Range and velocity in all weather | Resolution | Point lists; fused in BEV |
| Fusion | Complementary strengths | Calibration and timing burden | BEV feature fusion (BEVFusion) |

## 2. Eras: what each solved and what pushed the next

| Era | Representative methods | What it solved | Limitation that drove the next |
|---|---|---|---|
| **Hand-crafted features** (2001–2012) | Viola–Jones cascade (2001), HOG + SVM (2005), deformable part models (2010) | Real-time faces; pedestrians; articulated objects | Features hand-designed per class; accuracy plateaued |
| **Deep backbones** (2012–2016) | AlexNet (2012), VGG (2014), ResNet (2015) | Learned features; depth made trainable by residual connections (P2) | Classification only; detection still needed a pipeline |
| **Two-stage detectors** (2014–2017) | R-CNN → Fast → Faster R-CNN (RPN), FPN, Mask R-CNN | High accuracy; learned proposals; small objects; masks | Speed (Faster R-CNN about 5 fps with VGG-16) |
| **One-stage / YOLO** (2016–) | YOLO (45 FPS), SSD, YOLOv2/v3, RetinaNet (focal loss), YOLOv4–v10, YOLOX, Ultralytics YOLOv5/v8/YOLO11 | Real-time detection; focal loss fixed the accuracy gap; edge deployment | Hand-designed anchors, NMS and label assignment |
| **Anchor-free** (2019) | CenterNet, FCOS | Removed anchor tuning; objects as points | Still needs NMS |
| **Transformer detectors** (2020–) | DETR, Deformable DETR, DINO, RT-DETR | End-to-end set prediction, no NMS or anchors; real-time by 2024 | Fixed label set |
| **Open-vocabulary and foundation** (2021–) | CLIP, GLIP, OWL-ViT, Grounding DINO, YOLO-World, SAM / SAM 2, DINOv2 | Any category named in text; promptable masks; general features | Compute; calibration of scores; long-tail precision |
| **VLMs that localize** (2023–) | Kosmos-2, Qwen-VL, Florence-2, PaliGemma, LLaVA-style models | Reasoning, instructions, referring expressions, boxes as tokens | Latency, hallucination, weaker box precision than specialist detectors |
| **3D point clouds** (2017–) | PointNet/++, VoxelNet, SECOND, PointPillars, PointRCNN, PV-RCNN, CenterPoint | Learning on sparse, unordered 3D data at real-time rates | Sparsity at range; no semantics from colour |
| **Camera BEV and fusion** (2020–) | Lift-Splat-Shoot, DETR3D, BEVFormer, BEVFusion | 3D from cameras; one BEV space for all sensors | Depth uncertainty; calibration; compute |

## 3. Why perception is hard

| Difficulty | Example | Cookbook |
|---|---|---|
| **Scale variation and small objects** | A pallet at 2 m vs 30 m; drones at altitude | P1, FPN in P8 |
| **Extreme class imbalance** | ~200,000 anchors per image, a handful of objects | P6, P8 |
| **Duplicates and localization** | Many overlapping boxes per object; box quality vs class score | P3–P5 |
| **Occlusion and identity** | Objects disappear and reappear; ID switches | P16–P18 |
| **Depth from images** | Monocular scale ambiguity; depth error grows with range (S6) | P15 |
| **Sparsity in LiDAR** | Most of a pillar grid is empty; distant objects get a few points | P13 |
| **Open world and long tail** | Unseen objects, rare classes, new SKUs | P11 |
| **Domain shift** | Night, rain, new warehouse, new camera | P11 (foundation features help) |
| **Real-time budget** | 33 ms at 30 FPS for everything, including NMS and tracking | P20 |
| **Calibration and timing** | Wrong extrinsics misplace fused objects (S18) | P14 |
| **Evaluation subtleties** | AP definitions differ (VOC vs COCO); MOTA under-weights identity | P7, P18, P19 |

## 4. 2D detector families compared

| Family | Examples | How it predicts | Post-processing | Strengths | Weaknesses | Deployment today |
|---|---|---|---|---|---|---|
| Two-stage | Faster/Mask R-CNN + FPN | Proposals (RPN), then RoI classification and regression | NMS | Accurate, strong on small objects; masks | Slower; complex | Offline labelling, high-accuracy pipelines |
| One-stage, anchor-based | SSD, RetinaNet, YOLOv2–v7 | Dense predictions per anchor and cell | NMS | Fast, simple | Anchor tuning; NMS latency | Edge and real-time |
| One-stage, anchor-free | CenterNet, FCOS, YOLOX, YOLOv8/YOLO11 | Per-pixel centres or distances | NMS (YOLOv10 removes it) | Fewer hyperparameters | Still dense | The default real-time choice |
| Transformer (DETR family) | DETR, Deformable DETR, DINO, RT-DETR | Learned object queries; Hungarian matching in training | None | End-to-end, global reasoning | Training cost (improved by Deformable DETR and DINO) | RT-DETR competitive in real time |
| Open-vocabulary | GLIP, OWL-ViT, Grounding DINO, YOLO-World | Region–text similarity | NMS or none | New classes from prompts | Slower (except YOLO-World); lower precision on rare classes | Labelling, robotics with language |
| VLM | Florence-2, Qwen-VL, PaliGemma, Kosmos-2 | Generate box tokens from an instruction | None | Reasoning and referring expressions | Latency; box precision; hallucination | High-level semantics, not control loops |

## 5. 3D detection compared

| Representation | Examples | Idea | Speed / accuracy | Notes |
|---|---|---|---|---|
| Raw points | PointNet/++, PointRCNN | Shared MLP + symmetric pooling (P12) | Accurate, slower on large scenes | Good for small clouds and parts |
| Voxels | VoxelNet, SECOND | 3D grid + (sparse) 3D convolutions | Accurate; sparse convolution made it fast | Memory scales with grid |
| Pillars | PointPillars | Vertical columns → 2D pseudo-image → 2D CNN | 62 Hz (105 Hz fast version) | Embedded-friendly |
| Point-voxel | PV-RCNN | Voxel backbone + point refinement | High accuracy | Heavier |
| Centre-based | CenterPoint | BEV heatmap of object centres, then refinement | 65.5 NDS; tracking by closest-point matching | Rotation-friendly; also gives velocity |
| Camera → BEV | LSS, DETR3D, BEVFormer | Lift image features with depth distributions or 3D queries | BEVFormer 56.9 NDS (camera only) | Cheaper sensors; depth uncertain |
| Fusion in BEV | BEVFusion | Camera and lidar features in one BEV grid | +1.3 mAP/NDS over prior SOTA, BEV pooling 40× faster | Needs tight calibration |

## 6. Tracking paradigms

| Paradigm | Examples | How identities are kept | Strengths | Weaknesses |
|---|---|---|---|---|
| Tracking-by-detection, motion only | SORT (2016) | Kalman filter on boxes + Hungarian on IoU | 260 Hz; simple | ID switches after occlusion |
| + appearance | DeepSORT, BoT-SORT | Re-ID embeddings + motion (+ camera-motion compensation) | Survives occlusion | Re-ID network cost |
| + low-score association | ByteTrack | Second matching pass on low-score boxes | Recovers occluded objects; 80.3 MOTA on MOT17 | Depends on detector calibration |
| Observation-centric | OC-SORT | Re-anchors the Kalman state on new observations after gaps | Robust to non-linear motion and occlusion | Still motion-model based |
| Joint detection and tracking | Tracktor, FairMOT | Detector regresses previous boxes or emits re-ID features | One network | Coupled training |
| End-to-end | MOTR | Track queries persist across frames | No hand-made association | Data-hungry; slower |
| Segmentation tracking | SAM 2 | Streaming memory over masks | Any prompted object; 3× fewer interactions | Interactive or prompted; compute |
| 3D | AB3DMOT, CenterPoint tracking | 3D Kalman + Hungarian; velocity-based greedy matching | Metric 3D; simple | Inherits detector errors |

## 7. Paradigms in the collection's lens

| Lens | Classical / hand-engineered | Supervised deep (closed set) | Foundation / open-vocabulary / VLM |
|---|---|---|---|
| Knowledge source | Designed features and rules | Labelled boxes for fixed classes | Web-scale image-text pairs; data engines (SAM's 1B masks); self-supervision (DINOv2) |
| New categories | Redesign | Relabel and retrain | Type a prompt |
| Precision on known classes | Low | **Highest** | Lower on rare classes; improving |
| Latency | Low | Low (real-time YOLO / RT-DETR) | Medium (YOLO-World real-time) to high (VLMs) |
| Calibration and guarantees | Analyzable | Empirical | Empirical; harder to bound |
| Best role | Pre-filters, geometry checks | Real-time loops (driving, AMRs) | Labelling, rare objects, instructions, "what is this?" |

**Reference vs self-exploration, again.** Supervised detectors learn from a human-written reference: boxes for a fixed list. Foundation models learn from much broader, weaker signals (captions, self-supervision, model-in-the-loop data engines). As in the other collections, the strongest systems combine the two:
- foundation features fine-tuned into fast closed-set detectors;
- open-vocabulary models used to auto-label data for real-time detectors;
- classical tracking used for identity and motion.

## 8. Which method for which task

Fit: ●●● strong, ●● viable, ● niche, ○ rarely used. Columns are real-time 2D (YOLO / RT-DETR), 3D LiDAR / BEV, open-vocabulary / VLM, and classical tracking (SORT family).

| Task | Main difficulty | Best-suited approach | Fit 2D · 3D · VLM · Tracking | Notes |
|---|---|---|---|---|
| Warehouse AMR / forklift: people, carts, pallets | Real-time, embedded, safety | Edge YOLO or RT-DETR (INT8) + 2D lidar clustering; certified safety scanner kept separate | ●●● ●● ● ●● | Learned perception assists; doesn't replace safety sensors |
| Pallet-pocket and dock detection | ±1 cm geometry | Lidar/depth geometric fitting + a learned detector for candidates | ●● ●● ○ ○ | See M18 |
| Autonomous driving | 360° 3D, long range, weather | Lidar CenterPoint-style + camera BEV fused (BEVFusion); 3D tracking | ●● ●●● ● ●●● | Trackers feed prediction and planning |
| Drones and aerial imagery | Tiny objects, edge compute | YOLO with high-resolution tiling; FPN | ●●● ○ ● ●● | Small-object augmentation |
| Robot grasping of novel objects | Unknown objects, masks | Grounding DINO / OWL-ViT + SAM masks, or a fine-tuned instance segmenter | ●● ● ●●● ● | Language-specified targets |
| Retail, sports, video analytics | Identity over long occlusions | ByteTrack or BoT-SORT + re-ID | ●●● ○ ● ●●● | HOTA and IDF1 matter more than MOTA |
| Labelling and data engines | Cost of annotation | Open-vocabulary detectors + SAM to propose; humans verify | ●● ● ●●● ○ | Bootstraps closed-set models |
| Instruction-following robots (VLA) | Understanding "the red mug left of the laptop" | VLM grounding (Qwen-VL, PaliGemma, Florence-2) at low rate + fast tracker | ● ● ●●● ●● | VLM for what; detector and tracker for where, now |
| Agriculture and inspection | Domain shift, fine classes | Fine-tuned detector on foundation backbone (DINOv2) | ●●● ● ●● ●● | Few-shot adaptation |

**Decision rule.**
1. Hard real-time and a known class list → a closed-set detector (YOLO or RT-DETR in 2D; CenterPoint/BEV in 3D) + SORT-family tracking.
2. New or rare objects, or language-specified targets → an open-vocabulary detector (YOLO-World if real-time, Grounding DINO otherwise) + SAM for masks.
3. Reasoning, instructions or referring expressions → a VLM at low rate, handing boxes to the fast tracker.
4. Safety functions → certified sensors and logic, with learned perception advisory only.

## 9. Breakthroughs, year by year

| Year | Breakthrough | Problem it solved | Evidence |
|---|---|---|---|
| 2001 | Viola–Jones cascade | Real-time face detection | Haar features + boosted cascade |
| 2005 | HOG | Robust pedestrian features | Dalal & Triggs |
| 2009–10 | ImageNet; PASCAL VOC; deformable part models | Benchmarks at scale; best pre-deep detector | Deng et al.; Everingham et al.; Felzenszwalb et al. |
| 2012 | AlexNet | Learned features beat hand-crafted | ILSVRC 2012 win |
| 2014 | R-CNN; VGG; COCO | CNN features for detection; deeper nets; harder benchmark | Girshick et al.; Simonyan & Zisserman; Lin et al. |
| 2015 | Faster R-CNN; ResNet | Learned proposals; very deep training | 5 fps with VGG-16; 152 layers, 3.57% error, ILSVRC and COCO 2015 wins |
| 2016 | YOLO; SSD; SORT | Real-time single-shot detection; real-time tracking | 45 FPS (Fast YOLO 155 FPS); SORT at 260 Hz |
| 2017 | FPN; Mask R-CNN; focal loss; PointNet; DeepSORT | Multi-scale; masks; one-stage accuracy; raw point clouds; appearance tracking | RetinaNet surpasses two-stage accuracy |
| 2018 | YOLOv3; VoxelNet; SECOND | Multi-scale YOLO; learned 3D voxels; sparse convolution | Redmon & Farhadi; Zhou & Tuzel; Yan et al. |
| 2019 | PointPillars; CenterNet / FCOS; nuScenes, Waymo Open | Fast lidar detection; anchor-free; large driving benchmarks | 62 Hz; 6 cameras + lidar + radar |
| 2020 | DETR; Lift-Splat-Shoot; YOLOv4; AB3DMOT; HOTA | End-to-end detection; camera-to-BEV; 3D tracking baseline; balanced tracking metric | Carion et al.; Philion & Fidler |
| 2021 | CLIP; CenterPoint; Deformable DETR; Swin; ViT | Language supervision and zero-shot; centre-based 3D; fast DETR; transformer backbones | CLIP matches ResNet-50 zero-shot; CenterPoint 65.5 NDS |
| 2022 | ByteTrack; GLIP; OWL-ViT; BEVFormer; BEVFusion; DINO; YOLOv7 | Low-score association; grounded and open-vocabulary detection; camera BEV at lidar level; fusion | 80.3 MOTA on MOT17; 56.9 NDS camera-only |
| 2023 | SAM; Grounding DINO; DINOv2; LLaVA, Kosmos-2, Qwen-VL; OC-SORT | Promptable segmentation; text-prompted detection; general features; VLMs that localize | 1B masks; 52.5 AP zero-shot on COCO |
| 2024 | RT-DETR; YOLO-World; YOLOv9 / v10; SAM 2; Florence-2; PaliGemma | Real-time DETR; real-time open-vocabulary; NMS-free YOLO; video segmentation; unified vision models | 53.1 AP at 108 FPS; 35.4 AP on LVIS at 52 FPS; SAM 2 6× faster than SAM |
| 2025–26 | YOLO11 and later Ultralytics releases; VLM-based grounding in robot foundation models | Faster edge deployment; language-conditioned perception for robots | See the robot-learning collection (π0, VLAs) |

## 10. Deployment practice

- **Latency budget** (P20). At 30 FPS the whole pipeline has 33 ms. NMS, pre-processing and tracking count. NMS-free designs (DETR, RT-DETR, YOLOv10) remove one variable-latency step.
- **Precision and size.** INT8 quantization cuts memory 4× from fp32. Export through TensorRT, ONNX or OpenVINO. Check accuracy after quantization on your own data.
- **Data beats architecture** for a fixed domain. Collect hard cases and use open-vocabulary models and SAM to pre-label, with human verification.
- **Calibrate scores.** Trackers like ByteTrack rely on detection scores meaning something; open-vocabulary scores vary by prompt.
- **Fuse in BEV, track in metric space.** In 3D, track in vehicle or world coordinates with velocity, not in image space.
- **Keep VLMs out of the fast safety loop.** Use them for semantics and exceptions; keep a fast detector and tracker, and certified safety sensors, in the loop.

## 11. Quick start: textbooks, courses and tooling

| Resource | Access | Start with | Covers |
|---|---|---|---|
| [CS231n: Deep Learning for Computer Vision](https://cs231n.github.io/) (Stanford) | Free notes | CNNs, detection and segmentation lectures | P1–P8 |
| [Dive into Deep Learning: computer vision chapters](https://d2l.ai/chapter_computer-vision/index.html) | Free, runnable code | Anchor boxes, multiscale detection, SSD, R-CNN | P3–P8 |
| [Understanding Deep Learning](https://udlbook.github.io/udlbook/), Prince (2023) | Free PDF | Convolutional networks, residual networks, transformers | P1, P2, P9 |
| [Computer Vision: Algorithms and Applications](https://szeliski.org/Book/), Szeliski (2nd ed.) | Free PDF | Recognition chapter; camera geometry | P14 |
| [Object Detection in 20 Years](https://arxiv.org/abs/1905.05055), Zou et al. | Free survey | The whole history | Sections 2, 4 |
| [Ultralytics YOLO docs](https://docs.ultralytics.com/) | Free, hands-on | Train, validate, export and track modes | YOLO practice, P5, P20 |
| [Detectron2](https://detectron2.readthedocs.io/) and [MMDetection](https://mmdetection.readthedocs.io/) | Open source | Model zoos for R-CNN, RetinaNet, DETR families | Research baselines |
| [OpenPCDet](https://github.com/open-mmlab/OpenPCDet) | Open source | PointPillars, SECOND, PV-RCNN, CenterPoint configs | P12–P13 |
| [nuScenes](https://www.nuscenes.org/) and [COCO](https://www.cocodataset.org/) | Datasets + devkits | Detection and tracking evaluation code | P7, P19 |
| Surveys in this collection | Local PDFs | [Deep 3D point clouds](papers/00-surveys/guo2021pointcloud.pdf), [3D driving detection](papers/00-surveys/mao2023driving3d.pdf), [open-vocabulary](papers/00-surveys/zhu2023ovd.pdf), [VLMs](papers/00-surveys/zhang2024vlmsurvey.pdf), [MOT](papers/00-surveys/ciaparrone2020mot.pdf) | Each section |

The deep-learning, attention and generative-model maths is in the [Control-to-Learning cookbook](../robot-learning-control/cookbook/COOKBOOK.md) (R18–R22). Camera geometry and Kalman filtering are in the [SLAM cookbook](../slam-localization/cookbook/COOKBOOK.md) (S6–S9) and the [control cookbook](../control-estimation-theory/cookbook/COOKBOOK.md) (E3).

## 12. Sources and caveats

- All 84 entries in [CATALOG.md](CATALOG.md) have arXiv IDs (checked against the arXiv API) or DOIs (checked through Crossref). 20 open-access PDFs are saved locally.
- **Headline numbers are the authors' own,** on their stated hardware: YOLO 45 FPS; RT-DETR 108 FPS on a T4; YOLO-World 52 FPS on a V100; ByteTrack 30 FPS on a V100. They aren't directly comparable across GPUs.
- **YOLOv5, YOLOv8 and YOLO11 have no peer-reviewed papers.** They are cited by their documentation.
- The fit ratings and task map are a synthesis, not measurements.
