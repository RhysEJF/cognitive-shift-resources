---
corpus: agentic-memory
kind: paper-digest
slug: child-2019-sparse-transformers
title: "Generating Long Sequences with Sparse Transformers"
authors:
  - "Child, Rewon"
  - "Gray, Scott"
  - "Radford, Alec"
  - "Sutskever, Ilya"
year: 2019
publication_date: "2019-04"
venue: "arXiv preprint (OpenAI)"
source_url: "https://arxiv.org/abs/1904.10509"
doi: null
arxiv_id: "1904.10509"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Replace O(n²) full self-attention with two-step factorized attention patterns (strided for periodic data, fixed for arbitrary text) that reduce compute to O(n·√n) per token, then combine with pre-activation residual blocks, attention-block recomputation, and fused block-sparse GPU kernels — and you can train 128-layer Transformers on 12K-token contexts, generate audio sequences of 65K samples (5 seconds at 12kHz), and in principle scale to 1M-token sequences, while *beating* dense attention quality on Enwik8/CIFAR-10/ImageNet-64 because the structural sparsity acts as a useful inductive bias."
topics:
  - sparse-attention
  - long-context
  - autoregressive-generation
  - transformer-architecture
  - factorized-attention
  - gradient-checkpointing
  - inductive-bias
  - working-memory-window
tags:
  - paper
  - foundational
  - sparse-transformer
  - long-context
  - openai
  - memory-architecture
entities:
  - child-rewon
  - gray-scott
  - radford-alec
  - sutskever-ilya
  - openai
related_digests:
  - brown-2020-gpt3-few-shot
  - dai-2019-transformer-xl
  - beltagy-2020-longformer
  - vaswani-2017-attention-is-all-you-need
  - liu-2023-lost-in-the-middle
  - shazeer-2017-moe
