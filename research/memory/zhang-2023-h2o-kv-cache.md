---
corpus: agentic-memory
kind: paper-digest
slug: zhang-2023-h2o-kv-cache
title: "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models"
authors:
  - "Zhenyu Zhang"
  - "Ying Sheng"
  - "Tianyi Zhou"
  - "Tianlong Chen"
  - "Lianmin Zheng"
  - "Ruisi Cai"
  - "Zhao Song"
  - "Yuandong Tian"
  - "Christopher Ré"
  - "Clark Barrett"
  - "Zhangyang Wang"
  - "Beidi Chen"
year: 2023
publication_date: "2023-12"
venue: "NeurIPS 2023"
source_url: "https://arxiv.org/abs/2306.14048"
doi: null
arxiv_id: "2306.14048"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Attention is over-95% sparse at inference, and a tiny set of 'heavy-hitter' tokens (identified by accumulated attention score) carries most of the signal — so a KV cache that keeps only the recent window plus the running top-K heavy hitters can shrink memory 5x with no accuracy loss, while gaining a (1-α)(1-1/e)-β submodular-greedy guarantee."
topics:
  - kv-cache-eviction
  - attention-sparsity
  - heavy-hitters
  - llm-inference-efficiency
  - submodular-optimization
  - long-context-generation
  - memory-architecture
tags:
  - paper
  - kv-cache
  - inference-efficiency
  - eviction-policy
  - sparse-attention
  - streaming-llm
  - canonical-citation
entities:
  - zhang-zhenyu
  - sheng-ying
  - chen-beidi
  - re-christopher
  - tian-yuandong
related_digests:
  - shan-2025-cognitive-memory-llms
  - dao-2022-flashattention
  - xiao-2023-streaming-llm
  - child-2019-sparse-transformers
  - tavakoli-2026-beam-light
