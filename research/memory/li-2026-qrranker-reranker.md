---
corpus: agentic-memory
kind: paper-digest
slug: li-2026-qrranker-reranker
title: "Query-focused and Memory-aware Reranker for Long Context Processing"
authors:
  - "Yuqing Li"
  - "Jiangnan Li"
  - "Mo Yu"
  - "Guoxuan Ding"
  - "Zheng Lin"
  - "Weiping Wang"
  - "Jie Zhou"
year: 2026
publication_date: "2026-03"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2602.12192"
doi: null
arxiv_id: "2602.12192"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "A 4B-parameter listwise reranker built by training 16 Query-focused Retrieval (QR) attention heads — not generating tokens — beats heavier graph-based memory systems on LoCoMo (57.03 F1 vs 53.10 best baseline) using only 854 tokens of raw dialogue chunks, showing that smarter retrieval over flat memory can outperform sophisticated write-time memory engineering."
topics:
  - reranking
  - long-context-retrieval
  - retrieval-heads
  - attention-mechanism
  - dialogue-memory
  - listwise-ranking
  - locomo
  - narrative-qa
  - memory-architecture
  - rag
tags:
  - paper
  - reranker
  - qr-heads
  - attention-scores
  - memory-aware
  - locomo
  - benchmark
  - qwen3
  - lightweight-model
entities:
  - li-yuqing
  - li-jiangnan
  - yu-mo
  - lin-zheng
related_digests:
  - maharana-2024-locomo
  - chhikara-2025-mem0
  - latimer-2025-hindsight-memory
  - adler-2026-storage-not-memory
  - packer-2023-memgpt-os
