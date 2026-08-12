---
corpus: agentic-memory
kind: paper-digest
slug: wang-2023-trace-benchmark
title: "TRACE: A Comprehensive Benchmark for Continual Learning in Large Language Models"
authors:
  - "Wang, Xiao"
  - "Zhang, Yuansen"
  - "Chen, Tianze"
  - "Gao, Songyang"
  - "Jin, Senjie"
  - "Yang, Xianjun"
  - "Xi, Zhiheng"
  - "Zheng, Rui"
  - "Zou, Yicheng"
  - "Gui, Tao"
  - "Zhang, Qi"
  - "Huang, Xuanjing"
year: 2023
publication_date: "2023-10"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2310.06762"
doi: null
arxiv_id: "2310.06762"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Continual fine-tuning of aligned LLMs causes severe collateral damage to general capabilities — most dramatically math and reasoning — but training data that contains explicit reasoning paths (rather than just final answers) substantially mitigates this forgetting while also accelerating new-task convergence."
topics:
  - continual-learning
  - llm-evaluation
  - catastrophic-forgetting
  - benchmark
  - reasoning-augmentation
  - instruction-tuning
  - chain-of-thought
tags:
  - paper
  - benchmark
  - llm-finetuning
  - catastrophic-forgetting
  - reasoning
  - llama2
  - vicuna
entities:
  - wang-xiao
  - gui-tao
  - zhang-qi
  - fudan-university
related_digests:
  - ai-2026-memorybench-continual-learning
  - howard-2018-ulmfit
  - yang-2024-rwla-lifelong-robot
  - xu-2026-agentic-memo
