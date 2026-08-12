---
corpus: agentic-memory
kind: paper-digest
slug: malkov-2018-hnsw
title: "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs"
authors:
  - "Malkov, Yu. A."
  - "Yashunin, D. A."
year: 2018
publication_date: "2018"
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
source_url: "https://arxiv.org/abs/1603.09320"
doi: null
arxiv_id: "1603.09320"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Approximate nearest-neighbour search becomes logarithmic — and survives clustered, low-dimensional, non-metric data — when you stack proximity graphs into exponentially-thinning layers and replace 'connect to nearest M' with a diversity heuristic that deliberately keeps long bridges between clusters."
topics:
  - approximate-nearest-neighbor
  - vector-search
  - proximity-graphs
  - navigable-small-world
  - hnsw
  - retrieval-infrastructure
  - hierarchical-index
  - skip-list
tags:
  - paper
  - retrieval
  - vector-database
  - engram-retrieve
  - engram-network
  - memory-substrate
  - foundational
entities:
  - malkov-yury
  - yashunin-dmitry
related_digests:
  - adler-2026-storage-not-memory
  - chhikara-2025-mem0
  - latimer-2025-hindsight-memory
  - packer-2023-memgpt-os
citations:
  - title: "Distinctive image features from scale-invariant keypoints"
    authors: ["David G. Lowe"]
    year: 2004
    venue: "International Journal of Computer Vision"
    doi: null
    url: null
    arxiv_id: null
  - title: "Indexing by Latent Semantic Analysis"
    authors: ["S. Deerwester", "S. T. Dumais", "T. K. Landauer", "et al."]
    year: 1990
    venue: "Journal of the American Society for Information Science"
    doi: null
    url: null
    arxiv_id: null
  - title: "Data structures and algorithms for nearest neighbor search in general metric spaces"
    authors: ["Peter N. Yianilos"]
    year: 1993
    venue: "SODA"
    doi: null
    url: null
    arxiv_id: null
  - title: "Searching in metric spaces by spatial approximation"
    authors: ["Gonzalo Navarro"]
    year: 2002
    venue: "The VLDB Journal"
    doi: null
    url: null
    arxiv_id: null
  - title: "Singleton indexes for nearest neighbor search"
    authors: ["E. S. Tellez", "G. Ruiz", "E. Chavez"]
    year: 2016
    venue: "Information Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Scalable nearest neighbor algorithms for high dimensional data"
    authors: ["Marius Muja", "David G. Lowe"]
    year: 2014
    venue: "IEEE TPAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Rank-based similarity search: Reducing the dimensional dependence"
    authors: ["Michael E. Houle", "Michael Nett"]
    year: 2015
    venue: "IEEE TPAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Practical and optimal LSH for angular distance"
    authors: ["A. Andoni", "P. Indyk", "T. Laarhoven", "et al."]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Approximate nearest neighbors: towards removing the curse of dimensionality"
    authors: ["Piotr Indyk", "Rajeev Motwani"]
    year: 1998
    venue: "ACM STOC"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fast neighborhood graph search using cartesian concatenation"
    authors: ["J. Wang", "J. Wang", "G. Zeng", "et al."]
    year: 2015
    venue: "Multimedia Data Mining and Analytics (Springer)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fast exact search in hamming space with multi-index hashing"
    authors: ["M. Norouzi", "A. Punjani", "D. J. Fleet"]
    year: 2014
    venue: "IEEE TPAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "The inverted multi-index"
    authors: ["Artem Babenko", "Victor Lempitsky"]
    year: 2012
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Product quantization for nearest neighbor search"
    authors: ["Hervé Jegou", "Matthijs Douze", "Cordelia Schmid"]
    year: 2011
    venue: "IEEE TPAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient indexing of billion-scale datasets of deep descriptors"
    authors: ["Artem Babenko", "Victor Lempitsky"]
    year: 2016
    venue: "CVPR"
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
  - title: "Locally optimized product quantization for approximate nearest neighbor search"
    authors: ["Yannis Kalantidis", "Yannis Avrithis"]
    year: 2014
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient large-scale approximate nearest neighbor search on the GPU"
    authors: ["P. Wieschollek", "O. Wang", "A. Sorkine-Hornung", "et al."]
    year: 2016
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Approximate Nearest Neighbor Queries in Fixed Dimensions"
    authors: ["Sunil Arya", "David M. Mount"]
    year: 1993
    venue: "SODA"
    doi: null
    url: null
    arxiv_id: null
  - title: "Query-driven iterated neighborhood graph search for large scale indexing"
    authors: ["Jingdong Wang", "Shipeng Li"]
    year: 2012
    venue: "ACM Multimedia"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fast Nearest Neighbor Search in the Hamming Space"
    authors: ["Z. Jiang", "L. Xie", "X. Deng", "et al."]
    year: 2016
    venue: "MultiMedia Modeling (Springer)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Navigating k-nearest neighbor graphs to solve nearest neighbor searches"
    authors: ["Edgar Chávez", "Eric S. Tellez"]
    year: 2010
    venue: "Advances in Pattern Recognition (Springer)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fast approximate similarity search based on degree-reduced neighborhood graphs"
    authors: ["K. Aoyama", "K. Saito", "H. Sawada", "et al."]
    year: 2011
    venue: "ACM SIGKDD"
    doi: null
    url: null
    arxiv_id: null
  - title: "Finding Near Neighbors Through Local Search"
    authors: ["G. Ruiz", "E. Chávez", "M. Graff", "et al."]
    year: 2015
    venue: "Similarity Search and Applications (Springer)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Graphs for metric space searching"
    authors: ["Rodrigo Paredes"]
    year: 2008
    venue: "PhD Thesis, University of Chile"
    doi: null
    url: "http://www.dcc.uchile.cl/~raparede/publ/08PhDthesis.pdf"
    arxiv_id: null
  - title: "Scalable distributed algorithm for approximate nearest neighbor search problem in high dimensional general metric spaces"
    authors: ["Yury Malkov", "Alexander Ponomarenko", "Andrey Logvinov", "et al."]
    year: 2012
    venue: "Similarity Search and Applications (Springer)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Approximate nearest neighbor algorithm based on navigable small world graphs"
    authors: ["Yury Malkov", "Alexander Ponomarenko", "Andrey Logvinov", "et al."]
    year: 2014
    venue: "Information Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Skip lists: a probabilistic alternative to balanced trees"
    authors: ["William Pugh"]
    year: 1990
    venue: "Communications of the ACM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Extended navigability of small world networks: exact results and new insights"
    authors: ["C. C. Cartozo", "P. De Los Rios"]
    year: 2009
    venue: "Physical Review Letters"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient k-nearest neighbor graph construction for generic similarity measures"
    authors: ["Wei Dong", "Charikar Moses", "Kai Li"]
    year: 2011
    venue: "WWW"
    doi: null
    url: null
    arxiv_id: null
  - title: "Approximate Nearest Neighbor Search Small World Approach"
    authors: ["A. Ponomarenko", "Y. Malkov", "A. Logvinov", "et al."]
    year: 2011
    venue: "ICTA"
    doi: null
    url: null
    arxiv_id: null
  - title: "Navigation in a small world"
    authors: ["Jon M. Kleinberg"]
    year: 2000
    venue: "Nature"
    doi: null
    url: null
    arxiv_id: null
  - title: "Navigability of complex networks"
    authors: ["M. Boguna", "D. Krioukov", "K. C. Claffy"]
    year: 2009
    venue: "Nature Physics"
    doi: null
    url: null
    arxiv_id: null
  - title: "Comparative Analysis of Data Structures for Approximate Nearest Neighbor Search"
    authors: ["A. Ponomarenko", "N. Avrelin", "B. Naidan", "et al."]
    year: 2014
    venue: "Third International Conference on Data Analytics"
    doi: null
    url: null
    arxiv_id: null
  - title: "Permutation search methods are efficient, yet faster search is possible"
    authors: ["Bilegsaikhan Naidan", "Leonid Boytsov", "Eric Nyberg"]
    year: 2015
    venue: "VLDB"
    doi: null
    url: null
    arxiv_id: null
  - title: "Hyperbolic geometry of complex networks"
    authors: ["D. Krioukov", "F. Papadopoulos", "M. Kitsak", "et al."]
    year: 2010
    venue: "Physical Review E"
    doi: null
    url: null
    arxiv_id: null
  - title: "Navigable networks as Nash equilibria of navigation games"
    authors: ["A. Gulyás", "J. J. Bíró", "A. Kőrösi", "et al."]
    year: 2015
    venue: "Nature Communications"
    doi: null
    url: null
    arxiv_id: null
  - title: "Combinatorial algorithms for nearest neighbors, near-duplicates and small-world design"
    authors: ["Yury Lifshits", "Shengyu Zhang"]
    year: 2009
    venue: "ACM-SIAM SODA"
    doi: null
    url: null
    arxiv_id: null
  - title: "From Small-World Networks to Comparison-Based Search"
    authors: ["A. Karbasi", "S. Ioannidis", "L. Massoulie"]
    year: 2015
    venue: "IEEE Transactions on Information Theory"
    doi: null
    url: null
    arxiv_id: null
  - title: "Peer to peer multidimensional overlays: Approximating complex structures"
    authors: ["O. Beaumont", "A.-M. Kermarrec", "É. Rivière"]
    year: 2007
    venue: "Principles of Distributed Systems (Springer)"
    doi: null
    url: null
    arxiv_id: null
  - title: "VoroNet: A scalable object network based on Voronoi tessellations"
    authors: ["O. Beaumont", "A.-M. Kermarrec", "L. Marchal", "et al."]
    year: 2007
    venue: "IPDPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "The small-world phenomenon: An algorithmic perspective"
    authors: ["Jon Kleinberg"]
    year: 2000
    venue: "ACM STOC"
    doi: null
    url: null
    arxiv_id: null
  - title: "An experimental study of the small world problem"
    authors: ["Jeffrey Travers", "Stanley Milgram"]
    year: 1969
    venue: "Sociometry"
    doi: null
    url: null
    arxiv_id: null
  - title: "Collective dynamics of small-world networks"
    authors: ["Duncan J. Watts", "Steven H. Strogatz"]
    year: 1998
    venue: "Nature"
    doi: null
    url: null
    arxiv_id: null
  - title: "Growing homophilic networks are natural navigable small worlds"
    authors: ["Yury A. Malkov", "Alexander Ponomarenko"]
    year: 2016
    venue: "PLoS ONE"
    doi: null
    url: null
    arxiv_id: null
  - title: "The rainbow skip graph: a fault-tolerant constant-degree distributed data structure"
    authors: ["M. T. Goodrich", "M. J. Nelson", "J. Z. Sun"]
    year: 2006
    venue: "ACM-SIAM SODA"
    doi: null
    url: null
    arxiv_id: null
  - title: "The relative neighbourhood graph of a finite planar set"
    authors: ["Godfried T. Toussaint"]
    year: 1980
    venue: "Pattern Recognition"
    doi: null
    url: null
    arxiv_id: null
  - title: "FANNG: fast approximate nearest neighbour graphs"
    authors: ["Ben Harwood", "Tom Drummond"]
    year: 2016
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Higher-dimensional Voronoi diagrams in linear expected time"
    authors: ["Rex A. Dwyer"]
    year: 1991
    venue: "Discrete & Computational Geometry"
    doi: null
    url: null
    arxiv_id: null
  - title: "Engineering Efficient and Effective Non-metric Space Library"
    authors: ["Leonid Boytsov", "Bilegsaikhan Naidan"]
    year: 2013
    venue: "Similarity Search and Applications (Springer)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to prune in metric and non-metric spaces"
    authors: ["Leonid Boytsov", "Bilegsaikhan Naidan"]
    year: 2013
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Optimal Data-Dependent Hashing for Approximate Near Neighbors"
    authors: ["Alexandr Andoni", "Ilya Razenshteyn"]
    year: 2015
    venue: "ACM STOC"
    doi: null
    url: null
    arxiv_id: null
  - title: "GloVe: Global vectors for word representation"
    authors: ["Jeffrey Pennington", "Richard Socher", "Christopher D. Manning"]
    year: 2014
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "CoPhIR: a test collection for content-based image retrieval"
    authors: ["P. Bolettieri", "et al."]
    year: 2009
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "0905.4627"
  - title: "Gradient-based learning applied to document recognition"
    authors: ["Yann LeCun", "Léon Bottou", "Yoshua Bengio", "et al."]
    year: 1998
    venue: "Proceedings of the IEEE"
    doi: null
    url: null
    arxiv_id: null
  - title: "Near neighbor searching with K nearest references"
    authors: ["E. Chávez", "M. Graff", "G. Navarro", "et al."]
    year: 2015
    venue: "Information Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Effective proximity retrieval by ordering permutations"
    authors: ["E. C. Gonzalez", "K. Figueroa", "G. Navarro"]
    year: 2008
    venue: "IEEE TPAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Succinct nearest neighbor search"
    authors: ["E. S. Tellez", "E. Chávez", "G. Navarro"]
    year: 2013
    venue: "Information Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Software framework for topic modelling with large corpora"
    authors: ["Petr Sojka"]
    year: 2010
    venue: "LREC Workshop on New Challenges for NLP Frameworks"
    doi: null
    url: null
    arxiv_id: null
  - title: "Distance-based similarity models for content-based multimedia retrieval"
    authors: ["Christian Beecks"]
    year: 2013
    venue: "PhD Thesis, RWTH Aachen"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Illustration of the Hierarchical NSW idea — search starts from the top layer (red) and descends greedily through layers of decreasing characteristic radius to the query (green)"
  page: 3
  image_path: "figures/malkov-2018-hnsw-fig.png"
