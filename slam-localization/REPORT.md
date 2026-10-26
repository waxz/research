# SLAM and localization: lasers, LiDAR, cameras, IMUs and encoders

*An analysis of how mobile robots, self-driving cars and spacecraft (including the Space Shuttle) know where they are. It follows the format of the other collections in this repository. Equations are derived in the companion [cookbook](cookbook/COOKBOOK.md) (recipes S1–S21), and every source is in the [catalog](CATALOG.md). Quantitative claims were checked against abstracts or primary NASA sources on 26 Oct 2026.*

## Summary

- **Every platform solves the same problem:** dead-reckon with fast, drifting sensors, then correct with slower absolute measurements. Only the sensors and the stakes change.

  | Platform | Dead reckoning | Absolute correction |
  |---|---|---|
  | Warehouse robot | Wheel encoders | 2D laser scan against a map |
  | Self-driving car | IMU + wheel speed | Lidar against an HD map, plus RTK-GNSS |
  | Space Shuttle | Three IMUs | Star trackers, TACAN and the microwave landing system, through a Kalman filter |
  | Mars rover | Wheel odometry and IMU | Stereo visual odometry |

- **Model-based estimation still runs the field**, with one paradigm shift. In the 2000s, filtering (EKF, particle filters) gave way to **smoothing**: nonlinear least squares over factor graphs, as in iSAM2, ORB-SLAM3, VINS-Mono and LIO-SAM. The Kalman filter survives where computing is tight or latency matters: FAST-LIO2, MSCKF, spacecraft attitude, and the car's GNSS/INS fusion.
- **Learning has entered through perception, not estimation.**
  - learned features and matching (SuperPoint, SuperGlue);
  - place recognition (NetVLAD);
  - dense learned SLAM (DROID-SLAM);
  - neural and Gaussian-splatting maps;
  - 3D foundation models (DUSt3R, MASt3R-SLAM).

  The geometric back-end (bundle adjustment, pose graphs) remains, often *inside* the learned system.
- **"Reference vs self-exploration" has a clean analogue.** **Map-based localization** tracks against a prior reference map: AMCL, NDT on HD maps, terrain-relative navigation with orbital maps. **SLAM** builds its own map as it explores. Industry prefers maps wherever it can build them, because they bound error and make behaviour predictable.

---

## 1. Problem definitions

| Term | Estimates | Uses a prior map? | Drift |
|---|---|---|---|
| Dead reckoning / odometry | Motion from internal sensors (encoders, IMU) | No | Unbounded, grows with time or distance |
| Visual / lidar / visual-inertial odometry (VO, LO, VIO, LIO) | Motion from exteroceptive sensors, locally | No | Unbounded but slow (fractions of a percent of distance) |
| Localization | Pose in a known map or frame (GNSS, star catalog, HD map) | Yes | Bounded |
| SLAM | Pose *and* map together | No (builds one) | Bounded when loops close |
| Place recognition / loop closure | "Have I been here?" | Its own past | Removes accumulated drift |

**Filtering vs smoothing.** A filter keeps only the current state and a covariance and marginalizes the past (EKF, MSCKF, particle filter). A smoother keeps a window or the whole trajectory and re-linearizes as estimates improve (bundle adjustment, factor graphs). Smoothing is more accurate on nonlinear problems; filtering is cheaper and has constant latency (S11, S14).

## 2. The sensors

