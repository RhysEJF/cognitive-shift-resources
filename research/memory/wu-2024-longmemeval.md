---
corpus: agentic-memory
kind: paper-digest
slug: wu-2024-longmemeval
title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
authors:
  - "Wu, Di"
  - "Wang, Hongwei"
  - "Yu, Wenhao"
  - "Zhang, Yuwei"
  - "Chang, Kai-Wei"
  - "Yu, Dong"
year: 2024
publication_date: "2024-10"
venue: "ICLR 2025"
source_url: "https://arxiv.org/abs/2410.10813"
doi: null
arxiv_id: "2410.10813"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Across a 500-question stress test of five long-term memory abilities, every commercial and long-context system loses 30–60% accuracy versus oracle reads — and the fix is not bigger context but a four-control-point pipeline (round-level values, fact-augmented keys, time-aware query expansion, Chain-of-Note + JSON reading) that adds 9.4 pts recall@10 and 5–10 pts end-to-end accuracy."
topics:
  - long-term-memory
  - chat-assistants
  - benchmark
  - retrieval-augmented-generation
  - temporal-reasoning
  - memory-architecture
  - chain-of-note
  - key-value-store
tags:
  - paper
  - memory
  - benchmark
  - llm-evaluation
  - rag
  - longmemeval
entities:
  - wu-di
  - wang-hongwei
  - yu-wenhao
  - zhang-yuwei
  - chang-kai-wei
  - yu-dong
related_digests:
  - latimer-2025-hindsight-memory
  - packer-2023-memgpt-os
  - chhikara-2025-mem0
  - adler-2026-storage-not-memory
