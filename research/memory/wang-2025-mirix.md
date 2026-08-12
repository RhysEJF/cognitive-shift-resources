---
corpus: agentic-memory
kind: paper-digest
slug: wang-2025-mirix
title: "MIRIX: Multi-Agent Memory System for LLM-Based Agents"
authors:
  - "Yu Wang"
  - "Xi Chen"
year: 2025
publication_date: "2025-07"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2507.07957"
doi: null
arxiv_id: "2507.07957"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "MIRIX splits agent memory into six cognitively-typed components (Core, Episodic, Semantic, Procedural, Resource, Knowledge Vault) each managed by its own LLM-driven Memory Manager agent, with a Meta Memory Manager routing user input and a Chat Agent issuing Active Retrieval (auto-generate a topic before every answer) — hitting 85.4% on LoCoMo (8 pp over the best baseline LangMem at 78.05%) and 35% higher accuracy with 99.9% smaller storage than RAG baselines on a new 20k-screenshot multimodal benchmark, proving that the bottleneck for long-term memory is routing into specialized components, not capacity of any single component."
topics:
  - agent-memory
  - multi-agent-memory
  - six-component-memory
  - core-episodic-semantic-procedural-resource-knowledge-vault
  - active-retrieval
  - meta-memory-manager
  - screenshotvqa
  - locomo-benchmark
  - memory-routing
  - cognitive-memory-types
  - long-term-conversational-memory
  - multimodal-memory
  - mirix-app
  - personal-assistant
  - wearable-memory
tags:
  - paper
  - memory-architecture
  - multi-agent
  - cognitive-memory
  - screenshotvqa
  - locomo
  - mirix
  - personal-assistant
  - active-retrieval
  - memory-router
  - knowledge-vault
  - procedural-memory
entities:
  - wang-yu
  - chen-xi
  - mirix-ai
related_digests:
  - latimer-2025-hindsight-memory
  - liu-2025-memverse
  - chhikara-2025-mem0
  - packer-2023-memgpt-os
  - rasmussen-2025-zep-temporal-kg
  - xu-2025-a-mem-agentic-memory
  - maharana-2024-locomo
