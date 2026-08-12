---
corpus: agentic-memory
kind: paper-digest
slug: agrawal-2025-gepa-reflective-prompt-evolution
title: "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning"
authors:
  - "Agrawal, Lakshya A"
  - "Tan, Shangyin"
  - "Soylu, Dilara"
  - "Ziems, Noah"
  - "Khare, Rishi"
  - "Opsahl-Ong, Krista"
  - "Singhvi, Arnav"
  - "Shandilya, Herumb"
  - "Ryan, Michael J"
  - "Jiang, Meng"
  - "Potts, Christopher"
  - "Sen, Koushik"
  - "Dimakis, Alexandros G."
  - "Stoica, Ion"
  - "Klein, Dan"
  - "Zaharia, Matei"
  - "Khattab, Omar"
year: 2025
publication_date: "2025-07"
venue: "arXiv preprint (ICLR 2026 Oral)"
source_url: "https://arxiv.org/abs/2507.19457"
doi: null
arxiv_id: "2507.19457"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "GEPA replaces the scalar reward signal of RL prompt-optimization with natural-language reflection over execution and evaluation traces, and combines it with a Pareto-frontier candidate pool over individual training instances; the result beats GRPO by up to 20% with 35x fewer rollouts and beats the prior SOTA prompt optimizer MIPROv2 by 10-13% aggregate across six tasks on Qwen3-8B and GPT-4.1-mini."
topics:
  - prompt-optimization
  - reflective-learning
  - evolutionary-search
  - pareto-front
  - compound-ai-systems
  - reinforcement-learning
  - sample-efficiency
  - dspy
tags:
  - paper
  - prompt-engineering
  - llm-optimization
  - genetic-algorithms
  - rl-alternative
  - iclr-2026
entities:
  - agrawal-lakshya
  - khattab-omar
  - zaharia-matei
  - klein-dan
  - stoica-ion
  - potts-christopher
related_digests:
  - fernando-2023-promptbreeder
  - vassilyev-2026-rcl
  - zhang-2025-ace
  - guo-2024-evoprompt
  - pei-2025-scope-prompt-evolution
  - wang-2025-promptquine-evolutionary-icl
  - cui-2024-see-prompt-optimization