| Sensor | Measures | Rate | Strengths | Failure modes | Cookbook |
|---|---|---|---|---|---|
| **Wheel encoders** | Wheel rotation, giving distance and heading change | 100–1000 Hz | Cheap, precise on good floors | Slip, wheel wear, uneven ground; drift grows with distance | S2; mobile M6 |
| **IMU** (gyro + accelerometer) | Angular rate, specific force | 100–1000+ Hz | Self-contained, high rate, any environment | Bias integrates: position error grows as $t^2$ from accelerometer bias, faster from gyro tilt | S2, S3, S10 |
| **2D laser scanner** | Ranges in a plane | 10–50 Hz | Precise (mm–cm), indoor workhorse | Glass, black surfaces, long featureless corridors | S13, S17 |
| **3D LiDAR** (spinning, solid-state, FMCW) | 3D point clouds | 10–20 Hz | Metric 3D, lighting-independent | Motion distortion, rain, snow and fog, degenerate geometry (tunnels) | S12, S16 |
| **Camera** (mono, stereo, RGB-D, event) | Images | 10–100+ Hz | Rich texture, cheap, good for place recognition | Lighting, motion blur, textureless scenes; monocular scale is unobservable | S6–S9 |
| **GNSS** (GPS etc., RTK) | Pseudoranges, giving global position | 1–20 Hz | Global, absolute; RTK reaches cm level | Urban canyons, multipath, tunnels; not available far from Earth | S4, S5 |
| **Radar** | Range, Doppler | 10–20 Hz | Works in weather | Sparse, noisy | (mentioned) |
| **Star tracker** | Inertial attitude from star patterns | 1–10 Hz | Arcsecond attitude | Sun or Earth in view, high rates | S19 |
| **Radio navaids** (TACAN, MLS, DSN ranging) | Range and bearing to beacons | Low | Absolute | Infrastructure-dependent | S19 |

**IMU grades** (S2). The figures below are for uncompensated accelerometer bias, the reason IMUs always need aiding:

| Accelerometer bias | Typical grade | Position error after 60 s | After 10 min |
|---|---|---:|---:|
| 10 mg | Consumer MEMS | ≈ 177 m | ≈ 17.7 km |
| 1 mg | Industrial MEMS | ≈ 18 m | ≈ 1.8 km |
| 25 µg | Navigation grade | ≈ 0.4 m | ≈ 44 m |

## 3. Platforms

| Platform | Typical sensor suite | Typical estimator | Accuracy needed | Notes |
|---|---|---|---|---|
| **Warehouse AMR / AGV** | 2D safety lidars, wheel encoders, IMU; sometimes ceiling camera or reflectors | AMCL or EKF on a 2D map; Cartographer for mapping | ±1–5 cm, ±10 mm at docks | Mostly *map-based*: maps are built once with SLAM, then localized against |
| **Self-driving car** | 3D lidars, cameras, RTK-GNSS, automotive or tactical IMU, wheel speed, radar | Error-state KF fusing GNSS/INS with lidar map matching (NDT or intensity maps); SLAM offline to build HD maps | ~10 cm lateral (lane-level and better) | Levinson & Thrun (2010): RMS accuracy in the 10 cm range; Baidu (Wan et al. 2018): 5–10 cm RMS including tunnels and downtown |
| **Drone / MAV** | Camera(s) + IMU, sometimes lidar | VIO (MSCKF, VINS-Mono, ORB-SLAM3) | Decimetres, drift < 1% | Weight and power favour camera + IMU |
| **Space Shuttle** (1981–2011) | Three IMUs, two star trackers, TACAN, microwave landing system, air data, altimeters; GPS added late | IMU propagation with Kalman-filter updates from navaids, each gated by a fault-detection test; star trackers align the IMUs | Entry and landing on a runway | GPS ran in parallel with TACAN on four missions in 2006–07, before an all-GPS, no-TACAN flight (NASA) |
| **Apollo** (1960s) | IMU, optical sextant, ground tracking | Schmidt's extended Kalman filter, first used for Apollo navigation studies at NASA Ames | Translunar navigation | McGee & Schmidt 1985 (NASA TM-86847) |
| **Satellites** | Gyros, star trackers, sun sensors, magnetometers, GNSS (low Earth orbit) | Wahba/QUEST attitude + multiplicative EKF (Lefferts, Markley & Shuster 1982) | Arcseconds (attitude) | Attitude dominates; orbit from GNSS or ground tracking |
| **Mars rovers** | Stereo cameras, IMU, wheel odometry | Stereo visual odometry corrects wheel slip | Centimetres per drive | Spirit and Opportunity VO converged about 97% / 95% of the time and detected slip up to 125% (Maimone et al. 2007) |
| **Mars landers** (Perseverance 2021) | Descent camera, IMU, radar | Terrain-relative navigation: match descent images to an orbital map, fused with the IMU | Required within 60 m of target | The Lander Vision System starts around 4.2 km altitude (NASA) |
| **Mars helicopter** (Ingenuity) | Downward camera, IMU, laser altimeter | Vision-based navigation filter (Bayard et al. 2019) | Short flights over flat terrain | VIO in the thin Martian atmosphere |

