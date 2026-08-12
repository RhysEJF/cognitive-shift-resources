---
corpus: agentic-memory
kind: paper-digest
slug: joshi-2017-triviaqa
title: "TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension"
authors:
  - "Joshi, Mandar"
  - "Choi, Eunsol"
  - "Weld, Daniel S."
  - "Zettlemoyer, Luke"
year: 2017
publication_date: "2017-05"
venue: "ACL 2017"
source_url: "https://arxiv.org/abs/1705.03551"
doi: null
arxiv_id: "1705.03551"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "TriviaQA is the first large-scale QA benchmark where questions are written by trivia enthusiasts independently of any evidence document, and evidence is gathered retrospectively from Wikipedia + Web search — producing 650K question-answer-evidence triples that, by construction, force models to bridge lexical, syntactic, and multi-sentence gaps that crowdsourced-from-passage datasets (SQuAD, NewsQA) systematically smooth away."
topics:
  - reading-comprehension
  - question-answering
  - distant-supervision
  - benchmark-dataset
  - evidence-retrieval
  - multi-sentence-reasoning
  - long-document-qa
tags:
  - paper
  - benchmark
  - dataset
  - encode-dimension
  - ground-dimension
  - retrieve-dimension
  - aggregate-dimension
entities:
  - joshi-mandar
  - choi-eunsol
  - weld-daniel
  - zettlemoyer-luke
  - allen-school
  - allen-institute-ai
related_digests:
  - rajpurkar-2016-squad
  - bajaj-2016-ms-marco
  - dunn-2017-searchqa-dataset
  - chen-2017-drqa-machine-reading
  - clark-2017-multi-paragraph-rc
  - yang-2018-hotpotqa-multihop
  - roberts-2020-pack-knowledge
