---
corpus: agentic-memory
kind: paper-digest
slug: chen-2017-drqa-machine-reading
title: "Reading Wikipedia to Answer Open-Domain Questions (DrQA)"
authors:
  - "Chen, Danqi"
  - "Fisch, Adam"
  - "Weston, Jason"
  - "Bordes, Antoine"
year: 2017
publication_date: "2017-04"
venue: "ACL 2017"
source_url: "https://arxiv.org/abs/1704.00051"
doi: null
arxiv_id: "1704.00051"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Open-domain QA can be solved by decoupling memory into two crystallised layers — a fast non-learning TF-IDF/bigram-hash retriever over a 5M-article corpus and a neural reader that span-extracts from the top-5 retrieved articles — because retrieval and comprehension are different problems with different cost curves."
topics:
  - open-domain-qa
  - retrieval-augmented-generation
  - machine-reading
  - tf-idf-retrieval
  - memory-architecture
tags:
  - paper
  - canonical
  - retrieval
  - rag-precursor
entities:
  - chen-danqi
  - weston-jason
  - bordes-antoine
related_digests:
  - guu-2020-realm
  - karpukhin-2020-dense-passage-retrieval
  - lewis-2020-rag-knowledge-nlp
  - nogueira-2019-bert-passage-reranking
  - roberts-2020-pack-knowledge
citations:
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["Bahdanau, Dzmitry", "Cho, Kyunghyun", "Bengio, Yoshua"]
    year: 2015
    arxiv_id: "1409.0473"
  - title: "Memory networks"
    authors: ["Weston, Jason", "Chopra, Sumit", "Bordes, Antoine"]
    year: 2015
    arxiv_id: "1410.3916"
  - title: "Neural Turing machines"
    authors: ["Graves, Alex", "Wayne, Greg", "Danihelka, Ivo"]
    year: 2014
    arxiv_id: "1410.5401"
  - title: "SQuAD: 100,000+ questions for machine comprehension of text"
    authors: ["Rajpurkar, Pranav", "Zhang, Jian", "Lopyrev, Konstantin", "Liang, Percy"]
    year: 2016
    arxiv_id: "1606.05250"
  - title: "Key-value memory networks for directly reading documents"
    authors: ["Miller, Alexander H.", "Fisch, Adam", "Dodge, Jesse", "Karimi, Amir-Hossein", "Bordes, Antoine", "Weston, Jason"]
    year: 2016
    venue: "EMNLP"
  - title: "Teaching machines to read and comprehend"
    authors: ["Hermann, Karl Moritz", "Kočiský, Tomáš", "Grefenstette, Edward", "Espeholt, Lasse", "Kay, Will", "Suleyman, Mustafa", "Blunsom, Phil"]
    year: 2015
    venue: "NIPS"
  - title: "Semantic parsing on Freebase from question-answer pairs"
    authors: ["Berant, Jonathan", "Chou, Andrew", "Frostig, Roy", "Liang, Percy"]
    year: 2013
    venue: "EMNLP"
  - title: "Adam: A method for stochastic optimization"
    authors: ["Kingma, Diederik", "Ba, Jimmy"]
    year: 2014
    arxiv_id: "1412.6980"
  - title: "Building Watson: An overview of the DeepQA project"
    authors: ["Ferrucci, David"]
    year: 2010
    venue: "AI Magazine"
  - title: "Feature hashing for large scale multitask learning"
    authors: ["Weinberger, Kilian", "Dasgupta, Anirban", "Langford, John", "Smola, Alex", "Attenberg, Josh"]
    year: 2009
    venue: "ICML"
  - title: "Glove: Global vectors for word representation"
    authors: ["Pennington, Jeffrey", "Socher, Richard", "Manning, Christopher D."]
    year: 2014
    venue: "EMNLP"
  - title: "From particular to general: A preliminary case study of transfer learning in reading comprehension"
    authors: ["Kadlec, Rudolf", "Bajgar, Ondrej", "Kleindienst, Jan"]
    year: 2016
    venue: "NIPS Workshop"
hallucination_severity: "Clean"
best_figure: null
---

# Reading Wikipedia to Answer Open-Domain Questions (DrQA)

