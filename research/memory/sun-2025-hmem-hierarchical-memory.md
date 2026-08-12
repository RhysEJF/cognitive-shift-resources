---
corpus: agentic-memory
kind: paper-digest
slug: sun-2025-hmem-hierarchical-memory
title: "H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents"
authors:
  - "Sun, Haoran"
  - "Zeng, Shaoning"
year: 2025
publication_date: "2025-07"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2507.22925"
doi: null
arxiv_id: "2507.22925"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "H-MEM organises memory into a fixed 4-layer abstraction tree (Domain → Category → Memory Trace → Episode) with positional index pointers embedded inside each parent vector, so retrieval is a layer-by-layer top-k walk rather than a flat exhaustive similarity sweep — reducing complexity from O(a·10^6·D) to O((a + k·300)·D) and keeping retrieval latency under 100 ms vs MemoryBank's 461 ms on the largest LoCoMo task, while still beating five baselines by +14.98 F1 / +12.77 BLEU-1 on average."
topics:
  - hierarchical-memory
  - agent-memory
  - long-term-memory
  - retrieval-efficiency
  - locomo-benchmark
  - positional-index-encoding
  - memory-update
  - ebbinghaus-forgetting
tags:
  - paper
  - memory-architecture
  - llm-agents
  - retrieval
  - hierarchical-retrieval
  - faiss
  - benchmark-locomo
entities:
  - sun-haoran
  - zeng-shaoning
  - locomo-dataset
  - faiss-library
  - memorybank
  - a-mem
  - memgpt
  - readagent
related_digests:
  - kang-2025-memory-os
  - du-2025-rethinking-memory
  - xu-2025-a-mem-agentic-memory
  - zhong-2023-memorybank-llm
  - liu-2025-memverse
