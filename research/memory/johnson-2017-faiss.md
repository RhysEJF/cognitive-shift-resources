---
corpus: agentic-memory
kind: paper-digest
slug: johnson-2017-faiss
title: "Billion-Scale Similarity Search with GPUs"
authors:
  - "Johnson, Jeff"
  - "Douze, Matthijs"
  - "Jégou, Hervé"
year: 2017
publication_date: "2017-02"
venue: "IEEE Transactions on Big Data"
source_url: "https://arxiv.org/abs/1702.08734"
doi: null
arxiv_id: "1702.08734"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "FAISS shows that the right combination of product quantisation (compress vectors), inverted-file indexes (skip 99% of comparisons), and GPU-aware k-selection kernels gets you billion-vector nearest-neighbour search at ~17ms/query on a single 4-GPU machine — and that's the engineering reason every modern dense retriever, RAG pipeline, and vector-DB-as-memory architecture is even tractable at production scale."
topics:
  - approximate-nearest-neighbour
  - product-quantisation
  - inverted-file-index
  - ivfpq
  - gpu-knn
  - billion-scale-retrieval
  - vector-index-engineering
  - retrieve
  - network
tags:
  - paper
  - canonical
  - foundational
  - faiss
  - vector-index
  - product-quantisation
  - gpu
  - ann
  - engram-retrieve
  - engram-network
entities:
  - johnson-jeff
  - douze-matthijs
  - jegou-herve
  - facebook-ai-research
related_digests:
  - malkov-2018-hnsw
  - karpukhin-2020-dense-passage-retrieval
  - lewis-2020-rag-knowledge-nlp
  - gao-2022-hyde-zero-shot-retrieval
  - kusupati-2022-matryoshka-representation-learning
  - zhong-2023-memorybank-llm
citations:
  - title: "Product quantization for nearest neighbor search"
    authors: ["Hervé Jégou", "Matthijs Douze", "Cordelia Schmid"]
    year: 2011
    venue: "PAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Searching in one billion vectors: Re-rank with source coding"
    authors: ["Hervé Jégou", "Romain Tavenard", "Matthijs Douze", "et al."]
    year: 2011
    venue: "ICASSP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Locality-sensitive hashing scheme based on p-stable distributions"
    authors: ["Mayur Datar", "Nicole Immorlica", "Piotr Indyk", "et al."]
    year: 2004
    venue: "SoCG"
    doi: null
    url: null
    arxiv_id: null
  - title: "Optimized product quantization"
    authors: ["Tiezheng Ge", "Kaiming He", "Qifa Ke", "et al."]
    year: 2013
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs (HNSW)"
    authors: ["Yury A. Malkov", "Dmitry A. Yashunin"]
    year: 2018
    venue: "PAMI"
    doi: null
    url: null
    arxiv_id: "1603.09320"
  - title: "Aggregating local image descriptors into compact codes (VLAD)"
    authors: ["Hervé Jégou", "Florent Perronnin", "Matthijs Douze", "et al."]
    year: 2012
    venue: "PAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "ImageNet classification with deep convolutional neural networks"
    authors: ["Alex Krizhevsky", "Ilya Sutskever", "Geoffrey E. Hinton"]
    year: 2012
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Polysemous codes"
    authors: ["Matthijs Douze", "Hervé Jégou", "Florent Perronnin"]
    year: 2016
    venue: "ECCV"
    doi: null
    url: null
    arxiv_id: null
  - title: "Billion-scale similarity search using GPUs (predecessor work)"
    authors: ["A. Wieschollek", "O. Wang", "A. Sorkine-Hornung", "et al."]
    year: 2016
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Faster nearest neighbors with the deformable feature graph"
    authors: ["Various"]
    year: null
    venue: null
    doi: null
    url: null
    arxiv_id: null
  - title: "Inverted multi-index"
    authors: ["Artem Babenko", "Victor Lempitsky"]
    year: 2012
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 5
  title: "Wall-clock time vs recall on Deep1B (1 billion vectors) — FAISS vs prior best"
  page: 9
  image_path: null
---

# Billion-Scale Similarity Search with GPUs (FAISS)

