---
corpus: agentic-memory
kind: paper-digest
slug: cunningham-2023-sparse-autoencoders-features
title: "Sparse Autoencoders Find Highly Interpretable Features in Language Models"
authors:
  - "Cunningham, Hoagy"
  - "Ewart, Aidan"
  - "Riggs, Logan"
  - "Huben, Robert"
  - "Sharkey, Lee"
year: 2023
publication_date: "2023-09"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2309.08600"
doi: null
arxiv_id: "2309.08600"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Train a sparse autoencoder on a transformer's residual-stream activations and the ℓ1-penalised hidden units recover an overcomplete dictionary of monosemantic features — features that score higher on GPT-4 autointerpretability than neurons, PCA, ICA or random directions, and that localise the IOI task in fewer patches and with smaller edit magnitude than PCA — establishing an unsupervised, task-agnostic method for pulling features out of superposition that the entire 2024-2026 mech-interp memory-circuit literature is built on."
topics:
  - mechanistic-interpretability
  - sparse-autoencoders
  - superposition
  - feature-dictionaries
  - activation-patching
  - memory-architecture
tags:
  - paper
  - mech-interp
  - sae
  - interpretability
  - unsupervised
  - foundational
entities:
  - cunningham-hoagy
  - ewart-aidan
  - riggs-logan
  - huben-robert
  - sharkey-lee
  - eleutherai
  - apollo-research
related_digests:
  - marks-2024-sparse-feature-circuits
  - mao-2026-agent-memory-circuits
  - brown-2020-gpt3-few-shot