citations:
  - title: "SQuAD: 100,000+ questions for machine comprehension of text"
    authors: ["Rajpurkar, Pranav", "Zhang, Jian", "Lopyrev, Konstantin", "Liang, Percy"]
    year: 2016
    doi: null
    url: "https://aclweb.org/anthology/D16-1264"
    arxiv_id: "1606.05250"
  - title: "MS MARCO: A human generated machine reading comprehension dataset"
    authors: ["Nguyen, Tri", "Rosenberg, Mir", "Song, Xia", "Gao, Jianfeng", "Tiwary, Saurabh", "Majumder, Rangan", "Deng, Li"]
    year: 2016
    doi: null
    url: "https://arxiv.org/pdf/1611.09268.pdf"
    arxiv_id: "1611.09268"
  - title: "NewsQA: A machine comprehension dataset"
    authors: ["Trischler, Adam", "Wang, Tong", "Yuan, Xingdi", "Harris, Justin", "Sordoni, Alessandro", "Bachman, Philip", "Suleman, Kaheer"]
    year: 2016
    doi: null
    url: "https://arxiv.org/abs/1611.09830"
    arxiv_id: "1611.09830"
  - title: "WikiQA: A challenge dataset for open-domain question answering"
    authors: ["Yang, Yi", "Yih, Wen-tau", "Meek, Christopher"]
    year: 2015
    doi: null
    url: "http://aclweb.org/anthology/D15-1237"
    arxiv_id: null
  - title: "SearchQA: A new q&a dataset augmented with context from a search engine"
    authors: ["Dunn, Matthew", "Sagun, Levent", "Higgins, Mike", "Guney, Ugur", "Cirik, Volkan", "Cho, Kyunghyun"]
    year: 2017
    doi: null
    url: "https://arxiv.org/abs/1704.05179"
    arxiv_id: "1704.05179"
  - title: "Teaching machines to read and comprehend"
    authors: ["Hermann, Karl Moritz", "Kočiský, Tomáš", "Grefenstette, Edward", "Espeholt, Lasse", "Kay, Will", "Suleyman, Mustafa", "Blunsom, Phil"]
    year: 2015
    doi: null
    url: "http://arxiv.org/abs/1506.03340"
    arxiv_id: "1506.03340"
  - title: "Bidirectional attention flow for machine comprehension (BiDAF)"
    authors: ["Seo, Minjoon", "Kembhavi, Aniruddha", "Farhadi, Ali", "Hajishirzi, Hannaneh"]
    year: 2017
    doi: null
    url: "https://arxiv.org/abs/1611.01603"
    arxiv_id: "1611.01603"
  - title: "MCTest: A challenge dataset for the open-domain machine comprehension of text"
    authors: ["Richardson, Matthew", "Burges, Christopher J.C.", "Renshaw, Erin"]
    year: 2013
    doi: null
    url: "http://www.aclweb.org/anthology/D13-1020"
    arxiv_id: null
  - title: "A thorough examination of the CNN/Daily Mail reading comprehension task"
    authors: ["Chen, Danqi", "Bolton, Jason", "Manning, Christopher D."]
    year: 2016
    doi: null
    url: "http://www.aclweb.org/anthology/P16-1223"
    arxiv_id: null
  - title: "TAGME: On-the-fly annotation of short text fragments (by Wikipedia entities)"
    authors: ["Ferragina, Paolo", "Scaiella, Ugo"]
    year: 2010
    doi: "10.1145/1871437.1871689"
    url: null
    arxiv_id: null
  - title: "Who did what: A large-scale person-centered cloze dataset"
    authors: ["Onishi, Takeshi", "Wang, Hai", "Bansal, Mohit", "Gimpel, Kevin", "McAllester, David"]
    year: 2016
    doi: null
    url: "https://aclweb.org/anthology/D16-1241"
    arxiv_id: null
  - title: "The LAMBADA dataset: Word prediction requiring a broad discourse context"
    authors: ["Paperno, Denis", "Kruszewski, Germán", "Lazaridou, Angeliki", "Pham, Ngoc Quan", "Bernardi, Raffaella", "Pezzelle, Sandro", "Baroni, Marco", "Boleda, Gemma", "Fernandez, Raquel"]
    year: 2016
    doi: null
    url: "http://www.aclweb.org/anthology/P16-1144"
    arxiv_id: null
  - title: "RACE: Large-scale reading comprehension dataset from examinations"
    authors: ["Lai, Guokun", "Xie, Qizhe", "Liu, Hanxiao", "Yang, Yiming", "Hovy, Eduard"]
    year: 2017
    doi: null
    url: "https://arxiv.org/abs/1704.04683"
    arxiv_id: "1704.04683"
  - title: "Building a question answering test collection (TREC-8 QA)"
    authors: ["Voorhees, Ellen M.", "Tice, Dawn M."]
    year: 2000
    doi: "10.1145/345508.345577"
    url: null
    arxiv_id: null
  - title: "Building Watson: An overview of the DeepQA project"
    authors: ["Ferrucci, David", "Brown, Eric", "Chu-Carroll, Jennifer", "Fan, James", "Gondek, David", "Kalyanpur, Aditya A.", "Lally, Adam", "Murdock, J. William", "Nyberg, Eric", "Prager, John", "Schlaefer, Nico", "Welty, Chris"]
    year: 2010
    doi: null
    url: null
    arxiv_id: null
  - title: "Semantic parsing on Freebase from question-answer pairs"
    authors: ["Berant, Jonathan", "Chou, Andrew", "Frostig, Roy", "Liang, Percy"]
    year: 2013
    doi: null
    url: "http://aclweb.org/anthology/D/D13/D13-1160.pdf"
    arxiv_id: null
  - title: "Large-scale simple question answering with memory networks"
    authors: ["Bordes, Antoine", "Usunier, Nicolas", "Chopra, Sumit", "Weston, Jason"]
    year: 2015
    doi: null
    url: "https://arxiv.org/abs/1506.02075"
    arxiv_id: "1506.02075"
  - title: "Besting the quiz master: Crowdsourcing incremental classification games"
    authors: ["Boyd-Graber, Jordan", "Satinoff, Brianna", "He, He", "Daumé III, Hal"]
    year: 2012
    doi: null
    url: "http://www.aclweb.org/anthology/D12-1118"
    arxiv_id: null
  - title: "Compositional semantic parsing on semi-structured tables"
    authors: ["Pasupat, Panupong", "Liang, Percy"]
    year: 2015
    doi: null
    url: "http://www.aclweb.org/anthology/P15-2115"
    arxiv_id: null
  - title: "Modeling relations and their mentions without labeled text"
    authors: ["Riedel, Sebastian", "Yao, Limin", "McCallum, Andrew"]
    year: 2010
    doi: null
    url: "http://dl.acm.org/citation.cfm?id=1889788.1889799"
    arxiv_id: null
  - title: "Knowledge-based weak supervision for information extraction of overlapping relations"
    authors: ["Hoffmann, Raphael", "Zhang, Congle", "Ling, Xiao", "Zettlemoyer, Luke", "Weld, Daniel S."]
    year: 2011
    doi: null
    url: "http://www.aclweb.org/anthology/P11-1055"
    arxiv_id: null
  - title: "A neural network for factoid question answering over paragraphs"
    authors: ["Iyyer, Mohit", "Boyd-Graber, Jordan", "Claudino, Leonardo", "Socher, Richard", "Daumé III, Hal"]
    year: 2014
    doi: null
    url: "http://www.aclweb.org/anthology/D14-1070"
    arxiv_id: null
  - title: "Knowledge graph and corpus driven segmentation and answer inference for telegraphic entity-seeking queries"
    authors: ["Joshi, Mandar", "Sawant, Uma", "Chakrabarti, Soumen"]
    year: 2014
    doi: null
    url: "http://www.aclweb.org/anthology/D14-1117"
    arxiv_id: null
  - title: "Opponent modeling in deep reinforcement learning"
    authors: ["He, He", "Boyd-Graber, Jordan", "Kwok, Kevin", "Daumé III, Hal"]
    year: 2016
    doi: null
    url: "http://proceedings.mlr.press/v48/he16.html"
    arxiv_id: null
  - title: "Adapting boosting for information retrieval measures (LambdaMART)"
    authors: ["Wu, Qiang", "Burges, Christopher J.", "Svore, Krysta M.", "Gao, Jianfeng"]
    year: 2010
    doi: "10.1007/s10791-009-9112-1"
    url: null
    arxiv_id: null
  - title: "Hierarchical attention networks for document classification"
    authors: ["Yang, Zichao", "Yang, Diyi", "Dyer, Chris", "He, Xiaodong", "Smola, Alex", "Hovy, Eduard"]
    year: 2016
    doi: null
    url: "http://www.aclweb.org/anthology/N16-1174"
    arxiv_id: null
  - title: "The Goldilocks principle: Reading children's books with explicit memory representations"
    authors: ["Hill, Felix", "Bordes, Antoine", "Chopra, Sumit", "Weston, Jason"]
    year: 2015
    doi: null
    url: "https://arxiv.org/abs/1511.02301"
    arxiv_id: "1511.02301"
  - title: "Large-scale semantic parsing via schema matching and lexicon extension"
    authors: ["Cai, Qingqing", "Yates, Alexander"]
    year: 2013
    doi: null
    url: "http://www.aclweb.org/anthology/P13-1042"
    arxiv_id: null
  - title: "Open question answering over curated and extracted knowledge bases"
    authors: ["Fader, Anthony", "Zettlemoyer, Luke", "Etzioni, Oren"]
    year: 2014
    doi: "10.1145/2623330.2623677"
    url: null
    arxiv_id: null
  - title: "Machine comprehension with syntax, frames, and semantics"
    authors: ["Wang, Hai", "Bansal, Mohit", "Gimpel, Kevin", "McAllester, David"]
    year: 2015
    doi: null
    url: null
    arxiv_id: null
  - title: "Show, attend and tell: Neural image caption generation with visual attention"
    authors: ["Xu, Kelvin", "Ba, Jimmy", "Kiros, Ryan", "Cho, Kyunghyun", "Courville, Aaron", "Salakhutdinov, Ruslan", "Zemel, Richard", "Bengio, Yoshua"]
    year: 2015
    doi: null
    url: "https://arxiv.org/abs/1502.03044"
    arxiv_id: "1502.03044"
  - title: "WikiQA: A challenge dataset for open-domain question answering"
    authors: ["Yang, Yi", "Yih, Wen-tau", "Meek, Christopher"]
    year: 2015
    doi: null
    url: "http://aclweb.org/anthology/D15-1237"
    arxiv_id: null
  - title: "Dataset and neural recurrent sequence labeling model for open-domain factoid question answering"
    authors: ["Li, Peng", "Li, Wei", "He, Zhengyan", "Wang, Xuguang", "Cao, Ying", "Zhou, Jie", "Xu, Wei"]
    year: 2016
    doi: null
    url: "https://arxiv.org/abs/1607.06275"
    arxiv_id: "1607.06275"
  - title: "Learning joint query interpretation and response ranking"
    authors: ["Sawant, Uma", "Chakrabarti, Soumen"]
    year: 2013
    doi: "10.1145/2488388.2488484"
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Question-answer pairs with sample excerpts from evidence documents from TriviaQA exhibiting lexical and syntactic variability, and requiring reasoning from multiple sentences"
  page: 1
  image_path: "figures/joshi-2017-triviaqa-fig.png"
