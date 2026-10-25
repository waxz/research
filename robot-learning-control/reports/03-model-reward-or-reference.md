# Model, reward, or reference? Comparing robot control paradigms

*Markdown edition of [`html/model-reward-or-reference.html`](html/model-reward-or-reference.html), which has the figures and the decision flowchart. The fit ratings and task map are a synthesis of the surveys in [../CATALOG.md](../CATALOG.md#01-surveys), not measured results.*

Every controller gets its knowledge of what to do from somewhere. This note groups methods by that source:

| Family | Knowledge source | Examples |
|---|---|---|
| **MB:** model-based control | Equations of motion + cost | PID, LQR, trajectory optimization, MPC, whole-body QP |
| **RL:** self-exploration RL | Reward + trial and error (usually in simulation) | PPO with domain randomization |
| **REF:** supervised / reference learning | Demonstrations or reference motions | Behavior cloning, DAgger, teacher–student, inverse RL / GAIL, reference-tracking RL |

"Supervised RL" isn't a standard term. Here it covers every method where the learning signal comes from examples instead of, or on top of, a task reward.

## 1. Why robot control is hard

$$M(q)\ddot q+C(q,\dot q)\dot q+g(q)=S^\top\tau+\sum_{c\in\mathcal C(t)}J_c^\top\lambda_c,\qquad 0\le\lambda_{c,n}\perp\phi_c(q)\ge0,\quad\|\lambda_{c,t}\|\le\mu\lambda_{c,n}$$

| Source of difficulty | Hits hardest |
|---|---|
| High dimension (G1: 29 joints + 6 base DoF → 70-D state) | MB needs reduced models; RL pays in samples |
| Underactuation (the base has no motor; $S$ has no base rows) | All |
| Hybrid, non-smooth contact; combinatorial contact schedules | MB (fixed gait schedules), differentiable simulation (biased gradients, Suh 2022) |
| Friction cone with unknown μ; unknown payloads | All; motivates domain randomization |
| Partial observability, sensor noise, actuator limits and delay | All |
| Real-time budget (policy 50 Hz, PD 0.5–1 kHz, MPC 30–1000 Hz) | MB (online solve) |
| Sim-to-real gap | RL and REF trained in simulation |
| Specifying the goal; reward hacking | RL |
| Safety and hardware wear in real trials | Real-world RL (Dulac-Arnold 2021) |

## 2. Three paradigms

**MPC:**

$$\min_{u}\sum_{k=0}^{N-1}\ell(x_k,u_k)+\ell_f(x_N)\quad\text{s.t. } x_{k+1}=f(x_k,u_k),\ h(x_k,u_k)\le0$$

**Domain-randomized RL:**

$$\max_\theta\ \mathbb E_{\xi\sim p(\xi)}\mathbb E_{\tau\sim\pi_\theta,\xi}\Big[\sum_t\gamma^t r_t\Big]$$

**Behavior cloning and compounding error:**

$$\min_\theta\ \mathbb E_{\mathcal D}[-\log\pi_\theta(a|o)],\qquad J(\hat\pi)\le J(\pi^*)+T^2\epsilon\ \text{(BC)}\ \text{vs.}\ J(\pi^*)+uT\epsilon\ \text{(DAgger)}$$

| Criterion | MB | RL | REF |
|---|---|---|---|
| Offline cost | Low (expert modelling) | High (10⁸–10¹⁰ simulator steps, reward design) | Data collection + training |
| Online cost | High (optimize every 1–30 ms) | Very low (one forward pass) | Low (MLP) to high (VLA) |
| Constraints and safety | Explicit, with formal tools | Penalties only | Inherited from demos |
| Model mismatch | Sensitive | Robust with domain randomization | Covariate shift |
| Contact-rich, high-DoF | Hard | Strong | Good if data covers it |
| Behavior quality | Optimal for the cost; can look robotic | Novel and agile; may be unnatural | Natural; capped by data |
| Interpretability | High | Low | Low |

The surveys agree that the field is moving toward hybrids (Reiter 2026; Ha 2025; Hewing 2020). Examples include DTC (RL tracking trajectory-optimization plans), residual RL, TD-MPC and SuperMimic. Song et al. (2023) found that RL beats optimal control in drone racing because it *optimizes a better objective*, not because it optimizes better.

## 3. Reference-based RL vs self-exploration RL

Self-exploration reward (typical locomotion):

$$r_t=w_v e^{-\|v^{\mathrm{cmd}}-v\|^2/\sigma^2}-w_\tau\|\tau\|^2-w_a\|a_t-a_{t-1}\|^2+\text{hand-tuned shaping}$$

Reference reward (DeepMimic family):

$$r_t=w^I\sum_k w_k\exp(-\|x^{\mathrm{ref}}_k-x_k\|^2/\sigma_k^2)+w^G r^{\mathrm{goal}}_t$$

AMP sits between the two: a discriminator gives a style reward, $r=\max[0,1-0.25(D(s,s')-1)^2]$.

Methods sit on a spectrum: **behavior cloning → reference-tracking RL → style prior or demo-guided RL → shaped task reward → sparse task reward.** Moving right gives more novelty and needs less data, but exploration and reward design get harder. Moving left gives more natural, predictable motion and faster training, but performance is capped by the reference.

| Dimension | Reference-based RL | Self-exploration RL |
|---|---|---|
| Reward design | One generic tracking reward for thousands of clips | Many per-skill shaping terms; reward hacking |
| Exploration | Guided by reference-state initialization; dense reward; acrobatics learnable | Hard for long-horizon or acrobatic skills |
| Data | Mocap + retargeting + filtering (~9% of BONES-SEED dropped) | None beyond the simulator |
| Motion quality | Human-like | Often jittery or odd (Heess 2017) |
| Ceiling | Human motion, not robot-optimal | Can beat humans (Swift, Kaufmann 2023) |
| Task generality | Needs a task layer on top | Solves the scored task directly |
| Compute | Scales with library size (SONIC ~21k GPU-h; SuperMimic ~3) | Minutes for locomotion (Rudin 2022); much more for dexterity |

In practice, references set what the motion looks like and rewards set what it achieves.

## 4. Which method for which task

| | Tractable model | Simulatable, too complex to optimize online | Hard to simulate |
|---|---|---|---|
| **Easy to score** | **MB:** industrial arms, spacecraft, flat-ground quadruped MPC, process control | **RL + DR:** rough terrain, parkour, drone racing, in-hand reorientation | Real-world / offline RL (QT-Opt), residual RL |
| **Easier to show** | Learning from demonstration + MB execution (DMP, kinesthetic teaching) | **REF-RL:** humanoid tracking, dance, teleoperation, AMP gaits | **Imitation / VLA:** cloth folding, cooking, household tasks |

| Task | Best-suited approach | Representative work |
|---|---|---|
| Industrial pick-and-place, welding | MB + demos for programming | Industrial practice |
| Quadruped, flat terrain | MB convex MPC + WBC, or RL | Di Carlo 2018; Kim 2019; Rudin 2022 |
| Quadruped, rough terrain and parkour | RL + DR + teacher–student | Lee 2020; Miki 2022; Cheng 2024; Zhuang 2023 |
| Humanoid robust locomotion | RL, often with a style prior | Radosavovic 2024 |
| Humanoid expressive motion, teleoperation | Reference-tracking RL | H2O; BeyondMimic; SONIC; SuperMimic |
| Dexterous in-hand manipulation | RL with heavy DR; demos to speed up | OpenAI 2019; DAPG |
| Contact-rich assembly | Impedance control + residual RL or demos | Johannink 2019 |
| Household manipulation, deformables | Imitation (diffusion policy, VLA) | Chi 2023; ALOHA; π0 |
| Drone racing | RL; MB for known trajectories | Kaufmann 2023; Song 2023 |
| Autonomous driving | Large-scale imitation + MB safety layers | IL surveys |
| Surgical robots | MB + teleoperation; REF for sub-tasks | Brunke 2022 |
| Process and energy | MPC, RL for tuning | Reiter 2026; Hewing 2020 |

**Decision rule:**
1. If formal guarantees are needed, use MB.
2. Otherwise, if there is a tractable model that can be solved in real time, start with MB.
3. Otherwise, if the system can't be simulated faithfully, use imitation learning.
4. Otherwise, if the goal is easier to score than to show, use self-exploration RL with domain randomization and distill to a deployable student.
5. Otherwise, use reference-based RL with a task layer on top. Also switch to it when RL motion looks unnatural or hacks the reward.
