---
corpus: agentic-memory
kind: paper-digest
slug: laitenberger-2025-dos-rag
title: "Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models"
authors:
  - "Laitenberger, Alex"
  - "Manning, Christopher D."
  - "Liu, Nelson F."
year: 2025
publication_date: "2025-06"
venue: "arXiv preprint (v2: Jan 2026)"
source_url: "https://arxiv.org/abs/2506.03989"
doi: null
arxiv_id: "2506.03989"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "DOS RAG — vanilla retrieve-then-read, but with retrieved passages reordered back into their original document order before being handed to a long-context LM — consistently matches or beats two complex multi-stage pipelines (RAPTOR's hierarchical-summary tree and ReadAgent's gist-then-look-up agent) by 2-8 accuracy points on three long-context QA benchmarks (∞Bench, QuALITY, NarrativeQA) once the retrieval budget exceeds ~5K tokens, suggesting that modern long-context readers (GPT-4o / 4o-mini) have erased most of the motivation for the abstractive preprocessing those pipelines were designed for."
topics:
  - retrieval-augmented-generation
  - long-context-language-models
  - rag-baselines
  - question-answering
  - dos-rag
tags:
  - paper
  - rag
  - long-context
  - benchmark
  - stanford
  - simplicity-wins
entities:
  - laitenberger-alex
  - manning-christopher
  - liu-nelson
related_digests:
  - lee-2024-readagent-gist-memory
  - sarthi-2024-raptor
  - lewis-2020-rag-knowledge-nlp
  - liu-2023-lost-in-the-middle
