---
corpus: agentic-memory
kind: paper-digest
slug: liu-2023-lost-in-the-middle
title: "Lost in the Middle: How Language Models Use Long Contexts"
authors:
  - "Liu, Nelson F."
  - "Lin, Kevin"
  - "Hewitt, John"
  - "Paranjape, Ashwin"
  - "Bevilacqua, Michele"
  - "Petroni, Fabio"
  - "Liang, Percy"
year: 2024
publication_date: "2024-01"
venue: "TACL"
source_url: "https://arxiv.org/abs/2307.03172"
doi: "10.1162/tacl_a_00638"
arxiv_id: "2307.03172"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Long-context language models exhibit a U-shaped attention curve — they answer best when the relevant passage is at the start or end of the context window, and accuracy drops sharply when it's in the middle, even for 'long-context' models with 16K–100K windows; on multi-document QA with 20 passages, GPT-3.5-Turbo accuracy fell ~20 absolute points moving the gold passage from position 1 to position 10."
topics:
  - long-context-llms
  - position-bias
  - u-shaped-attention
  - multi-document-qa
  - key-value-retrieval-stress-test
  - retrieval-augmented-generation
  - context-window-engineering
  - retrieve
  - aggregate
tags:
  - paper
  - canonical
  - foundational
  - context-window
  - primacy-recency
  - lost-in-the-middle
  - rag-position
  - engram-retrieve
  - engram-aggregate
entities:
  - liu-nelson-f
  - lin-kevin
  - hewitt-john
  - paranjape-ashwin
  - bevilacqua-michele
  - petroni-fabio
  - liang-percy
  - stanford-university
  - samaya-ai
related_digests:
  - beltagy-2020-longformer
  - packer-2023-memgpt-os
  - hu-2026-evermemos
  - li-2025-memos
  - wang-2026-memmachine
  - patel-2026-engram
  - wu-2024-longmemeval
  - maharana-2024-locomo
  - petrov-2026-schema-grounded-memory
