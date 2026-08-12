---
corpus: agentic-memory
kind: paper-digest
slug: hu-2025-memoryagentbench
title: "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions"
authors:
  - "Hu, Yuanzhe"
  - "Wang, Yu"
  - "McAuley, Julian"
year: 2025
publication_date: "2025-07"
venue: "ICLR 2026 (arXiv:2507.05257)"
source_url: "https://arxiv.org/abs/2507.05257"
doi: null
arxiv_id: "2507.05257"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Every existing memory agent — long-context model, RAG variant, or commercial system like Mem0/MIRIX/MemGPT — wins on at most two of the four core memory competencies, and all of them collapse to ≤7% accuracy on multi-hop selective forgetting, exposing forgetting/updating as the structural blind spot of the field."
topics:
  - memory-agents
  - llm-evaluation
  - benchmarks
  - long-context
  - retrieval-augmented-generation
  - selective-forgetting
  - test-time-learning
  - agentic-memory
tags:
  - paper
  - benchmark
  - memory
  - rag
  - agentic-memory
  - iclr-2026
entities:
  - hu-yuanzhe
  - wang-yu
  - mcauley-julian
related_digests:
  - maharana-2024-locomo
  - wu-2024-longmemeval
  - chhikara-2025-mem0
  - wang-2025-mirix
  - packer-2023-memgpt-os
  - du-2025-rethinking-memory
  - hu-2026-evermemos
  - adler-2026-storage-not-memory
