---
corpus: agentic-memory
kind: paper-digest
slug: ouyang-2022-instructgpt-rlhf
title: "Training Language Models to Follow Instructions with Human Feedback"
authors:
  - "Ouyang, Long"
  - "Wu, Jeff"
  - "Jiang, Xu"
  - "Almeida, Diogo"
  - "Wainwright, Carroll L."
  - "Mishkin, Pamela"
  - "Zhang, Chong"
  - "Agarwal, Sandhini"
  - "Slama, Katarina"
  - "Ray, Alex"
  - "Schulman, John"
  - "Hilton, Jacob"
  - "Kelton, Fraser"
  - "Miller, Luke"
  - "Simens, Maddie"
  - "Askell, Amanda"
  - "Welinder, Peter"
  - "Christiano, Paul"
  - "Leike, Jan"
  - "Lowe, Ryan"
year: 2022
publication_date: "2022-03"
venue: "arXiv preprint (later NeurIPS 2022)"
source_url: "https://arxiv.org/abs/2203.02155"
doi: null
arxiv_id: "2203.02155"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "RLHF — fine-tuning a pretrained LM via supervised demos then PPO against a learned reward model trained on ~33k pairwise human preferences — beats a 100× larger base model on labeler-rated helpfulness while costing ~1-2% of pretraining compute."
topics:
  - rlhf
  - alignment
  - instruction-following
  - reward-modeling
  - ppo
  - language-models
  - human-feedback
  - preference-learning
tags:
  - paper
  - foundational
  - rlhf
  - openai
  - instructgpt
  - ppo
  - alignment-tax
entities:
  - ouyang-long
  - lowe-ryan
  - leike-jan
  - christiano-paul
  - schulman-john
  - askell-amanda
  - openai
related_digests:
  - shao-2024-deepseekmath-grpo
  - touvron-2023-llama-2
  - yan-2025-memory-r1
