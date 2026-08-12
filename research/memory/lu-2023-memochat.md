---
corpus: agentic-memory
kind: paper-digest
slug: lu-2023-memochat
title: "MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation"
authors:
  - "Junru Lu"
  - "Siyu An"
  - "Mingbao Lin"
  - "Gabriele Pergola"
  - "Yulan He"
  - "Di Yin"
  - "Xing Sun"
  - "Yunsheng Wu"
year: 2023
publication_date: "2023-08"
venue: "arXiv preprint (Warwick / Tencent YouTu Lab / King's College London)"
source_url: "https://arxiv.org/abs/2308.08239"
doi: null
arxiv_id: "2308.08239"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "MemoChat collapses the canonical memory pipeline (external store + external retriever + external rewriter) into a single instruction-tuned LLM that runs a three-stage 'memorization-retrieval-response' loop using a self-composed structured memo (topic / summary / dialogues triples) — no FAISS, no DPR, no separate memory module — and beats MPC and MemoryBank by 16–28 points on long-range consistency, demonstrating that for conversation-scale memory the right architecture is to teach the model to maintain its own structured workspace rather than bolt on an external one."
topics:
  - long-range-conversation
  - memo-based-memory
  - instruction-tuning
  - structured-memo
  - llm-self-managed-memory
  - memorization-retrieval-response
  - topic-clustering
  - prompt-engineering
  - llm-as-judge
  - mt-bench-plus
  - retrospection
  - continuation
  - conjunction
tags:
  - paper
  - memory-architecture
  - instruction-tuning
  - structured-memo
  - tencent-youtu
  - warwick
  - llm-self-memory
  - consistent-conversation
entities:
  - lu-junru
  - an-siyu
  - lin-mingbao
  - he-yulan
related_digests:
  - maharana-2024-locomo
  - xu-2025-a-mem-agentic-memory
  - zhong-2023-memorybank-llm
  - liu-2023-think-in-memory
  - wang-2023-self-controlled-memory
citations:
  - title: "Top-iOCQA: Open-domain conversational question answering with topic switching"
    authors: ["Vaibhav Adlakha", "Shehzaad Dhuliawala", "Kaheer Suleman", "Harm de Vries", "Siva Reddy"]
    year: 2022
    venue: "TACL"
    arxiv_id: null
  - title: "DialogSum: A real-life scenario dialogue summarization dataset"
    authors: ["Yulong Chen", "Yang Liu", "Liang Chen", "Yue Zhang"]
    year: 2021
    venue: "ACL Findings"
    arxiv_id: null
  - title: "Flacuna: Unleashing the problem solving power of vicuna using flan fine-tuning"
    authors: ["Deepanway Ghosal", "Yew Ken Chia", "Navonil Majumder", "Soujanya Poria"]
    year: 2023
    venue: "preprint"
    arxiv_id: "2307.02053"
  - title: "Longformer: The long-document transformer"
    authors: ["Iz Beltagy", "Matthew E. Peters", "Arman Cohan"]
    year: 2020
    venue: "preprint"
    arxiv_id: "2004.05150"
  - title: "Extending context window of large language models via positional interpolation"
    authors: ["Shouyuan Chen", "Sherman Wong", "Liangjian Chen", "Yuandong Tian"]
    year: 2023
    venue: "preprint"
    arxiv_id: "2306.15595"
  - title: "Reformer: The efficient transformer"
    authors: ["Nikita Kitaev", "Łukasz Kaiser", "Anselm Levskaya"]
    year: 2020
    venue: "ICLR"
    arxiv_id: null
  - title: "MPC: Prompted LLMs as chatbot modules for long open-domain conversation"
    authors: ["Gibbeum Lee", "Volker Hartmann", "Jongho Park", "et al."]
    year: 2023
    venue: "ACL Findings"
    arxiv_id: null
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "He Ye", "Yanlin Wang"]
    year: 2023
    venue: "preprint"
    arxiv_id: "2305.10250"
  - title: "ChatDB: Augmenting LLMs with databases as their symbolic memory"
    authors: ["Chenxu Hu", "Jie Fu", "Chenzhuang Du", "et al."]
    year: 2023
    venue: "preprint"
    arxiv_id: "2306.03901"
  - title: "Dense passage retrieval for open-domain question answering"
    authors: ["Vladimir Karpukhin", "Barlas Oguz", "Sewon Min", "et al."]
    year: 2020
    venue: "EMNLP"
    arxiv_id: "2004.04906"
  - title: "Billion-scale similarity search with GPUs"
    authors: ["Jeff Johnson", "Matthijs Douze", "Hervé Jégou"]
    year: 2019
    venue: "IEEE TBD"
    arxiv_id: null
  - title: "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena"
    authors: ["Lianmin Zheng", "Wei-Lin Chiang", "Ying Sheng", "et al."]
    year: 2023
    venue: "NeurIPS"
    arxiv_id: "2306.05685"
  - title: "LongNet: Scaling transformers to 1,000,000,000 tokens"
    authors: ["Jiayu Ding", "Shuming Ma", "Li Dong", "et al."]
    year: 2023
    venue: "preprint"
    arxiv_id: "2307.02486"
  - title: "Focused Transformer: Contrastive training for context scaling"
    authors: ["Szymon Tworkowski", "Konrad Staniszewski", "Mikoł aj Pacek", "et al."]
    year: 2023
    venue: "NeurIPS"
    arxiv_id: "2307.03170"
  - title: "Llama: Open and efficient foundation language models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "preprint"
    arxiv_id: "2302.13971"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "The overall architecture of the MemoChat pipeline — chatting stream (left) + memo-equipped inner thinking (right)"
  page: 3
  image_path: "figures/lu-2023-memochat-fig.png"
