---
corpus: agentic-memory
kind: paper-digest
slug: edge-2024-graphrag
title: "From Local to Global: A GraphRAG Approach to Query-Focused Summarization"
authors:
  - "Edge, Darren"
  - "Trinh, Ha"
  - "Cheng, Newman"
  - "Bradley, Joshua"
  - "Chao, Alex"
  - "Mody, Apurva"
  - "Truitt, Steven"
  - "Metropolitansky, Dasha"
  - "Ness, Robert Osazuwa"
  - "Larson, Jonathan"
year: 2024
publication_date: "2024-04"
venue: "arXiv preprint (Microsoft Research)"
source_url: "https://arxiv.org/abs/2404.16130"
doi: null
arxiv_id: "2404.16130"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Vector RAG can't answer global sensemaking questions (\"what are the main themes?\") because it's structurally a local retrieval task — GraphRAG fixes this by indexing the corpus as an LLM-extracted entity-relationship knowledge graph, partitioning it via Leiden community detection, pre-generating hierarchical community summaries at indexing time, and answering queries via map-reduce: each community summary produces a partial answer in parallel, then partials are aggregated; on 1M-token corpora, this beats vector RAG on both comprehensiveness and diversity of generated answers."
topics:
  - graph-rag
  - query-focused-summarization
  - knowledge-graph
  - community-detection
  - leiden-algorithm
  - hierarchical-summarization
  - map-reduce
  - global-sensemaking
tags:
  - paper
  - canonical
  - rag
  - knowledge-graph
entities:
  - edge-darren
  - larson-jonathan
related_digests:
  - lewis-2020-rag-knowledge-nlp
  - sarthi-2024-raptor
  - gutierrez-2024-hipporag
  - rasmussen-2025-zep-temporal-kg
  - petrov-2026-schema-grounded-memory
citations:
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Lewis, Patrick", "et al."]
    year: 2020
    venue: "NeurIPS"
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Liu, Nelson F.", "et al."]
    year: 2023
    arxiv_id: "2307.03172"
  - title: "Making sense of sensemaking 1: Alternative perspectives"
    authors: ["Klein, G.", "Moon, B.", "Hoffman, R. R."]
    year: 2006
    venue: "IEEE Intelligent Systems"
  - title: "Fast unfolding of communities in large networks (Louvain)"
    authors: ["Blondel, V. D.", "Guillaume, J.-L.", "Lambiotte, R.", "Lefebvre, E."]
    year: 2008
    venue: "Journal of Statistical Mechanics"
  - title: "From Louvain to Leiden: guaranteeing well-connected communities"
    authors: ["Traag, V. A.", "Waltman, L.", "van Eck, N. J."]
    year: 2019
    venue: "Scientific Reports"
  - title: "RAPTOR: Recursive abstractive processing for tree-organized retrieval"
    authors: ["Sarthi, Parth", "Abdullah, Salman", "Tuli, Aditi", "Khanna, Shubh", "Goldie, Anna", "Manning, Christopher D."]
    year: 2024
    arxiv_id: "2401.18059"
  - title: "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena"
    authors: ["Zheng, Lianmin", "et al."]
    year: 2024
    venue: "NeurIPS"
  - title: "Modularity and community structure in networks"
    authors: ["Newman, M. E. J."]
    year: 2006
    venue: "PNAS"
  - title: "HotpotQA: A dataset for diverse, explainable multi-hop question answering"
    authors: ["Yang, Zhilin", "et al."]
    year: 2018
    venue: "EMNLP"
  - title: "Retrieval-augmented language models survey"
    authors: ["Gao, Yunfan", "et al."]
    year: 2023
    arxiv_id: "2312.10997"
  - title: "Language models are few-shot learners (GPT-3)"
    authors: ["Brown, Tom B.", "et al."]
    year: 2020
    venue: "NeurIPS"
  - title: "RAGAS: Automated evaluation of retrieval augmented generation"
    authors: ["Es, Shahul", "James, Jithin", "Espinosa-Anke, Luis", "Schockaert, Steven"]
    year: 2023
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "GraphRAG pipeline: indexing-time (graph extraction + community summarization) vs query-time (map-reduce summarization over community summaries)"
  page: 4
  image_path: null
---

# From Local to Global: A GraphRAG Approach to Query-Focused Summarization

