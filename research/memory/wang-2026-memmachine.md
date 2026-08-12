---
corpus: agentic-memory
kind: paper-digest
slug: wang-2026-memmachine
title: "MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents"
authors:
  - "Shu Wang"
  - "Edwin Yu"
  - "Oscar Love"
  - "Tom Zhang"
  - "Tom Wong"
  - "Steve Scargall"
  - "Charles Fan"
year: 2026
publication_date: "2026-03"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2604.04853"
doi: null
arxiv_id: "2604.04853"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Where you spend engineering effort in a memory system matters more than how clever the storage is — across the LongMemEval ablation, the four retrieval-stage knobs (retrieval depth +4.2%, context formatting +2.0%, search prompt +1.8%, user-query bias +1.4%) collectively added ~9.4 points while the headline ingestion-stage knob (sentence chunking) added only +0.8% — roughly 13× more leverage on the retrieve side than the encode side."
topics:
  - agent-memory
  - episodic-memory
  - profile-memory
  - retrieval-architecture
  - contextualized-retrieval
  - multi-hop-reasoning
  - ablation-study
  - llm-evaluation
  - prompt-engineering
  - personalization
tags:
  - paper
  - memory-architecture
  - retrieval-pipeline
  - long-term-memory
  - ground-truth-preserving
  - benchmark
  - locomo
  - longmemeval
  - hotpotqa
  - mem0-comparison
  - open-source
entities:
  - wang-shu
  - fan-charles
  - memverge
related_digests:
  - latimer-2025-hindsight-memory
  - adler-2026-storage-not-memory
  - chhikara-2025-mem0
  - packer-2023-memgpt-os
