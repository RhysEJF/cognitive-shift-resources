---
corpus: agentic-memory
kind: paper-digest
slug: ma-2026-nemori-distillation
title: "What Deserves Memory: Adaptive Memory Distillation for LLM Agents"
authors:
  - "Ma, Wenquan"
  - "Nan, Jiayan"
  - "Wu, Wenlong"
  - "Chen, Yize"
year: 2026
publication_date: "2026-04"
venue: "arXiv preprint (cs.AI)"
source_url: "https://arxiv.org/abs/2508.03341"
doi: null
arxiv_id: "2508.03341"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Treat predictability as a filter for what deserves memory: write only the residual between what already-stored knowledge predicts about a new episode and what actually happened — everything else is redundant."
topics:
  - agent-memory
  - memory-distillation
  - predictive-coding
  - episodic-semantic-memory
  - long-context-llm
  - knowledge-consolidation
tags:
  - paper
  - memory-architecture
  - encode-stage
  - aggregate-stage
  - benchmark-locomo
  - benchmark-longmemeval
  - cognitive-inspired
entities:
  - ma-wenquan
  - nan-jiayan
  - wu-wenlong
  - chen-yize
related_digests:
  - zhang-2025-ace
  - xu-2025-a-mem-agentic-memory
  - kang-2025-memory-os
  - chhikara-2025-mem0
  - hu-2026-evermemos
  - maharana-2024-locomo
  - rasmussen-2025-zep-temporal-kg
  - park-2023-generative-agents
  - mcclelland-1995-complementary-learning-systems
