---
corpus: agentic-memory
kind: paper-digest
slug: de-lange-2022-stability-gap
title: "Continual Evaluation for Lifelong Learning: Identifying the Stability Gap"
authors:
  - "De Lange, Matthias"
  - "van de Ven, Gido M."
  - "Tuytelaars, Tinne"
year: 2022
publication_date: "2022-05"
venue: "ICLR 2023 (arXiv preprint May 2022, v2 Mar 2023)"
source_url: "https://arxiv.org/abs/2205.13452"
doi: null
arxiv_id: "2205.13452"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "State-of-the-art continual learning methods — including experience replay, GEM, EWC, SI, and LwF — all suffer a sharp, transient drop in accuracy on previously-learned tasks immediately after a task boundary, a phenomenon the authors name the stability gap; this drop is invisible to standard task-transition evaluation, can reach 100% forgetting before recovery, and is amplified by larger distribution shifts between tasks."
topics:
  - continual-learning
  - lifelong-learning
  - catastrophic-forgetting
  - experience-replay
  - evaluation-methodology
  - stability-plasticity-tradeoff
tags:
  - paper
  - iclr-2023
  - benchmark
  - evaluation-metrics
  - safety-critical
  - gradient-analysis
entities:
  - de-lange-matthias
  - van-de-ven-gido
  - tuytelaars-tinne
  - ku-leuven
related_digests:
  - thorne-2020-ewc-bias-inoculation
  - mcclelland-1995-complementary-learning-systems
  - logan-2026-continuum-memory-architectures
  - ai-2026-memorybench-continual-learning
  - hu-2026-evermemos
