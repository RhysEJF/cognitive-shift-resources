---
corpus: agentic-memory
kind: paper-digest
slug: guo-2023-working-memory
title: "Empowering Working Memory for Large Language Model Agents"
authors:
  - "Jing Guo"
  - "Nan Li"
  - "Jianchuan Qi"
  - "Hang Yang"
  - "Ruiqiao Li"
  - "Yuzhen Feng"
  - "Si Zhang"
  - "Ming Xu"
year: 2023
publication_date: "2023-12"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2312.17259"
doi: null
arxiv_id: "2312.17259"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Guo et al. translate Baddeley's working-memory model (Central Executive + Phonological Loop + Visuospatial Sketchpad + Episodic Buffer) into an LLM-agent architecture by adding a centralized Working Memory Hub that persistently stores all I/O, and an Episodic Buffer that retrieves complete past episodes — turning what used to be isolated, token-window-bounded conversations into a continuous memory substrate that can be shared across agents in a multi-agent system."
topics:
  - working-memory
  - llm-agents
  - memory-architecture
  - multi-agent-systems
  - episodic-buffer
  - cognitive-psychology
tags:
  - paper
  - memory
  - agent-architecture
  - baddeley
  - position-paper
entities:
  - guo-jing
  - li-nan
  - xu-ming
  - baddeley-alan
  - tsinghua-university
related_digests:
  - ma-2026-nemori-distillation
  - du-2025-rethinking-memory
  - wang-2026-memmachine
  - wang-2025-mirix
  - wu-2025-human-ai-memory-survey
  - zhang-2025-llm-memory-survey
