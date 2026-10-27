# Paper catalog

49 papers in 9 categories; 10 have a local PDF copy (open-access arXiv versions).
Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.

| Category | Papers | Local PDFs |
|---|---:|---:|
| [Surveys and overview papers](#00-surveys) | 7 | 3 |
| [Classical feedback and frequency-domain control](#01-classical-feedback) | 6 | 0 |
| [State space, stability and optimal control](#02-state-space-optimal) | 6 | 0 |
| [Robust control](#03-robust) | 2 | 0 |
| [Adaptive and nonlinear control](#04-adaptive-nonlinear) | 4 | 0 |
| [Model predictive control](#05-mpc) | 2 | 0 |
| [State estimation](#06-estimation) | 9 | 0 |
| [Learning-based and data-driven control](#07-learning-control) | 10 | 5 |
| [Learning-based estimation](#08-learning-estimation) | 3 | 2 |

<a id="00-surveys"></a>
## Surveys and overview papers

Where control and learning meet; industrial practice surveys.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2001 | **The Future of PID Control**<br>K. J. Astrom, T. Hagglund | Control Engineering Practice 9(11) | [link](https://doi.org/10.1016/S0967-0661(01)00062-4) | State of PID practice; about 90% of loops are PID. |
| 2003 | **A Survey of Industrial Model Predictive Control Technology**<br>S. J. Qin, T. A. Badgwell | Control Engineering Practice 11 | [link](https://doi.org/10.1016/S0967-0661(02)00186-7) | History and vendor survey of industrial MPC. |
| 2017 | **A Survey on Industry Impact and Challenges Thereof**<br>T. Samad | IEEE Control Systems Magazine 37(1) | [link](https://doi.org/10.1109/MCS.2016.2621438) | IFAC industry survey: PID rated highest impact (91% 'high'), then MPC. |
| 2019 | **A Tour of Reinforcement Learning: The View from Continuous Control**<br>B. Recht | Annual Review of Control, Robotics, and Autonomous Systems | [PDF](papers/00-surveys/recht2019tour.pdf) · [arXiv](https://arxiv.org/abs/1806.09460) | RL measured against LQR; sample complexity of model-free vs model-based. |
| 2020 | **Learning-Based Model Predictive Control: Toward Safe Learning in Control**<br>L. Hewing, K. P. Wabersich, M. Menner, M. N. Zeilinger | Annual Review of Control, Robotics, and Autonomous Systems | [link](https://doi.org/10.1146/annurev-control-090419-075625) | Learning the model, the cost, or a safety filter inside MPC. |
| 2022 | **Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning**<br>L. Brunke et al. | Annual Review of Control, Robotics, and Autonomous Systems | [PDF](papers/00-surveys/brunke2022safe.pdf) · [arXiv](https://arxiv.org/abs/2108.06266) | Taxonomy of safe learning-based control. |
| 2026 | **Synthesis of Model Predictive Control and Reinforcement Learning: Survey and Classification**<br>R. Reiter, J. Hoffmann et al. | Annual Reviews in Control | [PDF](papers/00-surveys/reiter2026synthesis.pdf) · [arXiv](https://arxiv.org/abs/2502.02133) | How MPC and RL are combined. |

<a id="01-classical-feedback"></a>
## Classical feedback and frequency-domain control

Governors, PID, the feedback amplifier, Nyquist and Bode.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1868 | **On Governors**<br>J. C. Maxwell | Proceedings of the Royal Society of London | [link](https://doi.org/10.1098/rspl.1867.0055) | First stability analysis of a feedback mechanism. |
| 1922 | **Directional Stability of Automatically Steered Bodies**<br>N. Minorsky | Journal of the American Society for Naval Engineers | [link](https://doi.org/10.1111/j.1559-3584.1922.tb04958.x) | Three-term (PID) ship steering control. |
| 1932 | **Regeneration Theory**<br>H. Nyquist | Bell System Technical Journal | [link](https://doi.org/10.1002/j.1538-7305.1932.tb02344.x) | The Nyquist stability criterion. |
| 1934 | **Stabilized Feedback Amplifiers**<br>H. S. Black | Bell System Technical Journal | [link](https://doi.org/10.1002/j.1538-7305.1934.tb00652.x) | Negative feedback trades gain for robustness. |
| 1940 | **Relations Between Attenuation and Phase in Feedback Amplifier Design**<br>H. W. Bode | Bell System Technical Journal | [link](https://doi.org/10.1002/j.1538-7305.1940.tb00839.x) | Gain-phase relations and margins. |
| 1942 | **Optimum Settings for Automatic Controllers**<br>J. G. Ziegler, N. B. Nichols | Transactions of the ASME | [link](https://doi.org/10.1115/1.4019264) | Ziegler-Nichols PID tuning rules. |

<a id="02-state-space-optimal"></a>
## State space, stability and optimal control

Lyapunov stability, LQR/LQG, guaranteed margins.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1957 | **Dynamic Programming**<br>R. Bellman | Princeton University Press (book) |  | The principle of optimality and the Bellman equation. |
| 1960 | **Contributions to the Theory of Optimal Control**<br>R. E. Kalman | Boletin de la Sociedad Matematica Mexicana |  | LQR, controllability, the state-space view. |
| 1962 | **The Mathematical Theory of Optimal Processes**<br>L. S. Pontryagin, V. G. Boltyanskii, R. V. Gamkrelidze, E. F. Mishchenko | Interscience (book; Russian edition 1961) |  | Pontryagin's maximum principle. |
| 1977 | **Gain and Phase Margin for Multiloop LQG Regulators**<br>M. G. Safonov, M. Athans | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/TAC.1977.1101470) | LQR state feedback: at least 6 dB gain and 60 deg phase margin. |
| 1978 | **Guaranteed Margins for LQG Regulators**<br>J. C. Doyle | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/TAC.1978.1101812) | Abstract: 'There are none.' The start of robust control. |
| 1992 | **The General Problem of the Stability of Motion (1892; English translation 1992)**<br>A. M. Lyapunov | International Journal of Control | [link](https://doi.org/10.1080/00207179208934253) | Lyapunov's direct method. |

<a id="03-robust"></a>
## Robust control

Sensitivity, H-infinity, the limits of LQG.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1981 | **Feedback and Optimal Sensitivity: Model Reference Transformations, Multiplicative Seminorms, and Approximate Inverses**<br>G. Zames | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/TAC.1981.1102603) | Founding H-infinity paper. |
| 1989 | **State-Space Solutions to Standard H2 and H-infinity Control Problems**<br>J. C. Doyle, K. Glover, P. P. Khargonekar, B. A. Francis | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/9.29425) | Riccati-based H-infinity synthesis (DGKF). |

<a id="04-adaptive-nonlinear"></a>
## Adaptive and nonlinear control

Self-tuning regulators, sliding modes, neural network control, iterative learning control.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1973 | **On Self Tuning Regulators**<br>K. J. Astrom, B. Wittenmark | Automatica | [link](https://doi.org/10.1016/0005-1098(73)90073-3) | Recursive identification + control design. |
| 1977 | **Variable Structure Systems with Sliding Modes**<br>V. Utkin | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/TAC.1977.1101446) | Sliding-mode control. |
| 1990 | **Identification and Control of Dynamical Systems Using Neural Networks**<br>K. S. Narendra, K. Parthasarathy | IEEE Transactions on Neural Networks | [link](https://doi.org/10.1109/72.80202) | Early neural-network adaptive control. |
| 2006 | **A Survey of Iterative Learning Control**<br>D. A. Bristow, M. Tharayil, A. G. Alleyne | IEEE Control Systems Magazine | [link](https://doi.org/10.1109/MCS.2006.1636313) | Learning from repeated trials, a pre-deep-learning 'learning control'. |

<a id="05-mpc"></a>
## Model predictive control

From industrial heuristics to stability theory, industry surveys.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1978 | **Model Predictive Heuristic Control**<br>J. Richalet, A. Rault, J. L. Testud, J. Papon | Automatica | [link](https://doi.org/10.1016/0005-1098(78)90001-8) | Early industrial MPC (IDCOM). |
| 2000 | **Constrained Model Predictive Control: Stability and Optimality**<br>D. Q. Mayne, J. B. Rawlings, C. V. Rao, P. O. M. Scokaert | Automatica | [link](https://doi.org/10.1016/S0005-1098(99)00214-9) | Terminal costs and sets: the stability theory of MPC. |

<a id="06-estimation"></a>
## State estimation

Kalman, Kalman-Bucy, RTS smoothing, unscented and particle filters, moving-horizon estimation.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1960 | **A New Approach to Linear Filtering and Prediction Problems**<br>R. E. Kalman | Journal of Basic Engineering | [link](https://doi.org/10.1115/1.3662552) | The discrete Kalman filter. |
| 1961 | **New Results in Linear Filtering and Prediction Theory**<br>R. E. Kalman, R. S. Bucy | Journal of Basic Engineering | [link](https://doi.org/10.1115/1.3658902) | Continuous-time Kalman-Bucy filter; duality with control. |
| 1965 | **Maximum Likelihood Estimates of Linear Dynamic Systems (RTS smoother)**<br>H. E. Rauch, F. Tung, C. T. Striebel | AIAA Journal | [link](https://doi.org/10.2514/3.3166) | Fixed-interval smoothing. |
| 1985 | **Discovery of the Kalman Filter as a Practical Tool for Aerospace and Industry**<br>L. A. McGee, S. F. Schmidt | NASA TM-86847 | [link](https://ntrs.nasa.gov/citations/19860003843) | The extended Kalman filter's origin in Apollo navigation studies. |
| 1993 | **Novel Approach to Nonlinear/Non-Gaussian Bayesian State Estimation**<br>N. J. Gordon, D. J. Salmond, A. F. M. Smith | IEE Proceedings F | [link](https://doi.org/10.1049/ip-f-2.1993.0015) | The bootstrap particle filter. |
| 1997 | **New Extension of the Kalman Filter to Nonlinear Systems**<br>S. J. Julier, J. K. Uhlmann | SPIE Proceedings | [link](https://doi.org/10.1117/12.280797) | The unscented transform and filter. |
| 2000 | **The Unscented Kalman Filter for Nonlinear Estimation**<br>E. A. Wan, R. van der Merwe | IEEE AS-SPCC Symposium | [link](https://doi.org/10.1109/ASSPCC.2000.882463) | UKF for state and parameter estimation. |
| 2003 | **Constrained State Estimation for Nonlinear Discrete-Time Systems: Stability and Moving Horizon Approximations**<br>C. V. Rao, J. B. Rawlings, D. Q. Mayne | IEEE Transactions on Automatic Control | [link](https://doi.org/10.1109/TAC.2002.808470) | Moving-horizon estimation: optimization-based estimation with constraints. |
| 2004 | **Unscented Filtering and Nonlinear Estimation**<br>S. J. Julier, J. K. Uhlmann | Proceedings of the IEEE | [link](https://doi.org/10.1109/JPROC.2003.823141) | The definitive UKF review. |

<a id="07-learning-control"></a>
## Learning-based and data-driven control

Learning MPC, safe RL, neural Lyapunov functions, Koopman and SINDy, DeePC, differentiable MPC, RL on real plants.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 1931 | **Hamiltonian Systems and Transformation in Hilbert Space**<br>B. O. Koopman | PNAS | [link](https://doi.org/10.1073/pnas.17.5.315) | The Koopman operator: nonlinear dynamics as linear dynamics on observables. |
| 2005 | **A Note on Persistency of Excitation (fundamental lemma)**<br>J. C. Willems, P. Rapisarda, I. Markovsky, B. L. M. De Moor | Systems & Control Letters | [link](https://doi.org/10.1016/j.sysconle.2004.09.003) | One rich trajectory spans all trajectories of an LTI system. |
| 2016 | **Discovering Governing Equations from Data by Sparse Identification of Nonlinear Dynamical Systems (SINDy)**<br>S. L. Brunton, J. L. Proctor, J. N. Kutz | PNAS | [PDF](papers/07-learning-control/brunton2016sindy.pdf) · [arXiv](https://arxiv.org/abs/1509.03580) | Sparse regression over a function library. |
| 2017 | **Safe Model-based Reinforcement Learning with Stability Guarantees**<br>F. Berkenkamp, M. Turchetta, A. P. Schoellig, A. Krause | NeurIPS | [PDF](papers/07-learning-control/berkenkamp2017safe.pdf) · [arXiv](https://arxiv.org/abs/1705.08551) | GP models + Lyapunov regions of attraction for safe exploration. |
| 2018 | **Differentiable MPC for End-to-end Planning and Control**<br>B. Amos, I. D. J. Rodriguez, J. Sacks, B. Boots, J. Z. Kolter | NeurIPS | [PDF](papers/07-learning-control/amos2018diffmpc.pdf) · [arXiv](https://arxiv.org/abs/1810.13400) | MPC as a differentiable layer. |
| 2018 | **Deep Learning for Universal Linear Embeddings of Nonlinear Dynamics**<br>B. Lusch, J. N. Kutz, S. L. Brunton | Nature Communications | [arXiv](https://arxiv.org/abs/1712.09707) | Deep Koopman embeddings. |
| 2019 | **Neural Lyapunov Control**<br>Y.-C. Chang, N. Roohi, S. Gao | NeurIPS | [arXiv](https://arxiv.org/abs/2005.00611) | Learning a controller and a neural Lyapunov function with verification. |
| 2019 | **Data-Enabled Predictive Control: In the Shallows of the DeePC**<br>J. Coulson, J. Lygeros, F. Dorfler | ECC | [PDF](papers/07-learning-control/coulson2019deepc.pdf) · [arXiv](https://arxiv.org/abs/1811.05890) | Predictive control directly from Hankel matrices of data. |
| 2019 | **Cautious Model Predictive Control using Gaussian Process Regression**<br>L. Hewing, J. Kabzan, M. N. Zeilinger | IEEE Transactions on Control Systems Technology | [PDF](papers/07-learning-control/hewing2019cautious.pdf) · [arXiv](https://arxiv.org/abs/1705.10702) | GP-corrected dynamics with uncertainty-aware constraints. |
| 2022 | **Magnetic Control of Tokamak Plasmas through Deep Reinforcement Learning**<br>J. Degrave et al. | Nature | [link](https://doi.org/10.1038/s41586-021-04301-9) | One RL policy driving all 19 TCV coils, trained in simulation. |

<a id="08-learning-estimation"></a>
## Learning-based estimation

Deep and differentiable Kalman filters, learned gains.

| Year | Paper | Venue | Links | Why it is here |
|---:|---|---|---|---|
| 2015 | **Deep Kalman Filters**<br>R. G. Krishnan, U. Shalit, D. Sontag | arXiv | [arXiv](https://arxiv.org/abs/1511.05121) | Learned nonlinear state-space models with variational inference. |
| 2016 | **Backprop KF: Learning Discriminative Deterministic State Estimators**<br>T. Haarnoja, A. Ajay, S. Levine, P. Abbeel | NeurIPS | [PDF](papers/08-learning-estimation/haarnoja2016backpropkf.pdf) · [arXiv](https://arxiv.org/abs/1605.07148) | End-to-end training through a Kalman filter. |
| 2022 | **KalmanNet: Neural Network Aided Kalman Filtering for Partially Known Dynamics**<br>G. Revach et al. | IEEE Transactions on Signal Processing | [PDF](papers/08-learning-estimation/revach2022kalmannet.pdf) · [arXiv](https://arxiv.org/abs/2107.10043) | Keep the KF structure, learn the gain with an RNN. |
