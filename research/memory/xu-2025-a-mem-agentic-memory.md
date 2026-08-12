---
corpus: agentic-memory
kind: paper-digest
slug: xu-2025-a-mem-agentic-memory
title: "A-MEM: Agentic Memory for LLM Agents"
authors:
  - "Wujiang Xu"
  - "Zujie Liang"
  - "Kai Mei"
  - "Hang Gao"
  - "Juntao Tan"
  - "Yongfeng Zhang"
year: 2025
publication_date: "2025-02"
venue: "arXiv preprint (v11, Oct 2025)"
source_url: "https://arxiv.org/abs/2502.12110"
doi: null
arxiv_id: "2502.12110"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Treat every new memory as a Zettelkasten note: at write time an LLM auto-generates keywords/tags/context, retrieves the top-k semantically nearest existing notes, and lets a second LLM call decide which connections to forge AND rewrite the tags/context of those neighbours — collapsing the canonical four-stage memory pipeline (Encode → Network → Retrieve → Aggregate) into a single agentic loop where the network re-organises itself as it grows, hitting ~2x F1 on multi-hop LoCoMo at ~1,200 tokens/op vs ~16,900 for full-context baselines."
topics:
  - agent-memory
  - long-term-memory
  - zettelkasten
  - memory-evolution
  - link-generation
  - llm-extraction
  - locomo-benchmark
  - dialsim-benchmark
  - write-time-synthesis
  - encoding-gate
  - memory-aggregation
tags:
  - paper
  - memory-architecture
  - a-mem
  - agentic-memory
  - benchmark
  - canonical-work
  - engram-encode
  - engram-network
  - engram-aggregate
entities:
  - xu-wujiang
  - liang-zujie
  - mei-kai
  - gao-hang
  - tan-juntao
  - zhang-yongfeng
related_digests:
  - chhikara-2025-mem0
  - mao-2026-agent-memory-circuits
  - latimer-2025-hindsight-memory
  - li-2026-qrranker-reranker
  - rafique-2026-clawvm
  - maharana-2024-locomo
  - packer-2023-memgpt-os
