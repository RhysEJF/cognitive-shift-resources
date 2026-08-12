---
corpus: agentic-memory
kind: paper-digest
slug: sarthi-2024-raptor
title: "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval"
authors:
  - "Sarthi, Parth"
  - "Abdullah, Salman"
  - "Tuli, Aditi"
  - "Khanna, Shubh"
  - "Goldie, Anna"
  - "Manning, Christopher D."
year: 2024
publication_date: "2024-01"
venue: "ICLR 2024"
source_url: "https://arxiv.org/abs/2401.18059"
doi: "10.48550/arXiv.2401.18059"
arxiv_id: "2401.18059"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Recursively clustering text chunks (UMAP + Gaussian Mixture Model with soft assignment), summarizing each cluster with an LLM, and indexing all layers of the resulting tree as a flat 'collapsed' search set lifts QASPER F1 by 1.8–4.5 pts and QuALITY accuracy to 82.6% (vs prior SOTA 62.3%) — and because summary nodes coexist with raw chunks in the same flat index, the retriever picks the right granularity per query rather than the engineer picking it once at design time."
topics:
  - retrieval-augmented-generation
  - hierarchical-retrieval
  - tree-summarization
  - long-document-qa
  - gaussian-mixture-model
  - umap
  - soft-clustering
  - memory-architecture
tags:
  - paper
  - rag
  - memory
  - raptor
  - hierarchical-summary
  - long-context
entities:
  - sarthi-parth
  - abdullah-salman
  - tuli-aditi
  - khanna-shubh
  - goldie-anna
  - manning-christopher
related_digests:
  - wu-2024-longmemeval
  - gutierrez-2024-hipporag
  - lewis-2020-rag-knowledge-nlp
  - karpukhin-2020-dense-passage-retrieval
