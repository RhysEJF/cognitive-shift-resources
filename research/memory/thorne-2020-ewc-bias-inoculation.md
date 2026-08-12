---
corpus: agentic-memory
kind: paper-digest
slug: thorne-2020-ewc-bias-inoculation
title: "Elastic weight consolidation for better bias inoculation"
authors:
  - "Thorne, James"
  - "Vlachos, Andreas"
year: 2020
publication_date: "2021-02"
venue: "arXiv preprint (EACL 2021)"
source_url: "https://arxiv.org/abs/2004.14366"
doi: null
arxiv_id: "2004.14366"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "When you fine-tune a model to fix a bias, the cheapest insurance against catastrophic forgetting isn't more data or new architecture — it's a per-parameter importance weight (Fisher diagonal) that costs ~2-25 seconds to estimate and lets the model decide for itself which neurons are 'load-bearing' for the original task."
topics:
  - catastrophic-forgetting
  - elastic-weight-consolidation
  - continual-learning
  - bias-mitigation
  - fine-tuning
  - fact-verification
  - natural-language-inference
  - memory-consolidation
  - regularization
tags:
  - paper
  - memory-architecture
  - engram-aggregate
  - engram-maintain
  - regularization
  - parameter-importance
  - fisher-information
entities:
  - thorne-james
  - vlachos-andreas
  - kirkpatrick-james
  - schuster-tal
related_digests:
  - mcclelland-1995-complementary-learning-systems
  - radford-2018-gpt1
  - liu-2025-memverse
  - patel-2026-engram
  - mao-2026-agent-memory-circuits
  - latimer-2025-hindsight-memory
