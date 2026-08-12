---
corpus: agentic-memory
kind: paper-digest
slug: deutch-2024-icl-gd-revisited
title: "In-context Learning and Gradient Descent Revisited"
authors:
  - "Gilad Deutch"
  - "Nadav Magar"
  - "Tomer Bar Natan"
  - "Guy Dar"
year: 2024
publication_date: "2024-03"
venue: "arXiv preprint (later NAACL 2024 Findings)"
source_url: "https://arxiv.org/abs/2311.07772"
doi: null
arxiv_id: "2311.07772"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "The widely-cited claim that in-context learning is implicitly performing gradient descent on the model itself collapses when you add the baselines the original work skipped: untrained transformers match or beat trained ones on the same similarity metrics, and a small change to the metric formula (cosine of update vectors instead of normalized raw vectors) makes the alignment scores deflate further — leaving 'ICL ≈ GD' as at best a weak, layer-causal correspondence rather than a mechanistic identity."
topics:
  - in-context-learning
  - gradient-descent
  - mesa-optimization
  - mechanistic-interpretability
  - transformer-interpretability
  - replication-failure
  - encoding-vs-retrieval
tags:
  - paper
  - icl
  - transformer
  - replication
  - benchmark-critique
  - memory-architecture
  - engram-encode
  - engram-aggregate
entities:
  - deutch-gilad
  - magar-nadav
  - bar-natan-tomer
  - dar-guy
  - dai-damai
  - von-oswald-johannes
  - akyurek-ekin
related_digests:
  - brown-2020-gpt3-few-shot
  - vassilyev-2026-rcl
  - hochreiter-1997-lstm
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "Per-layer SimAOU and SimAM∆ comparison of vanilla GD vs. layer-causal GD"
  page: 7
  image_path: "figures/deutch-2024-icl-gd-revisited-fig.png"