citations:
  - title: "Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning"
    authors: ["DeepSeek-AI"]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2501.12948"
  - title: "The faiss library"
    authors: ["Matthijs Douze", "Alexandr Guzhva", "Chengqi Deng", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "A survey on llm-as-a-judge"
    authors: ["Jiawei Gu", "Xuhui Jiang", "Zhichao Shi", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2411.15594"
  - title: "Memory matters: The need to improve long-term memory in llm-agents"
    authors: ["Kostas Hatalis", "Despina Christou", "Joshua Myers", "et al."]
    year: 2023
    venue: "Proceedings of the AAAI Symposium Series, vol 2, pp 277-280"
    doi: null
    url: null
    arxiv_id: null
  - title: "Understanding the planning of llm agents: A survey"
    authors: ["Xu Huang", "Weiwen Liu", "Xiaolong Chen", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2402.02716"
  - title: "A human-inspired reading agent with gist memory of very long contexts"
    authors: ["Kuang-Huei Lee", "Xinyun Chen", "Hiroki Furuta", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2402.09727"
  - title: "Personal llm agents: Insights and survey about the capability, efficiency and security"
    authors: ["Yuanchun Li", "Hao Wen", "Weijun Wang", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2401.05459"
  - title: "Evaluating very long-term conversational memory of llm agents"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2402.17753"
  - title: "Memgpt: Towards llms as operating systems"
    authors: ["Charles Packer", "Vivian Fang", "Shishir G Patil", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Meminsight: Autonomous memory augmentation for llm agents"
    authors: ["Rana Salama", "Jason Cai", "Michelle Yuan", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2503.21760"
  - title: "Llm with tools: A survey"
    authors: ["Zhuocheng Shen"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2409.18807"
  - title: "Llama: Open and efficient foundation language models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2302.13971"
  - title: "Enhancing large language model with self-controlled memory framework"
    authors: ["Bing Wang", "Xinnian Liang", "Jian Yang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2304.13343"
  - title: "A survey on llm-generated text detection: Necessity, methods, and future directions"
    authors: ["Junchao Wu", "Shu Yang", "Runzhe Zhan", "et al."]
    year: 2025
    venue: "Computational Linguistics"
    doi: null
    url: null
    arxiv_id: null
  - title: "A-mem: Agentic memory for llm agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2502.12110"
  - title: "Qwen2 technical report"
    authors: ["An Yang", "Baosong Yang", "Binyuan Hui", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2407.10671"
  - title: "Qwen2.5 technical report"
    authors: ["An Yang", "Baosong Yang", "Beichen Zhang", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2412.15115"
  - title: "A survey on large language model (llm) security and privacy: The good, the bad, and the ugly"
    authors: ["Yifan Yao", "Jinhao Duan", "Kaidi Xu", "et al."]
    year: 2024
    venue: "High-Confidence Computing"
    doi: null
    url: null
    arxiv_id: null
  - title: "A survey on recent advances in llm-based multi-turn dialogue systems"
    authors: ["Zihao Yi", "Jiarui Ouyang", "Yuwen Liu", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2402.18013"
  - title: "A survey on the memory mechanism of large language model based agents"
    authors: ["Zeyu Zhang", "Xiaohe Bo", "Chen Ma", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2404.13501"
  - title: "Memorybank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "et al."]
    year: 2024
    venue: "Proceedings of the AAAI Conference on Artificial Intelligence"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 4
  title: "Comparative analysis of computational efficiency"
  page: 8
  image_path: "figures/sun-2025-hmem-hierarchical-memory-fig.png"
---

# H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents

**Authors:** Haoran Sun, Shaoning Zeng
**Published:** 2025-07 · [Source](https://arxiv.org/abs/2507.22925)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

H-MEM is a hierarchical memory architecture for LLM agents that arranges every stored interaction into a fixed four-level abstraction tree — **Domain → Category → Memory Trace → Episode** — modelled on the section/subsection/subsubsection/content structure of a document. The novel mechanism: each non-leaf memory vector embeds, alongside its dense semantic vector, a **positional index encoding** containing pointers to its child sub-memories in the next layer. At retrieval time the system walks the tree top-down — encode the query, run FAISS top-k similarity at the Domain layer only, follow the index pointers of the winning domains to their child categories, top-k again over `k·100` candidates, descend, and so on. This converts a flat O(a·10^6·D) similarity sweep into an O((a + k·300)·D) layered traversal. On the LoCoMo long-conversation benchmark (50 dialogues, ~300 turns each, 7,512 QA pairs) H-MEM beats five baselines (LoCoMo, ReadAgent, MemoryBank, MemGPT, A-MEM) by an average of **+14.98 F1 / +12.77 BLEU-1** across six base models (Qwen-1.5B/3B, LLaMA-3.2-1B/3B, DeepSeek-R1-1.5B/7B). On computational efficiency, retrieval latency stays under 100 ms even at maximum memory load versus MemoryBank's 461 ms (5× faster) on the largest task. The Memory Update component augments the standard Ebbinghaus forgetting curve with an LLM-judged user-feedback signal (approval → boost, no feedback → natural decay, rebuttal → weaken).

## Key Takeaway

The contribution that distinguishes H-MEM from every other hierarchical agent-memory paper is the **positional index encoding stored inside the parent vector** — at write time the system embeds a list of pointer indices `{p_i1, ..., p_iK}` directly into each non-leaf memory's stored representation, alongside the semantic vector. At retrieval, similarity is computed only against the semantic-vector portion (ignoring the index portion); the matching parent then hands the searcher a pre-baked-in list of which child rows to descend into. This is structurally a learned-at-write-time inverted index baked into the memory record itself, eliminating the join step that pure graph or tree-of-vectors approaches still require. The cost: the hierarchy is committed at write time and the four-layer depth is a hand-tuned constant — the paper acknowledges this and adds a "self-adaptation hierarchy adjustment interface" letting users dial layers up or down by conversation complexity, but does not evaluate it experimentally.

## Implications

**For the ENGRAM E (Encode) dimension** — H-MEM puts a heavy LLM extractor on the write path: every user-LLM turn is passed to DeepSeek-R1-8B with a prompt that forces structured JSON extraction across four hierarchy levels (domain, category, keywords, events+user-profile). The write cost is paid once, the retrieval cost is amortised forever. This is the same architectural bet MemoryOS (Kang 2025) and Amory (Zhou 2026) make, but H-MEM commits earlier and harder — the entire retrieval index is materialised at write time, not lazily consolidated.

**For ENGRAM N (Network)** — the shape is a **layered vector store with embedded inverted-index pointers**, not a graph and not a flat vector DB. This is a polyglot stack in disguise: FAISS for similarity at each layer + explicit pointer following between layers. It sits between A-MEM's open-ended Zettelkasten graph and MemoryBank's flat vector store.

**For ENGRAM G (Ground)** — each retrieved memory at the Episode layer carries both vector and original text, plus a "memory weight" that's surfaced to the LLM as a **Confidence Level reference** (paper §3.2). This is provenance-aware: the final reasoning prompt receives a calibrated weight per memory, not just the raw text. Implication: agents can in principle reason about how much to trust each retrieved fact — but the paper does not evaluate whether the LLM actually uses the weight effectively.

**For ENGRAM R (Retrieve)** — top-k=10 is fixed; FAISS Flat index used; no hybrid lexical-semantic search. The hierarchy itself does the candidate-narrowing job that BM25+rerank does in flat systems. Practical limit: a query that doesn't match well at the Domain layer can never reach the right Episode, because the descent is hard-routed by parent matches. The paper doesn't discuss this failure mode or evaluate recall vs precision separately.

**For ENGRAM A (Aggregate)** — there is no consolidation step. Each turn becomes one Episode forever; abstractions are extracted once at write time and never re-summarised. Compare to Amory (Zhou 2026) which defers consolidation until topics go inactive, or A-MEM which mutates parent tags as new children are added. H-MEM is structurally **eager-extract, no-reconsolidate** — a deliberate architectural opposite of Amory's lazy approach.

**For ENGRAM M (Maintain)** — the Memory Update mechanism is the most novel maintenance contribution: a feedback-modulated Ebbinghaus forgetting curve. When a memory is retrieved, the LLM judges the user's downstream response (approval/silence/rebuttal) and multiplies the memory's weight by a feedback factor. This is structurally close to MemoryBank's update rule but adds user-feedback grounding. Open question: does the LLM-judged feedback signal drift, and how does it interact with the fixed hierarchy when a memory's domain effectively becomes wrong over time?

**Cross-dimensional interaction** — the **fixed four-layer write-time hierarchy (E) forces eager-extract semantics (A) and a layered FAISS retrieval shape (R)**, which together preclude lazy reconsolidation. If a Memory Trace turns out to belong under a different Category than originally written, there is no described mechanism to re-parent it — the index pointers are fixed at write time. This is the structural cost of trading aggregation for retrieval efficiency.

**For Flow OS** — H-MEM is the cleanest open-published worked example of "bake the index into the parent record." Compare with QMD: QMD's BM25 + vector + entity-edge stack does layer-narrowing at query time via filters/weights, where H-MEM does it at write time via stored pointers. The H-MEM approach is a closer fit when (a) write throughput is low relative to read throughput, and (b) the hierarchy is genuinely stable. For Flow's memory layer (mixed-modality, contradiction-heavy, frequently re-categorised), the Amory deferred-consolidation pattern is probably a better fit — but H-MEM's positional-index trick is worth borrowing for the *stable* parts of the hierarchy (e.g., venture → service → contact).

## How to Apply It (method)

**To replicate H-MEM as an architecture, the working pipeline is:**

1. **Write-time extractor (E)** — for every user-LLM turn, call a separate LLM (paper uses DeepSeek-R1-8B locally via Ollama) with a structured prompt that returns JSON across four levels: `{domain, category, keywords/trace, episode (raw text + timestamp + inferred user-profile)}`. The exact paper prompt (paraphrased in §3.1): *"You are a information analyze agent for a long-term LLM system. Given a dialogue, you must extract and structure the information into a hierarchical memory format. Follow this hierarchy strictly: 1. Identify the high-level domain of interest. 2. Extract specific categories or subdomains related to the topic. 3. Summarize the keywords of the dialogue. 4. Extract specific events and user profile. Output the result as structured JSON."*
2. **Vector storage (N)** — encode each level's text via BERT (paper's choice; any sentence encoder works) into dense vector e_i ∈ R^D. Each non-leaf vector is stored as the concatenation `[semantic_vector | self_index | child_index_1 | ... | child_index_K]`. Episode-layer vectors also retain the raw text and the timestamp/user-profile.
3. **Index registration (R)** — push every layer's vectors into FAISS (Flat index used in the paper for fair efficiency comparison; IVF/HNSW would scale better). The pointer indices are stored *outside* FAISS — they're just integer columns the application layer manages.
4. **Retrieval (R)** — at query time:
   - Embed the query q.
   - FAISS top-k at the Domain layer (semantic-vector portion only).
   - For each winning domain, read its stored child pointers and run FAISS top-k restricted to those Category vectors only.
   - Repeat at Memory Trace → Episode levels.
   - At Episode layer, return the top-k=10 raw texts plus their memory weights.
   - Prepend retrieved texts + "Confidence Level" weights to the LLM prompt.
5. **Update (M)** — after the LLM answers, run a feedback-judging LLM call: classify the user's next message as `{approval | no_feedback | rebuttal}`. Multiply the retrieved memories' weights by an LLM-generated feedback factor. No feedback → apply Ebbinghaus natural decay.
6. **Hierarchy adjustment (E)** — expose a user-facing knob to add/remove layers per conversation. Paper does not evaluate this — engineering reality is you'd need to re-extract every memory if the layer count changes mid-deployment.

**Hardware footprint:** experiments ran on 2× NVIDIA RTX 4090 with all models served locally via Ollama. Base QA models: Qwen-1.5B/3B, LLaMA-3.2-1B/3B, DeepSeek-R1-1.5B/7B. Memory analysis model: DeepSeek-R1-8B. Encoder: BERT.

**Cost model:** retrieval complexity is O((a + k·300)·D) where a = number of domains, k = top-k, D = embedding dimension — vs O(a·10^6·D) for flat retrieval. Concretely on Qwen-1.5B at maximum LoCoMo memory load: H-MEM retrieval = 80 ms / 4.38×10^7 compute ops; MemoryBank = 461 ms / 7.34×10^9 compute ops.

## Best Figure

![Figure 4 — Comparative analysis of computational efficiency (page 8)](figures/sun-2025-hmem-hierarchical-memory-fig.png)

**Image Candidates:**
- Figure 4 (p. 8): Side-by-side time + compute-ops curves of H-MEM vs MemoryBank as memory grows; H-MEM stays flat, MemoryBank grows exponentially — the paper's central efficiency claim in one view.
- Table 1 (p. 7): The 6-model × 5-task QA accuracy grid showing H-MEM beating five baselines on F1 and BLEU-1 in nearly every cell — the breadth-of-evidence shot.
- Figure 5 (p. 8): Ablation bars showing the storage-retrieval synergy collapses if either H or R is removed — confirms the mechanism is the architecture, not just the LLM.

**Best Image:**
- **Figure Name:** Figure 4: "Comparative analysis of computational efficiency"
- **Figure Page:** 8
- **Slide Caption:** Hierarchical retrieval keeps H-MEM under 100 ms even as memory grows; flat similarity search grows past 400 ms.
- **Description:** Figure 4 plots latency (ms, left axis) and compute operations (log scale, right axis) for H-MEM versus MemoryBank as cumulative LoCoMo questions accumulate from 2,000 to 7,500 on Qwen-1.5B. MemoryBank's time curve (blue bars) grows linearly with accumulated memory, ending above 400 ms; H-MEM's bars (orange) stay below 100 ms throughout. The compute-ops curves (lines) tell the same story on a log axis: MemoryBank rises by orders of magnitude, H-MEM stabilises. The figure is the visual proof of the hierarchical architecture's central claim — that the cost of similarity search is decoupled from the size of the memory store by the layered routing.

## What Experts Overlook

**1. The positional-index encoding is the entire contribution, but the paper barely sells it.** The novelty here is *not* hierarchical memory (MemoryOS, A-MEM, MemoryBank-with-cabinets all do that). It's that each parent vector physically contains its own child-pointer list as part of its stored representation — so the "follow the hierarchy" step becomes a lookup, not a join. This is a tiny architectural change that pays off massively at retrieval time, and most readers will skim past it because the prose buries it inside a math equation in §3.2.

**2. Fixed depth of 4 is empirically chosen, not principled.** The authors say "After calculating and experimenting with different L values, we finally chose the optimal 4-layer, which can simultaneously balance the accuracy and efficiency of retrieval" — but they do not show the ablation. No table or plot of L=2,3,4,5,6 vs F1/latency. Practitioners adopting H-MEM should treat L=4 as the LoCoMo-fit choice, not a universal one.

**3. The "self-adaptation hierarchy adjustment interface" is vaporware.** Mentioned in §3.1 as a feature, never evaluated, never described concretely. If the production deployment needs to add a layer mid-life, the paper provides no mechanism to do so without re-extracting every memory.

**4. The Memory Update mechanism's LLM-feedback-judge is unaudited.** The system uses an LLM to classify user responses as approval/silence/rebuttal and multiplies memory weights accordingly. There is no error rate reported on the feedback classifier, no evidence the agent doesn't promote its own prior outputs to confirmed facts via biased self-judging. This is a textbook drift-and-provenance failure surface.

**5. No graceful failure when top-k narrowing kills recall.** Because the descent is hard-routed by Domain-layer winners, a query that semantically belongs to a Domain that wasn't ranked in the top-k can never reach its correct Episode — regardless of how well it matches that Episode at the leaf level. The paper does not measure recall@k separately from final F1, nor offer a fallback (e.g., a parallel flat-retrieval safety net).

**6. The forgetting-curve update doesn't dialogue with the hierarchy.** Episodes age and decay independently of their parent Category or Domain. If a whole Category becomes stale (user no longer interested in skiing), Episodes underneath still decay only on their individual access pattern — there's no cascading inactivation. This contrasts with Amory's momentum-aware lazy consolidation, where inactivity at a higher level is itself the signal.

**7. The benchmark is LoCoMo only.** All claims rest on LoCoMo's 50 dialogues × ~300 turns × 7,512 QA pairs. The "5× faster" and "+14.98 F1" numbers are within-this-distribution. The paper does not test on cross-domain (e.g., enterprise knowledge bases), multi-user shared memory, or adversarial-conflict corpora.

**8. Citations 2024a and 2024b are duplicate entries.** Huang et al. 2024a and 2024b have identical title, authors, and arXiv ID — and so do Zhang et al. 2024a and 2024b. This is a bibliography hygiene flag, not a research one, but it suggests the manuscript was rushed.

## Extracted Prompts

**1. Hierarchical memory extraction (write-path)** — paraphrased from §3.1; paper notes "approximate simplified meaning of the prompt":

```
You are a information analyze agent for a long-term LLM system. Given
a dialogue, you must extract and structure the information into a
hierarchical memory format. Follow this hierarchy strictly:

1. Identify the high-level domain of interest.
2. Extract specific categories or subdomains related to the topic.
3. Summarize the keywords of the dialogue.
4. Extract specific events and user profile.

Output the result as structured JSON.
```

**2. Feedback-classification update (maintenance-path)** — implied by §3.3 but not given verbatim. The reconstructable form:

```
Given the user's previous message and the assistant's reply that used the
following retrieved memory: <memory_text>

Classify the user's downstream response as one of:
- approval (the user accepted or built on the assistant's reply)
- no_feedback (the user neither confirmed nor refuted)
- rebuttal (the user contradicted or corrected the assistant)

If approval, return a feedback weight in [1.0, 2.0].
If no_feedback, return 1.0 (memory will follow natural Ebbinghaus decay).
If rebuttal, return a weight in [0.0, 1.0].

Output: {classification, feedback_weight}
```

(Reconstruction — paper describes mechanism, does not publish the prompt.)

## Citations

The full citation list (21 entries) is in frontmatter as structured JSON for downstream citation-walk loops. Top entries by relevance to H-MEM's design:

- Zhong et al. 2024 — MemoryBank: the direct flat-vector baseline H-MEM beats on both efficiency (5×) and accuracy (+14.98 F1).
- Xu et al. 2025 — A-MEM: the Zettelkasten-graph baseline; H-MEM's strongest single competitor on Multi-Hop and Adversarial tasks.
- Packer et al. 2023 — MemGPT: the OS-inspired layered-memory ancestor; H-MEM cites it as motivation for the multi-level structure but rejects its retrieval-augmentation approach.
- Lee et al. 2024 — ReadAgent: gist-memory page-compression baseline.
- Maharana et al. 2024 — LoCoMo: the benchmark dataset used for every comparison; without LoCoMo this paper has nothing to evaluate against.
- Salama et al. 2025 — MemInsight: cited as a related-work autonomous memory augmentation approach; not in the baseline set.
- Douze et al. 2024 — FAISS library: the similarity-search engine used at every layer.
- DeepSeek-AI 2025 — DeepSeek-R1-8B: the LLM doing the write-path hierarchy extraction.
- Yang et al. 2024a, 2024b — Qwen 2 / 2.5 technical reports: the base QA models.
- Touvron et al. 2023 — LLaMA: a base QA model family.
- Hatalis et al. 2023 — "Memory matters" position paper motivating the long-term-memory research line.
- Zhang et al. 2024a, b — Memory mechanism survey: the canonical taxonomy paper this work positions against.
- Huang et al. 2024a, b — LLM agent planning survey.
- Li et al. 2024 — Personal LLM agents survey.
- Wang et al. 2023 — SCM (Self-Controlled Memory) framework, named in related work but not in baselines.
- Yi et al. 2024 — Multi-turn dialogue systems survey.
- Wu et al. 2025 — LLM-generated text detection survey.
- Yao et al. 2024 — LLM security/privacy survey.
- Shen 2024 — LLM-with-tools survey.
- Gu et al. 2024 — LLM-as-a-judge survey.

## Related Digests

- [[kang-2025-memory-os]] — Memory OS of AI Agent — closest cousin: also borrows OS-style layered discipline (FIFO dialogue-pages → topic-clustered segments) but does its consolidation as a separate background process rather than baking the index into the parent at write time
- [[du-2025-rethinking-memory]] — Rethinking Memory in LLM-based Agents — the 73-page survey that gives the taxonomy under which H-MEM falls (textual + indexed + LLM-extracted)
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: Agentic Memory — H-MEM's strongest baseline competitor; A-MEM mutates parent tags as children arrive, H-MEM freezes them at write time
- [[zhong-2023-memorybank-llm]] — MemoryBank — the flat-vector baseline H-MEM's efficiency comparison directly attacks; same Ebbinghaus decay heritage
- [[liu-2025-memverse]] — MemVerse: Multimodal Memory — a contrasting design point: graph-based long-term memory + periodic SFT, vs H-MEM's text-only fixed-depth hierarchy

## Reviewer Notes

**Overall severity:** Clean

All quantitative claims (F1 +14.98 / BLEU-1 +12.77 averages; Multi-Hop +21.25/+17.65; Adversarial +16.71/+12.03; 5× latency advantage; <100 ms vs 461 ms; complexity O((a + k·300)·D) vs O(a·10^6·D); LoCoMo stats 50 dialogues / ~300 turns / 7,512 QA pairs / 5 task categories with given pair counts; 6-model evaluation set; 2× RTX 4090 deployment; BERT encoder; FAISS Flat) cross-check against the paper's Tables 1 and 2 and §3.2-§4.1.

Architectural claims (positional-index encoding embedded in parent vectors; semantic-vector-only similarity at descent steps; LLM-judged feedback factor for the Ebbinghaus update; self-adaptation hierarchy interface acknowledged-but-unevaluated) all map to §3.1, §3.2, §3.3.

Critique claims in "What Experts Overlook" (no L-ablation shown; no recall-vs-F1 breakdown; no feedback-classifier audit; bibliography duplicate entries for Huang and Zhang 2024) are verifiable directly from the paper — they are absences, not contradictions.

The reconstructed feedback-classification prompt is explicitly marked as reconstruction (paper describes the mechanism but does not publish the prompt verbatim).