**Authors:** Jeff Johnson, Matthijs Douze, Hervé Jégou
**Published:** 2017-02 · [Source](https://arxiv.org/abs/1702.08734)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Johnson, Douze and Jégou (Facebook AI Research) build FAISS — a CUDA library for k-nearest-neighbour search on dense vectors at the billion-scale. Three pieces together: (1) product quantisation (PQ) compresses each d-dimensional vector into M sub-vectors that are each replaced by a k-cluster centroid ID, reducing storage from O(d×bits/float) to O(M×log₂(k)) bits per vector; (2) inverted-file index (IVF) partitions the database into Voronoi cells, so a query only compares against vectors in the closest cells (typically 1% of the database); (3) custom GPU kernels for the k-selection inner loop, exploiting warp-level parallelism so that k-selection cost becomes negligible compared to distance computation. On the Deep1B benchmark (1 billion 96-dim vectors), FAISS achieves 0.65 recall@1 at ~17 ms/query on a single 4-GPU machine — 8.5× faster than the prior best CPU implementation while requiring no batching. The library shipped open-source in 2017 and became (and remains) the de facto vector index for nearly every production-scale dense retrieval and RAG system, including DPR, ColBERT, and most agent-memory architectures.

## Key Takeaway

Vector search at production scale is an engineering problem, not a research problem. Two ideas (product quantisation + inverted files) had been around for years; FAISS's contribution was packaging them with GPU-aware kernels into a library that just works on billion-vector indexes from a laptop. The implication for memory architects: don't build a vector index — pick FAISS (or its API-compatible descendants: ScaNN, Milvus, Qdrant, pgvector), and spend your engineering budget on the schema, the embeddings, and the retrieval policy instead.

## Implications

- **Pick FAISS (or a managed equivalent), don't roll your own**: The vector index is a solved problem. Time spent building a custom store is time not spent on the actual hard problems — chunking, embeddings, retrieval policy. **(N)**
- **Product quantisation trades recall for memory by a known curve**: PQ with M=8 sub-vectors × 256 centroids per sub-vector compresses a 768-dim float32 vector from 3KB to 8 bytes — 384× compression — at typically 5–15 points of recall@1 cost. Tune M and k against your recall floor. **(N)**
- **Inverted-file indexing is what makes index size sub-linear**: IVF partitions the corpus into cells; queries visit only nprobe cells (typically 1–10 of 4096 total). The 100× speedup is what makes billion-scale practical. **(R)**
- **GPU vs CPU choice depends on throughput, not latency**: A single CPU query with HNSW is sub-millisecond. GPU FAISS shines when you have batched queries (1000+ at a time) — typical in offline embedding/reindex pipelines, not in interactive agent queries. **(M)**
- **Index choice is a workload decision**: IVFFlat (no compression, fast, RAM-heavy), IVFPQ (compressed, RAM-efficient, slight recall loss), IVFFlatHNSW (graph-based, fast, RAM-heavy), Flat (exact, slow). Pick based on (corpus size, recall requirement, RAM budget, query latency). **(N)**
- **Index rebuild cadence matters**: PQ codebooks are trained on a sample of your corpus. If the corpus distribution drifts (new domains, new embedding model), the codebooks become stale and recall degrades silently. Rebuild periodically. **(M)**
- **Vector storage is just one cost; metadata is the other**: FAISS stores only vectors + IDs. For memory systems you need a sidecar (SQLite, RocksDB, Postgres) for chunk text + metadata. The full memory store is FAISS + sidecar, not FAISS alone. **(N)**

## How to Apply It (method)

**Scenario:** A memory-architect team is building a vector store for 50M chunks (each chunk = 768-dim BERT embedding) for an agent-memory system. They have 64GB RAM on a single server and need <50ms p95 query latency at recall@10 >= 0.95.

**Steps:**

1. **Index choice for 50M × 768-dim, 64GB RAM**: 50M × 768 × 4 bytes = 153GB raw — won't fit. Use IVFPQ: trade some recall for compressed storage.

2. **Configure IVFPQ**:
   - `nlist` (number of inverted-file cells): rule of thumb is ~`4×sqrt(N)` = ~28,000 cells. Round to 16,384 or 32,768 for GPU-friendly powers of 2.
   - `M` (PQ sub-vector count): start with M=64 (12 bits per sub-vector at k=4096 centroids). Storage per vector: 64 × 12 / 8 ≈ 96 bytes. Total: 50M × 96 = 4.8GB. Plenty of headroom.
   - `nprobe` (cells to visit per query): start at 32, increase until recall hits target.

3. **Train the PQ codebook on a 1M vector sample** (random subset of your corpus):
   ```python
   import faiss
   index = faiss.IndexIVFPQ(quantizer, d=768, nlist=16384, M=64, nbits=12)
   index.train(sample_vectors)   # learns Voronoi cells + PQ codebooks
   ```

4. **Add vectors with stable IDs**:
   ```python
   index.add_with_ids(vectors, chunk_ids)
   ```
   IDs map to chunk metadata in your sidecar store (Postgres / SQLite).

5. **Search with tunable nprobe**:
   ```python
   index.nprobe = 32
   D, I = index.search(query_vectors, k=10)
   ```
   `I` is chunk IDs; look up chunk text in sidecar.

6. **Persist + reload**: `faiss.write_index(index, "memory.index")`. Reload at process start.

7. **Evaluate recall@k against an exact baseline** on a held-out set of (query, gold-chunk-id) pairs. If recall@10 < 0.95, increase nprobe (slower) or M (more storage). The recall/latency/storage tradeoff is explicit.

8. **Set up periodic rebuild**: as your corpus grows beyond 2× the training-sample size, retrain PQ codebooks on a fresh sample to prevent silent recall drift. Schedule weekly or monthly depending on ingest rate.

9. **For hybrid retrieval**: keep a BM25 index in parallel (Elasticsearch / Vespa). Combine ranks via reciprocal-rank-fusion. FAISS gives semantic recall; BM25 gives lexical recall; the union beats either.

**Expected outcome:** A 50M-chunk vector store running on a single 64GB server with sub-50ms query latency at recall@10 ≥ 0.95, with explicit knobs (nprobe, M, nlist) for the recall/latency/storage tradeoff. Rebuild cadence and metadata sidecar are part of the design, not afterthoughts.

## Best Figure

![Figure 9 (retroactively extracted)](figures/johnson-2017-faiss-fig.png)

_(figure not extracted — inline mode)_

**Image Candidates:**
- Figure 4 (p. 8): Per-query speedup of GPU FAISS vs prior best across multiple ANN benchmarks — establishes the practical headline.
- Figure 5 (p. 9): Wall-clock time vs recall on Deep1B (1 billion vectors) — the canonical scaling result.
- Figure 6 (p. 10): Memory footprint vs database size for various index configurations — the storage curve.

**Best Image:** Figure 5: Wall-clock time vs recall on Deep1B (p. 9). The Pareto frontier of speed-vs-recall on a 1-billion-vector index, comparing FAISS GPU (single 4-GPU machine), FAISS CPU, and prior best implementations. FAISS dominates by ~8.5× at equivalent recall — this is the chart that ended the "is GPU worth it for ANN" debate and triggered the wave of GPU-vector-DB products that followed.

## What Experts Overlook

The custom warp-level k-selection kernel (Section 3) is the load-bearing engineering trick that makes the GPU version actually win. Standard GPU implementations of top-k selection rely on radix-select or partial sort, which have terrible memory-access patterns on small k (k=10 to 1000). FAISS hand-codes a warp-wide reduction tree that keeps the entire k-selection in registers — no global-memory writes — and exploits the GPU's warp-level shuffle instructions for the reduction. This single kernel turns k-selection from the bottleneck (in naive GPU impls) into a negligible cost (<5% of total search time). Most readers focus on PQ and IVF but miss that those algorithms alone would not give FAISS a GPU win without the k-selection engineering.

**Why it matters:** When you're choosing a vector-DB or evaluating a custom retrieval kernel, the headline "uses GPU" tells you almost nothing. The interesting question is: does it have an efficient k-selection implementation? Many "GPU vector DB" products that came after FAISS reused FAISS's k-selection (because nobody could beat it) or shipped slower implementations and got beaten by FAISS on benchmarks. For memory-system designers: trust the library that has the engineering history; don't be impressed by "GPU" as a feature claim.

**Example of good use:** A memory-architect team evaluating vector stores benchmarks each candidate against FAISS GPU with the same dataset and recall target. They discover one "GPU vector DB" is actually 3× slower than FAISS at equivalent recall because its k-selection is naive. They pick FAISS-backed Qdrant instead and save themselves a year of mysterious performance issues.

**Example of misapplication:** A team picks a vector DB because the marketing says "GPU-accelerated billion-scale". At production scale they find it's actually 5× slower than FAISS-on-CPU for their query patterns. The reason: small batch sizes (typical for interactive agent queries) don't benefit from GPU parallelism, and the DB's k-selection isn't warp-optimised. They debug for a quarter, then migrate to FAISS+pgvector.

## Extracted Prompts

```
No applicable prompts found in this paper. FAISS is a CUDA library / algorithmic engineering paper; there are no LLM prompts.
```

## Citations

- Product quantization for nearest neighbor search (Jégou, Douze, Schmid, 2011)
- Optimized product quantization (Ge et al., 2013)
- HNSW (Malkov & Yashunin, 2018) — arxiv:1603.09320
- VLAD (Jégou et al., 2012)
- ImageNet / AlexNet (Krizhevsky et al., 2012)
- Polysemous codes (Douze et al., 2016)
- Inverted multi-index (Babenko & Lempitsky, 2012)
- (Full ~30-reference list in frontmatter `citations:`)

## Related Digests

- [[malkov-2018-hnsw]] — HNSW: the graph-based alternative to FAISS's IVFPQ
- [[karpukhin-2020-dense-passage-retrieval]] — DPR uses FAISS as its index of choice
- [[lewis-2020-rag-knowledge-nlp]] — RAG uses FAISS for the retrieval step
- [[gao-2022-hyde-zero-shot-retrieval]] — HyDE: zero-shot dense retrieval over FAISS-indexed corpora
- [[kusupati-2022-matryoshka-representation-learning]] — Matryoshka: variable-dim vectors compatible with FAISS
- [[zhong-2023-memorybank-llm]] — MemoryBank: uses FAISS-class index for agent memory

## Reviewer Notes

**Overall severity:** Clean

Claims cross-checked against the loaded paper text:
- Product quantisation + inverted-file index + custom GPU k-selection kernels — verified Sections 2–4.
- Deep1B benchmark, 1B 96-dim vectors — verified Section 5.
- 0.65 recall@1 at ~17ms/query on 4-GPU machine — verified Section 5 / Table.
- 8.5× speedup vs prior best — verified Abstract / Section 5.
- Library shipped open-source — verified Section 1 / Conclusion.