citations:
  - title: "Llama-embed-nemotron-8b: A universal text embedding model for multilingual and cross-lingual tasks"
    authors: ["Yauhen Babakhin", "Radek Osmulski", "Ronay Ak", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2511.07025"
  - title: "M3-embedding: Multi-linguality, multi-functionality, multi-granularity text embeddings through self-knowledge distillation"
    authors: ["Jianlyu Chen", "Shitao Xiao", "Peitian Zhang", "et al."]
    year: 2024
    venue: "Findings of ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mem0: Building production-ready AI agents with scalable long-term memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2504.19413"
  - title: "Lightmem: Lightweight and efficient memory-augmented generation"
    authors: ["Jizhan Fang", "Xinle Deng", "Haoming Xu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2510.18866"
  - title: "Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity"
    authors: ["William Fedus", "Barret Zoph", "Noam Shazeer"]
    year: 2022
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "From rag to memory: Non-parametric continual learning for large language models (HippoRAG-v2)"
    authors: ["Bernal Jiménez Gutiérrez", "Yiheng Shu", "Weijian Qi", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Evermemos: A self-organizing memory operating system for structured long-horizon reasoning"
    authors: ["Chuanrui Hu", "Xingze Gao", "Zuyi Zhou", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2601.02163"
  - title: "Memory matters more: Event-centric memory as a logic map for agent searching and reasoning (CompassMem)"
    authors: ["Yuyang Hu", "Jiongnan Liu", "Jiejun Tan", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2601.04726"
  - title: "Synapse: Empowering llm agents with episodic-semantic memory via spreading activation"
    authors: ["Hanqi Jiang", "Junhao Chen", "Yi Pan", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2601.02744"
  - title: "HippoRAG: Neurobiologically inspired long-term memory for large language models"
    authors: ["Bernal Jimenez Gutierrez", "Yiheng Shu", "Yu Gu", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "ColBERT: Efficient and effective passage search via contextualized late interaction over BERT"
    authors: ["Omar Khattab", "Matei Zaharia"]
    year: 2020
    venue: "SIGIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Siamese neural networks for one-shot image recognition"
    authors: ["Gregory Koch", "Richard Zemel", "Ruslan Salakhutdinov"]
    year: 2015
    venue: "ICML deep learning workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "The NarrativeQA reading comprehension challenge"
    authors: ["Tomáš Kočiský", "Jonathan Schwarz", "Phil Blunsom", "et al."]
    year: 2018
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "TiMem: Temporal-hierarchical memory consolidation for long-horizon conversational agents"
    authors: ["Kai Li", "Xuanqing Yu", "Ziyi Ni", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2601.02845"
  - title: "Mindscape-aware retrieval augmented generation for improved long context understanding"
    authors: ["Yuqing Li", "Jiangnan Li", "Zheng Lin", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2512.17220"
  - title: "MemOS: A memory OS for AI system"
    authors: ["Zhiyu Li", "Chenyang Xi", "Chunyu Li", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2507.03724"
  - title: "Just ask one more time! self-agreement improves reasoning of language models in (almost) all scenarios"
    authors: ["Lei Lin", "Jiayi Fu", "Pengli Liu", "et al."]
    year: 2024
    venue: "Findings of ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "SimpleMem: Efficient lifelong memory for LLM agents"
    authors: ["Jiaqi Liu", "Yaofeng Su", "Peng Xia", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2601.02553"
  - title: "ReasonRank: Empowering passage ranking with strong reasoning ability"
    authors: ["Wenhan Liu", "Xinyu Ma", "Weiwei Sun", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2508.07050"
  - title: "Uncertainty quantification and confidence calibration in large language models: A survey"
    authors: ["Xiaoou Liu", "Tiejin Chen", "Longchao Da", "et al."]
    year: 2025
    venue: "KDD"
    doi: null
    url: null
    arxiv_id: null
  - title: "Zero-shot listwise document reranking with a large language model"
    authors: ["Xueguang Ma", "Xinyu Zhang", "Ronak Pradeep", "et al."]
    year: 2023
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2305.02156"
  - title: "Evaluating very long-term conversational memory of LLM agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "et al."]
    year: 2024
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Nemori: Self-organizing agent memory inspired by cognitive science"
    authors: ["Jiayan Nan", "Wenquan Ma", "Wenlong Wu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2508.03341"
  - title: "RankVicuna: Zero-shot listwise document reranking with open-source large language models"
    authors: ["Ronak Pradeep", "Sahel Sharifymoghaddam", "Jimmy Lin"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.15088"
  - title: "RankZephyr: Effective and robust zero-shot listwise reranking is a breeze!"
    authors: ["Ronak Pradeep", "Sahel Sharifymoghaddam", "Jimmy Lin"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2312.02724"
  - title: "Large language models are effective text rankers with pairwise ranking prompting"
    authors: ["Zhen Qin", "Rolf Jagerman", "Kai Hui", "et al."]
    year: 2024
    venue: "Findings of NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "TongSearch-QR: Reinforced query reasoning for retrieval"
    authors: ["Xubo Qin", "Jun Bai", "Jiaqi Li", "et al."]
    year: 2025
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2506.11603"
  - title: "Zep: A temporal knowledge graph architecture for agent memory"
    authors: ["Preston Rasmussen", "Pavlo Paliychuk", "Travis Beauvais", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2501.13956"
  - title: "GroupRank: A groupwise reranking paradigm driven by reinforcement learning"
    authors: ["Duolin Sun", "Meixiu Long", "Dan Yang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2511.11653"
  - title: "Is ChatGPT good at search? Investigating large language models as re-ranking agents"
    authors: ["Weiwei Sun", "Lingyong Yan", "Xinyu Ma", "et al."]
    year: 2023
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Membox: Weaving topic continuity into long-range memory for LLM agents"
    authors: ["Dehao Tao", "Guoliang Ma", "Yongfeng Huang", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2601.03785"
  - title: "Augmented SBERT: Data augmentation method for improving bi-encoders for pairwise sentence scoring tasks"
    authors: ["Nandan Thakur", "Nils Reimers", "Johannes Daxenberger", "et al."]
    year: 2021
    venue: "NAACL-HLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "MuSiQue: Multi-hop questions via single-hop question composition"
    authors: ["Harsh Trivedi", "Niranjan Balasubramanian", "Tushar Khot", "et al."]
    year: 2022
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the theoretical limitations of embedding-based retrieval"
    authors: ["Orion Weller", "Michael Boratko", "Iftekhar Naim", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2508.21038"
  - title: "SiteMB-v1.5: Improved context-aware dense retrieval for semantic association and long story comprehension"
    authors: ["Junjie Wu", "Jiangnan Li", "Yuqing Li", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2508.01959"
  - title: "Retrieval head mechanistically explains long-context factuality"
    authors: ["Wenhao Wu", "Yizhong Wang", "Guangxuan Xiao", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2404.15574"
  - title: "A-Mem: Agentic memory for LLM agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2502.12110"
  - title: "DetectiveQA: Evaluating long-context reasoning on detective novels"
    authors: ["Zhe Xu", "Jiasheng Ye", "Xiaoran Liu", "et al."]
    year: 2025
    venue: "Workshop on Reasoning and Planning for LLMs"
    doi: null
    url: null
    arxiv_id: null
  - title: "Qwen3 technical report"
    authors: ["An Yang", "Anfeng Li", "Baosong Yang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2505.09388"
  - title: "HotpotQA: A dataset for diverse, explainable multi-hop question answering"
    authors: ["Zhilin Yang", "Peng Qi", "Saizheng Zhang", "et al."]
    year: 2018
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "HELMET: How to evaluate long-context language models effectively and thoroughly"
    authors: ["Howard Yen", "Tianyu Gao", "Minmin Hou", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2410.02694"
  - title: "Query-focused retrieval heads improve long-context reasoning and re-ranking"
    authors: ["Wuwei Zhang", "Fangcong Yin", "Howard Yen", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2506.09944"
  - title: "mGTE: Generalized long-context text representation and reranking models for multilingual text retrieval"
    authors: ["Xin Zhang", "Yanzhao Zhang", "Dingkun Long", "et al."]
    year: 2024
    venue: "EMNLP Industry Track"
    doi: null
    url: null
    arxiv_id: null
  - title: "Qwen3-Embedding: Advancing text embedding and reranking through foundation models"
    authors: ["Yanzhao Zhang", "Mingxin Li", "Dingkun Long", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2506.05176"
  - title: "KaLM-Embedding-v2: Superior training techniques and data inspire a versatile embedding model"
    authors: ["Xinping Zhao", "Xinshuo Hu", "Zifei Shan", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2506.20923"
  - title: "The essence of contextual understanding in theory of mind: A study on question answering with story characters"
    authors: ["Chulun Zhou", "Qiujing Wang", "Mo Yu", "et al."]
    year: 2025
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving multi-step rag with hypergraph-based memory for long-context complex relational modeling"
    authors: ["Chulun Zhou", "Chunkang Zhang", "Guoxin Yu", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2512.23959"
  - title: "Rank-R1: Enhancing reasoning in LLM-based document rerankers via reinforcement learning"
    authors: ["Shengyao Zhuang", "Xueguang Ma", "Bevan Koopman", "et al."]
    year: 2025
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2503.06034"
  - title: "ES-Mem: Event segmentation-based memory for long-term dialogue agents"
    authors: ["Huhai Zou", "Tianhao Sun", "Chuanjiang He", "et al."]
    year: 2026
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2601.07582"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "The structure of QRRanker, with memory construction (left), QRRanker scoring with QR-head highlights (middle), and the rank-rerank pipeline for narratives/wiki/dialogues (right)"
  page: 4
  image_path: "figures/li-2026-qrranker-reranker-fig.png"
---

# Query-focused and Memory-aware Reranker for Long Context Processing

**Authors:** Yuqing Li, Jiangnan Li, Mo Yu, Guoxuan Ding, Zheng Lin, Weiping Wang, Jie Zhou
**Published:** 2026-03 · [Source](https://arxiv.org/abs/2602.12192)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

QRRanker trains 16 "Query-focused Retrieval" (QR) attention heads inside a 4B-parameter Qwen3-Instruct backbone to act as a listwise reranker — scoring 50 candidate passages in a single prefill pass using attention weights rather than generated tokens. On LoCoMo (50 multi-session dialogues, ~9k tokens each), it hits 57.03 Overall F1 with GPT-4o-mini and 57.32 with GPT-5-mini using only 854 tokens of top-3 raw dialogue chunks — beating every memory-augmented baseline including Mem0 (45.09), Zep (43.56), MemoryOS (42.84), Membox (53.10), CompassMem (52.18 with a 20k-token budget), and even the elaborate Synapse spreading-activation graph. The same model lifts NarrativeQA from 28.48 F1 (SFT embedding) to 33.61, and DetectiveQA accuracy from 62.85 to 67.25. An optional summary prefix prepended to candidates improves long-narrative recall by +1 to +3 points but slightly hurts Wikipedia QA where evidence is localized. A "middle-layer" variant truncates the backbone after layer 24, dropping P50 latency to 910ms (vs 1221ms for Qwen3-Reranker batch=50) and peak GPU memory to 8.71GB. Code: a small 16-head training pipeline plus the standard rank-then-rerank embedding stack. The lesson: a smarter retriever over a flat memory beats sophisticated write-time memory engineering — at least on the benchmarks the field currently uses.

## Key Takeaway

A 4B-parameter listwise reranker built by training 16 Query-focused Retrieval (QR) attention heads — not generating tokens — beats heavier graph-based memory systems on LoCoMo (57.03 F1 vs 53.10 best baseline) using only 854 tokens of raw dialogue chunks, showing that smarter retrieval over flat memory can outperform sophisticated write-time memory engineering.

## Implications

- **[R, A] A trained reranker on flat memory can dominate elaborate memory architectures — re-balance your investment**: QRRanker beats Mem0, Zep, MemoryOS, Membox, ES-Mem, and the rest on LoCoMo while using raw dialogue chunks and no write-time consolidation. If you're spending weeks on memory-graph schemas, run this baseline first: SOTA embedding + 16 trained attention heads + top-3 to the generator. The result reframes "memory" as primarily a Retrieve-side problem, not an Aggregate-side one.
- **[R] Attention weights, not generated tokens, are the right currency for listwise scoring**: Listwise LLM rerankers (RankZephyr, GroupRank, ReasonRank) emit Likert scores or thinking tokens; QRRanker reads attention scores directly from selected heads — getting continuous scores for free, escaping Likert-data bottlenecks, and skipping all generation. If your reranker pipeline does any text generation per query, you're paying latency for output you didn't need.
- **[E, R] Memory enhancement works for narratives, hurts for Wikipedia — be honest about when summaries help**: Prepending a summary prefix improved DetectiveQA by +2.67 Recall@3 and NarrativeQA by +1.02, but degraded HotpotQA (-0.30) and MuSiQue (-0.03). Abstract global context helps when evidence is dispersed across a long narrative; it adds noise when evidence is already localized in a single passage. Match memory shape to recall problem.
- **[M] Middle-layer truncation gives you a free 25% latency cut with no accuracy loss**: Training QR heads on layers 17-24 instead of 28-35 matches full-model accuracy (54.28 vs 54.44 R@10 on NarrativeQA) and lets you discard layers 25+ entirely at inference — P50 drops from 1095ms to 910ms, peak GPU from 11.18GB to 8.71GB. For self-hosted memory layers, this is an obvious win.
- **[E, G] Silver evidence is enough — full human-gold annotations are not the bottleneck**: The training set uses MuSiQue's official supporting facts plus *constructed silver evidence* for NarrativeQA (no human-annotated gold chunks). The "limitations" section flags this as label noise, yet the model still gains 4-6 points over the trained Qwen-Reranker. For your own retrieval training, weak supervision via question-answer pairs and embedding-retrieved candidates is sufficient.
- **[R, M] Listwise > pointwise for shortlist holism, but only when scoring is continuous**: The paper's framing is that pointwise rerankers (Qwen-Reranker, BGE-m3) lose the global view, while listwise generators (RankVicuna, RankZephyr) have it but can't emit fine-grained scores. QR-head scoring gives you both. If you're using a pointwise cross-encoder today, consider switching — the +6 to +9 R@3 gains on Wikipedia QA are large.
- **[G] No-generation reranking eliminates one whole class of failure modes**: Generation-based listwise rerankers occasionally produce bad-format outputs (especially when forced to think first); QRRanker has no generation at all — just prefill the prompt, read attention. For production memory layers, this collapses an entire failure surface.
- **[E, R] Head-selection portability is real but not free**: QR heads selected on NarrativeQA (1000 random samples) transfer cleanly to LoCoMo and Wikipedia QA after training. But the paper notes that without training, QR heads "may change when moving to new tasks" — training is what gives transferability. Plan for a one-time seed-dataset training pass per new domain, not zero-shot deployment.

## How to Apply It (method)

**Scenario:** You're building Flow OS's memory-architect layer for long-running agents and have a flat markdown vault of session transcripts, decisions, and contacts (~50k chunks). Today you retrieve top-50 with QMD's vector search and dump everything into context. You suspect you're losing recall on multi-hop questions ("How did my thinking on X evolve given what Y said?") because the embedding model's geometric bottleneck can't represent the conjunction. You want to insert a listwise reranker that reorders the top-50 to a clean top-3 before handing context to the agent — with the smallest model that will fit your local stack.

**Steps:**

1. **Pick a backbone and freeze it**: Use Qwen3-4B-Instruct-2507 (36 layers × 32 attention heads = 1152 heads total). 4B parameters is the smallest scale where the paper showed strong reranking; smaller may not work.

2. **Build a seed dataset for QR-head discovery**: Sample 1000 questions from a representative source. The paper used NarrativeQA; for Flow OS, sample 1000 (question, gold-evidence-chunk) pairs from your own session logs — e.g., "What did the user decide about Howler Bikes pricing?" with the linked decision file as gold. Quality matters more than quantity here; this set only locates heads, doesn't train them.

3. **Score every attention head with the QR-score formula**: For each (Q, gold-chunk, distractor-chunks) instance, run a prefill pass through the backbone and compute, for every head `h`:

   ```
   QRScore(h) = (1/|Q|) · sum over gold-chunks ci: sum over query tokens wq: sum over chunk tokens wc: A_h^{Q→ci}[wq, wc]
   ```

   This is just the attention weight from query tokens onto gold-chunk tokens, averaged over the query length. Take the top-16 heads by mean QR-score across all 1000 samples. These are your "QR heads."

4. **Construct listwise training instances**: For each training question Q:
   - Retrieve top-50 candidates with your embedding model (Qwen3-Embedding-8B or whatever you use today)
   - Mark candidates whose text overlaps with known gold/silver evidence as positives (multi-positive is fine and exploited by the loss)
   - Construct the prompt as: `Inst(C, Q)` where C is the 50 chunks concatenated in retrieval order, Q is the question

5. **(Optional) Add a memory prefix M**: For narrative- or dialogue-heavy data, prepend summaries — either block summaries (every 20 consecutive chunks → one ~50-100 word summary via an editor-persona prompt) or event-centric summaries (extract 1-3 anchor/ephemeral events from each conversational session). Cap the prefix at 512 tokens, select summaries by max coverage of the retrieved chunks. Skip the prefix for Wikipedia-style localized-evidence corpora.

6. **Train the 16 QR heads with the group contrastive loss**: For each sample, compute the QR-head retrieval score for each of the 50 candidates by summing attention from query tokens onto each candidate's tokens across the 16 heads. Max-min normalize the 50 scores to range [0, scale=8]. Optimize:

   ```
   L_sample = (1/|G|) · sum over positives cp: log( τ(scp) / (τ(scp) + sum over negatives cn: τ(scn)) )
   ```

   where `τ` is `exp`, G is the set of positive documents, and the loss is averaged over positives so multi-positive samples are handled correctly. Train on Qwen3-4B with DeepSpeed ZERO2, batch=1, grad-accum=4, lr=1e-5, 8× H20 GPUs (or fewer with smaller batches).

7. **(Optional) Truncate after layer 24 for a faster ranker**: After training, you can discard layers 25-35 of the backbone for inference — the QR heads sit in layers 17-24 anyway. This drops P50 latency by ~17% and peak GPU memory by ~22% with no accuracy loss.

8. **Wire into the pipeline**: At query time, run embedding retrieval → top-50 → QRRanker prefill (no generation, just attention extraction) → reorder → pass top-3 to the generator (GPT-4o-mini, Claude, your local Llama, whatever). The paper's prompt template is in §B.3 and is intentionally minimal.

9. **Evaluate on a held-out slice**: Measure Recall@3/5/10 against gold for retrieval quality, and downstream F1/EM on the actual agent task. Compare against your current pipeline AND against a no-rerank baseline to confirm the reranker actually helps your data distribution.

**Expected outcome:** A 4B-parameter listwise reranker that runs at ~1 second per query on a single GPU, scores 50 candidates via attention extraction (no generation), and reorders them to a much tighter top-3. On your own corpus, expect retrieval-quality gains in the +5 to +10 Recall@3 range over a vanilla pointwise reranker, and modest but real downstream F1 lifts (1-4 points on long-context tasks, smaller on local-evidence tasks). You'll also have the option to swap the reranker out for the middle-layer variant later for production-latency wins.

## Best Figure

![Figure 2 — The structure of QRRanker, with memory construction (left), QRRanker scoring with QR-head highlights (middle), and the rank-rerank pipeline for narratives/wiki/dialogues (right) (page 4)](figures/li-2026-qrranker-reranker-fig.png)

**Image Candidates:**
- Figure 2 (p. 4): Three-panel architecture diagram showing memory construction (narrative + dialogue), QRRanker scoring with the highlighted QR heads, and the end-to-end rank-rerank pipeline — tells the entire story in one view.
- Table 3 (p. 7): LoCoMo comparison against 13 SOTA memory systems with token budgets, F1 scores across single-hop/multi-hop/temporal/open-domain — the killer headline number table.
- Table 7 (p. 8): Inference efficiency comparison showing QRRanker(middle) vs Qwen3-Reranker at P50/P95 latency, TFLOPs, and peak GPU memory — makes the efficiency win concrete.

**Best Image:** Figure 2 — `The structure of QRRanker is illustrated in the middle, where the highlighted heads are QR heads for document scoring. As QRRanker can be aware of memory enhancement to capture more contextual information, we can construct memories for narratives and dialogues, which is shown on the left. The right part demonstrates the rank-rerank pipeline of qa for narratives/wiki/dialogues, which involves no sophisticated design.`

**Slide Caption:** QRRanker = trained attention heads (middle panel) + optional memory prefix (left) + simple rank-then-rerank pipeline (right) — no generation, no graph.

**Description:** The three-panel figure decomposes the entire system. Left panel shows the two memory-construction modes: block summaries for in-order narratives (sub-summaries over 20-chunk blocks) and event summaries for dialogues (event-centric extraction across sessions). The middle panel — the contribution — shows the 4B backbone with the 16 QR heads highlighted as orange "QR" cells inside the head grid; Doc1, Doc2, Doc3 are scored simultaneously via attention extraction (no token generation), with Doc2 as gold (highlighted) and a contrastive-loss arrow pointing to the score outputs. Right panel shows the simple pipeline: corpus → embedding-retrieve top-50 → QRRanker reorder → top-3 to generator → answer. The "Memory equipment" middle block on the right shows the optional memory prefix being prepended for the three retrieval-content types (wiki article, narrative chunk, dialogue chunk). The figure's payoff: every component except the highlighted QR heads is off-the-shelf — the contribution is purely in training those 16 attention heads.

## What Experts Overlook

Most readers will fixate on the "trained attention heads" headline and miss the small operational detail that the QR heads QRRanker *actually trains* drift away from the QR heads it *starts with*. The paper shows in §6.3 / Appendix E that when you instead train a semi-automatic variant restricted to a window of layers (17-24) with learned gates picking heads per sample, performance matches QRRanker — but the heads the gates end up activating overlap only weakly with the precomputed QR heads (Appendix E, comparing QRRanker's static heads `20-15, 21-11, 17-27, 23-10, 22-4, 21-10, ...` with the variant's dynamically-selected ones). That means the original QR-head probe was just a useful *initialization*; the contrastive ranking objective then reshapes whichever heads happen to be in the right layer range into "rankers." This decouples the method from any specific theory of which heads are mechanistically retrieval heads.

**Why it matters:** This is the difference between believing the paper "found retrieval-special heads and made them better" versus understanding it actually "found *which layers* have the capacity to be trained into rankers, and then trained any 16 heads in there." The latter is far more portable — you don't need to re-run an expensive QR-score probe on every new backbone; you just pick 16 heads from layers ~50-70% of the way through the network and let the contrastive loss do the rest. It also explains why middle-layer truncation works: you're not throwing away the special heads, you're throwing away layers that don't host them in the first place.

**Example of good use:** A memory-architect team adapting QRRanker to a non-Qwen backbone (say, Llama-3-8B for a customer who only has that licensed). Instead of constructing 1000 NarrativeQA samples to compute QR scores from scratch on Llama, just pick 16 heads from layers 16-22 (the middle band of Llama's 32 layers), wire up the contrastive loss, and train. The semi-auto variant result predicts you'll land in the same accuracy zone.

**Example of misapplication:** A team takes the "QR heads are special" framing literally, spends two weeks building a QR-score probe pipeline for their custom backbone, and treats the resulting head list as load-bearing infrastructure — running ablations on which specific heads matter, debating whether to add or remove individual heads. They miss that the trained heads have drifted so far from the initial QR set that the discovery pipeline was, in effect, a fancy random head-selection in a known-good layer range. They spend their engineering budget on the wrong abstraction.

## Extracted Prompts

**Prompt explanation:** Block-based summary generation — used at memory-construction time for long narrative books; the paper segments each book into ~20-chunk blocks and runs this prompt per block to produce a 50-100 word summary that can later be prepended as a global memory prefix.

```
You are an expert fiction editor and continuity supervisor.
You are provided with a raw text segment from a book (Part {sub_idx} / {total_subs}). This segment consists of approximately 20 consecutive chunks combined.
<Raw_Text>
{raw_text}
</Raw_Text>
Please generate a Detailed Narrative Summary following these strict guidelines:
1. Narrative Reconstruction: Do not list events. Rewrite the content as a coherent story in the third person, past tense. It should read like a condensed version of the original text.
2. Detail Preservation:
   • Preserve specific Character Names and their relationships.
   • Keep key Dialogues that drive the plot.
   • Note specific Locations or setting changes.
3. Noise Filtering:
   • IGNORE any copyright notices, project gutenberg headers, page numbers, or table of contents.
   • If the text starts or ends in the middle of a sentence, ignore the broken fragments and focus on the complete thoughts.
4. Style:
   • NO meta-commentary (e.g., do NOT say "The text describes...", "In this chunk...").
   • Directly tell the story.
5. Length: 50-100 words.
Output the summary directly.
```

**Prompt explanation:** Event-centric summary generation — used at memory-construction time for dialogue data; extracts 1-3 anchor or ephemeral events per session, each linked back to the source utterance line indices for traceability.

```
INSTRUCT: You are a specialized system for extracting structured event representations from conversational data.
1. EVENT CLASSIFICATION
ANCHOR Events. Anchor events are MAJOR LIFE MILESTONES that will be remembered for years.
Only classify as an anchor if the event meets ALL of these criteria:
• Represents a first-time or rare life occurrence
• Has a lasting impact on the person's identity, relationships, or life trajectory
• Would be mentioned when telling someone about "important moments in my life"
Examples of TRUE ANCHOR events: First time attending LGBTQ support group, Starting adoption process, Career change, Moving to a new country, etc.
EPHEMERAL Events. Most events are ephemeral. These include:
• Plans and intentions ("I plan to...", "I want to...")
• Routine activities (exercise, hobbies, daily tasks)
• Casual conversations and updates
• Past events being recalled (unless first mention of major milestone)
4. RAW DIALOGUE REFERENCE
• related_line_indices: list the 2-4 most relevant line numbers (1-indexed from the dialogue)
• These lines will be saved as the event's source evidence
INPUT DIALOG: {dialog}
OUTPUT (JSON FORMAT, EXTRACT 1-3 EVENTS):
{
  "events": [
    {
      "summary": "concise description",
      "related_line_indices": [1, 2, 3]
    }
  ]
}
```

**Prompt explanation:** QRRanker inference-time instruction template — the prompt fed to the 4B backbone for attention-based scoring. No generation; the model only prefills this prompt and the QR heads' attention scores are read out.

```
INSTRUCT:
[Optional Memory Prefix M] Here are some session summaries that may help answer the query: {mapped summaries from top-50 chunks}
[Candidate Chunks C] Here are some retrieved chunks:
[1] {chunk c1}
[2] {chunk c2}
[3] {chunk c3}
[4] ...
[5] {chunk c50}
QUERY Q: {question}
```

**Prompt explanation:** LoCoMo downstream QA prompt — used by the generator (GPT-4o-mini or GPT-5-mini) after QRRanker has selected the top-3 dialogue chunks. Heavy timestamp-handling logic.

```
You are an intelligent memory assistant tasked with retrieving accurate information from conversation memories.
CONTEXT: You have access to memories from two speakers in a conversation. These memories contain timestamped information that may be relevant to answering the question.
INSTRUCTIONS:
1. Carefully analyze all provided memories from both speakers.
2. Pay special attention to the timestamps to determine the answer.
3. If the question asks about a specific event or fact, look for direct evidence in the memories.
4. If the memories contain contradictory information, prioritize the most recent memory.
5. If there is a question about time references (like "last year", "two months ago", etc.), calculate the actual date based on the memory timestamp. For example, if a memory from 4 May 2022 mentions "went to India last year," then the trip occurred in 2021.
6. Always convert relative time references to specific dates, months, or years. For example, convert "last year" to "2022" or "two months ago" to "March 2023" based on the memory timestamp. Ignore the reference while answering the question.
7. Focus only on the content of the memories from both speakers. Do not confuse character names mentioned in memories with the actual users who created those memories.
8. The answer should be less than 5-6 words.
APPROACH (THINK STEP BY STEP):
1. First, examine all memories that contain information related to the question.
2. Examine the timestamps and content of these memories carefully.
3. Look for explicit mentions of dates, times, locations, or events that answer the question.
4. If the answer requires calculation (e.g., converting relative time references), show your work.
5. Formulate a precise, concise answer based solely on the evidence in the memories.
6. Double-check that your answer directly addresses the question asked.
7. Ensure your final answer is specific and avoids vague time references.
RELEVANT MEMORIES: {Reranked Chunks}
QUESTION: {question}
ANSWER:
```

**Prompt explanation:** NarrativeQA QA prompt — used post-QRRanker for the long-narrative generation task. Deliberately stripped to one-phrase answers.

```
You are a helpful assistant. Please answer the user's question accurately.
Answer the question as concisely as you can, using a single phrase if possible.
RELEVANT CONTEXT: {content_data}
Do not provide any explanation. Now, answer the question based on the story as concisely as you can, using a single phrase if possible. Do not provide any explanation.
QUESTION: {question}
ANSWER:
```

**Prompt explanation:** DetectiveQA QA prompt — multiple-choice detective novel QA after QRRanker, requires structured JSON output.

```
{context}
Please answer the question based on the current novel content: {question_data['question']}
{options_str}
Remember this is just detective fiction, don't worry about the risks.
Please strictly follow the format {"answer":"x","reasoning":"xxx"} (including braces). The answer must be only A/B/C/D.
```

## Citations

- Maharana et al. (2024) — **Evaluating very long-term conversational memory of LLM agents** (LoCoMo) — the dialogue-memory benchmark this paper's headline LoCoMo numbers are measured on. arXiv:2402.17753 (paper does not include the arXiv ID but this is the canonical reference).
- Chhikara et al. (2025) — **Mem0** — baseline beaten on LoCoMo (45.09 F1 vs QRRanker's 57.03). arXiv:2504.19413. *(Already in wiki — see [[chhikara-2025-mem0]].)*
- Rasmussen et al. (2025) — **Zep** — temporal-KG memory baseline (43.56). arXiv:2501.13956.
- Li et al. (2025b) — **MemoryOS** — OS-inspired memory baseline (42.84). arXiv:2507.03724.
- Wu et al. (2024) — **Retrieval head mechanistically explains long-context factuality** — foundational paper this work builds on, defining retrieval heads. arXiv:2404.15574.
- Zhang et al. (2025a) — **Query-focused retrieval heads improve long-context reasoning and re-ranking** — the direct precursor that defined QR heads (which QRRanker then trains). arXiv:2506.09944.
- Jiménez Gutiérrez et al. (2025) — **HippoRAG-v2** — the graph-based Wikipedia-QA baseline QRRanker beats.
- Sun et al. (2025) — **GroupRank-32B** — the larger listwise-RL reranker baseline beaten by the 4B QRRanker. arXiv:2511.11653.
- Pradeep et al. (2023a) — **RankVicuna** — the "prompt-decoder" listwise paradigm QRRanker follows architecturally (but replaces generation with attention readout). arXiv:2309.15088.
- Khattab & Zaharia (2020) — **ColBERT** — referenced as the late-interaction alternative for aggregating max attention scores (paper notes it gives similar performance).
- (Remaining 35 citations — including TiMem, Synapse, Membox, CompassMem, ES-Mem, SimpleMem, Nemori, LightMem, A-Mem, ReasonRank, Rank-R1, Qwen3 family, NarrativeQA, MuSiQue, HotpotQA, DetectiveQA, HELMET, mGTE, M3-embedding, KaLM-Embedding-v2, llama-embed-nemotron-8b, Weller's geometric-bottleneck paper, plus methodological references like Switch Transformers, SBERT, Siamese networks, RRF, theory-of-mind QA — are in the full `citations[]` array in the frontmatter for future `/citation-walk` use.)

## Related Digests

- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo) — the benchmark this paper's headline numbers are measured on; QRRanker pushes LoCoMo Overall F1 from the 37.8% baseline (GPT-3.5-16K) and 42-53 range (memory-augmented baselines) to 57.32 with GPT-5-mini, narrowing — but not closing — the gap to the 87.9% human ceiling.
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory — directly compared as a LoCoMo baseline; QRRanker beats Mem0 by +11.94 Overall F1 with a smaller token budget, suggesting Mem0's write-time graph effort underperforms a better retriever on a flat store.
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20 — also gets large gains on long-conversation benchmarks but via the opposite philosophy (four epistemic memory networks plus retain/recall/reflect ops); contrast with QRRanker's "flat memory + smarter rerank" position.
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory — argues write-time intelligence is anti-intelligence; QRRanker is a clean empirical instance of that thesis applied to dialogue memory specifically.
- [[packer-2023-memgpt-os]] — MemGPT — the OS-tier view of memory; QRRanker is downstream of any paging system and would slot in as the "what to fetch when paged-in" retrieval primitive.

## Reviewer Notes

**Overall severity:** Clean

All quantitative claims (LoCoMo F1 57.03 / 57.32, NarrativeQA 33.61, DetectiveQA 67.25, latency 910ms middle-layer / 1095ms full, peak memory 8.71GB / 11.18GB, 854-token budget, 16 QR heads, 1000-sample seed set, Qwen3-4B-Instruct-2507 backbone, layer-24 truncation, top-50 → top-3 pipeline, contrastive loss with multi-positive group formulation, summary-prefix gains of +0.70 / +1.02 / +2.67 with the HotpotQA -0.30 / MuSiQue -0.03 honest regressions) cross-checked against Tables 1-7 and §4-6 of the paper. The "what experts overlook" claim about head drift between precomputed QR heads and trained heads is sourced directly from §6.3 and Appendix E. The framing of "smarter retrieval beats sophisticated write-time memory" is the paper's own conclusion in §2 ("a more powerful search for history, with simple memory construction, can beat complicated memory management"). No fabricated metrics, methods, or attributions detected.
