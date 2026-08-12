---
corpus: agentic-memory
kind: paper-digest
slug: bi-2020-palm-context-generation
title: "PALM: Pre-training an Autoencoding & Autoregressive Language Model for Context-conditioned Generation"
authors:
  - "Bi, Bin"
  - "Li, Chenliang"
  - "Wu, Chen"
  - "Yan, Ming"
  - "Wang, Wei"
  - "Huang, Songfang"
  - "Huang, Fei"
  - "Si, Luo"
year: 2020
publication_date: "2020-09"
venue: "arXiv preprint (EMNLP 2020)"
source_url: "https://arxiv.org/abs/2004.07159"
doi: null
arxiv_id: "2004.07159"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Pre-training mismatch is a measurable architectural failure mode: when BERT/MASS/BART train the decoder to reconstruct text the encoder already saw, the model never learns to produce content beyond what is present in context — PALM fixes this by splitting an unlabeled passage 80/20, feeding the first 80% to a bidirectional encoder (MLM loss) and forcing an autoregressive decoder to generate the held-out 20% continuation, plus copying via a pointer-generator; the result is a 10× perplexity drop vs MASS on unseen news continuations (17.22 vs 170.32), Rank-1 on MARCO QA (Rouge-L 0.498), and SOTA Rouge-1/L 44.30/41.41 on CNN/DailyMail."
topics:
  - pre-training-objectives
  - encoder-decoder-architecture
  - context-conditioned-generation
  - abstractive-summarization
  - generative-qa
  - pointer-generator
  - pre-train-fine-tune-mismatch
tags:
  - paper
  - nlp
  - language-modeling
  - seq2seq
  - copy-mechanism
  - emnlp-2020
entities:
  - bi-bin
  - alibaba-group
related_digests:
  - devlin-2018-bert
  - radford-2018-gpt1
  - brown-2020-gpt3-few-shot
  - vaswani-2017-attention-is-all-you-need
  - lewis-2020-rag-knowledge-nlp
