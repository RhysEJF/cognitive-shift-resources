---
corpus: agentic-memory
kind: paper-digest
slug: zhong-2023-memorybank-llm
title: "MemoryBank: Enhancing Large Language Models with Long-Term Memory"
authors:
  - "Zhong, Wanjun"
  - "Guo, Lianghong"
  - "Gao, Qiqi"
  - "Ye, He"
  - "Wang, Yanlin"
year: 2023
publication_date: "2023-05"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2305.10250"
doi: null
arxiv_id: "2305.10250"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "MemoryBank is a canonical early reference architecture for LLM long-term memory — a three-pillar design (hierarchical storage, dense FAISS retrieval, Ebbinghaus-inspired decay-on-recall updater) wrapped in an LLM-on-the-write-path summarisation loop that distils raw dialogue into daily/global event summaries and an evolving user portrait."
topics:
  - long-term-memory
  - llm-agents
  - memory-architecture
  - forgetting-curve
  - ai-companion
  - user-modeling
  - dense-retrieval
tags:
  - paper
  - memory-system
  - canonical
  - ebbinghaus
  - hierarchical-summary
  - llm-on-write-path
  - silicon-friend
entities:
  - zhong-wanjun
  - wang-yanlin
  - ebbinghaus-hermann
related_digests:
  - chhikara-2025-mem0
  - hu-2026-evermemos
  - tavakoli-2026-beam-light
  - latimer-2025-hindsight-memory
  - wu-2024-longmemeval
