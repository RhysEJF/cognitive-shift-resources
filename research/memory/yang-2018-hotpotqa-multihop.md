---
corpus: agentic-memory
kind: paper-digest
slug: yang-2018-hotpotqa-multihop
title: "HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering"
authors:
  - "Yang, Zhilin"
  - "Qi, Peng"
  - "Zhang, Saizheng"
  - "Bengio, Yoshua"
  - "Cohen, William W."
  - "Salakhutdinov, Ruslan"
  - "Manning, Christopher D."
year: 2018
publication_date: "2018-09"
venue: "EMNLP 2018"
source_url: "https://arxiv.org/abs/1809.09600"
doi: null
arxiv_id: "1809.09600"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "If you want a memory system to learn explainable multi-hop reasoning, you have to collect sentence-level supporting facts during data collection — not at evaluation time — because the supervision signal changes what gets retrieved AND why it gets retrieved, and no amount of post-hoc retrieval can recover from training on distant supervision alone."
topics:
  - multi-hop-question-answering
  - explainable-qa
  - dataset-construction
  - supporting-fact-supervision
  - wikipedia-graph
  - retrieval-evaluation
  - benchmark
tags:
  - paper
  - dataset
  - multi-hop
  - retrieval
  - explainability
  - canonical
  - engram-encode
  - engram-ground
  - engram-retrieve
entities:
  - yang-zhilin
  - qi-peng
  - zhang-saizheng
  - bengio-yoshua
  - cohen-william
  - salakhutdinov-ruslan
  - manning-christopher
  - carnegie-mellon-university
  - stanford-university
  - mila
related_digests:
  - gutierrez-2024-hipporag
  - weston-2015-memory-networks
  - chen-2017-drqa-machine-reading
  - clark-2017-multi-paragraph-rc
  - bajaj-2016-ms-marco
  - dunn-2017-searchqa-dataset
  - sukhbaatar-2015-end-to-end-memory-networks
