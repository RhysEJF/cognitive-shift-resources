---
corpus: agentic-memory
kind: paper-digest
slug: dai-2015-semi-supervised-sequence-learning
title: "Semi-supervised Sequence Learning"
authors:
  - "Dai, Andrew M."
  - "Le, Quoc V."
year: 2015
publication_date: "2015-11"
venue: "NeurIPS (NIPS 2015)"
source_url: "https://arxiv.org/abs/1511.01432"
doi: null
arxiv_id: "1511.01432"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "The fastest way to make a recurrent network 'remember' a long document is not to invent a better memory module — it is to first teach the network to literally regurgitate the document via an unsupervised autoencoder, then fine-tune for the task; the autoencoder's reconstruction objective stabilises training and turns previously untrainable long-context LSTMs into competitive classifiers."
topics:
  - sequence-learning
  - semi-supervised-learning
  - pretraining
  - lstm
  - autoencoder
  - language-model
  - representation-learning
tags:
  - paper
  - foundational
  - encode-aggregate
  - write-time-synthesis
  - unsupervised-pretraining
entities:
  - dai-andrew
  - le-quoc
related_digests:
  - radford-2018-gpt1
  - devlin-2018-bert
  - lewis-2019-bart
  - hochreiter-1997-lstm
  - bahdanau-2015-attention-align-translate
