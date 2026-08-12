---
corpus: agentic-memory
kind: paper-digest
slug: liu-2025-memverse
title: "MemVerse: Multimodal Memory for Lifelong Learning Agents"
authors:
  - "Junming Liu"
  - "Yifei Sun"
  - "Weihua Cheng"
  - "Haodong Lei"
  - "Yirong Chen"
  - "Licheng Wen"
  - "Xuemeng Yang"
  - "Daocheng Fu"
  - "Pinlong Cai"
  - "Nianchen Deng"
  - "Yi Yu"
  - "Shuyue Hu"
  - "Botian Shi"
  - "Ding Wang"
year: 2025
publication_date: "2025-12"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2512.03627"
doi: null
arxiv_id: "2512.03627"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "MemVerse splits agent memory into a slow hierarchical knowledge-graph long-term store (core/episodic/semantic subgraphs whose nodes/edges trace back to original multimodal chunks) plus a fast parametric model that is periodically supervised-fine-tuned on (query, retrieved-context) pairs from the graph — turning a 20-second RAG lookup into a 2.3-second parametric recall (89% faster) and lifting GPT-4o-mini ScienceQA from 76.82% to 85.48% while letting agents finally remember images, audio and video alongside text."
topics:
  - agent-memory
  - multimodal-memory
  - lifelong-learning
  - hierarchical-memory
  - knowledge-graph-memory
  - parametric-memory
  - dual-system-cognition
  - core-episodic-semantic-memory
  - periodic-distillation
  - mmkg
  - multimodal-knowledge-graph
  - sciqa
  - locomo
  - msrvtt
  - retrieval-augmented-generation
tags:
  - paper
  - memory-architecture
  - multimodal
  - lifelong-learning
  - knowledge-graph
  - parametric-memory
  - distillation
  - dual-path
  - shanghai-ai-lab
  - memverse
entities:
  - liu-junming
  - sun-yifei
  - wang-ding
  - shanghai-ai-lab
related_digests:
  - latimer-2025-hindsight-memory
  - chhikara-2025-mem0
  - packer-2023-memgpt-os
  - rasmussen-2025-zep-temporal-kg
  - tavakoli-2026-beam-light