citations:
  - title: "Working memory: looking back and looking forward"
    authors: ["Alan Baddeley"]
    year: 2003
    venue: "Nature Reviews Neuroscience"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language Models are Few-Shot Learners"
    authors: ["Tom B. Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2005.14165"
    url: "https://arxiv.org/abs/2005.14165"
    arxiv_id: "2005.14165"
  - title: "How can Transformers and large language models like ChatGPT help LCA practitioners?"
    authors: ["S. Cornago", "S. Ramakrishna", "J. S. C. Low"]
    year: 2023
    venue: "Resources, Conservation and Recycling"
    doi: "10.1016/j.resconrec.2023.107062"
    url: null
    arxiv_id: null
  - title: "Neural Turing Machines"
    authors: ["Alex Graves", "Greg Wayne", "Ivo Danihelka"]
    year: 2014
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.1410.5401"
    url: "https://arxiv.org/abs/1410.5401"
    arxiv_id: "1410.5401"
  - title: "Risks and Benefits of Large Language Models for the Environment"
    authors: ["Matthias C. Rillig", "Marlene Ågerstrand", "Mohan Bi", "et al."]
    year: 2023
    venue: "Environmental Science & Technology"
    doi: "10.1021/acs.est.3c01106"
    url: null
    arxiv_id: null
  - title: "End-To-End Memory Networks"
    authors: ["Sainbayar Sukhbaatar", "Arthur Szlam", "Jason Weston", "et al."]
    year: 2015
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.1503.08895"
    url: "https://arxiv.org/abs/1503.08895"
    arxiv_id: "1503.08895"
  - title: "Adapting LLM Agents Through Communication"
    authors: ["Kuan Wang", "Yadong Lu", "Michael Santacroce", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2310.01444"
    url: "https://arxiv.org/abs/2310.01444"
    arxiv_id: "2310.01444"
  - title: "Recursively Summarizing Enables Long-Term Dialogue Memory in Large Language Models"
    authors: ["Qingyue Wang", "Liang Ding", "Yanan Cao", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2308.15022"
    url: "https://arxiv.org/abs/2308.15022"
    arxiv_id: "2308.15022"
  - title: "Augmenting Language Models with Long-Term Memory"
    authors: ["Weizhi Wang", "Li Dong", "Hao Cheng", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2306.07174"
    url: "https://arxiv.org/abs/2306.07174"
    arxiv_id: "2306.07174"
  - title: "Memory Networks"
    authors: ["Jason Weston", "Sumit Chopra", "Antoine Bordes"]
    year: 2015
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.1410.3916"
    url: "https://arxiv.org/abs/1410.3916"
    arxiv_id: "1410.3916"
  - title: "Memory-Augmented LLM Personalization with Short- and Long-Term Memory Coordination"
    authors: ["Kai Zhang", "Fubang Zhao", "Yangyang Kang", "Xiaozhong Liu"]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2309.11696"
    url: "https://arxiv.org/abs/2309.11696"
    arxiv_id: "2309.11696"
  - title: "RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text"
    authors: ["Wangchunshu Zhou", "Yuchen Eleanor Jiang", "Peng Cui", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2305.13304"
    url: "https://arxiv.org/abs/2305.13304"
    arxiv_id: "2305.13304"
  - title: "PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training"
    authors: ["Dawei Zhu", "Nan Yang", "Liang Wang", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: "10.48550/arXiv.2309.10400"
    url: "https://arxiv.org/abs/2309.10400"
    arxiv_id: "2309.10400"
hallucination_severity: "Clean"
best_figure:
  number: 4
  title: "Innovative working memory model"
  page: 6
  image_path: "figures/guo-2023-working-memory-fig.png"
---

# Empowering Working Memory for Large Language Model Agents

**Authors:** Jing Guo, Nan Li, Jianchuan Qi, Hang Yang, Ruiqiao Li, Yuzhen Feng, Si Zhang, Ming Xu (Tsinghua University)
**Published:** 2023-12 · [Source](https://arxiv.org/abs/2312.17259)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

This is a position/blueprint paper from Tsinghua (Dec 2023) — no experiments, no benchmarks — arguing that today's LLM agents fail because they translate a textbook short-term-memory cache into an architecture, while ignoring Baddeley's full multi-component working-memory model from cognitive psychology (Central Executive, Phonological Loop, Visuospatial Sketchpad, and crucially the Episodic Buffer added in 2000). The authors diagnose two concrete failure modes in current LLM-agent designs: (1) a hard token-window ceiling on the Interaction History Window that drops old context, and (2) "domain isolation" where each new session is a fresh episodic island with no link to prior sessions — fatal in multi-agent systems where collective progress requires shared experience. Their proposed remedy is an architecture diagram (Figure 4) adding a centralized **Working Memory Hub** that persistently stores all I/O across components, plus an **Episodic Buffer** that retrieves complete past episodes when relevant. Implementation pathways suggested: third-party databases (Postgres/Elasticsearch for raw text, Pinecone for vectors, Xata/PaaS for both), API-driven access, and five concrete access-control strategies for multi-agent settings (role-based, task-based, autonomous, collaboration-scenario, and a dedicated Memory Management Agent). They explicitly recommend combining SQL, full-text, and semantic search in layered retrieval — SQL for chronological slicing, full-text for exact strings, semantic for intent. The paper ends without metrics or a runnable implementation, leaving the blueprint as conceptual scaffolding rather than a tested system.

## Key Takeaway

Guo et al. translate Baddeley's working-memory model (Central Executive + Phonological Loop + Visuospatial Sketchpad + Episodic Buffer) into an LLM-agent architecture by adding a centralized Working Memory Hub that persistently stores all I/O, and an Episodic Buffer that retrieves complete past episodes — turning what used to be isolated, token-window-bounded conversations into a continuous memory substrate that can be shared across agents in a multi-agent system. The real load-bearing idea is **persistent storage of every interaction at a layer below the LLM's context window**, with separate retrieval components (summarizing window, episode buffer) drawing from that hub. This decouples "what the LLM sees right now" from "what the agent has ever seen," and re-introduces Baddeley's distinction between transient buffers and the consolidation pathway that hands memory back and forth with long-term storage.

## Implications

- **Stop building memory at the prompt layer — build it at the substrate layer**: The paper's core architectural move is to put the memory store *underneath* the LLM, not inside the prompt. If you're stuffing summaries into a system prompt today, you've conflated "context window" with "memory" — the right separation is a Working Memory Hub that owns all I/O, with the LLM as a Central Processor that pulls slices on demand.
- **Treat the Episodic Buffer as a first-class component, not a RAG side-channel**: Most retrieval-augmented agents today merge episodes into a flat vector index. Baddeley's model says episodes should retain *coherent structure* — a whole conversation as a unit, not chunks. Build a retrieval layer that returns complete episodes when an episode is what's relevant.
- **Layer SQL + full-text + semantic search rather than picking one**: The paper explicitly recommends combining all three — SQL for "what did we discuss last Tuesday," full-text for exact-string queries, semantic for "everything related to climate change." If your agent only does vector search, you're missing chronological and exact-match retrieval modes that LLMs are bad at synthesizing on their own.
- **Pick a memory-access strategy that matches the collaboration pattern**: The five strategies (role-based, task-based, autonomous, collaboration-scenario, Memory Management Agent) are not interchangeable. A supervisor agent needs broad read access; a single-task worker needs scoped access for both efficiency and security. Default to role-based as your spine and add a Memory Management Agent when planning agents start trawling history.
- **Plan for memory security from day one in MAS**: The paper flags — but doesn't solve — that opening memory sharing across agents creates an attack surface. Authentication, authorization, and per-segment access control should be a Memory Hub design constraint, not an afterthought.
- **Use a PaaS like Xata when you need both raw text and vectors in one store**: The paper specifically names Xata as the way to avoid the Postgres-vs-Pinecone split. The architectural insight is that splitting storage by retrieval method (text vs. vector) forces you to maintain two consistency models; unified storage simplifies that.
- **This paper is a blueprint, not a result — treat it accordingly**: No benchmarks, no implementation, no comparisons against existing memory systems (MemGPT, MemoryBank, Voyager, etc., which existed when this was written and are not cited). Use the architecture as a vocabulary and decomposition framework, not as evidence that this design beats alternatives.
- **The "domain isolation" diagnosis is sharper than the proposed fix**: The cleanest contribution is the explicit naming of "domain isolation" — every new session is a fresh island. That framing is useful even if you don't adopt the Working Memory Hub diagram. Any cross-session memory system should explicitly answer: how does episode N get linked to episode N-1?

## How to Apply It (method)

**Scenario:** You're building a multi-agent customer-success system for a SaaS company. Agent A handles tier-1 chat support, Agent B writes follow-up emails, Agent C maintains a per-customer health summary, and a Supervisor agent reviews escalations. Today each agent's context is its own session — Agent B has no memory of what Agent A said, and the Supervisor can't tell what Agent C used to think two weeks ago. You want to apply this paper's blueprint to give your agents persistent, shared episodic memory.

**Steps:**

1. **Stand up the Working Memory Hub as a separate service**: Pick one storage backend that handles both raw text and vectors. Xata or Postgres-with-pgvector are the canonical choices the paper hints at. This service is *not* the LLM and *not* an agent — it's a passive data layer that every agent reads from and writes to via API.

2. **Log every input/output at the Hub, not just summaries**: For each turn of each agent — user message in, agent response out, tool call, tool response — write a record to the Hub with: timestamp, agent_id, session_id (= "episode" boundary), customer_id, raw text, embedding, and a structured tag (e.g. `kind: user_message`, `kind: agent_response`, `kind: tool_call`). The cardinal rule: nothing transient. If the LLM saw it, the Hub stores it.

3. **Build the Interaction History Window as a view, not a store**: Each agent's "short-term memory" is now a query against the Hub — e.g. "give me the last N turns of session_id X." It can be a rolling window, an abstractive summary, or pertinent extracts, but it's *derived* from the Hub. Don't let agents accumulate state outside the Hub.

4. **Build the Episodic Buffer as a complete-episode retriever**: When Agent B drafts an email after Agent A's chat ends, it should fetch the *entire chat episode* (not chunked snippets) from the Hub. The interface should be: `get_episode(session_id) -> List[Turn]`. This is the part most RAG stacks get wrong — they return paragraph-sized chunks when the agent needs a coherent conversation.

5. **Layer three retrieval modes on top of the Hub**:
   - **SQL search** for chronological/structured queries: "interactions from this customer last Tuesday," "all escalations this month."
   - **Full-text search** for exact-string matches: "show me messages mentioning 'refund'."
   - **Semantic search** for intent-based queries: "everything related to billing confusion."

   Expose all three as tools the agents can call. Don't force one mode to do all three.

6. **Apply role-based memory access as your default**:

   ```
   - Tier-1 chat agent (Agent A): read/write own session episodes only; read customer's health summary
   - Email follow-up agent (Agent B): read most recent chat episode for the customer; write its own draft
   - Customer health agent (Agent C): read all episodes for its customer; write the health summary
   - Supervisor agent: read across all agents, all customers
   ```

   Encode these as authentication scopes in the Hub's API. Treat the Hub as a database with row-level security, not as a free-for-all.

7. **Add a Memory Management Agent for planning tasks**: When an agent needs to "plan" — e.g. the Supervisor deciding which customer needs proactive outreach — don't let it trawl the Hub directly. Route through a dedicated Memory Management Agent that summarizes, ranks, and returns the curated slice. This keeps planning agents from drowning in raw history.

8. **Validate by inverting the failure mode the paper names**: Pre-Hub baseline: Agent B writes the follow-up email with no awareness of what Agent A actually said in chat. Post-Hub: Agent B's emails should reference specific points from the chat ("As I mentioned, the refund will process in 5-7 days"). If you can't see that change, the Episodic Buffer isn't being used correctly.

**Expected outcome:** Each agent has access to a shared, persistent record of every interaction with every customer, with retrieval modes that match the task (chronological for billing, full-text for keyword complaints, semantic for "general frustration"). Cross-agent handoffs become coherent — Agent B's emails reference Agent A's chat; the Supervisor can audit decisions retrospectively; the Customer Health agent builds longitudinal summaries from real episodes rather than reconstructions. The infrastructure is heavier than a single-agent LangChain memory, but the failure mode the paper names — domain isolation — is gone.

## Best Figure

![Figure 4 — Innovative working memory model (page 6)](figures/guo-2023-working-memory-fig.png)

Image Candidates:
Figure 1 (p. 2): Contrasts isolated traditional LLM interactions against the proposed Working Memory model — the high-level "why" diagram.
Figure 3 (p. 4): Current working memory model of LLM agents — shows the *before* state, with Central Processor + Interaction History Window + External Environment Sensor but no Episodic Buffer and "task domain" dotted-line walls between sessions.
Figure 4 (p. 6): The innovative working memory model — adds the Working Memory Hub and Episodic Buffer to the architecture, the paper's central contribution.

Best Image:
Figure Name: Figure 4: "Innovative working memory model"
Figure Page: 6
Slide Caption: The paper's proposed architecture — a centralized Working Memory Hub underpins every component and an Episodic Buffer joins Central Processor, Interaction History Window, and External Environment Interface.
Description: Figure 4 is the paper's central architectural proposal. The Central Processor (the LLM itself) sits at the top, with three peer components below it — the External Environment Interface (real-time I/O), the Interaction History Window (short-term cache of recent turns), and the new Episodic Buffer (which retrieves complete past episodes). All three connect down to the Working Memory Hub, which is the persistent data substrate storing every input, output, and interaction history across sessions. The bidirectional arrows show that every component both reads from and writes to the Hub. The difference from Figure 3 (the "before" state) is exactly two additions: the Episodic Buffer and the Working Memory Hub — these are the load-bearing pieces of the paper's thesis.

## What Experts Overlook

The overlooked detail is that the **Working Memory Hub is not just a database — it's the architectural element that decouples "what the LLM sees" from "what the agent remembers."** Most engineers reading this paper will see the diagram and think "oh, this is just RAG with a vector store." But the paper is making a sharper claim: every other component (Interaction History Window, Episodic Buffer, External Environment Interface) is a *view* over the Hub, not a separate store. The Hub owns all I/O and persists it durably; the other components are configurable lenses on that single source of truth. This is visible in the paper's repeated phrasing — "All inputs and outputs are stored in the Working Memory Hub," "Drawing from the Working Memory Hub, Interaction History Window maintains a short-term cache," "The Episodic Buffer retrieves complete episodes from Working Memory Hub." Section 3 makes the point explicit: "Without the orchestrating function of the Working Memory Hub, the components would be isolated islands of memory."

**Why it matters:** Most memory designs in 2024-2025 conflate the store with the access pattern — they bolt a vector index onto the prompt and call it memory, which inherits all the brittleness of the prompt layer (token limits, lossy summarization, no chronological control). The Hub-as-substrate framing forces you to make the persistent record the *source of truth* and treat windows, buffers, and summaries as derived views. That separation is what enables cross-session continuity, cross-agent sharing, and the ability to swap retrieval strategies without losing data.

**Example of good use:** A customer-success multi-agent system writes every chat turn, email draft, and tool call to a Postgres-backed Hub with row-level security per customer. The chat agent reads the last 10 turns through a "rolling window" view; the email agent reads the whole chat episode through an "episode" view; the supervisor reads cross-agent activity through a "by-customer-by-week" SQL view. Same Hub, three views — when you decide later to add a "monthly summary" view or a "frustrated-customers" semantic-search view, the underlying data is already there.

**Example of misapplication:** A team reads "Working Memory Hub" as "add a vector database" and bolts Pinecone onto their existing prompt-based memory. Every agent still maintains its own session state in memory, with periodic dumps to Pinecone for retrieval. When they later try to enable cross-agent memory, they discover their Pinecone index is incomplete (only what agents chose to dump), fragmented (each agent's dumps in its own namespace), and lossy (only summaries, not raw turns). They've added complexity without gaining the substrate-level decoupling — the Hub design assumed the *persistent* record owns the data, not the agents.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- Baddeley, A. (2003). Working memory: looking back and looking forward. *Nature Reviews Neuroscience*, 4, 829–839.
- Brown, T. B., Mann, B., Ryder, N., et al. (2020). Language Models are Few-Shot Learners. [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Cornago, S., Ramakrishna, S., & Low, J. S. C. (2023). How can Transformers and large language models like ChatGPT help LCA practitioners? *Resources, Conservation and Recycling*, 196, 107062.
- Graves, A., Wayne, G., & Danihelka, I. (2014). Neural Turing Machines. [arXiv:1410.5401](https://arxiv.org/abs/1410.5401)
- Rillig, M. C., Ågerstrand, M., Bi, M., et al. (2023). Risks and Benefits of Large Language Models for the Environment. *Environmental Science & Technology*, 57(9), 3464–3466.
- Sukhbaatar, S., Szlam, A., Weston, J., et al. (2015). End-To-End Memory Networks. [arXiv:1503.08895](https://arxiv.org/abs/1503.08895)
- Wang, K., Lu, Y., Santacroce, M., et al. (2023). Adapting LLM Agents Through Communication. [arXiv:2310.01444](https://arxiv.org/abs/2310.01444)
- Wang, Q., Ding, L., Cao, Y., et al. (2023). Recursively Summarizing Enables Long-Term Dialogue Memory in Large Language Models. [arXiv:2308.15022](https://arxiv.org/abs/2308.15022)
- Wang, W., Dong, L., Cheng, H., et al. (2023). Augmenting Language Models with Long-Term Memory. [arXiv:2306.07174](https://arxiv.org/abs/2306.07174)
- Weston, J., Chopra, S., & Bordes, A. (2015). Memory Networks. [arXiv:1410.3916](https://arxiv.org/abs/1410.3916)

(13 references total — full structured list in frontmatter `citations:`)

## Related Digests

- [[ma-2026-nemori-distillation]] — What Deserves Memory: Adaptive Memory Distillation for LLM Agents
- [[du-2025-rethinking-memory]] — Rethinking Memory in LLM based Agents: Representations, Operations, and Emerging Topics
- [[wang-2026-memmachine]] — MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents
- [[wang-2025-mirix]] — MIRIX: Multi-Agent Memory System for LLM-Based Agents
- [[wu-2025-human-ai-memory-survey]] — From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs
- [[zhang-2025-llm-memory-survey]] — Memory in Large Language Models: Mechanisms, Evaluation and Evolution

## Reviewer Notes

**Overall severity:** Clean

Every substantive claim in the digest is grounded in the paper text:
- The two-challenge diagnosis (token-window ceiling + domain isolation) is stated explicitly in Section 2.2.
- The Working Memory Hub / Episodic Buffer additions, their roles, and the framing of other components as views over the Hub are quoted near-verbatim from Section 3.
- The third-party database recommendations (Postgres, Elasticsearch, Pinecone, Xata/PaaS) and PaaS access pattern are from Section 4.
- The five access-control strategies (role-based, task-based, autonomous, collaboration-scenario, Memory Management Agent) are enumerated in Section 5.1.
- The three search-modality recommendation (SQL + full-text + semantic, combined in layered retrieval) is from Section 5.2.
- The "no experiments / position paper" framing is accurate — the paper contains no benchmarks, no experiments, no quantitative results.
- The implication caveat ("Use as vocabulary, not as evidence") is appropriately conservative.

One typo in the source paper: "Picone" appears to be a misspelling of "Pinecone" (vector database) — the digest uses "Pinecone" for clarity; this is a correction, not a hallucination.

The architectural reading of the Hub as "substrate" with other components as "views" is interpretive but well-supported by the paper's repeated framing ("All inputs and outputs are stored in the Working Memory Hub," "Drawing from the Working Memory Hub..."). Flagged here as interpretation, not as a paper quote.