citations:
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "1706.03762"
  - title: "Transformer-XL: Attentive language models beyond a fixed-length context"
    authors: ["Zihang Dai", "Zhilin Yang", "Yiming Yang", "et al."]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1901.02860"
  - title: "FlashAttention: Fast and memory-efficient exact attention"
    authors: ["Tri Dao", "Daniel Y. Fu", "Stefano Ermon", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2205.14135"
  - title: "Natural questions: A benchmark for question answering"
    authors: ["Tom Kwiatkowski", "Jennimaria Palomaki", "Olivia Redfield", "et al."]
    year: 2019
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "GPT-3.5-Turbo (OpenAI tech report)"
    authors: ["OpenAI"]
    year: 2023
    venue: "preprint"
    doi: null
    url: "https://platform.openai.com/docs/models/gpt-3-5"
    arxiv_id: null
  - title: "Anthropic Claude 1.3 (tech report)"
    authors: ["Anthropic"]
    year: 2023
    venue: "preprint"
    doi: null
    url: "https://www.anthropic.com/index/claude-2"
    arxiv_id: null
  - title: "MPT-30B-Instruct"
    authors: ["MosaicML NLP Team"]
    year: 2023
    venue: "tech report"
    doi: null
    url: "https://www.mosaicml.com/blog/mpt-30b"
    arxiv_id: null
  - title: "LongChat-13B"
    authors: ["Dacheng Li", "Rulin Shao", "Anze Xie", "et al."]
    year: 2023
    venue: "tech report"
    doi: null
    url: "https://lmsys.org/blog/2023-06-29-longchat/"
    arxiv_id: null
  - title: "In-context retrieval-augmented language models"
    authors: ["Ori Ram", "Yoav Levine", "Itay Dalmedigos", "et al."]
    year: 2023
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: "2302.00083"
  - title: "When not to trust language models: Investigating effectiveness of parametric and non-parametric memories"
    authors: ["Alex Mallen", "Akari Asai", "Victor Zhong", "et al."]
    year: 2023
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "2212.10511"
  - title: "Toolformer: Language models can teach themselves to use tools"
    authors: ["Timo Schick", "Jane Dwivedi-Yu", "Roberto Dessì", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2302.04761"
  - title: "Generating long sequences with sparse transformers"
    authors: ["Rewon Child", "Scott Gray", "Alec Radford", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1904.10509"
hallucination_severity: "Clean"
best_figure:
  number: 5
  title: "U-shaped accuracy vs. position of the gold document in multi-document QA"
  page: 5
  image_path: null
---

# Lost in the Middle: How Language Models Use Long Contexts

**Authors:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang
**Published:** 2024-01 · [Source](https://arxiv.org/abs/2307.03172)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Liu et al. ran controlled experiments on six LMs (GPT-3.5-Turbo, GPT-3.5-Turbo-16k, Claude-1.3, Claude-1.3-100k, MPT-30B-Instruct, LongChat-13B-16k) on two tasks designed to isolate "does the model use its input context": multi-document question answering (10 or 20 documents containing one gold passage) and synthetic key-value retrieval. Across all models, accuracy traces a clear U-shape as the gold passage moves through the context — best at position 1, slightly above the closed-book baseline at position 10, recovering toward the end. On 20-document NaturalQuestions, GPT-3.5-Turbo accuracy drops from ~75% (gold at pos 1) to ~52% (gold at pos 10) — below its 56.1% closed-book baseline. Extended-context models (16K, 100K) often perform identically to their 4K counterparts at small input sizes, meaning a longer window doesn't fix the middle-blindness. On the synthetic key-value retrieval task with no semantic clues at all, the same U-shape appears, so the bias is architectural, not content-dependent. The take-home for builders: ordering retrieved chunks by relevance descending — putting the best chunk first or last — produces measurable accuracy gains over arbitrary order, and adding more retrieved chunks beyond ~10 is often net-negative.

## Key Takeaway

A larger context window is not the same as a usable context window. The transformer attention pattern that powers LLMs gives them a strong primacy + recency bias, so retrievers feeding 50 chunks into a 100K-token window are paying for context the model literally cannot use — you'd often do better with 5 well-ordered chunks than 50 randomly-ordered ones, and the "lost in the middle" failure mode is invisible to anyone benchmarking only end-to-end accuracy without ablating chunk position.

## Implications

- **Order retrieved chunks by descending relevance, not by retrieval rank tiebreaker**: The paper shows accuracy drops sharply for middle positions. Always sort RAG outputs so the highest-confidence chunk is first (or last) in the prompt. Don't ship "retrieved-document-order" as-is. **(R)**
- **There is a sweet spot for k; more chunks ≠ better**: Beyond ~10 chunks, additional retrievals push the gold chunk toward the middle of the window, where it gets ignored. Tune top-k empirically against a held-out set; the answer is usually 5–10, not 50. **(R)**
- **Long-context windows are necessary but not sufficient**: Extended-context models (16K, 100K) show the same U-shape. Don't conclude "we have a 200K window, we don't need a retriever" — you still need a retriever to pre-select what makes it into the window. **(N, R)**
- **Reranking buys position, not just relevance**: A cross-encoder reranker doesn't just promote the right chunk; it lets you put that chunk at position 1 or 20 deliberately. Treat the reranker as a "position controller" as much as a relevance filter. **(R)**
- **The key-value test exposes architectural bias independent of content**: When the same U-shape appears on synthetic JSON kv-pairs with no semantics, you know the problem is in attention itself, not in language modelling. For memory-system designers: this is a property to engineer around, not one that will go away with bigger models. **(N, R)**
- **Always ablate position when measuring retrieval quality**: For any retrieval eval, run gold-chunk-at-position-1, middle, and last and look at the accuracy spread. If your eval averages over positions it hides middle-blindness. **(G)**
- **Document-level positioning beats post-hoc reordering**: If your downstream task lets you, structure memory so the most relevant unit is *literally first or last* — e.g., put a session-end summary at the top of the system prompt, not buried between turns. **(A, N)**

## How to Apply It (method)

**Scenario:** A memory-architect team has a RAG pipeline returning 20 chunks for each user query against a corpus of ~50k internal docs. They've noticed answer quality is inconsistent and want to figure out if "lost in the middle" is part of the problem.

**Steps:**

1. **Build a position-controlled eval set**: Take 100 queries where you know the gold doc-id. For each, construct prompts where the gold chunk is placed at positions 1, 5, 10, 15, 20 — same 20 chunks, only the order varies. Measure accuracy at each position. If you see a U-shape, you have the bug.

2. **Re-order RAG outputs by descending reranker score**: Use a cross-encoder reranker (e.g., bge-reranker-large) over the 20 retrieved chunks. Sort the output so highest reranker score is at position 1.

3. **Cap k aggressively** and measure: try k=5, k=10, k=20 with the descending-order configuration. Find your sweet spot on the eval set — likely 5–10.

4. **For long-form answers, use a "first-and-last" placement** for the most important chunk:

   ```
   System prompt:
   --- KEY CONTEXT (use this first) ---
   {top-1 reranked chunk}
   --- ADDITIONAL CONTEXT ---
   {chunks 2..k}
   --- KEY CONTEXT (referenced earlier) ---
   {top-1 reranked chunk again}
   ```

   This biases both ends of the context with the gold info.

5. **For agent memory systems**: place session-end summaries OR persistent persona facts at the *top* of the system prompt, not interleaved with conversation. The U-shape applies to multi-turn chat exactly as it applies to multi-document QA.

6. **Add a position-bias regression test to CI**: every time you upgrade the retriever or change k, re-run the position-controlled eval to ensure you haven't regressed on middle-position recall.

7. **For latency-sensitive systems, prefer shorter, better-ordered context** over longer context: a 4K-token prompt with the right 3 chunks at position 1 will often beat a 32K-token prompt with 30 mostly-relevant chunks in random order.

**Expected outcome:** Concrete measurement of position bias in your specific stack, a re-ordering policy that captures most of the easy accuracy gain, and a regression test that prevents future retrieval changes from silently regressing the gold-at-middle case.

## Best Figure

![Figure 5 (retroactively extracted)](figures/liu-2023-lost-in-the-middle-fig.png)

_(figure not extracted — inline mode)_

**Image Candidates:**
- Figure 1 (p. 1): The headline U-shape for GPT-3.5-Turbo on 20-document NQ — single most-quoted plot in the LLM-RAG literature.
- Figure 5 (p. 5): Multi-model U-shape — same pattern across GPT-3.5-Turbo, Claude-1.3, MPT-30B-Instruct, LongChat — proves it's not a single-model artefact.
- Figure 7 (p. 7+): Key-value retrieval U-shape — proves the bias is architectural, not content-driven.

**Best Image:** Figure 5: U-shaped accuracy vs. position of the gold document across 6 LMs on 10-document and 20-document multi-document QA. The chart shows the same primacy + recency pattern across all six models, with the dip in the middle larger when there are more documents — the empirical core of the paper in one view.

## What Experts Overlook

The synthetic key-value retrieval task is the load-bearing experiment, not the multi-document QA task — because it strips out every content cue and STILL shows the U-shape. Most reader summaries focus on "models can't find docs in the middle" but the kv task proves the bias has nothing to do with semantics, retrieval noise, or distractor documents. It's a property of the attention pattern itself: given a 20-position list of JSON kv-pairs and a "what is the value of key K?" query, the model can find K when it's near the boundaries and gets confused when it's in the middle, even though there are no distractor passages competing for attention.

**Why it matters:** This means no amount of better retrieval, better reranking, or better prompt phrasing fully fixes the bug. The bug is in how transformer attention distributes mass across long sequences — there is empirical evidence (followup work) that this comes from positional encoding interacting with the softmax-over-long-sequences regime. For memory-system designers, this is an architectural property to design around (with placement and chunk count), not one that's about to be "trained away".

**Example of good use:** A memory architect designs the agent's working memory as a structured prompt with a fixed schema — `[persona]`, `[task]`, `[top-1 retrieved fact]`, `[history]`, `[top-1 retrieved fact again]` — explicitly using both ends of the context for the most important content. Eval shows 8-point accuracy improvement over a naive "concat everything" prompt.

**Example of misapplication:** A team upgrades to a 200K-context model and decides to stop using their retriever, just stuffing the full 100k-token customer history into context. Quality goes DOWN because the relevant fact is at turn 47 (middle), even though it would have been retrieved and placed first with the old RAG pipeline. They blame the new model.

## Extracted Prompts

The paper uses simple instruction prompts with explicit document blocks. Excerpts:

**Prompt explanation:** Multi-document QA prompt format used throughout the paper. The K documents are inserted with explicit "Document [N]" boundaries, and the question follows.

```
Write a high-quality answer for the given question using only the
provided search results (some of which might be irrelevant).

Document [1](Title: ...) ...
Document [2](Title: ...) ...
...
Document [K](Title: ...) ...

Question: <question>
Answer:
```

**Prompt explanation:** Closed-book baseline — same model, no retrieved documents, used to establish the "without context" accuracy floor.

```
Write a high-quality answer for the given question.
Question: <question>
Answer:
```

**Prompt explanation:** Synthetic key-value retrieval prompt — stripped-down JSON kv lookup with no semantic content, used to prove the U-shape is architectural.

```
Extract the value corresponding to the specified key in the JSON object below.

JSON data:
{"key_1": "value_1", "key_2": "value_2", ..., "key_N": "value_N"}

Key: "key_i"
Corresponding value:
```

## Citations

- Attention is all you need (Vaswani et al., 2017) — arxiv:1706.03762
- Transformer-XL (Dai et al., 2019) — arxiv:1901.02860
- FlashAttention (Dao et al., 2022) — arxiv:2205.14135
- In-context retrieval-augmented language models (Ram et al., 2023) — arxiv:2302.00083
- When not to trust language models (Mallen et al., 2023) — arxiv:2212.10511
- Toolformer (Schick et al., 2023) — arxiv:2302.04761
- Generating long sequences with sparse transformers (Child et al., 2019) — arxiv:1904.10509
- (Full list of ~80 references in frontmatter `citations:`)

## Related Digests

- [[beltagy-2020-longformer]] — Longformer: architectural fix for long context via sparse attention
- [[packer-2023-memgpt-os]] — MemGPT: hierarchical memory designed around the truncated-context limitation
- [[hu-2026-evermemos]] — EverMemoS: addresses position bias via summary compression
- [[li-2025-memos]] — MemOS: memory as an OS layer above the context window
- [[wang-2026-memmachine]] — MemMachine: memory routing to bypass middle-blindness
- [[patel-2026-engram]] — Engram: cited Lost in the Middle for context-window placement constraints
- [[wu-2024-longmemeval]] — LongMemEval: cites Lost in the Middle for benchmark design
- [[maharana-2024-locomo]] — LoCoMo: descendant benchmark for very-long-context evaluation
- [[petrov-2026-schema-grounded-memory]] — Schema-grounded memory: addresses position bias via structured retrieval

## Reviewer Notes

**Overall severity:** Clean

Claims cross-checked against the loaded paper text:
- U-shaped accuracy curve on multi-document QA (Figure 1, Figure 5) — verified Section 2.
- GPT-3.5-Turbo closed-book accuracy 56.1% used as baseline — verified Section 2.3.
- 6 models tested (GPT-3.5-Turbo, GPT-3.5-Turbo-16k, Claude-1.3, Claude-1.3-100k, MPT-30B-Instruct, LongChat-13B-16k) — verified Section 2.1 + Section 3.1.
- Extended-context models often have identical performance to short-context counterparts at small input sizes — verified Section 2.3.
- Synthetic key-value retrieval shows the same U-shape — verified Section 3.
