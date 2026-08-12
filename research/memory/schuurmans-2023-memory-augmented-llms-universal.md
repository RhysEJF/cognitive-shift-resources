---
corpus: agentic-memory
kind: paper-digest
slug: schuurmans-2023-memory-augmented-llms-universal
title: "Memory Augmented Large Language Models are Computationally Universal"
authors:
  - "Schuurmans, Dale"
year: 2023
publication_date: "2023-01"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2301.04589"
doi: null
arxiv_id: "2301.04589"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "A frozen 540B language model, wired to an associative read-write dictionary by finite-state regex glue, can exactly simulate the universal Turing machine U15,2 — so the LLM-as-CPU + memory-as-RAM split is not just a useful design pattern but a theoretical upper bound, and the load-bearing constraint is the language model's reliability on a finite, enumerable set of (state, symbol) prompt cases rather than memory size."
topics:
  - memory-augmented-llms
  - computational-universality
  - turing-completeness
  - associative-memory
  - stored-instruction-computer
  - prompt-programming
  - external-memory
  - read-write-memory
tags:
  - paper
  - theory
  - memory-architecture
  - engram-encode
  - engram-network
  - engram-retrieve
  - engram-aggregate
  - flan-u-palm
  - turing-machine
entities:
  - schuurmans-dale
  - flan-u-palm-540b
  - google-brain
  - university-of-alberta
related_digests:
  - graves-2014-neural-turing-machines
  - hu-2023-chatdb-symbolic-memory
  - modarressi-2024-memllm
  - modarressi-2023-ret-llm
  - packer-2023-memgpt-os