citations:
  - title: "Where is Your Evidence: Improving Fact-checking by Justification Modeling"
    authors: ["Tariq Alhindi", "Savvas Petridis", "Smaranda Muresan"]
    year: 2018
    venue: "Proceedings of FEVER Workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "MultiFC: A Real-World Multi-Domain Dataset for Evidence-Based Fact Checking of Claims"
    authors: ["Isabelle Augenstein", "Christina Lioma", "Dongsheng Wang", "et al."]
    year: 2019
    venue: "EMNLP-IJCNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Beat the AI: Investigating Adversarial Human Annotations for Reading Comprehension"
    authors: ["Max Bartolo", "Alastair Roberts", "Johannes Welbl", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Enhanced LSTM for Natural Language Inference"
    authors: ["Qian Chen", "Xiaodan Zhu", "Zhenhua Ling", "et al."]
    year: 2016
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."]
    year: 2019
    venue: "NAACL-HLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Catastrophic forgetting in connectionist networks"
    authors: ["Robert M French"]
    year: 1999
    venue: "Trends in Cognitive Sciences"
    doi: null
    url: null
    arxiv_id: null
  - title: "AllenNLP: A Deep Semantic Natural Language Processing Platform"
    authors: ["Matt Gardner", "Joel Grus", "Mark Neumann", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Annotation Artifacts in Natural Language Inference Data"
    authors: ["Suchin Gururangan", "Swabha Swayamdipta", "Omer Levy", "et al."]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Overcoming catastrophic forgetting in neural networks"
    authors: ["James Kirkpatrick", "Razvan Pascanu", "Neil Rabinowitz", "et al."]
    year: 2017
    venue: "PNAS"
    doi: "10.1073/pnas.1611835114"
    url: null
    arxiv_id: null
  - title: "Inoculation by Fine-Tuning: A Method for Analyzing Challenge Datasets"
    authors: ["Nelson F. Liu", "Roy Schwartz", "Noah A. Smith"]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "RoBERTa: A Robustly Optimized BERT Pretraining Approach"
    authors: ["Yinhan Liu", "Myle Ott", "Naman Goyal", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "End-to-End Bias Mitigation by Modelling Biases in Corpora"
    authors: ["Rabeeh Karimi Mahabadi", "Yonatan Belinkov", "James Henderson"]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "New insights and perspectives on the natural gradient method"
    authors: ["James Martens"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference"
    authors: ["Thomas R. McCoy", "Ellie Pavlick", "Tal Linzen"]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Stress Test Evaluation for Natural Language Inference"
    authors: ["Aakanksha Naik", "Abhilasha Ravichander", "Norman Sadeh", "et al."]
    year: 2018
    venue: "COLING"
    doi: null
    url: null
    arxiv_id: null
  - title: "Hypothesis Only Baselines in Natural Language Inference"
    authors: ["Adam Poliak", "Jason Naradowsky", "Aparajita Haldar", "et al."]
    year: 2018
    venue: "*SEM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fake News Challenge"
    authors: ["Dean Pomerleau", "Delip Rao"]
    year: 2017
    venue: "fakenewschallenge.org"
    doi: null
    url: "http://fakenewschallenge.org/"
    arxiv_id: null
  - title: "An Overview of Multi-Task Learning in Deep Neural Networks"
    authors: ["Sebastian Ruder"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Domain Adaptive Inference for Neural Machine Translation"
    authors: ["Danielle Saunders", "Felix Stahlberg", "Adrià de Gispert", "et al."]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards Debiasing Fact Verification Models"
    authors: ["Tal Schuster", "Darsh J Shah", "Yun Jie Serene Yeo", "et al."]
    year: 2019
    venue: "EMNLP-IJCNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the Importance of Delexicalization for Fact Verification"
    authors: ["Sandeep Suntwal", "Mithun Paul", "Rebecca Sharp", "et al."]
    year: 2019
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Overcoming Catastrophic Forgetting During Domain Adaptation of Neural Machine Translation"
    authors: ["Brian Thompson", "Jeremy Gwinnup", "Huda Khayrallah", "et al."]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "FEVER: a large-scale dataset for Fact Extraction and VERification"
    authors: ["James Thorne", "Andreas Vlachos", "Christos Christodoulopoulos", "et al."]
    year: 2018
    venue: "NAACL-HLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference (MultiNLI)"
    authors: ["Adina Williams", "Nikita Nangia", "Samuel Bowman"]
    year: 2018
    venue: "NAACL-HLT"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Pareto frontiers of fine-tuning BERT and ESIM models showing FT+EWC dominates FT"
  page: 4
  image_path: "figures/thorne-2020-ewc-bias-inoculation-fig.png"
---

# Elastic weight consolidation for better bias inoculation

**Authors:** James Thorne, Andreas Vlachos
**Published:** 2021-02 · [Source](https://arxiv.org/abs/2004.14366)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Thorne and Vlachos show that Elastic Weight Consolidation (EWC) — a Fisher-information-weighted L2 penalty originally proposed by Kirkpatrick et al. (2017) to keep neural nets from forgetting old tasks — Pareto-dominates plain fine-tuning when you use small "inoculation" datasets to debias sentence-pair classifiers. On FEVER fact verification with the Schuster et al. (2019) symmetric counterfactual set (~1,420 instances; <1% of FEVER), plain fine-tuning of BERT-Base lifted symmetric-set accuracy from 74.77% → 87.07% but collapsed original FEVER accuracy from 86.88% → 78.82%; adding EWC (λ=10⁷, FT learning rate 4·10⁻⁶, Fisher diagonal estimated from 2,000 samples in ~25s per epoch) gave 85.11% on the symmetric set while holding FEVER at 82.23% — significantly better than both plain fine-tuning and ordinary L2 regularization (p<0.05) across ESIM+GloVe, ESIM+ELMo, BERT-Base, and RoBERTa-Base. EWC also stacks on top of Product-of-Experts and Debiased Focal Loss, and the same pattern reproduces on MultiNLI antonym and numerical-reasoning stress tests. Practical takeaway: when you're consolidating a small corrective signal into a model that already encodes a lot you want to keep, regularize updates by per-parameter importance — not uniformly, not by intuition about which layers matter.

## Key Takeaway

The conventional fix for "the model now forgets the original task" is more data, bigger architectures, or multi-task heads — but here the cheapest, most surgical answer is a per-parameter importance score that costs 2-25 seconds to estimate and a single hyperparameter (λ) to tune. The model itself tells you which weights are load-bearing for the old task; you just have to ask it. The counter-intuitive bit: this importance signal — the Fisher information diagonal — comes from squaring the gradients you'd compute anyway, so it's almost free. Treating all parameters as equally protectable (plain L2) is strictly dominated; treating them as equally overwritable (plain fine-tuning) is also strictly dominated. **EWC** [E·N·A·M] **A — Aggregate / M — Maintain**: this is consolidation as a maintenance discipline. The paper makes a quiet but important architectural claim: when you ingest a new memory ("this counter-example refutes the model's prior bias"), you must simultaneously **score how much each existing parameter mattered for the prior memory state** and use that score to gate the update. This generalises directly to AI memory systems — the analog of "Fisher importance" for a memory architect is per-memory or per-edge provenance weighting that determines update permission.

## Implications

- **[A — Aggregate] Per-parameter importance is the missing piece in most memory-consolidation pipelines**: Memory systems that fold experiences into patterns typically use uniform overwrite or LRU-style eviction. EWC's lesson — store an importance map alongside the artifact itself — translates to: when you compile session memories into a long-lived pattern file, attach a per-claim "Fisher-like" importance score (how many downstream decisions depend on this claim) and gate updates by it. Don't let a single new session rewrite a claim that 50 prior sessions reinforced unless its importance-weighted disagreement clears a threshold.

- **[G — Ground] Consolidation needs an "old-task evaluation set" that survives the update**: Thorne keeps FEVER as a held-out original-task eval throughout fine-tuning — that's the only way "catastrophic forgetting" is even measurable. Memory architects should keep a small held-out set of canonical queries ("what does the user believe about X") and replay it after every consolidation pass. If consolidation moves answers on the held-out set, you've forgotten — surface this as a contradiction, don't silently smooth it.

- **[M — Maintain] Regularization beats merging when the new data is <1% of the old**: Merging the symmetric set (700 instances) with FEVER's training data gave only "modest improvements" because the small signal was drowned out (Table 1: ESIM+GloVe merged 79.57% vs FT+EWC 73.20% on FT-test). For memory systems: when a small but important contradiction arrives (e.g., "Nadia is the user's partner, not a sales prospect"), don't try to merge it into the entire training/retrieval pool and hope re-ranking surfaces it. Instead, treat it as an inoculation pass with importance-gated update.

- **[N — Network · M — Maintain] L2 is a strict baseline you should still run**: The paper shows FT+EWC dominates FT+L2 — but FT+L2 still beats plain FT. For memory architects: uniform regularization (e.g., "decay all old memories at rate γ") is better than no regularization, but importance-weighted regularization is strictly better. Build both into your update pipeline; treat L2 as the floor, EWC-style as the target.

- **[E — Encode · A — Aggregate] Write-time importance estimation is cheap**: Fisher diagonal estimation took 2s (ESIM) to 25s (BERT/RoBERTa) on 2,000 samples — trivial relative to the model's training time. For agentic memory: the equivalent — scoring how much each memory entry contributes to current behavior — can be done at write time with a cheap pass over a fixed reference set of "what we know we care about." Don't compute it lazily at query time; bake it into the write path.

- **[A — Aggregate] EWC stacks with architectural debiasing — they're orthogonal interventions**: FT+EWC on top of PoE and DFL improved both — meaning regularization-style consolidation is complementary to architectural moves like graph reshaping or polyglot stores. Don't pick one; layer them. In memory terms: keeping per-edge importance scores is compatible with adding a graph layer or compiled-bundle layer on top.

- **[G — Ground] Hyperparameter sweeps reveal the trade-off curve — single λ values mislead**: Figure 2's Pareto frontiers are constructed by sweeping λ from 10⁶ to 10⁸ (10 values) crossed with 3 learning rates. The point isn't "use λ=10⁷"; it's "trace the frontier and pick where you want to sit on the old-task-vs-new-task trade-off." Memory architects evaluating consolidation strategies should report Pareto curves, not single configurations, because the "right" trade-off depends on the cost of forgetting in their domain.

- **[E — Encode] Label-distribution shift is the silent killer of fine-tuning passes**: Thorne explicitly notes the antonym stress-test contains only "contradiction" labels — so plain fine-tuning collapses to predicting contradiction every time (yellow dashed line, Figure 3). For memory systems: when you ingest a batch of corrections that all skew one way (e.g., a week of negative feedback about a contact), don't let it rewrite the model's prior — EWC-style importance gating becomes essential, not just nice-to-have.

## How to Apply It (method)

**Scenario:** You run an agentic memory system (markdown vault + vector store, like Flow OS) that has accumulated ~1,000 session memories about a user's beliefs, contacts, and decisions. A new piece of data arrives — say, 30 corrections from a single weekend session that contradict prior memories ("actually I've changed my mind about X", "Y is no longer a customer", "Z is my partner not a prospect"). You want to consolidate these corrections into the long-lived memory layer without catastrophically rewriting the model's prior, correct beliefs about the rest of the user's world. Plain fine-tuning of an embedding/reranker on the 30 new examples will overshoot; ignoring them will leave stale claims in retrieval. You want an EWC-style consolidation pass.

**Steps:**

1. **Define your "original task" eval set**: Before any consolidation, write a held-out set of ~50 canonical queries that exercise the model's prior, known-good behavior — facts you trust, contacts you've verified, decisions that haven't changed. This is your `D_original` evaluation. Without it, you cannot measure forgetting and you cannot tune λ.

2. **Estimate Fisher importance for each memory artifact**: For each memory file (or each chunk in your vector store), compute an importance score. Concretely, for a learned-parameter system (e.g., a fine-tuned reranker), do the EWC recipe — sample 2,000 instances from `D_original`, run forward+backward, square the per-parameter gradients, average. For a non-parametric memory store, the analog is: score each memory by how often it's the top-ranked retrieval result over the eval set queries, weighted by the downstream decision it fed. High-Fisher memories = "load-bearing" — touching them costs you.

   ```
   For each parameter θ_i (or each memory m_i):
     F_i = E_{(x,y) ~ D_original} [ (∂ log p(y|x; θ_i))^2 ]
   ```

3. **Define the consolidation loss with importance gating**:

   ```
   L(θ) = L_FT(θ) + (λ/2) * sum_i [ F_i * (θ_i - θ_i*)^2 ]
   ```

   where `θ_i*` is the parameter value (or memory content) before consolidation, and λ controls how much you penalize movement on high-importance parameters. For a markdown memory system: `λ * F_i` is the threshold a new claim must clear to overwrite memory `m_i`.

4. **Cross-validate λ via the trade-off**: Sweep λ across at least 10 values spanning two orders of magnitude (Thorne used 10⁶ to 10⁸). For each λ, measure both `D_original` accuracy (forgetting) and `D_correction` accuracy (new-task learning). Plot the Pareto frontier. Choose the λ that sits where you want on the trade-off — if your domain punishes forgetting hard (e.g., a contact's name), bias toward high λ; if corrections are urgent (e.g., a stale claim about a customer status), bias low.

5. **Run the consolidation pass with the chosen λ**: Apply the gated update. For parametric systems, this is gradient descent on `L(θ)`. For memory vaults, this is the update policy: for each candidate edit, accept if `(novelty * confidence) > λ * F_i`, else write to a contradictions/ sidecar for review.

6. **Re-evaluate `D_original` after consolidation, every time**: This is the catastrophic-forgetting check. If accuracy on `D_original` drops more than your tolerance (Thorne's papers tolerate ~3-5 percentage points for ~10-point gains on the new task), the consolidation pass needs re-tuning or rollback. Surface the regression as a visible event, not a silent drift.

7. **Stack with other interventions**: EWC composes with architectural mitigations. If you also have a debiasing reranker, a contradiction surfacer, or a graph-overlay store, layer EWC-style importance gating on top — Thorne shows FT+EWC stacks with PoE/DFL for additive gains.

**Expected outcome:** A consolidation pipeline that ingests new corrections without silently rewriting load-bearing memories. You end up with (a) a measurable forgetting rate on every consolidation pass, (b) a tunable trade-off between staleness and over-correction, (c) a surfaced log of "high-importance memories the update tried to touch" for human review. This is the "AI as maintainer, not oracle" pattern — the memory system tells you what it's about to forget before it forgets it, and asks permission proportional to importance.

## Best Figure

![Figure 2 — Pareto frontiers of fine-tuning BERT and ESIM models showing FT+EWC dominates FT (page 4)](figures/thorne-2020-ewc-bias-inoculation-fig.png)

**Image Candidates:**
- Figure 1 (p. 1): Block diagram of the hypothesis-only bias problem and the EWC fix — useful for slides explaining the setup but doesn't show evidence.
- Figure 2 (p. 4): Pareto frontiers showing FT+EWC strictly dominating FT on both BERT+PoE and ESIM+DFL — the paper's central evidential claim in a single view.
- Table 1 (p. 4): Headline numbers across all four model architectures (ESIM+GloVe, ESIM+ELMo, BERT-Base, RoBERTa-Base) with significance markers.

**Best Image: Figure 2 — Pareto frontiers of fine-tuning BERT and ESIM models showing FT+EWC dominates FT.**

**Slide Caption:** EWC (purple) dominates plain fine-tuning (orange) across the entire trade-off curve — for every level of new-task accuracy you'd accept, EWC gives back more of the original task.

**Description:** Figure 2 plots two scatter-plus-line panels: the left for BERT trained with Product-of-Experts (PoE) bias mitigation, the right for ESIM trained with Debiased Focal Loss (DFL). The x-axis is relative accuracy on the symmetric (FT-test) counterfactual set; the y-axis is relative accuracy on the original FEVER task. Each curve is the Pareto frontier traced by sweeping hyperparameters (learning rate for FT, learning rate × λ for FT+EWC) — Appendix D.5 spec. Blue x's are PoE/DFL alone, orange is +FT, purple is +FT+EWC. The story is visually unambiguous: the purple FT+EWC curve sits above-right of the orange FT curve across the entire range, meaning for any chosen level of new-task accuracy, EWC preserves strictly more of the original task. The mechanism — Fisher-information-weighted parameter penalty — is what enables this dominance, and the figure compresses the paper's central claim into one comparison.

## What Experts Overlook

Most experts read this paper as "use EWC instead of L2 for fine-tuning" and stop there. They miss that the **empirical Fisher diagonal must be recomputed before every epoch** (Section 2, end: "diagonal elements are approximated through squaring first-order gradients from a sample of instances, recomputed before each epoch"). This isn't a one-shot importance estimate frozen at the start of fine-tuning — it's a moving target. As the model's parameters shift during fine-tuning, what counts as "important for the original task" also shifts, and the regularizer follows. This is why the paper specifies the Fisher estimation procedure as part of the training loop rather than a pre-processing step, and why the cost numbers in Appendix C (2s for ESIM, 25s for BERT/RoBERTa) include "per-epoch" semantics — not "per-run."

**Why it matters:** The recomputation is what keeps EWC a tractable approximation of the (intractable) full continual-learning objective. A stale Fisher estimate would still regularize you toward the initial parameters, but it wouldn't reflect the current optimization landscape — meaning some weights that started "unimportant" but became important under fine-tuning would be free to drift, and some that started important but were de-emphasized would be over-protected. The per-epoch refresh is what makes EWC track which parameters are currently load-bearing, not historically. This is the bridge between the elegant theory (Fisher information at the local minimum equals the Hessian) and the messy practice (the local minimum is moving).

**Example of good use:** A memory system applying EWC-style importance gating to a vector store recomputes "how often is memory m_i the top-ranked retrieval result for the canonical eval queries" at the end of every consolidation cycle, not once at system bootstrap. As the corpus evolves (new memories added, some pruned, retrieval distribution shifts), the importance map evolves with it — so a memory that was load-bearing six months ago but is now stale gets less protection, while a memory that has accumulated downstream-decision dependency gets more.

**Example of misapplication:** A team implements "EWC-for-memory" by computing each memory's importance score once at ingestion time and freezing it forever. Six months in, the corpus has drifted — old memories that were peripheral are now central pivots (because related memories link back to them), and old memories that were central are now superseded. But the importance map still reflects the bootstrap state, so the system over-protects the wrong things and under-protects the right things. Consolidation passes start producing "looks fine but actually wrong" updates: the regularizer is no longer pulling toward what currently matters. This is the same failure mode as a static Fisher diagonal, just at the memory-vault scale instead of the parameter scale.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

Full citation list of 24 references in frontmatter `citations:`. Highlights for memory-architecture work:

- **Kirkpatrick, J., Pascanu, R., Rabinowitz, N., et al. (2017).** Overcoming catastrophic forgetting in neural networks. *PNAS* 114(13):3521-3526. — The original EWC paper. Required reading for anyone building EWC-style importance gating.
- **French, R.M. (1999).** Catastrophic forgetting in connectionist networks. *Trends in Cognitive Sciences* 3(4):128-135. — Foundational framing of the catastrophic forgetting problem.
- **Schuster, T., Shah, D.J., Yeo, Y.J.S., et al. (2019).** Towards Debiasing Fact Verification Models. *EMNLP-IJCNLP*. — Source of the symmetric counterfactual evaluation set used in this paper. Treats the problem as a re-weighting (loss-side) intervention rather than parameter regularization.
- **Mahabadi, R.K., Belinkov, Y., Henderson, J. (2020).** End-to-End Bias Mitigation by Modelling Biases in Corpora. *ACL*. — Source of the PoE and DFL baselines Thorne stacks EWC on top of. Architectural bias mitigation that EWC complements.
- **Liu, N.F., Schwartz, R., Smith, N.A. (2019a).** Inoculation by Fine-Tuning: A Method for Analyzing Challenge Datasets. *NAACL*. — The "inoculation" framing this paper extends. Fine-tuning on small targeted sets as a diagnostic.
- **Thompson, B., Gwinnup, J., Khayrallah, H., et al. (2019).** Overcoming Catastrophic Forgetting During Domain Adaptation of Neural Machine Translation. — Earlier EWC application to NMT domain adaptation. Different domain, same recipe.
- **Saunders, D., Stahlberg, F., de Gispert, A., et al. (2019).** Domain Adaptive Inference for Neural Machine Translation. *ACL*. — EWC for NMT (acknowledged in the paper's thanks).
- **Martens, J. (2014).** New insights and perspectives on the natural gradient method. — Source of the empirical-Fisher approximation Thorne uses for efficiency.
- **Ruder, S. (2017).** An Overview of Multi-Task Learning in Deep Neural Networks. — Connects EWC to multi-task framings (regularization toward old solutions is a one-task approximation of multi-task).
- **Naik, A., Ravichander, A., Sadeh, N., et al. (2018).** Stress Test Evaluation for NLI. *COLING*. — Source of the antonym and numerical-reasoning challenge datasets.

## Related Digests

- [[mcclelland-1995-complementary-learning-systems]] — Why There Are Complementary Learning Systems in the Hippocampus and Neocortex. The neuroscience precursor to EWC's "protect the old while learning the new" framing — interleaved learning vs. sharp consolidation.
- [[radford-2018-gpt1]] — Improving Language Understanding by Generative Pre-Training (GPT-1). Uses an auxiliary LM loss (λ=0.1–0.5) during task fine-tuning to prevent catastrophic forgetting of the pretraining distribution — same family of fix as EWC, lower-tech instantiation.
- [[liu-2025-memverse]] — MemVerse: Multimodal Memory for Lifelong Learning Agents. Explicitly rejects "parametric-only (catastrophic-forgetting)" vs. "RAG-only" — runs both pathways, sidestepping the trade-off EWC tries to navigate inside a single model.
- [[patel-2026-engram]] — ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents. Source of the six-dimension framework this digest uses to tag findings.
- [[mao-2026-agent-memory-circuits]] — What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis. Reveals that different memory framework outputs recruit the same internal circuits — relevant because EWC operates at the parameter level where this convergence lives.
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects. Memory architecture with explicit retention/recall/reflection layers — EWC's importance-gating maps to its retention layer.

## Reviewer Notes

**Overall severity:** Clean

All claims in the digest are accurate against the paper text. Specific numbers verified:
- BERT-Base FEVER: 86.88 → 78.82 → 82.23 (Table 1) ✓
- BERT-Base symmetric: 74.77 → 87.07 → 85.11 (Table 1) ✓
- Symmetric set size ~1,420, <1% of FEVER ✓ (Section 3)
- Fisher diagonal estimation cost: ~2s ESIM, ~25s BERT/RoBERTa on 2,000 instances ✓ (Appendix C)
- λ=10⁷ chosen via 5-fold CV, sweep over 10 values 10⁶–10⁸ ✓ (Section 3, Appendix D.5)
- FT learning rate 4·10⁻⁶ for transformers ✓ (Section 3)
- EWC stacks with PoE and DFL ✓ (Section 4.2, Figure 2)
- Per-epoch Fisher recomputation ✓ (Section 2)
- MultiNLI antonym collapse to "contradiction-only" ✓ (Section 4.3)
- Pareto-dominance language matches Figure 2 caption and Section 4.2 ✓

The ENGRAM dimension tagging is interpretive (the paper does not use ENGRAM), but the mapping is honest — clearly labeled as the reviewer's framework, not the paper's claim.