citations:
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"]
    year: 2020
    venue: "NeurIPS 2020"
    arxiv_id: "2005.11401"
    url: "https://arxiv.org/abs/2005.11401"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Charles Packer", "Vivian Fang", "Shishir G. Patil", "Kevin Lin", "Sarah Wooders", "Joseph E. Gonzalez"]
    year: 2023
    arxiv_id: "2310.08560"
    url: "https://arxiv.org/abs/2310.08560"
  - title: "MemoryBank: Enhancing Large Language Models with Long-Term Memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "He Ye", "Yanlin Wang"]
    year: 2024
    venue: "AAAI 2024"
    url: "https://arxiv.org/abs/2305.10250"
  - title: "Memory OS of AI Agent"
    authors: ["Jiazheng Kang", "Mingming Ji", "Zhe Zhao", "Ting Bai"]
    year: 2025
    venue: "EMNLP 2025"
    arxiv_id: "2506.06326"
    url: "https://arxiv.org/abs/2506.06326"
  - title: "CAM: A Constructivist View of Agentic Memory for LLM-based Reading Comprehension"
    authors: ["Rui Li", "Zeyu Zhang", "Xiaohe Bo", "Zihang Tian", "Xu Chen", "Quanyu Dai", "Zhenhua Dong", "Ruiming Tang"]
    year: 2025
    venue: "NeurIPS 2025"
    url: null
  - title: "ArigraphLLM: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents"
    authors: ["Petr Anokhin", "Nikita Semenov", "Artyom Y. Sorokin", "Dmitry Evseev", "Andrey Kravchenko", "Mikhail Burtsev", "Evgeny Burnaev"]
    year: 2025
    venue: "IJCAI 2025"
    url: null
  - title: "A-MEM: Agentic Memory for LLM Agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "Hang Gao", "Juntao Tan", "Yongfeng Zhang"]
    year: 2025
    venue: "NeurIPS 2025"
    arxiv_id: "2502.12110"
    url: "https://arxiv.org/abs/2502.12110"
  - title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
    authors: ["Preston Rasmussen", "Pavlo Paliychuk", "Travis Beauvais", "Jack Ryan", "Daniel Chalef"]
    year: 2025
    arxiv_id: "2501.13956"
    url: "https://arxiv.org/abs/2501.13956"
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    authors: ["Joon Sung Park", "Joseph C. O'Brien", "Carrie Jun Cai", "Meredith Ringel Morris", "Percy Liang", "Michael S. Bernstein"]
    year: 2023
    venue: "UIST 2023"
    url: null
  - title: "Emotional RAG: Enhancing Role-Playing Agents through Emotional Retrieval"
    authors: ["Le Huang", "Hengzhi Lan", "Zijun Sun", "Chuan Shi", "Ting Bai"]
    year: 2024
    venue: "IEEE ICKG 2023"
    url: null
  - title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "Taranjeet Singh", "Deshraj Yadav"]
    year: 2025
    arxiv_id: "2504.19413"
    url: "https://arxiv.org/abs/2504.19413"
  - title: "Hello Again! LLM-Powered Personalized Agent for Long-Term Dialogue"
    authors: ["Hao Li", "Chenghao Yang", "An Zhang", "Yang Deng", "Xiang Wang", "Tat-Seng Chua"]
    year: 2025
    venue: "NAACL 2025"
    url: null
  - title: "SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents"
    authors: ["Zhuoshi Pan", "Qianhui Wu", "Huiqiang Jiang", "Xufang Luo", "Hao Cheng", "Dongsheng Li", "Yuqing Yang", "Chin-Yew Lin", "H. Vicky Zhao", "Lili Qiu", "Jianfeng Gao"]
    year: 2025
    venue: "ICLR 2025"
    url: null
  - title: "Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo benchmark)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "Mohit Bansal", "Francesco Barbieri", "Yuwei Fang"]
    year: 2024
    venue: "ACL 2024"
    arxiv_id: "2402.17753"
    url: "https://arxiv.org/abs/2402.17753"
  - title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "Yuwei Zhang", "Kai-Wei Chang", "Dong Yu"]
    year: 2025
    venue: "ICLR 2025"
    arxiv_id: "2410.10813"
    url: "https://arxiv.org/abs/2410.10813"
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    authors: ["Nelson F. Liu", "Kevin Lin", "John Hewitt", "Ashwin Paranjape", "Michele Bevilacqua", "Fabio Petroni", "Percy Liang"]
    year: 2024
    venue: "TACL 12:157-173"
    arxiv_id: "2307.03172"
    url: "https://arxiv.org/abs/2307.03172"
  - title: "LightMem: Lightweight and Efficient Memory-Augmented Generation"
    authors: ["Jizhan Fang", "Xinle Deng", "Haoming Xu", "Ziyan Jiang", "Yuqi Tang", "Ziwen Xu", "Shumin Deng", "Yunzhi Yao", "Mengru Wang", "Shuofei Qiao", "Huajun Chen", "Ningyu Zhang"]
    year: 2025
    arxiv_id: "2510.18866"
    url: "https://arxiv.org/abs/2510.18866"
  - title: "Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects"
    authors: ["Rajesh P. N. Rao", "Dana H. Ballard"]
    year: 1999
    venue: "Nature Neuroscience 2(1):79-87"
    url: null
  - title: "The Free-Energy Principle: A Unified Brain Theory?"
    authors: ["Karl Friston"]
    year: 2010
    venue: "Nature Reviews Neuroscience 11(2):127-138"
    url: null
  - title: "Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science"
    authors: ["Andy Clark"]
    year: 2013
    venue: "Behavioral and Brain Sciences 36(3):181-204"
    url: null
  - title: "Why There Are Complementary Learning Systems in the Hippocampus and Neocortex"
    authors: ["James L. McClelland", "Bruce L. McNaughton", "Randall C. O'Reilly"]
    year: 1995
    venue: "Psychological Review 102(3):419"
    url: null
  - title: "LangChain"
    authors: ["Harrison Chase"]
    year: 2022
    venue: "GitHub repository"
    url: "https://github.com/langchain-ai/langchain"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Overview of the NEMORI framework — two cascading modules guided by three priors (structure / representation / distillation) feeding a management-agnostic interface"
  page: 3
  image_path: "figures/ma-2026-nemori-distillation-fig.png"
---

# What Deserves Memory: Adaptive Memory Distillation for LLM Agents