citations:
  - title: "Language Models are Few-Shot Learners"
    authors: ["Brown, T.", "Mann, B.", "Ryder, N.", "Subbiah, M.", "Kaplan, J.", "Dhariwal, P.", "et al."]
    year: 2020
    venue: "NeurIPS"
    url: "https://arxiv.org/abs/2005.14165"
    arxiv_id: "2005.14165"
  - title: "Scaling Instruction-Finetuned Language Models"
    authors: ["Chung, H. W.", "Hou, L.", "Longpre, S.", "Zoph, B.", "Tay, Y.", "Fedus, W.", "et al."]
    year: 2022
    venue: "arXiv"
    url: "https://arxiv.org/abs/2210.11416"
    arxiv_id: "2210.11416"
  - title: "Language Model Cascades"
    authors: ["Dohan, D.", "Xu, W.", "Lewkowycz, A.", "Austin, J.", "Bieber, D.", "Lopes, R. G.", "et al."]
    year: 2022
    venue: "arXiv"
    url: "https://arxiv.org/abs/2207.10342"
    arxiv_id: "2207.10342"
  - title: "Training language models to follow instructions with human feedback"
    authors: ["Ouyang, L.", "Wu, J.", "Jiang, X.", "Almeida, D.", "Wainwright, C.", "Mishkin, P.", "et al."]
    year: 2022
    venue: "NeurIPS"
    url: "https://arxiv.org/abs/2203.02155"
    arxiv_id: "2203.02155"
  - title: "Language models are unsupervised multitask learners"
    authors: ["Radford, A.", "Wu, J.", "Child, R.", "Luan, D.", "Amodei, D.", "Sutskever, I."]
    year: 2019
    venue: "OpenAI technical report"
    url: "https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf"
    arxiv_id: null
  - title: "Chain of Thought Prompting Elicits Reasoning in Large Language Models"
    authors: ["Wei, J.", "Wang, X.", "Schuurmans, D.", "Bosma, M.", "Ichter, B.", "Xia, F.", "Chi, E.", "Le, Q.", "Zhou, D."]
    year: 2022
    venue: "NeurIPS"
    url: "https://arxiv.org/abs/2201.11903"
    arxiv_id: "2201.11903"
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    authors: ["Zhou, D.", "Schärli, N.", "Hou, L.", "Wei, J.", "Scales, N.", "Wang, X.", "Schuurmans, D.", "et al."]
    year: 2022
    venue: "arXiv"
    url: "https://arxiv.org/abs/2205.10625"
    arxiv_id: "2205.10625"
  - title: "On the Turing Completeness of Modern Neural Network Architectures"
    authors: ["Pérez, J.", "Marinković, J.", "Parceló, P."]
    year: 2019
    venue: "ICLR"
    url: "https://arxiv.org/abs/1901.03429"
    arxiv_id: "1901.03429"
  - title: "On the Practical Computational Power of Finite Precision RNNs for Language Recognition"
    authors: ["Weiss, G.", "Goldberg, Y.", "Yahav, E."]
    year: 2018
    venue: "ACL"
    url: "https://arxiv.org/abs/1805.04908"
    arxiv_id: "1805.04908"
  - title: "On the Computational Power of Neural Nets"
    authors: ["Siegelmann, H.", "Sontag, E."]
    year: 2019
    venue: "COLT (orig. 1992)"
    url: null
    arxiv_id: null
  - title: "On the Computational Power of Transformers and its Implications in Sequence Modeling"
    authors: ["Bhattamishra, S.", "Patel, A.", "Goyal, N."]
    year: 2020
    venue: "CONLL"
    url: "https://arxiv.org/abs/2006.09286"
    arxiv_id: "2006.09286"
  - title: "Statistically Meaningful Approximation: a case study on approximating Turing machines with Transformers"
    authors: ["Wei, C.", "Chen, Y.", "Ma, T."]
    year: 2022
    venue: "NeurIPS"
    url: "https://arxiv.org/abs/2107.13163"
    arxiv_id: "2107.13163"
  - title: "Four Small Universal Turing Machines"
    authors: ["Neary, T.", "Woods, D."]
    year: 2009
    venue: "Fundamenta Informaticae 91:105–126"
    url: null
    arxiv_id: null
  - title: "Small Universal Turing Machines"
    authors: ["Neary, T."]
    year: 2008
    venue: "PhD thesis, National University of Ireland, Maynooth"
    url: null
    arxiv_id: null
  - title: "Universality in Elementary Cellular Automata"
    authors: ["Cook, M."]
    year: 2004
    venue: "Complex Systems 15:1–40"
    url: null
    arxiv_id: null
  - title: "A New Kind of Science"
    authors: ["Wolfram, S."]
    year: 2002
    venue: "Wolfram Media (book)"
    url: null
    arxiv_id: null
  - title: "A Universal Turing Machine with Two Internal States"
    authors: ["Shannon, C."]
    year: 1956
    venue: "Automata Studies, Annals of Mathematics Studies 34:157–165"
    url: null
    arxiv_id: null
  - title: "On Computable Numbers, with an Application to the Entscheidungsproblem"
    authors: ["Turing, A."]
    year: 1937
    venue: "Proceedings of the London Mathematical Society 2(42):230–265"
    url: null
    arxiv_id: null
  - title: "First Draft of a Report on the EDVAC"
    authors: ["von Neumann, J."]
    year: 1945
    venue: "Moore School / U. Penn technical report"
    url: null
    arxiv_id: null
  - title: "Calculatrices digitales du déchiffrage de formules logico-mathématiques par la machine même dans la conception du programme"
    authors: ["Böhm, C."]
    year: 1954
    venue: "PhD thesis, ETH Zürich"
    url: null
    arxiv_id: null
  - title: "General considerations in the design of an all purpose electronic digital computer"
    authors: ["Booth, A.", "Britten, K."]
    year: 1947
    venue: "Institute for Advanced Study, Princeton, technical report (2nd ed.)"
    url: null
    arxiv_id: null
  - title: "Introduction to the Theory of Computation"
    authors: ["Sipser, M."]
    year: 2013
    venue: "Cengage Learning, 3rd edition (textbook)"
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Transition table for the universal Turing machine U15,2 (the 29 (state, symbol) prompt cases the LLM must execute reliably)"
  page: 7
  image_path: "figures/schuurmans-2023-memory-augmented-llms-universal-fig.png"