## 4. Why localization and SLAM are hard

| Difficulty | Example | Cookbook |
|---|---|---|
| **Drift** | Odometry and inertial errors integrate: an accelerometer bias gives $\tfrac12bt^2$; a gyro error tilts the gravity vector | S2, S3 |
| **Observability** | Monocular vision has no scale. VIO cannot observe global position or yaw (4 directions). A lidar in a long corridor cannot observe motion along it | S9, S17 |
| **Data association** | Matching the wrong feature or scan; repetitive structure (aisles, crop rows); false loop closures | S7, S15 |
| **Nonlinearity and manifolds** | Rotations live on SO(3), not $\mathbb R^3$; naïve linearization breaks filters | S1, S11 |
| **Motion distortion and timing** | A spinning lidar measures during motion; a 10 ms timestamp error at 20 m/s is 0.2 m | S12, S18 |
| **Calibration** | Camera intrinsics, lidar–IMU extrinsics, time offsets | S18 |
| **Dynamic and changing worlds** | People, cars, moved pallets, seasons, lighting | S15, S16 |
| **Compute and power** | Embedded CPUs on robots; radiation-hardened processors on spacecraft | S11, S14 |
| **No GNSS** | Indoors, underground, tunnels, and anywhere beyond Earth orbit | S5, S19 |

## 5. Three paradigms

Here the three families are:
- **MB:** geometric and probabilistic model-based estimation;
- **LRN:** learning-based;
- **MAP:** reference-map-based. This is the localization counterpart of reference tracking.

| Criterion | MB: filters and smoothers (EKF, MSCKF, factor graphs, ICP/NDT, bundle adjustment) | LRN: learned components and end-to-end (SuperPoint/SuperGlue, NetVLAD, DROID-SLAM, neural/Gaussian maps, DUSt3R/MASt3R) | MAP: localization against a prior map (AMCL, NDT on HD maps, terrain-relative navigation, star catalogs) |
|---|---|---|---|
| Needs | Sensor models, calibration | Training data, GPUs | A map built and maintained beforehand |
| Accuracy | High where geometry is good | High on benchmarks; fewer catastrophic failures (DROID-SLAM) | Highest and bounded (10 cm cars; arcseconds with star catalogs) |
| Robustness to appearance change | Weak for vision, strong for lidar | Strongest (learned features and place recognition) | Depends on map freshness |
| Uncertainty estimates | Principled covariances | Usually poor or absent | Principled if the map is |
| Compute | CPU real-time | GPU-heavy (MASt3R-SLAM runs at 15 FPS) | Low online, high for map building |
| Certifiability | Good (aerospace practice) | Hard | Good, with integrity monitoring |
| Where it dominates | Robots, drones, spacecraft, car fusion | Perception front-ends, AR, research | Warehouses, robotaxis, landers, spacecraft attitude |

**What the surveys say.**
- Cadena et al. (2016) frame modern SLAM as maximum-a-posteriori estimation on factor graphs. They name robustness (failure detection, outlier rejection, long-term operation) as the main open challenge, not accuracy.
- Huang (2019) reviews the filter-vs-optimization split in visual-inertial navigation and stresses observability and consistency.

