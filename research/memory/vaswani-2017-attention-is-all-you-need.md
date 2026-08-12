---
corpus: agentic-memory
kind: paper-digest
slug: vaswani-2017-attention-is-all-you-need
title: "Attention Is All You Need"
authors:
  - "Vaswani, Ashish"
  - "Shazeer, Noam"
  - "Parmar, Niki"
  - "Uszkoreit, Jakob"
  - "Jones, Llion"
  - "Gomez, Aidan N."
  - "Kaiser, Lukasz"
  - "Polosukhin, Illia"
year: 2017
publication_date: "2017-12"
venue: "NeurIPS"
source_url: "https://arxiv.org/abs/1706.03762"
doi: null
arxiv_id: "1706.03762"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Recurrence and convolution were both load-bearing assumptions, not necessary ingredients — replace them with self-attention and the model becomes massively more parallelisable, trains faster (12 hours on 8 GPUs to beat the best ensembles), and gives you a uniform substrate where every token is one constant-time hop from every other token in the same layer; this is the architecture every modern memory/retrieval system inherits."
topics:
  - transformer
  - self-attention
  - multi-head-attention
  - encoder-decoder
  - positional-encoding
  - parallelisable-training
  - layer-norm
  - sequence-modelling-foundation
  - network
  - retrieve
tags:
  - paper
  - canonical
  - foundational
  - transformer
  - attention
  - architecture
  - engram-network
entities:
  - vaswani-ashish
  - shazeer-noam
  - parmar-niki
  - uszkoreit-jakob
  - jones-llion
  - gomez-aidan
  - kaiser-lukasz
  - polosukhin-illia
  - google-brain
  - google-research
related_digests:
  - devlin-2018-bert
  - brown-2020-gpt3-few-shot
  - beltagy-2020-longformer
  - dai-2019-transformer-xl
  - radford-2018-gpt1
citations:
  - title: "Long short-term memory"
    authors: ["Sepp Hochreiter", "Jürgen Schmidhuber"]
    year: 1997
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["Dzmitry Bahdanau", "Kyunghyun Cho", "Yoshua Bengio"]
    year: 2014
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1409.0473"
  - title: "Sequence to sequence learning with neural networks"
    authors: ["Ilya Sutskever", "Oriol Vinyals", "Quoc V. Le"]
    year: 2014
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "1409.3215"
  - title: "Layer normalization"
    authors: ["Jimmy Lei Ba", "Jamie Ryan Kiros", "Geoffrey E. Hinton"]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1607.06450"
  - title: "Deep residual learning for image recognition"
    authors: ["Kaiming He", "Xiangyu Zhang", "Shaoqing Ren", "et al."]
    year: 2016
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: "1512.03385"
  - title: "Adam: A method for stochastic optimization"
    authors: ["Diederik P. Kingma", "Jimmy Ba"]
    year: 2015
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1412.6980"
  - title: "Convolutional sequence to sequence learning"
    authors: ["Jonas Gehring", "Michael Auli", "David Grangier", "et al."]
    year: 2017
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "1705.03122"
  - title: "Neural GPUs learn algorithms"
    authors: ["Lukasz Kaiser", "Ilya Sutskever"]
    year: 2015
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1511.08228"
  - title: "Massive exploration of neural machine translation architectures"
    authors: ["Denny Britz", "Anna Goldie", "Minh-Thang Luong", "et al."]
    year: 2017
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "1703.03906"
  - title: "Effective approaches to attention-based neural machine translation"
    authors: ["Minh-Thang Luong", "Hieu Pham", "Christopher D. Manning"]
    year: 2015
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "1508.04025"
  - title: "Long short-term memory-networks for machine reading"
    authors: ["Jianpeng Cheng", "Li Dong", "Mirella Lapata"]
    year: 2016
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "1601.06733"
  - title: "Dropout: A simple way to prevent neural networks from overfitting"
    authors: ["Nitish Srivastava", "Geoffrey Hinton", "Alex Krizhevsky", "et al."]
    year: 2014
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "The Transformer model architecture"
  page: 3
  image_path: null
---

# Attention Is All You Need

