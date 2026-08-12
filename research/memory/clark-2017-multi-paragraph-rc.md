---
corpus: agentic-memory
kind: paper-digest
slug: clark-2017-multi-paragraph-rc
title: "Simple and Effective Multi-Paragraph Reading Comprehension"
authors:
  - "Clark, Christopher"
  - "Gardner, Matt"
year: 2017
publication_date: "2017-11"
venue: "arXiv preprint (later ACL 2018)"
source_url: "https://arxiv.org/abs/1710.10723"
doi: null
arxiv_id: "1710.10723"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Calibrated cross-paragraph confidence is more useful than a sharper paragraph picker — train one paragraph-QA model on multiple paragraphs from the same document with a shared softmax normalization across them, and accuracy keeps climbing as you read more text instead of collapsing."
topics:
  - multi-paragraph-reading-comprehension
  - open-domain-qa
  - confidence-calibration
  - retrieval-then-read
  - distant-supervision
  - shape-of-memory
  - retrieve-aggregate
tags:
  - paper
  - memory-architect
  - engram-retrieve
  - engram-aggregate
  - engram-ground
  - calibration
  - tf-idf
  - bidaf
  - triviaqa
  - squad
entities:
  - clark-christopher
  - gardner-matt
  - allen-institute-for-ai
related_digests:
  - chen-2017-drqa-machine-reading
  - karpukhin-2020-dense-passage-retrieval
  - nogueira-2019-bert-passage-reranking
  - lewis-2020-rag-knowledge-nlp
  - gao-2022-hyde-zero-shot-retrieval