---

# Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs

**Authors:** Yu. A. Malkov, D. A. Yashunin
**Published:** 2018 · [Source](https://arxiv.org/abs/1603.09320)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

HNSW is a fully graph-based approximate-K-nearest-neighbour index that stacks proximity graphs into layers whose level for each element is drawn from an exponentially decaying distribution (geometric with parameter mL = 1/ln(M)), giving an expected O(log N) search instead of the polylogarithmic scaling of the older NSW algorithm. Construction is incremental: each insertion (i) greedily walks down from the current top entry point with ef=1 per layer, then (ii) at its assigned level and below, runs a wider search with `efConstruction` candidates and connects to M neighbours chosen by a diversity heuristic — a node only joins the link list if it is closer to the new element than to any already-selected neighbour, which deliberately preserves long bridges between clusters (the "relative neighbourhood graph" property). On 5M SIFT (d=128) a quality index builds in ~3 minutes on a 4×10-core Xeon; on a 200M SIFT subset it indexes in 5.6 hours with M=16, efConstruction=500 at ~64 GB RAM and beats Faiss-PQ on both speed and accuracy (at the cost of more memory: 64 GB vs ~24-30 GB). Against open-source rivals on SIFT/GloVe/CoPhIR/DEEP/MNIST it wins decisively, and on the wiki-8 JS-divergence dataset where the old NSW failed, HNSW is ~3 orders of magnitude faster. Typical knobs: M ∈ [5, 48], Mmax0 = 2M, efConstruction ≈ 100-500, mL = 1/ln(M); memory cost ≈ (Mmax0 + mL·Mmax)·bytes_per_link ≈ 60-450 bytes per stored element on top of the data itself. Takeaway: for any vector or general-metric retrieval workload where you have RAM, HNSW is the default graph-index baseline, and the heuristic neighbour-selection step — not the hierarchy — is what makes it survive clustered and low-dimensional data.

## Key Takeaway

Approximate nearest-neighbour search becomes logarithmic — and survives clustered, low-dimensional, non-metric data — when you stack proximity graphs into exponentially-thinning layers and replace "connect to nearest M" with a diversity heuristic that deliberately keeps long bridges between clusters. The hierarchy gives you scale separation (top-layer hops cover huge distances cheaply, bottom-layer hops fine-tune); the heuristic gives you connectivity (the graph cannot disintegrate into isolated cluster components). Each idea on its own is incremental; together they explain why HNSW became the default vector-index baseline. **[ENGRAM dimensions: Network — shape-of-memory choice — and Retrieve — the recall-time mechanic.]**

## Implications

- **Default your retrieval layer to HNSW when memory permits, not flat or IVF-PQ** *(Retrieve)*: On every dataset the paper tested in single-thread mode — SIFT 1M, GloVe 1.2M, CoPhIR 2M, DEEP 1M, MNIST 60k, random d=4 30M, and the wiki-8/wiki-128/ImageNet/DNA general-space set — HNSW dominated Annoy, FLANN, FALCONN, VP-tree, NAPP, and NSW. If your agent-memory store has the RAM to keep the graph in memory, HNSW is the strongest single-index default; compress only when RAM forces it.
- **Budget RAM, not query time** *(Network · Maintain)*: Per-element memory ≈ (Mmax0 + mL·Mmax)·bytes_per_link, ~60-450 bytes on top of the data (Section 4.2.3). On the 200M SIFT comparison, HNSW used 64 GB while Faiss-PQ ran in 23-30 GB — HNSW is the RAM-hungry option. If your memory store has tens of millions of records and a tight RAM envelope, plan for IVF-PQ as a fallback or a two-tier (HNSW over PQ-compressed vectors) design.
- **The heuristic neighbour-selector is mandatory for clustered or low-dim data** *(Network · Ground)*: Figure 7 shows that without the diversity heuristic (Alg. 4 vs Alg. 3) HNSW collapses on 100-cluster d=10 data — recall stops climbing. Most "RAG works" intuition assumes uniform embeddings; if your real corpus is naturally clumpy (tightly themed memories, repeated boilerplate, near-duplicate notes), the cheaper k-NN-graph variant is silently lossy. Always turn the heuristic on.
- **Pick M for your dimensionality and recall target, not by intuition** *(Retrieve)*: Recommended M ∈ [5, 48]. Smaller M → faster, lower-recall, low-dim friendly. Larger M → higher recall on high-dim data, more RAM (Section 4.1, Fig. 8). For agent-memory embeddings (typically d=384-1536) and recall ≥ 0.95, the paper's evidence points to M = 16-32 with Mmax0 = 2M.
- **efConstruction trades index-build time for index quality** *(Maintain)*: Treat it as a hyperparameter your *write path* sets once, not a query knob. Paper guidance: large enough to make construction-time recall ≈ 0.95-1.0 (commonly 100-500). Fig. 10 shows the curve flattens fast — efConstruction=100 is "reasonable", 500 squeezes the last percent of recall at much higher build cost.
- **Build is parallelisable, search is not naturally distributable** *(Maintain)*: Construction scales near-linearly with thread count and produces the same index (Fig. 9 — 10M SIFT in ~3 min on 40 cores). But because every query must enter at the global top layer, you cannot shard the index across nodes the way base NSW could. If you want a distributed memory store, partition the data into per-shard HNSW indices and merge — accept that throughput per node won't scale ideally.
- **No support for deletes or updates** *(Maintain)*: The paper itself flags this as future work (Section 6). HNSW as published is insert-only. If your memory architecture needs forget / decay / supersede semantics, you must implement them outside the index — tombstone lists at the read path, or periodic rebuild. This is the single most operationally annoying limitation in production.
- **Incremental indexing is real and order-tolerant** *(Encode · Maintain)*: Unlike base NSW which required pre-shuffling, HNSW's level-randomisation gives correct behaviour even if insertion order drifts with time (e.g. memories arriving in temporal sequence). Useful if write traffic is bursty or non-stationary; the structure self-randomises.

## How to Apply It (method)

**Scenario:** You are building an agent-memory store for a long-running personal AI: ~5 million atomic notes / observations / extractions, embedded with a 768-dim model, queried at every turn. You want sub-50ms recall@10 ≥ 0.95 on a single laptop-class box, plus the ability to ingest ~1000 new memories per day without rebuild. You have ~16 GB RAM headroom for the index.

**Steps:**

1. **Pick the M, Mmax0, mL, efConstruction tuple from the paper's recipe** (Section 4.1): start with M = 16 (768-dim is "high enough"), Mmax0 = 2·M = 32, mL = 1/ln(M) ≈ 0.36, efConstruction = 200. These are the values nmslib/HNSWlib defaults derive from this paper; deviate only if you have evidence you should.

2. **Estimate memory before you build**: per-element cost is (Mmax0 + mL·Mmax) · bytes_per_link. With 32 + 0.36·16 ≈ 38 links/element × 4 bytes (uint32) = ~152 bytes/element for the graph alone, plus 768·4 = 3072 bytes per stored vector. 5M elements ≈ 16 GB total. Headroom check: pass.

3. **Implement INSERT (Alg. 1) once per new memory**:

   ```
   procedure INSERT(hnsw, q, M, Mmax, efConstruction, mL):
     1. W = {}
     2. ep = current top entry point of hnsw
     3. L = level of ep
     4. l = floor(-ln(uniform(0,1)) * mL)       # element's level
     5. for lc from L down to l+1:
          W = SEARCH-LAYER(q, ep, ef=1, lc)
          ep = nearest(W, q)
     6. for lc from min(L, l) down to 0:
          W = SEARCH-LAYER(q, ep, efConstruction, lc)
          neighbors = SELECT-NEIGHBORS-HEURISTIC(q, W, M, lc,
                       extendCandidates=False, keepPrunedConnections=True)
          add bidirectional edges between q and neighbors at layer lc
          for each e in neighbors:
            if degree(e, lc) > Mmax_for(lc):
              e.neighbors_lc = SELECT-NEIGHBORS-HEURISTIC(
                e, e.neighbors_lc, Mmax_for(lc), lc)
          ep = W
     7. if l > L:
          set entry point of hnsw to q
   ```

   `SEARCH-LAYER` (Alg. 2) is best-first beam search with a dynamic list W of size ef and a visited set. `SELECT-NEIGHBORS-HEURISTIC` (Alg. 4) iterates candidates from nearest to furthest and keeps a candidate only if it is closer to `q` than to any already-chosen neighbour — this is the key step.

4. **Implement K-NN-SEARCH (Alg. 5) for queries**:

   ```
   procedure K-NN-SEARCH(hnsw, q, K, ef):
     1. ep = entry point of hnsw
     2. L = level of ep
     3. for lc from L down to 1:
          W = SEARCH-LAYER(q, ep, ef=1, lc)
          ep = nearest(W, q)
     4. W = SEARCH-LAYER(q, ep, ef, 0)
     5. return top-K nearest from W to q
   ```

   `ef` is the only per-query knob you expose to callers — bigger ef = higher recall, more compute. Start with ef = 50 for recall@10 ≈ 0.95 on this dataset shape; tune via offline evaluation.

5. **Use an off-the-shelf library, not your own implementation**: `hnswlib` (header-only C++ with Python bindings, written by Malkov himself; github.com/nmslib/hnswlib) or `faiss` (`IndexHNSWFlat`). Re-implementing is a multi-week tax for no quality gain.

6. **Plan for deletes upfront**: HNSW has none. Maintain a separate tombstone set keyed by element ID; filter results post-retrieval. If tombstones exceed ~20% of indexed elements, schedule a background full-rebuild from your source-of-truth store.

7. **Evaluate honestly**: build an offline test set of (query, ground-truth-top-K) pairs by running a brute-force comparison on a sample. Track recall@K and p50/p95 latency as you sweep ef. Don't trust hyperparameter folklore — the paper itself emphasises that the optimal trade-off curve depends on your dataset's intrinsic dimensionality.

**Expected outcome:** A persistent on-disk HNSW index loaded into memory at agent startup, serving recall@10 ≥ 0.95 queries in sub-50ms on a single CPU core, incrementally accepting new memories one at a time without rebuilds. Memory budget closes around 16 GB; deletes are handled at the application layer via tombstones. The agent now has a retrieval substrate that scales to ~50M memories on a 64 GB workstation before you need to consider IVF-PQ compression or sharding.

## Best Figure

![Figure 1 — Illustration of the Hierarchical NSW idea (page 3)](figures/malkov-2018-hnsw-fig.png)

Image Candidates:
Figure 1 (p. 3): The canonical HNSW diagram — three stacked layers with "Decreasing characteristic radius", red arrows tracing greedy descent from top-layer red entry node to bottom-layer green query, the single image every subsequent HNSW explainer redraws.
Figure 12 (p. 8): Side-by-side scaling plot of HNSW vs base NSW on d=8 random vectors, showing distance-computation count and raw query time both diverging as dataset size grows from 10² to 10⁸ — proves the log-vs-polylog scaling story.
Figure 13 (p. 9): Six-panel recall/query-time grid comparing HNSW against Annoy, NSW, FLANN, VP-tree, FALCONN across SIFT, GloVe, CoPhIR, DEEP, MNIST, 30M random — the "we win everywhere" panel that drove adoption.

Best Image:
Figure Name: Figure 1: "Illustration of the Hierarchical NSW idea. The search starts from an element from the top layer (shown red). Red arrows show direction of the greedy algorithm from the entry point to the query (shown green)."
Figure Page: 3
Slide Caption: HNSW search: enter at the top sparse layer, greedily hop to a local minimum, drop a layer, repeat — characteristic edge length shrinks each layer down.
Description: Figure 1 is the paper's defining diagram. Three stacked rectangles represent layers 2, 1, 0 of the multi-layer proximity graph. Each layer is a graph whose edge length scale shrinks as you descend (annotated "Decreasing characteristic radius" by a vertical arrow on the right). The search starts at a red entry node in the top layer, traverses one or two long edges to reach a local minimum (red arrows), then drops vertically (dashed grey) into the next layer where it continues greedy search with shorter edges, until it lands on the green query node in layer 0. The figure makes three architectural decisions visually obvious in one frame: (1) the index is hierarchical with exponentially thinning population per layer; (2) search is greedy and monotone — never re-enters an upper layer; (3) per-element work per layer is bounded, so the total work is O(layers) ≈ O(log N). It is the figure every subsequent vector-DB blog post redraws, and the right image to show a reader who is meeting HNSW for the first time.

## What Experts Overlook

The diversity-preserving neighbour-selection heuristic (Algorithm 4) is what actually makes HNSW robust on realistic data, not the hierarchy. Most explainers focus on the multi-layer skip-list-of-graphs picture (Figure 1), but Figure 7 shows the more important thing: on 100-cluster d=10 data, replacing the heuristic with the naive "connect to the M nearest candidates" (Algorithm 3) makes recall stop improving past ~0.7 no matter how long you search — the graph fractures into isolated cluster components and greedy walk can never cross the gap. The heuristic's rule is deceptively small: iterate candidates from nearest to farthest and *only add a candidate to your neighbour list if it is closer to you than to any neighbour you've already added*. That single inversion gives you a subgraph of the *relative neighbourhood graph*, which provably preserves a connected component across the whole dataset — including across cluster boundaries (Figure 2 shows the inserted element on cluster 1's boundary keeping one long link to cluster 2 instead of using all M slots on its immediate cluster-1 neighbours).

**Why it matters:** Real corpora — agent memories, document chunks, support tickets, scientific abstracts — are almost never uniformly distributed. They cluster by topic, author, time, project. A k-NN-graph index on clustered data routinely returns "the 10 closest neighbours that all happen to be in the same cluster as my query" and silently misses the answer in an adjacent topic. The heuristic is what prevents this silent failure mode, and it's the reason HNSW dominates the wiki-8 Jensen-Shannon-divergence dataset (Figure 14) by *three orders of magnitude* over base NSW — wiki-8 is a low-dimensional non-metric space where the old algorithm fractured. The architecture-level lesson for memory systems: when you choose your *Network* shape (ENGRAM N), the rule that decides *which edges live and which die* is more load-bearing than the topology itself.

**Example of good use:** A memory-architect building a long-context agent for a research workflow turns on the heuristic (`extendCandidates=True` if clusters are extreme), keeps `keepPrunedConnections=True` so the M-degree is preserved, and validates recall on a held-out set of cross-topic queries (deliberately ask things that should hop categories). Recall holds above 0.95 across topic boundaries because the long bridges survive. Bonus: the same heuristic yields the *relative neighbourhood graph as a byproduct*, which is a free hint structure if you ever want to do graph-shaped reasoning over memories later.

**Example of misapplication:** A team copies the multi-layer structure but reaches for the simpler Algorithm 3 ("just connect to the M nearest, the hierarchy will handle the rest") to save implementation time. On their synthetic uniform-distribution benchmark everything looks fine. In production with clustered customer-support tickets, recall@10 drops from a measured 0.94 to ~0.7 with no visible error — the index "works" but returns intra-cluster duplicates. They blame the embedding model, swap embeddings twice, and never look at the graph-construction code. The fix is one function call; the cost of not knowing the fix is a quarter of a roadmap.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- D. G. Lowe. "Distinctive image features from scale-invariant keypoints." *IJCV*, 2004.
- S. Deerwester, S. T. Dumais, T. K. Landauer, et al. "Indexing by Latent Semantic Analysis." *JASIS*, 1990.
- P. N. Yianilos. "Data structures and algorithms for nearest neighbor search in general metric spaces." *SODA*, 1993.
- G. Navarro. "Searching in metric spaces by spatial approximation." *The VLDB Journal*, 2002.
- M. Muja, D. G. Lowe. "Scalable nearest neighbor algorithms for high dimensional data." *IEEE TPAMI*, 2014.
- A. Andoni, P. Indyk, T. Laarhoven, et al. "Practical and optimal LSH for angular distance." *NeurIPS*, 2015.
- P. Indyk, R. Motwani. "Approximate nearest neighbors: towards removing the curse of dimensionality." *STOC*, 1998.
- H. Jegou, M. Douze, C. Schmid. "Product quantization for nearest neighbor search." *IEEE TPAMI*, 2011.
- W. Pugh. "Skip lists: a probabilistic alternative to balanced trees." *CACM*, 1990.
- J. M. Kleinberg. "Navigation in a small world." *Nature*, 2000.

_(60 total citations extracted — full structured list in the frontmatter `citations:` array, used as the auto-research hook for `/citation-walk` and future `/auto-research`.)_

## Related Digests

- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems

## Reviewer Notes

**Overall severity:** Clean

All quantitative claims in the digest (M ∈ [5, 48]; Mmax0 = 2M; mL = 1/ln(M); efConstruction ≈ 100-500; per-element memory ≈ 60-450 bytes; 200M SIFT build = 5.6 hours at 64 GB; ~3 orders of magnitude speedup over NSW on wiki-8 JS-divergence; 10M SIFT in ~3 min on 40 cores; dominance over Annoy/FLANN/FALCONN/VP-tree/NAPP on the named datasets) are directly supported by Sections 4.1, 4.2.3, 5.1-5.4, and Tables 1-3 / Figures 6-15 of the paper. The architectural claims (hierarchy + diversity heuristic, scale-separated layers, relative-neighbourhood-graph property, insert-only, O(log N) search, O(N log N) construction) match Sections 3, 4, and 4.2 verbatim. The Method section's pseudocode for INSERT, SEARCH-LAYER, and K-NN-SEARCH is faithful to Algorithms 1, 2, and 5; the SELECT-NEIGHBORS-HEURISTIC description matches Algorithm 4. The "no deletes/updates" caveat is flagged by the authors themselves in Section 6. The lens-tagging to ENGRAM dimensions is editorial framing for the memory-architect reader and is clearly marked as such. No hallucinated metrics, no invented benchmarks.
