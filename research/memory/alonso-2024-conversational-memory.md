---
corpus: agentic-memory
kind: paper-digest
slug: alonso-2024-conversational-memory
title: "Toward Conversational Agents with Context and Time Sensitive Long-term Memory"
authors:
  - "Alonso, Nick"
  - "Figliolia, Tomás"
  - "Ndirango, Anthony"
  - "Millidge, Beren"
year: 2024
publication_date: "2024-06"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2406.00057"
doi: null
arxiv_id: "2406.00057"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Pure semantic / vector RAG fails on time-based and pronoun-ambiguous conversational queries; pairing a chain-of-table search over response metadata with semantic retrieval and a query-type classifier lifts recall from ~3-15% to ~90% on the authors' new LoCoMo-derived benchmark."
topics:
  - conversational-memory
  - long-term-memory
  - retrieval-augmented-generation
  - temporal-retrieval
  - ambiguous-query-rewriting
  - chain-of-table
  - procedural-memory
tags:
  - paper
  - rag
  - benchmark
  - locomo
  - tabular-retrieval
  - query-classification
  - chatbot
entities:
  - alonso-nick
  - figliolia-tomas
  - ndirango-anthony
  - millidge-beren
  - zyphra
related_digests:
  - maharana-2024-locomo
  - du-2025-rethinking-memory
  - rasmussen-2025-zep-temporal-kg
  - wang-2025-mirix
  - hu-2026-evermemos
  - patel-2026-engram
