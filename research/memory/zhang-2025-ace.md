---
corpus: agentic-memory
kind: paper-digest
slug: zhang-2025-ace
title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
authors:
  - "Qizheng Zhang"
  - "Changran Hu"
  - "Shubhangi Upasani"
  - "Boyuan Ma"
  - "Fenglu Hong"
  - "Vamsidhar Kamanuru"
  - "Jay Rainton"
  - "Chen Wu"
  - "Mengmeng Ji"
  - "Hanchen Li"
  - "Urmish Thakker"
  - "James Zou"
  - "Kunle Olukotun"
year: 2025
publication_date: "2025-10"
venue: "ICLR 2026"
source_url: "https://arxiv.org/abs/2510.04618"
doi: null
arxiv_id: "2510.04618"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "ACE refuses the brevity-bias / context-collapse failure mode of prior context optimizers (GEPA, MIPROv2, Dynamic Cheatsheet, Reflexion) by representing the agent's evolving context as a structured itemized playbook of bullets (each with a unique ID and helpful/harmful counters) updated via three specialised LLM roles — Generator (produces reasoning trajectories), Reflector (distills insights from successes and failures), Curator (integrates insights as compact delta entries merged by lightweight non-LLM logic) — plus a grow-and-refine de-duplication pass; the architecture lifts AppWorld agent accuracy by up to 17.1% over baselines, beats the IBM-CUGA GPT-4.1 production agent leaderboard winner using only open-source DeepSeek-V3.1, cuts adaptation latency by 86.9% on average, and works without labeled supervision — using execution feedback alone as the learning signal."
topics:
  - context-engineering
  - context-adaptation
  - self-improving-agents
  - playbook-memory
  - delta-updates
  - grow-and-refine
  - generator-reflector-curator
  - context-collapse
  - brevity-bias
  - appworld
  - finer
  - formula
  - bird-sql
  - ddxplus
  - in-context-learning
  - dynamic-cheatsheet
  - gepa
  - mipro
  - reflexion
  - agentic-memory
  - online-context-adaptation
tags:
  - paper
  - context-engineering
  - agentic-memory
  - ace
  - playbook
  - delta-update
  - grow-and-refine
  - iclr-2026
  - appworld
  - stanford
  - sambanova
  - berkeley
  - self-improving
entities:
  - zhang-qizheng
  - hu-changran
  - zou-james
  - olukotun-kunle
  - stanford
  - sambanova
  - uc-berkeley
related_digests:
  - latimer-2025-hindsight-memory
  - wang-2025-mirix
  - liu-2025-memverse
  - kang-2025-memory-os
  - du-2025-rethinking-memory
  - xu-2025-a-mem-agentic-memory