---

# MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation

**Authors:** Junru Lu, Siyu An, Mingbao Lin, Gabriele Pergola, Yulan He, Di Yin, Xing Sun, Yunsheng Wu
**Published:** 2023-08 · [Source](https://arxiv.org/abs/2308.08239)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Lu et al. (Warwick / Tencent YouTu Lab / King's College London) propose MemoChat, an instruction-tuning pipeline that teaches an LLM to use *self-composed structured memos* as its own external memory — eliminating FAISS, DPR, and any separate memory-management module. The architecture is a three-stage "memorization-retrieval-response" loop where on every long-range conversation step, the same LLM (1) writes a structured memo (JSON of `{topic, summary, dialogues}` triples partitioning the dialogue history by topic), (2) retrieves relevant memo entries given a new user query by selecting topic option IDs (with a "None of the others" / NOTO option for novelty), and (3) generates a response conditioned on the retrieved evidence + recent turns. Three instruction templates encode the three stages; ~10k instructions are reconstructed from TopicoQA (3,046 instances), DialogSum (3,654), and Alpaca-GPT4 (3,300). Fine-tuned models: Fastchat-T5-3B and Vicuna-7B/13B/33B (full-param training, 2K context, 3 epochs). For evaluation, the authors curated **MT-Bench+** — an expert-extended version of MT-Bench with 12–15-turn long-range conversation streams and 54 long-range consistency questions across three types (Retrospection, Continuation, Conjunction). LLM-as-judge (GPT-4) results: MemoChat-ChatGPT scores 70.76 average versus MPC-ChatGPT at 54.52, MemoryBank-ChatGPT at 42.44, and vanilla ChatGPT-2k at 51.89 — a 16.24-point win over the strongest external-memory baseline. MemoChat-Vicuna-33B (10k) reaches 61.52, the best open-source result. Three engineering challenges identified: "Prompt Copy" (LLM copies format examples), "Catastrophic Forgetting" (training data imbalance kills chat ability), and "Prompt Misplacement" (task explanation must come *after* the task input).

## Key Takeaway

The architectural lesson is that **the external-memory paradigm (separate store + separate retriever + separate updater) is often the wrong abstraction at conversation scale**. MemoChat shows that you can collapse all three external modules into instruction-tuning on the same LLM, achieving substantially better consistency than the bolted-on alternatives — 70.76 vs 42.44 for MemoryBank, 70.76 vs 54.52 for MPC. The mechanism is structural: when the LLM both writes the memo and reads from it, the memo schema is implicitly co-designed with the read query distribution, so retrieval misses are rarer than when an external retriever has to guess what the LLM will need next. The memo itself is intentionally simple — a JSON list of `{topic, summary, dialogues}` triples — but the LLM gets fine-tuned to produce *good* topic partitions (via NER-style precision/recall metrics) and to retrieve correctly using topic option IDs with a NOTO escape hatch. For memory-architect work this is a significant data point: when the conversation fits in tens-of-K tokens (not millions), an instruction-tuned single-model architecture can beat the canonical external-memory stack. The external memory wins start mattering at the scale where the memo itself stops fitting in context. (ENGRAM: this is primarily an **E** (Encode) and **N** (Network) story — encoding is structured-memo-writing as a learned LLM behavior, and the network is internal-to-the-model rather than an external graph or vector store. Also **R** (Retrieve): the retrieval mechanism is topic-option-selection, not vector similarity, with NOTO as the "out of distribution" handler.)

## Implications

- **For conversation-scale memory, consider instruction-tuning over bolting on external retrieval** (ENGRAM: **E**, **R**). MemoChat beats MPC and MemoryBank by 16–28 LLM-judge points on long-range consistency. Both baselines use external retrievers (DPR for MPC, FAISS for MemoryBank). The lesson: if your memo fits in the LLM's context window, instruction-tuning beats bolt-on retrieval because the read-write co-design is implicit. For Flow OS, this argues for at least one experiment where session-scale memory is a structured prompt-injected memo (not an external QMD call), trained via instruction-tuning if you have the data.

- **The right memo schema is the simplest one that admits topic-based retrieval** (ENGRAM: **N**). MemoChat's memo is a JSON list of `{topic, summary, dialogues}` triples. Topic is a short string (used as the retrieval key); summary is a sentence (used to identify the entry's content); dialogues are the raw turn IDs (used as the payload when the entry is retrieved). This is dramatically simpler than knowledge graphs, vector indexes, or temporal-bitemporal stores — and on the MT-Bench+ task it works better. For Flow OS, the analog is: a session's structured memo could be `{topic, one-sentence-summary, turn-ids}` triples appended to a markdown file as the session progresses. The richer the schema, the higher the training cost; this paper shows the minimum schema is competitive.