citations:
  - title: "Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)"
    authors: ["Maharana, A.", "Lee, D.-H.", "Tulyakov, S.", "Bansal, M.", "Barbieri, F.", "Fang, Y."]
    year: 2024
    arxiv_id: "2402.17753"
    url: "https://arxiv.org/abs/2402.17753"
    doi: null
  - title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
    authors: ["Wu, D.", "Wang, H.", "Yu, W.", "Zhang, Y.", "Chang, K.-W.", "Yu, D."]
    year: 2025
    arxiv_id: null
    url: "https://openreview.net/forum?id=pZiyCaVuti"
    doi: null
  - title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
    authors: ["Chhikara, P.", "Khant, D.", "Aryan, S.", "Singh, T.", "Yadav, D."]
    year: 2025
    arxiv_id: "2504.19413"
    url: "https://arxiv.org/abs/2504.19413"
    doi: null
  - title: "MIRIX: Multi-Agent Memory System for LLM-Based Agents"
    authors: ["Wang, Y.", "Chen, X."]
    year: 2025
    arxiv_id: "2507.07957"
    url: "https://arxiv.org/abs/2507.07957"
    doi: null
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Packer, C.", "Fang, V.", "Patil, S. G.", "Lin, K.", "Wooders, S.", "Gonzalez, J. E."]
    year: 2023
    arxiv_id: "2310.08560"
    url: "https://arxiv.org/abs/2310.08560"
    doi: null
  - title: "From Local to Global: A GraphRAG Approach to Query-Focused Summarization"
    authors: ["Edge, D.", "Trinh, H.", "Cheng, N.", "Bradley, J.", "Chao, A.", "Mody, A.", "Truitt, S.", "Metropolitansky, D.", "Ness, R. O.", "Larson, J."]
    year: 2024
    arxiv_id: "2404.16130"
    url: "https://arxiv.org/abs/2404.16130"
    doi: null
  - title: "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models (HippoRAG-V2)"
    authors: ["Gutiérrez, B. J.", "Shu, Y.", "Qi, W.", "Zhou, S.", "Su, Y."]
    year: 2025
    arxiv_id: "2502.14802"
    url: "https://arxiv.org/abs/2502.14802"
    doi: null
  - title: "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval"
    authors: ["Sarthi, P.", "Abdullah, S.", "Tuli, A.", "Khanna, S.", "Goldie, A.", "Manning, C. D."]
    year: 2024
    arxiv_id: "2401.18059"
    url: "https://arxiv.org/abs/2401.18059"
    doi: null
  - title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
    authors: ["Rasmussen, P.", "Paliychuk, P.", "Beauvais, T.", "Ryan, J.", "Chalef, D."]
    year: 2025
    arxiv_id: "2501.13956"
    url: "https://arxiv.org/abs/2501.13956"
    doi: null
  - title: "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
    authors: ["Asai, A.", "Wu, Z.", "Wang, Y.", "Sil, A.", "Hajishirzi, H."]
    year: 2024
    arxiv_id: "2310.11511"
    url: "https://arxiv.org/abs/2310.11511"
    doi: null
  - title: "A-MEM: Agentic Memory for LLM Agents"
    authors: ["Xu, W.", "Mei, K.", "Gao, H.", "Tan, J.", "Liang, Z.", "Zhang, Y."]
    year: 2025
    arxiv_id: "2502.12110"
    url: "https://arxiv.org/abs/2502.12110"
    doi: null
  - title: "MemoryBank: Enhancing Large Language Models with Long-Term Memory"
    authors: ["Zhong, W.", "Guo, L.", "Gao, Q.", "Wang, Y."]
    year: 2023
    arxiv_id: "2305.10250"
    url: "https://arxiv.org/abs/2305.10250"
    doi: null
  - title: "MQUAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions"
    authors: ["Zhong, Z.", "Wu, Z.", "Manning, C. D.", "Potts, C.", "Chen, D."]
    year: 2023
    arxiv_id: "2305.14795"
    url: "https://arxiv.org/abs/2305.14795"
    doi: null
  - title: "Infinity-Bench: Extending Long Context Evaluation Beyond 100K Tokens"
    authors: ["Zhang, X.", "Chen, Y.", "Hu, S.", "Xu, Z.", "Chen, J.", "Hao, M.", "Han, X.", "Thai, Z.", "Wang, S.", "Liu, Z."]
    year: 2024
    arxiv_id: "2402.13718"
    url: "https://arxiv.org/abs/2402.13718"
    doi: null
  - title: "RULER: What's the Real Context Size of Your Long-Context Language Models?"
    authors: ["Hsieh, C.-P.", "Sun, S.", "Kriman, S.", "Acharya, S.", "Rekesh, D.", "Jia, F.", "Zhang, Y.", "Ginsburg, B."]
    year: 2024
    arxiv_id: "2404.06654"
    url: "https://arxiv.org/abs/2404.06654"
    doi: null
  - title: "DetectiveQA: Evaluating Long-Context Reasoning on Detective Novels"
    authors: ["Xu, Z.", "Ye, J.", "Liu, X.", "Liu, X.", "Sun, T.", "Liu, Z.", "Guo, Q.", "Li, L.", "Liu, Q.", "Huang, X."]
    year: 2024
    arxiv_id: "2409.02465"
    url: "https://arxiv.org/abs/2409.02465"
    doi: null
  - title: "BANKING77: Efficient Intent Detection with Dual Sentence Encoders"
    authors: ["Casanueva, I.", "Temčinas, T.", "Gerz, D.", "Henderson, M.", "Vulić, I."]
    year: 2020
    arxiv_id: "2003.04807"
    url: "https://aclanthology.org/2020.nlp4convai-1.5/"
    doi: null
  - title: "CLINC150: An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction"
    authors: ["Larson, S.", "Mahendran, A.", "Peper, J. J.", "Clarke, C.", "Lee, A.", "Hill, P.", "Kummerfeld, J. K.", "Leach, K.", "Laurenzano, M. A.", "Tang, L.", "Mars, J."]
    year: 2019
    arxiv_id: "1909.02027"
    url: "https://aclanthology.org/D19-1131/"
    doi: null
  - title: "In-Context Learning with Long-Context Models: An In-Depth Exploration"
    authors: ["Bertsch, A.", "Ivgi, M.", "Xiao, E.", "Alon, U.", "Berant, J.", "Gormley, M. R.", "Neubig, G."]
    year: 2024
    arxiv_id: "2405.00200"
    url: "https://arxiv.org/abs/2405.00200"
    doi: null
  - title: "Large Language Models as Zero-Shot Conversational Recommenders"
    authors: ["He, Z.", "Xie, Z.", "Jha, R.", "Steck, H.", "Liang, D.", "Feng, Y.", "Majumder, B. P.", "Kallus, N.", "McAuley, J."]
    year: 2023
    arxiv_id: "2308.10053"
    url: "https://arxiv.org/abs/2308.10053"
    doi: null
  - title: "HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly"
    authors: ["Yen, H.", "Gao, T.", "Hou, M.", "Ding, K.", "Fleischer, D.", "Izsak, P.", "Wasserblat, M.", "Chen, D."]
    year: 2024
    arxiv_id: "2410.02694"
    url: "https://arxiv.org/abs/2410.02694"
    doi: null
  - title: "MemoryLLM: Towards Self-Updatable Large Language Models"
    authors: ["Wang, Y.", "Gao, Y.", "Chen, X.", "Jiang, H.", "Li, S.", "Yang, J.", "Yin, Q.", "Li, Z.", "Li, X.", "Yin, B."]
    year: 2024
    arxiv_id: "2402.04624"
    url: "https://arxiv.org/abs/2402.04624"
    doi: null
  - title: "Mass-Editing Memory in a Transformer"
    authors: ["Meng, K.", "Sharma, A. S.", "Andonian, A. J.", "Belinkov, Y.", "Bau, D."]
    year: 2023
    arxiv_id: "2210.07229"
    url: "https://openreview.net/forum?id=MkbcAHIYgyS"
    doi: null
  - title: "BM25 / Some Simple Effective Approximations to the 2-Poisson Model for Probabilistic Weighted Retrieval"
    authors: ["Robertson, S. E.", "Walker, S."]
    year: 1994
    arxiv_id: null
    url: null
    doi: "10.1007/978-1-4471-2099-5_24"
  - title: "Unsupervised Dense Information Retrieval with Contrastive Learning (Contriever)"
    authors: ["Izacard, G.", "Caron, M.", "Hosseini, L.", "Riedel, S.", "Bojanowski, P.", "Joulin, A.", "Grave, E."]
    year: 2021
    arxiv_id: "2112.09118"
    url: "https://arxiv.org/abs/2112.09118"
    doi: null
  - title: "Qwen3 Embedding: Advancing Text Embedding and Reranking through Foundation Models"
    authors: ["Zhang, Y.", "Li, M.", "Long, D.", "Zhang, X.", "Lin, H.", "Yang, B.", "Xie, P.", "Yang, A.", "Liu, D.", "Lin, J."]
    year: 2025
    arxiv_id: "2506.05176"
    url: "https://arxiv.org/abs/2506.05176"
    doi: null
  - title: "MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation"
    authors: ["Qian, H.", "Liu, Z.", "Zhang, P.", "Mao, K.", "Lian, D.", "Dou, Z.", "Huang, T."]
    year: 2025
    arxiv_id: "2409.05591"
    url: "https://arxiv.org/abs/2409.05591"
    doi: null
  - title: "Why There Are Complementary Learning Systems in the Hippocampus and Neocortex"
    authors: ["McClelland, J. L.", "McNaughton, B. L.", "O'Reilly, R. C."]
    year: 1995
    arxiv_id: null
    url: "https://pubmed.ncbi.nlm.nih.gov/7624455/"
    doi: "10.1037/0033-295X.102.3.419"
  - title: "Retrieval Induces Adaptive Forgetting of Competing Memories via Cortical Pattern Suppression"
    authors: ["Wimber, M.", "Alink, A.", "Charest, I.", "Kriegeskorte, N.", "Anderson, M. C."]
    year: 2015
    arxiv_id: null
    url: "https://www.nature.com/articles/nn.3973"
    doi: "10.1038/nn.3973"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Four complementary competencies that memory agents should have"
  page: 2
  image_path: "figures/hu-2025-memoryagentbench-fig.png"
