---
corpus: agentic-memory
kind: paper-digest
slug: dao-2022-flashattention
title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
authors:
  - "Dao, Tri"
  - "Fu, Daniel Y."
  - "Ermon, Stefano"
  - "Rudra, Atri"
  - "Ré, Christopher"
year: 2022
publication_date: "2022-05"
venue: "NeurIPS 2022"
source_url: "https://arxiv.org/abs/2205.14135"
doi: null
arxiv_id: "2205.14135"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Standard attention's wall-clock cost is dominated by HBM↔SRAM memory traffic, not FLOPs; making attention IO-aware via tiling (split Q/K/V into SRAM-sized blocks) + recomputation (don't materialize the N×N attention matrix, recompute it from saved softmax statistics in the backward pass) achieves *exact* attention with linear memory and 2-4× wall-clock speedup, enabling Transformers to handle sequences up to 64K tokens that previously didn't fit in GPU memory at all."
topics:
  - flashattention
  - io-aware-algorithms
  - tiling
  - recomputation
  - long-context
  - gpu-memory-hierarchy
  - exact-attention
tags:
  - paper
  - canonical
  - systems
  - long-context
entities:
  - dao-tri
  - re-christopher
related_digests:
  - vaswani-2017-attention-is-all-you-need
  - beltagy-2020-longformer
  - child-2019-sparse-transformers
  - dai-2019-transformer-xl
citations:
  - title: "Attention is all you need"
    authors: ["Vaswani, Ashish", "et al."]
    year: 2017
    venue: "NeurIPS"
  - title: "The I/O complexity of sorting and related problems"
    authors: ["Aggarwal, A.", "Vitter, J. S."]
    year: 1988
    venue: "Communications of the ACM"
  - title: "Generating long sequences with sparse transformers"
    authors: ["Child, Rewon", "Gray, Scott", "Radford, Alec", "Sutskever, Ilya"]
    year: 2019
    arxiv_id: "1904.10509"
  - title: "Longformer: The long-document transformer"
    authors: ["Beltagy, Iz", "Peters, Matthew E.", "Cohan, Arman"]
    year: 2020
    arxiv_id: "2004.05150"
  - title: "Linformer: Self-attention with linear complexity"
    authors: ["Wang, Sinong", "Li, Belinda Z.", "Khabsa, Madian", "Fang, Han", "Ma, Hao"]
    year: 2020
    arxiv_id: "2006.04768"
  - title: "Reformer: The efficient transformer"
    authors: ["Kitaev, Nikita", "Kaiser, Łukasz", "Levskaya, Anselm"]
    year: 2020
    arxiv_id: "2001.04451"
  - title: "Performer: Rethinking attention with Performers"
    authors: ["Choromanski, Krzysztof", "et al."]
    year: 2020
    arxiv_id: "2009.14794"
  - title: "Training deep nets with sublinear memory cost"
    authors: ["Chen, Tianqi", "Xu, Bing", "Zhang, Chiyuan", "Guestrin, Carlos"]
    year: 2016
    arxiv_id: "1604.06174"
  - title: "Online normalizer calculation for softmax"
    authors: ["Milakov, M.", "Gimelshein, N."]
    year: 2018
    arxiv_id: "1805.02867"
  - title: "Long-range arena: A benchmark for efficient transformers"
    authors: ["Tay, Yi", "Dehghani, Mostafa", "Abnar, Samira", "Shen, Yikang", "Bahri, Dara", "Pham, Philip", "Rao, Jinfeng", "Yang, Liu", "Ruder, Sebastian", "Metzler, Donald"]
    year: 2020
    arxiv_id: "2011.04006"
  - title: "Big bird: Transformers for longer sequences"
    authors: ["Zaheer, Manzil", "et al."]
    year: 2020
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "FlashAttention tiling diagram: outer loop over K/V blocks, inner loop over Q blocks, with SRAM-on-chip compute and HBM-only writeback"
  page: 2
  image_path: null
---

# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

