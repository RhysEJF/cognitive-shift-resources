---
corpus: agentic-memory
kind: paper-digest
slug: tavakoli-2026-beam-light
title: "Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs"
authors:
  - "Tavakoli, Mohammad"
  - "Salemi, Alireza"
  - "Ye, Carrie"
  - "Abdalla, Mohamed"
  - "Zamani, Hamed"
  - "Mitchell, J. Ross"
year: 2026
publication_date: "2026-02"
venue: "ICLR 2026"
source_url: "https://arxiv.org/abs/2510.27246"
doi: null
arxiv_id: "2510.27246"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Even 1M-token long-context LLMs and naive RAG collapse on multi-hop, contradiction, and event-ordering questions as conversations grow past 100K tokens; a cognitively-inspired three-tier memory (episodic vector index + scratchpad of distilled facts + recent-turn working memory + LLM noise filter) consistently rescues them, with the gain growing from +3.5–12.7 percentage points on average to +107–156% at 10M-token contexts where no baseline natively fits the input."
topics:
  - long-term-memory
  - long-context-llms
  - conversational-memory
  - episodic-memory
  - scratchpad-memory
  - rag-augmentation
  - benchmark-construction
  - synthetic-dialogue-generation
  - memory-ablation
  - human-cognition-inspired-memory
tags:
  - paper
  - benchmark
  - memory-system
  - long-context
  - rag
  - cognitive-inspired
  - iclr-2026
entities:
  - tavakoli-mohammad
  - salemi-alireza
  - zamani-hamed
  - mitchell-j-ross
  - university-of-alberta
  - umass-amherst
related_digests:
  - latimer-2025-hindsight-memory
  - chhikara-2025-mem0
  - packer-2023-memgpt-os
  - adler-2026-storage-not-memory