citations:
  - title: "Riemannian walk for incremental learning: Understanding forgetting and intransigence"
    authors: ["Chaudhry, A.", "Dokania, P.K.", "Ajanthan, T.", "Torr, P.H.S."]
    year: 2018
    venue: "ECCV"
    url: null
    arxiv_id: null
  - title: "Efficient lifelong learning with A-GEM"
    authors: ["Chaudhry, A.", "Ranzato, M.", "Rohrbach, M.", "Elhoseiny, M."]
    year: 2019
    venue: "ICLR"
    url: "https://openreview.net/forum?id=Hkf2_sC5FX"
    arxiv_id: null
  - title: "Continual learning with tiny episodic memories"
    authors: ["Chaudhry, A.", "Rohrbach, M.", "Elhoseiny, M.", "Ajanthan, T.", "Dokania, P.K.", "Torr, P.H.S.", "Ranzato, M."]
    year: 2019
    venue: "arXiv preprint"
    url: null
    arxiv_id: "1902.10486"
  - title: "Continual prototype evolution: Learning online from non-stationary data streams"
    authors: ["De Lange, M.", "Tuytelaars, T."]
    year: 2021
    venue: "ICCV"
    url: null
    arxiv_id: null
  - title: "A continual learning survey: Defying forgetting in classification tasks"
    authors: ["De Lange, M.", "Aljundi, R.", "Masana, M.", "Parisot, S.", "Jia, X.", "Leonardis, A.", "Slabaugh, G.", "Tuytelaars, T."]
    year: 2021
    venue: "IEEE TPAMI"
    doi: "10.1109/TPAMI.2021.3057446"
    url: null
    arxiv_id: null
  - title: "Catastrophic forgetting in connectionist networks"
    authors: ["French, R.M."]
    year: 1999
    venue: "Trends in Cognitive Sciences 3(4):128-135"
    url: null
    arxiv_id: null
  - title: "Studies of mind and brain: neural principles of learning, perception, development, cognition, and motor control"
    authors: ["Grossberg, S."]
    year: 1982
    venue: "Reidel (Boston Studies in the Philosophy of Science 70)"
    url: null
    arxiv_id: null
  - title: "Distilling the knowledge in a neural network"
    authors: ["Hinton, G.", "Vinyals, O.", "Dean, J."]
    year: 2015
    venue: "arXiv preprint"
    url: null
    arxiv_id: "1503.02531"
  - title: "Natural continual learning: success is a journey, not (just) a destination"
    authors: ["Kao, T.-C.", "Jensen, K.", "van de Ven, G.", "Bernacchia, A.", "Hennequin, G."]
    year: 2021
    venue: "NeurIPS 34"
    url: "https://proceedings.neurips.cc/paper/2021/file/ec5aa0b7846082a2415f0902f0da88f2-Paper.pdf"
    arxiv_id: null
  - title: "Overcoming catastrophic forgetting in neural networks"
    authors: ["Kirkpatrick, J.", "Pascanu, R.", "Rabinowitz, N.", "Veness, J.", "Desjardins, G.", "Rusu, A.A.", "Milan, K.", "Quan, J.", "Ramalho, T.", "Grabska-Barwinska, A."]
    year: 2017
    venue: "PNAS"
    doi: "10.1073/pnas.1611835114"
    url: null
    arxiv_id: null
  - title: "Learning without forgetting"
    authors: ["Li, Z.", "Hoiem, D."]
    year: 2017
    venue: "IEEE TPAMI 40(12):2935-2947"
    url: null
    arxiv_id: null
  - title: "Avalanche: an end-to-end library for continual learning"
    authors: ["Lomonaco, V.", "Pellegrini, L.", "Cossu, A.", "Carta, A.", "Graffieti, G.", "Hayes, T.L.", "De Lange, M.", "Masana, M.", "Pomponi, J.", "van de Ven, G.M."]
    year: 2021
    venue: "CVPR Workshops"
    url: null
    arxiv_id: null
  - title: "Gradient episodic memory for continual learning"
    authors: ["Lopez-Paz, D.", "Ranzato, M."]
    year: 2017
    venue: "NeurIPS"
    url: null
    arxiv_id: null
  - title: "Continual lifelong learning with neural networks: A review"
    authors: ["Parisi, G.I.", "Kemker, R.", "Part, J.L.", "Kanan, C.", "Wermter, S."]
    year: 2019
    venue: "Neural Networks"
    url: null
    arxiv_id: null
  - title: "iCaRL: Incremental classifier and representation learning"
    authors: ["Rebuffi, S.-A.", "Kolesnikov, A.", "Sperl, G.", "Lampert, C.H."]
    year: 2017
    venue: "CVPR"
    url: null
    arxiv_id: null
  - title: "Brain-inspired replay for continual learning with artificial neural networks"
    authors: ["van de Ven, G.M.", "Siegelmann, H.T.", "Tolias, A.S."]
    year: 2020
    venue: "Nature Communications 11:4069"
    url: null
    arxiv_id: null
  - title: "Three types of incremental learning"
    authors: ["van de Ven, G.M.", "Tuytelaars, T.", "Tolias, A.S."]
    year: 2022
    venue: "Nature Machine Intelligence 4:1185-1197"
    url: null
    arxiv_id: null
  - title: "Rehearsal revealed: The limits and merits of revisiting samples in continual learning"
    authors: ["Verwimp, E.", "De Lange, M.", "Tuytelaars, T."]
    year: 2021
    venue: "ICCV pp. 9385-9394"
    url: null
    arxiv_id: null
  - title: "Continual learning through synaptic intelligence"
    authors: ["Zenke, F.", "Poole, B.", "Ganguli, S."]
    year: 2017
    venue: "ICML pp. 3987-3995"
    url: null
    arxiv_id: null
  - title: "Memory aware synapses: Learning what (not) to forget"
    authors: ["Aljundi, R.", "Babiloni, F.", "Elhoseiny, M.", "Rohrbach, M.", "Tuytelaars, T."]
    year: 2018
    venue: "ECCV pp. 139-154"
    url: null
    arxiv_id: null
  - title: "Online continual learning with maximally interfered retrieval"
    authors: ["Aljundi, R.", "Caccia, L.", "Belilovsky, E.", "Caccia, M.", "Lin, M.", "Charlin, L.", "Tuytelaars, T."]
    year: 2019
    venue: "NeurIPS 32"
    url: null
    arxiv_id: null
  - title: "Domain adaptive ensemble learning"
    authors: ["Zhou, K.", "Yang, Y.", "Qiao, Y.", "Xiang, T."]
    year: 2021
    venue: "IEEE Transactions on Image Processing 30:8008-8018"
    url: null
    arxiv_id: null
  - title: "Moment matching for multi-source domain adaptation"
    authors: ["Peng, X.", "Bai, Q.", "Xia, X.", "Huang, Z.", "Saenko, K.", "Wang, B."]
    year: 2019
    venue: "ICCV pp. 1406-1415"
    url: null
    arxiv_id: null
  - title: "Matching networks for one shot learning"
    authors: ["Vinyals, O.", "Blundell, C.", "Lillicrap, T.", "Kavukcuoglu, K.", "Wierstra, D."]
    year: 2016
    venue: "NeurIPS 30 pp. 3637-3645"
    url: null
    arxiv_id: null
  - title: "Imagenet large scale visual recognition challenge"
    authors: ["Russakovsky, O.", "Deng, J.", "Su, H.", "Krause, J.", "Satheesh, S.", "Ma, S.", "Huang, Z.", "Karpathy, A.", "Khosla, A.", "Bernstein, M."]
    year: 2015
    venue: "IJCV 115(3):211-252"
    url: null
    arxiv_id: null
  - title: "Continual learning for recurrent neural networks: An empirical evaluation"
    authors: ["Cossu, A.", "Carta, A.", "Lomonaco, V.", "Bacciu, D."]
    year: 2021
    venue: "Neural Networks 143:607-627"
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Average accuracy on the first task when using ER (class- and domain-incremental). Per-iteration evaluation reveals sharp, transient drops: the stability gap."
  page: 5
  image_path: "figures/de-lange-2022-stability-gap-fig.png"
