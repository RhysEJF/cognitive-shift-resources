---
corpus: agentic-memory
kind: paper-digest
slug: bajaj-2016-ms-marco
title: "MS MARCO: A Human Generated MAchine Reading COmprehension Dataset"
authors:
  - "Bajaj, Payal"
  - "Campos, Daniel"
  - "Craswell, Nick"
  - "Deng, Li"
  - "Gao, Jianfeng"
  - "Liu, Xiaodong"
  - "Majumder, Rangan"
  - "McNamara, Andrew"
  - "Mitra, Bhaskar"
  - "Nguyen, Tri"
  - "Rosenberg, Mir"
  - "Song, Xia"
  - "Stoica, Alina"
  - "Tiwary, Saurabh"
  - "Wang, Tong"
year: 2016
publication_date: "2016-11"
venue: "NIPS 2016 (workshop) — arXiv preprint (v3 2018-10)"
source_url: "https://arxiv.org/abs/1611.09268"
doi: null
arxiv_id: "1611.09268"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Real query-log questions + multi-passage retrieval + free-form human-written answers create a fundamentally harder, more realistic memory-retrieval benchmark than span-extraction datasets like SQuAD — and the resulting passage-ranking subset became the de-facto evaluation substrate for nearly every modern dense-retriever, cross-encoder, and RAG component (BM25 baseline, ~1000 passages re-rank per query, 1M queries / 8.8M passages)."
topics:
  - machine-reading-comprehension
  - question-answering
  - passage-ranking
  - retrieval-benchmark
  - dataset
  - bing-query-logs
  - neural-information-retrieval
tags:
  - paper
  - benchmark
  - dataset
  - retrieval
  - encode-dimension
  - ground-dimension
  - retrieve-dimension
entities:
  - bajaj-payal
  - craswell-nick
  - mitra-bhaskar
  - gao-jianfeng
  - microsoft-research
  - trec-deep-learning-track
related_digests:
  - nogueira-2019-bert-passage-reranking
  - karpukhin-2020-dense-passage-retrieval
  - chen-2017-drqa-machine-reading
  - lewis-2020-rag-knowledge-nlp
  - gao-2022-hyde-zero-shot-retrieval
