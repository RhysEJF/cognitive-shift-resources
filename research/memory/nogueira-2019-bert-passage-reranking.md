---
corpus: agentic-memory
kind: paper-digest
slug: nogueira-2019-bert-passage-reranking
title: "Passage Re-ranking with BERT"
authors:
  - "Rodrigo Nogueira"
  - "Kyunghyun Cho"
year: 2019
publication_date: "2019-01"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/1901.04085"
doi: null
arxiv_id: "1901.04085"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Feeding (query, passage) as BERT's sentence-A/sentence-B pair and fine-tuning the [CLS] token as a binary relevance classifier — over a cheap BM25 first stage — beats the previous SOTA on MS MARCO by 27% relative MRR@10 after seeing only 12.8M of the 400M training pairs, demonstrating that the heavy reranker tier is where pretrained transformers earn their keep, not the recall tier."
topics:
  - passage-reranking
  - bert
  - information-retrieval
  - retrieve-stage
  - hybrid-retrieval
  - bm25
  - ms-marco
  - trec-car
  - cross-encoder
  - two-stage-retrieval
tags:
  - paper
  - retrieval
  - reranker
  - foundational
  - benchmark
entities:
  - nogueira-rodrigo
  - cho-kyunghyun
related_digests:
  - adler-2026-storage-not-memory
  - gao-2022-hyde-zero-shot-retrieval
  - latimer-2025-hindsight-memory
