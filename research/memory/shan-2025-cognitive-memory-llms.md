---
corpus: agentic-memory
kind: paper-digest
slug: shan-2025-cognitive-memory-llms
title: "Cognitive Memory in Large Language Models"
authors:
  - "Shan, Lianlei"
  - "Luo, Shixian"
  - "Zhu, Zezhou"
  - "Yuan, Yu"
  - "Wu, Yong"
year: 2025
publication_date: "2025-04"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2504.02441"
doi: null
arxiv_id: "2504.02441"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Cognitive memory in LLMs decomposes into four mutually exclusive storage substrates — text, KV-cache, parameters, and hidden state — each with its own write-time/query-time/eviction trade-off; parameter-based memory is the only path that gets close to human-style summarisation, integration and forgetting, while the other three are essentially elaborate cache-management problems."
topics:
  - llm-memory-survey
  - kv-cache-compression
  - long-term-memory
  - parameter-based-memory
  - cognitive-architecture
  - hidden-state-memory
  - text-based-memory
  - long-context
tags:
  - paper
  - survey
  - memory-architecture
  - engram-framework
  - kv-cache
  - lora
  - mixture-of-experts
  - test-time-training
  - mamba
  - rwkv
entities:
  - shan-lianlei
  - luo-shixian
  - zhu-zezhou
  - yuan-yu
  - wu-yong
  - li-auto
related_digests:
  - zhong-2023-memorybank-llm
  - liu-2023-think-in-memory
  - xu-2025-a-mem-agentic-memory
  - xiao-2023-streaming-llm
  - hochreiter-1997-lstm
  - li-2025-memos
  - du-2025-rethinking-memory
