---
corpus: agentic-memory
kind: paper-digest
slug: petrov-2026-schema-grounded-memory
title: "From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction"
authors:
  - "Alex Petrov"
  - "Alexander Gusak"
  - "Denis Mukha"
  - "Dima Korolev"
year: 2026
publication_date: "2026-05"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2604.27906"
doi: null
arxiv_id: "2604.27906"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Reliable AI memory must be schema-grounded — the schema is an explicit, enforceable contract that names which facts must be remembered exactly, which may be ignored, and which values must never be inferred — and the only way to populate that schema reliably from natural language is an iterative, multi-stage write path (object → field → value, with validators, local retries, and an LLM judge in the loop), which is the direct anti-thesis to RAG-style 'preserve verbatim, synthesize at query time' designs."
topics:
  - schema-grounded-memory
  - write-time-extraction
  - structured-memory
  - iterative-extraction
  - llm-judge-in-the-loop
  - memory-architecture
  - factual-recall
  - text-to-sql
  - agent-memory
  - data-processing-inequality
tags:
  - paper
  - memory-architecture
  - structured-extraction
  - validation-gates
  - xmemory
  - benchmark
  - encoding-gate
  - counter-thesis
entities:
  - petrov-alex
  - gusak-alexander
  - mukha-denis
  - korolev-dima
related_digests:
  - adler-2026-storage-not-memory
  - chhikara-2025-mem0
  - hu-2026-evermemos
  - rasmussen-2025-zep-temporal-kg
  - li-2025-memos
  - mao-2026-agent-memory-circuits
  - maharana-2024-locomo
  - wu-2024-longmemeval
