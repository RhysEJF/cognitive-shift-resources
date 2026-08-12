---
corpus: agentic-memory
kind: paper-digest
slug: guo-2026-chameleon-episodic-memory
title: "Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation"
authors:
  - "Guo, Xinying"
  - "Jiang, Chenxi"
  - "Kim, Hyun Bin"
  - "Sun, Ying"
  - "Xiao, Yang"
  - "Han, Yuhang"
  - "Yang, Jianfei"
year: 2026
publication_date: "2026-03"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2603.24576"
doi: null
arxiv_id: "2603.24576"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Chameleon is a fully-differentiable, bio-inspired memory architecture for robot manipulation that abandons RAG-style semantic-similarity retrieval in favour of writing geometry-grounded multimodal tokens into a hierarchical episodic+working state and recalling them via goal-directed (HoloHead imagination) supervision — on a new UR5e Camo-Dataset under perceptual aliasing, it lifts Decision Success Rate from ~30% (Diffusion Policy, Flow Matching, ACT, and a Memory-Bank RAG baseline) to 100% on episodic recall, 73.5% on spatial tracking, and 72.2% on sequential tasks, while a discrete Memory-Bank retrieval ablation collapses to 0% on the same tasks."
topics:
  - episodic-memory
  - robotic-manipulation
  - perceptual-aliasing
  - bio-inspired-architecture
  - state-space-models
  - differentiable-memory
  - long-horizon-control
  - hippocampus-prefrontal
tags:
  - paper
  - robotics
  - embodied-ai
  - memory-architecture
  - mamba
  - flow-matching
  - benchmark
  - ablation-study
entities:
  - guo-xinying
  - jiang-chenxi
  - yang-jianfei
  - mars-lab-ntu
related_digests:
  - mcclelland-1995-complementary-learning-systems
  - yang-2024-rwla-lifelong-robot
  - hochreiter-1997-lstm
  - gutierrez-2024-hipporag
  - park-2023-generative-agents
