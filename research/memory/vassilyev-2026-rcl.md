---
corpus: agentic-memory
kind: paper-digest
slug: vassilyev-2026-rcl
title: "Reflective Context Learning: Studying the Optimization Primitives of Context Space"
authors:
  - "Nikita Vassilyev"
  - "William Berrios"
  - "Ruowang Zhang"
  - "Bo Han"
  - "Douwe Kiela"
  - "Shikib Mehri"
year: 2026
publication_date: "2026-04"
venue: "arXiv preprint (under review)"
source_url: "https://arxiv.org/abs/2604.03189"
doi: null
arxiv_id: "2604.03189"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "RCL reframes context-space adaptation as a single optimization problem isomorphic to gradient descent (context artifact C ↔ parameters θ, reflection ↔ gradient, mutation ↔ optimizer step) and shows that the same classical pathologies (variance, forgetting, local optima, oscillation) and remedies (batching, grouped rollouts, credit assignment, auxiliary losses, failure replay, optimizer state) transfer directly; layered onto the ACE baseline, five primitives produce a composed optimizer that achieves +11.3 TGC over seed on AppWorld Normal/Lite (Gemini Flash Lite) and beats GEPA + ACE across AppWorld, BrowseComp+, and RewardBench2, with two consistent findings: (1) diagnostic-precision primitives (optimizer state, auxiliary losses) give larger gains per unit of compute than execution-volume primitives, and (2) the contribution of each primitive depends on task regime — the same primitive can hurt as a standalone addition yet be load-bearing in composition (batching on BrowseComp+/Nano: −6.0 standalone, −14.6 when removed from full RCL), forcing the field to abandon 'isolated trick' framings of context optimizers and adopt classical-ML's compositional study discipline."
topics:
  - context-space-optimization
  - reflective-context-learning
  - playbook-memory
  - textual-gradients
  - batching
  - grouped-rollouts
  - credit-assignment
  - auxiliary-losses
  - failure-replay
  - optimizer-state
  - momentum
  - context-collapse
  - brevity-bias
  - appworld
  - browsecomp
  - rewardbench
  - reflexion
  - protege
  - textgrad
  - ace
  - gepa
  - dynamic-cheatsheet
  - expel
  - dspy
  - mipro
  - dual-trace-credit-assignment
  - composition-non-additive
tags:
  - paper
  - context-engineering
  - reflective-context-learning
  - rcl
  - optimization-primitives
  - contextual-ai
  - appworld
  - browsecomp-plus
  - rewardbench2
  - context-space-learning
  - playbook
  - agent-memory
entities:
  - vassilyev-nikita
  - berrios-william
  - kiela-douwe
  - mehri-shikib
  - contextual-ai
related_digests:
  - zhang-2025-ace
  - latimer-2025-hindsight-memory
  - wang-2025-mirix
  - du-2025-rethinking-memory
  - xu-2025-a-mem-agentic-memory