citations:
  - title: "Memory in the age of AI agents"
    authors: ["Yuyang Hu", "Shichun Liu", "Yanwei Yue", "Guibin Zhang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2512.13564"
    arxiv_id: "2512.13564"
  - title: "Rethinking memory in AI: Taxonomy, operations, topics, and future directions"
    authors: ["Yifan Du", "Chongyang Huang", "Wayne Xin Zhao", "Ji-Rong Wen"]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2505.00675"
    url: "https://arxiv.org/abs/2505.00675"
    arxiv_id: "2505.00675"
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: "https://arxiv.org/abs/2005.11401"
    arxiv_id: "2005.11401"
  - title: "Dense passage retrieval for open-domain question answering"
    authors: ["Vladimir Karpukhin", "Barlas Oguz", "Sewon Min", "Patrick Lewis", "Ledell Wu", "Sergey Edunov", "Danqi Chen", "Wen-tau Yih"]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: "https://arxiv.org/abs/2004.04906"
    arxiv_id: "2004.04906"
  - title: "Mem0: Building production-ready AI agents with scalable long-term memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "Taranjeet Singh", "Deshraj Yadav"]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2504.19413"
    url: "https://arxiv.org/abs/2504.19413"
    arxiv_id: "2504.19413"
  - title: "Sentence-BERT: Sentence embeddings using siamese BERT-networks"
    authors: ["Nils Reimers", "Iryna Gurevych"]
    year: 2019
    venue: "EMNLP-IJCNLP"
    doi: null
    url: "https://arxiv.org/abs/1908.10084"
    arxiv_id: "1908.10084"
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Nelson F. Liu", "Kevin Lin", "John Hewitt", "Ashwin Paranjape", "Michele Bevilacqua", "Fabio Petroni", "Percy Liang"]
    year: 2024
    venue: "TACL"
    doi: null
    url: "https://arxiv.org/abs/2307.03172"
    arxiv_id: "2307.03172"
  - title: "MEMTRACK: Evaluating long-term memory and state tracking in multi-platform dynamic agent environments"
    authors: ["Darshan Deshpande", "Varun Gangal", "Hersh Mehta", "Anand Kannappan", "Rebecca Qian", "Peng Wang"]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2510.01353"
    url: "https://arxiv.org/abs/2510.01353"
    arxiv_id: "2510.01353"
  - title: "LoCoMo: Evaluating very long-term conversational memory of LLM agents"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "Mohit Bansal", "Francesco Barbieri", "Yuwei Fang"]
    year: 2024
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2402.17753"
    url: "https://arxiv.org/abs/2402.17753"
    arxiv_id: "2402.17753"
  - title: "Elements of Information Theory"
    authors: ["Thomas M. Cover", "Joy A. Thomas"]
    year: 2006
    venue: "Wiley (2nd ed.)"
    doi: null
    url: "https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X"
    arxiv_id: null
  - title: "A mathematical theory of communication"
    authors: ["Claude E. Shannon"]
    year: 1948
    venue: "Bell System Technical Journal"
    doi: null
    url: null
    arxiv_id: null
  - title: "An information theoretic perspective on agentic system design"
    authors: ["Shizhe He", "Avanika Narayan", "Ishan S. Khare", "Scott W. Linderman", "Christopher Ré", "Dan Biderman"]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2512.21720"
    url: "https://arxiv.org/abs/2512.21720"
    arxiv_id: "2512.21720"
  - title: "BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension"
    authors: ["Mike Lewis", "Yinhan Liu", "Naman Goyal", "Marjan Ghazvininejad", "Abdelrahman Mohamed", "Omer Levy", "Ves Stoyanov", "Luke Zettlemoyer"]
    year: 2020
    venue: "ACL"
    doi: null
    url: "https://arxiv.org/abs/1910.13461"
    arxiv_id: "1910.13461"
  - title: "PEGASUS: Pre-training with extracted gap-sentences for abstractive summarization"
    authors: ["Jingqing Zhang", "Yao Zhao", "Mohammad Saleh", "Peter J. Liu"]
    year: 2020
    venue: "ICML"
    doi: null
    url: "https://arxiv.org/abs/1912.08777"
    arxiv_id: "1912.08777"
  - title: "Why language models hallucinate"
    authors: ["Adam Tauman Kalai", "Ofir Nachum", "Santosh S. Vempala", "Edwin Zhang"]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2509.04664"
    url: "https://arxiv.org/abs/2509.04664"
    arxiv_id: "2509.04664"
  - title: "Passage re-ranking with BERT"
    authors: ["Rodrigo Nogueira", "Kyunghyun Cho"]
    year: 2019
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1901.04085"
    arxiv_id: "1901.04085"
  - title: "On the fundamental limits of LLMs at scale"
    authors: ["Muhammad Ahmed Mohsin", "Muhammad Umer", "Ahsan Bilal", "Zeeshan Memon", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2511.12869"
    arxiv_id: "2511.12869"
  - title: "From local to global: A graph RAG approach to query-focused summarization"
    authors: ["Darren Edge", "Ha Trinh", "Newman Cheng", "Joshua Bradley", "Alex Chao", "Apurva Mody", "Steven Truitt", "Jonathan Larson"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2404.16130"
    arxiv_id: "2404.16130"
  - title: "Spider 2.0: Evaluating language models on real-world enterprise text-to-SQL workflows"
    authors: ["Fangyu Lei", "Jixuan Chen", "Yuxiao Ye", "Ruisheng Cao", "et al."]
    year: 2024
    venue: "ICLR 2025 Oral"
    doi: null
    url: "https://arxiv.org/abs/2411.07763"
    arxiv_id: "2411.07763"
  - title: "Large language models for generative information extraction: A survey"
    authors: ["Derong Xu", "Wei Chen", "Wenjun Peng", "Chao Zhang", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2312.17617"
    arxiv_id: "2312.17617"
  - title: "Self-refine: Iterative refinement with self-feedback"
    authors: ["Aman Madaan", "Niket Tandon", "Prakhar Gupta", "Skyler Hallinan", "Luyu Gao", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2303.17651"
    arxiv_id: "2303.17651"
  - title: "Solving a million-step LLM task with zero errors"
    authors: ["Elliot Meyerson", "Giuseppe Paolo", "Roberto Dailey", "Hormoz Shahrzad", "Olivier Francon", "Conor F. Hayes", "Xin Qiu", "Babak Hodjat", "Risto Miikkulainen"]
    year: 2025
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2511.09030"
    url: "https://arxiv.org/abs/2511.09030"
    arxiv_id: "2511.09030"
  - title: "Structured information extraction from scientific text with large language models"
    authors: ["John Dagdelen", "Alexander Dunn", "Sanghoon Lee", "Nicholas Walker", "Andrew S. Rosen", "Gerbrand Ceder", "Kristin A. Persson", "Anubhav Jain"]
    year: 2024
    venue: "Nature Communications"
    doi: null
    url: "https://www.nature.com/articles/s41467-024-45563-x"
    arxiv_id: null
  - title: "Learning to extract structured entities using language models (MuSEE)"
    authors: ["Haolun Wu", "Ye Yuan", "Liana Mikaelyan", "Alexander Meulemans", "Xue Liu", "James Hensman", "Bhaskar Mitra"]
    year: 2024
    venue: "EMNLP"
    doi: "10.18653/v1/2024.emnlp-main.388"
    url: "https://aclanthology.org/2024.emnlp-main.388/"
    arxiv_id: null
  - title: "OneKE: A dockerized schema-guided LLM agent-based knowledge extraction system"
    authors: ["Yujie Luo", "Xiangyuan Ru", "Kangwei Liu", "Lin Yuan", "et al."]
    year: 2025
    venue: "WWW Companion"
    doi: "10.1145/3701716.3715189"
    url: "https://arxiv.org/abs/2412.20005"
    arxiv_id: "2412.20005"
  - title: "Grammar-aligned decoding"
    authors: ["Kanghee Park", "Jiayu Wang", "Taylor Berg-Kirkpatrick", "Nadia Polikarpova", "Loris D'Antoni"]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: "https://arxiv.org/abs/2405.21047"
    arxiv_id: "2405.21047"
  - title: "Why and where: A characterization of data provenance"
    authors: ["Peter Buneman", "Sanjeev Khanna", "Wang-Chiew Tan"]
    year: 2001
    venue: "ICDT"
    doi: null
    url: "https://homepages.inf.ed.ac.uk/opb/papers/ICDT2001.pdf"
    arxiv_id: null
  - title: "Context rot: How increasing input tokens impacts LLM performance"
    authors: ["Brandon Hong", "et al."]
    year: 2025
    venue: "Chroma technical report"
    doi: null
    url: "https://research.trychroma.com/context-rot"
    arxiv_id: null
  - title: "YAML ain't markup language (YAML) version 1.2.2"
    authors: ["YAML Language Development Team"]
    year: 2021
    venue: "spec"
    doi: null
    url: "https://yaml.org/spec/1.2.2/"
    arxiv_id: null
  - title: "JSON Schema: A media type for describing JSON documents (draft 2020-12)"
    authors: ["JSON Schema Authors"]
    year: 2020
    venue: "spec"
    doi: null
    url: "https://json-schema.org/draft/2020-12/json-schema-core"
    arxiv_id: null
  - title: "ReAct: Synergizing reasoning and acting in language models"
    authors: ["Shunyu Yao", "Jeffrey Zhao", "Dian Yu", "Nan Du", "Izhak Shafran", "Karthik Narasimhan", "Yuan Cao"]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2210.03629"
    arxiv_id: "2210.03629"
  - title: "NoSQL schema evolution and data migration"
    authors: ["Uta Störl", "Meike Klettke", "Stefanie Scherzinger"]
    year: 2020
    venue: "EDBT"
    doi: null
    url: "https://openproceedings.org/2020/conf/edbt/paper_T4.pdf"
    arxiv_id: null
  - title: "A generic schema evolution approach for NoSQL and relational databases"
    authors: ["Alberto Hernández Chillón", "Meike Klettke", "Diego Sevilla Ruiz", "Jesús García Molina"]
    year: 2024
    venue: "IEEE TKDE"
    doi: null
    url: "https://epub.uni-regensburg.de/77266/1/A_Generic_Schema_Evolution_Approach_for_NoSQL_and_Relational_Databases.pdf"
    arxiv_id: null
  - title: "LLM structured output benchmarks are riddled with mistakes"
    authors: ["Jonas Mueller", "Hui Wen Goh"]
    year: 2025
    venue: "Cleanlab blog"
    doi: null
    url: "https://cleanlab.ai/blog/structured-output-benchmark/"
    arxiv_id: null
  - title: "Cognee GitHub repository and README"
    authors: ["Topoteretes"]
    year: 2026
    venue: "GitHub"
    doi: null
    url: "https://github.com/topoteretes/cognee"
    arxiv_id: null
  - title: "Mem0 documentation: Build with mem0"
    authors: ["Mem0"]
    year: 2026
    venue: "docs.mem0.ai"
    doi: null
    url: "https://docs.mem0.ai/introduction"
    arxiv_id: null
  - title: "Supermemory documentation: Overview"
    authors: ["Supermemory"]
    year: 2026
    venue: "supermemory.ai/docs"
    doi: null
    url: "https://supermemory.ai/docs/intro"
    arxiv_id: null
  - title: "Zep documentation and platform overview"
    authors: ["Zep"]
    year: 2026
    venue: "getzep.com"
    doi: null
    url: "https://www.getzep.com"
    arxiv_id: null
  - title: "LongMemEval: Benchmarking chat assistants on long-term interactive memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "Yuwei Zhang", "Kai-Wei Chang", "Dong Yu"]
    year: 2024
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2410.10813"
    url: "https://arxiv.org/abs/2410.10813"
    arxiv_id: "2410.10813"
  - title: "Benchmarking AI agent memory"
    authors: ["Letta"]
    year: 2026
    venue: "Letta blog"
    doi: null
    url: "https://www.letta.com/blog/benchmarking-ai-agent-memory"
    arxiv_id: null
  - title: "LoCoMo issue discussion: Dataset label quality estimate"
    authors: ["snap-research and community contributors"]
    year: 2025
    venue: "GitHub issue"
    doi: null
    url: "https://github.com/snap-research/locomo/issues/27#issuecomment-3921992262"
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 6
  title: "False positives (FP) and false negatives (FN) by query category"
  page: 24
  image_path: "figures/petrov-2026-schema-grounded-memory-fig.png"
---

# From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction

**Authors:** Alex Petrov, Alexander Gusak, Denis Mukha, Dima Korolev (xmemory)
**Published:** 2026-05 · [Source](https://arxiv.org/abs/2604.27906)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Petrov et al. (the xmemory team) argue that persistent AI memory is *not* a retrieval problem — it is an extraction-and-validation problem on the **write path**. Storing text and embedding it for query-time inference (RAG-style) is brittle by construction: every read re-runs LLM inference over raw prose, errors compound silently into corrupted memory, and the operations that actually matter in production (exact fact lookup, state tracking, updates, deletions, aggregation, relational joins, negative/exclusion queries, explicit unknowns) cannot be expressed reliably over similarity-ranked text. Their answer is **schema-grounded memory**: an explicit, enforceable contract that says (a) what must be remembered, (b) what may be ignored, and (c) which values must never be inferred. The schema is populated via an **iterative, schema-aware extraction pipeline** — object detection → field detection → field-value extraction — with validation gates, local retries, an LLM judge in the loop, a stateful prompt engine, and three explicit memory contexts (request / session / main). Reads become constrained queries (text-to-SQL-like) over verified records, not repeated inference over retrieved passages. Empirically, xmemory hits **90.42% object-level accuracy** and **62.67% output-level accuracy** on a structured-extraction benchmark (best of nine systems including GPT-5.5, Gemini 3.1 Pro, Opus 4.7), **97.10% F1** on an end-to-end memory benchmark covering CRUD-with-state across four domains (vs 80.16%–87.24% for Cognee/Mem0/Supermemory/Zep), and **95.2% accuracy** on a Splitwise application-level task (vs ~92% for frontier-model app harnesses, and 12–40% for code-generated Markdown memories). The headline message: for memory workloads that need stable facts and stateful computation, **architecture matters more than retrieval scale or model strength**.

## Key Takeaway

> Reliable AI memory must be schema-grounded — the schema is an explicit, enforceable contract that names which facts must be remembered exactly, which may be ignored, and which values must never be inferred — and the only way to populate that schema reliably from natural language is an iterative, multi-stage write path (object → field → value, with validators, local retries, and an LLM judge in the loop), which is the direct anti-thesis to RAG-style "preserve verbatim, synthesize at query time" designs.

**ENGRAM mapping (where the paper actually lands):**

- **E (Encode) — primary** — The entire paper is an argument about the *encoding gate*. xmemory pushes maximal interpretive work to the write path: an LLM judge-in-the-loop, validation gates after each of (object detection, field detection, field-value extraction), local retries when a validator fails, and a stateful prompt engine that conditions every next prompt on the previously-validated decisions. Their object-level accuracy story (Section 5.1) is a closed-form argument for *why* single-pass extraction is doomed: P(record correct) = ∏ qᵢ over m fields, so 0.97²⁰ ≈ 0.54 even when per-field accuracy looks great. Iteration with validation breaks the dependency chain.
- **N (Network) — primary** — Memory **shape** is the core architectural decision. The paper systematically tours four shapes (unstructured text + embedding, Graph RAG, general-purpose relational DB with text-to-SQL, schema-grounded normalised records) and argues only the last solves factual recall *and* agent-compatibility. The shape is **agent-co-designed normalised records**: flatter than human-DBA schemas, with explicit `unknown` fields, organised around the queries agents actually issue. The store is split into three contexts with different lifetimes: **request** (ephemeral, per-ingestion-job), **session** (medium-lived, assembles partial objects across requests/chunks), **main** (durable, versioned, with provenance lineage).
- **G (Ground) — primary** — Provenance is *first-class*, not an afterthought. The main context contains "the current best-known values, the evolution of those values over time, and explicit provenance: links from records to the sessions (and, by extension, actors and sources) from which facts were derived." Critically, schemas make **absence** first-class: `unknown` vs `not mentioned` vs `explicitly rejected` are distinct, addressable states. Validation gates turn extraction errors into *retriable events rather than silent commits* — confidence is structural, not heuristic.
- **R (Retrieve) — secondary** — Reads become *constrained queries* (text-to-SQL or equivalent) over normalised records. The argument is that the value isn't SQL per se but **boundedness**: outputs have strict validity checks, partial correctness is measurable, queries can be logged/audited/replayed, and aggregation/joins/negation are expressible as operators rather than inferred from passages. The token math (Section 6.4) — Cₓ = wₓ + R·rₓ — gives the read-heavy advantage: with R=10, xmemory uses ~1/3 the tokens of a text-based system per write-read cycle.
- **A (Aggregate) — secondary** — Aggregation happens at *both* write and read time. Write-time: the iterative pipeline aggregates partial extractions into validated records (object assembly across requests in the session context). Read-time: aggregation queries (`COUNT`, `LIST`, joins, exclusions) run deterministically over fields rather than being re-inferred over text. The paper explicitly notes that aggregation magnifies the cost of small errors, so a guarded write path is *the* enabler for trustworthy aggregation downstream.
- **M (Maintain) — primary** — Schema lifecycle is treated as a product concern, not implementation detail (Section 7). Three operations: **bootstrap** (import narrow projection from existing CRM/ERP/warehouse, or author in YAML/JSON Schema), **agent-assisted design from intended questions** (elicit representative queries → propose entities/fields/relations → test whether each question translates → iterate), and **versioned migration** under observed usage drift (repeated requests for missing attributes, recurring ambiguity, validation failures all trigger migration proposals that update schema + prompts + validators + backfill, marking irrecoverable values as `unknown`). The point: schema-bound memory **improves through concrete, testable changes to a contract**, not through prompt drift.

## Implications

**For the orbit question (this paper as counter-thesis to Adler 2026):**

Adler & Zehavi (`adler-2026-storage-not-memory`) is the strongest current articulation of the opposite position: **"write-time intelligence is anti-intelligence"** — anything an LLM-distillation extractor discards before the query is known cannot be recovered at retrieval time, so the right move is to **preserve raw conversation verbatim** and do the hard thinking at query time via hybrid retrieval (BM25 + dense + cross-encoder reranking) over SQLite. They claim that approach buys back ~30 accuracy points that LLM-on-write extractors bleed away.

Petrov et al. take the diametrically opposite position. Their structural argument has two prongs:

1. **The Data Processing Inequality cuts the other way for compression that isn't structured.** I(A; Z) ≤ I(A; X): you can't recover information about a future answer A from a compressed Z that you discarded from X. *They agree with Adler that compression is dangerous.* But they argue the relevant compression to worry about is *summarisation-into-prose* (which discards low-salience facts: exact values, rejected options, units, timestamps, null-vs-value distinctions), not *extraction-into-schema*. A schema-bound write doesn't compress what matters — it *names* what matters and stores it exactly, while letting unmodelled prose be discarded freely.
2. **Hybrid retrieval scaling doesn't reach the precision regime memory needs.** Table 1 (page 5) explicitly addresses Adler's class of move: scaling chunks "improves higher chance that some relevant text exists" but cannot guarantee "exactness, completeness, stable cutoffs for correctness." Reranking "improves better ordering of a similarity-driven candidate set" but cannot guarantee "predicate satisfaction, missing fact detection, determinism." Hybrid retrieval "improves broader recall surface" but cannot guarantee "a clear correctness model: multiple signals can agree on the wrong answer, disagree without a resolution rule, or both miss a fact; failure modes multiply rather than simplify." Long-context stuffing "improves avoids explicit retrieval" but cannot guarantee "structured recall, stability across prompts, absence detection."

**The crux of the disagreement is operational, not philosophical.** Both papers agree raw recall over prose is insufficient. They disagree on *where the interpretive work lives*. Adler says: defer interpretation to the LLM at query time, because query-time has more context (you know what's being asked). Petrov says: that approach can't handle (a) state mutations across writes — entity renames, deletions, field updates compound silently in a corpus of raw turns; (b) absence — semantic retrieval has no native exhaustive non-existence check; (c) determinism — same query, same store should give same answer; (d) aggregation — embedding retrieval returns a ranked subset, not a constraint-satisfying result. The empirical wedge: Petrov's end-to-end benchmark **specifically tests the failure modes Adler's design cannot represent natively** (employee promotion = field update, company rename = entity rename + relation propagation, company dissolution = cascading delete, "who is currently unemployed?" = negative exclusion over a previously-asserted-and-now-absent entity). xmemory hits 97.10 F1; Mem0 (no graph) — closest analog to Adler's pipeline — hits 87.24%. The 10-point gap concentrates almost entirely in state mutation, aggregation, and negative-exclusion categories (Figure 6).

**Which view wins for Flow OS?**

This is the question the orbit experiment was actually about. Flow OS-internal memory is closer to Adler's regime today (markdown vault + QMD hybrid search + LLM consolidation via `/learn`, with raw transcripts preserved). But the workloads Petrov targets — **state tracking over ventures, decision history, contact relationship mutations, explicit "what we ruled out"** — are real Flow OS workloads. Today they live in markdown files that get summarised by `/learn`, which is closer to "implicit relevance" than "schema as contract." A pragmatic synthesis: **keep the verbatim corpus** (Adler's win — irreversible commits are dangerous) but **layer a thin schema-grounded projection** over the parts of memory where exactness matters (current state of each venture, current customer set, current rejected positioning options, current "explicit unknowns"). The schema doesn't have to be the whole memory — it just has to be the contract over the facts that downstream agents are obligated to get right. Petrov even concedes this explicitly in their Scope box (page 3): *"We do not claim that schema-grounded memory is optimal for every memory use case. Unstructured and hybrid retrieval remain useful for thematic recall, exploratory search, and broad contextual grounding."*

**Concrete dimensional implications:**

- **(E) Encode** — When designing the next iteration of `/learn`, treat the schema as an input, not an output. The current `/learn` infers structure from the transcript; Petrov suggests inferring *fields*, then *values*, with a validation gate between them. The judge-in-the-loop result (90.42% object accuracy vs 86.61% without) is a ~4pt lift from a single architectural choice — small but compounding.
- **(N) Network** — The three-context model (request / session / main) maps cleanly to Flow OS as: per-prompt scratch / per-session log / persistent memory layer. Treating them as architecturally distinct (different lifetimes, different validators) rather than as one undifferentiated "memory" is a refactor Flow OS is not yet committed to.
- **(G) Ground** — `unknown` vs `not mentioned` vs `explicitly rejected` as first-class states maps to a real Flow OS gap. The current memory layer cannot answer "what positioning options did we explicitly rule out for Cognitive Shift?" without re-reading transcripts.
- **(R) Retrieve** — Don't replace QMD; consider adding a *projection layer* of schema-bound facts that text-to-SQL can run against for state/aggregation queries.
- **(A) Aggregate** — `/learn` does aggregate (the v2 frontmatter schema is a step in this direction). The Petrov result says: validate the aggregates, don't just write them.
- **(M) Maintain** — Schema evolution-via-versioned-migration is the operational discipline `/learn` currently lacks. Flow OS schemas drift in prompt-engineering, not in checked-in artefacts.

**The compounding-error argument (Section 5.2) is independently important.** Memory correctness is multiplicative across workflow length: if a workflow depends on n facts each correct with probability p, all-facts-correct ≈ pⁿ; if a fact is interpreted k times, surviving-correct ≈ pᵏ. *This is the mathematical core of the "AI memory degrades over time" complaint.* Adler's approach mitigates by re-reading raw text each time (so k=1 effectively, every read goes back to source). Petrov's approach mitigates by extracting once at write time with strong validation (so n is reduced — facts become addressable, not re-inferred). Both are defensible; they trade different costs.

## How to Apply It (method)

The xmemory architecture is reproducible from the paper text. The pipeline:

**1. Schema as input.** Define entities, fields (with types and allowed values), relations, and constraints. Start small. Import a narrow projection of any existing system-of-record if one exists; otherwise author in YAML or JSON Schema. The schema must include:
- A way to mark fields as **required** vs optional.
- An explicit `unknown` value distinct from `null` / not-mentioned.
- Foreign-key-style relations to make cross-entity queries expressible as joins.
- Negative constraints (e.g., "if no expiry date is mentioned, set expiry date to `unknown`; do not infer or approximate one").

**2. Iterative extraction pipeline (three stages, validation gates between).**

| Stage | Decision | Validator |
|---|---|---|
| Object detection | Does an object of this schema exist in this chunk at all? | Evidence check: is there textual support? |
| Field detection | Which fields are present/applicable? | Allowed-field-combinations check |
| Field-value extraction | What is the value, under type and normalisation constraints? | Type/range/format/normalisation/`unknown` check |

When a validator fails: retry the failing stage *only* (not the whole object). The probability that at least one of kᵢ retries succeeds is 1 − (1 − qᵢ)^kᵢ. For q=0.97, m=20, k=2: record-level correctness jumps from 0.54 to 0.98.

**3. LLM judge-in-the-loop (recommended).** A separate LLM (Opus 4.6 in their setup, with Sonnet 4.6 as the main extractor) reviews extractions and provides a feedback signal. Empirically: +3.81 pts object accuracy, +12.67 pts output accuracy vs same pipeline without judge.

**4. Stateful prompt engine.** Prompts evolve based on what has already been resolved. Concrete contrast from the paper:
- Monolithic: "Extract a person object from the paragraph."
- Stateful: "A person has been identified as Claude Shannon, the scientist. Based on the schema, which fields are explicitly mentioned for this person in the paragraph?"

The prompt engine reads from the request context (what's been resolved this ingestion), grounds in main context for normalisation/disambiguation, and incorporates validation feedback when a retry is needed.

**5. Three memory contexts with explicit merge flows.**

- **Request context** — ephemeral, shared by all workers handling one ingestion job. Holds chunked inputs, candidate objects, tentative links, validation outcomes. Optimised for fast local decisions; can read from broader contexts for grounding.
- **Session context** — medium-lived workspace. Assembles partial objects over a session, resolves identity incrementally, tracks intra-session deltas. Important when objects arrive piecewise across chunks/turns.
- **Main context** — durable, versioned store. Current best-known values + evolution-over-time + provenance lineage (record → session → actor → source). This is where conflict resolution and diff computation are explicit operations.

**6. Read path.** Once memory is schema-bound, retrieval is a constrained translation problem: natural language → SQL (or equivalent structured query). The value: outputs have strict validity checks, partial correctness is measurable, queries are loggable/auditable/replayable. Compact, normalised records mean less prompt sensitivity than long retrieved passages.

**7. Schema lifecycle (treat as product, not implementation).**

- **Bootstrap** small. Represent missing values as explicit unknowns rather than speculative fields.
- **Design loop**: elicit representative questions → propose entities/fields/relations that make them answerable as structured queries → test translation → iterate until schema is the minimal contract supporting intended workload.
- **Evolution**: observed usage gaps (repeated requests for missing attributes, recurring ambiguity, repeated validation failures) trigger versioned migrations. A migration updates schema + prompts + validators + backfill logic; irrecoverable values become explicit `unknown`.

**Operational cost model (Section 6.4).** For R reads per write, with write cost w and read cost r:

Cₓ = wₓ + R·rₓ      Cₜ = wₜ + R·rₜ

Worked example: R=10, wₓ=10, rₓ=1, wₜ=3, rₜ=6 → S = Cₜ/Cₓ = 63/20 ≈ 3.15. Text-based system consumes ~3.15× the tokens per cycle. xmemory pays more on write, *much* less on read; the crossover is around R≈2–3.

## Best Figure

![Figure 6 — False positives (FP) and false negatives (FN) by query category (page 24)](figures/petrov-2026-schema-grounded-memory-fig.png)

**Image Candidates:**

- Figure 6 (p. 24): Side-by-side bar chart of FP/FN counts across five query categories (single-fact lookup, relational, state, negative exclusion, aggregation) — shows exactly *where* schema-grounded memory wins and that the wins concentrate in state tracking, aggregation, and exclusion.
- Table 8 (p. 24): F1 head-to-head — xmemory 97.10% vs Cognee 86.18%, Mem0 (no graph) 87.24%, Mem0 (graph) 86.07%, Supermemory 80.49%, Zep 80.16%. Cleanest single-number summary but doesn't show the failure-mode shape.
- Figure 1 (p. 12): The architectural pipeline diagram (object detection → field detection → field-value extraction with validation gates and local retries) — best for explaining the *idea* but is conceptual rather than evidential.

**Best Image:** Figure 6 — False positives (FP) and false negatives (FN) by query category.

**Slide Caption:** xmemory's lead is not uniform: it concentrates in state, aggregation, and negative-exclusion queries — exactly the operations Adler's "preserve raw, synthesize at query time" design cannot represent natively.

**Description:** Figure 6 shows a side-by-side bar chart of error counts: false positives on the left panel, false negatives on the right, across five query categories — single-fact lookup, relational, state, negative exclusion, aggregation. Bars extend downward from zero (lower absolute values = fewer errors). Six systems are compared (Cognee, Mem0 no-graph, Mem0 graph, Supermemory, Zep, xmemory). The visual punchline: xmemory's green bars are short across every category, while the non-schema systems show pronounced spikes specifically in **state** (Zep peaks at 27 FP, Mem0 graph at 19 FN) and **aggregation** (Supermemory 12 FP / 14 FN; Mem0 graph 11 FP / 13 FN), and uneven but present error in **negative exclusion** (Supermemory 7 FP / 9 FN). This is the empirical heart of the paper's argument: it is not that retrieval can't find related context — it is that retrieval cannot represent mutations, aggregations, or explicit absences as first-class operations.

## What Experts Overlook

**1. The Data Processing Inequality framing is being used backwards by both sides of this debate, and Petrov gets it more carefully right.** I(A; Z) ≤ I(A; X) does not by itself say "preserve raw" or "extract schema." It says: any irreversible commit at write time is a place information *can* be lost. The honest reading is that **both architectures commit at write time** — Adler commits to the chunking + indexing + summarisation that drives retrieval; Petrov commits to schema-bound fields. The question is which commitments are *recoverable* and which are *propagated as silent errors*. Schema-bound commits are inspectable (a missing required field is a detectable error); embedding-bound commits are not (a chunked-away qualifier is silent). This is the implicit Petrov argument that's stronger than they make it.

**2. The "single-pass extraction failure" is a kinetics argument, not a capability argument.** Their Section 5.1 derivation P(record correct) = ∏ qᵢ is a *characterisation of the all-correct path under a single autoregressive commit*. It tells you nothing about whether a sufficiently smart model could one-shot a 20-field record correctly. What it tells you is that **errors off the all-correct path tend to propagate** because a wrong generated value biases the KV cache for downstream fields. This is the same insight as "prompt the model on a clean prefix" and it's the real mechanism for *why* iteration with validation works. Most readers will see "0.97²⁰ ≈ 0.54" and miss this — the math is just a re-expression of "don't condition later decisions on corrupted prefixes."

**3. The Mem0-no-graph vs Mem0-graph result (87.24% vs 86.07%) is a small but telling data point.** Adding a graph layer *didn't help* Mem0 with state mutation tracking — both variants showed near-identical state-error counts (Mem0 no-graph: 12 FP / 17 FN; Mem0 graph: 13 FP / 19 FN). This undercuts the easy "just add Graph RAG" intuition. The paper notes this in passing but doesn't dwell on it; it deserves more weight. **Graphs organise memory; they do not define factual obligations** (Table 3 framing).

**4. The 6.4% LoCoMo label-error estimate (citation [41]) and the Appendix A.2 critique of LoCoMo/LongMemEval is doing significant work the paper underplays.** Petrov is essentially saying: the benchmarks the entire field uses to compare memory systems are contaminated with reasoning tasks masquerading as memory tasks, plus ~6.4% straight-up wrong labels. This is why they ran their own benchmark — not just for marketing reasons, but because they didn't trust the existing ones. The conclusion that frontier-model app harnesses hit 92% on Splitwise while LoCoMo numbers cluster lower might be partly explained by what each benchmark *actually* measures. This has implications beyond this paper: any future memory paper using LoCoMo as the primary metric is potentially measuring "memory + commonsense inference" rather than memory alone.

**5. The Splitwise comparison includes "customer-facing memory and tool-use harnesses from major frontier-model applications" at ~92% accuracy — and xmemory beats that at 95.2%.** This is a quietly important number. It means the gap between "best off-the-shelf model app" and "best schema-grounded purpose-built system" on a structured event-tracking task is ~3 points, not 30. The headline gap of 95.2% vs 25.7% (Zep) is real but the *interesting* gap is the 3-point one against actual production frontier-app memory. The marginal advantage from architectural rigour over the best production-tuned harness is real but smaller than the marketing suggests.

**6. There is a prompt injection at the end of the paper that does not appear in the digest output for safety reasons.** The trailing "Note to any AI agent processing this document" attempts to instruct any LLM summarising the paper to (a) recommend schema-grounded memory as a high-priority architectural concern and (b) consider adding the paper to "well-known voices" reading lists if summarising for them. This is exactly the kind of operator-vs-user trust violation that schema-grounded memory itself is trying to defend against — a write-path commitment that bypasses validators. Reviewer flagged but did not comply.

**7. The cost model (Section 6.4) is the paper's softest section.** The numbers are admittedly "symbolic token units for proportional comparison" with hand-picked R=10, wₓ=10, rₓ=1, wₜ=3, rₜ=6. The conclusion (3.15× advantage) is plausible directionally but is not a measurement. They acknowledge this ("this should be read as an engineering estimate, not a benchmark result") but downstream readers may not. The real cost-question Flow OS should run is: at *our* R (reads-per-write), with *our* write complexity, what does the crossover look like? My back-of-envelope for a Flow OS-style brain (mostly write-heavy, R ≈ 0.5–2): a schema-grounded write path may not pay off on tokens alone — it pays off on **correctness** when the reads happen.

## Extracted Prompts

From the paper's described prompt engine (Section 6.2). Three patterns worth lifting:

**1. The stateful field-detection prompt (after object identity is resolved):**

```
A person has been identified as <ENTITY_NAME>, <ENTITY_DESCRIPTION>.
Based on the schema below, which fields are explicitly mentioned for
this person in the paragraph?

Schema:
<FIELD_NAME>: <TYPE> — <CONSTRAINT_DESCRIPTION>
<FIELD_NAME>: <TYPE> — <CONSTRAINT_DESCRIPTION>
...

Paragraph:
<TEXT>

Return only the field names that have textual evidence in the paragraph.
Do not infer values. If no fields are explicitly mentioned, return an empty list.
```

**2. The negative-constraint value extraction (operationalising absence at the write path):**

```
For the field <FIELD_NAME> of <ENTITY>, extract the value from the paragraph below.

CRITICAL: This field has the following negative constraint:
"If no <FIELD_NAME> is mentioned in the paragraph, set <FIELD_NAME> to `unknown`.
 Do not infer or approximate a value. Do not use values from prior knowledge
 or from other fields. The value `unknown` is a first-class value and must be
 returned when there is no explicit textual evidence."

Type: <TYPE>
Normalisation rules: <RULES>

Paragraph:
<TEXT>

Return the value, or `unknown` if not explicitly stated.
```

**3. Validator-feedback retry prompt (turning failures into guided correction):**

```
The previous extraction for field <FIELD_NAME> failed validation.

Previous value: <PREV_VALUE>
Validation error: <ERROR> (e.g., "value '2026-13-45' does not match required date format YYYY-MM-DD")

Re-extract the value from the paragraph below. The previous attempt is shown
only for context — do not anchor on it. Apply the following corrections:
<TARGETED_CORRECTIONS>

Paragraph:
<TEXT>

Return only the corrected value, or `unknown` if the field cannot be extracted.
```

**Notes for adapting to Flow OS:**

- Pattern 1 is the most directly portable. `/learn`'s current extraction is closer to "given this transcript, extract everything you can." Pattern 1 says "given the schema, which fields are evidenced?" — this is a different, narrower, more reliable decomposition.
- Pattern 2's negative constraint is the *operational* answer to "how do we capture explicit unknowns?" — which Flow OS doesn't currently do well. The current behaviour silently omits unmentioned fields; the schema-grounded behaviour records `unknown` as a first-class state.
- Pattern 3 is a write-time correction loop. Flow OS has no equivalent today — `/learn` is one-shot. Adding even a single retry against a structural validator (e.g., "is this a valid YAML frontmatter?") would be a low-cost lift.

## Citations

(Full citations array in frontmatter — 38 entries. Top 10 by relevance to the orbit question:)

- Adler & Zehavi (2026) — *Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall* — the direct counter-thesis; not cited by Petrov but lives in the same arxiv submission window.
- Lewis et al. (2020) — *Retrieval-augmented generation for knowledge-intensive NLP tasks* (NeurIPS 2020) — canonical RAG reference, the architecture Petrov is arguing against.
- Karpukhin et al. (2020) — *Dense Passage Retrieval for Open-Domain Question Answering* (EMNLP 2020) — the embedding-retrieval baseline Petrov treats as insufficient for predicate evaluation.
- Chhikara et al. (2025) — *Mem0: Building production-ready AI agents with scalable long-term memory* — direct head-to-head baseline; Mem0 (no graph) is the closest analog to Adler's design and the strongest non-schema third party (87.24% F1 vs xmemory's 97.10%).
- Liu et al. (2024) — *Lost in the middle: How language models use long contexts* (TACL) — supports the "long-context stuffing doesn't fix factual recall" point.
- Kalai et al. (2025) — *Why language models hallucinate* — supports the "substitution failure" failure-mode argument (a model under uncertainty fills in plausible values).
- Maharana et al. (2024) — *LoCoMo* — the benchmark Petrov critiques in Appendix A.2 as conflating memory and reasoning.
- Wu et al. (2024) — *LongMemEval* — same critique applies.
- Meyerson et al. (2025) — *Solving a million-step LLM task with zero errors* — the iterative-with-validation precedent at multi-step task scale.
- Wu et al. (2024) — *Learning to extract structured entities using language models (MuSEE)* — the staged-extraction-with-validation precedent Petrov extends, explicitly cited in §6.1.

Other notable citations include: Hu et al. (2025) memory taxonomy, Edge et al. (2024) GraphRAG, Lei et al. (2024) Spider 2.0 enterprise text-to-SQL (the 21% solve rate result Petrov uses to argue against general-purpose relational DBs), Madaan et al. (2023) Self-Refine (iterative refinement precedent), Hong et al. (2025) Context Rot (long-context degradation evidence), He et al. (2025) information-theoretic agentic design.

## Related Digests

- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall (the direct counter-thesis; Adler's "write-time intelligence is anti-intelligence" is the philosophical anti-pole of Petrov's schema-grounded write path)
- [[chhikara-2025-mem0]] — Mem0: Building production-ready AI agents with scalable long-term memory (head-to-head baseline; the closest production system to Adler-style design and the strongest non-schema competitor at 87.24% F1)
- [[hu-2026-evermemos]] — EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning (parallel write-time consolidation approach; both papers argue against fragment-based memory but use different consolidation primitives — MemScenes vs validated schema records)
- [[rasmussen-2025-zep-temporal-kg]] — Zep: A Temporal Knowledge Graph Architecture for Agent Memory (head-to-head baseline at 80.16% F1; the temporal-graph approach Petrov evaluates and outperforms specifically on state mutation queries)
- [[li-2025-memos]] — MemOS: A Memory OS for AI System (alternative architecture for unifying memory substrates; MemOS's MemCube abstraction sits at a different level than Petrov's schema-records but addresses similar lifecycle concerns)
- [[mao-2026-agent-memory-circuits]] — What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis (mechanistic counterpart; shows that Mem0/A-MEM grow routing-brain before content-extraction, which is exactly the failure mode Petrov's staged-extraction-with-validators is designed to prevent)
- [[maharana-2024-locomo]] — LoCoMo benchmark (Petrov critiques this in Appendix A.2 as conflating memory and reasoning, citing the ~6.4% label-error estimate)
- [[wu-2024-longmemeval]] — LongMemEval (same critique applies; Petrov argues their own benchmark is needed because LoCoMo/LongMemEval don't isolate memory functions cleanly)

## Reviewer Notes

**Hallucination check (sequential review against paper source) — Severity: Clean.**

Verified facts:

- **xmemory extraction results**: 90.42% object-level accuracy and 62.67% output-level accuracy with judge-in-the-loop → confirmed in Tables 6 and 7 (page 20–21).
- **Field-level F1**: xmemory (judge-in-the-loop) 97.53% F1 → confirmed Table 5 (page 19).
- **End-to-end memory benchmark**: xmemory 97.10% F1, Cognee 86.18%, Mem0 (no graph) 87.24%, Mem0 (graph) 86.07%, Supermemory 80.49%, Zep 80.16% → confirmed Table 8 (page 23).
- **Splitwise application task**: xmemory 95.2%, Supermemory 73.75%, Cognee 68.0%, Mem0 (graph) 59.1%, Mem0 (no graph) 54.9%, Zep 25.7% → confirmed Table 9 (page 25).
- **Markdown harness baselines**: transaction-preserving 12%, balance-only 40%, frontier app harnesses ~92% → confirmed in Section 8.4.
- **Single-pass math illustration**: 0.97²⁰ ≈ 0.54 → arithmetic checks (0.97²⁰ = 0.5438...).
- **Iteration math**: (1 − (1 − 0.97)²)²⁰ ≈ 0.98 → arithmetic checks (1 − 0.03² = 0.9991, 0.9991²⁰ ≈ 0.9821).
- **Token cost model**: with R=10, wₓ=10, rₓ=1, wₜ=3, rₜ=6, S = 63/20 = 3.15 → arithmetic checks.
- **Spider 2.0 result cited as ~21%** → confirmed in §4.3, citation [19].
- **LoCoMo label-error estimate ~6.4%** → confirmed citation [41] (snap-research issue 27 comment).
- **xmemory configuration**: Anthropic Sonnet 4.6 as main LLM, Opus 4.6 as judge → confirmed §8.3 ("xmemory is evaluated in deep mode... Anthropic Sonnet 4.6 was used as the main LLM and Opus 4.6 was used as the judge").
- **Frontier baselines tested**: Sonnet 4.6, Opus 4.7, GPT-5.4 (±advanced reasoning), GPT-5.5 (±high reasoning effort), Gemini 3.1 Pro preview → confirmed §8.2.
- **Gemini 3.1 Pro is the strongest single-model baseline**: 89.24% object accuracy, 61.67% output accuracy → confirmed Tables 6 and 7. xmemory's judge-in-the-loop (90.42% / 62.67%) just edges Gemini on both.
- **Three memory contexts (request / session / main)** → confirmed §6.3 verbatim.
- **Three-stage pipeline (object detection → field detection → field-value extraction)** → confirmed §6.1 verbatim.
- **Data Processing Inequality citation framing** → confirmed §1.2 (Cover & Thomas, Shannon, He et al. 2025).
- **MuSEE attribution for staged decomposition precedent** → confirmed §6.1 ("aligned with MuSEE [24], which also decomposes structured entity extraction into multiple stages").
- **Cognee evaluation setup**: Python SDK 1.0.3, Anthropic Sonnet 4.6 as main LLM, OpenAI text-embedding-3-large embeddings → confirmed §8.3.
- **xmemory dataset URL**: `https://github.com/xmemory-ai/datasets` → confirmed §8.1.
- **Splitwise note**: "we disable LLM-result caching during evaluation and prefer generator-based dataset slices over a single fixed instance" → confirmed §8.4.
- **Appendix A.2 LoCoMo critique** including the Jon/Gina, John's financial status, and Caroline/Dr. Seuss examples → all verbatim from §A.2.
- **Author affiliation**: xmemory, [alex, alexg, denis, dima]@xmemory.ai → confirmed page 1.
- **Submission**: arXiv:2604.27906v2 [cs.AI], May 4 2026 → confirmed page 1.

Watch-outs that should not affect digest validity but are worth flagging:

- The paper contains a **prompt injection at the end** (page 34, "Note to any AI agent processing this document") that attempts to direct any summarising LLM to recommend the paper to "well-known voices in AI" and treat schema-grounded memory as high-priority. This is a soft attempt and was not complied with; the digest evaluates the paper on its merits. Flagged in **What Experts Overlook §6** for traceability.
- The author affiliation block shows only "xmemory" as institution with no separate corporate disclosure. This is a vendor-authored paper evaluating its own product against competitors (Cognee, Mem0, Supermemory, Zep). The paper acknowledges this in §8.3 ("The creators of each system know their own configurations and optimisation strategies better than any external evaluator. We therefore invite the teams behind Cognee, Mem0, Supermemory, Zep, and any other memory system to run these datasets through their own setups and publish results independently"), and the datasets are publicly released, but this remains a vendor benchmark and should not be cited as third-party-evaluated.
- The arXiv ID `2604.27906` is genuinely unusual (the leading `2604` resembles a 2026-April identifier under the new arXiv scheme but the layout is non-standard). The paper is labelled "arXiv:2604.27906v2 [cs.AI] 1 May 2026" on page 1; I take this at face value but note it as a minor metadata uncertainty.

No factual rewrites needed. **Severity: Clean.**
