---
corpus: agentic-memory
kind: paper-digest
slug: k-2025-procedural-memory-benchmark
title: "A Benchmark for Procedural Memory Retrieval in Language Agents"
authors:
  - "Ishant K"
  - "Aswanth Krishnan"
year: 2025
publication_date: "2025-12"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2511.21730"
doi: null
arxiv_id: "2511.21730"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Embedding-based agent retrievers behave as bag-of-words memorizers and lose 25-42% MAP the moment query objects fall outside the corpus vocabulary, while a one-step LLM rewrite that strips object identities before embedding holds performance steady (-11% only) — proving that current single-stage retrieval pipelines structurally cannot separate procedural structure from surface tokens."
topics:
  - procedural-memory
  - retrieval-benchmarking
  - cross-context-generalization
  - ai-agents
  - alfworld
  - embedding-limits
  - llm-as-judge
tags:
  - paper
  - benchmark
  - agent-memory
  - retrieval
  - generalization
  - sentence-transformers
  - bm25
entities:
  - ishant-k
  - aswanth-krishnan
  - qpi-ai
related_digests:
  - wang-2025-mirix
  - patel-2026-engram
  - wang-2023-voyager-embodied-agent
  - ai-2026-memorybench-continual-learning
  - zhang-2024-llm-agent-memory-survey
