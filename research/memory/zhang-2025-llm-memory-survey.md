---
corpus: agentic-memory
kind: paper-digest
slug: zhang-2025-llm-memory-survey
title: "Memory in Large Language Models: Mechanisms, Evaluation and Evolution"
authors:
  - "Zhang, Dianxing"
  - "Li, Wendong"
  - "Song, Kani"
  - "Lu, Jiaye"
  - "Li, Gang"
  - "Yang, Liuchun"
  - "Li, Sheng"
year: 2025
publication_date: "2025-09"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2509.18868"
doi: null
arxiv_id: "2509.18868"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Treat LLM memory as a four-substrate system (parametric / contextual / external / procedural-episodic) measured under three parallel regimes (PO / Offline-Retrieval / Online-Retrieval) and governed via a release-grade DMM-Gov closed loop (versioning → canary → online monitoring → rollback → audit) — the survey's central thesis is that 'memory' is not a single thing and conflating substrates is the root cause of irreproducible RAG/editing/long-context results."
topics:
  - llm-memory
  - memory-taxonomy
  - rag-evaluation
  - knowledge-editing
  - machine-unlearning
  - long-context-evaluation
  - procedural-memory
  - temporal-governance
  - dmm-gov
  - engram
tags:
  - paper
  - survey
  - memory-architecture
  - evaluation-framework
  - rag
  - knowledge-editing
  - unlearning
  - governance
entities:
  - zhang-dianxing
  - li-sheng
  - digital-china-ai-research-institute
related_digests:
  - patel-2026-engram
  - du-2025-rethinking-memory
  - li-2025-memos
  - liu-2023-lost-in-the-middle
  - maharana-2024-locomo
  - packer-2023-memgpt-os
