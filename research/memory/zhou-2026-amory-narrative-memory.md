---
corpus: agentic-memory
kind: paper-digest
slug: zhou-2026-amory-narrative-memory
title: "Amory: Building Coherent Narrative-Driven Agent Memory through Agentic Reasoning"
authors:
  - "Yue Zhou"
  - "Xiaobo Guo"
  - "Belhassen Bayar"
  - "Srinivasan H. Sengamedu"
year: 2026
publication_date: "2026-01"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2601.06282"
doi: null
arxiv_id: "2601.06282"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Defer write-time consolidation until a topic goes inactive — momentum-aware (lazy) consolidation outperforms rapid (eager) consolidation by +5.4 on temporal reasoning, because the inactivity itself is the temporal-boundary signal; bound to narrative plot+character structure plus coherence-driven LLM retrieval, this beats Mem0 by +27.8 J-score on LoCoMo and beats full-context on multi-hop by +3% at ~half the latency."
topics:
  - agent-memory
  - episodic-memory
  - narrative-memory
  - consolidation-timing
  - coherence-retrieval
  - locomo-benchmark
  - long-conversation
  - llm-evaluation
  - write-time-synthesis
tags:
  - paper
  - memory-architecture
  - narrative-binding
  - inactive-consolidation
  - momentum-trigger
  - graph-rag
  - benchmark
entities:
  - zhou-yue
  - guo-xiaobo
  - bayar-belhassen
  - sengamedu-srinivasan
related_digests:
  - hu-2026-evermemos
  - adler-2026-storage-not-memory
  - li-2025-memos
  - patel-2026-engram
  - maharana-2024-locomo