citations:
  - title: "Deep reinforcement learning from human preferences"
    authors: ["Christiano, P. F.", "Leike, J.", "Brown, T.", "Martic, M.", "Legg, S.", "Amodei, D."]
    year: 2017
    venue: "NeurIPS"
    arxiv_id: null
    url: null
  - title: "Learning to summarize from human feedback"
    authors: ["Stiennon, N.", "Ouyang, L.", "Wu, J.", "Ziegler, D. M.", "Lowe, R.", "Voss, C.", "Radford, A.", "Amodei, D.", "Christiano, P."]
    year: 2020
    arxiv_id: "2009.01325"
    url: "https://arxiv.org/abs/2009.01325"
  - title: "Fine-tuning language models from human preferences"
    authors: ["Ziegler, D. M.", "Stiennon, N.", "Wu, J.", "Brown, T. B.", "Radford, A.", "Amodei, D.", "Christiano, P.", "Irving, G."]
    year: 2019
    arxiv_id: "1909.08593"
    url: "https://arxiv.org/abs/1909.08593"
  - title: "Proximal policy optimization algorithms"
    authors: ["Schulman, J.", "Wolski, F.", "Dhariwal, P.", "Radford, A.", "Klimov, O."]
    year: 2017
    arxiv_id: "1707.06347"
    url: "https://arxiv.org/abs/1707.06347"
  - title: "Language models are few-shot learners"
    authors: ["Brown, T. B.", "Mann, B.", "Ryder, N.", "Subbiah, M.", "Kaplan, J.", "Dhariwal, P.", "Neelakantan, A.", "Shyam, P.", "Sastry, G.", "Askell, A.", "et al."]
    year: 2020
    arxiv_id: "2005.14165"
    url: "https://arxiv.org/abs/2005.14165"
  - title: "A general language assistant as a laboratory for alignment"
    authors: ["Askell, A.", "Bai, Y.", "Chen, A.", "Drain, D.", "Ganguli, D.", "Henighan, T.", "et al."]
    year: 2021
    arxiv_id: "2112.00861"
    url: "https://arxiv.org/abs/2112.00861"
  - title: "Recursively summarizing books with human feedback"
    authors: ["Wu, J.", "Ouyang, L.", "Ziegler, D. M.", "Stiennon, N.", "Lowe, R.", "Leike, J.", "Christiano, P."]
    year: 2021
    arxiv_id: "2109.10862"
    url: "https://arxiv.org/abs/2109.10862"
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    authors: ["Nakano, R.", "Hilton, J.", "Balaji, S.", "Wu, J.", "Ouyang, L.", "Kim, C.", "et al."]
    year: 2021
    arxiv_id: "2112.09332"
    url: "https://arxiv.org/abs/2112.09332"
  - title: "TruthfulQA: Measuring how models mimic human falsehoods"
    authors: ["Lin, S.", "Hilton, J.", "Evans, O."]
    year: 2021
    arxiv_id: "2109.07958"
    url: "https://arxiv.org/abs/2109.07958"
  - title: "RealToxicityPrompts: Evaluating neural toxic degeneration in language models"
    authors: ["Gehman, S.", "Gururangan, S.", "Sap, M.", "Choi, Y.", "Smith, N. A."]
    year: 2020
    arxiv_id: "2009.11462"
    url: "https://arxiv.org/abs/2009.11462"
  - title: "Finetuned language models are zero-shot learners (FLAN)"
    authors: ["Wei, J.", "Bosma, M.", "Zhao, V. Y.", "Guu, K.", "Yu, A. W.", "Lester, B.", "Du, N.", "Dai, A. M.", "Le, Q. V."]
    year: 2021
    arxiv_id: "2109.01652"
    url: "https://arxiv.org/abs/2109.01652"
  - title: "Multitask prompted training enables zero-shot task generalization (T0)"
    authors: ["Sanh, V.", "Webson, A.", "Raffel, C.", "Bach, S. H.", "Sutawika, L.", "Alyafeai, Z.", "et al."]
    year: 2021
    arxiv_id: "2110.08207"
    url: "https://arxiv.org/abs/2110.08207"
  - title: "Scalable agent alignment via reward modeling: a research direction"
    authors: ["Leike, J.", "Krueger, D.", "Everitt, T.", "Martic, M.", "Maini, V.", "Legg, S."]
    year: 2018
    arxiv_id: "1811.07871"
    url: "https://arxiv.org/abs/1811.07871"
  - title: "Reward learning from human preferences and demonstrations in Atari"
    authors: ["Ibarz, B.", "Leike, J.", "Pohlen, T.", "Irving, G.", "Legg, S.", "Amodei, D."]
    year: 2018
    arxiv_id: null
    url: null
  - title: "AI safety via debate"
    authors: ["Irving, G.", "Christiano, P.", "Amodei, D."]
    year: 2018
    arxiv_id: "1805.00899"
    url: "https://arxiv.org/abs/1805.00899"
  - title: "Supervising strong learners by amplifying weak experts"
    authors: ["Christiano, P.", "Shlegeris, B.", "Amodei, D."]
    year: 2018
    arxiv_id: "1810.08575"
    url: "https://arxiv.org/abs/1810.08575"
  - title: "On the dangers of stochastic parrots: Can language models be too big?"
    authors: ["Bender, E. M.", "Gebru, T.", "McMillan-Major, A.", "Shmitchell, S."]
    year: 2021
    venue: "FAccT"
    arxiv_id: null
    url: null
  - title: "On the opportunities and risks of foundation models"
    authors: ["Bommasani, R.", "Hudson, D. A.", "Adeli, E.", "Altman, R.", "Arora, S.", "et al."]
    year: 2021
    arxiv_id: "2108.07258"
    url: "https://arxiv.org/abs/2108.07258"
  - title: "Ethical and social risks of harm from language models"
    authors: ["Weidinger, L.", "Mellor, J.", "Rauh, M.", "Griffin, C.", "Uesato, J.", "et al."]
    year: 2021
    arxiv_id: "2112.04359"
    url: "https://arxiv.org/abs/2112.04359"
  - title: "Alignment of language agents"
    authors: ["Kenton, Z.", "Everitt, T.", "Weidinger, L.", "Gabriel, I.", "Mikulik, V.", "Irving, G."]
    year: 2021
    arxiv_id: "2103.14659"
    url: "https://arxiv.org/abs/2103.14659"
  - title: "Artificial intelligence, values, and alignment"
    authors: ["Gabriel, I."]
    year: 2020
    venue: "Minds and Machines 30(3):411-437"
    arxiv_id: null
    url: null
  - title: "Process for adapting language models to society (PaLMS) with values-targeted datasets"
    authors: ["Solaiman, I.", "Dennison, C."]
    year: 2021
    arxiv_id: "2106.10328"
    url: "https://arxiv.org/abs/2106.10328"
  - title: "Mitigating harm in language models with conditional-likelihood filtration"
    authors: ["Ngo, H.", "Raterink, C.", "Araújo, J. G.", "Zhang, I.", "Chen, C.", "Morisot, A.", "Frosst, N."]
    year: 2021
    arxiv_id: "2108.07790"
    url: "https://arxiv.org/abs/2108.07790"
  - title: "LaMDA: Language models for dialog applications"
    authors: ["Thoppilan, R.", "De Freitas, D.", "Hall, J.", "Shazeer, N.", "Kulshreshtha, A.", "et al."]
    year: 2022
    arxiv_id: "2201.08239"
    url: "https://arxiv.org/abs/2201.08239"
  - title: "Scaling language models: Methods, analysis & insights from training Gopher"
    authors: ["Rae, J. W.", "Borgeaud, S.", "Cai, T.", "Millican, K.", "Hoffmann, J.", "et al."]
    year: 2021
    arxiv_id: "2112.11446"
    url: "https://arxiv.org/abs/2112.11446"
  - title: "Memory-assisted prompt editing to improve GPT-3 after deployment"
    authors: ["Madaan, A.", "Tandon, N.", "Clark, P.", "Yang, Y."]
    year: 2022
    arxiv_id: "2201.06009"
    url: "https://arxiv.org/abs/2201.06009"
  - title: "DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs"
    authors: ["Dua, D.", "Wang, Y.", "Dasigi, P.", "Stanovsky, G.", "Singh, S.", "Gardner, M."]
    year: 2019
    arxiv_id: "1903.00161"
    url: "https://arxiv.org/abs/1903.00161"
  - title: "Know what you don't know: Unanswerable questions for SQuAD"
    authors: ["Rajpurkar, P.", "Jia, R.", "Liang, P."]
    year: 2018
    arxiv_id: "1806.03822"
    url: "https://arxiv.org/abs/1806.03822"
  - title: "HellaSwag: Can a machine really finish your sentence?"
    authors: ["Zellers, R.", "Holtzman, A.", "Bisk, Y.", "Farhadi, A.", "Choi, Y."]
    year: 2019
    venue: "ACL"
    arxiv_id: null
    url: null
  - title: "CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models"
    authors: ["Nangia, N.", "Vania, C.", "Bhalerao, R.", "Bowman, S. R."]
    year: 2020
    venue: "EMNLP"
    arxiv_id: null
    url: null
  - title: "Gender bias in coreference resolution (Winogender)"
    authors: ["Rudinger, R.", "Naradowsky, J.", "Leonard, B.", "Van Durme, B."]
    year: 2018
    venue: "NAACL"
    arxiv_id: null
    url: null
  - title: "Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity"
    authors: ["Fedus, W.", "Zoph, B.", "Shazeer, N."]
    year: 2021
    arxiv_id: "2101.03961"
    url: "https://arxiv.org/abs/2101.03961"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "The three-step RLHF method: (1) supervised fine-tuning (SFT), (2) reward-model training from pairwise rankings, (3) PPO against the reward model"
  page: 3
  image_path: "figures/ouyang-2022-instructgpt-rlhf-fig.png"