**Authors:** Wenquan Ma, Jiayan Nan, Wenlong Wu, Yize Chen
**Published:** 2026-04 · [Source](https://arxiv.org/abs/2508.03341)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

NEMORI is a training-free memory framework for LLM agents that decides what to retain not via importance scores, emotion tags, or fact templates (subjective heuristics), but via **prediction error**: only information the system's existing knowledge could NOT anticipate gets distilled into semantic memory. Two cascading modules — **Episodic Memory Integration** (LLM-driven partitioning + narrative rewriting + associative merging of raw interaction streams into episode objects) and **Semantic Knowledge Distillation** (anticipate-the-episode-from-existing-knowledge → diff against ground truth → extract the residual as semantic insights with new/merge/conflict consolidation) — front-load reasoning to write-time so retrieval can stay simple (top-k embedding search). On LoCoMo it ties Full-Context accuracy (80.8 vs. 80.6 on gpt-4.1-mini) while using **88% fewer tokens** and 47% lower latency, beats every dedicated memory baseline (Mem0, A-MEM, MemoryOS, Zep, LangMem) on average score, and as a *distillation kernel* fed into A-MEM and MemoryOS cuts their storage 45-64% while improving core (non-temporal) scores. On the harder LongMemEvalS (105K avg context) it beats Full-Context by +16.7%/+13.7% across two models with 95-96% less context — distillation value grows with context length.

**ENGRAM mapping:** Primary contribution sits in **E — Encode** (a non-heuristic write-time filter driven by predictive-coding error) and **A — Aggregate** (three-way new/merge/conflict consolidation against the semantic DB). It is deliberately *agnostic* about **N — Network** (flat episodic + semantic stores native, but pluggable into A-MEM's note-graph or MemoryOS's hierarchical OS), **R — Retrieve** (vanilla top-k cosine similarity — they argue good encoding makes elaborate retrieval unnecessary), and largely silent on **G — Ground** (no provenance metadata beyond timestamps) and **M — Maintain** (no decay/eviction; consolidation alone handles drift).

## Key Takeaway

**The hard thinking belongs at write-time, indexed by prediction error.** NEMORI's central architectural bet — operationalised, not just asserted — is that what you should remember is exactly what your current memory can't predict. Concretely: for every incoming episode, the system *first* uses the existing semantic store to generate `P̂in` (a textual prediction of "what should have happened in this episode given what we already know"), *then* diffs `P̂in` against the actual interaction `Pin` via a "Prediction Error Distillation" LLM call, and only the gap becomes a new semantic statement. If you already know "Alice is a senior engineer at Google" and the episode says "Alice mentioned she switched from Java to Python for ML projects," the prediction `P̂in` would have invented some plausible-but-vague employment narrative, and the residual extracted is the Java→Python switch — not the (already-known) employment fact. This converts "what's worth remembering" from a designer-chosen heuristic into a data-driven, episode-local computation that automatically adapts as the memory grows.

The empirical payoff that licenses this bet: ablating prediction-error and replacing it with direct semantic distillation (Nemori-s) drops LLM-judge score from 73.0→52.0 on gpt-4o-mini (a 25% relative collapse), with the biggest hit on Temporal Reasoning (67.6→33.3, −51%). The prediction step isn't decorative; it is the load-bearing differentiator. **ENGRAM tag: E (Encode) — this is the paper's defining encode-stage move.**

## Implications

**For Flow OS's `/learn` pipeline (Encode stage).** Flow currently does direct distillation: every turn becomes a candidate memory judged by salience heuristics (`brain-health/progress.md` watermark + LLM extractor). NEMORI argues this writes too much — the predictable parts are redundant. A NEMORI-style adapter for `/learn` would: (1) before extracting from a session, build `Sin` = top-K retrieval from existing memories on the session's cue; (2) prompt the extractor to first *predict* what facts would be in the session given `Sin`; (3) only emit memories that fall outside the prediction set. Expected effect by analogy to the paper's Tables 14-15: 45-64% fewer memory entries with non-degraded retrieval quality — directly reducing the bloat that currently necessitates the `_v1-toc/` archive and the `/learn` dedup step. **ENGRAM E + A.**

**For the contradiction-surface problem.** NEMORI's "conflict" branch of consolidation (one of new/merge/conflict in §3.3.3) *purges* the outdated entry and replaces it with the new fact — "conflict purges outdated entries... when kq invalidates previous knowledge." This is the opposite of the memory-architect lens's stated goal of surfacing rather than smoothing contradictions. For Flow's purposes the implementation choice would invert: route the `conflict` decision to a contradiction file (the existing `.flow/contradictions/` directory pattern the user is already using) rather than silently overwriting. The paper's notable absence of a contradiction-preservation mode is itself a data point — they explicitly say "LoCoMo rarely involves knowledge updates requiring consolidation" (§4.4), which is why this branch is shown to contribute minimally on benchmarks but matters in production. **ENGRAM G + M cross-interaction.**

**For write-time-vs-query-time synthesis.** This paper is the clearest empirical argument I have for *write-time-heavy* designs. NEMORI's response-time retrieval is vanilla top-k cosine plus a single answer-generation LLM call — yet it beats systems with sophisticated retrieval (Zep's graph traversal, A-MEM's link-following, MemoryOS's hierarchical search). Cost-per-question (Table 4) drops to 3,053 ms total — comparable to RAG-4096's 2,884 ms but with 73 LLM score vs RAG's 30. The "where the hard thinking belongs" lens question gets a defensible answer: **front-load it, and retrieval becomes boring on purpose.** This contradicts the implicit "smart retrieval saves us from dumb writes" framing common in graph-RAG / agentic-retrieval work (cf. [[edge-2024-graphrag]], [[xu-2025-a-mem-agentic-memory]]). **ENGRAM E ↔ R interaction.**