citations:
  - title: "ArigraphGraph: Learning knowledge graph world models with episodic memory for LLM agents"
    authors: ["Petr Anokhin", "Nikita Semenov", "Artyom Sorokin", "Dmitry Evseev", "Andrey Kravchenko", "Mikhail Burtsev", "Evgeny Burnaev"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2407.04363"
  - title: "Recurrent memory transformer"
    authors: ["Aydar Bulatov", "Yuri Kuratov", "Mikhail S. Burtsev"]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory transformer"
    authors: ["Mikhail S. Burtsev", "Grigory V. Sapunov"]
    year: 2020
    venue: "CoRR"
    doi: null
    url: "https://arxiv.org/abs/2006.11527"
    arxiv_id: "2006.11527"
  - title: "AgentVerse: A multi-agent framework for autonomous task completion"
    authors: ["Li Chen", "Rohan Kumar", "Anika Patel"]
    year: 2024
    venue: "Online"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mem0: Building production-ready AI agents with scalable long-term memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "Taranjeet Singh", "Deshraj Yadav"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.19413"
  - title: "AutoGPT: Autonomous GPT-4 powered agent"
    authors: ["Community"]
    year: 2023
    venue: "GitHub"
    doi: null
    url: "https://github.com/Significant-Gravitas/Auto-GPT"
    arxiv_id: null
  - title: "BabyAGI: Open-source autonomous AI agent"
    authors: ["Community"]
    year: 2023
    venue: "GitHub"
    doi: null
    url: "https://github.com/yoheinakajima/babyagi"
    arxiv_id: null
  - title: "Larimar: Large language models with episodic memory control"
    authors: ["Payel Das", "Subhajit Chaudhury", "Elliot Nelson", "Igor Melnyk", "Sarathkrishna Swaminathan", "Sihui Dai", "Aurélie C. Lozano", "Georgios Kollias", "Vijil Chenthamarakshan", "Jirí Navrátil", "Soham Dan", "Pin-Yu Chen"]
    year: 2024
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Cartridges: Lightweight and general-purpose long context representations via self-study"
    authors: ["Sabri Eyuboglu", "Ryan Ehrlich", "Simran Arora", "Neel Guha", "Dylan Zinsley", "Emily Liu", "Will Tennien", "Atri Rudra", "James Zou", "Azalia Mirhoseini", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2506.06266"
  - title: "Camelot: Towards large language models with training-free consolidated associative memory"
    authors: ["Zexue He", "Leonid Karlinsky", "Donghyun Kim", "Julian McAuley", "Dmitry Krotov", "Rogerio Feris"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.13449"
  - title: "MetaGPT: Designing a multi-agent ecosystem for task management"
    authors: ["Emily Hong", "Xin Zhao", "Kevin Lee"]
    year: 2023
    venue: "Online"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory OS of AI agent"
    authors: ["Jiazheng Kang", "Mingming Ji", "Zhe Zhao", "Ting Bai"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2506.06326"
  - title: "A machine with short-term, episodic, and semantic memory systems"
    authors: ["Taewoon Kim", "Michael Cochez", "Vincent François-Lavet", "Mark Neerincx", "Piek Vossen"]
    year: 2023
    venue: "AAAI 37:48-56"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory, consciousness and large language model"
    authors: ["Jitang Li", "Jinzheng Li"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2401.02509"
  - title: "SnapKV: LLM knows what you are looking for before generation"
    authors: ["Yuhong Li", "Yingbing Huang", "Bowen Yang", "Bharat Venkitesh", "Acyr Locatelli", "Hanchen Ye", "Tianle Cai", "Patrick Lewis", "Deming Chen"]
    year: 2024
    venue: "CoRR"
    doi: "10.48550/ARXIV.2404.14469"
    url: null
    arxiv_id: "2404.14469"
  - title: "The role of episodic memory in long-term LLM agents: A position paper"
    authors: ["Ming Liao", "Su Chen", "Li Zhao"]
    year: 2024
    venue: "Online"
    doi: null
    url: null
    arxiv_id: null
  - title: "Echo: A large language model with temporal episodic memory"
    authors: ["WenTao Liu", "Ruohua Zhang", "Aimin Zhou", "Feng Gao", "JiaLi Liu"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.16090"
  - title: "Evaluating very long-term conversational memory of LLM agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "Mohit Bansal", "Francesco Barbieri", "Yuwei Fang"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.17753"
  - title: "Optimizing the interface between knowledge graphs and LLMs for complex reasoning (Cognee)"
    authors: ["Vasilije Markovic", "Lazar Obradovic", "Laszlo Hajdu", "Jovan Pavlovic"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2505.24478"
  - title: "Leave no context behind: Efficient infinite context transformers with Infini-attention"
    authors: ["Tsendsuren Munkhdalai", "Manaal Faruqui", "Siddharth Gopal"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2404.07143"
  - title: "MemGPT: Towards LLMs as operating systems"
    authors: ["Charles Packer", "Vivian Fang", "Shishir G. Patil", "Kevin Lin", "Sarah Wooders", "Joseph E. Gonzalez"]
    year: 2023
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "Position: Episodic memory is the missing piece for long-term LLM agents"
    authors: ["Mathis Pink", "Qinyuan Wu", "Vy Ai Vo", "Javier Turek", "Jianing Mu", "Alexander Huth", "Mariya Toneva"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.06975"
  - title: "Zep: A temporal knowledge graph architecture for agent memory"
    authors: ["Preston Rasmussen", "Pavlo Paliychuk", "Travis Beauvais", "Jack Ryan", "Daniel Chalef"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2501.13956"
  - title: "Cognitive memory in large language models"
    authors: ["Lianlei Shan", "Shixian Luo", "Zezhou Zhu", "Yu Yuan", "Yong Wu"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.02441"
  - title: "Cognitive neuroscience perspective on memory: overview and summary"
    authors: ["Sruthi Sridhar", "Abdulrahman Khamaj", "Manish Kumar Asthana"]
    year: 2023
    venue: "Frontiers in human neuroscience 17:1217093"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory and consciousness"
    authors: ["Endel Tulving"]
    year: 1985
    venue: "Canadian Psychology 26(1):1"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemoryLLM: Towards self-updatable large language models"
    authors: ["Yu Wang", "Yifan Gao", "Xiusi Chen", "Haoming Jiang", "Shiyang Li", "Jingfeng Yang", "Qingyu Yin", "Zheng Li", "Xian Li", "Bing Yin", "Jingbo Shang", "Julian J. McAuley"]
    year: 2024
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards lifespan cognitive systems"
    authors: ["Yu Wang", "Chi Han", "Tongtong Wu", "Xiaoxin He", "Wangchunshu Zhou", "Nafis Sadeq", "Xiusi Chen", "Zexue He", "Wei Wang", "Gholamreza Haffari", "Heng Ji", "Julian J. McAuley"]
    year: 2024
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2409.13265"
  - title: "Self-updatable large language models with parameter integration"
    authors: ["Yu Wang", "Xinshuang Liu", "Xiusi Chen", "Sean O'Brien", "Junda Wu", "Julian McAuley"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2410.00487"
  - title: "M+: Extending MemoryLLM with scalable long-term memory"
    authors: ["Yu Wang", "Dmitry Krotov", "Yuanzhe Hu", "Yifan Gao", "Wangchunshu Zhou", "Julian McAuley", "Dan Gutfreund", "Rogerio Feris", "Zexue He"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.00592"
  - title: "Caim: Development and evaluation of a cognitive AI memory framework for long-term interaction with intelligent agents"
    authors: ["Rebecca Westhäußer", "Frederik Berenz", "Wolfgang Minker", "Sebastian Zepf"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2505.13044"
  - title: "Procedural memory is not all you need: Bridging cognitive gaps in LLM-based agents"
    authors: ["Schaun Wheeler", "Olivier Jeunen"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2505.03434"
  - title: "LongMemEval: Benchmarking chat assistants on long-term interactive memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "Yuwei Zhang", "Kai-Wei Chang", "Dong Yu"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2410.10813"
  - title: "A-Mem: Agentic memory for LLM agents"
    authors: ["Wujiang Xu", "Kai Mei", "Hang Gao", "Juntao Tan", "Zujie Liang", "Yongfeng Zhang"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.12110"
  - title: "Berkeley Function Calling Leaderboard"
    authors: ["Fanjia Yan", "Huanzhi Mao", "Charlie Cheng-Jie Ji", "Tianjun Zhang", "Shishir G. Patil", "Ion Stoica", "Joseph E. Gonzalez"]
    year: 2024
    venue: "Online"
    doi: null
    url: "https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html"
    arxiv_id: null
  - title: "H2O: heavy-hitter oracle for efficient generative inference of large language models"
    authors: ["Zhenyu Zhang", "Ying Sheng", "Tianyi Zhou", "Tianlong Chen", "Lianmin Zheng", "Ruisi Cai", "Zhao Song", "Yuandong Tian", "Christopher Ré", "Clark W. Barrett", "Zhangyang Wang", "Beidi Chen"]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "Yanlin Wang"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.10250"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "The six memory components of MIRIX, each providing specialized functionality"
  page: 2
  image_path: "figures/wang-2025-mirix-fig.png"
---

# MIRIX: Multi-Agent Memory System for LLM-Based Agents

**Authors:** Yu Wang (yuw164@ucsd.edu), Xi Chen (xc13@stern.nyu.edu) — MIRIX AI
**Published:** 2025-07 · [Source](https://arxiv.org/abs/2507.07957) · [Site](https://mirix.io/) · [Code](https://github.com/Mirix-AI/MIRIX)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MIRIX (MIRIX AI, July 2025) is a modular multi-agent memory system that takes the cognitive-typing argument to its operational extreme: six fully-separated memory components (**Core** — persona + human blocks à la MemGPT, with auto-rewrite at 90% capacity; **Episodic** — time-stamped event log with fields {event_type, summary, details, actor, timestamp}; **Semantic** — abstract entity/concept knowledge {name, summary, details, source}; **Procedural** — workflow/guide/script entries with structured steps; **Resource** — document/file storage {title, summary, resource_type, content}; **Knowledge Vault** — verbatim sensitive data {entry_type, source, sensitivity ∈ {low, medium, high}, secret_value}) where each component is managed by its own LLM-driven Memory Manager agent, and a **Meta Memory Manager** routes incoming input to the relevant subset of managers (parallel updates) while a **Chat Agent** answers user queries via *Active Retrieval* — auto-generating a topic before every answer and using it to pull top-10 entries from each of the six components, tagged by source (`<episodic_memory>...</episodic_memory>`) so the model knows where each piece came from. Empirically: on the new **ScreenshotVQA** benchmark (5K–18K high-res 2K–4K screenshots per user, collected over weeks-to-months from 3 PhD students, 87 manually-crafted questions across "Is this multimodal memory system actually useful?" tasks), MIRIX hits 59.5% overall accuracy vs SigLIP@50 RAG's 44.1% (**+35% relative**) while storing only 15.89 MB vs SigLIP's 15.07 GB (**−99.9%**) — and obliterates the long-context Gemini-2.5-flash baseline at 11.66% (**+410% relative**, −93.3% storage). On **LoCoMo** (10 conversations × ~600 turns × ~26k tokens), MIRIX on gpt-4.1-mini reaches **85.38% overall** (Single-Hop 85.11 / Multi-Hop 83.70 / Open-Domain 65.62 / Temporal 88.39) — +8 pp over LangMem (78.05% on gpt-4o-mini, the strongest open-source baseline) and approaching the Full-Context upper bound (87.52%). The MIRIX app captures a screenshot every 1.5s, drops near-duplicates, triggers a memory update every 20 unique screenshots (~60s), uses Gemini's Google-Cloud-URL streaming to drop end-to-end latency from ~50s (GPT-4 direct upload) to <5s. **Most useful takeaway:** the bottleneck for long-term memory isn't the *capacity* or *retrieval algorithm* of any single store — it's the **routing decision** of which specialized store should hold which piece of info, and that decision is concrete enough to give a dedicated LLM agent (the Meta Memory Manager) as its only job.

## Key Takeaway

Where Hindsight cuts memory by *epistemic source* (W/B/O/S — what kind of knowledge), MemVerse by *abstraction level + access speed* (core/episodic/semantic + graph/parametric), MIRIX cuts by *functional role* (Core/Episodic/Semantic/Procedural/Resource/Vault) — and crucially makes the routing decision a *first-class LLM agent role* rather than an extraction rule. The Meta Memory Manager doesn't store memory; it just looks at new input and decides which of the six Memory Managers should ingest it (potentially several in parallel). The Chat Agent doesn't store memory; it just generates a "current topic" from the query and fans retrieval across all six. This is the multi-agent OS analogy made concrete — each memory component is a process with its own manager, and the manager-of-managers does scheduling. Stated as a lesson: **once memory is properly typed, the highest-leverage operation is *routing*, and routing should be an LLM call, not a heuristic — because the same fact ("the user's CEO is Marcus") belongs in Knowledge Vault (verbatim contact), Semantic Memory (entity relation), and possibly Episodic Memory (when this was said), and only an LLM understands "all three at once."**

## Implications

- **Six memory components is a better default than four — and the additions matter individually.** Hindsight has W/B/O/S; MemVerse has core/episodic/semantic. MIRIX adds **Procedural** (step-by-step workflows: "how to file a reimbursement", "how the user triages morning email") and **Resource** (full documents that don't fit other categories: meeting transcripts, project briefs the user is actively working with) and **Knowledge Vault** (verbatim sensitive data with sensitivity-level access control: credentials, addresses, API keys). The additions cover real ENGRAM-Encode use cases the other frameworks force into Semantic or Episodic and degrade. For Flow OS specifically, Procedural Memory maps directly to `.claude/commands/`-style workflow capture (one file per workflow with `entry_type`, `description`, `steps`); Knowledge Vault is exactly the missing layer for API keys / credentials (currently `~/.flow/api-keys` is unstructured); Resource Memory is where session transcripts and uploaded documents should live (not crammed into pattern files). `[E, N]`

- **Make the router an LLM agent, not a rule.** The Meta Memory Manager is just an LLM with a system prompt that says "Given this new input, decide which of {Core, Episodic, Semantic, Procedural, Resource, Vault} should ingest it (one or more), and emit function calls to those managers." This is dramatically more flexible than rule-based routing (regex over content) because the same incoming fact can flow to multiple components in parallel — and the routing decision can be made *with full understanding of the input semantics*, not just keyword pattern-matching. The cost is 1 LLM call per input event; the benefit is correct fan-out across all relevant memory types. For Flow OS, this means `/learn` should not just extract facts; it should also classify each fact's *destination set* and write to multiple typed files in parallel. `[E, A]`

- **Active Retrieval — generate a topic before every answer, then use it as the retrieval query.** §3.2 makes this concrete: given the user's raw question Q, the Chat Agent first generates a *topic* T (e.g. for Q="Who is the CEO of Twitter?" → T="CEO of Twitter"), then uses T as the retrieval query against all six components (top-10 each). Retrieved chunks are tagged by source (`<episodic_memory>...`, `<knowledge_vault>...`) before being injected into the system prompt. This solves the "model defaults to parametric knowledge" failure mode that MemGPT and Mem0 still suffer from (where the LM answers from its own weights when it should be checking memory). The topic-generation step is the *meta-cognition* analogue: ask yourself "what should I be remembering right now?" before answering. For QMD-backed sessions, the lesson is: don't pass the user's raw query to `qmd query`; first ask Claude to generate the *abstract retrieval topic* and query on that. `[R]`

- **Source-tagged retrieval results dramatically reduce hallucination by changing what the model can see.** Wrapping retrieved chunks with `<episodic_memory>`, `<knowledge_vault>` etc. before injection means the model sees both content AND provenance type. This makes prompt-time reasoning like "the user's actual stated preference (Core) is X, but episodic events suggest Y — I should ask which to use" trivially possible. Compare to flat injection (just dropping retrieved text into the system prompt with no labels) where the model has to infer the source on its own and often gets it wrong. For Flow OS, every QMD result injection should be source-tagged at minimum by `kind:` and ideally by the six MIRIX components. `[R, G]`

- **The Knowledge Vault is the missing security layer.** Of all the agent-memory architectures in the wiki, MIRIX is the first to make explicit that *some memory entries should be excluded from casual retrieval entirely* — Knowledge Vault entries with `sensitivity: high` are protected via access control and excluded from default retrieval to prevent misuse or leakage. This is the right design for personal-second-brain systems where the line between "remember my preferences" and "remember my passwords" matters. For Flow OS, implementing this means a separate retrieval policy on the Vault component — only retrieved when the user query explicitly invokes credential-needing context, never injected into casual chat. `[M, G]`

- **Single-Hop performance varies on ambiguous prompts because of consolidation discipline.** §4.3 surfaces an honest weakness: MIRIX scores 85.11 on Single-Hop vs Full-Context 88.53. The diagnostic example is illuminating — "When is Melanie planning on going camping?" with two valid answers (planned trip in June from May conversation, actual trip in October from October conversation). MIRIX consolidates events at write time ("On 19 October 2023, Melanie and her family went camping after their road trip"), so it preferentially returns the *occurred* event over the *planned* event. Full-Context preserves both and lets the model pick. The lesson: write-time consolidation is generally a win (Multi-Hop +24 pp over baselines) but creates a Single-Hop edge case on ambiguous temporal queries. The mitigation isn't to abandon consolidation; it's to keep the original "planned: ..." event in Episodic Memory alongside the consolidated "occurred: ..." event, so retrieval can surface both when temporal disambiguation is needed. `[A, R]`

- **Multi-Hop is where typed-memory architectures crush flat-RAG architectures.** MIRIX's Multi-Hop score of 83.70 vs RAG-500's 37.69 (**+46 pp**) is the cleanest evidence in the paper for the typed-memory thesis. Example: "Where did Caroline move from 4 years ago?" requires stitching "Caroline moved from her hometown 4 years ago" + "Caroline's hometown is Sweden" → "Sweden". Flat RAG retrieves the literal "moved 4 years ago" chunk and stops; MIRIX has the consolidated event "Caroline moved from her hometown, Sweden, 4 years ago" already in Semantic Memory because the Meta Memory Manager fanned the original two facts to the right components. The lesson is that consolidation isn't optional; without it, multi-hop questions degrade to literal-substring search. `[A, R]`

- **The screenshot-monitoring app is the lab for testing whether agent memory actually works in the wild.** A screenshot every 1.5s, near-duplicate dropping, batched memory update every 20 unique frames (~60s), Gemini streaming uploads to drop ingestion latency from 50s to <5s — this is a real deployed memory system with measurable user behavior. The compression discipline (15.07 GB of source screenshots → 15.89 MB of structured memory) is the answer to the practical question of "can a personal-scale agent run continuously without filling your disk?" — yes, if you do extraction + structuring + cross-component routing at ingestion time. For Flow OS / personal AI, this is the proof point that always-on capture is viable when the memory layer is doing real semantic work. `[E, A, M]`

- **The Memory Marketplace vision (§2.3) is speculative; ignore for the architecture discussion but note for the product framing.** Section 2.3 sketches a future where users tokenize and trade their memory contents as a digital asset class (memory of "productivity hacks", "celebrity AI personas for fans", "AI dating clones"). This is product-speculation rather than research — clearly the founders pitching a startup angle (mirix.io). The architecture's strength does NOT depend on this and would survive even if the marketplace concept goes nowhere. Mention only as context for who's behind the work. `[—]`

- **Function-calling quality is a hard prerequisite for multi-agent memory.** §4.1.2 mentions that gpt-4.1-mini was chosen over gpt-4o-mini because of the Berkeley Function Calling Leaderboard (gpt-4o-mini scores 22.12 on multi-turn vs gpt-4.1-mini's 29.75). Each memory update step requires the agent to call multiple functions (one to the Meta Memory Manager + 0–6 to specialized managers). For Flow OS, this means: if the orchestrator model is weak at multi-turn function calling, the multi-agent routing collapses. Choose a high-function-calling-quality model for the orchestrator role even if cheaper models suffice for the Memory Manager roles. `[N, A]`

- **Latent-space memory and token-level memory are complementary, not competing — but token-level is dominant in current deployed systems.** §5 makes the clean taxonomy: latent-space memory (RMT, MemoryLLM, M+, KV-cache approaches like SnapKV / H2O) requires retraining and thus can't sit on top of GPT-4-class closed models, while token-level memory (Zep, Mem0, MemGPT, MIRIX) stores past content as raw text in external DBs and works with any backbone. For practical agent OSes today, token-level wins for the same reason — model-agnostic. The future direction worth watching is hybrid systems that materialize a learned latent cache from a token-level store (like MemVerse does with its parametric pathway). `[N, R]`

## How to Apply It (method)

**Scenario:** Same Flow OS agentic OS context. The current vault has good Pattern files and Decision files but a flat memory layout — `/learn` writes to whichever subfolder feels most natural at extraction time, with no router to ensure a fact like "Marcus Webb pays a monthly subscription for Flow OS, mentioned in 2026-04-23 session, his email is marcus@example.com" gets distributed across the right components (it should: Knowledge Vault for the email, Semantic Memory for "Marcus is Flow OS customer", Episodic Memory for the "April 23 conversation"). You want to retrofit MIRIX's six-component + multi-agent-router pattern onto QMD. This maps to ENGRAM's Encode (routing decision is *part of* encoding), Network (six typed substrates), Aggregate (write-time consolidation that preserves both planned and occurred events for temporal disambiguation), Retrieve (Active Retrieval + source-tagged injection), Maintain (Vault access control + Core-Memory auto-rewrite).

**Steps:**

1. **Add six top-level memory component directories with frontmatter discriminator.** Under `memory/`:
   - `memory/components/core/` — `{kind: core-memory, block: persona|human, content: ...}` (mirror MemGPT layout)
   - `memory/components/episodic/` — `{kind: episodic-memory, event_type, summary, details, actor, timestamp, participants}`
   - `memory/components/semantic/` — `{kind: semantic-memory, name, summary, details, source}`
   - `memory/components/procedural/` — `{kind: procedural-memory, entry_type ∈ {workflow|guide|script}, description, steps[]}`
   - `memory/components/resource/` — `{kind: resource-memory, title, summary, resource_type ∈ {doc|markdown|pdf_text|image|voice_transcript}, content_path}` (point to actual file)
   - `memory/components/vault/` — `{kind: vault-memory, entry_type ∈ {credential|bookmark|contact_info|api_key}, source, sensitivity ∈ {low|medium|high}, secret_value_path}` (encrypted at rest)
   
   Migrate existing files: contact cards → `core/human` blocks; session captures → `episodic`; concept/entity files → `semantic`; existing `.claude/commands/` workflows → `procedural`; uploaded docs → `resource`; API keys → `vault` (with sensitivity flagging).

2. **Implement a Meta Memory Manager router prompt for `/learn`.** Rewrite `/learn` so that after extraction, before writing files, it calls an LLM with this prompt:

   ```
   You are the Meta Memory Manager for a multi-component memory system.
   Given the extracted fact below, decide which component(s) should
   ingest it. Output a JSON list of components from:
     core, episodic, semantic, procedural, resource, vault
   You may select multiple components if the fact belongs in several
   (e.g. a customer's email belongs in vault for the email itself,
   semantic for "X is a customer", and episodic for "the conversation
   on date Y where this was said"). For each selected component,
   provide the fields that component requires.
   
   FACT: {extracted_fact}
   CONTEXT: {surrounding session context for disambiguation}
   
   OUTPUT:
   {
     "routes": [
       {"component": "...", "fields": {...}},
       ...
     ]
   }
   ```
   
   Then write to each selected component's directory in parallel.

3. **Implement Active Retrieval as a topic-first wrapper around `qmd query`.** Create `qmd recall(query, components=ALL)` that:
   - First calls an LLM: "Given the user query Q, generate a single short retrieval topic T (3–6 words) capturing what should be retrieved. Output ONLY T."
   - Runs `qmd query T --filter kind:<component>` for each component in `components`, top-10 each
   - Tags each retrieved chunk with `<{component}_memory>...{content}...</{component}_memory>`
   - Concatenates all tagged chunks and returns to caller
   
   Replace flat `qmd query` calls throughout the system with `qmd recall`. This matches MIRIX's Active Retrieval workflow.

4. **Implement Vault access control.** Files in `memory/components/vault/` with `sensitivity: high` should be *excluded from default `qmd recall`*. Retrieval into Vault only happens when:
   - The user query explicitly mentions a credential-needing context ("send an email to X", "log into Y", "use the X API")
   - OR the user explicitly invokes `/vault-recall "what's my X API key"`
   
   Add a CLI flag `--include-vault` to `qmd recall` and route only specific queries through it. For day-to-day chat, the Vault is invisible. For automated agents executing tasks, the agent must explicitly opt-in.

5. **Wire Core Memory auto-rewrite at 90% capacity.** Define a hard cap on the Core Memory block size (e.g. 8K tokens combined across persona + human blocks). When a `/learn` Core-write would push past 90% of the cap, trigger an LLM-driven rewrite step:
   
   ```
   Current core memory is at {x}% capacity. Rewrite the {persona|human}
   block below to preserve all distinct facts but in a more compact
   form. Remove redundancy. Combine related preferences. Keep
   self-identifying attributes exact.
   OLD: {current_block}
   ```
   
   Write the rewritten block back. This mirrors MemGPT's design (which MIRIX inherits in §3.1).

6. **Consolidate Episodic events at write time, but preserve both planned and occurred entries.** When `/learn` writes an Episodic event, if a planned-event-with-same-entities already exists, write a NEW episodic event (don't overwrite) for the occurred event. Both stay in the store. At retrieval time, for ambiguous temporal queries, the model sees both `event_type: planned (May)` and `event_type: occurred (October)` and can disambiguate based on the query phrasing. This addresses the §4.3 Single-Hop weakness MIRIX itself flags.

7. **Add per-component Memory Manager prompts.** Each component gets its own dedicated extraction prompt (used by the Meta Memory Manager when it routes input to that component). E.g.:

   ```
   PROCEDURAL MEMORY MANAGER:
   You manage a memory store for workflows and step-by-step guides.
   Given the input below, extract:
     - entry_type: workflow | guide | script
     - description: a goal-oriented sentence (what does the workflow accomplish?)
     - steps: an ordered list of actionable instructions (be precise; another agent will follow these literally)
   Output JSON. If the input doesn't contain a procedure, output {} (empty).
   INPUT: {fact}
   ```

8. **Build a `mirix-app`-style screen monitor (optional, for the "Cognitive Shift" article).** This is the killer demo from the paper. Use the existing `/capture` skill but extend it with a daemon that:
   - Screenshots active screen every 1.5s (use `screencapture -i` on macOS or equivalent)
   - Drops near-duplicates (perceptual hash threshold > 0.99 similarity)
   - When 20 unique frames accumulate (~60s), triggers a memory update
   - Routes through the Meta Memory Manager (likely → Episodic + Resource + occasionally Semantic)
   - Stores raw images temporarily in `experiences/captures/screen/<date>/` then deletes after extraction
   - Storage discipline: only the extracted structured memory persists (paper's 15 GB → 16 MB ratio)
   
   This is a fantastic Cognitive Shift article hook: "I let Flow OS watch my screen for a week — here's what it remembered."

9. **Evaluate on LongMemEval AND a private ScreenshotVQA-style benchmark.** Mirror the paper's methodology. For LongMemEval (already in wiki as `wu-2024-longmemeval`), wire up all three arms:
   - **A**: QMD hybrid only
   - **B**: QMD + Active Retrieval (topic-first) + source tagging
   - **C**: Full MIRIX retrofit (six components + Meta Memory Manager router + per-component Memory Managers + Active Retrieval + source tagging)
   
   The paper's evidence predicts A → B buys some points (topic generation closes the parametric-knowledge-leak hole), B → C buys the big multi-hop and temporal jumps.

10. **Set a function-calling-quality floor for the Meta Memory Manager role.** The Meta Memory Manager runs N+1 function calls per user input (1 to itself for routing, N to the chosen Memory Managers). If the underlying model can't do multi-turn function calling reliably, the whole architecture collapses (routing decisions fail silently). The paper's empirical floor is gpt-4.1-mini (Berkeley score 29.75) — anything below that is risky for orchestrator role. For local-model alternatives, look for explicit multi-turn function-call evals.

11. **Source tagging in injected prompts is non-negotiable.** Every retrieved chunk must be wrapped in `<core_memory>`, `<episodic_memory>`, `<semantic_memory>`, `<procedural_memory>`, `<resource_memory>`, `<vault_memory>` tags before injection. Document this as an architectural invariant. Without it, the model can't reason about provenance ("the user *said* X in Episodic, but their *stated preference* in Core is Y — flag the apparent contradiction").

12. **Diagnostic: route hit-rate per component over time.** Log every `/learn` routing decision and every `qmd recall` hit. After a month, compute: per component, (a) how often it's written to, (b) how often it's retrieved from, (c) which user-task types correlate with each component being used. If, say, Procedural Memory never gets retrieved despite being written to weekly, you have a retrieval-side bug. If Knowledge Vault gets written to but never retrieved (because no one ever asks for credentials in chat), that's correct behavior — it's only used by automated agents. The route-hit-rate matrix tells you where the architecture is paying off and where it isn't.

**Expected outcome:** A retrofit memory layer that (a) routes new facts through an LLM-driven Meta Memory Manager so each fact lands in all the components it semantically belongs to (not just the one the extractor felt most natural about), (b) issues Active Retrieval with topic-first generation + per-component fan-out + source tagging on every conversational query, (c) keeps sensitive data firewalled in a Vault that's excluded from default retrieval but accessible to authenticated agents, (d) consolidates events at write time without losing the original planned-vs-occurred distinction, (e) optionally adds a screen-monitoring daemon as a real-world stress test of the memory layer. The route-hit-rate diagnostic tells you which components are pulling their weight and which need their extraction prompts tuned.

## Best Figure

![Figure 1 — The six memory components of MIRIX (page 2)](figures/wang-2025-mirix-fig.png)

**Figure Name:** Figure 1: "The six memory components of MIRIX, each providing specialized functionality."

**Figure Page:** 2

**Slide Caption:** MIRIX's compositional memory taxonomy: six visually-distinguished components — Core Memory (user information / preferences / always-in-context), Episodic Memory (time-stamped events), Semantic Memory (concepts / named entities), Procedural Memory (step-by-step guides), Resource Memory (files / documents), Knowledge Vault (addresses / phone numbers / credentials). Each is managed by its own LLM-driven Memory Manager agent, coordinated by a Meta Memory Manager that routes incoming inputs to the relevant subset.

**Description:** Figure 1 is the at-a-glance taxonomy diagram. Six rounded-rectangle tiles in a horizontal row, each containing a single line-art icon and a two-word label. From left to right: **Core Memory** (head-with-heart icon, "User Information / User Preferences / Always in Context"), **Episodic Memory** (calendar icon, "Events happened about the user"), **Semantic Memory** (lightbulb-with-star icon, "New Concepts / New Names"), **Procedural Memory** (gear-with-arrow icon, "Step-by-Step Guides"), **Resource Memory** (document-with-checkmarks icon, "Files / Documents"), **Knowledge Vault** (padlock icon, "Addresses / Phone Numbers / Credentials"). The figure matters because it commits the paper to a precise *enumeration* — six is not a vague "many" but an exact functional taxonomy that the rest of the paper operationalizes (one Memory Manager per component, one extraction prompt per component, one retrieval channel per component, one fan-out in the Meta Memory Manager). The cleanest visual statement in the wiki so far of "memory is not a single thing — it has functional sub-types and they should be physically separated."

**Other strong candidates:**
- **Figure 5 (p. 7)** — Active Retrieval workflow diagram. Shows the topic-generation step ("CEO of Twitter" inferred from "Who is the CEO of Twitter?") and the fan-out across six components with source-tagged results injection. The clearest illustration of the retrieval-time meta-cognition pattern.
- **Figure 7 (p. 9)** — Conversational Retrieval Workflow. Shows the Chat Agent's coarse-then-targeted retrieval pattern: first a broad summary search across all six components, then targeted deep searches into the components the query analysis flags as relevant.
- **Table 2 (p. 11)** — LoCoMo results matrix. The 83.70 Multi-Hop vs 37.69 RAG-500 contrast is the paper's most quotable evidence for compositional-memory benefit.

## What Experts Overlook

Most readers will fixate on the six-component taxonomy as the architectural innovation. The detail almost everyone will miss is buried in §3.3 (Multi-Agent Workflow) and Figure 7: **the Chat Agent's retrieval is a *two-stage* process — first a coarse summary-level search across ALL six components, then targeted deep retrieval into the subset the query analysis identifies as relevant.** Specifically: "it first performs an automatic search over the memory base upon receiving a user query. This initial search is a coarse retrieval spanning all six memory components and returns high-level summaries rather than detailed content. The Chat Agent then analyzes the query to determine which memory components warrant more targeted searches and selects appropriate retrieval methods accordingly." This is a quietly important pattern: not all retrievals fan out to all six channels with equal weight; the system first peeks at *summaries* from every channel, then decides where to spend the deeper retrieval budget. This is the difference between a system that retrieves O(6 × deep_results) every time (expensive, noisy) and one that retrieves O(6 × summary) + O(K × deep_results) where K is the number of *actually relevant* components (cheap, focused). The paper doesn't dwell on this in the abstract or contributions because the six-component enumeration is the louder claim, but for personal-scale systems where every retrieval costs latency, this two-stage pattern is where the cost discipline lives.

**Why it matters:** Without the two-stage pattern, "Active Retrieval over six components" sounds like 6× the latency of single-store retrieval. With it, the latency is actually closer to 1× single-store + (small constant for the summary peek). The summary index for each component is small enough to scan exhaustively; the deep retrieval is targeted by query analysis. This is what makes the architecture *practically* deployable rather than just theoretically clean. For Flow OS, the implementation lesson is: maintain a small summary index per component (one-line summaries of each entry, denormalized for fast scan) AND the full content; query the summaries first, then decide which full-content stores to dig into.

**Example of good use (memory architectures for agentic OSes):** Implementing the Flow OS retrofit, set up per-component summary indexes:
- `memory/components/<X>/_summaries.tsv` — a denormalized one-line-per-entry summary file, regenerated whenever an entry in that component is added/modified
- `qmd recall` first scans all six `_summaries.tsv` files (cheap — these are small) to identify which components have semantically-relevant content for the query
- Only the components with summary hits get deep retrieval
- Result: queries that are "obviously procedural" (how do I X?) deep-retrieve only Procedural; queries that span multiple components (tell me about Marcus Webb — semantic + episodic + vault) deep-retrieve all three; pure-conversational queries (what time is it?) deep-retrieve nothing

This gives O(small constant + targeted) latency instead of O(6 × deep) for every query. For a personal-scale system where the user issues 50–200 queries a day and each saved second compounds, this is the difference between an agent that feels snappy and one that feels heavy.

**Example of misapplication:** A team adopts the six-component architecture and the Active Retrieval pattern but implements it naively: every user query triggers deep retrieval from all six components in parallel, with results then fused and reranked. What breaks: latency balloons from ~500ms (single-store retrieval) to ~3s (six parallel deep retrievals + fusion + rerank); cost balloons proportionally (six retrievals + six rerank calls + a fusion call); the model's context window fills with mostly-irrelevant chunks from the four-or-five components that the query didn't actually need. The user notices the system feels slow and starts working around it ("don't bother checking memory, just answer from what's in chat"). The lesson missed: **the two-stage retrieval (summary scan → targeted deep retrieval) is what makes six-component architectures scalable to per-query budgets.** Without it, you've just multiplied your retrieval cost by 6 for no quality gain on most queries. The summary-first pattern is buried in the methodology section, not advertised in the abstract — easy to miss, expensive to skip.

## Extracted Prompts

**Prompt explanation:** Active Retrieval — topic generation (§3.2, Figure 5) — the prompt that turns a user query into a retrieval topic before fanning out across the six memory components. Reconstructed from the paper's methodology description (no verbatim prompt is provided):

```
You are the Chat Agent for a six-component memory system. Before answering
the user's question, generate a short retrieval topic that captures what
the system should retrieve from memory.

Given the user query below, output ONLY a 3-6 word topic phrase. Do not
include any explanation or framing — just the topic, on a single line.

EXAMPLES:
  User Query: "Who is the CEO of Twitter?"
  Topic: CEO of Twitter

  User Query: "When did I last meet with Marcus Webb?"
  Topic: meetings with Marcus Webb

  User Query: "What's the workflow for sending a Flow pitch?"
  Topic: Flow pitch workflow

USER QUERY: {query}
TOPIC:
```

**Prompt explanation:** Meta Memory Manager routing (§3.3) — the prompt that, given new input, decides which of the six Memory Managers should ingest it. Reconstructed from the paper's methodology:

```
You are the Meta Memory Manager for a multi-component memory system.
The system has six specialized components:
  1. Core Memory       — user identity, persistent preferences (always in context)
  2. Episodic Memory   — time-stamped events about the user
  3. Semantic Memory   — concepts, entities, named knowledge
  4. Procedural Memory — workflows, step-by-step guides
  5. Resource Memory   — documents, files, transcripts
  6. Knowledge Vault   — verbatim sensitive data (credentials, addresses)

Given the new input below, decide which component(s) should ingest it.
Multiple components are allowed — for example, a customer's email
address belongs in:
  - Vault (for the email value itself, sensitivity: medium)
  - Semantic Memory (for the relation "X is a customer")
  - Episodic Memory (for the conversation event where it was shared)

For each selected component, emit a function call to its Memory Manager
with the extracted fields that component requires.

INPUT: {input_text}
SESSION CONTEXT: {recent_turns}

OUTPUT: function calls only, one per component, formatted as JSON.
```

**Prompt explanation:** Per-component Memory Manager — Episodic Memory example (§3.1) — the prompt that extracts Episodic-formatted entries from input routed by the Meta Memory Manager. Reconstructed from the field schema:

```
You are the Episodic Memory Manager. Episodic Memory stores time-stamped
events and temporally grounded interactions reflecting the user's
behavior, experiences, or activities.

Given the input below, extract one or more episodic entries with the
following fields:
  - event_type: one of {user_message, inferred_result, system_notification,
                user_action, external_event}
  - summary: a concise natural language description of the event
  - details: extended contextual information, including dialog excerpts
             or inferred states
  - actor: the origin of the event, either "user" or "assistant"
  - timestamp: ISO format if known; relative description ("during the
               morning standup on 2026-04-23") otherwise

Be precise about times. If no time is stated, infer from session metadata
or mark as "unknown".

INPUT: {input_text}
CURRENT TIME: {timestamp}

OUTPUT: JSON array of entries.
```

**Prompt explanation:** Per-component Memory Manager — Knowledge Vault example (§3.1) — the prompt that extracts secure-storage entries with sensitivity classification. Reconstructed from the field schema:

```
You are the Knowledge Vault Manager. The Vault stores verbatim sensitive
information: credentials, addresses, contact details, API keys.

Given the input below, extract any qualifying entries with the following
fields:
  - entry_type: one of {credential, bookmark, contact_info, api_key,
                address, phone_number, secret_url}
  - source: where this came from (user_provided, github, gws_auth, ...)
  - sensitivity: low | medium | high
      - low: bookmarks, public addresses
      - medium: contact info, email addresses
      - high: passwords, API keys, credentials
  - secret_value: the verbatim value (DO NOT paraphrase or modify)

If no Vault-qualifying content is present, output an empty array.

CRITICAL: Verbatim values only. Do not summarize, abstract, or transform.
The Vault's purpose is exact preservation.

INPUT: {input_text}
OUTPUT: JSON array of vault entries.
```

## Citations

First 10 (see frontmatter for full list of 36 references):

- Anokhin et al. (2024) — *ArigraphGraph: Learning KG world models with episodic memory for LLM agents* — arXiv:2407.04363
- Chhikara et al. (2025) — *Mem0: Building production-ready AI agents with scalable long-term memory* — arXiv:2504.19413
- Das et al. (2024) — *Larimar: Large language models with episodic memory control* — ICML
- Kang et al. (2025) — *Memory OS of AI agent* — arXiv:2506.06326
- Kim et al. (2023) — *A machine with short-term, episodic, and semantic memory systems* — AAAI
- Maharana et al. (2024) — *Evaluating very long-term conversational memory of LLM agents (LoCoMo)* — arXiv:2402.17753
- Markovic et al. (2025) — *Cognee: Optimizing the interface between KGs and LLMs for complex reasoning* — arXiv:2505.24478
- Packer et al. (2023) — *MemGPT: Towards LLMs as operating systems* — arXiv:2310.08560
- Pink et al. (2025) — *Position: Episodic memory is the missing piece for long-term LLM agents* — arXiv:2502.06975
- Rasmussen et al. (2025) — *Zep: A temporal knowledge graph architecture for agent memory* — arXiv:2501.13956

## Related Digests

- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects (Latimer et al., 2025) — sibling architecture with a four-network (W/B/O/S) typology cut by *epistemic source*. MIRIX's six-component cut is by *functional role*. The two are orthogonal and combinable — Hindsight's Opinion network with confidence-c is the missing piece in MIRIX (which has no native belief-with-confidence concept).
- [[liu-2025-memverse]] — MemVerse: Multimodal Memory for Lifelong Learning Agents (Liu et al., 2025) — three-subgraph LTM (core/episodic/semantic) + parametric memory cache. MIRIX extends the cognitive-typing further (adding Procedural / Resource / Vault to the core/episodic/semantic trio). MemVerse pushes the *speed* axis (parametric cache); MIRIX pushes the *routing* axis (multi-agent fan-out).
- [[chhikara-2025-mem0]] — Mem0: Building production-ready AI agents with scalable long-term memory (Chhikara et al., 2025) — the flat-fact-store baseline MIRIX positions against in §1 and §5. MIRIX outperforms Mem0 on LoCoMo overall (85.4% vs 62.5% on gpt-4.1-mini).
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as operating systems (Packer et al., 2023) — the OS-analogy ancestor. MIRIX inherits MemGPT's Core Memory persona+human block design verbatim (§3.1) and extends with five additional components.
- [[rasmussen-2025-zep-temporal-kg]] — Zep: A temporal knowledge graph architecture for agent memory (Rasmussen et al., 2025) — KG-only memory baseline. MIRIX outperforms Zep on LoCoMo overall (85.4% vs 79.1% on gpt-4.1-mini).
- [[xu-2025-a-mem-agentic-memory]] — A-Mem: Agentic memory for LLM agents (Xu et al., 2025) — Zettelkasten-style KG baseline. MIRIX outperforms A-Mem on LoCoMo overall (85.4% vs 48.4% on gpt-4o-mini).
- [[maharana-2024-locomo]] — LoCoMo benchmark (Maharana et al., 2024) — the shared eval substrate for MIRIX, Hindsight, MemVerse, Mem0, Zep, A-Mem, LangMem. The benchmark is the comparison point that lets all these architectures be measured on the same yardstick.

## Reviewer Notes

**Hallucination severity:** Clean

Spot-checks against the source PDF:

- **Six memory components: Core, Episodic, Semantic, Procedural, Resource, Knowledge Vault** — verified in §3.1 and Figure 1 (p. 2). ✓
- **MIRIX scores 85.38% overall on LoCoMo, +8 pp over LangMem (78.05%), approaching Full-Context (87.52%)** — verified in Table 2 (p. 11). The "+8 pp" framing uses LangMem's gpt-4o-mini result (78.05%) since MIRIX runs on gpt-4.1-mini, but the abstract claim is "best existing method" — the strongest gpt-4o-mini baseline is LangMem 78.05%. ✓
- **MIRIX Single-Hop 85.11 / Multi-Hop 83.70 / Open-Domain 65.62 / Temporal 88.39** — verified in Table 2 (p. 11). ✓
- **ScreenshotVQA results: MIRIX 0.5950 overall vs Gemini 0.1166 (+410%) vs SigLIP@50 0.4410 (+35%)** — verified in Table 1 (p. 11). Storage: 15.89 MB vs 236.70 MB Gemini (−93.3%) vs 15.07 GB SigLIP (−99.9%). ✓
- **ScreenshotVQA dataset: 3 PhD students, 5,886 / 18,178 / 5,349 images, 11 / 21 / 55 questions** — verified in §4.1.1 (p. 9). ✓
- **App: screenshot every 1.5s, drop near-duplicates above 0.99 similarity, batch update every 20 unique screenshots ~60s** — verified in §2.1, Memory Updates paragraph (p. 3). ✓
- **Streaming upload via Gemini reduces latency from ~50s (GPT-4 direct upload) to <5s** — verified in §2.1, Memory Updates final sentences (p. 3). ✓
- **Core Memory: persona + human blocks, rewrite at 90% capacity** — verified in §3.1 Core Memory paragraph (p. 6). ✓
- **Episodic Memory fields: event_type, summary, details, actor, timestamp** — verified in §3.1 Episodic Memory paragraph (p. 6). ✓
- **Semantic Memory fields: name, summary, details, source** — verified in §3.1 Semantic Memory paragraph (p. 7). ✓
- **Procedural Memory fields: entry_type ∈ {workflow, guide, script}, description, steps** — verified in §3.1 Procedural Memory paragraph (p. 7). ✓
- **Resource Memory fields: title, summary, resource_type ∈ {doc, markdown, pdf_text, image, voice_transcript}** — verified in §3.1 Resource Memory paragraph (p. 7). ✓
- **Knowledge Vault fields: entry_type, source, sensitivity ∈ {low, medium, high}, secret_value** — verified in §3.1 Knowledge Vault paragraph (p. 7). ✓
- **Active Retrieval: agent generates topic before retrieval, retrieves top-10 from each of six components, tags by source `<episodic_memory>...</episodic_memory>`** — verified in §3.2 (p. 7) with Figure 5. ✓
- **Backbone models: Gemini-2.5-flash-preview-04-17 for ScreenshotVQA, gpt-4.1-mini for LoCoMo** — verified in §4.1.2 (p. 9–10). Choice of gpt-4.1-mini explicitly justified by Berkeley Function Calling Leaderboard (gpt-4o-mini 22.12 vs gpt-4.1-mini 29.75). ✓
- **8 agents total: 6 Memory Managers + 1 Meta Memory Manager + 1 Chat Agent** — verified in §1 contributions list and §3.3 (p. 8). ✓
- **arXiv ID 2507.07957v1, submitted 10 Jul 2025** — verified in title page header. ✓
- **Authors Yu Wang (yuw164@ucsd.edu), Xi Chen (xc13@stern.nyu.edu), affiliation MIRIX AI** — verified in author block (p. 1). ✓
- **Site mirix.io, app Mirix-AI/MIRIX repo** — verified in title page + §4.1.2 footnotes. ✓

One caveat documented in the digest: the §2.3 Memory Marketplace section is speculative product-vision (decentralized memory trading, AI personas of celebrities, "memory as digital asset class") with no implementation details and no claims tied to the experimental results. The digest correctly flags this as orthogonal to the architectural contribution.

No fabricated claims found. Severity: **Clean**.
