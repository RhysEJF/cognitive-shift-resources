---
corpus: agentic-memory
kind: paper-digest
slug: shen-2023-icl-not-gd
title: "Do pretrained Transformers Learn In-Context by Gradient Descent?"
authors:
  - "Shen, Lingfeng"
  - "Mishra, Aayush"
  - "Khashabi, Daniel"
year: 2023
publication_date: "2023-10"
venue: "ICML 2024 (PMLR 235); arXiv preprint"
source_url: "https://arxiv.org/abs/2310.08540"
doi: null
arxiv_id: "2310.08540"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Real-world pretrained LLMs do not perform in-context learning by implicit gradient descent: the GD-equivalence proofs (von Oswald, Akyürek, Dai) rely on hand-constructed >99.99%-sparse weights that LLaMa-7B and GPT-J empirically violate (sparsity ratio measured <60% across WK/WQ/WV layers), on models trained with an ICL-specific objective rather than next-token CLM, and on the false assumption of order-stability — ICL's output-distribution standard deviation across 10 demo permutations is ~3-5x higher than GD/SGD/Adam, falsifying any equivalence to an order-stable optimizer."
topics:
  - in-context-learning
  - gradient-descent-equivalence
  - transformer-mechanism
  - order-sensitivity
  - implicit-finetuning
  - llama-7b
  - icl-objective
tags:
  - paper
  - counter-thesis
  - mechanism-gap
  - memory-architect
  - icml-2024
entities:
  - shen-lingfeng
  - mishra-aayush
  - khashabi-daniel
  - von-oswald-johannes
  - akyurek-ekin
  - dai-damai
related_digests:
  - vassilyev-2026-rcl
  - brown-2020-gpt3-few-shot
  - mao-2026-agent-memory-circuits
  - elhage-2022-toy-models-superposition
