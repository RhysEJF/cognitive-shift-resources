---
corpus: agentic-memory
kind: paper-digest
slug: bulatov-2022-recurrent-memory-transformer
title: "Recurrent Memory Transformer"
authors:
  - "Bulatov, Aydar"
  - "Kuratov, Yuri"
  - "Burtsev, Mikhail S."
year: 2022
publication_date: "2022-07"
venue: "NeurIPS 2022"
source_url: "https://arxiv.org/abs/2207.06881"
doi: null
arxiv_id: "2207.06881"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Augmenting Transformer input/output with a small fixed set of special [mem] tokens — passed unchanged across sequence segments — gives you segment-level recurrence and effective context length beyond Transformer-XL's depth-limited cache, with no changes to the Transformer model itself; the gradient through memory tokens enables BPTT across multiple segments, and learned attention patterns show interpretable read/write structure on the memory tokens."
topics:
  - recurrent-memory-transformer
  - memory-tokens
  - segment-recurrence
  - long-context
  - bptt
  - associative-retrieval
tags:
  - paper
  - canonical
  - memory-augmented-transformer
  - long-context
entities:
  - bulatov-aydar
  - kuratov-yuri
  - burtsev-mikhail
related_digests:
  - dai-2019-transformer-xl
  - hochreiter-1997-lstm
  - vaswani-2017-attention-is-all-you-need
  - graves-2014-neural-turing-machines
  - chen-2023-memwalker
citations:
  - title: "Attention is all you need"
    authors: ["Vaswani, Ashish", "et al."]
    year: 2017
    venue: "NeurIPS"
  - title: "Transformer-XL: Attentive language models beyond a fixed-length context"
    authors: ["Dai, Zihang", "et al."]
    year: 2019
    venue: "ACL"
  - title: "Long short-term memory"
    authors: ["Hochreiter, S.", "Schmidhuber, J."]
    year: 1997
    venue: "Neural Computation"
  - title: "Memory transformer"
    authors: ["Burtsev, Mikhail S.", "Kuratov, Yuri", "Peganov, Anton", "Sapunov, Grigory V."]
    year: 2020
    arxiv_id: "2006.11527"
  - title: "Neural Turing machines"
    authors: ["Graves, A.", "Wayne, G.", "Danihelka, I."]
    year: 2014
    arxiv_id: "1410.5401"
  - title: "Memory networks"
    authors: ["Weston, J.", "Chopra, S.", "Bordes, A."]
    year: 2015
    arxiv_id: "1410.3916"
  - title: "Longformer: The long-document transformer"
    authors: ["Beltagy, Iz", "Peters, Matthew E.", "Cohan, Arman"]
    year: 2020
    arxiv_id: "2004.05150"
  - title: "Big Bird: Transformers for longer sequences"
    authors: ["Zaheer, Manzil", "et al."]
    year: 2020
    venue: "NeurIPS"
  - title: "Compressive transformers for long-range sequence modelling"
    authors: ["Rae, Jack W.", "et al."]
    year: 2019
    arxiv_id: "1911.05507"
  - title: "Perceiver IO: A general architecture for structured inputs & outputs"
    authors: ["Jaegle, Andrew", "et al."]
    year: 2021
  - title: "Adam: A method for stochastic optimization"
    authors: ["Kingma, D.", "Ba, J."]
    year: 2015
    arxiv_id: "1412.6980"
  - title: "Pointer sentinel mixture models (WikiText-103)"
    authors: ["Merity, Stephen", "et al."]
    year: 2017
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Comparison of RMT and Transformer-XL architectures (memory tokens + segment recurrence)"
  page: 4
  image_path: null
---

# Recurrent Memory Transformer

