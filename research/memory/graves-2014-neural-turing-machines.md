---
corpus: agentic-memory
kind: paper-digest
slug: graves-2014-neural-turing-machines
title: "Neural Turing Machines"
authors:
  - "Graves, Alex"
  - "Wayne, Greg"
  - "Danihelka, Ivo"
year: 2014
publication_date: "2014-12"
venue: "preprint"
source_url: "https://arxiv.org/abs/1410.5401"
doi: null
arxiv_id: "1410.5401"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Graves, Wayne and Danihelka built the first end-to-end differentiable architecture where a neural-network controller learns to read from and write to an external memory matrix using soft, content-addressable attention — the conceptual ancestor of every modern attention-over-external-memory mechanism, and the paper that named the (controller + addressable memory) split that today's agent-memory systems re-implement at every scale."
topics:
  - external-memory-network
  - differentiable-memory
  - content-addressable-memory
  - location-addressable-memory
  - controller-memory-split
  - soft-attention
  - read-write-heads
  - algorithmic-tasks
  - encode
  - retrieve
  - network
tags:
  - paper
  - canonical
  - foundational
  - neural-turing-machine
  - external-memory
  - differentiable-memory
  - precursor-to-attention
  - engram-network
  - engram-retrieve
entities:
  - graves-alex
  - wayne-greg
  - danihelka-ivo
  - google-deepmind
related_digests:
  - sukhbaatar-2015-end-to-end-memory-networks
  - vaswani-2017-attention-is-all-you-need
  - hu-2026-evermemos
  - liu-2023-think-in-memory
  - zhong-2023-memorybank-llm
citations:
  - title: "Long short-term memory"
    authors: ["Sepp Hochreiter", "Jürgen Schmidhuber"]
    year: 1997
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generating sequences with recurrent neural networks"
    authors: ["Alex Graves"]
    year: 2013
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1308.0850"
  - title: "On the difficulty of training recurrent neural networks"
    authors: ["Razvan Pascanu", "Tomas Mikolov", "Yoshua Bengio"]
    year: 2013
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "1211.5063"
  - title: "Recursive distributed representations"
    authors: ["Jordan B. Pollack"]
    year: 1990
    venue: "Artificial Intelligence"
    doi: null
    url: null
    arxiv_id: null
  - title: "Holographic reduced representations"
    authors: ["Tony A. Plate"]
    year: 1995
    venue: "IEEE TNN"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sequence to sequence learning with neural networks"
    authors: ["Ilya Sutskever", "Oriol Vinyals", "Quoc V. Le"]
    year: 2014
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "1409.3215"
  - title: "Memory networks"
    authors: ["Jason Weston", "Sumit Chopra", "Antoine Bordes"]
    year: 2014
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1410.3916"
  - title: "Speech recognition with deep recurrent neural networks"
    authors: ["Alex Graves", "Abdel-rahman Mohamed", "Geoffrey Hinton"]
    year: 2013
    venue: "ICASSP"
    doi: null
    url: null
    arxiv_id: "1303.5778"
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["Dzmitry Bahdanau", "Kyunghyun Cho", "Yoshua Bengio"]
    year: 2014
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1409.0473"
  - title: "RMSProp"
    authors: ["Tijmen Tieleman", "Geoffrey Hinton"]
    year: 2012
    venue: "Coursera lecture notes"
    doi: null
    url: null
    arxiv_id: null
  - title: "Computability and unsolvability"
    authors: ["Martin Davis"]
    year: 1958
    venue: "book"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Neural Turing Machine architecture: controller + read/write heads + memory matrix"
  page: 4
  image_path: null
---

# Neural Turing Machines