citations:
  - title: "A framework for learning predictive structures from multiple tasks and unlabeled data"
    authors: ["Rie Kubota Ando", "Tong Zhang"]
    year: 2005
    venue: "Journal of Machine Learning Research"
    doi: null
    url: null
    arxiv_id: null
  - title: "Datasets for single-label text categorization"
    authors: ["Ana Cardoso-Cachopo"]
    year: 2015
    venue: "online"
    doi: null
    url: "http://web.ist.utl.pt/acardoso/datasets/"
    arxiv_id: null
  - title: "Listen, attend and spell"
    authors: ["William Chan", "Navdeep Jaitly", "Quoc V. Le", "et al."]
    year: 2015
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1508.01211"
  - title: "End-to-end continuous speech recognition using attention-based recurrent nn: First results"
    authors: ["Jan Chorowski", "Dzmitry Bahdanau", "Kyunghyun Cho", "et al."]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1412.1602"
  - title: "Stochastic ratio matching of RBMs for sparse high-dimensional inputs"
    authors: ["Yann Dauphin", "Yoshua Bengio"]
    year: 2013
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to forget: Continual prediction with LSTM"
    authors: ["Felix A. Gers", "Jurgen Schmidhuber", "Fred Cummins"]
    year: 2000
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "LSTM: A search space odyssey"
    authors: ["Klaus Greff", "Rupesh K. Srivastava", "Jan Koutnik", "et al."]
    year: 2015
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Gradient flow in recurrent nets: the difficulty of learning long-term dependencies"
    authors: ["Sepp Hochreiter", "Yoshua Bengio", "Paolo Frasconi", "et al."]
    year: 2001
    venue: "A Field Guide to Dynamical Recurrent Neural Networks"
    doi: null
    url: null
    arxiv_id: null
  - title: "Long short-term memory"
    authors: ["Sepp Hochreiter", "Jurgen Schmidhuber"]
    year: 1997
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "On using very large target vocabulary for neural machine translation"
    authors: ["Sebastien Jean", "Kyunghyun Cho", "Roland Memisevic", "et al."]
    year: 2014
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Effective use of word order for text categorization with convolutional neural networks"
    authors: ["Rie Johnson", "Tong Zhang"]
    year: 2014
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Convolutional neural networks for sentence classification"
    authors: ["Yoon Kim"]
    year: 2014
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Skip-thought vectors"
    authors: ["Ryan Kiros", "Yukun Zhu", "Ruslan Salakhutdinov", "et al."]
    year: 2015
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Convolutional deep belief networks on CIFAR-10"
    authors: ["Alex Krizhevsky"]
    year: 2010
    venue: "Technical report, University of Toronto"
    doi: null
    url: null
    arxiv_id: null
  - title: "Imagenet classification with deep convolutional neural networks"
    authors: ["Alex Krizhevsky", "Ilya Sutskever", "Geoffrey E. Hinton"]
    year: 2012
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Newsweeder: Learning to filter netnews"
    authors: ["Ken Lang"]
    year: 1995
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning algorithms for the classification restricted boltzmann machine"
    authors: ["Hugo Larochelle", "Michael Mandel", "Razvan Pascanu", "et al."]
    year: 2012
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Distributed representations of sentences and documents"
    authors: ["Quoc V. Le", "Tomas Mikolov"]
    year: 2014
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "DBpedia – a large-scale, multilingual knowledge base extracted from wikipedia"
    authors: ["Jens Lehmann", "Robert Isele", "Max Jakob", "et al."]
    year: 2014
    venue: "Semantic Web"
    doi: null
    url: null
    arxiv_id: null
  - title: "Addressing the rare word problem in neural machine translation"
    authors: ["Thang Luong", "Ilya Sutskever", "Quoc V. Le", "et al."]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1410.8206"
  - title: "Learning word vectors for sentiment analysis"
    authors: ["Andrew L. Maas", "Raymond E. Daly", "Peter T. Pham", "et al."]
    year: 2011
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Hidden factors and hidden topics: understanding rating dimensions with review text"
    authors: ["Julian McAuley", "Jure Leskovec"]
    year: 2013
    venue: "RecSys"
    doi: null
    url: null
    arxiv_id: null
  - title: "Recurrent neural network based language model"
    authors: ["Tomas Mikolov", "Martin Karafiat", "Lukas Burget", "et al."]
    year: 2010
    venue: "INTERSPEECH"
    doi: null
    url: null
    arxiv_id: null
  - title: "Beyond short snippets: Deep networks for video classification"
    authors: ["Joe Yue-Hei Ng", "Matthew J. Hausknecht", "Sudheendra Vijayanarasimhan", "et al."]
    year: 2015
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales"
    authors: ["Bo Pang", "Lillian Lee"]
    year: 2005
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning representations by back-propagating errors"
    authors: ["David Rumelhart", "Geoffrey E. Hinton", "Ronald J. Williams"]
    year: 1986
    venue: "Nature"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neural responding machine for short-text conversation"
    authors: ["Lifeng Shang", "Zhengdong Lu", "Hang Li"]
    year: 2015
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Semantic compositionality through recursive matrix-vector spaces"
    authors: ["Richard Socher", "Brody Huval", "Christopher D. Manning", "et al."]
    year: 2012
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Recursive deep models for semantic compositionality over a sentiment treebank"
    authors: ["Richard Socher", "Alex Perelygin", "Jean Y. Wu", "et al."]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Unsupervised learning of video representations using LSTMs"
    authors: ["Nitish Srivastava", "Elman Mansimov", "Ruslan Salakhutdinov"]
    year: 2015
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sequence to sequence learning with neural networks"
    authors: ["Ilya Sutskever", "Oriol Vinyals", "Quoc V. Le"]
    year: 2014
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Grammar as a foreign language"
    authors: ["Oriol Vinyals", "Lukasz Kaiser", "Terry Koo", "et al."]
    year: 2015
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "A neural conversational model"
    authors: ["Oriol Vinyals", "Quoc V. Le"]
    year: 2015
    venue: "ICML Deep Learning Workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "Show and tell: A neural image caption generator"
    authors: ["Oriol Vinyals", "Alexander Toshev", "Samy Bengio", "et al."]
    year: 2014
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Baselines and bigrams: Simple, good sentiment and topic classification"
    authors: ["Sida I. Wang", "Christopher D. Manning"]
    year: 2012
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Beyond regression: New tools for prediction and analysis in the behavioral sciences"
    authors: ["Paul J. Werbos"]
    year: 1974
    venue: "PhD thesis, Harvard"
    doi: null
    url: null
    arxiv_id: null
  - title: "Recurrent neural network regularization"
    authors: ["Wojciech Zaremba", "Ilya Sutskever", "Oriol Vinyals"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1409.2329"
  - title: "Character-level convolutional networks for text classification"
    authors: ["Xiang Zhang", "Yann LeCun"]
    year: 2015
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "The sequence autoencoder for the sequence 'WXYZ'"
  page: 2
  image_path: "figures/dai-2015-semi-supervised-sequence-learning-fig.png"
---

# Semi-supervised Sequence Learning

**Authors:** Andrew M. Dai, Quoc V. Le (Google Inc.)
**Published:** 2015-11 · [Source](https://arxiv.org/abs/1511.01432)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Dai & Le show that pre-training an LSTM on unlabelled text with two simple unsupervised objectives — a next-token language model (LM-LSTM) or a sequence autoencoder that reads a document into a hidden state and reconstructs it (SA-LSTM, Figure 1) — dramatically stabilises subsequent supervised training and unlocks longer-context recurrent models. Trained for ~500K steps with batch 128, then fine-tuned, SA-LSTMs match or beat prior best on five benchmarks: IMDB sentiment 7.24% (vs Paragraph Vectors 7.42%), Rotten Tomatoes 16.7% with 7.9M Amazon-review pre-training data (vs CNN-non-static 18.5%), 20 Newsgroups 15.6% (vs SVM+BoW 17.1%), DBpedia character-level 1.19% with 3-layer SA-LSTM + linear gain (vs Large ConvNet 1.73%), and on CIFAR-10 a 2-layer LM-LSTM hits 18.0% beating Convolutional DBNs at 21.1%. The headline finding for transfer: adding 7.9M unlabelled Amazon movie reviews to the SA pre-training drops Rotten Tomatoes error from 20.5% to 16.7% — roughly equivalent to the gain that competing methods got from 215,154 additional hand-labelled phrases. The actionable takeaway: in a long-context recurrent system, the cheap unsupervised "reconstruct what you just read" step is the load-bearing trick — it both initialises good representations and gives gradients short-cut paths that prevent the optimisation blow-ups that previously made LSTMs unusable on long documents.

## Key Takeaway

The fastest way to make a recurrent network "remember" a long document is not to invent a better memory module — it is to first teach the network to literally regurgitate the document via an unsupervised autoencoder, then fine-tune for the task. The autoencoder's reconstruction objective is dumb on the surface (predict what you just saw) but it forces the hidden state to actually compress the input, and the resulting weights are so much easier to optimise that previously-untrainable long-context LSTMs become competitive — and adding unlabelled text from a *related* domain (Amazon reviews → Rotten Tomatoes) buys you accuracy that previously cost six-figure labelling budgets.

## Implications

- **Treat write-time reconstruction as a first-class memory primitive (ENGRAM: E + A)**: The single biggest stabiliser in this paper is forcing the encoder to *reconstruct* what it read before it's ever asked to classify. For a memory-OS, this is the analogue of distilling each captured session into a structured re-statement on the write path — the act of compression itself is the value, separate from any downstream query. The paper's evidence: SA-LSTM lets you grow hidden state / backprop horizon without the objective exploding (§4.1).
- **Domain-matched unlabelled corpora beat hand-labelled in-domain data (ENGRAM: E)**: Pre-training the SA on 7.9M Amazon movie reviews — a *neighbouring* corpus, not the target one — improved Rotten Tomatoes from 20.5% → 16.7%, comparable to the gain Socher et al. got from 215,154 newly-labelled phrases (Table 5). For memory architects, this argues for sweeping a wide "adjacent" capture net (sibling project notes, related domains) into the consolidation pass rather than hoarding only target-task examples.
- **Pure next-token prediction is structurally weaker than reconstruction for long-context recall (ENGRAM: A)**: LM-LSTM matched SA-LSTM on short tasks (Rotten Tomatoes 21.7% vs SA 20.3%) but lagged on long-document tasks like IMDB (LM 7.64% vs SA 7.24%). The authors' explanation: language modelling is a short-horizon objective so the hidden state only learns to predict the next few words; the autoencoder forces it to retain the *whole* document. For agentic memory pipelines, this is the case for whole-session summarisation objectives over greedy local prediction.
- **Stability before scale (ENGRAM: M)**: Without SA pre-training, scaling hidden units or backprop steps on long documents caused the loss to "explode even with careful tuning of gradient clipping" (§4.1). A memory system that grows its context window or chunk size without an equivalent stabilisation primitive will hit the same wall. Build the reconstruction warm-up before you build the scale-up.
- **Joint training underperforms two-stage pre-train-then-fine-tune (ENGRAM: A + M)**: SA-LSTM with joint training scored 14.7% on IMDB, much worse than pre-train-then-fine-tune at 7.24% (Table 2). For consolidation pipelines this is a clean warning: trying to learn the structured representation *and* the downstream task simultaneously degrades both. Separate the consolidation pass from the query-serving pass.
- **Linear label gain is a cheap gradient-injection trick for very long sequences (ENGRAM: R)**: On 13K-character DBpedia documents, putting the label at every timestep with linearly-increasing weight (Section 3) lifted plain LSTM from 13.64% → 1.32% error — competitive with a 3-layer SA-LSTM. For retrieval over very long memory windows, this argues for emitting intermediate supervision signals along the chunk sequence rather than waiting for the end.
- **The result generalises beyond text — modality is not the bottleneck (ENGRAM: E)**: A 2-layer LM-LSTM trained to predict the next *row of pixels* in a CIFAR-10 image hit 18.0% test error, beating both the non-pretrained LSTM (26.0%) and a Convolutional DBN (21.1%). The implication for memory architects: reconstruction-pretraining as an encoding strategy is not a NLP trick — it's a representation-learning prior that travels to any sequence-shaped input (audio, screen-frames, sensor streams).
- **Don't bypass the reconstruction stage with off-the-shelf embeddings (ENGRAM: E + G)**: Initialising with word2vec embeddings gave only a 0.5% gain on Rotten Tomatoes vs random init, while sequence-autoencoder pre-training gave ~4% — because the recurrent weights, not just token-level embeddings, are what carry the work. Pure RAG-style "drop in better embeddings" is the equivalent shortcut in modern memory systems and is likely to under-deliver for the same reason: representational lift is in the *recurrent* (sequence-aggregating) layer, not the token layer.

## How to Apply It (method)

**Scenario:** You're a memory architect for an agentic OS. Each user has a personal log of ~50K daily captures (Slack messages, browser history, voice notes) plus 5K hand-labelled "important" events. You want a retrieval re-ranker that, given a query, returns the most relevant prior captures. Your re-ranker is a small recurrent model that consumes the candidate event sequence and outputs a relevance score. Direct supervised training on the 5K labelled set overfits badly and fails on long sessions. This paper's method gives you a recipe for unsupervised pre-training on the unlabelled 50K so the supervised step actually works.

**Steps:**

1. **Choose your unsupervised objective**: Pick *sequence autoencoder* (SA) for long captures (paragraph-length notes, long Slack threads) because it forces the hidden state to compress the *entire* sequence. Pick *language model* (LM) for short captures where next-token prediction is enough. If you only have one model, use SA — it dominates on long inputs (IMDB: 7.24% vs LM 7.64%).

2. **Tokenise consistently across labelled and unlabelled data**: Same tokeniser, same vocabulary. The paper treats punctuation as separate tokens, drops words appearing only once, and uses no stemming. Match this — vocabulary mismatches between pre-train and fine-tune destroy the benefit.

3. **Configure the SA encoder-decoder with weight-tying**: Build an LSTM where the decoder shares weights with the encoder. Add an `<eos>` token to the end of each input. The decoder starts reconstructing *after* `<eos>` (see Figure 1). Standard LSTM gates (input/forget/output), 1,024 cell units, 512-dim input embedding worked for IMDB.

4. **Run unsupervised pre-training**: Train for ~500K steps at batch size 128 on the unlabelled 50K captures, clipping cell outputs and gradients per Sutskever et al. (2014). Truncate backprop at 400 timesteps from the *end* of each sequence (this is the only concession to GPU memory — don't truncate the input itself).

   ```
   Loss = sum over t of CE( decoder_output_t , input_t )
   subject to: decoder shares weights with encoder
              decoder is initialised from final encoder hidden state
              truncated BPTT = 400 steps
   ```

5. **Initialise the supervised re-ranker from SA weights**: Copy *both* the word-embedding matrix and the LSTM recurrent weights into the supervised re-ranker. Add a single 512-unit hidden layer + classifier head on top of the final LSTM state.

6. **Fine-tune on the 5K labelled set with aggressive dropout**: Use input-embedding dropout (the paper used 80% on IMDB — yes, eighty) and a 50% dropout between the last hidden state and the classifier. Use early stopping on a held-out validation slice (the paper used 15% of training). Choose dropout rates on the validation set, not the test set.

7. **(Optional) Add linear label gain for very long captures**: If your captures routinely exceed a few thousand tokens, emit a relevance score at every timestep and weight the prediction loss linearly from 0 (start) to 1 (end). On 13K-char DBpedia this took plain LSTM from 13.64% → 1.32% error. Skip this for shorter inputs — it didn't help on IMDB.

8. **Do NOT do joint training**: Don't try to optimise the SA reconstruction loss and the supervised re-ranker loss simultaneously. The paper tested this; SA-LSTM with joint training scored 14.70% on IMDB vs 7.24% for two-stage. Keep the consolidation pass and the query-serving pass on separate schedules.

**Expected outcome:** A re-ranker that trains stably on long captures (no more loss explosions when you widen the model or extend backprop), generalises better than random-init or word2vec-init baselines, and — crucially — gets *better* as you sweep more unrelated-but-domain-adjacent captures into the unsupervised pre-training pool. Your evaluation should show three things: (1) lower validation error than the supervised-only baseline, (2) lower variance across hyperparameter sweeps, (3) monotonic improvement as you add more unlabelled data, mirroring the Rotten Tomatoes IMDB→Amazon progression (20.5% → 18.6% → 16.7%).

## Best Figure

![Figure 1 — The sequence autoencoder for the sequence "WXYZ" (page 2)](figures/dai-2015-semi-supervised-sequence-learning-fig.png)

Image Candidates:
Figure 1 (p. 2): Single-view diagram of the sequence autoencoder reading "WXYZ" into a hidden state and decoding it back — the whole architectural argument in one picture.
Table 1 (p. 3): Summary table contrasting SA-LSTM error vs previous best on all four text benchmarks — the headline results compressed to one view.
Table 4 (p. 5): Rotten Tomatoes results showing the additive lift from adding unlabelled IMDB then Amazon data — the cleanest demonstration that unlabelled scale buys accuracy.

Best Image:
Figure Name: Figure 1: "The sequence autoencoder for the sequence 'WXYZ'"
Figure Page: 2
Slide Caption: A weight-tied LSTM reads "W X Y Z `<eos>`" into a hidden state, then reconstructs the same sequence — the unsupervised objective that stabilises subsequent supervised training.
Description: Figure 1 shows the sequence autoencoder architecture in a single horizontal RNN unrolling. The left half (input side) consumes tokens W, X, Y, Z, `<eos>` one timestep at a time; the right half (output side) re-emits W, X, Y, Z conditioned on the final hidden state and the previous output. The encoder and decoder share the same weights. The diagram is the entire architectural claim of the paper compressed to one image: there is no special memory module, no attention, no copy mechanism — just an LSTM trained to reconstruct its input, then re-used as the initialisation for a downstream classifier. The figure matters because it makes visible why this is a stable training signal: every output has a clear target (the input itself), gradients have short paths back to the embedding, and the hidden state is structurally forced to compress the whole input rather than just predict the next token.

## What Experts Overlook

The non-obvious load-bearing detail is **weight tying between encoder and decoder** (mentioned almost in passing in §2: "the weights for the decoder network and the encoder network are the same"). Most readers see "autoencoder" and assume two networks; the paper actually trains *one* set of weights to do both the compress and the decompress. This means the optimisation is not learning two transforms that happen to compose to identity — it's learning a *single* representation that has to be reversible. That reversibility constraint is what produces the stability: the hidden state cannot afford to be a lossy task-specific summary, because it must also be a faithful enough record to reconstruct from. When you then fine-tune for classification, you're starting from weights that have already proven they can hold the whole document — so the supervised gradient just needs to *re-weight* the existing information rather than re-discover it.

**Why it matters:** This collapses what looks like "more parameters" into "more constraint." A two-stage encoder→decoder with independent weights would have twice the capacity but only half the inductive bias. Weight-tying turns the autoencoder into a self-consistency check on the encoder. For memory architects, this is the difference between *summarisation* (one pass, no verifiability) and *reconstructable summarisation* (compression that can be inverted back to source). The latter is much harder to fool into smoothing-away contradictions because the loss explicitly penalises information loss.

**Example of good use:** A memory-OS write-time pipeline could tie the parameters of its "distil-this-session-into-structured-memory" model with those of its "reconstruct-the-session-from-the-structured-memory" model. The reconstructability constraint becomes a provenance signal (ENGRAM: G) — any memory whose reconstruction loss exceeds a threshold gets flagged for human review or stored with its raw source rather than the distillation. The compression itself carries a self-audit.

**Example of misapplication:** If you train the distil and the reconstruct heads with *independent* weights, you get what looks like an autoencoder loss but you've actually built a system that can learn to round-trip *via the loss-encoded side channel* — the decoder learns to invert the encoder's idiosyncrasies rather than the source semantics. You'll get low reconstruction loss but the encoder representation will be useless for any downstream task. Concrete failure: a session summariser that produces beautiful summaries but, when fine-tuned on "find me the session where I decided X," is no better than random — because the representation was never forced to be a *general* compression, only a private code the paired decoder could undo. Tied weights prevent this.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- Sutskever, Vinyals & Le (2014) — *Sequence to sequence learning with neural networks*, NIPS — the seq2seq foundation the autoencoder is built on.
- Hochreiter & Schmidhuber (1997) — *Long short-term memory*, Neural Computation — the LSTM cell itself.
- Kiros et al. (2015) — *Skip-thought vectors*, NIPS — the closest contemporary unsupervised sentence-representation method; the paper positions SA as easier to fine-tune.
- Le & Mikolov (2014) — *Distributed representations of sentences and documents*, ICML — Paragraph Vectors, the IMDB SOTA the paper beats.
- Maas et al. (2011) — *Learning word vectors for sentiment analysis*, ACL — source of the IMDB benchmark.
- Pang & Lee (2005) — *Seeing stars*, ACL — Rotten Tomatoes dataset.
- Lehmann et al. (2014) — *DBpedia*, Semantic Web — DBpedia ontology/dataset.
- Zhang & LeCun (2015) — *Character-level convolutional networks for text classification*, NIPS — DBpedia ConvNet baseline.
- Socher et al. (2013) — *Recursive deep models for semantic compositionality over a sentiment treebank*, EMNLP — the labelled-data comparison point for Rotten Tomatoes.
- Mikolov et al. (2010) — *Recurrent neural network based language model*, INTERSPEECH — the LM-LSTM ancestor.

(Full structured citation list of 38 references in frontmatter.)

## Related Digests

- [[radford-2018-gpt1]] — Improving Language Understanding by Generative Pre-Training (the direct heir: same pre-train-then-fine-tune recipe, swapped LSTM for Transformer decoder, scaled the unsupervised corpus)
- [[devlin-2018-bert]] — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (extends the reconstruction idea from sequence-autoencoder to masked-token denoising)
- [[lewis-2019-bart]] — BART: Denoising Sequence-to-Sequence Pre-training (the modern descendant of the sequence-autoencoder objective with corruption schedules)
- [[hochreiter-1997-lstm]] — Long Short-Term Memory (the underlying cell architecture this paper stabilises via pretraining)
- [[bahdanau-2015-attention-align-translate]] — Neural Machine Translation by Jointly Learning to Align and Translate (contemporary seq2seq encoder-decoder design, parallel approach to long-context recurrent learning)

## Reviewer Notes

**Overall severity:** Clean — every claim in the digest above is grounded in the paper text. Specifically verified: (a) all error rates in TLDR match Tables 1, 2, 4, 7, 8; (b) "215,154 phrases" and "7.9M Amazon reviews" numbers match §4.2 and footnote 3; (c) "500K steps with batch 128" matches §4; (d) "80% input embedding dropout on IMDB" matches §4.1; (e) "joint training scored 14.7%" matches Table 2; (f) "linear gain DBpedia 1.32%" matches Table 7; (g) "CIFAR-10 2-layer LM-LSTM 18.0%" matches Table 8; (h) weight-tying claim verified at §2 "the weights for the decoder network and the encoder network are the same"; (i) "next row of pixels" CIFAR setup verified at §4.5. No fabricated experiments, models, or metrics.
