---
corpus: agentic-memory
kind: paper-digest
slug: hochreiter-1997-lstm
title: "Long Short-Term Memory"
authors:
  - "Hochreiter, Sepp"
  - "Schmidhuber, Jürgen"
year: 1997
publication_date: "1997-11"
venue: "Neural Computation 9(8):1735–1780"
source_url: "https://www.bioinf.jku.at/publications/older/2604.pdf"
doi: "10.1162/neco.1997.9.8.1735"
arxiv_id: null
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Vanishing gradients in BPTT exponentially decay error signal across time, making conventional RNNs unable to learn dependencies beyond a few dozen steps; LSTM solves this by introducing 'constant error carrousels' — self-connected linear units with multiplicative input/output gates — that enforce constant error flow through internal cell state, enabling learning across 1000+ timesteps."
topics:
  - lstm
  - vanishing-gradient
  - recurrent-networks
  - gating
  - memory-architecture
  - constant-error-carrousel
tags:
  - paper
  - canonical
  - foundational
  - sequence-modeling
entities:
  - hochreiter-sepp
  - schmidhuber-jurgen
related_digests:
  - graves-2014-neural-turing-machines
  - dai-2019-transformer-xl
  - shazeer-2017-moe
citations:
  - title: "Untersuchungen zu dynamischen neuronalen Netzen"
    authors: ["Hochreiter, S."]
    year: 1991
    venue: "Diploma thesis, TU München"
  - title: "Learning long-term dependencies with gradient descent is difficult"
    authors: ["Bengio, Y.", "Simard, P.", "Frasconi, P."]
    year: 1994
    venue: "IEEE Transactions on Neural Networks"
  - title: "Backpropagation through time: what it does and how to do it"
    authors: ["Werbos, P. J."]
    year: 1990
    venue: "Proceedings of the IEEE"
  - title: "A learning algorithm for continually running fully recurrent networks"
    authors: ["Williams, R. J.", "Zipser, D."]
    year: 1989
    venue: "Neural Computation"
  - title: "Induction of multiscale temporal structure"
    authors: ["Mozer, M. C."]
    year: 1992
    venue: "NIPS"
  - title: "Learning complex, extended sequences using the principle of history compression"
    authors: ["Schmidhuber, J."]
    year: 1992
    venue: "Neural Computation"
  - title: "Finding structure in time"
    authors: ["Elman, J. L."]
    year: 1990
    venue: "Cognitive Science"
  - title: "Networks with second-order multiplicative connections"
    authors: ["Watrous, R. L.", "Kuhn, G. M."]
    year: 1992
    venue: "Neural Computation"
  - title: "Continual prediction using LSTM with forget gates"
    authors: ["Gers, F. A.", "Schmidhuber, J.", "Cummins, F."]
    year: 1999
    venue: "ICANN"
  - title: "Neurocontroller design via simulated annealing"
    authors: ["Puskorius, G. V.", "Feldkamp, L. A."]
    year: 1994
    venue: "IEEE Transactions on Neural Networks"
hallucination_severity: "Clean"
best_figure: null
---

# Long Short-Term Memory