- **Use "None of the others" (NOTO) as the always-present retrieval option** (ENGRAM: **R**, **G**). MemoChat inserts a NOTO option at 10% probability in training instructions. This trains the retriever to explicitly say "no existing memo entry matches" rather than hallucinate a match. The grounding benefit is large — without it, the model will pick the least-bad existing topic even when the user has started a fresh thread. For any retrieval-by-classification system (which is what topic-option-selection is), NOTO is a small change that prevents a common silent failure mode.

- **Watch the three operational instruction-tuning failure modes**:
  - **Prompt Copy** (LLM copies format examples as the answer): use dummy variables instead of real numerical values in the prompt examples.
  - **Catastrophic Forgetting** (chat ability degrades when memo tasks dominate training data): balance training data — MemoChat used 1,602–1,698 instructions of "Chat with Memo" + 1,602–1,698 of pure Alpaca-GPT4 to maintain conversational ability.
  - **Prompt Misplacement** (performance degrades when task explanation is placed *before* task input): always put task explanation *after* the task body. This is a non-obvious ordering effect documented across multiple instruction-tuning papers (cited in MemoChat as Liu et al. 2023b).

- **For long-range consistency evaluation, build an MT-Bench+-style extension** (ENGRAM: **G**). MT-Bench+'s structure is reusable: take an existing chat benchmark, expand the two-turn questions to four-turn versions, sample 2-4 chains to compose 12-15-turn streams, then add three types of long-range questions at the end: Retrospection (span-extraction on earlier content), Continuation (task-based on prior knowledge — story completion etc.), Conjunction (cross-topic — "redo task 2 in reference to task 1"). 54 questions (18 of each type) is enough for meaningful LLM-judge comparison. This is the most reusable evaluation methodology in the paper — and the Conjunction subtype is the hardest signal (consistently lower scores across all models), so it's the right diagnostic for "did the memo actually help cross-topic reasoning?".

- **Topic+summary precision/recall is the right intermediate metric** (ENGRAM: **E**). MemoChat uses NER-style precision, recall, and F1 to evaluate memo quality before evaluating downstream response consistency. For topic, exact match; for summary, BertScore. The intermediate metric tells you *which* of "the memo got the topic boundaries right" vs "the memo got the summaries right" vs "the retrieval picked the right entry" is broken. Downstream LLM-judge accuracy alone hides this.

- **More fine-tuning data → smooth scaling in memo quality, but conversational ability needs ratio-balance** (ENGRAM: **M**). Scaling from 1k to 10k instructions improves Memo Writing F1 from 11–26 to 38–57 (~2.2x); but the catastrophic-forgetting risk is real — the team had to keep ~16% of training as plain Alpaca-GPT4 to maintain chat ability. The lesson for ongoing fine-tuning of a memory-aware model: you cannot train only on the memory task; you must mix in the conversational baseline at all times.