citations:
  - title: "Language Models are Few-Shot Learners (GPT-3)"
    authors: ["Brown, Tom B.", "Mann, Benjamin", "Ryder, Nick", "et al."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2005.14165"
    arxiv_id: "2005.14165"
  - title: "Llama 2: Open Foundation and Fine-Tuned Chat Models (Touvron et al.)"
    authors: ["Touvron, Hugo", "Lavril, Thibaut", "Izacard, Gautier", "et al."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2302.13971"
    arxiv_id: "2302.13971"
  - title: "LoRA: Low-Rank Adaptation of Large Language Models"
    authors: ["Hu, Edward J.", "Shen, Yelong", "Wallis, Phillip", "et al."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2106.09685"
    arxiv_id: "2106.09685"
  - title: "Overcoming Catastrophic Forgetting in Neural Networks (EWC)"
    authors: ["Kirkpatrick, James", "Pascanu, Razvan", "Rabinowitz, Neil", "et al."]
    year: 2017
    doi: null
    url: null
    arxiv_id: null
  - title: "Gradient Episodic Memory for Continual Learning"
    authors: ["Lopez-Paz, David", "Ranzato, Marc'Aurelio"]
    year: 2017
    doi: null
    url: null
    arxiv_id: null
  - title: "Experience Replay for Continual Learning"
    authors: ["Rolnick, David", "Ahuja, Arun", "Schwarz, Jonathan", "et al."]
    year: 2019
    doi: null
    url: null
    arxiv_id: null
  - title: "Orthogonal Gradient Descent for Continual Learning"
    authors: ["Farajtabar, Mehrdad", "Azizan, Navid", "Mott, Alex", "Li, Ang"]
    year: 2020
    doi: null
    url: null
    arxiv_id: null
  - title: "Progressive Prompts: Continual Learning for Language Models"
    authors: ["Razdaibiedina, Anastasia", "Mao, Yuning", "Hou, Rui", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Fine-tuned Language Models are Continual Learners"
    authors: ["Scialom, Thomas", "Chakrabarty, Tuhin", "Muresan, Smaranda"]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "An Empirical Study of Catastrophic Forgetting in LLMs During Continual Fine-tuning"
    authors: ["Luo, Yun", "Yang, Zhen", "Meng, Fandong", "et al."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2308.08747"
    arxiv_id: "2308.08747"
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    authors: ["Wei, Jason", "Wang, Xuezhi", "Schuurmans, Dale", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "Large Language Models are Zero-Shot Reasoners"
    authors: ["Kojima, Takeshi", "Gu, Shixiang Shane", "Reid, Machel", "Matsuo, Yutaka", "Iwasawa, Yusuke"]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    authors: ["Zhou, Denny", "Schärli, Nathanael", "Hou, Le", "et al."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2205.10625"
    arxiv_id: "2205.10625"
  - title: "LIMA: Less Is More for Alignment"
    authors: ["Zhou, Chunting", "Liu, Pengfei", "Xu, Puxin", "et al."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.11206"
    arxiv_id: "2305.11206"
  - title: "Measuring Massive Multitask Language Understanding (MMLU)"
    authors: ["Hendrycks, Dan", "Burns, Collin", "Basart, Steven", "et al."]
    year: 2020
    doi: null
    url: null
    arxiv_id: null
  - title: "Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them (BBH)"
    authors: ["Suzgun, Mirac", "Scales, Nathan", "Schärli, Nathanael", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2210.09261"
  - title: "TyDiQA: Information-Seeking QA in Typologically Diverse Languages"
    authors: ["Clark, Jonathan H.", "Choi, Eunsol", "Collins, Michael", "et al."]
    year: 2020
    doi: null
    url: null
    arxiv_id: null
  - title: "PIQA: Reasoning about Physical Commonsense in Natural Language"
    authors: ["Bisk, Yonatan", "Zellers, Rowan", "Gao, Jianfeng", "Choi, Yejin"]
    year: 2020
    doi: null
    url: null
    arxiv_id: null
  - title: "BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions"
    authors: ["Clark, Christopher", "Lee, Kenton", "Chang, Ming-Wei", "et al."]
    year: 2019
    doi: null
    url: null
    arxiv_id: "1905.10044"
  - title: "ScienceQA: Learn to Explain — Multimodal Reasoning via Thought Chains for Science QA"
    authors: ["Lu, Pan", "Mishra, Swaroop", "Xia, Tony", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "NumGLUE: A Suite of Fundamental yet Challenging Mathematical Reasoning Tasks"
    authors: ["Mishra, Swaroop", "Mitra, Arindam", "Varshney, Neeraj", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "MeetingBank: A Benchmark Dataset for Meeting Summarization"
    authors: ["Hu, Yebowen", "Ganter, Tim", "Deilamsalehy, Hanieh", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "C-STANCE: A Large Dataset for Chinese Zero-Shot Stance Detection"
    authors: ["Zhao, Chenye", "Li, Yingjie", "Caragea, Cornelia"]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "20Minuten: Document-Level Text Simplification in German"
    authors: ["Rios, Annette", "Spring, Nicolas", "Kew, Tannon", "et al."]
    year: 2021
    doi: null
    url: null
    arxiv_id: null
  - title: "CodeXGLUE: A Machine Learning Benchmark for Code Understanding and Generation"
    authors: ["Lu, Shuai", "Guo, Daya", "Ren, Shuo", "et al."]
    year: 2021
    doi: null
    url: null
    arxiv_id: null
  - title: "Trillion Dollar Words: A New Financial Dataset, Task & Market Analysis (FOMC)"
    authors: ["Shah, Agam", "Paturi, Suvan", "Chava, Sudheer"]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Self-Instruct: Aligning Language Model with Self-Generated Instructions"
    authors: ["Wang, Yizhong", "Kordi, Yeganeh", "Mishra, Swaroop", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2212.10560"
  - title: "Safety-Tuned LLaMAs (CoNa dataset)"
    authors: ["Bianchi, Federico", "Suzgun, Mirac", "Attanasio, Giuseppe", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: "2309.07875"
  - title: "Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90% ChatGPT Quality"
    authors: ["Chiang, Wei-Lin", "Li, Zhuohan", "Lin, Zi", "et al."]
    year: 2023
    doi: null
    url: "https://lmsys.org/blog/2023-03-30-vicuna/"
    arxiv_id: null
  - title: "Baichuan 2: Open Large-Scale Language Models"
    authors: ["Baichuan"]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2309.10305"
    arxiv_id: "2309.10305"
  - title: "Scaling Instruction-Finetuned Language Models (FLAN)"
    authors: ["Chung, Hyung Won", "Hou, Le", "Longpre, Shayne", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2210.11416"
  - title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
    authors: ["Zheng, Lianmin", "Chiang, Wei-Lin", "Sheng, Ying", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: "2306.05685"
  - title: "Orthogonal Subspace Learning for Language Model Continual Learning (O-LoRA)"
    authors: ["Wang, Xiao", "Chen, Tianze"]
    year: 2023
    doi: null
    url: null
    arxiv_id: "2310.06174"
  - title: "Riemannian Walk for Incremental Learning"
    authors: ["Chaudhry, Arslan", "Dokania, Puneet K.", "Ajanthan, Thalaiyasingam", "Torr, Philip H.S."]
    year: 2018
    doi: null
    url: null
    arxiv_id: null
  - title: "A Comprehensive Survey of Continual Learning: Theory, Method and Application"
    authors: ["Wang, Liyuan", "Zhang, Xingxing", "Su, Hang", "Zhu, Jun"]
    year: 2023
    doi: null
    url: null
    arxiv_id: "2302.00487"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Overview of TRACE benchmark — eight sequential tasks plus four post-training evaluation deltas"
  page: 2
  image_path: "figures/wang-2023-trace-benchmark-fig.png"
---

# TRACE: A Comprehensive Benchmark for Continual Learning in Large Language Models

**Authors:** Xiao Wang, Yuansen Zhang, Tianze Chen, Songyang Gao, Senjie Jin, Xianjun Yang, Zhiheng Xi, Rui Zheng, Yicheng Zou, Tao Gui, Qi Zhang, Xuanjing Huang (Fudan University, UC Santa Barbara, Shanghai AI Laboratory)
**Published:** 2023-10 · [Source](https://arxiv.org/abs/2310.06762)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

The authors argue that existing continual-learning (CL) benchmarks for NLP are too easy and too contaminated to challenge modern aligned LLMs. They introduce **TRACE**, a benchmark of 8 sequential tasks (ScienceQA, FOMC, MeetingBank, C-STANCE, 20Minuten, Py150, NumGLUE-cm, NumGLUE-ds) spanning domain-specific knowledge, multilinguality, code completion, and math reasoning — each balanced to 5,000 train / 2,000 test examples in a unified format. Critically, they add three new evaluation axes beyond the traditional Overall-Performance (OP) and Backward-Transfer (BWT) scores: **General Ability Delta** (∆R^G on MMLU/BBH/TydiQA/PIQA/BoolQ/GSM), **Instruction Following Delta** (GPT-4 win-rate on Self-Instruct + LIMA), and **Safety Delta** (GPT-4 win-rate on CoNa). Evaluating five aligned models (LLaMA-2-7B/13B-Chat, Vicuna-7B/13B-V1.5, Baichuan2-7B-Instruct) across four CL methods (SeqFT, LoRASeqFT, Replay, ICL), they find sequential fine-tuning catastrophically collapses general reasoning — most strikingly, **LLaMA-2-13B-Chat's GSM8K accuracy drops from 43.14% to 2.12% after SeqFT** — while multilingual capability sometimes *improves* (TydiQA goes from 23.47 to 33.23 F1). Replay mitigates forgetting on target tasks but still hurts general ability. LoRA preserves the backbone but adapts worst on target tasks and most hurts instruction-following. Building on the observation that ScienceQA (which contains explicit reasoning paths in its answers) *increased* BBH after training, they propose **Reasoning-augmented Continual Learning (RCL)**: have GPT-4 annotate reasoning paths for each training example, then fine-tune on the augmented data. RCL with just 500 samples matches SeqFT trained on 5,000 samples on target performance, outperforms SeqFT on GSM (+12.7 pts) and BBH, and improves instruction-following by 8% over SeqFT.

## Key Takeaway

**Continual fine-tuning of aligned LLMs causes severe collateral damage to general capabilities — most dramatically math and reasoning — but training data that contains explicit reasoning paths (rather than just final answers) substantially mitigates this forgetting while also accelerating new-task convergence.** The single most striking concrete result: a sequential fine-tune on TRACE's 8 tasks drops LLaMA-2-Chat-13B's gsm8k accuracy from 28.8% to 2% (a 93% relative collapse). The single most actionable insight: when constructing CL training data, prefer datasets whose answers include the reasoning trace (or generate the trace with a stronger model), because this style of supervision both teaches the new task faster (500 vs 5,000 samples for parity) and inoculates the model against forgetting its prior reasoning skills. The authors frame this through LIMA's "Superficial Alignment Hypothesis" — the model already has the underlying skills; CL should be about *aligning* those latent capabilities to the new task surface, not retraining them from scratch.

## Implications

- **Catastrophic forgetting is not symmetric across capability types.** Math and chain-of-thought reasoning are the most fragile (collapsing to near-zero); multilingual QA is the most robust and sometimes *improves*; commonsense (PIQA) is largely untouched. Anyone fine-tuning an aligned model should test reasoning-heavy benchmarks specifically, not assume MMLU or PIQA stability implies safety.
- **Parameter-efficient fine-tuning (LoRA) is not a free lunch for CL.** LoRA preserves backbone weights but in TRACE actually fits target tasks *worse* (LLaMA-2-7B SeqFT OP=48.7, LoRASeqFT OP=12.7) AND degrades instruction-following the most (LoRA win-rate vs base is 3%/4%/94% Win/Tie/Loss — almost total collapse on helpfulness). The community intuition that "LoRA = safe fine-tuning" needs a sharper qualifier: *the backbone is safe, but the model behavior is not*.
- **Replay with alignment data (LIMA) reliably preserves target performance** (Replay BWT is positive across all 5 models) but still loses general ability — so replay alone is not sufficient if you care about the model retaining its broad capabilities.
- **Safety alignment is sticky.** Across LLaMA-2-7B/13B, the three CL methods all produced ~86–98% Tie or Win in safety evaluations — sequential fine-tuning on benign tasks does *not* meaningfully unsafe-ify an aligned model on the CoNa benchmark. This narrows the "alignment tax" concern in CL to capability preservation, not safety preservation.
- **Reasoning-augmented data is a sample-efficient training strategy independent of CL.** RCL+500 ≈ SeqFT+5,000 on overall task performance. If the finding generalizes, anyone fine-tuning an LLM on a new domain might benefit from generating CoT rationales (via GPT-4 or a stronger teacher) before training, regardless of whether they care about CL.
- **The Superficial Alignment Hypothesis gets indirect empirical support.** RCL works because it activates rather than overwrites — it tells the model "use your existing reasoning skills to solve this", which is exactly what LIMA's hypothesis would predict should be easier than re-teaching the skill.

## How to Apply It (method)

The paper offers two distinct artifacts to apply: (1) the benchmark itself, (2) the RCL training recipe.

**Using TRACE as a benchmark:**
1. Pull the dataset from `https://github.com/BeyonderXX/TRACE` — 8 tasks already balanced to 5k train / 2k test in unified format.
2. Train your aligned model sequentially through the 8 tasks in TRACE's order (C-STANCE → FOMC → MeetingBank → Py150 → ScienceQA → NumGLUE-cm → NumGLUE-ds → 20Minuten, based on Tables 7–11 ordering). The paper used learning rate 1e-5, batch size 128, weight decay 0, no LoRA; for the 8 tasks they used 1/1/5/5/1/5/5/5 epochs respectively. All experiments on 8×80G A100 with DeepSpeed.
3. After the full sequence, report:
   - **OP and BWT** (eqs. 2 and 3) — traditional CL metrics on the 8 target tasks
   - **General Ability Delta** — average score change on MMLU (5-shot acc), GSM (8-shot CoT EM), BBH (3-shot CoT EM), TydiQA (1-shot gold-passage F1), BoolQ (0-shot acc), PIQA (0-shot acc), evaluated via OpenCompass
   - **Instruction Following Delta** — GPT-4 pairwise win-rate of post-CL model vs base model on Self-Instruct (175 prompts) and LIMA (300 prompts)
   - **Safety Delta** — GPT-4 pairwise win-rate on CoNa (178 hate-speech-adjacent prompts)

**Applying RCL to your own continual fine-tuning:**
1. For each training example in your new task, manually annotate 3 reasoning-path demonstrations as a few-shot prompt for GPT-4.
2. Use GPT-4 (or a comparable strong model) with those demonstrations in context to generate a reasoning path for every example in the training set. The paper reports 94% approval rate on a 100-sample human spot-check, so quality is high but not perfect — budget for some filtering.
3. Verify the GPT-4-generated reasoning against the ground-truth label; keep examples where the final answer matches.
4. Reformat the training data so the target is `Reasoning: <chain> Answer: <label>` rather than just `<label>`. Prompt the model with "Give your reasoning first, and then the answer."
5. Fine-tune sequentially as before, but on the reasoning-augmented dataset. The paper found 500 samples per task is sufficient — a 10× reduction over raw SeqFT.
6. Optionally combine with Replay (RCL+Replay in Figure 6) for further gains on reasoning tasks (GSM and BBH).

**What this *won't* fix:** RCL still loses some general ability vs the base model — it's a mitigation, not a cure. It also relies on having a teacher model strong enough to produce reliable reasoning paths, which may not hold in low-resource domains.

## Best Figure

![Figure 1 — Overview of TRACE benchmark (page 2)](figures/wang-2023-trace-benchmark-fig.png)

**Figure Page: 2**

This is the architectural overview of TRACE. The left side shows the four task families (Domain-specific, Multi-lingual, Mathematical reasoning, Code completion) feeding sequentially into the LLM (the llama icon is a literal pun on Llama-2). The right side is the evaluation diamond, which is the paper's real contribution: post-training, the model is scored on four orthogonal axes — *Performance of sequential tasks* (the traditional CL metric), *General Ability Delta* (does it still know things), *Instruction Following Delta* (does it still follow user instructions), and *Safety Delta* (is it still safe). The visual placement of "sequential task performance" as just one of four equally-weighted axes is the entire argument of the paper in a single image: prior CL work only measured the top vertex, and missed that the other three vertices can collapse without anyone noticing. Pairing this with the paper's most-quoted number — LLaMA-2-13B-Chat's GSM8K dropping from 43.14% to 2.12% — gives you the headline takeaway visually. This figure is what you'd put on a slide.

## What Experts Overlook

A practitioner reading only the abstract might miss several non-obvious findings tucked into the body:

1. **Multilingual capability frequently *improves* under continual fine-tuning.** TydiQA F1 went up for almost every (model, method) combination in Table 2 — sometimes by 10+ points. Most discourse on catastrophic forgetting assumes uniform degradation; this paper provides a counterexample driven by the presence of Chinese (C-STANCE) and German (20Minuten) data in the sequence, with apparent cross-lingual transfer to other languages in TydiQA.

2. **Safety is much more robust than people fear.** Across the three CL methods on LLaMA-2-13B, GPT-4 safety win/tie rates were 86–98% — i.e., the post-CL model is judged at least as safe as the base in the vast majority of pairwise comparisons. The "alignment tax" intuition that CL must erode safety alignment is *not supported* by this paper's CoNa evaluation. (Caveat: CoNa is one safety dataset; this doesn't prove safety across all threat models.)

3. **LoRA's reputation as the "safe" fine-tuning method is misleading on two axes.** It (a) adapts worst on target tasks (OP roughly half that of SeqFT in some configurations), and (b) loses instruction-following most aggressively (LoRA-Win vs SeqFT-Win: 3% vs 14%; LoRA-Loss: 94% vs 53%). The paper explicitly says "be cautious when exploring approaches like LoRA for continual learning in LLMs", which contradicts the common framing of LoRA as the conservative default for fine-tuning aligned models.

4. **The dataset ORDER probably matters but isn't ablated.** Tables 7–11 reveal that some tasks (notably FOMC) crater to near-zero on certain rounds (LLaMA-2-7B FOMC drops from 0.735 → 0.0 between rounds 4 and 5) and then partially recover. The paper doesn't run permutation experiments on task ordering, so it's unclear whether TRACE's specific sequence is representative or pathological.

5. **The RCL "94% approval rate" on GPT-4-generated reasoning is the weakest evidentiary link.** It's a single human spot-check on 100 samples — no inter-annotator agreement reported, no breakdown by task, no analysis of *which* 6% failed. If you're planning to apply RCL in production, this is the number you should re-measure on your own data.

6. **ICL is a surprisingly strong baseline on overall performance** (Table 1: ICL OP often within 5-10 points of SeqFT, e.g., LLaMA-2-13B ICL=41.9 vs SeqFT=49.9) and obviously preserves general ability perfectly because it doesn't update weights. For practitioners with modest task adaptation needs, ICL may dominate any of the fine-tuning methods on the full set of TRACE metrics.

7. **The benchmark itself may already be partially contaminated by 2026.** TRACE was released October 2023; ScienceQA, NumGLUE, PIQA, MMLU, BBH, TydiQA, BoolQ, and Self-Instruct are all in the public training corpora of major frontier models released after TRACE. Anyone using TRACE today should treat the General Ability Delta numbers with caution — base model scores may now reflect memorization, not capability.

## Extracted Prompts

The paper does not include verbatim prompts in the main text, but two are reconstructible from method descriptions and Figure 5:

**RCL training-time prompt** (Figure 5, reasoning-based CL example, reformatted):
```
Instruction:
Solve the following math problem.
Give your reasoning first, and then the answer.

Question:
A football team practices for 6 hours daily. This week they could not practice
due to rain on 1 days. Find the total number of hours they practiced this week.

Reasoning:
[model generates chain-of-thought]
Answer:
[model generates final answer, e.g., 36]
```

**RCL data-generation prompt for GPT-4 annotation** (paraphrased from §5):
```
[3 human-annotated demonstrations of (question, reasoning, answer) for THIS task]

Now solve this question and give your reasoning first, then the answer.
Question: <new question>
Answer: <ground-truth final label>  [used for verification, not shown to GPT-4]
```

The paper does NOT share the exact GPT-4 evaluation prompts used for Instruction-Following and Safety pairwise judgments — these are referenced as "Appendix .7" but the specific prompt template is not in the main body of the version on arXiv.

## Citations

The paper draws on ~50 cited works. The most important threads, condensed (full structured list in the frontmatter):

- **Continual learning foundations:** Kirkpatrick et al. 2017 (EWC), Lopez-Paz & Ranzato 2017 (GEM), Rolnick et al. 2019 (Experience Replay), Farajtabar et al. 2020 (OGD), Razdaibiedina et al. 2023 (Progressive Prompts), Wang et al. 2023a (CL survey).
- **CL benchmarks for NLP (the ones TRACE is replacing):** Zhang et al. 2015 (5 text-classification datasets), Razdaibiedina et al. 2023 (long-CL benchmark), Scialom et al. 2022 (English NLG CL).
- **Empirical CL on LLMs:** Luo et al. 2023 (forgetting in Bloomz), Liu & Huang 2023 (LoRA prompt-learning for forgetting), Wang & Chen 2023 (O-LoRA).
- **Aligned LLMs evaluated:** Touvron et al. 2023 (Llama 2), Chiang et al. 2023 (Vicuna), Baichuan 2023.
- **Chain-of-thought / reasoning prior art (the basis for RCL):** Wei et al. 2022 (CoT prompting), Kojima et al. 2022 (zero-shot CoT), Zhou et al. 2022 (least-to-most), Ho et al. 2022 (Fine-tune-CoT), Lu et al. 2022 (ScienceQA).
- **Alignment philosophy:** Zhou et al. 2023 (LIMA + Superficial Alignment Hypothesis), Wang et al. 2022 (Self-Instruct).
- **General-ability evaluation suite components:** Hendrycks et al. 2020 (MMLU), Suzgun et al. 2022 (BBH), Clark et al. 2020 (TydiQA), Bisk et al. 2020 (PIQA), Clark et al. 2019 (BoolQ).
- **TRACE's eight constituent datasets:** Lu et al. 2022 (ScienceQA), Shah et al. 2023 (FOMC), Hu et al. 2023 (MeetingBank), Zhao et al. 2023 (C-STANCE), Rios et al. 2021 (20Minuten), Lu et al. 2021 (CodeXGLUE/Py150), Mishra et al. 2022 (NumGLUE).
- **GPT-4 as judge:** OpenAI 2023 (GPT-4 tech report), Zheng et al. 2023 (LLM-as-a-judge).

## Related Digests

- [[ai-2026-memorybench-continual-learning]] — MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems (the natural successor benchmark, focused on memory-augmented agentic systems rather than weight fine-tuning)
- [[howard-2018-ulmfit]] — Universal Language Model Fine-tuning for Text Classification (the pre-LLM ancestor of "fine-tune a general LM into a domain"; ULMFiT's discriminative LR + slanted-triangular LR + gradual unfreezing are the original mitigations for the exact forgetting TRACE measures)
- [[yang-2024-rwla-lifelong-robot]] — Task-agnostic Lifelong Robot Learning with Retrieval-based Weighted Local Adaptation (parallel lifelong-learning framing in robotics; retrieval-based mitigation rather than reasoning-augmented training)
- [[xu-2026-agentic-memo]] — Contextual Agentic Memory is a Memo, Not True Memory (cites SSR / self-synthesized rehearsal, a 2024 follow-up to TRACE's data-augmentation strategy)

## Reviewer Notes

**Hallucination severity: Clean.**

Spot-checked claims against the paper text:
- LLaMA-2-13B-Chat GSM8K 28.8% → 2% claim: confirmed in abstract ("the accuracy of llama2-chat 13B on gsm8k dataset declined precipitously from 28.8% to 2%"). Table 2 shows 43.14 → 2.12 for the SeqFT row using a different shot count (8-shot CoT); both numbers are accurate, the 28.8 → 2 is the abstract's headline; the 43.14 → 2.12 is Table 2 specifics. The digest cites both with their correct context.
- Number of datasets: 8 (confirmed in abstract and §4.1).
- Five models evaluated: LLaMA-2-7B-Chat, LLaMA-2-13B-Chat, Vicuna-7B-V1.5, Vicuna-13B-V1.5, Baichuan2-7B-Instruct (confirmed §4.3.1).
- Three new deltas: General Ability Delta, Instruction Following Delta, Safety Delta (confirmed §4.2 and Figure 1).
- RCL 500 vs SeqFT 5000 parity: confirmed in §5.1 and Table 3 ("achieves comparable results to the SeqFT method trained on 5000 samples").
- RCL +12.7 GSM gain over SeqFT, +8% instruction-following over SeqFT: confirmed in §5.2 and §5.3.
- TydiQA improvement (LLaMA-2-7B-Chat 23.47 → 33.23): confirmed in Table 2.
- LoRA win/tie/loss rates (Replay 10/18/72, LoRA 3/4/94, SeqFT 14/34/53 for helpful; 88/12 Replay, 86/14 LoRA, 98/2 SeqFT for safety): confirmed in Figure 2.
- 94% approval rate on 100-sample reasoning spot-check: confirmed in §5.
- Hardware: 8×80G A100, DeepSpeed: confirmed in Appendix .1.
- Hyperparameters (lr 1e-5 / 1e-4 LoRA, batch size 128, weight decay 0, temp 0.1): confirmed in Appendix .1.
- Task epoch counts (1/1/5/5/1/5/5/5 for non-LoRA): confirmed in Appendix .1.
- The 6-shot ICL setting: confirmed in §4.3.1.
- Replay uses 10% of LIMA data: confirmed in §4.3.1.

No fabricated numbers detected. The digest correctly distinguishes between abstract claims and table-specific values where these differ slightly due to evaluation configuration. The Superficial Alignment Hypothesis attribution to LIMA (Zhou et al. 2023) is correctly framed in §6.