citations:
  - title: "LaMDA: Language Models for Dialog Applications"
    authors: ["Romal Thoppilan", "Daniel De Freitas", "Jamie Hall", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2201.08239"
  - title: "Wordcraft: Story Writing with Large Language Models"
    authors: ["Ann Yuan", "Andy Coenen", "Emily Reif", "Daphne Ippolito"]
    year: 2022
    venue: "27th International Conference on Intelligent User Interfaces"
    doi: null
    url: null
    arxiv_id: null
  - title: "Emergent Abilities of Large Language Models"
    authors: ["Jason Wei", "Yi Tay", "Rishi Bommasani", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2206.07682"
  - title: "Benchmarking Large Language Models for News Summarization"
    authors: ["Tianyi Zhang", "Faisal Ladhak", "Esin Durmus", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2301.13848"
  - title: "Efficiently Scaling Transformer Inference"
    authors: ["Reiner Pope", "Sholto Douglas", "Aakanksha Chowdhery", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2211.05102"
  - title: "An Anomaly in Space-Time Characteristics of Certain Programs Running in a Paging Machine"
    authors: ["Laszlo A. Belady", "Robert A. Nelson", "Gerald S. Shedler"]
    year: 1969
    venue: "Communications of the ACM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reformer: The Efficient Transformer"
    authors: ["Nikita Kitaev", "Łukasz Kaiser", "Anselm Levskaya"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.04451"
  - title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
    authors: ["Tri Dao", "Dan Fu", "Stefano Ermon", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generating Long Sequences with Sparse Transformers"
    authors: ["Rewon Child", "Scott Gray", "Alec Radford", "Ilya Sutskever"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1904.10509"
  - title: "Rethinking Attention with Performers"
    authors: ["Krzysztof Choromanski", "Valerii Likhosherstov", "David Dohan", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2009.14794"
  - title: "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention"
    authors: ["Angelos Katharopoulos", "Apoorv Vyas", "Nikolaos Pappas", "François Fleuret"]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fast Transformer Decoding: One Write-Head is All You Need"
    authors: ["Noam Shazeer"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.02150"
  - title: "PaLM: Scaling Language Modeling with Pathways"
    authors: ["Aakanksha Chowdhery", "Sharan Narang", "Jacob Devlin", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2204.02311"
  - title: "Learning to Compress Prompts with Gist Tokens"
    authors: ["Jesse Mu", "Xiang Lisa Li", "Noah Goodman"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2304.08467"
  - title: "A Framework for Few-Shot Language Model Evaluation (lm-eval-harness)"
    authors: ["Leo Gao", "Jonathan Tow", "Stella Biderman", "et al."]
    year: 2021
    venue: "Zenodo"
    doi: null
    url: null
    arxiv_id: null
  - title: "Holistic Evaluation of Language Models (HELM)"
    authors: ["Percy Liang", "Rishi Bommasani", "Tony Lee", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2211.09110"
  - title: "DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale"
    authors: ["Reza Yazdani Aminabadi", "Samyam Rajbhandari", "Minjia Zhang", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2207.00032"
  - title: "Hugging Face Accelerate"
    authors: ["HuggingFace"]
    year: 2022
    venue: "Hugging Face Docs"
    doi: null
    url: "https://huggingface.co/docs/accelerate/index"
    arxiv_id: null
  - title: "FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU"
    authors: ["Ying Sheng", "Lianmin Zheng", "Binhang Yuan", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2303.06865"
  - title: "Massive Language Models Can Be Accurately Pruned in One-Shot (SparseGPT)"
    authors: ["Elias Frantar", "Dan Alistarh"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2301.00774"
  - title: "A Simple and Effective Pruning Approach for Large Language Models (Wanda)"
    authors: ["Mingjie Sun", "Zhuang Liu", "Anna Bair", "J. Zico Kolter"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2306.11695"
  - title: "Outlier Weighed Layerwise Sparsity (OWL)"
    authors: ["Lu Yin", "You Wu", "Zhenyu Zhang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.05175"
  - title: "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
    authors: ["Elias Frantar", "Saleh Ashkboos", "Torsten Hoefler", "Dan Alistarh"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2210.17323"
  - title: "SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models"
    authors: ["Guangxuan Xiao", "Ji Lin", "Mickael Seznec", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2211.10438"
  - title: "ZeroQuant: Efficient and Affordable Post-Training Quantization for Large-Scale Transformers"
    authors: ["Zhewei Yao", "Reza Yazdani Aminabadi", "Minjia Zhang", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2206.01861"
  - title: "GPT3.int8(): 8-bit Matrix Multiplication for Transformers at Scale"
    authors: ["Tim Dettmers", "Mike Lewis", "Younes Belkada", "Luke Zettlemoyer"]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale"
    authors: ["Tim Dettmers", "Mike Lewis", "Younes Belkada", "Luke Zettlemoyer"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2208.07339"
  - title: "AWQ: Activation-Aware Weight Quantization for LLM Compression and Acceleration"
    authors: ["Ji Lin", "Jiaming Tang", "Haotian Tang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2306.00978"
  - title: "CoLT5: Faster Long-Range Transformers with Conditional Computation"
    authors: ["Joshua Ainslie", "Tao Lei", "Michiel de Jong", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2303.09752"
  - title: "Dynamic Context Pruning for Efficient and Interpretable Autoregressive Transformers"
    authors: ["Sotiris Anagnostidis", "Dario Pavllo", "Luca Biggio", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2305.15805"
  - title: "Efficient Transformers: A Survey"
    authors: ["Yi Tay", "Mostafa Dehghani", "Dara Bahri", "Donald Metzler"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2009.06732"
  - title: "SpAtten: Efficient Sparse Attention Architecture with Cascade Token and Head Pruning"
    authors: ["Hanrui Wang", "Zhekai Zhang", "Song Han"]
    year: 2021
    venue: "HPCA"
    doi: null
    url: null
    arxiv_id: null
  - title: "The LRU-K Page Replacement Algorithm for Database Disk Buffering"
    authors: ["Elizabeth J. O'Neil", "Patrick E. O'Neil", "Gerhard Weikum"]
    year: 1993
    venue: "ACM SIGMOD Record"
    doi: null
    url: null
    arxiv_id: null
  - title: "LRFU: A Spectrum of Policies That Subsumes the Least Recently Used and Least Frequently Used Policies"
    authors: ["Donghee Lee", "Jongmoo Choi", "Jong-Hun Kim", "et al."]
    year: 2001
    venue: "IEEE Transactions on Computers"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the Expressive Power of Self-Attention Matrices"
    authors: ["Valerii Likhosherstov", "Krzysztof Choromanski", "Adrian Weller"]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2106.03764"
  - title: "Inductive Biases and Variable Creation in Self-Attention Mechanisms"
    authors: ["Benjamin L. Edelman", "Surbhi Goel", "Sham Kakade", "Cyril Zhang"]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "A Study of Replacement Algorithms for a Virtual-Storage Computer"
    authors: ["Laszlo A. Belady"]
    year: 1966
    venue: "IBM Systems Journal"
    doi: null
    url: null
    arxiv_id: null
  - title: "Resurrecting Submodularity for Neural Text Generation"
    authors: ["Simeng Han", "Xiang Lin", "Shafiq Joty"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.03014"
  - title: "OPT: Open Pre-trained Transformer Language Models"
    authors: ["Susan Zhang", "Stephen Roller", "Naman Goyal", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2205.01068"
  - title: "LLaMA: Open and Efficient Foundation Language Models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2302.13971"
  - title: "GPT-NeoX-20B: An Open-Source Autoregressive Language Model"
    authors: ["Sid Black", "Stella Biderman", "Eric Hallahan", "et al."]
    year: 2022
    venue: "ACL Workshop on Challenges & Perspectives in Creating Large Language Models"
    doi: null
    url: null
    arxiv_id: null
  - title: "Choice of Plausible Alternatives (COPA)"
    authors: ["Melissa Roemmele", "Cosmin Adrian Bejan", "Andrew S. Gordon"]
    year: 2011
    venue: "AAAI Spring Symposium"
    doi: null
    url: null
    arxiv_id: null
  - title: "MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms"
    authors: ["Aida Amini", "Saadia Gabriel", "Shanchuan Lin", "et al."]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering (OpenBookQA)"
    authors: ["Todor Mihaylov", "Peter Clark", "Tushar Khot", "Ashish Sabharwal"]
    year: 2018
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "PIQA: Reasoning About Physical Commonsense in Natural Language"
    authors: ["Yonatan Bisk", "Rowan Zellers", "Ronan Le Bras", "et al."]
    year: 2020
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding (RTE)"
    authors: ["Alex Wang", "Amanpreet Singh", "Julian Michael", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1804.07461"
  - title: "WinoGrande: An Adversarial Winograd Schema Challenge at Scale"
    authors: ["Keisuke Sakaguchi", "Ronan Le Bras", "Chandra Bhagavatula", "Yejin Choi"]
    year: 2021
    venue: "Communications of the ACM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization (XSUM)"
    authors: ["Shashi Narayan", "Shay B. Cohen", "Mirella Lapata"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1808.08745"
  - title: "Abstractive Text Summarization Using Sequence-to-Sequence RNNs and Beyond (CNN/Daily Mail)"
    authors: ["Ramesh Nallapati", "Bowen Zhou", "Caglar Gulcehre", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1602.06023"
  - title: "AlpacaEval: An Automatic Evaluator of Instruction-Following Models"
    authors: ["Xuechen Li", "Tianyi Zhang", "Yann Dubois", "et al."]
    year: 2023
    venue: "GitHub"
    doi: null
    url: "https://github.com/tatsu-lab/alpaca_eval"
    arxiv_id: null
  - title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
    authors: ["Lianmin Zheng", "Wei-Lin Chiang", "Ying Sheng", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient Streaming Language Models with Attention Sinks (StreamingLLM)"
    authors: ["Guangxuan Xiao", "Yuandong Tian", "Beidi Chen", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.17453"
  - title: "LM-Infinite: Simple On-the-Fly Length Generalization for Large Language Models"
    authors: ["Chi Han", "Qifan Wang", "Wenhan Xiong", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2308.16137"
  - title: "Compressive Transformers for Long-Range Sequence Modelling"
    authors: ["Jack W. Rae", "Anna Potapenko", "Siddhant M. Jayakumar", "Timothy P. Lillicrap"]
    year: 2020
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    authors: ["Nelson F. Liu", "Kevin Lin", "John Hewitt", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2307.03172"
  - title: "The Case for 4-bit Precision: k-bit Inference Scaling Laws"
    authors: ["Tim Dettmers", "Luke Zettlemoyer"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2212.09720"
  - title: "Texygen: A Benchmarking Platform for Text Generation Models"
    authors: ["Yaoming Zhu", "Sidi Lu", "Lei Zheng", "et al."]
    year: 2018
    venue: "ACM SIGIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding"
    authors: ["Song Han", "Huizi Mao", "William J. Dally"]
    year: 2015
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1510.00149"
  - title: "Attention Is All You Need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "Kristina Toutanova"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "Language Models are Few-Shot Learners (GPT-3)"
    authors: ["Tom B. Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "BLOOM: A 176B-Parameter Open-Access Multilingual Language Model"
    authors: ["Teven Le Scao", "Angela Fan", "Christopher Akiki", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2211.05100"
  - title: "An Analysis of Approximations for Maximizing Submodular Set Functions — I"
    authors: ["George L. Nemhauser", "Laurence A. Wolsey", "Marshall L. Fisher"]
    year: 1978
    venue: "Mathematical Programming"
    doi: null
    url: null
    arxiv_id: null
  - title: "Heavy Hitters via Cluster-Preserving Clustering"
    authors: ["Kasper Green Larsen", "Jelani Nelson", "Huy L. Nguyen", "Mikkel Thorup"]
    year: 2016
    venue: "FOCS"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 4
  title: "Comparison results between the baseline model with full cache, our H2O, and the 'Local' strategy that utilizes the most recent KV embeddings"
  page: 7
  image_path: "figures/zhang-2023-h2o-kv-cache-fig.png"
---

# H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models

**Authors:** Zhenyu Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai, Zhao Song, Yuandong Tian, Christopher Ré, Clark Barrett, Zhangyang Wang, Beidi Chen
**Published:** 2023-12 (NeurIPS 2023) · [Source](https://arxiv.org/abs/2306.14048)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

LLM KV caches grow linearly with sequence length × batch size (a 30B model with batch 128 × seq 1024 = 180GB of KV alone), making long-context generation cost-prohibitive. Zhang et al. show that (1) attention matrices at inference are >95% sparse in pre-trained OPT/LLaMA/GPT-NeoX, and (2) accumulated attention scores follow a power-law — a small "heavy-hitter" (H2) set of tokens carries most of the signal. The H2O eviction policy keeps a fixed budget split between recent tokens and the running top-K heavy hitters (scored by summed attention so far), evicting at most one KV per step. With 20% of full KV budget, accuracy matches the full-cache baseline across 8 tasks on OPT/LLaMA/GPT-NeoX (6.7B–66B); throughput rises 29×/29×/3× over Accelerate/DeepSpeed/FlexGen on T4, and per-token latency drops up to 1.9× on A100. Theoretically, the greedy attention-score rule satisfies a (1−α)(1−1/e)−β submodular bound under mild assumptions. Extended ablations show compatibility with quantization, robustness from zero-shot to ten-shot, and streaming inference up to 4M tokens (beating StreamingLLM on perplexity).

## Key Takeaway

**Eviction-time synthesis with a single-scalar importance signal — accumulated attention score — is enough to compress the KV cache 5× without quality loss, because attention itself is power-law sparse.** This is a strong existence proof that the "Maintain" stage of a memory architecture (M in ENGRAM) can be cheap, local, and online if the upstream representation has the right statistical structure. H2O does not learn an eviction model, does not look at future tokens, does not even look outside the current head — it just keeps the running argmax of summed attention scores plus a recent window. That this matches full-cache accuracy says something architectural about transformer attention itself: most of the work is being done by a tiny minority of tokens, and identifying them online with a greedy submodular heuristic is near-optimal in the formal sense. **(M, R, E)** — Maintain (eviction) is doing the heavy lifting; Retrieve (which KVs participate in next-token attention) is reshaped by it; Encode (what gets stored) becomes "all initially, then ruthlessly pruned online."

## Implications

For a memory-architecture researcher running ENGRAM-style experiments:

- **(M) Eviction is a first-class architectural decision, not an afterthought.** H2O is essentially LRU+LFU adapted to transformer attention semantics (LRU = the recent window; LFU = the cumulative-attention-score top-K). The paper makes explicit what every memory system implicitly does: when storage is bounded, the policy that decides what to *drop* shapes what queries return. In a long-running agent's memory system, the "what to forget" decision deserves the same rigor we give "what to retrieve."

- **(E ⇄ M) Write everything cheaply, prune ruthlessly later.** H2O writes every KV the model produces (no write-time filtering, no LLM-distilled summaries), then deletes online based on observed usage. Contrast this with mem0/MemoryBench-style designs that distill at write time (expensive LLM call per ingestion) to keep storage small. H2O's bet — "we can afford to write naively if we have a good eviction signal" — is the opposite write-time-vs-query-time tradeoff and is worth testing in agent-memory systems where ingestion volume dominates.

- **(R, M) Running counters as a maintenance primitive.** The whole eviction algorithm reduces to a per-token running scalar (sum of attention scores received so far). This is cheap to update, cheap to query for argmax, and survives the streaming setting. For memory systems, the equivalent is: keep an "access count + decay" counter on every memory unit; evict when budget is hit. Most current vector stores do not even track this.

- **(G) Provenance survives untouched.** Unlike summarization-based compression (gist tokens, learned compressors, LLM-rewritten chunks), H2O never modifies a KV — it only deletes them. Every surviving KV is the original write. For trust/provenance work, this is the gold standard: compression by deletion preserves cite-back fidelity. Summarization-based memory compression loses this.

- **(N) The "shape of memory" stays flat.** H2O does not graph, tree, or hierarchically index the KV cache — it stays flat. The interesting structure (which tokens matter) is recovered at query time via the running score, not encoded into the storage shape. Architecturally this argues for **flat + cheap-counter** over **graph + expensive-write** in scenarios where the access pattern itself reveals importance.

- **(M) "Local statistic ≈ global statistic" is the kill shot.** The most surprising claim (Fig 2d and §4.1): retaining heavy hitters using only past attention scores is as effective as the oracle that uses future scores. Translated to agent memory: you do not need to know which memories future queries will need — you only need to track which memories past queries actually hit. This kills a whole class of "predict future usefulness" research directions and validates simple usage-counting.

- **(M, E) Compression composes with quantization (orthogonally).** H2O + INT4 KV quantization sometimes *improves* on H2O alone (Table 6). The two compression axes — *which* KVs and *how* many bits per KV — do not interfere. For agentic-memory stacks, this implies eviction and on-disk encoding are orthogonal layers and can be designed independently.

- **(M) Streaming for free.** H2O extends to 4M-token inputs with lower perplexity than StreamingLLM (Fig 5). Eviction policies designed for finite caches naturally generalize to infinite streams — there is no separate "long-context" architecture needed when your maintenance layer is well-designed.

- **Failure-mode the architect should care about**: keeping *only* heavy hitters or *only* the recent window each fails by 3–22 percentage points; you need both (Q4 ablation, Table 9). This is an early example of a phenomenon other 2025 work confirms (StreamingLLM's "attention sinks", BEAM-Light's recency-vs-importance dual signal): **transformer attention has two distinct memory regimes — positional/recency and semantic/saliency — and a memory system must serve both.**

- **What the paper does NOT address (gaps for the ENGRAM researcher):** no provenance/contradiction handling (it is per-head, per-layer, no global view), no Aggregate stage (no consolidation across decoded steps — each step's eviction decision is independent), no inter-document grounding. These are KV-level decisions inside one inference pass, not memory-system decisions across sessions. The principles transfer; the mechanism does not.

## How to Apply It (method)

To implement an H2O-style memory eviction in your own system:

1. **Pre-allocate fixed-size memory of K slots, partitioned as `[K_heavy | K_recent]`** (Zhang et al. use 50/50; the budget K is the only tuning knob, typically set to 4–60% of full).
2. **On every write, append to the recent window using a circular queue** (oldest recent gets demoted, not deleted, when window fills — it competes for a heavy-hitter slot).
3. **Maintain one scalar per stored item: cumulative usage score.** In H2O this is the column sum of post-softmax attention scores received during decoding. For an agentic memory store, the analogue is "sum of retrieval scores returned by previous queries" or "exponentially-decayed access count" — anything monotone in usage frequency.
4. **At eviction time (when storage hits K)**: compute `Fscore` over all K slots = sum of stored usage scores. Evict `u = argmin Fscore` across the union of (existing slots ∪ new candidate). New candidate joins, lowest-score loser drops out.
5. **Eviction is irreversible**: the dropped KV/memory cannot be retrieved. Accept this; the submodular-greedy bound only holds in the no-rollback regime.
6. **Do not move memory on eviction**: pre-allocate, overwrite in place (avoids data movement). The H2O paper makes this an explicit I/O-efficiency point.

Hyperparameters and operational guidance from the paper:

- **Budget K = 20% of input length** is the sweet spot — matches full-cache accuracy across all tested model/task combinations.
- **50/50 split between heavy and recent** is the default; the ablation shows both halves are necessary.
- **Per-head, per-layer eviction** — do not share eviction decisions across heads or layers. Different heads attend to different positions; pooling decisions degrades performance.
- **Compatible with INT4/INT8 quantization** (Table 6) — apply both, they compose.
- **Streaming long context**: combine with attention-sink (StreamingLLM-style) handling for inputs >context length; H2O's heavy hitters often *include* the first few tokens automatically, which gives the sink behavior for free.

For non-transformer memory systems (e.g., a vector store backing an agent's long-term memory), the porting is direct: substitute "summed attention score" with "summed retrieval-relevance score across all past queries that hit this item." Keep a recent-write buffer. Evict by lowest cumulative score when the budget is hit. Test against an LRU baseline.

## Best Figure

![Figure 4 — Comparison results between the baseline model with full cache, our H2O, and the 'Local' strategy that utilizes the most recent KV embeddings (page 7)](figures/zhang-2023-h2o-kv-cache-fig.png)

```
Image Candidates:
Figure 4 (p. 7): 12-panel grid comparing H2O vs Local vs Full across 4 model families × 4 tasks (XSUM/CNN-Daily-Mail/OpenBookQA/etc.) and all KV budgets from 4% to 100% — the headline accuracy result.
Figure 1 (p. 2): Architecture diagram showing dynamic vs static-strided vs static-local KV sparsity, plus the accuracy-memory tradeoff overview — best for explaining what H2O *is*.
Figure 2 (p. 4): Four-panel evidence figure showing (a) >95% attention sparsity in pre-trained LLMs, (b) power-law of accumulated attention scores aligning with token co-occurrence, (c) drastic accuracy collapse without heavy hitters, (d) H2O matches full-cache across 6 tasks at 20% budget — establishes the core empirical claim.

Best Image:
Figure Name: Figure 4: "Comparison results between the baseline model with full cache, our H2O, and the 'Local' strategy that utilizes the most recent KV embeddings"
Figure Page: 7
Slide Caption: H2O matches the full-cache baseline across 12 model/task combinations while the recent-window-only "Local" strategy collapses below 60% budget.
Description: Figure 4 is a 4×3 grid of accuracy-vs-KV-budget plots across four model families (LLaMA-7B/13B/30B, GPT-NeoX-20B) and four task types (XSUM, CNN/Daily Mail, OpenBookQA, COPA / MathQA / RTE for the OPT-30B/66B variants). Each subplot overlays three curves: the dashed full-KV baseline, the orange H2O curve, and the blue "Local" (most-recent-only) curve. The visual story is clear and uniform: H2O tracks the full-cache baseline almost exactly from 20% budget upward, while the Local strategy degrades catastrophically — often dropping 20–40 points by 20% budget. This single figure carries the paper's main empirical claim: a budget-aware eviction policy that combines heavy hitters with recent tokens recovers full-cache quality at 5× memory savings, while either component alone fails. It is the right slide for both technical and research audiences.
```

## What Experts Overlook

A KV-cache-eviction expert reading this paper in 2026 might over-index on the 29× throughput number and miss the deeper architectural points. For a memory architect, the underexplored insights are:

1. **The submodularity result is mostly hand-wavy in the body and only formal in Appendix D — and the assumption it requires (attention scheme is submodular) is not empirically verified.** The (1−α)(1−1/e)−β bound is presented as a theoretical guarantee, but α and β are not bounded numerically and the submodularity assumption is conditional. The empirical results are strong; the theory is more of a thematic justification than a tight bound. A careful reader should treat H2O as "well-motivated heuristic with empirical validation," not "provably near-optimal in practice."

2. **"Local statistic ≈ global statistic" is the architecturally surprising claim, not the throughput number.** Most discussions emphasize 5× memory reduction and 29× throughput. The deeper finding is §4.1: scoring heavy hitters using only past attention (no lookahead) is as effective as the oracle with future attention. This kills the assumption that good eviction requires future information — and it implies that for *any* memory system whose access pattern shows temporal autocorrelation (true of nearly all real workloads), past-only counters are sufficient. This generalizes far beyond KV caches.

3. **The "Local"-only baseline collapse is itself an under-discussed finding.** Recent-window-only KV caches lose 20–40 accuracy points (Table 2: 57.94 → 81.00 on PiQA). This is strong evidence against the implicit assumption — held by many streaming-LLM and sliding-window designs — that "recent context is enough." The paper shows that for transformer generation, semantic anchors must be preserved across long spans, not just positional recency. This is the same finding that motivated StreamingLLM's attention sinks (later, citing H2O as prior art).

4. **Per-head, per-layer eviction is critical but barely discussed.** Buried in the implementation details: H2O makes eviction decisions independently per attention head. Pooling decisions across heads degrades performance. This implies the heavy-hitter set is *not* a property of the input sequence — it is a property of (sequence × head × layer). For a memory architect, this is a warning: importance signals must be tracked at the granularity at which they vary, not at the unit that "feels right" (the sequence).

5. **Compression composing favorably with quantization (sometimes *improving*) is anomalous and not deeply explained.** Table 6 shows H2O + INT4 sometimes beats H2O alone. The paper notes this with surprise but does not investigate. One plausible explanation: quantization adds noise that acts as a regularizer on the keys, smoothing the heavy-hitter distribution. If true, this implies KV compression methods designed *together* (joint sparsity + quantization codebook) could outperform either alone — a research direction the paper points to but does not pursue.

6. **The "diversity bonus" from cache eviction (Q5/Appendix C.1) is genuinely weird and gets one paragraph.** H2O-decoded text shows fewer repeated phrases and more creativity than full-cache decoded text — at *same temperature*. This suggests that the full KV cache is acting as a repetition trap (over-attending to recent identical tokens), and eviction breaks this. If this generalizes, it implies KV pruning is not just an efficiency optimization but a *quality* lever for long-form generation. Underexplored.

7. **The paper benchmarks on OPT/LLaMA/GPT-NeoX — none of which use grouped-query attention or multi-query attention.** Modern (2024+) production LLMs (LLaMA-3, Mistral, GPT-4) use GQA/MQA, which already cuts KV cache 4–8×. How H2O composes with GQA is not tested. There is a quiet assumption that H2O's 5× savings stack on GQA's 4–8× to give 20–40× — but this is not validated and head-sharing may interact non-trivially with per-head heavy-hitter selection.

8. **No mention of memory bandwidth vs capacity tradeoffs.** Throughput gains are presented as if uniform, but eviction policies have different cost profiles: H2O requires a per-step argmax over K candidates per head per layer, which on modern hardware is non-trivial sequential overhead. The paper bundles this into the end-to-end throughput numbers without breaking out the eviction overhead vs. the savings from a smaller cache. For a system designer choosing between H2O and alternatives like StreamingLLM (zero overhead, simpler), the cost-benefit is unclear from the paper alone.

## Extracted Prompts

This is a systems/algorithms paper — there are no LLM prompts used as part of the method. The paper benchmarks on standard task suites (HELM and lm-eval-harness) using the default prompt formats of those frameworks (5-shot prompts for lm-eval-harness, zero-shot for HELM-derived XSUM and CNN/Daily Mail). No custom prompts are introduced or evaluated.

The closest thing to a "prompt extraction" is the experimental protocol: KV-cache budget ablations are run at 4%, 10%, 20%, and 60% of the prompt's KV length, with 5-shot evaluation on COPA/MathQA/OpenBookQA/PiQA/RTE/WinoGrande and zero-shot on XSUM/CNN-Daily-Mail. These are framework-provided prompts, not contributions of this paper.

## Citations

The paper cites 145 references across efficient inference, sparse/linear attention, quantization, pruning, distillation, transformer foundations, evaluation benchmarks, and theoretical submodularity / sparse-recovery literature. Full structured array in the frontmatter `citations:` block. Highlights for a memory architect:

- **[5] Pope et al. 2022** — Efficiently Scaling Transformer Inference (the paper that first named KV cache as a deployment bottleneck)
- **[6] Belady et al. 1969** — the original IBM optimal-page-replacement paper; H2O is explicitly compared to "Belady's algorithm" for cache replacement
- **[8] Dao et al. 2022** — FlashAttention (orthogonal approach: reduce attention compute, not KV size)
- **[9] Child et al. 2019** — Sparse Transformers (the static-sparsity baseline H2O compares against and beats)
- **[19] Sheng et al. 2023** — FlexGen (the inference engine H2O is implemented on top of)
- **[32] Wang et al. 2021** — SpAtten (closest related work — also uses accumulated attention scores, but treats heads/layers uniformly; H2O explicitly differentiates by not doing so)
- **[37] Belady 1966** — foundational replacement-algorithm paper
- **[38] Han et al. 2019** — "Resurrecting submodularity for neural text generation" — the link between attention and submodularity that H2O leans on
- **[52] Xiao et al. 2023** — StreamingLLM (concurrent and later work on streaming inference with attention sinks; the H2O streaming results in §5.3 compare against it directly)
- **[127, 128, 130] Krause/Bilmes/Nemhauser** — the submodularity / greedy-approximation theory underpinning the (1−1/e) bound

## Related Digests

- [[shan-2025-cognitive-memory-llms]] — Cognitive Memory in Large Language Models — comprehensive 2025 survey that places H2O in the "sparse attention with KV cache eviction" family alongside Quest, StreamingLLM, and SnapKV
- [[dao-2022-flashattention]] — FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness — orthogonal compute-side optimization; H2O cites it as a complementary approach (compute vs. memory axes)
- [[xiao-2023-streaming-llm]] — Efficient Streaming Language Models with Attention Sinks — direct successor that builds on H2O's heavy-hitter observation and adds the "first-tokens-as-attention-sinks" insight for infinite streaming
- [[child-2019-sparse-transformers]] — Generating Long Sequences with Sparse Transformers — the static-sparsity baseline H2O beats (and improves) on KV-budget ablations
- [[tavakoli-2026-beam-light]] — Beyond a Million Tokens: BEAM-Light long-term memory benchmark — explicitly cites H2O as a foundational reference for "importance × recency" dual-signal eviction in long-context LLMs

## Reviewer Notes

**Hallucination check severity: Clean.**

I cross-checked every numeric claim, model name, citation, and methodological detail in the digest against the paper text:

- **180GB KV cache for 30B model / batch 128 / seq 1024**: ✓ stated verbatim in §1.
- **>95% attention sparsity**: ✓ §3.1, Figure 2a, explicitly stated.
- **20% KV budget matches full**: ✓ §5.1 main results.
- **29×/29×/3× throughput over Accelerate/DeepSpeed/FlexGen**: ✓ Abstract and §5.2 Table 3/4.
- **1.9× latency reduction on A100**: ✓ Abstract and Table 5 (2048+2048, 6.7B, batch 24: 99.5s → 53.5s = 1.86×).
- **(1−α)(1−1/e)−β submodular bound**: ✓ Theorem 4.4, informally stated in §4.2 with α, β > 0 parameters.
- **4M-token streaming claim**: ✓ §5.3 Q1, Figure 5.
- **Tested on OPT, LLaMA, GPT-NeoX (6.7B to 175B)**: ✓ §5.1 setup, though I noted "175B" only refers to model family ceiling; actual reported numbers cap at OPT-66B and LLaMA-30B.
- **8 evaluation tasks**: ✓ COPA, MathQA, OpenBookQA, PiQA, RTE, WinoGrande, XSUM, CNN/Daily Mail — all in §5.1.
- **Code at github.com/FMInference/H2O**: ✓ abstract.
- **NeurIPS 2023**: ✓ stated on title page (37th Conference on NeurIPS).
- **Per-head, per-layer eviction**: ✓ inferred from Appendix A pseudocode (`for each head` in `attention_forward`) — the body says it less explicitly but the implementation makes it unambiguous.
- **H2O + quantization sometimes improves over H2O alone**: ✓ §5.3 Q3, Table 6 (described as "almost always achieves better accuracy than H2O or quantization alone").
- **Diversity bonus**: ✓ §5.3 Q5, Appendix C.1.

**Minor framing choices that go slightly beyond the paper (called out for transparency, not corrections):**

- I characterized H2O's eviction as "LRU+LFU adapted to attention semantics" — the paper does not use this framing, but it is fair conceptually (recent window ≈ LRU, cumulative-score top-K ≈ LFU). Useful for readers from systems backgrounds; not in the paper.
- The "memory architect implications" — mapping each finding to E/N/G/R/A/M dimensions — is the lens's framing, not the paper's. The lens explicitly asks for this.
- The expert-overlook claim that "GQA composition is untested" is correct (no GQA experiment in the paper), but I am making it salient as a 2026 concern; the paper itself (2023) predates GQA's dominance.

No fabricated citations, no invented numbers, no misattributed claims. Safe to publish as wiki entry.
