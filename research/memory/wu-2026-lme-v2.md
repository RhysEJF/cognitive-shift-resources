---
corpus: agentic-memory
kind: paper-digest
slug: wu-2026-lme-v2
title: "LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues"
authors:
  - "Wu, Di"
  - "Ji, Zixiang"
  - "Kawatkar, Asmi"
  - "Kwan, Bryan"
  - "Gu, Jia-Chen"
  - "Peng, Nanyun"
  - "Chang, Kai-Wei"
year: 2026
publication_date: "2026-05"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2605.12493"
doi: null
arxiv_id: "2605.12493"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Stop compressing trajectories at write time — store them as files and let an off-the-shelf coding agent rummage at query time; lightweight scaffolding (a workflow doc, a manifest, an inspection helper) lifts that approach from 69.9% to 74.9% on a 25M-token web-agent haystack while cutting latency 39% versus vanilla Codex."
topics:
  - agent-memory
  - long-term-memory
  - benchmark
  - web-agents
  - retrieval-augmented-generation
  - coding-agents
  - context-gathering
  - trajectory-memory
  - engram-encode
  - engram-network
  - engram-retrieve
  - engram-aggregate
tags:
  - paper
  - agent-memory
  - benchmark
  - rag
  - coding-agent
  - file-system-memory
  - web-agent
  - longmemeval
entities:
  - wu-di
  - chang-kai-wei
  - ucla
related_digests:
  - wu-2024-longmemeval
  - packer-2023-memgpt-os
  - chhikara-2025-mem0
  - maharana-2024-locomo
  - latimer-2025-hindsight-memory
  - adler-2026-storage-not-memory
  - tavakoli-2026-beam-light
