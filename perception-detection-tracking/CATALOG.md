# Paper catalog

84 entries in 11 categories. **73** have a PDF available online (PDF ↗) and **20** also have a local copy in this repository (PDF).
Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.

| Category | Entries | PDF online | Local PDF |
|---|---:|---:|---:|
| [Surveys and reviews](#00-surveys) | 8 | 8 | 7 |
| [Classical detectors and the datasets that drove progress](#01-classical-datasets) | 6 | 1 | 0 |
| [Backbones and representation learning](#02-backbones) | 6 | 5 | 1 |
| [Two-stage detectors](#03-two-stage) | 5 | 5 | 1 |
| [One-stage detectors and the YOLO family](#04-one-stage-yolo) | 14 | 13 | 2 |
| [Transformer detectors](#05-transformer-detectors) | 4 | 4 | 1 |
| [Open-vocabulary detection, segmentation and VLMs](#06-open-vocabulary-vlm) | 12 | 12 | 4 |
| [Point-cloud 3D detection](#07-point-cloud-3d) | 8 | 7 | 3 |
| [Camera 3D, BEV and sensor fusion](#08-camera-bev-fusion) | 4 | 4 | 0 |
| [Multi-object tracking](#09-tracking) | 10 | 9 | 1 |
| [Benchmarks and metrics](#10-benchmarks-metrics) | 7 | 5 | 0 |

<a id="00-surveys"></a>
## Surveys and reviews

Overviews of 2D detection, YOLO, 3D point-cloud and driving detection, open-vocabulary detection, VLMs and multi-object tracking.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2020 | **Deep Learning in Video Multi-Object Tracking: A Survey**<br>G. Ciaparrone et al. | Neurocomputing | [PDF](papers/00-surveys/ciaparrone2020mot.pdf) · [PDF ↗](https://arxiv.org/pdf/1907.12740) · [arXiv](https://arxiv.org/abs/1907.12740) | Detection, feature extraction, affinity and association stages. |
| 2020 | **Deep Learning for Generic Object Detection: A Survey**<br>L. Liu et al. | IJCV | [PDF](papers/00-surveys/liu2020generic.pdf) · [PDF ↗](https://arxiv.org/pdf/1809.02165) · [arXiv](https://arxiv.org/abs/1809.02165) | Taxonomy of deep 2D detectors. |
| 2021 | **Deep Learning for 3D Point Clouds: A Survey**<br>Y. Guo et al. | IEEE TPAMI | [PDF](papers/00-surveys/guo2021pointcloud.pdf) · [PDF ↗](https://arxiv.org/pdf/1912.12033) · [arXiv](https://arxiv.org/abs/1912.12033) | Point-cloud classification, detection, tracking, segmentation. |
| 2023 | **3D Object Detection for Autonomous Driving: A Comprehensive Survey**<br>J. Mao, S. Shi, X. Wang, H. Li | IJCV | [PDF](papers/00-surveys/mao2023driving3d.pdf) · [PDF ↗](https://arxiv.org/pdf/2206.09474) · [arXiv](https://arxiv.org/abs/2206.09474) | LiDAR, camera and fusion 3D detection. |
| 2023 | **A Comprehensive Review of YOLO Architectures in Computer Vision: From YOLOv1 to YOLOv8 and YOLO-NAS**<br>J. Terven, D.-M. Cordova-Esparza, J.-A. Romero-Gonzalez | Machine Learning and Knowledge Extraction | [PDF ↗](https://arxiv.org/pdf/2304.00501) · [arXiv](https://arxiv.org/abs/2304.00501) | Generation-by-generation YOLO changes. (51 MB PDF; linked rather than stored) |
| 2023 | **A Survey on Open-Vocabulary Detection and Segmentation: Past, Present, and Future**<br>C. Zhu, L. Chen | arXiv / TPAMI | [PDF](papers/00-surveys/zhu2023ovd.pdf) · [PDF ↗](https://arxiv.org/pdf/2307.09220) · [arXiv](https://arxiv.org/abs/2307.09220) | Open-vocabulary detection and segmentation taxonomy. |
| 2023 | **Object Detection in 20 Years: A Survey**<br>Z. Zou, K. Chen, Z. Shi, Y. Guo, J. Ye | Proceedings of the IEEE | [PDF](papers/00-surveys/zou2023twenty.pdf) · [PDF ↗](https://arxiv.org/pdf/1905.05055) · [arXiv](https://arxiv.org/abs/1905.05055) | From Viola-Jones to deep detectors; milestones and datasets. |
| 2024 | **Vision-Language Models for Vision Tasks: A Survey**<br>J. Zhang, J. Huang, S. Jin, S. Lu | IEEE TPAMI | [PDF](papers/00-surveys/zhang2024vlmsurvey.pdf) · [PDF ↗](https://arxiv.org/pdf/2304.00685) · [arXiv](https://arxiv.org/abs/2304.00685) | VLM pre-training, transfer and distillation for vision tasks. |

<a id="01-classical-datasets"></a>
## Classical detectors and the datasets that drove progress

Hand-crafted features before deep learning; ImageNet, PASCAL VOC, COCO.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2001 | **Rapid Object Detection using a Boosted Cascade of Simple Features**<br>P. Viola, M. Jones | CVPR | [link](https://doi.org/10.1109/CVPR.2001.990517) | Real-time face detection with Haar features and a cascade. |
| 2005 | **Histograms of Oriented Gradients for Human Detection**<br>N. Dalal, B. Triggs | CVPR | [link](https://doi.org/10.1109/CVPR.2005.177) | HOG + linear SVM pedestrian detection. |
| 2009 | **ImageNet: A Large-Scale Hierarchical Image Database**<br>J. Deng et al. | CVPR | [link](https://doi.org/10.1109/CVPR.2009.5206848) | The dataset behind the deep-learning turn. |
| 2010 | **The Pascal Visual Object Classes (VOC) Challenge**<br>M. Everingham et al. | IJCV | [link](https://doi.org/10.1007/s11263-009-0275-4) | Detection benchmark and AP@0.5 metric. |
| 2010 | **Object Detection with Discriminatively Trained Part-Based Models**<br>P. F. Felzenszwalb, R. B. Girshick, D. McAllester, D. Ramanan | IEEE TPAMI | [link](https://doi.org/10.1109/TPAMI.2009.167) | Deformable part models: the pre-deep-learning peak. |
| 2014 | **Microsoft COCO: Common Objects in Context**<br>T.-Y. Lin et al. | ECCV | [PDF ↗](https://arxiv.org/pdf/1405.0312) · [arXiv](https://arxiv.org/abs/1405.0312) | 80 classes; AP averaged over IoU 0.5:0.95. |

<a id="02-backbones"></a>
## Backbones and representation learning

AlexNet to ResNet to Vision Transformers and self-supervised features.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2012 | **ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)**<br>A. Krizhevsky, I. Sutskever, G. E. Hinton | NeurIPS (CACM 2017 version linked) | [link](https://doi.org/10.1145/3065386) | GPU-trained CNN wins ILSVRC 2012. |
| 2015 | **Very Deep Convolutional Networks for Large-Scale Image Recognition (VGG)**<br>K. Simonyan, A. Zisserman | ICLR | [PDF ↗](https://arxiv.org/pdf/1409.1556) · [arXiv](https://arxiv.org/abs/1409.1556) | Stacks of 3x3 convolutions. |
| 2016 | **Deep Residual Learning for Image Recognition (ResNet)**<br>K. He, X. Zhang, S. Ren, J. Sun | CVPR | [PDF](papers/02-backbones/he2016resnet.pdf) · [PDF ↗](https://arxiv.org/pdf/1512.03385) · [arXiv](https://arxiv.org/abs/1512.03385) | 152-layer residual nets; 3.57% ImageNet error; won ILSVRC and COCO 2015. |
| 2021 | **An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ViT)**<br>A. Dosovitskiy et al. | ICLR | [PDF ↗](https://arxiv.org/pdf/2010.11929) · [arXiv](https://arxiv.org/abs/2010.11929) | Vision Transformer. |
| 2021 | **Swin Transformer: Hierarchical Vision Transformer using Shifted Windows**<br>Z. Liu et al. | ICCV | [PDF ↗](https://arxiv.org/pdf/2103.14030) · [arXiv](https://arxiv.org/abs/2103.14030) | Hierarchical windowed attention, a detection backbone. |
| 2024 | **DINOv2: Learning Robust Visual Features without Supervision**<br>M. Oquab et al. | TMLR | [PDF ↗](https://arxiv.org/pdf/2304.07193) · [arXiv](https://arxiv.org/abs/2304.07193) | Self-supervised general-purpose visual features. |

<a id="03-two-stage"></a>
## Two-stage detectors

The R-CNN family and feature pyramids.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2014 | **Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation (R-CNN)**<br>R. Girshick, J. Donahue, T. Darrell, J. Malik | CVPR | [PDF ↗](https://arxiv.org/pdf/1311.2524) · [arXiv](https://arxiv.org/abs/1311.2524) | CNN features on region proposals. |
| 2015 | **Fast R-CNN**<br>R. Girshick | ICCV | [PDF ↗](https://arxiv.org/pdf/1504.08083) · [arXiv](https://arxiv.org/abs/1504.08083) | Shared computation with RoI pooling. |
| 2015 | **Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks**<br>S. Ren, K. He, R. Girshick, J. Sun | NeurIPS | [PDF](papers/03-two-stage/ren2015faster.pdf) · [PDF ↗](https://arxiv.org/pdf/1506.01497) · [arXiv](https://arxiv.org/abs/1506.01497) | Learned proposals (RPN); 5 fps with VGG-16. |
| 2017 | **Mask R-CNN**<br>K. He, G. Gkioxari, P. Dollar, R. Girshick | ICCV | [PDF ↗](https://arxiv.org/pdf/1703.06870) · [arXiv](https://arxiv.org/abs/1703.06870) | Instance segmentation with RoIAlign. |
| 2017 | **Feature Pyramid Networks for Object Detection**<br>T.-Y. Lin et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/1612.03144) · [arXiv](https://arxiv.org/abs/1612.03144) | Multi-scale features for small objects. |

<a id="04-one-stage-yolo"></a>
## One-stage detectors and the YOLO family

YOLO, SSD, RetinaNet, anchor-free detectors, real-time YOLO generations.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2016 | **SSD: Single Shot MultiBox Detector**<br>W. Liu et al. | ECCV | [PDF ↗](https://arxiv.org/pdf/1512.02325) · [arXiv](https://arxiv.org/abs/1512.02325) | Multi-scale default boxes. |
| 2016 | **You Only Look Once: Unified, Real-Time Object Detection (YOLO)**<br>J. Redmon, S. Divvala, R. Girshick, A. Farhadi | CVPR | [PDF](papers/04-one-stage-yolo/redmon2016yolo.pdf) · [PDF ↗](https://arxiv.org/pdf/1506.02640) · [arXiv](https://arxiv.org/abs/1506.02640) | Detection as one regression; 45 FPS (Fast YOLO 155 FPS). |
| 2017 | **Focal Loss for Dense Object Detection (RetinaNet)**<br>T.-Y. Lin, P. Goyal, R. Girshick, K. He, P. Dollar | ICCV | [PDF](papers/04-one-stage-yolo/lin2017focal.pdf) · [PDF ↗](https://arxiv.org/pdf/1708.02002) · [arXiv](https://arxiv.org/abs/1708.02002) | Focal loss fixes foreground-background imbalance. |
| 2017 | **YOLO9000: Better, Faster, Stronger (YOLOv2)**<br>J. Redmon, A. Farhadi | CVPR | [PDF ↗](https://arxiv.org/pdf/1612.08242) · [arXiv](https://arxiv.org/abs/1612.08242) | Anchors, batch norm, multi-scale training. |
| 2018 | **YOLOv3: An Incremental Improvement**<br>J. Redmon, A. Farhadi | arXiv | [PDF ↗](https://arxiv.org/pdf/1804.02767) · [arXiv](https://arxiv.org/abs/1804.02767) | Multi-scale predictions, Darknet-53. |
| 2019 | **FCOS: Fully Convolutional One-Stage Object Detection**<br>Z. Tian, C. Shen, H. Chen, T. He | ICCV | [PDF ↗](https://arxiv.org/pdf/1904.01355) · [arXiv](https://arxiv.org/abs/1904.01355) | Anchor-free per-pixel detection. |
| 2019 | **Objects as Points (CenterNet)**<br>X. Zhou, D. Wang, P. Krahenbuhl | arXiv | [PDF ↗](https://arxiv.org/pdf/1904.07850) · [arXiv](https://arxiv.org/abs/1904.07850) | Anchor-free centre-heatmap detection. |
| 2020 | **YOLOv4: Optimal Speed and Accuracy of Object Detection**<br>A. Bochkovskiy, C.-Y. Wang, H.-Y. M. Liao | arXiv | [PDF ↗](https://arxiv.org/pdf/2004.10934) · [arXiv](https://arxiv.org/abs/2004.10934) | Bag of freebies and specials. |
| 2020 | **EfficientDet: Scalable and Efficient Object Detection**<br>M. Tan, R. Pang, Q. V. Le | CVPR | [PDF ↗](https://arxiv.org/pdf/1911.09070) · [arXiv](https://arxiv.org/abs/1911.09070) | BiFPN and compound scaling. |
| 2021 | **YOLOX: Exceeding YOLO Series in 2021**<br>Z. Ge et al. | arXiv | [PDF ↗](https://arxiv.org/pdf/2107.08430) · [arXiv](https://arxiv.org/abs/2107.08430) | Anchor-free decoupled-head YOLO. |
| 2023 | **YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors**<br>C.-Y. Wang, A. Bochkovskiy, H.-Y. M. Liao | CVPR | [PDF ↗](https://arxiv.org/pdf/2207.02696) · [arXiv](https://arxiv.org/abs/2207.02696) | Real-time architecture and training refinements. |
| 2024 | **YOLOv10: Real-Time End-to-End Object Detection**<br>A. Wang et al. | NeurIPS | [PDF ↗](https://arxiv.org/pdf/2405.14458) · [arXiv](https://arxiv.org/abs/2405.14458) | NMS-free training via consistent dual assignments. |
| 2024 | **YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information**<br>C.-Y. Wang, I.-H. Yeh, H.-Y. M. Liao | ECCV | [PDF ↗](https://arxiv.org/pdf/2402.13616) · [arXiv](https://arxiv.org/abs/2402.13616) | Programmable gradient information. |
| 2025 | **Ultralytics YOLO documentation (YOLOv5, YOLOv8, YOLO11)**<br>Ultralytics | Software documentation | [link](https://docs.ultralytics.com/) | Widely used open YOLO implementations without accompanying papers. |

<a id="05-transformer-detectors"></a>
## Transformer detectors

DETR and its fast, real-time descendants.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2020 | **End-to-End Object Detection with Transformers (DETR)**<br>N. Carion et al. | ECCV | [PDF](papers/05-transformer-detectors/carion2020detr.pdf) · [PDF ↗](https://arxiv.org/pdf/2005.12872) · [arXiv](https://arxiv.org/abs/2005.12872) | Set prediction with bipartite matching; no NMS or anchors. |
| 2021 | **Deformable DETR: Deformable Transformers for End-to-End Object Detection**<br>X. Zhu et al. | ICLR | [PDF ↗](https://arxiv.org/pdf/2010.04159) · [arXiv](https://arxiv.org/abs/2010.04159) | Sparse deformable attention; much faster convergence. |
| 2023 | **DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection**<br>H. Zhang et al. | ICLR | [PDF ↗](https://arxiv.org/pdf/2203.03605) · [arXiv](https://arxiv.org/abs/2203.03605) | Denoising training; DETR reaches SOTA. |
| 2024 | **DETRs Beat YOLOs on Real-time Object Detection (RT-DETR)**<br>Y. Zhao et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/2304.08069) · [arXiv](https://arxiv.org/abs/2304.08069) | 53.1 AP at 108 FPS (R50, T4 GPU). |

<a id="06-open-vocabulary-vlm"></a>
## Open-vocabulary detection, segmentation and VLMs

CLIP, grounded detection, promptable segmentation, vision-language models that localize.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2021 | **Learning Transferable Visual Models From Natural Language Supervision (CLIP)**<br>A. Radford et al. | ICML | [PDF](papers/06-open-vocabulary-vlm/radford2021clip.pdf) · [PDF ↗](https://arxiv.org/pdf/2103.00020) · [arXiv](https://arxiv.org/abs/2103.00020) | 400M image-text pairs; zero-shot matches ResNet-50 on ImageNet. |
| 2022 | **Grounded Language-Image Pre-training (GLIP)**<br>L. H. Li et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/2112.03857) · [arXiv](https://arxiv.org/abs/2112.03857) | Detection as phrase grounding. |
| 2022 | **Simple Open-Vocabulary Object Detection with Vision Transformers (OWL-ViT)**<br>M. Minderer et al. | ECCV | [PDF ↗](https://arxiv.org/pdf/2205.06230) · [arXiv](https://arxiv.org/abs/2205.06230) | CLIP-style ViT turned into an open-vocabulary detector. |
| 2023 | **Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond**<br>J. Bai et al. | arXiv | [PDF ↗](https://arxiv.org/pdf/2308.12966) · [arXiv](https://arxiv.org/abs/2308.12966) | VLM with grounding and box output. |
| 2023 | **Segment Anything (SAM)**<br>A. Kirillov et al. | ICCV | [PDF](papers/06-open-vocabulary-vlm/kirillov2023sam.pdf) · [PDF ↗](https://arxiv.org/pdf/2304.02643) · [arXiv](https://arxiv.org/abs/2304.02643) | Promptable segmentation; SA-1B with 1B masks on 11M images. |
| 2023 | **Visual Instruction Tuning (LLaVA)**<br>H. Liu, C. Li, Q. Wu, Y. J. Lee | NeurIPS | [PDF ↗](https://arxiv.org/pdf/2304.08485) · [arXiv](https://arxiv.org/abs/2304.08485) | Instruction-tuned VLM from a vision encoder + LLM. |
| 2023 | **Kosmos-2: Grounding Multimodal Large Language Models to the World**<br>Z. Peng et al. | arXiv | [PDF ↗](https://arxiv.org/pdf/2306.14824) · [arXiv](https://arxiv.org/abs/2306.14824) | MLLM that outputs boxes as location tokens. |
| 2024 | **PaliGemma: A Versatile 3B VLM for Transfer**<br>L. Beyer et al. | arXiv | [PDF ↗](https://arxiv.org/pdf/2407.07726) · [arXiv](https://arxiv.org/abs/2407.07726) | Small transferable VLM with detection and segmentation tokens. |
| 2024 | **YOLO-World: Real-Time Open-Vocabulary Object Detection**<br>T. Cheng et al. | CVPR | [PDF](papers/06-open-vocabulary-vlm/cheng2024yoloworld.pdf) · [PDF ↗](https://arxiv.org/pdf/2401.17270) · [arXiv](https://arxiv.org/abs/2401.17270) | 35.4 AP zero-shot on LVIS at 52 FPS (V100). |
| 2024 | **Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection**<br>S. Liu et al. | ECCV | [PDF](papers/06-open-vocabulary-vlm/liu2024groundingdino.pdf) · [PDF ↗](https://arxiv.org/pdf/2303.05499) · [arXiv](https://arxiv.org/abs/2303.05499) | 52.5 AP zero-shot on COCO; text-prompted detection. |
| 2024 | **SAM 2: Segment Anything in Images and Videos**<br>N. Ravi et al. | arXiv / ICLR 2025 | [PDF ↗](https://arxiv.org/pdf/2408.00714) · [arXiv](https://arxiv.org/abs/2408.00714) | Streaming-memory video segmentation; 6x faster than SAM on images. |
| 2024 | **Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks**<br>B. Xiao et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/2311.06242) · [arXiv](https://arxiv.org/abs/2311.06242) | One sequence-to-sequence model for captioning, detection, grounding, segmentation. |

<a id="07-point-cloud-3d"></a>
## Point-cloud 3D detection

PointNet to voxel, pillar, point-voxel and center-based detectors.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2017 | **PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation**<br>C. R. Qi, H. Su, K. Mo, L. J. Guibas | CVPR | [PDF](papers/07-point-cloud-3d/qi2017pointnet.pdf) · [PDF ↗](https://arxiv.org/pdf/1612.00593) · [arXiv](https://arxiv.org/abs/1612.00593) | Permutation-invariant networks on raw points. |
| 2017 | **PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space**<br>C. R. Qi, L. Yi, H. Su, L. J. Guibas | NeurIPS | [PDF ↗](https://arxiv.org/pdf/1706.02413) · [arXiv](https://arxiv.org/abs/1706.02413) | Hierarchical local grouping. |
| 2018 | **SECOND: Sparsely Embedded Convolutional Detection**<br>Y. Yan, Y. Mao, B. Li | Sensors | [link](https://doi.org/10.3390/s18103337) | Sparse 3D convolutions for speed. |
| 2018 | **VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection**<br>Y. Zhou, O. Tuzel | CVPR | [PDF ↗](https://arxiv.org/pdf/1711.06396) · [arXiv](https://arxiv.org/abs/1711.06396) | Voxel feature encoding + 3D convolutions. |
| 2019 | **PointPillars: Fast Encoders for Object Detection from Point Clouds**<br>A. H. Lang et al. | CVPR | [PDF](papers/07-point-cloud-3d/lang2019pointpillars.pdf) · [PDF ↗](https://arxiv.org/pdf/1812.05784) · [arXiv](https://arxiv.org/abs/1812.05784) | Pillars + 2D CNN; 62 Hz (105 Hz fast version). |
| 2019 | **PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud**<br>S. Shi, X. Wang, H. Li | CVPR | [PDF ↗](https://arxiv.org/pdf/1812.04244) · [arXiv](https://arxiv.org/abs/1812.04244) | Two-stage point-based detection. |
| 2020 | **PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection**<br>S. Shi et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/1912.13192) · [arXiv](https://arxiv.org/abs/1912.13192) | Combines voxel and point features. |
| 2021 | **Center-based 3D Object Detection and Tracking (CenterPoint)**<br>T. Yin, X. Zhou, P. Krahenbuhl | CVPR | [PDF](papers/07-point-cloud-3d/yin2021centerpoint.pdf) · [PDF ↗](https://arxiv.org/pdf/2006.11275) · [arXiv](https://arxiv.org/abs/2006.11275) | Objects as BEV centres; 65.5 NDS, 63.8 AMOTA on nuScenes. |

<a id="08-camera-bev-fusion"></a>
## Camera 3D, BEV and sensor fusion

Lifting images to bird's-eye view; camera-lidar fusion.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2020 | **Lift, Splat, Shoot: Encoding Images From Arbitrary Camera Rigs by Implicitly Unprojecting to 3D**<br>J. Philion, S. Fidler | ECCV | [PDF ↗](https://arxiv.org/pdf/2008.05711) · [arXiv](https://arxiv.org/abs/2008.05711) | Per-pixel depth distributions lifted to BEV. |
| 2021 | **DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries**<br>Y. Wang et al. | CoRL | [PDF ↗](https://arxiv.org/pdf/2110.06922) · [arXiv](https://arxiv.org/abs/2110.06922) | 3D queries projected into images. |
| 2022 | **BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers**<br>Z. Li et al. | ECCV | [PDF ↗](https://arxiv.org/pdf/2203.17270) · [arXiv](https://arxiv.org/abs/2203.17270) | Camera-only 56.9 NDS on nuScenes, on par with lidar baselines. |
| 2023 | **BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation**<br>Z. Liu et al. | ICRA | [PDF ↗](https://arxiv.org/pdf/2205.13542) · [arXiv](https://arxiv.org/abs/2205.13542) | Camera + lidar fused in BEV; BEV pooling 40x faster. |

<a id="09-tracking"></a>
## Multi-object tracking

Tracking-by-detection to joint and end-to-end trackers, 2D and 3D.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1955 | **The Hungarian Method for the Assignment Problem**<br>H. W. Kuhn | Naval Research Logistics Quarterly | [link](https://doi.org/10.1002/nav.3800020109) | Optimal assignment, used by SORT and DETR. |
| 2016 | **Simple Online and Realtime Tracking (SORT)**<br>A. Bewley, Z. Ge, L. Ott, F. Ramos, B. Upcroft | ICIP | [PDF ↗](https://arxiv.org/pdf/1602.00763) · [arXiv](https://arxiv.org/abs/1602.00763) | Kalman filter + Hungarian on IoU; 260 Hz. |
| 2017 | **Simple Online and Realtime Tracking with a Deep Association Metric (DeepSORT)**<br>N. Wojke, A. Bewley, D. Paulus | ICIP | [PDF ↗](https://arxiv.org/pdf/1703.07402) · [arXiv](https://arxiv.org/abs/1703.07402) | Adds appearance re-identification features. |
| 2019 | **Tracking without Bells and Whistles (Tracktor)**<br>P. Bergmann, T. Meinhardt, L. Leal-Taixe | ICCV | [PDF ↗](https://arxiv.org/pdf/1903.05625) · [arXiv](https://arxiv.org/abs/1903.05625) | Detector regression head propagates tracks. |
| 2020 | **3D Multi-Object Tracking: A Baseline and New Evaluation Metrics (AB3DMOT)**<br>X. Weng, J. Wang, D. Held, K. Kitani | IROS | [PDF ↗](https://arxiv.org/pdf/1907.03961) · [arXiv](https://arxiv.org/abs/1907.03961) | 3D Kalman + Hungarian baseline. |
| 2021 | **FairMOT: On the Fairness of Detection and Re-Identification in Multiple Object Tracking**<br>Y. Zhang et al. | IJCV | [PDF ↗](https://arxiv.org/pdf/2004.01888) · [arXiv](https://arxiv.org/abs/2004.01888) | Joint detection and re-ID in one network. |
| 2022 | **BoT-SORT: Robust Associations Multi-Pedestrian Tracking**<br>N. Aharon, R. Orfaig, B.-Z. Bobrovsky | arXiv | [PDF ↗](https://arxiv.org/pdf/2206.14651) · [arXiv](https://arxiv.org/abs/2206.14651) | Camera-motion compensation + re-ID. |
| 2022 | **MOTR: End-to-End Multiple-Object Tracking with Transformer**<br>F. Zeng et al. | ECCV | [PDF ↗](https://arxiv.org/pdf/2105.03247) · [arXiv](https://arxiv.org/abs/2105.03247) | Track queries carried across frames. |
| 2022 | **ByteTrack: Multi-Object Tracking by Associating Every Detection Box**<br>Y. Zhang et al. | ECCV | [PDF](papers/09-tracking/zhang2022bytetrack.pdf) · [PDF ↗](https://arxiv.org/pdf/2110.06864) · [arXiv](https://arxiv.org/abs/2110.06864) | Associates low-score boxes too; 80.3 MOTA, 77.3 IDF1, 63.1 HOTA on MOT17 at 30 FPS. |
| 2023 | **Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking**<br>J. Cao et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/2203.14360) · [arXiv](https://arxiv.org/abs/2203.14360) | Fixes Kalman drift during occlusion. |

<a id="10-benchmarks-metrics"></a>
## Benchmarks and metrics

Driving datasets and tracking metrics.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2008 | **Evaluating Multiple Object Tracking Performance: The CLEAR MOT Metrics**<br>K. Bernardin, R. Stiefelhagen | EURASIP JIVP | [link](https://doi.org/10.1155/2008/246309) | MOTA and MOTP. |
| 2012 | **Are We Ready for Autonomous Driving? The KITTI Vision Benchmark Suite**<br>A. Geiger, P. Lenz, R. Urtasun | CVPR | [link](https://doi.org/10.1109/CVPR.2012.6248074) | 2D/3D detection and tracking benchmark. |
| 2016 | **MOT16: A Benchmark for Multi-Object Tracking**<br>A. Milan et al. | arXiv | [PDF ↗](https://arxiv.org/pdf/1603.00831) · [arXiv](https://arxiv.org/abs/1603.00831) | MOTChallenge pedestrian tracking benchmark. |
| 2016 | **Performance Measures and a Data Set for Multi-Target, Multi-Camera Tracking (IDF1)**<br>E. Ristani et al. | ECCV Workshops | [PDF ↗](https://arxiv.org/pdf/1609.01775) · [arXiv](https://arxiv.org/abs/1609.01775) | Identity-based metrics. |
| 2020 | **nuScenes: A Multimodal Dataset for Autonomous Driving**<br>H. Caesar et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/1903.11027) · [arXiv](https://arxiv.org/abs/1903.11027) | 6 cameras, lidar, radar; NDS metric. |
| 2020 | **Scalability in Perception for Autonomous Driving: Waymo Open Dataset**<br>P. Sun et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/1912.04838) · [arXiv](https://arxiv.org/abs/1912.04838) | Large-scale driving perception benchmark. |
| 2021 | **HOTA: A Higher Order Metric for Evaluating Multi-Object Tracking**<br>J. Luiten et al. | IJCV | [PDF ↗](https://arxiv.org/pdf/2009.07736) · [arXiv](https://arxiv.org/abs/2009.07736) | Balances detection and association. |