## 6. Map-based localization vs SLAM (reference vs self-exploration)

| Dimension | Map-based localization | SLAM |
|---|---|---|
| Error | Bounded by map accuracy | Bounded only when loops close; drifts between closures |
| Setup cost | Survey or map the site first; keep the map current | None up front |
| Robustness | Fails if the world changes past the map (moved pallets, construction) | Adapts, but can corrupt its map with false loop closures |
| Compute online | Low (match against a fixed map) | Higher (map building, loop closure, optimization) |
| Typical users | Warehouse AMRs, robotaxis, planetary landers, star trackers | Exploration robots, AR/VR, drones, mapping vehicles, first visits |

**Practice combines them.** Build the map with SLAM (offline or during commissioning), freeze it, then localize against it. Run SLAM in the background to detect and patch changes. Cars do this with HD maps; warehouse robots do it with Cartographer maps plus AMCL.

## 7. Fusion architectures

- **Loosely coupled.** Each sensor produces its own pose estimate (a GNSS fix, a VO pose), and a filter fuses the poses. Simple and modular, but it loses information when a sensor is weak (two satellites still carry information that a loosely coupled system throws away).
- **Tightly coupled.** Raw measurements (pseudoranges, feature tracks, lidar points) and IMU data enter one estimator: FAST-LIO2 (iterated EKF), LIO-SAM and VINS-Mono (factor graphs), ORB-SLAM3 (MAP estimation including IMU initialization). More accurate and robust, but harder to engineer.
- **The IMU is the backbone** in almost every tightly coupled system. It bridges gaps between slower sensors, de-skews lidar scans, and makes monocular scale observable through gravity and acceleration (S9, S10).

## 8. Which method for which task

| | Map available or buildable | Unknown or changing environment |
|---|---|---|
| **GNSS or radio available** | GNSS/INS + map matching (robotaxis, Shuttle entry with TACAN/MLS) | GNSS/INS + VO/LO for gaps (agriculture, outdoor robots) |
| **No GNSS** | Lidar/AMCL on site maps (warehouses); terrain-relative navigation (Mars landing); star catalogs (attitude) | LIO/VIO SLAM (drones, mines, caves); stereo VO (Mars rovers); learned dense SLAM (AR, research) |

Fit: ●●● strong, ●● viable, ● niche, ○ rarely used.

| Task | Best-suited approach | Fit MB · LRN · MAP | Evidence |
|---|---|---|---|
| Warehouse AMR / forklift | 2D lidar + encoders + IMU; AMCL or reflector EKF on a commissioned map | ●●● ● ●●● | Industry standard (see the mobile-robot collection) |
| Robotaxi in a city | RTK-GNSS + IMU + lidar map matching in an error-state KF; camera for lanes and signs | ●●● ●● ●●● | 10 cm RMS (Levinson 2010); 5–10 cm RMS (Wan 2018) |
| Drone in a GPS-denied building | Tightly coupled VIO (camera + IMU), optionally a small lidar | ●●● ●● ● | VINS-Mono, ORB-SLAM3 |
| Mine, tunnel, subterranean robot | Lidar-inertial odometry + loop closure; beware degenerate tunnels | ●●● ● ●● | LIO-SAM, FAST-LIO2 |
| AR/VR headset | VIO + relocalization against shared maps; learned features | ●●● ●● ●● | ORB-SLAM3-class pipelines |
| Planetary rover | Stereo VO + IMU + wheel odometry; slip detection | ●●● ○ ● | 97% / 95% VO convergence on Spirit / Opportunity |
| Planetary landing | Terrain-relative navigation against orbital maps + IMU | ●● ● ●●● | Mars 2020 LVS, 60 m requirement |
| Spacecraft attitude | Star tracker + gyro multiplicative EKF; Wahba/QUEST for lost-in-space | ●●● ○ ●●● | Lefferts, Markley & Shuster 1982 |
| Space Shuttle entry and landing | Redundant IMUs + Kalman filter with navaid updates and fault detection | ●●● ○ ●● | NASA SP-504; TACAN → GPS transition 2006–07 |
| Dense 3D reconstruction from video | Learned dense SLAM or 3D foundation models | ●● ●●● ○ | DROID-SLAM, MASt3R-SLAM |

