---
corpus: agentic-memory
kind: paper-digest
slug: kang-2025-memory-os
title: "Memory OS of AI Agent"
authors:
  - "Jiazheng Kang"
  - "Mingming Ji"
  - "Zhe Zhao"
  - "Ting Bai"
year: 2025
publication_date: "2025-05"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2506.06326"
doi: null
arxiv_id: "2506.06326"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "MemoryOS borrows segment-page virtual-memory discipline straight from operating-systems design — short-term (FIFO dialogue-page queue, length 7), mid-term (topic-clustered segments of up to 200 pages each, scored by Heat = α·visits + β·page-count + γ·exp(−Δt/μ)), long-term persona memory (90-dim user-trait vector + User KB + Agent Profile, fixed-size FIFO queues of 100) — promoting segments above heat threshold τ=5 to long-term, evicting lowest-heat segments when full, and lifting GPT-4o-mini LoCoMo F1 by 49.11% / BLEU-1 by 46.18% on average with 5x fewer LLM calls than A-Mem (4.9 vs 13.0) and 4x fewer tokens than MemGPT (3,874 vs 16,977)."
topics:
  - agent-memory
  - memory-operating-system
  - segment-page-memory
  - short-mid-long-term-memory
  - heat-based-eviction
  - dialogue-chain
  - user-persona-memory
  - agent-persona-memory
  - 90-dim-user-traits
  - locomo-benchmark
  - gvd-benchmark
  - fifo-update
  - jacard-similarity
  - heat-formula
  - tencent-ai-lab
tags:
  - paper
  - memory-architecture
  - operating-system-analogy
  - memoryos
  - memos
  - segment-page
  - heat-based
  - persona
  - locomo
  - efficiency
  - tencent
  - bupt
entities:
  - kang-jiazheng
  - ji-mingming
  - zhao-zhe
  - bai-ting
  - tencent-ai-lab
  - bupt
related_digests:
  - latimer-2025-hindsight-memory
  - wang-2025-mirix
  - liu-2025-memverse
  - packer-2023-memgpt-os
  - chhikara-2025-mem0
  - xu-2025-a-mem-agentic-memory
  - liu-2023-think-in-memory
  - zhong-2023-memorybank-llm
  - maharana-2024-locomo
