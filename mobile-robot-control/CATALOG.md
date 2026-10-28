# Paper catalog

49 entries in 8 categories. **22** have a PDF available online (PDF ↗) and **8** also have a local copy in this repository (PDF).
Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.

| Category | Entries | PDF online | Local PDF |
|---|---:|---:|---:|
| [Surveys and overview papers](#00-surveys) | 5 | 1 | 1 |
| [Localization and mapping](#01-localization-mapping) | 7 | 1 | 0 |
| [Path and motion planning](#02-planning) | 4 | 2 | 1 |
| [Path tracking and local obstacle avoidance](#03-tracking-and-local-control) | 10 | 2 | 1 |
| [Fleet management and multi-robot coordination](#04-fleet-management) | 4 | 1 | 1 |
| [Learning-based navigation](#05-learning-navigation) | 12 | 12 | 3 |
| [Systems and deployments](#06-systems-and-deployments) | 5 | 2 | 1 |
| [Standards](#07-standards) | 2 | 1 | 0 |

<a id="00-surveys"></a>
## Surveys and overview papers

Reviews of AGV/AMR planning and control, and of learning-based mobile robot navigation.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2006 | **A Review of Design and Control of Automated Guided Vehicle Systems**<br>T. Le-Anh, M. B. M. De Koster | European Journal of Operational Research | [link](https://doi.org/10.1016/j.ejor.2005.01.036) | Dispatching, scheduling and deadlock handling for AGV systems. |
| 2006 | **Survey of Research in the Design and Control of Automated Guided Vehicle Systems**<br>I. F. A. Vis | European Journal of Operational Research | [link](https://doi.org/10.1016/j.ejor.2004.09.020) | Classic OR survey: guide-path design, fleet sizing, dispatching, routing. |
| 2020 | **Automated Guided Vehicle Systems, State-of-the-Art Control Algorithms and Techniques**<br>M. De Ryck, M. Versteyhe, F. Debrouwere | Journal of Manufacturing Systems 54 | [link](https://doi.org/10.1016/j.jmsy.2019.12.002) | AGV control algorithms; central vs decentral control trend. |
| 2021 | **Planning and Control of Autonomous Mobile Robots for Intralogistics: Literature Review and Research Agenda**<br>G. Fragapane, R. de Koster, F. Sgarbossa, J. O. Strandhagen | European Journal of Operational Research 294(2) | [link](https://doi.org/10.1016/j.ejor.2021.01.019) | AMR planning/control framework; decentralization vs AGV central control. |
| 2022 | **Motion Planning and Control for Mobile Robot Navigation Using Machine Learning: a Survey**<br>X. Xiao, B. Liu, G. Warnell, P. Stone | Autonomous Robots | [PDF](papers/00-surveys/xiao2022survey.pdf) · [PDF ↗](https://arxiv.org/pdf/2011.13112) · [arXiv](https://arxiv.org/abs/2011.13112) | How learning relates to the classical navigation stack; common challenges. |

<a id="01-localization-mapping"></a>
## Localization and mapping

Beacon/reflector EKF localization, Monte Carlo localization, lidar and visual SLAM, odometry calibration.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1991 | **Mobile Robot Localization by Tracking Geometric Beacons**<br>J. J. Leonard, H. F. Durrant-Whyte | IEEE Transactions on Robotics and Automation | [link](https://doi.org/10.1109/70.88147) | EKF localization against known beacons: the model behind reflector navigation. |
| 1996 | **Measurement and Correction of Systematic Odometry Errors in Mobile Robots**<br>J. Borenstein, L. Feng | IEEE Transactions on Robotics and Automation | [link](https://doi.org/10.1109/70.544770) | UMBmark odometry calibration. |
| 1999 | **Monte Carlo Localization for Mobile Robots**<br>F. Dellaert, D. Fox, W. Burgard, S. Thrun | ICRA | [link](https://doi.org/10.1109/robot.1999.772544) | Particle-filter localization; basis of AMCL. |
| 2003 | **Adapting the Sample Size in Particle Filters Through KLD-Sampling**<br>D. Fox | IJRR 22(12) | [link](https://doi.org/10.1177/0278364903022012001) | Adaptive particle count used by AMCL. |
| 2007 | **Improved Techniques for Grid Mapping with Rao-Blackwellized Particle Filters**<br>G. Grisetti, C. Stachniss, W. Burgard | IEEE Transactions on Robotics | [link](https://doi.org/10.1109/tro.2006.889486) | GMapping lidar SLAM. |
| 2016 | **Real-Time Loop Closure in 2D LIDAR SLAM (Cartographer)**<br>W. Hess, D. Kohler, H. Rapp, D. Andor | ICRA | [link](https://doi.org/10.1109/icra.2016.7487258) | Submap + branch-and-bound loop closure; widely used on AMRs. |
| 2017 | **ORB-SLAM2: an Open-Source SLAM System for Monocular, Stereo and RGB-D Cameras**<br>R. Mur-Artal, J. D. Tardos | IEEE Transactions on Robotics | [PDF ↗](https://arxiv.org/pdf/1610.06475) · [arXiv](https://arxiv.org/abs/1610.06475) | Feature-based visual SLAM. |

<a id="02-planning"></a>
## Path and motion planning

Graph search, kinematically feasible planning for car-like vehicles, sampling-based planning, benchmarks.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1968 | **A Formal Basis for the Heuristic Determination of Minimum Cost Paths (A*)**<br>P. E. Hart, N. J. Nilsson, B. Raphael | IEEE Transactions on Systems Science and Cybernetics | [link](https://doi.org/10.1109/tssc.1968.300136) | A* search. |
| 2010 | **Path Planning for Autonomous Vehicles in Unknown Semi-Structured Environments (Hybrid A*)**<br>D. Dolgov, S. Thrun, M. Montemerlo, J. Diebel | IJRR | [link](https://doi.org/10.1177/0278364909359210) | Kinematically feasible search for car-like vehicles; 50-300 ms replanning in the Urban Challenge. |
| 2011 | **Sampling-based Algorithms for Optimal Motion Planning (RRT*)**<br>S. Karaman, E. Frazzoli | IJRR | [PDF ↗](https://arxiv.org/pdf/1105.1186) · [arXiv](https://arxiv.org/abs/1105.1186) | Asymptotically optimal sampling-based planning. |
| 2020 | **Benchmarking Metric Ground Navigation (BARN)**<br>D. Perille, A. Truong, X. Xiao, P. Stone | SSRR | [PDF](papers/02-planning/perille2020barn.pdf) · [PDF ↗](https://arxiv.org/pdf/2008.13315) · [arXiv](https://arxiv.org/abs/2008.13315) | 300 navigation environments ranked by difficulty. |

<a id="03-tracking-and-local-control"></a>
## Path tracking and local obstacle avoidance

Tracking controllers, reactive and optimization-based local planners, sampling MPC, safety filters.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1983 | **Asymptotic Stability and Feedback Stabilization**<br>R. W. Brockett | Differential Geometric Control Theory (Birkhauser) | [link](https://doi.org/10.1007/springerreference_60687) | Why nonholonomic vehicles cannot be stabilized to a pose by smooth static feedback. |
| 1990 | **A Stable Tracking Control Method for an Autonomous Mobile Robot**<br>Y. Kanayama, Y. Kimura, F. Miyazaki, T. Noguchi | ICRA | [link](https://doi.org/10.1109/robot.1990.126006) | Lyapunov-based trajectory tracking for unicycle robots. |
| 1992 | **Implementation of the Pure Pursuit Path Tracking Algorithm**<br>R. C. Coulter | CMU-RI-TR-92-01 |  | Geometric path tracking used in many AGVs. Technical report; no stable public link verified. |
| 1997 | **The Dynamic Window Approach to Collision Avoidance**<br>D. Fox, W. Burgard, S. Thrun | IEEE Robotics & Automation Magazine | [link](https://doi.org/10.1109/100.580977) | Velocity-space local planner; basis of ROS DWB. |
| 2007 | **Autonomous Automobile Trajectory Tracking for Off-Road Driving (Stanley controller)**<br>G. M. Hoffmann, C. J. Tomlin, M. Montemerlo, S. Thrun | ACC | [link](https://doi.org/10.1109/acc.2007.4282788) | Front-axle cross-track steering law. |
| 2011 | **Reciprocal n-Body Collision Avoidance (ORCA)**<br>J. van den Berg, S. J. Guy, M. Lin, D. Manocha | Robotics Research (STAR) | [link](https://doi.org/10.1007/978-3-642-19457-3_1) | Velocity obstacles for many agents. |
| 2015 | **Model Predictive Path Integral Control using Covariance Variable Importance Sampling**<br>G. Williams, A. Aldrich, E. Theodorou | arXiv | [PDF ↗](https://arxiv.org/pdf/1509.01149) · [arXiv](https://arxiv.org/abs/1509.01149) | Sampling-based MPC (MPPI). |
| 2017 | **Integrated Online Trajectory Planning and Optimization in Distinctive Topologies (TEB)**<br>C. Rosmann, F. Hoffmann, T. Bertram | Robotics and Autonomous Systems | [link](https://doi.org/10.1016/j.robot.2016.11.007) | Timed elastic band local planner. |
| 2017 | **Information Theoretic Model Predictive Control: Theory and Applications to Autonomous Driving**<br>G. Williams et al. | arXiv / T-RO 2018 | [PDF](papers/03-tracking-and-local-control/williams2017itmpc.pdf) · [PDF ↗](https://arxiv.org/pdf/1707.02342) · [arXiv](https://arxiv.org/abs/1707.02342) | MPPI theory; aggressive driving; basis of Nav2's MPPI controller. |
| 2019 | **Control Barrier Functions: Theory and Applications**<br>A. D. Ames et al. | ECC | [link](https://doi.org/10.23919/ecc.2019.8796030) | Safety filters that can wrap any controller, including learned ones. |

<a id="04-fleet-management"></a>
## Fleet management and multi-robot coordination

Warehouse fleets, multi-agent path finding, traffic and task assignment.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2008 | **Coordinating Hundreds of Cooperative, Autonomous Vehicles in Warehouses**<br>P. R. Wurman, R. D'Andrea, M. Mountz | AI Magazine 29(1) | [link](https://ojs.aaai.org/index.php/aimagazine/article/view/2082) | Kiva goods-to-person system; productivity factor of two or more (authors' claim). |
| 2015 | **Conflict-Based Search for Optimal Multi-Agent Pathfinding**<br>G. Sharon, R. Stern, A. Felner, N. R. Sturtevant | Artificial Intelligence 219 | [link](https://doi.org/10.1016/j.artint.2014.11.006) | CBS: optimal MAPF by resolving conflicts in a constraint tree. |
| 2021 | **Lifelong Multi-Agent Path Finding in Large-Scale Warehouses (RHCR)**<br>J. Li, A. Tinka, S. Kiesel, J. W. Durham, T. K. S. Kumar, S. Koenig | AAAI | [PDF](papers/04-fleet-management/li2021lifelongmapf.pdf) · [PDF ↗](https://arxiv.org/pdf/2005.07371) · [arXiv](https://arxiv.org/abs/2005.07371) | Rolling-horizon collision resolution for up to 1,000 agents. |
| 2025 | **Amazon deploys its millionth robot and launches DeepFleet fleet foundation model (news)**<br>Robotics 24/7 | Industry news | [link](https://www.robotics247.com/article/amazon_launches_new_ai_foundation_model_to_power_its_robotic_fleet_deploys_millionth_robot/amazon_robotics) | Company-reported aim of 10% better fleet travel efficiency. |

<a id="05-learning-navigation"></a>
## Learning-based navigation

Reinforcement learning, imitation learning and navigation foundation models.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2016 | **End to End Learning for Self-Driving Cars**<br>M. Bojarski et al. | arXiv | [PDF ↗](https://arxiv.org/pdf/1604.07316) · [arXiv](https://arxiv.org/abs/1604.07316) | Behavior cloning from human driving: camera to steering. |
| 2017 | **Decentralized Non-communicating Multiagent Collision Avoidance with Deep Reinforcement Learning (CADRL)**<br>Y. F. Chen, M. Liu, M. Everett, J. P. How | ICRA | [PDF ↗](https://arxiv.org/pdf/1609.07845) · [arXiv](https://arxiv.org/abs/1609.07845) | More than 26% better path quality than ORCA in simulation. |
| 2017 | **Socially Aware Motion Planning with Deep Reinforcement Learning**<br>Y. F. Chen, M. Everett, M. Liu, J. P. How | IROS | [PDF ↗](https://arxiv.org/pdf/1703.08862) · [arXiv](https://arxiv.org/abs/1703.08862) | RL with social norms for crowd navigation. |
| 2017 | **From Perception to Decision: A Data-driven Approach to End-to-end Motion Planning for Autonomous Ground Robots**<br>M. Pfeiffer et al. | ICRA | [PDF ↗](https://arxiv.org/pdf/1609.07910) · [arXiv](https://arxiv.org/abs/1609.07910) | Imitating a classical planner from lidar. |
| 2017 | **Virtual-to-real Deep Reinforcement Learning: Continuous Control of Mobile Robots for Mapless Navigation**<br>L. Tai, G. Paolo, M. Liu | IROS | [PDF](papers/05-learning-navigation/tai2017virtual.pdf) · [PDF ↗](https://arxiv.org/pdf/1703.00420) · [arXiv](https://arxiv.org/abs/1703.00420) | Mapless RL planner from 10 range readings, transferred to a real robot. |
| 2017 | **Target-driven Visual Navigation in Indoor Scenes using Deep Reinforcement Learning**<br>Y. Zhu et al. | ICRA | [PDF ↗](https://arxiv.org/pdf/1609.05143) · [arXiv](https://arxiv.org/abs/1609.05143) | Goal-conditioned visual navigation. |
| 2018 | **Towards Optimally Decentralized Multi-Robot Collision Avoidance via Deep Reinforcement Learning**<br>P. Long et al. | ICRA | [PDF ↗](https://arxiv.org/pdf/1709.10082) · [arXiv](https://arxiv.org/abs/1709.10082) | Sensor-level multi-robot policy trained with PPO on many robots. |
| 2020 | **DD-PPO: Learning Near-Perfect PointGoal Navigators from 2.5 Billion Frames**<br>E. Wijmans et al. | ICLR | [PDF](papers/05-learning-navigation/wijmans2020ddppo.pdf) · [PDF ↗](https://arxiv.org/pdf/1911.00357) · [arXiv](https://arxiv.org/abs/1911.00357) | 2.5B steps in under 3 days on 64 GPUs; near-perfect PointGoal navigation in simulation. |
| 2021 | **BADGR: An Autonomous Self-Supervised Learning-Based Navigation System**<br>G. Kahn, P. Abbeel, S. Levine | RA-L | [PDF ↗](https://arxiv.org/pdf/2002.05700) · [arXiv](https://arxiv.org/abs/2002.05700) | Learns traversability from real-world experience without simulation. |
| 2023 | **GNM: A General Navigation Model to Drive Any Robot**<br>D. Shah et al. | ICRA | [PDF](papers/05-learning-navigation/shah2023gnm.pdf) · [PDF ↗](https://arxiv.org/pdf/2210.03370) · [arXiv](https://arxiv.org/abs/2210.03370) | 60 hours of data from 6 robots; cross-embodiment navigation. |
| 2023 | **ViNT: A Foundation Model for Visual Navigation**<br>D. Shah et al. | CoRL | [PDF ↗](https://arxiv.org/pdf/2306.14846) · [arXiv](https://arxiv.org/abs/2306.14846) | Transformer navigation foundation model; kilometer-scale navigation. |
| 2024 | **NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration**<br>A. Sridhar et al. | ICRA | [PDF ↗](https://arxiv.org/pdf/2310.07896) · [arXiv](https://arxiv.org/abs/2310.07896) | Diffusion policy for goal-reaching and exploration. |

<a id="06-systems-and-deployments"></a>
## Systems and deployments

Navigation stacks and field deployments that set the bar for real-world reliability.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1999 | **Experiences with an Interactive Museum Tour-Guide Robot (RHINO)**<br>W. Burgard et al. | Artificial Intelligence 114 | [link](https://doi.org/10.1016/s0004-3702(99)00070-3) | Six-day museum deployment among crowds, 1997. |
| 2010 | **Visual Teach and Repeat for Long-Range Rover Autonomy**<br>P. Furgale, T. D. Barfoot | Journal of Field Robotics 27(5) | [link](https://doi.org/10.1002/rob.20342) | 32+ km of route repeating, 99.6% autonomous, no GPS. |
| 2010 | **The Office Marathon: Robust Navigation in an Indoor Office Environment**<br>E. Marder-Eppstein et al. | ICRA | [link](https://doi.org/10.1109/robot.2010.5509725) | The ROS navigation stack on a PR2. |
| 2010 | **A Voice-Commandable Robotic Forklift Working Alongside Humans in Minimally-Prepared Outdoor Environments**<br>S. Teller et al. | ICRA | [PDF ↗](https://people.csail.mit.edu/jrg/2010/Teller-ICRA10.pdf) | Autonomous pallet handling with local sensing, near people. |
| 2020 | **The Marathon 2: A Navigation System (Nav2)**<br>S. Macenski, F. Martin, R. White, J. Gines Clavero | IROS | [PDF](papers/06-systems-and-deployments/macenski2020nav2.pdf) · [PDF ↗](https://arxiv.org/pdf/2003.00368) · [arXiv](https://arxiv.org/abs/2003.00368) | ROS 2 navigation with behavior trees; the open-source AMR baseline. |

<a id="07-standards"></a>
## Standards

Safety and interoperability standards that constrain industrial vehicle control.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2023 | **ISO 3691-4:2023 Industrial trucks - Safety requirements and verification - Part 4: Driverless industrial trucks and their systems**<br>ISO | ISO standard (2nd ed.) | [link](https://www.iso.org/standard/83545.html) | Covers AGVs, AMRs, tuggers; first edition 2020. |
| 2024 | **VDA 5050: Interface for the communication between automated guided vehicles (AGV) and a master control, v2.1.0**<br>VDA / VDMA | Industry standard | [PDF ↗](https://vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/VDA5050-V2p1p0.pdf) | Vendor-neutral MQTT interface for mixed fleets; v2.0.0 in Feb 2022. |