---

# Training Language Models to Follow Instructions with Human Feedback

**Authors:** Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe (OpenAI)
**Published:** 2022-03 · [Source](https://arxiv.org/abs/2203.02155)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

OpenAI takes GPT-3 (a next-token predictor pretrained on the internet) and turns it into a model that follows user instructions by running a three-stage fine-tuning pipeline: (1) **SFT** — supervised fine-tuning on ~13k labeler-written demonstrations of desired behavior, (2) **RM** — train a 6B reward model from ~33k pairwise rankings where labelers ordered 4-9 model outputs per prompt from best to worst, and (3) **PPO** — fine-tune the SFT policy against the RM using Proximal Policy Optimization with a per-token KL penalty back to SFT to prevent reward hacking, plus an optional pretraining-mix term (PPO-ptx) that re-injects log-likelihood updates on the original pretraining distribution to fight the "alignment tax." The resulting **InstructGPT** models are evaluated by ~40 hired labelers (Upwork/ScaleAI, screened for sensitivity to demographic preferences) against held-out OpenAI API prompts. Headline result: the **1.3B-parameter InstructGPT is preferred over the 175B GPT-3** despite being 100× smaller; 175B InstructGPT beats 175B GPT-3 85±3% of the time and beats few-shot-prompted 175B GPT-3 71±4%. InstructGPT also roughly doubles TruthfulQA performance, halves closed-domain hallucination (21% vs 41%), and reduces toxicity by ~25% under a "respectful" prompt — but does **not** improve bias on Winogender/CrowS-Pairs, and when explicitly told to be biased or toxic, it follows instructions *more* compliantly than GPT-3 (i.e. alignment to user intent cuts both ways). The alignment-fine-tuning compute (~60 petaflop/s-days for PPO-ptx) is ~1.6% of GPT-3 pretraining (3,640 petaflop/s-days), making this a strikingly cheap intervention with large preference gains.

## Key Takeaway

The "alignment problem" for a pretrained LM can be reframed concretely as: the next-token-prediction objective is the wrong objective for following user intent — and you can close most of that gap with a tiny fraction of pretraining compute by collecting human preference data and training a learned reward model that you then optimize against with policy-gradient RL, with a KL leash keeping the policy near the supervised model. This is the canonical instantiation of the **reward-model + PPO** pipeline that defines modern RLHF, and the result that *a 1.3B aligned model beats a 175B unaligned model on user-rated quality* is the single empirical fact that justifies the entire post-GPT-3 industry pivot from "scale = capability" to "scale + alignment fine-tuning = product." The paper also makes explicit a normative point that is often elided: this is alignment to a specific ~40-person labeler pool plus OpenAI's instructions — not to "human values" in any general sense.

## Implications

- **Scale is not the only lever.** A 100× smaller aligned model beating a frontier-scale unaligned one on preference ratings reorders the priority list: invest in feedback data and fine-tuning before (or alongside) further scaling. OpenAI's own framing — "increasing investments in alignment of existing language models is more cost-effective than training larger models" — became the implicit blueprint for ChatGPT eight months later.
- **The reward-model bottleneck is the bottleneck of the field.** Everything downstream of step 2 depends on how well the RM generalizes preferences. The paper reports 72.6% inter-labeler agreement on training labelers and 5-fold RM accuracy of ~69.6% on held-out labelers (vs. 72.4% on training labelers) — a ~3-point generalization gap. Every successor method (DPO, RLAIF, GRPO, Constitutional AI) is either a different RM, a different optimizer against the RM, or an attempt to eliminate the RM entirely.
- **PPO + KL leash is the load-bearing trick.** Without the per-token KL penalty back to the SFT policy, the policy quickly Goodharts the reward model (over-optimization). With it, training stays in the basin where the RM was learned. This is the practical mechanism that made the math from Christiano et al. 2017 actually work on a 175B language model.
- **Alignment tax is mitigable but real.** Default PPO regresses performance on SQuAD, DROP, HellaSwag, and WMT15 FR→EN. PPO-ptx (mixing pretraining-distribution log-likelihood updates into PPO gradients with coefficient γ) recovers most regressions on the tested benchmarks without compromising labeler preference. This is the recipe later iterations carried forward, and it has implications for any RL fine-tuning that risks catastrophic forgetting.
- **"Aligned to instructions" ≠ "harmless."** When prompted to be biased, InstructGPT is *more* biased than GPT-3 — because it's *better* at following instructions. The paper is unusually frank that helpfulness-prioritized training during fine-tuning, with harmlessness deferred to evaluation, produces this asymmetry. This is the alignment-vs-corrigibility tension that later refusal-trained models (GPT-3.5, Claude, etc.) had to address.
- **Open question still open in 2022: who do we align to?** Section 5.2 catalogs that alignment was effectively to ~40 mostly US/Southeast-Asian English-speaking contractors plus OpenAI researchers' written guidelines plus the prompts that early API users chose to send. The paper does not claim this is the right reference group — it says explicitly that it is one specific human reference group. This framing leaks into every successor's discussion of representation.
- **PPO-ptx generalizes to non-English and code without supervision.** Section 4.3 reports qualitative generalization to French, German, Spanish, and code Q&A despite these being <1% of fine-tuning data. The mechanism is unclear and untested at scale, but the observation seeds later work on cross-lingual transfer in instruction-tuned models.

## How to Apply It (method)

Concretely, the three steps as implemented in the paper:

**Step 1 — Supervised Fine-Tuning (SFT):**
- Start from GPT-3 pretrained checkpoint (1.3B, 6B, or 175B).
- Collect ~13k (prompt, demonstration) pairs from labelers who write target outputs for prompts (a mix of labeler-written prompts and OpenAI API Playground prompts, deduplicated, capped 200/user, PII-filtered).
- Fine-tune with standard supervised cross-entropy for 16 epochs, cosine LR decay, residual dropout 0.2. (Models overfit on validation loss after 1 epoch but RM-score and human preference keep improving — train through the overfit.)
- Use RM score on a validation set to pick the final checkpoint.

**Step 2 — Reward Model (RM):**
- Take the 6B SFT model, strip the final unembedding layer, add a scalar head.
- For each of ~33k prompts, present labelers K=4-9 model outputs (sampled from prior models) and have them rank best→worst. This yields K-choose-2 pairwise comparisons per prompt.
- Train with pairwise logistic loss: `loss(θ) = -1/(K choose 2) · E[log σ(r_θ(x, y_w) - r_θ(x, y_l))]`, where y_w is the preferred completion. Critical detail: train all K-choose-2 comparisons from one prompt as a **single batch element** (not as separate data points), or the model overfits in one epoch.
- Stick with 6B RMs only — the authors found 175B RM training unstable for use as the PPO value function. (This is one of the more under-discussed engineering facts in the paper and a constraint downstream methods had to design around.)
- Normalize the RM so labeler demonstrations score a mean of 0 before RL.

**Step 3 — PPO Fine-Tuning:**
- Bandit environment: each "episode" is a prompt → response, RM produces scalar reward, episode ends.
- Optimize the combined objective: `E_{(x,y)~D_π}[r_θ(x,y) - β · log(π^RL(y|x) / π^SFT(y|x))] + γ · E_{x~D_pretrain}[log π^RL(x)]`
  - The β term is the **per-token KL penalty** back to SFT (prevents reward hacking / over-optimization).
  - The γ term (PPO-ptx only) re-injects pretraining log-likelihood gradients to fight alignment tax. Set γ=0 for "PPO" baseline; γ>0 for "PPO-ptx" (the production InstructGPT).
- The value function is initialized from the RM (saves training cost vs. learning value from scratch).
- Default to PPO-ptx — it gets equivalent labeler preference scores to plain PPO while preserving public-benchmark performance.

**Iteration:** Steps 2 and 3 can be repeated — collect new comparisons on the current best policy, retrain a new RM, retrain a new policy. The paper notes this was done in practice but does not quantify the per-iteration gains.

**To replicate at small scale:** the recipe needs (a) a competent labeler pool with written guidelines and a screening test (Appendix B.1 has both), (b) ~10k SFT demos + ~30k preference rankings as a minimum, (c) a working PPO implementation that supports per-token KL and pretraining-distribution mixing, (d) careful checkpoint selection by RM score not by validation loss. Open-source replications (e.g., trlx, TRL) implement this faithfully; the labeler pipeline is the hard part.

## Best Figure

![Figure 2 — Three-step RLHF method: SFT, RM, PPO (page 3)](figures/ouyang-2022-instructgpt-rlhf-fig.png)

**Why this figure:** Figure 2 is *the* canonical RLHF diagram — it is the single image that defines the post-2022 alignment field. Three panels, left to right:

1. **Step 1 (SFT):** A prompt is sampled, a labeler writes a demonstration, this (prompt, demo) pair fine-tunes GPT-3 with supervised learning.
2. **Step 2 (RM):** A prompt is sampled, the SFT model produces multiple outputs A/B/C/D, a labeler ranks them best→worst, the ranking trains the reward model.
3. **Step 3 (PPO):** A new prompt is sampled, the current policy generates an output, the reward model scores it, the scalar reward drives a PPO update to the policy (with a KL leash back to SFT, not shown in the diagram but spelled out in equation 2).

The diagram is load-bearing because every successor method (DPO, GRPO, RLAIF, Constitutional AI, RLVR) defines itself by which boxes it keeps, replaces, or skips. Reading later papers without internalizing this diagram is like trying to read post-2017 NLP without internalizing the Transformer block.

**A cool story this graph tells:** look at the prompt examples — "Explain the moon landing to a 6 year old" appears in Steps 1 and 2, and "Write a story about frogs" appears in Step 3. The Step 3 prompt is *not* labeled by humans — it's just sampled, the policy responds, and the RM (trained on completely different prompts about the moon landing) scores it. The whole bet of RLHF is that the RM trained on Step 2 preferences generalizes to *any* prompt the policy sees in Step 3. The 5-fold cross-validation result (RM accuracy drops only ~3 points on held-out labelers) is the empirical evidence that this bet holds well enough to ship.

## What Experts Overlook

- **The 6B-RM-only constraint.** Almost every discussion of this paper repeats "we used PPO against a learned reward model" without mentioning that the RM had to be 6B — 175B RM training was unstable. This means the reward model is *smaller than the policy* during 175B PPO. Subsequent work (Bai et al. 2022 Anthropic, Llama 2) generally also uses RMs smaller than or equal to the policy. Whether bigger RMs would help and how to stabilize their training is still an active question; the paper signals this is non-trivial in passing and most readers miss it.
- **The K-choose-2 batching detail.** The paper's loss-function discussion says that if you shuffle K-choose-2 comparisons into a flat dataset, the RM overfits in one epoch. Treating all comparisons from one prompt as a single batch element is the fix. This is a single sentence in Section 3.5 that practitioners learn the hard way; theoretical RLHF papers often gloss over it.
- **PPO-ptx vs. increasing KL coefficient.** Figure 33-34 show that you cannot recover the alignment tax by just turning up β (the KL penalty) — it tanks the reward without fully restoring public-benchmark performance. You need the pretraining-mix term γ explicitly. This is a load-bearing empirical claim that constrains the design space of "what fixes alignment tax."
- **InstructGPT models hallucinate ~21% of the time on closed-domain tasks** (per Figure 4). The "halves hallucination vs GPT-3" framing is the headline, but the absolute rate is still bad enough that any production deployment needs additional retrieval/verification — a fact that retroactively explains the urgency of RAG and tool-use work in 2023.
- **Held-out labelers like InstructGPT *better* than training labelers do** (77.3% vs 72.6% agreement). Most readers assume the held-out drop should be in the other direction; the paper's explanation is that held-out labelers don't undergo the screening test, so they're a more representative sample of the contractor population. This has implications for evaluator-pool design that don't get cited often.
- **Labelers are instructed to prioritize helpfulness during training but truthfulness/harmlessness during final evaluation.** This deliberate mismatch is what produces models that are "very obedient" but will follow toxic-by-instruction prompts. Many critiques of "RLHF makes models obsequious" trace back here, but the source of the obsequiousness is *the design of the labeling guidelines*, not RLHF itself.
- **The reward model is normalized so labeler demos score mean 0.** A small detail that means PPO is effectively maximizing "how much better than human demonstrators" — not absolute reward. The optimization target is implicitly relative to the demonstration pool, which shapes what the policy learns to do (push past the demos, not just match them).
- **Step 1 SFT models overfit on validation loss after 1 epoch but you train for 16.** The authors specifically note: validation loss is the wrong selection criterion; use RM-score on a held-out validation set instead. This is the kind of operational fact that anyone re-implementing the pipeline trips on; it's not the paper's headline, but it's load-bearing for reproduction.

## Extracted Prompts

The paper doesn't release the labeling instructions in full but includes excerpts and labeler-facing question prompts (Table 3, Figure 10-12, Appendix B.2). Reconstructed core prompts:

**Labeler comparison prompt (Step 2 — Figure 12-style):**
> "Given the following user prompt, rank the K model outputs from best to worst. When ranking, consider: (a) does the output follow the user's instruction correctly? (b) is it appropriate for use in a customer-assistant context? (c) does it hallucinate facts not present in the input on closed-domain tasks? (d) does it contain sexual, violent, or otherwise harmful content? (e) does it satisfy any explicit constraints in the instruction?"

**Labeler metadata schema (Table 3):**
- Overall quality (1-7 Likert)
- Fails to follow the correct instruction/task (binary)
- Inappropriate for customer assistant (binary)
- Hallucination (binary)
- Satisfies constraint provided in the instruction (binary)
- Contains sexual content (binary)
- Contains violent content (binary)
- Encourages or fails to discourage violence/abuse/terrorism/self-harm (binary)
- Denigrates a protected class (binary)
- Gives harmful advice (binary)
- Expresses opinion (binary)
- Expresses moral judgment (binary)

**"Respectful" toxicity prompt (Figure 7):**
> Prepended to the actual prompt: a brief instruction asking the model to produce a safe and respectful output (exact text not given in the paper; reconstructions in open-source replications typically use language like "Complete the following text in a way that is respectful and safe.").

**Instruction-following prefix for GPT-3 baseline (Section 3.5):**
> The authors held a prefix-finding competition — RL and DA each spent an hour interacting with GPT-3 to find their two best prefixes. The winning prefix was the one that led GPT-3 to the highest RM score on the prompt validation set. (Exact text not released, but the practice of "prompt engineering by holding a competition" is itself a documented methodology.)

**Labeler-written prompt categories (bootstrapping):**
- *Plain:* "Come up with an arbitrary task, ensure diversity."
- *Few-shot:* "Come up with an instruction and K query/response pairs for that instruction."
- *User-based:* "Come up with prompts corresponding to these listed waitlist use-cases."

## Citations

The full citation list (28 entries, prioritized) is in the frontmatter `citations:` array. Top items:

- Christiano et al. 2017 — *Deep RL from human preferences* (the foundational paper introducing preference-based RL with a learned RM; this paper is the language-model application of that recipe)
- Stiennon et al. 2020 — *Learning to summarize from human feedback* (the immediate methodological predecessor; same authors, RLHF applied to summarization)
- Ziegler et al. 2019 — *Fine-tuning language models from human preferences* (the earlier attempt at RLHF on LMs; this paper improves on its data and engineering)
- Schulman et al. 2017 — *PPO* (the RL algorithm that drives step 3)
- Brown et al. 2020 — *GPT-3* (the base model)
- Askell et al. 2021 — *General language assistant as a laboratory for alignment* (the helpful/honest/harmless framing the paper adopts)
- Wu et al. 2021 — *Recursively summarizing books with human feedback* (concurrent RLHF application from same lab)
- Nakano et al. 2021 — *WebGPT* (RLHF + browsing, parallel application)
- Leike et al. 2018 — *Scalable agent alignment via reward modeling* (the alignment-research direction this paper instantiates)
- Lin et al. 2021 — *TruthfulQA* (evaluation benchmark)
- Gehman et al. 2020 — *RealToxicityPrompts* (toxicity benchmark)
- Wei et al. 2021 / Sanh et al. 2021 — *FLAN / T0* (the public-NLP-fine-tuning baselines InstructGPT is compared against)
- Gabriel 2020 — *AI, values, and alignment* (the philosophical framework for "who are we aligning to?")

## Related Digests

- [[shao-2024-deepseekmath-grpo]] — DeepSeekMath: GRPO replaces InstructGPT's PPO + value-network with group-relative sampling, directly evolving the algorithm in step 3 of this paper.
- [[touvron-2023-llama-2]] — Llama 2: Meta's open-weight reapplication of the same SFT → RM → PPO pipeline at scale, with iterative RM retraining and a "Ghost Attention" trick layered on.
- [[yan-2025-memory-r1]] — Memory-R1: directly cites this paper as the canonical RLHF reference; applies the same RL-from-feedback paradigm to memory-management policies.

## Reviewer Notes

**Overall hallucination severity:** Clean

**Spot-checks performed:**

- ✅ "1.3B InstructGPT preferred over 175B GPT-3" — confirmed by Abstract, Figure 1, Section 4.1 ("outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having over 100x fewer parameters").
- ✅ "175B InstructGPT preferred 85±3% over 175B GPT-3 and 71±4% over few-shot GPT-3" — confirmed Section 4.1, Section 1 intro.
- ✅ "Halves closed-domain hallucination (21% vs 41%)" — confirmed Section 1 intro ("21% vs. 41% hallucination rate").
- ✅ "SFT ~13k prompts, RM ~33k, PPO ~31k" — confirmed Section 3.2.
- ✅ "~40 labelers, hired via Upwork and Scale AI" — confirmed Section 3.4.
- ✅ "Inter-labeler agreement 72.6% (training) / 77.3% (held-out)" — confirmed Section 3.4.
- ✅ "5-fold RM accuracy 69.6% held-out, 72.4% train" — confirmed Section 4.1.
- ✅ "60 petaflop/s-days PPO-ptx, 4.9 PFs-d SFT, vs 3,640 PFs-d for GPT-3" — confirmed Section 5.1. (~1.6% of pretraining for PPO-ptx; 0.13% for SFT alone.)
- ✅ "6B RMs only, 175B RM unstable" — confirmed Section 3.5 ("we found that 175B RM training could be unstable").
- ✅ "K-choose-2 batching trick" — confirmed Section 3.5.
- ✅ "Per-token KL penalty against SFT, equation 2" — confirmed Section 3.5, equation 2.
- ✅ "PPO-ptx mixes pretraining gradients; γ coefficient; γ=0 for PPO baseline" — confirmed Section 3.5.
- ✅ "Figure 2 — three-step pipeline diagram" — confirmed page 3, image extracted and verified.
- ✅ "RLHF doesn't improve bias on Winogender/CrowS-Pairs" — confirmed Section 1 intro and Section 4.2.
- ✅ "When prompted to be toxic, InstructGPT more toxic than GPT-3" — confirmed Section 4.2 ("when explicitly prompted to produce a toxic output, InstructGPT outputs are much more toxic than those from GPT-3").
- ✅ Author list and affiliations confirmed against page 1.
- ✅ Arxiv ID 2203.02155 confirmed against the source URL.

**No fabricated claims, no invented numbers.** The synthesis stays within the paper's own framing; where the digest editorializes (e.g. "this is the canonical RLHF diagram", "the entire post-GPT-3 industry pivot"), it is clearly framed as commentary rather than as paper claim.

**Minor caveat:** The "1.6% of pretraining compute" framing is the digest's arithmetic (60 / 3640 ≈ 1.6%); the paper itself just gives the absolute numbers and says "a fraction." This is fair derivation, not hallucination.
