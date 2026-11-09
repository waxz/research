# Paper catalog

55 entries in 7 categories. **10** have a PDF available online (PDF ↗) and **9** also have a local copy in this repository (PDF).
Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.

| Category | Entries | PDF online | Local PDF |
|---|---:|---:|---:|
| [Free books, courses and documentation](#00-books-courses-docs) | 9 | 0 | 0 |
| [Physics and signal foundations](#01-physics-foundations) | 4 | 0 | 0 |
| [Mechanics, transmissions and actuators](#02-mechanics-actuators) | 13 | 5 | 5 |
| [Electrical drives, power electronics and sensing](#03-electrical-drives) | 5 | 0 | 0 |
| [Embedded real-time control and communication](#04-embedded-realtime) | 9 | 4 | 4 |
| [Software engineering for control systems](#05-software-engineering) | 8 | 1 | 0 |
| [Functional safety and standards](#06-safety-standards) | 7 | 0 | 0 |

<a id="00-books-courses-docs"></a>
## Free books, courses and documentation

Open textbooks, university courses and the documentation of the software and bus standards used in control systems.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2007 | **6.334 Power Electronics (Spring 2007)**<br>D. J. Perreault | MIT OpenCourseWare | [link](https://ocw.mit.edu/courses/6-334-power-electronics-spring-2007/) | Free course on converters, PWM and switching. |
| 2008 | **Feedback Systems: An Introduction for Scientists and Engineers**<br>K. J. Åström, R. M. Murray | Princeton University Press (free online) | [link](https://fbswiki.org/) | Loop design, margins and sampling basics. |
| 2013 | **6.685 Electric Machines (Fall 2013)**<br>J. L. Kirtley Jr. | MIT OpenCourseWare | [link](https://ocw.mit.edu/courses/6-685-electric-machines-fall-2013/) | Free course on motor physics and dq models. |
| 2017 | **Modern Robotics: Mechanics, Planning, and Control**<br>K. M. Lynch, F. C. Park | Cambridge University Press (free online) | [link](https://modernrobotics.northwestern.edu/) | Rigid-body dynamics, actuation and transmissions, with videos. |
| 2026 | **CAN in Automation (CiA): CAN FD, CANopen and the CiA 402 drive profile**<br>CAN in Automation | Organization | [link](https://www.can-cia.org/) | Specifications for CAN-based drive communication and state machines. |
| 2026 | **FreeRTOS**<br>FreeRTOS project | Documentation | [link](https://www.freertos.org/) | Small real-time kernel for microcontrollers. |
| 2026 | **ros2_control documentation**<br>ros2_control maintainers | Documentation | [link](https://control.ros.org/) | Hardware interfaces, controller manager and real-time loop for ROS 2. |
| 2026 | **ROS 2 documentation**<br>Open Robotics and contributors | Documentation | [link](https://docs.ros.org/en/rolling/) | Nodes, executors, DDS quality of service, real-time guidance. |
| 2026 | **Zephyr Project**<br>Linux Foundation Zephyr Project | Documentation | [link](https://www.zephyrproject.org/) | Real-time operating system for embedded devices. |

<a id="01-physics-foundations"></a>
## Physics and signal foundations

Electromagnetism, the dq transform and the sampling theorem.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1865 | **A Dynamical Theory of the Electromagnetic Field**<br>J. C. Maxwell | Philosophical Transactions of the Royal Society of London | [link](https://doi.org/10.1098/rstl.1865.0008) | Maxwell's equations: the physics behind motors, generators and EMC. |
| 1928 | **Certain Topics in Telegraph Transmission Theory**<br>H. Nyquist | Transactions of the American Institute of Electrical Engineers | [link](https://doi.org/10.1109/T-AIEE.1928.5055024) | Sampling and bandwidth limits that later became the sampling theorem. |
| 1929 | **Two-Reaction Theory of Synchronous Machines: Generalized Method of Analysis, Part I**<br>R. H. Park | Transactions of the American Institute of Electrical Engineers | [link](https://doi.org/10.1109/T-AIEE.1929.5055275) | The dq transform that turns AC machines into DC-like systems. |
| 1949 | **Communication in the Presence of Noise**<br>C. E. Shannon | Proceedings of the IRE | [link](https://doi.org/10.1109/JRPROC.1949.232969) | Sampling theorem and channel capacity. |

<a id="02-mechanics-actuators"></a>
## Mechanics, transmissions and actuators

Friction, backlash, series elastic and quasi-direct-drive actuators for robots.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1994 | **A Survey of Models, Analysis Tools and Compensation Methods for the Control of Machines with Friction**<br>B. Armstrong-Hélouvry, P. Dupont, C. Canudas de Wit | Automatica | [link](https://doi.org/10.1016/0005-1098(94)90209-7) | Survey of friction models, analysis tools and compensation. |
| 1995 | **A New Model for Control of Systems with Friction**<br>C. Canudas de Wit, H. Olsson, K. J. Åström, P. Lischinsky | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/9.376053) | LuGre dynamic friction model. |
| 1995 | **Series Elastic Actuators**<br>G. A. Pratt, M. M. Williamson | IEEE/RSJ IROS | [link](https://doi.org/10.1109/IROS.1995.525827) | Series elastic actuators: a spring for force control and shock tolerance. |
| 2002 | **Controlling Mechanical Systems with Backlash: A Survey**<br>M. Nordin, P.-O. Gutman | Automatica | [link](https://doi.org/10.1016/S0005-1098(02)00047-X) | Survey of backlash models and compensation. |
| 2015 | **Design Principles for Energy-Efficient Legged Locomotion and Implementation on the MIT Cheetah Robot**<br>S. Seok, A. Wang, M. Y. Chuah, D. J. Hyun, J. Lee et al. | IEEE/ASME Transactions on Mechatronics | [link](https://doi.org/10.1109/TMECH.2014.2339013) | Energy-efficient legged locomotion and the MIT Cheetah's actuator design. |
| 2016 | **Design Principles for a Family of Direct-Drive Legged Robots**<br>G. Kenneally, A. De, D. E. Koditschek | IEEE Robotics and Automation Letters | [link](https://doi.org/10.1109/LRA.2016.2528294) | Direct-drive legged robots: transparency over torque density. |
| 2017 | **Proprioceptive Actuator Design in the MIT Cheetah: Impact Mitigation and High-Bandwidth Physical Interaction for Dynamic Legged Robots**<br>P. M. Wensing, A. Wang, S. Seok, D. Otten, J. Lang, S. Kim | IEEE Transactions on Robotics | [link](https://doi.org/10.1109/TRO.2016.2640183) | Proprioceptive actuators: low gear ratio for impact mitigation and force control. |
| 2019 | **Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation**<br>D. V. Gealy, S. McKinley, B. Yi, P. Wu, P. R. Downey et al. | ICRA | [PDF](papers/02-mechanics-actuators/gealy2019blue.pdf) · [PDF ↗](https://arxiv.org/pdf/1904.03815) · [arXiv](https://arxiv.org/abs/1904.03815) | Quasi-direct-drive 7-DoF arm for low-cost force-controlled manipulation. |
| 2019 | **Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control**<br>B. Katz, J. Di Carlo, S. Kim | ICRA | [link](https://doi.org/10.1109/ICRA.2019.8793865) | Low-cost quasi-direct-drive quadruped platform. |
| 2019 | **Stanford Doggo: An Open-Source, Quasi-Direct-Drive Quadruped**<br>N. Kau, A. Schultz, N. Ferrante, P. Slade | ICRA | [PDF](papers/02-mechanics-actuators/kau2019doggo.pdf) · [PDF ↗](https://arxiv.org/pdf/1905.04254) · [arXiv](https://arxiv.org/abs/1905.04254) | Open-source quasi-direct-drive quadruped for under $3000. |
| 2020 | **An Open Torque-Controlled Modular Robot Architecture for Legged Locomotion Research**<br>F. Grimminger, A. Meduri, M. Khadiv, J. Viereck, M. Wüthrich et al. | IEEE Robotics and Automation Letters | [PDF](papers/02-mechanics-actuators/grimminger2020odri.pdf) · [PDF ↗](https://arxiv.org/pdf/1910.00093) · [arXiv](https://arxiv.org/abs/1910.00093) · [link](https://doi.org/10.1109/LRA.2020.2976639) | Open torque-controlled actuator modules and electronics for legged robots (ODRI). |
| 2022 | **Alternative Metrics to Select Motors for Quasi-Direct Drive Actuators**<br>K. Urs, C. E. Adu, E. J. Rouse, T. Y. Moore | arXiv | [PDF](papers/02-mechanics-actuators/urs2022motor.pdf) · [PDF ↗](https://arxiv.org/pdf/2202.12365) · [arXiv](https://arxiv.org/abs/2202.12365) | Motor-selection metrics for quasi-direct-drive actuators, invariant to gear ratio. |
| 2024 | **Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque Estimation for Legged Robotics**<br>A. Zhu, Y. Tanaka, F. Rafeedi, D. Hong | arXiv | [PDF](papers/02-mechanics-actuators/zhu2024cycloidal.pdf) · [PDF ↗](https://arxiv.org/pdf/2410.16591) · [arXiv](https://arxiv.org/abs/2410.16591) | Cycloidal quasi-direct-drive actuators with actuator-network torque estimation. |

<a id="03-electrical-drives"></a>
## Electrical drives, power electronics and sensing

PWM, space vectors, direct torque control, motion control and velocity estimation.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1986 | **A New Quick-Response and High-Efficiency Control Strategy of an Induction Motor**<br>I. Takahashi, T. Noguchi | IEEE Transactions on Industry Applications | [link](https://doi.org/10.1109/TIA.1986.4504799) | Direct torque control of induction motors. |
| 1988 | **Analysis and Realization of a Pulsewidth Modulator Based on Voltage Space Vectors**<br>H. W. van der Broeck, H.-C. Skudelny, G. V. Stanke | IEEE Transactions on Industry Applications | [link](https://doi.org/10.1109/28.87265) | Space-vector pulse-width modulation. |
| 1992 | **Analysis of Algorithms for Velocity Estimation from Discrete Position versus Time Data**<br>R. Brown, S. Schneider, M. Mulligan | IEEE Transactions on Industrial Electronics | [link](https://doi.org/10.1109/41.121906) | Comparison of velocity estimation from encoder data. |
| 1992 | **Pulsewidth Modulation: A Survey**<br>J. Holtz | IEEE Transactions on Industrial Electronics | [link](https://doi.org/10.1109/41.161472) | Survey of pulse-width modulation methods. |
| 1996 | **Motion Control for Advanced Mechatronics**<br>K. Ohnishi, M. Shibata, T. Murakami | IEEE/ASME Transactions on Mechatronics | [link](https://doi.org/10.1109/3516.491410) | Disturbance observers for robust motion control. |

<a id="04-embedded-realtime"></a>
## Embedded real-time control and communication

Scheduling, control timing, anti-windup, CAN, EtherCAT, real-time ROS 2 and embedded optimization.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1973 | **Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment**<br>C. L. Liu, J. W. Layland | Journal of the ACM | [link](https://doi.org/10.1145/321738.321743) | Rate-monotonic scheduling and its utilization bound. |
| 1989 | **Integrator Windup and How to Avoid It**<br>K. J. Åström, L. Rundqwist | 1989 American Control Conference | [link](https://doi.org/10.23919/ACC.1989.4790464) | Integrator windup and anti-windup schemes. |
| 2003 | **How Does Control Timing Affect Performance? Analysis and Simulation of Timing Using Jitterbug and TrueTime**<br>A. Cervin, D. Henriksson, B. Lincoln, J. Eker, K.-E. Årzén | IEEE Control Systems Magazine | [link](https://doi.org/10.1109/MCS.2003.1200240) | How delay and jitter degrade control, with analysis tools. |
| 2004 | **Real-Time Ethernet: The EtherCAT Solution**<br>D. Jansen, H. Büttner | Computing and Control Engineering | [link](https://doi.org/10.1049/cce:20040104) | EtherCAT: on-the-fly processing and distributed clocks. |
| 2007 | **Controller Area Network (CAN) Schedulability Analysis: Refuted, Revisited and Revised**<br>R. I. Davis, A. Burns, R. J. Bril, J. J. Lukkien | Real-Time Systems | [link](https://doi.org/10.1007/s11241-007-9012-7) | Correct worst-case response-time analysis for CAN. |
| 2020 | **OpEn: Code Generation for Embedded Nonconvex Optimization**<br>P. Sopasakis, E. Fresk, P. Patrinos | arXiv | [PDF](papers/04-embedded-realtime/sopasakis2020open.pdf) · [PDF ↗](https://arxiv.org/pdf/2003.00292) · [arXiv](https://arxiv.org/abs/2003.00292) | OpEn: Rust code generation for embedded nonconvex optimization. |
| 2021 | **Budget-based real-time Executor for Micro-ROS**<br>J. Staschulat, R. Lange, D. N. Dasari | arXiv | [PDF](papers/04-embedded-realtime/staschulat2021microros.pdf) · [PDF ↗](https://arxiv.org/pdf/2105.05590) · [arXiv](https://arxiv.org/abs/2105.05590) | Budget-based real-time executor for micro-ROS on microcontrollers. |
| 2024 | **Bridging the Gap between ROS~2 and Classical Real-Time Scheduling for Periodic Tasks**<br>H. Teper, O. Bell, M. Günzel, C. Gill, J.-J. Chen | arXiv | [PDF](papers/04-embedded-realtime/teper2024ros2.pdf) · [PDF ↗](https://arxiv.org/pdf/2408.03696) · [arXiv](https://arxiv.org/abs/2408.03696) | Classical real-time scheduling theory applied to ROS 2 via the events executor. |
| 2025 | **A Survey of Real-Time Support, Analysis, and Advancements in ROS 2**<br>D. Casini, J.-J. Chen, J. Li, F. Reghenzani, H. Teper | arXiv | [PDF](papers/04-embedded-realtime/casini2025ros2survey.pdf) · [PDF ↗](https://arxiv.org/pdf/2601.10722) · [arXiv](https://arxiv.org/abs/2601.10722) | Survey of real-time support, analysis and advances in ROS 2. |

<a id="05-software-engineering"></a>
## Software engineering for control systems

Modularity, statecharts, safety-critical coding, cyber-physical design, HIL testing, ROS and ros_control.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1972 | **On the Criteria to Be Used in Decomposing Systems into Modules**<br>D. L. Parnas | Communications of the ACM | [link](https://doi.org/10.1145/361598.361623) | Information hiding: the basis of layered, replaceable software modules. |
| 1987 | **No Silver Bullet: Essence and Accidents of Software Engineering**<br>F. P. Brooks | Computer | [link](https://doi.org/10.1109/MC.1987.1663532) | Essential versus accidental complexity in software. |
| 1987 | **Statecharts: A Visual Formalism for Complex Systems**<br>D. Harel | Science of Computer Programming | [link](https://doi.org/10.1016/0167-6423(87)90035-9) | Statecharts: hierarchical state machines for reactive systems. |
| 2005 | **On Hardware-in-the-Loop Simulation**<br>M. Bacic | IEEE CDC | [link](https://doi.org/10.1109/CDC.2005.1582653) | Hardware-in-the-loop simulation for control. |
| 2006 | **The Power of 10: Rules for Developing Safety-Critical Code**<br>G. J. Holzmann | Computer | [link](https://doi.org/10.1109/MC.2006.212) | Ten rules for analysable safety-critical code. |
| 2008 | **Cyber Physical Systems: Design Challenges**<br>E. A. Lee | 2008 11th IEEE International Symposium on Object and Component-Oriented Real-Time Distributed Computing (ISORC) | [link](https://doi.org/10.1109/ISORC.2008.25) | Cyber-physical systems: timing and physics as first-class design concerns. |
| 2017 | **ros_control: A Generic and Simple Control Framework for ROS**<br>S. Chitta, E. Marder-Eppstein, W. Meeussen, V. Pradeep, A. R. Tsouroukdissian et al. | The Journal of Open Source Software | [link](https://doi.org/10.21105/joss.00456) | ros_control: hardware abstraction and controller management for ROS. |
| 2022 | **Robot Operating System 2: Design, architecture, and uses in the wild**<br>S. Macenski, T. Foote, B. Gerkey, C. Lalancette, W. Woodall | Science Robotics | [PDF ↗](https://arxiv.org/pdf/2211.07752) · [arXiv](https://arxiv.org/abs/2211.07752) · [link](https://doi.org/10.1126/scirobotics.abm6074) | ROS 2 design, architecture and production use. Linked, not stored (17 MB). |

<a id="06-safety-standards"></a>
## Functional safety and standards

Accident analyses, systems safety and the main functional-safety and PLC standards.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1993 | **An Investigation of the Therac-25 Accidents**<br>N. G. Leveson, C. S. Turner | Computer | [link](https://doi.org/10.1109/MC.1993.274940) | Therac-25 overdoses: software race conditions after hardware interlocks were removed. |
| 2004 | **A New Accident Model for Engineering Safer Systems**<br>N. Leveson | Safety Science | [link](https://doi.org/10.1016/S0925-7535(03)00047-X) | STAMP: accidents as failures of control, not only of components. |
| 2010 | **IEC 61508-1:2010 Functional safety of electrical/electronic/programmable electronic safety-related systems, Part 1**<br>IEC | International standard | [link](https://webstore.iec.ch/en/publication/5515) | SIL 1–4 and the safety life cycle. |
| 2018 | **ISO 26262-1:2018 Road vehicles: Functional safety, Part 1**<br>ISO | International standard | [link](https://www.iso.org/standard/68383.html) | ASIL A–D and the automotive safety life cycle. |
| 2023 | **ISO 13849-1:2023 Safety of machinery: Safety-related parts of control systems, Part 1**<br>ISO | International standard | [link](https://www.iso.org/standard/73481.html) | Performance levels a–e, categories, MTTFd, DC and common-cause failures. |
| 2025 | **IEC 61131-3:2025 Programmable controllers, Part 3: Programming languages**<br>IEC | International standard | [link](https://webstore.iec.ch/en/publication/68533) | PLC languages, 4th edition. |
| 2026 | **MISRA C and MISRA C++ guidelines**<br>MISRA | Coding standard | [link](https://misra.org.uk/) | Safe subsets of C and C++ for embedded and safety-related code. |