citations:
  - title: "Language models are few-shot learners (GPT-3)"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "FireAct: Toward language agent fine-tuning"
    authors: ["Baian Chen", "Chang Shu", "Ehsan Shareghi", "Nigel Collier", "Karthik Narasimhan", "Shunyu Yao"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.05915"
  - title: "Vidbot: Learning generalizable 3D actions from in-the-wild 2D human videos"
    authors: ["Hanzhi Chen", "Boyang Sun", "Anran Zhang", "Marc Pollefeys", "Stefan Leutenegger"]
    year: 2025
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "VAST: A vision-audio-subtitle-text omni-modality foundation model and dataset"
    authors: ["Sihan Chen", "Handong Li", "Qunbo Wang", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Knowledge graphs meet multi-modal learning"
    authors: ["Z. Chen", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.05391"
  - title: "Mem0: Building production-ready AI agents with scalable long-term memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "Taranjeet Singh", "Deshraj Yadav"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.19413"
  - title: "Insight-V: Exploring long-chain visual reasoning with multimodal LLMs"
    authors: ["Yuhao Dong", "Zuyan Liu", "Hai-Long Sun", "et al."]
    year: 2025
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "VideoAgent: A memory-augmented multimodal agent for video understanding"
    authors: ["Yue Fan", "Xiaojian Ma", "Rujie Wu", "Yuntao Du", "Jiaqi Li", "Zhi Gao", "Qing Li"]
    year: 2025
    venue: "ECCV 2024 (Springer 2025)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Thinking, Fast and Slow"
    authors: ["Daniel Kahneman"]
    year: 2011
    venue: "Farrar, Straus and Giroux"
    doi: null
    url: null
    arxiv_id: null
  - title: "Dense passage retrieval for open-domain question answering (DPR)"
    authors: ["Vladimir Karpukhin", "Barlas Oğuz", "Sewon Min", "Patrick Lewis", "Ledell Wu", "Sergey Edunov", "Danqi Chen", "Wen-tau Yih"]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "2004.04906"
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks (RAG)"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2005.11401"
  - title: "BLIP-2: Bootstrapping language-image pre-training with frozen image encoders and LLMs"
    authors: ["Junnan Li", "Dongxu Li", "Silvio Savarese", "Steven C. H. Hoi"]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "2301.12597"
  - title: "Aligning vision to language: Annotation-free multimodal knowledge graph construction for enhanced LLM reasoning (VaLiK)"
    authors: ["Junming Liu", "Siyuan Meng", "Yanting Gao", "et al."]
    year: 2025
    venue: "ICCV"
    doi: null
    url: null
    arxiv_id: null
  - title: "HM-RAG: Hierarchical multi-agent multimodal retrieval augmented generation"
    authors: ["Pei Liu", "Xin Liu", "Ruoyu Yao", "Junming Liu", "Siyuan Meng", "Ding Wang", "Jun Ma"]
    year: 2025
    venue: "ACM MM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learn to explain: Multimodal reasoning via thought chains for science question answering (ScienceQA)"
    authors: ["Pan Lu", "Swaroop Mishra", "Tanglin Xia", "Liang Qiu", "Kai-Wei Chang", "Song-Chun Zhu", "Oyvind Tafjord", "Peter Clark", "Ashwin Kalyan"]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Chameleon: Plug-and-play compositional reasoning with large language models"
    authors: ["Pan Lu", "Baolin Peng", "Hao Cheng", "Michel Galley", "Kai-Wei Chang", "Ying Nian Wu", "Song-Chun Zhu", "Jianfeng Gao"]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Evaluating very long-term conversational memory of LLM agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "Mohit Bansal", "Francesco Barbieri", "Yuwei Fang"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.17753"
  - title: "MemGPT: Towards LLMs as operating systems"
    authors: ["Charles Packer", "Vivian Fang", "Shishir G. Patil", "Kevin Lin", "Sarah Wooders", "Joseph E. Gonzalez"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "Neural episodic control"
    authors: ["Alexander Pritzel", "Benigno Uria", "Sriram Srinivasan", "Adrià Puigdomènech Badia", "Oriol Vinyals", "et al."]
    year: 2017
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemoRAG: Boosting long context processing with global memory-enhanced retrieval augmentation"
    authors: ["Hongjin Qian", "Zheng Liu", "Peitian Zhang", "Kelong Mao", "Defu Lian", "Zhicheng Dou", "Tiejun Huang"]
    year: 2025
    venue: "WWW 2025"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning transferable visual models from natural language supervision (CLIP)"
    authors: ["Alec Radford", "Jong Wook Kim", "Chris Hallacy", "Aditya Ramesh", "Gabriel Goh", "Sandhini Agarwal", "et al."]
    year: 2021
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "2103.00020"
  - title: "Robust speech recognition via large-scale weak supervision (Whisper)"
    authors: ["Alec Radford", "Jong Wook Kim", "Tao Xu", "Greg Brockman", "Christine McLeavey", "Ilya Sutskever"]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Supermemory"
    authors: ["Dhravya Shah", "Mahesh Sanikommu", "Yash", "et al."]
    year: 2025
    venue: "supermemory.ai"
    doi: null
    url: "https://supermemory.ai/"
    arxiv_id: null
  - title: "Memory-R1: Enhancing large language model agents to manage and utilize memories via reinforcement learning"
    authors: ["Sikuan Yan", "Xiufeng Yang", "Zuchao Huang", "Ercong Nie", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2508.19828"
  - title: "Mirix: Multi-agent memory system for LLM-based agents"
    authors: ["Yu Wang", "Xi Chen"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2507.07957"
  - title: "MemoryLLM: Towards self-updatable large language models"
    authors: ["Yu Wang", "Yifan Gao", "Xiusi Chen", "Haoming Jiang", "Shiyang Li", "Jingfeng Yang", "Qingyu Yin", "Zheng Li", "Xian Li", "Bing Yin", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.04624"
  - title: "MemViT: Memory-augmented multiscale vision transformer for efficient long-term video recognition"
    authors: ["Chao-Yuan Wu", "Yanghao Li", "Karttikeya Mangalam", "Haoqi Fan", "Bo Xiong", "Jitendra Malik", "Christoph Feichtenhofer"]
    year: 2022
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "MSR-VTT: A large video description dataset for bridging video and language"
    authors: ["Jun Xu", "Tao Mei", "Ting Yao", "Yong Rui"]
    year: 2016
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "A-Mem: Agentic memory for LLM agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "Hang Gao", "Juntao Tan", "Yongfeng Zhang"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.12110"
  - title: "ReAct: Synergizing reasoning and acting in language models"
    authors: ["Shunyu Yao", "Jeffrey Zhao", "Dian Yu", "Nan Du", "Izhak Shafran", "Karthik R Narasimhan", "Yuan Cao"]
    year: 2023
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Agent Lumos: Unified and modular training for open-source language agents"
    authors: ["Da Yin", "Faeze Brahman", "Abhilasha Ravichander", "Khyathi Chandu", "Kai-Wei Chang", "Yejin Choi", "Bill Yuchen Lin"]
    year: 2024
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemAgent: Reshaping long-context LLM with multi-conv RL-based memory agent"
    authors: ["Hongli Yu", "Tinghong Chen", "Jiangtao Feng", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2507.02259"
  - title: "MemGen: Weaving generative latent memory for self-evolving agents"
    authors: ["Guibin Zhang", "Muxin Fu", "Shuicheng Yan"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2509.24704"
  - title: "A survey on the memory mechanism of large language model-based agents"
    authors: ["Zeyu Zhang", "Quanyu Dai", "Xiaohe Bo", "Chen Ma", "Rui Li", "Xu Chen", "Jieming Zhu", "Zhenhua Dong", "Ji-Rong Wen"]
    year: 2025
    venue: "ACM Trans. Inf. Syst. 43(6)"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "He Ye", "Yanlin Wang"]
    year: 2024
    venue: "AAAI 38(17):19724-19731"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multi-modal knowledge graph construction and application"
    authors: ["Xiangru Zhu", "Zhixu Li", "Xiaodan Wang", "Xueyao Jiang", "Penglei Sun", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2202.05786"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "MemVerse architecture: short-term + long-term MMKG + parametric memory orchestrated by a memory orchestrator"
  page: 4
  image_path: "figures/liu-2025-memverse-fig.png"
---

# MemVerse: Multimodal Memory for Lifelong Learning Agents

**Authors:** Junming Liu, Yifei Sun (equal contrib.); Weihua Cheng, Haodong Lei, Yirong Chen, Licheng Wen, Xuemeng Yang, Daocheng Fu, Pinlong Cai, Nianchen Deng, Yi Yu, Shuyue Hu, Botian Shi, Ding Wang (corresponding) — Shanghai Artificial Intelligence Laboratory
**Published:** 2025-12 · [Source](https://arxiv.org/abs/2512.03627)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MemVerse (Shanghai AI Lab, Dec 2025) is a model-agnostic, plug-and-play memory framework that explicitly rejects the choice between parametric-only (rigid, opaque, catastrophic-forgetting) and RAG-only (flat, noisy, no abstraction) by running both at once: a slow non-parametric pathway organised as three knowledge-graph subgraphs (`core` for durable user-specific facts/preferences, `episodic` for time-ordered events, `semantic` for generalisable concept/entity relations) where every node v and relation r retains pointers ℓ_v(v), ℓ_r(r) back to its supporting raw text chunks (and through them to the original multimodal data via cross-modal alignment), plus a fast parametric pathway implemented as a 7B-parameter Qwen2.5 that is *supervised-fine-tuned on (question q, retrieved context R) pairs harvested from the graph* so it learns to "emulate the retrieval behavior of LTM within its parametric space" — minimising L_update = −Σ log P_Θ(r_t | q, r_{<t}). Multimodal inputs (images via GPT-4o-mini captions, audio via Whisper, video via VLM frame-captions) are first translated into text S = D_text(A(E_mod(M))), chunked, then graph-extracted via G = Φ_LLM(C) = (V, R). A central rule-based memory orchestrator (no trainable params) routes additions/updates/deletions/retrievals across short-term (sliding window of the last K turns), long-term MMKG, and the parametric model. Empirically: on ScienceQA, GPT-4o-mini + MemVerse hits 85.48% average (vs 76.82% baseline, +8.66 pp) and Qwen2.5-72B + MemVerse hits 80.25% (vs 78.37%, +1.88 pp); on MSR-VTT text-to-video R@1 jumps from CLIP's 29.7% to 90.4% (+60.7 pp) and video-to-text from 21.4% to 89.2% (+67.8 pp); on latency the parametric path takes 2.28 s/query vs 8.26 s for LTM-only retrieval and 20.17 s for full RAG — a 72% / 89% speedup. Released at github.com/KnowledgeXLab/MemVerse. **Most useful takeaway:** the *write-back loop from retrieved (q, R) into a small fine-tunable LLM* is a concrete, low-cost way to give an agent operating-system the equivalent of "skill compilation" — frequently-retrieved knowledge stops paying the RAG tax because it migrates into parameters, while the graph stays as the slow-but-traceable backing store.

## Key Takeaway

The interesting move in MemVerse is not the four memory types (Hindsight has four too; Mem0 has two; MemGPT has paged blocks). It's that **the parametric memory is built by training on the output of the graph retriever** — periodic supervised fine-tuning of a 7B model on (q, R) pairs sampled from the LTM construction pipeline (eqn 9: L_update = −Σ log P_Θ(r_t | q, r_{<t})), with dynamic expansion at each step t adding ∆Θ_t to the previous parameter state (eqn 10). The graph is the slow, traceable, interpretable substrate; the small LLM is its "cache" that compounds with use, gives 89% retrieval speedup, and crucially can be cold-evicted (just re-init Θ_pretrained) without losing any knowledge because the graph is the canonical source. Stated as a lesson: **periodic distillation of retrieval outputs into a small parametric layer is how a memory architecture turns "retrieval" into "skill" — the system literally gets faster at recurring queries the more it sees them, without conflating that with the underlying ground truth.**

## Implications

- **Adopt dual-pathway memory: slow graph for ground truth, fast small LLM for hot paths.** This is the cleanest write-time-vs-query-time partition I've seen in the wiki so far. Hindsight pushes write-time (four typed networks, narrative extraction); Storage-Is-Not-Memory (Adler 2026) pushes query-time (verbatim raw store, multi-stage retrieval). MemVerse argues both, with a phase boundary: the graph is the authoritative write-time structure, the parametric model is a *learned cache* for query-time speed. For Flow OS / QMD this maps to: keep the markdown vault + entity graph as the canonical substrate, but also train a small 1.5–7B model on (recent-query, qmd-retrieval-output) pairs so common queries stop paying the BM25+vector tax. `[E, R, A]`

- **Triple-subgraph LTM (core / episodic / semantic) is a richer type system than Hindsight's W/B/O/S.** MemVerse's three subgraphs map cleanly onto cognitive psychology (Tulving): core = user-specific durable facts (this is roughly Hindsight's `Observation`); episodic = time-ordered event entries (Hindsight's `Experience`); semantic = abstract concept/entity relations (no Hindsight equivalent — Hindsight collapses this into `World`). The MemVerse split is sharper on *abstraction level* than Hindsight's split on *epistemic source*. The two schemas are orthogonal and combinable: a v3 schema could index every memory cell as `(epistemic_type ∈ {W,B,O,S}) × (abstraction_level ∈ {core, episodic, semantic})`. `[E, N]`

- **Every graph node/edge must keep a back-pointer to source chunks (provenance discipline).** ℓ_v: V → P(C) and ℓ_r: R → P(C) maintain persistent references from each entity v / relation r to its supporting text chunks (eqns 5, 6). This is what makes the digest-of-evidence auditable — you can always reconstruct the raw conversational basis for any abstract claim, and through cross-modal alignment trace back to the original image/audio/video. For Flow OS's contacts/companies/observation cards, this is the missing provenance layer: every claim in an Observation should point at the session-extraction chunks that produced it, so the user can verify and the system can re-derive on edit. `[G]`

- **Multimodal inputs should be canonicalised to text early, with a back-pointer kept to the original modality.** MemVerse handles arbitrary modalities by running them through pretrained MLLMs (GPT-4o-mini for images, Whisper for audio, VLM frame-sampling for videos) into descriptive text tokens S = D_text(A(E_mod(M))) — then the text S serves as the chunk the graph indexes, but "activating an entity or relation in G simultaneously triggers the corresponding original dialogue text C and any associated multimodal data M." This bilingual-by-design approach (graph in text, payload in original modality) is the practical recipe for a multimodal second brain. `[E, N]`

- **Periodic distillation, not online updates, for parameter-write — and start fresh from Θ_pretrained.** Crucial design discipline: the parametric memory updates are periodic (driven by graph expansion at update step t), not per-query streaming; initialisation is M^0_parametric = Θ_pretrained (a clean base, not a previous parametric memory). This is what prevents the catastrophic forgetting + interference the paper indicts parameter-embedded memory for in §1. The graph is the consolidated truth; the parametric layer is a stateless-able cache rebuilt from it. `[A, M]`

- **The parametric pathway is what makes "as-fast-as-built-in-knowledge" possible.** 20.17 s → 8.26 s → 2.28 s per query (RAG → LTM-only retrieval → parametric) is the latency budget that decides whether agents feel responsive at conversational scale. The parametric step's accuracy "remains similar" to LTM retrieval (paper's claim, modestly hedged in §4.2). For agentic OS use cases where the agent answers from memory dozens of times per session, a ~9× speedup on the dominant path is the difference between an agent and a slow chatbot. `[R]`

- **Memory effectiveness varies a lot by host model — GPT-4o-mini gets +8.66 pp on ScienceQA, Qwen2.5-72B only +1.88 pp.** §4.2 surfaces an under-discussed dependency: "GPT-based models are more capable of leveraging retrieved knowledge... In contrast, Qwen struggles to connect retrieved content with the question context, which can result in errors even when correct information is retrieved." Memory-retrofit gains are not free; they require an instruction-tuned model that knows how to *use* injected context. For my own QMD-fed sessions, this suggests prompt-design discipline matters as much as retrieval quality. `[R, A]`

- **MMKG construction with explicit modality alignment is feasible with GPT-4o-mini at acceptable cost.** All MMKG construction in the paper uses GPT-4o-mini as the LLM for both extraction and retrieval (§4.1 Implementation). The whole pipeline runs on a single A100 80G GPU for fine-tuning. This is well within personal-second-brain budget. The recipe for Flow OS: a nightly job that pulls new session captures, runs GPT-4o-mini to extract entities/relations into core/episodic/semantic subgraphs, links nodes to source chunks, optionally fine-tunes a Qwen2.5-1.5B on the resulting (q, R) pairs. `[E, A]`

- **Sliding-window short-term memory is just K most-recent turns — don't over-engineer it.** M_STM = {q_{t-K+1}, ..., q_t} is a literal sliding window over the dialogue queue (eqn 2). No semantic compression, no decay function, no policy. The paper's argument: "the contextual information in a short dialogue session is already captured within this window" so frequent consolidation into LTM is wasteful. Lesson: don't bolt an over-clever STM onto the front of a sophisticated LTM; keep STM dumb and let the consolidation step (periodic graph expansion) do the abstraction work. `[N, A]`

- **The headline MSR-VTT jump (29.7% → 90.4%) needs a caveat asterisk.** The 60.7 pp improvement over CLIP baseline on text-to-video R@1 is real but the paper's own explanation in §4.2 acknowledges that during MMKG construction, "pairs of captions (the original caption and the caption generated from the video) are partially aligned and connected through GPT-4o-mini's powerful understanding... forming linked representations." The author insists ground-truth alignment is not exposed — but the *captioning model* GPT-4o-mini sees both modalities at construction time and creates the link structure. The retrieval benchmark is therefore essentially "can we retrieve when a strong VLM has pre-built the cross-modal index?" — which is impressive systems engineering but not directly comparable to pure CLIP-style alignment. Treat the 90% as "the MMKG construction step pays off heavily when the test happens to be a multimodal retrieval task that the construction step structures for." Stronger numbers on ScienceQA (a reasoning task, not a memorisation task) are the more transferable result. `[R, G]`

## How to Apply It (method)

**Scenario:** You're running Flow OS's memory layer. The vault has ~45 paper digests, growing contacts/companies/ventures cards, and session-extracted memories across 6+ ventures. Today: QMD does BM25+vector hybrid over markdown files, no graph, no entity resolution, no parametric cache. Queries take 5–15 s when the corpus is hot; recall is decent for keyword-matching questions but poor for "what's the chain across these three ventures that led me to pause Ride Ready" (requires multi-hop graph walk) and "what's the fastest way for the agent to answer 'who is Marcus Webb' without re-deriving it from 12 session chunks every time" (requires a parametric cache). You want to retrofit MemVerse-style dual-path memory on top of QMD without replacing it. This maps to ENGRAM's Encode (modality → text → chunks), Network (vault + KG + parametric), Aggregate (periodic graph extraction + periodic distillation), Retrieve (orchestrator routes to STM / LTM-graph / parametric), Maintain (periodic re-init of parametric from current graph state).

**Steps:**

1. **Add a `kind: knowledge-graph-node` and `kind: knowledge-graph-edge` to v2 frontmatter, with provenance back-pointers.** Each node (entity slug, e.g. `tom-parker`) and edge file stores the list of source chunk IDs (markdown file path + line range) that support it. Pseudocode:

   ```yaml
   ---
   kind: knowledge-graph-node
   entity: tom-parker
   subgraph: core            # core | episodic | semantic
   supporting_chunks:
     - file: memory/contacts/tom-parker.md
       lines: 1-30
     - file: experiences/captures/2026-04-17-session.md
       lines: 45-67
   ---
   ```

   This is the ℓ_v back-pointer. Every claim in any abstract card can be traced to raw evidence — the foundation of the provenance discipline.

2. **Build the three subgraphs by running GPT-4o-mini extraction over the vault.** Nightly job (or on-demand via `/learn`):
   - Pull all markdown files modified in the last N days
   - Chunk into 500-token windows
   - For each chunk, prompt GPT-4o-mini: "Extract entities and typed relations. Classify each entity as `core` (durable user-specific fact / preference), `episodic` (time-bound event), or `semantic` (general concept/relation). Output JSON: `{entities: [{slug, type, ...}], relations: [{subject, predicate, object, ...}]}`."
   - Merge new entities/relations into the existing graph; for collisions, prefer the most recent supporting chunk; resolve entity duplicates by string + co-occurrence + temporal similarity (MemVerse's ρ(m) = argmax_e [α·sim_str + β·sim_co + γ·sim_temp] from the related Hindsight work).

3. **Wrap QMD's retrieval with an orchestrator that fans out across STM, LTM-graph, parametric.** Replace `qmd query "..."` calls with:

   ```python
   def recall(query, token_budget=8000, latency_budget_ms=3000):
       # 1) STM: last K=10 turn embeddings from current session
       stm_hits = current_session.last_k(K=10, matching=query)
       # 2) Parametric: if a small fine-tuned LLM is loaded, ask it first
       if parametric_model_loaded():
           para_answer = parametric_model.generate(query, max_tokens=512)
           if confidence(para_answer) > 0.85:
               return para_answer  # 2.3 s path
       # 3) LTM-graph: spreading activation from query embedding seeds
       ltm_hits = graph_walk(query, max_hops=2)
       # 4) Fuse via RRF (k=60), then cross-encoder rerank
       fused = rrf_fuse([stm_hits, ltm_hits], k=60)
       reranked = cross_encoder.rerank(query, fused, top_k=100)
       # 5) Greedy pack to token_budget
       return pack_to_budget(reranked, token_budget)
   ```

4. **Train the parametric memory weekly on (q, R) pairs harvested from the orchestrator's own logs.** Once a week:
   - Log every `recall(query)` call with `(query, retrieved_chunks, was_helpful?)` tuples (the last from user feedback or downstream task success)
   - Build a training set of (q, R) pairs where R is the helpful retrieved context
   - Fine-tune a Qwen2.5-1.5B (smaller than the paper's 7B — personal-scale budget) with the paper's loss: L = −Σ log P_Θ(r_t | q, r_{<t}). Single A100 or even RTX 4090 with bf16 + gradient checkpointing is enough.
   - **Always re-init from Θ_pretrained**, never from the prior week's parametric memory. The graph is the source of truth; the parametric model is a re-derivable cache. This is the paper's eqn 8 discipline.

5. **For multimodal inputs, canonicalise to text + keep payload pointers.** When `/capture` ingests an audio clip, image, or video:
   - Run Whisper / GPT-4o-mini / VLM frame-captioner to produce descriptive text S
   - Store S as the chunk content; store the original file path in frontmatter as `payload: { modality: audio|image|video, path: ... }`
   - When the graph extractor processes the chunk, the entities/relations link back to S, which links back to the payload — so "show me the audio that led me to add Marcus Webb as a contact" works.

6. **Implement the orchestrator as rule-based, not learned.** MemVerse's orchestrator is explicitly "rule-based control logic without introducing additional trainable parameters." This is the right call for personal-scale systems: a learned router adds opacity and a training-data dependency for no clear benefit on the small set of routing decisions (which subgraph, which channel, how much budget). Hard-code the rules: STM is checked when query has temporal markers ("today", "earlier", "just now"); parametric is checked first when query looks like a recall question on a well-trodden entity (high `entity_query_frequency` from logs); LTM-graph is the fallback.

7. **Evaluate on a private LongMemEval-style benchmark with three arms.** Mirror the methodology from Hindsight (already in the wiki — `latimer-2025-hindsight-memory.md`) but extend to test the parametric path specifically:
   - **A**: QMD hybrid only (current baseline)
   - **B**: QMD + orchestrator + LTM-graph (no parametric cache)
   - **C**: full MemVerse retrofit (orchestrator + STM + LTM-graph + weekly-trained parametric Qwen2.5-1.5B)
   
   Measure: accuracy on multi-hop / cross-venture questions (paper predicts B → A buys gains here), latency on hot-path queries (paper predicts C → B drops from ~5 s to ~1 s), and the *graceful degradation* property — if you delete the parametric weights, does C drop to B's accuracy? (Should, because graph is the canonical source.)

8. **Schedule the periodic distillation at session boundaries.** Don't run the weekly parametric training cron-blind. Tie it to `/save` events — when a substantial session ends and `/learn` has updated the graph, *that's* the trigger to refresh the parametric layer. This matches MemVerse's "periodic update strategy" (paper's Appendix D ablation) which they find is more stable than per-turn updates.

9. **Diagnostic: log which path served each query, and what the speedup was.** For every `recall()` call, log `{path: stm|parametric|ltm-graph|fused, latency_ms, accuracy_proxy}`. After a month, you'll see the distribution — if 80% of queries go through `parametric` at 2 s but 20% go through `ltm-graph` at 8 s, you know where to invest in graph optimisation. If `parametric` accuracy drops below 0.85 confidence threshold often, you're overfitting the cache and need to slow the distillation cadence or shrink the model.

10. **Graceful invalidation on graph edits.** When `/learn` updates the graph (a new fact added, an entity merged, an edge re-typed), mark the parametric model as `stale` rather than re-training immediately. Next session-end triggers re-distillation. This avoids re-training on every minor edit while still preserving the "graph = source of truth" invariant.

11. **Keep the STM dumb.** Implement `M_STM = {q_{t-K+1}, ..., q_t}` literally — last K=10 turns in the current session, with embeddings, end of story. Don't add LRU, don't add salience scoring, don't try to be clever. The paper's empirical claim is that STM contributes "relatively little" on ScienceQA (a non-sequential benchmark) but the architectural insight is that STM is just a recent-context buffer, not a memory tier with its own policy. The cleverness lives in LTM.

12. **Watch for the cross-modal MMKG construction trap.** MemVerse's MSR-VTT result is partly an artifact of the construction step doing the heavy lifting (GPT-4o-mini sees both modalities and builds cross-modal links). If you set up Flow OS's MMKG, be explicit in the eval that the construction-time alignment is "free" — the real test is queries where construction-time didn't see the pairing it has to recall, just like in real-world unseen-data deployment.

**Expected outcome:** A retrofit memory layer that (a) gives Flow OS a 3-subgraph (core / episodic / semantic) LTM grounded in markdown chunks with full provenance, (b) introduces a small parametric Qwen2.5-1.5B cache that compounds with usage and drops hot-path latency from ~5 s to ~2 s, (c) keeps the markdown vault as the canonical source so any parametric drift is recoverable, (d) handles multimodal captures (voice, screenshots, video clips) through a unified text-canonical pipeline with payload back-pointers. The diagnostic logs let you tune the orchestrator's routing rules empirically; the periodic distillation schedule prevents the parametric layer from interfering with itself.

## Best Figure

![Figure 2 — MemVerse architecture (page 4)](figures/liu-2025-memverse-fig.png)

**Figure Name:** Figure 2: "MemVerse integrates three memory components: short-term memory for recent context, long-term memory structured as a multimodal knowledge graph, and parametric memory as a lightweight neural model for fast context encoding."

**Figure Page:** 4

**Slide Caption:** MemVerse's architecture: a central rule-based memory orchestrator routes between three memory components — Short-term Memory (sliding window over the recent conversation queue), Long-term Memory (a multimodal knowledge graph with entity nodes and typed relations, every node back-pointed to its supporting text chunks and to the original multimodal payload), and Parametric Memory (a small fine-tunable LLM trained on (q, R) pairs harvested from the LTM retrievals). Multimodal user input is canonicalised to text, fed to all three; queries are fanned out and responses fused.

**Description:** Figure 2 is the canonical architecture diagram. Three vertical bands. Left band: multimodal user input flows through the orchestrator into a "Retrieved Memory" return path. Center-left: Short-term Memory shown as a "Recent Conversations List" with 4 example queued queries. Center-right: Parametric Memory shown as a small neural network that takes the query and outputs context, with arrows back to "Train" pointing at the long-term store. Right band: Long-term Memory shown as a multimodal knowledge graph — entity nodes (e.g. "British Shorthair", "cat", "coat", "Mia", "Hawaii", "Kobe Bryant", "Waikiki Beach") connected by typed edges (`wear`, `perched`, `breed`, `designs`, `raises`, `visits`, `admires`, `features`) with attached image chunks (cat with sunglasses, scientist, beach scene) — these are the `Relation`, `Image of`, `Chunk of` links visualised. A `Store` arrow runs from short-term to long-term; a `Train` arrow runs from long-term to parametric. The agent and API access on the left feed user queries through the orchestrator. The figure matters because it makes legible in one view the system's central architectural claim: memory is partitioned by *speed of access* (STM fastest, parametric fast-cached, LTM slow but authoritative) rather than by epistemic type (which is how Hindsight cuts it), and the parametric model is *constructed by training on the graph's retrieval outputs* — making it a learned shortcut rather than an independent memory store.

**Other strong candidates:**
- **Figure 1 (p. 2)** — Side-by-side comparison of without-memory vs with-MemVerse responses across four modalities (audio, image, video, text). The cleanest illustration of the multimodal-memory failure mode (hallucinated answer about "Truffles the Kitty" with no grounding vs the grounded "Mia owns the British Shorthair kitten" with provenance).
- **Table 1 (p. 7)** — ScienceQA results matrix; the 76.82 → 85.48 jump for GPT-4o-mini is the paper's strongest reasoning-task evidence.
- **Table 2 (p. 8)** — MSR-VTT video-text retrieval matrix; the 29.7 → 90.4 R@1 is the most eye-catching but caveated number (see the implications discussion).

## What Experts Overlook

Most readers will fixate on the multimodal angle (the paper's title and Figure 1 push it heavily) and miss the *training loop that makes the parametric memory work*. The detail almost everyone will skip is in §3.2 (Parametric Memory) and §3.2's "Memory Initialization" subsection: **the parametric memory is always re-initialised from the pretrained base model Θ_pretrained, not from the previous parametric memory state, before each round of supervised fine-tuning on the latest (q, R) pairs.** The dynamic-memory-expansion equation M^{t+1}_parametric = M^t_parametric + ∆Θ_t (eqn 10) at first reading looks like a streaming online update, but read with the initialization clause it actually means *the parametric memory is a periodically rebuilt cache, not an accumulating model*. The graph is the canonical store; the parametric model is a re-derivable shortcut. This is what insulates the system from the catastrophic-forgetting failure mode the paper indicts parameter-embedded memory for in §1 — because every periodic rebuild starts from a clean base, you can never have stale knowledge stuck in parameters that the graph no longer supports. Hindsight's opinion reinforcement (small Δc steps to evolve confidence without overwriting history) is the equivalent discipline for belief evolution; MemVerse's "always re-init from pretrained" is the equivalent for parametric caching.

**Why it matters:** This is the architectural commitment that makes the parametric pathway a *cache* rather than a *parallel memory store*. A cache can be invalidated; a parallel store accumulates drift. A team that reads only §3.2's main text and not the initialization clause might build a parametric layer that fine-tunes incrementally from the prior parametric state — and within a few months their "fast memory" has silently diverged from their graph, with no way to detect or recover. The fact that this is a one-line discipline buried in a sub-subsection of the methodology, not flagged in the abstract or contributions, is exactly the kind of design decision that gets lost in implementation. For Flow OS / QMD: when you build the parametric layer, ALWAYS re-init from Θ_pretrained on every distillation cycle. Document this as a non-negotiable architectural invariant.

**Example of good use (memory architectures for agentic OSes):** Implementing the Flow OS retrofit, you set up the weekly parametric training cron to:
1. Load Θ_pretrained (e.g. fresh Qwen2.5-1.5B checkpoint from disk — cached locally, no download)
2. Sample (query, retrieved-context) pairs from the past week's `recall()` logs where the user marked the response helpful (or where downstream task succeeded)
3. Fine-tune for ~1 epoch on this dataset
4. Write the new parametric weights to a versioned path (`memory/parametric/v-2026-W21.bin`)
5. Atomic-swap the symlink `memory/parametric/current.bin` → new path
6. Delete the previous week's weights (no need to keep them — graph is the source)

This gives you: (a) a parametric cache that compounds with use, (b) full recoverability if anything goes wrong (just delete the binary and let next week's cron rebuild), (c) the discipline that the parametric layer can never silently contradict the graph because it's always re-derived from it. The fast path stays in sync; the slow path stays canonical.

**Example of misapplication:** A team adopts MemVerse's dual-path architecture but implements parametric updates as continual streaming — every new (q, R) pair gets a small gradient step into the parametric model in real-time, with the model state persisted across sessions. They argue this is "more responsive" because the parametric cache learns from each interaction immediately. What breaks: as the graph evolves (a fact gets corrected, an entity gets merged, a relation gets retyped), the parametric model retains traces of the old graph state in its weights — and because there's no periodic re-init from Θ_pretrained, those traces accumulate. After three months, the parametric model is answering "Marcus Webb works at AcmeCorp" because that was true in week 4, but the graph has since recorded the move to NewCorp. The orchestrator preferentially serves from parametric (it's faster), so the user sees the stale answer for routine queries — and the only way to detect the drift is to bypass the parametric layer and compare answers, which the system isn't designed to do because the architects assumed parametric and graph would stay in sync. The lesson missed: **the periodic re-init from pretrained is what makes parametric a cache, not a memory.** Without it, you have two memory stores that drift apart silently, and the faster one wins by default.

## Extracted Prompts

**Prompt explanation:** Multimodal-to-text canonicalisation (§3.1, Multimodal Processing) — the operational recipe for handling arbitrary input modalities by translating to text before graph indexing. Not given verbatim as a system prompt in the paper, but reconstructed from the methodology equation S = D_text(A(E_mod(M))) and §4.1 Implementation:

```
For modality M ∈ {image, audio, video}:
  - image:   prompt GPT-4o-mini with "Describe this image in detail, listing all
             objects, people, settings, colors, and any text visible. Focus on
             entities that could be referenced later: named persons, distinctive
             objects, locations, brand marks."
  - audio:   run Whisper transcription → text S
  - video:   sample frames at 1 fps (or scene-change boundaries); caption each
             frame with the image prompt above; concatenate captions in temporal
             order with timestamps.
Output: text S that serves as the chunk for graph extraction.
Preserve: a back-pointer to the original payload file path so retrieval can
return the multimodal evidence, not just the text description.
```

**Prompt explanation:** Knowledge graph construction (§3.1, Long-Term Memory; eqn 4 G = Φ_LLM(C) = (V, R)) — the LLM prompt that converts a chunked text segment into entity nodes and typed relation edges. Reconstructed from the paper's methodology description (§3.1, §4.1) since no verbatim prompt is provided:

```
You are an entity-and-relation extractor for a knowledge graph used by an
agentic AI memory system.

Given the text chunk below, extract:
1. ENTITIES: each as {slug, type ∈ {core, episodic, semantic}, canonical_name,
   aliases?, supporting_quote}
   - core: a user-specific durable fact or preference (e.g. user's name,
     long-standing preference, family member)
   - episodic: a time-bound event the user participated in or witnessed
     (e.g. a meeting, a decision moment)
   - semantic: a generalisable concept, person, place, or object referenced
     in the text but not specific to the user (e.g. "British Shorthair cat
     breed")
2. RELATIONS: each as {subject_slug, predicate, object_slug, supporting_quote,
   confidence ∈ [0,1]}
   - predicate is a verb phrase or typed relation (e.g. "owns", "wears",
     "discussed_with", "decided_on")
3. PROVENANCE: for every entity and relation, the supporting_quote field
   must be a verbatim span from the source chunk that justifies the claim.

Be conservative: prefer fewer high-confidence relations over many speculative
ones. If the chunk does not mention an entity explicitly, do NOT add it from
your own knowledge.

Output JSON only:
{
  "entities": [{...}, ...],
  "relations": [{...}, ...]
}
```

**Prompt explanation:** Parametric memory training input format (§3.2, Training Implementation, eqn 11) — the exact format used to construct (q, R) supervised-fine-tuning pairs for the parametric memory model:

```
Prompt: "Question: {q} Choices: {c1}, {c2}, ..., {cn}"

Target (R): {retrieved context from the explicit memory module}

Training loss: L_update = −Σ log P_Θ(r_t | q, r_{<t})

Hyperparameters used:
  - sequence length: 2048
  - optimizer: AdamW
  - learning rate: 2e-6
  - LR scheduler: linear with 10% warm-up steps
  - gradient clipping: max-norm 1.0
  - mixed precision: bfloat16
  - gradient checkpointing: on
  - hardware: single A100 80G GPU
  - base model: Qwen2.5-7B (any pretrained LLM/VLM works)
  - initialization: M^0_parametric = Θ_pretrained (always start from base; do
    NOT continue training from previous parametric memory checkpoint)
```

## Citations

First 10 (see frontmatter for full list of 36 references):

- Brown et al. (2020) — *Language models are few-shot learners (GPT-3)* — NeurIPS, arXiv:2005.14165
- Chen et al. (2023) — *FireAct: Toward language agent fine-tuning* — arXiv:2310.05915
- Chhikara et al. (2025) — *Mem0: Building production-ready AI agents with scalable long-term memory* — arXiv:2504.19413
- Kahneman (2011) — *Thinking, Fast and Slow* — Farrar, Straus and Giroux
- Karpukhin et al. (2020) — *Dense passage retrieval for open-domain question answering (DPR)* — EMNLP, arXiv:2004.04906
- Lewis et al. (2020) — *Retrieval-augmented generation for knowledge-intensive NLP tasks (RAG)* — NeurIPS, arXiv:2005.11401
- Li et al. (2023) — *BLIP-2: Bootstrapping language-image pre-training* — ICML, arXiv:2301.12597
- Maharana et al. (2024) — *Evaluating very long-term conversational memory of LLM agents (LoCoMo)* — arXiv:2402.17753
- Packer et al. (2023) — *MemGPT: Towards LLMs as operating systems* — arXiv:2310.08560
- Radford et al. (2021) — *Learning transferable visual models from natural language supervision (CLIP)* — ICML, arXiv:2103.00020

## Related Digests

- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects (Latimer et al., 2025) — direct architectural counterpoint. Both papers split memory into multiple typed components, but the cut is orthogonal: Hindsight cuts by *epistemic source* (World/Experience/Opinion/Observation), MemVerse cuts by *abstraction level* (core/episodic/semantic) plus by *access speed* (graph vs parametric). Read together to see the design space along two independent axes.
- [[chhikara-2025-mem0]] — Mem0: Building production-ready AI agents with scalable long-term memory (Chhikara et al., 2025) — the "production retrieval-only" baseline this paper positions against in §2.1. MemVerse cites Mem0 as a representative of "production-grade memory layers" providing summarization/compression for retrieval-augmented deployments.
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as operating systems (Packer et al., 2023) — the OS-analogy paged-memory baseline. MemVerse cites it as one of the canonical non-parametric memory frameworks alongside MemoryBank and MemoRAG.
- [[rasmussen-2025-zep-temporal-kg]] — Zep: A temporal knowledge graph architecture for agent memory (Rasmussen et al., 2025) — closest architectural cousin (both use a knowledge graph as the LTM substrate). Zep's distinction is its temporal-bitemporal modelling; MemVerse's is its multimodal scope and parametric cache pathway.
- [[tavakoli-2026-beam-light]] — Beyond a Million Tokens (Tavakoli et al., 2026) — also a hierarchical memory system (episodic + scratchpad + working memory + LLM filter) testing on LoCoMo. MemVerse and BEAM agree that cognitively-inspired tiering helps but partition differently — BEAM is text-only and emphasises noise filtering, MemVerse is multimodal and emphasises parametric distillation.

## Reviewer Notes

**Hallucination severity:** Clean

Spot-checks against the source PDF:

- **GPT-4o-mini + MemVerse 85.48% ScienceQA average vs 76.82% baseline (+8.66 pp)** — verified in Table 1 (p. 7) under "GPT-4o-mini (MemVerse)" row Average column. ✓
- **Qwen2.5-72B + MemVerse 80.25% vs 78.37% baseline (+1.88 pp)** — verified in Table 1 same column. ✓
- **MSR-VTT R@1 text-to-video 90.4% vs CLIP 29.7%; video-to-text 89.2% vs 21.4%** — verified in Table 2 (p. 8) bottom rows. ✓
- **Latency: RAG 20.17s / LTM-only 8.26s / parametric 2.28s; ~89% speedup vs RAG, 72% vs LTM-only** — verified in §4.2 paragraph after Table 1 ("the parametric memory further reduces the average retrieval time to 2.28 seconds, achieving an acceleration of approximately 89% compared to RAG and 72% compared to long-term retrieval"). ✓
- **Three subgraph types: core, episodic, semantic** — verified in §3.1 "Long-Term Memory" paragraph: "k ∈ {core, episodic, semantic}". ✓
- **M_STM sliding window of K recent queries** — verified in eqn 2 (§3.1, Short-Term Memory). ✓
- **G = Φ_LLM(C) = (V, R) construction equation** — verified in eqn 4 (§3.1). ✓
- **Provenance back-pointers ℓ_v, ℓ_r** — verified in eqns 5 and 6 (§3.1). ✓
- **L_update training loss formula** — verified in eqn 9 (§3.2, Supervised Fine-tuning). ✓
- **Dynamic memory expansion M^{t+1} = M^t + ∆Θ_t** — verified in eqn 10. ✓
- **Initialization M^0_parametric = Θ_pretrained** — verified in eqn 8 ("the parametric memory is initialized with the original pretrained parameters of the base language model"). The "What Experts Overlook" section emphasises the always-re-init-from-pretrained discipline; the paper's text is consistent with this interpretation (the dynamic expansion equation describes within-cycle accumulation; eqn 8 is the initialization for each training cycle).
- **Multimodal input handling: GPT-4o-mini for image captioning, Whisper for audio, VLM for video frame captions** — verified in §4.1 Implementation. ✓
- **Base model Qwen2.5-7B with SFT, single A100 80G GPU, AdamW lr=2e-6 cosine scheduler, seq_len=2048** — verified in §4.1 Implementation (paper says "linear learning rate scheduler" with 10% warmup; the digest paraphrases as "linear LR scheduler" — matches). ✓
- **Shanghai AI Lab affiliation** — verified in author block on page 1. ✓
- **GitHub at github.com/KnowledgeXLab/MemVerse** — verified in author block on page 1. ✓
- **arXiv ID 2512.03627v1, submitted 3 Dec 2025** — verified in the title page header. ✓
- **Memory effectiveness varies by host model (GPT-4o-mini benefits a lot, Qwen2.5 less so)** — verified in §4.2 paragraph beginning "Furthermore, we observe that the impact of memory enhancement differs between Qwen and GPT-4o-mini." ✓

One caveat acknowledged in the digest: the MSR-VTT 60.7 pp improvement is partly attributable to the MMKG construction step doing cross-modal alignment work via GPT-4o-mini — the paper acknowledges this in §4.2 ("pairs of captions... are partially aligned and connected through GPT-4o-mini's powerful understanding"). The digest flags this in the Implications section as the appropriate level of qualification. Not a hallucination; the paper itself is transparent about this construction-time advantage.

No fabricated claims found. Severity: **Clean**.
