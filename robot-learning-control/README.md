# Robot learning and control: SuperMimic and control paradigms

A research collection on **SuperMimic** (CoRL 2026) and on how model-based control, self-exploration reinforcement learning and reference/imitation learning compare for real robots. It holds three written reports, two illustrated HTML pages, and a catalog of 96 papers, 35 of them saved locally as PDFs.

## Start here

| Read | What it covers |
|---|---|
| [reports/01-supermimic-overview.md](reports/01-supermimic-overview.md) | What SuperMimic is, its reported results, caveats, and how it compares with PPO and distillation pipelines |
| [reports/02-supermimic-method-and-history.md](reports/02-supermimic-method-and-history.md) | The method with all equations (world model, BPTT objective, critic), training loop, and a timeline from classic RL to 2026 |
| [reports/03-model-reward-or-reference.md](reports/03-model-reward-or-reference.md) | Why robot control is hard; model-based vs RL vs imitation; reference-based vs self-exploration RL; which method fits which task |
| [reports/04-breakthrough-timeline.md](reports/04-breakthrough-timeline.md) | One breakthrough per year, 2010–2026: the bottleneck it solved, the experiment that proved it, and its real-world reach |
| [cookbook/COOKBOOK.md](cookbook/COOKBOOK.md) | The math behind all of it, in 39 self-contained recipes: linear algebra and optimization, classical control (PID, LQR, Kalman, MPC, whole-body QP, LIPM), ML, deep learning, RL (Bellman to PPO, world models, analytic gradients, imitation, sim-to-real) and motion tracking. Every worked example is reproduced by `cookbook/examples.py` |
| [CATALOG.md](CATALOG.md) | Every paper, grouped by topic, with year, venue, links, local PDF and a one-line reason it matters |

The HTML pages in [reports/html/](reports/html/) are the illustrated versions, with diagrams, rendered equations and a decision flowchart. GitHub shows HTML as source, so download them and open them in a browser. The equations load MathJax from a CDN, so they need an internet connection.

## Layout

```
robot-learning-control/
├── README.md                 this file
├── CATALOG.md                generated paper catalog (do not edit by hand)
├── catalog.json              source of truth for all papers and categories
├── catalog.csv               same catalog as a spreadsheet
├── reports/
│   ├── 01-supermimic-overview.md
│   ├── 02-supermimic-method-and-history.md
│   ├── 03-model-reward-or-reference.md
│   └── html/
│       ├── supermimic-explained.html
│       └── model-reward-or-reference.html
├── papers/                   local PDFs, one folder per category, named <citekey>.pdf
│   ├── 00-supermimic/                 3   SuperMimic, SONIC, BeyondMimic
│   ├── 01-surveys/                   22   survey and overview papers
│   ├── 02-rl-foundations/             2   PPO, GAE
│   ├── 03-model-based-rl/             2   MBPO, Dreamer
│   ├── 04-differentiable-simulation/  3   SVG, SHAC, Suh et al.
│   ├── 05-character-motion-imitation/ 2   DeepMimic, AMP
│   └── 09-imitation-learning/         1   DAgger
├── cookbook/
│   ├── COOKBOOK.md           the math cookbook (source)
│   ├── examples.py           runnable worked examples, NumPy only (python3 examples.py r08)
│   ├── build_html.py         renders COOKBOOK.md into cookbook.html
│   └── cookbook.html         rendered version with equations, diagrams and a recipe index
└── tools/
    └── build_catalog.py      regenerates CATALOG.md / catalog.csv and downloads PDFs
```

Categories 06–08 and 10 (humanoid control, legged locomotion, model-based control, dexterous and agile) are in the catalog as links only, to keep the repository small.

## Key surveys

| Topic | Survey | PDF |
|---|---|---|
| Model-based legged control | Wensing et al., *Optimization-Based Control for Dynamic Legged Robots*, IEEE T-RO 2024 | [pdf](papers/01-surveys/wensing2024optimization.pdf) |
| Learning-based locomotion | Ha et al., *Learning-based Legged Locomotion*, IJRR 2025 | [pdf](papers/01-surveys/ha2025learning.pdf) |
| MPC + RL hybrids | Reiter et al., *Synthesis of MPC and RL*, Annual Reviews in Control 2026 | [pdf](papers/01-surveys/reiter2026synthesis.pdf) |
| Control vs RL | Recht, *A Tour of RL: The View from Continuous Control*, 2019 | [pdf](papers/01-surveys/recht2019tour.pdf) |
| Control vs RL, empirical | Song et al., *Optimal Control versus RL* (drone racing), Science Robotics 2023 | [pdf](papers/01-surveys/song2023reaching.pdf) |
| Model-based RL | Moerland et al., *Model-based RL: A Survey*, FnT ML 2023 | [pdf](papers/01-surveys/moerland2023mbrl.pdf) |
| Imitation learning | Osa et al., *An Algorithmic Perspective on Imitation Learning*, 2018 | [pdf](papers/01-surveys/osa2018algorithmic.pdf) |
| Exploration | Ladosz et al., *Exploration in Deep RL: A Survey*, 2022 | [pdf](papers/01-surveys/ladosz2022exploration.pdf) |
| Real-world RL | Dulac-Arnold et al., *Challenges of Real-World RL*, Machine Learning 2021 | [pdf](papers/01-surveys/dulacarnold2021challenges.pdf) |
| Safe learning | Brunke et al., *Safe Learning in Robotics*, 2022 | [pdf](papers/01-surveys/brunke2022safe.pdf) |
| Differentiable simulation | Newbury et al., *A Review of Differentiable Simulators*, IEEE Access 2024 | [pdf](papers/01-surveys/newbury2024review.pdf) |
| Humanoids | Gu et al., *Humanoid Locomotion and Manipulation*, 2025 | [pdf](papers/01-surveys/gu2025humanoid.pdf) |

The full list is in [CATALOG.md](CATALOG.md#01-surveys).

## Adding a paper

1. Add an entry to `catalog.json`. The fields are `key`, `cat`, `title`, `authors`, `year`, `venue`, `note`, plus `arxiv` and/or `url`. Set `"pdf": true` to keep a local copy; this works only for entries with an arXiv ID.
2. Run `python3 tools/build_catalog.py --download` from this folder.
3. Commit `catalog.json`, the regenerated `CATALOG.md` and `catalog.csv`, and any new PDF.

## Notes on sources

- Local PDFs are the authors' open-access arXiv versions, downloaded from arxiv.org. Journal-only papers (for example Kober 2013, Hewing 2020, Mnih 2015) are linked by DOI and not copied.
- All arXiv IDs and DOIs in the catalog were checked against the arXiv API and Crossref when the collection was built (25 October 2026).
- SuperMimic's figures are the authors' self-reported numbers from a preprint. The task fit ratings in report 03 are a synthesis of the surveys, not measured results.
