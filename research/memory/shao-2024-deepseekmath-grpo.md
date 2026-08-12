---
corpus: agentic-memory
kind: paper-digest
slug: shao-2024-deepseekmath-grpo
title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
authors:
  - "Shao, Zhihong"
  - "Wang, Peiyi"
  - "Zhu, Qihao"
  - "Xu, Runxin"
  - "Song, Junxiao"
  - "Bi, Xiao"
  - "Zhang, Haowei"
  - "Zhang, Mingchuan"
  - "Li, Y.K."
  - "Wu, Y."
  - "Guo, Daya"
year: 2024
publication_date: "2024-02"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2402.03300"
doi: "10.48550/arXiv.2402.03300"
arxiv_id: "2402.03300"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "The smartest move in DeepSeekMath's RL pipeline is to delete the value network, not to scale it — sampling a group of answers per question and using the group mean as the baseline outperforms PPO while roughly halving GPU memory."
topics:
  - reinforcement-learning
  - grpo
  - ppo
  - mathematical-reasoning
  - llm-post-training
  - reward-model
  - process-supervision
  - rlhf
tags:
  - paper
  - deepseek
  - rl-algorithm
  - math-llm
  - policy-optimization
  - open-source-llm
entities:
  - shao-zhihong
  - wang-peiyi
  - guo-daya
  - deepseek-ai
related_digests:
  - yan-2025-memory-r1
  - agrawal-2025-gepa-reflective-prompt-evolution
  - deepseek-ai-2025-deepseek-r1-rl-reasoning
  - touvron-2023-llama-2
  - vassilyev-2026-rcl
