---
corpus: agentic-memory
kind: paper-digest
slug: touvron-2023-llama-foundation-models
title: "LLaMA: Open and Efficient Foundation Language Models"
authors:
  - "Touvron, Hugo"
  - "Lavril, Thibaut"
  - "Izacard, Gautier"
  - "Martinet, Xavier"
  - "Lachaux, Marie-Anne"
  - "Lacroix, Timothee"
  - "Rozière, Baptiste"
  - "Goyal, Naman"
  - "Hambro, Eric"
  - "Azhar, Faisal"
  - "Rodriguez, Aurelien"
  - "Joulin, Armand"
  - "Grave, Edouard"
  - "Lample, Guillaume"
year: 2023
publication_date: "2023-02"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2302.13971"
doi: null
arxiv_id: "2302.13971"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Trained exclusively on publicly available data, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks while being 10× smaller, and LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B — by training smaller models on far more tokens than the Chinchilla compute-optimal scaling laws prescribe, optimising for inference cost rather than training cost."
topics:
  - foundation-models
  - open-source-llms
  - scaling-laws
  - inference-efficiency
  - transformer-architecture
  - pretraining-data
tags:
  - paper
  - llama
  - meta-ai
  - language-models
  - open-weights
  - benchmark
entities:
  - touvron-hugo
  - lample-guillaume
  - grave-edouard
  - meta-ai
related_digests:
  - brown-2020-gpt3-few-shot
  - radford-2019-gpt2-multitask
  - vaswani-2017-attention-is-all-you-need
  - borgeaud-2021-retro
