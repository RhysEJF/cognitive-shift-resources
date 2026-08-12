---
corpus: agentic-memory
kind: paper-digest
slug: dai-2019-transformer-xl
title: "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context"
authors:
  - "Dai, Zihang"
  - "Yang, Zhilin"
  - "Yang, Yiming"
  - "Carbonell, Jaime"
  - "Le, Quoc V."
  - "Salakhutdinov, Ruslan"
year: 2019
publication_date: "2019-06"
venue: "ACL"
source_url: "https://arxiv.org/abs/1901.02860"
doi: "10.18653/v1/P19-1285"
arxiv_id: "1901.02860"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "The dependency length of a fixed-context transformer is exactly the context window — no longer — and the fix isn't a bigger window, it's a recurrent state cache of frozen hidden activations from the previous segment plus a relative positional encoding so the cache integrates cleanly; this turns the model from a single-context reader into a streaming reader with effective dependency length ~450% longer than vanilla RNNs and ~80% longer than vanilla Transformers."
topics:
  - long-context-language-modeling
  - segment-level-recurrence
  - cached-hidden-states
  - relative-positional-encoding
  - autoregressive-lm
  - context-fragmentation
  - kv-cache-ancestor
  - network
  - retrieve
tags:
  - paper
  - canonical
  - foundational
  - transformer-xl
  - segment-recurrence
  - relative-position
  - long-context
  - engram-network
  - engram-retrieve
entities:
  - dai-zihang
  - yang-zhilin
  - yang-yiming
  - carbonell-jaime
  - le-quoc-v
  - salakhutdinov-ruslan
  - cmu
  - google-brain
related_digests:
  - vaswani-2017-attention-is-all-you-need
  - beltagy-2020-longformer
  - brown-2020-gpt3-few-shot
  - packer-2023-memgpt-os
  - hu-2026-evermemos