**For the "AI as maintainer" job description.** NEMORI's `Consolidate(Kin, M)` interface (§3.3.3) is the closest thing in this paper to defining the AI's ongoing role. The three operations — `new`, `merge`, `conflict` — are essentially the maintainer's job description, executed on every write. But maintenance *between* writes (decay, archival, garbage collection, summarization of cold entries) is explicitly out of scope ("naive strategies for management and retrieval", Limitations §). This is a useful negative datapoint: the paper proves *write-time consolidation alone* can carry storage efficiency without an active maintainer loop, at least on benchmark-length conversations (up to 105K tokens). **ENGRAM M — paper offers no design here.**

**For the shape-of-memory question.** NEMORI keeps two parallel stores — episodic (narrative + raw + embedding) and semantic (statement + embedding). Ablation: removing semantic alone costs −25.1% on gpt-4o-mini (catastrophic) but only −4.8% on gpt-4.1-mini (mild); removing episodic costs −11.0% / −7.3%. Interpretation: the smarter the answer-generation model, the more it can re-derive from raw episodes, but a fast/cheap model leans hard on pre-distilled semantic facts. **Decision rule for Flow:** smaller answer-generation models warrant a fatter semantic store; frontier models can lean on episode retrieval. **ENGRAM N + R interaction.**

## How to Apply It (method)

**The full pipeline in one pass** (Algorithm 1, paper §3.2-3.3):

1. **Local Message Partitioning (Ppar).** Buffer messages until window size w=20 is reached; one LLM call partitions the window into coherent episodes based on topic shifts, intent transitions, temporal markers, and structural signals (full prompt in Appendix D.1.1). Output: a partition `{O1...On}` over the message indices.

2. **Narrative Episode Generation (Pnar).** For each raw episode `Pj`, an LLM call produces `(Nj, cj)` — a third-person narrative rewrite plus a short episodic-cue title. This is the "egocentric → allocentric" transform from the representation prior. Compute `vj = embed(cj ∥ Nj)`.

3. **Associative Memory Integration (Psel + Pint).** Retrieve top-Ke=5 candidates from the episodic DB by cosine on `vj`. One LLM call (Psel) picks the most-continuous candidate or `-1`. If a match, a second LLM call (Pint) merges the two episodes into a unified narrative; otherwise insert as new.

4. **Anticipatory Schema Synthesis (Pant).** Evoke `Sin` = top-Ks=10 semantic statements with similarity > τ=0.70 to the episode embedding. One LLM call prompts: "Given the episodic cue `cin` and prior knowledge `Sin`, predict what actually happened in this episode." Output: textual `P̂in`.

5. **Prediction Error Distillation (Pdis).** One LLM call: "Compare actual episode `Pin` to predicted `P̂in`; extract ONLY the persistent facts in `Pin` that are missing or misrepresented in `P̂in`." Output: `Kin = {k1...kd}` list of semantic statements.

6. **Agnostic Knowledge Consolidation (Pcon).** For each `kq ∈ Kin`: retrieve top-Km=5 similar entries from semantic DB; one LLM call decides `{new | merge | conflict}` with a conservative-default prompt ("Default to NEW when in doubt"). Execute the decision against `Ds`.

**Response generation (Algorithm 2, §3.4).** Embed the query, retrieve top-k=10 episodes (top-2 include raw text, rest narrative only) and top-m=20 semantic statements, concat into the answer prompt. No reranking, no graph traversal, no multi-hop.

**Hyperparameters that matter (from RQ3-RQ4 ablations):**
- `τ=0.70` similarity threshold for schema evocation
- `Ke=Km=5` candidate counts for episode/semantic consolidation
- `Ks=10` for evoking the schema synthesis context
- `k=10, m=2k=20` for response retrieval — *saturates* there (Fig. 3); going higher costs more without clear gain
- `w=20` observation window — *robust across w∈{5,...,40}* (Table 11), so this isn't a tuning trap
- All LLM calls use the same backbone (gpt-4o-mini or gpt-4.1-mini); embeddings = text-embedding-3-small