---

# Memory Augmented Large Language Models are Computationally Universal

**Authors:** Dale Schuurmans (Google Brain & University of Alberta)
**Published:** 2023-01 · [Source](https://arxiv.org/abs/2301.04589)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

A transformer LLM with bounded context is, formally, just a finite automaton. Schuurmans shows that bolting an external associative read/write memory (a plain Python dictionary mapping string keys to string/int values) onto a frozen Flan-U-PaLM 540B — with only regex-based finite-state pre/post-processing between them — promotes the system to full Turing completeness. The construction is a von Neumann stored-instruction computer where the LLM is the CPU, the dictionary is the RAM, and an "instruction register" memory slot called `op` holds the next prompt. The fidelity proof reduces to checking that the LLM produces the correct output on each of 29 enumerated (state, symbol) prompt cases needed to simulate the universal Turing machine U15,2 (15 states, 2 tape symbols, Pareto-optimal smallest known) at temperature 0. No weights are modified. The result repositions "memory" from a useful augmentation to the *necessary and sufficient* lift from finite-state to universal — and identifies the LLM's reliability on a small, enumerable set of prompt programs (not its scale, not memory size) as the load-bearing constraint. [ENGRAM: E, N, R, A]

## Key Takeaway

The boundary between "a chatbot" and "an arbitrary computer" is one bounded-length context, one regex parser, and one mutable dictionary. Once you can persist *outside* the context window and write back into the next prompt deterministically, the model's frozen weights already contain enough generalisable conditional/assignment competence to drive universal computation — provided you can verify it answers a finite, enumerable set of prompt cases correctly. This recasts what memory is *for*: not "fitting more tokens" but "closing the substrate loop" so the LLM can act as a CPU rather than as a one-shot oracle. The constraint that bites is not memory size (the dictionary is unbounded by definition) or model size (540B was sufficient) — it is **LLM reliability on the specific prompt program**, and that's a brittle, enumerable, testable surface. [ENGRAM: E, N, A]

## Implications

**For ENGRAM Encode (E).** Encoding here is not "summarise and write" — it is mechanical regex extraction of `variable_name = "value"` and `variable_name += increment` patterns from the LLM's raw output, then literal assignment into the dictionary. There is no LLM-in-the-write-path. The system is *fully agnostic* to what the LLM "meant"; it only cares about the syntactic shape of the output. **Implication for our Flow OS write path:** any time we let an LLM distil before writing, we are doing strictly more than Schuurmans needs to do for *Turing universality*. Distillation is a comfort, not a requirement. The minimum viable write-path is regex over deterministic decoding. [ENGRAM: E]

**For ENGRAM Network (N).** The "shape of memory" here is a single flat key→value dictionary. Not a graph, not a tree, not a vector store, not a polyglot stack. Crucially, this is enough for *universal* computation — so claims that "we need a graph" or "we need vectors" for capability reasons are theoretically falsifiable. Graphs/vectors buy *ergonomics, retrieval quality, and economy* — not capability. The dictionary's only special slot is `op`, the instruction register; control flow is just "assign a different string to `op`". **Implication:** before adding shape, ask what *retrieval/ergonomic* problem it solves — capability is already covered by flat-KV. [ENGRAM: N]

**For ENGRAM Retrieve (R).** Retrieval is by *exact key* (`MEMORY[label]`), with two layers of substitution: `%[x]` in LLM outputs (post-processing) and `@[x]` in LLM inputs (pre-processing, with bounded-depth nesting allowed for `@[@[i]]`-style indirection). This is hash-table lookup, not similarity search. The lesson: when the agent itself is constructing the keys, exact-match retrieval is sufficient and *more reliable* than semantic retrieval. Semantic retrieval is for cases where the *querier* doesn't know the exact key. **Implication:** Flow OS should keep hybrid search (BM25 + vector) for human-authored queries but consider a pure-KV path for agent-internal scratchpad / state. [ENGRAM: R]

**For ENGRAM Aggregate (A).** Aggregation here is *zero-LLM* and *zero-loss*: outputs are parsed back into the dictionary verbatim. No "consolidation" step rewrites memories. This is the cleanest possible answer to the contradiction-and-drift problem: if you never compress or rewrite, you can never silently corrupt. **Implication:** consolidation is an *optimisation* (for space and recall ergonomics), never a *correctness* requirement. Any consolidation pipeline that destroys originals should be treated as lossy compression with a quality budget. [ENGRAM: A, G]

**For ENGRAM Ground (G).** Provenance is trivial because writes are mechanical regex extractions — every memory entry traces back to a specific (instruction, input) pair that produced it. There is no "the LLM concluded that…" gap to audit. **Implication for memory-architect work:** the cheapest path to perfect provenance is to *not* have the LLM be the writer. Have it be the producer of *strings that get parsed*. [ENGRAM: G]

**Cross-dimensional interaction.** Schuurmans' construction makes the *Maintain* dimension (M) almost trivially solved — there is nothing to maintain, because there is no consolidation, no eviction, no compaction. The price paid: the burden moves to *prompt engineering reliability*. The system only works because the 29 enumerated prompts produce correct outputs deterministically. **This is the trade we need to surface explicitly in Flow OS:** every time we add encoding/aggregation logic to ease ongoing maintenance, we are paying for it in correctness and provenance complexity elsewhere. [ENGRAM: E × M, A × M]

**For agentic OS framings (MemGPT, ChatDB, MemLLM lineage).** Schuurmans is the *theoretical floor* under all "LLM as OS" papers. Those papers add policies, paged memory, schemas, tool calls — but the universality result already holds with a flat dict and regex glue. The 2023 papers that came later (MemGPT, ChatDB, Ret-LLM) inherit a capability ceiling that is, formally, "Turing" — and their contribution is *ergonomics, retrieval quality, and reliability under real workloads*, not capability expansion. Calling them "memory architectures" is correct; calling them "the thing that makes LLMs powerful" overstates what they add to Schuurmans. [ENGRAM: meta]

## How to Apply It (method)

The full construction in operational terms:

1. **State.** A single global `MEMORY: dict[str, str|int]` with one reserved key, `op`, that holds the next prompt string ("instruction register"). A `BLANK` symbol (the string `'0'`) and a head-position integer at key `'i'`.

2. **Post-processor (LLM output → memory).** Three regex parsers run in sequence on the LLM's output string:
   - `substitute(string, '%')` — replaces `%[x]` with `MEMORY[x]` (single pass).
   - `assignments(string)` — matches `(?s)((?:\w|-)+)\s*=\s*"((?:.*\n)|(?:[^"]*))"` and applies `MEMORY[label] = value`.
   - `updates(suffix)` — matches `(\w+)\s*((?:\+|-)=)\s*(\d+)` and applies integer in/decrements.

3. **Pre-processor (memory → LLM input).** `substitute_nested(string, '@')` repeatedly replaces `@[x]` with `MEMORY[x]` until no more matches — *bounded to depth 2* so the parser stays finite-state. This is what lets `@[@[i]]` read "the value at the address stored in `i`" (i.e. the tape symbol under the head).

4. **Main loop (the entire OS).**
   ```python
   while True:
       op = MEMORY['op']
       if op == 'halt': return
       prompt = substitute_nested(op, '@')
       result = call_llm_server(prompt)            # temperature 0
       result = substitute(result, '%')
       suffix = assignments(result)
       updates(suffix)
   ```

5. **Programming model.** A "prompt program" is a finite set of pre-designed strings A…O stored under keys `'A'`…`'O'`, each prefixed with `@[boot]` (a long demonstration block teaching the LLM the if-then conditional pattern). Each `X` string encodes one Turing-machine state's behaviour: write a symbol to `MEMORY[MEMORY['i']]`, in/decrement `i`, and assign the next state's key to `op`.

6. **The boot prompt is doing all the heavy in-context learning.** It contains worked examples of the conditional pattern for many (input-symbol, next-state) pairs. The state-specific instruction strings A…O are then *small* — they just specialise the boot pattern for the current state's transitions.

7. **Verification protocol (the whole "proof").** Run the language model with `temperature=0` on each of the 29 distinct `(state, symbol)` prompt strings the U15,2 simulation can ever generate. Print the output. If every output matches the expected result string exactly, fidelity is established by induction on compute cycles.

**Pattern to reuse:** for *any* finite-state-controlled task, you can lift a frozen LLM to "deterministic executor of arbitrary algorithm X" by (a) flattening X to a finite set of state-transition prompts, (b) verifying each one at T=0 against the frozen model, (c) wrapping the call in a regex+dict loop. The work is in the *enumeration*, not the model.

## Best Figure

![Figure 1 — Transition table for the universal Turing machine U15,2 (page 7)](figures/schuurmans-2023-memory-augmented-llms-universal-fig.png)

**Why it matters (memory-architect view).** This is the entire verifiable surface of the system. Every cell `(σ, q) → (σ', m, q')` corresponds to one prompt string `X` (e.g. state A's instruction) that the frozen LLM must produce a specific output for when pre-processed with the current tape symbol. Two rows × fifteen columns × two symbols = 30 cells, minus state F's symbol-independent collapse = **29 enumerable test cases**. That is the entire correctness budget of a universal computer. The figure crystallises the paper's deepest lesson: *capability is bounded by the size of the prompt program you can verify, not by memory or model scale*. When we evaluate Flow OS or any memory-augmented agent, the equivalent of this table is the right artefact to build — "what is the finite set of (state, input) prompt cases your agent needs to be reliable on?" — and reliability on that set is the actual capability ceiling.

## What Experts Overlook

1. **Most "memory" papers cite Schuurmans for credibility but rarely engage with what he actually proved.** The cited claim is usually "LLMs + memory are Turing complete", treated as a footnote justifying any RAG/agent system. The actual result is much more specific and much more useful: *finite-state glue + a dictionary suffice*, and the bottleneck is LLM reliability on an enumerable test set, not architectural sophistication. Every paper that adds vector stores, graphs, or schemas should justify why they need *more* than Schuurmans' minimum — most don't.

2. **The boot prompt is doing the real work, and the paper barely names it.** ~17 worked conditional examples teach the model the if-then evaluation pattern in-context. The "state instructions" A…O are tiny because they ride on the boot pattern. Architecturally, this is a *demonstration-prefix style* memory architecture hiding inside what looks like assembly code. The paper presents it as engineering convenience; it is actually the substrate that makes the construction work, and it is not portable across models (Schuurmans notes other LLMs failed even on the same prompts).

3. **`temperature=0` is not a detail — it is the contract.** Universality requires deterministic reproduction of the 29 outputs. Any sampling temperature > 0 breaks the equivalence, because a single wrong token on a single cycle corrupts memory permanently with no recovery mechanism. The "associative memory" has no checksumming, no consensus, no retry. Real-world memory-augmented systems running at non-zero temperature are *not* the system Schuurmans proved universal — they are a stochastic relaxation of it. The reliability question for production agents is exactly: "how do you maintain the deterministic-LLM property at scale?"

4. **The Discussion admits the model couldn't handle if-then-else, only if-then.** This forced the use of U15,2 instead of the smaller U6,4 (which needs three conditionals per state). This is a structural admission: *the construction works because the prompt program was reshaped to fit what the LLM can do reliably, not the other way around*. The pattern of "discover what the LLM does deterministically, then encode your algorithm in those primitives" is the actual transferable methodology — and it generalises far beyond Turing machines.

5. **The construction never writes to memory using LLM judgement.** All writes are regex matches. This is the polar opposite of how Flow OS, MemGPT, ChatDB, and most contemporary memory systems work (LLM extracts and decides what to store). Schuurmans' minimal architecture has *no risk of the LLM promoting prior inferences to confirmed facts* because the LLM is never the writer. Every system that puts an LLM on the write path is paying capability tax for ergonomics — and that's fine, but the trade should be named explicitly.

6. **"Universality" here is asymptotic, not practical.** The simulation runs at one LLM call per Turing-machine compute cycle. A non-trivial computation would mean *millions* of frozen-LLM calls at T=0. The result is foundational, not deployable. For Flow OS, the practical takeaway is: stop using "Turing complete" as a feature; instead, ask how many *useful, verifiable* (state, input) prompt cases you can compile and check.

## Extracted Prompts

The paper contains exactly **2 categories** of prompt template that drive a universal computer. Both are verbatim, designed for Flan-U-PaLM 540B at T=0; portability to other models is not guaranteed.

### 1. The boot prompt (demonstrates conditional-evaluation pattern)

Stored at `MEMORY['boot']`. Shape: ~17 worked examples of the pattern:
```
result = " op="%[X]" %[i]="<sym>" i±=1 "
if <cond> then result = " op="%[Y]" %[i]="<sym>" i±=1 "
$result
" op="%[Z]" %[i]="<sym>" i±=1 "
```
Each example shows the LLM what to output (the `$result` line) for both the false-condition branch and the true-condition branch. This is in-context demonstration learning posing as code.

### 2. The 15 state-instruction prompts (A through O)

Each is two lines plus the spliced boot. Template:
```
@[boot]result = " op="%[<next_if_0>]" %[i]="<sym_if_0>" i<dir>=1 "
if @[@[i]]==1 then result = " op="%[<next_if_1>]" %[i]="<sym_if_1>" i<dir>=1 "
$result
```
Example (state A): writes symbol 0 and goes to B if current tape symbol is 0; writes symbol 1 and stays in A if current symbol is 1.
```
A = """@[boot]result = " op="%[B]" %[i]="0" i+=1 "
if @[@[i]]==1 then result = " op="%[A]" %[i]="1" i+=1 "
$result
"""
```

**Reusable prompt pattern (for memory-architect work):** the (`@[boot]` demo block + 2-line state-specific specialisation) shape is a *prompt-program template* that generalises beyond Turing machines. Any finite-state task can be encoded by:
1. A boot prompt teaching the LLM the conditional/assignment primitives.
2. One short specialisation per state that imports the boot via splicing.
3. A `MEMORY['op']` instruction register holding the active state's name.

For Flow OS, this maps cleanly to: routine-specific boot prompts compiled once, lightweight per-step prompts, deterministic regex-only state updates.

## Citations

The full citation list (22 entries) is in the frontmatter `citations[]`. The most load-bearing for a memory-architect:

- **[Chung et al., 2022]** — Flan-U-PaLM 540B (the actual model used; instruction-tuned PaLM). The construction is brittle and only worked on this model among those tried.
- **[Neary and Woods, 2009] / [Neary, 2008]** — U15,2 is from here. The choice of U15,2 over the smaller U6,4 is consequential (if-then-else limitation).
- **[Pérez et al., 2019], [Bhattamishra et al., 2020], [Wei et al., 2022a]** — prior Turing-completeness results for Transformers; Schuurmans positions his as distinct: those modify weights, his uses frozen weights + external memory.
- **[Siegelmann and Sontag, 2019], [Weiss et al., 2018]** — RNN universality results, same lineage.
- **[Dohan et al., 2022]** — "language model cascades" framing for chained LLM calls; Schuurmans' work is the minimal-feedback-loop variant.
- **[Zhou et al., 2022]** — least-to-most prompting; cited as a sibling "expand the computational reach" approach.
- **[Wei et al., 2022b]** — chain-of-thought; cited similarly.
- **[Wolfram, 2002] / [Cook, 2004]** — Rule 110 universality; Schuurmans considered this earlier but dropped it (needs unbounded periodic init).
- **[von Neumann, 1945] / [Böhm, 1954] / [Booth & Britten, 1947]** — von Neumann architecture and early assembly languages; the analogy is explicit in the paper.

## Related Digests

- [[graves-2014-neural-turing-machines]] — Neural Turing Machines: the *learned* differentiable-memory ancestor of this work; Schuurmans is the *frozen, prompt-driven* counterpoint.
- [[hu-2023-chatdb-symbolic-memory]] — ChatDB: same family ("LLM + external symbolic store"), but Schuurmans proves the *theoretical floor* under all such designs.
- [[modarressi-2024-memllm]] — MemLLM: fine-tunes an LLM to use a read/write memory; explicitly extends what Schuurmans achieved with zero training.
- [[modarressi-2023-ret-llm]] — Ret-LLM: general read/write memory for LLMs; sibling architecture.
- [[packer-2023-memgpt-os]] — MemGPT: "LLMs as OS" — Schuurmans is the universality result that legitimises the OS framing.

## Reviewer Notes

**Overall hallucination severity: Clean.**

Cross-checked every load-bearing factual claim in this digest against the paper text:

- ✅ Model identity: "Flan-U-PaLM 540B" (paper §5, abstract). Correctly attributed to Chung et al., 2022.
- ✅ Universal Turing machine choice: U15,2 with 15 states and 2 tape symbols, Pareto-optimal smallest known (paper §3, citing Neary & Woods 2009 and Neary 2008).
- ✅ "29 (state, symbol) cases" — explicitly stated in paper §4 ("A similar verification succeeds for all 29 (state, symbol) cases") and reflected in 29 enumerated verification tests in §5.
- ✅ "Update in state F does not depend on input, so one fewer case than total" — paper §4 verbatim.
- ✅ "temperature for the language model is set to zero (pure greedy decoding)" — paper §5 verbatim.
- ✅ "construction relies solely on designing a form of stored instruction computer that can subsequently be programmed with a specific set of prompts" — paper abstract verbatim.
- ✅ "no modification of the language model weights" — paper abstract and §1.
- ✅ Regex post-processing: three functions `assignments`, `substitute`, `updates`. Code in §2.1–§2.2 confirmed verbatim.
- ✅ Main loop structure: matches paper §2.3 exactly.
- ✅ if-then vs if-then-else admission and U6,4 abandonment: paper §6 verbatim.
- ✅ Rule 110 / Cook 2004 abandonment: paper §6 verbatim.
- ✅ Distinction from Pérez 2019 / Bhattamishra 2020 / Wei 2022a (weight manipulation vs frozen-weights + memory): paper §6 verbatim.
- ✅ Author affiliation Google Brain & University of Alberta: paper title page.
- ✅ Bounded-depth nesting "depth bound 2" claim: paper §2.2 verbatim.
- ✅ Acknowledgments mention CIFAR Canada AI Research Chairs, NSERC, Amii: paper Acknowledgments §.

**ENGRAM tagging:** the mapping in this digest is interpretive (the paper doesn't use ENGRAM language; the framework is from the lens-holder's own 2026 meta-analysis). Tags are this reviewer's mapping, not Schuurmans' framing — flagged here as interpretive overlay rather than paper claim.

**One minor interpretive call:** the digest claims "the boot prompt is doing all the heavy in-context learning" and that A…O are small *because* they ride on the boot demonstrations. This is consistent with the paper's structure (boot is hundreds of lines; A…O are 3 lines each) and consistent with Discussion §6's note that "compactness seemed essential" — but the paper itself does not analytically separate the boot's contribution from the state instructions' contribution. Treat that point as a defensible interpretation, not a direct paper claim.

No corrections needed to the digest body. Ship as-is.
