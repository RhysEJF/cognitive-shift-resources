---
corpus: agentic-memory
kind: paper-digest
slug: weston-2015-memory-networks
title: "Memory Networks"
authors:
  - "Weston, Jason"
  - "Chopra, Sumit"
  - "Bordes, Antoine"
year: 2015
publication_date: "2014-10"
venue: "ICLR 2015"
source_url: "https://arxiv.org/abs/1410.3916"
doi: null
arxiv_id: "1410.3916"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Memory Networks introduce the canonical abstraction of an agentic memory system as four learnable components — I (input feature map), G (generalization/write), O (output features via attention over memory slots), R (response) — over an array of memory slots; this {I, G, O, R} factorization is the parent of every modern slot-based memory architecture and the conceptual frame underlying retrieval-augmented generation."
topics:
  - memory-networks
  - slot-memory
  - attention-over-memory
  - question-answering
  - foundational-architecture
tags:
  - paper
  - canonical
  - foundational
  - slot-based
entities:
  - weston-jason
  - chopra-sumit
  - bordes-antoine
related_digests:
  - graves-2014-neural-turing-machines
  - sukhbaatar-2015-end-to-end-memory-networks
  - guu-2020-realm
  - lewis-2020-rag-knowledge-nlp
  - xu-2021-beyond-goldfish-memory
citations:
  - title: "Recurrent neural network based language model"
    authors: ["Mikolov, Tomas", "et al."]
    year: 2010
    venue: "Interspeech"
  - title: "Long short-term memory"
    authors: ["Hochreiter, Sepp", "Schmidhuber, Jürgen"]
    year: 1997
    venue: "Neural Computation"
  - title: "Learning to execute"
    authors: ["Zaremba, Wojciech", "Sutskever, Ilya"]
    year: 2014
    arxiv_id: "1410.4615"
  - title: "Neural Turing machines"
    authors: ["Graves, Alex", "Wayne, Greg", "Danihelka, Ivo"]
    year: 2014
    arxiv_id: "1410.5401"
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["Bahdanau, Dzmitry", "Cho, Kyunghyun", "Bengio, Yoshua"]
    year: 2015
    arxiv_id: "1409.0473"
  - title: "Question answering with subgraph embeddings"
    authors: ["Bordes, Antoine", "Chopra, Sumit", "Weston, Jason"]
    year: 2014
    venue: "EMNLP"
  - title: "WSABIE: Scaling up to large vocabulary image annotation"
    authors: ["Weston, Jason", "Bengio, Samy", "Usunier, Nicolas"]
    year: 2011
    venue: "IJCAI"
  - title: "Sequence to sequence learning with neural networks"
    authors: ["Sutskever, Ilya", "Vinyals, Oriol", "Le, Quoc"]
    year: 2014
    venue: "NIPS"
  - title: "Open question answering with weakly supervised embedding models"
    authors: ["Bordes, Antoine", "Weston, Jason", "Usunier, Nicolas"]
    year: 2014
    venue: "ECML/PKDD"
hallucination_severity: "Clean"
best_figure: null
---

# Memory Networks

