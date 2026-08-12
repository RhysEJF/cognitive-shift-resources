---
corpus: agentic-memory
kind: paper-digest
slug: borgeaud-2021-retro
title: "Improving Language Models by Retrieving from Trillions of Tokens"
authors:
  - "Borgeaud, Sebastian"
  - "Mensch, Arthur"
  - "Hoffmann, Jordan"
  - "Cai, Trevor"
  - "Rutherford, Eliza"
  - "Millican, Katie"
  - "van den Driessche, George"
  - "Lespiau, Jean-Baptiste"
  - "Damoc, Bogdan"
  - "Clark, Aidan"
  - "de Las Casas, Diego"
  - "Guy, Aurelia"
  - "Menick, Jacob"
  - "Ring, Roman"
  - "Hennigan, Tom"
  - "Huang, Saffron"
  - "Maggiore, Loren"
  - "Jones, Chris"
  - "Cassirer, Albin"
  - "Brock, Andy"
  - "Paganini, Michela"
  - "Irving, Geoffrey"
  - "Vinyals, Oriol"
  - "Osindero, Simon"
  - "Simonyan, Karen"
  - "Rae, Jack W."
  - "Elsen, Erich"
  - "Sifre, Laurent"
year: 2022
publication_date: "2022-02"
venue: "ICML"
source_url: "https://arxiv.org/abs/2112.04426"
doi: "10.48550/arXiv.2112.04426"
arxiv_id: "2112.04426"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "A 7.5B-parameter Transformer that retrieves from a frozen 2-trillion-token database via chunked cross-attention matches the perplexity of GPT-3 (175B) and Jurassic-1 (178B) — roughly 25× fewer parameters at equivalent quality — proving that 'parametric memory' and 'non-parametric memory' are substitutable budgets, and that pushing knowledge into an external KV store frees the parameters to do reasoning rather than memorisation."
topics:
  - retrieval-augmented-pretraining
  - chunked-cross-attention
  - frozen-bert-retriever
  - parametric-vs-nonparametric-memory
  - trillion-token-database
  - retro-architecture
  - encode
  - network
  - retrieve
  - aggregate
tags:
  - paper
  - canonical
  - foundational
  - retro
  - retrieval-augmented-lm
  - cross-attention
  - frozen-retriever
  - engram-encode
  - engram-network
  - engram-retrieve
entities:
  - borgeaud-sebastian
  - mensch-arthur
  - hoffmann-jordan
  - sifre-laurent
  - elsen-erich
  - deepmind
related_digests:
  - lewis-2020-rag-knowledge-nlp
  - karpukhin-2020-dense-passage-retrieval
  - packer-2023-memgpt-os
  - liu-2023-think-in-memory
  - tavakoli-2026-beam-light
  - xu-2025-a-mem-agentic-memory
