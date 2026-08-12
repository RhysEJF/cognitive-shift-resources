---
corpus: agentic-memory
kind: paper-digest
slug: lewis-2019-bart
title: "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension"
authors:
  - "Lewis, Mike"
  - "Liu, Yinhan"
  - "Goyal, Naman"
  - "Ghazvininejad, Marjan"
  - "Mohamed, Abdelrahman"
  - "Levy, Omer"
  - "Stoyanov, Ves"
  - "Zettlemoyer, Luke"
year: 2019
publication_date: "2019-10"
venue: "arXiv preprint (later ACL 2020)"
source_url: "https://arxiv.org/abs/1910.13461"
doi: null
arxiv_id: "1910.13461"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Reconstructing a deliberately corrupted document forces a single model to learn both understanding and generation in one pass — making the choice of corruption function (not architecture) the lever that decides what the model is good at."
topics:
  - denoising-autoencoder
  - pretraining-objectives
  - sequence-to-sequence
  - text-infilling
  - encode-strategy
  - write-time-synthesis
tags:
  - paper
  - nlp
  - pretraining
  - bart
  - transformer
  - canonical
entities:
  - lewis-mike
  - liu-yinhan
  - goyal-naman
  - zettlemoyer-luke
  - levy-omer
related_digests:
  - devlin-2018-bert
  - radford-2018-gpt1
  - liu-2019-roberta-pretraining
  - radford-2019-gpt2-multitask
  - brown-2020-gpt3-few-shot
  - dai-2015-semi-supervised-sequence-learning
