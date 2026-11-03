# Paper catalog

72 entries in 9 categories. **59** have a PDF available online (PDF ↗) and **19** also have a local copy in this repository (PDF).
Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.

| Category | Entries | PDF online | Local PDF |
|---|---:|---:|---:|
| [Surveys and reviews](#00-surveys) | 7 | 5 | 3 |
| [The reality gap: foundations and measurement](#01-reality-gap) | 3 | 1 | 1 |
| [Domain randomization and adaptive randomization](#02-domain-randomization) | 11 | 11 | 3 |
| [System identification and actuator modelling](#03-sysid-actuators) | 15 | 13 | 5 |
| [Adaptation and robust policies](#04-adaptation-robustness) | 6 | 6 | 1 |
| [Contact models and simulators](#05-contact-simulators) | 16 | 10 | 3 |
| [Landmark sim-to-real results](#06-achievements) | 9 | 8 | 0 |
| [Real-to-sim, photorealistic and generative simulation](#07-real2sim-generative) | 4 | 4 | 3 |
| [Real-robot datasets for modelling and benchmarking](#08-datasets-benchmarks) | 1 | 1 | 0 |

<a id="00-surveys"></a>
## Surveys and reviews

Overviews of sim-to-real transfer, randomized simulation and the reality gap.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2020 | **The frontier of simulation-based inference**<br>K. Cranmer, J. Brehmer, G. Louppe | PNAS | [PDF ↗](https://arxiv.org/pdf/1911.01429) · [arXiv](https://arxiv.org/abs/1911.01429) | Review of likelihood-free inference: the toolbox behind BayesSim and neural posterior calibration. |
| 2020 | **Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop**<br>S. Hofer et al. | RSS workshop summary | [PDF ↗](https://arxiv.org/pdf/2012.03806) · [arXiv](https://arxiv.org/abs/2012.03806) | Debate on whether to close the gap or design around it. |
| 2020 | **Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey**<br>W. Zhao, J. P. Queralta, T. Westerlund | IEEE SSCI | [PDF](papers/00-surveys/zhao2020survey.pdf) · [PDF ↗](https://arxiv.org/pdf/2009.13303) · [arXiv](https://arxiv.org/abs/2009.13303) | Domain randomization, adaptation, imitation, meta-learning for transfer. |
| 2021 | **Sim2Real in Robotics and Automation: Applications and Challenges**<br>S. Hofer et al. | IEEE Transactions on Automation Science and Engineering | [link](https://doi.org/10.1109/TASE.2021.3064065) | Expert perspectives on where sim-to-real works and fails. |
| 2021 | **Crossing the Reality Gap: A Survey on Sim-to-Real Transferability of Robot Controllers in Reinforcement Learning**<br>E. Salvato, G. Fenu, E. Medvet, F. A. Pellegrino | IEEE Access | [link](https://doi.org/10.1109/ACCESS.2021.3126658) | Transferability methods for RL controllers. |
| 2022 | **Robot Learning from Randomized Simulations: A Review**<br>F. Muratore, F. Ramos, G. Turk, W. Yu, M. Gienger, J. Peters | Frontiers in Robotics and AI | [PDF](papers/00-surveys/muratore2022review.pdf) · [PDF ↗](https://arxiv.org/pdf/2111.00956) · [arXiv](https://arxiv.org/abs/2111.00956) | Taxonomy of randomization: static, adaptive, adversarial. |
| 2025 | **A Survey of Sim-to-Real Methods in RL: Progress, Prospects and Challenges with Foundation Models**<br>L. Da et al. | arXiv | [PDF](papers/00-surveys/da2025survey.pdf) · [PDF ↗](https://arxiv.org/pdf/2502.13187) · [arXiv](https://arxiv.org/abs/2502.13187) | Sim-to-real in the foundation-model era. |

<a id="01-reality-gap"></a>
## The reality gap: foundations and measurement

Where the term comes from and how to measure whether simulation predicts reality.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1995 | **Noise and the Reality Gap: The Use of Simulation in Evolutionary Robotics**<br>N. Jakobi, P. Husbands, I. Harvey | ECAL (LNCS) | [link](https://doi.org/10.1007/3-540-59496-5_337) | Early statement of the reality gap; adding noise to simulation. |
| 2013 | **The Transferability Approach: Crossing the Reality Gap in Evolutionary Robotics**<br>S. Koos, J.-B. Mouret, S. Doncieux | IEEE Transactions on Evolutionary Computation | [link](https://doi.org/10.1109/TEVC.2012.2185849) | Optimize for behaviours that transfer, using a learned transferability estimate. |
| 2020 | **Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?**<br>A. Kadian et al. | RA-L | [PDF](papers/01-reality-gap/kadian2020srcc.pdf) · [PDF ↗](https://arxiv.org/pdf/1912.06321) · [arXiv](https://arxiv.org/abs/1912.06321) | Sim-vs-real correlation (SRCC) was 0.18 for Habitat PointGoal success; agents exploited collision sliding. |

<a id="02-domain-randomization"></a>
## Domain randomization and adaptive randomization

Visual and dynamics randomization, automatic and data-driven randomization ranges.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2017 | **CAD2RL: Real Single-Image Flight without a Single Real Image**<br>F. Sadeghi, S. Levine | RSS | [PDF ↗](https://arxiv.org/pdf/1611.04201) · [arXiv](https://arxiv.org/abs/1611.04201) | Randomized rendering for indoor drone flight. |
| 2017 | **Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World**<br>J. Tobin et al. | IROS | [PDF](papers/02-domain-randomization/tobin2017domain.pdf) · [PDF ↗](https://arxiv.org/pdf/1703.06907) · [arXiv](https://arxiv.org/abs/1703.06907) | Visual randomization; real detector accurate to 1.5 cm from synthetic images only. |
| 2018 | **Learning Dexterous In-Hand Manipulation**<br>OpenAI et al. | IJRR 2020 | [PDF ↗](https://arxiv.org/pdf/1808.00177) · [arXiv](https://arxiv.org/abs/1808.00177) | Heavy physics and visual randomization; no demonstrations. |
| 2018 | **Sim-to-Real Transfer of Robotic Control with Dynamics Randomization**<br>X. B. Peng, M. Andrychowicz, W. Zaremba, P. Abbeel | ICRA | [PDF](papers/02-domain-randomization/peng2018dynrand.pdf) · [PDF ↗](https://arxiv.org/pdf/1710.06537) · [arXiv](https://arxiv.org/abs/1710.06537) | Randomizing masses, friction, damping and latency with recurrent policies. |
| 2019 | **Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience**<br>Y. Chebotar et al. | ICRA | [PDF ↗](https://arxiv.org/pdf/1810.05687) · [arXiv](https://arxiv.org/abs/1810.05687) | SimOpt: fit the randomization distribution to a few real rollouts. |
| 2019 | **Sim-to-Real via Sim-to-Sim: Data-efficient Robotic Grasping via Randomized-to-Canonical Adaptation Networks**<br>S. James et al. | CVPR | [PDF ↗](https://arxiv.org/pdf/1812.07252) · [arXiv](https://arxiv.org/abs/1812.07252) | Translate randomized and real images into a canonical sim view. |
| 2019 | **Solving Rubik's Cube with a Robot Hand**<br>OpenAI et al. | arXiv | [PDF](papers/02-domain-randomization/openai2019rubik.pdf) · [PDF ↗](https://arxiv.org/pdf/1910.07113) · [arXiv](https://arxiv.org/abs/1910.07113) | Automatic domain randomization (ADR) widens ranges as the policy succeeds. |
| 2019 | **BayesSim: Adaptive Domain Randomization via Probabilistic Inference for Robotics Simulators**<br>F. Ramos, R. C. Possas, D. Fox | RSS | [PDF ↗](https://arxiv.org/pdf/1906.01728) · [arXiv](https://arxiv.org/abs/1906.01728) | Likelihood-free posterior over simulator parameters. |
| 2021 | **Data-efficient Domain Randomization with Bayesian Optimization**<br>F. Muratore, C. Eilers, M. Gienger, J. Peters | RA-L | [PDF ↗](https://arxiv.org/pdf/2003.02471) · [arXiv](https://arxiv.org/abs/2003.02471) | BayRn: Bayesian optimization of randomization parameters on real returns. |
| 2023 | **DROPO: Sim-to-Real Transfer with Offline Domain Randomization**<br>G. Tiboni, K. Arndt, V. Kyrki | Robotics and Autonomous Systems | [PDF ↗](https://arxiv.org/pdf/2201.08434) · [arXiv](https://arxiv.org/abs/2201.08434) | Estimate randomization distributions from offline real data. |
| 2025 | **Neural Fidelity Calibration for Informative Sim-to-Real Adaptation**<br>Y. Yu, L. Liu | arXiv | [PDF ↗](https://arxiv.org/pdf/2504.08604) · [arXiv](https://arxiv.org/abs/2504.08604) | Diffusion posterior over simulator parameters plus residual dynamics and residual terrain; anomaly-triggered fine-tuning on a Jackal. Reviewed in reports/01. Linked, not stored (30 MB). |

<a id="03-sysid-actuators"></a>
## System identification and actuator modelling

Identifying simulator parameters, actuator networks, latency, residual and learned dynamics.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1995 | **Series Elastic Actuators**<br>G. A. Pratt, M. M. Williamson | IROS | [link](https://doi.org/10.1109/IROS.1995.525827) | Compliant actuators: torque sensing and shock tolerance. |
| 2017 | **Proprioceptive Actuator Design in the MIT Cheetah: Impact Mitigation and High-Bandwidth Physical Interaction for Dynamic Legged Robots**<br>P. M. Wensing et al. | IEEE Transactions on Robotics | [link](https://doi.org/10.1109/TRO.2016.2640183) | Low-gear-ratio actuators that are easier to model and transparent to forces. |
| 2018 | **Sim-to-Real: Learning Agile Locomotion For Quadruped Robots**<br>J. Tan et al. | RSS | [PDF](papers/03-sysid-actuators/tan2018agile.pdf) · [PDF ↗](https://arxiv.org/pdf/1804.10332) · [arXiv](https://arxiv.org/abs/1804.10332) | System ID, an accurate actuator model and simulated latency, plus randomization (Minitaur). |
| 2019 | **Learning Agile and Dynamic Motor Skills for Legged Robots**<br>J. Hwangbo et al. | Science Robotics | [PDF](papers/03-sysid-actuators/hwangbo2019agile.pdf) · [PDF ↗](https://arxiv.org/pdf/1901.08652) · [arXiv](https://arxiv.org/abs/1901.08652) | Actuator network learned from real motor data, inserted into the simulator (ANYmal). |
| 2019 | **Iterative Reinforcement Learning Based Design of Dynamic Locomotion Skills for Cassie**<br>Z. Xie et al. | arXiv | [PDF ↗](https://arxiv.org/pdf/1903.09537) · [arXiv](https://arxiv.org/abs/1903.09537) | Iterative sim-to-real design for a biped. |
| 2021 | **NeuralSim: Augmenting Differentiable Simulators with Neural Networks**<br>E. Heiden, D. Millard, E. Coumans, Y. Sheng, G. S. Sukhatme | ICRA | [PDF ↗](https://arxiv.org/pdf/2011.04217) · [arXiv](https://arxiv.org/abs/2011.04217) | Hybrid differentiable simulator: neural networks inserted where analytical models fall short, including frictional contact. |
| 2022 | **Probabilistic Inference of Simulation Parameters via Parallel Differentiable Simulation**<br>E. Heiden, C. E. Denniston, D. Millard, F. Ramos, G. S. Sukhatme | ICRA | [PDF ↗](https://arxiv.org/pdf/2109.08815) · [arXiv](https://arxiv.org/abs/2109.08815) | Posterior over simulator parameters with Stein variational gradient descent and a multiple-shooting likelihood. |
| 2024 | **Identifying Terrain Physical Parameters from Vision: Towards Physical-Parameter-Aware Locomotion and Navigation**<br>J. Chen, J. Frey, R. Zhou, T. Miki, G. Martius, M. Hutter | IEEE RA-L | [PDF ↗](https://arxiv.org/pdf/2408.16567) · [arXiv](https://arxiv.org/abs/2408.16567) | Friction and stiffness decoded from proprioception in simulation, then used to label images for a visual predictor (ANYmal). |
| 2025 | **ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills**<br>T. He et al. | RSS | [PDF](papers/03-sysid-actuators/he2025asap.pdf) · [PDF ↗](https://arxiv.org/pdf/2502.01143) · [arXiv](https://arxiv.org/abs/2502.01143) | Delta (residual) action model learned from real data, then fine-tuning in the corrected simulator. |
| 2025 | **Achieving Precise and Reliable Locomotion with Differentiable Simulation-Based System Identification**<br>V. Kovalev, E. Chaikovskaia, E. Davydenko, R. Gorbachev | arXiv | [PDF](papers/03-sysid-actuators/kovalev2025diffsysid.pdf) · [PDF ↗](https://arxiv.org/pdf/2508.04696) · [arXiv](https://arxiv.org/abs/2508.04696) | Earlier version: MJX fit of armature, friction loss and damping; +46% distance, -75% rotation error on a small humanoid. Reviewed in reports/01. |
| 2025 | **Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics**<br>C. Li, A. Krause, M. Hutter | arXiv | [PDF ↗](https://arxiv.org/pdf/2501.10100) · [arXiv](https://arxiv.org/abs/2501.10100) | Learned neural simulator for policy training. |
| 2025 | **Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots**<br>C. Li, A. Krause, M. Hutter | arXiv | [PDF ↗](https://arxiv.org/pdf/2504.16680) · [arXiv](https://arxiv.org/abs/2504.16680) | Offline learned model with uncertainty penalties. |
| 2025 | **Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation**<br>P. Roth, J. Frey, C. Cadena, M. Hutter | RSS | [PDF ↗](https://arxiv.org/pdf/2504.19322) · [arXiv](https://arxiv.org/abs/2504.19322) | Forward dynamics model trained on simulated and real experience, used inside MPPI planning. |
| 2025 | **Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning**<br>N. Sobanbabu, G. He, T. He, Y. Yang, G. Shi | arXiv | [PDF ↗](https://arxiv.org/pdf/2505.14266) · [arXiv](https://arxiv.org/abs/2505.14266) | SPI-Active: parallel sampling instead of gradients, Fisher-information exploration; 42-63% better than baselines on locomotion tasks. |
| 2026 | **Trajectory-based actuator identification via differentiable simulation**<br>V. Kovalev, E. Chaikovskaia, E. Davydenko, R. Gorbachev | arXiv | [PDF](papers/03-sysid-actuators/kovalev2026trajid.pdf) · [PDF ↗](https://arxiv.org/pdf/2604.10351) · [arXiv](https://arxiv.org/abs/2604.10351) | Encoder-only actuator ID through MJX: TrajID-NN 7.54 mrad vs bench model 14.20; 23x faster than an ASAP-like residual. Reviewed in reports/01. |

<a id="04-adaptation-robustness"></a>
## Adaptation and robust policies

Online system identification, privileged teachers, adaptation modules, adversarial training.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2017 | **Robust Adversarial Reinforcement Learning**<br>L. Pinto, J. Davidson, R. Sukthankar, A. Gupta | ICML | [PDF ↗](https://arxiv.org/pdf/1703.02702) · [arXiv](https://arxiv.org/abs/1703.02702) | An adversary applies disturbance forces during training. |
| 2017 | **Preparing for the Unknown: Learning a Universal Policy with Online System Identification**<br>W. Yu, J. Tan, C. K. Liu, G. Turk | RSS | [PDF ↗](https://arxiv.org/pdf/1702.02453) · [arXiv](https://arxiv.org/abs/1702.02453) | Policy conditioned on parameters estimated online (UP-OSI). |
| 2020 | **Learning Quadrupedal Locomotion over Challenging Terrain**<br>J. Lee et al. | Science Robotics | [PDF ↗](https://arxiv.org/pdf/2010.11251) · [arXiv](https://arxiv.org/abs/2010.11251) | Privileged teacher, proprioceptive-history student; zero-shot to mud, snow, water. |
| 2021 | **RMA: Rapid Motor Adaptation for Legged Robots**<br>A. Kumar, Z. Fu, D. Pathak, J. Malik | RSS | [PDF](papers/04-adaptation-robustness/kumar2021rma.pdf) · [PDF ↗](https://arxiv.org/pdf/2107.04034) · [arXiv](https://arxiv.org/abs/2107.04034) | Adaptation module estimates environment latent from history in fractions of a second. |
| 2021 | **Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning**<br>J. Siekmann et al. | RSS | [PDF ↗](https://arxiv.org/pdf/2105.08328) · [arXiv](https://arxiv.org/abs/2105.08328) | Terrain randomization for Cassie stairs without vision. |
| 2022 | **Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild**<br>T. Miki et al. | Science Robotics | [PDF ↗](https://arxiv.org/pdf/2201.08117) · [arXiv](https://arxiv.org/abs/2201.08117) | Belief encoder learns when to trust perception. |

<a id="05-contact-simulators"></a>
## Contact models and simulators

Rigid-body contact formulations, simulator comparisons and validation against real impacts.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1996 | **An Implicit Time-Stepping Scheme for Rigid Body Dynamics with Inelastic Collisions and Coulomb Friction**<br>D. E. Stewart, J. C. Trinkle | International Journal for Numerical Methods in Engineering | [link](https://doi.org/10.1002/(sici)1097-0207(19960815)39:15<2673::aid-nme972>3.0.co;2-i) | Velocity-level complementarity (LCP) time stepping. |
| 2012 | **MuJoCo: A Physics Engine for Model-Based Control**<br>E. Todorov, T. Erez, Y. Tassa | IROS | [link](https://doi.org/10.1109/IROS.2012.6386109) | Soft, convex contact designed for optimization and control. |
| 2014 | **Convex and Analytically-Invertible Dynamics with Contacts and Constraints: Theory and Implementation in MuJoCo**<br>E. Todorov | ICRA | [link](https://doi.org/10.1109/ICRA.2014.6907751) | The convex contact formulation behind MuJoCo. |
| 2015 | **Simulation Tools for Model-Based Robotics: Comparison of Bullet, Havok, MuJoCo, ODE and PhysX**<br>T. Erez, Y. Tassa, E. Todorov | ICRA | [link](https://doi.org/10.1109/ICRA.2015.7139807) | Speed-accuracy trade-offs across engines. |
| 2017 | **Fundamental Limitations in Performance and Interpretability of Common Planar Rigid-Body Contact Models**<br>N. Fazeli et al. | ISRR | [PDF](papers/05-contact-simulators/fazeli2017limitations.pdf) · [PDF ↗](https://arxiv.org/pdf/1710.04979) · [arXiv](https://arxiv.org/abs/1710.04979) | Six contact models identified on real impact data; limits of the rigid-body paradigm. |
| 2018 | **Per-Contact Iteration Method for Solving Contact Dynamics**<br>J. Hwangbo, J. Lee, M. Hutter | RA-L | [link](https://doi.org/10.1109/LRA.2018.2792536) | Hard-contact solver behind RaiSim. |
| 2019 | **On the Similarities and Differences Among Contact Models in Robot Simulation**<br>P. C. Horak, J. C. Trinkle | RA-L | [link](https://doi.org/10.1109/LRA.2019.2891085) | Compares complementarity, convex and penalty formulations. |
| 2020 | **ContactNets: Learning Discontinuous Contact Dynamics with Smooth, Implicit Representations**<br>S. Pfrommer, M. Halm, M. Posa | CoRL | [PDF ↗](https://arxiv.org/pdf/2009.11193) · [arXiv](https://arxiv.org/abs/2009.11193) | Learns signed distances and contact Jacobians with a complementarity-inspired loss; realistic impact and stiction from 60 s of real data. |
| 2021 | **Learning Contact Dynamics using Physically Structured Neural Networks**<br>A. Hochlehnert, A. Terenin, S. Sæmundsson, M. P. Deisenroth | AISTATS | [PDF ↗](https://arxiv.org/pdf/2102.11206) · [arXiv](https://arxiv.org/abs/2102.11206) | Physically structured networks learn discontinuous contact data-efficiently; touch feedback makes the problem tractable. |
| 2021 | **Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning**<br>V. Makoviychuk et al. | NeurIPS Datasets and Benchmarks | [PDF ↗](https://arxiv.org/pdf/2108.10470) · [arXiv](https://arxiv.org/abs/2108.10470) | GPU-parallel simulation. |
| 2022 | **Validating Robotics Simulators on Real-World Impacts**<br>B. Acosta, W. Yang, M. Posa | RA-L | [PDF](papers/05-contact-simulators/acosta2022impacts.pdf) · [PDF ↗](https://arxiv.org/pdf/2110.00541) · [arXiv](https://arxiv.org/abs/2110.00541) | Drake, MuJoCo, Bullet vs real data: inelastic impacts captured, elastic ones not. |
| 2022 | **Dojo: A Differentiable Physics Engine for Robotics**<br>T. A. Howell, S. Le Cleac'h, J. Brüdigam, Q. Chen, J. Sun, J. Z. Kolter, M. Schwager, Z. Manchester | arXiv | [PDF ↗](https://arxiv.org/pdf/2203.00806) · [arXiv](https://arxiv.org/abs/2203.00806) | Hard contact as a nonlinear complementarity problem with cone constraints; tunable smoothing gives useful gradients. |
| 2024 | **DiffSim2Real: Deploying Quadrupedal Locomotion Policies Purely Trained in Differentiable Simulation**<br>J. Bagajo, C. Schwarke, V. Klemm, I. Georgiev, J.-P. Sleiman, J. Tordesillas, A. Garg, M. Hutter | arXiv | [PDF ↗](https://arxiv.org/pdf/2411.02189) · [arXiv](https://arxiv.org/abs/2411.02189) | Smooth contact model that keeps both gradients and accuracy; real quadruped walking from analytic-gradient training. |
| 2024 | **Contact Models in Robotics: a Comparative Analysis**<br>Q. Le Lidec, W. Jallet, L. Montaut, I. Laptev, C. Schmid, J. Carpentier | IEEE T-RO | [PDF ↗](https://arxiv.org/pdf/2304.06372) · [arXiv](https://arxiv.org/abs/2304.06372) | Physical relaxations of each simulator's contact model, with quantitative benchmarks. |
| 2024 | **Learning Deployable Locomotion Control via Differentiable Simulation**<br>C. Schwarke, V. Klemm, J. Bagajo, J.-P. Sleiman, I. Georgiev, J. Tordesillas, M. Hutter | arXiv | [PDF ↗](https://arxiv.org/pdf/2404.02887) · [arXiv](https://arxiv.org/abs/2404.02887) | Differentiable contact model with informative gradients; first legged policy trained entirely in a differentiable simulator and deployed. |
| 2025 | **MuJoCo Playground**<br>K. Zakka et al. | arXiv / RSS | [PDF](papers/05-contact-simulators/zakka2025playground.pdf) · [PDF ↗](https://arxiv.org/pdf/2502.08844) · [arXiv](https://arxiv.org/abs/2502.08844) | MJX-based training and zero-shot sim-to-real for quadrupeds, humanoids, hands and arms. |

<a id="06-achievements"></a>
## Landmark sim-to-real results

Legged, humanoid, dexterous and aerial systems trained in simulation and deployed on hardware.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2022 | **Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning**<br>N. Rudin, D. Hoeller, P. Reist, M. Hutter | CoRL | [PDF ↗](https://arxiv.org/pdf/2109.11978) · [arXiv](https://arxiv.org/abs/2109.11978) | Minutes of GPU training, transferred to ANYmal. |
| 2023 | **Visual Dexterity: In-Hand Reorientation of Novel and Complex Object Shapes**<br>T. Chen et al. | Science Robotics | [PDF ↗](https://arxiv.org/pdf/2211.11744) · [arXiv](https://arxiv.org/abs/2211.11744) | Depth-camera in-hand reorientation trained in simulation; open-source hardware under $5,000. |
| 2023 | **Champion-Level Drone Racing Using Deep Reinforcement Learning**<br>E. Kaufmann et al. | Nature | [link](https://doi.org/10.1038/s41586-023-06419-4) | Residual models of perception and dynamics fitted from real data. |
| 2023 | **Reaching the Limit in Autonomous Racing: Optimal Control versus Reinforcement Learning**<br>Y. Song et al. | Science Robotics | [PDF ↗](https://arxiv.org/pdf/2310.10943) · [arXiv](https://arxiv.org/abs/2310.10943) | RL with domain randomization beats optimal control at the limit. |
| 2024 | **Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning**<br>T. Haarnoja et al. | Science Robotics | [PDF ↗](https://arxiv.org/pdf/2304.13653) · [arXiv](https://arxiv.org/abs/2304.13653) | Zero-shot transfer via high-frequency control, targeted dynamics randomization and perturbations; walked 181% faster than a scripted baseline. |
| 2024 | **ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots**<br>D. Hoeller et al. | Science Robotics | [PDF ↗](https://arxiv.org/pdf/2306.14874) · [arXiv](https://arxiv.org/abs/2306.14874) | Perceptive parkour trained in simulation. |
| 2024 | **DextrAH-G: Pixels-to-Action Dexterous Arm-Hand Grasping with Geometric Fabrics**<br>T. G. W. Lum et al. | CoRL | [PDF ↗](https://arxiv.org/pdf/2407.02274) · [arXiv](https://arxiv.org/abs/2407.02274) | Sim-trained arm-hand grasping from depth. |
| 2024 | **SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning**<br>J. Luo et al. | ICRA | [PDF ↗](https://arxiv.org/pdf/2401.16013) · [arXiv](https://arxiv.org/abs/2401.16013) | RL directly in the real world, the alternative to sim-to-real. |
| 2024 | **Real-World Humanoid Locomotion with Reinforcement Learning**<br>I. Radosavovic et al. | Science Robotics | [PDF ↗](https://arxiv.org/pdf/2303.03381) · [arXiv](https://arxiv.org/abs/2303.03381) | Transformer policy, zero-shot humanoid walking outdoors. |

<a id="07-real2sim-generative"></a>
## Real-to-sim, photorealistic and generative simulation

Digital twins, Gaussian-splat rendering, generated tasks and scenes.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2024 | **SplatSim: Zero-Shot Sim2Real Transfer of RGB Manipulation Policies Using Gaussian Splatting**<br>M. N. Qureshi et al. | arXiv / ICRA 2025 | [PDF](papers/07-real2sim-generative/qureshi2024splatsim.pdf) · [PDF ↗](https://arxiv.org/pdf/2409.10161) · [arXiv](https://arxiv.org/abs/2409.10161) | Gaussian-splat rendering; 86.25% zero-shot vs 97.5% real-data policies. |
| 2024 | **Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation (RialTo)**<br>M. Torne et al. | RSS | [PDF](papers/07-real2sim-generative/torne2024rialto.pdf) · [PDF ↗](https://arxiv.org/pdf/2403.03949) · [arXiv](https://arxiv.org/abs/2403.03949) | Scan the scene into a digital twin, fine-tune with RL; over 67% robustness gain. |
| 2024 | **RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation**<br>Y. Wang et al. | ICML | [PDF ↗](https://arxiv.org/pdf/2311.01455) · [arXiv](https://arxiv.org/abs/2311.01455) | Foundation models propose tasks, scenes and rewards in simulation. |
| 2026 | **RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks**<br>K. Chen, S. Xie, U. Yoo, X. Zhu, C. Magner, A. Zhu, D. Kim, E. Heiden, E. Coumans, M. Macklin, S. Huang, K. Goldberg | arXiv | [PDF](papers/07-real2sim-generative/chen2026robosimstudio.pdf) · [PDF ↗](https://arxiv.org/pdf/2610.18835) · [arXiv](https://arxiv.org/abs/2610.18835) | Editable solver, contact model and parameters on Newton; humans and coding agents tune simulations against video. Stored PDF is v1. Reviewed in reports/01. |

<a id="08-datasets-benchmarks"></a>
## Real-robot datasets for modelling and benchmarking

Large logs of real proprioception, contact estimates and ground truth that actuator, contact and state-estimation models can be fitted and tested on.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2026 | **GrandTour: A Legged Robotics Dataset in the Wild for Multi-Modal Perception and State Estimation**<br>T. Tuna, J. Frey, F. Fu, K. Patterson, T. Xu, M. Fallon, C. Cadena, M. Hutter | arXiv | [PDF ↗](https://arxiv.org/pdf/2602.18164) · [arXiv](https://arxiv.org/abs/2602.18164) | ANYmal-D: 49 missions, >10 km, 12 actuators' position, velocity and torque, estimator contacts, RTK-GNSS and total-station ground truth. Reviewed in reports/01. Linked, not stored (28 MB). |