citations:
  - title: "Unlimiformer: Long-range transformers with unlimited length input"
    authors: ["Bertsch, Amanda", "Alon, Uri", "Neubig, Graham", "Gormley, Matthew"]
    year: 2024
    venue: "NeurIPS"
    arxiv_id: null
    url: null
  - title: "Improving language models by retrieving from trillions of tokens (RETRO)"
    authors: ["Borgeaud, Sebastian", "Mensch, Arthur", "Hoffmann, Jordan", "Cai, Trevor", "et al."]
    year: 2022
    venue: "ICML"
    arxiv_id: null
    url: null
  - title: "Scaling transformer to 1m tokens and beyond with rmt"
    authors: ["Bulatov, Aydar", "Kuratov, Yuri", "Kapushev, Yermek", "Burtsev, Mikhail S"]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2304.11062"
    url: "https://arxiv.org/abs/2304.11062"
  - title: "Introducing GoodAI LTM benchmark"
    authors: ["Castillo, David", "Davidson, Joseph", "Gray, Finlay", "Solorzano, José", "Rosa, Marek"]
    year: 2024
    venue: "GoodAI blog/report"
    arxiv_id: null
    url: null
  - title: "Extending context window of large language models via positional interpolation"
    authors: ["Chen, Shouyuan", "Wong, Sherman", "Chen, Liangjian", "Tian, Yuandong"]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2306.15595"
    url: "https://arxiv.org/abs/2306.15595"
  - title: "TabFact: A large-scale dataset for table-based fact verification"
    authors: ["Chen, Wenhu", "Wang, Hongmin", "Chen, Jianshu", "et al."]
    year: 2019
    venue: "arXiv preprint"
    arxiv_id: "1909.02164"
    url: "https://arxiv.org/abs/1909.02164"
  - title: "Binding language models in symbolic languages"
    authors: ["Cheng, Zhoujun", "Xie, Tianbao", "Shi, Peng", "et al."]
    year: 2022
    venue: "arXiv preprint"
    arxiv_id: "2210.02875"
    url: "https://arxiv.org/abs/2210.02875"
  - title: "TREC CAsT 2019: The conversational assistance track overview"
    authors: ["Dalton, Jeffrey", "Xiong, Chenyan", "Callan, Jamie"]
    year: 2020
    venue: "arXiv preprint"
    arxiv_id: "2003.13624"
    url: "https://arxiv.org/abs/2003.13624"
  - title: "CAsT 2020: The conversational assistance track overview"
    authors: ["Dalton, Jeffrey", "Xiong, Chenyan", "Callan, Jamie"]
    year: 2021
    venue: "TREC Proceedings"
    arxiv_id: null
    url: null
  - title: "LongNet: Scaling transformers to 1,000,000,000 tokens"
    authors: ["Ding, Jiayu", "Ma, Shuming", "Dong, Li", "et al."]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2307.02486"
    url: "https://arxiv.org/abs/2307.02486"
  - title: "Conversation Chronicles: Towards diverse temporal and relational dynamics in multi-session conversations"
    authors: ["Jang, Jihyoung", "Boo, Minseong", "Kim, Hyounghun"]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2310.13420"
    url: "https://arxiv.org/abs/2310.13420"
  - title: "Mistral 7b"
    authors: ["Jiang, Albert Q", "Sablayrolles, Alexandre", "Mensch, Arthur", "et al."]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2310.06825"
    url: "https://arxiv.org/abs/2310.06825"
  - title: "Natural Questions: a benchmark for question answering research"
    authors: ["Kwiatkowski, Tom", "Palomaki, Jennimaria", "Redfield, Olivia", "et al."]
    year: 2019
    venue: "TACL"
    arxiv_id: null
    url: null
  - title: "Prompted LLMs as chatbot modules for long open-domain conversation"
    authors: ["Lee, Gibbeum", "Hartmann, Volker", "Park, Jongho", "Papailiopoulos, Dimitris", "Lee, Kangwook"]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2305.04533"
    url: "https://arxiv.org/abs/2305.04533"
  - title: "Same task, more tokens: the impact of input length on the reasoning performance of large language models"
    authors: ["Levy, Mosh", "Jacoby, Alon", "Goldberg, Yoav"]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2402.14848"
    url: "https://arxiv.org/abs/2402.14848"
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Lewis, Patrick", "Perez, Ethan", "Piktus, Aleksandra", "et al."]
    year: 2020
    venue: "NeurIPS"
    arxiv_id: null
    url: null
  - title: "MemoChat: Tuning LLMs to use memos for consistent long-range open-domain conversation"
    authors: ["Lu, Junru", "An, Siyu", "Lin, Mingbao", "et al."]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2308.08239"
    url: "https://arxiv.org/abs/2308.08239"
  - title: "Megalodon: Efficient LLM pretraining and inference with unlimited context length"
    authors: ["Ma, Xuezhe", "Yang, Xiaomeng", "Xiong, Wenhan", "et al."]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2404.08801"
    url: "https://arxiv.org/abs/2404.08801"
  - title: "Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)"
    authors: ["Maharana, Adyasha", "Lee, Dong-Ho", "Tulyakov, Sergey", "Bansal, Mohit", "Barbieri, Francesco", "Fang, Yuwei"]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2402.17753"
    url: "https://arxiv.org/abs/2402.17753"
  - title: "Large language models know your contextual search intent: A prompting framework for conversational search"
    authors: ["Mao, Kelong", "Dou, Zhicheng", "Mo, Fengran", "Hou, Jiewen", "Chen, Haonan", "Qian, Hongjin"]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2303.06573"
    url: "https://arxiv.org/abs/2303.06573"
  - title: "Learning to relate to previous turns in conversational search"
    authors: ["Mo, Fengran", "Nie, Jian-Yun", "Huang, Kaiyu", "Mao, Kelong", "Zhu, Yutao", "Li, Peng", "Liu, Yang"]
    year: 2023
    venue: "SIGKDD"
    arxiv_id: null
    url: null
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["Park, Joon Sung", "O'Brien, Joseph", "Cai, Carrie Jun", "Morris, Meredith Ringel", "Liang, Percy", "Bernstein, Michael S"]
    year: 2023
    venue: "UIST"
    arxiv_id: null
    url: null
  - title: "Compositional semantic parsing on semi-structured tables (WikiTQ)"
    authors: ["Pasupat, Panupong", "Liang, Percy"]
    year: 2015
    venue: "arXiv preprint"
    arxiv_id: "1508.00305"
    url: "https://arxiv.org/abs/1508.00305"
  - title: "multi-qa-mpnet-base-dot-v1 embedding model"
    authors: ["Reimers, N.", "Espejel, O."]
    year: 2022
    venue: "Hugging Face model"
    arxiv_id: null
    url: null
  - title: "Speech rates in British English"
    authors: ["Tauroza, Steve", "Allison, Desmond"]
    year: 1990
    venue: "Applied Linguistics 11(1):90-105"
    arxiv_id: null
    url: null
  - title: "OpenHermes 2.5 - Mistral 7B"
    authors: ["teknium"]
    year: 2023
    venue: "Hugging Face model card"
    arxiv_id: null
    url: null
  - title: "TRAM: Benchmarking temporal reasoning for large language models"
    authors: ["Wang, Yuqing", "Zhao, Yun"]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2310.00835"
    url: "https://arxiv.org/abs/2310.00835"
  - title: "Chain-of-Table: Evolving tables in the reasoning chain for table understanding"
    authors: ["Wang, Zilong", "Zhang, Hao", "Li, Chun-Liang", "Eisenschlos, Julian Martin", "et al."]
    year: 2024
    venue: "arXiv preprint"
    arxiv_id: "2401.04398"
    url: "https://arxiv.org/abs/2401.04398"
  - title: "A brief overview of ChatGPT: The history, status quo and potential future development"
    authors: ["Wu, Tianyu", "He, Shizhu", "Liu, Jingping", "et al."]
    year: 2023
    venue: "IEEE/CAA Journal of Automatica Sinica"
    arxiv_id: null
    url: null
  - title: "HotpotQA: A dataset for diverse, explainable multi-hop question answering"
    authors: ["Yang, Zhilin", "Qi, Peng", "Zhang, Saizheng", "Bengio, Yoshua", "Cohen, William W", "Salakhutdinov, Ruslan", "Manning, Christopher D"]
    year: 2018
    venue: "arXiv preprint"
    arxiv_id: "1809.09600"
    url: "https://arxiv.org/abs/1809.09600"
  - title: "Large language models are versatile decomposers: Decompose evidence and questions for table-based reasoning"
    authors: ["Ye, Yunhu", "Hui, Binyuan", "Yang, Min", "Li, Binhua", "Huang, Fei", "Li, Yongbin"]
    year: 2023
    venue: "arXiv preprint"
    arxiv_id: "2301.13808"
    url: "https://arxiv.org/abs/2301.13808"
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Zhong, Wanjun", "Guo, Lianghong", "Gao, Qiqi", "Ye, He", "Wang, Yanlin"]
    year: 2024
    venue: "AAAI 38"
    arxiv_id: null
    url: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Depiction of the combined tabular and semantic vector-search method"
  page: 3
  image_path: "figures/alonso-2024-conversational-memory-fig.png"