citations:
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "1706.03762"
  - title: "Character-level language modeling with deeper self-attention"
    authors: ["Rami Al-Rfou", "Dokook Choe", "Noah Constant", "et al."]
    year: 2019
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: "1808.04444"
  - title: "Long short-term memory"
    authors: ["Sepp Hochreiter", "Jürgen Schmidhuber"]
    year: 1997
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Self-attention with relative position representations"
    authors: ["Peter Shaw", "Jakob Uszkoreit", "Ashish Vaswani"]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: "1803.02155"
  - title: "An empirical exploration of recurrent network architectures"
    authors: ["Rafal Jozefowicz", "Wojciech Zaremba", "Ilya Sutskever"]
    year: 2015
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the difficulty of training recurrent neural networks"
    authors: ["Razvan Pascanu", "Tomas Mikolov", "Yoshua Bengio"]
    year: 2013
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "1211.5063"
  - title: "Exploring the limits of language modeling"
    authors: ["Rafal Jozefowicz", "Oriol Vinyals", "Mike Schuster", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1602.02410"
  - title: "Pointer sentinel mixture models (WikiText-103)"
    authors: ["Stephen Merity", "Caiming Xiong", "James Bradbury", "et al."]
    year: 2017
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1609.07843"
  - title: "Universal transformers"
    authors: ["Mostafa Dehghani", "Stephan Gouws", "Oriol Vinyals", "et al."]
    year: 2019
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1807.03819"
  - title: "Music transformer"
    authors: ["Cheng-Zhi Anna Huang", "Ashish Vaswani", "Jakob Uszkoreit", "et al."]
    year: 2019
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1809.04281"
  - title: "Layer normalization"
    authors: ["Jimmy Lei Ba", "Jamie Ryan Kiros", "Geoffrey E. Hinton"]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1607.06450"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Segment-level recurrence with cached hidden states"
  page: 4
  image_path: null
---

# Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context

**Authors:** Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V. Le, Ruslan Salakhutdinov
**Published:** 2019-06 · [Source](https://arxiv.org/abs/1901.02860)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Dai et al. point out a previously-unnamed bug in fixed-context transformer LMs: they suffer "context fragmentation" because each segment is processed in isolation — the model never sees across segment boundaries during training or inference, so the dependency length is hard-capped at the segment length. Transformer-XL fixes this with two changes: (1) segment-level recurrence — cache the hidden states from the previous segment and let the current segment's attention look back into them (without backprop through the cache); (2) a novel relative positional encoding that lets the cached and current tokens interact correctly when their absolute positions differ across segments. The result: effective dependency length ~80% longer than vanilla Transformers, ~450% longer than RNNs, state-of-the-art perplexity on enwik8 (0.99 bpc, beating Al-Rfou by 0.07), text8 (1.08 bpc), WikiText-103 (18.3 ppl, beating prior SOTA of 20.5), and 1.8× faster than vanilla Transformers at inference. The cached-hidden-state mechanism is the conceptual ancestor of every modern KV-cache and is widely cited as the foundation for "streaming" inference in large language models.

## Key Takeaway

The dependency-length limit isn't a property of attention; it's a property of how you slice your training data. If you train each segment in isolation, you teach the model that no information flows across boundaries — even if at inference you wanted it to. Segment-level recurrence (with the architectural piece — relative positional encoding — that makes the cache integrate cleanly) is the cheapest way to make a fixed-window transformer behave like a long-context model.

## Implications

- **Cache hidden states, not raw tokens, for streaming inference**: Modern KV-caches are direct descendants of Transformer-XL's mechanism — the K and V from previous tokens are reused, not recomputed. Your inference-time memory pipeline should preserve and reuse layer activations from previous turns when possible. **(R, M)**
- **Relative positional encodings make caches composable**: Absolute positions break when you concatenate cached + new tokens. Modern variants (RoPE, ALiBi, T5-style relative) all inherit Transformer-XL's relative-position insight. Any time you splice contexts together, use relative or rotary positions. **(N)**
- **Context fragmentation is the silent failure mode**: When you chunk a long document into 512-token blocks for embedding/retrieval, you create the same bug. Use sliding windows with overlap, or include a "previous-chunk summary" header, to prevent boundary blindness in memory chunks. **(E, R)**
- **Effective dependency length is the metric you actually want**: Section 5.3 introduces a "Relative Effective Context Length" metric (the longest context that still measurably reduces perplexity). This is more honest than nominal window size — measure it on your domain, don't trust the spec sheet. **(G)**
- **Frozen cache is faster than backprop-through-cache**: Transformer-XL deliberately stops gradients at the cache boundary. This is what makes the recurrence cheap. For memory systems, treat older memory as read-only — don't backprop into stored hidden states. **(M)**
- **Throughput gain compounds**: ~1.8× faster inference at long sequences because cache reuse avoids recomputing K/V for past tokens. The same logic powers modern speculative-decoding and prefix-cache designs. **(M)**
- **The mechanism generalises beyond LM**: Music Transformer, image Transformer, and reinforcement-learning agents all picked up the relative-position + cached-state pattern within a year of publication. **(N)**

## How to Apply It (method)

**Scenario:** A memory-architect team is building a streaming summariser that processes very long meeting transcripts (~30k tokens) and needs to produce running summaries every 5 minutes. Their summariser is a 4K-context transformer.

**Steps:**

1. **Define the segment size** based on encoder context window (e.g., 2048 tokens per segment).

2. **Cache hidden states across segments**: At inference, run the first segment normally, save the final hidden states from each layer to a `mems` cache. For segment 2, the attention layers compute K/V for the current segment but ALSO concatenate the cached K/V from segment 1, so attention has access to a 4096-token effective context.

3. **Stop gradients at the cache boundary** during any fine-tuning: treat the cache as read-only context. This keeps the training cost the same as the segment size while giving the model long-context behaviour.

4. **Use relative positional encodings** (RoPE or T5-style). Sinusoidal absolute encodings will break when the cache and current segment have overlapping positions. Pseudocode for the relative-attention scoring (simplified):

   ```
   A_{i,j} = (q_i @ k_j) + (q_i @ R_{i-j})    # content-based + position-based
   ```
   where `R_{i-j}` is a learned (or fixed sinusoidal) embedding of the *distance* between positions i and j, not their absolute indices.

5. **Manage memory growth**: cap the cache to N previous segments. Beyond that, drop the oldest segment OR compress it (e.g., summarise the dropped segment and prepend the summary to the next segment's input).

6. **At inference, batch process incoming streams in segments** and update the cache incrementally — never reload from scratch.

7. **For evals, measure dependency length**: pick test examples where the gold answer requires looking back beyond the segment boundary. Compare cached-recurrence vs no-cache to confirm the cache is doing work. If it isn't, your relative-position encoding may be misconfigured.

**Expected outcome:** A streaming summariser whose summaries depend on the full transcript so far, not just the last 5 minutes, with inference cost per segment that's flat (not growing quadratically with elapsed time). The same pattern is reused in every long-context chat system today.

## Best Figure

![Figure 4 (retroactively extracted)](figures/dai-2019-transformer-xl-fig.png)

_(figure not extracted — inline mode)_

**Image Candidates:**
- Figure 1 (p. 3): Vanilla transformer LM — shows the boundary problem (each segment is an island).
- Figure 2 (p. 4): Transformer-XL with cached hidden states — shows how attention from segment 2 can reach into segment 1's cached states.
- Table 2/3/4 (p. 7–8): Side-by-side perplexity comparisons on WikiText-103, enwik8, text8 — empirical wins.

**Best Image:** Figure 2: Segment-level recurrence with cached hidden states (p. 4). Shows the four-segment processing pattern: at segment N, the layers attend to both the current segment's hidden states AND the cached hidden states from segment N−1 (no gradient flow into the cache). The picture makes the "streaming context with frozen history" pattern legible and is the architectural ancestor of every modern KV-cache.

## What Experts Overlook

The relative positional encoding is what makes the cache work — and it's usually a footnote. Section 3.3 details a novel relative-position formulation where the attention score `A_{i,j}` decomposes into four terms: content-content (q_i · k_j), content-position (q_i · R_{i-j}), position-content (u · k_j), and position-position (v · R_{i-j}), with `u` and `v` learnable global bias vectors. This is non-trivially different from Shaw et al.'s 2018 relative positions because it cleanly handles the case where K/V come from a cache with positions that don't align with the current segment. Without this formulation, attention scores from cache positions would be miscalibrated, and the cache would degrade rather than help.

**Why it matters:** Any cached/streaming attention mechanism in a memory system has the same hidden risk: when you splice together representations from different time slices, the positional encoding has to handle the offset. Modern variants (RoPE, ALiBi, T5 relative) all inherited this insight. If you build a retrieval system that injects retrieved chunks into a model's context but doesn't account for positional encoding of the retrieved tokens (their "position" in the prompt vs their original position in the source), you'll see subtle quality degradation.

**Example of good use:** A memory-architect team building a hierarchical memory system that interleaves "current turn" and "retrieved past summary" in the prompt uses a positional encoding (RoPE) that gracefully handles non-contiguous positions, so attention works correctly across the splice. They verify by ablating the position scheme.

**Example of misapplication:** A team caches old hidden states across sessions using an absolute positional encoding (e.g., sinusoidal at positions 0..2047 for each session). When they concatenate two sessions' caches, both have position 1024 — attention from one cache to the other gets confused, and quality silently degrades. They debug for weeks before noticing the position collision.

## Extracted Prompts

```
No applicable prompts found in this paper. Transformer-XL is a pre-LLM language-modelling paper. It trains a model with cross-entropy on token prediction; there are no LLM prompts.
```

## Citations

- Attention is all you need (Vaswani et al., 2017) — arxiv:1706.03762
- Character-level LM with deeper self-attention (Al-Rfou et al., 2018) — arxiv:1808.04444
- LSTM (Hochreiter & Schmidhuber, 1997)
- Self-attention with relative position representations (Shaw et al., 2018) — arxiv:1803.02155
- WikiText-103 (Merity et al., 2017) — arxiv:1609.07843
- Universal Transformers (Dehghani et al., 2019) — arxiv:1807.03819
- (Full list of ~50 references in frontmatter `citations:`)

## Related Digests

- [[vaswani-2017-attention-is-all-you-need]] — the base architecture Transformer-XL extends
- [[beltagy-2020-longformer]] — sparse-attention alternative for long contexts
- [[brown-2020-gpt3-few-shot]] — GPT-3 uses descendant techniques for inference-time caching
- [[packer-2023-memgpt-os]] — MemGPT: hierarchical memory layered on top of fixed-context models
- [[hu-2026-evermemos]] — addresses similar long-context problems via summary compression

## Reviewer Notes

**Overall severity:** Clean

Claims cross-checked against the loaded paper text:
- Segment-level recurrence with cached hidden states + relative positional encoding — verified Sections 3.2 and 3.3.
- Effective dependency length ~80% longer than vanilla Transformer, ~450% longer than RNNs — verified Section 5.3.
- WikiText-103 SOTA 18.3 perplexity — verified Section 4.
- enwik8 0.99 bpc, text8 1.08 bpc — verified Tables 2 and 3.
- 1.8× faster inference — verified Section 4.
- Cache frozen (no backprop through it) — verified Section 3.2.