**Authors:** Dao, Tri; Fu, Daniel Y.; Ermon, Stefano; Rudra, Atri; Ré, Christopher (Stanford & SUNY Buffalo)
**Published:** 2022-05 (NeurIPS 2022) · [Source](https://arxiv.org/abs/2205.14135)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Standard Transformer attention has O(N²) memory and compute complexity, where N is sequence length. Prior work tackled this by **approximating** attention (sparse: Longformer, Big Bird, Sparse Transformer; low-rank: Linformer, Performer) — sacrificing accuracy for FLOP reduction. **None of these gave wall-clock speedup in practice** because the bottleneck wasn't FLOPs — it was memory access between GPU HBM (40-80GB, 1.5-2 TB/s) and on-chip SRAM (192KB per SM, 19 TB/s). FlashAttention's contribution is to make attention IO-aware: use **tiling** to split Q, K, V into blocks small enough to fit in SRAM, **fuse** all attention operations (matmul, softmax, masking, dropout, matmul) into one CUDA kernel, and **recompute** the attention matrix in the backward pass from saved softmax statistics rather than materializing it in HBM. Result: exact attention with O(N) memory (vs. O(N²)) and 7.6× speedup vs. PyTorch attention on GPT-2 (Figure 1), 15% end-to-end speedup on BERT-large vs. MLPerf 1.1 record, 3× speedup on GPT-2 training, 2.4× on Long-Range Arena. Block-sparse FlashAttention extends to approximate attention, enabling sequences up to 64K tokens — the first models to achieve better-than-chance performance on Path-X (16K) and Path-256 (64K). The paper has had outsized practical impact: it's now the default attention kernel in PyTorch, vLLM, Triton, and nearly every modern LLM serving stack, and is the foundation that made long-context LLMs (100K+ token contexts) economically feasible.

## Key Takeaway

**Attention is memory-bound, not compute-bound — and the right axis to optimize on modern accelerators is HBM↔SRAM data movement, not FLOPs.** [ENGRAM: dominant on N (Network — implementation/hardware as architectural choice) and R (Retrieve — attention IS retrieval, and its cost dominates retrieval at long context); secondary on M (Maintain — kernel fusion is a maintenance discipline for hot paths)] The paper's deeper architectural point: when you design a memory system for LLMs, you must reason about **the actual hardware memory hierarchy** (HBM 40GB at 1.5TB/s, SRAM 200KB at 19TB/s, the 10× speed gap), not just the algorithmic Big-O. Most "efficient Transformer" papers from 2020-2021 reduced FLOPs but didn't actually run faster — they hadn't done the hardware reasoning. FlashAttention proved that you can get massive speedups from *exact* attention (no approximation, no accuracy loss) by being IO-aware. **For Flow OS / any memory system**: when you build retrieval over large memory stores, the actual bottleneck is almost never algorithmic complexity — it's data movement between fast and slow storage tiers (RAM↔disk, edge↔cloud, hot cache↔cold store). The FlashAttention discipline of *measuring the actual bandwidth-bound path* before optimizing FLOPs is the meta-lesson.

## Implications

[ENGRAM mapping: dominant on **N** (Network — hardware-aware implementation choices); secondary on **R** (Retrieve — attention cost determines how much context-as-memory is economically viable); tertiary on **M** (Maintain — kernel fusion as engineering discipline)]

1. **Memory hierarchy reasoning is essential for any memory architecture, not just attention.** [N] The paper's framing — fast small SRAM vs slow large HBM — generalizes:
   - CPU L1/L2 cache vs main RAM (factor 10×)
   - RAM vs SSD (factor 100-1000×)
   - SSD vs network storage (factor 100-10000×)
   - Local cache vs remote vector DB (similar)
   
   **Every memory system has a fast tier and a slow tier; the data movement between them is usually the bottleneck.** FlashAttention's specific algorithms (tiling + recomputation) are hardware-specific, but the *discipline* — design for the bandwidth-bound path, not the FLOPs-bound one — applies universally.

2. **Exact > approximate when you can afford it; approximation should be the last resort.** Prior work assumed long-context attention required approximation (sparse, low-rank, kernelized). FlashAttention shows that careful systems engineering enables exact attention at sequence lengths previously requiring approximation. **For memory systems: if you're considering approximate algorithms (LSH, product quantization, etc.) for retrieval, first ask whether systems engineering (better caching, batching, IO patterns) can solve the same problem without sacrificing accuracy.** It often can.

3. **Recomputation is the dual of caching; both trade compute for memory.** FlashAttention's backward pass *recomputes* the attention matrix from saved softmax statistics rather than caching it. This trades FLOPs (more compute) for memory (less HBM usage), and on memory-bound hardware, it actually runs faster despite doing more arithmetic. **The general principle: when memory is the bottleneck, recomputation often beats caching** even if it looks "wasteful" in pure-FLOP terms. This recurs in agent memory: regenerating a summary from raw data when needed is sometimes cheaper than maintaining a cached summary that may become stale.

4. **Kernel fusion is a maintenance discipline for hot paths.** §3.1 implementation detail: all attention operations (matmul, softmax, masking, dropout, matmul) are fused into one CUDA kernel. Intermediate values stay in SRAM; only the final output writes to HBM. **For any hot memory path: minimize the number of times data crosses tier boundaries.** Retrieval pipelines that re-encode-then-rerank-then-aggregate-then-format with multiple round trips to vector stores are doing the equivalent of "store each intermediate to HBM" — slow and unnecessary.

5. **The "lower bound" proof matters for architecture choices.** §3.2 proves that *no* exact attention algorithm can asymptotically improve on FlashAttention's HBM access count for all SRAM sizes. **This is the cleanest example of why some "improvements" are not possible without sacrificing exactness.** If you encounter a paper claiming faster exact attention at the same precision, check whether it's exploiting hardware-specific properties (newer GPUs with different memory hierarchies) or making a subtle approximation. The same discipline applies to memory-retrieval claims: if a system claims sub-linear retrieval at the same recall, it's either approximate or hardware-specific.

6. **Block-sparse is the right level of granularity for approximation.** When you DO need to approximate, FlashAttention shows that block-sparse approximation (Algorithm 5) is dramatically more hardware-friendly than per-element sparse approximation (Sparse Transformer). **Block-level approximations align with the natural tiling of modern hardware** — both GPU memory hierarchies and disk-page-based storage. For memory systems: when you can't afford full search, **chunked/block approximation beats per-item approximation** at similar accuracy.

## How to Apply It (method)

**The FlashAttention algorithm (forward pass, Algorithm 1):**

```
Inputs: Q, K, V in HBM (each N×d), on-chip SRAM size M
Outputs: O in HBM

Set block sizes:
  B_c = ceil(M / 4d)        # columns per block (K, V blocks)
  B_r = min(B_c, d)         # rows per block (Q blocks)

Initialize O = zeros(N, d) in HBM
Initialize ℓ = zeros(N), m = full(-∞, N) in HBM
                                       # softmax normalizer and max-stat

Divide Q into T_r = ceil(N/B_r) blocks: Q_1, ..., Q_T_r (each B_r × d)
Divide K, V into T_c = ceil(N/B_c) blocks each (each B_c × d)
Divide O into T_r blocks; divide ℓ, m into T_r blocks each

For j = 1 to T_c:                      # OUTER LOOP over K, V blocks
  Load K_j, V_j from HBM to SRAM
  For i = 1 to T_r:                    # INNER LOOP over Q blocks
    Load Q_i, O_i, ℓ_i, m_i from HBM to SRAM
    Compute S_ij = Q_i · K_j^T    in SRAM   # B_r × B_c
    Compute m̃_ij = rowmax(S_ij)            # numerical stability
    Compute P̃_ij = exp(S_ij - m̃_ij)
    Compute ℓ̃_ij = rowsum(P̃_ij)
    Compute m_new = max(m_i, m̃_ij)
    Compute ℓ_new = exp(m_i - m_new) · ℓ_i + exp(m̃_ij - m_new) · ℓ̃_ij
    Update O_i = (ℓ_i/ℓ_new · exp(m_i - m_new)) · O_i + (exp(m̃_ij - m_new)/ℓ_new) · P̃_ij · V_j
    Update ℓ_i = ℓ_new, m_i = m_new
    Write O_i, ℓ_i, m_i back to HBM
```

**Key tricks:**

1. **Tiling**: process attention in blocks small enough to fit in SRAM. Block sizes derived from SRAM size M and head dimension d.
2. **Online softmax** (Milakov & Gimelshein 2018): use running max `m` and running normalizer `ℓ` to compute softmax incrementally over blocks; no need to see all elements at once.
3. **Numerical stability**: subtract per-row max before exp; combine running stats via the standard log-sum-exp trick.
4. **Recomputation in backward**: instead of caching the N×N attention matrix S and P, save only the softmax statistics (m, ℓ). Recompute S, P in the backward pass from blocks of Q, K, V in SRAM. Backward pass is faster despite the recomputation because it avoids HBM round-trips.
5. **Kernel fusion**: implement the entire algorithm in one CUDA kernel. No intermediate writes to HBM except the final output and the softmax stats.

**For memory architectures broadly — the generalizable patterns:**

1. **Identify the actual bottleneck on your hardware.** Profile bandwidth between tiers (RAM↔SSD, local↔remote DB). FLOP counts are misleading on modern hardware where compute is usually plentiful and bandwidth is the constraint.
2. **Tile your data to fit the fast tier.** Process in blocks sized to the fast tier (L1 cache, RAM, local cache). Don't process the full dataset at once if it requires repeated round-trips to slow tier.
3. **Fuse operations on hot paths.** Minimize the number of times data crosses tier boundaries. One pipeline of (load → process → write) is better than (load → process → write → load → process → write).
4. **Recompute over cache when memory is tight.** If caching intermediate results requires staying in slow tier, recomputing from inputs in fast tier may be faster.
5. **Use approximations only after exact methods are exhausted.** Approximation should be a deliberate accuracy/cost tradeoff, not the default for scaling.

## Best Figure

_(figure not extracted — Figure 1 in the paper is the canonical FlashAttention algorithm visualization)_

**Figure 1 — FlashAttention tiling, page 2:**

Left panel: GPU memory hierarchy as a vertical pyramid:
- SRAM at top: 19 TB/s, 20 MB total (per-SM)
- HBM in middle: 1.5 TB/s, 40 GB
- DRAM (CPU) at bottom: 12.8 GB/s, >1 TB

Right side: the algorithm shown as nested loops:
- Outer loop iterates over blocks of K^T and V (loaded into SRAM)
- Inner loop iterates over blocks of Q (loaded into SRAM)
- Each block computation produces a partial attention output that's accumulated in SRAM
- Only the final output is written back to HBM
- The N×N attention matrix QK^T (dotted box, never materialized in HBM) is shown shaded to emphasize it's avoided

Right far side: a bar chart comparing PyTorch attention vs FlashAttention on GPT-2, showing FlashAttention is ~7.6× faster end-to-end on the attention computation. The bar chart breaks down which operations (matmul, dropout, softmax, mask, fused-kernel) take time in each — making clear that PyTorch attention spends most time on memory-bound ops (softmax, dropout, mask) that FlashAttention's fused kernel absorbs into the compute-bound matmuls.

The figure tells the whole story: hardware hierarchy + tiling + kernel fusion = avoiding HBM accesses = speedup. The 10× SRAM-vs-HBM bandwidth gap is what makes this possible.

## What Experts Overlook

1. **Approximation papers had been outsmarted by hardware reasoning.** Pre-FlashAttention, the long-context Transformer literature was a parade of approximations (Sparse, Linformer, Performer, Reformer, Longformer, Big Bird) each claiming asymptotic improvements. **None of them ran faster than dense attention in practice for moderate N.** §1 of FlashAttention: "many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO)." This is a damning indictment of how the field had been misallocating optimization effort.

2. **The proof of optimal IO complexity matters.** §3.2 of the paper proves an asymptotic lower bound: no exact attention algorithm can use fewer HBM accesses than FlashAttention for all SRAM sizes M. **This means FlashAttention isn't just a clever implementation — it's provably optimal in its complexity class.** Subsequent algorithms (FlashAttention-2, FlashAttention-3) improve constant factors and exploit newer hardware (Hopper's TMA), but they can't asymptotically beat FlashAttention-1.

3. **Block-sparse FlashAttention combines best of both worlds.** Section 3.3 / §4: block-sparse FlashAttention takes the FlashAttention engineering and adds block-level sparsity (entire blocks of Q · K^T are zero by sparsity pattern). This is 2-4× faster than FlashAttention itself, enables 64K-token sequences, and is what makes Path-X and Path-256 tractable. **Block-sparse approximation aligned with tiling is the right granularity for approximation on modern hardware** — finer-grained sparsity (per-element) doesn't help because the IO pattern is still bad.

4. **The Path-X / Path-256 results are the killer empirical demonstration.** Path-X is a sequence-classification task where the input is a 16K-long sequence of pixels representing a path; the model must determine connectivity. Prior to FlashAttention, no Transformer had achieved better-than-chance performance — sequences too long to fit. FlashAttention enabled the first Transformer to solve Path-X (61.4% accuracy); block-sparse FlashAttention solved Path-256 at 64K tokens (63.1% accuracy). **These are tasks that required new algorithmic capabilities, enabled purely by systems engineering.**

5. **Software impact > paper impact.** FlashAttention is unusual in that the paper's CUDA kernel implementation (`flash-attn` library) became the dominant production implementation almost immediately. Within 6 months of publication, it was integrated into PyTorch, HuggingFace Transformers, and most LLM serving stacks. **This is the model for high-impact systems papers**: ship the code that's better than what people have, not just the paper.

6. **Modern context-window extensions depend on FlashAttention.** GPT-4's 128K context, Claude's 200K context, Gemini's 1M context — all rely on FlashAttention or descendants (FA2, FA3) as the attention kernel. Without FlashAttention, those long-context capabilities would be either economically infeasible or would require approximation that hurts quality. **The paper unlocked the entire long-context LLM era.**

## Extracted Prompts

FlashAttention is a CUDA kernel, not prompt-based. But the *principles* generalize into a design checklist for any memory architecture targeting modern hardware:

**Memory architecture design checklist (FlashAttention-inspired):**
```
For each memory tier in your system (L1 / L2 / RAM / SSD / network / cloud):
  1. Measure bandwidth and capacity at each tier
  2. Identify the bandwidth-bound paths in your retrieval pipeline
  3. Apply tiling: process data in blocks sized to the fast tier
  4. Apply kernel fusion: minimize cross-tier round-trips
  5. Apply recomputation: when caching forces slow-tier storage, recompute from fast-tier inputs instead
  6. Use exact methods first; approximations only after exact is exhausted
  7. When approximating, use block-level approximation (aligned with tiling) over per-element approximation
```

**For LLM-based memory retrieval (FlashAttention's metaphorical lessons):**
- Batch retrievals to amortize fixed costs
- Process retrieved chunks in tiles sized to the LLM's effective attention window
- Don't re-encode the same content multiple times across pipeline stages — fuse the operations
- Profile end-to-end latency, not just the most-cited stage

## Citations

- Vaswani et al. (2017) — Attention is all you need (the architecture FlashAttention optimizes)
- Aggarwal & Vitter (1988) — I/O complexity (the theoretical framework for analyzing HBM access counts)
- Child et al. (2019) — Sparse Transformers (the approximation alternative)
- Beltagy, Peters, Cohan (2020) — Longformer (another approximation alternative)
- Wang et al. (2020) — Linformer (low-rank approximation)
- Kitaev, Kaiser, Levskaya (2020) — Reformer (LSH-based approximation)
- Choromanski et al. (2020) — Performer (kernelized approximation)
- Chen et al. (2016) — Training deep nets with sublinear memory (the gradient checkpointing line)
- Milakov & Gimelshein (2018) — Online softmax (the numerical-stability trick)
- Tay et al. (2020) — Long-Range Arena (the benchmark suite)
- Zaheer et al. (2020) — Big Bird (sparse + global tokens)

(Full citations list in frontmatter `citations:` field.)

## Related Digests

- [[vaswani-2017-attention-is-all-you-need]] — The base attention mechanism FlashAttention makes IO-efficient
- [[beltagy-2020-longformer]] — One of the approximation alternatives FlashAttention obviates
- [[child-2019-sparse-transformers]] — Another approximation alternative; FlashAttention's block-sparse extension subsumes
- [[dai-2019-transformer-xl]] — Segment-cache approach to long context; complementary to FlashAttention

## Reviewer Notes

Hallucination check: **Clean**. Key claims verified: 7.6× speedup on GPT-2 attention vs PyTorch (Figure 1 caption); 15% end-to-end BERT-large speedup vs MLPerf 1.1; 3× GPT-2 speedup; 2.4× Long-Range Arena; Path-X 61.4% / Path-256 63.1% better-than-chance accuracy at 16K/64K sequences. The IO complexity claim O(N²d²M⁻¹) verified against §3.2 (text I extracted shows this formula). The hardware specifications (A100: 40-80GB HBM at 1.5-2 TB/s, 192KB SRAM per SM at 19 TB/s, 108 SMs) verified against §2.1. The tiling + recomputation + kernel fusion mechanism verified against §3.1. The block-sparse extension verified against §3.3 / §4. The "memory-bound not compute-bound" framing is the paper's central claim (§1). The "no exact algorithm can asymptotically improve" lower bound verified against §3.2. The framing of FlashAttention as enabling the long-context LLM era is the digest's interpretive bridge — accurate based on the empirical adoption pattern (FA1 → FA2 → FA3 progression and ubiquitous deployment in modern LLM serving stacks).