---

# Continual Evaluation for Lifelong Learning: Identifying the Stability Gap

**Authors:** Matthias De Lange, Gido M. van de Ven, Tinne Tuytelaars (KU Leuven)
**Published:** May 2022 (v2 March 2023) · ICLR 2023 · [Source](https://arxiv.org/abs/2205.13452)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

State-of-the-art continual learning methods do not actually "remember" past tasks smoothly the way the field has long claimed — they catastrophically forget at every task boundary and then *recover*, and the field had missed this because it only evaluated at task boundaries (i.e., after the recovery had happened). The authors introduce **per-iteration continual evaluation** and three new worst-case metrics (min-ACC, WC-ACC, windowed-forgetting WF^w) and show that experience replay (ER), gradient episodic memory (GEM), elastic weight consolidation (EWC), synaptic intelligence (SI), and learning-without-forgetting (LwF) all exhibit a sharp transient drop in old-task accuracy in the first few iterations of training on a new task. On class-incremental Split-MiniImagenet, standard ACC reports 32.9%, but min-ACC = 0.5% and WC-ACC = 4.1% — i.e., old-task accuracy briefly collapses to near zero. They call this transient collapse the **stability gap**, show it grows with task dissimilarity (in Rotated-MNIST it grows from 0.7% to 9.8% forgetting as rotation goes 10°→80°), and give a gradient-decomposition argument for *why* it happens: the stability gradient ∇L_stability has near-zero norm right after a task switch, so the plasticity gradient ∇L_plasticity dominates for the first few updates and overwrites prior knowledge before replay/regularization can react.

## Key Takeaway

The "stability gap" is the gap between what task-boundary evaluation reports and what the model actually does in the worst case during a task transition: even continual-learning methods designed to prevent forgetting suffer a sharp, temporary collapse in old-task accuracy at every task boundary, and that collapse has been hidden by an evaluation convention (evaluate only at task transitions, after recovery) rather than fixed by any algorithm. The contribution is half methodological (per-iteration evaluation + min-ACC, WC-ACC, WF^w as worst-case metrics) and half mechanistic (a gradient-decomposition story showing why ER, GEM, EWC, SI, and LwF all have ‖∇L_stability‖ ≈ 0 in the first iterations of a new task, leaving the plasticity gradient unopposed). The practical bite: if a continual learner is deployed in any setting where the worst-case matters (safety-critical inference, adversarial data streams, real-time agents), reporting only end-of-task ACC is misleading by 20–40 percentage points.

## Implications

1. **Continual learning benchmarks need a worst-case axis.** Reporting end-of-task average accuracy alone is now demonstrably insufficient — papers in the field should additionally report min-ACC, WC-ACC, or WF^w. The authors' open-source `ContinualEvaluation` repo plus integration with the Avalanche library lower the cost of doing this.
2. **Safety-critical and real-time deployments are exposed.** Any system that infers on incoming data while the model is mid-update (autonomous driving, medical triage, recommendation re-ranking under drift) can see brief but extreme accuracy crashes after a distribution shift. The paper explicitly calls out that an adversary controlling the data stream could *induce* such crashes by triggering a synthetic distribution shift.
3. **Replay-style methods don't work the way we thought.** The conventional intuition for ER/GEM was that the buffer's stability gradient continuously counter-balances forgetting. The gradient analysis here shows the stability gradient is actually near-zero exactly when it would be most needed (at task transitions, because the model has already converged on buffer samples). Stability is preserved by *relearning* the buffer after the drop, not by *preventing* the drop. This reframes how mitigation should be designed.
4. **The "human brain analogy" for current CL methods is shakier than claimed.** Humans seem not to show transient catastrophic forgetting on task boundaries; current ANNs do. The paper notes this as an open biological question and reframes it as a gap between aspiration ("learn like humans") and reality ("forget and recover at every boundary").
5. **Task similarity is a major confound in benchmarks.** The Rotated-MNIST experiment shows the stability gap nearly doubles in absolute forgetting between φ=60° and φ=80° while standard FORG barely moves (Δ = 1.1%). Benchmarks that pick "convenient" task sequences may be systematically underestimating real-world performance variance.
6. **For LLM-agent memory work specifically** (which is downstream from this paper in the authors' citation graph): the lesson is that "no forgetting between sessions" measured at session boundaries can hide intra-session collapses. Any LLM-agent memory benchmark that evaluates after batched ingestion (rather than mid-ingestion) inherits exactly this blind spot.

## How to Apply It (method)

A practitioner who wants to use the paper's framework on their own continual learner:

1. **Instrument per-iteration evaluation.** Wrap the training loop so that every ρ_eval iterations (start with ρ_eval = 1 for the most fine-grained view; appendix B shows ρ_eval = 100 is a tractable compromise on large benchmarks), the model is evaluated on the held-out test set of every previously-seen task.
2. **Make evaluation tractable.** Subsample each evaluation task's test set to ~1k examples (the paper validates this against the full test set with negligible bias). For larger sets of past tasks, optionally bin similar tasks via task2vec into fixed-capacity evaluation bins.
3. **Compute the new metrics.**
   - min-ACC = average over previous tasks of the *minimum* accuracy seen on that task since it was learned (Eq. 2).
   - WC-ACC = (1/k)·A(current task) + (1−1/k)·min-ACC (Eq. 6); lower-bounds final ACC.
   - WF^w = average maximum accuracy drop in any window of w iterations (Eq. 4); the paper uses w = 10 and w = 100. Doesn't need task identifiers, so it works on task-agnostic streams.
   - WP^w = symmetric upward-window plasticity counterpart.
4. **Report both task-based (ACC, FORG) and continual (min-ACC, WC-ACC, WF^w) metrics side-by-side.** Divergence between the two columns IS the stability gap.
5. **Diagnose mechanistically by gradient decomposition.** Split your loss as L = α·L_plasticity + (1−α)·L_stability (Eq. 8 — the exact decomposition for ER, GEM, LwF, EWC, SI is given in §5). Log ‖∇L_stability‖ per iteration. If you see ‖∇L_stability‖ ≈ 0 in the first ~5–50 iterations after a task boundary, you have the classic stability gap; the fix is to introduce a non-zero stability signal *before* the plasticity gradient is applied (e.g., warm-start by replaying buffer-only for a few iterations before mixing in new-task data).
6. **Use the open-source code.** `github.com/mattdl/ContinualEvaluation` (Avalanche-based) reproduces all main results out of the box.
7. **Run a task-similarity ablation.** Reproduce the Rotated-MNIST controlled experiment (φ ∈ {10°, 30°, 60°, 80°}) on your own setup before claiming your method tolerates real distribution shift — this is where the gap blows up.

## Best Figure

![Figure 2 — Average accuracy on the first task when using ER across four continual learning benchmarks; per-iteration evaluation reveals the stability gap (page 5)](figures/de-lange-2022-stability-gap-fig.png)

**Image Candidates:**
- Figure 2 (p. 5): Four-panel grid showing ER first-task accuracy on Split-MNIST, Split-CIFAR10, Split-MiniImagenet, Mini-DomainNet under different evaluation periodicities — the canonical visualization of the stability gap.
- Figure 4 (p. 8): GEM vs. ER accuracy curves + per-iteration ‖∇L_stability‖ norms on Split-MNIST — ties the empirical drop to the gradient-mechanism story in one figure.
- Figure 3 (p. 7): Rotated-MNIST controlled task-similarity experiment showing the stability gap deepening as φ grows from 10° to 80°.

**Best Image — Figure 2: Average accuracy on the first task when using ER across class- and domain-incremental benchmarks.**

This is the figure the paper opens with as evidence and the one most people will cite. Each of the four panels (a) Split-MNIST, (b) Split-CIFAR10, (c) Split-MiniImagenet, (d) Mini-DomainNet shows the accuracy on Task 1 across the entire training stream. Three curves are overlaid: ρ_eval = 1 (per-iteration evaluation, orange), ρ_eval = 100 (blue), and standard task-based evaluation (red diamonds, only at task transitions). The story is told in a single glance: the red diamonds tell the comforting "ER mostly retains Task 1" story; the orange ρ_eval = 1 curve reveals deep transient crashes at every task boundary — on Split-CIFAR10 Task 1 accuracy crashes from ~95% to near 0% momentarily, on Split-MiniImagenet to ~0.5%. The horizontal lines mark min-ACC averaged over seeds, making explicit how far below the standard ACC the worst case actually sits. The figure simultaneously demonstrates (i) the gap is real, (ii) it's invisible without fine-grained evaluation, (iii) it generalizes across both class- and domain-incremental learning, and (iv) it gets *more* hidden the coarser your evaluation periodicity becomes. This is the entire thesis of the paper in one image.

## What Experts Overlook

A careful reader who already works in continual learning still tends to miss several things this paper actually says:

- **The stability gap is not the same as catastrophic forgetting.** Catastrophic forgetting is the *permanent* loss measured at the end of a task; the stability gap is *transient* loss that recovers. The paper's correlation analysis (Fig. 9, Appendix D.5) shows the two metrics (FORG and WF^10) are only weakly correlated on the harder benchmarks (ρ = −0.37 on Split-CIFAR10, ρ = 0.61 on Split-MiniImagenet). So one cannot be predicted from the other — they are genuinely different phenomena, and a method that fixes FORG may leave the stability gap untouched.
- **Stability is preserved by *relearning*, not by *preventing* loss.** This is the key conceptual reframe in §5. The conventional story for ER is "the buffer gradient counter-balances forgetting." The actual story the paper proves is "the buffer gradient is near-zero at the moment of forgetting because ER has already converged on the buffer; what saves you is that *after* the plasticity update perturbs the parameters, the buffer gradient grows again and the model re-learns the buffer." If you internalize this, the design space for mitigation changes — you'd want a stability signal that's pre-emptively active during the transition, not one that activates after the damage.
- **GEM is *worse* than ER on the stability gap, not better.** This is the paper's most counter-intuitive empirical finding. GEM was designed explicitly to enforce non-negative-loss constraints on previous tasks, which one would expect to prevent the gap. But Figure 4 shows GEM's min-ACC drops *further* than ER's on Split-MNIST tasks T3 and T4 because GEM's stability gradient also collapses to near-zero magnitude on task transitions (the QP projection produces ‖g̃ − g_t‖ ≈ 0 when constraints are only slightly violated). Constraint-based methods aren't a free pass.
- **The gap holds even when you store every sample.** Appendix D.2 shows that with M = |S| (i.e., the buffer literally contains every example ever seen — effectively joint training), the stability gap *still* appears, just smaller. So "more memory" is not a cure. The gap is structural to the optimizer's update pattern, not just a function of buffer capacity.
- **Standard ρ_eval = 1 evaluation is feasible on real benchmarks.** Many readers assume per-iteration evaluation is prohibitively expensive. Appendix B shows that with 1k-subsample evaluation sets, ρ_eval = 1 on Split-MiniImagenet runs without unusual hardware. Practitioners who currently skip continual evaluation citing "compute cost" are likely overestimating it.
- **The gap is bigger in online continual learning than in 10-epoch settings.** Appendix D.1 shows that under single-pass streaming (each sample observed once), ER's min-ACC on Split-MNIST is 50.8 ± 8.7% with WF^10 of 39.9 ± 7.4% — i.e., transient forgetting nearly 8× larger than the FORG metric (5.3%) reports. This is the more deployment-realistic regime and the gap is worse there, not better.
- **The phenomenon transfers off image classification.** Appendix D.4 reproduces the stability gap on Synthetic Speech Commands (30 spoken words, class-incremental). The community sometimes treats CL benchmarks as a vision-only sport — this paper shows the phenomenon is modality-independent.

## Extracted Prompts

This is a benchmarks/methodology paper with no LLM prompts in it, so there are no extracted prompts to transplant.

The closest "operational" things the paper hands you are the equations and a procedure. The procedure is in **How to Apply It (method)** above. The core equations to keep nearby for any continual-learning evaluation harness:

- **min-ACC at task T_k** = (1/(k−1)) Σ_{i<k} min_n A(E_i, f_n), n ranging from after task i was learned to current iteration t.
- **WC-ACC at iteration t** = (1/k)·A(E_k, f_t) + (1 − 1/k)·min-ACC.
- **WF^w** = average over evaluation tasks of the maximum accuracy drop in any window of w consecutive evaluations.
- **Gradient decomposition** ∇L = α∇L_plasticity + (1−α)∇L_stability, with per-method definitions of L_stability:
  - ER: L_stability is the loss on the replay buffer M.
  - GEM: L_stability = g̃ − g_t when QP-constraints hgt, gni ≥ 0 are violated, else 0 (Eq. 9).
  - LwF: L_stability = KL(f_{t|T_{k−1}|}(x_t) ‖ f_t(x_t)).
  - EWC/SI: L_stability = (θ − θ*)^T Ω (θ − θ*).

A useful diagnostic prompt for a human collaborator (not an LLM, but in the spirit of "extracted prompts"): *"For our continual learner, log ‖∇L_stability‖ at every iteration. After every task transition, plot the first 50 iterations. If the norm starts at ≈ 0 and grows over the next 5–20 steps while accuracy on the previous task drops then recovers, you have a stability gap. Report min-ACC and WC-ACC alongside ACC."*

## Citations

The full citation list is in this digest's `citations:` frontmatter (26 references extracted). Top 10 most-cited / most-load-bearing for understanding the paper:

- Chaudhry et al. 2019b — Continual learning with tiny episodic memories (ER baseline, arXiv 1902.10486)
- Chaudhry et al. 2018 — Riemannian walk for incremental learning (FORG metric origin)
- Lopez-Paz & Ranzato 2017 — Gradient episodic memory (GEM baseline)
- Kirkpatrick et al. 2017 — Overcoming catastrophic forgetting in neural networks (EWC baseline, PNAS)
- Zenke, Poole & Ganguli 2017 — Continual learning through synaptic intelligence (SI baseline)
- Li & Hoiem 2017 — Learning without forgetting (LwF baseline)
- De Lange et al. 2021 — A continual learning survey (TPAMI; setup grounding)
- van de Ven, Tuytelaars & Tolias 2022 — Three types of incremental learning (Nature Machine Intelligence; benchmark taxonomy)
- French 1999 — Catastrophic forgetting in connectionist networks (origin of the problem)
- Grossberg 1982 — Stability-plasticity dilemma (origin of the framing)

## Related Digests

- [[thorne-2020-ewc-bias-inoculation]] — Elastic weight consolidation for better bias inoculation. Uses the EWC method this paper shows is vulnerable to the stability gap.
- [[mcclelland-1995-complementary-learning-systems]] — Why There Are Complementary Learning Systems in the Hippocampus and Neocortex. Biological grounding for the "stability vs plasticity" framing that motivates this paper's question about whether human brains exhibit a stability gap.
- [[logan-2026-continuum-memory-architectures]] — Continuum Memory Architectures for Long-Horizon LLM Agents. Modern downstream work on continual memory in LLM agents — inherits the evaluation problem this paper diagnoses.
- [[ai-2026-memorybench-continual-learning]] — MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems. The LLM-era analogue of the evaluation problem; same blind spot if it only evaluates between sessions.
- [[hu-2026-evermemos]] — EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning. Already references "stability gap" by name.

## Reviewer Notes

**Overall severity: Clean.**

Spot-checks against the paper text:
- Title, authors, KU Leuven affiliation, arXiv ID 2205.13452 v2, ICLR 2023 venue: verified against page 1.
- Split-MiniImagenet numbers (ACC 32.9 ± 0.8, FORG 32.3 ± 1.0, min-ACC 0.5 ± 0.2, WC-ACC 4.1 ± 0.3 at ρ_eval=1): verified against Table 1.
- Rotated-MNIST forgetting span (ACC drop 6.6% from φ=10 to φ=80, min-ACC drop 25.1%, WF^10 drop 5.0% between φ=60 and φ=80): verified against Table 2.
- Online CL Split-MNIST numbers (FORG 5.3%, WF^10 39.9%, min-ACC 50.8%): verified against Table 5.
- Set of methods analyzed (ER, GEM, EWC, SI, LwF): verified against §5 and §5.1.
- Pearson correlation values (Split-MNIST ρ=0.86, Split-CIFAR10 ρ=−0.37, Split-MiniImagenet ρ=0.61): verified against Figure 9.
- Eq. 6 form of WC-ACC = (1/k)·A(current) + (1−1/k)·min-ACC: verified against §3.3.
- Claim that the gap persists even when the buffer stores all samples (M = |S|): verified against Appendix D.2.
- Speech-domain reproduction on Synthetic Speech Commands: verified against Appendix D.4.

One framing nuance worth flagging (not a fact error): the paper says "stability is preserved by relearning, not preventing loss" — this is a conceptual claim derived from the gradient-norm analysis plus the recovery shape of the curves, not a separate ablation that proves the counterfactual. The digest reports it as the authors' conceptual analysis, which is accurate.

No fabricated numbers or invented connections detected.

---

*Digested 2026-05-20 via /digest-paper (cycle 4 orbit). Lens: generic.*