citations:
  - title: "Claude Opus 4.6 System Card"
    authors: ["Anthropic"]
    year: 2026
    venue: "model card"
    doi: null
    url: "https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf"
    arxiv_id: null
  - title: "LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks"
    authors: ["Yushi Bai", "Shangqing Tu", "Jiajie Zhang", "et al."]
    year: 2025
    venue: "ACL 2025"
    doi: null
    url: "https://aclanthology.org/2025.acl-long.183/"
    arxiv_id: null
  - title: "WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks"
    authors: ["Léo Boisvert", "Megh Thakkar", "Maxime Gasse", "et al."]
    year: 2024
    venue: "NeurIPS 2024"
    doi: null
    url: "http://papers.nips.cc/paper_files/paper/2024/hash/0b82662b6c32e887bb252a74d8cb2d5e-Abstract-Datasets_and_Benchmarks_Track.html"
    arxiv_id: null
  - title: "RepairAgent: An Autonomous LLM-based Agent for Program Repair"
    authors: ["Islem Bouzenia", "Premkumar T. Devanbu", "Michael Pradel"]
    year: 2025
    venue: "ICSE 2025"
    doi: "10.1109/ICSE55347.2025.00157"
    url: "https://doi.org/10.1109/ICSE55347.2025.00157"
    arxiv_id: null
  - title: "Coding Agents are Effective Long-Context Processors"
    authors: ["Weili Cao", "Xunjian Yin", "Bhuwan Dhingra", "et al."]
    year: 2026
    venue: "preprint"
    doi: "10.48550/ARXIV.2603.20432"
    url: "https://doi.org/10.48550/arXiv.2603.20432"
    arxiv_id: "2603.20432"
  - title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "et al."]
    year: 2025
    venue: "ECAI 2025"
    doi: "10.3233/FAIA251160"
    url: "https://doi.org/10.3233/FAIA251160"
    arxiv_id: null
  - title: "CL-Bench: A Benchmark for Context Learning"
    authors: ["Shihan Dou", "Ming Zhang", "Zhangyue Yin", "et al."]
    year: 2026
    venue: "preprint"
    doi: "10.48550/ARXIV.2602.03587"
    url: "https://doi.org/10.48550/arXiv.2602.03587"
    arxiv_id: "2602.03587"
  - title: "WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks?"
    authors: ["Alexandre Drouin", "Maxime Gasse", "Massimo Caccia", "et al."]
    year: 2024
    venue: "ICML 2024"
    doi: null
    url: "https://proceedings.mlr.press/v235/drouin24a.html"
    arxiv_id: null
  - title: "PerLTQA: A Personal Long-Term Memory Dataset for Memory Classification, Retrieval, and Synthesis in Question Answering"
    authors: ["Yiming Du", "Hongru Wang", "Zhengyi Zhao", "et al."]
    year: 2024
    venue: "preprint"
    doi: "10.48550/ARXIV.2402.16288"
    url: "https://doi.org/10.48550/arXiv.2402.16288"
    arxiv_id: "2402.16288"
  - title: "AgentLongBench: A Controllable Long Benchmark for Long-Contexts Agents via Environment Rollouts"
    authors: ["Shicheng Fang", "Yuxin Wang", "Xiaoran Liu", "et al."]
    year: 2026
    venue: "preprint"
    doi: "10.48550/ARXIV.2601.20730"
    url: "https://doi.org/10.48550/arXiv.2601.20730"
    arxiv_id: "2601.20730"
  - title: "Gemini 3 Pro Model Card"
    authors: ["Google DeepMind"]
    year: 2025
    venue: "model card"
    doi: null
    url: "https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf"
    arxiv_id: null
  - title: "MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks"
    authors: ["Zexue He", "Yu Wang", "Churan Zhi", "et al."]
    year: 2026
    venue: "preprint"
    doi: "10.48550/ARXIV.2602.16313"
    url: "https://doi.org/10.48550/arXiv.2602.16313"
    arxiv_id: "2602.16313"
  - title: "RULER: What's the Real Context Size of Your Long-Context Language Models?"
    authors: ["Cheng-Ping Hsieh", "Simeng Sun", "Samuel Kriman", "et al."]
    year: 2024
    venue: "preprint"
    doi: "10.48550/ARXIV.2404.06654"
    url: "https://doi.org/10.48550/arXiv.2404.06654"
    arxiv_id: "2404.06654"
  - title: "HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model"
    authors: ["Mengkang Hu", "Tianxing Chen", "Qiguang Chen", "et al."]
    year: 2025
    venue: "ACL 2025"
    doi: null
    url: "https://aclanthology.org/2025.acl-long.1575/"
    arxiv_id: null
  - title: "Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale"
    authors: ["Bowen Jiang", "Zhuoqun Hao", "Young-Min Cho", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2504.14225"
    url: "https://doi.org/10.48550/arXiv.2504.14225"
    arxiv_id: "2504.14225"
  - title: "PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory"
    authors: ["Bowen Jiang", "Yuan Yuan", "Maohao Shen", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2512.06688"
    url: "https://doi.org/10.48550/arXiv.2512.06688"
    arxiv_id: "2512.06688"
  - title: "Needle in a Haystack: Pressure Testing LLMs"
    authors: ["Gregory Kamradt"]
    year: 2023
    venue: "GitHub repository"
    doi: null
    url: "https://github.com/gkamradt/LLMTest_NeedleInAHaystack"
    arxiv_id: null
  - title: "One Thousand and One Pairs: A Novel Challenge for Long-Context Language Models"
    authors: ["Marzena Karpinska", "Katherine Thai", "Kyle Lo", "et al."]
    year: 2024
    venue: "EMNLP 2024"
    doi: "10.18653/V1/2024.EMNLP-MAIN.948"
    url: "https://doi.org/10.18653/v1/2024.emnlp-main.948"
    arxiv_id: null
  - title: "DialSim: A Real-time Simulator for Evaluating Long-Term Dialogue Understanding of Conversational Agents"
    authors: ["Jiho Kim", "Woosog Chay", "Hyeonji Hwang", "et al."]
    year: 2024
    venue: "preprint"
    doi: "10.48550/ARXIV.2406.13144"
    url: "https://doi.org/10.48550/arXiv.2406.13144"
    arxiv_id: "2406.13144"
  - title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
    authors: ["Woosuk Kwon", "Zhuohan Li", "Siyuan Zhuang", "et al."]
    year: 2023
    venue: "SOSP 2023"
    doi: null
    url: null
    arxiv_id: null
  - title: "EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents"
    authors: ["Xinze Li", "Ziyue Zhu", "Siyuan Liu", "et al."]
    year: 2026
    venue: "preprint"
    doi: "10.48550/ARXIV.2601.16690"
    url: "https://doi.org/10.48550/arXiv.2601.16690"
    arxiv_id: "2601.16690"
  - title: "Sleep-time Compute: Beyond Inference Scaling at Test-time"
    authors: ["Kevin Lin", "Charlie Snell", "Yu Wang", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2504.13171"
    url: "https://doi.org/10.48550/arXiv.2504.13171"
    arxiv_id: "2504.13171"
  - title: "FileGram: Grounding Agent Personalization in File-system Behavioral Traces"
    authors: ["Shuai Liu", "Shulin Tian", "Kairui Hu", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2604.04901"
  - title: "The Pensieve Paradigm: Stateful Language Models Mastering Their Own Context"
    authors: ["Xiaoyuan Liu", "Tian Liang", "Dongyang Ma", "et al."]
    year: 2026
    venue: "preprint"
    doi: "10.48550/ARXIV.2602.12108"
    url: "https://doi.org/10.48550/arXiv.2602.12108"
    arxiv_id: "2602.12108"
  - title: "Evaluating Very Long-term Conversational Memory of LLM Agents"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "et al."]
    year: 2024
    venue: "ACL 2024"
    doi: "10.18653/V1/2024.ACL-LONG.747"
    url: "https://doi.org/10.18653/v1/2024.acl-long.747"
    arxiv_id: null
  - title: "NoLiMa: Long-context Evaluation Beyond Literal Matching"
    authors: ["Ali Modarressi", "Hanieh Deilamsalehy", "Franck Dernoncourt", "et al."]
    year: 2025
    venue: "ICML 2025"
    doi: null
    url: "https://proceedings.mlr.press/v267/modarressi25a.html"
    arxiv_id: null
  - title: "Codex CLI"
    authors: ["OpenAI"]
    year: null
    venue: "software"
    doi: null
    url: "https://github.com/openai/codex"
    arxiv_id: null
  - title: "Update to GPT-5 System Card: GPT-5.2"
    authors: ["OpenAI"]
    year: 2025
    venue: "system card"
    doi: null
    url: "https://openai.com/index/gpt-5-system-card-update-gpt-5-2/"
    arxiv_id: null
  - title: "GPT-5 System Card"
    authors: ["OpenAI"]
    year: 2026
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2601.03267"
    arxiv_id: "2601.03267"
  - title: "OpenRouter"
    authors: ["OpenRouter"]
    year: 2026
    venue: "API"
    doi: null
    url: "https://openrouter.ai/"
    arxiv_id: null
  - title: "ReasoningBank: Scaling Agent Self-evolving with Reasoning Memory"
    authors: ["Siru Ouyang", "Jun Yan", "I-Hung Hsu", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2509.25140"
    url: "https://doi.org/10.48550/arXiv.2509.25140"
    arxiv_id: "2509.25140"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Charles Packer", "Vivian Fang", "Shishir G. Patil", "et al."]
    year: 2023
    venue: "preprint"
    doi: "10.48550/ARXIV.2310.08560"
    url: "https://doi.org/10.48550/arXiv.2310.08560"
    arxiv_id: "2310.08560"
  - title: "Qwen3.5: Towards Native Multimodal Agents"
    authors: ["Qwen Team"]
    year: 2026
    venue: "blog post"
    doi: null
    url: "https://qwen.ai/blog?id=qwen3.5"
    arxiv_id: null
  - title: "ChemAgent: Self-updating Library in Large Language Models Improves Chemical Reasoning"
    authors: ["Xiangru Tang", "Tianyu Hu", "Muyang Ye", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2501.06590"
    url: "https://doi.org/10.48550/arXiv.2501.06590"
    arxiv_id: "2501.06590"
  - title: "Beyond a Million Tokens: Benchmarking and Enhancing Long-term Memory in LLMs"
    authors: ["Mohammad Tavakoli", "Alireza Salemi", "Carrie Ye", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2510.27246"
    url: "https://doi.org/10.48550/arXiv.2510.27246"
    arxiv_id: "2510.27246"
  - title: "CocoaBench: Evaluating Unified Digital Agents in the Wild"
    authors: ["CocoaBench Team", "Shibo Hao", "Zhining Zhang", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2604.11201"
    arxiv_id: "2604.11201"
  - title: "Voyager: An Open-ended Embodied Agent with Large Language Models"
    authors: ["Guanzhi Wang", "Yuqi Xie", "Yunfan Jiang", "et al."]
    year: 2024
    venue: "TMLR 2024"
    doi: null
    url: "https://openreview.net/forum?id=ehfRiF0R3a"
    arxiv_id: null
  - title: "MEMORYLLM: Towards Self-updatable Large Language Models"
    authors: ["Yu Wang", "Yifan Gao", "Xiusi Chen", "et al."]
    year: 2024
    venue: "ICML 2024"
    doi: null
    url: "https://proceedings.mlr.press/v235/wang24s.html"
    arxiv_id: null
  - title: "Mem-α: Learning Memory Construction via Reinforcement Learning"
    authors: ["Yu Wang", "Ryuichi Takanobu", "Zhiqi Liang", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2509.25911"
    url: "https://doi.org/10.48550/arXiv.2509.25911"
    arxiv_id: "2509.25911"
  - title: "Agent Workflow Memory"
    authors: ["Zora Zhiruo Wang", "Jiayuan Mao", "Daniel Fried", "et al."]
    year: 2025
    venue: "ICML 2025"
    doi: null
    url: "https://proceedings.mlr.press/v267/wang25bx.html"
    arxiv_id: null
  - title: "LongMemEval: Benchmarking Chat Assistants on Long-term Interactive Memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "et al."]
    year: 2025
    venue: "ICLR 2025"
    doi: null
    url: "https://openreview.net/forum?id=pZiyCaVuti"
    arxiv_id: null
  - title: "Auto-scaling Continuous Memory for GUI Agent"
    authors: ["Wenyi Wu", "Kun Zhou", "Ruoxin Yuan", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2510.09038"
    url: "https://doi.org/10.48550/arXiv.2510.09038"
    arxiv_id: "2510.09038"
  - title: "Memorizing Transformers"
    authors: ["Yuhuai Wu", "Markus Norman Rabe", "DeLesley Hutchins", "et al."]
    year: 2022
    venue: "ICLR 2022"
    doi: null
    url: "https://openreview.net/forum?id=TrjbxzRcnf-"
    arxiv_id: null
  - title: "Grok 4.1 Model Card"
    authors: ["xAI"]
    year: 2025
    venue: "model card"
    doi: null
    url: "https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf"
    arxiv_id: null
  - title: "A-MEM: Agentic Memory for LLM Agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2502.12110"
    url: "https://doi.org/10.48550/arXiv.2502.12110"
    arxiv_id: "2502.12110"
  - title: "Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning"
    authors: ["Sikuan Yan", "Xiufeng Yang", "Zuchao Huang", "et al."]
    year: 2025
    venue: "preprint"
    doi: "10.48550/ARXIV.2508.19828"
    url: "https://doi.org/10.48550/arXiv.2508.19828"
    arxiv_id: "2508.19828"
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    authors: ["Shunyu Yao", "Jeffrey Zhao", "Dian Yu", "et al."]
    year: 2023
    venue: "ICLR 2023"
    doi: null
    url: "https://openreview.net/forum?id=WE_vluYUL-X"
    arxiv_id: null
  - title: "MemSkill: Learning and Evolving Memory Skills for Self-evolving Agents"
    authors: ["Haozhen Zhang", "Quanyu Long", "Jianzhu Bao", "et al."]
    year: 2026
    venue: "preprint"
    doi: "10.48550/ARXIV.2602.02474"
    url: "https://doi.org/10.48550/arXiv.2602.02474"
    arxiv_id: "2602.02474"
  - title: "ExpeL: LLM Agents are Experiential Learners"
    authors: ["Andrew Zhao", "Daniel Huang", "Quentin Xu", "et al."]
    year: 2024
    venue: "AAAI 2024"
    doi: "10.1609/AAAI.V38I17.29936"
    url: "https://doi.org/10.1609/aaai.v38i17.29936"
    arxiv_id: null
  - title: "LMEB: Long-horizon Memory Embedding Benchmark"
    authors: ["Xinping Zhao", "Xinshuo Hu", "Jiaxin Xu", "et al."]
    year: 2026
    venue: "preprint"
    doi: "10.48550/ARXIV.2603.12572"
    url: "https://doi.org/10.48550/arXiv.2603.12572"
    arxiv_id: "2603.12572"
  - title: "AMA-Bench: Evaluating Long-horizon Memory for Agentic Applications"
    authors: ["Yujie Zhao", "Boqin Yuan", "Junbo Huang", "et al."]
    year: 2026
    venue: "preprint"
    doi: "10.48550/ARXIV.2602.22769"
    url: "https://doi.org/10.48550/arXiv.2602.22769"
    arxiv_id: "2602.22769"
  - title: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
    authors: ["Shuyan Zhou", "Frank F. Xu", "Hao Zhu", "et al."]
    year: 2024
    venue: "ICLR 2024"
    doi: null
    url: "https://openreview.net/forum?id=oKn9c6ytLx"
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 6
  title: "AgentRunbook improves the query accuracy-latency frontier of memory modules"
  page: 9
  image_path: "figures/wu-2026-lme-v2-fig.png"
---

# LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues

**Authors:** Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang (UCLA)
**Published:** 2026-05 · [Source](https://arxiv.org/abs/2605.12493)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

LongMemEval-V2 (LME-V2) is a 451-question benchmark that asks whether a memory system can turn a stream of web-agent trajectories into an "experienced colleague" inside a customized environment (WebArena's OneStopShop/CMS/Reddit and WorkArena's ServiceNow). Questions probe five abilities — static state recall, dynamic state tracking, workflow knowledge, environment gotchas, and premise awareness — and are paired with two haystack tiers: 100 trajectories (~25M tokens) and ~500 trajectories per question (~115M tokens), versus a 1.39-trajectory / 310K-token oracle (i.e. ~370× scale-up). Frontier LLMs answer with zero history at only 14.1% (best, Kimi-K2.5), confirming the questions require environment-specific memory rather than parametric knowledge. The authors propose **AgentRunbook**, with two variants: **-R**, a multi-pool RAG (raw state slices + state-transition events + procedure/hint notes) that hits 58.6% accuracy at ~27s latency, and **-C**, which stores trajectories as files and invokes a Codex coding agent (GPT-5.4-mini, xhigh reasoning) augmented with a workflow document, a manifest artifact, and a trajectory-inspection helper script — reaching 74.9% on Small and 70.1% on Medium, beating vanilla Codex (69.9%/68.7%) at 32-39% lower latency (108s vs 177s on Small). Three ablations: removing the workflow doc costs the most accuracy (-4.8pp Small, -6.0pp Medium); removing manifests mainly hurts latency; helper-function effects are mixed across tiers. The headline takeaway: write-time-heavy memory (RAG with summaries/notes) loses to query-time-heavy memory (file storage + scaffolded coding agent) on every category except gotchas, but at ~6.9× the latency.

## Key Takeaway

The naive intuition says "compress the trajectory at write time so retrieval is fast and clean." This paper flips it: the best memory module barely thinks at write time — it just dumps each trajectory to disk as a JSON + screenshots folder — and concentrates all the intelligence at query time inside a sandboxed coding agent that runs `grep`, opens files, and reads screenshots until it's found exactly the evidence it needs. That counter-intuitive design (AgentRunbook-C) beats a carefully-engineered three-pool RAG by 16 accuracy points on the 25M-token haystack, because once you've discarded the raw observation at write time you cannot recover it at query time — but if you keep everything verbatim, a competent agent-as-controller can locate the needle in the haystack and return ~3 states per span. The lesson, in ENGRAM terms: an aggressive **Aggregate** stage trades accuracy for latency; the best Pareto point right now is *no aggregation at all*, with all the work pushed into **Retrieve**.

## Implications

- **[E/A] Stop digesting trajectories at insertion time if accuracy matters more than latency**: AgentRunbook-C does almost no write-time work (it just copies files) yet beats AgentRunbook-R, which spends an LLM call per state-transition and two LLM-generated notes per trajectory. If your memory layer is using an LLM extractor on every input, you are paying a write-time tax that bleeds accuracy you could have at retrieval time. Reserve aggregation for cases where query latency is the binding constraint.
- **[N] Use the file system as the memory shape for high-fidelity environment knowledge**: The authors deliberately reframe memory management as a "file management problem" (§4.2) — trajectories are directories, screenshots are PNGs, manifests are markdown summary files. This shape lets an off-the-shelf coding agent operate natively. If your memory store is already a vector DB and your agents need to inspect detailed evidence, you may be using the wrong substrate.
- **[R] Scaffolding beats a bigger model for memory-controller agents**: Adding three lightweight components — a workflow doc, query-time manifest artifacts, and a `scripts/inspect_trajectory.py` helper — lifts Codex from 69.9% to 74.9% on Small and cuts latency from 177s to 108s. Ablating the workflow doc alone costs 4.8pp; ablating the manifest costs almost no accuracy but ~30s of latency. The cheapest way to make a coding-agent memory better is not a better LLM — it's better task framing and inspection tooling.
- **[A] Decompose by granularity if you must aggregate**: AgentRunbook-R outperforms a single-pool slice+notes RAG (58.6% vs 51.0% Small) because it splits memory into three pools — raw state slices, state-transition events, and procedure/hint notes — each retrieved by a separate LLM-generated query (max 5 raw-state queries, 1 event query, 1 note query). If you must compress, multiplex the compression at different granularities and let a controller-LLM decide which streams to query.
- **[G] Provenance preservation is the silent reason file-based memory wins**: AgentRunbook-C returns evidence as `trajectory_id` + zero-based inclusive `start_state_index`/`end_state_index` spans (max 20 states per query). Every piece of returned evidence is traceable to a specific state in a specific trajectory. RAG pipelines that return summarized chunks lose this. If your agent will be questioned on "why do you believe that?", the file-pointer-with-span model is auditable in a way that vectorized-and-summarized stores are not.
- **[R+G] Gotchas resist the file-memory approach — abstention and gotcha categories need a different design**: AgentRunbook-C actually *underperforms* vanilla Codex on gotchas (0.483 vs 0.586 on Small, 0.449 vs 0.517 on Medium). The authors don't fully explain why, but it suggests subtle-failure-pattern questions need cross-trajectory reasoning that file-by-file inspection misses. If you're building memory for incident-pattern detection, plan for a different retrieval shape (probably more aggregated, not less).
- **[M] Failure trajectories are first-class memory assets**: The benchmark deliberately balances successful and failed trajectories in haystacks because "many questions can only be answered from failed trajectories" (§3.2). Memory systems that filter out failed runs at insertion are throwing away the most informative experience. The Maintain stage should retain failures with intent, not garbage-collect them.
- **[E] Sanitize task descriptions to prevent leakage between question and evidence**: For WorkArena Level-2/3 tasks, the authors rewrite the goal to strip explicit navigation hints (Table 3) — otherwise procedure questions become trivially answerable from the goal string alone. If your agent stores prompts verbatim alongside observations, your future retrieval queries may be answering themselves from the prompt rather than the experience.

## How to Apply It (method)

**Scenario:** You are building a memory layer for a long-running customer-support agent operating across your company's bespoke Zendesk-style ticketing tool plus internal admin dashboards. Over six months the agent has executed ~800 ticket-resolution trajectories. New tickets keep recurring on the same gotchas (e.g., "the customer's plan field doesn't update unless you click 'Save & Apply' rather than just 'Save'"). You want to evaluate two memory designs — a structured RAG pipeline versus a file-based coding-agent memory — and pick the better Pareto point.

**Steps:**

1. **Collect and structure the trajectory pool**: For each historical ticket, capture a directory with a `trajectory.json` containing the goal, outcome, ordered states (URL + accessibility tree text + thoughts + action), and a `screenshots/` folder with one image per state. Sanitize the goal to remove explicit navigation hints — anything the agent should *learn* rather than be told.

2. **Curate a 50-100 question evaluation set across five abilities**: For each of static-state, dynamic-state, workflow, gotcha, and premise-awareness, write ~10 questions that an experienced agent in your tool would answer correctly but a fresh GPT-5 wouldn't (because the answers are environment-specific). Verify the parametric-knowledge cutoff: run each question through a frontier model with no context and confirm <20% accuracy. For each question, annotate the answer-bearing trajectory IDs.

3. **Build the two haystacks**: A small shared haystack (~100 trajectories total, balanced success/failure), and a per-question larger haystack (~500 trajectories) where you reuse the answer-core but pad with diversity-sampled fillers.

4. **Implement Memory A — AgentRunbook-R (three-pool RAG)**:
   - **Insertion**: For each trajectory, create three pool entries. The *raw state pool* stores radius-1 windows around each state with accessibility tree + screenshot. The *event pool* uses an LLM to generate one transition note per consecutive-state pair using this prompt:
     ```
     System: You convert one UI transition from a longer task trajectory into retrieval-ready event text. Return exactly one JSON object: {"overview":"...","state_transition":"..."}. The overview briefly recaps the task goal and workflow stage. The state-transition field explicitly compares the post-state to the pre-state and describes what changed after the action.
     User: Generate an event for transition {state_i} -> {state_j}. Goal: {goal}. Outcome: {outcome}. Full action trace: {actions}. Pre-state: {url, thoughts, action, AXTree, screenshot}. Post-state: {...}.
     ```
   - The *note pool* uses an LLM once per trajectory to generate a procedure note (workflow steps) and a hint note (gotchas, durable facts).
   - Embed everything with Qwen3-Embedding-8B (or any strong dense encoder).
   - **Query**: At query time, ask the controller LLM to produce up to 5 raw-state queries + 1 event query + 1 note query as structured JSON. Retrieve top-6 events, top-3 notes, and `min(2, 6//n_queries)` raw-state results per raw-state query. Render in note-then-event-then-slice order, truncate at 200K tokens.

5. **Implement Memory B — AgentRunbook-C (file-based coding agent)**:
   - **Insertion**: Just copy the trajectory directory into a `workspace/trajectories/<id>/` location. No LLM processing.
   - **Pre-query rendering** (cheap, ~1s): Generate `TRAJECTORY_SUMMARY_CONCISE.md` and `TRAJECTORY_SUMMARY_FULL.md` manifests listing all trajectories with their goals, start URLs, action sequences, and outcomes.
   - **Query-time sandbox**: For each query, create an isolated dir containing `question.json`, `INSTRUCTION.md` (the workflow doc), the manifests, a `scripts/inspect_trajectory.py` helper (with `--state`, `--span`, `--match` modes), and a symlink to `trajectories/`.
   - **Invoke Codex CLI** with this prompt:
     ```
     You are acting as the query-time agent for Coding Agent Memory. Read the local files in this directory, especially INSTRUCTION.md and question.json. The local trajectories/ directory contains the current haystack for this evaluation item, and you must explore trajectories/ before returning your final result. Write your final result to memory_module_output.json as valid JSON. Use the local inspection helper under scripts/ when you need to inspect one trajectory, one state, one span, or match text within one trajectory quickly.
     ```
   - The agent writes `memory_module_output.json` with `{"memory_markdown": "...", "trajectory_spans": [{"trajectory_id": ..., "start_state_index": ..., "end_state_index": ...}]}`. Cap at 20 total states across spans. Render the selected states into the context passed to your fixed reader.

6. **Evaluate with the context gathering protocol**: Stream all haystack trajectories through `Insert(h)`, call `Query(q)`, truncate the returned context to your reader's budget (paper uses 200K tokens for Qwen3.5-9B), and ask the reader the question. Score with normalized string match for structured answers and an LLM judge for free-form. Report per-category accuracy and per-query latency.

7. **Compare the Pareto frontier**: Plot accuracy vs latency for both methods at multiple reasoning-effort settings (low/medium/xhigh for the coding agent; thinking-on/thinking-off for the RAG controller). Pick the operating point that fits your downstream SLA — RAG for sub-30s queries, coding-agent for accuracy-critical queries up to ~3 minutes.

**Expected outcome:** You will have empirical accuracy/latency numbers for both architectures on YOUR environment, broken down by memory ability. Expect the file-based coding-agent memory to outperform on static and dynamic state questions by ~15-20pp, the RAG memory to be competitive on workflow questions, and gotchas to be hard for both. Latency will be the tradeoff axis — choose the architecture whose Pareto point matches your downstream agent's budget.

## Best Figure

![Figure 6 — AgentRunbook improves the query accuracy-latency frontier of memory modules (page 9)](figures/wu-2026-lme-v2-fig.png)

**Image Candidates:**
- Figure 6 (p. 9): Twin accuracy–latency scatter plots (LME-V2-Small + Medium) overlaying all four method families across reasoning-effort settings — the clearest single visual of the paper's central Pareto claim.
- Table 2 (p. 9): Full results matrix with per-category accuracy and latency for all baselines + ablations across both tiers — most informative but dense.
- Figure 7 (p. 24): Stacked-bar error composition (retrieval miss major/minor, reading error, gotcha, premise) for each method on both tiers — diagnostically rich but a secondary finding.

**Best Image — Figure 6: "AgentRunbook improves the query accuracy-latency frontier of memory modules" (page 9)**

The figure overlays four method families — Baseline RAG (slice+notes), AgentRunbook-R, vanilla Codex, and AgentRunbook-C — across multiple reasoning-effort operating points (no-thinking / thinking for RAG; gpt-5.4-mini at low / medium / xhigh reasoning for the coding agents). The x-axis is query latency in seconds (0-200s), the y-axis is overall accuracy. On both tiers, AgentRunbook-C's curve dominates the upper-left corner: at any latency budget, the scaffolded coding agent achieves higher accuracy than vanilla Codex; equivalently, at any accuracy target, it runs faster. AgentRunbook-R occupies a separate cluster at much lower latency (~25s) and moderate accuracy (~0.55-0.59), making it the right choice when query speed dominates. The visual makes the paper's core argument in one glance: scaffolding shifts the Pareto frontier up-and-left, and RAG-vs-coding-agent is a budget-driven choice, not a uniform winner.

## What Experts Overlook

The detail most reviewers will skim past is buried in §4.2 and Table 11: **AgentRunbook-C's coding agent does not answer the question — it returns a structured `memory_module_output.json` with a brief `memory_markdown` analysis plus a list of `trajectory_spans` (zero-based inclusive state ranges, max 20 states total)**. The downstream `Qwen3.5-9B` reader, not Codex, produces the final answer. This split — coding-agent-as-memory-retriever-only, fixed-reader-as-answerer — is what makes the result a clean memory-system measurement rather than an end-to-end QA measurement, and it's what lets the authors honestly compare against AgentRunbook-R (same reader, different memory). Most descriptions of "coding agents as memory" would have the coding agent answer directly; this paper forces a separation of concerns that makes the evaluation interpretable.

**Why it matters:** Without this separation, an apples-to-apples accuracy comparison between RAG and coding-agent memory is impossible — you'd be measuring "Codex doing QA" against "Qwen3.5 doing QA on RAG output." By fixing the reader and varying only the memory module, the authors isolate memory quality as the independent variable. It's also a useful API pattern: if you want a coding-agent-backed memory store in your own stack, you need it to *retrieve and explain*, not *answer*, otherwise it can't be drop-in-swapped for a vector store.

**Example of good use:** A team building a memory layer for an enterprise SQL-querying agent could wire Claude Code as the memory controller, with a workflow doc that says "Find supporting tables and rows for the analyst's question. Return a JSON list of relevant table references and row ranges, plus a one-paragraph explanation. Do not run the user's analysis." The analyst's actual report-writing LLM then receives those tables + explanation and writes the report. The coding agent never sees the final analysis prompt, so it can't confuse its job with the analyst's — and you can swap in a different memory backend without rewriting the analyst's prompt.

**Example of misapplication:** A team builds the same coding-agent-backed memory but forgets the separation and lets Codex answer the user's question directly from the trajectory store. They benchmark this against a vanilla vector-store RAG with a separate reader and conclude "coding agents are 30 accuracy points better than vector RAG." What they actually measured is that GPT-5.4-mini is a better answerer than their reader-LLM — the memory component wasn't isolated. When they swap in a different reader for production, the gain disappears.

## Extracted Prompts

**Prompt explanation:** Reader system prompt for the WebArena (Magento/Postmill/Reddit) main evaluation — explicit "no guessing" instruction and `\boxed{}` answer format.

```
You are an experienced colleague in a web browsing environment that has a customized Magento-based shopping website, a customized Magento-based shopping admin CMS website, as well as a customized forum website based on Reddit/Postmill. Answer based on your memory of the environment. If you do not know the answer, output exactly \boxed{UNKNOWN}. Do not guess. Never attempt to guess an answer if you are not sure. If you believe the question's construction/premise is wrong, provide an explanation in \boxed{} explaining why the question is flawed.
```

**Prompt explanation:** Reader system prompt for the WorkArena (ServiceNow) main evaluation — identical structure, swapped domain framing.

```
You are an experienced colleague working in a customized ServiceNow environment. Answer based on your memory of the environment. If you do not know the answer, output exactly \boxed{UNKNOWN}. Do not guess. Never attempt to guess an answer if you are not sure. If you believe the question's construction/premise is wrong, provide an explanation in \boxed{} explaining why the question is flawed.
```

**Prompt explanation:** Reader user-prompt template that wraps the returned memory context with the question — the fixed interface between memory module and reader.

```
### Memory context:
{memory context returned by the memory module, after truncation}
### Question to answer:
{question text}
```

**Prompt explanation:** AgentRunbook-R note-generation prompt that turns one trajectory into a procedure note + hint note pair at insertion time. The "do not invent unseen fields" guardrail is the key grounding constraint.

```
System: You convert one UI task trajectory into two reusable memory notes for a future agent. Assume these notes will later be retrieved for unknown future questions. Preserve the workflow and the highest-value reusable facts from the touched pages. Write procedure_note and hint_note. Each note must contain title, description, and content. Use only evidence grounded in the provided goal, outcome, thoughts, annotated actions, and screenshots. Do not invent unseen fields, filters, modules, or outcomes. If the run failed, describe only the intended or attempted workflow where the evidence supports it. Keep the procedure note focused on the reliable core workflow and use the hint note for durable facts, pitfalls, option sets, confirmation signals, absent functionality, and distinctions between easily confused controls. Return only valid JSON: {"procedure_note":{"title":"...","description":"...","content":"-..."},"hint_note":{"title":"...","description":"...","content":"-..."}}.
User: Extract two reusable notes from this UI task run. Goal: {goal}. Outcome: {outcome}. Start URL: {start_url}. Each state block is followed by the screenshot for that state. The action line is the action taken from that state, annotated with recoverable object or module details.
```

**Prompt explanation:** AgentRunbook-R state-transition event-generation prompt — distills one before/after state change into a retrieval-ready event description at insertion time.

```
System: You convert one UI transition from a longer task trajectory into retrieval-ready event text. You will be given the task goal and outcome, the full annotated action trace, and one target transition defined as pre-state, annotated action, and post-state. Return exactly one JSON object: {"overview":"...","state_transition":"..."}. The overview briefly recaps the task goal and workflow stage. The state-transition field explicitly compares the post-state to the pre-state and describes what changed after the action, such as a new page, revealed panel, form fields, changed values, confirmation signal, blocker, popup, navigation, or lack of visible change. Ground the output only in the provided evidence and preserve exact UI labels when available.
User: Generate an event for transition {state_i} -> {state_j}. Goal: {goal}. Outcome: {outcome}. Full action trace: {actions}. Pre-state: {url, thoughts, action, AXTree, screenshot}. Post-state: {url, thoughts, action, AXTree, screenshot}.
```

**Prompt explanation:** AgentRunbook-R query-generation prompt run at query time by the controller LLM — emits a structured JSON bundle of multi-stream queries.

```
System: You generate structured retrieval queries for an active memory system with three pools: raw state slices, state-transition events, and procedure/hint notes. Return exactly one JSON object: {"raw_state_queries":["..."],"event_query":"...","note_query":"..."}. Maximize retrieval of memory entries that would help answer the question later. Do not answer the question yourself. Use raw-state queries for exact UI surface evidence, such as pages, forms, records, tabs, fields, buttons, dropdowns, options, labels, values, counts, and missing controls. Use the event query only when navigation, before/after change, revealed content, confirmation, blocker, popup, or workflow stage matters. Use the note query for reusable procedures, module paths, disambiguation, absent functionality, pitfalls, and durable hints. Remove formatting instructions and final-answer wrappers. Preserve exact entity names and literal UI labels. Deduplicate raw-state queries and cap them at five. Return JSON only.
User: Memory pool summary: {runtime_summary}. Output schema example: {schema_example}. Prompt examples: {few_shot_examples}. Question ID: {question_id}. Question type: {question_type}. Question text: {question}. Question image path: {image_path or <none>}. Original goals attached to this benchmark question: {original_goals}. Return only the JSON object.
```

**Prompt explanation:** AgentRunbook-C Codex invocation prompt — what the binary is launched with at query time. Notably tells the agent to *retrieve*, not *answer*.

```
You are acting as the query-time agent for Coding Agent Memory. Read the local files in this directory, especially INSTRUCTION.md and question.json. The local trajectories/ directory contains the current haystack for this evaluation item, and you must explore trajectories/ before returning your final result. If question.json refers to an image, view it carefully. Write your final result to memory_module_output.json as valid JSON. Use the local inspection helper under scripts/ when you need to inspect one trajectory, one state, one span, or match text within one trajectory quickly.
```

**Prompt explanation:** AgentRunbook-C `INSTRUCTION.md` task overview — frames the coding agent as a retrieval module with latency awareness.

```
You are acting as a quick memory retrieval module to provide contexts from agent trajectories collected from a customized web environment for a downstream reader to answer questions specific to that environment. The question is in question.json. Aggregate information from the local trajectories/ directory. Follow the workflow and do not attempt to re-verify or rebuild maps unnecessarily, since the task has latency constraints. Be quick and do not over-explore unless necessary. Work inside the current directory and never explore outside it.
```

**Prompt explanation:** AgentRunbook-C output-requirement instruction — locks the schema and explicitly handles flawed-premise (abstention) questions.

```
Write the final result to memory_module_output.json as valid JSON: {"memory_markdown":"## Support Analysis\n...\n\n## Relevant Procedure and Hint Notes\n...","trajectory_spans":[{"trajectory_id":"...", "start_state_index":0,"end_state_index":0}]}. The support analysis should briefly describe where the evidence can be found. If the evidence contradicts the premise of the question, clearly say that the premise is wrong and include the contradicting evidence. The trajectory spans must use zero-based inclusive indices and preserve order by importance.
```

**Prompt explanation:** AgentRunbook-C workflow instruction guiding the coding agent's exploration policy — manifest-first, helper-script for verification, budget caps.

```
First classify the question before opening trajectories in detail. If the question contains an image, inspect it and align it with the matching surface or state. For direct lookup questions, find an exact state showing the requested field, value, button, or page. For comparison questions, find one supporting state per side when needed. For procedure questions, stay within the same workflow family unless the question explicitly asks for a shared pattern across workflows. Start from TRAJECTORY_SUMMARY_FULL.md and shortlist only a few likely trajectories using the goal, start URL, action sequence, and final reward. Prefer the helper script for exact verification: python scripts/inspect_trajectory.py <trajectory_id>, --state <i>, --span <i:j>, or --match "<pattern>". Use the helper on shortlisted trajectories rather than performing broad raw-file search. Keep the final evidence package small, usually no more than three states per span, and use at most 20 states in total.
```

**Prompt explanation:** Abstention LLM judge prompt — used to grade flawed-premise question answers via GPT-5.2 medium-reasoning. Strict scoring: model must identify the flaw, not just say UNKNOWN.

```
System: You are a strict grader for flawed-premise (abstention) questions. Judge whether a model answer correctly identifies that the question premise is wrong, consistent with the reference answer. If the model follows the flawed premise and gives a concrete answer under that premise, it must be graded 0. If the model's final answer is just UNKNOWN / cannot determine without identifying the flaw, grade 0. If the model is contradictory (both rejects premise and also gives a concrete premise-following answer), grade 0. Paraphrases are allowed when they preserve the same core flaw described by the reference answer.
User: Evaluate whether the model correctly handled a flawed-premise question.
Question: {question_text}
Reference answer: {reference_answer}
Model full response: {model_full_response}
Model extracted final answer: {model_final_answer}
Scoring rubric: Label 1 only if the model clearly identifies the flawed premise and reaches a conclusion equivalent to the reference answer. Label 1 also if the model explicitly says it lacks access to the user's specific live environment/instance/configuration and therefore cannot verify, provided it does not give a concrete premise-following answer. Label 0 if the model follows the flawed premise and gives a concrete answer under that premise. Label 0 for generic UNKNOWN/insufficient-info replies that do not identify a flaw and do not make the explicit environment-access limitation clear. Label 0 if contradictory.
Output JSON only: {"label": 0 or 1, "reason": "short rationale"}
```

**Prompt explanation:** Gotchas LLM judge prompt — partial-coverage grading for insight-style questions.

```
System: You are a strict grader for gotchas-style insight questions. The reference answer describes the key insight(s). Grade 1 if the model response includes at least one correct insight point from the reference answer (paraphrase allowed), and does not contradict any reference point. If the model's direction is wrong, or it contains contradictions against any reference point, grade 0. If the model gives multiple points, partial coverage is enough for 1 as long as no contradictions appear.
User: Evaluate whether the model answer captures the gotcha insight.
Question: {question_text}
Reference answer: {reference_answer}
Model full response: {model_full_response}
Model extracted final answer: {model_final_answer}
Scoring rubric: Label 1 if the model includes at least one correct insight point from the reference answer (paraphrase acceptable), and does not contradict any reference point. Label 1 even if only part of a multi-point reference answer is covered, as long as there is no contradiction. Label 0 if direction is wrong (suggests opposite action/cause), even if some wording overlaps. Label 0 if any point in the model response contradicts any reference point. Label 0 if the response is irrelevant or generic without insight.
Output JSON only: {"label": 0 or 1, "reason": "short rationale"}
```

## Citations

- Wu et al. 2025a — *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory* (ICLR 2025) — the V1 predecessor; see [[wu-2024-longmemeval]].
- Packer et al. 2023 — *MemGPT: Towards LLMs as Operating Systems* (arXiv:2310.08560); see [[packer-2023-memgpt-os]].
- Chhikara et al. 2025 — *Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory* (ECAI 2025); see [[chhikara-2025-mem0]].
- Maharana et al. 2024 — *Evaluating Very Long-Term Conversational Memory of LLM Agents* (LoCoMo, ACL 2024); see [[maharana-2024-locomo]].
- Tavakoli et al. 2025 — *Beyond a Million Tokens: Benchmarking and Enhancing Long-term Memory in LLMs* (BEAM, arXiv:2510.27246); see [[tavakoli-2026-beam-light]].
- Xu et al. 2025 — *A-MEM: Agentic Memory for LLM Agents* (arXiv:2502.12110).
- Cao et al. 2026 — *Coding Agents are Effective Long-Context Processors* (arXiv:2603.20432) — the direct inspiration for AgentRunbook-C's file-system approach.
- Wang et al. 2025b — *Agent Workflow Memory* (ICML 2025) — high-level workflow consolidation inspiration.
- Ouyang et al. 2025 — *ReasoningBank: Scaling Agent Self-evolving with Reasoning Memory* (arXiv:2509.25140).
- Zhou et al. 2024 — *WebArena* (ICLR 2024) — source environment for OneStopShop, CMS, Reddit haystacks.
- Drouin et al. 2024 / Boisvert et al. 2024 — *WorkArena / WorkArena++* (ICML/NeurIPS 2024) — source environment for ServiceNow haystacks.
- He et al. 2026 — *MemoryArena* (arXiv:2602.16313) — closest prior benchmark; evaluates memory indirectly via task success.
- Zhao et al. 2026b — *AMA-Bench* (arXiv:2602.22769) — closest direct comparator; single-trajectory focus vs LME-V2's cross-trajectory.
- Fang et al. 2026 — *AgentLongBench* (arXiv:2601.20730); Li et al. 2026 — *EMemBench* (arXiv:2601.16690); Liu et al. 2026a — *FileGram* (arXiv:2604.04901) — three other 2026 agent-memory benchmarks situating LME-V2.

(Full 53-entry citation array in frontmatter.)

## Related Digests

- [[wu-2024-longmemeval]] — LongMemEval V1 (ICLR 2025): the direct predecessor — conversational long-term memory benchmark; LME-V2 shifts the substrate from user-assistant chat to web-agent trajectories and adds gotchas + workflow + multimodal evaluation.
- [[packer-2023-memgpt-os]] — MemGPT: cited as the foundational "agent-as-memory-controller" precedent. LME-V2's AgentRunbook-C generalises the MemGPT idea from tier-paging to file-system manipulation.
- [[chhikara-2025-mem0]] — Mem0: cited as the canonical write-time-distillation approach. The LME-V2 results are evidence against this paradigm for agent-trajectory memory — file storage + query-time retrieval beats write-time facts.
- [[maharana-2024-locomo]] — LoCoMo: cited as the user-user-chat memory benchmark, included in Table 1's comparison. LME-V2 explicitly contrasts its ~115M-token haystacks with LoCoMo's ~16K-token chats.
- [[tavakoli-2026-beam-light]] — BEAM: cited as one of the most recent conversational-memory benchmarks (4.5–100 sessions, 124K–10M tokens), positioned as a long-context conversational baseline next to LME-V2's agent-trajectory focus.
- [[latimer-2025-hindsight-memory]] — Hindsight Memory: same memory-architect lens; an orthogonal write-time approach (four epistemically-typed networks) that achieves SOTA on V1 LongMemEval — would be informative to evaluate on V2.
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: a sibling argument that "write-time intelligence is anti-intelligence." LME-V2 provides empirical backing — AgentRunbook-C's no-op write path beats every aggregation-heavy variant.

## Reviewer Notes

**Overall severity:** Clean

All numeric claims in the digest were cross-checked against the paper:
- 451 questions, 5 abilities — §Abstract, §3.1.
- 100 / 500 trajectories, 25M / 115M tokens — §Abstract, §3.2, Figure 3.
- 1.39-trajectory / 310.8K-token oracle baseline — Figure 3 inset.
- 14.1% best no-context accuracy (Kimi-K2.5) — Table 6.
- AgentRunbook-C overall 72.5% in abstract; 74.9% Small, 70.1% Medium in Table 2 — both reported correctly with tier disambiguation.
- Vanilla Codex 69.3% abstract / 69.9% Small / 68.7% Medium — abstract figure cited; tier-level figures from Table 2.
- 108.3s AgentRunbook-C Small latency vs 177.2s Codex Small latency — Table 2; "32-39% faster" reflects both small (108/177 = 39% reduction) and medium (139.9/185.8 = 25% reduction), so range cited is correct.
- Workflow-ablation cost on Small: 0.749 - 0.701 = 4.8pp — Table 2.
- Workflow-ablation cost on Medium: 0.701 - 0.641 = 6.0pp — Table 2.
- Gotchas: AgentRunbook-C 0.483 vs Codex 0.586 on Small, 0.449 vs 0.517 on Medium — Table 2; underperformance verified.
- Three-pool RAG 58.6% Small / 57.0% Medium — Table 2.
- Slice+notes RAG 51.0% Small / 45.9% Medium — Table 2.
- 6.9× slower (Codex vs AgentRunbook-R) — paper §1 explicitly says "about 6.9 times slower than AgentRunbook-R."
- ENGRAM dimension tags are interpretive (lens-supplied), not paper claims; they appear as bracketed labels and are framed as the digest author's mapping, not the paper's framework.

The "16 accuracy points" gap cited in Key Takeaway: 74.9 - 58.6 = 16.3pp Small. Accurate.

No fabricated facts or invented metrics detected. The Implications section's gotcha hypothesis ("cross-trajectory reasoning that file-by-file inspection misses") is flagged as the digest author's speculation, not a paper claim — the paper says only that gotcha errors persist across methods (Figure 7) without explaining the AgentRunbook-C underperformance specifically.
