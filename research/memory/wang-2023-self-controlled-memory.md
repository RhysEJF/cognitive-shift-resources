---
corpus: agentic-memory
kind: paper-digest
slug: wang-2023-self-controlled-memory
title: "Enhancing Large Language Model with Self-Controlled Memory Framework"
authors:
  - "Bing Wang"
  - "Xinnian Liang"
  - "Jian Yang"
  - "Hui Huang"
  - "Shuangzhi Wu"
  - "Peihao Wu"
  - "Lu Lu"
  - "Zejun Ma"
  - "Zhoujun Li"
year: 2023
publication_date: "2023-04"
venue: "arXiv preprint (Beihang / HIT / ByteDance AI Lab)"
source_url: "https://arxiv.org/abs/2304.13343"
doi: null
arxiv_id: "2304.13343"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Self-Controlled Memory (SCM) shows that the load-bearing component of a long-conversation memory architecture is not the memory store or the retriever — it is the controller: a small LLM-driven gate that, on every turn, asks 'do I need history?' and 'is a summary enough?' before fetching anything; without that gate (ablation), multi-turn accuracy collapses from 75% to 49% even though retrieval recall barely changes (94.0 → 93.8), proving that the win is signal-to-noise discipline at read time, not richer memory."
topics:
  - long-term-memory
  - llm-memory-controller
  - memory-stream
  - ultra-long-input
  - long-term-dialogue
  - book-summarization
  - meeting-summarization
  - recency-relevance-ranking
  - flash-memory
  - activation-memory
  - memory-controller-ablation
  - signal-to-noise-retrieval
tags:
  - paper
  - memory-architecture
  - memory-controller
  - llm-agent
  - bytedance-ai-lab
  - retrieval-gate
  - summarization-on-write
entities:
  - wang-bing
  - liang-xinnian
  - yang-jian
  - li-zhoujun
related_digests:
  - maharana-2024-locomo
  - packer-2023-memgpt-os
  - zhong-2023-memorybank-llm
  - xu-2025-a-mem-agentic-memory
  - park-2023-generative-agents
citations:
  - title: "Language models are few-shot learners (GPT-3)"
    authors: ["Tom B. Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    arxiv_id: "2005.14165"
  - title: "Longformer: The long-document transformer"
    authors: ["Iz Beltagy", "Matthew E. Peters", "Arman Cohan"]
    year: 2020
    venue: "preprint"
    arxiv_id: "2004.05150"
  - title: "Big Bird: Transformers for longer sequences"
    authors: ["Manzil Zaheer", "Guru Guruganesh", "et al."]
    year: 2021
    venue: "NeurIPS"
    arxiv_id: "2007.14062"
  - title: "Linformer: Self-attention with linear complexity"
    authors: ["Sinong Wang", "Belinda Z. Li", "Madian Khabsa", "Han Fang", "Hao Ma"]
    year: 2020
    venue: "preprint"
    arxiv_id: "2006.04768"
  - title: "Train short, test long: Attention with linear biases enables input length extrapolation (ALiBi)"
    authors: ["Ofir Press", "Noah Smith", "Mike Lewis"]
    year: 2022
    venue: "ICLR"
    arxiv_id: "2108.12409"
  - title: "Recursively summarizing books with human feedback"
    authors: ["Jeff Wu", "Long Ouyang", "Daniel M. Ziegler", "et al."]
    year: 2021
    venue: "preprint"
    arxiv_id: "2109.10862"
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "He Ye", "Yanlin Wang"]
    year: 2023
    venue: "preprint"
    arxiv_id: "2305.10250"
  - title: "VCSum: A versatile Chinese meeting summarization dataset"
    authors: ["Han Wu", "Mingjie Zhan", "Haochen Tan", "et al."]
    year: 2023
    venue: "preprint"
    arxiv_id: null
  - title: "LongT5: Efficient text-to-text transformer for long sequences"
    authors: ["Mandy Guo", "Joshua Ainslie", "David Uthus", "et al."]
    year: 2022
    venue: "NAACL Findings"
    arxiv_id: null
  - title: "Llama: Open and efficient foundation language models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "preprint"
    arxiv_id: "2302.13971"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Workflow of the Self-Controlled Memory (SCM) framework — six explicit steps from observation to response"
  page: 3
  image_path: "figures/wang-2023-self-controlled-memory-fig.png"
---

# Enhancing Large Language Model with Self-Controlled Memory Framework

