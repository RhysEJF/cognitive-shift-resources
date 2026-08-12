---
corpus: agentic-memory
kind: paper-digest
slug: li-2024-ld-agent
title: "Hello Again! LLM-powered Personalized Agent for Long-term Dialogue"
authors:
  - "Li, Hao"
  - "Yang, Chenghao"
  - "Zhang, An"
  - "Deng, Yang"
  - "Wang, Xiang"
  - "Chua, Tat-Seng"
year: 2024
publication_date: "2024-06"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2406.05925"
doi: "10.48550/arXiv.2406.05925"
arxiv_id: "2406.05925"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Decomposing long-term dialogue memory into three independently tunable modules — event-summary long+short memory bank with topic-overlap+semantic+time-decay retrieval, bidirectional user/agent persona extractor, and a unified response generator — beats single-model approaches by 2-10 BLEU points across MSC and CC benchmarks, with the topic-noun overlap signal (Equation 1) adding measurably more retrieval accuracy than pure semantic similarity (~20pt accuracy gap on human eval), proving that lexical noun-overlap is still a load-bearing signal even when stacked on top of dense retrieval."
topics:
  - long-term-dialogue
  - personalized-agent
  - memory-architecture
  - persona-extraction
  - retrieval-augmented-generation
  - event-summarization
  - bidirectional-modeling
tags:
  - paper
  - memory
  - dialogue
  - ld-agent
  - persona
  - chatbot
entities:
  - li-hao
  - yang-chenghao
  - zhang-an
  - deng-yang
  - wang-xiang
  - chua-tat-seng
related_digests:
  - wu-2024-longmemeval
  - chhikara-2025-mem0
  - xu-2021-beyond-goldfish-memory
  - maharana-2024-locomo
