---
corpus: agentic-memory
kind: paper-digest
slug: patel-2026-engram
title: "ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents"
authors:
  - "Patel, Daivik"
  - "Patel, Shrenik"
year: 2026
publication_date: "2026-02"
venue: "arXiv preprint (cs.MA)"
source_url: "https://arxiv.org/abs/2511.12960"
doi: null
arxiv_id: "2511.12960"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Three typed stores (episodic / semantic / procedural) + one router + one cosine-similarity retriever beats every elaborate memory architecture on LoCoMo (LLM-as-Judge 77.55 vs MemOS 72.99, Mem0 64.73, Zep 42.29) and the full-context oracle on LongMemEvalS (71.40% vs 56.20% at ~1% of the tokens) — provided you (a) actually split the stores rather than collapsing to one (single-store ablation drops 31 pts to 46.56%) and (b) cap the merged top-k budget at K≈25, where marginal accuracy/token return is 12.8 J-pts per 1k tokens vs 0.29 beyond K=30."
topics:
  - long-term-memory
  - typed-memory
  - episodic-semantic-procedural
  - dense-retrieval
  - locomo
  - longmemeval
  - conversational-agents
  - memory-routing
  - ablation-study
tags:
  - paper
  - memory-architecture
  - simplicity-thesis
  - counter-thesis-to-adler-2026
  - benchmark-locomo
  - benchmark-longmemeval
  - typed-memory-stores
  - write-time-extraction
  - dense-only-retrieval
  - naming-collision-with-user-framework
entities:
  - patel-daivik
  - patel-shrenik
  - rutgers-university
related_digests:
  - adler-2026-storage-not-memory
  - li-2025-memos
  - chhikara-2025-mem0
  - rasmussen-2025-zep-temporal-kg
  - packer-2023-memgpt-os
  - maharana-2024-locomo
  - wu-2024-longmemeval
  - hu-2026-evermemos
  - latimer-2025-hindsight-memory
