---
corpus: agentic-memory
kind: paper-digest
slug: dunn-2017-searchqa-dataset
title: "SearchQA: A New Q&A Dataset Augmented with Context from a Search Engine"
authors:
  - "Dunn, Matt"
  - "Sagun, Levent"
  - "Higgins, Mike"
  - "Güney, V. Uğur"
  - "Cirik, Volkan"
  - "Cho, Kyunghyun"
year: 2017
publication_date: "2017-06"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/1704.05179"
doi: null
arxiv_id: "1704.05179"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Building a question-answering corpus by working backwards from real Jeopardy! Q&A pairs and then attaching whatever Google actually returns produces a dataset where humans only hit ~57% F1 and the best neural reader (Attention Sum Reader) hits ~23% — proving that the bottleneck in real-world QA is not reading comprehension but coping with noisy, partially-relevant retrieved snippets, the exact regime any production memory system operates in."
topics:
  - question-answering
  - retrieval-augmented-qa
  - benchmark-dataset
  - noisy-context
  - machine-reading-comprehension
tags:
  - paper
  - dataset
  - retrieval
  - benchmark
  - attention-sum-reader
  - jeopardy
entities:
  - dunn-matt
  - cho-kyunghyun
  - sagun-levent
related_digests:
  - chen-2017-drqa-machine-reading
  - bajaj-2016-ms-marco
  - karpukhin-2020-dense-passage-retrieval
  - lewis-2020-rag-knowledge-nlp
  - roberts-2020-pack-knowledge
