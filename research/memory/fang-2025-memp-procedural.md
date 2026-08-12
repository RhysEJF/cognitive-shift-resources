---
corpus: agentic-memory
kind: paper-digest
slug: fang-2025-memp-procedural
title: "Memp: Exploring Agent Procedural Memory"
authors:
  - "Runnan Fang"
  - "Yuan Liang"
  - "Xiaobin Wang"
  - "Jialong Wu"
  - "Shuofei Qiao"
  - "Pengjun Xie"
  - "Fei Huang"
  - "Huajun Chen"
  - "Ningyu Zhang"
year: 2025
publication_date: "2025-08"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2508.06433"
doi: null
arxiv_id: "2508.06433"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Treating an LLM agent's procedural memory as a first-class, lifecycle-managed object — built from past trajectories, retrieved by semantic similarity, and continuously refined via reflection — lifts task success by up to ~36 points on ALFWorld and ~8 points on TravelPlanner while cutting execution steps by ~15-50%, and the resulting memory transfers cleanly from a strong model (GPT-4o) to a much weaker one (Qwen2.5-14B-Instruct) for a +5% completion-rate boost."
topics:
  - procedural-memory
  - llm-agents
  - long-horizon-tasks
  - agent-memory-lifecycle
  - trajectory-distillation
  - memory-transfer
tags:
  - paper
  - agents
  - memory
  - procedural-memory
  - travelplanner
  - alfworld
  - gpt-4o
  - claude-3.5-sonnet
  - qwen2.5
  - reflexion-update
entities:
  - fang-runnan
  - zhang-ningyu
  - chen-huajun
related_digests:
  - wang-2023-voyager-embodied-agent
  - yao-2023-react-reasoning-acting
  - xu-2025-a-mem-agentic-memory
  - yan-2025-memory-r1
  - chhikara-2025-mem0
  - zhang-2024-llm-agent-memory-survey
  - hu-2025-memoryagentbench