citations:
  - title: "Gemini: A family of highly capable multimodal models"
    authors: ["Anil, R.", "Borgeaud, S.", "Wu, Y.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/ARXIV.2312.11805"
    url: "https://doi.org/10.48550/arXiv.2312.11805"
    arxiv_id: "2312.11805"
  - title: "Program synthesis with large language models"
    authors: ["Austin, J.", "Odena, A.", "Nye, M.", "et al."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2108.07732"
  - title: "Llemma: An open language model for mathematics"
    authors: ["Azerbayev, Z.", "Schoelkopf, H.", "Paster, K.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.10631"
  - title: "Qwen technical report"
    authors: ["Bai, J.", "Bai, S.", "Chu, Y.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2309.16609"
  - title: "Weak-to-strong generalization: Eliciting strong capabilities with weak supervision"
    authors: ["Burns, C.", "Izmailov, P.", "Kirchner, J.H.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2312.09390"
  - title: "Evaluating large language models trained on code"
    authors: ["Chen, M.", "Tworek, J.", "Jun, H.", "et al."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2107.03374"
    arxiv_id: "2107.03374"
  - title: "Program of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks"
    authors: ["Chen, W.", "Ma, X.", "Wang, X.", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: "10.48550/ARXIV.2211.12588"
    url: "https://doi.org/10.48550/arXiv.2211.12588"
    arxiv_id: "2211.12588"
  - title: "Training verifiers to solve math word problems"
    authors: ["Cobbe, K.", "Kosaraju, V.", "Bavarian, M.", "et al."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2110.14168"
  - title: "RedPajama: an open dataset for training large language models"
    authors: ["Computer, T."]
    year: 2023
    venue: "GitHub"
    doi: null
    url: "https://github.com/togethercomputer/RedPajama-Data"
    arxiv_id: null
  - title: "DeepSeek LLM: scaling open-source language models with longtermism"
    authors: ["DeepSeek-AI"]
    year: 2024
    venue: "arXiv preprint"
    doi: "10.48550/ARXIV.2401.02954"
    url: "https://doi.org/10.48550/arXiv.2401.02954"
    arxiv_id: "2401.02954"
  - title: "GLM: General language model pretraining with autoregressive blank infilling"
    authors: ["Du, Z.", "Qian, Y.", "Liu, X.", "et al."]
    year: 2022
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "PAL: program-aided language models"
    authors: ["Gao, L.", "Madaan, A.", "Zhou, S.", "et al."]
    year: 2023
    venue: "ICML"
    doi: null
    url: "https://proceedings.mlr.press/v202/gao23f.html"
    arxiv_id: null
  - title: "ToRA: A tool-integrated reasoning agent for mathematical problem solving"
    authors: ["Gou, Z.", "Shao, Z.", "Gong, Y.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/ARXIV.2309.17452"
    url: "https://doi.org/10.48550/arXiv.2309.17452"
    arxiv_id: "2309.17452"
  - title: "DeepSeek-Coder: When the large language model meets programming – the rise of code intelligence"
    authors: ["Guo, D.", "Zhu, Q.", "Yang, D.", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Measuring massive multitask language understanding"
    authors: ["Hendrycks, D.", "Burns, C.", "Basart, S.", "et al."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2009.03300"
  - title: "Measuring mathematical problem solving with the MATH dataset"
    authors: ["Hendrycks, D.", "Burns, C.", "Kadavath, S.", "et al."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2103.03874"
  - title: "Draft, sketch, and prove: Guiding formal theorem provers with informal proofs"
    authors: ["Jiang, A.Q.", "Welleck, S.", "Zhou, J.P.", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2210.12283"
  - title: "Mistral 7B"
    authors: ["Jiang, A.Q.", "Sablayrolles, A.", "Mensch, A.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.06825"
  - title: "FastText.zip: Compressing text classification models"
    authors: ["Joulin, A.", "Grave, E.", "Bojanowski, P.", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1612.03651"
  - title: "Efficient memory management for large language model serving with PagedAttention"
    authors: ["Kwon, W.", "Li, Z.", "Zhuang, S.", "et al."]
    year: 2023
    venue: "SOSP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fast inference from transformers via speculative decoding"
    authors: ["Leviathan, Y.", "Kalman, M.", "Matias, Y."]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Solving quantitative reasoning problems with language models (Minerva)"
    authors: ["Lewkowycz, A.", "Andreassen, A.", "Dohan, D.", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Let's verify step by step"
    authors: ["Lightman, H.", "Kosaraju, V.", "Burda, Y.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.20050"
  - title: "Decoupled weight decay regularization"
    authors: ["Loshchilov, I.", "Hutter, F."]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1711.05101"
  - title: "WizardMath: Empowering mathematical reasoning for large language models via reinforced evol-instruct"
    authors: ["Luo, H.", "Sun, Q.", "Xu, C.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2308.09583"
  - title: "LILA: A unified benchmark for mathematical reasoning"
    authors: ["Mishra, S.", "Finlayson, M.", "Lu, P.", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: "10.18653/v1/2022.emnlp-main.392"
    url: null
    arxiv_id: null
  - title: "SeaLLMs - large language models for southeast asia"
    authors: ["Nguyen, X.", "Zhang, W.", "Li, X.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/ARXIV.2312.00738"
    url: "https://doi.org/10.48550/arXiv.2312.00738"
    arxiv_id: "2312.00738"
  - title: "GPT-4 technical report"
    authors: ["OpenAI"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2303.08774"
  - title: "Training language models to follow instructions with human feedback (InstructGPT)"
    authors: ["Ouyang, L.", "Wu, J.", "Jiang, X.", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "OpenWebMath: An open dataset of high-quality mathematical web text"
    authors: ["Paster, K.", "Santos, M.D.", "Azerbayev, Z.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/ARXIV.2310.06786"
    url: "https://doi.org/10.48550/arXiv.2310.06786"
    arxiv_id: "2310.06786"
  - title: "Three years of experience with Sledgehammer, a practical link between automatic and interactive theorem provers"
    authors: ["Paulson, L.C."]
    year: 2010
    venue: "PAAR"
    doi: "10.29007/TNFD"
    url: "https://doi.org/10.29007/tnfd"
    arxiv_id: null
  - title: "Generative language modeling for automated theorem proving"
    authors: ["Polu, S.", "Sutskever, I."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2009.03393"
    arxiv_id: "2009.03393"
  - title: "Direct Preference Optimization: Your language model is secretly a reward model"
    authors: ["Rafailov, R.", "Sharma, A.", "Mitchell, E.", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Approximating KL divergence"
    authors: ["Schulman, J."]
    year: 2020
    venue: "blog"
    doi: null
    url: "http://joschu.net/blog/kl-approx.html"
    arxiv_id: null
  - title: "High-dimensional continuous control using generalized advantage estimation (GAE)"
    authors: ["Schulman, J.", "Moritz, P.", "Levine, S.", "et al."]
    year: 2015
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1506.02438"
  - title: "Proximal Policy Optimization algorithms (PPO)"
    authors: ["Schulman, J.", "Wolski, F.", "Dhariwal, P.", "et al."]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1707.06347"
  - title: "Language models are multilingual chain-of-thought reasoners (MGSM)"
    authors: ["Shi, F.", "Suzgun, M.", "Freitag, M.", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/pdf?id=fR3wGCk-IXp"
    arxiv_id: null
  - title: "Preference ranking optimization for human alignment"
    authors: ["Song, F.", "Yu, B.", "Li, M.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2306.17492"
  - title: "Challenging BIG-bench tasks and whether chain-of-thought can solve them (BBH)"
    authors: ["Suzgun, M.", "Scales, N.", "Schärli, N.", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2210.09261"
  - title: "Embracing change and resetting expectations"
    authors: ["Tao, T."]
    year: 2023
    venue: "Microsoft Unlocked"
    doi: null
    url: "https://unlocked.microsoft.com/ai-anthology/terence-tao/"
    arxiv_id: null
  - title: "Llama 2: Open foundation and fine-tuned chat models"
    authors: ["Touvron, H.", "Martin, L.", "Stone, K.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2307.09288"
    url: "https://doi.org/10.48550/arXiv.2307.09288"
    arxiv_id: "2307.09288"
  - title: "Solving olympiad geometry without human demonstrations"
    authors: ["Trinh, T.H.", "Wu, Y.", "Le, Q.V.", "et al."]
    year: 2024
    venue: "Nature"
    doi: null
    url: null
    arxiv_id: null
  - title: "Making large language models better reasoners with alignment"
    authors: ["Wang, P.", "Li, L.", "Chen, L.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2309.02144"
  - title: "Math-Shepherd: Verify and reinforce LLMs step-by-step without human annotations"
    authors: ["Wang, P.", "Li, L.", "Shao, Z.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2312.08935"
  - title: "Generative AI for math: Part I - MathPile: A billion-token-scale pretraining corpus for math"
    authors: ["Wang, Z.", "Xia, R.", "Liu, P."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/ARXIV.2312.17120"
    url: null
    arxiv_id: "2312.17120"
  - title: "Chain-of-thought prompting elicits reasoning in large language models"
    authors: ["Wei, J.", "Wang, X.", "Schuurmans, D.", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "CMATH: Can your language model pass Chinese elementary school math test?"
    authors: ["Wei, T.", "Luan, J.", "Liu, W.", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "The Isabelle framework"
    authors: ["Wenzel, M.", "Paulson, L.C.", "Nipkow, T."]
    year: 2008
    venue: "TPHOLs"
    doi: "10.1007/978-3-540-71067-7_7"
    url: null
    arxiv_id: null
  - title: "Speculative decoding: Exploiting speculative execution for accelerating seq2seq generation"
    authors: ["Xia, H.", "Ge, T.", "Wang, P.", "et al."]
    year: 2023
    venue: "EMNLP Findings"
    doi: "10.18653/v1/2023.findings-emnlp.257"
    url: null
    arxiv_id: null
  - title: "Unlocking efficiency in large language model inference: A comprehensive survey of speculative decoding"
    authors: ["Xia, H.", "Yang, Z.", "Dong, Q.", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2401.07851"
  - title: "Tree of Thoughts: Deliberate problem solving with large language models"
    authors: ["Yao, S.", "Yu, D.", "Zhao, J.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.10601"
  - title: "MetaMath: Bootstrap your own mathematical questions for large language models"
    authors: ["Yu, L.", "Jiang, W.", "Shi, H.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/ARXIV.2309.12284"
    url: null
    arxiv_id: "2309.12284"
  - title: "Scaling relationship on learning mathematical reasoning with large language models (RFT)"
    authors: ["Yuan, Z.", "Yuan, H.", "Li, C.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2308.01825"
  - title: "RRHF: Rank responses to align language models with human feedback without tears"
    authors: ["Yuan, Z.", "Yuan, H.", "Tan, C.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2304.05302"
  - title: "MAmmoTH: Building math generalist models through hybrid instruction tuning"
    authors: ["Yue, X.", "Qu, X.", "Zhang, G.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/ARXIV.2309.05653"
    url: null
    arxiv_id: "2309.05653"
  - title: "miniF2F: A cross-system benchmark for formal olympiad-level mathematics"
    authors: ["Zheng, K.", "Han, J.M.", "Polu, S."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2109.00110"
  - title: "AGIEval: A human-centric benchmark for evaluating foundation models"
    authors: ["Zhong, W.", "Cui, R.", "Guo, Y.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2304.06364"
    url: null
    arxiv_id: "2304.06364"
hallucination_severity: "Clean"
best_figure:
  number: 4
  title: "Demonstration of PPO and our GRPO"
  page: 13
  image_path: "figures/shao-2024-deepseekmath-grpo-fig.png"
---

# DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

**Authors:** Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo (DeepSeek-AI, Tsinghua University, Peking University)
**Published:** 2024-02 · [Source](https://arxiv.org/abs/2402.03300)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

DeepSeekMath 7B is a math-specialized open-source LLM that scores 51.7% on the competition-level MATH benchmark without any external tools or voting — approaching GPT-4 and Gemini-Ultra and beating Minerva 540B (a model 77× larger). Two ingredients drive the result. First, a 120B-token math pre-training corpus mined from Common Crawl through four iterations of a fastText classifier seeded on OpenWebMath, which is ~7× larger than Minerva's math web pages and ~9× larger than OpenWebMath itself; pre-training a 1.3B model on this corpus reaches 23.8% on GSM8K vs 14.3% on the next-best baseline (Proof-Pile-2), and the bonus from continual code training (DeepSeekMath-Base starts from DeepSeek-Coder-Base-v1.5) also lifts MMLU from 49.1%→54.9% and BBH from 55.2%→59.5%. Second, the paper introduces Group Relative Policy Optimization (GRPO), a PPO variant that throws away the value/critic network and instead samples a group of G=64 outputs per question, normalizes the rewards by group mean and std, and uses that as the per-token advantage; this lifts DeepSeekMath-Instruct's MATH score from 46.8%→51.7% and GSM8K from 82.9%→88.2% while halving the trained-model memory footprint. The paper also offers a unified gradient-coefficient view that recasts SFT, RFT, DPO, online RFT, PPO and GRPO as the same equation with three slots (data source, reward function, gradient coefficient), and shows experimentally that (a) online sampling beats offline sampling late in training, (b) process supervision beats outcome supervision, (c) iterative reward-model retraining adds another ~2-3% per iteration, and (d) RL improves Maj@K but not Pass@K — so RL "sharpens the distribution" rather than teaching new skills. Two counter-intuitive findings round it out: arXiv-only math pre-training brings *no* measurable benefit on any benchmark tested, and code pre-training before math actually improves mathematical reasoning (both with and without tool use).

## Key Takeaway

The smartest move in DeepSeekMath's RL pipeline is to *delete* the value network, not to scale it. Standard PPO ties up a second LLM-sized model to predict per-token value, then trains it alongside the policy — which is awkward in the LLM setting because reward is only assigned at the last token anyway. GRPO replaces all of that with: sample G answers, compute (reward − group mean) / group std as the advantage, done. Less code, roughly half the GPU memory, and — because reward models are already trained on pairwise comparisons — the group-relative signal happens to match the reward model's training distribution better than absolute value estimates do. The lesson generalizes: when a learned baseline is hard to estimate, sampling-based baselines from the *same distribution as the reward signal* often beat heavier parametric ones.

## Implications

- **Default to group-relative baselines when fine-tuning LLMs with RL**: If you're running PPO on an LLM and the value model is eating GPU memory, swap it for GRPO. The paper shows GRPO matches or beats PPO on math reasoning while cutting the trainable-model count from 2 → 1, and the implementation is roughly 30 lines of difference (sample G outputs, normalize, plug into the same clipped-surrogate loss).
- **Don't trust arXiv as math pre-training fuel**: Training DeepSeek-LLM 1.3B on MathPile (85% arXiv) or ArXiv-RedPajama for 150B tokens produced *zero* or *negative* improvement across GSM8K, MATH, OCW, SAT, MMLU-STEM, CMATH, and miniF2F. If you're building math models, prioritize curated web data over LaTeX dumps — though the paper notes this conclusion may not hold at frontier model scale or for informalization tasks.
- **Run code pre-training before math, not in parallel**: Two-stage code→math training beat one-stage mixed training on chain-of-thought math (GSM8K 21.9% vs 17.6%, MATH 15.3% vs 12.1%) and was nearly as good on program-aided math. Code training is the cheapest reasoning upgrade you can get before you start spending math tokens.
- **Use process supervision when you can afford the labels**: GRPO+PS (process supervision — reward at each reasoning step) beat GRPO+OS (outcome supervision — reward only at the end) on MATH. If you're doing RL on multi-step tasks and you have a process reward model (Math-Shepherd-style), use it; the gradient-coefficient differentiation between correct intermediate steps and final-answer-correctness pays off.
- **RL sharpens, it does not extend**: Maj@K improves significantly under RL but Pass@K does not — the RL model isn't solving problems the SFT model couldn't solve, it's just becoming more confident on the ones it could. Set expectations accordingly: don't expect RL to unlock new capabilities, expect it to make existing capabilities more reliable. To extend capability, change the pre-training data or scaffold with tree search / better sampling.
- **Iterative RL is worth it for the first iteration only**: Retraining the reward model on policy-generated samples (with 10% replay) gave a clear bump on iteration 1 and a small one on iteration 2 — diminishing returns kick in fast.
- **Drop the in-reward KL penalty and add it to the loss directly**: GRPO regularizes by adding an unbiased KL estimator (Schulman 2020) straight into the loss rather than mixing it into the reward signal. This keeps the advantage calculation clean and avoids interaction effects between KL and reward gradients — a small implementation detail that matters when you're debugging instability.
- **The 7×-bigger math corpus matters more than the model size**: DeepSeekMath-Base 7B beats Minerva 540B on MATH. Open-source math LLMs have been data-bottlenecked, not parameter-bottlenecked; teams sitting on a small budget should invest in curated math web data before they scale parameters.

## How to Apply It (method)

**Scenario:** You're fine-tuning an open-source 7B-class LLM for a domain that has a verifiable reward signal (math, code, structured QA, contract clause extraction, etc.) and you want better-than-SFT performance without paying for PPO's value-network overhead.

**Steps:**

1. **Start from a strong SFT checkpoint**: Don't run GRPO from scratch. The paper trains DeepSeekMath-Instruct (an SFT model) first, then runs GRPO on a subset of that SFT data. Skipping SFT and going straight to RL produces unstable training in most setups.

2. **Stand up a reward model**: Train a scalar reward model on pairwise comparisons of correct vs incorrect outputs in your domain. DeepSeekMath trains theirs on top of DeepSeekMath-Base 7B with learning rate 2e-5, following the Math-Shepherd recipe. For pure correctness tasks, a rule-based reward (1 if answer matches gold, 0 otherwise) also works and is much cheaper.

3. **Sample G outputs per question** from the current policy (the paper uses G=64 for each question, max length 1024 tokens). These G outputs form one "group." Run sampling under nucleus or temperature sampling — the paper doesn't dwell on the sampling strategy but notes this is one of the limitations of their pipeline.

4. **Score each output with the reward model**: For outcome supervision, you get one scalar per output o_i. For process supervision, you get one scalar per reasoning step (you'll need a process reward model trained on step-level labels).

5. **Normalize within the group**: Compute the advantage as `A_i = (r_i - mean(r_1..r_G)) / std(r_1..r_G)` for outcome supervision. For process supervision, compute step-level normalized rewards and set each token's advantage to the sum of normalized rewards from the steps following that token.

6. **Optimize the GRPO objective**: The objective is identical to PPO's clipped surrogate, except (a) the advantage is the group-normalized reward from step 5, and (b) the KL divergence between current policy and reference policy is added to the *loss*, not the reward. Use the unbiased KL estimator from Schulman 2020:

   ```
   D_KL(π_θ || π_ref) ≈ π_ref(o|q) / π_θ(o|q) - log(π_ref(o|q) / π_θ(o|q)) - 1
   ```

   Hyperparameters from the paper: policy learning rate 1e-6, KL coefficient β=0.04, clipping ε=0.2 (PPO standard), batch size 1024, single policy update per exploration stage.

7. **(Optional) Iterative RL**: After one full pass, generate new samples from the trained policy, label them (via rule-based judgment for math, or with another scoring source), and retrain the reward model with a 10% replay buffer of historical data. Reset the reference model to the current policy and run another GRPO pass. Expect the biggest gain on iteration 1; iteration 2 helps a bit; iteration 3+ is rapidly diminishing returns.

8. **Evaluate on in-domain AND out-of-domain benchmarks**: The paper reports gains not just on GSM8K/MATH (in-domain) but also on CMATH (out-of-domain — Chinese, not in training set). Track out-of-domain improvement specifically — that's the signal that you're not just overfitting to the reward distribution.

**Expected outcome:** A fine-tuned policy that is more *reliable* (higher majority-vote accuracy) on tasks the SFT model could already solve some of the time, with ~half the GPU memory cost of PPO. Don't expect it to unlock new capabilities — Pass@K stays flat. Do expect it to make existing capabilities much more dependable.

## Best Figure

![Figure 4 — Demonstration of PPO and our GRPO (page 13)](figures/shao-2024-deepseekmath-grpo-fig.png)

**Image Candidates:**
- Figure 4 (p. 13): The signature figure of the paper — side-by-side architecture diagrams of PPO (with its Value Model in yellow) vs GRPO (with its group computation block instead), making instantly visible *what GRPO removed*.
- Figure 1 (p. 1): Top-1 accuracy of open-source models on MATH — the headline result chart, but it's a banner more than an analysis.
- Table 5 (p. 12): A dense comparison table showing DeepSeekMath-RL 7B beating Llama-70B-class open models and matching most closed models — the most quantitative comparison view but less visually striking.

**Best Image — Figure 4: "Demonstration of PPO and our GRPO"**

The figure is a two-panel architectural diagram on page 13. The top panel shows PPO: a Policy Model (trained, yellow) produces output o from question q, then a Reference Model, Reward Model and Value Model (the latter trained, yellow) all consume o; the Reward Model's score is KL-summed with the Reference Model's, then fed through GAE alongside the Value Model's output v to produce an advantage A. The bottom panel shows GRPO: the same Policy Model now produces G outputs o_1...o_G; each goes through the Reference Model (for KL) and the Reward Model (frozen, blue) to produce rewards r_1...r_G; a "Group Computation" block then turns those rewards into per-output advantages A_1...A_G with no value model in sight. The legend makes the punchline explicit: PPO has *two* yellow (trainable) blocks, GRPO has only *one*. This is the entire intuition of the paper in one image — the value network is the thing you can delete, and group-relative sampling is what replaces it.

## What Experts Overlook

The detail most readers skim past is the choice to put the KL penalty *in the loss* rather than *in the reward*. Standard PPO-RLHF (following Ouyang et al. 2022) adds `−β log(π_θ / π_ref)` to the per-token reward, which means the KL signal flows through the advantage calculation alongside the actual reward. GRPO instead drops the KL out of the reward entirely, normalizes the group-relative reward cleanly, and adds the KL divergence as a separate term in the loss using Schulman's unbiased estimator (which is also guaranteed positive — small but non-trivial). This shows up in Equation 3 of the paper, almost as a footnote.

**Why it matters:** Mixing KL into the reward creates a coupling between "how good is this answer" and "how far is this policy from the reference," which the advantage estimator then has to disentangle. By separating them, GRPO makes the advantage purely about reward quality (group-relative) and KL purely about regularization (additive in loss). It's a small algebraic move that has two practical consequences: (1) the group-relative advantages are cleaner and more stable, especially when reward magnitudes are highly variable across questions, and (2) you can tune the KL coefficient β without worrying about how it interacts with reward normalization. This is exactly the kind of "obvious in hindsight" change that turns a finicky algorithm (PPO) into a robust one (GRPO).

**Example of good use:** A team fine-tuning a code-generation LLM with RL notices that training is unstable — reward goes up but then collapses around step 5,000 as the policy drifts too far from the SFT model. Instead of cranking up the in-reward KL penalty (which would dampen learning signal), they refactor to the GRPO-style setup: group sampling, group-normalized advantage, KL added directly to loss. Training stabilizes because the KL no longer fights the reward gradient inside the advantage calculation, and they can crank β independently.

**Example of misapplication:** A team copies GRPO's pseudocode but keeps PPO's habit of subtracting log(π_θ / π_ref) from the per-token reward "for safety." Now they have KL pressure entering through *two* paths — once in the reward (which goes into the advantage normalization) and once in the loss. The two signals interfere; the advantage normalization warps in non-obvious ways; training looks stable on a toy benchmark but produces oddly conservative outputs in deployment. Worst case, they conclude GRPO "doesn't work" and revert to PPO — when the actual problem was double-counting the KL.

## Extracted Prompts

No applicable prompts found in this paper.

(The paper trains DeepSeekMath using few-shot CoT and program-of-thought prompting on standard benchmarks (GSM8K, MATH, MMLU, etc.) and references the prompting techniques from prior work — Wei et al. 2022 for CoT, Chen et al. 2022 for PoT, Gou et al. 2023 for tool-integrated reasoning — but it does not publish full prompt templates. The model itself is the artifact; the prompts are external benchmark prompts.)

## Citations

(56 references extracted into frontmatter `citations:` — first 10 shown below as bullets.)

- **Anil et al. 2023** — *Gemini: A family of highly capable multimodal models* — arXiv:2312.11805
- **Austin et al. 2021** — *Program synthesis with large language models* — arXiv:2108.07732
- **Azerbayev et al. 2023** — *Llemma: An open language model for mathematics* — arXiv:2310.10631
- **Bai et al. 2023** — *Qwen technical report* — arXiv:2309.16609
- **Burns et al. 2023** — *Weak-to-strong generalization* — arXiv:2312.09390
- **Chen et al. 2021** — *Evaluating large language models trained on code* — arXiv:2107.03374
- **Chen et al. 2022** — *Program of thoughts prompting* — arXiv:2211.12588
- **Cobbe et al. 2021** — *Training verifiers to solve math word problems (GSM8K)* — arXiv:2110.14168
- **DeepSeek-AI 2024** — *DeepSeek LLM: scaling open-source language models with longtermism* — arXiv:2401.02954
- **Gou et al. 2023** — *ToRA: A tool-integrated reasoning agent for mathematical problem solving* — arXiv:2309.17452

Remaining 46 citations in frontmatter.

## Related Digests

- [[yan-2025-memory-r1]] — Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning (directly uses GRPO as the training algorithm for memory policies)
- [[agrawal-2025-gepa-reflective-prompt-evolution]] — GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning (positions itself as a non-RL alternative to GRPO for the same kinds of tasks)
- [[deepseek-ai-2025-deepseek-r1-rl-reasoning]] — DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (the follow-up paper from the same lab that scales GRPO to general reasoning)
- [[touvron-2023-llama-2]] — Llama 2: Open Foundation and Fine-Tuned Chat Models (canonical RLHF/PPO recipe that GRPO is implicitly contrasted against)
- [[vassilyev-2026-rcl]] — Reflective Context Learning (later work building on GEPA/RL distinction explored in DeepSeekMath's unified paradigm)

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim in this digest (51.7% MATH, 88.2% GSM8K, 60.9% self-consistency-over-64 on MATH, Minerva 540B comparison, 120B-token corpus, 7×/9× corpus size ratios, G=64 outputs, learning rate 1e-6, KL coefficient β=0.04, batch size 1024, MMLU 49.1→54.9% from code training, BBH 55.2→59.5%, GSM8K 23.8% vs Proof-Pile-2 14.3% at 1.3B-scale, GRPO+PS > GRPO+OS, Maj@K up but Pass@K flat) is directly traceable to the paper's text, Tables 1-7, Figures 5-7, and Section 4.2's training-config paragraph. The architectural description of GRPO vs PPO matches Equation 3 and Algorithm 1. The KL-in-loss vs KL-in-reward distinction matches the discussion immediately after Equation 3 and Equation 4 (Schulman 2020 unbiased estimator). The "RL sharpens, doesn't extend" claim matches Figure 7 and Section 5.2.2 verbatim. The arXiv-ineffective finding matches Tables 8 and 9. The code-before-math finding matches Tables 6 and 7. No fabricated numbers, no overgeneralized claims beyond what the paper explicitly shows.