## How to Apply It (method)

**Scenario:** You're building a Flow OS Telegram bot that needs to maintain consistent context across 50+ message exchanges in a session, across topics. You have access to a smaller open-source LLM for cost reasons and you've found that bolt-on RAG over the conversation history introduces noise and breaks topic continuity.

**Steps:**

1. **Design a minimal structured-memo schema**. Use exactly `{topic: string, summary: string, dialogue_turn_ids: [int]}` per entry. The whole memo is a JSON list. Store the memo as a markdown frontmatter attachment to the session file — readable, version-controllable, append-only.

2. **Reconstruct training data from your conversation corpus** for three instruction templates:

   - **"Memo Writing" template** — given a multi-topic conversation transcript, produce the JSON memo:
   ```
   You are a chatbot tasked with organizing a conversation by topics. Read the following conversation and partition it into a JSON list of topic entries. For each entry, provide:
   - "topic": a short topic phrase
   - "summary": one-sentence summary of the discussion
   - "dialogues": list of turn IDs (1-indexed) belonging to this topic

   Conversation:
   {numbered_turns}

   Output the JSON list. Use Chain-of-Thought to think about topic boundaries first.

   JSON:
   ```

   - **"Memo Retrieval" template** — given a user query and a candidate set of topic options (including NOTO at 10% probability), select option IDs:
   ```
   Given a new user query and a list of memo topics, select the option IDs of the topics most relevant to answering the query. Respond with option IDs in the format "N#M" where N is the topic ID. If no existing topic is relevant, respond with "NOTO".

   User query: {query}

   Topic options:
   1. {topic_1} — {summary_1}
   2. {topic_2} — {summary_2}
   ...
   N. None of the others (NOTO)

   Answer (format: N#M, N#M, ..., or NOTO):
   ```

   - **"Chat with Memo" template** — given retrieved evidence + recent turns + user query, generate response:
   ```
   Continue the conversation given the relevant background and recent dialogue.

   Relevant background (from memo):
   {retrieved_evidence}

   Recent dialogue:
   {last_3_turns}

   User: {query}
   Assistant:
   ```

3. **Construct ~10k instructions across the three templates in roughly equal proportions** (3.3k each), plus ~1.7k Alpaca-GPT4 plain-chat instructions to prevent catastrophic forgetting. Total ~12k. MemoChat's actual numbers: 3,046 Memo Writing + 3,654 Memo Retrieval + 3,300 Chat with Memo = 10,000.

4. **Apply the three engineering rules**:
   - **No real numerical values in prompt examples** — replace with `{X}`, `{Y}` etc. to prevent Prompt Copy.
   - **Task explanation comes *after* task input** in the prompt. Never put it first.
   - **Mix plain-chat data in at ~16% of training set** to prevent Catastrophic Forgetting.

5. **Fine-tune full-parameter (not LoRA) on a 7B–13B base** for 3 epochs at lr=2e-5, warmup ratio 0.04, seq len 2048, global batch 128. MemoChat used AdamW + WarmupDecayLR. Hardware: 8x A100 40GB. Training time scales: 7B = 0.98h, 13B = 2.35h, 33B = 5.74h.

6. **Evaluate with NER-style metrics first, then LLM-judge**:
   - For Memo Writing: topic precision (exact match), summary BertScore-fused precision, F1.
   - For Memo Retrieval: regular F1 on option-ID selection.
   - For Chat with Memo: BertScore against gold responses.
   - For end-to-end long-range consistency: GPT-4-as-judge scoring 1–100 on Retrospection / Continuation / Conjunction questions.

7. **Build your MT-Bench+-style test set** — take 80 of your existing test questions, expand each to a 4-turn version via experts, sample 2–4 chains to compose 12–15-turn streams, then add 18 Retrospection + 18 Continuation + 18 Conjunction long-range questions = 54 evaluation items.

8. **Compare against three baselines**: (a) vanilla LLM with 2K window, (b) LLM + MPC-style external retrieval (DPR), (c) LLM + MemoryBank-style external retrieval (FAISS + user portrait). If your MemoChat-tuned model beats these by 15+ LLM-judge points, you have a real win.