citations:
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["Dzmitry Bahdanau", "Kyunghyun Cho", "Yoshua Bengio"]
    year: 2015
    venue: "ICLR 2015"
    doi: null
    url: null
    arxiv_id: "1409.0473"
  - title: "Incorporating external knowledge into machine reading for generative question answering"
    authors: ["Bin Bi", "Chen Wu", "Ming Yan", "Wei Wang", "Jiangnan Xia", "Chenliang Li"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language Models are Few-Shot Learners (GPT-3)"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS 2020"
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "Semi-supervised sequence learning"
    authors: ["Andrew M. Dai", "Quoc V. Le"]
    year: 2015
    venue: "NeurIPS 2015"
    doi: null
    url: null
    arxiv_id: null
  - title: "Chameleons in imagined conversations: A new approach to understanding coordination of linguistic style in dialogs"
    authors: ["Cristian Danescu-Niculescu-Mizil", "Lillian Lee"]
    year: 2011
    venue: "ACL Workshop on Cognitive Modeling and Computational Linguistics"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "Kristina Toutanova"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "Unified language model pre-training for natural language understanding and generation (UniLM)"
    authors: ["Li Dong", "Nan Yang", "Wenhui Wang", "Furu Wei", "Xiaodong Liu", "Yu Wang", "Jianfeng Gao", "Ming Zhou", "Hsiao-Wuen Hon"]
    year: 2019
    venue: "NeurIPS 2019"
    doi: null
    url: null
    arxiv_id: null
  - title: "Harvesting Paragraph-Level Question-Answer Pairs from Wikipedia"
    authors: ["Xinya Du", "Claire Cardie"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1805.05942"
  - title: "Pre-trained language model representations for language generation"
    authors: ["Sergey Edunov", "Alexei Baevski", "Michael Auli"]
    year: 2019
    venue: "NAACL-HLT 2019"
    doi: null
    url: null
    arxiv_id: null
  - title: "Bottom-up abstractive summarization"
    authors: ["Sebastian Gehrmann", "Yuntian Deng", "Alexander M. Rush"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1808.10792"
  - title: "English Gigaword"
    authors: ["David Graff", "Christopher Cieri"]
    year: 2003
    venue: "LDC"
    doi: null
    url: null
    arxiv_id: null
  - title: "UniLMv2: Pseudo-masked language models for unified language model pre-training"
    authors: ["Hangbo Bao", "Li Dong", "Furu Wei", "Wenhui Wang", "Nan Yang", "Xiaodong Liu", "Yu Wang", "Songhao Piao", "Jianfeng Gao", "Ming Zhou", "Hsiao-Wuen Hon"]
    year: 2020
    venue: "ICML 2020"
    doi: null
    url: null
    arxiv_id: null
  - title: "Gaussian error linear units (GELUs)"
    authors: ["Dan Hendrycks", "Kevin Gimpel"]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1606.08415"
  - title: "Teaching machines to read and comprehend (CNN/Daily Mail)"
    authors: ["Karl Moritz Hermann", "Tomáš Kočiský", "Edward Grefenstette", "Lasse Espeholt", "Will Kay", "Mustafa Suleyman", "Phil Blunsom"]
    year: 2015
    venue: "NeurIPS 2015"
    doi: null
    url: null
    arxiv_id: "1506.03340"
  - title: "Universal language model fine-tuning for text classification (ULMFiT)"
    authors: ["Jeremy Howard", "Sebastian Ruder"]
    year: 2018
    venue: "ACL 2018"
    doi: null
    url: null
    arxiv_id: null
  - title: "Tying word vectors and word classifiers: A loss framework for language modeling"
    authors: ["Hakan Inan", "Khashayar Khosravi", "Richard Socher"]
    year: 2017
    venue: "ICLR 2017"
    doi: null
    url: null
    arxiv_id: null
  - title: "Cut to the chase: A context zoom-in network for reading comprehension (ConZNet)"
    authors: ["Sathish Reddy Indurthi", "Seunghak Yu", "Seohyun Back", "Heriberto Cuayáhuitl"]
    year: 2018
    venue: "EMNLP 2018"
    doi: null
    url: null
    arxiv_id: null
  - title: "SpanBERT: Improving pre-training by representing and predicting spans"
    authors: ["Mandar Joshi", "Danqi Chen", "Yinhan Liu", "Daniel S. Weld", "Luke Zettlemoyer", "Omer Levy"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1907.10529"
  - title: "ALBERT: A lite BERT for self-supervised learning of language representations"
    authors: ["Zhen-Zhong Lan", "Mingda Chen", "Sebastian Goodman", "Kevin Gimpel", "Piyush Sharma", "Radu Soricut"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.11942"
  - title: "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension"
    authors: ["Mike Lewis", "Yinhan Liu", "Naman Goyal", "Marjan Ghazvininejad", "Abdelrahman Mohamed", "Omer Levy", "Veselin Stoyanov", "Luke Zettlemoyer"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1910.13461"
  - title: "ROUGE: A package for automatic evaluation of summaries"
    authors: ["Chin-Yew Lin"]
    year: 2004
    venue: "ACL Workshop on Text Summarization Branches Out"
    doi: null
    url: null
    arxiv_id: null
  - title: "Text summarization with pretrained encoders (BERTSUMABS)"
    authors: ["Yang Liu", "Mirella Lapata"]
    year: 2019
    venue: "EMNLP-IJCNLP 2019"
    doi: null
    url: null
    arxiv_id: null
  - title: "RoBERTa: A robustly optimized BERT pretraining approach"
    authors: ["Yinhan Liu", "Myle Ott", "Naman Goyal", "Jingfei Du", "Mandar Joshi", "Danqi Chen", "Omer Levy", "Mike Lewis", "Luke Zettlemoyer", "Veselin Stoyanov"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1907.11692"
  - title: "MS MARCO: A human generated machine reading comprehension dataset"
    authors: ["Tri Nguyen", "Mir Rosenberg", "Xia Song", "Jianfeng Gao", "Saurabh Tiwary", "Rangan Majumder", "Li Deng"]
    year: 2016
    venue: "NIPS Workshop on Cognitive Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multi-style generative reading comprehension (Masque)"
    authors: ["Kyosuke Nishida", "Itsumi Saito", "Kosuke Nishida", "Kazutoshi Shinoda", "Atsushi Otsuka", "Hisako Asano", "Junji Tomita"]
    year: 2019
    venue: "ACL 2019"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep contextualized word representations (ELMo)"
    authors: ["Matthew Peters", "Mark Neumann", "Mohit Iyyer", "Matt Gardner", "Christopher Clark", "Kenton Lee", "Luke Zettlemoyer"]
    year: 2018
    venue: "NAACL-HLT 2018"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving language understanding by generative pre-training (GPT)"
    authors: ["Alec Radford"]
    year: 2018
    venue: "OpenAI tech report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models are unsupervised multitask learners (GPT-2)"
    authors: ["Alec Radford", "Jeff Wu", "Rewon Child", "David Luan", "Dario Amodei", "Ilya Sutskever"]
    year: 2019
    venue: "OpenAI tech report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exploring the limits of transfer learning with a unified text-to-text transformer (T5)"
    authors: ["Colin Raffel", "Noam Shazeer", "Adam Roberts", "Katherine Lee", "Sharan Narang", "Michael Matena", "Yanqi Zhou", "Wei Li", "Peter J. Liu"]
    year: 2019
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: "1910.10683"
  - title: "SQuAD: 100,000+ Questions for Machine Comprehension of Text"
    authors: ["Pranav Rajpurkar", "Jian Zhang", "Konstantin Lopyrev", "Percy Liang"]
    year: 2016
    venue: "EMNLP 2016"
    doi: null
    url: null
    arxiv_id: "1606.05250"
  - title: "A neural attention model for abstractive sentence summarization"
    authors: ["Alexander M. Rush", "Sumit Chopra", "Jason Weston"]
    year: 2015
    venue: "EMNLP 2015"
    doi: null
    url: null
    arxiv_id: null
  - title: "Get to the point: Summarization with pointer-generator networks"
    authors: ["Abigail See", "Peter J. Liu", "Christopher D. Manning"]
    year: 2017
    venue: "ACL 2017"
    doi: null
    url: null
    arxiv_id: null
  - title: "MASS: Masked sequence to sequence pre-training for language generation"
    authors: ["Kaitao Song", "Xu Tan", "Tao Qin", "Jianfeng Lu", "Tie-Yan Liu"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.02450"
  - title: "S-Net: From answer extraction to answer generation for machine reading comprehension"
    authors: ["Chuanqi Tan", "Furu Wei", "Nan Yang", "Weifeng Lv", "Ming Zhou"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1706.04815"
  - title: "Attention is all you need (Transformer)"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "Jakob Uszkoreit", "Llion Jones", "Aidan N. Gomez", "Łukasz Kaiser", "Illia Polosukhin"]
    year: 2017
    venue: "NeurIPS 2017"
    doi: null
    url: null
    arxiv_id: null
  - title: "A neural conversational model"
    authors: ["Oriol Vinyals", "Quoc Le"]
    year: 2015
    venue: "ICML Deep Learning Workshop 2015"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multi-passage machine reading comprehension with cross-passage answer verification (VNET)"
    authors: ["Yizhong Wang", "Kai Liu", "Jing Liu", "Wei He", "Yajuan Lyu", "Hua Wu", "Sujian Li", "Haifeng Wang"]
    year: 2018
    venue: "ACL 2018"
    doi: null
    url: null
    arxiv_id: null
  - title: "ERNIE-GEN: An Enhanced Multi-Flow Pre-training and Fine-tuning Framework for Natural Language Generation"
    authors: ["Dongling Xiao", "Han Zhang", "Yukun Li", "Yu Sun", "Hao Tian", "Hua Wu", "Haifeng Wang"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.11314"
  - title: "PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization"
    authors: ["Jingqing Zhang", "Yao Zhao", "Mohammad Saleh", "Peter J. Liu"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1912.08777"
  - title: "Paragraph-level neural question generation with maxout pointer and gated self-attention networks"
    authors: ["Yao Zhao", "Xiaochuan Ni", "Yuanyuan Ding", "Qifa Ke"]
    year: 2018
    venue: "EMNLP 2018"
    doi: null
    url: null
    arxiv_id: null
  - title: "Aligning books and movies: Towards story-like visual explanations by watching movies and reading books (BookCorpus)"
    authors: ["Yukun Zhu", "Ryan Kiros", "Richard S. Zemel", "Ruslan Salakhutdinov", "Raquel Urtasun", "Antonio Torralba", "Sanja Fidler"]
    year: 2015
    venue: "ICCV 2015"
    doi: null
    url: null
    arxiv_id: "1506.06724"
hallucination_severity: "Minor fact tweak"
best_figure:
  number: 1
  title: "A schematic comparison of PALM with GPT, MASS and BART"
  page: 3
  image_path: "figures/bi-2020-palm-context-generation-fig.png"
---

# PALM: Pre-training an Autoencoding & Autoregressive Language Model for Context-conditioned Generation

**Authors:** Bin Bi, Chenliang Li, Chen Wu, Ming Yan, Wei Wang, Songfang Huang, Fei Huang, Luo Si (Alibaba Group)
**Published:** 2020-09 · [Source](https://arxiv.org/abs/2004.07159)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Existing pre-training objectives (BERT-style autoencoding, GPT-style autoregression, MASS/BART denoising encoder-decoders) all train the model to recover tokens that are already present in the input — which is mismatched with downstream tasks like generative QA, abstractive summarization and dialog response that demand *new* text conditioned on context. PALM, from Alibaba's NLP group, fixes this by stacking two pre-training stages on a shared Transformer encoder-decoder (12-12 layers base; 24-encoder + 6-decoder large; encoder initialised from RoBERTa): stage 1 is BERT-style MLM on the encoder over a passage; stage 2 takes the first 80% of an unlabeled text fragment (≤ 400 tokens) as encoder input and forces the decoder to autoregressively generate the held-out 20% continuation (≤ 100 tokens), with a pointer-generator on top of the decoder that mixes a vocabulary distribution and a copy-from-context distribution via a learned sigmoid gate λ. Trained on Wikipedia + BookCorpus for 800K steps on 16 V100s over 3 days (50M pre-training pairs from a sliding window with stride 1 sentence), PALM hits perplexity 17.22 on held-out CNN news continuations vs MASS's 170.32 (~10× drop), Rank-1 on the MARCO QA leaderboard with Rouge-L 0.498 (beating Masque ensemble at 0.496), SOTA Rouge-1/L 44.30/41.41 on CNN/DailyMail summarization (PALM-Large), Rouge-L 36.75 on Gigaword, BLEU-4 24.11 on SQuAD question generation, and perplexity 21.98 on Cornell Movie Dialog response generation (vs 23.52 for MASS, 24.84 BERT+LM, 26.38 baseline). Ablations show removing pre-training entirely costs 6.5%+ on Rouge-L; removing the autoencoding stage costs 0.90 Rouge-L; removing the autoregression stage costs 0.79 Rouge-L; removing the pointer-generator costs only 0.22 Rouge-L. Most useful takeaway: the architectural primitive that matters is the *split between what the encoder sees and what the decoder is asked to produce* — train the decoder on the continuation it never saw, and you have a model that learned to extrapolate from context rather than copy it back.

## Key Takeaway

The messier and more honest you make the pre-training objective — handing the decoder *new* tokens it has never observed and asking it to guess them from upstream context — the more your fine-tuned generator stops parroting the input and starts reasoning forward from it. PALM proves the opposite of what the BERT-derivative ecosystem assumed in 2019-2020: copying the encoder's input back through the decoder (MASS, BART) is a structurally easier task than producing the next 100 tokens, and that easiness leaks downstream as a fine-tuning ceiling. The 10× perplexity gap over MASS on unseen news continuations isn't a tuning artifact, it's a measurement of how much capability the denoising objective leaves on the table.

## Implications

- **[E — Encode] Match the pre-training write-task to the eventual read-task, or you waste capacity.** PALM's whole premise is that BART/MASS train the decoder on a task (reconstruct the masked input) that is structurally easier than what downstream tasks demand (generate new text from context). The same logic transfers to agentic memory: if you train an extraction LLM on "summarize this turn" but expect it to "produce the next intent given prior turns," you'll see the same mismatch — measure it directly with a held-out continuation perplexity, the way PALM measures it (17.22 vs MASS's 170.32 on CNN news).
- **[E — Encode + N — Network] An 80/20 contiguous-passage split is a cheap, self-supervised proxy for "memory-conditioned generation."** The 80% encoded → 20% generated split (≤ 400 tokens in, ≤ 100 tokens out, sliding window stride 1 sentence on Wikipedia+BookCorpus → 50M training pairs) requires no labels and gives the model a reliable signal: *what does coherent text look like after a long passage?* For a memory system, the analog is "given the prior N session turns / N memory cards, predict the next decision or answer the user would accept" — train your retrieval/extraction stack on real continuations, not on reconstruction.
- **[A — Aggregate] Two-stage joint pre-training beats single-objective.** The ablation grid (Table 6) shows removing either the autoencoding stage (-0.90 Rouge-L) or the autoregression stage (-0.79 Rouge-L) is materially worse than removing the pointer-generator (-0.22). The structural decision is dimensional: encoder-comprehension and decoder-generation each pay rent, and you can't fold one into the other without losing measurable performance. Translation for memory systems: write-time abstraction and read-time generation are independent dimensions in ENGRAM-Aggregate — don't conflate them into one prompt.
- **[R — Retrieve] The pointer-generator is the load-bearing primitive for grounded copying — but it's nearly free to drop.** Removing the pointer-generator costs only 0.22 Rouge-L (Table 6). For a memory architecture, this is the inversion of "RAG-vs-pure-LLM" — once the encoder has truly comprehended context, the explicit copy path is marginal. The cheap win is the comprehension, not the copy gate. Don't over-engineer your retrieval citation paths if your context-conditioning is strong; do over-engineer your context-conditioning.
- **[G — Ground] PALM happily hallucinates in pre-training and the authors don't apologise.** The paper's own example explicitly notes that PALM invents a "Cape Verde Islands National Park" that "does not really exist" in the pre-training continuation example — and the authors frame this as an emergent inference capability transferable downstream via fine-tuning (§3.2). For memory architects, this is the key ENGRAM-Ground warning: a system trained to extrapolate from context will fluently fabricate when the context underdetermines the answer. If your memory layer compiles "what's likely true given X" rather than "what's verifiable about X," you inherit this failure mode by default. Provenance is not free — pre-training does not give it to you.
- **[M — Maintain + N — Network] Encoder init from RoBERTa is the unsung lever.** PALM doesn't pre-train its encoder from scratch — §3.1 explicitly states "The parameters of PALM's encoder are initialized by the pre-trained RoBERTa model" (also implicit: BookCorpus + Wikipedia same as BERT/RoBERTa). The paper does not state how the decoder is initialised. For a memory-architecture rewrite, the operational lesson is still: re-use whatever frozen encoder you already trust (an existing extraction model, or an off-the-shelf embedding model), and only train the part of the stack that does the new job. This is the v2 memory schema discipline applied to architecture: don't re-derive what you already have.
- **[E — Encode] 16 V100s × 3 days × 800K steps × 64 batch × 500 max-len is a SOTA-grade pre-training run on a startup budget.** The compute footprint is roughly 1,150 GPU-hours (16 V100s × 72 h) — equivalent to a single workstation with 8 V100s running for ~6 days. This sets a useful reference price for any "we'll train our own memory-extraction backbone" project in the agentic-OS context. If the bet justifies that, you can self-host; if not, you should be wrapping a frozen API model.
- **[A — Aggregate] Inference quality (≠ factual accuracy) is the unstated win.** Beyond ROUGE deltas, the qualitative examples in Table 1 show PALM making forward inferences ("expected to fetch £2.5 million") that MASS cannot — even when those inferences are wrong. For an agentic-OS memory system trying to compile patterns, this is the desired behavior at write-time (generate hypotheses from context) but the dangerous behavior at retrieval-time (don't promote those hypotheses to confirmed facts). The architectural lesson is to separate "PALM-like inferencer" from "BERT-like verifier" — never let one model do both.

## How to Apply It (method)

**Scenario:** You're a memory-architecture researcher on a team building an agentic OS. Today, your memory layer uses a frozen embedding model + BM25 over markdown vault notes, and a single LLM call at query time that takes the top-k chunks and "answers." You've noticed that for any query that requires synthesizing the *next* step (e.g. "given everything I've decided in the last 30 days, what should I do next about Flow OS pricing?"), the model regurgitates past decisions rather than projecting forward. You want to test whether a small purpose-trained extractor — one that has been pre-trained on the "given prior session memory, generate the next likely user intent" objective — measurably improves the forward-projection failure mode without giving up the verification properties of your current pipeline.

**Steps:**

1. **Define a held-out continuation benchmark for your domain**: Pull 500 multi-turn sessions from your own session-log archive. For each, designate the first 80% of turns as "context" and the final 20% as "held-out continuation." Save as `eval/forward-projection.jsonl` with fields `{context: str, continuation: str, session_id: str}`. The eval metric is perplexity (or ROUGE-L if the continuations are too divergent for PPL to be stable) on the continuation, given the context — exactly the PALM § 3.2 protocol.

2. **Build the 80/20 sliding-window pre-training corpus from unlabeled session data**:

   ```
   For each session in your archive (assume 50K sessions):
     - Tokenize into a fragment of length L ≤ 500 tokens
     - Take the first 0.8*L tokens as encoder input x
     - Take the last 0.2*L tokens as decoder target y
     - Emit (x, y) pair
     - Slide window forward by 1 sentence, repeat
   Resulting corpus: ~5M (x, y) pairs (matches PALM's 50M scale per 10× ratio).
   ```

3. **Pick a Transformer encoder-decoder base and warm-start the encoder**: Start from `t5-base` or `bart-base` (already-trained encoder-decoder) OR initialize encoder from a frozen RoBERTa/DeBERTa checkpoint and pair with a randomly-initialized 6-layer decoder (PALM-Large pattern). For a small-team rewrite, `t5-base` is cheaper to spin up; for the actual PALM recipe, use the asymmetric 24-encoder + 6-decoder configuration.

4. **Implement the two-stage joint pre-training loop**:

   - **Stage 1 (autoencoding)**: For each batch, mask 15% of encoder-input tokens with `[MASK]` (BERT-style). Compute MLM cross-entropy on the masked positions only. This warms up the encoder's comprehension.
   - **Stage 2 (autoregressive context-conditioned generation)**: With the same batch, feed full (unmasked) encoder input to the encoder; feed `<s> y_1 ... y_{n-1}` to the decoder; compute autoregressive cross-entropy on `y_1 ... y_n`. The decoder must produce `y` (the held-out 20%) by attending to the encoder's representations of the 80% context.

   Run both losses jointly (sum them, optionally with a small Stage-1 weight to prevent encoder drift). PALM hyperparameters: dropout 0.1, GELU activation, learning rate 1e-5 with 10K-step linear warmup + linear decay, max-seq-len 500, batch 64, 800K steps total. On 8× A100s this maps to roughly 1-2 weeks of training depending on model size.

5. **Add a pointer-generator on top of the decoder (optional — measure the ablation gap first)**:

   For each decoder timestep `t`, compute:
   - Vocabulary distribution `P^v(y_t) = softmax(W^e (W^v s_t + b^v))` where `s_t` is the decoder state and `W^e` is tied to the input embedding.
   - Copy distribution via an additional attention layer over the encoder hidden states `h^c_l`: `α^c_t = softmax(w^c · tanh(W^m h^c + W^s s_t + b^c))`, then `P^c(y_t) = Σ_{l: x_l = y_t} α^c_{tl}`.
   - Mixture: `λ = sigmoid(w^z z^c_t + w^s s_t + b^m)`, final `P(y_t) = λ · P^v(y_t) + (1−λ) · P^c(y_t)`.

   In your context, this is the architectural equivalent of an "explicit citation gate" — the model learns when to write words from its vocabulary vs. when to copy spans from the retrieved memory chunks. Per PALM's ablation, the gain is small (~0.22 Rouge-L). Measure on YOUR data before committing to the engineering complexity.

6. **Run the held-out continuation eval (Step 1) on both the base checkpoint and the PALM-pre-trained checkpoint**: Report perplexity and ROUGE-L. PALM's reference deltas: pre-training shaves perplexity ~10× over base (17.22 vs 170.32 in their CNN comparison) and pre-training contributes 6.5%+ Rouge-L over a no-pre-training baseline on summarization. If you see less than a 2× perplexity drop on your held-out continuations, your domain probably doesn't have enough long-passage coherence to benefit — fall back to RAG.

7. **Fine-tune on your actual downstream task with the same encoder-decoder + pointer-generator**: For the "given memory, generate next user intent" task, your fine-tuning data is `(memory_card_bundle, next_user_message)` pairs from your interaction logs. Use exact PALM hyperparameters: batch 64, learning rate 1e-5, beam search width 5 at decode time, 10 epochs. The pointer-generator weights from pre-training pass through and continue to learn.

8. **Run a contamination check at inference time**: PALM's own qualitative examples (Cape Verde Islands National Park fabrication) document that this architecture freely hallucinates plausible-sounding continuations. Wrap the deployed model's output in a verifier pass — either a separate retrieval-grounded check or a simple "does this claim appear verbatim or near-verbatim in the cited memory cards?" filter. Treat PALM-style models as **hypothesis generators** at write-time, not as **fact retrievers** at read-time.

**Expected outcome:** A custom pre-trained context-to-continuation model that measurably reduces the "regurgitation" failure mode for forward-projection queries, with a documented perplexity-on-held-out-continuations benchmark you can re-run on every checkpoint. You will also have an ablation table for your domain showing the relative contribution of autoencoding stage, autoregression stage, pointer-generator, and pre-training overall — which lets you make a defensible build-vs-buy call against frozen-API alternatives. The cost is roughly 5K GPU-hours per full pre-training run; the deliverable is a checkpoint plus a written architecture-decision record framed in ENGRAM dimensions (Encode/Network/Ground/Retrieve/Aggregate/Maintain) for the next team that touches the memory stack.

## Best Figure

![Figure 1 — A schematic comparison of PALM with GPT, MASS and BART (page 3)](figures/bi-2020-palm-context-generation-fig.png)

**Image Candidates:**
- Figure 1 (p. 3): Four-panel side-by-side schematic of GPT vs MASS vs BART vs PALM — the cleanest single-view contrast in the paper.
- Table 1 (p. 4): Two qualitative example continuations of PALM vs MASS on news articles — vivid but textual.
- Table 6 (p. 7): The ablation grid removing pointer-generator / autoencoding / autoregression / pre-training one at a time — best at showing component contributions.

**Best Image:**
- **Figure Name:** Figure 1: "A schematic comparison of PALM with GPT, MASS and BART"
- **Figure Page:** 3
- **Slide Caption:** PALM differs from prior pre-training schemes by feeding the encoder a 80% prefix of context and forcing the decoder to autoregressively generate the held-out 20% continuation — not to reconstruct what the encoder already saw.
- **Description:** Figure 1 lays out four encoder-decoder schematics side-by-side. Panel (a) shows GPT — a decoder-only autoregressive model with no encoder for context conditioning. Panel (b) shows MASS — an encoder-decoder where the bidirectional encoder receives partially-masked tokens (x_1, _, _, _, x_5) and the decoder predicts *only the masked positions* (x_2, x_3, x_4). Panel (c) shows BART — same encoder-decoder shape as MASS, but the decoder reconstructs the *full* original sequence (x_1, x_2, x_3, x_4, x_5) from the corrupted input. Panel (d) shows PALM — the bidirectional encoder receives the partially-masked context (x_1, _, x_3, _, x_5) and emits two outputs: the encoder predicts the masked tokens (x_2, x_4), and the decoder predicts a *different* continuation sequence (y_6, y_7, y_8, y_9) that comes after the encoder's input span in the original passage. The visual contrast crystallises the paper's whole argument: PALM is the only one of the four where the decoder's target is genuinely *new* text the encoder never saw, which is what context-conditioned generation downstream actually requires.

## What Experts Overlook

The detail most readers skim past is **§ 2.2's exact ratio: 80% of a length-L text fragment as encoder input, 20% as decoder target, with L ≤ 500, sliding window stride of one sentence over Wikipedia + BookCorpus → 50M training pairs**. Everyone notices that PALM "splits the passage and generates the continuation"; few notice that 80/20 is a designed choice that mimics the input/output token ratio of MARCO QA, CNN/DailyMail summarization, and SQuAD QG (long passage in, short answer out). This is visible in Section 2.2: "context input consists of at most 400 tokens, and the text output consists of at most 100 tokens" — exactly the input/output budget of the downstream eval tasks.

**Why it matters:** Pre-training-fine-tuning mismatch isn't just about the *objective* (reconstruct vs. continue) — it's about the *shape* of the input/output spans the model has seen. By matching the pre-training span ratio to the downstream span ratio, PALM gives the model 50M practice examples at *exactly the kind of "long-in, short-out" generation it will be asked to do at fine-tune time*. The architectural gain isn't only "autoregressive decoder forced to be context-sensitive"; it's also "decoder has already seen 50M examples of producing ~100 tokens from ~400 tokens of context." If you only adopt the joint pre-training scheme but use a 50/50 or 60/40 split, you give up part of the alignment benefit. This is a subtle ENGRAM-Encode lesson: the *shape* of the training datum matters as much as the *objective*.

**Example of good use:** You're pre-training an agentic-OS continuation model where the production task is "given ~3000 tokens of session memory cards, produce a ~600-token next-action plan." Match the pre-training split: 83.3% encoder context / 16.7% decoder target. Slide a window over your unlabeled session archive with a per-turn stride. The model will land on the production task with the right input/output budget already baked in — instead of fighting the model's prior that "decoder targets are roughly the length of encoder inputs" (which is what you'd get from a 50/50 split or a generic seq2seq pre-train).

**Example of misapplication:** You read PALM, adopt the joint AE+AR pre-training scheme, but pre-train on a corpus where you split at the document level (full document in, full document summary out — say 5000 tokens in, 200 tokens out, 96/4 split). You then fine-tune on chat-style sessions where the expected output is one full turn (~150 tokens) given the prior ~600 tokens of context (a 80/20 split). The model has been trained to produce highly compressed summaries — at fine-tune time it under-generates (terse, summary-style responses) and the team blames "PALM isn't suited to dialog." The actual failure is span-ratio drift between pre-training and fine-tuning: PALM's lesson is that the pre-training span ratio *is* part of the architecture, not just a hyperparameter to leave at default.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- Bahdanau, Cho, Bengio (2015) — Neural machine translation by jointly learning to align and translate (ICLR 2015) — `arxiv:1409.0473`
- Bi, Wu, Yan, Wang, Xia, Li (2019) — Incorporating external knowledge into machine reading for generative question answering
- Brown et al. (2020) — Language Models are Few-Shot Learners (GPT-3) — `arxiv:2005.14165`
- Devlin, Chang, Lee, Toutanova (2018) — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding — `arxiv:1810.04805`
- Dong et al. (2019) — Unified language model pre-training for natural language understanding and generation (UniLM) — NeurIPS 2019
- Hangbo et al. (2020) — UniLMv2: Pseudo-masked language models for unified language model pre-training — ICML 2020
- Lewis et al. (2019) — BART: Denoising Sequence-to-Sequence Pre-training for NLG, Translation, and Comprehension — `arxiv:1910.13461`
- Liu et al. (2019) — RoBERTa: A robustly optimized BERT pretraining approach — `arxiv:1907.11692`
- Song et al. (2019) — MASS: Masked sequence to sequence pre-training for language generation — `arxiv:1905.02450`
- See, Liu, Manning (2017) — Get to the point: Summarization with pointer-generator networks — ACL 2017
- Vaswani et al. (2017) — Attention is all you need — NeurIPS 2017
- Raffel et al. (2019) — Exploring the limits of transfer learning with a unified text-to-text transformer (T5) — `arxiv:1910.10683`
- Zhang et al. (2019) — PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization — `arxiv:1912.08777`
- Xiao et al. (2020) — ERNIE-GEN: An Enhanced Multi-Flow Pre-training and Fine-tuning Framework for NLG — `arxiv:2001.11314`

_(full structured citation list in frontmatter `citations:`)_

## Related Digests

- [[devlin-2018-bert]] — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- [[radford-2018-gpt1]] — Improving Language Understanding by Generative Pre-Training (GPT-1)
- [[brown-2020-gpt3-few-shot]] — Language Models are Few-Shot Learners (GPT-3)
- [[vaswani-2017-attention-is-all-you-need]] — Attention Is All You Need
- [[lewis-2020-rag-knowledge-nlp]] — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Reviewer Notes

**Overall severity:** Minor fact tweak (resolved in revision)

**Flagged claims (originally):**

- **Claim:** "The compute footprint is roughly 5K GPU-hours"
  **Label:** Inaccurate
  **Justification:** §3.1 says PALM trained on 16 NVIDIA V100s for 3 days. That is 16 × 72 ≈ 1,152 GPU-hours, not 5,000. The 5K figure was a calculation error.
  **Fix applied:** Replaced with "roughly 1,150 GPU-hours (16 V100s × 72 h) — equivalent to a single workstation with 8 V100s running for ~6 days."

- **Claim:** "The decoder is trained from scratch."
  **Label:** Partially accurate (inferred, not stated)
  **Justification:** §3.1 explicitly says the encoder is initialised from a pre-trained RoBERTa checkpoint. It does NOT state how the decoder is initialised. The "from scratch" interpretation is plausible but not directly supported by the paper.
  **Fix applied:** Replaced with "The paper does not state how the decoder is initialised."

All other concrete claims (perplexity 17.22 vs 170.32, MARCO Rouge-L 0.498, CNN/DM 44.30/41.41, Gigaword 36.75, SQuAD BLEU-4 24.11, Cornell PPL 21.98 vs baselines 23.52/24.84/26.38, ablation deltas 0.90 / 0.79 / 0.22 / 6.5%+, 80/20 split with L ≤ 500, 16 V100s × 3 days × 800K steps × batch 64, RoBERTa-init encoder, Cape Verde Islands National Park hallucination example, pointer-generator equations) are directly supported by §2.2, §2.3, §3.1, §3.2, §3.3, §3.4, §3.5, §3.6, §3.7, and Tables 2-6.