citations:
  - title: "Beyond goldfish memory: Long-term open-domain conversation (MSC dataset)"
    authors: ["Xu, J.", "Szlam, A.", "Weston, J."]
    year: 2022
    doi: "10.18653/v1/2022.acl-long.356"
    url: "https://aclanthology.org/2022.acl-long.356/"
    arxiv_id: null
  - title: "Long time no see! Open-domain conversation with long-term persona memory"
    authors: ["Xu, X.", "Gou, Z.", "Wu, W.", "Niu, Z.-Y.", "Wu, H.", "Wang, H.", "Wang, S."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    authors: ["Park, J. S.", "O'Brien, J.", "Cai, C. J.", "Morris, M. R.", "Liang, P.", "Bernstein, M. S."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Conversation Chronicles (CC): Towards Diverse Temporal and Relational Dynamics in Multi-Session Conversations"
    authors: ["Jang, J.", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "History-aware hierarchical transformer for multi-session long-term dialogue (HAHT)"
    authors: ["Zhang, T.", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "ChatGLM-6B/130B"
    authors: ["Zeng, A.", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Recipes for building an open-domain chatbot (BlenderBot)"
    authors: ["Roller, S.", "et al."]
    year: 2021
    doi: null
    url: null
    arxiv_id: null
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    authors: ["Wei, J.", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "Finetuned Language Models are Zero-Shot Learners (instruction tuning)"
    authors: ["Wei, J.", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers"
    authors: ["Wang, W.", "et al."]
    year: 2020
    doi: null
    url: null
    arxiv_id: null
  - title: "DialogSum: A Real-Life Scenario Dialogue Summarization Dataset"
    authors: ["Chen, Y.", "Liu, Y.", "Chen, L.", "Zhang, Y."]
    year: 2021
    doi: null
    url: null
    arxiv_id: null
  - title: "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension"
    authors: ["Lewis, M.", "et al."]
    year: 2020
    doi: null
    url: null
    arxiv_id: null
  - title: "GSN: A Graph-Structured Network for Multi-Party Dialogues (Ubuntu IRC)"
    authors: ["Hu, W.", "et al."]
    year: 2019
    doi: null
    url: null
    arxiv_id: null
  - title: "LoRA: Low-Rank Adaptation of Large Language Models"
    authors: ["Hu, E. J.", "Shen, Y.", "Wallis, P.", "Allen-Zhu, Z.", "Li, Y.", "Wang, S.", "Wang, L.", "Chen, W."]
    year: 2022
    doi: null
    url: null
    arxiv_id: null
  - title: "BLEU: a Method for Automatic Evaluation of Machine Translation"
    authors: ["Papineni, K.", "Roukos, S.", "Ward, T.", "Zhu, W.-J."]
    year: 2002
    doi: null
    url: null
    arxiv_id: null
  - title: "ROUGE: A Package for Automatic Evaluation of Summaries"
    authors: ["Lin, C.-Y."]
    year: 2004
    doi: null
    url: null
    arxiv_id: null
  - title: "METEOR: An Automatic Metric for MT Evaluation with Improved Correlation with Human Judgments"
    authors: ["Banerjee, S.", "Lavie, A."]
    year: 2005
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "The Framework of LD-Agent — Event Module (long+short memory) + Persona Module (bidirectional extractor) + Response Module (unified generator)"
  page: 5
  image_path: "figures/li-2024-ld-agent-fig.png"
---

# Hello Again! LLM-powered Personalized Agent for Long-term Dialogue

**Authors:** Hao Li, Chenghao Yang, An Zhang, Yang Deng, Xiang Wang, Tat-Seng Chua
**Published:** 2024-06 · [Source](https://arxiv.org/abs/2406.05925)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

LD-Agent attacks long-term open-domain dialogue with a 3-module decomposition:
1. **Event memory module** — splits memory into long-term (vector-encoded event summaries indexed in a memory bank, MiniLM encoder) and short-term (timestamped dialogue cache, flushed every 600 seconds into long-term). Retrieval combines three signals: semantic similarity `s_sem` (with γ=0.5 threshold to abstain when nothing matches), topic-noun overlap `s_top` (Eq 1: symmetric Dice-like coefficient over extracted noun sets), and time-decay `λ_t = e^(-t/τ)` with τ=1e7. The final score is `s_overall = λ_t (s_sem + s_top)`. Event summarization itself is *instruction-tuned* (not zero-shot) on a restructured DialogSum dataset.
2. **Persona module** — bidirectional user-AND-agent persona banks, populated by a tunable extractor (LoRA on top of base LLM) trained on an MSC-derived persona-extraction dataset. When utterance has no traits, extractor outputs `NO_TRAIT`. Falls back to Chain-of-Thought zero-shot extraction if no tuning data available.
3. **Response generation** — generator receives `(current utterance, retrieved memories, short-term context, user personas, agent personas)`, trained on a custom dataset built by simulating progression through MSC/CC sessions with all upstream modules engaged.

The framework is model-agnostic — tested on ChatGPT, ChatGLM, BlenderBot, BART. Across MSC and CC benchmarks (5 sessions each, ~50 turns/sample), LD-Agent lifts every base model by significant margins: ChatGLM_LDA tuned on CC hits BL-2=25.69 vs base ChatGLM 15.89 on session 2 of CC (+9.8pt absolute). Ablation shows event memory contributes most, persona modules add stable consistency over time. Cross-domain (train on MSC, test on CC and vice versa) shows only slight degradation, beating zero-shot by large margins. Human evaluation on retrieval shows topic-noun overlap retrieval beats pure semantic retrieval by ~20pt accuracy and ~20pt recall — the simple lexical signal still does load-bearing work.

## Key Takeaway

**Lexical noun-overlap is not obsoleted by dense retrieval — it's complementary, and the gap is large.** [R + G] The architectural temptation in 2024 was to assume that good embeddings (MiniLM, BGE, OpenAI ada) make symbolic signals like noun overlap redundant. LD-Agent's Figure 3a human evaluation falsifies this for long-term dialogue retrieval: pure semantic retrieval underperforms topic-noun retrieval by ~20pt accuracy and ~20pt recall on the same memory bank, same encoder. The fix isn't a better encoder; it's adding a Dice-like noun-overlap term (Eq 1: `(|V_q ∩ V_k| / |V_q| + |V_q ∩ V_k| / |V_k|) / 2`) to the semantic score. This works because dialogue utterances are short, semantically ambiguous, and full of pronouns — the dense encoder doesn't disambiguate "the bike" → "the white bike I bought one month ago" reliably, but the noun "bike" anchors the retrieval lexically. Combined with a time-decay term `e^(-t/τ)` to bias recent memories, the three-signal sum dominates any single-signal approach. Architectural lesson: when retrieval lives over short, redundant, sparse-content units (dialogue turns), lexical signals are not "old retrieval tech"; they're orthogonal to semantic signals and stack additively.

## Implications

- **[E + A] Instruction-tune the event summarizer; don't trust zero-shot.** The paper rebuilds DialogSum into an instruction-tuned dataset specifically for event summarization, and reports this directly improves summary quality (no ablation table, but the design choice is explicit in §3.2.1). The implicit comparison is with Generative Agents (Park 2023) and other systems that "entirely rely on LLM's zero-shot ability to excavate and summarize events" — LD-Agent argues this is leaving accuracy on the table. For Flow OS this maps to fine-tuning Haiku on a Flow-OS-specific summary dataset built from `/learn` outputs, rather than relying on Haiku's zero-shot summarization.
- **[N] Short-term + long-term split with explicit consolidation trigger.** Short-term memory holds the current session's raw turns with timestamps. When inactivity exceeds β=600 seconds, the short-term cache is summarized (via the tuned event-summary module) into a long-term entry, then cleared. This is the only explicit "consolidation" event in the system — it converts episodic detail into semantic event memory at a defined boundary. The 600-second threshold is a Schelling point: long enough to capture a session, short enough to avoid concatenating unrelated conversations.
- **[R] Three-signal retrieval beats single-signal — and topic-overlap > semantic alone.** The retrieval ranking is `s_overall = λ_t (s_sem + s_top)`, gated by a semantic-similarity threshold γ=0.5 (below which "No relevant memory" is returned — explicit abstention). Figure 3a shows topic-noun retrieval beats direct semantic by ~20pt across both ACC and Recall. This is a real, measured advantage of mixed signals over pure dense retrieval. The Dice-like overlap formula (Eq 1) is normalized symmetrically — `(|V_q ∩ V_k| / |V_q| + |V_q ∩ V_k| / |V_k|) / 2` — so it doesn't blow up for short queries or short keys.
- **[G] Explicit abstention via γ threshold prevents "wrong memory" failures.** If the highest-scoring memory's semantic score is below γ=0.5, retrieval returns "No relevant memory" rather than the best (still-bad) match. This is rare in memory papers — most assume the retriever always returns SOMETHING. LD-Agent's design treats "no answer" as a first-class output of retrieval, which means the downstream generator sees an explicit cue to not invent context. Crucial for long-term agents where many queries reference no historical event at all.
- **[A] Bidirectional persona modeling (user AND agent) is non-default but worth it.** Most persona work models only the user. LD-Agent runs two persona banks — one for the user, one for the agent — and updates both from every turn. The agent-persona bank ensures the agent stays consistent ("I am professional swimmer" doesn't drift to "I'm scared of water"). Ablation (Table 2) shows agent-persona alone contributes BL-2 +1.5pt on MSC; user-persona +1.6pt; memory module is biggest at +2pt; combined Full is +5pt.
- **[A + E] LoRA-based persona extractor with `NO_TRAIT` output.** Persona extraction is a binary problem followed by a free-text problem: does this utterance contain a personality trait? If yes, extract it; if no, output `NO_TRAIT`. Table 3 shows LoRA-tuning the extractor lifts the binary classification ACC from 61.6% (zero-shot CoT) to 77.8%, and the extracted-trait quality (BLEU-2: 5.05→8.31, R-L: 25.54→43.70). The 16pt ACC lift specifically reduces the "this turn says nothing personal, but extractor invents a trait anyway" failure mode that pollutes the persona bank with noise.
- **[M] Cross-domain generalization is the test of decomposed architectures.** LD-Agent tuned on MSC and tested on CC retains most of its advantage (Table 8: CC-tuning_LDA = 25.69 BL-2 vs MSC-tuning_LDA = 21.71 BL-2 on CC session 2; both vastly above CC-tuning baseline = 15.89). The modular decomposition makes this possible — only the generator needs cross-domain robustness; the event summarizer and persona extractor are dataset-agnostic by design. Monolithic dialogue models lose much more cross-domain.
- **[N + M] LD-Agent doesn't propagate timestamps into the retrieved memory string itself.** The time-decay is folded into the retrieval score (λ_t multiplier) but the memory text passed to the generator is just the summary, not "(2024-04-17) summary text". This means the generator can't reason about *which* time period a memory came from. Compared to Wu 2024 (LongMemEval), this is a known weakness for temporal-reasoning queries: "what happened *last* week" needs the timestamp visible to the reader, not just biased in retrieval.

## How to Apply It (method)

**Scenario:** Flow OS already maintains per-session memory files via `/learn`. Users converse with the agent across sessions and weeks. We want the agent to (a) bring up relevant past topics naturally ("last week you decided to go with Dana"), (b) maintain consistent traits ("you tend to prefer biweekly cadence with engineering teams"), and (c) not hallucinate context from sessions that don't exist. LD-Agent is a near-drop-in pattern for these three goals.

**Steps:**

1. **Build the event memory bank.** For every session memory file produced by `/learn`, run an event-summary LLM call (Sonnet/Haiku) with this verbatim system+user prompt from Appendix D.1:
   ```
   SYS PROMPT: You are good at extracting events and summarizing them in brief sentences. You will be shown a conversation between {user name} and {agent name}.
   USER PROMPT: Conversation: {context}. Based on the Conversation, please summarize the main points of the conversation with brief sentences in English, within 20 words.
   SUMMARY:
   ```
   The 20-word constraint is critical — keeps the summaries short, focused, retrieval-friendly. Embed each summary with QMD's encoder; store as `{timestamp, summary, embedding, noun_topics: extract_nouns(summary)}` in a long-term memory bank table.
2. **Extract noun topics at write time.** For each summary, run a noun extractor (spaCy or a small LLM call) to get `V_k = {noun1, noun2, ...}`. Store alongside the embedding. This is what powers the topic-overlap retrieval signal.
3. **Build the persona bank, bidirectional.** Run a persona extractor over every user message AND every agent response with this verbatim prompt (Appendix D.2):
   ```
   SYS: You excel at extracting user personal traits from their words, a renowned local communication expert.
   USER: If no traits can be extracted in the sentence, you should reply NO_TRAIT. Given some format examples...
   1. "I no longer serve in the military..." → Extracted Traits: I now work elsewhere. I used to be in the military.
   2. "That must have been some kind of endeavor..." → NO_TRAIT
   Please extract the personal traits who said this sentence (no more than 20 words): {sentence}
   ```
   Maintain two persona banks: `P_user` (traits about the user) and `P_agent` (traits about the Flow agent's stable identity). De-dupe via cosine similarity on persona embeddings; append only novel traits.
4. **Wire short-term memory with a 10-minute flush trigger.** Maintain `M_S = {(t_i, u_i)}` for the current session in volatile storage. When `t_now - t_last > 600 seconds` and a new utterance arrives, summarize the entire `M_S` via the event-summary LLM, embed it, store as a new long-term memory, then clear `M_S`. This is the consolidation moment.
5. **Implement three-signal retrieval at query time.** For each new user utterance `q`:
   - Compute `V_q = extract_nouns(q)`.
   - Compute `s_sem(q, k) = cosine_sim(embed(q), embed(k))` for each memory.
   - Compute `s_top(q, k) = (|V_q ∩ V_k| / |V_q| + |V_q ∩ V_k| / |V_k|) / 2`.
   - Compute `λ_t = exp(-(t_now - t_k) / τ)` with `τ = 1e7` (the paper's setting — roughly a 4-month half-life; tune for Flow OS based on session frequency).
   - `s_overall = λ_t * (s_sem + s_top)`.
   - Filter to memories where `s_sem > γ=0.5` (abstention threshold).
   - If empty set: pass "No relevant memory" to generator.
   - Else: take top-k by `s_overall`.
6. **Construct the response generation prompt** (Appendix D.3, Prompt 4):
   ```
   SYS: As a communication expert with outstanding communication habits, you embody the role of {agent_name}. Here are some of your distinctive personal traits: {agent_traits}.
   USER:
   <CONTEXT>
   Drawing from your recent conversation with {user_name}:
   {short_term_context}
   <MEMORY>
   The memories linked to the ongoing conversation are:
   {retrieved_memories}
   <USER TRAITS>
   During the conversation process between you and {user_name} in the past, you found that the {user_name} has the following characteristics:
   {user_traits}
   Now, please role-play as {agent_name} to continue the dialogue.
   {user_name} just said: {input}
   Please respond using the following format (maximum 30 words, must be in English):
   RESPONSE:
   ```
   The 30-word response limit is in the paper — for Flow OS, relax it but keep the structural sections (CONTEXT / MEMORY / USER TRAITS / agent traits in system).
7. **Add timestamps to retrieved memory strings** — this is the one place I'd improve on LD-Agent. The paper passes only summary text; add the date inline ("(2024-04-17) Discussed switching to biweekly cadence with Dana") so the generator can reason temporally. This addresses LongMemEval's finding that time-aware reading lifts performance 6-10pt on temporal queries.

**Expected outcome:** On Flow OS dialogue evals, retrieval ACC should be ~20pt higher than pure-semantic baseline (replicating Figure 3a). Response quality should improve materially on questions referencing past sessions, especially after multiple turns where the context window is filling up. Persona consistency should hold across weeks — the agent shouldn't "forget" stable user traits between sessions.

## Best Figure

![Figure 2 — The Framework of LD-Agent (page 5)](figures/li-2024-ld-agent-fig.png)

Image Candidates:
Figure 2 (p. 5): Three-module framework diagram showing Event Module (long+short memory), Persona Module (bidirectional extractor), and Response Module (unified generator). Clearest single view of the decomposed architecture.
Figure 1 (p. 3): The motivating before/after dialogue example showing how event summary and personas guide responses (girl offers to teach swimming based on a one-week-old conversation). Better for narrative pitch, weaker for methodology.
Figure 3a (p. 9): Topic vs semantic retrieval head-to-head showing the ~20pt gap that proves topic-noun overlap is load-bearing. The strongest single numerical result.

Best Image:
Figure Name: Figure 2: "The Framework of LD-Agent"
Figure Page: 5
Slide Caption: LD-Agent decomposes long-term dialogue memory into three tunable modules — long+short event memory, bidirectional user-agent persona banks, and a response generator that integrates all signals — making each module independently trainable and the whole framework model-agnostic.
Description: Figure 2 is a top-down architectural diagram with three labeled panels arranged around a central user utterance "I'm not injured, but my bike is broken." Top-left ("Event Module"): the user utterance is fed as a `query` arrow into a "Long Memory" sub-panel containing a memory bank (icon of stacked papers) on the left and "relevant memory" output on the right ("one month ago, the boy bought a new white bike"); below this, a "Short Memory" sub-panel shows a `time check` step on dialogue cache content ("User: I encountered a traffic accident yesterday. Agent: It's too scary, are you injured?") with a Summarizer that promotes content into Long Memory via a `store` arrow. Top-right ("Persona Module"): the utterance flows via an `extract` arrow into an "Extractor" component, which outputs two persona banks — user persona ("I am a student / I like cycling") and agent persona ("I'm helpful / I excel at mechanics"). Bottom-right ("Response Module"): four feature blocks — Context, Relevant Memory, User Personas, Agent Personas — feed into a "Generator" component, which produces the final agent response ("Is it the white one you just bought? Maybe I can try to fix it."). The figure makes the modular decomposition concrete and shows the data dependencies between modules — most importantly, that the response generator sees four independent streams (current context, retrieved memory, user persona, agent persona) and must integrate them. This is the load-bearing figure because it shows the three-module separation that makes the framework model-agnostic, the timestamp+content split in long memory, and the bidirectional persona modeling that ensures both user AND agent consistency.

## What Experts Overlook

The detail that does most of the work is **the topic-noun overlap term in retrieval** (Equation 1 + Figure 3a). Most production long-term dialogue systems in 2024-2026 use pure semantic retrieval (cosine similarity over MiniLM/BGE/ada embeddings) and accept the ~20pt accuracy gap that Figure 3a measures versus topic-overlap. The argument is usually "embeddings encode noun overlap implicitly, plus more" — LD-Agent's human evaluation shows this is empirically false. On dialogue retrieval specifically, where utterances are short and pronoun-heavy and topical, the explicit lexical signal of noun-set Dice coefficient catches what dense embeddings systematically miss: that "the bike" in the query lexically grounds to "the white bike" in the memory, regardless of how similar the embeddings of the two full sentences are. The combined `s_sem + s_top` score is a strict superset of either alone.

**Why it matters:** This invalidates the "embeddings make BM25 obsolete" hypothesis for the dialogue-memory regime. The right architectural posture is hybrid by default, sparse-only as a fallback only when corpus is huge. For a Flow OS memory layer where each memory file is short (~10-100 lines of structured markdown), the noun-overlap signal will catch references that pure semantic retrieval misses (e.g., "the Dana onboarding plan" — "Dana" is a high-IDF noun that dense embeddings underweight relative to the abstract "onboarding plan" embedding). Adding ~50 lines of noun-extraction + Dice-coefficient code on top of QMD's vector retrieval would likely yield 10-20pt recall improvement on dialogue-style queries — for nearly zero compute cost.

**Example of good use:** Augmenting QMD's hybrid retrieval with a noun-overlap term computed at indexing time (cache `nouns` per file) and combined at query time. The combination function exactly mirrors LD-Agent: `s_overall = λ_t (s_sem + s_top)`, where `λ_t` decays by file mtime. This makes the retriever behave correctly for entity-anchored queries ("what did we decide about Dana") while preserving its semantic strength for thematic queries ("how should I think about consulting offers").

**Example of misapplication:** Replacing semantic retrieval *entirely* with noun-overlap. The paper threshold-gates retrieval on `s_sem > γ=0.5` precisely because pure topic overlap returns false matches (two utterances both mention "bike" but in entirely different contexts). The two signals are complementary, not interchangeable.

A second overlooked detail: **the abstention threshold γ=0.5 is a separate design pattern.** Most retrieval pipelines pass the top-k results to the reader regardless of how bad the matches are. LD-Agent explicitly returns "No relevant memory" when nothing exceeds γ. This converts "wrong context hallucination" into "no context provided" — a much safer failure mode. For Flow OS, this maps to: when QMD's top hit scores below threshold, don't surface ANY memory to the model rather than surfacing a weak one that the model will then over-rely on.

A third overlooked detail: **the agent persona bank.** Most memory systems track the user. LD-Agent argues bidirectional tracking matters for long-term consistency — the agent should be a stable character, not regenerate its identity each session. For a Flow OS agent that represents the user's "second brain", the agent's stable identity (tone, decision-making style, what it does and doesn't do) is itself a piece of memory that needs persistence. The paper's framework gives a concrete way to track this.

## Extracted Prompts

**Prompt explanation:** Event summarization (D.1) — the workhorse encoder that converts raw dialogue into compact summaries for the long-term memory bank. The 20-word constraint is critical for retrieval-friendliness.

```
SYS PROMPT:
You are good at extracting events and summarizing them in brief sentences. You will be shown a conversation between {user name} and {agent name}.

USER PROMPT:
Conversation: {context}.
Based on the Conversation, please summarize the main points of the conversation with brief sentences in English, within 20 words.
SUMMARY:
```

**Prompt explanation:** Persona extraction (D.2) — fed every utterance to extract personality traits or output `NO_TRAIT`. Critical: the few-shot examples explicitly include a `NO_TRAIT` case so the model knows abstention is a valid output.

```
SYS PROMPT:
You excel at extracting user personal traits from their words, a renowned local communication expert.

USER PROMPT:
If no traits can be extracted in the sentence, you should reply NO_TRAIT. Given you some format examples of traits extraction, such as:
1. "No, I have no longer serve in the millitary, I had served up the full term that I signed up for, and now work outside of the millitary."
Extracted Traits: I now work elsewhere. I used to be in the military.
2. "That must a been some kind of endeavor. Its great that people are aware of issues that arise in their homes, otherwise it can be very problematic in the future."
NO_TRAIT
Please extract the personal traits who said this sentence (no more than 20 words):{sentence}
```

**Prompt explanation:** Base response generation (D.3, Prompt 3) — used when no agent traits are tracked. The role-play framing + 30-word response limit are LD-Agent's defaults.

```
SYS PROMPT:
As a communication expert with outstanding communication habits, you embody the role of {agent name} throughout the following dialogues.

USER PROMPT:
<CONTEXT>
Drawing from your recent conversation with {user name}:
{context}
Now, please role-play as {agent name} to continue the dialogue between {agent name} and {user name}.
{user name} just said: {input}
Please respond to {user name}'s statement using the following format (maximum 30 words, must be in English):
RESPONSE:
```

**Prompt explanation:** Full response generation (D.3, Prompt 4) — the production prompt with all four memory streams (context, retrieved memory, user traits, agent traits) wired in. The four-block structure is a clean template for any memory-aware dialogue system.

```
SYS PROMPT:
As a communication expert with outstanding communication habits, you embody the role of {agent name} throughout the following dialogues. Here are some of your distinctive personal traits: {agent traits}.

USER PROMPT:
<CONTEXT>
Drawing from your recent conversation with {user name}:
{context}
<MEMORY>
The memories linked to the ongoing conversation are:
{memories}
<USER TRAITS>
During the conversation process between you and {user name} in the past, you found that the {user name} has the following characteristics:
{user traits}
Now, please role-play as {agent name} to continue the dialogue between {agent name} and {user name}.
{user name} just said: {input}
Please respond to {user name}'s statement using the following format (maximum 30 words, must be in English):
RESPONSE:
```

## Citations

- Xu et al. 2022 — *MSC dataset* (the primary multi-session benchmark; LD-Agent's 5-session, ~50-turn structure)
- Jang et al. 2023 — *Conversation Chronicles (CC)* (the secondary benchmark; different collection method tests cross-domain generalization)
- Zhang et al. 2022 — *HAHT* (the prior SOTA hierarchical transformer that LD-Agent beats by large BL-2 margin)
- Park et al. 2023 — *Generative Agents* (the most-related prior work; LD-Agent argues against its pure zero-shot LLM summarization approach)
- Xu et al. 2022 — *Long time no see (DuLeMon)* (introduces bidirectional persona modeling that LD-Agent adopts)
- Roller et al. 2021 — *BlenderBot* (baseline classical chatbot architecture)
- Zeng et al. 2023 — *ChatGLM* (the offline LLM backbone)
- Wang et al. 2020 — *MiniLM* (the long-term memory encoder)
- Chen et al. 2021 — *DialogSum* (the dialogue-summarization dataset rebuilt for instruction-tuning the event summarizer)
- Wei et al. 2022 — *Chain-of-Thought Prompting* (the zero-shot fallback for persona extraction)
- Wei et al. 2022 — *FLAN/Instruction tuning* (the technique applied to the event summarizer)
- Hu et al. 2022 — *LoRA* (the parameter-efficient tuning method for the persona extractor)
- Lewis et al. 2020 — *BART* (one of the tested base models)
- Papineni et al. 2002, Lin 2004, Banerjee & Lavie 2005 — *BLEU/ROUGE/METEOR* (the automatic eval metrics)
- Hu et al. 2019 — *Ubuntu IRC / GSN* (multiparty dialogue task tested for cross-task transferability)

_Full citations list with DOIs/URLs is in the frontmatter `citations[]` array (17 entries — paper has ~90 refs, digest pulls the load-bearing subset for the memory-architect lens)._

## Related Digests

- [[wu-2024-longmemeval]] — LongMemEval benchmarks LD-Agent as one of 9 memory systems and finds its summary-and-fact compression of values loses recall on detail-heavy questions vs round-level indexing
- [[chhikara-2025-mem0]] — Mem0 generalizes LD-Agent's idea of explicit memory management to a production agent memory layer with graph variants
- [[xu-2021-beyond-goldfish-memory]] — MSC (Beyond Goldfish Memory) is the primary benchmark used here; LD-Agent's framework is designed to extract maximum performance from this benchmark
- [[maharana-2024-locomo]] — LoCoMo is the contemporaneous long-term conversation benchmark that LD-Agent does NOT evaluate against (a gap, given LongMemEval cites both)

## Reviewer Notes

**Overall severity:** Clean

All major claims verified:
- 3 modules (event memory, persona, response) — §3 verbatim ✓
- Long-term + short-term split with β=600s flush trigger — §3.2.1, §3.2.2 ✓
- Retrieval formula `s_overall = λ_t (s_sem + s_top)` with γ=0.5 abstention — Eq 1, Eq 2, §3.2.1 ✓
- `τ = 1e+7` for time decay — §3.2.1 ✓
- MiniLM as encoder — §3.2.1 ✓
- Tuned event summarizer beats zero-shot (rebuilt DialogSum) — §3.2.1 (no ablation table for the summarizer specifically, just architectural claim) — digest accurately reports this as a design choice
- Persona extraction: LoRA, NO_TRAIT output — §3.3 ✓
- Persona extractor table 3: CoT ACC=61.6%, Tuned ACC=77.8% (+16.2pt) — Table 3 ✓
- BL-2 ChatGLM_LDA on CC session 2 tuned: 25.69 — Table 1 ✓
- Topic vs semantic retrieval: "significant gap" on ACC and Recall (Figure 3a, no numerical values given in text but described as "significant"; the ~20pt figure is my reading from the visible bars) — flagged as approximate
- Cross-domain results: Table 4 / Table 8 ✓
- MSC and CC: 5 sessions, ~50 turns each — §4.1 ✓
- Ubuntu IRC for multiparty — §4.1 ✓

Where I had to interpret:
- The ~20pt accuracy / recall gap in Figure 3a — paper does not provide numerical labels in the figure text (it only says "significant gap"). My ~20pt estimate is from visual inspection of the bar chart in the rendered paper image. The exact number could be in the 15-25pt range. Flagged as approximate.
- "The agent persona bank" framed as innovative — Xu 2022 (DuLeMon) introduces bidirectional persona modeling; LD-Agent adopts and operationalizes it. My phrasing emphasizes LD-Agent's contribution but cites Xu 2022 as the source. Defensible.

The application scenario in "How to Apply It" is explicitly framed as a Flow OS hypothetical, not a paper claim. The specific suggestion to add inline timestamps to retrieved memories is presented as an improvement on LD-Agent (motivated by LongMemEval), not as something LD-Agent does.