citations:
  - title: "Pythia: A suite for analyzing large language models across training and scaling"
    authors: ["Stella Biderman", "Hailey Schoelkopf", "Quentin Gregory Anthony", "et al."]
    year: 2023
    venue: "International Conference on Machine Learning (ICML)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models can explain neurons in language models"
    authors: ["Steven Bills", "Nick Cammarata", "Dan Mossing", "et al."]
    year: 2023
    venue: "OpenAI technical report"
    doi: null
    url: "https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html"
    arxiv_id: null
  - title: "Curve circuits"
    authors: ["Nick Cammarata", "Gabriel Goh", "Shan Carter", "et al."]
    year: 2021
    venue: "Distill"
    doi: "10.23915/distill.00024.006"
    url: "https://distill.pub/2020/circuits/curve-circuits"
    arxiv_id: null
  - title: "Towards automated circuit discovery for mechanistic interpretability"
    authors: ["Arthur Conmy", "Augustine N Mavor-Parker", "Aengus Lynch", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2304.14997"
  - title: "Adaptively sparse transformers"
    authors: ["Gonçalo M Correia", "Vlad Niculae", "André FT Martins"]
    year: 2019
    venue: "EMNLP-IJCNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "LLM.int8(): 8-bit matrix multiplication for transformers at scale"
    authors: ["Tim Dettmers", "Mike Lewis", "Younes Belkada", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2208.07339"
  - title: "A mathematical framework for transformer circuits"
    authors: ["Nelson Elhage", "Neel Nanda", "Catherine Olsson", "et al."]
    year: 2021
    venue: "Transformer Circuits Thread"
    doi: null
    url: null
    arxiv_id: null
  - title: "Softmax linear units"
    authors: ["Nelson Elhage", "Tristan Hume", "Catherine Olsson", "et al."]
    year: 2022
    venue: "Transformer Circuits Thread"
    doi: null
    url: "https://transformer-circuits.pub/2022/solu/index.html"
    arxiv_id: null
  - title: "Toy models of superposition"
    authors: ["Nelson Elhage", "Tristan Hume", "Catherine Olsson", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2209.10652"
  - title: "Privileged bases in the transformer residual stream"
    authors: ["Nelson Elhage", "Robert Lasenby", "Chris Olah"]
    year: 2023
    venue: "Transformer Circuits Thread"
    doi: null
    url: "https://transformer-circuits.pub/2023/privileged-basis/index.html"
    arxiv_id: null
  - title: "The lottery ticket hypothesis: Finding sparse, trainable neural networks"
    authors: ["Jonathan Frankle", "Michael Carbin"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1803.03635"
  - title: "Cognitron: A self-organizing multilayered neural network"
    authors: ["Kunihiko Fukushima"]
    year: 1975
    venue: "Biological Cybernetics"
    doi: "10.1007/BF00342633"
    url: "https://doi.org/10.1007/BF00342633"
    arxiv_id: null
  - title: "The Pile: An 800gb dataset of diverse text for language modeling"
    authors: ["Leo Gao", "Stella Biderman", "Sid Black", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2101.00027"
  - title: "Accelerating convolutional neural networks via activation map compression"
    authors: ["Georgios Georgiadis"]
    year: 2019
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "An overview of catastrophic AI risks"
    authors: ["Dan Hendrycks", "Mantas Mazeika", "Thomas Woodside"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2306.12001"
  - title: "Elite backprop: Training sparse interpretable neurons"
    authors: ["Theodoros Kasioumis", "Joe Townsend", "Hiroya Inakoshi"]
    year: 2021
    venue: "NeSy"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient sparse coding algorithms"
    authors: ["Honglak Lee", "Alexis Battle", "Rajat Raina", "et al."]
    year: 2006
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Is sparse attention more interpretable?"
    authors: ["Clara Meister", "Stefan Lazov", "Isabelle Augenstein", "et al."]
    year: 2021
    venue: "ACL"
    doi: null
    url: "https://api.semanticscholar.org/CorpusID:235293798"
    arxiv_id: null
  - title: "The alignment problem from a deep learning perspective"
    authors: ["Richard Ngo", "Lawrence Chan", "Sören Mindermann"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2209.00626"
  - title: "Zoom in: An introduction to circuits"
    authors: ["Chris Olah", "Nick Cammarata", "Ludwig Schubert", "et al."]
    year: 2020
    venue: "Distill"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sparse coding with an overcomplete basis set: A strategy employed by V1?"
    authors: ["Bruno A Olshausen", "David J Field"]
    year: 1997
    venue: "Vision Research"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sparse coding of sensory inputs"
    authors: ["Bruno A Olshausen", "David J Field"]
    year: 2004
    venue: "Current Opinion in Neurobiology"
    doi: null
    url: null
    arxiv_id: null
  - title: "Analysis of the optimization landscapes for overcomplete representation learning"
    authors: ["Qing Qu", "Yuexiang Zhai", "Xiao Li", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1912.02427"
  - title: "Taking features out of superposition with sparse autoencoders"
    authors: ["Lee Sharkey", "Dan Braun", "Beren Millidge"]
    year: 2023
    venue: "AI Alignment Forum (interim research report)"
    doi: null
    url: "https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition"
    arxiv_id: null
  - title: "Investigating gender bias in language models using causal mediation analysis"
    authors: ["Jesse Vig", "Sebastian Gehrmann", "Yonatan Belinkov", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Interpretability in the wild: a circuit for indirect object identification in GPT-2 small"
    authors: ["Kevin Wang", "Alexandre Variengien", "Arthur Conmy", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2211.00593"
  - title: "High-dimensional data analysis with low-dimensional models: Principles, computation, and applications"
    authors: ["John Wright", "Yi Ma"]
    year: 2022
    venue: "Cambridge University Press"
    doi: null
    url: null
    arxiv_id: null
  - title: "Transformer visualization via dictionary learning: contextualized embedding as a linear superposition of transformer factors"
    authors: ["Zeyu Yun", "Yubei Chen", "Bruno A Olshausen", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2103.15949"
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "Number of features patched vs KL divergence from target (Left) and Mean edit magnitude vs KL divergence (Right) across residual-stream decompositions on IOI"
  page: 5
  image_path: "figures/cunningham-2023-sparse-autoencoders-features-fig.png"
---

# Sparse Autoencoders Find Highly Interpretable Features in Language Models

**Authors:** Hoagy Cunningham, Aidan Ewart, Logan Riggs, Robert Huben, Lee Sharkey (EleutherAI / MATS / Bristol AI Safety Centre / Apollo Research)
**Published:** 2023-09 (v3: 4 Oct 2023) · [Source](https://arxiv.org/abs/2309.08600)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Cunningham, Ewart, Riggs, Huben and Sharkey train a single-hidden-layer autoencoder (ReLU, tied weights, hidden dim `R · d_model` where R∈{0.5, 1, 2, 4, 8}) on the cached residual-stream activations of Pythia-70M (d=512) and Pythia-410M (d=1024) using the Pile, with the loss `||x − x̂||₂² + α||c||₁` — i.e. a vanilla reconstruction MSE plus an ℓ1 sparsity penalty on the hidden code. The learned hidden units form an overcomplete "feature dictionary" that beats neurons, random directions, PCA and ICA on GPT-4-judged autointerpretability scores (Figure 2: clear margin in early/mid layers, comparable to ICA by layer 4, minimal advantage in the final layer), recovers crisp monosemantic features (an apostrophe feature, a closing-parenthesis feature, a token-"the" feature, period and newline features — see Section 5.1 / Figure 4) and, on the Indirect Object Identification (IOI) task of Wang et al. 2022, requires fewer activation patches and smaller edit magnitudes than PCA to reach the same KL divergence from a counterfactual target (Figure 3, layer 11 of Pythia-410M, trained on ~7M activations from the first 10,000 elements of the Pile). The method runs in <1h on a single A40 GPU per dictionary, scales unsupervised, and explicitly fails to fully reconstruct activations (replacing layer-2 residual stream of Pythia-70M with its reconstruction increases Pile perplexity from 25 → 40) — i.e. you get an interpretable but lossy decomposition. The most useful takeaway: superposition can be undone post-hoc by a tiny ℓ1-regularised autoencoder, so feature-level mechanistic interpretability becomes a scalable engineering problem rather than a hand-crafted one.

## Key Takeaway

Polysemanticity (a single neuron firing for many unrelated concepts) is a symptom; superposition (the network packing more features than dimensions into an overcomplete basis of non-orthogonal directions) is the cause; and the cure is shockingly simple — train a sparse autoencoder on the layer's activations and read out its hidden units as the feature dictionary. This is the paper that turned "find the features" from a bespoke per-circuit cottage industry (Olah et al. 2020, Wang et al. 2022) into an unsupervised, scalable, task-agnostic procedure that runs in under an hour on a single GPU and produces features measurably more monosemantic than every prior baseline. Everything in the 2024-2026 mech-interp memory-circuit literature — Marks et al. 2024's sparse feature circuits, Anthropic's SAE-on-Claude work, Mao et al. 2026's agent-memory circuits — rests on this single result. **[ENGRAM: E (Encode), A (Aggregate)]** — the SAE is itself an LLM-on-the-write-path encoder for *the model's own activations*, distilling polysemantic raw signal into atomic monosemantic units; and it is an aggregation primitive, in that the dictionary features compose into causal circuits readable across layers.

## Implications

- **The SAE is the prototype of "structure-on-the-write-path" for model internals — apply the same logic to your memory store**: The paper's whole pitch is that raw activations are unusable as memory units because they're polysemantic; you have to *re-encode* them into atomic monosemantic features before downstream reasoning becomes tractable. The same logic applies to chat transcripts in a memory architecture — raw turns are polysemantic ("the user booked a paragliding trip and also signed Marcus Webb as a Flow customer"), and a structured extractor (LLM-on-write distilling into atomic memory units with one fact each) is the analogue of an SAE on the activation space. **[ENGRAM: E (Encode)]**

- **Choose your atomicity coefficient deliberately — there is no free lunch**: The α hyperparameter in `L = MSE + α||c||₁` is a smooth knob between "atomic & sparse" and "lossy & few-features-active". Section 6.2 admits non-zero reconstruction loss (perplexity 25 → 40 when layer-2 residual stream is replaced with its reconstruction in Pythia-70M). For a memory architect, this maps to: **how aggressively you canonicalise/atomise an inbound memory trades against how much of the original signal survives** — there is no setting that wins on both axes. **[ENGRAM: E×G (Encode × Ground)]** — atomisation destroys provenance fidelity by design.

- **Train on data that looks like inference-time data, not on task-specific data**: The SAE is trained on Pile activations (general webtext), not on IOI-task activations, yet it locates the IOI circuit *more precisely* than task-specific decompositions like PCA-on-this-task's-activations. This contradicts the intuitive "train your memory extractor on the kind of conversations you'll later index" instinct — a *general-purpose* extractor trained on a broad corpus may localise specific behaviours better than a narrowly-tuned one. **[ENGRAM: E×R (Encode × Retrieve)]**

- **Validate your atomisation with an interpretability score, not eyeballing**: The paper uses Bills et al. 2023's auto-interpretability protocol (Appendix A): GPT-4 writes a description from 5 top-activating fragments; GPT-3.5 simulates the feature's activations on held-out fragments; correlation between simulated and actual activations is the score. The exact analogue for a memory system: after your write-path extractor distils a turn into atoms, have GPT-4 describe each atom and GPT-3.5 predict which turns would activate it, then correlate. If you can't, your atomisation is polysemantic. **[ENGRAM: G (Ground)]** — provenance is testable via auto-interp.

- **Sparsity isn't a hyperparameter you tune once — there's a Pareto curve**: Figure 6 shows a smooth tradeoff (no "knee") between average number of active features and unexplained variance. The same will hold for memory: there is no single "right number of facts per turn" — it's a Pareto frontier between recall completeness and retrieval precision, and your operating point depends on what queries you'll serve. **[ENGRAM: A×R (Aggregate × Retrieve)]**

- **Beware dead atoms in the late layers**: SAE training on MLP layers and especially deeper layers produces many "dead features" — dictionary units that never fire on the corpus. By dictionary-size ratio R=2, more than half the units can be dead in MLP layers. Translation for memory: as you ratchet up your taxonomy granularity, some labelled buckets will receive zero memories. **You need a reaping pass.** The authors flag "reinitialising dead features" as future work; your memory system needs the equivalent (merge, drop, or repurpose unused categories). **[ENGRAM: M (Maintain)]**

- **The unit of retrieval (the dictionary feature) is not the same as the unit of computation (the activation)**: This is the deep architectural lesson — the residual stream itself is *not* the right shape for interpretation or retrieval; you have to project it into a different (overcomplete) basis to make it useful. The memory analogue: raw transcripts are the right shape for *replay*, but the *index* should live in a different shape (atomic memory units, entity-edge graph, schema-grounded records). Don't conflate the storage substrate with the retrieval substrate. **[ENGRAM: N (Network)]** — the shape of memory should differ from the shape of input.

- **Tied weights as a default; untie when reality forces you**: The encoder and decoder weights are tied for the residual-stream SAE (Footnote 2: "the directions which detect and define the feature should be the same") but Appendix C.3 shows MLP-layer SAEs work better with separate matrices `M_e` and `M_d`. For a memory system: your "read embedding" and "write embedding" of the same memory can be the same vector (tied) for generic content, but specialised content types (e.g., code, structured data, formal documents) may demand asymmetric read/write paths. **[ENGRAM: E×R (Encode × Retrieve)]**

## How to Apply It (method)

**Scenario:** You're a memory-architecture researcher running an ENGRAM-tagged experiment. You suspect your current write-path extractor is producing polysemantic memory atoms — single records that smear two or three unrelated facts together — and you want an unsupervised, scalable test that doesn't require hand-labelling thousands of memory atoms. You want to know which extractor configuration produces the most atomic, monosemantic memory units, and you want to verify causally that those atoms can be edited (e.g., to suppress a false memory or correct a biased inference) without touching the rest of the memory store.

**Steps:**

1. **Treat each memory atom's embedding as a "model activation".** Concatenate all your stored memory atom embeddings into a matrix `X ∈ ℝ^{N × d}` (N atoms, d embedding dim). This is your analogue of the paper's residual-stream activation cache. Cache 5–50M atoms worth of embeddings; if you have fewer, train fewer epochs.

2. **Train a sparse autoencoder on these embeddings.** Single hidden layer, hidden width `R · d` where R is your overcompleteness ratio (try R ∈ {0.5, 1, 2, 4, 8} as the paper does), ReLU activation, tied weights to start:

   ```
   c = ReLU(M·x + b)
   x̂ = Mᵀ·c
   L(x) = ||x − x̂||₂² + α·||c||₁
   ```

   Normalise rows of M (so the model can't game the sparsity loss by inflating feature magnitudes). Optimise with Adam at lr=1e-3 for 1–3 epochs. The paper reports <1h on a single A40 for residual-stream Pythia-70M (d=512).

3. **Sweep α** over roughly {1e-4, 3e-4, 1e-3, 3e-3}. Plot, for each α: number of active features (≥10 firings per 10M atoms) vs unexplained variance. You're looking for the operating point that maximises atomicity (low active count per atom) without losing too much information (low unexplained variance). Expect a smooth Pareto, not a knee (Figure 6).

4. **Score atomicity with auto-interp (Appendix A protocol).** For each learned dictionary feature (= candidate atomic memory schema):
   - Find the top-20 atoms (by feature activation) and pass 5 to GPT-4 with their per-token activations; ask GPT-4 for a one-line description of when the feature fires.
   - Have GPT-3.5 simulate the feature's activation on 5 different top-activating atoms + 5 random atoms; correlate predicted vs actual activations.
   - This correlation is your monosemanticity score for that atom-type. Apostrophe-feature-equivalent atoms in your store should score >0.5; polysemantic catch-alls will score near 0.

   Use this exact prompt skeleton (Bills et al. 2023):

   ```
   We're studying neurons in a neural network. Each neuron fires on certain
   tokens. Look at the following 5 text excerpts, with the activation strength
   of the neuron shown after each token in <brackets>. Write a single sentence
   description of what this neuron is detecting.

   [excerpt 1 with per-token activations]
   [excerpt 2 ...]
   ...

   Description:
   ```

5. **Validate causal localisation with activation patching.** Pick a behaviour you want to edit — e.g., "the system should not surface stale lead-status memories for entities labelled 'partner'". Run two memory queries: one on the base scenario, one on a counterfactual (where the entity is correctly labelled). Save the dictionary feature activations `c̄` from the counterfactual. Now run the base query but patch a small subset F of dictionary features to their counterfactual values:

   ```
   x'_i = x_i + Σ_{j ∈ F} (c̄_{i,j} − c_{i,j}) · f_j
   ```

   Measure KL divergence of the final output from the counterfactual target. Use the ACDC algorithm (Conmy et al. 2023) to greedily select F. **You should be able to fix the behaviour with far fewer patches than if you patched raw atom embeddings.** (Figure 3, Left: ~50–150 dictionary features beat the entire PCA decomposition at the same KL.)

6. **Compare against baselines.** Repeat steps 4–5 with: (a) the default embedding basis (with negatives zeroed for nonnegative-activation parity), (b) random unit directions, (c) PCA on `X`, (d) ICA on `X`. The paper finds sparse-coding wins in early/mid layers; ICA is the closest competitor (Section 3.2, Figure 2). If your SAE doesn't beat ICA in the early layers of your memory store, your atomisation is no better than a generic decorrelation.

7. **Hunt for dead atoms.** Count dictionary features that never activate above threshold across the corpus. If >50% are dead at R=2, your overcompleteness ratio is too aggressive for this layer/embedding family — drop R, or switch to untied weights (Equations 5–6 in Appendix C.3). This is your maintenance signal — Section 6.2 explicitly calls "reinitialise dead features" out as future work.

8. **Document where the method fails.** The paper is honest about three failure modes: (i) deep layers — interpretability scores converge with ICA by layer 4 of Pythia-70M; (ii) MLPs — many dead features even at α=0; (iii) attention heads — the paper hasn't solved them. For your memory system, the analogue is: SAE-style atomisation will work best on shallow, generic content; deep multi-hop inferences, structured data, and conversational meta-features may need different treatment.

**Expected outcome:** A learned dictionary of memory-atom schemas (1×R × your-embedding-dim units), each with an auto-interpretability score and a position on the Pareto curve of atomicity vs reconstruction. You can pick a target operating point for your write-path extractor (e.g., the α that gives 90% reconstruction at <30 active features per atom), and you can causally edit specific memories by patching their dictionary-feature representations — without touching unrelated memories. The artifact composes with the rest of an ENGRAM stack: the dictionary feeds N (the shape becomes "vector + sparse code"), gives you a testable monosemanticity metric for G (ground), and produces a maintenance signal (dead features) for M.

## Best Figure

![Figure 3 — Number of features patched vs KL divergence (Left) and Mean edit magnitude vs KL divergence (Right) on IOI, page 5](figures/cunningham-2023-sparse-autoencoders-features-fig.png)

**Image Candidates:**
- Figure 2 (p. 4): Bar chart comparing autointerpretability scores of SAE features vs neurons, random, PCA and ICA across residual-stream layers — the headline interpretability result.
- Figure 3 (p. 5): Two-panel plot showing IOI causal localisation — SAE features beat PCA and non-sparse dictionaries on both number-of-patches and edit-magnitude vs KL divergence. The clearest contrastive "story" figure.
- Figure 5 (p. 8): Causal circuit graph of the closing-parenthesis feature, showing how dictionary features in successive layers compose into a human-readable circuit — the qualitative "look, monosemantic units form circuits" result.

**Best:** Figure 3 wins because it's the paper's load-bearing causal claim. Figure 2 shows SAE features are more *interpretable*; Figure 3 shows they're more *useful* — i.e. that you can edit model behaviour through them more precisely than through any alternative decomposition. The Left panel proves it's the *count* that drops (fewer surgical edits for the same effect); the Right panel proves it's the *magnitude* that drops (the edits don't have to be huge). Both panels overlay four α settings of the dictionary against PCA and non-sparse (α=0) baselines, giving the visual "we sweep this hyperparameter and still win" story. For a memory-architect reader, this figure is the proof that atomisation isn't cosmetic — it's the basis for surgical, sparse causal interventions on the model (or, by analogy, on the memory store).

**Slide caption:** SAE features beat PCA, ICA and non-sparse dictionaries on the IOI causal-patching task — fewer patches and smaller edits to reach the same KL divergence from the counterfactual target (Pythia-410M, layer 11).

## What Experts Overlook

The detail most experts miss is **how the autoencoder treats negative activations**. The paper uses ReLU on the hidden code `c`, which means the dictionary features can only contribute *positively* to the reconstruction (Equation 3: `x̂ = Σ c_i f_i` with `c_i ≥ 0`). In contrast, every baseline they compare against — the default basis, random directions, PCA, ICA — is allowed to activate in *both directions* (a PCA component is "active on an entire half-space on one side of a hyperplane through the origin", Appendix G). To make the comparison fair on the residual-stream-basis and random-directions baselines, they manually replace negative activations with zeros. But more critically, **the SAE's bias term `b` is empirically always negative** (Appendix G), which means dictionary features activate on a strictly *less than full direction* — only the part of activation space on the far side of a hyperplane that doesn't even pass through the origin. This is what gives the SAE its sparsity advantage: each feature occupies a tiny "spike" in activation space rather than a half-space, so many features can coexist without interfering. The authors run an explicit control (Appendix G "Top-K Comparisons") where they restrict PCA/ICA to also have only K active directions per datapoint — the sparse-coding advantage *shrinks but does not disappear*, confirming the "spikes vs half-spaces" geometry is part of why it works.

**Why it matters:** The standard intuition for "why sparse codes are interpretable" is "they have fewer active components". But the SAE is doing two things at once: (a) restricting how many features fire (sparsity), and (b) restricting *where* a feature can fire (less-than-a-full-direction, via ReLU + negative bias). Strip out (b) — e.g., by using an autoencoder with linear or tanh activations — and you lose half the geometric story. This is also why naive replacements ("just train an SAE on my memory embeddings") may underperform: cosine-similarity-based memory retrieval is implicitly *half-space-based* (any vector positively correlated with the query is a hit), whereas the SAE features live on positive-only "spikes". If you adapt SAE atomisation to a memory store, you need to think about whether your downstream retrieval respects the same geometry.

**Example of good use:** A memory architect wants to extract atomic facts from chat transcripts without smearing two facts into one record. Instead of clustering transcript embeddings (which gives "this turn is roughly about topic X" — a half-space judgment), they train an SAE on the transcript embeddings with α tuned to give ~10 active features per turn. Each feature corresponds to a strictly-positive "spike" in embedding space — i.e. a narrowly-defined fact-type. They then route each turn through the SAE and store one memory atom per active feature. Result: per-turn memory atom count rises to ~10, but each atom is far more monosemantic and far easier to search for, edit, or invalidate.

**Example of misapplication:** A naive engineer reads "sparse autoencoders find interpretable features" and bolts a *linear* (no ReLU) autoencoder onto their memory embeddings, thinking "the ℓ1 penalty does the work". They get sparse codes that have both positive and negative components, run cosine-similarity retrieval, and find their "atomic" features are actually *bidirectional half-space indicators* — the "Marcus Webb is a Flow customer" feature also fires (with opposite sign) for "Marcus Webb is NOT a Flow customer" memories. Causal edits to one polarity unexpectedly affect the other. The system superficially looks like it's working — features are sparse, retrieval returns results — but the monosemanticity guarantee is gone, and they can't tell whether an edit will have side effects until they ship a bug.

## Extracted Prompts

The paper's load-bearing LLM prompt is the auto-interpretability protocol from Bills et al. 2023 (Appendix A). The Cunningham paper does not republish the full prompt verbatim, but it specifies the inputs and the operation exactly. The two prompts below are reconstructed from the protocol description (Appendix A, steps 2 and 3) — these are the *operational* prompts you'd need to reproduce the paper.

**Prompt explanation:** Step 2 — given 5 text fragments with per-token feature activations rescaled to integers 0–10, ask GPT-4 to write a one-line interpretation of when this dictionary feature fires.

```
We're studying neurons in a neural network. Each neuron looks for some particular thing in a short text excerpt.

Look at the parts of the excerpts where the neuron activates and summarize in a single sentence what the neuron is looking for. Don't list examples of words.

The activation format is token<tab>activation, with the activation strength rescaled to an integer between 0 and 10. A neuron firing strongly is represented by a high number, and a neuron not firing is represented by 0.

Excerpt 1:
<token>	<activation>
<token>	<activation>
...

Excerpt 2:
...

(5 excerpts total — the top-activating 5 of the top 20 fragments across 50,000 lines of OpenWebText, 64 tokens each.)

Description of what this neuron is looking for:
```

**Prompt explanation:** Step 3 — given the description, ask GPT-3.5 (used in place of GPT-4 because the simulation step requires logprobs, which OpenAI's public API exposes for GPT-3.5 but not GPT-4 at the time of the paper) to predict per-token activations on held-out text fragments (5 highly-activating + 5 random). The correlation between predicted and actual activations is the autointerpretability score.

```
Neuron <id>

Explanation of neuron <id> behavior: <description from Step 2>

Now, given the explanation, predict how the neuron will respond to each token of the following text. Output one integer between 0 and 10 per token, separated by tabs, on a single line per excerpt.

Excerpt 1:
<token1> <token2> <token3> ...

Predicted activations:
<int1>	<int2>	<int3>	...

(repeat for 10 excerpts: 5 top-activating, 5 random with non-zero variation)
```

(No other prompts appear in the body of the paper — all model-internal text generation is for autointerpretation. The paper does not contain persona prompts, evaluation rubric prompts, or any other free-form LLM instructions.)

## Citations

(28 references extracted — full list in frontmatter `citations:` array. Top 10 below.)

- Biderman et al. 2023 — **Pythia**: A suite for analyzing large language models across training and scaling (ICML). The model family the SAE is trained on (70M and 410M).
- Bills et al. 2023 — **Language models can explain neurons in language models** (OpenAI). The auto-interpretability protocol used to score features.
- Cammarata et al. 2021 — Curve circuits (Distill). Precursor mech-interp work.
- Conmy et al. 2023 — Towards **Automated Circuit Discovery** for Mechanistic Interpretability (arXiv:2304.14997). The ACDC algorithm used to select feature subsets F for IOI patching.
- Correia, Niculae & Martins 2019 — Adaptively sparse transformers (EMNLP). Baseline architectural sparsity approach contrasted with the post-hoc SAE.
- Elhage et al. 2021 — **A mathematical framework for transformer circuits** (Transformer Circuits Thread). Foundational mech-interp.
- Elhage et al. 2022a — Softmax linear units (Transformer Circuits Thread). Architectural attempt at interpretability.
- Elhage et al. 2022b — **Toy models of superposition** (arXiv:2209.10652). The theoretical basis for the whole paper.
- Elhage, Lasenby & Olah 2023 — Privileged bases in the transformer residual stream. Justifies why basis-aligned features aren't expected.
- Frankle & Carbin 2018 — Lottery ticket hypothesis (arXiv:1803.03635). Contrasted training-time sparsity approach.

Other key entries: Gao et al. 2020 (**The Pile** — training corpus), Olshausen & Field 1997 (**sparse coding original** — V1 visual cortex inspiration), Sharkey, Braun & Millidge 2023 (**direct predecessor** SAE-on-superposition work this paper builds on), Wang et al. 2022 (**IOI circuit** — the benchmark task), Yun et al. 2021 (**parallel dictionary-learning** work on transformer activations).

## Related Digests

- [[marks-2024-sparse-feature-circuits]] — Marks et al. 2024 (hop-1 of this walk): the direct extension of Cunningham — uses SAE features as nodes in a causal graph and demonstrates editable circuits (e.g., debiasing gender features in a profession classifier without disambiguating data).
- [[mao-2026-agent-memory-circuits]] — Mao et al. 2026 (hop-0 / seed of this walk): applies the Cunningham → Marks circuit-discovery pipeline to *agent memory*, treating long-term memory updates as activations the SAE can decompose.
- [[brown-2020-gpt3-few-shot]] — establishes the era of large transformers whose internals are opaque; Cunningham's SAE is one of the first scalable answers to "how do we understand what they're doing".

(QMD vsearch did not surface additional digests with score > 0.5 on the topic vocabulary used. As the wiki grows, expect Anthropic's "Towards Monosemanticity" and "Scaling Monosemanticity" papers to land here as natural neighbours.)

## Reviewer Notes

**Overall severity:** Clean

All claims in the digest are supported by the paper text:

- TLDR statistics — single-hidden-layer SAE, tied weights, ReLU, R∈{0.5,1,2,4,8}, α as ℓ1 coefficient, Pythia-70M (d=512) and Pythia-410M (d=1024), trained on Pile activations, <1h on A40, perplexity 25→40 on Pythia-70M layer 2: all directly from Section 2, Footnote 1, Appendix B, Section 6.2 (Limitations).
- IOI experiment details — Section 4, Figure 3 caption: "feature dictionaries were trained on the first 10,000 elements of the Pile (approximately 7 million activations) using the indicated α and R values, on layer 11 of Pythia-410M".
- Baseline comparisons (default basis, random, PCA, ICA) — Section 3.2.
- Monosemantic features listed (apostrophe, period, " the", newline; closing-parenthesis) — Section 5.1, Figures 4, 5, 14, 15.
- α–accuracy tradeoff smoothness, no knee — Section B, Figure 6.
- Dead features in MLPs and "more than half" claim — Appendix C.3, Appendix E.
- Untied weights for MLP (Equations 5–6) — Appendix C.3.
- Negative bias / "less than full direction" geometry — Footnote 5, Appendix G.

The ENGRAM tagging is the digester's own framework overlay (lens-driven), not a paper claim. The paragraph-form reconstructions of the Bills et al. 2023 auto-interp prompts are explicitly labelled as reconstructed from the protocol description (Appendix A doesn't reprint the full prompt verbatim) — flagging this in-line maintains provenance honesty.

No hallucinated metrics, no invented citations, no overextended claims.