---

# Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions

**Authors:** Yuanzhe Hu, Yu Wang, Julian McAuley (UC San Diego)
**Published:** 2025-07 · [Source](https://arxiv.org/abs/2507.05257) · ICLR 2026
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

This paper argues that memory in LLM agents is currently under-evaluated because existing benchmarks were designed for either short-context QA (LoCoMo, LongBench) or static long-context reading (NovelQA, Infinity-Bench, NOCHA) — none of which match the incremental, multi-turn way real memory agents actually consume information. The authors propose four core competencies drawn from cognitive-science classics (James 1890; McClelland 1995; Wimber 2015): **Accurate Retrieval (AR)**, **Test-Time Learning (TTL)**, **Long-Range Understanding (LRU)**, and **Selective Forgetting (SF)**. They release **MemoryAgentBench**, a 2,071-question benchmark spanning context depths from 103K to 1.44M tokens, built by (a) reformatting existing datasets into chunked multi-turn dialogues that get fed to the agent piece-by-piece, and (b) constructing two new datasets — **EventQA** (novel-event ordering, ~534K tokens) and **FactConsolidation** (counterfactual edits from MQUAKE concatenated into 6K–262K contexts, used to test forgetting). They evaluate 20+ memory agents in three families — long-context LLMs (GPT-4o, GPT-4.1-mini, Gemini-2.0-Flash, Claude-3.7-Sonnet), RAG variants (BM25, Contriever, OpenAI/Qwen3 embeddings, RAPTOR, GraphRAG, MemoRAG, HippoRAG-v2), and commercial memory agents (Mem0, Cognee, Zep, MemGPT, MIRIX, Self-RAG). The headline result: no single agent type wins across all four competencies, and **every method collapses on multi-hop selective forgetting (≤7% accuracy)**. Long-context agents dominate TTL/LRU; RAG dominates AR; nothing handles SF. With a stronger backbone (GPT-4.1-mini), MIRIX jumps +9.7 points on average, suggesting agentic memory still has headroom — but the SF cliff persists even with o4-mini reasoning models when contexts cross 32K tokens.

## Key Takeaway

**Every existing memory agent — long-context model, RAG variant, or commercial system like Mem0/MIRIX/MemGPT — wins on at most two of the four core memory competencies, and all of them collapse to ≤7% accuracy on multi-hop selective forgetting, exposing forgetting/updating as the structural blind spot of the field.** Concretely: the best long-context model (Claude-3.7-Sonnet) reaches 62.2 on LRU but only 22.5 on SF; the best RAG agent (HippoRAG-v2) reaches 65.1 on AR but 19.9 on LRU; the best agentic system in the table (MIRIX with GPT-4.1-mini backbone) reaches 63.0 on AR but only 11.5 on SF. The numbers say the field has been optimising for retrieval while quietly assuming that "remembering" and "un-remembering" are the same competency — they aren't.

## Implications

1. **The four-competency frame is now load-bearing for memory benchmarks.** AR/TTL/LRU/SF gives the field a vocabulary it didn't have. Any new memory system shipped after this paper will be expected to report all four numbers — the way long-context models report needle-in-a-haystack at multiple depths.

2. **Selective forgetting is the next big benchmark target.** Multi-hop SF performance is 1–7% across all systems including o4-mini reasoning models at 32K context. This is one of the lowest absolute numbers in any agent benchmark right now and reads as an open problem rather than a saturated one.

3. **The "memory ≠ long context" distinction has been operationalised.** Earlier critiques of long-context-as-memory were intuitive arguments. This benchmark codifies the difference: feeding context as chunks with explicit memorisation instructions, then querying later, produces different rankings than feeding the same content as a single block. RAG systems that look great on static long-context QA degrade when forced into the streaming setup.

4. **RAG-vs-memory-agent is more nuanced than "agentic wins."** Simple BM25 outperforms most embedding-based and structure-augmented RAG systems on the headline overall score (41.5 vs ~37–38), and outperforms three of the four commercial memory agents (Cognee 20.6, Mem0 21.1, Zep 24.0). MemGPT and MIRIX only catch up when given GPT-4.1-mini. Translation: a lot of "memory" engineering is still being beaten by a 1994 retrieval algorithm with a fresh backbone.

5. **The "backbone is no longer the bottleneck" finding for RAG cuts against a common assumption.** Upgrading BM25's backbone from 4o-mini to 4.1-mini gives +1.4 points. Upgrading MIRIX's backbone gives +9.7 points. This implies that for pure retrieval-style memory the LLM is now mostly downstream of retrieval quality, while for agentic memory the LLM's reasoning still gates the whole system. Useful diagnostic: if your memory system gets a lot better when you upgrade the model, you're doing agentic memory; if it doesn't, you're doing retrieval.

6. **The benchmark itself is the most reusable artefact.** Datasets and code are open-sourced under MIT/CC BY 4.0, and the EventQA pipeline is described as fully automated for any novel-style text — meaning anyone with a corpus of long-form narrative can spin up a comparable memory benchmark for their domain.

## How to Apply It (method)

The methodology breaks into four moves:

**1. Pick four memory competencies grounded in cognitive science.**
- **AR** (accurate retrieval): can the agent extract a snippet given a query — single- or multi-hop, but answerable from one query? Operationalised via SH-Doc QA (197K), MH-Doc QA (421K), LongMemEval (S\*) at 355K, and the new EventQA at 534K.
- **TTL** (test-time learning): can the agent acquire a new skill in-context from accumulated examples? Operationalised via five classification datasets (BANKING77, CLINC150, NLU, TREC-Coarse, TREC-Fine) at 103K tokens, plus a 1.44M-token movie-recommendation task.
- **LRU** (long-range understanding): can the agent integrate information across the whole input to answer global questions? Operationalised via Infinity-Bench novel summarisation (172K) and a hard subset of DetectiveQA (124K).
- **SF** (selective forgetting): can the agent overwrite stale facts with newer contradictory ones? Operationalised via FactConsolidation, built from MQUAKE counterfactual edit pairs concatenated into contexts of 6K, 32K, 64K, 262K tokens.

**2. Reformat every dataset into chunked multi-turn input.**
Standard format: chunks `c1...cn` (paired with "memorise this" instructions) followed by questions `q1...qm`. For FactConsolidation, an explicit guardrail is added: "facts are indexed by serial numbers; newer facts have larger serial numbers; resolve conflicts by finding the newest fact." Chunk size is 512 for AR/SF tasks composed of synthesised short texts, and 4096 elsewhere (and uniformly 4096 for Mem0/Cognee/Zep/MIRIX). This is the part you'd reproduce most directly.

**3. Run three categories of agents with standardised prompt templates.**
- **Long-context agents** keep a FIFO buffer of the most recent tokens until the window fills.
- **RAG agents** split into Simple (BM25), Embedding (Contriever, OpenAI text-embed-3-{small,large}, Qwen3-Embedding-4B), and Structure-Augmented (RAPTOR, GraphRAG, MemoRAG, HippoRAG-v2, plus the commercial Mem0/Cognee/Zep).
- **Agentic memory agents** (Self-RAG, MemGPT, MIRIX) run iterative reformulate-retrieve-reflect loops.

For the AR/SF sub-tasks where the input is synthesised, chunk size is 512; everywhere else it's 4096. Retrieval top-k is held at 10 for the headline table, with ablations at 2/5/10 and chunk-size ablations at 512/1024/2048/4096.

**4. Report a per-competency average plus an overall score.**
For each competency, average the per-dataset numbers; for overall, average the four competency averages. This protects systems that are excellent on one competency from getting hidden by the global mean — and it makes the four-axis weakness pattern visible at a glance in Table 3.

**To use this as a yardstick for your own memory system:** clone the repo, swap your agent in for one of the three roles, run it under the same chunk-size and top-k settings, and compare on the AR-TTL-LRU-SF radar. A claim that "system X has good memory" without numbers on all four is now incomplete by construction.

## Best Figure

![Figure 1 — Four complementary competencies that memory agents should have (page 2)](figures/hu-2025-memoryagentbench-fig.png)

Figure 1 is the conceptual core of the paper: four cartoon panels show the same persona being asked to do AR ("What did I see at the zoo?"), TTL ("Which class is A1? Which class is B1?" after seeing labeled examples), LRU ("Help me summarize the story"), and SF ("Do I love pears?" after the user first said "I love the pear" then later "I don't like fruits. I love peas"). The figure works because it makes the four-competency frame intuitive in a way the prose alone doesn't: each panel forces a different cognitive operation, and the SF panel in particular makes obvious that overwriting old information is qualitatively different from retrieving it. Everything else in the paper — the benchmark design, the evaluation protocol, the headline finding — is downstream of accepting these four as the right partition.

**Figure Page: 2**

## What Experts Overlook

A reader who is already deep in memory-agent research is most likely to skim past the following three findings.

1. **BM25 beats almost every commercial memory agent on the overall score.** BM25 hits 41.5 overall; Mem0 21.1, Cognee 20.6, Zep 24.0, MemGPT 28.3, MIRIX 26.2. The structure-augmented Mem0/Cognee/Zep systems are getting outscored by a non-neural string-matching algorithm from 1994 because they sacrifice raw retrieval coverage for graph structure that doesn't translate to AR/TTL/LRU gains. This is a structural critique of the "build a knowledge graph for agent memory" line of work — at least under this benchmark's setup.

2. **Embedding-based RAG performance is surprisingly flat across embedding choices.** Contriever 33.9 → text-embed-3-small 53.8 → text-embed-3-large 54.6 → Qwen3-Embedding-4B 54.7. Going from a 2021 BERT-based retriever to a 2025 state-of-the-art embedding model gives a meaningful jump, but the gap between text-embed-3-small and the much-newer Qwen3-Embedding-4B is under 1 point. The intuition "newer embedding = better memory" doesn't really survive contact with the benchmark.

3. **Backbone-upgrade gains are categorical, not continuous.** Table 4 shows that swapping GPT-4o-mini for GPT-4.1-mini gives BM25 +1.4 points, text-embed-3-small +0.4, GraphRAG +1.9, but **MIRIX +9.7**. The simple reading is "agentic memory benefits more from a stronger backbone." The less-obvious reading is that this is a diagnostic test for whether a memory system is bottlenecked on retrieval or on reasoning. If your system doesn't move much when you upgrade the LLM, the LLM isn't the limiting factor — your retriever is. If it does move, you have an agentic loop whose effectiveness scales with model capability. This is a more useful diagnostic than the "overall score" column.

A fourth, easier-to-miss point: the SF results for reasoning models (Table 5) show o4-mini going from 100% on the 6K version of FactCon-SH to 61% at 32K, and from 80% on the 6K version of FactCon-MH to 14% at 32K. The authors frame this as "our dataset is solvable, the problem is long-range." It also reads as "selective forgetting decays roughly with context length even for the best reasoning model available" — a sharper claim than "memory agents fail at SF."

## Extracted Prompts

The paper uses fixed templates across all agents. Excerpts shown in Figure 5 of the paper (Appendix D):

**Memorisation wrapper (every chunk):**
> "Please memorize it and I will ask some questions about it later."

**Selective Forgetting guardrail (FactConsolidation):**
> "Facts are indexed by serial numbers. Newer facts have larger serial numbers. When two facts conflict, prioritise the fact with the larger serial number."

**TTL / classification template (paraphrased from §3.3):**
> "Given the labeled examples you have seen, map the following sentence to one of the class labels."

**Recommendation template (paraphrased from §3.3):**
> "Based on the long dialogue history of movie-related interactions, recommend twenty relevant movies."

**Detective QA (paraphrased):**
> "Reason over the events in the novel you have been reading and answer the following question."

These prompts are intentionally minimal and uniform — the comparison is between memory architectures, not between prompt-engineering tricks. For anyone running their own memory eval, treating the "memorise this chunk" wrapper as a contract between the harness and the agent (rather than an optional instruction) is the part that most cleanly separates "long-context QA" from "memory benchmarking."

## Citations

The paper cites ~70 works across long-context benchmarks, RAG systems, memory agents, and cognitive-science theory. Highlights with arxiv IDs (full list in frontmatter):

- LoCoMo — Maharana et al. 2024 (arXiv:2402.17753) — the prior dominant memory benchmark, ~9K tokens
- LongMemEval — Wu et al. 2025 — synthetic long-form conversations, the closest prior art to this paper
- MemGPT — Packer et al. 2023 (arXiv:2310.08560) — LLM-as-OS memory architecture
- MIRIX — Wang & Chen 2025 (arXiv:2507.07957) — multi-agent memory system, top agentic performer here
- Mem0 — Chhikara et al. 2025 (arXiv:2504.19413) — production memory layer
- HippoRAG-v2 — Gutiérrez et al. 2025 (arXiv:2502.14802) — best structure-augmented RAG on this benchmark
- GraphRAG — Edge et al. 2024 (arXiv:2404.16130) — knowledge-graph RAG baseline
- RAPTOR — Sarthi et al. 2024 (arXiv:2401.18059) — tree-organised retrieval baseline
- Zep — Rasmussen et al. 2025 (arXiv:2501.13956) — temporal-KG memory architecture
- MQUAKE — Zhong et al. 2023 (arXiv:2305.14795) — counterfactual edit pairs, source of FactConsolidation
- Infinity-Bench — Zhang et al. 2024 (arXiv:2402.13718) — long-context benchmark, source of En.Sum
- DetectiveQA — Xu et al. 2024 (arXiv:2409.02465) — long-range narrative reasoning
- HELMET — Yen et al. 2024 (arXiv:2410.02694) — long-context eval framework, source of TTL setup
- RULER — Hsieh et al. 2024 (arXiv:2404.06654) — long-context measurement framework
- James 1890 — cognitive theory of primary/secondary memory
- McClelland et al. 1995 — complementary learning systems theory
- Wimber et al. 2015 — adaptive forgetting via cortical pattern suppression

## Related Digests

- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents — the prior memory benchmark this paper supersedes (9K tokens, AR only)
- [[wu-2024-longmemeval]] — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory — closest prior art for chunked multi-turn evaluation
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory — one of the commercial systems evaluated here (21.1 overall)
- [[wang-2025-mirix]] — MIRIX: Multi-Agent Memory System for LLM-Based Agents — top agentic-memory performer in this benchmark (37.7 with 4.1-mini)
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems — agentic memory baseline (28.3 overall)
- [[du-2025-rethinking-memory]] — Rethinking Memory in LLM based Agents: Representations, Operations, and Emerging Topics — complementary survey of memory operations (write/update/forget) that maps onto AR/TTL/LRU/SF
- [[hu-2026-evermemos]] — EverMemOS — write-time consolidation argument that becomes more interesting once SF is the bottleneck
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory — retrieval-centred architecture whose claims should be re-evaluated under the four-competency frame

## Reviewer Notes

**Hallucination severity: Clean.**

Spot checks against the paper text:
- "Multi-hop SF ≤7%": paper Table 3 shows FC-MH column max of 7.0 (Contriever, MemoRAG, MIRIX). ✓
- "BM25 41.5 overall": Table 3 row "BM25" overall column = 41.5. ✓
- "MIRIX +9.7 with 4.1-mini": Table 4, MIRIX row, Avg. column = "25.6 (9.7↑)". ✓
- "Claude-3.7-Sonnet LRU 62.2": Table 3, Long-Context row, LRU Avg. column. ✓
- "EventQA ~534K tokens": Table 2 row EventQA, AvgL. column. ✓
- "MQUAKE source for FactConsolidation": §3.1 explicitly states this. ✓
- "James 1890; McClelland 1995; Wimber 2015 as cognitive grounding": §1 and §Appendix B references. ✓
- "Chunk size 512 for AR/SF synthetic, 4096 elsewhere": §4.1. ✓

One interpretive choice worth flagging: the digest treats the paper's framing of "memory ≠ long context" as a strong claim. The paper itself is slightly hedged — it argues that long-context benchmarks don't *directly* apply to memory agents because they don't simulate incremental ingestion, not that the underlying competency is different in kind. Readers should not over-extend this to "long-context models can't have memory" — the paper actually finds long-context models win two of four competencies.

No fabricated numbers, no invented citations.
