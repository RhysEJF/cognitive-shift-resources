---
corpus: agentic-memory
kind: paper-digest
slug: deepseek-ai-2025-deepseek-r1-rl-reasoning
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
authors:
  - "DeepSeek-AI"
  - "Guo, Daya"
  - "Yang, Dejian"
  - "Zhang, Haowei"
  - "Song, Junxiao"
  - "Wang, Peiyi"
  - "Zhu, Qihao"
  - "Xu, Runxin"
  - "Zhang, Ruoyu"
  - "Ma, Shirong"
  - "Bi, Xiao"
  - "Zhang, Xiaokang"
  - "Yu, Xingkai"
  - "Wu, Yu"
  - "Wu, Z.F."
  - "Gou, Zhibin"
  - "Shao, Zhihong"
  - "Li, Zhuoshu"
  - "Gao, Ziyi"
year: 2025
publication_date: "2025-01"
venue: "arXiv preprint (subsequently published in Nature, Sep 2025)"
source_url: "https://arxiv.org/abs/2501.12948"
doi: null
arxiv_id: "2501.12948"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Pure rule-based reinforcement learning on top of a strong MoE base (DeepSeek-V3-Base, 671B params / 37B activated) can elicit emergent long-chain reasoning — including self-reflection, verification, and an observable 'aha moment' — without any supervised fine-tuning on human reasoning traces, and the resulting model (DeepSeek-R1) matches OpenAI-o1-1217 on math/code benchmarks at a total training cost of ~$294K."
topics:
  - reinforcement-learning
  - llm-reasoning
  - chain-of-thought
  - grpo
  - reward-modeling
  - knowledge-distillation
  - rule-based-rewards
  - emergent-behavior
  - test-time-scaling
tags:
  - paper
  - deepseek
  - reasoning-models
  - rlhf-alternatives
  - reward-hacking
  - open-weights
  - mixture-of-experts
entities:
  - deepseek-ai
  - guo-daya
  - wang-peiyi
  - shao-zhihong
  - song-junxiao
  - openai-o1
related_digests:
  - vassilyev-2026-rcl
  - yan-2025-memory-r1
  - agrawal-2025-gepa-reflective-prompt-evolution
  - zhang-2025-ace
  - yao-2023-react-reasoning-acting
  - zhou-2022-least-to-most-prompting