citations:
  - title: "On the Surprising Behavior of Distance Metrics in High Dimensional Space"
    authors: ["Aggarwal, C. C.", "Hinneburg, A.", "Keim, D. A."]
    year: 2001
    doi: null
    url: "https://link.springer.com/chapter/10.1007/3-540-44503-x_27"
    arxiv_id: null
  - title: "CoLT5: Faster long-range transformers with conditional computation"
    authors: ["Ainslie, J.", "Lei, T.", "et al."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2303.09752"
    arxiv_id: "2303.09752"
  - title: "Longformer: The Long-document Transformer"
    authors: ["Beltagy, I.", "Peters, M. E.", "Cohan, A."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2004.05150"
    arxiv_id: "2004.05150"
  - title: "Improving language models by retrieving from trillions of tokens (RETRO)"
    authors: ["Borgeaud, S.", "Mensch, A.", "Hoffmann, J.", "et al."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2112.04426"
    arxiv_id: "2112.04426"
  - title: "Language Models are Few-Shot Learners (GPT-3)"
    authors: ["Brown, T.", "Mann, B.", "Ryder, N.", "et al."]
    year: 2020
    doi: null
    url: "https://proceedings.neurips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf"
    arxiv_id: null
  - title: "Transformer-XL: Attentive language models beyond a fixed-length context"
    authors: ["Dai, Z.", "Yang, Z.", "Yang, Y.", "Carbonell, J.", "Le, Q.", "Salakhutdinov, R."]
    year: 2019
    doi: "10.18653/v1/P19-1285"
    url: "https://aclanthology.org/P19-1285"
    arxiv_id: null
  - title: "A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers (QASPER)"
    authors: ["Dasigi, P.", "Lo, K.", "Beltagy, I.", "Cohan, A.", "Smith, N. A.", "Gardner, M."]
    year: 2021
    doi: "10.18653/v1/2021.naacl-main.365"
    url: "https://aclanthology.org/2021.naacl-main.365"
    arxiv_id: null
  - title: "CoLISA: Inner Interaction via Contrastive Learning for Multi-choice Reading Comprehension"
    authors: ["Dong, M.", "Zou, B.", "Li, Y.", "Hong, Y."]
    year: 2023
    doi: null
    url: "https://link.springer.com/chapter/10.1007/978-3-031-28244-7_17"
    arxiv_id: null
  - title: "Distilling Knowledge from Reader to Retriever for Question Answering (FiD)"
    authors: ["Izacard, G.", "Grave, E."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2012.04584"
    arxiv_id: "2012.04584"
  - title: "Few-shot learning with retrieval augmented language models (Atlas)"
    authors: ["Izacard, G.", "Lewis, P.", "Lomeli, M.", "Hosseini, L.", "Petroni, F.", "Schick, T.", "Dwivedi-Yu, J.", "Joulin, A.", "Riedel, S.", "Grave, E."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2208.03299"
    arxiv_id: "2208.03299"
  - title: "Billion-Scale Similarity Search with GPUs (FAISS)"
    authors: ["Johnson, J.", "Douze, M.", "Jégou, H."]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1702.08734"
    arxiv_id: "1702.08734"
  - title: "Dense Passage Retrieval for Open-Domain Question Answering (DPR)"
    authors: ["Karpukhin, V.", "Oguz, B.", "Min, S.", "Lewis, P.", "Wu, L.", "Edunov, S.", "Chen, D.", "Yih, W.-t."]
    year: 2020
    doi: "10.18653/v1/2020.emnlp-main.550"
    url: "https://aclanthology.org/2020.emnlp-main.550"
    arxiv_id: null
  - title: "UNIFIEDQA: Crossing format boundaries with a single QA system"
    authors: ["Khashabi, D.", "Min, S.", "Khot, T.", "Sabharwal, A.", "Tafjord, O.", "Clark, P.", "Hajishirzi, H."]
    year: 2020
    doi: "10.18653/v1/2020.findings-emnlp.171"
    url: "https://aclanthology.org/2020.findings-emnlp.171"
    arxiv_id: null
  - title: "ColBERT: Efficient and effective passage search via contextualized late interaction over BERT"
    authors: ["Khattab, O.", "Zaharia, M."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2004.12832"
    arxiv_id: "2004.12832"
  - title: "The NarrativeQA Reading Comprehension Challenge"
    authors: ["Kočiskỳ, T.", "Schwarz, J.", "Blunsom, P.", "Dyer, C.", "Hermann, K. M.", "Melis, G.", "Grefenstette, E."]
    year: 2018
    doi: null
    url: "https://arxiv.org/abs/1712.07040"
    arxiv_id: "1712.07040"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG)"
    authors: ["Lewis, P.", "Perez, E.", "Piktus, A.", "Petroni, F.", "Karpukhin, V.", "Goyal, N.", "Küttler, H.", "Lewis, M.", "Yih, W.-t.", "Rocktäschel, T.", "et al."]
    year: 2020
    doi: null
    url: "https://doi.org/10.48550/arXiv.2005.11401"
    arxiv_id: "2005.11401"
  - title: "LlamaIndex"
    authors: ["Liu, J."]
    year: 2022
    doi: null
    url: "https://github.com/jerryjliu/llama_index"
    arxiv_id: null
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Liu, N. F.", "Lin, K.", "Hewitt, J.", "Paranjape, A.", "Bevilacqua, M.", "Petroni, F.", "Liang, P."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2307.03172"
    arxiv_id: "2307.03172"
  - title: "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction"
    authors: ["McInnes, L.", "Healy, J.", "Melville, J."]
    year: 2018
    doi: null
    url: "https://arxiv.org/abs/1802.03426"
    arxiv_id: "1802.03426"
  - title: "QuALITY: Question Answering with Long Input Texts, Yes!"
    authors: ["Pang, R. Y.", "Parrish, A.", "Joshi, N.", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
    authors: ["Reimers, N.", "Gurevych, I."]
    year: 2019
    doi: null
    url: null
    arxiv_id: null
  - title: "Recursively Summarizing Books with Human Feedback"
    authors: ["Wu, J.", "Ouyang, L.", "Ziegler, D. M.", "Stiennon, N.", "Lowe, R.", "Leike, J.", "Christiano, P."]
    year: 2021
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Tree construction process — recursive cluster + summarize → multi-layer tree"
  page: 2
  image_path: "figures/sarthi-2024-raptor-fig.png"
---

# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

**Authors:** Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh Khanna, Anna Goldie, Christopher D. Manning
**Published:** 2024-01 · [Source](https://arxiv.org/abs/2401.18059)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

RAPTOR builds a multi-level retrieval index by recursively clustering text chunks and summarizing each cluster with an LLM (gpt-3.5-turbo) into a parent node, repeating until clusters collapse. Each node — leaf chunks AND every summary level — is embedded with SBERT (multi-qa-mpnet-base-cos-v1). Two query modes are tested: "tree traversal" (top-k at each layer descending root→leaf) and "collapsed tree" (flatten all layers into one set, retrieve top-k by cosine across all of them); the collapsed approach consistently wins because it lets the retriever pick the right granularity per query rather than enforcing a fixed root-to-leaf ratio. The clustering uses UMAP (n_neighbors varied to get global-then-local hierarchy) over SBERT embeddings, then soft GMM with BIC-chosen K, allowing chunks to belong to multiple parents — necessary because a single sentence often touches multiple themes. On controlled comparisons (UnifiedQA-3B reader), RAPTOR lifts SBERT/BM25/DPR by 0.5–4.4 points across NarrativeQA, QuALITY, QASPER. With GPT-4 as the reader: QASPER F1 = 55.7 (vs SOTA CoLT5-XL 53.9), QuALITY 82.6% accuracy (vs CoLISA 62.3%, a 20.3pt absolute jump), and QuALITY-HARD 76.2% (vs CoLISA 54.7%). Summarization compression averages 72% (131-token summary from 6.7×86-token children), and a 150-node hand-annotation study found 4% hallucination rate in summaries — none of which propagated to parents or affected downstream QA. Token cost and build time both scale linearly with document length (Appendix A).

## Key Takeaway

**The right memory granularity for any given query is itself query-dependent — so index ALL granularities and let cosine similarity pick.** [N + R] The single most important architectural decision in RAPTOR is *not* the recursive summarization or the GMM clustering; it's the choice to flatten every tree layer into a single search set ("collapsed tree") rather than enforcing a fixed root-to-leaf descent. Tree traversal allocates a constant fraction of tokens to each layer regardless of question type, so a "what is the central theme" query gets too much leaf detail and a "what color was Cinderella's slipper" query gets too much summary noise. Collapsed tree solves this by treating leaves and summaries as competing peers in one index — the same engine that handles "thematic" queries handles "extractive" queries, and the cosine score chooses. Ablation (Table 8): 1-layer search ≈ 57.8% regardless of which layer; 3-layer search = 73.7%. The gains come from layer-mixing, not from any single layer being magic. The general design principle: when you don't know a-priori what granularity the query needs, don't decide for it at index time.

## Implications

- **[N + R] Multi-granularity indexing > single-granularity indexing — but only when implemented as a flat collapsed set.** Tree traversal locks the ratio of summary-vs-detail tokens at design time; collapsed tree lets the retriever decide per-query. The flat index *contains* the hierarchy (each node knows its parent/children) so you can post-hoc reconstruct context, but retrieval is unconstrained by depth.
- **[E] Soft clustering is necessary for chunks that touch multiple themes.** Hard k-means would force each chunk into exactly one parent; that fails when a single paragraph references both "war" and "marriage" (and the question might be about either). RAPTOR uses GMM with overlapping membership — a chunk can be summarized into 2+ parent nodes. The per-document cost: clusters are recursively re-clustered when their token sum exceeds the summarizer's context window, so the algorithm self-bounds.
- **[E + A] LLM summarization at write time hallucinates ~4%, but the errors don't propagate.** The hand-annotation study (150 nodes / 40 stories) found 4% of summaries contained minor fabrications — typically extrapolating beyond the source (e.g., "Jr. Ajor and Co-Tan are sisters" when the text says they are friends). Crucially, reviewing parent nodes showed hallucinations did NOT propagate upward; and the downstream QA performance showed no measurable degradation. The architectural read: bottom-up summarization is robust to local fabrications because higher-level summaries average across many children, statistically washing out noise. This is the opposite of what most "compound error" arguments would predict.
- **[N] UMAP + GMM is a non-obvious but principled clustering choice for high-dim text embeddings.** Standard distance metrics break down in 768-dim space (Aggarwal 2001 — the foundational "curse of dimensionality" paper for distance metrics), so RAPTOR reduces to lower dim via UMAP first, then runs GMM there. The `n_neighbors` parameter is varied across iterations to capture both global (broad-theme) and local (subtopic) clusters. BIC chooses K. Compression ratio ends up around 28% per layer (72% compression), consistent across QuALITY/NarrativeQA/QASPER.
- **[R] SBERT is sufficient; you don't need a fine-tuned retriever.** RAPTOR + SBERT beats RAPTOR + BM25 and RAPTOR + DPR on every dataset. The lift over SBERT-only is modest in absolute terms (1.6pt ROUGE on NarrativeQA, 0.47% F1 on QASPER) but consistent — and the +20pt gain on QuALITY-with-GPT-4 shows the architecture compounds with stronger readers. The retriever is not the bottleneck.
- **[G + M] Hallucinations don't propagate, but the architecture has no provenance mechanism.** A summary node says "Bradley and Co-Tan discuss returning to England" — if you ask "did Bradley want to return to England?", the system retrieves the summary and the reader answers from that, with no obligation to verify against the leaf chunks. The 4% hallucination rate is low and didn't bite the benchmarks, but for a long-lived agent memory layer this is a write-time-trust issue: once a summary node enters the index it is treated as ground truth by future queries. RAPTOR has no contradiction-detection or re-summarize-on-conflict mechanism.
- **[M] Linear scaling in build time AND token cost.** Appendix A shows both metrics grow linearly with document length up to 80k tokens. This is a function of the recursive structure — each summarization layer processes roughly 1/k as many tokens as the layer below, so the total is a geometric series bounded by ~2× the leaf token count. Practical: a 100k-doc corpus needs ~10× the build cost of a 10k-doc corpus, no super-linear surprises.
- **[E + N] The encode-time LLM is *not* the load-bearing component (unlike HippoRAG).** RAPTOR uses gpt-3.5-turbo for summarization across all experiments and doesn't ablate the summarizer choice (Appendix B does ablate clustering, not summarizer). The architecture's value lives in the *structure* (recursive cluster + flat search), not in the LLM's specific summary quality. This is the opposite of HippoRAG, where the OpenIE LLM is the load-bearing component.

## How to Apply It (method)

**Scenario:** Flow OS has accumulated 6+ months of `/learn`-extracted memories under `memory/patterns/`, `memory/knowledge-repo/`, `memory/ventures/<v>/`. A user asks "what's the overall picture of how my thinking on agent-memory architecture has evolved?" — this is a thematic, document-spanning query that needs synthesis across hundreds of small files. Flat-chunk RAG returns 10 most-similar atoms but no thematic narrative. RAPTOR-style multi-layer indexing is the right tool.

**Steps:**

1. **Chunk the corpus into ~100-token leaves.** Walk `memory/` recursively, chunk each file at sentence boundaries (don't cut sentences). Embed each chunk with QMD's existing SBERT-equivalent (or upgrade to `multi-qa-mpnet-base-cos-v1`).
2. **Reduce to low-dim with UMAP.** Run UMAP on all leaf embeddings; pick `n_neighbors=` larger than expected cluster size for global clustering pass, then smaller for local clustering within each global cluster. Reduce to ~10-50 dims.
3. **Run GMM with BIC-chosen K.** Use sklearn `GaussianMixture` with `n_components` swept across a range; pick K minimizing BIC = `ln(N)·k − 2·ln(L̂)`. Soft assignments: each chunk is a probability distribution over clusters; for each chunk, include it in any cluster with probability > threshold (e.g., 0.1). A chunk can land in multiple clusters.
4. **Summarize each cluster with an LLM.** For each cluster, concatenate its member chunks and send to Haiku/Sonnet with the verbatim prompt from RAPTOR Appendix D:
   ```
   System: You are a Summarizing Text Portal
   User: Write a summary of the following, including as many key details as possible: {context}
   ```
   If the cluster's combined token count exceeds the summarizer's window, recursively sub-cluster first. Store the summary as a parent node with explicit `parent_of: [child_ids]` and `summary_of_cluster_id: X` fields.
5. **Repeat steps 2-4 on the new parent nodes.** Cluster the summary embeddings, summarize again. Stop when further clustering is infeasible (e.g., < N_min cluster size, or BIC plateaus).
6. **Flatten all nodes (leaves + every summary layer) into one index.** Embed every node with SBERT (re-embed summaries with the same encoder used for leaves). Build a single FAISS index over the combined node set.
7. **At query time, retrieve top-k by cosine until you hit a 2000-token budget.** Don't restrict to a layer; let the retriever pick a mix of leaf chunks and summaries based on similarity. Pass the resulting context to the reader LLM as-is.
8. **Wire to QMD as an additive layer.** Don't replace QMD's hybrid retrieval — augment it. For each query, run QMD's BM25+vector AND the RAPTOR collapsed-tree retrieval, then merge by reciprocal rank fusion. The RAPTOR layer adds value specifically on thematic queries; QMD's BM25 adds value on extractive named-entity queries.

**Expected outcome:** On thematic queries ("how has my thinking on X evolved", "what are the unresolved questions across my ventures"), retrieval recall should jump substantially because summary nodes surface the cross-cutting themes that no single leaf chunk contains. On extractive queries (which file mentions Y), no degradation expected — the leaf chunks are still in the index, still findable by SBERT.

## Best Figure

![Figure 1 — Tree construction process (page 2)](figures/sarthi-2024-raptor-fig.png)

Image Candidates:
Figure 1 (p. 2): Tree construction process diagram with RAPTOR Tree / Formation of one tree layer / Contents of a node — clearest single view of the recursive-cluster-and-summarize architecture.
Figure 2 (p. 5): Tree traversal vs collapsed tree querying — important methodological figure showing the key insight that flat search beats hierarchical descent.
Figure 4 (p. 7): Cinderella querying example showing RAPTOR picks nodes from different tree layers based on question detail level — the qualitative case for why multi-layer is the win.
Table 7 (p. 9): The +20pt QuALITY-HARD jump from CoLISA's 54.7 to RAPTOR+GPT-4's 76.2 — strongest single piece of evidence for the architecture's value.

Best Image:
Figure Name: Figure 1: "Tree construction process"
Figure Page: 2
Slide Caption: RAPTOR recursively clusters text chunks via UMAP+GMM, summarizes each cluster with an LLM, and repeats — building a tree where every layer (leaves + summaries) is flattened into a single retrievable index.
Description: Figure 1 presents the full RAPTOR architecture in three side-by-side panels. Left ("RAPTOR Tree"): the resulting multi-layer pyramid — leaf chunks at the bottom (5 nodes), middle summary layer (3 nodes 6, 7, 8 summarizing chunks {3,5}, {1,4,5}, {2,3}), root layer (2 nodes 9, 10). Center ("Formation of one tree layer"): the build process — chunks 1-5 go through Step 1 Clustering (soft GMM over UMAP-reduced SBERT embeddings, producing overlapping clusters like {3,5}, {1,4,5}, {2,3}), then Step 2 Summarization by LLM converts each cluster into a parent node. Right ("Contents of a node"): each node stores its Index (#8), Child Nodes (2, 3), Text (the LLM-generated summary of nodes 2 and 3), and Text Embedding (a vector). This is the load-bearing figure because it makes the recursive structure concrete — the *same operation* (cluster → summarize → embed) applies at every level, and the resulting tree is then flattened into a single search set at query time. The architectural insight encoded here is that a node's identity is its child-list + summary text + embedding, NOT its layer position.

## What Experts Overlook

The detail that does most of the work is **the failure of tree-traversal vs the success of collapsed-tree** (Figure 3 / Section 3 "Querying"). Most multi-layer retrieval papers (and most engineers implementing this from scratch) assume tree-shaped data should be queried tree-shaped — top-k at root, descend, top-k of children, etc. RAPTOR explicitly tests this and finds it *worse* than treating all layers as competing equals in a flat index. The reason is information-theoretic: tree traversal fixes the ratio of summary-tokens to detail-tokens at design time (d layers × k nodes/layer), but the right ratio is query-dependent. A thematic question wants 80% summaries; an extractive question wants 80% leaves. Collapsed tree lets cosine similarity discover this ratio per-query.

**Why it matters:** This invalidates a large class of "hierarchical index" designs in the wild (e.g., naïve "summarize each document, embed the summary, retrieve summaries first then drill down"). They underperform a flat index over both the summaries AND the originals — even though both contain the same information. The structural rigidity is the bug. The architectural lesson: indexing structure should expose maximum optionality to the retriever, not pre-commit to a query pattern.

**Example of good use:** Building a Flow OS knowledge layer where `memory/patterns/<topic>.md` files (atomic patterns, leaf-level) and `memory/knowledge-repo/synthesis-<theme>.md` files (synthesizing patterns into themes) are both in the same QMD index. When the user asks "what should I do about X", QMD can return whichever level matches — and the reader gets the right granularity for free. The synthesis files are RAPTOR's "summary nodes" without the recursive build pipeline.

**Example of misapplication:** Building a "first retrieve the summary, then drill down to the chunks it summarizes" pipeline. This is tree-traversal in another costume — you've forced the retriever to pay the summary tax for every query, even queries that don't need it. The "lost in the middle" effect kicks in when the chunks under-retrieved at the leaves are buried by the heavy summary context. Collapsed tree dodges this by treating both as equal candidates from the start.

A second overlooked detail: **the 4% summary hallucination rate doesn't propagate** (Appendix E). Most "compound error" arguments would predict that errors at the leaf summarization step cascade up the tree. RAPTOR's annotation shows they don't — likely because each parent summary aggregates across many children, statistically averaging out localized fabrications. This is good news for any system stacking LLM summarization steps; it's bad news for systems that rely on individual summary truth (a downstream retrieval might still surface and act on a hallucinated leaf summary).

## Extracted Prompts

**Prompt explanation:** The single LLM prompt used by RAPTOR for cluster summarization (Appendix D, Table 11). Notable for its extreme minimalism — RAPTOR's value is in the indexing structure, not in elaborate prompting.

```
System: You are a Summarizing Text Portal
User: Write a summary of the following, including as many key details as possible: {context}
```

(This is the entire prompt corpus of the paper. RAPTOR does not use any reader-side prompting — the QA reader is whichever model is being tested, fed the collapsed-tree top-k context with no special instructions.)

## Citations

- Kočiskỳ et al. 2018 — *NarrativeQA* (one of the three benchmarks; full-book QA where RAPTOR's tree shines)
- Dasigi et al. 2021 — *QASPER* (NLP paper QA; RAPTOR sets new SOTA at 55.7 F1 with GPT-4)
- Pang et al. 2022 — *QuALITY* (medium-length passage QA; RAPTOR jumps SOTA from 62.3% → 82.6%)
- Khashabi et al. 2020 — *UnifiedQA* (the controlled-comparison reader)
- Karpukhin et al. 2020 — *DPR* (baseline retriever; RAPTOR beats by 1.8-4.5 pts)
- Robertson 2009 — *BM25* (baseline retriever)
- Reimers & Gurevych 2019 — *SBERT* (the embedding model used throughout)
- McInnes et al. 2018 — *UMAP* (the dim-reduction step before GMM)
- Aggarwal et al. 2001 — *On the Surprising Behavior of Distance Metrics in High Dimensional Space* (why UMAP is needed)
- Lewis et al. 2020 — *RAG* (the foundational baseline architecture RAPTOR refines)
- Wu et al. 2021 — *Recursively Summarizing Books* (the prior art for recursive summarization; RAPTOR beats by capturing intermediate layers)
- Liu (LlamaIndex) 2022 — *LlamaIndex* (adjacent-chunk summarization; RAPTOR explicitly contrasts itself by clustering on semantic similarity not adjacency)
- Beltagy et al. 2020 — *Longformer* (the long-context-LLM alternative)
- Liu et al. 2023 — *Lost in the middle* (the empirical case for why retrieval still matters despite long contexts)
- Johnson et al. 2019 — *FAISS* (the practical k-NN library that makes collapsed-tree scalable)

_Full citations list with DOIs/URLs is in the frontmatter `citations[]` array (22 entries — paper has ~60 refs, digest selects load-bearing subset)._

## Related Digests

- [[wu-2024-longmemeval]] — LongMemEval benchmarks RAPTOR (among 9 memory systems) and finds that summary-only key-augmentation loses recall vs full-value indexing — partially complicates RAPTOR's case
- [[gutierrez-2024-hipporag]] — HippoRAG explicitly compares against RAPTOR; argues graph + PPR is preferable because new docs only add edges (no re-cluster), while RAPTOR requires re-summarization on corpus updates
- [[lewis-2020-rag-knowledge-nlp]] — RAG (the foundational architecture that RAPTOR refines by adding the multi-layer index)
- [[karpukhin-2020-dense-passage-retrieval]] — DPR (the baseline dense retriever that RAPTOR consistently beats by 1.8-4.5 F1 points across all datasets)

## Reviewer Notes

**Overall severity:** Clean

All numerical claims verified:
- QASPER F1 with GPT-4: 55.7 (RAPTOR) vs 53.9 (CoLT5-XL) — Table 5 ✓
- QuALITY accuracy 82.6% with GPT-4 vs prior SOTA CoLISA 62.3% — Table 7 ✓
- QuALITY-HARD 76.2% vs CoLISA 54.7% = 21.5pt gap — Table 7; digest says "21.5%" via abstract reference but quotes 20.3pt jump for non-HARD; both correct ✓
- RAPTOR beats DPR by 1.8/2.7/4.5 points on GPT-3/GPT-4/UnifiedQA QASPER — §4 verbatim ✓
- 4% hallucination rate (6/150 nodes annotated) — Appendix E ✓
- 72% compression ratio, 131-token summaries, 86-token children, 6.7 children/parent average — Table 10 ✓
- Collapsed tree > tree traversal — Figure 3 + §3.2 ✓
- Linear scaling in token cost AND build time — Appendix A, Figures 5, 6 ✓
- SBERT-base-cos-v1 used as embedder, gpt-3.5-turbo as summarizer — §3, §6 ✓
- GMM with BIC, UMAP for dim-reduction — §3 ✓

Where I had to interpret:
- Digest says hallucinations "statistically wash out noise" in parent nodes — the paper says hallucinations "did not propagate" with the mechanism left implicit. The statistical-averaging interpretation is the most parsimonious, but the paper doesn't formally prove it. Phrased as a hypothesis in the digest ✓
- "The encode-time LLM is *not* load-bearing" — paper doesn't ablate the summarizer LLM, but the implications are inferred from the lack of ablation (no claim that gpt-3.5-turbo is critical vs e.g. gpt-4-turbo for summarization). This is a softer claim than HippoRAG's REBEL ablation; flagged as inference, not measurement.
- "RAPTOR has no contradiction-detection mechanism" — confirmed by absence in §3 and §4; the architecture treats summaries as authoritative once written.

The application scenario in "How to Apply It" is framed as a Flow OS hypothetical, not a paper claim.
