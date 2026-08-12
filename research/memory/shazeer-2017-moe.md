---
corpus: agentic-memory
kind: paper-digest
slug: shazeer-2017-moe
title: "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"
authors:
  - "Shazeer, Noam"
  - "Mirhoseini, Azalia"
  - "Maziarz, Krzysztof"
  - "Davis, Andy"
  - "Le, Quoc"
  - "Hinton, Geoffrey"
  - "Dean, Jeff"
year: 2017
publication_date: "2017-01"
venue: "ICLR 2017"
source_url: "https://arxiv.org/abs/1701.06538"
doi: null
arxiv_id: "1701.06538"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "By inserting a Sparsely-Gated Mixture-of-Experts layer — up to 131,072 expert FFNs, of which only 4 are activated per token by a learned noisy top-k gating network — between recurrent layers, you can build a 137-billion-parameter model whose per-example compute cost is unchanged from a 100-million-parameter baseline, achieving >1000× capacity-per-FLOP scaling and 39% perplexity drops on 100B-word datasets, provided you handle (a) the shrinking-batch problem via data+model parallelism, (b) load balancing via an importance-variance auxiliary loss, and (c) network bandwidth via wide-hidden experts."
topics:
  - mixture-of-experts
  - conditional-computation
  - sparse-activation
  - learned-routing
  - model-capacity
  - parametric-memory
  - load-balancing
  - distributed-training
tags:
  - paper
  - foundational
  - moe
  - sparse-models
  - memory-architecture
  - google-brain
entities:
  - shazeer-noam
  - mirhoseini-azalia
  - maziarz-krzysztof
  - davis-andy
  - le-quoc
  - hinton-geoffrey
  - dean-jeff
  - google-brain
related_digests:
  - brown-2020-gpt3-few-shot
  - guu-2020-realm
  - roberts-2020-pack-knowledge
  - kusupati-2022-matryoshka-representation-learning
  - vaswani-2017-attention-is-all-you-need