citations:
  - title: "Character-level language modeling with deeper self-attention"
    authors: ["Rami Al-Rfou", "Dokook Choe", "Noah Constant", "Mandy Guo", "Llion Jones"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1808.04444"
  - title: "Layer Normalization"
    authors: ["Jimmy Lei Ba", "Jamie Ryan Kiros", "Geoffrey E. Hinton"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1607.06450"
  - title: "Efficient attention using a fixed-size memory representation"
    authors: ["Denny Britz", "Melody Y. Guan", "Minh-Thang Luong"]
    year: 2017
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1707.00110"
  - title: "Training deep nets with sublinear memory cost"
    authors: ["Tianqi Chen", "Bing Xu", "Chiyuan Zhang", "Carlos Guestrin"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1604.06174"
  - title: "PixelSNAIL: An improved autoregressive generative model"
    authors: ["Xi Chen", "Nikhil Mishra", "Mostafa Rohaninejad", "Pieter Abbeel"]
    year: 2017
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1712.09763"
  - title: "Monotonic chunkwise attention"
    authors: ["Chung-Cheng Chiu", "Colin Raffel"]
    year: 2017
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1712.05382"
  - title: "Transformer-XL: Language modeling with longer-term dependency"
    authors: ["Zihang Dai", "Zhilin Yang", "Yiming Yang", "William W. Cohen", "Jaime Carbonell", "Quoc V. Le", "Ruslan Salakhutdinov"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "The challenge of realistic music generation: modelling raw audio at scale"
    authors: ["Sander Dieleman", "Aäron van den Oord", "Karen Simonyan"]
    year: 2018
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Convolutional sequence to sequence learning"
    authors: ["Jonas Gehring", "Michael Auli", "David Grangier", "Denis Yarats", "Yann N. Dauphin"]
    year: 2017
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "1705.03122"
  - title: "Memory-efficient backpropagation through time"
    authors: ["Audrūnas Gruslys", "Rémi Munos", "Ivo Danihelka", "Marc Lanctot", "Alex Graves"]
    year: 2016
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Identity mappings in deep residual networks"
    authors: ["Kaiming He", "Xiangyu Zhang", "Shaoqing Ren", "Jian Sun"]
    year: 2016
    venue: "ECCV"
    doi: null
    url: null
    arxiv_id: "1603.05027"
  - title: "Bridging nonlinearities and stochastic regularizers with Gaussian error linear units (GELU)"
    authors: ["Dan Hendrycks", "Kevin Gimpel"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1606.08415"
  - title: "An improved relative self-attention mechanism for Transformer with application to music generation"
    authors: ["Cheng-Zhi Anna Huang", "Ashish Vaswani", "Jakob Uszkoreit", "Noam Shazeer", "Curtis Hawthorne", "Andrew M. Dai", "Matthew D. Hoffman", "Douglas Eck"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1809.04281"
  - title: "Exploring the limits of language modeling"
    authors: ["Rafal Jozefowicz", "Oriol Vinyals", "Mike Schuster", "Noam Shazeer", "Yonghui Wu"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1602.02410"
  - title: "Glow: Generative flow with invertible 1x1 convolutions"
    authors: ["Diederik P. Kingma", "Prafulla Dhariwal"]
    year: 2018
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "A clockwork RNN"
    authors: ["Jan Koutnik", "Klaus Greff", "Faustino Gomez", "Jürgen Schmidhuber"]
    year: 2014
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1402.3511"
  - title: "Generating Wikipedia by summarizing long sequences"
    authors: ["Peter J. Liu", "Mohammad Saleh", "Etienne Pot", "Ben Goodrich", "Ryan Sepassi", "Lukasz Kaiser", "Noam Shazeer"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1801.10198"
  - title: "SampleRNN: An unconditional end-to-end neural audio generation model"
    authors: ["Soroush Mehri", "Kundan Kumar", "Ishaan Gulrajani", "Rithesh Kumar", "Shubham Jain", "Jose Sotelo", "Aaron Courville", "Yoshua Bengio"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1612.07837"
  - title: "Generating high fidelity images with subscale pixel networks and multidimensional upscaling"
    authors: ["Jacob Menick", "Nal Kalchbrenner"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1812.01608"
  - title: "Mixed precision training"
    authors: ["Paulius Micikevicius", "Sharan Narang", "Jonah Alben", "Gregory Diamos", "Erich Elsen", "David Garcia", "Boris Ginsburg", "Michael Houston", "Oleksii Kuchaev", "Ganesh Venkatesh", "et al."]
    year: 2017
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1710.03740"
  - title: "Pixel recurrent neural networks"
    authors: ["Aaron van den Oord", "Nal Kalchbrenner", "Koray Kavukcuoglu"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1601.06759"
  - title: "Image Transformer"
    authors: ["Niki Parmar", "Ashish Vaswani", "Jakob Uszkoreit", "Lukasz Kaiser", "Noam Shazeer", "Alexander Ku"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1802.05751"
  - title: "Improving language understanding by generative pre-training (GPT-1)"
    authors: ["Alec Radford", "Karthik Narasimhan", "Tim Salimans", "Ilya Sutskever"]
    year: 2018
    venue: "OpenAI Technical Report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Parallel multiscale autoregressive density estimation"
    authors: ["Scott Reed", "Aäron van den Oord", "Nal Kalchbrenner", "Sergio Gómez Colmenarejo", "Ziyu Wang", "Dan Belov", "Nando de Freitas"]
    year: 2017
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "1703.03664"
  - title: "PixelCNN++: Improving the PixelCNN with discretized logistic mixture likelihood and other modifications"
    authors: ["Tim Salimans", "Andrej Karpathy", "Xi Chen", "Diederik P. Kingma"]
    year: 2017
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1701.05517"
  - title: "End-to-end memory networks"
    authors: ["Sainbayar Sukhbaatar", "Jason Weston", "Rob Fergus", "et al."]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "WaveNet: A generative model for raw audio"
    authors: ["Aäron van den Oord", "Sander Dieleman", "Heiga Zen", "Karen Simonyan", "Oriol Vinyals", "Alex Graves", "Nal Kalchbrenner", "Andrew Senior", "Koray Kavukcuoglu"]
    year: 2016
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1609.03499"
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "Jakob Uszkoreit", "Llion Jones", "Aidan N. Gomez", "Łukasz Kaiser", "Illia Polosukhin"]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "Two 2d factorized attention schemes (strided + fixed) vs full attention"
  page: 3
  image_path: "figures/child-2019-sparse-transformers-fig.png"
---

# Generating Long Sequences with Sparse Transformers

**Authors:** Rewon Child, Scott Gray, Alec Radford, Ilya Sutskever (OpenAI)
**Published:** Apr 2019 · [Source](https://arxiv.org/abs/1904.10509)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

The Transformer's self-attention is O(n²) in sequence length — both memory and compute. To scale to long sequences (12K text tokens, 65K audio samples, in-principle 1M+), Child et al. factorize the attention pattern into two heads each touching only √n positions, giving O(n·√n) total cost. Two variants: **strided** (head 1 sees previous l tokens, head 2 sees every l-th token; l ≈ √n) — works for periodic data like images and music — and **fixed** (head 1 attends within a block, head 2 attends to specific "summarizer" cells inside each block) — works for non-periodic data like text. Combined with three engineering tricks: (1) pre-activation residual blocks + 1/√(2N) initialization for stable 128-layer training; (2) attention-and-FFN recomputation during backward pass to slash memory; (3) fused block-sparse GPU kernels with skipped upper-triangle. Result: SOTA on CIFAR-10 (2.80 bpd), Enwik8 (0.99 bpd matching Transformer-XL at half the params), ImageNet-64 (3.44 bpd), and 5-second classical music samples — *and* the sparse attention actually *beats* dense attention on the same data, suggesting structural sparsity is a useful inductive bias.

**ENGRAM dimensions: R (Retrieve — sparse attention IS a hand-designed retrieval over the context window), E (Encode — what enters working memory), M (Maintain — memory budget of long-sequence training).**

## Key Takeaway

Replace O(n²) full self-attention with two-step factorized attention patterns (strided for periodic data, fixed for arbitrary text) that reduce compute to O(n·√n) per token, then combine with pre-activation residual blocks, attention-block recomputation, and fused block-sparse GPU kernels — and you can train 128-layer Transformers on 12K-token contexts, generate audio sequences of 65K samples (5 seconds at 12kHz), and in principle scale to 1M-token sequences, while *beating* dense attention quality on Enwik8/CIFAR-10/ImageNet-64 because the structural sparsity acts as a useful inductive bias.

The deep insight for memory architecture: **attention patterns are themselves a memory schema.** Most of the literature treats attention as a black-box mechanism; this paper takes the qualitative observation that *learned* attention patterns in 128-layer Transformers are mostly sparse and structured (Figure 2 in paper) and *hard-codes* that structure into the architecture. The gains come from removing the cost of computing weights for entries the model would have learned to ignore anyway. **For agent memory: design the access pattern to match the actual workload, don't let the model burn compute attending to obviously-irrelevant context.**

## Implications

**For working-memory / context-window architecture (R + E dimensions):**

1. **The cost of attention is dominated by structurally irrelevant entries.** The qualitative analysis (Section 4.1, Figure 2 in paper) showed that even in a 128-layer dense Transformer trained on CIFAR-10, most attention patterns naturally became sparse — local convolution-like patterns in early layers, row+column factorization in mid layers, data-dependent sparsity in deep layers. **For agent memory:** if your retrieval doesn't have a strong shape (locality, recency, hierarchy), you're probably wasting compute on irrelevance the model would have learned to ignore anyway.

2. **Hand-designed sparsity beats learned sparsity at the same compute budget.** Table 2: Sparse (fixed) on Enwik8 hits 0.99 bpd vs dense's 1.00 bpd — *better* loss in *less than half* the time. This is counterintuitive: less computation, better quality. The explanation: structural sparsity acts as an inductive bias that prevents the optimizer from getting stuck on the wrong attention patterns. **For agent memory:** if you know your retrieval pattern (recency-heavy, entity-hop, document-graph), encode it explicitly — don't make the model learn it from scratch.

3. **The strided/fixed dichotomy is a profound design principle.** *Strided* (local + every-l-th) works for data with periodic structure: images (pixels in same column/row are related), music (beats), but **breaks on text** because text doesn't align with any fixed stride. *Fixed* (block + summarizer cells per block) works for text because the "summarizer" cells aggregate block-local information that's propagated globally — the architectural analog of "summary memory + chunked details." **For agent memory:** this is the architectural precursor of hierarchical memory systems (MemGPT page-level summaries, mem0 episodic+semantic split). The lesson: provide a *summary level* between full granularity and full reduction.

4. **Two-step access preserves full connectivity at √n cost.** The math (Section 4.2): for any j ≤ i, there's a 2-step path j → a → i where j is in A^{(1)}_a and a is in A^{(2)}_i. Total compute per token: |A^{(1)}| + |A^{(2)}| = 2√n. **For agent memory:** if you're doing 2-hop retrieval (find entity → find documents about entity), the same math applies — you can serve any query at sqrt-cost of the naive all-pairs version, provided the hop graph is well-designed.

**For long-context training (M dimension):**

5. **Attention recomputation during backward pass is essentially free quality.** Section 5.4: gradient checkpointing for attention is "particularly effective for self-attention layers when long sequences are processed, as memory usage is high for these layers relative to the cost of computing them." Trade FLOPs for memory at favorable ratios. **For agent training (if you ever fine-tune on long-context data): always recompute attention.**

6. **128+ layer training requires architectural care.** Section 5.2: pre-activation residual blocks (He 2016) + 1/√(2N) scaling of certain weight matrices. Without this, deep Transformers don't converge. **For agent systems training custom long-context models: depth requires its own engineering attention, separate from attention engineering.**

7. **Block-sparse GPU kernels are a non-trivial engineering moat.** Section 5.5: custom fused kernels that skip the upper triangle of the attention matrix entirely (autoregressive mask makes them zero anyway) and slice block-sparse patterns directly. This is half the speedup. **For practitioners:** modern alternatives include FlashAttention, xFormers, Triton kernels — but the architectural insight is the same: if you can express your sparse pattern as fixed-size blocks, you can exploit GPU memory hierarchy.

**For Flow-OS-style architectures:**

8. **Working-memory context windows have analogous patterns.** A Flow-OS agent reading from its vault is doing exactly the problem this paper solves: which subset of memory to attend to for the next decision. The strided/fixed distinction maps to:
   - **Strided**: useful for periodic structures (sessions in time order, daily logs)
   - **Fixed**: useful for arbitrary topical retrieval (entity-keyed lookup)
9. **65,536 audio samples at 5 seconds = the canonical "long episode" benchmark.** For agent memory, this corresponds to roughly the working-memory window of a multi-hour session. The architectural pattern (sparse cross-context links) is directly transferable.

## How to Apply It (method)

**Factorized attention recipe:**

1. **Decide which pattern fits your data:**
   - **Strided** (Section 4.3): two heads. Head 1 attends to previous `l` positions. Head 2 attends to every `l`-th position. Pick `l ≈ √n`. Works for periodic data.
   - **Fixed** (Section 4.3): two heads. Head 1 attends within a block of size `l` (positions where `floor(j/l) == floor(i/l)`). Head 2 attends to a set of "summarizer" positions within each block (the last `c` positions of each block, propagated to all subsequent blocks). Works for arbitrary structure including text. Typical `l ∈ {128, 256}`, `c ∈ {8, 16, 32}`.

2. **Choose head integration scheme:**
   - **Interleave**: one attention type per residual block (Equation 6). Cheapest.
   - **Merge**: single head attends to union of factorized patterns (Equation 7). Higher compute by constant factor.
   - **Multi-head**: n_h heads, each computing factorized attention in parallel (Equation 8). Most expressive.

3. **Architecture (Section 5.2):**
   - Pre-activation residual blocks (He 2016): `resblock(H) = a(H) + b(H)` where `a` is `dropout(attention(norm(H)))` and `b` is `dropout(ff(norm(H + a(H))))`.
   - Initialize W2 (in FFN) and Wp (post-attention) by 1/√(2N) where N = number of layers. Critical for stability beyond 100 layers.
   - LayerNorm + GELU activations. FFN hidden = 4d (or 2d for "half-size").

4. **Embeddings (Section 5.3):**
   - For images: data embeddings — one for row, column, channel.
   - For text/audio: attention embeddings — encode the row/column index in the factorization grid.

5. **Memory tricks (Section 5.4):**
   - Recompute attention weights and FFN activations during backward pass.
   - Don't apply dropout *within* attention block (incompatible with recomputation); only at end of residual addition.

6. **GPU kernels (Section 5.5):**
   - Fused softmax kernel using registers.
   - Skip upper-triangle of attention matrix (autoregressive mask makes it zero — halves operations and removes neg-bias term).
   - Block-sparse matrix multiplies for strided/fixed patterns.

7. **Mixed precision (Section 5.6):**
   - Weights in fp32, activations and gradients in fp16. Use dynamic loss scaling.
   - At sampling time, cast queries/keys back to fp32 (query-key product can overflow fp16).

**Hyperparameters that worked for them:**
- CIFAR-10 (3072 ctx): 128 layers, d=256, 2 heads, 120 epochs, lr 0.00035, dropout 0.25. Result: 2.80 bpd.
- Enwik8 (12,288 ctx): 30 layers, d=512, 8 heads, dropout 0.40, 80 epochs, stride 128, c=32, merged heads. Result: 0.99 bpd.
- ImageNet-64 (12,288 ctx): 48 layers, d=512, 16 heads, stride 128, dropout 0.01, 70 epochs / 7 days on 64 V100s. Result: 3.44 bpd.
- Classical music (65,536 ctx): 152M params, strided. Result: 1.97 bpd at 5-second samples.
- **Scaling rule (Section 7.4): 4× sequence length needs ~8× parameter reduction to fit in same memory** (the 4 × 4√4 = 8 factor).

**Translation to Flow-OS-style memory:**

| Sparse Transformer concept | Flow OS analog |
|---|---|
| Strided attention (local + periodic) | Read recent N sessions + every Nth older session for context |
| Fixed attention (block + summarizer) | Read all of current session + summary digest of each prior session |
| Block-sparse GPU kernels | Per-vault-section retrieval with cached embeddings |
| Pre-activation residual + 1/√(2N) init | (Not directly applicable — agent memory isn't deeply stacked) |
| Recompute attention during backward | (Training-only; agent inference recomputes anyway) |
| Custom data/attention embeddings | Structured frontmatter on every memory file (entities, topics, dates) |
| Halving compute by skipping upper triangle | Don't read memories from "the future" (timestamps > current session) |

## Best Figure

![Figure 3 — Two 2d factorized attention schemes (strided + fixed) vs full attention (page 3)](figures/child-2019-sparse-transformers-fig.png)

**Why this figure matters for the memory-architect lens:** It is the cleanest single image of *attention patterns as memory access shapes*. Panel (a) shows full Transformer attention — a dense triangular matrix where every output attends to every prior input. Panels (b) and (c) show the two sparse alternatives. The top row in each panel illustrates which positions two attention heads see when computing a specific output for a 6×6 image. The bottom row shows the connectivity matrix across all positions.

For ENGRAM, this figure is the canonical illustration of the **R (Retrieve) dimension as a designed schema rather than a learned one**. The full attention pattern (a) is "retrieve everything"; the strided pattern (b) is "retrieve recent + periodic"; the fixed pattern (c) is "retrieve local-block + designated summarizers." Each pattern is a hypothesis about the *shape* of the relevant context. The paper's empirical result — that hand-designed patterns *beat* learned dense attention on Enwik8 — is the strongest possible evidence that **shape-of-memory matters more than capacity-of-memory**.

The pattern in (c) — block + summarizer — is also the architectural ancestor of every "hierarchical memory" design that has emerged since: the summarizer cells are the analog of MemGPT page summaries, mem0 episodic/semantic split, and Flow OS's session-summary headers.

**Figure Page: 3**

## What Experts Overlook

1. **Sparse attention *beats* dense attention at equal compute — not just matches it.** Table 2 Enwik8: dense 1.00 bpd at 1.31 time/iter; sparse (fixed) 0.99 bpd at 0.55 time/iter. The sparse model is *both* faster *and* better. The standard intuition that "sparse approximates dense" is wrong — sometimes the structural prior is the right answer. **For agent memory: don't reflexively assume more context is better. Sometimes the constraint that prevents the model from looking at irrelevant context is itself useful.**

2. **Strided patterns *fail* on text.** Section 4.3: "for data without a periodic structure, like text, however, we find that the network can fail to properly route information with the strided pattern, as spatial coordinates for an element do not necessarily correlate with the positions where the element may be most relevant in the future." This is a strong negative result that is usually buried. **For agent memory: time-based retrieval (the strided analog) is insufficient for arbitrary text; you need entity-keyed or topic-keyed retrieval (the fixed analog).**

3. **The c=8/16/32 hyperparameter is doing real work.** Section 4.3: c=1 limits expressivity because many representations are used for only one block. c larger means more positions can act as "summarizers." This is a critical hyperparameter that defines how much information bandwidth flows between blocks. **For agent memory: the number of summarizer items per session/document matters disproportionately — too few and downstream context can't access the past; too many and you've reinvented full attention.**

4. **Reaching 1M+ context requires giving up almost everything else.** Section 7.4: 65,536 ctx → 152M params; 262,144 ctx → 25M params; 1,048,576 ctx → 3M params. To get 1M context, you have to drop to a tiny model. **The honest tradeoff: long context is bought with parameter capacity, not for free.** This is something modern long-context LM papers often elide. For agent memory: don't believe "infinite context" claims without checking what was sacrificed.

5. **The "two-step path" formalism (Section 4.2) generalises beyond p=2.** They only experiment with p=2 (two attention heads, √n cost) but explicitly note "the same techniques can be easily extended to higher dimensions." For p=3 you'd get n^{1/3} cost, etc. **For agent memory: the same factorization principle applies to multi-hop retrieval — entity → document → section as three sparse steps replace a single dense scan.**

6. **Custom embeddings encode the factorization structure.** Section 5.3: rather than just position embeddings, they add embeddings that encode *which row* and *which column* of the factorization grid the token belongs to. **For agent memory: structured frontmatter (entities, topics, dates) on every memory file is the analog — it tells the retriever how the memory item fits into the access pattern.**

7. **Quality degraded at 131,072 experts is also true at extreme context length.** Compare to [[shazeer-2017-moe]]: MoE quality dropped at 131K experts (too much sparsity); here, quality degrades at 1M context (model too small). **Both papers point to a fundamental principle: sparsity has an optimum, not a monotonic gain.** Past the optimum, signal-to-noise drops and quality declines.

## Extracted Prompts

This is an architecture paper, not a prompting paper — no system prompts. But three architectural patterns generalise:

1. **The factorization formalism (Section 4.2):**
   ```
   For p-step factorization with subsets A^{(1)}, A^{(2)}, ..., A^{(p)}:
   For any j ≤ i, there must exist a path (j, a, b, ..., i) of length p+1
   where j ∈ A^{(1)}_a, a ∈ A^{(2)}_b, etc.
   ```
   This is a general principle for any multi-hop retrieval: every source must be reachable from every query via a path of bounded length.

2. **The strided/fixed dichotomy as a design choice:**
   - Use **strided** when your data has periodic structure (timestamps, indices, fixed-format tables).
   - Use **fixed** when your data is arbitrary (free-form text, semantic content).

3. **Initialization for deep networks (Section 5.2):**
   ```
   Scale W2 and Wp by 1/√(2N), where N = number of layers
   ```
   Critical for training networks beyond ~50 layers. Doesn't apply directly to agent systems but underlies why modern long-context LMs can be so deep.

## Citations

28 citations. Highlights for the memory-architect lens:
- **Transformer foundations**: Vaswani 2017 ([[vaswani-2017-attention-is-all-you-need]]) — the dense attention this paper sparsifies.
- **Long-context contemporaries**: Dai 2018 (Transformer-XL, [[dai-2019-transformer-xl]]) — caching previous segment as memory; Al-Rfou 2018 (Deeper Self-Attention) — character-level LM that motivated their depth work; Liu 2018 (Generating Wikipedia by summarizing long sequences) — long-form generation precedent.
- **Memory-network ancestors**: Sukhbaatar 2015 (End-to-End Memory Networks, [[sukhbaatar-2015-end-to-end-memory-networks]]) — explicit memory access with multiple hops.
- **Multi-scale / hierarchical**: Koutnik 2014 (Clockwork RNN) — multi-rate temporal hierarchy; Mehri 2016 (SampleRNN) — hierarchical audio generation.
- **Block-sparse + memory infrastructure**: Chen 2016 (gradient checkpointing), Gruslys 2016 (memory-efficient BPTT), Micikevicius 2017 (mixed precision).
- **Image generation precedents**: Oord 2016 (Pixel RNN/CNN), Parmar 2018 (Image Transformer), Salimans 2017 (PixelCNN++), Reed 2017 (Parallel Multiscale), Menick & Kalchbrenner 2018 (SPN).
- **Audio generation precedents**: Van Den Oord 2016 (WaveNet), Dieleman 2018 (realistic music generation).

Full structured list in frontmatter `citations[]`.

## Related Digests

- [[brown-2020-gpt3-few-shot]] — GPT-3: uses sparse-Transformer-style architecture variants at 175B scale (sparse and dense layers interleaved)
- [[dai-2019-transformer-xl]] — Transformer-XL: contemporary alternative — caches previous segment as memory rather than factorizing attention
- [[beltagy-2020-longformer]] — Longformer: direct descendant — local + global attention pattern in same paper-style
- [[vaswani-2017-attention-is-all-you-need]] — the original dense Transformer this paper sparsifies
- [[liu-2023-lost-in-the-middle]] — Lost in the Middle: documents the failure mode (middle-context attention degradation) that this paper's structural sparsity might mitigate
- [[shazeer-2017-moe]] — MoE: parallel form of sparse activation (sparse over expert FFNs vs sparse over attention positions)

## Reviewer Notes

**Severity: Clean.**

Cross-checked against the paper text:
- O(n·√n) complexity claim: verified (Section 4.2 — they call it O(n·p√n) for general p, and use p=2).
- Strided formulation: A^{(1)}_i = {t, t+1, ..., i} where t = max(0, i-l); A^{(2)}_i = {j : (i-j) mod l = 0}. Verified.
- Fixed formulation: A^{(1)}_i = {j : floor(j/l) = floor(i/l)}; A^{(2)}_i = {j : j mod l ∈ {t, ..., l}} where t = l-c. Verified.
- Bits-per-byte results: CIFAR-10 2.80 (Sparse 59M strided), Enwik8 0.99 (Sparse 95M fixed), ImageNet-64 3.44 (Sparse 152M strided), classical music 1.97 (152M strided, 65K context). All verified Table 1.
- Table 2: Enwik8 Dense 1.00 / 1.31; Sparse Fixed 0.99 / 0.55; Sparse Strided 1.13 / 0.35. Verified.
- Table 4: 65K → 152M; 262K → 25M; 1M → 3M params. Verified.
- 1/√(2N) initialization scaling: verified Section 5.2.
- Recompute attention during backward: verified Section 5.4.
- GELU activation: f(X) = X · sigmoid(1.702 · X). Verified.
- Training: 8 V100 GPUs, Adam, 5000-iter linear warmup, gradient clip 1.0, weight decay 0.01, cosine LR decay. Verified Section 6.
- Stride 128, c=8/16/32 hyperparameters: verified Sections 4.3 and 7.2.

No fabrication detected. Author list (Child, Gray, Radford, Sutskever — all OpenAI) verified.