**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
**Published:** 2017-12 · [Source](https://arxiv.org/abs/1706.03762)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Vaswani et al. propose the Transformer — an encoder-decoder built entirely from scaled dot-product attention, multi-head attention (8 heads in the base config), point-wise feed-forward layers (d_ff = 2048), residual connections, layer normalisation, and sinusoidal positional encodings — and abandon recurrence and convolution entirely. On WMT 2014 English-to-German they reach 28.4 BLEU (then state-of-the-art, beating the best ensembles by >2 BLEU) in 12 hours on 8 P100 GPUs; on WMT 2014 English-to-French they reach 41.8 BLEU in 3.5 days on the same hardware — orders of magnitude less training compute than the RNN/CNN systems they beat. Attention scales as O(n²·d) per layer but is fully parallel within a layer (constant maximum path length between any two positions), whereas RNNs are O(n·d²) but sequential. The architecture is the substrate every modern LLM (GPT, BERT, T5, PaLM, Llama, Claude) and every modern dense retriever, reranker, and memory encoder is built on.

## Key Takeaway

The thing the whole field thought was the problem (modelling long-range dependencies in sequences) was a side effect of the actual problem (training-time parallelism). Killing the recurrence kills the gradient bottleneck, and once every position can talk to every other position in a single matmul, "long-range dependency" becomes a property you tune (with positional encoding and attention masking) rather than a property you fight (with LSTM gates and gradient clipping).

## Implications

- **The attention block is your default memory primitive**: Every modern memory system — vector retrieval, attention-over-KV-cache, attention-over-summary-bank — is structurally an attention block. Understand multi-head + scaled dot-product first; everything else is variations. **(N, R)**
- **Position is a feature, not a constraint**: Self-attention is permutation-equivariant by default; the positional encoding is what gives it order. For memory systems this means you can deliberately ORDER your retrieved chunks (cf. Lost in the Middle) — the model has no innate "this came first" prior beyond the positions you encode. **(R)**
- **O(n²) is the cost of universality**: The price of every-token-to-every-token attention is quadratic memory. Sparse, sliding-window, and retrieval-augmented variants exist because of this constraint — choose your variant based on whether your task actually needs n²-many interactions. **(N)**
- **Multi-head ≠ ensemble; it's specialised attention**: 8 heads with d_k = 64 each beats 1 head with d_k = 512. Different heads learn different relations (syntax, coreference, etc.). For memory retrieval, multi-head means a single query can probe along multiple semantic dimensions in one shot. **(R)**
- **Layer norm + residual is the recipe for deep stacks**: 6 layers in the original paper; modern LLMs use 80+. The Add-Norm pattern is what makes very-deep transformers trainable. Memory-system designers building learned components should default to this pattern rather than reinventing. **(N)**
- **The encoder-decoder split is optional**: BERT keeps only the encoder; GPT keeps only the decoder; T5 keeps both. The "right" choice depends on whether you need an embedding (encoder-only) or a generator (decoder-only) or both — memory systems use all three flavours. **(E, N)**
- **Training-time parallelism is the actual moat**: The reason the field switched isn't BLEU; it's that you can saturate a GPU at training time. Memory-pipeline components you train should preserve this — batch everything, avoid per-example state. **(M)**

## How to Apply It (method)

**Scenario:** A memory-architect team needs to build a domain-specific dense encoder for chunk retrieval over an internal corpus. They want to understand the attention machinery well enough to (a) choose a backbone, (b) decide whether to use cross-attention reranking, and (c) reason about cost.

**Steps:**

1. **Choose backbone size based on the (n, d_model) cost curve**: For a typical chunk encoder, n ≤ 512 tokens, d_model = 768. The O(n²·d) cost is ~150M flops/layer/example. Going to n = 4096 makes the layer cost ~10B flops — that's why long-context encoders use sparse attention.

2. **Scaled dot-product attention recipe** (for any custom attention layer you build):

   ```
   Q = X @ W_Q    # (batch, n, d_k)
   K = X @ W_K    # (batch, n, d_k)
   V = X @ W_V    # (batch, n, d_v)
   scores = (Q @ K.T) / sqrt(d_k)         # divide by sqrt(d_k) to keep softmax in the well-behaved regime
   attn = softmax(scores)
   output = attn @ V
   ```
   The 1/sqrt(d_k) divisor is non-optional — Section 3.2.1 shows without it the dot products grow with d_k, softmax saturates, and gradients vanish.

3. **For retrieval/reranking: bi-encoder uses self-attention only; cross-encoder uses self+cross**:
   - Bi-encoder (fast, scalable): encode query and chunk separately with self-attention. Compare via cosine. Used for first-pass retrieval over millions of chunks.
   - Cross-encoder (slow, accurate): concatenate query and chunk into one sequence, run self-attention over the joint sequence. Used for reranking top-k from the bi-encoder.

4. **Multi-head budget**: Default to 8 heads × d_k=64 for d_model=512, or 12 heads × 64 for d_model=768. Don't use 1 head with full d_model — the paper's ablation Section 3.2.2 shows quality drops.

5. **Positional encoding choice**: Original sinusoidal; modern alternatives RoPE or ALiBi handle longer contexts better. For memory chunks, use whatever your backbone shipped with — don't mix-and-match.

6. **For long-context memory blocks, replace dense attention with sliding-window + global tokens** (Longformer pattern) rather than truncating. Pay attention to which positions get full visibility (CLS, retrieved tokens) — those become your memory hooks.

7. **Cache attention computation across layers when possible**: KV-caching is the standard inference-time optimisation; it works because past K and V vectors don't change as new tokens arrive. Any inference-time memory pipeline should reuse cached K/V where possible.

**Expected outcome:** Solid mental model of the per-layer cost and behaviour of transformers, an informed choice of bi-vs-cross-encoder for the retrieval pipeline, and a baseline configuration (head count, d_model, layers) for any custom attention component the team needs to train.

## Best Figure

![Figure 1 (retroactively extracted)](figures/vaswani-2017-attention-is-all-you-need-fig.png)

**Image Candidates:**
- Figure 1 (p. 3): The canonical encoder-decoder Transformer diagram — single most-reproduced figure in deep learning.
- Figure 2 (p. 4): Scaled dot-product and multi-head attention block diagrams.
- Table 1 (p. 6): Per-layer complexity comparison — Self-Attention O(n²·d) vs RNN O(n·d²) vs Convolution O(k·n·d²) — the foundational rationale for the architecture.

**Best Image:** Figure 1: The Transformer model architecture (p. 3). The encoder stack on the left (6 layers, each with multi-head self-attention + feed-forward), the decoder stack on the right (6 layers, each with masked multi-head self-attention + multi-head cross-attention to encoder + feed-forward), positional encoding fed in to both, the linear+softmax output head. Every paper that came after — BERT (encoder-only), GPT (decoder-only), T5 (both), every retrieval-augmented generator — is a variant or subset of this diagram.

## What Experts Overlook

The 1/sqrt(d_k) scaling factor in scaled dot-product attention is the load-bearing detail almost nobody notices but everything depends on. Section 3.2.1 explains it: as d_k grows, the dot products grow with it, pushing the softmax into regions where the gradient is vanishingly small. Without the divisor, the model literally cannot train at large d_k — you'd hit a gradient floor and progress stops. With it, the variance of the dot products stays roughly constant regardless of d_k.

**Why it matters:** Any time you build a custom attention-like component for a memory system (e.g., a learned reranker that does query-chunk dot products, or an attention-over-memory block), you must apply the same scaling, or you'll get inexplicable training instability when you scale up d_model. The scaling is the reason why "let me just try a bigger query/key dimension" doesn't break the transformer's training dynamics.

**Example of good use:** A memory-architect team building a learned routing layer between retrieved chunks divides their query-chunk dot products by sqrt(d) before softmaxing, even though their layer is "just" a single attention head. Their model trains stably across d_model = 256, 768, 4096.

**Example of misapplication:** A team copies an attention block from a tutorial that omits the sqrt(d_k) divisor (it's a common bug in toy code). Training works fine at d_model = 256 but inexplicably plateaus at d_model = 1024. They blame the data, the optimiser, anything except the missing scaling.

## Extracted Prompts

```
No applicable prompts found in this paper. (Attention Is All You Need is a pre-LLM-era paper. It trains an encoder-decoder for translation; there are no LLM prompts.)
```

## Citations

- LSTM (Hochreiter & Schmidhuber, 1997)
- Bahdanau attention (2014) — arxiv:1409.0473
- Seq2seq learning (Sutskever et al., 2014) — arxiv:1409.3215
- Layer normalization (Ba et al., 2016) — arxiv:1607.06450
- Deep residual learning / ResNet (He et al., 2016) — arxiv:1512.03385
- Adam optimiser (Kingma & Ba, 2015) — arxiv:1412.6980
- ConvS2S (Gehring et al., 2017) — arxiv:1705.03122
- Dropout (Srivastava et al., 2014)
- (Full ~40-reference list in frontmatter `citations:`)

## Related Digests

- [[devlin-2018-bert]] — BERT (encoder-only Transformer)
- [[brown-2020-gpt3-few-shot]] — GPT-3 (decoder-only Transformer at scale)
- [[beltagy-2020-longformer]] — Longformer (sparse-attention variant for long inputs)
- [[dai-2019-transformer-xl]] — Transformer-XL (recurrence + attention for long sequences)
- [[radford-2018-gpt1]] — GPT-1 (the original decoder-only Transformer LM)

## Reviewer Notes

**Overall severity:** Clean

Claims cross-checked against the loaded paper text:
- WMT 2014 EN-DE 28.4 BLEU — verified Abstract.
- WMT 2014 EN-FR 41.8 BLEU, 3.5 days on 8 P100 GPUs — verified Abstract.
- 6-layer encoder + 6-layer decoder, multi-head attention with 8 heads — verified Section 3.
- Scaled dot-product attention with 1/sqrt(d_k) divisor — verified Section 3.2.1.
- O(n²·d) self-attention vs O(n·d²) recurrent — verified Table 1 / Section 4.
- d_ff = 2048, d_model = 512 base — verified Section 3.3.