citations:
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["Dzmitry Bahdanau", "Kyunghyun Cho", "Yoshua Bengio"]
    year: 2014
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1409.0473"
    arxiv_id: "1409.0473"
  - title: "Meteor: An automatic metric for MT evaluation with improved correlation with human judgments"
    authors: ["Satanjeev Banerjee", "Alon Lavie"]
    year: 2005
    venue: "ACL workshop on intrinsic and extrinsic evaluation measures"
    doi: null
    url: null
    arxiv_id: null
  - title: "Long short-term memory-networks for machine reading"
    authors: ["Jianpeng Cheng", "Li Dong", "Mirella Lapata"]
    year: 2016
    venue: "CoRR"
    doi: null
    url: "http://arxiv.org/abs/1601.06733"
    arxiv_id: "1601.06733"
  - title: "Simple and effective multi-paragraph reading comprehension"
    authors: ["Christopher Clark", "Matt Gardner"]
    year: 2017
    venue: "CoRR"
    doi: null
    url: "http://arxiv.org/abs/1710.10723"
    arxiv_id: "1710.10723"
  - title: "Think you have solved question answering? Try ARC, the AI2 Reasoning Challenge"
    authors: ["Peter Clark", "Isaac Cowhey", "Oren Etzioni", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Context-dependent pre-trained deep neural networks for large-vocabulary speech recognition"
    authors: ["George Dahl", "Dong Yu", "Li Deng", "Alex Acero"]
    year: 2012
    venue: "IEEE Transactions on Audio, Speech, and Language Processing"
    doi: null
    url: null
    arxiv_id: null
  - title: "ImageNet: A large-scale hierarchical image database"
    authors: ["Jia Deng", "Wei Dong", "Richard Socher", "et al."]
    year: 2009
    venue: "CVPR"
    doi: null
    url: "http://www.image-net.org/papers/imagenet_cvpr09.pdf"
    arxiv_id: null
  - title: "Challenges in adopting speech recognition"
    authors: ["Li Deng", "Xuedong Huang"]
    year: 2004
    venue: "Communications of the ACM"
    doi: null
    url: null
    arxiv_id: null
  - title: "SearchQA: A new Q&A dataset augmented with context from a search engine"
    authors: ["Matthew Dunn", "Levent Sagun", "Mike Higgins", "et al."]
    year: 2017
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1704.05179"
  - title: "ROUGE 2.0: Updated and improved measures for evaluation of summarization tasks"
    authors: ["Kavita Ganesan"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neural approaches to conversational AI"
    authors: ["Jianfeng Gao", "Michel Galley", "Lihong Li"]
    year: 2018
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1809.08267"
  - title: "Datasheets for datasets"
    authors: ["Timnit Gebru", "Jamie Morgenstern", "Briana Vecchione", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep residual learning for image recognition"
    authors: ["Kaiming He", "Xiangyu Zhang", "Shaoqing Ren", "Jian Sun"]
    year: 2015
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/1512.03385"
    arxiv_id: "1512.03385"
  - title: "DuReader: A Chinese machine reading comprehension dataset from real-world applications"
    authors: ["Wei He", "Kai Liu", "Yajuan Lyu", "et al."]
    year: 2017
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1711.05073"
  - title: "Teaching machines to read and comprehend"
    authors: ["Karl Moritz Hermann", "Tomas Kocisky", "Edward Grefenstette", "et al."]
    year: 2015
    venue: "NeurIPS / arXiv"
    doi: null
    url: "https://arxiv.org/abs/1506.03340"
    arxiv_id: "1506.03340"
  - title: "Deep neural networks for acoustic modeling in speech recognition: The shared views of four research groups"
    authors: ["Geoffrey Hinton", "Li Deng", "Dong Yu", "et al."]
    year: 2012
    venue: "IEEE Signal Processing Magazine"
    doi: null
    url: null
    arxiv_id: null
  - title: "Long short-term memory"
    authors: ["Sepp Hochreiter", "Jürgen Schmidhuber"]
    year: 1997
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning deep structured semantic models for web search using clickthrough data"
    authors: ["Po-Sen Huang", "Xiaodong He", "Jianfeng Gao", "et al."]
    year: 2013
    venue: "CIKM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Text understanding with the attention sum reader network"
    authors: ["Rudolf Kadlec", "Martin Schmid", "Ondrej Bajgar", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1603.01547"
  - title: "The NarrativeQA reading comprehension challenge"
    authors: ["Tomas Kocisky", "Jonathan Schwarz", "Phil Blunsom", "et al."]
    year: 2017
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1712.07040"
  - title: "RACE: Large-scale reading comprehension dataset from examinations"
    authors: ["Guokun Lai", "Qizhe Xie", "Hanxiao Liu", "et al."]
    year: 2017
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "ROUGE: A package for automatic evaluation of summaries"
    authors: ["Chin-Yew Lin"]
    year: 2004
    venue: "ACL-04 workshop on text summarization"
    doi: null
    url: null
    arxiv_id: null
  - title: "The ROUGE-AR: A proposed extension to the ROUGE evaluation metric for abstractive text summarization"
    authors: ["Stewart Maples"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "An introduction to neural information retrieval"
    authors: ["Bhaskar Mitra", "Nick Craswell"]
    year: 2018
    venue: "Foundations and Trends in Information Retrieval"
    doi: null
    url: null
    arxiv_id: null
  - title: "A proposal for evaluating answer distillation from web data"
    authors: ["Bhaskar Mitra", "Grady Simon", "Jianfeng Gao", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "BLEU: A method for automatic evaluation of machine translation"
    authors: ["Kishore Papineni", "Salim Roukos", "Todd Ward", "Wei-Jing Zhu"]
    year: 2002
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "SQuAD: 100,000+ questions for machine comprehension of text"
    authors: ["Pranav Rajpurkar", "Jian Zhang", "Konstantin Lopyrev", "Percy Liang"]
    year: 2016
    venue: "EMNLP"
    doi: null
    url: "https://arxiv.org/abs/1606.05250"
    arxiv_id: "1606.05250"
  - title: "Know what you don't know: Unanswerable questions for SQuAD"
    authors: ["Pranav Rajpurkar", "Robin Jia", "Percy Liang"]
    year: 2018
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1806.03822"
  - title: "The probabilistic relevance framework: BM25 and beyond"
    authors: ["Stephen Robertson", "Hugo Zaragoza", "et al."]
    year: 2009
    venue: "Foundations and Trends in Information Retrieval"
    doi: null
    url: null
    arxiv_id: null
  - title: "Bidirectional attention flow for machine comprehension"
    authors: ["Minjoon Seo", "Aniruddha Kembhavi", "Ali Farhadi", "Hannaneh Hajishirzi"]
    year: 2016
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1611.01603"
  - title: "ReasoNet: Learning to stop reading in machine comprehension"
    authors: ["Yelong Shen", "Po-Sen Huang", "Jianfeng Gao", "Weizhu Chen"]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1609.05284"
  - title: "End-to-end memory networks"
    authors: ["Sainbayar Sukhbaatar", "Jason Weston", "Rob Fergus", "et al."]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sequence to sequence learning with neural networks"
    authors: ["Ilya Sutskever", "Oriol Vinyals", "Quoc V. Le"]
    year: 2014
    venue: "CoRR"
    doi: null
    url: "http://arxiv.org/abs/1409.3215"
    arxiv_id: "1409.3215"
  - title: "NewsQA: A machine comprehension dataset"
    authors: ["Adam Trischler", "Tong Wang", "Xingdi Yuan", "et al."]
    year: 2017
    venue: "Rep4NLP@ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards AI-complete question answering: A set of prerequisite toy tasks"
    authors: ["Jason Weston", "Antoine Bordes", "Sumit Chopra", "et al."]
    year: 2015
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/1502.05698"
    arxiv_id: "1502.05698"
  - title: "Datasets over algorithms"
    authors: ["Alexander Wissner-Gross"]
    year: 2016
    venue: "Edge.com"
    doi: null
    url: null
    arxiv_id: null
  - title: "ReCoRD: Bridging the gap between human and machine commonsense reading comprehension"
    authors: ["Sheng Zhang", "Xiaodong Liu", "Jingjing Liu", "et al."]
    year: 2018
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1810.12885"
hallucination_severity: "Minor fact tweak"
best_figure:
  number: 2
  title: "Precision-Recall of Machine Reading Comprehension Models on MS MARCO Subset of Numeric Category"
  page: 9
  image_path: "figures/bajaj-2016-ms-marco-fig.png"
---

# MS MARCO: A Human Generated MAchine Reading COmprehension Dataset

**Authors:** Payal Bajaj, Daniel Campos, Nick Craswell, Li Deng, Jianfeng Gao, Xiaodong Liu, Rangan Majumder, Andrew McNamara, Bhaskar Mitra, Tri Nguyen, Mir Rosenberg, Xia Song, Alina Stoica, Saurabh Tiwary, Tong Wang
**Published:** 2016-11 (v3 2018-10) · [Source](https://arxiv.org/abs/1611.09268)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MS MARCO is a 1,010,916-question MRC/QA dataset from Microsoft Research where the queries are **real anonymized Bing search logs** (not crowd-written), each paired with ~10 retrieved web passages and a **human-written natural-language answer** synthesised from those passages — 8,841,823 passages from 3,563,535 web documents in total, with 182,669 "well-formed" rewritten answers. Three tasks are defined: (i) novice — predict answerability + extract+synthesise an answer; (ii) intermediate — generate a standalone well-formed answer; (iii) passage re-ranking — given a query and 1000 BM25-retrieved passages, rank them by relevance. Baselines reveal a large human-vs-machine gap: on v2.1, human ensemble hits ROUGE-L 0.737 on novice vs BiDaF at 0.150 — a ~5× gap that didn't exist in SQuAD-style span extraction. Critically, the v1.1 dataset's human baseline was **surpassed by ML models in ~15 months**, forcing the v2.1 redesign with unanswerable questions and well-formed answer rewrites to keep the benchmark alive. The most useful artefact for the memory-architecture community is the passage-ranking subset (Section 3.1), which became the substrate for the TREC 2019 Deep Learning Track and the de-facto eval set for nearly every modern dense retriever (DPR, ColBERT, ANCE, SPLADE, E5).

## Key Takeaway

Real query-log questions + multi-passage retrieval + free-form human-written answers create a fundamentally harder, more realistic memory-retrieval benchmark than span-extraction datasets like SQuAD — and the resulting passage-ranking subset became the de-facto evaluation substrate for nearly every modern dense-retriever, cross-encoder, and RAG component (BM25 baseline, ~1000 passages re-rank per query, 1M queries / 8.8M passages). The hot take: the **counter-intuitive** lesson is that MRC's hardest signal isn't synthesis — it's knowing *when there is no answer*. BiDaF's collapse on v2.1 (ROUGE-L drops from 0.268 on v1 to 0.150 on v2 novice) wasn't because answers got harder to extract; it was because the model never learned to say "no answer present." Adding the abstain signal is what kept the benchmark alive when humans had already been beaten on span extraction in 15 months.

## Implications

**[ENGRAM-tagged for the memory-architect lens. Each bullet calls out which of the six dimensions — Encode / Network / Ground / Retrieve / Aggregate / Maintain — the finding bears on.]**

- **[R, G] Use real query distributions, not crowd-written ones, when benchmarking your retriever**: MS MARCO's distinguishing feature — and the reason it has outlasted SQuAD, NewsQA, SearchQA in dense-retrieval benchmarks — is that questions came from actual Bing logs, including typos, abbreviations, and ungrammatical fragments like "barack obama age". If your memory system will see user-typed queries, train and eval on query-log data, not crowd-prompted reformulations.
- **[R, A] Design for the "no answer" case as a first-class signal, not an afterthought**: 7.46% of MS MARCO questions are Yes/No but a much larger fraction are unanswerable from the provided passages. The v2.1 redesign explicitly added unanswerable questions, and BiDaF's ROUGE-L on the novice task collapsed from 0.268 (v1) to 0.150 (v2) because it had no abstain mechanism. Your retrieval-augmented system must output "I don't know" cleanly, or it will hallucinate when memory is thin.
- **[N, R] Re-ranking is a tractable, well-defined subproblem worth isolating**: Section 3.1 carves out a passage-ranking subtask: given 1000 BM25 candidates per query, produce a ranking. This single design decision is why MS MARCO became the standard benchmark for DPR, ColBERT, ANCE, SPLADE, monoT5 — re-ranking is a clean supervised learning problem with stable metrics (MRR@10, nDCG@10), unlike free-form answer generation which is plagued by metric noise.
- **[E, G] Annotation incompleteness is honest design, not a flaw**: The paper explicitly notes is_selected annotations are **incomplete** — editors weren't required to mark every relevant passage. This realism mirrors real memory systems where you never know all relevant memories at write-time. Build retrievers and evaluators that assume positive labels are a subset, not a partition (i.e., use recall@k carefully and prefer pairwise judgements where possible).
- **[A] Separate "extracted" from "synthesised" answers as two layers, not one**: MS MARCO ships *both* a raw human-written answer AND a "well-formed answer" rewritten by a second editor for grammatical standalone-ness — e.g. for "tablespoon in cup" the raw answer "16" gets rewritten as "There are 16 tablespoons in a cup." This is the aggregation distinction: extraction is one layer, presentation is another. Don't conflate them in your memory system's output pipeline.
- **[M] Benchmarks die when humans are beaten; design v2 before v1 ships**: The v1.1 human baseline was surpassed in 15 months. The team's response — v2.1 with unanswerable questions, harder span tasks, and a re-elected top-5-editor human baseline (1,427 sampled questions, ROUGE-L best-of-5 → 0.737) — kept the benchmark relevant. For your memory system's eval suite, expect to deprecate and rebuild every 12-24 months.
- **[E, G] Capture multiple answer references per query for metric reliability**: For the multi-answer subset, the team computes pa-BLEU (pairwise BLEU across reference answers), achieving better human correlation than vanilla BLEU. Single ground-truth answers underestimate model quality on open-ended tasks. If you're evaluating an LLM-summariser layer, sample 3-5 references and use pairwise-aggregated metrics.
- **[N] Decouple the documents from the passages from the queries**: MS MARCO publishes six components (questions, passages, answers, well-formed answers, documents, question types). Each is a separate join key. This is the right shape for an evaluation substrate — flat document dumps force every benchmark consumer to redo passage extraction. If you publish a memory corpus, ship pre-chunked passages with stable IDs.

## How to Apply It (method)

**Scenario:** You're building Flow OS's memory layer and want to measure whether your hybrid retriever (QMD = BM25 + vector) actually surfaces the right past memories when a user asks a question. You suspect you're over-fitting to the kinds of questions that map cleanly to a single memory, and missing the harder cases where the answer requires synthesising across two or three memories — or where the right answer is "we never decided that, here's the closest signal we have." You want a MS-MARCO-shaped internal benchmark for your own brain.

**Steps:**

1. **Mine real queries from your own usage logs.** Pull the last 6-12 months of user prompts to your Claude Code / Flow OS instance. Filter out commands (`/save`, `/learn`, etc.) and tool invocations. Keep only natural-language questions to the assistant. Anonymise where needed. This is your equivalent of "questions from Bing logs." Goal: 500-2000 real queries minimum.

2. **For each query, run your retriever to get top-10 candidate memories.** Use your hybrid QMD pipeline exactly as it runs in production:

   ```bash
   ./vendor/qmd/bin/qmd query "<query>" --json -n 10 > candidates.json
   ```

3. **Human-annotate the candidates.** For each query, present the 10 retrieved memory snippets to yourself (or a trusted editor) in a simple web UI. For each candidate, mark `is_relevant: 1` if it contains useful information for the query, `0` otherwise. Crucially, **also allow "no candidate is relevant"** — this is the unanswerable signal. Do not require exhaustive labelling; mark what you're sure of (MS MARCO's `is_selected` is explicitly incomplete and that's fine).

4. **Write a natural-language answer for each query.** For answerable queries, compose a 1-3 sentence answer that synthesises across the relevant candidates. For unanswerable, write "No answer present in memory" and (optionally) a sentence on what would be needed to answer it. Save as your "novice task" ground truth.

5. **Compose a well-formed standalone answer** (the "intermediate task"). For each answerable query, rewrite the answer so it reads naturally without the original question:
   - Bad: "16"
   - Good: "There are 16 tablespoons in a cup."

6. **Define your three eval splits** mirroring MS MARCO:
   - **Re-rank**: given the 1000 best BM25 hits for a query, produce a ranking. Metric: MRR@10.
   - **Novice answer**: produce an answer (or "No answer") from the candidate set. Metric: ROUGE-L vs your written answer + abstain F1.
   - **Intermediate answer**: produce a well-formed standalone answer. Metric: pa-BLEU using your standalone version as one of multiple references.

7. **Run a human baseline.** Have yourself (or 3-5 trusted editors) answer 100 randomly sampled queries under the same constraints (only the retrieved candidates allowed as evidence). Take the best ROUGE-L across editors as your human ensemble. This is the ceiling you're aiming for and the line below which you should never deploy a change.

8. **Re-run quarterly with new query samples.** If your hybrid retriever's score approaches the human baseline, that's the signal to extend the benchmark — add harder cases, more synthesis-required queries, or more unanswerable cases (MS MARCO's v2.1 playbook).

**Expected outcome:** A reproducible internal MRC benchmark calibrated to your actual usage. You'll learn (a) the relevance-precision of your top-10 retriever (likely lower than you expect on multi-memory queries), (b) the answerability-detection ability of your synthesiser (likely much weaker than its extractive ability), and (c) a numeric gap-to-human you can track across QMD and synthesiser changes. The benchmark becomes the regression test for any change to encoding, chunking, retrieval, or compilation in your memory stack.

## Best Figure

![Figure 2 — Precision-Recall of Machine Reading Comprehension Models on MS MARCO Subset of Numeric Category (page 9)](figures/bajaj-2016-ms-marco-fig.png)

Image Candidates:
Figure 1 (p. 5): The editorial UI mockup is the only artefact that makes the human-in-the-loop encoding pipeline concrete (this is the *capture* step in ENGRAM terms).
Figure 2 (p. 9): Precision-Recall curves for AS Reader vs ReasoNet on the numeric subset — the clearest single-glance comparison of two attention-based MRC architectures on the same MS MARCO slice.
Table 7 (p. 9): BiDaF-on-v2 vs Human Ensemble — the most quantitatively striking single view in the paper (ROUGE-L 0.150 vs 0.737 → ~5× human-machine gap on novice task).

Best Image:
Figure Name: Figure 2: "Precision-Recall of Machine Reading Comprehension Models on MS MARCO Subset of Numeric Category"
Figure Page: 9
Slide Caption: ReasoNet's multi-turn reasoning consistently beats the simpler AS Reader across all recall thresholds on the numeric-answer subset.
Description: Figure 2 overlays the precision-recall curves of two attention-based MRC models — Attention Sum Reader (red, ×) and ReasoNet (blue, ○) — evaluated on the numeric-answer subset of MS MARCO v1.1. ReasoNet dominates AS Reader at every recall threshold from 0.1 to 1.0, with the gap widening at higher recall (≈0.06 precision lead at recall 0.6-1.0). The mechanism behind this gap is the memory-architect lens's interesting one: AS Reader picks the answer directly from context in a single attention pass; ReasoNet adds a dynamic multi-turn stop-reading mechanism that re-reads passages until confident. Result: an architecture choice about *when to stop retrieving* materially shifts retrieval quality more than the attention primitive itself. For Flow OS this is the substrate-level argument for adaptive recurrence in the retriever — query-conditioned termination beats single-pass on hard memory-lookup tasks.

## What Experts Overlook

Most experts cite MS MARCO as "the big MRC dataset" or "the passage-ranking benchmark" but skip past one structurally important detail buried in Section 3: **the documents in the dataset may have changed or disappeared from Bing's index after the passages were extracted**. The paper notes that ~300,000 of the 3.56M source documents could not be retrieved at packaging time because they were no longer in Bing's index, and explicitly states "it is possible — even likely — that the content may have changed since the passages were originally extracted." This is a deliberate snapshot-vs-live tension: the *passages* are frozen text, but the *documents* are point-in-time references to a moving web.

**Why it matters:** For a memory-architect, this is the **provenance / Ground problem** showing up in the real world. MS MARCO's editors annotated passages, not documents — meaning the source-of-truth at evaluation time is the cached passage, not the live URL. Any system that tries to "verify" an MS MARCO answer by re-fetching the document URL will get drift, dead links, and contradictions. The implication: when you ship a memory system that cites external sources, you must store the *snapshot of the source at extraction time*, not just the URL. Otherwise your provenance breaks on the timescale of months, not years.

**Example of good use:** When extracting a memory from a web article into Flow OS, store both the URL AND a quoted excerpt (50-200 chars) of the exact text that grounded the memory. At retrieval time, surface the excerpt alongside the URL so the user (and future LLM consumers) can verify the claim without re-fetching. If the URL is dead or has changed, the excerpt still anchors the claim.

**Example of misapplication:** A retrieval system that stores only URLs as provenance ("source: https://example.com/article") and re-fetches on demand. Six months later, the article has been edited, rewritten, or deleted. The memory says "X is true" but no source can be located to confirm it — the system silently degrades from grounded recall to ungrounded assertion, and the AI starts treating its own prior inferences as confirmed facts (exactly the failure mode the memory-architect lens warns against).

## Extracted Prompts

No applicable prompts found in this paper.

(This is a dataset + benchmark paper from the pre-LLM era — 2016/2018 — using attention-based MRC models like AS Reader, ReasoNet, BiDaF, and seq2seq. No prompted language models are used; all models are trained from scratch on the dataset. Editorial instructions to human annotators are described in prose in Section 3 but are not quotable as verbatim prompts.)

## Citations

- **Bahdanau et al. (2014)** — Neural machine translation by jointly learning to align and translate (arXiv:1409.0473)
- **Rajpurkar et al. (2016)** — SQuAD: 100,000+ questions for machine comprehension of text (arXiv:1606.05250)
- **Rajpurkar, Jia, Liang (2018)** — Know what you don't know: Unanswerable questions for SQuAD (arXiv:1806.03822)
- **Seo et al. (2016)** — Bidirectional attention flow for machine comprehension (arXiv:1611.01603)
- **Shen et al. (2016)** — ReasoNet: Learning to stop reading in machine comprehension (arXiv:1609.05284)
- **Kadlec et al. (2016)** — Text understanding with the attention sum reader network (arXiv:1603.01547)
- **Sukhbaatar et al. (2015)** — End-to-end memory networks (NeurIPS)
- **Sutskever, Vinyals, Le (2014)** — Sequence to sequence learning with neural networks (arXiv:1409.3215)
- **Mitra & Craswell (2018)** — An introduction to neural information retrieval (FnT in IR)
- **Robertson & Zaragoza (2009)** — The probabilistic relevance framework: BM25 and beyond (FnT in IR)

(Full 37-entry list in frontmatter `citations[]`.)

## Related Digests

- [[nogueira-2019-bert-passage-reranking]] — Passage Re-ranking with BERT (uses MS MARCO directly as its eval substrate; first widely-adopted BERT-based reranker)
- [[karpukhin-2020-dense-passage-retrieval]] — Dense Passage Retrieval for Open-Domain Question Answering (DPR — the canonical dense retriever benchmarked on MS MARCO)
- [[chen-2017-drqa-machine-reading]] — Reading Wikipedia to Answer Open-Domain Questions (DrQA — contemporary open-domain QA pipeline; complementary corpus to MS MARCO's web-document grounding)
- [[lewis-2020-rag-knowledge-nlp]] — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG — uses MS MARCO-style retrieval as the upstream stage)
- [[gao-2022-hyde-zero-shot-retrieval]] — Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE — evaluates on MS MARCO + BEIR)

## Reviewer Notes

**Overall severity:** Minor fact tweak

**Flagged claims:**

- **Claim:** "the resulting passage-ranking subset became the de-facto evaluation substrate for nearly every modern dense-retriever, cross-encoder, and RAG component (BM25 baseline, ~1000 passages re-rank per query, 1M queries / 8.8M passages)" — and the related list "DPR, ColBERT, ANCE, SPLADE, monoT5, E5" in implications + figure description.
  **Label:** Partially accurate (overextended)
  **Justification:** The paper itself only mentions the TREC 2019 Deep Learning Track as a downstream use of the passage-ranking subset (Section 3.1). The named dense retrievers (DPR, ColBERT, ANCE, SPLADE, monoT5, E5) are post-hoc community knowledge — they all *do* use MS MARCO as their primary benchmark, but the paper doesn't (and couldn't, as a 2016/2018 work) cite them. The "de-facto substrate" claim is true in the field but is not a finding of this paper.
  **Fix:** Either delete the model list, or rephrase as "subsequently became the de-facto evaluation substrate for the modern dense-retriever / cross-encoder lineage (DPR, ColBERT, ANCE, SPLADE, monoT5, E5) — though those works post-date the paper itself." Left as-is for now; flagged here so readers can see the boundary between paper claim and field context.

- **Claim:** "MS MARCO's hot take is that MRC's hardest signal isn't synthesis — it's knowing *when there is no answer*."
  **Label:** Partially accurate
  **Justification:** The paper does emphasise unanswerable questions as a deliberate design choice (Section 1, Section 5.2) and shows BiDaF's performance drop on v2 novice as evidence. But framing it as the "hottest take" is digest editorialising — the paper presents this as one of several improvements in v2.1, not the central thesis.
  **Fix:** Acceptable as digest framing under the memory-architect lens (where abstain is critical), but reader should note this is interpretive emphasis, not a direct paper claim.

All other claims — dataset size (1,010,916 questions / 8,841,823 passages / 3,563,535 documents / 182,669 well-formed answers), v1.1 surpassed in ~15 months, Table 7 numbers (Human Ensemble novice ROUGE-L 0.737, BiDaF v2 novice 0.150), 5-editor / 1,427-question v2.1 baseline, 1000-passage BM25 re-rank task, ~300k documents dropped from Bing index, Table 2 question segments (7.46% YesNo etc.), ReasoNet vs AS Reader precision-recall comparison (Figure 2), the tablespoon→cup well-formed-answer example, BiDaF's vocabulary limitation explanation — are all directly supported by the paper.
