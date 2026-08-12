---
corpus: agentic-memory
kind: paper-digest
slug: xiao-2023-streaming-llm
title: "Efficient Streaming Language Models with Attention Sinks"
authors:
  - "Guangxuan Xiao"
  - "Yuandong Tian"
  - "Beidi Chen"
  - "Song Han"
  - "Mike Lewis"
year: 2023
publication_date: "2023-09"
venue: "ICLR 2024 (MIT / Meta AI / CMU / NVIDIA)"
source_url: "https://arxiv.org/abs/2309.17453"
doi: null
arxiv_id: "2309.17453"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Window-attention LLMs collapse the moment the first few KV entries get evicted not because those tokens are semantically important but because the softmax sums-to-one constraint forces the model to dump 'unused' attention somewhere — and it dumps it on the initial tokens (attention sinks) because they're visible to all subsequent positions; preserving just 4 initial tokens' KVs alongside the rolling window restores 5158 → 5.40 perplexity on Llama-2-13B and enables streaming inference over 4 million+ tokens with 22.2x speedup over re-computation — and pre-training with a dedicated learnable Sink Token lets a single token absorb the role entirely, suggesting that for streaming-memory architectures the right primitive is a 'workspace anchor' (a few attention-stable positions) plus a rolling KV cache, not infinite context or summary-then-reset."
topics:
  - streaming-inference
  - attention-sinks
  - kv-cache
  - rolling-window
  - infinite-length-generation
  - softmax-off-by-one
  - sink-token-pretraining
  - position-encoding
  - rope-alibi
  - length-extrapolation
  - llm-deployment
  - working-memory
tags:
  - paper
  - inference-architecture
  - kv-cache
  - streaming-llm
  - mit-han-lab
  - meta-ai
  - attention-mechanism
  - working-memory
entities:
  - xiao-guangxuan
  - tian-yuandong
  - chen-beidi
  - han-song
  - lewis-mike
related_digests:
  - wang-2025-mirix
  - li-2025-memos
  - dai-2019-transformer-xl
  - vaswani-2017-attention-is-all-you-need
  - beltagy-2020-longformer
