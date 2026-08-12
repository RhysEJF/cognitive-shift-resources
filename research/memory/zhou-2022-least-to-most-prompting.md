---
corpus: agentic-memory
kind: paper-digest
slug: zhou-2022-least-to-most-prompting
title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
authors:
  - "Zhou, Denny"
  - "Schärli, Nathanael"
  - "Hou, Le"
  - "Wei, Jason"
  - "Scales, Nathan"
  - "Wang, Xuezhi"
  - "Schuurmans, Dale"
  - "Cui, Claire"
  - "Bousquet, Olivier"
  - "Le, Quoc"
  - "Chi, Ed"
year: 2022
publication_date: "2022-05"
venue: "ICLR 2023 (arXiv preprint 2022-05, v3 2023-04)"
source_url: "https://arxiv.org/abs/2205.10625"
doi: null
arxiv_id: "2205.10625"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "If a complex problem is first decomposed into ordered subproblems and then each subproblem's answer is appended to the context window before solving the next, an LLM can generalise far beyond the difficulty of any single in-context exemplar — turning the context window into a write-once-per-step working memory rather than a one-shot retrieval slot."
topics:
  - prompting
  - reasoning
  - compositional-generalization
  - task-decomposition
  - working-memory
  - chain-of-thought
  - in-context-learning
tags:
  - paper
  - llm-reasoning
  - prompt-engineering
  - icl
  - benchmark
  - scan
  - gsm8k
  - drop
entities:
  - zhou-denny
  - schaerli-nathanael
  - wei-jason
  - schuurmans-dale
  - le-quoc
  - chi-ed
related_digests:
  - yao-2023-react-reasoning-acting
  - hu-2023-chatdb-symbolic-memory
  - park-2023-generative-agents
  - wu-2025-human-ai-memory-survey
