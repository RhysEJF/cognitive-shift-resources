---
corpus: agentic-memory
kind: paper-digest
slug: li-2023-loogle
title: "LooGLE: Can Long-Context Language Models Understand Long Contexts?"
authors:
  - "Jiaqi Li"
  - "Mengmeng Wang"
  - "Zilong Zheng"
  - "Muhan Zhang"
year: 2023
publication_date: "2023-11"
venue: "arXiv preprint (BIGAI / Peking University) — ACL 2024 Findings"
source_url: "https://arxiv.org/abs/2311.04939"
doi: null
arxiv_id: "2311.04939"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "LooGLE shows that 'long context' is two different problems — short-dependency tasks (single-paragraph lookup) and long-dependency tasks (synthesise evidence dispersed across 5,000+ words), and every modern LLM fails the second: even GPT-4-32k scores under 40% GPT-4-judge accuracy on long-dependency QA, retrieval-based methods (LlamaIndex) actively hurt long-dependency performance because retrieved snippets lose inter-segment context, CoT gives marginal gains, and extending context window past 8K barely helps summarisation — meaning the bottleneck for long-context understanding is comprehension/reasoning across distant evidence, not memory of distant tokens."
topics:
  - long-context-llm
  - benchmark
  - long-dependency
  - short-dependency
  - llm-evaluation
  - retrieval-vs-context
  - cot-evaluation
  - timeline-reordering
  - multi-document-qa
  - data-leakage
  - post-2022-documents
  - true-long-context-understanding
  - llm-as-judge
tags:
  - paper
  - long-context
  - benchmark
  - long-dependency-evaluation
  - bigai
  - peking-university
  - llm-evaluation
entities:
  - li-jiaqi
  - wang-mengmeng
  - zheng-zilong
  - zhang-muhan
related_digests:
  - liu-2023-lost-in-the-middle
  - maharana-2024-locomo
  - wu-2024-longmemeval
  - wu-2026-lme-v2
  - tavakoli-2026-beam-light
citations:
  - title: "ZeroSCROLLS: A zero-shot benchmark for long text understanding"
    authors: ["Uri Shaham", "Maor Ivgi", "Avia Efrat", "et al."]
    year: 2023
    venue: "EMNLP Findings"
    arxiv_id: "2305.14196"
  - title: "L-Eval: Instituting standardized evaluation for long context language models"
    authors: ["Chenxin An", "Shansan Gong", "Ming Zhong", "et al."]
    year: 2023
    venue: "ACL"
    arxiv_id: "2307.11088"
  - title: "LongBench: A bilingual, multitask benchmark for long context understanding"
    authors: ["Yushi Bai", "Xin Lv", "Jiajie Zhang", "et al."]
    year: 2023
    venue: "preprint"
    arxiv_id: "2308.14508"
  - title: "Lost in the Middle: How language models use long contexts"
    authors: ["Nelson F. Liu", "Kevin Lin", "John Hewitt", "et al."]
    year: 2023
    venue: "TACL"
    arxiv_id: "2307.03172"
  - title: "FlashAttention: Fast and memory-efficient exact attention with IO-awareness"
    authors: ["Tri Dao", "Daniel Y. Fu", "Stefano Ermon", "et al."]
    year: 2022
    venue: "NeurIPS"
    arxiv_id: "2205.14135"
  - title: "Extending context window of LLMs via positional interpolation"
    authors: ["Shouyuan Chen", "Sherman Wong", "Liangjian Chen", "Yuandong Tian"]
    year: 2023
    venue: "preprint"
    arxiv_id: "2306.15595"
  - title: "Focused Transformer: Contrastive training for context scaling"
    authors: ["Szymon Tworkowski", "Konrad Staniszewski", "Mikoł aj Pacek", "et al."]
    year: 2023
    venue: "NeurIPS"
    arxiv_id: "2307.03170"
  - title: "RWKV: Reinventing RNNs for the transformer era"
    authors: ["Bo Peng", "Eric Alcaide", "Quentin Anthony", "et al."]
    year: 2023
    venue: "EMNLP Findings"
    arxiv_id: "2305.13048"
  - title: "Llama 2: Open foundation and fine-tuned chat models"
    authors: ["Hugo Touvron", "Louis Martin", "Kevin Stone", "et al."]
    year: 2023
    venue: "preprint"
    arxiv_id: "2307.09288"
  - title: "LlamaIndex"
    authors: ["Jerry Liu"]
    year: 2022
    venue: "GitHub"
    url: "https://github.com/jerryjliu/llama_index"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "The LooGLE benchmark for long context understanding"
  page: 1
  image_path: "figures/li-2023-loogle-fig.png"
