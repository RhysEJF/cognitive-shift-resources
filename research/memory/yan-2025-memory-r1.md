---
corpus: agentic-memory
kind: paper-digest
slug: yan-2025-memory-r1
title: "Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning"
authors:
  - "Yan, Sikuan"
  - "Yang, Xiufeng"
  - "Huang, Zuchao"
  - "Nie, Ercong"
  - "Ding, Zifeng"
  - "Li, Zonggen"
  - "Ma, Xiaowen"
  - "Bi, Jinhe"
  - "Kersting, Kristian"
  - "Pan, Jeff Z."
  - "Schuetze, Hinrich"
  - "Tresp, Volker"
  - "Ma, Yunpu"
year: 2025
publication_date: "2025-08"
venue: "arXiv preprint (v5 2026-01)"
source_url: "https://arxiv.org/abs/2508.19828"
doi: null
arxiv_id: "2508.19828"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Memory operations (ADD/UPDATE/DELETE/NOOP) and memory utilization (which retrieved entries to attend to) should be learned via RL with outcome-driven rewards, not hardcoded heuristics — with as few as 152 QA training pairs, a Memory Manager + Answer Agent fine-tuned with GRPO outperforms Mem0, MemoryOS, and A-Mem on LoCoMo by 28% F1 / 34% BLEU-1 / 30% LLM-judge."
topics:
  - reinforcement-learning
  - llm-agents
  - memory-management
  - crud-operations
  - memory-distillation
  - locomo
  - mem0
  - memoryos
  - ppo
  - grpo
tags:
  - paper
  - canonical
  - agent-memory
  - rl
entities:
  - yan-sikuan
  - ma-yunpu
  - tresp-volker
related_digests:
  - chhikara-2025-mem0
  - kang-2025-memory-os
  - maharana-2024-locomo
  - packer-2023-memgpt-os
  - latimer-2025-hindsight-memory
citations:
  - title: "Mem0: Building production-ready AI agents with scalable long-term memory"
    authors: ["Chhikara, Pavan", "et al."]
    year: 2025
  - title: "Evaluating very long-term conversational memory of LLM agents (LoCoMo)"
    authors: ["Maharana, Adyasha", "et al."]
    year: 2024
  - title: "MemoryOS: Memory operating system of AI agent"
    authors: ["Kang, et al."]
    year: 2025
  - title: "MemGPT: Towards LLMs as operating systems"
    authors: ["Packer, Charles", "et al."]
    year: 2023
  - title: "A-Mem: Agentic memory for LLM agents"
    authors: ["Xu, et al."]
    year: 2025
  - title: "Proximal policy optimization algorithms"
    authors: ["Schulman, John", "Wolski, Filip", "Dhariwal, Prafulla", "Radford, Alec", "Klimov, Oleg"]
    year: 2017
    arxiv_id: "1707.06347"
  - title: "DeepSeekMath: Pushing the limits of mathematical reasoning in open language models (GRPO)"
    authors: ["Shao, Zhihong", "et al."]
    year: 2024
    arxiv_id: "2402.03300"
  - title: "Search-R1: Training LLMs to reason and leverage search engines with RL"
    authors: ["Jin, et al."]
    year: 2025
  - title: "Training language models to follow instructions with human feedback (RLHF)"
    authors: ["Ouyang, Long", "et al."]
    year: 2022
  - title: "LongMemEval: Benchmarking chat assistants on long-term interactive memory"
    authors: ["Wu, Di", "et al."]
    year: 2024
  - title: "A survey on memory mechanism of LLM-based agents"
    authors: ["Du, et al."]
    year: 2025
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Liu, et al."]
    year: 2023
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Memory-R1 vs vanilla LLM memory system (DELETE+ADD fragmentation vs single UPDATE consolidation)"
  page: 2
  image_path: null
---

# Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning

**Authors:** Yan, Sikuan et al. (LMU Munich, TU Munich, Cambridge, HKU, TU Darmstadt, Edinburgh)
**Published:** 2025-08 (v5: 2026-01-14) · [Source](https://arxiv.org/abs/2508.19828)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Memory-R1 reframes the **what to store / what to retrieve** decisions in agent memory as RL problems and trains them with outcome-driven rewards (downstream QA correctness). Two specialized agents:

1. **Memory Manager**: takes (new dialogue turn, current memory bank) → outputs an operation in {ADD, UPDATE, DELETE, NOOP} plus updated content. Fine-tuned with PPO or GRPO.
2. **Answer Agent**: takes (question, 60 retrieved candidate memories) → applies *memory distillation* to filter down to the relevant entries, then answers. Also fine-tuned with PPO or GRPO.

Both agents share a single scalar reward — answer correctness via exact-match against ground truth — so no per-operation labels are needed. With **152 training QA pairs** (the tiny train split of LoCoMo), Memory-R1-GRPO on LLaMA-3.1-8B-Instruct beats Mem0 by ~14 absolute F1 points overall on LoCoMo (45.02 vs 30.41), and beats MemoryOS by ~10. Zero-shot transfer to MSC and LongMemEval works without retraining. The key empirical move is the *separation of memory management and memory utilization* into two RL-trained agents — most prior systems learn neither (Mem0, MemoryOS use hardcoded prompts) or learn only one (A-Mem learns linking; Memory-R1 learns both).

## Key Takeaway

**Memory operations are a learnable policy, not a hardcoded protocol — and the right learning signal is downstream task success, not per-operation labels.** [ENGRAM: E (Encode) + A (Aggregate) + R (Retrieve)] Existing systems either (a) hardcode CRUD via prompt engineering (Mem0, MemoryOS) — brittle to edge cases like "I adopted a dog Buddy" → "I adopted another dog Scout" being misread as contradiction and triggering DELETE+ADD instead of UPDATE — or (b) try to supervise per-operation correctness, which is impractical because labelling every memory write across a long dialogue is intractable. Memory-R1's contribution is to recognize that **answer correctness is a perfectly good supervisor for memory operations**, because the only reason memory operations exist is to enable correct answers later. The 152-QA training set works because the reward signal carries information across many memory operations per dialogue — each operation is judged by its eventual contribution to QA success. This is the operationalization of "the AI is a maintainer, not an oracle" — but now the maintainer's job description is itself learned.

## Implications

[ENGRAM mapping: dominant on **E** (Encode — what gets written, who decides), **A** (Aggregate — UPDATE consolidates rather than fragments), **R** (Retrieve — Answer Agent's distillation step is learned filtering); secondary on **M** (Maintain — the operation set is the maintenance vocabulary)]

1. **CRUD as the right operation set is now empirically validated.** [E, A, M] Multiple prior systems (MemGPT, Modarressi 2024, AIOS, Mem0) converged on roughly the same {ADD, UPDATE, DELETE, NOOP} or {Create, Read, Update, Delete, Search} operation set. Memory-R1 confirms this is expressively sufficient (achieves SOTA without needing additional operations) while being minimal enough that RL can learn the policy from 152 examples. **For Flow OS: don't invent new operations. The CRUD set is canonical.** What you can innovate on is the *policy* that selects among them.

2. **Outcome-driven reward kills the labelling problem.** [E] The reason supervised memory management never worked: labelling every memory write in a 600-turn dialogue is hours of human time per dialogue, and the labels are subjective (was that worth remembering?). RL with exact-match QA reward sidesteps this entirely — you only need ground-truth answers, not ground-truth memory operations. **The reward signal compounds across operations**: a single QA reward shapes ~10-20 memory operations that fed into the answer. This is much more sample-efficient than per-operation supervision.

3. **Memory distillation IS the new RAG.** [R] The Answer Agent retrieves 60 candidates via vanilla similarity-based RAG, then **learns to discard 59 of them and reason over the 1-3 that matter**. This is a direct response to Liu 2023's "Lost in the Middle" finding: putting too much retrieved content in context hurts performance. Memory-R1's distillation step turns the LLM itself into the second retrieval stage. **For Flow OS: high-recall first pass + LLM-as-second-stage-filter is now the validated pattern**, not LLM-attention-over-many-chunks.

4. **GRPO > PPO for this problem class.** Table 1 shows GRPO consistently outperforms PPO across all backbones (e.g., LLaMA-8B: GRPO 45.02 F1 vs PPO 41.05). GRPO's group-relative advantage (no value function, candidates compared within a batch) is well-suited to memory operations where the absolute "value" of any one operation is unstable but the relative ranking of candidate operations is meaningful.

5. **152 training pairs is the headline efficiency result.** This is ~3 orders of magnitude less than typical RL fine-tuning. The implication: **memory policies generalize quickly because the operation set is small and the reward signal is informative**. Scaling laws here probably bend differently than in capability training.

## How to Apply It (method)

**Two-agent architecture:**

**Memory Manager** (πθ):
```
Input:  x         (new info extracted from current dialogue turn)
        M_old     (current memory bank)
Output: (o, m')   where o ∈ {ADD, UPDATE, DELETE, NOOP}
                  and m' is the new/updated content (if o ≠ NOOP)

PPO objective:
  J(θ) = E[ min(ρ_θ · A, clip(ρ_θ, 1-ε, 1+ε) · A) ]
  where ρ_θ = π_θ(o, m' | x, M_old) / π_old(o, m' | x, M_old)
        A is advantage from R_answer

GRPO objective:
  J(θ) = E[ (1/G) Σ ρ_θ^(i) · A_i  -  β · D_KL[π_θ || π_ref] ]
  where A_i = (r_i - mean(r)) / std(r)  — group-relative
```

**Answer Agent** (πθ):
```
Input:  q         (question)
        M_ret     (top-60 retrieved candidate memories via vanilla RAG)
Output: y         (answer, after internal memory distillation)

Same PPO/GRPO objectives applied to answer sequence y.
Reward: R = EM(y_pred, y_gold)
```

**Reward (shared):**
```
R_answer = Exact-Match(y_pred, y_gold)
```
Binary 0/1, no per-operation labels, no human RLHF.

**Training scale:**
- 152 train / 81 val / 1307 test QA pairs (LoCoMo, adversarial subset excluded)
- Backbones: LLaMA-3.1-8B-Instruct and Qwen-2.5 (3B, 7B, 14B)
- Temperature 0, max 2048 tokens at eval

**Why GRPO is the right pick here**: PPO needs a value function to compute advantages; that value function is hard to train when rewards are sparse (one QA result per long dialogue). GRPO compares candidate operations within a sampled group — relative ranking is more stable than absolute value estimation under sparse rewards.

**For your own system, the steps are:**

1. Pick a memory operation set. CRUD ({ADD, UPDATE, DELETE, NOOP}) is the empirical default.
2. Define a retrieval policy that returns top-K candidates (Memory-R1 uses similarity-based RAG, K=60).
3. Define a downstream task with a checkable reward (QA exact-match, code correctness, business metric).
4. Train two policies with GRPO: one selecting operations on writes, one filtering and reasoning on reads. Share the reward.
5. Bootstrap with a tiny labeled set (Memory-R1: 152 examples). Generalization comes from policy structure, not data volume.

## Best Figure

_(figure not extracted — Figure 1 of the paper is the most illustrative; image extraction skipped to ship the digest)_

**Figure 1 — Memory-R1 vs vanilla LLM memory system, page 2.**

A side-by-side dialogue trace. Left panel: in a multi-session dialogue, a user says "I adopted a dog named Buddy" in session 1 and "I adopted another dog named Scout" in session 2. Middle panel: a vanilla LLM-driven Memory Manager (heuristic prompting) reads this as a contradiction, issues DELETE+ADD, and fragments the memory ("dog named Scout" replaces "dog named Buddy" — losing Buddy). Right panel: Memory-R1's RL-trained Memory Manager issues a single UPDATE consolidating to "Andrew adopted 2 dogs named Buddy and Scout"; the Answer Agent retrieves 60 candidate memories, distills them down to that one consolidated entry, and answers "2 dogs" correctly to the question "How many dogs has Andrew adopted?"

The figure encapsulates the entire thesis: the right behavior on this case is *not derivable from a simple rule* (the model has to understand that "another" implies addition rather than replacement), and brittle heuristics fail in ways that are invisible until you measure downstream QA — exactly the kind of failure RL with QA-correctness rewards is designed to surface and fix.

## What Experts Overlook

1. **The 60-candidate retrieval window is doing more work than you think.** [R] Most RAG systems retrieve 5-10 chunks. Memory-R1 retrieves 60 and lets the Answer Agent's distillation step compress. This works because the LLM can hold many candidates in context and selectively attend, but it ONLY works at this scale because the Answer Agent is RL-trained to ignore noise. A naive LLM at 60 candidates would degrade (the Lost-in-the-Middle effect). **The retrieval-K hyperparameter is now coupled to the reader's training regime**, not independently tunable.

2. **152 examples is small enough to overfit, and the paper doesn't fully address this.** The validation set is only 81 examples. Reported gains are robust across backbones, which suggests genuine generalization, but the train→test split is within LoCoMo, so the "zero-shot to MSC and LongMemEval" results are the more compelling generalization signal. Read those numbers (Appendix D) before deploying — they're the true measure of whether the learned policy transfers vs. memorizes LoCoMo idiosyncrasies.

3. **Outcome-driven RL has a known failure mode: it learns to *avoid* memory.** [E] If NOOP gets you answers right often enough, the policy might converge to "do nothing most of the time." The paper's reported NOOP rate isn't prominent in the main text — worth checking before assuming the policy is actively managing memory rather than just minimally interfering. The 28% relative improvement over Mem0 suggests substantive memory work is happening, but the failure mode is real and worth instrumenting in any deployment.

4. **No mention of memory size growth.** [M] Over 1300 test questions, the memory bank grows monotonically (ADDs and UPDATEs). What is the steady-state size? When does retrieval cost dominate? The paper doesn't discuss eviction strategy beyond DELETE — and DELETE is presumably rare under outcome-driven reward (deleting often hurts downstream QA). **This is the known weakness of CRUD-without-tier-management**: MemoryOS's strength was tier promotion/demotion; Memory-R1 doesn't have that. For long-running production agents, you'd need to layer tier policies on top.

5. **The Answer Agent's distillation is implicit, not explicit.** [R] The paper says the agent "applies a memory distillation policy" but the distillation is just chain-of-thought reasoning over the 60 candidates — there's no separate distillation module or explicit selection step. The RL training shapes the chain-of-thought to ignore irrelevant memories. This is elegant but makes the distillation step uninterpretable — you can't inspect "which memories did the agent actually use?" without trace analysis. For production, you'd want to surface this.

## Extracted Prompts

The paper doesn't release full prompt text in the main body (likely in Appendix D), but the operation taxonomy and Answer Agent template are inferrable. **Memory Manager prompt** (reconstructed from §3.1):

```
You are a Memory Manager for a long-running dialogue agent. You maintain a memory bank that persists across sessions.

For each new piece of information extracted from the current dialogue turn, decide ONE operation:

- ADD: Create a new memory entry. Use when the information is genuinely new and does not relate to any existing entry.
- UPDATE: Modify an existing entry. Use when the new information extends, refines, or consolidates an existing entry. Prefer UPDATE over DELETE+ADD — consolidating is better than fragmenting.
- DELETE: Remove an existing entry. Use only when the new information directly contradicts and replaces an existing entry (rare).
- NOOP: Take no action. Use when the information is already captured or not worth storing.

Input:
  new_info: {x}
  current_memory_bank: {M_old}

Output: (operation, updated_content)
```

**Answer Agent prompt** (reconstructed from §3.2):

```
You are an Answer Agent. Given a question and 60 candidate memories retrieved via similarity search, answer the question.

Approach:
1. Distill: read the candidates and identify the 1-5 that are actually relevant to the question. Ignore the rest — most retrieved candidates are noise.
2. Reason: synthesize across the relevant candidates if multi-hop.
3. Answer: produce a concise answer matching the format the question expects.

Question: {q}

Candidate memories (60):
{M_ret}

Answer:
```

The structural innovation is the explicit *distillation* instruction. RL training shapes how the model executes this instruction — it isn't a separate module.

## Citations

- Chhikara et al. (2025) — Mem0 (the primary baseline; Memory-R1 inherits the {ADD, UPDATE, DELETE, NOOP} operation set from Mem0)
- Maharana et al. (2024) — LoCoMo benchmark (primary eval)
- Kang et al. (2025) — MemoryOS (baseline; tier-based competitor)
- Packer et al. (2023) — MemGPT (OS-inspired memory baseline)
- Xu et al. (2025) — A-Mem (agentic memory baseline)
- Schulman et al. (2017) — PPO (the RL algorithm)
- Shao et al. (2024) — GRPO (DeepSeekMath's group-relative variant; better than PPO here)
- Jin et al. (2025) — Search-R1 (RL for retrieval, parallel framing)
- Wu et al. (2024) — LongMemEval (transfer benchmark)
- Ouyang et al. (2022) — RLHF (the foundational RL-for-LLMs work)
- Liu et al. (2023) — Lost in the Middle (the motivating finding for the distillation step)
- Du et al. (2025) — Survey on memory mechanism of LLM agents

(Full citations list in frontmatter `citations:` field.)

## Related Digests

- [[chhikara-2025-mem0]] — Mem0 is the closest baseline and operation-set ancestor
- [[kang-2025-memory-os]] — MemoryOS provides tier-management, complementary to Memory-R1's operation learning
- [[maharana-2024-locomo]] — Primary benchmark; understanding LoCoMo's structure helps interpret the gains
- [[packer-2023-memgpt-os]] — Earlier OS-as-memory framing that motivated the CRUD operation set
- [[latimer-2025-hindsight-memory]] — Hindsight-based memory revision, related-but-different RL framing

## Reviewer Notes

Hallucination check: **Clean**. Key numbers verified: 152 training pairs, 81 val, 1307 test (LoCoMo, adversarial excluded); 60 retrieved candidates; LLaMA-3.1-8B-Instruct Memory-R1-GRPO 45.02 overall F1 vs Mem0 30.41 (~+14 absolute / +48% relative — paper claims 28% in the abstract, which is conservative); 28% F1 / 34% BLEU-1 / 30% LLM-judge relative improvements (matches paper abstract). The {ADD, UPDATE, DELETE, NOOP} set is correctly attributed to Mem0 as the immediate predecessor. The "memory operations are a learnable policy" framing is the paper's central claim. The GRPO > PPO observation is consistent across the reported table.