citations:
  - title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."]
    year: 2019
    venue: "NAACL-HLT"
    doi: "10.18653/v1/N19-1423"
    url: "https://www.aclweb.org/anthology/N19-1423"
    arxiv_id: null
  - title: "RoBERTa: A Robustly Optimized BERT Pretraining Approach"
    authors: ["Yinhan Liu", "Myle Ott", "Naman Goyal", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1907.11692"
  - title: "XLNet: Generalized Autoregressive Pretraining for Language Understanding"
    authors: ["Zhilin Yang", "Zihang Dai", "Yiming Yang", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1906.08237"
  - title: "SpanBERT: Improving Pre-training by Representing and Predicting Spans"
    authors: ["Mandar Joshi", "Danqi Chen", "Yinhan Liu", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1907.10529"
  - title: "Unified Language Model Pre-training for Natural Language Understanding and Generation"
    authors: ["Li Dong", "Nan Yang", "Wenhui Wang", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.03197"
  - title: "MASS: Masked Sequence to Sequence Pre-training for Language Generation"
    authors: ["Kaitao Song", "Xu Tan", "Tao Qin", "et al."]
    year: 2019
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Attention Is All You Need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Cross-lingual Language Model Pretraining"
    authors: ["Guillaume Lample", "Alexis Conneau"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1901.07291"
  - title: "ALBERT: A Lite BERT for Self-Supervised Learning of Language Representations"
    authors: ["Zhenzhong Lan", "Mingda Chen", "Sebastian Goodman", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.11942"
  - title: "Deep Contextualized Word Representations"
    authors: ["Matthew E. Peters", "Mark Neumann", "Mohit Iyyer", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1802.05365"
  - title: "Improving Language Understanding by Generative Pre-training"
    authors: ["Alec Radford", "Karthik Narasimhan", "Tim Salimans", "et al."]
    year: 2018
    venue: "OpenAI tech report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language Models are Unsupervised Multitask Learners"
    authors: ["Alec Radford", "Jeffrey Wu", "Rewon Child", "et al."]
    year: 2019
    venue: "OpenAI Blog"
    doi: null
    url: null
    arxiv_id: null
  - title: "SQuAD: 100,000+ Questions for Machine Comprehension of Text"
    authors: ["Pranav Rajpurkar", "Jian Zhang", "Konstantin Lopyrev", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1606.05250"
  - title: "GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding"
    authors: ["Alex Wang", "Amanpreet Singh", "Julian Michael", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1804.07461"
  - title: "Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization"
    authors: ["Shashi Narayan", "Shay B. Cohen", "Mirella Lapata"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1808.08745"
  - title: "ELI5: Long Form Question Answering"
    authors: ["Angela Fan", "Yacine Jernite", "Ethan Perez", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1907.09190"
  - title: "Teaching Machines to Read and Comprehend"
    authors: ["Karl Moritz Hermann", "Tomas Kocisky", "Edward Grefenstette", "et al."]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "The Second Conversational Intelligence Challenge (ConvAI2)"
    authors: ["Emily Dinan", "Varvara Logacheva", "Valentin Malykh", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1902.00098"
  - title: "Text Summarization with Pretrained Encoders"
    authors: ["Yang Liu", "Mirella Lapata"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1908.08345"
  - title: "Get to the Point: Summarization with Pointer-Generator Networks"
    authors: ["Abigail See", "Peter J. Liu", "Christopher D. Manning"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1704.04368"
  - title: "Pre-trained Language Model Representations for Language Generation"
    authors: ["Sergey Edunov", "Alexei Baevski", "Michael Auli"]
    year: 2019
    venue: "NAACL-HLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Edinburgh Neural Machine Translation Systems for WMT 16"
    authors: ["Rico Sennrich", "Barry Haddow", "Alexandra Birch"]
    year: 2016
    venue: "WMT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Gaussian Error Linear Units (GELUs)"
    authors: ["Dan Hendrycks", "Kevin Gimpel"]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1606.08415"
  - title: "Controllable Abstractive Summarization"
    authors: ["Angela Fan", "David Grangier", "Michael Auli"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1711.05217"
  - title: "Regularizing Neural Networks by Penalizing Confident Output Distributions"
    authors: ["Gabriel Pereyra", "George Tucker", "Jan Chorowski", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1701.06548"
  - title: "Efficient Estimation of Word Representations in Vector Space"
    authors: ["Tomas Mikolov", "Kai Chen", "Greg Corrado", "et al."]
    year: 2013
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1301.3781"
  - title: "A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference"
    authors: ["Adina Williams", "Nikita Nangia", "Samuel R. Bowman"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1705.04426"
  - title: "Neural Network Acceptability Judgments"
    authors: ["Alex Warstadt", "Amanpreet Singh", "Samuel R. Bowman"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1805.12471"
  - title: "Recursive Deep Models for Semantic Compositionality over a Sentiment Treebank"
    authors: ["Richard Socher", "Alex Perelygin", "Jean Wu", "et al."]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Automatically Constructing a Corpus of Sentential Paraphrases"
    authors: ["William B. Dolan", "Chris Brockett"]
    year: 2005
    venue: "International Workshop on Paraphrasing"
    doi: null
    url: null
    arxiv_id: null
  - title: "The PASCAL Recognising Textual Entailment Challenge"
    authors: ["Ido Dagan", "Oren Glickman", "Bernardo Magnini"]
    year: 2006
    venue: "Springer"
    doi: null
    url: null
    arxiv_id: null
  - title: "The Winograd Schema Challenge"
    authors: ["Hector J. Levesque", "Ernest Davis", "Leora Morgenstern"]
    year: 2011
    venue: "AAAI Spring Symposium"
    doi: null
    url: null
    arxiv_id: null
  - title: "Proceedings of the Fourth International Workshop on Semantic Evaluations (SemEval-2007)"
    authors: ["Eneko Agirre", "Lluís Màrquez", "Richard Wicentowski"]
    year: 2007
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "A schematic comparison of BART with BERT and GPT"
  page: 2
  image_path: "figures/lewis-2019-bart-fig.png"
---

# BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension

**Authors:** Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov, Luke Zettlemoyer
**Published:** 2019-10 · [Source](https://arxiv.org/abs/1910.13461)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

BART is a denoising autoencoder built as a standard Transformer encoder-decoder that is pre-trained by corrupting documents with arbitrary noising functions and learning to reconstruct the originals — explicitly generalizing BERT (bidirectional encoder, no generation), GPT (left-to-right decoder, no bidirectional context), and several other 2018–2019 pretraining schemes inside one framework. Lewis et al. evaluate five corruptions (token masking, token deletion, sentence permutation, document rotation, text infilling with Poisson span lengths λ=3) on six tasks; the winning recipe combines text infilling with sentence shuffling, masking 30% of tokens, and shows that document rotation and pure sentence permutation are nearly useless in isolation (SQuAD F1 drops from ~90 to 77 and 85, respectively). At RoBERTa scale (12+12 layers, hidden=1024, batch 8000, 500k steps, 160GB of news/books/stories/web) BART matches RoBERTa within 0.1–0.5 points on GLUE/SQuAD while setting new SOTA on abstractive generation: **+6 ROUGE on XSum** (45.14/22.27/37.25 vs. 38.81/16.50/31.27 for BERTSUMEXTABS), wins on CNN/DailyMail and ConvAI2, +1.2 ROUGE-L on ELI5, and +1.1 BLEU on WMT16 RO-EN by stacking a small randomly-initialized encoder that "translates" Romanian into BART's denoising input space. Most actionable: with one architecture you can decide what the model is good at by changing the corruption function on the write path, and the same recipe transfers across understanding, generation, and translation.

## Key Takeaway

Reconstructing a deliberately corrupted document forces a single model to learn both understanding and generation in one pass — making the choice of corruption function (not architecture) the lever that decides what the model is good at. The deep counter-intuitive lesson is that **destroying the input on purpose, then asking the model to repair it, is a more general and more transferable training signal than predicting missing tokens in place**: it makes the model reason about length, order, and continuity (not just identity), which is precisely the bundle of capabilities downstream generation tasks need.

## Implications

- **Treat the corruption function as a design variable, not a fixed objective**: BART shows that swapping noising schemes inside one architecture moves XSum perplexity from 6.61 (text infilling) to 17.14 (document rotation) — a 2.6× swing. For a memory system, the analogue is treating *which signals you corrupt-and-reconstruct on the write path* (full session vs sentence vs entity-span) as a knob you tune per downstream task — not a one-time installation decision. **ENGRAM: E (Encode), A (Aggregate).**

- **Span-level corruption beats token-level when downstream work has variable structure**: Token masking and token deletion get you to a baseline, but text infilling — replacing variable-length spans (drawn from Poisson λ=3) with a single mask — wins on every generation metric because it forces the model to learn *how much is missing*, not just *what*. For memory consolidation, this argues for "summarize this span and re-expand it" as a write-path objective rather than "fill in this redacted noun." **ENGRAM: E (Encode), A (Aggregate).**

- **One model, many shapes — but only if pretraining trains the seq2seq alignment from the start**: BART's discriminative scores (GLUE: 89.9/90.1 MNLI, ~equal to RoBERTa) come *not* from a special classification head trained later, but from feeding the same input to encoder and decoder and reading off the final decoder token. For polyglot memory stacks, this is the cleanest evidence that a single backbone can serve retrieval, classification, and generation if it was trained on a reconstruction objective that touches all three modes. **ENGRAM: N (Network), R (Retrieve).**

- **The decoder is always trained on uncorrupted context — that's the bridge between pretraining and generation**: Unlike UniLM (where masks are conditionally independent) or MASS (disjoint encoder/decoder token sets), BART's decoder sees the full original document during pretraining. This reduces the pretraining-generation mismatch that hobbles BERT-family models when asked to write. For a memory architect this maps to: **train your synthesizer on the actual target it will produce at query time, not on a degraded surrogate.** **ENGRAM: A (Aggregate), R (Retrieve).**

- **A small randomly-initialized "adapter encoder" can compose a foreign signal onto a pretrained model**: For RO-EN translation, BART replaces its embedding layer with a fresh encoder trained to map Romanian into BART's noised English input space, then fine-tunes (+1.1 BLEU over a strong back-translation baseline). For memory systems this is a templating pattern: when a new source format arrives (Slack thread, calendar event, podcast transcript), train a small adapter that re-encodes it into your existing model's "denoised" canonical form rather than retraining the whole pipeline. **ENGRAM: E (Encode), N (Network).**

- **The pretraining objective is not the only important factor**: BART's permuted LM ablation underperforms XLNet even though both use permutation, because BART omits relative-position embeddings and segment-level recurrence. Translation: **architectural details (positional encoding, layer norm placement, attention masking) interact with the training objective non-trivially** — when evaluating a published memory system, control for these or your replication will silently regress. **ENGRAM: G (Ground) — provenance over claimed mechanisms.**

- **Some signals just don't repay heavy pretraining**: On ELI5 (long-form abstractive QA where answers are only weakly specified by the question), a pure language model beats every denoising variant — BART explicitly says "BART is less effective when the output is only loosely constrained by the input." For memory systems: **when query→answer determinism is low, expensive write-time synthesis is wasted; lean on raw retrieval + generation.** **ENGRAM: R (Retrieve), A (Aggregate).**

- **Disable dropout near the end of training**: Buried in §5.1 — they disabled dropout for the final 10% of pre-training steps to better fit the data. This kind of late-stage tightening is the sort of detail that gets dropped from re-implementations and silently costs 1–2 points of downstream accuracy. **ENGRAM: M (Maintain) — lifecycle tuning matters as much as objective choice.**

## How to Apply It (method)

**Scenario:** You are maintaining a session-memory layer for an agentic OS. Currently you run a write-time extractor that pulls "atomic" facts from each session transcript into a flat vector store. Two problems: (1) retrieval recall is low when queries phrase things differently than the extracted facts, and (2) you have no way to consolidate stale episodes into denser summaries without losing source attribution. You want to test whether a BART-style "corrupt-and-reconstruct" write-path objective produces a memory layer that (a) preserves provenance, (b) generalizes across query phrasings, and (c) can be tuned for different downstream agent jobs without retraining from scratch.

**Steps:**

1. **Pick your corruption catalogue**: Define 4–6 corruption functions over your atomic memory unit (session paragraph, decision log, contact note). At minimum include the BART set:
   - **Token masking** — replace 15% of tokens with `[MASK]`.
   - **Token deletion** — drop 15% of tokens silently (model must infer position).
   - **Text infilling** — sample spans with length ~ Poisson(λ=3), replace each span with one `[MASK]` token (0-length spans become inserted masks).
   - **Sentence permutation** — shuffle sentences inside the unit.
   - **Document rotation** — rotate the unit to start at a random token.
   - **Composite** — text infilling + sentence permutation (BART's winning combo).

2. **Build the encoder-decoder synthesizer**: Stand up a small seq2seq transformer (6+6 base or 12+12 large). Encoder takes the corrupted memory; decoder reconstructs the original. Cross-entropy loss between decoder output and original. Use GELU activations and N(0, 0.02) init. Mask **30%** of tokens per unit (BART's large-scale value, higher than BERT's 15%).

   ```
   write_path(session_text):
       corrupted = compose(text_infilling, sentence_permutation)(session_text)
       reconstruction = decoder(encoder(corrupted))
       loss = cross_entropy(reconstruction, session_text)
       store(corrupted, reconstruction, original=session_text, loss_history)
   ```

3. **Run the ablation table (BART §4)**: Pre-train one variant per corruption on the same data, same code, same fine-tuning. Evaluate on three representative downstream jobs your memory layer must serve:
   - **Retrieval recall** (analogue of SQuAD F1) — query phrased differently from store, must return correct memory.
   - **Pattern consolidation** (analogue of XSum ROUGE) — produce a one-paragraph summary of N related memories.
   - **Free-form Q&A** (analogue of ELI5) — answer a vague question grounded in memory.
   Build a 6-row × 3-column table. Keep the row whose worst column score is highest — that is your text-infilling-equivalent.

4. **Disable dropout for the final 10% of pretraining**: This is the §5.1 detail. If you skip it, expect ~1–2 points of regression on consolidation quality.

5. **Adapter pattern for new sources**: When a new source format arrives (e.g., calendar events, voice transcripts), do NOT retrain. Instead, freeze the synthesizer and train a small randomly-initialized adapter encoder (BART §3.4 pattern) that maps the new format into your synthesizer's "denoised" canonical token space. Train in two phases: (a) freeze most params, train only the adapter + positional embeddings + first self-attention input projection; (b) unfreeze everything for a small number of steps.

6. **Provenance: log the corruption + the reconstruction + the loss**: BART itself does not address provenance — but as a memory architect you must. Store all three artifacts alongside the original. The loss is your confidence signal; large reconstruction loss = the model couldn't predict its own input = likely a novel/non-canonical memory that deserves a manual review flag. **This is the Ground (G) hook BART doesn't give you for free.**

**Expected outcome:** A write-time synthesis layer where (a) you can switch downstream agent jobs by swapping the fine-tuning head rather than retraining, (b) you have a per-memory confidence signal (reconstruction loss), and (c) new input formats compose in via a small adapter rather than a full retrain. The honest caveat: you have replicated 2019-era pretraining engineering. The lifecycle-management dimensions of memory (eviction, contradiction surfacing, drift detection) are not addressed by BART itself — see "What Experts Overlook" below.

## Best Figure

![Figure 1 — A schematic comparison of BART with BERT and GPT (page 2)](figures/lewis-2019-bart-fig.png)

Image Candidates:
Figure 1 (p. 2): The schematic that names BART's positioning relative to BERT and GPT — single image that explains why BART exists.
Figure 2 (p. 3): Visual summary of the five noising transformations (Token Masking, Token Deletion, Sentence Permutation, Document Rotation, Text Infilling) — the design space of "what to corrupt."
Table 1 (p. 4): The ablation matrix showing BART variants vs. baselines across SQuAD/MNLI/ELI5/XSum/ConvAI2/CNN-DM — quantitative payoff of the design choices Figure 1 implies.

Best Image:
Figure Name: Figure 1: "A schematic comparison of BART with BERT (Devlin et al., 2019) and GPT (Radford et al., 2018)"
Figure Page: 2
Slide Caption: BART positions a bidirectional encoder in front of an autoregressive decoder, generalizing BERT (encode only) and GPT (decode only) into a denoising seq2seq.
Description: Three side-by-side panels. (a) BERT: a bidirectional encoder takes a masked input (`A _ C _ E`) and predicts missing tokens independently — good for understanding, bad for generation. (b) GPT: an autoregressive decoder predicts each token from leftward context (`<s> A B C D` → `A B C D E`) — good for generation, bad at bidirectional understanding. (c) BART: a corrupted input (`A _ B _ E`) goes through a bidirectional encoder, then an autoregressive decoder reconstructs the original `A B C D E` token by token. The figure makes BART's design thesis legible in one glance: it is structurally the union of the previous two, with the corruption function as the design variable that did not exist in either predecessor.

## What Experts Overlook

The detail most experts overlook is not the text-infilling objective (everyone quotes that), but **the asymmetry between what the encoder sees and what the decoder is trained on**. In BART, the encoder sees a corrupted document, but the decoder is *always* trained on the original uncorrupted next-token target. This is the opposite of MASS (where encoder and decoder see disjoint token sets) and UniLM (where masked predictions are conditionally independent). The asymmetry is visible only when you read §7 "Related Work" carefully — Lewis explicitly says "BART reduces the mismatch between pre-training and generation tasks, because the decoder is always trained on un-corrupted context." This single design choice is why BART transfers so well to generation: at inference time the decoder is doing the *same job* it was pretrained to do (predict the next correct token given the previous correct tokens), whereas BERT-family decoders have to bridge from "predict missing token from context" to "generate a coherent sequence."

**Why it matters:** For a memory architect, this is the cleanest argument for **train your synthesizer on the actual output distribution it will produce at query time**. If your write-time consolidator is trained on "fill the gap in a fact" but at query time you ask it to "write a paragraph summarizing five memories," you have a pretraining-generation mismatch that no amount of fine-tuning data fully closes. BART's trick is to make pretraining and generation share the *exact same decoder regime*. The corruption only lives on the encoder side.

**Example of good use:** You are designing a session-summary synthesizer. Instead of pretraining it on "predict the missing sentence in a session," pretrain it on "given a corrupted session (sentences shuffled, some spans masked), reconstruct the original session sentence by sentence in original order." At query time when you ask it to "summarize these five sessions," the decoder is doing the same autoregressive-over-clean-text job it was trained on — just conditioned on different encoder inputs. You get smoother outputs and less mode collapse.

**Example of misapplication:** You read BART's headline result ("+6 ROUGE on XSum from text infilling") and decide to add text infilling as your write-path objective for a fact-store consolidator. You train encoder-side on infilled spans, but your decoder is a separately-trained summarizer that was fine-tuned with teacher forcing on summary-target pairs. At query time the decoder has never seen "smooth autoregressive reconstruction of original document" as its objective — it has only seen "produce a summary." Your reconstructions look fine in isolation but they degrade when you stack them (consolidating consolidations) because each step is slightly off-distribution from the next. The symptom looks like "the synthesizer gets vaguer with each round" and you'll blame the data — but the root cause is that you copied the encoder trick without copying the decoder regime.

## Extracted Prompts

No applicable prompts found in this paper.

(BART is a pretrained model paper — it predates the prompting era. There are no LLM prompt templates in the methodology; the model is conditioned via fine-tuning on labeled data and input-output token sequences, not natural-language prompts.)

## Citations

- Devlin et al., 2019 — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- Liu et al., 2019 — RoBERTa: A Robustly Optimized BERT Pretraining Approach
- Yang et al., 2019 — XLNet: Generalized Autoregressive Pretraining for Language Understanding
- Joshi et al., 2019 — SpanBERT: Improving Pre-training by Representing and Predicting Spans
- Dong et al., 2019 — UniLM: Unified Language Model Pre-training
- Song et al., 2019 — MASS: Masked Sequence to Sequence Pre-training for Language Generation
- Vaswani et al., 2017 — Attention Is All You Need
- Radford et al., 2018 / 2019 — GPT / GPT-2 (Improving Language Understanding by Generative Pre-training; Language Models are Unsupervised Multitask Learners)
- Lample & Conneau, 2019 — Cross-lingual Language Model Pretraining
- Lan et al., 2019 — ALBERT

(Full citations list of 30 entries in the `citations:` frontmatter.)

## Related Digests

- [[devlin-2018-bert]] — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- [[radford-2018-gpt1]] — Improving Language Understanding by Generative Pre-Training
- [[liu-2019-roberta-pretraining]] — RoBERTa: A Robustly Optimized BERT Pretraining Approach
- [[radford-2019-gpt2-multitask]] — Language Models are Unsupervised Multitask Learners (GPT-2)
- [[brown-2020-gpt3-few-shot]] — Language Models are Few-Shot Learners
- [[dai-2015-semi-supervised-sequence-learning]] — Semi-supervised Sequence Learning

## Reviewer Notes

**Overall severity:** Clean

All quantitative claims (+6 ROUGE XSum, +1.1 BLEU WMT16 RO-EN, +1.2 ROUGE-L ELI5, Poisson λ=3, 30% masking, 12+12 layers, hidden=1024, batch 8000, 500k steps, 160GB corpus, SQuAD F1 90.8/77.2/85.4 across infilling/rotation/shuffling, XSum PPL 6.61→17.14, GLUE MNLI 89.9/90.1) verified against Tables 1, 2, 3, 5, 6 and §5.1. Architectural claims (decoder always trained on uncorrupted context; adapter encoder pattern for translation; disable dropout final 10%) verified against §7 Related Work, §3.4, and §5.1 respectively. The ENGRAM-dimension tags and memory-system applications in the Implications and How to Apply It sections are clearly framed as analogical extrapolations rather than paper claims — BART itself addresses only NLP pretraining objectives, not memory-system lifecycle, provenance, or eviction.