**Authors:** Bing Wang, Xinnian Liang, Jian Yang, Hui Huang, Shuangzhi Wu, Peihao Wu, Lu Lu, Zejun Ma, Zhoujun Li
**Published:** 2023-04 · [Source](https://arxiv.org/abs/2304.13343)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Wang et al. (Beihang / HIT / ByteDance AI Lab) propose the Self-Controlled Memory (SCM) framework, a plug-and-play memory layer wrapping any instruction-following LLM (they evaluate `text-davinci-003` and `gpt-3.5-turbo-0301`) so that it can handle 20k–2M token inputs without fine-tuning or architectural changes. SCM has three components: (1) an **LLM-based agent** as the response generator, (2) a **memory stream** holding all past interactions — each item is a tuple of `{interaction_index, observation, response, summary, embedding}` keyed by a `text-embedding-ada-002` vector — backed by Redis/Pinecone, and (3) a **memory controller**, itself an LLM, that on every turn answers two yes/no questions: *"is memory retrieval necessary for this user input?"* and *"can the user input be answered using only the summary of the retrieved memory?"*. Retrieved memory is partitioned into **Activation Memory** (top-k items ranked by `recency_score + relevance_score` with k ∈ [3,10]) and **Flash Memory** (the immediately preceding turn T−1). The benchmark is a new dataset across three tasks — long-term dialogue (18 instances, up to 34k tokens, 200 turns), book summarization (10 instances, up to 2M tokens), meeting summarization (20 instances, up to 50k tokens) — with 105 hand-annotated probing questions split into single-turn (49) and multi-turn (56). Headline ablation: `SCM-davinci003` scores 77.1% answer accuracy / 75.0% multi-turn accuracy; removing the controller drops these to 59.3% / 49.4%; removing activation memory drops them to 10.5% / 0.0%. RecursiveSum (OpenAI's recursive-summarize baseline) is beaten on both coverage and coherence in side-by-side human eval on books and meetings.

## Key Takeaway

The architectural lesson is that the **memory controller is the load-bearing component, not the store**. Standard memory architectures over-invest in encoding (write-time distillation) and retrieval (clever vector indexes) while leaving the gate that decides *whether to retrieve at all* and *whether the summary is enough* as a hard-coded if/else or a per-query top-k constant. SCM moves that gate inside the LLM itself: two prompts ("is memory necessary? Y/N", "can the summary answer this? Y/N") run on every observation. The ablation isolates the gate's contribution cleanly: removing it leaves the same memory stream, the same recency+relevance ranking, the same retrieval recall (93.8% vs 94.0%) — and multi-turn accuracy still collapses 25.6 absolute points, from 75.0% to 49.4%. The mechanism is signal-to-noise: without the gate, the system concatenates retrieved content and truncates at 2,500 tokens; with the gate, it prunes irrelevant retrieved items and substitutes summaries for verbose ones, leaving room in the context window for what actually matters. The corollary: high retrieval recall is a misleading metric for memory systems; if your downstream accuracy doesn't move when you ablate the controller, you have a noise problem, not a recall problem. (ENGRAM: this is primarily an **R** (Retrieve) and **A** (Aggregate) story — the controller is a *retrieval-time decision layer* and the summary-vs-full-content choice is *content-shape adaptation at read time*; **E** matters too because per-turn summaries are pre-computed on the write path.)

## Implications

- **Add an explicit "is retrieval necessary?" gate before every retriever call** (ENGRAM: **R**). The SCM ablation isolates this exact decision and shows 25.6 absolute points of multi-turn accuracy depend on it. For a Flow OS-style memory system, this means the response loop should not unconditionally query QMD on every turn — wrap retrieval in a small LLM call ("does this turn need history? Y/N") and skip retrieval when the answer is N. Cost is ~1 extra LLM call per turn (cheap); win is dramatically less noise in the response prompt.

- **Pre-compute per-turn summaries on the write path, then choose summary-vs-full at read time** (ENGRAM: **E**, **A**). SCM stores `{observation, response, summary, embedding}` for every interaction. The summary lets the read-time controller substitute a compressed version when the full content would exceed a budget. Architecturally this is the same idea as paged virtual memory's "page table entry holds metadata about content" — the page itself (full text) lives in the store, but the summary lives in the index. Result: per-item, the system can adaptively decide compression ratio based on the query.

- **Recency + Relevance, with addition (not multiplication), is the SCM ranking function** (ENGRAM: **R**). `rank_score = recency_score + relevance_score`. Addition has the property that a very-recent-but-irrelevant item can still surface (which matters when the user is referring to "the thing we just discussed"), and a very-relevant-but-old item can still surface (which matters for callbacks). This is functionally equivalent to Park-style generative-agents scoring (recency × importance × relevance), but with importance dropped and a simpler addition operator. For Flow OS's QMD layer, mixing in a recency boost at retrieval-rank time (not just at score time) would be a small change with potentially large impact for ongoing-conversation use cases.

- **Concatenating retrieved content and truncating at 2,500 tokens is the bad baseline** (ENGRAM: **R**, **A**). The "w/o memory controller" condition (SCM's ablation) is essentially what most naive RAG stacks do today — top-k retrieve, concatenate, truncate. The 25.6-point drop in multi-turn accuracy is the cost of that default. Any team building a memory layer should reproduce this ablation on their own benchmark; if their controller-vs-no-controller delta is tiny, their retriever is over-fetching (or the controller is under-discriminating).

- **Flash Memory ablation barely moves the needle** (ENGRAM: **R**). Removing the immediately-prior-turn flash memory drops accuracy by only 4.2 points. This is counter-intuitive — you'd expect the immediately preceding turn to be load-bearing. The explanation in the paper: the probing questions in the benchmark are mostly about *distant* history, not the immediate preceding turn, so flash memory's value is mostly bounded by the question distribution. If your application is dominated by "what did you just say?" style follow-ups, flash memory is more valuable than this ablation suggests.

- **Activation memory is everything** (ENGRAM: **R**, **M**). The most dramatic ablation: removing long-term (activation) memory drops accuracy to 10.5% overall and 0.0% on multi-turn. This isn't surprising in itself, but the magnitude tells you that 60+% of the framework's headline number comes from the retrieval-from-long-term-store path. Optimisation effort should be proportionate.

- **The framework is plug-and-play across LLMs but performance is bottlenecked by the controller LLM's instruction-following quality** (ENGRAM: **R**, **M**). The paper notes a limitation: SCM works well with `text-davinci-003` and `gpt-3.5-turbo-0301` because they can reliably answer the controller's yes/no questions. Weaker instruction-following models will degrade the gate. For Flow OS this matters because the controller LLM doesn't need to be the response LLM — you can run a cheaper instruction-following model (Haiku, a small Qwen) as the gate and the large model as the responder.

## How to Apply It (method)

**Scenario:** You're building Flow OS's per-session response loop and you've noticed that your assistant either over-pulls memory (response prompts hit context limits, generation gets diluted) or under-pulls (forgets what was said three turns ago). You want a controlled retrieval gate that decides per-turn whether to pull history at all, and whether the compressed or full version is enough.

**Steps:**

1. **Add a `summary` field to every stored memory item** (write-time). When you persist a turn, run a single LLM call with this prompt (SCM's Figure 3 prompt):

   ```
   Below is a conversation between a user and an AI assistant. Please provide a summary of the user's question and the assistant's response in one sentence each, with separate paragraphs, while preserving key information as much as possible.

   Conversation:
   User: {user input}
   Assistant: {system response}

   Summary:
   ```

   Store the summary alongside the raw text. This adds ~50ms and ~$0.0002 per turn but unlocks the read-time choice.

2. **Replace "always retrieve top-k" with a gated retrieval** (read-time). Before calling QMD, run this Figure 5 prompt:

   ```
   Given a user command, determine whether executing the command requires historical or previous information, or whether it requires recalling the conversation content. Simply answer yes (A) or no (B) without explaining the information:

   User Command: {user_input}

   Answer:
   ```

   If the answer is B, skip retrieval entirely — go straight to the LLM with just the current observation + flash memory (preceding turn). This will cut your retrieval call count by 30–60% in normal conversation and remove a substantial amount of noise.

3. **For items above a size threshold, run a summary-sufficiency gate** (read-time). For each activated memory item that exceeds 800 tokens (and when total activation > 2,000 tokens), ask:

   ```
   Given the conversation content and the user question, please answer the command question.

   Conversation Content: ```{summary}```
   User Question: ```{query}```

   Command Question: Based on the conversation content, can the user question be answered by conversation content? Respond with (A) for yes, (B) for no.
   ```

   If A, swap the full content for its summary in the prompt. This is the SCM's compression-on-demand pattern.

4. **Use recency + relevance ranking with addition** (read-time). For each candidate memory `m`, compute `rank_score(m) = recency_score(m) + relevance_score(m)`, where:
   - `relevance_score(m) = cosine_similarity(query_embedding, memory_embedding)`
   - `recency_score(m) = exp(-Δt / τ)` for some half-life τ (SCM doesn't specify; pick τ such that a one-day-old memory scores ~0.5)
   Take top-k for `k ∈ [3, 10]`. The paper doesn't ablate `k`, but you should sweep it on your own data; for memory-architect work the LoCoMo finding (peak at k=5 for distilled units) is a reasonable prior.

5. **Run the controller ablation on your own benchmark before shipping**. The single most useful experiment is to A/B (controller-on, controller-off) on your test set. If the delta is < 5 points on multi-turn accuracy, your controller's prompts are not discriminating enough — iterate on the wording. If the delta is > 15 points, ship it.

6. **Treat the controller LLM as a separate model from the responder**. You don't need GPT-4 for "is retrieval necessary?" — a Haiku-tier model is plenty, costs ~$0.0001 per gate call, and means you can run the gate on every turn without budget anxiety.

7. **Combine SCM with a paged-virtual-memory layer (MemGPT-style) for unbounded conversations**. SCM doesn't address eviction — it assumes the memory stream is a single growing list with Redis-style cache speedup. For Flow OS-scale data, you need a tier-promote/tier-demote story on top (which is exactly what MemGPT and MemoryOS provide). SCM's controller becomes the *L1 cache decision-maker* in that stack; the OS-style paging becomes the *L1/L2 tier mover*.

**Expected outcome:** Per-turn cost increases by ~1 small-model LLM call (~$0.0001–0.0005). Response-prompt size decreases substantially (30–60% fewer turns will pull history at all, and pulled history is shorter when summaries can substitute). Multi-turn accuracy in your end-to-end eval moves up by 10–25 absolute points, matching SCM's 75.0% → 49.4% delta direction in their long-term dialogue benchmark.

## Best Figure

![Figure 2 — Workflow of the Self-Controlled Memory (SCM) framework — six explicit steps (page 3)](figures/wang-2023-self-controlled-memory-fig.png)

Image Candidates:

- **Figure 2 (p. 3):** Workflow diagram of the SCM framework — the six-step loop from observation acquisition to response generation, with Memory Stream, Activation Memory, Flash Memory and Memory Controller labeled in the data-flow. This is the load-bearing architecture diagram.
- **Figure 4 (p. 4):** Memory Controller decision tree — the two-question gate ("Is memory retrieval necessary?" → "Summary or Full Content?"). This is the *single most important* diagram for the architectural insight; it shows the gate logic that the ablations later prove is load-bearing.
- **Table 2 (p. 6):** Long-term dialogue evaluation results with the ablation rows. This is the empirical evidence that the controller is load-bearing — the "-25.6 multi-turn accuracy" cell when the controller is removed.

**Best Image — Figure 2: The workflow of the SCM framework** (page 3). The figure shows the six-step loop visually: observation #T arrives, the memory controller (left) decides whether to activate memory, retrieves from the memory stream (top-left), produces an activation memory bundle that combines with flash memory (memory from #T-1) and the observation as input to the LLM agent (center), which generates response #T (right), and finally the new (observation, response, summary, embedding) tuple is appended back to the memory stream. The numbered labels 1–6 make the loop traceable in one glance. This is the clearest single-image representation of the "controller as gate + memory as store + LLM as responder" architecture that the rest of the paper experimentally defends.

## What Experts Overlook

The most overlooked operational detail is the **embedding strategy for memory items**: SCM concatenates *observation summary + response summary* (not raw observation + raw response, and not raw observation alone) before embedding with `text-embedding-ada-002`. The paper's stated reason (§2.3) is that the observation and response can differ in length by an order of magnitude — a 4-word user input and a 600-word assistant response — and embedding raw text gives the response disproportionate influence on the vector. Embedding the summaries normalises the contribution of each side.

**Why it matters:** Most teams shipping QMD-style memory layers embed the raw text and call it done. This means a chatty assistant's responses dominate the vector space and user-intent retrieval starts to drift toward "assistant said X" rather than "user wanted X" matching. For Flow OS's per-session memory layer (transcripts + extracted memories), this suggests:

- Embed the summary, not the raw turn — the raw turn stays as the payload for the LLM to read.
- If you can't / don't want a summary step on the write path, at minimum truncate the response and the observation to comparable lengths before embedding.

**Example of good use:** A `/learn`-extracted memory carries `{full_text, summary, summary_embedding}` in its frontmatter. QMD indexes the summary text; the responder reads the full text. Retrieval is over user-intent-shaped vectors; generation has access to the un-lossy source.

**Example of misapplication:** A team builds a memory store that embeds raw concatenated dialogue, ships it, and notices that conversations about *implementation details of the assistant's own past responses* dominate retrieval. They blame the embedding model, swap embedding models, see no improvement. The bug is in the input to the embedder, not the embedder itself.

## Extracted Prompts

**Prompt explanation:** Memory-necessity gate (Figure 5). Determines whether the current user input requires retrieval at all. The single most important controller prompt — the SCM ablation shows the rest of the architecture's gains depend on this gate working.

```
Given a user command, determine whether executing the command requires historical or previous information, or whether it requires recalling the conversation content. Simply answer yes (A) or no (B) without explaining the information:

User Command: {User Input}

Answer:
```

**Prompt explanation:** Summary-sufficiency gate (Figure 6). For each activated memory item > 800 tokens (when total activation > 2,000 tokens), this prompt decides whether the precomputed summary is enough or the full content must be inlined. This is the read-time compression-on-demand mechanism.

```
Given the conversation content and the user question, please answer the command question.

Conversation Content: ```{content}```
User Question: ```{query}```

Command Question: Based on the conversation content, can the user question be answered by conversation content? Respond with (A) for yes, (B) for no.

Please strictly follow the format below to answer the questions:
[Answer]: (A) / (B).
```

**Prompt explanation:** Memory summarization for dialogue (Figure 3). Run on the write path for every interaction. Produces the `summary` field stored alongside the raw turn. Crucially the summary is *bipartite* — separate one-sentence summaries of the user question and assistant response — so that embedding-time the two sides contribute equally.

```
Below is a conversation between a user and an AI assistant. Please provide a summary of the user's question and the assistant's response in one sentence each, with separate paragraphs, while preserving key information as much as possible.

Conversation:

User: {user input}
Assistant: {system response}

Summary:
```

**Prompt explanation:** Response generation with retrieved memory (Figure 7). Combines the retrieved history with the immediately preceding turn (flash memory) and the new user input into the final responder prompt. The `history_turn` field is the retrieved activation memories (full text or summary depending on the read-time gate decisions).

```
Here is a conversation between a user and an AI assistant. Please answer the user's current question based on the history of the conversation:

History of the conversation: {history_turn}

Previous conversation: {last_turn}

###

User: {user_input}
Assistant:
```

## Citations

The paper cites ~30 works spanning long-context architectures (Longformer, BigBird, Linformer, ALiBi, LongT5), foundation LLMs (GPT-3, LLaMA, BLOOM, PaLM, OPT), instruction-tuning recipes (FLAN, InstructGPT), and conversational memory work (MemoryBank). Full list in frontmatter. Most relevant for the memory-architect lens: Zhong et al. 2023 (MemoryBank — already in wiki), Beltagy 2020 (Longformer — already in wiki), Press 2022 (ALiBi).

## Related Digests

- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents (the seed for this citation walk; SCM cites it as related contemporaneous work)
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems (similar OS-inspired framing; SCM is the controller-as-gate, MemGPT is the paging-as-memory-tier)
- [[zhong-2023-memorybank-llm]] — MemoryBank: Enhancing LLMs with Long-Term Memory (the closest contemporary architecture; SCM uses MemoryBank as a comparator)
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: Agentic Memory for LLM Agents (next-gen version of the controller-as-gate idea, where the gate also rewrites neighbouring memories)
- [[park-2023-generative-agents]] — Generative Agents: Interactive Simulacra of Human Behavior (recency × importance × relevance scoring, the canonical precursor to SCM's recency + relevance addition)

## Reviewer Notes

**Severity: Clean.**

Cross-checked the digest against the paper:

- Numbers in the ablation table (77.1 / 75.0 / 59.3 / 49.4 / 10.5 / 0.0 / 94.0 / 93.8) match Table 2 exactly.
- Dataset statistics (18 dialogues / 10 books / 20 meetings; 34k / 2M / 50k max tokens; 200 / -- / 80 max turns) match Table 1.
- 105 probing questions (49 single-turn + 56 multi-turn) is from the caption of Table 2.
- The two controller prompts (necessity, summary-sufficiency) are accurate transcriptions from Figures 5 and 6.
- The summarization prompt (Figure 3) is accurately transcribed.
- The recency + relevance addition formula `rank_score = recency_score + relevance_score` is on p. 4.
- The "controller is also a language model" claim is from §2.4.
- The author affiliation list (Beihang / HIT / ByteDance AI Lab) matches the title page.

One paraphrase to flag: the digest claims "60+%" of the framework's headline accuracy comes from activation memory (based on the -66.6 single-turn drop and -75.0 multi-turn drop when activation memory is removed). The paper itself only says "approximately 60% decrease in performance" — the digest's framing is consistent with that and not overstated.

No invented facts, no misattributed citations.