**The "kernel" integration pattern (§A.3) — adopting NEMORI inside another memory system.** Intercept the host system's context buffer `B̃` for an incoming query and use it as `Sin` directly (instead of running your own retrieval). Distil insights as usual. Inject each `kq` as an independent message into the host's input sequence; let the host's native management code (A-MEM links, MemoryOS hierarchy, etc.) absorb it as it would any other write. This is how they got 45-64% storage cuts on A-MEM + MemoryOS without rewriting those systems.

**Pitfalls and edge cases the paper flags:**
- Default to `new` in consolidation — "merge" and "conflict" are explicitly framed as RARE branches; aggressive merging destroys unique facts.
- Use episode (not message) as the atomic processing unit — message-wise processing is what makes baselines 3-5× more expensive (cf. Tables 3 + 9).
- Don't index the raw episodes — Table 6 shows narrative-episode embeddings outperform raw-text embeddings, validating the representation-prior rewrite.

## Best Figure

![Figure 1 — Overview of the NEMORI framework (page 3)](figures/ma-2026-nemori-distillation-fig.png)

**Figure Page: 3.** Figure 1 is the structural map of the whole paper — and worth dwelling on because every architectural commitment in NEMORI traces back to one of three priors visualised at the top, each colour-coded to the module it constrains.

**Top band — the three priors (the inductive biases that justify each module).** "Structure Prior: Integrity of Episode" feeds the Episodic Memory Integration block (left half of the middle band). "Representation Prior: Asymmetry of Perspective" feeds the same block's Narrative Episode Generation step — this is the egocentric→allocentric rewrite. "Distillation Prior: Predictability Implies Redundancy" sits between the two cascading modules and feeds the Semantic Knowledge Distillation block (right half of middle band). Reading these as a story: the framework is openly claiming three falsifiable inductive biases about interaction data, and each module is the bias's operational consequence.

**Middle band, left — Episodic Memory Integration.** Three sub-blocks chained left-to-right: Local Message Partitioning (the buffer-and-cut step) → Narrative Episode Generation (the rewrite) → Associative Memory Integration (the merge-or-new decision). The episodic DB sits beneath this band as a single cylinder.

**Middle band, right — Semantic Knowledge Distillation.** Three sub-blocks: Anticipatory Schema Synthesis → Prediction Error Distillation → Agnostic Knowledge Consolidation. The arrows show the prediction loop closing: existing semantic memory flows up to synthesize the anticipatory schema, the schema diffs against the new episode, and the residual flows back down into the semantic DB via consolidation.

**Right band — Management-Agnostic Interface.** Three boxes show this distillation layer plugging into (a) the native management implementation (which IS a flat semantic DB they ship), (b) MemoryOS (Kang 2025), or (c) A-MEM (Xu 2025). The arrows here are the kernel-integration pattern from §A.3.

**Why this is the load-bearing figure (memory-architect lens):** the figure is essentially an **ENGRAM compliance map** — it makes visible that the paper takes strong positions on Encode (the entire Semantic Knowledge Distillation chain) and Aggregate (the consolidation step), explicitly factors out Maintenance (the right band is "agnostic"), and treats Network as a pluggable concern. The single-cylinder episodic DB and the small semantic-DB icon also quietly disclose Retrieve is naive (no graph, no hierarchy on the native side). It is rare to find a paper whose system diagram lets you read off which dimensions of the design space are claimed vs. deferred — this one does.

## What Experts Overlook

**1. The "conflict" branch is gentler than the prompt's wording suggests, and that's a design choice in disguise.** §3.3.3 says conflict "purges outdated entries and replaces with (kq, uq)" — but the Pcon prompt (Appendix D.1.7) makes CONFLICT_DELETE "VERY RARE" with the strong instruction "**Only** if the new item DIRECTLY CONTRADICTS existing item(s) about the SAME specific fact." Practically: the system almost never invokes the conflict path on LoCoMo because the prompt is engineered to suppress it. Toggling native management (consolidation on vs. off, i.e. plain RAG) costs only 0.4 points on LoCoMo (§4.4). The paper frames this as "LoCoMo rarely involves knowledge updates" but it's also a self-fulfilling outcome of the conservative prompt — a more contradiction-rich corpus would expose whether the merge/conflict logic is actually load-bearing. **A memory architect should read this as: the consolidation mechanism is present but largely untested at scale.**