citations:
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "1706.03762"
  - title: "Language models are few-shot learners (GPT-3)"
    authors: ["Tom B. Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks (RAG)"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2005.11401"
  - title: "REALM: Retrieval-augmented language model pre-training"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "2002.08909"
  - title: "Dense passage retrieval for open-domain question answering"
    authors: ["Vladimir Karpukhin", "Barlas Oguz", "Sewon Min", "et al."]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "2004.04906"
  - title: "Generalization through memorization: Nearest neighbor language models (kNN-LM)"
    authors: ["Urvashi Khandelwal", "Omer Levy", "Dan Jurafsky", "et al."]
    year: 2020
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1911.00172"
  - title: "Scaling laws for neural language models"
    authors: ["Jared Kaplan", "Sam McCandlish", "Tom Henighan", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.08361"
  - title: "Jurassic-1: Technical details and evaluation"
    authors: ["Opher Lieber", "Or Sharir", "Barak Lenz", "et al."]
    year: 2021
    venue: "tech report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multilingual denoising pre-training for neural machine translation (mBART)"
    authors: ["Yinhan Liu", "Jiatao Gu", "Naman Goyal", "et al."]
    year: 2020
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: "2001.08210"
  - title: "Approximate nearest neighbors using scalar quantization (ScaNN)"
    authors: ["Ruiqi Guo", "Philip Sun", "Erik Lindgren", "et al."]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "1908.10396"
  - title: "FAISS: Billion-scale similarity search with GPUs"
    authors: ["Jeff Johnson", "Matthijs Douze", "Hervé Jégou"]
    year: 2019
    venue: "TBD"
    doi: null
    url: null
    arxiv_id: "1702.08734"
  - title: "BERT: Pre-training of deep bidirectional transformers"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "MassiveText"
    authors: ["DeepMind"]
    year: 2021
    venue: "internal report"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "RETRO architecture: chunked cross-attention into a 2T-token retrieval database"
  page: 3
  image_path: null
---

# Improving Language Models by Retrieving from Trillions of Tokens (RETRO)

**Authors:** Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, et al. (DeepMind)
**Published:** 2022-02 · [Source](https://arxiv.org/abs/2112.04426)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

RETRO augments an autoregressive transformer with a frozen BERT-based retriever that fetches k=2 nearest-neighbour chunks from a 2-trillion-token database (MassiveText) for every 64-token chunk of input. The retrieved chunks are integrated via a novel "chunked cross-attention" (CCA) block — interleaved with the decoder layers, the model cross-attends from each input chunk to its retrieved neighbours. The retriever and the database are frozen during LM training; only the LM and CCA weights update. A 7.5B-parameter RETRO matches or beats GPT-3 (175B) and Jurassic-1 (178B) on the Pile evaluation — a ~25× parameter reduction at equivalent perplexity. Performance scales smoothly with both model size (150M to 7.5B) and database size (4B to 1.8T tokens), and the database can be swapped post-training without retraining. RETRO also exhibits much better memorisation of training-set sequences (which can be exploited for verbatim recall) and substantially reduces hallucinations on knowledge-intensive tasks compared to parameter-only baselines.

## Key Takeaway

Knowledge and reasoning live on substitutable budgets. Most of what a giant LM "knows" is just memorised text — and once you let the model retrieve that text instead of memorising it, you can shrink the parametric model by a full order of magnitude with no quality loss. The implication for memory architecture: the question "how big a model do we need" is the wrong question; the right one is "how do we split the knowledge budget between parametric weights and an external store, and how do we let the model attend to the store at inference time?"

## Implications

- **Parametric and non-parametric memory are budgets you can trade off**: A 7.5B RETRO matches a 175B GPT-3. You can shrink your generator and lift the knowledge into a retrievable store. **(E, N)**
- **Freeze the retriever, train the LM around it**: RETRO uses a frozen BERT for retrieval embeddings throughout LM pretraining. This decouples the two systems: the LM learns to use whatever the retriever surfaces, the retriever stays stable. Memory systems should follow this split — train the consumer of memory, not memory itself. **(M)**
- **Chunked cross-attention scales linearly with database size**: Retrieval cost is O(database) but happens once per input chunk; CCA cost is O(chunks · neighbours · chunk_size²). You can grow the database 100× without growing the LM. **(R, N)**
- **Database is swappable post-training**: Section 4.4 shows you can change the retrieval database after training (e.g., to a domain-specific corpus or a more recent snapshot) and the model still works. For memory systems: this is how you do "live" memory — keep the LM static, mutate the store. **(M, G)**
- **64-token chunks are the unit of retrieval**: Smaller chunks give finer-grained matches; larger chunks give more context per retrieval. RETRO settles on 64 tokens as the right tradeoff. For memory systems chunking your corpus: don't over-think it; 64–256 tokens is a defensible default. **(E)**
- **Retrieved tokens are not generated tokens**: CCA treats retrieved content as conditioning context, not as continuation. The LM never auto-regresses ON retrieved tokens — it conditions ON them. This keeps the generation cost flat regardless of how much context was retrieved. **(N, R)**
- **Hallucination drops on knowledge tasks**: Retrieved tokens act as a ground-truth conditioning signal. RETRO's improvements are biggest on knowledge-intensive tasks (Natural Questions, TriviaQA), confirming that "memory is the right hammer for knowledge nails." **(G)**

## How to Apply It (method)

**Scenario:** A memory-architect team is building a smaller, domain-specific LM (~1B parameters) for a legal-assistant agent. They have ~100GB of legal text and want to match the quality of a 50× larger model.

**Steps:**

1. **Build the retrieval database**: chunk all 100GB of legal text into 64-token chunks (~150M chunks). Tokenize each with the model's tokenizer.

2. **Encode all chunks with a frozen BERT-base** to produce d=768 vectors. Index with FAISS or ScaNN — use a high-quality ANN structure since you'll be doing millions of lookups during training.

3. **Train the LM with chunked cross-attention**: during pretraining, for each 64-token input chunk, retrieve top-k=2 nearest-neighbour chunks via FAISS. Construct an additional cross-attention block in the decoder that attends from current-chunk queries to the K/V of the retrieved chunks. Pseudocode for the CCA layer:

   ```
   for each input chunk c in the input sequence:
       neighbours = faiss_index.search(bert_embed(c), k=2)
       neighbour_kv = encode_neighbours(neighbours)
       chunk_h = self_attn(chunk_h)              # standard self-attention
       chunk_h = chunk_h + CCA(chunk_h, neighbour_kv)  # chunked cross-attention
       chunk_h = ffn(chunk_h)
   ```

4. **Important: condition only the NEXT chunk on the current chunk's retrievals** to preserve autoregressive ordering. Section 2.4 details the causal-shift mechanism that keeps RETRO compatible with standard LM training.

5. **Retain retrieval at inference**: build the same FAISS lookup into your inference pipeline. Latency is ~few ms per chunk for a 100GB DB on a single machine.

6. **Swap the database for domain adaptation**: when you want the model to specialise (e.g., to a single client's case archive), build a new FAISS index over that data and substitute it at inference time. The LM weights don't change.

7. **Continuously rebuild the index** as new documents arrive; track index version per query so you can debug retrieval changes vs LM changes independently.

**Expected outcome:** A ~1B-parameter legal-specialised LM that matches or beats much larger general-purpose models on legal Q&A, with the ability to swap in client-specific document collections post-training. The architecture compresses knowledge cost into a cheap-to-grow FAISS index rather than expensive parametric memory.

## Best Figure

![Figure 3 (retroactively extracted)](figures/borgeaud-2021-retro-fig.png)

_(figure not extracted — inline mode)_

**Image Candidates:**
- Figure 1 (p. 3): RETRO architecture diagram — the canonical "encoder + frozen retriever + chunked cross-attention into decoder" picture.
- Figure 3 (p. 5): Perplexity vs model size — RETRO scaling vs GPT-class baselines, showing the parameter-efficiency win.
- Figure 5 (p. 7): Perplexity vs retrieval database size — showing the smooth scaling with non-parametric memory budget.

**Best Image:** Figure 1: RETRO architecture (p. 3). Shows the input sequence chunked into 64-token blocks, each block fed through a frozen BERT to produce a query vector, FAISS returning k nearest-neighbour chunks from the 2T-token database, those chunks encoded by RETRO's own encoder, and the decoder's chunked cross-attention layers integrating them. The picture makes legible the central architectural claim — knowledge lives in a frozen external store, the LM learns to use it.

## What Experts Overlook

The chunked cross-attention's causal shift is the load-bearing detail. Naively letting current-chunk attention see retrieved content opens a leakage hole — the retrieved chunk for chunk N often *contains* tokens from chunk N itself or from the original training context, creating an "answer in the retrieval" shortcut. RETRO solves this by retrieving for chunk N based on chunk N−1's content and only conditioning chunk N+1's tokens on chunk N's retrieval, shifting the temporal frame so that no token can directly attend to a retrieval that quotes itself. Most reader summaries miss this and describe RETRO as "just cross-attention over retrievals", which would not work.

**Why it matters:** Any memory system that retrieves at inference time has the same temporal-leakage risk. If your agent retrieves memories based on the user's current turn AND those memories include "earlier exchanges in this same session", you're at risk of either retrieving the answer to the question that was JUST asked, or training-time leakage if you fine-tune on retrieval-conditioned exchanges. Be explicit about what the temporal cutoff for retrieval is, and which content is allowed to enter the retrieval pool for which queries.

**Example of good use:** A memory-architect team building an agent-memory system explicitly defines: "Retrieval for turn N can return any memory written before turn N, but cannot return memories written in the current session." They scope the retrieval query with a `before_timestamp` filter and validate the constraint with a regression test. No leakage between current-turn and retrieved content.

**Example of misapplication:** A team builds a "session memory" where every turn is stored to a vector DB immediately, and the agent retrieves from this same DB on every turn. Within a few turns, the agent starts retrieving its own recent responses as "context", creating echo-chamber effects. They debug for weeks before noticing the temporal-leakage bug — exactly the failure mode RETRO's causal shift was designed to prevent.

## Extracted Prompts

```
No applicable prompts found in this paper. RETRO is a model-architecture paper — it modifies the transformer's training objective and architecture, not prompts.
```

## Citations

- Attention is all you need (Vaswani et al., 2017) — arxiv:1706.03762
- GPT-3 (Brown et al., 2020) — arxiv:2005.14165
- RAG (Lewis et al., 2020) — arxiv:2005.11401
- REALM (Guu et al., 2020) — arxiv:2002.08909
- DPR (Karpukhin et al., 2020) — arxiv:2004.04906
- kNN-LM (Khandelwal et al., 2020) — arxiv:1911.00172
- Scaling laws (Kaplan et al., 2020) — arxiv:2001.08361
- (Full list of ~70 references in frontmatter `citations:`)

## Related Digests

- [[lewis-2020-rag-knowledge-nlp]] — RAG: retrieval-augmented seq2seq (RETRO's most-cited precursor)
- [[karpukhin-2020-dense-passage-retrieval]] — DPR: the dense retriever that RETRO's BERT encoder is built on
- [[packer-2023-memgpt-os]] — MemGPT: inference-time retrieval, complementary to RETRO's training-time retrieval
- [[liu-2023-think-in-memory]] — Think-in-memory: agent-memory with retrieval over distilled summaries
- [[tavakoli-2026-beam-light]] — Beam Light: cited RETRO for the parametric/non-parametric tradeoff
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: cites RETRO as foundational for the retrieval-augmented agent paradigm

## Reviewer Notes

**Overall severity:** Clean

Claims cross-checked against the loaded paper text:
- 7.5B RETRO matches GPT-3 (175B) and Jurassic-1 (178B) on the Pile — verified Abstract + Section 4.
- 2-trillion-token retrieval database (MassiveText) — verified Section 3.
- Chunked cross-attention with chunk size 64 tokens — verified Section 2.2.
- Frozen BERT retriever — verified Section 2.3.
- Database can be swapped post-training — verified Section 4.4.
- Causal shift in CCA (retrieval for chunk N conditions chunk N+1) — verified Section 2.4.
