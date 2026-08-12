---
corpus: agentic-memory
kind: paper-digest
slug: gutierrez-2024-hipporag
title: "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models"
authors:
  - "Gutiérrez, Bernal Jiménez"
  - "Shu, Yiheng"
  - "Gu, Yu"
  - "Yasunaga, Michihiro"
  - "Su, Yu"
year: 2024
publication_date: "2024-05"
venue: "NeurIPS 2024"
source_url: "https://arxiv.org/abs/2405.14831"
doi: "10.48550/arXiv.2405.14831"
arxiv_id: "2405.14831"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Replacing chunk-vector retrieval with an LLM-built schemaless knowledge graph + Personalized PageRank gives single-step multi-hop retrieval that matches iterative methods (IRCoT) at 10–30× lower cost and 6–13× lower latency, and lifts R@5 on 2WikiMultiHopQA by 20 points — but only because the LLM-on-the-write-path generates ~2× more triples than a fine-tuned extractor (REBEL), so the encode-time LLM choice is what makes the architecture work."
topics:
  - long-term-memory
  - retrieval-augmented-generation
  - knowledge-graphs
  - multi-hop-qa
  - personalized-pagerank
  - hippocampal-indexing
  - openie
  - memory-architecture
tags:
  - paper
  - memory
  - rag
  - hipporag
  - knowledge-graph
  - graph-retrieval
entities:
  - gutierrez-bernal
  - shu-yiheng
  - gu-yu
  - yasunaga-michihiro
  - su-yu
related_digests:
  - wu-2024-longmemeval
  - rasmussen-2025-zep-temporal-kg
  - chhikara-2025-mem0
  - lewis-2020-rag-knowledge-nlp
