# Paper catalog

61 entries in 7 categories. **36** have a PDF available online (PDF ↗) and **14** also have a local copy in this repository (PDF).
Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.

| Category | Entries | PDF online | Local PDF |
|---|---:|---:|---:|
| [Surveys, tutorials and free books](#00-surveys-books) | 11 | 8 | 3 |
| [Classical stability](#01-classical) | 5 | 0 | 0 |
| [Robust, nonlinear and hybrid stability](#02-robust-nonlinear) | 9 | 0 | 0 |
| [Computation and design with certificates](#03-computation-design) | 8 | 1 | 0 |
| [Learning with stability and safety guarantees](#04-learning-with-guarantees) | 15 | 14 | 4 |
| [Neural-network verification for control](#05-nn-verification) | 9 | 9 | 5 |
| [Stability and safety on real robots](#06-robot-deployment) | 4 | 4 | 2 |

<a id="00-surveys-books"></a>
## Surveys, tutorials and free books

Overviews of learned certificates, safe learning, barrier functions, contraction and verification, plus free textbooks.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1994 | **Linear Matrix Inequalities in System and Control Theory**<br>S. Boyd, L. El Ghaoui, E. Feron, V. Balakrishnan | SIAM (free online) | [link](https://web.stanford.edu/~boyd/lmibook/) | LMIs for Lyapunov functions, absolute stability and robust control. |
| 1998 | **Mathematical Control Theory: Deterministic Finite Dimensional Systems (2nd ed.)**<br>E. D. Sontag | Springer (free PDF) | [PDF ↗](http://www.sontaglab.org/FTPDIR/sontag_mathematical_control_theory_springer98.pdf) | Control Lyapunov functions, ISS and nonlinear stabilization. |
| 2008 | **Feedback Systems: An Introduction for Scientists and Engineers**<br>K. J. Åström, R. M. Murray | Princeton University Press (free online) | [link](https://fbswiki.org/) | Eigenvalues, Lyapunov functions, Nyquist criterion and margins. |
| 2019 | **Control Barrier Functions: Theory and Applications**<br>A. D. Ames, S. Coogan, M. Egerstedt, G. Notomista, K. Sreenath, P. Tabuada | ECC | [PDF](papers/00-surveys-books/ames2019cbf.pdf) · [PDF ↗](https://arxiv.org/pdf/1903.11199) · [arXiv](https://arxiv.org/abs/1903.11199) | Tutorial overview of control barrier functions and CLF–CBF quadratic programs. |
| 2021 | **Contraction Theory for Nonlinear Stability Analysis and Learning-based Control: A Tutorial Overview**<br>H. Tsukamoto, S.-J. Chung, J.-J. E. Slotine | Annual Reviews in Control | [PDF ↗](https://arxiv.org/pdf/2110.00675) · [arXiv](https://arxiv.org/abs/2110.00675) | Tutorial on contraction theory for stability analysis and learning-based control. |
| 2022 | **Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning**<br>L. Brunke, M. Greeff, A. W. Hall, Z. Yuan, S. Zhou et al. | Annual Review of Control, Robotics, and Autonomous Systems | [PDF ↗](https://arxiv.org/pdf/2108.06266) · [arXiv](https://arxiv.org/abs/2108.06266) | Safe learning in robotics, from learning-based control to safe RL. |
| 2023 | **Safe Control with Learned Certificates: A Survey of Neural Lyapunov, Barrier, and Contraction methods**<br>C. Dawson, S. Gao, C. Fan | IEEE T-RO | [PDF](papers/00-surveys-books/dawson2023certificates.pdf) · [PDF ↗](https://arxiv.org/pdf/2202.11762) · [arXiv](https://arxiv.org/abs/2202.11762) | Survey of neural Lyapunov, barrier and contraction certificates learned with controllers. |
| 2023 | **The Safety Filter: A Unified View of Safety-Critical Control in Autonomous Systems**<br>K.-C. Hsu, H. Hu, J. F. Fisac | Annual Review of Control, Robotics, and Autonomous Systems | [PDF ↗](https://arxiv.org/pdf/2309.05837) · [arXiv](https://arxiv.org/abs/2309.05837) | Unified view of safety filters: barrier functions, reachability, predictive filters. |
| 2023 | **Underactuated Robotics**<br>R. Tedrake | MIT course notes (free online) | [link](https://underactuated.mit.edu/) | Lyapunov analysis, sum-of-squares, regions of attraction, walking models. |
| 2026 | **Bridging Control with Neural Network Verifier alpha-beta-CROWN: A Tutorial**<br>H. Li, X. Zhong, H. Cheng, B. Hu, H. Zhang | arXiv | [PDF](papers/00-surveys-books/li2026crowntutorial.pdf) · [PDF ↗](https://arxiv.org/pdf/2605.26577) · [arXiv](https://arxiv.org/abs/2605.26577) | Tutorial on using the α,β-CROWN verifier for Lyapunov, barrier and reachability problems in control. |
| 2026 | **Stabilization Learning: A Paradigm Transition Bridging Control Theory and Machine Learning**<br>Q. Quan | arXiv | [PDF ↗](https://arxiv.org/pdf/2606.31562) · [arXiv](https://arxiv.org/abs/2606.31562) | Proposes 'stabilization learning': stability, not reward, as the primary objective of learned control. |

<a id="01-classical"></a>
## Classical stability

The founding results: governors, polynomial criteria, Lyapunov's method, Nyquist, LaSalle.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1868 | **On Governors**<br>J. C. Maxwell | Proceedings of the Royal Society of London | [link](https://doi.org/10.1098/rspl.1867.0055) | First mathematical stability analysis of a feedback mechanism. |
| 1895 | **Ueber die Bedingungen, unter welchen eine Gleichung nur Wurzeln mit negativen reellen Theilen besitzt**<br>A. Hurwitz | Mathematische Annalen | [link](https://doi.org/10.1007/BF01446812) | Hurwitz criterion: stability from polynomial coefficients. |
| 1932 | **Regeneration Theory**<br>H. Nyquist | Bell System Technical Journal | [link](https://doi.org/10.1002/j.1538-7305.1932.tb02344.x) | Closed-loop stability from the open-loop frequency response. |
| 1960 | **Some Extensions of Liapunov's Second Method**<br>J. P. LaSalle | IRE Transactions on Circuit Theory | [link](https://doi.org/10.1109/TCT.1960.1086720) | Invariance principle: convergence from dV/dt <= 0. |
| 1992 | **The General Problem of the Stability of Motion (1892; English translation 1992)**<br>A. M. Lyapunov | International Journal of Control | [link](https://doi.org/10.1080/00207179208934253) | Lyapunov's thesis: the direct and indirect methods. |

<a id="02-robust-nonlinear"></a>
## Robust, nonlinear and hybrid stability

Absolute stability, small gain, dissipativity, passivity, ISS, IQCs, contraction, switched systems and time delay.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1963 | **Lyapunov Functions for the Problem of Lur'e in Automatic Control**<br>R. E. Kalman | PNAS | [link](https://doi.org/10.1073/pnas.49.2.201) | KYP lemma: frequency-domain tests (Popov) linked to Lyapunov functions. |
| 1966 | **On the Input-Output Stability of Time-Varying Nonlinear Feedback Systems, Part I**<br>G. Zames | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/TAC.1966.1098316) | Small-gain theorem and the circle criterion for feedback interconnections. |
| 1972 | **Dissipative Dynamical Systems Part I: General Theory**<br>J. C. Willems | Archive for Rational Mechanics and Analysis | [link](https://doi.org/10.1007/BF00276493) | Dissipativity and storage functions: the general theory of passivity. |
| 1981 | **A New Feedback Method for Dynamic Control of Manipulators**<br>M. Takegaki, S. Arimoto | Journal of Dynamic Systems, Measurement, and Control | [link](https://doi.org/10.1115/1.3139651) | PD control with gravity compensation is globally stable for robot arms. |
| 1989 | **Smooth Stabilization Implies Coprime Factorization**<br>E. D. Sontag | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/9.28018) | Introduces input-to-state stability (ISS). |
| 1997 | **System Analysis via Integral Quadratic Constraints**<br>A. Megretski, A. Rantzer | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/9.587335) | Unified robustness analysis with integral quadratic constraints. |
| 1998 | **Multiple Lyapunov Functions and Other Analysis Tools for Switched and Hybrid Systems**<br>M. S. Branicky | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/9.664150) | Stability of switched and hybrid systems with multiple Lyapunov functions. |
| 1998 | **On Contraction Analysis for Non-linear Systems**<br>W. Lohmiller, J.-J. E. Slotine | Automatica | [link](https://doi.org/10.1016/S0005-1098(98)00019-3) | Contraction: incremental stability via a metric on the Jacobian. |
| 2014 | **Tutorial on Lyapunov-based Methods for Time-Delay Systems**<br>E. Fridman | European Journal of Control | [link](https://doi.org/10.1016/j.ejcon.2014.10.001) | Lyapunov–Krasovskii functionals and LMIs for delay systems. |

<a id="03-computation-design"></a>
## Computation and design with certificates

Sum-of-squares, control Lyapunov and barrier functions, LQR-trees, hybrid zero dynamics.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1983 | **Stabilization with Relaxed Controls**<br>Z. Artstein | Nonlinear Analysis: Theory, Methods & Applications | [link](https://doi.org/10.1016/0362-546X(83)90049-4) | A control Lyapunov function implies stabilizability. |
| 1989 | **A 'Universal' Construction of Artstein's Theorem on Nonlinear Stabilization**<br>E. D. Sontag | Systems & Control Letters | [link](https://doi.org/10.1016/0167-6911(89)90028-5) | Sontag's formula: a feedback law from any control Lyapunov function. |
| 2002 | **On the Construction of Lyapunov Functions using the Sum of Squares Decomposition**<br>A. Papachristodoulou, S. Prajna | IEEE CDC | [link](https://doi.org/10.1109/CDC.2002.1184414) | Polynomial Lyapunov functions by sum-of-squares programming. |
| 2003 | **Semidefinite Programming Relaxations for Semialgebraic Problems**<br>P. A. Parrilo | Mathematical Programming | [link](https://doi.org/10.1007/s10107-003-0387-5) | Sum-of-squares relaxations, following Parrilo's 2000 Caltech thesis. |
| 2003 | **Hybrid Zero Dynamics of Planar Biped Walkers**<br>E. R. Westervelt, J. W. Grizzle, D. E. Koditschek | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/TAC.2002.806653) | Stability of underactuated bipedal walking via hybrid zero dynamics and Poincaré maps. |
| 2010 | **LQR-trees: Feedback Motion Planning via Sums-of-Squares Verification**<br>R. Tedrake, I. R. Manchester, M. Tobenkin, J. W. Roberts | International Journal of Robotics Research | [link](https://doi.org/10.1177/0278364910369189) | Verified regions of attraction stitched into a feedback motion plan. |
| 2014 | **Rapidly Exponentially Stabilizing Control Lyapunov Functions and Hybrid Zero Dynamics**<br>A. D. Ames, K. Galloway, K. Sreenath, J. W. Grizzle | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/TAC.2014.2299335) | CLF-QPs for bipedal walking. |
| 2017 | **Control Barrier Function Based Quadratic Programs for Safety Critical Systems**<br>A. D. Ames, X. Xu, J. W. Grizzle, P. Tabuada | IEEE Transactions on Automatic Control | [PDF ↗](https://arxiv.org/pdf/1609.06408) · [arXiv](https://arxiv.org/abs/1609.06408) | Control barrier functions unified with CLFs in real-time quadratic programs. |

<a id="04-learning-with-guarantees"></a>
## Learning with stability and safety guarantees

Lyapunov-constrained RL, learned Lyapunov, barrier and contraction certificates, stable learned dynamics.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2002 | **Lyapunov Design for Safe Reinforcement Learning**<br>T. J. Perkins, A. G. Barto | Journal of Machine Learning Research | [link](https://www.jmlr.org/papers/v3/perkins02a.html) | First Lyapunov-constrained RL: actions restricted so that a Lyapunov function decreases. |
| 2017 | **Safe Model-based Reinforcement Learning with Stability Guarantees**<br>F. Berkenkamp, M. Turchetta, A. P. Schoellig, A. Krause | NeurIPS | [PDF](papers/04-learning-with-guarantees/berkenkamp2017safe.pdf) · [PDF ↗](https://arxiv.org/pdf/1705.08551) · [arXiv](https://arxiv.org/abs/1705.08551) | Safe model-based RL: statistical models certify and expand a region of attraction during learning. |
| 2018 | **A Lyapunov-based Approach to Safe Reinforcement Learning**<br>Y. Chow, O. Nachum, E. Duenez-Guzman, M. Ghavamzadeh | NeurIPS | [PDF](papers/04-learning-with-guarantees/chow2018lyapunov.pdf) · [PDF ↗](https://arxiv.org/pdf/1805.07708) · [arXiv](https://arxiv.org/abs/1805.07708) | Lyapunov-based safe RL in constrained MDPs. |
| 2018 | **The Lyapunov Neural Network: Adaptive Stability Certification for Safe Learning of Dynamical Systems**<br>S. M. Richards, F. Berkenkamp, A. Krause | CoRL | [PDF](papers/04-learning-with-guarantees/richards2018lyapunovnn.pdf) · [PDF ↗](https://arxiv.org/pdf/1808.00924) · [arXiv](https://arxiv.org/abs/1808.00924) | Lyapunov neural network that learns a safety certificate for a closed loop. |
| 2019 | **Neural Lyapunov Control**<br>Y.-C. Chang, N. Roohi, S. Gao | NeurIPS | [PDF](papers/04-learning-with-guarantees/chang2019neurallyap.pdf) · [PDF ↗](https://arxiv.org/pdf/2005.00611) · [arXiv](https://arxiv.org/abs/2005.00611) | Learns controller and neural Lyapunov function with a falsifier; larger regions of attraction than LQR and SOS. |
| 2019 | **End-to-End Safe Reinforcement Learning through Barrier Functions for Safety-Critical Continuous Control Tasks**<br>R. Cheng, G. Orosz, R. M. Murray, J. W. Burdick | AAAI | [PDF ↗](https://arxiv.org/pdf/1903.08792) · [arXiv](https://arxiv.org/abs/1903.08792) | Model-free RL combined with CBF controllers to stay safe during learning. |
| 2019 | **Learning Stable Deep Dynamics Models**<br>G. Manek, J. Z. Kolter | NeurIPS | [PDF ↗](https://arxiv.org/pdf/2001.06116) · [arXiv](https://arxiv.org/abs/2001.06116) | Deep dynamics models stable by construction via a jointly learned Lyapunov function. |
| 2020 | **Actor-Critic Reinforcement Learning for Control with Stability Guarantee**<br>M. Han, L. Zhang, J. Wang, W. Pan | IEEE Robotics and Automation Letters | [PDF ↗](https://arxiv.org/pdf/2004.14288) · [arXiv](https://arxiv.org/abs/2004.14288) | Actor-critic RL with a Lyapunov critic for closed-loop stability guarantees. |
| 2020 | **Learning Control Barrier Functions from Expert Demonstrations**<br>A. Robey, H. Hu, L. Lindemann, H. Zhang, D. V. Dimarogonas et al. | IEEE CDC | [PDF ↗](https://arxiv.org/pdf/2004.03315) · [arXiv](https://arxiv.org/abs/2004.03315) | Learning control barrier functions from expert demonstrations. |
| 2020 | **Learning for Safety-Critical Control with Control Barrier Functions**<br>A. Taylor, A. Singletary, Y. Yue, A. Ames | L4DC | [PDF ↗](https://arxiv.org/pdf/1912.10099) · [arXiv](https://arxiv.org/abs/1912.10099) | Learning to reduce model uncertainty in CBF safety constraints. |
| 2020 | **Neural Contraction Metrics for Robust Estimation and Control: A Convex Optimization Approach**<br>H. Tsukamoto, S.-J. Chung | IEEE Control Systems Letters | [PDF ↗](https://arxiv.org/pdf/2006.04361) · [arXiv](https://arxiv.org/abs/2006.04361) | Neural contraction metrics for robust estimation and control. |
| 2022 | **Neural Lyapunov Control of Unknown Nonlinear Systems with Stability Guarantees**<br>R. Zhou, T. Quartz, H. De Sterck, J. Liu | NeurIPS | [PDF ↗](https://arxiv.org/pdf/2206.01913) · [arXiv](https://arxiv.org/abs/2206.01913) | Neural Lyapunov control of unknown nonlinear systems, with an SMT-verified region of attraction. |
| 2023 | **Neural Lyapunov Control for Discrete-Time Systems**<br>J. Wu, A. Clark, Y. Kantaros, Y. Vorobeychik | NeurIPS | [PDF ↗](https://arxiv.org/pdf/2305.06547) · [arXiv](https://arxiv.org/abs/2305.06547) | Neural Lyapunov control for discrete-time systems. |
| 2026 | **Stability Verification for Switched Systems using Neural Multiple Lyapunov Functions**<br>J. Huang, S. Li, X. Yin | arXiv | [PDF ↗](https://arxiv.org/pdf/2601.00587) · [arXiv](https://arxiv.org/abs/2601.00587) | Neural multiple Lyapunov functions with counterexample-guided synthesis for switched systems. |
| 2026 | **Universal Approximation of Maximal Lyapunov Functions with Anchored Neural Networks**<br>J. Liu | arXiv | [PDF ↗](https://arxiv.org/pdf/2608.17290) · [arXiv](https://arxiv.org/abs/2608.17290) | Universal approximation of maximal Lyapunov functions by anchored neural networks. |

<a id="05-nn-verification"></a>
## Neural-network verification for control

Exact and bound-propagation verifiers, Lipschitz bounds, quadratic constraints and verified neural controllers.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2017 | **Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks**<br>G. Katz, C. Barrett, D. Dill, K. Julian, M. Kochenderfer | CAV | [PDF](papers/05-nn-verification/katz2017reluplex.pdf) · [PDF ↗](https://arxiv.org/pdf/1702.01135) · [arXiv](https://arxiv.org/abs/1702.01135) | Reluplex: exact SMT verification of ReLU networks; shows the problem is NP-complete. |
| 2018 | **Efficient Neural Network Robustness Certification with General Activation Functions**<br>H. Zhang, T.-W. Weng, P.-Y. Chen, C.-J. Hsieh, L. Daniel | NeurIPS | [PDF ↗](https://arxiv.org/pdf/1811.00866) · [arXiv](https://arxiv.org/abs/1811.00866) | CROWN: linear-relaxation bounds for networks with general activations. |
| 2019 | **Efficient and Accurate Estimation of Lipschitz Constants for Deep Neural Networks**<br>M. Fazlyab, A. Robey, H. Hassani, M. Morari, G. J. Pappas | NeurIPS | [PDF](papers/05-nn-verification/fazlyab2019lipsdp.pdf) · [PDF ↗](https://arxiv.org/pdf/1906.04893) · [arXiv](https://arxiv.org/abs/1906.04893) | LipSDP: tight Lipschitz-constant upper bounds by semidefinite programming. |
| 2019 | **On the Effectiveness of Interval Bound Propagation for Training Verifiably Robust Models**<br>S. Gowal, K. Dvijotham, R. Stanforth, R. Bunel, C. Qin et al. | ICCV | [PDF ↗](https://arxiv.org/pdf/1810.12715) · [arXiv](https://arxiv.org/abs/1810.12715) | Interval bound propagation for training verifiably robust networks. |
| 2021 | **Lyapunov-stable neural-network control**<br>H. Dai, B. Landry, L. Yang, M. Pavone, R. Tedrake | RSS | [PDF](papers/05-nn-verification/dai2021lyapunovnn.pdf) · [PDF ↗](https://arxiv.org/pdf/2109.14152) · [arXiv](https://arxiv.org/abs/2109.14152) | Lyapunov-stable neural-network control verified by mixed-integer programs; pendulum and 2D/3D quadrotors. |
| 2021 | **Reachability Analysis of Neural Feedback Loops**<br>M. Everett, G. Habibi, C. Sun, J. P. How | IEEE Access | [PDF ↗](https://arxiv.org/pdf/2108.04140) · [arXiv](https://arxiv.org/abs/2108.04140) | Forward reachable sets of neural feedback loops. |
| 2021 | **Beta-CROWN: Efficient Bound Propagation with Per-neuron Split Constraints for Complete and Incomplete Neural Network Robustness Verification**<br>S. Wang, H. Zhang, K. Xu, X. Lin, S. Jana et al. | NeurIPS | [PDF ↗](https://arxiv.org/pdf/2103.06624) · [arXiv](https://arxiv.org/abs/2103.06624) | β-CROWN: bound propagation with neuron-split constraints for complete verification. |
| 2022 | **Stability Analysis using Quadratic Constraints for Systems with Neural Network Controllers**<br>H. Yin, P. Seiler, M. Arcak | IEEE Transactions on Automatic Control | [PDF](papers/05-nn-verification/yin2022iqc.pdf) · [PDF ↗](https://arxiv.org/pdf/2006.07579) · [arXiv](https://arxiv.org/abs/2006.07579) | Stability and region-of-attraction ellipsoids for NN-controlled loops via quadratic constraints. |
| 2024 | **Lyapunov-stable Neural Control for State and Output Feedback: A Novel Formulation**<br>L. Yang, H. Dai, Z. Shi, C.-J. Hsieh, R. Tedrake, H. Zhang | ICML | [PDF](papers/05-nn-verification/yang2024lyapunovstable.pdf) · [PDF ↗](https://arxiv.org/pdf/2404.07956) · [arXiv](https://arxiv.org/abs/2404.07956) | Lyapunov-stable neural state and output feedback verified with GPU bound propagation, no SOS/MIP/SMT. |

<a id="06-robot-deployment"></a>
## Stability and safety on real robots

Safety filters and stability-guided learning deployed on legged robots, humanoids and manipulators.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2022 | **Safe Reinforcement Learning for Legged Locomotion**<br>T.-Y. Yang, T. Zhang, L. Luu, S. Ha, J. Tan, W. Yu | IROS | [PDF ↗](https://arxiv.org/pdf/2203.02638) · [arXiv](https://arxiv.org/abs/2203.02638) | Safe RL for legged locomotion: a recovery policy takes over before unsafe states. |
| 2026 | **Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions**<br>K. Lee, S. Park, G. Park, M.-J. Kim, J. Park | arXiv | [PDF ↗](https://arxiv.org/pdf/2605.25546) · [arXiv](https://arxiv.org/abs/2605.25546) | Input-to-state safe CBFs for humanoid whole-body control under bounded disturbances. |
| 2026 | **Safe Execution of RL Policies Via Acceleration-Based CBF-QP Constraint Enforcement for Real-World Robotic Deployments**<br>B. Muraccioli, A. Cariou, P.-A. Leziart, M. Celerier, A. Demont et al. | arXiv | [PDF](papers/06-robot-deployment/muraccioli2026acccbf.pdf) · [PDF ↗](https://arxiv.org/pdf/2607.14488) · [arXiv](https://arxiv.org/abs/2607.14488) | Acceleration-based CBF-QP filter for RL policies; 92% fewer violations on a real Unitree H1. |
| 2026 | **Stability of Control Lyapunov Function Guided Reinforcement Learning**<br>Z. Olkin, W. D. Compton, A. D. Ames | arXiv | [PDF](papers/06-robot-deployment/olkin2026clfrl.pdf) · [PDF ↗](https://arxiv.org/pdf/2605.01978) · [arXiv](https://arxiv.org/abs/2605.01978) | Exponential stability of optimal policies under CLF-guided RL rewards; humanoid walking orbits. |