citations:
  - title: "Transformers learn to implement preconditioned gradient descent for in-context learning"
    authors: ["Ahn, K.", "Cheng, X.", "Daneshmand, H.", "Sra, S."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: "https://arxiv.org/abs/2306.00297"
    arxiv_id: "2306.00297"
  - title: "What learning algorithm is in-context learning? Investigations with linear models"
    authors: ["Akyürek, E.", "Schuurmans, D.", "Andreas, J.", "et al."]
    year: 2022
    venue: "ICLR"
    doi: null
    url: "https://arxiv.org/abs/2211.15661"
    arxiv_id: "2211.15661"
  - title: "GPT-Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow"
    authors: ["Black, S.", "Gao, L.", "Wang, P.", "et al."]
    year: 2021
    venue: "Zenodo"
    doi: "10.5281/zenodo.5297715"
    url: "https://doi.org/10.5281/zenodo.5297715"
    arxiv_id: null
  - title: "Language Models are Few-Shot Learners"
    authors: ["Brown, T.", "Mann, B.", "Ryder, N.", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: "https://arxiv.org/abs/2005.14165"
    arxiv_id: "2005.14165"
  - title: "Data distributional properties drive emergent in-context learning in transformers"
    authors: ["Chan, S.", "Santoro, A.", "Lampinen, A.", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: "https://arxiv.org/abs/2205.05055"
    arxiv_id: "2205.05055"
  - title: "Tighter bounds on the expressivity of transformer encoders"
    authors: ["Chiang, D.", "Cholak, P.", "Pillay, A."]
    year: 2023
    venue: "ICML"
    doi: null
    url: "https://arxiv.org/abs/2301.10743"
    arxiv_id: "2301.10743"
  - title: "The PASCAL Recognising Textual Entailment Challenge"
    authors: ["Dagan, I.", "Glickman, O.", "Magnini, B."]
    year: 2005
    venue: "Machine Learning Challenges Workshop"
    doi: null
    url: "https://link.springer.com/chapter/10.1007/11736790_9"
    arxiv_id: null
  - title: "Why can GPT learn in-context? Language models secretly perform gradient descent as meta optimizers"
    authors: ["Dai, D.", "Sun, Y.", "Dong, L.", "et al."]
    year: 2023
    venue: "ACL Findings"
    doi: null
    url: "https://arxiv.org/abs/2212.10559"
    arxiv_id: "2212.10559"
  - title: "The CommitmentBank: Investigating projection in naturally occurring discourse"
    authors: ["De Marneffe, M.-C.", "Simons, M.", "Tonhauser, J."]
    year: 2019
    venue: "Sinn und Bedeutung"
    doi: null
    url: "https://ojs.ub.uni-konstanz.de/sub/index.php/sub/article/view/601"
    arxiv_id: null
  - title: "What can transformers learn in-context? A case study of simple function classes"
    authors: ["Garg, S.", "Tsipras, D.", "Liang, P. S.", "Valiant, G."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: "https://arxiv.org/abs/2208.01066"
    arxiv_id: "2208.01066"
  - title: "A theory of emergent in-context learning as implicit structure induction"
    authors: ["Hahn, M.", "Goyal, N."]
    year: 2023
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2303.07971"
    arxiv_id: "2303.07971"
  - title: "Understanding in-context learning via supportive pretraining data"
    authors: ["Han, X.", "Simig, D.", "Mihaylov, T.", "et al."]
    year: 2023
    venue: "ACL"
    doi: null
    url: "https://arxiv.org/abs/2306.15091"
    arxiv_id: "2306.15091"
  - title: "Large language models are zero-shot reasoners"
    authors: ["Kojima, T.", "Gu, S. S.", "Reid, M.", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: "https://arxiv.org/abs/2205.11916"
    arxiv_id: "2205.11916"
  - title: "The closeness of in-context learning and weight shifting for softmax regression"
    authors: ["Li, S.", "Song, Z.", "Xia, Y.", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2304.13276"
    arxiv_id: "2304.13276"
  - title: "Dual operating modes of in-context learning"
    authors: ["Lin, Z.", "Lee, K."]
    year: 2024
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2402.18819"
    arxiv_id: "2402.18819"
  - title: "Transformers learn shortcuts to automata"
    authors: ["Liu, B.", "Ash, J. T.", "Goel, S.", "et al."]
    year: 2022
    venue: "ICLR"
    doi: null
    url: "https://arxiv.org/abs/2210.10749"
    arxiv_id: "2210.10749"
  - title: "Generating wikipedia by summarizing long sequences"
    authors: ["Liu, P. J.", "Saleh, M.", "Pot, E.", "et al."]
    year: 2018
    venue: "ICLR"
    doi: null
    url: "https://arxiv.org/abs/1801.10198"
    arxiv_id: "1801.10198"
  - title: "Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity"
    authors: ["Lu, Y.", "Bartolo, M.", "Moore, A.", "et al."]
    year: 2022
    venue: "ACL"
    doi: null
    url: "https://arxiv.org/pdf/2104.08786.pdf"
    arxiv_id: "2104.08786"
  - title: "Saturated transformers are constant-depth threshold circuits"
    authors: ["Merrill, W.", "Sabharwal, A.", "Smith, N. A."]
    year: 2022
    venue: "TACL"
    doi: null
    url: "https://arxiv.org/abs/2106.16213"
    arxiv_id: "2106.16213"
  - title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    authors: ["Min, S.", "Lyu, X.", "Holtzman, A.", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: null
    url: "https://arxiv.org/abs/2202.12837"
    arxiv_id: "2202.12837"
  - title: "Reframing instructional prompts to GPTk's language"
    authors: ["Mishra, S.", "Khashabi, D.", "Baral, C.", "et al."]
    year: 2022
    venue: "ACL Findings"
    doi: null
    url: "https://arxiv.org/abs/2109.07830"
    arxiv_id: "2109.07830"
  - title: "In-context learning and induction heads"
    authors: ["Olsson, C.", "Elhage, N.", "Nanda, N.", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2209.11895"
    arxiv_id: "2209.11895"
  - title: "What in-context learning \"learns\" in-context: Disentangling task recognition and task learning"
    authors: ["Pan, J.", "Gao, T.", "Chen, H.", "Chen, D."]
    year: 2023
    venue: "ACL Findings"
    doi: null
    url: "https://aclanthology.org/2023.findings-acl.527"
    arxiv_id: null
  - title: "True few-shot learning with language models"
    authors: ["Perez, E.", "Kiela, D.", "Cho, K."]
    year: 2021
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models are unsupervised multitask learners"
    authors: ["Radford, A.", "Wu, J.", "Child, R.", "et al."]
    year: 2019
    venue: "OpenAI blog"
    doi: null
    url: "https://openai.com/blog/better-language-models/"
    arxiv_id: null
  - title: "Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression"
    authors: ["Raventós, A.", "Paul, M.", "Chen, F.", "Ganguli, S."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Impact of pretraining term frequencies on few-shot reasoning"
    authors: ["Razeghi, Y.", "Logan IV, R. L.", "Gardner, M.", "Singh, S."]
    year: 2022
    venue: "ACL Findings"
    doi: null
    url: "https://arxiv.org/abs/2202.07206"
    arxiv_id: "2202.07206"
  - title: "Linear transformers are secretly fast weight programmers"
    authors: ["Schlag, I.", "Irie, K.", "Schmidhuber, J."]
    year: 2021
    venue: "ICML"
    doi: null
    url: "http://proceedings.mlr.press/v139/schlag21a.html"
    arxiv_id: null
  - title: "Flatness-aware prompt selection improves accuracy and sample efficiency"
    authors: ["Shen, L.", "Tan, W.", "Zheng, B.", "Khashabi, D."]
    year: 2023
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2305.10713"
    arxiv_id: "2305.10713"
  - title: "On the effect of pretraining corpora on in-context learning by a large-scale language model"
    authors: ["Shin, S.", "Lee, S. W.", "Ahn, H.", "et al."]
    year: 2022
    venue: "NAACL"
    doi: null
    url: "https://arxiv.org/abs/2204.13509"
    arxiv_id: "2204.13509"
  - title: "Recursive deep models for semantic compositionality over a sentiment treebank"
    authors: ["Socher, R.", "Perelygin, A.", "Wu, J.", "et al."]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: "https://aclanthology.org/D13-1170.pdf"
    arxiv_id: null
  - title: "Beyond the imitation game: Quantifying and extrapolating the capabilities of language models"
    authors: ["Srivastava, A.", "Rastogi, A.", "Rao, A.", "et al."]
    year: 2023
    venue: "TMLR"
    doi: null
    url: "https://arxiv.org/abs/2206.04615"
    arxiv_id: "2206.04615"
  - title: "LLaMA: Open and efficient foundation language models"
    authors: ["Touvron, H.", "Lavril, T.", "Izacard, G.", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2302.13971"
    arxiv_id: "2302.13971"
  - title: "Attention is All You Need"
    authors: ["Vaswani, A.", "Shazeer, N.", "Parmar, N.", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: "https://arxiv.org/abs/1706.03762"
    arxiv_id: "1706.03762"
  - title: "Transformers learn in-context by gradient descent"
    authors: ["von Oswald, J.", "Niklasson, E.", "Randazzo, E.", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: "https://arxiv.org/abs/2212.07677"
    arxiv_id: "2212.07677"
  - title: "GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model"
    authors: ["Wang, B.", "Komatsuzaki, A."]
    year: 2021
    venue: "GitHub"
    doi: null
    url: "https://github.com/kingoflolz/mesh-transformer-jax"
    arxiv_id: null
  - title: "Self-Instruct: Aligning Language Model with Self Generated Instructions"
    authors: ["Wang, Y.", "Kordi, Y.", "Mishra, S.", "et al."]
    year: 2023
    venue: "ACL"
    doi: null
    url: "https://arxiv.org/abs/2212.10560"
    arxiv_id: "2212.10560"
  - title: "Finetuned language models are zero-shot learners"
    authors: ["Wei, J.", "Bosma, M.", "Zhao, V.", "et al."]
    year: 2021
    venue: "ICLR"
    doi: null
    url: "https://arxiv.org/abs/2109.01652"
    arxiv_id: "2109.01652"
  - title: "Emergent abilities of large language models"
    authors: ["Wei, J.", "Tay, Y.", "Bommasani, R.", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2206.07682"
    arxiv_id: "2206.07682"
  - title: "The learnability of in-context learning"
    authors: ["Wies, N.", "Levine, Y.", "Shashua, A."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: "https://arxiv.org/abs/2303.07895"
    arxiv_id: "2303.07895"
  - title: "An explanation of in-context learning as implicit Bayesian inference"
    authors: ["Xie, S. M.", "Raghunathan, A.", "Liang, P.", "Ma, T."]
    year: 2021
    venue: "ICLR"
    doi: null
    url: "https://arxiv.org/abs/2111.02080"
    arxiv_id: "2111.02080"
  - title: "Large language models as optimizers"
    authors: ["Yang, C.", "Wang, X.", "Lu, Y.", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: "https://arxiv.org/abs/2309.03409"
    arxiv_id: "2309.03409"
  - title: "Trained transformers learn linear models in-context"
    authors: ["Zhang, R.", "Frei, S.", "Bartlett, P. L."]
    year: 2023
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2306.09927"
    arxiv_id: "2306.09927"
  - title: "Character-level convolutional networks for text classification"
    authors: ["Zhang, X.", "Zhao, J.", "LeCun, Y."]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Calibrate before use: Improving few-shot performance of language models"
    authors: ["Zhao, Z.", "Wallace, E.", "Feng, S.", "et al."]
    year: 2021
    venue: "ICML"
    doi: null
    url: "http://proceedings.mlr.press/v139/zhao21c/zhao21c.pdf"
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 5
  title: "Comparison of ICL and GD/GD-hat on three metrics for the AGNews dataset (with 4 ICL demos)"
  page: 7
  image_path: "figures/shen-2023-icl-not-gd-fig.png"
---

# Do pretrained Transformers Learn In-Context by Gradient Descent?

**Authors:** Lingfeng Shen, Aayush Mishra, Daniel Khashabi (Johns Hopkins University)
**Published:** 2023-10 (ICML 2024 / PMLR 235; v5 2024-06) · [Source](https://arxiv.org/abs/2310.08540)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Shen, Mishra, and Khashabi attack the increasingly popular thesis (Akyürek 2022, von Oswald 2023, Dai 2023) that in-context learning (ICL) in real LLMs *is* implicit gradient descent (GD) on an inner sub-model, and show the equivalence collapses under three concrete tests on LLaMa-7B and GPT-J. (1) **Setup mismatch:** the GD-equivalence proofs require models trained with an explicit ICL objective on a restricted task family (call it ICL-hat); real LLMs are trained with the next-token CLM objective on natural text and there is no path from one space of models to the other. (2) **Sparsity mismatch:** the hand-constructed weight matrices (WK, WQ, WV, P) that make a forward pass equal a GD step require ≥99.99% sparsity in WK/WQ and ~75% in WV; measured at multiple thresholds in LLaMa-7B and GPT-J the sparsity ratio stays below ~60% across all layers (Figure 2). They also show (Figure 3) that ICL accuracy on AGNews is approximately constant across GPT-J checkpoints from 310k→380k steps even though average weight changes grow steadily — falsifying the "single special weight configuration" precondition. (3) **Order-sensitivity mismatch:** they prove a theorem — any algorithm equivalent to ICL must share its order-sensitivity profile — and empirically show ICL output-distribution standard deviation across 10 random demo permutations is ~3-5x higher than GD, SGD, or Adam at every epoch up to 200 (Figure 4); the gap holds across LLaMa-7B, Qwen-7B, and GPT-J and across batch sizes 1, 2, 4. On the three relative metrics (Accuracy, Token Overlap @ K=10, Overlap Cosine Similarity) ICL vs GD/GD-hat (whole-model, mid-layer-WV, deep-layer-WV) shows a persistent gap on AGNews/CB/SST-2/RTE with 1/2/4/8 demos — and GD only catches ICL accuracy with 512 demos (vs 8 for ICL: AGNews 0.42→0.69, CB 0.39→0.72, SST-2 0.49→0.75, RTE 0.36→0.65). The most actionable consequence: when your memory layer "remembers" via context injection, do not assume the model is doing the same optimization a fine-tune would — they modify the output distribution measurably differently, so cache-warming intuitions ported from GD will silently mislead.

## Key Takeaway

ICL is not implicit gradient descent in pretrained LLMs. The order-sensitivity gap is the load-bearing argument: any algorithm equivalent to ICL must respond identically to demonstration reordering (their Theorem 1), but ICL's standard deviation over 10 demo orders is roughly 3-5x that of GD/SGD/Adam at every epoch — so ICL cannot be equivalent to any order-stable optimizer, including all standard GD variants. Combined with the >99.99%-sparsity precondition that real LLMs empirically violate and the fact that prior proofs train on a restricted ICL-hat objective rather than natural-text CLM, the bridge from "Transformers can simulate GD" to "real pretrained Transformers do simulate GD" simply does not hold. For memory-architecture work this means treating in-context demonstrations as a fundamentally different write/read pathway from weight updates — closer to retrieval-conditioned prior selection (consistent with Xie 2021's Bayesian-inference framing) than to implicit fine-tuning.

## Implications

- **[Encode + Aggregate] Stop treating context-window injection as "implicit fine-tuning"** [ENGRAM E, A]: The paper falsifies the equivalence that underwrites the "context = weight update" mental model used by RCL (Vassilyev 2026), Dai 2023, and most context-engineering frameworks. If your memory architecture promotes prompt-injected facts to "learned" facts on the assumption that the model has implicitly gradient-descended on them, you are conflating two mechanically distinct write paths — context-conditioning (order-sensitive, prior-selecting) and weight-update (order-stable, parameter-modifying). Build separate eviction and provenance rules for each.

- **[Retrieve] Treat demonstration ordering as a first-class retrieval parameter, not a tie-breaker** [ENGRAM R]: ICL's standard deviation over 10 permutations of 8 AGNews demos on LLaMa-7B is ~0.10-0.15 vs GD's ~0.01-0.02 (Figure 4) — about an order of magnitude. Memory layers that retrieve top-k chunks and concatenate them in arbitrary score order will get systematically different model behavior than ones that pin a canonical order. Pick an order rule (e.g., chronological, score-descending, or task-tuned via Lu et al. 2022) and persist it as part of the retrieval contract.

- **[Ground] Demos are prior-selection signals, not training data** [ENGRAM G]: Because GD only catches ICL accuracy with ~64x more demonstrations (8 → 512 demos to match ICL on AGNews/CB/SST-2/RTE — their Table 1), ICL is doing something other than "learn from examples." Pan et al. 2023 (cited approvingly) frames it as task-recognition + prior-recall. Provenance should attribute ICL outputs to "model prior conditioned on demo k" rather than "model learned from demos" — otherwise your trust layer overcredits the few-shot examples for accuracy that came from pretraining.

- **[Encode] CLM-pretrained ≠ ICL-pretrained — do not transfer findings between regimes** [ENGRAM E]: The paper isolates a clean methodology bug across the GD-equivalence literature: every constructive proof (Akyürek 2022, von Oswald 2023, Garg 2022) trains models on the ICL objective (arg-min over `L(f(x), M(x1°f(x1)°...°xi))`), which embeds an inductive bias for "x-y-x-y-... + query" structure. Real LLMs are trained on next-token prediction over natural text. If you're using a small-task simulator to probe your memory architecture, never assume the dynamics transfer to LLaMa/Qwen/GPT scales without re-running the test there.

- **[Maintain] Weight-sparsity is a falsifier — measure it before claiming GD-emergence** [ENGRAM M]: They give a concrete falsification recipe (§3.2 + Figure 2): for any claim that "GD lives in sub-matrix X of weights," measure the sparsity ratio of X at multiple thresholds δ ∈ [10², 10⁶], averaged across layers. Real LLaMa-7B WK/WQ/WV all stay below ~60% at any sensible δ — far from the 99.99% required by von Oswald's construction. Bake this measurement into your maintenance pass on any LoRA/PEFT memory adapter that claims to encode a learned "implicit optimizer" — if it's not that sparse, it isn't doing what the theory says it is.

- **[Aggregate] The "comparable performance with more demos" argument is a trap** [ENGRAM A]: It's tempting to say "GD eventually matches ICL with enough demos, so they're equivalent in the limit." The paper explicitly rebuts this (Table 1 + §5.2): GD needs 64x more demos to approach ICL's 8-demo accuracy, and even then the output *distributions* (not just argmax) diverge across all three of their metrics. Equivalence at the prediction layer is not equivalence at the mechanism layer — don't let your eval suite hide this by only measuring accuracy.

- **[Retrieve + Ground] Use Token Overlap and Overlap Cosine Similarity, not just accuracy, when comparing memory strategies** [ENGRAM R, G]: Their §5.1 metrics (Token Overlap @ K=10 between two output distributions; OCS as cosine over the intersection) are directly portable to memory-architecture eval: when comparing "context-injection vs LoRA-finetune vs retrieval-augmented" pipelines, accuracy alone collapses too much information. If two pipelines hit the same accuracy with low Token Overlap, they're solving the task with different internal representations — and that has downstream implications for stacking, hallucination behavior, and contradiction handling.

- **[Cross-dimensional] The cleanest empirical bridge to RCL's claim is the order-sensitivity test** [ENGRAM R↔A]: RCL (Vassilyev 2026) re-uses the GD analogy at the context-artifact level (reflection ↔ gradient, mutation ↔ optimizer step). The order-sensitivity test from Theorem 1 generalizes cleanly: if RCL's context-artifact mutation pipeline is truly isomorphic to GD, mutating-then-applying a fixed set of reflections in different orders should produce identical artifacts. If it doesn't (which seems likely given attention's causal masking), the GD-isomorphism is decorative, not mechanical — and you should evaluate RCL as a memory architecture on its empirical merits, not its theoretical analogy.

## How to Apply It (method)

**Scenario:** You're building the Encode + Retrieve layer of an agentic memory architecture. A teammate proposes "we can treat the LLM's context window as a fast weight-update layer — every retrieved chunk is effectively one GD step on a hidden sub-model, so we can reason about cache eviction the way we reason about gradient checkpoints." Before you spend a quarter building eviction policy on that premise, you want to falsify (or confirm) the GD-equivalence on *your* model family.

**Steps:**

1. **Pick your model and your evaluation tasks**: Choose the LLM your memory layer actually uses (e.g., LLaMa-7B, Llama-3-8B, Qwen-7B, GPT-J — pick something open-weights so you can fine-tune). Choose 3-4 simple classification tasks with clear label sets (the paper used AGNews, CB, SST-2, RTE — small N, ~4 classes each is fine). Sample a fixed test set of ~500 examples per task.

2. **Set up the three comparison conditions**: For each (model, task) pair you'll generate three sets of output distributions:
   - **ICL condition**: feed N demos in the prompt (try N=1, 2, 4, 8), record the full vocabulary-distribution output on each test input.
   - **GD condition**: take the same N demos, fine-tune the *whole* model for 200 epochs at learning rates {1e-4, 5e-4, 1e-5, 5e-5}; record outputs at every 20-epoch checkpoint, with no demos in the prompt.
   - **GD-hat condition**: same as GD but only update WV in one chosen layer (mid or deep). The paper used "WV of a single deep layer" and "WV of a single middle layer" as intuitive sub-models — pick the two you'd actually use as a memory adapter.

   Critical: when computing the GD loss use *only* the label tokens (not the prefix), to match the ICL formulation where only the output is what counts.

3. **Run the order-sensitivity test (this is the load-bearing one)**: For each (model, task, N) combination, generate 10 random permutations of the N demos. Record output distributions for all 10.
   - **For ICL**: 10 different prompts → 10 distributions per test input.
   - **For GD/GD-hat**: 10 different demo orders → 10 fine-tuned model checkpoints → 10 distributions per test input.
   Compute the Sen metric (standard deviation across the 10 distributions for each vocab dimension, then sum across V).

4. **Compute the three comparison metrics on ICL-vs-GD pairs**:

   ```
   Accuracy = (1/|Stest|) * Σ 1{y_test == argmax M(C, x_test)}    over full vocab V

   Token Overlap = (1/K) * |T_K^1 ∩ T_K^2|   with K=10, T_K = top-K tokens by prob

   OCS = Σ_{t∈O} p1(t) * p2(t)  /  sqrt( (Σ p1²) * (Σ p2²) * (K - |O|) )
         where O = T_K^1 ∩ T_K^2
   ```

   For ICL-vs-ICL: compute these between two different demo orderings (the "noise floor").
   For ICL-vs-GD and ICL-vs-GD-hat: compute these between ICL output and the GD checkpoint output at the same effective compute budget.

5. **Decide based on the gap**: If `Sen(ICL) / Sen(GD) > 3` at any reasonable epoch (the paper sees ~5x on LLaMa-7B), the GD-equivalence is falsified for your model — context-injection cannot be a fast GD update, full stop. If additionally `Token Overlap(ICL-ICL) > Token Overlap(ICL-GD)`, you have a second independent falsifier (ICL is more self-consistent across demo orders than it is consistent with any GD checkpoint). Conversely, if both gaps are small, the equivalence is at least *not falsified* on your stack and the GD intuition can guide your eviction policy.

6. **Optional sparsity check** (defensive): Measure sparsity of WK, WQ, WV averaged across layers at thresholds δ ∈ [10², 10⁶]. If max sparsity < 95% across all (layer, matrix, δ), no construction in the Akyürek/von Oswald family can be running inside your model — independent falsification of the equivalence claim.

7. **Document the verdict in your memory architecture's decision log**: Record the (model, task, N, Sen-ratio, Token-Overlap-gap, sparsity-max) tuple. This becomes a maintenance contract: if you swap base models, re-run this test before assuming the GD-vs-ICL framing still holds.

**Expected outcome:** A reproducible falsification (or, rarely, confirmation) of GD-equivalence on the specific LLM your memory layer uses, with three independent metrics and a sparsity-floor check. The deliverable is a one-page report: "On model X at task Y with N=8 demos, ICL Sen = a, GD Sen = b (ratio a/b), Token Overlap(ICL,ICL) = c vs Token Overlap(ICL,GD) = d, max sparsity = e. Verdict: context-injection IS / IS NOT equivalent to implicit GD. Eviction policy implication: <use weight-update intuitions / treat context as prior-selection only>." This becomes part of your Ground layer's provenance metadata for every retrieved chunk.

## Best Figure

![Figure 5 — Comparison of ICL and GD/GD-hat on three metrics (page 7)](figures/shen-2023-icl-not-gd-fig.png)

Image Candidates:
Figure 5 (p. 7): A 3-row × 3-column grid that visually fingerprints ICL-vs-GD divergence across Accuracy, Token Overlap, and Overlap Cosine Similarity — the paper's central empirical claim in one chart.
Figure 4 (p. 5): A single-panel time series showing ICL's order-sensitivity standard deviation sitting ~3-5x above GD/SGD/Adam at every epoch — the load-bearing falsifier in one image.
Figure 2 (p. 4): Sparsity-ratio curves for LLaMa-7B WK/WQ/WV against the 99.99%/75% theoretical thresholds, falsifying the von Oswald weight construction at a glance.

Best Image:
Figure Name: Figure 5: "Comparison of ICL and GD/GD-hat on our three metrics for the AGNews dataset (with 4 ICL demos)"
Figure Page: 7
Slide Caption: ICL and GD diverge across three orthogonal metrics — accuracy, token overlap, and cosine similarity — under whole-model, mid-layer, and deep-layer fine-tuning.
Description: Figure 5 is a 3×3 grid where rows are the three comparison metrics (Accuracy, Token Overlap @ K=10, Overlap Cosine Similarity) and columns are the three GD variants (whole-model GD, GD-hat on a single mid layer's WV, GD-hat on a single deep layer's WV). Each panel plots multiple learning-rate curves for GD (1e-3, 1e-4, 5e-3, 5e-4) against the ICL reference line, across 200 epochs of fine-tuning on AGNews with 4 ICL demos. The persistent gray gap between ICL and all GD curves across all nine panels — and the fact that ICL's two reference lines (in Token Overlap and OCS) measure ICL-against-itself with different demo orderings yet still sit higher than ICL-vs-GD — is the paper's empirical knockout: even when accuracy looks close, the output distributions are mechanically different. This matters for memory-architecture work because it shows that "matching accuracy" is a weak equivalence test; only when the full token-distribution agrees can two write pathways be called the same operation.

## What Experts Overlook

The detail most memory-architecture readers miss is the **distinction between hypothesis 1 and hypothesis 2** as stated in §1 of the paper. Hypothesis 2 — "there exist Transformer weights such that ICL-hat is algorithmically equivalent to GD" — is provable and is what the Akyürek/von Oswald/Dai papers actually establish; it's a statement about the *expressivity* of the Transformer architecture given a particular ICL-objective training regime. Hypothesis 1 — "for any Transformer from natural-text CLM pretraining and any well-defined task, ICL is equivalent to GD" — is what the field colloquially repeats as "ICL = GD" and is what every memory-architecture framework actually needs to be true to port GD intuitions over. Shen et al.'s §3 makes the case that no result in the literature, no matter how often cited, actually establishes hypothesis 1: the training distribution differs (Mc vs M), the task space differs (F-hat vs F), and the model arrived at via ICL-objective training has different inductive biases than the model arrived at via CLM training. The Figure-1 inset diagram (with arrows A, B, C between "whole model"/"sub-model" × "emergent"/"not-emergent" quadrants) is the cleanest visualization of the equivocation.

**Why it matters:** Most experts cite "ICL is implicit GD (Dai 2023, von Oswald 2023)" as if it were established for real LLMs. It isn't — what's established is that *some* artificial Transformer trained on an ICL-specific objective can be made to compute a GD step. The slippage from "can" (expressivity, hypothesis 2) to "does" (mechanism, hypothesis 1) is invisible in 90% of secondary discussions and is exactly the slippage that breaks every downstream design that assumes context-injection has fine-tune semantics.

**Example of good use:** A memory-architecture team reviewing a new paper that claims "our retrieval layer acts as a fast gradient step" should immediately ask: which hypothesis are you proving — that the architecture *can* simulate GD given the right weights (hypothesis 2, expressivity), or that it *does* under natural pretraining (hypothesis 1, mechanism)? If the paper only trains on small ICL-objective simulators (Garg-2022-style linear regression demos), it's hypothesis 2 and the eviction/grounding implications don't port to your LLaMa-3 deployment without separate empirical validation on your stack.

**Example of misapplication:** A team builds a long-term memory system whose eviction policy treats every retrieved chunk as a "stale gradient step" (decay weight inversely with steps since retrieval, just like learning-rate decay). The intuition came from "ICL = GD" papers. In practice, because ICL is actually doing prior-selection / task-recognition (Pan 2023, Xie 2021), the "decay since retrieval" policy systematically prunes chunks that are still strong prior-selection signals — performance degrades and the team blames retrieval quality when the real bug is the GD analogy at the eviction-policy layer.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- Akyürek et al. (2022) — *What learning algorithm is in-context learning? Investigations with linear models* — ICLR — [arxiv:2211.15661](https://arxiv.org/abs/2211.15661)
- von Oswald et al. (2023) — *Transformers learn in-context by gradient descent* — ICLR — [arxiv:2212.07677](https://arxiv.org/abs/2212.07677)
- Dai et al. (2023) — *Why can GPT learn in-context? Language models secretly perform gradient descent as meta optimizers* — ACL Findings — [arxiv:2212.10559](https://arxiv.org/abs/2212.10559)
- Garg et al. (2022) — *What can transformers learn in-context? A case study of simple function classes* — NeurIPS — [arxiv:2208.01066](https://arxiv.org/abs/2208.01066)
- Ahn et al. (2024) — *Transformers learn to implement preconditioned gradient descent for in-context learning* — NeurIPS — [arxiv:2306.00297](https://arxiv.org/abs/2306.00297)
- Zhang, Frei & Bartlett (2023) — *Trained transformers learn linear models in-context* — preprint — [arxiv:2306.09927](https://arxiv.org/abs/2306.09927)
- Li, Song et al. (2023) — *The closeness of in-context learning and weight shifting for softmax regression* — preprint — [arxiv:2304.13276](https://arxiv.org/abs/2304.13276)
- Xie et al. (2021) — *An explanation of in-context learning as implicit Bayesian inference* — ICLR — [arxiv:2111.02080](https://arxiv.org/abs/2111.02080)
- Pan et al. (2023) — *What in-context learning "learns" in-context: Disentangling task recognition and task learning* — ACL Findings — [link](https://aclanthology.org/2023.findings-acl.527)
- Lu et al. (2022) — *Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity* — ACL — [arxiv:2104.08786](https://arxiv.org/abs/2104.08786)

(Full 44-entry citations list in frontmatter.)

## Related Digests

- [[vassilyev-2026-rcl]] — Reflective Context Learning: Studying the Optimization Primitives of Context Space — direct counter-thesis target: RCL reuses the ICL-as-GD analogy at the context-artifact level; Shen et al. is the empirical falsifier RCL must answer
- [[brown-2020-gpt3-few-shot]] — Language Models are Few-Shot Learners — the original empirical observation of emergent ICL that motivates all GD-equivalence theorizing
- [[mao-2026-agent-memory-circuits]] — What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis — mechanistic counterpart: circuit-level look at how memory operations actually emerge inside agents (vs the GD-analogy story)
- [[elhage-2022-toy-models-superposition]] — Toy Models of Superposition — adjacent on the "mechanistic interpretability of attention" axis, cited via induction heads (Olsson 2022)

## Reviewer Notes

**Overall severity:** Clean

Every numerical claim in the digest (sparsity thresholds 99.99% / 75%, GD-vs-ICL demo ratio 512:8, AGNews/CB/SST-2/RTE accuracy figures 0.42/0.39/0.49/0.36 → 0.69/0.72/0.75/0.65, evaluation lr set {1e-4, 5e-4, 1e-5, 5e-5}, 200 epochs, 10 random orders, K=10 for Token Overlap, batch sizes {1, 2, 4}, GPT-J checkpoints 310k-380k, model list LLaMa-7B / Qwen-7B / GPT-J) maps directly to the paper sections cited (§1, §3.1-3.2, §4, §5.1-5.2, Tables 1, Figures 2-5, Appendices A-B). The ENGRAM tagging is the digester's framing per the memory-architect lens and is not claimed to be in the paper. The "3-5x" order-sensitivity gap is a careful read of Figure 4 / Figure 6 (LLaMa-7B Sen ~0.10-0.15 for ICL vs ~0.01-0.05 for GD/SGD/Adam across most epochs); a tighter "5x" claim would be at the high end of the visible range, "3-5x" matches the visible distribution. The hypothesis 1 vs hypothesis 2 distinction is taken verbatim from §1 of the paper. No fabricated tools, datasets, or metrics.