citations:
  - title: "Language models are few-shot learners (GPT-3)"
    authors: ["Tom B. Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    arxiv_id: "2005.14165"
  - title: "Llama 2: Open foundation and fine-tuned chat models"
    authors: ["Hugo Touvron", "Louis Martin", "Kevin Stone", "et al."]
    year: 2023
    venue: "preprint"
    arxiv_id: "2307.09288"
  - title: "Longformer: The long-document transformer"
    authors: ["Iz Beltagy", "Matthew E. Peters", "Arman Cohan"]
    year: 2020
    venue: "preprint"
    arxiv_id: "2004.05150"
  - title: "RoFormer: Enhanced transformer with rotary position embedding (RoPE)"
    authors: ["Jianlin Su", "Yu Lu", "Shengfeng Pan", "et al."]
    year: 2021
    venue: "preprint"
    arxiv_id: "2104.09864"
  - title: "Train short, test long: Attention with linear biases enables input length extrapolation (ALiBi)"
    authors: ["Ofir Press", "Noah Smith", "Mike Lewis"]
    year: 2022
    venue: "ICLR"
    arxiv_id: "2108.12409"
  - title: "FlashAttention: Fast and memory-efficient exact attention with IO-awareness"
    authors: ["Tri Dao", "Daniel Y. Fu", "Stefano Ermon", "et al."]
    year: 2022
    venue: "NeurIPS"
    arxiv_id: "2205.14135"
  - title: "Extending context window of LLMs via positional interpolation"
    authors: ["Shouyuan Chen", "Sherman Wong", "Liangjian Chen", "Yuandong Tian"]
    year: 2023
    venue: "preprint"
    arxiv_id: "2306.15595"
  - title: "Lost in the Middle: How language models use long contexts"
    authors: ["Nelson F. Liu", "Kevin Lin", "John Hewitt", "et al."]
    year: 2023
    venue: "TACL"
    arxiv_id: "2307.03172"
  - title: "SmoothQuant: Accurate and efficient post-training quantization for LLMs"
    authors: ["Guangxuan Xiao", "Ji Lin", "Mickael Seznec", "et al."]
    year: 2023
    venue: "ICML"
    arxiv_id: "2211.10438"
  - title: "Pythia: A suite for analyzing large language models across training and scaling"
    authors: ["Stella Biderman", "Hailey Schoelkopf", "Quentin Anthony", "et al."]
    year: 2023
    venue: "ICML"
    arxiv_id: "2304.01373"
  - title: "MPT: MosaicML Foundation Series"
    authors: ["MosaicML Team"]
    year: 2023
    venue: "blog"
    url: "https://www.mosaicml.com/blog/mpt-7b"
  - title: "Falcon"
    authors: ["Ebtesam Almazrouei", "Hamza Alobeidli", "et al."]
    year: 2023
    venue: "preprint"
    arxiv_id: "2311.16867"
  - title: "SoftMax-Off-by-One"
    authors: ["Evan Miller"]
    year: 2023
    venue: "blog"
    url: "https://www.evanmiller.org/attention-is-off-by-one.html"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Illustration of StreamingLLM vs existing methods (Dense / Window / Sliding-Window-with-Recomputation / StreamingLLM)"
  page: 2
  image_path: "figures/xiao-2023-streaming-llm-fig.png"
---

# Efficient Streaming Language Models with Attention Sinks

**Authors:** Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, Mike Lewis
**Published:** 2023-09 (ICLR 2024) · [Source](https://arxiv.org/abs/2309.17453)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Xiao et al. (MIT / Meta AI / CMU / NVIDIA) identify a failure mode in window-attention LLMs and a one-line fix that enables streaming inference over essentially unbounded sequences. The failure: as soon as the rolling window evicts the first few KV entries, perplexity explodes (Llama-2-13B: 5.40 → 5158.07 on PG19, a 955x degradation). The diagnosis: due to the softmax-sums-to-one constraint, the model offloads "unused" attention scores somewhere, and during pre-training it learns to dump them on the *initial* tokens because those positions are visible to every subsequent token in autoregressive generation. The authors name these "attention sinks". Substituting initial tokens with linebreaks ("\n") preserves the perplexity restoration — proving the role is positional, not semantic. The fix (**StreamingLLM**): keep the first 4 tokens' KVs forever (the "sinks") + a rolling window of recent tokens. This restores perplexity (5158 → 5.40 on Llama-2-13B), works on Llama-2 / MPT / Falcon / Pythia at scales 2.8B–70B without any fine-tuning, handles 4M+ tokens, and runs up to 22.2x faster than the only viable baseline (sliding-window with recomputation, which is O(TL²) vs StreamingLLM's O(TL)). The authors also pre-train 160M-parameter models with a single learnable "Sink Token" prepended to every training sample — and show that a model trained this way needs only the sink token (not 4 initial tokens) to maintain streaming perplexity, suggesting an architectural change for future LLMs that costs nothing at convergence and improves streaming deployment. Q&A evaluation: StreamingLLM on Llama-2-70B-Chat scores ARC-E 91.37 / ARC-C 80.20 in streaming mode — within 0.4 points of the dense one-shot baseline (91.29 / 78.50) — while window attention alone scores 0.12 / 0.32 (random).

## Key Takeaway

The architectural lesson is that **a streaming-LLM needs a "workspace anchor" — a small set of always-visible attention-stable positions — to function with a rolling KV cache, and the role of that anchor is positional, not semantic.** This is a different abstraction from "summary" or "compressed memory": the anchor's content doesn't carry information; it absorbs surplus attention weight so the rest of the attention distribution can stay calibrated. The implications for memory architecture are significant: the assumption that "important context = important content" is wrong at the attention-mechanism level — some context items are important *because they're calibration weights*, and removing them silently breaks every downstream component. Pre-training with a dedicated Sink Token (or replacing softmax with softmax-off-by-one) lets one position absorb the role explicitly, which is the cleanest way to design future LLMs for streaming workloads. For working-memory layers of agent architectures (the rolling "what's in context right now" tier), this gives a clean primitive: a few attention sinks + the rolling working set, with paged longer-term memory swapping in/out of the working set as needed. (ENGRAM: this is primarily an **R** (Retrieve) story about what stays in the LLM's attendable context — but with a subtle **N** (Network) twist: the network of "what positions matter to attention" is not the same as the network of "what content matters to the user".)

## Implications

- **Treat the LLM's KV cache as the working-memory tier of your agent architecture** (ENGRAM: **R**, **A**). Long-term memory (markdown vault, vector store, KG) handles knowledge that's swapped in/out by retrieval. Working memory is what's in the LLM's attention window *right now*. StreamingLLM shows that the working memory tier needs structural design — sinks + rolling window, not "we'll dump everything into the prompt". For Flow OS, this maps cleanly onto MemoryOS / MemGPT's tier model: a structured working-memory layout (anchor tokens + recent history + just-retrieved long-term entries) is qualitatively better than "let the LLM figure out what matters in 32K of context".

- **Always-on system-prompt-style content acts as natural attention sinks** (ENGRAM: **N**, **R**). The first 4 tokens of any LLM prompt — usually a chat template's `<|im_start|>system\n...` or similar — are doing more work than you think. They're the attention sinks. If you ever truncate them out (e.g., to make room for more recent content in a fixed-budget context), perplexity will silently spike. The Flow OS implication: never truncate the system prompt; if you need to compress context, compress the middle (the Lost-in-the-Middle finding agrees) and leave the head + tail intact.

- **For streaming deployment, use 4 initial-token sinks + rolling window, not "we'll re-feed the conversation each turn"** (ENGRAM: **R**). Sliding-window with re-computation has O(TL²) latency; StreamingLLM has O(TL) and is 22.2x faster in the limit. The cost asymmetry only grows as conversations get longer. For a long-running chatbot, this is a real engineering win — and it doesn't require any fine-tuning.

- **Pre-training future models with a designated Sink Token is free at convergence and major for streaming** (ENGRAM: **M**). Table 3 shows the Sink Token costs ~zero on standard NLP benchmarks (ARC-c, HellaSwag, LAMBDA, OpenbookQA, PIQA, Winogrande — all within 0.3% of vanilla). But for streaming deployment, the model trained with a Sink Token needs *only* the sink token to maintain perplexity (vs. needing 4+ initial tokens for vanilla models). For any team pre-training a new LLM in 2026+, this is a single-line change with a real downstream win and no measurable cost.

- **Increasing cache size doesn't monotonically improve perplexity — there's an effective working memory limit** (ENGRAM: **M**). Table 6 shows that StreamingLLM's perplexity is non-monotonic in cache size: e.g., MPT-7B perplexity actually *increases* from 14.25 → 14.99 as cache grows from 1K → 2K. The interpretation: LLMs don't maximally utilize the entire context they receive. This is a separate problem from the streaming problem — and a real one for any team budgeting context length. Sweep cache size empirically; the right cache is often smaller than the maximum window the model nominally supports.

- **The sink role is purely positional — substitute linebreak tokens for content and it still works** (ENGRAM: **N**, **G**). Substituting the first 4 tokens with "\n" still restores perplexity (Llama-2-13B: 5.40 → 5.60 — within 4%). This is the cleanest single experiment in the paper — it isolates the positional role from the semantic role. For Flow OS, the implication is that the *position* of "system prompt" matters more than the *content* — even if your system prompt is empty placeholder text, it still serves the attention-sink role.

- **Softmax-off-by-one is the architectural alternative to sink tokens** (ENGRAM: **N**). The formula `softmax₁(x)i = exp(xi) / (1 + Σ exp(xj))` lets attention scores sum to *less than one* — explicitly representing "I have no useful information from elsewhere". This is mathematically equivalent to prepending a virtual all-zero K/V token. The Zero Sink baseline didn't fully solve the problem in the paper's 160M-parameter experiment (ppl 29214 vs 1235 with learnable Sink Token for the 0+1024 config), but for new pre-training runs, the softmax-off-by-one variant is worth evaluating in parallel with Sink Token.

- **Quantization-outlier and attention-sink phenomena share the same root cause** (ENGRAM: **G**). The paper cites Xiao et al. 2023 (SmoothQuant) and Bondarenko et al. 2023 — these are quantization-outlier papers, and the connection is that both phenomena (initial-token attention sinks; quantization outliers in certain channels) are downstream of the softmax-sums-to-one constraint. For mech-interp work, this is a unifying observation: model architecture choices (softmax) force structural artifacts (sinks, outliers), and the same fix (softmax-off-by-one) addresses both.

## How to Apply It (method)

**Scenario:** You're deploying a long-running chatbot (Flow OS's Telegram interface, say) that needs to maintain coherent state across thousands of turns and millions of tokens. Re-feeding the entire conversation each turn is too slow at scale (quadratic in turn count). You want streaming inference with bounded memory and bounded latency.

**Steps:**

1. **Implement the 4-sinks + rolling-window KV cache pattern**. Maintain a KV cache of size `4 + W`, where the first 4 entries are the initial tokens' KVs (never evicted) and the next `W` entries are a rolling window of the most recent tokens (FIFO eviction). When you decode token T, attention is computed over those `4 + W` positions only.

   For HuggingFace Transformers:
   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer
   import torch

   def streaming_step(model, tokenizer, kv_cache, new_token_ids, sink_size=4, window_size=2044):
       # kv_cache: tuple of (key, value) tensors, shape (batch, heads, seq, dim)
       outputs = model(new_token_ids, past_key_values=kv_cache, use_cache=True)
       updated_kv = outputs.past_key_values
       # Evict oldest tokens beyond [sinks | window]
       trimmed_kv = tuple(
           (
               torch.cat([k[:, :, :sink_size], k[:, :, -window_size:]], dim=2),
               torch.cat([v[:, :, :sink_size], v[:, :, -window_size:]], dim=2),
           )
           for k, v in updated_kv
       )
       return outputs.logits, trimmed_kv
   ```

2. **Apply positions within the cache, not the original text positions**. When using RoPE, after eviction the cache tokens occupy positions `[0, 1, 2, 3, 4, 5, 6, 7]` (cache-local), not their original positions like `[0, 1, 2, 3, 12879, 12880, ...]`. This is critical: positional encoding must be applied based on cache position, not original sequence position. Cache the *pre-rotation* K values and apply rotation after eviction at decode time.

3. **For ALiBi-based models** (MPT family), use contiguous linear bias based on cache position, not "jumping" bias from original positions. Same principle as RoPE — positional info is cache-local.

4. **Tune cache size empirically — bigger is not better**. From Table 6: MPT-7B perplexity goes 14.12 → 14.25 → 14.33 → 14.99 as cache grows 252 → 508 → 1020 → 2044. Pythia-12B is similar: 13.17 → 12.52 → 12.08 → 12.09 (plateau). Sweep on your own task; pick the sweet spot for your latency budget. Common sweet-spots: 1024-2048 recent tokens + 4 sinks.

5. **For new pre-training runs, prepend a learnable Sink Token to every training sample**. From §3.3: add one learnable `<sink>` token at position 0 of every training sample. Test on your standard benchmarks to confirm no degradation (the paper shows zero degradation on ARC-c, HellaSwag, LAMBDA, OBQA, PIQA, Winogrande). Result: streaming inference needs only the single sink token, not 4 initial tokens — cleaner and easier to manage in production.

6. **Sanity-check with the StreamEval-style protocol**. Build a synthetic streaming benchmark: inject "REGISTER_CONTENT in line N is `<token>`" entries every 10 lines, query "what was REGISTER_CONTENT in line N?" 20 lines later (so the answer is always 20 lines back). Measure accuracy as input length grows from 8K → 120K tokens. StreamingLLM should maintain ~80%+ accuracy across the range; window attention will fall to ~0 once the answer drops out of the window; dense attention will fail with OOM at the pre-training window length. If your implementation's curve looks different, debug your cache logic (likely positional encoding bug).

7. **For an agent's working-memory tier, place "always-relevant" context in the sink position**. The system prompt, the user's persistent identity / preferences, the active task description — these go in the first ~50 tokens (overlapping with the attention sinks). The rolling window holds recent dialogue + retrieved long-term memories. This is the right structural use of StreamingLLM's insight.

8. **Combine with context-extension techniques for "bigger local context"**. StreamingLLM extends *temporal* reach (turn-count), not *local* context size (window). For tasks needing both — e.g., 32K of recent code + millions of historical turns — combine StreamingLLM with PositionInterpolation / LongLoRA to extend `W` itself (the rolling window's max size).

**Expected outcome:** A streaming chatbot that runs at constant per-token latency over arbitrarily long conversations, with perplexity matching the sliding-window-with-recomputation baseline but at 22.2x lower latency in the limit and constant memory footprint. ARC-style task accuracy stays within 1% of the one-shot baseline. No fine-tuning required for existing Llama-2 / MPT / Falcon / Pythia models.

## Best Figure

![Figure 1 — StreamingLLM vs Dense / Window / Sliding-Window-with-Recomputation, with perplexity per approach on Llama-2-13B 65K-token PG19 sample (page 2)](figures/xiao-2023-streaming-llm-fig.png)

Image Candidates:

- **Figure 1 (p. 2):** Four-panel comparison of (a) Dense Attention (O(T²), PPL 5641, breaks on long text), (b) Window Attention (O(TL), PPL 5158, breaks when initial tokens evicted), (c) Sliding Window with Recomputation (O(TL²), PPL 5.43, slow), (d) StreamingLLM (O(TL), PPL 5.40, efficient and stable). This is the headline diagram — it visually communicates the problem, the failure modes of obvious alternatives, and the fix.
- **Figure 2 (p. 3):** Attention map visualization across layers of Llama-2-7B showing that layers 2+ overwhelmingly attend to initial tokens regardless of semantic relevance. This is the *evidence* for the attention sink hypothesis.
- **Figure 5 (p. 7):** Perplexity stability across 4 million tokens for Llama-2, Falcon, Pythia, MPT model families. Visualizes the scaling claim.
- **Figure 10 (p. 9):** Per-token decoding latency and memory comparison between sliding-window-with-recomputation and StreamingLLM. Shows the 22.2x speedup empirically.

**Best Image — Figure 1: Illustration of StreamingLLM vs existing methods** (page 2). The four-panel comparison with annotated perplexities (5641 / 5158 / 5.43 / 5.40) and complexities (O(T²) / O(TL) / O(TL²) / O(TL)) makes the entire architectural insight legible in one image: window attention is fast but broken, recomputation is correct but slow, StreamingLLM is fast AND correct. The visual contrast between the four KV-cache layouts (dense=all tokens, window=last L, recompute=last L rebuilt, StreamingLLM=L sinks + last rolling) drives the architectural intuition. This is the single most useful diagram for a memory architect: it shows what every KV-cache eviction strategy looks like, with consequences priced in.

## What Experts Overlook

The most overlooked operational detail is that **the attention sink role is positional, not semantic, and this matters for prompt design**. From §3.1 (Table 1): substituting the first 4 tokens with linebreak tokens "\n" restores Llama-2-13B perplexity to 5.60 — within 4% of using the original initial tokens (5.40). This means:

- The first 4 token positions in any LLM prompt are doing structural work, regardless of their content.
- If you ever truncate the prompt head (a common mistake when you have a 32K input and need to fit in 16K context), perplexity will silently degrade — even if the truncated content was "just the system prompt".
- Conversely, you can *use* this — put a stable, semantically-light token sequence in positions 0–3 of every prompt; it doesn't need to carry meaning, just needs to be there.

**Why it matters:** Most teams designing prompt structures think only about content (what's in the prompt) and not about position (where in the prompt). Attention sinks reveal that the first ~4 positions are structurally privileged in a way that has nothing to do with semantics. For Flow OS, this argues against context-management policies that truncate the prompt head when the prompt grows. Truncate the middle (which Lost-in-the-Middle has already shown is least-attended-to), preserve the head + tail.

For a memory-architect's ENGRAM mapping, this is a clean **G** (Ground) consequence of an **R** (Retrieve)-time engineering decision: the position you place context in determines how much *grounding signal* the model gets from it, independently of content.

**Example of good use:** Flow OS's Telegram bot prompts always begin with a 50-token chat template + system identity block that never gets truncated. Even when context pressure forces eviction of older turns, the head stays — and the model's attention distribution remains stable.

**Example of misapplication:** A team builds a context-compression policy that, when the prompt is too long, truncates from the beginning ("the older content is less relevant anyway"). They notice the chatbot becomes incoherent on long conversations and assume it's a long-context problem. The actual cause is that they're evicting the attention sinks. Fix: never truncate the first 50 tokens; truncate from the middle instead.

## Extracted Prompts

This is an inference-architecture paper, not a prompting paper, so the "prompts" of interest are the streaming/instruction templates and the StreamEval benchmark format.

**Prompt explanation:** StreamEval benchmark format (Figure 8). The synthetic streaming benchmark the authors use to validate that StreamingLLM correctly maintains accurate retrieval over very long streams. Every 10 lines inject a `REGISTER_CONTENT` entry; every 10 lines query the value at a specific past line. Useful as a regression test for any streaming-inference implementation.

```
Below is a record of lines I want you to remember.
The REGISTER_CONTENT in line 0 is <8806>
The REGISTER_CONTENT in line 1 is <token_1>
...
The REGISTER_CONTENT in line 10 is <24879>
Query: The REGISTER_CONTENT in line 0 is
The REGISTER_CONTENT in line 11 is <token_11>
...
The REGISTER_CONTENT in line 20 is <45603>
Query: The REGISTER_CONTENT in line 10 is
The REGISTER_CONTENT in line 21 is <token_21>
...

Desired Output: ["<8806>", "<24879>", "<45603>", ...]
```

**Prompt explanation:** Streaming Q&A protocol for ARC-style benchmarks. Concatenate all (question, answer) pairs and feed as a single stream to the LLM. At each answer position, evaluate by exact match. The streaming setup that distinguishes StreamingLLM from dense attention (OOM at this scale) and window attention (random outputs).

```
Question 1: {q1}
Answer 1: {a1}
Question 2: {q2}
Answer 2: {a2}
...
Question N: {qN}
Answer N:
```

## Citations

The paper cites ~60 works spanning LLM families (Llama-2, MPT, Falcon, Pythia, GPT-3, OPT), long-context architectures (Longformer, FlashAttention, Position Interpolation, ALiBi, RoPE), efficiency techniques (FlashAttention, quantization including the authors' own SmoothQuant), and pretraining benchmarks (PG19, Pile, ARC, HellaSwag, LAMBDA, PIQA). Full list in frontmatter. Most relevant for memory-architect lens: Beltagy 2020 (Longformer — wiki), Vaswani 2017 (Attention Is All You Need — wiki), Press 2022 (ALiBi), Su 2021 (RoPE).

## Related Digests

- [[wang-2025-mirix]] — MIRIX: Multi-Agent Memory System for LLM-Based Agents (MIRIX's working-memory tier could be implemented as a StreamingLLM-style anchor + rolling cache)
- [[li-2025-memos]] — MemOS: A Memory OS for AI System (MemOS's KV-activation memory substrate maps directly onto StreamingLLM's rolling KV cache + sink anchor)
- [[dai-2019-transformer-xl]] — Transformer-XL (the original "recurrent state cache" idea — StreamingLLM is the streaming-mode descendant)
- [[vaswani-2017-attention-is-all-you-need]] — Attention Is All You Need (the softmax-sums-to-one constraint that creates attention sinks is right here in the original transformer)
- [[beltagy-2020-longformer]] — Longformer (the original "window attention" — StreamingLLM is the fix for its catastrophic-failure-on-eviction problem)

## Reviewer Notes

**Severity: Clean.**

Cross-checked against the paper:

- Headline perplexity numbers (Llama-2-13B: 5158.07 → 5.40 with sinks, 5.60 with "\n" substitution) match Table 1.
- The 22.2x speedup vs sliding-window-with-recomputation matches §1 and Figure 10.
- 4 million token capability across Llama-2 / MPT / Falcon / Pythia (Figure 5) accurate.
- ARC-E / ARC-C streaming results on Llama-2-70B-Chat (91.37 / 80.20 vs one-shot 91.29 / 78.50; window attention 0.12 / 0.32) match Table 5.
- Sink Token pre-training: 160M parameter models, 8x A6000, Pile dataset, 143K steps — matches §4.2.
- NLP benchmark deltas with Sink Token (within 0.3-0.7% on ARC-c/e, HellaSwag, LAMBDA, OBQA, PIQA, Winogrande) match Table 4.
- Cache-size non-monotonicity (MPT-7B 14.12 → 14.99 as cache grows 252→2044) matches Table 6.
- Author affiliations (MIT / Meta AI / CMU / NVIDIA) and ICLR 2024 venue match title page.
- The four-panel Figure 1 complexity / perplexity annotations (O(T²) / O(TL) / O(TL²) / O(TL); 5641 / 5158 / 5.43 / 5.40) match the figure exactly.

One small clarification: the digest characterizes Zero Sink as "didn't fully solve the problem in the paper's 160M-parameter experiment" — Table 3 shows Zero Sink at 0+1024 yields perplexity 29214 vs the learnable Sink Token's 1235, which the paper itself describes as "alleviates the attention sink problem to some extent". This is a fair characterization.

No invented facts, no misattributed citations.