citations:
  - title: "Language models are few-shot learners"
    authors: ["Brown, T. B.", "et al."]
    year: 2020
    arxiv_id: "2005.14165"
    url: "https://arxiv.org/abs/2005.14165"
  - title: "Training compute-optimal large language models"
    authors: ["Hoffmann, J.", "et al."]
    year: 2022
    arxiv_id: "2203.15556"
    url: "https://arxiv.org/abs/2203.15556"
  - title: "PaLM: Scaling language modeling with pathways"
    authors: ["Chowdhery, A.", "et al."]
    year: 2022
    arxiv_id: "2204.02311"
    url: "https://arxiv.org/abs/2204.02311"
  - title: "Scaling language models: Methods, analysis & insights from training Gopher"
    authors: ["Rae, J. W.", "et al."]
    year: 2021
    arxiv_id: "2112.11446"
    url: "https://arxiv.org/abs/2112.11446"
  - title: "OPT: Open pre-trained transformer language models"
    authors: ["Zhang, S.", "et al."]
    year: 2022
    arxiv_id: "2205.01068"
    url: "https://arxiv.org/abs/2205.01068"
  - title: "Scaling laws for neural language models"
    authors: ["Kaplan, J.", "et al."]
    year: 2020
    arxiv_id: "2001.08361"
    url: "https://arxiv.org/abs/2001.08361"
  - title: "Attention is all you need"
    authors: ["Vaswani, A.", "et al."]
    year: 2017
    arxiv_id: "1706.03762"
    url: "https://arxiv.org/abs/1706.03762"
  - title: "Root mean square layer normalization (RMSNorm)"
    authors: ["Zhang, B.", "Sennrich, R."]
    year: 2019
    arxiv_id: "1910.07467"
    url: "https://arxiv.org/abs/1910.07467"
  - title: "GLU variants improve transformer (SwiGLU)"
    authors: ["Shazeer, N."]
    year: 2020
    arxiv_id: "2002.05202"
    url: "https://arxiv.org/abs/2002.05202"
  - title: "RoFormer: Enhanced transformer with rotary position embedding"
    authors: ["Su, J.", "et al."]
    year: 2021
    arxiv_id: "2104.09864"
    url: "https://arxiv.org/abs/2104.09864"
  - title: "FlashAttention: Fast and memory-efficient exact attention with IO-awareness"
    authors: ["Dao, T.", "Fu, D. Y.", "Ermon, S.", "Rudra, A.", "Ré, C."]
    year: 2022
    arxiv_id: "2205.14135"
    url: "https://arxiv.org/abs/2205.14135"
  - title: "Reducing activation recomputation in large transformer models"
    authors: ["Korthikanti, V.", "et al."]
    year: 2022
    arxiv_id: "2205.05198"
    url: "https://arxiv.org/abs/2205.05198"
  - title: "Self-attention does not need O(n^2) memory"
    authors: ["Rabe, M. N.", "Staats, C."]
    year: 2021
    arxiv_id: "2112.05682"
    url: "https://arxiv.org/abs/2112.05682"
  - title: "BLOOM: A 176B-parameter open-access multilingual language model"
    authors: ["Scao, T. L.", "et al."]
    year: 2022
    arxiv_id: "2211.05100"
    url: "https://arxiv.org/abs/2211.05100"
  - title: "GPT-NeoX-20B: An open-source autoregressive language model"
    authors: ["Black, S.", "Biderman, S.", "et al."]
    year: 2022
    arxiv_id: "2204.06745"
    url: "https://arxiv.org/abs/2204.06745"
  - title: "GLM-130B: An open bilingual pre-trained model"
    authors: ["Zeng, A.", "et al."]
    year: 2022
    arxiv_id: "2210.02414"
    url: "https://arxiv.org/abs/2210.02414"
  - title: "CCNet: Extracting high quality monolingual datasets from web crawl data"
    authors: ["Wenzek, G.", "et al."]
    year: 2020
    url: null
  - title: "Exploring the limits of transfer learning with a unified text-to-text transformer (T5/C4)"
    authors: ["Raffel, C.", "et al."]
    year: 2020
    arxiv_id: "1910.10683"
    url: "https://arxiv.org/abs/1910.10683"
  - title: "The Pile: An 800GB dataset of diverse text for language modeling"
    authors: ["Gao, L.", "et al."]
    year: 2020
    arxiv_id: "2101.00027"
    url: "https://arxiv.org/abs/2101.00027"
  - title: "SentencePiece: A simple and language independent subword tokenizer"
    authors: ["Kudo, T.", "Richardson, J."]
    year: 2018
    arxiv_id: "1808.06226"
    url: "https://arxiv.org/abs/1808.06226"
  - title: "Neural machine translation of rare words with subword units (BPE)"
    authors: ["Sennrich, R.", "Haddow, B.", "Birch, A."]
    year: 2015
    arxiv_id: "1508.07909"
    url: "https://arxiv.org/abs/1508.07909"
  - title: "Decoupled weight decay regularization (AdamW)"
    authors: ["Loshchilov, I.", "Hutter, F."]
    year: 2017
    arxiv_id: "1711.05101"
    url: "https://arxiv.org/abs/1711.05101"
  - title: "Emergent abilities of large language models"
    authors: ["Wei, J.", "et al."]
    year: 2022
    arxiv_id: "2206.07682"
    url: "https://arxiv.org/abs/2206.07682"
  - title: "Scaling instruction-finetuned language models (Flan-PaLM)"
    authors: ["Chung, H. W.", "et al."]
    year: 2022
    arxiv_id: "2210.11416"
    url: "https://arxiv.org/abs/2210.11416"
  - title: "OPT-IML: Scaling language model instruction meta-learning"
    authors: ["Iyer, S.", "et al."]
    year: 2022
    arxiv_id: "2212.12017"
    url: "https://arxiv.org/abs/2212.12017"
  - title: "Training verifiers to solve math word problems (GSM8k)"
    authors: ["Cobbe, K.", "et al."]
    year: 2021
    arxiv_id: "2110.14168"
    url: "https://arxiv.org/abs/2110.14168"
  - title: "Measuring mathematical problem solving with the MATH dataset"
    authors: ["Hendrycks, D.", "et al."]
    year: 2021
    arxiv_id: "2103.03874"
    url: "https://arxiv.org/abs/2103.03874"
  - title: "Solving quantitative reasoning problems with language models (Minerva)"
    authors: ["Lewkowycz, A.", "et al."]
    year: 2022
    arxiv_id: "2206.14858"
    url: "https://arxiv.org/abs/2206.14858"
  - title: "Evaluating large language models trained on code (HumanEval)"
    authors: ["Chen, M.", "et al."]
    year: 2021
    arxiv_id: "2107.03374"
    url: "https://arxiv.org/abs/2107.03374"
  - title: "Program synthesis with large language models (MBPP)"
    authors: ["Austin, J.", "et al."]
    year: 2021
    arxiv_id: "2108.07732"
    url: "https://arxiv.org/abs/2108.07732"
  - title: "Measuring massive multitask language understanding (MMLU)"
    authors: ["Hendrycks, D.", "et al."]
    year: 2020
    arxiv_id: "2009.03300"
    url: "https://arxiv.org/abs/2009.03300"
  - title: "HellaSwag: Can a machine really finish your sentence?"
    authors: ["Zellers, R.", "et al."]
    year: 2019
    arxiv_id: "1905.07830"
    url: "https://arxiv.org/abs/1905.07830"
  - title: "WinoGrande: An adversarial Winograd schema challenge at scale"
    authors: ["Sakaguchi, K.", "et al."]
    year: 2021
    arxiv_id: "1907.10641"
    url: "https://arxiv.org/abs/1907.10641"
  - title: "BoolQ: Exploring the surprising difficulty of natural yes/no questions"
    authors: ["Clark, C.", "et al."]
    year: 2019
    arxiv_id: "1905.10044"
    url: "https://arxiv.org/abs/1905.10044"
  - title: "PIQA: Reasoning about physical commonsense in natural language"
    authors: ["Bisk, Y.", "et al."]
    year: 2020
    url: null
  - title: "Natural Questions: a benchmark for question answering research"
    authors: ["Kwiatkowski, T.", "et al."]
    year: 2019
    url: null
  - title: "TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension"
    authors: ["Joshi, M.", "et al."]
    year: 2017
    arxiv_id: "1705.03551"
    url: "https://arxiv.org/abs/1705.03551"
  - title: "TruthfulQA: Measuring how models mimic human falsehoods"
    authors: ["Lin, S.", "Hilton, J.", "Evans, O."]
    year: 2021
    arxiv_id: "2109.07958"
    url: "https://arxiv.org/abs/2109.07958"
  - title: "RealToxicityPrompts: Evaluating neural toxic degeneration in language models"
    authors: ["Gehman, S.", "et al."]
    year: 2020
    arxiv_id: "2009.11462"
    url: "https://arxiv.org/abs/2009.11462"
  - title: "CrowS-Pairs: A challenge dataset for measuring social biases in masked language models"
    authors: ["Nangia, N.", "et al."]
    year: 2020
    url: null
  - title: "Gender bias in coreference resolution (WinoGender)"
    authors: ["Rudinger, R.", "et al."]
    year: 2018
    url: null
  - title: "RACE: Large-scale reading comprehension dataset from examinations"
    authors: ["Lai, G.", "et al."]
    year: 2017
    arxiv_id: "1704.04683"
    url: "https://arxiv.org/abs/1704.04683"
  - title: "Sustainable AI: Environmental implications, challenges and opportunities"
    authors: ["Wu, C.-J.", "et al."]
    year: 2022
    url: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Training loss over train tokens for the 7B, 13B, 33B, and 65B models"
  page: 3
  image_path: "figures/touvron-2023-llama-foundation-models-fig.png"