## 9. Breakthroughs, year by year

| Year | Breakthrough | Problem it solved | Evidence / reach |
|---|---|---|---|
| 1960 | Kalman filter | Optimal recursive estimation from noisy measurements | Kalman 1960 |
| Early 1960s | Schmidt's extended Kalman filter for Apollo | Nonlinear navigation on a small flight computer | Studies at NASA Ames (McGee & Schmidt 1985) |
| 1965 | Wahba's problem | Attitude from vector observations | Basis of star-tracker attitude |
| 1981 | Space Shuttle first flight; QUEST | Redundant aided-inertial navigation for a reusable vehicle; fast optimal attitude | Three IMUs + star trackers + Kalman updates with fault detection; Shuster & Oh 1981 |
| 1982 | Multiplicative EKF for spacecraft attitude | Filtering quaternions correctly on SO(3) | Lefferts, Markley & Shuster |
| 1986 | The stochastic map | Robot and landmark uncertainties are correlated | Smith & Cheeseman; the start of SLAM |
| 1997 | Graph-based scan alignment | Globally consistent maps from laser scans | Lu & Milios; the first pose graph |
| 1999 | Monte Carlo localization | Multimodal, global localization | Dellaert et al. (mobile collection) |
| 2003 | NDT scan matching | Robust laser registration | Biber & Strasser; later standard for car map matching |
| 2004 | Visual odometry; Mars rovers land | Camera-based motion estimation in real time | Nistér et al.; Spirit and Opportunity VO from 2004 |
| 2007 | MonoSLAM, PTAM, MSCKF | Real-time single-camera SLAM; keyframe bundle adjustment; efficient VIO filter | Davison et al.; Klein & Murray; Mourikis & Roumeliotis |
| 2010 | Probabilistic lidar maps for cars | Centimetre-level urban localization | Levinson & Thrun: RMS in the 10 cm range |
| 2011–12 | KinectFusion; iSAM2; KITTI | Dense RGB-D mapping; incremental smoothing; standard benchmarks | Newcombe et al.; Kaess et al.; Geiger et al. |
| 2014 | LOAM | Real-time 3D lidar odometry and mapping | Zhang & Singh |
| 2015–17 | ORB-SLAM, DSO, IMU preintegration, VINS-Mono | Robust feature and direct visual SLAM; efficient VIO optimization | Mur-Artal et al.; Engel et al.; Forster et al.; Qin et al. |
| 2016 | Cartographer; the Cadena et al. survey | Real-time 2D lidar loop closure; the factor-graph consensus | Hess et al.; Cadena et al. |
| 2018–20 | SuperPoint, SuperGlue, NetVLAD; Baidu multi-sensor fusion | Learned features, matching and place recognition; cm-level city localization | 5–10 cm RMS including tunnels (Wan et al.) |
| 2020–21 | LIO-SAM, FAST-LIO2, ORB-SLAM3, DROID-SLAM | Tightly coupled lidar-inertial; multi-map VI-SLAM (2–5× more accurate per its authors); deep SLAM with fewer catastrophic failures | Shan et al.; Xu et al.; Campos et al.; Teed & Deng |
| 2021 | Perseverance terrain-relative landing; Ingenuity flights | Hazard-avoiding precision landing; vision navigation on another planet | NASA LVS; Bayard et al. |
| 2023–24 | Neural and Gaussian-splatting SLAM; DUSt3R | Photorealistic dense maps; geometry from a learned 3D prior | iMAP, SplaTAM, Gaussian Splatting SLAM, DUSt3R |
| 2025 | MASt3R-SLAM | Real-time monocular dense SLAM on a 3D foundation model | Murai et al., 15 FPS |