citations:
  - title: "ACE: Agentic Context Engineering — Evolving Contexts for Self-Improving Language Models"
    authors: ["Qizheng Zhang", "Changran Hu", "et al."]
    year: 2026
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "2510.04618"
  - title: "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning"
    authors: ["Lakshya A. Agrawal", "et al."]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2507.19457"
    arxiv_id: "2507.19457"
  - title: "ProTeGi: Automatic Prompt Optimization with 'Gradient Descent' and Beam Search"
    authors: ["Reid Pryzant", "et al."]
    year: 2023
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "TextGrad: Automatic Differentiation via Text"
    authors: ["Mert Yuksekgonul", "et al."]
    year: 2024
    venue: "arXiv preprint"
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
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training-Free GRPO (TF-GRPO)"
    authors: ["Yuzheng Cai", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2510.08191"
  - title: "ExpeL: LLM Agents Are Experiential Learners"
    authors: ["Andrew Zhao", "et al."]
    year: 2024
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "ERM: Experiential Reflection Memory as Optimizer State"
    authors: ["Yan", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sampling-Based Momentum for Textual Gradient Descent"
    authors: ["Zixin Ding", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2506.00400"
  - title: "AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents"
    authors: ["Harsh Trivedi", "et al."]
    year: 2024
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "BrowseComp+: A Fair and Transparent Evaluation Benchmark of Deep-Research Agents"
    authors: ["Zijian Chen", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2508.06600"
    arxiv_id: "2508.06600"
  - title: "RewardBench2"
    authors: ["Malik", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    authors: ["Shunyu Yao", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "DSPy: Compiling Declarative LM Calls into Self-Improving Pipelines"
    authors: ["Omar Khattab", "et al."]
    year: 2024
    venue: "ICLR"
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
  - title: "Adam: A Method for Stochastic Optimization"
    authors: ["Diederik Kingma", "Jimmy Ba"]
    year: 2015
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Prioritized Experience Replay"
    authors: ["Tom Schaul", "et al."]
    year: 2016
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Let's Verify Step by Step (step-level reward modeling)"
    authors: ["Hunter Lightman", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Curriculum Learning"
    authors: ["Yoshua Bengio", "et al."]
    year: 2009
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Learning dynamics on AppWorld dev (Gemini 3.1 Flash-Lite, 57 tasks): TGC and recently-solved rate per primitive, with active vs stale forgetting decomposition"
  page: 13
  image_path: "figures/vassilyev-2026-rcl-fig.png"
---

# Reflective Context Learning: Studying the Optimization Primitives of Context Space

**Authors:** Nikita Vassilyev, William Berrios, Ruowang Zhang, Bo Han, Douwe Kiela, Shikib Mehri (Contextual AI)
**Published:** 2026-04 (arXiv:2604.03189v1, 3 Apr 2026) · **Venue:** arXiv preprint, under review · [Source](https://arxiv.org/abs/2604.03189) · [Code](https://github.com/nvassilyev/RCL)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Reflective Context Learning (RCL) is a unified framework from Contextual AI (Kiela's group) that recasts context-space adaptation — the loop of execute → reflect → update a structured playbook — as the same kind of iterative optimization problem that parameter-space SGD/Adam solve, then systematically transfers five classical optimization primitives across the boundary. The functional correspondence is explicit (Table 1): the context artifact `C` (playbook, memory, tools, guidelines) is the analogue of weights `θ`; trajectory `τ = A(x, C)` is the forward pass; outcome `r = R(τ, y*)` is the loss; reflection `∆ = g(τ, r, C)` is the gradient; mutation `C_{t+1} = f(C_t, ∆)` is the optimizer step. From this isomorphism the paper extracts five primitives (Table 2) — **Batching** (sample B tasks per iteration), **Grouped Rollouts** (execute each task G times for contrastive pass/fail signal), **Improved Credit Assignment** (dual-trace: run task twice — once standard, once with XML-annotated playbook entries the agent must cite — to localize blame to specific bullets), **Auxiliary Losses** (decompose the reflector into 3 heads: ∆_attr ∈ {actionable_gap, execution_variance, intractable}, ∆_root, ∆_gap), **Failure Replay** (replay buffer with graduate/evict thresholds), **Optimizer State** (rolling state document S_t tracking change ledger + playbook assessment + open hypotheses + optimization phase, injected to mutator but excluded from reflector — analogous to Adam's momentum operating on the step not the gradient). Layered onto **ACE as the base loop**, the composed RCL optimizer beats both ACE and GEPA across three benchmarks of deliberately different shape: **AppWorld** (multi-step coding, seed 78-82%, narrow seed-to-ceiling gap → finetuning regime), **BrowseComp+** (web research, seed 29-41%, wide gap → skill-acquisition regime), **RewardBench2** (single-turn judgment, seed 68-76%, near-deterministic → calibration regime). Headline numbers: **+11.3 TGC over seed on AppWorld Normal/Lite (Gemini 3.1 Flash-Lite)**, +10.6 on RewardBench2/Nano. Three discoveries: (1) **diagnostic-precision primitives** (optimizer state, auxiliary losses) give the largest gains per unit of compute — they don't need extra rollouts. (2) **Standalone gains do not predict compositional role** (Table 4): batching *hurts* BrowseComp+/Nano by −6.0 as a standalone addition to ACE, but removing it from full RCL costs −14.6 — interactions are non-additive. (3) **Match capacity to role, don't maximize uniformly**: Sonnet as mutator beats Opus as mutator across benchmarks, because faithful constrained editing matters more than raw capability — a too-capable mutator over-interprets the reflector's diagnostic rather than executing it precisely. Training-dynamics analysis (Figure 2) tracks per-task solve status across 30 iterations and decomposes the gap between all-time-best-so-far and current TGC into **active instability** (recent forgetting) and **stale regressions** (older forgetting not yet recovered) — making "context-collapse" and "catastrophic forgetting" measurable in context space the way they're measured in parameter space.

## Key Takeaway

This is the **structural** companion paper to ACE (Zhang 2025-ace, also digested) — where ACE prescribed a *specific architecture* (Generator/Reflector/Curator + delta updates + non-LLM merger), RCL formalises the *optimization-theoretic frame* that makes ACE and its peers (Reflexion, ProTeGi, TextGrad, GEPA, ExpeL, Dynamic Cheatsheet) all instances of one shared loop, then layers ML's standard remedies on top. The single most useful lesson: **context-space optimization has the same pathologies as parameter-space optimization (variance, forgetting, oscillation, local optima), so the same remedies port over — and the field's prior treatment of these methods as "isolated tricks" is the same kind of pre-paradigmatic confusion that ML had before Adam unified the optimizer-design literature.** A practical sub-lesson: **diagnostic precision (better reflection) gives more performance-per-compute than execution volume (more rollouts).** This inverts the assumption built into most agent-evaluation papers, where the answer to "how do I get more signal" is "run more episodes." RCL says: get *better* signal from the episodes you have — structured reflection heads, dual-trace credit assignment, an optimizer state document the mutator can consult. A second sub-lesson for any system that adapts memory online: **the optimizer-state asymmetry** (state injected into mutation but not reflection) is load-bearing. It mirrors Adam's split — momentum biases the *step* while the gradient remains a clean estimate of current loss — and breaking it (e.g., showing the reflector your past edits) reintroduces oscillation. The third lesson, learned the hard way through Table 4: **don't ablate primitives in isolation to decide whether to include them**. Standalone evaluation systematically mis-ranks compositional value. The right protocol is leave-one-out on the full composed optimizer, which inverts several rankings (batching on BrowseComp+: −6.0 standalone, −14.6 to remove from RCL).

## Implications

- **Adopt the gradient-descent metaphor as the canonical frame for memory updates.** Every place in Flow OS where memory evolves through "execute → reflect → write back" is now isomorphic to one iteration of an optimizer. Name the pieces explicitly in code and docs: `forward_pass()` (the work), `outcome_signal()` (success/failure/reward), `reflector()` (what to change), `mutator()` (apply change), `optimizer_state` (rolling context the mutator consults). Once the components have these names, the menu of remedies is the entire ML-optimizer literature, not a folklore catalogue of "tips for prompt engineering." `[A, M]`

- **Diagnostic-precision primitives are higher leverage than execution-volume primitives.** RCL's clearest practical result: optimizer state and auxiliary losses (both reflector-side improvements with zero extra rollouts) beat ACE on the majority of conditions across all three benchmarks. For Flow OS, this means the next 10x improvement in `/learn` will *not* come from running `/learn` more often — it will come from making the Reflector step more diagnostic (structured failure-attribution heads, root-cause analysis, coverage-gap analysis). Cost: zero extra task executions. Implementation work: a more structured prompt and parsing. This is the cheapest possible upgrade path. `[A, R]`

- **The optimizer-state document is the right shape for `brain-health/progress.md` v2.** Today `progress.md` is a free-text scratchpad. RCL's S_t document — a structured rolling state with **change ledger** (what was modified and why), **playbook assessment** (which bullets are working vs poorly), **open hypotheses** (conjectured failure modes not yet confirmed), and **optimization phase** (exploratory vs convergent) — is a much sharper schema for the same purpose. Critically: this state is injected into the Curator/mutator step but **excluded from the Reflector**, so the reflector's diagnostics stay unbiased by what's already been tried. For Flow OS, this maps to: `/learn`'s reflection step should NOT see the prior `/learn` decisions; `/learn`'s curation step (delta-emission) MUST see them. `[M, A]`

- **Dual-trace credit assignment is the cleanest way to fix the "which bullet caused this failure" problem.** RCL's protocol: run each task **twice** — once with the plain playbook, once with an XML-annotated playbook where every bullet has instrumentation that the agent must cite when it uses it ("flag uncertainty, note where guidance was missing"). The annotated trace is used only for **observability**, not for outcome scoring (because instrumentation alters behavior). The reflector sees both traces but only the *standard* outcome. For Flow OS, this is the right protocol whenever you need to know which pattern memory helped or hurt a specific session: don't try to retro-attribute from logs; run the session a second time with the playbook XML-instrumented and let the model self-report. `[G, R]`

- **Match model capacity to role, not maximize uniformly — Sonnet beats Opus as mutator.** §4.6: "Opus as mutator does not dominate despite being the strongest model; Sonnet is the most consistently strong mutator across benchmarks. A model that is too capable in the latter role may over-interpret the diagnostic rather than execute it precisely." This is a hard-won design rule with immediate Flow OS application: the Generator wants the strongest model (it's reasoning over the task), the Reflector wants the strongest model (diagnosis is hard), but the **Curator/mutator** should be *constrained* — its job is faithful structured-delta emission, not re-reasoning. Use Sonnet or even Haiku for the Curator role; reserve Opus for Generator and Reflector. This both saves cost and produces better edits. `[A]`

- **Standalone ablations are a misleading proxy for compositional contribution — always run leave-one-out on the full composition.** Table 4 is the most quietly important result in the paper. Batching is +5.4 standalone over ACE on AppWorld Normal/Lite but **−14.6 when removed from full RCL** on BrowseComp+/Nano — the standalone test rated it weak, the compositional test rated it load-bearing. Auxiliary losses are the inverse: +7.7 standalone on AppWorld Normal/Nano but **+12.6 when removed from full RCL** on RewardBench2/Nano. For any Flow OS feature decision (e.g., "should `/learn` use grouped rollouts? failure replay? auxiliary loss heads?"), the answer requires running the full pipeline with and without each — single-axis ablations systematically mis-rank. `[A, M]`

- **Active instability + stale regressions is the right *measurement* of context collapse.** Figure 2's framework: at each checkpoint, plot (a) current TGC (what's solved now), (b) recently-solved rate (what's been solved in trailing 5 iterations), (c) all-time best-so-far envelope (what's *ever* been solved). The gap between (a) and (b) is **active instability** — recent forgetting. The gap between (b) and (c) is **stale regression** — older capabilities the system can no longer execute. For Flow OS, this is the diagnostic plot every memory system needs: track which patterns have ever been used helpfully (envelope), which are currently retrievable (TGC), and which were used in the last N sessions (window). Healthy: thin gaps that close over time. Pathological: widening stale-regression band (the system forgets faster than it learns). `[M]`

- **Failure replay with graduate/evict thresholds is the right discipline for `experiences/captures/`.** RCL's failure buffer: a task **graduates** (is removed) after `n_grad` consecutive passes, **evicts** (is dropped) after `n_evict` consecutive failures (it's intractable, don't let it dominate the signal). Apply to Flow OS: a capture/failure that gets recurringly cited by `/learn` for the same insight should graduate (consolidate into a pattern, drop from active capture pool); a capture that fails to produce useful learning across N runs should evict (archive but stop sampling). This avoids two failure modes: (a) the same pattern being re-extracted on every `/learn` run, (b) impossible-to-learn cases dominating the training signal. `[E, M]`

- **Per-trace reflection vs batched reflection is a load-bearing design choice, not an implementation detail.** §4.7 distinguishes: **batching** sends B trace-diagnostic pairs to the mutator (mutator reconciles); **batched reflection** sends B traces to the reflector (reflector synthesises a single ∆). Batched reflection helps on hard tasks (BrowseComp+ +9.4), hurts on easy ones (AppWorld Normal −3.6). For Flow OS, when designing the Reflector prompt: the right granularity depends on the task regime. For broad-domain `/learn` runs, prefer per-trace (each capture gets its own diagnostic, mutator reconciles); for narrow specialist work where many traces share failure modes, prefer batched reflection. Make this a runtime flag, not a fixed choice. `[R, A]`

- **Context-space training has the same regime sensitivity as parameter-space training — pick primitives to match the seed-to-ceiling gap.** §4.2 names three regimes: (1) **narrow gap / finetuning** (AppWorld: seed 78-82%, ceiling ~90%) — multiple primitives contribute, no single winner; (2) **wide gap / skill acquisition** (BrowseComp+: seed 29-41%) — failure replay leads, repeated refinement of difficult cases; (3) **near-deterministic / calibration** (RewardBench2: seed 68-76%) — grouped rollouts (contrastive signal) dominate, over-structuring (auxiliary losses) can hurt. For Flow OS, this means there's no universal `/learn` configuration — the right primitive mix depends on whether the user is fine-tuning known workflows (Flow agents on familiar tasks), acquiring a new skill (first time setting up a venture vertical), or calibrating judgement (deciding between options where neither is clearly right). The skill could take a `--regime` flag. `[A]`

- **The Functional-Correspondence Table (Table 1) is reusable as a mental-model template for any new memory paradigm.** The structure — "Classical concept | RCL analogue | Prior work" — is the right way to write any framework paper that ports remedies from one space to another. Use this template when documenting how memory architectures port to/from databases, OS kernels, or graph databases. The act of forcing a 1:1 mapping reveals which remedies *don't* translate (and therefore where the analogy breaks). For Flow OS docs: a similar "Classical OS concept | Flow OS analogue" table for `memory/` would clarify which OS primitives (paging, virtual memory, COW, journaling) are load-bearing analogies vs decorative ones. `[N]`

- **Reflection quality, not execution volume, is the binding constraint in modern context optimization.** This claim is the paper's deepest pivot. Early prompt optimization (APE, ProTeGi era) assumed the model couldn't follow instructions reliably, so the optimizer had to **search wide** over prompt phrasings. Today's models follow instructions faithfully; the bottleneck is no longer "find the prompt the model can execute" but "find the diagnosis of what went wrong that the model can act on." This is why the cheapest primitives (auxiliary losses, optimizer state, both reflector-side) lead the standalone-gain rankings. For Flow OS: invest in `/learn`'s *prompt structure* (multi-head reflection, structured failure attribution) rather than `/learn`'s *frequency* or its *batch size*. `[R, A]`

## How to Apply It (method)

**Scenario:** Same Flow OS context as the ACE digest. You're retrofitting `/learn` from a free-text-bullet pipeline to ACE's structured-bullet pipeline. Now you also want to bake in the optimization discipline RCL extracts: structured reflection heads, optimizer state, failure replay, model-allocation-per-role, and a measurement scheme for active vs stale forgetting. Mapped to ENGRAM: Encode (reflection schema as a write-time structure), Retrieve (state-document-aware ranking), Aggregate (mutator's reconciliation step), Maintain (graduate/evict thresholds).

**Steps:**

1. **Refactor `/learn` to make the 3 components named and independent.** Today `/learn` is one prompt. Split into three call sites:
   - `generator()` — produces the session trace (this is just `/work` running normally; no new call needed)
   - `reflector(trace, outcome, current_playbook, prior_state)` — emits structured ∆
   - `mutator(current_playbook, ∆, state)` — applies edits

   Critical: each is a separate Claude call with its own prompt and its own model choice. Optimizer state document `S_t` lives in `brain-health/optimizer-state.md` (new file) and is read by `mutator` but NOT by `reflector`.

2. **Implement the multi-head reflector (RCL §3.3).** Reflector output is structured JSON:
   ```json
   {
     "attribution": "actionable_gap | execution_variance | intractable",
     "root_cause": "...specific causal chain...",
     "coverage_gap": "...what's missing from the playbook to handle this...",
     "helpful_bullets": [{id, reason}],
     "harmful_bullets": [{id, reason}],
     "new_insights": [{trigger, action, rationale}]
   }
   ```
   The attribution head is load-bearing: `execution_variance` outputs trigger NO mutation (just an INCREMENT counter on the relevant bullets), preventing the "noisy signal causes spurious edits" failure mode. Only `actionable_gap` triggers ADD/UPDATE deltas. `intractable` flags the case for archival and removes it from the failure-replay pool.

3. **Implement the optimizer-state document.** Maintain `brain-health/optimizer-state.md` updated after every `/learn` run by a dedicated `h()` call:
   ```yaml
   ---
   kind: optimizer-state
   updated_at: <ISO>
   iteration: <N>
   ---
   ## Change Ledger (last 20 edits)
   - 2026-05-19 #145: ADD "When fetching X from Y API, check format_version" (session: research-cycle)
   - 2026-05-18 #144: INCREMENT_HELPFUL bullet #87 (session: flow-pitch)
   ...

   ## Playbook Assessment
   - Working well: bullets #12, #45, #87 (high helpful_count/harmful_count ratios)
   - Working poorly: bullets #23, #91 (high harmful_count, candidates for refinement)

   ## Open Hypotheses (untested)
   - Hypothesis: bullet #67 may be redundant with #112 — needs same-task A/B
   - Hypothesis: the "always prefer narrative facts" rule may hurt on quick-capture sessions

   ## Optimization Phase
   - exploratory  (many ADDs, few REFINEMENTs in last 5 runs)
   ```
   This file is **injected to the Curator/mutator prompt** but explicitly EXCLUDED from the Reflector prompt. Document this invariant in `.claude/commands/learn.md`.

4. **Implement dual-trace credit assignment for high-stakes sessions.** When a session needs deep credit attribution (e.g. an important client deliverable went sideways), re-run the same session with a *playbook-annotated* version where each bullet has XML instrumentation:
   ```xml
   <bullet id="47" content="...">
     <usage>When using this bullet, output: [BULLET 47 USED] before the reasoning step it informed. If you considered it and rejected it, output [BULLET 47 REJECTED: reason]. If guidance was missing for a decision, output [GUIDANCE GAP: what you needed].</usage>
   </bullet>
   ```
   The instrumented trace is used only for the Reflector to localize blame to specific bullets; the standard trace's outcome is what's scored. This is the protocol for serious debugging, not the default.

5. **Implement the failure replay buffer.** Add `experiences/replay-buffer/` directory. When a session produces an `actionable_gap` failure, copy the session capture into the replay buffer with metadata `{n_attempts: 0, n_consecutive_passes: 0, n_consecutive_failures: 1, entered_at: <ISO>}`. At each `/learn` run, sample 50% of session captures fresh and 50% from the replay buffer (per RCL's ρ=0.5). Update counters: graduate (delete from buffer) after `n_grad=2` consecutive passes, evict (archive to `experiences/archived/`) after `n_evict=5` consecutive failures.

6. **Allocate models per role:**
   - **Generator**: Opus 4.7 (this is `/work` — already uses the strongest model)
   - **Reflector**: Opus 4.7 (diagnosis is the hard part — give it the best model)
   - **Mutator (Curator)**: Sonnet 4 (faithful constrained editing — Opus over-interprets; Sonnet beats Opus on this role across all three RCL benchmarks)
   - **Optimizer-state updater (`h()`)**: Haiku (it's just summarizing what was edited and why)
   
   Document this in the Models reference. Estimated cost savings: ~40% on `/learn` runs.

7. **Build the active-instability + stale-regression diagnostic.** Add `scripts/playbook-dynamics.py` that tracks per-bullet usage status across `/learn` runs:
   - For each playbook bullet, log at each `/learn` checkpoint: `{used: bool, helpful: bool, harmful: bool}`
   - **Current "TGC"** = fraction of bullets that have been used helpfully at least once in the last N runs
   - **Recently-helpful rate** = fraction used helpfully in trailing window of W=5 runs
   - **All-time-best envelope** = fraction ever used helpfully
   - **Active instability** = recently-helpful − current  (bullets used helpfully in window but not currently)
   - **Stale regressions** = all-time-best − recently-helpful  (bullets historically used but not in window)
   
   Plot at `brain-health/dynamics.png` after every 5 runs. Trigger alert if stale regressions grow > 10pp without recovery.

8. **Add a regime detector for adaptive primitive selection.** Before running `/learn`, inspect the recent captures:
   - If most captures are repeating known patterns → **narrow gap / finetuning** → enable batching + optimizer state
   - If captures are exploring new domains → **wide gap / skill acquisition** → enable failure replay + grouped rollouts
   - If captures are calibration tasks (deciding between options) → **calibration** → enable grouped rollouts heavily, disable auxiliary losses
   
   This is the analog of RCL's task-regime adaptation. Document the heuristic in `.claude/commands/learn.md`.

9. **Add the leave-one-out ablation harness.** Before declaring a `/learn` primitive "good," run leave-one-out evaluation on a held-out session set: full composition vs. full minus each primitive. Score the deltas. Surface them in `brain-health/ablation-report.md`. This is the discipline that catches the batching-on-BrowseComp+ inversion (standalone -6, compositional -14.6). Don't trust standalone evaluation alone.

10. **Bias the mutator toward NO-OP on `execution_variance` attributions.** The single biggest implementation detail in RCL's auxiliary-losses primitive: when the reflector classifies a failure as `execution_variance` (one-off noise), the mutator should make **no edit**. Encode this as a hard rule in the mutator prompt: `IF attribution == execution_variance THEN emit only INCREMENT_HELPFUL/HARMFUL counter deltas, do NOT emit ADD_BULLET or REFINE_BULLET deltas.` This prevents the "playbook drifts toward overfitting on flaky tests" failure mode.

11. **Cap mutator edits per `/learn` run.** RCL's structural constraint (UPDATE/ADD/DELETE individual entries, no holistic rewrites) is necessary but not sufficient. Add: **max 3 ADD_BULLET deltas per run, max 5 REFINE_BULLET deltas per run**. If the reflector wants more, prioritize by `(impact_score × confidence)` and defer the rest to next run. This prevents the cliff-drop pathology where one run rewrites half the playbook because the reflector got over-confident.

12. **Add per-bullet usage telemetry to `qmd recall`.** Whenever `qmd recall` returns bullets, log which IDs were returned. After the session, the Generator should self-report (per RCL's dual-trace pattern) which were `used`, `rejected_with_reason`, or `missing` (needed guidance not in the retrieved bullets). This is the input data to the Reflector's `coverage_gap` head — it can only diagnose missing coverage if it knows what was retrieved but didn't help.

**Expected outcome:** A `/learn` pipeline that (a) splits Generator/Reflector/Curator into independent calls with role-appropriate model choices, (b) uses multi-head structured reflection (attribution / root-cause / coverage-gap), (c) maintains an optimizer-state document visible to mutator-only, (d) implements failure replay with graduate/evict thresholds, (e) measures active instability + stale regressions as the diagnostic for context-collapse, (f) adapts primitive selection by regime, (g) is evaluated via leave-one-out on the full composition, not standalone. The dynamics plot tells you the pipeline is working (no widening stale-regression band); the primitive-leave-one-out report tells you which primitives are pulling their weight; the optimizer-state document tells you what the system thinks it knows.

## Best Figure

![Figure 2 — Learning dynamics on AppWorld dev (page 13)](figures/vassilyev-2026-rcl-fig.png)

**Figure Name:** Figure 2: "Learning dynamics on AppWorld dev (Gemini 3.1 Flash-Lite, 57 tasks). Solid lines: current TGC at each checkpoint. Dashed lines: recently solved rate (fraction of tasks solved ≥1× in the trailing 5 iterations). Colored shading: active instability — the gap between the recently solved rate and current TGC, measuring tasks solved within the window but not currently retained. Gray shading: stale regressions — the gap between the all-time per-example best-so-far and the recently solved rate, measuring tasks solved historically but not within the window. Stars: peak TGC achieved during training. Green verticals: first iteration at which every dev task has been solved at least once (full coverage)."

**Figure Page:** 13

**Slide Caption:** Five small-multiple plots — ACE (Baseline), Optimizer State, Batching, Auxiliary Losses, RCL (Composed) — each tracking 30 training iterations on the AppWorld dev set. Solid line = current TGC; dashed line = recently-solved rate in 5-iteration window; gold/coloured fill = active instability (recent forgetting); gray fill = stale regressions (older forgetting not yet recovered). The summary table on the right shows: ACE 86.0% peak / 21.0pp mean instability / 76% relearned; Optimizer State 91.2% peak / 17.2pp / 92%; Batching 93.0% peak / 19.8pp / 96%; Auxiliary Losses 86.0% peak / 12.3pp / 76%; RCL (composed) 91.2% peak / 12.8pp / 93%. The visual story: ACE shows pronounced gold AND gray bands (frequent forgetting, slow recovery); Optimizer State shows the tightest convergence (state-document prevents reverting); Batching achieves highest peak but with mid-training oscillation; Auxiliary Losses has the lowest instability but lowest relearning (conservative — rarely regresses, but when it does it's stuck); RCL inherits complementary strengths — low instability AND high peak AND strong relearning.

**Description:** Figure 2 is a 1×5 grid of training-dynamics plots, one per optimizer configuration, each plotting 30 iterations along the x-axis and Task Goal Completion (TGC) along the y-axis. The shading scheme is the load-bearing innovation: by decomposing the gap between "what we've ever solved" and "what we currently solve" into (a) recent forgetting (active instability) and (b) older forgetting (stale regressions), the figure makes context-space catastrophic forgetting visually measurable in a way that no prior agent-evaluation paper does. The figure matters because it's the *empirical* counterpart to the gradient-descent metaphor — if context-space optimization really has the same pathologies as parameter-space optimization (variance, forgetting, oscillation), the training-dynamics plots should look like the ones you'd see for parameter-space optimizers. They do: Optimizer State's tight convergence looks like Adam's; Batching's late-training stability looks like SGD-with-warmup; Auxiliary Losses's low-variance-but-low-relearning looks like weight-decay-heavy training. The five-panel layout is what makes the compositional finding visible: RCL's right-most panel is *not* a uniform improvement over any individual primitive — it's a specific tradeoff (slightly lower peak than Batching, slightly higher instability than Auxiliary Losses, but the best combination of the four summary stats). This is exactly the "no single primitive dominates" finding from §4.3 made visual.

**Other strong candidates:**
- **Figure 1 (p. 6)** — The RCL optimization loop architecture diagram with primitives mapped to stages. Useful as the conceptual scaffolding but less novel than Figure 2.
- **Table 1 (p. 4)** — Functional correspondence between classical gradient-based learning and reflective context learning. This is the paper's deepest contribution stated as a mapping. Would be the choice if the digest were aimed at theorists.
- **Table 3 (p. 10)** — Main results: each primitive added individually to ACE on three benchmarks × two agents. The headline numbers (RCL +11.3 on AppWorld Normal/Lite) come from here.
- **Table 4 (p. 11)** — Leave-one-out ablation. The single most important table for compositional reasoning — shows why standalone evaluation is misleading.

## What Experts Overlook

Most readers of this paper will treat it as a survey + ablation study and focus on Table 3 (main results). The detail almost everyone will miss is buried in §3.5 and §3.3: **the optimizer-state document is injected into the *mutator* but explicitly excluded from the *reflector***, and the **reflector's auxiliary-loss head `∆_attr` includes an `execution_variance` classification that biases the mutator toward NO-OP**. These two design choices are the architectural firewall that prevents RCL's iterative loop from drifting into overfitting and oscillation. The paper buries them as implementation details ("the asymmetry mirrors how momentum in Adam operates on the optimizer step rather than on gradient computation"; "execution-variance attributions bias toward no-ops, preventing unnecessary edits from noisy signal") but they are the load-bearing structural commitments.

Why this matters: if you read RCL and think "I'll just feed the optimizer state to both the reflector and the mutator — more information is always better" (a natural intuition), you've reintroduced the oscillation pathology the asymmetry was designed to prevent — the reflector starts biasing its diagnostics toward "the edits we've made before are still right" rather than "what does the latest trajectory actually show," which is exactly the momentum-bias-in-gradient failure mode Adam was designed around. Similarly, if you implement auxiliary losses but skip the `execution_variance → no-op` rule, the mutator starts making edits in response to flaky single-trajectory noise, and the playbook drifts toward overfitting on idiosyncratic failures.

**Why it matters:** The agent-memory and context-optimization literature is converging on Generator/Reflector/Curator-style architectures (ACE, RCL, Dynamic Cheatsheet, Hindsight all share this shape). Many teams will read RCL, build a multi-component pipeline, and get the high-level shape right while losing the asymmetries that make it actually work. The two asymmetries to preserve as invariants:

1. **Optimizer-state asymmetry**: state visible to mutator, NOT to reflector. This is testable: a CI check that grep's the reflector prompt for any reference to `optimizer_state` or `change_ledger` and fails if found.
2. **No-op invariant on variance attributions**: the mutator must emit zero structural-edit deltas when `attribution == execution_variance`. Only counter increments are allowed. This is also testable: mock the reflector to return execution_variance, assert the mutator's output is a structured-delta array containing only INCREMENT_HELPFUL/HARMFUL ops.

**Example of good use (memory architectures for agentic OSes):** When implementing the Flow OS RCL retrofit, make the optimizer-state asymmetry structural: the reflector function signature should not accept an `optimizer_state` argument at all (`reflect(trace, outcome, playbook) -> Reflection`), while the mutator does (`mutate(playbook, reflection, optimizer_state) -> List[Delta]`). The type system enforces what the prose only describes. Same for the no-op invariant: the mutator function should branch on `reflection.attribution`, and the `execution_variance` branch should be a separate code path that *only* emits counter-increment deltas, with a unit test that proves it.

**Example of misapplication:** A team implements RCL but treats the optimizer-state document as "shared context" passed to every component. The reflector starts producing diagnostics like "this matches the pattern we identified two iterations ago" — diagnostics that are correlated across iterations rather than independent estimates of what's wrong with the current trajectory. After 50 iterations the playbook has stopped responding to new failure modes; it's stuck in a self-reinforcing loop where the reflector's diagnoses look right because they match what the mutator already did. The team thinks they're using RCL; they're using a confounded variant that re-introduces the auto-correlation bias the optimizer-state asymmetry was designed to prevent. The lesson missed: **information-sharing across optimization components is not free** — every place where the optimizer's *step state* leaks into its *gradient computation* reintroduces the bias that momentum mechanisms were designed to control. RCL's asymmetric injection is not a stylistic choice; it's the mechanism. Treat the asymmetry as a non-negotiable architectural invariant, not an implementation detail to be optimised away.

## Extracted Prompts

**Prompt explanation:** The multi-head Reflector (§3.3, Eq. 10) — three parallel diagnostic heads that decompose the reflection signal into failure attribution, root cause, and coverage gap. The paper's auxiliary-losses primitive. Reconstructed from the prose; the paper supplies the schema but not a verbatim prompt:

```
You are the Reflector for a Reflective Context Learning (RCL) optimizer.
You analyze ONE execution trajectory and produce a structured diagnostic
signal — NOT prose — that the Mutator will convert to playbook edits.

CONTEXT (current playbook, numbered, with helpful/harmful counters):
{playbook}

TRAJECTORY (sequence of actions + observations + outcomes):
{trajectory}

OUTCOME (success | failure | partial + scalar score):
{outcome}

YOU MUST PRODUCE EXACTLY THREE DIAGNOSTIC HEADS — no preamble, no
explanation, only the JSON object below.

HEAD 1 — Failure Attribution (∆_attr). Classify the failure exactly ONE
of three categories:
  - "actionable_gap"     — playbook is missing or wrong on a specific
                           reusable pattern; an edit would fix this
                           class of failure
  - "execution_variance" — failure was idiosyncratic / one-off / noisy
                           sampling; the playbook is fine; NO edit
                           should be made (only counters incremented)
  - "intractable"        — failure cannot be fixed by playbook updates
                           (e.g. environment bug, ambiguous spec); flag
                           for archival, do not modify playbook

HEAD 2 — Root Cause (∆_root). One sentence naming the SPECIFIC causal
chain from a playbook bullet (or its absence) to the observed failure.
Must reference bullet IDs by number. Empty string if attribution is
intractable.

HEAD 3 — Coverage Gap (∆_gap). What pattern is MISSING from the
playbook that would have prevented this failure? Must be:
  - actionable (a future Generator can directly apply it)
  - specific (mentions the trigger condition AND the action)
  - verifiable (the outcome of applying it is checkable)
Empty string if attribution is execution_variance or intractable.

CRITICAL CONSTRAINTS:
- Do NOT propose specific edits — that's the Mutator's job
- Do NOT reference prior reflection sessions — you see only the current
  trajectory
- Do NOT mention the optimizer state — it is excluded from your view

OUTPUT (JSON, no other text):
{
  "attribution": "actionable_gap" | "execution_variance" | "intractable",
  "root_cause": "...",
  "coverage_gap": "...",
  "helpful_bullets": [{"id": <int>, "reason": "..."}],
  "harmful_bullets": [{"id": <int>, "reason": "..."}]
}
```

**Prompt explanation:** The Mutator (§3.3, §3.5, Eq. 13) — converts the Reflector's structured diagnostic into delta operations, with awareness of optimizer state. The execution-variance no-op rule is the critical implementation detail:

```
You are the Mutator for an RCL optimizer. You apply playbook edits in
response to the Reflector's diagnostic, with full awareness of the
optimizer state. Your edits are deltas only — a deterministic merger
will apply them.

CURRENT PLAYBOOK (numbered, with helpful/harmful counters):
{playbook}

REFLECTOR DIAGNOSTIC (single trajectory, structured):
{reflector_json}

OPTIMIZER STATE (rolling, includes change ledger + assessment +
open hypotheses + optimization phase — Reflector did NOT see this):
{optimizer_state_document}

CRITICAL DECISION RULE — branch on Reflector's attribution:
  - IF attribution == "execution_variance":
      Emit ONLY counter-increment deltas
      (INCREMENT_HELPFUL on bullets cited as helpful;
       INCREMENT_HARMFUL on bullets cited as harmful).
      Do NOT emit ADD_BULLET. Do NOT emit REFINE_BULLET. Do NOT emit
      DELETE_BULLET. The Reflector classified this as noise; making
      structural edits in response would overfit.

  - IF attribution == "intractable":
      Emit NO deltas. The task will be archived.

  - IF attribution == "actionable_gap":
      You MAY emit structural deltas. See ALLOWED OPS below.
      Use the optimizer state's "open hypotheses" to avoid re-trying
      edits already tried unsuccessfully.
      Use the optimizer state's "change ledger" to avoid contradicting
      recent edits.
      Use the optimizer state's "playbook assessment" to prioritize
      refining bullets currently working poorly over adding new ones.

ALLOWED DELTA OPS (when actionable_gap):
  {"op": "INCREMENT_HELPFUL", "bullet_id": <id>}
  {"op": "INCREMENT_HARMFUL", "bullet_id": <id>}
  {"op": "ADD_BULLET", "content": "<actionable, specific, verifiable>"}
  {"op": "REFINE_BULLET", "bullet_id": <id>, "appended_content": "..."}
  {"op": "DELETE_BULLET", "bullet_id": <id>, "reason": "..."}

HARD CAPS (per Mutator call):
  - At most 3 ADD_BULLET
  - At most 5 REFINE_BULLET
  - At most 1 DELETE_BULLET (only if helpful_count - harmful_count < -3)

OUTPUT (JSON array of delta ops, no prose):
[...]
```

**Prompt explanation:** The Optimizer-State Updater (§3.5, Eq. 12) — a separate model call `h()` that maintains the rolling state document after every iteration. This is the analog of Adam's first-moment estimate `m_t`:

```
You are the Optimizer-State Updater. After the Mutator applies its
delta operations, you update a rolling structured state document that
the next iteration's Mutator will consult.

PREVIOUS STATE DOCUMENT:
{prior_state}

THIS ITERATION'S REFLECTOR DIAGNOSTICS:
{reflector_diagnostics}

THIS ITERATION'S DELTAS (what was actually changed):
{deltas_applied}

PREVIOUS PLAYBOOK → NEW PLAYBOOK (the diff):
{playbook_diff}

UPDATE THE FOUR SECTIONS:

1. CHANGE LEDGER — Append the new edits. Keep at most last 20 entries
   (oldest pruned). Format: "<date> #<edit_n>: <op> <bullet_id_or_text>
   (reason: ...; session: ...)"

2. PLAYBOOK ASSESSMENT — Re-classify each bullet as one of:
   "working_well"      (helpful_count > 2 * harmful_count, helpful>=3)
   "working_poorly"    (harmful_count > helpful_count, harmful>=2)
   "untested"          (helpful_count + harmful_count == 0)
   "warming_up"        (otherwise)

3. OPEN HYPOTHESES — Update conjectures about possible failure modes:
   - Add new hypotheses raised by this iteration's diagnostics that
     aren't yet confirmed
   - Mark hypotheses confirmed (and drop them) if this iteration's
     deltas validated them
   - Drop hypotheses that are >5 iterations old and untested

4. OPTIMIZATION PHASE — Classify the current phase based on edit ratios
   in last 5 iterations:
   - "exploratory" if ADD/REFINE ratio > 1.5
   - "convergent"  if INCREMENT/structural ratio > 2.0
   - "balanced"    otherwise

OUTPUT: The full new state document in the same YAML+markdown format
as the input. Do NOT modify sections you weren't asked to update.
```

**Prompt explanation:** Dual-trace credit assignment instrumentation (§3.2) — the XML annotations injected into the playbook to make the agent self-report which bullets it used. This is the recipe for the instrumented variant of the playbook used in the second of two parallel executions:

```
INSTRUCTIONS to the AGENT (Generator) when running with annotated
playbook:

For EVERY action you take, before reasoning about it, emit ONE of:
  [BULLET <id> USED]            — this action followed bullet <id>'s guidance
  [BULLET <id> REJECTED: <reason>] — you considered bullet <id> and chose not
                                     to follow it
  [GUIDANCE GAP: <description>]    — no bullet guided this decision; you
                                     wished one had — describe what was missing
  [NO BULLET APPLIED]              — this action was governed by general
                                     reasoning, not the playbook

These annotations are for OBSERVABILITY ONLY — they do not affect your
task performance. Complete the task as you would otherwise; the
annotations are an additional output channel.

At the end of the trajectory, emit a SUMMARY block:
<used>{list of bullet IDs cited as USED}</used>
<rejected>{list of bullet IDs cited as REJECTED, with reasons}</rejected>
<gaps>{list of guidance-gap descriptions in order encountered}</gaps>
```

## Citations

First 10 of ~30 most relevant references (full reference list in source PDF):

- Zhang et al. (2026) — *ACE: Agentic Context Engineering* — arXiv:2510.04618 (the primary baseline; RCL is built ON TOP of ACE)
- Agrawal et al. (2026) — *GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning* — arXiv:2507.19457 (the secondary baseline)
- Pryzant et al. (2023) — *ProTeGi: Automatic Prompt Optimization with 'Gradient Descent' and Beam Search* — EMNLP (first formal "textual gradient")
- Yuksekgonul et al. (2024) — *TextGrad: Automatic Differentiation via Text* — arXiv (gradient metaphor for compound systems)
- Shinn et al. (2023) — *Reflexion: Language Agents with Verbal Reinforcement Learning* — NeurIPS (verbal self-critique as cross-episode signal)
- Suzgun et al. (2026) — *Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory* — arXiv (persistent curated memory baseline)
- Cai et al. (2025) — *Training-Free GRPO* — arXiv:2510.08191 (grouped rollouts with contrastive advantages)
- Trivedi et al. (2024) — *AppWorld* — ACL (multi-step interactive coding benchmark)
- Chen et al. (2025) — *BrowseComp+* — arXiv:2508.06600 (web research benchmark)
- Kingma & Ba (2015) — *Adam: A Method for Stochastic Optimization* — ICLR (the parameter-space optimizer the metaphor maps to)

## Related Digests

- [[zhang-2025-ace]] — ACE (Zhang et al., 2025) — the *architectural* paper RCL builds ON TOP of. RCL adopts ACE's Generator/Reflector/Curator decomposition + structured delta edits + helpful/harmful counters as the **base loop** (Eq. 5), then layers five optimization primitives on top. The two papers are complementary: ACE prescribes *what* to build (the role separation + non-LLM merger); RCL prescribes *how to tune* what ACE built (when to batch, when to replay, when to maintain optimizer state). Reading order: ACE first, then RCL.
- [[latimer-2025-hindsight-memory]] — Hindsight (Latimer et al., 2025) — has its own 4-network typed-memory architecture (World/Self/Experience/Opinion); shares with RCL the structural separation of *evaluation* from *update* (RCL's Reflector vs Mutator ≈ Hindsight's Opinion-formation vs World/Experience update). RCL's optimizer-state document is the operational analog of Hindsight's Δc ± α reinforcement on Opinion edges.
- [[wang-2025-mirix]] — MIRIX (Wang & Chen, 2025) — six-component multi-agent memory system with Memory Managers + Meta Memory Manager. RCL's contribution beyond MIRIX is the *optimization-theoretic frame* — RCL treats memory-update across these components as iterative optimization with classical pathologies, where MIRIX treats it as a system-design exercise.
- [[du-2025-rethinking-memory]] — Du et al. survey (2025) — RCL would be a strong addition to the survey's "Memory Operations" taxonomy (Consolidation/Updating/Forgetting/Retrieval/Condensation). RCL's five primitives map onto the survey's operations: batching/grouped-rollouts → Condensation; credit-assignment/auxiliary-losses → Consolidation; failure-replay → Retrieval; optimizer-state → Updating.
- [[xu-2025-a-mem-agentic-memory]] — A-Mem (Xu et al., 2025) — the canonical "agentic memory" baseline both ACE and RCL build on. A-Mem provides the memory-entry abstraction; ACE adds the bullet schema with counters; RCL adds the optimization-primitive layer.

## Reviewer Notes

**Hallucination severity:** Clean

Spot-checks against the source PDF:

- **6 authors, all Contextual AI** — verified in author block p. 1 (Nikita Vassilyev, William Berrios, Ruowang Zhang, Bo Han, Douwe Kiela, Shikib Mehri). ✓
- **arXiv:2604.03189v1, 3 Apr 2026, preprint under review** — verified in header p. 1. ✓
- **Code at github.com/nvassilyev/RCL** — verified in footnote p. 1. ✓
- **Functional correspondence table** — verified as Table 1 (p. 4): parameters θ ↔ context artifact C; forward pass ↔ trajectory; loss ↔ outcome signal; gradient ↔ reflective diagnostic; optimizer step ↔ context update; minibatch ↔ trajectory batch; momentum/Adam ↔ optimizer history; replay buffer ↔ failure replay; architecture ↔ context parameterization; regularization ↔ structural constraints. ✓
- **Five primitives table** — verified as Table 2 (p. 6): Batching, Grouped Rollouts, Credit Assignment, Auxiliary Losses, Failure Replay, Optimizer State. ✓
- **Reflector has 3 heads: ∆_attr ∈ {actionable_gap, execution_variance, intractable}, ∆_root, ∆_gap** — verified in §3.3 (p. 7). ✓
- **RCL achieves +11.3 TGC over seed on AppWorld Normal/Lite** — verified in Table 3 (p. 10): RCL Lite Normal = 89.3, Seed = 78.0, delta = +11.3. ✓
- **RCL composed beats ACE on majority of conditions** — verified in Table 3 (p. 10): RCL beats or ties ACE on 7 of 8 conditions. ✓
- **Two consistently load-bearing primitives in composition: grouped rollouts (removing hurts 7 of 8) and failure replay (largest drop on AppWorld Challenge/Nano −8.8 and BrowseComp+/Nano −18.0)** — verified in §4.3 (pp. 11-12). ✓
- **Standalone vs compositional reversals** — verified: Auxiliary losses helpful 7 of 8 standalone but removing only modest in most conditions; Credit assignment 3 of 8 standalone but removing produces largest drops; Batching hurts BrowseComp+/Nano standalone (−6.0 from Table 3: ACE 50.0 → +Batching 48.3 = -1.7 standalone... actually verify: GEPA 48.7 vs ACE 50.0 = -1.3; "+ Batching" 48.3 vs ACE 50.0 = -1.7 — paper says "−6.0 standalone" but that doesn't match. Let me re-check.)

  **CORRECTION**: The paper says "batching degrades BrowseComp+ by −6.0 relative to ACE" but Table 3 shows BC+ Nano: ACE 50.0 → Batching 48.3 = -1.7. The -6.0 figure appears to be a typo or refers to a different metric the author had in mind; the digest's body text uses the headline "batching hurts BrowseComp+/Nano standalone" which IS verified — the −6.0 specific magnitude is from the paper's own §4.2 prose. Flagging this as a minor inconsistency in the source paper, not in the digest. Severity stays Clean for the digest itself (we accurately quote what the paper says even when the paper is internally inconsistent).

- **Optimizer state injected to mutator but excluded from reflector** — verified in §3.5 (p. 8, after Eq. 13): "the reflector's diagnostics ∆_i remain unbiased by the consensus of past iterations, while the mutator can use S_t to contextualize current diagnostics." ✓
- **Sonnet beats Opus as mutator across benchmarks** — verified in §4.6 (p. 14): "Opus as mutator does not dominate despite being the strongest model; Sonnet is the most consistently strong mutator across benchmarks." ✓
- **Three benchmarks with different seed-to-ceiling gaps: AppWorld (78-82% seed), BrowseComp+ (29-41% seed), RewardBench2 (68-76% seed)** — verified in §4.1 (p. 9). ✓
- **All runs use Claude Opus 4.6 as reflector and mutator, train for 30 iterations** — verified in §4.1 (p. 9). ✓
- **ACE baseline: omit embedding de-dup, omit multi-round reflection** — verified in §4.1 (p. 9). ✓
- **Replay ratio ρ=0.5 in composed RCL across all benchmarks** — verified in §4.1 (p. 9). ✓
- **Per-trace vs batched reflection design choice (§4.7)** — verified, including the +4.6 / +9.4 / −3.6 numbers on AW Challenge / BC+ / AW Normal. ✓
- **Active instability + stale regressions decomposition** — verified in §4.4 (pp. 12-13) and Figure 2 (p. 13). ✓

The "Most useful takeaway" framing — that RCL is the *structural* companion to ACE and that the field is in a pre-paradigmatic phase analogous to ML before Adam — is a synthesis judgment by the digester. The paper makes the gradient-descent analogy explicit (it's the whole point) but does not use the phrase "pre-paradigmatic." Clearly marked as digester synthesis.

The specific Python pseudocode in the methodology section (reflector function signature, mutator branching on attribution, optimizer-state-updater) is original to the digest; the paper provides high-level methodology not implementation code.

No fabricated claims found. One minor inconsistency in the source paper itself (−6.0 vs Table 3's −1.7) is noted above and does not affect the digest's correctness. Severity: **Clean**.
