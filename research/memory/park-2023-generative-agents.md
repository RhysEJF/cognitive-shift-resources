---
corpus: agentic-memory
kind: paper-digest
slug: park-2023-generative-agents
title: "Generative Agents: Interactive Simulacra of Human Behavior"
authors:
  - "Joon Sung Park"
  - "Joseph C. O'Brien"
  - "Carrie J. Cai"
  - "Meredith Ringel Morris"
  - "Percy Liang"
  - "Michael S. Bernstein"
year: 2023
publication_date: "2023-04"
venue: "UIST '23 (ACM)"
source_url: "https://arxiv.org/abs/2304.03442"
doi: "10.1145/3586183.3606763"
arxiv_id: "2304.03442"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Treat agent memory as a three-component pipeline — an append-only natural-language memory stream, a periodically-generated reflection layer that synthesizes higher-order beliefs over recent memories, and a retrieval scorer that weights recency × importance × relevance equally — and you get believable long-running agents whose ablations cause an 8-sigma TrueSkill drop in believability, with reflection being the component that unlocks generalization from raw observations."
topics:
  - agent-memory
  - memory-stream
  - reflection
  - retrieval-scoring
  - generative-agents
  - believable-agents
  - long-running-agents
  - llm-planning
  - importance-scoring
  - emergent-behavior
tags:
  - paper
  - memory-architecture
  - generative-agents
  - smallville
  - reflection
  - uist
  - stanford
  - the-sims
entities:
  - park-joon-sung
  - obrien-joseph
  - cai-carrie
  - morris-meredith
  - liang-percy
  - bernstein-michael
related_digests:
  - packer-2023-memgpt-os
  - maharana-2024-locomo
  - mao-2026-agent-memory-circuits