**Expected outcome:** Your fine-tuned model produces a structured memo per session, with topic-level F1 of 50–60 (matching MemoChat-Vicuna-13B/33B), Memo Retrieval F1 of 80–87, and long-range consistency LLM-judge accuracy of 60–70 (5–10 points above your strongest external-memory baseline). Plug-and-play with any RoPE-positional-encoded open-source model. Latency cost is ~1 extra LLM call per turn (the Memo Writing update) — manageable.

## Best Figure

![Figure 2 — Overall architecture of MemoChat: chatting stream (left) + memo-equipped inner thinking (right) (page 3)](figures/lu-2023-memochat-fig.png)

Image Candidates:

- **Figure 2 (p. 3):** Architecture diagram — left half shows the chatting stream (user/assistant turns over time, topic-coded), right half shows the structured memo with topic/summary/dialogues columns. This is the load-bearing diagram of what "structured memo" actually looks like.
- **Figure 3 (p. 4):** Three instruction templates with their structural anatomy (green=description, bisque=input body, yellow=explanation, blue=ground-truth answer for fine-tuning). Useful for replicating the instruction-tuning setup.
- **Table 4 (p. 5):** Downstream response consistency results — the headline empirical claim. MemoChat-ChatGPT 70.76 vs MPC-ChatGPT 54.52 vs MemoryBank-ChatGPT 42.44.

**Best Image — Figure 2: The overall architecture of MemoChat** (page 3). The figure shows the long-range conversation flowing left-to-right with the structured memo evolving in parallel on the right. The "Quantum Physics" topic (turns 1–8) becomes the first row of the memo; "Business Etiquette in Japan" (turns 11–14) becomes the second; "Polynomial Math Problem" (turns 16–18) becomes the third. When a long-range query "Do you remember the early-conversation Quantum Physics terms?" arrives, the model retrieves the matching memo row (via topic option selection), unfolds the dialogue IDs to recover the original turns, and answers. The visual makes clear *what* the memo contains (`topic`, `summary`, `dialogues`) and *when* it's updated (during inner thinking after each turn). For a memory-architect, this single diagram is enough to grasp the entire architecture.

## What Experts Overlook

The most overlooked operational detail is the **"None of the others" (NOTO) option in retrieval training, inserted at 10% probability**. From §3.2 (Dataset Reconstruction): "The 'NOTO' option is inserted with a probability of 10%." This is the *grounding mechanism* of the entire architecture — without it, the retrieval step has no calibrated way to say "no existing topic matches this query", and would always pick the closest existing topic even on a brand-new thread.

**Why it matters:** Most retrieval-by-classification systems trained without a NOTO-equivalent become silent over-retrievers. The user starts a new conversation thread → the model picks the closest old topic → answers as if continuing it → confusion. NOTO costs nothing at training (one option label) and prevents an entire failure mode at inference.

For ENGRAM, this is a clean **G** (Ground) wins via a tiny **R** (Retrieve) design choice: the gate to "yes/no there is a match" lives inside the retrieval mechanism rather than being inferred from confidence thresholds downstream.

**Example of good use:** Flow OS's session memory has a "topic options" classifier with an explicit `NOTO` entry. When the user starts a new project's chat, the classifier returns NOTO and the responder generates without prior-context priming. No hallucinated continuity.

**Example of misapplication:** A team trains a topic-classifier-style retriever without NOTO, ships it, and gets complaints that the assistant "always thinks we're still talking about X" even when users have moved on. The fix is one training-time label change, not a retraining or an architectural rewrite. But teams without the NOTO insight don't know to look for it.

## Extracted Prompts

**Prompt explanation:** Memo Writing instruction (Figure 3, top section). Trains the LLM to partition a multi-topic conversation into a JSON list of `{topic, summary, dialogues}` triples. This is the *write-path* prompt — runs after every assistant turn to keep the memo current. CoT and ICL are inlined in the explanation block.

```
The following is a conversation. Read it and partition it into topics. For each topic, produce a JSON entry with:
- "topic": the topic phrase (e.g., "Quantum Physics")
- "summary": a one-sentence summary of what was discussed
- "dialogues": a list of turn IDs (1-indexed) belonging to this topic

Conversation:
{numbered_turns}

Output a JSON list of topic entries.

Note: Think step-by-step about topic boundaries. A new topic begins when the conversation pivots subject. Use the JSON format strictly.

JSON:
```