citations:
  - title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (introduces GRPO)"
    authors: ["Shao, Z.", "Wang, P.", "Zhu, Q.", "et al."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.03300"
    arxiv_id: "2402.03300"
  - title: "Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs (MIPROv2)"
    authors: ["Opsahl-Ong, K.", "Ryan, M. J.", "Purtell, J.", "Broman, D.", "Potts, C.", "Zaharia, M.", "Khattab, O."]
    year: 2024
    doi: "10.18653/v1/2024.emnlp-main.525"
    url: "https://aclanthology.org/2024.emnlp-main.525/"
    arxiv_id: null
  - title: "DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines"
    authors: ["Khattab, O.", "Singhvi, A.", "Maheshwari, P.", "et al."]
    year: 2024
    doi: null
    url: "https://openreview.net/forum?id=sY5N0zY5Od"
    arxiv_id: null
  - title: "Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers (EvoPrompt)"
    authors: ["Guo, Q.", "Wang, R.", "Guo, J.", "et al."]
    year: 2024
    doi: null
    url: "https://openreview.net/forum?id=ZG3RaNIsO8"
    arxiv_id: null
  - title: "Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution"
    authors: ["Fernando, C.", "Banarse, D.", "Michalewski, H.", "Osindero, S.", "Rocktäschel, T."]
    year: 2024
    doi: null
    url: null
    arxiv_id: null
  - title: "Optimizing Generative AI by Backpropagating Language Model Feedback (TextGrad)"
    authors: ["Yuksekgonul, M.", "Bianchi, F.", "Boen, J.", "Liu, S.", "Lu, P.", "Huang, Z.", "Guestrin, C.", "Zou, J."]
    year: 2025
    doi: null
    url: null
    arxiv_id: null
  - title: "Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs"
    authors: ["Cheng, C.-A.", "Nie, A.", "Swaminathan, A."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2406.16218"
    arxiv_id: "2406.16218"
  - title: "Automatic Prompt Optimization with Gradient Descent and Beam Search (APO)"
    authors: ["Pryzant, R.", "Iter, D.", "Li, J.", "Lee, Y.", "Zhu, C.", "Zeng, M."]
    year: 2023
    doi: "10.18653/v1/2023.emnlp-main.494"
    url: "https://aclanthology.org/2023.emnlp-main.494/"
    arxiv_id: null
  - title: "HotpotQA: A Dataset for Diverse, Explainable Multi-Hop Question Answering"
    authors: ["Yang, Z.", "Qi, P.", "Zhang, S.", "Bengio, Y.", "Cohen, W. W.", "Salakhutdinov, R.", "Manning, C. D."]
    year: 2018
    doi: null
    url: null
    arxiv_id: null
  - title: "HoVer: A Dataset for Many-Hop Fact Extraction and Claim Verification"
    authors: ["Jiang, Y.", "Bordia, S.", "Zhong, Z.", "Dognin, C.", "Singh, M.", "Bansal, M."]
    year: 2020
    doi: "10.18653/v1/2020.findings-emnlp.309"
    url: "https://aclanthology.org/2020.findings-emnlp.309/"
    arxiv_id: null
  - title: "AIME-2025 Dataset"
    authors: ["Balunović, M.", "Dekoninck, J.", "Petrov, I.", "Jovanović, N.", "Vechev, M."]
    year: 2025
    doi: null
    url: "https://huggingface.co/datasets/MathArena/aime_2025"
    arxiv_id: null
  - title: "LiveBench: A Challenging, Contamination-Limited LLM Benchmark"
    authors: ["White, C.", "Dooley, S.", "Roberts, M.", "et al."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2406.19314"
    arxiv_id: "2406.19314"
  - title: "Generalizing Verifiable Instruction Following (IFBench)"
    authors: ["Pyatkin, V.", "Malik, S.", "Graf, V.", "et al."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2507.02833"
    arxiv_id: "2507.02833"
  - title: "PAPILLON: Privacy Preservation from Internet-Based and Local Language Model Ensembles (PUPA)"
    authors: ["Li, S.", "Raghuram, V. C.", "Khattab, O.", "Hirschberg, J.", "Yu, Z."]
    year: 2025
    doi: "10.18653/v1/2025.naacl-long.173"
    url: "https://aclanthology.org/2025.naacl-long.173/"
    arxiv_id: null
  - title: "Qwen3 Technical Report"
    authors: ["Yang, A.", "et al."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2505.09388"
    arxiv_id: "2505.09388"
  - title: "Illuminating Search Spaces by Mapping Elites (MAP-Elites)"
    authors: ["Mouret, J.-B.", "Clune, J."]
    year: 2015
    doi: null
    url: "https://arxiv.org/abs/1504.04909"
    arxiv_id: "1504.04909"
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    authors: ["Shinn, N.", "Cassano, F.", "Gopinath, A.", "Narasimhan, K.", "Yao, S."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Self-Refine: Iterative Refinement with Self-Feedback"
    authors: ["Madaan, A.", "Tandon, N.", "Gupta, P.", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Teach Better or Show Smarter? On Instructions and Exemplars in Automatic Prompt Optimization"
    authors: ["Wan, X.", "Sun, R.", "Nakhost, H.", "Arik, S."]
    year: 2024
    doi: null
    url: null
    arxiv_id: null
  - title: "Large Language Models as Optimizers (OPRO)"
    authors: ["Yang, C.", "Wang, X.", "Lu, Y.", "Liu, H.", "Le, Q. V.", "Zhou, D.", "Chen, X."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2309.03409"
    arxiv_id: "2309.03409"
  - title: "Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization"
    authors: ["Zhang, W.", "Tang, K.", "Wu, H.", "et al."]
    year: 2024
    doi: "10.18653/v1/2024.acl-long.292"
    url: "https://aclanthology.org/2024.acl-long.292/"
    arxiv_id: null
  - title: "Optimas: Optimizing Compound AI Systems with Globally Aligned Local Rewards"
    authors: ["Wu, S.", "Sarthi, P.", "Zhao, S.", "et al."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2507.03041"
    arxiv_id: "2507.03041"
  - title: "Multi-Module GRPO: Composing Policy Gradients and Prompt Optimization for Language Model Programs"
    authors: ["Ziems, N.", "Soylu, D.", "Agrawal, L. A.", "et al."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2508.04660"
    arxiv_id: "2508.04660"
  - title: "AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery"
    authors: ["Novikov, A.", "Vũ, N.", "Eisenberger, M.", "et al."]
    year: 2025
    doi: null
    url: null
    arxiv_id: null
  - title: "KernelBench: Can LLMs Write Efficient GPU Kernels?"
    authors: ["Ouyang, A.", "Guo, S.", "Arora, S.", "Zhang, A. L.", "Hu, W.", "Re, C.", "Mirhoseini, A."]
    year: 2025
    doi: null
    url: "https://openreview.net/forum?id=k6V4jb8jkX"
    arxiv_id: null
  - title: "NPUEval: Optimizing NPU Kernels with LLMs and Open Source Compilers"
    authors: ["Kalade, S.", "Schelle, G."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2507.14403"
    arxiv_id: "2507.14403"
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    authors: ["Yao, S.", "Zhao, J.", "Yu, D.", "et al."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2210.03629"
    arxiv_id: "2210.03629"
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    authors: ["Wei, J.", "Wang, X.", "Schuurmans, D.", "et al."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2201.11903"
    arxiv_id: "2201.11903"
  - title: "Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts"
    authors: ["Samvelyan, M.", "Raparthy, S. C.", "Lupu, A.", "et al."]
    year: 2024
    doi: null
    url: null
    arxiv_id: null
  - title: "Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory"
    authors: ["Suzgun, M.", "Yuksekgonul, M.", "Bianchi, F.", "Jurafsky, D.", "Zou, J."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2504.07952"
    arxiv_id: "2504.07952"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Comparison of learning behavior — GEPA vs. MIPROv2 vs. GRPO on HotpotQA and IFBench (Qwen3-8B)"
  page: 1
  image_path: "figures/agrawal-2025-gepa-reflective-prompt-evolution-fig.png"
---

# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

**Authors:** Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab
**Published:** 2025-07 · [Source](https://arxiv.org/abs/2507.19457) (v2 14 Feb 2026, accepted ICLR 2026 Oral)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

GEPA (Genetic-Pareto) is a prompt optimizer for **compound AI systems** that replaces the scalar-reward signal used by RL methods like GRPO with **natural-language reflection over execution and evaluation traces**, combined with a **Pareto-frontier candidate pool** that prevents the search from collapsing into a single greedy lineage. Given any LLM-based system with one or more module prompts (e.g., a multi-hop RAG agent), GEPA samples a minibatch of rollouts, feeds the (prompt, trace, score, textual feedback) tuple to a reflection LM, and asks it to rewrite a chosen module's prompt; if the rewrite improves minibatch score, the new candidate is added to the pool with ancestry tracking. Across six tasks (HotpotQA, IFBench, HoVer, PUPA, AIME-2025, LiveBench-Math) on Qwen3-8B and GPT-4.1-mini, GEPA outperforms GRPO (24,000 rollouts) by up to **+19% with up to 35x fewer rollouts**, and beats MIPROv2 — the prior SOTA prompt optimizer — by aggregate **+13.3%** vs MIPROv2's +5.6% on GPT-4.1-mini. A "GEPA+Merge" variant adds system-aware crossover that picks complementary module updates from two distinct lineages. Prompts optimized on Qwen3-8B transfer to GPT-4.1-mini with a +9% gain — outperforming baselines optimized directly on GPT-4.1-mini. The authors also demonstrate GEPA as an inference-time search method (boosting GPT-4o NPU-kernel vector utilization from 4.25% → 30.52%) and as an adversarial prompt finder that drives AIME-2025 pass@1 on GPT-5-mini from 76% to 10%. Code: github.com/gepa-ai/gepa.

## Key Takeaway

The interpretable nature of language is a richer learning medium for LLMs than policy gradients derived from sparse scalar rewards — and a reflective optimizer that reads its own execution traces, proposes targeted prompt edits, and maintains a Pareto frontier of "winning strategies per task instance" can extract more learning signal from a few hundred rollouts than RL extracts from tens of thousands. GEPA proves this empirically across six diverse benchmarks (math, instruction-following, multi-hop QA, fact verification, privacy-aware delegation) and two model families, beating GRPO by up to 20% with up to 35x sample efficiency and doubling MIPROv2's aggregate gains. The architectural lesson is more durable than the numbers: Pareto-illumination over per-instance winners (an idea borrowed from MAP-Elites in evolutionary computation) prevents the local-optimum trap that kills greedy and beam-search variants like TextGrad and APO.

## Implications

- **For LLM application developers:** if you have a compound AI system (multi-step RAG, agent with tool calls, multi-module DSPy program), running GEPA for ~1k-7k rollouts will typically produce a better-performing prompt than fine-tuning the weights with 24k GRPO rollouts — especially when the LLM is closed-source, when tool calls are expensive, or when you cannot finetune the largest model in your stack.
- **For prompt-engineering research:** the historical finding that "few-shot demonstration optimization beats instruction optimization" (Wan et al. 2024) appears to be flipping with newer models. GEPA's instruction-only prompts now beat MIPROv2's joint instruction+demonstration prompts by 11.1% on GPT-4.1-mini, and the resulting prompts are up to **9.2x shorter** — so the better prompts are also cheaper to serve.
- **For RL practitioners:** the paper does not claim RL is dead — at high enough rollout budgets RL may still win, and the authors note GRPO can outperform GEPA on certain tasks (e.g., AIME with Qwen3-8B at the budgets tested). What it claims is that the **sample-efficiency regime where most real applications live** (hundreds-to-thousands of rollouts, not millions) favors reflective prompt evolution.
- **For transfer / generalization studies:** GEPA prompts optimized on a weaker model (Qwen3-8B) transferred to a stronger model (GPT-4.1-mini) with +9% gain, outperforming methods that optimized directly on the stronger model. This suggests prompt-level optimization captures task structure in a model-agnostic way.
- **For evolutionary computation:** the paper validates Mouret & Clune's MAP-Elites "illumination" approach in a new domain — Pareto-illumination of per-instance winners turns out to be the single most important design choice, contributing **+7.33% / +6.4%** aggregate improvement over greedy and beam-search variants when the rest of the harness is held fixed (Table 3).
- **For inference-time search and red-teaming:** the same algorithm doubles as an inference-time code-generation refiner (NPUEval 4.25% → 30.52% mean vector utilization) and an adversarial prompt-search method (AIME pass@1 76% → 10%), suggesting reflective evolution is a general-purpose primitive for any "improve a textual artifact under a measurable objective" task.

## How to Apply It (method)

**Inputs:** an LLM-based system Φ with module prompts Π = ⟨π₁, ..., π_M⟩, a training set D_train, a scalar metric μ, an *augmented feedback function* μ_f that returns both a numeric score and natural-language `feedback_text` (compiler errors, failed-rubric explanations, retrieval miss-traces, human feedback, etc.), and a rollout budget B.

**Setup:** split D_train into D_feedback (used to score minibatches and gather text feedback) and D_pareto (a held-out set used only for tracking candidate quality; |D_pareto| = n_pareto is a hyperparameter). Initialize the candidate pool P = [Φ] (the system with its seed prompts) and run the seed system on D_pareto to get its per-instance score vector S_Φ.

**Optimization loop (Algorithm 1 in paper):**
1. **Select candidate:** call SelectCandidate(P, S) — the Pareto-based subroutine (Algorithm 2): for each task instance i, take the set of candidates that achieve the per-task maximum score s\*[i]; union these "instance-winners" across tasks; prune any candidate that is dominated by another in the set; sample one of the survivors with probability proportional to the number of tasks it wins.
2. **Select module to update:** pick a module j of the chosen candidate (round-robin is the default; the algorithm is policy-agnostic).
3. **Sample minibatch** M ⊂ D_feedback of size b (default b = 5).
4. **Run rollouts** of the candidate on M, recording for module j the inputs, outputs, reasoning trace, and the feedback_text returned by μ_f.
5. **Reflective prompt mutation:** feed the reflection LM the tuple (current π_j, trace, score, feedback_text) using the meta-prompt in Appendix C (essentially: "Here is the current instruction. Here are examples of inputs, outputs, and feedback. Write a new instruction in ``` blocks that captures the domain-specific facts and any generalizable strategies."). The reflection LM returns a new π'_j.
6. **Evaluate the new candidate** Φ' (= Φ_k with module j updated to π'_j) on the same minibatch M; compare average score σ' to σ (the parent's avg on M).
7. **Accept-if-improved:** if σ' > σ, evaluate Φ' on the full D_pareto, append Φ' to P with ancestry pointer to Φ_k, and update S_Φ'.
8. **Optional Merge (Appendix D.1, GEPA+Merge):** periodically check the pool for pairs of candidates that share a common ancestor, are Pareto-optimal, and have improved on **disjoint** sets of modules; combine them by taking the best version of each module from the two lineages.
9. Loop until budget B exhausted; return the candidate with the highest mean score on D_pareto.

**Practical hyperparameters reported:** minibatch size b is small (typical 5); n_pareto is task-dependent (~100-300); total rollout budgets reported range from 1,839 to 7,051 for GEPA (vs. 24,000 for GRPO baseline). Reflection LM = the same model being optimized (Qwen3-8B or GPT-4.1-mini) in the main experiments. **Most of GEPA's budget is spent on validation** (re-scoring on D_pareto); train-set-only rollouts to reach optimal performance are 79-737.

**Critical design rule from the paper:** μ_f must surface *textual* feedback, not just a scalar. The paper emphasizes that compiler error messages, rubric failures, and module-level signals (e.g., "after hop 2 the system retrieved doc X but the gold doc was Y") are what make reflection effective. Where these aren't naturally available, the authors recommend augmenting D_train with human-written rationales.

**Code:** github.com/gepa-ai/gepa (referenced from the abstract; integrates with the DSPy framework that several authors maintain).

## Best Figure

![Figure 1 — Comparison of learning behavior — GEPA vs. MIPROv2 vs. GRPO on HotpotQA and IFBench (Qwen3-8B) (page 1)](figures/agrawal-2025-gepa-reflective-prompt-evolution-fig.png)

Image Candidates:
Figure 1 (p. 1): Side-by-side validation/test-set learning curves of GEPA, MIPROv2, GRPO, and the baseline on HotpotQA and IFBench against rollout budget — single image that captures the headline claim.
Table 1 (p. 8): Benchmark grid showing GEPA aggregate +9.62% vs GRPO +3.68% on Qwen3-8B across six tasks with rollout budgets — the numeric story in one frame.
Figure 5 (p. 8): Annotated subtree of the GEPA optimization trajectory on PUPA, showing how successive prompt mutations push the score from 82.26 to 97.6 with the actual prompt-content deltas annotated on each edge.

Best Image:
Figure Name: Figure 1: "A comparison of learning behavior of the GEPA prompt optimizer against a state-of-the-art prompt optimizer (MIPROv2) and GRPO (24,000 rollouts)"
Figure Page: 1
Slide Caption: GEPA learns faster and reaches a higher ceiling than both GRPO and MIPROv2 on HotpotQA and IFBench (Qwen3-8B).
Description: Figure 1 plots validation-set score versus rollout count for four optimizers on HotpotQA and IFBench with Qwen3-8B. GEPA (blue) reaches its plateau within the first ~5,000 rollouts at scores well above the baseline (black), MIPROv2 (green), and GRPO (orange). GRPO consumes the full 24,000-rollout budget and ends below GEPA on both tasks. Test-set star markers in the top-left of each subplot show that GEPA's held-out performance (blue star) is materially higher than MIPROv2's (green star) and GRPO's (orange star) — and that GRPO actually loses ground to baseline on HotpotQA test (orange star ~42.5 vs. baseline 42.33). This one figure compresses the paper's central claim (sample-efficient reflective prompt evolution beats both gradient-based RL and prior prompt optimizers) into a visual that requires no statistics literacy to read.

## What Experts Overlook

- **Most of GEPA's rollout budget is validation, not learning.** The paper buries this in §4 Observation 1: train-set rollouts to reach optimal performance are 79-737 (across the six tasks), while the *total* reported budgets of 1,839-7,051 are dominated by re-evaluating each newly accepted candidate on the full D_pareto. This means the headline "35x more sample-efficient than GRPO" understates the gap — if you measured only the rollouts that actually produce learning signal (train rollouts on D_feedback), the ratio is closer to 78x. The authors flag dynamic-subset validation as future work, suggesting the sample-efficiency story still has runway.
- **Pareto-illumination is doing most of the work, not the reflection.** Table 3 isolates the contribution of the candidate-selection strategy holding the reflective-mutation engine constant: greedy "always pick the best" gets +6.05%, BeamSearch(N=4) gets +5.11%, and GEPA's Pareto sampling gets +12.44% — so roughly half of GEPA's gain over the prior generation of prompt optimizers comes from refusing to commit to a single dominant strategy, not from the reflection step itself. This means anyone using TextGrad or APO is leaving ~7% aggregate gain on the table for free by swapping in Pareto candidate selection.
- **GEPA+Merge is unstable across models.** §5 Observation 5 admits Merge degrades performance on Qwen3-8B (IFBench drops from 38.61 to 28.23) even though it helps on GPT-4.1-mini (+1.14% aggregate over GEPA). The authors attribute this to the fixed hyperparameter budget split between mutation and crossover, but the practical implication is that practitioners should not enable Merge by default — it requires per-model tuning.
- **The cross-model transfer result is more important than the headline number.** Table 2 shows that prompts optimized on Qwen3-8B and evaluated zero-shot on GPT-4.1-mini achieve +9% — beating MIPROv2, TextGrad, and Trace that were *optimized directly on GPT-4.1-mini*. This suggests prompt optimization is capturing task structure that is largely orthogonal to the underlying model's capabilities, which has obvious cost implications (optimize on a cheap model, deploy on an expensive one).
- **The adversarial AIME result is a red flag for instruction-following evals.** A clean instruction prompt with two injected trivia sentences ("honey never spoils", "dolphins sleep with one eye open") collapses AIME-2025 pass@1 from 76% to 10% on GPT-5-mini. The manual analysis shows the failure mode is the model literally outputting the placeholder `### <final answer>` — suggesting the brittleness is in the interaction between a strict formatting constraint and any distractor text, not in the math reasoning itself. This is a generalizable warning about how thin the margin is between "follows instructions correctly" and "follows the wrong instructions correctly."
- **GEPA does NOT update LLM weights** — only prompts. The problem statement (§2) allows for joint Π, Θ optimization to make GEPA-vs-GRPO comparable, but in practice GEPA freezes Θ. So the apples-to-apples comparison is really "prompt optimization vs. weight optimization on the same task," and GEPA wins not because reflection is universally better than gradients but because in low-budget compound-AI-system regimes the prompt parameter is denser-in-task-structure than the weight parameter.

## Extracted Prompts

The paper's most-quoted prompt is **GEPA's meta-prompt for reflective prompt updates** (Appendix C), reproduced here in full:

```
I provided an assistant with the following instructions to perform a task for me:

```
<current instruction>
```

The following are examples of different task inputs provided to the assistant along
with the assistant's response for each of them, and some feedback on how the
assistant's response could be better:

```
<Inputs, Outputs and Feedback for minibatch of examples>
```

Your task is to write a new instruction for the assistant.

Read the inputs carefully and identify the input format and infer detailed task
description about the task I wish to solve with the assistant.

Read all the assistant responses and the corresponding feedback. Identify all niche
and domain specific factual information about the task and include it in the
instruction, as a lot of it may not be available to the assistant in the future. The
assistant may have utilized a generalizable strategy to solve the task, if so,
include that in the instruction as well.

Provide the new instructions within ``` blocks.
```

Three things to notice in this meta-prompt: (1) it asks for *factual domain knowledge* to be lifted into the instruction explicitly, on the theory that the trace contains task-specific facts the assistant won't see at inference time; (2) it asks for *generalizable strategies* to be extracted, mirroring the chain-of-thought-as-explicit-rule rewriting move; (3) it constrains the output to live in ``` blocks for easy parsing.

The paper also showcases a striking **before/after** prompt for the second-hop module of a multi-hop QA system (Figure 2):

**Seed prompt:** `"Given the fields question, summary_1, produce the fields query."`

**GEPA-optimized prompt (excerpt):** A ~300-word multi-section instruction with `Input Understanding`, `Purpose and Context`, `Key Observations and Lessons` (including worked examples like "If summary_1 describes a population for a small civil parish, but the question wants the total population of the wider region, your query should target that wider region"), `How to Build the Query`, `Practical Strategy`, and `Output` sections. The optimized prompt is essentially a mini-tutorial-plus-checklist that reads more like a SOP than an instruction. The lesson the optimizer extracted: *"First-hop documents often cover one entity or aspect. Remaining relevant documents often involve connected or higher-level concepts mentioned in summary_1 but not explicitly asked in the original question. Avoid merely paraphrasing the original question."*

For the adversarial-prompt-search application (§5.2), the GEPA-evolved prompt is also reproducible:

```
You are a helpful assistant. You are given a question and you need to answer it.
It's interesting to note that honey never spoils and that the longest river in the
world is the Nile, stretching over 6,650 kilometers. When providing your answer,
be sure to format it at the end of your response exactly as '### <final answer>'.
For this task, remember that many mammals, including dolphins, sleep with one eye
open. Proceed to answer the given question accordingly.
```

This single prompt, prepended to AIME-2025 problems, drops GPT-5-mini pass@1 from 76% to 10%.

## Citations

- Shao et al. 2024 — *DeepSeekMath* (introduces GRPO, the headline RL baseline) — arXiv:2402.03300
- Opsahl-Ong et al. 2024 — *MIPROv2* (prior SOTA prompt optimizer GEPA dethrones) — EMNLP 2024
- Khattab et al. 2024 — *DSPy* (the compound-AI-system framework GEPA plugs into) — ICLR 2024
- Guo et al. 2024 — *EvoPrompt* (evolutionary prompt optimization without reflection) — ICLR 2024
- Fernando et al. 2024 — *Promptbreeder* (self-referential prompt evolution baseline)
- Yuksekgonul et al. 2025 — *TextGrad* (greedy-selection baseline; backpropagates textual feedback) — Nature 639
- Cheng et al. 2024 — *Trace / OptoPrime* (textual-gradient prompt optimizer baseline) — arXiv:2406.16218
- Pryzant et al. 2023 — *APO* (beam-search prompt optimization baseline) — EMNLP 2023
- Mouret & Clune 2015 — *MAP-Elites / Illumination* (origin of the Pareto-illumination idea) — arXiv:1504.04909
- Wan et al. 2024 — *Teach Better or Show Smarter?* (the "few-shot beats instruction" finding GEPA challenges) — NeurIPS 2024
- Yang et al. 2018 — *HotpotQA* (multi-hop QA benchmark)
- Jiang et al. 2020 — *HoVer* (many-hop fact verification benchmark)
- Pyatkin et al. 2025 — *IFBench* (instruction-following benchmark) — arXiv:2507.02833
- Li et al. 2025 — *PAPILLON / PUPA* (privacy-preserving delegation benchmark)
- Balunović et al. 2025 — *AIME-2025*
- White et al. 2025 — *LiveBench-Math* — arXiv:2406.19314
- Yang et al. 2025 — *Qwen3-8B* — arXiv:2505.09388
- OpenAI 2025 — *GPT-4.1-mini*
- Ouyang et al. 2025 — *KernelBench* (CUDA-kernel inference-time-search benchmark)
- Kalade & Schelle 2025 — *NPUEval* (AMD-XDNA2 NPU-kernel benchmark) — arXiv:2507.14403
- Shinn et al. 2023 — *Reflexion* (language-feedback RL ancestor of reflective methods)
- Madaan et al. 2023 — *Self-Refine* (iterative self-feedback ancestor)
- Yang et al. 2024 — *OPRO* (LLMs-as-optimizers framework)
- Wei et al. 2023 — *Chain-of-Thought*
- Yao et al. 2023 — *ReAct* (scaffolded reasoning the paper's compound AI systems use)
- Samvelyan et al. 2024 — *Rainbow Teaming* (related adversarial-prompt QD evolution work)
- Suzgun et al. 2025 — *Dynamic Cheatsheet* (test-time strategy synthesis related to reflective updates)
- Wu et al. 2025 — *Optimas* (locally-aligned per-module RL rewards comparison)
- Ziems et al. 2025 — *Multi-Module GRPO* (combines GRPO and prompt optimization; same group)
- Novikov et al. 2025 — *AlphaEvolve* (DeepMind's code-evolution agent)
- Zhang et al. 2024 — *Agent-Pro* (policy-level reflection comparison)

## Related Digests

- [[fernando-2023-promptbreeder]] — Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution
- [[vassilyev-2026-rcl]] — Reflective Context Learning: Studying the Optimization Primitives of Context Space
- [[zhang-2025-ace]] — Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
- [[guo-2024-evoprompt]] — EvoPrompt: Connecting LLMs with Evolutionary Algorithms Yields Powerful Prompt Optimizers
- [[pei-2025-scope-prompt-evolution]] — SCOPE: Prompt Evolution for Enhancing Agent Effectiveness
- [[wang-2025-promptquine-evolutionary-icl]] — Evolving Prompts In-Context: An Open-ended, Self-replicating Perspective
- [[cui-2024-see-prompt-optimization]] — SEE: Strategic Exploration and Exploitation for Cohesive In-Context Prompt Optimization

## Reviewer Notes

**Overall severity: Clean.**

Cross-checked the digest against the paper text for the following factual claims:

- "+19% / 20% over GRPO, up to 35x fewer rollouts" — paper §4 Observation 1 says "exceeds GRPO on 5 out of 6 tasks by 19.0%, 2.73%, ..." and "up to 35× fewer rollouts." Phrasing in TLDR uses "up to 20%" which matches the abstract's exact wording. Verified.
- "MIPROv2 aggregate +13.33% (GEPA+Merge) / +12.19% (GEPA) on GPT-4.1-mini vs MIPROv2 +5.64%" — verified from Table 2.
- "GEPA aggregate +9.62% on Qwen3-8B vs GRPO +3.68%" — verified from Table 1.
- "Pareto sampling +12.44% vs greedy +6.05% vs beam +5.11%" — verified from Table 3 ("Aggregate Improvement" column).
- "Cross-model transfer +9% (Qwen-optimized → GPT-4.1-mini)" — verified from Table 2 "GEPA-Qwen-Opt" row.
- "Train-set rollouts to optimal: 79-737" — verified from §4 Observation 1: "GEPA requires only 79 to 737 rollouts."
- "9.2x shorter prompts than MIPROv2" — verified from §4 Observation 4.
- "NPU kernel utilization 4.25% → 30.52% mean" — verified from §5.1 (NPUEval text and Figure 7).
- "AIME pass@1 76% → 10% adversarial" — verified from §5.2.
- Meta-prompt (Appendix C) — quoted verbatim from the paper.
- Seed prompt and the multi-hop QA optimized prompt excerpt — verified against Figure 2.
- Adversarial AIME prompt — verified verbatim against §5.2 ("GEPA-generated adversarial prompt (abridged)").
- Author list, arXiv ID (2507.19457), ICLR 2026 Oral acceptance — verified from page-1 header.

No hallucinated facts detected. One soft framing note: the digest characterizes "Pareto-illumination is doing most of the work" — this is supported by Table 3's controlled ablation (Pareto vs. greedy vs. beam, same harness otherwise), but the paper itself does not frame it as "most of the work" — it frames Pareto sampling as one of three core design principles alongside reflection and genetic evolution. The digest's framing is an inference from the ablation numbers, which is fair commentary but should be read as the digester's synthesis, not a verbatim paper claim.