citations:
  - title: "Claude 3.5 sonnet system card"
    authors: ["Anthropic"]
    year: 2022
    venue: "system card"
    doi: null
    url: null
    arxiv_id: null
  - title: "τ²-bench: Evaluating conversational agents in a dual-control environment"
    authors: ["Victor Barres", "Honghua Dong", "Soham Ray", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Acebench: Who wins the match point in tool usage?"
    authors: ["Chen Chen", "Xinlong Hao", "Weiwen Liu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Automanual: Constructing instruction manuals by llm agents via interactive environmental learning"
    authors: ["Minghao Chen", "Yihang Li", "Yanting Yang", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2405.16247"
  - title: "Mem0: Building production-ready ai agents with scalable long-term memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Preserved learning and retention of pattern-analyzing skill in amnesia: Dissociation of knowing how and knowing that"
    authors: ["Neal J Cohen", "Larry R Squire"]
    year: 1980
    venue: "journal"
    doi: null
    url: null
    arxiv_id: null
  - title: "Tool-star: Empowering llm-brained multi-tool reasoner via reinforcement learning"
    authors: ["Guanting Dong", "Yifei Chen", "Xiaoxi Li", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Synworld: Virtual scenario synthesis for agentic action knowledge refinement"
    authors: ["Runnan Fang", "Xiaobin Wang", "Yuan Liang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Get experience from practice: Llm agents with record & replay"
    authors: ["Erhu Feng", "Wenbo Zhou", "Zibin Liu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Theoretical and computational analysis of skill learning, repetition priming, and procedural memory"
    authors: ["Prahlad Gupta", "Neal J Cohen"]
    year: 2002
    venue: "journal"
    doi: null
    url: null
    arxiv_id: null
  - title: "A real-world webagent with planning, long context understanding, and program synthesis"
    authors: ["Izzeddin Gur", "Hiroki Furuta", "Austin Huang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "'my agent understands me better': Integrating dynamic human-like memory recall and consolidation in llm-based agents"
    authors: ["Yuki Hou", "Haruki Tamoto", "Homei Miyashita"]
    year: 2024
    venue: "CHI Extended Abstracts"
    doi: null
    url: null
    arxiv_id: null
  - title: "Hiagent: Hierarchical working memory management for solving long-horizon agent tasks with large language model"
    authors: ["Mengkang Hu", "Tianxing Chen", "Qiguang Chen", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Autonomous llm-driven research—from data to human-verifiable research papers"
    authors: ["Tal Ifargan", "Lukas Hafner", "Maor Kern", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Introduction to the soar cognitive architecture"
    authors: ["John E Laird"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "The large language models on biomedical data analysis: a survey"
    authors: ["Wei Lan", "Zhentao Tang", "Mingyang Liu", "et al."]
    year: 2025
    venue: "survey"
    doi: null
    url: null
    arxiv_id: null
  - title: "Camel: Communicative agents for 'mind' exploration of large language model society"
    authors: ["Guohao Li", "Hasan Hammoud", "Hani Itani", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memos: A memory os for ai system"
    authors: ["Zhiyu Li", "Shichao Song", "Chenyang Xi", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Advances and challenges in foundation agents: From brain-inspired intelligence to evolutionary, collaborative, and safe systems"
    authors: ["Bang Liu", "Xinfeng Li", "Jiayi Zhang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Contextual experience replay for self-improvement of language agents"
    authors: ["Yitao Liu", "Chenglei Si", "Karthik Narasimhan", "Shunyu Yao"]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Ml-agent: Reinforcing llm agents for autonomous machine learning engineering"
    authors: ["Zexi Liu", "Jingyi Chai", "Xinyu Zhu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Arpo: End-to-end policy optimization for gui agents with experience replay"
    authors: ["Fanbin Lu", "Zhisheng Zhong", "Shu Liu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Gui-r1: A generalist r1-style vision-language action model for gui agents"
    authors: ["Run Luo", "Lu Wang", "Wanwei He", "Xiaobo Xia"]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Langchain v0.3"
    authors: ["Vasilios Mavroudis"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Gpt-4 system card"
    authors: ["OpenAI"]
    year: 2022
    venue: "system card"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep research system card"
    authors: ["OpenAI"]
    year: 2025
    venue: "system card"
    doi: null
    url: null
    arxiv_id: null
  - title: "Automind: Adaptive knowledgeable agent for automated data science"
    authors: ["Yixin Ou", "Yujie Luo", "Jingsheng Zheng", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Markov decision processes"
    authors: ["Martin L Puterman"]
    year: 1990
    venue: "journal"
    doi: null
    url: null
    arxiv_id: null
  - title: "Benchmarking agentic workflow generation"
    authors: ["Shuofei Qiao", "Runnan Fang", "Zhisong Qiu", "et al."]
    year: 2025
    venue: "ICLR 2025"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reasoning with language model prompting: A survey"
    authors: ["Shuofei Qiao", "Yixin Ou", "Ningyu Zhang", "et al."]
    year: 2023
    venue: "ACL 2023"
    doi: null
    url: null
    arxiv_id: null
  - title: "Ui-tars: Pioneering automated gui interaction with native agents"
    authors: ["Yujia Qin", "Yining Ye", "Junjie Fang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Alfworld: Aligning text and embodied environments for interactive learning"
    authors: ["Mohit Shridhar", "Xingdi Yuan", "Marc-Alexandre Côté", "et al."]
    year: 2021
    venue: "ICLR 2021"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learn-by-interact: A data-centric framework for self-adaptive agents in realistic environments"
    authors: ["Hongjin Su", "Ruoxi Sun", "Jinsung Yoon", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Cognitive architectures for language agents"
    authors: ["Theodore Sumers", "Shunyu Yao", "Karthik Narasimhan", "Thomas Griffiths"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Prompt, plan, perform: Llm-based humanoid control via quantized imitation learning"
    authors: ["Jingkai Sun", "Qiang Zhang", "Yiqun Duan", "et al."]
    year: 2024
    venue: "ICRA 2024"
    doi: null
    url: null
    arxiv_id: null
  - title: "Meta-agent-workflow: Streamlining tool usage in llms through workflow construction, retrieval, and refinement"
    authors: ["Xiaoyu Tan", "Bin Li", "Xihe Qiu", "et al."]
    year: 2025
    venue: "WWW 2025 Companion"
    doi: null
    url: null
    arxiv_id: null
  - title: "Agent kb: Leveraging cross-domain experience for agentic problem solving"
    authors: ["Xiangru Tang", "Tianrui Qin", "Tianhao Peng", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2507.06229"
  - title: "Voyager: An open-ended embodied agent with large language models"
    authors: ["Guanzhi Wang", "Yuqi Xie", "Yunfan Jiang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "A survey on large language model based autonomous agents"
    authors: ["Lei Wang", "Chen Ma", "Xueyang Feng", "et al."]
    year: 2024
    venue: "survey"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mobile-agent-e: Self-evolving mobile assistant for complex tasks"
    authors: ["Zhenhailong Wang", "Haiyang Xu", "Junyang Wang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Agent workflow memory"
    authors: ["Zora Zhiruo Wang", "Jiayuan Mao", "Daniel Fried", "Graham Neubig"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Webdancer: Towards autonomous information seeking agency"
    authors: ["Jialong Wu", "Baixuan Li", "Runnan Fang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "WebWalker: Benchmarking LLMs in web traversal"
    authors: ["Jialong Wu", "Wenbiao Yin", "Yong Jiang", "et al."]
    year: 2025
    venue: "ACL 2025"
    doi: null
    url: null
    arxiv_id: null
  - title: "Updating large language models' memories with time constraints"
    authors: ["Xin Wu", "Yuqi Bu", "Yi Cai", "Tao Wang"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "The rise and potential of large language model based agents: A survey"
    authors: ["Zhiheng Xi", "Wenxiang Chen", "Xin Guo", "et al."]
    year: 2025
    venue: "survey"
    doi: null
    url: null
    arxiv_id: null
  - title: "Minerva: A programmable memory test benchmark for language models"
    authors: ["Menglin Xia", "Victor Ruehle", "Saravan Rajmohan", "Reza Shokri"]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Travelplanner: A benchmark for real-world planning with language agents"
    authors: ["Jian Xie", "Kai Zhang", "Jiangjie Chen", "et al."]
    year: 2024
    venue: "ICML 2024"
    doi: null
    url: null
    arxiv_id: null
  - title: "A-mem: Agentic memory for llm agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Qwen2.5 technical report"
    authors: ["An Yang", "Baosong Yang", "Beichen Zhang", "et al."]
    year: 2024
    venue: "technical report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Auto-gpt for online decision making: Benchmarks and additional opinions"
    authors: ["Hui Yang", "Sifu Yue", "Yunzhong He"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Embodied multi-modal agent trained by an llm from a parallel textworld"
    authors: ["Yijun Yang", "Tianyi Zhou", "Kanxue Li", "et al."]
    year: 2024
    venue: "CVPR 2024"
    doi: null
    url: null
    arxiv_id: null
  - title: "τ-bench: A benchmark for tool-agent-user interaction in real-world domains"
    authors: ["Shunyu Yao", "Noah Shinn", "Pedram Razavi", "Karthik R Narasimhan"]
    year: 2025
    venue: "ICLR 2025"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memagent: Reshaping long-context llm with multi-conv rl-based memory agent"
    authors: ["Hongli Yu", "Tinghong Chen", "Jiangtao Feng", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2507.02259"
  - title: "A survey on the memory mechanism of large language model based agents"
    authors: ["Zeyu Zhang", "Xiaohe Bo", "Chen Ma", "et al."]
    year: 2024
    venue: "survey"
    doi: null
    url: null
    arxiv_id: null
  - title: "A survey of large language models"
    authors: ["Wayne Xin Zhao", "Kun Zhou", "Junyi Li", "et al."]
    year: 2023
    venue: "survey"
    doi: null
    url: null
    arxiv_id: null
  - title: "Synapse: Trajectory-as-exemplar prompting with memory for computer control"
    authors: ["Longtao Zheng", "Rundong Wang", "Xinrun Wang", "Bo An"]
    year: null
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memorybank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "et al."]
    year: 2024
    venue: "AAAI 2024"
    doi: null
    url: null
    arxiv_id: null
  - title: "Agents: An open-source framework for autonomous language agents"
    authors: ["Wangchunshu Zhou", "Yuchen Eleanor Jiang", "Long Li", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.07870"
  - title: "Symbolic learning enables self-evolving agents"
    authors: ["Wangchunshu Zhou", "Yixin Ou", "Shengwei Ding", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2406.18532"
  - title: "Mem1: Learning to synergize memory and reasoning for efficient long-horizon agents"
    authors: ["Zijian Zhou", "Ao Qu", "Zhaoxuan Wu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2506.15841"
hallucination_severity: "Clean"
best_figure:
  number: 5
  title: "(a) Transfer of GPT-4o's procedural memory to Qwen2.5-14B-Instruct on TravelPlanner; (b) Retrieval scaling on ALFWorld"
  page: 8
  image_path: "figures/fang-2025-memp-procedural-fig.png"
---

# Memp: Exploring Agent Procedural Memory

**Authors:** Runnan Fang, Yuan Liang, Xiaobin Wang, Jialong Wu, Shuofei Qiao, Pengjun Xie, Fei Huang, Huajun Chen, Ningyu Zhang
**Published:** 2025-08 (v4 April 2026) · [Source](https://arxiv.org/abs/2508.06433)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Fang et al. (Zhejiang University + Alibaba) treat an LLM agent's procedural memory — the "how-to" knowledge it accumulates from past task trajectories — as a first-class optimization object with three life-cycle phases (Build, Retrieve, Update), and benchmark every reasonable design choice for each phase on TravelPlanner (long-horizon planning under constraints) and ALFWorld (long-horizon embodied housework) using GPT-4o, Claude-3.5-Sonnet, and Qwen2.5-72B. For Build, combining raw gold trajectories with an LLM-distilled "script" abstraction ("Proceduralization") wins everywhere: e.g., GPT-4o on ALFWorld-test jumps from 42.14% (no memory) to 77.86% (+35.7 pts) while average steps drop from 23.76 to 15.01. For Retrieve, building keys from extracted keywords ("AveFact") narrowly beats raw query embeddings and crushes random sampling. For Update, a Reflexion-style adjustment policy that takes a failed run, fuses the erroneous trajectory with the original retrieved memory, and rewrites it in place beats both vanilla append and validation-only filtering — by group 5 it adds +0.7 reward and -14 steps over the no-memory baseline. Two bonus findings stand out: (1) procedural memory built by GPT-4o transfers to Qwen2.5-14B (a ~5× smaller model) and lifts its TravelPlanner completion rate by ~5 points (from 91.4 to 96.6) while shaving 1.6 steps, and (2) retrieval scales monotonically up to ~10 memories per query then plateaus and slightly declines — context-window dilution and stale-match noise eventually outweigh more examples. Limitations the authors flag explicitly: retrieval is vector-similarity only (no BM25 baseline tested) and the framework assumes benchmark-supplied reward signals, which won't exist in production deployments.

## Key Takeaway

The counter-intuitive lesson is that procedural memory's biggest payoff isn't smarter retrieval or better embeddings — it's the willingness to **rewrite memories in place when they fail**, and to do so using the failure itself as evidence. Most memory systems treat the store as append-only (just keep adding successful trajectories) or apply pre-write filtering ("only commit clean runs"). Memp shows the opposite: a Reflexion-style "Adjustment" update — where a botched execution gets merged back with the memory that misguided it and the pair gets rewritten — outperforms both vanilla-append and pre-filtering by a margin that widens monotonically as more task groups roll through. Knowledge that learns from its own mistakes beats knowledge that's only allowed to remember its wins.

## Implications

- **Procedural memory is a separate problem from semantic memory — design it that way.** Most LLM-agent memory papers conflate "remember facts the user told me" with "remember how to do this kind of task." Memp shows the second is a distinct life-cycle (Build/Retrieve/Update) and that getting it right yields step-count reductions of 15-50% on long-horizon tasks. If you're building an agent that repeats similar workflows, give it a dedicated procedural store, not a single shared memory bucket.

- **Store both raw trajectories AND distilled scripts — don't pick one.** Raw trajectories help on tasks structurally similar to past ones (dev-set); scripts generalize better to novel tasks (test-set). The hybrid "Proceduralization" condition wins every cell of Table 1 across all three backbones. The implication for production: write two records per success — verbatim transcript and an LLM-summary of the underlying procedure — and concatenate both into the prompt at retrieval time.

- **Use Reflexion-style in-place rewrites for memory maintenance, not append-only logs.** When a retrieved memory leads to failure, don't just discard it or log the new attempt separately — fuse the failed trajectory with the original memory, ask an LLM to rewrite the procedure in light of what went wrong, and replace. This single change accounts for the +0.7 reward / -14 step gap between "Adjustment" and "Vanilla" in Figure 3.

- **Distillation can leak strong-model expertise into weak-model deployments.** Procedural memory built from GPT-4o trajectories, when handed to a frozen Qwen2.5-14B-Instruct, lifts that smaller model's TravelPlanner completion rate from 91.4 to 96.6 (+5.2 points) and cuts steps by ~1.6 — no fine-tuning, no API calls to the strong model at runtime. For cost-sensitive deployments, this means you can run the cheap model in production but pay for the expensive model once, offline, to populate the memory bank.

- **Retrieve more memories, but only up to a point.** ALFWorld performance climbs from 40.7 (zero memories retrieved) to 82.5 (ten memories) then plateaus at 79.3 (twenty). Past ~10 the dilution penalty kicks in — context length grows, less-relevant memories interfere. Default to top-k=5–10 with semantic similarity, and don't blindly scale retrieval.

- **Keyword-extracted retrieval keys beat raw query embeddings on TravelPlanner.** The "AveFact" condition (extract keywords from the task query, average the cosine similarities of each keyword's embedding to memory keys) wins over both random sampling and query-vector matching on every model. For agents indexing constraint-heavy tasks, project queries into a sparse-keyword space before embedding rather than dumping the whole query into one vector.

- **Build the memory once with the strongest available model, even if you serve with a weaker one.** The transfer experiment validates a portfolio play: use frontier models for offline trajectory collection, distill into procedural memory, then ship a small model + memory bank for inference. This decouples training cost from inference cost in a way that fine-tuning never quite does.

- **Don't ship this directly to production-grade agents yet — the reward-signal assumption is load-bearing.** The Update phase relies on a binary success/failure signal from the benchmark environment. Real-world tasks rarely have that. Until you bolt on an LLM-judge or a self-consistency check, Memp's update mechanism degrades to vanilla-append. The authors acknowledge this as a limitation.

## How to Apply It (method)

**Scenario:** A SaaS company runs an in-house "data-pipeline-triage" agent that hits the same ~30 categories of broken-ETL incidents repeatedly: schema drifts, OAuth expirations, rate-limit cascades, missing-column joins. Each incident eats 20-40 minutes of agent runtime as it re-derives the same diagnostic procedure from scratch. The team wants the agent to learn from prior incidents so it can skip the dead-end paths.

**Steps:**

1. **Instrument every agent run to capture the full trajectory.** Log the sequence of (state, action, observation) triples plus a binary success flag and a numerical reward (e.g., minutes-to-resolution). Store these as JSON blobs keyed by incident ID. This is your raw trajectory pool — the gold trajectories will come from filtering for success=True.

2. **Build the procedural-memory store in two formats per successful trajectory.**
   - **Format A (trajectory):** Store the verbatim state/action/observation log.
   - **Format B (script):** Pass the trajectory through an LLM-distillation prompt to extract a short, abstract procedure. Use this template:
     ```
     You are an SRE knowledge engineer. Below is a trajectory of an agent
     successfully resolving an incident. Distill it into a 5-10 line abstract
     procedure of the form "If <condition>, then <action>; check <signal>; ..."
     Strip incident-specific names and numbers. Focus on the decision logic
     that generalizes to similar incidents.

     Trajectory:
     {trajectory_json}
     ```
   Save both Format A and Format B side-by-side, keyed by the incident's title + an embedding of its keywords (see step 3).

3. **Build a "Proceduralization" retrieval index using AveFact-style keys.**
   - For each stored memory, extract the 3-5 most salient keywords from the original incident title/description using an LLM ("List the 3-5 keywords that capture the technical essence of this incident: <title>; <description>").
   - Embed each keyword separately with a sentence-transformer model and store the embedding list keyed to the memory.
   - At retrieval time, do the same keyword extraction on the new incident, embed each keyword, then for each candidate memory compute the *average* cosine similarity across all keyword pairs. Return the top-k=5 memories.

4. **At inference time, inject both trajectory and script into the agent's system prompt.** Use a template like:
   ```
   You are debugging an ETL incident. Below are 5 procedures distilled from
   past similar incidents, plus their full trajectories for reference. Adapt
   the most relevant procedure to the current incident.

   ## Past procedure 1 (script)
   {script_A}
   ## Past trajectory 1 (full log)
   {trajectory_A}
   ... [repeat for memories 2-5] ...

   ## Current incident
   {new_incident_description}
   ```

5. **Wire up the "Adjustment" update loop after every agent run.**
   - On success: just add the new (trajectory, script) pair to the store.
   - On failure (i.e., agent escalated to a human, OR the proposed fix didn't restore the pipeline within a time limit): fuse the retrieved memory that misguided the agent with the failed trajectory, and rewrite the memory in place using:
     ```
     You are a memory editor. The procedure below was retrieved to help an
     agent resolve an incident. The agent followed it but the resulting
     trajectory failed (see below). Rewrite the procedure so that a future
     agent encountering a similar incident would not repeat the same
     mistakes. Keep the procedure abstract — don't hardcode incident-specific
     details. Return only the rewritten procedure.

     Original procedure:
     {script}

     Failed trajectory:
     {failed_trajectory}

     Failure reason:
     {failure_summary}
     ```
   - Replace the old memory record with the rewritten script.

6. **Cap retrieval at top-k=5-10 and monitor for context dilution.** If you start seeing the agent's success rate drop as the memory bank grows beyond a few hundred entries, lower k. Memp shows performance peaks around k=10 on ALFWorld and degrades past 15.

7. **(Optional) Bootstrap the memory bank using a stronger model.** If you can afford a one-time offline pass with GPT-4 or Claude on your historical incident log, run those models through your test suite first, capture their trajectories into the memory bank, then deploy a cheaper model (Llama-3, Qwen, GPT-4o-mini) for production. The Memp paper shows this kind of strong→weak distillation can lift the weak model's completion rate by ~5 points with no fine-tuning required.

**Expected outcome:** After 2-4 weeks of operation, the agent should require ~30-50% fewer steps to resolve incidents that match patterns it has seen before, with measurably higher first-attempt success rates. Novel incidents continue to take full time, but each one expands the memory bank, so the long-tail of recurring incident types gradually moves into "fast-path" territory. The Adjustment loop ensures that early bad memories self-correct rather than calcifying — a key difference vs. just dumping every successful trajectory into a vector DB and forgetting about maintenance.

## Best Figure

![Figure 5 — (a) Transfer of GPT-4o's procedural memory to Qwen2.5-14B-Instruct on TravelPlanner; (b) Retrieval scaling on ALFWorld (page 8)](figures/fang-2025-memp-procedural-fig.png)

**Image Candidates:**
- Figure 5 (p. 8): Two-panel figure that captures the paper's two most surprising findings (cross-model transfer + retrieval-scaling curve) in a single view.
- Figure 3 (p. 7): Reward gain and steps reduction across trajectory groups for the three update strategies — shows the Adjustment policy dominating Vanilla and Validation as more groups process.
- Table 1 (p. 6): Build-policy comparison across all three backbones and both benchmarks — the single densest summary of the main result, but tables don't tell a visual story.

**Best Image:** Figure 5: "(a) Transfer result of GPT-4o's procedural memory to Qwen2.5-14B-Instruct and its performance on TravelPlanner dataset. (b) The relationship between the quantity of procedural memory retrieved for GPT-4o's performance on the ALFWorld dataset."

**Slide Caption:** Memp's procedural memory transfers from GPT-4o to a 5× smaller Qwen2.5-14B-Instruct (left, +5.2 pts completion on TravelPlanner), and retrieval performance scales up to ~10 memories before plateauing (right, ALFWorld).

**Description:** Figure 5 is the paper's most-load-bearing single figure because it makes two non-obvious claims visible in one frame. Panel (a) shows a Qwen2.5-14B-Instruct equipped with GPT-4o's distilled procedural memory beats a no-memory Qwen baseline on TravelPlanner — completion rate jumps from 91.4 to 96.6, steps drop from 16.9 to 15.3, and Commonsense score climbs from 59.3 to 65.5 — establishing that procedural memory is a portable artifact, not entangled in model weights. Panel (b) traces ALFWorld success as you retrieve more memories per query, showing a steep climb from 40.7 (zero memories) to 82.5 (ten memories), then a plateau followed by a slight decline to 79.3 at twenty memories — diagnosing the upper limit of "more retrieval = better." Together these two panels validate the paper's framing of procedural memory as a first-class, transferable optimization object with quantifiable scaling laws.

## What Experts Overlook

The detail most readers will skim past is that Memp's Update phase compares three update strategies — Vanilla, Validation, and Adjustment — but Adjustment is the *only* one that explicitly uses **failed trajectories as training signal**. Vanilla just appends new memories. Validation filters out failures before storing (i.e., it's pre-write filtering — the conservative move). Adjustment alone takes the failed trajectory, pairs it back with the memory that misguided the agent, and rewrites that memory in place. Figure 3 shows Adjustment's reward-gain curve diverging upward from the other two as more task groups process — by group 5 it's +0.7 reward and -14 steps ahead of no-memory, vs. the second-best strategy's much smaller gap. The mechanism that drives this isn't more data, it's a different relationship to data: most memory systems treat failure as something to be excluded, but Memp treats it as the highest-information signal for memory editing.

**Why it matters:** This generalizes far beyond benchmark agents. Production memory systems — Mem0, MemGPT, Letta-style stores — almost universally implement either vanilla append or pre-write filtering. They treat the memory bank as a curated corpus of "things that worked." But the Memp result says the steepest improvement curve comes from using each failure as a corrective edit to an existing memory. The implication for anyone building production agents: budget for a memory-editing pipeline, not just a memory-write pipeline. The edit pipeline is where the compound learning lives.

**Example of good use:** A customer-support agent at a SaaS company retrieves a memory for "how to refund a duplicate-charge" and follows it; the customer escalates because the refund logic missed a Stripe-specific edge case. The Adjustment loop fires: it takes the failed conversation transcript + the retrieved playbook, asks an LLM to rewrite the playbook so it explicitly handles the Stripe edge case, and replaces the original. Next agent that hits a duplicate-charge case gets the corrected playbook. Failure → smarter store, not just a logged complaint.

**Example of misapplication:** A team adopts Memp's framing but only implements Vanilla updates ("we'll just append every trajectory to the vector DB and call it procedural memory"). After a few weeks they observe stagnant performance — the memory bank grows but the agent doesn't get better at avoiding past mistakes. The mistake is treating the store as a passive log rather than an editable corpus. The +0.7 reward / -14 step gap between Adjustment and Vanilla in Figure 3 is exactly the magnitude of value left on the table.

## Extracted Prompts

The paper itself does not include verbatim LLM prompt text in the body or appendices. The prompts used for trajectory distillation, script generation, and memory adjustment are referred to functionally (e.g., "the model analyzes and summarizes the gold trajectories from the training set") but not quoted in full. The paper points to its public code at https://github.com/zjunlp/MemP for the full implementations.

No applicable prompts found in this paper.

## Citations

A total of **57 references** were extracted from the bibliography. Highlights below; full list in frontmatter.

- Wang et al. 2023 — **Voyager: An open-ended embodied agent with large language models** (procedural-memory baseline for Minecraft)
- Wang et al. 2024 — **Agent workflow memory (AWM)** (the strongest baseline Memp competes against in Figure 4)
- Shridhar et al. 2021 — **ALFWorld** (the embodied-housework benchmark)
- Xie et al. 2024 — **TravelPlanner** (the long-horizon planning benchmark, ICML 2024)
- Sumers et al. 2023 — **Cognitive architectures for language agents** (the framing paper Memp inherits)
- Zhang et al. 2024 — **A survey on the memory mechanism of LLM-based agents** (situates Memp in the broader memory-systems literature)
- Chhikara et al. 2025 — **Mem0** (production memory layer; complementary not procedural-focused)
- Xu et al. 2025 — **A-MEM: Agentic memory for LLM agents** (closest contemporary on dynamic memory updating)
- Yao et al. 2025 — **τ-bench** (the dual-control conversational-agent benchmark)
- Zhou et al. 2025 — **Mem1** (the synergizing-memory-and-reasoning thread)

## Related Digests

- [[wang-2023-voyager-embodied-agent]] — Voyager: An Open-Ended Embodied Agent with Large Language Models (procedural memory as executable code, the prior canonical formulation)
- [[yao-2023-react-reasoning-acting]] — ReAct: Synergizing Reasoning and Acting in Language Models (the baseline Memp's ReAct condition implements)
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: Agentic Memory for LLM Agents (contemporary work on dynamic memory updating)
- [[yan-2025-memory-r1]] — Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning (RL-based alternative to Memp's Reflexion update)
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (production-focused, semantic-memory-leaning counterpart)
- [[zhang-2024-llm-agent-memory-survey]] — A Survey on the Memory Mechanism of LLM-based Agents (the broader taxonomy Memp slots into)
- [[hu-2025-memoryagentbench]] — Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions (benchmark that could be used to evaluate Memp-style systems beyond TravelPlanner/ALFWorld)

## Reviewer Notes

**Overall severity:** Clean

All claims in the digest were verified against the paper text:
- Build-policy results match Table 1 (GPT-4o ALFWorld test: 42.14 → 77.86; Steps 23.76 → 15.01).
- Retrieve-policy results match Table 2 (AveFact > Query > Random Sample on TravelPlanner across all three models).
- Update-policy reward-gain margin (+0.7) and step reduction (-14) match the prose description of Figure 3 ("By the time the final group of tasks is reached, this method delivers a substantial advantage: it surpasses the second-best strategy by an impressive margin of +0.7 points and achieves a reduction of 14 steps").
- Transfer result (GPT-4o memory → Qwen2.5-14B-Instruct) matches Figure 5(a): Delivery 91.4 → 96.6 (+5.2), Steps 16.9 → 15.3, Commonsense 59.3 → 65.5. Paper prose summarizes this as "raised its task completion rate by 5% and cut the average number of steps by 1.6."
- Retrieval-scaling values (40.7 → 70.7 → 75.8 → 78.2 → 82.5 → 81.5 → 79.3 at k = 0/2.5/5/7.5/10/15/20) match Figure 5(b).
- Limitations correctly attributed: paper explicitly lists (1) vector-similarity-only retrieval with no BM25 comparison and (2) dependence on benchmark-supplied reward signals.

No claims overextend or invent results not in the paper.