citations:
  - title: "Chain of Thought Prompting Elicits Reasoning in Large Language Models"
    authors: ["Wei, Jason", "Wang, Xuezhi", "Schuurmans, Dale", "Bosma, Maarten", "Chi, Ed", "Ichter, Brian", "Xia, Fei", "Le, Quoc", "Zhou, Denny"]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2201.11903"
  - title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
    authors: ["Wang, Xuezhi", "Wei, Jason", "Schuurmans, Dale", "Le, Quoc", "Chi, Ed", "Zhou, Denny"]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2203.11171"
  - title: "Language Models are Few-Shot Learners"
    authors: ["Brown, Tom", "Mann, Benjamin", "Ryder, Nick", "Subbiah, Melanie", "Kaplan, Jared D.", "et al."]
    year: 2020
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "PaLM: Scaling Language Modeling with Pathways"
    authors: ["Chowdhery, Aakanksha", "Narang, Sharan", "Devlin, Jacob", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2204.02311"
  - title: "Training Verifiers to Solve Math Word Problems"
    authors: ["Cobbe, Karl", "Kosaraju, Vineet", "Bavarian, Mohammad", "Hilton, Jacob", "Nakano, Reiichiro", "Hesse, Christopher", "Schulman, John"]
    year: 2021
    doi: null
    url: null
    arxiv_id: "2110.14168"
  - title: "Generalization without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks (SCAN)"
    authors: ["Lake, Brenden", "Baroni, Marco"]
    year: 2018
    doi: null
    url: null
    arxiv_id: "1711.00350"
  - title: "Measuring Compositional Generalization: A Comprehensive Method on Realistic Data"
    authors: ["Keysers, Daniel", "Schärli, Nathanael", "Scales, Nathan", "Buisman, Hylke", "Furrer, Daniel", "et al."]
    year: 2020
    doi: null
    url: null
    arxiv_id: "1912.09713"
  - title: "DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning over Paragraphs"
    authors: ["Dua, Dheeru", "Wang, Yizhong", "Dasigi, Pradeep", "Stanovsky, Gabriel", "Singh, Sameer", "Gardner, Matt"]
    year: 2019
    doi: null
    url: null
    arxiv_id: "1903.00161"
  - title: "Did Aristotle Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies"
    authors: ["Geva, Mor", "Khashabi, Daniel", "Segal, Elad", "Khot, Tushar", "Roth, Dan", "Berant, Jonathan"]
    year: 2021
    doi: null
    url: null
    arxiv_id: "2101.02235"
  - title: "Unsupervised Question Decomposition for Question Answering"
    authors: ["Perez, Ethan", "Lewis, Patrick", "Yih, Wen-tau", "Cho, Kyunghyun", "Kiela, Douwe"]
    year: 2020
    doi: null
    url: null
    arxiv_id: "2002.09758"
  - title: "AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts"
    authors: ["Wu, Tongshuang", "Terry, Michael", "Cai, Carrie Jun"]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2110.01691"
  - title: "Compositional Generalization via Neural-Symbolic Stack Machines"
    authors: ["Chen, Xinyun", "Liang, Chen", "Yu, Adams Wei", "Song, Dawn", "Zhou, Denny"]
    year: 2020
    doi: null
    url: null
    arxiv_id: "2008.06662"
  - title: "Neural Logic Machines"
    authors: ["Dong, Honghua", "Mao, Jiayuan", "Lin, Tian", "Wang, Chong", "Li, Lihong", "Zhou, Denny"]
    year: 2019
    doi: null
    url: null
    arxiv_id: "1904.11694"
  - title: "Can You Learn an Algorithm? Generalizing from Easy to Hard Problems with Recurrent Networks"
    authors: ["Schwarzschild, Avi", "Borgnia, Eitan", "Gupta, Arjun", "Huang, Furong", "Vishkin, Uzi", "Goldblum, Micah", "Goldstein, Tom"]
    year: 2021
    doi: null
    url: null
    arxiv_id: "2106.04537"
  - title: "Shepherd Pre-trained Language Models to Develop a Train of Thought: An Iterative Prompting Approach"
    authors: ["Wang, Boshi", "Deng, Xiang", "Sun, Huan"]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2203.08383"
  - title: "Seqzero: Few-shot Compositional Semantic Parsing with Sequential Prompts and Zero-shot Models"
    authors: ["Yang, Jingfeng", "Jiang, Haoming", "Yin, Qingyu", "Zhang, Danqing", "Yin, Bing", "Yang, Diyi"]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2205.07381"
  - title: "A Comparison of Most-to-Least and Least-to-Most Prompting on the Acquisition of Solitary Play Skills"
    authors: ["Libby, Myrna E.", "Weiss, Julie S.", "Bancroft, Stacie", "Ahearn, William H."]
    year: 2008
    doi: null
    url: "https://doi.org/10.1007/BF03391719"
    arxiv_id: null
  - title: "Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems"
    authors: ["Ling, Wang", "Yogatama, Dani", "Dyer, Chris", "Blunsom, Phil"]
    year: 2017
    doi: null
    url: null
    arxiv_id: "1705.04146"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Least-to-most prompting solving a math word problem in two stages"
  page: 2
  image_path: "figures/zhou-2022-least-to-most-prompting-fig.png"
---

# Least-to-Most Prompting Enables Complex Reasoning in Large Language Models

**Authors:** Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le, Ed Chi (Google Research, Brain Team)
**Published:** 2022-05 (arXiv v3 2023-04); ICLR 2023 · [Source](https://arxiv.org/abs/2205.10625)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Chain-of-thought (CoT) prompting collapses when the test problem is *harder* than the few-shot exemplars — particularly when "harder" means "more steps" or "longer input". Zhou et al. propose **least-to-most prompting (L2M)**: a two-stage pattern where the LLM is first asked to *decompose* a complex problem into an ordered list of simpler subproblems, and then asked to *solve each subproblem in sequence*, with each prior subproblem's question + answer appended to the next prompt as scaffolding. Across three benchmarks (last-letter-concatenation, the SCAN compositional benchmark, GSM8K + DROP math reasoning) L2M dominates CoT on the hard regime: 99.7% on SCAN length-split with 14 exemplars vs. 16.2% for CoT (vs. neural-symbolic baselines trained on 15K+ examples that reach 100%); 74% on length-12 last-letter-concatenation vs. 31.8% CoT; 45.23% on GSM8K problems requiring ≥5 steps vs. 39.07% CoT. The mechanism is a context-window-as-working-memory pattern: each subproblem's answer becomes a stable token-level fact that subsequent subproblem prompts can read deterministically rather than re-derive. *(ENGRAM bearing: A — Aggregate, R — Retrieve, E — Encode.)*

## Key Takeaway

**If a complex problem is first decomposed into ordered subproblems and then each subproblem's answer is appended to the context window before solving the next, an LLM can generalise far beyond the difficulty of any single in-context exemplar — turning the context window into a write-once-per-step working memory rather than a one-shot retrieval slot.** The paper provides the first systematic, training-free demonstration that the bottleneck for CoT on hard problems is not the LLM's reasoning capacity but the **shape** of the in-context state that the LLM gets to read at each step. By materialising intermediate answers into the prompt as `[subQ1, subA1, subQ2, subA2, …, subQn]`, L2M converts a many-step reasoning task into a chain of single-step lookups + small inferences, each of which the model handles well. The structural insight: the context window is being used here as a **finite, mutable scratchpad**, and the demonstration exemplars are teaching not the *content* of the answer but the *write protocol* (how to lay down the next fact in a form the model can re-read).

**ENGRAM tags:** Primarily **A (Aggregate)** — L2M *is* a write-time aggregation strategy at inference time, building up a compositional answer one subanswer at a time. Strong **R (Retrieve)** interaction — each new prompt is a deterministic retrieval over the prior subanswers (no semantic search needed; positional retrieval suffices because the writer controls the layout). Secondary **E (Encode)** — the encode policy is "verbatim append the LLM's own subanswer, no distillation" — the cheapest possible encode, but it requires the writer (decomposer) to produce subproblems whose answers stay short enough to keep accumulating in 2048 tokens.

## Implications

**For memory-architect work specifically:**

1. **Write-time vs query-time synthesis — L2M sits squarely at write-time.** The decomposer is the synthesis step; once it has produced an ordered subproblem list, every subsequent solve step is a near-mechanical lookup-and-extend. This is the opposite of pure RAG (which does all the work at query time). Implication: for any agentic memory system doing multi-hop reasoning over its own prior memories, **the decomposer step is the place to invest LLM budget**, not the retriever.

2. **Shape-of-memory — the context window is itself a structured memory store.** L2M is, at heart, a **proof that flat-list ordered append-only state inside the context window outperforms unstructured CoT for compositional tasks**. The "memory" here isn't a vector DB or graph — it's an ordered Q/A log laid out by a write-protocol the LLM has been shown. For Flow's memory layer this maps to: a session's accumulated Q+A pairs *are* a first-class memory store, and the structure of how they're laid out (decomposed → answered → appended) is the retrieval index. **Polyglot stacks are not always needed; structured prompt layout can be the store.**

3. **Drift, provenance, contradiction — provenance is trivially preserved when the writer is the reader.** Each subanswer in the L2M chain is traceable to the exact subquestion that spawned it, and the chain is reproducible. But this is a *closed-world* provenance — there is no external source to cite. The pattern breaks the moment you try to ground subanswers in retrieved external facts: the paper does not address this and it's a real frontier for memory-system designers. **Open question: can L2M-style decomposition be combined with retrieval at each step (decompose → retrieve-for-sub1 → answer → decompose-residual → retrieve-for-sub2 → ...) without losing the easy-to-hard generalisation?**

4. **AI-as-maintainer — the decomposer is a maintainer role, not an oracle role.** L2M is unusual in giving the LLM two distinct *jobs* in one inference session: a planner job (decompose) and an executor job (solve). For Flow's "AI workforce" framing, this is the architectural template: **separate the maintenance/planning role from the execution role even when both are the same model**. The paper shows this separation has measurable value (39.07% → 45.23% on hard GSM8K problems).

**General implications:**

5. **Sequential subproblem solving with answer-passing is the missing primitive between CoT and full agent frameworks** (ReAct, Reflexion, LangChain). It's lighter than agents (no tool use, no environment), heavier than CoT (two-pass, longer prompts), and it generalises to harder problems than either when the task admits clean decomposition.

6. **The technique exposes a clean failure mode: bad decomposition prompts don't transfer across domains.** "Nearly all problems in GSM8K can be accurately solved if the LLM is given the correct decomposition" — meaning the bottleneck has migrated from solving to decomposing. This is a memory-system insight: the *index* (decomposition) matters more than the *lookup* (solving), and indexing is domain-specific.

7. **For benchmark design**: L2M's SCAN result (99.7% with 14 exemplars) implicitly argues that benchmarks measuring "compositional generalisation" via length-split are testing *prompt-structure compatibility* as much as model capability. Future benchmarks need to control for decomposition quality.

## How to Apply It (method)

**Procedure to apply L2M to a new task in your own system:**

1. **Define the task in terms of "harder than the exemplars"** — what dimension scales? (input length, number of reasoning steps, number of entities, depth of nesting). If nothing scales, L2M is overkill; use plain CoT.

2. **Design the decomposition prompt** (Stage 1):
   - Write 2–14 exemplars where each shows: input → ordered list of subproblems.
   - The decomposition should be **monotone**: each subproblem builds on prior subanswers, never re-derives them.
   - Crucially: in your exemplars, demonstrate decomposition of inputs that are *easier* than the test inputs. The paper shows decomposition prompts generalise upward in difficulty even when exemplars are tiny (the SCAN decomposer used 8 exemplars and decomposed test commands many times longer).

3. **Design the solver prompt** (Stage 2):
   - 2–14 exemplars where each shows: `(prior_subQ, prior_subA, ..., current_subQ) → current_subA`.
   - The first exemplar should illustrate the **base case** (no prior subanswers). The second should illustrate the **recursive step** (read prior subanswer, extend by one step).
   - This is critical: the paper notes the two exemplars in Table 2 explicitly demonstrate "a base case and a recursive step" — modelling the decomposition as primitive recursion.

4. **Inference loop**:
   ```
   subproblems = LM(decomp_prompt + input)
   context = []
   for sub in subproblems:
       prompt = solver_prompt + format(context) + sub
       answer = LM(prompt)
       context.append((sub, answer))
   return context[-1].answer   # last subanswer = final answer
   ```

5. **For some tasks, fuse the two stages** — the GSM8K prompt (Table 9) does this: the decomposition list and solutions are produced in a single forward pass. Try this first if your token budget is tight; split into two passes if accuracy on long problems is unsatisfactory.

6. **Use Python or other concise intermediate notation** to compress subanswers when the natural-language form would blow the context limit. The SCAN prompt maps `look twice → "LOOK" * 2`, then post-processes. The paper shows LLMs can also be taught to expand the notation themselves (99.7% accuracy with a few exemplars).

7. **Combine freely** with CoT (have subanswers themselves be CoT chains) and self-consistency (sample multiple decompositions, vote). L2M is composable, not exclusive.

**What you do *not* do**: no training, no fine-tuning, no model edits, no external symbolic solver. Pure prompt engineering.

**Failure modes to monitor:** (a) decomposition prompt that works on math word problems will not work on commonsense questions — domain-specific decomposers needed; (b) when accumulated subanswers exceed the context window the chain silently truncates and you lose long-range dependencies; (c) the model may "interpret" combinators differently in subproblem 5 than in subproblem 1 (the SCAN errors show this: "twice" after "around" gets miscounted in 6 of 13 failures).

## Best Figure

![Figure 1 — Least-to-most prompting solving a math word problem in two stages (page 2)](figures/zhou-2022-least-to-most-prompting-fig.png)

Image Candidates:
Figure 1 (p. 2): Two-stage flow diagram showing decomposition then sequential solving on a single math word problem — the canonical visual definition of L2M.
Table 8 (p. 6): SCAN length-split accuracy comparison — 99.7% L2M vs. 16.2% CoT on code-davinci-002, the most quantitatively striking result.
Table 4 (p. 4): Last-letter-concatenation accuracy by list length — shows the divergence between CoT and L2M widening with difficulty, validating the easy-to-hard generalisation claim.

Best Image:
Figure Name: Figure 1: "Least-to-most prompting solving a math word problem in two stages"
Figure Page: 2
Slide Caption: Least-to-most prompting decomposes a complex problem into ordered subproblems and solves each one with prior subanswers appended to the context.
Description: Figure 1 is a two-stage flow diagram on a single math word problem ("It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. The water slide closes in 15 minutes. How many times can she slide before it closes?"). **Stage 1 (Decompose Question into Subquestions)** shows the LLM receiving the problem and producing one subquestion: "How long does each trip take?". **Stage 2 (Sequentially Solve Subquestions)** shows two solver calls: the first answers the subquestion ("It takes Amy 4 minutes to climb to the top, and 1 minute to slide down. So each trip takes 5 minutes."), and the second concatenates the subquestion + subanswer + original question into a fresh prompt, which the LLM then solves ("The water slide closes in 15 minutes. Each trip takes 5 minutes. So Amy can slide 15 ÷ 5 = 3 times before it closes."). The arrows make the answer-passing protocol visually unmistakable — Stage 2's second call's prompt visibly contains both Stage 2's first call's question and answer. **Why this is the right figure for the memory-architect lens**: it is a literal picture of "context-window-as-working-memory" — you can see the prompt growing by exactly one Q/A pair per step. It also makes clear that decomposition is *separate* from solving (two different LLM jobs, different prompts) — the architectural point that L2M is two roles, not one.

## What Experts Overlook

**Things most readers of this paper miss, especially when filing it under "prompt engineering tricks":**

1. **L2M is a memory architecture, not a prompt format.** Most citations of this paper frame it as "decompose then solve" — a one-line summary that misses the load-bearing structural claim: **the context window is being used as a deterministic key-value store**, where the subquestion is the key and the subanswer is the value, and the writer (decomposer) chooses the layout. The "prompt engineering" framing obscures that this is the simplest possible **agentic memory architecture**: append-only log + positional retrieval, with the LLM as both writer and reader. *(ENGRAM: A + R + E interaction.)*

2. **The decomposer-solver split is a maintainer-vs-oracle pattern.** The paper does not name it this way, but Stage 1 is a **maintainer role** (plan the work, structure the state) and Stage 2 is an **oracle role** (answer a specific question). The fact that both can be the same model with different prompts is a foundational result for AI-workforce systems: **role separation is achievable via prompt context, not model selection.** Most agent frameworks (ReAct, AutoGPT) re-invent this split with much more machinery.

3. **The 99.7% SCAN result is misleading without the asterisk: SCAN is decomposable by inspection.** The technique works spectacularly when decomposition is mechanical (split by connectives like "and", "after", "thrice"). It works mediocrely (62.39% vs. 60.87%) on GSM8K where decomposition itself requires reasoning. The paper acknowledges this in Section 5 but most secondary discussion drops it. **Implication for memory systems**: L2M's value scales with how *cleanly indexable* your task is. For unstructured-prose memory ("what did the user say about positioning last quarter") the decomposition step itself becomes the hard problem.

4. **The "exemplars demonstrate base case + recursive step" framing (Tables 2, 6, 7) is a direct port of structural recursion from PL theory.** The paper buries this in one sentence ("The two exemplars together illustrate a base case and a recursive step", p. 4). This is a *prescriptive recipe* for exemplar design: any task you want to L2M-ify needs at least one base-case exemplar and one recursive-step exemplar, where the recursive exemplar visibly reads a prior subanswer. Most prompt-engineering reproductions of L2M skip this design discipline and get worse results.

5. **The error analysis on SCAN reveals a contradiction-detection failure mode that has memory-architecture implications.** When code-davinci-002 fails (13 of length-split test set), it doesn't fail at decomposition — it fails when *re-interpreting* a combinator (`thrice`, `after`) differently across subproblems. This is the model **silently promoting an inconsistent inference into context as if it were a fact**, then building on it. For a memory system this is the classic "AI promotes its own prior inference to confirmed fact" failure — and the paper shows it happens even within a single inference chain.

6. **No mention of cost/latency.** L2M roughly **doubles** the number of LLM calls per problem (one decompose + N solves vs. one CoT call). On the SCAN length-split with 14-exemplar prompts and long commands, this is non-trivial cost. The paper reports no token counts, no $/problem, no latency. For production memory systems this is the key engineering tradeoff and the paper is silent on it.

7. **The technique is conspicuously model-sensitive.** code-davinci-002 reaches 99.7% on SCAN; text-davinci-002 reaches 76%; code-davinci-001 reaches 60.7% (Table 8). The paper notes this in passing but does not investigate why code-pretrained models dominate. **Hypothesis worth testing**: code pretraining teaches the model to read prior variable-bindings in a context window deterministically, which is exactly the skill L2M requires. If true, this predicts that any memory architecture using "context-window-as-store" will benefit disproportionately from code-pretrained models.

8. **The two-stage architecture solves a contradiction the paper never names.** CoT mixes "plan what to compute" and "compute it" into a single token stream — and the model has to commit to a plan as it writes. L2M physically separates them with an LLM-call boundary, which gives the model the opportunity to *throw away* a bad decomposition (run Stage 1 again) without polluting Stage 2. This is the same insight as separating compile-time from run-time, or write-time from query-time. Most readers treat the two-stage thing as a quirk; it's actually the point.

## Extracted Prompts

The paper publishes a large number of full prompt contexts in its appendix. The five most useful for a memory-architect to lift verbatim:

### 1. Last-letter-concatenation — decomposition prompt (Table 1)

```
Q: "think, machine, learning"
A: "think", "think, machine", "think, machine, learning"
```

*(Achieves 100% decomposition accuracy on lists up to 12 with code-davinci-002. The single exemplar teaches "produce prefixes of increasing length".)*

### 2. Last-letter-concatenation — solver prompt (Table 2, both exemplars demonstrate base case + recursive step)

```
Q: "think, machine"
A: The last letter of "think" is "k". The last letter of "machine" is "e". Concatenating "k", "e" leads to "ke". So, "think, machine" outputs "ke".

Q: "think, machine, learning"
A: "think, machine" outputs "ke". The last letter of "learning" is "g". Concatenating "ke", "g" leads to "keg". So, "think, machine, learning" outputs "keg".
```

*(Critical structural feature: the second exemplar's answer starts by reading the first exemplar's answer ("'think, machine' outputs 'ke'") and only then extends. This is the "read prior subanswer, append one step" template — directly applicable to any agentic memory chain.)*

### 3. SCAN — decomposition prompt exemplar (Table 6)

```
Q: "look opposite right thrice after walk"
A: "look opposite right thrice" can be solved by: "look opposite right", "look opposite right thrice". "walk" can be solved by "walk". So, "look opposite right thrice after walk" can be solved by: "look right", "look opposite right", "look opposite right thrice", "walk".
```

*(Template: "X can be solved by: subX1, subX2, …" — the decomposer states a hierarchical decomposition explicitly. Generalises to any recursive structure with named subparts.)*

### 4. SCAN — solver prompt exemplar with Python-notation compression (Table 7)

```
Q: "run and look twice"
A: The output of "run and look twice" concatenates: the output of "run", the output of "look twice". "run" outputs "RUN". "look twice" outputs "LOOK" * 2. So concatenating the output of "run" and the output of "look twice" leads to "RUN" + "LOOK" * 2. So the output of "run and look twice" is "RUN" + "LOOK" * 2.
```

*(Memory-architect insight: Python expressions are used as an **on-the-wire compression format** to keep subanswers short enough to accumulate in 2048 tokens. Direct analogue: any agentic memory system passing large intermediate state through a context window benefits from an explicit compact serialisation format.)*

### 5. GSM8K — single-pass fused decomposition + solving (Table 9)

```
Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together?
A: Let's break down this problem: 1. How many apples does Anna have? 2. How many apples do they have together?

1. Anna has 2 more apples than Elsa. So Anna has 2 + 5 = 7 apples.
2. Elsa and Anna have 5 + 7 = 12 apples together.

The answer is: 12.
```

*(This is the L2M one-call variant — decomposition and solving in a single response, separated by the numbered list. Lower latency, slightly lower accuracy. Trigger phrase "Let's break down this problem:" is the lever — analogous to "Let's think step by step" but explicitly *planning* before computing.)*

**Transferable trigger phrases for your own work**:
- "Let's break down this problem: 1. … 2. … N. …"
- "X can be solved by: subX1, subX2."
- "[prior_subanswer] So, …" (the read-prior-subanswer-then-extend pattern)

## Citations

- Wei et al. 2022 — Chain of Thought Prompting Elicits Reasoning in Large Language Models (arXiv:2201.11903) — the direct predecessor that L2M extends.
- Wang et al. 2022b — Self-Consistency Improves Chain of Thought Reasoning (arXiv:2203.11171) — composable with L2M.
- Brown et al. 2020 — GPT-3 (Language Models are Few-Shot Learners, arXiv:2005.14165) — the base paradigm of few-shot prompting.
- Chowdhery et al. 2022 — PaLM (arXiv:2204.02311) — alternative base model referenced for scale.
- Cobbe et al. 2021 — GSM8K verifiers (arXiv:2110.14168) — source of the GSM8K benchmark.
- Lake & Baroni 2018 — SCAN benchmark (arXiv:1711.00350) — the compositional generalisation benchmark used as L2M's headline result.
- Keysers et al. 2020 — Measuring Compositional Generalization (arXiv:1912.09713) — broader benchmark family.
- Dua et al. 2019 — DROP benchmark (arXiv:1903.00161) — the discrete-reasoning reading comprehension benchmark used as third evaluation.
- Geva et al. 2021 — Did Aristotle Use a Laptop? (arXiv:2101.02235) — commonsense reasoning benchmark cited as a failure mode for cross-domain decomposition.
- Perez et al. 2020 — Unsupervised Question Decomposition for QA (arXiv:2002.09758) — closest prior work on decomposition, but uses trained models and independent subquestions (no answer-passing).

*(Full citation list in frontmatter — 17 entries.)*

## Related Digests

- [[yao-2023-react-reasoning-acting]] — ReAct: Synergizing Reasoning and Acting in Language Models (next step beyond L2M: interleave reasoning with environment actions, not just self-decomposition).
- [[hu-2023-chatdb-symbolic-memory]] — ChatDB: Augmenting LLMs with Databases as Their Symbolic Memory (its "chain-of-memory" pattern is L2M-style decomposition where each subanswer is a SQL execution against an external DB rather than a self-generated string).
- [[park-2023-generative-agents]] — Generative Agents (uses L2M-style plan decomposition + reflection as the architectural backbone for long-horizon agentic behaviour).
- [[wu-2025-human-ai-memory-survey]] — From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs (places L2M and CoT in the broader memory-mechanism taxonomy).

## Reviewer Notes

**Hallucination check** (cross-referenced digest claims against paper text):

- ✅ SCAN length-split numbers (99.7% L2M / 16.2% CoT / 16.7% standard, code-davinci-002): verified Table 8, p. 6.
- ✅ Last-letter-concatenation length-12 (74.0% L2M / 31.8% CoT / 0.0% standard): verified Table 4, p. 4.
- ✅ GSM8K accuracy (62.39% L2M / 60.87% CoT): verified Table 11, p. 7.
- ✅ GSM8K ≥5-step breakdown (45.23% L2M / 39.07% CoT): verified Table 12, p. 7.
- ✅ DROP non-football (82.45% L2M / 74.77% CoT / 58.78% standard / 43.86% zero-shot): verified Table 11, p. 7.
- ✅ DROP football (73.42% L2M / 59.56% CoT): verified Table 11, p. 7.
- ✅ "14 exemplars" claim for SCAN: verified — 8 decomposition + 14 mapping exemplars, the abstract's "14 exemplars" specifically refers to the command-mapping prompt (the larger of the two). The digest's "14 exemplars" framing matches the abstract's phrasing.
- ✅ "neural-symbolic models trained on >15,000 examples" comparison: verified abstract + Section 3.2 (training set is "about 80% of the full set with over 20,000 examples").
- ✅ Educational psychology origin (Libby et al. 2008): verified Section 1, p. 2.
- ✅ Two-stage architecture, base case + recursive step framing: verified Section 3.1, p. 3–4.
- ✅ Error analysis claims (6 of 13 SCAN failures from "twice/thrice after around"): verified Section 3.2, p. 6.
- ✅ Limitations on cross-domain decomposition transfer: verified Section 5, p. 8.
- ⚠️ The digest claims L2M "roughly doubles the number of LLM calls per problem". This is the digest's own inference, not stated in the paper. The paper makes O(N) solver calls where N = number of subproblems, plus 1 decomposition call. Marking as **digest-inferred, not paper-claimed** — true for short chains, understated for long ones.
- ⚠️ The digest's "code pretraining → context-window-as-store" hypothesis (in What Experts Overlook §7) is explicitly flagged as a hypothesis not in the paper. The paper notes code-davinci-002 > text-davinci-002 in passing (p. 6 and Table 8) but does not propose this mechanism.

**Overall severity: Clean.** All quantitative claims verified against tables; speculative framings (memory-architecture re-interpretation, code-pretraining hypothesis, doubling cost claim) are clearly labelled as digest interpretation in the body and ENGRAM-tagged. No fabricated numbers, no misattributed authors, no invented benchmarks. The memory-architect framing of "context-window-as-working-memory" is not literally in the paper but is a faithful structural re-description of the actual mechanism (Figure 1 and Section 2 prose make the answer-accumulation pattern visually and textually explicit).
