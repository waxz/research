# Robot learning breakthroughs, 2010–2026

*Markdown edition of [`html/robot-learning-breakthroughs.html`](html/robot-learning-breakthroughs.html). This lists one breakthrough per year, chosen for how much it changed what robots could do the following year. Quantitative figures were checked against paper abstracts or primary press releases on 25 Oct 2026.*

Paradigm: **MB** = model-based control / simulation, **RL** = self-exploration reinforcement learning, **REF** = imitation, demonstrations or reference motion.

## Roots before 2010

| Year | Milestone | Why it matters later |
|---|---|---|
| 1957–60 | Bellman dynamic programming; Kalman filter and LQR | The math later methods approximate |
| 1986 | Raibert's hopping robots (MB) | Dynamic balance; lineage of BigDog, Spot, Atlas |
| 1989–92 | Q-learning, REINFORCE, TD-Gammon (RL) | Value-based and policy-gradient RL |
| 2000 | Honda ASIMO, ZMP walking (MB) | Precise-model humanoid walking, but brittle |
| 2004 | Kohl & Stone, policy-gradient Aibo gait (RL) | RL on hardware beats hand-tuned gaits |
| 2004–06 | Ng et al., inverted helicopter flight via RL | RL in a learned model |
| 2005 | Stanley wins the DARPA Grand Challenge | Learned perception + classical control, deployed |
| 2008 | BigDog (MB) | The rough-terrain bar RL later had to clear |

## Year by year

| Year | Breakthrough | Bottleneck it answered | Evidence / experiment | Real-world reach |
|---|---|---|---|---|
| 2010 | Apprenticeship learning for helicopter aerobatics (REF) | Hand-designed control can't do edge-of-envelope maneuvers | Abbeel, Coates & Ng (IJRR 2010): flips, rolls, tic-tocs and chaos at expert-pilot level | Learning from demonstration for agile vehicles |
| 2011 | PILCO (MB); also DAgger | Real trials expensive; model bias | Real cart-pole learned from seconds of interaction; DAgger makes imitation error grow linearly, not quadratically | Small real systems; DAgger becomes the basis of teacher–student |
| 2012 | MuJoCo + online trajectory optimization (MB) | Slow, inaccurate contact simulation | Simulated humanoid get-up, balance and walking via near-real-time MPC (Tassa et al.) | Standard RL engine; MuJoCo Warp trains SuperMimic in 2026 |
| 2013 | Deep Q-Network (RL) | RL needed hand-made features | Beat prior methods on 6 of 7 Atari games, and a human expert on 3 | Started deep RL |
| 2014 | Contact-implicit trajectory optimization; guided policy search (MB) | Optimizers give trajectories, not policies | Neural policies supervised by trajectory optimizers, using far fewer samples | Optimizer-as-teacher pattern (later DTC, distillation) |
| 2015 | Deep RL for continuous control (TRPO, GAE, DDPG); DARPA Robotics Challenge Finals (MB/RL) | Deep RL limited to discrete actions; humanoids hand-built | DQN reaches human-professional level on about half of 49 games; simulated 3-D humanoid running; at the DRC, KAIST DRC-HUBO wins and many robots fall | Brittle model-based humanoids make learned controllers worth pursuing |
| 2016 | End-to-end visuomotor control; large-scale grasping (RL) | Separate perception and control; little real-robot learning | Cap onto bottle from pixels (92k-parameter CNN); 800k+ grasp attempts over 2 months on 6–14 robots | Robot learning is limited by data |
| 2017 | Domain randomization + PPO (RL) | Reality gap | Detector trained only on simulated images is accurate to 1.5 cm on real images (Tobin) | Default sim-to-real recipe for a decade |
| 2018 | Dactyl in-hand manipulation (RL); also DeepMimic, QT-Opt | Dexterity beyond model-based control | Up to 50 consecutive reorientations; ~100 simulated years in 50 h on 6,144 CPUs + 8 GPUs; QT-Opt reaches 96% real grasp success from 580k attempts | Sim-only RL transfers contact-rich skills |
| 2019 | Sim-to-real RL on a quadruped with a learned actuator net (RL) | Legged dynamics break sim-to-real | ANYmal more precise and efficient, faster than before, recovers from falls (Hwangbo) | Field shifts from MPC to RL for legs; also Rubik's cube (60% / 20% success) |
| 2020 | Privileged teacher → proprioceptive student (RL) | Unseen natural terrain | Zero-shot on mud, snow, rubble, vegetation, flowing water (Lee) | Same group in team CERBERUS, DARPA SubT winner 2021 |
| 2021 | Massively parallel GPU RL (RL) | Days of training per policy | Flat terrain in < 4 min, rough terrain in 20 min on one GPU, transferred to ANYmal (Rudin) | Learned locomotion standard on commercial quadrupeds; RMA, AMP |
| 2022 | Perceptive locomotion in the wild (RL) | Blind proprioceptive walking | Mt. Etzel: 2.2 km, 120 m climb, summit in 31 min (signpost 35), loop in 78 min, no falls (Miki) | Inspection quadrupeds in plants and mines; also SHAC, DayDreamer |
| 2023 | Swift drone racing (RL); Diffusion Policy and ACT (REF) | Beat humans in a real competition? Skills with no sim or reward? | Swift won 15 of 25 races against world champions, fastest lap by 0.5 s; Diffusion Policy +46.9% average over prior SOTA; ACT 80–90% success from 10 min of demos | RL where the task can be scored, imitation where it can be shown; Swift failed under unfamiliar lighting |
| 2024 | Learned humanoid control; generalist VLA (π0) (REF/RL) | Humanoids model-based; single-task manipulation | Real humanoid walks outdoors zero-shot (Radosavovic); π0 folds laundry, clears tables, assembles boxes | Humanoid companies move to learned control |
| 2025 | General motion trackers (BeyondMimic, ASAP) (REF) | One reward and policy per skill | Diverse dynamic motions on a real G1 from one recipe; Beijing half-marathon winner in 2:40:42, with a human pacer | Entertainment and teleoperation; public demos still show human assistance |
| 2026 | SONIC at scale; SuperMimic on one GPU (REF/RL/MB) | Library-scale PPO costs ~21k GPU-hours | SuperMimic beats SONIC's return in 3 GPU-hours; 25 vs 179 failed motions; real G1 flips (preprint, not reproduced) | Affordable scaling-law studies; flat ground only so far |

