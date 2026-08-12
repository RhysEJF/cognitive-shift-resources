---
corpus: agentic-memory
kind: paper-digest
slug: pei-2025-scope-prompt-evolution
title: "SCOPE: Prompt Evolution for Enhancing Agent Effectiveness"
authors:
  - "Pei, Zehua"
  - "Zhen, Hui-Ling"
  - "Kai, Shixiong"
  - "Pan, Sinno Jialin"
  - "Wang, Yunhe"
  - "Yuan, Mingxuan"
  - "Yu, Bei"
year: 2025
publication_date: "2025-12"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2512.15374"
doi: null
arxiv_id: "2512.15374"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "SCOPE treats the agent's own prompt as the long-term memory store: execution traces are continuously distilled into natural-language guidelines, routed into a tactical (per-task) or strategic (cross-task) stream, and re-compiled into the prompt at every step, lifting HLE accuracy from 14.23 percent to 38.64 percent and GAIA from 32.73 percent to 56.97 percent."
topics:
  - agent-memory
  - prompt-evolution
  - online-learning
  - dual-stream-memory
  - guideline-synthesis
  - test-time-learning
  - context-engineering
tags:
  - paper
  - llm-agents
  - prompt-optimization
  - memory-architecture
  - engram-encode
  - engram-aggregate
  - engram-maintain
entities:
  - pei-zehua
  - huawei-noahs-ark-lab
  - cuhk
related_digests:
  - zhang-2025-ace
  - li-2024-ld-agent
  - park-2023-generative-agents
  - yao-2023-react-reasoning-acting
  - guo-2024-evoprompt