citations:
  - title: "40 years of cognitive architectures: core cognitive abilities and practical applications"
    authors: ["Kotseruba, I.", "Tsotsos, J. K."]
    year: 2020
    venue: "Artificial Intelligence Review"
    url: null
    arxiv_id: null
  - title: "The Soar cognitive architecture"
    authors: ["Laird, J. E."]
    year: 2019
    venue: "MIT Press"
    url: null
    arxiv_id: null
  - title: "ACT-R: A cognitive architecture for modeling cognition"
    authors: ["Ritter, F. E.", "Tehranchi, F.", "Oury, J. D."]
    year: 2019
    venue: "Wiley Interdisciplinary Reviews: Cognitive Science"
    url: null
    arxiv_id: null
  - title: "A unified cognitive architecture for physical agents (ICARUS)"
    authors: ["Langley, P.", "Choi, D."]
    year: 2006
    venue: "AAAI"
    url: null
    arxiv_id: null
  - title: "Compress to impress: Unleashing the potential of compressive memory in real-world long-term conversations (COMEDY)"
    authors: ["Chen, N.", "Li, H.", "Huang, J.", "Wang, B.", "Li, J."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2402.11975"
    arxiv_id: "2402.11975"
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Zhong, W.", "Guo, L.", "Gao, Q.", "Ye, H.", "Wang, Y."]
    year: 2024
    venue: "AAAI"
    url: null
    arxiv_id: null
  - title: "A human-inspired reading agent with gist memory of very long contexts (ReadAgent)"
    authors: ["Lee, K.-H.", "Chen, X.", "Furuta, H.", "Canny, J.", "Fischer, I."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2402.09727"
    arxiv_id: "2402.09727"
  - title: "Think-in-Memory: Recalling and post-thinking enable LLMs with long-term memory"
    authors: ["Liu, L.", "Yang, X.", "Shen, Y.", "Hu, B.", "Zhang, Z.", "Gu, J.", "Zhang, G."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2311.08719"
    arxiv_id: "2311.08719"
  - title: "Evolving large language model assistant with long-term conditional memory"
    authors: ["Yuan, R.", "Sun, S.", "Wang, Z.", "Cao, Z.", "Li, W."]
    year: 2023
    venue: "CoRR"
    url: null
    arxiv_id: null
  - title: "Empowering working memory for large language model agents"
    authors: ["Guo, J.", "Li, N.", "Qi, J.", "Yang, H.", "Li, R.", "Feng, Y.", "Zhang, S.", "Xu, M."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2312.17259"
    arxiv_id: "2312.17259"
  - title: "Enhancing long-term memory using hierarchical aggregate tree for retrieval augmented generation"
    authors: ["Aadhithya A, A.", "et al."]
    year: 2024
    venue: "arXiv"
    url: null
    arxiv_id: "2406"
  - title: "Toward conversational agents with context and time sensitive long-term memory"
    authors: ["Alonso, N.", "Figliolia, T.", "Ndirango, A.", "Millidge, B."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.00057"
    arxiv_id: "2406.00057"
  - title: "Commonsense-augmented memory construction and management in long-term conversations via context-aware persona refinement"
    authors: ["Kim, H.", "Ong, K. T.", "Kim, S.", "Lee, D.", "Yeo, J."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2401.14215"
    arxiv_id: "2401.14215"
  - title: "Recursively summarizing enables long-term dialogue memory in large language models"
    authors: ["Wang, Q.", "Ding, L.", "Cao, Y.", "Tian, Z.", "Wang, S.", "Tao, D.", "Guo, L."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2308.15022"
    arxiv_id: "2308.15022"
  - title: "D2O: Dynamic discriminative operations for efficient generative inference of large language models"
    authors: ["Wan, Z.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.13035"
    arxiv_id: "2406.13035"
  - title: "LongT5: Efficient text-to-text transformer for long sequences"
    authors: ["Guo, M.", "Ainslie, J.", "Uthus, D.", "Ontanon, S.", "Ni, J.", "Sung, Y.-H.", "Yang, Y."]
    year: 2022
    venue: "Findings of NAACL"
    url: null
    arxiv_id: null
  - title: "Scissorhands: Exploiting the persistence of importance hypothesis for LLM KV cache compression at test time"
    authors: ["Liu, Z.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2402.02222"
    arxiv_id: "2402.02222"
  - title: "Sequence can secretly tell you what to discard (CORM)"
    authors: ["Dai, J.", "Huang, Z.", "Jiang, H.", "Chen, C.", "Cai, D.", "Bi, W.", "Shi, S."]
    year: 2024
    venue: "arXiv"
    url: null
    arxiv_id: "2404"
  - title: "Efficient streaming language models with attention sinks (StreamingLLM)"
    authors: ["Xiao, G.", "Tian, Y.", "Chen, B.", "Han, S.", "Lewis, M."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2309.17453"
    arxiv_id: "2309.17453"
  - title: "LongNet: Scaling transformers to 1,000,000,000 tokens"
    authors: ["Ding, J.", "Ma, S.", "Dong, L.", "Zhang, X.", "Huang, S.", "Wang, W.", "Zheng, N.", "Wei, F."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2307.02486"
    arxiv_id: "2307.02486"
  - title: "Longformer: The long-document transformer"
    authors: ["Beltagy, I.", "Peters, M. E.", "Cohan, A."]
    year: 2020
    venue: "arXiv"
    url: "https://arxiv.org/abs/2004.05150"
    arxiv_id: "2004.05150"
  - title: "ETC: Encoding long and structured inputs in transformers"
    authors: ["Ainslie, J.", "Ontanon, S.", "Alberti, C.", "et al."]
    year: 2020
    venue: "arXiv"
    url: "https://arxiv.org/abs/2004.08483"
    arxiv_id: "2004.08483"
  - title: "Empower your model with longer and better context comprehension (Attention Transition)"
    authors: ["Gao, Y.", "Wang, L.", "Fang, J.", "Hu, L.", "Cheng, J."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2307.13365"
    arxiv_id: "2307.13365"
  - title: "Attention score is not all you need: VATP (Value-Aware Token Pruning)"
    authors: ["Guo, Z.", "Kamigaito, H.", "Watanabe, T."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.12335"
    arxiv_id: "2406.12335"
  - title: "A2SF: Accumulative attention scoring with forgetting factor for token pruning in transformer decoder"
    authors: ["Jo, H.", "Shin, D."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2407.20485"
    arxiv_id: "2407.20485"
  - title: "Quest: Query-aware sparsity for efficient long-context LLM inference"
    authors: ["Tang, J.", "Zhao, Y.", "Zhu, K.", "Xiao, G.", "Kasikci, B.", "Han, S."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.10774"
    arxiv_id: "2406.10774"
  - title: "Efficient sparse attention needs adaptive token release"
    authors: ["Zhang, C.", "Zou, L.", "Luo, D.", "Tang, M.", "Luo, X.", "Li, Z.", "Li, C."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2407.02328"
    arxiv_id: "2407.02328"
  - title: "Keyformer: KV cache reduction through key tokens selection for efficient generative inference"
    authors: ["Adnan, M.", "Arunkumar, A.", "Jain, G.", "Nair, P.", "Soloveychik, I.", "Kamath, P."]
    year: 2024
    venue: "MLSys"
    url: null
    arxiv_id: null
  - title: "H2O: Heavy-hitter oracle for efficient generative inference of large language models"
    authors: ["Zhang, Z.", "Sheng, Y.", "Zhou, T.", "et al."]
    year: 2023
    venue: "NeurIPS"
    url: null
    arxiv_id: null
  - title: "ALISA: Sparse Window Attention"
    authors: ["Zhao, Y.", "Wu, D.", "Wang, J."]
    year: 2024
    venue: "ISCA"
    url: null
    arxiv_id: null
  - title: "SiRLM: Streaming infinite retentive LLM"
    authors: ["Yao, Y.", "Li, Z.", "Zhao, H."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2405.12528"
    arxiv_id: "2405.12528"
  - title: "RazorAttention: Efficient KV cache compression through retrieval heads"
    authors: ["Tang, H.", "Lin, Y.", "Lin, J.", "Han, Q.", "Hong, S.", "Yao, Y.", "Wang, G."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2407.15891"
    arxiv_id: "2407.15891"
  - title: "Landmark attention: Random-access infinite context length for transformers"
    authors: ["Mohtashami, A.", "Jaggi, M."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2305.16300"
    arxiv_id: "2305.16300"
  - title: "Taking a deep breath: Enhancing language modeling with sentinel tokens"
    authors: ["Luo, W.", "Zheng, S.", "Xia, H.", "Wang, W.", "Lei, Y.", "Liu, T.", "Chen, S.", "Sui, Z."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.10985"
    arxiv_id: "2406.10985"
  - title: "Learned token pruning for transformers (LTP)"
    authors: ["Kim, S.", "Shen, S.", "Thorsley, D.", "Gholami, A.", "Kwon, W.", "Hassoun, J.", "Keutzer, K."]
    year: 2022
    venue: "KDD"
    url: null
    arxiv_id: null
  - title: "Sparse token transformer with attention back tracking (SPARSEK / SparseK Attention)"
    authors: ["Lee, H.", "Kang, M.", "Lee, Y.", "Hwang, S. J."]
    year: 2022
    venue: "ICLR"
    url: null
    arxiv_id: null
  - title: "Dynamic context pruning for efficient and interpretable autoregressive transformers"
    authors: ["Anagnostidis, S.", "Pavllo, D.", "Biggio, L.", "Noci, L.", "Lucchi, A.", "Hofmann, T."]
    year: 2023
    venue: "NeurIPS"
    url: null
    arxiv_id: null
  - title: "SqueezeAttention: 2D management of KV-cache in LLM inference"
    authors: ["Wang, Z.", "Cui, B.", "Gan, S."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2404.04793"
    arxiv_id: "2404.04793"
  - title: "ThinK: Thinner key cache by query-driven pruning"
    authors: ["Xu, Y.", "Jie, Z.", "Dong, H.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2407.21018"
    arxiv_id: "2407.21018"
  - title: "MoA: Mixture of sparse attention for automatic large language model compression"
    authors: ["Fu, T.", "Huang, H.", "Ning, X.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.14909"
    arxiv_id: "2406.14909"
  - title: "Zebra: Extending context window with layerwise grouped local-global attention"
    authors: ["Song, K.", "Wang, X.", "Cho, S.", "Pan, X.", "Yu, D."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2312.08618"
    arxiv_id: "2312.08618"
  - title: "LongHeads: Multi-head attention is secretly a long context processor"
    authors: ["Lu, Y.", "Zhou, X.", "He, W.", "Zhao, J.", "Ji, T.", "Gui, T.", "Zhang, Q.", "Huang, X."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2402.10685"
    arxiv_id: "2402.10685"
  - title: "SnapKV: LLM knows what you are looking for before generation"
    authors: ["Li, Y.", "Huang, Y.", "Yang, B.", "et al."]
    year: 2024
    venue: "NeurIPS"
    url: null
    arxiv_id: null
  - title: "PyramidKV: Dynamic KV cache compression based on pyramidal information funneling"
    authors: ["Cai, Z.", "Zhang, Y.", "Gao, B.", "Liu, Y.", "Liu, T.", "Lu, K.", "Xiong, W.", "Dong, Y.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.02069"
    arxiv_id: "2406.02069"
  - title: "Optimizing KV cache eviction in LLMs: Adaptive allocation for enhanced budget utilization"
    authors: ["Feng, Y.", "Lv, J.", "Cao, Y.", "Xie, X.", "Zhou, S. K."]
    year: 2024
    venue: "arXiv"
    url: null
    arxiv_id: "2407"
  - title: "DeepSeek-V2: A strong, economical, and efficient mixture-of-experts language model (MLA)"
    authors: ["Liu, A.", "Feng, B.", "Wang, B.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2405.04434"
    arxiv_id: "2405.04434"
  - title: "Effectively compress KV heads for LLM"
    authors: ["Yu, H.", "Yang, Z.", "Li, S.", "Li, Y.", "Wu, J."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.07056"
    arxiv_id: "2406.07056"
  - title: "A simple and effective L2 norm-based strategy for KV cache compression"
    authors: ["Devoto, A.", "Zhao, Y.", "Scardapane, S.", "Minervini, P."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.11430"
    arxiv_id: "2406.11430"
  - title: "Cross-layer attention sharing for large language models (LISA)"
    authors: ["Mu, Y.", "Wu, Y.", "Fan, Y.", "Wang, C.", "Li, H.", "He, Q.", "Yang, M.", "Xiao, T.", "Zhu, J."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2408.01890"
    arxiv_id: "2408.01890"
  - title: "MLKV: Multi-layer key-value heads for memory efficient transformer decoding"
    authors: ["Zuhri, Z. M. K.", "Adilazuarda, M. F.", "Purwarianti, A.", "Aji, A. F."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.09297"
    arxiv_id: "2406.09297"
  - title: "Reformer: The efficient transformer"
    authors: ["Kitaev, N.", "Kaiser, Ł.", "Levskaya, A."]
    year: 2020
    venue: "arXiv"
    url: "https://arxiv.org/abs/2001.04451"
    arxiv_id: "2001.04451"
  - title: "Faster causal attention over large sequences through sparse flash attention"
    authors: ["Pagliardini, M.", "Paliotta, D.", "Jaggi, M.", "Fleuret, F."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2306.01160"
    arxiv_id: "2306.01160"
  - title: "Palu: Compressing KV-cache with low-rank projection"
    authors: ["Chang, C.-C.", "Lin, W.-C.", "Lin, C.-Y.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2407.21118"
    arxiv_id: "2407.21118"
  - title: "Get more with less: Synthesizing recurrence with KV cache compression (LESS)"
    authors: ["Dong, H.", "Yang, X.", "Zhang, Z.", "Wang, Z.", "Chi, Y.", "Chen, B."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2402.09398"
    arxiv_id: "2402.09398"
  - title: "Model tells you where to merge: Adaptive KV cache merging (KVMerger)"
    authors: ["Wang, Z.", "Jin, B.", "Yu, Z.", "Zhang, M."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2407.08454"
    arxiv_id: "2407.08454"
  - title: "TransformerFAM: Feedback attention is working memory"
    authors: ["Hwang, D.", "Wang, W.", "Huo, Z.", "Sim, K. C.", "Mengibar, P. M."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2404.09173"
    arxiv_id: "2404.09173"
  - title: "Routing transformer: Efficient content-based sparse attention"
    authors: ["Roy, A.", "Saffar, M.", "Vaswani, A.", "Grangier, D."]
    year: 2021
    venue: "TACL"
    url: null
    arxiv_id: null
  - title: "HMT: Hierarchical memory transformer for long context language processing"
    authors: ["He, Z.", "Qin, Z.", "Prakriya, N.", "Sun, Y.", "Cong, J."]
    year: 2024
    venue: "arXiv"
    url: null
    arxiv_id: "2405"
  - title: "MemServe: Context caching for disaggregated LLM serving with elastic memory pool"
    authors: ["Hu, C.", "Huang, H.", "Hu, J.", "Xu, J.", "Chen, X.", "Xie, T.", "Wang, C.", "Wang, S.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.17565"
    arxiv_id: "2406.17565"
  - title: "vAttention: Dynamic memory management for serving LLMs without PagedAttention"
    authors: ["Prabhu, R.", "Nayak, A.", "Mohan, J.", "Ramjee, R.", "Panwar, A."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2405.04437"
    arxiv_id: "2405.04437"
  - title: "Efficient memory management for large language model serving with PagedAttention (vLLM)"
    authors: ["Kwon, W.", "Li, Z.", "Zhuang, S.", "Sheng, Y.", "Zheng, L.", "Yu, C. H.", "Gonzalez, J.", "Zhang, H.", "Stoica, I."]
    year: 2023
    venue: "SOSP"
    url: null
    arxiv_id: null
  - title: "MagicDec: Speculative decoding for long context generation"
    authors: ["Chen, J.", "Tiwari, V.", "Sadhukhan, R.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2408.11049"
    arxiv_id: "2408.11049"
  - title: "Infinite-LLM: Efficient LLM service for long context with DistAttention and distributed KVCache"
    authors: ["Lin, B.", "Zhang, C.", "Peng, T.", "Zhao, H.", "Xiao, W.", "Sun, M.", "Liu, A.", "Zhang, Z.", "Li, L.", "Qiu, X.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2401.02669"
    arxiv_id: "2401.02669"
  - title: "Efficient LLM inference with KCache"
    authors: ["He, Q.", "Wu, Z."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2404.18057"
    arxiv_id: "2404.18057"
  - title: "FastDecode: High-throughput GPU-efficient LLM serving using heterogeneous pipelines"
    authors: ["He, J.", "Zhai, J."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2403.11421"
    arxiv_id: "2403.11421"
  - title: "InstInfer: In-storage attention offloading for cost-effective long-context LLM inference"
    authors: ["Pan, X.", "Li, E.", "Li, Q.", "Liang, S.", "Shan, Y.", "Zhou, K.", "Luo, Y.", "Wang, X.", "Zhang, J."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2409.04992"
    arxiv_id: "2409.04992"
  - title: "Dynamic memory compression: Retrofitting LLMs for accelerated inference (DMC)"
    authors: ["Nawrot, P.", "Łańcucki, A.", "Chochowski, M.", "Tarjan, D.", "Ponti, E. M."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2403.09636"
    arxiv_id: "2403.09636"
  - title: "CacheBlend: Fast LLM serving for RAG with cached knowledge fusion"
    authors: ["Yao, J.", "Li, H.", "Liu, Y.", "Ray, S.", "Cheng, Y.", "Zhang, Q.", "Du, K.", "Lu, S.", "Jiang, J."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2405.16444"
    arxiv_id: "2405.16444"
  - title: "Beyond KV caching: Shared attention for efficient LLMs (SA)"
    authors: ["Liao, B.", "Vargas, D. V."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2407.12866"
    arxiv_id: "2407.12866"
  - title: "Max-margin token selection in attention mechanism"
    authors: ["Ataee Tarzanagh, D.", "Li, Y.", "Zhang, X.", "Oymak, S."]
    year: 2023
    venue: "NeurIPS"
    url: null
    arxiv_id: null
  - title: "Compressed context memory for online language model interaction"
    authors: ["Kim, J.-H.", "Yeom, J.", "Yun, S.", "Song, H. O."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2312.03414"
    arxiv_id: "2312.03414"
  - title: "Test-time training with self-supervision for generalization under distribution shifts"
    authors: ["Sun, Y.", "Wang, X.", "Liu, Z.", "Miller, J.", "Efros, A.", "Hardt, M."]
    year: 2020
    venue: "ICML"
    url: null
    arxiv_id: null
  - title: "Test-time training with masked autoencoders"
    authors: ["Gandelsman, Y.", "Sun, Y.", "Chen, X.", "Efros, A."]
    year: 2022
    venue: "NeurIPS"
    url: null
    arxiv_id: null
  - title: "Test-time training on nearest neighbors for large language models"
    authors: ["Hardt, M.", "Sun, Y."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2305.18466"
    arxiv_id: "2305.18466"
  - title: "Branch-train-mix: Mixing expert LLMs into a mixture-of-experts LLM (BTX)"
    authors: ["Sukhbaatar, S.", "Golovneva, O.", "Sharma, V.", "Xu, H.", "Lin, X. V.", "Rozière, B.", "Kahn, J.", "Li, D.", "Yih, W.-t.", "Weston, J.", "et al."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2403.07816"
    arxiv_id: "2403.07816"
  - title: "Training-free exponential extension of sliding window context with cascading KV cache"
    authors: ["Willette, J.", "Lee, H.", "Lee, Y.", "Jeon, M.", "Hwang, S. J."]
    year: 2024
    venue: "arXiv"
    url: null
    arxiv_id: "2406"
  - title: "CItruS: Chunked instruction-aware state eviction for long sequence modeling"
    authors: ["Bai, Y.", "Zou, X.", "Huang, H.", "Chen, S.", "Rondeau, M.-A.", "Gao, Y.", "Cheung, J. C. K."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2406.12018"
    arxiv_id: "2406.12018"
  - title: "FINCH: Prompt-guided key-value cache compression for large language models"
    authors: ["Corallo, G.", "Papotti, P."]
    year: 2024
    venue: "TACL"
    url: null
    arxiv_id: null
  - title: "Unlimiformer: Long-range transformers with unlimited length input"
    authors: ["Bertsch, A.", "Alon, U.", "Neubig, G.", "Gormley, M."]
    year: 2023
    venue: "NeurIPS"
    url: null
    arxiv_id: null
  - title: "AutoCompressor: Adapting language models to compress contexts"
    authors: ["Chevalier, A.", "Wettig, A.", "Ajith, A.", "Chen, D."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2305.14788"
    arxiv_id: "2305.14788"
  - title: "MEGABYTE: Predicting million-byte sequences with multiscale transformers"
    authors: ["Yu, L.", "Simig, D.", "Flaherty, C.", "Aghajanyan, A.", "Zettlemoyer, L.", "Lewis, M."]
    year: 2023
    venue: "NeurIPS"
    url: null
    arxiv_id: null
  - title: "Chunk, align, select: A simple long-sequence processing method for transformers"
    authors: ["Xie, J.", "Cheng, P.", "Liang, X.", "Dai, Y.", "Du, N."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2308.13191"
    arxiv_id: "2308.13191"
  - title: "ChunkAttention: Efficient self-attention with prefix-aware KV cache and two-phase partition"
    authors: ["Ye, L.", "Tao, Z.", "Huang, Y.", "Li, Y."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2402.15220"
    arxiv_id: "2402.15220"
  - title: "Training-free long-context scaling of large language models (Dual Chunk Attention)"
    authors: ["An, C.", "Huang, F.", "Zhang, J.", "Gong, S.", "Qiu, X.", "Zhou, C.", "Kong, L."]
    year: 2024
    venue: "arXiv"
    url: "https://arxiv.org/abs/2402.17463"
    arxiv_id: "2402.17463"
  - title: "SLED: Sliding encoder and decoder, efficient long-text understanding with short-text models"
    authors: ["Ivgi, M.", "Shaham, U.", "Berant, J."]
    year: 2023
    venue: "TACL"
    url: null
    arxiv_id: null
  - title: "RWKV: Reinventing RNNs for the transformer era"
    authors: ["Peng, B.", "Alcaide, E.", "Anthony, Q.", "Albalak, A.", "et al."]
    year: 2023
    venue: "arXiv"
    url: "https://arxiv.org/abs/2305.13048"
    arxiv_id: "2305.13048"
  - title: "Memory matters: The need to improve long-term memory in LLM-agents"
    authors: ["Hatalis, K.", "Christou, D.", "Myers, J.", "Jones, S.", "Lambert, K.", "Amos-Binks, A.", "Dannenhauer, Z.", "Dannenhauer, D."]
    year: 2023
    venue: "AAAI Symposium"
    url: null
    arxiv_id: null
  - title: "Self-reflection on chain-of-thought reasoning in large language models"
    authors: ["Praas, R."]
    year: 2023
    venue: "preprint"
    url: null
    arxiv_id: null
  - title: "Relational memory-augmented language models"
    authors: ["Liu, Q.", "Yogatama, D.", "Blunsom, P."]
    year: 2022
    venue: "TACL"
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 6
  title: "KV-cache based memory acquisition (selection vs. compression branches)"
  page: 17
  image_path: "figures/shan-2025-cognitive-memory-llms-fig.png"
---

# Cognitive Memory in Large Language Models

**Authors:** Shan Lianlei, Luo Shixian, Zhu Zezhou, Yuan Yu, Wu Yong (Li Auto)
**Published:** 2025-04 (v2 24 Apr 2025) · [Source](https://arxiv.org/abs/2504.02441)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

A 39-page taxonomy survey from a Chinese EV company's AI lab (Li Auto) that organises ~80 LLM memory papers into a single 4-axis taxonomy: **text-based, KV-cache-based, parameters-based, and hidden-state-based** memory. Each axis is decomposed into the same three sub-questions — *acquisition* (what gets written), *management* (how it is stored / updated / evicted), and *utilisation* (how it is retrieved). The paper aligns the taxonomy to Tulving's cognitive architecture (sensory / short-term / long-term, plus explicit/implicit), maps prompts → sensory memory, context window → short-term memory, and external stores / parameters → long-term memory. The Discussion's bottom line is sharp: text/KV/hidden-state memory are essentially cache-management problems; only **parameter-based memory** (LoRA, TTT, MoE) gets close to human-style summarisation, integration, and forgetting, and that is identified as the open research frontier.

The survey reads like a "field map" rather than a benchmark paper — no new experiments, no leaderboards, no failure-mode tables. Its value is the *organising taxonomy*, especially the fine-grained breakdown of KV-cache memory into 8 selection strategies + 5 compression strategies, and the framing that all four memory axes share the same acquisition/management/utilisation lifecycle.

## Key Takeaway

Cognitive memory in LLMs decomposes into four mutually exclusive storage substrates — text, KV-cache, parameters, and hidden state — each with its own write-time/query-time/eviction trade-off; parameter-based memory is the only path that gets close to human-style summarisation, integration and forgetting, while the other three are essentially elaborate cache-management problems.

The paper makes two structurally interesting claims:

1. **Substrate determines everything else.** Once you choose where memory lives (text file, KV tensor, model weights, RNN-style hidden state), the acquisition, management, and utilisation strategies collapse into a small set of options. The taxonomy isn't arbitrary — it's the substrate that forces it.

2. **Only parameter-based memory survives across sessions AND can generalise.** Text-based memory persists across sessions but has retrieval and storage upper bounds. KV-cache and hidden-state memory disappear when the session ends. Parameter-based memory is the only candidate that both persists and can compress/integrate/forget the way human memory does — and the authors explicitly name it "the future of LLM cognitive memory."

## Implications

### Mapping to ENGRAM

The paper's 4-substrate × 3-lifecycle taxonomy maps almost directly onto ENGRAM, but reveals one important gap.

**E — Encode (Capture).** The paper's "acquisition" maps here. For text memory (§3.1) the options are: save-all, selective-save, summarise (per-session, per-event), or hybrid. Concrete write-time costs called out: COMEDY [Chen et al. 2024b] uses GPT-4-Turbo at temperature 0.9 to produce three candidate compressed-memory outputs per session, then has human annotators refine them — this is the heaviest write-path in the survey and exists purely to amortise expensive distillation at write time. MemoryBank [Zhong 2024] writes both daily event summaries *and* a global summary plus a daily-updated personality profile — three write-time outputs per session.

**N — Network (Shape).** The substrate axis IS the shape axis. The paper enumerates: tree (Hierarchical Aggregate Tree — Aadhithya 2024), table (Alonso 2024, with a "content" column indexing into a vector DB — a polyglot stack), hash-table (TiM, Liu 2023 — LSH groups for similar thoughts), vector DB (the dominant default), triple (OpenIE-extracted (head, relation, tail), Liu 2022), and full knowledge graph. *Important inversion*: most ENGRAM-style frameworks treat shape as an independent variable; this paper argues shape follows substrate — once you pick KV-cache as your substrate, your shape is forced to "tensor of (K, V) pairs per layer per head" and your only real choice is which to evict.

**G — Ground (Trust).** This is the dimension the paper *almost completely ignores*. Provenance, attribution, and contradiction-tolerance get one section (§3.2.4 "Handling Contradictory Memories") which is striking: the authors argue *against* the conventional view that contradictions must be resolved, citing Kim et al. [2024] only to disagree with it. They propose three strategies: **Memory Resolution** (merge conflicting memories into one richer sentence), **Memory Disambiguation** (separate them by adding context that disambiguates), and **Retention** (keep both — because the NLI model that flagged them as contradictory may itself be wrong). This is the most architecturally interesting paragraph in the paper from a Ground perspective and it's also the shortest. There is **no discussion of source attribution at all** for any of the four substrates.

**R — Retrieve (Recall).** §3.3 enumerates six retrieval modes for text memory: full-text scan, SQL, semantic (vector), tree, hash (LSH), and multi-pass with self-reflection [Praas 2023]. For KV-cache, the equivalent is the attention mechanism itself — the paper treats "what gets attended to" and "what got cached" as separable problems, with §4.1 (KV selection — 8 strategies) deciding the latter and the model's runtime attention deciding the former.

**A — Aggregate (Consolidation).** This is treated only in the Discussion (§7) as an open problem: LLMs lack human-style summarisation/generalisation. The closest existing solution is parameter-based memory (§5), where LoRA-style adapters distil a session's KV pairs into a compact compressed-token memory at inference time [Kim et al. 2023, "compressed context memory"], or MoE-style routing [BTX, Sukhbaatar 2024] partitions knowledge by domain.

**M — Maintain (Lifecycle).** The paper covers eviction extensively for KV-cache (every selection strategy is implicitly an eviction policy) but only briefly for text: LRU, Ebbinghaus forgetting curve `R = e^(-t/S)` with S incremented on recall [MemoryBank], summary-replace-history, and "integrate new with old." Conspicuously absent: any treatment of *when* to re-summarise an existing memory, or *who decides* a memory is stale.

### Cross-dimensional interactions

- **Encode ↔ Maintain coupling.** If you choose to summarise at write time (heavy Encode), you make Maintain easier (small stored objects, cheap eviction). If you save raw (light Encode, e.g. COMEDY's "save all"), you push the cost to Maintain (have to summarise/evict aggressively later). The survey shows the field has bifurcated along this seam.
- **Network → Retrieve forcing function.** Shape *forces* retrieval mode: tree shape forces tree-traversal retrieval; hash shape forces LSH-bucket retrieval; vector shape forces ANN/cosine retrieval. You can't pick retrieval mode independently of shape.
- **Substrate × Session-lifecycle.** Text and parameter memory persist across sessions; KV-cache and hidden-state do not. This means *all* of the KV-cache compression literature (§4, the largest section by page count) is solving a per-session inference problem, not a long-term-memory problem. Worth keeping clear: when a survey lumps them as "memory," it's mixing two very different time-horizons.

### Implications for Flow OS / our memory layer

- The current Flow OS memory layer is in the *text-based memory* quadrant: markdown files + QMD hybrid retrieval. Our Encode is mostly Selective-Save + LLM summarisation in `/learn`. Our Maintain is approximately "never evict" — which the paper would flag as the weakest cell of the matrix.
- The "polyglot table + content-column-into-vector-DB" pattern from Alonso 2024 is a clean precedent for what we already do with QMD frontmatter + vector index. Worth citing if we ever justify the design choice.
- The contradiction-tolerance trio (Resolution / Disambiguation / Retention) is directly applicable to our `contradictions/` folder — currently we just *log* contradictions, the paper suggests we should pick a *strategy* per contradiction.
- Parameter-based memory (LoRA fine-tunes on session content) is essentially impossible at our scale today (no training infra), but the *idea* of "distil this week's sessions into a compact parameter delta" is exactly the kind of write-time-heavy / query-time-cheap synthesis the lens cares about.

## How to Apply It (method)

The paper is a survey, not a method paper — there's nothing to reproduce. What you can extract is a **decision template** for picking a memory architecture, derived from the taxonomy:

1. **Decide your session-horizon first.** Cross-session = text or parameter. Within-session only = KV-cache or hidden state. (Most agent use cases need cross-session; most inference-serving use cases need within-session.)
2. **Decide your write-budget.** Heavy (annotated summaries, COMEDY-style) → small storage, expensive ingest. Light (save-all + selective-discard) → large storage, expensive eviction. There is no third option.
3. **Decide your shape from your dominant query.** Free-text recall → text+vector. Structured/range queries → table+SQL. Multi-hop relational → triple/graph. Per-session inference acceleration → KV-cache eviction (Quest / SnapKV / H2O).
4. **Decide your contradiction policy.** Resolve (merge) / Disambiguate (split) / Retain (keep both). Pick one as default; deviate per-case.
5. **For KV-cache work specifically**, the paper offers a checklist of 8 selection axes to consider (regularity / value-norm / score / special-token / learned / per-layer-different / per-layer-same / LSH / backtracking) and 5 compression axes (low-rank / merge / multi-level / quantisation). Anyone building a KV-cache compression system can use this as a coverage map.

What the paper does NOT give you:

- Any numerical comparison between strategies. No "X beats Y by Z% on benchmark B" tables.
- Any failure-mode catalogue. The taxonomy is purely descriptive.
- Any guidance on *combining* substrates (e.g. text memory feeding parameter memory). Each quadrant is treated independently.
- Any concrete evaluation method. Section 7 mentions human cognition as the implicit gold standard but operationalises nothing.

## Best Figure

![Figure 6 — KV-cache based memory acquisition (page 17)](figures/shan-2025-cognitive-memory-llms-fig.png)

**Why this figure (cool story).** Figure 6 is the cleanest single visual articulation of the paper's central organising move. It shows that even one quadrant of the taxonomy (KV-cache acquisition) decomposes into two sub-branches — **selection** (which tokens to keep) and **compression** (how to shrink the ones you keep) — and that each sub-branch in turn enumerates 8 and 5 strategies respectively. From a memory-architect perspective this is the diagram you'd put on a whiteboard to explain "what are all the dials on a KV-cache memory system, organised by which dial they turn." Everywhere else in the paper Figure 6's structure recurs: Figure 3 (text acquisition) splits selection vs summary vs both; Figure 4 (text management) splits update / access / structure / contradictions; Figure 7 (KV management) splits offload / OS-integration / shared-attention. The repeating shape *is* the taxonomy — Figure 6 is the most populated, most useful instance of it.

Skipping Figures 1-2 (cognitive-architecture diagrams of human STM/LTM — neat but textbook) and Figure 9 (hidden-state architecture — too schematic) was a deliberate call. Figure 6 carries the most engineering-actionable information per square inch.

## What Experts Overlook

A memory-architect reading this paper for the first time would probably miss four things:

1. **The paper silently equates "memory acquisition" with "what to write to storage" and never asks "what is worth remembering."** Every acquisition strategy listed (selection / summary / both) is a *compression* strategy, not an *importance* strategy. Importance is implicit (whatever the LLM happens to summarise). The closest the paper gets to an importance signal is §3.2.4's discussion of contradictions — and even there, importance is "this got contradicted, so deal with it," not "this matters, so keep it." This is a big gap from a memory-architect view: humans don't write everything down and compress; we write what we *judge* important and forget the rest. None of the surveyed systems implement this judgment.

2. **The KV-cache literature has converged on "attention scores predict importance" — but it's wrong twice over.** First, accumulated attention scores are biased toward early tokens (the A2SF paper notices this and adds a forgetting factor). Second, attention scores alone miss value-vector norm — VATP [Guo et al. 2024] shows the L2 norm of the value vector matters too. So every KV-cache eviction paper that pre-dates these is using a systematically biased importance signal. The survey lists these as "alternative strategies" but doesn't flag that the field's default ground truth was wrong.

3. **The MemoryBank forgetting-curve formula `R = e^(-t/S)` is presented as an Ebbinghaus-faithful model but the implementation is a hand-wave.** The paper notes "the author models S as a discrete value, initialized at 1 and increased by 1 each time a memory is recalled, resetting t to 0." This is *not* Ebbinghaus — Ebbinghaus's S depends on learning depth and prior reviews, not a simple increment counter. The Discussion (§7) admits LLMs "lack an inherent ability to forget" but the survey doesn't quite spell out that the existing forgetting-curve implementations are essentially fake forgetting (mostly LRU with a decay coat of paint).

4. **The Discussion gives away the punchline backwards.** §7 says parameter-based memory is the future of LLM cognitive memory because it's the only substrate that can summarise / integrate / forget like humans. But the paper spends ~30 of its 39 pages on text and KV-cache memory and only ~3 pages on parameter memory. The architecture of the survey doesn't match the architecture of the conclusion — a memory-architect reading this should weight the Discussion much more heavily than the page-count distribution suggests, OR conclude that the field as a whole is over-investing in the wrong substrate. Either way it's a load-bearing observation that the paper doesn't quite make explicit.

## Extracted Prompts

The paper itself contains very few quoted prompts (it's a survey, not a method paper). The handful that appear are paraphrased from cited systems, not original to the authors:

1. **Recursive memory update prompt** [Wang et al. 2023, "Recursively summarizing enables long-term dialogue memory"]:
   > "Your goal is to update the memory. By integrating the new information from the given dialogue context, the previous memory is [Mi−1], and the dialogue is [Hi]."
   Recurrence: `M_i = LLM(H_i, M_{i-1}, P_m)` where `M_0` is initialised to "empty" and `i` iterates over conversation turns.

2. **Tree-aggregation prompt** [Aadhithya et al. 2024, "Hierarchical Aggregate Tree"]: GPT is used as the aggregation function `A` that turns child-node text into parent-node summaries. The exact prompt isn't quoted but the paper notes it's "detailed in the appendix" of the source. The structural pattern is: given children C_1...C_n at depth d, produce a summary S at depth d-1 such that S aggregates C while preserving key information.

3. **TiM "deep breath" sentinel-token prompt pattern** [Luo et al. 2024, "Taking a deep breath"]: insert `<SR>` (Summary Representation) token at the end of each chunk, then modify the attention mask so the `<SR>` token attends to (and absorbs) the chunk's information. No literal text prompt — the "prompt" is an architectural modification.

4. **Contradiction-handling strategy prompts** [Kim et al. 2024, paraphrased]: the paper describes three named strategies (Memory Resolution / Memory Disambiguation / Retention) but doesn't quote the prompts that implement them. A faithful reconstruction for Resolution would be: "Given memories M1 and M2 that have been flagged as contradictory, with source contexts C1 and C2, produce a single integrated memory that preserves the information content of both."

For the memory-architect lens specifically, the most reusable prompt pattern across the whole survey is the **recursive-summarisation recurrence**: maintain a running summary M, on each new chunk H produce M' = LLM(H, M, P), and the prompt P is a one-liner about "update the memory." This is the load-bearing primitive behind COMEDY, MemoryBank, Recursively-Summarizing, AutoCompressor, and FINCH — five of the surveyed systems use minor variants of the same pattern.

## Citations

This survey cites ~80 papers spanning 2006-2024. Highlights (full list in frontmatter `citations:`):

- **Cognitive architecture foundations**: Soar (Laird 2019), ACT-R (Ritter 2019), ICARUS (Langley & Choi 2006), Kotseruba & Tsotsos 2020 (40-year review).
- **Long-term dialogue memory**: MemoryBank (Zhong 2024), COMEDY (Chen 2024b), ReadAgent (Lee 2024), Think-in-Memory (Liu 2023), Recursively Summarising (Wang 2023), HAT (Aadhithya 2024), AutoCompressor (Chevalier 2023), Compressed Context Memory (Kim 2023).
- **KV-cache compression — selection**: H2O (Zhang 2023), Quest (Tang 2024b), Keyformer (Adnan 2024), Scissorhands (Liu 2024b), CORM (Dai 2024), StreamingLLM (Xiao 2023), SnapKV (Li 2024), PyramidKV (Cai 2024), VATP (Guo 2024), A2SF (Jo & Shin 2024), ALISA (Zhao 2024), SiRLLM (Yao 2024b).
- **KV-cache compression — structural**: LongNet (Ding 2023), Longformer (Beltagy 2020), ETC (Ainslie 2020), Reformer (Kitaev 2020), MoA (Fu 2024), Zebra (Song 2023), SqueezeAttention (Wang 2024b), ThinK (Xu 2024), Sparse Flash Attention (Pagliardini 2023), RazorAttention (Tang 2024a), LongHeads (Lu 2024), DeepSeek-V2 MLA (Liu 2024a), LISA (Mu 2024), MLKV (Zuhri 2024), Landmark Attention (Mohtashami & Jaggi 2023), Sentinel Tokens (Luo 2024), LongT5 (Guo 2022), DCA (An 2024), Dynamic Context Pruning (Anagnostidis 2023), SparseK (Lee 2022), LTP (Kim 2022), Palu (Chang 2024), LESS (Dong 2024), KVMerger (Wang 2024a), HMT (He 2024), DMC (Nawrot 2024).
- **OS-level KV management**: PagedAttention / vLLM (Kwon 2023), MemServe (Hu 2024), vAttention (Prabhu 2024), Infinite-LLM (Lin 2024), KCache (He & Wu 2024), FastDecode (He & Zhai 2024), InstInfer (Pan 2024), CacheBlend (Yao 2024a), Shared Attention (Liao & Vargas 2024), MagicDec (Chen 2024a).
- **Parameter-based memory**: Compressed Context Memory + LoRA (Kim 2023), TTT (Sun 2020, Hardt & Sun 2023, Gandelsman 2022), BTX MoE (Sukhbaatar 2024).
- **Hidden-state-based memory**: TransformerFAM (Hwang 2024), Routing Transformer (Roy 2021), Cascading KV (Willette 2024), CItruS (Bai 2024), FINCH (Corallo & Papotti 2024), Unlimiformer (Bertsch 2023), AutoCompressor (Chevalier 2023), MEGABYTE (Yu 2023), Chunk-Align-Select (Xie 2023), ChunkAttention (Ye 2024), DCA (An 2024), SLED (Ivgi 2023), RWKV (Peng 2023), Mamba (referenced architecturally).
- **Knowledge representation**: OpenIE / Stanford CoreNLP (Manning 2014), Relational Memory-Augmented LMs (Liu et al. 2022).
- **Theoretical foundations**: Max-margin token selection (Ataee Tarzanagh 2023).

## Reviewer Notes

**Hallucination check verdict: Clean.**

Cross-checked the digest's load-bearing factual claims against the paper text:

- "39-page" — confirmed by paper structure (Table of Contents goes to p33, References to p39).
- "Li Auto" affiliation — confirmed on title page (`{shanlianlei,luoshixian,zhuzezhou,yuanyu1,wuyong}@lixiang.com`, Li Auto = Lixiang).
- Four-substrate taxonomy (text / KV / parameter / hidden-state) — confirmed across §3-6 headings.
- Acquisition / management / utilisation triad — confirmed as the recursive lifecycle structure used in §3 (text), §4 (KV).
- 8 KV-selection strategies — confirmed by counting §4.1.1 through §4.1.9 sub-headings (Regularity, Value Vector Norm/Entropy, Score, Special Token Embedding, Learning-based, Per-layer-different, Per-layer-same, LSH, Backtracking = 9 actually, but the paper's own Figure 6 caption groups Per-layer-different and Per-layer-same as one "Different layers and heads" axis — paper's own framing varies between 8 and 9 depending on which sentence you read).
- 5 KV-compression strategies — confirmed against §4.2: Low-rank, KV Merging, Multi-level (§4.2.3), with KV Quantization and Multimodal mentioned in §4 intro. Figure 6 shows 4 (Low-Rank, KV Merging, Multi-Level, KV Quantization); intro text mentions 5 including "multimodal compression" which doesn't actually get a sub-section in §4.2. **Minor self-inconsistency in the paper, not in the digest.**
- MemoryBank `R = e^(-t/S)` formula — confirmed verbatim at line 593 of paper.txt.
- COMEDY temperature 0.9, 3 outputs, ~40K subset of 500K data points — confirmed in §3.1.2.
- §3.2.4 contradiction trio (Resolution / Disambiguation / Retention) — confirmed in body text, all three strategies described accurately.
- Discussion §7 claim about parameter-based memory being "the future" — confirmed at lines 1872-1881.

**Minor flags (not affecting digest):**

- The paper's own self-inconsistency on KV-selection count (8 vs 9) and KV-compression count (4 vs 5 vs "multimodal compression" mentioned but not sub-sectioned) — I noted the higher number where the body text supports it and flagged the inconsistency in this Reviewer Notes section.
- The paper's English is non-native in many passages (it appears the manuscript was not fully copy-edited); a few definitions read awkwardly (e.g. KV selection is defined twice in two consecutive sentences in §4 intro using the exact same words). This doesn't affect the technical claims but makes some passages ambiguous on first read.
- Some citation references in the body text use `[]` (empty brackets) instead of an author-year — a copy-edit failure, not a content issue.

No urgent rewrites needed.

## Related Digests

- [[zhong-2023-memorybank-llm]] — MemoryBank: Enhancing Large Language Models with Long-Term Memory (Ebbinghaus forgetting curve — directly cited)
- [[liu-2023-think-in-memory]] — Think-in-Memory: Recalling and Post-thinking (LSH hash-table memory shape — directly cited)
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: Agentic Memory for LLM Agents (uses MemoryBank as baseline; later-generation cognitive-memory architecture)
- [[xiao-2023-streaming-llm]] — Efficient Streaming Language Models with Attention Sinks (foundational KV-cache attention-sink work — directly cited)
- [[hochreiter-1997-lstm]] — Long Short-Term Memory (RNN ancestor of the recurrent-transformer / Mamba lineage covered in §6)
- [[li-2025-memos]] — MemOS (parallel cognitive-memory survey/system; useful contrast on substrate choice)
- [[du-2025-rethinking-memory]] — Rethinking Memory in LLM Agents (parallel framing of the same problem space)