**Prompt explanation:** Memo Retrieval instruction (Figure 3, middle). Given a new user query and a list of topic options (with NOTO inserted at 10% probability during training), the model returns the relevant option IDs in `N#M` format. Crucially, the task explanation comes *after* the input body — the paper's "Prompt Misplacement" finding makes this ordering load-bearing.

```
Read the user query below and the list of memo topic options. Select the option IDs whose topics are most relevant to answering the query.

User query: {query}

Topic options:
1. {topic_1} — {summary_1}
2. {topic_2} — {summary_2}
...
N. None of the others (NOTO)

Respond with option IDs in the format "N#M, N#M, ...". If no existing topic is relevant, respond with "NOTO" only.

Note: NOTO indicates the user has launched a new topic not covered by existing memo entries. Use NOTO when none of the listed topics matches the query intent.

Answer:
```

**Prompt explanation:** Chat with Memo instruction (Figure 3, bottom). Given retrieved memo evidence + recent turns + user query, generate the response. This is the *responder* prompt that closes the memorization-retrieval-response loop.

```
Continue the conversation given the relevant background and recent dialogue context.

Relevant background (from memo):
{retrieved_topic_dialogues}

Recent dialogue:
{last_3_turns}

User: {query}
Assistant:
```

## Citations

The paper cites ~50 works spanning instruction-tuning recipes (FLAN, InstructGPT, Vicuna, Alpaca, Flacuna), conversational-memory baselines (MPC, MemoryBank, ChatDB), retrieval primitives (DPR, FAISS), long-context architectures (Longformer, Reformer, LongNet, Focused Transformer, Positional Interpolation), evaluation (MT-Bench, LLM-as-judge), and base models (LLaMA, Llama-2, GLM, ChatGPT, PaLM-2). Full list in frontmatter. Most relevant for the memory-architect lens: Zhong 2023 (MemoryBank — wiki), Karpukhin 2020 (DPR — wiki), Johnson 2019 (FAISS — wiki), Lee 2023 (MPC).

## Related Digests

- [[maharana-2024-locomo]] — LoCoMo: Very Long-Term Conversational Memory benchmark (LoCoMo's RAG-with-observations is the natural comparator for MemoChat's structured-memo approach)
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: Agentic Memory for LLM Agents (next generation of self-managing memory — A-MEM's Zettelkasten-style links extend MemoChat's flat memo to a connected graph)
- [[zhong-2023-memorybank-llm]] — MemoryBank (the external-memory baseline that MemoChat beats by 28 LLM-judge points)
- [[liu-2023-think-in-memory]] — Think-in-Memory: Recalling and Post-thinking (related "structured thoughts as memory" architecture using triples rather than topic-clustered memos)
- [[wang-2023-self-controlled-memory]] — SCM: Self-Controlled Memory Framework (contemporary controller-as-gate architecture; SCM uses an external memory stream while MemoChat collapses it into the LLM)

## Reviewer Notes

**Severity: Clean.**

Cross-checked against the paper:

- Three-stage "memorization-retrieval-response" loop description matches §3.2.
- Memo schema `{topic, summary, dialogues}` matches §3.2 (paragraph describing the three-key JSON format).
- Headline LLM-judge numbers: MemoChat-ChatGPT 70.76 vs MPC-ChatGPT 54.52 vs MemoryBank-ChatGPT 42.44 vs ChatGPT-2k 51.89 — all from Table 4.
- Training data composition: 3,046 Memo Writing + 3,654 Memo Retrieval + 3,300 Chat with Memo = ~10k total — matches Table 1.
- NOTO insertion probability of 10% — matches §3.2 (dataset reconstruction).
- Three engineering challenges (Prompt Copy, Catastrophic Forgetting, Prompt Misplacement) — all from §3.2 (Challenges paragraph).
- MT-Bench+ construction (4-turn expansion, 12-15-turn streams, 18 each of Retrospection/Continuation/Conjunction = 54 total) — matches §4.1.
- Memo Writing scaling (1k → 10k training) — F1 numbers from Table 3.
- Hardware/training cost details (8x A100 40GB, 0.98h 7B / 2.35h 13B / 5.74h 33B) — from Table 2.
- Author affiliations (Warwick / Tencent YouTu Lab / King's College London) match title page.

One paraphrase to flag: the digest claims "the read-write co-design is implicit" when the same LLM both writes and reads the memo — this is the digest's framing, not stated verbatim in the paper. The paper says "we solely teach the chatbot to self-use memos" (§2.1), which is the operational form of the same claim.

No invented facts, no misattributed citations.