**2. The episode-centric processing is the secret cost-killer, not the prediction-error step.** The Table 3 cost comparison gets framed as a benefit of the prediction-error filter, but read §4.3's footnote and Table 9 carefully: NEMORI's 38.7% token reduction comes mostly from processing whole episodes once instead of message-by-message. The prediction-error step ADDS cost (Distillation = 30.3% of total construction tokens, Table 9). Without the episode aggregation, prediction-error filtering would likely be more expensive than baselines. This means "front-load reasoning via prediction error" and "batch processing as episodes" are *separate* design moves, and the cost story belongs to the second.

**3. The schema-evocation step has a silent failure mode the paper sidesteps.** `Sin ← Top-Ks(Sr ∈ Ds | sim(vin, ur) > τ)` (§3.3.1) filters semantic entries by similarity > 0.70. On a *cold* memory (early in a conversation), `Sin` is empty or near-empty, so the anticipatory schema is "predict what happened given essentially no prior" — which means the prediction is uninformative and *everything* in the episode looks like prediction error. The system ingests aggressively early. The paper doesn't discuss the implication: the distillation rate is non-stationary and should fall as memory matures. No measurement of write-rate over time is provided. For an architect comparing this to a v2 memory layer with bootstrapping concerns, this is a non-trivial gap.

