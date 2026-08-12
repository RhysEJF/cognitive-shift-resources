---
corpus: agentic-memory
kind: paper-digest
slug: rafique-2026-clawvm
title: "ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents"
authors:
  - "Mofasshara Rafique"
  - "Laurent Bindschaedler"
year: 2026
publication_date: "2026-04"
venue: "EuroMLSys '26"
source_url: "https://arxiv.org/abs/2604.10352"
doi: "10.1145/3805621.3807648"
arxiv_id: "2604.10352"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Recurring \"forgot the protocol\", \"lost the plan\", and \"dirty state vanished on reset\" failures in long-running agents are not retrieval-quality problems — they are the absence of an OS-style virtual-memory contract at the harness layer, and once you install one (typed pages + minimum-fidelity invariants + multi-resolution representations + validated writeback at every lifecycle boundary) you go from 67.8 mean policy-controllable faults per workload to zero, with <50 microseconds of overhead per turn."
topics:
  - agent-memory
  - virtual-memory
  - context-management
  - compaction
  - lifecycle-management
  - residency-and-durability
  - writeback-protocol
  - fault-model
  - openclaw
  - agent-harness
tags:
  - paper
  - memory-architecture
  - virtual-memory
  - eviction-policy
  - eurosys-mlsys
  - engram-maintain
  - engram-encode
  - engram-ground
  - osr-replay-oracle
entities:
  - rafique-mofasshara
  - bindschaedler-laurent
  - mpi-sws
related_digests:
  - packer-2023-memgpt-os
  - adler-2026-storage-not-memory
  - latimer-2025-hindsight-memory
  - chhikara-2025-mem0