citations:
  - title: "GPT-4 Technical Report"
    authors: ["Josh Achiam", "Steven Adler", "Sandhini Agarwal", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2303.08774"
    arxiv_id: "2303.08774"
  - title: "Llama 3.3 — model cards and prompt formats"
    authors: ["Meta AI"]
    year: 2024
    venue: "Meta"
    doi: null
    url: "https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3/"
    arxiv_id: null
  - title: "Claude 3 model card"
    authors: ["Anthropic"]
    year: 2024
    venue: "Anthropic Technical Report"
    doi: null
    url: "https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf"
    arxiv_id: null
  - title: "Claude 4 model card (Claude Opus 4 & Sonnet 4)"
    authors: ["Anthropic"]
    year: 2025
    venue: "Anthropic Technical Report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Longformer: The Long-Document Transformer"
    authors: ["Iz Beltagy", "Matthew E. Peters", "Arman Cohan"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.05150"
  - title: "The neurobiology of semantic memory"
    authors: ["Jeffrey R. Binder", "Rutvik H. Desai"]
    year: 2011
    venue: "Trends in Cognitive Sciences"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving language models by retrieving from trillions of tokens (RETRO)"
    authors: ["Sebastian Borgeaud", "Arthur Mensch", "Jordan Hoffmann", "et al."]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language Models are Few-Shot Learners (GPT-3)"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Broaden Your SCOPE! Efficient Multi-Turn Conversation Planning for LLMs with Semantic Space"
    authors: ["Zhiliang Chen", "Xinyuan Niu", "Chuan-Sheng Foo", "et al."]
    year: 2025
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=3cgMU3TyyE"
    arxiv_id: null
  - title: "Adapting Language Models to Compress Contexts (AutoCompressor)"
    authors: ["Alexis Chevalier", "Alexander Wettig", "Anirudh Ajith", "Danqi Chen"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2305.14788"
  - title: "Rethinking Attention with Performers"
    authors: ["Krzysztof Choromanski", "Valerii Likhosherstov", "David Dohan", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2009.14794"
  - title: "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context"
    authors: ["Zihang Dai", "Zhilin Yang", "Yiming Yang", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1901.02860"
  - title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
    authors: ["Tri Dao", "Dan Fu", "Stefano Ermon", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Gemini 2.0 Flash: A Multimodal Model with 1 Million Token Context Window"
    authors: ["Google DeepMind"]
    year: 2025
    venue: "Google"
    doi: null
    url: "https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash"
    arxiv_id: null
  - title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "Kristina Toutanova"]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens"
    authors: ["Yiran Ding", "Li Lyna Zhang", "Chengruidong Zhang", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2402.13753"
  - title: "The FAISS Library"
    authors: ["Matthijs Douze", "Alexandr Guzhva", "Chengqi Deng", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2401.08281"
  - title: "PerLTQA: A Personal Long-Term Memory Dataset for Memory Classification, Retrieval, and Fusion in Question Answering"
    authors: ["Yiming Du", "Hongru Wang", "Zhengyi Zhao", "et al."]
    year: 2024
    venue: "SIGHAN"
    doi: null
    url: null
    arxiv_id: null
  - title: "RMT: Retentive Networks Meet Vision Transformers"
    authors: ["Qihang Fan", "Huaibo Huang", "Mingrui Chen", "et al."]
    year: 2024
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Large Language Models for Code Analysis: Do LLMs Really Do Their Job?"
    authors: ["Chongzhou Fang", "Ning Miao", "Shaurya Srivastav", "et al."]
    year: 2024
    venue: "USENIX Security"
    doi: null
    url: null
    arxiv_id: null
  - title: "SPLADE v2: Sparse Lexical and Expansion Model for Information Retrieval"
    authors: ["Thibault Formal", "Carlos Lassance", "Benjamin Piwowarski", "Stéphane Clinchant"]
    year: 2022
    venue: "SIGIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
    authors: ["Albert Gu", "Tri Dao"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2312.00752"
  - title: "Retrieval Augmented Language Model Pre-Training (REALM)"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "The Curious Case of Neural Text Degeneration"
    authors: ["Ari Holtzman", "Jan Buys", "Li Du", "et al."]
    year: 2020
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=rygGQyrFvH"
    arxiv_id: null
  - title: "Large Language Models (LLMs) for Source Code Analysis: Applications, Models and Datasets"
    authors: ["Hamed Jelodar", "Mohammad Meymani", "Roozbeh Razavi-Far"]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2503.17502"
    arxiv_id: "2503.17502"
  - title: "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models"
    authors: ["Bernal Jimenez Gutierrez", "Yiheng Shu", "Yu Gu", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Why Language Models Hallucinate"
    authors: ["Adam Tauman Kalai", "Ofir Nachum", "Santosh S. Vempala", "Edwin Zhang"]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2509.04664"
  - title: "The Treatment of Ties in Ranking Problems"
    authors: ["Maurice G. Kendall"]
    year: 1945
    venue: "Biometrika"
    doi: null
    url: null
    arxiv_id: null
  - title: "DialSim: A Real-Time Simulator for Evaluating Long-Term Dialogue Understanding of Conversational Agents"
    authors: ["Jiho Kim", "Woosog Chay", "Hyeonji Hwang", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2406"
  - title: "Retrieval-Enhanced Machine Learning: Synthesis and Opportunities"
    authors: ["To Eun Kim", "Alireza Salemi", "Andrew Drozdov", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2407.12982"
    arxiv_id: "2407.12982"
  - title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
    authors: ["Woosuk Kwon", "Zhuohan Li", "Siyuan Zhuang", "et al."]
    year: 2023
    venue: "SOSP"
    doi: null
    url: null
    arxiv_id: null
  - title: "LLMs Get Lost in Multi-Turn Conversation"
    authors: ["Philippe Laban", "Hiroaki Hayashi", "Yingbo Zhou", "Jennifer Neville"]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2505.06120"
    arxiv_id: "2505.06120"
  - title: "A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts"
    authors: ["Kuang-Huei Lee", "Xinyun Chen", "Hiroki Furuta", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2402.09727"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "A Survey of Long-Document Retrieval in the PLM and LLM Era"
    authors: ["Minghan Li", "Miyang Luo", "Tianrui Lv", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2509.07759"
    arxiv_id: "2509.07759"
  - title: "SnapKV: LLM Knows What You Are Looking For Before Generation"
    authors: ["Yuhong Li", "Yingbing Huang", "Bowen Yang", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Ring Attention with Blockwise Transformers for Near-Infinite Context"
    authors: ["Hao Liu", "Matei Zaharia", "Pieter Abbeel"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.01889"
  - title: "Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2402.17753"
  - title: "The Llama 4 Herd: The Beginning of a New Era of Natively Multimodal AI Innovation"
    authors: ["Meta-AI"]
    year: 2025
    venue: "Meta AI Blog"
    doi: null
    url: "https://ai.meta.com/blog/llama-4-multimodal-intelligence/"
    arxiv_id: null
  - title: "LLMs for Legal Reasoning: A Unified Framework and Future Perspectives"
    authors: ["Ha Thanh Nguyen", "Wachara Fungwacharakorn", "May Myo Zin", "et al."]
    year: 2025
    venue: "Computer Law & Security Review"
    doi: "10.1016/j.clsr.2025.106165"
    url: "https://www.sciencedirect.com/science/article/pii/S2212473X25000380"
    arxiv_id: null
  - title: "BAAI/bge-small-en-v1.5"
    authors: ["Beijing Academy of Artificial Intelligence"]
    year: 2023
    venue: "Hugging Face model"
    doi: null
    url: "https://huggingface.co/BAAI/bge-small-en-v1.5"
    arxiv_id: null
  - title: "Introducing GPT-4.1 in the API"
    authors: ["OpenAI"]
    year: 2025
    venue: "OpenAI"
    doi: null
    url: "https://openai.com/index/gpt-4-1/"
    arxiv_id: null
  - title: "GPT-4.1-mini Model Card"
    authors: ["OpenAI"]
    year: 2025
    venue: "OpenAI"
    doi: null
    url: "https://platform.openai.com/docs/models#gpt-4-1-mini"
    arxiv_id: null
  - title: "RWKV: Reinventing RNNs for the Transformer Era"
    authors: ["Bo Peng", "Eric Alcaide", "Quentin Anthony", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2305.13048"
  - title: "YaRN: Efficient Context Window Extension of Large Language Models"
    authors: ["Bowen Peng", "Jeffrey Quesnelle", "Honglu Fan", "Enrico Shippole"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.00071"
  - title: "Hyena Hierarchy: Towards Larger Convolutional Language Models"
    authors: ["Michael Poli", "Stefano Massaroli", "Eric Nguyen", "et al."]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Initial Nugget Evaluation Results for the TREC 2024 RAG Track with the AutoNuggetizer Framework"
    authors: ["Ronak Pradeep", "Nandan Thakur", "Shivani Upadhyay", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2411.09607"
  - title: "The Great Nugget Recall: Automating Fact Extraction and RAG Evaluation with Large Language Models"
    authors: ["Ronak Pradeep", "Nandan Thakur", "Shivani Upadhyay", "et al."]
    year: 2025
    venue: "SIGIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation (ALiBi)"
    authors: ["Ofir Press", "Noah A. Smith", "Mike Lewis"]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2108.12409"
  - title: "Improving Language Understanding by Generative Pre-Training (GPT-1)"
    authors: ["Alec Radford", "Karthik Narasimhan", "Tim Salimans", "Ilya Sutskever"]
    year: 2018
    venue: "OpenAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language Models Are Unsupervised Multitask Learners (GPT-2)"
    authors: ["Alec Radford", "Jeffrey Wu", "Rewon Child", "et al."]
    year: 2019
    venue: "OpenAI Blog"
    doi: null
    url: null
    arxiv_id: null
  - title: "Compressive Transformers for Long-Range Sequence Modelling"
    authors: ["Jack W. Rae", "Anna Potapenko", "Siddhant M. Jayakumar", "Timothy P. Lillicrap"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.05507"
  - title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5)"
    authors: ["Colin Raffel", "Noam Shazeer", "Adam Roberts", "et al."]
    year: 2020
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "From Tools to Teammates: Evaluating LLMs in Multi-Session Coding Interactions (MemoryCode)"
    authors: ["Nathanaël Carraz Rakotonirina", "Mohammed Hamdy", "Jon Ander Campos", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2502.13791"
  - title: "Understanding LLM Scientific Reasoning Through Promptings and Model's Explanation on the Answers"
    authors: ["Alice Rueda", "Mohammed S. Hassan", "Argyrios Perivolaris", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2505.01482"
    arxiv_id: "2505.01482"
  - title: "Learning to Rank for Multiple Retrieval-Augmented Models Through Iterative Utility Maximization"
    authors: ["Alireza Salemi", "Hamed Zamani"]
    year: 2025
    venue: "ICTIR"
    doi: "10.1145/3731120.3744584"
    url: "https://doi.org/10.1145/3731120.3744584"
    arxiv_id: null
  - title: "Plan-and-Refine: Diverse and Comprehensive Retrieval-Augmented Generation"
    authors: ["Alireza Salemi", "Chris Samarinas", "Hamed Zamani"]
    year: 2025
    venue: "preprint"
    doi: null
    url: "https://arxiv.org/abs/2504.07794"
    arxiv_id: "2504.07794"
  - title: "Cognitive Neuroscience Perspective on Memory: Overview and Summary"
    authors: ["Sruthi Sridhar", "Abdulrahman Khamaj", "Manish Kumar Asthana"]
    year: 2023
    venue: "Frontiers in Human Neuroscience"
    doi: null
    url: null
    arxiv_id: null
  - title: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
    authors: ["Jianlin Su", "Murtadha Ahmed", "Yu Lu", "et al."]
    year: 2024
    venue: "Neurocomputing"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents"
    authors: ["Haoran Tan", "Zeyu Zhang", "Chen Ma", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2506.21605"
  - title: "Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens of Context"
    authors: ["Gemini Team", "Petko Georgiev", "Ving Ian Lei", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2403.05530"
  - title: "Qwen2.5: A Party of Foundation Models"
    authors: ["Qwen Team"]
    year: 2024
    venue: "Qwen"
    doi: null
    url: "https://qwenlm.github.io/blog/qwen2.5/"
    arxiv_id: null
  - title: "The Hippocampal Memory Indexing Theory"
    authors: ["Timothy J. Teyler", "Pascal DiScenna"]
    year: 1986
    venue: "Behavioral Neuroscience"
    doi: null
    url: null
    arxiv_id: null
  - title: "Linformer: Self-Attention with Linear Complexity"
    authors: ["Sinong Wang", "Belinda Z. Li", "Madian Khabsa", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2006.04768"
  - title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2410.10813"
  - title: "Memformer: A Memory-Augmented Transformer for Sequence Modeling"
    authors: ["Qingyang Wu", "Zhenzhong Lan", "Kun Qian", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2010.06891"
  - title: "C-Pack: Packaged Resources to Advance General Chinese Embedding"
    authors: ["Shitao Xiao", "Zheng Liu", "Peitian Zhang", "Niklas Muennighoff"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Effective Long-Context Scaling of Foundation Models"
    authors: ["Wenhan Xiong", "Jingyu Liu", "Igor Molybog", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.16039"
  - title: "Beyond Goldfish Memory: Long-Term Open-Domain Conversation (MSC)"
    authors: ["Jing Xu", "Arthur Szlam", "Jason Weston"]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2107.07567"
  - title: "Long Time No See! Open-Domain Conversation with Long-Term Persona Memory (DuLeMon)"
    authors: ["Xinchao Xu", "Zhibin Gou", "Wenquan Wu", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2203.05797"
  - title: "Big Bird: Transformers for Longer Sequences"
    authors: ["Manzil Zaheer", "Guru Guruganesh", "Kumar Avinava Dubey", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models"
    authors: ["Zhenyu Zhang", "Ying Sheng", "Tianyi Zhou", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemoryBank: Enhancing Large Language Models with Long-Term Memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "et al."]
    year: 2024
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Overview of the LIGHT framework — episodic retrieval + scratchpad + working memory buffer"
  page: 6
  image_path: "figures/tavakoli-2026-beam-light-fig.png"
---

# Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs

**Authors:** Mohammad Tavakoli, Alireza Salemi, Carrie Ye, Mohamed Abdalla, Hamed Zamani, J. Ross Mitchell (University of Alberta / UMass Amherst)
**Published:** 2026-02 (ICLR 2026) · [Source](https://arxiv.org/abs/2510.27246)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

The authors build BEAM, a benchmark of 100 synthetic single-user conversations ranging 100K to 10M tokens (sourced across 19 domains: coding, math, finance, health, therapy, trip planning, etc.) and 2,000 human-validated probing questions across 10 memory abilities — adding three never-before-evaluated dimensions (Contradiction Resolution, Event Ordering, Instruction Following) to the seven inherited from prior benchmarks. Conversations are generated via a 5-stage pipeline that builds a plan from an MBTI-grounded user profile + relationship graph + timeline, expands it into user turns (LLaMA-3.3 70B), then bi-directional assistant turns (GPT-4.1) with question-detection (δ₁=2) and follow-up (δ₂=2) loops; human annotators score average Coherence 4.53, Realism 4.57, Complexity 4.64 out of 5, with Cohen's κ = 0.70–0.78. On BEAM, 1M-context models — GPT-4.1-nano, Gemini-2.0-flash, Qwen2.5-32B-AWQ, Llama-4-Maverick-fp8 — degrade sharply as context grows. The authors then propose LIGHT, a three-tier memory stack: (1) an episodic vector index of per-turn key-value pairs + summaries embedded with BAAI/bge-small-en-v1.5 in FAISS, (2) a scratchpad where Qwen2.5-32B-AWQ distills salient facts after each turn (compressed to 15K tokens by GPT-4.1-nano when it exceeds 30K), (3) the last N user-assistant pairs as working memory — plus a Qwen-based yes/no noise filter over scratchpad chunks at inference. LIGHT lifts average score by 3.5–12.7 percentage points over the best baseline at all lengths, and as high as +107% (GPT-4.1-nano) and +156% (Llama-4-Maverick) at 10M tokens where no baseline natively fits. Largest gains are in summarization (+160.6%), preference following (+76.5%), information extraction (+56.7%), and temporal reasoning (+56.3%); contradiction resolution remains the hardest, with all systems near floor. Best retrieval budget is K=15; working memory is roughly neutral at ≤1M tokens but contributes –5.7% at 10M when removed.

## Key Takeaway

The most counter-intuitive result is that simply giving a frontier LLM the entire 1M-token conversation **inside its native context window does not beat a smaller model armed with a three-tier external memory** — and the gap widens as conversations grow. At 100K tokens (where everything fits comfortably), LIGHT already gives a 44% relative lift to GPT-4.1-nano over its long-context baseline; at 1M (still fitting), the lift is 76%; at 10M (where nothing fits natively), the long-context baseline collapses and LIGHT yields +107%. In other words, "just throw it in the context window" — the dominant industry response to long-history problems — is losing to write-time distillation + retrieval even when no truncation is required. The right architectural move is **write-time intelligence (key-value extraction + scratchpad distillation) plus retrieve-time noise filtering**, not bigger windows.

## Implications

- **[ENGRAM: Encode + Aggregate] Distill on every turn, not at recall time** — LIGHT extracts key-value pairs *and* a salient-facts scratchpad after each turn, then compresses the scratchpad to half size when it crosses 30K tokens. The summarization gain alone is +160.6%, the largest per-ability lift, telling you that the bottleneck for long conversations is not retrieval coverage but *pre-computed structure*. For your own memory layer, this is the strongest argument yet for a write-time `/learn`-style extractor that fires every session rather than a query-time re-derivation pass.
- **[ENGRAM: Network] Two parallel shapes are doing different jobs**: a vector index (episodic, per-event grounding) and a free-form scratchpad blob (cross-event abstraction). Removing either at 10M tokens costs –8.5% and –3.7% respectively, which means polyglot storage is non-optional once dialogues are long enough. A pure-vault or pure-vector store will plateau.
- **[ENGRAM: Retrieve] More retrieval is not better** — peak performance is at K=15 retrieved chunks (+7.4% to +10.8% over K=5); K=20 already starts hurting from noisy context. The implication for your QMD-backed stack is to cap recall at ~15 hits and lean on a relevance filter; chasing higher K is a false economy.
- **[ENGRAM: Retrieve] Noise filtering may matter more than retrieval itself at extreme scale** — at 10M tokens, removing the LLM-judge yes/no chunk filter costs –8.3%, nearly identical to the –8.5% loss from removing retrieval entirely. This says you should treat the post-retrieval filter as a first-class memory component, not a bolt-on.
- **[ENGRAM: Ground] Contradiction resolution is the open frontier** — every system tested, including LIGHT, scored 0.000–0.050 on contradiction resolution (essentially floor) across all four conversation lengths. None of the proposed components meaningfully help. If your memory architecture is supposed to "surface, not smooth away" contradictions, no published system has solved the detection half yet; you may need a dedicated contradiction-detection subsystem (e.g., a maintenance loop that re-reads scratchpad pairs).
- **[ENGRAM: Aggregate] Working memory is roughly neutral until conversations are very long** — at 100K-1M tokens, ablating working memory actually slightly *improves* LIGHT's score (–1.6%, +1%, +1.4%), but at 10M it becomes essential (removal costs –5.7%). This is evidence that "recent-turn buffer" deserves a length-dependent default: small at short contexts, larger at long ones — not a fixed constant.
- **[ENGRAM: Maintain] Treat compression as a first-class lifecycle step** — LIGHT compresses scratchpad from 30K → 15K via GPT-4.1-nano when it grows past threshold. This is an explicit eviction policy: drop redundancy, keep what is still relevant. Most open-source memory systems lack any such pass — they either grow unboundedly or wipe state. The 30K/15K thresholds (~2:1 ratio, fired once per overflow) are a concrete starting point.
- **[ENGRAM: Encode + Maintain] Plan-driven synthetic data is now realistic enough to benchmark against** — the BEAM pipeline scores ≥4.5/5 on human-judged coherence, realism, and complexity, with inter-annotator κ = 0.70–0.78. Your evaluation harness for memory systems can lean on synthetic long-conversation generation rather than waiting for hand-curated corpora; the seed → narratives → plan → user-turn → assistant-turn → probing-question recipe is reusable.

## How to Apply It (method)

**Scenario:** You're testing whether your QMD-backed Flow OS memory layer keeps state coherent across long single-user research conversations — say, six months of compounding sessions with one venture client, totalling hundreds of thousands of tokens. You want to know which abilities (recall, multi-hop, contradiction handling, instruction following, preference adherence) actually hold up, and whether your current "vault + vector + extracted memories" shape is closer to LIGHT's three-tier architecture or to a naive RAG baseline.

**Steps:**

1. **Pick the ten memory abilities you care about**: Information Extraction (IE), Multi-Hop Reasoning (MR), Knowledge Update (KU), Temporal Reasoning (TR), Abstention (ABS), Contradiction Resolution (CR), Event Ordering (EO), Instruction Following (IF), Preference Following (PF), Summarization (SUM). For each, write a one-line operational definition: e.g., for IF — "did the system honour a user-stated constraint set 200 turns earlier?"

2. **Generate (or sample) a probe set per ability**: Either use the BEAM repository (https://github.com/mohammadtavakoli78/BEAM) or build one against your own conversation logs. If generating synthetically, use the 5-stage pipeline: seed → narratives → plan with N sub-plans of M bullets → user turns (in K batches of I) → assistant turns with bi-directional follow-up loops. Cap follow-up depth at δ₁=δ₂=2 — beyond that, dialogues become unrealistic. Augment the plan with a separate GPT-4.1 pass that injects bullets specifically designed to elicit CR / KU / IF probes (BEAM does this in a second stage because single-pass generation under-covers those abilities).

3. **For each conversation, generate 2 probes per ability** (20 per chat) with provenance: each probe carries source IDs pointing to the dialogue turns containing the answer. Decompose the gold answer into atomic nuggets (each one minimal self-contained criterion). The LLM-judge scoring prompt is:

   ```
   Return your evaluation in JSON format with two fields:
   {"score": [1.0 | 0.5 | 0.0], "reason": "[detailed explanation]"}
   NOTE: ONLY output the json object.
   ```

   For Event Ordering use Kendall tau-b on aligned event sequences (alignments via a binary YES/NO equivalence prompt) — not nugget scoring.

4. **Build the LIGHT-style memory stack alongside your current one** (so you can A/B):

   a. **Episodic index (key-value)** — after each user-assistant turn, extract key-value pairs + a one-line summary. The published extraction prompt is short and reusable:

      ```
      I provide you with a text. Your task it to identify all the details stated in the text,
      and output that in key: value format.
      E.g.: Key 1: Value 1, Key 2: Value 2, ...
      Also at the end, provide a brief summary: Summary: 'summarized text'
      Note: only output key-values and the summary. DO NOT provide explanation.
      Note: Do not output Key 1, Key 2, ...

      **Previous Context:** {history}
      text: {text}
      ```

      Embed with BAAI/bge-small-en-v1.5 (you already use QMD, which uses a similar dense model). Store the embedding as key, the original turn as value.

   b. **Scratchpad (salient facts)** — after each pair, run the longer "Extracted Facts" prompt that distils into bulleted facts/decisions/preferences/instructions/dates. When the scratchpad crosses 30K tokens, compress to 15K with the clustering+deduplication prompt that returns the structured KEY ENTITIES / CORE DECISIONS / USER PREFERENCES / etc. format.

   c. **Working memory** — last N user-assistant pairs verbatim (the paper does not fix N publicly but ablation results suggest tuning per length: small for short conversations, larger for ≥10M tokens).

5. **Wire the inference path**: At query time, retrieve K=15 nearest-neighbour episodic chunks, semantic-chunk the scratchpad (LangChain SemanticChunker), run a yes/no relevance filter on each chunk:

   ```
   I provide you with a user query and a text chunk.
   You need to decide if the text chunk is necessary for answering user question.
   If we need the text chunk to answer the user question, or if the text chunk is part of the answer return 'yes'
   If the text chunk is noise and not relevant return 'no'.
   Output format: Return only 'yes' or 'no', without any explanation.

   User query: {query}
   Text chunk: {doc_text}
   ```

   Concatenate {filtered episodic + filtered scratchpad + verbatim working memory} and pass to the model with the strict-context answer prompt.

6. **Run an ablation pass on YOUR stack** — disable each of (episodic / scratchpad / working memory / noise filter) one at a time and re-score. If any of them costs less than ~2 points at all conversation lengths, that component is not pulling its weight in your setup (the paper finds working memory is a free variable at <1M tokens but essential at 10M).

7. **Watch the contradiction-resolution column** — if your stack also bottoms out near zero there (as every system in the paper does), you've identified the right place to invest: build a contradiction-detection maintenance loop that re-reads pairs of scratchpad entries during idle compute.

**Expected outcome:** A scored table — one row per memory ability, one column per architecture variant — that tells you exactly which of (full context, RAG, episodic+scratchpad, episodic-only, scratchpad-only) your stack most resembles, and which ablations are safe vs. catastrophic. Concretely, you should be able to answer: "Does adding write-time scratchpad distillation actually move my numbers, or am I just paying for a vault that already does the same job?"

## Best Figure

![Figure 2 — Overview of the LIGHT framework (page 6)](figures/tavakoli-2026-beam-light-fig.png)

Image Candidates:
Figure 2 (p. 6): Architecture diagram showing the three memory pathways (episodic vector index, scratchpad with summarizer, working memory) feeding into a unified inference call — clearest single-view explanation of the method.
Table 1 (p. 8): Full results table across four conversation lengths × four LLMs × three methods × ten memory abilities, showing LIGHT wins almost every cell — the empirical receipt for the headline claim.
Figure 3 (p. 9): Ablation study showing component-by-component contribution growing with context length — visualises why each piece earns its place.

Best Image:
Figure Name: Figure 2: "Overview of the LIGHT framework"
Figure Page: 6
Slide Caption: LIGHT combines an episodic key-value index, a continually-distilled scratchpad of salient facts, and a recent-turn working memory; at inference, retrieved chunks and the noise-filtered scratchpad are fused with working memory before the LLM answers.
Description: The figure splits into two stacked panels. The upper panel is the *write path*: each user-assistant turn enters a Key-Value Extractor that emits per-event key-values, which are embedded and dropped into a vector database as episodic memory; in parallel, a Scratchpad Generator distils salient content for each pair into a running buffer; when the buffer crosses a token threshold, a Summarizer compresses it into semantic memory. The lower panel is the *read path*: an incoming query is sent to both a Retriever Model (which fetches relevant chunks from the episodic index) and a Filtering Noise module (which evaluates scratchpad chunks for question-relevance); the surviving scratchpad chunks, the retrieved episodic chunks, and the verbatim working memory are unioned and passed to the LLM, which produces the response. The figure is the cleanest single view of the paper's central architectural claim — that long-term memory is not one component but three coordinated, asynchronously-maintained subsystems with a noise filter at the seam.

## What Experts Overlook

LIGHT's headline numbers come from the architecture, but the detail almost nobody mentions is the **two-pass plan augmentation for evaluation coverage**: BEAM first generates a conversation plan from the seed, then runs a *second* GPT-4.1 pass (Listing 27) that injects three additional bullet points into every sub-plan specifically designed to make Contradiction Resolution, Knowledge Update, and Instruction Following testable. The paper explicitly notes that single-pass generation produces "lower quality and less reliable coverage of these abilities" — meaning the benchmark itself only exists because synthetic data generation was decomposed into a base-plan stage and a probe-coverage augmentation stage. This is visible in §2.2.1 and again in §B.3.2.

**Why it matters:** Most experts will read "we built a benchmark" and assume the hard part was the generator. The actual unlock is that long-tail abilities (contradictions, updates, persistent instructions) do not arise naturally even from very rich plans — you have to *plant* the conditions for them. The same lesson applies to any AI-as-maintainer memory system: if you want to evaluate (or train) for rare-but-load-bearing behaviours, you must inject the triggering structure into the data, not hope it shows up by accident. Without this, the most consequential failure modes never get tested and the architecture never gets stressed in the right places.

**Example of good use:** When building a synthetic harness to test whether the Flow OS memory layer correctly surfaces *contradictions* across sessions (e.g., a client says "I want to focus on AskRally" in March, then "let's pause AskRally" in May), you generate a normal multi-month session sequence and then run a deliberate augmentation pass that inserts paired statements designed to contradict each other at known turn distances. You can now measure whether your memory layer detects them — a capability you literally cannot evaluate without intentional probe planting.

**Example of misapplication:** A team builds an "agent-memory benchmark" by just sampling real user logs at scale, assuming volume substitutes for coverage. Their multi-hop and information-extraction numbers look reasonable because those abilities show up organically, but their contradiction-resolution and instruction-following scores are near zero across the board — and they conclude the model is great at memory, when really the benchmark never tested the hard parts. They ship the system; the first time a real user updates a preference, the agent ignores the update. The miss is structural: organic data does not generate enough adversarial inconsistency or long-range instruction adherence to score those columns meaningfully.

## Extracted Prompts

**Prompt explanation:** Episodic memory write — per-turn key-value extraction with running summary; feeds the vector index that backs LIGHT's episodic recall.

```
I provide you with a text. Your task it to identify all the details stated in the text,
and output that in key: value format.
E.g.:
Key 1: Value 1,
Key 2: Value 2,
Key 3: Value 3,
....

Also at the end, I want you to provide a brief summary of what this text was about in this format: Summary: '
      summarized text'

Note: only output key-values and the summary. DO NOT provide any explanation before or after that.
Note: Do not output Key 1, Key 2, ...

**Previous Context:**
{history}

text: {text}
```

**Prompt explanation:** Scratchpad write — the salient-facts extractor invoked after every user-assistant pair; produces the structured "Extracted Facts" block that accumulates LIGHT's long-term scratchpad.

```
You are a highly analytical AI assistant. Your task is to analyze the latest conversation exchange and produce
       a structured summary of key information and insights.

**Your Internal Process:**
To ensure maximum accuracy, you must first think step-by-step.
1. **Analyze:** Break down the user's latest message.
2. **Identify:** Pinpoint all facts, instructions, and updates.
3. **Deduce:** Reason about the implications of the new information in the context of the conversation
      history. What is the user's underlying goal or state?
4. **Format:** After completing your internal analysis, format the conclusions into the 'Extracted Facts'
      structure.

**Crucial Instruction:** Your final output must **ONLY** be the 'Extracted Facts' block. **DO NOT** include
      your step-by-step reasoning or any other text in your response. Strictly follow the format shown in the
      example's output.

---
**EXAMPLE**

**Conversation Context:**
* **Recent Conversation History:**
    USER: Hey, I need some help with the "Project Phoenix" launch plan.
    ASSISTANT: Of course. What do you need?
    USER: The launch date is set for September 15th, 2025. I'm responsible for the marketing materials.
* **Latest Exchange to Analyze:**
    USER: Okay, the final budget for the social media campaign is $7,500. The client, Innovate Corp, just
          approved it. Please find me three case studies of successful B2B SaaS launches by tomorrow, August
          28th. And don't include any of our direct competitors in the examples.
    ASSISTANT: Understood. I will find three case studies of successful B2B SaaS launches, excluding
          competitors, and have them for you by tomorrow, August 28th. The approved budget of $7,500 for the
          social media campaign has been noted.

**Example of Correct Final Output:**
    * The client's name is "Innovate Corp".
    * The project is related to a "B2B SaaS launch".
    * The final budget for the social media campaign is \$7,500.
    * A deadline is set for "tomorrow, August 28th".
    * User intends to review three case studies for the project.
    * Instruction: Find three case studies.
    * Constraint: Do not include direct competitors in the examples.
    * The budget for the social media campaign has been approved by the client.
    * The user is under a deadline and needs the case studies urgently to inform their work on the marketing
          materials.

---
**ACTUAL TASK**

**Recent Conversation History:**
{history}

**Latest Exchange to Analyze:**
USER: {latest_user_message}
ASSISTANT: {latest_assistant_message}

**Extracted Facts:**
```

**Prompt explanation:** Scratchpad maintenance — compression pass fired when the scratchpad exceeds 30K tokens; outputs a structured 15K-token (target) summary clustered by entity, decision, preference, instruction, date, context, action item, and development.

```
You are tasked with summarizing and compressing scratch pad content to fit within a specific token limit.
**Input Content:**
{content}

**Target Length:** {tokens_limit} tokens

**Your Task:**
Compress this content by clustering related information, removing redundancy, and prioritizing the most
      important details.

**Process:**
1. **Cluster**: Group related information by topic, entity, or theme
2. **Deduplicate**: Remove redundant or repetitive information
3. **Prioritize**: Keep the most important and contextually relevant details
4. **Compress**: Condense while maintaining essential meaning and context

**Output Format:**
Return ONLY the compressed content organized as:

**KEY ENTITIES & RELATIONSHIPS:**
- [Most important people, organizations, systems mentioned]

**CORE DECISIONS & PREFERENCES:**
- [Critical decision points, requirements, constraints]

**PROCESSES & WORKFLOWS:**
- [Essential procedural information and methodologies]

**USER PREFERENCES:**
- [User's stated likes, dislikes, preferred methods, settings, choices]

**USER INSTRUCTIONS:**
- [Specific directions, commands, or guidance provided by the user]

**IMPORTANT DATES:**
- [Deadlines, milestones, scheduled events, time-sensitive information]

**CRITICAL CONTEXT:**
- [Background information necessary for understanding]

**ACTIONABLE ITEMS:**
- [Next steps, pending actions, deadlines]

**IMPORTANT DEVELOPMENTS:**
- [Significant events, changes, milestones]

**Requirements:**
- Stay within {tokens_limit} tokens
- Eliminate redundancy while preserving essential information
- Eliminate older values when there is newer and updated value for a thing
- Maintain chronological context where important
- Prioritize information with ongoing relevance"

**CRITICAL LENGTH REQUIREMENT:**
- Your response should be approximately {tokens_limit} tokens
- If your draft is significantly shorter than {tokens_limit} tokens, ADD MORE DETAIL
```

**Prompt explanation:** Retrieve-time noise filter — binary classifier called on each semantic-chunk of the scratchpad against the query; only chunks marked "yes" pass through to the answer generator.

```
I provide you with a user query and a text chunk.
You need to decide if the text chunk is nesseccery for answering user question.
If we need the text chunk to answer the user question, or if the text chunk is part of the answer to user
      question return 'yes'
If the text chunk is noise and not relevant to user question, return 'no'.
Output format: Return only 'yes' or 'no', without any explantion before or after that.

User query: {query} \n\n
Text chunk: {doc_text}
```

**Prompt explanation:** Final answer generation — strict-context generation prompt used by both LIGHT and the RAG baseline; forbids drawing on parametric knowledge.

```
You are an assistant that MUST answer questions using ONLY the information provided in the context below.

STRICT INSTRUCTIONS:
1. Answer ONLY based on the provided context
2. Do NOT use your internal knowledge

CONTEXT:
<context>

QUESTION:
<question>

ANSWER REQUIREMENTS:
- Be direct and concise
- Only output the answer to the question without any explanation

RESPONSE:
```

**Prompt explanation:** Nugget-level rubric scorer — the LLM judge used to score each system response against the atomic nugget criteria for nine of ten abilities (event ordering is scored via Kendall tau-b instead).

```
Return your evaluation in JSON format with two fields:

{
    "score": [your score: 1.0, 0.5, or 0.0],
    "reason": "[detailed explanation of whether the rubric criterion was satisfied and why this justified the
          assigned score]"
}

NOTE: ONLY output the json object, without any explanation before or after that
```

**Prompt explanation:** Event-equivalence detector — binary classifier used to align events in system responses with gold nuggets before computing Kendall tau-b for Event Ordering scoring.

```
You are a binary classifier.
If the TWO snippets describe the SAME event/fact, reply **YES**
Otherwise reply **NO**. No extra words.
DO NOT provide any explanation.

First snippet: {first_paragraph}
Second snippet: {second_paragraph}
```

(Listings 1–19, 22–39 in Appendix H — chat-title, narrative, conversation-plan, user-turn, assistant-turn, follow-up, question-detection, contradiction/update/instruction probe-generation prompts — are also present in the paper but omitted here for brevity; they are reproducible via the BEAM repository at https://github.com/mohammadtavakoli78/BEAM.)

## Citations

- GPT-4 Technical Report — Achiam et al., 2023 (arXiv:2303.08774)
- Llama 3.3 model cards — Meta AI, 2024
- Claude 3 model card — Anthropic, 2024
- Claude 4 model card — Anthropic, 2025
- Longformer — Beltagy et al., 2020 (arXiv:2004.05150)
- The neurobiology of semantic memory — Binder & Desai, 2011 (Trends in Cognitive Sciences)
- RETRO — Borgeaud et al., 2022 (ICML)
- GPT-3 — Brown et al., 2020 (NeurIPS)
- SCOPE — Chen et al., 2025 (ICLR)
- AutoCompressor — Chevalier et al., 2023 (arXiv:2305.14788)

…and 65 more in the full `citations:` array in the frontmatter (75 total: full BEAM/LIGHT bibliography including the long-context backbone family — Transformer-XL, FlashAttention, Linformer, Performer, Mamba, RWKV, Hyena, BigBird, RoFormer, ALiBi, YaRN, LongRoPE, PagedAttention, Ring Attention, H2O, SnapKV — plus the memory-benchmark family — MSC, DuLeMon, MemoryBank, PerLTQA, LoCoMo, DialSim, LongMemEval, MemBench, MemoryCode — and the cognitive-science grounding (Binder & Desai 2011, Sridhar et al. 2023, Teyler & DiScenna 1986)).

## Related Digests

- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects (epistemically-typed four-network memory; LongMemEval results)
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems (paged virtual-memory metaphor for context; complementary to LIGHT's scratchpad-compression pass)
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (flat extracted-memory vs. graph variant; comparable extract-on-write architecture)
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory (write-time-distillation-is-anti-intelligence framing; directly relevant counter-thesis to LIGHT's heavy write-time work)

## Reviewer Notes

**Overall severity:** Clean

All quantitative claims in this digest map directly to numbers stated in the paper:

- **TLDR — "100 conversations, 2,000 questions, 10 abilities, 19 domains, three new dimensions (CR/EO/IF)"**: Verified in §2.2 (line ~190) and Appendix B.3.1 / Table 5.
- **TLDR — "average 3.5–12.7 percentage points lift over best baseline"**: Verified in Abstract (line 38) and §4.2.
- **TLDR — "+107% for GPT-4.1-nano and +156% for Llama-4-Maverick at 10M"**: Verified in §4.2 "Main Results" (line ~595).
- **TLDR — "summarization +160.6%, multi-hop +27.2%, preference following +76.5%, IE +56.7%, IF +39.5%, TR +56.3%"**: Verified in §4.2 (line ~602).
- **TLDR — "human evaluation: 4.53/4.57/4.64, Cohen's κ = 0.70–0.78"**: Verified in §4.2 "Human Evaluation" + Appendix B.2 Table 4.
- **TLDR — "δ₁ = δ₂ = 2 for question/follow-up loops"**: Verified in §2.2.3 (line ~328) and Appendix B.3.4.
- **TLDR — "BAAI/bge-small-en-v1.5 + FAISS"**: Verified in §3.1 and §4.1.
- **TLDR — "Qwen2.5-32B-AWQ for KV extraction and scratchpad, GPT-4.1-nano for compression"**: Verified in §3.1, §3.2.
- **TLDR — "30K → 15K token compression threshold"**: Verified in §3.2 "Construction" (line ~488).
- **Implications — "K=15 is best, K=20 starts hurting"**: Verified in §4.2 "Effect of Retrieval Budget" (line ~639): "+7.39%, +10.75%, +6.79%, and +6.3% at 100K, 500K, 1M, and 10M" — those numbers are quoted accurately.
- **Implications — "removing noise filter costs –8.3% at 10M, retrieval –8.5%, scratchpad –3.7%, working memory –5.7%"**: Verified in §4.2 "Ablation" (line ~622).
- **Implications — "working memory ablation slightly *improves* score at ≤1M"**: Verified in §4.2 "Ablation" (line ~624): "Working memory also degrades results here (–1.6%)" — the digest states this neutrally; minor watch-out: the paper phrases the ≤1M working-memory effect as "removing slightly improves" and "very slightly enhances," which is a small (~1-2pt) magnitude. The digest's "roughly neutral" framing is accurate.
- **Implications — "Contradiction Resolution scores 0.000–0.050 across systems"**: Verified by inspection of Table 1 (CR rows at all four lengths).
- **Method — "augmentation pass uses Listing 27 to inject three CR/KU/IF bullets"**: Verified in §2.2.1 (line ~283) and §B.3.2.
- **What Experts Overlook — two-pass plan augmentation**: Verified in §2.2.1 (line ~282) and §B.3.2 (line ~1428).

Two minor watch-outs worth noting but not warranting a downgrade from Clean:

- The lift numbers reported as "+44.3% for GPT-4.1-nano at 100K" and "+75.9% for GPT-4.1-nano at 1M" come straight from the paper (§4.2, line ~593), and these are *relative* improvements over the long-context baseline, not absolute points. The digest's "Key Takeaway" section uses the phrase "44% relative lift" and "76%" — this is correct framing, but a casual reader could mis-parse them as absolute. Acceptable as written.
- The digest cites "FAISS" for the vector store (verified §4.1 line ~586) and "BAAI/bge-small-en-v1.5" for embeddings (verified §4.1). No fabrication.

The figure section, prompts (Listings 20, 21, 40, 41, 42, 43, 44), and citation list are all directly transcribed from the source PDF.

Conclusion: Clean. No claims to revise; no fabricated metrics or methodology details detected.