---

# LooGLE: Can Long-Context Language Models Understand Long Contexts?

**Authors:** Jiaqi Li, Mengmeng Wang, Zilong Zheng, Muhan Zhang
**Published:** 2023-11 · [Source](https://arxiv.org/abs/2311.04939)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Li et al. (BIGAI / Peking University) introduce LooGLE, a long-context benchmark for LLMs with three deliberate design choices that distinguish it from prior work (ZeroSCROLLS, L-Eval, LongBench): (1) all 776 documents are post-2022 to minimise pre-training data leakage; (2) documents average 19,367 words (well over modern long-context window sizes, with many exceeding 100K words); and (3) the benchmark separates **short-dependency tasks** (single-paragraph lookup) from **long-dependency tasks** (5,000+ word evidence spans), with 1,101 hand-annotated long-dependency QA pairs across four subtypes: Multiple-source retrieval, Timeline reorder, Computation, Comprehension+reasoning. Annotation used a two-annotator-blind questioner/answerer protocol with 81.88% inter-annotator agreement. Eight LLMs evaluated — commercial (GPT-4-32k, GPT-4-8k, GPT-3.5-turbo-16k), open-source (LLaMA2-7B-32K, ChatGLM2-6B-32k, LongLLaMa-3B-256k, RWKV-4-14B-pile), retrieval (LlamaIndex). Headline findings: commercial models dominate (GPT-4-32k wins 6 of 7 task categories), but **even GPT-4-32k scores under 40% GPT-4-judge accuracy on long-dependency QA** (43.60 information retrieval / 64.43 timeline reorder / 37.36 computation / 61.26 comprehension+reasoning). LlamaIndex retrieval *hurts* on long-dependency tasks (GPT-4-32k drops from 54.09% to 28.25% GPT-4-judge accuracy when wrapped in LlamaIndex). Extending input length from 8K → 32K barely improves summarisation but substantially improves long-dependency QA. CoT prompting gives only marginal gains. Open-source 32K models (LLaMA2-7B-32K, RWKV-4-14B-pile) perform near zero on long-dependency tasks. Conclusion: long context window ≠ long context understanding.

## Key Takeaway

The architectural lesson is that **"long context" is two different problems collapsed under one label, and the second one is unsolved**. Short-dependency tasks (locate a fact in a paragraph) are largely solved — commercial LLMs at 16K–32K hit 60–87% accuracy. Long-dependency tasks (synthesise evidence dispersed across 5,000+ word spans, reorder timelines, compute from numbers scattered across the text) are *not* solved — the best model (GPT-4-32k) scores under 40% on multiple-information-retrieval QA and 37% on computation. And retrieval-augmentation — the default "long context" workaround — *actively hurts* on long-dependency tasks, because the retrieved snippets lose the inter-segment context that the question requires. For memory-architect work the implication is sharp: a memory system that retrieves top-k chunks will succeed at short-dependency questions and fail at long-dependency ones, and adding more context to the responder won't fix it because the model itself can't synthesise across distant evidence reliably. (ENGRAM: this is a **R** (Retrieve) and **A** (Aggregate) story — retrieval-only architectures saturate at short-dependency tasks; long-dependency tasks need aggregation/synthesis primitives the retriever doesn't provide. Also **G** (Ground) because long-dependency-task failure modes include hallucination of "the text does not provide information" responses when context is truncated.)

## Implications

- **Bucket your memory-system evaluation by dependency length** (ENGRAM: **R**, **A**). The single most useful diagnostic is to split your QA bench into short-dependency (answer in one paragraph) and long-dependency (answer requires evidence spanning 5,000+ words). The LooGLE 81.88% inter-annotator-agreement protocol is reusable: assign questioner + answerer blind to each other, require minimum 5,000-word evidence span, enforce diverse question types per document (max 4 of the same subtype). If your memory architecture's short-dependency win is 20+ points but long-dependency is < 5 points, you have a retrieval-only system — the synthesis layer is missing.

- **Retrieval-augmentation is a short-dependency win and a long-dependency anti-pattern** (ENGRAM: **R**, **A**). Table 6 in the paper shows GPT-4-32k drops from 54.09 (no retrieval) to 28.25 (LlamaIndex retrieval) on long-dependency QA. The mechanism: retrieved snippets lack inter-segment context, so the responder hallucinates or refuses ("the text does not provide information"). Implication for Flow OS: do NOT default to retrieval for every query — gate by question type. If the question requires synthesis across the conversation, pass more context with structure (e.g., section summaries) rather than top-k snippets.

- **Use post-2022-only documents to test memory architectures** (ENGRAM: **E**, **G**). The LooGLE design choice of post-2022 documents prevents data leakage from pre-training corpora. For a memory system you're benchmarking against your own data, the equivalent is: never use documents that match the LLM's training cut-off date. Use very recent documents (last 6 months) or synthetic-from-fresh-seed material.

- **Timeline reordering is the cleanest single test of temporal-memory architecture** (ENGRAM: **A**). Of LooGLE's four long-dependency tasks, timeline reorder has the most-spread distribution of model scores and the clearest interpretation: "given events scattered across the document, put them in chronological order". A memory system claiming temporal reasoning should publish its score on this subtask. GPT-4-32k hits 64.43 here — surprisingly high — while LlamaIndex+GPT-4-32k drops to 47.83. The reason GPT-4 does well: events have explicit dates in the prose, so it's effectively a high-recall extract-then-sort task. A memory system using temporal-KG primitives (like Zep) should be competitive or better.

- **Computation across distant evidence is the bluntest test** (ENGRAM: **A**, **R**). The Computation subtask asks the model to do small arithmetic on numbers extracted from widely-dispersed sentences — "how many inhabitants increased from end-of-19th-century to 1970?". Best model: GPT-4-32k at 37.36 GPT-4-judge accuracy. This is the cleanest single metric for "can the system find scattered numbers AND combine them correctly?". If your memory architecture pulls scattered facts but can't compose them, this is where the failure shows.

- **Extending context past 8K is mostly wasted on summarisation, but valuable on long-dependency QA** (ENGRAM: **R**). Table 5: GPT-4-32k summarisation accuracy is flat across 8K → 16K → 24K → 32K (~83 GPT-4-judge). But long-dependency QA climbs from 38.34 (8K) → 47.55 (16K) → 54.65 (32K). The asymmetry: summarisation has the intro/conclusion which already covers most of the signal, so more middle adds noise; QA needs the middle. For a memory system, this suggests *task-conditioned* context-length policies — pull more for synthesis questions, pull less for summary-style requests.

- **Open-source 32K models are not a substitute for commercial 32K models on long-dependency tasks** (ENGRAM: **R**). LLaMA2-7B-32K scores 3.01–6.85 on long-dependency QA subtasks; RWKV-4-14B-pile (8K) scores 4.40–7.13; ChatGLM2-6B-32k scores 5.43–14.17. These are near-zero in practical terms. The 32K context window is real but the reasoning over that context isn't. For a self-hosted Flow OS deployment, "we have a 32K open-source model" is not equivalent to "we have a long-context system" — you'll need to compose with a stronger reasoner at the top of the stack.

- **GPT-4-as-judge is the single most-reliable LLM evaluation metric and BERTScore is misleading** (ENGRAM: **G**). LooGLE shows that BERTScore stays high (70–87) for nearly every model on nearly every task — including LLaMA2-7B-32K's 50.28 on long-dependency QA where GPT-4-judge says 4.18%. BERTScore is measuring fluency, not correctness. Use GPT-4-as-judge as the primary metric for any memory-system QA eval, and consider human evaluation on a subset for calibration.

## How to Apply It (method)

**Scenario:** You're evaluating Flow OS's memory architecture and want to know whether the gains you're seeing are real (work on hard long-dependency questions) or shallow (only short-dependency lookup). You want a robust benchmark methodology that doesn't overstate gains.

**Steps:**

1. **Bucket your benchmark into short- and long-dependency questions before running anything**. For each test question, identify the supporting evidence in the document/conversation. If all evidence is within a single 800-word window, it's short-dependency. If evidence spans ≥ 5,000 words (or equivalent — multiple sessions, multiple sections), it's long-dependency. Report metrics separately for each bucket. Almost every public benchmark conflates them; your numbers will be more informative than the field's.

2. **Use the LooGLE annotation protocol for new test data**:
   - Assign two annotators per document, blind to each other's identity
   - Annotator 1 (questioner) writes 5–10 questions, provides answers, marks evidence spans (≥ 5,000 words for long-dependency)
   - Annotator 2 (answerer) reads the document and the questions only — produces independent answers, flags ambiguous questions
   - Annotator 1 reconciles, revises questions, unifies answers
   - Expect ~18% drop-rate (LooGLE saw 206 of 1,137 first-pass questions fail)

3. **Include all four LooGLE long-dependency subtypes in your evaluation**:
   - Multiple information retrieval (~35% of long-dep QA)
   - Timeline reorder (~20%)
   - Computation (~9%)
   - Comprehension and reasoning (~37%)
   This distribution is the empirical-relevance prior from a year of LooGLE annotation; matching it gives you generalisability across question types.

4. **Use GPT-4-as-judge as primary metric** with this prompt structure (LooGLE's Appendix D):
   ```
   Given a question, the ground-truth answer, and a model's predicted answer, judge whether the predicted answer is semantically equivalent to the ground-truth answer. Respond with 'yes' or 'no'.

   Question: {q}
   Ground-truth: {a_gold}
   Model answer: {a_pred}

   Equivalent?:
   ```
   Compute accuracy as fraction of "yes" responses. Calibrate against human evaluation on a sample.

5. **Sweep input length on each subtype separately**. For each task type, try the question with 4K, 8K, 16K, 32K of context. Plot accuracy-vs-length curves. The shape will tell you which tasks are "more context helps" and which are "synthesis bottleneck — more context is wasted". Use this to set per-task context-length budgets in production.

6. **Always run an ablation against the retrieval baseline (LlamaIndex or your QMD)**. For long-dependency tasks specifically, expect retrieval to *hurt*. If your memory architecture beats both no-retrieval and naive-retrieval baselines on long-dependency QA, you have a real synthesis layer. If you only beat no-retrieval, you have a clever retriever — useful but limited.

7. **Document data-leakage hygiene**. State explicitly which documents your benchmark uses and confirm they post-date the LLM training cut-off. Otherwise your numbers will not reproduce on newer models.

8. **Compare against the LooGLE leaderboard numbers as priors**. GPT-4-32k at 43.60 on multi-source retrieval, 64.43 on timeline reorder, 37.36 on computation, 61.26 on comprehension+reasoning. If your memory-augmented system can't beat these on the LooGLE dataset itself, your architecture is not yet adding value to commercial long-context models on real long-dependency tasks.

**Expected outcome:** A benchmark report that distinguishes which of your memory-architecture wins are real synthesis improvements vs. retrieval-recall improvements. For most teams the result will be sobering — long-dependency QA gains are small, and a chunk of "memory architecture" investment is really delivering "better retrieval" wins on short-dependency questions. Knowing this directs effort to the right layer.

## Best Figure

![Figure 1 — The LooGLE benchmark for long context understanding (page 1)](figures/li-2023-loogle-fig.png)

Image Candidates:

- **Figure 1 (p. 1):** Overview infographic of LooGLE — shows the three data sources (arXiv, Wikipedia, scripts), the two task families (short-dependency + long-dependency with four subtypes), and the average word counts at a glance. This is the single best diagram for understanding the benchmark structure.
- **Figure 3 (p. 7):** Overall performance radar chart of all 8 models across the 7 tasks. Visually compelling story of "commercial wins, open-source collapses on long-dependency".
- **Table 4 (p. 7):** Performance of long-dependency tasks broken down by model and metric. Best for the headline numbers (GPT-4 scores).
- **Table 6 (p. 8):** LlamaIndex vs. raw long-context. The single most useful empirical artifact — shows retrieval *hurts* on long-dependency QA.

**Best Image — Figure 1: The LooGLE benchmark for long context understanding** (page 1). The diagram visually communicates the benchmark's design philosophy in one image: documents are bucketed into arXiv (516 papers, summarization task), Wikipedia (105 articles, both short and long QA), and Movie/TV scripts (155, cloze and long QA). The long-dependency QA branch is sub-bucketed into the four subtypes (Multi-source retrieval 34.51%, Timeline reorder 19.53%, Calculation 9.08%, Comprehension+reasoning 36.88%). The 19,367-average-word size is annotated. This is the single image that anchors the rest of the paper — once you see it, the asymmetry "short-dep solved, long-dep unsolved" becomes the natural reading frame.

## What Experts Overlook

The most overlooked operational detail is that **LooGLE's retrieval-baseline negative result is task-conditional**: LlamaIndex *helps* on short-dependency QA but *hurts* on long-dependency QA. From Table 6 and Table 4: on short-dependency, LlamaIndex achieves GPT-4 score 59.61 — competitive with GPT-3.5-turbo-16k (66.82). On long-dependency, LlamaIndex with default config drops to 33.16 vs. raw GPT-4-32k's 54.09. This means **a single global "should we use retrieval?" architecture decision is wrong**; you need a per-query-type routing decision.

**Why it matters:** Most production RAG systems are built on a single policy — every query goes through the retriever. LooGLE shows this is a self-imposed accuracy ceiling on the long-dependency portion of your traffic. A memory system that wants to handle both query types well needs either:

- A query classifier (short-dep → retrieve; long-dep → pass-through with structured context), OR
- A two-stage architecture: retrieval generates a candidate context, then a synthesis step composes the answer across the retrieved chunks (multi-hop or chain-of-density style)

**Example of good use:** Flow OS routes incoming questions through a small classifier ("is this answer in one paragraph, or does it span multiple sessions?"). For the latter, it pulls section-level summaries + the relevant raw transcripts rather than top-k chunks. Long-dependency accuracy beats the LlamaIndex baseline because the model has structured context, not snippets.

**Example of misapplication:** A team adds RAG to their long-context system, sees aggregate accuracy *drop*, blames their embedding model, swaps models, sees no change. They never bucketed the eval by dependency type — so they don't know that RAG helped short-dep and hurt long-dep, and the average is washing out the structure.

## Extracted Prompts

**Prompt explanation:** Long-dependency QA annotation guidance (LooGLE annotation protocol, Section 3.2.2). Used to instruct human annotators producing the 1,101 long-dependency QA pairs. The "≥ 5,000 word minimum evidence span" is the load-bearing definition — it operationalises "long-dependency" as something measurable.

```
For each document, generate 5 to 10 question-answer pairs such that:

- Each question must exhibit a "long dependency": the evidence supporting the answer should have a wide span across the document. The recommended dependency length (distance between earliest and latest evidence) is a minimum of 5,000 words.
- Diverse problem types: no more than 4 questions of the same type per document.
- Clear and precise questions: formulation must adhere to clarity, conciseness, no ambiguity.
- Deterministic and objective answers: rigorously checked to be deterministic and objective; no open-ended questions.

For each Q-A pair, also pinpoint the specific evidentiary passages within the document that substantiate the answer.
```

**Prompt explanation:** GPT-4-as-judge for QA evaluation. The metric LooGLE found most reliable (versus BLEU/ROUGE/BERTScore which were misleading). Use this directly when scoring your own memory-system QA outputs.

```
Given a question, the ground-truth answer, and a model's predicted answer, judge whether the predicted answer is semantically equivalent to the ground-truth answer. Respond with 'yes' or 'no'.

Question: {q}
Ground-truth: {a_gold}
Model answer: {a_pred}

Equivalent?:
```

**Prompt explanation:** Short-dependency QA generation prompt (using GPT-3.5-turbo-16k on Wikipedia segments). This is the *automated* generation step LooGLE used for short-dependency QA — useful as a template for bootstrapping a memory-system eval set from your own data.

```
Read the following passage and generate a list of question-answer pairs, with each pair containing:
- A clear, concise question that can be answered from the passage
- The answer
- The exact supporting evidence (verbatim sentence) from the passage

Aim for diverse question types: factual lookup, attribute extraction, relationship identification.

Passage: {passage}
```

## Citations

Cites ~60 works spanning long-context architectures (Longformer, FlashAttention, Position Interpolation, Focused Transformer, RWKV), benchmarks (ZeroSCROLLS, L-Eval, LongBench, LongEval), evaluation methods (BLEU, ROUGE, BERTScore, GPT-4-as-judge), and foundation LLMs (GPT-4, Llama-2, ChatGLM2). Most relevant for the memory-architect lens: Liu 2023 (Lost in the Middle — already in wiki), Shaham 2023 (ZeroSCROLLS), Bai 2023 (LongBench), Chen 2023 (Position Interpolation).

## Related Digests

- [[liu-2023-lost-in-the-middle]] — Lost in the Middle: How LMs Use Long Contexts (the U-shaped attention curve LooGLE cites as motivation for head+tail truncation)
- [[maharana-2024-locomo]] — LoCoMo: Very Long-Term Conversational Memory benchmark (sibling benchmark — LooGLE for documents, LoCoMo for dialogues)
- [[wu-2024-longmemeval]] — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory (the conversational-memory equivalent of LooGLE's document-memory evaluation)
- [[wu-2026-lme-v2]] — LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues (the next-generation extension that adds 25M-token web-agent haystacks)
- [[tavakoli-2026-beam-light]] — Beyond a Million Tokens: Benchmarking Long-Term Memory in LLMs (extends LooGLE's findings to 1M–10M token context regimes)

## Reviewer Notes

**Severity: Clean.**

Cross-checked against the paper:

- 776 documents averaging 19,367 words; 6,448 test instances; 1,101 long-dependency QA pairs — all match Table 2 and §3.1.
- The four long-dependency subtype proportions (34.51% / 19.53% / 9.08% / 36.88%) match Figure 2.
- Inter-annotator agreement 81.88% is from §3.2.2.
- GPT-4-32k headline numbers (43.60 / 64.43 / 37.36 / 61.26) match Table 7 exactly.
- LlamaIndex+GPT-4-32k 28.25 vs raw 54.09 is from Table 4 vs Table 6.
- Summarization length insensitivity (Table 5: 82.84 → 83.15 → 82.82 → 82.75 across 32K→24K→16K→8K) is accurate.
- Long-dep QA length sensitivity (Table 5: 54.65 → 50.61 → 47.55 → 38.34) is accurate.
- LooGLE annotation protocol (questioner/answerer blind, 5,000-word minimum dependency, max 4 of same type per doc) is from §3.2.2.

One paraphrase: the digest claims open-source 32K models "perform near zero" on long-dependency QA. The actual numbers are 3.01–7.13 GPT-4-judge accuracy across LLaMA2-7B-32K, RWKV-4-14B-pile, and similar. "Near zero" is a fair operational characterization — these are below the level of useful production use.

No invented facts, no misattributed citations.