## The logic of the sequence

1. Hand-designed control can't fly aerobatics → **learn from demonstrations** (2010)
2. Real trials are expensive → **learn a model and optimize in it** (2011)
3. Learning loops need fast contact physics → **MuJoCo** (2012)
4. RL needs hand-made features → **deep end-to-end networks** (2013–15)
5. Model-based humanoids are brittle (DRC 2015) → **learned controllers on real robots** (2016)
6. Real data doesn't scale → **simulation + domain randomization** (2017–18)
7. Legged dynamics break transfer → **learned actuator models** (2019)
8. Unseen terrain → **privileged teacher → student** (2020) and **perception fusion** (2022)
9. Training takes days → **GPU-parallel simulation** (2021)
10. No simulator or reward for household tasks → **generative imitation and VLAs** (2023–24)
11. RL motion unnatural, one policy per skill → **reference tracking at library scale** (2025–26)
12. Library-scale PPO is too expensive → **analytic gradients through a learned world model** (2026)

## What the record shows

- **Models moved inside learning.** PILCO, guided policy search, learned actuator nets and SuperMimic's world model all put a model at the center of a learning system.
- **Data throughput set the pace from 2016 to 2023:** 800k real grasps, then 100 simulated years, then 20 minutes on one GPU.
- **Specifying behavior is now the bottleneck,** which has pushed the field toward demonstrations, motion libraries and language.
- **Every deployment has caveats:** Swift's lighting failures, the marathon pacer, SuperMimic's flat-ground limit.

Papers are listed in [../CATALOG.md](../CATALOG.md).