citations:
  - title: "Walking down the memory maze: Beyond context limit through interactive reading"
    authors: ["Chen, Howard", "Pasunuru, Ramakanth", "Weston, Jason", "Celikyilmaz, Asli"]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2310.05029"
    arxiv_id: "2310.05029"
  - title: "UNIFIEDQA: Crossing format boundaries with a single QA system"
    authors: ["Khashabi, Daniel", "Min, Sewon", "Khot, Tushar", "Sabharwal, Ashish", "Tafjord, Oyvind", "Clark, Peter", "Hajishirzi, Hannaneh"]
    year: 2020
    doi: null
    url: "https://aclanthology.org/2020.findings-emnlp.171/"
    arxiv_id: null
  - title: "The NarrativeQA reading comprehension challenge"
    authors: ["Kočiský, Tomáš", "Schwarz, Jonathan", "Blunsom, Phil", "Dyer, Chris", "Hermann, Karl Moritz", "Melis, Gábor", "Grefenstette, Edward"]
    year: 2018
    doi: null
    url: "https://aclanthology.org/Q18-1023/"
    arxiv_id: null
  - title: "A human-inspired reading agent with gist memory of very long contexts (ReadAgent)"
    authors: ["Lee, Kuang-Huei", "Chen, Xinyun", "Furuta, Hiroki", "Canny, John", "Fischer, Ian"]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.09727"
    arxiv_id: "2402.09727"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    authors: ["Lewis, Patrick", "Perez, Ethan", "Piktus, Aleksandra", "Petroni, Fabio", "Karpukhin, Vladimir", "Goyal, Naman", "Küttler, Heinrich", "Lewis, Mike", "Yih, Wen-tau", "Rocktäschel, Tim", "Riedel, Sebastian", "Kiela, Douwe"]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2005.11401"
    arxiv_id: "2005.11401"
  - title: "Retrieval augmented generation or long-context LLMs? A comprehensive study and hybrid approach"
    authors: ["Li, Zhuowan", "Li, Cheng", "Zhang, Mingyang", "Mei, Qiaozhu", "Bendersky, Michael"]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2407.16833"
    arxiv_id: "2407.16833"
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Liu, Nelson F.", "Lin, Kevin", "Hewitt, John", "Paranjape, Ashwin", "Bevilacqua, Michele", "Petroni, Fabio", "Liang, Percy"]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2307.03172"
    arxiv_id: "2307.03172"
  - title: "Embedding and clustering your data can improve contrastive pretraining (Arctic-Embed)"
    authors: ["Merrick, Luke"]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2407.18887"
    arxiv_id: "2407.18887"
  - title: "QuALITY: Question answering with long input texts, yes!"
    authors: ["Pang, Richard Yuanzhe", "Parrish, Alicia", "Joshi, Nitish", "Nangia, Nikita", "Phang, Jason", "Chen, Angelica", "Padmakumar, Vishakh", "Ma, Johnny", "Thompson, Jana", "He, He", "Bowman, Samuel R."]
    year: 2022
    doi: null
    url: "https://aclanthology.org/2022.naacl-main.391/"
    arxiv_id: null
  - title: "RAPTOR: Recursive abstractive processing for tree-organized retrieval"
    authors: ["Sarthi, Parth", "Abdullah, Salman", "Tuli, Aditi", "Khanna, Shubh", "Goldie, Anna", "Manning, Christopher D."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2401.18059"
    arxiv_id: "2401.18059"
  - title: "PEARL: Prompting large language models to plan and execute actions over long documents"
    authors: ["Sun, Simeng", "Liu, Yang", "Wang, Shuohang", "Iter, Dan", "Zhu, Chenguang", "Iyyer, Mohit"]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2305.14564"
    arxiv_id: "2305.14564"
  - title: "Retrieval meets long context large language models"
    authors: ["Xu, Peng", "Ping, Wei", "Wu, Xianchao", "McAfee, Lawrence", "Zhu, Chen", "Liu, Zihan", "Subramanian, Sandeep", "Bakhturina, Evelina", "Shoeybi, Mohammad", "Catanzaro, Bryan"]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2310.03025"
    arxiv_id: "2310.03025"
  - title: "In defense of RAG in the era of long-context language models"
    authors: ["Yu, Tan", "Xu, Anbang", "Akkiraju, Rama"]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2409.01666"
    arxiv_id: "2409.01666"
  - title: "∞Bench: Extending long context evaluation beyond 100K tokens"
    authors: ["Zhang, Xinrong", "Chen, Yingfa", "Hu, Shengding", "Xu, Zihang", "Chen, Junhao", "Hao, Moo", "Han, Xu", "Thai, Zhen", "Wang, Shuo", "Liu, Zhiyuan", "Sun, Maosong"]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.13718"
    arxiv_id: "2402.13718"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "∞Bench En.MC performance of various multi-stage RAG systems and long-context baselines"
  page: 1
  image_path: "figures/laitenberger-2025-dos-rag-fig.png"
---

# Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models

**Authors:** Alex Laitenberger, Christopher D. Manning, Nelson F. Liu (Stanford University)
**Published:** 2025-06 (v2: 2026-01) · [Source](https://arxiv.org/abs/2506.03989)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

A three-author Stanford NLP paper (Laitenberger, Manning, Liu) asks: now that GPT-4-class models can swallow tens of thousands of tokens in one prompt, are the increasingly clever multi-stage RAG pipelines (hierarchical-summary trees, gist-and-look-up agents) still worth the complexity? They run a controlled comparison on three long-context QA benchmarks — ∞Bench En.MC (229 multiple-choice questions over 184K-token docs), QuALITY (2,086 MC questions over 2K-8K-token passages), and NarrativeQA (10,557 short-answer questions over 57K-token average stories) — pitting two recent multi-stage methods (RAPTOR's recursive cluster-and-summarise tree from Sarthi et al. 2024 and ReadAgent's pagination-gisting-lookup loop from Lee et al. 2024) against three baselines: Vanilla RAG (retrieve top-k by cosine sim, concatenate in similarity order), a full-document baseline (just paste the whole doc into the model — QuALITY only), and DOS RAG. DOS ("Document's Original Structure") RAG is the punchline: it is exactly Vanilla RAG with one extra line — after retrieval, sort the surviving passages back into their original document order. That single change, paired with GPT-4o or GPT-4o-mini as the reader and Snowflake Arctic-embed-m 1.5 as the retriever, beats both multi-stage baselines on every benchmark once the retrieval budget exceeds ~5K tokens, by margins of 2-8 accuracy points (∞Bench), 2-7 points (QuALITY), and 3-4 F1 points (NarrativeQA). ReadAgent, despite spending ~86K tokens per query on ∞Bench, underperforms DOS RAG at 20K. The authors argue that DOS RAG should become the default baseline for future RAG papers, and that any pipeline introducing extra LM-based preprocessing stages must justify the cost against this stronger floor.

## Key Takeaway

The complex multi-stage RAG pipelines of 2023-24 — RAPTOR's hierarchical-summary tree and ReadAgent's gist-then-look-up agent — were designed around the limitations of earlier reader LMs that could only fit ~4K tokens; once you swap in a long-context model like GPT-4o and give it the retrieved passages **in their original document order** rather than sorted by similarity, that one fix (and only that fix) closes or reverses the gap, suggesting much of the field's recent pipeline complexity is solving a reader-LM problem that no longer exists. The clean ablation that makes the case: Vanilla RAG and DOS RAG share the exact same retriever, embedding model, and top-k passages — the only difference is whether the retrieved passages are sorted by similarity score (Vanilla) or by their original document position (DOS) — and DOS RAG wins by 4-6 accuracy points across ∞Bench and QuALITY at retrieval budgets ≥10K tokens. The mechanism is concrete and testable: retrieve more (recall over precision) within the LM's effective context, preserve narrative continuity by document-order reordering, never replace original passages with LM-generated summaries.

## Implications

- **For RAG practitioners building production systems**: if you are already running Vanilla RAG with a modern long-context reader, adding a single one-line passage-reorder step (track each retrieved passage's original position, sort ascending before concatenating) is plausibly the highest-ROI improvement available — the paper measures +4-6 accuracy points on QA benchmarks for that change alone, with zero additional API calls or latency. Conversely, if you are paying for RAPTOR-style preprocessing (recursive LM-summarised cluster trees) or ReadAgent-style multi-step gist-then-lookup, the paper suggests you should re-benchmark against DOS RAG at matched token budgets before continuing to invest in the pipeline complexity — the authors estimate ReadAgent uses ~86K tokens per ∞Bench query versus DOS RAG's ~30K for higher accuracy.
- **For benchmark authors and reviewers**: the paper makes an explicit methodological recommendation that RAG papers should benchmark new methods against DOS RAG under matched token budgets, not against Vanilla RAG alone. The argument is that "Vanilla RAG" as historically defined understates the strength of simple retrieve-then-read because it shuffles passages by similarity rank, and the same retrieved content presented in document order is a meaningfully different (and stronger) condition.
- **For researchers studying multi-stage agentic RAG**: the result narrows where multi-stage pipelines need to show their worth. The authors are careful to scope their findings — multi-doc QA, open-ended generation, domain-specialist tasks, and non-GPT-4o readers are explicitly out of scope. So the claim is not "multi-stage RAG is dead" but "multi-stage RAG cannot justify itself on single-document long-context QA with modern long-context readers under matched token budgets" — a much narrower claim, but one that invalidates a meaningful slice of recent SOTA reporting.
- **For the "long-context kills RAG" debate**: the paper takes a deliberately middle position. It does not claim long-context LMs make retrieval obsolete (the full-document baseline only wins on QuALITY, where all docs fit in context). It claims retrieval and long-context are complementary, and that the right way to combine them is the simplest possible way (retrieve broadly, preserve order, hand to a strong reader). This is closer to Yu et al. 2024 ("In defense of RAG") than to Li et al. 2024 ("RAG vs long-context").
- **What this implies for system design more broadly**: when the underlying primitive (reader LM) gets dramatically stronger, the abstractions that were built to compensate for its weakness can become net-negative — they add latency, cost, and failure modes for capability you no longer need. The paper is one concrete data point for the broader pattern that pipeline complexity should be revisited at every major model-capability jump.

## How to Apply It (method)

**To replicate or use DOS RAG in your own system:**

1. **Chunk the document.** Split into passages capped at 100 tokens each, preserving sentence boundaries where possible (the paper uses NLTK's default sentence segmenter for boundary detection). Record each passage's original position index `i` in the document — this index is what the reorder step uses.
2. **Embed query and passages.** Use Snowflake Arctic-embed-m 1.5 (109M params, available on Hugging Face — the paper picks it because it's a strong open-weights sentence embedder that scales cleanly). Both query and passages get encoded into the same vector space; passage embeddings can be cached per document.
3. **Retrieve by cosine similarity.** Rank all passages by cosine similarity to the query embedding. Take the top-k passages where `sum(passage_tokens) ≤ budget` — the paper sweeps budgets of 500, 1K, 1.5K, 2K, 4K, 6K, 8K, 10K, 20K, 30K, 40K tokens. The 10-40K range is where DOS RAG decisively beats baselines.
4. **The DOS step (the one-line change).** Take the surviving k passages and sort them in ascending order of their original document position index `i` — *not* by similarity score. So if you retrieved passages at positions {17, 3, 42, 9}, you concatenate them as 3 → 9 → 17 → 42, not as 17 → 3 → 42 → 9 (the Vanilla RAG order, sorted by descending similarity).
5. **Construct the reader prompt.** Use the paper's QA template (Prompt A.1 in Appendix A.8): `[Start of Context]: {ordered_passages} [End of Context] [Start of Question]: {questionAndOptions} [End of Question] [Instructions:] Based on the context provided, select the most accurate answer...` For free-form QA use Prompt A.2 (asks for short factual answer or "Not found in context").
6. **Greedy decode with GPT-4o or GPT-4o-mini** (the paper uses `gpt-4o-2024-11-20` and `gpt-4o-mini-2024-07-18`). The paper's ablations and ceiling effects suggest you want recall up to ~30K tokens; pushing past that hits diminishing returns and even slight degradation on ∞Bench, consistent with Liu et al. 2024's "lost in the middle" findings on the effective context-window limit.

**To benchmark your own RAG method against DOS RAG (the paper's headline ask):**

- Match the token budget at the reader's input, not at retrieval — different methods produce different prompt sizes from the same k.
- Report mean ± standard deviation over at least 5 runs (the paper uses 5).
- Use a reader strong enough to be representative of today's deployment surface (GPT-4-class or open-weights equivalent at ≥32K context); reporting only on weaker readers risks reproducing RAPTOR's original "UnifiedQA-3B at 400 tokens" framing that no longer generalises.
- Code is released at https://github.com/alex-laitenberger/stronger-baselines-rag.

## Best Figure

![Figure 1 — ∞Bench En.MC performance of various multi-stage RAG systems and long-context baselines (page 1)](figures/laitenberger-2025-dos-rag-fig.png)

**Image Candidates:**
- Figure 1 (p. 1): The headline plot — accuracy vs. average LM input tokens on ∞Bench with GPT-4o, showing DOS RAG (orange) above Vanilla RAG (blue) and RAPTOR (green) across all token budgets, with ReadAgent (red dot) far to the right consuming ~86K tokens but underperforming DOS RAG at 30K.
- Figure 3 (p. 4): QuALITY counterpart showing DOS RAG wins under token budgets but the full-document baseline wins overall once docs fit in context — the "long-context can subsume retrieval when it fits" caveat.
- Figure 2 (p. 2): Pipeline-architecture comparison diagram showing Vanilla/DOS RAG as one box (Embed → Retrieve → Read) versus RAPTOR's four-stage pipeline (Embed → Cluster → Summarize → Retrieve → Read) versus ReadAgent's three LM-based stages (Paginate → Gist → Lookup → Read) — visually communicates the simplicity argument.

**Best Image: Figure 1** — the single chart that carries the paper's whole thesis. The x-axis is "Average LM Input Tokens per Question" (1.5K to 90K, broken axis); the y-axis is accuracy on ∞Bench En.MC (72.5% to 92.5%). Four curves: DOS RAG (orange) climbs from ~76% at 1.5K to a peak of 93.1% at 30K, then plateaus. Vanilla RAG (blue) follows the same shape but ~5-6 points lower. RAPTOR (green) is another ~3 points below Vanilla. ReadAgent appears as a single red dot at ~86K tokens, ~90.3% accuracy — visibly worse than DOS RAG's 91.4% at 20K. The chart makes the cost/benefit argument viscerally: spending 4-5× the tokens via a multi-stage agent gets you nothing. Caption notes "For token budgets greater than 5K, DOS RAG outperforms the complex multi-stage methods (ReadAgent and RAPTOR) by 2-8 points."

## What Experts Overlook

- **The "exact ablation" framing of Vanilla RAG vs RAPTOR is the load-bearing rhetorical move that most readers will skim past.** The paper explicitly designed Vanilla RAG to be RAPTOR with the summary-tree step removed (same embedding model, same retriever, same reader) — and Vanilla RAG beats RAPTOR. That means the RAPTOR contribution itself (recursive LM-summarised cluster trees) is what's costing accuracy, not just being neutral. Many readers will see "DOS RAG > RAPTOR" and conclude "the reorder step is what matters" — but Vanilla RAG > RAPTOR shows the summary step is actively harmful in this regime, separately from the reorder benefit DOS RAG layers on top.
- **The paper's headline benchmark (∞Bench En.MC, 229 questions over 58 documents) is small.** Multiple-choice accuracy on 229 questions with five runs gives reasonably tight error bars (reported standard deviations are 0.2-1.2 points), but the absolute test surface is narrow. NarrativeQA (10,557 questions) provides the heavier statistical evidence; QuALITY (2,086 questions) is middle ground. Readers reaching for "RAPTOR is dead" should be aware the strongest piece of evidence is on the smallest benchmark.
- **The ReadAgent result is reported as one point at one token budget**, not as a curve. ReadAgent's design doesn't admit a clean token-budget sweep the way Vanilla/DOS RAG do (its token cost is determined by the gisting+pagination stages, not by a tunable k), so the paper compares ReadAgent's natural operating point to DOS RAG at a comparable budget. That's a defensible methodological choice but it's not the same kind of comparison the Vanilla/DOS/RAPTOR curves represent.
- **The full-document baseline beats DOS RAG on QuALITY** (91.2% vs 90.4% at 8K, with GPT-4o). The paper acknowledges this — when the document fits in context, just paste the whole thing. That's a useful boundary condition: DOS RAG's value proposition is for docs that *don't* fit (∞Bench's 184K-token average, NarrativeQA's 57K average up to 404K). Practitioners with mostly-short documents may not need retrieval at all.
- **The paper does not measure end-to-end cost** (embedding-time, preprocessing, only inference tokens). RAPTOR builds its tree once per document but the build cost is non-trivial; ReadAgent runs gisting LM calls per query. The paper estimates these add cost but doesn't quantify them — a gap acknowledged in the Limitations section. For a comparison framed around "simplicity wins," not measuring the actual cost dimension is a real gap.
- **The "effective context window" finding** — DOS RAG accuracy on ∞Bench peaks at 30K and declines at 40K — is treated as a brief aside but echoes Nelson Liu's own prior "Lost in the Middle" work (one of the authors). It implies the recommended operating point is the effective-context-window minus some safety margin, not simply "as much retrieval as you can afford." Most readers will miss this calibration nuance.
- **Author asymmetry matters here.** Christopher Manning is co-author on both RAPTOR (Sarthi et al. 2024) and this paper, and Nelson Liu is co-author on both "Lost in the Middle" (Liu et al. 2024) and this paper. So the paper is partly a Stanford NLP group revisiting and qualifying its own recent work as model capabilities advanced — not an outside critique. That's actually a good sign for credibility (the authors had every incentive to keep RAPTOR's positioning intact) but worth knowing.

## Extracted Prompts

The paper publishes two reader prompts verbatim. Both use a simple bracket-tagged structure that signals start/end of context and question — useful for any retrieve-then-read system where the reader needs to clearly distinguish supplied context from the question.

**Prompt A.1 — Multiple-choice QA** (∞Bench En.MC, QuALITY):

```
[Start of Context]:
{context}
[End of Context]
[Start of Question]:
{questionAndOptions}
[End of Question]
[Instructions:] Based on the context provided, select the most accurate answer to the question from the given options. Start with a short explanation and then provide your answer as [[1]] or [[2]] or [[3]] or [[4]]. For example, if you think the most accurate answer is the first option, respond with [[1]].
```

**Prompt A.2 — Short-answer QA** (NarrativeQA):

```
[Start of Context]:
{context}
[End of Context]
[Start of Question]:
{question}
[End of Question]
[Instructions:] - Answer the question **only** based on the provided context.
- Keep the answer **short and factual** (preferably between 1-20 words).
- Do **not** provide explanations or additional details beyond what is necessary.
- If the answer is **not explicitly stated** in the context, respond with: "Not found in context."
```

Two design choices worth borrowing: (a) explicit `[[N]]` answer formatting for MC so you can regex-extract the answer reliably, and (b) the explicit "Not found in context" escape hatch for free-form QA, which gives the model a graceful refusal path instead of forcing hallucination when retrieval misses.

## Citations

The paper cites 14 prior works, all extracted to the `citations` frontmatter array. First 10 as bullets:

- **Chen et al. 2023** — Walking down the memory maze: Beyond context limit through interactive reading (ArXiv:2310.05029) — cited as early multi-stage agentic-retrieval work
- **Khashabi et al. 2020** — UNIFIEDQA: Crossing format boundaries with a single QA system (Findings of EMNLP) — the 400-token-input reader RAPTOR's original ablation used; cited to argue RAPTOR's win does not generalise to modern long-context readers
- **Kočiský et al. 2018** — The NarrativeQA reading comprehension challenge (TACL) — benchmark used in the paper
- **Lee et al. 2024** — ReadAgent: A human-inspired reading agent with gist memory of very long contexts (ICML) — one of the two multi-stage baselines compared. Already in wiki at [[lee-2024-readagent-gist-memory]]
- **Lewis et al. 2020** — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (NeurIPS) — the canonical RAG paper. Already in wiki at [[lewis-2020-rag-knowledge-nlp]]
- **Li et al. 2024** — Retrieval augmented generation or long-context LLMs? A comprehensive study and hybrid approach (EMNLP Industry) — Related Work, on the long-context-vs-RAG debate
- **Liu et al. 2024** — Lost in the middle: How language models use long contexts (TACL) — Nelson Liu's own prior paper; cited for the effective-context-window limit. Already in wiki at [[liu-2023-lost-in-the-middle]]
- **Merrick 2024** — Embedding and clustering your data can improve contrastive pretraining (Snowflake Arctic-Embed paper, ArXiv:2407.18887) — the embedding model used throughout
- **Pang et al. 2022** — QuALITY: Question answering with long input texts, yes! (NAACL) — benchmark used in the paper
- **Sarthi et al. 2024** — RAPTOR: Recursive abstractive processing for tree-organized retrieval (ICLR) — one of the two multi-stage baselines compared, and Christopher Manning is co-author on both this paper and RAPTOR. Already in wiki at [[sarthi-2024-raptor]]

Remaining 4 (Sun 2024 PEARL, Xu 2024 retrieval-meets-long-context, Yu 2024 in-defense-of-RAG, Zhang 2024 ∞Bench) preserved in frontmatter for the auto-research hook.

## Related Digests

- [[sarthi-2024-raptor]] — RAPTOR: Recursive abstractive processing for tree-organized retrieval (one of the two multi-stage baselines this paper argues against; Manning is co-author of both)
- [[lee-2024-readagent-gist-memory]] — ReadAgent: A human-inspired reading agent with gist memory of very long contexts (the other multi-stage baseline compared; shown to consume ~86K tokens while underperforming DOS RAG at 30K)
- [[lewis-2020-rag-knowledge-nlp]] — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (the canonical RAG framing that DOS RAG simplifies back toward)
- [[liu-2023-lost-in-the-middle]] — Lost in the middle: How language models use long contexts (Nelson Liu's prior work; explains why DOS RAG accuracy peaks then declines past 30K tokens — the effective-context-window ceiling)

## Reviewer Notes

**Hallucination severity:** Clean

**Reviewer summary:** The digest faithfully reflects the paper's claims, methodology, and numbers. Specific numeric claims spot-checked against the paper text:

- "DOS RAG achieves 93.1% at 30K on ∞Bench" — verified against Table 2 (∞Bench / GPT-4o / DOS RAG / 30K = 93.1% ± 0.5%). Correct.
- "Vanilla RAG 87.8% at 30K on ∞Bench / GPT-4o" — Table 2: 87.8% ± 0.4%. Correct.
- "ReadAgent ~86K tokens" — verified against Table 1 / Table 2 "(Avg. Tokens: 86K)". Correct.
- "Full document beats DOS RAG on QuALITY (91.2% vs 90.4% at 8K, GPT-4o)" — Table 4: full document 91.2% ± 0.2%, DOS RAG 90.4% ± 0.3% at 8K. Correct.
- "NarrativeQA DOS RAG uses ~1/3 the tokens of ReadAgent at superior performance" — paper says: "DOS RAG achieves superior results while using only one third of the tokens required by ReadAgent." Direct quote. Correct.
- "Snowflake Arctic-embed-m 1.5, 109M parameters" — Appendix A.1 confirms. Correct.
- "229 multiple-choice questions on 58 documents (avg 184K tokens) for ∞Bench" — Section 2.1 confirms. Correct.
- "115 documents, 2086 questions for QuALITY dev set" — Section 2.1 confirms. Correct.
- "355 stories, 57K avg up to 404K, 10,557 questions for NarrativeQA test set" — Section 2.1 confirms (with 352 / 10,391 after broken downloads, per Appendix C). Correct — the digest mentions the headline 355/10,557 figure consistent with how the paper introduces the benchmark.
- "DOS RAG performance peaks at 30K and plateaus past that on ∞Bench" — Section 3 ∞Bench paragraph explicitly says "DOS RAG performance begins to plateau as the retrieval budget grows beyond 30K tokens." Correct.
- "RAPTOR's original paper used UnifiedQA-3B at 400-token input" — Section 4 confirms. Correct.

**Minor calibrations:** The digest characterises the four-factor analysis (source fidelity, recall-over-precision, document-order reordering, simplicity) accurately — these are explicitly the four bullets in Section 4 and again summarised in Section 6 Conclusion. The framing that this paper is partly "a Stanford NLP group revisiting its own work" is supported by author overlap (Manning on RAPTOR; Nelson Liu on Lost in the Middle) and is presented as context not as critique.

**Net verdict:** Clean. No invented numbers, no fabricated mechanisms, no claims the paper does not make. The digest is conservative where the paper is conservative (limitations explicitly scoped to single-doc MC/short-answer QA with GPT-4o readers).