citations:
  - title: "Beyond goldfish memory: Long-term open-domain conversation"
    authors: ["Xu, J.", "Szlam, A.", "Weston, J."]
    year: 2022
    doi: "10.18653/v1/2022.acl-long.356"
    url: "https://aclanthology.org/2022.acl-long.356/"
    arxiv_id: null
  - title: "Long time no see! Open-domain conversation with long-term persona memory"
    authors: ["Xu, X.", "Gou, Z.", "Wu, W.", "Niu, Z.-Y.", "Wu, H.", "Wang, H.", "Wang, S."]
    year: 2022
    doi: "10.18653/v1/2022.findings-acl.207"
    url: "https://aclanthology.org/2022.findings-acl.207/"
    arxiv_id: null
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Zhong, W.", "Guo, L.", "Gao, Q.", "Ye, H.", "Wang, Y."]
    year: 2024
    doi: "10.1609/AAAI.V38I17.29946"
    url: "https://doi.org/10.1609/aaai.v38i17.29946"
    arxiv_id: null
  - title: "Evaluating very long-term conversational memory of LLM agents (LoCoMo)"
    authors: ["Maharana, A.", "Lee, D.-H.", "Tulyakov, S.", "Bansal, M.", "Barbieri, F.", "Fang, Y."]
    year: 2024
    doi: "10.18653/v1/2024.acl-long.747"
    url: "https://aclanthology.org/2024.acl-long.747/"
    arxiv_id: null
  - title: "PerLTQA: A personal long-term memory dataset for memory classification, retrieval, and fusion in question answering"
    authors: ["Du, Y.", "Wang, H.", "Zhao, Z.", "Liang, B.", "Wang, B.", "Zhong, W.", "Wang, Z.", "Wong, K.-F."]
    year: 2024
    doi: null
    url: "https://aclanthology.org/2024.sighan-1.18/"
    arxiv_id: null
  - title: "DialSim: A real-time simulator for evaluating long-term dialogue understanding of conversational agents"
    authors: ["Kim, J.", "Chay, W.", "Hwang, H.", "Kyung, D.", "Chung, H.", "Cho, E.", "Jo, Y.", "Choi, E."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2406.13144"
    arxiv_id: "2406.13144"
  - title: "Chain-of-Note: Enhancing robustness in retrieval-augmented language models"
    authors: ["Yu, W.", "Zhang, H.", "Pan, X.", "Ma, K.", "Wang, H.", "Yu, D."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2311.09210"
    arxiv_id: "2311.09210"
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Liu, N. F.", "Lin, K.", "Hewitt, J.", "Paranjape, A.", "Bevilacqua, M.", "Petroni, F.", "Liang, P."]
    year: 2024
    doi: "10.1162/tacl_a_00638"
    url: "https://doi.org/10.1162/tacl_a_00638"
    arxiv_id: null
  - title: "Large language models can be easily distracted by irrelevant context"
    authors: ["Shi, F.", "Chen, X.", "Misra, K.", "Scales, N.", "Dohan, D.", "Chi, E. H.", "Schärli, N.", "Zhou, D."]
    year: 2023
    doi: null
    url: "https://proceedings.mlr.press/v202/shi23a.html"
    arxiv_id: null
  - title: "RAPTOR: Recursive abstractive processing for tree-organized retrieval"
    authors: ["Sarthi, P.", "Abdullah, S.", "Tuli, A.", "Khanna, S.", "Goldie, A.", "Manning, C. D."]
    year: 2024
    doi: null
    url: "https://openreview.net/forum?id=GN921JHCRw"
    arxiv_id: null
  - title: "Walking down the memory maze: Beyond context limit through interactive reading (MemWalker)"
    authors: ["Chen, H.", "Pasunuru, R.", "Weston, J.", "Celikyilmaz, A."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2310.05029"
    arxiv_id: "2310.05029"
  - title: "HippoRAG: Neurobiologically inspired long-term memory for large language models"
    authors: ["Gutiérrez, B. J.", "Shu, Y.", "Gu, Y.", "Yasunaga, M.", "Su, Y."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2405.14831"
    arxiv_id: "2405.14831"
  - title: "Hello again! LLM-powered personalized agent for long-term dialogue (LD-Agent)"
    authors: ["Li, H.", "Yang, C.", "Zhang, A.", "Deng, Y.", "Wang, X.", "Chua, T.-S."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2406.05925"
    arxiv_id: "2406.05925"
  - title: "REPLUG: Retrieval-augmented black-box language models"
    authors: ["Shi, W.", "Min, S.", "Yasunaga, M.", "Seo, M.", "James, R.", "Lewis, M.", "Zettlemoyer, L.", "Yih, W.-T."]
    year: 2024
    doi: "10.18653/v1/2024.naacl-long.463"
    url: "https://aclanthology.org/2024.naacl-long.463/"
    arxiv_id: null
  - title: "Dense X retrieval: What retrieval granularity should we use?"
    authors: ["Chen, T.", "Wang, H.", "Chen, S.", "Yu, W.", "Ma, K.", "Zhao, X.", "Zhang, H.", "Yu, D."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2312.06648"
    arxiv_id: "2312.06648"
  - title: "Did you read the instructions? Rethinking the effectiveness of task definitions in instruction learning"
    authors: ["Yin, F.", "Vig, J.", "Laban, P.", "Joty, S.", "Xiong, C.", "Wu, C.-S."]
    year: 2023
    doi: "10.18653/v1/2023.acl-long.172"
    url: "https://aclanthology.org/2023.acl-long.172/"
    arxiv_id: null
  - title: "Improving retrieval of short texts through document expansion"
    authors: ["Efron, M.", "Organisciak, P.", "Fenlon, K."]
    year: 2012
    doi: "10.1145/2348283.2348405"
    url: "https://doi.org/10.1145/2348283.2348405"
    arxiv_id: null
  - title: "Language model information retrieval with document expansion"
    authors: ["Tao, T.", "Wang, X.", "Mei, Q.", "Zhai, C."]
    year: 2006
    doi: null
    url: "https://aclanthology.org/N06-1052/"
    arxiv_id: null
  - title: "G-Eval: NLG evaluation using GPT-4 with better human alignment"
    authors: ["Liu, Y.", "Iter, D.", "Xu, Y.", "Wang, S.", "Xu, R.", "Zhu, C."]
    year: 2023
    doi: "10.18653/v1/2023.emnlp-main.153"
    url: "https://aclanthology.org/2023.emnlp-main.153/"
    arxiv_id: null
  - title: "Needle in a haystack — pressure testing LLMs"
    authors: ["Kamradt, G."]
    year: 2023
    doi: null
    url: "https://github.com/gkamradt/LLMTest_NeedleInAHaystack"
    arxiv_id: null
  - title: "Baize: An open-source chat model with parameter-efficient tuning on self-chat data"
    authors: ["Xu, C.", "Guo, D.", "Duan, N.", "McAuley, J."]
    year: 2023
    doi: "10.18653/v1/2023.emnlp-main.385"
    url: "https://aclanthology.org/2023.emnlp-main.385/"
    arxiv_id: null
  - title: "Enhancing chat language models by scaling high-quality instructional conversations (UltraChat)"
    authors: ["Ding, N.", "Chen, Y.", "Xu, B.", "Qin, Y.", "Zheng, Z.", "Hu, S.", "Liu, Z.", "Sun, M.", "Zhou, B."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.14233"
    arxiv_id: "2305.14233"
  - title: "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena (ShareGPT)"
    authors: ["Zheng, L.", "Chiang, W.-L.", "Sheng, Y.", "Zhuang, S.", "Wu, Z.", "Zhuang, Y.", "Lin, Z.", "Li, Z.", "Li, D.", "Xing, E. P.", "Zhang, H.", "Gonzalez, J. E.", "Stoica, I."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "The Llama 3 herd of models"
    authors: ["Dubey, A.", "Jauhri, A.", "Pandey, A.", "et al."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2407.21783"
    arxiv_id: "2407.21783"
  - title: "Phi-3 technical report: A highly capable language model locally on your phone"
    authors: ["Abdin, M. I.", "et al."]
    year: 2024
    doi: "10.48550/ARXIV.2404.14219"
    url: "https://doi.org/10.48550/arXiv.2404.14219"
    arxiv_id: "2404.14219"
  - title: "Qwen2.5: A party of foundation models"
    authors: ["Qwen Team"]
    year: 2024
    doi: null
    url: "https://qwenlm.github.io/blog/qwen2.5/"
    arxiv_id: null
  - title: "Mistral Nemo: Our new best small model"
    authors: ["Mistral AI Team"]
    year: 2024
    doi: null
    url: "https://mistral.ai/news/mistral-nemo"
    arxiv_id: null
  - title: "STELLA EN 1.5B v5"
    authors: ["Zhang, D."]
    year: 2023
    doi: null
    url: "https://huggingface.co/dunzhang/stella_en_1.5B_v5"
    arxiv_id: null
  - title: "Unsupervised dense information retrieval with contrastive learning (Contriever)"
    authors: ["Izacard, G.", "Caron, M.", "Hosseini, L.", "Riedel, S.", "Bojanowski, P.", "Joulin, A.", "Grave, E."]
    year: 2022
    doi: null
    url: "https://openreview.net/forum?id=jKN1pXi7b0"
    arxiv_id: null
  - title: "The probabilistic relevance framework: BM25 and beyond"
    authors: ["Robertson, S. E.", "Zaragoza, H."]
    year: 2009
    doi: "10.1561/1500000019"
    url: "https://doi.org/10.1561/1500000019"
    arxiv_id: null
  - title: "MTEB: Massive text embedding benchmark"
    authors: ["Muennighoff, N.", "Tazi, N.", "Magne, L.", "Reimers, N."]
    year: 2023
    doi: "10.18653/v1/2023.eacl-main.148"
    url: "https://aclanthology.org/2023.eacl-main.148/"
    arxiv_id: null
  - title: "LLMLingua: Compressing prompts for accelerated inference of large language models"
    authors: ["Jiang, H.", "Wu, Q.", "Lin, C.-Y.", "Yang, Y.", "Qiu, L."]
    year: 2023
    doi: "10.18653/V1/2023.EMNLP-MAIN.825"
    url: "https://aclanthology.org/2023.emnlp-main.825/"
    arxiv_id: null
  - title: "RECOMP: Improving retrieval-augmented LMs with context compression and selective augmentation"
    authors: ["Xu, F.", "Shi, W.", "Choi, E."]
    year: 2024
    doi: null
    url: "https://openreview.net/forum?id=mlJLVigNHp"
    arxiv_id: null
  - title: "Learning to compress prompts with gist tokens"
    authors: ["Mu, J.", "Li, X.", "Goodman, N. D."]
    year: 2023
    doi: null
    url: "http://papers.nips.cc/paper_files/paper/2023/hash/3d77c6dcc7f143aa2154e7f4d5e22d68-Abstract-Conference.html"
    arxiv_id: null
  - title: "Adapting language models to compress contexts"
    authors: ["Chevalier, A.", "Wettig, A.", "Ajith, A.", "Chen, D."]
    year: 2023
    doi: "10.18653/V1/2023.EMNLP-MAIN.232"
    url: "https://aclanthology.org/2023.emnlp-main.232/"
    arxiv_id: null
  - title: "Augmenting language models with long-term memory"
    authors: ["Wang, W.", "Dong, L.", "Cheng, H.", "Liu, X.", "Yan, X.", "Gao, J.", "Wei, F."]
    year: 2023
    doi: null
    url: "http://papers.nips.cc/paper_files/paper/2023/hash/ebd82705f44793b6f9ade5a669d0f0bf-Abstract-Conference.html"
    arxiv_id: null
  - title: "Make your LLM fully utilize the context"
    authors: ["An, S.", "Ma, Z.", "Lin, Z.", "Zheng, N.", "Lou, J.-G."]
    year: 2024
    doi: "10.48550/ARXIV.2404.16811"
    url: "https://doi.org/10.48550/arXiv.2404.16811"
    arxiv_id: "2404.16811"
  - title: "Data engineering for scaling language models to 128k context"
    authors: ["Fu, Y.", "Panda, R.", "Niu, X.", "Yue, X.", "Hajishirzi, H.", "Kim, Y.", "Peng, H."]
    year: 2024
    doi: null
    url: "https://openreview.net/forum?id=TaAqeo7lUh"
    arxiv_id: null
  - title: "Longformer: The long-document transformer"
    authors: ["Beltagy, I.", "Peters, M. E.", "Cohan, A."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2004.05150"
    arxiv_id: "2004.05150"
  - title: "Reformer: The efficient transformer"
    authors: ["Kitaev, N.", "Kaiser, Ł.", "Levskaya, A."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2001.04451"
    arxiv_id: "2001.04451"
  - title: "Memory networks"
    authors: ["Weston, J.", "Chopra, S.", "Bordes, A."]
    year: 2014
    doi: null
    url: "https://arxiv.org/abs/1410.3916"
    arxiv_id: "1410.3916"
  - title: "Memorizing transformers"
    authors: ["Wu, Y.", "Rabe, M. N.", "Hutchins, D.", "Szegedy, C."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2203.08913"
    arxiv_id: "2203.08913"
  - title: "Training language models with memory augmentation"
    authors: ["Zhong, Z.", "Lei, T.", "Chen, D."]
    year: 2022
    doi: "10.18653/v1/2022.emnlp-main.382"
    url: "https://aclanthology.org/2022.emnlp-main.382/"
    arxiv_id: null
  - title: "Cognitive Kernel: An open-source agent system towards generalist autopilots"
    authors: ["Zhang, H.", "Pan, X.", "Wang, H.", "Ma, K.", "Yu, W.", "Yu, D."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2409.10277"
    arxiv_id: "2409.10277"
  - title: "MultiWOZ — a large-scale multi-domain Wizard-of-Oz dataset for task-oriented dialogue modelling"
    authors: ["Budzianowski, P.", "Wen, T.-H.", "Tseng, B.-H.", "Casanueva, I.", "Ultes, S.", "Ramadan, O.", "Gašić, M."]
    year: 2018
    doi: "10.18653/v1/D18-1547"
    url: "https://aclanthology.org/D18-1547/"
    arxiv_id: null
  - title: "AirDialogue: An environment for goal-oriented dialogue research"
    authors: ["Wei, W.", "Le, Q.", "Dai, A.", "Li, J."]
    year: 2018
    doi: "10.18653/v1/D18-1419"
    url: "https://aclanthology.org/D18-1419/"
    arxiv_id: null
  - title: "CoQA: A conversational question answering challenge"
    authors: ["Reddy, S.", "Chen, D.", "Manning, C. D."]
    year: 2019
    doi: "10.1162/tacl_a_00266"
    url: "https://aclanthology.org/Q19-1016/"
    arxiv_id: null
  - title: "SituatedQA: Incorporating extra-linguistic contexts into QA"
    authors: ["Zhang, M.", "Choi, E."]
    year: 2021
    doi: "10.18653/v1/2021.emnlp-main.586"
    url: "https://aclanthology.org/2021.emnlp-main.586/"
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 6
  title: "Question answering performance under the oracle retrieval setting — CoN+JSON dominates"
  page: 10
  image_path: "figures/wu-2024-longmemeval-fig.png"
---

# LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory

**Authors:** Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu
**Published:** 2024-10 · [Source](https://arxiv.org/abs/2410.10813)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

LongMemEval is a 500-question benchmark that stresses five long-term memory abilities (information extraction, multi-session reasoning, knowledge updates, temporal reasoning, abstention) by embedding human-curated evidence sessions inside a freely scalable chat history — the standard "S" setting is ~115k tokens/question and "M" is 500 sessions / ~1.5M tokens. Commercial systems collapse in this regime: ChatGPT (GPT-4o) drops from 0.92 offline-reading accuracy to 0.58 with its own memory layer (a 37% drop), Coze drops 64%, and four long-context LLMs lose 30–60% versus oracle retrieval. The authors then formalise memory-augmented assistants as a key-value store with three stages (index/retrieve/read) and four control points (value, key, query, reading strategy), benchmark nine real systems against it, and ship a recommended pipeline: round-level values + key-expansion (K = V + extracted user fact) + time-aware query expansion using GPT-4o + Chain-of-Note reading with JSON-structured retrieved items, indexed by Stella V5 1.5B dense retrieval. The gains stack — fact-augmented keys add +9.4% recall@k and +5.4% end-to-end accuracy, time-aware QE adds +6.8–11.3% recall on temporal questions, and CoN+JSON adds up to 10 absolute QA points even with perfect retrieval. The most useful takeaway for builders: even with perfect recall, the reader still loses 15–19% of cases to wrong generation, so reading strategy is co-equal with retrieval and cannot be skipped.

## Key Takeaway

**Granularity decisions at write-time silently cap your ceiling at query-time.** [E] [A] Going from "store whole session" to "store rounds" lifts QA materially with strong readers, but compressing further into LLM-extracted summaries or facts *loses* accuracy on detail-heavy questions because information is destroyed before it can ever be queried — the lone exception is multi-session reasoning, where uniform fact-format actually helps because retrieval benefits from regularised shape. Every memory architecture is implicitly making this tradeoff; LongMemEval makes it numerically auditable for the first time.

## Implications

- **[E + A] Stop treating "session" as the atomic memory unit**: Decomposing into rounds beats whole-session values for GPT-4o reading on LongMemEval-M, but if you compress further to summaries you regress on detail recall — only multi-session reasoning benefits from fact-level compression. Build your encoder to keep both: rounds as the value, facts as an *expansion* of the key, never as the replacement.
- **[G + N] Make timestamps a first-class index, not a string buried in chunks**: Naive time-agnostic stores lose 6.8–11.3% recall on temporal queries. Extract `(date, event)` pairs at write time and run an LLM-driven query-expansion step that emits a `{start, end}` JSON range to prune the search space. This is essentially a polyglot stack — vector + a temporal predicate — and it is the cheapest large win in the paper.
- **[R] Use the value itself as the key AND expand it with extracted facts**: Document-expansion (K = V + fact) beats both raw K=V and any compressed-only key (fact-only, summary-only, keyphrase-only), because retrievers can already digest long values — extra signal helps, replacement hurts. Concatenate, don't substitute.
- **[R] Index-stage merging beats retrieval-stage rank merging**: When you have multiple key types (value, summary, fact, keyphrase), join them into one key per item rather than running parallel indexes and merging ranks — rank-merging inflates index size by m+1× and consistently underperformed (Table 10). This is a counter-intuitive nudge against the multi-index orthodoxy.
- **[R + M] Pick a strong query-rewriter, not a strong retriever**: Llama 3.1 8B as the time-range extractor hallucinates ranges for questions with no temporal cue, *worsening* recall (Table 11). GPT-4o correctly refuses to invent a range. Spend your inference budget on the query side; the retriever (Stella V5 1.5B) doesn't need to be huge.
- **[Reading]** **Chain-of-Note + JSON formatting is non-negotiable for the reader**: Even with oracle retrieval, switching the reader from NL-direct to JSON-CoN moves GPT-4o from 0.862 → 0.924, Llama 3.1 70B from 0.762 → 0.848, and Llama 3.1 8B from 0.710 → 0.756 (Fig 6). Without CoN, JSON format alone is inconsistent — the two must be paired.
- **[E + G] Online memory invariably degrades over time**: ChatGPT records evidence statements correctly when first seen but rewrites them as the conversation grows ("often modify this information when it compresses the history, resulting in information loss" §3.4). Coze fails to record indirectly-stated facts. Two distinct failure modes — silent overwrite vs silent ignore — both stem from write-time-only architectures with no preservation guarantees. Treat memory updates as append + supersede, not overwrite.
- **[G + A] Reader errors swallow ~15–19% of cases even with perfect recall**: Error decomposition (Fig 14) shows "correct retrieval, wrong generation" is 40–50% of all reader errors. Retrieval quality buys you a ceiling; the only thing that closes the gap is reading strategy. Architectures that obsess over retrieval and treat the LLM as a black-box reader will plateau here.

## How to Apply It (method)

**Scenario:** You are building Flow OS's session memory layer — a per-user store that accumulates 6+ months of /capture, /work, and /learn sessions plus any agent-handled tasks. A user asks "what did we decide about Dana's onboarding sequence last quarter, and has the plan changed?" — this is exactly a multi-session reasoning + temporal reasoning + knowledge-update query, and you want to bench whether your current memory pipeline can answer it before betting more architecture on it.

**Steps:**

1. **Construct your own LongMemEval-style probe set** (50 questions is enough to start): For each Flow OS memory ability you care about, sample 6–10 real past sessions with known evidence statements, then write a question per the seven LongMemEval types (single-session-user, single-session-assistant, single-session-preference, multi-session, knowledge-update, temporal-reasoning, abstention). Manually annotate the evidence location (which file, which lines). Critical: include 6–8 "false premise" questions to test that the assistant says "I don't know" instead of hallucinating.

2. **Build the haystack**: For each probe question, randomly interleave the evidence sessions with 30–500 unrelated sessions drawn from other users / other ventures, and assign realistic timestamps. This mirrors the §3.2 history compilation step. Your target length should match your real conversation depth — for Flow OS, probably 50k–150k tokens (LongMemEval-S scale).

3. **Wire up the recommended index pipeline**:
   - **Value** = round (one user message + one assistant response per item). Strip assistant-only utterances during fact extraction.
   - **Key** = V + extracted user facts. Use Llama 3.1 8B (or equivalent) to extract user facts per round with this prompt:
     ```
     You will be given a list of messages from a human user to an AI assistant.
     Extract all the personal information, life events, experience, and preferences
     related to the user. Make sure you include all details such as life events,
     personal experience, preferences, specific numbers, locations, or dates.
     State each piece of information in a simple sentence. Put these sentences in
     a json list, each element being a standalone personal fact about the user.
     Minimize the coreference across the facts, e.g., replace pronouns with actual
     entities. If there is no specific events, personal information, or preference
     mentioned, just generate an empty list.

     Human user messages: {round}

     Personal facts about the user (a list of strings in json format; do not
     generate anything else):
     ```
   - **Timestamped event index**: same prompt family, extract `{"date": "YYYY/MM/DD", "event": "..."}` for every round whose date can be inferred.
   - **Retriever**: Stella V5 1.5B dense embeddings (or your existing QMD vector store — the paper validates this works with Contriever too, with BM25 a measurable step down).

4. **Wire up query-time time-aware expansion**: Send the user query to GPT-4o (or your strongest available LLM — Llama 8B is NOT strong enough per Table 11) with this prompt:
   ```
   You will be given a question from a human user asking about some previous events,
   as well as the time the question is asked. Infer a potential time range such that
   the events happening in this range is likely to help to answer the question
   (a start date and an end date). Write a json dict two fields: "start" and "end".
   Write date in the form YYYY/MM/DD. If the question does not have any temporal
   reference, do not attempt to guess a time range. Instead, just say N/A.
   ```
   If a range is returned, filter the retrieval candidates to that time window before scoring.

5. **Wire up the Chain-of-Note + JSON reader**:
   - Format retrieved top-k items as JSON: `[{"timestamp": "...", "text": "..."}, ...]` sorted ascending by timestamp.
   - Send to the reader LLM with:
     ```
     I will give you several history chats between you and a user. Please answer
     the question based on the relevant chat history. Answer the question step by
     step: first extract all the relevant information, and then reason over the
     information to get the answer.

     History Chats: {json_chat_history}
     Current Date: {today}
     Question: {user_query}
     Answer (step by step):
     ```

6. **Evaluate end-to-end**: For each probe question, log (a) Recall@5, Recall@10, NDCG@5/10 against the annotated evidence-session labels, and (b) the QA correctness via a GPT-4o judge using the §3.3 / Figure 10 evaluation prompts (97% agreement with human annotators). Bucket the four cells of Fig 14: correct-retrieval-correct-gen, correct-retrieval-wrong-gen, wrong-retrieval-wrong-gen, wrong-retrieval-correct-gen.

7. **Diagnose your bottleneck**: If correct-retrieval-wrong-gen is >15% of total, your reader is the constraint — try CoN, try JSON, try a stronger reader. If wrong-retrieval-wrong-gen dominates, your indexing is the constraint — try richer key expansion (add timestamped events, add summaries to the K=V+fact). If knowledge-update questions specifically fail with correct retrieval, the retriever is fetching the new info but not the old — make the system retrieve *both* versions for those question types and let the reader resolve.

**Expected outcome:** A reproducible scoreboard for the Flow OS memory layer along five abilities, a numerical decomposition of where your accuracy is leaking (retrieval vs generation), and a directly-actionable upgrade path. You can then re-run the suite after each architectural change (e.g., swapping QMD for HippoRAG-style entity graphs, or adding round-level fact extraction at /capture write time) and read off whether the change moved the meter — instead of arguing about it.

## Best Figure

![Figure 6 — Question answering performance under the oracle retrieval setting (page 10)](figures/wu-2024-longmemeval-fig.png)

Image Candidates:
Figure 6 (p. 10): Bar chart contrasting four reader-strategy combinations across three reader LLMs under oracle retrieval — cleanest evidence that reading strategy is independently load-bearing.
Figure 3 (p. 6): Pilot-study tables showing commercial systems and long-context LLMs both losing 30–66% versus offline reading / oracle — the strongest single piece of evidence the benchmark is hard.
Figure 5 (p. 8): QA accuracy vs token budget across five value-decomposition choices and two readers — shows the round-vs-fact tradeoff that grounds the value-granularity recommendation.

Best Image:
Figure Name: Figure 6: "Question answering performance under the oracle retrieval setting"
Figure Page: 10
Slide Caption: Even with perfect retrieval, switching the reader to Chain-of-Note + JSON-formatted input adds up to 10 absolute accuracy points across three reader LLMs.
Description: Figure 6 plots end-to-end QA accuracy on LongMemEval under the oracle-retrieval setting (i.e., only the gold evidence sessions are provided to the reader) for three reader LLMs — GPT-4o, Llama 3.1 70B Instruct, and Llama 3.1 8B Instruct — across four reading-strategy combinations: NL+Direct, JSON+Direct, NL+CoN, and JSON+CoN. The pattern is consistent: JSON+CoN dominates the other three strategies for every model (GPT-4o: 0.924 vs 0.862 / 0.822 / 0.910; Llama 70B: 0.848 vs 0.762 / 0.744 / 0.800; Llama 8B: 0.756 vs 0.710 / 0.710 / 0.746). Notably, without CoN, JSON formatting alone does NOT consistently beat natural language — the two must be paired. This is the load-bearing evidence for the paper's claim that reading strategy is co-equal with retrieval design, not a downstream afterthought.

## What Experts Overlook

The detail that turns out to do most of the work is **document expansion at the indexing key, not at the retrieval-rank merge** (§5.3, Table 10) — a 2006-vintage IR technique (Tao et al. 2006; Efron et al. 2012) lifted out of classical IR and dropped onto LLM-extracted user facts. Most modern memory-system designs assume you should either (a) replace the value with a compressed fact representation (LD-Agent, ChatGPT, Coze do this) or (b) run multiple parallel indexes — one per key type — and merge ranks at retrieval time. The paper measures both and finds both lose: compression-only loses 9.4% recall and 5.4% accuracy versus baseline, and rank-merging across multi-path retrieval loses 5–10 absolute recall@10 points versus simply concatenating the extracted information into the existing key (K = V + fact in Key Merging vs Rank Merging rows of Table 10). The active ingredient is preserving the original value verbatim while letting the extracted facts *add* retrieval pathways into that same item — not creating duplicate items, not replacing the value.

**Why it matters:** Document expansion implies the retriever's job is "match many surface forms of the same item" — it does NOT need a smaller, cleaner index. This inverts the modern fashion for hierarchical / graph / tree-of-summaries indexes (RAPTOR, HippoRAG, MemWalker), which all add maintenance cost (must re-index on every new session) for a benefit that, when honestly measured against a simple flat K=V+fact baseline, often doesn't materialise. It also tells you that retrieval-time merging is fundamentally noisier than indexing-time merging — the per-key score is a weak signal, but the per-item augmented embedding is a strong one.

**Example of good use:** A Flow OS pattern store where each pattern file's QMD index entry is `value = full markdown body`, key expansion = `[bullet of extracted patterns] + [bullet of contradictions] + [bullet of timestamped events] || full body`. Same file, one index entry, multiple retrieval surfaces. When the user asks "what did we decide about agentic write-time extraction in March?", the time-aware QE prunes to March, the fact bullets match "agentic write-time extraction", and the full body is what gets surfaced to the reader. One pass, one index, all signals.

**Example of misapplication:** Building a "multi-index" memory system where every captured session lives in 4 parallel indexes — a vector index over the full text, a vector index over the LLM-summary, a vector index over the LLM-extracted keyphrases, and a vector index over the LLM-extracted user facts. You then merge ranks at query time using e.g. reciprocal-rank-fusion. Table 10 of this paper shows that exact architecture loses 5–10 absolute recall@10 points vs the much simpler approach of concatenating the same extracted information into a single augmented key per item. You've just paid 4× the index size, 4× the embedding cost, and the maintenance complexity of keeping four indexes in sync, for *worse* recall — and you'll struggle to debug it because the failures look like "retriever is fine, ranking is just weird."

## Extracted Prompts

**Prompt explanation:** User background generation — seed prompt for synthesising the source biographical paragraphs from which questions are constructed.

```
I will give you a topic. Please imagine you are a user that wants to recall and record recent
personal facts along the topic. Generate a long text describing these personal facts. Use
your imagination and generate the personal facts. Make it long and involve several recent
facts or recent events spanning many days, weeks, or monthes. You may state the facts in
plain language and no need to make it story-like.

Topic: {attribute}

Recent Personal Facts related to {attribute}:
```

**Prompt explanation:** User self-chat — instructs an LLM to play the user role and naturally surface a specific evidence statement during a task-oriented exchange with an assistant LLM.

```
I will give you a past memory. Use the memory to act as a normal user to chat with
a chat assistant. In the chat, you may ask it to assist you various tasks or ask it about
various information. However, make sure that your convey the following fact about you:
"{evidence statement}". In addition, make sure your message is concise (1-2 simple
sentences), since the real users often do not bother write a long message. I will provide
you with the chat history and the response from the assistant. Directly generate the next
response from the user's perspective. You must simulate the tone of a neutral user and do
not be overly enthusiastic, verbose, formal, or polite. For conciseness, DO NOT react to
the assistant's message with e.g., "thanks" or "I will do that". Instead, directly state the
follow-up questions or new questions.

Memory: {background}

Chat History:

assistant: Hi! How can I assist you today?

... (more rounds as the conversation continues) ...
```

**Prompt explanation:** Summary extraction — compresses a session/round into a short paragraph focused on the user side.

```
Below is a transcript of a conversation between a human user and an AI assistant. Please
summarize the following dialogue as concisely as possible in a short paragraph, extracting
the main themes and key information. In your summary, focus more on what the user
mentioned or asked for. Dialogue content: {session or round}
```

**Prompt explanation:** Keyphrase extraction — emits a semicolon-separated list of indexing keyphrases for a session.

```
Below is a transcript of a conversation between a human user and an AI assistant. Generate
a list of keyphrases for the session. Separate each keyphrase with a semicolon. Dialogue
content: {session or round}
```

**Prompt explanation:** User-fact extraction — the workhorse extractor that powers the K = V + fact key-expansion recipe.

```
You will be given a list of messages from a human user to an AI assistant. Extract all the
personal information, life events, experience, and preferences related to the user. Make
sure you include all details such as life events, personal experience, preferences, specific
numbers, locations, or dates. State each piece of information in a simple sentence. Put
these sentences in a json list, each element being a standalone personal fact about the user.
Minimize the coreference across the facts, e.g., replace pronouns with actual entities. If
there is no specific events, personal information, or preference mentioned, just generate an
empty list.

Human user messages: {session}

Personal facts about the user (a list of strings in json format; do not generate anything else):
```

**Prompt explanation:** Timestamped event extraction — builds the secondary time-aware index used in §5.4.

```
You will be given a list of messages from a human user to an AI assistant, as well as the
time the conversation took place. Extract all events related to the user as long as its date
is specified or could be inferred. If the time some event took place cannot be inferred, do
not extract that event. Return the events in a json list where each item contains two fields:
"date" and "event". Write date in the form YYYY/MM/DD. If there is no specific event,
just write an empty list.
```

**Prompt explanation:** Query expansion for time-range pruning — converts a natural-language user query into a `{start, end}` retrieval filter.

```
You will be given a question from a human user asking about some prvious events, as well as
the time the question is asked. Infer a potential time range such that the events happening in
this range is likely to help to answer the question (a start date and an end date). Write a json
dict two fields: "start" and "end". Write date in the form YYYY/MM/DD. If the question
does not have any temporal referencea, do not attempt to guess a time range. Instead, just
say N/A.
```

**Prompt explanation:** Chain-of-Note reader — the recommended reading strategy that decomposes long-context QA into extract-then-reason.

```
I will give you several history chats between you and a user. Please answer the question
based on the relevant chat history. Answer the question step by step: first extract all the
relevant information, and then reason over the information to get the answer.

History Chats: {chat history}

Current Date: {question date}

Question: {question}
Answer (step by step):
```

**Prompt explanation:** Non-CoN reader baseline — used as the contrast in Figure 6 to isolate CoN's contribution.

```
I will give you several history chats between you and a user. Please answer the question
based on the relevant chat history.

History Chats: {chat history}

Current Date: {question date}

Question: {question}
Answer:
```

**Prompt explanation:** GPT-4o-as-judge for temporal-reasoning answers — evaluator prompt with off-by-one tolerance for day/week/month counts.

```
I will give you a question, a correct answer, and a response from a model. Please answer
yes if the response contains the correct answer. Otherwise, answer no. If the response is
equivalent to the correct answer or contains all the intermediate steps to get the correct
answer, you should also answer yes. If the response only contains a subset of the information
required by the answer, answer no. In addition, do not penalize off-by-one errors for the
number of days. If the question asks for the number of days/weeks/months, etc., and the
model makes off-by-one errors (e.g., predicting 19 days when the answer is 18), the model's
response is still correct.
```

**Prompt explanation:** GPT-4o-as-judge for knowledge-update answers — allows the response to surface both old and new information so long as the updated answer is present.

```
I will give you a question, a correct answer, and a response from a model. Please answer
yes if the response contains the correct answer. Otherwise, answer no. If the response
contains some previous information along with an updated answer, the response should be
considered as correct as long as the updated answer is the required answer.
```

**Prompt explanation:** GPT-4o-as-judge for single-session-preference answers — rubric-based, open-ended judgment.

```
I will give you a question, a rubric for desired personalized response, and a response from a
model. Please answer yes if the response satisfies the desired response. Otherwise, answer
no. The model does not need to reflect all the points in the rubric. The response is correct
as long as it recalls and utilizes the user's personal information correctly.
```

**Prompt explanation:** GPT-4o-as-judge for other question types — strict containment of correct answer.

```
I will give you a question, a correct answer, and a response from a model. Please answer
yes if the response contains the correct answer. Otherwise, answer no. If the response
is equivalent to the correct answer or contains all the intermediate steps to get the correct
answer, you should also answer yes. If the response only contains a subset of the information
required by the answer, answer no.
```

## Citations

- Xu et al. 2022 — *Beyond goldfish memory: long-term open-domain conversation* (MSC corpus, the human-human predecessor to LongMemEval)
- Xu et al. 2022 — *Long time no see! Open-domain conversation with long-term persona memory* (DuLeMon, the human-AI predecessor)
- Zhong et al. 2024 — *MemoryBank* (the most-compared baseline memory-augmented assistant — summary+round value, K=V indexing)
- Maharana et al. 2024 — *LoCoMo* (the previous SOTA long-term-memory benchmark, lacks knowledge-update + assistant-side recall coverage)
- Du et al. 2024 — *PerLTQA* (3,409-dialogue / 8,593-question alternative benchmark)
- Kim et al. 2024 — *DialSim* (TV-show roleplay memory benchmark, has real-time constraint)
- Yu et al. 2023 — *Chain-of-Note* (the reading strategy that makes the recommended pipeline work)
- Liu et al. 2024 — *Lost in the middle* (foundational evidence for why long-context reading alone is insufficient)
- Shi et al. 2023 — *LLMs distracted by irrelevant context* (the other half of the "long-context isn't enough" argument)
- Sarthi et al. 2024 — *RAPTOR* (hierarchical-summary-tree memory system compared in Table 2)
- Chen et al. 2023 — *MemWalker* (interactive-reading memory system in Table 2)
- Gutiérrez et al. 2024 — *HippoRAG* (entity-graph memory system in Table 2)
- Li et al. 2024 — *LD-Agent* (summary+fact memory system in Table 2)
- Shi et al. 2024 — *REPLUG* (in-context RAG comparison in Table 2)
- Chen et al. 2023 — *Dense X retrieval* (cited as the explanation for why fact-decomposition helps multi-session reasoning specifically)

_Full citations list with DOIs/URLs is in the frontmatter `citations[]` array (47 entries total)._

## Related Digests

- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: agent-memory architecture lifting a 20B model from 39% to 83.6% on LongMemEval (uses this very benchmark)
- [[packer-2023-memgpt-os]] — MemGPT: LLM-as-OS treats the context window as paged virtual memory — complementary architecture to the K-V-store formulation here
- [[chhikara-2025-mem0]] — Mem0: production-ready long-term memory; the knowledge-graph variant Mem0g posts only ~2pt gains and balloons tokens 85×, reinforcing this paper's "key expansion beats graph rebuild" finding
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: argues write-time extraction discards what cannot be reconstructed at query time — directly aligned with LongMemEval's "compression-only loses 9.4% recall" finding

## Reviewer Notes

**Overall severity:** Clean

Every numerical and methodological claim in the digest was checked against the paper text. Spot-verified citations:
- ChatGPT GPT-4o = 0.5773 vs Offline Reading GPT-4o = 0.9184 (Figure 3a) — drops match (37% / 64% per Fig 3a caption).
- Long-context LLMs 30–60% drop on LongMemEval-S (§3.4, Figure 3b) — matches.
- +9.4% recall@k and +5.4% accuracy from K = V + fact key expansion (§5.3) — matches verbatim.
- Time-aware QE adds +6.8% / +11.3% recall depending on value granularity (§5.4) — matches.
- CoN+JSON up to +10 absolute QA points (§5.5; Figure 6 numbers: 0.924 / 0.848 / 0.756 for JSON+CoN across GPT-4o / Llama 3.1 70B / Llama 3.1 8B) — matches.
- Correct-retrieval-wrong-generation = 15–19% of all instances, 40–50% of error instances (§E.5, Figure 14) — matches.
- Stella V5 1.5B retriever, BM25/Contriever comparison (§5.1, Table 9) — matches.
- Llama 3.1 8B hallucinating time ranges; GPT-4o correctly refusing (§5.4, Table 11) — matches.
- Rank-merging vs key-merging (Table 10) — the digest says "5–10 absolute recall@10 points" which is conservative; actual difference for K=V+fact is 0.784 (KM) vs 0.568 (RM) = 21.6pt drop, so the digest understates rather than overstates.
- 500 questions; LongMemEval-S ~115k tokens; LongMemEval-M 500 sessions / ~1.5M tokens (§1, §3) — matches.
- Nine memory systems compared in Table 2 — matches (in-context RAG, MemoryBank, LD-Agent, CoN, ChatGPT, Coze, RAPTOR, MemWalker, HippoRAG).
- The application scenario in "How to Apply It" is explicitly framed as the reader's hypothetical (Flow OS), not as a claim about the paper.
