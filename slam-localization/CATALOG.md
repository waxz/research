# Paper catalog

49 entries in 9 categories. **25** have a PDF available online (PDF ↗) and **9** also have a local copy in this repository (PDF).
Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.

| Category | Entries | PDF online | Local PDF |
|---|---:|---:|---:|
| [Surveys, tutorials and reference texts](#00-surveys-tutorials) | 7 | 3 | 2 |
| [Foundations of probabilistic localization and mapping](#01-foundations) | 3 | 0 | 0 |
| [Laser and LiDAR localization and SLAM](#02-laser-lidar) | 8 | 5 | 2 |
| [Visual odometry and visual SLAM](#03-visual) | 10 | 6 | 1 |
| [Visual-inertial navigation](#04-visual-inertial) | 3 | 2 | 2 |
| [Smoothing and factor graphs](#05-optimization) | 1 | 0 | 0 |
| [Learning-based and neural SLAM](#06-learning-neural) | 6 | 6 | 2 |
| [Spacecraft, planetary and Shuttle navigation](#07-space) | 9 | 3 | 0 |
| [Benchmarks and datasets](#08-benchmarks) | 2 | 0 | 0 |

<a id="00-surveys-tutorials"></a>
## Surveys, tutorials and reference texts

Where to start: SLAM surveys, the VO tutorial, the visual-inertial review, factor graphs.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2006 | **Simultaneous Localization and Mapping (SLAM): Part II**<br>T. Bailey, H. Durrant-Whyte | IEEE Robotics & Automation Magazine | [link](https://doi.org/10.1109/mra.2006.1678144) | Computational complexity, data association, environment representation. |
| 2006 | **Simultaneous Localization and Mapping: Part I**<br>H. Durrant-Whyte, T. Bailey | IEEE Robotics & Automation Magazine | [link](https://doi.org/10.1109/MRA.2006.1638022) | Tutorial on the SLAM problem and EKF/particle solutions. |
| 2011 | **Visual Odometry [Tutorial]**<br>D. Scaramuzza, F. Fraundorfer | IEEE Robotics & Automation Magazine | [link](https://doi.org/10.1109/mra.2011.943233) | Two-part tutorial on VO pipelines. |
| 2016 | **Past, Present, and Future of Simultaneous Localization and Mapping: Toward the Robust-Perception Age**<br>C. Cadena, L. Carlone, H. Carrillo, Y. Latif, D. Scaramuzza, J. Neira, I. Reid, J. J. Leonard | IEEE Transactions on Robotics | [PDF](papers/00-surveys-tutorials/cadena2016past.pdf) · [PDF ↗](https://arxiv.org/pdf/1606.05830) · [arXiv](https://arxiv.org/abs/1606.05830) | The standard modern SLAM survey: factor graphs, robustness, open problems. |
| 2017 | **Factor Graphs for Robot Perception**<br>F. Dellaert, M. Kaess | Foundations and Trends in Robotics | [link](https://doi.org/10.1561/2300000043) | The factor-graph view of SLAM and its solvers. |
| 2019 | **Visual-Inertial Navigation: A Concise Review**<br>G. Huang | ICRA | [PDF](papers/00-surveys-tutorials/huang2019vins.pdf) · [PDF ↗](https://arxiv.org/pdf/1906.02650) · [arXiv](https://arxiv.org/abs/1906.02650) | Filter vs optimization VINS, observability, calibration. |
| 2024 | **State Estimation for Robotics (2nd ed.)**<br>T. D. Barfoot | Cambridge University Press (free PDF) | [PDF ↗](https://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser24.pdf) | Estimation on Lie groups, batch and recursive. |

<a id="01-foundations"></a>
## Foundations of probabilistic localization and mapping

The Kalman filter, the stochastic map, graph-based scan alignment.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1960 | **A New Approach to Linear Filtering and Prediction Problems**<br>R. E. Kalman | Journal of Basic Engineering | [link](https://doi.org/10.1115/1.3662552) | The Kalman filter. |
| 1986 | **On the Representation and Estimation of Spatial Uncertainty**<br>R. C. Smith, P. Cheeseman | IJRR | [link](https://doi.org/10.1177/027836498600500404) | The stochastic map: correlated robot and landmark uncertainty. |
| 1997 | **Globally Consistent Range Scan Alignment for Environment Mapping**<br>F. Lu, E. Milios | Autonomous Robots | [link](https://doi.org/10.1023/A:1008854305733) | First pose-graph formulation of scan-based mapping. |

<a id="02-laser-lidar"></a>
## Laser and LiDAR localization and SLAM

Scan matching, lidar odometry and mapping, lidar-inertial fusion, place recognition, map-based vehicle localization.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2003 | **The Normal Distributions Transform: A New Approach to Laser Scan Matching**<br>P. Biber, W. Strasser | IROS | [link](https://doi.org/10.1109/iros.2003.1249285) | NDT: scan matching against local Gaussians; common for map-based car localization. |
| 2010 | **Robust Vehicle Localization in Urban Environments Using Probabilistic Maps**<br>J. Levinson, S. Thrun | ICRA | [PDF ↗](https://fileadmin.cs.lth.se/ai/Proceedings/ICRA2010/MainConference/data/papers/1912.pdf) · [link](https://doi.org/10.1109/robot.2010.5509700) | Lidar-intensity map localization with RMS accuracy in the 10 cm range. |
| 2014 | **LOAM: Lidar Odometry and Mapping in Real-time**<br>J. Zhang, S. Singh | RSS | [PDF ↗](https://www.roboticsproceedings.org/rss10/p07.pdf) · [link](https://doi.org/10.15607/rss.2014.x.007) | Edge/planar features, split odometry and mapping. |
| 2016 | **Real-Time Loop Closure in 2D LIDAR SLAM (Cartographer)**<br>W. Hess, D. Kohler, H. Rapp, D. Andor | ICRA | [link](https://doi.org/10.1109/icra.2016.7487258) | Submaps and branch-and-bound loop closure. |
| 2018 | **Scan Context: Egocentric Spatial Descriptor for Place Recognition within 3D Point Cloud Map**<br>G. Kim, A. Kim | IROS | [link](https://doi.org/10.1109/iros.2018.8593953) | Lidar place recognition for loop closure. |
| 2018 | **Robust and Precise Vehicle Localization based on Multi-sensor Fusion in Diverse City Scenes**<br>G. Wan et al. | ICRA | [PDF ↗](https://arxiv.org/pdf/1711.05805) · [arXiv](https://arxiv.org/abs/1711.05805) | GNSS RTK + lidar map + IMU error-state KF; 5-10 cm RMS. |
| 2020 | **LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping**<br>T. Shan, B. Englot, D. Meyers, W. Wang, C. Ratti, D. Rus | IROS | [PDF](papers/02-laser-lidar/shan2020liosam.pdf) · [PDF ↗](https://arxiv.org/pdf/2007.00258) · [arXiv](https://arxiv.org/abs/2007.00258) | Factor-graph LIO with IMU preintegration, GPS and loop-closure factors. |
| 2022 | **FAST-LIO2: Fast Direct LiDAR-inertial Odometry**<br>W. Xu, Y. Cai, D. He, J. Lin, F. Zhang | IEEE Transactions on Robotics | [PDF](papers/02-laser-lidar/xu2022fastlio2.pdf) · [PDF ↗](https://arxiv.org/pdf/2107.06829) · [arXiv](https://arxiv.org/abs/2107.06829) | Iterated error-state KF registering raw points; ikd-Tree map. |

<a id="03-visual"></a>
## Visual odometry and visual SLAM

Feature-based, direct and dense camera methods, learned features and place recognition.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2004 | **Visual Odometry**<br>D. Nister, O. Naroditsky, J. Bergen | CVPR | [link](https://doi.org/10.1109/cvpr.2004.1315094) | Named and established real-time visual odometry. |
| 2007 | **MonoSLAM: Real-Time Single Camera SLAM**<br>A. J. Davison, I. D. Reid, N. D. Molton, O. Stasse | IEEE TPAMI | [link](https://doi.org/10.1109/tpami.2007.1049) | EKF SLAM with a single camera. |
| 2007 | **Parallel Tracking and Mapping for Small AR Workspaces (PTAM)**<br>G. Klein, D. Murray | ISMAR | [link](https://doi.org/10.1109/ismar.2007.4538852) | Split tracking and keyframe bundle adjustment. |
| 2011 | **KinectFusion: Real-Time Dense Surface Mapping and Tracking**<br>R. A. Newcombe et al. | ISMAR | [link](https://doi.org/10.1109/ismar.2011.6092378) | Dense RGB-D mapping on GPU. |
| 2015 | **ORB-SLAM: a Versatile and Accurate Monocular SLAM System**<br>R. Mur-Artal, J. M. M. Montiel, J. D. Tardos | IEEE Transactions on Robotics | [PDF ↗](https://arxiv.org/pdf/1502.00956) · [arXiv](https://arxiv.org/abs/1502.00956) | Feature-based SLAM with loop closing and relocalization. |
| 2016 | **NetVLAD: CNN Architecture for Weakly Supervised Place Recognition**<br>R. Arandjelovic et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/1511.07247) · [arXiv](https://arxiv.org/abs/1511.07247) | Learned global descriptors for loop closure. |
| 2017 | **Direct Sparse Odometry**<br>J. Engel, V. Koltun, D. Cremers | IEEE TPAMI | [PDF ↗](https://arxiv.org/pdf/1607.02565) · [arXiv](https://arxiv.org/abs/1607.02565) | Direct photometric optimization. |
| 2018 | **SuperPoint: Self-Supervised Interest Point Detection and Description**<br>D. DeTone, T. Malisiewicz, A. Rabinovich | CVPR Workshops | [PDF ↗](https://arxiv.org/pdf/1712.07629) · [arXiv](https://arxiv.org/abs/1712.07629) | Learned keypoints. |
| 2020 | **SuperGlue: Learning Feature Matching with Graph Neural Networks**<br>P.-E. Sarlin, D. DeTone, T. Malisiewicz, A. Rabinovich | CVPR | [PDF ↗](https://arxiv.org/pdf/1911.11763) · [arXiv](https://arxiv.org/abs/1911.11763) | Learned matching. |
| 2021 | **ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM**<br>C. Campos, R. Elvira, J. J. G. Rodriguez, J. M. M. Montiel, J. D. Tardos | IEEE Transactions on Robotics | [PDF](papers/03-visual/campos2021orbslam3.pdf) · [PDF ↗](https://arxiv.org/pdf/2007.11898) · [arXiv](https://arxiv.org/abs/2007.11898) | Multi-map visual-inertial SLAM; 2-5x more accurate than prior systems (authors). |

<a id="04-visual-inertial"></a>
## Visual-inertial navigation

Filter- and optimization-based camera + IMU fusion.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2007 | **A Multi-State Constraint Kalman Filter for Vision-aided Inertial Navigation**<br>A. I. Mourikis, S. I. Roumeliotis | ICRA | [link](https://doi.org/10.1109/robot.2007.364024) | Filter-based VIO without landmarks in the state. |
| 2017 | **On-Manifold Preintegration for Real-Time Visual-Inertial Odometry**<br>C. Forster, L. Carlone, F. Dellaert, D. Scaramuzza | IEEE Transactions on Robotics | [PDF](papers/04-visual-inertial/forster2017preint.pdf) · [PDF ↗](https://arxiv.org/pdf/1512.02363) · [arXiv](https://arxiv.org/abs/1512.02363) | IMU preintegration on SO(3). |
| 2018 | **VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator**<br>T. Qin, P. Li, S. Shen | IEEE Transactions on Robotics | [PDF](papers/04-visual-inertial/qin2018vinsmono.pdf) · [PDF ↗](https://arxiv.org/pdf/1708.03852) · [arXiv](https://arxiv.org/abs/1708.03852) | Sliding-window optimization VIO with 4-DoF pose graph. |

<a id="05-optimization"></a>
## Smoothing and factor graphs

Incremental nonlinear least squares for SLAM.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2012 | **iSAM2: Incremental Smoothing and Mapping Using the Bayes Tree**<br>M. Kaess et al. | IJRR | [link](https://doi.org/10.1177/0278364911430419) | Incremental factor-graph solver behind GTSAM. |

<a id="06-learning-neural"></a>
## Learning-based and neural SLAM

Deep SLAM, neural implicit and Gaussian-splatting maps, 3D foundation models.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2021 | **iMAP: Implicit Mapping and Positioning in Real-Time**<br>E. Sucar, S. Liu, J. Ortiz, A. J. Davison | ICCV | [PDF ↗](https://arxiv.org/pdf/2103.12352) · [arXiv](https://arxiv.org/abs/2103.12352) | Neural implicit map as the SLAM representation. |
| 2021 | **DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras**<br>Z. Teed, J. Deng | NeurIPS | [PDF](papers/06-learning-neural/teed2021droid.pdf) · [PDF ↗](https://arxiv.org/pdf/2108.10869) · [arXiv](https://arxiv.org/abs/2108.10869) | Recurrent updates through a differentiable dense bundle-adjustment layer. |
| 2024 | **SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM**<br>N. Keetha et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/2312.02126) · [arXiv](https://arxiv.org/abs/2312.02126) | Gaussian-splatting SLAM (RGB-D). |
| 2024 | **Gaussian Splatting SLAM**<br>H. Matsuki, R. Murai, P. H. J. Kelly, A. J. Davison | CVPR | [PDF ↗](https://arxiv.org/pdf/2312.06741) · [arXiv](https://arxiv.org/abs/2312.06741) | Monocular Gaussian-splatting SLAM. |
| 2024 | **DUSt3R: Geometric 3D Vision Made Easy**<br>S. Wang et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/2312.14132) · [arXiv](https://arxiv.org/abs/2312.14132) | 3D foundation model predicting pointmaps from image pairs. |
| 2025 | **MASt3R-SLAM: Real-Time Dense SLAM with 3D Reconstruction Priors**<br>R. Murai, E. Dexheimer, A. J. Davison | CVPR | [PDF](papers/06-learning-neural/murai2025mast3rslam.pdf) · [PDF ↗](https://arxiv.org/pdf/2412.12392) · [arXiv](https://arxiv.org/abs/2412.12392) | Monocular dense SLAM on a learned 3D prior, 15 FPS. |

<a id="07-space"></a>
## Spacecraft, planetary and Shuttle navigation

Attitude determination, the Apollo-era Kalman filter, Shuttle navigation, rover visual odometry, terrain-relative landing, Mars helicopter.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1965 | **A Least Squares Estimate of Satellite Attitude (Wahba's problem)**<br>G. Wahba | SIAM Review | [link](https://doi.org/10.1137/1007077) | Attitude from vector observations. |
| 1975 | **Space Shuttle entry navigation study (aided-inertial Kalman filter)**<br>The Analytic Sciences Corp. for NASA | NASA technical report | [PDF ↗](https://ntrs.nasa.gov/api/citations/19750015582/downloads/19750015582.pdf) · [link](https://ntrs.nasa.gov/citations/19750015582) | IMU aided by TACAN, MLS and altimeters through a Kalman filter. |
| 1981 | **Three-Axis Attitude Determination from Vector Observations (QUEST)**<br>M. D. Shuster, S. D. Oh | Journal of Guidance and Control | [link](https://doi.org/10.2514/3.19717) | TRIAD and QUEST algorithms. |
| 1982 | **Kalman Filtering for Spacecraft Attitude Estimation**<br>E. J. Lefferts, F. L. Markley, M. D. Shuster | AIAA Aerospace Sciences Meeting | [link](https://doi.org/10.2514/6.1982-70) | Multiplicative EKF for gyro + star-tracker attitude. |
| 1985 | **Discovery of the Kalman Filter as a Practical Tool for Aerospace and Industry**<br>L. A. McGee, S. F. Schmidt | NASA TM-86847 | [PDF ↗](https://ntrs.nasa.gov/api/citations/19860003843/downloads/19860003843.pdf) · [link](https://ntrs.nasa.gov/citations/19860003843) | How the Kalman filter entered Apollo navigation. |
| 1989 | **Space Shuttle Avionics: Guidance, Navigation and Control (NASA SP-504, section 4.5)**<br>NASA | NASA SP-504 | [link](https://www.klabs.org/DEI/Processor/shuttle/sp-504/section_4/section_4_05_guidance_navigation_control.htm) | Three IMUs, two star trackers, Kalman updates with fault detection. |
| 2007 | **Two Years of Visual Odometry on the Mars Exploration Rovers**<br>M. Maimone, Y. Cheng, L. Matthies | Journal of Field Robotics 24(3) | [PDF ↗](https://robotics.jpl.nasa.gov/media/documents/rob-06-0081.R4.pdf) · [link](https://doi.org/10.1002/rob.20184) | Stereo VO on Spirit and Opportunity; slip detection. |
| 2019 | **Vision-Based Navigation for the NASA Mars Helicopter**<br>D. S. Bayard et al. | AIAA SciTech | [link](https://doi.org/10.2514/6.2019-1411) | Camera + IMU + laser altimeter navigation for Ingenuity. |
| 2023 | **Mars 2020 Lander Vision System flight performance**<br>NASA JPL | NASA technical report | [link](https://ntrs.nasa.gov/citations/20230006986) | Terrain-relative navigation fusing map-matched landmarks with IMU. |

<a id="08-benchmarks"></a>
## Benchmarks and datasets

How accuracy claims are measured.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2012 | **Are We Ready for Autonomous Driving? The KITTI Vision Benchmark Suite**<br>A. Geiger, P. Lenz, R. Urtasun | CVPR | [link](https://doi.org/10.1109/cvpr.2012.6248074) | Odometry benchmark (drift in % of distance). |
| 2016 | **The EuRoC Micro Aerial Vehicle Datasets**<br>M. Burri et al. | IJRR | [link](https://doi.org/10.1177/0278364915620033) | Visual-inertial benchmark with ground truth. |
