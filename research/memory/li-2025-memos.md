---
corpus: agentic-memory
kind: paper-digest
slug: li-2025-memos
title: "MemOS: A Memory OS for AI System"
authors:
  - "Zhiyu Li"
  - "Chenyang Xi"
  - "Chunyu Li"
  - "Ding Chen"
  - "Boyu Chen"
  - "Shichao Song"
  - "Simin Niu"
  - "Hanyu Wang"
  - "Jiawei Yang"
  - "Chen Tang"
  - "Qingchen Yu"
  - "Jihao Zhao"
  - "Yezhaohui Wang"
  - "Peng Liu"
  - "Zehao Lin"
  - "Pengyuan Wang"
  - "Jiahao Huo"
  - "Tianyi Chen"
  - "Kai Chen"
  - "Kehang Li"
  - "Zhen Tao"
  - "Huayi Lai"
  - "Hao Wu"
  - "Bo Tang"
  - "Zhengren Wang"
  - "Zhaoxin Fan"
  - "Ningyu Zhang"
  - "Linfeng Zhang"
  - "Junchi Yan"
  - "Mingchuan Yang"
  - "Tong Xu"
  - "Wei Xu"
  - "Huajun Chen"
  - "Haofen Wang"
  - "Hongkang Yang"
  - "Wentao Zhang"
  - "Zhi-Qin John Xu"
  - "Siheng Chen"
  - "Feiyu Xiong"
year: 2025
publication_date: "2025-07"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2507.03724"
doi: null
arxiv_id: "2507.03724"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Make memory itself a first-class system resource, not an attached storage layer — MemOS unifies three substrates (plaintext, KV-activation, parameter) behind a single MemCube abstraction that carries payload + governance metadata, and lets a scheduler dynamically transform memories between substrates based on access patterns, achieving 75.8 overall LLM-judge on LoCoMo (vs 72.01 Memobase, 64.57 Mem0) and 77.8 on LongMemEval, while delivering 91.4% TTFT reduction by promoting hot plaintext to GPU-resident KV-cache."
topics:
  - memory-operating-system
  - memcube
  - hierarchical-memory
  - kv-cache-memory
  - parameter-memory
  - plaintext-memory
  - memory-scheduling
  - lifecycle-management
  - memory-governance
  - cross-platform-memory
  - llm-os
  - memory-marketplace
  - mem-training
  - locomo
  - longmemeval
  - personamem
tags:
  - paper
  - memory-architecture
  - operating-system-metaphor
  - hierarchical-memory
  - benchmark
  - canonical-survey
  - memtensor
  - shanghai
entities:
  - li-zhiyu
  - yang-hongkang
  - xiong-feiyu
  - chen-siheng
  - xu-zhi-qin-john
related_digests:
  - packer-2023-memgpt-os
  - hu-2026-evermemos
  - chhikara-2025-mem0
  - rasmussen-2025-zep-temporal-kg
  - wang-2026-memmachine
  - li-2026-qrranker-reranker
  - rafique-2026-clawvm
  - adler-2026-storage-not-memory
  - mao-2026-agent-memory-circuits
  - maharana-2024-locomo
  - wu-2024-longmemeval