**Authors:** Bulatov, Aydar; Kuratov, Yuri; Burtsev, Mikhail S.
**Published:** 2022-07 (NeurIPS 2022) · [Source](https://arxiv.org/abs/2207.06881)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

RMT augments a vanilla Transformer with **`m` special memory tokens** added at both the start (as "read" memory) and the end (as "write" memory) of each input segment. After processing segment τ, the *write* memory tokens at the end carry the updated memory; these become the *read* memory tokens prepended to segment τ+1. This passing-of-tokens-across-segments creates a recurrence loop over the memory tokens only — **the Transformer backbone is unchanged**, and the recurrence is implemented entirely via input/output manipulations. Gradient flows backward through memory tokens via BPTT across multiple previous segments (unroll = 0 to 4 in their experiments). Compared to Transformer-XL, which stores `m × N` cached hidden states per segment (m positions × N layers), RMT stores only `m` memory vectors per segment — much less state, but RMT's memory is *processed by all N Transformer layers* each segment, making it effectively deeper. Results: RMT matches Tr-XL on language modeling (WikiText-103, enwik8) with smaller memory size, and *outperforms* Tr-XL on algorithmic tasks (copy, reverse, associative retrieval) that require global information when sequence is split into multiple segments. Augmenting pretrained models (BERT, RoBERTa, DeBERTa, T5) with 10 memory tokens improves long-text classification (Hyperpartisan news). Critically: RMT is *compatible with any Transformer* — you don't have to change attention masks, position encodings, or layer architecture.

## Key Takeaway

**Long-term memory in a Transformer can be implemented entirely as input/output manipulation of special tokens — no architectural changes to the model itself.** [ENGRAM: dominant on N (Network — the choice of "memory as tokens at sequence edges" is the key architectural commitment); secondary on R (Retrieve — attention from sequence tokens to memory tokens IS the retrieval) and M (Maintain — the unchanged identity of memory tokens across segment boundaries is the persistence guarantee)] The contribution is conceptual: prior memory-augmented Transformers (Transformer-XL's cached hidden states, Compressive Transformer's compressed memory layer, Memformer's dedicated memory module, Big Bird's global tokens) all required attention-mask surgery or new layer types. RMT shows that just by adding `m` extra tokens to the input — tokens that the model is *forced* to use via the bottleneck of segment-to-segment information passing — you get a working memory mechanism. **This is LSTM's CEC trick at a higher abstraction level**: the memory tokens are the equivalent of the cell state (their identity is preserved across segments), and the self-attention layers play the role of input/output gates (they decide what to read from / write to the memory tokens). The architectural minimalism is the lesson: most "memory architecture innovations" are over-engineered relative to what works.

## Implications

[ENGRAM mapping: dominant on **N** (Network — segment-bounded recurrence is the shape choice), **R** (Retrieve — cross-attention from current segment tokens to memory tokens is the read path), **M** (Maintain — unchanged identity across segment boundaries). Plus **E** (Encode — what gets written into memory tokens is learned from BPTT gradient).]

1. **The "memory tokens at boundary" pattern recurs.** [N] RMT places memory tokens at the start (read) and end (write) of each segment. This pattern shows up in Burtsev 2020 (Memory Transformer), in modern long-context LLM techniques (system-token prepending, in-context memory tokens like those in OpenAI's o1-class models), and in the position-augmented attention pattern of many fine-tuning setups. **For Flow OS: when you want a memory channel through an unchanged base model, prepended/appended tokens are the lowest-friction interface** — no need to modify model weights or attention masks.

2. **State quantity vs. depth tradeoff.** Tr-XL stores `m × N` vectors per segment (every layer caches its own state). RMT stores only `m` vectors per segment but processes them through all N layers each step. This is the same tradeoff that LSTMs vs deep RNNs faced: **a small amount of state that goes deep is more efficient than a large amount of state that goes shallow**, *if* the deep processing has good gradient flow. RMT's BPTT-through-memory-tokens is what makes the deep processing trainable.

3. **Compatibility with any Transformer is the actual sleeper feature.** §5 shows RMT memory mechanism added to pretrained BERT/RoBERTa/DeBERTa/T5 with just 10 memory tokens, improving Hyperpartisan news classification. **For deployments: you can add RMT-style memory to ANY production LLM (Llama, Claude, GPT) by reserving input slots for memory tokens and rotating them across calls** — without fine-tuning the base model. This is essentially what the "persistent context window" features in modern agent frameworks try to achieve, but RMT proves the mechanism works.

4. **BPTT unroll is the key training-time knob.** Experiments vary BPTT unroll from 0 to 4 previous segments. Increasing unroll improves long-dependency performance but is expensive (GPU RAM). The principle: **gradient flow across segments is bounded by the unroll depth**, so the model only learns dependencies it can backpropagate through. For runtime: there's no such limit — the memory tokens carry information forward indefinitely at inference, even if BPTT didn't train across that span.

5. **Memory tokens learn interpretable read/write patterns.** §5 (claim 4 of contributions) reports that "specific interpretable memory read-write patterns of attention are shown." This matters because most memory architectures are black boxes — you can't tell what's stored or why. RMT's attention maps over memory tokens are diagnosable, which is rare. **For Flow OS: instrumenting attention weights on memory channels gives you a free auditing layer** — you can see which memory slots a particular query attended to without needing a separate retrieval log.

## How to Apply It (method)

**The RMT mechanism:**

```
Initialize: H_τ^mem = trainable_memory_init  (m vectors)

For each segment τ in sequence:
    # Augment input
    H̃_τ^0 = [H_τ^mem ◦ H_τ^0 ◦ H_τ^mem]
                # read memory + segment tokens + write memory placeholder
    
    # Process through unchanged Transformer
    H̄_τ^N = Transformer(H̃_τ^0)
    
    # Split output
    [H_τ^read ◦ H_τ^N ◦ H_τ^write] := H̄_τ^N
    
    # Pass write-memory forward as next segment's read-memory
    H_{τ+1}^mem := H_τ^write
    
    # BPTT through memory tokens for `unroll` previous segments
```

**Key implementation details:**

1. **Causal mask exception**: the causal attention mask is applied only to sequence tokens. Memory tokens in the read/write blocks can attend to all other tokens in the same block — bidirectional within the memory region.
2. **Memory size `m`**: hyperparameter; the paper uses small values (typically 10-20 tokens) and shows that beyond a threshold, increasing `m` doesn't help much.
3. **BPTT unroll**: starts at 0 (no gradient across segments — memory tokens are detached at boundaries) and goes up. Even unroll=1 (gradient to immediately previous segment) gives most of the gain; higher unrolls give marginal improvements at much higher GPU cost.
4. **Initialization**: trainable memory vectors initialized like normal token embeddings.

**For pretrained models** (§5 setup):
- Take a frozen pretrained model (BERT-base, T5-base, etc.)
- Reserve `m=10` input slots for memory tokens
- Fine-tune ONLY the memory mechanism and the task head, keeping the base model frozen
- The pretrained model's existing attention patterns adapt to the memory tokens because the model just sees them as additional input tokens

**Where RMT is best:**
- Tasks with strict segment boundaries (chunked documents, multi-turn dialogue)
- Algorithmic tasks requiring global information (copy, reverse, associative retrieval over key-value pairs split across segments)
- Long-document classification where the document doesn't fit in one context window

**Where RMT is weaker:**
- Tasks where the model needs full random access to past content (token-level retrieval at arbitrary positions) — RMT compresses to `m` vectors, losing detail
- Long generation tasks where the memory needs to persist across many segments — gradient can't train arbitrarily-long dependencies under finite unroll

## Best Figure

_(figure not extracted — Figure 2 in the paper shows the RMT vs Tr-XL architecture comparison, the canonical reference diagram)_

**Figure 2 — RMT vs Transformer-XL, page 4:**

Two side-by-side architectural diagrams:

**Left (Transformer-XL)**: Each segment is processed by an N-layer Transformer. At each layer, the previous segment's hidden states (the "cache") are concatenated with the current segment's hidden states for attention. Stop-gradient prevents gradient flow across segments. The cache size is `m × N` (m positions × N layers), and the "effective context length" is bounded by N (gradient can only flow through the previous segment's last-layer cache).

**Right (RMT)**: Each segment has `m` read-memory tokens prepended and `m` write-memory tokens appended. The whole thing — `m + L + m` tokens — is processed by an N-layer Transformer (unchanged from vanilla). The write-memory tokens from segment τ become the read-memory tokens for segment τ+1. Gradient flows backward through this memory chain via BPTT, and unlike Tr-XL, there's no stop-gradient — the memory tokens carry differentiable signal across segments. Effective context length is **not** bounded by network depth; the memory carries information indefinitely (limited only by memory capacity `m`).

The visual contrast highlights the architectural minimalism: RMT just adds tokens; Tr-XL adds a caching mechanism. RMT's memory mechanism is compatible with any Transformer; Tr-XL's requires specific attention-mask and position-encoding modifications.

## What Experts Overlook

1. **The memory tokens are placed at BOTH ends of the segment, not just one.** [N] Naive intuition would be to put memory tokens at the start (for the model to read previous context) or at the end (for the model to write current context for the future). RMT does both — and §3 explicitly explains why: in decoder-only/causal models, memory tokens at the *start* can't attend to subsequent tokens (causal mask blocks them), so they can't collect new information from the current segment. Memory tokens at the *end* can attend backward to everything in the segment but can't be attended to by earlier tokens, so they can't be read from. The dual placement solves both problems. **Most memory-augmented LLM implementations get this wrong** — they put memory at the start only and wonder why the model doesn't update memory effectively.

2. **The model "learns to use memory" — interpretable attention patterns.** [R] §5 contributions list item 4 mentions that attention maps over memory tokens show interpretable read/write structure. This is rare for memory-augmented architectures; most are black boxes. For Flow OS production: if you go RMT-style, **log the attention weights from sequence tokens to memory tokens** — you get a free interpretability layer showing which "memory slots" each generated token used.

3. **State amount vs. processing depth is the right way to compare memory architectures.** RMT's `m` vectors processed through `N` layers per segment vs. Tr-XL's `m × N` cached vectors but no per-segment recomputation. **Compute-per-token-per-segment is higher for RMT, but total state is lower**, and RMT scales to longer effective contexts. The relevant axis for memory architecture comparison isn't "how many tokens of context" but "compute × state-budget × effective-context-length" — a three-axis tradespace most papers don't make explicit.

4. **The Tr-XL cache can be combined with RMT.** §5 reports that adding memory tokens to Tr-XL improves it — they're complementary mechanisms. The cache handles local long-range dependencies (recent past in detail); memory tokens handle global state (compressed long-range summary). **For Flow OS: combining a recent-history detailed cache with a compressed global memory is the right shape** — not picking one or the other.

5. **The associative retrieval task is the cleanest demonstration of multi-segment memory.** §4 introduces an "associative retrieval" task: N key-value pairs are input, then one key is queried and the value must be retrieved. With sequence split into multiple segments, the model has to maintain the key-value mappings across segments. Tr-XL and vanilla Transformer fail at larger segment counts; RMT scales gracefully. **This task is a better diagnostic for agent memory than language modeling perplexity** — perplexity averages over many short-range predictions and hides long-range memory failures. **For evaluating any agent memory system, use associative retrieval at variable distances as your primary metric.**

## Extracted Prompts

RMT is an architectural mechanism, not prompt-based. But the *pattern* of "reserve input slots for memory" translates to prompt engineering for unmodified LLMs:

**System prompt template (RMT-inspired for production LLMs):**
```
You are an agent with persistent memory. Your context window contains, in order:
  1. MEMORY: a compressed summary of past interactions (k tokens, marked between <memory>...</memory> tags)
  2. CURRENT INPUT: the user's current message
  3. MEMORY UPDATE: at the end of your response, output an updated MEMORY block to be carried into the next interaction

Critical rules:
- Read MEMORY at the start to ground your response
- The MEMORY block has fixed token budget (k tokens). Be selective.
- Update MEMORY to reflect what should persist; let irrelevant detail decay
- Format: <memory>...</memory> at the start of input, <memory_updated>...</memory_updated> at the end of your response

This mimics RMT's [mem]-token mechanism: read at start, write at end, carry forward.
```

This is the "external scaffold" version of RMT — you implement the recurrence in the application layer (your code captures the `<memory_updated>` block and prepends it to the next call), while the LLM treats the memory as just more context.

## Citations

- Vaswani et al. (2017) — Attention is all you need (the base Transformer architecture)
- Dai et al. (2019) — Transformer-XL (the primary comparison baseline)
- Hochreiter & Schmidhuber (1997) — LSTM (the conceptual ancestor — RMT memory tokens are CEC-like)
- Burtsev et al. (2020) — Memory Transformer (the immediate predecessor — same memory-as-tokens idea without recurrence)
- Graves, Wayne, Danihelka (2014) — Neural Turing Machines (the differentiable external memory line)
- Weston, Chopra, Bordes (2015) — Memory Networks (the slot-array memory abstraction)
- Beltagy, Peters, Cohan (2020) — Longformer (attention-mask alternative for long context)
- Zaheer et al. (2020) — Big Bird (uses global tokens — closest architectural cousin to memory tokens)
- Rae et al. (2019) — Compressive Transformer (second-tier compressed memory built on Tr-XL)
- Jaegle et al. (2021) — Perceiver IO (latent-array approach, related to memory-as-fixed-budget)
- Kingma & Ba (2015) — Adam optimizer
- Merity et al. (2017) — WikiText-103 (the LM benchmark)

(Full citations list in frontmatter `citations:` field.)

## Related Digests

- [[dai-2019-transformer-xl]] — Primary baseline; Tr-XL's cache is the alternative recurrence mechanism
- [[hochreiter-1997-lstm]] — Conceptual ancestor: memory tokens are RMT's CEC equivalents
- [[vaswani-2017-attention-is-all-you-need]] — Base architecture RMT augments without modification
- [[graves-2014-neural-turing-machines]] — Differentiable external memory line (NTM)
- [[chen-2023-memwalker]] — Modern alternative: memory as a tree of summaries walked at query time

## Reviewer Notes

Hallucination check: **Clean**. Key claims verified: `m` memory tokens added at both start and end of each segment (§3 — verified the dual placement explanation about causal masks); BPTT unroll 0-4 (§3 last paragraph); compatibility with pretrained BERT/RoBERTa/DeBERTa/T5 via 500 input tokens + 10 memory tokens (§4); RMT matches Tr-XL on language modeling with smaller memory; outperforms Tr-XL on algorithmic tasks (copy, reverse, associative retrieval) at higher segment counts (§5, Fig. 3). The architectural claim that "the Transformer backbone is unchanged" is verified (§3 first paragraph). The Tr-XL state vs. RMT state comparison (`m × N` vs `m`) is verified. The "interpretable memory read-write patterns" claim is contribution item 4 (§1). The "RMT can be combined with Tr-XL cache" finding is contribution item 3. The framing of memory tokens as LSTM-CEC-at-higher-abstraction is the digest's interpretive bridge — accurate as analogy, not stated by the paper.