citations:
  - title: "Language models are few-shot learners"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "Advances in Neural Information Processing Systems (NeurIPS) 33"
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "PaLM: Scaling language modeling with pathways"
    authors: ["Aakanksha Chowdhery", "Sharan Narang", "Jacob Devlin", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2204.02311"
  - title: "Scaling instruction-finetuned language models"
    authors: ["Hyung Won Chung", "Le Hou", "Shayne Longpre", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2210.11416"
  - title: "Memory: A contribution to experimental psychology"
    authors: ["Hermann Ebbinghaus"]
    year: 1964
    venue: "book (English translation)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neural turing machines"
    authors: ["Alex Graves", "Greg Wayne", "Ivo Danihelka"]
    year: 2014
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1410.5401"
  - title: "LoRA: Low-rank adaptation of large language models"
    authors: ["Edward Hu", "Yelong Shen", "Phillip Wallis", "et al."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2106.09685"
  - title: "Billion-scale similarity search with GPUs"
    authors: ["Jeff Johnson", "Matthijs Douze", "Hervé Jégou"]
    year: 2019
    venue: "IEEE Transactions on Big Data 7(3):535-547"
    doi: null
    url: null
    arxiv_id: null
  - title: "Dense passage retrieval for open-domain question answering"
    authors: ["Vladimir Karpukhin", "Barlas Oğuz", "Sewon Min", "et al."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: "https://github.com/facebookresearch/DPR"
    arxiv_id: "2004.04906"
  - title: "LangChain"
    authors: ["LangChain Inc."]
    year: 2022
    venue: "software documentation"
    doi: null
    url: "https://docs.langchain.com/docs/"
    arxiv_id: null
  - title: "Dialogue intent classification with long short-term memory networks"
    authors: ["Lian Meng", "Minlie Huang"]
    year: 2018
    venue: "NLPCC 2017 proceedings, Springer pp. 42-50"
    doi: null
    url: null
    arxiv_id: null
  - title: "text2vec: A tool for text to vector"
    authors: ["Xu Ming"]
    year: 2022
    venue: "software"
    doi: null
    url: "https://github.com/shibing624/text2vec"
    arxiv_id: null
  - title: "ChatGPT"
    authors: ["OpenAI"]
    year: 2022
    venue: "product release"
    doi: null
    url: "https://chat.openai.com/chat"
    arxiv_id: null
  - title: "GPT-4 technical report"
    authors: ["OpenAI"]
    year: 2023
    venue: "technical report"
    doi: null
    url: null
    arxiv_id: "2303.08774"
  - title: "Stanford Alpaca: An instruction-following LLaMA model"
    authors: ["Rohan Taori", "Ishaan Gulrajani", "Tianyi Zhang", "et al."]
    year: 2023
    venue: "github project"
    doi: null
    url: "https://github.com/tatsu-lab/stanford_alpaca"
    arxiv_id: null
  - title: "LLaMA: Open and efficient foundation language models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2302.13971"
  - title: "MiniLM: Deep self-attention distillation for task-agnostic compression of pre-trained transformers"
    authors: ["Wenhui Wang", "Furu Wei", "Li Dong", "et al."]
    year: 2020
    venue: "Advances in Neural Information Processing Systems (NeurIPS) 33:5776-5788"
    doi: null
    url: null
    arxiv_id: "2002.10957"
  - title: "Beyond goldfish memory: Long-term open-domain conversation"
    authors: ["Jing Xu", "Arthur Szlam", "Jason Weston"]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2107.07567"
  - title: "Long time no see! Open-domain conversation with long-term persona memory"
    authors: ["Xinchao Xu", "Zhibin Gou", "Wenquan Wu", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2203.05797"
  - title: "BELLE: Be Everyone's Large Language Model Engine"
    authors: ["Yunjie Ji", "Yan Gong", "Yiping Peng", "et al."]
    year: 2023
    venue: "github project"
    doi: null
    url: "https://github.com/LianjiaTech/BELLE"
    arxiv_id: null
  - title: "GLM-130B: An open bilingual pre-trained model"
    authors: ["Aohan Zeng", "Xiao Liu", "Zhengxiao Du", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2210.02414"
  - title: "OPT: Open pre-trained transformer language models"
    authors: ["Susan Zhang", "Stephen Roller", "Naman Goyal", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2205.01068"
  - title: "A survey of large language models"
    authors: ["Wayne Xin Zhao", "Kun Zhou", "Junyi Li", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2303.18223"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Overview of MemoryBank"
  page: 3
  image_path: "figures/zhong-2023-memorybank-llm-fig.png"
---

# MemoryBank: Enhancing Large Language Models with Long-Term Memory

**Authors:** Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, Yanlin Wang
**Published:** 2023-05 · [Source](https://arxiv.org/abs/2305.10250)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MemoryBank is a three-pillar long-term-memory layer for LLM-based assistants — a hierarchical memory store, a dual-tower dense retriever, and an Ebbinghaus-Forgetting-Curve-inspired updater — proposed by Zhong et al. (Sun Yat-Sen, HIT, KTH) and shipped as the open-source chatbot SiliconFriend. Storage holds three things: timestamped raw dialogue turns, LLM-generated daily-then-global event summaries, and an LLM-generated evolving user portrait (personality + emotion traits). Retrieval uses LangChain + FAISS with MiniLM (English) or text2vec (Chinese) as the encoder for both stored memory pieces and the current conversational query, returning top-k pieces plus the global user portrait and global event summary into a "memory-augmented prompt". The decay updater models retention as R = e^(-t/S), initialises S=1 on first mention, and on every recall increments S by 1 and resets t to 0 — so frequently recalled items become near-immortal while ignored ones decay. To evaluate, the authors hand-wrote 194 probing questions (97 EN + 97 ZH) against a synthetic 10-day, 15-virtual-user corpus generated by ChatGPT playing personas; SiliconFriend-ChatGPT scored retrieval accuracy 0.763 EN / 0.711 ZH, response correctness 0.716 / 0.655, contextual coherence 0.912 / 0.675, and a ranking score of 0.818 / 0.758 against SiliconFriend-ChatGLM and SiliconFriend-BELLE (both 6-7B open-source models tuned with LoRA r=16 on 38k psychological dialogues). The actionable takeaway: even in 2023 the design pattern of LLM-as-summariser-on-write + dense retrieval + biologically-motivated decay was already viable, and it sets the template later refined by MemGPT, Mem0, and the modern agent-memory stack — but the eval is small, mostly self-generated, and never measures whether the decay mechanism actually improves outcomes versus a no-forget baseline.

## Key Takeaway

The counter-intuitive lesson of MemoryBank isn't that you need a forgetting curve — it's that the LLM itself should sit on the *write* path, not just the read path. Most "agent memory" intuitions treat the LLM as the consumer of retrieved chunks; MemoryBank flips it: every day the LLM is asked to distil that day's turns into an event summary, then the LLM is asked again to roll those daily summaries into a global summary, and again to maintain a rolling user-portrait. Retrieval then has three layers of pre-chewed material to draw from, and the conversational prompt gets the global portrait and global summary *for free* alongside the retrieved fine-grained turns. The Ebbinghaus decay is the publicity stunt; the real architectural choice is paying for LLM compute at memory-write time so query-time retrieval has something other than raw dialogue chunks to grab.

## Implications

- **Pay your LLM tax at write-time, not query-time** [ENGRAM: E + A]: MemoryBank's design commits LLM compute to distil raw dialogue into event summaries and a user portrait as the conversation grows, which means retrieval can return *summaries plus turns* instead of just turns. For Flow OS / Contact-With-Reality this validates the pattern of running `/learn` (LLM-on-write) rather than relying purely on lazy summarisation at recall time.
- **Hierarchical summary as a shape-of-memory choice** [ENGRAM: N + A]: The "raw turns → daily event summary → global event summary" stack is a deliberate Aggregate-dimension decision — three retrieval units with different granularity, each useful for different query types. Worth replicating: don't force one chunk size; let the AI maintainer build multiple altitudes of the same content.
- **Decay-on-recall is computationally trivial** [ENGRAM: M]: S=1 on first write; on every recall S += 1 and t := 0. That's a 2-line maintenance pass over the index — no heavyweight scheduler needed. If you want lifecycle management without graph DBs, this is a credible starting point.
- **But: the paper never proves the decay mechanism helps** [ENGRAM: M — critical gap]: Table 2 reports results from SiliconFriend variants; there is no ablation that toggles the forgetting mechanism on/off and measures retrieval/correctness deltas. The "Ebbinghaus" framing is rhetorical, not empirically tested in the paper.
- **The user portrait is an under-discussed Encode-dimension decision** [ENGRAM: E + G]: Asking the LLM to summarise *personality* (not just events) from dialogue is the move that makes the chatbot feel "human-like" — and is also the most provenance-risky step in the system, because once "Linda is introverted" is written into the global portrait it gets injected into *every* future prompt with no source link back to the conversation that produced it. The paper does not address how to surface contradictions when a later session shows Linda being extroverted. This is a Ground-dimension hole worth closing in any production replica.
- **Single-encoder, language-specific retrieval is a maintenance debt** [ENGRAM: R + M]: The English/Chinese variants use *different* embedding models (MiniLM vs text2vec). That bifurcates the index and means cross-language queries won't work without an adapter. Multilingual encoders solve this in 2025+; the paper's choice is a 2023-era artefact and a warning against premature language sharding.
- **Self-generated eval is a structural risk** [ENGRAM: G — for evaluation, not the system]: ChatGPT generated the 15 personas, the 10-day dialogue corpus *and* (implicitly via the authors) the probing questions. ChatGPT-backed SiliconFriend then sat the test. Of course it scores 0.912 on contextual coherence — same model, same style. Treat the 0.76/0.91/0.82 numbers as upper-bound smoke-test, not external validation.
- **LangChain + FAISS + MiniLM is still a reasonable starter stack** [ENGRAM: R]: For Flow OS-style personal-context memory at <100k items, this combo (the SiliconFriend implementation) remains a sane minimum. QMD's BM25+vec hybrid is a step up but the lesson — "use an interchangeable encoder, don't marry the model" — holds.

## How to Apply It (method)

**Scenario:** You're prototyping a memory layer for a long-running personal-assistant agent that holds multi-session conversations with a single user over months. You want to test whether an LLM-on-the-write-path summarisation loop plus a simple decay-on-recall scheduler gives you measurably better retrieval than raw chunk-and-embed RAG. You don't yet have a graph DB and don't want one; you want a stack you can stand up in a day on a laptop.

**Steps:**

1. **Stand up the dual-tower retriever**: Use LangChain's vector-store interface backed by FAISS for the index, and a small interchangeable sentence encoder for both memory pieces and the live query — MiniLM is the paper's English choice; for any modern replica swap in `text-embedding-3-small` or a multilingual model like `bge-m3`. The retrieval contract is: given the current user utterance `c`, encode to `h_c`, return top-k pieces from `M` ranked by cosine similarity.

2. **Define three retrieval units, not one**: Every memory write produces three rows in the store:
   - The raw dialogue turn (timestamped, both speaker and AI text).
   - A pointer to the daily event summary that turn belongs to (filled in nightly).
   - A pointer to the current user-portrait revision.

3. **Run two LLM summarisation passes nightly (or on session-close)**. Pass A: per-day event summary. Pass B: roll daily summaries into a rolling global summary. Pass C: refresh the user portrait from the day's dialogue. Use the actual paper prompts:

   ```
   Summarize the events and key information in the content [dialog/events]
   ```

   ```
   Based on the following dialogue, please summarize the user's personality traits and emotions.[dialog]
   ```

   ```
   The following are the user's exhibited personality traits and emotions throughout multiple days. Please provide a highly concise and general summary of the user's personality[daily Personalities]
   ```

4. **Add the Ebbinghaus decay scheduler on the index**: Every row carries `(S, t_last_seen)`. On retrieval of row `r`, before returning the result set: `S[r] += 1; t_last_seen[r] := now`. At query time, drop or down-weight any row where `R = exp(-(now - t_last_seen) / S) < threshold`. The paper uses S=1 initial; threshold is a knob you tune. For zero-loss audit, *don't physically delete* — flag rows as "decayed-out" but keep them in cold storage so you can surface the contradiction later if the agent's "forgotten" claim contradicts what's actually on disk.

5. **Construct the memory-augmented prompt at query time**: Inject three blocks into the system prompt — `{relevant_memory}` (top-k pieces), `{global_user_portrait}` (the latest portrait revision, always-on), `{global_event_summary}` (the rolling summary, always-on). Then the user turn. This is the SiliconFriend pattern; it's what makes the agent "remember the user" without retrieval needing to surface the portrait every turn.

6. **Build a probing-question harness, not a conversation-rating harness**: Generate or hand-write 50-200 questions of the form "What did you tell me about X on day N?" and score model responses on three axes copied from the paper: (i) retrieval accuracy {0,1}, (ii) response correctness {0, 0.5, 1}, (iii) contextual coherence {0, 0.5, 1}. This is far cheaper to evaluate than full transcript review and surfaces the memory-system behaviour cleanly.

7. **Critical addition the paper skips — run a no-forget ablation**: Run the same probing set with the decay mechanism disabled (R := 1 always). If your retrieval/correctness/coherence numbers are *identical* with and without decay, you've learned the Ebbinghaus mechanism is decorative for your workload. If they diverge, you've quantified the real cost/benefit of forgetting — which the paper never does.

**Expected outcome:** A working minimum-viable long-term-memory layer in <1 week, with quantified probing-question scores that let you make decisions about the encoder (swap MiniLM for a multilingual one if cross-language matters), the summary cadence (nightly vs per-session vs every-N-turns), and the decay threshold (tight vs loose). You'll also know whether decay actually helps your workload — answer the question the original paper left open.

## Best Figure

![Figure 1 — Overview of MemoryBank (page 3)](figures/zhong-2023-memorybank-llm-fig.png)

Image Candidates:
Figure 1 (p. 3): The architecture diagram showing all three pillars (storage, retrieval, updating) plus the SiliconFriend prompt-construction flow — single best whole-story view.
Figure 2 (p. 6): Side-by-side conversation comparing SiliconFriend's empathic response to baseline ChatGLM — illustrates the psychological-tuning value but is the wrong story for the architecture lens.
Table 2 (p. 9): Quantitative results table with retrieval/correctness/coherence/ranking for all three SiliconFriend variants across EN+ZH — the strongest numeric evidence in the paper but visually dense.

Best Image:
Figure Name: Figure 1: "Overview of MemoryBank"
Figure Page: 3
Slide Caption: The MemoryBank architecture: a three-pillar memory layer (storage of conversations + event summaries + user portrait, dense FAISS retrieval, and an Ebbinghaus-decay updater) that feeds a memory-augmented prompt into the SiliconFriend chatbot.
Description: Figure 1 lays out the full system on one page. The left panel ("MemoryBank") shows the three pillars: a Memory Storage box stacking past conversations (timestamped daily blocks), an Event Summary block ("Book and gifts recommendation / Experience of visiting parks / Improving drawing skills"), and a User Portrait block ("open-minded, curious, and receptive to advice"). Below the storage is the Memory Updating subsystem, with a tiny sketch of the Ebbinghaus forgetting curve next to "Memory Strength Updating". The right panel ("SiliconFriend") shows the inference-time prompt: a Meta Prompt section assembling Event Summary + User Portrait + Relevant Memory, then a History pane, then a Query input. Two arrows connect the panels — "Memory Augmented Prompt" going right (storage → prompt) and "Memory Retrieval" going left (query → storage). This single figure encodes every architectural decision in the paper: the three storage units, the dual flow of writing-and-reading, the always-on global context, and the decay-driven maintenance loop.

## What Experts Overlook

The detail most readers (and most "summaries-of-MemoryBank" downstream papers) skip is that **the global event summary and the global user portrait are injected into every conversational turn unconditionally — they are not retrieved**. Section 3 ("Integration with MemoryBank") and Figure 1's "Meta Prompt" panel make this visible: alongside the *retrieved* `relevant memory`, the prompt template always carries `global user portrait` and `global event summary` as fixed context. Retrieval is only used to pull the fine-grained turns; the high-altitude summaries ride along on every turn for free. This is what gives SiliconFriend its "the bot remembers me" feel without paying a retrieval round-trip for the user-modelling layer.

**Why it matters:** This is a deliberate decoupling of two different memory roles — "Who is this user, generally?" (always-on context, small and cheap) and "What specifically did we discuss?" (retrieval-gated, large and selective). It exploits the asymmetry that global summaries compress hundreds of turns into a few hundred tokens, so they're cheap to keep in the prompt at all times, while raw turns are expensive and need filtering. Skip this design choice and you end up paying retrieval cost for the user portrait *and* missing it half the time when the query doesn't lexically match — which destroys the perceived continuity that makes the chatbot feel companionable.

**Example of good use:** A Flow OS-style assistant maintains a rolling "who is the user, generally" summary that is regenerated weekly (small LLM cost) and injected on every session start. Specific past decisions ("what we agreed about the Howler frame geometry on April 14") stay in the retrieved layer. The assistant feels personalised every turn, costs almost nothing in retrieval for the personalisation, and only pays retrieval cost when specific context is actually needed.

**Example of misapplication:** A naive replica puts the user portrait into the FAISS index as just another row and relies on retrieval to surface it. Whenever the user's query is topical ("help me write this email"), the portrait is *not* retrieved (no lexical overlap), and the bot generates a generic email with no personalisation. The user concludes the memory system is broken — when in fact the engineer skipped the always-on injection that the paper explicitly designed in.

## Extracted Prompts

**Prompt explanation:** Daily / global event-summarisation prompt — runs on the write path to distil raw dialogue (or daily summaries) into an event summary used as a retrieval unit and as always-on context.

```
Summarize the events and key information in the content [dialog/events]
```

**Prompt explanation:** Per-day personality-extraction prompt — runs on the write path to produce a daily personality snapshot from that day's dialogue.

```
Based on the following dialogue, please summarize the user's personality traits and emotions.[dialog]
```

**Prompt explanation:** Global personality-aggregation prompt — rolls daily personality snapshots into a single user portrait that is injected into every prompt.

```
The following are the user's exhibited personality traits and emotions throughout multiple days. Please provide a highly concise and general summary of the user's personality[daily Personalities]
```

## Citations

- Brown et al. 2020 — *Language models are few-shot learners* (GPT-3 paper, NeurIPS 33)
- Chowdhery et al. 2022 — *PaLM: Scaling language modeling with pathways* (arXiv:2204.02311)
- Chung et al. 2022 — *Scaling instruction-finetuned language models* (FLAN-T5, arXiv:2210.11416)
- Ebbinghaus 1964 — *Memory: A contribution to experimental psychology* (English translation)
- Graves, Wayne & Danihelka 2014 — *Neural turing machines* (arXiv:1410.5401)
- Hu et al. 2021 — *LoRA: Low-rank adaptation of large language models* (arXiv:2106.09685)
- Johnson, Douze & Jégou 2019 — *Billion-scale similarity search with GPUs* (FAISS, IEEE TBD 7(3))
- Karpukhin et al. 2020 — *Dense passage retrieval for open-domain question answering* (DPR, arXiv:2004.04906)
- LangChain Inc. 2022 — *LangChain* (software)
- Meng & Huang 2018 — *Dialogue intent classification with LSTM networks* (NLPCC 2017)

(22 total references; full list in frontmatter `citations:` for auto-walk.)

## Related Digests

- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory
- [[hu-2026-evermemos]] — EverMemOS: a memory operating system for always-on agents
- [[tavakoli-2026-beam-light]] — Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects
- [[wu-2024-longmemeval]] — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory

## Reviewer Notes

**Overall severity:** Clean

Every claim in this digest was cross-checked against the paper text. Confirmed against the source:

- Three-pillar architecture (storage / retrieval / updating) — §2 opening and Figure 1.
- Hierarchical summary structure (turns → daily event summary → global event summary) — §2.1 "Hierarchical Event Summary".
- Dual-tower dense retrieval with FAISS — §2.2.
- Ebbinghaus formula `R = e^(-t/S)` with S=1 initial, S+=1 on recall, t reset to 0 — §2.3.
- LangChain + MiniLM (EN) + text2vec (ZH) — §3 "Integration with MemoryBank".
- 38k psychological dialogues, LoRA r=16, 3 epochs, A100 — §3 "Parameter-efficient Tuning".
- 194 probing questions (97 EN + 97 ZH), 15 virtual users, 10 days — §4.2.
- Quantitative results (0.763 / 0.711 / 0.716 / etc.) — Table 2.
- Always-on injection of global user portrait and global event summary into the prompt — §3 final paragraph + Figure 1 Meta Prompt panel.
- Critical observation that the paper has no decay-on/off ablation — verified by full read of §4: only model-variant comparisons appear, no forgetting-mechanism ablation.

No claims required adjustment. The digest's stronger framings (e.g., "the Ebbinghaus framing is rhetorical, not empirically tested") are the digest's own analytical commentary, clearly attributable as such, not misrepresented as paper findings.