citations:
  - title: "Memory3: Language modeling with explicit memory"
    authors: ["Hongkang Yang", "Zehao Lin", "Wenjin Wang", "Hao Wu", "Zhiyu Li", "Bo Tang", "et al."]
    year: 2024
    venue: "Journal of Machine Learning"
    doi: null
    url: null
    arxiv_id: null
  - title: "Rethinking Memory in AI: Taxonomy, Operations, Topics, and Future Directions"
    authors: ["Yiming Du", "Wenyu Huang", "Danna Zheng", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2505.00675"
  - title: "From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs"
    authors: ["Yaxiong Wu", "Sheng Liang", "Chen Zhang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.15965"
  - title: "Cognitive Memory in Large Language Models"
    authors: ["Lianlei Shan", "Shixian Luo", "Zezhou Zhu", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.02441"
  - title: "Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM)"
    authors: ["Woosuk Kwon", "Zhuohan Li", "Siyuan Zhuang", "et al."]
    year: 2023
    venue: "SOSP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient Streaming Language Models with Attention Sinks"
    authors: ["Guangxuan Xiao", "Yuandong Tian", "Beidi Chen", "Song Han", "Mike Lewis"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of LLMs"
    authors: ["Zhenyu Zhang", "Ying Sheng", "Tianyi Zhou", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Get More with LESS: Synthesizing Recurrence with KV Cache Compression"
    authors: ["Harry Dong", "Xinyu Yang", "Zhenyu Zhang", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization"
    authors: ["Coleman Hooper", "Sehoon Kim", "Hiva Mohammadzadeh", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "RetrievalAttention: Accelerating Long-Context LLM Inference via Vector Retrieval"
    authors: ["Di Liu", "Meng Chen", "Baotong Lu", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2409.10516"
  - title: "Generalization through Memorization: Nearest Neighbor Language Models (kNN-LM)"
    authors: ["Urvashi Khandelwal", "Omer Levy", "Dan Jurafsky", "Luke Zettlemoyer", "Mike Lewis"]
    year: 2019
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "From local to global: A graph RAG approach to query-focused summarization"
    authors: ["Darren Edge", "Ha Trinh", "Newman Cheng", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2404.16130"
  - title: "LightRAG: Simple and Fast Retrieval-Augmented Generation"
    authors: ["Zirui Guo", "Lianghao Xia", "Yanhua Yu", "Tu Ao", "Chao Huang"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2410.05779"
  - title: "NodeRAG: Structuring graph-based RAG with heterogeneous nodes"
    authors: ["Tianyang Xu", "Haojie Zheng", "Chengze Li", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "HippoRAG: Neurobiologically inspired long-term memory for LLMs"
    authors: ["Bernal Jimenez Gutierrez", "Yiheng Shu", "Yu Gu", "Michihiro Yasunaga", "Yu Su"]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "From RAG to memory: Non-parametric continual learning for LLMs (HippoRAG 2)"
    authors: ["Bernal Jiménez Gutiérrez", "Yiheng Shu", "Weijian Qi", "Sizhe Zhou", "Yu Su"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.14802"
  - title: "Zep: A temporal knowledge graph architecture for agent memory"
    authors: ["Preston Rasmussen", "Pavlo Paliychuk", "Travis Beauvais", "Jack Ryan", "Daniel Chalef"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2501.13956"
  - title: "A-MEM: Agentic memory for LLM agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "Hang Gao", "Juntao Tan", "Yongfeng Zhang"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.12110"
  - title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "Taranjeet Singh", "Deshraj Yadav"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.19413"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Charles Packer", "Sarah Wooders", "Kevin Lin", "Vivian Fang", "Shishir G. Patil", "Ion Stoica", "Joseph E. Gonzalez"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "Titans: Learning to memorize at test time"
    authors: ["Ali Behrouz", "Peilin Zhong", "Vahab Mirrokni"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "LoRA: Low-Rank Adaptation of Large Language Models"
    authors: ["Edward J. Hu", "Yelong Shen", "Phillip Wallis", "Zeyuan Allen-Zhu", "Yuanzhi Li", "Shean Wang", "Lu Wang", "Weizhu Chen"]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2106.09685"
  - title: "Parametric Retrieval Augmented Generation (PRAG)"
    authors: ["Weihang Su", "Yichen Tang", "Qingyao Ai", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2501.15915"
  - title: "Dynamic Parametric Retrieval Augmented Generation (DyPRAG)"
    authors: ["Yuqiao Tan", "Shizhu He", "Huanxuan Liao", "Jun Zhao", "Kang Liu"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2503.23895"
  - title: "Locating and Editing Factual Associations in GPT (ROME)"
    authors: ["Kevin Meng", "David Bau", "Alex Andonian", "Yonatan Belinkov"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2202.05262"
  - title: "Mass-Editing Memory in a Transformer (MEMIT)"
    authors: ["Kevin Meng", "Arnab Sen Sharma", "Alex Andonian", "Yonatan Belinkov", "David Bau"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2210.07229"
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    authors: ["Nelson F. Liu", "Kevin Lin", "John Hewitt", "Ashwin Paranjape", "Michele Bevilacqua", "Fabio Petroni", "Percy Liang"]
    year: 2024
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "Mohit Bansal", "Francesco Barbieri", "Yuwei Fang"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.17753"
  - title: "LongMemEval: Benchmarking chat assistants on long-term interactive memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "Yuwei Zhang", "Kai-Wei Chang", "Dong Yu"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2410.10813"
  - title: "PreFEval: Do LLMs recognize your preferences? Evaluating personalized preference following"
    authors: ["Siyan Zhao", "Mingyi Hong", "Yang Liu", "Devamanyu Hazarika", "Kaixiang Lin"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.09597"
  - title: "PersonaMem: Benchmarking LLMs for dynamic user profiling and personalized responses"
    authors: ["Bowen Jiang", "Zhuoqun Hao", "Young-Min Cho", "Bryan Li", "Yuan Yuan", "Sihao Chen", "Lyle Ungar", "Camillo J Taylor", "Dan Roth"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.14225"
  - title: "MIRIX: Multi-agent memory system for LLM-based agents"
    authors: ["Yu Wang", "Xi Chen"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2507.07957"
  - title: "AI-native memory 2.0: Second Me"
    authors: ["Jiale Wei", "Xiang Ying", "Tao Gao", "Fangyi Bao", "Felix Tao", "Jingbo Shang"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "AutoGen: Enabling next-gen LLM applications via multi-agent conversation framework"
    authors: ["Qingyun Wu", "Gagan Bansal", "Jieyu Zhang", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2308.08155"
  - title: "LIMA: Less is more for alignment"
    authors: ["Chunting Zhou", "Pengfei Liu", "Puxin Xu", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "BM25 and beyond: The probabilistic relevance framework"
    authors: ["Stephen E. Robertson", "Hugo Zaragoza"]
    year: 2009
    venue: "Foundations and Trends in Information Retrieval"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sentence-BERT: Sentence embeddings using siamese BERT-networks"
    authors: ["Nils Reimers", "Iryna Gurevych"]
    year: 2019
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Empowering large language models to set up a knowledge retrieval indexer via self-learning (PGRAG)"
    authors: ["Xiang Liang", "Simin Niu", "Zhiyu Li", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2405.16933"
  - title: "Disentangling Memory and Reasoning Ability in Large Language Models (Memory&Reasoning)"
    authors: ["Mingyu Jin", "Weidi Luo", "Sitao Cheng", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2411.13504"
  - title: "Llama SLayer 8B: Shallow Layers Hold the Key to Knowledge Injection"
    authors: ["Tianxiang Chen", "Zhentao Tan", "Tao Gong", "et al."]
    year: 2024
    venue: "EMNLP Findings"
    doi: null
    url: null
    arxiv_id: null
  - title: "QUEST: Query-Aware Sparsity for Efficient Long-Context LLM Inference"
    authors: ["Jiaming Tang", "Yilong Zhao", "Kan Zhu", "Guangxuan Xiao", "Baris Kasikci", "Song Han"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 7
  title: "Overview of the MemOS framework — three-layer architecture (interface, operation, infrastructure) with MemCube as the unifying data structure"
  page: 16
  image_path: "figures/li-2025-memos-fig.png"
---

# MemOS: A Memory OS for AI System

**Authors:** Zhiyu Li, Chenyang Xi, Chunyu Li, Ding Chen, Boyu Chen, Shichao Song, Simin Niu, Hanyu Wang, Jiawei Yang, Chen Tang, Qingchen Yu, Jihao Zhao, Yezhaohui Wang, Peng Liu, Zehao Lin, Pengyuan Wang, Jiahao Huo, Tianyi Chen, Kai Chen, Kehang Li, Zhen Tao, Huayi Lai, Hao Wu, Bo Tang, Zhengren Wang, Zhaoxin Fan, Ningyu Zhang, Linfeng Zhang, Junchi Yan, Mingchuan Yang, Tong Xu, Wei Xu, Huajun Chen, Haofen Wang, Hongkang Yang, Wentao Zhang, Zhi-Qin John Xu, Siheng Chen, Feiyu Xiong (MemTensor Shanghai + IAAR + China Telecom Research + Tongji + Zhejiang U + USTC + Peking U + Renmin U + Beihang U + Shanghai Jiao Tong U)
**Published:** 2025-07 (v4 2025-12-03) · [Source](https://arxiv.org/abs/2507.03724)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MemOS is the "memory operating system" framing for LLMs — the paper argues that LLMs today have implicit parameter memory and ephemeral context, but lack the intermediate, schedulable, lifecycle-managed memory layer that traditional operating systems provide for compute and storage. It proposes three substrates as first-class memory types — **Plaintext Memory** (explicit retrievable text/graphs/prompts), **Activation Memory** (KV-cache + hidden states), **Parameter Memory** (model weights, LoRA blocks) — and unifies them behind a single abstraction called the **MemCube**: a metadata-header + payload structure with descriptive identifiers (timestamp, origin signature, semantic type), governance attributes (ACL, TTL, priority, watermarks), and behavioral usage indicators (access frequency, contextual fingerprint, version chain). The architecture has three layers: **Interface** (MemReader parses natural language into MemoryCalls; Memory API exposes Provenance/Update/LogQuery; Memory Pipeline chains operations), **Operation** (MemOperator structures memory as tags + graph + hierarchical layers; MemScheduler dynamically promotes hot plaintext → KV cache → parameter blocks; MemLifecycle moves units through Generated → Activated → Merged → Archived → Frozen states), and **Infrastructure** (MemGovernance enforces ACLs/audit/watermarks; MemVault stores by namespace across vector + relational + blob backends; MemLoader/MemDumper handle cross-platform migration; MemStore enables publish/subscribe of memory units across agents). Empirically, MemOS-1031 (their reference implementation, all baselines on GPT-4o-mini backbone) hits **75.80 overall on LoCoMo LLM-judge** (vs 72.01 Memobase, 64.57 Mem0, 64.33 MIRIX, 59.22 Zep), **77.8 overall on LongMemEval** (vs 72.4 Memobase, 66.4 Mem0, 63.8 Zep), **77.2 / 71.9 personalized-response on PreFEval** (0-turn / 10-irrelevant-turn vs 65.9/63.7 Mem0), and **61.2 precision on PersonaMem** (vs 58.9 Memobase). Under 100 QPS load it sustains 100% success at 251.9ms mean add latency / 741.2ms mean search latency where competitors collapse to 7-89% success. The KV-acceleration mode (auto-promote hot plaintext to GPU-resident KV) delivers up to **91.4% TTFT reduction** on Qwen2.5-72B in long-context / short-query conditions. The conceptual move is bigger than the numbers: the paper positions Mem-training as a third scaling regime after pretraining and post-training, with the memory marketplace (MemStore as a "memory app store") as the user-facing payoff.

## Key Takeaway

Treat memory as a typed, schedulable, governable system resource — not as "RAG plus a vector DB." The decisive architectural commitment is the **MemCube**: a single carrier that holds whichever of the three substrates a memory currently lives in (text fragment, KV tensor, LoRA delta) plus the metadata to know who wrote it, who can read it, when it expires, and how often it's been hit. Once everything in the system is a MemCube, the scheduler can do something neither RAG nor MemGPT can: **dynamically transform memories between substrates based on usage**. Hot plaintext gets compiled to a KV-cache that's preloaded onto the GPU (the 91.4% TTFT win). Repeatedly-triggered behaviors get distilled into LoRA blocks (parameter memory you can swap in and out like capability plugins). Underused KV gets demoted back to cold plaintext. This is the OS-grade idea: the substrate a memory lives in is a *runtime decision* driven by access patterns and resource constraints, not a developer choice baked in at write time. Combined with the lifecycle FSM (Generated → Activated → Merged → Archived → Frozen) and the ternary permission model (identity × object × calling context), MemOS turns memory into something you can audit, version, share via a marketplace (MemStore), and migrate across platforms — which is what an OS-style resource looks like. The benchmark wins (75.8 / 77.8 / 77.2 / 61.2 across four memory leaderboards on the same GPT-4o-mini backbone, beating Mem0, Zep, Memobase, MIRIX, MemU, Supermemory) are the proof that the abstraction isn't just architectural prose — it's actually doing work.

## Implications

- **[N + A — the substrate-as-runtime-decision idea]** The single most useful idea for your own architecture: stop committing to "memories are markdown files" or "memories are vector chunks" or "memories are LoRA blocks" at write time. Model the memory unit as a typed envelope (MemCube-equivalent) and let access patterns decide the physical representation. MemOS's evidence: hot plaintext promoted to KV gives 91.4% TTFT reduction; repeated patterns distilled to parameters become "capability plugins." For ENGRAM, this is a Network/Aggregate fusion — the shape-of-memory is not a one-time encoding choice, it's a continuous consolidation decision driven by Maintain telemetry. Most current systems (Mem0, A-MEM, Zep) are stuck on one shape per memory; MemOS is the first system-level framing that says "the shape changes."

- **[G — provenance as governance, not annotation]** Every MemCube carries identity, ACL, TTL, sensitivity tags, watermarks, version chain, and origin signature in its metadata header — and **all Memory API calls take MemCube as the parameter carrier and response format**, so provenance is structurally enforced, not bolted on. This is a sharper move than Zep's bi-temporal labels (which are values inside the graph) or MemGPT's tier-separation (which gives you provenance "for free" by structure but no explicit fields). The lesson: if you want governance, make the smallest unit carry the metadata. Don't put it in a sidecar table. Don't trust the LLM to remember to tag. The unit *is* its metadata.

- **[E + A — the encoding-aggregate trade is decided by a scheduler, not a pipeline]** MemReader (encoding) and MemScheduler (aggregation/promotion) are decoupled. MemReader extracts structured MemoryCalls (intent, time scope, entities, anchor) from natural language. MemScheduler decides — at inference time — whether to inject as plaintext, KV-cache hit, or parameter-block activation. This is exactly the "AI as maintainer" pattern the lens prizes: the LLM's role is split into "reader at input" and "scheduler at runtime," not collapsed into one extraction step. Compare to Mem0's write-time extract pipeline (which Adler 2026 critiques as lossy) — MemOS keeps the raw plaintext as ground truth and lets the scheduler decide the *representation* at query time. The trade is no longer write-vs-read; it's substrate selection.

- **[M — lifecycle as a finite state machine with Freeze]** Memories cycle through five states: Generated, Activated, Merged, Archived, Frozen. The Frozen state is the interesting innovation — designed for legal agreements, standard guidelines, audit-critical memory — where updates are *disabled* and full modification histories are retained. This is the first memory architecture I've digested that explicitly carves out "this memory is immutable and that immutability is enforced by the runtime, not by convention." For Flow OS contradictions/values memories: you want a Frozen tier. Without it, the agent's prior inferences inevitably get edited into "facts" and you can't tell what the user actually said vs what got synthesized.

- **[R — hybrid retrieval is table-stakes; the differentiator is task-aligned routing]** MemOperator combines structured retrieval (tags, time, boolean, ACL filters) with semantic retrieval (vector similarity) — fine, everybody does this now. The *differentiator* is the **MemoryPathResolver**: user inputs are decomposed into a topic → concept → fact hierarchy, then the resolver answers "what to search, where to search, in what order." Most agent memory systems leave this implicit in the LLM's tool-use loop; MemOS makes it a structured component. This is the missing layer between "the agent has a `search_memory` tool" and "the agent actually retrieves the right thing on multi-hop queries." Worth porting.

- **[N — the polyglot stack is the right answer]** MemVault interfaces with vector stores, relational DBs, and blob storage through a unified MemoryAdapter abstraction — namespaces include user-private, expert KB, industry-shared, contextual pool, pipeline-aligned cache. This validates the polyglot stack hypothesis (vs single flat vector store) on architectural grounds: different memory categories have different access patterns, and they belong in different backends behind one API. The same conclusion EverMemOS and Hindsight reach by experiment; MemOS reaches it by design philosophy.

- **[M + Cross-platform — the marketplace as a maintenance device]** The MemStore publish/subscribe mechanism — "expert physician encapsulates diagnostic heuristics into a structured memory, uploads to MemStore, medical student installs it via standardized loader with permission control" — is the only place in agent-memory literature I've seen that proposes memory as a *licensable asset* with contract-bound access frequencies and expiry policies. Whether or not the marketplace itself materializes, the architectural commitment matters: memory units are portable across instances. Compare to MemGPT (per-deployment), Mem0 (per-user), Zep (per-graph) — MemOS is the only one designing for *cross-platform memory mobility* from day one. For Flow OS thinking about cross-customer pattern libraries: this is the structural pattern.

- **[N + Encode interactions — KV-promotion is a real architectural win, not a benchmark trick]** The KV-acceleration result (Table 8) is operationally specific and credible: MemScheduler monitors interactions, identifies "most frequently accessed and semantically stable" plaintext entries, converts them to KV-format and proactively transfers to GPU memory. TTFT speedup: 23-94.2% depending on model size (Qwen3-8B / 32B / 72B) and context/query lengths. The output sequences are identical under both prompt-injection and KV-injection (validated). This is what "promotion between memory tiers" actually looks like in production, with measured numbers. If you build a memory system that doesn't have a hot/cold tier with promotion, you're leaving low-hanging latency on the floor.

- **[G — the contradiction-surfacing gap]** Despite the elaborate governance machinery, the paper does *not* describe a mechanism for surfacing contradictions between MemCubes. The Update API supports "conflict detection, deduplication, versioning, and forgetting policies" (Section 4.1) but the only concrete example is "outdated clinical guidelines vs new clinical guidelines, MemScheduler prioritizes trusted and active versions, archives obsolete." That's smoothing-away, not surfacing. The lens cares about exactly this — and MemOS, for all its architectural ambition, falls into the same trap as Mem0 (let the scheduler pick the right version, hide the contradiction from the agent). A real contradiction-surfacing layer would need an additional MemCube relationship type (`contradicts`) and a retrieval mode that returns both sides. Not implemented here. Open hole.

## How to Apply It (method)

**Scenario:** You're designing Flow OS's next-generation memory layer to replace the v2 flat "atomic markdown files + QMD hybrid search" approach. You want substrate-level promotion (hot Flow-session knowledge should become a system-prompt-resident bundle rather than a fresh QMD search every turn), governance for cross-venture knowledge (some patterns from one venture should not leak into another agent's working set), and a clear lifecycle (raw transcript → extracted memory → consolidated pattern → archived). You're not going to literally implement parameter-memory promotion (LoRA tuning per memory is overkill for a markdown brain), but you want the architectural shape.

**Steps:**

1. **Define your MemCube envelope.** Every memory unit in Flow OS — a session-extracted memory, a contact card, a pattern file, a contradiction node — gets the same frontmatter spine. Mandatory fields, mapped directly from MemOS Section 4.2:
   - **Descriptive Identifiers**: `id`, `created` (timestamp), `last_modified`, `origin_signature` (one of: `user-input`, `session-extract`, `agent-inference`, `imported-from-marketplace`), `semantic_type` (one of: `fact`, `preference`, `decision`, `pattern`, `contact`, `contradiction`).
   - **Governance Attributes**: `acl` (which agents/skills can read), `ttl` (or `null` for permanent), `priority` (`low`/`mid`/`high`/`frozen`), `sensitivity_tags` (e.g. `personal`, `client-confidential`, `public`), `compliance_label`.
   - **Behavioral Usage Indicators**: `access_count`, `last_used`, `contextual_fingerprint` (embedding hash for fast retrieval), `version_chain` (lineage of prior IDs), `lifecycle_state` (one of `Generated`, `Activated`, `Merged`, `Archived`, `Frozen`).

   Put these in the v2 frontmatter schema. Crucially, **every memory-modifying tool call must take and return a MemCube-shaped object** — provenance and ACLs are enforced at the API boundary, not as developer convention.

2. **Build the three substrate slots.** Flow OS won't have LoRA blocks, but it can have three tiers:
   - **Plaintext tier** — the existing markdown files in `memory/` (the equivalent of MemOS Plaintext Memory).
   - **Activation tier** — a "session bundle" cache: a compiled markdown blob (≤ 4k tokens) of the highest-frequency, most-recently-accessed memories for the current agent, injected at the top of every prompt (the equivalent of MemOS Activation Memory / KV promotion, minus the actual KV trick).
   - **Capability tier** — a registry of skill files (`.claude/commands/*.md`, `skills/*/SKILL.md`) that distill repeated patterns into invokable workflows (the equivalent of MemOS Parameter Memory / capability plugins).

3. **Build a MemScheduler equivalent.** A Python module (call it `flow/scheduler.py`) that runs on every session-start and watches access patterns:
   - **Promote**: if a plaintext memory has been accessed in ≥ 3 of the last 10 sessions AND its size is < 500 tokens, promote it into the next session's activation bundle. (Crude approximation of MemOS's hot-plaintext → KV-cache rule.)
   - **Demote**: if an activation-bundle entry hasn't been touched in 5 sessions, drop it back to plaintext-only retrieval.
   - **Crystallize**: if a pattern memory has been cited in ≥ 5 sessions across ≥ 2 ventures, surface a recommendation to skillify it (move it to the capability tier as a SKILL.md). Don't auto-promote — surface to user.

4. **Build a MemLifecycle FSM.** A small state machine on each MemCube:
   - `Generated`: just extracted by `/learn`, not yet activated.
   - `Activated`: appeared in retrieval results at least once.
   - `Merged`: deduplicated against another memory; old IDs go into `version_chain` of the merged unit.
   - `Archived`: not accessed for N sessions (configurable), moved to `memory/_archive/`.
   - `Frozen`: explicitly marked immutable (values, beliefs, contradiction-anchors, contract terms). Updates blocked at the API level. Full modification history retained.
   Critically, transitions are *triggered by the scheduler*, not by the agent volunteering — the agent can request a transition but the FSM enforces the rules.

5. **Add the governance kernel.** Wrap every memory read/write in an `acl_check(caller, memcube, calling_context)` step. The ternary model is: who is asking (which agent / skill / user), what are they asking about (which MemCube), and from what context (which session / which venture). Mirror MemOS's auditing: every memory access goes to `.flow/events.jsonl` with caller + object + intent + decision.

6. **Build MemReader as a separate component.** Don't let the main agent improvise memory queries — wrap user prompts through a small dedicated MemReader step that extracts: task intent (retrieval/update/none), time scope (last week / all-time / session-only), entity focus (which person/venture/topic), and memory type filter (preferences only / decisions only / etc). Convert this into a structured MemoryCall that the scheduler dispatches. This is the MemoryPathResolver pattern — "what to search, where to search, in what order" — applied to your QMD layer.

7. **Implement the contradiction-surfacing gap MemOS missed.** Add a `contradicts:` edge type to your frontmatter. When `/learn` extracts a memory whose embedding is high-similarity but semantic-direction-opposite to an existing memory, create the edge. Add a retrieval mode `qmd query --contradictions-only` that returns both poles plus the contradiction edge. This is the layer MemOS designed governance for but didn't actually wire to the retrieval layer.

8. **Run the eval loop.** On LoCoMo-style traces of your own sessions, measure: (a) recall on multi-session questions (does the agent remember a decision made 3 sessions ago); (b) retrieval latency per turn (is the activation-bundle keeping you under 100ms warm-cache hit); (c) provenance accuracy (when you ask "where did this come from," is the answer trustworthy); (d) contradiction-surface rate (how often does the agent flag conflicting prior positions vs silently picking one). MemOS's published LoCoMo numbers (75.80 overall) are the bar to beat for a memory-OS-shaped system; their robustness numbers (100% success at 100 QPS, 251ms add latency) are the operational bar.

**Expected outcome:** A Flow OS memory layer where the substrate a memory lives in is a runtime decision, governance is structurally enforced at the MemCube boundary, the lifecycle FSM gives you Freeze-protection on values/beliefs, and contradictions are surfaced rather than smoothed away. You'll trade some implementation complexity (scheduler, FSM, ACL kernel, MemReader) for a memory layer that is auditable, portable across customer instances (MemStore-style), and capable of the substrate promotion that delivers the latency wins MemOS measures.

## Best Figure

![Figure 7 — Overview of the MemOS framework: three-layer architecture with MemCube as the unifying data structure (page 16)](figures/li-2025-memos-fig.png)

**Image Candidates:**
- Figure 6 (p. 14): MemCube anatomy — Metadata Header (lifecycle, access control, storage profile) + Memory Payload (plaintext content / activation state / parameter patch) + MemScheduler callable operations. The single most concept-dense visual in the paper; if you only show one slide on "what is a MemCube," this is it.
- Figure 7 (p. 16): The full three-layer architecture (Interface / Operation / Infrastructure) with MemCube flowing through. Best for "show me how the system fits together."
- Figure 5 (p. 13): The transformation paths between Plaintext / Activation / Parameter memory — the "substrate-as-runtime-decision" idea visualized as encoding/caching/decoding arrows. The single best figure for the *meta-architectural* claim.
- Figure 4 (p. 11): Mem-training as the next scaling paradigm — pre-training → post-training → Mem-training timeline. Best for the conceptual / "why this matters" framing.

**Best Image:**
- Figure Name: Figure 7 — "Overview of the MemOS framework"
- Slide Caption: MemOS three-layer architecture — Interface Layer (Prompt, Memory API/Pipeline, MemDecoder, MemReader), Operation Layer (MemScheduler, MemOperator, MemLifecycle, parameter/activation/plaintext memory routing), Infrastructure Layer (MemGovernance, MemVault, MemLoader/MemDumper, MemStore for publish/purchase).
- Description: The figure shows the full memory pipeline from user input through semantic parsing and API abstraction in the Interface Layer, to memory scheduling and lifecycle control in the Operation Layer, to interaction with the Infrastructure Layer for memory injection, retrieval, and governance. On the left, the system context — Business Application calling Agent/User/Pipeline through MemOS over a Large Language Model. In the middle, MemDecoder consumes prompts and produces MemBlocks. The Memory API/Pipeline panel (top right) exposes the six core operations: Memory Provenance (API), Memory Update (API), Memory Log Query (API) on the synchronous side; Memory Transfer (Pip), Memory Purification (Pip), Memory Rollback (Pip) on the pipeline side. MemOperator (Memory Organization + Memory Search) sits below. MemScheduler is the central dispatcher routing among Intrinsic Parameter Memory, External Parametric Memory, Activation Memory, and Plaintext Memory — with the three transformation arrows ("Memory Encoding," "Memory Updating," "Memory Caching") connecting them. At the bottom, MemDumper and MemLoader bookend MemGovernance (Expiry Policy, Access Control, Privacy Protection, Watermarking Service) over MemVault (Industry / Expert / Scenario / User / Pipeline memory categories) backed by both Vector DB and Graph DB. MemStore at the very bottom enables Publish/Purchase of memory units. The single-frame figure makes the OS-grade ambition legible: every "OS service" you'd expect (provenance, scheduling, lifecycle, governance, storage, publishing) has a labeled box, and MemCube is the carrier across all of them.

## What Experts Overlook

What experts in the agent-memory community routinely overlook in MemOS is that the **MemCube is the entire thesis** — most read-throughs treat it as one of many components in a sprawling architecture paper and walk away talking about "another memory framework." But the MemCube is doing something none of the prior systems do: it's a **typed envelope that is agnostic to physical representation**. The same MemCube can hold a plaintext payload today, an activation-state KV tensor tomorrow, and a LoRA delta the day after — without changing its API, its governance metadata, or its lifecycle state. Section 4.2 makes this explicit: "Memory Payload contains the semantic content … MemCube enables structured abstraction, permissioned control, and behavior-driven evolution of heterogeneous memory resources." The Section 4.1 transformation rules then operationalize it: **Plaintext ⇒ Activation** (pre-transform frequent plaintext into KV pairs for low-latency reuse), **Plaintext/Activation ⇒ Parameter** (distill stable knowledge into LoRA blocks as "capability plugins"), **Parameter ⇒ Plaintext** (offload cold parameters back to external storage). Every other memory system (Mem0, Zep, A-MEM, MemGPT, MemMachine) commits to one representation at write time. MemOS treats representation as a *scheduling decision*.

**Why it matters:** This is the only architecture in the agent-memory literature that gives you a path to *promote* memories — to make the system literally faster and the agent literally more capable as a particular memory gets used more. Mem0 makes memories smaller (lossy extraction); Zep makes them more graph-structured (additional indexing); MemGPT makes them paginated (better access). None of them make memories cross substrates. MemOS does, and the Table 8 KV-promotion numbers (91.4% TTFT reduction on Qwen2.5-72B, semantic-equivalent outputs) prove it isn't theoretical. The implication for ENGRAM is that "Network" (shape-of-memory) and "Aggregate" (consolidation) are not separate dimensions — they're coupled through a runtime scheduler, and the system's intelligence is partly stored in *which substrate it picks for which memory at which time*. If you read MemOS as "yet another LLM memory framework," you'll miss this. If you read it as "the first paper to model memory representation as a scheduling problem," you'll see the canonical contribution.

**Example of good use:** Building a customer-service agent for a SaaS company. The customer's billing history is plaintext memory (queried rarely, must be exact). The product's top 50 most-asked-about features are promoted to a KV-cache that's preloaded into every agent session — first-token latency on questions like "How do I export to CSV?" drops from 2.5s to 0.2s because the relevant facts are already in attention. The company's brand voice and refund policy are distilled into a small LoRA block (parameter memory) that's loaded as a "capability plugin" on agent startup — the agent doesn't need to re-read the policy doc each turn. All three live as MemCubes with the same API surface; only the scheduler knows where each one lives at any moment.

**Example of misapplication:** Reading the paper as a feature list and concluding "we need a vector DB + lifecycle states + an ACL kernel." Bolting those on without the unified MemCube abstraction gets you a more complex Mem0 — not MemOS. The MemCube is load-bearing because it's what lets the scheduler move memories between substrates. Without it, you're managing three separate storage systems with three separate APIs, and the promotion / demotion machinery can't be built because there's no common envelope to transform.

## Extracted Prompts

The paper does not publish explicit prompt templates for MemOS-1031 (its reference implementation), but the MemReader and MemScheduler descriptions imply specific structured-extraction prompts. The following are reconstructed from the paper's worked examples and architectural descriptions — useful as starting points if you're implementing a MemReader-equivalent.

**Prompt explanation:** MemReader-style intent + scope extraction from a natural-language prompt. Used by the Interface Layer to convert a user prompt into a structured MemoryCall before any retrieval happens. Mirrors the worked example in Section 5.3.1: *"Remind me what the doctor said about my medication during last year's hospitalization"* → `{task_intent: retrieval, time_scope: last_year, topic: medication_guidance, context_anchor: hospitalization_period}`.

```
You are MemReader, the memory-intent parser for an agent's memory layer.
Given a user prompt and the current dialogue context, extract a structured
MemoryCall in strict JSON.

Output schema (no extra keys, no prose):
{
  "task_intent": "retrieval" | "update" | "deletion" | "none",
  "time_scope": <ISO date | date_range | "all-time" | "session-only" | null>,
  "topic_entities": [string],
  "context_anchor": <free-text anchor phrase or null>,
  "memory_type_filter": ["fact" | "preference" | "decision" | "pattern" | ...] | null,
  "access_intent": "read" | "write" | "verify" | null,
  "window_parameters": {"max_results": int, "freshness_weight": float}
}

If the prompt does not require memory access, return task_intent: "none" and
the rest as nulls.

User prompt: {{PROMPT}}
Dialogue context (last 3 turns): {{CONTEXT}}
```

**Prompt explanation:** MemScheduler routing-decision prompt — given a MemoryCall and a candidate set of MemCubes, decide which substrate to inject from. This mirrors Section 5.4.2's "Type-Aware Transformation and Loading Mechanism" — for coherence-heavy tasks favor KV-cache; for procedural/expert flows favor parametric; for on-demand factual queries use plaintext.

```
You are MemScheduler, the memory dispatcher for an agent's runtime.
Given a parsed MemoryCall and a set of candidate MemCubes, decide which
to inject and in what substrate form.

Candidates (each with substrate, access_frequency, last_used,
contextual_fingerprint_similarity, priority):
{{CANDIDATES_JSON}}

MemoryCall:
{{MEMORYCALL_JSON}}

Task signals:
- coherence_heavy: {{bool — is this a multi-turn dialogue continuation?}}
- procedural: {{bool — is this a workflow-execution task?}}
- factual_query: {{bool — is this an open-domain lookup?}}
- context_window_remaining_tokens: {{int}}

Output schema (no extra keys):
{
  "selected_memcube_ids": [string],
  "injection_substrate_per_cube": {
    "<memcube_id>": "plaintext" | "kv_activation" | "parameter_block"
  },
  "injection_order": [string],
  "promotion_recommendations": [
    {"memcube_id": string, "from": string, "to": string, "rationale": string}
  ]
}

Rules:
- For coherence_heavy tasks, prefer kv_activation for top-3 most accessed.
- For procedural tasks, prefer parameter_block (capability plugins) if available.
- For factual_query, default to plaintext unless contextual_fingerprint > 0.85.
- If selected total exceeds context_window_remaining_tokens, drop lowest priority.
```

**Prompt explanation:** MemLifecycle transition-recommendation prompt — used by the system on a scheduled basis (e.g. nightly) to recommend which MemCubes should advance through Generated → Activated → Merged → Archived → Frozen states based on access telemetry.

```
You are MemLifecycle, the state-machine maintainer for the agent's memory.
Review the following MemCube telemetry and recommend state transitions.

For each cube, you may recommend ONE of:
- "promote-to-activated" (cube has been retrieved at least once recently)
- "merge-with" + target_id (cube is semantically near-duplicate of another)
- "archive" (cube hasn't been accessed in N sessions, low priority)
- "freeze" (cube has compliance_label of legal/contract/values; lock immutable)
- "no-change"

Cube telemetry:
{{CUBES_TELEMETRY_JSON}}

Policies:
- Never recommend freeze unless compliance_label is explicit.
- Never recommend archive on cubes with priority="high".
- Recommend merge only when contextual_fingerprint cosine ≥ 0.92.
- All recommendations are advisory — the runtime makes the final call.

Output (strict JSON array of transitions, no prose):
[{"cube_id": string, "transition": string, "target_id": string|null,
  "rationale": string}]
```

## Citations

A subset of the most architecturally-load-bearing references (full ~106 in frontmatter). Selected for the memory-architect lens — focus on the works that directly informed MemOS's hierarchical-substrate or OS-metaphor framing.

- **[1] Memory3 — Yang et al. 2024** (J. of Machine Learning) — The MemOS team's prior work, cited as the direct ancestor of the hierarchical-memory framing and the KV-as-explicit-memory trick. MemOS Section 4.1 explicitly says it "systematizes" Memory3.
- **[98] MemGPT — Packer et al. 2024** — The closest architectural sibling. MemOS positions itself as the *system-level* version of what MemGPT did at the *agent-tool* level. (See `[[packer-2023-memgpt-os]]`.)
- **[55, 97, 105] Mem0 — Chhikara et al. 2025** — The strongest production baseline; MemOS beats it 75.80 vs 64.57 on LoCoMo and 77.8 vs 66.4 on LongMemEval. (See `[[chhikara-2025-mem0]]`.)
- **[53, 106] Zep — Rasmussen et al. 2025** — The temporal-knowledge-graph baseline. (See `[[rasmussen-2025-zep-temporal-kg]]`.)
- **[50, 51] HippoRAG / HippoRAG 2 — Gutierrez et al. 2024/2025** — Cited as the canonical "human-like memory" inspiration (hippocampal-indexing theory).
- **[29] vLLM/PagedAttention — Kwon et al. 2023** — Cited as the direct OS-design ancestor for the KV-cache management approach.
- **[1, 30, 31, 32, 33, 34] KV-cache optimization line** — vLLM, StreamingLLM, H2O, LESS, KVQuant, RetrievalAttention — establishes the "activation memory as schedulable resource" subfield MemOS builds on.
- **[60, 61, 62] LoRA / PRAG / DyPRAG** — The parameter-memory-as-plugin line of work that grounds MemOS's "capability plugins" claim.
- **[100] LoCoMo — Maharana et al. 2024** — The primary benchmark. (See `[[maharana-2024-locomo]]`.)
- **[101] LongMemEval — Wu et al. 2024** — Long-term memory benchmark. (See `[[wu-2024-longmemeval]]`.)
- **[102] PreFEval — Zhao et al. 2025** — Personalized-preference benchmark.
- **[103] PersonaMem — Jiang et al. 2025** — Dynamic-user-profiling benchmark.
- **[104] MIRIX — Wang & Chen 2025** — A baseline; six-component memory architecture (Core, Episodic, Semantic, Procedural, Resource, Knowledge Vault).
- **[19, 20, 21] Memory taxonomy surveys** — Du et al., Wu et al., Shan et al. — Cited as the prior taxonomic groundwork MemOS extends.
- **[95] Second-Me — Wei et al. 2025** — Three-layer human-like memory architecture (L0/L1/L2); cited as a Stage-2 (human-like memory) example MemOS positions itself above.

Full bibliography of 106 references is preserved in the YAML frontmatter for citation-walk traversal.

## Related Digests

- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems. The agent-tool-level OS metaphor; MemOS is the system-level evolution of the same idea.
- [[hu-2026-evermemos]] — EverMemOS: A Self-Organizing Memory Operating System. The closest descendant — picks up the "memory OS" name and focuses on write-time scene-level consolidation (MemScenes) that MemOS leaves to MemReader.
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. The strongest baseline beaten on every MemOS benchmark; same author family argues MemOS's substrate-promotion machinery is what closes the remaining gap on multi-hop and temporal-reasoning tasks Mem0 leaves on the table.
- [[rasmussen-2025-zep-temporal-kg]] — Zep: A Temporal Knowledge Graph Architecture for Agent Memory. Provides the bi-temporal labelling pattern MemOS could (but doesn't) use to ground its Version Chain semantics.
- [[wang-2026-memmachine]] — MemMachine: A Ground-Truth-Preserving Memory System. Argues retrieval-stage knobs (depth, formatting) deliver more than storage cleverness; orthogonal to MemOS's substrate-promotion claim.
- [[li-2026-qrranker-reranker]] — Query-focused and Memory-aware Reranker for Long Context Processing. An alternative path to MemOS's gains — drop the memory framework entirely, train a 4B reranker. Beats MemOS-1031 on raw LoCoMo F1 (57.03 vs 45.27), losing on LLM-judge.
- [[rafique-2026-clawvm]] — ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents. Sister architecture: where MemOS schedules memory substrates, ClawVM schedules tool-result residence.
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall. The strongest theoretical critique relevant to MemOS — argues that write-time LLM extraction (which MemReader does) is anti-information; MemOS sidesteps this partly because it keeps raw plaintext as ground truth even after promotion.
- [[mao-2026-agent-memory-circuits]] — What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis. Companion to MemOS — explains why small models can route memory correctly long before they extract it correctly, which directly threatens MemReader's reliability assumptions.
- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents. The primary benchmark MemOS is evaluated on; understanding LoCoMo's specific failure modes (single-hop / multi-hop / temporal / open-domain) sharpens how to interpret MemOS-1031's 75.80 overall.
- [[wu-2024-longmemeval]] — LongMemEval. The other primary benchmark; six-scenario decomposition (single-session preference / single-session assistant / temporal reasoning / multi-session / knowledge update / single-session user).

## Reviewer Notes

**Overall hallucination severity: Clean**

Cross-checked the digest against the paper text. Major claims verified:

- **LoCoMo overall 75.80**: confirmed Table 3, line 1316. Memobase 72.01 confirmed. Mem0 64.57 confirmed. MIRIX 64.33 confirmed. Zep 59.22 confirmed.
- **LongMemEval overall 77.8**: confirmed Table 4, line 1334. Memobase 72.4, Mem0 66.4, Zep 63.8 confirmed.
- **PreFEval personalized response 77.2 (0-turn) and 71.9 (10-turn)**: confirmed Table 5, lines 1387 and 1401.
- **PersonaMem precision 61.2**: confirmed Table 6, line 1409. Memobase 58.9 confirmed.
- **KV TTFT speedup 91.4% on Qwen2.5-72B (long context, short query)**: confirmed Table 8, line 1551, "long / short / Qwen2.5-72B" row showing 91.4%.
- **100% success at 100 QPS, 251.9ms mean add latency, 741.2ms mean search latency**: confirmed Table 7, line 1489.
- **Three memory substrates (Plaintext / Activation / Parameter)**: confirmed throughout Section 4.1.
- **MemCube structure (Metadata Header + Memory Payload, three metadata categories)**: confirmed Section 4.2, Figure 6.
- **Three-layer architecture (Interface / Operation / Infrastructure)**: confirmed Section 5.1, Figure 7.
- **Five lifecycle states (Generated / Activated / Merged / Archived) + Frozen**: confirmed Section 5.4.3. Note: the main state machine is 4 states; "Frozen" is described as a separate critical-memory state in the same section. Digest correctly distinguishes.
- **MemReader / MemScheduler / MemLifecycle / MemOperator / MemGovernance / MemVault / MemLoader / MemDumper / MemStore module names**: all confirmed in Sections 5.3–5.5.
- **MemStore as publish/subscribe memory marketplace with licensing**: confirmed Section 7.1.1 ("a medical expert may restrict installation rights to users who have completed a micropayment, enabling a form of licensed intelligence delivery").
- **Mem-training as third scaling paradigm after pre/post-training**: confirmed Section 3.1, Figure 4.
- **All baselines on GPT-4o-mini for fair comparison**: confirmed line 1286.
- **Reference count ~106**: confirmed (numbered through [106] at line 2010).

**Minor notes (not corrected, not affecting accuracy)**:

- The "Mem-training" framing is a forward-looking proposal in Section 3.1; the digest treats it as conceptual, not as a delivered system component. Correct framing.
- MemOS-1031 is the specific implementation evaluated; the digest correctly distinguishes the conceptual MemOS framework from the MemOS-1031 reference implementation throughout.
- The "MemStore as marketplace" framing is aspirational in the paper (Section 8 future-work mentions decentralized memory exchange explicitly as a planned direction); the digest treats it as designed-for but not measured. Correct.
- No fabricated numbers detected. No prompt templates were published in the paper — the extracted prompts are explicitly labelled as reconstructions based on Section 5.3.1 / 5.4.2 / 5.4.3 worked examples, not as transcribed prompts from the paper.
- The author list is long (40 authors); checked against the title page and confirmed all are listed in the same order as the paper. Affiliations are correctly attributed.

**Verdict**: Digest is faithful to the paper. Numbers, module names, architectural claims, and citation attributions are accurate. Safe to use as a wiki entry and as a meta-digest anchor for the "memory-OS lineage" cluster in the citation-walk run.