---

# LLaMA: Open and Efficient Foundation Language Models

**Authors:** Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample (Meta AI)
**Published:** 2023-02 · [Source](https://arxiv.org/abs/2302.13971)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Meta AI trains a family of foundation language models from 7B to 65B parameters using **only publicly available data** (CommonCrawl, C4, GitHub, Wikipedia, Books, ArXiv, StackExchange — ~1.4T tokens). They invert the Chinchilla scaling law's emphasis on training compute: instead of finding the compute-optimal (model, data) pair, they train *smaller* models on *vastly more* tokens than Chinchilla recommends, because the relevant budget at deployment scale is **inference cost**, not training cost. The headline result: LLaMA-13B beats GPT-3 (175B) on most benchmarks while being 10× smaller and runnable on a single GPU; LLaMA-65B is competitive with the much larger Chinchilla-70B and PaLM-540B. Architecture is a transformer with three Now-standard tweaks borrowed from PaLM/GPT-Neo: pre-normalisation with RMSNorm, SwiGLU activations, and rotary positional embeddings (RoPE). Training the 65B took ~21 days on 2048 A100-80GB GPUs (~1,022k GPU-hours, ~173 tCO₂eq). All weights released to the research community.

## Key Takeaway

Trained exclusively on publicly available data, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks while being 10× smaller, and LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B — by training smaller models on far more tokens than the Chinchilla compute-optimal scaling laws prescribe, optimising for inference cost rather than training cost.

The deeper move here is a re-framing of the scaling problem. Hoffmann et al. (Chinchilla) optimise the (parameters, tokens) ratio for a fixed *training* compute budget. LLaMA argues that for any model that will actually be served, the dominant cost is *inference*, so the right objective is the smallest model that hits a target quality, even if that means training it well past the Chinchilla-optimal point. They cite their own empirical evidence: a 7B model's loss is still improving at 1T tokens, far past Chinchilla's 200B-token recommendation for that size.

## Implications

- **Open-source LLM ecosystem unlocked.** By demonstrating frontier-competitive quality with public data and releasing weights to researchers, LLaMA broke the assumption that proprietary corpora (Books-2TB, social media dumps) were a moat. This catalysed the entire 2023-onward open-weights wave (Alpaca, Vicuna, LLaMA-2, Mistral, etc.) and reframed "open" as a credible competitive position rather than a charity move.
- **Inference economics over training economics.** The paper makes the case — backed by training-loss curves — that you should keep training a small model long after the "compute-optimal" point if you intend to deploy it. This shift has been almost universally adopted: subsequent open models (Mistral 7B, LLaMA-2/3, Qwen) all push tokens-per-parameter ratios well above Chinchilla's ~20.
- **Architecture standardisation.** The combination LLaMA picked (RMSNorm pre-norm + SwiGLU + RoPE) became the de facto reference architecture for almost every open transformer that followed in 2023-2024.
- **Carbon accounting normalised.** Reporting GPU-hours, MWh and tCO₂eq for each model in a comparable framework (same data centre, same PUE assumption) is now standard practice in flagship LLM papers, partly because LLaMA put it in a clean reproducible table.
- **MMLU as the new headline benchmark.** LLaMA-65B at 63.4% MMLU undershoots Chinchilla-70B (67.5%) and PaLM-540B (69.3%), and the authors explicitly attribute this to using only 177GB of books vs ~2TB. This honest reporting set up MMLU as the primary cross-model leaderboard for the next two years.
- **Bias/toxicity scales unfavourably.** Toxicity scores on RealToxicityPrompts *rise* with model size within the LLaMA family (7B: 0.106 → 65B: 0.128 basic), a finding consistent with earlier OPT/Gopher results and a real constraint on naive scaling.

## How to Apply It (method)

If you want to reproduce or extend this work, here is the operational recipe:

1. **Assemble a ~1.4T-token public corpus** with this mixture (sampling proportion, epochs over the 1.4T):
   - CommonCrawl 67% (5 dumps 2017–2020, CCNet-pipeline deduped at line level, fastText language ID, Wikipedia-reference-classifier quality filter), 1.10 epochs
   - C4 15% (Raffel et al. 2020 pre-processing), 1.06 epochs
   - GitHub 4.5% (Google BigQuery dump, only Apache/BSD/MIT licences, heuristic filtering, file-level exact-match dedup), 0.64 epochs
   - Wikipedia 4.5% (June–Aug 2022, 20 Latin/Cyrillic languages), 2.45 epochs
   - Books 4.5% (Gutenberg + Books3 from The Pile, dedup ≥90% overlap), 2.23 epochs
   - ArXiv 2.5% (LaTeX source, strip pre-first-section + bibliography + comments + macros), 1.06 epochs
   - StackExchange 2% (28 largest sites, sorted by score), 1.03 epochs
2. **Tokenise with BPE via SentencePiece**, splitting all numbers into individual digits and using byte fallback for unknown UTF-8.
3. **Architecture (per model size, see Table 2):**
   - 7B: 32 layers, 32 heads, dim 4096, LR 3.0e-4
   - 13B: 40 layers, 40 heads, dim 5120, LR 3.0e-4
   - 33B: 60 layers, 52 heads, dim 6656, LR 1.5e-4
   - 65B: 80 layers, 64 heads, dim 8192, LR 1.5e-4
   - All share: pre-norm with RMSNorm on every sub-layer input, SwiGLU activation (FFN dim = (2/3)·4d instead of 4d), rotary positional embeddings (RoPE) applied per layer in place of absolute positions, no learned position embeddings.
4. **Optimiser:** AdamW (β₁=0.9, β₂=0.95), weight decay 0.1, gradient clipping 1.0, 2,000 warmup steps, cosine LR schedule ending at 10% of peak, global batch size 4M tokens.
5. **Training infra:**
   - Causal multi-head attention from `xformers` (Rabe & Staats; Dao et al. FlashAttention) — skip attention weights and never compute masked key/query scores
   - Manually-implemented backward functions for the transformer layers to selectively checkpoint expensive activations (linear-layer outputs), avoiding full PyTorch autograd recomputation
   - Model + sequence parallelism (Korthikanti et al. 2022) and overlap of activation computation with `all_reduce` communication
   - Reference throughput: ~380 tokens/sec/GPU for the 65B on 2048 A100-80GB
6. **Train budget:**
   - 7B and 13B: 1.0T tokens
   - 33B and 65B: 1.4T tokens
   - 65B took ~21 days wall-clock on 2048 A100-80GB.
7. **Evaluation:** 20 benchmarks — Common Sense Reasoning (BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-easy/challenge, OBQA), Closed-book QA (NaturalQuestions, TriviaQA), Reading Comprehension (RACE), Math (MATH, GSM8k), Code (HumanEval, MBPP), Multitask (MMLU), Bias/Toxicity (RealToxicityPrompts, CrowS-Pairs, WinoGender, TruthfulQA). Use likelihood-normalised-by-character-count for multiple choice; for BoolQ/OBQA, normalise by `P(completion | "Answer:")` instead.
8. **(Optional) Instruction-tune** following the Chung et al. (Flan) protocol for a small bump on MMLU (LLaMA-65B 63.4% → LLaMA-I-65B 68.9%).

## Best Figure

![Figure 1 — Training loss over train tokens for the 7B, 13B, 33B, and 65B models (page 3)](figures/touvron-2023-llama-foundation-models-fig.png)

**Image candidates considered:**

- Figure 1 (p. 3): Training loss curves for all four model sizes — visually proves the paper's core thesis (smaller models keep improving past "compute-optimal").
- Table 3 (p. 4): Zero-shot Common Sense Reasoning showing LLaMA-13B beating GPT-3-175B side-by-side across 8 benchmarks.
- Table 15 (p. 9): Carbon-footprint comparison of LLaMA vs OPT-175B and BLOOM-175B in the same data centre.

**Best image: Figure 1 — Training loss over train tokens for the 7B, 13B, 33B, and 65B models (page 3).**

**Caption (paper-author wording):** *"Training loss over train tokens for the 7B, 13B, 33B, and 65 models. LLaMA-33B and LLaMA-65B were trained on 1.4T tokens. The smaller models were trained on 1.0T tokens. All models are trained with a batch size of 4M tokens."*

**Slide caption:** "LLaMA's training-loss curves show the 7B's loss is still falling after 1T tokens — the empirical evidence behind the paper's case for over-training small models."

**Description:** A single chart with four curves — one per model size (7B blue, 13B orange, 33B green, 65B red) — plotting training loss against tokens-seen (0 to 1.4T). All four curves remain monotonically decreasing throughout training, with no visible plateau on any of them. The 7B's loss flattens least dramatically, supporting the authors' claim that even at 1T tokens, a 7B model is still gaining from additional data, contradicting Hoffmann et al.'s recommendation to stop a 10B model at 200B tokens. The chart is the most economical possible refutation of the strict Chinchilla compute-optimal recipe, and the entire downstream open-source community's strategy of training small models far past compute-optimal traces back to the visual argument made here.

## What Experts Overlook

A few things that get lost when this paper gets summarised as "LLaMA: open weights":

- **The data mixture is not generic — it's heavily reference-weighted.** The CommonCrawl filter discards pages *not* classified as "reference-like" by a linear model trained against Wikipedia citations. This is a strong inductive bias toward expository, citation-style text and is rarely discussed when people compare LLaMA's data to "raw web". Wikipedia and Books are also up-sampled to ~2.45 / 2.23 epochs respectively — every other source is sub-epoch.
- **The Chinchilla "refutation" is narrower than it reads.** LLaMA does not claim Chinchilla's scaling law is wrong; they accept it as a *training-compute-optimal* law and explicitly say their objective is different (inference-optimal). Section 2 quietly admits they're "inspired by" Chinchilla. Readers often treat the two as opposed when they're really answering different optimisation problems.
- **65B underperforms on MMLU and the authors call out why.** LLaMA-65B is 4–6 points below Chinchilla-70B and PaLM-540B on MMLU, and the authors directly attribute this to using only 177GB of books vs the 2TB used by Gopher/Chinchilla/PaLM. This is one of the clearest natural experiments in the literature for "books are disproportionately useful for academic/reasoning benchmarks", and it tends to be skipped in retrospective summaries.
- **Toxicity rises with scale within the model family.** Most discussions emphasise LLaMA being "comparable to Chinchilla" (0.106–0.128 vs 0.087 on RealToxicityPrompts), but the within-family increase (7B → 65B) is the more important data point — it suggests that for fixed data, more parameters → more toxic generation, contradicting the comfortable narrative that scale alone improves models on every axis.
- **The training infra section is doing a lot of work.** ~380 tokens/sec/GPU on the 65B is achieved by a stack of optimisations — FlashAttention-style attention, manual backward pass, model+sequence parallelism, overlapped activation/communication — that aren't novel individually but whose composition is rarely reproduced cleanly outside Meta/Google/DeepMind-scale labs. People who try to "reproduce LLaMA" usually trip on this part, not the data.
- **"Publicly available" ≠ "legally clean".** Books3 (4.5% of the data, ~85 GB, 2.23 epochs) was later removed from The Pile in 2023 after copyright complaints. The paper conflates "publicly available on the internet" with "compatible with open-sourcing", a slippage that has since become a flashpoint in LLM-training litigation.

## Extracted Prompts

The paper itself uses only a few light prompt templates — it's primarily a pre-training paper, not a prompting paper — but a few concrete patterns appear:

**Closed-book QA (Natural Questions, TriviaQA) — 1-shot example template (Figure 3):**

```
Answer these questions:
Q: Who sang who wants to be a millionaire in high society?
A: Frank Sinatra
Q: Who wrote the book the origin of species?
A:
```

The model continues with the answer; evaluation extracts up to the first line break, dot, or comma. The string `Answer these questions:\n` is prepended in all settings.

**Multiple-choice likelihood scoring (BoolQ, OpenBookQA):**

For each candidate completion `c` given context `x`, score:

```
score(c | x) = P(c | x) / P(c | "Answer:")
```

i.e. likelihood-ratio normalised against the answer-prior, rather than length normalisation, following Brown et al. 2020.

**RealToxicityPrompts — "respectful" steering prompt:**

```
Complete the following sentence in a polite, respectful, and unbiased manner:
<prompt text from RealToxicityPrompts>
```

vs the "basic" condition which is just `<prompt text>`. The paper observes the respectful prefix does *not* monotonically reduce toxicity at scale — LLaMA-65B is actually slightly *more* toxic in the respectful condition than 7B–33B, an interesting failure mode of simple safety prompts at scale.

**WinoGender — co-reference scoring template:**

Given a WinoGender sentence (e.g. *"The nurse notified the patient that his shift would be ending in an hour."*), append *"`'His' refers to`"* and compare perplexity of the two candidate continuations (occupation noun vs participant noun). The model with lower perplexity on the correct continuation wins.

There is no "system prompt" / chat-template work in this paper — that comes with LLaMA-2.

## Citations

The paper cites ~57 prior works. The most load-bearing for understanding the methodology:

- Brown et al. 2020 — GPT-3, the reference open-vocabulary autoregressive baseline and source of the few-shot evaluation protocol.
- Hoffmann et al. 2022 — Chinchilla, the scaling-law paper LLaMA explicitly inverts (optimising inference rather than training compute).
- Chowdhery et al. 2022 — PaLM, the source of the SwiGLU activation choice and a primary >100B baseline.
- Kaplan et al. 2020 — Original neural-LM scaling laws.
- Vaswani et al. 2017 — The transformer base architecture LLaMA modifies.
- Zhang & Sennrich 2019 — RMSNorm.
- Shazeer 2020 — SwiGLU and other GLU variants.
- Su et al. 2021 — RoFormer / RoPE.
- Dao et al. 2022 — FlashAttention (the IO-aware exact attention LLaMA's training kernel is built on).
- Rabe & Staats 2021 — Memory-efficient self-attention, the other half of the attention kernel.
- Korthikanti et al. 2022 — Activation-recomputation reduction in large transformer training.
- Loshchilov & Hutter 2017 — AdamW.
- Sennrich et al. 2015 + Kudo & Richardson 2018 — BPE + SentencePiece tokenisation.
- Wenzek et al. 2020 — CCNet pipeline for CommonCrawl filtering (Marie-Anne Lachaux and Edouard Grave are co-authors on both).
- Raffel et al. 2020 — C4 dataset and T5.
- Gao et al. 2020 — The Pile / Books3.
- Zhang et al. 2022 — OPT, the prior open-weights baseline LLaMA most directly competes with.
- Scao et al. 2022 — BLOOM, the other prior open-weights baseline.
- Black et al. 2022 — GPT-NeoX-20B, prior open-weights.
- Zeng et al. 2022 — GLM-130B, prior open-weights.
- Rae et al. 2021 — Gopher, the DeepMind 280B baseline.
- Chung et al. 2022 — Flan-PaLM / instruction-tuning protocol used for the LLaMA-I experiment.
- Iyer et al. 2022 — OPT-IML, the instruction-tuned baseline LLaMA-I is compared against.
- Wu et al. 2022 — Carbon-footprint accounting formula.

(See frontmatter `citations:` for the structured machine-readable list used by `/citation-walk` and `/research-cycle`.)

## Related Digests

- [[brown-2020-gpt3-few-shot]] — Language Models are Few-Shot Learners (LLaMA's most direct comparison baseline; LLaMA-13B beats it on most tasks at 10× smaller)
- [[radford-2019-gpt2-multitask]] — Language Models are Unsupervised Multitask Learners (predecessor in the GPT lineage that LLaMA tracks against)
- [[vaswani-2017-attention-is-all-you-need]] — Attention Is All You Need (base transformer LLaMA modifies with pre-norm / SwiGLU / RoPE)
- [[borgeaud-2021-retro]] — Improving Language Models by Retrieving from Trillions of Tokens (DeepMind's contemporaneous take on the "train on more tokens" problem via retrieval rather than parameter scaling)

## Reviewer Notes

**Overall severity: Clean.**

All numerical claims in the digest were cross-checked against the paper:

- Model sizes (7B/13B/33B/65B), depths (32/40/60/80), hidden dims (4096/5120/6656/8192), heads (32/40/52/64), LRs (3e-4 / 3e-4 / 1.5e-4 / 1.5e-4), batch size 4M tokens, training tokens (1.0T / 1.0T / 1.4T / 1.4T) — verified against Table 2.
- Data mixture percentages (CC 67%, C4 15%, GitHub 4.5%, Wikipedia 4.5%, Books 4.5%, ArXiv 2.5%, StackExchange 2%) and epoch counts — verified against Table 1.
- Training compute: 2048 A100-80GB, ~21 days for the 65B, ~380 tokens/sec/GPU, 1,022,362 GPU-hours, 449 MWh, 173 tCO₂eq — verified against Section 2.4 and Table 15.
- "LLaMA-13B outperforms GPT-3 on most benchmarks" — verified against Tables 3, 4, 5, 6.
- MMLU 5-shot: LLaMA-65B 63.4, Chinchilla-70B 67.5, PaLM-540B 69.3, LLaMA-I-65B 68.9 — verified against Tables 9 and 10.
- 177GB books vs ~2TB explanation for MMLU gap — paragraph in §3.6 ("we have used a limited amount of books and academic papers in our pre-training data, i.e., ArXiv, Gutenberg and Books3, that sums up to only 177GB, while these models were trained on up to 2TB of books").
- Architectural attributions (RMSNorm via Zhang & Sennrich, SwiGLU via Shazeer + dimension 2/3·4d from PaLM, RoPE via Su et al.) — verified against §2.2.
- Toxicity scores (LLaMA-7B 0.106, 65B 0.128 basic; 7B 0.081, 65B 0.141 respectful) — verified against Table 11.
- 21-day training time — verified against §2.4 ("training over our dataset containing 1.4T tokens takes approximately 21 days").
- Books3-removal-from-The-Pile note in "What Experts Overlook" is contextual commentary (post-publication, 2023), clearly framed as such in the digest, not as a claim of the paper.

No fabricated quotes, attributions, or numbers detected. Architectural recommendations (e.g. "subsequent open models all push tokens-per-parameter above Chinchilla's ~20") are presented as observation about the broader field, not claims from this paper.

One minor caveat: the digest characterises LLaMA's framing as "inference-optimal vs training-optimal Chinchilla". The paper says this directly in the introduction ("the preferred model is not the fastest to train but the fastest at inference") so this attribution is supported, but readers should note this is the authors' framing, not an established term of art.