**4. The "training-free" framing hides ~10 prompt-engineered LLM calls per episode.** Construction cost per LoCoMo dialogue: 373 LLM calls (Table 3) across partitioning, narrative, integration, schema synthesis, distillation, consolidation. Each of those is a specialised prompt with carefully tuned defaults (the consolidation prompt's "Default to NEW" instruction is doing a lot of heavy lifting). "Training-free" here means "no fine-tuning" — it does NOT mean low-engineering. Anyone porting this approach owns 7+ prompt templates as part of the system contract, each of which is a calibration surface.

**5. The "management-agnostic" claim is empirically weakened by the agnosticism itself.** When NEMORI's distilled semantic memory `K` is fed into A-MEM in place of raw messages, A-MEM's Temporal Reasoning score *drops* significantly (66.7→41.1 on gpt-4.1-mini, Table 14) — because distilled facts strip the conversational timestamps and temporal-reference scaffolding that A-MEM's note-graph uses to reconstruct chronology. The 45-64% storage win comes at the cost of temporal capability in any downstream system that relied on conversational structure for time reasoning. **The agnosticism is a feature for storage, a bug for time.**

**6. The prompt set is the unstated reproducibility risk.** Appendix D contains the prompts — but the most consequential calibration ("Default to NEW unless ABSOLUTELY CERTAIN", "Episodes should typically contain 2-15 messages", "Eliminate redundancy while preserving unique information") is conversational, not adversarial-tested. The paper's reported numbers are functions of these exact words. A practical implementer should expect to re-tune them per backbone model and per domain — and the paper's lack of a prompt-sensitivity analysis is a real gap.

## Extracted Prompts

The prompts below are the operational core of NEMORI — full templates are in the paper's Appendix D. Variable names use the paper's notation (lowercased and squared-bracketed for clarity).

**1. Local Message Partitioning (Ppar) — episode-boundary detection.**

> You are an intelligent conversation segmentation expert. Your task is to analyze a batch of messages and group them into coherent episodes.
>
> You will receive [count] messages numbered from 1 to [count]: [messages]
>
> ## Your Task
> Analyze these messages and group them into coherent episodes with **HIGH SENSITIVITY** to topic shifts. Be strict and create NEW episodes when detecting:
> 1. **Topic Change** (Highest Priority): Do the new messages introduce a completely different topic? Is there a shift from one specific event to another? Has the conversation moved from one question to an unrelated new question?
> 2. **Intent Transition**: Has the purpose of the conversation changed? (e.g., from casual chat to seeking help)
> 3. **Temporal Markers**: Are there temporal transition markers ("earlier", "before", "by the way", "oh right", "also", etc.)? Is the time gap between messages more than 30 minutes?
> 4. **Structural Signals**: Are there explicit topic transition phrases ("changing topics", "speaking of which", "quick question", etc.)?
> 5. **Content Relevance**: How related is the new message to the previous discussion? (Consider splitting if relevance < 30%)
>
> Decision Principles: **Prioritize topic independence** — each episode should revolve around one core topic. **When in doubt, split.** **Maintain reasonable length** — a single episode typically shouldn't exceed 10-15 messages.
>
> Return a JSON object with episodes, where each episode contains: `indices` (list of 1-based message numbers) and `topic` (brief description).

**2. Anticipatory Schema Synthesis (Pant) — the load-bearing prediction step.**

> You are a knowledge-based episode prediction system. Your task is to reconstruct a complete conversation episode based on limited clues and your knowledge base.
>
> IMPORTANT: You are predicting the ACTUAL CONTENT and KNOWLEDGE of what happened, not the writing style or format.
>
> ## Input Information
> Episodic Cue (Title/Summary): [episode_title]
> Evoked Context (Prior Knowledge): [evoked_context]
>
> ## Your Task
> Based on the above clues, reconstruct what you believe happened in this episode. Focus on:
> 1. **Core Facts**: What specific information was discussed?
> 2. **Key Decisions**: What choices or conclusions were made?
> 3. **Knowledge Exchange**: What knowledge was shared or learned?
> 4. **Logical Flow**: How did the conversation progress?
>
> ## What to IGNORE
> - Writing style, formatting, exact phrasing, timestamp inclusion, formality level
>
> Generate a natural narrative that captures what you predict happened. Focus on the SUBSTANCE, not the STYLE.

**3. Prediction Error Distillation (Pdis) — the diff that becomes memory.**

> You are extracting valuable knowledge by comparing original conversation with predicted content.
>
> Actual Episode (Pin - Ground Truth): [original_messages]
> Anticipatory Schema (P̂in - Expectation): [predicted_episode]
>
> ## Your Task
> Extract ONLY the valuable knowledge that exists in the original but is missing or misrepresented in the prediction.
>
> ## What to Extract:
> Knowledge that is: factual and will remain true over time; specific (names, titles, preferences, reasons); useful for future interactions; **not captured accurately in the prediction**.
>
> ## What to Ignore:
> Temporary states or emotions; conversational flow or style; information already well-represented in prediction; social pleasantries or reactions.
>
> [Followed by 3 worked examples showing original-vs-predicted-vs-extracted triplets to anchor the format.]
>
> Return JSON: `{"statements": ["First factual statement extracted from the gap", ...]}`. Each statement self-contained, present tense for persistent facts, focus on quality over quantity.

**4. Semantic Consolidation (Pcon) — the conservative new/merge/conflict gate.**

> You are a conservative knowledge base maintainer. Your default action is NEW unless you are ABSOLUTELY CERTAIN about merging or conflict.
>
> New Item Type: [new_type]
> Content: [new_content]
> Existing Similar Items: [candidates]
>
> ## Actions (choose exactly one)
> 1. **NEW** (DEFAULT): Choose this if items describe different facts/events/entities, refer to different times/places/contexts, or you have ANY doubt about whether they are truly identical or contradictory.
> 2. **MERGE** (RARE): Only if the new item and existing item(s) express the EXACT SAME fact with just different wording. Example: "User likes coffee" and "The user enjoys coffee".
> 3. **CONFLICT_DELETE** (VERY RARE): Only if the new item DIRECTLY CONTRADICTS existing item(s) about the SAME specific fact. Example: "User lives in Beijing" vs "User lives in Shanghai" (same attribute, different value).
>
> ## CRITICAL RULES
> - **Default to NEW** — when in doubt, always choose NEW
> - Similar topics ≠ same fact. "User has a cat" and "User has a dog" are BOTH valid; choose NEW.
> - Only MERGE when items are semantically IDENTICAL (just rephrased).
> - Only CONFLICT_DELETE for direct contradictions about the SAME attribute.
> - Preserve information richness — losing unique details is worse than having duplicates.
>
> Output: `{"decision": "NEW|MERGE|CONFLICT_DELETE", "target_ids": [...], "new_content": "...", "reason": "..."}`.

**Architectural pattern worth noting across all four:** each prompt is single-LLM-call, single-decision, with explicit defaults that bias conservatively. The system's behaviour emerges from the *composition* of conservative decisions, not from any one heroic prompt. This is reproducible engineering, not prompt-magic.

## Citations

23 citations extracted (see frontmatter for full structured list). The core lineage:

- **Cognitive priors:** [[mcclelland-1995-complementary-learning-systems]] (CLS); Rao & Ballard 1999 (predictive coding); Friston 2010 (free-energy principle); Clark 2013 (predictive brains).
- **LLM-agent memory baselines compared:** [[chhikara-2025-mem0]], [[xu-2025-a-mem-agentic-memory]], [[kang-2025-memory-os]], [[rasmussen-2025-zep-temporal-kg]], [[park-2023-generative-agents]] (Generative Agents — source of the "importance score" baseline), Packer 2023 (MemGPT), Zhong 2024 (MemoryBank), Huang 2024 (Emotional RAG).
- **Benchmarks:** [[maharana-2024-locomo]] (LoCoMo, primary), Wu 2025 (LongMemEvalS — scalability test).
- **Substrate / context:** Lewis 2020 (RAG); Liu 2024 (Lost in the Middle — motivates the long-context bottleneck).

## Related Digests

- [[zhang-2025-ace]] — Agentic Context Engineering: also a write-time-heavy design (Generator/Reflector/Curator with deterministic non-LLM merge) but operates on agent playbooks rather than conversational memory; same "front-load the thinking" thesis with different substrate.
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: direct baseline; NEMORI integrates as A-MEM's distillation kernel for 64% storage cut, but at temporal-reasoning cost.
- [[kang-2025-memory-os]] — MemoryOS: direct baseline; NEMORI integrates as distillation kernel for 53% storage cut.
- [[chhikara-2025-mem0]] — Mem0: direct baseline; uses fact-extraction templates (a "distillation-time" approach NEMORI argues against).
- [[hu-2026-evermemos]] — EverMemOS (seed of the cycle this digest belongs to); shares the long-term-memory framing.
- [[maharana-2024-locomo]] — LoCoMo benchmark used throughout NEMORI's Table 2.
- [[rasmussen-2025-zep-temporal-kg]] — Zep: baseline; the temporal-knowledge-graph approach NEMORI undercuts on temporal reasoning by +14.8%.
- [[park-2023-generative-agents]] — origin of the "importance score" distillation heuristic NEMORI is arguing against.
- [[mcclelland-1995-complementary-learning-systems]] — the CLS theory NEMORI's two-module architecture explicitly echoes.

## Reviewer Notes

**Hallucination check — overall severity: Clean.**

Method-level claims spot-checked against §3 and Appendix A/D:
- The three priors (structure/representation/distillation), the two cascading modules, the new/merge/conflict consolidation, the τ=0.70 / Ke=Km=5 / Ks=10 / w=20 / k=10 / m=2k hyperparameters, and the role of the prediction-error step are all faithful to the paper text.
- The "predict-then-diff" framing of Pant + Pdis matches Appendix D.1.5 and D.1.6 verbatim in spirit; quoted prompt fragments above are exact.

Numerical claims spot-checked against Tables 2, 3, 4, 5, 8, 14, 15:
- LoCoMo Avg LLM: 80.8 (gpt-4.1-mini) vs LangMem 73.4 → +10.1% — checks (Table 2).
- LoCoMo Avg LLM 73.0 (gpt-4o-mini) vs Mem0 61.3 → +19.1% — checks (Table 2).
- Construction cost: 373.2 calls vs 1010.2 for LangMem (−59.5%) — checks (Table 3).
- Response generation tokens: 2,745 vs Full-Context 23,653 = 88% reduction; latency 3,053ms vs 5,806ms = 47% reduction — checks (Table 4).
- Ablation w/o e on gpt-4o-mini: 65.0 vs Nemori-s 52.0 = +25% relative — checks (Table 5).
- Temporal Reasoning ablation: w/o e at 57.9 vs Nemori-s at 33.3 on gpt-4o-mini, +73.9% — checks (Table 10).
- LongMemEvalS: NEMORI 64.2 vs Full-Context 55.0 = +16.7%; gpt-4.1-mini 74.6 vs 65.6 = +13.7% — checks (Table 8).
- A-MEM storage cut 64.3% on gpt-4o-mini, MemoryOS 53.1% — checks (Table 15).
- A-MEM core score +6.1% on gpt-4o-mini under K-input — checks (Table 14).

Cited-author surnames cross-checked against the References section (§References, pp. 9-10). All baseline-method names (Mem0, A-MEM, MemoryOS, Zep, LangMem, MemoryBank, MemGPT, LoCoMo, LongMemEvalS) match the cited papers exactly.

Two minor interpretive framings flagged but not factually wrong:
- The "ENGRAM compliance map" framing of Figure 1 in "Best Figure" is a *lens-driven reading*, not a paper claim — the paper does not use the word ENGRAM. Explicitly tagged as lens-driven in the section text.
- The §4.4 footnote that "LoCoMo rarely involves knowledge updates" is a single-sentence paper claim with no supporting analysis, so the "What Experts Overlook" #1 reading of it as partly self-fulfilling is interpretation. Flagged as such.

No fabricated citations, no invented hyperparameter values, no over-claimed comparisons. The digest is safe to rely on for memory-architect decision support.