citations:
  - title: "Bug: Pre-compaction memory flush uses stale token counts, can be bypassed"
    authors: ["AmbitiousRealism2025"]
    year: 2026
    venue: "GitHub issue #5457, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/issues/5457"
    arxiv_id: null
  - title: "SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning"
    authors: ["Edward Y. Chang", "Longling Geng"]
    year: 2025
    venue: "Proceedings of the VLDB Endowment 18(12)"
    doi: "10.14778/3750601.3750611"
    url: null
    arxiv_id: null
  - title: "AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations"
    authors: ["Jiayang Cheng", "Dongyu Ru", "Lin Qiu", "Yiyang Li", "Xuezhi Cao", "Yangqiu Song", "Xunliang Cai"]
    year: 2026
    venue: "ICLR 2026"
    doi: null
    url: "https://openreview.net/forum?id=sfrVLzsmlf"
    arxiv_id: null
  - title: "Cognee — OpenClaw integration guide"
    authors: ["Cognee"]
    year: null
    venue: "Cognee documentation"
    doi: null
    url: "https://docs.cognee.ai/integrations/openclaw-integration"
    arxiv_id: null
  - title: "The Working Set Model for Program Behavior"
    authors: ["Peter J. Denning"]
    year: 1968
    venue: "Communications of the ACM 11(5)"
    doi: "10.1145/363095.363141"
    url: null
    arxiv_id: null
  - title: "Feature Request: Pre-prompt memory injection hook (message:before event)"
    authors: ["Dowser"]
    year: 2026
    venue: "GitHub issue #11910, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/issues/11910"
    arxiv_id: null
  - title: "[Bug] Pre-compaction memory flush prompt causes agents to overwrite existing memory files"
    authors: ["EmberCF"]
    year: 2026
    venue: "GitHub issue #6877, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/issues/6877"
    arxiv_id: null
  - title: "Your agent forgets everything after compaction. Here's a fix (open source, $0.10/month)"
    authors: ["gavlaahh"]
    year: 2026
    venue: "Reddit r/openclaw"
    doi: null
    url: "https://www.reddit.com/r/openclaw/comments/1r3nyro/your_agent_forgets_everything_after_compaction/"
    arxiv_id: null
  - title: "OpenClaw \"forgot\" to run a protocol that we agreed it would"
    authors: ["haymourt"]
    year: 2026
    venue: "Reddit r/AI_Agents"
    doi: null
    url: "https://www.reddit.com/r/AI_Agents/comments/1qxo8lw/openclaw_forgot_to_run_a_protocol_that_we_agreed/"
    arxiv_id: null
  - title: "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions (MemoryAgentBench)"
    authors: ["Yuanzhe Hu", "Yu Wang", "Julian McAuley"]
    year: 2026
    venue: "ICLR 2026"
    doi: null
    url: "https://openreview.net/forum?id=DT7JyQC3MR"
    arxiv_id: null
  - title: "RAGCache: Efficient Knowledge Caching for Retrieval-Augmented Generation"
    authors: ["Chao Jin", "Zili Zhang", "Xuanlin Jiang", "Fangyue Liu", "Shufan Liu", "Xuanzhe Liu", "Xin Jin"]
    year: 2025
    venue: "ACM Transactions on Computer Systems 44(1)"
    doi: "10.1145/3768628"
    url: null
    arxiv_id: "2404.12457"
  - title: "Memory OS of AI Agent"
    authors: ["Jiazheng Kang", "Mingming Ji", "Zhe Zhao", "Ting Bai"]
    year: 2025
    venue: "EMNLP 2025"
    doi: "10.18653/v1/2025.emnlp-main.1318"
    url: null
    arxiv_id: null
  - title: "MemOS: A Memory OS for AI System"
    authors: ["Zhiyu Li", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2507.03724"
    url: null
    arxiv_id: "2507.03724"
  - title: "fix(memory-flush): add softThresholdPercent for context-relative threshold"
    authors: ["Limitless2023"]
    year: 2026
    venue: "GitHub PR #17041, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/pull/17041"
    arxiv_id: null
  - title: "AgentBench: Evaluating LLMs as Agents"
    authors: ["Xiao Liu", "et al."]
    year: 2024
    venue: "ICLR 2024"
    doi: null
    url: null
    arxiv_id: "2308.03688"
  - title: "QMD - Query Markup Documents"
    authors: ["Tobias Lütke"]
    year: 2026
    venue: "GitHub repository"
    doi: null
    url: "https://github.com/tobi/qmd"
    arxiv_id: null
  - title: "Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "Mohit Bansal", "Francesco Barbieri", "Yuwei Fang"]
    year: 2024
    venue: "ACL 2024"
    doi: "10.18653/v1/2024.acl-long.747"
    url: null
    arxiv_id: "2402.17753"
  - title: "Memory flush uses stale token count, fires after compaction instead of before"
    authors: ["marcmeezy"]
    year: 2026
    venue: "GitHub issue #2397, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/issues/2397"
    arxiv_id: null
  - title: "AIOS: LLM Agent Operating System"
    authors: ["Kai Mei", "et al."]
    year: 2025
    venue: "COLM 2025"
    doi: null
    url: "https://openreview.net/forum?id=L4HHkCDz2x"
    arxiv_id: "2403.16971"
  - title: "Mem0 — OpenClaw integration guide"
    authors: ["Mem0"]
    year: null
    venue: "Mem0 documentation"
    doi: null
    url: "https://docs.mem0.ai/integrations/openclaw"
    arxiv_id: null
  - title: "Feature: Workspace-aware post-compaction bootstrap to prevent amnesia"
    authors: ["mmartoccia"]
    year: 2026
    venue: "GitHub issue #20225, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/issues/20225"
    arxiv_id: null
  - title: "Memory flush softThresholdTokens doesn't scale with context window size"
    authors: ["Moddy14"]
    year: 2026
    venue: "GitHub issue #17034, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/issues/17034"
    arxiv_id: null
  - title: "feat: workspace-aware post-compaction context"
    authors: ["nickjlamb"]
    year: 2026
    venue: "GitHub PR #20267, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/pull/20267"
    arxiv_id: null
  - title: "[Feature]: Memory flush on /new and /reset (pre-reset memory save)"
    authors: ["NullSense"]
    year: 2026
    venue: "GitHub issue #8185, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/issues/8185"
    arxiv_id: null
  - title: "OpenClaw Compaction documentation"
    authors: ["OpenClaw"]
    year: 2026
    venue: "OpenClaw Docs"
    doi: null
    url: "https://docs.openclaw.ai/concepts/compaction"
    arxiv_id: null
  - title: "OpenClaw Configuration Reference"
    authors: ["OpenClaw"]
    year: 2026
    venue: "OpenClaw Docs"
    doi: null
    url: "https://docs.openclaw.ai/gateway/configuration-reference"
    arxiv_id: null
  - title: "OpenClaw Context documentation"
    authors: ["OpenClaw"]
    year: 2026
    venue: "OpenClaw Docs"
    doi: null
    url: "https://docs.openclaw.ai/concepts/context"
    arxiv_id: null
  - title: "OpenClaw Memory Overview"
    authors: ["OpenClaw"]
    year: 2026
    venue: "OpenClaw Docs"
    doi: null
    url: "https://docs.openclaw.ai/concepts/memory"
    arxiv_id: null
  - title: "OpenClaw Session Management Deep Dive"
    authors: ["OpenClaw"]
    year: 2026
    venue: "OpenClaw Docs"
    doi: null
    url: "https://docs.openclaw.ai/reference/session-management-compaction"
    arxiv_id: null
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Charles Packer", "Sarah Wooders", "Kevin Lin", "Vivian Fang", "Shishir G. Patil", "Ion Stoica", "Joseph E. Gonzalez"]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2310.08560"
    url: null
    arxiv_id: "2310.08560"
  - title: "LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression"
    authors: ["Zhuoshi Pan", "et al."]
    year: 2024
    venue: "Findings of ACL 2024"
    doi: "10.18653/v1/2024.findings-acl.57"
    url: null
    arxiv_id: null
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    authors: ["Joon Sung Park", "Joseph C. O'Brien", "Carrie J. Cai", "Meredith Ringel Morris", "Percy Liang", "Michael S. Bernstein"]
    year: 2023
    venue: "UIST '23"
    doi: "10.1145/3586183.3606763"
    url: null
    arxiv_id: "2304.03442"
  - title: "NanoClaw"
    authors: ["Qwibit.ai"]
    year: 2026
    venue: "GitHub repository"
    doi: null
    url: "https://github.com/qwibitai/nanoclaw"
    arxiv_id: null
  - title: "OpenClaw Best Practices: What Actually Works After Running It Daily"
    authors: ["robdih"]
    year: 2026
    venue: "Reddit r/openclaw"
    doi: null
    url: "https://www.reddit.com/r/openclaw/comments/1r4t9q8/openclaw_best_practices_what_actually_works_after/"
    arxiv_id: null
  - title: "Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents"
    authors: ["Yiting Shen", "Kun Li", "Wei Zhou", "Songlin Hu"]
    year: 2026
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2601.19935"
    url: null
    arxiv_id: "2601.19935"
  - title: "PicoClaw"
    authors: ["Sipeed"]
    year: 2026
    venue: "GitHub repository"
    doi: null
    url: "https://github.com/sipeed/picoclaw"
    arxiv_id: null
  - title: "QMD memory_search silently returns empty in Discord guild channels"
    authors: ["Skipper-Assistant-1968"]
    year: 2026
    venue: "GitHub issue #10191, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/issues/10191"
    arxiv_id: null
  - title: "Cognitive Architectures for Language Agents (CoALA)"
    authors: ["Theodore R. Sumers", "Shunyu Yao", "Karthik R. Narasimhan", "Thomas L. Griffiths"]
    year: 2024
    venue: "TMLR"
    doi: null
    url: "https://openreview.net/forum?id=1i6ZCvflQJ"
    arxiv_id: "2309.02427"
  - title: "Feature: Post-compaction system event injection for context continuity"
    authors: ["theghostybot"]
    year: 2026
    venue: "GitHub issue #10524, openclaw/openclaw"
    doi: null
    url: "https://github.com/openclaw/openclaw/issues/10524"
    arxiv_id: null
  - title: "How I solved context loss in long-running Claude agent sessions (OpenClaw)"
    authors: ["These-Koala9672"]
    year: 2026
    venue: "Reddit r/ClaudeAI"
    doi: null
    url: "https://www.reddit.com/r/ClaudeAI/comments/1r351ho/how_i_solved_context_loss_in_longrunning_claude/"
    arxiv_id: null
  - title: "Text2Mem: A Unified Memory Operation Language for Memory Operating System"
    authors: ["Yi Wang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2509.11145"
    url: null
    arxiv_id: "2509.11145"
  - title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "Yuwei Zhang", "Kai-Wei Chang", "Dong Yu"]
    year: 2025
    venue: "ICLR 2025"
    doi: null
    url: null
    arxiv_id: "2410.10813"
  - title: "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments"
    authors: ["Tianbao Xie", "et al."]
    year: 2024
    venue: "NeurIPS 2024 Datasets and Benchmarks"
    doi: "10.52202/079017-1650"
    url: null
    arxiv_id: "2404.07972"
  - title: "A-Mem: Agentic Memory for LLM Agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "Hang Gao", "Juntao Tan", "Yongfeng Zhang"]
    year: 2025
    venue: "NeurIPS 2025"
    doi: null
    url: "https://openreview.net/forum?id=FiM0M8gcct"
    arxiv_id: "2502.12110"
  - title: "We Built Persistent Memory for OpenClaw (FKA Moltbot, ClawdBot) AI Agents"
    authors: ["Deshraj Yadav"]
    year: 2026
    venue: "Mem0 blog post"
    doi: null
    url: "https://mem0.ai/blog/mem0-memory-for-openclaw"
    arxiv_id: null
  - title: "ZeroClaw"
    authors: ["ZeroClaw Labs"]
    year: 2026
    venue: "GitHub repository"
    doi: null
    url: "https://github.com/zeroclaw-labs/zeroclaw"
    arxiv_id: null
  - title: "Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks"
    authors: ["Yuxiang Zhang", "Jiangming Shu", "Ye Ma", "Xueyuan Lin", "Shangxi Wu", "Jitao Sang"]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2510.12635"
    url: null
    arxiv_id: "2510.12635"
  - title: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
    authors: ["Shuyan Zhou", "et al."]
    year: 2024
    venue: "ICLR 2024"
    doi: null
    url: null
    arxiv_id: "2307.13854"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Architecture of a stateful tool-using agent with the ClawVM layer"
  page: 3
  image_path: "figures/rafique-2026-clawvm-fig.png"
---

# ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents

**Authors:** Mofasshara Rafique (Independent), Laurent Bindschaedler (MPI for Software Systems)
**Published:** 2026-04 · [Source](https://arxiv.org/abs/2604.10352)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

ClawVM is an OS-style virtual-memory layer that sits inside the agent harness (the layer that already assembles prompts, mediates tools, and observes lifecycle events like compaction and reset) and treats all assistant-relevant state as **typed pages** with **minimum-fidelity invariants**, **multi-resolution representations** under a token budget, and **validated, non-destructive writeback** at every lifecycle boundary. Each page can live at one of four levels — `full` → `compressed` (via LLMLingua-2) → `structured` (typed fields) → `pointer` (resolvable handle) — and is downgraded but never silently dropped below its declared minimum. A two-phase deterministic policy first installs all hard-pinned/minimum-required pages, then greedily upgrades by marginal utility-per-token until the budget is exhausted. A WritebackJournal three-phase protocol (structured staging → deterministic validation → scoped commit with deterministic merge) replaces the "free-form flush prompt that overwrites memory.md" failure mode. Across four synthetic workload families × six token budgets (120–500), 12 real Claude Code session traces (100 and 200 turn truncations), 30 task-level replays, and three adversarial stress tests (starvation, churn, cascade reset), ClawVM **eliminates 100% of policy-controllable faults** — going from 67.8 mean faults per workload-budget (retrieval-only) and 1.5 (best practitioner-configured compaction+retrieval) to **zero** — confirmed against an offline 3-turn-horizon oracle that proves zero remaining headroom. Median policy overhead is <50 µs per turn, peak memory <83 KB, prototype is 1,300 lines of Python with zero external dependencies.

## Key Takeaway

Recurring "forgot the protocol", "lost the plan", and "dirty state vanished on reset" failures in long-running agents are not retrieval-quality problems — they are the absence of an OS-style virtual-memory contract at the harness layer, and once you install one (typed pages + minimum-fidelity invariants + multi-resolution representations + validated writeback at every lifecycle boundary) you go from 67.8 mean policy-controllable faults per workload to zero, with <50 microseconds of overhead per turn. The "harness is the kernel" claim is load-bearing: only the harness sees session lifecycle events, prompt assembly, and tool mediation simultaneously, so it is the **only** layer where residency and durability can be made deterministic rather than best-effort. External memory plugins (Mem0, Cognee, QMD, the authors' own ecosystem) sit one layer up and cannot create the contract — they are orthogonal recall-quality improvements, not enforcement.

## Implications

**Mapped to ENGRAM dimensions** — the six interacting decisions every memory architecture makes:

- **E — Encode (Capture).** ClawVM converts capture from optional/discretionary to **policy-driven**: for designated state, the harness drives capture, not the model. Pre-extraction of multi-resolution variants happens at page creation/update time, not on demand under budget pressure — this is a deliberate move of write-time work off the hot path (no runtime LLM calls or compression passes inside selection). Implication for memory-architect work: any system that defers extraction to query time pays a residency-decision-time tax in tokens or wall-clock; ClawVM pays it once up front.
- **N — Network (Shape).** Memory is a **typed page table** with six page classes (Bootstrap/Policy, Constraint, Plan, Preference, Evidence, Conversation Segment), each with declared scope (project/shared vs. session-private), provenance (originating tool call or transcript span), and a minimum-fidelity floor. This is a **polyglot stack**: SessionPageTable + RepresentationSelector + WritebackJournal + FaultObserver + DecisionTrace (JSON-lines audit log) + ClawVMEngine, with pluggable adapters that normalize external stores (workspace files, hybrid retrieval, Mem0/Cognee/QMD) into pages. The contract is retrieval-agnostic — you can swap the underlying retriever without changing the contract.
- **G — Ground (Trust).** **Provenance is first-class metadata, required for observability and safe writeback.** The validation phase rejects any update whose `evidence_ref` does not resolve (dangling provenance → reject), any non-append/merge/set-with-version op (destructive overwrite → reject with `DESTRUCTIVE_OP` reason code), and any out-of-scope write (`SCOPE_DENIED`). This is the strongest treatment of provenance in the wiki so far — *Storage Is Not Memory* argued for retention of source; ClawVM operationalizes it as a hard precondition for commit.
- **R — Retrieve (Recall).** Recall becomes **observable**: the runtime distinguishes "no match", "denied", and "backend error" via explicit reason codes — closing the silent-recall-fault class. The selection policy itself is a **multi-choice knapsack with hard constraints**, deterministically resolved with explicit tie-breaks by (page_id, rep_level). Ranking is hybrid (pin status + bootstrap/plan membership + recency + scope + recompute cost) but the structural safety is independent of ranking — an LRU baseline keeping the same structural features (pinning, writeback, prefetch, pointer resolution) achieves identical zero faults and identical thrash (0.901). Utility scoring is for *quality above the fault-free floor*, not for safety.
- **A — Aggregate (Consolidation).** ClawVM explicitly **does not consolidate**. Pages degrade in fidelity but retain identity and provenance — there is no abstraction/pattern-extraction step. This is a *deliberate non-choice*: the authors locate semantic synthesis (and its associated hallucination risk) outside their contract, arguing "the model can produce a well-formed, properly scoped update that is factually wrong; semantic verification could be layered on via domain-specific validation predicates on the writeback journal" (Section 7). Architects designing for compound learning need to bolt aggregation on top — ClawVM is the substrate.
- **M — Maintain (Lifecycle).** This is ClawVM's home dimension. Every lifecycle event (compaction, pruning, memory flush, reset/save) is a **page-replacement decision** that the harness owns. Durability is "lifecycle-complete": dirty state commits at every boundary where the runtime would otherwise destroy the only copy. Writeback is **three-phase** (structured staging → deterministic validation → scoped commit with deterministic merge rules), and rejected updates remain in the journal with reason codes for diagnosis.

**Cross-dimensional interactions worth noting:**

- **Encode ↔ Maintain.** Pre-computing all four representation levels at page-creation time (rather than on demand) trades one-time encode cost for deterministic, LLM-free selection at maintenance/lifecycle decision time. This is a hard architectural commitment — it would not work if pages were heterogeneous in compression cost or if upstream content drifted.
- **Network ↔ Ground.** Typing pages by class lets the minimum-fidelity invariant differ per class (Bootstrap can degrade to structured but never below; Constraint is hard-pinned at structured; Plan keeps goal + current step at minimum; Preference may degrade to pointer). Without the typed-page network, you cannot express the trust invariant cleanly.
- **Retrieve ↔ Maintain.** The fault model (refetch, duplicate-tool, pinned-invariant-miss, post-compaction bootstrap, silent-recall, flush-miss) is the bridge — these are not recall failures *or* lifecycle failures, they are paging failures that span both, and naming them is what lets the system be diagnosable.

**For Flow OS and similar memory layers:** the paper is a direct prescription. The "central /learn-only writes" rule in CLAUDE.md is structurally equivalent to ClawVM's "capture is policy, not discretion." The dedup-via-QMD step in `/learn` is an ad-hoc form of validated writeback. What Flow OS lacks: typed page classes with minimum-fidelity invariants, an explicit fault model with reason codes, and lifecycle-boundary commit guarantees. Adopting even the page-class + fault-model vocabulary would make Flow's failures diagnosable rather than anecdotal.

## How to Apply It (method)

The full implementation is a 1,300-line Python prototype in six modules (zero external dependencies), with code at https://github.com/mpi-dsg/clawvm. The reproducible recipe:

1. **Identify lifecycle hooks in your harness.** ClawVM requires six engine operations exposed by the harness: session-start, prompt-assemble, post-model, tool-execute, compaction, reset. If your harness does not surface these as named events, retrofit them — without lifecycle visibility, residency and durability cannot be made deterministic.
2. **Define your page classes.** Start from the six in Table 1 — Bootstrap/Policy, Constraint, Plan, Preference, Evidence, Conversation Segment — and decide a minimum-fidelity floor for each (e.g., Constraint = hard-pinned at structured; Plan = goal + current step). Tag each page with scope (project-shared vs. session-private) and provenance (originating tool call or transcript span). Provenance is mandatory, not optional.
3. **Pre-compute multi-resolution variants at write time.** At page ingestion/update, generate all four representations: `full` (verbatim), `compressed` (token-reduced text via LLMLingua-2 or equivalent), `structured` (typed fields satisfying the invariant), `pointer` (resolvable handle + minimal metadata). Do this once, store all variants — never recompute at selection time.
4. **Implement the deterministic two-phase prompt-assembly policy** (Listing 1):
   - Phase 1: install fixed region (system prompt, schemas) + `minimumRequired(candidates)` for all hard-pinned/minimum pages. If the minimum-required set does not fit, surface a *pinned-invariant-miss* fault — this is physical insufficiency, not policy failure.
   - Phase 2: rank all candidate upgrades by `ΔUtility(u) / ΔTokens(u)` descending; greedily apply each upgrade that fits the remaining budget, respects invariants, and conflicts with no other upgrade. Tie-break deterministically by `(page_id, rep_level)`.
   - Utility function: `U_t(p, r) = w_pin · I_pin + w_boot · I_boot + w_plan · I_plan + w_rec · R_t + w_scope · S + w_rc · C`. Reference weights: pin boost (2.0 hard, 0.6 soft), recency 0.6, recompute cost 0.4. Weight sweep (84 runs) showed all configurations within `pin ∈ [0.5, 4.0]`, `recency ∈ [0.1, 1.2]`, `recompute cost ∈ [0.0, 1.2]` produce identical fault counts — *the structural constraints are what eliminate faults, the weights only sort quality above the floor*.
5. **Implement the three-phase validated writeback protocol:**
   - Phase 1 (structured staging): at eviction/downgrade/lifecycle hooks, the harness requests only typed `(field, op, value, scope, evidence_ref)` tuples with ops drawn from `{append, merge, set-with-version}`. Append to a WritebackJournal but do not apply.
   - Phase 2 (deterministic validation): check schema correctness, provenance resolvability, scope permission, non-destructive semantics (set-with-version requires staged version == last committed version `v_k`, else reject as `DESTRUCTIVE_OP`), and policy/safety. Rejected updates stay in the journal with reason codes (e.g., `SCOPE_DENIED`).
   - Phase 3 (scoped commit): validated updates commit via deterministic merge rules at logged commit points.
6. **Stand up the fault observer.** Define six observable faults: `refetch`, `duplicate-tool`, `pinned-invariant-miss`, `post-compaction-bootstrap`, `silent-recall`, `flush-miss`. Emit these as structured events to a JSON-lines `DecisionTrace`. These are the *policy-controllable* faults — physical insufficiency (token budget too small for all pins) and semantic correctness (model produces well-formed but wrong updates) are out of scope and must be evaluated separately.
7. **Validate with the six-test Tier-1 regression gate** (Table 3): post-compaction bootstrap, reset dirty-page flush miss, threshold-jump race, silent recall visibility, unsafe persistence rejection, evidence churn duplicate tool. Each must trigger the expected fault or rejection with the correct reason code.
8. **Run replay-oracle analysis to separate policy quality from budget insufficiency.** Given a trace + budget, an oracle with bounded future knowledge picks representations minimizing faults; the *oracle gap* (online − oracle fault counts) measures unavoidable workload pressure. If your gap is non-zero, the workload is starved at that budget — no policy can help. ClawVM matches the 3-turn-horizon oracle on fault count.

Adapters normalize external sources (workspace files, transcript indexes, hybrid retrieval, QMD/Mem0/Cognee) into pages — the contract is retrieval-agnostic, so you can swap in any backend.

## Best Figure

![Figure 1 — Architecture of a stateful tool-using agent with the ClawVM layer (page 3)](figures/rafique-2026-clawvm-fig.png)

**Image Candidates:**
- **Figure 1 (p. 3)**: Architecture diagram of harness + ClawVM layer + durable stores, with field-report failure points (a/b/c) annotated directly on the dataflow — telegraphs the entire paper in one glance.
- **Table 4 (p. 5)**: Aggregate fault reductions vs. three baselines averaged over 24 configurations — the headline result, but a flat table.
- **Table 6 (p. 5)**: Subtractive ablation showing pointer resolution removal causes 126 faults while removing utility-scoring causes 0 — the surgical evidence that *structure*, not *tuning*, is what eliminates faults.

**Best Image — Figure 1: "Architecture of a stateful tool-using agent with the ClawVM layer"**

Slide caption: *ClawVM interposes a virtual-memory contract (page table, representation selector, fault observer, writeback journal) between the agent harness and durable stores; failure points from public field reports are annotated directly on the dataflow.*

This figure carries the full argument in one panel. The Agent Harness box (top) shows the conventional pieces — Session Manager, Prompt Assembler, Tool Mediator, plus lifecycle events (Compaction, Pruning, Memory Flush, Reset/Save). The shaded ClawVMLayer underneath shows the four enforcement components and the dashed lines that connect each lifecycle event to the journal — making explicit that lifecycle boundaries are write barriers. The Context Window on the right shows the four fidelity tiers as colored boxes (full/compressed/structured/ptr) stacking against the token budget. Most importantly, three letters (a/b/c) point at the exact dataflow positions where field reports document failures: (a) bootstrap loss after Compaction, (b) flush miss at Reset/Save, (c) corrupt write into the durable stores. The picture says "we know where it breaks; here is the layer that intercepts each break."

## What Experts Overlook

Five things a memory-architecture practitioner reading this paper might miss or under-weight:

1. **The harness, not the model, is the kernel.** Most agent-memory literature debates *model-driven* vs *runtime-driven* paging (MemGPT vs A-MEM vs Memory-as-Action). ClawVM's framing — "structurally, the harness is an OS kernel for agent state: it controls what stays resident and when state becomes durable" — re-locates the design conversation. The model is the *workload*; the harness is the *runtime*. A model-driven pager (MemGPT, Memory-as-Action) is compatible with ClawVM but composable inside it, not an alternative. The paper says this explicitly: "a MemGPT-style model could serve as the paging heuristic inside ClawVM's enforcement layer." Most "agent memory" papers conflate these layers.
2. **Utility weights are decoupled from safety — surprisingly so.** The weight-sensitivity sweep (Section 5.2) shows *all 84 configurations* across wide ranges of pin/recency/recompute-cost weights produce **identical** fault counts and **identical** thrash (0.901). The LRU baseline (recency only, no utility scoring) keeps the same structural features and also achieves zero faults. The architectural claim — "fault elimination is robust by construction" — is the headline, but the practical implication is that *practitioners spend their tuning budget in the wrong place*. Hyperparameter sweeps on memory weights are wasted motion once the structural primitives (hard pinning, lifecycle writeback, pointer resolution) are in place. Direct any tuning effort at the page-class minimum-fidelity floors instead.
3. **Multi-resolution representations are pre-computed, not on-demand.** Easy to miss in the design section: "Representations are generated at page creation time, not on demand under budget pressure." This is what makes selection an O(table-lookup + token-arithmetic) operation rather than O(call-LLM-to-compress). It also means stale representations: if the underlying source changes, you must re-encode. This is a hard architectural commitment with consequences for systems where pages mutate frequently (e.g., active plans).
4. **"Capture is optional, recall is optional, compaction is destructive" — diagnosis as design.** Buried in Section 2: the three root causes derived from public issue trackers. This three-word diagnosis is the cleanest framing of why best-effort agent memory fails, anywhere in the wiki so far. It is a *better* problem statement than the solution it motivates. Memorize it; quote it.
5. **The semantic-correctness gap is explicit and unaddressed by design.** Section 7 (Limitations): "a model can produce a well-formed, properly scoped update that is factually wrong." ClawVM validates schema, provenance, scope, non-destructiveness — *not* truth. Authors flag this as future work via "domain-specific validation predicates on the writeback journal." This is the same boundary *Storage Is Not Memory* hits from the other side (write-time intelligence is anti-intelligence) — the wiki's open question is whether semantic verification belongs in the writeback layer at all, or one layer up.

One thing the paper itself **does not** claim but a careful reader should not overlook: the live-hook validation (Table 11) is only 20 single-session tasks, and the authors note "the live experiment confirms hook correctness but exercises only single-session execution; cross-session lifecycle edges (compaction, reset) remain replay-validated only." The headline numbers are *replay-validated*, not online. Anyone planning to deploy must extend the validation themselves.

## Extracted Prompts

The paper does not publish LLM prompts in the traditional sense — its enforcement is *pre-LLM*, structural. The closest analogues are pseudo-code listings and structured-protocol specifications that any implementer would translate into harness code:

**Listing 1 — Deterministic multi-resolution prompt assembly** (the policy itself, in pseudo-code; the "prompt" is the assembled context window):

```
function assemblePrompt(session, candidates, budget):
    prompt    <- fixedRegion(session)
    prompt    <- prompt + minimumRequired(candidates)
    remaining <- budget - tokens(prompt)

    upgrades  <- allRepresentationUpgrades(candidates)
    sort upgrades by (deltaUtility(u) / deltaTokens(u)) descending

    for u in upgrades:
        if deltaTokens(u) <= remaining
           and respectsInvariants(u)
           and noConflict(u):
            applyUpgrade(prompt, u)
            remaining <- remaining - deltaTokens(u)

    return prompt
```

**Three-phase writeback protocol** (the "prompt" the harness uses to talk to its journal):

```
Phase 1 — structured staging:
    Harness requests typed updates only:
        (field, op, value, scope, evidence_ref)
    where op ∈ {append, merge, set-with-version}.
    Append to WritebackJournal; do not apply.

Phase 2 — deterministic validation, five invariants:
    (1) Schema correctness  (fields, types, sizes)
    (2) Provenance          (evidence_ref resolves; reject dangling)
    (3) Scope               (allowed for active principal/session)
    (4) Non-destructive     (no overwrite of committed content;
                            set-with-version requires staged_v == v_k,
                            else reject as DESTRUCTIVE_OP)
    (5) Policy / safety     (no hard-pin violation)
    Rejected updates remain in journal with reason codes
        (e.g. SCOPE_DENIED, DESTRUCTIVE_OP).

Phase 3 — scoped commit:
    Validated updates commit via deterministic merge rules
    at explicit, logged commit points.
```

**Reason-code vocabulary** for observable faults — six labels that should be adopted verbatim by any agent memory system claiming diagnosability: `refetch`, `duplicate-tool`, `pinned-invariant-miss`, `post-compaction-bootstrap`, `silent-recall`, `flush-miss`. (Plus rejection codes `DESTRUCTIVE_OP`, `SCOPE_DENIED`.)

**Utility function** for ranking upgrades:

```
U_t(p, r) = w_pin · I_pin(p)
          + w_boot · I_boot(p)
          + w_plan · I_plan(p, t)
          + w_rec  · R_t(p)
          + w_scope · S(p)
          + w_rc   · C(p, r)

Reference weights: w_pin = 2.0 (hard) / 0.6 (soft),
                   w_rec = 0.6,
                   w_rc  = 0.4
Rank by:           s(u) = ΔU_t(u) / Δtokens(u)
Tie-break:         (page_id, rep_level)
```

## Citations

49 references extracted (full structured JSON in the frontmatter `citations:` block). Highlights — the citations a memory-architect should chase next:

- [[packer-2023-memgpt-os]] — MemGPT, the explicit predecessor; ClawVM frames it as the model-driven paging baseline it composes with rather than replaces.
- **MemOS: A Memory OS for AI System** (Zhiyu Li et al., 2025, arXiv:2507.03724) — sibling abstraction targeting representation-and-evolution unification across memory types; orthogonal to ClawVM's enforcement angle.
- **Memory OS of AI Agent** (Kang et al., 2025, EMNLP) — OS-inspired hierarchical storage with segmented page organization; closer to ClawVM in spirit but does not enforce a contract.
- **SagaLLM** (Chang & Geng, 2025, VLDB) — Saga-style transaction guarantees for multi-agent LLM planning; the transaction angle ClawVM cites as a sibling primitive.
- **A-Mem** (Xu et al., 2025, NeurIPS) — Zettelkasten-style dynamic memory network; the deliberately-not-paging alternative.
- **Memory as Action** (Zhang et al., 2025, arXiv:2510.12635) — model-driven paging; ClawVM positions it as a composable inner heuristic.
- **CoALA** (Sumers et al., 2024, TMLR) — what memory an agent *should have*; ClawVM addresses how the harness enforces that the memory survives lifecycle transitions.
- **LongMemEval** (Wu et al., 2025, ICLR) and **LoCoMo** (Maharana et al., 2024, ACL) — the long-conversation benchmarks the field uses; ClawVM does not score on them because it explicitly measures *structural* not *semantic* outcomes.
- **MemoryAgentBench** (Hu et al., 2026, ICLR), **AMemGym** (Cheng et al., 2026, ICLR), **Mem2ActBench** (Shen et al., 2026, arXiv:2601.19935) — the new wave of memory-specific benchmarks.
- **LLMLingua-2** (Pan et al., 2024, ACL Findings) — the compression engine ClawVM cites as its `compressed` representation generator.
- **Denning 1968** (Working Set Model, CACM) — the load-bearing OS citation; the thrash index is `F/(H+1)` from this lineage.
- **18+ OpenClaw issue tracker citations** (refs [1], [7], [9], [14], [18], [21–24], [37], [39], [40] and several more) — the field-report corpus the paper derives its three failure classes from. Worth grepping for the exact issue titles to see the *language* practitioners use; the paper's diagnosis is excellent at translating community pain into named fault classes.

(Full structured JSON in frontmatter `citations:` block — ready for `/citation-walk`.)

## Related Digests

- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems — the explicit predecessor; ClawVM composes with model-driven paging rather than replacing it.
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory — orthogonal lens on the same gap: ClawVM enforces residency/durability, Adler argues against premature distillation; both reject write-time lossy collapse.
- [[latimer-2025-hindsight-memory]] — Hindsight Is 20/20: Retain/Recall/Reflect — typed-memory networks operating at one layer above ClawVM's contract; the consolidation/aggregation layer ClawVM deliberately leaves out.
- [[chhikara-2025-mem0]] — Mem0: Production-Ready Long-Term Memory — an external memory plugin of exactly the kind ClawVM's adapter layer wraps; cited directly in the paper as an example of the orthogonal recall-quality layer.

## Reviewer Notes

**Severity: Clean.** Spot-checks against the paper text:

- "67.8 mean policy-controllable faults per workload-budget" → §1 abstract and §5.1 Table 4 confirm: retrieval baseline = 67.8 mean explicit faults, ClawVM = 0.0, Comp-Hybrid = 1.5.
- "<50 µs of policy-engine overhead per turn" → §1 abstract states "adds median <50 µs of policy-engine overhead per turn"; §5.3 final paragraph refines to "median 18–44 µs per turn (p95 <60 µs, worst-case 114 µs), excluding model and tool latency, and <83 KB peak memory" — both numbers used in the digest are present in the paper.
- "12 real Claude Code session traces" → §5.3 "12 trace-derived replay workloads from real Claude Code sessions" — exact phrasing preserved.
- "4 representation levels: full / compressed / structured / pointer" → §3 Multi-resolution residency paragraph — verbatim.
- "1,300 lines of Python, zero external dependencies, 6 modules" → §4 Implementation: "six Python modules (~1,300 lines of non-comment code, zero external dependencies)" — confirmed.
- LRU baseline equivalence claim → §5.2 LRU baseline paragraph confirms identical fault counts and thrash at budget 180.
- The "harness is an OS kernel for agent state" quote → §1 paragraph 4, verbatim.
- Six page classes (Bootstrap, Constraint, Plan, Preference, Evidence, Conversation Segment) → §3 Table 1 and surrounding text — confirmed; minimum-fidelity floors and degradation paths reproduced accurately.
- Three failure classes diagnosis ("capture is optional, recall is optional, compaction is destructive") → §2 final paragraph, refs [28, 34, 45] — verbatim.

No fabricated claims. One minor framing note (not a hallucination): the digest's ENGRAM mapping is the lens's analytic overlay, not the paper's own framing — flagged in-text as "Mapped to ENGRAM dimensions". The paper itself does not use ENGRAM vocabulary; the mapping is the reviewer-architect's contribution.

Citation extraction: all 48 numbered references in the paper bibliography preserved (some condensed in the body summary); OpenClaw issue-tracker URLs reproduced with full GitHub paths and dates as given. The arxiv ID `2604.10352` is faithfully recorded but is an unusually high-numbered ID — the paper is dated April 2026 so this is consistent with arXiv's monotonic numbering at that date.