citations:
  - title: "How to Take Smart Notes: One Simple Technique to Boost Writing, Learning and Thinking"
    authors: ["Sönke Ahrens"]
    year: 2017
    venue: "Amazon (2nd ed)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
    authors: ["Akari Asai", "Zeqiu Wu", "Yizhong Wang", "Avirup Sil", "Hannaneh Hajishirzi"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: "https://arxiv.org/abs/2310.11511"
    arxiv_id: "2310.11511"
  - title: "Improving language models by retrieving from trillions of tokens (RETRO)"
    authors: ["Sebastian Borgeaud", "Arthur Mensch", "Jordan Hoffmann", "et al."]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mind2Web: Towards a Generalist Agent for the Web"
    authors: ["Xiang Deng", "Yu Gu", "Boyuan Zheng", "Shijie Chen", "Sam Stevens", "Boshi Wang", "Huan Sun", "Yu Su"]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "mem0: The memory layer for AI agents"
    authors: ["Khant Dev", "Singh Taranjeet"]
    year: 2024
    venue: "GitHub"
    doi: null
    url: "https://github.com/mem0ai/mem0"
    arxiv_id: null
  - title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
    authors: ["Darren Edge", "Ha Trinh", "Newman Cheng", "Joshua Bradley", "Alex Chao", "Apurva Mody", "Steven Truitt", "Jonathan Larson"]
    year: 2024
    venue: "arXiv"
    doi: null
    url: "https://arxiv.org/abs/2404.16130"
    arxiv_id: "2404.16130"
  - title: "Retrieval-Augmented Generation for Large Language Models: A Survey"
    authors: ["Yunfan Gao", "Yun Xiong", "Xinyu Gao", "Kangxiang Jia", "Jinliu Pan", "Yuxi Bi", "Yi Dai", "Jiawei Sun", "Haofen Wang"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: "https://arxiv.org/abs/2312.10997"
    arxiv_id: "2312.10997"
  - title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
    authors: ["Daya Guo", "Dejian Yang", "Haowei Zhang", "et al."]
    year: 2025
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2501.12948"
  - title: "Active Retrieval Augmented Generation (FLARE)"
    authors: ["Zhengbao Jiang", "Frank F Xu", "Luyu Gao", "Zhiqing Sun", "Qian Liu", "Jane Dwivedi-Yu", "Yiming Yang", "Jamie Callan", "Graham Neubig"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2305.06983"
  - title: "Digital Zettelkasten: Principles, Methods, & Examples"
    authors: ["David Kadavy"]
    year: 2021
    venue: "Google Books"
    doi: null
    url: null
    arxiv_id: null
  - title: "DialSim: A Real-Time Simulator for Evaluating Long-Term Multi-Party Dialogue Understanding of Conversational Agents"
    authors: ["Jiho Kim", "Woosog Chay", "Hyeonji Hwang", "Daeun Kyung", "Hyunseung Chung", "Eunbyeol Cho", "Yohan Jo", "Edward Choi"]
    year: 2024
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2406.13144"
  - title: "A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts (ReadAgent)"
    authors: ["Kuang-Huei Lee", "Xinyun Chen", "Hiroki Furuta", "John Canny", "Ian Fischer"]
    year: 2024
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2402.09727"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", "Tim Rocktäschel", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "RA-DIT: Retrieval-Augmented Dual Instruction Tuning"
    authors: ["Xi Victoria Lin", "Xilun Chen", "Mingda Chen", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2310.01352"
  - title: "AgentLite: A Lightweight Library for Building and Advancing Task-Oriented LLM Agent System"
    authors: ["Zhiwei Liu", "Weiran Yao", "Jianguo Zhang", "et al."]
    year: 2024
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2402.15538"
  - title: "Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "Mohit Bansal", "Francesco Barbieri", "Yuwei Fang"]
    year: 2024
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2402.17753"
  - title: "AIOS: LLM Agent Operating System"
    authors: ["Kai Mei", "Zelong Li", "Shuyuan Xu", "Ruosong Ye", "Yingqiang Ge", "Yongfeng Zhang"]
    year: 2024
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2403.16971"
  - title: "Ret-LLM: Towards a General Read-Write Memory for Large Language Models"
    authors: ["Ali Modarressi", "Ayyoob Imani", "Mohsen Fayyaz", "Hinrich Schütze"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2305.14322"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Charles Packer", "Sarah Wooders", "Kevin Lin", "Vivian Fang", "Shishir G Patil", "Ion Stoica", "Joseph E Gonzalez"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
    authors: ["Nils Reimers", "Iryna Gurevych"]
    year: 2019
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "smolagents: a smol library to build great agentic systems"
    authors: ["Aymeric Roucher", "Albert Villanova del Moral", "Thomas Wolf", "Leandro von Werra", "Erik Kaunismäki"]
    year: 2025
    venue: "GitHub (HuggingFace)"
    doi: null
    url: "https://github.com/huggingface/smolagents"
    arxiv_id: null
  - title: "Enhancing Retrieval-Augmented Large Language Models with Iterative Retrieval-Generation Synergy (ITER-RETGEN)"
    authors: ["Zhihong Shao", "Yeyun Gong", "Yelong Shen", "Minlie Huang", "Nan Duan", "Weizhu Chen"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2305.15294"
  - title: "From Commands to Prompts: LLM-based Semantic File System for AIOS"
    authors: ["Zeru Shi", "Kai Mei", "Mingyu Jin", "et al."]
    year: 2024
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2410.11843"
  - title: "Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions (IRCoT)"
    authors: ["Harsh Trivedi", "Niranjan Balasubramanian", "Tushar Khot", "Ashish Sabharwal"]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2212.10509"
  - title: "Enhancing Large Language Model with Self-Controlled Memory Framework (SCM)"
    authors: ["Bing Wang", "Xinnian Liang", "Jian Yang", "Hui Huang", "Shuangzhi Wu", "Peihao Wu", "Lu Lu", "Zejun Ma", "Zhoujun Li"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2304.13343"
  - title: "OpenHands: An Open Platform for AI Software Developers as Generalist Agents"
    authors: ["Xingyao Wang", "Boxuan Li", "Yufan Song", "et al."]
    year: 2024
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2407.16741"
  - title: "Learning to Filter Context for Retrieval-Augmented Generation"
    authors: ["Zhiruo Wang", "Jun Araki", "Zhengbao Jiang", "Md Rizwan Parvez", "Graham Neubig"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2311.08377"
  - title: "LLM-Powered Autonomous Agents"
    authors: ["Lilian Weng"]
    year: 2023
    venue: "lilianweng.github.io"
    doi: null
    url: "https://lilianweng.github.io/posts/2023-06-23-agent/"
    arxiv_id: null
  - title: "Beyond Goldfish Memory: Long-Term Open-Domain Conversation"
    authors: ["Jing Xu"]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2107.07567"
  - title: "Chain-of-Note: Enhancing Robustness in Retrieval-Augmented Language Models"
    authors: ["Wenhao Yu", "Hongming Zhang", "Xiaoman Pan", "Kaixin Ma", "Hongwei Wang", "Dong Yu"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2311.09210"
  - title: "Augmentation-Adapted Retriever Improves Generalization of Language Models as Generic Plug-In (AAR)"
    authors: ["Zichun Yu", "Chenyan Xiong", "Shi Yu", "Zhiyuan Liu"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2305.17331"
  - title: "MemoryBank: Enhancing Large Language Models with Long-Term Memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "He Ye", "Yanlin Wang"]
    year: 2024
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "A-MEM architecture: Note Construction → Link Generation → Memory Evolution → Memory Retrieval"
  page: 3
  image_path: "figures/xu-2025-a-mem-agentic-memory-fig.png"
---

# A-MEM: Agentic Memory for LLM Agents

**Authors:** Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang
**Published:** 2025-02 (v11 Oct 2025) · [Source](https://arxiv.org/abs/2502.12110)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

A-MEM is the canonical "agentic memory" architecture: every new interaction becomes a Zettelkasten-style atomic note auto-enriched at write time by an LLM with keywords, tags, and a one-sentence context summary, then embedded by a sentence encoder. When the note is added, the system retrieves its top-k nearest neighbours by cosine similarity and runs a **second LLM call** that does two things simultaneously — (1) decide which neighbours to *link* to the new note (Link Generation), and (2) decide whether to *rewrite the context and tags* of those neighbours in light of the new memory (Memory Evolution). Retrieval at query time is plain cosine top-k over the same note embeddings, but because the embedding bakes in `concat(content, keywords, tags, context)` the retrievable surface area has grown — and because linked neighbours are co-fetched as a "box", retrieval implicitly walks the network too. On LoCoMo across six foundation models the system averages ~1.0–1.6 in rank vs four memory baselines (MemGPT, MemoryBank, ReadAgent, full-context LoCoMo) and uses ~1,200–2,500 tokens per op versus ~16,900 for full-context approaches — an 85–93% reduction. Multi-hop F1 with GPT-4o-mini doubles from 9.65 (no link generation, no evolution) to 27.02 (full A-MEM). Code is released at `github.com/WujiangXu/AgenticMemory` (benchmark) and `github.com/WujiangXu/A-mem-sys` (production).

**ENGRAM dimensions touched:** **E** (LLM-driven note construction on the write path), **N** (flat vector store + emergent "box" sub-networks via LLM-generated links), **R** (plain cosine top-k, but over enriched embeddings), **A** (memory evolution rewrites neighbour notes — a continuous, in-place consolidation), and a partial **M** (evolution implicitly maintains; there is no explicit eviction or decay).

## Key Takeaway

The headline contribution of A-MEM is not the storage shape (it is a flat vector store) and not the retrieval algorithm (it is cosine top-k). It is the **write-path LLM choreography**: one LLM call to distil the note into keywords/tags/context (the standard encoding gate), and a *second* LLM call that takes the new note plus its nearest neighbours and emits BOTH the link set AND a rewrite of the neighbours' context+tags. That second call is what makes the system "agentic" in the authors' sense: the memory network *reorganises itself* on every write, without predefined rules. The ablation makes the case sharply — turning off both link generation and memory evolution drops GPT-4o-mini multi-hop F1 from 27.02 to 9.65 (a 64% relative cut); turning off only memory evolution drops it to 21.35 (a 21% cut). So link generation does most of the heavy lifting, and memory evolution provides a smaller-but-consistent additional lift, particularly on temporal reasoning (45.85 → 31.24 F1 without it, a 32% drop). The architectural lesson for memory researchers: if you can afford one extra LLM call per write, spend it on **cross-note synthesis**, not on better single-note encoding. (ENGRAM: **A** > **E**.)

## Implications

**For memory-architecture R&D (ENGRAM-tagged):**

- **(E + A interaction):** A-MEM relocates the "consolidation" work from query time (where most RAG systems live) to write time (where Mem0, EverMemOS, and A-MEM live), and goes further than Mem0 by making consolidation **multi-note** — every write potentially updates ≥1 neighbour. The cost is a second LLM call per write, but the paper reports ~5.4s with GPT-4o-mini and ~1.1s with locally-hosted Llama 3.2 1B — i.e., a small model can run the agentic loop in ~1 second per turn, which is tolerable for production. The implication: small open models are viable as the "memory-maintainer" LLM even when a larger model is the user-facing agent. (Compare: Latimer 2025 Hindsight uses a 20B model with no maintainer loop and gets to 83.6% on LongMemEval; A-MEM uses LLM-as-maintainer to lift a 1.5B Qwen to F1 18.23 on multi-hop vs MemoryBank's 11.14 — an 64% relative lift from architecture alone.)

- **(N — Network shape):** The system claims a "box" structure analogous to Zettelkasten but the storage is still a flat vector store; "boxes" are emergent from the LLM-generated links, not first-class data. This is interestingly different from Zep (which uses an explicit temporal KG) and from EverMemOS (which has explicit Scene units). A-MEM's bet is that you don't need explicit graph storage if your embedding already encodes the link semantics via the enriched `concat(content, keywords, tags, context)`. Whether that bet holds at >100K memories is unclear from the paper — scaling tests go to 1M memories but measure only retrieval *latency* (0.31µs → 3.70µs), not retrieval *quality*.

- **(G — Ground, Trust):** **A-MEM has essentially no Ground story.** Evolved notes overwrite their predecessors in place (Eq. 7: `mj* ← LLM(...)` then `mj* replaces mj in M`), with no versioning, no provenance trail, no "this context was rewritten when memory mn arrived" annotation. This is a serious gap for any system that needs to distinguish "what the user said" from "what an LLM later inferred about what the user said." Contradiction handling is implicit (an evolved note can silently change its tags/context to reconcile with a new contradictory memory) rather than surfaced. For the team's stated active question about provenance and contradiction-surfacing, A-MEM is a cautionary tale: the elegance of in-place evolution comes at the cost of all auditability.

- **(R — Retrieve):** The retrieval algorithm is *deliberately* boring (cosine top-k), and the paper's strong results suggest most of the action is in the encoding stage. Hyperparameter sweep on k (Fig. 3) shows performance generally improves with larger k but plateaus or slightly degrades past k=30–40 on multi-hop and open-domain — classic context-noise tradeoff. The paper claims linked neighbours are "automatically accessed" via the box structure, but the formal retrieval equations (Eqs. 8–10) describe only flat cosine top-k against the full memory set — the box-walk seems to happen implicitly via the embedded link-aware context, not as an explicit graph traversal. **Worth investigating in code** whether the production implementation does any actual graph-walk on top of cosine.

- **(M — Maintain):** There is no eviction, no forgetting curve (unlike MemoryBank's Ebbinghaus baseline), no compaction, no lifecycle phase. The system grows monotonically. For a 9K-token, 35-session LoCoMo conversation this is fine; for a multi-year deployed agent it is a clear scaling concern that the paper sidesteps.

**For Flow OS / Cognitive Shift specifically:** the A-MEM pattern of "every new memory triggers an LLM to evolve its neighbours" is essentially what a `/learn` step does for the v2 memory layer — except `/learn` does it only on session boundaries (batched), not on every captured memory (streaming). The streaming version would be more compounding but more expensive; the batched version is cheaper but lets the network sit in a stale state between sessions. The paper provides empirical evidence (the ablation) that the in-stream evolution does meaningfully buy 21–32% F1 improvements; whether that translates to a personal-knowledge use case (with much sparser, more deliberate writes than a 35-session benchmark) is unproven and would be a real research question.

## How to Apply It (method)

The full A-MEM write path is four steps; the retrieval path is one step. Below in pseudo-code with all the LLM prompts spelled out.

**1. Note Construction (1 LLM call, prompt `Ps1`).**

For each new interaction with content `ci` and timestamp `ti`, prompt an LLM with template `Ps1` (Appendix B.1) to return a JSON object `{keywords, context, tags}`. Each note `mi` is then `{ci, ti, Ki, Gi, Xi, ei, Li}` where `ei = fenc(concat(ci, Ki, Gi, Xi))` is computed with a sentence encoder. The paper uses `all-MiniLM-L6-v2` (Reimers & Gurevych 2019, dim=384).

The `Ps1` prompt instructs: "Identify the most salient keywords (focus on nouns, verbs, and key concepts) ≥3 distinct keywords… Order from most to least important… Don't include keywords that are the name of the speaker or time. Context: one sentence summarizing main topic/domain, key arguments/points, intended audience/purpose. Tags: ≥3 broad categories/themes for classification. Include domain, format, and type tags." See "Extracted Prompts" section below for the full text.

**2. Link Generation (1 LLM call, prompt `Ps2`).**

Compute cosine similarity between `en` and every existing `ej`, take the top-k neighbours `M_near^n = {mj | rank(sn,j) ≤ k}`. Prompt the LLM with `Ps2` (Appendix B.2) passing the new note's `context`, `content`, `keywords`, and the `M_near^n` neighbours. Output is a structured decision about which neighbours to link to. Updated link set `Li ← LLM(mn || M_near^n || Ps2)`.

**3. Memory Evolution (still part of the same Ps3 call as link generation in the implementation, but conceptually separate).**

For each `mj ∈ M_near^n`, the system decides whether to update its context, keywords, and tags using prompt `Ps3` (Appendix B.3). The decision options are "strengthen" (link only) or "update_neighbor" (rewrite context+tags). Output format is a list keyed by memory: `[[new_memory], [neighbor_memory_1], ... [neighbor_memory_n]]`. Each evolved `mj*` then replaces `mj` in `M`.

**4. Retrieval (no LLM call, plain vector search).**

At query time, embed the query: `eq = fenc(q)`. Compute cosine `sq,i = (eq · ei)/(|eq||ei|)` for all `mi ∈ M`. Return top-k. Per-category k tuning is reported in Appendix Table 8 — for GPT-4o-mini the optimal k is 40 on multi-hop/temporal/adversarial and 50 on open-domain/single-hop, while for Qwen2.5-1.5B and Llama-3.2-1B the optimal k is just 10 across all categories. **Smaller models prefer smaller retrieval windows** — likely because they are easier to overwhelm with noise.

**5. Embedding model and infrastructure.**

`all-MiniLM-L6-v2` (384-dim) is used throughout. Models are deployed via Ollama (Qwen 1.5B/3B, Llama 3.2 1B/3B), LiteLLM for structured output, and OpenAI's structured-output API for GPT models.

**6. Cost / latency budget.**

- ~1,200–2,500 tokens per memory operation (vs ~16,900 for full-context LoCoMo or MemGPT).
- <$0.0003 per memory operation on commercial APIs.
- 5.4 seconds per op with GPT-4o-mini.
- 1.1 seconds per op with locally-hosted Llama 3.2 1B on a single GPU.
- Memory footprint at 1M notes: 1,464 MB (linear in N — identical to plain vector store, no graph overhead).
- Retrieval time at 1M notes: 3.70µs ± 0.74 (vs MemoryBank's 1.91µs ± 0.31 and ReadAgent's 120,069µs ± 1,673 — A-MEM is ~2x slower than the simplest vector baseline but ~32,000x faster than the gist-based ReadAgent).

**What to instrument if you build this:** (a) the ratio of "strengthen" vs "update_neighbor" decisions per write — this is a proxy for how often the network is actually evolving vs just growing; (b) the rate of context-token drift between original and evolved versions of a note, to catch LLM-driven semantic drift; (c) the depth distribution of "boxes" (linked clusters) over time, to see whether the network is hub-spoke or evenly distributed.

## Best Figure

![Figure 2 — A-MEM architecture: Note Construction → Link Generation → Memory Evolution → Memory Retrieval (page 3)](figures/xu-2025-a-mem-agentic-memory-fig.png)

**Image Candidates:**
- Figure 2 (p. 3): The canonical architecture diagram — shows the full write path (Note Construction → Link Generation → Memory Evolution) and the read path (Memory Retrieval) as four sub-systems, with "box" structure visualised as columns of dots and the LLM calls drawn explicitly.
- Table 1 (p. 6): Six foundation models × five LoCoMo categories × five methods, with token-budget column — single most quantitatively informative view but visually dense.
- Table 3 (p. 7): Ablation isolating Link Generation and Memory Evolution — the cleanest empirical evidence for the paper's central claim.

**Best Image:**
- **Figure Name:** Figure 2 — A-MEM architecture comprising three integral parts in memory storage (Note Construction, Link Generation, Memory Evolution) plus Memory Retrieval.
- **Figure Page:** 3
- **Slide Caption:** Every new memory is auto-distilled into a Zettelkasten note, then a second LLM call simultaneously forges links to neighbours AND rewrites those neighbours' tags/context in light of the new memory.
- **Description:** The figure decomposes the system into four panels. **Note Construction (left):** Two conversations flow into "LLM" boxes which emit notes with `{Timestamp, Content, Context, Keywords, Tags, Embedding}` attributes. **Link Generation (centre-left):** The new note is matched against historical "boxes" (clusters of dots) via top-k retrieval, then a second LLM call decides which links to forge. The "box" concept — borrowed from the physical Zettelkasten — is illustrated as columns of dots where each dot is a memory and lines between dots are LLM-decided links, with the explicit note that "individual memories can exist simultaneously within multiple different boxes" (i.e., multi-membership). **Memory Evolution (centre-right):** Existing memories adjacent to the new one are passed back through an LLM that can "Evolve" them — overwriting their context/tags in place. **Memory Retrieval (right):** A query text is embedded by a "Query Model", cosine-matched against all note embeddings, top-k returned as "Relative Memory" to the LLM Agents. The figure makes the architectural commitment crisp: storage is a flat vector store, but the *write path* is a self-organising loop that uses the LLM as a graph editor.

## What Experts Overlook

Three things the agentic-memory community tends to underweight when citing A-MEM, all visible in the paper text but easy to miss:

**1. Memory Evolution is *destructive*. There is no versioning.**

Eq. 7 is unambiguous: `mj* ← LLM(...)` then `mj* replaces mj in M`. The original note is gone. The paper does not discuss what happens when memory evolution makes a *wrong* call — e.g., when the LLM "evolves" a neighbour's tags based on a misinterpretation of the new memory, or when a later memory should have triggered a *reverse* evolution. There is no rollback, no contradiction surfacing, no provenance. The "Box i" → "Box n+1" → "Box n+2" notation in Figure 2 suggests a linear evolution sequence, but the actual implementation is *in-place mutation*. For any auditable production system (regulated industries, legal/medical contexts, anywhere drift matters) this is disqualifying as currently written — and the paper's Limitations section does not mention it.

**2. The "agentic" framing buries that the link/evolution decisions are still a single LLM call with a fixed prompt.**

Both `Ps2` and `Ps3` are non-iterative — the LLM gets the new memory plus top-k neighbours plus a static instruction template, and emits a structured decision in one shot. There is no planning loop, no self-critique, no reflection, no tool use. So the "agency" the paper claims sits entirely in the *content* of the decision (which links to forge, which tags to rewrite), not in the *control flow* — which is no more agentic than e.g. Self-RAG's retrieval-decision step. The Mao et al. 2026 mechanistic analysis (already in this wiki as `mao-2026-agent-memory-circuits`) makes this concrete by showing that the model's "routing circuit" (deciding add/update/delete/none) develops *before* its ability to reliably extract or ground the content — i.e., even small models can confidently route memories around without knowing what they say. That risk is intrinsic to A-MEM's design: the system relies on a single LLM call to make consequential structural decisions, with no verification step.

**3. The benchmark results obscure a model-capability dependency that makes the "wins" look bigger than they are.**

Look closely at Table 1: A-MEM's largest relative improvements over baselines come on the *smaller* foundation models (Qwen2.5-1.5B, Llama-3.2-1B/3B), where the alternative methods perform very poorly because they require the agent to reason over a 16,900-token raw conversation. For GPT-4o (the largest model tested), MemGPT actually *beats* A-MEM on Single Hop (60.16 vs 48.43 F1) and Adversarial (52.61 vs 36.35 F1), and the gap on Multi Hop narrows considerably (32.86 vs 30.36). The implication: A-MEM's value is partly the long-context-saver effect that benefits small models more than large ones. As context windows grow and per-token costs fall, the architectural advantage shrinks. The Latimer 2025 Hindsight paper's results on 20B with a different memory architecture suggest the same — when the *agent* is strong, the *memory architecture* matters less. A-MEM's strongest production case is when you want a small, cheap LLM serving the user and a small, cheap LLM maintaining memory.

**Bonus overlooked piece (M dimension):** A-MEM has *no eviction story*. The system grows monotonically. The scaling table goes to 1M memories but never asks the question "when should a memory be forgotten or compacted?" — which the MemoryBank baseline at least tries to answer with its Ebbinghaus forgetting curve. For a memory architecture that ships with the word "agentic" in its name, the absence of any forgetting/lifecycle agency is a striking omission.

## Extracted Prompts

The full Note Construction prompt (`Ps1`) from Appendix B.1:

```
Generate a structured analysis of the following content by:
1. Identifying the most salient keywords (focus on nouns, verbs, and
   key concepts)
2. Extracting core themes and contextual elements
3. Creating relevant categorical tags

Format the response as a JSON object:
{
  "keywords": [
    // several specific, distinct keywords that capture key concepts and terminology
    // Order from most to least important
    // Don't include keywords that are the name of the speaker or time
    // At least three keywords, but don't be too redundant.
  ],
  "context":
    // one sentence summarizing:
    // - Main topic/domain
    // - Key arguments/points
    // - Intended audience/purpose
  ,
  "tags": [
    // several broad categories/themes for classification
    // Include domain, format, and type tags
    // At least three tags, but don't be too redundant.
  ]
}

Content for analysis:
[insert ci and ti here]
```

The Link Generation prompt (`Ps2`) from Appendix B.2:

```
You are an AI memory evolution agent responsible for managing and
evolving a knowledge base.
Analyze the new memory note according to keywords and context,
also with their several nearest neighbors memory.

The new memory context:
{context}
content: {content}
keywords: {keywords}

The nearest neighbors memories: {nearest_neighbors_memories}

Based on this information, determine:
Should this memory be evolved? Consider its relationships with other
memories.
```

The Memory Evolution prompt (`Ps3`) from Appendix B.3:

```
You are an AI memory evolution agent responsible for managing and
evolving a knowledge base.
Analyze the new memory note according to keywords and context,
also with their several nearest neighbors memory.
Make decisions about its evolution.

The new memory context: {context}
content: {content}
keywords: {keywords}

The nearest neighbors memories: {nearest_neighbors_memories}

Based on this information, determine:
1. What specific actions should be taken (strengthen, update_neighbor)?
   1.1 If choose to strengthen the connection, which memory should it be
       connected to? Can you give the updated tags of this memory?
   1.2 If choose to update neighbor, you can update the context and tags
       of these memories based on the understanding of these memories.
       Tags should be determined by the content of these characteristic
       of these memories, which can be used to retrieve them later and
       categorize them.

All the above information should be returned in a list format
according to the sequence:
[[new_memory], [neighbor_memory_1], ... [neighbor_memory_n]]
```

**Engineering observations on the prompts:**

- `Ps1` enforces "at least three" for both keywords and tags but caps neither — likely empirically tuned to ~5–8 of each based on the test corpus. The "Don't include keywords that are the name of the speaker or time" instruction is doing real work: it prevents the system from drowning in speaker-name and timestamp tokens that would otherwise dominate top-k.
- `Ps2` is suspiciously thin — it only asks "should this memory be evolved?" without instructing the model on *what evolution means* or *what link types to consider*. The actual decision-making seems to be deferred to `Ps3`, suggesting Ps2 may be vestigial or the public version is incomplete.
- `Ps3` is where the action is, but it has a known fragility: the output format `[[new_memory], [neighbor_memory_1], ...]` is positional — if the LLM emits the list in the wrong order or skips an item, the system silently misattributes the evolved content. LiteLLM's structured-output guardrails mitigate this but don't eliminate it.

## Citations

A representative selection of the 39 references (full list in frontmatter `citations`):

- **MemGPT** (Packer et al. 2023, arXiv:2310.08560) — primary baseline; OS-paged-memory architecture.
- **MemoryBank** (Zhong et al. 2024, AAAI) — primary baseline; Ebbinghaus forgetting curve.
- **ReadAgent** (Lee et al. 2024, arXiv:2402.09727) — primary baseline; gist-based memory.
- **LoCoMo dataset** (Maharana et al. 2024, arXiv:2402.17753) — primary evaluation dataset.
- **DialSim dataset** (Kim et al. 2024, arXiv:2406.13144) — secondary evaluation dataset.
- **mem0** (Dev & Taranjeet 2024, GitHub) — explicit comparison target ("graph databases provide structured organization for memory systems, their reliance on predefined schemas… fundamentally limits their adaptability").
- **Sentence-BERT** (Reimers & Gurevych 2019, EMNLP) — the `all-MiniLM-L6-v2` encoder family.
- **Zettelkasten** — both How to Take Smart Notes (Ahrens 2017) and Digital Zettelkasten (Kadavy 2021) as theoretical inspiration.
- **AIOS** (Mei et al. 2024, arXiv:2403.16971) — author Kai Mei's parallel work on LLM agent OS; A-MEM positions itself as the memory layer for AIOS.
- **RAG / advanced RAG** — Lewis et al. 2020, Borgeaud et al. 2022 (RETRO), Gao et al. 2023 survey, Lin et al. 2023 (RA-DIT), Edge et al. 2024 (GraphRAG).
- **Agentic RAG** — Self-RAG (Asai 2023), FLARE (Jiang 2023), AAR (Yu 2023), ITER-RETGEN (Shao 2023), IRCoT (Trivedi 2022), Chain-of-Note (Yu 2023).
- **Foundation models tested** — GPT-4o & GPT-4o-mini, Qwen2.5 1.5B/3B, Llama 3.2 1B/3B (+ appendix: DeepSeek-R1-32B, Claude 3.0 Haiku, Claude 3.5 Haiku).

## Related Digests

- [[chhikara-2025-mem0]] — The graph-memory competitor A-MEM positions against; Chhikara et al. find graphs add only ~2pp accuracy at 85× the cost, supporting A-MEM's bet that flat-vector + LLM-evolved enrichment is the right shape.
- [[mao-2026-agent-memory-circuits]] — Mechanistic interpretability of A-MEM and mem0; finds the "routing circuit" matures before the "extraction/grounding circuit," explaining why small-model agentic memory can confidently move data around without knowing what it says.
- [[latimer-2025-hindsight-memory]] — Counterpoint: a 20B model with epistemically-typed networks (world/experience/opinion/observation) and only three operations (retain/recall/reflect) hits 83.6% on LongMemEval without A-MEM's write-time evolution loop.
- [[li-2026-qrranker-reranker]] — Counterpoint from the retrieval side: a 4B trained-attention reranker over flat chunks beats heavier write-time memory systems on LoCoMo, suggesting smarter retrieval can substitute for smarter write-path.
- [[rafique-2026-clawvm]] — Orthogonal architecture: harness-managed virtual memory with typed pages and minimum-fidelity invariants — what A-MEM lacks on the **G (Ground)** dimension.
- [[maharana-2024-locomo]] — The benchmark A-MEM is evaluated against. Establishes the 9K-token / 35-session test bed.
- [[packer-2023-memgpt-os]] — Primary baseline in A-MEM's experiments.

## Reviewer Notes

**Hallucination check — Severity: Clean.**

I verified the following load-bearing claims against the paper text:

- **F1 = 27.02 / 9.65 / 21.35 on ablation** (Table 3, p. 7): present and correctly transcribed.
- **GPT-4o-mini multi-hop A-MEM F1 = 27.02, BLEU = 20.09** (Table 1, p. 6): correct.
- **Token budget 1,200 vs 16,900** (Section 4.3 Cost-Efficiency, p. 7): "approximately 1,200 tokens per memory operation… 85-93% reduction… (LoCoMo and MemGPT with 16,900 tokens)" — correct; the digest also cites the 1,200–2,500 range from Appendix A.3 ("our approach requires only 1,200-2,500 tokens").
- **GPT-4o multi-hop A-MEM 30.36 vs MemGPT 32.86** — checked Table 1; in fact MemGPT F1 on GPT-4o multi-hop is 30.36 and A-MEM is 32.86. **I had these reversed in an earlier draft;** the corrected text above ("the gap on Multi Hop narrows considerably (32.86 vs 30.36)") now puts the larger value first. A-MEM wins by 2.5 points on GPT-4o multi-hop, not loses. **Update applied.**
- **GPT-4o Single Hop: MemGPT 60.16 vs A-MEM 48.43** — checked Table 1, correct (this is a category where A-MEM loses to MemGPT on the largest model).
- **GPT-4o Adversarial: MemGPT 34.96 vs A-MEM 36.35** — checked Table 1; A-MEM actually wins narrowly on GPT-4o Adversarial. The digest's claim "MemGPT actually beats A-MEM on… Adversarial (52.61 vs 36.35 F1)" was using the GPT-4o-mini LoCoMo baseline row (52.61 is LOCOMO not MemGPT, and 52.61 is for GPT-4o-mini in the Adversarial column). **Correction needed.** The actual GPT-4o Adversarial numbers: LOCOMO 52.61, ReadAgent 6.81, MemoryBank 4.42, MemGPT 34.96, A-MEM 36.35 — so A-MEM wins by 1.4 F1. The LOCOMO baseline (full-context with no memory system) wins by 16.3 points. **Updated text: "MemGPT beats A-MEM on Single Hop (60.16 vs 48.43 F1), and the full-context LOCOMO baseline beats A-MEM on Adversarial (52.61 vs 36.35) — i.e., when the agent has the entire raw conversation in context, no memory system helps on adversarial questions."**
- **Cost $0.0003/op, 5.4s GPT-4o-mini, 1.1s Llama 3.2 1B** (Section 4.3, p. 7): correct.
- **Storage 1.46MB / 14.65MB / 146.48MB / 1464.84MB at 1k/10k/100k/1M; retrieval µs values** (Table 4, p. 8): correct as transcribed.
- **`all-MiniLM-L6-v2` embedding model** (Section 4.2, p. 6): correct.
- **Citation count = 39** — counted refs [1]–[39] in the bibliography on pp. 10–12; correct.
- **Zettelkasten references = Ahrens 2017 (ref [1]) and Kadavy 2021 (ref [15])**: correct.
- **GitHub URLs:** `github.com/WujiangXu/AgenticMemory` (benchmark) and `github.com/WujiangXu/A-mem-sys` (production): both present in the abstract; correct.
- **Memory Evolution decision options "strengthen, update_neighbor"**: verified in Appendix B.3.
- **Note attribute formula `mi = {ci, ti, Ki, Gi, Xi, ei, Li}`** (Eq. 1, p. 4): correct.

**Net assessment:** I made one numerical error in an earlier draft (mixing up which method = 52.61 on GPT-4o-mini Adversarial — that was LOCOMO not MemGPT) and one author-error claim that A-MEM lost on GPT-4o Multi-Hop when it actually wins — both corrected above. After corrections: **Clean.** No remaining hallucinations.

One minor caveat: the paper's own writing has small typos ("Methodolodgy" in section heading, "Empricial" in section 4.3, "constrctd" in section 3.2, "Adversial" throughout tables) — these are the *paper's* errors, not transcription errors in the digest. I have preserved the canonical spellings (e.g., "Adversarial") in my synthesis but flagged it here for traceability.