citations:
  - title: "Goal reasoning and narrative cognition"
    authors: ["Tory S Anderson", "Gatech Edu"]
    year: 2015
    venue: "Goal Reasoning: Papers from the ACS Workshop"
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
  - title: "From local to global: A graph rag approach to query-focused summarization"
    authors: ["Darren Edge", "Ha Trinh", "Newman Cheng", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2404.16130"
  - title: "Interdependence of episodic and semantic memory: Evidence from neuropsychology"
    authors: ["Daniel L Greenberg", "Mieke Verfaellie"]
    year: 2010
    venue: "Journal of the International Neuropsychological Society"
    doi: null
    url: null
    arxiv_id: null
  - title: "LightRAG: Simple and fast retrieval-augmented generation"
    authors: ["Zirui Guo", "Lianghao Xia", "Yanhua Yu", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2410.05779"
  - title: "Towards reasoning in large language models: A survey"
    authors: ["Jie Huang", "Kevin Chen-Chuan Chang"]
    year: 2023
    venue: "Findings of the Association for Computational Linguistics: ACL 2023"
    doi: null
    url: null
    arxiv_id: null
  - title: "HippoRAG: Neurobiologically inspired long-term memory for large language models"
    authors: ["Bernal Jimenez Gutierrez", "Yiheng Shu", "Yu Gu", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "A human-inspired reading agent with gist memory of very long contexts"
    authors: ["Kuang-Huei Lee", "Xinyun Chen", "Hiroki Furuta", "et al."]
    year: 2024
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2005.11401"
  - title: "MemOS: An operating system for memory-augmented generation (MAG) in large language models"
    authors: ["Zhiyu Li", "Shichao Song", "Hanyu Wang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2505.22101"
  - title: "Evaluating very long-term conversational memory of LLM agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "et al."]
    year: 2024
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemGPT: Towards LLMs as operating systems"
    authors: ["Charles Packer", "Sarah Wooders", "Kevin Lin", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "AgentIF: Benchmarking instruction following of large language models in agentic scenarios"
    authors: ["Yunjia Qi", "Hao Peng", "Xiaozhi Wang", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2505.16944"
  - title: "Zep: A temporal knowledge graph architecture for agent memory"
    authors: ["Preston Rasmussen", "Pavlo Paliychuk", "Travis Beauvais", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2501.13956"
  - title: "Memory consolidation"
    authors: ["Larry R Squire", "Lisa Genzel", "John T Wixted", "et al."]
    year: 2015
    venue: "Cold Spring Harbor Perspectives in Biology"
    doi: null
    url: null
    arxiv_id: null
  - title: "Episodic and semantic memory"
    authors: ["Endel Tulving"]
    year: 1972
    venue: "Organization of Memory"
    doi: null
    url: null
    arxiv_id: null
  - title: "A-MEM: Agentic memory for LLM agents"
    authors: ["Wujiang Xu", "Kai Mei", "Hang Gao", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2502.12110"
  - title: "A contextual binding theory of episodic memory: systems consolidation reconsidered"
    authors: ["Andrew P Yonelinas", "Charan Ranganath", "Arne D Ekstrom", "et al."]
    year: 2019
    venue: "Nature Reviews Neuroscience"
    doi: null
    url: null
    arxiv_id: null
  - title: "G-Memory: Tracing hierarchical memory for multi-agent systems"
    authors: ["Guibin Zhang", "Muxin Fu", "Guancheng Wan", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2506.07398"
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2305.10250"
  - title: "Veracity bias and beyond: Uncovering LLMs' hidden beliefs in problem-solving reasoning"
    authors: ["Yue Zhou", "Barbara Di Eugenio"]
    year: 2025
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Paraphrase and solve: Exploring and exploiting the impact of surface form on mathematical reasoning in large language models"
    authors: ["Yue Zhou", "Yada Zhu", "Diego Antognini", "et al."]
    year: 2024
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Minor fact tweak (corrected)"
---

# Amory: Building Coherent Narrative-Driven Agent Memory through Agentic Reasoning

**Authors:** Yue Zhou (UIC), Xiaobo Guo, Belhassen Bayar, Srinivasan H. Sengamedu (Amazon)
**Published:** 2026-01 · [Source](https://arxiv.org/abs/2601.06282)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Amory (Zhou et al., UIC + Amazon, Jan 2026) builds working memory by having an LLM (Claude 3.5 Sonnet V2) construct episodic narratives with plot/subplot/character structure plus a side-channel semantic graph of "peripheral facts" (Neo4j triples), rather than dumping turns into embeddings — on LoCoMo (10 scenarios, ~20k tokens each, ~200 Qs per scenario across single-hop / multi-hop / commonsense / temporal), the EM+SM variant scores **87.7 overall J-score vs 59.9 for Mem0** (+27.8 absolute), 86.1 for Full-Context, 79.8 for ReadAgent, 54.5 HippoRAG, 52.6 RAG, 37.5 A-MEM, 29.6 Zep, and crucially **beats Full-Context on multi-hop (+3%) and temporal (+11%) at roughly half FC's p90 latency (3.21s vs 6.08s)** `[Encode + Retrieve + Aggregate]`. The headline mechanism is **momentum-aware "inactive" consolidation** — wait until a narrative stops accreting new fragments (N=10 lookback) before summarising it, which beats rapid consolidation by +5.4 on temporal (87.7 vs 82.3) and +6.2 on commonsense (78.1 vs 71.9), and beats no-consolidation by +6.0 overall — directly addressing the *when to compile* question with a concrete signal (topic-drift = consolidation trigger) `[Maintain + Aggregate, cross-interaction with Encode]`. Retrieval uses LLM coherence reasoning over plot-headline trees instead of cosine similarity, achieving substantially higher memory-coverage at top-k=2 (saturating ~k=4), with embedding retrieval collapsing especially on multi-hop — qualitative examples show the agentic retriever picks memories with sim-scores of 0.08–0.29 (vs embedder's 0.49–0.59) because it follows causal/logical links rather than lexical overlap `[Retrieve + Ground]`. Semantic memory is deliberately restricted to *peripheral* facts as graph triples to avoid the noisy OpenIE-over-dialogue failure mode, and context compression at k=2 still drops 96.3% of raw conversation tokens `[Encode + Ground]`. On an out-of-distribution stress test (350k-token AgentIF-derived agentic dialogue with p=0.5 topic switching), Amory hits **47.4% constraint recall vs ReadAgent 36.8 / A-Mem 27.8 / Mem0 25.1 / HippoRAG 23.9 / Zep 21.3** — showing embedding/graph baselines collapse when many instructions share surface form ("You are a..."). **Most actionable takeaway:** defer write-time synthesis until a topic goes inactive — rapid/eager consolidation actively destroys temporal reasoning, while waiting for the momentum signal converts the same LLM calls into a +27.8-point win, and structuring memory as narratives with characters makes coherence-driven retrieval beat embeddings hardest exactly where it matters (multi-hop).

## Key Takeaway

Consolidating memory eagerly — the obvious move, and what Mem0 and most "agentic memory" systems do on every turn — actively *degrades* temporal reasoning, while waiting until a narrative thread goes quiet outperforms both eager and no-consolidation across the board (+27.8% over Mem0). The reason is that conversational topics have **momentum**: a thread's inactivity is itself the signal that it's safe to compress, because premature summarization fights ongoing accumulation and smears chronological boundaries. The retrieval flip is just as sharp — embedding similarity is the wrong metric for memory because it pulls back surface-token matches ("LeBron James" → "meeting LeBron James") while missing the coherent narrative that actually answers the query (John's own basketball aspirations), so a slower LLM-reasoning retriever beats a fast vector one on coverage, especially for multi-hop.

## Implications

- **Invest write-time effort to slash query-time latency**: Amory shows that doing narrative construction, consolidation, and semanticisation offline (asynchronous to the user) yields full-context-quality answers at half the latency. For a Ralph-style stateless loop, that means biasing toward heavier `/learn`-time work (frontmatter, narrative binding, dedup) over more clever query-time RAG. `[E → R]`

- **Bind fragments into narratives, not isolated chunks**: The biggest gains (+27.8% over Mem0, +11% temporal vs full-context) come from grouping logically/chronologically connected fragments under plot+character headlines, not from better embeddings. Reframe `experiences/captures/` and patterns as evolving narratives with characters (people, ventures) and headlines that can branch into subplots, rather than flat atomic memories. `[E, N]`

- **Consolidate on inactivity, never on a fixed step**: "Rapid consolidation" lifts multi-hop but hurts temporal reasoning, while "inactive consolidation" (only after N quiet turns on that thread) outperformed it by **+2.4 overall and +5.4 on temporal** (87.7 vs 85.3 overall; 87.7 vs 82.3 temporal in Table 2). Trigger `/learn`-style summarization per-thread when that thread goes quiet, not on a global schedule, to avoid premature summarization that loses chronology. `[A, M]`

- **Headlines must be revisable, not frozen at creation**: Amory re-evaluates whether the current plot headline still covers all subplots and rewrites it when it doesn't — drift is detected by structural mismatch, not by similarity decay. Treat your pattern/memory headers as mutable summaries that get re-derived from their children, and store the rewrite history so you can audit drift. `[A, M]`

- **Split the store: narrative episodic vs. peripheral semantic triples**: Amory deliberately restricts the graph to "trivia" that's tangential to the main plot, because forcing all facts into a graph yields "dense and noisy" structures from informal dialogue. In your QMD setup, keep the rich free-text patterns/captures as episodic memory and reserve the triple/graph layer for orphan facts (e.g., "Nadia is the user's partner") that don't belong to a venture-narrative. `[E, G]`

- **Coherence-driven retrieval beats embeddings for multi-hop**: Top-1 embedding choices scored 0.49–0.59 cosine sim but were wrong; the agentic retriever picked items at sim ~0.08–0.29 that were *logically* connected. For your hybrid `qmd query`, lean on the LLM to reason over plot headlines as a second pass rather than raising the BM25/vector top-k — coverage saturates at k=4 with agentic, degrades with embedding. `[R]`

- **Measure coverage separately from answer accuracy**: Amory introduces a "memory coverage rate" (% of questions where all ground-truth evidence is in top-k) distinct from J-score, exposing cases where the model guessed right without evidence or got it wrong with full context. Add a coverage harness to your eval (does `/learn` actually surface the file containing the truth?) — don't conflate "Claude answered well" with "memory retrieval worked." `[R, M]`

- **Reactivation matters as much as consolidation**: An "inactive" narrative can be reactivated when new related fragments arrive, which preserves the option to extend rather than fork a duplicate story. Your `/learn` dedup step should not just suppress writes — it should *reopen* a dormant memory file and append, so venture/contact narratives stay coherent across months rather than fragmenting into near-duplicates. `[N, M]`

- **Watch the long-horizon failure mode embeddings hide**: On a 350k-token agentic conversation (AgentIF), all embedding/graph baselines collapsed to 21–37% constraint recall while Amory's narrative-grouped EM+SM hit 47.4% — embeddings retrieve semantically-similar-but-wrong instructions because everything starts "You are a...". Stress-test your stack with synthetic long-context constraint-recall tasks, not just LoCoMo-style Q&A, before trusting it for multi-month venture memory. `[R, M]`

## How to Apply It (method)

**Scenario:** You run Flow OS with a QMD hybrid-search memory layer where each turn is queued by a Stop hook and drained by an LLM extractor on the next session start (extraction-on-write). You suspect that pushing more synthesis into the *write* path — specifically, organising fragments into episodic narratives with momentum-triggered consolidation — would beat your current "extract atomic memories + rely on BM25/vector at query time" pattern, especially for multi-hop questions like "what did we say about X across these three ventures." Before paying the cost of rewriting your write path, you want to A/B test Amory's three write-time mechanisms (Binding, Consolidation-with-Momentum, Semanticisation) against your current Flow OS extractor on a fixed eval set, measured on memory-coverage (Encode/Retrieve quality), p90 retrieval latency (Maintain cost), and accuracy by reasoning type (multi-hop vs temporal vs single-hop).

**Steps:**

1. **Freeze a held-out eval set from your own corpus.** Pick ~5 long-running conversation threads from `experiences/captures/` and `.flow/events.jsonl` — each ~15–25k tokens, spanning multiple sessions. For each thread, hand-annotate ~20 questions across the four LoCoMo categories: multi-hop ("did Dana and Sam both mention pricing concerns?"), temporal ("when did we shift away from rapid consolidation?"), commonsense ("is Nadia a sales prospect?" — should be no), and single-hop ("what's Flow's revenue as of April 2026?"). Record the gold answer AND the gold evidence span (which fragments must be retrieved). This separates retrieval quality from answer quality later.

2. **Set up four arms.** Run the same eval set through each:
   - **Arm A (control)**: your current Flow OS extractor — atomic memory files with frontmatter, retrieved via `qmd query` (BM25+vector hybrid).
   - **Arm B (Amory-EM only)**: episodic-narrative write path with Binding + inactive Consolidation, retrieved via coherence prompt (no semantic graph).
   - **Arm C (Amory-EM+SM)**: Arm B plus Semanticisation into a Neo4j graph for peripheral facts.
   - **Arm D (raw + full-context)**: no write-time extraction, just dump full thread into the model — the latency-blown ceiling.

3. **Implement the four Amory write-time prompts as-is.** Use Claude 3.5 Sonnet V2 (paper's setting) or your current model — keep model constant across arms. Set `T = 20` turns (init threshold), `N = 10` (fragments analysed per consolidation), `k = 2` (top memories retrieved). An episodic memory is "inactive" when one full iteration passes with no new fragment bound to it — that's your consolidation trigger.

4. **Run inactive vs rapid consolidation as a sub-ablation.** Inside Arm B, run two variants: rapid (consolidate every iteration) vs inactive (only when momentum stalls). The paper found rapid HURT temporal reasoning by 5.4 points while inactive helped — if your eval has lots of "when did X happen" questions, this matters.

5. **Generate answers with a fixed QA prompt across all arms.** Same model, same prompt, only the retrieved context differs — this isolates the write-path effect. Use the paper's QA prompt verbatim (convert relative time references to specific dates, answer in <6 words).

6. **Score with the paper's LLM-as-Judge.** Use Claude as judge with the paper's stricter rubric (paper notes Mem0's original rubric was "overly permissive"). Report a J-score per reasoning category AND overall — the shape of the curve across categories is what tells you which mechanism is doing the work.

7. **Compute two retrieval-quality metrics independent of accuracy.**
   - **Memory coverage rate** = fraction of questions where ALL gold evidence spans are present in top-k retrieved memories. Sweep k = 1..4. Coverage saturates around k=4 in the paper.
   - **Context compression rate** = fraction of full conversation NOT used at query time. Paper hits >96.3% at k=2. This is your Maintain-axis efficiency number.

8. **Log latency percentiles per arm** — p50, p90, p95, p99. Track both online (query-time) and offline (write-time, async). Paper found agentic retrieval added latency vs embedding retrieval but stayed at ~50% of full-context.

9. **Decide using the ENGRAM lens.** Look across the matrix:
   - **Encode**: did Amory's narrative binding produce higher-quality fragments than your atomic extractor? (proxy: coverage at k=1)
   - **Network**: did consolidation+semanticisation create useful structure? (proxy: multi-hop J-score)
   - **Ground**: are timestamps preserved end-to-end?
   - **Retrieve**: coherence-driven vs embedding (paper Table 3: embedder picks "Caroline's paintings exploring identity" for "What is Caroline's identity?" — high token overlap, wrong story. Agentic picks the LGBTQ journey story — coherent, correct.)
   - **Aggregate/Maintain**: offline-processing curve (paper Fig 2)

10. **Optional generalisation test.** Repeat on a long-horizon agentic eval. Paper builds one from AgentIF (350k-token interleaved-task conversation) and measures constraint recall. Amory hits 47.4% vs Mem0's 25.1% — the gap widens as horizon grows.

**Expected outcome:** A 4-arm × 4-reasoning-category accuracy matrix plus a coverage-vs-k curve, a compression-vs-k curve, and latency percentiles per arm — enough to decide whether to replace your current atomic-extraction write path with narrative-binding+inactive-consolidation, keep your current one, or adopt a hybrid (e.g., Amory-EM for episodic threads, your current extractor for facts). The decisive signal is whether multi-hop and temporal J-scores lift by Amory's reported ~+27.8% on YOUR corpus, and whether p90 latency stays under ~3.5s once you absorb the agentic-retrieval cost. If multi-hop and temporal both lift but single-hop doesn't, the right move is hybrid; if temporal alone lifts, your win is from inactive-consolidation timing, not narrative structure per se.

## Best Figure

![Figure 4 — Memory coverage rate using coherence-driven and embedding-based retriever (page 8)](figures/zhou-2026-amory-narrative-memory-fig.png)

**Figure Name:** Figure 4: "Memory coverage rate using coherence-driven and embedding-based retriever (Left and Middle) and context compression rate at different top-k for memory retrieving (Right)."

**Slide Caption:** Coherence-driven retrieval beats embedding similarity on memory coverage — especially for multi-hop questions — while still compressing 96%+ of the conversation.

**Description:** Three-panel comparison on LoCoMo. Left and Middle: memory-coverage-rate at top-k = 1-4 for four reasoning categories (multi-hop, temporal, commonsense, single-hop) — left for Amory's coherence-driven agentic retriever, middle for a standard embedding-based retriever. Right: context compression rate as top-k grows. The contrast is the paper's core retrieval claim made visible: coverage climbs and saturates around k=4 for the agentic retriever, whereas the embedding retriever's coverage collapses on multi-hop queries. The compression panel anchors the practicality side, showing the system still discards >96% of raw context at k=2, so coverage gains do not come from retrieving more. For an ENGRAM-lens reader this is the Retrieve-stage money shot: isolates retrieval quality from end-to-end accuracy and shows the mechanism (coherence reasoning over plot/subplot structure) is what carries the win.

**Other strong candidates:**
- **Figure 2 (p. 6)** — Offline processing-time curves contrast Amory (with/without consolidation) against six baselines on a single axis, exposing the cost-of-coherence trade-off.
- **Figure 3 (p. 7)** — Episodic memory evolvement visualization shows narrative threads accreting fragments and branching subplots over offline iterations — the most direct view of the "active construction" thesis.

## What Experts Overlook

The detail most readers will skim past is the **asymmetric ablation result on consolidation timing** (Table 2 and the surrounding discussion in §4.3). Everyone sees that "consolidation helps." Few notice that **rapid consolidation actively hurts temporal reasoning (82.3 vs 87.7), even though it helps multi-hop reasoning**. The authors' explanation is buried in one sentence: topic shifts in human conversation are *correlated with* temporal changes, so the moment of inactivity is itself a temporal signal. Consolidating on a fixed schedule destroys that signal — you collapse fragments that happen to fall in the same window regardless of whether the topic actually moved. Consolidating on inactivity preserves the boundary between "things that belonged together" and "things that just happened nearby in time," because the boundary is drawn by the *conversation's own rhythm* rather than by the clock. The headline that a subplot ends up with is therefore implicitly time-anchored — it summarizes a coherent stretch, not a fixed-length stretch.

**Why it matters:** This reframes consolidation as a *measurement* problem, not a *compression* problem. The trigger isn't a cost-saving heuristic — it's a load-bearing inductive bias that injects temporal structure into the resulting summary for free. If you read the paper as "Amory works because narratives," you'll miss that the narratives are only well-formed because the segmentation respects momentum. Strip the momentum trigger and use rapid consolidation, and you still get narratives — they just lose 5+ points on temporal reasoning because their boundaries no longer correlate with actual topic shifts. The same logic applies to any synthesizing system: the *event* that triggers synthesis encodes information that the synthesis itself cannot recover.

**Example of good use:** In an ENGRAM-style agentic OS, the "Aggregate" step is often run on a cadence — every N turns, every K tokens, nightly cron. Take Amory's lesson and instead aggregate when the *agent's working set goes quiet*: when no new memories have been bound to a given thread for some span, or when the salience score of incoming items against a thread drops below threshold. The resulting plot/subplot summaries inherit the conversation's natural punctuation, so later queries like "what was happening when X stalled" can find the right cluster without explicit timestamp reasoning — the cluster boundary *is* the temporal answer. Especially powerful for the write-time-vs-query-time question: you can afford to do more at write-time precisely because the trigger gives you a free signal you'd otherwise have to recompute at query-time.

**Example of misapplication:** A team building a memory layer reads Amory, likes the narrative-tree idea, and implements consolidation on a fixed cadence ("every 10 new fragments, summarize") because it's simpler to schedule and easier to reason about for capacity planning. Multi-hop benchmarks look fine — possibly even better than inactive consolidation, matching Table 2. They ship it. Three weeks in, users report the agent confidently bundles unrelated events that happened in the same session ("you mentioned the contract renewal *and* your dog's vet visit on Tuesday — here's the connection") and badly mis-orders things in temporal queries ("when did we decide to pause Fizz?" returns a cluster that conflates two distinct decision moments six weeks apart). The narratives look coherent on paper but the boundaries are arbitrary, so any query that depends on *when* a topic was alive returns garbage. Worse, because the headlines were generated post-hoc over arbitrary windows, there's no clean fix short of re-segmenting the entire memory store — the damage is baked into the summaries the LLM already wrote.

## Extracted Prompts

**Prompt explanation:** LLM-as-Judge — labels a generated answer as CORRECT or WRONG by comparing against gold for a question about prior conversations.

```
Your task is to label an answer to a question as CORRECT or WRONG. You will be given the following data:
(1) a question (posed by one user to another user),
(2) a gold (ground truth) answer,
(3) a generated answer
which you will score as CORRECT / WRONG.

The point of the question is to ask about something one user should know about the other user based on their prior conversations.
The gold answer will usually be a concise and short answer that includes the referenced topic, for example:
Question: Do you remember what I got the last time I went to Hawaii?
Gold answer: A shell necklace
The generated answer might be much longer, but you should be generous with your grading — as long as it **expresses the same meaning** as the gold answer, it should be counted as CORRECT.

For time related questions, the gold answer will be a specific date, month, year, etc. The generated answer might be much longer or use relative time references (like "last Tuesday" or "next month"), but you should be generous with your grading — as long as it refers to the same date or time period as the gold answer, it should be counted as CORRECT. Even if the format differs (e.g., "May 7th" vs "7 May"), consider it CORRECT if it's the same date.

Now its time for the real question:
Question: {question}
Gold answer: {gold_answer}
Generated answer: {generated_answer}

First, provide a short (one sentence) explanation of your reasoning, then finish with CORRECT or WRONG.
Do NOT include both CORRECT and WRONG in your response, or it will break the evaluation script.

Just return the label CORRECT or WRONG in a json format with the key as "label".
```

**Prompt explanation:** Question-Answering prompt — agent answers user queries by reasoning over retrieved episodic and semantic memory stories with timestamps.

```
You are an intelligent memory assistant tasked with retrieving accurate information from conversation memories.

# CONTEXT:
You have access to stories from two speakers in a conversation. These stories contain timestamped information that may be relevant to answering the question.

# INSTRUCTIONS:
1. Carefully analyze all provided stories and pay special attention to the timestamps to determine the answer
2. If the question asks about a specific event or fact, look for direct evidence in the story content
4. If there is a question about time references (like "last year", "two months ago", etc.), calculate the **actual date** based on the story timestamp. For example, if a story note on 4 May 2022 mentions "went to India the previous year," then the trip occurred in 2021.
5. Always convert relative time references to **specific dates, months, or years**. For example, convert "last year" to "2022" or "two months ago" to "March 2023" based on the memory timestamp. Ignore the reference while answering the question.
6. If additional information is needed beyond the stories, take your best guess with commonsense.
7. Be concise. The answer should be less than 5-6 words.

Relevant Stories:
{full_stories}

Additional Stories:
{add_trivas}

Question: {question}

Answer:
```

**Prompt explanation:** Story Initialization — segments a multi-turn, multi-date conversation into distinct story threads (initial episodic memory bank construction).

```
You are given a multi-turn, multi-date conversation between two people. The conversation may include topic switches, story developments, or new ideas being introduced over time.

Your task is to extract and organize the conversation into a list of story threads, where each story:

* Belongs to one main owner (the story owner).
* Has a distinct topic or subject.
* Evolves chronologically with unfolding related messages.

For each story, return a Python dictionary with:

* `"owner"`: the speaker of the story.
* `"topic"`: a title for the story.
* `"content"`: a copy of the message, including the timestamp, speaker, and utterance.

Very Important:
If a new message connects logically and chronologically to an existing story, expand that story in the content tuple. Treat them as separate stories only if they belong to different domains.

The conversation:
{conv}

Output format: return the Python list of dictionaries.
```

**Prompt explanation:** Memory Binding — routes a new conversation turn either to extend an existing story or to create a new story.

```
You are given:

1. A list of existing stories, each with:
 - "owner": the speaker of the story.
 - "topic": a title for the story

2. A short context window of recent dialogue turns

3. A new turn

Your task:
Use the **recent dialogue context** only to better understand the **new turn**. Then, for this new message(s) (only when it contains factual information, see below), decide:

Whether it logically and thematically extends an existing story, OR
Whether it introduces a new story in which, propose a new owner and a topic for it.

If the new message belongs to a new domain, create a new story instead.

Input:

Existing stories:
{headlines}

Recent dialogue context:
{recent_context}

New conversation turn:
{new_conv}

Output format: a list of routing decisions.
Each decision should be a Python dictionary with:
 * "message_excerpt": a copy of the message, including the timestamp, speaker, and utterance.
 * "action": one of:
      - "extend_story"
      - "create_new_story"
 * If "extend_story": include "topic" and "owner"
 * If "create_new_story": include a proposed "topic" and "owner"

Return **only** the list of routing decisions. No explanation or verbose.
```

**Prompt explanation:** Consolidation — analyzes new memory items, proposes substory topics summarizing them, and updates the main story topic if needed.

```
You are analyzing the structure of a story composed of memory items.

The current **main topic** of the story is:
   "{main_topic}"

Here are the **existing substories**:
{substories_text if substories else "None yet."}

Here are the **new memory items** to analyze:
{new_items_text}

Your tasks:
1. Determine a **substory topic** that summarizes the **new memory items**. The topic should be specific, informative, and include all the main events.
2. You can include multiple substories if there are various memory items can't be summarized into one substory.
3. It is safe to assume that each substory consists of a continuous block of items.
4. Determine whether the current main topic still conceptually covers **all** substory topics. If not, propose a new, broader or more accurate topic.
5. Return a Python dictionary with a list of these new substories (with corresponding indice of the memories/utterances) and the new topic (or None if unchanged).

The return format must be strictly:
{{
     "substories": [
          {{"sub_topic": "...", "indice": (start, end)}},
          ...
     ],
     "new_topic": "..." or None
}}
```

**Prompt explanation:** Semanticisation — extracts peripheral factual details NOT logically inferable from story topics, as facts with timestamps for the semantic memory graph.

```
You are analyzing memory items within the context of a story.

Main story topic:
"{main_topic}"
Existing substories:
{substories_text if substories else "None."}

New memory items:
{new_items_text}

Your task:

Identify memory items that contain facts, but **not logically inferable from the main and substory topics**. These items contain specific fact that are important, but would be difficult to retrieve later if only the story headline is used.

Output format:
Return a Python list of dictionaries, each with two keys:
- "fact": the summary of important detail
- "timestamp": the timestamp or reference from the memory item

If there are no such items, return an empty list: []

No verbose or explanation.
```

**Prompt explanation:** Coherence Retrieving — selects the top-k stories most likely to contain information relevant to the user's question.

```
You are given a question and a list of story titles. Some of the stories may contain sub-stories as additional information.
Your task is to select the top {k} stories that are most likely to contain information useful for answering the question.

Question:
{question}

Stories:
{headlines}

Output format: a list of choice(s) based on the relevance.
Each choice should be a Python dictionary with:
 * "owner": the owner
 * "topic": the topic

Return only the Python list of choice(s) based on the relevance. No verbose.
```

## Citations

First 10 (see frontmatter for full list of 22 references):

- Anderson (2015) — *Goal reasoning and narrative cognition* — Goal Reasoning ACS Workshop
- Chhikara et al. (2025) — *Mem0: Building production-ready AI agents with scalable long-term memory* — arXiv:2504.19413
- Edge et al. (2024) — *From local to global: A graph RAG approach to query-focused summarization* — arXiv:2404.16130
- Greenberg & Verfaellie (2010) — *Interdependence of episodic and semantic memory* — J Int Neuropsychol Soc
- Guo et al. (2025) — *LightRAG: Simple and fast retrieval-augmented generation* — arXiv:2410.05779
- Jimenez Gutierrez et al. (2024) — *HippoRAG: Neurobiologically inspired long-term memory* — NeurIPS
- Lee et al. (2024) — *A human-inspired reading agent with gist memory of very long contexts* — ICML
- Li et al. (2025) — *MemOS: An operating system for memory-augmented generation* — arXiv:2505.22101
- Maharana et al. (2024) — *Evaluating very long-term conversational memory of LLM agents* (LoCoMo) — ACL
- Packer et al. (2024) — *MemGPT: Towards LLMs as operating systems* — arXiv:2310.08560

## Related Digests

- [[hu-2026-evermemos]] — EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall
- [[li-2025-memos]] — MemOS: A Memory OS for AI System
- [[patel-2026-engram]] — ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents
- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents (the LoCoMo benchmark)

## Reviewer Notes

**Overall severity:** Minor fact tweak (corrected)

Two issues caught and fixed:

1. **Implications bullet on consolidation timing** previously claimed "+5.4 overall and +5.4 on temporal" for inactive vs rapid consolidation. The +5.4 figure is correct for the temporal category only (87.7 vs 82.3); the overall gap is **+2.4** (87.7 vs 85.3 in Table 2). Fixed inline. The TLDR's framing ("+5.4 on temporal... +6.2 on commonsense... +6.0 overall vs no-consolidation") was already correct — those numbers compare inactive against *no consolidation*, not against rapid.

2. **Author affiliation** — Yue Zhou (lead author) is at University of Illinois Chicago, not Amazon. The other three authors are at Amazon. Updated to "(Zhou et al., UIC + Amazon)" in the header and TLDR.

All other quantitative claims cross-checked and accurate:
- LoCoMo headline numbers (87.7 EM+SM, 59.9 Mem0, +27.8 absolute, 86.1 Full-Context, 79.8 ReadAgent, 54.5 HippoRAG, 52.6 RAG, 37.5 A-MEM, 29.6 Zep)
- Multi-hop gain vs FC (+3%), Temporal gain vs FC (+11%)
- Latency (3.21s vs 6.08s p90)
- Inactive vs no-consolidation overall (+6.0)
- Inactive vs rapid commonsense (+6.2)
- Compression rate 96.3% at k=2
- AgentIF constraint recall (47.4% Amory vs 36.8/27.8/25.1/23.9/21.3 for baselines)
- Sim-score ranges (0.08-0.29 agentic vs 0.49-0.59 embedder)
- Parameters T=20, N=10, k=2; model Claude 3.5 Sonnet V2
- All 7 prompt templates verbatim against the paper's appendix
