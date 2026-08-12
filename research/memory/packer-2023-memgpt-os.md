---
corpus: agentic-memory
kind: paper-digest
slug: packer-2023-memgpt-os
title: "MemGPT: Towards LLMs as Operating Systems"
authors:
  - "Charles Packer"
  - "Sarah Wooders"
  - "Kevin Lin"
  - "Vivian Fang"
  - "Shishir G. Patil"
  - "Ion Stoica"
  - "Joseph E. Gonzalez"
year: 2023
publication_date: "2023-10"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2310.08560"
doi: null
arxiv_id: "2310.08560"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Treat the LLM context window as a paged virtual-memory tier and let the model itself page data in and out via function calls — the OS metaphor turns a fixed-context model into a self-managing memory system that beats both lossy summarization and naive RAG on long-conversation consistency (92.5% vs 32.1% on Deep Memory Retrieval with GPT-4) and unbounded document QA."
topics:
  - agent-memory
  - long-context
  - virtual-memory
  - hierarchical-memory
  - self-editing-memory
  - llm-os
  - function-calling
  - rag
  - conversational-agents
  - document-qa
tags:
  - paper
  - memory-architecture
  - memgpt
  - operating-system-metaphor
  - paging
  - benchmark
  - berkeley
entities:
  - packer-charles
  - wooders-sarah
  - gonzalez-joseph
  - stoica-ion