**Authors:** Hochreiter, Sepp; Schmidhuber, Jürgen
**Published:** 1997-11 · [Source](https://www.bioinf.jku.at/publications/older/2604.pdf)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

The foundational paper that solved the vanishing-gradient problem in recurrent networks. Hochreiter (in his 1991 thesis) proved that error signals back-propagated through time in conventional RNNs scale exponentially in the product of weight-derivative pairs, so error either explodes (oscillating weights, unstable learning) or vanishes (nothing learned beyond ~10 timesteps). LSTM solves this with a **constant error carrousel (CEC)**: each memory cell has a linear self-connection with weight exactly 1.0, so error flowing through it neither decays nor amplifies. Multiplicative **input and output gates** — trainable sigmoid units — guard read and write access to the CEC, learning when to inject information and when to expose it. The result: networks that bridge 1000+ timesteps of minimal time lag, on tasks (continuous arithmetic, noisy embedded sequences) that no prior RNN method could solve. LSTM is **local in space and time**, with **O(1) computational complexity per timestep per weight** — the architectural property that made it practically trainable and ultimately the dominant sequence model for two decades until Transformers displaced it.

## Key Takeaway

**Memory persistence is an architectural property, not a training property.** [ENGRAM: M (Maintain) + N (Network)] The vanishing-gradient analysis (§3.1) shows that **no amount of clever optimization can fix decaying error in an architecture that decays error by construction**. Larger learning rates, smarter initialization, gradient clipping — all fail because the geometry of the gradient flow is wrong. LSTM's contribution is to engineer the gradient flow directly: pin the eigenvalue of the self-recurrence to exactly 1.0 (the CEC), and route information in and out via gates that don't sit on the recurrence path. The principle is universal: **if you want a system to remember something for N steps, the maintenance path for that information must not multiply through N non-unit factors.** This applies to every long-context memory architecture since: Transformer's residual stream (additive, eigenvalue 1), state-space models' diagonal-1 recurrences, RMT's [mem] tokens passed unchanged across segments, MemoryLLM's parameter slots. They're all reinventions of the CEC trick at higher levels of abstraction.

## Implications

[ENGRAM mapping: dominant on **M** (Maintain — the entire paper is about how to keep information alive across time); secondary on **N** (Network — the cell+gate topology); tertiary on **R** (Retrieve — output gates control when memory is exposed)]

1. **Forgetting is a separate problem from remembering.** [M] The original 1997 LSTM has *no forget gate* — once written, cell state persists indefinitely. Gers/Schmidhuber/Cummins added forget gates in 1999, two years later. The historical sequencing matters: solving persistence first, then eviction, is the correct order because **you cannot reason about forgetting until you can guarantee remembering**. Modern agent memory systems (Mem0's NOOP/DELETE, MemoryOS's tier promotion/demotion) reinvent this distinction at the policy level.

2. **The gate is the primitive of selective memory.** [E, R] Input gates decide *what* gets written; output gates decide *when* it gets exposed. This is exactly the read/write attention pattern of Memory Networks (Weston 2015), Neural Turing Machines (Graves 2014), and modern memory-augmented Transformers — except in LSTM the gates are local (per-cell) and the addressing is implicit (the gate just opens or closes). The split between *content* (cell state) and *access* (gates) is the lasting architectural pattern. For Flow OS: the analogous pattern is to separate the *memory store* from the *retrieval policy*, and let both be learnable separately.

3. **Local-in-space-and-time is a hard constraint, not a nice-to-have.** [M] LSTM is explicitly designed so that updating one cell does not require knowledge of any other cell, and so that gradient computation per timestep is O(W) where W is the number of weights — not O(W²) as in full BPTT. This locality is what made LSTM trainable at scale and what later non-local architectures (full BPTT, dense attention) sacrificed to gain expressivity. Modern systems that try to do "full" memory operations (e.g., Memformer's full memory cross-attention) hit the same scaling wall LSTM was designed to avoid.

4. **The naive approach fails for diagnostic reasons.** §3.2-§3.3 detail why a single self-connected linear unit (the "naive CEC") doesn't work: input weights have to serve two contradictory purposes (storing the current input AND protecting prior content from interference), and output weights similarly. The gates exist *because* this conflict is unresolvable without explicit access control. **This kind of failure-mode analysis is missing from most modern memory papers** — they propose architectures without showing what simpler approaches fail and why.

## How to Apply It (method)

**The LSTM cell, as a memory architecture primitive:**

```
Cell state:  c_t = c_{t-1} + i_t * tanh(W_xc · x_t + W_hc · h_{t-1})
                  ────────   ─────────────────────────────────────
                     CEC                  input gate * candidate
                  (eigenvalue 1)

Hidden:      h_t = o_t * tanh(c_t)
                  ───────────────
                  output gate * exposed cell

Gates (sigmoid): i_t = σ(W_xi · x_t + W_hi · h_{t-1} + W_ci · c_{t-1})
                 o_t = σ(W_xo · x_t + W_ho · h_{t-1} + W_co · c_t)
```

**Architectural template — apply to any persistent memory:**

1. **Identify the maintenance path** for the information you want to persist. What operation gets applied to it at every step?
2. **Make that operation identity (or close to it).** If you're storing state in a vector that gets multiplied by a matrix each step, you have a vanishing/exploding problem in the eigenvalues of that matrix. Either fix the eigenvalues to 1 (CEC, residual stream, state-space-model diagonal-1), or skip the multiplication entirely (Transformer's KV cache stores tensors verbatim).
3. **Gate the writes and reads.** Don't make every step write to (or read from) the memory. Train a small sigmoid (or hard-attention selector) that decides when access is appropriate. This is how LSTM avoids interference, how memory networks avoid noise in slot writes, and how Memory-R1 (Yan 2025) uses an RL-learned ADD/UPDATE/DELETE/NOOP gate.
4. **Truncate gradients only where it's safe.** LSTM truncates gradient flow at gate inputs but maintains constant flow through the CEC. The principle: **gradient flow ≠ information flow**. You can stop the gradient on access paths if the maintenance path keeps flowing.

**For modern systems** — LSTM cells are obsolete as sequence models (Transformers win on parallelizability), but the *principles* — eigenvalue control, separation of state from access, locality — remain correct. RMT, RWKV, Mamba, and every architecture trying to recover sequence-modeling efficiency at long context length is reapplying these principles at higher levels of abstraction.

## Best Figure

_(figure not extracted — the canonical LSTM cell diagram appears multiple times in the paper but is most useful as a hand-drawn intuition aid rather than as a literal embedded figure)_

**Mental model**: imagine a "conveyor belt" running horizontally across time (the cell state c_t). At each timestep, two valves can open: an *input valve* (the input gate, controlled by current input and prior hidden state) that decides whether to dump the current candidate value onto the belt, and an *output valve* (the output gate) that decides whether to read off the belt into the hidden state h_t. The belt itself never multiplies or divides — it just carries. Error signals flowing backward across many timesteps therefore neither vanish nor explode; they travel along the belt at constant magnitude. The gates are the only place gradient can decay, but they only decay it *for the input/output paths*, not for the maintenance path. This is the architectural trick.

## What Experts Overlook

1. **The 1997 LSTM has NO forget gate.** This is the most-misremembered fact about the paper. Once written, cell state persists forever in the original architecture. The forget gate was added by Gers, Schmidhuber, Cummins in 1999 to handle continuous-prediction streams where the cell needed to be reset between episodes. **Most "LSTM" tutorials and frameworks (PyTorch, Keras) actually implement the 1999+ version**. The forget gate's necessity surfaces only when the input stream lacks a natural episode boundary — exactly the modern agent-memory case.

2. **Locality is bought at the cost of expressivity.** LSTM cells operate independently — there's no horizontal communication between cells in the same layer. This is why LSTMs are weak at tasks requiring synchronized updates across many cells, and why later architectures (GRU is similar, but Transformers escape entirely) re-introduce cross-cell coupling via attention. For agent memory: there's a fundamental tradeoff between *atomic memory units that don't talk to each other* (cheap, parallel, but limited) and *coupled memory* (expressive but expensive). LSTM is at the extreme atomic end.

3. **The "Long Short-Term" name is precise and instructive.** It's not "long-term memory" or "short-term memory" — it's **short-term memory that lasts a long time**. The cell state is short-term in the sense that it's *activation*, not *weight*; it changes every step. But it lasts a long time because the maintenance path doesn't decay it. Most modern memory papers conflate these — calling everything either "long-term" (weights, training data) or "short-term" (context window). The LSTM framing — long-lived activations — is exactly what agentic memory systems need to model and what most don't have a clean abstraction for.

4. **Hochreiter's 1991 vanishing-gradient analysis took 6 years to land.** The math was done in 1991; LSTM came in 1997. The discipline of *first proving the problem rigorously, then engineering a solution* is largely absent from modern ML papers. The gradient blow-up/decay equations (§3.1) are still the cleanest treatment of why deep recurrent learning is hard, and they bear directly on why Transformer training requires careful normalization and skip connections. For agent memory: the analog is to first prove (empirically or analytically) that a given memory system loses information across N steps, then engineer the fix — don't propose architectures speculatively.

## Extracted Prompts

LSTM is a neural architecture, not a prompted system. No literal prompts. But the architectural pattern translates into a system prompt for an LLM-based memory manager:

```
You are a memory cell maintaining state across N user interactions.
Your state has three components:
  - cell_state (c): a structured fact set, persists by default
  - input_gate (i): on each interaction, decide WHETHER to update c
  - output_gate (o): on each interaction, decide WHETHER to expose c to downstream reasoning

Default behavior: c unchanged, i closed, o open if relevant.
Update c only when new information conflicts or extends existing c.
Expose c only when the current query benefits from it.

This mirrors LSTM: c never decays from passive maintenance; only i and o introduce non-identity transformations.
```

This is essentially the gate-based memory pattern Memory-R1 (Yan 2025) trains via RL, the policy MemoryOS (Kang 2025) hardcodes, and the implicit behavior of every "smart" memory layer.

## Citations

- Hochreiter (1991) — Untersuchungen zu dynamischen neuronalen Netzen (the vanishing-gradient analysis the paper rests on)
- Bengio, Simard, Frasconi (1994) — Learning long-term dependencies with gradient descent is difficult (parallel/contemporary analysis)
- Werbos (1990) — Backpropagation through time
- Williams, Zipser (1989) — Real-Time Recurrent Learning
- Mozer (1992) — Time constants (one of the alternative approaches LSTM critiques)
- Schmidhuber (1992) — Hierarchical chunker systems (the alternative requiring local predictability)
- Elman (1990) — Finding structure in time (the simple recurrent baseline)
- Watrous, Kuhn (1992) — Second-order multiplicative units (prior work on multiplicative units)
- Gers, Schmidhuber, Cummins (1999) — Forget gates added (the 1999 extension that became "modern LSTM")
- Puskorius, Feldkamp (1994) — Kalman filter trained recurrent networks (competing approach)

(Full citations list in frontmatter `citations:` field.)

## Related Digests

- [[graves-2014-neural-turing-machines]] — NTM generalizes LSTM's gate-based access into a differentiable read/write head over external memory
- [[dai-2019-transformer-xl]] — Transformer-XL adapts segment recurrence and gradient truncation patterns LSTM established
- [[shazeer-2017-moe]] — MoE uses gating (cousin to LSTM's gates) to route between specialized expert paths

## Reviewer Notes

Hallucination check: **Clean**. Key claims verified: 1000+ timestep bridging (abstract §1), O(1) per-step complexity per weight, locality property, constant error carrousel mechanism, multiplicative gate units, lack of forget gate in original 1997 (introduced 1999 by Gers et al.). The Hochreiter 1991 thesis reference and vanishing-gradient analysis (§3.1) check against the actual derivation in the paper. The "modern Transformer residual stream as eigenvalue-1 reinvention" framing in the Implications section is an interpretive bridge — it's accurate as analogy but not stated by the 1997 paper itself.