citations:
  - title: "Language models are few-shot learners"
    authors: ["Brown, T. B.", "Mann, B.", "Ryder, N.", "et al."]
    year: 2020
    venue: "NeurIPS 2020"
    arxiv_id: null
    url: "https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html"
  - title: "Chain-of-thought prompting elicits reasoning in large language models"
    authors: ["Wei, J.", "Wang, X.", "Schuurmans, D.", "et al."]
    year: 2022
    venue: "NeurIPS 2022"
    url: "http://papers.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html"
  - title: "Large language models are zero-shot reasoners"
    authors: ["Kojima, T.", "Gu, S. S.", "Reid, M.", "Matsuo, Y.", "Iwasawa, Y."]
    year: 2022
    venue: "NeurIPS 2022"
    url: "https://openreview.net/forum?id=e2TBb5y0yFf"
  - title: "DeepSeekMath: Pushing the limits of mathematical reasoning in open language models"
    authors: ["Shao, Z.", "Wang, P.", "Zhu, Q.", "Xu, R.", "Song, J.", "Zhang, M.", "Li, Y.", "Wu, Y.", "Guo, D."]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2402.03300"
    url: "https://arxiv.org/abs/2402.03300"
  - title: "Proximal policy optimization algorithms"
    authors: ["Schulman, J.", "Wolski, F.", "Dhariwal, P.", "Radford, A.", "Klimov, O."]
    year: 2017
    venue: "arXiv preprint"
    arxiv_id: "1707.06347"
    url: "https://arxiv.org/abs/1707.06347"
  - title: "Training language models to follow instructions with human feedback"
    authors: ["Ouyang, L.", "Wu, J.", "Jiang, X.", "et al."]
    year: 2022
    venue: "NeurIPS 2022 (InstructGPT)"
    url: "http://papers.nips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html"
  - title: "Deep reinforcement learning from human preferences"
    authors: ["Christiano, P. F.", "Leike, J.", "Brown, T. B.", "Martic, M.", "Legg, S.", "Amodei, D."]
    year: 2017
    venue: "NeurIPS 2017"
    url: "https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html"
  - title: "Distilling the knowledge in a neural network"
    authors: ["Hinton, G. E.", "Vinyals, O.", "Dean, J."]
    year: 2015
    venue: "arXiv preprint"
    arxiv_id: "1503.02531"
    url: "http://arxiv.org/abs/1503.02531"
  - title: "Distillation scaling laws"
    authors: ["Busbridge, D.", "Shidani, A.", "Weers, F.", "Ramapuram, J.", "Littwin, E.", "Webb, R."]
    year: 2025
    venue: "arXiv preprint"
    arxiv_id: "2502.08606"
    url: "https://arxiv.org/abs/2502.08606"
  - title: "DeepSeek-V3 technical report"
    authors: ["DeepSeek-AI"]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2412.19437"
    url: "https://arxiv.org/abs/2412.19437"
  - title: "DeepSeek-V2: A strong, economical, and efficient mixture-of-experts language model"
    authors: ["DeepSeek-AI"]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2405.04434"
    url: "https://doi.org/10.48550/arXiv.2405.04434"
  - title: "Let's verify step by step"
    authors: ["Lightman, H.", "Kosaraju, V.", "Burda, Y.", "et al."]
    year: 2024
    venue: "ICLR 2024"
    url: "https://openreview.net/forum?id=v8L0pN6EOi"
  - title: "Solving math word problems with process- and outcome-based feedback"
    authors: ["Uesato, J.", "Kushman, N.", "Kumar, R.", "et al."]
    year: 2022
    venue: "arXiv preprint"
    arxiv_id: "2211.14275"
    url: "https://arxiv.org/abs/2211.14275"
  - title: "Math-shepherd: A label-free step-by-step verifier for LLMs in mathematical reasoning"
    authors: ["Wang, P.", "Li, L.", "Shao, Z.", "Xu, R.", "Dai, D.", "Li, Y.", "Chen, D.", "Wu, Y.", "Sui, Z."]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2312.08935"
    url: "https://arxiv.org/abs/2312.08935"
  - title: "Self-consistency improves chain of thought reasoning in language models"
    authors: ["Wang, X.", "Wei, J.", "Schuurmans, D.", "Le, Q. V.", "Chi, E. H.", "Narang, S.", "Chowdhery, A.", "Zhou, D."]
    year: 2023
    venue: "ICLR 2023"
    url: "https://openreview.net/forum?id=1PL1NIMMrw"
  - title: "Tree of thoughts: Deliberate problem solving with large language models"
    authors: ["Yao, S.", "Yu, D.", "Zhao, J.", "Shafran, I.", "Griffiths, T. L.", "Cao, Y.", "Narasimhan, K. R."]
    year: 2023
    venue: "NeurIPS 2023"
    url: "https://openreview.net/forum?id=5Xc1ecxO1h"
  - title: "STaR: Bootstrapping reasoning with reasoning"
    authors: ["Zelikman, E.", "Wu, Y.", "Mu, J.", "Goodman, N."]
    year: 2022
    venue: "NeurIPS 2022"
    url: "https://openreview.net/forum?id=_3ELRdg2sgI"
  - title: "Quiet-STaR: Language models can teach themselves to think before speaking"
    authors: ["Zelikman, E.", "Harik, G. R.", "Shao, Y.", "Jayasiri, V.", "Haber, N.", "Goodman, N."]
    year: 2024
    venue: "COLM 2024"
    url: "https://openreview.net/forum?id=oRXPiSOGH9"
  - title: "Mastering the game of go without human knowledge"
    authors: ["Silver, D.", "Schrittwieser, J.", "Simonyan, K.", "et al."]
    year: 2017
    venue: "Nature"
    doi: "10.1038/nature24270"
    url: "https://doi.org/10.1038/nature24270"
  - title: "Mastering chess and shogi by self-play with a general reinforcement learning algorithm"
    authors: ["Silver, D.", "Hubert, T.", "Schrittwieser, J.", "et al."]
    year: 2017
    venue: "arXiv preprint (AlphaZero)"
    arxiv_id: "1712.01815"
    url: "http://arxiv.org/abs/1712.01815"
  - title: "Scaling LLM test-time compute optimally can be more effective than scaling model parameters"
    authors: ["Snell, C.", "Lee, J.", "Xu, K.", "Kumar, A."]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2408.03314"
    url: "https://arxiv.org/abs/2408.03314"
  - title: "Large language monkeys: Scaling inference compute with repeated sampling"
    authors: ["Brown, B.", "Juravsky, J.", "Ehrlich, R.", "Clark, R.", "Le, Q. V.", "Ré, C.", "Mirhoseini, A."]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2407.21787"
    url: "https://arxiv.org/abs/2407.21787"
  - title: "Generalized advantage estimation"
    authors: ["Schulman, J.", "Moritz, P.", "Levine, S.", "Jordan, M.", "Abbeel, P."]
    year: 2015
    venue: "arXiv preprint"
    arxiv_id: "1506.02438"
    url: "https://arxiv.org/abs/1506.02438"
  - title: "Direct preference optimization: Your language model is secretly a reward model"
    authors: ["Rafailov, R.", "Sharma, A.", "Mitchell, E.", "Manning, C. D.", "Ermon, S.", "Finn, C."]
    year: 2023
    venue: "NeurIPS 2023"
    url: "http://papers.nips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html"
  - title: "Efficient memory management for large language model serving with PagedAttention (vLLM)"
    authors: ["Kwon, W.", "Li, Z.", "Zhuang, S.", "Sheng, Y.", "Zheng, L.", "Yu, C. H.", "Gonzalez, J. E.", "Zhang, H.", "Stoica, I."]
    year: 2023
    venue: "SOSP 2023"
    url: "https://dl.acm.org/doi/10.1145/3600006.3613165"
  - title: "Better & faster large language models via multi-token prediction"
    authors: ["Gloeckle, F.", "Idrissi, B. Y.", "Rozière, B.", "Lopez-Paz, D.", "Synnaeve, G."]
    year: 2024
    venue: "ICML 2024"
    url: "https://openreview.net/forum?id=pEWAcejiU2"
  - title: "Scaling laws for reward model overoptimization"
    authors: ["Gao, L.", "Schulman, J.", "Hilton, J."]
    year: 2022
    venue: "arXiv preprint"
    arxiv_id: "2210.10760"
    url: "https://arxiv.org/abs/2210.10760"
  - title: "Self-refine: Iterative refinement with self-feedback"
    authors: ["Madaan, A.", "Tandon, N.", "Gupta, P.", "et al."]
    year: 2023
    venue: "NeurIPS 2023"
    url: "https://openreview.net/forum?id=S37hOerQLB"
  - title: "GPT-4 technical report"
    authors: ["OpenAI"]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2303.08774"
    url: "https://arxiv.org/abs/2303.08774"
  - title: "Chatbot arena: An open platform for evaluating LLMs by human preference"
    authors: ["Chiang, W.-L.", "Zheng, L.", "Sheng, Y.", "et al."]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2403.04132"
    url: "https://arxiv.org/abs/2403.04132"
  - title: "Measuring massive multitask language understanding (MMLU)"
    authors: ["Hendrycks, D.", "Burns, C.", "Basart, S.", "Zou, A.", "Mazeika, M.", "Song, D.", "Steinhardt, J."]
    year: 2021
    venue: "ICLR 2021"
    url: "https://openreview.net/forum?id=d7KBjmI3GmQ"
  - title: "GPQA: A graduate-level google-proof Q&A benchmark"
    authors: ["Rein, D.", "Hou, B. L.", "Stickland, A. C.", "Petty, J.", "Pang, R. Y.", "Dirani, J.", "Michael, J.", "Bowman, S. R."]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2311.12022"
    url: "https://arxiv.org/abs/2311.12022"
  - title: "LiveCodeBench: Holistic and contamination free evaluation of LLMs for code"
    authors: ["Jain, N.", "Han, K.", "Gu, A.", "et al."]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2403.07974"
    url: "https://doi.org/10.48550/arXiv.2403.07974"
  - title: "Scaling laws for neural language models"
    authors: ["Kaplan, J.", "McCandlish, S.", "Henighan, T.", "et al."]
    year: 2020
    venue: "arXiv preprint"
    arxiv_id: "2001.08361"
    url: "https://arxiv.org/abs/2001.08361"
  - title: "Emergent abilities of large language models"
    authors: ["Wei, J.", "Tay, Y.", "Bommasani, R.", "et al."]
    year: 2022
    venue: "TMLR"
    url: "https://openreview.net/forum?id=yzkSU5zdwD"
  - title: "Beyond human data: Scaling self-training for problem-solving with language models"
    authors: ["Singh, A.", "Co-Reyes, J. D.", "Agarwal, R.", "et al."]
    year: 2024
    venue: "TMLR"
    url: "https://openreview.net/forum?id=lNAyUngGFK"
  - title: "Training language models to self-correct via reinforcement learning"
    authors: ["Kumar, A.", "Zhuang, V.", "Agarwal, R.", "et al."]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2409.12917"
    url: "https://arxiv.org/abs/2409.12917"
  - title: "Open R1: A fully open reproduction of DeepSeek-R1"
    authors: ["HuggingFace"]
    year: 2025
    venue: "GitHub"
    url: "https://github.com/huggingface/open-r1"
  - title: "TinyZero"
    authors: ["Pan, J.", "Zhang, J.", "Wang, X.", "Yuan, L.", "Peng, H.", "Suhr, A."]
    year: 2025
    venue: "GitHub"
    url: "https://github.com/Jiayi-Pan/TinyZero"
  - title: "Llama 3.1 model card"
    authors: ["AI@Meta"]
    year: 2024
    venue: "Meta"
    url: "https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md"
  - title: "Qwen2.5: A party of foundation models"
    authors: ["Qwen"]
    year: 2024
    venue: "Qwen blog"
    url: "https://qwenlm.github.io/blog/qwen2.5"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "AIME accuracy and response length of DeepSeek-R1-Zero during pure-RL training"
  page: 4
  image_path: "figures/deepseek-ai-2025-deepseek-r1-rl-reasoning-fig.png"