related_digests: []
citations:
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "Advances in neural information processing systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."]
    year: 2018
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "Language models are few-shot learners"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "Advances in Neural Information Processing Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training language models to follow instructions with human feedback"
    authors: ["Long Ouyang", "Jeffrey Wu", "Xu Jiang", "et al."]
    year: 2022
    venue: "Advances in Neural Information Processing Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Llama 2: Open foundation and fine-tuned chat models"
    authors: ["Hugo Touvron", "Louis Martin", "Kevin Stone", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2307.09288"
  - title: "Transformer-XL: Attentive language models beyond a fixed-length context"
    authors: ["Zihang Dai", "Zhilin Yang", "Yiming Yang", "et al."]
    year: 2019
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1901.02860"
  - title: "Reformer: The efficient transformer"
    authors: ["Nikita Kitaev", "Lukasz Kaiser", "Anselm Levskaya"]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2001.04451"
  - title: "Longformer: The long-document transformer"
    authors: ["Iz Beltagy", "Matthew E Peters", "Arman Cohan"]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2004.05150"
  - title: "A survey on long text modeling with transformers"
    authors: ["Zican Dong", "Tianyi Tang", "Lunyi Li", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2302.14502"
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Nelson F Liu", "Kevin Lin", "John Hewitt", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2307.03172"
  - title: "Toolformer: Language models can teach themselves to use tools"
    authors: ["Timo Schick", "Jane Dwivedi-Yu", "Roberto Dessi", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2302.04761"
  - title: "AgentBench: Evaluating LLMs as agents"
    authors: ["Xiao Liu", "Hao Yu", "Hanchen Zhang", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2308.03688"
  - title: "A case for redundant arrays of inexpensive disks (RAID)"
    authors: ["David A Patterson", "Garth Gibson", "Randy H Katz"]
    year: 1988
    venue: "Proceedings of the 1988 ACM SIGMOD international conference on Management of data"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generating long sequences with sparse transformers"
    authors: ["Rewon Child", "Scott Gray", "Alec Radford", "et al."]
    year: 2019
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1904.10509"
  - title: "Linformer: Self-attention with linear complexity"
    authors: ["Sinong Wang", "Belinda Z Li", "Madian Khabsa", "et al."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2006.04768"
  - title: "Set transformer: A framework for attention-based permutation-invariant neural networks"
    authors: ["Juho Lee", "Yoonho Lee", "Jungtaek Kim", "et al."]
    year: 2019
    venue: "International conference on machine learning"
    doi: null
    url: null
    arxiv_id: null
  - title: "Extending context window of large language models via positional interpolation"
    authors: ["Shouyuan Chen", "Sherman Wong", "Liangjian Chen", "Yuandong Tian"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2306.15595"
  - title: "Train short, test long: Attention with linear biases enables input length extrapolation"
    authors: ["Ofir Press", "Noah A Smith", "Mike Lewis"]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2108.12409"
  - title: "In-context retrieval-augmented language models"
    authors: ["Ori Ram", "Yoav Levine", "Itay Dalmedigos", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2302.00083"
  - title: "Improving language models by retrieving from trillions of tokens"
    authors: ["Sebastian Borgeaud", "Arthur Mensch", "Jordan Hoffmann", "et al."]
    year: 2022
    venue: "International conference on machine learning"
    doi: null
    url: null
    arxiv_id: null
  - title: "Dense passage retrieval for open-domain question answering"
    authors: ["Vladimir Karpukhin", "Barlas Oguz", "Sewon Min", "et al."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2004.04906"
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2020
    venue: "Advances in Neural Information Processing Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Retrieval augmented language model pre-training"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."]
    year: 2020
    venue: "International conference on machine learning"
    doi: null
    url: null
    arxiv_id: null
  - title: "RA-DIT: Retrieval-augmented dual instruction tuning"
    authors: ["Xi Victoria Lin", "Xilun Chen", "Mingda Chen", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Active retrieval augmented generation"
    authors: ["Zhengbao Jiang", "Frank F Xu", "Luyu Gao", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.06983"
  - title: "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions"
    authors: ["H. Trivedi", "Niranjan Balasubramanian", "Tushar Khot", "Ashish Sabharwal"]
    year: 2022
    venue: "ArXiv"
    doi: null
    url: null
    arxiv_id: "2212.10509"
  - title: "Leveraging passage retrieval with generative models for open domain question answering"
    authors: ["Gautier Izacard", "Edouard Grave"]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2007.01282"
  - title: "Unsupervised dense information retrieval with contrastive learning"
    authors: ["Gautier Izacard", "Mathilde Caron", "Lucas Hosseini", "et al."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2112.09118"
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["Joon Sung Park", "Joseph C O'Brien", "Carrie J Cai", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2304.03442"
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    authors: ["Reiichiro Nakano", "Jacob Hilton", "Suchir Balaji", "et al."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2112.09332"
  - title: "ReAct: Synergizing reasoning and acting in language models"
    authors: ["Shunyu Yao", "Jeffrey Zhao", "Dian Yu", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2210.03629"
  - title: "Chain-of-thought prompting elicits reasoning in large language models"
    authors: ["Jason Wei", "Xuezhi Wang", "Dale Schuurmans", "et al."]
    year: 2022
    venue: "Advances in Neural Information Processing Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Beyond goldfish memory: Long-term open-domain conversation"
    authors: ["Jing Xu", "Arthur Szlam", "Jason Weston"]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2107.07567"
  - title: "Judging LLM-as-a-judge with MT-bench and chatbot arena"
    authors: ["Lianmin Zheng", "Wei-Lin Chiang", "Ying Sheng", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2306.05685"
  - title: "ROUGE: A package for automatic evaluation of summaries"
    authors: ["Chin-Yew Lin"]
    year: 2004
    venue: "Text summarization branches out"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "MemGPT architecture — fixed-context LLM processor augmented with hierarchical memory and OS-style functions"
  page: 3
  image_path: "figures/packer-2023-memgpt-os-fig.png"
---

# MemGPT: Towards LLMs as Operating Systems

**Authors:** Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez
**Published:** 2023-10 (v2 2024-02) · [Source](https://arxiv.org/abs/2310.08560)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MemGPT proposes treating the LLM context window as a paged virtual-memory tier rather than as a static prompt, then giving the LLM function calls so it can page data in and out of its own context like a process talking to an OS. The architecture has two memory tiers: **main context** (system instructions + read-write `working_context` block + FIFO message queue, all inside the LLM's prompt window) and **external context** (`archival_storage`, an unstructured vector-searchable text DB, and `recall_storage`, the full message-event log). A queue manager fires `memory pressure` warnings at 70% of context and a forced recursive-summarization flush at 100%, prompting the model to use functions like `working_context.append`, `working_context.replace`, `archival_storage.insert/search`, and `conversation_search` to decide what to keep. On a new **Deep Memory Retrieval** task built from the MSC dataset, MemGPT+GPT-4 hits **92.5% accuracy / 0.814 ROUGE-L** vs **32.1% / 0.296** for GPT-4 with a recursive summary baseline — and MemGPT+GPT-4-Turbo reaches **93.4%**. On the **nested KV retrieval** task (140 UUID pairs ≈ 8k tokens, multi-hop lookups), GPT-4 and GPT-4-Turbo collapse to 0% accuracy by 3 nesting levels while MemGPT+GPT-4 stays flat across all 4 levels. On document QA, MemGPT's accuracy is roughly flat as documents-retrieved scales from 0→200 while fixed-context baselines plateau at retriever ceiling. GPT-3.5 underperforms with MemGPT due to weaker function calling — the OS metaphor only pays off above a function-call competence threshold.

## Key Takeaway

Make the LLM the memory manager of itself. By giving a fixed-context model two scratch tiers it can read but only one it can directly act in, and OS-style interrupts ("memory pressure warning") when it's about to lose information, you flip memory from a passive store the model queries into an active process the model maintains. The counter-intuitive result: the dumber tier (lossy recursive summary baseline) is the one that *can't* recover — once a fact is summarized away, it's gone. MemGPT's recall storage holds the full conversation log indefinitely, so what looks like "infinite memory" is really just *deferring the compression decision* until query time, when the model knows which facts it actually needs. The OS metaphor is doing real work here: paging, interrupts, and self-managed eviction aren't decoration — they're what stop write-time summarization from destroying information the agent will later need.

## Implications

- **[E + M] Defer the compression decision to query time wherever you can**: MemGPT's biggest win on DMR (60-point accuracy lift over recursive-summary baselines) comes from the architectural choice that *evicted messages still live in recall storage forever* — the recursive summary is for the in-context tier only. If you're designing a memory layer for an agentic OS, do not let the only path be "LLM distills → store distillation → throw raw away." Keep the raw layer cheap (append-only message log) and let synthesis be either (a) lazy at query time, or (b) revisable. The encoding gate is anti-information, and MemGPT proves this years before the "Storage Is Not Memory" framing did.

- **[N + R] Two retrieval tiers, two access modes — don't collapse them**: MemGPT separates `recall_storage` (message-event log, queried by `conversation_search`) from `archival_storage` (arbitrary text DB with vector search via pgvector + HNSW). Conversational provenance lives in one, semantically-indexed knowledge in the other. Mapping to ENGRAM Network: a polyglot stack (log + vector DB) beats a single flat vector store because the agent reasons differently about "what was said" vs "what I know."

- **[R + Encode-controls] Pagination is part of retrieval, not a UI detail**: Search results are paginated and explicitly token-bounded (the system literally tells the model "Showing 10 of 124 results (page 1/13)") so retrieval can't crash the context window. The agent learns to page through results until satisfied — and the paper notes MemGPT *sometimes stops too early*, which is a failure mode worth instrumenting. For your own memory layer, treat retrieval as a controlled iteration, not a one-shot fetch.

- **[A] Recursive summarization at flush time is the only aggregation done — and it underperforms when used as the *only* layer**: When the FIFO queue overflows (100% context), MemGPT flushes ~50% of messages and folds them into a new recursive summary. This is the *only* aggregation step. The baselines that get *only* this summary score 32-39% on DMR; MemGPT scores 67-93%. The lesson for Aggregation design: recursive summarization is fine as a *fallback in-context view* but catastrophic as a primary store. Keep it as a sidecar.

- **[G] Provenance is preserved by structural separation, not by tagging**: Source attribution in MemGPT is "free" because messages live in `recall_storage` with their original timestamps and metadata — the agent's working_context edits are clearly distinguishable from raw message recall. You don't need elaborate provenance schemas if your tiers themselves encode the trust gradient. (Working context = LLM-asserted current belief; recall storage = ground-truth event log.)

- **[Encode] Self-editing memory needs interrupts, not polling**: The `memory pressure` warning is an asynchronous system message injected into the FIFO queue at 70% context — the LLM does not have to ask "am I full yet?" The OS metaphor matters: maintenance happens via *interrupt*, not via the agent volunteering to introspect. If you're building a memory-maintaining agent, fire events at it rather than expecting it to check.

- **[Maintain] Base-model capability is a hard floor**: GPT-3.5 with MemGPT *underperforms* GPT-4 baselines on nested KV retrieval — it can't reliably chain function calls and gives up early. This means: don't promise users an OS-style memory layer if the underlying model can't handle multi-step function chaining. The architecture amplifies model capability; it doesn't substitute for it.

- **[N] Function chaining via `request_heartbeat=true` is the equivalent of yielding vs blocking in OS-land**: A function call with `request_heartbeat=true` immediately returns control to the LLM for another inference cycle; without it, MemGPT pauses until the next external event. This is the lever that turns memory operations from one-shot tool calls into multi-step retrievals. Build this primitive into your own memory APIs — without it, agents can't perform multi-hop lookups (as evidenced by the nested KV results).

## How to Apply It (method)

**Scenario:** You're building Flow OS's session-memory layer. Each Flow session is a long-running agent thread (sometimes days, with multiple human check-ins) that needs to remember decisions, contacts, and prior reasoning *across context-window resets* — but you don't want to ship a custom RAG stack per session, and you've already seen that pure recursive summarization loses information. You want an OS-style memory layer that compounds across sessions while keeping the per-turn cost predictable.

**Steps:**

1. **Define your main-context layout**: Split the prompt window into three contiguous regions. Read-only system instructions (describing the memory tiers and the function schemas). A fixed-size read-write `working_context` block (~1500-2000 tokens). A FIFO message queue for everything else. Index 0 of the FIFO is reserved for a recursive summary of evicted messages.

2. **Set up the two external tiers**: `recall_storage` is an append-only event log of every message/system-event with timestamps — backed by Postgres or SQLite. `archival_storage` is a vector-searchable text DB (the paper uses pgvector + HNSW with OpenAI's `text-embedding-ada-002`). Function calls write to it explicitly; nothing auto-stores.

3. **Expose the function schema to the model in the system prompt**. Minimum surface:

   ```
   working_context.append(text)
   working_context.replace(old_text, new_text)
   archival_storage.insert(text)
   archival_storage.search(query, page=N)
   conversation_search(query, page=N)
   ```

   Each function should support a `request_heartbeat: bool` flag — when true, control returns to the LLM for another inference cycle (multi-step chaining); when false, MemGPT yields until the next external event.

4. **Implement the queue manager with two thresholds**. At 70% of the LLM's context window (the *warning token count*), inject a system message into the FIFO: `"System Alert: Memory Pressure"` — this is the interrupt. At 100% (the *flush token count*), evict ~50% of the oldest queue messages, generate a new recursive summary that folds the previous summary plus the evicted messages, and place that summary at FIFO index 0.

5. **Build pagination into every retrieval function**. Every search returns `"Showing N of M results (page X/Y)"`. The model must explicitly call `page=2` etc. to continue. This bounds context use and forces the agent to reason about when to stop searching. Set a hard cap (e.g. 10 pages) per query if you want to prevent runaway loops.

6. **Use a structured persona block as the seed of `working_context`**. The paper's DMR persona starts with: *"The following is information about myself. My task is to completely immerse myself in this role…"* — this gives the model an instruction-anchored reason to read and edit working_context. Don't leave it empty; seed it with the conversation's identity / goals.

7. **Run the eval loop**. For document QA, embed the corpus (e.g. your full session history across all Flow sessions) into archival storage with HNSW. For multi-session chat, run real sessions and evaluate (a) **Deep Memory Retrieval** — ask the agent specific factual questions about prior sessions; (b) **Nested KV / multi-hop** — chain two or three lookups together; (c) **Conversation opener** — start a new session and measure whether the model spontaneously surfaces relevant prior context. Use an LLM judge (GPT-4) for grading and bin scores into CORRECT / WRONG.

8. **Set the underlying model to GPT-4 or GPT-4-Turbo-class**. The paper shows GPT-3.5 underperforms MemGPT badly on nested KV due to weak function chaining. The architecture amplifies model capability, it doesn't replace it. If you must use a weaker model, expect heavy degradation on multi-hop tasks and consider hardcoding the chain.

**Expected outcome:** A session-memory layer where each Flow session retains structured working context that the agent itself edits, falls back to a recursive summary when context pressure spikes, and can recover *any* prior message or stored artifact via paginated vector search. Cross-session DMR-style accuracy should land in the 80-93% range with GPT-4; the same model without MemGPT (just a recursive summary preprompt) lands at 30-35%. You'll also get a clean separation between "what the model currently believes" (working_context) and "what was actually said" (recall_storage) — a natural provenance gradient for free.

## Best Figure

![Figure 3 — MemGPT architecture: fixed-context LLM processor augmented with hierarchical memory and OS-style functions (page 3)](figures/packer-2023-memgpt-os-fig.png)

**Image Candidates:**
- Figure 3 (p. 3): The single-view system diagram showing the memory hierarchy — main context (system instructions + working context + FIFO queue) inside the finite context window, paired with archival and recall storage outside, connected via Function Executor and Queue Manager.
- Figure 5 (p. 6): Document QA accuracy plotted against documents retrieved (0-200) — flat line for MemGPT vs declining/plateauing baselines is the clearest before/after evidence of the architecture's value.
- Figure 7 (p. 7): Nested KV retrieval accuracy across nesting levels 0-4 — shows GPT-4 and GPT-4-Turbo collapsing to 0% by level 3 while MemGPT+GPT-4 stays flat at ~100%; the strongest demonstration of multi-hop function chaining.

**Best Image:**
- Figure Name: Figure 3: "In MemGPT, a fixed-context LLM processor is augmented with a hierarchical memory system and functions that let it manage its own memory."
- Slide Caption: MemGPT's two-tier memory architecture — main context (in-window) and external context (archival + recall storage), connected by a Function Executor the LLM itself drives.
- Description: Figure 3 shows the complete MemGPT system in one view. Inside the LLM's finite context window (8k tokens in the example), the prompt tokens are split into three regions: System Instructions (read-only static MemGPT system prompt), Working Context (a fixed-size read-write scratchpad written via function calls), and the FIFO Queue (rolling message history with a recursive summary at index 0). Outside the context window sit Archival Storage (read/write via functions, vector-searchable) and Recall Storage (the full message-event log, read via functions, written via the queue manager). The Function Executor interprets the LLM's completion tokens as function calls and moves data between tiers; the Queue Manager handles eviction and FIFO mechanics. The dashed lines between in-context regions vs solid lines to external storage make the OS analogy literal: prompt tokens are "main memory," external storage is "disk," and the LLM is the process that issues page-in/page-out instructions.

## What Experts Overlook

The method works not just because MemGPT gives the LLM tools to manage memory, but because **memory pressure is delivered as an injected system message inside the FIFO queue itself, not as an external API signal the LLM has to poll for**. The warning sits *in-context* at the moment the LLM next runs inference. The paper's Section 2.3 says: *"MemGPT prompts the processor with warnings regarding token limitations to guide its memory management decisions."* This is an OS interrupt embedded as a literal sentence the model reads alongside ordinary conversation. Without it, the model has no way to know it's approaching a context-window cliff — and even if it had a tool to ask, it wouldn't know when to call it. The system tells it. This is the difference between an LLM with memory tools and an LLM that *behaves like a process inside a memory-managed runtime.*

**Why it matters:** Most agentic-memory designs hand the LLM a `save_to_memory(...)` function and assume the agent will know when to use it. MemGPT's evidence (DMR baselines at 32-39% with recursive summary, vs 67-93% with MemGPT) says that's not enough — the agent needs a *forcing function*, an interrupt that fires before the loss happens. The forcing function turns memory management from an *optional* skill (which weak agents skip) into a *reactive* skill (which any function-calling agent can handle, because it's responding to a prompt it sees). For ENGRAM, this is a Maintain/Encode interaction: maintenance triggers shape what gets encoded, and trigger placement (in-prompt system message vs out-of-prompt API event) determines whether maintenance happens at all.

**Example of good use:** In Flow OS's session-memory layer, fire a synthetic `system_alert` message into the agent's prompt whenever a session crosses ~70% of effective context budget, telling it: *"Your active working memory is approaching capacity. Use `working_context.replace` to consolidate outdated facts, or `archival_storage.insert` to offload reference material."* The agent will respond because the alert is now part of the conversation it must reply to. Pair this with a hard flush at 100% so you have a safety net even if the agent ignores the warning.

**Example of misapplication:** Add `save_to_memory(...)` as a passive function in the agent's toolset, document it in the system prompt as "use this whenever you think information is important," and ship. The agent will not call it consistently — there's no in-context signal of urgency, so the model has no triggering event. You'll see drift after long sessions (the agent contradicts earlier turns, forgets user preferences) and assume the model is bad at memory. The architecture is what's bad — it's missing the interrupt.

## Extracted Prompts

**Prompt explanation:** MemGPT persona instruction used for the DMR (Deep Memory Retrieval) task — anchors the agent to a role-playing identity and tells it to use core memory + conversation search.

```
The following is information about myself. My task is to completely immerse myself in this role (I should never say that I am an AI, and should reply as if I am playing this role). If the user asks me a question, I should reply with a best guess using the information in core memory and conversation search.
```

**Prompt explanation:** Baseline (no MemGPT) system prompt for DMR — gives the model only a recursive summary of prior conversations and forces a "NO ANSWER" abstention when uncertain.

```
Your task is to answer a question from the user about your prior conversations.
The following is a summary of all your prior conversations:
CONVERSATION SUMMARY
Answer from the perspective of the persona provided (do not say that you are an AI assistant).
If you do not have enough information to answer the question, reply 'NO ANSWER'. Either reply with the answer, or reply 'NO ANSWER', do not say anything else.
```

**Prompt explanation:** LLM-judge prompt for DMR / Conversation Opener — uses GPT-4 to grade a generated answer against a gold answer with worked CORRECT / WRONG examples.

```
Your task is to label an answer to a question as 'CORRECT' or 'WRONG'.
You will be given the following data:
(1) a question (posed by one user to another user), (2) a 'gold' (ground truth) answer, (3) a generated answer which you will score as CORRECT/WRONG.
The point of the question is to ask about something one user should know about the other user based on their prior conversations.
The gold answer will usually be a concise and short answer that includes the referenced topic, for example:
Question: Do you remember what I got the last time I went to Hawaii?
Gold answer: A shell necklace
The generated answer might be much longer, but you should be generous with your grading - as long as it touches on the same topic as the gold answer, it should be counted as CORRECT.
For example, the following answers would be considered CORRECT:
Generated answer (CORRECT): Oh yeah, that was so fun! I got so much stuff there, including that shell necklace.
Generated answer (CORRECT): I got a ton of stuff... that surfboard, the mug, the necklace, those coasters too..
Generated answer (CORRECT): That cute necklace
The following answers would be considered WRONG:
Generated answer (WRONG): Oh yeah, that was so fun! I got so much stuff there, including that mug.
Generated answer (WRONG): I got a ton of stuff... that surfboard, the mug, those coasters too..
Generated answer (WRONG): I'm sorry, I don't remember what you're talking about.
Now it's time for the real question:
Question: QUESTION
Gold answer: GOLD ANSWER
Generated answer: GENERATED ANSWER
First, provide a short (one sentence) explanation of your reasoning, then finish with CORRECT or WRONG. Do NOT include both CORRECT and WRONG in your response, or it will break the evaluation script.
```

**Prompt explanation:** Self-instruct prompt used to generate the DMR question/answer pairs from the MSC dataset — defines what counts as a valid "memory challenge" question (must require chat-log knowledge, not persona summary).

```
Your task is to write a "memory challenge" question for a simulated dialogue between two users.
You get as input:
- personas for each user (gives you their basic facts)
- a record of an old chat the two users had with each other
Your task is to write a question from user A to user B that test's user B's memory.
The question should be crafted in a way that user B must have actually participated in the prior conversation to answer properly, not just have read the persona summary.
Do NOT under any circumstances create a question that can be answered using the persona information (that's considered cheating).
Instead, write a question that can only be answered by looking at the old chat log (and is not contained in the persona information).

For example, given the following chat log and persona summaries:
old chat between user A and user B
A: Are you into surfing? I'm super into surfing myself
B: Actually I'm looking to learn. Maybe you could give me a basic lesson some time!
A: Yeah for sure! We could go to Pacifica, the waves there are pretty light and easy
A: There's even a cool Taco Bell right by the beach, could grab a bite after
B: What about this Sunday around noon?
A: Yeah let's do it!

user A persona:
I like surfing
I grew up in Santa Cruz

user B persona:
I work in tech
I live in downtown San Francisco

Here's an example of a good question that sounds natural, and an answer that cannot be directly inferred from user A's persona:
User B's question for user A
B: Remember that one time we went surfing? What was that one place we went to for lunch called?
A: Taco Bell!

This is an example of a bad question, where the question comes across as unnatural, and the answer can be inferred directly from user A's persona:
User B's question for user A
B: Do you like surfing?
A: Yes, I like surfing

Never, ever, ever create questions that can be answered from the persona information.
```

**Prompt explanation:** MemGPT persona for the document analysis task — primes the agent to keep searching archival storage until the answer is found, and to anchor temporal context to 2018.

```
You are MemGPT DOC-QA bot. Your job is to answer questions about documents that are stored in your archival memory. The answer to the users question will ALWAYS be in your archival memory, so remember to keep searching if you can't find the answer.
Answer the questions as if though the year is 2018.
```

**Prompt explanation:** Per-question instruction for MemGPT on document analysis — enforces a strict ANSWER/DOCUMENT response format so the LLM judge can grade both correctness and provenance.

```
Search your archival memory to answer the provided question. Provide both the answer and the archival memory result from which you determined your answer. Format your response with the format 'ANSWER: [YOUR ANSWER], DOCUMENT: [ARCHIVAL MEMORY TEXT]. Your task is to answer the question:
```

**Prompt explanation:** Baseline (no MemGPT) instruction for document QA — gives the model a fixed retrieved doc list and explicitly allows "INSUFFICIENT INFORMATION" to prevent unsourced hallucinations.

```
Answer the question provided according to the list of documents below (some of which might be irrelevant. In your response, provide both the answer and the document text from which you determined the answer. Format your response with the format 'ANSWER: <YOUR ANSWER>, DOCUMENT: [DOCUMENT TEXT]'. If none of the documents provided have the answer to the question, reply with 'INSUFFICIENT INFORMATION'. Do NOT provide an answer if you cannot find it in the provided documents. Your response will only be considered correct if you provide both the answer and relevant document text, or say 'INSUFFICIENT INFORMATION'. Answer the question as if though the current year is 2018.
```

**Prompt explanation:** LLM-judge prompt for the document analysis task — accepts paraphrases and more-specific answers as correct, but treats "INSUFFICIENT INFORMATION" or a missing DOCUMENT field as incorrect.

```
Your task is to evaluate whether an LLM correct answered a question. The LLM response should be the format "ANSWER: [answer], DOCUMENT: [document text]" or say "INSUFFICIENT INFORMATION". The true answer is provided in the format "TRUE ANSWER:[list of possible answers]". The questions is provided in the format "QUESTION: [question]". If the LLM response contains both the correct answer and corresponding document text, the response is correct. Even if the LLM's answer and the true answer are slightly different in wording, the response is still correct. For example, if the answer is more specific than the true answer or uses a different phrasing that is still correct, the response is correct. If the LLM response if "INSUFFICIENT INFORMATION", or the "DOCUMENT" field is missing, the response is incorrect. Respond with a single token: "CORRECT" or "INCORRECT".
```

**Prompt explanation:** MemGPT persona for the nested KV (multi-hop) retrieval task — explicitly instructs the agent to keep doing nested lookups until a value is verified as not also being a key.

```
You are MemGPT DOC-QA bot. Your job is to answer questions about documents that are stored in your archival memory. The answer to the users question will ALWAYS be in your archival memory, so remember to keep searching if you can't find the answer. DO NOT STOP SEARCHING UNTIL YOU VERIFY THAT THE VALUE IS NOT A KEY. Do not stop making nested lookups until this condition is met.
```

**Prompt explanation:** Baseline instruction for nested KV — describes the recursive lookup rule but provides the full JSON of pairs in-context rather than via search functions.

```
Below is a JSON object containing key-value pairings, all keys and values are 128-bit UUIDs, and your task is to return the value associated with the specified key. If a value itself is also a key, return the value of that key (do a nested lookup). For example, if the value of 'x' is 'y', but 'y' is also a key, return the value of key 'y'.
```

## Citations

- Vaswani et al. (2017) — Attention is all you need.
- Devlin et al. (2018) — BERT: Pre-training of deep bidirectional transformers.
- Brown et al. (2020) — Language models are few-shot learners (GPT-3).
- Touvron et al. (2023) — Llama 2: Open foundation and fine-tuned chat models.
- Liu et al. (2023a) — Lost in the middle: How language models use long contexts (arXiv:2307.03172).
- Schick et al. (2023) — Toolformer (function calling foundation).
- Patterson et al. (1988) — A case for RAID (the OS hierarchy precedent the paper builds on).
- Park et al. (2023) — Generative agents (closest prior work on LLM memory + planner).
- Xu et al. (2021) — Beyond goldfish memory: Long-term open-domain conversation (the MSC dataset).
- Zheng et al. (2023) — Judging LLM-as-a-judge with MT-bench (the judging method used here).

_(Full structured citation list — 35 entries total — in frontmatter `citations:` for the auto-research hook.)_

## Related Digests

- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall (the 2026 follow-on critique of write-time intelligence — MemGPT's deferred-compression instinct is exactly what Adler & Zehavi formalize three years later)

## Reviewer Notes

**Overall severity:** Clean

Every numeric claim in the digest was cross-checked against the paper text:

- DMR results (38.7% / 66.9% / 32.1% / 92.5% / 35.3% / 93.4%) — verified against Table 2.
- ROUGE-L values (0.394 / 0.629 / 0.296 / 0.814 / 0.359 / 0.827) — verified against Table 2.
- Nested KV result ("0% accuracy by 3 nesting levels", "MemGPT+GPT-4 unaffected") — verified against Section 3.2.2 narrative and Figure 7.
- "140 UUID pairs ≈ 8k tokens" and "nesting levels 0-4, 30 ordering configs" — verified against Section 3.2.2.
- Memory pressure threshold 70% / flush 100% / evict ~50% — verified against Section 2.2.
- Architecture component names (working_context, FIFO Queue, archival_storage, recall_storage, Function Executor, Queue Manager) — verified against Section 2 and Figure 3.
- pgvector + HNSW + text-embedding-ada-002 — verified against Section 3.2.1.
- "request_heartbeat=true" function chaining flag — verified against Figure 3 caption and Section 2.4.
- Document QA setup (NaturalQuestions-Open, 50 questions, top-K retrieval) — verified against Section 3.2.1.
- "GPT-3.5 underperforms with MemGPT" — verified against Figure 5 and Section 3.2.1 ("MemGPT has significantly degraded performance using GPT-3.5, due to its limited function calling capabilities").
- All extracted prompts copied verbatim from Section 6.1 appendix.

No metrics, methods, or tool names were fabricated. The ENGRAM dimension tags in the Implications section are the digester's interpretive overlay (per the memory-architect lens), not claims about the paper itself.