**Authors:** Alex Graves, Greg Wayne, Ivo Danihelka
**Published:** 2014-12 · [Source](https://arxiv.org/abs/1410.5401)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Graves, Wayne and Danihelka introduce the Neural Turing Machine (NTM): a neural network "controller" (an MLP or LSTM) coupled to an external memory matrix M ∈ R^{N×M} via differentiable "read" and "write" heads. Each head emits a soft attention vector over the N memory locations using a combination of content-based addressing (cosine similarity between a key emitted by the controller and the rows of memory) and location-based addressing (shift and sharpen the previous attention vector). Because every operation is differentiable, the whole architecture can be trained end-to-end with backprop on algorithmic tasks. NTMs learn to perform copy, repeat copy, associative recall, sorting, and dynamic n-gram inference from input/output examples alone — tasks that ordinary LSTMs fail to learn at the same parameter budget. The paper introduces the controller/memory split, content-addressable attention, and the read-write head abstraction that every subsequent attention-over-memory system inherits — making it the conceptual parent of Memory Networks, the Transformer's attention mechanism, and modern agent-memory architectures.

## Key Takeaway

You can give a neural network a side-loaded memory and let it learn the access pattern, as long as every access operation is differentiable. The implication for memory architects: the read/write API to a memory store doesn't have to be hand-coded; if you can make it differentiable, the consumer learns the access pattern that fits the task. Even when you can't (because your memory is a flat vector DB), the NTM split — controller + addressable store + attention-based read/write — is the right mental model.

## Implications

- **The controller/memory split is the right interface**: A general-purpose computation engine talks to a separately-managed memory through a well-defined read/write API. Every modern agent-memory system (MemGPT, Mem0, A-MEM) re-implements this split. **(N)**
- **Content-addressable + location-addressable hybrids beat either alone**: NTM combines cosine-similarity (content) addressing with shift/sharpen (location) addressing. Modern systems use cosine-sim for retrieval but still need explicit ordering (recency, timestamp, conversation-id) for many queries — same hybrid. **(R)**
- **Soft attention is the differentiable substitute for hard read/write**: A read head emits a probability distribution over memory locations and reads a weighted average. This makes the whole architecture trainable. For learned memory consumers: soft attention over retrieved chunks (not hard top-1 selection) preserves gradient flow. **(R)**
- **Memory can be tiny if access is smart**: NTMs solve copy and sorting with N=128 memory rows. For agent-memory systems, you don't need millions of stored entries to solve a task — you need entries that are addressable by the right semantic keys. **(N, A)**
- **Read and write heads are separate roles**: Each NTM has independent read heads and write heads. The roles are different — write involves an "erase + add" combo, read is just a weighted sum. For memory systems: distinguish the write-path component (what to store, how to merge with existing) from the read-path (what to retrieve). **(E, R)**
- **End-to-end training is the holy grail (and rarely achievable in practice)**: NTMs prove it's possible in principle, but modern systems usually train components separately (encoder, retriever, generator) because end-to-end training over external memory is unstable. **(M)**
- **Generalisation length matters**: NTMs trained on length-20 sequences generalise to length-120 — a key property for memory systems that must scale beyond training-time examples. Measure it. **(G)**

## How to Apply It (method)

**Scenario:** A memory-architect team is building an agent that has to perform multi-step reasoning over a structured memory (e.g., a customer's order history). They want to understand whether an attention-over-memory approach is right for them.

**Steps:**

1. **Define the controller/memory split clearly**: separate "the policy/LLM that decides what to do" from "the store of facts/history that it queries". Even if you're not training end-to-end, this conceptual split makes the system debuggable.

2. **Implement content-addressable read** using cosine similarity:

   ```
   key = controller.emit_key()
   scores = [cosine_similarity(key, m_i) for m_i in memory]
   weights = softmax(scores * sharpness)    # sharpness β >= 1 controls how peaked
   read_result = sum(weights * memory)
   ```

3. **Implement explicit location-addressing as a complement** — for memory queries that depend on order (most recent, oldest, k-th most recent):

   ```
   # Time-decay weighting
   age = current_step - timestamp[i]
   recency_weight = exp(-age / tau)
   weights = recency_weight * cosine_weights
   ```

4. **Use separate read and write heads**: write involves an "erase vector" (multiplicative gate) followed by an "add vector" (additive update):

   ```
   M_new[i] = M[i] * (1 - w_write[i] * erase) + w_write[i] * add
   ```

   This is the formal recipe for "soft overwrite" — equivalent to a learned "update-or-leave-alone" gate per location.

5. **Train with curriculum**: NTMs only learn copy/sort when starting from short sequences and increasing length gradually. Same applies to any learned memory access: start simple, scale up.

6. **For non-differentiable production systems**: use the NTM's API surface even if the access is hard (top-k retrieval, not soft attention). Track which memory entries were retrieved per query for debugging — the "attention pattern" is your interpretability hook.

7. **Generalisation eval**: train on length L=20, test on L=120. If quality degrades sharply, your access mechanism didn't actually learn the structure — it memorised a length-specific pattern.

**Expected outcome:** A debuggable agent-memory system with a clean controller/memory split, attention-based read/write that gives you interpretable retrieval traces, and a stress test (length generalisation) that distinguishes learned access patterns from memorised ones.

## Best Figure

![Figure 4 (retroactively extracted)](figures/graves-2014-neural-turing-machines-fig.png)

_(figure not extracted — inline mode)_

**Image Candidates:**
- Figure 1 (p. 4): NTM architecture — controller + read/write heads + memory matrix — the canonical "what is an NTM" diagram.
- Figure 2 (p. 7): Combined addressing mechanism — content-based + location-based + shift + sharpen.
- Figures 4–8 (p. 10–14): Learning curves on the algorithmic tasks (copy, repeat copy, associative recall, dynamic n-grams, priority sort) showing NTM beats LSTM by large margins.

**Best Image:** Figure 1: Neural Turing Machine architecture (p. 4). The controller (LSTM or MLP) communicates with the external memory matrix via read heads (output: read vector) and write heads (output: erase + add vectors). The picture establishes the controller/memory split that became standard in subsequent work — Memory Networks, End-to-End Memory Networks, and ultimately the attention-over-external-keys pattern that powers every modern agent.

## What Experts Overlook

The "interpolation gate" g_t between content-addressing and the previous read weights is the unsung hero of NTM's location-addressing mechanism. Section 3.3.2 describes: the read head can either reset its attention to a content-based search (g=1) OR keep its previous attention vector and just shift it (g=0). This explicit interpolation lets the controller decide on every step whether to "look up" something new or "step through" the memory iteratively — exactly the choice a programmer makes between random-access (lookup) and sequential-access (iterate) APIs. Most readers focus on the cosine-similarity addressing and miss that the interpolation gate is what makes NTM learn algorithms like sorting (which need iteration over fetched values).

**Why it matters:** Modern agent-memory systems usually do only content-based retrieval — every query starts from scratch with a new embedding. But many real workflows need "from where I just was, step forward" — e.g., walking through a citation graph, iterating through a customer's order history in date order. Without an explicit "continue from previous attention" mechanism, the agent has to re-search every step, which is both expensive and brittle.

**Example of good use:** A memory-architect team building an agent that walks through email threads exposes both a content-based search ("find emails about X") AND a cursor-based iteration ("get the next email after the one we just looked at"). The cursor is the NTM-style location-addressing layer. The agent can fluidly switch between random-access lookup and sequential walking, dramatically reducing the LLM round-trips for multi-step queries.

**Example of misapplication:** A team exposes only content-based vector search over memory. When the agent needs to walk a chronological sequence, every step requires a new embedding-query — and small embedding noise causes the agent to "jump" out of the sequence or revisit the same entry twice. They blame the vector store but the missing primitive is iteration / location-addressing.

## Extracted Prompts

```
No applicable prompts found in this paper. NTMs are trained with gradient descent on algorithmic input/output pairs; there are no LLM prompts.
```

## Citations

- LSTM (Hochreiter & Schmidhuber, 1997)
- Generating sequences with RNNs (Graves, 2013) — arxiv:1308.0850
- On the difficulty of training RNNs (Pascanu et al., 2013) — arxiv:1211.5063
- Recursive distributed representations (Pollack, 1990)
- Holographic reduced representations (Plate, 1995)
- Seq2seq learning (Sutskever et al., 2014) — arxiv:1409.3215
- Memory networks (Weston et al., 2014) — arxiv:1410.3916
- Bahdanau attention (2014) — arxiv:1409.0473
- (Full ~30-reference list in frontmatter `citations:`)

## Related Digests

- [[sukhbaatar-2015-end-to-end-memory-networks]] — direct descendant: makes Memory Networks end-to-end differentiable, building on NTM
- [[vaswani-2017-attention-is-all-you-need]] — Transformer attention is the modern realisation of NTM's content-addressable read
- [[hu-2026-evermemos]] — modern agent memory; cites NTM as a foundational ancestor
- [[liu-2023-think-in-memory]] — Think-in-memory: cites NTM for the controller/memory split
- [[zhong-2023-memorybank-llm]] — MemoryBank: cites NTM as a precursor to learned external memory

## Reviewer Notes

**Overall severity:** Clean

Claims cross-checked against the loaded paper text:
- Controller + read/write heads + external memory matrix M ∈ R^{N×M} — verified Section 3.
- Content-based + location-based addressing — verified Section 3.3.
- Differentiable end-to-end training — verified Section 3 / 4.
- Tasks: copy, repeat copy, associative recall, dynamic n-grams, priority sort — verified Section 4.
- NTM with LSTM controller, NTM with feedforward controller, LSTM-only baseline — verified Section 4.
- Generalisation to longer-than-training sequences — verified Figures 4–8.
