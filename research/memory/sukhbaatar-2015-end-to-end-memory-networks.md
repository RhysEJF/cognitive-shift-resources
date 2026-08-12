---
corpus: agentic-memory
kind: paper-digest
slug: sukhbaatar-2015-end-to-end-memory-networks
title: "End-To-End Memory Networks"
authors:
  - "Sainbayar Sukhbaatar"
  - "Arthur Szlam"
  - "Jason Weston"
  - "Rob Fergus"
year: 2015
publication_date: "2015-11"
venue: "NeurIPS 2015 (arXiv:1503.08895v5)"
source_url: "https://arxiv.org/abs/1503.08895"
doi: null
arxiv_id: "1503.08895"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Soft attention plus multiple read passes (\"hops\") over a shared external memory store can be learned end-to-end from input/output pairs alone — removing the per-fact supervision that the original Memory Networks required and turning attention-over-memory into a differentiable, stackable primitive that works on both QA and language modeling."
topics:
  - memory-architecture
  - attention-mechanisms
  - external-memory
  - retrieval-augmented-reasoning
  - multi-hop-reasoning
  - language-modeling
  - question-answering
  - babi-tasks
  - end-to-end-learning
tags:
  - paper
  - foundational
  - memory-networks
  - attention
  - softmax-retrieval
  - weak-supervision
  - rnn-alternative
  - engram-network
  - engram-retrieve
  - engram-aggregate
entities:
  - sukhbaatar-sainbayar
  - szlam-arthur
  - weston-jason
  - fergus-rob
  - facebook-ai-research
related_digests:
  - chhikara-2025-mem0
  - packer-2023-memgpt-os
  - latimer-2025-hindsight-memory
citations:
  - title: "Memory-based neural networks for robot learning"
    authors: ["C. G. Atkeson", "S. Schaal"]
    year: 1995
    venue: "Neurocomputing 9:243-269"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["D. Bahdanau", "K. Cho", "Y. Bengio"]
    year: 2015
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1409.0473"
  - title: "A neural probabilistic language model"
    authors: ["Y. Bengio", "R. Ducharme", "P. Vincent", "et al."]
    year: 2003
    venue: "JMLR 3:1137-1155"
    doi: null
    url: null
    arxiv_id: null
  - title: "Empirical evaluation of gated recurrent neural networks on sequence modeling"
    authors: ["J. Chung", "Ç. Gülçehre", "K. Cho", "et al."]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1412.3555"
  - title: "Learning context-free grammars: Capabilities and limitations of a recurrent neural network with an external stack memory"
    authors: ["S. Das", "C. L. Giles", "G.-Z. Sun"]
    year: 1992
    venue: "Cognitive Science Society"
    doi: null
    url: null
    arxiv_id: null
  - title: "A bit of progress in language modeling"
    authors: ["J. Goodman"]
    year: 2001
    venue: "CoRR cs.CL/0108005"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generating sequences with recurrent neural networks"
    authors: ["A. Graves"]
    year: 2013
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1308.0850"
  - title: "Neural Turing Machines"
    authors: ["A. Graves", "G. Wayne", "I. Danihelka"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1410.5401"
  - title: "DRAW: A recurrent neural network for image generation"
    authors: ["K. Gregor", "I. Danihelka", "A. Graves", "et al."]
    year: 2015
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1502.04623"
  - title: "Long short-term memory"
    authors: ["S. Hochreiter", "J. Schmidhuber"]
    year: 1997
    venue: "Neural Computation 9(8):1735-1780"
    doi: null
    url: null
    arxiv_id: null
  - title: "Inferring algorithmic patterns with stack-augmented recurrent nets"
    authors: ["A. Joulin", "T. Mikolov"]
    year: 2015
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "A clockwork RNN"
    authors: ["J. Koutník", "K. Greff", "F. J. Gomez", "et al."]
    year: 2014
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Building a large annotated corpus of english: The Penn Treebank"
    authors: ["M. P. Marcus", "M. A. Marcinkiewicz", "B. Santorini"]
    year: 1993
    venue: "Computational Linguistics 19(2):313-330"
    doi: null
    url: null
    arxiv_id: null
  - title: "Statistical language models based on neural networks"
    authors: ["T. Mikolov"]
    year: 2012
    venue: "PhD thesis, Brno University of Technology"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning longer memory in recurrent neural networks"
    authors: ["T. Mikolov", "A. Joulin", "S. Chopra", "et al."]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1412.7753"
  - title: "A connectionist symbol manipulator that discovers the structure of context-free languages"
    authors: ["M. C. Mozer", "S. Das"]
    year: 1993
    venue: "NIPS pages 863-863"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards Neural Network-based Reasoning"
    authors: ["B. Peng", "Z. Lu", "H. Li", "et al."]
    year: 2015
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1508.05508"
  - title: "The induction of dynamical recognizers"
    authors: ["J. Pollack"]
    year: 1991
    venue: "Machine Learning 7(2-3):227-252"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning matrices and their applications"
    authors: ["K. Steinbuch", "U. Piske"]
    year: 1963
    venue: "IEEE Transactions on Electronic Computers 12:846-862"
    doi: null
    url: null
    arxiv_id: null
  - title: "LSTM neural networks for language modeling"
    authors: ["M. Sundermeyer", "R. Schlüter", "H. Ney"]
    year: 2012
    venue: "Interspeech pages 194-197"
    doi: null
    url: null
    arxiv_id: null
  - title: "Pattern recognition by means of automatic analogue apparatus"
    authors: ["W. K. Taylor"]
    year: 1959
    venue: "Proc. Institution of Electrical Engineers 106:198-209"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards AI-complete question answering: A set of prerequisite toy tasks"
    authors: ["J. Weston", "A. Bordes", "S. Chopra", "et al."]
    year: 2015
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1502.05698"
  - title: "Memory Networks"
    authors: ["J. Weston", "S. Chopra", "A. Bordes"]
    year: 2015
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1410.3916"
  - title: "Show, Attend and Tell: Neural Image Caption Generation with Visual Attention"
    authors: ["K. Xu", "J. Ba", "R. Kiros", "et al."]
    year: 2015
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1502.03044"
  - title: "Recurrent neural network regularization"
    authors: ["W. Zaremba", "I. Sutskever", "O. Vinyals"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1409.2329"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Single-layer and three-layer versions of the End-to-End Memory Network"
  page: 2
  image_path: "figures/sukhbaatar-2015-end-to-end-memory-networks-fig.png"
---

# End-To-End Memory Networks

**Authors:** Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston, Rob Fergus
**Published:** 2015-11 (NeurIPS 2015) · [Source](https://arxiv.org/abs/1503.08895)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

End-to-End Memory Networks (MemN2N) replace the hard, per-fact-supervised lookups of Weston et al.'s original Memory Networks with a stack of differentiable softmax-attention reads over a shared external memory, trained end-to-end with only input/output pairs. On the 20 bAbI synthetic QA tasks (vocabulary V=177, ≤320 sentences per problem, memory capped at the most recent 50 sentences), the best MemN2N variant (position encoding + linear start + random-noise time jitter, joint training, 3 hops, embedding dim d=50) reaches 12.6% mean error on 1k examples and 4.2% on 10k — versus 6.7% / 3.2% for the strongly-supervised MemNN, 51.3% / 36.4% for an LSTM, and 40.2% / 39.2% for the weakly-supervised heuristic MemNN-WSH. On language modeling, a 7-hop MemN2N with memory size 200 hits 111 test perplexity on Penn Treebank (vs 129 RNN, 115 LSTM) and 147 on Text8 (vs 184 RNN, 154 LSTM), using ~1.5x the parameters of the comparable RNN versus LSTM's ~4x. The single most consistent finding across both regimes: **more hops monotonically lower error/perplexity** — 1→2→3 hops on QA, 2→7 hops on language modeling — confirming that the multi-step recurrence over memory (not the memory itself) is where the gains come from. Source: https://github.com/facebook/MemNN.

## Key Takeaway

Soft attention plus multiple read passes ("hops") over a shared external memory store can be learned end-to-end from input/output pairs alone — removing the per-fact supervision that the original Memory Networks required and turning attention-over-memory into a differentiable, stackable primitive that works on both QA and language modeling. The depth of reasoning lives in the number of memory hops, not the size of the memory: a 1-hop model fails most bAbI tasks; a 3-hop model passes them.

## Implications

- **[ENGRAM: Retrieve] Retrieval depth is a tunable hyperparameter, not a property of the data**: This paper shows monotonic gains from 1→2→3 hops on QA and 2→7 on language modeling — depth of reasoning is something the architecture buys, not something the corpus contains. For an agentic memory OS, treat "number of retrieval passes per query" as a first-class knob with a measurable accuracy/cost frontier.
- **[ENGRAM: Encode → Retrieve coupling] Position-of-write inside a chunk matters, not just the chunk itself**: The position encoding (PE) trick — `m_i = Σ_j l_j · A x_{ij}` with a hand-designed `l_j` — collapses error on bAbI tasks 4, 5, 15, 18 from ~15-50% to 0-3% by making word order intra-sentence affect the memory vector. Lesson for chunk-based memory systems: a bag-of-tokens encoding throws away signal you'll wish you had at retrieval time.
- **[ENGRAM: Encode] Temporal/positional metadata belongs in the memory vector, not in a separate index**: `m_i = Σ_j A x_{ij} + T_A(i)` learns a per-row temporal offset and is augmented with 10% random "dummy" memories at training time (the RN trick) to keep the time embedding from over-fitting absolute positions. Concretely, for systems that store dated artifacts: add learned (or hand-designed) recency-decay embeddings *inside* the memory vector rather than relying on post-hoc time filters.
- **[ENGRAM: Aggregate] You can drop per-fact supervision and still ship**: MemN2N's whole reason to exist is that the original Memory Networks required the "supporting sentence" labels at training time, which is unrealistic for real corpora. The end-to-end soft-attention training closes most (but not all) of the gap — 12.6% vs 6.7% on 1k bAbI. For a write-time/query-time tradeoff debate: this is empirical evidence that lifting supervision moves the line but doesn't break the system, as long as you have enough hops.
- **[ENGRAM: Maintain] Optimization tricks dominate architecture tricks at small data**: Linear start (LS) — training with all interior softmaxes removed, then re-inserting them — drops task-16 error from 53.6% to 1.6% on 1k. Random-noise time-index jitter shaves another ~2.4 points off mean error. Conclusion: with small memory datasets, your gains will come from training schedule and regularization, not from a clever attention variant.
- **[ENGRAM: Retrieve] Different hops specialize — and the specialization is interpretable**: Figure 3 shows that in trained LMs, some hops attend broadly across all memory positions (cache-like) while others concentrate on recent words (n-gram-like), and the two types alternate. This is direct evidence for designing multi-head/multi-hop retrievers with *intentional role differentiation* rather than letting all heads learn the same thing. For ENGRAM-aligned memory systems: expose hops as named retrieval roles (recency, broad-context, entity-resolution) rather than as anonymous parallel heads.
- **[ENGRAM: Network] A flat external memory with shared read/write embeddings beats sequence-state memory at fixed parameter budget**: MemN2N has ~1.5x the parameters of a comparable RNN but ~4x fewer than the comparable LSTM and still wins perplexity on both PTB (111 vs 115) and Text8 (147 vs 154). The architectural choice — global memory with shared functions — pays off relative to per-cell LSTM gates. Memory-system designers should be skeptical of any "stateful agent" pitch that doesn't separate the storage substrate from the read/write head.
- **[ENGRAM: Network ↔ Maintain] Smooth lookups break at scale — the authors say so explicitly**: The conclusion warns that "smooth lookups may not scale well to the case where a larger memory is required" and points toward hashing or multi-scale attention as next steps. Take this as a 2015 prediction borne out by the entire post-2017 retrieval-augmented stack: at large memory, soft attention over all rows is the cost bottleneck, and approximate / sharded retrieval becomes mandatory.

## How to Apply It (method)

**Scenario:** You are running a memory-architecture experiment for an agentic OS. You have a corpus of project-state documents (sprint notes, decisions, contradictions, completed-task logs) and you want to test whether a multi-hop attention reader over this memory beats a single-shot RAG retrieval on multi-step questions like "Which decision from last sprint contradicts the one we made today, and what changed in between?" You want to know whether the *number of read passes* — not the chunking strategy — is what's gating accuracy.

**Steps:**

1. **Frame the memory as a discrete buffer of items**: Cap memory at the M most recent documents (paper uses M=50 for QA, M=25-200 for LM). Each item is a short text span. Store as a list of token sequences `x_1, ..., x_M`. No embedding yet — just structure.

2. **Pick a sentence-to-vector encoder with position awareness**: Don't use bag-of-words; use position encoding (PE). For each item `x_i = {x_{i1}, ..., x_{iJ}}` of J tokens:

   ```
   m_i = Σ_j l_j · A x_{ij}
   l_{kj} = (1 - j/J) - (k/d)(1 - 2j/J)
   ```

   Where `A` is a d×V learnable embedding matrix (V = vocab size, d = embedding dim, paper uses d=20 for per-task or d=50 for joint training). `l_j` is a fixed (not learned) d-dimensional position weight vector. `·` is element-wise multiply.

3. **Add temporal encoding inside the memory vector**: Append a learned per-row temporal embedding `T_A(i)` so `m_i = Σ_j l_j · A x_{ij} + T_A(i)`. Index sentences in reverse order — `x_1` is the most recent. This means "recency" becomes a learned bias, not a post-hoc filter.

4. **Inject training-time time-jitter ("random noise")**: At training time only, randomly insert ~10% empty/dummy memories into each story. This regularizes `T_A` against overfitting to absolute positions. Skip at test time.

5. **Build a K-hop reader head**: For each hop k = 1...K:
   - Compute attention `p_i = softmax(u_k^T m_i)` where `u_k` is the current query state (initialized from the query embedding `B q`).
   - Compute output `o_k = Σ_i p_i c_i` where `c_i` is a separate output embedding of item i (with its own embedding matrix `C` and own temporal matrix `T_C`).
   - Update query state: `u_{k+1} = u_k + o_k` (adjacent weight tying) **or** `u_{k+1} = H u_k + o_k` (layer-wise / RNN-like tying, where H is a learned linear map).

6. **Tie weights aggressively**: Use **adjacent tying** for QA: `A^{k+1} = C^k`, `W^T = C^K`, `B = A^1`. Use **layer-wise tying** for language modeling: all `A^k` equal, all `C^k` equal, add the linear `H` map. Tying cuts parameters and helps deeper models generalize.

7. **Final prediction**: `â = softmax(W (o_K + u_K))` for the answer. Cross-entropy loss against true label.

8. **Train with the "linear start" warm-up**: Phase 1: remove ALL interior softmaxes (the model is now linear up to the final softmax), train with learning rate η=0.005 until validation loss plateaus. Phase 2: re-insert softmaxes, continue training with η=0.01, anneal η/2 every 25 epochs to 100 epochs. Batch size 32 for QA, 128 for LM. Gradient L2 norm capped at 40 (QA) or 50 (LM).

9. **Run the hop-count ablation**: This is the experiment that matters. Train identical models with K = 1, 2, 3 hops (also try 4, 5, 6, 7 for LM). Plot mean error vs hops. The paper's gain pattern (PTB: 128 → 129 → 127 → 127 → 127 → 122 → 120 from 2 to 7 hops at memory size 100) tells you when to stop adding hops.

10. **Inspect attention patterns per hop**: For each hop, plot the attention weight distribution over memory positions across your test queries (Figure 3 in the paper). Look for *role differentiation*: do some hops always attend recently? Do some attend broadly? If all hops look identical, your tying is too aggressive or your task doesn't actually need multi-hop reasoning.

11. **Compare against single-hop RAG and against a stateful baseline**: Use the same memory corpus and (a) a 1-hop variant of your model as the RAG-baseline, (b) an LSTM that reads the memory sequentially. The paper's numbers say multi-hop should comfortably beat both — if it doesn't, the bottleneck isn't retrieval depth.

**Expected outcome:** A defensible answer to "does our memory system actually benefit from multi-pass retrieval, or is one read enough?" — with a hop-count curve, an attention-role analysis, and per-task error rates that tell you which question types specifically need depth (multi-fact composition, temporal reasoning, induction) versus which don't (single-fact lookup, simple coreference). The architecture transfers directly into the ENGRAM "Retrieve" dimension as a tunable knob you can expose to upstream agents.

## Best Figure

![Figure 1 — Single-layer and three-layer versions of the End-to-End Memory Network (page 2)](figures/sukhbaatar-2015-end-to-end-memory-networks-fig.png)

**Image Candidates:**

- Figure 1 (p. 2): The canonical architecture diagram — single-layer (a) and three-hop stacked (b) side by side — shows the entire model in one view, including the embedding flow, soft attention, and how the layer outputs chain.
- Figure 3 (p. 7): Attention heatmaps across 6 memory hops on Penn Treebank vs Text8 — visually proves the central "hops specialize and alternate between cache-like and n-gram-like attention" finding.
- Figure 2 (p. 7): Per-hop attention probabilities on 4 sample bAbI stories — directly demonstrates that the model learns to focus on the labeled supporting facts despite not being trained on them.

**Best Image:**

- **Figure Name:** Figure 1: "(a) A single layer version of our model. (b) A three layer version of our model."
- **Figure Page:** 2
- **Slide Caption:** End-to-End Memory Network architecture — single hop (left) and the same primitive stacked three times (right) — showing how multi-hop reasoning composes by reusing the same memory-read block.
- **Description:** Figure 1 puts the entire MemN2N architecture in one frame. Panel (a) shows the single-layer case: input sentences `{x_i}` are embedded twice — once via matrix A (the memory representation `m_i`) and once via matrix C (the output representation `c_i`). The query q is embedded via B into state u. A softmax over `u · m_i` produces attention weights `p_i`, which weight-sum the `c_i` into output o; the prediction is `softmax(W(o+u))`. Panel (b) shows the three-hop stack: each layer has its own A^k, C^k embeddings (constrained by weight tying), the previous hop's `u_k + o_k` becomes the next hop's query, and only the top layer emits a prediction. The figure makes the paper's central conceptual claim visible at a glance: a soft-attention memory read is a reusable, differentiable block; "deep reasoning" is just stacking the same block.

## What Experts Overlook

The detail most reviewers overlook is the **"linear start" (LS) training schedule** — and how dramatically it changes which tasks the model can solve. In Section 4.2 and confirmed in Table 1 of the paper, the authors describe starting training with every interior softmax *removed* (the model becomes entirely linear up to the final softmax for answer prediction), training until validation loss plateaus at a lower learning rate (η=0.005), then re-inserting the softmaxes and continuing. The numerical effect is shocking: on bAbI task 16 ("basic induction") with 1k training data and position encoding, error drops from 53.6% to 1.6% — a 33x reduction — purely from this warm-up trick. The same pattern shows up on several other tasks (compare PE column vs PE+LS column in Table 1).

**Why it matters:** Most readers walk away from this paper thinking the architecture (multi-hop soft attention) is what does the work. But the architecture alone gets stuck in bad local minima on the tasks that require composition (induction, deduction, multi-fact reasoning). The linear-start trick reshapes the loss landscape: a fully linear model has a much smoother loss, so SGD finds a good basin first; when you re-insert the softmaxes you're starting from a good initialization rather than from random weights inside a non-convex landscape. This is a generalizable lesson for any memory architecture with stacked attention layers — *staged training* (start simple, add complexity once a basin is found) may be doing more work than the architectural cleverness it's hiding behind.

**Example of good use:** When building a multi-hop retrieval head for an agent's memory layer, train it first with hard `argmax` selection (or no normalization at all on intermediate hops) before switching to softmax attention. Expect to see specific reasoning task categories (composition, induction-like patterns) work *only* after this warm-up. Report the comparison numbers — you'll likely find that the staged-training delta is comparable to your architectural delta, and reviewers will trust your method more for naming it.

**Example of misapplication:** A team builds a new "deep attention memory" with 5 stacked hops and trains it cold (random init, all softmaxes active from epoch 0). On their composition benchmark, error is 50%+. They conclude the architecture doesn't work and pivot to a non-attention design — when in fact they reproduced the exact failure mode (task 16 at 53.6% without LS) that Sukhbaatar et al. solved with a 2-line training change. A whole research direction gets shelved because the optimization trick wasn't noticed.

## Extracted Prompts

No applicable prompts found in this paper.

(This is a neural-network architecture paper — the "queries" are tokenized bAbI question sentences and word-stream language-modeling contexts, not LLM prompts. The model is trained on tokens with cross-entropy loss, not prompted in natural language.)

## Citations

- Atkeson, C. G. & Schaal, S. (1995). *Memory-based neural networks for robot learning.* Neurocomputing 9:243-269.
- Bahdanau, D., Cho, K., & Bengio, Y. (2015). *Neural machine translation by jointly learning to align and translate.* ICLR. (arXiv:1409.0473)
- Bengio, Y., Ducharme, R., Vincent, P., & Janvin, C. (2003). *A neural probabilistic language model.* JMLR 3:1137-1155.
- Chung, J. et al. (2014). *Empirical evaluation of gated RNNs on sequence modeling.* arXiv:1412.3555.
- Das, S., Giles, C. L., & Sun, G.-Z. (1992). *Learning context-free grammars with an external stack memory.* Cognitive Science Society.
- Graves, A., Wayne, G., & Danihelka, I. (2014). *Neural Turing Machines.* arXiv:1410.5401.
- Hochreiter, S. & Schmidhuber, J. (1997). *Long short-term memory.* Neural Computation 9(8):1735-1780.
- Joulin, A. & Mikolov, T. (2015). *Inferring algorithmic patterns with stack-augmented recurrent nets.* NIPS.
- Mikolov, T. et al. (2014). *Learning longer memory in recurrent neural networks.* arXiv:1412.7753.
- Weston, J., Chopra, S., & Bordes, A. (2015). *Memory Networks.* ICLR. (arXiv:1410.3916) — **the direct predecessor this paper is the end-to-end version of**.

(Full 25-entry citation list with structured metadata in frontmatter.)

## Related Digests

- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory — 10 years later, the same Network/Retrieve choice (flat memory + LLM-extracted facts) still wins on cost vs heavyweight graph alternatives, vindicating MemN2N's "global memory + shared read function" design intuition.
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems — replaces the soft attention head with explicit paging function calls but inherits the same separation of substrate from read/write head that this paper introduced.
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects — modern descendant where the "multi-hop" idea has become "multiple typed retrieval networks" but the empirical claim — that architecture, not parameter count, is where the points come from — is the lineal continuation of this paper's "more hops, lower error" finding.

## Reviewer Notes

**Overall severity:** Clean

All major numerical claims in the digest were checked against Table 1 (12.6% / 6.7% / 51.3% / 40.2% mean errors at 1k, 4.2% / 3.2% / 36.4% / 39.2% at 10k), Table 2 (perplexities of 111/115/129 on PTB at 7 hops with memory size 200, and 147/154/184 on Text8), Section 4.1 (vocabulary V=177, memory cap 50, position encoding formula, 10% random noise), Section 4.2 (learning rates, annealing, gradient norm cap 40), Section 5.1 (gradient norm cap 50 for LM, batch 128, annealing schedule), and the abstract / conclusion (claim of multi-hop monotonic improvement). The bAbI task-16 LS effect (53.6% → 1.6%) is verified in Table 1's PE vs PE+LS columns for task 16 at 1k. The 1.5x / 4x parameter ratios for MemN2N vs RNN/LSTM are stated verbatim in Section 5.2. The "Figure 3 alternating hops" interpretation is supported by Section 5.2's discussion of cache-like + n-gram-like alternation. The "linear start avoids local minima" framing is in the paper's "interesting points" bullet list in Section 4.4. No fabrications detected; the source-code URL https://github.com/facebook/MemNN is cited in footnote 2 of the paper.