## 10. Quick start: textbooks and tutorials

| Resource | Access | Start with | Covers |
|---|---|---|---|
| *Probabilistic Robotics*, Thrun, Burgard & Fox (2005) | Book | Gaussian filters, particle filters, EKF and graph SLAM chapters | S5, S13–S14 |
| [State Estimation for Robotics](https://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser24.pdf), Barfoot (2nd ed., 2024) | Free PDF | Linear-Gaussian estimation, matrix Lie groups, pose estimation | S1, S11, S14 |
| [A Micro Lie Theory for State Estimation in Robotics](https://arxiv.org/abs/1812.01537), Solà et al. | Free paper | Exp/log maps and Jacobians on SO(3) and SE(3) | S1, S10 |
| *Multiple View Geometry in Computer Vision*, Hartley & Zisserman (2nd ed., 2004) | Book | Camera models, epipolar geometry, triangulation, bundle adjustment | S6–S8 |
| [Computer Vision: Algorithms and Applications](https://szeliski.org/Book/), Szeliski (2nd ed.) | Free PDF | Feature detection, structure from motion, SLAM sections | S6–S9, S15 |
| Visual Odometry tutorial, Scaramuzza & Fraundorfer (RAM 2011–12) | Paper | Both parts | S7–S9 |
| [Visual-Inertial Navigation: A Concise Review](https://arxiv.org/abs/1906.02650), Huang (2019) | Free paper | Filter vs optimization, observability | S9–S11 |
| Factor Graphs for Robot Perception, Dellaert & Kaess (2017) | Monograph | The whole text, with GTSAM | S14 |
| *Principles of GNSS, Inertial, and Multisensor Integrated Navigation Systems*, Paul Groves (2nd ed., 2013) | Book | Inertial navigation, GNSS, INS/GNSS integration | S2–S5 |
| *Fundamentals of Spacecraft Attitude Determination and Control*, Markley & Crassidis (2014) | Book | Static attitude determination, attitude filtering | S19 |
| [Stachniss lectures](https://www.ipb.uni-bonn.de/teaching/) (Uni Bonn) | Free videos | SLAM course, graph-based SLAM, ICP | S12–S15 |
| [Cadena et al. survey](https://arxiv.org/abs/1606.05830) | Free paper | Sections on the factor-graph formulation and open problems | Whole field |

The general linear algebra, probability, Kalman filter and deep learning background is in the [Control-to-Learning cookbook](../robot-learning-control/cookbook/COOKBOOK.md) (R1–R3, R9, R18–R22).

## 11. Sources

All works are in [CATALOG.md](CATALOG.md) with DOI, arXiv or NASA links (9 local PDFs). Space-program facts come from:
- [NASA SP-504 GNC section](https://www.klabs.org/DEI/Processor/shuttle/sp-504/section_4/section_4_05_guidance_navigation_control.htm);
- the [NASA Shuttle entry-navigation report](https://ntrs.nasa.gov/citations/19750015582);
- the [Shuttle GNC overview workbook](https://ibiblio.org/apollo/Shuttle/TD0198%20-%20GNC%20OV%202102%20-%20GNC%20Overview%20Workbook.pdf);
- [McGee & Schmidt 1985](https://ntrs.nasa.gov/citations/19860003843);
- the [Mars 2020 TRN/LVS reports](https://ntrs.nasa.gov/citations/20230006986) and the [NASA TRN overview](https://science.nasa.gov/technology/technology-highlights/terrain-relative-navigation-landing-between-the-hazards);
- the [JPL MER visual odometry paper](https://robotics.jpl.nasa.gov/media/documents/rob-06-0081.R4.pdf).

The Shuttle GPS transition (four missions in 2006–07) comes from a NASA-sourced search excerpt; check the original NASA document before formal citation.