citations:
  - title: "Many-Shot In-Context Learning (ICL)"
    authors: ["Rishabh Agarwal", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "GEPA: Genetic-Pareto Prompt Optimization via Reflective Prompt Evolution"
    authors: ["Lakshya A. Agrawal", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
    authors: ["Akari Asai", "Zeqiu Wu", "Yizhong Wang", "Avirup Sil", "Hannaneh Hajishirzi"]
    year: 2024
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving Language Models by Retrieving from Trillions of Tokens (RETRO)"
    authors: ["Sebastian Borgeaud", "Arthur Mensch", "Jordan Hoffmann", "et al."]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents"
    authors: ["Harsh Trivedi", "et al."]
    year: 2024
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    authors: ["Noah Shinn", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory"
    authors: ["Mirac Suzgun", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "A-MEM: Agentic Memory for LLM Agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "Hang Gao", "Juntao Tan", "Yongfeng Zhang"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.12110"
  - title: "TextGrad: Automatic Differentiation via Text"
    authors: ["Mert Yuksekgonul", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "MIPROv2: Optimizing Multi-Stage Language Model Programs"
    authors: ["Krista Opsahl-Ong", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Chain-of-Thought Prompting Elicits Reasoning in LLMs"
    authors: ["Jason Wei", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    authors: ["Shunyu Yao", "Jeffrey Zhao", "Dian Yu", "Nan Du", "Izhak Shafran", "Karthik Narasimhan", "Yuan Cao"]
    year: 2023
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG)"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2005.11401"
  - title: "FiNER: Financial Numeric Entity Recognition for XBRL Tagging"
    authors: ["Lefteris Loukas", "et al."]
    year: 2022
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Decomposed Prompting: A Modular Approach for Solving Complex Tasks"
    authors: ["Tushar Khot", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Dynamic Cheatsheet (earlier version)"
    authors: ["Krause", "et al."]
    year: 2019
    venue: "n/a"
    doi: null
    url: null
    arxiv_id: null
  - title: "BIRD-SQL: Big Bench for Large-Scale Database Grounded Text-to-SQL Evaluation"
    authors: ["Jinyang Li", "et al."]
    year: 2023
    venue: "NeurIPS Datasets and Benchmarks"
    doi: null
    url: null
    arxiv_id: null
  - title: "DDXPlus: A Large-Scale Diagnostic Dataset for Medical Decision Making"
    authors: ["Arsene Fansi Tchango", "et al."]
    year: 2022
    venue: "NeurIPS Datasets and Benchmarks"
    doi: null
    url: null
    arxiv_id: null
  - title: "StreamBench: Towards Benchmarking Continuous Improvement of Language Agents"
    authors: ["Cheng-Kuang Wu", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "IBM-CUGA: Multi-Agent System for AppWorld Leaderboard"
    authors: ["Asaf Marreed", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Formula: A Financial Numerical Reasoning Benchmark"
    authors: ["Wang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "The Shift to Saturating Contexts (long-context paradigm)"
    authors: ["Jiang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 4
  title: "The ACE Framework: Generator → Reflector → Curator pipeline with delta context items merged back into the playbook"
  page: 5
  image_path: "figures/zhang-2025-ace-fig.png"
---

# Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

**Authors:** Qizheng Zhang* (Stanford, qizhengz@stanford.edu), Changran Hu* (SambaNova/Berkeley, changran_hu@berkeley.edu) — equal contribution; Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Urmish Thakker (SambaNova Systems); Hanchen Li (UC Berkeley); James Zou (Stanford); Kunle Olukotun (Stanford, kunle@stanford.edu)
**Published:** 2025-10 (v3 29 Mar 2026) · **Venue:** ICLR 2026 · [Source](https://arxiv.org/abs/2510.04618) · [Site](https://ace-agent.github.io) · [Code](https://github.com/ace-agent/ace)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

ACE (Stanford + SambaNova + Berkeley, Oct 2025, ICLR 2026) attacks a specific pathology in agentic-memory + context-optimization systems: monolithic LLM rewriting of the accumulated context causes **context collapse** — a documented failure mode where, e.g., at step 60 the AppWorld context contained 18,282 tokens and scored 66.7% accuracy, then at step 61 it collapsed to 122 tokens and scored 57.1% (below the 63.7% no-context baseline). The complementary failure is **brevity bias** — prompt optimizers like GEPA reward concise summaries, sacrificing the domain-specific heuristics and failure modes the system actually needs. ACE's prescription: represent the context as a structured itemized playbook of bullets (each bullet = `{id, helpful_count, harmful_count, content}` where content is a reusable strategy / domain concept / failure mode), and update it via three specialised LLM roles inspired by human learning. **Generator** produces reasoning trajectories for new queries, highlighting which bullets were useful or misleading. **Reflector** distills concrete insights from successes and errors in the trajectories, optionally refining across multiple iterations. **Curator** integrates these insights as compact delta entries which are then merged into the playbook by **deterministic non-LLM logic** (this last point is load-bearing — taking the LLM out of the merge step is what prevents context collapse). Two architectural pillars: **(1) incremental delta updates** — never regenerate the playbook in full; produce small candidate-bullet deltas distilled by the Reflector; merge localised; allows parallel batched updates; **(2) grow-and-refine** — append new-ID bullets; update existing-ID bullets in place (e.g., increment counters); periodically de-duplicate via semantic embedding similarity (proactive after each delta or lazy on context overflow). Empirically: **+10.6% on agents and +8.6% on finance** average gains across both offline (system prompt optimization) and online (test-time memory adaptation) settings; on **AppWorld** specifically up to +17.1% over baselines; **matches IBM-CUGA (GPT-4.1, leaderboard #1) overall and surpasses it on test-challenge** using only open-source DeepSeek-V3.1; **86.9% lower adaptation latency** than existing adaptive methods; works **without labeled supervision** — execution feedback alone is enough. Code released at github.com/ace-agent/ace. **Most useful takeaway:** the **role-separation** (Generator / Reflector / Curator) + **structured bullets with counters** + **non-LLM merge** is the recipe that turns "evolving context" from a vague aspiration into a deployable system. The merge step being deterministic is what makes it reliable; the bullet metadata is what makes it explainable; the role separation is what makes it scalable.

## Key Takeaway

The agentic-memory papers in the wiki so far (Hindsight, MIRIX, MemVerse, MemoryOS, A-Mem) all focus on *what kind of memory store* to build. ACE asks the orthogonal question: *given any memory store, how should it evolve over time without degrading?* Two specific pathologies dominate naive context evolution: **context collapse** (the LLM that rewrites the context periodically collapses it to a tiny summary) and **brevity bias** (the optimizer reward function pushes toward short generic prompts). ACE's three-role pipeline is a *protocol for safe context evolution*: the Generator surfaces what worked / what failed without writing to context; the Reflector extracts insights without writing to context; the Curator emits *small structured deltas* (not full rewrites) that are merged by *non-LLM code* (not by the LLM that could collapse the context). Stated as a lesson: **when an LLM is allowed to fully rewrite a long context, it will eventually collapse it — the architectural defense is to remove the LLM from the merge step entirely and force it to emit only structured deltas the deterministic merger can apply.** This is one of those design rules that becomes obvious in retrospect but isn't obvious until you've seen the failure mode plotted (Figure 2: 18,282 tokens → 122 tokens in one step, 66.7% → 57.1% accuracy).

## Implications

- **Never let an LLM monolithically rewrite an evolving context.** The 18,282 → 122 token collapse in Figure 2 is the single most useful diagnostic in the paper. The lesson generalises far beyond context engineering — any system where an LLM is repeatedly asked to "update" a persistent representation by full rewrite will eventually collapse it. The fix: force the LLM to emit *deltas* (structured changes) that a deterministic merger applies. For Flow OS's `/learn` and the future MTM segment-summary refresh, this means: don't ask the LLM "rewrite this segment summary including the new page"; ask it "emit JSON deltas (add bullet X, increment counter Y, remove bullet Z)" and apply the deltas with Python code. `[A, M]`

- **Adopt the three-role pipeline (Generator / Reflector / Curator) as a general agent-memory protocol.** ACE's role separation generalises beyond context engineering — it's a recipe for any system where an agent acts (Generator), reflects on outcomes (Reflector), and updates persistent state (Curator). For Flow OS: `/work` is the Generator, `/learn` is the Reflector + Curator (currently conflated). Split them — `/learn` should first run the Reflector pass (extract insights from session execution traces, mark which prior memory bullets were helpful/harmful) and then the Curator pass (emit structured deltas, apply via deterministic merger). This division of labour avoids the "one prompt to do everything" failure that GEPA/DC fall into. `[A, N]`

- **Bullets-with-metadata (helpful_count, harmful_count, ID) is the right unit, not free-text summaries.** Each ACE bullet is `{id, helpful_count, harmful_count, content}`. The counters provide a *self-correcting feedback signal* — bullets repeatedly flagged as harmful get pruned by grow-and-refine; bullets repeatedly flagged as helpful get retained even when the merger considers dropping them. The unique ID lets the Curator emit precise update ops (`update bullet 47: increment helpful_count`) rather than fuzzy edits. For Flow OS, this is the right unit for a `decision-memory` or `pattern-memory` file — not free-text bullet points, but structured items the system can update individually. `[E, N, M]`

- **Grow-and-refine with semantic-embedding de-duplication is the right "Forgetting" operation.** Most agent-memory systems' Forgetting is just FIFO eviction (Memory OS) or threshold-based heat-decay. ACE's grow-and-refine is more nuanced: append new bullets, update in-place when IDs match, then periodically de-duplicate via cosine similarity in semantic embedding space. This catches redundancy that simple FIFO would miss — e.g. when the Reflector emits "always validate JSON before passing to tool" as a new bullet but the playbook already has "validate inputs to tools" as bullet #15. Semantic de-dup merges them. For Flow OS, this is the de-duplication discipline that should run during `/learn` to prevent the same pattern from being captured twice with slightly different phrasing. `[A, M]`

- **The non-LLM merger is the architectural lynchpin — don't let the LLM near the merge step.** §3.1: "delta entries... are merged into the existing context by lightweight, non-LLM logic. Because updates are itemized and localized, multiple deltas can be merged in parallel, enabling batched adaptation at scale." This isn't just for efficiency — it's the structural protection against context collapse. If you let the LLM merge, you reintroduce the risk of monolithic rewriting (because the LLM might decide to "consolidate" the deltas before applying them, which is just collapse in disguise). For Flow OS, every memory-update path should have a deterministic, code-based merger as the final step. The LLM proposes; the code disposes. `[M, A]`

- **Execution feedback is sufficient learning signal — labels are not required.** §4.3: ACE works "without labeled supervision and instead by leveraging natural execution feedback." For AppWorld, execution feedback = whether the agent's actions succeeded in the simulated environment. This is the "self-improving" property — the system can get better at a task by *attempting it and observing what worked*, with no human-labeled training data. For Flow OS, the equivalent is: `/learn` doesn't need the user to mark which captures were "good" or "bad"; it can infer from downstream signals (did the agent successfully complete the next task using the retrieved memory? did the user have to correct the response?). Bake this self-evaluating signal into the `/learn` pipeline. `[E, A]`

- **86.9% adaptation latency reduction is the production-deployability number.** §4.7: ACE cuts adaptation latency by 86.9% on average versus baselines because incremental delta updates avoid the cost of full context regeneration. For a system that runs many adaptation cycles per session, this is the difference between a system that feels responsive and one that feels frozen between turns. For Flow OS, this argues for moving from periodic batch `/learn` runs (which require regenerating large memory chunks) to incremental delta-style updates during normal session work. `[R, M]`

- **Beats GPT-4.1 production agent (IBM-CUGA) on AppWorld using open-source DeepSeek-V3.1.** §1, bullet 3: "On the AppWorld benchmark leaderboard, ACE surpasses the top-1-ranked production-level agent IBM-CUGA (powered by GPT-4.1) while using an open-source model (DeepSeek-V3.1)." Two implications: (a) architectural choice (how the context evolves) can outweigh model-quality choice (which model is the backbone) for agentic tasks — same takeaway as Hindsight's +44.6 pp on OSS-20B; (b) ACE works with open-source models, so Flow OS can deploy it without depending on a frontier-model API. `[R, A]`

- **Brevity bias is a design choice in optimizers, not an inevitable side effect.** §2.2: "GEPA highlights brevity as a strength, but such abstraction can omit domain-specific heuristics, tool-use guidelines, or common failure modes that matter in practice." This is a sharp critique — GEPA's *reward function* explicitly favors brevity, which means it's structurally incapable of accumulating the long-tail domain knowledge that agentic tasks need. The lesson for any prompt-optimization or memory-curation system: design the optimization objective to *value retention*, not just *value compression*. ACE's grow-and-refine explicitly preserves bullet count growth, with de-duplication as a separate refinement pass. For Flow OS, `/learn`'s consolidation prompt should explicitly reward including domain heuristics + failure modes, not just core takeaways. `[A]`

- **The playbook metaphor is more useful than the "memory" metaphor for agent context.** ACE consistently uses "playbook" rather than "memory store" to describe the evolving context. A playbook is something you *consult while playing the game* — it's not background knowledge, it's actionable strategies / heuristics / failure modes you reference during execution. This framing better matches what agents need: not a database of facts, but a curated list of patterns ("when you see X, try Y; common failure mode is Z; recent success used technique W"). For Flow OS, the rebrand might be: `memory/playbooks/` instead of `memory/patterns/` — a more precise framing of what those files actually are. `[N]`

- **The Reflector role validates separation of evaluation from curation.** §3 lists three innovations, the first of which is "a dedicated Reflector that separates evaluation and insight extraction from curation." This is a discipline that maps to Hindsight's separation of Opinion-formation from World/Experience facts. In both papers, the lesson is: *who decides what was important* (the Reflector / Opinion-former) should be a different agent than *who writes it down* (the Curator / Updater). Conflating them — one LLM call that both evaluates and writes — produces worse outcomes than splitting them. For Flow OS, `/learn` should split into `/reflect` (evaluate which session events were important) and `/curate` (write them as deltas into the playbook). `[A]`

- **ACE's playbook is what the Du et al. survey would call a Procedural Memory store.** The survey's functional-type taxonomy (Episodic, Semantic, Procedural, Working) classifies "procedural memory" as "memory that supports the execution of learned skills and action sequences." ACE's bullets are exactly that — reusable strategies, common failure modes, tool-use heuristics. So ACE is best understood as a system for the *procedural* layer of agent memory, not the episodic or semantic. This positioning matters for Flow OS: ACE's pattern is the right architectural choice for `memory/procedural/` (workflows, skill heuristics, common-error fixes), not necessarily for `memory/episodic/` (timeline of events) or `memory/semantic/` (entity relations). `[N, E]`

## How to Apply It (method)

**Scenario:** Same Flow OS context. You have `/learn` that runs after sessions to extract patterns and decisions. Today it's a single prompt that reads the session transcript and emits free-text bullet points into pattern files. Over months of running, the pattern files have started to drift — some patterns get rewritten in slightly different words and accumulate as duplicates; some genuinely-helpful patterns get accidentally summarized away when `/learn` decides "we already have something like this"; you have no mechanism for marking a pattern as harmful when retrieving it produced a wrong answer. You want to retrofit ACE's three-role pipeline + structured bullets + deterministic merger onto `/learn`. This maps to ENGRAM Encode (bullets as structured units), Aggregate (Reflector distillation), Maintain (grow-and-refine with helpful/harmful counters).

**Steps:**

1. **Define the bullet schema.** Replace free-text bullets in pattern files with structured entries:

   ```yaml
   ---
   kind: playbook-bullet
   id: bullet-2026-05-19-001
   playbook: flow-os-agent-memory
   content: "When extracting facts from session captures, prefer narrative facts (2-5 per session that preserve cross-turn context) over atomic facts (single utterances). Atomicization loses the deliberation thread."
   helpful_count: 3
   harmful_count: 0
   source_sessions:
     - 2026-04-23-flow-pitch-tom
     - 2026-05-10-research-cycle
   embedding_hash: "sha256-..."   # cached for de-dup
   created_at: "2026-05-19"
   updated_at: "2026-05-19"
   ---
   ```
   
   Multiple bullets per file (one playbook file = list of bullets); each has its own permanent ID.

2. **Split `/learn` into `/reflect` + `/curate` (Reflector + Curator).** Two new prompts:
   
   **Reflector prompt:**
   ```
   You are the Reflector for a self-improving agent.
   Given the session execution trace below + the current relevant
   playbook bullets, identify:
     1. Bullets that were USED in this session and proved HELPFUL
     2. Bullets that were USED and proved HARMFUL (caused errors)
     3. NEW INSIGHTS that emerged from this session not in any existing bullet
     4. EXISTING bullets that should be REFINED (e.g. corner case added)
   
   Output JSON only — do not write to memory yourself.
   SESSION TRACE: {transcript}
   RELEVANT BULLETS: {top-K bullets by qmd recall}
   OUTPUT: { "helpful_bullets": [id, id, ...], "harmful_bullets": [id, ...], "new_insights": ["...", "..."], "refinements": [{bullet_id, refined_content}, ...] }
   ```
   
   **Curator prompt:**
   ```
   You are the Curator. Given the Reflector's output, emit STRUCTURED
   DELTAS that the deterministic merger will apply.
   
   Allowed delta types:
     - INCREMENT_HELPFUL: bullet_id
     - INCREMENT_HARMFUL: bullet_id
     - ADD_BULLET: {new_id, content, source_session}
     - REPLACE_CONTENT: {bullet_id, new_content}
   
   Do NOT write prose. Do NOT regenerate the playbook. Only emit deltas.
   REFLECTOR OUTPUT: {reflector_json}
   OUTPUT: JSON array of delta objects.
   ```

3. **Build the deterministic merger.** A Python script (NOT an LLM) that takes delta JSON and applies it to the playbook files:
   - INCREMENT_HELPFUL → find bullet by ID, increment helpful_count, update `updated_at`
   - INCREMENT_HARMFUL → find bullet by ID, increment harmful_count, update `updated_at`
   - ADD_BULLET → generate ID, compute embedding hash, append to playbook file
   - REPLACE_CONTENT → find bullet by ID, replace content, recompute embedding hash, update `updated_at`
   
   This script is deterministic, fast, and *cannot* collapse the playbook by accident.

4. **Implement grow-and-refine de-duplication.** Schedule weekly (or lazy-on-write-threshold):
   - For each playbook file, compute pairwise cosine similarity of bullet embeddings
   - For pairs > 0.92 similarity (tunable), merge: keep the bullet with higher `helpful_count - harmful_count`, drop the other, copy the dropped bullet's source_sessions and add its counters to the kept bullet
   - Log every merge to an audit trail
   - This is the field's missing Forgetting operation, implemented as semantic-similarity merging rather than naive deletion

5. **Add execution-feedback gathering to `/work`.** Today `/work` doesn't log which patterns it used or whether they helped. Add a wrapper:
   - When `/work` reads context via `qmd recall`, log which bullet IDs were returned
   - After each task completes, prompt Claude: "Of the bullets you saw, which were helpful and which were misleading?" Log to `experiences/playbook-feedback/<session>.json`
   - This feedback is the input to the Reflector at session end

6. **Add a context-collapse guard.** Before writing any update to a playbook file, compute the diff: if the new file is < 50% the size of the old file (or > 50% smaller than the historical median size), abort the write and log a warning. This catches collapse early — the system should never lose more than half its accumulated playbook in a single update, even by accident. Force human intervention if the threshold is hit.

7. **Run the bullets through a brevity-bias detector.** Periodically (weekly?), scan each playbook file for bullets that are too short (< 20 tokens) or too generic (e.g. "be careful with X" without specifying X). Flag for Reflector enrichment in the next session. This actively counters the brevity-bias failure mode that ACE diagnoses in GEPA.

8. **Use the helpful/harmful counters in `qmd recall` ranking.** When returning playbook bullets, weight by `(helpful_count - 2*harmful_count)` (penalize harmful 2x). Bullets that have been flagged harmful multiple times stop being retrieved unless explicitly invoked. This is the dynamic-prioritization signal that makes the playbook self-improve through use rather than through occasional manual review.

9. **Build an ACE-style benchmark harness.** Take the AppWorld benchmark (Trivedi et al. 2024, referenced in the paper) or a Flow-OS-relevant analog (a task that requires multi-turn reasoning + tool use), set up two arms: (A) baseline `/learn` (current behavior), (B) Reflector + Curator + deterministic merger pipeline. Run both for N iterations on the same task suite, measure task success rate per iteration. The paper's prediction: A plateaus or degrades; B monotonically improves. If your result matches, you have a publishable Flow OS contribution.

10. **Cap context length per playbook, not per individual write.** ACE's grow-and-refine doesn't cap individual write size; it caps total context size at refinement time. This is the right discipline — let individual deltas be small (so context collapse can't happen), and let the playbook grow until a refinement cycle prunes via semantic de-dup. Set a soft cap per playbook (e.g. 50K tokens for a top-level playbook, 10K for a sub-playbook) and trigger grow-and-refine when exceeded.

11. **Diagnostic: track context length trajectory per playbook.** For each playbook file, log its token count after every update. Plot the trajectory. The healthy pattern: monotonic growth with periodic small drops (de-dup pruning). The pathological pattern (context collapse): a sudden cliff from N tokens to N/10 tokens — same shape as ACE Figure 2. If you see that shape, the deterministic merger has a bug or someone bypassed it. Set an alert.

12. **Apply the same protocol to `/citation-walk`'s wiki growth.** The papers wiki grows through `/citation-walk` and `/digest-paper`. The same context-collapse risk applies to the meta-digests synthesised at the end of `/citation-walk` runs — if the meta-digest is regenerated wholesale each run, it can collapse. Apply ACE's discipline: the meta-digest is a playbook of bullets (one bullet per cross-paper insight); each `/citation-walk` run emits structured deltas (new bullets, refined bullets) merged deterministically. The meta-digest accumulates rather than rewrites.

**Expected outcome:** A `/learn` pipeline that (a) splits into Reflector + Curator + deterministic merger, (b) produces structured bullets with helpful/harmful counters instead of free-text summaries, (c) implements grow-and-refine de-duplication as the field's missing Forgetting operation, (d) cannot collapse the playbook by accident (context-collapse guard catches anomalous shrinkage), (e) self-improves through execution feedback without requiring labeled supervision. The context-length trajectory plot per playbook is the diagnostic that tells you the pipeline is working; the helpful/harmful counter distribution tells you which bullets are pulling their weight.

## Best Figure

![Figure 4 — The ACE Framework: Generator → Reflector → Curator pipeline (page 5)](figures/zhang-2025-ace-fig.png)

**Figure Name:** Figure 4: "The ACE Framework. Inspired by Dynamic Cheatsheet, ACE adopts an agentic architecture with three specialized components: a Generator, a Reflector, and a Curator."

**Figure Page:** 5

**Slide Caption:** The ACE pipeline's three-role data flow: a Query plus the current Context Playbook feeds the Generator (LLM #1), which produces a reasoning Trajectory; the Trajectory feeds the Reflector (LLM #2, with iterative-refinement self-loop), which extracts Insights; the Insights feed the Curator (LLM #3), which emits Delta Context Items; the deltas are then merged back into the Context Playbook by deterministic non-LLM logic (the Update arrow on the bottom). The key architectural commitment: every LLM call produces a structured intermediate (Trajectory / Insights / Delta) but only deterministic code writes the final Playbook update.

**Description:** Figure 4 is the architecture diagram in a single horizontal row. Left side: two stacked inputs — "Query" (a stack of document tiles) and "Context Playbook" (a notebook icon). Both feed into a circular node labeled "Generator" (with an LLM icon inside), which outputs "Trajectory" (a stack of trajectory tiles). The Trajectory feeds rightward into the next circular node "Reflector" (LLM icon), which has a dashed self-loop labeled "Iterative Refinement" arcing back into itself. The Reflector outputs "Insights" (a stack of insight tiles), which feed rightward into the third circular node "Curator" (LLM icon). At the bottom of the figure: an "Update" arrow runs from the Curator back to the Context Playbook, passing through "Delta Context Items" (a stack of delta tiles). The figure matters because it visually commits the architecture to the load-bearing claim — that the LLM appears in three places (Generator, Reflector, Curator), each with a *structured intermediate output* (Trajectory, Insights, Delta), and the final Playbook update is applied by *deterministic code*, not by an LLM. This is the structural firewall against context collapse: the LLM never gets to "rewrite the playbook"; it only proposes deltas which are mechanically applied.

**Other strong candidates:**
- **Figure 1 (p. 1)** — Overall performance bar charts on AppWorld / FiNER / Formula. Shows ACE consistently above all baselines (LLM-Base, ICL, GEPA, DC) on all three benchmarks.
- **Figure 2 (p. 3)** — The Context Collapse case study. 18,282 tokens → 122 tokens in one step, 66.7% → 57.1% accuracy. The single most useful diagnostic plot in the paper — visceral evidence for why monolithic rewriting fails.
- **Figure 3 (p. 4)** — Example ACE-generated context on AppWorld. Shows the playbook as a structured document with detailed domain-specific insights, tool snippets, and readily-usable code blocks — concrete proof that the architecture produces useful long context rather than degenerate summaries.

## What Experts Overlook

Most readers will focus on the three-role pipeline (Generator / Reflector / Curator) as the architectural innovation. The detail almost everyone will miss is in §3.1 (Incremental Delta Updates): **the merger of delta context items into the existing context is performed by "lightweight, non-LLM logic"** — Python code, not an LLM call. This single design decision is the load-bearing protection against context collapse. The paper's prose treats it as a minor implementation detail ("merged deterministically into the existing context by lightweight, non-LLM logic"), but read carefully: this is the *only* place in the entire pipeline where the persistent context state is written, and it's the only place where the LLM is *not* in the loop.

Why this matters: if you read the architecture and think "I'll just have the Curator LLM output the new merged context directly" (saving the round-trip through Python merger code), you've reintroduced context collapse as a failure mode — because now the LLM has to read the entire prior context plus the deltas and emit a coherent merged context, which is exactly the monolithic-rewriting risk the architecture was designed to prevent. The non-LLM merger isn't optional cleanup; it's the *whole point*. The paper buries this in implementation detail because the authors take it for granted, but for anyone trying to replicate or adapt the architecture, this is the must-not-skip step.

**Why it matters:** Context engineering and agent memory are hot enough that many teams will read this paper, build a Generator/Reflector/Curator pipeline, and lose the non-LLM merger somewhere in the implementation — either because they think "the Curator's output IS the merged context" (it's not — the Curator outputs *deltas*) or because they bolt the merge step into the Curator's prompt for efficiency ("output the merged playbook in one step"). Either path reintroduces context collapse and the team will see exactly the failure mode in Figure 2: working pipeline for weeks, then a sudden cliff drop in accuracy as the playbook collapses. The paper's table of contributions lists "incremental delta updates" as one of three key innovations, but the actual innovation — the architectural firewall — is that the LLM *cannot write to the playbook directly*. Make this an invariant in any implementation: there's no code path where an LLM's output becomes the new playbook content; only Python merger code can do that.

**Example of good use (memory architectures for agentic OSes):** When implementing the Flow OS retrofit, structure the code so the Curator function returns a `List[Delta]` typed JSON, and the playbook update function `apply_deltas(playbook: Playbook, deltas: List[Delta]) -> Playbook` is *strictly Python* with no LLM calls. Add a CI test that mocks the Curator to return a "rewrite everything as 'TODO'" delta, then verifies the merger correctly applies it only to the bullets explicitly named in the delta (not collapsing the whole playbook). This makes the non-LLM-merger invariant testable. Combined with the Context-Collapse guard (step 6 in the method section above), you have two independent safeguards: the architectural one (the LLM can only emit deltas) and the runtime one (the guard rejects updates that shrink the playbook by >50%).

**Example of misapplication:** A team adopts ACE's three-role pipeline but implements it with a single combined "Reflector-Curator" prompt that takes the trajectory + current playbook and outputs the new playbook directly. They argue this is "more efficient" because it saves a step. Within a few months of running, the playbook collapses exactly as Figure 2 predicts — the combined LLM has been gradually preferring shorter outputs (because shorter outputs are cheaper and the model has been trained on "concise is better"), and one day it produces a 95% smaller playbook that misses critical domain heuristics. The team thinks they're using ACE; they're actually using a Reflexion-style monolithic rewriter that the ACE paper specifically warned against. The lesson missed: **the three roles + structured bullets are necessary but not sufficient; the deterministic non-LLM merger is the architectural firewall, and removing it for "efficiency" reintroduces the failure mode the architecture was designed to prevent.** Treat the non-LLM merger as a non-negotiable architectural invariant, not an implementation detail to be optimised away.

## Extracted Prompts

**Prompt explanation:** Generator role (§3, Figure 4) — produces reasoning trajectories for new queries while annotating which playbook bullets were used and how. Reconstructed from the paper's methodology since no verbatim prompt is given:

```
You are the Generator agent. Your job is to solve the given query using
the current playbook of accumulated strategies and to produce a detailed
trajectory that the Reflector can later analyze.

CURRENT PLAYBOOK (numbered bullets with metadata):
{playbook_bullets_with_ids}

QUERY: {query}

INSTRUCTIONS:
1. Solve the query step by step. Show all reasoning, all tool calls, and
   all intermediate outputs.
2. As you reason, EXPLICITLY MARK which bullets you used and how:
     [BULLET 17 USED] — followed the strategy here
     [BULLET 23 ATTEMPTED, INCORRECT] — this strategy didn't apply
     [NO BULLET APPLIED] — for a step where no existing bullet guided you
3. At the end, produce your final answer.

Your output is a complete trajectory: reasoning + tool calls + bullet
annotations + final answer.

OUTPUT FORMAT:
<trajectory>
  <step>...</step>
  <step>... [BULLET 17 USED]</step>
  ...
  <final_answer>...</final_answer>
</trajectory>
```

**Prompt explanation:** Reflector role (§3, §4.6) — distills concrete insights from the Generator's trajectory, separating success patterns from failure modes. Optionally iterated multiple times for refinement.

```
You are the Reflector agent. You analyze a Generator's trajectory to
extract concrete insights that should be added to or refined in the
playbook.

CURRENT PLAYBOOK (numbered bullets with metadata):
{playbook_bullets_with_ids}

GENERATOR'S TRAJECTORY:
{trajectory}

EXECUTION OUTCOME (success / failure / partial):
{outcome}

YOUR TASK — extract:

1. HELPFUL BULLETS: bullet IDs that were used AND contributed to success.
   For each, briefly justify why it helped.

2. HARMFUL BULLETS: bullet IDs that were used AND led to error or wasted
   effort. For each, briefly justify why it misled.

3. NEW INSIGHTS: concrete strategies, failure modes, or domain heuristics
   that emerged from this trajectory and are NOT already captured by any
   existing bullet. Each new insight must be:
     - Actionable (a future Generator can directly apply it)
     - Specific (mentions the trigger condition, not just the rule)
     - Verifiable (the outcome of applying it can be checked)

4. REFINEMENTS: existing bullets that should be updated with a corner case,
   exception, or clarification revealed by this trajectory.

CRITICAL CONSTRAINTS:
- Do NOT propose merging existing bullets — the merger is non-LLM.
- Do NOT propose deleting bullets — flag as HARMFUL if relevant.
- Do NOT generate vague platitudes ("be more careful"); be SPECIFIC about
  triggers and actions.

OUTPUT JSON:
{
  "helpful_bullets": [{"id": 17, "reason": "..."}, ...],
  "harmful_bullets": [{"id": 23, "reason": "..."}, ...],
  "new_insights": [
    {"trigger": "when X happens", "action": "do Y", "rationale": "because Z"}
  ],
  "refinements": [
    {"bullet_id": 15, "additional_content": "Note: this fails when ..."}
  ]
}
```

**Prompt explanation:** Curator role (§3, §3.1) — converts the Reflector's insights into structured delta operations that the non-LLM merger can apply. The strict output format is the architectural firewall.

```
You are the Curator agent. Given the Reflector's analysis, emit
STRUCTURED DELTA OPERATIONS that the deterministic merger will apply
to the playbook.

REFLECTOR OUTPUT:
{reflector_json}

ALLOWED DELTA OPERATIONS:
1. {"op": "INCREMENT_HELPFUL", "bullet_id": <id>}
2. {"op": "INCREMENT_HARMFUL", "bullet_id": <id>}
3. {"op": "ADD_BULLET", "content": "<actionable, specific, verifiable insight>", "source_trajectory_id": "<id>"}
4. {"op": "REFINE_BULLET", "bullet_id": <id>, "appended_content": "<addition to existing content>"}

CRITICAL CONSTRAINTS:
- Output ONLY a JSON array of delta operations. No prose, no explanation,
  no metadata outside the array.
- Do NOT emit operations not in the allowed list.
- Do NOT propose a full playbook rewrite. The merger handles merging.
- Each ADD_BULLET must have content < 500 tokens. Larger insights should
  be split into multiple bullets.

OUTPUT:
[
  {"op": "INCREMENT_HELPFUL", "bullet_id": 17},
  {"op": "ADD_BULLET", "content": "When fetching X from the Y API, the response shape differs in <500 vs >=500 token requests. Always check the `format_version` field.", "source_trajectory_id": "traj-456"},
  ...
]
```

**Prompt explanation:** Grow-and-refine de-duplication trigger (§3.2) — the rule for when to invoke semantic-similarity-based bullet merging. Conceptual recipe rather than a prompt:

```
PROACTIVE MODE (after each delta application):
  For each newly-added bullet:
    Compute embedding e_new
    For each existing bullet b in the same playbook with embedding e_b:
      if cosine(e_new, e_b) > 0.92:
        # Candidate merger
        Keep bullet with higher (helpful_count - harmful_count)
        Merge counters from dropped bullet into kept bullet
        Merge source_sessions lists
        Log the merger to audit trail

LAZY MODE (only when playbook exceeds soft cap, e.g. 50K tokens):
  Run pairwise cosine similarity across ALL bullets in the playbook
  Apply the same merging rule for pairs > 0.92 similarity
  Continue until playbook fits below soft cap OR no more high-similarity pairs

NEVER:
  - Delete a bullet without merging its counters elsewhere
  - Merge bullets with disjoint source_sessions (loses provenance)
  - Use an LLM to decide which bullets to merge — use only deterministic
    cosine similarity + counter comparison
```

## Citations

First 10 of ~30 most relevant references (full reference list in source PDF):

- Agarwal et al. (2024) — *Many-Shot In-Context Learning* — arXiv preprint (the ICL baseline)
- Agrawal et al. (2025) — *GEPA: Genetic-Pareto Prompt Optimization* — arXiv preprint (the strongest baseline)
- Asai et al. (2024) — *Self-RAG: Learning to Retrieve, Generate, and Critique* — ICLR
- Lewis et al. (2020) — *RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* — arXiv:2005.11401
- Opsahl-Ong et al. (2024) — *MIPROv2: Optimizing Multi-Stage LM Programs* — arXiv preprint
- Shinn et al. (2023) — *Reflexion: Language Agents with Verbal Reinforcement Learning* — NeurIPS
- Suzgun et al. (2025) — *Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory* — arXiv preprint (architectural ancestor)
- Trivedi et al. (2024) — *AppWorld: Benchmark for Interactive Coding Agents* — ACL
- Wei et al. (2022) — *Chain-of-Thought Prompting Elicits Reasoning in LLMs* — NeurIPS
- Xu et al. (2025) — *A-Mem: Agentic Memory for LLM Agents* — arXiv:2502.12110

## Related Digests

- [[latimer-2025-hindsight-memory]] — Hindsight (Latimer et al., 2025) — operates at the *memory store* level (four typed networks); ACE operates at the *context evolution* level (playbook of bullets with counters). Complementary: Hindsight's Opinion-reinforcement step (Δc ± α) is the analog of ACE's INCREMENT_HELPFUL / INCREMENT_HARMFUL counter updates.
- [[wang-2025-mirix]] — MIRIX (Wang & Chen, 2025) — six-component multi-agent memory system. MIRIX's Memory Managers + Meta Memory Manager are an analog of ACE's three-role split; ACE's contribution is the structural focus on *delta updates + non-LLM merger* as the protection against context collapse.
- [[liu-2025-memverse]] — MemVerse (Liu et al., 2025) — slow KG + fast parametric cache. MemVerse's periodic distillation parallels ACE's grow-and-refine refinement cycle, but ACE's refinement targets explicit bullet de-duplication while MemVerse's targets parameter compression.
- [[kang-2025-memory-os]] — MemoryOS (Kang et al., 2025) — STM/MTM/LPM with heat-based eviction. MemoryOS's heat-based segment eviction is one form of Forgetting; ACE's semantic-similarity de-duplication is another. Both reject naive FIFO.
- [[du-2025-rethinking-memory]] — Du et al. survey (2025) — ACE is mentioned as an example of "Agentic Context Engineering" in the survey's Multi-Source Retrieval / Long-Context sections. The survey's six-operation taxonomy categorizes ACE as implementing Consolidation (Curator), Updating (delta merger), Forgetting (grow-and-refine de-dup), Retrieval (Generator's bullet selection), Condensation (Reflector's distillation).
- [[xu-2025-a-mem-agentic-memory]] — A-Mem (Xu et al., 2025) — referenced as the canonical "agentic memory" baseline; ACE's bullet concept "builds on top of" A-Mem's memory entry concept (§3.1).

## Reviewer Notes

**Hallucination severity:** Clean

Spot-checks against the source PDF:

- **Three-role pipeline: Generator + Reflector + Curator** — verified in §3 (p. 4) and Figure 4 (p. 5). ✓
- **+10.6% on agents and +8.6% on finance average gains** — verified in §1, second-to-last sentence of abstract and §4 results bullets. ✓
- **AppWorld up to +17.1% over baselines** — verified in §4 first bullet ("It boosts accuracy on the AppWorld benchmark by up to 17.1%"). ✓
- **Matches IBM-CUGA (GPT-4.1) on overall and surpasses on test-challenge using DeepSeek-V3.1** — verified in §1 third bullet. ✓
- **86.9% adaptation latency reduction** — verified in §4 fourth bullet. ✓
- **No labeled supervision required — execution feedback alone** — verified in §1 second bullet and §4.3. ✓
- **Context collapse: 18,282 tokens → 122 tokens at step 60→61, 66.7% → 57.1% accuracy, below 63.7% baseline** — verified in §2.2 ("Context Collapse" subsection p. 3) and Figure 2 (p. 3). ✓
- **Brevity bias critique of GEPA** — verified in §2.2 ("GEPA highlights brevity as a strength, but such abstraction can omit domain-specific heuristics"). ✓
- **Incremental delta updates + grow-and-refine + non-LLM merge** — verified in §3.1 and §3.2. ✓
- **Bullet schema: id + content + helpful/harmful counters** — verified in §3.1 ("(1) metadata, including a unique identifier and counters tracking how often it was marked helpful or harmful; and (2) content"). ✓
- **De-duplication via semantic embeddings (cosine similarity)** — verified in §3.2 ("A de-duplication step then prunes redundancy by comparing bullets via semantic embeddings"). ✓
- **AppWorld benchmark from Trivedi et al. 2024** — verified in §4.1 with citation. ✓
- **FiNER from Loukas et al. 2022; Formula from Wang et al. 2025a; BIRD-SQL from Li et al. 2023; DDXPlus from Fansi Tchango et al. 2022** — verified in §4.1. ✓
- **Backbone for the IBM-CUGA comparison: open-source DeepSeek-V3.1** — verified in §1 third bullet. ✓
- **Inspired by Dynamic Cheatsheet (Suzgun et al. 2025)** — verified in §3 ("Inspired by the agentic design of Dynamic Cheatsheet"). ✓
- **arXiv ID 2510.04618v3, 29 Mar 2026** — verified in title page header. ✓
- **Published as ICLR 2026 conference paper** — verified in top-of-page banner. ✓
- **Authors: Stanford (Zhang, Zou, Olukotun) + SambaNova (Hu, Upasani, Ma, Hong, Kamanuru, Rainton, Wu, Ji, Thakker) + UC Berkeley (Li, Hu cross-affiliated)** — verified in author block (p. 1). ✓
- **Code at github.com/ace-agent/ace, site ace-agent.github.io** — verified in title page. ✓

The digest's framing of the non-LLM merger as "the architectural firewall against context collapse" is a synthesis judgment by the digester. The paper's prose treats it as an implementation detail ("merged deterministically into the existing context by lightweight, non-LLM logic"); the "What Experts Overlook" section flags this gap between the paper's framing and its actual importance — clearly marked as digester synthesis, not paper claim.

The digest's specific Python merger pseudocode in the methodology section is original to the digest; the paper provides high-level methodology not implementation code.

No fabricated claims found. Severity: **Clean**.