---

# TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension

**Authors:** Mandar Joshi, Eunsol Choi, Daniel S. Weld, Luke Zettlemoyer
**Published:** 2017-05 · [Source](https://arxiv.org/abs/1705.03551)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

TriviaQA assembles 650K question-answer-evidence triples by starting from 95K human-authored trivia questions (scraped from 14 trivia/quiz-league sites) and then *retrospectively* gathering evidence — top 10 Bing web pages plus TAGME-linked Wikipedia entity pages (avg 6 docs per question). Crucially, neither questions nor evidence were crowdsourced *from* the documents, so questions are organically compositional (avg 14 tokens, 1.77 entities each, 69% syntactic variation vs. evidence, 40% requiring multi-sentence reasoning) and evidence is noisy/long (avg 2,895 words per doc). The "distant supervision" lever — assuming any document containing the answer string is a positive — holds ~75% of the time. Two baselines (a LambdaMART feature classifier and BiDAF, 2017's SOTA on SQuAD) achieve 23% and 40% EM respectively, vs. 79.7% human performance, leaving a ~40-point gap that the authors argue justifies the dataset's existence.

**Why this matters for memory architects:** TriviaQA is the cleanest early demonstration that *decoupling write-time (question authoring) from retrieval-time (evidence gathering)* surfaces the actual retrieval and reasoning challenges that crowdsourcing-from-passage hides. Every modern open-book RAG benchmark inherits this design discipline.

## Key Takeaway

**Independence between question authoring and evidence collection is the single design choice that determines whether a QA benchmark measures retrieval-and-reasoning or pattern-matching against the passage the annotator was staring at.** TriviaQA's 5-column comparison table (Large scale / Freeform answer / Well-formed / Independent of evidence / Varied evidence) puts it as the only dataset of the era satisfying all five — and the resulting >3× rate of multi-sentence reasoning vs. SQuAD plus 69% syntactic divergence between question and evidence sentence are the *consequences* of that one decision, not separate features the authors had to design in.

For a memory system, this is the ENGRAM-**E**ncode / ENGRAM-**G**round / ENGRAM-**A**ggregate cross-cut: the **shape of the write-time artifact (the question)** and the **shape of the source the answer must ground in (the evidence corpus)** determine what the retrieval+reasoning stack actually has to learn. If you author memory write-ups that quote the source verbatim, your retrieval evaluation is measuring index recall, not reasoning. If you author them independently (as a real user would), you get the realistic difficulty.

## Implications

**ENGRAM mapping** (per the memory-architect lens):

| Finding | ENGRAM dim(s) | Detail |
|---|---|---|
| Questions authored independently of evidence | **E** (Encode) + **A** (Aggregate) | The write-time artifact (Q+A) is *not* a summary of the source. This is the agentic-memory analogue of writing a user-facing note from a goal description, not from the source doc. Forces aggregation across multiple sources at query time. |
| 6 evidence docs per Q (web) / 1.8 per Q (wiki) | **N** (Network) + **R** (Retrieve) | Web evidence is *redundant* (treat each Q,A,D triple as independent); Wikipedia evidence is *non-redundant* (pool docs, never repeat Q). Same task, two retrieval shapes — authors explicitly engineered different supervision strategies per source. Direct precedent for hybrid memory stacks (markdown vault + vector store) where the same query expression must work over heterogeneously-shaped memory. |
| Distant-supervision assumption (answer-string-in-doc → relevant) holds 75–80% of the time | **G** (Ground) | Quantified provenance noise. 19% of error-analysis incorrect predictions had *no* evidence in any provided document. This is the same failure mode as RAG retrieval-returning-irrelevant — and TriviaQA quantified it 7 years before "RAG hallucination" became a buzzword. |
| Average doc length 2,895 words; BiDAF truncates to 800 | **R** (Retrieve) + **N** (Network) | The 2017 retrieval-shape constraint: short-context models can't ingest the full evidence, so truncation pushes the burden upstream onto a *retriever* or onto better windowing. Foreshadows the whole long-context-vs-RAG debate. |
| Multi-doc score aggregation: sum BiDAF confidence over per-doc predictions | **A** (Aggregate) + **R** (Retrieve) | The "sum confidence" trick is the simplest possible cross-document consolidation strategy. Modern dense-retriever rerank + LLM-fusion pipelines are direct descendants. Note the simplicity: no learned aggregator, no per-doc weighting — and it still outperforms the single-best-doc baseline. |
| 7% of answers live in HTML tables/lists | **N** (Network) | Modality boundary inside the same memory store. Their RNN baselines can't reach these; argues for polyglot memory (text + table extraction) rather than treating every source as flat prose. |
| Verified subset (1,975 human-certified Q,D,A triples) | **G** (Ground) | Distinct from the noisy 650K — a clean held-out evaluation set built by humans confirming "yes, the answer is actually in this doc." This is the explicit pattern for a *trust-calibrated* eval split that agentic-memory teams should copy: keep a small, human-verified subset alongside the noisy training/operational corpus. |
| 79.7% human ceiling on Wikipedia, 75.4% on Web | **G** (Ground) | Even *humans* can't always find the answer in a randomly-sampled set of evidence docs. This is the irreducible noise floor — useful as a sanity check when an agentic-memory eval reports >80% retrieval recall: that's likely overfitting to oracle-style evaluation. |

**Cross-dimensional interaction**: the **E** decision (independent question authoring) *forces* the **G** decision (you must build a verified subset because distant supervision is provably 25% noisy) which *forces* the **R** decision (you can't just match on n-grams because syntactic and lexical variation is the norm not the exception). This is a clean example of how one encoding choice cascades through the rest of ENGRAM.

**For Flow OS memory layer specifically:** TriviaQA's setup is essentially the test for "can our extracted memory cards (analogous to QA pairs) be found and used when the original session transcript (analogous to evidence docs) is long, noisy, and uses different vocabulary from the way the user phrases the future query?" — which is exactly the QMD retrieval evaluation problem. Worth adopting their "verified subset" pattern: a hand-curated set of ~100 "this query should retrieve this memory" pairs as a regression test.

## How to Apply It (method)

If you're building a memory/retrieval benchmark for an agentic system, the TriviaQA recipe is:

1. **Source the queries independently of the corpus.** Don't crowdsource from passages, don't generate via LLM prompted with the passage — get them from a population that naturally produces query-shaped artifacts (here: 14 quiz-league sites; for agentic memory: real user chat logs, real support tickets, real planning sessions).
2. **Filter for query quality before evidence-gathering.** Joshi et al. dropped any question with <4 tokens (too vague / too simple). For memory: filter logged queries below some specificity threshold so the eval isn't dominated by "what's the weather."
3. **Gather evidence retrospectively from heterogeneous sources.** TriviaQA used Bing top-50 (then top-10 after PDF/url-keyword filtering) + TAGME entity-linked Wikipedia pages. For memory: pull every session transcript, doc, and prior memory the agent could *plausibly* have access to — not just the one that contains the answer.
4. **Exclude leakage paths.** They dropped any URL containing trivia/question/answer to avoid contaminating evidence with the question source. For memory: exclude any document that was generated *as* the canonical answer to that query.
5. **Apply distant-supervision filtering, but measure its noise rate.** Keep only doc-question pairs where the answer string appears in the doc, *then* hand-verify ~2000 of them to measure how often the answer-presence assumption actually implies the doc answers the question. (TriviaQA: 75–80%.)
6. **Split by question, not by doc.** When the same question maps to many docs (web), each (Q, A, D) triple is independent; when the same question maps to a few non-redundant docs (Wikipedia), pool the docs and treat the question as one data point. This prevents train-test leakage at the question level.
7. **Build both a noisy large set AND a verified small set.** The noisy set is for training/operational use; the verified set is for trustworthy evaluation. Different sizes (650K vs. 2K), different roles.
8. **Report aggregate AND fine-grained metrics.** Joshi et al. broke out: EM, F1, oracle ceiling; per-domain (Wiki vs Web); per-question-length bin; per-answer-type. A flat headline number hides the failure modes.

## Best Figure

![Figure 1 — Question-answer pairs with sample excerpts (page 1)](figures/joshi-2017-triviaqa-fig.png)

Two real TriviaQA examples — "the Dodecanese Campaign of WWII…inspired which 1961 commando film?" → *The Guns of Navarone*, and "Callan Pinckney's eponymously named system became a best-selling 1980s book/video franchise in what genre?" → *Fitness*. In both cases the question and the evidence excerpt share almost no surface tokens. The Navarone evidence mentions "1957 novel" and "1961 movie of the same name" — the model has to bridge "1961 commando film" → "1961 movie The Guns of Navarone." The Callan Pinckney evidence never uses the word *genre* — the model has to infer "fitness" from "fitness professional / fitness video."

This single figure is the whole pitch for TriviaQA: this is what naturally-authored questions look like when paired with the actual documents that contain the answer, and it's qualitatively different from "given this Wikipedia paragraph, write a question whose answer is in it."

**For the memory-architect lens:** this figure is the visual answer to "why does keyword search collapse on real retrieval problems." A BM25 query over the question would not surface either excerpt as the top hit. You need either query expansion, semantic embedding, or LLM-mediated rephrasing — which is exactly the design space modern memory systems explore.

## What Experts Overlook

1. **The verified subset is the load-bearing part of the dataset.** Most secondary citations of TriviaQA report the 650K headline number and the BiDAF 40% EM baseline. But the *interesting* number is the 79.7% human ceiling and the gap between BiDAF on distant-supervision dev (40.26 EM) vs. BiDAF on the verified dev (47.47 EM, +7 points). That gap is the "noise from distant supervision" tax — and it tells you how much of your apparent model weakness is actually label noise. Most readers miss this.

2. **The dataset is two datasets, not one.** Wikipedia-domain and Web-domain have fundamentally different retrieval shapes (non-redundant vs. redundant evidence), different evaluation units (question-level vs. document-level), and different supervision strategies. Treating "TriviaQA performance" as a single number is wrong — papers that fine-tune only on web and report a single score are conflating regimes.

3. **The 800-word truncation is a forced engineering choice that distorts results.** Average evidence doc is 2,895 words; BiDAF can only ingest 800. The authors explicitly note that splitting into sub-documents *hurt* performance because most subdocs don't contain the answer (no positive supervision). This means the BiDAF baseline is *not* an upper bound on what RC models can do on full documents — it's an upper bound on what 2017 RC models can do on the first 800 words. Modern long-context models running on full docs would have an entirely different error profile, and old "BiDAF gets 40%" numbers are not the comparison point for, e.g., GPT-4 over the full evidence set.

4. **Distant supervision noise is non-uniform.** Web evidence assumption holds 75.4%; Wikipedia 79.7%. The 5-point gap matters because it means Web training data has 25% noise — a real but rarely-discussed bias source when training models that report numbers on the verified-test set.

5. **Question-length is a strong difficulty signal.** BiDAF: 50% EM on ≤5-word questions, 32% EM on ≥20-word questions. Most QA papers since haven't reported this breakdown, but it's a free diagnostic for "is my model handling compositional questions at all" — applies directly to evaluating agentic-memory retrieval over multi-clause user queries.

6. **The "natural language questions" framing undersells the real contribution.** The contribution isn't that questions are in natural language (so are SQuAD's). It's that questions are written *without* the answerer ever seeing the source document. That's the difference between "well-formed" and "*independent of evidence*" in Table 1, and only TriviaQA satisfies both.

7. **TAGME is doing a lot of unsung work.** The Wikipedia evidence set comes from TAGME entity-linking the *question* and pulling the linked Wikipedia pages. So the retrieval-time scope is *already* narrowed by a high-precision entity linker before the RC model ever runs. Modern systems that use vector-similarity retrieval on full-question embeddings are doing a noisier version of this — and TriviaQA's results don't tell you what happens without the TAGME prefilter.

## Extracted Prompts

The paper doesn't contain LLM prompts (it's a 2017 paper, predating instruction-tuned LLMs). But it contains several *task templates* and *annotation prompts* that are equivalent for our purposes:

**Trivia-question authoring prompt** (implicit, derived from the quiz-league source population): "Write a question whose answer is a notable entity, where the question itself contains 1–2 entity clues plus a fine-grained type constraint, and is at least 4 tokens long."

**Distant-supervision filtering rule**: For each question Q with answer A and candidate doc D from retrieval, *keep (Q, A, D)* iff `A` appears as a substring of `D`. Discard otherwise. This is the canonical rule — copy it into any memory-eval pipeline where you want a noisy-but-cheap relevance signal.

**Human-verification annotation prompt** (paraphrased from §4): "Given a question Q and the set of evidence documents D, answer Q using only the minimal facts present in D (ignoring temporal references like 'this year'). If the minimal facts required are not present in D, abstain. Then we compare your answer to the original answer string and aliases."

**Error-analysis taxonomy** (Table 8 — directly usable for any memory-retrieval system's error-classification step):
- Insufficient evidence (19%)
- Prediction from incorrect document(s) (7%)
- Answer not in clipped document (15%)
- Paraphrasing (29%)
- Distractor entities (11%)
- Reasoning over multiple sentences (18%)

**Reasoning-type analysis taxonomy** (Table 5 — useful as a difficulty taxonomy for any QA-over-memory benchmark):
- Lexical variation / synonym
- Lexical variation + world knowledge
- Syntactic variation
- Multiple-sentence reasoning
- Lists / tables

## Citations

- **SQuAD** (Rajpurkar et al., 2016) — the explicit foil; crowdsourced from passages, ~100K Qs
- **MS MARCO** (Nguyen et al., 2016) — concurrent independently-authored open-domain QA
- **NewsQA** (Trischler et al., 2016) — crowdsourced from news summaries
- **SearchQA** (Dunn et al., 2017) — Jeopardy! Qs paired with search snippets
- **WikiQA** (Yang et al., 2015) — answer-sentence selection
- **CNN/Daily Mail** (Hermann et al., 2015) — cloze-style; the baseline comparison
- **BiDAF** (Seo et al., 2017) — the SOTA RC model used as TriviaQA's neural baseline
- **MCTest** (Richardson et al., 2013) — small (2.6K) multiple-choice RC predecessor
- **TAGME** (Ferragina & Scaiella, 2010) — entity linker used to fetch Wikipedia evidence
- **LambdaMART** (Wu et al., 2010) — boosted tree ranker for the classifier baseline

(Full 33-entry citation graph in frontmatter `citations:`.)

## Related Digests

- [[rajpurkar-2016-squad]] — SQuAD: the explicit foil; passage-grounded crowdsourced Qs
- [[bajaj-2016-ms-marco]] — MS MARCO: concurrent independently-authored real-query benchmark
- [[dunn-2017-searchqa-dataset]] — SearchQA: similar Q+search-evidence pairing, Jeopardy-sourced
- [[chen-2017-drqa-machine-reading]] — DrQA: open-domain RC over full Wikipedia
- [[clark-2017-multi-paragraph-rc]] — Multi-paragraph RC that directly addresses TriviaQA's truncation problem
- [[yang-2018-hotpotqa-multihop]] — HotpotQA: pushes multi-sentence reasoning further into multi-hop
- [[roberts-2020-pack-knowledge]] — Closed-book QA: T5 reaches 61.6% on TriviaQA from parameters alone

## Reviewer Notes

**Overall severity:** Clean.

Spot-checked claims against the source text:

- 650K Q-A-evidence triples, 95K Q-A pairs, 14 trivia sites — verified (Abstract + §3).
- Avg 6 docs per Q in web; 1.8 docs per Q in Wikipedia — verified (§3, §2).
- 79.7% / 75.4% human accuracy on Wikipedia / Web verified subsets — verified (§4, "the accuracy ... for the Wikipedia and Web domains was 79.6 and 75.3"). Abstract rounds to 80%.
- BiDAF 40% / Classifier 23% — verified (Table 7: BiDAF Wiki dev EM 40.26; Classifier Wiki dev EM 23.42). Abstract uses these as headline numbers.
- 69% syntactic variation, 41% lexical variation (Wiki) — verified (§4: "69% of the questions had a different syntactic structure while 41% were lexically different").
- 40% multi-sentence reasoning (Wiki) — verified (Table 5: "Multiple sentences ... 40% in Wiki documents, 35% in web documents").
- 73.5% fine-grained answer type, 15.5% coarse — verified (Table 3 / §4).
- 92.85% answers are Wikipedia titles; 4.17% numerical — verified (Table 4).
- 800-word BiDAF truncation; avg doc length 2,895 words — verified (§5.3, Table 2).
- TAGME used for Wikipedia entity linking — verified (§3).
- LambdaMART used for classifier — verified (§5.2).
- 5-column comparison table (Large scale / Freeform / Well-formed / Independent / Varied) — verified (Table 1). Note the table also shows TriviaQA is the *only* dataset of those listed satisfying all five.
- "First dataset where full-sentence questions are authored organically (independent of evidence)" claim — verified (§1, intro).
- Error analysis 19% insufficient evidence, 29% paraphrasing — verified (Table 8).
- 7% answers in HTML tables/lists — verified (Table 5 + §7).

ENGRAM mapping (E/G/A cascade interpretation) is the digester's framework, not the paper's — flagged as analyst's overlay rather than the paper's claim. The paper itself uses "distant supervision" and "decoupling" as its framing.

No factual rewrites needed.