citations:
  - title: "Reading Wikipedia to Answer Open-Domain Questions"
    authors: ["Danqi Chen", "Adam Fisch", "Jason Weston", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1704.00051"
  - title: "Simple and Effective Multi-Paragraph Reading Comprehension"
    authors: ["Christopher Clark", "Matt Gardner"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1710.10723"
  - title: "Convolutional Neural Networks for Soft-Matching N-Grams in Ad-hoc Search"
    authors: ["Zhuyun Dai", "Chenyan Xiong", "Jamie Callan", "et al."]
    year: 2018
    venue: "WSDM"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "Quasar: Datasets for Question Answering by Search and Reading"
    authors: ["Bhuwan Dhingra", "Kathryn Mazaitis", "William W. Cohen"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1707.03904"
  - title: "TREC Complex Answer Retrieval Overview"
    authors: ["Laura Dietz", "Manisha Verma", "Filip Radlinski", "et al."]
    year: 2017
    venue: "TREC"
    doi: null
    url: null
    arxiv_id: null
  - title: "SearchQA: A New Q&A Dataset Augmented with Context from a Search Engine"
    authors: ["Matthew Dunn", "Levent Sagun", "Mike Higgins", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1704.05179"
  - title: "A Deep Relevance Matching Model for Ad-hoc Retrieval"
    authors: ["Jiafeng Guo", "Yixing Fan", "Qingyao Ai", "et al."]
    year: 2016
    venue: "CIKM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Co-PACRR: A Context-Aware Neural IR Model for Ad-hoc Retrieval"
    authors: ["Kai Hui", "Andrew Yates", "Klaus Berberich", "et al."]
    year: 2018
    venue: "WSDM"
    doi: null
    url: null
    arxiv_id: null
  - title: "TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension"
    authors: ["Mandar Joshi", "Eunsol Choi", "Daniel S. Weld", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1705.03551"
  - title: "Adam: A Method for Stochastic Optimization"
    authors: ["Diederik P. Kingma", "Jimmy Ba"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1412.6980"
  - title: "The Neural Hype and Comparisons Against Weak Baselines"
    authors: ["Jimmy Lin"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Contextualized PACRR for Complex Answer Retrieval"
    authors: ["Sean MacAvaney", "Andrew Yates", "Kai Hui"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to Match Using Local and Distributed Representations of Text for Web Search"
    authors: ["Bhaskar Mitra", "Fernando Diaz", "Nick Craswell"]
    year: 2017
    venue: "WWW"
    doi: null
    url: null
    arxiv_id: null
  - title: "MS MARCO: A Human Generated Machine Reading Comprehension Dataset"
    authors: ["Tri Nguyen", "Mir Rosenberg", "Xia Song", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1611.09268"
  - title: "Semi-supervised Sequence Tagging with Bidirectional Language Models"
    authors: ["Matthew E. Peters", "Waleed Ammar", "Chandra Bhagavatula", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1705.00108"
  - title: "Improving Language Understanding by Generative Pre-Training"
    authors: ["Alec Radford", "Karthik Narasimhan", "Tim Salimans", "et al."]
    year: 2018
    venue: "OpenAI tech report"
    doi: null
    url: "https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf"
    arxiv_id: null
  - title: "SQuAD: 100,000+ Questions for Machine Comprehension of Text"
    authors: ["Pranav Rajpurkar", "Jian Zhang", "Konstantin Lopyrev", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1606.05250"
  - title: "Bidirectional Attention Flow for Machine Comprehension"
    authors: ["Minjoon Seo", "Aniruddha Kembhavi", "Ali Farhadi", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1611.01603"
  - title: "End-to-End Neural Ad-hoc Ranking with Kernel Pooling"
    authors: ["Chenyan Xiong", "Zhuyun Dai", "Jamie Callan", "et al."]
    year: 2017
    venue: "SIGIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Anserini: Reproducible Ranking Baselines Using Lucene"
    authors: ["Peilin Yang", "Hui Fang", "Jimmy Lin"]
    year: 2018
    venue: "JDIQ"
    doi: null
    url: null
    arxiv_id: null
  - title: "QANet: Combining Local Convolution with Global Self-Attention for Reading Comprehension"
    authors: ["Adams Wei Yu", "David Dohan", "Minh-Thang Luong", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1804.09541"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Number of MS MARCO examples seen during training vs. MRR@10 performance"
  page: 3
  image_path: "figures/nogueira-2019-bert-passage-reranking-fig.png"
---

# Passage Re-ranking with BERT

**Authors:** Rodrigo Nogueira, Kyunghyun Cho
**Published:** 2019-01 · [Source](https://arxiv.org/abs/1901.04085)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Nogueira & Cho take pretrained BERT (Large), feed it `(query [SEP] candidate-passage)` as the standard sentence-pair input, train a single classification head on top of the `[CLS]` token to predict relevance, and use that as a second-stage re-ranker over the top-1,000 passages BM25 retrieves first. On MS MARCO, this lifts MRR@10 from the prior SOTA of 27.8 (IR-NET) to 36.5 — a 27% relative gain — using 12.8M training pairs (~2% of the 400M available; 30 hours on one TPU v3-8). On TREC-CAR, MAP rises from 14.8 (best 2017 entry) to 33.5 with BERT Large, even after re-pretraining BERT only on the Wikipedia half allowed by the TREC-CAR train split (to avoid test leakage from BERT's original full-Wikipedia pretraining). Figure 1 shows the win is already visible at 100k training pairs (0.3% of available data), where BERT Large already beats IR-NET by 1.4 MRR@10. Practical takeaway: keep your fast lexical recall layer, spend the compute on a heavy transformer reranker over the top-N — that's where the accuracy lives.

## Key Takeaway

The cheapest way to add a real intelligence layer to your retrieval stack in 2019 was to put a pretrained transformer on top of BM25 — not to replace BM25. BM25 alone scored 16.7 MRR@10 on MS MARCO; BERT Large reranking the top-1,000 BM25 hits scored 36.5 — more than doubling, while leaving the candidate-recall layer untouched. The compute heavy step (a 24-layer transformer scoring 1,000 passages per query) is contained inside the reranker tier, where you can budget it; the recall tier stays linear-scan-friendly. **ENGRAM: R (Retrieve)** — this is a pure Retrieve-dimension result: same encoding, same store, same shape — the only thing that changes is the ranking function over already-recalled candidates, and that change buys the entire accuracy delta.

## Implications

- **Put your "AI tax" on the reranker, not the recall tier (ENGRAM: R)**: BM25 (or any cheap lexical/embedding hybrid) is fine for getting 1,000 candidates in front of the model. Spending transformer compute to rescore those candidates yielded a 27% relative MRR@10 gain over the previous neural SOTA — your memory layer probably has the same shape (lots of candidates retrieved cheaply, only a handful actually used), so reserve the cross-encoder for the small-N rescoring step.
- **The cross-encoder format is the unlock, not the model size (ENGRAM: R)**: Feeding `(query, passage)` as a single sentence-pair input — letting every query token attend to every passage token through 24 transformer layers — is the architectural primitive. A BERT-Base variant already scored 34.7 vs IR-NET's 27.8; BERT-Large only added 1.8 more points. The format change (joint attention vs separate encoders) does more work than the parameter count.
- **You don't need the full training set — the prior + a small task signal is enough (ENGRAM: A, E)**: 12.8M of the 400M MS MARCO training pairs (~2%) was enough to saturate. Three more days of training added zero dev-set gain. For your Aggregate stage, this means: when you fine-tune a memory-scoring model on user feedback, you probably need far fewer labels than you think; the pretrained prior is doing most of the work.
- **Re-pretrain the encoder when your test corpus leaked into its training (ENGRAM: G)**: For TREC-CAR, the authors re-pretrained BERT on only the Wikipedia half allowed by their train split, because the official BERT was pretrained on all of Wikipedia (which includes the TREC-CAR test set). Provenance/Ground: your retrieval model's pretraining corpus is a hidden source of test leakage. If your memory system uses an off-the-shelf embedding model, audit what it has already seen.
- **Truncation policy is a load-bearing detail (ENGRAM: E)**: They truncate the query to ≤64 tokens and the passage to fit `query + passage + separators ≤ 512` total. Whatever you write into your retrieval unit beyond that length is, for the reranker's purposes, invisible. Memory shapes that exceed the cross-encoder context window (multi-page docs, long agent traces) silently lose their tails at score time — chunk first, score second.
- **Two-tier scoring beats end-to-end neural retrieval in 2019 (ENGRAM: N, R)**: The win comes from accepting the polyglot shape — keep BM25 (sparse inverted index) for recall, add BERT (dense transformer) for precision. Resist the urge to replace BM25 with a single neural model; that wasn't yet the dominant pattern in 2019 and the cross-encoder reranker over a sparse first stage is still a strong default in 2026 (especially since dense bi-encoders still under-perform BM25 on out-of-distribution queries).
- **The candidate ceiling caps your accuracy (ENGRAM: R)**: BM25 only retrieves 1,000 candidates on MS MARCO dev, and the corpus was built by scraping Bing's top-10 plus annotator labels — so some relevant passages don't appear in the top-1,000 BM25 returns and the reranker cannot recover them. No reranker can score a candidate it never sees. If your retrieval recall@K is poor, the cross-encoder cannot save you — invest in the recall tier first, then the rerank tier.
- **Open the code, get the gains (ENGRAM: M)**: The authors published the full implementation (github.com/nyu-dl/dl4marco-bert). The pattern propagated immediately — by 2020-2021, BERT-style cross-encoder rerankers were the default second stage in BEIR, ColBERT, and nearly every production retrieval pipeline. Maintainability lesson: when you ship a memory architecture, ship the training script — the diffusion speed is what determines whether your idea becomes a primitive.

## How to Apply It (method)

**Scenario:** You're a memory-architecture researcher running the ENGRAM bench: you have an agent-memory system with ~500k stored memory chunks (markdown notes, doc snippets, prior agent traces). Hybrid BM25+embedding search returns the top-100 hits for any query, but precision at the top-10 is weak — the right memory is often retrieved into the candidate set but not surfaced at the top. You want to add a cross-encoder rerank stage à la Nogueira & Cho before generation consumes it.

**Steps:**

1. **Confirm the recall ceiling first**: For 100 representative queries, manually label the top-100 candidates from your current retriever. Compute recall@100 — the fraction of queries where the correct memory is somewhere in the top-100. If recall@100 < 80%, fix the recall tier (better BM25 tuning, query rewriting, or denser embedding model) before adding a reranker — no reranker recovers a candidate the retriever never returned. (Mirrors the MS MARCO caveat: relevant passages outside BM25's top-1,000 are unreachable for the BERT reranker.)

2. **Choose a cross-encoder base**: In 2019 the authors used `bert-large-uncased` (340M params, 24 layers). In 2026 use a modern instruction-tuned cross-encoder — `BAAI/bge-reranker-v2-m3`, `mxbai-rerank-large-v1`, or `cohere-rerank-3.5`. The architectural pattern is the same: a single transformer that ingests `[CLS] query [SEP] passage [SEP]` and emits a relevance score.

3. **Build the training pairs**: For each labeled query, take the *correct* memory chunk as a positive and 7-15 *incorrect* memories sampled from the same top-100 retrieved set as hard negatives (NOT random negatives from elsewhere in the store — the paper uses BM25-retrieved non-relevant passages, which is the hard-negatives recipe). This is the standard "in-batch hard negatives" pattern.

   ```
   query: "What did Adler 2026 say about Mem0's encoding gate?"
   pos:   "Adler argues write-time LLM distillation is anti-intelligence
           because anything dropped pre-query is unrecoverable..."
   negs:  [
     "Mem0g adds a knowledge graph layer on top of LLM-extracted memories...",
     "Packer 2023 frames the context window as a virtual-memory tier...",
     ...
   ]
   ```

4. **Apply the truncation policy**: Truncate the query to ≤64 tokens. Truncate the passage so `query + passage + 3 separator tokens ≤ context_window` (512 for original BERT, 8k+ for modern rerankers). For agent memories longer than the window, chunk first — score chunks, then aggregate per memory by max-pool or sum.

5. **Fine-tune with cross-entropy**: Frame each `(query, passage)` pair as binary classification. Loss is `L = − Σ_pos log(s_j) − Σ_neg log(1 − s_j)` (equation 1 of the paper). Adam, learning rate `3e-6`, β1=0.9, β2=0.999, L2 weight decay 0.01, 10k warmup steps, linear decay, dropout 0.1. Batch size 128 sequences × 512 tokens = 65,536 tokens per batch.

6. **Train for ~12.8M pairs, then stop**: The paper trained for 100k iterations on MS MARCO and saw no improvement past that point even after 3 more days (~50M total pairs seen). Use the dev set to detect this plateau. Don't burn compute past it — the pretrained prior + a small task-specific signal is the whole game.

7. **Score with the reranker over your retriever's top-K**: At query time, take the top-100 (or top-1,000) from hybrid recall, batch-score each `(query, candidate)` pair through the cross-encoder, sort by score, return top-5 to the agent. Latency budget: ~50-200ms for 100 candidates on a single GPU with a modern reranker.

8. **Audit pretraining-corpus leakage**: List every corpus your cross-encoder was pretrained on. If your evaluation memories were sourced from any of them (Wikipedia, Reddit, Common Crawl), your offline eval numbers are inflated. The paper re-pretrained BERT on only the TREC-CAR-allowed half of Wikipedia precisely to avoid this — for memory systems, this means: hold out a recently-added private subset of memories as your eval set, where no pretraining contamination is possible.

**Expected outcome:** A two-tier retrieval pipeline whose top-5 precision lifts substantially over hybrid-search-alone, at the cost of one extra batched transformer call per query. ENGRAM-wise, the Retrieve dimension goes from cheap-but-imprecise to cheap-recall + precise-rerank, without changing what you Encode, where you Network, how you Ground, what you Aggregate, or how you Maintain. The pattern is composable: every existing memory system can bolt on a reranker without touching its other five dimensions.

## Best Figure

![Figure 1 — Number of MS MARCO examples seen during training vs. MRR@10 performance (page 3)](figures/nogueira-2019-bert-passage-reranking-fig.png)

Image Candidates:
Figure 1 (p. 3): Log-scale training-curve overlay showing BERT Large blowing past IR-NET's SOTA at just 100k training pairs and then plateauing — the entire paper's argument in one chart.
Table 1 (p. 3): Tabular comparison of BM25, three prior neural rerankers, and BERT Base/Large on MS MARCO and TREC-CAR — shows the absolute gap but lacks the data-efficiency dimension.
(No Figure 2 in the paper.)

Best Image:
Figure Name: Figure 1: "Number of MS MARCO examples seen during training vs. MRR@10 performance"
Figure Page: 3
Slide Caption: BERT Large blows past the previous SOTA at just 100k training pairs and plateaus by 12.8M — pretraining does most of the work.
Description: A log-scale line chart with the number of training query-passage pairs on the x-axis (from 1k to 100M) and MRR@10 on the y-axis (0 to 0.4). BERT Large is plotted as connected blue diamonds; the previous SOTA (IR-NET, ~0.28 MRR@10) is plotted as a horizontal dashed line. BERT Large crosses the IR-NET line between 10k and 100k training pairs and continues climbing to ~0.37 by 10M pairs, where it plateaus. The figure does two things simultaneously: it proves data-efficiency (you don't need the full 400M training set — 2% gets you there) and it visualizes the gap-to-SOTA closing inside a single order of magnitude of training pairs. For a memory-architecture audience, this is the headline: when the encoder carries the right prior, the task-specific layer needs almost no labeled data.

## What Experts Overlook

Most readers walk away with "use BERT as a reranker, +27% MRR." The detail they miss is the TREC-CAR pretraining hack in Section 3.2: the authors did not use the official `bert-large-uncased` checkpoint for TREC-CAR. They re-pretrained BERT from scratch on only the half of Wikipedia included in TREC-CAR's training fold, because the released BERT model had already seen all of Wikipedia — including the test-set documents — during its unsupervised pretraining. They explicitly call this out as "to avoid this leak of test data into training." A retrieval benchmark whose corpus is Wikipedia, evaluated with a model whose pretraining corpus is also Wikipedia, has no clean train/test split — the encoder has already memorized the test documents.

**Why it matters:** This is a Ground (provenance) issue dressed up as a Retrieve (recall) issue. The headline number — BERT Large achieving 33.5 MAP on TREC-CAR — is only honest because of this re-pretraining step. Without it, the model would have been scored on documents it had already seen as a language-modeling task, and the gain over BM25 would have been partly memorization, not generalization. For anyone building a memory system on top of off-the-shelf embedding or reranker models in 2026, the same trap applies: if the pretraining corpus of your encoder overlaps with the documents you're evaluating recall against, your evaluation is overstating the model's ability to handle genuinely novel content.

**Example of good use:** A memory-architect benchmarking a retrieval pipeline holds out the last 30 days of newly-added memories as the eval set. None of those memories existed when the encoder was pretrained or fine-tuned, so retrieval accuracy on them is a clean measure of generalization, not memorization. They report this measure alongside their LongMemEval / LoCoMo numbers and explicitly note any benchmark whose corpus was likely in the encoder's pretraining set.

**Example of misapplication:** A team building an enterprise-knowledge agent benchmarks recall on a publicly-known dataset like NaturalQuestions (Wikipedia-based) using `bge-large-en-v1.5` as the embedding model. They publish a recall@10 of 0.91 and conclude their pipeline is production-ready. Their actual customers will have private documents the encoder has never seen, where recall is closer to 0.62 — and they only discover this in week 3 of the rollout when sales engineers start complaining. The Nogueira-style fix is to either re-pretrain (impractical) or to construct an eval corpus the encoder demonstrably never saw, and treat the public-benchmark number as a leaky upper bound.

## Extracted Prompts

No applicable prompts found in this paper.

(The paper uses BERT as a binary classifier over token embeddings — the input is `[CLS] query [SEP] passage [SEP]` fed as token IDs, not a natural-language prompt to a generative LLM. No prompt engineering is involved.)

## Citations

(22 references in the paper's bibliography — full list in frontmatter `citations[]`. Top 10 below.)

- **BERT** — Devlin et al., 2018 — `arXiv:1810.04805` — the pretrained encoder this paper fine-tunes
- **MS MARCO** — Nguyen et al., 2016 — `arXiv:1611.09268` — the main benchmark dataset (1M real queries, ~400M training pairs)
- **TREC-CAR overview** — Dietz et al., 2017 — TREC — the second benchmark
- **Anserini (BM25 baseline tooling)** — Yang et al., 2018 — JDIQ — toolkit used to index and retrieve top-1,000 candidates
- **The Neural Hype and Comparisons Against Weak Baselines** — Lin, 2019 — directly cited as the methodological warning that pre-BERT neural rankers under-performed classical IR on strong baselines
- **OpenAI GPT** — Radford et al., 2018 — companion pretraining-paradigm reference
- **ELMo / Semi-supervised Sequence Tagging with BLMs** — Peters et al., 2017 — `arXiv:1705.00108` — the third pretrained-LM reference in the framing
- **KNRM (End-to-End Neural Ad-hoc Ranking with Kernel Pooling)** — Xiong et al., 2017 — SIGIR — neural-ranking baseline in Table 1
- **Conv-KNRM** — Dai et al., 2018 — WSDM — second neural-ranking baseline in Table 1
- **Co-PACRR** — Hui et al., 2018 — WSDM — third neural-ranking baseline
- *(12 more in frontmatter — Adam, SQuAD, SearchQA, TriviaQA, Quasar-T, BiDAF, DrQA, DocumentQA, QAnet, DUET, DRMM, Co-PACRR variants)*

## Related Digests

- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall (uses BM25+vector hybrid recall with cross-encoder reranking — the exact two-stage shape this paper popularized)
- [[gao-2022-hyde-zero-shot-retrieval]] — Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE) (alternative path to better recall — generate a hypothetical answer first, then retrieve; complementary to BERT reranker which improves precision over an existing recall set)
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects (a downstream "Recall" operation in a 2025 agent-memory framework that still relies on a reranker stage built on the cross-encoder pattern established here)

## Reviewer Notes

**Overall severity:** Clean

Every numeric claim, methodological detail, and architectural choice in the digest is taken directly from the paper text:

- MRR@10 numbers (16.7, 21.8, 27.8, 29.0, 34.7, 36.5) — Table 1 in paper
- 27% relative MRR@10 improvement — paper abstract
- TREC-CAR MAP numbers (12.3, 14.8, 15.3, 31.0, 33.5) — Table 1
- 400M training tuples — Section 3.1
- 12.8M training pairs / 100k iterations / 30 hours on TPU v3-8 — Section 3.1 "Training"
- 50M pairs / 3 days saw no improvement — Section 3.1 "Training"
- Hyperparameters (Adam, lr 3e-6, β1=0.9, β2=0.999, L2 wd 0.01, 10k warmup, dropout 0.1) — Section 3.1 "Training"
- Batch size 128 × 512 tokens = 65,536 tokens/batch — Section 3.1
- Query truncated to ≤64 tokens; query+passage+seps ≤ 512 — Section 2 "Method"
- TREC-CAR Wikipedia leakage workaround (re-pretrain on half of Wikipedia) — Section 3.2 "Training"
- 30M TREC-CAR training pairs (3M queries × 10 passages); 400k iterations × 32 = 12.8M examples = 40% of training set — Section 3.2
- 100k pairs = 0.3% of MS MARCO data, 1.4 MRR@10 over IR-NET — Section 3.3 "Training size vs performance"
- BM25 candidate-ceiling caveat (corpus built from Bing top-10) — Section 3.1
- Cross-entropy loss formula — Equation (1)
- Code release URL `github.com/nyu-dl/dl4marco-bert` — paper abstract

Framing claims (e.g., "ENGRAM dimension mapping", "cross-encoder format is the unlock", "2026-era reranker options") are clearly labeled as the digest's interpretation/extrapolation rather than paper assertions, and are scoped accurately.

No fabricated metrics, no invented experiments, no overextended generalizations identified.