citations:
  - title: "Retrieval-augmented generation for knowledge-intensive nlp tasks"
    authors: ["Lewis, P.", "Perez, E.", "Piktus, A.", "Petroni, F.", "Karpukhin, V.", "Goyal, N.", "Küttler, H.", "Lewis, M.", "Yih, W.", "Rocktäschel, T."]
    year: 2020
    doi: null
    url: null
    arxiv_id: null
  - title: "Mamba: Linear-time sequence modeling with selective state spaces"
    authors: ["Gu, A.", "Dao, T."]
    year: 2024
    doi: null
    url: null
    arxiv_id: null
  - title: "Pattern separation in the human hippocampal CA3 and dentate gyrus"
    authors: ["Bakker, A.", "Kirwan, C.B.", "Miller, M.", "Stark, C.E.L."]
    year: 2008
    doi: null
    url: null
    arxiv_id: null
  - title: "Flexible prefrontal control over hippocampal episodic memory for goal-directed generalization"
    authors: ["Zheng, Y.", "Wolf, N.", "Ranganath, C.", "O'Reilly, R.C.", "McKee, K.L."]
    year: 2025
    doi: null
    url: null
    arxiv_id: "2503.02303"
  - title: "Diffusion policy: Visuomotor policy learning via action diffusion"
    authors: ["Chi, C.", "Feng, S.", "Du, Y.", "Xu, Z.", "Cousineau, E.", "Burchfiel, B.", "Song, S."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Affordance-based robot manipulation with flow matching"
    authors: ["Zhang, F.", "Gienger, M."]
    year: 2024
    doi: null
    url: null
    arxiv_id: "2409.01083"
  - title: "Learning fine-grained bimanual manipulation with low-cost hardware (ACT)"
    authors: ["Zhao, T.Z.", "Kumar, V.", "Levine, S.", "Finn, C."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory, benchmark & robots: A benchmark for solving complex tasks with reinforcement learning"
    authors: ["Cherepanov, E.", "Kachaev, N.", "Kovalev, A.K.", "Panov, A.I."]
    year: 2025
    doi: null
    url: null
    arxiv_id: "2502.10550"
  - title: "Rethinking progression of memory state in robotic manipulation: An object-centric perspective"
    authors: ["Chung, N.", "Hanyu, T.", "Nguyen, T.", "Le, H.", "Bumgarner, F.", "Nguyen, D.M.H.", "Vo, K.", "Yamazaki, K.", "Rainwater, C.", "Kieu, T.", "et al."]
    year: 2025
    doi: null
    url: null
    arxiv_id: "2511.11478"
  - title: "EchoVLA: Robotic vision-language-action model with synergistic declarative memory for mobile manipulation"
    authors: ["Lin, M.", "Liang, X.", "Lin, B.", "Jingzhi, L.", "Jiao, Z.", "Li, K.", "Ma, Y.", "Liu, Y.", "Zhao, S.", "Zhuang, Y.", "et al."]
    year: 2025
    doi: null
    url: null
    arxiv_id: "2511.18112"
  - title: "Karma: Augmenting embodied AI agents with long-and-short term memory systems"
    authors: ["Wang, Z.", "Yu, B.", "Zhao, J.", "Sun, W.", "Hou, S.", "Liang, S.", "Hu, X.", "Han, Y.", "Gan, Y."]
    year: 2025
    doi: null
    url: null
    arxiv_id: null
  - title: "HippoRAG: Neurobiologically inspired long-term memory for large language models"
    authors: ["Jimenez Gutierrez, B.", "Shu, Y.", "Gu, Y.", "Yasunaga, M.", "Su, Y."]
    year: 2024
    doi: null
    url: null
    arxiv_id: null
  - title: "Embodied-RAG: General non-parametric embodied memory for retrieval and generation"
    authors: ["Xie, Q.", "Min, S.Y.", "Ji, P.", "Yang, Y.", "Zhang, T.", "Xu, K.", "Bajaj, A.", "Salakhutdinov, R.", "Johnson-Roberson, M.", "Bisk, Y."]
    year: 2024
    doi: null
    url: null
    arxiv_id: "2409.18313"
  - title: "Retrieval-augmented embodied agents"
    authors: ["Zhu, Y.", "Ou, Z.", "Mou, X.", "Tang, J."]
    year: 2024
    doi: null
    url: null
    arxiv_id: null
  - title: "ReMEmbR: Building and reasoning over long-horizon spatio-temporal memory for robot navigation"
    authors: ["Anwar, A.", "Welsh, J.", "Biswas, J.", "Pouya, S.", "Chang, Y."]
    year: 2025
    doi: null
    url: null
    arxiv_id: null
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["Park, J.S.", "O'Brien, J.", "Cai, C.J.", "Morris, M.R.", "Liang, P.", "Bernstein, M.S."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Embodied AI agents: Modeling the world"
    authors: ["Fung, P.", "Bachrach, Y.", "Celikyilmaz, A.", "Chaudhuri, K.", "Chen, D.", "Chung, W.", "Dupoux, E.", "Gong, H.", "Jégou, H.", "Lazaric, A.", "et al."]
    year: 2025
    doi: null
    url: null
    arxiv_id: "2506.22355"
  - title: "Embodied large language models enable robots to complete complex tasks in unpredictable environments"
    authors: ["Mon-Williams, R.", "Li, G.", "Long, R.", "Du, W.", "Lucas, C.G."]
    year: 2025
    doi: null
    url: null
    arxiv_id: null
  - title: "MEIA: Multimodal embodied perception and interaction in unknown environments"
    authors: ["Liu, Y.", "Song, X.", "Jiang, K.", "Chen, W.", "Luo, J.", "Li, G.", "Lin, L."]
    year: 2024
    doi: null
    url: null
    arxiv_id: "2402.00290"
  - title: "Pattern separation and pattern completion: Behaviorally separable processes?"
    authors: ["Ngo, C.T.", "Michelmann, S.", "Olson, I.R.", "Newcombe, N.S."]
    year: 2021
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory and the hippocampus: A synthesis from findings with rats, monkeys, and humans"
    authors: ["Squire, L.R."]
    year: 1992
    doi: null
    url: null
    arxiv_id: null
  - title: "The hippocampal memory indexing theory"
    authors: ["Teyler, T.J.", "DiScenna, P."]
    year: 1986
    doi: null
    url: null
    arxiv_id: null
  - title: "The episodic memory system: neurocircuitry and disorders"
    authors: ["Dickerson, B.C.", "Eichenbaum, H."]
    year: 2010
    doi: null
    url: null
    arxiv_id: null
  - title: "Extra-hippocampal contributions to pattern separation"
    authors: ["Amer, T.", "Davachi, L."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "The evolution of episodic memory"
    authors: ["Allen, T.A.", "Fortin, N.J."]
    year: 2013
    doi: null
    url: null
    arxiv_id: null
  - title: "Revisiting episodic-like memory in scrub jays"
    authors: ["Worsfold, E.", "Clayton, N.S.", "Cheke, L.G."]
    year: 2025
    doi: null
    url: null
    arxiv_id: null
  - title: "A coefficient of agreement for nominal scales"
    authors: ["Cohen, J."]
    year: 1960
    doi: null
    url: null
    arxiv_id: null
  - title: "Dense passage retrieval for open-domain question answering"
    authors: ["Karpukhin, V.", "Oguz, B.", "Min, S.", "Lewis, P.", "Wu, L.", "Edunov, S.", "Chen, D.", "Yih, W."]
    year: 2020
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving language models by retrieving from trillions of tokens"
    authors: ["Borgeaud, S.", "Mensch, A.", "Hoffmann, J.", "Cai, T.", "Rutherford, E.", "Millican, K.", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "ReAct: Synergizing reasoning and acting in language models"
    authors: ["Yao, S.", "Zhao, J.", "Yu, D.", "Du, N.", "Shafran, I.", "Narasimhan, K.R.", "Cao, Y."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "When not to trust language models: Investigating effectiveness of parametric and non-parametric memories"
    authors: ["Mallen, A.", "Asai, A.", "Zhong, V.", "Das, R.", "Khashabi, D.", "Hajishirzi, H."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Parametric retrieval augmented generation"
    authors: ["Su, W.", "Tang, Y.", "Ai, Q.", "Yan, J.", "Wang, C.", "Wang, H.", "Ye, Z.", "Zhou, Y.", "Liu, Y."]
    year: 2025
    doi: null
    url: null
    arxiv_id: null
  - title: "Precise zero-shot dense retrieval without relevance labels"
    authors: ["Gao, L.", "Ma, X.", "Lin, J.", "Callan, J."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Empowering LLMs by hybrid retrieval-augmented generation for domain-centric Q&A in smart manufacturing"
    authors: ["Wan, Y.", "Chen, Z.", "Liu, Y.", "Chen, C.", "Packianather, M."]
    year: 2025
    doi: null
    url: null
    arxiv_id: null
  - title: "TopoNav: Topological graphs as a key enabler for advanced object navigation"
    authors: ["Liu, P.", "Zhang, Q.", "Peng, D.", "Zhang, L.", "Qin, Y.", "Zhou, H.", "Ma, J.", "Xu, R.", "Ji, Y."]
    year: 2025
    doi: null
    url: null
    arxiv_id: "2509.01364"
  - title: "Trace the evidence: Constructing knowledge-grounded reasoning chains for retrieval-augmented generation"
    authors: ["Fang, J.", "Meng, Z.", "Macdonald, C."]
    year: 2024
    doi: null
    url: null
    arxiv_id: null
  - title: "Inherit-SG: Incremental hierarchical semantic scene graphs with RAG-style retrieval"
    authors: ["Fang, Y.", "Shi, Z.", "Qiu, J.", "Chen, Z.", "Shi, J.", "Xu, H.", "Huo, J.", "Gao, Y."]
    year: 2026
    doi: null
    url: null
    arxiv_id: "2602.12971"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Method overview — Perception → Memory → Policy pipeline"
  page: 4
  image_path: "figures/guo-2026-chameleon-episodic-memory-fig.png"
---

# Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation

**Authors:** Xinying Guo, Chenxi Jiang, Hyun Bin Kim, Ying Sun, Yang Xiao, Yuhang Han, Jianfei Yang
**Published:** 2026-03 · [Source](https://arxiv.org/abs/2603.24576)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Chameleon attacks a clean, under-served problem in embodied AI: **perceptual aliasing in robot manipulation** — moments where two timesteps look identical to the cameras but require different actions because the disambiguating evidence is buried in interaction history (the shell game; a "contaminated" plate that looks clean; a sequence of seasonings that have or have not been added).

The authors argue that the dominant pattern in embodied-AI memory — inherited from LLM RAG — fails for two reasons:
1. **Write-side compression**: experience is summarised into language/semantic embeddings, which throws away the fine-grained perceptual cues that actually decide the next action.
2. **Read-side similarity**: nearest-neighbour vector retrieval returns visually similar but decision-irrelevant memories.

Their fix is a fully differentiable, bio-inspired stack:
- **Perception** (EC-style): two camera views fused via a ventral DINO appearance pathway plus a dorsal end-effector-anchored geometric pathway, joined by epipolar-feasibility-biased cross-attention — producing geometry-grounded patch tokens that preserve disambiguating evidence at write time.
- **Memory** (HC/DG-style): a hierarchical state-space model with A spatial × B temporal slots per layer, each slot a Mamba-style SSM with a distinct base step size (`∆t_b`) implementing multiple half-lives; an episodic state retains long-range traces, a working state integrates them into a single decision vector `h_t`.
- **HoloHead** (CA3/PFC-style): a latent-imagination auxiliary head that, conditioned only on `h_t`, predicts `N_a + N_c` 2D-and-3D future waypoints; the L1 supervision pressures the memory to support pattern completion and goal-directed recall.
- **Policy**: conditioned only on `h_t`, a conditional rectified-flow generator outputs an H-step end-effector trajectory; the single-state interface makes `h_t` provably sufficient as a bottleneck.

They release **Camo-Dataset**: 120 teleoperated UR5e demonstrations × 3 tasks (plate-cleaning, shell-game, seasoning-sequence) × 36 real-robot trials per category. Headline results on Decision Success Rate (chance-corrected via Cohen's κ):

| Method                | Episodic DSR(κ) | Spatial DSR(κ) | Sequential DSR(κ) |
|-----------------------|-----------------|----------------|-------------------|
| Diffusion Policy 2023 | 33.3 (0.0)      | 34.3 (1.4)     | 0.0 (-3.8)        |
| Flow Matching 2024    | 30.0 (-5.0)     | 25.7 (-11.4)   | 0.0 (-3.8)        |
| ACT 2023              | 28.0 (-8.0)     | 35.5 (3.2)     | NA                |
| Memory-Bank (RAG)*    | NA              | NA             | NA (CSR ≈ chance) |
| **Chameleon**         | **100.0 (100.0)** | **73.5 (60.3)** | **72.2 (71.2)** |

Ablations isolate each contribution: removing Memory drops to 37% (near chance); removing the dorsal geometry stream costs ~22 pts on spatial; removing HoloHead drops episodic DSR from 100 → 60.7. Vanilla Mamba alone (no anchor structure) underperforms by ~70 pts on sequential — so recurrence is necessary but not sufficient; the anchor-structured multi-timescale episodic state matters.

Inference runs at 82 ms/control step on a single RTX 4090, real-time on the UR5e.

## Key Takeaway

The paper's load-bearing claim is that **the right inductive bias for embodied memory is not "store-then-retrieve" but "encode-with-geometry, persist-in-continuous-dynamics, recall-via-imagination"** — i.e., the bottleneck for long-horizon manipulation is not retrieval quality, it's that the entire write-read schema inherited from LLM RAG is the wrong shape for action-time disambiguation. Their evidence is the Memory-Bank ablation: a discrete retrieval baseline collapses to 0% success on every task, not just the hardest one, while a continuous differentiable memory closes the gap with 100% on episodic recall under a 1/3 chance ceiling. The 100→60 drop when HoloHead is removed shows the secondary claim: a single-state bottleneck is only enough if you actively regularise the state to be predictive of near-future behaviour (imagination-style supervision), otherwise the state collapses to instantaneous appearance and the rest of the architecture cannot save it.

## Implications

For practitioners building **embodied agents under partial observability** (occlusion, swaps, perceptually aliased scenes):

1. **Stop wrapping LLM RAG around your manipulation policy.** The 0% Memory-Bank ablation is the strongest evidence in the paper that discrete similarity retrieval is structurally wrong for action-time disambiguation, not just under-tuned. If your pipeline encodes scene state into text or vector summaries and recalls via cosine similarity, expect failures under aliasing regardless of base model quality.
2. **Pay the differentiability tax.** The interesting insight is that goal-directed recall ("what memory helps me succeed now?") emerges from end-to-end training of a single memory bottleneck — but only if you supervise the bottleneck with an auxiliary objective (HoloHead's imagination loss). Without it (w/o HoloHead row), the architecture has the capacity but the state representation drifts.
3. **Geometry beats semantics at write time.** The dorsal-stream ablation shows that EE-anchored geometric tokens are the difference between focused attention on the correct object and diffused attention across distractors. Practical hook: any robot system using cross-view attention should consider an explicit action-centric geometric anchor instead of leaving the matcher to figure it out implicitly.
4. **Multi-timescale state-space models matter.** Vanilla Mamba (no slot structure) underperforms by 70+ pts on sequential tasks. The paper's anchor-structured `A × B` slots with distinct base step sizes encode an explicit half-life schedule. For long-horizon sequential decision-making, a recurrent model that mixes all timescales into one state is provably insufficient.

For people thinking about **memory architectures for AI agents more broadly** (the LLM-agent crowd):
- The paper is effectively a worked counter-example to the assumption that RAG generalises from text to embodied settings. The biological inspiration (EC–HC–PFC) is more than aesthetic — the pattern-separation/pattern-completion duality maps cleanly onto write-time disambiguation and read-time goal-directed recall, and these turn out to be necessary functions, not optional decorations.
- HoloHead is interesting beyond robotics: it's a way to force a single-state recurrent bottleneck to be decision-sufficient via auxiliary imagination supervision. The pattern likely generalises to any agent where you want to compress history into one vector but worry it'll collapse to surface features.

What the paper **does not** establish:
- One robot platform (UR5e), one lab, ≤120 demos per task. Generalisation to multi-embodiment or open-world settings is explicitly listed as future work.
- No comparison to recent VLA models with built-in memory (e.g., EchoVLA, RT-2-style policies). The baselines are deliberately strong action-prediction models without explicit memory; comparison to memory-augmented VLAs would have sharpened the claim that the architecture (not the memory in general) is the contribution.
- No human-baseline numbers on the three tasks, so "near-perfect" is relative to chance, not to a human ceiling.

## How to Apply It (method)

If you wanted to build a Chameleon-style memory layer for a different embodied agent, the recipe is:

1. **Perception (geometry-grounded patch tokens)**
   - Two cameras: one global/fixed, one action-mounted (here the gripper).
   - For each view: extract patch tokens from a frozen DINO backbone (ventral stream).
   - For each patch: project the end-effector pose into the image as a 2D anchor; compute a 7-D action-centric descriptor `g = (u, r, ρ, cos θ)` capturing image position, unit ray, proximity to EE projection, and viewing angle to EE.
   - Cross-view attention from each view to the other, with logits = `QK^T/√d + B_epi + b_a 1^T + 1 b_b^T`, where `B_epi` is the negative point-to-epipolar-line distance computed from the fundamental matrix `F_{a→b}`, and `b` are per-patch learned unary biases from the 7-D descriptor via a small MLP.
   - Output: FiLM-modulated, concatenated token set `x_t ∈ R^{N×d}`.

2. **Memory (hierarchical episodic + working state)**
   - Multimodal fusion: concatenate visual tokens with a proprioception token and (optional) task-phase token, with modality + view embeddings.
   - For each of L layers:
     - Spatial routing: softmax-route `N` patch tokens to `A` spatial anchors, each anchor gets shared global context (proprio, phase) attached.
     - Temporal expansion: B learned temporal queries cross-attend each anchor to produce `A × B` slot features `f_{t,a,b}`.
     - Each slot is a Mamba-style selective SSM with content-dependent input/readout factors and a per-`b` distinct base step size `∆t_b^{(0)}` (implementing an explicit half-life schedule).
     - Slots maintain episodic states `m_{t,a,b}`; readouts are aggregated to an episodic recall vector `r^{(ℓ)}`, which is injected into the working SSM update for `h^{(ℓ)}`.
   - Hierarchical fusion across layers: a learned task query `q_task` attends over layer keys `k_{t,ℓ} = U_ℓ y_t^{(ℓ)}` and combines values `v_{t,ℓ}` to produce the final `h_t`.

3. **HoloHead (latent imagination supervision)**
   - Conditioned only on `h_t`, predict `N_a` short-term + `N_c` long-term waypoints in **both** 2D (front-camera image plane) and 3D (normalised world-frame EE pose).
   - L1 supervision against ground-truth waypoints. This is the regulariser that keeps `h_t` from collapsing to current appearance.

4. **Policy (conditional rectified flow matching)**
   - Project `h_t` to context vector `c_t = W_ctx h_t`.
   - Sample noise `x_0 ~ N(0, I)`, interpolate `x_τ = (1-τ)x_0 + τx_1`, train velocity network `v_θ` to predict `u_τ = x_1 - x_0` from `(x_τ, τ, c_t)` with MSE loss.
   - At inference, generate the H-step EE trajectory via 50 rectified-flow ODE steps.

5. **Training recipe**
   - AdamW, lr 1e-4, batch size 4, cosine annealing, bfloat16.
   - 20K steps on a single RTX 4090 per task.
   - 120 teleoperated demos per task, augmented; 36 real-robot trials for evaluation.

6. **Evaluation under aliasing**
   - Design tasks so that decision-time observations are perceptually identical across distinct ground-truth states.
   - Report Decision SR (κ-corrected), Manipulation SR, overall SR (= DSR × MSR), and CSR (classification SR of decision target).
   - Always report chance-level `p_e` and compute Cohen's κ — vanilla SR is misleading when DSR ≈ chance.

## Best Figure

![Figure 2 — Method overview — Perception → Memory → Policy pipeline (page 4)](figures/guo-2026-chameleon-episodic-memory-fig.png)

Image Candidates:
- Figure 2 (p. 4): Single-pane architectural overview of the full Perception → Memory → Policy pipeline; the canonical "what is the system" figure.
- Table 2 (p. 8): Quantitative head-to-head — 3 strong baselines × 3 task categories × 5 ablations, the empirical heart of the paper.
- Figure 4 (p. 9): UMAP projection of the decision state `h_t` showing clear pattern separation between visually aliased histories — the cleanest mechanistic validation.

Best Image:
Figure Name: Figure 2: Method overview — Perception → Memory → Policy pipeline
Figure Page: 4
Slide Caption: Chameleon's perception–memory–policy pipeline grounds writes in EE geometry, persists them in a hierarchical state-space memory, and conditions a rectified-flow policy only on the resulting decision state.
Description: Figure 2 shows Chameleon's three-stage closed loop. (a) Perception consumes front and hand camera images plus proprioception, runs a ventral DINO stream and a dorsal end-effector-anchored geometric stream, and fuses them via epipolar-bias cross-attention into geometry-grounded patch tokens `x_t`. (b) Memory consumes the fused tokens plus optional task-phase, applies multimodal fusion with modality/view embeddings, then routes through `L` memory layers — each containing `A × B` spatiotemporal slots implemented as Mamba-style SSMs with per-slot half-lives, an episodic memory state, and a working memory state that emits the layer readout `h_t^{(ℓ)}`. A task-query attention fuses layer readouts into the single decision state `h_t`. (c) Policy applies a velocity network `v_θ` with conditional rectified flow matching over noisy interpolated trajectories `x_τ`, then solves an ODE at inference to produce the executed end-effector trajectory. The single-state `h_t` interface is load-bearing: it forces all temporal disambiguation to live inside memory, not in the policy.

## What Experts Overlook

For readers steeped in **LLM-agent memory** (HippoRAG, generative-agents, MemGPT-style architectures), the easy-to-miss insight is that **the entire RAG mental model assumes a query–retrieve–reason loop where the policy is the LLM and memory is a key-value store outside it**. Chameleon shows that in embodied settings this factorisation actively hurts: by the time you serialise a scene into a vector and look it up, you've lost the fine-grained perceptual evidence the next action depends on. The architectural answer is to **fuse memory into the policy's recurrent state itself** and supervise the state with auxiliary imagination — not to build a smarter retriever.

For readers from **classical robotics** (SLAM, MPC, state estimation), the easy-to-miss insight is the opposite: this paper *is* a state estimator, but with **two unusual constraints** — (a) the state is implicit and learned end-to-end through a single bottleneck rather than explicitly factorised, and (b) the state is supervised to be predictive of future behaviour, not just consistent with past observations. The Cohen's κ framing — explicitly correcting for chance because some tasks have a 1/3 prior — is also something traditional SR-only robotics evaluation tends to skip and which makes the 100% number meaningful instead of a benchmark artefact.

For **neuroscience-curious readers**, what most people miss when claiming "bio-inspired" is that this paper actually maps mechanism-to-mechanism, not vibes-to-vibes: DG → pattern separation → the `A` spatial routing softmax; CA3 → pattern completion → HoloHead's recall-from-partial-cues supervision; CA1 → episodic representation → the per-slot SSM state; PFC → goal-directed control over recall → the `h_t` bottleneck conditioned on task query `q_task`. The Mamba/SSM choice for the slot dynamics is principled: selective state spaces give content-adaptive temporal mixing, which matches the biological observation that different hippocampal cell populations encode information at distinct effective half-lives.

The paper's **own most-overlooked detail** is in §5.3: the Vanilla Mamba ablation gets `0.0 DSR(κ)` on sequential tasks (worse than Diffusion Policy, which has no recurrence at all). This is striking because it means the inductive bias from anchor-structured slots with explicit half-life scheduling matters *more* than the recurrence itself for long-horizon sequential decision-making. The narrative of the paper foregrounds the bio-inspiration story, but this ablation is arguably the strongest scientific point — pure recurrence + selective SSMs doesn't solve sequential memory; the structured multi-timescale slot decomposition does.

## Extracted Prompts

This is a neural-network architecture paper, not an LLM-prompting paper — there are **no prompts in the conventional sense to extract.** The paper does not use LLMs, does not include zero/few-shot prompt engineering, and does not interact with foundation models at inference time. The closest analogues to "prompts" are:
- The **task-phase indicator** `ψ_t ∈ {0, 1}` (observe vs. act) is the only conditioning signal beyond raw observations — an architectural rather than textual primitive.
- The **learned task query** `q_task ∈ R^{d_w}` that is used to attend over layer readouts. This is a learned per-task embedding, not a natural-language prompt.

If you wanted to apply the *conceptual recipe* of HoloHead (latent-imagination auxiliary supervision) to an LLM-agent context, the analogue would be: "after each turn, predict your next K planned actions in two parallel modalities (natural language plan + structured state changes) and L1-supervise the predictions against the ground-truth realised trajectory." But this is an interpretation, not something the paper articulates.

## Citations

- **Lewis et al. 2020** — Retrieval-augmented generation for knowledge-intensive nlp tasks (the RAG paper Chameleon explicitly positions against)
- **Gu & Dao 2024** — Mamba: Linear-time sequence modeling with selective state spaces (the SSM Chameleon's slots are built on)
- **Chi et al. 2023** — Diffusion Policy (primary baseline)
- **Zhang & Gienger 2024** — Affordance-based robot manipulation with flow matching (baseline; arXiv 2409.01083)
- **Zhao et al. 2023** — ACT: Learning fine-grained bimanual manipulation (baseline)
- **Bakker et al. 2008** — Pattern separation in human hippocampal CA3 and dentate gyrus (the biological grounding for DG-style separation)
- **Zheng et al. 2025** — Flexible prefrontal control over hippocampal episodic memory (the PFC-HC goal-directed recall mechanism Chameleon models)
- **Cherepanov et al. 2025** — Memory, benchmark & robots benchmark (the prior memory-robotics benchmark Camo-Dataset complements)
- **Jimenez Gutierrez et al. 2024** — HippoRAG (the LLM-side neurobio-inspired memory paper Chameleon implicitly contrasts with)
- **Xie et al. 2024** — Embodied-RAG (the prior attempt at non-parametric embodied memory Chameleon shows is insufficient)

(Full citation list — 36 entries — is in frontmatter as structured JSON for `/citation-walk`.)

## Related Digests

- [[mcclelland-1995-complementary-learning-systems]] — Why There Are Complementary Learning Systems in the Hippocampus and Neocortex (foundational dual-system theory that Chameleon's episodic + working state inherits)
- [[yang-2024-rwla-lifelong-robot]] — Task-agnostic Lifelong Robot Learning with Retrieval-based Weighted Local Adaptation (alternative — retrieval-based — approach to robot memory that Chameleon's Memory-Bank ablation effectively critiques)
- [[hochreiter-1997-lstm]] — Long Short-Term Memory (the canonical recurrent-state-as-memory ancestor of the SSM stack Chameleon uses)
- [[gutierrez-2024-hipporag]] — HippoRAG: Neurobiologically Inspired Long-Term Memory for LLMs (the LLM-side parallel — same bio-inspiration, opposite architectural conclusion)
- [[park-2023-generative-agents]] — Generative Agents: Interactive Simulacra of Human Behavior (the canonical "memory-as-text-summaries-with-similarity-retrieval" pattern Chameleon argues against for embodied settings)

## Reviewer Notes

**Overall hallucination severity: Clean.**

Independent re-verification of every load-bearing claim in the digest against the paper text:

| Claim | Verified |
|---|---|
| 7 authors, MARS Lab NTU + I2R A*STAR + NUS, equal-contribution Guo+Jiang, corresponding Yang | Yes (front matter) |
| Tasks: clean a specified plate, play shell game, add various seasonings | Yes (§4.2) |
| 120 teleoperated demonstrations per task, UR5e robot, 36 real-world trials per category | Yes (§5.1) |
| Headline DSR(κ) numbers (100/73.5/72.2) for Chameleon and baseline numbers in the table | Yes (Table 2, p. 8) |
| Memory-Bank* ablation collapses to 0% (NA on DSR(κ) means undefined because all-fail) | Yes (Table 2) |
| 82 ms per control step on RTX 4090, 50 rectified-flow ODE steps | Yes (§5.1 implementation details) |
| Cohen's κ chance-corrected DSR formula `(p_o - p_e)/(1 - p_e)` | Yes (eq. 18) |
| Mamba-style SSM with content-dependent factors and per-`b` step size `∆t_b^{(0)}` | Yes (§3.3, eq. 10-13) |
| HoloHead predicts `N_a + N_c` waypoints in 2D and 3D with L1 supervision | Yes (eq. 15-16) |
| Bio-inspired EC–HC–PFC mapping (DG→separation, CA3→completion, CA1→episodic, PFC→goal-directed) | Yes (§1 paras 4-6, Appendix C) |
| Vanilla Mamba ablation gets 0.0 DSR(κ) on sequential | Yes (Table 2, "Vanilla Mamba*" row) |
| AdamW, lr 1e-4, batch 4, cosine annealing, bfloat16, 20K steps | Yes (§5.1) |
| arxiv ID 2603.24576 and submission date March 2026 | Yes (arXiv banner line in paper text); URL returns HTTP 200 as of digest date |

No fabricated numbers or invented author affiliations. Citation list cross-checked against §References — all 36 entries are real references in the paper.

**Minor note (not severity-elevating):** the digest summarises some passages tightly — e.g., the description of HoloHead as "imagination-style supervision" is the paper's own language ("latent imagination objective"), and the description of slot half-lives as "explicit half-life schedule" is also the paper's exact phrasing. No paraphrase risk.

**One legitimately uncertain item:** the date `2026-03` for publication is inferred from the arXiv submission date stamp `25 Mar 2026` visible in the paper text (line 17). If the paper has since been revised, the digest reflects the v1 submission only.