citations:
  - title: "Arigraph: Learning knowledge graph world models with episodic memory for llm agents"
    authors: ["Petr Anokhin", "Nikita Semenov", "Artyom Sorokin", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2404.11622"
    url: null
    arxiv_id: "2404.11622"
  - title: "Working memory"
    authors: ["Alan D. Baddeley", "Graham Hitch"]
    year: 1974
    venue: "The Psychology of Learning and Motivation, vol. 8"
    doi: null
    url: null
    arxiv_id: null
  - title: "Longformer: The long-document transformer"
    authors: ["Iz Beltagy", "Matthew E. Peters", "Arman Cohan"]
    year: 2020
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2004.05150"
    url: null
    arxiv_id: "2004.05150"
  - title: "Improving language models by retrieving from trillions of tokens"
    authors: ["Sebastian Borgeaud", "Arthur Mensch", "Jordan Hoffmann", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2112.04426"
    url: null
    arxiv_id: "2112.04426"
  - title: "Mem0: Building production-ready ai agents with scalable long-term memory"
    authors: ["Pratyaksh Chhikara", "Devvrat Khant", "Shubh Aryan", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2504.19413"
    url: null
    arxiv_id: "2504.19413"
  - title: "Preserved learning and retention of pattern-analyzing skill in amnesia: dissociation of knowing how and knowing that"
    authors: ["Neal J. Cohen", "Larry R. Squire"]
    year: 1980
    venue: "Science 210(4466):207-210"
    doi: "10.1126/science.7414331"
    url: null
    arxiv_id: null
  - title: "Transformer-xl: Attentive language models beyond a fixed-length context"
    authors: ["Zihang Dai", "Zhilin Yang", "Yiming Yang", "et al."]
    year: 2019
    venue: "ACL"
    doi: "10.18653/v1/P19-1285"
    url: null
    arxiv_id: null
  - title: "Extending context window of large language models via semantic compression"
    authors: ["Wenhao Fei", "Xiao Niu", "Peng Zhou", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2312.09571"
    url: null
    arxiv_id: "2312.09571"
  - title: "Realm: Retrieval-augmented language model pre-training"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."]
    year: 2020
    venue: "ICML"
    doi: null
    url: "https://arxiv.org/abs/2002.08909"
    arxiv_id: "2002.08909"
  - title: "Dense passage retrieval for open-domain question answering"
    authors: ["Vladimir Karpukhin", "Barlas Oguz", "Sewon Min", "et al."]
    year: 2020
    venue: "EMNLP"
    doi: "10.18653/v1/2020.emnlp-main.550"
    url: "https://arxiv.org/abs/2004.04906"
    arxiv_id: "2004.04906"
  - title: "Generalization through memorization: Nearest neighbor language models"
    authors: ["Urvashi Khandelwal", "Angela Fan", "Dan Jurafsky", "et al."]
    year: 2020
    venue: "ICML"
    doi: null
    url: "https://proceedings.mlr.press/v119/khandelwal20a.html"
    arxiv_id: null
  - title: "LangMem: Modular memory for agentic systems"
    authors: ["LangChain"]
    year: 2024
    venue: "GitHub"
    doi: null
    url: "https://github.com/langchain-ai/langmem"
    arxiv_id: null
  - title: "Retrieval-augmented generation for knowledge-intensive nlp tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: "10.48550/arXiv.2005.11401"
    url: null
    arxiv_id: "2005.11401"
  - title: "Graphreader: Building graph-based agent to enhance long-context abilities of llms"
    authors: ["Shilong Li", "Yancheng He", "Hangyu Guo", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2410.12345"
  - title: "Memos: A memory os for ai system"
    authors: ["Zhiyu Li", "Shichao Song", "Chenyang Xi", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2507.03724"
    url: null
    arxiv_id: "2507.03724"
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Nelson F. Liu", "Kevin Lin", "John Hewitt", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2307.03172"
    url: null
    arxiv_id: "2307.03172"
  - title: "Evaluating very long-term conversational memory of llm agents"
    authors: ["Amanpreet Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "et al."]
    year: 2024
    venue: "ACL"
    doi: null
    url: "https://arxiv.org/abs/2402.17753"
    arxiv_id: "2402.17753"
  - title: "Memllm: Finetuning llms to use an explicit read-write memory"
    authors: ["Ali Modarressi", "Alperen Koksal", "Ahmad Imani", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2404.11672"
    url: null
    arxiv_id: "2404.11672"
  - title: "Gpt-4 technical report"
    authors: ["OpenAI"]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2303.08774"
    url: null
    arxiv_id: "2303.08774"
  - title: "Memgpt: Towards llms as operating systems"
    authors: ["Charles Packer", "Vivian Fang", "Shishir G. Patil", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2307.05030"
    url: null
    arxiv_id: "2307.05030"
  - title: "Bleu: a method for automatic evaluation of machine translation"
    authors: ["Kishore Papineni", "Salim Roukos", "Todd Ward", "Wei-Jing Zhu"]
    year: 2002
    venue: "ACL"
    doi: "10.3115/1073083.1073135"
    url: null
    arxiv_id: null
  - title: "Zep: A temporal knowledge graph architecture for agent memory"
    authors: ["Preston Rasmussen", "Pavlo Paliychuk", "Travis Beauvais", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2501.13956"
    url: null
    arxiv_id: "2501.13956"
  - title: "Episodic and semantic memory"
    authors: ["Endel Tulving"]
    year: 1972
    venue: "Organization of Memory, Academic Press"
    doi: null
    url: null
    arxiv_id: null
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS 30"
    doi: null
    url: "https://arxiv.org/abs/1706.03762"
    arxiv_id: "1706.03762"
  - title: "Augmenting language models with long-term memory"
    authors: ["Weizhi Wang", "Li Dong", "Hao Cheng", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: "10.48550/arXiv.2306.07174"
    url: null
    arxiv_id: "2306.07174"
  - title: "Longmemeval: Benchmarking chat assistants on long-term interactive memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "et al."]
    year: 2025
    venue: "ICLR"
    doi: null
    url: "https://arxiv.org/abs/2410.10813"
    arxiv_id: "2410.10813"
  - title: "Memory-r1: Enhancing large language model agents to manage and utilize memories via reinforcement learning"
    authors: ["Sikuan Yan", "Xiufeng Yang", "Zuchao Huang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2508.19828"
    url: null
    arxiv_id: "2508.19828"
  - title: "Judging llm-as-a-judge with mt-bench and chatbot arena"
    authors: ["Lianmin Zheng", "Wei-Lin Chiang", "Ying Sheng", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2306.05685"
    arxiv_id: "2306.05685"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "System overview of ENGRAM — typed routing + per-type top-k retrieval"
  page: 2
  image_path: "figures/patel-2026-engram-fig.png"
---

# ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents

**Authors:** Daivik Patel, Shrenik Patel (Rutgers University)
**Published:** 2026-02 · [Source](https://arxiv.org/abs/2511.12960)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

> **Namespace warning for this lens.** This paper proposes a memory system *called* ENGRAM with three typed stores. Your own "memory-architect" lens uses **ENGRAM** as a six-dimension framework (Encode / Network / Ground / Retrieve / Aggregate / Maintain) extracted from your 2026 meta-analysis of 53 OSS memory systems. They are not the same artifact and there is no relationship between the two — the acronym collision is coincidence. Throughout this digest, "ENGRAM (paper)" refers to Patel & Patel's system; "ENGRAM (framework)" refers to your six-dimension lens.

## TLDR

ENGRAM (paper) is a deliberately stripped-down LLM memory system from Rutgers: every user turn is passed through a single router that emits a three-bit mask over `{episodic, semantic, procedural}` stores, three small LLM extractors convert the turn into typed JSON records (episodic `(title, summary, timestamp, embedding)`, semantic `(fact, timestamp, embedding)`, procedural `(title, content, timestamp, embedding)`), records land in a local SQLite database, and at query time the system does per-type cosine top-k retrieval, set-union deduplicates, truncates to K=25, and renders speaker-segregated banks into a fixed prompt template fed to `gpt-4o-mini`. Holding backbone and prompt fixed, ENGRAM scores **LLM-as-Judge 77.55** overall on LoCoMo (vs MemOS 72.99, Mem0 64.73, OpenAI memory 52.81, Zep 42.29, LangMem 55.28), winning every category — single-hop 79.90, multi-hop 79.79, open-domain 72.92, temporal 70.79 (only MemOS edges it on temporal at 72.68) — while using **916 mean evidence tokens vs 1593 for MemOS and 4064 for OpenAI** (a 35%+ reduction). Median total latency is 1.487 s vs 9.940 s for full-context (≈85% faster) and 4.965 s for MemOS. On LongMemEvalS it lifts overall accuracy from 56.20% (full-context, 101K tokens) to **71.40% at ≈1.0–1.2K tokens — a ~99% token reduction with +15.2 pts accuracy**, with single-session-preference jumping from 23.33% to 93.33%. The headline ablation: collapsing all three stores into one drops overall accuracy from 77.55% to **46.56% (-31 pts)** — typed separation is the load-bearing design choice, not the retriever. K-sweep shows the knee at K≈25 (75.65 at K=20 → 80.43 at K=60 but evidence tokens grow 767 → 4,196, so marginal return falls from 12.8 to 0.29 J-pts per 1k tokens beyond K=30). **Most useful takeaway:** for the LoCoMo/LongMemEvalS regime, typed partitioning of writes plus dense-only per-type retrieval is sufficient — knowledge graphs, MemOS-style schedulers, and Zep's temporal KG add complexity that does not pay back here, and the entire system fits in a 3-bit routing mask + one SQLite file.

## Key Takeaway

The counter-intuitive lesson is that the architectural axis that buys ~31 accuracy points in agent memory is *not* the retriever, not the LLM backbone, not the storage substrate — it's whether you bother to *type* writes into episodic vs semantic vs procedural buckets before storing them. The same dense cosine retriever over an undifferentiated bag scores 46.56% on LoCoMo; sharded into three typed buckets with a 3-bit router, the identical retriever scores 77.55%. The reason it works isn't that any one store is better — episodic-only hits 66.60%, semantic-only 61.56%, procedural-only 55.06%, and none come within 10 points of the joint system — it's that typed partitioning **prevents cross-type competition at retrieval**: event timelines, stable facts, and procedural protocols are each guaranteed budget before truncation, instead of being washed out by a global scorer ranking them against each other. In other words: the biggest lever in this paper's regime sits at the **Encode** stage of the ENGRAM (framework) lifecycle, but its mechanism of action is at the **Retrieve / Aggregate** stage — you encode types specifically so retrieval doesn't have to do the disambiguation.

## Implications

- **(Encode + Aggregate) Typed routing is the load-bearing decision, not the retriever**: The single largest ablation delta in the paper is the no-typed-routing variant (-31 pts to 46.56%). If you are choosing where to spend engineering effort, typed write-time partitioning of `(episodic, semantic, procedural)` over a shared embedding space outperforms swapping in a heavier retriever or graph DB. The ENGRAM-framework dimension this hits is `E` (the Encode/Capture decision), but the *mechanism* is at `A` (Aggregate / cross-type competition).

- **(Network) Polyglot storage is unnecessary at this scale and benchmark**: ENGRAM (paper) puts all three typed stores in one SQLite file with embeddings stored inline. It still beats MemOS (multi-tier MemCube scheduler with KV-activation + parameter substrates) and Zep (Neo4j temporal KG) on LoCoMo. For LoCoMo-class workloads (10 dialogues, ~16K tokens each, ~600 turns), single-file flat storage is sufficient — polyglot persistence is only earning its keep if your workload exceeds this scale or has hard governance requirements MemCubes solve.

- **(Retrieve) Dense-only cosine + per-type top-k + set union beats hybrid retrieval here**: No reranker, no lexical/BM25 stage, no cross-encoder, no graph traversal. This is at odds with the Adler 2026 counter-thesis (which argues retrieval-time hybrid + reciprocal-rank-fusion + L3 salience reweight + cross-encoder rerank is where the points live). Reconcile by reading both: ENGRAM (paper) shifts intelligence to the **write path** (the type router and the three extractors are LLM calls), Adler shifts it to the **query path**. They aren't contradicting each other on *whether* work needs to happen — they're disagreeing about where.

- **(Aggregate) K=25 is the accuracy/cost knee — burn token budget here last**: Marginal J-per-1k-tokens collapses from 12.8 (K=20→25) to 0.29 (K=30→40). If you're tuning a memory system in this regime, set K=25 first, then ablate elsewhere. Don't reflexively scale K to "give the model more"; past K=30 you're paying for prompt distraction (Liu 2023 lost-in-the-middle).

- **(Ground) The provenance story is shallow — single-source, no contradiction surfacing, "most recent wins"**: The answer-generation prompt explicitly tells the model to "prioritize the most recent memory" when memories contradict. This is the cheapest possible conflict resolution (vs. Zep's bi-temporal `T/T'` graph, EverMemOS scene-level Foresight, A-MEM Zettelkasten linking). For a Flow OS / memory-architect researcher: this is the dimension where ENGRAM (paper) under-engineers most — fine for QA benchmarks where ground truth exists, dangerous in production where the user actually needs to know "wait, why does the assistant think X — has that changed?". If you are building on top of ENGRAM (paper) you almost certainly need to add a provenance / temporal layer separately.

- **(Maintain) There is no eviction, decay, or rewrite policy at all**: The paper has zero maintenance machinery. Records are append-only. Memory governance (redaction, decay, user-facing controls) is explicitly listed in the Discussion as **future work**. So if you're auditing this against the ENGRAM (framework) `M` dimension: it's a green-field — every Mem-system on the wiki (MemoryBank's Ebbinghaus decay, MemOS's MemCube scheduler, ClawVM's validated writeback, Adler's encoding gate) has more `M` than this paper. The implication is that ENGRAM (paper) is best understood as a *retrieval baseline* with strong-typed writes, not as a complete OS.

- **(Counter-thesis to your seed)** Treat the ~99% token reduction claim with care — it's *vs full-context*, not vs other compact systems**: On LongMemEvalS, the comparison is ENGRAM @ ~1.0–1.2K tokens at 71.40% versus full-context @ 101K tokens at 56.20%. This is *not* a head-to-head against Mem0 / MemOS / EverMemOS on LongMemEvalS. The paper deliberately freezes baselines and tests only against full-context for that benchmark to "isolate horizon generalization." So the +15-point gap is impressive but is best read as "selective retrieval beats indiscriminate context-stuffing," not "ENGRAM beats all other memory systems at scale." The Adler paper (`adler-2026-storage-not-memory`) and EverMemOS (`hu-2026-evermemos`) digests already in your wiki are the more interesting head-to-head benchmarks.

- **(Reproducibility win)** Anonymized full implementation + eval harness is published**: `https://anonymous.4open.science/r/engram-68FF/` — this is one of the few memory papers on the wiki that releases both system and eval scripts. If you want a clean baseline to plug into Flow OS's memory testbed (or to fork as a typed-routing skeleton you then bolt provenance + maintenance onto), this is unusually low-friction compared to MemOS or Zep.

## How to Apply It (method)

**Scenario:** You're prototyping a memory layer for Flow OS that needs to retain multi-week founder conversations (Slack DMs, Telegram, and meeting transcripts) and answer questions like "What did Marcus say about pricing last quarter?" or "What's the standard procedure when a customer reports an outage?" You want a baseline that beats naive RAG, doesn't require a graph DB or KV-cache scheduler, and runs in a single container. ENGRAM (paper) is the right minimum-viable architecture to clone; you can layer provenance and decay on top later.

**Steps:**

1. **Stand up a single-file SQLite store with three typed tables** (or one table with a `type` enum + per-type indexes). Schema:

   ```sql
   CREATE TABLE episodic  (id PK, title TEXT, summary TEXT, ts TIMESTAMP, embedding BLOB, user_id TEXT);
   CREATE TABLE semantic  (id PK, fact TEXT, ts TIMESTAMP, embedding BLOB, user_id TEXT);
   CREATE TABLE procedural(id PK, title TEXT, content TEXT, ts TIMESTAMP, embedding BLOB, user_id TEXT);
   ```

   Use `sqlite-vec` or store embeddings as `BLOB` and do similarity in Python — at LoCoMo scale, brute-force cosine is fine.

2. **Implement the router as a single small-LLM call returning a 3-bit mask.** Use this prompt verbatim:

   ```
   Given this message, determine which storage types are most relevant:
   Message: {message}
   Storage types:
     • episodic: Event and experiences with temporal context (a personal diary of events that is timelined)
     • semantic: Facts, observations, preferences (only route to this if the message reveals a non-event fact or preference about a person, place, or thing)
     • procedural: How-to information, processes
   Determine which types are relevant for this message.
   ```

   A turn can route to multiple stores (e.g., "I always check the dashboard at 9am" → episodic *and* procedural).

3. **For each store the router selected, run the corresponding extractor.** Use the paper's three prompts (full text in §"Extracted Prompts" below):
   - Episodic → returns `{title, summary, timestamp}` JSON. Critically: infer the *event* timestamp from message content + conversation timestamp, not the message timestamp itself ("yesterday" with conv-ts of 2026-05-13 → event-ts 2026-05-12).
   - Semantic → returns `{fact}` JSON. ONE fact per message. Preserve specific nouns verbatim — no generalizing "Marcus Webb" to "the founder".
   - Procedural → returns `{title, content}` JSON.

4. **Embed each record's primary text field** (`summary` for episodic, `fact` for semantic, `content` for procedural) with `text-embedding-3-small` (the paper's choice — cheap, 1536-d). Store the embedding alongside the JSON record.

5. **At query time, embed the question once, then run per-type top-k cosine independently.** Take top-K=25 from EACH store, then merge, dedup, and truncate the combined set back to K=25. Do NOT do a global top-K=25 over the union — that's the no-typed-routing ablation that drops you 31 pts.

6. **Render the prompt with per-speaker memory banks.** Each retrieved record is serialized as `<timestamp>: <text>`. Group by `user_id`. Pass to the answering LLM (paper uses `gpt-4o-mini`) with this answer-generation prompt:

   ```
   You are an intelligent memory assistant tasked with retrieving accurate information from conversation memories.
   You have access to memories from two speakers in a conversation. These memories contain timestamped information that may be relevant to answering the question.
   1. Carefully analyze all provided memories from both speakers.
   2. Pay special attention to the timestamps to determine the answer.
   3. If memories contain contradictory information, prioritize the most recent memory.
   4. Always convert relative time references to specific dates ("last year" → "2025").
   5. Keep the answer concise but preserve nouns exactly as they appear in the memories.
   Memories for {speaker_1_id}: {speaker_1_memories}
   Memories for {speaker_2_id}: {speaker_2_memories}
   Question: {question}
   ```

7. **Set K=25 and leave it there.** The paper's ablation (Appendix A.2) shows accuracy is monotonically increasing in K but marginal token cost explodes past K=30. K=25 returns 12.8 J-points per 1k tokens of evidence; K=30→40 returns 0.29. Only revisit if your domain genuinely needs >80% accuracy and you can afford 4× the prompt tokens.

8. **Evaluate with LLM-as-a-Judge, not F1.** ENGRAM scores 77.55 on LoCoMo by Judge but only 21.08 F1 / 13.31 BLEU-1 — because longer factually-correct answers dilute lexical overlap. Use `gpt-4o-mini` or similar as a binary correctness judge, run 3× and report mean ± std. F1/BLEU are diagnostics, not the metric.

**Expected outcome:** A single-container memory layer that, on LoCoMo-like workloads, beats every commercial / OSS memory system in the public baseline matrix at ~916 mean evidence tokens per question and ~1.5 s median total latency. You'll have a clean substrate to ablate against (your next move: add a Zep-style bi-temporal layer for the `Ground` dimension, or an EverMemOS-style scene consolidator for `Aggregate`). The dangerous thing you will NOT have is any maintenance policy — you'll need to graft that on before this goes near a multi-month production deployment.

## Best Figure

![Figure 1 — System overview of ENGRAM (page 2)](figures/patel-2026-engram-fig.png)

**Image Candidates:**
- Figure 1 (p. 2): System overview — the canonical architecture diagram showing typed routing + per-type top-k + aggregation in one view; conceptually load-bearing for the whole paper.
- Table 1 (p. 6): Cross-system LoCoMo comparison — shows ENGRAM winning every category against MemOS, Mem0, Zep, LangMem, OpenAI memory while using fewest mean evidence tokens; this is the headline result table.
- Table 4 (p. 12, App A.1): The no-typed-routing ablation — single-store variants each drop 10–22 pts and collapsing to one undifferentiated store drops 31 pts to 46.56%; this is the single most important experiment in the paper.

**Best Image:** Figure 1: "System overview of ENGRAM"
**Figure Page:** 2
**Slide caption:** ENGRAM's full architecture in one view — a single LLM router emits a 3-bit type mask per turn, three small extractors produce typed JSON records, all stored in one SQLite database; at query time the system runs per-type top-k cosine, merges/dedups/truncates, and renders speaker-segregated banks into a fixed prompt template.
**Description:** Figure 1 splits cleanly into Memory Creation (top) and Memory Retrieval (bottom). On the creation side, a conversation flows into the Memory Router (step 1), which fans out to three parallel Extractor → Memory Store pipelines for episodic, semantic, and procedural — all writing into a single SQLite Database on the right (step 2). On the retrieval side, a Query is embedded (step 3), used to fetch per-type top-k from the same Database, then Aggregation + Rank + Truncation (step 4) produces a single evidence set that flows to Prompt Injection (step 5) and out as Output Context. The diagram makes the paper's central claim visible in one glance: there is no graph, no scheduler, no reranker — just three buckets, one cosine retriever, and a fixed prompt template.

## What Experts Overlook

The overlooked detail is the **timestamp-disambiguation instruction inside the episodic extractor prompt** (Appendix D.2). The paper makes it look incidental: "Reason carefully about time. Do not blindly copy the input timestamp; infer the event timestamp from the message and context." With two concrete examples: input-ts `10:55 am on 22 July, 2024` + message "I went to Cheesequake park yesterday" ⇒ event-ts `July 21 2024`; same input + message "I went camping in Banff last month" ⇒ event-ts `June 2024`. This is a tiny prompt sub-clause, but it's the reason ENGRAM (paper) does well on LoCoMo's *temporal-reasoning* category (70.79 LLM-Judge) despite having no temporal knowledge graph and no Zep-style bi-temporal `T/T'` layer.

**Why it matters:** Most experts would assume that handling "when did X happen?" questions at long horizons requires a graph schema with explicit temporal edges (Rasmussen 2025 Zep does this; Anokhin 2024 Arigraph does this). What this paper quietly shows is that you can push the temporal disambiguation back to the *write path*, inside the episodic extractor, and have the LLM resolve relative-time phrases to absolute dates before the record is even embedded. The downstream retriever then never sees "yesterday" or "last month" — it sees `July 21 2024` and `June 2024`, which are searchable as exact strings AND embedded as concrete date tokens. The router doesn't need a temporal store; the extractor's prompt has already done the work. This is a case where intelligence at the encode step (`E` in the ENGRAM framework) preempts the need for structure at the network step (`N`). It's the inverse of the Adler 2026 thesis — Adler argues "anything the extractor decides before query is lost forever"; Patel & Patel argue "the extractor can decide *some* things safely because temporal anchoring is query-independent." Both are correct; the question is which class of decisions belongs on which side of the write/read boundary.

**Example of good use:** You're building a Flow OS memory layer for founder conversations across Slack, Telegram, and meeting transcripts. Every time a user says "I'll have the proposal ready by next Friday," your episodic extractor resolves "next Friday" to an absolute date at write time, attaches it as the `timestamp` field, and indexes it. A month later when someone asks "what's the proposal status?", the retriever surfaces a record dated `2026-05-22` with the explicit text, and the answer model can reason about deadline lapsing without a temporal graph anywhere in the stack.

**Example of misapplication:** You faithfully copy the ENGRAM architecture but use a generic extractor prompt that just summarizes the message without the explicit "infer event timestamp from content" instruction. Records get the `message timestamp` as their `timestamp` field. Now a user message at `10:55 am 22 July 2024` saying "yesterday I had lunch with Dana" gets stored as a `July 22` episodic record — and three months later when the user asks "when did I last meet Dana?", the system answers "July 22" instead of "July 21". The error is silent because the embedding still works, lexical search still works, top-k still works — but the data is one day wrong everywhere. This is the failure mode where Adler 2026's concern bites hardest: an extractor that throws away information (here, the disambiguation) before query time corrupts the substrate in a way no retriever can recover. The paper avoids this only because the prompt explicitly tells the extractor to do the disambiguation; lose that one sentence and the architecture quietly degrades on every temporal question.

## Extracted Prompts

**Prompt explanation:** Memory router — the LLM call that emits the 3-bit type mask deciding which of `{episodic, semantic, procedural}` stores a given user turn writes to.

```
Given this message, determine which storage types are most relevant:
Message: {message}
Storage types:
   • episodic: Event and experiences with temporal context (think of this as a personal diary of events that is timelined)
   • semantic: Facts, observations, preferences (only route to this if the message reveals a non-event fact or preference about a person, place, or thing)
   • procedural: How-to information, processes

Determine which types are relevant for this message.
```

**Prompt explanation:** Episodic memory extractor — converts a turn into a structured event record with title, summary, and *inferred event timestamp* (not the message timestamp).

```
You are an intelligent memory assistant tasked with converting a single conversation message into an episodic memory JSON object.
Context
You receive a raw message string and a conversation timestamp. The conversation timestamp reflects when the message was sent, not necessarily when the event occurred. You must infer the actual event time from the message content and conversation context.
Instructions
   1. Preserve specific nouns exactly as written: use exact place names, object/activity names, proper nouns, numbers, and titles verbatim.
   2. Reason carefully about time. Do not blindly copy the input timestamp; infer the event timestamp from the message and context.
   3. Write in third person.
   4. Do not use temporal words in the summary (e.g., "yesterday", "last week").
   5. Return only a single JSON object with keys title, summary, and timestamp.

Approach (think step by step)
   1. Read the message and identify specific entities (names, places, objects) to preserve verbatim.
   2. Extract temporal cues (e.g., "yesterday", "last month", holiday names) and map them to absolute dates based on the conversation timestamp.
   3. If the message implies a date range (e.g., a month without a day), output the most specific resolvable form (e.g., "June 2024").
   4. Form a concise title that includes specific details; then write a one-sentence summary in third person with exact nouns preserved.
   5. Compute the timestamp as the actual event date/time derived from the message (not merely the conversation time).

Timestamp reasoning examples
   • Input timestamp: "10:55 am on 22 July, 2024"; message: "I went to Cheesequake park yesterday with my friends" ⇒ event timestamp: "July 21 2024".
   • Input timestamp: "10:55 am on 22 July, 2024"; message: "I went camping in Banff last month" ⇒ event timestamp: "June 2024".

Inputs
Message: {message}
Conversation Timestamp: {timestamp}
Output (return only this JSON)
{"title": "...", "summary": "...", "timestamp": "..."}
```

**Prompt explanation:** Semantic memory extractor — extracts ONE key fact per message, with strict instructions to preserve specific nouns verbatim (no generalizing).

```
Extract ONE key fact or observation from this message.
CRITICAL: Preserve specific nouns exactly as mentioned. Do NOT generalize or paraphrase:
       • Use exact place names, not generic terms
       • Use exact object/activity names, not categories
       • Use exact relationship terms, not synonyms
       • Keep proper nouns, numbers, and specific terms verbatim

RULES:
       • One sentence with specific details preserved exactly as written
       • Include exact names, places, objects, activities as mentioned
       • Proper nouns must be preserved verbatim
       • Be specific and detailed, avoid generic terms

Message: {message}
Return only a JSON object:
{"fact": "detailed fact with specific nouns preserved exactly"}
```

**Prompt explanation:** Procedural memory extractor — converts how-to / process messages into title + content. Notably terse compared to the episodic prompt.

```
Convert this message into procedural memory format:
Inputs
Message: {message}
Extract
       • title: A title for this procedure/instruction
       • content: The procedural content/steps (can be a string or list of steps)
```

**Prompt explanation:** Answer-generation prompt — given the merged top-k evidence from both speakers' memory banks plus a question, produces the final answer. Notable: explicit "most recent memory wins" conflict-resolution rule, and the instruction to keep answers concise but with verbatim nouns.

```
You are an intelligent memory assistant tasked with retrieving accurate information from conversation memories.
Context
You have access to memories from two speakers in a conversation. These memories contain timestamped information that may be relevant to answering the question.
Instructions
   1. Carefully analyze all provided memories from both speakers.
   2. Pay special attention to the timestamps to determine the answer.
   3. If the question asks about a specific event or fact, look for direct evidence in the memories.
   4. If the memories contain contradictory information, prioritize the most recent memory.
   5. Always convert relative time references to specific dates, months, or years. For example, convert "last year" to "2022" or "two months ago" to "March 2023" based on the memory timestamp. Ignore the original relative phrasing when answering.
   6. Focus only on the content of the memories from both speakers. Do not confuse character names mentioned in memories with the actual users who created those memories.
   7. Keep the answer concise but preserve nouns exactly as they appear in the memories (e.g., use the specific food names given).

Approach (think step by step)
   1. Examine all memories that relate to the question.
   2. Check timestamps and content carefully.
   3. Identify explicit mentions of dates, times, locations, or events that answer the question.
   4. If conversion is needed (e.g., relative → absolute dates), briefly show the calculation.
   5. Formulate a precise, concise answer based solely on evidence in the memories.
   6. Double-check that the answer directly addresses the question.
   7. Ensure the final answer uses specific time references (no vague phrases).

Inputs
Memories for user {speaker_1_user_id}: {speaker_1_memories}
Memories for user {speaker_2_user_id}: {speaker_2_memories}

Question: {question}
```

## Citations

The paper cites 29 references — full structured array in frontmatter. Selected highlights most relevant to the memory-architect lens:

- Maharana et al. 2024 — *Evaluating very long-term conversational memory of llm agents* (LoCoMo benchmark; arxiv 2402.17753). Already on wiki as `maharana-2024-locomo`.
- Wu et al. 2025 — *Longmemeval: Benchmarking chat assistants on long-term interactive memory* (ICLR; arxiv 2410.10813). Already on wiki as `wu-2024-longmemeval`.
- Li et al. 2025 — *Memos: A memory os for ai system* (arxiv 2507.03724). Already on wiki as `li-2025-memos`. ENGRAM's strongest competitor on LoCoMo.
- Chhikara et al. 2025 — *Mem0: Building production-ready ai agents with scalable long-term memory* (arxiv 2504.19413). Already on wiki as `chhikara-2025-mem0`.
- Rasmussen et al. 2025 — *Zep: A temporal knowledge graph architecture for agent memory* (arxiv 2501.13956). Already on wiki as `rasmussen-2025-zep-temporal-kg`.
- Packer et al. 2023 — *Memgpt: Towards llms as operating systems* (arxiv 2307.05030). Already on wiki as `packer-2023-memgpt-os`.
- Lewis et al. 2020 — *Retrieval-augmented generation for knowledge-intensive nlp tasks* (NeurIPS; arxiv 2005.11401). Already on wiki as `lewis-2020-rag-knowledge-nlp`.
- Liu et al. 2023 — *Lost in the middle: How language models use long contexts* (arxiv 2307.03172). Foundational for the "compact context beats stuffed context" half of the paper's argument.
- Tulving 1972 — *Episodic and semantic memory* (Organization of Memory, Academic Press). The cognitive-science source for the type taxonomy.
- Cohen & Squire 1980 — *Preserved learning and retention of pattern-analyzing skill in amnesia: dissociation of knowing how and knowing that* (Science 210). Source for the procedural-vs-declarative split.

## Related Digests

- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall. **Direct counter-thesis.** Adler argues write-time extraction is anti-intelligence and that all hard work should be at query time (lexical+dense fusion, RRF, salience reweight, cross-encoder rerank). Patel & Patel argue typed write-time extraction is the load-bearing decision. Both achieve top-tier LoCoMo accuracy. Read both back-to-back to understand the write/read trade-off frontier in 2025–2026 memory research.
- [[li-2025-memos]] — MemOS: A Memory OS for AI System. ENGRAM's strongest competitor on LoCoMo (72.99 vs 77.55). MemOS adds MemCube abstraction + KV-activation + scheduler; ENGRAM strips them out. The two papers together bound the simplicity-vs-substrate trade-off.
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. ENGRAM beats it 77.55 vs 64.73 with fewer tokens (916 vs 1182). Mem0 is the production-deployed reference; ENGRAM is the research baseline.
- [[rasmussen-2025-zep-temporal-kg]] — Zep: A Temporal Knowledge Graph Architecture for Agent Memory. The graph-heavy alternative; ENGRAM beats it 77.55 vs 42.29 on LoCoMo, suggesting the graph adds latency without accuracy in this benchmark.
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems. The OS-metaphor ancestor of both MemOS and (by negation) ENGRAM. Packer says "make the LLM manage paging"; Patel & Patel say "don't bother".
- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents. The benchmark ENGRAM headlines on.
- [[wu-2024-longmemeval]] — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. The scale stress test where ENGRAM beats full-context by 15 pts at ~1% of the tokens.
- [[hu-2026-evermemos]] — EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning. The other "what if you compile experiences into scenes at write time" thesis. EverMemOS's MemScenes vs ENGRAM's typed records are two different bets on what the right write-time unit is.
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects. The four-network (world/experience/opinion/observation) typed variant. ENGRAM's three (episodic/semantic/procedural) is a simpler taxonomy applied at the storage level rather than the access level.

## Reviewer Notes

**Hallucination severity: Clean.**

Cross-checked against paper:
- All numerical claims (77.55 LoCoMo overall, 46.56 no-typed-routing ablation, 71.40 vs 56.20 on LongMemEvalS, 916 mean tokens, 1.487s p50 latency, K=25 knee with 12.8 → 0.29 J/1k slope, single-store variants 66.60/61.56/55.06, OpenAI memory 52.81, MemOS 72.99, Mem0 64.73, Zep 42.29, LangMem 55.28, 35%+ token reduction, ≈99% reduction on LongMemEvalS, single-session-preference 23.33%→93.33%, 35-session ≈600-turn ≈16K-token LoCoMo structure, 500-question 115K-token LongMemEvalS) verified against Tables 1, 2, 3, 4 and §5.3 in the paper.
- The "MemOS edges ENGRAM on temporal" claim (72.68 vs 70.79) verified from Table 1 temporal-reasoning row.
- The 3-bit router mask and the per-type record schemas `(t,σ,δ,e), (f,δ,e), (t,c,δ,e)` are verbatim from §3.2-3.3.
- All five prompts in §"Extracted Prompts" are verbatim from Appendix D (D.1-D.5).
- The "namespace collision" warning is genuine — Patel & Patel's ENGRAM is named after the neurobiology term "engram" (memory trace, going back to Semon 1904 / Tulving / Squire — they cite Tulving 1972 and Cohen & Squire 1980). The user's ENGRAM framework is a separate coinage extracted from their 2026 meta-analysis of 53 OSS memory systems. There is no relationship; the digest flags this explicitly so memories don't bleed.
- The categorisation of typed routing's mechanism as `E`-encoded but `A`-realized is the digester's analytical framing, not a paper claim — labeled as such in the Key Takeaway.
- Citation count: 29 entries extracted from the bibliography (§References, pp. 10-11). All on-paper; no fabrication.

No urgent rewrite needed.