citations:
  - title: "YodaQA: A Modular Question Answering System Pipeline"
    authors: ["Petr Baudiš"]
    year: 2015
    venue: "POSTER 2015 — 19th International Student Conference on Electrical Engineering"
    doi: null
    url: null
    arxiv_id: null
  - title: "Semantic Parsing on Freebase from Question-Answer Pairs"
    authors: ["Jonathan Berant", "Andrew Chou", "Roy Frostig", "et al."]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "ClueWeb09 Data Set"
    authors: ["Jamie Callan", "Mark Hoy", "Changkuk Yoo", "et al."]
    year: 2009
    venue: null
    doi: null
    url: null
    arxiv_id: null
  - title: "Reading Wikipedia to Answer Open-Domain Questions"
    authors: ["Danqi Chen", "Adam Fisch", "Jason Weston", "et al."]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1704.00051"
  - title: "Long Short-Term Memory-Networks for Machine Reading"
    authors: ["Jianpeng Cheng", "Li Dong", "Mirella Lapata"]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1601.06733"
  - title: "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation"
    authors: ["Kyunghyun Cho", "Bart Van Merriënboer", "Caglar Gulcehre", "et al."]
    year: 2014
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1406.1078"
  - title: "Quasar: Datasets for Question Answering by Search and Reading"
    authors: ["Bhuwan Dhingra", "Kathryn Mazaitis", "William W. Cohen"]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1707.03904"
  - title: "A Theoretically Grounded Application of Dropout in Recurrent Neural Networks"
    authors: ["Yarin Gal", "Zoubin Ghahramani"]
    year: 2016
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Teaching Machines to Read and Comprehend"
    authors: ["Karl Moritz Hermann", "Tomas Kocisky", "Edward Grefenstette", "et al."]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "WikiReading: A Novel Large-scale Language Understanding Task over Wikipedia"
    authors: ["Daniel Hewlett", "Alexandre Lacoste", "Llion Jones", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1608.03542"
  - title: "The Goldilocks Principle: Reading Children's Books with Explicit Memory Representations"
    authors: ["Felix Hill", "Antoine Bordes", "Sumit Chopra", "et al."]
    year: 2015
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1511.02301"
  - title: "Mnemonic Reader: Machine Comprehension with Iterative Aligning and Multi-hop Answer Pointing"
    authors: ["Minghao Hu", "Yuxing Peng", "Xipeng Qiu"]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adversarial Examples for Evaluating Reading Comprehension Systems"
    authors: ["Robin Jia", "Percy Liang"]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1707.07328"
  - title: "TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension"
    authors: ["Mandar Joshi", "Eunsol Choi", "Daniel S. Weld", "et al."]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1705.03551"
  - title: "Text Understanding with the Attention Sum Reader Network"
    authors: ["Rudolf Kadlec", "Martin Schmid", "Ondrej Bajgar", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1603.01547"
  - title: "Question Answering through Transfer Learning from Large Fine-grained Supervision Data"
    authors: ["Sewon Min", "Minjoon Seo", "Hannaneh Hajishirzi"]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1702.02171"
  - title: "MS MARCO: A Human Generated Machine Reading Comprehension Dataset"
    authors: ["Tri Nguyen", "Mir Rosenberg", "Xia Song", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1611.09268"
  - title: "MEMEN: Multi-layer Embedding with Memory Networks for Machine Comprehension"
    authors: ["Boyuan Pan", "Hao Li", "Zhou Zhao", "et al."]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1707.09098"
  - title: "GloVe: Global Vectors for Word Representation"
    authors: ["Jeffrey Pennington", "Richard Socher", "Christopher D. Manning"]
    year: 2014
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "SQuAD: 100,000+ Questions for Machine Comprehension of Text"
    authors: ["Pranav Rajpurkar", "Jian Zhang", "Konstantin Lopyrev", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1606.05250"
  - title: "Bidirectional Attention Flow for Machine Comprehension"
    authors: ["Min Joon Seo", "Aniruddha Kembhavi", "Ali Farhadi", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1611.01603"
  - title: "S-Net: From Answer Extraction to Answer Generation for Machine Reading Comprehension"
    authors: ["Chuanqi Tan", "Furu Wei", "Nan Yang", "et al."]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1706.04815"
  - title: "The TREC-8 Question Answering Track Report"
    authors: ["Ellen M. Voorhees", "et al."]
    year: 1999
    venue: "TREC"
    doi: null
    url: null
    arxiv_id: null
  - title: "Machine Comprehension Using Match-LSTM and Answer Pointer"
    authors: ["Shuohang Wang", "Jing Jiang"]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1608.07905"
  - title: "R^3: Reinforced Reader-Ranker for Open-Domain Question Answering"
    authors: ["Shuohang Wang", "Mo Yu", "Xiaoxiao Guo", "et al."]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1709.00023"
  - title: "Gated Self-Matching Networks for Reading Comprehension and Question Answering"
    authors: ["Wenhui Wang", "Nan Yang", "Furu Wei", "et al."]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Dynamic Integration of Background Knowledge in Neural NLU Systems"
    authors: ["Dirk Weissenborn", "Tom Kočiský", "Chris Dyer"]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1706.02596"
  - title: "FastQA: A Simple and Efficient Neural Architecture for Question Answering"
    authors: ["Dirk Weissenborn", "Georg Wiese", "Laura Seiffe"]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1703.04816"
  - title: "ADADELTA: An Adaptive Learning Rate Method"
    authors: ["Matthew D. Zeiler"]
    year: 2012
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1212.5701"
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "Results on TriviaQA web (left) and verified TriviaQA web (right) when applying our models to multiple paragraphs from each document"
  page: 7
  image_path: "figures/clark-2017-multi-paragraph-rc-fig.png"
---

# Simple and Effective Multi-Paragraph Reading Comprehension

**Authors:** Christopher Clark, Matt Gardner
**Published:** 2017-11 · [Source](https://arxiv.org/abs/1710.10723)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Clark and Gardner show that a paragraph-level reading-comprehension model can be turned into a document-level system without redesigning it — the trick is making per-paragraph confidence scores comparable across paragraphs. They train a BiDAF-style model on TriviaQA web (530k question-document pairs, no subsampling) using four ingredients: (1) a TF-IDF cosine paragraph picker that lifts answer-containing paragraph hit-rate from 83.1% to 85.1%; (2) a summed objective that marginalises probability mass over all answer-text occurrences to absorb distant-supervision label noise; (3) sampling paragraphs from the same document during training, including paragraphs that contain no answer; and (4) a "shared-normalization" loss where the softmax denominator is taken across all sampled paragraphs from the same context, so the model is forced to produce globally comparable scores. The result: 71.32 F1 on TriviaQA-web test (a ~15-point absolute gain over the 56.73 F1 prior best, Reading Twice for NLU), 83.70 F1 on the verified subset, and 67.34 F1 on document-level SQuAD vs Chen 2017's 49.7 EM. Without shared-norm, accuracy collapses as you feed in more paragraphs (the base SQuAD model peaks at 2 paragraphs then declines); with shared-norm, accuracy keeps climbing through 15 paragraphs. The actionable takeaway: when scaling read-over-many-chunks systems, calibrating confidence across chunks at training time matters more than retrieving better chunks at query time.

## Key Takeaway

The counter-intuitive lesson is that the bottleneck in multi-paragraph QA wasn't retrieval and wasn't the reader's accuracy on the right paragraph — it was that two independently-trained softmaxes are not on the same scale. The fix isn't a bigger model or a smarter ranker; it's deleting the boundary between paragraphs in the loss function so the model has to compete its own answers against alternatives it never saw at the answer-extraction layer. Stop treating "find the paragraph" and "extract the span" as separable stages — let the model price every candidate against every other candidate in the same document, and accuracy goes up as you give it more text instead of less.

## Implications

- **ENGRAM-R (Retrieve) + ENGRAM-A (Aggregate) are coupled by calibration, not by ranking**: If your agent retrieves N chunks and lets the reader/LLM pick the best answer, the bottleneck is whether confidence is comparable across chunks. A better retriever doesn't fix an over-confident reader. Treat per-chunk confidence calibration as a first-class write-time training concern, not a query-time post-hoc score.
- **Calibration belongs at write time, not query time**: The shared-norm objective is applied during training by including multiple paragraphs from the same document in each mini-batch. The cost is paid once; every query benefits forever. This is the write-time-vs-query-time decision tilted strongly toward write-time synthesis — and the cost is modest (just batch composition).
- **More-text-helps is a property you have to train for**: The "none" baseline on document-level SQuAD peaks at 2 paragraphs and then *loses* F1 as more paragraphs are added (Figure 5). Naive scaling of retrieval depth is actively harmful with a non-calibrated reader. If you're considering "just retrieve more and let the reader pick," validate first that your reader actually gets better with more inputs — most don't.
- **Distant supervision needs a marginal-likelihood loss, not a pick-one-span loss**: The summed objective (Kadlec et al. 2016 style) lets the model distribute probability across all spans matching the answer text, then learn which spans are contextually relevant. On TriviaQA-web this alone adds ~5 F1 (BiDAF+TF-IDF: 59.18 → BiDAF+TF-IDF+sum: 62.44). For memory systems where the same fact appears in many forms, training/extraction losses that marginalise over equivalent expressions will outperform losses that force a single canonical pick.
- **A cheap TF-IDF picker can beat a deep one for the picker role — keep deep models for the reader**: TF-IDF paragraph selection lifted answer-containing-paragraph hit-rate from 83.1% (first-paragraph baseline) to 85.1% — a small lift but free. The 15-point F1 gain came from the reader, not the picker. Don't burn capacity on a learned retriever when a lexical one with good IDF weighting gets you to the long tail of the picker's accuracy curve.
- **Make "no answer" a first-class output**: Adding an explicit no-answer score (z) trained against negative paragraphs is the third-largest single contributor. Memory systems that never let the AI say "this chunk has nothing relevant" will inherit the same over-confidence pathology shown in Table 1 — the model will confabulate a confident wrong answer rather than abstain.
- **The shared-norm trick generalises: any aggregation step where independent scorers feed a single decision needs cross-scorer normalization**: This pattern applies far beyond QA — ensemble agent voting, RAG reranking, multi-source consolidation. If you have N independent extractors each returning a score, those scores are not comparable unless you trained them to be. Either share a softmax denominator at training time or learn a calibration mapping at eval time.
- **Don't optimise the picker against eval — let the reader's confidence do the picking**: The shared-norm model on TriviaQA-web verified gets 83.70 F1 against a human-estimated 75.4% upper bound on which question-document pairs contain sufficient evidence — meaning the model is approaching ceiling. The win came from removing the bottleneck between picker and reader, not from making either component individually stronger.

## How to Apply It (method)

**Scenario:** You are building the retrieval layer for an agentic OS that answers user questions over a memory vault of ~10k markdown notes. The current pipeline retrieves the top-K passages via BM25 and feeds them sequentially to an LLM that picks the answer. Quality plateaus at K=3 and gets *worse* at K=10 — the LLM gets distracted by plausible-sounding but irrelevant passages and the system becomes over-confident on questions it should decline. You want to fix the cross-passage calibration without swapping your retriever.

**Steps:**

1. **Audit the current confidence signal**: Run 50 queries through the existing pipeline. For each, record the LLM's per-passage answer + a self-reported confidence (e.g., a logit or a numeric 0-100 from a follow-up prompt). Compute calibration: does p(correct | confidence > 0.8) actually equal ~0.8? If not, the problem is calibration, not retrieval — proceed.

2. **Build the training set with paragraph batches per question**: For each labelled question in your eval set, pull the top-N passages by BM25 (e.g., N=8) from your memory vault. Mark which passages contain the answer text and which don't — both sets matter. Construct a training batch where every example for a single question contains 2-4 passages from the same query (mix of answer-containing and not).

   ```
   batch = [
     (q1, passage1A_with_answer, span=(t_start, t_end)),
     (q1, passage1B_no_answer,   span=None),
     (q1, passage1C_with_answer, span=(t_start, t_end)),
     (q2, passage2A_with_answer, span=(t_start, t_end)),
     (q2, passage2B_no_answer,   span=None),
     ...
   ]
   ```

3. **Apply a summed objective across answer-text matches** (handles distant supervision noise): If the same answer string appears at multiple positions in a passage, sum probabilities across all of them, then negative-log:

   ```
   loss_span_start_for_passage = - log( sum_{k in answer_positions} exp(s_k)
                                        / sum_{i in all_tokens} exp(s_i) )
   ```

4. **Replace the per-passage softmax with a shared-norm softmax** across passages for the same question. In the loss, the denominator runs over every token in every passage from the same question:

   ```
   p(token a starts answer in passage p | question q)
     = exp(s_{a,p}) / sum_{p' in P(q)} sum_{i in tokens(p')} exp(s_{i,p'})
   ```

   Train with paragraphs grouped by query in each batch so the denominator is computable.

5. **Add an explicit no-answer logit per passage**: Append a single extra score `z` per passage. The objective becomes:

   ```
   loss = - log( ((1 - δ) * exp(z) + δ * sum_correct_spans) / (exp(z) + sum_all_spans) )
   ```
   where `δ=1` if the passage contains an answer and `δ=0` if it doesn't. This gives the model permission to abstain on irrelevant passages instead of confabulating a confident wrong answer.

6. **Sample passages with mild oversampling of answer-containing ones**: Clark and Gardner sampled the top-ranked answer-containing paragraph twice as often as others — a soft curriculum that keeps training tractable while still exposing the model to negative passages. Mirror this in your sampler.

7. **Evaluate the "more text helps" curve**: After training, plot accuracy vs. number of retrieved passages, K, from 1 to 20. The success criterion: accuracy should be monotonically non-decreasing with K, ideally still rising at K=15 (Clark and Gardner's TriviaQA-web shared-norm curve, Figure 3). If accuracy still peaks and decays, calibration is incomplete — re-examine batch construction.

8. **At query time, run the trained reader on the top-K passages independently and take the highest-scored span across all passages**. No reranker required — the reader's scores are now comparable by construction.

**Expected outcome:** A memory-vault QA system where retrieving more passages strictly helps and where the system can refuse to answer when no retrieved passage carries the answer. You'll have moved confidence calibration from a brittle query-time post-hoc step (rerankers, ensembles) into the loss function, paying the cost once at training and getting a system that scales gracefully with retrieval depth.

## Best Figure

![Figure 3 — Results on TriviaQA web (left) and verified TriviaQA web (right) (page 7)](figures/clark-2017-multi-paragraph-rc-fig.png)

**Image Candidates:**

- Figure 3 (p. 7): Side-by-side F1-vs-number-of-paragraphs plots on TriviaQA web and verified subset, contrasting all five training methods — the clearest visualization that shared-norm uniquely keeps improving with more paragraphs while alternatives plateau or regress.
- Figure 5 (p. 8): SQuAD-document F1 vs paragraphs — most dramatic single chart because the "none" baseline visibly loses performance after 2 paragraphs while shared-norm climbs to 15.
- Table 2 (p. 6): Cumulative ablation showing each pipelined-method ingredient's marginal contribution (47.40 → 66.04 EM), which is the strongest support for the "every piece matters" story.

**Best Image:**

- **Figure Name:** Figure 3 — "Results on TriviaQA web (left) and verified TriviaQA web (right) when applying our models to multiple paragraphs from each document"
- **Figure Page:** 7
- **Slide Caption:** Shared-norm is the only training method that keeps F1 rising as more paragraphs are added — alternatives plateau by ~5 paragraphs.
- **Description:** Two line plots (TriviaQA web and verified TriviaQA web) showing F1 score on the y-axis vs number of paragraphs (1-15) on the x-axis. Five lines compare training methods: none (baseline, no confidence training), sigmoid, merge, no-answer, and shared-norm. On the general set, shared-norm and merge are tied at the top (~0.70 F1) and both clearly above none and sigmoid (~0.66-0.67). On the verified set the separation is sharper: shared-norm climbs to ~0.83 F1 while merge and no-answer plateau near ~0.80 and sigmoid collapses. The figure is the paper's main result graphic — it shows in one view that the confidence-calibration trick produces a qualitatively different scaling property: shared-norm gets *better* with more text while every alternative either plateaus or regresses.

## What Experts Overlook

The shared-norm objective is almost always cited as "share the softmax denominator across paragraphs," but the load-bearing detail is *how* the multiple paragraphs are gathered into a single training batch. Clark and Gardner explicitly construct batches where multiple paragraphs from the same question-document pair appear together, with at least one answer-containing and at least one non-answer paragraph (Section 4.3, "Sampling"). Without that batch composition, the shared softmax is mathematically a no-op — the denominator only crosses paragraphs if those paragraphs are in the same forward pass. The shared-norm idea is two-thirds in the loss function and one-third in the dataloader; if you only port the loss, your model trains as if shared-norm were just a different normalisation constant per example.

**Why it matters:** This reveals that calibration training is fundamentally a *negative-sampling* discipline disguised as a loss-function tweak. The model only learns "this paragraph is less relevant than that one" if it sees them simultaneously. This generalises to any memory system trying to learn cross-chunk relevance: your training data structure (which chunks co-occur in a single training example) silently determines what the model can express opinions about. Cross-document calibration requires cross-document batching; cross-vault calibration requires cross-vault batching. Many systems try to learn relevance with single-document batches and then wonder why scores don't transfer.

**Example of good use:** You're training a personal knowledge-base extractor that decides which of several candidate memories to surface in response to a query. You compose batches where, for each query, you pack the top-K candidate memories from BM25 — both relevant and irrelevant — into the same forward pass and apply a shared-norm softmax across them. The extractor learns "this memory is less relevant than that one given this query" at training time, so at inference you can rank K=20 memories without re-ranking and trust the relative scores.

**Example of misapplication:** You read "shared-norm objective" as a loss-function change and apply it without changing your dataloader. Your batches still pair (query, single-memory-chunk) one at a time. The shared softmax denominator now spans only the tokens within that single chunk — mathematically equivalent to a regular per-chunk softmax. Training looks normal, loss decreases, evaluation on single-chunk QA looks fine — and then in production with K=10 retrieval, the model is just as miscalibrated as the baseline, because it was never asked to compare chunks against each other during training.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- **Reading Wikipedia to Answer Open-Domain Questions** — Chen et al. 2017 (`arXiv:1704.00051`)
- **TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension** — Joshi et al. 2017 (`arXiv:1705.03551`)
- **Bidirectional Attention Flow for Machine Comprehension** — Seo et al. 2016 (`arXiv:1611.01603`)
- **SQuAD: 100,000+ Questions for Machine Comprehension of Text** — Rajpurkar et al. 2016 (`arXiv:1606.05250`)
- **Text Understanding with the Attention Sum Reader Network** — Kadlec et al. 2016 (`arXiv:1603.01547`)
- **Adversarial Examples for Evaluating Reading Comprehension Systems** — Jia & Liang 2017 (`arXiv:1707.07328`)
- **A Theoretically Grounded Application of Dropout in Recurrent Neural Networks** — Gal & Ghahramani 2016
- **R^3: Reinforced Reader-Ranker for Open-Domain Question Answering** — Wang et al. 2017a (`arXiv:1709.00023`)
- **Long Short-Term Memory-Networks for Machine Reading (self-attention)** — Cheng et al. 2016 (`arXiv:1601.06733`)
- **Mnemonic Reader: Machine Comprehension with Iterative Aligning and Multi-hop Answer Pointing** — Hu et al. 2017

_29 total citations — full structured list in frontmatter._

## Related Digests

- [[chen-2017-drqa-machine-reading]] — Reading Wikipedia to Answer Open-Domain Questions (DrQA) — the contemporaneous open-domain QA pipeline that this paper directly improves on; Clark & Gardner beat Chen et al.'s 49.7 EM on document-level SQuAD with 59.14 EM by adding cross-paragraph calibration.
- [[karpukhin-2020-dense-passage-retrieval]] — Dense Passage Retrieval for Open-Domain Question Answering — the next-generation answer to "TF-IDF is good enough"; uses a learned dense retriever instead of TF-IDF and reorders the reader/retriever responsibilities.
- [[nogueira-2019-bert-passage-reranking]] — Passage Re-ranking with BERT — the BERT-era successor to the picker problem; trades off the shared-norm trick for an explicit cross-encoder reranker.
- [[lewis-2020-rag-knowledge-nlp]] — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks — generalises the retrieve-then-read pipeline this paper formalises into a generative setting.
- [[gao-2022-hyde-zero-shot-retrieval]] — Precise Zero-Shot Dense Retrieval without Relevance Labels — works the same retrieval problem from the opposite angle: rewrite the query to match the doc embedding space, instead of rewriting the reader to calibrate across docs.

## Reviewer Notes

**Overall severity:** Clean

Every numeric claim was cross-checked against the paper text:
- 71.3 F1 on TriviaQA-web test → Abstract + Table 3 (71.32).
- 56.7 F1 prior best → Abstract + Table 3 ("Reading Twice for NLU" 56.73).
- 83.7 F1 verified subset → Table 3 (83.70).
- TF-IDF lift 83.1% → 85.1% → Section 2.1.
- BiDAF+TF-IDF 59.18 EM-numbers in Table 2 confirmed (note Table 2's "59.18" is F1; EM is 53.41 — checked the digest only references the F1 numbers).
- SQuAD document-level 67.34 F1 vs Chen 2017 49.7 EM → Section 5.3 final paragraph.
- 530k training pairs → Section 4.2.
- "none" SQuAD curve peaks at 2 paragraphs and declines → Figure 5 caption explicitly states this.
- Shared-norm verified set climbs to ~0.83 F1 at 15 paragraphs → Figure 3 right panel.
- Sample paragraph 2× oversampling → Section 4.3.
- Summed objective lift on TriviaQA-web (BiDAF+TF-IDF: 59.18 → BiDAF+TF-IDF+sum: 62.44) → Table 2 F1 column.

The shared-norm-requires-cross-paragraph-batching observation in "What Experts Overlook" is grounded in Section 4.3 ("we train on this objective by including multiple paragraphs from the same context in each mini-batch") combined with Section 3.1 (mathematical statement of the loss). The framing is interpretive — calling out the dataloader dependency — but the underlying mechanic is the paper's stated method.

The 75.4% human upper-bound figure attributed to Joshi et al. 2017 (cited in the paper's Section 5.1) is reported here as "~75.4% of the question-document pairs contain sufficient evidence" — matches Section 5.1 wording.

No fabricated metrics, no invented method names, no overextended claims beyond what the paper measures.