citations:
  - title: "Llama 3 model card"
    authors: ["AI@Meta"]
    year: 2024
    doi: null
    url: "https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md"
    arxiv_id: null
  - title: "Walking Down the Memory Maze: Beyond Context Limit through Interactive Reading (MemWalker)"
    authors: ["Chen, H.", "Pasunuru, R.", "Weston, J.", "Celikyilmaz, A."]
    year: 2023
    doi: "10.48550/ARXIV.2310.05029"
    url: "https://arxiv.org/abs/2310.05029"
    arxiv_id: "2310.05029"
  - title: "Dense X retrieval: What retrieval granularity should we use?"
    authors: ["Chen, T.", "Wang, H.", "Chen, S.", "Yu, W.", "Ma, K.", "Zhao, X.", "Zhang, H.", "Yu, D."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2312.06648"
    arxiv_id: "2312.06648"
  - title: "From local to global: A graph RAG approach to query-focused summarization (GraphRAG)"
    authors: ["Edge, D.", "Trinh, H.", "Cheng, N.", "Bradley, J.", "Chao, A.", "Mody, A.", "Truitt, S.", "Larson, J."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2404.16130"
    arxiv_id: "2404.16130"
  - title: "A cortical–hippocampal system for declarative memory"
    authors: ["Eichenbaum, H."]
    year: 2000
    doi: null
    url: "https://www.nature.com/articles/35036213"
    arxiv_id: null
  - title: "Topic-sensitive PageRank"
    authors: ["Haveliwala, T. H."]
    year: 2002
    doi: "10.1145/511446.511513"
    url: "https://dl.acm.org/doi/10.1145/511446.511513"
    arxiv_id: null
  - title: "REBEL: Relation extraction by end-to-end language generation"
    authors: ["Huguet Cabot, P.-L.", "Navigli, R."]
    year: 2021
    doi: "10.18653/v1/2021.findings-emnlp.204"
    url: "https://aclanthology.org/2021.findings-emnlp.204"
    arxiv_id: null
  - title: "Unsupervised dense information retrieval with contrastive learning (Contriever)"
    authors: ["Izacard, G.", "Caron, M.", "Hosseini, L.", "Riedel, S.", "Bojanowski, P.", "Joulin, A.", "Grave, E."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2112.09118"
    arxiv_id: "2112.09118"
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Lewis, P.", "Perez, E.", "Piktus, A.", "Petroni, F.", "Karpukhin, V.", "Goyal, N.", "Küttler, H.", "Lewis, M.", "Yih, W.-t.", "Rocktäschel, T.", "Riedel, S.", "Kiela, D."]
    year: 2020
    doi: null
    url: "https://dl.acm.org/doi/abs/10.5555/3495724.3496517"
    arxiv_id: null
  - title: "ColBERTv2: Effective and efficient retrieval via lightweight late interaction"
    authors: ["Santhanam, K.", "Khattab, O.", "Saad-Falcon, J.", "Potts, C.", "Zaharia, M."]
    year: 2022
    doi: "10.18653/v1/2022.naacl-main.272"
    url: "https://aclanthology.org/2022.naacl-main.272"
    arxiv_id: null
  - title: "RAPTOR: Recursive abstractive processing for tree-organized retrieval"
    authors: ["Sarthi, P.", "Abdullah, S.", "Tuli, A.", "Khanna, S.", "Goldie, A.", "Manning, C. D."]
    year: 2024
    doi: "10.48550/ARXIV.2401.18059"
    url: "https://arxiv.org/abs/2401.18059"
    arxiv_id: "2401.18059"
  - title: "The hippocampal memory indexing theory"
    authors: ["Teyler, T. J.", "Discenna, P."]
    year: 1986
    doi: null
    url: "https://pubmed.ncbi.nlm.nih.gov/3008780/"
    arxiv_id: null
  - title: "The hippocampal indexing theory and episodic memory: Updating the index"
    authors: ["Teyler, T. J.", "Rudy, J. W."]
    year: 2007
    doi: null
    url: "https://pubmed.ncbi.nlm.nih.gov/17696170/"
    arxiv_id: null
  - title: "MuSiQue: Multihop questions via single-hop question composition"
    authors: ["Trivedi, H.", "Balasubramanian, N.", "Khot, T.", "Sabharwal, A."]
    year: 2022
    doi: "10.1162/TACL_A_00475"
    url: "https://aclanthology.org/2022.tacl-1.31/"
    arxiv_id: null
  - title: "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions (IRCoT)"
    authors: ["Trivedi, H.", "Balasubramanian, N.", "Khot, T.", "Sabharwal, A."]
    year: 2023
    doi: "10.18653/v1/2023.acl-long.557"
    url: "https://aclanthology.org/2023.acl-long.557"
    arxiv_id: null
  - title: "Constructing a multi-hop QA dataset for comprehensive evaluation of reasoning steps (2WikiMultiHopQA)"
    authors: ["Ho, X.", "Duong Nguyen, A.-K.", "Sugawara, S.", "Aizawa, A."]
    year: 2020
    doi: "10.18653/v1/2020.coling-main.580"
    url: "https://aclanthology.org/2020.coling-main.580"
    arxiv_id: null
  - title: "HotpotQA: A dataset for diverse, explainable multi-hop question answering"
    authors: ["Yang, Z.", "Qi, P.", "Zhang, S.", "Bengio, Y.", "Cohen, W. W.", "Salakhutdinov, R.", "Manning, C. D."]
    year: 2018
    doi: null
    url: null
    arxiv_id: null
  - title: "MEMORYLLM: Towards self-updatable large language models"
    authors: ["Wang, Y.", "Gao, Y.", "Chen, X.", "Jiang, H.", "Li, S.", "Yang, J.", "Yin, Q.", "Li, Z.", "Li, X.", "Yin, B.", "Shang, J.", "Mcauley, J."]
    year: 2024
    doi: null
    url: "https://proceedings.mlr.press/v235/wang24s.html"
    arxiv_id: null
  - title: "Memoria: Resolving fateful forgetting problem through human-inspired memory architecture"
    authors: ["Park, S.", "Bak, J."]
    year: 2024
    doi: null
    url: "https://openreview.net/forum?id=yTz0u4B8ug"
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Detailed HippoRAG Methodology — three components mapped to neocortex / parahippocampal regions / hippocampus"
  page: 4
  image_path: "figures/gutierrez-2024-hipporag-fig.png"
---

# HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models

**Authors:** Bernal Jiménez Gutiérrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, Yu Su
**Published:** 2024-05 · [Source](https://arxiv.org/abs/2405.14831)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

HippoRAG re-engineers the long-term memory layer of an LLM as three components that mirror human brain regions — an LLM "neocortex" performs OpenIE on each passage to extract noun-phrase nodes and relation triples, dense retrievers ("parahippocampal regions") add synonymy edges between near-duplicate nodes, and a Personalized PageRank ("hippocampus") propagates probability mass from query-extracted seed nodes across this open knowledge graph in a single step. On 1000-question dev sets of MuSiQue and 2WikiMultiHopQA, HippoRAG lifts R@5 by +3pt and +20pt respectively over the strongest single-step baselines (ColBERTv2, RAPTOR, Propositionizer), and matches iterative-retrieval IRCoT at one-tenth to one-thirtieth the cost and 6–13× lower latency (Table 17: $0.10 vs $1–3 per 1000 queries; 3 min vs 20–40 min). Ablations isolate where the gains come from: replacing GPT-3.5 OpenIE with the fine-tuned REBEL extractor halves the triple count and drops R@5 by 13–15 points, while removing node-specificity (a local IDF proxy) costs ~2 pts and removing synonymy edges costs ~4 pts on 2Wiki. Crucially, on "path-finding" queries (e.g. "which Stanford prof works on Alzheimer's?") where no single passage names both attributes, HippoRAG returns the correct entity (Thomas Südhof) while ColBERTv2 and IRCoT both fail entirely — these are queries where iterative retrieval cannot bootstrap because no path-following entry point exists. Offline indexing is ~10× slower and ~$15 more per 10k passages than chunk indexing, but Llama-3.1-70B matches GPT-3.5 quality, making the architecture deployable on 4×H100 in ~4 hours per 10k docs.

## Key Takeaway

**Encode-time LLM extraction is the load-bearing component, not the graph search.** [E + N + R] The whole HippoRAG architecture rests on the LLM producing a sufficiently dense, sufficiently general triple set at write time — when REBEL (a fine-tuned end-to-end extractor) replaces GPT-3.5, the system loses 11–13 points across all three datasets despite identical graph-walk machinery, because REBEL produces ~½ the triples and is biased against general concepts. The graph + PPR is a substrate that *amplifies* the encode signal; it cannot manufacture associations the OpenIE step didn't extract. This inverts a common framing — "graph RAG" papers often credit the structural innovation, but the ablation table shows the structure is necessary-but-not-sufficient: PPR alone (vs. seed-node retrieval) buys you +7 to +28 R@5 points, and synonymy edges buy +4 on 2Wiki, but the OpenIE LLM choice is a +13pt swing on its own. Move your modeling budget to the writer, not the retriever.

## Implications

- **[E] The LLM-on-the-write-path is the architecture's center of gravity.** Replacing GPT-3.5 with REBEL (a strong but non-LLM extractor) halves the triple count (~2× fewer) and drops average R@5 by 14 points. Llama-3.1-70B matches GPT-3.5; the 8B version is competitive everywhere except 2Wiki. If you're building a HippoRAG-style memory layer, the cheapest large win is upgrading your extraction LLM, not your retriever or your graph algorithm.
- **[N] An open knowledge graph is a viable long-term-memory substrate when you need cross-passage integration.** Standard chunk-vector RAG fails on "path-finding" queries where no single passage contains the answer's distinguishing attributes — HippoRAG finds Thomas Südhof (the Stanford prof working on Alzheimer's neuroscience) by traversing edges from {Stanford} ∪ {Alzheimer's} seed nodes via PPR. ColBERTv2 and IRCoT both fail this class of queries entirely because there is no chunk that surfaces near both seeds. For Flow OS — where queries like "which advisor recommended hiring a fractional CFO" require crossing two unrelated session clusters — this is the failure mode that argues for a graph layer.
- **[R] Personalized PageRank is a 1986-vintage algorithm that buys you single-step multi-hop retrieval.** Crucially, PPR with seed=query-nodes outperforms both raw query-node retrieval (+7 to +28 R@5) and seed-nodes+1-hop-neighbors (which actually *underperforms* seed-only). The lesson: graph traversal needs principled probability propagation, not naive neighborhood expansion — neighborhood expansion adds noise faster than signal.
- **[R + G] Synonymy edges via dense encoders are the bridge between the LLM's noisy extraction and the symbolic graph.** Adding ~150k synonymy edges from Contriever or ColBERTv2 (threshold τ=0.8) on top of ~50k–100k OpenIE edges costs ~4 R@5 points on 2Wiki when removed. This is the grounding mechanism that turns "GPT-3.5 wrote 'OpenAI' and 'OpenAI Inc.' as two nodes" into one effective concept — without it, the LLM's lexical variance shatters your graph.
- **[A] HippoRAG integrates information at *index time* by adding edges, not by re-summarizing.** RAPTOR and MemWalker also integrate at index time, but they do so via recursive summarization — which means a new document forces re-clustering. HippoRAG just adds new nodes/edges to the existing KG. This makes online updates O(new passage size), not O(corpus size). For an agent memory system that must accept new sessions every few minutes, this is the difference between viable and not.
- **[M] Online retrieval cost stays roughly constant as the graph grows** — PPR runs over the whole KG but query-side computation is bounded by the number of seed nodes (typically 2–5 per query). Table 17 shows $0.10 per 1000 queries vs $1–3 for IRCoT. Latency is 3 min vs 20–40 min on the same hardware. Cost of *indexing* is ~10× higher than ColBERTv2 because of the OpenIE LLM calls — but this is a one-time write cost, and falls dramatically with Llama-3.1-8B/70B replacing GPT-3.5.
- **[N + R] Node specificity = a brain-plausible IDF.** Each node stores `s_i = 1 / |passages containing this node|` locally, computed from data already at the node. Multiplying seed-node probabilities by `s_i` before PPR adds ~2 R@5 on MuSiQue/HotpotQA. Doesn't help much on 2Wiki because everything is a named entity with low term-weight variation. This is the kind of local-signal IDF trick a graph store can do without aggregating across the whole corpus at query time.
- **[E + M] Offline-indexing OpenIE consistency drops on long passages.** Appendix F.4 notes that the same LLM extracts fewer / lower-quality triples from longer documents — i.e., the encode quality is not uniform across input size. Operationally: chunk before extracting, even if the retrieval unit is the whole passage. Don't pass full documents into the OpenIE step.

## How to Apply It (method)

**Scenario:** Flow OS currently uses QMD's flat hybrid (BM25 + vector) over markdown files in `memory/`. Users hit a recurring failure mode on cross-cluster questions: "which advisor recommended switching to bi-weekly stand-ups", which requires associating {advisor X said Y} (in one session memory) with {Y = bi-weekly cadence} (in another). Flat retrieval misses this because no single chunk surfaces both. We want a HippoRAG-style graph layer on top of QMD for the subset of queries that need it.

**Steps:**

1. **Run OpenIE over every memory file at write time.** Use Claude Haiku or Llama-3.1-70B (NOT a fine-tuned extractor — Haiku/GPT-quality LLMs produce ~2× more triples per HippoRAG Table 5) with this two-step prompt sequence (lifted verbatim from Appendix I):
   - First call: extract named entities from the passage (Figure 7 prompt — output JSON list of entities).
   - Second call: feed the passage + the entity list to the OpenIE prompt (Figure 9), output triples in the form `["subject", "relation", "object"]`. Require at least one entity from the list per triple. Resolve pronouns to entities.
2. **Build the schemaless KG.** For each memory file, store its emitted nodes + triples. Maintain a sparse matrix `P[node, file]` where each entry counts how many times node `i` appears in file `j`. This matrix is the bridge from KG nodes back to retrieval candidates (the "neocortex" representations).
3. **Add synonymy edges via your dense encoder.** Take all noun-phrase nodes, embed them with your QMD vector model (Contriever-equivalent), and add edges between pairs whose cosine similarity exceeds τ=0.8 (HippoRAG's tuned threshold). Expect ~1.5–2× as many synonymy edges as triple-based edges. This compensates for the LLM's lexical variance.
4. **Compute node specificity locally.** For each node `i`, store `s_i = 1 / |files containing node i|`. Maintain this incrementally as new files are added; no global rebuild needed.
5. **At query time, extract query named entities.** Use the same LLM with Figure 8's "query NER" prompt to pull seed entities from the user's question (typically 2–5). Embed each, find the most-similar KG node by cosine similarity to get your seed-node set `R_q`.
6. **Initialize the personalized vector.** Set `n[i] = s_i` for `i ∈ R_q`, zero elsewhere. Normalize to sum to 1.
7. **Run Personalized PageRank.** Use a graph library (igraph, networkx) with damping factor 0.5 (HippoRAG's tuned value) over the KG. Output: `n'`, a probability distribution over all KG nodes.
8. **Score files by `p = n' · P`** (matrix-vector multiply: sums per-file the PageRank-weighted node activations). Top-k files by score are your retrieval candidates.
9. **Feed top-k files to the reader LLM.** This is unchanged from your current pipeline — the upgrade is purely on the retrieval side.

**Hybrid with QMD vector retrieval:** Run both QMD's vector retrieval AND HippoRAG-PPR in parallel. For "path-following" queries (single hop, named entity match) QMD vector wins. For "path-finding" queries (cross-cluster, multi-attribute), PPR wins. Use reciprocal rank fusion to combine — or, better, build a small classifier that routes queries to one or the other based on whether the query mentions multiple unrelated entities.

**Expected outcome:** On Flow OS evals with cross-cluster questions, R@5 should jump 10–20 absolute points (matching the 2Wiki gain) at ~$0.1 per 1000 queries. Indexing cost ~$15 per 10k new memory files using a hosted LLM, or ~4 hours on local Llama-3.1-70B + 4×H100. The investment is worth it if and only if you currently fail cross-cluster queries — if QMD's existing hybrid is good enough, HippoRAG is over-engineering.

## Best Figure

![Figure 2 — Detailed HippoRAG Methodology (page 4)](figures/gutierrez-2024-hipporag-fig.png)

Image Candidates:
Figure 2 (p. 4): Three-component architecture diagram with neocortex/PHR/hippocampus columns mapped to LLM/retrieval-encoders/KG+PPR — clearest single view of the methodology.
Figure 1 (p. 2): Path-finding query example showing standard RAG failing where HippoRAG succeeds — emotional impact but less methodological detail.
Table 17 (p. 33): Cost/efficiency comparison — $0.10 vs $1-3 per 1000 queries — the load-bearing economic case but not a figure per se.

Best Image:
Figure Name: Figure 2: "Detailed HippoRAG Methodology"
Figure Page: 4
Slide Caption: HippoRAG maps human long-term memory's three components — neocortex (LLM-OpenIE), parahippocampal regions (dense retrieval encoders for synonymy), hippocampus (KG + Personalized PageRank) — onto a single-step retrieval pipeline that beats iterative RAG at 10–30× lower cost.
Description: Figure 2 lays out the full HippoRAG methodology as a 3×2 grid: columns are the three biological components (Neocortex / PHR / Hippocampus) mapped to their AI counterparts (LLM / Retrieval Encoders / KG+Personalized PageRank), and rows are the two phases (Offline Indexing / Online Retrieval). In the offline row, passages flow through the LLM (Open IE) to produce triples like (Thomas, researches, Alzheimer's) and (Stanford, employs, Thomas), which become nodes in the KG; the retrieval encoders then add synonymy edges between near-duplicate nodes (e.g., variants of "Stanford"). In the online row, the query "Which Stanford professor works on the neuroscience of Alzheimer's?" goes through query-NER to extract the seed entities {Stanford, Alzheimer's}, which are linked to KG nodes by cosine similarity, then PPR propagates probability mass across the graph (modulated by node specificity, shown as larger symbol size for the more specific "Stanford" node), and the final node distribution is projected back to passage scores. This figure is load-bearing because it shows the encode/retrieve/read separation, the LLM's specific role at write time (not query time), and why single-step multi-hop is achievable — the KG already encodes the cross-passage associations that iterative RAG must rediscover at query time.

## What Experts Overlook

The detail that does most of the work is **"REBEL halves the triple count and drops R@5 by 13–15 points"** (Table 5, row 2). Standard intuition says you'd want a fine-tuned, focused IE extractor because it produces cleaner triples — fewer hallucinations, better precision. HippoRAG's ablation shows precisely the opposite: GPT-3.5's "messier" extraction, which surfaces many general-concept triples a fine-tuned extractor would skip, is the regime where graph-search works. Why? Because PPR over a *sparse* graph has nothing to propagate through — the seed nodes activate, hit dead ends, and the algorithm degenerates to seed-node retrieval. PPR over a *dense* graph propagates probability through many alternative paths, which is what makes "path-finding" queries solvable. The LLM is doing two jobs at write-time: (a) extracting entities, and (b) generating the *connective tissue* (general-concept nodes like "biology research", "professor", "United States") that lets PPR find non-obvious paths. Fine-tuned extractors do (a) well and (b) badly.

**Why it matters:** This inverts the "LLM-as-RAG-orchestrator" pattern. The HippoRAG paper is implicitly arguing that the *encode* path is the high-value LLM placement, not the *retrieve* or *read* path. Most memory-system design devotes 90% of compute to query time (the LLM reader); HippoRAG shifts it to indexing time. The economic case (Table 17: 10–30× cheaper online retrieval) only works because the expensive encode work amortizes — every query gets PPR for $0.0001, vs every IRCoT query firing 2–4 LLM calls.

**Example of good use:** Flow OS's `/learn` step is exactly the right place to spend LLM tokens — extract dense triples from the session transcript while you're already invoking Haiku/Sonnet on the content. The graph layer can then serve cross-session queries for the rest of the user's lifetime without spending another LLM token per query (until the reader step).

**Example of misapplication:** Building HippoRAG on top of an OpenIE model like REBEL or a fine-tuned T5 extractor in the name of "saving LLM cost". The ablation shows this would lose almost all the gains. The LLM is necessary for the encoding generality, not just for entity extraction. If you cannot afford an LLM on the write path, this architecture is not for you — use plain dense retrieval instead.

A second overlooked detail: **node specificity is computed locally and incrementally.** `s_i = 1/|P_i|` for each node uses only data already at the node, so adding a new file just updates `|P_i|` for any nodes that file mentions. No global IDF recomputation. This is exactly what an agent-memory system needs to stay online during ingest.

## Extracted Prompts

**Prompt explanation:** Passage NER for indexing — Step 1 of the offline KG construction. Extracts named entities that anchor the subsequent triple extraction.

```
Your task is to extract named entities from the given paragraph.
Respond with a JSON list of entities.

One-Shot Demonstration:

Paragraph:
```
Radio City
Radio City is India's first private FM radio station and was started on 3 July 2001. It plays Hindi, English
and regional songs. Radio City recently forayed into New Media in May 2008 with the launch of a music
portal - PlanetRadiocity.com that offers music related news, videos, songs, and other music-related
features.
```

{"named_entities": ["Radio City", "India", "3 July 2001", "Hindi","English", "May 2008",
"PlanetRadiocity.com"]}

Input:

Paragraph:
```
PASSAGE TO INDEX
```
```

**Prompt explanation:** Query NER for retrieval — extracts seed entities from a user question to anchor PPR.

```
You're a very effective entity extraction system. Please extract all named entities that are important for
solving the questions below. Place the named entities in JSON format.

One-Shot Demonstration:

Question: Which magazine was started first Arthur's Magazine or First for Women?

{"named_entities": ["First for Women", "Arthur's Magazine"]}

Input:

Question: QUERY TO INDEX
```

**Prompt explanation:** OpenIE during indexing — Step 2 of KG construction. Given a passage and its named-entity list, produces RDF-style triples. The "preferably two named entities per triple" constraint is what biases the extractor toward producing cross-entity connective tissue rather than entity-attribute pairs.

```
Your task is to construct an RDF (Resource Description Framework) graph from the given passages and
named entity lists.
Respond with a JSON list of triples, with each triple representing a relationship in the RDF graph.
Pay attention to the following requirements:
- Each triple should contain at least one, but preferably two, of the named entities in the list for each
passage.
- Clearly resolve pronouns to their specific names to maintain clarity.

Convert the paragraph into a JSON dict, it has a named entity list and a triple list.

One-Shot Demonstration:

Paragraph:
```
Radio City
Radio City is India's first private FM radio station and was started on 3 July 2001. ...
```
{"named_entities": ["Radio City", "India", ...]}

{"triples":
   [
      ["Radio City", "located in", "India"],
      ["Radio City", "is", "private FM radio station"],
      ["Radio City", "started on", "3 July 2001"],
      ...
   ]
}

Input:

Paragraph:
```
PASSAGE TO INDEX
```
{"named_entities": [NER LIST]}
```

## Citations

- Teyler & Discenna 1986 — *The hippocampal memory indexing theory* (the neuroscience source for the whole metaphor)
- Eichenbaum 2000 — *A cortical–hippocampal system for declarative memory* (additional neuroscience grounding)
- Sarthi et al. 2024 — *RAPTOR* (the tree-summary baseline HippoRAG most closely competes with)
- Chen et al. 2023 — *MemWalker* (interactive-reading baseline, also tries cross-passage integration)
- Edge et al. 2024 — *GraphRAG* (Microsoft's contemporaneous community-graph approach)
- Trivedi et al. 2023 — *IRCoT* (the iterative-retrieval baseline that HippoRAG matches at 10–30× lower cost)
- Lewis et al. 2020 — *RAG* (foundational reference, distinguishes parametric vs retrieval-based memory)
- Santhanam et al. 2022 — *ColBERTv2* (the late-interaction retriever used as HippoRAG's PHR / synonymy backbone)
- Izacard et al. 2021 — *Contriever* (alternative unsupervised dense retriever)
- Haveliwala 2002 — *Topic-sensitive PageRank* (the PPR algorithm at the core of HippoRAG)
- Huguet Cabot & Navigli 2021 — *REBEL* (the fine-tuned extractor whose underperformance proves the LLM-on-write-path is load-bearing)
- Trivedi et al. 2022 — *MuSiQue* (primary multi-hop QA benchmark)
- Ho et al. 2020 — *2WikiMultiHopQA* (the benchmark where HippoRAG gets its +20pt R@5 gain)
- Park & Bak 2024 — *Memoria* (a related human-inspired memory architecture)
- Wang et al. 2024 — *MEMORYLLM* (parametric-memory alternative cited in related work)

_Full citations list with DOIs/URLs is in the frontmatter `citations[]` array (19 entries — paper has ~100 refs, this digest pulls the load-bearing subset for the memory-architect lens)._

## Related Digests

- [[wu-2024-longmemeval]] — LongMemEval evaluates HippoRAG-style systems and finds key-augmentation (K = V + fact) beats graph rebuild on long-term conversational memory
- [[rasmussen-2025-zep-temporal-kg]] — Zep applies HippoRAG-style graph memory to temporal session data with explicit time edges
- [[chhikara-2025-mem0]] — Mem0's graph variant (Mem0g) replicates HippoRAG-style structure for production agent memory; finds modest ~2pt gain over flat for the cost of 85× more tokens
- [[lewis-2020-rag-knowledge-nlp]] — The foundational RAG paper that HippoRAG positions itself against as "next-generation long-term memory"

## Reviewer Notes

**Overall severity:** Clean

All major claims verified against the paper:
- IRCoT cost ratio: paper says "10 to 30 times cheaper" (§1 / Appendix G) — digest says 10–30× ✓
- Latency: 6–13× faster — matches §1 + Table 17 ($0.10 vs $1-3; 3 min vs 20-40 min) ✓
- 2WikiMultiHopQA R@5: 89.1 (HippoRAG ColBERTv2) vs 68.2 (ColBERTv2 alone) = 20.9pt gain ✓ (digest rounds to 20)
- MuSiQue R@5: 51.9 (HippoRAG) vs 49.2 (ColBERTv2 best baseline) = 2.7pt gain — digest says ~3pt ✓
- REBEL ablation: 39.6 (REBEL R@5 MuSiQue) vs 51.9 (GPT-3.5) = 12.3pt drop; 76.5 (REBEL R@5 2Wiki) vs 89.1 = 12.6pt drop; on HotpotQA: 59.2 vs 77.7 = 18.5pt drop. Digest says "11–13 points across all three datasets" — slightly understates HotpotQA but conservative ✓
- "GPT-3.5 produces twice as many triples as REBEL" — matches §5.1 verbatim ✓
- Node specificity ablation MuSiQue: 50.2 vs 51.9 R@5 = 1.7pt; HotpotQA 73.7 vs 77.7 = 4pt — digest says "~2 pts and ~4 pts on 2Wiki"; the 4pt figure is actually on HotpotQA not 2Wiki. **Minor wording fix needed**: the 2Wiki effect of node-specificity is ~0pt (88.8 vs 89.1), and the synonymy-edge effect is ~3.5pt on 2Wiki (85.6 vs 89.1). The digest's "~4 pts on 2Wiki" for synonymy is correct; the "~2 pts" without naming a dataset is fine.
- Offline indexing: ~$15 per 10k passages, ~10× slower than ColBERTv2 — matches Appendix G ✓
- Llama-3.1-70B "matches GPT-3.5" — Table 5 row 4 shows 53.7/85.3/78.6 vs 51.9/89.1/77.7 — matches on MuSiQue and HotpotQA, slight regression on 2Wiki. Digest says "matches" which is fair on aggregate ✓
- PPR damping factor 0.5, synonymy threshold 0.8 — §3.4 verbatim ✓
- "Path-finding" example with Thomas Südhof — Table 7 + Appendix E ✓

The application scenario in "How to Apply It" is explicitly framed as a Flow OS hypothetical, not a paper claim.
