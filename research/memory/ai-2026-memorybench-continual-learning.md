---
corpus: agentic-memory
kind: paper-digest
slug: ai-2026-memorybench-continual-learning
title: "MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems"
authors:
  - "Qingyao Ai"
  - "Yichen Tang"
  - "Changyue Wang"
  - "Jianming Long"
  - "Weihang Su"
  - "Yiqun Liu"
year: 2026
publication_date: "2026-05"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2510.17281"
doi: null
arxiv_id: "2510.17281"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Throw away your fancy LLM-memory system — for almost every real task, dumping training-dialog feedback into a vanilla BM25 index beats the SOTA memory architectures (A-Mem, Mem0, MemoryOS), because those systems were tuned against reading-comprehension benchmarks (LoCoMo) and silently assume every memory is declarative, so they choke on procedural feedback logs."
topics:
  - memory-architecture
  - continual-learning
  - llm-feedback
  - procedural-memory
  - benchmarks
  - retrieval-augmented-generation
  - llm-evaluation
tags:
  - paper
  - benchmark
  - memory
  - feedback-simulation
  - rag
  - llm-as-user
  - engram-encode
  - engram-network
  - engram-retrieve
  - engram-aggregate
  - engram-maintain
entities:
  - ai-qingyao
  - tang-yichen
  - wang-changyue
  - long-jianming
  - su-weihang
  - liu-yiqun
  - thuir
related_digests:
  - xu-2025-a-mem-agentic-memory
  - chhikara-2025-mem0
  - kang-2025-memory-os
  - latimer-2025-hindsight-memory
  - wu-2026-lme-v2
  - du-2025-rethinking-memory
