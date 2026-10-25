# SuperMimic: overview, contribution and challenges

*Research note, October 2026. Sources: [arXiv:2610.28480](https://arxiv.org/abs/2610.28480), [project page](https://supermimic.github.io/). Local copy: [PDF](../papers/00-supermimic/liao2026supermimic.pdf).*

**Paper.** Q. Liao, Y. Shao, J. Long, K. Zakka, R. Horowitz, P. Abbeel, K. Sreenath (UC Berkeley). *SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model.* CoRL 2026 (oral). arXiv v1, 20 Oct 2026.

**News status (25 Oct 2026).** No press coverage yet. There are listings on alphaXiv, Emergent Mind and papers.cool, plus several unofficial community reimplementations on GitHub (`Go-Youngster/supermimic-reproduce`, `Shimingyi/allmimic`, `YanYuan98/Supermimic_mod`, `lzyang2000/morphmimic`). The authors have not endorsed any of them.

## Main contribution

Training one humanoid policy to track a whole motion-capture library has been done two ways, both expensive. One is to distill many per-motion PPO experts into a single policy, which loses information. The other is to train one PPO policy with cluster-scale compute. SONIC, the main baseline, used 128 GPUs for 7 days, about 21,000 GPU-hours.

SuperMimic learns **one differentiable world model** of the shared humanoid dynamics instead. The model is fit online from transitions logged by MuJoCo Warp. The policy is trained by **backpropagation through time (BPTT) over 32-step imagined rollouts**, and a critic bootstraps the return beyond the horizon. Gradients never pass through the simulator, so its non-smooth contacts are not a problem.

| Reported result | Value |
|---|---|
| Time to beat SONIC's normalized return (0.90) | 3 h on one H100 |
| GPU-hours | ~3 vs ~21,000 (> 1000× fewer) |
| Failed motions (129,514 clips) | 25 at 3 h; 0 after 9.8 h on 2 GPUs; SONIC 179 |
| World-model 8-step error, 1 → 264 h of data | stable, 0.007–0.011 |
| Analytic gradients vs PPO in the same world model | ~64× fewer imagined steps |
| Hardware | One policy on a real Unitree G1 (skipping jump, side roll, 90° and 360° flips) |

## Challenges and caveats

- **Mismatched comparison:** different GPUs (H100 vs L40) and data (264.56 h public BONES-SEED vs SONIC's 611 h). The controlled LAFAN1 test (SuperMimic return 0.82 in 1.2 h; PPO in the simulator ends at 0.60/0.70/0.72 on 1/4/8 GPUs after 18 h) is the cleanest evidence.
- **Coverage, not generalization:** the benchmark motions are the training motions.
- **Bounded by model accuracy:** the model is deterministic, so random pushes were removed from training. Changed conditions such as friction have to be passed to the model as inputs.
- **Horizon:** without the critic, training fails at H ≤ 16. Beyond H = 64, training gets slower and the final result worse.
- **Scope:** flat ground only, simulator data only. Multi-interface training is still preliminary.
- **Not yet reproduced:** it is a preprint with one main baseline and no independent reproduction.

## Comparison with traditional pipelines

| Aspect | Model-free RL (PPO, e.g. SONIC) | Supervised distillation (experts → student) | SuperMimic |
|---|---|---|---|
| Gradient signal | Sampled likelihood-ratio, high variance | Supervised regression to expert actions | Analytic gradient through learned model |
| Dynamics | Black-box simulator | None (experts hold it) | One shared differentiable model |
| Compute | ~21k GPU-h | Many experts + distillation | ~3 GPU-h |
| Scaling with motions | More GPUs | Expert count grows; lossy merge | Shared model; error stays flat |
| Main weakness | Slow, noisy | Errors compound off-distribution; capped by the teachers | Model accuracy; short horizon; needs critic |

See [02-supermimic-method-and-history.md](02-supermimic-method-and-history.md) for the equations and [03-model-reward-or-reference.md](03-model-reward-or-reference.md) for the broader comparison of control paradigms.