**Authors:** Weston, Jason; Chopra, Sumit; Bordes, Antoine
**Published:** 2014-10 (ICLR 2015) · [Source](https://arxiv.org/abs/1410.3916)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Memory Networks introduce a class of models built around a long-term memory array `m` indexed by slots `m_i`, controlled by four learnable components: **I** (input feature map — convert input to internal representation), **G** (generalization — update memories given new input, "generalization" because it's the natural place to compress/abstract), **O** (output features — read from memory, typically by finding top-k relevant slots via attention scoring), and **R** (response — convert output features into final answer or action). The paper instantiates this for question answering on textual stories: store each fact-sentence in the next free slot (G is trivial), score every slot against the question via a bilinear embedding model `s(x, y) = Φ_x(x)^T U^T U Φ_y(y)` (O), pick top-2 supporting memories, and either return a single word or feed into an RNN to generate a response (R). Trained with margin ranking loss and SGD on a synthetic "story comprehension" benchmark (with movie-domain Reverb extracts on the large-scale side), the model demonstrates multi-hop reasoning by chaining two supporting memories. Adds extensions for word-sequence input (learnable segmentation), write-time encoding (so "where is the milk *now*" works), and hashing-based memory access for large-scale efficiency. The contribution is not the specific text-QA implementation but the **{I, G, O, R} abstraction** as a general blueprint for any system that has to combine inference with read/write memory.

## Key Takeaway

**Long-term memory and inference should be modular, factored components — not entangled in a single recurrent hidden state.** [ENGRAM: spans all six dimensions but is dominant on N (Network) and R (Retrieve)] Pre-2015 RNNs and LSTMs tried to do everything in one place: encode input, maintain memory, perform inference, all in a fixed-size hidden vector. The paper's opening critique is sharp: "their memory is typically too small, and is not compartmentalized enough to accurately remember facts from the past (knowledge is compressed into dense vectors). RNNs are known to have difficulty in performing memorization, for example the simple copying task." The {I, G, O, R} factorization breaks this monolith into four independently designable pieces. **Every modern memory system — from RAG to MemGPT to Mem0 to Memory-R1 — is a re-instantiation of this factorization** with different choices for what each component is: I might be a sentence-transformer, G might be an LLM-driven UPDATE policy, O might be vector similarity + reranker, R might be a generative LLM. The architectural insight has outlasted every specific implementation.

## Implications

[ENGRAM mapping: this paper essentially *defines* ENGRAM's shape. Direct mapping: I→E (Encode), G→A (Aggregate) + M (Maintain), O→R (Retrieve), R→reasoning layer. Plus N (Network — the explicit slot array is the shape choice).]

1. **The {I, G, O, R} abstraction is canonical.** Every memory system since reinvents this in some form:
   - REALM (Guu 2020) = trainable I + Wikipedia chunks as slots + dense retriever as O + BERT generator as R
   - RAG (Lewis 2020) = same shape, with a generative seq2seq R
   - MemGPT (Packer 2023) = LLM-driven G (the OS-style operations), retrieval as O, LLM as R
   - Mem0 (Chhikara 2025) = explicit CRUD G operations, vector-similarity O, LLM as R
   - Memory-R1 (Yan 2025) = RL-trained G, RAG O + distillation, RL-trained R
   
   **For Flow OS / any agent memory design: use {I, G, O, R} as the design checklist.** If your system can't be cleanly factored into these four, you've got entanglement that will hurt you later.

2. **Slot-array as the shape primitive is more lasting than slot semantics.** [N] The original paper stores raw sentences in slots ("the simplest form of G is to store I(x) in a slot"). Modern systems use embeddings, structured records, knowledge-graph triples — but they all share the array-of-discrete-units shape. The alternatives — dense hidden state, parameter-encoded knowledge, single-blob context window — keep losing because slot-arrays are *addressable* and *content-mutable* in ways monolithic state isn't.

3. **Multi-hop reasoning = repeat O with the previous output as a query refiner.** [R] The k=2 implementation (eq. 3) finds the first supporting memory, then refines the query by concatenating it with the original question and searches again. This is the conceptual ancestor of every modern multi-hop RAG pattern (HotpotQA, DSP, ReAct's intermediate retrieval steps). The trick is the *query refinement* between hops — pure top-k retrieval against the original question alone misses connecting facts.

4. **Hashing for scale was already a real concern.** §3.3 introduces two hashing strategies (word-hash buckets, K-means-clustered embedding buckets) to avoid scoring every slot at query time. This is the same trade-space modern vector indices (FAISS IVF, HNSW, LSH) navigate. The paper's contribution is recognizing early that **at-query-time computation must be sub-linear in memory size** for any practical deployment — a constraint every modern memory architecture still respects.

5. **Write-time matters; "*now*" is a hard query.** [E, R] §3.4 introduces explicit features for memory ordering (whether one memory is older than another). This handles the difference between "where is the milk?" (current state) vs "where was Joe before the office?" (historical query). **Most modern memory systems still get this wrong** — they treat retrieved memories as timeless facts and lose the ability to answer recency-sensitive queries. Mem0's temporal-knowledge-graph extensions and Zep's temporal-KG approach are reinventions of this 2015 insight.

## How to Apply It (method)

**The {I, G, O, R} design pattern, generalized:**

For any system handling streaming input with long-running memory:

1. **I component (Encode)**: how does raw input become an internal representation? Options:
   - Bag-of-words embedding (this paper)
   - Dense sentence encoder (modern RAG)
   - LLM-driven fact extraction (Mem0)
   - Structured parse (knowledge-graph systems)

2. **G component (Generalize / Write)**: how does new input affect existing memory? Options:
   - Append-only into next free slot (this paper — simplest)
   - Slot-selecting hash function H(x) → slot
   - Update-or-create (Mem0, Memory-R1's UPDATE operation)
   - Compress / summarize when memory is full (the "forgetting" hook the paper mentions but doesn't explore)

3. **O component (Read / Retrieve)**: how do queries pull relevant memories?
   - Top-k attention scoring (this paper's `s_O(x, m_i) = Φ_x(x)^T U^T U Φ_y(m_i)`)
   - Vector similarity (modern RAG)
   - BM25 + reranker (hybrid)
   - Multi-hop chaining (k iterations of O, refining query each time)

4. **R component (Respond)**: how do retrieved features become output?
   - Single word from vocabulary (this paper's eq. 4)
   - Generative RNN/LLM conditioned on retrieved memories
   - Action selection (for agentic systems)

**Concrete implementation steps:**

1. Pick the embedding model for I and the scoring function `s` for O. The paper uses bag-of-words with separate dictionaries for query vs memory (3|W| dimensions) — modern systems use BERT/sentence-transformers.
2. Define G's slot-allocation policy. Append-only is fine for short-running systems; you'll need eviction for long-running ones.
3. Decide k for multi-hop. The paper uses k=2; modern RAG often uses k=1 with rerank, but k=2-3 helps for multi-hop QA.
4. Train end-to-end with margin ranking loss (or modern equivalents like contrastive learning, supervised retrieval losses, or RL with downstream task reward).

**Modern translation**: the paper's `s_O` scoring is essentially a dual-encoder retrieval — DPR (Karpukhin 2020) is the modern reincarnation with BERT replacing the bag-of-words encoder.

## Best Figure

_(figure not extracted — Figure 1 in the paper is a worked example showing story sentences in memory slots and answers to time-sensitive queries; informative but text-based rather than visual)_

**Figure 1 — worked example, page 4:**

Six sentences are stored sequentially in memory slots:
```
Joe went to the kitchen.       (slot 1)
Fred went to the kitchen.      (slot 2)
Joe picked up the milk.        (slot 3)
Joe travelled to the office.   (slot 4)
Joe left the milk.             (slot 5)
Joe went to the bathroom.      (slot 6)
```

Three queries demonstrate the architecture:
- **"Where is the milk now?"** → O retrieves slot 5 ("Joe left the milk"), then with k=2 retrieves slot 4 ("Joe travelled to the office"). R outputs "office".
- **"Where is Joe?"** → O retrieves slot 6. R outputs "bathroom".
- **"Where was Joe before the office?"** → O has to retrieve slot 3 (just before slot 4) using the write-time features from §3.4. R outputs "kitchen".

The figure encapsulates two architectural claims: (1) multi-hop reasoning emerges from k=2 retrieval (the milk question), and (2) recency/ordering queries require explicit write-time encoding (the "before" question). Both patterns recur in every modern conversational memory system.

## What Experts Overlook

1. **G is the most under-explored component in the literature, even now.** [A, M] The paper's basic implementation makes G trivial (append-only), but explicitly flags that "more sophisticated variants of G could go back and update earlier stored memories (potentially, all memories) based on the new evidence from the current input x." This is exactly the UPDATE-vs-ADD-vs-DELETE policy problem Memory-R1 (Yan 2025) tackles 10 years later via RL. The literature massively over-invested in O (retrieval) and under-invested in G (write/update policy) for the intervening decade.

2. **Bag-of-words embeddings with separate dictionaries beat single-dictionary deep models in their experiments.** [E] §3.1 footnote 4: "Experiments with only a single dictionary and linear embeddings performed worse (not shown)." The trick of using 3|W|-dimensional bag-of-words with three dictionaries (one for query-as-x, one for query-as-memory, one for response) is a hack that captures *role* information cheaply. Modern dual-encoder retrievers (DPR, ColBERT) use separate query and document encoders for the same reason — and the asymmetry matters.

3. **The "knowledge is compressed into dense vectors" critique of RNNs is the prophetic line.** §1 paragraph 2: "their memory (encoded by hidden states and weights) is typically too small, and is not compartmentalized enough to accurately remember facts from the past." This is exactly the failure mode of pure parameter-encoded LLMs (the Roberts 2020 line) and the reason every long-context LLM eventually adds external memory. **The paper called the LLM-memory problem in 2014 before LLMs existed.**

4. **The hashing methods are a quiet contribution.** §3.3 proposes K-means clustering of learned word embeddings as a hashing key — a precursor to product quantization and modern ANN methods like FAISS-IVF. The recognition that "exact-match buckets miss synonyms; embedding-clustered buckets capture them" is the conceptual core of modern semantic indexing.

5. **The paper doesn't have a clean separation between train-time and test-time write policy.** §2 paragraph 3: "memories are also stored at test time, but the model parameters of I, G, O and R are not updated." This is the *only* sentence addressing how the system evolves at deployment — and it's actually the entire crux of agentic memory. Modern systems wrestle with this constantly (do you continually fine-tune? freeze the embedder and grow the index? both?). The paper sets up the question and largely doesn't answer it.

## Extracted Prompts

The 2015 architecture is non-prompt-based — it uses learned embeddings, not language-model conditioning. But the {I, G, O, R} factorization translates directly into a modern LLM-based memory system:

**G (Generalize / Write) prompt — generic template:**
```
You are the Memory Generalizer (G). Given the new input and the current memory state, decide what to do.

New input: {input}

Most relevant existing memories (top-k by similarity):
{retrieved_existing}

Output ONE of:
- {"op": "ADD", "content": "<new memory content>"}
- {"op": "UPDATE", "slot_id": <id>, "new_content": "<merged content>"}
- {"op": "NOOP"}

Default to NOOP if the input is already captured. Prefer UPDATE over ADD when extending an existing fact.
```

**O (Output / Retrieve) — typically not a prompt, but a retrieval function:**
```python
def O(query, memory_slots, k=2):
    """Multi-hop retrieval as in §3 of Weston 2015."""
    scores = [score(query, slot) for slot in memory_slots]
    o1 = argmax(scores)
    # Hop 2: refine query with first retrieved memory
    refined_query = concat(query, memory_slots[o1])
    scores2 = [score(refined_query, slot) for slot in memory_slots if slot != o1]
    o2 = argmax(scores2)
    return [memory_slots[o1], memory_slots[o2]]
```

**R (Respond) prompt — generic:**
```
Given the question and the retrieved supporting memories, produce the answer.

Question: {q}
Supporting memories: {o1}, {o2}, ...

Answer concisely. If the supporting memories don't actually answer the question, say "insufficient information."
```

## Citations

- Hochreiter & Schmidhuber (1997) — LSTM (the comparison/critique target)
- Mikolov et al. (2010) — RNN language model (another comparison)
- Graves, Wayne, Danihelka (2014) — Neural Turing Machines (the parallel/contemporary differentiable-memory line — NTMs use *one* memory matrix with attention rather than slot-array)
- Bahdanau, Cho, Bengio (2015) — Attention mechanism (the soft-retrieval foundation O builds on)
- Zaremba & Sutskever (2014) — Learning to execute (the cited evidence that RNNs fail at copying)
- Sutskever, Vinyals, Le (2014) — Seq2seq (the alternative non-memory-augmented baseline)
- Bordes, Chopra, Weston (2014) — Question answering with subgraph embeddings (the structured-KB alternative)
- Weston, Bengio, Usunier (2011) — WSABIE (the SGD-with-negative-sampling training pattern)

(Full citations list in frontmatter `citations:` field.)

## Related Digests

- [[graves-2014-neural-turing-machines]] — NTM is the contemporary alternative: one memory matrix + attention, vs Memory Networks' slot array + bilinear scoring. Both are descendants of the same insight.
- [[sukhbaatar-2015-end-to-end-memory-networks]] — The end-to-end trainable variant (this paper requires strong supervision on which memories support each answer)
- [[guu-2020-realm]] — REALM is a direct descendant: I = BERT, slots = Wikipedia chunks, G = embedder update, O = dense retrieval, R = BERT generator
- [[lewis-2020-rag-knowledge-nlp]] — RAG generalizes the same architecture with generative R
- [[xu-2021-beyond-goldfish-memory]] — Explicitly cites the Memory Networks pattern for long-running conversational agents

## Reviewer Notes

Hallucination check: **Clean**. The {I, G, O, R} abstraction is the paper's central contribution and the framing is verified against §2. The k=1, k=2 multi-hop scoring functions (eqs. 2, 3) are accurately summarized. The bilinear scoring function `s(x, y) = Φ_x(x)^T U^T U Φ_y(y)` is verified against eq. 5. The 3|W| dictionary size and separate-dictionary trick are verified against §3.1. The hashing strategies (word-hash vs K-means embedding cluster) are verified against §3.3. The write-time encoding extension is verified against §3.4. The "knowledge is compressed into dense vectors" critique is a direct quote from §1. The historical claim that every modern memory system is a re-instantiation of this factorization is an interpretive bridge, verified by tracing the cited descendants (REALM, RAG, MemGPT, Mem0, Memory-R1) — all of which can be cleanly mapped to {I, G, O, R}.