citations:
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["Dzmitry Bahdanau", "Kyunghyun Cho", "Yoshua Bengio"]
    year: 2014
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1409.0473"
    arxiv_id: "1409.0473"
  - title: "Large-scale simple question answering with memory networks"
    authors: ["Antoine Bordes", "Nicolas Usunier", "Sumit Chopra", "Jason Weston"]
    year: 2015
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1506.02075"
    arxiv_id: "1506.02075"
  - title: "Learning phrase representations using RNN encoder-decoder for statistical machine translation"
    authors: ["Kyunghyun Cho", "Bart van Merrienboer", "Caglar Gulcehre", "et al."]
    year: 2014
    venue: "EMNLP 2014"
    doi: null
    url: null
    arxiv_id: null
  - title: "Teaching machines to read and comprehend"
    authors: ["Karl Moritz Hermann", "Tomas Kocisky", "Edward Grefenstette", "et al."]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "The Goldilocks principle: Reading children's books with explicit memory representations"
    authors: ["Felix Hill", "Antoine Bordes", "Sumit Chopra", "Jason Weston"]
    year: 2015
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1511.02301"
    arxiv_id: "1511.02301"
  - title: "Text understanding with the attention sum reader network"
    authors: ["Rudolf Kadlec", "Martin Schmid", "Ondrej Bajgar", "Jan Kleindienst"]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1603.01547"
    arxiv_id: "1603.01547"
  - title: "Adam: A method for stochastic optimization"
    authors: ["Diederik Kingma", "Jimmy Ba"]
    year: 2014
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1412.6980"
    arxiv_id: "1412.6980"
  - title: "ImageNet classification with deep convolutional neural networks"
    authors: ["Alex Krizhevsky", "Ilya Sutskever", "Geoffrey E. Hinton"]
    year: 2012
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "MS MARCO: A human generated machine reading comprehension dataset"
    authors: ["Tri Nguyen", "Mir Rosenberg", "Xia Song", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1611.09268"
    arxiv_id: "1611.09268"
  - title: "Who did what: A large-scale person-centered cloze dataset"
    authors: ["Takeshi Onishi", "Hai Wang", "Mohit Bansal", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1608.05457"
    arxiv_id: "1608.05457"
  - title: "SQuAD: 100,000+ questions for machine comprehension of text"
    authors: ["Pranav Rajpurkar", "Jian Zhang", "Konstantin Lopyrev", "Percy Liang"]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1606.05250"
    arxiv_id: "1606.05250"
  - title: "Dropout: a simple way to prevent neural networks from overfitting"
    authors: ["Nitish Srivastava", "Geoffrey E. Hinton", "Alex Krizhevsky", "et al."]
    year: 2014
    venue: "Journal of Machine Learning Research"
    doi: null
    url: null
    arxiv_id: null
  - title: "NewsQA: A machine comprehension dataset"
    authors: ["Adam Trischler", "Tong Wang", "Xingdi Yuan", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1611.09830"
    arxiv_id: "1611.09830"
  - title: "Pointer networks"
    authors: ["Oriol Vinyals", "Meire Fortunato", "Navdeep Jaitly"]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Achieving human parity in conversational speech recognition"
    authors: ["Wayne Xiong", "Jasha Droppo", "Xuedong Huang", "et al."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1610.05256"
    arxiv_id: "1610.05256"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "One example in .json format"
  page: 2
  image_path: "figures/dunn-2017-searchqa-dataset-fig.png"
---

# SearchQA: A New Q&A Dataset Augmented with Context from a Search Engine

**Authors:** Matt Dunn, Levent Sagun, Mike Higgins, V. Uğur Güney, Volkan Cirik, Kyunghyun Cho
**Published:** 2017-06 · [Source](https://arxiv.org/abs/1704.05179)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

SearchQA inverts the usual machine-reading-comprehension data-construction pipeline: instead of starting from a clean article and writing a question against it, the authors crawl 140,461 trivia question-answer pairs from J! Archive (the Jeopardy! fan archive), fire each question at production Google, keep the top ~50 snippets per question (49.6±2.1 on average, 37.3±11.7 tokens each, 6.9M snippets total, 1.26M unique tokens), and filter to tuples where the answer (≤3 words) appears somewhere in the noisy retrieved context. Splits are temporal (99,820 train / 13,393 valid / 27,248 test, with later years held out), so generalisation is tested against future questions, not random shuffles. Thirteen NYU master's volunteers averaged 47 questions each: 66.97% top-1 on unigram answers, 42.86% on n-gram, and only 57.62% F1 — already low because the snippets are excerpts not full sentences. A naïve TF-IDF-max baseline (pick the highest-TF-IDF word) hits 13% unigram top-1. The Attention Sum Reader (Kadlec 2016, 100-unit GRU, Adam + dropout), extended with a small second recurrence so it can emit multi-word answers, reaches 41.3% unigram top-1 / 65.1% top-5 / 22.8% F1 on the n-gram test set. The actionable takeaway: a meaningful human-machine gap exists, but the *real* difficulty exposed by SearchQA is not reading comprehension over clean text — it is operating over a noisy, partially-relevant retrieved bundle, which is the regime every production memory + retrieval architecture lives in.

## Key Takeaway

The interesting failure mode isn't the model — it's the humans. When you stop hand-curating context and let an actual search engine choose the snippets, NYU master's-level students drop to **57.62% F1** and the strongest neural reader of the day lands at 22.8%. Both numbers say the same thing: comprehension is not the bottleneck in real-world QA. The bottleneck is reasoning across a smear of partially-relevant excerpts that were chosen by some other system you don't control. Every memory architect designing a "RAG works" pipeline is implicitly betting the gap between SQuAD-style 90%+ scores and SearchQA's 57% can be closed by a better retriever — but Dunn et al. show that even when a real production retriever is doing its best, *humans* can't reach 60%. That's a sobering ceiling on what extractive QA over snippets can structurally deliver.

## Implications

- **[ENGRAM: Encode + Retrieve] Build your benchmark backwards from real queries, not forward from clean documents**: Almost every QA dataset in 2017 (SQuAD, CNN/DailyMail, NewsQA, CBT) generates questions from a pre-selected clean context — which silently bakes in the assumption that retrieval is solved. For a memory system, do the inverse: start from real user questions you logged, retrieve with your actual production retriever, and grade on whether the answer is recoverable. SearchQA's method is directly transferable.
- **[ENGRAM: Network] Snippet-as-retrieval-unit is a real architectural choice, not a default**: The paper treats Google snippets (≈37 tokens, often sentence fragments) as the atomic memory unit. Document-tree and graph systems should consciously ask: what's the smallest chunk a downstream reader can still answer from? 37 tokens is enough for 41% unigram accuracy here — useful calibration when sizing chunks for your own retriever.
- **[ENGRAM: Ground] A human ceiling below 60% F1 is a provenance signal, not a model failure**: When humans can't reach the upper bound on your benchmark, your retrieval pipeline is dropping ground-truth-bearing context. Use human-ceiling drop as an early-warning that your retriever needs work, before pouring compute into a bigger reader.
- **[ENGRAM: Maintain] Split temporally, not randomly**: Train ≤ 2015, validate 2015–2016, test ≥ 2016 — the authors enforce this because random splits leak entity-level priors. Any memory system facing future queries about evolving entities (people, products, events) should adopt the same discipline; random K-fold over a memory store will systematically overstate generalisation.
- **[ENGRAM: Retrieve] Cheap lexical baselines matter as your floor**: TF-IDF-max gets 13% top-1 just from the questioner's words leaking into Google's snippet ranking. Before claiming a learned retriever is helping, prove it beats this kind of "free" lexical signal — many production "RAG" systems are unknowingly just running expensive TF-IDF.
- **[ENGRAM: Aggregate] A 22.8% F1 multi-word answer score exposes the cost of extractive-only architectures**: ASR can only point at a span in the context; if the answer needs synthesis across snippets, it cannot generate one. For agentic memory, the answer is almost never a single span — design for aggregation/generation from the start rather than retrofitting a span-pointer.
- **[ENGRAM: Encode] Metadata you "won't use" today becomes the audit trail tomorrow**: The authors keep snippet URL, Jeopardy! category, dollar value, show number, air date — even though their baselines ignore them — because future research will. Same discipline applies to a memory store: capture provenance fields at write time even if your current retriever ignores them; you cannot bolt them on later.
- **[ENGRAM: Ground + Encode] Compute-driven filtering shapes the benchmark in ways that matter**: They dropped tuples where the answer string wasn't in the snippets (for training efficiency), and capped answers to ≤3 tokens. Both choices push the dataset towards extractive-friendly questions and away from synthesis. Be explicit about analogous filters in your own corpus or the benchmark will mislead.

## How to Apply It (method)

**Scenario:** You're running an agentic memory system that ingests web/Slack/email content, and you want to know whether your retrieval-and-read pipeline can actually answer your team's questions — not just the easy ones from your CLAUDE.md, but the real, half-remembered, "I think we discussed this in March" kind. You want a *realistic* benchmark whose context resembles what your system retrieves in production, not a curated cleanroom.

**Steps:**

1. **Mine a pool of natural Q&A pairs from your own history**: Pull questions your team has already asked (Slack #help threads, GitHub issue Q&A, customer support tickets). You need question + canonical answer + nothing else. Aim for 1k–10k pairs.

2. **Run each question through your actual production retriever**: For every question, fire it as-is through the same retriever your live system uses (BM25, hybrid, vector — whatever ships). Capture the top-K (here, K≈50) chunks/snippets per question along with their provenance:

   ```yaml
   - question: "When did we decide to drop the Mongo backend?"
     answer: "April 2026"
     snippets:
       - text: "<chunk text>"
         source: "<file or url>"
         retrieval_rank: 1
         retrieval_score: 0.83
   ```

3. **Apply Dunn et al.'s filtering pass — be explicit about every cut**:
   - Drop any tuple where the answer string is not findable in any snippet (this is your *retrieval-floor* filter — these are pairs your retriever physically cannot answer regardless of reader).
   - Cap answer length (they used ≤3 tokens — relax to a domain-appropriate cap, e.g. ≤25 tokens for prose answers).
   - Document every filter as a percentage drop. SearchQA dropped a substantial fraction at the answer-in-context step — knowing your own drop rate tells you the ceiling of any reader.

4. **Temporal split, not random**: Sort by timestamp. Use the oldest ~75% for train (if you're training anything), middle ~10% for validation, newest ~15% for test. This catches drift — new entities, new vocabulary, new internal jargon — which random splits hide.

5. **Run two baselines before any learned model**:
   - **TF-IDF max** (or BM25-max): per question, return the highest-scoring word in the concatenated snippets. This is your "is retrieval already answering the question" floor.
   - **Attention Sum Reader-style extractor**: a 100-unit GRU encoding question and snippets, dot-product attention scoring, sum-by-unique-word normalisation. Use it as your "what does cheap extractive get me" reference. For multi-word answers, add the second GRU that conditions on previously-emitted answer words and predicts `<answer>` to terminate.

6. **Get humans to take the test under retrieval conditions, time-boxed**: Hand 5–10 team members a 40-minute window, show them only the snippet bundle (not the source documents), and let them click words to assemble an answer. Compute per-question accuracy and per-answerer std-dev. *This is the most important step* — it gives you the true ceiling. If humans can't get past 60% F1, you know your retriever is the bottleneck, not your reader.

7. **Report the gap, then close it deliberately**: Tabulate human-vs-baseline-vs-learned gaps separately for unigram (single-word) and n-gram (multi-word) answers. The gap that matters for memory architecture is human-vs-retrieval-floor — if humans can answer and TF-IDF-max already nearly gets it, you don't need a bigger reader. If humans can answer but no machine can, you need better aggregation across snippets, not better retrieval.

**Expected outcome:** A reproducible internal benchmark that tells you, quantitatively, where your memory pipeline breaks: at retrieval (humans can't answer either → fix the retriever first), at extraction (humans can answer but extractive baselines can't → consider generation/aggregation), or at synthesis (humans + extractor both stuck → multi-snippet reasoning is the limiter). You'll also have a temporal-split test set that catches the drift random splits paper over, and a human ceiling that prevents wasting compute chasing scores that aren't achievable.

## Best Figure

![Figure 1 — One example in .json format (page 2)](figures/dunn-2017-searchqa-dataset-fig.png)

**Image Candidates:**
- Figure 1 (p. 2): The single per-tuple JSON record showing how question, answer, and noisy Google snippet metadata sit side-by-side — the entire data-model argument in one view.
- Table 1 (p. 2): Human accuracy table — 66.97% unigram / 42.86% n-gram / 57.62% F1 — the surprise that humans cap out far below SQuAD-style numbers.
- Table 2 (p. 3): Baseline-vs-ASR results across unigram and n-gram conditions, including 41.3% top-1 / 65.1% top-5 / 22.8% F1 — the machine-side of the gap.

**Best Figure:** Figure 1 — *One example in .json format*. The figure shows a single JSON record from the SearchQA dataset for the question "Guinness says that by number of users this language, devised by fictional language..." (answer: "Klingon", round: "Jeopardy!", value: "$1000"), with one search-result snippet from `en.wikipedia.org/wiki/Klingon` carrying URL, snippet text, related_links, title, and air_date metadata. It is the most compelling figure for a memory architect because it is, in effect, the entire ENGRAM-Encode argument of the paper in a single artefact: every record is question + answer + ranked retrieval result + retrieval-time provenance (URL, source title, retrieval date, Jeopardy! show metadata). That metadata-on-write discipline is what makes the dataset reusable across future research (Bordes-style memory networks, Lewis-2020-RAG, DPR all reuse SearchQA structures), and is the single architectural lesson worth copying for any memory system that wants to be auditable downstream.

## What Experts Overlook

Most readers focus on the headline result — humans get 57% F1, machines get 22.8%, big gap, exciting benchmark — and skip past the data-construction detail that actually creates the benchmark's value: the filter that **drops every Q-A pair where the answer string does not appear verbatim inside the retrieved snippets** ("we removed any tuple whose context did not include the answer"). This filter was introduced "mainly for computational efficiency in building a question-answering system using the proposed dataset," but its real effect is to silently anchor SearchQA in the *extractive* regime: every question in the benchmark has an answer that is recoverable by a span-pointer in principle. The paper's reported "gap between human and machine" is therefore a gap over the *extractable* subset of Jeopardy! questions — the harder subset, where the answer needs to be synthesised from multiple snippets or doesn't appear verbatim at all, was filtered out before measurement began.

**Why it matters:** This filter is the difference between SearchQA being a benchmark for "how good is your extractive reader given a noisy snippet bundle" (which it actually is) and "how good is your QA system at real Jeopardy questions" (which it isn't). For a memory architect, the lesson is structural: any benchmark that pre-filters its corpus on the very property your system is being graded on will overstate that system's ability and understate the harder failure modes you care about most. SearchQA's design choice means that systems trained on it learn to be excellent span-pointers and are systematically unaccountable for cases where the answer needs aggregation or paraphrase. The "gap" the paper reports is genuine, but it is a ceiling on extractive readers, not a ceiling on QA itself.

**Example of good use:** A memory architect building a benchmark for an internal RAG system explicitly logs, separately, (a) Q-A pairs where the literal answer appears in at least one retrieved chunk, (b) pairs where it appears only after synthesis across two or more chunks, and (c) pairs where the chunks together imply but never state the answer. They measure their system on each bucket separately and publish all three numbers. Now they know whether they need a better retriever, better aggregation, or generative synthesis — and they don't get fooled by a high overall score driven by bucket (a) being the bulk of traffic.

**Example of misapplication:** A team copies SearchQA's pipeline verbatim for an internal benchmark over their support knowledge base — but their real support questions disproportionately need synthesis across multiple articles (the kind SearchQA filters out). They train and tune against the filtered benchmark, ship a 70% F1 system, and watch it crash to 30% in production because the dropped class — the synthesis-required questions — is dominant in real traffic. The benchmark is misleading specifically because it inherited the extractive-only filter without inheriting the warning that the filter exists.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- Bahdanau et al. (2014) — *Neural machine translation by jointly learning to align and translate* — arXiv 1409.0473
- Bordes et al. (2015) — *Large-scale simple question answering with memory networks* — arXiv 1506.02075
- Cho et al. (2014) — *Learning phrase representations using RNN encoder-decoder for statistical machine translation* — EMNLP 2014
- Hermann et al. (2015) — *Teaching machines to read and comprehend* — NeurIPS
- Hill et al. (2015) — *The Goldilocks principle: Reading children's books with explicit memory representations* — arXiv 1511.02301
- Kadlec et al. (2016) — *Text understanding with the attention sum reader network* — arXiv 1603.01547
- Kingma & Ba (2014) — *Adam: A method for stochastic optimization* — arXiv 1412.6980
- Krizhevsky et al. (2012) — *ImageNet classification with deep convolutional neural networks* — NeurIPS
- Nguyen et al. (2016) — *MS MARCO: A human generated machine reading comprehension dataset* — arXiv 1611.09268
- Onishi et al. (2016) — *Who did what: A large-scale person-centered cloze dataset* — arXiv 1608.05457

(Remaining 5 citations in frontmatter `citations:` array: Rajpurkar/SQuAD, Srivastava/Dropout, Trischler/NewsQA, Vinyals/Pointer Networks, Xiong/Conversational Speech Recognition.)

## Related Digests

- [[chen-2017-drqa-machine-reading]] — Reading Wikipedia to Answer Open-Domain Questions (DrQA)
- [[bajaj-2016-ms-marco]] — MS MARCO: A Human Generated Machine Reading Comprehension Dataset (explicitly contrasted in §3 — the closest peer to SearchQA, differing in choice of search engine + question source)
- [[karpukhin-2020-dense-passage-retrieval]] — Dense Passage Retrieval for Open-Domain Question Answering (a direct successor on the retrieval side of the same pipeline SearchQA stress-tests)
- [[lewis-2020-rag-knowledge-nlp]] — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (the generative answer to SearchQA's extractive-only design limitation)
- [[roberts-2020-pack-knowledge]] — How Much Knowledge Can You Pack Into the Parameters of a Language Model? (the no-retrieval counterpoint that SearchQA's noisy-context world implicitly contests)

## Reviewer Notes

**Overall severity:** Clean

All quantitative claims in the digest (140,461 question-answer pairs, 49.6±2.1 snippets per pair, 37.3±11.7 tokens per snippet, 6.9M snippets, 1,257,327 unique tokens, 99,820/13,393/27,248 train/val/test split, human 66.97% unigram / 42.86% n-gram / 57.62% F1, TF-IDF-Max 13.0 valid / 12.7 test, ASR 41.3% top-1 / 65.1% top-5 / 22.8% F1 on test) are direct quotes from §2 (Basic Statistics, Training/Validation/Test Sets), Table 1, and Table 2 of the paper. The Attention Sum Reader architectural description (two encoders, dot-product attention, sum-by-unique-word, softmax) matches §4.2 verbatim, including the n-gram extension that adds a recurrent network encoding previous answer words and appends an `<answer>` end-token. The model hyperparameters (100 GRU units, Adam optimizer, dropout) match the paper. The extractive-filter critique in *What Experts Overlook* is grounded in the paper's own statement: "we removed any tuple whose context did not include the answer. This was done mainly for computational efficiency." The temporal-split design and the snippet-as-excerpt-not-full-sentence observation are both stated in the paper. No invented metrics, no invented methods, no overextended claims about generation or aggregation capabilities the paper does not test.