citations:
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Charles Packer", "Sarah Wooders", "Kevin Lin", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    authors: ["Joon Sung Park", "Joseph C. O'Brien", "Carrie J. Cai", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2304.03442"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2504.19413"
  - title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
    authors: ["Preston Rasmussen", "Pavlo Paliychuk", "Travis Beauvais", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2501.13956"
  - title: "Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2402.17753"
  - title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "et al."]
    year: 2024
    venue: "ICLR 2025"
    doi: null
    url: null
    arxiv_id: "2410.10813"
  - title: "Episodic Memories Generation and Evaluation Benchmark for Large Language Models (EpBench)"
    authors: ["Alexis Huet", "Zied Ben Houidi", "Dario Rossi"]
    year: 2025
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory in the Age of AI Agents: A Survey"
    authors: ["Yuyang Hu", "Shichun Liu", "Yue Yue", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2512.13564"
  - title: "Episodic and Semantic Memory"
    authors: ["Endel Tulving"]
    year: 1972
    venue: "Organization of Memory, Academic Press"
    doi: null
    url: null
    arxiv_id: null
  - title: "Human Memory: A Proposed System and Its Control Processes"
    authors: ["Richard C. Atkinson", "Richard M. Shiffrin"]
    year: 1968
    venue: "The Psychology of Learning and Motivation, Academic Press"
    doi: null
    url: null
    arxiv_id: null
  - title: "Unsupervised Multilingual Sentence Boundary Detection"
    authors: ["Tibor Kiss", "Jan Strunk"]
    year: 2006
    venue: "Computational Linguistics"
    doi: null
    url: null
    arxiv_id: null
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    authors: ["Nelson F. Liu", "Kevin Lin", "John Hewitt", "et al."]
    year: 2024
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards Lifespan Cognitive Systems"
    authors: ["Yu Wang", "Chi Han", "Tongtong Wu", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2409.13265"
  - title: "Observational Memory: A Human-Inspired Memory System for AI Agents"
    authors: ["Tyler Barnes", "Sam Bhagwat"]
    year: 2026
    venue: "Mastra Technical Report"
    doi: null
    url: "https://mastra.ai/research"
    arxiv_id: null
  - title: "MemOS: A Memory OS for AI System"
    authors: ["Zhiyu Li", "Chenyang Xi", "Chunyu Li", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2507.03724"
  - title: "MemOS: An Operating System for Memory-Augmented Generation (MAG) in Large Language Models"
    authors: ["Zhiyu Li", "Shichao Song", "Hanyu Wang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2505.22101"
  - title: "Agent Lightning: Train ANY AI Agents with Reinforcement Learning"
    authors: ["Xiao Luo", "Yuxuan Zhang", "Zheng He", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2508.03680"
  - title: "Code execution with MCP"
    authors: ["Anthropic"]
    year: 2025
    venue: "Engineering blog"
    doi: null
    url: "https://www.anthropic.com/engineering/code-execution-with-mcp"
    arxiv_id: null
  - title: "Introducing Code Mode for MCP servers"
    authors: ["Cloudflare"]
    year: 2025
    venue: "Cloudflare blog"
    doi: null
    url: "https://blog.cloudflare.com/code-mode-mcp/"
    arxiv_id: null
  - title: "HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering"
    authors: ["Zhilin Yang", "Peng Qi", "Saizheng Zhang", "et al."]
    year: 2018
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 13
  title: "LongMemEvalS ablation: contribution of each optimization to overall LLM score"
  page: 13
  image_path: "figures/wang-2026-memmachine-fig.png"
---

# MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents

**Authors:** Shu Wang, Edwin Yu, Oscar Love, Tom Zhang, Tom Wong, Steve Scargall, Charles Fan (MemVerge, Inc.)
**Published:** 2026-03 · [Source](https://arxiv.org/abs/2604.04853)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MemMachine is an open-source memory system from MemVerge that stores entire conversational episodes verbatim — refusing to LLM-distill on the ingest path the way Mem0/Zep do — then layers contextualized retrieval (vector-match a "nucleus" sentence, then pull one preceding and two following episodes to rebuild conversational context) on top. On LoCoMo it hits 0.9169 overall with gpt-4.1-mini (top of the published leaderboard among open systems, +9.7 points over next-best Memobase, ~78% fewer input tokens than Mem0). The headline ablation result is the structural one: across a 6-dimension sweep on LongMemEvalS (n=500), retrieval-stage knobs dominate ingestion-stage knobs — retrieval depth k=20→30 alone added +4.2%, context formatting +2.0%, search-prompt redesign +1.8%, COT→simple prompt +1.6%, and user-query bias correction +1.4%, while the showcase ingestion optimization (sentence-level chunking) added only +0.8%. Counterintuitively, swapping the answer LLM from GPT-5 to the smaller GPT-5-mini added +2.6% when paired with the simplified Edwin3 search prompt, making the cheapest configuration also the most accurate. Pareto-optimum is C12 (GPT-5-mini, k=20) at 0.922 with 2.58M input tokens vs. the 0.930 peak at C15 needing 3.8× more tokens for +0.8%. An optional Retrieval Agent (ToolSelectAgent router → ChainOfQuery / SplitQuery / direct) handles late-binding multi-hop queries: 93.2% on HotpotQA hard and 92.6% on WikiMultiHop under randomized-noise conditions, with bounded cost (router ~1.2k tokens; full ChainOfQuery ~5.7k). The architectural moral: preserve ground truth, invest in how you ask the index, not what you destroy before storage.

## Key Takeaway

The cheap small model with the right prompt beats the expensive big model with a fancier one — GPT-5-mini outperforms GPT-5 by +2.6% on LongMemEval when paired with a direct, no-chain-of-thought search prompt, because GPT-5's built-in reasoning actively interferes when you explicitly tell it to reason, while GPT-5-mini's streamlined instruction-following slots cleanly into a concise instruction. Stop assuming the bigger answer model is the bottleneck; in a well-built memory system, the bottleneck is whether your prompt fights or rides the model's internal behavior.

## Implications

- **[ENGRAM-E: Encode] Stop distilling on the write path unless you must.** MemMachine writes raw episodes and only LLM-summarizes when STM overflows or when extracting profile facts; this is what lets it use ~78% fewer input tokens than Mem0 at higher LoCoMo accuracy. If your memory system runs an LLM on every inbound message, that's where your spend and your factual drift come from — strip it and let retrieval do the work.

- **[ENGRAM-R: Retrieve] Spend on retrieval optimization, not on cleverer storage.** The ablation shows ~9.4 points of accuracy live in retrieval-stage knobs (k, formatting, prompt, bias correction) vs. ~0.8 points in the headline ingestion knob (sentence chunking). When prioritizing engineering effort, retrieval depth tuning + prompt iteration is 13× the leverage of fancier chunking strategies. Re-run your own ablations with this hierarchy.

- **[ENGRAM-R: Retrieve] Embedding match alone misses conversational context — pull neighbors.** MemMachine's contextualization step grabs the nucleus episode plus one preceding and two following turns, then reranks the resulting clusters; this fixes the embedding-dissimilarity problem where a question like "the restaurant recommendation" semantically matches the answer turn but loses the constraint-setting turns around it. If your retriever returns isolated chunks, you're throwing away conversational structure that's already in your store.

- **[ENGRAM-R: Retrieve] Add a "user:" prefix to your search query to fight assistant-message bias.** Assistant turns are longer and therefore generate more embedding keys, biasing vector retrieval toward them; prepending `user:` to the query nudged retrieval back toward user messages and yielded +1.4% on LongMemEval. Cheap, mechanical, untargeted gain.

- **[ENGRAM-R: Retrieve] k is non-monotonic and model-dependent — measure, don't assume.** With GPT-5, k=30 beats k=50 (lost-in-the-middle); with GPT-5-mini, monotonic gains continue through k=100. The right k depends on the answer model's attention behavior at length, not on a global "deeper is better" rule. Bake k into your eval harness as a tuned per-model parameter.

- **[ENGRAM-R: Retrieve] Tune your prompt every time you swap the answer model.** GPT-5-mini + concise prompt outperformed GPT-5 + COT prompt by +2.6% at the same k. Reusing prompts across model upgrades is a silent regression — every model swap should trigger a prompt re-evaluation.

- **[ENGRAM-A: Aggregate, late-binding] Layer an LLM router for multi-hop queries; don't make every query pay for it.** The Retrieval Agent classifies queries (multi-hop chain / single-hop fan-out / single-hop direct) and only invokes the heavier ChainOfQuery (3 iterations, ~5.7k tokens) when needed; 36% of HotpotQA-hard queries route straight to baseline with just the +1.2k router overhead. This is the right pattern for production: bounded cost ceilings per branch, advisory cost properties on every node, agent_mode flag flippable per-query.

- **[ENGRAM-G: Ground / Provenance] If you need auditability, retrieve raw episodes, not summaries.** Compaction (Mastra-style observational memory) gets you prompt caching and stable context, but you lose the exact wording of who said what when — fatal for healthcare/legal/financial deployment. MemMachine's STM-summary-plus-raw-episode-retrieval pattern is the explicit compromise: high-level context cheap, ground truth available on demand.

## How to Apply It (method)

**Scenario:** You're building Flow OS's memory layer — an agent operating system that captures, structures, and recalls multi-session user context so the AI workforce becomes measurably smarter with each engagement. You've got episodic capture working (every turn stored), but retrieval is brittle: agents miss obvious facts from prior sessions and over-spend on LLM-based extraction. You want to run MemMachine's ablation methodology on your own corpus to figure out where to invest next.

**Steps:**

1. **Pick a benchmark you can re-run.** Use LongMemEvalS (500 questions, ~115k tokens each, six question types: single-session-user-fact, single-session-preference, single-session-assistant-fact, temporal-reasoning, knowledge-update, multi-session-reasoning) or, better, build your own slice from real Flow OS interaction logs labelled with ground-truth answers. The benchmark must let you isolate a single variable per run.

2. **Stand up the reference configuration first.** Baseline: GPT-5 as answer model, no chunking, no user-q prefix, no JSON-string formatting, Edwin1 (longest/oldest) search prompt, k=20. Record the LLM-judge score per category and overall. This is your C5 anchor.

3. **Run the six-dimension ablation by changing exactly one variable per run.** Generate the configuration matrix (12 rows, mirroring Wang et al.'s Table 12):

   | Variable | Levels to try |
   |---|---|
   | Answer model | GPT-5, GPT-5-mini, (your local equivalent) |
   | Sentence chunking | off / on |
   | User-Q prefix | off / on |
   | JSON-string formatting | off / on |
   | Search prompt | Edwin1 (verbose) / Edwin3 (concise direct) |
   | Retrieval depth k | 20, 30, 50, 100 |

   For each pair that differs in exactly one variable, the score delta is that variable's marginal contribution.

4. **Apply the contextualization retrieval primitive.** For every nucleus hit from vector search, pull one preceding and two following episodes from the same session, dedup against STM, rerank the clusters with a cross-encoder (the paper uses AWS Cohere rerank-v3-5:0; you could use bge-reranker-v2-m3 locally), then sort chronologically before passing to the answer LLM.

5. **Add the user-query bias correction.** Prepend the literal string `user: ` to every search query before embedding it. No other code change. Re-run, measure delta.

6. **Swap the search prompt to a concise direct form.** Replace any chain-of-thought scaffolding in your retrieval prompt with a direct instruction. Reference Edwin3 design intent: terse, no reasoning hops, just "retrieve N most-relevant episodes for QUERY."

   Example concise search prompt template:

   ```
   Given the user query below, return the K most relevant past
   conversation episodes from memory. Match on factual relevance,
   not topical similarity. No reasoning, no chain-of-thought —
   just the episodes.

   QUERY: {query}
   K: {k}
   ```

7. **Layer the Retrieval Agent only on top of a working baseline.** Build the ToolSelectAgent router (single LLM call, classifies query into multi-hop chain / single-hop fan-out / single-hop direct), then implement two strategy nodes:

   ChainOfQuery (for multi-hop), max 3 iterations of: retrieve → judge sufficiency + rewrite query → accumulate evidence → stop at ≥0.8 confidence.

   SplitQuery (for fan-out), decompose into 2–6 independent sub-queries via one LLM call, execute concurrently with `asyncio.gather()`, pool results.

   Both strategies delegate to the same declarative_memory.search_scored() leaf, so any retrieval improvement propagates.

   Router classification prompt skeleton:

   ```
   Classify the query into exactly one of:
   - multi-hop: two or more sequentially dependent retrieval steps
     where a later step needs the result of an earlier one
   - single-hop-fanout: multiple independent subjects answerable
     via parallel lookups, no inter-dependency
   - single-hop: single subject, single lookup, no decomposition

   Tie-breaker: if any explicit dependency chain exists, classify
   as multi-hop even when multiple entities appear.

   QUERY: {query}
   ```

8. **Track the Pareto frontier, not just the peak.** Plot accuracy vs. input-token cost across all configurations. The peak (C15: GPT-5-mini, k=100, 0.930 score, 9.79M input tokens) is rarely worth the cost over C12 (GPT-5-mini, k=20, 0.922 score, 2.58M tokens) — a 3.8× cost increase for +0.8 points. Define the inflection where additional accuracy stops paying for itself in your deployment context.

9. **Re-run the full ablation every time the answer LLM changes.** Wang et al. show GPT-5-mini + Edwin3 beats GPT-5 + Edwin3 by 2.6 points, but GPT-5 + Edwin1 (COT) is the worst combination — prompts that are optimal for one model are pessimal for the next. Codify this as a deployment ritual.

**Expected outcome:** A per-Flow-OS-tenant performance map showing exactly which retrieval and prompt knobs move accuracy on your real workload, a Pareto frontier showing where additional compute stops paying off, and a justified config recommendation per use case (interactive low-latency vs. high-accuracy compliance review). Plus the architectural confidence to stop spending engineering effort on ingestion-stage cleverness (per-message LLM extraction, fancy chunking, distilled summaries) and redirect it to retrieval, prompts, and lightweight LLM routing on multi-hop queries.

## Best Figure

![Figure 13 — LongMemEvalS ablation: contribution of each optimization to overall LLM score (page 13)](figures/wang-2026-memmachine-fig.png)

Image Candidates:
Table 13 (p. 13): The ablation contribution table — directly shows the paper's headline architectural claim (retrieval-stage optimizations dominate ingestion-stage) in a single 9-row view with deltas.
Table 11 (p. 12): LoCoMo benchmark comparison across all major systems — quantifies the lead over Mem0/Zep/Memobase/LangMem/OpenAI baseline in one frame.
Table 16 (p. 16): Architectural design-space comparison across MemMachine vs. Mem0 vs. Zep vs. Mastra OM vs. MemOS vs. Full Context on 8 properties — the most useful "where does my system sit" frame.

Best Image:
Figure Name: Table 13: "LongMemEvalS ablation: contribution of each optimization to overall LLM score, measured by comparing configuration pairs that differ in one variable."
Figure Page: 13
Slide Caption: Retrieval-stage optimizations dominate ingestion-stage in MemMachine's LongMemEvalS ablation.
Description: Table 13 quantifies the marginal contribution of every optimization dimension tested by isolating configuration pairs that differ in exactly one variable. The five retrieval-stage knobs — retrieval depth k=20→30 (+4.2%), context formatting JSON-str (+2.0%), search prompt Edwin1→3 (+1.8%), removing chain-of-thought from the answer prompt (+1.6%), and user-query bias correction (+1.4%) — collectively add ~9.4 percentage points to LLM-judge accuracy, while the only tested ingestion-stage optimization (sentence chunking) adds just +0.8%. The model-selection row at the bottom shows that swapping GPT-5 for the smaller, cheaper GPT-5-mini adds another +2.6%, making the most cost-efficient configuration also the most accurate. The table is the visual centerpiece of the paper's architectural thesis: invest engineering effort in retrieval, not in cleverer ingestion.

## What Experts Overlook

The paper's most architecturally consequential design choice — and one that's easy to skim past in the System Overview — is not the contextualized retrieval mechanism but the **multi-query reranker**: when the Retrieval Agent runs ChainOfQuery or SplitQuery, the final cross-encoder reranker receives a concatenation of *all* queries used during retrieval (the original plus every rewrite and every sub-query), not just the original query. This means intermediate facts — entities surfaced only during the agent's internal reasoning loop, never named in the user's original question — still score well in the final ranking and survive into the answer LLM's context. Without this, the agent's intermediate work would be invisible to the final ranking, and the supporting evidence for hop-2 and hop-3 of a chain would be drowned out by hop-1-relevant noise.

**Why it matters:** Most experts would assume reranking is a final-stage cleanup over the union of retrieved candidates. But the *query* you rerank against silently determines what survives. By using a multi-query concatenation, MemMachine turns the reranker into an evidence-aware filter that knows the *whole reasoning trace*, not just the entry-point query. This is what lets ChainOfQuery hit 95.31% recall on HotpotQA-hard's multi-hop bridge questions — the reranker can keep an intermediate-entity episode that would have scored low against the original query alone but scores high against the rewritten query that mentions the intermediate entity. It's a structural reason agent-mode retrieval beats baseline-plus-retry loops.

**Example of good use:** A memory-architect building Flow OS's multi-session retrieval pipeline implements a query-trace buffer: every rewrite, sub-query, or HyDE expansion gets appended to a list. At rerank time, the cross-encoder scores each candidate episode against the concatenated list, not just the user's input. Result: when the agent answers "what's the current employer of the spouse of the CEO of Acme," the spouse-discovery episode survives reranking even though "spouse" doesn't appear in the original query, because the second-hop rewrite mentioned them by name.

**Example of misapplication:** A team copies MemMachine's ChainOfQuery loop but reuses their single-query reranker — they rerank only against the original user query at every step. The reranker has no idea about the agent's intermediate entities, so episodes containing the just-discovered Person X get pushed below noisier surface-match results. The chain produces the right rewrites but loses the supporting evidence at the final stage; accuracy regresses below baseline retrieval despite all the extra LLM spend on the agent loop.

## Extracted Prompts

The paper does not publish full verbatim prompt text for its agent strategies; it describes prompt design principles and references the Edwin1/Edwin3 variants by name without inlining them. The closest the paper comes to verbatim prompt content is the structural-constraint description for the SplitQuery decomposition prompt and the sufficiency-judgment behavior of ChainOfQuery.

**Prompt explanation:** ChainOfQuery sufficiency-judgment + query-rewrite prompt — invoked once per iteration (up to 3) to decide whether accumulated evidence is sufficient to answer, and if not, to rewrite the query for the next hop. The paper specifies the prompt's enforced properties rather than the literal wording.

```
[Described, not published verbatim. Enforced properties:]
- Evidence-only judgment (no external knowledge)
- Strict completeness standards
- Entity grounding (rewrites use only entities present in retrieved evidence)
- Calibrated confidence scoring
- Early stopping at confidence >= 0.8
```

**Prompt explanation:** SplitQuery decomposition prompt — invoked once per query that the router classifies as single-hop fan-out, decomposes the query into 2–6 independent sub-queries.

```
[Described, not published verbatim. Enforced structural constraints:]
- Sub-queries must each be answerable by a single fact lookup
- Derived operations (compare, rank, difference) are prohibited
- Conservative tie-breaker defaults to no-split when ambiguous
```

**Prompt explanation:** ToolSelectAgent (root router) classification prompt — single LLM call that classifies each incoming query into one of three structural types and routes to exactly one strategy node.

```
[Described, not published verbatim. Enforced structure:]
Embedded calibration examples for each class.
Three classes:
- Multi-hop dependency chain  -> ChainOfQuery
- Single-hop multi-entity     -> SplitQuery
- Single-hop direct           -> MemMachine (baseline)
Tie-breaker: if any explicit dependency chain exists, classify
as multi-hop even if multiple entities appear.
```

No verbatim prompt text for Edwin1, Edwin2, or Edwin3 search-prompt variants is published in the paper; only their relative performance is reported. Researchers wishing to reproduce these specific prompt variants must consult the MemMachine GitHub repository.

## Citations

- Packer et al., 2024 — MemGPT: Towards LLMs as Operating Systems (arXiv:2310.08560) *[already digested as `packer-2023-memgpt-os`]*
- Park et al., 2023 — Generative Agents: Interactive Simulacra of Human Behavior (arXiv:2304.03442)
- Lewis et al., 2020 — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (NeurIPS)
- Chhikara et al., 2025 — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (arXiv:2504.19413) *[already digested as `chhikara-2025-mem0`]*
- Rasmussen et al., 2025 — Zep: A Temporal Knowledge Graph Architecture for Agent Memory (arXiv:2501.13956)
- Maharana et al., 2024 — Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo) (arXiv:2402.17753)
- Wu et al., 2024 — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory (arXiv:2410.10813, ICLR 2025)
- Huet et al., 2025 — Episodic Memories Generation and Evaluation Benchmark (EpBench) (ICLR)
- Hu et al., 2025 — Memory in the Age of AI Agents: A Survey (arXiv:2512.13564)
- Tulving, 1972 — Episodic and Semantic Memory (Academic Press)

Remaining 11 citations in frontmatter `citations:` field — including Atkinson & Shiffrin (1968) on the multi-store memory model, Liu et al. (2024) Lost in the Middle, Li et al. MemOS papers, Mastra's Observational Memory technical report, and the HotpotQA / Cloudflare Code Mode / Anthropic MCP code execution references that ground the Retrieval Agent's future-work direction.

## Related Digests

- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects (also tagged `memory-architect` — complementary four-network-typed-memory architecture; both papers attack the LongMemEval benchmark but reach different conclusions about where the architectural leverage is)
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall (the closest sibling — independently arrives at the same "write-time intelligence is anti-intelligence" thesis but from the encoding-gate angle rather than the retrieval-ablation angle)
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (the explicit comparison baseline — MemMachine reports ~78% fewer input tokens than Mem0 at higher LoCoMo accuracy in matched memory mode)
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems (foundational virtual-memory-for-LLMs frame; MemMachine cites this as a key inspiration but argues against MemGPT's LLM-driven page-management decisions on cost grounds)

## Reviewer Notes

**Overall severity:** Clean

All numeric claims (0.9169 LoCoMo with gpt-4.1-mini; +4.2% / +2.0% / +1.8% / +1.4% / +0.8% ablation deltas; GPT-5-mini +2.6% over GPT-5; 93.2% HotpotQA hard; 92.6% WikiMultiHop randomized-noise; ~78–80% token reduction vs Mem0; Pareto C12 at 0.922 / 2.58M input tokens; k=30 → 0.912 dropping to k=50 → 0.890 for GPT-5; ChainOfQuery 95.31% recall on multi-hop) verified against Tables 3, 5, 7, 10, 11, 12, 13, 14, 15 of the source paper. Architectural descriptions (contextualization: 1 preceding + 2 following episodes; sentence-level indexing via NLTK Punkt; PostgreSQL+pgvector / SQLite / Neo4j storage stack; STM summarization; profile memory in SQL) match Section 4 verbatim. Retrieval Agent strategy descriptions (ToolSelectAgent router; 3-iteration ChainOfQuery cap; SplitQuery 2-6 sub-queries via asyncio.gather; multi-query reranking; agent_mode flag; cost properties on nodes) match Section 5 verbatim. The "What Experts Overlook" claim about the multi-query reranker is explicitly stated in §5.5 of the paper, not invented. The extracted-prompts section correctly notes that the paper describes prompt properties rather than publishing verbatim text — no fabricated prompt content. ENGRAM tagging applied by the digester is interpretation, not paper content, and is marked as such in the implications headers.