citations:
  - title: "Reflexion: Language agents with verbal reinforcement learning"
    authors: ["Noah Shinn", "Joseph Cassano", "Aaron Labash", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2303.11366"
    arxiv_id: "2303.11366"
  - title: "Retrieval-augmented generation for knowledge-intensive nlp tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2005.11401"
    arxiv_id: "2005.11401"
  - title: "ALFWorld: Aligning text and embodied environments for interactive learning"
    authors: ["Mohit Shridhar", "Xingdi Yuan", "Marc-Alexandre Côté", "et al."]
    year: 2021
    venue: "ICLR"
    doi: null
    url: "https://arxiv.org/abs/2010.03768"
    arxiv_id: "2010.03768"
  - title: "AgentInstruct dataset"
    authors: ["zai-org"]
    year: 2024
    venue: "HuggingFace"
    doi: null
    url: "https://huggingface.co/datasets/zai-org/AgentInstruct"
    arxiv_id: null
  - title: "Memp: Exploring agent procedural memory"
    authors: ["Runnan Fang", "Yuan Liang", "Xiaobin Wang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2508.06433"
    arxiv_id: "2508.06433"
  - title: "LEGOMem: Modular procedural memory for multi-agent LLM systems for workflow automation"
    authors: ["Dongge Han", "Camille Couturier", "Daniel Madrigal Diaz", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2510.04851"
    arxiv_id: "2510.04851"
  - title: "Procedural memory is not all you need"
    authors: ["Andrew Wheeler", "Olivier Jeunen"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2505.03434"
    arxiv_id: "2505.03434"
  - title: "MIRIX: Multi-agent memory system for LLM-based agents"
    authors: ["Yu Wang", "Xi Chen"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2507.07957"
    arxiv_id: "2507.07957"
  - title: "Sentence-BERT: Sentence embeddings using siamese BERT-networks"
    authors: ["Nils Reimers", "Iryna Gurevych"]
    year: 2019
    venue: "EMNLP-IJCNLP"
    doi: null
    url: "https://arxiv.org/abs/1908.10084"
    arxiv_id: "1908.10084"
  - title: "The probabilistic relevance framework: BM25 and beyond"
    authors: ["Stephen Robertson", "Hugo Zaragoza"]
    year: 2009
    venue: "Foundations and Trends in Information Retrieval"
    doi: "10.1561/1500000019"
    url: null
    arxiv_id: null
  - title: "TRACE: Grounding time series in context for multimodal embedding and retrieval"
    authors: ["Jialin Chen", "Ziyu Zhao", "Gaukhar Nurbek", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2506.09114"
    arxiv_id: "2506.09114"
  - title: "Enhancing memory retrieval in generative agents through LLM-trained cross attention networks"
    authors: ["Yucheng Hong", "He He"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2402.11729"
    arxiv_id: "2402.11729"
  - title: "PAL-UI: Planning with active look-back for vision-based GUI agents"
    authors: ["Shuo Sun", "Lingfeng Yang", "Xingyao Wang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2510.00413"
    arxiv_id: "2510.00413"
  - title: "TrajAgent: An LLM-agent framework for trajectory modeling via large-and-small model collaboration"
    authors: ["Yuwei Du", "Jie Feng", "Jie Zhao", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2410.20445"
    arxiv_id: "2410.20445"
  - title: "Voyager: An open-ended embodied agent with large language models"
    authors: ["Guanzhong Wang", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2305.16291"
    arxiv_id: "2305.16291"
  - title: "A survey on memory mechanisms in LLM-based agents"
    authors: ["Yuan Zhang", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2404.13501"
    arxiv_id: "2404.13501"
  - title: "Trajectory prediction meets large language models: A survey"
    authors: ["Yi Xu", "Ruining Yang", "Yitian Zhang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2506.03408"
    arxiv_id: "2506.03408"
  - title: "ACON: Optimizing context compression for long-horizon LLM agents"
    authors: ["Minki Kang", "Wei-Ning Chen", "Dongge Han", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2510.00615"
    arxiv_id: "2510.00615"
  - title: "CoALA: Cognitive architectures for language agents"
    authors: ["Bosheng Ding", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2309.02427"
    arxiv_id: "2309.02427"
  - title: "Scaling laws for neural language models"
    authors: ["Jared Kaplan", "Sam McCandlish", "Tom Henighan", "et al."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/2001.08361"
    arxiv_id: "2001.08361"
  - title: "LangChain"
    authors: ["LangChain"]
    year: 2025
    venue: "GitHub repository"
    doi: null
    url: "https://github.com/langchain-ai/langchain"
    arxiv_id: null
  - title: "GPT-5 system card"
    authors: ["OpenAI"]
    year: 2025
    venue: "OpenAI"
    doi: null
    url: "https://openai.com/index/introducing-gpt-5/"
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Overview of the procedural retrieval problem and benchmark pipeline"
  page: 2
  image_path: "figures/k-2025-procedural-memory-benchmark-fig.png"
---

# A Benchmark for Procedural Memory Retrieval in Language Agents

**Authors:** Ishant K, Aswanth Krishnan (Qpi AI)
**Published:** 2025-12 · [Source](https://arxiv.org/abs/2511.21730)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Two Qpi AI researchers built the first benchmark that isolates **procedural memory retrieval** from end-to-end agent execution, then used it to show that today's standard embedding stack quietly fails on novel tasks. The setup: ALFWorld (text-based household tasks, 6 task types) with two corpora — 78 hand-coded expert trajectories and 336 GPT-4-generated AgentInstruct trajectories — plus a 40-query coverage-balanced query bank (15 EASY / 14 MEDIUM / 11 HARD) where every query is guaranteed 8-20 relevant trajectories. Six retrievers (action-only, enriched, summary, and combined embeddings using `all-MiniLM-L6-v2`; plus BM25 and Jaccard keyword baselines) are scored via GPT-5-as-judge with a relevance threshold of ≥6/10, calibrated against 200 hand-annotated query-trajectory pairs (human-LLM specificity 89.5%, Cohen's κ = 0.178). Two regimes are run: an 18-seen / 18-unseen exploratory split, then the 40-query coverage-balanced benchmark. The headline finding — the **generalization cliff** — is a 25-42% MAP drop on unseen-vocabulary queries and a full **rank inversion**: Combined Embeddings goes from #1 (MAP 0.844) to #3 (0.592), BM25 from #2 to #6, while LLM-generated procedural summaries climb from #6 (0.754) to #1 (0.671, only -11%). Ablations show that 4.3× more corpus data buys 27.7% MAP gain whereas 10× richer state-aware text buys only 9.9%, and the authors prove formally that mean-pooled sentence encoders treat trajectories as bags of words — so action-only beats state-aware on MEDIUM-complexity multi-step tasks because extra state tokens just dilute the signal. The actionable takeaway: don't bolt a vector DB onto your agent's procedural memory and call it done; preprocess trajectories with an LLM to strip object identities before embedding, or split retrieval into two stages (structure extraction → similarity).

## Key Takeaway

The hot take is that **the bottleneck on agent memory generalization is not the corpus, not the embedding model, and not even retrieval engineering — it's the mean-pooling step at the bottom of every sentence transformer**, which mathematically guarantees the encoder cannot tell `[take, heat, place]` apart from `[place, heat, take]`. So the fix that actually works isn't a better encoder or more data — it's a one-shot LLM rewrite *before* embedding that says "locate item → heat item → place in storage" and throws away every object name. That dumb-looking preprocessing step beats the cleverest embedding stack on novel-vocabulary tasks by 13 percentage points, because it does for free what the encoder structurally cannot.

## Implications

- **Stop treating your agent's procedural memory as a vector DB problem**: The paper shows the embedding model is the limiting factor, not the retrieval engine. If your agent stores past trajectories and uses cosine similarity to recall them, plan to lose 25-42% accuracy the moment a user asks something with new vocabulary — exactly when memory matters most.
- **Preprocess trajectories with an LLM before embedding, not after retrieval**: A single GPT-class summarization pass that strips object identities ("clean salt shaker" → "clean object") and keeps action order delivers the only retrieval method in the study that does NOT collapse under distribution shift. Generation-time abstraction is doing the work, not the embedder.
- **Corpus scale beats representation richness by ~3×**: A 4.3× corpus increase yields 27.7% MAP improvement; a 10× richer state-aware representation yields only 9.9%. If you have engineering hours to spend, spend them on collecting more diverse trajectories before you spend them on tweaking embedding inputs.
- **Don't trust "MAP improved on our held-out set" without a vocabulary-shift test**: The paper documents complete rank inversion between seen and unseen splits. A retriever that wins your benchmark may lose in production the first time vocabulary drifts. Always score retrieval on both in-vocab and out-of-vocab queries.
- **Action-only representations can beat richer ones on multi-step tasks**: On MEDIUM-complexity queries (state changes like heating, cleaning), action-only embeddings score 0.802 MAP vs. state-aware's 0.746 — because extra state tokens dilute the signal under mean pooling. When tasks are sequential, less context is more.
- **Use LLM-as-judge for procedural relevance, but treat it as a conservative lower bound**: GPT-5 at "low reasoning" with threshold ≥6/10 achieved 89.5% specificity against human annotators but only κ = 0.178 — humans recognize partial procedural utility that the LLM scores below threshold. So LLM-judge numbers are reliable for *relative* method ranking, not absolute capability claims.
- **Plan for the two-stage retrieval architecture the authors recommend**: Separate (1) procedural structure extraction from (2) similarity computation. The paper's own Summary Embeddings is a primitive version of this; future systems should make the split explicit rather than asking a single embedding to encode both content and order.
- **BM25 and lexical baselines remain competitive in stable-vocabulary settings**: BM25 scored 0.815 MAP on seen tasks — beating most embeddings. If your domain has bounded vocabulary (internal tools, fixed product catalog), the cheap option may still win; reserve embeddings for genuinely diverse text.

## How to Apply It (method)

**Scenario:** You're shipping a customer-support agent that remembers past tickets and retrieves similar resolutions to handle new ones. You want to know whether your current retrieval setup (sentence transformers + a vector DB) will generalize to next quarter's new product launch, where customer language and product names will be different from anything in your historical corpus.

**Steps:**

1. **Carve your existing ticket history into two query banks — "seen" and "unseen"**: From your last 12 months of resolved tickets, sample 18 tickets whose products and vocabulary appear frequently in the rest of the corpus (the "seen" set) and 18 tickets about a product line, region, or feature that the corpus barely covers (the "unseen" set). Confirm the vocabulary overlap on each set with a simple token-overlap script — the unseen set should have less than 5% lexical overlap with the corpus on average.

2. **Run a semantic-equivalence check on the two query banks** so any performance gap can't be blamed on "the unseen queries are just harder." Embed both sets with the same sentence transformer you use in production (e.g. `all-MiniLM-L6-v2` or `bge-small`), compute pairwise cosine similarity inside each bank and across banks, and verify the distributions overlap (small Cohen's *d*, near-zero silhouette score). If they don't, rebalance.

3. **Generate procedural summaries with an LLM for every ticket in your corpus** — a one-shot preprocessing pass that strips product names and customer identifiers and keeps only the action structure. Use a prompt like:

   ```
   Rewrite this support resolution as a procedure. Replace every product
   name, customer name, and concrete identifier with a generic role
   ("locate <item>", "verify <field>", "escalate to <team-type>"). Preserve
   the order and dependencies of the steps. Output only the rewritten
   procedure as a single arrow-separated sequence, no commentary.

   Resolution:
   {ticket_resolution_text}
   ```

4. **Build four parallel retrieval indexes over the corpus** so you can ablate cleanly: (a) action-only — just the agent actions, no surrounding context; (b) enriched — actions + ticket metadata + product info; (c) summary — your LLM-generated procedural summaries from step 3; (d) combined — enriched concatenated with the summary. Use the same embedding model and cosine similarity for all four.

5. **Score each index with an LLM-as-judge**: For each query in both query banks, retrieve top-K = 5 tickets per index, ask GPT-5 (or your preferred frontier model) to score each retrieved ticket on a 1-10 procedural-relevance scale with a one-line justification. Use a strict task-agnostic prompt:

   ```
   Score how procedurally similar the retrieved support resolution is to
   the query ticket, on a scale of 1-10. Procedural similarity means the
   same underlying sequence of steps and dependencies, even if the products,
   customer names, or system specifics differ. Score 6 or higher only if a
   support engineer could plausibly apply the retrieved resolution as a
   playbook for the query with minor object substitutions.

   Query: {query_ticket}
   Retrieved: {retrieved_ticket}

   Output: {"score": <1-10>, "reason": "<one line>"}
   ```

   Treat ≥6 as binary-relevant for MAP, Precision@5, Recall@5.

6. **Compute MAP on both query banks per index**: Calculate the generalization gap as `Gap = (MAP_seen − MAP_unseen) / MAP_seen` for each of the four indexes. The paper reports gaps of 11% (summary embeddings) to 42% (BM25/lexical) — anything in the 25-40% range tells you embeddings are memorizing your corpus vocabulary.

7. **Pick a deployment strategy based on the gap pattern**: If your unseen-set MAP holds up (low gap, like the summary embeddings did at 11%), ship the summary-embedding pipeline as the procedural memory layer. If you see a wide gap (>25%), accept that you need a two-stage architecture — keep the embedding index for fast in-vocabulary recall, but add an LLM rewrite step in front for novel queries, or fall back to enriched-context retrieval with explicit object replacement.

8. **Lock in a monthly re-evaluation cadence**: As new product lines launch, rebuild your "unseen" query bank from the latest weeks' tickets, rerun steps 5-6, and watch the gap. The benchmark is a maintenance tool, not a one-off audit — the moment your gap creeps above 30% is the moment your agent will start failing in production on novel cases.

**Expected outcome:** You will have a quantified, reproducible measurement of how badly your agent's procedural memory fails when customer vocabulary shifts, ranked across four alternative retrieval designs. You will also have a deployment-ready preprocessing pipeline (the LLM-generated procedural summaries) and a defensible answer to "will our memory system survive the next product launch" — backed by Gap and Robustness numbers, not vendor benchmarks. Crucially, you will discover whether your problem is embedding-bound (in which case generation-time abstraction wins) or corpus-bound (in which case you need to invest in trajectory collection, not retrieval engineering).

## Best Figure

![Figure 1 — Overview of the procedural retrieval problem and benchmark pipeline (page 2)](figures/k-2025-procedural-memory-benchmark-fig.png)

Image Candidates:
Figure 1 (p. 2): Single-page overview showing both the failure mode (embedding-based retrieval confusing CLEAN vs HEAT vs COOL under vocabulary shift) AND the benchmark pipeline that fixes the diagnosis — the whole paper in one diagram.
Table 1 (p. 11): The clearest evidence panel — six retrievers, seen vs unseen MAP, percentage drop, and the rank-reversal column showing Combined Embeddings 1→3 and Summary Embeddings 6→1.
Figure 2 (p. 8): Threshold sensitivity for LLM-as-judge — shows why ≥6 is the right cutoff (0% zero-relevant queries vs 50% at ≥10).

Best Image:
Figure Name: Figure 1: "Overview of the procedural retrieval problem and benchmark pipeline"
Figure Page: 2
Slide Caption: Embedding retrieval confuses transformation types under vocabulary shift; the benchmark pipeline isolates that failure for standardized procedural-retrieval evaluation.
Description: Figure 1 is a two-panel diagram. The left panel shows the failure mode: a corpus of two expert trajectories ("clean apple → place in cabinet" and "clean salt shaker → place in drawer") and a query ("wash a tomato → put it on the counter"). The embedding retriever, asked to find procedurally similar trajectories, returns instead "heat some plate → put on countertop" (WRONG transformation: HEAT ≠ CLEAN), "cool some lettuce → put it in the garbagecan" (WRONG: COOL ≠ CLEAN), and "first two laptops → put them on the bed" (missing the transformation step entirely) — all because they share lexical surface features with the query but encode completely different procedures. The right panel shows the benchmark pipeline that diagnoses this: representation formats (action-only vs state-aware), retrieval methods (embedding + summaries), an LLM judge calibrated by human annotators, and standard IR metrics (MAP, P@k, NDCG, R@k). The figure tells the whole paper's story in one view: the surface-feature failure mode on the left, the diagnostic apparatus on the right.

## What Experts Overlook

The detail most experts would miss is the **mean-pooling proof in §5.1** — a four-line piece of algebra showing that for any sentence transformer that aggregates token embeddings by mean pooling (i.e., every standard `all-MiniLM-L6-v2`-style encoder), the embedding of `[a₁ → a₂ → a₃]` is mathematically *identical* to the embedding of `[a₂ → a₁ → a₃]`, because mean pooling is permutation-invariant. The paper makes this visible by formalizing it (Equation 12) right after the empirical rank inversion — showing the failure isn't a bug to be tuned away, it's a structural property of the architecture. Positional encodings inside the transformer help during contextual encoding but get washed out by the final pool. This is why the authors don't recommend "use a better embedding model" — there is no embedding model in the `all-MiniLM` lineage that can fix this without abandoning mean pooling.

**Why it matters:** Every agent-memory architect implicitly assumes their vector store preserves "meaning" — and most assume "meaning" includes temporal order, because that's how humans read procedures. The paper proves the assumption is wrong at the mathematical level. Once you see this, the rest of the paper's findings stop being surprising and start being inevitable: of course richer state context (10× more tokens) only buys 9.9% MAP — you're adding more terms to a sum that throws away order anyway. Of course action-only beats state-aware on multi-step tasks — fewer terms in the sum means each action's contribution is louder, even though the order is still lost. The mean-pooling identity is the load-bearing observation; the cliff is its shadow.

**Example of good use:** A team building an agent that recalls past customer-support resolutions reads §5.1 and decides to put an LLM summarization step in front of their vector index, not behind it. They generate procedure-only summaries ("verify entitlement → locate logs → re-issue credentials") with object identifiers stripped, embed *those*, and retrieve. The cliff disappears because the LLM extracted the procedural structure into the text *before* the mean pool flattened it — the encoder is now handling structurally-typed input. Their unseen-vocabulary recall stops collapsing on new product launches.

**Example of misapplication:** A different team reads only the abstract and tries to fix the cliff by adding more context — they switch from action-only to state-aware embeddings, hoping the extra state tokens will give the encoder more signal. Per Table 2, this buys them 7 points on EASY tasks but *costs* them 5.6 points on MEDIUM-complexity multi-step tasks (state-aware 0.746 vs action-only 0.802), because mean pooling drowns out the action sequence under a flood of state tokens. They ship the "richer" representation, customer-support recall regresses on exactly the multi-step tickets that matter most (e.g., debugging chains, multi-step refunds), and they spend the next quarter chasing the regression through prompt engineering instead of fixing the encoder architecture.

## Extracted Prompts

**Prompt explanation:** LLM-as-judge scoring of retrieved trajectories against the query — described in §3.4.4 as "a single task-agnostic prompt stressing functional and procedural equivalence" with GPT-5 at low reasoning effort, output as a 1-10 graded relevance score with brief justification. Exact prompt text is not reproduced verbatim in the paper; only the configuration is.

```
No applicable prompts found in this paper. (The paper specifies LLM-as-judge configuration — GPT-5, reasoning_effort="low", 1-10 scale with justification, task-agnostic functional/procedural equivalence — but does not reproduce the verbatim prompt text. Summary-embedding generation also uses GPT-5 to produce object-agnostic procedural abstractions but the generation prompt is not included.)
```

## Citations

- **Shinn et al. (2023)** — Reflexion: Language agents with verbal reinforcement learning. [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)
- **Lewis et al. (2020)** — Retrieval-augmented generation for knowledge-intensive NLP tasks. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
- **Shridhar et al. (2021)** — ALFWorld: Aligning text and embodied environments for interactive learning. ICLR. [arXiv:2010.03768](https://arxiv.org/abs/2010.03768)
- **zai-org (2024)** — AgentInstruct dataset. HuggingFace.
- **Fang et al. (2025)** — Memp: Exploring agent procedural memory. [arXiv:2508.06433](https://arxiv.org/abs/2508.06433)
- **Han et al. (2025)** — LEGOMem: Modular procedural memory for multi-agent LLM systems. [arXiv:2510.04851](https://arxiv.org/abs/2510.04851)
- **Wheeler & Jeunen (2025)** — Procedural memory is not all you need. [arXiv:2505.03434](https://arxiv.org/abs/2505.03434)
- **Wang & Chen (2025)** — MIRIX: Multi-agent memory system for LLM-based agents. [arXiv:2507.07957](https://arxiv.org/abs/2507.07957)
- **Reimers & Gurevych (2019)** — Sentence-BERT. EMNLP-IJCNLP. [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- **Robertson & Zaragoza (2009)** — The probabilistic relevance framework: BM25 and beyond. Foundations and Trends in IR.

(Full 21-entry citation list in frontmatter `citations:` field.)

## Related Digests

- [[wang-2025-mirix]] — MIRIX: Multi-Agent Memory System for LLM-Based Agents (six cognitively-typed memory components including procedural — direct precursor to the typed-memory hypothesis this paper validates)
- [[patel-2026-engram]] — ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents (typed write-time partitioning of episodic/semantic/procedural buckets — same convergence on "structure-before-similarity")
- [[wang-2023-voyager-embodied-agent]] — Voyager: skill library as executable-code procedural memory for Minecraft (the original procedural-memory-via-skill-store reference cited in §2.3)
- [[ai-2026-memorybench-continual-learning]] — MemoryBench: BM25-over-raw-sessions Pareto-dominates SOTA memory systems on procedural memory — strongly converges with this paper's "corpus-scale > representation enrichment" ablation
- [[zhang-2024-llm-agent-memory-survey]] — A Survey on Memory Mechanisms of LLM-Based Agents (the survey the paper cites for the gap it fills — no existing benchmark isolates retrieval quality from end-to-end task success)

## Reviewer Notes

**Overall severity:** Clean

All numerical claims, method descriptions, and architectural arguments in the digest are supported by the paper. Verified: 78 expert trajectories (§3.2.1), 336 AgentInstruct trajectories (§3.2.2), 4.3× scale ratio (§3.2.2), 40-query coverage-balanced benchmark with 15/14/11 EASY/MEDIUM/HARD split (§3.4.2), six retrieval methods (§3.3), GPT-5 judge at threshold ≥6 with 89.5% specificity and Cohen's κ = 0.178 (§4.4.3), all-MiniLM-L6-v2 with 384-dim embeddings and ChromaDB (§3.3.1), 25-40% generalization gap (§5.1), exact MAP values from Tables 1-3 (Combined 0.844→0.592, BM25 0.815→0.469, Summary 0.754→0.671, state-aware MAP 0.7945 on EASY 0.842 MEDIUM 0.746 HARD 0.791, action-only MAP 0.7231 on EASY 0.668 MEDIUM 0.802 HARD 0.699, 27.7% corpus-scale gain vs 9.9% representation gain). Mean-pooling permutation-invariance proof verified at Equation 12 (§5.1). Rank inversion 1→3 / 6→1 verified in Table 1 column "Rank Reversal."

One minor characterization to flag in future digests: the paper says BM25 was *excluded* from the coverage-balanced benchmark (§4.2) due to information leakage from the keyword-based coverage filter, so BM25's "rank 6 on unseen" result is from the exploratory 78-trajectory regime only, not the coverage-balanced one. The digest body correctly contextualizes this in the TLDR ("Two regimes are run...") but a careless reader might conflate the two regimes. Not a fact error in the digest — just a place where readers could misinterpret.
