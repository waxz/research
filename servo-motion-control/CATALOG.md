# Paper catalog

40 entries in 6 categories. **8** have a PDF available online (PDF ↗) and **8** also have a local copy in this repository (PDF).
Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.

| Category | Entries | PDF online | Local PDF |
|---|---:|---:|---:|
| [Surveys and tutorials](#00-surveys-tutorials) | 4 | 0 | 0 |
| [Field-oriented control and drives](#01-foc-drives) | 8 | 1 | 1 |
| [Single-axis servo loops](#02-servo-loops) | 4 | 1 | 1 |
| [High-precision motion control](#03-precision-motion) | 8 | 4 | 4 |
| [Multi-axis robot arm control](#04-robot-arms) | 14 | 2 | 2 |
| [Standards and documentation](#05-standards-docs) | 2 | 0 | 0 |

<a id="00-surveys-tutorials"></a>
## Surveys and tutorials

Overviews of precision motion control, learning control, lithography stages and robot collision handling.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2006 | **A Survey of Iterative Learning Control**<br>D. A. Bristow, M. Tharayil, A. G. Alleyne | IEEE Control Systems Magazine | [link](https://doi.org/10.1109/MCS.2006.1636313) | Design and analysis of ILC: learning and robustness filters, convergence. |
| 2011 | **Position Control in Lithographic Equipment**<br>H. Butler | IEEE Control Systems Magazine | [link](https://doi.org/10.1109/MCS.2011.941882) | How wafer and reticle stages reach nanometre precision: feedforward, MIMO control, learning. |
| 2017 | **Robot Collisions: A Survey on Detection, Isolation, and Identification**<br>S. Haddadin, A. De Luca, A. Albu-Schäffer | IEEE Transactions on Robotics | [link](https://doi.org/10.1109/TRO.2017.2723903) | Survey of robot collision detection, isolation, identification and reaction. |
| 2018 | **Advanced Motion Control for Precision Mechatronics: Control, Identification, and Learning of Complex Systems**<br>T. Oomen | IEEJ Journal of Industry Applications | [link](https://doi.org/10.1541/ieejjia.7.127) | Open-access overview of precision motion control: feedforward, identification and learning for complex mechatronics. |

<a id="01-foc-drives"></a>
## Field-oriented control and drives

The dq transform, interior-magnet motors, field weakening, PWM, dead time, sensorless and predictive current control.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1929 | **Two-Reaction Theory of Synchronous Machines: Generalized Method of Analysis, Part I**<br>R. H. Park | Transactions of the American Institute of Electrical Engineers | [link](https://doi.org/10.1109/T-AIEE.1929.5055275) | The dq transform at the heart of field-oriented control. |
| 1986 | **Interior Permanent-Magnet Synchronous Motors for Adjustable-Speed Drives**<br>T. M. Jahns, G. B. Kliman, T. W. Neumann | IEEE Transactions on Industry Applications | [link](https://doi.org/10.1109/TIA.1986.4504786) | Interior permanent-magnet motors: reluctance torque, MTPA and wide speed range. |
| 1986 | **A New Quick-Response and High-Efficiency Control Strategy of an Induction Motor**<br>I. Takahashi, T. Noguchi | IEEE Transactions on Industry Applications | [link](https://doi.org/10.1109/TIA.1986.4504799) | Direct torque control, the main alternative to FOC. |
| 1988 | **Analysis and Realization of a Pulsewidth Modulator Based on Voltage Space Vectors**<br>H. W. van der Broeck, H.-C. Skudelny, G. V. Stanke | IEEE Transactions on Industry Applications | [link](https://doi.org/10.1109/28.87265) | Space-vector PWM: 15% more usable voltage than sine PWM. |
| 1990 | **Expansion of Operating Limits for Permanent Magnet Motor by Current Vector Control Considering Inverter Capacity**<br>S. Morimoto, Y. Takeda, T. Hirasa, K. Taniguchi | IEEE Transactions on Industry Applications | [link](https://doi.org/10.1109/28.60058) | Current-vector control for field weakening within inverter voltage and current limits. |
| 1994 | **Inverter Output Voltage Synthesis Using Novel Dead Time Compensation**<br>J.-W. Choi, S.-I. Yong, S.-K. Sul | IEEE APEC | [link](https://doi.org/10.1109/APEC.1994.316413) | Dead-time compensation for accurate low-voltage synthesis. |
| 1996 | **Sensorless PM Brushless DC Motor Drives**<br>N. Matsui | IEEE Transactions on Industrial Electronics | [link](https://doi.org/10.1109/41.491354) | Back-EMF based position estimation and its limits. |
| 2019 | **Data-Driven Recursive Least Squares Estimation for Model Predictive Current Control of Permanent Magnet Synchronous Motors**<br>A. Brosch, S. Hanke, O. Wallscheid, J. Böcker | arXiv | [PDF](papers/01-foc-drives/brosch2019mpccurrent.pdf) · [PDF ↗](https://arxiv.org/pdf/1911.12065) · [arXiv](https://arxiv.org/abs/1911.12065) | Model predictive current control of PMSMs with recursive least-squares model correction. |

<a id="02-servo-loops"></a>
## Single-axis servo loops

Disturbance observers, feedforward, shaped commands and automatic cascade tuning.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1990 | **Preshaping Command Inputs to Reduce System Vibration**<br>N. C. Singer, W. P. Seering | Journal of Dynamic Systems, Measurement, and Control | [link](https://doi.org/10.1115/1.2894142) | Input shaping: commands that cancel their own vibration. |
| 1996 | **Motion Control for Advanced Mechatronics**<br>K. Ohnishi, M. Shibata, T. Murakami | IEEE/ASME Transactions on Mechatronics | [link](https://doi.org/10.1109/3516.491410) | Disturbance observers for robust motion control. |
| 1999 | **Disturbance Observer and Feedforward Design for a High-Speed Direct-Drive Positioning Table**<br>C. J. Kempf, S. Kobayashi | IEEE Transactions on Control Systems Technology | [link](https://doi.org/10.1109/87.784416) | DOB and feedforward for a direct-drive positioning table. |
| 2020 | **Performance-Driven Cascade Controller Tuning with Bayesian Optimization**<br>M. Khosravi, V. Behrunani, P. Myszkorowski, R. S. Smith, A. Rupenyan, J. Lygeros | arXiv | [PDF](papers/02-servo-loops/khosravi2020bocascade.pdf) · [PDF ↗](https://arxiv.org/pdf/2007.12536) · [arXiv](https://arxiv.org/abs/2007.12536) | Bayesian optimization tunes a linear-axis cascade (position and speed loops) jointly on hardware. |

<a id="03-precision-motion"></a>
## High-precision motion control

ZPETC, iterative and repetitive learning control, cross-coupled contouring and learned feedforward.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1980 | **Cross-Coupled Biaxial Computer Control for Manufacturing Systems**<br>Y. Koren | Journal of Dynamic Systems, Measurement, and Control | [link](https://doi.org/10.1115/1.3149612) | Cross-coupled control of contour error in multi-axis machines. |
| 1984 | **Bettering Operation of Robots by Learning**<br>S. Arimoto, S. Kawamura, F. Miyazaki | Journal of Robotic Systems | [link](https://doi.org/10.1002/rob.4620010203) | Origin of iterative learning control for repeated robot motion. |
| 1987 | **Zero Phase Error Tracking Algorithm for Digital Control**<br>M. Tomizuka | Journal of Dynamic Systems, Measurement, and Control | [link](https://doi.org/10.1115/1.3143822) | ZPETC: feedforward through non-minimum-phase zeros. |
| 1988 | **Repetitive Control System: A New Type Servo System for Periodic Exogenous Signals**<br>S. Hara, Y. Yamamoto, T. Omata, M. Nakano | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/9.1274) | Repetitive control for periodic disturbances. |
| 2019 | **Neural Network Augmented Physics Models for Systems with Partially Unknown Dynamics: Application to Slider-Crank Mechanism**<br>W. De Groote, E. Kikken, E. Hostens, S. Van Hoecke, G. Crevecoeur | arXiv | [PDF](papers/03-precision-motion/degroote2019nnap.pdf) · [PDF ↗](https://arxiv.org/pdf/1910.12212) · [arXiv](https://arxiv.org/abs/1910.12212) | Neural-network-augmented physics models for servo systems with partly unknown dynamics. |
| 2022 | **Physics-Guided Neural Networks for Feedforward Control: An Orthogonal Projection-Based Approach**<br>J. Kon, D. Bruijnen, J. van de Wijdeven, M. Heertjes, T. Oomen | arXiv | [PDF](papers/03-precision-motion/kon2022pgnn.pdf) · [PDF ↗](https://arxiv.org/pdf/2201.03308) · [arXiv](https://arxiv.org/abs/2201.03308) | Physics-guided neural feedforward with orthogonal projection for identifiable physical parameters. |
| 2023 | **Physics-guided neural networks for feedforward control with input-to-state stability guarantees**<br>M. Bolderman, H. Butler, S. Koekebakker, E. van Horssen, R. Kamidi et al. | Control Engineering Practice | [PDF](papers/03-precision-motion/bolderman2023pgnn.pdf) · [PDF ↗](https://arxiv.org/pdf/2301.08568) · [arXiv](https://arxiv.org/abs/2301.08568) | Physics-guided neural feedforward with input-to-state stability guarantees for precision mechatronics. |
| 2026 | **Optimal shaping filter design for data-driven feedforward controller tuning**<br>Y. Fujimoto | arXiv | [PDF](papers/03-precision-motion/fujimoto2026shaping.pdf) · [PDF ↗](https://arxiv.org/pdf/2607.29480) · [arXiv](https://arxiv.org/abs/2607.29480) | Optimal shaping filter for data-driven feedforward tuning in two-degree-of-freedom control. |

<a id="04-robot-arms"></a>
## Multi-axis robot arm control

Robot dynamics, gravity compensation, adaptive control, flexible joints, identification, impedance, collision detection and time-optimal paths.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1980 | **On-Line Computational Scheme for Mechanical Manipulators**<br>J. Y. S. Luh, M. W. Walker, R. P. C. Paul | Journal of Dynamic Systems, Measurement, and Control | [link](https://doi.org/10.1115/1.3149599) | Recursive Newton-Euler: inverse dynamics in O(n) for computed torque. |
| 1981 | **Hybrid Position/Force Control of Manipulators**<br>M. H. Raibert, J. J. Craig | Journal of Dynamic Systems, Measurement, and Control | [link](https://doi.org/10.1115/1.3139652) | Hybrid position/force control. |
| 1981 | **A New Feedback Method for Dynamic Control of Manipulators**<br>M. Takegaki, S. Arimoto | Journal of Dynamic Systems, Measurement, and Control | [link](https://doi.org/10.1115/1.3139651) | PD with gravity compensation is globally stable for robot arms. |
| 1985 | **Time-Optimal Control of Robotic Manipulators Along Specified Paths**<br>J. E. Bobrow, S. Dubowsky, J. S. Gibson | The International Journal of Robotics Research | [link](https://doi.org/10.1177/027836498500400301) | Time-optimal motion along a specified path under torque limits. |
| 1985 | **Impedance Control: An Approach to Manipulation, Part I: Theory**<br>N. Hogan | Journal of Dynamic Systems, Measurement, and Control | [link](https://doi.org/10.1115/1.3140702) | Impedance control for manipulation in contact. |
| 1987 | **Adaptive Control of Mechanical Manipulators**<br>J. J. Craig, P. Hsu, S. S. Sastry | The International Journal of Robotics Research | [link](https://doi.org/10.1177/027836498700600202) | Adaptive computed-torque control of manipulators. |
| 1987 | **On the Adaptive Control of Robot Manipulators**<br>J.-J. E. Slotine, W. Li | The International Journal of Robotics Research | [link](https://doi.org/10.1177/027836498700600303) | Slotine-Li adaptive controller: passivity-based adaptation without acceleration measurement. |
| 1987 | **Modeling and Control of Elastic Joint Robots**<br>M. W. Spong | Journal of Dynamic Systems, Measurement, and Control | [link](https://doi.org/10.1115/1.3143860) | Flexible-joint robot model and control (harmonic drives). |
| 1990 | **Direct Calculation of Minimum Set of Inertial Parameters of Serial Robots**<br>M. Gautier, W. Khalil | IEEE Transactions on Robotics and Automation | [link](https://doi.org/10.1109/70.56655) | Base inertial parameters: robot dynamics linear in identifiable parameters. |
| 1997 | **Optimal Robot Excitation and Identification**<br>J. Swevers, C. Ganseman, D. Tukel, J. de Schutter, H. Van Brussel | IEEE Transactions on Robotics and Automation | [link](https://doi.org/10.1109/70.631234) | Optimal excitation trajectories (Fourier series) for robot identification. |
| 2006 | **Collision Detection and Safe Reaction with the DLR-III Lightweight Manipulator Arm**<br>A. De Luca, A. Albu-Schäffer, S. Haddadin, G. Hirzinger | IEEE/RSJ IROS | [link](https://doi.org/10.1109/IROS.2006.282053) | Momentum-observer collision detection and safe reaction on the DLR-III arm. |
| 2007 | **The DLR Lightweight Robot: Design and Control Concepts for Robots in Human Environments**<br>A. Albu-Schäffer, S. Haddadin, Ch. Ott, A. Stemmer, T. Wimböck, G. Hirzinger | Industrial Robot: An International Journal | [link](https://doi.org/10.1108/01439910710774386) | Torque-controlled lightweight robot design and control (basis of the KUKA LBR). |
| 2018 | **A New Approach to Time-Optimal Path Parameterization Based on Reachability Analysis**<br>H. Pham, Q.-C. Pham | IEEE Transactions on Robotics | [PDF](papers/04-robot-arms/pham2018toppra.pdf) · [PDF ↗](https://arxiv.org/pdf/1707.07239) · [arXiv](https://arxiv.org/abs/1707.07239) · [link](https://doi.org/10.1109/TRO.2018.2819195) | TOPP-RA: fast, robust time-optimal path parameterization by reachability analysis. |
| 2019 | **Industrial Robot Trajectory Tracking Using Multi-Layer Neural Networks Trained by Iterative Learning Control**<br>S. Chen, J. T. Wen | arXiv | [PDF](papers/04-robot-arms/chen2019robotilc.pdf) · [PDF ↗](https://arxiv.org/pdf/1903.00082) · [arXiv](https://arxiv.org/abs/1903.00082) | Industrial-robot trajectory tracking with neural networks trained by ILC through the vendor controller. |

<a id="05-standards-docs"></a>
## Standards and documentation

Drive profiles and motion-control programming standards.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2026 | **CiA 402: CANopen device profile for drives and motion control**<br>CAN in Automation | Specification (organization page) | [link](https://www.can-cia.org/) | Drive state machine and cyclic synchronous position, velocity and torque modes; also used over EtherCAT (CoE). |
| 2026 | **PLCopen Motion Control: function blocks for IEC 61131-3**<br>PLCopen | Specification (organization page) | [link](https://plcopen.org/) | Standard motion blocks (MC_MoveAbsolute and others) and jerk-limited profiles for PLC-based motion control. |
