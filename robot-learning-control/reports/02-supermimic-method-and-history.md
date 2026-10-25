# SuperMimic explained: method, equations and history

*Markdown edition of the illustrated page [`html/supermimic-explained.html`](html/supermimic-explained.html), which has the diagrams. Equations (1)–(3) and all hyperparameters come from [arXiv:2610.28480v1](https://arxiv.org/abs/2610.28480). The adjoint expansion in §3 is this note's own illustration.*

## 1. Problem setup

The setup is a goal-conditioned POMDP on a Unitree G1 (29 joints). The policy is deterministic:

$$a_t = \pi_\theta(o_t, g_t),\qquad o_t = \bar o_t + \eta_t,\qquad q^{\mathrm{sp}} = \alpha a_t + q^0$$

- $o_t$: proprioception (joint positions and velocities, IMU angular velocity, projected gravity, previous action), with a history of 10 frames.
- $g_t$: the next $K=10$ reference frames.
- $a_t$: a low-gain PD set-point, which acts as a proxy for torque.

Returns use a soft survival weight, so that predicted terminations stay differentiable:

$$c_0=1,\quad c_{t+1}=c_t(1-d_{t+1}),\qquad J(\theta)=\mathbb E\Big[\sum_{t\ge0}\gamma^t c_t r_{t+1}\Big]$$

The reward is BeyondMimic's tracking reward: Gaussian kernels on body position (σ = 0.3 m), orientation (0.4 rad), linear velocity (1.0 m/s) and angular velocity (3.14 rad/s), each with weight 1.0, plus root position and orientation terms (0.5 each), an action-smoothness penalty (−0.1) and a joint-limit penalty (−2). The self-collision penalty is removed because a deterministic policy cannot exploit noise suppression.

## 2. World model

The simulator's randomness has known sources: the sim context $\xi$ (friction μ ∈ [0.3, 1.2], joint offsets, torso centre-of-mass offset) and the sensor noise $\eta$. The model can therefore be deterministic:

$$\hat s_{t+1}=f_\omega(\hat s_t,a_t,\xi),\quad \hat r_{t+1}=r_\omega(\hat s_t,a_t,g_t),\quad \hat{\bar o}_t=g_\omega(\hat s_t,\xi),\quad \hat d_t=d_\omega(\hat s_t,g_t)$$

**Eq. 1** fits the model on 8-step autoregressive windows taken from the replay buffer:

$$\mathcal L_{\mathrm{WM}}(\omega)=\mathbb E_{\mathcal B}\Big[\sum_{j=1}^{k}\|\hat s_j-s_j\|^2+(\hat r_j-r_j)^2+\|\hat{\bar o}_j-\bar o_j\|^2+\mathrm{BCE}(\hat d_j,d_j)\Big],\quad \hat s_0=s_0,\ k=8$$

$f_\omega$ is an MLP with three hidden layers of 2048 units. Its rollouts are more than 10× faster than MuJoCo Warp at 2k–16k environments, and 62× faster at 64k.

## 3. Policy learning through imagination

**Eq. 2** is the imagined objective, over $H=32$ steps with a critic tail:

$$\hat J(\theta)=\mathbb E_{s_0\sim\rho_0}\Big[\sum_{t=0}^{H-1}\gamma^t\hat c_t\hat r_{t+1}+\gamma^H\hat c_H V_\psi(\hat s_H,g_H,\xi)\Big],\qquad a_t=\pi_\theta(\hat{\bar o}_t+\eta_t,g_t)$$

PPO uses the zeroth-order likelihood-ratio estimator, $\nabla_\theta J\approx\frac1N\sum\nabla_\theta\log\pi_\theta(a|s)\hat A$. SuperMimic differentiates the return pathwise instead. With the adjoint $\lambda_t=\partial\hat J/\partial\hat s_t$ (illustrative expansion, termination terms omitted):

$$\nabla_\theta\hat J=\sum_{t}\Big(\gamma^t\hat c_t\tfrac{\partial\hat r_{t+1}}{\partial a_t}+\lambda_{t+1}\tfrac{\partial f_\omega}{\partial a_t}\Big)\tfrac{\partial\pi_\theta}{\partial\theta},\qquad
\lambda_t=\gamma^t\hat c_t\tfrac{\partial\hat r_{t+1}}{\partial\hat s_t}+\lambda_{t+1}\Big(\tfrac{\partial f_\omega}{\partial\hat s_t}+\tfrac{\partial f_\omega}{\partial a_t}\tfrac{\partial\pi_\theta}{\partial o}\tfrac{\partial g_\omega}{\partial\hat s_t}\Big)$$

**Eq. 3** is the critic, fit to λ-returns computed backward over the imagined rollout:

$$\hat R_t=\hat r_{t+1}+\gamma(1-\hat d_{t+1})\big[(1-\lambda)V_{t+1}+\lambda\hat R_{t+1}\big],\quad \hat R_H=V_H,\qquad \mathcal L_V=\mathbb E\sum_t(V_t-\hat R_t)^2$$

| Horizon H | No critic | With critic |
|---|---|---|
| 8 | fails to reach return 0.82 | fails |
| 16 | fails | matches no-critic H = 32 |
| **32 (default)** | reaches 0.82 | fastest |
| 64 → 128 | ~3× slower, lower final return | same |

**Training loop** (320k iterations):
1. Collect data in 4096 simulator envs per GPU, with action noise 𝒩(0, 0.1²).
2. Reset episodes by return-based sampling: 50% uniform over 1-s bins, 40% from softmax(−25 G/Gmax), 10% by historical weight.
3. Fit the world model (Eq. 1).
4. Run BPTT on 4096 imagined rollouts (Adam with β = (0.9, 0.95); gradients clipped to global norm 1.0, then element-wise to 0.1).
5. Fit the critic (γ = 0.99, λ = 0.95, 5 epochs).

The update-to-data ratio is 0.4. Downstream interfaces share one decoder: $z=\mathrm{enc}_{\theta,i}(g)$, $a=\mathrm{dec}_\theta(z,o)$. In a preliminary study, an RL-trained velocity encoder beat distillation on 650 of 672 commands.

## 4. How we got here

| Period | Idea | Key works |
|---|---|---|
| 1957–1992 | Bellman optimality, Dyna (imagined experience), REINFORCE | Bellman; Sutton 1991; Williams 1992 |
| 2011–2015 | Analytic gradients through models | PILCO; Stochastic Value Gradients |
| 2015–2018 | Deep model-free RL | DQN, TRPO, DDPG, GAE, PPO, SAC |
| 2018–2021 | Motion imitation for characters | DeepMimic, NPMP, AMP, SuperTrack (BPTT through a learned model) |
| 2017–2022 | Learned world models; sim-to-real with domain randomization and GPU simulation | World Models, MBPO, Dreamer; Tobin, Peng; Hwangbo, Isaac Gym, legged_gym |
| 2022–2025 | Differentiable simulation with actor-critic; contact-gradient pathologies; learned dynamics for characters and robots | SHAC; Suh et al.; ControlVAE, MoConVQ, SuperDyno; Song 2024; RWM; DreamerV3 |
| 2023–2026 | Humanoid tracking on hardware at scale | PHC, H2O/OmniH2O, ExBody, HumanPlus, ASAP, BeyondMimic, SONIC |
| Oct 2026 | One learned differentiable world model + short-horizon BPTT for humanoid tracking | SuperMimic |

Key equations along the way:

- Bellman: $Q^*(s,a)=\mathbb E[r+\gamma\max_{a'}Q^*(s',a')]$
- PPO: $L^{\mathrm{CLIP}}=\mathbb E[\min(\rho_t\hat A_t,\mathrm{clip}(\rho_t,1\pm\epsilon)\hat A_t)]$
- DeepMimic: $r_t=0.65r^p+0.1r^v+0.15r^e+0.1r^c$, with $r^p=\exp[-2\sum_j\|\hat q_j\ominus q_j\|^2]$
- SHAC: $\mathcal L=-\frac1{Nh}\sum_i[\sum_{t=t_0}^{t_0+h-1}\gamma^{t-t_0}r_t+\gamma^hV(s_{t_0+h})]$
- Teacher–student DAgger: $\min_\phi\mathbb E_{s\sim d^{\pi_\phi}}\|\pi_\phi(o)-\pi^{\mathrm{teacher}}(s)\|^2$

Every work mentioned here is listed with links in [../CATALOG.md](../CATALOG.md).