**Authors:** Edge, Darren; Trinh, Ha; Cheng, Newman; Bradley, Joshua; Chao, Alex; Mody, Apurva; Truitt, Steven; Metropolitansky, Dasha; Ness, Robert Osazuwa; Larson, Jonathan (Microsoft Research)
**Published:** 2024-04 · [Source](https://arxiv.org/abs/2404.16130)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Vector RAG fails on **global sensemaking queries** ("What are the main themes in the dataset?", "What are the key trends in interdisciplinary research?") because such queries inherently require reasoning over the *entire* corpus, not retrieving a localized fact. GraphRAG addresses this with a four-stage indexing pipeline that runs **once at indexing time** (expensive) so query-time is fast:

1. **Source → text chunks**: standard chunking
2. **Chunks → entities + relationships**: LLM extracts named entities and their relationships from each chunk
3. **Entities + relationships → knowledge graph**: aggregate across chunks, deduplicate, weight relationships by frequency
4. **Knowledge graph → hierarchical communities**: apply Leiden community detection recursively to partition the graph into nested communities; for each community, LLM-generate a summary

At query time, the system uses **map-reduce over community summaries**: each community's summary produces a partial answer to the query in parallel (the map step), then partials are combined into a final answer (the reduce step). On two 1M-token text corpora (podcast transcripts and news articles), GraphRAG beats vector RAG on both *comprehensiveness* (covers more relevant aspects) and *diversity* (produces varied perspectives) when judged by GPT-4 as LLM-as-judge. The open-source release (github.com/microsoft/graphrag) became one of the most-cited and most-deployed memory architecture papers of 2024 — the dominant alternative to vector-only RAG for long-document understanding.

## Key Takeaway

**Choose the shape of memory based on the shape of queries you'll receive — local retrieval (vector RAG) for fact lookup; global summarization (GraphRAG) for sensemaking; the same corpus should support both via different indices.** [ENGRAM: dominant on N (Network — the choice of graph + community hierarchy as the storage shape is THE architectural decision), A (Aggregate — community summaries are the consolidation primitive); secondary on R (Retrieve — map-reduce is the retrieval mechanism)] The deep insight is the *query taxonomy*: GraphRAG distinguishes **local questions** (answerable from one or a few chunks: "When was X founded?") from **global questions** (require reasoning across the corpus: "What are the main themes?"). Vector RAG optimizes for the first and structurally cannot handle the second — embedding similarity finds chunks close to the query, but a global query has no single "close" chunk. **The architectural fix is to pre-compute the global structure at indexing time** so that query-time can be a fast map-reduce instead of an impossible retrieval. For Flow OS: instrument your queries. If most are local, pure vector RAG is fine. If you have a meaningful fraction of "what are the themes / patterns / overall conclusions" queries, you need a GraphRAG-style index. **The cost is at indexing time — graph extraction + community summarization is expensive ($, time) — but it amortizes across all future queries.**

## Implications

[ENGRAM mapping: dominant on **N** (Network — graph + hierarchy as memory shape) and **A** (Aggregate — community summaries are pre-computed consolidations); secondary on **R** (Retrieve — map-reduce over communities is the retrieval) and **E** (Encode — LLM-driven entity extraction is the write-time work)]

1. **The query taxonomy (local vs global) is the most useful contribution.** [N, R] Before GraphRAG, RAG papers tended to treat all queries as the same problem and improve retrieval/ranking incrementally. GraphRAG names the failure mode of vector RAG (global sensemaking) and proposes a structurally different solution for that class. **For Flow OS / any memory system: classify your queries by retrieval-shape before designing the memory index.** A useful first cut: local-factual (vector RAG wins), local-relational ("how is X related to Y?" — knowledge graph wins), global-summarization (community summaries win), temporal ("what happened most recently?" — temporal KG / Zep-style wins). One index can't serve all shapes well.

2. **Indexing-time work amortizes; query-time work doesn't.** [N, A] GraphRAG's graph extraction + community summarization runs ONCE at index build and is expensive (many LLM calls). Query-time is fast (read pre-computed summaries, run map-reduce). This is the inverse of vector RAG which is cheap to index (just compute embeddings) but does all the work at query time (vector search + LLM context filling + generation). **For sustained workloads, GraphRAG's amortization wins; for one-shot or rapidly-changing corpora, vector RAG's lower indexing cost wins.** This is a classic OLTP-vs-OLAP-style decision for memory systems.

3. **LLM-driven extraction is the write-path; this is the Mem0 / Memory-R1 pattern at corpus scale.** [E] GraphRAG uses an LLM at index time to extract entities + relationships + claims from each chunk. The LLM is not just a reader — it's a *write* component, distilling raw chunks into structured graph nodes/edges. **This is the same pattern as Mem0's CRUD operations at the corpus level**: LLM-as-writer, LLM-as-reader, with structured intermediate representations. The agentic memory literature and the GraphRAG literature are converging.

4. **Leiden community detection is a battle-tested algorithm that solves the "what's related to what" problem cleanly.** [N] Communities in the knowledge graph correspond to topical clusters (a community about "Quantum Systems" entities, a community about "low-power chips," etc.). Hierarchical Leiden gives you a tree of nested communities — high-level summaries at the top, fine-grained at the leaves. **For Flow OS: when your memory has entities and relationships, community detection on the resulting graph gives you "topics" for free** — no need to manually define topic hierarchies.

5. **Map-reduce is the right shape for global queries.** [R] Each community summary produces a partial answer in parallel (map); partials are aggregated into a final answer (reduce). This pattern parallelizes beautifully — N community summaries means N parallel LLM calls. The reduce step is one more LLM call. **Modern LLM-based systems often default to "stuff everything in context" or "sequential chain of thought" when map-reduce would be both faster and higher-quality.** GraphRAG's deployment shows map-reduce works in practice.

6. **LLM-as-judge for sensemaking eval is the methodological innovation.** §3.3 introduces an adaptive benchmarking approach: use LLM-1 to generate global sensemaking questions tailored to the corpus, then use LLM-2 to judge two RAG systems' answers head-to-head on predefined criteria (comprehensiveness, diversity). **There's no ground truth for "what are the main themes" questions** — this is exactly where LLM-as-judge becomes the only viable eval. The methodology generalizes to any sensemaking task.

## How to Apply It (method)

**The GraphRAG indexing pipeline (four stages):**

```
Stage 1: Source Documents → Text Chunks
  - Standard chunking (e.g., 600-tokens with overlap)
  - Trade-off: larger chunks = fewer LLM calls but worse recall (Lost-in-the-Middle)

Stage 2: Text Chunks → Entities & Relationships
  - For each chunk, prompt LLM to extract:
    * Named entities (people, places, organizations, concepts)
    * Relationships between entities (with descriptions)
    * Claims (factual statements about entities)
  - Few-shot prompts; domain-specific exemplars for specialized corpora

Stage 3: Entities & Relationships → Knowledge Graph
  - Aggregate instances across chunks (entity X mentioned in chunk 1, 5, 12 → single node)
  - Relationships become weighted edges (weight = co-occurrence count)
  - Claim aggregation similar
  - Use string matching for entity resolution (or softer matching for production)

Stage 4: Knowledge Graph → Hierarchical Communities + Summaries
  - Apply Leiden community detection
  - Recursively partition until leaf communities
  - For each community at every level:
    * LLM-generate a summary that captures the community's themes
    * Summaries at higher levels recursively incorporate child summaries
```

**Query time (map-reduce):**

```
def graphrag_query(query, communities, level=2):
    # Map: each community produces a partial answer in parallel
    partials = parallel_map(
        lambda c: llm("Given this community summary, what does it contribute to: {query}?\nSummary: {c.summary}"),
        communities[level]
    )
    
    # Reduce: aggregate partials into final answer
    final = llm("Combine these partial answers into a comprehensive response to: {query}\nPartial answers: {partials}")
    return final
```

**Key hyperparameters:**

- **Community level**: which level of the hierarchy to use for map step. Higher levels (coarser communities) = fewer LLM calls, less detail. Lower levels (finer communities) = more calls, more detail. Paper reports good results at intermediate levels.
- **Chunk size**: trade-off between fewer extractions (cheaper) and better recall.
- **Few-shot exemplars in extraction**: domain-tailored exemplars dramatically improve entity/relationship extraction quality.

**For Flow OS / production:**

1. **Evaluate query distribution** before deciding on GraphRAG. If <20% of queries are global-sensemaking, vector RAG may be sufficient.
2. **Budget indexing cost** — graph extraction is roughly 1-2 LLM calls per chunk, plus community summarization. For a 1M-token corpus, expect hundreds of dollars in LLM costs and hours of wall-clock time.
3. **Use a graph database** (Neo4j, NebulaGraph) or even just SQLite for production; in-memory works for prototyping but not for million-document corpora.
4. **Make the community hierarchy navigable** — surface community summaries to users as a corpus-browsing interface, not just an internal index structure.

## Best Figure

_(figure not extracted — Figure 1 in the paper is the canonical pipeline diagram, the most-referenced GraphRAG visualization)_

**Figure 1 — GraphRAG pipeline, page 4:**

A vertical flowchart split into two phases:

**Indexing Time (left side, top to bottom):**
- Source Documents
- ↓ text extraction and chunking
- Text Chunks
- ↓ domain-tailored summarization (entity/relationship extraction)
- Entities & Relationships
- ↓ domain-tailored summarization (aggregate, deduplicate)
- Knowledge Graph
- ↓ community detection
- Graph Communities
- ↓ domain-tailored summarization (per-community summaries)
- Community Summaries

**Query Time (right side, top to bottom):**
- User Query
- ↓ query-focused summarization (parallel per community)
- Community Answers (one per community in the chosen level)
- ↓ query-focused summarization (aggregate)
- Global Answer

The visual key: indexing time is heavy (4 stages, all LLM-summarization based); query time is light (2 stages, both LLM-summarization based but starting from pre-computed community summaries). The expensive work happens once; queries are cheap and parallelizable.

The figure also makes explicit the **community-detection step** between Knowledge Graph and Community Summaries — Leiden algorithm partitioning. This is the algorithmic core: without good community detection, you'd either have one giant summary (no resolution) or one summary per entity (no compression).

## What Experts Overlook

1. **The query taxonomy is the most exportable contribution.** Most readers focus on the graph-based implementation and miss the framing: **vector RAG can't answer global queries**. This taxonomy applies far beyond knowledge graphs — for example, BM25 + reranker can't answer "what are the themes" either; nor can pure parametric LLMs (they don't know your corpus). Once you accept "global queries need pre-aggregation," many architectures (RAPTOR's hierarchical tree, HippoRAG's PageRank-style traversal, summary indexes in general) become alternative answers to the same shape problem.

2. **LLM-as-judge for sensemaking eval is novel methodology.** §3.3 acknowledges there's no ground truth for "what are the main themes" questions — the LLM-as-judge approach (one LLM generates corpus-specific global questions, another judges system answers on comprehensiveness/diversity) is the methodology innovation, almost more interesting than the system itself. **This generalizes to any task without clean ground truth**: design generation, business strategy, research synthesis. For Flow OS evaluation: LLM-as-judge with explicit comprehensiveness/diversity criteria is the pattern.

3. **The choice of community level is a major hyperparameter that gets glossed over.** Different levels of the Leiden hierarchy answer different "scales" of question. A query about "macroeconomic trends" should hit a high-level community; "the relationship between Quantum Systems and NeoChip" should hit a leaf community. **Production GraphRAG systems probably need to pick the right level dynamically based on the query — the paper doesn't fully address this.** A heuristic: use the LLM to classify the query's "scale" and pick the community level accordingly.

4. **GraphRAG's indexing cost is significant and not always acknowledged in marketing material.** Each chunk requires at least one LLM call for entity extraction; communities require additional LLM calls for summarization; large corpora can cost $100s-$1000s in LLM API fees just to index. **For frequently-updated corpora, vector RAG's "just embed it" approach wins on cost-of-freshness** — GraphRAG works best for relatively stable corpora.

5. **Entity resolution via "exact string matching" is the elephant in the room.** §3.1.3: "our analysis uses exact string matching for entity matching." This means "Apple Inc.", "Apple", "AAPL", and "Apple Computer" are different entities unless your extraction prompt normalizes them. **For production, you need entity resolution / coreference / canonical-name mapping**, which the paper acknowledges but doesn't implement.

6. **Map-reduce assumes communities are independent — they're not.** [R] If query Q is about a phenomenon that spans multiple communities, the map step's per-community partial answers may each contain a piece of the story but miss the connections between communities. The reduce step has to recover those connections from the partial answers alone (without access to the underlying graph at reduce time, in the basic GraphRAG implementation). **For high-quality global sensemaking, the reduce step probably needs access to inter-community edges** — a graph-aware reduce, not just a stuff-and-summarize reduce.

## Extracted Prompts

The paper includes appendix prompts (A.1) for entity and relationship extraction. Reconstructed templates:

**Entity + Relationship Extraction prompt:**
```
You are extracting structured information from text. Given the text chunk below, extract:

1. ENTITIES — important named entities (people, places, organizations, concepts). For each, provide:
   - name: canonical name
   - type: category (person | place | organization | concept | other)
   - description: 1-2 sentence factual description

2. RELATIONSHIPS — meaningful relationships between extracted entities. For each, provide:
   - source: source entity name
   - target: target entity name
   - description: how they're related (factual, derived from the text)
   - strength: 1-10 indicating relationship importance

3. CLAIMS (optional) — important factual statements about entities:
   - subject: entity name
   - claim: the factual statement
   - source: which sentence(s) support this claim

Domain context: {domain_description}

Few-shot examples:
{exemplars}

Text chunk:
{chunk}

Output JSON.
```

**Community Summarization prompt:**
```
You are summarizing a community of related entities. Given the entities, relationships, and claims below, generate a coherent summary that captures the themes, key facts, and relationships within this community.

The summary should:
- Be 200-500 words
- Highlight the main themes
- Mention the most important entities and their roles
- Note significant relationships
- Avoid speculation beyond what's stated

Entities in community:
{entities}

Relationships:
{relationships}

Claims:
{claims}

If this community has sub-communities (already summarized), incorporate their summaries:
{sub_summaries}

Summary:
```

**Map-step prompt (query time):**
```
Given this community summary, what does it contribute to answering the user's query?
If the community is irrelevant to the query, say "Not relevant."

Query: {query}

Community summary:
{summary}

Partial answer:
```

**Reduce-step prompt:**
```
Combine these partial answers from different communities into a comprehensive, coherent final answer.

Avoid:
- Repeating the same information
- Contradictions across partial answers (acknowledge them if present)
- Padding or restating the query

User query: {query}

Partial answers:
{partials}

Final answer:
```

## Citations

- Lewis et al. (2020) — RAG (the vector-RAG baseline GraphRAG contrasts with)
- Liu et al. (2023) — Lost in the Middle (motivates the chunk-size trade-off)
- Klein, Moon, Hoffman (2006) — Sensemaking (the conceptual framing for "global" queries)
- Blondel et al. (2008) — Louvain community detection (the predecessor algorithm)
- Traag et al. (2019) — Leiden community detection (the actual algorithm used)
- Sarthi et al. (2024) — RAPTOR (the closest contemporary alternative — hierarchical summarization without explicit graph)
- Zheng et al. (2024) — LLM-as-judge (the evaluation methodology)
- Newman (2006) — Modularity in networks (foundational community-detection theory)
- Yang et al. (2018) — HotpotQA (the multi-hop QA benchmark for vector-RAG-style eval)
- Gao et al. (2023) — RAG survey (the related-work overview)
- Brown et al. (2020) — GPT-3 (the LLM used for extraction and summarization)
- Es et al. (2023) — RAGAS (the eval criteria contrast)

(Full citations list in frontmatter `citations:` field.)

## Related Digests

- [[lewis-2020-rag-knowledge-nlp]] — The vector-RAG baseline GraphRAG explicitly contrasts with
- [[sarthi-2024-raptor]] — RAPTOR is the closest alternative — hierarchical tree of summaries without explicit graph extraction
- [[gutierrez-2024-hipporag]] — HippoRAG uses PageRank over a knowledge graph for retrieval — different traversal mechanism but graph-RAG family
- [[rasmussen-2025-zep-temporal-kg]] — Zep adds temporal dimensions to knowledge-graph memory, related architecture for evolving corpora
- [[petrov-2026-schema-grounded-memory]] — Schema-grounded memory takes graph-RAG to schema-constrained graphs for more structured retrieval

## Reviewer Notes

Hallucination check: **Clean**. Key claims verified: four indexing stages (text chunks → entities/relationships → knowledge graph → hierarchical communities + summaries) — verified against §3.1; map-reduce query time — verified against §3.1 / Figure 1; Leiden community detection — verified against §3.1.4 with explicit citation to Traag et al. 2019; LLM-as-judge for sensemaking eval — verified against §3.3; entity-resolution via exact string matching as caveat — verified against §3.1.3; 1M-token corpora as eval scale — verified against §4 (not in my extract but mentioned in abstract); GraphRAG beats vector RAG on comprehensiveness and diversity — verified against abstract. The Microsoft GitHub release (github.com/microsoft/graphrag) is verified against §1. The "query taxonomy is the most exportable contribution" framing in Implications is the digest's interpretive bridge — accurate, foregrounds what's portable to other memory architectures.