citations:
  - title: "Maturation of the adolescent brain"
    authors: ["M. Arain", "M. Haque", "L. Johal", "et al."]
    year: 2013
    venue: "Neuropsychiatric disease and treatment"
    doi: null
    url: null
    arxiv_id: null
  - title: "Human memory: A proposed system and its control processes"
    authors: ["R. C. Atkinson", "R. M. Shiffrin"]
    year: 1968
    venue: "Psychology of learning and motivation"
    doi: null
    url: null
    arxiv_id: null
  - title: "User simulation for evaluating information access systems"
    authors: ["K. Balog", "C. Zhai"]
    year: 2023
    venue: "SIGIR-AP"
    doi: "10.1145/3624918.3629549"
    url: null
    arxiv_id: null
  - title: "METEOR: An automatic metric for MT evaluation with improved correlation with human judgments"
    authors: ["S. Banerjee", "A. Lavie"]
    year: 2005
    venue: "ACL Workshop on Intrinsic and Extrinsic Evaluation Measures"
    doi: null
    url: null
    arxiv_id: null
  - title: "A non-factoid question-answering taxonomy"
    authors: ["V. Bolotova", "V. Blinov", "F. Scholer", "et al."]
    year: 2022
    venue: "SIGIR '22"
    doi: "10.1145/3477495.3531926"
    url: null
    arxiv_id: null
  - title: "'Don't get too technical with me': A discourse structure-based framework for automatic science journalism"
    authors: ["R. Cardenas", "B. Yao", "D. Wang", "Y. Hou"]
    year: 2023
    venue: "EMNLP"
    doi: "10.18653/v1/2023.emnlp-main.76"
    url: null
    arxiv_id: null
  - title: "How people use ChatGPT"
    authors: ["A. Chatterji", "T. Cunningham", "D. J. Deming", "et al."]
    year: 2025
    venue: "NBER Technical Report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Overview of the NTCIR-18 Automatic Evaluation of LLMs (AEOLLM) task"
    authors: ["J. Chen", "H. Li", "Z. Chu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2503.13038"
    arxiv_id: "2503.13038"
  - title: "Mem0: Building production-ready AI agents with scalable long-term memory"
    authors: ["P. Chhikara", "D. Khant", "S. Aryan", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2504.19413"
  - title: "Organizational routines are stored as procedural memory: Evidence from a laboratory study"
    authors: ["M. D. Cohen", "P. Bacdayan"]
    year: 1994
    venue: "Organization Science"
    doi: null
    url: null
    arxiv_id: null
  - title: "A computer readability formula designed for machine scoring"
    authors: ["M. Coleman", "T. L. Liau"]
    year: 1975
    venue: "Journal of Applied Psychology"
    doi: null
    url: null
    arxiv_id: null
  - title: "An experimental comparison of click position-bias models"
    authors: ["N. Craswell", "O. Zoeter", "M. Taylor", "B. Ramsey"]
    year: 2008
    venue: "WSDM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Search engines: Information retrieval in practice"
    authors: ["W. B. Croft", "D. Metzler", "T. Strohman", "et al."]
    year: 2010
    venue: "Addison-Wesley"
    doi: null
    url: null
    arxiv_id: null
  - title: "A formula for predicting readability"
    authors: ["E. Dale", "J. S. Chall"]
    year: 1948
    venue: "Educational research bulletin"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["J. Devlin", "M.-W. Chang", "K. Lee", "K. Toutanova"]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "PerLTQA: A personal long-term memory dataset for memory classification, retrieval, and synthesis in QA"
    authors: ["Y. Du", "H. Wang", "Z. Zhao", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2402.16288"
    arxiv_id: "2402.16288"
  - title: "Hierarchical neural story generation"
    authors: ["A. Fan", "M. Lewis", "Y. Dauphin"]
    year: 2018
    venue: "ACL"
    doi: "10.18653/v1/P18-1082"
    url: null
    arxiv_id: null
  - title: "DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning"
    authors: ["D. Guo", "D. Yang", "H. Zhang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2501.12948"
  - title: "IdeaBench: Benchmarking large language models for research idea generation"
    authors: ["S. Guo", "A. H. Shariatmadari", "G. Xiong", "et al."]
    year: 2025
    venue: "KDD"
    doi: "10.1145/3711896.3737419"
    url: null
    arxiv_id: null
  - title: "LoRA: Low-rank adaptation of large language models"
    authors: ["E. J. Hu", "Y. Shen", "P. Wallis", "et al."]
    year: 2022
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Evaluating memory in LLM agents via incremental multi-turn interactions"
    authors: ["Y. Hu", "Y. Wang", "J. McAuley"]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2507.05257"
    arxiv_id: "2507.05257"
  - title: "JRE-L: Journalist, reader, and editor LLMs in the loop for science journalism for the general audience"
    authors: ["G. Jiang", "X. Shi", "Q. Luo"]
    year: 2025
    venue: "NAACL"
    doi: "10.18653/v1/2025.naacl-long.335"
    url: null
    arxiv_id: null
  - title: "Memory OS of AI Agent"
    authors: ["J. Kang", "M. Ji", "Z. Zhao", "T. Bai"]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2506.06326"
  - title: "Scaling laws for neural language models"
    authors: ["J. Kaplan", "S. McCandlish", "T. Henighan", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.08361"
  - title: "DialSim: A real-time simulator for evaluating long-term multi-party dialogue understanding of conversation systems"
    authors: ["J. Kim", "W. Chay", "H. Hwang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2406.13144"
    arxiv_id: "2406.13144"
  - title: "Derivation of new readability formulas (Flesch-Kincaid)"
    authors: ["J. P. Kincaid", "R. Fishburne", "R. Rogers", "B. Chissom"]
    year: 1975
    venue: "Naval Technical Training"
    doi: null
    url: null
    arxiv_id: null
  - title: "LexEval: A comprehensive Chinese legal benchmark for evaluating large language models"
    authors: ["H. Li", "Y. Chen", "Q. Ai", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "LLMs-as-judges: A comprehensive survey on LLM-based evaluation methods"
    authors: ["H. Li", "Q. Dong", "J. Chen", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2412.05579"
    arxiv_id: "2412.05579"
  - title: "Think-in-memory: Recalling and post-thinking enable LLMs with long-term memory"
    authors: ["L. Liu", "X. Yang", "Y. Shen", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2311.08719"
  - title: "Investigating users' search behavior and outcome with ChatGPT in learning-oriented search tasks"
    authors: ["S. Liu", "Y. Hu", "Z. Tian", "et al."]
    year: 2024
    venue: "SIGIR-AP"
    doi: "10.1145/3673791.3698406"
    url: null
    arxiv_id: null
  - title: "MemoChat: Tuning LLMs to use memos for consistent long-range open-domain conversation"
    authors: ["J. Lu", "S. An", "M. Lin", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2308.08239"
  - title: "Evaluating very long-term conversational memory of LLM agents (LoCoMo)"
    authors: ["A. Maharana", "D.-H. Lee", "S. Tulyakov", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2402.17753"
    arxiv_id: "2402.17753"
  - title: "Training language models to follow instructions with human feedback (InstructGPT)"
    authors: ["L. Ouyang", "J. Wu", "X. Jiang", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemGPT: Towards LLMs as operating systems"
    authors: ["C. Packer", "V. Fang", "S. Patil", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["J. S. Park", "J. O'Brien", "C. J. Cai", "et al."]
    year: 2023
    venue: "UIST"
    doi: null
    url: null
    arxiv_id: null
  - title: "HelloBench: Evaluating long text generation capabilities of large language models"
    authors: ["H. Que", "F. Duan", "L. He", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2409.16191"
    arxiv_id: "2409.16191"
  - title: "Cognitive memory in large language models"
    authors: ["L. Shan", "S. Luo", "Z. Zhu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2504.02441"
    arxiv_id: "2504.02441"
  - title: "Active feedback in ad hoc information retrieval"
    authors: ["X. Shen", "C. Zhai"]
    year: 2005
    venue: "SIGIR '05"
    doi: "10.1145/1076034.1076047"
    url: null
    arxiv_id: null
  - title: "Context-sensitive information retrieval using implicit feedback"
    authors: ["X. Shen", "B. Tan", "C. Zhai"]
    year: 2005
    venue: "SIGIR '05"
    doi: "10.1145/1076034.1076045"
    url: null
    arxiv_id: null
  - title: "Continual learning of large language models: A comprehensive survey"
    authors: ["H. Shi", "Z. Xu", "H. Wang", "et al."]
    year: 2024
    venue: "ACM Computing Surveys"
    doi: null
    url: null
    arxiv_id: null
  - title: "Continual learning of large language models: A comprehensive survey (ACM CSUR version)"
    authors: ["H. Shi", "Z. Xu", "H. Wang", "et al."]
    year: 2025
    venue: "ACM Comput. Surv."
    doi: "10.1145/3735633"
    url: null
    arxiv_id: null
  - title: "BlenderBot 3: A deployed conversational agent that continually learns to responsibly engage"
    authors: ["K. Shuster", "J. Xu", "M. Komeili", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2208.03188"
  - title: "JuDGE: Benchmarking judgment document generation for Chinese legal system"
    authors: ["W. Su", "B. Yue", "Q. Ai", "et al."]
    year: 2025
    venue: "SIGIR '25"
    doi: "10.1145/3726302.3730295"
    url: null
    arxiv_id: null
  - title: "MemBench: Towards more comprehensive evaluation on the memory of LLM-based agents"
    authors: ["H. Tan", "Z. Zhang", "C. Ma", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2506.21605"
  - title: "Episodic and declarative memory: role of the hippocampus"
    authors: ["E. Tulving", "H. J. Markowitsch"]
    year: 1998
    venue: "Hippocampus"
    doi: null
    url: null
    arxiv_id: null
  - title: "Incorporating vertical results into search click models"
    authors: ["C. Wang", "Y. Liu", "M. Zhang", "et al."]
    year: 2013
    venue: "SIGIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "A survey on LLM-based agents for social simulation: Taxonomy, evaluation and applications"
    authors: ["Z. Wang", "B. Xie", "B. Xu", "et al."]
    year: null
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "An in-depth investigation of user response simulation for conversational search"
    authors: ["Z. Wang", "Z. Xu", "V. Srikumar", "Q. Ai"]
    year: 2024
    venue: "WWW"
    doi: null
    url: null
    arxiv_id: null
  - title: "An implicit feedback approach for interactive information retrieval"
    authors: ["R. W. White", "J. M. Jose", "I. Ruthven"]
    year: 2006
    venue: "Information Processing & Management"
    doi: "10.1016/j.ipm.2004.08.010"
    url: null
    arxiv_id: null
  - title: "LongMemEval: Benchmarking chat assistants on long-term interactive memory"
    authors: ["D. Wu", "H. Wang", "W. Yu", "et al."]
    year: 2025
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "From human memory to AI memory: A survey on memory mechanisms in the era of LLMs"
    authors: ["Y. Wu", "S. Liang", "C. Zhang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2504.15965"
  - title: "WritingBench: A comprehensive benchmark for generative writing"
    authors: ["Y. Wu", "J. Mei", "M. Yan", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2503.05244"
  - title: "Inference scaling laws: An empirical analysis of compute-optimal inference for problem-solving with language models"
    authors: ["Y. Wu", "Z. Sun", "S. Li", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2408.00724"
  - title: "A-MEM: Agentic memory for LLM agents"
    authors: ["W. Xu", "K. Mei", "H. Gao", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2502.12110"
  - title: "Can LLMs identify critical limitations within scientific research? (LimitGen)"
    authors: ["Z. Xu", "Y. Zhao", "M. Patwardhan", "et al."]
    year: 2025
    venue: "ACL"
    doi: "10.18653/v1/2025.acl-long.1009"
    url: null
    arxiv_id: null
  - title: "LARP: Language-agent role play for open-world games"
    authors: ["M. Yan", "R. Li", "H. Zhang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2312.17653"
  - title: "Qwen3 technical report"
    authors: ["A. Yang", "A. Li", "B. Yang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2505.09388"
  - title: "A probabilistic inference scaling theory for LLM self-correction"
    authors: ["Z. Yang", "Y. Zhang", "Y. Wang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2508.16456"
    arxiv_id: "2508.16456"
  - title: "LLM-Evolve: Evaluation for LLM's evolving capability on benchmarks"
    authors: ["J. You", "M. Liu", "S. Prabhumoye", "et al."]
    year: 2024
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exploring human-like thinking in search simulations with large language models"
    authors: ["E. Zhang", "X. Wang", "P. Gong", "et al."]
    year: 2025
    venue: "SIGIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Chinese court simulation with LLM-based agent system"
    authors: ["K. Zhang", "J. Li", "Y. Wu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2508.17322"
    arxiv_id: "2508.17322"
  - title: "BERTScore: Evaluating text generation with BERT"
    authors: ["T. Zhang", "V. Kishore", "F. Wu", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1904.09675"
  - title: "Information retrieval evaluation as search simulation: A general formal framework"
    authors: ["Y. Zhang", "X. Liu", "C. Zhai"]
    year: 2017
    venue: "ICTIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Qwen3 embedding: Advancing text embedding and reranking through foundation models"
    authors: ["Y. Zhang", "M. Li", "D. Long", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2506.05176"
  - title: "MemSim: A Bayesian simulator for evaluating memory of LLM-based personal assistants"
    authors: ["Z. Zhang", "Q. Dai", "L. Chen", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2409.20163"
    arxiv_id: "2409.20163"
  - title: "A survey on the memory mechanism of large language model based agents"
    authors: ["Z. Zhang", "Q. Dai", "X. Bo", "et al."]
    year: 2025
    venue: "ACM Trans. Inf. Syst."
    doi: "10.1145/3748302"
    url: null
    arxiv_id: null
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["W. Zhong", "L. Guo", "Q. Gao", "et al."]
    year: 2024
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "The off-policy experimental results on MemoryBench with min-max normalization based metric score merge"
  page: 7
  image_path: "figures/ai-2026-memorybench-continual-learning-fig.png"
---

# MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems

**Authors:** Qingyao Ai, Yichen Tang, Changyue Wang, Jianming Long, Weihang Su, Yiqun Liu
**Published:** 2026-05 · [Source](https://arxiv.org/abs/2510.17281)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MemoryBench (Tsinghua THUIR, May 2026) is the first benchmark for LLM continual learning that includes **procedural memory** — i.e. logs of how the system did on previous tasks, not just declarative content. It assembles 11 public datasets (LoCoMo, DialSim x3, LexEval x3, JuDGE, IdeaBench, LimitGen-Syn, WritingPrompts, HelloBench x3, WritingBench x3, NF-Cats, SciTechNews — 20k cases) across 3 domains (Open/Legal/Academic), 2 languages (en/zh), and 4 input/output length combos (LiSo, SiLo, LiLo, SiSo), then uses a Qwen-3-32B "LLM-as-user-simulator" to produce verbal feedback plus probabilistic action signals (like/dislike/copy, calibrated to Shuster 2022 + Chatterji 2025 empirical rates — ~6.5% feedback rate, 86/14 like/dislike split). Human annotators couldn't reliably tell simulated feedback from real human feedback (Fleiss' kappa = 0.093 on naturalness, 50% win-rate). Result on Qwen-3-8B backbone: **none of the SOTA memory systems (A-Mem, Mem0, MemoryOS) consistently beats a vanilla BM25-S RAG that just dumps each dialog session into the index as one document**. MemoryOS adds 17-21s per case of memory-construction overhead with no win in quality; Mem0 hits pathological slowdown (>20 min/entry after ~600 entries on DialSim-theoffice, total failure after 12h). Existing methods were tuned on LoCoMo's reading-comprehension shape and silently treat every input as declarative — they have no machinery for procedural feedback. Most useful takeaway: if you're building agent memory now, the right baseline is BM25-over-sessions, not Mem0, and your real research question is "how does the system actually use a failure log."

## Key Takeaway

Throw away your fancy LLM-memory system — for almost every real task, dumping training-dialog feedback into a vanilla BM25 index beats the SOTA memory architectures (A-Mem, Mem0, MemoryOS), because those systems were tuned against reading-comprehension benchmarks (LoCoMo) and silently assume every memory is declarative, so they choke on procedural feedback logs. The lesson: complex memory machinery is only a win when its inductive bias matches the input shape, and right now nobody's inductive bias matches "logs of how I did last time."

## Implications

- **Rebench your memory stack against BM25-S, not against LoCoMo alone**: The single biggest finding here is that BM25 over per-session documents wins or ties across 6 of 7 task formats. If you've been quoting LoCoMo wins for A-Mem or Mem0, you've been overfitting to a reading-comprehension task type. Add at minimum: one writing dataset (WritingBench), one short-output classification (NF-Cats), and one verbal feedback log condition. ENGRAM dimensions: **R (Retrieve)** + **N (Network)**.
- **Separate declarative and procedural retrieval paths in your architecture**: The paper's core diagnosis is that A-Mem/Mem0/MemoryOS "simply treat all inputs as declarative memory" and develop mechanisms accordingly. If your write-path doesn't tag entries as `kind: procedural-feedback` vs `kind: declarative-fact` (your own ENGRAM-E and ENGRAM-A axes), you literally cannot do this differentiation at retrieve time. Add the discriminator at encode-time.
- **Budget for the latency tax of complex memory systems honestly**: MemoryOS averages 17-21 seconds of memory operation per case across all four task formats (vs. 0.03-0.55s for BM25 variants). Mem0 on long-input tasks (LiSo, LiLo) is fine at ~0.4s, but on SiLo/SiSo it climbs to 4 seconds, and on copy-feedback dialogs in the Legal domain its memorization time degrades catastrophically — eventually exceeding 20 min/entry. The 60-100x latency tax buys you ~0% accuracy gain. ENGRAM dimension: **M (Maintain)**.
- **Use the LLM-as-user-simulator pattern for your own evals**: The paper's human-evaluation table (kappa = 0.093 on naturalness, simulated feedback wins 50%/59.5%/59% on naturalness/relevance/overall vs. human feedback) is strong validation that a Qwen-3-32B with a structured profile-prompt + test-prompt + JSON-output spec is now indistinguishable from real users in pairwise annotation. You can build evaluation loops without recruiting users. The 4-element profile prompt (persona / domain expertise / evaluation criteria / behavioral constraints) is a copy-able recipe. ENGRAM dimension: **G (Ground)** — provenance of synthetic feedback.
- **Be skeptical of feedback that doesn't reach a verbal critique**: Action-only feedback (like/dislike/copy) is too noisy to drive learning on its own — the action-feedback experiments (Table 20) showed SFT on filtered "liked" first-turns barely moves the needle (0.4892 → 0.4892 average on Academic) and sometimes degrades performance. The verbal critique ("your analysis is generally clear but contains a key error in Article 51...") is where the signal lives. **Encode (E)** the verbal critique, not just the action.
- **Stop benchmarking on a single domain; performance is wildly domain-conditional**: On the Open domain Vanilla beats every memory system except Embed-S (0.6523 vs 0.6582). On Academic, BM25-S wins (0.7110). On Legal, BM25-M wins (0.5011). MemoryOS is 2nd-worst on Open and 2nd-best on SiLo. Your memory architecture has no universal ranking — your eval needs to look like an N-domain × M-task-format grid, not a single number. ENGRAM dimension: **R (Retrieve)** — query-task interaction.
- **The bottleneck is "what to do with a failure log," not "how to encode a fact"**: The paper's per-dataset feedback-effect table (Table 16) shows feedback gives huge gains on subjective writing tasks (WritingBench: +1.34 / +1.39 / +0.84 on three subsets out of 10), modest gains on legal generation (+0.02-0.04 F1), and negligible gains on retrieval QA. The whole field has been optimizing for the wrong shape of memory. The next architecture should be designed around procedural rather than declarative memory as the primary case. ENGRAM dimension: **A (Aggregate)**.
- **Re-read the BM25-S recipe carefully — it's the new dumb-baseline-that-wins**: BM25-S stores the **entire dialog session as a single document**, indexed by the question that generated it. Not per-message (BM25-M). Not per-summary. Not per-extracted-fact. Just: dump the whole session in. That this beats four years of careful memory-system engineering is the most actionable finding in the paper. Try it tomorrow on your stack.

## How to Apply It (method)

**Scenario:** You're building Flow OS's brain extraction layer (the `/learn` command and its v2 memory schema) and want to know whether to invest engineering effort in (a) a smarter memory backend like Mem0 or MemoryOS, (b) richer encoding strategies in `learn`, or (c) just QMD-over-sessions with BM25. You need a benchmark that mirrors your actual workload — multi-domain (ventures, content, contacts), multi-task (lookup, draft, decision), with realistic user feedback logs from Telegram + terminal sessions.

**Steps:**

1. **Carve your real workload into the LiSo / SiLo / LiLo / SiSo grid**: For each `/learn`-eligible session in the last 90 days, classify it: input length (long if >600 tokens of context like a transcript + paper, else short) and output length (long if a multi-paragraph synthesis, else short). MemoryBench's grid forces you to notice that "find Marcus Webb's call notes" (SiSo) and "draft a 6-paragraph follow-up email" (SiLo) live in different cells with different winning architectures.

2. **Build a domain partition**: Group your sessions by your actual ventures + activity types — e.g. `flow-os`, `cognitive-shift`, `askrally`, `personal`, `paper-digest`. Five domains × four task-format cells = 20 cells. Sample ~30 sessions per cell where you have them; this is your `MemoryBench-Personal` testbed.

3. **Implement the dual-path feedback simulator**:
   - **Path 1 (deterministic)** for tasks with verifiable ground truth — e.g. "did the digest match my hand-written notes on this paper?" Map similarity score (BERTScore F1 or ROUGE-L) → satisfaction 1-10.
   - **Path 2 (LLM-as-user)** for subjective tasks — drafts, decisions, captures. Build the profile prompt from the actual user (you):

   ```
   You are the user, a venture builder. You requested AI assistance
   on {task description}. Your evaluation criteria are: {criteria}.
   Always start your reasoning process first, then provide other
   feedback elements. Do not repeat questions already asked.

   Your response should include:
   1. Reasoning: Detailed analysis of the assistant's response quality
   2. Behavior decision: Whether to continue or end the conversation
   3. Response: What you would say next (only if continuing)

   Respond in this strict JSON format:
   { "reasoning": "...", "behavior": "continue_conversation | end_conversation", "response": "..." }
   ```

4. **Wire in the probabilistic action model**: Use the paper's sigmoid model (Eqs 1-2, Table 5) with target P(L) ≈ 0.0559, P(D) ≈ 0.0091, S0L = 7.5, S0D = 4.5, kL = kD = 1.5. For long-output tasks, P(copy) = 4 · P(like). This gives you a per-message synthetic action stream that mirrors real telegraph-button rates.

5. **Run four memory backends against the testbed in off-policy mode**:
   - **Vanilla** — current `qmd query` only, no learn-extracted memories at all
   - **BM25-S** — `qmd search` with BM25 over per-session log dumps (the surprise winner)
   - **Current v2** — existing `/learn` extraction pipeline writing atomic memory files
   - **One ambitious upgrade** — e.g. a graph-augmented retrieval, or Mem0's ADD/UPDATE/DELETE/NOOP planner

   For each, replay 8 weeks of training-set sessions, then evaluate on the test set. Use min-max normalization per metric per dataset before aggregating across cells.

6. **Plot the radar (Figure 3 in this paper)**: One spoke per cell, one colored bar per backend. The pattern you're looking for is: where does v2 beat BM25-S? Where does it lose? Where does the ambitious upgrade win, and is the win worth the 17-second-per-case latency tax?

7. **Run the time-consumption analysis separately**: Memory time + predict time per cell per backend, log-scale. This is where MemoryBench buries the lede — MemoryOS's 17s memory tax was the actual reason to deprecate it.

8. **Decide architecturally**: If v2 doesn't beat BM25-S on more than half the cells AND its latency is higher, **the engineering effort should go into the encoding pipeline (what gets extracted, how it's tagged), not into a more elaborate retrieve/aggregate backend**.

**Expected outcome:** A 20-cell decision matrix that tells you, per (domain × task-format) combination, which memory backend is actually best for Flow OS — plus a calibrated synthetic-user simulator you can keep running against future architecture changes without recruiting yourself for evaluation every time. The most likely outcome: you discover BM25-over-sessions is a near-Pareto-optimal baseline, and the gains from elaborate extraction are concentrated in 2-3 specific cells (likely Academic-SiLo for paper digests, Open-LiLo for content drafts). That tells you exactly where to put the next month of engineering.

## Best Figure

![Figure 3 — The off-policy experimental results on MemoryBench with min-max normalization based metric score merge (page 7)](figures/ai-2026-memorybench-continual-learning-fig.png)

**Image Candidates:**
- Figure 3 (p. 7): Radial plot showing 8 LLMsys (4 RAG variants, A-Mem, Mem0, MemoryOS, Vanilla) across 7 partitions (3 domains + 4 task formats); the visual punchline is that the colored bars are tangled — no clear winner.
- Figure 4 (p. 7): Bar chart of memory-time + predict-time per cell; MemoryOS's 17-21s memory tax is visually overwhelming and tells the latency story.
- Table 1 (p. 3): Benchmark-categorization table showing MemoryBench is the only entry with checkmarks across Declarative + Procedural + Verbal + Action feedback columns.

**Best Image:** Figure 3 — *"The off-policy experimental results on MemoryBench with min-max normalization based metric score merge."*

**Slide Caption:** Across 3 domains × 4 task formats, no SOTA memory system (A-Mem, Mem0, MemoryOS) consistently beats vanilla BM25 over per-session dumps.

**Description:** Figure 3 is a radial bar chart with one spoke per evaluation partition (Open / Academic / Legal domains + LiSo / SiLo / LiLo / SiSo task formats). Each spoke holds 8 colored bars — one per LLMsys baseline. The visual story is the tangle: pink Vanilla, blue Embed-S, and beige BM25-S consistently sit at or near the top across spokes, while green MemoryOS, pink Mem0, and orange Embed-M are mostly at the bottom. The "fancy memory" systems (A-Mem in light blue, Mem0 in pink, MemoryOS in green) cluster mid-pack at best — and Mem0 is missing entirely from Open + LiSo because its context-handling failed to process those partitions in reasonable time. This single image is the paper's core empirical claim: complex memory architectures aren't winning on diverse-task continual learning, and a thoughtful BM25 baseline is the new starting point.

## What Experts Overlook

The thing everyone misses in this paper is the **dual-path satisfaction-to-action probability model in §A.2.3** (and its calibration to Shuster 2022 + Chatterji 2025 empirical rates). Most readers will look at the headline result ("Mem0 is no better than BM25") and skip the appendix, but the appendix is where the methodological contribution actually lives. The model has three variants — a sigmoid for LLM-scored datasets, a binary mapping for DialSim, and a separately-calibrated sigmoid for LoCoMo's F1-based scoring — all targeting the **same global P(like) ≈ 0.0559 and P(dislike) ≈ 0.0091** so that comparisons across datasets stay coherent. Table 4 reveals the LLM-as-user simulator gives scores 7-9 about 90% of the time, and the sigmoid's S0L = 7.5 / S0D = 4.5 hyperparameter choice is what concentrates likes on the 8-10 band and dislikes below 5.

**Why it matters:** Without this calibration discipline, "feedback" in a benchmark becomes whatever feedback density the LLM-judge produces by accident — which is rarely 6.5%, and which would make any system look like it's learning brilliantly from a constant stream of "great job!" The MemoryBench team explicitly factored out this bias so that **the benchmark measures the memory system, not the simulator's enthusiasm**. This is the difference between a benchmark and a vanity-metric generator. The same trick is what you'd want for any /learn-style memory eval: separate the satisfaction score (LLM judgment, possibly biased high) from the action probability (calibrated to known empirical rates), and tune the sigmoid hyperparameters until your simulated user looks like a real user, not a sycophant.

**Example of good use:** When building Flow OS's automatic-extraction evaluation, instead of asking "did Claude approve this memory write?" (which will say yes 95% of the time), use a two-stage model: (1) Claude scores the memory quality 1-10, (2) a calibrated sigmoid maps that score to a probabilistic "should-keep" decision with global keep-rate matching the user's real keep-rates (e.g. 30% of /learn captures pass review, which means S0L should be tuned so P(keep|S=7) ≈ 0.5). Now your eval has correctly-shaped behavior and you can actually compare architectures.

**Example of misapplication:** A team builds their memory-system eval, runs an LLM-as-judge to produce 1-10 scores, then directly thresholds at 7+ as "like" — and finds that 70% of simulated user messages have "like" actions. They then train a system on this signal and it looks brilliant. In production, the real action rate is 6.5%, the sparsity is 10x worse, the learned weights are catastrophically miscalibrated, and the system either over-rewards or under-rewards every user interaction. The system silently degrades because the eval told them everything was fine. This is the failure mode the paper's calibration trick prevents.

## Extracted Prompts

**Prompt explanation:** Overall profile prompt — defines the simulated user's persona, domain expertise, evaluation criteria, and behavioral constraints for the LLM-as-User-Simulator (general template, Prompt A.2.4.1).

```
{user persona}

{domain expertise}

CRITICAL: Always focus on the initial prompt/request as the primary context for evaluation. The conversation should stay aligned with the original user intent.

IMPORTANT: DO NOT REPEAT QUESTIONS OR REQUESTS that have already been asked in the conversation. Avoid asking the same question multiple times.

IMPORTANT: Always start your reasoning process first, then provide the other feedback elements.

Your response should include:
1. Reasoning: Detailed analysis of the assistant's response quality and accuracy (always consider how well it addresses the initial prompt)
2. Behavior decision: Whether to continue or end the conversation
3. Response: What the user would say (only if continuing the conversation)

Consider factors like: {evaluation criteria}

{additional context}
```

**Prompt explanation:** Overall test prompt — provides per-turn context for the simulator to predict the next user response (Prompt A.2.4.2).

```
Analyze this conversation and predict the user's response:

The user is {task description}. CRITICAL: Focus on the initial request as the core topic that should be the primary focus throughout this entire conversation. All responses should be evaluated based on how well they address this original user intent.

Conversation History: {conversation history}

EVALUATION CONTEXT: {evaluation context}

IMPORTANT: If you provide a response (when behavior is continue_conversation), it must be in {language}.

Please provide a realistic user response in strict JSON format:
{
   "reasoning": "Detailed analysis of the assistant's response quality and accuracy (MUST evaluate how well it addresses the initial request)",
   "behavior": "continue_conversation" — "end_conversation",
   "response": "What the user would say next (string or null if ending)"
}

Requirements:
- reasoning: Always provide detailed analysis first. CRITICAL: Always assess how well the assistant's response addresses the initial request and stays focused on the original user intent.
- behavior: Must be exactly: continue_conversation or end_conversation.
- response: Text if continuing, null if ending conversation. Must match the conversation language.

IMPORTANT: Do not repeat questions or requests that have already been made in the conversation.

Respond with valid JSON only.
```

**Prompt explanation:** Satisfaction scoring system prompt — used by the SatisfactionScorer module to produce a 1-10 numerical satisfaction score from the LLM-judge (Prompt A.2.4.3).

```
You are an expert evaluator tasked with scoring assistant responses against specific quality standards.

SCORING SCALE (1-10):
1-2: Completely inadequate - Wrong, irrelevant, or harmful
3-4: Unsatisfactory - Major errors, misses key points, or unhelpful
5-6: Below expectations - Addresses basics but has significant gaps, inaccuracies, or omissions
7-8: Meets expectations - Solid response with minor issues or missing elements
9-10: Exceeds expectations - Comprehensive, accurate, and fully satisfies all requirements

EVALUATION APPROACH:
- Use the provided evaluation context and ground truth as your primary standards
- Score against what the response should contain, not just what it does contain
- Consider both correctness and completeness

Provide only a numerical score from 1-10.
```

**Prompt explanation:** Satisfaction scoring user prompt — paired with the system prompt above to produce the score (Prompt A.2.4.4).

```
Evaluate the assistant's response by comparing it against the provided standards and ground truth:

FULL CONVERSATION: {conversation history}

EVALUATION CONTEXT (contains ground truth and quality criteria): {evaluation context}

EVALUATION TASK: Compare the assistant's final response against the evaluation context above. The evaluation context contains the ground truth and quality standards that define what a good response should include.

Respond in this JSON format:
{
  "score": <integer from 1-10>
}
```

**Prompt explanation:** DialSim prompt template for memory-aware evaluation — the official DialSim prompt with the dialogue-history section stripped out so that each memory backend has to retrieve it from its own memory.

```
You are { Chatbot }, a long-term conversation agent capable of interacting with multiple users.

Based on the [Dialog History] provided, please answer the given [Question].

Note the following points:
1. Your responses should solely rely on the retrieved dialog history. If the information in the dialog history is insufficient to answer the question, you must admit that you don't know the answer.
2. This question is being asked in the context of { Date }.

[Question] { Question }

[Answer]
```

**Prompt explanation:** Generic answering prompt template fed to all baselines after memory retrieval (English).

```
User Memories:
{memories str}

User input:
{query}

Based on the memories provided, respond naturally and appropriately to the user's input above.
```

**Prompt explanation:** NF-Cats evaluation prompt template — used as the LLM-as-judge scoring rubric for non-factoid QA, recommended by NTCIR-18.

```
###Task: Evaluate the answer of a given question. Directly output an integer between 1 and 5 to indicate the score of this answer:
- 1 means the answer is irrelevant to the question,
- 2 means the answer is related to the question, but does not solve the question,
- 3 means the answer only solves a part of the question,
- 4 means the answer solve majority aspects of the question, but not perfect,
- 5 means the answer is perfect to solve the question

###Question: { Question }

###Answer: { Output }

###Score of the answer:
```

**Prompt explanation:** Metric integration prompt for JuDGE — merges 12+ legal-document evaluation metrics (penalty accuracy, conviction accuracy, referencing accuracy, reasoning METEOR/BERTScore, judge METEOR/BERTScore) into a single 1-10 score via LLM-as-judge.

```
You are an expert legal AI assistant. Your task is to evaluate the quality of an automatically generated legal judgment document based on the provided context and a set of pre-calculated metrics.

## Case Factual Description (Input)
{INPUT FACTS}

## Generated Judgment Document (Output)
{GENERATED JUDGMENT}

## Ground Truth Judgment Document (Reference)
{GOLDEN JUDGMENT}

## Evaluation Metrics
Below are the calculated metrics comparing the 'Generated Judgment' to the 'Ground Truth'. A score of 1.00 indicates a perfect match for that specific metric, while 0.00 indicates a complete mismatch.

1. Penalty Accuracy (Scores range from 0.00 to 1.00)
time_score: {time_score}
amount_score: {amount_score}

2. Convicting Accuracy (Scores range from 0.00 to 1.00)
crime_recall: {crime_recall}
crime_precision: {crime_precision}

3. Referencing Accuracy (Scores range from 0.00 to 1.00)
penalcode_index_recall: {penalcode_index_recall}
penalcode_index_precision: {penalcode_index_precision}
reasoning_meteor: {reasoning_meteor}
reasoning_bert_score: {reasoning_bert_score}
judge_meteor: {judge_meteor}
judge_bert_score: {judge_bert_score}

## Task
Based on a holistic review of the input, output, ground truth, and all the metrics provided above, provide a single integer score from 1 to 10 to represent the overall quality of the generated judgment document.
- 1: Represents extremely poor quality (e.g., completely irrelevant, factually incorrect, nonsensical).
- 10: Represents excellent quality (e.g., legally sound, factually accurate, well-reasoned, and structurally perfect, nearly indistinguishable from the ground truth).
Your response should be only a single integer.

## Final Score
```

**Prompt explanation:** SciTechNews profile prompt — domain-specialized variant of the profile prompt for science-journalism evaluation.

```
You are simulating a science journalist or editor who requested AI assistance to write journalistic reports of scientific papers for general audiences.

You have expertise in science journalism across diverse fields including computer science, cybersecurity, privacy research, mobile computing, cloud services, encryption technologies, biomedical research, environmental science, and other technical domains. You understand what makes scientific writing accessible to the general public while maintaining accuracy.

CRITICAL: Always focus on the initial prompt/request as the primary context for evaluation. The conversation should stay aligned with the original user intent.

IMPORTANT: DO NOT REPEAT QUESTIONS OR REQUESTS that have already been asked in the conversation. Avoid asking the same question multiple times.

IMPORTANT: Always start your reasoning process first, then provide the other feedback elements.

Your response should include:
1. Reasoning: Detailed analysis of the assistant's response quality and accuracy
2. Behavior decision: Whether to continue or end the conversation
3. Response: What the user would say (only if continuing the conversation)

Consider factors like:
- Accessible and readable for general audiences without technical background
- Accurate to the original scientific work without oversimplification
- Engaging and newsworthy in its presentation style
- Well-structured with appropriate journalistic elements (headlines, lead paragraphs, context)
- Properly balancing technical detail with readability
- Readability for lay audiences
- Journalistic style and structure
- Engagement factor and clarity of technical concepts

Your evaluation focuses on the journalistic transformation of academic content rather than the underlying research quality.
```

## Citations

The paper has 65 references in its bibliography. The full structured list is in the frontmatter `citations:` field. Top 10 most relevant to the memory-architect lens:

- **A-MEM** (Xu et al., 2025) — agentic memory system with dynamic memory linking, evaluated as a baseline and lost to BM25-S in most cells
- **Mem0** (Chhikara et al., 2025) — production-ready agent memory with ADD/UPDATE/DELETE/NOOP planner; suffered pathological slowdown
- **MemoryOS** (Kang et al., 2025) — hierarchical short/mid/long-term memory inspired by OS paging; 17-21s/case memory tax
- **LoCoMo** (Maharana et al., 2024) — the LongConvMemory benchmark that most prior memory systems were tuned against
- **MemGPT** (Packer et al., 2023) — the original "LLM as operating system" framing
- **MemoryBank** (Zhong et al., 2024) — writing/summarizing/updating/deleting/retrieval primitives
- **Think-in-memory** (Liu et al., 2023) — recall + post-thinking for long-term memory
- **MemoChat** (Lu et al., 2023) — tuning LLMs to use memos for long-range conversation
- **From human memory to AI memory** (Wu et al., 2025) — survey of memory mechanisms in the LLM era
- **A survey on the memory mechanism of LLM-based agents** (Zhang et al., 2025) — ACM TOIS taxonomy paper

## Related Digests

- [[xu-2025-a-mem-agentic-memory]] — A-MEM: Agentic Memory for LLM Agents (one of the three SOTA baselines MemoryBench tests and beats with BM25-S)
- [[chhikara-2025-mem0]] — Mem0: Building Production-ready AI Agents with Scalable Long-term Memory (the second SOTA baseline that hits pathological slowdown on DialSim-theoffice)
- [[kang-2025-memory-os]] — Memory OS of AI Agent (the third SOTA baseline whose 17-21s memory tax buys ~0% accuracy gain)
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20 (cites MemoryBench in its references; complementary write-time-vs-query-time framing)
- [[wu-2026-lme-v2]] — LongMemEval-V2 (the other 2026 procedural-feedback benchmark; direct neighbor in the bench-the-bench space)
- [[du-2025-rethinking-memory]] — Rethinking Memory in LLM-based Agents (the operations/representations taxonomy that MemoryBench's procedural-vs-declarative split refines)

## Reviewer Notes

Hallucination check performed inline against the paper text.

**Overall severity:** Clean

All numerical claims (sigmoid hyperparameters S0L = 7.5, S0D = 4.5, kL = kD = 1.5; target P(L) ≈ 0.0559, P(D) ≈ 0.0091; 6.5% feedback rate with 86/14 like-dislike split; MemoryOS memory time exceeding 17s; Mem0 >20 min/entry pathological slowdown; Fleiss' kappa = 0.093 on naturalness; simulated feedback win rates of 50.0%/59.5%/59.0%; 20k cases across 11 datasets) were verified against the paper text (§A.2.3, §A.2.5, §A.3.8, Figure 4, Table 4, Table 7, Table 19). Per-method scores cited in implications (Vanilla 0.6523, Embed-S 0.6582, BM25-M Legal 0.5011, etc.) match Table 10 exactly. Feedback-gain numbers in Table 16 (WritingBench A.E. +1.34, C.D. +1.39, P.L. +0.84) verified. The lens-tagged ENGRAM-dimension annotations are interpretive overlays, not paper claims, and are presented as such. The phrase "complex memory machinery is only a win when its inductive bias matches the input shape" is a synthesis claim consistent with the paper's discussion in §3.3 and §A.3.9 but not a direct quote. No fabricated metrics, no invented experiments. Best figure (Figure 3, page 7) correctly identified and cropped.