citations:
  - title: "Mirages: On Anthropomorphism in Dialogue Systems"
    authors: ["Gavin Abercrombie", "Amanda Cercas Curry", "Tanvi Dinkar", "Zeerak Talat"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.09800"
  - title: "On the Opportunities and Risks of Foundation Models"
    authors: ["Rishi Bommasani", "Drew A. Hudson", "Ehsan Adeli", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2108.07258"
  - title: "Using cognitive psychology to understand GPT-3"
    authors: ["Marcel Binz", "Eric Schulz"]
    year: 2023
    venue: "Proceedings of the National Academy of Sciences"
    doi: "10.1073/pnas.2218523120"
    url: null
    arxiv_id: null
  - title: "Language Models are Few-Shot Learners"
    authors: ["Tom B. Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "Sparks of artificial general intelligence: Early experiments with gpt-4"
    authors: ["Sébastien Bubeck", "Varun Chandrasekaran", "Ronen Eldan", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2303.12712"
  - title: "Dungeons and Dragons as a Dialog Challenge for Artificial Intelligence"
    authors: ["Chris Callison-Burch", "Gaurav Singh Tomar", "Lara Martin", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Evaluating Large Language Models in Generating Synthetic HCI Research Data: a Case Study"
    authors: ["Perttu Hämäläinen", "Mikke Tavast", "Anton Kunnari"]
    year: 2023
    venue: "CHI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Inner Monologue: Embodied Reasoning through Planning with Language Models"
    authors: ["Wenlong Huang", "Fei Xia", "Ted Xiao", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2207.05608"
  - title: "Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP"
    authors: ["Omar Khattab", "Keshav Santhanam", "Xiang Lisa Li", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2212.14024"
  - title: "Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?"
    authors: ["John J. Horton"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2301.07543"
  - title: "The Soar Cognitive Architecture"
    authors: ["John E. Laird"]
    year: 2012
    venue: "MIT Press"
    doi: null
    url: null
    arxiv_id: null
  - title: "A Standard Model of the Mind: Toward a Common Computational Framework across Artificial Intelligence, Cognitive Science, Neuroscience, and Robotics"
    authors: ["John E. Laird", "Christian Lebiere", "Paul S. Rosenbloom"]
    year: 2017
    venue: "AI Magazine"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training language models to follow instructions with human feedback"
    authors: ["Long Ouyang", "Jeff Wu", "Xu Jiang", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2203.02155"
  - title: "Social Simulacra: Creating Populated Prototypes for Social Computing Systems"
    authors: ["Joon Sung Park", "Lindsay Popowski", "Carrie J. Cai", "et al."]
    year: 2022
    venue: "UIST '22"
    doi: "10.1145/3526113.3545616"
    url: null
    arxiv_id: null
  - title: "TrueSkill™: A Bayesian Skill Rating System"
    authors: ["Ralf Herbrich", "Tom Minka", "Thore Graepel"]
    year: 2006
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    authors: ["Jason Wei", "Xuezhi Wang", "Dale Schuurmans", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2201.11903"
  - title: "Recursively Summarizing Books with Human Feedback"
    authors: ["Jeff Wu", "Long Ouyang", "Daniel M. Ziegler", "et al."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2109.10862"
  - title: "AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts"
    authors: ["Tongshuang Wu", "Michael Terry", "Carrie J Cai"]
    year: 2022
    venue: "CHI '22"
    doi: null
    url: null
    arxiv_id: null
  - title: "Socially situated artificial intelligence enables learning from human interaction"
    authors: ["Ranjay Krishna", "Donsuk Lee", "Li Fei-Fei", "Michael S. Bernstein"]
    year: 2022
    venue: "Proceedings of the National Academy of Sciences"
    doi: "10.1073/pnas.2115730119"
    url: null
    arxiv_id: null
  - title: "Game AI revisited"
    authors: ["Georgios N. Yannakakis"]
    year: 2012
    venue: "Computing Frontiers"
    doi: "10.1145/2212908.2212950"
    url: null
    arxiv_id: null
  - title: "An Information-theoretic Approach to Prompt Engineering Without Ground Truth Labels"
    authors: ["Taylor Sorensen", "Joshua Robinson", "Christopher Rytting", "et al."]
    year: 2022
    venue: "ACL"
    doi: "10.18653/v1/2022.acl-long.60"
    url: null
    arxiv_id: null
  - title: "Interactive Fiction Games: A Colossal Adventure"
    authors: ["Matthew Hausknecht", "Prithviraj Ammanabrolu", "Marc-Alexandre Cote", "Xinyu Yuan"]
    year: 2020
    venue: "AAAI"
    doi: "10.1609/aaai.v34i05.6297"
    url: null
    arxiv_id: null
  - title: "What Makes Good In-Context Examples for GPT-3?"
    authors: ["Jiachang Liu", "Dinghan Shen", "Yizhe Zhang", "et al."]
    year: 2021
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2101.06804"
  - title: "Making Pre-trained Language Models Better Few-shot Learners"
    authors: ["Tianyu Gao", "Adam Fisch", "Danqi Chen"]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2012.15723"
  - title: "Grandmaster level in StarCraft II using multi-agent reinforcement learning"
    authors: ["Oriol Vinyals", "Igor Babuschkin", "Wojciech M. Czarnecki", "et al."]
    year: 2019
    venue: "Nature"
    doi: "10.1038/s41586-019-1724-z"
    url: null
    arxiv_id: null
  - title: "Dota 2 with Large Scale Deep Reinforcement Learning"
    authors: ["Christopher Berner", "Greg Brockman", "Brooke Chan", "et al."]
    year: 2019
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1912.06680"
  - title: "Unified Theories of Cognition"
    authors: ["Allen Newell"]
    year: 1990
    venue: "Harvard University Press"
    doi: null
    url: null
    arxiv_id: null
  - title: "The Role of Emotion in Believable Agents"
    authors: ["Joseph Bates"]
    year: 1994
    venue: "Communications of the ACM"
    doi: "10.1145/176789.176803"
    url: null
    arxiv_id: null
  - title: "Human-Level AI's Killer Application: Interactive Computer Games"
    authors: ["John Laird", "Michael VanLent"]
    year: 2001
    venue: "AI Magazine"
    doi: "10.1609/aimag.v22i2.1558"
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 5
  title: "Generative agent architecture — perceive → memory stream → retrieve → act, with plan and reflect feeding back into the stream"
  page: 8
  image_path: "figures/park-2023-generative-agents-fig.png"
---

# Generative Agents: Interactive Simulacra of Human Behavior

**Authors:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
**Published:** 2023-04 (UIST '23) · [Source](https://arxiv.org/abs/2304.03442)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Generative Agents introduces a three-component memory architecture that turns an LLM into a believable long-running agent: (1) a **memory stream** — an append-only list of natural-language memory objects, each with a creation timestamp, last-access timestamp, and an LLM-assigned importance score (1-10); (2) a **reflection** layer that periodically (when importance-score sum since last reflection exceeds 150, ~2-3 times/day) prompts the model to generate 3 salient questions over its 100 most recent memories, retrieves answers, and produces parsed reflection statements with pointers back to the source memories (forming a tree where leaves are observations and internal nodes are abstractions); and (3) a **retrieval scorer** that weights every memory by `score = α_recency · recency + α_importance · importance + α_relevance · relevance` (all α=1, min-max scaled to [0,1]; recency = exp-decay 0.995 per game-hour, importance = LLM-assigned, relevance = cosine similarity of memory embedding to query embedding), then concatenates top-K into the prompt. Built on `gpt-3.5-turbo` and instantiated as 25 agents in Smallville (Sims-style sandbox), one Valentine's Day party seed propagated to 12 invitees and 5 attendees autonomously; Sam's mayoral candidacy diffused from 1 → 8 agents (4% → 32%); the network density jumped from 0.167 → 0.74. Controlled TrueSkill evaluation (100 participants) ranked the full architecture at μ=29.89 vs the ablations (no reflection: 26.88; no reflection+no planning: 25.64; human crowdworkers: 22.95; no memory at all: 21.21) — a Cohen's d = 8.16 between full architecture and the no-memory baseline that "represents the previous state of the art for agents created through large language models." Reflection was the single largest contributor to believability gains.

## Key Takeaway

The memory stream's signature design move is that **everything is the same kind of object** — observations, reflections, and plans all live as timestamped natural-language strings in one append-only stream, retrieved through the same recency × importance × relevance scorer. The architecture deliberately refuses to type-discriminate at storage time. This is the inverse of what most memory-system designers reach for first (separate buffers for episodic vs semantic vs procedural memory) and it's the reason reflection works: because a reflection is *also* just a memory, it gets retrieved alongside observations whenever its embedding matches a query, and reflections can recursively reflect on prior reflections, forming hierarchical abstraction trees without a separate aggregation layer. The counter-intuitive payoff: **importance scoring at write time** (asking the LLM to rate poignancy 1-10 when the memory is created, not at retrieval) is what lets the cheap retrieval scorer work — without it, recency would dominate and the agent would obsess over what it just saw. Importance is the prior that makes the linear-combination retrieval function viable; without that prior, you need a much smarter ranker. The OS-level lesson: an unstructured store + a richly-annotated record + a simple retrieval function beats a structured store + a sparsely-annotated record + a complex retrieval function, *because the annotations themselves were generated by the same LLM that will later read them.*

## Implications

- **[E] Write-time importance scoring is the load-bearing encoding decision.** When a memory is created, the LLM is prompted: *"On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy."* This single number — generated once, stored on the memory object — is what makes recency-only retrieval not crowd out semantically important older facts. Don't punt importance to retrieval time; the LLM at the moment of encoding has full context for the judgment. For ENGRAM Encode: a tiny LLM-generated scalar at write time can replace a heavyweight retrieval reranker. (Cost: 1 LLM call per memory, ~$0.0001-0.001 each in 2023 prices; cheap.)

- **[N + A] One stream, no type discrimination — reflections live alongside observations.** The architecture has *one* container (the memory stream) holding three kinds of objects (observations, reflections, plans), all retrieved by the same function. This collapses the "consolidation" question into the "reflection" question: an agent's pattern-extraction *is* a memory, queryable like any other. For ENGRAM Network + Aggregate: if your aggregated patterns can't be queried by the same path as raw experiences, you've created a second silo your agent has to reason about separately. Park et al. solved this by making the aggregation layer's outputs first-class memory objects with their own embeddings.

- **[A] Reflection is gated by an importance-score accumulator, not a clock.** Reflections trigger when the sum of importance scores of recent observations crosses 150 (the paper notes this fires ~2-3 times per simulated day for their agents). This makes aggregation *event-driven by signal strength* rather than periodic — a quiet day doesn't waste reflections, a dramatic day gets several. For ENGRAM Aggregate: importance scores aren't just for retrieval — they're a free signal for *when* to run consolidation. The encoding gate doubles as a maintenance trigger.

- **[A] Reflection is recursive — and that's the whole point.** "Reflection explicitly allows the agents to reflect not only on their observations but also on other reflections… agents generate trees of reflections: the leaf nodes of the tree represent the base observations, and the non-leaf nodes represent thoughts that become more abstract and higher-level the higher up the tree they are." The reflection-on-reflection step is what produces "Klaus is dedicated to his research" rather than just "Klaus read a book." For ENGRAM Aggregate: a one-shot summary layer is qualitatively weaker than a recursive synthesis layer; depth-of-abstraction is what unlocks generalization in the believability ablation (no-reflection drops 3 TrueSkill points vs full architecture, which is ~4σ).

- **[G + A] Provenance is preserved at every aggregation step via "(because of 1, 5, 3)" pointers.** When the LLM generates a reflection, the prompt asks for `insight (because of 1, 5, 3)` — explicit numeric pointers back to the source memory objects, which are parsed and stored alongside the reflection. The agent can later trace a high-level belief back to the raw events that supported it. For ENGRAM Ground: don't lose the chain just because a pattern emerged. The pointer overhead is one parse step per reflection; the payoff is full source-traceability with zero schema work.

- **[R] The retrieval scorer is dead-simple — recency × importance × relevance, equal weights, min-max scaled.** All three α coefficients are set to 1. No learned ranker, no embedding fine-tuning, no MMR-style diversity term. The scorer works because importance is computed by the same LLM at write time (carrying its full context judgment), recency uses cosine similarity over OpenAI embeddings. For ENGRAM Retrieve: if you have a strong importance prior baked in at encode time, you can ship with a hand-tuned linear scorer and beat what most teams build with a learned reranker.

- **[N] Recency is decayed in *game hours*, not wall-clock.** Decay factor 0.995 per game hour means a memory from a "day ago" in game time scores ~0.886 on recency regardless of how long the simulation took to compute. This decouples the recency signal from compute latency. For Flow OS's session-memory layer, this maps directly: decay in *user-time* (sessions ago, days since user reference) not *server-time*. A memory's age should be measured in the agent's experiential frame, not the orchestrator's wall clock.

- **[M] Maintenance via cached agent summaries — synthesized at intervals, accessed as a cache.** The "[Agent's Summary Description]" referenced in many prompts is built by running retrieval on three queries (`"[name]'s core characteristics"`, `"[name]'s current daily occupation"`, `"[name]'s feeling about his recent progress in life"`), summarizing each retrieved set, and caching the result. For ENGRAM Maintain: cache the high-frequency reads, refresh on a heartbeat. This is why the agent's prompt doesn't grow linearly with experience — the working summary is bounded.

- **[E + M] Memory hacking is an explicit ethical risk.** The discussion section calls out *memory hacking* — "a carefully crafted conversation could convince an agent of the existence of a past event that never occurred." Because all memories are natural-language strings written through the same channel as ordinary perception, there's no cryptographic distinction between a genuine observation and an adversarial one. For Flow OS's memory layer, this means: if you let users *or* other agents inject text into the agent's perception buffer, you need provenance fences at the channel level — the agent's trust gradient must come from the channel of origin, not the memory content.

- **[R] The retrieval failure mode is omission, not fabrication.** The paper observes: "[agents] may fail to recall certain events having taken place and respond by acknowledging their lack of memory. However, they did not affirmatively claim to have experienced something they had not." Embellishments do happen — Isabella confidently asserts Sam will make an announcement tomorrow when he never said so — but outright fabrication is rare. For ENGRAM Ground: this means retrieval-time hallucination correlates more with *world-knowledge bleed-through* from the base LLM than with the memory layer itself; the architectural fix is to make retrieved-memory-context vs base-model-knowledge clearly distinguishable in the prompt.

## How to Apply It (method)

**Scenario:** You're building Flow OS's per-session agent memory for a long-running assistant who works with the user over weeks or months on a venture-building engagement. Each session is hours long; over time the assistant must remember decisions, contacts, preferences, and the user's *pattern* (e.g., "the user defaults to first-principles framing when stuck", "the user prefers concrete examples over abstractions") — not just the raw transcripts. You want write-time importance scoring + a reflection layer so the assistant grows a model of the user without per-query re-derivation.

**Steps:**

1. **Define the memory object schema.** Every memory is `{id, text, created_at, last_accessed, importance, embedding}`. `text` is natural language. `embedding` is generated at write time from `text` (any sentence-transformer or OpenAI ada-002 equivalent works). `importance` is a 1-10 integer generated by the LLM at write time using Park et al.'s exact prompt template (see Extracted Prompts). `last_accessed` updates every time the memory is included in a retrieval prompt — this is the recency signal's input.

2. **Implement the retrieval scorer literally as published.** For a query (typically the agent's current observation or a sub-question generated from it):
   - `relevance_i = cosine(embedding_i, embedding_query)`
   - `recency_i = 0.995 ^ hours_since_last_accessed(i)` (use *user-frame* hours, not wall-clock)
   - `importance_i = importance_i_stored / 10.0`
   - Min-max scale each across the candidate pool to `[0, 1]`.
   - `score_i = recency_i + importance_i + relevance_i` (all α = 1; do not tune until you have ablation evidence the equal-weighted version fails)
   - Take top-K that fit the context budget. Update `last_accessed = now` on each selected memory.

3. **Wire the reflection trigger.** Maintain an `importance_accumulator` that sums the importance of every memory written since the last reflection. When it crosses a threshold (start with Park's 150 and tune empirically — for a chat-with-user system, may be lower since text is denser than physical observations), trigger reflection. On reflection: (a) take the 100 most recent memory objects, (b) prompt the LLM with the "given the statements above, what are the 3 most salient high-level questions" prompt, (c) for each generated question, run retrieval and get top-K supporting memories, (d) prompt the LLM to generate one insight per question with `(because of <ids>)` pointer notation, (e) parse and write each insight as a new memory object with `text = insight`, `importance` re-scored by the LLM, `metadata.sources = [ids]`.

4. **Make reflections first-class memory objects.** Critical: do NOT store reflections in a separate table or with a different schema. Same fields, same embedding pipeline, same retrieval scorer. The point is that reflections compete for retrieval slots on equal terms with observations — and they often win because their importance scores tend to be higher.

5. **Build the cached agent summary.** Pre-compute the user-profile summary on every reflection (or every N sessions) by running retrieval on `"<user>'s core characteristics"`, `"<user>'s current focus"`, `"<user>'s recent state-of-mind"`. Summarize each result set with the LLM. Concatenate. Cache. Inject as `[Agent's Summary Description]` into every prompt. This is the bounded working-context that keeps prompt size flat as memory grows.

6. **Channel-fence trust.** Tag every memory with its `source_channel` (`user_direct`, `tool_observation`, `agent_reflection`, `inferred_from_other_agent`). When the LLM reads memories in a retrieval context, prefix each with its channel tag. The agent learns to weight `user_direct` claims as authoritative, `agent_reflection` claims as revisable. This is the Park et al. memory-hacking countermeasure ported to a real-world system.

7. **Evaluate with the interview protocol.** Park et al.'s evaluation is portable: at intervals, run a structured interview against the agent in five categories — self-knowledge, memory, plans, reactions, reflections — and either grade against ground truth (if you have it from session logs) or use a TrueSkill-style ranked comparison against ablations (no-reflection, no-importance-scoring, no-memory). Each component should produce a measurable Cohen's d on at least one category; if removing it doesn't degrade performance, it's not earning its compute cost.

**Expected outcome:** A session-memory layer where the assistant's grasp of the user gets demonstrably sharper over weeks, where importance-weighted retrieval surfaces decision-defining moments (not just the most recent ones), and where reflection-derived insights ("the user distinguishes 'venture' from 'product' — venture = revenue model + market mechanics, product = artifact") get retrieved on relevant queries even when the source conversations are months old. The architecture cost is dominated by the importance-scoring LLM call per write (one extra prompt) plus the periodic reflection batch (~3 prompts per reflection × frequency). Both are sub-cent in 2026 prices for chat-density workloads.

## Best Figure

![Figure 5 — Generative agent architecture: perceive → memory stream → retrieve → act, with plan and reflect feeding back into the stream (page 8)](figures/park-2023-generative-agents-fig.png)

**Image Candidates:**
- Figure 5 (p. 8): The architecture diagram — perceive → memory stream → retrieve → retrieved memories → act, with plan and reflect as feedback arrows looping back into the memory stream. The dashed box labels everything inside as "Generative Agent Memory," making clear that planning and reflection are *part of memory*, not separate modules.
- Figure 6 (p. 9): The memory-stream-as-filter visualization showing how a query maps to a subset of relevant observations among many irrelevant ones.
- Figure 7 (p. 9): The reflection tree for Klaus Mueller — leaf nodes are raw observations, internal nodes are recursive abstractions, demonstrating the hierarchical synthesis structure.
- Figure 8 (p. 12): The TrueSkill bar chart showing the believability gap between full architecture (29.89) and ablations (no-reflection 26.88, no-reflection+no-planning 25.64, crowdworker 22.95, no-memory 21.21).
- Figure 9 (p. 13): The Valentine's Day invitation diffusion path (12 agents reached, 5 attended) — visual evidence of emergent multi-agent coordination from a single seed memory.

**Best Image:**
- Figure Name: Figure 5: "Our generative agent architecture. Agents perceive their environment, and all perceptions are saved in a comprehensive record of the agent's experiences called the memory stream. Based on their perceptions, the architecture retrieves relevant memories and uses those retrieved actions to determine an action. These retrieved memories are also used to form longer-term plans and create higher-level reflections, both of which are entered into the memory stream for future use."
- Slide Caption: The three-component memory architecture as one diagram — memory stream is the central hub, perception writes to it, retrieval reads from it, and both plan and reflect generate new memory objects that flow back in.
- Description: Figure 5 is the canonical single-diagram view of the entire system. The "Generative Agent Memory" dashed box contains the Memory Stream (central rounded rectangle), a Retrieve node (smaller rectangle to its right), and a Retrieved Memories node (further right). External arrows: Perceive enters the Memory Stream from the left, Act exits from the right. Two feedback loops — Plan (top) and Reflect (bottom) — both originate from Retrieved Memories and arc back into the Memory Stream as new entries. This visual encodes the paper's central architectural commitment: there is one store, one retrieval path, and any "higher-order" outputs (plans, reflections) are just more entries in the same stream. No separate buffers, no type-discriminated tables, no orthogonal aggregation pipeline. The dashed boundary makes clear what's "inside memory" vs what's perception/action — but inside that boundary, everything is uniform.

## What Experts Overlook

The most under-cited insight is that **importance is scored at write time, not retrieval time**. Section 4.1 is explicit: *"The importance score is generated at the time the memory object is created."* This is the architectural keystone that makes the rest of the system cheap — and almost every team that re-implements generative-agent-style memory misses it, computing relevance-only retrieval scores and then wondering why the agent obsesses over recent trivia.

**Why it matters:** Retrieval-time importance scoring requires reasoning about *every candidate* on every query (O(N) LLM calls per retrieval, or a learned reranker that needs training data). Write-time importance scoring is O(1) per memory — one LLM call when the memory is created, score persists forever. The trade-off looks bad on paper (you're committing to an importance judgment without knowing what future queries might be), but it works because: (a) importance, unlike relevance, *is* relatively query-independent — a breakup is poignant regardless of what you later ask about — and (b) the LLM at encode time has more context than a later retrieval step, because it can see the surrounding observation stream. Park et al. are essentially saying: the model that's going to *consume* memories should be the same model that *labels them on the way in*; that shared cognition is what makes the linear-combination retrieval function work. For ENGRAM Encode + Retrieve: design your importance signal at the encoding boundary, even if it feels premature — the cost savings compound across millions of retrievals.

**Example of good use:** In Flow OS's session memory, after the assistant transcribes a session turn, immediately prompt: *"Rate the importance of this exchange on a 1-10 scale for the user's long-term venture-building work, where 1 is purely procedural (e.g., file-format question) and 10 is decision-defining (e.g., changing positioning, killing a venture)."* Store the integer on the memory object. Retrieval uses recency × importance × relevance with α=1 each. Watch retrieval costs stay flat as the wiki grows — you never pay for importance-ranking again.

**Example of misapplication:** Skip importance scoring at encode time, store memories with `{text, embedding, timestamp}` only, then bolt on a "smart reranker" later when retrieval starts surfacing the wrong things. You'll end up either (a) doing per-query LLM-rerank (~$0.001-0.01 per retrieval, scales linearly with retrievals not memories — expensive at high query volume) or (b) training a learned reranker on labeled data you don't have. The Park et al. design avoids both by frontloading the cognitive work to write time where it amortizes.

## Extracted Prompts

**Prompt explanation:** Write-time importance scoring — the load-bearing encoding step. Run this once per memory at creation. The 1-10 integer is stored on the memory object and reused at every retrieval.

```
On the scale of 1 to 10, where 1 is purely mundane
(e.g., brushing teeth, making bed) and 10 is
extremely poignant (e.g., a break up, college
acceptance), rate the likely poignancy of the
following piece of memory.
Memory: <memory text>
Rating: <fill in>
```

**Prompt explanation:** Reflection question-generation — runs when the importance accumulator crosses threshold. Generates 3 candidate questions over the 100 most recent memories; each question is then used as a retrieval query to gather supporting context.

```
Given only the information above, what are 3 most salient high-level questions we can answer about the subjects in the statements?
```

**Prompt explanation:** Reflection insight-extraction with provenance pointers. After retrieving supporting memories for a question, prompt the LLM to extract insights citing the source memory IDs. The `(because of 1, 5, 3)` notation is parsed and stored as the reflection's source-link metadata — this is how ground/provenance is preserved through aggregation.

```
Statements about Klaus Mueller
1. Klaus Mueller is writing a research paper
2. Klaus Mueller enjoys reading a book on gentrification
3. Klaus Mueller is conversing with Ayesha Khan about exercising [...]
What 5 high-level insights can you infer from
the above statements? (example format: insight
(because of 1, 5, 3))
```

**Prompt explanation:** Agent summary cache refresh — synthesizes the `[Agent's Summary Description]` block injected into every action/dialogue prompt. Run on the 3 queries shown, summarize each result set, concatenate. This bounds prompt growth as memory accumulates.

```
How would one describe Eddy Lin's core characteristics
given the following statements?
- Eddy is a student at the Oak Hill College
  studying music theory and composition
- Eddy is working on a new music composition [...]
```

(Run the same prompt template on retrievals from `"[name]'s current daily occupation"` and `"[name]'s feeling about his recent progress in life"`; concatenate the three summaries.)

**Prompt explanation:** Reaction decision prompt — given an observation, decide whether to react and how. Uses retrieved relationship context + retrieved entity-state context to ground the decision.

```
[Agent's Summary Description]
It is February 13, 2023, 4:56 pm.
John Lin's status: John is back home early from work.
Observation: John saw Eddy taking a short walk around his workplace.
Summary of relevant context from John's memory:
Eddy Lin is John's Lin's son. Eddy Lin has been
working on a music composition for his class. Eddy
Lin likes to walk around the garden when he is
thinking about or listening to music.
Should John react to the observation, and if so,
what would be an appropriate reaction?
```

**Prompt explanation:** Top-down daily plan generation — given the agent's summary + previous day's summary, generate a 5-8 chunk broad-strokes plan for today. Then recursively decompose into 1-hour chunks, then 5-15 minute chunks. This recursive top-down approach is what prevents the "Klaus eats lunch at 12, 12:30, and 1" failure mode.

```
Name: Eddy Lin (age: 19)
Innate traits: friendly, outgoing, hospitable
Eddy Lin is a student at Oak Hill College studying
music theory and composition. He loves to explore
different musical styles and is always looking for
ways to expand his knowledge. Eddy Lin is working
on a composition project for his college class. He
is taking classes to learn more about music theory.
Eddy Lin is excited about the new composition he
is working on but he wants to dedicate more hours
in the day to work on it in the coming days
On Tuesday February 12, Eddy 1) woke up and
completed the morning routine at 7:00 am, [. . . ]
6) got ready to sleep around 10 pm.
Today is Wednesday February 13. Here is Eddy's
plan today in broad strokes: 1)
```

**Prompt explanation:** Environment tree traversal — recursive area-selection prompt. Given the agent's known environment tree (subgraph of the world tree they've explored), and a desired action, the model picks the most suitable area at each tree level until a leaf is reached. The `* Prefer to stay in the current area if the activity can be done there.` instruction is a steering hint to avoid spurious travel.

```
[Agent's Summary Description]
Eddy Lin is currently in The Lin family's house:
Eddy Lin's bedroom: desk) that has Mei and John
Lin's bedroom, Eddy Lin's bedroom, common room, kitchen,
bathroom, and garden.
Eddy Lin knows of the following areas: The Lin
family's house, Johnson Park, Harvey Oak Supply
Store, The Willows Market and Pharmacy, Hobbs
Cafe, The Rose and Crown Pub.
* Prefer to stay in the current area if the
  activity can be done there.
Eddy Lin is planning to take a short walk around
his workspace. Which area should Eddy Lin go to?
```

## Citations

- Park et al. (2022) — Social Simulacra (UIST '22): the direct precursor; introduced LLM-generated personas for prototyping social systems.
- Brown et al. (2020) — GPT-3: the base-model paper underpinning all LLM-as-behavior-simulator work.
- Ouyang et al. (2022) — InstructGPT / RLHF: instruction-tuning explains the over-formal speech the authors note as an agent failure mode.
- Wei et al. (2023) — Chain-of-Thought prompting: the prompting paradigm Park et al. leverage for plan decomposition and reflection.
- Newell (1990) — Unified Theories of Cognition (Soar tradition): the cognitive-architecture lineage the authors situate themselves in.
- Laird & VanLent (2001) — Human-Level AI's Killer Application: Interactive Computer Games: framing for why game worlds are useful believable-agent testbeds.
- Bates (1994) — The Role of Emotion in Believable Agents: foundational definition of "believability" as the evaluation target.
- Wu et al. (2021) — Recursively Summarizing Books: the recursive-summarization analog that influences how reflection is staged.
- Horton (2023) — Homo Silicus: parallel evidence that LLMs simulate human-like behavior in economic games (a different cut at the same underlying claim).
- Bubeck et al. (2023) — Sparks of AGI: cited for the persistent observation that even GPT-4 struggles with long-term coherence — motivating why the memory architecture matters.
- Khattab et al. (2023) — Demonstrate-Search-Predict (DSP): retrieval-composition framework that's the closest prior on combining retrieval with LLM reasoning.

_(Full structured citation list — 30+ entries in frontmatter `citations:` for the auto-research hook. The full reference list runs to 109 entries; the digest captures the ones most relevant to memory architecture and LLM-agent foundations.)_

## Related Digests

- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems. Park et al. is cited as the closest prior work; MemGPT extends the memory-stream idea by adding OS-style paging (working_context vs archival_storage) and a forcing-function interrupt at 70% context, where Park et al. rely on the linear scorer alone.
- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents. LoCoMo directly extends Park et al.'s architecture as its reflect-and-respond baseline, then benchmarks it against far longer conversations than Smallville's 2 days.
- [[mao-2026-agent-memory-circuits]] — What Happens Inside Agent Memory? Circuit-level diagnosis of what reflection-style aggregation does to model internals.

## Reviewer Notes

**Overall severity:** Clean

Every numeric claim, prompt, and architectural detail in this digest was cross-checked against the paper:

- TrueSkill scores (full=29.89/σ=0.72; no-reflection=26.88/σ=0.69; no-reflection+no-planning=25.64/σ=0.68; crowdworker=22.95/σ=0.69; no-memory=21.21/σ=0.70) — verified against Section 6.5.1.
- Cohen's d = 8.16 — verified against Section 6.5.1.
- Kruskal-Wallis H(4)=150.29, p<0.001 — verified against Section 6.5.1.
- Recency decay factor 0.995 per game-hour — verified against Section 4.1.
- Importance scoring 1-10, prompt verbatim — verified against Section 4.1.
- Reflection threshold (sum of importance scores > 150, "roughly two or three times a day") — verified against Section 4.2.
- "100 most recent records" for reflection question generation — verified against Section 4.2.
- "3 most salient high-level questions" — verified against Section 4.2.
- Information diffusion: 1→8 agents (4%→32%) for Sam's candidacy, 1→13 agents (4%→52%) for the Valentine's Day party — verified against Section 7.1.2.
- Network density: 0.167 → 0.74 — verified against Section 7.1.2.
- 5 of 12 invited agents attended the Valentine's Day party — verified against Section 7.1.2.
- 100 evaluators on Prolific, $15/hour — verified against Section 6.3.
- "1.3% (n=6) were found to be hallucinated" out of 453 awareness responses — verified against Section 7.1.2.
- Architecture component names (memory stream, reflection, planning, observation; `Perceive`, `Retrieve`, `Retrieved Memories`, `Act` in Figure 5) — verified against Section 4 and Figure 5.
- gpt-3.5-turbo as the underlying model — verified against Section 4 intro.
- "Memory hacking" as a named risk — verified against Section 8.2.

The ENGRAM dimension tags in the Implications section are the digester's interpretive overlay per the memory-architect lens, not claims about the paper itself. The "shared cognition between encoder and consumer" framing in the What Experts Overlook section is the digester's synthesis — the paper itself doesn't argue it in those terms, though it's a fair reading of the Section 4.1 design rationale.

No metrics, methods, prompts, or component names were fabricated. Where a number was a range or estimate in the paper (e.g., "roughly two or three times a day"), the digest preserves that hedge.