citations:
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Lewis, P.", "Perez, E.", "Piktus, A.", "Petroni, F.", "Karpukhin, V.", "Goyal, N.", "Küttler, H.", "Lewis, M.", "Yih, W.-t.", "Rocktäschel, T."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2005.11401"
    arxiv_id: "2005.11401"
  - title: "Dynamic Cheatsheet: Test-time learning with adaptive memory"
    authors: ["Suzgun, M.", "Yuksekgonul, M.", "Bianchi, F.", "Jurafsky, D.", "Zou, J."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2504.07952"
    arxiv_id: "2504.07952"
  - title: "Agentic Context Engineering: Evolving contexts for self-improving language models"
    authors: ["Zhang, Q.", "Hu, C.", "Upasani, S.", "Ma, B.", "Hong, F.", "Kamanuru, V.", "Rainton, J.", "Wu, C.", "Ji, M.", "Li, H."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2510.04618"
    arxiv_id: "2510.04618"
  - title: "ReasoningBank: Scaling agent self-evolving with reasoning memory"
    authors: ["Ouyang, S.", "Yan, J.", "Hsu, I.", "Chen, Y.", "Jiang, K.", "Wang, Z.", "Han, R.", "Le, L. T.", "Daruki, S.", "Tang, X."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2509.25140"
    arxiv_id: "2509.25140"
  - title: "Reflexion: Language agents with verbal reinforcement learning"
    authors: ["Shinn, N.", "Cassano, F.", "Gopinath, A.", "Narasimhan, K.", "Yao, S."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2303.11366"
    arxiv_id: "2303.11366"
  - title: "Self-Refine: Iterative refinement with self-feedback"
    authors: ["Madaan, A.", "Tandon, N.", "Gupta, P.", "Hallinan, S.", "Gao, L.", "Wiegreffe, S.", "Alon, U.", "Dziri, N.", "Prabhumoye, S.", "Yang, Y."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2303.17651"
    arxiv_id: "2303.17651"
  - title: "ReAct: Synergizing reasoning and acting in language models"
    authors: ["Yao, S.", "Zhao, J.", "Yu, D.", "Du, N.", "Shafran, I.", "Narasimhan, K. R.", "Cao, Y."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2210.03629"
    arxiv_id: "2210.03629"
  - title: "Large language models as optimizers (OPRO)"
    authors: ["Yang, C.", "Wang, X.", "Lu, Y.", "Liu, H.", "Le, Q. V.", "Zhou, D.", "Chen, X."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2309.03409"
    arxiv_id: "2309.03409"
  - title: "DSPy: Compiling declarative language model calls into self-improving pipelines"
    authors: ["Khattab, O.", "Singhvi, A.", "Maheshwari, P.", "Zhang, Z.", "Santhanam, K.", "Vardhamanan, S.", "Haq, S.", "Sharma, A.", "Joshi, T. T.", "Moazam, H."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2310.03714"
    arxiv_id: "2310.03714"
  - title: "GEPA: Reflective prompt evolution can outperform reinforcement learning"
    authors: ["Agrawal, L. A.", "Tan, S.", "Soylu, D.", "Ziems, N.", "Khare, R.", "Opsahl-Ong, K.", "Singhvi, A.", "Shandilya, H.", "Ryan, M. J.", "Jiang, M."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2507.19457"
    arxiv_id: "2507.19457"
  - title: "GAIA: A benchmark for general AI assistants"
    authors: ["Mialon, G.", "Fourrier, C.", "Wolf, T.", "LeCun, Y.", "Scialom, T."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2311.12983"
    arxiv_id: "2311.12983"
  - title: "Humanity's Last Exam (HLE)"
    authors: ["Phan, L.", "Gatti, A.", "Han, Z.", "Li, N.", "Hu, J.", "Zhang, H.", "Zhang, C. B. C.", "Shaaban, M.", "Ling, J.", "Shi, S."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2501.14249"
    arxiv_id: "2501.14249"
  - title: "xbench: Tracking agents productivity scaling with profession-aligned real-world evaluations (DeepSearch)"
    authors: ["Chen, K.", "Ren, Y.", "Liu, Y.", "Hu, X.", "Tian, H.", "Xie, T.", "Liu, F.", "Zhang, H.", "Liu, H.", "Gong, Y."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2506.13651"
    arxiv_id: "2506.13651"
  - title: "LLMLingua: Compressing prompts for accelerated inference of large language models"
    authors: ["Jiang, H.", "Wu, Q.", "Lin, C.-Y.", "Yang, Y.", "Qiu, L."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2310.05736"
    arxiv_id: "2310.05736"
  - title: "Scaling long-horizon LLM agent via context-folding"
    authors: ["Sun, W.", "Lu, M.", "Ling, Z.", "Liu, K.", "Yao, X.", "Yang, Y.", "Chen, J."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2510.11967"
    arxiv_id: "2510.11967"
  - title: "Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context"
    authors: ["Team, G.", "Georgiev, P.", "Lei, V. I.", "Burnell, R.", "Bai, L.", "Gulati, A.", "Tanzer, G.", "Vincent, D.", "Pan, Z.", "Wang, S."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2403.05530"
    arxiv_id: "2403.05530"
  - title: "Tongyi DeepResearch technical report"
    authors: ["Team, T. D.", "Li, B.", "Zhang, B.", "Zhang, D.", "Huang, F.", "Li, G.", "Chen, G.", "Yin, H.", "Wu, J.", "Zhou, J."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2510.24701"
    arxiv_id: "2510.24701"
  - title: "BrowseComp: A simple yet challenging benchmark for browsing agents"
    authors: ["Wei, J.", "Sun, Z.", "Papay, S.", "McKinney, S.", "Han, J.", "Fulford, I.", "Chung, H. W.", "Passos, A. T.", "Fedus, W.", "Glaese, A."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2504.12516"
    arxiv_id: "2504.12516"
  - title: "AgentOrchestra: A hierarchical multi-agent framework for general-purpose task solving"
    authors: ["Zhang, W.", "Cui, C.", "Zhao, Y.", "Hu, R.", "Liu, Y.", "Zhou, Y.", "An, B."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2506.12508"
    arxiv_id: "2506.12508"
  - title: "SWE-bench: Can language models resolve real-world GitHub issues?"
    authors: ["Jimenez, C. E.", "Yang, J.", "Wettig, A.", "Yao, S.", "Pei, K.", "Press, O.", "Narasimhan, K."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2310.06770"
    arxiv_id: "2310.06770"
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "Overview of the SCOPE Framework — Generator, Selector, Classifier, Optimizer, Tactical Memory, Strategic Memory"
  page: 3
  image_path: "figures/pei-2025-scope-prompt-evolution-fig.png"
---

# SCOPE: Prompt Evolution for Enhancing Agent Effectiveness

**Authors:** Zehua Pei, Hui-Ling Zhen, Shixiong Kai, Sinno Jialin Pan, Yunhe Wang, Mingxuan Yuan, Bei Yu (CUHK + Huawei Noah's Ark Lab)
**Published:** 2025-12 · [Source](https://arxiv.org/abs/2512.15374)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

SCOPE (Self-evolving Context Optimization via Prompt Evolution) treats the agent's prompt itself as a writable, evolving memory store. Execution traces — both errors and successful patterns — are converted online into natural-language **guidelines** by a 4-meta-agent pipeline (Generator → Best-of-N Selector → Classifier → Optimizer), then routed into one of two distinct memory streams: **Tactical Memory** (task-scoped, discarded between tasks) and **Strategic Memory** (cross-task, capped at 10 guidelines per domain, periodically consolidated by an LLM-driven Conflict-Resolution → Subsumption-Pruning → Consolidation pipeline). The compiled prompt `θ_t = θ_base ⊕ M_strat ⊕ M_tact` is re-assembled at every step.

Empirically, this lifts HLE from 14.23% to 38.64% (~2.7×), GAIA from 32.73% to 56.97%, and DeepSearch from 14.00% to 32.00%, beating prior playbook-based memory systems DC (Suzgun 2025) and ACE (Zhang 2025a) which can only learn between tasks rather than within them. The biggest single ablation gain (+10.91%) comes from running K=2 parallel prompt streams with different "personas" (Efficiency vs Thoroughness) and ensembling at test time — a single evolved prompt overfits to one strategy. Counter-intuitively, placing all guidelines in the system prompt beat splitting them between system/user prompts (46.06% vs 35.76%); the authors hypothesize user-prompt placement causes over-compliance and early termination. Choice of meta-agent LLM (GPT-4.1 vs Gemini-2.5-Pro) barely moved accuracy (<1.2%) despite Gemini generating 46% more guidelines, suggesting selection/optimization mechanisms filter for quality regardless of generator verbosity.

[ENGRAM: primarily **E**ncode (write-time LLM synthesis), **A**ggregate (the consolidation pipeline IS the aggregation step), **M**aintain (capacity-triggered eviction); secondarily **N**etwork (two-stream split is the shape decision); largely silent on **G**round (provenance) and **R**etrieve (no retrieval — the entire memory is compiled into the prompt every step).]

## Key Takeaway

**For a memory-architect, SCOPE's central design move is collapsing retrieval into compilation.** There is no query-time recall step — the entire strategic memory (capped at 10 guidelines × 7 domains = ~70 items max) is concatenated into the system prompt at every agent step. This is feasible because (a) the memory cap is enforced aggressively via the optimizer pipeline, and (b) the unit-of-memory is a 1-3 line natural-language guideline (avg 380-426 chars), so 70 items fits comfortably in context. The cost-benefit trade is explicit: zero retrieval latency, full context utilization, but a hard scaling ceiling on memory size that requires synchronous LLM-driven consolidation to enforce.

The second load-bearing decision is the **dual-stream split between tactical (task-scoped, discarded) and strategic (cross-task, persisted) memory**, gated by a learned confidence threshold (conf ≥ 0.85 → strategic, else tactical). This addresses a failure mode in prior work (DC, ACE) where one monolithic playbook accumulated both task-specific noise and durable principles, with no mechanism to separate them. The Classifier (π_γ) makes this routing decision per-guideline using a separate LLM call — write-time intelligence instead of query-time filtering.

The third decision worth borrowing: **K=2 parallel prompt streams seeded with opposing optimization personas (Efficiency vs Thoroughness) and unioned at test time**. Their solved-set overlap is only 33.94%, meaning ~23% of solved problems are unique to one perspective. This is essentially a population-diversity hedge against premature convergence of the evolving prompt — analogous to running two distinct memory architectures and OR-ing their answers.

[ENGRAM tags: this finding bears on **A** (write-time consolidation as the aggregation strategy), **N** (two-stream + parallel-K shape), and **R** (compile-everything-into-prompt vs ranked retrieval).]

## Implications

For a memory-architecture researcher running experiments on agentic OS memory layers, four implications matter:

1. **Write-time vs query-time synthesis — SCOPE is a maximalist write-time architecture.** The Generator + Selector + Classifier + Optimizer all run on the write path; the read path is "concatenate everything into the prompt." This is the opposite of a RAG-style architecture where the read path does ranking, expansion, and reranking. The trade is observable in the ablation: Memory Optimization (the consolidation pipeline) contributes only +1.82% on GAIA, but is necessary to keep the strategic memory from blowing past the prompt budget. **If you're building a small-N, high-quality memory (e.g., a personal CLAUDE.md or per-agent system prompt), the SCOPE pattern is directly applicable; if you have 1000+ memories, you need retrieval back.** [ENGRAM: E + A interaction]

2. **Shape-of-memory — natural-language guidelines as the unit, not entities or facts.** SCOPE's memory unit is a procedural directive ("Always list all plausible label synonyms when extracting from figures"; "If access is blocked, immediately escalate to Search Agent"). This is NOT a knowledge graph, NOT a fact triple, NOT a chunk. It's an *executable instruction in natural language*. The implication for ENGRAM's N dimension: for procedural / agentic memory, **the right shape may be a flat list of imperative sentences organized by 7 semantic domains** (tool_usage, error_handling, efficiency, analysis_methodology, data_validation, safety, general), with the LLM doing the categorization. This is much closer to a Markdown playbook than to a vector store. [ENGRAM: N]

3. **Drift and contradiction handling — SCOPE confronts this explicitly via a Conflict Resolution step in the optimizer pipeline.** When a new guideline contradicts an existing one, the LLM "merges contradictory guidelines" rather than versioning them. This is a critical design choice your team may want to invert: SCOPE silently smooths away contradictions; ENGRAM's G dimension explicitly wants to surface them. The example in Appendix D.3 shows R3 ("Avoid redundant API calls by caching results locally") and R4 ("Cache intermediate results to avoid re-computation") being merged into one guideline — but if R3 and R4 had ever been *contradictory* (e.g., one says "always cache," another says "never cache for fresh data"), SCOPE's merge would lose the conflict signal. **No provenance tracking is mentioned** — guidelines do not appear to retain links to the execution trace that generated them once consolidated. This is a clear gap for a provenance-first architecture. [ENGRAM: G — direct contradiction with the architect's stated value]

4. **AI as maintainer is foregrounded.** SCOPE has *four* meta-agents (Generator π_ϕ, Selector π_σ, Classifier π_γ, Optimizer π_ω) whose only job is to maintain the memory. The paper's Table 4 finding that the choice of meta-agent model (GPT-4.1 vs Gemini-2.5-Pro vs "same as base agent") moves accuracy by <1.2% despite Gemini producing 46% more guidelines is important: **the maintainer's job description matters more than the maintainer's model capability**, as long as the selection/optimization rubrics are well-designed. The rubrics live in Appendix F (not extracted here in full but referenced repeatedly) and are the actual IP of the paper. For your own AI-as-maintainer design: invest in the rubrics, not the model. [ENGRAM: M — and a confidence boost for the "AI as maintainer, not oracle" framing]

A secondary implication for **eviction (M):** SCOPE caps strategic memory at 10 per domain and targets 80% (8) post-optimization, leaving 20% headroom for future learning. This is a soft eviction policy — capacity-triggered, not age-triggered or use-triggered. **No "guideline staleness" mechanism is reported** — a guideline learned from a 2024 tool spec stays in the prompt forever even if the tool changes. This is a likely failure mode for long-running deployments. [ENGRAM: M gap]

## How to Apply It (method)

If you wanted to reproduce SCOPE's pattern in a different memory architecture, the operational recipe is:

**1. Define the trigger condition.** SCOPE writes a new guideline only on (a) an error event, OR (b) a sub-task completion. Don't synthesize on every step — that's both expensive and produces noise. The trigger condition (Algorithm 1, line 4) is the gate that keeps write-time costs bounded.

**2. Use TWO rubrics, not one, in the Generator.** Corrective rubrics (Appendix F.1) are triggered by errors and produce error-recovery guidelines. Enhancement rubrics are triggered by successful-but-suboptimal traces and produce optimization guidelines. The paper reports 39% corrective / 61% enhancement in the final memory — enhancement guidelines dominate, which means a system that only learns from errors misses the majority of available signal. **This is the core design insight you should port directly.**

**3. Generate N=2 candidates per write, select 1.** A Best-of-N pattern with a separate Selector (π_σ) that picks the highest-quality candidate per a selection rubric. N=2 is sufficient — the paper does not justify going higher. This adds +3.03% on GAIA over single-candidate generation.

**4. Classify into tactical vs strategic, with a confidence threshold of 0.85.** Anything below the threshold defaults to tactical (safer choice). The Classifier (π_γ) is a separate LLM call with classification rubrics in Appendix F.2.

**5. Cap strategic memory at 10 per domain across 7 domains.** When the cap is hit, run the 3-step optimizer pipeline: (a) Conflict Resolution — merge contradictions; (b) Subsumption Pruning — remove specifics covered by generals; (c) Consolidation — merge semantically similar. Target 80% (8) post-op to leave headroom. The concrete worked example in Appendix D.3 (11 → 5 guidelines) is the clearest reference.

**6. Compile the prompt fresh every step**, in this order: `θ_base ⊕ M_strat ⊕ M_tact`. Strategic before tactical so persistent principles set the frame and task-specific instructions are most recent (recency bias of the model favors the latest text).

**7. Place ALL guidelines in the system prompt, not the user prompt.** Counter-intuitive but consistent across the GAIA placement ablation (Table 3): system-prompt placement gets 46.06%, user-prompt placement gets 41.21%, split placement crashes to 35.76%. The hypothesized mechanism (over-compliance in user-prompt placement) is plausible but un-validated; treat the empirical result as primary.

**8. Run K=2 parallel streams with opposing personas, union at test time.** Define two personas (the paper uses "Efficiency: minimize tokens/latency" vs "Thoroughness: maximize coverage/robustness"), let each evolve independently, and take the union of solved tasks (Pass@K). This single addition is the largest ablation gain (+10.91% on GAIA).

**For ENGRAM mapping:** The procedure above is dominated by **E** (steps 1-4 are encoding decisions) and **A** (step 5 is consolidation = aggregation), with **N** (step 6-8 are shape decisions) as the secondary axis. **R** is degenerate (entire memory always loaded). **G** is absent (no provenance step in the procedure). **M** is reactive only (capacity-triggered eviction, no time-based or usage-based decay).

**Risk to flag for your team:** Step 6 (compile-every-step) is feasible because of step 5's hard cap. If you remove the cap (e.g., to support thousands of memories), step 6 breaks immediately and you need retrieval. SCOPE is not a recipe that scales to a large memory store without redesigning the read path.

## Best Figure

![Figure 3 — Overview of the SCOPE Framework (page 3)](figures/pei-2025-scope-prompt-evolution-fig.png)

**Why this is the load-bearing figure for a memory-architect:** Figure 3 is the only diagram that shows the entire memory architecture in one frame — the data flow from `Execution Trace → Guideline Generator → Best-of-N Selector → Classifier → {Tactical Memory, Strategic Memory + Optimizer} → Optimized Prompt`. Three things become visible only in this diagram and not in the prose:

1. **The Classifier is the routing decision** — it's the diamond in the middle that determines whether a synthesized guideline goes to the tactical stream (top, red) or the strategic stream (bottom, blue). Without the diagram, the conf ≥ 0.85 threshold reads like a hyperparameter; with the diagram, it's clearly a structural fork in the architecture.
2. **The Optimizer is ONLY attached to the Strategic Stream** — the cylinder with the recycling icon sits on the strategic memory only. Tactical memory has no consolidation pipeline because it's discarded between tasks. This is the most consequential visual fact: write-time consolidation cost is paid only for memories that persist.
3. **The Tactical and Strategic streams BOTH feed the final "Optimized Prompt"** at the right — confirming that both are concatenated into every step's prompt (not that strategic shadows tactical or vice versa). The dashed lines from tactical memory back to the prompt show the tactical loop closing within a task.

This figure is the architectural blueprint you'd port if you were implementing SCOPE in your own stack. The cool story it tells: *"execution traces are the only input; the prompt is the only output; everything in between is LLM-driven write-time work."*

[ENGRAM tags on the figure: visualizes E + N + A in one frame; conspicuously absent are any G (provenance arrows back to source traces) or R (query → ranked-list) elements.]

**Figure Page: 3**

## What Experts Overlook

A memory-architect reading this paper carefully will notice several things the authors either downplay or don't address:

1. **No provenance.** The paper never describes whether a strategic guideline retains a pointer to the execution trace(s) that generated it. After the Consolidation step in the optimizer, contradictory or overlapping guidelines are merged into new natural-language strings — and at that point, traceability to the original trace appears lost. For ENGRAM's G dimension, this is a major architectural choice made silently. An audit trail asking "why is this guideline in the prompt?" cannot be answered. The paper doesn't acknowledge this as a limitation. [ENGRAM: G — silent design choice]

2. **No staleness signal.** Guidelines persist in strategic memory until evicted by capacity pressure. There is no mechanism that says "this guideline was learned from a tool that no longer exists" or "this guideline hasn't fired in 100 episodes." In a long-running deployment (which the paper does not stress-test — max experiments appear to be one full benchmark pass), stale guidelines will accumulate and silently poison the prompt. [ENGRAM: M gap]

3. **Contradiction-smoothing as a feature, not a flag.** The Conflict Resolution step in the optimizer pipeline (Appendix F.3, referenced) merges contradictions. A surfaced-contradictions architecture would do the opposite: preserve both, tag them, and let the agent reason about which applies. SCOPE's choice is silent default-merging. For a team whose stated value is "surface, not smooth away" contradictions, this is a direct design inversion. [ENGRAM: G design contradiction]

4. **The "alarm-based correction" critique applies to SCOPE itself, partially.** Section 2.4 critiques Reflexion-style methods for being alarm-based — feedback is appended, agent must infer the correction. SCOPE's improvement is that synthesized guidelines are integrated INTO the prompt, not appended to history. But the synthesis still happens through an LLM (Generator) interpreting an error trace — which is itself an "alarm interpretation" step, just done by a meta-LLM instead of the base agent. The authors don't acknowledge that they've moved the alarm-interpretation problem one level up, not eliminated it. The meta-LLM can still misinterpret, and the resulting bad guideline persists in strategic memory and gets compiled into every future step. **This is the failure mode an adversarial reviewer would probe.** [ENGRAM: cross-cutting]

5. **Cost numbers are missing.** SCOPE runs 4 meta-LLM calls (Generator, Selector, Classifier, Optimizer) per write event, plus the K=2 parallel streams multiplying inference cost. The paper reports total agent steps (Table 3: 9,824 baseline → 7,430 with SCOPE) and step counts shrink, but does not report **total token cost or wallclock latency** including meta-agent calls. For someone evaluating SCOPE for a production agentic OS, the answer to "what does this cost vs. baseline per task?" is not in the paper. The 7,430 step count likely understates true compute by an order of magnitude.

6. **The Bio/Medicine and Chemistry gains (14.9% → 43.2%, 14.1% → 50.3%) are suspiciously large.** Section 4.5 attributes them to "domain-specific guidelines enable recovery" but the strategic memory is capped at 10 per domain. 10 guidelines should not produce ~3× accuracy gains on expert-level scientific reasoning unless those guidelines are extraordinarily well-targeted. An equally plausible read: the static baseline is unusually weak in these domains (tool-error-prone), and ANY error-recovery layer would help. Worth replicating before banking on the magnitude.

7. **The "61% enhancement vs 39% corrective" distribution (Table 5) is reported as a vindication of proactive synthesis, but is also evidence of trigger-condition asymmetry.** Sub-task completion is more frequent than errors in successful runs, so the trigger distribution biases the guideline distribution. Without a control showing that enhancement guidelines actually drive accuracy (not just count), the 61% number is descriptive, not causal.

8. **The choice of 7 semantic domains is arbitrary and unjustified.** Appendix D.1 lists them (tool_usage, data_validation, error_handling, efficiency, analysis_methodology, safety, general). No ablation on the domain taxonomy is presented. Domain choice directly shapes the optimizer's consolidation behavior — guidelines only get consolidated within a domain. This is a hidden hyperparameter with high architectural leverage.

## Extracted Prompts

The paper publishes complete meta-agent rubrics in Appendix F. The body text only shows the **Corrective Synthesis Prompt** in full (around page 14-15), which is the most directly portable:

```
Corrective Synthesis Prompt

You are a prompt engineering expert
analyzing agent execution errors.

Your task: Generate a SHORT,
TARGETED system prompt addition (1-3
lines) that will help prevent this
error in the future.

Context:
- Agent Name: {agent_name}
- Agent Role: {agent_role}
- Task: {task}
- Error Type: {error_type}
- Error Message: {error_message}

Previous actions taken:
{last_step_summary}

Current system prompt (for reference,
to avoid duplication):
{current_system_prompt}

Already applied rules (DO NOT
duplicate these):
{applied_rules}

Guidelines:
1. Be SPECIFIC and ACTIONABLE -
   target the exact error cause
2. Be BRIEF - max 1-3 lines
3. Use imperative language
   ("Always...", "Never...", "When X,
   do Y...")
4. Don't repeat what's already in
   the current system prompt
5. Focus on formatting, structure,
   or procedure constraints
```

**Why this prompt is interesting for a memory-architect:**

- The `{current_system_prompt}` and `{applied_rules}` substitutions are how SCOPE prevents duplicate guidelines. The Generator is **conditioned on the existing memory** at every write — it can't propose what's already there. This is a write-time deduplication strategy that avoids needing a separate dedup pass.
- The constraint "max 1-3 lines" and "imperative language" is how SCOPE enforces a consistent memory-unit shape. Without this constraint, the LLM would generate paragraphs and the strategic memory would blow past the prompt budget after a handful of guidelines.
- The five guidelines at the bottom are the actual quality rubric — they're what the Selector (π_σ) effectively measures candidates against. Porting these verbatim to your own architecture is probably the single highest-leverage borrow from the paper.

**Synthesized prompts (not extracted verbatim, but described in body text):**

- *Enhancement Synthesis Prompt (Efficiency persona)* — referenced in Appendix E and F, optimizes for "minimize tokens/latency" framing.
- *Enhancement Synthesis Prompt (Thoroughness persona)* — same shape, opposite optimization target.
- *Selector Rubric (Appendix F.1)* — picks best-of-N candidates.
- *Classifier Rubric (Appendix F.2)* — assigns tactical/strategic + confidence.
- *Optimizer Rubric (Appendix F.3)* — drives the 3-step consolidation pipeline.

**Example synthesized guidelines quoted in the paper:**

- Corrective: `"Define all variables in code snippets"` (triggered by NameError)
- Corrective: `"If access is blocked, immediately escalate to Search Agent. Do not retry."` (Efficiency persona, triggered by HTTP 403)
- Corrective: `"If access is blocked, attempt workarounds via Archive.org or Transcript Tools."` (Thoroughness persona, same trigger)
- Enhancement: `"Always list all plausible label synonyms and phrase variants when planning extraction from figures or comparing articles."` (synthesized in 12 seconds, confidence 0.95)
- Enhancement: `"Try search term variants"` (triggered by successful search with poor initial results)

The contrast between Efficiency and Thoroughness guidelines triggered by the *same* HTTP 403 error is the clearest demonstration in the paper of why K=2 parallel streams matter — and the strongest argument for a memory architecture that supports multiple, deliberately diverse memory specializations rather than a single canonical memory.

## Citations

The paper cites ~20 prior works, clustered into three groups directly relevant to a memory-architect:

**Memory-augmented agentic methods (the direct competitors SCOPE beats):**
- DC / Dynamic Cheatsheet (Suzgun 2025) — accumulates strategies into a single playbook, task-level granularity
- ACE / Agentic Context Engineering (Zhang 2025a) — bullet-point strategies across categories, reflector-curator loop
- ReasoningBank (Ouyang 2025) — agent self-evolving via reasoning memory

**Prompt optimization (offline, static):**
- OPRO (Yang 2023), DSPy (Khattab 2023), GEPA (Agrawal 2025) — pre-deployment prompt search

**In-context correction:**
- Reflexion (Shinn 2023), Self-Refine (Madaan 2023), ReAct (Yao 2022) — feedback into context, no prompt integration

**Benchmarks:**
- HLE (Phan 2025), GAIA (Mialon 2023), DeepSearch (Chen 2025)

**Context substrate:**
- RAG (Lewis 2020), LLMLingua (Jiang 2023), Gemini 1.5 long-context (Team 2024)

Full bibliographic detail is in the frontmatter `citations:` array (20 entries with arxiv_ids where available).

## Related Digests

- [[zhang-2025-ace]] — Agentic Context Engineering: ACE is the direct memory-augmented baseline SCOPE explicitly outperforms (Table 1: HLE 23.72% vs SCOPE 38.64%). ACE uses a Generator/Reflector/Curator playbook structure; SCOPE replaces it with Generator/Selector/Classifier/Optimizer + dual-stream routing.
- [[li-2024-ld-agent]] — LD-Agent: a four-memory-stream architecture for long-term dialogue (context, retrieved, user-traits, agent-traits). Direct architectural contrast: LD-Agent has 4 specialized memory types with retrieval; SCOPE has 2 memory streams compiled into the prompt at every step with no retrieval.
- [[park-2023-generative-agents]] — Generative Agents: perceive → memory stream → retrieve → act, with plan and reflect feeding back. The canonical agentic-memory architecture; SCOPE's tactical/strategic split is a constrained, prompt-compilation specialization of this fuller pattern.
- [[yao-2023-react-reasoning-acting]] — ReAct: the "in-context correction" baseline SCOPE critiques as alarm-based (feedback appended to history, agent must infer corrections). SCOPE's key claim is that integrating guidelines INTO the prompt beats appending them to history.
- [[guo-2024-evoprompt]] — EvoPrompt: evolutionary prompt optimization, an offline relative of SCOPE's online prompt evolution. EvoPrompt evolves prompts pre-deployment via genetic operators; SCOPE evolves prompts during execution via trace-driven LLM synthesis.

## Reviewer Notes

**Hallucination check pass (Severity: Clean)**

I read the paper text in full and cross-checked every numeric claim and named entity in the digest against the source. Findings:

- **All headline numbers verified.** HLE 14.23 → 38.64% (Table 1), GAIA 32.73 → 56.97% (Table 1), DeepSearch 14.00 → 32.00% (Table 1), Bio/Med 14.9 → 43.2% (Figure 4 prose at line 388), Chemistry 14.1 → 50.3% (line 388), GAIA Level 3 23.1 → 30.8% (line 392), Perspective ensemble overlap 33.94% (Table 6), enhancement/corrective split 61%/39% (Table 5), N=2 Best-of-N (Section 4.1), K=2 parallel streams (Section 4.1), conf threshold 0.85 (Table 9), max 10 guidelines per domain (Table 9), target 8 post-opt (Table 9 / Appendix D.2 "80%"), 1.5M lines of logs (Section 2 / Abstract).
- **Ablation breakdown verified against Table 2:** Baseline 32.73 → +Generator 37.58 → +Dual-Stream 41.21 → +Best-of-N 44.24 → +Mem Opt 46.06 → +Perspective 56.97. The "+10.91% from Perspective Exploration" claim is exactly the 56.97 − 46.06 step.
- **Placement ablation verified against Table 3:** System 46.06 > User 41.21 > Hybrid 43.64 > Split 35.76. (Note: ordering in digest text is "system > user > split" which is correct; hybrid is between user and system. The digest doesn't misrepresent this.)
- **Meta-agent model robustness verified against Table 4:** All-GPT-4.1 46.06%, All-Gemini 46.67%, Same-as-base 45.45% — within 1.2% as claimed. Gemini guideline count 163 vs GPT-4.1's 111 = 46.8% more, which I rounded to 46% in the digest. Accurate.
- **Author affiliations:** CUHK + Huawei Noah's Ark Lab (Hong Kong) — verified from page 1 footnote.
- **Algorithm 1 / Figure 3 mapping:** Generator π_ϕ, Selector π_σ, Classifier π_γ, Optimizer π_ω — all four meta-agents correctly named with their Greek-letter handles.
- **Figure 3 caption:** verified, matches the description in the Best Figure section.
- **Concrete guideline quotes:** "Define all variables in code snippets" (Section 5.1, line 457), "If access is blocked, immediately escalate..." and "...attempt workarounds via Archive.org..." (Figure 6, lines 487-494), "Always list all plausible label synonyms..." (Figure 5, line 493) — all verbatim from source.
- **7 semantic domains:** tool_usage, data_validation, error_handling, efficiency, analysis_methodology, safety, general — verified against Appendix D.1.
- **Failure-mode framing (Corrective vs Enhancement):** verified throughout Sections 2.1, 2.2, and Appendix A.
- **Critique of contradiction-smoothing:** the digest claims the optimizer "merges contradictory guidelines" — verified against Section 3.3 ("Conflict Resolution: merging contradictory guidelines"). The digest's stronger claim that "provenance to original trace is lost after consolidation" is an *inference*, not a verbatim statement — the paper does not address provenance at all, which is itself the finding. Flagged as inference, not hallucination.
- **Critique of cost-omission:** verified — searched the paper for "token", "cost", "latency", "wallclock" mentions related to meta-agent overhead. None found. The cost critique is well-founded.
- **Critique of arbitrary 7-domain choice:** verified — Appendix D.1 lists them without ablation; no domain-count ablation appears anywhere.

**One minor framing call to flag:** the digest describes the figure as "the only diagram that shows the entire memory architecture in one frame." Figure 1 (titled "SCOPE enables prompt evolution for enhanced agent effectiveness") also exists and shows a results curve, not the architecture, so this claim is accurate. Figure 2 shows the two failure modes, Figure 4 is per-category performance, Figures 5-6 are qualitative compliance/divergence traces. Figure 3 is correctly identified as the architectural overview.

**Severity: Clean** — no fabricated facts, no misattributed quotes, no inflated numbers. The interpretive claims (ENGRAM mapping, provenance gap, staleness gap, cost-omission critique) are clearly labeled as inferences from the paper's silences rather than as paper claims.