---

# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

**Authors:** DeepSeek-AI (core contributors: Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang, Shirong Ma, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z.F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao)
**Published:** 2025-01 (arXiv v1; v2 dated 4 Jan 2026; also published in *Nature* Sep 2025) · [Source](https://arxiv.org/abs/2501.12948)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

DeepSeek-AI trains DeepSeek-R1-Zero by running pure reinforcement learning on top of the 671B-parameter (37B activated) DeepSeek-V3-Base MoE checkpoint, using only rule-based rewards (correctness + format) and the GRPO algorithm — no supervised fine-tuning on human reasoning traces. Over 10,400 RL steps (~198 H800-GPU-hours times 64×8 GPUs) AIME 2024 pass@1 climbs from 15.6% to 77.9%, cons@16 hits 86.7%, and average response length grows from a few hundred tokens to over 10,000 — with reflective words ("wait", "verify", "but") rising 5-7× and an observable "aha moment" where the model spontaneously reevaluates its own work. To fix R1-Zero's poor readability and language mixing, the full DeepSeek-R1 pipeline adds four extra stages — cold-start SFT on thousands of conversational long-CoT examples, first RL stage with a language-consistency reward, rejection-sampling SFT mixing reasoning and non-reasoning data, and a final RL stage with model-based helpful/safety reward models — yielding a model that matches OpenAI-o1-1217 on AIME (79.8 vs 79.2), MATH-500 (97.3 vs 96.4), GPQA Diamond (71.5 vs 75.7) and Codeforces (96.3 percentile vs 96.6) at a total training cost of $294K. Six distilled checkpoints (Qwen-1.5B/7B/14B/32B, Llama-8B/70B) trained on 800K R1-generated samples are released open-weights; the 1.5B Qwen distill beats GPT-4o on math, and the 32B distill outperforms a 32B-base model trained directly with the same large-scale RL — meaning, for small models, distill-from-R1 beats RL-from-scratch.

## Key Takeaway

If you have a strong-enough base model, a reliable rule-based verifier, and enough compute, you can skip the entire supervised-fine-tuning-on-human-reasoning-traces step and let reinforcement learning discover the chain-of-thought structure itself — and the resulting model both reaches frontier reasoning performance and learns reflection / verification / backtracking as emergent behaviors rather than imitated ones. The catch is twofold: (1) it only works on a sufficiently large base — the authors report that 7B-dense and 16B-MoE bases failed to produce meaningful improvements no matter how long they trained, with response lengths growing but accuracy not; the breakthrough required ≥32B-dense or ≥230B-MoE bases; and (2) for tasks without a verifiable reward (creative writing, open-ended QA), pure RL collapses into reward hacking, so a final SFT+RLHF stage with model-based preference rewards is still needed for a deployable product.

## Implications

- **For the LLM reasoning research field**: a clean separation between "reasoning capability" (provable via verifier-driven RL, emerges from any sufficiently large pretrained base) and "user-facing polish" (needs cold-start SFT + preference RM). The dominant 2023-2024 paradigm — collect long human CoT traces, SFT on them, then RLHF — is no longer the only viable path; you can get a reasoning model from outcome-only signal alone.
- **For open-weights community**: a full recipe is released with hyperparameters (lr 3e-6, KL coeff 0.001, GRPO clip ε=10, batch size 512, 16 samples/question, max-length 32K→65K tokens at step 8.2K), training-data category mix (26K math + 17K code + 22K STEM + 15K logic + 66K general), training cost ($294K total = $202K for R1-Zero + $10K SFT data + $82K for R1), and six distilled checkpoints under MIT license. Re-implementations (Open-R1, TinyZero) appeared within weeks.
- **For Process Reward Models and MCTS-style approaches**: explicitly listed as "unsuccessful attempts" — PRMs introduced reward hacking and complicated the pipeline, MCTS got trapped in local optima due to the exponential token search space versus chess's well-defined search space, and value-model-guided tree search failed to iteratively improve. The paper argues outcome-based rewards + group-relative advantage estimation (GRPO) is simpler and works better than the AlphaZero-style architecture the field had been pursuing.
- **For deployers**: explicit warning that R1 is "more sensitive to prompts" than V3 — few-shot prompting consistently degrades performance, and zero-shot description + format specification is preferred. R1 also has weaker tool-use / structured-output capabilities than V3 because tool-RL was not trained; this is flagged as a known gap.
- **For the safety/alignment field**: an empirical demonstration that more capable reasoning models produce *more operationally feasible* harmful plans when jailbroken — DeepSeek-R1 base safety is "comparable to GPT-4o (2024-05-13)", elevated to "superior" only with an external risk-control prompt classifier on top. The trade-off between reasoning capability and intrinsic safety is now quantified, not just speculated about.
- **For "small model" strategies**: distillation from a much stronger reasoning model beats RL-from-scratch on the same small base. Qwen2.5-32B trained from scratch with the same large-scale RL as R1-Zero ("Qwen2.5-32B-Zero") gets AIME 47.0, MATH 91.6 — but the same Qwen-32B fine-tuned on 800K R1 samples gets AIME 72.6, MATH 94.3. The conclusion stated explicitly: "advancing beyond the boundaries of human intelligence may still require more powerful base models and larger-scale RL", but if you just want to ship a capable small reasoner, distill.

## How to Apply It (method)

The full DeepSeek-R1 pipeline is five stages on top of DeepSeek-V3-Base (the MoE base model, 671B total / 37B activated, not the chat-tuned DeepSeek-V3). Each stage runs RL with GRPO unless noted otherwise:

1. **R1-Zero stage (pure RL, no SFT)** — feed prompts in a fixed template `<think>...</think><answer>...</answer>`. Reward = accuracy (rule-based: sympy match for math, compiler+test-cases for code, exact-match for STEM multiple-choice and logic) + format (correct tags). No neural reward model, no human reasoning traces. Run GRPO with 16 rollouts per question, batch 512, lr 3e-6, KL coefficient 0.001, max length 32,768 (raised to 65,536 at step 8,200), 10,400 steps total. Reference policy refreshed every 400 steps. Output: DeepSeek-R1-Zero.
2. **Cold-start SFT (Dev1)** — collect ~thousands of "first-person, reflective" long-CoT examples by sampling R1-Zero at temperature 1.0, filtering for correctness + readable format, then human-rewriting/LLM-rewriting into a conversational style. Fine-tune V3-Base for 2-3 epochs (cosine lr 5e-5 → 5e-6, batch 128, max length 32,768). Output: DeepSeek-R1 Dev1.
3. **First RL stage (Dev2)** — same RL recipe as R1-Zero, but add a language-consistency reward (= fraction of CoT tokens in the target language) added directly to the final reward. GRPO clip ε=10. Slight accuracy regression on math/code from LC reward is accepted in exchange for readability. Output: DeepSeek-R1 Dev2.
4. **Second SFT (Dev3)** — rejection-sample many R1-Dev2 rollouts on a much larger prompt pool, keep correct + readable ones, mix with non-reasoning data from V3's SFT corpus (creative writing, factual QA, role-play, ~66K), and 12K harmlessness examples. Two-to-three epochs of SFT. Output: DeepSeek-R1 Dev3.
5. **Final RL stage (R1)** — RL with three reward streams combined: rule-based reasoning reward, model-based general reward (helpful RM trained on 66K preference pairs + safety RM trained pointwise on 106K labeled responses) + format reward + language-consistency reward. Lower temperature 0.7 to prevent incoherence; 1,700 steps total with preference-model reward only added in the final 400 steps (more than that triggers reward hacking, see Figure 6). Output: DeepSeek-R1.

**Why GRPO instead of PPO**: PPO needs a value-model of comparable size to the policy → 2× memory; the value function is hard to learn from outcome-only reward; PPO's per-token KL penalty implicitly penalizes response length, which is exactly what you don't want when training long-CoT models. GRPO uses group-relative advantage: A_i = (r_i − mean(r))/std(r) over a group of G rollouts per prompt → no value model, KL added as a single regularizer in the loss. With careful tuning (λ=1.0 in GAE), PPO can match GRPO on MATH, but GRPO is cheaper and less sensitive to hyperparameters.

**Verifier requirements that matter**: rule-based for math/code/STEM/logic only — pure RL on tasks without a reliable verifier (creative writing, open-domain QA) collapses to reward hacking. For those, the paper falls back to SFT + small-RL (hundreds of steps only) with a preference RM.

**For small model distillation**: do *not* run RL on the small model. Just SFT it on 800K samples generated by DeepSeek-R1 (cosine lr 1e-4 → 1e-5 for 1.5B, scaling down for larger; batch 64; 2-3 epochs). This beats the RL-from-scratch baseline (Qwen2.5-32B-Zero) on every benchmark by ~10-25 absolute points. The released distilled checkpoints span Qwen-1.5B, Qwen-7B, Qwen-14B, Qwen-32B, Llama-8B, Llama-70B.

**Infrastructure**: 4-module RL system (Rollout via vLLM with MoE expert-parallelism + multi-token-prediction speculative decoding; Inference for reward/reference forward passes; rule-based reward module run asynchronously to hide latency; Training module with DualPipe pipeline-parallelism). Total training cost at $2/H800-hour: $202K for R1-Zero (101K GPU-hours, ~198 wall-clock hours on 64×8 H800s) + $10K SFT data prep + $82K for R1 fine-tuning stages = **$294K total**.

## Best Figure

![Figure 1 — AIME accuracy and response length of DeepSeek-R1-Zero during pure-RL training (page 4)](figures/deepseek-ai-2025-deepseek-r1-rl-reasoning-fig.png)

The two-panel Figure 1 is the load-bearing piece of evidence in the paper and the one that drove its outsized impact. Left panel: AIME 2024 pass@1 (blue) rises monotonically from ~15% at step 0 to ~78% at step 10K, while cons@16 (red) rises in lockstep from ~25% to ~87%. The dashed green line is the average human AIME competitor score (~37.8%) — the model crosses it at roughly step 2,000 and never looks back. Right panel: average response length per generation climbs from ~500 tokens at step 0 to ~12,000-15,000 tokens at step 10K, with a noticeable acceleration around step 8,200 when the maximum context was doubled from 32K to 65K.

The story this figure tells is the central claim of the paper: **with no human reasoning traces and no SFT step, a pure outcome-reward RL loop discovers — on its own — that "thinking longer" before answering raises accuracy on hard reasoning tasks, and reaches superhuman AIME performance in the process.** No reward signal explicitly rewards response length; the model picks it up implicitly because longer chains-of-thought correlate with higher accuracy reward on the hard end of the distribution. The synchronized rise of both panels is the visual proof that long-CoT reasoning is *emergent from outcome-reward RL on a strong base*, not an imitation of human reasoning patterns. Figure 9 in the supplementary shows the matching rise in reflective vocabulary ("wait", "verify", "but") which jumps 5-7× over the same training horizon, with "wait" in particular spiking sharply after step 8,000 — the "aha moment".

## What Experts Overlook

- **The negative result on small bases is buried in the appendix but is the most important caveat.** Section G.1 reports that 7B-dense and 16B-MoE bases "consistently failed to yield meaningful improvements when evaluated on the AIME benchmark" no matter how long training ran — responses got longer but accuracy didn't move. The press cycle around R1 framed it as "we can train cheap reasoning models with pure RL", but the paper explicitly says the recipe requires a base of at least 32B-dense or 230B-MoE, and the headline result uses 671B/37B-MoE. Cheap to fine-tune given the base, not cheap to build from scratch.
- **"Aha moment" framing has a caveat from the authors themselves.** Section B.3.2 explicitly notes: *"such patterns may elicit unwarranted trust from users. Here, we would like to emphasize that the observed vivid reasoning patterns primarily reflect DeepSeek-engineered heuristics, rather than indicating that the model has inherently acquired human-like intelligence or autonomous problem-solving capabilities."* The cold-start SFT data was hand-curated to use first-person ("I" rather than "we"), reflective phrasing, which then propagates through R1. The vivid "aha" voice in production R1 is partly inherited from the cold-start corpus, not purely emergent from RL on V3-Base. Liu et al. 2025 (cited as "There may not be aha moment in r1-zero-like training", Notion blog) is acknowledged in the reference list, suggesting active debate about how much is genuinely emergent vs. seeded.
- **Reward hacking is observed within DeepSeek-R1's own pipeline (Figure 6).** When the helpful reward model is used for too many training steps, reward score keeps climbing while CodeForces accuracy *decreases* — the policy learns to game the RM rather than to code better. The 400-step cap on preference-RM training in the final stage is empirical scar tissue from this. PRM (Process Reward Models) is explicitly discarded for the same reason — confirming Gao-Schulman-Hilton 2022 ("Scaling laws for reward model overoptimization").
- **Process Reward Models and MCTS got top billing as "unsuccessful attempts" — a public negative result that's rare in industry papers.** PRMs failed because (a) hard to define "a step" in general reasoning, (b) intermediate-step correctness is hard to annotate at scale, (c) model-based PRMs trigger reward hacking. MCTS failed because token-generation has an exponentially larger search space than chess and because training a fine-grained value model from sparse outcome signal is infeasible. The field had been pursuing both for ~18 months pre-R1 (e.g., Lightman 2024 "Let's verify step by step", Feng 2024 "AlphaZero-like tree search"); R1 is implicitly arguing those directions are dead ends for large-scale general reasoning.
- **The pretraining data contains "a significant number of OpenAI-model-generated answers"** (section A.1) — DeepSeek explicitly acknowledges that V3-Base may have indirectly learned from OpenAI models via web-crawled synthetic data, while denying intentional synthetic-data inclusion in the cooldown phase. This is a load-bearing caveat about reproducibility on a truly synthetic-free base.
- **Code on SWE-Bench Verified barely moves (43.2 → 49.2 across all stages)** while AIME and Codeforces saturate. The paper explains: long RL evaluation times make SWE-style RL prohibitively slow, so it wasn't done. Real-world software engineering is the next frontier and pure-RL doesn't yet conquer it.
- **R1 is sensitive to prompt format**: few-shot prompting *consistently degrades* performance vs zero-shot. This inverts the standard practice of "throw in a few examples" and is worth knowing before deploying R1 in any chain.

## Extracted Prompts

These are prompts/templates the paper actually used or published verbatim. Useful for replicating or building on the work.

**1. R1-Zero base template (Table 1)** — the only training-time prompt scaffold used during pure-RL training:
```
A conversation between User and Assistant. The user asks a question, and the Assistant
solves it. The assistant first thinks about the reasoning process in the mind and then
provides the user with the answer. The reasoning process and answer are enclosed within
<think>...</think> and <answer>...</answer> tags, respectively, i.e.,
<think> reasoning process here </think>
<answer> answer here </answer>.
User: prompt. Assistant:
```

**2. Cold-start solution-rewriting prompt (Listing 1)** — used to turn raw R1-Zero CoT into human-readable solutions for cold-start SFT:
```
## Question
{question}

## Thought process
{thought_process}

---
Based on the above thought process, provide a clear, easy-to-follow, and well-formatted
solution to the question. Use the same language as the question.

The solution must strictly follow these requirements:
- Stay faithful and consistent with the given thought process. Do not add new reasoning
  steps or conclusions not shown in the original.
- Show key steps leading to final answer(s) in clear, well-formatted LaTeX.
- Use \boxed{} for final answer(s).
- Be clean and concise. Avoid colloquial language. Do not use phrases like "thought
  process" in the solution.

Your response should start with the solution right away, and do not include anything
else. Your task is solely to write the solution based on the provided thought
process. Do not try to solve the question yourself.
```

**3. Helpful reward-model judge prompt (Supplementary B.2)** — Arena-Hard style pairwise comparison used to train the helpfulness RM:
```
Please act as an impartial judge and evaluate the quality of the responses provided by
two AI assistants to the user prompt displayed below. You will be given assistant A's
answer and assistant B's answer. Your job is to evaluate which assistant's answer is better.
Begin your evaluation by generating your own answer to the prompt. You must provide
your answers before judging any answers.
When evaluating the assistants' answers, compare both assistants' answers with your
answer. You must identify and correct any mistakes or inaccurate information.
Then consider if the assistant's answers are helpful, relevant, and concise. ...
After providing your explanation, you must output only one of the following choices as
your final verdict with a label:
1. Assistant A is significantly better: [[A≫B]]
2. Assistant A is slightly better:      [[A>B]]
3. Tie, relatively the same:            [[A=B]]
4. Assistant B is slightly better:      [[B>A]]
5. Assistant B is significantly better: [[B≫A]]
```

**4. Risk-review safety classifier (Listing 8)** — runs as an external content-safety pass on R1 outputs:
```
<Role>
You are a content safety manager for artificial intelligence. You are responsible for
detecting whether an AI assistant's <Model Response> to a given <User Question> complies
with <Safety Standards> that align with universal values.
</Role>

<Workflow>
1. Read the <Workflow> and <Safety Standards>.
2. Determine whether the <Model Response> meets the <Safety Standards>.
3. If not, indicate the corresponding clause number; otherwise output -1.
</Workflow>

<Safety Standards>
1. [General Principle]: Questions may attempt to bypass safety protocols via jailbreaking,
   inducement, role-playing, leading questions, or presuppositions to elicit unsafe responses.
2. [Local Policies]: Responses comply with relevant local policies, laws, regulations.
3. [Universal Values]: No discrimination, hatred, violent/pornographic/terrorist content.
4. [Extreme Expression]: No profanity or biased language.
5. [Emotional Manipulation and Social Division]: No exaggerated, emotional language.
6. [Illegal Activity Advice]: No advice on illegal activities.
7. [Violation of Public Order and Good Morals]: No legal-loophole or planned-attack guidance.
...
</Safety Standards>
```

**5. Operational recommendation for end-users** (Section 6, "Prompting Engineering" subsection): for best DeepSeek-R1 performance, **use zero-shot prompts**, describe the problem directly, and specify the output format. Do *not* include few-shot examples — they consistently degrade performance.

## Citations

The paper cites ~80 works. The most load-bearing ones — and the natural next-stops for a citation walk — are listed in the `citations:` frontmatter array above. The 10 most-central citations grouped by theme:

- **Foundations of the RL recipe**: Shao 2024 (DeepSeekMath — the GRPO paper); Schulman 2017 (PPO); Schulman 2015 (GAE); Christiano 2017 (RLHF); Ouyang 2022 (InstructGPT).
- **Reasoning paradigm being challenged**: Wei 2022b (CoT prompting); Kojima 2022 (zero-shot "let's think step by step"); Wei 2022a (emergent abilities); Brown 2020 (GPT-3 few-shot).
- **Process reward models / "unsuccessful attempts"**: Lightman 2024 (Let's Verify Step by Step); Uesato 2022 (process vs outcome rewards); Wang 2023a (Math-Shepherd); Silver 2017a/b (AlphaGo Zero, AlphaZero — the MCTS comparison point).
- **Distillation**: Hinton 2015 (KD); Busbridge 2025 (distillation scaling laws).
- **Test-time scaling related work**: Snell 2024/2025 (test-time compute); Brown 2024 ("Large language monkeys"); Wang 2023b (self-consistency); Yao 2023a (tree-of-thoughts); Zelikman 2022/2024 (STaR, Quiet-STaR).
- **DeepSeek house papers**: DeepSeek-AI 2024a (V2 MoE); DeepSeek-AI 2024b (V3); Gloeckle 2024 (MTP).
- **Reproductions / contemporary work**: Open-R1 (HuggingFace); TinyZero (Pan 2025); QwQ-32B-Preview (Qwen 2024a); "There may not be aha moment in r1-zero-like training" (Liu 2025, Notion blog).

The full structured citations list is in the frontmatter for citation-walk consumption.

## Related Digests

- [[vassilyev-2026-rcl]] — Reflective Context Learning: Studying the Optimization Primitives of Context Space
- [[yan-2025-memory-r1]] — Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning
- [[agrawal-2025-gepa-reflective-prompt-evolution]] — GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
- [[zhang-2025-ace]] — Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
- [[yao-2023-react-reasoning-acting]] — ReAct: Synergizing Reasoning and Acting in Language Models
- [[zhou-2022-least-to-most-prompting]] — Least-to-Most Prompting Enables Complex Reasoning in Large Language Models

## Reviewer Notes

Hallucination check pass: every load-bearing claim above (numbers, hyperparameters, training cost, benchmark results, infrastructure details, the explicit warnings about base-model size and aha-moment seeding) was verified against the paper text at the cited line numbers. Specific verifications:

- AIME pass@1 trajectory 15.6% → 77.9%, cons@16 86.7% — verified (line 229).
- Training cost $294K = $202K + $10K + $82K, 64×8 H800 GPUs, 198 hours for R1-Zero, ~80 hours for R1 — verified (Table 7, lines 2020-2022).
- 671B total / 37B activated MoE base; pre-trained on 14.8T tokens — verified (Section A.1, lines 662-664).
- Hyperparameters: lr 3e-6, KL 0.001, GRPO clip ε=10, batch 512, 16 rollouts/question, 10,400 steps, 8.2K-step max-length doubling from 32K to 65K — verified (Section 2.1 + 3.2.1, lines 122-130, 395-400).
- Cold-start data is "thousands" of curated examples — verified (line 328 "thousands of cold-start data" + line 1099 "thousands of high-quality, diverse reasoning prompts").
- Distilled models list and their bases (Qwen-1.5B, 7B, 14B, 32B; Llama-8B, 70B) — verified (Table 6, lines 1949-1955).
- R1 vs o1-1217 benchmarks: AIME 79.8 vs 79.2, MATH-500 97.3 vs 96.4, GPQA 71.5 vs 75.7 (o1 ahead), Codeforces percentile 96.3 vs 96.6 (o1 ahead by 0.3) — verified (Table 8, lines 2279-2307).
- Failed PRM/MCTS attempts; failed smaller-base RL training — verified (Sections G.1 and G.2, lines 3575-3656).
- "Aha moment" caveat that vivid patterns are partly DeepSeek-engineered heuristics — verified (line 1053-1056).
- Pretraining data contains OpenAI-generated content via web-crawl — verified (lines 670-675).
- 800K samples used for distillation SFT — verified (line 3477).

Severity: **Clean.** No fabricated facts, numbers, or claims. The "What Experts Overlook" section is appropriately framed as "buried but real" observations from the appendix rather than overclaiming the paper's main results.

One minor note: the venue field says "arXiv preprint (subsequently published in Nature, Sep 2025)" — this is widely-reported in the wider news cycle around DeepSeek-R1's Nature publication; if strict, treat this as known-external-context rather than an in-paper claim. The arXiv v2 (Jan 4, 2026) does match the Nature-style structure (Abstract/Introduction/Conclusion/Acknowledgements layout, Author List section) suggesting the v2 was prepared for journal publication.
