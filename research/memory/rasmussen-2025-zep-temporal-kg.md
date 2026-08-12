---
corpus: agentic-memory
kind: paper-digest
slug: rasmussen-2025-zep-temporal-kg
title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
authors:
  - "Preston Rasmussen"
  - "Pavlo Paliychuk"
  - "Travis Beauvais"
  - "Jack Ryan"
  - "Daniel Chalef"
year: 2025
publication_date: "2025-01"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2501.13956"
doi: null
arxiv_id: "2501.13956"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Adding a bi-temporal layer to the memory graph — every fact carries both when-it-held-true (T) and when-the-system-learned-it (T') — is what lets Zep handle knowledge that changes mid-conversation; without it, contradictions either silently overwrite each other or pile up as duplicates, and the model gets confused about which fact is currently valid."
topics:
  - agent-memory
  - knowledge-graph
  - temporal-reasoning
  - bi-temporal-model
  - graph-rag
  - long-conversation
  - llm-evaluation
  - hybrid-retrieval
  - reranking
  - edge-invalidation
  - community-detection
  - longmemeval
  - dmr-benchmark
  - encoding-gate
  - graph-shape
tags:
  - paper
  - memory-architecture
  - zep
  - graphiti
  - knowledge-graph
  - temporal
  - bi-temporal
  - production-ai
  - latency
  - reranking
entities:
  - rasmussen-preston
  - paliychuk-pavlo
  - beauvais-travis
  - ryan-jack
  - chalef-daniel
related_digests:
  - packer-2023-memgpt-os
  - wu-2024-longmemeval
  - chhikara-2025-mem0
  - latimer-2025-hindsight-memory
  - adler-2026-storage-not-memory
  - maharana-2024-locomo
  - wang-2026-memmachine
citations:
  - title: "Attention Is All You Need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1706.03762"
  - title: "A statistical interpretation of term specificity and its application in retrieval"
    authors: ["K. Sparck Jones"]
    year: 1972
    venue: "Journal of Documentation"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Charles Packer", "Sarah Wooders", "Kevin Lin", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
    authors: ["Darren Edge", "Ha Trinh", "Newman Cheng", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2404.16130"
  - title: "Zep: Long-term memory for AI agents"
    authors: ["Zep"]
    year: 2024
    venue: "commercial product"
    doi: null
    url: "https://www.getzep.com"
    arxiv_id: null
  - title: "Graphiti: Temporal knowledge graphs for agentic applications"
    authors: ["Zep"]
    year: 2024
    venue: "open source"
    doi: null
    url: "https://github.com/getzep/graphiti"
    arxiv_id: null
  - title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2410.10813"
  - title: "The relationship between semantic and episodic memory: Exploring the effect of semantic neighbourhood density on episodic memory"
    authors: ["Wong Gonzalez", "Daniela"]
    year: 2018
    venue: "PhD thesis, University of Windsor"
    doi: null
    url: null
    arxiv_id: null
  - title: "AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents"
    authors: ["Petr Anokhin", "Nikita Semenov", "Artyom Sorokin", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2407.04363"
  - title: "HiQA: A Hierarchical Contextual Augmentation RAG for Multi-Documents QA"
    authors: ["Xinyue Chen", "Pengyu Gao", "Jiangjiang Song", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "HIRO: Hierarchical Information Retrieval Optimization"
    authors: ["Krish Goel", "Mahek Chandak"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    authors: ["Noah Shinn", "Federico Cassano", "Edward Berman", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2303.11366"
  - title: "Learning from labeled and unlabeled data with label propagation"
    authors: ["Xiaojin Zhu", "Zoubin Ghahramani"]
    year: 2002
    venue: "Technical report, CMU"
    doi: null
    url: null
    arxiv_id: null
  - title: "From Louvain to Leiden: guaranteeing well-connected communities"
    authors: ["V. A. Traag", "L. Waltman", "N. J. van Eck"]
    year: 2019
    venue: "Scientific Reports 9, 5233"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neo4j — the world's leading graph database"
    authors: ["Neo4j"]
    year: 2012
    venue: "commercial product"
    doi: null
    url: null
    arxiv_id: null
  - title: "Apache Lucene — Scoring"
    authors: ["Apache Software Foundation"]
    year: 2011
    venue: "documentation"
    doi: null
    url: null
    arxiv_id: null
  - title: "LightRAG: Simple and Fast Retrieval-Augmented Generation"
    authors: ["Zirui Guo", "Lianghao Xia", "Yanhua Yu", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2410.05779"
  - title: "Vector Search with OpenAI Embeddings: Lucene Is All You Need"
    authors: ["Jimmy Lin", "Ronak Pradeep", "Tommaso Teofili", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2308.14963"
  - title: "Distill-SynthKG: Distilling Knowledge Graph Synthesis Workflow for Improved Coverage and Efficiency"
    authors: ["Prafulla Kumar Choubey", "Xin Su", "Man Luo", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reciprocal Rank Fusion outperforms Condorcet and individual rank learning methods"
    authors: ["Gordon V. Cormack", "Charles L. A. Clarke", "Stefan Buettcher"]
    year: 2009
    venue: "SIGIR '09"
    doi: null
    url: null
    arxiv_id: null
  - title: "The use of MMR, diversity-based reranking for reordering documents and producing summaries"
    authors: ["Jaime Carbonell", "Jade Goldstein"]
    year: 1998
    venue: "SIGIR '98"
    doi: null
    url: null
    arxiv_id: null
  - title: "Beyond Goldfish Memory: Long-Term Open-Domain Conversation"
    authors: ["Jing Xu", "Arthur Szlam", "Jason Weston"]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2107.07567"
  - title: "Making Large Language Models a Better Foundation for Dense Retrieval"
    authors: ["Chaofan Li", "Zheng Liu", "Shitao Xiao", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation"
    authors: ["Jianlv Chen", "Shitao Xiao", "Peitian Zhang", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Triplex: A SOTA LLM for Knowledge Graph Construction"
    authors: ["Shreyas Pimpalgaonkar", "Nolan Tremelling", "Owen Colegrove"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "GraphReader: Building Graph-based Agent to Enhance Long-Context Abilities of Large Language Models"
    authors: ["Shilong Li", "Yancheng He", "Hangyu Guo", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "FinanceBench: A New Benchmark for Financial Question Answering"
    authors: ["Pranab Islam", "Anand Kannappan", "Douwe Kiela", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models"
    authors: ["Nandan Thakur", "Nils Reimers", "Andreas Rücklé", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2104.08663"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "LongMemEvals headline results + per-question-type breakdown (Tables 2 and 3)"
  page: 7
  image_path: "figures/rasmussen-2025-zep-temporal-kg-fig.png"
---

# Zep: A Temporal Knowledge Graph Architecture for Agent Memory

**Authors:** Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais, Jack Ryan, Daniel Chalef (Zep AI)
**Published:** 2025-01 · [Source](https://arxiv.org/abs/2501.13956)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Zep is a production memory service for LLM agents built on Graphiti, a temporally-aware knowledge graph engine with three hierarchical tiers — episodes (raw messages, JSON, text), semantic entities/facts (LLM-extracted with reflexion-style verification, 1024-d BGE-m3 embeddings, hybrid Lucene+cosine+BFS search, deduplicated against existing nodes via an LLM resolver), and communities (label-propagation clusters with map-reduce summaries). Its central novelty is a bi-temporal model: every edge carries both `t_valid`/`t_invalid` for when a fact actually held true (timeline T) and `t'_created`/`t'_expired` for when the system ingested it (timeline T'), and an LLM contradiction-checker invalidates outdated edges instead of overwriting them. Retrieval is a three-step `f(α) = χ(ρ(ϕ(α)))` pipeline — multi-method search (BM25 + cosine + breadth-first over the graph), reranking (RRF, MMR, graph-distance, episode-mentions, or LLM cross-encoder), and a constructor that emits a FACTS+ENTITIES context string with date ranges. On the MemGPT Deep Memory Retrieval benchmark (500 multi-session chats, 60 messages each) Zep edges MemGPT 94.8% vs 93.4% with gpt-4-turbo and 98.2% vs 98.0% (full-context baseline) with gpt-4o-mini — improvements the authors acknowledge are marginal because the conversations fit in-context. On LongMemEval (avg 115k-token conversations) Zep delivers 71.2% vs 60.2% full-context (gpt-4o), a 90% latency reduction (2.58s vs 28.9s), and shrinks the context from 115k to 1.6k tokens; the largest gains are on single-session-preference (+184% with gpt-4o), temporal-reasoning (+38%), and multi-session (+31%) — but performance regresses on single-session-assistant by 17.7%, an unresolved failure mode the authors flag.

## Key Takeaway

The hot take isn't that knowledge graphs beat flat memory — it's that the *time dimension* of the graph is what actually does the work. Most "graph memory" systems treat the graph as a static index that gets updated in place, which silently destroys the past whenever a fact changes. Zep separates two timelines — when a fact was true in the world, and when the system learned about it — so when "I work at Google" gets contradicted by "I just joined Anthropic," the old edge isn't deleted; its `t_invalid` is set to the moment of the new edge's `t_valid`. This lets the agent answer both "where do you work now?" and "where did you work last year?" from the same graph, which a non-temporal graph or a summary-based memory simply cannot do without rebuilding from raw episodes.

## Implications

- **The bi-temporal split is the cheapest contradiction-handling primitive you'll find [E + G + M]**: Most agent-memory systems either silently overwrite (losing history) or accumulate duplicates (forcing the retriever to disambiguate). Zep's two-timeline design adds four datetime fields per edge and an LLM-driven contradiction check at write time — a small schema cost that gives you provenance, audit, and time-travel queries for free. If you're building a long-running agent, copy this pattern even if you don't copy the graph.

- **Hybrid retrieval is non-negotiable for graph memory [R]**: Zep runs three search functions in parallel — Lucene BM25 (word similarity), cosine on 1024-d BGE-m3 embeddings (semantic similarity), and breadth-first traversal (contextual/graph similarity) — then reranks. Each catches a different failure mode. The BFS step is the most underrated: it lets recent episodes seed the search, so "what did we just talk about" gets natural recency without a separate decay model.

- **Write-time work is real, and the paper doesn't quantify it [E + cost]**: Every ingested message triggers entity extraction with reflexion verification, entity embedding, hybrid search for duplicates, LLM-driven entity resolution, fact extraction, fact embedding, fact deduplication, temporal extraction, and LLM-driven contradiction detection. That's at least 5–7 LLM calls per message turn. The paper shows that the *retrieval* latency drops 90% (because the context shrinks from 115k to 1.6k tokens), but the *ingestion* cost is reported nowhere — the related Mem0 paper [[chhikara-2025-mem0]] independently measured Zep at 600k+ tokens per LOCOMO conversation, ~85× Mem0's cost. Budget for it.

- **Use Cypher templates, not LLM-generated queries [G + M]**: Zep deliberately writes to Neo4j through pre-defined Cypher rather than letting the LLM generate database queries. This is a "trust boundary" choice — the LLM proposes nodes/edges/facts, but a deterministic layer commits them with a fixed schema. Anyone building an agent memory should adopt this pattern; LLM-generated SQL/Cypher is where silent corruption enters production systems.

- **Reranker zoo beats reranker choice [R]**: Zep doesn't pick one reranker; it offers five (RRF, MMR, graph-distance from a centroid node, episode-mention frequency, and a cross-encoder). The "episode-mentions" reranker is the most novel — it turns recency-of-mention into a free relevance signal without needing time-decay tuning. The graph-distance reranker lets you "anchor" a query to a user or topic node, which is exactly what production multi-tenant agents need.

- **DMR is dead as a benchmark; use LongMemEval [evaluation]**: The paper's own analysis (Section 4.2) tears down DMR — single-turn fact retrieval on 60-message conversations that any modern LLM solves with full-context dump (98.0% baseline). The 0.4-0.2 point gap over full-context is "marginal" by the authors' own admission. The real story is LongMemEval at 115k tokens with six question types, where the gap stretches to +11 points and the latency story turns favorable.

- **The single-session-assistant regression is the most useful number in the paper [failure mode]**: Zep *loses* 17.7% on single-session-assistant questions with gpt-4o. The authors don't explain it, but the most likely cause is that "what did the assistant say" requires the verbatim utterance, which graph extraction destroys — you get the entity/relation, not the wording. Any extraction-based memory will have this failure mode. Adler 2026 [[adler-2026-storage-not-memory]] articulates the general principle: anything you discard at write time is unrecoverable at query time.

- **Communities are an experiment, not a result [A]**: Zep builds a third subgraph of communities via label-propagation (chosen over Leiden for cheap incremental updates) with map-reduce summaries. The paper *describes* this layer in detail but never reports a benchmark with vs without communities — so we don't know whether communities contribute to the 71.2% score or whether they're scaffolding for future work. Treat this layer as unvalidated.

## How to Apply It (method)

**Scenario:** You're running an AI workforce manager (Flow OS) where one agent persistently supports a customer over months. The customer says "I'm head of product at Acme" in January, then in April "I just moved to Nova as VP eng." Without temporal memory the agent either (a) silently forgets January, (b) duplicates Acme/Nova as parallel facts, or (c) hallucinates that the customer holds both roles. You want the agent to answer correctly: "You're VP eng at Nova as of April; you were head of product at Acme until April."

**Steps:**

1. **Pick a graph store with timestamped edges**: Neo4j (Zep's choice) gives you Cypher, full-text Lucene, and vector indexes in one engine. Postgres + pgvector + a junction table also works if you prefer SQL. Whatever you pick, every edge gets four datetime fields: `t_valid`, `t_invalid`, `t_created`, `t_expired`.

2. **Ingest each turn as an Episode with a reference timestamp**: Store the raw message verbatim (don't summarize on the write path). Attach the `tref` of when the message was sent. Episodes are append-only and non-lossy — they're your audit trail.

3. **Extract entities with reflexion-style verification**: Run an LLM pass that names speaker first, then all other significant entities. Feed it the last 4 messages (2 conversation turns) for context. Add a second "reflection" pass that asks the LLM to check coverage and hallucination before committing:

   ```
   <PREVIOUS MESSAGES>
   {previous_messages}
   </PREVIOUS MESSAGES>
   <CURRENT MESSAGE>
   {current_message}
   </CURRENT MESSAGE>
   Given the above conversation, extract entity nodes from the CURRENT MESSAGE that are
   explicitly or implicitly mentioned:
   Guidelines:
   1. ALWAYS extract the speaker/actor as the first node.
   2. Extract other significant entities, concepts, or actors mentioned.
   3. DO NOT create nodes for relationships or actions.
   4. DO NOT create nodes for temporal information like dates, times or years.
   5. Be as explicit as possible in your node names, using full names.
   ```

4. **Resolve each new entity against existing graph entities**: Embed the entity name in a 1024-d vector (BGE-m3). Run cosine + Lucene full-text search to surface candidates. Pass candidates + context to an LLM resolver that returns `is_duplicate: true|false` and the canonical name:

   ```
   <EXISTING NODES>
   {existing_nodes}
   </EXISTING NODES>
   <NEW NODE>
   {new_node}
   </NEW NODE>
   Task:
   1. If the New Node represents the same entity as any node in Existing Nodes,
      return 'is_duplicate: true'. Otherwise, return 'is_duplicate: false'
   2. If is_duplicate is true, also return the uuid of the existing node
   3. If is_duplicate is true, return a name for the node that is the most complete full name.
   ```

5. **Extract facts as typed edges between entity pairs**: Each fact is `(entity_a, RELATION_TYPE, entity_b)` plus a verbose human-readable fact string. Embed the fact string. Search for duplicate edges *between the same entity pair only* (not all edges) — this prevents bad merges across unrelated entities.

6. **Extract temporal info from the fact text using `tref` as anchor**:

   ```
   <FACT>
   {fact}
   </FACT>
   <REFERENCE TIMESTAMP>
   {reference_timestamp}
   </REFERENCE TIMESTAMP>
   Definitions:
   - valid_at: when the relationship became true.
   - invalid_at: when the relationship stopped being true.
   Use ISO 8601 format. Don't infer dates from related events. Use reference timestamp for
   relative mentions ("two weeks ago"). If only a year is given, use January 1st.
   ```

7. **Run contradiction detection before writing the edge**: For each candidate new edge, fetch semantically related existing edges between the same entity pair. Pass them to an LLM that determines if the new edge contradicts the old one. If yes, set the old edge's `t_invalid` to the new edge's `t_valid` (do NOT delete the old edge — its history is the point).

8. **At query time, run three searches in parallel**: BM25 over fact/entity-name fields, cosine over fact/entity embeddings, breadth-first over the graph (seeded by recent episodes or a centroid node). Pull the top 20 candidates.

9. **Rerank**: Start with Reciprocal Rank Fusion as a default. For UI surfaces where freshness matters, add the episode-mentions reranker. For multi-tenant queries, add the graph-distance reranker anchored to the user node. Reserve the LLM cross-encoder for high-stakes queries — it's accurate but the most expensive component in the stack.

10. **Construct the context string**: Emit facts with their date ranges and entities with their summaries:

    ```
    FACTS and ENTITIES represent relevant context to the current conversation.
    These are the most relevant facts and their valid date ranges. If the fact is about
    an event, the event takes place during this time.
    format: FACT (Date range: from - to)
    <FACTS>
    {facts}
    </FACTS>
    These are the most relevant entities
    ENTITY_NAME: entity summary
    <ENTITIES>
    {entities}
    </ENTITIES>
    ```

11. **Run nightly community refreshes**: Use label propagation (cheaper than Leiden, supports incremental updates). Generate community summaries via map-reduce. Generate community *names* containing key terms for the cosine-similarity search path.

**Expected outcome:** Your agent answers "where do you work?" with the current employer, and "where did you work in February?" with the historical employer — from the same graph, with citations back to the original Episode that established each fact. Retrieval drops to ~1–2k tokens of context per query (vs 100k+ for full-conversation dumps), latency drops by an order of magnitude, and contradictions surface as visible edge-invalidations in the audit trail rather than silent overwrites.

## Best Figure

![Figure — LongMemEvals headline results + per-question-type breakdown (Tables 2 and 3, page 7)](figures/rasmussen-2025-zep-temporal-kg-fig.png)

**Image Candidates:**
- Table 1 (p. 6): Deep Memory Retrieval scores — but DMR is the weak benchmark; the deltas are tiny (94.8 vs 94.4) and the authors themselves call it inadequate.
- Table 2 (p. 7): LongMemEvals headline — accuracy, latency, IQR, and avg context tokens for full-context vs Zep across two models. Shows the 90% latency drop and 115k → 1.6k context shrink.
- Table 3 (p. 7): LongMemEvals per-question-type breakdown — the only place that reveals where Zep wins (preference, temporal, multi-session) and where it loses (single-session-assistant -17.7%).

**Best Image:** Tables 2 + 3 combined (page 7). Table 2 alone gives the headline number; Table 3 alone gives the diagnostic detail; together they tell the full story — the headline gains AND the regression that lets you understand the trade-off Zep is making.

Tables 2 and 3 together establish two things. First, Zep is dramatically faster than dumping the full 115k-token conversation into context — 2.58 s vs 28.9 s on gpt-4o, a 90% reduction, while *also* improving accuracy from 60.2% to 71.2%. Second, that headline accuracy gain is unevenly distributed across question types: Zep wins big on preference (+184% with gpt-4o), temporal-reasoning (+38%), multi-session (+31%), and user-recall (+14%), but loses on single-session-assistant (-17.7%) and shows mixed results on knowledge-update with the smaller model. This is exactly the trade-off you'd expect from an extraction-based memory: structured facts crush queries that require synthesis across sessions, but lose to raw context when you need the verbatim assistant utterance from a specific session.

## What Experts Overlook

The overlooked detail is not the knowledge graph and not even the bi-temporal model — it's the *edge-invalidation protocol* in §2.2.3. When a new fact arrives that contradicts an old one, Zep does not delete the old edge. It also does not write a "version 2" edge alongside it. Instead, it runs an LLM check against semantically-related existing edges between the same entity pair, identifies the temporal overlap, and sets the old edge's `t_invalid` to the new edge's `t_valid`. The old edge persists in the graph forever — it's no longer "current" but it's still queryable. This is the engineering primitive that lets the same graph answer "where do you work now?" and "where did you work last year?" without keeping two parallel databases.

**Why it matters:** Most graph memory systems treat the graph as a state, not a history — they MERGE on conflict, which destroys the past. Most flat memory systems treat the memory as an append log — they keep everything but force the retriever to disambiguate. Zep's invalidation protocol is a middle path: append-only on the write side (no edge ever gets deleted), state-like on the read side (queries filter by current time). This is the same trick that bi-temporal SQL data warehouses (Snowflake, Postgres temporal tables) use, applied to LLM agent memory. The cost is exactly one LLM contradiction-check per write — cheap by AI standards, expensive by database standards.

**Example of good use:** A customer-success agent watching a long-running B2B account. The contact's role changes from "manager" to "director" to "VP" over 18 months. With invalidation, the agent answers "current title" correctly today AND can compose a thank-you note for the promotion path: "Congrats on your promotion from director to VP — I remember you were a manager when we first spoke." All three role-edges still exist in the graph; only the current-time filter changes.

**Example of misapplication:** Treating contradiction detection as a *cleanup* step run nightly across the whole graph (rather than at write time, edge-by-edge, within the same entity pair). This is the easy mistake to make if you're building a Zep clone — "we'll batch the LLM calls to save cost." The break case: the agent ingests "Acme just acquired Beta Corp" at 09:00 and "Beta Corp is hiring CTOs" at 09:30. By the time the nightly job runs, the agent has already given a customer false information about Beta Corp being independent. The whole point of the protocol is that it runs synchronously *during ingestion*, scoped to the entity pair so the LLM context stays tiny. Skip the per-write check and you've just rebuilt a state-overwriting system with extra metadata.

## Extracted Prompts

**Prompt explanation:** Entity extraction — pulls named entities from the current message, anchored by 4 messages of conversational context, with strict rules about what counts as an entity.

```
<PREVIOUS MESSAGES>
{previous_messages}
</PREVIOUS MESSAGES>
<CURRENT MESSAGE>
{current_message}
</CURRENT MESSAGE>
Given the above conversation, extract entity nodes from the CURRENT MESSAGE that are explicitly or implicitly mentioned:
Guidelines:
1. ALWAYS extract the speaker/actor as the first node. The speaker is the part before the colon in each line of dialogue.
2. Extract other significant entities, concepts, or actors mentioned in the CURRENT MESSAGE.
3. DO NOT create nodes for relationships or actions.
4. DO NOT create nodes for temporal information like dates, times or years (these will be added to edges later).
5. Be as explicit as possible in your node names, using full names.
6. DO NOT extract entities mentioned only
```

**Prompt explanation:** Entity resolution — decides whether a newly extracted entity is a duplicate of an existing graph node, and if so, returns the canonical name.

```
<PREVIOUS MESSAGES>
{previous_messages}
</PREVIOUS MESSAGES>
<CURRENT MESSAGE>
{current_message}
</CURRENT MESSAGE>
<EXISTING NODES>
{existing_nodes}
</EXISTING NODES>
Given the above EXISTING NODES, MESSAGE, and PREVIOUS MESSAGES. Determine if the NEW NODE extracted from the conversation is a duplicate entity of one of the EXISTING NODES.
<NEW NODE>
{new_node}
</NEW NODE>
Task:
1. If the New Node represents the same entity as any node in Existing Nodes, return 'is_duplicate: true' in the response. Otherwise, return 'is_duplicate: false'
2. If is_duplicate is true, also return the uuid of the existing node in the response
3. If is_duplicate is true, return a name for the node that is the most complete full name.
Guidelines:
1. Use both the name and summary of nodes to determine if the entities are duplicates, duplicate nodes may have different names
```

**Prompt explanation:** Fact extraction — extracts typed relationship edges between already-identified entities, with a concise all-caps relation type and a verbose fact string.

```
<PREVIOUS MESSAGES>
{previous_messages}
</PREVIOUS MESSAGES>
<CURRENT MESSAGE>
{current_message}
</CURRENT MESSAGE>
<ENTITIES>
{entities}
</ENTITIES>
Given the above MESSAGES and ENTITIES, extract all facts pertaining to the listed ENTITIES from the CURRENT MESSAGE.
Guidelines:
1. Extract facts only between the provided entities.
2. Each fact should represent a clear relationship between two DISTINCT nodes.
3. The relation_type should be a concise, all-caps description of the fact (e.g., LOVES, IS_FRIENDS_WITH, WORKS_FOR).
4. Provide a more detailed fact containing all relevant information.
5. Consider temporal aspects of relationships when relevant.
```

**Prompt explanation:** Fact (edge) resolution — checks whether a newly extracted edge duplicates an existing edge between the same entity pair, returning the canonical uuid.

```
Given the following context, determine whether the New Edge represents any of the edges in the list of Existing Edges.
<EXISTING EDGES>
{existing_edges}
</EXISTING EDGES>
<NEW EDGE>
{new_edge}
</NEW EDGE>
Task:
1. If the New Edges represents the same factual information as any edge in Existing Edges, return 'is_duplicate: true' in the response. Otherwise, return 'is_duplicate: false'
2. If is_duplicate is true, also return the uuid of the existing edge in the response
Guidelines:
1. The facts do not need to be completely identical to be duplicates, they just need to express the same information.
```

**Prompt explanation:** Temporal extraction — parses the fact text to extract `valid_at` and `invalid_at` datetimes, resolving relative phrases ("two weeks ago") against the message's reference timestamp.

```
<PREVIOUS MESSAGES>
{previous_messages}
</PREVIOUS MESSAGES>
<CURRENT MESSAGE>
{current_message}
</CURRENT MESSAGE>
<REFERENCE TIMESTAMP>
{reference_timestamp}
</REFERENCE TIMESTAMP>
<FACT>
{fact}
</FACT>
IMPORTANT: Only extract time information if it is part of the provided fact. Otherwise ignore the time mentioned.
Make sure to do your best to determine the dates if only the relative time is mentioned. (eg 10 years ago, 2 mins ago) based on the provided reference timestamp
If the relationship is not of spanning nature, but you are still able to determine the dates, set the valid_at only.
Definitions:
- valid_at: The date and time when the relationship described by the edge fact became true or was established.
- invalid_at: The date and time when the relationship described by the edge fact stopped being true or ended.
Task:
Analyze the conversation and determine if there are dates that are part of the edge fact. Only set dates if they explicitly relate to the formation or alteration of the relationship itself.
Guidelines:
1. Use ISO 8601 format (YYYY-MM-DDTHH:MM:SS.SSSSSSZ) for datetimes.
2. Use the reference timestamp as the current time when determining the valid_at and invalid_at dates.
3. If the fact is written in the present tense, use the Reference Timestamp for the valid_at date
4. If no temporal information is found that establishes or changes the relationship, leave the fields as null.
5. Do not infer dates from related events. Only use dates that are directly stated to establish or change the relationship.
6. For relative time mentions directly related to the relationship, calculate the actual datetime based on the reference timestamp.
7. If only a date is mentioned without a specific time, use 00:00:00 (midnight) for that date.
8. If only year is mentioned, use January 1st of that year at 00:00:00.
9. Always include the time zone offset (use Z for UTC if no specific time zone is mentioned).
```

**Prompt explanation:** Retrieval context constructor — the template Zep emits to the agent, listing relevant facts with date ranges and entities with summaries.

```
FACTS and ENTITIES represent relevant context to the current conversation.
These are the most relevant facts and their valid date ranges. If the fact is about an event, the event takes place during this time.
format: FACT (Date range: from - to)
<FACTS>
{facts}
</FACTS>
These are the most relevant entities
ENTITY_NAME: entity summary
<ENTITIES>
{entities}
</ENTITIES>
```

## Citations

- **Packer et al. 2024** — MemGPT: Towards LLMs as Operating Systems ([[packer-2023-memgpt-os]])
- **Wu et al. 2024** — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory ([[wu-2024-longmemeval]])
- **Edge et al. 2024** — From Local to Global: A Graph RAG Approach to Query-Focused Summarization (the GraphRAG paper)
- **Anokhin et al. 2024** — AriGraph: Knowledge graph world models with episodic memory for LLM agents
- **Guo et al. 2024** — LightRAG: Simple and Fast Retrieval-Augmented Generation
- **Choubey et al. 2024** — Distill-SynthKG: Distilling knowledge graph synthesis workflow for improved coverage and efficiency
- **Shinn et al. 2023** — Reflexion: Language agents with verbal reinforcement learning (source of the extraction-verification technique)
- **Cormack et al. 2009** — Reciprocal Rank Fusion (one of Zep's rerankers)
- **Carbonell & Goldstein 1998** — MMR: diversity-based reranking (another Zep reranker)
- **Xu et al. 2021** — Beyond Goldfish Memory (source of the Multi-Session Chat dataset used by DMR)

Full citation list (27 references) in frontmatter.

## Related Digests

- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems (the system Zep beats 94.8 vs 93.4 on DMR, and frames itself against)
- [[wu-2024-longmemeval]] — LongMemEval benchmark (Zep's headline evaluation surface)
- [[chhikara-2025-mem0]] — Mem0: argues against heavy graph memory; independently measures Zep at ~85× Mem0's token cost
- [[latimer-2025-hindsight-memory]] — Hindsight: a four-typed-network alternative to Zep's three-tier graph
- [[adler-2026-storage-not-memory]] — Adler 2026: articulates why write-time extraction (like Zep's) loses information vs raw-event storage
- [[maharana-2024-locomo]] — LOCOMO benchmark (the conversation dataset Mem0 uses to compare against Zep)
- [[wang-2026-memmachine]] — MemMachine: a ground-truth-preserving alternative to Zep's extracted-only model

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim, methodology description, and prompt in this digest is sourced directly from the paper. The most load-bearing numbers (94.8% / 93.4% DMR; 71.2% / 60.2% LongMemEval; 2.58 s / 28.9 s latency; 115k → 1.6k tokens; -17.7% single-session-assistant) are verbatim from Tables 1, 2, 3. Implementation details (n=4 context window for extraction, 1024-d BGE-m3 embeddings, BGE-m3 reranker, gpt-4o-mini for graph construction, label propagation over Leiden, Cypher templates over LLM-generated queries, three subgraph tiers, three search functions, five rerankers) all appear in §2 and §3. The bi-temporal model details (four datetime fields, two timelines T and T') are from §2.2.3. The cross-paper claim about Mem0 measuring Zep at "600k+ tokens / 85×" is sourced from [[chhikara-2025-mem0]]'s digest, not from the Zep paper itself — flagged as cross-reference, not an original Zep claim.