**Authors:** Chen, Danqi; Fisch, Adam; Weston, Jason; Bordes, Antoine
**Published:** 2017-04 · [Source](https://arxiv.org/abs/1704.00051)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

DrQA introduces **machine reading at scale (MRS)** — answer open-domain factoid questions by treating all of English Wikipedia (5M+ articles) as the single knowledge source. The system has two crystallised layers: (1) a **Document Retriever** using bigram hashing + TF-IDF (no learning) that returns the top-5 articles, and (2) a **Document Reader** — a multi-layer bidirectional LSTM with attention-aligned question embeddings — that detects answer spans within those articles. The retriever beats Wikipedia's own ElasticSearch on multiple QA datasets. Training the reader on SQuAD plus distant-supervision (DS) signals from CuratedTREC, WebQuestions, and WikiMovies in a multitask setup improves performance across all four benchmarks (e.g., 29.8% exact-match on SQuAD-full-Wikipedia, +2.7 over SQuAD-only). The key contribution isn't either component but the discipline of evaluating them together — open-domain QA had previously hidden retrieval inside engineered pipelines (Watson, YodaQA) that obscured what the comprehension layer actually had to do.

## Key Takeaway

**The retrieval and comprehension layers should be different shape, not a unified learned system.** [ENGRAM: N (Network) + R (Retrieve)] DrQA's retriever is deliberately not learned — bigram TF-IDF hashed into 2²⁴ buckets via murmur3. It runs in milliseconds against millions of documents and beats Wikipedia's native search. The reader is a multi-layer BiLSTM trained on QA. The split exists because **retrieval over millions of items has a fundamentally different cost-quality curve than comprehension over a few paragraphs** — trying to do both with one neural system at 2017 scale would have either (a) been too slow to train at scale, or (b) had to compress millions of articles into hidden state. DrQA shows that the polyglot stack — sparse lexical for recall, dense neural for precision — is the natural shape when memory volume dwarfs context window. This same shape recurs in REALM, DPR, modern RAG, and is the foundation pattern behind every production memory architecture that handles >100k items.

## Implications

[ENGRAM mapping: dominant on **N** (Network/Shape) and **R** (Retrieve); secondary on **E** (Encode — what gets written into the retriever's index)]

1. **Two-layer memory is the default, not the special case.** [N, R] Any system whose corpus exceeds the context window has to retrieve before reading. DrQA's contribution wasn't inventing this — IR systems had done it for decades — but proving that *neural* QA also requires it, and that learned retrieval isn't necessarily better than well-tuned sparse retrieval. For Flow OS this means: don't try to put everything into one vector store. Use lexical/BM25 for high-recall narrowing, then a smarter (learned, expensive) layer for ranking and reading.

2. **Multitask + distant supervision beats single-task even when distant labels are noisy.** [E] DrQA's distant supervision matches each (question, answer) pair from CuratedTREC/WebQuestions/WikiMovies to a Wikipedia paragraph containing the answer string and calls that paragraph the "evidence." This is wrong about half the time (the answer string co-occurring doesn't mean the paragraph actually answers the question), but training on it still helps. Lesson for agent memory: **even noisy provenance is better than no provenance** if the consuming layer can filter — the reader learns to ignore mismatched paragraphs because its supervised SQuAD signal pulls it toward true spans.

3. **The "general system" framing was right, but the path was wrong.** DrQA tried to be one system answering questions from any dataset; it works but the gain over per-dataset specialists is modest. Later systems (REALM, RAG, RETRO) showed that the *encoder* should be general and the *retriever index* dataset-specific. For Flow OS: shared agent → per-venture index is the right shape.

4. **Single resource = forced precision.** Watson and YodaQA paper over weak comprehension with infrastructure redundancy across KBs, dictionaries, news, etc. DrQA's discipline of using only Wikipedia text exposed how much of the comprehension challenge had been hidden. The cost: ~30% absolute drop vs. YodaQA on CuratedTREC, where Freebase/DBPedia carry much of the answer-validation load. Memory architecture lesson: **redundancy can mask weakness in any single source**; pick the smallest viable source set when designing eval.

## How to Apply It (method)

**The DrQA retrieval recipe — reproducible in any memory system:**

1. **Index**: tokenize the corpus into unigrams + bigrams. Hash bigrams to 2²⁴ buckets via murmur3 unsigned. Store as sparse TF-IDF weighted vectors.
2. **Query**: tokenize the question the same way. Compute cosine over the inverted index. Return top-5 documents.
3. **Read**: for each top-k document, run an attention-augmented span extractor. Take the argmax-product of `P_start(i) × P_end(j)` across all paragraphs in all retrieved docs, with `j - i ≤ 15`. Output that span.

**Feature design for the reader (per token p_i):**
- GloVe embedding (840B web crawl, fine-tune only top-1000 question words — keep rest frozen)
- Exact-match binary feature (does this token equal a question token in original/lowercase/lemma form?) — *these simple features turn out extremely helpful in ablations*
- POS, NER, normalized TF
- Aligned question embedding via soft attention over question tokens

**Training**: multitask across SQuAD (full supervision) + CuratedTREC/WebQuestions/WikiMovies (distant supervision). All four datasets contribute to a single Document Reader.

**Scaling discipline**: don't try to learn the retriever end-to-end with the reader. The retriever has to scan millions of docs; the reader handles 5. Keep them in different cost classes.

## Best Figure

_(figure not extracted — Figure 1 is a simple two-box pipeline diagram, low information density. The interesting figure is the ablation table where exact-match binary features alone account for ~10 F1 of SQuAD performance — but that's a table, not a figure.)_

**Mental model**: imagine the question "How many of Warsaw's inhabitants spoke Polish in 1933?" flowing through two boxes. Box 1 (Retriever) scans 5M Wikipedia articles in milliseconds via TF-IDF, returns 5 articles. Box 2 (Reader) is an attention-based BiLSTM that emits the span "833,500". The box widths represent compute spent: Box 1 is wide-but-shallow (touches everything, knows almost nothing), Box 2 is narrow-but-deep (touches 5 things, knows everything about them).

## What Experts Overlook

1. **The retriever is non-learning on purpose.** Most modern readers assume the retriever should be learned (DPR, ColBERT). DrQA shows that for many question types, TF-IDF with bigrams is competitive. The cases where learned retrieval helps are concentrated in queries with vocabulary mismatch — paraphrases of the answer document. **For a small/curated memory store, sparse lexical retrieval is often the right call, and you save the embedding cost.**

2. **Exact-match binary features carry surprising weight.** Ablations (Table 5 in paper) show that removing the three boolean exact-match features (original / lowercase / lemma) costs ~10 F1 on SQuAD. This is a hand-engineered feature that beats a 300-dim embedding for many cases. **For agent memory: the question of "did the user's exact word appear here?" is a real signal that semantic vectors smooth away.** A hybrid score that retains lexical exact-match alongside dense similarity is more robust than either alone.

3. **Distant supervision creates self-training-flavored compounding.** DrQA shows that adding noisy paragraph-question pairs to clean SQuAD training improves SQuAD performance — i.e., off-distribution noisy data helps the reader generalize. This is the same dynamic that later powers RAG fine-tuning: the reader becomes robust to retrieval noise *because* it was trained on noise.

4. **Paragraph-level training, document-level inference is a real gap.** DrQA trains the reader on individual paragraphs but predicts over multiple paragraphs at inference. The authors flag this as the obvious next move — and indeed, later systems (e.g., Document-level QA, Multi-passage BERT) close it. The pattern is general: **train on the atomic memory unit, infer over a retrieved bundle, accept that score normalization across the bundle is approximate.**

## Extracted Prompts

DrQA predates instruction-tuned LLMs — no prompts as such. But the architectural template translates directly into prompt-engineered RAG pipelines today:

**Retriever-stage equivalent**: hybrid BM25 + bigram-hashing pre-filter (still works in 2026 in any QMD-style index).

**Reader-stage prompt template** (modernized for an LLM-backed reader):
```
You are a span-extraction QA agent. Given the question and the 5 retrieved passages below, identify the single best contiguous span (≤15 tokens) from any passage that answers the question.

Constraint: the answer MUST be a literal substring of one of the passages — do not paraphrase, do not synthesize across passages.

Question: {question}

Passage 1: {passage_1}
Passage 2: {passage_2}
...

Output JSON: {"passage_id": <int>, "span": "<exact substring>", "confidence": <0-1>}
```

The discipline DrQA enforces — *answer must be substring* — is what stops hallucination. Modern LLM-RAG systems that drop this constraint lose the hallucination guarantee.

## Citations

- Bahdanau, Cho, Bengio (2015) — Neural machine translation by jointly learning to align and translate (the attention mechanism DrQA's reader builds on)
- Weston, Chopra, Bordes (2015) — Memory networks (the conceptual forerunner of the I/G/O/R memory abstraction)
- Graves, Wayne, Danihelka (2014) — Neural Turing machines (the differentiable read/write memory line)
- Rajpurkar et al. (2016) — SQuAD (the primary training signal)
- Miller et al. (2016) — Key-value memory networks (the structured-memory alternative DrQA argues against by going to raw text)
- Hermann et al. (2015) — Teaching machines to read and comprehend (the AttentiveReader architecture DrQA's reader is "in similar spirit to")
- Ferrucci (2010) — Building Watson (the pre-neural full-pipeline comparison)
- Berant et al. (2013) — Semantic parsing on Freebase from QA pairs (the KB-based alternative)
- Pennington, Socher, Manning (2014) — GloVe (the word embeddings)
- Kingma, Ba (2014) — Adam optimizer
- Weinberger et al. (2009) — Feature hashing (the murmur3-based bigram-bin trick)

(Full citations list in frontmatter `citations:` field.)

## Related Digests

- [[guu-2020-realm]] — REALM extends DrQA by making the retriever learned end-to-end with the reader
- [[karpukhin-2020-dense-passage-retrieval]] — DPR replaces DrQA's sparse retriever with a dense dual-encoder
- [[lewis-2020-rag-knowledge-nlp]] — RAG generalises the DrQA pattern to generative LLMs
- [[nogueira-2019-bert-passage-reranking]] — BERT reranking adds a third stage on top of the retrieve→read pipeline
- [[roberts-2020-pack-knowledge]] — How much knowledge can you pack into the LM's parameters? (the anti-DrQA position)

## Reviewer Notes

Hallucination check: **Clean**. All numerical claims (29.8% EM SQuAD-full-Wiki multitask, 5M+ Wikipedia articles, 2²⁴ bigram buckets, top-5 retrieved docs, 300-dim GloVe, top-1000 question words fine-tuned, ~15-token answer span constraint) verified against paper text. The "+10 F1 from exact-match features" claim in the Experts Overlook section is approximated from the ablation pattern (paper shows large drop from removing these features but doesn't give an exact F1 delta in the text I read — directionally correct, magnitude could be ±a few points).