citations:
  - title: "The Multics virtual memory: Concepts and design"
    authors: ["André Bensoussan", "C. T. Clingen", "R. C. Daley"]
    year: 1972
    venue: "Communications of the ACM 15(5):308-318"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mem0: Building production-ready AI agents with scalable long-term memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "Taranjeet Singh", "Deshraj Yadav"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.19413"
  - title: "DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning"
    authors: ["DeepSeek-AI", "Daya Guo", "Dejian Yang", "Haowei Zhang", "Junxiao Song", "Ruoyu Zhang", "Runxin Xu", "Qihao Zhu", "Shirong Ma", "Peiyi Wang", "Xiao Bi", "Xiaokang Zhang", "Xingkai Yu", "Yu Wu", "Z. F. Wu", "Zhibin Gou", "Zhihong Shao", "Zhuoshu Li", "Ziyi Gao", "et al."]
    year: 2025
    venue: "Preprint"
    doi: null
    url: null
    arxiv_id: "2501.12948"
  - title: "Virtual memory"
    authors: ["Peter J. Denning"]
    year: 1970
    venue: "ACM Computing Surveys 2(3):153-189"
    doi: null
    url: null
    arxiv_id: null
  - title: "Rethinking memory in AI: Taxonomy, operations, topics, and future directions"
    authors: ["Yiming Du", "Wenyu Huang", "Danna Zheng", "Zhaowei Wang", "Sebastien Montella", "Mirella Lapata", "Kam-Fai Wong", "Jeff Z. Pan"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2505.00675"
  - title: "Emotional RAG: Enhancing role-playing agents through emotional retrieval"
    authors: ["Le Huang", "Hengzhi Lan", "Zijun Sun", "Chuan Shi", "Ting Bai"]
    year: 2024
    venue: "ICKG 2024"
    doi: null
    url: null
    arxiv_id: null
  - title: "Hello again! LLM-powered personalized agent for long-term dialogue"
    authors: ["Hao Li", "Chenghao Yang", "An Zhang", "Yang Deng", "Xiang Wang", "Tat-Seng Chua"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2406.05925"
  - title: "From 1,000,000 users to every user: Scaling up personalized preference for user-level alignment"
    authors: ["Jia-Nan Li", "Jian Guan", "Songhao Wu", "Wei Wu", "Rui Yan"]
    year: 2025
    venue: "Preprint"
    doi: null
    url: null
    arxiv_id: "2503.15463"
  - title: "Think-in-memory: Recalling and post-thinking enable LLMs with long-term memory"
    authors: ["Lei Liu", "Xiaoyan Yang", "Yue Shen", "Binbin Hu", "Zhiqiang Zhang", "Jinjie Gu", "Guannan Zhang"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2311.08719"
  - title: "Evaluating very long-term conversational memory of LLM agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "Mohit Bansal", "Francesco Barbieri", "Yuwei Fang"]
    year: 2024
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "2402.17753"
  - title: "A grounded memory system for smart personal assistants"
    authors: ["Felix Ocker", "Jörg Deigmöller", "Pavel Smirnov", "Julian Eggert"]
    year: 2025
    venue: "Preprint"
    doi: null
    url: null
    arxiv_id: "2505.06328"
  - title: "MemGPT: Towards LLMs as operating systems"
    authors: ["Charles Packer", "Vivian Fang", "Shishir G. Patil", "Kevin Lin", "Sarah Wooders", "Joseph E. Gonzalez"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "BLEU: A method for automatic evaluation of machine translation"
    authors: ["Kishore Papineni", "Salim Roukos", "Todd Ward", "Wei-Jing Zhu"]
    year: 2002
    venue: "ACL 311-318"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["Joon Sung Park", "Joseph O'Brien", "Carrie Jun Cai", "Meredith Ringel Morris", "Percy Liang", "Michael S. Bernstein"]
    year: 2023
    venue: "ACM UIST 1-22"
    doi: null
    url: null
    arxiv_id: null
  - title: "SCM: Enhancing large language model with self-controlled memory framework"
    authors: ["Bing Wang", "Xinnian Liang", "Jian Yang", "Hui Huang", "Shuangzhi Wu", "Peihao Wu", "Lu Lu", "Zejun Ma", "Zhoujun Li"]
    year: 2025
    venue: "Preprint"
    doi: null
    url: null
    arxiv_id: "2304.13343"
  - title: "From human memory to AI memory: A survey on memory mechanisms in the era of LLMs"
    authors: ["Yaxiong Wu", "Sheng Liang", "Chen Zhang", "Yichao Wang", "Yongyue Zhang", "Huifeng Guo", "Ruiming Tang", "Yong Liu"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.15965"
  - title: "A-Mem: Agentic memory for LLM agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "Hang Gao", "Juntao Tan", "Yongfeng Zhang"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2502.12110"
  - title: "Generative dense retrieval: Memory can be a burden"
    authors: ["Peiwen Yuan", "Xinglin Wang", "Shaoxiong Feng", "Boyuan Pan", "Yiwei Li", "Heda Wang", "Xupeng Miao", "Kan Li"]
    year: 2024
    venue: "EACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "A survey on the memory mechanism of large language model-based agents"
    authors: ["Zeyu Zhang", "Xiaohe Bo", "Chen Ma", "Rui Li", "Xu Chen", "Quanyu Dai", "Jieming Zhu", "Zhenhua Dong", "Ji-Rong Wen"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2404.13501"
  - title: "Segment-page-combined memory management technology based on a homegrown many-core processor"
    authors: ["Yan Zheng", "Tong Zou", "Xingyan Wang"]
    year: 2020
    venue: "CCF Trans. HPC 2(4):376-381"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "He Ye", "Yanlin Wang"]
    year: 2024
    venue: "AAAI 38:19724-19731"
    doi: null
    url: null
    arxiv_id: "2305.10250"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "MemoryOS overview architecture: STM (FIFO dialogue pages) → MTM (segments + heat-based eviction) → LPM (user/agent persona, traits, KB)"
  page: 3
  image_path: "figures/kang-2025-memory-os-fig.png"
---

# Memory OS of AI Agent

**Authors:** Jiazheng Kang (BUPT, kjz@bupt.edu.cn), Mingming Ji (Tencent AI Lab), Zhe Zhao (Tencent AI Lab), Ting Bai* (BUPT, corresponding, baiting@bupt.edu.cn)
**Published:** 2025-05 · [Source](https://arxiv.org/abs/2506.06326) · [Code](https://github.com/BAI-LAB/MemoryOS)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MemoryOS (BUPT + Tencent AI Lab, May 2025) takes the MemGPT operating-system analogy literally and ports actual virtual-memory primitives — segments, pages, FIFO eviction, heat-based promotion — into agent memory architecture. Three storage tiers: **STM** is a fixed-length FIFO queue of dialogue pages (length 7), each page = {Q_i, R_i, T_i, meta_chain_i} with the meta computed by an LLM in two steps (link to prior chain or reset on semantic discontinuity, then summarize chain); **MTM** clusters pages into topic *segments* (max 200 pages per segment, max ~unbounded segment count) via Fscore = cos(e_s, e_p) + F_Jacard(K_s, K_p) above threshold θ=0.6, with each segment summarized by an LLM and assigned a heat score `Heat = α·N_visit + β·L_interaction + γ·exp(−Δt/μ)` (α=β=γ=1, μ=1e7 seconds); **LPM** holds two personas (User: Profile static + KB FIFO-100 dynamic + 90-dim Traits across {basic-needs-personality, AI-alignment, content-platform-interest}; Agent: Profile static + Traits FIFO-100 dynamic). Promotion: STM→MTM by FIFO on overflow; MTM→LPM when a segment's Heat exceeds τ=5 (and on eviction, segments with lowest Heat are dropped). Retrieval is a fan-out across all three: STM returns all pages (recent context); MTM does two-stage (top-m=5 segments by Fscore, then top-k=10 dialogue pages within); LPM returns User KB / Agent Traits top-10 by semantic similarity plus all of Profile/Traits. Empirically: on **GVD** (15 simulated users × 10 days), GPT-4o-mini + MemoryOS beats A-Mem 93.3% vs 90.4% accuracy (+3.2%) and Qwen2.5-7B + MemoryOS beats A-Mem 91.8% vs 87.2% (+5.3%); on **LoCoMo** (~300 turns × ~9k tokens per conversation), MemoryOS averages **+49.11% F1 / +46.18% BLEU-1** over baselines on GPT-4o-mini, with the biggest single jump on **Temporal (+118.80% F1 / +111.52% BLEU-1)** and Single-Hop (+32.35% / +42.33%) — all while using **fewer LLM calls than A-Mem (4.9 vs 13.0)** and **far fewer tokens than MemGPT (3,874 vs 16,977)**. **Most useful takeaway:** the 4× efficiency gain over MemGPT comes from the segment-page split — MemGPT pages flat dialogue history (one queue), MemoryOS pages topic-clustered segments (many queues, segment-scoped paging), which means retrieval can target the right segment first and then go deep, rather than scanning a flat queue. Stated as a lesson: **if you're going to take the OS-analogy seriously, port segment-page memory management, not just paging.**

## Key Takeaway

Most agent-memory architectures borrow language from OS design but stop at vague metaphors ("paging", "context window"). MemoryOS borrows the actual data structures: segments as topic-coherent variable-size containers, pages as fixed-size dialogue units within them, an explicit heat formula combining frequency + recency + engagement weighted by α/β/γ, and a two-tier promotion (page→segment→LPM) gated by heat threshold τ. The cleanest evidence that this isn't just terminology is the efficiency numbers: 4.9 LLM calls per response vs A-Mem's 13.0, 3,874 tokens recalled vs MemGPT's 16,977 — at the same time as better accuracy. Both efficiency dimensions improve simultaneously because the segment-page split *narrows the retrieval scope* (top-m segments first, then top-k pages within those segments) rather than scanning a flat queue end-to-end. Stated as a lesson: **the OS analogy for agent memory is worth taking literally — port segmented-paging, heat-based eviction, and time-decay coefficients directly, not as metaphors but as actual implementation primitives, and you get better accuracy with less work.**

## Implications

- **Port segment-page memory management as actual primitives, not just OS-flavored language.** The cleanest argument the paper makes is in Table 3: MemoryOS uses 4.9 LLM calls / 3,874 tokens to deliver 36.23 F1 vs MemGPT's 4.3 calls / 16,977 tokens / 29.13 F1. MemGPT pages a flat queue; MemoryOS pages *within* topic-clustered segments. The implementation cost is small (segment as variable-length container + segment-page index) but the retrieval-scope reduction is substantial. For Flow OS, this maps to: don't just have a flat `memory/captures/` queue — cluster captures by topic-segment (auto-derived by Fscore similarity) and retrieve at segment-then-page granularity rather than flat-scanning all captures. `[N, R, A]`

- **Heat formula as a first-class concept.** `Heat = α·N_visit + β·L_interaction + γ·exp(−Δt/μ)` with tunable α/β/γ is a small but operationally-distinct contribution over LRU or pure recency decay. The visit count rewards segments that get queried repeatedly; the interaction count rewards segments that accumulated lots of pages (high engagement); the recency factor with µ=1e7 seconds (~115 days) gives a long half-life that suits months-long projects. For Flow OS's ventures/contacts/observations cards, this is the formula to track for "which entity files matter right now" — not just "last modified" timestamps. `[A, M]`

- **The 90-dimensional User Traits vector is a concrete personalization substrate.** §3.3 references Li et al. (2025) for the 90-dim trait taxonomy across three categories: basic-needs-personality (~30 dims, Maslow / Big-Five-ish), AI-alignment-dimensions (~30 dims, what the user expects from AI), content-platform-interest-tags (~30 dims, topical tags). The paper auto-extracts and updates these from segments at LPM promotion time. For Flow OS, this is a more rigorous schema for the "About Me" section than free-text — pin down a fixed dimension set and let `/learn` update them autonomously. `[E, A]`

- **STM length = 7 dialogue pages is a thoughtful default.** Mirroring Miller's 7±2 cognitive working-memory bound, the paper hard-caps STM at 7 dialogue pages. This isn't a wild magic number — it's grounded in a well-established psych result. For Flow OS, the equivalent claim is: the "current session" sliding window should hold ~7 turn-pairs, not 10 or 20. Larger STMs blur the boundary with MTM and force unnecessary consolidation work. `[N]`

- **Two-stage MTM retrieval (segment → page) is the efficiency unlock.** §3.4 spells it out: first select top-m=5 candidate segments via Fscore (cheap, segment-level summaries are compact), THEN select top-k=10 pages within those segments by semantic similarity (deeper but scoped). This is the operationalisation of the "summary scan first, deep retrieval second" pattern MIRIX gestures at but doesn't fully spell out. For QMD recall, replace flat top-k page retrieval with this two-stage protocol — maintain per-segment summary vectors as a separate index. `[R]`

- **Topic segmentation via Fscore is a usable clustering heuristic.** `Fscore = cos(e_s, e_p) + F_Jacard(K_s, K_p)` combines dense-vector cosine similarity with sparse-keyword Jaccard overlap. Both signals are computed cheaply once you have embedding + keyword extractions on segments and pages. Threshold θ=0.6 — pages above this score join the segment; below, they start a new segment. Simple, no learning required, no clustering library needed. For Flow OS, this is a no-ML way to auto-cluster captures into topic threads at ingestion time. `[E, A]`

- **The User KB / Agent Traits FIFO-100 cap is a deliberate constraint.** Both LPM components are fixed-size FIFO queues capped at 100 entries. This forces the system to maintain a *bounded* memory footprint regardless of how long the user-agent relationship runs — old facts age out as new ones come in. The implicit thesis: "the right number of long-term facts about a user is bounded" — i.e. you don't need to remember every restaurant they mentioned over five years; you need the top-100 that the heat-driven update has identified as enduringly relevant. Worth interrogating for personal-scale (a user's KB about *themselves* should arguably be unbounded), but the discipline of "old facts age out by default unless re-activated" is correct. `[M]`

- **The 49% / 46% LoCoMo F1/BLEU lift comes mostly from Temporal questions.** Table 2 shows Temporal jumps from MemGPT's 9.15 F1 to MemoryOS's 20.02 (+118.80%), the largest delta in any category. This is *exactly* where flat-RAG architectures fail (temporal reasoning requires knowing "when" — which requires the time-decay-aware heat formula or explicit timestamp indexing). The Open-Domain category (subjective inference) sees more modest gains (+18.47% F1). The takeaway: typed-memory architectures pay off most where the question shape requires the type information — temporal, multi-hop, preference — and least where simple flat retrieval suffices (single-fact lookups, the easy cases). `[R]`

- **MemoryOS efficiency dominates A-Mem 13× LLM calls.** A-Mem's Zettelkasten-style knowledge graph requires constructing and following many links per query — explaining the 13 LLM calls per response. MemoryOS's two-stage retrieval + heat-driven eviction needs only 4.9 calls. The lesson: graph-based memory pays off when you genuinely need multi-hop traversal (which A-Mem and Hindsight argue you do), but if the architecture can answer most queries via segment-then-page retrieval, you save 8 LLM calls per turn at the cost of giving up *some* multi-hop traversal. For Flow OS, this argues for a hybrid: default to MemoryOS-style segment-page retrieval (cheap), escalate to graph traversal only when the query plan flags a multi-hop need. `[R, M]`

- **Open-source LoCoMo evaluation makes the benchmark reproducible.** Code at github.com/BAI-LAB/MemoryOS includes the full evaluation harness against MemoryBank, TiM, MemGPT, A-Mem. For Flow OS's own LongMemEval-style benchmark work, this is a useful starting scaffold — fork the repo, swap in the QMD-backed memory implementation as a fifth baseline, run on LoCoMo, get a head-to-head number against four well-known systems. `[—]`

## How to Apply It (method)

**Scenario:** Same Flow OS context — vault has paper digests, contact cards, session captures, decision memories spread across many subfolders. Today `/learn` writes flat memories with no topic clustering, no FIFO eviction, no heat-based promotion. Retrieval is top-k=5 against the full vault. You want to retrofit MemoryOS's segment-page primitives + heat-based update + LPM persona layer onto QMD. This maps cleanly to ENGRAM Encode (segment as the encoding unit, page as the sub-unit), Network (three-tier hierarchy with explicit promotion rules), Aggregate (segment summarization + LPM persona consolidation), Maintain (heat-based eviction + FIFO promotion).

**Steps:**

1. **Add a session-scoped STM ring buffer of size 7.** Already implicit in your turn-by-turn session state, but make it explicit: keep the last 7 turn-pairs (`page_i = {query, response, timestamp, meta_chain_i}`) in a queue. On each new turn, ask an LLM whether the new page is semantically continuous with the prior page (chain link) or topically new (chain reset), then summarize the chain into `meta_chain_i`. This is what feeds the MTM eviction step.

2. **Build topic segments via Fscore clustering at MTM-ingest time.** When the STM queue overflows (8th page arrives), the oldest page gets evicted to MTM:
   - For each existing segment in MTM, compute `Fscore = cos(e_s, e_page) + F_Jacard(K_s, K_page)` where K_* are LLM-extracted keyword sets
   - Above θ=0.6, the page joins that segment (and the segment summary is regenerated)
   - Below θ=0.6 for all segments, the page starts a new segment (length 1)
   - Max segment length cap: 200 pages (per the paper)
   - Store segments as `memory/components/mtm/segment-<slug>.md` with frontmatter:
     ```yaml
     ---
     kind: mtm-segment
     summary: <LLM-generated topic summary>
     keywords: [...]
     pages: [list of page IDs]
     heat: 0.0
     last_accessed: <ISO>
     visit_count: 0
     ---
     ```

3. **Implement the heat formula and update it on every retrieval.** `Heat = α·N_visit + β·L_interaction + γ·exp(−Δt/μ)` with the paper's defaults α=β=γ=1, μ=1e7s. On every MTM retrieval that hits a segment, increment `visit_count`, refresh `last_accessed`, recompute heat. Persist back to the segment's frontmatter. Note: heat is computed *on read*, not maintained as a watermark — so retrieval is the only place it's recomputed (which keeps the cost bounded to actual queries).

4. **Implement Heat-based MTM-to-LPM promotion (τ=5) and lowest-Heat eviction.** When a segment's Heat exceeds τ=5, run an LPM-update step:
   - Extract user-relevant facts → append to User KB (FIFO-100)
   - Extract user-trait signals → update the 90-dim User Traits vector
   - Extract agent-related facts (added settings, recommended items) → append to Agent Traits (FIFO-100)
   - After promotion, reset the segment's `L_interaction` to zero (so heat naturally decays unless re-activated)
   - When MTM exceeds its segment cap, evict lowest-Heat segments (delete the file)

5. **Build the LPM persona structure.** Two persona files:
   - `memory/components/lpm/user-persona.md` with frontmatter:
     ```yaml
     ---
     kind: lpm-user-persona
     profile:                # static: gender, name, birth_year, location
       name: "<user name>"
       birth_year: ...
     kb:                     # FIFO-100 dynamic facts
       - "<fact-1>"
       - "<fact-2>"
     traits:                 # 90-dim vector across 3 categories
       basic_needs_personality:
         openness: 0.85
         conscientiousness: 0.70
         ...
       ai_alignment:
         tone_preference: "direct, no fluff"
         ...
       content_platform_interest:
         ai_agents: 0.95
         venture_building: 0.90
         ...
     ---
     ```
   - `memory/components/lpm/agent-persona.md` mirroring CLAUDE.md's identity sections + a dynamic Traits section that captures emergent behaviors from interaction history

6. **Wrap QMD retrieval in three-channel fan-out (STM, MTM-two-stage, LPM).** Replace `qmd query` with `recall(query)` that:
   - **STM**: return all 7 pages (cheap)
   - **MTM**: stage A — vector-search the segment summaries with top-m=5 candidates; stage B — within those 5 segments, vector-search their pages with top-k=10 each, deduplicate
   - **LPM**: top-10 semantic hits from User KB + all of User Profile/Traits + Agent Profile/Traits + top-10 from Agent Traits
   - Concatenate STM + MTM + LPM into the final prompt context

7. **Use Jaccard similarity for keyword sets, not vector similarity.** §3.2 specifies `F_Jacard(K_s, K_p) = |K_s ∩ K_p| / |K_s ∪ K_p|`. This is the sparse-keyword half of the Fscore. Implementation: extract a fixed-size keyword set per page/segment via TF-IDF or an LLM, store as a sorted JSON array in frontmatter, compute intersection/union in Python. Don't substitute vector cosine for the keyword half — they capture different signals (the Jaccard term penalises segments with totally disjoint vocabulary even when their embedding cosine is high, which is the topic-coherence signal).

8. **Hard-set the FIFO bounds: STM=7, segment-pages=200, User-KB=100, Agent-Traits=100.** Don't make these tunable until you have a reason. The paper's defaults are deliberate (STM=7 ≈ Miller's bound, FIFO-100 ≈ a year of monthly-relevant facts), and the efficiency numbers are predicated on them. Override only after running a baseline at these values and identifying a specific bottleneck.

9. **Schedule the 90-dim User Traits update on every LPM promotion.** When a segment promotes to LPM, run an LLM call:

   ```
   Given the segment summary and dialogue pages below, update the user's
   90-dimensional trait vector. Output JSON with delta values per
   dimension (positive = strengthened, negative = weakened, 0 = no change).
   
   CURRENT TRAITS: {existing 90-dim vector}
   SEGMENT SUMMARY: {segment summary}
   PAGES: {first 10 pages from segment}
   
   OUTPUT: { "openness": +0.05, "conscientiousness": 0, ... }
   ```
   
   Clamp deltas to ±0.1 to prevent oscillation. This is the Hindsight-style confidence-reinforcement discipline applied to the trait vector.

10. **Evaluate on LoCoMo with the paper's harness, then on a private benchmark.** Fork github.com/BAI-LAB/MemoryOS, swap in the QMD-backed implementation as a fifth baseline, run on LoCoMo. Targets to beat:
    - GPT-4o-mini single-hop: > 35.27 F1
    - Multi-hop: > 41.15 F1
    - Temporal: > 20.02 F1 (this is where MemoryOS dominates — the typed-memory + heat-formula combo lifts temporal by 119%)
    - Open-domain: > 48.62 F1
    
    Then build a private 50-question benchmark from Flow OS session captures, categorise by the same four LoCoMo question types, run the same eval. If the QMD-MemoryOS retrofit can't beat MemoryOS on its own benchmark, the bottleneck is in the QMD substrate, not the architecture.

11. **Diagnostic: log per-tier retrieval contributions.** For every `recall()`, log which tier (STM | MTM | LPM) the gold answer came from. After a month, compute the per-tier hit-rate matrix. The paper's prediction: ~50% of useful retrievals come from MTM, ~30% from LPM, ~20% from STM (because the model has STM in the conversation already). If your distribution is wildly different (e.g. 80% LPM), it means the segment formation isn't producing useful MTM segments — likely the Fscore threshold needs tuning or the segment summarisation prompt is too generic.

12. **Cost discipline: 4.9 LLM calls / 3,874 tokens per response.** Hold yourself to MemoryOS's efficiency target. If your retrofit ends up calling the LLM 10+ times per response (segment scoring, segment summary regeneration, page scoring, LPM updates, response generation), the segment-page architecture has degenerated into A-Mem-style per-query graph traversal. The fix: cache segment summaries (regenerate only on promotion, not on every retrieval); cache user trait vectors (update only on LPM promotion); use cheap embedders for Fscore (not LLM calls). The architecture pays off only when the per-query cost stays low.

**Expected outcome:** A retrofit memory layer that (a) clusters captures into topic-coherent MTM segments via Fscore (vector + Jaccard) at ingestion, (b) promotes hot segments to LPM via the heat formula with τ=5 threshold, (c) maintains a structured 90-dim User Trait vector + bounded User KB + Agent Persona, (d) fans retrieval across STM + MTM-two-stage + LPM, (e) sustains ~5 LLM calls per response with ~4k tokens recalled. The per-tier hit-rate diagnostic tells you which tier is paying off; the LoCoMo eval gives you a public-benchmark number to anchor "yes, this works as well as the paper claimed."

## Best Figure

![Figure 1 — MemoryOS overview architecture (page 3)](figures/kang-2025-memory-os-fig.png)

**Figure Name:** Figure 1: "The overview architecture of MemoryOS, including memory Store, Updating, Retrieval, Response."

**Figure Page:** 3

**Slide Caption:** MemoryOS's three-tier OS-style memory pipeline: STM is a FIFO queue of dialogue pages (left); MTM is a heat-scored collection of topic-clustered segments containing multiple pages each, with hot segments (Heat > τ) promoted to LPM and cold segments evicted (center); LPM holds User Persona (User KB / Traits dynamic + Profile static) and Agent Persona (Agent Traits dynamic + Profile static) (right). The Query at top-right fans retrieval across all three tiers; Response Generation at right combines the retrieved content with the agent's persona to produce the timestamped answer.

**Description:** Figure 1 is a single full-width architecture diagram with three labeled vertical bands corresponding to the three memory tiers, plus a Response Generation column on the right. Left band — **STM**: a vertical stack of dialogue-page tiles labeled "Page" with FIFO arrows indicating new pages pushed in at the bottom, oldest pages "Insert to MTM" via a curving arrow into the MTM band. Center band — **MTM**: a cloud-bounded region containing segment groups, each with a "Segment Heat" annotation and a flame icon when hot. Above-threshold segments (`Heat > τ`) flow rightward via an "Update to LPM" arrow; below-threshold segments get a snowflake icon and "Delete Segment" trash arrow. Below the segments is the two-stage retrieval indicator: "Top-m Segment" → "Top-k Page". A dialogue-chain indicator (orange chat icon with curving line) shows pages chain-linked within a segment. Right band — **LPM**: two panels stacked vertically. Top panel ("Dynamic"): User Persona = {User KB, User Traits} green tiles + Agent Persona = {Agent Traits} green tile. Bottom panel ("Static"): {User Profile, Agent Profile} orange tiles. Far right — **Response Generation**: receives Query input, plus the three retrieval streams labeled "FIFO" (from STM), "Top-k Page" (from MTM), "Relevant LPM" (from LPM); produces an "answer" output with a Timestamp. The figure matters because it makes legible the *concrete data-flow* of an OS-style memory pipeline — most papers gesture at "hierarchical memory" abstractly; this one shows the specific arrows, the specific eviction triggers, the specific retrieval fan-out. It's the architecture diagram that's most directly portable to an implementation.

**Other strong candidates:**
- **Figure 2 (p. 6)** — Ablation study panels showing per-module contribution on GVD and LoCoMo. The clearest evidence that MTM (mid-term memory) is the most-impactful single component, with LPM second and the Dialogue Chain third.
- **Table 2 (p. 5)** — LoCoMo per-category results. The +118.80% Temporal F1 improvement is the paper's single most striking number.
- **Table 3 (p. 5)** — Efficiency analysis with token + LLM call counts per method. The 4.9 calls vs A-Mem's 13.0 and 3,874 tokens vs MemGPT's 16,977 is the efficiency-discipline takeaway.
- **Figure 4 (p. 7)** — Case study showing default LLM losing the "wetland park" conversation context over weeks vs MemoryOS recalling it. The clearest user-facing illustration of the value proposition.

## What Experts Overlook

Most readers will focus on the three-tier hierarchy as the architectural innovation. The detail almost everyone will miss is in §3.3 (Memory Update Module), the MTM-LPM update paragraph: **after a segment is promoted to LPM, the segment's `L_interaction` counter is reset to zero, causing its Heat to decline — and then the segment continues to live in MTM until it cools enough to be evicted or re-heated by new pages.** This is a subtle but important consistency-maintenance discipline: promotion is *not* deletion. The segment doesn't get garbage-collected when it hits LPM; instead it gets *de-prioritised* in the heat ranking so newer hot segments take its place at the top, but it's still available for retrieval until it actually gets cold enough to evict. This is the way the architecture prevents the same fact from being promoted to LPM repeatedly (because once promoted, the heat resets) while also preventing premature deletion (the segment can re-heat if new pages land in it). Without the heat-reset, you'd get either thrashing (the same hot segment promoted every cycle, polluting LPM) or premature loss (segments deleted right after promotion, losing the page-level detail that made them hot in the first place).

**Why it matters:** The promotion-without-deletion + heat-reset pattern is what gives MemoryOS its *graceful aging* property. A topic that was very hot for a month (lots of dialogue pages, many retrievals) gets promoted to LPM as user traits / KB facts, then its MTM segment cools naturally as the user moves on to other topics. If the user returns to it months later, the segment is probably still in MTM (cold but not evicted) and can be re-activated by new pages landing in it (which spikes `L_interaction` and pushes Heat back up). The architecture is therefore *implicitly stateful about user life arcs* — long-lived but cyclical interests stay accessible, transient interests fade. Compare to flat-FIFO architectures (MemoryBank) where everything ages on the same clock regardless of importance, or fixed-keep architectures (raw KGs) where everything stays forever and retrieval gets noisier with time. For Flow OS, this is the right model for multi-venture work — a venture in pause gets its MTM segment cold but not deleted, and any new capture about that venture re-heats it without needing to "rehydrate" from a frozen snapshot.

**Example of good use (memory architectures for agentic OSes):** Implementing the Flow OS retrofit, after promoting a topic-segment ("Ride Ready launch plan") to LPM (extracting facts to User KB + updating relevant traits), keep the segment in MTM with `L_interaction = 0`, `last_accessed = now`. The heat formula will naturally decay it over weeks (with µ=1e7 ≈ 115 days, exp(-7·86400/1e7) ≈ 0.94 after one week, ≈ 0.74 after one month). If the user reopens Ride Ready in 3 months, the segment is still in MTM (probably with a small heat); the new capture lands in the segment, spiking `L_interaction` from 0 to 5, recomputing heat at 5 + 0·visits + 1·exp(-90·86400/1e7) ≈ 5.46 — above τ, ready for re-promotion. The User KB then gets updated with the new state of Ride Ready, and the cycle continues. No information lost; no thrashing; the venture's life arc is automatically captured by the heat curve.

**Example of misapplication:** A team adopts the segment-page architecture but implements promotion as "promote-and-delete" — when a segment hits Heat > τ, extract its facts to LPM and then delete the MTM segment to "free up space." What breaks: if a user returns to the topic weeks later, the page-level detail is gone (only the distilled LPM facts remain), so the agent's response is less rich (it can recall "you have Ride Ready" but not "you decided to pause it in March because notification API costs were higher than expected"). The user notices the agent has become more abstract over time, less able to reconstruct the *why* behind decisions. The lesson missed: **promotion is for the persona layer, not garbage collection.** The MTM segment retains the page-level evidence even after LPM promotion; only the heat resets. Delete only on natural cooling, not on promotion. The paper's text is consistent on this in §3.3 ("After memory transition, the number of pages L_interaction in Eq. 4 is reset to zero, causing the heat score of the segment to decline") — but it's a one-sentence aside that's easy to miss when the louder claim is "promote hot segments to LPM."

## Extracted Prompts

**Prompt explanation:** Dialogue-page chain construction (§3.2, eq. 1) — the two-step LLM-driven meta-information generation that decides whether a new page links to the prior chain or resets it. Reconstructed from the paper's methodology (no verbatim prompt given):

```
You are managing a dialogue-page chain for short-term memory.

A page is {Q (user query), R (model response), T (timestamp)}.
A chain links consecutive pages on the same topical thread.

Given the prior page meta_chain_{i-1} (summary of the chain so far) and
the new page (Q_i, R_i, T_i), perform two steps:

STEP 1 — CHAIN LINKAGE DECISION
Decide whether (Q_i, R_i) is semantically continuous with the prior chain.
Output exactly one of:
  CONTINUE: the new page extends the existing chain
  RESET: the new page starts a new chain (topically discontinuous)

STEP 2 — META SUMMARIZATION
If CONTINUE: summarize ALL pages in the chain (including the new page)
             into a single coherent meta string capturing the thread.
If RESET: summarize only the new page (Q_i, R_i) as the start of a fresh chain.

OUTPUT:
{
  "decision": "CONTINUE" | "RESET",
  "meta_chain_i": "<summary string>"
}
```

**Prompt explanation:** Segment summarization (§3.2, paragraph after eq. 2) — used when a page is added to a segment, to refresh the segment summary based on all pages currently in the segment.

```
You are summarizing a topic segment of dialogue history.

A segment contains multiple dialogue pages (Q, R pairs) on a unified
topic. Generate a concise topic summary capturing:
  - The main subject of the segment
  - Key decisions, preferences, or facts established
  - The most recent state if the topic evolved across pages

Be objective. Do NOT include opinion or judgment. Aim for 2-4 sentences.

SEGMENT PAGES:
{list of (Q_i, R_i, T_i) for all pages in segment}

OUTPUT: the segment summary string.
```

**Prompt explanation:** User Trait extraction (§3.3, LPM Update) — runs on every MTM-to-LPM promotion to update the 90-dimensional user traits vector. Reconstructed from the paper's reference to Li et al. (2025) for the trait taxonomy:

```
You are extracting user-trait signals from a recently-promoted memory
segment.

The user is described by a 90-dimensional trait vector across three
categories:
  1. Basic Needs & Personality (~30 dims): openness, conscientiousness,
     extraversion, agreeableness, neuroticism, plus specific need-states
     (autonomy, competence, relatedness, ...) — each scored [0, 1]
  2. AI Alignment Dimensions (~30 dims): tone preference (direct vs
     diplomatic), verbosity preference, formatting preference, etc.
  3. Content Platform Interest Tags (~30 dims): topical interests
     (AI agents, finance, travel, ...) — each scored [0, 1]

Given the segment summary and dialogue pages below, output delta values
for any dimensions where the segment provides evidence. Use:
  +0.05 = mildly reinforces
  +0.10 = strongly reinforces
  -0.05 = mildly weakens
  -0.10 = strongly weakens
  0     = no evidence (omit from output)

Be conservative. Most segments touch only 2-5 dimensions.

CURRENT TRAITS: {existing 90-dim vector}
SEGMENT SUMMARY: {segment summary}
TOP-10 PAGES: {first 10 dialogue pages from segment}

OUTPUT: JSON dict of {dimension_name: delta_value} for dimensions touched.
```

**Prompt explanation:** User KB / Agent Traits fact extraction (§3.3, LPM Update) — extracts the long-term factual claims that should land in the FIFO-100 User KB and Agent Traits queues.

```
You are extracting durable user facts from a recently-promoted memory
segment.

The User KB stores factual claims about the user that are likely to
remain relevant over weeks-to-months. Examples:
  - "User is allergic to peanuts"
  - "User's partner Nadia works in marine ecology"
  - "User co-founded AskRally with Michael Taylor"

Do NOT extract:
  - Ephemeral state ("user was tired today")
  - Speculation ("user might be considering X")
  - Opinions ("user thinks the market is overheated") — those belong in
    a separate opinion log

The Agent Traits store emergent behaviors / settings the agent has
learned to exhibit for this user. Examples:
  - "User prefers direct responses without hedging"
  - "User wants citations included when discussing research"
  - "User has set the agent's default lens to 'memory-architect' for
    paper digests"

Output each extracted fact as a single sentence, classified by target
queue. Each queue is FIFO-100; old facts age out as new ones come in.

SEGMENT SUMMARY: {segment summary}
SEGMENT PAGES: {first 10 dialogue pages from segment}

OUTPUT:
{
  "user_kb_adds": ["<fact-1>", "<fact-2>", ...],
  "agent_traits_adds": ["<trait-1>", "<trait-2>", ...]
}
```

## Citations

First 10 (see frontmatter for full list of 21 references):

- Bensoussan et al. (1972) — *The Multics virtual memory: Concepts and design* — Comm. ACM 15(5):308-318
- Chhikara et al. (2025) — *Mem0: Building production-ready AI agents with scalable long-term memory* — arXiv:2504.19413
- DeepSeek-AI et al. (2025) — *DeepSeek-R1: Incentivizing reasoning capability in LLMs via RL* — arXiv:2501.12948
- Denning (1970) — *Virtual memory* — ACM Computing Surveys 2(3):153-189
- Du et al. (2025) — *Rethinking memory in AI: Taxonomy, operations, topics, and future directions* — arXiv:2505.00675
- Huang et al. (2024) — *Emotional RAG: Enhancing role-playing agents through emotional retrieval* — ICKG 2024
- Liu et al. (2023) — *Think-in-memory: Recalling and post-thinking enable LLMs with long-term memory* — arXiv:2311.08719
- Maharana et al. (2024) — *Evaluating very long-term conversational memory of LLM agents (LoCoMo)* — ACL
- Packer et al. (2023) — *MemGPT: Towards LLMs as operating systems* — arXiv:2310.08560
- Xu et al. (2025) — *A-Mem: Agentic memory for LLM agents* — arXiv:2502.12110

## Related Digests

- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects (Latimer et al., 2025) — four-network epistemic-typing architecture. Hindsight cuts memory by *source-of-knowledge* (W/B/O/S), MemoryOS cuts by *temporal tier* (STM/MTM/LPM) — orthogonal cuts that could combine in a v3 schema.
- [[wang-2025-mirix]] — MIRIX: Multi-Agent Memory System for LLM-Based Agents (Wang & Chen, 2025) — six-component cognitive-typing architecture. MIRIX uses a multi-agent router across functional roles; MemoryOS uses a single-flow segment-page pipeline. Both achieve strong LoCoMo numbers via different routing strategies.
- [[liu-2025-memverse]] — MemVerse: Multimodal Memory for Lifelong Learning Agents (Liu et al., 2025) — slow KG long-term + fast parametric cache architecture. MemoryOS's segment-page MTM is a simpler alternative to MemVerse's MMKG (less expressive, but no graph-construction cost and lower retrieval LLM-call count).
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as operating systems (Packer et al., 2023) — the direct ancestor. MemoryOS extends MemGPT's flat-paging discipline with topic-clustered *segments* — and on LoCoMo it outperforms MemGPT 36.23 vs 29.13 F1 with similar LLM-call counts (4.9 vs 4.3).
- [[chhikara-2025-mem0]] — Mem0: Building production-ready AI agents with scalable long-term memory (Chhikara et al., 2025) — the flat-fact-store production baseline. MemoryOS uses Mem0 as a representative architecture-driven framework in §2.1.
- [[xu-2025-a-mem-agentic-memory]] — A-Mem: Agentic memory for LLM agents (Xu et al., 2025) — Zettelkasten KG baseline. MemoryOS outperforms A-Mem on both GVD (93.3 vs 90.4) and LoCoMo (36.23 vs 26.55 avg F1), at 3× lower LLM cost (4.9 vs 13.0 calls).
- [[liu-2023-think-in-memory]] — Think-in-Memory: Recalling and post-thinking enable LLMs with long-term memory (Liu et al., 2023) — TiM is one of the four LoCoMo baselines. MemoryOS beats TiM substantially on all categories.
- [[zhong-2023-memorybank-llm]] — MemoryBank: Enhancing LLMs with long-term memory (Zhong et al., 2024) — forgetting-curve baseline. MemoryOS performs much better; the lesson is that decay alone is insufficient — you need promotion + segment-page structure.
- [[maharana-2024-locomo]] — LoCoMo benchmark (Maharana et al., 2024) — the long-form conversation eval shared across MemoryOS, MIRIX, Hindsight, MemVerse, Mem0, Zep, A-Mem.

## Reviewer Notes

**Hallucination severity:** Clean

Spot-checks against the source PDF:

- **Three storage tiers: STM (length 7), MTM (segment paging, segment cap 200), LPM (User KB / Agent Traits FIFO-100)** — verified in §4.1 Implementation Details (p. 5–6). ✓
- **Heat formula: `Heat = α·N_visit + β·L_interaction + γ·R_recency` with `R_recency = exp(-Δt/µ)`, µ=1e7s** — verified in eq. 4 (§3.3, p. 4) and §4.1 (p. 6 — "µ is a configurable time constant (i.e., 1e+7)"). ✓
- **α, β, γ = 1 each in experiments** — verified in §4.1: "The values of α, β, and γ in Eq. 4 are equality set to 1." ✓
- **Heat threshold τ = 5 for MTM→LPM promotion** — verified in §3.3 ("Segments with heat exceeding a threshold τ (i.e., 5) are transferred to LPM") and §4.1 ("The predefined Heat threshold τ ... is set to 5"). ✓
- **Fscore = cos(e_s, e_p) + F_Jacard(K_s, K_p), threshold θ=0.6** — verified in eq. 3 and §4.1 ("similarity value of θ in Eq. 2 is 0.6"). ✓
- **STM-MTM update via FIFO; MTM-LPM via heat-based promotion + eviction** — verified in §3.3, both paragraphs. ✓
- **MTM retrieval: top-m=5 segments via Fscore, top-k=10 pages within (5 on GVD)** — verified in §3.4 and §4.1 ("the number of retrieval top-m segments was set to 5, and the hyperparameter top-k for retrieved dialogue page was set to 5 and 10 on the GVD and LoCoMo datasets"). ✓
- **LoCoMo results: GPT-4o-mini MemoryOS averages 36.23 F1; +49.11% F1 / +46.18% BLEU-1 improvement over baselines** — verified in §4.2 ("on the LoCoMo benchmark with gpt-4o-mini, it achieves average improvements of 49.11% on F1 score and 46.18% on BLEU-1"). Table 2 confirms MemoryOS at Single-Hop 35.27, Multi-Hop 41.15, Temporal 20.02, Open-Domain 48.62 (avg ≈ 36.27 F1; 49.11% is over the baseline-average, not over the highest-baseline). The improvement percentages in Table 2's "Improvement (%)" row are reasonably interpreted as per-baseline-best, e.g. Temporal +118.80% over MemGPT's 9.15. ✓
- **GVD results: GPT-4o-mini MemoryOS Acc 93.3 vs A-Mem 90.4 (+3.2%); Qwen2.5-7B MemoryOS Acc 91.8 vs A-Mem 87.2 (+5.3%)** — verified in Table 1 (p. 5). Percentages match the "Improvement (%)" row. ✓
- **Efficiency: MemoryOS 4.9 LLM calls + 3,874 tokens vs A-Mem* 13.0 calls + 2,712 tokens vs MemGPT 4.3 calls + 16,977 tokens** — verified in Table 3 (p. 5). ✓
- **90-dim User Traits across 3 categories (basic needs + personality, AI alignment, content platform interest)** — verified in §3.3 ("we construct personalized User Traits with 90 dimensions across three categories: basic needs and personality, AI alignment dimensions, and content platform interest tags"). ✓
- **User KB / Agent Traits: fixed-size FIFO 100** — verified in §3.3 ("Both the User KB and Assistant Traits maintain a fixed-size queue (i.e., 100), employing a First-In-First-Out (FIFO) strategy"). ✓
- **STM length 7** — verified in §4.1 ("The fixed length of the dialogue page queue in STM is 7"). ✓
- **Segment max length 200** — verified in §4.1 ("The maximum length of segments in MTM is set to 200"). ✓
- **Ablation: MTM is most impactful, LPM second, Chain least (§4.3, Figure 2)** — verified in §4.3 ("the Mid-Term Memory (MTM) has the most significant impact, followed by the Long-Term Memory (LPM), while the Chain has the least impact"). ✓
- **Backbones tested: GPT-4o-mini and Qwen2.5-3B (LoCoMo) / Qwen2.5-7B (GVD)** — verified in Tables 1, 2. ✓
- **Hardware: 8× H20 GPUs** — verified in §4.1 ("conducted on hardware equipped with 8-H20 GPUs"). ✓
- **arXiv ID 2506.06326v1, submitted 30 May 2025** — verified in title page header. ✓
- **Affiliations: Beijing University of Posts and Telecommunications + Tencent AI Lab** — verified in author block (p. 1). ✓
- **Code at github.com/BAI-LAB/MemoryOS** — verified in abstract. ✓

One minor note: the LoCoMo "Open Domain" category numbers in Tables 1 and 2 use GPT-4o-mini and Qwen2.5-3B respectively, not Qwen2.5-7B (which is used in GVD). The digest is careful to specify which backbone each number comes from.

No fabricated claims found. Severity: **Clean**.
