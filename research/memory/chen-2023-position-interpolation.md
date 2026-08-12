---
corpus: agentic-memory
kind: paper-digest
slug: chen-2023-position-interpolation
title: "Extending Context Window of Large Language Models via Positional Interpolation"
authors:
  - "Chen, Shouyuan"
  - "Wong, Sherman"
  - "Chen, Liangjian"
  - "Tian, Yuandong"
year: 2023
publication_date: "2023-06"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2306.15595"
doi: null
arxiv_id: "2306.15595"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Don't extrapolate position encodings past where the model was trained — interpolate them inward."
topics:
  - long-context
  - position-encoding
  - rope
  - llama
  - context-window-extension
  - fine-tuning
tags:
  - paper
  - llm
  - transformer
  - attention
  - canonical
entities:
  - chen-shouyuan
  - tian-yuandong
  - meta-ai
related_digests:
  - dai-2019-transformer-xl
  - liu-2023-lost-in-the-middle
  - xiao-2023-streaming-llm
  - bulatov-2022-recurrent-memory-transformer
  - beltagy-2020-longformer
  - vaswani-2017-attention-is-all-you-need
citations:
  - title: "Colt5: Faster long-range transformers with conditional computation"
    authors: ["Joshua Ainslie", "Tao Lei", "Michiel de Jong", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Proof-pile"
    authors: ["Zhangir Azerbayev", "Edward Ayers", "Bartosz Piotrowski"]
    year: 2022
    venue: "github"
    doi: null
    url: "https://github.com/zhangir-azerbayev/proof-pile"
    arxiv_id: null
  - title: "Longformer: The long-document transformer"
    authors: ["Iz Beltagy", "Matthew E. Peters", "Arman Cohan"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Recurrent memory transformer"
    authors: ["Aydar Bulatov", "Yuri Kuratov", "Mikhail S. Burtsev"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generating long sequences with sparse transformers"
    authors: ["Rewon Child", "Scott Gray", "Alec Radford", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Rethinking attention with performers"
    authors: ["Krzysztof Choromanski", "Valerii Likhosherstov", "David Dohan", "et al."]
    year: 2021
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "RedPajama: An open source recipe to reproduce LLaMA training dataset"
    authors: ["Together Computer"]
    year: 2023
    venue: "github"
    doi: null
    url: "https://github.com/togethercomputer/RedPajama-Data"
    arxiv_id: null
  - title: "Transformer-XL: Attentive language models beyond a fixed-length context"
    authors: ["Zihang Dai", "Zhilin Yang", "Yiming Yang", "et al."]
    year: 2019
    venue: "ACL"
    doi: "10.18653/v1/P19-1285"
    url: null
    arxiv_id: null
  - title: "FlashAttention: Fast and memory-efficient exact attention with IO-awareness"
    authors: ["Tri Dao", "Daniel Y. Fu", "Stefano Ermon", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "An image is worth 16x16 words: Transformers for image recognition at scale"
    authors: ["Alexey Dosovitskiy", "Lucas Beyer", "Alexander Kolesnikov", "et al."]
    year: 2021
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=YicbFdNTTy"
    arxiv_id: null
  - title: "The Pile: An 800GB dataset of diverse text for language modeling"
    authors: ["Leo Gao", "Stella Biderman", "Sid Black", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2101.00027"
  - title: "REALM: Retrieval-augmented language model pre-training"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Transformer language models without positional encodings still learn positional information"
    authors: ["Adi Haviv", "Ori Ram", "Ofir Press", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "LoRA: Low-rank adaptation of large language models"
    authors: ["Edward J. Hu", "Yelong Shen", "Phillip Wallis", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2106.09685"
  - title: "Efficient attentions for long document summarization"
    authors: ["Luyang Huang", "Shuyang Cao", "Nikolaus Parulian", "et al."]
    year: 2021
    venue: "NAACL"
    doi: "10.18653/v1/2021.naacl-main.112"
    url: "https://aclanthology.org/2021.naacl-main.112"
    arxiv_id: null
  - title: "Atlas: Few-shot learning with retrieval augmented language models"
    authors: ["Gautier Izacard", "Patrick Lewis", "Maria Lomeli", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Retrieval as attention: End-to-end learning of retrieval and reading within a single transformer"
    authors: ["Zhengbao Jiang", "Luyu Gao", "Jun Araki", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Things I'm learning while training SuperHOT"
    authors: ["kaiokendev"]
    year: 2023
    venue: "blog"
    doi: null
    url: "https://kaiokendev.github.io/til#extending-context-to-8k"
    arxiv_id: null
  - title: "Dense passage retrieval for open-domain question answering"
    authors: ["Vladimir Karpukhin", "Barlas Oguz", "Sewon Min", "et al."]
    year: 2020
    venue: "EMNLP"
    doi: "10.18653/v1/2020.emnlp-main.550"
    url: null
    arxiv_id: null
  - title: "Relevance-guided supervision for OpenQA with ColBERT"
    authors: ["Omar Khattab", "Christopher Potts", "Matei Zaharia"]
    year: 2021
    venue: "TACL"
    doi: "10.1162/tacl_a_00405"
    url: null
    arxiv_id: null
  - title: "Reformer: The efficient transformer"
    authors: ["Nikita Kitaev", "Lukasz Kaiser", "Anselm Levskaya"]
    year: 2020
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing"
    authors: ["Taku Kudo", "John Richardson"]
    year: 2018
    venue: "EMNLP demo"
    doi: "10.18653/v1/D18-2012"
    url: "https://aclanthology.org/D18-2012"
    arxiv_id: null
  - title: "ROUGE: A package for automatic evaluation of summaries"
    authors: ["Chin-Yew Lin"]
    year: 2004
    venue: "Text Summarization Branches Out"
    doi: null
    url: "https://aclanthology.org/W04-1013"
    arxiv_id: null
  - title: "Decoupled weight decay regularization"
    authors: ["Ilya Loshchilov", "Frank Hutter"]
    year: 2019
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=Bkg6RiCqY7"
    arxiv_id: null
  - title: "∞-former: Infinite memory transformer"
    authors: ["Pedro Henrique Martins", "Zita Marinho", "André F. T. Martins"]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Landmark attention: Random-access infinite context length for transformers"
    authors: ["Amirkeivan Mohtashami", "Martin Jaggi"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2305.16300"
  - title: "Learning to compress prompts with gist tokens"
    authors: ["Jesse Mu", "Xiang Lisa Li", "Noah Goodman"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "PyTorch: An Imperative Style, High-Performance Deep Learning Library"
    authors: ["Adam Paszke", "Sam Gross", "Francisco Massa", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Train short, test long: Attention with linear biases enables input length extrapolation (ALiBi)"
    authors: ["Ofir Press", "Noah Smith", "Mike Lewis"]
    year: 2022
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=R8sQPpGCv0"
    arxiv_id: null
  - title: "Compressive transformers for long-range sequence modelling"
    authors: ["Jack W. Rae", "Anna Potapenko", "Siddhant M. Jayakumar", "et al."]
    year: 2020
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=SylKikSYDH"
    arxiv_id: null
  - title: "Combiner: Full attention transformer with sparse computation cost"
    authors: ["Hongyu Ren", "Hanjun Dai", "Zihang Dai", "et al."]
    year: 2021
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "ColBERTv2: Effective and efficient retrieval via lightweight late interaction"
    authors: ["Keshav Santhanam", "Omar Khattab", "Jon Saad-Falcon", "et al."]
    year: 2022
    venue: "NAACL"
    doi: "10.18653/v1/2022.naacl-main.272"
    url: null
    arxiv_id: null
  - title: "SCROLLS: Standardized CompaRison over long language sequences"
    authors: ["Uri Shaham", "Elad Segal", "Maor Ivgi", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: null
    url: "https://aclanthology.org/2022.emnlp-main.823"
    arxiv_id: null
  - title: "RoFormer: Enhanced transformer with rotary position embedding (RoPE)"
    authors: ["Jianlin Su", "Yu Lu", "Shengfeng Pan", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "A length-extrapolatable transformer"
    authors: ["Yutao Sun", "Li Dong", "Barun Patra", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "LLaMA: Open and efficient foundation language models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: "https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf"
    arxiv_id: null
  - title: "Linformer: Self-attention with linear complexity"
    authors: ["Sinong Wang", "Belinda Z. Li", "Madian Khabsa", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memformer: A memory-augmented transformer for sequence modeling"
    authors: ["Qingyang Wu", "Zhenzhong Lan", "Kun Qian", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memorizing transformers"
    authors: ["Yuhuai Wu", "Markus Norman Rabe", "DeLesley Hutchins", "et al."]
    year: 2022
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Big Bird: Transformers for longer sequences"
    authors: ["Manzil Zaheer", "Guru Guruganesh", "Kumar Avinava Dubey", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "OPT: Open pre-trained transformer language models"
    authors: ["Susan Zhang", "Stephen Roller", "Naman Goyal", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "PyTorch FSDP: Experiences on scaling fully sharded data parallel"
    authors: ["Yanli Zhao", "Andrew Gu", "Rohan Varma", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Extrapolation versus interpolation"
  page: 4
  image_path: "figures/chen-2023-position-interpolation-fig.png"
---

# Extending Context Window of Large Language Models via Positional Interpolation

**Authors:** Shouyuan Chen, Sherman Wong, Liangjian Chen, Yuandong Tian (Meta Platforms Inc.)
**Published:** 2023-06 · [Source](https://arxiv.org/abs/2306.15595)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Chen et al. show that you can stretch the context window of a RoPE-based LLM (they use LLaMA 7B–65B, originally 2048 tokens) up to 32,768 tokens by linearly down-scaling the integer position indices into the original pre-trained range — instead of letting them run past it — and then fine-tuning for only ~1000 steps on the Pile. Naive direct fine-tuning at longer lengths barely moves the effective window (2048 → 2560 after >10,000 steps); Position Interpolation reaches the full target window (8192/16384/32768) in just 200 steps of fine-tuning and shows monotonically decreasing perplexity as the context grows (e.g. LLaMA-7B on PG19: 7.20 at 2048 → 6.77 at 32768; on Arxiv Math Proof-pile: 2.77 → 2.24 at 16384). Theoretically, the interpolated attention-score bound is at least ~600× smaller than the extrapolation bound in the LLaMA-7B setting (`d/(8 ln c)` vs. `≥ 2d·B(s)`), which the authors prove via a second-order Taylor argument. On standard 2048-token LLaMA benchmarks (BoolQ, PIQA, RACE-M/H, WinoGrande) the extended models lose only ~2% at 8k context and somewhat more at 32k, and on GovReport summarization the 16k-extended LLaMA-7B reaches ROUGE-1 60.0 — competitive with CoLT5 XL (61.3) — without architecture changes. The actionable takeaway: don't extrapolate position encodings past their trained range — interpolate them inward instead, and almost no fine-tuning is needed.

## Key Takeaway

The catastrophic failure of "just run RoPE at a longer sequence length" was never about the model forgetting how to attend at distance — it was about position encodings being asked to produce values they never produced during training. RoPE attention scores look well-behaved inside the training range but the trigonometric basis is a universal approximator, so the same coefficients that fit a tame curve on [0, 2048] can balloon to >8000 on [2048, 4096]. Squeezing the new, longer position indices back into the trained range (the "interpolation" move) keeps every attention score inside a region the model already knows is safe — and that's why fine-tuning needs only hundreds of steps instead of months.

## Implications

- **If you need a longer context window, don't train a new model — interpolate the position indices of an existing one**: For any RoPE-based pre-trained LLM, scaling input position indices `m → mL/L'` (where `L` is the original window and `L'` the desired one) plus ~1000 steps of fine-tuning is enough to reach 4× to 16× the original window with usable quality. This is dramatically cheaper than pre-training from scratch on long sequences.
- **Stop treating "context window" as a fixed architectural property**: Because PI doesn't change weights or architecture — only the rescaling of position indices — existing inference infrastructure (kv-cache, FlashAttention, sharding) keeps working. Treat context length as a post-hoc hyperparameter that can be re-targeted whenever workload demands change.
- **Budget for almost no compute when extending**: The authors used 32–128 A100s only because of memory headroom, not training time; the actual step count needed is 200 to reach the target effective window and 1000 to consolidate quality. For most labs that means a single overnight run, not a multi-week project.
- **Trust passkey-retrieval as your "did it actually extend?" test**: Perplexity can look fine while the model still can't reach back across the new window. The synthetic passkey retrieval probe (random 5-digit number hidden at varying depths in filler text) gives a hard yes/no answer on effective context — and clearly shows that direct fine-tuning is a dud (`k_max` stays at 2048–2560 after 10k steps) while PI reaches `k_max = L'` after 200 steps.
- **Expect a small quality cost on short tasks — design around it**: Models extended to 8192 lose roughly 2% on standard 2048-token benchmarks (BoolQ, PIQA, RACE, WinoGrande); extension to 32768 costs more (BoolQ drops from 76.1 to 64.7 for LLaMA-7B). If you serve both short and long prompts, consider keeping a non-extended copy for the short ones, or use a smaller extension factor.
- **Don't generalize PI to non-RoPE encodings without re-checking the theory**: The 600× bound advantage and the Taylor-based interpolation guarantee depend on RoPE's specific frequency family `θ_j = 10000^(-2j/d)`. The authors flag that learned absolute embeddings (e.g. OPT) likely need a different approach — the Vision Transformer / Dosovitskiy 2021 technique of interpolating the embeddings themselves — and that's untested at LLM scale.
- **Use the magnitude-of-coefficients lens to predict future regularization wins**: The authors note that both interpolation and extrapolation bounds share the term `max_j |h_j|` — the maximum magnitude of query/key dot products. Regularizing this term during pre-training could make extrapolation safe natively, eliminating the need for the interpolation trick entirely. This is an open lever no one has pulled.
- **PI is complementary to retrieval, sparse attention, and memory transformers, not in competition with them**: The paper makes the case explicitly. You can stack PI-extended attention with retrieval augmentation or efficient attention variants — they operate on different parts of the stack.

## How to Apply It (method)

**Scenario:** You run engineering at a startup that ships a B2B legal-document review tool built on an open-weight RoPE-based 7B model. Customers keep handing you 30-page contracts that blow past your 2048-token window; you can't afford to pre-train a long-context model from scratch, and "chunk-and-stitch" loses cross-clause references. You want to extend your model's window to 16384 tokens and validate that it actually uses the extra context.

**Steps:**

1. **Confirm your model uses RoPE positional encoding**: Inspect the model's attention implementation. If it's a LLaMA, Mistral, Falcon, Qwen, or similar RoPE-based architecture, PI applies directly. If it uses learned absolute embeddings (BERT, OPT) or ALiBi (BLOOM), this exact recipe does not — flag and stop.

2. **Choose extension factor `L'/L`**: Decide your target window `L'` (e.g. 16384) given your original window `L` (e.g. 2048). The scale factor is `L/L' = 0.125`. Larger factors work (up to 32×, per the paper) but the per-step degradation on short prompts grows.

3. **Modify the RoPE function in inference and training code**: Replace `f(x, m)` with `f'(x, m) = f(x, m·L/L')`. Concretely, wherever the model computes the RoPE rotation for position index `m`, multiply `m` by `L/L'` before applying the trig. No weights change; no new parameters.

4. **Prepare a fine-tuning corpus of long-form text**: Use a pre-training-grade corpus (the authors used the Pile; RedPajama works equivalently). Pack samples into sequences of length `L'`. The paper found fine-tuning quality is insensitive to corpus choice — the model isn't learning new knowledge, only adapting to the rescaled positions.

5. **Fine-tune with the next-token-prediction objective for 1000 steps**:
   - Optimizer: AdamW with β1=0.9, β2=0.95, weight decay 0.
   - Learning rate: 2e-5 for 7B/13B, 1e-5 for 33B/65B, with linear warmup over 20 steps starting from 10% of max LR.
   - Batch size: 64 global for 8k window, 128 global for 16k+/larger models.
   - Run with FSDP + FlashAttention; memory dominates, not flops.
   - Checkpoint at 200, 600, 1000 steps — quality plateaus quickly after 200.

6. **Validate effective context with passkey retrieval**: Build a test set following the paper's template:

   ```
   There is an important info hidden inside a lot of irrelevant text. Find
   it and memorize them. I will quiz you about the important information
   there.
   The grass is green. The sky is blue. The sun is yellow. Here we go.
   There and back again. (repeat X times)
   The pass key is <RANDOM 5 DIGITS>. Remember it. <SAME 5 DIGITS> is the pass key.
   The grass is green. The sky is blue. The sun is yellow. Here we go.
   There and back again. (repeat Y times)
   What is the pass key? The pass key is
   ```

   Sample `k` (the passkey's distance from the prompt end) uniformly across [0, L']. Run 10 trials per `k`. Define `k_max` as the largest `k` with ≥20% success across all smaller `k`. For PI it should reach `k_max = L'`; if it doesn't, you've botched the rescaling.

7. **Sanity-check short-prompt quality**: Re-run your existing eval suite on prompts ≤ 2048 tokens. Expect a 1–5% regression on standard benchmarks; if you see much more, your fine-tuning LR is likely too high or you over-trained past 1000 steps.

8. **Validate on the actual domain task**: For the legal-review case, replay 100 historical 8–15k-token contracts through both the original (chunked) pipeline and the extended model. Compare F1 on clause-extraction tasks where the gold answer requires cross-document reference — that's where the long context should pay off.

**Expected outcome:** A drop-in replacement for your existing model that handles 8× longer inputs, reuses your inference stack (no FlashAttention rewrites, no KV-cache surgery), and shows clear, measurable wins on tasks that span the new context window. The whole project should be one engineer-week of work plus one fine-tuning run, not a quarter-long pre-training effort.

## Best Figure

![Figure 2 — Extrapolation versus interpolation (page 4)](figures/chen-2023-position-interpolation-fig.png)

Image Candidates:
Figure 1 (p. 2): Illustrates the core conceptual contrast between normal use, extrapolation, and Position Interpolation in a single schematic — good for explainers but visually qualitative.
Figure 2 (p. 4): Shows the actual numerical behavior of fitted attention scores in three panels — bounded fit inside training range, catastrophic spike when extrapolating, smooth behavior when interpolating; this is the empirical heart of the theoretical argument.
Figure 5 (p. 16): Plots the extrapolation bound term B(s)/d versus positional difference, supporting the 600× claim — important but appendix-level supporting evidence.

Best Image:
Figure Name: Figure 2: "Extrapolation versus interpolation"
Figure Page: 4
Slide Caption: A fitted attention-score function explodes past 8000 outside the training range (middle panel) but stays smoothly bounded when interpolated between integer positions (right panel) — the visual proof of why PI works.
Description: Figure 2 shows three panels for a single fitted attention-score function `a(s)` built from RoPE's basis functions at the LLaMA-7B setting (d = 4096/32 = 128). The left panel fits the function via least squares to random points within [0, 2048], producing a curve approximately within [-1, 1] — the "well-behaved" training regime. The middle panel zooms out to [0, 4096] and shows the same fitted function ballooning to over 8000 once `s > 2048` — this is the catastrophic extrapolation regime that breaks attention computation. The right panel zooms in on a small interpolated region (positional differences 30–75) with vertical dotted lines at each integer position, showing that between any two trained integer positions the curve is smooth and well-bounded. The contrast is the paper's central empirical claim: the same RoPE encoding is dangerous outside its trained range but safe inside it, so squeezing longer sequences inward is the right move.

## What Experts Overlook

The piece most readers underweight is that **PI's stability does not come from "compressing information" — it comes from forcing the relative-distance argument of every trig basis function back into a region the model has already memorized as safe**. The mechanism is visible in Section 2.3 / Theorem 2.1: RoPE's attention score is a sum of trigonometric basis functions `e^(isθ_j)` over `j ∈ [0, d/2)`, with frequencies `θ_j = 10000^(-2j/d)`. The training process implicitly learns coefficient magnitudes `|h_j|` that produce sane scores on integer `s ∈ [0, L]` — but those same coefficients are not bounded outside `[0, L]`, and the trig family is a universal approximator that can shoot to arbitrary magnitudes once you leave the trained interval. The interpolation bound (`d·max|h_j| / (8 ln c)`) is provably ~600× tighter than the extrapolation bound — but only because interpolation keeps the trig argument inside a known-safe interval. It's not a smoothness argument about the model — it's a smoothness argument about the basis functions evaluated at unseen vs. seen positions.

**Why it matters:** Many people misread PI as "the model learns to compress more tokens into less position-space." That framing predicts you'd need to fine-tune a lot — like teaching the model a new encoding. The real story is the opposite: you don't need much fine-tuning because the model already knows how to handle every position index PI feeds it (they're all in the original trained range). The fine-tuning just adapts the model to the slightly higher density of meaningful tokens at each position. That's why 200 steps already saturate effective context window, while 10,000 steps of naive fine-tuning still don't move the needle. If you assume the wrong mechanism, you'll over-budget for compute and under-budget for the rescaling math.

**Example of good use:** An ML engineer adding PI to a new RoPE-based model first verifies that her rescaling formula is correct by sanity-checking that, without any fine-tuning, perplexity at the new length is already in the low double-digits (paper reports < 20 at 8192, vs > 1000 for raw extrapolation). She knows the model "already knows" these positions, so she budgets a single overnight run for 1000 steps of fine-tuning rather than a multi-week training campaign — and ships.

**Example of misapplication:** A team trying to combine PI with a more aggressive sparse-attention scheme assumes "PI just gives me a longer window" and so they expect to fine-tune for 10,000+ steps to consolidate the new attention pattern. They burn weeks of GPU time and see slow improvement, then conclude PI "doesn't work for our case" — when the actual problem is that they confused PI's mechanism (rescaling positions into safe territory) with a learning problem (teaching the model new attention patterns). They should have validated the rescaling math first with raw PI (no fine-tuning), confirmed perplexity was already finite, and then only added their sparse-attention modification.

## Extracted Prompts

**Prompt explanation:** Passkey retrieval — synthetic probe used to estimate the effective context window size; a random 5-digit passkey is hidden inside repeated filler text and the model must retrieve it.

```
There is an important info hidden inside a lot of irrelevant text. Find
it and memorize them. I will quiz you about the important information
there.
The grass is green. The sky is blue. The sun is yellow. Here we go.
There and back again. (repeat X times)
The pass key is 12345. Remember it. 12345 is the pass key.
The grass is green. The sky is blue. The sun is yellow. Here we go.
There and back again. (repeat Y times)
What is the pass key? The pass key is
```

**Prompt explanation:** Long-document summarization template — used to fine-tune and evaluate the 16k-extended LLaMA on the GovReport dataset.

```
Read the following article and then summarize it.
# .... Document goes here
Now summarize the above article.
Summary:
```

## Citations

- Su et al. 2021 — RoFormer: Enhanced transformer with rotary position embedding (RoPE) — the position-encoding scheme PI rescales.
- Touvron et al. 2023 — LLaMA: Open and efficient foundation language models — the base model family extended in this paper.
- Press et al. 2022 — Train short, test long: Attention with linear biases enables input length extrapolation (ALiBi) — the main prior length-extrapolation baseline.
- Sun et al. 2022 — A length-extrapolatable transformer (LeX) — another extrapolation-oriented position-encoding scheme.
- Vaswani et al. 2017 — Attention is all you need — original Transformer hypothesis that motivates extrapolation work.
- Dosovitskiy et al. 2021 — An image is worth 16x16 words: ViT — the most directly related prior interpolation result (interpolating learnt position embeddings for higher-resolution images).
- Mohtashami & Jaggi 2023 — Landmark attention: Random-access infinite context length for transformers — source of the passkey-retrieval evaluation.
- Rae et al. 2020 — Compressive transformers for long-range sequence modelling — source of the PG19 evaluation dataset.
- Azerbayev et al. 2022 — Proof-pile — source of the Arxiv Math evaluation dataset.
- Huang et al. 2021 — Efficient attentions for long document summarization — source of the GovReport summarization benchmark.

(43 citations total — see frontmatter for the full structured list.)

## Related Digests

- [[dai-2019-transformer-xl]] — Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context (the earlier "extend context via recurrence + relative positions" answer that PI sidesteps)
- [[liu-2023-lost-in-the-middle]] — Lost in the Middle: How Language Models Use Long Contexts (downstream caveat — even PI-extended models have U-shaped attention)
- [[xiao-2023-streaming-llm]] — Efficient Streaming Language Models with Attention Sinks (different lever on the same length-extension problem: attention sinks vs. position interpolation)
- [[bulatov-2022-recurrent-memory-transformer]] — Recurrent Memory Transformer (alternative path: memory tokens vs. position rescaling)
- [[beltagy-2020-longformer]] — Longformer: The Long-Document Transformer (architecture-level long-context approach — sliding window + global attention)
- [[vaswani-2017-attention-is-all-you-need]] — Attention Is All You Need (origin of the "Transformer can extrapolate to longer sequences" hypothesis PI partially confirms)

## Reviewer Notes

**Overall severity:** Clean

All claims in this digest were verified against the paper text:
- Context window numbers (2048 → 32768), model sizes (7B–65B), and fine-tuning step counts (200, 1000, 10000) match Tables 1–4 and Section 3.1 exactly.
- The 600× ratio between interpolation and extrapolation bounds is stated explicitly in Section 2.3 ("the interpolation bound is at least 2 · 294.73 ∼ 600× smaller than the extrapolation bound").
- The "fitted curve > 8000 outside the trained range" detail is direct from Figure 2 / Section 2.2.
- Direct fine-tuning effective window staying at 2048→2560 after >10,000 steps is from Section 1 and Table 4.
- Perplexity drops (7.20 → 6.77 on PG19, 2.77 → 2.24 on Proof-pile) are exact values from Tables 1 and 2.
- GovReport ROUGE-1 of 60.0 vs CoLT5 XL 61.3 are from Table 6.
- Standard-benchmark degradation of "up to 2%" at 8192 and larger at 32768 is from Section 3.4 and Table 5 (BoolQ 76.1 → 73.2 at 8192, → 64.7 at 32768).
- Optimizer details (AdamW, β1=0.9, β2=0.95, LR 2e-5/1e-5, weight decay 0, 20-step warmup, FSDP + FlashAttention) are exact from Section 3.1.
- The passkey-retrieval template is reproduced verbatim from Figure 3.
- The Taylor-expansion proof in Appendix A is correctly summarized.

No fabricated numbers, no overextended claims, no invented baselines.