citations:
  - title: "Transformers learn to implement preconditioned gradient descent for in-context learning"
    authors: ["Kwangjun Ahn", "Xiang Cheng", "Hadi Daneshmand", "Suvrit Sra"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "What learning algorithm is in-context learning? Investigations with linear models"
    authors: ["Ekin Akyürek", "Dale Schuurmans", "Jacob Andreas", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Greedy layer-wise training of deep networks"
    authors: ["Yoshua Bengio", "Pascal Lamblin", "Dan Popovici", "et al."]
    year: 2006
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models are few-shot learners"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "Transformers implement functional gradient descent to learn non-linear functions in context"
    authors: ["Xiang Cheng", "Yuxin Chen", "Suvrit Sra"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Why can GPT learn in-context? Language models implicitly perform gradient descent as meta-optimizers"
    authors: ["Damai Dai", "Yutao Sun", "Li Dong", "et al."]
    year: 2023
    venue: "ACL Findings"
    doi: null
    url: null
    arxiv_id: "2212.10559"
  - title: "Analyzing transformers in embedding space"
    authors: ["Guy Dar", "Mor Geva", "Ankit Gupta", "Jonathan Berant"]
    year: 2023
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "The CommitmentBank: Investigating projection in naturally occurring discourse"
    authors: ["Marie-Catherine de Marneffe", "Mandy Simons", "Judith Tonhauser"]
    year: 2019
    venue: "Sinn und Bedeutung"
    doi: null
    url: null
    arxiv_id: null
  - title: "Jump to conclusions: Short-cutting transformers with linear transformations"
    authors: ["Alexander Yom Din", "Taelin Karidi", "Leshem Choshen", "Mor Geva"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "A mathematical framework for transformer circuits"
    authors: ["Nelson Elhage", "Neel Nanda", "Catherine Olsson", "et al."]
    year: 2021
    venue: "Transformer Circuits Thread"
    doi: null
    url: "https://transformer-circuits.pub/2021/framework/index.html"
    arxiv_id: null
  - title: "Transformer feed-forward layers build predictions by promoting concepts in the vocabulary space"
    authors: ["Mor Geva", "Avi Caciularu", "Kevin Ro Wang", "Yoav Goldberg"]
    year: 2022
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "In-context learning creates task vectors"
    authors: ["Roee Hendel", "Mor Geva", "Amir Globerson"]
    year: 2023
    venue: "EMNLP Findings"
    doi: null
    url: null
    arxiv_id: null
  - title: "Risks from learned optimization in advanced machine learning systems"
    authors: ["Evan Hubinger", "Chris van Merwijk", "Vladimir Mikulik", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1906.01820"
  - title: "Transformers learn in-context by gradient descent"
    authors: ["Johannes von Oswald", "Eyvind Niklasson", "Ettore Randazzo", "et al."]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "2212.07677"
  - title: "Uncovering mesa-optimization algorithms in transformers"
    authors: ["Johannes von Oswald", "Eyvind Niklasson", "Maximilian Schlegel", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Interpreting GPT: the logit lens"
    authors: ["nostalgebraist"]
    year: 2020
    venue: "LessWrong blog"
    doi: null
    url: "https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens"
    arxiv_id: null
  - title: "In-context learning and induction heads"
    authors: ["Catherine Olsson", "Nelson Elhage", "Neel Nanda", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2209.11895"
  - title: "A sentimental education: Sentiment analysis using subjectivity summarization based on minimum cuts"
    authors: ["Bo Pang", "Lillian Lee"]
    year: 2004
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales"
    authors: ["Bo Pang", "Lillian Lee"]
    year: 2005
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Trainable transformer in transformer"
    authors: ["Abhishek Panigrahi", "Sadhika Malladi", "Mengzhou Xia", "Sanjeev Arora"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2307.01189"
  - title: "Do pretrained transformers really learn in-context by gradient descent?"
    authors: ["Lingfeng Shen", "Aayush Mishra", "Daniel Khashabi"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Recursive deep models for semantic compositionality over a sentiment treebank"
    authors: ["Richard Socher", "Alex Perelygin", "Jean Wu", "et al."]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "BranchyNet: Fast inference via early exiting from deep neural networks"
    authors: ["Surat Teerapittayanon", "Bradley McDanel", "H. T. Kung"]
    year: 2017
    venue: "ICPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Function vectors in large language models"
    authors: ["Eric Todd", "Millicent L. Li", "Arnab Sen Sharma", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Emergent abilities of large language models"
    authors: ["Jason Wei", "Yi Tay", "Rishi Bommasani", "et al."]
    year: 2022
    venue: "TMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "An explanation of in-context learning as implicit Bayesian inference"
    authors: ["Sang Michael Xie", "Aditi Raghunathan", "Percy Liang", "Tengyu Ma"]
    year: 2022
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Character-level convolutional networks for text classification"
    authors: ["Xiang Zhang", "Junbo Zhao", "Yann LeCun"]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
---

# In-context Learning and Gradient Descent Revisited

**Authors:** Gilad Deutch, Nadav Magar, Tomer Bar Natan, Guy Dar
**Published:** 2024-03 · [Source](https://arxiv.org/abs/2311.07772)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Deutch, Magar, Bar Natan and Dar revisit the popular Dai et al. (2023) claim that in-context learning (ICL) in real GPT-style transformers implicitly executes one step of gradient descent (GD) over the model's own weights — the "strong ICL-GD correspondence." Using the same six text-classification benchmarks (SST2, SST5, MR, Subj, AGNews, CB) and a 1.3B-parameter fairseq GPT, they show two evaluation defects in the original benchmark. First, the SimAOU_norm metric algebraically collapses to a constant for two random vectors of equal norm (worked example: any two added-noise vectors of norm 2‖z‖ yield SimAOU_norm = 1/4), so inflated similarity numbers can come from normalisation artifacts rather than real alignment; their unnormalised SimAOU and a delta version of the attention-map metric (SimAM∆, which compares update vectors instead of raw post-softmax maps) deflate scores significantly. Second — and most damaging — a completely untrained transformer reaches SimAOU and SimAM∆ scores at least as high as the trained model on all six datasets (e.g. SimAOU 0.07-0.18 untrained vs 0.04-0.17 trained), which means whatever the metric is measuring is not a learned mesa-optimisation. They then introduce Layer-Causal Gradient Descent (LCGD), a per-layer detached early-exit objective that respects the fact that an ICL update to layer ℓ can only depend on layers < ℓ; LCGD beats vanilla GD on SimAOU on every dataset (average 0.167 vs 0.102) and on SimAM∆ on 5/6 datasets (avg 0.336 vs 0.267), but the absolute numbers stay low (<0.4) and LCGD's own update vectors are themselves only ~0.1 cosine-similar to vanilla GD's. The most useful takeaway: the influential "ICL = GD on the model" mechanistic story does not survive a proper baseline; at best ICL implements a much weaker, layer-causal, possibly functional/kernel-regression-like update — a result memory-system designers should remember whenever they hear "the LLM is just doing implicit gradient descent on the context."

## Key Takeaway

The headline meta-optimisation story — "in-context learning is GD on the model" — survives only because the original benchmark forgot to compare to an untrained transformer. Once you add that one trivial baseline, an untrained model matches the trained model on the same alignment metrics, which logically rules out a learned ICL-as-GD mechanism. The story most experts already believe is built on a measurement artifact, not a real correspondence.

## Implications

- **Default to "weak correspondence" framing in any memory pipeline that leans on the ICL ≈ GD intuition** [ENGRAM-Encode, ENGRAM-Aggregate]: If your architecture treats in-context demonstrations as "free finetuning" of the substrate model, you are over-claiming. Treat ICL as steering through a shallow, layer-causal, possibly kernel-regression-like update — useful, but not a substitute for write-time consolidation into long-term memory.
- **Always add an untrained-substrate baseline to mechanistic claims about memory operations** [ENGRAM-Ground]: This paper's untrained transformer is the analog of running your retrieval/synthesis evaluation on a non-trained model or a shuffled index. If a metric stays high on that null condition, the metric is measuring geometry, not learning. Your provenance/trust layer should refuse to count such "wins."
- **Prefer Δ-style update metrics over normalised raw-vector metrics**: SimAOU_norm rewarded random noise of sufficient magnitude (worked out to a constant 1/4 of similarity for two equal-norm random additions). For any memory-retrieval or memory-synthesis evaluation that compares states pre- and post-update, compare the update vectors (deltas) rather than normalised raw vectors — the latter has free-energy from the shared prior state alone.
- **Layer causality is a useful design constraint for compiled/compacted memory** [ENGRAM-Aggregate, ENGRAM-Maintain]: LCGD wins on similarity because it respects the constraint that downstream representations cannot leak back into upstream ones. The analogue for memory: when compiling/compacting older memories, only let earlier (more abstract / longer-lived) summaries feed later (more specific / recent) ones — backward leakage during consolidation is what makes agents promote their own inferences to facts.
- **Don't conflate "shallow GD on a context-window function" with "GD on the model"** [ENGRAM-Encode]: The paper devotes a section to terminology drift — von Oswald-style "ICL = GD" works on linear / kernel toy functions, Dai-style works on the transformer itself. These are not the same claim. When you cite ICL-as-GD as evidence that "the model is updating itself", you are almost certainly citing the toy version and ignoring that the realistic version doesn't hold.
- **Use untrained-model checks as a routine probe in your own memory experiments** [ENGRAM-Ground]: The untrained-substrate trick generalises. For any "memory write at query time" architecture (RAG, scratchpad, function-vector injection), repeat the eval with the substrate's weights randomly initialised. The portion of your score that survives is geometric/inductive-bias artefact; the portion that disappears is the real learned effect.
- **Be cautious about agents that "self-finetune via prompt"** [ENGRAM-Maintain]: A growing class of agent designs argue that long context is equivalent to ongoing finetuning, so memory consolidation can be deferred indefinitely. This paper undermines that argument's mechanistic basis. Long context still ≠ persistent memory; consolidation is still an architectural choice you have to make explicitly, not something the substrate is silently doing on your behalf.
- **The published "ICL implements GD" finding is a candidate citation-failure case study** [ENGRAM-Ground]: If you maintain a memory of "what is known about ICL", flag the Dai et al. (2023) finding with a contradicting-evidence pointer to this paper. Contradictions of this size shouldn't be smoothed away by an aggregation step — they should be a first-class surfacing in the memory.

## How to Apply It (method)

**Scenario:** You are running an in-house memory-architecture research programme for an agent stack. One of your colleagues has just shipped a "context-as-finetuning" module that defers all write-time memory consolidation on the grounds that long-context ICL "is gradient descent anyway, so the model will internalise the demos for free." Before allowing the module to ship to customers, you want to falsify this assumption in your own setup — the same way Deutch et al. falsify Dai et al.'s strong correspondence.

**Steps:**

1. **Pin the benchmark**: Choose 3-5 tasks your agent actually does (e.g. ticket triage, customer-segment classification, RAG-answer scoring). For each, collect (a) a zero-shot prompt, (b) a k-shot ICL prompt with the same demonstrations the production agent would use, and (c) a true finetuned model on the same demonstrations. Fix the seed and the model.
2. **Capture per-layer attention output and attention map vectors** for the three conditions (ZSL / ICL / FT) at the last token of the test query. Save as numpy arrays per (layer, head, condition).
3. **Compute Δ-style similarity metrics rather than normalised raw metrics**. For each layer ℓ:

   ```
   SimAOU(ℓ)    = cosine( h_ICL(ℓ) - h_ZSL(ℓ),    h_FT(ℓ) - h_ZSL(ℓ) )
   SimAM∆(ℓ,h) = cosine( m_ICL(ℓ,h) - m_ZSL(ℓ,h), m_FT(ℓ,h) - m_ZSL(ℓ,h) )
   ```

   Average across layers (and heads, for SimAM∆). Avoid SimAOU_norm — the paper proves it collapses to 1/4 for two random equal-norm additions.
4. **Add an untrained-substrate baseline**: Re-initialise the same model architecture with random weights, keeping only positional + input embeddings if you want a "trained embeddings" variant. Repeat steps 2 and 3. If untrained scores match or exceed your trained scores, you have not measured a learned ICL ≈ FT alignment — you have measured representational geometry that any transformer of this shape exhibits.
5. **Add a random-noise control**: Compute the same SimAOU between two independent Gaussian-noise updates of the same norm as the FT update. This is the lower bound for "no real similarity" — your trained-model score must beat this by a meaningful margin or the metric is unusable.
6. **Stress-test with a layer-causal variant of finetuning**. Implement LCGD: for each layer, project its hidden state through the unembedding head, compute cross-entropy against the next token, take the gradient with respect to that layer's weights *with `.detach()` on its inputs* (`SG(·)` in the paper). This forbids gradient flow back through earlier layers and gives you the "best-case plausibly-implementable-by-ICL" GD upper bound. Re-run SimAOU and SimAM∆ against LCGD.
7. **Compute the GD-vs-LCGD α-correlation** (Appendix B): `α = cosine(m_LCGD − m_ZS, m_GD − m_ZS)` per layer. If α stays around 0.1-0.2 (as the paper found), even your "best-case ICL-implementable" GD is not the same direction as vanilla GD — meaning whatever ICL is doing, it is not a low-rank approximation of finetuning.
8. **Make the design decision**: If trained ≈ untrained on any metric, the "context-as-finetuning" module is not doing what it claims. Require the team to either (a) explicit write-time consolidation, or (b) a sharper claim about what shallow / layer-causal update ICL is actually approximating in your setup.

**Expected outcome:** A reproducible memo with per-layer plots showing (i) trained vs untrained substrate scores on SimAOU and SimAM∆, (ii) vanilla GD vs LCGD scores, (iii) α-correlation between the two, and (iv) a clear yes/no on whether the "context = finetuning" claim holds in your stack. If the pattern matches Deutch et al.'s — untrained matches trained, LCGD modestly beats GD, α stays low — you have falsified the strong correspondence in your own measurement setup and can require the team to add an explicit consolidation layer before shipping.

## Best Figure

![Figure 3 — Per-layer SimAOU and SimAM∆ comparison of vanilla GD vs. layer-causal GD (page 7)](figures/deutch-2024-icl-gd-revisited-fig.png)

**Image Candidates:**
- Figure 1 (p. 4): Architectural diagram of LCGD — shows the "stop gradient" early-exit projection at every layer that defines layer-causal finetuning.
- Table 2 (p. 5): Numerical head-to-head of GD vs LCGD across all six datasets on all four similarity variants — the headline quantitative result.
- Figure 3 (p. 7): Per-layer SimAOU (top) and SimAM∆ (bottom) bar plots showing where LCGD beats GD across the model — the only figure that reveals the non-uniform layer-by-layer story.

**Best Image:**
- **Figure Name:** Figure 3: Similarity computed per layer aggregated across tasks and seeds
- **Figure Page:** 7
- **Slide Caption:** Layer-causal GD's advantage over vanilla GD is not uniform across the 24-layer model — it dominates in early and late layers but loses in the middle stack.
- **Description:** Figure 3 plots SimAOU (top) and SimAM∆ (bottom) at every one of the model's 24 layers, comparing layer-causal GD (blue) against vanilla GD (orange) with error bars across seeds and tasks. SimAOU shows LCGD beating GD across virtually all layers — modestly in the early stack, dramatically in layers 16-20. SimAM∆ tells the opposite story: LCGD dominates in layers 3-11, then vanilla GD overtakes in layers 12-17, then both crash near zero past layer 20. This non-uniform pattern is what makes the figure load-bearing — it kills any simple "LCGD is just a better approximation of GD" story and forces a more nuanced reading: hidden-state updates (SimAOU) consistently respect layer causality, but attention-map updates (SimAM∆) only do so in the early-to-mid stack. For a memory architect, this is the diagnostic visual: it shows where in your stack the ICL-as-update story is plausible and where it isn't.

## What Experts Overlook

The detail most readers skip is the algebraic worked example in Section 3.1, where the authors *derive* that SimAOU_norm equals exactly 1/4 for two independent Gaussian-noise updates of norm 2‖z‖ added to a shared zero-shot state z. This isn't a stat-significance complaint — it's a closed-form proof that the metric in the original Dai et al. (2023) paper has a structural floor produced by the normalisation step itself: even pure noise produces a "similarity" of 0.25 when the norms align. Anyone who scans the paper for the empirical table will see "Deutch et al. complain that scores are biased" but miss that the bias is mathematically guaranteed by the formula, independent of any model, any task, any seed. The fix is mechanical: drop the normalisation and compare the unnormalised update vectors instead — which they call SimAOU and SimAM∆.

**Why it matters:** Most memory-system evaluations follow the same pattern — measure a "post-update" representation, normalise it (often to unit norm "so cosines are comparable"), then take the cosine against a reference. The Deutch derivation generalises: any time you normalise the *raw post-update* state instead of the *update direction*, you inherit free similarity from whatever the shared prior state contributed to the norm. This is structurally the same trap that ELO-rating systems hit when they normalise across cohorts, that benchmark leaderboards hit when they normalise per-sample scores instead of per-task, and that "fact-recall accuracy" metrics hit when they measure the post-write embedding rather than the write delta. The thing being measured silently picks up a constant offset that survives every comparison.

**Example of good use:** Suppose you're evaluating a memory-consolidation step that compacts a session's micro-memories into a single pattern-memory and you want to know whether the compacted memory retains the same retrieval geometry as the raw set. Compare the *update vectors* — `(compacted_query_embedding − base_query_embedding)` against `(raw_query_embedding − base_query_embedding)` — rather than normalising the post-update embeddings. You'll catch the case where compaction looks "highly similar" only because the base embedding dominates the norm.

**Example of misapplication:** A team builds an "agent-memory benchmark" that scores how similar an LLM's response with retrieved memory is to its response with the gold finetuned answer. They normalise both response embeddings to unit norm and cosine-compare. They publish strong scores. Six months later someone notices the same numbers come out with a random (untrained) base model — exactly the Deutch failure mode. The benchmark hasn't been measuring "did memory transfer the knowledge"; it has been measuring "do two long English responses share the dominant low-frequency direction in embedding space." Every paper that cited the benchmark now has a footnote-of-shame to add.

## Extracted Prompts

No applicable prompts found in this paper.

(This is a mechanistic-interpretability paper on transformer internals; the only "inputs" given to the model are raw text-classification examples from SST2 / SST5 / MR / Subj / AGNews / CB used as ICL demonstrations and test queries. No free-text prompts to elicit behaviour are documented.)

## Citations

- Brown et al. (2020). *Language models are few-shot learners.* (arXiv:2005.14165) — the canonical ICL emergence paper.
- Dai et al. (2023). *Why can GPT learn in-context? Language models implicitly perform gradient descent as meta-optimizers.* (arXiv:2212.10559) — the primary target of this paper's critique.
- von Oswald et al. (2023a). *Transformers learn in-context by gradient descent.* (ICML) — the canonical "ICL = GD on a shallow function" paper.
- von Oswald et al. (2023b). *Uncovering mesa-optimization algorithms in transformers.* — extends 2023a with mesa-optimisation framing.
- Akyürek et al. (2023). *What learning algorithm is in-context learning? Investigations with linear models.* — companion shallow-GD work.
- Ahn et al. (2023). *Transformers learn to implement preconditioned gradient descent for ICL.* — another shallow-GD result.
- Cheng et al. (2024). *Transformers implement functional gradient descent to learn non-linear functions in context.* — kernel-regression formulation Deutch et al. note is more compatible with LCGD.
- Shen, Mishra, Khashabi (2023). *Do pretrained transformers really learn in-context by gradient descent?* — earlier critique focused on demonstration-order sensitivity.
- Olsson et al. (2022). *In-context learning and induction heads.* (arXiv:2209.11895) — alternative mechanistic story for ICL.
- Hendel, Geva, Globerson (2023). *In-context learning creates task vectors.* — another alternative ("task vector") story.

(Full bibliography of 27 references in frontmatter `citations:` array.)

## Related Digests

- [[brown-2020-gpt3-few-shot]] — Language Models are Few-Shot Learners (the paper that established ICL as the phenomenon Deutch et al. are trying to mechanistically explain)
- [[vassilyev-2026-rcl]] — Reflective Context Learning: treats context-space adaptation as gradient descent over a context artifact (the optimistic flip-side of the same ICL ≈ GD intuition Deutch et al. critique; useful as the "if the strong correspondence held, this is the system you'd build" reference)
- [[hochreiter-1997-lstm]] — Long Short-Term Memory (the original "learn-to-learn-across-time-via-gates" architecture that pre-dates and motivates the modern in-context-learning-as-implicit-optimisation framing)

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim in the digest (untrained SimAOU 0.07-0.18 vs trained 0.04-0.17, average SimAOU GD 0.102 vs LCGD 0.167, average SimAM∆ GD 0.267 vs LCGD 0.336, α ≈ 0.1-0.2, the 1/4 closed-form for SimAOU_norm under equal-norm random additions, 5/6 datasets where LCGD beats GD on SimAM∆) is directly traceable to Tables 1 and 2 and Sections 3.1, 4, and Appendix B of the paper. The "LCGD wins on SimAOU across all six datasets and on 5/6 datasets for SimAM∆" claim matches Table 2 exactly (only AGNews favours vanilla GD on SimAM∆). The "ICL update to layer ℓ depends only on layers < ℓ" characterisation matches the paper's "Layer Causality" definition box in Section 4.1. The methodology translation (Steps 1-8 in *How to Apply It*) extends the paper's protocol to a memory-architecture setting, but the underlying technical operations (LCGD with `.detach()` on layer inputs, SimAOU/SimAM∆ as Δ-style cosine, untrained baseline) all come directly from the paper's Sections 3-4. The "kernel regression / functional GD" connection mentioned in the implications matches the Discussion section's reference to Cheng et al. (2024). No fabricated citations or invented metrics.