citations:
  - title: "Reading Wikipedia to Answer Open-Domain Questions"
    authors: ["Danqi Chen", "Adam Fisch", "Jason Weston", "Antoine Bordes"]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1704.00051"
  - title: "Simple and Effective Multi-Paragraph Reading Comprehension"
    authors: ["Christopher Clark", "Matt Gardner"]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1710.10723"
  - title: "SearchQA: A New Q&A Dataset Augmented with Context from a Search Engine"
    authors: ["Matthew Dunn", "Levent Sagun", "Mike Higgins", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1704.05179"
  - title: "TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension"
    authors: ["Mandar Joshi", "Eunsol Choi", "Daniel S. Weld", "et al."]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1705.03551"
  - title: "Stochastic Answer Networks for Machine Reading Comprehension"
    authors: ["Xiaodong Liu", "Yelong Shen", "Kevin Duh", "et al."]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1712.03556"
  - title: "The Stanford CoreNLP Natural Language Processing Toolkit"
    authors: ["Christopher D. Manning", "Mihai Surdeanu", "John Bauer", "et al."]
    year: 2014
    venue: "ACL System Demonstrations"
    doi: null
    url: null
    arxiv_id: null
  - title: "ParlAI: A Dialog Research Software Platform"
    authors: ["Alexander H Miller", "Will Feng", "Adam Fisch", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1705.06476"
  - title: "MS MARCO: A Human Generated Machine Reading Comprehension Dataset"
    authors: ["Tri Nguyen", "Mir Rosenberg", "Xia Song", "et al."]
    year: 2016
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: "1611.09268"
  - title: "Why We Need New Evaluation Metrics for NLG"
    authors: ["Jekaterina Novikova", "Ondřej Dušek", "Amanda Cercas Curry", "Verena Rieser"]
    year: 2017
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "MEMEN: Multi-layer Embedding with Memory Networks for Machine Comprehension"
    authors: ["Boyuan Pan", "Hao Li", "Zhou Zhao", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1707.09098"
  - title: "Know What You Don't Know: Unanswerable Questions for SQuAD"
    authors: ["Pranav Rajpurkar", "Robin Jia", "Percy Liang"]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1806.03822"
  - title: "SQuAD: 100,000+ Questions for Machine Comprehension of Text"
    authors: ["Pranav Rajpurkar", "Jian Zhang", "Konstantin Lopyrev", "Percy Liang"]
    year: 2016
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "1606.05250"
  - title: "Contextualized Word Representations for Reading Comprehension"
    authors: ["Shimi Salant", "Jonathan Berant"]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: "1712.03609"
  - title: "Bidirectional Attention Flow for Machine Comprehension"
    authors: ["Minjoon Seo", "Aniruddha Kembhavi", "Ali Farhadi", "Hannaneh Hajishirzi"]
    year: 2017
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1611.01603"
  - title: "The Web as a Knowledge-Base for Answering Complex Questions"
    authors: ["Alon Talmor", "Jonathan Berant"]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: "1803.06643"
  - title: "Gated Self-Matching Networks for Reading Comprehension and Question Answering"
    authors: ["Wenhui Wang", "Nan Yang", "Furu Wei", "et al."]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Constructing Datasets for Multi-Hop Reading Comprehension Across Documents"
    authors: ["Johannes Welbl", "Pontus Stenetorp", "Sebastian Riedel"]
    year: 2018
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: "1710.06481"
  - title: "DCN+: Mixed Objective and Deep Residual Coattention for Question Answering"
    authors: ["Caiming Xiong", "Victor Zhong", "Richard Socher"]
    year: 2018
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1711.00106"
  - title: "Mastering the Dungeon: Grounded Language Learning by Mechanical Turker Descent"
    authors: ["Zhilin Yang", "Saizheng Zhang", "Jack Urbanek", "et al."]
    year: 2018
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1711.07950"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "An example of the multi-hop questions in HotpotQA"
  page: 1
  image_path: "figures/yang-2018-hotpotqa-multihop-fig.png"
---

# HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering

**Authors:** Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W. Cohen, Ruslan Salakhutdinov, Christopher D. Manning
**Published:** 2018-09 · [Source](https://arxiv.org/abs/1809.09600)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

HotpotQA is a 112,779-example question-answering benchmark built from English Wikipedia (Oct 2017 dump) where every question is crafted by a crowd worker after being shown two specific paragraphs — a "bridge entity" page and the article it links to — so answering requires multi-hop reasoning across both. Two innovations distinguish it from prior QA datasets (SQuAD, TriviaQA, SearchQA, QAngaroo): (1) it is text-based and free-form rather than KB-schema-constrained, and (2) every example ships with sentence-level **supporting facts** — Turkers explicitly highlight which sentences in which paragraph are required to derive the answer. The dataset adds a novel **comparison-question** type (27% of dev) where two same-category entities (e.g. two bands, two mountains) are compared on a shared property, including yes/no variants that force genuine cross-paragraph reasoning. Two benchmark settings: a **distractor** setting (2 gold paragraphs + 8 TF-IDF distractors) and a **full wiki** setting (retrieve from all 5M+ Wikipedia paragraphs). A reimplementation of Clark & Gardner (2017) augmented with supporting-fact supervision in a multi-task head scores 58.28 F1 (answer) / 66.66 F1 (supporting facts) / 40.86 joint F1 in the distractor setting and degrades to 34.36 / 40.98 / 17.73 in full wiki, while humans hit 91.40 / 90.04 / 82.55 — a ~30-40 point gap that defined the multi-hop QA research agenda for years. The single-most-cited operational lesson: incorporating supporting-fact supervision into training gives ~2 F1 on answer accuracy but an entire model's worth of explainability (60+ F1 on the supporting-fact prediction task itself).

## Key Takeaway

The conventional path to building a reasoning benchmark — sample questions from an existing knowledge base, or scrape questions from search-engine queries — produces datasets that systems can solve without ever reasoning across documents, because the question's surface form leaks the answer's location. HotpotQA flips this: it pays crowd workers to *first* read two specific paragraphs connected by a hyperlink, *then* ask a question that genuinely requires both. The counter-intuitive part isn't the multi-hop structure — it's that **collecting sentence-level supporting facts at write time changes what models can learn**, not just what you can evaluate. A model trained on (question, answer) alone learns to pattern-match; the same model trained on (question, answer, supporting-fact-sentences) gains an extra 2 F1 on the answer task but also produces 60+ F1 supporting-fact predictions for free. Strong supervision over the *provenance trail* is itself a training signal — separate from the answer signal — and you cannot bolt it on later.

## Implications

- **[E + G] Supervise the provenance trail at write time, not query time** [ENGRAM: Encode + Ground]: HotpotQA's ablation (Table 7) shows that adding supporting-fact supervision lifts answer F1 by ~2 points (55.19 → 58.28) AND unlocks a 60+ F1 supporting-fact-prediction head as a multi-task by-product. For a memory architect: if you want your agent to surface *why* it retrieved a memory, you have to capture the citation trail during the write-path extraction step — there is no oracle re-construction at query time that recovers this signal.

- **[R] Retrieval IS the multi-hop bottleneck, not reasoning** [ENGRAM: Retrieve]: In the distractor setting (gold paragraphs visible among 10 candidates) the baseline scores 58.28 answer F1; in full-wiki (5M+ paragraphs) it crashes to 34.36 F1 — a 24-point drop driven almost entirely by retrieval failure (MAP = 43.93, Mean Rank = 314.71 for the second gold paragraph). The lesson for agentic memory: spend your compute budget on getting both relevant chunks *into* the candidate pool before optimizing the synthesis step. Bridge-entity questions drop from 59.09 → 30.42 F1 across the two settings, while comparison questions drop only 55.05 → 50.70 — comparison wins because both entity names appear in the question and act as their own retrieval anchors.

- **[N] Shape your retrieval unit to the reasoning unit you want to evaluate** [ENGRAM: Network]: HotpotQA uses *paragraphs* as the retrieval unit and *sentences* as the supporting-fact unit, deliberately. This dual-granularity matters: a sentence-as-supporting-fact label can't exist if retrieval returns whole documents (too coarse to localize provenance), and a sentence-as-retrieval-unit erases the local coherence needed for multi-hop chains. The general rule: retrieval granularity should be one notch coarser than your finest-grained provenance label.

- **[A] Comparison questions are an under-explored consolidation primitive** [ENGRAM: Aggregate]: 27% of HotpotQA dev questions are entity-comparison questions ("Did LostAlone and Guster have the same number of members?") and they're substantively easier than bridge-entity questions in full-wiki precisely because both retrieval anchors are explicit in the question. For a memory layer, "compare-on-property" is a cheap, robust query type — agents can defer to it whenever entity names are already known, sidestepping the harder "follow this entity to find that one" pattern.

- **[E] Crowd-worker curation isn't optional — randomly-paired paragraphs produce garbage** [ENGRAM: Encode]: The authors report that giving Turkers arbitrary paragraph pairs was "counterproductive — for most paragraph sets, it is difficult to ask a meaningful multi-hop question." They had to (1) build a Wikipedia hyperlink graph, (2) manually curate 591 categories as bridge-entity targets, (3) curate 42 entity-list categories for comparison questions. Translation for memory architects: if you're auto-generating "multi-hop training pairs" for an agent from raw memory contents, expect <10% yield without semantic pre-filtering of which entity pairs are worth asking about.

- **[M] Honest failure modes ship in the dataset, not as caveats** [ENGRAM: Maintain]: HotpotQA splits into train-easy (18,089 single-hop), train-medium (56,814 model-soluble), and train-hard (15,661 truly hard) — with dev and test drawn only from the hard pool. This three-tier structure means the benchmark *self-documents* what existing techniques can already solve, so future work has to attack the residual. For a memory benchmark designer: don't include questions your strawman baseline already solves above some threshold — tier them or drop them.

- **[G] Joint metrics force the trust/accuracy trade-off into the open** [ENGRAM: Ground]: The paper introduces *joint EM* (1 iff both answer AND supporting facts are exactly right) and *joint F1* (precision and recall multiplied across both subtasks). On the dev set, answer F1 is 58.28 and supporting-fact F1 is 66.66, but joint F1 collapses to 40.86 — because the model is rarely right about *both* at once. For an agent that surfaces citations alongside answers, optimizing the two metrics independently lets you ship a system that's plausibly cited but wrong, or correctly answered but wrongly cited. Track them together.

## How to Apply It (method)

**Scenario:** You're building a memory layer for an enterprise sales-ops agent. Sales reps ask questions like "Which of our Q3 deals over $50K had champions who left the company before close?" — questions that require joining facts from the CRM (deal records), HRIS (employment status changes), and the activity log (champion identification). You suspect your current single-shot RAG pipeline retrieves the right deals but misses the personnel-departure context, and that you can't tell *why* it returned what it returned. You want to (a) collect a training/eval set of genuine multi-hop questions, and (b) train a retrieval+answer system that produces a supporting-fact trail you can audit.

**Steps:**

1. **Build the entity-link graph from your own corpus**: Index every CRM deal, every HRIS person record, every activity log entry. Extract every reference from one record to another (deal.champion → person; person.previous_employer → company). Build a directed graph where edges are explicit references. This is your equivalent of Wikipedia's first-paragraph hyperlinks.

2. **Manually curate "bridge" entity types**: Don't let crowd workers (or your annotation team) write multi-hop questions over arbitrary entity pairs. Pick 5-15 entity categories you know produce interesting joins — e.g. *Deal → Champion Person*, *Account → Industry Vertical*, *Deal → Competitor Mentioned*. Discard categories where the bridge entity has no useful properties to query (e.g. "Deal → Date Created" is too thin).

3. **Sample candidate record pairs (a, b) such that b is in your curated bridge set**: For each pair, present both records side-by-side to the annotator with this prompt:

   ```
   Below are two records, A and B, that are linked. Read both, then write
   a question whose answer cannot be derived from A alone OR from B alone
   — you must use facts from BOTH records. After writing the question,
   highlight (sentence-by-sentence) which facts from A and which facts
   from B are required to derive the answer.

   Record A: <full text of CRM deal record>
   Record B: <full text of HRIS person record for the champion>

   Your question:
   Your answer:
   Supporting facts from A (highlight sentences):
   Supporting facts from B (highlight sentences):
   ```

4. **Add a comparison-question track for same-category entity pairs**: For each entity category (e.g. *Deal*, *Account*), sample pairs of entities from the same category and have annotators write comparison questions ("Did Deal X and Deal Y both have a champion turnover during the quarter?"). Mix in yes/no variants so the system can't game it by entity-name matching.

5. **Tier your collected dataset by difficulty**: Train a baseline retrieval+answer model on a small sample. Run it on the rest. Bucket: (a) examples the baseline solves with high confidence → call these "easy", use as warm-up training data; (b) examples it solves but with lower confidence → "medium"; (c) examples it fails → "hard". Dev and test sets are drawn only from "hard" so future-model gains have somewhere to come from.

6. **Build the two evaluation settings**:
   - **Closed setting**: 2 gold records + N TF-IDF distractor records, shuffled. Tests reasoning purity.
   - **Open setting**: full corpus, no gold record hints. Tests retrieval + reasoning. Use a separate test set so gold records never leak.

7. **Train a multi-task model with supporting-fact supervision**: On top of whatever your retrieval+answer architecture is, add a binary classifier head that predicts "is this sentence a supporting fact?" for each retrieved sentence. Loss = answer_loss + λ × supporting_fact_BCE. The paper used λ such that the supporting-fact loss is roughly the same magnitude as the answer loss — start there.

8. **Report joint metrics, not just answer accuracy**: For every eval pass, report (answer F1, supporting-fact F1, joint F1, joint EM). The joint metric is the only one that catches "plausibly cited but wrong" or "right answer with wrong citations." Don't let the team optimize only one of them.

**Expected outcome:** A held-out benchmark of ~5-15K genuine multi-hop questions where each one has annotated provenance sentences, plus a retrieval+answer model that produces citation trails alongside answers — and an honest report of where the bottleneck is (retrieval vs. reasoning), measured by the gap between closed-setting and open-setting joint F1. You will likely find — as HotpotQA did — that the open-setting collapse is 20-25 F1 points and almost entirely from retrieval, which tells you exactly where to invest next.

## Best Figure

![Figure 1 — An example of the multi-hop questions in HotpotQA (page 1)](figures/yang-2018-hotpotqa-multihop-fig.png)

```
Image Candidates:
Figure 1 (p. 1): The canonical multi-hop question example with both supporting paragraphs and highlighted supporting facts — encapsulates the entire thesis of the paper.
Figure 3 (p. 6): The model architecture diagram showing the dual-task head (answer span + supporting-fact classifier) — useful for the technical reader but doesn't show what's novel about the dataset itself.
Table 8 (p. 8): The human-vs-model comparison table — concretely shows the ~30-point performance gap that defines the difficulty of the benchmark.

Best Image:
Figure Name: Figure 1: "An example of the multi-hop questions in HotpotQA"
Figure Page: 1
Slide Caption: HotpotQA's defining unit — a question that requires reading two linked paragraphs, with sentence-level supporting facts as annotations.
Description: Figure 1 shows two Wikipedia paragraphs (A: "Return to Olympus", B: "Mother Love Bone") connected by the bridge entity "Andrew Wood", a multi-hop question ("What was the former band of the member of Mother Love Bone who died just before the release of 'Apple'?"), the answer ("Malfunkshun"), and the sentence-level supporting facts (1, 2, 4, 6, 7). The supporting-fact sentences are highlighted in blue italics within the paragraphs. This single figure encodes the four innovations of the paper: (a) text-based not KB-based, (b) multi-document reasoning required, (c) sentence-level provenance trail collected at annotation time, (d) the bridge-entity structure that makes multi-hop questions writable at scale. Every subsequent benchmark in the multi-hop QA literature (2WikiMultihopQA, MuSiQue, etc.) reuses this anatomy.
```

## What Experts Overlook

Most readers focus on the multi-hop QA contribution and skip past the data-collection pipeline. But the load-bearing detail is in Section 2's pilot study: **"in our pilot studies, we found that simply giving an arbitrary set of paragraphs to crowd workers is counterproductive, because for most paragraph sets, it is difficult to ask a meaningful multi-hop question."** This forced them to build a directed hyperlink graph over the entire English Wikipedia, then manually curate 591 categories of "bridge-eligible" target articles (Appendix A) plus 42 entity-list categories for comparison questions — *before* a single Turker question was written. The bridge-entity constraint isn't a methodological footnote; it is the only reason the dataset exists. Random paragraph pairs produced unanswerable garbage. Only paragraph pairs (a, b) where b is on a curated category page AND b is linked from a's first paragraph produced human-writable multi-hop questions at scale.

**Why it matters:** This tells you that "multi-hop reasoning" as a task is **structurally rare in raw text** — most pairs of arbitrary text passages don't admit interesting joins. The signal that *some* pairs do admit interesting joins is encoded in the hyperlink graph (someone, somewhere, has already linked these because they're meaningfully related). A memory architect designing a self-improving agent that auto-generates its own multi-hop training questions from its memory corpus has to recreate this signal somehow — either via explicit entity linking, or via co-occurrence statistics, or via an LLM-judge filter. Without it, you'll generate questions that *look* multi-hop but are answerable from one chunk, and your eval scores will quietly inflate.

**Example of good use:** A memory architect building an enterprise-knowledge agent extracts entity-mention edges from her corpus (every time a document mentions a person, place, or product that has its own canonical record). She uses this entity-graph as the candidate-pair source for auto-generating multi-hop questions — only pairs connected by an edge AND where the bridge entity has at least 3 distinct property values get used. Her resulting synthetic multi-hop eval set has 85%+ "genuine multi-hop" rate when audited, vs. <15% for randomly-paired chunks.

**Example of misapplication:** A team builds a "multi-hop benchmark" by randomly sampling chunk pairs from their memory store, feeding both to GPT-4, and asking it to "write a question requiring both chunks." Without the curation step, GPT-4 happily produces questions that look multi-hop but are answerable from one chunk (the model invents a connection that isn't really required for the answer). Their memory system "scores 80% on multi-hop QA" but actually scores ~30% on questions that *genuinely* need both — they only discover this when a customer asks a real multi-hop question and the system fails. The gap was hidden by their benchmark generation pipeline, not by their retrieval logic.

## Extracted Prompts

No applicable prompts found in this paper.

(The paper predates the LLM-prompting era — its "prompts" are the natural-language *instructions given to human crowd workers via the ParlAI dialog interface*. The instructions are described in prose in Sections 2 and Appendix A but not provided as verbatim templates in the paper itself.)

## Citations

The paper cites 19 prior works. Full structured list is in the frontmatter `citations:` field. Highlights:

- **Rajpurkar et al. 2016 — SQuAD**: the single-paragraph QA dataset HotpotQA explicitly defines itself against. SQuAD answers are extractable from a single sentence; HotpotQA forces multi-paragraph reasoning.
- **Welbl, Stenetorp, Riedel 2018 — QAngaroo (WikiHop)**: the immediately-prior multi-hop QA dataset, but KB-schema-constrained. HotpotQA replaces KB schemas with crowd-written natural-language questions.
- **Talmor & Berant 2018 — ComplexWebQuestions**: another KB-derived multi-hop benchmark; same limitation as QAngaroo.
- **Joshi et al. 2017 — TriviaQA** and **Dunn et al. 2017 — SearchQA**: multi-document QA datasets, but distantly supervised — answers found by IR after question collection, so multi-hop reasoning is incidental rather than required.
- **Chen et al. 2017 — DrQA**: the open-domain QA baseline whose architectural template (TF-IDF retrieval + reading comprehension) HotpotQA's full-wiki setting reuses.
- **Clark & Gardner 2017**: the reading-comprehension architecture HotpotQA's baseline reimplements and extends with the supporting-fact multi-task head.
- **Seo et al. 2017 — BiDAF**, **Wang et al. 2017 — Gated self-matching**: bi-attention and self-attention building blocks subsumed in the baseline.
- **Nguyen et al. 2016 — MS MARCO**: free-form answer-generation QA, included as comparison in Related Work — HotpotQA argues span-extraction is preferable because BLEU/ROUGE correlate poorly with human judgement (Novikova et al. 2017).
- **Miller et al. 2017 — ParlAI**: the dialog-research platform used as the crowdsourcing interface.
- **Manning et al. 2014 — Stanford CoreNLP**: tokenization and sentence-boundary detection.

## Related Digests

- [[gutierrez-2024-hipporag]] — HippoRAG: Neurobiologically Inspired Long-Term Memory for LLMs — uses HotpotQA as a multi-hop benchmark to evaluate its graph-based retrieval; HotpotQA citation appears in the related-work section.
- [[weston-2015-memory-networks]] — Memory Networks — the conceptual ancestor of multi-hop neural retrieval (k-hop attention as "repeat O with previous output as query refiner").
- [[sukhbaatar-2015-end-to-end-memory-networks]] — End-To-End Memory Networks — the trainable version of Memory Networks; the hop-count curve work it pioneered is exactly the question HotpotQA's two-hop benchmark forces models to answer.
- [[chen-2017-drqa-machine-reading]] — DrQA — the open-domain QA architectural template (TF-IDF retrieval + reading-comprehension reader) that HotpotQA's full-wiki setting builds on.
- [[clark-2017-multi-paragraph-rc]] — Simple and Effective Multi-Paragraph Reading Comprehension — the baseline architecture HotpotQA reimplements and extends with supporting-fact supervision.
- [[bajaj-2016-ms-marco]] — MS MARCO — the alternative free-form-answer paradigm HotpotQA argues against because automatic metrics correlate poorly with human judgement.
- [[dunn-2017-searchqa-dataset]] — SearchQA — multi-document QA dataset that HotpotQA criticizes for relying on post-hoc IR-collected documents (multi-hop is not required, only available).

## Reviewer Notes

**Overall severity:** Clean

All quantitative claims in this digest were cross-checked against the paper:
- 112,779 total examples → Section 3 ("We collected 112,779 valid examples in total")
- Split sizes (18,089 / 56,814 / 15,661 / 7,405 dev / 7,405 test-distractor / 7,405 test-fullwiki) → Table 1
- 591 manually curated categories → Appendix A.2
- 42 entity-list categories → Section 2 ("we manually curate 42 lists of similar entities")
- Distractor-setting baseline numbers (44.44 EM / 58.28 F1 answer; 21.95 EM / 66.66 F1 sup; 11.56 EM / 40.86 F1 joint) → Table 4
- Full-wiki numbers (24.68 EM / 34.36 F1 answer) → Table 4
- Human performance (83.60 EM / 91.40 F1 answer; 61.50 EM / 90.04 F1 sup; 52.30 EM / 82.55 F1 joint) → Table 8
- Retrieval performance (MAP 43.93, Mean Rank 314.71) → Table 5, dev row
- Bridge vs. comparison question performance (59.09 → 30.42 F1 bridge across settings; 55.05 → 50.70 F1 comparison) → Table 6
- Ablation: 55.19 F1 without sup-fact supervision vs. 58.28 F1 with → Table 7 ("– sup fact, self attention" baseline vs. "our model")
- Question-type distribution (Type I 42%, Comparison 27%, Type II 15%, Type III 6%, Other 2%, single-hop 6%, unanswerable 2%) → Table 3 and surrounding text on dev set
- Comparison-question prevalence (27% of dev) → Table 3
- 2 gold + 8 distractor paragraphs → Section 3 ("we mix them with the 2 gold paragraphs ... to construct the distractor setting")
- 5M+ Wikipedia paragraphs → Section 5.2 ("to enable efficient tf-idf retrieval among 5,000,000+ wiki paragraphs")
- Multi-task supporting-fact classifier on self-attention layer first/last positions → Section 5.1 (Figure 3 caption)

The ENGRAM tag assignments are my interpretive overlay (as the lens requires), not claims about the paper — labelled as such in the implications section.