citations:
  - title: "TensorFlow: Large-scale machine learning on heterogeneous distributed systems"
    authors: ["Martín Abadi", "Ashish Agarwal", "et al."]
    year: 2016
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1603.04467"
  - title: "Expert gate: Lifelong learning with a network of experts"
    authors: ["Rahaf Aljundi", "Punarjay Chakravarty", "Tinne Tuytelaars"]
    year: 2016
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1611.06194"
  - title: "Dynamic capacity networks"
    authors: ["A. Almahairi", "N. Ballas", "T. Cooijmans", "Y. Zheng", "H. Larochelle", "A. Courville"]
    year: 2015
    venue: "ArXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep Speech 2: End-to-end speech recognition in English and Mandarin"
    authors: ["Dario Amodei", "Rishita Anubhai", "et al."]
    year: 2015
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1512.02595"
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["Dzmitry Bahdanau", "Kyunghyun Cho", "Yoshua Bengio"]
    year: 2014
    venue: "ICLR / arXiv"
    doi: null
    url: null
    arxiv_id: "1409.0473"
  - title: "Conditional computation in neural networks for faster models"
    authors: ["Emmanuel Bengio", "Pierre-Luc Bacon", "Joelle Pineau", "Doina Precup"]
    year: 2015
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1511.06297"
  - title: "Estimating or propagating gradients through stochastic neurons for conditional computation"
    authors: ["Yoshua Bengio", "Nicholas Léonard", "Aaron Courville"]
    year: 2013
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1308.3432"
  - title: "One billion word benchmark for measuring progress in statistical language modeling"
    authors: ["Ciprian Chelba", "Tomas Mikolov", "Mike Schuster", "Qi Ge", "Thorsten Brants", "Phillipp Koehn", "Tony Robinson"]
    year: 2013
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1312.3005"
  - title: "Exponentially increasing the capacity-to-computation ratio for conditional computation in deep learning"
    authors: ["Kyunghyun Cho", "Yoshua Bengio"]
    year: 2014
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "SVMixture: A mixture-of-experts approach using SVMs"
    authors: ["Ronan Collobert", "Yoshua Bengio", "Samy Bengio"]
    year: 2002
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Low-rank approximations for conditional feedforward computation in deep neural networks"
    authors: ["Andrew Davis", "Itamar Arel"]
    year: 2013
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "Distributed Gaussian processes"
    authors: ["Marc Peter Deisenroth", "Jun Wei Ng"]
    year: 2015
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning factored representations in a deep mixture of experts"
    authors: ["David Eigen", "Marc'Aurelio Ranzato", "Ilya Sutskever"]
    year: 2013
    venue: "ICLR Workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "Ensemble learning for multi-source neural machine translation"
    authors: ["Ekaterina Garmash", "Christof Monz"]
    year: 2016
    venue: "COLING"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to forget: Continual prediction with LSTM"
    authors: ["Felix A. Gers", "Jürgen Schmidhuber", "Fred Cummins"]
    year: 2000
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory-efficient backpropagation through time"
    authors: ["Audrūnas Gruslys", "Rémi Munos", "Ivo Danihelka", "Marc Lanctot", "Alex Graves"]
    year: 2016
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep neural networks for acoustic modeling in speech recognition: The shared views of four research groups"
    authors: ["Geoffrey Hinton", "Li Deng", "Dong Yu", "et al."]
    year: 2012
    venue: "IEEE Signal Processing Magazine"
    doi: null
    url: null
    arxiv_id: null
  - title: "Long short-term memory"
    authors: ["Sepp Hochreiter", "Jürgen Schmidhuber"]
    year: 1997
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adaptive mixtures of local experts"
    authors: ["Robert A. Jacobs", "Michael I. Jordan", "Steven J. Nowlan", "Geoffrey E. Hinton"]
    year: 1991
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Google's multilingual neural machine translation system: Enabling zero-shot translation"
    authors: ["Melvin Johnson", "Mike Schuster", "Quoc V. Le", "et al."]
    year: 2016
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Hierarchical mixtures of experts and the EM algorithm"
    authors: ["Michael I. Jordan", "Robert A. Jacobs"]
    year: 1994
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exploring the limits of language modeling"
    authors: ["Rafal Jozefowicz", "Oriol Vinyals", "Mike Schuster", "Noam Shazeer", "Yonghui Wu"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1602.02410"
  - title: "ImageNet classification with deep convolutional neural networks"
    authors: ["Alex Krizhevsky", "Ilya Sutskever", "Geoffrey E. Hinton"]
    year: 2012
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Building high-level features using large scale unsupervised learning"
    authors: ["Quoc V. Le", "Marc'Aurelio Ranzato", "Rajat Monga", "Matthieu Devin", "Kai Chen", "Greg S. Corrado", "Jeff Dean", "Andrew Y. Ng"]
    year: 2012
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep sequential neural network"
    authors: ["Ludovic Denoyer", "Patrick Gallinari"]
    year: 2014
    venue: "ICML / arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "Effective approaches to attention-based neural machine translation"
    authors: ["Minh-Thang Luong", "Hieu Pham", "Christopher D. Manning"]
    year: 2015
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Addressing the rare word problem in neural machine translation"
    authors: ["Minh-Thang Luong", "Ilya Sutskever", "Quoc V. Le", "Oriol Vinyals", "Wojciech Zaremba"]
    year: 2015
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Infinite mixtures of Gaussian process experts"
    authors: ["Carl E. Rasmussen", "Zoubin Ghahramani"]
    year: 2002
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Nonlinear models using Dirichlet process mixtures"
    authors: ["Babak Shahbaba", "Radford Neal"]
    year: 2009
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sequence to sequence learning with neural networks"
    authors: ["Ilya Sutskever", "Oriol Vinyals", "Quoc V. Le"]
    year: 2014
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generative image modeling using spatial LSTMs"
    authors: ["Lucas Theis", "Matthias Bethge"]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mixtures of Gaussian processes"
    authors: ["Volker Tresp"]
    year: 2001
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Google's neural machine translation system: Bridging the gap between human and machine translation (GNMT)"
    authors: ["Yonghui Wu", "Mike Schuster", "Zhifeng Chen", "et al."]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "Hierarchical mixture of classification experts for classification"
    authors: ["Bo Yao", "Dirk Walther", "Diane Beck", "Li Fei-Fei"]
    year: 2009
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep recurrent models with fast-forward connections for neural machine translation"
    authors: ["Jie Zhou", "Ying Cao", "Xuguang Wang", "Peng Li", "Wei Xu"]
    year: 2016
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "A Mixture of Experts (MoE) layer embedded within a recurrent language model"
  page: 2
  image_path: "figures/shazeer-2017-moe-fig.png"
---

# Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer

**Authors:** Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean (Google Brain / Jagiellonian University)
**Published:** Jan 2017 · [Source](https://arxiv.org/abs/1701.06538)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Insert a Mixture-of-Experts (MoE) layer — thousands of independent feed-forward sub-networks — between stacked LSTM layers. A learned "noisy top-k" gating network routes each token to just k experts (k=4 in most experiments). Compute scales with k, not n. Train 137-billion-parameter models on 100B-word corpora that activate only ~100M parameters per token, beating dense LSTMs at 6% of the compute. Three engineering hurdles cracked: (1) shrinking-batch problem solved via combined data+model parallelism (each expert sees `kbd/n` examples where d is device count); (2) load balancing via a soft `Limportance` auxiliary loss (square of coefficient-of-variation of per-expert gate sums) + a `Lload` term; (3) network bandwidth handled by making expert hidden layers wide so compute-to-IO ratio exceeds GPU's compute-to-bandwidth ratio. Results: 39% perplexity drop on 100B-word Google News with 68B-param MoE vs computationally-matched LSTM baseline; +1.34 BLEU on WMT'14 En→Fr with 8.7B-param MoE at lower training cost than GNMT's 278M-param baseline.

**ENGRAM dimensions: E (Encode — what gets routed where), R (Retrieve — gating acts as a learned routing/selection function), A (Aggregate — specialised experts as consolidated knowledge clusters).**

## Key Takeaway

By inserting a Sparsely-Gated Mixture-of-Experts layer — up to 131,072 expert FFNs, of which only 4 are activated per token by a learned noisy top-k gating network — between recurrent layers, you can build a 137-billion-parameter model whose per-example compute cost is unchanged from a 100-million-parameter baseline, achieving >1000× capacity-per-FLOP scaling and 39% perplexity drops on 100B-word datasets, provided you handle (a) the shrinking-batch problem via data+model parallelism, (b) load balancing via an importance-variance auxiliary loss, and (c) network bandwidth via wide-hidden experts.

The deep result for the memory-architect lens: **sparse routing is itself a form of conditional memory access**. The gating network decides *which* slice of parametric memory to read for *this* token. That's structurally a retrieval operation — just over weight matrices instead of text documents. The MoE paper proves the principle works at scale, and every retrieval-augmented architecture since (REALM, RAG, RETRO, the modern agent-memory systems) inherits the same selection-as-conditional-computation insight, even if they spell it differently.

## Implications

**For memory-architecture design (E + R dimensions):**

1. **Capacity ≠ compute, when access is sparse.** The paper's headline number is *1000× capacity at unchanged compute*. For agent memory, the analog is: your vault can grow indefinitely without per-query slowdown, as long as the retrieval step is sub-linear and the active set per query is bounded. This is the architectural justification for "memory grows forever, working context stays small."

2. **Learned routing > heuristic routing.** All prior MoE work used hard-coded or weakly-trained gates. The noisy top-k gating (Equations 3-5) is the first generally-effective approach. The principle for agent memory: **the *router* is a first-class trained component**, not a static heuristic. This is the same insight REALM later proved for document retrieval — and it generalises: any system that has to *select what to think about next* benefits from learning the selection function.

3. **Specialisation emerges from gating without supervision.** Appendix E Table 9 (not shown here but cited) shows that experts naturally specialise on syntactic/semantic clusters — one expert handles punctuation, another handles names, another handles articles, etc. **For agent memory:** if you let a routing model train freely against a downstream objective, it will discover and exploit natural clusters in your memory. No need to manually tag/categorise; the categories emerge from utility.

4. **Sparsity is the corruption-resistance property.** When 99.994% of the layer is inactive per token, a single corrupted/poisoned expert affects only ~0.006% of inferences. **For agent memory:** sparse retrieval gives natural fault isolation — a poisoned memory affects only queries that route to it, not the whole system.

**For load balancing and routing collapse (M dimension):**

5. **Gating networks collapse to a few favourites unless explicitly fought.** Section 4: "the gating network tends to converge to a state where it always produces large weights for the same few experts. This imbalance is self-reinforcing." The fix is an auxiliary loss `L_importance = w · CV(Importance(X))²` (square of coefficient of variation across experts). **For agent memory:** if you train a router on session signal, it will collapse to retrieving the same memories repeatedly unless you add a diversity/load-balance term. This is a hidden gotcha in any "learned retrieval" pipeline.

6. **Two losses needed, not one.** Even with `L_importance` balancing total gate-mass per expert, you still need `L_load` to balance *number of examples* per expert (one expert could get few high-weighted examples; another could get many low-weighted ones, both with equal importance but very different compute load). **The general principle: balanced *attention* ≠ balanced *examples*. Both need to be enforced.**

**For distributed/scaled systems (engineering):**

7. **The shrinking-batch problem is real and has a clean fix.** When k of n experts fire per token, each expert sees `kb/n` examples — collapses GPU efficiency. Solution: mix data + model parallelism. d devices, batch b per device, each expert sees `kbd/n`. **Implication for agent-system architecture:** if you shard a memory across multiple workers, each worker needs to see enough queries per second to make its compute cost amortisable. Pure functional decomposition (worker per expert) doesn't scale; you need pooled query batches.

8. **Network bandwidth, not compute, is the real bottleneck.** GPUs have ~1000:1 compute-to-bandwidth ratios. To stay efficient, your expert's `compute / IO size` must exceed that ratio. **For agent memory:** the cost of fetching a memory is dominated by transfer (network + serialisation), not by the LLM's "thinking" about it. Optimise for fewer, denser memory chunks rather than many small ones.

**For Flow-OS-style architectures:**
9. **This paper is the architectural ancestor of every "learned router" in the agent stack.** Whether it's a query router (which retriever?), a tool router (which MCP server?), or a memory router (which vault section?), the design principles trace back here: noisy top-k gating, importance-balance loss, sparse activation, learned specialisation.

## How to Apply It (method)

**MoE layer construction (n experts, top-k routing):**

1. **Experts:** n identical-architecture feed-forward networks E_1, ..., E_n (each ~1M params in the paper). They share input/output dimensionality but have independent parameters.

2. **Gating network (Noisy Top-K):**
   ```
   H(x)_i = (x · W_g)_i + StandardNormal() · Softplus((x · W_noise)_i)
   KeepTopK(H, k)_i = H_i if H_i in top-k else -∞
   G(x) = Softmax(KeepTopK(H(x), k))
   ```
   - W_g: gating weight matrix (input_dim × n)
   - W_noise: noise scaling matrix (input_dim × n)
   - Noise is critical for load balancing (Appendix A); without it, gating collapses.

3. **MoE output:**
   ```
   y = Σ_{i=1..n} G(x)_i · E_i(x)
   ```
   Sparse: skip computation for any E_i where G(x)_i = 0.

4. **Auxiliary losses:**
   - `Importance(X) = Σ_{x∈X} G(x)` — per-expert total gate mass over batch X.
   - `L_importance(X) = w_importance · CV(Importance(X))²` — penalise variance.
   - Also need `L_load` (Appendix A) to balance per-expert example counts.

5. **Two-level hierarchical MoE** for very large n: primary gating picks groups; secondary gating within group picks experts. Reduces gating compute from n to √n.

**Performance engineering:**

6. **Mixed data+model parallelism.** d devices each handling batch b. Standard layers (LSTM, gating) use data parallelism. Experts: one copy per device, each receiving combined `kbd/n`-sized batch from all data-parallel inputs.

7. **Convolutional trick.** For language modeling, apply MoE to all timesteps of a sequence in one batched call (multiplies batch size by sequence length).

8. **Wide expert hidden layers.** Hidden size determines compute-to-IO ratio. Use hidden_size > 1000 RELU units to exceed GPU's compute/bandwidth ratio.

**Reference results to expect:**
- 1B-word benchmark: MoE-4096 experts, ~8M ops/timestep — beats baseline LSTM (151M params, 151M ops/timestep) at 6% of compute.
- 100B-word benchmark: MoE-65536 experts (68B params total), 8M ops/timestep — 39% lower perplexity than computationally-matched baseline.
- WMT'14 En→Fr: MoE-2048 (8.7B params, 85M ops/timestep) — 40.56 BLEU vs GNMT's 39.22 BLEU at faster training time.

**Translation to Flow-OS-style memory:**

| MoE concept | Flow OS analog |
|---|---|
| 131K expert FFNs, 4 active per token | 50K markdown memory files, top-4 retrieved per query |
| Noisy top-k gating | QMD hybrid scoring + random tiebreak |
| L_importance loss | Diversity-aware reranker (penalise reusing same memories) |
| L_load loss | Per-memory-file query counter to detect hot spots |
| Hierarchical 2-level MoE | Coarse-to-fine retrieval: route to vault section, then to file |
| Mixed data+model parallelism | Per-vault-section worker pool |
| Wide expert hidden layers | Denser memory chunks (larger paragraphs, not sentences) |
| Convolutional batching | Batch multiple agent queries through retriever simultaneously |

## Best Figure

![Figure 1 — A Mixture of Experts (MoE) layer embedded within a recurrent language model (page 2)](figures/shazeer-2017-moe-fig.png)

**Why this figure matters for the memory-architect lens:** The left panel shows the MoE layer slotted into a recurrent network like any other layer — interchangeable with a standard FFN. The right panel zooms into the MoE layer: a *Gating Network* takes input x, produces sparse weights G(x)_2 and G(x)_{n-1} (note: only two experts are non-zero — Expert 2 and Expert n-1), routes the input to *only* those experts, multiplies the outputs by their gate weights, and sums to produce y.

For ENGRAM, this is the canonical picture of **conditional access to parametric memory**. Each expert is a chunk of memorised knowledge. The gating network is the retriever. The top-k selection is the rerank-and-cut step. The sum is the aggregation. *This is RAG implemented as differentiable weight matrices instead of differentiable document embeddings.* The fact that the same architecture diagram fits both interpretations is exactly why MoE → DPR → REALM → modern agent memory is one continuous lineage.

**Figure Page: 2**

## What Experts Overlook

1. **The 131,072-expert experiment *degraded* performance.** Section 5.2: scaling from 65,536 experts (68B params) to 131,072 (137B params) on the 100B-word corpus made perplexity *worse*. They speculate "too much sparsity." **The lesson everyone misses: there's an optimal sparsity ratio relative to dataset size, not a "more is always better" curve.** For agent memory: more memories isn't always better — past a certain point, retrieval signal degrades because the router can't distinguish them.

2. **Noise in the gating is load-balancing infrastructure, not just regularisation.** The `Softplus((x · W_noise)_i)` term in Eq. 4 is essential — without per-component learned noise, the gating collapses (Appendix A). **For agent memory:** any learned retrieval system needs *exploration* — pure greedy top-k will collapse onto a small set of memories. The fix is either explicit noise (epsilon-greedy retrieval) or a UCB-style bonus for under-explored items.

3. **The hierarchical MoE (Appendix B) is the unsung scaling hero.** A flat n-expert MoE has gating compute O(n). A two-level hierarchical MoE has O(√n). For n=131,072 that's 363 vs 131,072 — a 360× reduction. **For agent memory:** if your vault has >10K items, do not retrieve over all of them with a single embedding lookup. Cluster first, retrieve within cluster.

4. **Expert specialisation is data-driven, not designed.** Appendix E Table 9 shows experts spontaneously specialising into things like "research topics", "ID-like sequences", "punctuation", "phrasal verbs". **No supervision on this — the routing just discovered the natural clusters.** This is profound for agent memory: *don't impose a taxonomy*. Let the router learn what categorical structure the data has. The taxonomy you'd design by hand will be wrong; the one emerging from gradient is right.

5. **Network bandwidth, not compute, is the actual binding constraint at scale.** Section 3.2: "computational power thousands of times greater than the aggregate inter-device network bandwidth." For agent systems, this maps to: serialisation/deserialisation costs of memory items dominate over LLM inference cost for short queries. **Optimisation target: pack more information per memory item, not more memory items.** Compress related memories together rather than splitting them apart.

6. **The "shrinking batch problem" generalises to any sparse system.** Whenever you have N producers and K consumers per producer, each consumer sees `K/N` of the load — which kills batch-efficiency. **For agent memory:** if each query touches 5 of 50,000 memories, each memory file gets 0.01% of query load. Without batching across queries, individual-file compute is wildly inefficient. The MoE paper's `kbd/n` math is the template for thinking about this.

7. **"Lifelong learning with a network of experts" (Aljundi 2016) cited but not discussed.** This is a precursor to *adding experts over time* — sequential expert addition. **For agent memory:** the analog is *growing the vault*. The literature on how to add experts without disrupting prior ones is directly relevant to how to add memories without disrupting existing retrieval patterns. Worth following the Aljundi thread separately.

## Extracted Prompts

This is a pre-LLM-prompting paper — no system prompts per se. But three *patterns* generalise:

1. **The gating function (Eq. 3) as a "tool router" template:**
   ```
   G(x) = Softmax(KeepTopK(linear(x) + noise(x), k))
   ```
   Any agent that has to pick K tools from N available tools at each step can use this exact form. The noisy top-k is the proven recipe.

2. **The auxiliary load-balance loss as a "diversity penalty" template:**
   ```
   L_importance = w · CV(per_item_selection_count)²
   ```
   Any retrieval pipeline that wants to avoid collapse onto a few favourite items can add this loss (or its inference-time equivalent: rerank with diversity bonus).

3. **Importance vs Load distinction (Section 4):**
   - *Importance*: sum of weights given to each item.
   - *Load*: number of times each item is touched.
   Both need to be balanced — they're different. This is the implicit framing of "how many times was this memory cited" vs "how strongly was it cited each time" — both matter, neither is sufficient.

## Citations

35 citations. Highlights for the memory-architect lens:
- **MoE lineage**: Jacobs 1991 (the original adaptive mixtures of experts), Jordan & Jacobs 1994 (hierarchical MoE + EM), Eigen 2013 (deep MoE — directly extends Eigen's idea).
- **Conditional computation precursors**: Bengio 2013 (gradient estimation through stochastic neurons), Bengio 2015 (boolean gates + REINFORCE), Davis & Arel 2013, Almahairi 2015, Cho & Bengio 2014.
- **Lifelong-learning analog**: Aljundi 2016 (Expert Gate — sequentially added experts).
- **LSTM/RNN backbone**: Hochreiter & Schmidhuber 1997 (LSTM), Sutskever 2014 (seq2seq), Bahdanau 2014 (attention NMT).
- **Strong baseline being beaten**: Jozefowicz 2016 (LSTM LM SOTA on 1B word), Wu 2016 (GNMT).
- **Distributed training infrastructure**: Abadi 2016 (TensorFlow), Gruslys 2016 (memory-efficient BPTT).

Full structured list in frontmatter `citations[]`.

## Related Digests

- [[brown-2020-gpt3-few-shot]] — GPT-3: dense scaling thesis (no MoE) — the architectural alternative
- [[guu-2020-realm]] — REALM: retrieval-augmented LM where retrieval-as-routing has the same gradient structure as MoE gating
- [[roberts-2020-pack-knowledge]] — How Much Knowledge: 11B-param T5 baselines that MoE could in principle out-scale
- [[kusupati-2022-matryoshka-representation-learning]] — Matryoshka: another form of sparse/multiscale representation
- [[vaswani-2017-attention-is-all-you-need]] — Attention is all you need: same year, same lab branch, dense self-attention as the other approach to "select what to attend to"

## Reviewer Notes

**Severity: Clean.**

Cross-checked against the paper text:
- "137 billion parameters" in MoE layer — verified (Section 5.2, 131,072 experts).
- "1000× improvements in model capacity" — verified verbatim from abstract.
- "4 experts active per input" for the LM experiments — verified (Section 5.1).
- "39% lower perplexity at 65,536 experts (68B parameters)" on 100B-word corpus — verified (Section 5.2). Also verified that 131,072 experts *degraded* performance.
- Table 1 results: Best Published 34.7/30.6 perplexity at 151M params; Low-Budget MoE 34.1 perplexity at 4303M params, 8.9M ops/timestep, 15 hours/16 K40s. All correct.
- WMT'14 En→Fr: MoE-2048 8.7B params, 40.56 BLEU after longer training, vs GNMT 39.22. Verified.
- Multilingual MoE: 19% lower dev perplexity than GNMT-Multi. Verified.
- Gating equations 3-5: verified verbatim.
- L_importance loss: `w * CV(Importance(X))²` verified.
- "99.994% layer sparsity at 65,536 experts" — verified (4 active out of 65,536 = 99.994% sparsity).
- Architecture: 2 stacked LSTMs with MoE between (Figure 1) — verified.
- Hierarchical MoE gating complexity O(√n) — implied by 2-level structure described in Appendix B; the paper doesn't say "O(√n)" explicitly but this is correct math for balanced two-level routing.

No fabrication detected. Author list (7 — Shazeer, Mirhoseini, Maziarz, Davis, Le, Hinton, Dean) verified. Maziarz is the Jagiellonian University intern; others Google Brain.
