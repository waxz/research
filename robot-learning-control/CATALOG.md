# Paper catalog

96 papers in 11 categories; 35 have a local PDF copy (open-access arXiv versions).
Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.

| Category | Papers | Local PDFs |
|---|---:|---:|
| [SuperMimic and direct baselines](#00-supermimic) | 3 | 3 |
| [Surveys and overview papers](#01-surveys) | 26 | 22 |
| [RL foundations](#02-rl-foundations) | 7 | 2 |
| [Model-based RL and world models](#03-model-based-rl) | 10 | 2 |
| [Differentiable simulation and analytic gradients](#04-differentiable-simulation) | 8 | 3 |
| [Physics-based character motion imitation](#05-character-motion-imitation) | 7 | 2 |
| [Humanoid whole-body control](#06-humanoid-whole-body-control) | 7 | 0 |
| [Legged locomotion and sim-to-real](#07-legged-locomotion-sim2real) | 11 | 0 |
| [Model-based and hybrid control](#08-model-based-control) | 6 | 0 |
| [Imitation learning and manipulation](#09-imitation-learning) | 9 | 1 |
| [Dexterous manipulation and agile flight](#10-dexterous-agile) | 2 | 0 |

<a id="00-supermimic"></a>
## SuperMimic and direct baselines

The target paper and the two humanoid trackers it builds on and compares against.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2026 | **BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion**<br>Q. Liao et al. | Science Robotics 11(117) | [PDF](papers/00-supermimic/liao2026beyondmimic.pdf) · [arXiv](https://arxiv.org/abs/2508.08241) | Tracking reward and recipe that SuperMimic reuses. |
| 2026 | **SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model**<br>Q. Liao, Y. Shao, J. Long, K. Zakka, R. Horowitz, P. Abbeel, K. Sreenath | CoRL 2026 (oral) | [PDF](papers/00-supermimic/liao2026supermimic.pdf) · [arXiv](https://arxiv.org/abs/2610.28480) · [link](https://supermimic.github.io/) | Target paper. BPTT through one learned world model; beats SONIC in 3 GPU-hours. |
| 2026 | **SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control**<br>Z. Luo et al. | Science Robotics 11(117) | [PDF](papers/00-supermimic/luo2026sonic.pdf) · [arXiv](https://arxiv.org/abs/2511.07820) | Main baseline: cluster-scale PPO tracker (128 GPUs, 7 days). |

<a id="01-surveys"></a>
## Surveys and overview papers

Reviews of model-based control, RL, imitation learning, exploration, sim-to-real, humanoids and foundation models.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2013 | **Reinforcement Learning in Robotics: A Survey**<br>J. Kober, J. A. Bagnell, J. Peters | IJRR 32(11) | [link](https://doi.org/10.1177/0278364913495721) | Classic pre-deep-learning survey of robot RL. |
| 2017 | **A Brief Survey of Deep Reinforcement Learning**<br>K. Arulkumaran, M. P. Deisenroth, M. Brundage, A. A. Bharath | IEEE Signal Processing Magazine | [PDF](papers/01-surveys/arulkumaran2017brief.pdf) · [arXiv](https://arxiv.org/abs/1708.05866) | Compact overview of deep RL. |
| 2018 | **An Algorithmic Perspective on Imitation Learning**<br>T. Osa, J. Pajarinen, G. Neumann, J. A. Bagnell, P. Abbeel, J. Peters | Foundations and Trends in Robotics | [PDF](papers/01-surveys/osa2018algorithmic.pdf) · [arXiv](https://arxiv.org/abs/1811.06711) | Behavior cloning vs inverse RL in robotics. |
| 2018 | **Reinforcement Learning: An Introduction (2nd ed.)**<br>R. S. Sutton, A. G. Barto | MIT Press (book) | [link](http://incompleteideas.net/book/the-book-2nd.html) | Standard RL textbook; free online from the authors. |
| 2019 | **Reinforcement Learning and Optimal Control**<br>D. P. Bertsekas | Athena Scientific (book) | [link](https://web.mit.edu/dimitrib/www/RLbook.html) | Bridges dynamic programming, optimal control and RL. |
| 2019 | **Challenges of Real-World Reinforcement Learning**<br>G. Dulac-Arnold, D. Mankowitz, T. Hester | ICML RL4RealLife workshop | [PDF](papers/01-surveys/dulacarnold2019challenges.pdf) · [arXiv](https://arxiv.org/abs/1904.12901) | Short original version of the challenges list. |
| 2019 | **A Tour of Reinforcement Learning: The View from Continuous Control**<br>B. Recht | Annual Review of Control, Robotics, and Autonomous Systems | [PDF](papers/01-surveys/recht2019tour.pdf) · [arXiv](https://arxiv.org/abs/1806.09460) | RL compared with LQR and MPC; sample complexity. |
| 2020 | **Learning-Based Model Predictive Control: Toward Safe Learning in Control**<br>L. Hewing, K. P. Wabersich, M. Menner, M. N. Zeilinger | Annual Review of Control, Robotics, and Autonomous Systems | [link](https://doi.org/10.1146/annurev-control-090419-075625) | Learning models, costs and safety filters inside MPC. |
| 2020 | **Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey**<br>W. Zhao, J. P. Queralta, T. Westerlund | IEEE SSCI | [PDF](papers/01-surveys/zhao2020sim2real.pdf) · [arXiv](https://arxiv.org/abs/2009.13303) | Domain randomization, adaptation and sim-to-real methods. |
| 2021 | **Challenges of Real-World Reinforcement Learning: Definitions, Benchmarks and Analysis**<br>G. Dulac-Arnold et al. | Machine Learning 110 | [PDF](papers/01-surveys/dulacarnold2021challenges.pdf) · [arXiv](https://arxiv.org/abs/2003.11881) | Nine challenges for deploying RL; arXiv title is 'An empirical investigation of the challenges of real-world RL'. |
| 2022 | **Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning**<br>L. Brunke et al. | Annual Review of Control, Robotics, and Autonomous Systems | [PDF](papers/01-surveys/brunke2022safe.pdf) · [arXiv](https://arxiv.org/abs/2108.06266) | Control-theoretic guarantees meet learning. |
| 2022 | **Exploration in Deep Reinforcement Learning: A Survey**<br>P. Ladosz, L. Weng, M. Kim, H. Oh | Information Fusion | [PDF](papers/01-surveys/ladosz2022exploration.pdf) · [arXiv](https://arxiv.org/abs/2205.00824) | Sparse rewards and exploration strategies. |
| 2023 | **Exploration in Deep Reinforcement Learning: From Single-Agent to Multiagent Domain**<br>J. Hao, T. Yang et al. | IEEE TNNLS | [PDF](papers/01-surveys/hao2023exploration.pdf) · [arXiv](https://arxiv.org/abs/2109.06668) | Uncertainty- vs intrinsic-motivation exploration. |
| 2023 | **Model-based Reinforcement Learning: A Survey**<br>T. M. Moerland, J. Broekens, A. Plaat, C. M. Jonker | Foundations and Trends in Machine Learning | [PDF](papers/01-surveys/moerland2023mbrl.pdf) · [arXiv](https://arxiv.org/abs/2006.16712) | Reference survey for model-based RL. |
| 2023 | **Reaching the Limit in Autonomous Racing: Optimal Control versus Reinforcement Learning**<br>Y. Song, A. Romero, M. Mueller, V. Koltun, D. Scaramuzza | Science Robotics 8(82) | [PDF](papers/01-surveys/song2023reaching.pdf) · [arXiv](https://arxiv.org/abs/2310.10943) | Head-to-head: RL wins by optimizing a better objective. |
| 2023 | **A Survey of Imitation Learning: Algorithms, Recent Developments, and Challenges**<br>M. Zare, P. M. Kebria, A. Khosravi, S. Nahavandi | arXiv | [PDF](papers/01-surveys/zare2023survey.pdf) · [arXiv](https://arxiv.org/abs/2309.02473) | Recent imitation learning methods. |
| 2024 | **A Review of Differentiable Simulators**<br>R. Newbury et al. | IEEE Access | [PDF](papers/01-surveys/newbury2024review.pdf) · [arXiv](https://arxiv.org/abs/2407.05560) | Gradients, contact models and tools for differentiable physics. |
| 2024 | **Optimization-Based Control for Dynamic Legged Robots**<br>P. M. Wensing, M. Posa, Y. Hu, A. Escande, N. Mansard, A. Del Prete | IEEE Transactions on Robotics | [PDF](papers/01-surveys/wensing2024optimization.pdf) · [arXiv](https://arxiv.org/abs/2211.11644) | Model-based control survey: MPC, WBC, trajectory optimization. |
| 2025 | **Benchmarking Model Predictive Control and Reinforcement Learning Based Control for Legged Robot Locomotion in MuJoCo Simulation**<br>S. Akki, T. Chen | arXiv | [PDF](papers/01-surveys/akki2025benchmarking.pdf) · [arXiv](https://arxiv.org/abs/2501.16590) | Direct MPC vs RL benchmark on Unitree Go1. |
| 2025 | **Foundation Models in Robotics: Applications, Challenges, and the Future**<br>R. Firoozi et al. | IJRR | [PDF](papers/01-surveys/firoozi2025foundation.pdf) · [arXiv](https://arxiv.org/abs/2312.07843) | Foundation models across perception, planning and control. |
| 2025 | **Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning**<br>Z. Gu et al. | arXiv | [PDF](papers/01-surveys/gu2025humanoid.pdf) · [arXiv](https://arxiv.org/abs/2501.02116) | Model-based and learning-based humanoid control. |
| 2025 | **Learning-based Legged Locomotion: State of the Art and Future Perspectives**<br>S. Ha, J. Lee, M. van de Panne, Z. Xie, W. Yu, M. Khadiv | IJRR | [PDF](papers/01-surveys/ha2025learning.pdf) · [arXiv](https://arxiv.org/abs/2406.01152) | RL and imitation for legged robots; relation to model-based control. |
| 2025 | **Survey of Vision-Language-Action Models for Embodied Manipulation**<br>H. Li, Y. Chen et al. | arXiv | [PDF](papers/01-surveys/li2025vla.pdf) · [arXiv](https://arxiv.org/abs/2508.15201) | Large-scale imitation for open-ended manipulation. |
| 2025 | **Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes**<br>C. Tang, B. Abbatematteo, J. Hu, R. Chandra, R. Martin-Martin, P. Stone | Annual Review of Control, Robotics, and Autonomous Systems | [PDF](papers/01-surveys/tang2025deep.pdf) · [arXiv](https://arxiv.org/abs/2408.03539) | Where RL actually works on hardware. |
| 2025 | **A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots**<br>M. Yuan et al. | arXiv | [PDF](papers/01-surveys/yuan2025bfm.pdf) · [arXiv](https://arxiv.org/abs/2506.20487) | Large pretrained whole-body controllers. |
| 2026 | **Synthesis of Model Predictive Control and Reinforcement Learning: Survey and Classification**<br>R. Reiter, J. Hoffmann et al. | Annual Reviews in Control | [PDF](papers/01-surveys/reiter2026synthesis.pdf) · [arXiv](https://arxiv.org/abs/2502.02133) | Taxonomy of MPC + RL hybrids. |

<a id="02-rl-foundations"></a>
## RL foundations

Core model-free algorithms used by every robot-learning pipeline.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1992 | **Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning**<br>R. J. Williams | Machine Learning 8 | [link](https://doi.org/10.1007/BF00992696) | REINFORCE / likelihood-ratio policy gradient. |
| 2015 | **Human-Level Control through Deep Reinforcement Learning**<br>V. Mnih et al. | Nature 518 | [link](https://doi.org/10.1038/nature14236) | DQN. |
| 2015 | **Trust Region Policy Optimization**<br>J. Schulman, S. Levine, P. Moritz, M. Jordan, P. Abbeel | ICML | [arXiv](https://arxiv.org/abs/1502.05477) | Trust-region policy updates. |
| 2016 | **Continuous Control with Deep Reinforcement Learning**<br>T. P. Lillicrap et al. | ICLR | [arXiv](https://arxiv.org/abs/1509.02971) | DDPG. |
| 2016 | **High-Dimensional Continuous Control Using Generalized Advantage Estimation**<br>J. Schulman, P. Moritz, S. Levine, M. Jordan, P. Abbeel | ICLR | [PDF](papers/02-rl-foundations/schulman2016gae.pdf) · [arXiv](https://arxiv.org/abs/1506.02438) | GAE / lambda-returns, used by SuperMimic's critic. |
| 2017 | **Proximal Policy Optimization Algorithms**<br>J. Schulman, F. Wolski, P. Dhariwal, A. Radford, O. Klimov | arXiv | [PDF](papers/02-rl-foundations/schulman2017ppo.pdf) · [arXiv](https://arxiv.org/abs/1707.06347) | PPO: default optimizer for robot RL. |
| 2018 | **Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor**<br>T. Haarnoja, A. Zhou, P. Abbeel, S. Levine | ICML | [arXiv](https://arxiv.org/abs/1801.01290) | SAC. |

<a id="03-model-based-rl"></a>
## Model-based RL and world models

Learning dynamics models and training policies in imagination.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1991 | **Dyna, an Integrated Architecture for Learning, Planning, and Reacting**<br>R. S. Sutton | ACM SIGART Bulletin 2(4) | [link](https://doi.org/10.1145/122344.122377) | Imagined experience from a learned model. |
| 2011 | **PILCO: A Model-Based and Data-Efficient Approach to Policy Search**<br>M. P. Deisenroth, C. E. Rasmussen | ICML | [link](https://icml.cc/2011/papers/323_icmlpaper.pdf) | Analytic gradients through a GP dynamics model. |
| 2018 | **World Models**<br>D. Ha, J. Schmidhuber | NeurIPS | [arXiv](https://arxiv.org/abs/1803.10122) | Policies trained inside a learned latent model. |
| 2019 | **When to Trust Your Model: Model-Based Policy Optimization**<br>M. Janner, J. Fu, M. Zhang, S. Levine | NeurIPS | [PDF](papers/03-model-based-rl/janner2019mbpo.pdf) · [arXiv](https://arxiv.org/abs/1906.08253) | Short model rollouts branched from real states (Dyna-style). |
| 2020 | **Dream to Control: Learning Behaviors by Latent Imagination**<br>D. Hafner, T. Lillicrap, J. Ba, M. Norouzi | ICLR | [PDF](papers/03-model-based-rl/hafner2020dreamer.pdf) · [arXiv](https://arxiv.org/abs/1912.01603) | Backprop of lambda-returns through latent imagination. |
| 2022 | **Temporal Difference Learning for Model Predictive Control**<br>N. Hansen, X. Wang, H. Su | ICML | [arXiv](https://arxiv.org/abs/2203.04955) | Short-horizon planning with a terminal value. |
| 2023 | **DayDreamer: World Models for Physical Robot Learning**<br>P. Wu, A. Escontrela, D. Hafner, K. Goldberg, P. Abbeel | CoRL | [arXiv](https://arxiv.org/abs/2206.14176) | World-model learning directly on hardware. |
| 2025 | **Mastering Diverse Domains through World Models (DreamerV3)**<br>D. Hafner, J. Pasukonis, J. Ba, T. Lillicrap | Nature 640 | [arXiv](https://arxiv.org/abs/2301.04104) | General world-model agent. |
| 2025 | **Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics**<br>C. Li, A. Krause, M. Hutter | arXiv | [arXiv](https://arxiv.org/abs/2501.10100) | PPO inside a learned neural simulator; real-robot transfer. |
| 2025 | **Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots**<br>C. Li, A. Krause, M. Hutter | arXiv | [arXiv](https://arxiv.org/abs/2504.16680) | Offline MBRL with uncertainty penalties. |

<a id="04-differentiable-simulation"></a>
## Differentiable simulation and analytic gradients

First-order policy gradients through simulators or learned models.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2015 | **Learning Continuous Control Policies by Stochastic Value Gradients**<br>N. Heess, G. Wayne, D. Silver, T. Lillicrap, Y. Tassa, T. Erez | NeurIPS | [PDF](papers/04-differentiable-simulation/heess2015svg.pdf) · [arXiv](https://arxiv.org/abs/1510.09142) | Pathwise gradients through learned models with a critic. |
| 2021 | **SuperTrack: Motion Tracking for Physically Simulated Characters Using Supervised Learning**<br>L. Fussell, K. Bergamin, D. Holden | ACM TOG 40(6) | [link](https://doi.org/10.1145/3478513.3480527) | First tracker trained by BPTT through a learned world model. |
| 2022 | **Do Differentiable Simulators Give Better Policy Gradients?**<br>H. J. T. Suh, M. Simchowitz, K. Zhang, R. Tedrake | ICML | [PDF](papers/04-differentiable-simulation/suh2022differentiable.pdf) · [arXiv](https://arxiv.org/abs/2202.00817) | Bias and variance of analytic gradients through contact. |
| 2022 | **Accelerated Policy Learning with Parallel Differentiable Simulation (SHAC)**<br>J. Xu, V. Makoviychuk, Y. Narang, F. Ramos, W. Matusik, A. Garg, M. Macklin | ICLR | [PDF](papers/04-differentiable-simulation/xu2022shac.pdf) · [arXiv](https://arxiv.org/abs/2204.07137) | Short-horizon actor-critic; template for SuperMimic's objective. |
| 2022 | **ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters**<br>H. Yao, Z. Song, B. Chen, L. Liu | ACM TOG 41(6) | [arXiv](https://arxiv.org/abs/2210.06063) | Jointly learned dynamics, skill latent and controller. |
| 2024 | **Learning Quadruped Locomotion Using Differentiable Simulation**<br>Y. Song, S. Kim, D. Scaramuzza | CoRL | [arXiv](https://arxiv.org/abs/2403.14864) | Real quadruped trained with analytic gradients. |
| 2024 | **MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations**<br>H. Yao et al. | ACM TOG 43(4) | [link](https://doi.org/10.1145/3658137) | Learned-model training on tens of hours of motion. |
| 2025 | **Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics**<br>Y. Lei, Z. Luo, T. He, J. Cao, G. Shi, K. Kitani | ICLR 2025 Workshop on World Models | [link](https://openreview.net/pdf/b3031990328dd52267a571b265c15328bf6d6120.pdf) | Differentiable neural dynamics scaled to many clips. |

<a id="05-character-motion-imitation"></a>
## Physics-based character motion imitation

Reference-tracking RL and motion priors for simulated characters.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2018 | **DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills**<br>X. B. Peng, P. Abbeel, S. Levine, M. van de Panne | ACM TOG 37(4) | [PDF](papers/05-character-motion-imitation/peng2018deepmimic.pdf) · [arXiv](https://arxiv.org/abs/1804.02717) | Reference-tracking reward and reference-state initialization. |
| 2019 | **Neural Probabilistic Motor Primitives for Humanoid Control**<br>J. Merel et al. | ICLR | [arXiv](https://arxiv.org/abs/1811.11711) | Distilling many experts into one latent controller. |
| 2021 | **AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control**<br>X. B. Peng, Z. Ma, P. Abbeel, S. Levine, A. Kanazawa | ACM TOG 40(4) | [PDF](papers/05-character-motion-imitation/peng2021amp.pdf) · [arXiv](https://arxiv.org/abs/2104.02180) | Style reward from a discriminator instead of exact tracking. |
| 2022 | **ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters**<br>X. B. Peng et al. | ACM TOG 41(4) | [arXiv](https://arxiv.org/abs/2205.01906) | Reusable skill latent space. |
| 2023 | **Perpetual Humanoid Control for Real-time Simulated Avatars**<br>Z. Luo, J. Cao, A. Winkler, K. Kitani, W. Xu | ICCV | [arXiv](https://arxiv.org/abs/2305.06456) | Tracking almost all of AMASS with recovery. |
| 2024 | **Universal Humanoid Motion Representations for Physics-Based Control (PULSE)**<br>Z. Luo et al. | ICLR | [arXiv](https://arxiv.org/abs/2310.04582) | Latent motion representation for downstream RL. |
| 2024 | **MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting**<br>C. Tessler, Y. Guo, O. Nabati, G. Chechik, X. B. Peng | ACM TOG 43(6) | [arXiv](https://arxiv.org/abs/2409.14393) | Partial and multimodal goals via inpainting. |

<a id="06-humanoid-whole-body-control"></a>
## Humanoid whole-body control

Motion tracking, teleoperation and locomotion on real humanoids.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2024 | **Expressive Whole-Body Control for Humanoid Robots (ExBody)**<br>X. Cheng et al. | RSS | [arXiv](https://arxiv.org/abs/2402.16796) | Upper body imitates, legs follow velocity. |
| 2024 | **HumanPlus: Humanoid Shadowing and Imitation from Humans**<br>Z. Fu, Q. Zhao, Q. Wu, G. Wetzstein, C. Finn | CoRL | [arXiv](https://arxiv.org/abs/2406.10454) | Shadowing plus imitation learning on a humanoid. |
| 2024 | **Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation (H2O)**<br>T. He et al. | IROS | [arXiv](https://arxiv.org/abs/2403.04436) | Mocap tracking for real humanoid teleoperation. |
| 2024 | **OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning**<br>T. He et al. | CoRL | [arXiv](https://arxiv.org/abs/2406.08858) | Teacher-student tracking with multiple input modalities. |
| 2024 | **Real-World Humanoid Locomotion with Reinforcement Learning**<br>I. Radosavovic et al. | Science Robotics 9(89) | [arXiv](https://arxiv.org/abs/2303.03381) | Self-exploration RL for robust humanoid walking. |
| 2025 | **ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills**<br>T. He et al. | RSS | [arXiv](https://arxiv.org/abs/2502.01143) | Delta-action model to close the sim-to-real gap. |
| 2026 | **Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data (LATENT)**<br>Z. Zhang et al. | IROS | [arXiv](https://arxiv.org/abs/2603.12686) | Motion representations for downstream task RL. |

<a id="07-legged-locomotion-sim2real"></a>
## Legged locomotion and sim-to-real

Self-exploration RL with domain randomization on quadrupeds.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2017 | **Emergence of Locomotion Behaviours in Rich Environments**<br>N. Heess et al. | arXiv | [arXiv](https://arxiv.org/abs/1707.02286) | Pure self-exploration: capable but unnatural gaits. |
| 2017 | **Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World**<br>J. Tobin et al. | IROS | [arXiv](https://arxiv.org/abs/1703.06907) | Domain randomization. |
| 2018 | **Sim-to-Real Transfer of Robotic Control with Dynamics Randomization**<br>X. B. Peng, M. Andrychowicz, W. Zaremba, P. Abbeel | ICRA | [arXiv](https://arxiv.org/abs/1710.06537) | Randomizing dynamics parameters for transfer. |
| 2019 | **Learning Agile and Dynamic Motor Skills for Legged Robots**<br>J. Hwangbo et al. | Science Robotics 4(26) | [arXiv](https://arxiv.org/abs/1901.08652) | Learned actuator model; RL on ANYmal. |
| 2020 | **Learning Quadrupedal Locomotion over Challenging Terrain**<br>J. Lee, J. Hwangbo, L. Wellhausen, V. Koltun, M. Hutter | Science Robotics 5(47) | [arXiv](https://arxiv.org/abs/2010.11251) | Privileged teacher, proprioceptive student. |
| 2021 | **Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning**<br>V. Makoviychuk et al. | NeurIPS Datasets and Benchmarks | [arXiv](https://arxiv.org/abs/2108.10470) | Massively parallel GPU simulation. |
| 2022 | **Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions**<br>A. Escontrela et al. | IROS | [arXiv](https://arxiv.org/abs/2203.15103) | Style prior replaces hand-tuned shaping. |
| 2022 | **Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild**<br>T. Miki et al. | Science Robotics 7(62) | [arXiv](https://arxiv.org/abs/2201.08117) | Perception plus RL on real terrain. |
| 2022 | **Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning**<br>N. Rudin, D. Hoeller, P. Reist, M. Hutter | CoRL | [arXiv](https://arxiv.org/abs/2109.11978) | legged_gym: PPO locomotion in minutes. |
| 2023 | **Robot Parkour Learning**<br>Z. Zhuang et al. | CoRL | [arXiv](https://arxiv.org/abs/2309.05665) | Agile parkour via RL and distillation. |
| 2024 | **Extreme Parkour with Legged Robots**<br>X. Cheng, K. Shi, A. Agarwal, D. Pathak | ICRA | [arXiv](https://arxiv.org/abs/2309.14341) | Vision-based parkour from self-exploration RL. |

<a id="08-model-based-control"></a>
## Model-based and hybrid control

MPC, whole-body control and hybrids of optimal control with RL.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2014 | **A Direct Method for Trajectory Optimization of Rigid Bodies Through Contact**<br>M. Posa, C. Cantu, R. Tedrake | IJRR 33(1) | [link](https://doi.org/10.1177/0278364913506757) | Contact-implicit trajectory optimization. |
| 2016 | **Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot**<br>S. Kuindersma et al. | Autonomous Robots 40 | [link](https://doi.org/10.1007/s10514-015-9479-3) | Model-based humanoid control stack. |
| 2018 | **Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control**<br>J. Di Carlo, P. M. Wensing, B. Katz, G. Bledt, S. Kim | IROS | [link](https://doi.org/10.1109/IROS.2018.8594448) | Convex MPC on a single-rigid-body model. |
| 2019 | **Residual Reinforcement Learning for Robot Control**<br>T. Johannink et al. | ICRA | [arXiv](https://arxiv.org/abs/1812.03201) | RL residual on top of a conventional controller. |
| 2019 | **Highly Dynamic Quadruped Locomotion via Whole-Body Impulse Control and Model Predictive Control**<br>D. Kim, J. Di Carlo, B. Katz, G. Bledt, S. Kim | arXiv | [arXiv](https://arxiv.org/abs/1909.06586) | MPC + whole-body impulse control. |
| 2024 | **DTC: Deep Tracking Control**<br>F. Jenelten, J. He, F. Farshidian, M. Hutter | Science Robotics | [arXiv](https://arxiv.org/abs/2309.15462) | RL policy tracks trajectory-optimization plans. |

<a id="09-imitation-learning"></a>
## Imitation learning and manipulation

Behavior cloning, DAgger, adversarial imitation and visuomotor policies.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2000 | **Algorithms for Inverse Reinforcement Learning**<br>A. Y. Ng, S. Russell | ICML | [link](https://ai.stanford.edu/~ang/papers/icml00-irl.pdf) | Recovering a reward from demonstrations. |
| 2010 | **Efficient Reductions for Imitation Learning**<br>S. Ross, J. A. Bagnell | AISTATS | [link](https://proceedings.mlr.press/v9/ross10a.html) | T^2 compounding-error bound for behavior cloning. |
| 2011 | **A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger)**<br>S. Ross, G. Gordon, J. A. Bagnell | AISTATS | [PDF](papers/09-imitation-learning/ross2011dagger.pdf) · [arXiv](https://arxiv.org/abs/1011.0686) | DAgger: linear error bound via on-policy expert queries. |
| 2016 | **Generative Adversarial Imitation Learning**<br>J. Ho, S. Ermon | NeurIPS | [arXiv](https://arxiv.org/abs/1606.03476) | Adversarial imitation; basis of AMP. |
| 2018 | **QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation**<br>D. Kalashnikov et al. | CoRL | [arXiv](https://arxiv.org/abs/1806.10293) | Large-scale real-world RL for grasping. |
| 2018 | **Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations (DAPG)**<br>A. Rajeswaran et al. | RSS | [arXiv](https://arxiv.org/abs/1709.10087) | Demonstrations accelerate RL exploration. |
| 2023 | **Diffusion Policy: Visuomotor Policy Learning via Action Diffusion**<br>C. Chi et al. | RSS | [arXiv](https://arxiv.org/abs/2303.04137) | Diffusion-based behavior cloning. |
| 2023 | **Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA / ACT)**<br>T. Z. Zhao, V. Kumar, S. Levine, C. Finn | RSS | [arXiv](https://arxiv.org/abs/2304.13705) | Teleoperation data + action-chunking transformer. |
| 2024 | **pi0: A Vision-Language-Action Flow Model for General Robot Control**<br>K. Black et al. | arXiv | [arXiv](https://arxiv.org/abs/2410.24164) | Generalist VLA policy trained on large demo data. |

<a id="10-dexterous-agile"></a>
## Dexterous manipulation and agile flight

Tasks where self-exploration RL reached or beat expert performance.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2019 | **Solving Rubik's Cube with a Robot Hand**<br>OpenAI et al. | arXiv | [arXiv](https://arxiv.org/abs/1910.07113) | Self-exploration RL with automatic domain randomization. |
| 2023 | **Champion-Level Drone Racing Using Deep Reinforcement Learning**<br>E. Kaufmann et al. | Nature 620 | [link](https://doi.org/10.1038/s41586-023-06419-4) | RL beat human world-champion drone pilots. |