citations:
  - title: "FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation"
    authors: ["Vu, T.", "Iyyer, M.", "Wang, X.", "Constant, N.", "Wei, J.", "Wei, J.", "Tar, C.", "Sung, Y.-H.", "Zhou, D.", "Le, Q.", "Luong, T."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2310.03214"
    arxiv_id: "2310.03214"
  - title: "A Dataset for Answering Time-Sensitive Questions (TimeQA)"
    authors: ["Chen, W.", "Wang, X.", "Wang, W. Y."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2108.06314"
    arxiv_id: "2108.06314"
  - title: "Time-Aware Language Models as Temporal Knowledge Bases"
    authors: ["Dhingra, B.", "Cole, J. R.", "Eisenschlos, J. M.", "Gillick, D.", "Eisenstein, J.", "Cohen, W. W."]
    year: 2022
    doi: "10.1162/tacl_a_00459"
    url: "https://aclanthology.org/2022.tacl-1.15/"
    arxiv_id: "2106.15110"
  - title: "Artificial Intelligence Risk Management Framework (AI RMF 1.0)"
    authors: ["Tabassi, E."]
    year: 2023
    doi: "10.6028/NIST.AI.100-1"
    url: "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf"
    arxiv_id: null
  - title: "OWASP Top 10 for Large Language Model Applications"
    authors: ["OWASP Foundation"]
    year: 2023
    doi: null
    url: "https://owasp.org/www-project-top-10-for-large-language-model-applications/"
    arxiv_id: null
  - title: "Language Models as Knowledge Bases? (LAMA probe)"
    authors: ["Petroni, F.", "Rocktäschel, T.", "Lewis, P.", "Bakhtin, A.", "Wu, Y.", "Miller, A. H.", "Riedel, S."]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1909.01066"
    arxiv_id: "1909.01066"
  - title: "KILT: a Benchmark for Knowledge Intensive Language Tasks"
    authors: ["Petroni, F.", "Piktus, A.", "Fan, A.", "Lewis, P.", "Yazdani, M.", "De Cao, N.", "Thorne, J.", "Jernite, Y.", "Karpukhin, V.", "Maillard, J.", "Plachouras, V.", "Rocktäschel, T.", "Riedel, S."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2009.02252"
    arxiv_id: "2009.02252"
  - title: "Transformer Feed-Forward Layers Are Key-Value Memories"
    authors: ["Geva, M.", "Schuster, R.", "Berant, J.", "Levy, O."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2012.14913"
    arxiv_id: "2012.14913"
  - title: "A Mathematical Framework for Transformer Circuits"
    authors: ["Elhage, N.", "Nanda, N.", "Olsson, C.", "Henighan, T.", "Joseph, N.", "Mann, B.", "Askell, A.", "Bai, Y.", "Chen, A.", "Conerly, T.", "DasSarma, N.", "Drain, D.", "Ganguli, D.", "Hatfield-Dodds, Z.", "Hernandez, D.", "Jones, A.", "Kernion, J.", "Lovitt, L.", "Ndousse, K.", "Amodei, D.", "Brown, T.", "Clark, J.", "Kaplan, J.", "McCandlish, S.", "Olah, C."]
    year: 2021
    doi: null
    url: "https://transformer-circuits.pub/2021/framework/index.html"
    arxiv_id: null
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG)"
    authors: ["Lewis, P.", "Perez, E.", "Piktus, A.", "Petroni, F.", "Karpukhin, V.", "Goyal, N.", "Küttler, H.", "Lewis, M.", "Yih, W.-t.", "Rocktäschel, T.", "Riedel, S.", "Kiela, D."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2005.11401"
    arxiv_id: "2005.11401"
  - title: "REALM: Retrieval-Augmented Language Model Pre-training"
    authors: ["Guu, K.", "Lee, K.", "Tung, Z.", "Pasupat, P.", "Chang, M.-W."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2002.08909"
    arxiv_id: "2002.08909"
  - title: "Improving Language Models by Retrieving from Trillions of Tokens (RETRO)"
    authors: ["Borgeaud, S.", "Mensch, A.", "Hoffmann, J.", "Cai, T.", "Rutherford, E.", "Millican, K.", "van den Driessche, G.", "Lespiau, J.-B.", "Damoc, B.", "Clark, A.", "et al."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2112.04426"
    arxiv_id: "2112.04426"
  - title: "Sufficient Context: A New Lens on Retrieval-Augmented Generation Systems"
    authors: ["Joren, H.", "Zhang, J.", "Ferng, C.-S.", "Juan, D.-C.", "Taly, A.", "Rashtchian, C."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2411.06037"
    arxiv_id: "2411.06037"
  - title: "Unifying Large Language Models and Knowledge Graphs: A Roadmap"
    authors: ["Pan, S.", "Luo, L.", "Wang, Y.", "Chen, C.", "Wang, J.", "Wu, X."]
    year: 2024
    doi: "10.1109/TKDE.2024.3352100"
    url: "https://arxiv.org/abs/2306.08302"
    arxiv_id: "2306.08302"
  - title: "ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems"
    authors: ["Saad-Falcon, J.", "Khattab, O.", "Potts, C.", "Zaharia, M."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2311.09476"
    arxiv_id: "2311.09476"
  - title: "RAGChecker: A Fine-Grained Framework for Diagnosing Retrieval-Augmented Generation"
    authors: ["Ru, D.", "Qiu, L.", "Hu, X.", "Zhang, T.", "Shi, P.", "Chang, S.", "Wang, C.", "Sun, S.", "Li, H.", "Zhang, Z.", "Wang, B.", "Jiang, J.", "He, T.", "Wang, Z.", "Liu, P.", "Zhang, Y.", "Zhang, Z."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2408.08067"
    arxiv_id: "2408.08067"
  - title: "RAGAS: Automated Evaluation of Retrieval Augmented Generation"
    authors: ["Es, S.", "James, J.", "Espinosa-Anke, L.", "Schockaert, S."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2309.15217"
    arxiv_id: "2309.15217"
  - title: "RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems"
    authors: ["Friel, R.", "Belyi, M.", "Sanyal, A."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2407.11005"
    arxiv_id: "2407.11005"
  - title: "CRAG — Comprehensive RAG Benchmark"
    authors: ["Yang, X.", "Sun, K.", "Xin, H.", "Sun, Y.", "Bhalla, N.", "Chen, X.", "Choudhary, S.", "et al."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2406.04744"
    arxiv_id: "2406.04744"
  - title: "Retrieval-Augmented Generation with Conflicting Evidence (RAMDocs)"
    authors: ["Wang, H.", "Prasad, A.", "Stengel-Eskin, E.", "Bansal, M."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2504.13079"
    arxiv_id: "2504.13079"
  - title: "QAFactEval: Improved QA-based Factual Consistency Evaluation for Summarization"
    authors: ["Fabbri, A. R.", "Wu, C.-S.", "Liu, W.", "Xiong, C."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2112.08542"
    arxiv_id: "2112.08542"
  - title: "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation"
    authors: ["Min, S.", "Krishna, K.", "Lyu, X.", "Lewis, M.", "Yih, W.-t.", "Koh, P. W.", "Iyyer, M.", "Zettlemoyer, L.", "Hajishirzi, H."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.14251"
    arxiv_id: "2305.14251"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Packer, C.", "Wooders, S.", "Lin, K.", "Fang, V.", "Patil, S. G.", "Stoica, I.", "Gonzalez, J. E."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2310.08560"
    arxiv_id: "2310.08560"
  - title: "Locating and Editing Factual Associations in GPT (ROME)"
    authors: ["Meng, K.", "Bau, D.", "Andonian, A.", "Belinkov, Y."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2202.05262"
    arxiv_id: "2202.05262"
  - title: "Fast Model Editing at Scale (MEND)"
    authors: ["Mitchell, E.", "Lin, C.", "Bosselut, A.", "Finn, C.", "Manning, C. D."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2110.11309"
    arxiv_id: "2110.11309"
  - title: "Memory-Based Model Editing at Scale (SERAC)"
    authors: ["Mitchell, E.", "Lin, C.", "Bosselut, A.", "Manning, C. D.", "Finn, C."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2206.06520"
    arxiv_id: "2206.06520"
  - title: "Mass-Editing Memory in a Transformer (MEMIT)"
    authors: ["Meng, K.", "Sharma, A. S.", "Andonian, A.", "Belinkov, Y.", "Bau, D."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2210.07229"
    arxiv_id: "2210.07229"
  - title: "History Matters: Temporal Knowledge Editing in Large Language Model (AToKE)"
    authors: ["Yin, X.", "Jiang, J.", "Yang, L.", "Wan, X."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2312.05497"
    arxiv_id: "2312.05497"
  - title: "Event-Level Knowledge Editing (ELKEN)"
    authors: ["Peng, H.", "Wang, X.", "Li, C.", "Zeng, K.", "Duo, J.", "Cao, Y.", "Hou, L.", "Li, J."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.13093"
    arxiv_id: "2402.13093"
  - title: "MUSE: Machine Unlearning Six-Way Evaluation for Language Models"
    authors: ["Shi, W.", "Lee, J.", "Huang, Y.", "Malladi, S.", "Zhao, J.", "Holtzman, A.", "Liu, D.", "Zettlemoyer, L.", "Smith, N. A.", "Zhang, C."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2407.06460"
    arxiv_id: "2407.06460"
  - title: "TOFU: A Task of Fictitious Unlearning for LLMs"
    authors: ["Maini, P.", "Feng, Z.", "Schwarzschild, A.", "Lipton, Z. C.", "Kolter, J. Z."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2401.06121"
    arxiv_id: "2401.06121"
  - title: "Negative Preference Optimization: From Catastrophic Collapse to Effective Unlearning (NPO)"
    authors: ["Zhang, R.", "Lin, L.", "Bai, Y.", "Mei, S."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2404.05868"
    arxiv_id: "2404.05868"
  - title: "RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models"
    authors: ["Jin, Z.", "Cao, P.", "Wang, C.", "He, Z.", "Yuan, H.", "Li, J.", "Chen, Y.", "Liu, K.", "Zhao, J."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2406.10890"
    arxiv_id: "2406.10890"
  - title: "The WMDP Benchmark: Measuring and Reducing Malicious Use with Unlearning"
    authors: ["Li, N.", "Pan, A.", "Gopal, A.", "Yue, S.", "Berrios, D.", "Gatti, A.", "Li, J. D.", "et al."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2403.03218"
    arxiv_id: "2403.03218"
  - title: "Extracting Training Data from Large Language Models"
    authors: ["Carlini, N.", "Tramèr, F.", "Wallace, E.", "Jagielski, M.", "Herbert-Voss, A.", "Lee, K.", "Roberts, A.", "Brown, T.", "Song, D.", "Erlingsson, Ú.", "Oprea, A.", "Raffel, C."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2012.07805"
    arxiv_id: "2012.07805"
  - title: "Do Membership Inference Attacks Work on Large Language Models?"
    authors: ["Duan, M.", "Suri, A.", "Mireshghallah, N.", "Min, S.", "Shi, W.", "Zettlemoyer, L.", "Tsvetkov, Y.", "Choi, Y.", "Evans, D.", "Hajishirzi, H."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.07841"
    arxiv_id: "2402.07841"
  - title: "Quantifying Memorization Across Neural Language Models"
    authors: ["Carlini, N.", "Ippolito, D.", "Jagielski, M.", "Lee, K.", "Tramer, F.", "Zhang, C."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2202.07646"
    arxiv_id: "2202.07646"
  - title: "Deduplicating Training Data Mitigates Privacy Risks in Language Models"
    authors: ["Kandpal, N.", "Wallace, E.", "Raffel, C."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2202.06539"
    arxiv_id: "2202.06539"
  - title: "Deduplicating Training Data Makes Language Models Better"
    authors: ["Lee, K.", "Ippolito, D.", "Nystrom, A.", "Zhang, C.", "Eck, D.", "Callison-Burch, C.", "Carlini, N."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2107.06499"
    arxiv_id: "2107.06499"
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    authors: ["Liu, N. F.", "Lin, K.", "Hewitt, J.", "Paranjape, A.", "Bevilacqua, M.", "Petroni, F.", "Liang, P."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2307.03172"
    arxiv_id: "2307.03172"
  - title: "Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization"
    authors: ["Hsieh, C.-Y.", "Chuang, Y.-S.", "Li, C.-L.", "Wang, Z.", "Le, L. T.", "Kumar, A.", "Glass, J.", "Ratner, A.", "Lee, C.-Y.", "Krishna, R.", "Pfister, T."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2406.16008"
    arxiv_id: "2406.16008"
  - title: "RULER: What's the Real Context Size of Your Long-Context Language Models?"
    authors: ["Hsieh, C.-P.", "Sun, S.", "Kriman, S.", "Acharya, S.", "Rekesh, D.", "Jia, F.", "Zhang, Y.", "Ginsburg, B."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2404.06654"
    arxiv_id: "2404.06654"
  - title: "LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding"
    authors: ["Bai, Y.", "Lv, X.", "Zhang, J.", "Lyu, H.", "Tang, J.", "Huang, Z.", "Du, Z.", "Liu, X.", "Zeng, A.", "Hou, L.", "Dong, Y.", "Tang, J.", "Li, J."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2308.14508"
    arxiv_id: "2308.14508"
  - title: "HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly"
    authors: ["Yen, H.", "Gao, T.", "Hou, M.", "Ding, K.", "Fleischer, D.", "Izsak, P.", "Wasserblat, M.", "Chen, D."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2410.02694"
    arxiv_id: "2410.02694"
  - title: "InfiniteBench: Extending Long Context Evaluation Beyond 100k Tokens"
    authors: ["Zhang, X.", "Chen, Y.", "Hu, S.", "Xu, Z.", "Chen, J.", "Hao, M. K.", "Han, X.", "Thai, Z. L.", "Wang, S.", "Liu, Z.", "Sun, M."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.13718"
    arxiv_id: "2402.13718"
  - title: "LV-Eval: A Balanced Long-Context Benchmark with 5 Length Levels up to 256k"
    authors: ["Yuan, T.", "Ning, X.", "Zhou, D.", "Yang, Z.", "Li, S.", "Zhuang, M.", "Tan, Z.", "Yao, Z.", "Lin, D.", "Li, B.", "Dai, G.", "Yan, S.", "Wang, Y."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.05136"
    arxiv_id: "2402.05136"
  - title: "LongMemEval: Benchmarking Chat Assistants on Long-term Interactive Memory"
    authors: ["Wu, D.", "Wang, H.", "Yu, W.", "Zhang, Y.", "Chang, K.-W.", "Yu, D."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2410.10813"
    arxiv_id: "2410.10813"
  - title: "Episodic Memories Generation and Evaluation Benchmark for Large Language Models"
    authors: ["Huet, A.", "Ben Houidi, Z.", "Rossi, D."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2501.13121"
    arxiv_id: "2501.13121"
  - title: "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context"
    authors: ["Dai, Z.", "Yang, Z.", "Yang, Y.", "Carbonell, J.", "Le, Q. V.", "Salakhutdinov, R."]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1901.02860"
    arxiv_id: "1901.02860"
  - title: "Compressive Transformers for Long-Range Sequence Modelling"
    authors: ["Rae, J. W.", "Potapenko, A.", "Jayakumar, S. M.", "Lillicrap, T. P."]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1911.05507"
    arxiv_id: "1911.05507"
  - title: "Efficient Streaming Language Models with Attention Sinks (StreamingLLM)"
    authors: ["Xiao, G.", "Tian, Y.", "Chen, B.", "Han, S.", "Lewis, M."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2309.17453"
    arxiv_id: "2309.17453"
  - title: "Leave No Context Behind: Efficient Infinite Context Transformers with Infini-Attention"
    authors: ["Munkhdalai, T.", "Faruqui, M.", "Gopal, S."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2404.07143"
    arxiv_id: "2404.07143"
  - title: "Generalization through Memorization: Nearest Neighbor Language Models (kNN-LM)"
    authors: ["Khandelwal, U.", "Levy, O.", "Jurafsky, D.", "Zettlemoyer, L.", "Lewis, M."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/1911.00172"
    arxiv_id: "1911.00172"
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    authors: ["Park, J. S.", "O'Brien, J. C.", "Cai, C. J.", "Morris, M. R.", "Liang, P.", "Bernstein, M. S."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2304.03442"
    arxiv_id: "2304.03442"
  - title: "TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogues"
    authors: ["Ge, Y.", "Romeo, S.", "Cai, J.", "Shu, R.", "Sunkara, M.", "Benajiba, Y.", "Zhang, Y."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2502.09455"
    arxiv_id: "2502.09455"
  - title: "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models"
    authors: ["Jiménez Gutiérrez, B.", "Shu, Y.", "Gu, Y.", "Yasunaga, M.", "Su, Y."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2405.14831"
    arxiv_id: "2405.14831"
  - title: "Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)"
    authors: ["Maharana, A.", "Lee, D.-H.", "Tulyakov, S.", "Bansal, M.", "Barbieri, F.", "Fang, Y."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.17753"
    arxiv_id: "2402.17753"
  - title: "Evaluating the Ripple Effects of Knowledge Editing in Language Models (RIPPLEEDITS)"
    authors: ["Cohen, R.", "Biran, E.", "Yoran, O.", "Globerson, A.", "Geva, M."]
    year: 2023
    doi: "10.1162/tacl_a_00644"
    url: "https://arxiv.org/abs/2307.12976"
    arxiv_id: "2307.12976"
  - title: "Long-form Evaluation of Model Editing (LEME)"
    authors: ["Rosati, D.", "Gonzales, R.", "Chen, J.", "Yu, X.", "Erkan, M.", "Kayani, Y.", "Chavatapalli, S. D.", "Rudzicz, F.", "Sajjad, H."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.09394"
    arxiv_id: "2402.09394"
  - title: "Editing the Mind of Giants: An In-depth Exploration of Pitfalls of Knowledge Editing (ConflictEdit/Pitfalls)"
    authors: ["Hsueh, C.-H.", "Huang, P. K.-M.", "Lin, T.-H.", "Liao, C.-W.", "Fang, H.-C.", "Huang, C.-W.", "Chen, Y.-N."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2406.01436"
    arxiv_id: "2406.01436"
  - title: "WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models"
    authors: ["Wang, P.", "Li, Z.", "Zhang, N.", "Xu, Z.", "Yao, Y.", "Jiang, Y.", "Xie, P.", "Huang, F.", "Chen, H."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2405.14768"
    arxiv_id: "2405.14768"
  - title: "AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models"
    authors: ["Fang, J.", "Jiang, H.", "Wang, K.", "Ma, Y.", "Shi, J.", "Wang, X.", "He, X.", "Chua, T.-s."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2410.02355"
    arxiv_id: "2410.02355"
  - title: "Learning to Edit: Aligning LLMs with Knowledge Editing (LTE)"
    authors: ["Jiang, Y.", "Wang, Y.", "Wu, C.", "Zhong, W.", "Zeng, X.", "Gao, J.", "Li, L.", "Jiang, X.", "Shang, L.", "Tang, R.", "Liu, Q.", "Wang, W."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2402.11905"
    arxiv_id: "2402.11905"
  - title: "Uncovering Overfitting in Large Language Model Editing (EVOKE)"
    authors: ["Zhang, M.", "Ye, X.", "Liu, Q.", "Ren, P.", "Wu, S.", "Chen, Z."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2410.07819"
    arxiv_id: "2410.07819"
  - title: "Rebuilding ROME: Resolving Model Collapse during Sequential Model Editing (r-ROME)"
    authors: ["Gupta, A.", "Anumanchipalli, G. K."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2403.07175"
    arxiv_id: "2403.07175"
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    authors: ["Wei, J.", "Wang, X.", "Schuurmans, D.", "Bosma, M.", "Ichter, B.", "Xia, F.", "Chi, E.", "Le, Q.", "Zhou, D."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2201.11903"
    arxiv_id: "2201.11903"
  - title: "RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models"
    authors: ["Niu, C.", "Wu, Y.", "Zhu, J.", "Xu, S.", "Shum, K.", "Zhong, R.", "Song, J.", "Zhang, T."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2401.00396"
    arxiv_id: "2401.00396"
  - title: "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models"
    authors: ["Thakur, N.", "Reimers, N.", "Rücklé, A.", "Srivastava, A.", "Gurevych, I."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2104.08663"
    arxiv_id: "2104.08663"
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    authors: ["Shinn, N.", "Cassano, F.", "Berman, E.", "Gopinath, A.", "Narasimhan, K.", "Yao, S."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2303.11366"
    arxiv_id: "2303.11366"
  - title: "Voyager: An Open-Ended Embodied Agent with Large Language Models"
    authors: ["Wang, G.", "Xie, Y.", "Jiang, Y.", "Mandlekar, A.", "Xiao, C.", "Zhu, Y.", "Fan, L.", "Anandkumar, A."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.16291"
    arxiv_id: "2305.16291"
  - title: "AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents"
    authors: ["Anokhin, P.", "Semenov, N.", "Sorokin, A.", "Evseev, D.", "Kravchenko, A.", "Burtsev, M.", "Burnaev, E."]
    year: 2025
    doi: null
    url: "https://arxiv.org/abs/2407.04363"
    arxiv_id: "2407.04363"
  - title: "Holistic Evaluation of Language Models (HELM)"
    authors: ["Liang, P.", "Bommasani, R.", "Lee, T.", "Tsipras, D.", "Soylu, D.", "Yasunaga, M.", "Zhang, Y.", "Narayanan, D.", "Wu, Y.", "Kumar, A.", "et al."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2211.09110"
    arxiv_id: "2211.09110"
  - title: "Dynabench: Rethinking Benchmarking in NLP"
    authors: ["Kiela, D.", "Bartolo, M.", "Nie, Y.", "Kaushik, D.", "Geiger, A.", "Wu, Z.", "Vidgen, B.", "Prasad, G.", "Singh, A.", "Ringshia, P.", "Ma, Z.", "Thrush, T.", "Riedel, S.", "Waseem, Z.", "Stenetorp, P.", "Jia, R.", "Bansal, M.", "Potts, C.", "Williams, A."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2104.14337"
    arxiv_id: "2104.14337"
  - title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
    authors: ["Zheng, L.", "Chiang, W.-L.", "Sheng, Y.", "Zhuang, S.", "Wu, Z.", "Zhuang, Y.", "Lin, Z.", "Li, Z.", "Li, D.", "Xing, E. P.", "Zhang, H.", "Gonzalez, J. E.", "Stoica, I."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2306.05685"
    arxiv_id: "2306.05685"
  - title: "Large Language Models Are Not Fair Evaluators"
    authors: ["Wang, P.", "Li, L.", "Chen, L.", "Cai, Z.", "Zhu, D.", "Lin, B.", "Cao, Y.", "Liu, Q.", "Liu, T.", "Sui, Z."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.17926"
    arxiv_id: "2305.17926"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "A unified framework for LLM memory research: mechanisms, evaluation, and governance"
  page: 3
  image_path: "figures/zhang-2025-llm-memory-survey-fig.png"
---

# Memory in Large Language Models: Mechanisms, Evaluation and Evolution

**Authors:** Zhang, Dianxing · Li, Wendong · Song, Kani · Lu, Jiaye · Li, Gang · Yang, Liuchun · Li, Sheng
**Published:** 2025-09 · [Source](https://arxiv.org/abs/2509.18868)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

A 50-page Digital China AI Research Institute survey that tries to do for "LLM memory" what Codd did for databases — give it a definition, a typology, and a release-grade operating model. It defines memory as **any persistent, addressable state written during pretraining / finetuning / inference that stably influences outputs**, then partitions that into a 4-substrate taxonomy — **parametric** (weights), **contextual** (KV cache / activations), **external** (RAG / retrieval index), and **procedural/episodic** (cross-session event store) — each annotated by a "memory quadruple" of *storage location · persistence · write/access path · controllability*. Around this it stacks three reusable scaffolds: (1) a **three-regime evaluation protocol** — Parametric-Only (PO) / Offline-Retrieval / Online-Retrieval — run **in parallel on the same slice** so capability and information availability are decoupled; (2) **layered metric families** per substrate (closed-book P@k for parametric; position-performance curves and mid-sequence drop for contextual; Retrieval-Quality × Faithfulness/Attribution × Context-Utilization three-layer for external; the **E-MARS+ five-panel** Encode-Memorize / Attribute-Replay / Suppress-Freshness-Conflict / Stability / Cost for procedural); and (3) **DMM-Gov**, a deployment-grade governance loop — admission thresholds → progressive rollout → online monitoring → reversible rollback → change-audit certificate — that wraps DAPT/TAPT, PEFT, model editing (ROME / MEND / MEMIT / SERAC, hardened with AlphaEdit / WISE / LTE / AToKE / ELKEN), and RAG inside a single decision surface aligned with NIST AI-RMF and OWASP LLM Top-10. The paper closes with four falsifiable open propositions, including the engineering-load-bearing one: **under fixed latency/cost budgets, does retrieval + small-window replay systematically beat ultra-long-context direct reading?** The survey's posture is unmistakably industrial — fewer model-card numbers, more pre-registered thresholds, rollback points, and "edit/forgetting certificates" you can hand to an auditor. **[ENGRAM: all six dimensions; this paper is itself a coordinate system, not a method.]**

## Key Takeaway

For a memory-architecture team, the load-bearing contribution is **not** the four-way taxonomy (which is largely a re-shuffle of prior literature) but the **three-regime parallel protocol + DMM-Gov audit loop**: run PO, Offline-Retrieval, and Online-Retrieval on the *same data slice* and *same time window*, and report all of {answer text, evidence citations, model confidence, refusal flags} for each — otherwise any cross-system claim conflates "what the model knows" with "what was available to retrieve." Combined with pre-registered thresholds (their illustrative defaults: Citation Coverage ≥ 0.85, Unsupported Claim Rate ≤ 0.05, Recall@5 ≥ 0.85, Freshness ≥ 0.80, Conflict-Handled@5 ≥ 0.80, ESR ≈ 0.90, Locality ≈ 0.95, Drawdown ≤ 1–2%) plus rollback points and an "edit/forgetting certificate" (target / time / method / verification / regression / rollback / audit), this is the closest the field has come to a release SOP for memory mutations. **[ENGRAM: G (Ground — provenance + audit), M (Maintain — rollback as first-class), A (Aggregate — when to consolidate via edit vs externalize)]**.

## Implications

**For Flow OS memory architecture (mapped to ENGRAM):**

- **E — Encode**. The paper's "boundary judgments should follow observable behavior" decision rules give a clean test for what counts as a memory write in Flow's `/learn` pipeline: information that *requires placement in the prompt* is contextual (not memory); information that *enters the generation loop via retrieval/tools* is external memory; information requiring *cross-turn replay of structured events* is procedural. This validates Flow's choice to gate `/learn` (write only when episodic/procedural signal is present) rather than auto-capturing every turn into vector storage. The "retrievers and caches do not automatically constitute memory; they count only when their returns enter the generation loop and reproducibly affect outputs" principle is a direct prescription against the failure mode of "rich vector store, no demonstrated effect on outputs." **[ENGRAM-E]**

- **N — Network (shape)**. The paper's "rule of thirds" for substrate selection — external memory first for timeliness/traceability, model editing for small unambiguous fact corrections, DAPT/PEFT for broad-stable scope — argues directly for Flow's current architecture (markdown vault + QMD hybrid as external + procedural memory) and against the temptation to fine-tune for personalization. The boundary-ambiguity warning about RAG's "dual identity" (documents become contextual once concatenated into the prompt) is the right framing for Flow's prompt-injection step: when QMD hits are injected by the UserPromptSubmit hook, the same content is **simultaneously** external (provenance-preserved file paths) and contextual (subject to mid-sequence drop). The implication: keep file-path citations even when injecting raw chunks, because that's the only thing that lets you fall back to external-memory evaluation when the contextual layer drops the evidence. **[ENGRAM-N]**

- **G — Ground (trust)**. The three-layer decoupling — Retrieval Quality (Recall@k, nDCG) × Attribution/Faithfulness (FActScore, Citation Recall) × Context-Utilization (mid/end position robustness) — is **exactly** the missing diagnostic for Flow's UserPromptSubmit BM25 injection. Right now, a wrong assistant answer can fail at any of three places (the file wasn't retrieved, the file was retrieved but the model didn't cite it, or the file was retrieved + cited but at a position the model under-utilizes). Without the three-layer split, all three look like "QMD is broken." The fix is to log per-turn whether (i) the right file was in the top-k, (ii) the assistant cited it, (iii) the cited content actually appeared in the answer. **[ENGRAM-G, ENGRAM-R]**

- **A — Aggregate (consolidation)**. The Pareto warning — effectiveness ⊥ locality ⊥ generalization in editing, and effectiveness ⊥ utility-retention ⊥ scalability in unlearning — is a strong argument for the **externalize-first** posture in Flow's pattern consolidation: pattern memories should be retrievable text, not weights. The survey's evidence that **contextual editing outperforms parametric editing on ripple effects (RIPPLEEDITS)** — i.e., putting "Paris is the capital of Japan" in the prompt produces *more* consistent downstream behavior than rewriting the weight — is the formal version of why Flow's `/learn` writes to markdown rather than attempting model-side knowledge edits. **[ENGRAM-A]**

- **M — Maintain (lifecycle)**. DMM-Gov maps **directly** onto a missing layer in Flow: there is no "edit/forgetting certificate" for memory mutations. Right now, when `/learn` updates a pattern file from LOW → MEDIUM confidence, or when a contradiction detector flags an old memory, there is no machine-readable record of *target / effective time / method / verification slice / rollback point*. The seven-field certificate schema (F1–F7) is small enough to be a frontmatter block on every memory mutation. Combined with the four-dimensional forgetting acceptance (thoroughness / utility retention / scalability / sustainability), this is a release-grade upgrade path for `/learn` and a future `/forget` skill. **[ENGRAM-M]**

**For research-cycle / longitudinal compounding**: the paper's argument that **closed-set answerability assumptions (KILT-style) fundamentally differ from FreshQA-style dynamic update settings** is the formal explanation for why `/research-cycle` over time produces drift between cycle digests: each cycle's "snapshot" of the literature is closed-set, but the underlying field is online-retrieval. The fix is to record the snapshot date and the wiki state on every cycle digest, then compare longitudinally as a freshness/conflict diagnostic — not as a "consensus shifted" finding.

## How to Apply It (method)

Concrete protocol for adopting this paper in a memory-architecture project:

1. **Inventory your substrates against the 4-way taxonomy.** For each piece of state your system reads/writes, classify it as P / C / E / Pr and record the memory quadruple (storage location, persistence, write path, controllability). Borderline cases (e.g., KV-cache eviction policy, RAG chunks in the prompt) get tagged with both labels; the survey's decision rules (§3.2 "Operational criteria") resolve them by observable behavior.

2. **Stand up the three-regime evaluation harness.** Pick one task slice you care about (for Flow: "recall what user said about topic X over past N weeks"). Build three runners on the *same data slice and time window*:
   - **PO**: disable retrieval, disable memory injection.
   - **Offline-Retrieval**: frozen QMD index from a fixed snapshot date.
   - **Online-Retrieval**: live QMD index, allowed to drain captures queue.
   For each, log answer text + evidence citations + confidence + refusal flag. Use paired bootstrap with Holm–Bonferroni for cross-regime claims.

3. **Pick the right metric family per substrate.** Don't substitute a single number; report:
   - Parametric: closed-book P@k or domain QA accuracy, plus edit ESR / Locality / Drawdown if you do any param-side updates.
   - Contextual: position–performance curve at min 3 length bins; report mid-sequence drop in absolute percentage points.
   - External: dual-track (nDCG@10 + Recall@5 for IR quality; FActScore + Citation Recall for attribution; one Context-Utilization probe).
   - Procedural/Episodic: E-MARS+ five-panel (Event-F1, RSF, Step-Order Acc, Abstention@Unanswerable, Slope@T, Cost@Target).

4. **Pre-register thresholds and rollback points before any deployment.** Use the survey's illustrative defaults as a starting point, calibrated to your risk tier. Write them down *before* the canary, not after, so you can't move the goalposts.

5. **Add the edit/forgetting certificate (F1–F7) to every memory mutation.** Minimal frontmatter block: `target`, `effective_time`/`expiry_time`, `method` (RAG / edit / PEFT / system-override), `verification_slice_and_metric`, `regression_set` (long-form LEME-style + conflict ConflictEdit-style), `rollback_point`, `audit_chain`. This is the artifact that makes the loop closeable.

6. **For long-context decisions, use the survey's six-step decision flow (§5.4.2)**: identify timeliness → determine granularity of change → constrain consistency (time windows? multi-entity?) → pre-register thresholds → canary + monitor → rollback or harden. This is the missing decision rubric for "should I add this to the system prompt, store as memory, or rebuild the index."

## Best Figure

![Figure 1 — A unified framework for LLM memory research: mechanisms, evaluation, and governance (page 3)](figures/zhang-2025-llm-memory-survey-fig.png)

**Reading the figure.** Top row (orange): the four memory substrates with their storage and persistence properties — *Parametric* (weights, long-term), *Contextual* (KV cache, transient), *External* (retrieval index, updatable), *Procedural/Episodic* (event store, session-level). All four flow into a central blue block: the **Write (W) — Read-out (R) — Inhibit/Update (I)** cycle that the survey uses as its unifying causal chain. From R/W/I, three evaluation modules branch out (middle row, green/purple): *Mechanistic Evaluation* (addressability, causal tracing — the ROME / RIPPLEEDITS family), the *Layered Evaluation System* (the three-regime + four-substrate layered metrics that make up §4), and *Performance Evaluation* (three-regime protocol, FActScore). Below that, a *Risk Evaluation* node (privacy leakage, hallucination rate) bridges into the bottom red row — the **DMM-Gov Dynamic Governance Framework** with its three operational arms: an *Edit/Forgetting Certificate* (the F1–F7 schema), a *Six-Step Decision Flow* (the rubric for choosing parametric edit vs RAG vs procedural memory), and at the bottom *Online Monitoring Metrics* and *Rollback Strategy*. The dashed outer frame is labelled "Timeline Alignment · Auditability" — the survey's deliberate framing that the *whole* picture only works under shared snapshot dates and a release-grade audit trail.

**Why this is the right figure for the memory-architect lens.** Most LLM-memory papers give you one box from this diagram: a new retriever, a new editing method, a new long-context benchmark. This figure makes explicit what the paper claims is missing from the field — the **connecting tissue** between the four substrates (top), the layered evaluations (middle), and a deployable governance loop (bottom). For Flow OS the figure is also a literal architecture template: the four orange boxes are direct analogues of base model weights / current prompt / QMD vault / session captures; the central R/W/I cycle is the contract `/learn` and the UserPromptSubmit hook implement together; and the red bottom row is the missing layer (no `/forget`, no rollback ledger, no audit certificate yet).

**One thing the figure under-sells.** The diagram presents the substrates as parallel siblings, but the survey's text repeatedly returns to the **dual-identity** problem: in any RAG system the *same* string is simultaneously External (in the index) and Contextual (once concatenated into the prompt), and these two identities have *opposite* failure modes (External: wrong/stale retrieval; Contextual: lost-in-the-middle). A diagram that drew an explicit handoff arrow between External and Contextual would better capture the paper's central engineering claim.

## What Experts Overlook

**1. The three-regime protocol is the actual deliverable; the taxonomy is the wrapper.** Most readers will quote the four-way taxonomy and skip §4.1.2. The four-way taxonomy is largely a relabeling — Geva et al. 2021 (FFN as KV memory), Lewis et al. 2020 (RAG), Packer et al. 2024 (MemGPT) already implicitly carved this space. What's actually novel is the *protocol*: running PO + Offline-Retrieval + Online-Retrieval **in parallel on the same data slice** with unified reporting (answer + citations + confidence + refusal). Without that, every cross-paper RAG / editing / long-context claim is silently confounded by which version of the index was in scope.

**2. "Contextual editing outperforms parametric editing on ripple effects" is a load-bearing finding most surveys bury.** The RIPPLEEDITS result — that adding "Paris is the capital of Japan" to the *prompt* produces more consistent downstream behavior than rewriting the *weight* — is presented in §4.2.2 as a one-paragraph aside but is the most operationally important finding in the paper for memory-architecture teams. It is the formal justification for the externalize-first principle that underlies LangChain / LlamaIndex / Flow OS / MemGPT — and it directly contradicts the implicit pitch of every model-editing paper (that param-side edits are the "real" fix and prompt overrides are a workaround).

**3. The illustrative thresholds are calibrated to high-stakes industrial deployment, not to research benchmarks.** Citation Coverage ≥ 0.85, Unsupported Claim Rate ≤ 0.05, Drawdown ≤ 1–2% — these are NIST/OWASP-grade numbers, not arxiv-leaderboard numbers. A research reader will dismiss them as "obvious"; an engineering reader will recognize them as the line below which a system can't be shipped to a regulated client. The paper does not flag this gap, but the entire DMM-Gov framework only makes sense under the second posture.

**4. "Visible ≠ usable" applies to memory systems, not just long contexts.** The Lost-in-the-Middle phenomenon is invoked in §4.3 as a long-context problem, but the same principle applies to any memory system that retrieves > 5 documents and concatenates them: the middle ones drop out *regardless of the retriever's quality*. This is why the External / Contextual handoff (see "Best Figure" above) is the real bottleneck, and why optimizing retriever recall above ~Recall@5 yields diminishing returns until you also fix position handling.

**5. The dimensional Pareto warnings are *necessary* facts, not engineering limitations to optimize away.** Effectiveness ⊥ locality ⊥ generalization (editing) and effectiveness ⊥ utility-retention ⊥ scalability (unlearning) are presented as challenges, but they are likely **provable Pareto frontiers** — not bottlenecks that better methods will eliminate. The survey hints at this in Open Proposition C ("Do combinations exist that attain a provable Pareto frontier?") but doesn't commit. A memory architect should treat these as load-bearing constraints to design around, not problems to wait out.

**6. The paper does not engage with the human-side cost of `Refusal@Stale`.** Selective answering ("refuse when evidence is insufficient") is treated as a positive system property. In a personal-assistant deployment (Flow's posture), high refusal rate is a *worse* outcome than a soft-confidence answer with a citation. The paper's metric system gives you risk-coverage curves (AURC) but doesn't argue for where the operating point should sit for a low-stakes single-user deployment — this is a gap to fill from the user side.

## Extracted Prompts

The paper does not contain explicit LLM prompts, but it does contain three **operational templates** that function as prompts-to-the-engineering-team:

**1. The Minimum Reproducibility Disclosure (MRD) YAML schema (Table 4.3 / Appendix A)** — a machine-readable preamble that should accompany any memory-system evaluation. Verbatim fields:

```yaml
mrd_version: "0.1"
study_id: "<short-identifier>"
claim_type: ["capability_change", "freshness_related"]
temporal_governance:
  train:
    window: "YYYY-MM-DD..YYYY-MM-DD"
    snapshot_date: "YYYY-MM-DD"
    sources: ["<corpus1>", "<corpus2>"]
  index_or_session_store:
    snapshot_date: "YYYY-MM-DD"
    dedup_strategy: "<e.g., MinHash@J=0.85, URL+title exact>"
    update:
      last_time: "YYYY-MM-DDThh:mm:ssZ"
      frequency: "<e.g., daily | weekly | ad-hoc>"
  test:
    window: "YYYY-MM-DD..YYYY-MM-DD"
    snapshot_date: "YYYY-MM-DD"
    contamination_notes: "<potential benchmark leakage & mitigation>"
leakage_overlap_auditing:
  methods: ["<e.g., SimHash, BM25-topk cross-match>"]
  thresholds: {"near_dup_jaccard": 0.85}
  exclusion_criteria: "<rules applied>"
  impact_fraction:
    train∩test: 0.012
    train∩index: 0.034
    index∩test: 0.007
implementation_resources:
  model: { name: "<model-family>", checkpoint: "<hash/tag>", decoding_hparams: {temperature: 0.7, top_p: 0.95, max_new_tokens: 512}, random_seeds: [2024, 2025, 2026] }
  retrieval: { retriever_type: "<BM25 | DPR | ColBERT | hybrid>", k: 10, fusion_strategy: "<RRF@60 | concat-then-rerank>", reranker_type: "<Cross-Encoder-msmarco>" }
  hardware_cost: { accelerators: {"A100_80G": 8}, total_gpu_hours: 120.5, per_unit_cost_usd: 1.8 }
regimes:
  - name: "PO"
    shared_slice_with: ["Offline", "Online"]
  - name: "Offline"
  - name: "Online"
limitations_and_robustness:
  undisclosed_fields: ["<e.g., exact costs>"]
  reason: "<compliance | NDA | privacy>"
  sensitivity_analyses: ["<brief pointer to what was varied and the effect>"]
```

**2. The Edit/Forgetting Certificate (F1–F7, §5.4.4)** — a per-mutation record:

> **Target (F1):** fact/concept, sources, evidence links, snapshots.
> **Time (F2):** effective/expiry timestamps; time-window settings (AToKE).
> **Method (F3):** update/forgetting path (RAG/edit/PEFT/system-override) and constraints (AlphaEdit/WISE/ELKEN).
> **Verification (F4):** ESR ≈ 0.90, Locality ≈ 0.95, Drawdown ≤ 1–2%, Citation Coverage ≥ 0.80–0.90, Unsupported Claim ≤ 0.05–0.10, Recall@5 ≥ 0.80–0.90, Freshness ≥ 0.75–0.85; for forgetting evaluate along thoroughness–utility–scalability–sustainability.
> **Regression (F5):** long-form consistency (LEME), conflict/reversibility (ConflictEdit), out-of-template/domain generalization (EVOKE).
> **Rollback (F6):** rollback points/snapshots and impact-surface analysis; fallback via SERAC/RAG.
> **Audit (F7):** version IDs, operation logs, ownership/approval chain; alignment with NIST AI RMF / OWASP LLM Top-10.

**3. The Six-Step Decision Flow (§5.4.2)** — verbatim rubric for choosing among substrates:

> **S1** Identify timeliness and conflict. Knowledge highly time-sensitive / conflict-prone → external memory first (RAG/RETRO/kNN-LM or SERAC).
> **S2** Determine granularity of change. Small set of clear facts → parametric editing (ROME/MEND/MEMIT; pair with AlphaEdit/WISE for sequential cases; gray with SERAC before merging).
> **S3** Constrain consistency. Temporal evolution → time windows and versioned evidence (AToKE); multi-entity/constraints → event-level editing (ELKEN).
> **S4** Pre-register thresholds. ESR/Locality/Drawdown/Generalization (parametric), Citation Coverage/Unsupported Claim/Freshness/Recall@k (external/retrieval).
> **S5** Canary and online monitoring. Roll out with low traffic; track Citation Coverage, Unsupported Claim Rate, Recall@k/nDCG@k, Freshness, ESR/Locality/Drawdown.
> **S6** Rollback and evidence hardening. If thresholds exceeded, auto-degrade or rollback (index/edit); version and archive "fact–evidence–time-window" change records for audit.

## Citations

(Full structured array in frontmatter; first ~30 below as bullets — the rest are in the YAML `citations:` field.)

- [1] Vu et al. 2023 — **FreshLLMs**: refreshing LLMs with search engine augmentation. [arXiv:2310.03214](https://arxiv.org/abs/2310.03214)
- [2] Chen, Wang & Wang 2021 — **TimeQA**: dataset for time-sensitive QA. [arXiv:2108.06314](https://arxiv.org/abs/2108.06314)
- [3] Dhingra et al. 2022 — Time-aware language models as temporal KBs (TACL).
- [4] Tabassi 2023 — **NIST AI RMF 1.0** (anchor for the survey's audit framework).
- [5] OWASP Foundation 2023 — **OWASP Top 10 for LLM Applications** (the other audit anchor).
- [6] Petroni et al. 2019 — **LAMA probe**: language models as knowledge bases. [arXiv:1909.01066](https://arxiv.org/abs/1909.01066)
- [7] Petroni et al. 2021 — **KILT** benchmark. [arXiv:2009.02252](https://arxiv.org/abs/2009.02252)
- [8] Geva et al. 2021 — **FFN as key-value memories**. [arXiv:2012.14913](https://arxiv.org/abs/2012.14913)
- [9] Elhage et al. 2021 — A mathematical framework for transformer circuits.
- [11] Lewis et al. 2020 — **RAG** original paper. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
- [12] Guu et al. 2020 — **REALM**: retrieval-augmented LM pretraining. [arXiv:2002.08909](https://arxiv.org/abs/2002.08909)
- [13] Borgeaud et al. 2022 — **RETRO**: retrieving from trillions of tokens. [arXiv:2112.04426](https://arxiv.org/abs/2112.04426)
- [17] Saad-Falcon et al. 2024 — **ARES** automated RAG evaluation. [arXiv:2311.09476](https://arxiv.org/abs/2311.09476)
- [18] Ru et al. 2024 — **RAGChecker**. [arXiv:2408.08067](https://arxiv.org/abs/2408.08067)
- [19] Es et al. 2023 — **RAGAS**. [arXiv:2309.15217](https://arxiv.org/abs/2309.15217)
- [20] Friel, Belyi & Sanyal 2024 — **RAGBench** (TRACe framework). [arXiv:2407.11005](https://arxiv.org/abs/2407.11005)
- [21] Yang et al. 2024 — **CRAG** comprehensive RAG benchmark. [arXiv:2406.04744](https://arxiv.org/abs/2406.04744)
- [25] Fabbri et al. 2022 — **QAFactEval**. [arXiv:2112.08542](https://arxiv.org/abs/2112.08542)
- [26] Min et al. 2023 — **FActScore**. [arXiv:2305.14251](https://arxiv.org/abs/2305.14251)
- [31] Packer et al. 2024 — **MemGPT**. [arXiv:2310.08560](https://arxiv.org/abs/2310.08560) — see [[packer-2023-memgpt-os]]
- [42] Meng et al. 2023 — **ROME** locating + editing factual associations in GPT. [arXiv:2202.05262](https://arxiv.org/abs/2202.05262)
- [43] Mitchell et al. 2022 — **MEND** fast model editing at scale.
- [45] Meng et al. 2023 — **MEMIT** mass-editing memory in a transformer. [arXiv:2210.07229](https://arxiv.org/abs/2210.07229)
- [48] Shi et al. 2024 — **MUSE** machine unlearning six-way evaluation. [arXiv:2407.06460](https://arxiv.org/abs/2407.06460)
- [49] Maini et al. 2024 — **TOFU** fictitious unlearning. [arXiv:2401.06121](https://arxiv.org/abs/2401.06121)
- [63] Liu et al. 2023 — **Lost in the Middle**. [arXiv:2307.03172](https://arxiv.org/abs/2307.03172) — see [[liu-2023-lost-in-the-middle]]
- [65] Hsieh et al. 2024 — **RULER**. [arXiv:2404.06654](https://arxiv.org/abs/2404.06654)
- [66] Bai et al. 2024 — **LongBench**. [arXiv:2308.14508](https://arxiv.org/abs/2308.14508)
- [73] Wu et al. 2025 — **LongMemEval**. [arXiv:2410.10813](https://arxiv.org/abs/2410.10813)
- [97] Park et al. 2023 — **Generative Agents**. [arXiv:2304.03442](https://arxiv.org/abs/2304.03442)
- [99] Ge et al. 2025 — **TReMu** neuro-symbolic temporal reasoning. [arXiv:2502.09455](https://arxiv.org/abs/2502.09455)
- [110] Wang et al. 2024 — **WISE** lifelong model editing. [arXiv:2405.14768](https://arxiv.org/abs/2405.14768)
- [112] Maharana et al. 2024 — **LoCoMo** long-term conversational memory. [arXiv:2402.17753](https://arxiv.org/abs/2402.17753) — see [[maharana-2024-locomo]]
- [129] Hu, Wu, Liu & Sun 2023 — **EVOKE** evoking critical thinking abilities in LLMs.
- [131] Cohen et al. 2023 — **RIPPLEEDITS** evaluating ripple effects of knowledge editing.
- [173] Fang et al. 2025 — **AlphaEdit** null-space constrained editing. [arXiv:2410.02355](https://arxiv.org/abs/2410.02355)

_(Full 179-reference list captured in `citations:` frontmatter as structured JSON; only the most load-bearing entries are shown above as bullets.)_

## Related Digests

- [[patel-2026-engram]] — ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents *(the user's own ENGRAM framework — this survey maps directly onto ENGRAM's six dimensions)*
- [[du-2025-rethinking-memory]] — Rethinking Memory in LLM-based Agents: Representations, Operations, and Emerging Topics *(parallel taxonomy effort from a different research group)*
- [[li-2025-memos]] — MemOS: A Memory OS for AI System *(MemOS is exactly the "operating system" framing the survey aspires to — useful as a concrete instantiation)*
- [[liu-2023-lost-in-the-middle]] — Lost in the Middle: How Language Models Use Long Contexts *(canonical evidence for "visible ≠ usable" in the contextual-memory section)*
- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents *(the survey's anchor benchmark for procedural/episodic memory, E-MARS+ Panel P4)*
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems *(the "OS for memory" precedent the survey extends with DMM-Gov)*

## Reviewer Notes

**Hallucination check — severity: Clean.**

The digest text was cross-checked against the paper. All numerical claims (P@1 ≈ 74.5% for BERT-large on T-REx 1-to-1; r-ROME ~5000 sequential edits before collapse vs ROME failing within 100; nDCG@10 ≥ 0.7 as warning threshold; FActScore gain of ~14.2% at nDCG@5 > 0.75 vs >62% drop otherwise; illustrative deployment thresholds ESR ≈ 0.90 / Locality ≈ 0.95 / Drawdown ≤ 1–2% / Citation Coverage 0.80–0.90 / Unsupported Claim 0.05–0.10 / Recall@5 0.80–0.90 / Freshness 0.75–0.85) trace verbatim to §4.2.1, §4.2.2, §4.4.1, and §5.4.4 of the paper.

Specific method names were checked: ROME, MEND, MEMIT, SERAC, AlphaEdit, WISE, SEAL, LTE, AToKE, ELKEN, LEME, ConflictEdit/Pitfalls, EVOKE all appear in the survey with the attributions used here. The E-MARS+ five-panel acronym (Encode/Memorize–Attribute/Replay–Suppress/Freshness/Conflict–Stability–Cost) and the DMM-Gov six-step decision flow are quoted as defined in §4.5.3 and §5.4.2 respectively.

The framing additions in the digest — particularly the ENGRAM mapping, the Flow-OS-specific implications, and the "three things experts overlook" — are interpretive overlays added under the memory-architect lens, not claims attributed to the paper. They are marked as such in prose.

One minor framing call: the paper presents its 4-substrate taxonomy as novel; the digest characterises it as "largely a re-shuffle of prior literature." This is the digest's editorial judgment, anchored on the survey's own citations to Geva 2021, Lewis 2020, and Packer 2024 — the survey does not refute this framing but does claim its contribution is the operationalised definition + quadruple, which the digest also credits.

The figure caption attribution ("Figure 1: A unified framework for LLM memory research: mechanisms, evaluation, and governance") matches the PDF on page 3.

No hallucinated metrics, no fabricated citations, no invented method names detected. Severity: **Clean**.