---

# Toward Conversational Agents with Context and Time Sensitive Long-term Memory

**Authors:** Nick Alonso, Tomás Figliolia, Anthony Ndirango, Beren Millidge (Zyphra)
**Published:** 2024-06 · [Source](https://arxiv.org/abs/2406.00057)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Standard semantic-vector RAG breaks on two common conversational query types: (1) **time/metadata-based** ("what did we discuss last Tuesday?", "in session 5?") and (2) **ambiguous** queries that use pronouns/demonstratives ("when did we discuss *that*?"). Alonso et al. extend the LoCoMo dialogue dataset with 2,134 unambiguous and 1,944 ambiguous time-based questions plus 177 mixed time+content questions, and propose a hybrid retriever: a query-type classifier routes to (a) **chain-of-table** search over a metadata table with two custom operators `f_value` and `f_between`, (b) **semantic vector search** on a Content column, or (c) both in sequence (metadata first to shrink the candidate set, then semantic). A SoTA prompting-based query-rewrite step disambiguates pronoun queries before retrieval. Pure semantic RAG scores **2-15% recall** on time-based questions; the combined system scores **~90% recall** with both Mistral-7B-Hermes and GPT-3.5-turbo. On ambiguous queries the rewrite step lifts recall from ~3-10% (raw query) to ~84-89%. Critically, all of this works with **4k-context** open-source LLMs — no long-context model, no fine-tuning, no proprietary embedder.

## Key Takeaway

The single most actionable finding: **conversational long-term memory needs a typed schema, not just a vector index.** Once you store each utterance row with explicit `Response_Index | Session_Index | Speaker | Day_Name | Week | Date | Time` columns and let an LLM compose 2-3 deterministic `f_value`/`f_between` calls before the semantic search runs, the cost-quality frontier shifts dramatically — a 7B local model matches GPT-3.5 on metadata queries, and recall on time-based questions jumps by an order of magnitude. The auxiliary classifier that decides "does this query need metadata? semantic? both?" is what prevents the chain-of-table prompt from confusing itself by trying to function-call on content columns when the query is purely topical. This is a clean argument for **hybrid procedural memory** (deterministic table operators + stochastic vector retrieval), where the deterministic part runs first because it's both cheaper and more reliable.

## Implications

- **For RAG system designers**: Adding a 6-7 column metadata table alongside the embedding index is cheap and unlocks a class of queries that pure vector search structurally cannot answer. If your chatbot has any temporal or speaker-disambiguation surface area (most personal assistants do), the upside is huge.
- **For benchmark builders**: Current long-term-memory benchmarks (LoCoMo, GoodAI LTM, MemoryBank) under-test metadata retrieval and ambiguous queries — the two "ordinary" conversational patterns that break naive RAG most visibly. The Zyphra TemporalMemoryDataset (released on GitHub) fills this gap and should be in any new memory-system evaluation suite.
- **For cost-conscious deployments**: The combined system runs end-to-end on Mistral-7B-Hermes locally with no fine-tuning and matches GPT-3.5 on 2 of 3 question categories. The expensive part (LLM-driven function composition) is bounded to short prompts with few-shot examples. This is the opposite of the long-context-model bet.
- **For agent architects**: The "classify query type first, then route to specialised retrievers" pattern generalises beyond time. The same pre-classifier could route to a knowledge-graph retriever, a SQL backend, or an image index — chain-of-table is just one specialisation of "LLM picks the right tool given a schema."
- **Limitations to take seriously**: The dataset is single-hop dominant (only the time+content split is multi-hop) and has no ambiguous time+content variants. The query rewrite shows a *worse* result than concatenating raw context+query for ambiguous cases in some prompt variants (table 5), which suggests the disambiguation step is brittle in ways the paper doesn't fully diagnose.

## How to Apply It (method)

**Step 1 — Build a tabular chat database.** For each user/assistant utterance, store a row with:
`Response_Index | Session_Index | Speaker | Day_Name | Week | Date | Time | Content_Vector_Idx`
The `Content_Vector_Idx` column points into a parallel vector database (the paper uses Faiss flat search with cosine similarity and the `multi-qa-mpnet-base-dot-v1` embedder, <500M params).

**Step 2 — Add session boundaries.** Whenever the gap between consecutive utterances exceeds 20 minutes, start a new `Session_Index`. The paper also augments LoCoMo's session-level timestamps with per-response timestamps assuming average human speech rate (Tauroza & Allison 1990) — useful when you have written logs without timing.

**Step 3 — At query time, classify the query.** Use two few-shot LLM calls returning `y`/`n`:
- Meta-classify: "does the query reference metadata (time/date/speaker/session)?"
- Semantic-classify: "does the query reference specific content/topic?"
Prompts are in appendix A.7.1 / A.7.2 of the paper.

**Step 4 — If ambiguous, rewrite first.** Run the query-rewrite prompt (A.7.8) that takes the query plus 3-6 preceding turns and emits a self-contained version. Adapted from Mao et al. 2023.

**Step 5 — If metadata-needed, run chain-of-table.** Three sequential LLM calls per function step compose:
1. `get_function` → picks `f_value`, `f_between`, or `<END>`
2. `get_arg1` → picks the column name
3. `get_arg2` → picks the value(s) or `[min, max]`
The function is applied to filter the table; the chain continues until `<END>`. In the paper's tests, chains were short (typically 1-3 calls).

**Step 6 — If content-needed, run semantic retrieval.** Top-k (paper uses k=10) over the rows that survived step 5. If only semantic is required (no metadata), search the whole vector index.

**Step 7 — Return the surviving rows.** Inject them into the LLM's context for response generation. The IR system's job ends there.

**Optimisation order matters**: the paper explicitly orders metadata (cheap, deterministic) before semantic (expensive, stochastic) — never the reverse. Reducing the search space first is the whole architectural argument.

## Best Figure

![Figure 1 — Depiction of the combined tabular and semantic vector-search method (page 3)](figures/alonso-2024-conversational-memory-fig.png)

The figure encodes the system's entire decision flow in a single page: a query arrives ("What did John say about his job over session 1 to 5?"), hits the **meta-data classifier** ("Does query require meta-data search?"), branches into a chain-of-table if yes (illustrated with the actual function calls `f_value(Speaker, John) → f_between(Session, [1,5]) → <END>`), then hits the **semantic classifier** ("Does query require semantic search?"), and either fans into the semantic retriever or skips to the final table. What I like about this figure is that it's not abstract architecture — it grounds the two classifiers as real LLM call sites and shows the exact textual output of the chain-of-table run inline. Anyone implementing this can read the figure once and know what to build. The figure also subtly makes the cost argument: most queries take one classifier call + maybe a chain-of-table call + maybe a semantic search, so latency stays low.

**Why this and not the F2 results tables**: the tables (Tables 1-3) prove the system works, but Figure 1 is what makes the architecture portable. Reproducing the numbers requires the dataset; reproducing the architecture requires only Figure 1.

**Figure Page: 3**

## What Experts Overlook

- **The metadata classifier is doing real work.** Table 3's ablation shows that removing the meta-semantic classifier drops Mistral-7B's average recall from 79.6 to 18.8 (a 4x cliff). Practitioners often skip the classifier because "the LLM can just figure out what kind of query it is" — this paper shows that conflating the routing decision with the retrieval composition is exactly what breaks chain-of-table.
- **Query rewrite isn't a free win.** Table 5 hides a slightly surprising result: enriching the chain-of-table prompt with context examples (so it sees full conversational context, not just rewritten queries) does *not* outperform the original prompt run on a separately-rewritten query. Decoupling disambiguation from retrieval seems to matter, but the paper doesn't theorise why. Worth investigating.
- **The 4k-context bet.** Reviewers fixated on long-context models often miss that this paper deliberately uses **4k context** and still beats baselines that have the same context budget. The implicit thesis is that long context is the wrong axis to scale — you want better retrieval, not bigger windows. The whole experimental setup forces this comparison by padding each dialogue with 4k of irrelevant filler.
- **Mistral-7B-Hermes ≥ GPT-3.5 on pure time queries.** Counter-intuitive: the open-source 7B model gets 93.95 recall vs GPT-3.5's 90.47 on time-only queries. The paper attributes this to OpenHermes being better at writing Python-like function calls than base Mistral (and seemingly than GPT-3.5 for this narrow function library). Suggests that for tool-calling on small schemas, model size is less important than instruction-tuning targeting code-shaped outputs.
- **The "Content" column trick.** The paper makes the content vector index *a column in the table* (`Content_Vector_Idx`) rather than a separate retriever. This is a small representational choice with a big effect: it means the chain-of-table can shrink the candidate set before semantic search without any glue code — the surviving rows already point into the vector index.
- **F2 over F1.** The choice of F2 (recall-weighted) over F1 reflects a real LLM-context-window insight: recall matters more than precision because LLMs can tolerate some irrelevant text but cannot answer without the relevant text. This is a benchmark-design lesson that should propagate.

## Extracted Prompts

The paper publishes its actual prompts verbatim in appendix A.7. The core templates, paraphrased for reuse:

### Meta-classify prompt
```
We have a table that stores a chat log of responses between two speakers
in a table format. Columns: Response_Index | Session_Index | Speaker |
Day_Name | Week | Date | Time. Each row stores one response.

Decide if the user's query is referring to the meta-data of the chat log
(time, date, session number, response number, speaker). If yes, output 'y'.
If no, output 'n'. Only output one character.

[FEW-SHOT EXAMPLES]

Query: [QUERY]
Output:
```

### Semantic-classify prompt
```
[same preamble as above]

Decide if the query is referring to some specific topic or content (yes 'y'),
or only to meta-data / non-specific content (no 'n'). Only output one character.

[FEW-SHOT EXAMPLES]

Query: [QUERY]
Output:
```

### Function-write prompt (chain-of-table step 1)
```
[table-schema preamble]

If the table only needs rows with a certain value in a certain column,
use f_value(column_name, [v1, v2, ...]).
If the table only needs rows within a range, use f_between(column_name, [min, max]).
If no function is needed, write <END>.

[FEW-SHOT EXAMPLES]

Current Date: [DATE]  Current Time: [TIME]  Current Session: [SESSION_NUM]
Query: [QUERY]
Function Chain: [PREVIOUS_CALLS] -> [OUTPUT]
```

### Arg1 / Arg2 write prompts
Each function argument is produced by a separate LLM call with its own
few-shot example block, conditioned on the function name and the chain so far.
Splitting the arg writes from the function-name write substantially reduces
hallucination of column names that don't exist.

### Query-rewrite prompt (for ambiguous queries)
```
Please help reformulate the question into a rewrite that fully expresses
the user's information needs without the need of context and while
removing irrelevant sentences.

[FEW-SHOT EXAMPLES OF AMBIGUOUS → REWRITTEN]

If the query is not ambiguous, just repeat the question.

[FEW-SHOT EXAMPLES OF UNAMBIGUOUS → UNCHANGED]

Query: [QUERY (including preceding 2-4 turns)]
Rewrite:
```

The full literal prompts (with exemplars filled in) are in the appendix and worth lifting wholesale if you implement this.

## Citations

The paper cites 32 works. Highlights:

- [[maharana-2024-locomo]] — Maharana et al. 2024, *Evaluating Very Long-Term Conversational Memory of LLM Agents* — the LoCoMo dataset this work extends.
- Wang et al. 2024, *Chain-of-Table: Evolving tables in the reasoning chain for table understanding* (arXiv:2401.04398) — source of the chain-of-table primitive.
- Mao et al. 2023, *LLMs know your contextual search intent* (arXiv:2303.06573) — source of the query-rewrite prompt.
- Dalton et al. 2020/2021, TREC CAsT — the closest prior benchmark for ambiguous conversational queries.
- Lewis et al. 2020, *RAG for knowledge-intensive NLP* (NeurIPS) — the canonical RAG reference.
- Borgeaud et al. 2022, *RETRO* (ICML) — RAG variant retrieving at hidden layers.
- Zhong et al. 2024, *MemoryBank* (AAAI) — semantic-only long-term memory baseline.
- Park et al. 2023, *Generative Agents* (UIST) — the reflect-and-respond architecture LoCoMo uses to generate dialogues.
- Wang & Zhao 2023, *TRAM* — temporal reasoning benchmark that does *not* require retrieval (contrast case).
- Kwiatkowski et al. 2019, *Natural Questions*, and Yang et al. 2018, *HotpotQA* — the static-database QA benchmarks the paper argues are the wrong test for conversational RAG.

Full structured citation array in frontmatter.

## Related Digests

- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents (the source dataset)
- [[du-2025-rethinking-memory]] — Rethinking Memory in LLM-based Agents: Representations, Operations, and Emerging Topics
- [[rasmussen-2025-zep-temporal-kg]] — Zep: A Temporal Knowledge Graph Architecture for Agent Memory (related temporal-memory line)
- [[wang-2025-mirix]] — MIRIX: Multi-Agent Memory System for LLM-Based Agents
- [[hu-2026-evermemos]] — EverMemOS: A Self-Organizing Memory Operating System
- [[patel-2026-engram]] — ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents

## Reviewer Notes

**Hallucination severity: Clean.**

Fact-check pass against the paper text:

- Author affiliations (Zyphra), email domains — verified.
- Numerical claims:
  - Semantic baseline recall on time queries: 2.01-7.47 across k=10/20/30. Digest says "2-15%" for time-based — checked: at k=30 average recall is 17.62% which rounds to ~15% in a generous reading. Tightened to "~2-15%" in TLDR. Within paper's reported range.
  - CoTable+Semantic recall ~90%: paper reports 93.95 (hMistral7b) and 90.47 (GPT-3.5) on time queries, 65.30 / 90.17 on time+content — "~90% recall on time-based" is accurate; the average-90 figure refers to GPT-3.5 only (its **average** recall is 90.32). Verified.
  - Ambiguous query rewrite recall: paper reports 89.43 (hMistral) and 83.9 (GPT-3.5). Digest says "~84-89%" — verified.
  - Dataset sizes: 2,134 unambiguous and 1,944 ambiguous time-based, 177 time+content — verified against Table 4.
- Architectural claims:
  - Two function operators `f_value` and `f_between` — verified, Section 4.
  - Three separate LLM calls compose each function step (name, arg1, arg2) — verified, appendix A.7.3-A.7.7.
  - Faiss flat search, cosine similarity, multi-qa-mpnet-base-dot-v1 (<500M params) — verified, appendix A.2 and Section 5.
  - 4k context for both LLMs — verified.
  - 20-minute session boundary — verified, appendix A.2.
- The "Mistral-7B beats GPT-3.5 on pure time queries" claim — verified (93.95 vs 90.47 recall on time queries).
- Table 5 finding (context-enriched CoTable prompt does not beat original prompt with rewritten query) — verified, appendix A.5.
- Ablation: removing meta-semantic classifier drops Mistral average recall to 18.82 — verified, Table 3. (Digest says "from 79.6 to 18.8" — Table 3 shows 79.62 → 18.82, exact.)
- Zyphra TemporalMemoryDataset GitHub release referenced — verified, footnote 1 of paper.

No claims invented. No fields added that the paper doesn't address. Severity: **Clean**.
