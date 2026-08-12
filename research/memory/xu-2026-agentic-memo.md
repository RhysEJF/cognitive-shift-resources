---
corpus: agentic-memory
kind: paper-digest
slug: xu-2026-agentic-memo
title: "Contextual Agentic Memory is a Memo, Not True Memory"
authors:
  - "Xu, Binyan"
  - "Dai, Xilin"
  - "Zhang, Kehuan"
year: 2026
publication_date: "2026-04"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2604.27707"
doi: null
arxiv_id: "2604.27707"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Current agentic memory systems (vector stores, RAG, scratchpads, MemGPT-style context paging) implement lookup, not memory — a category error with a provable generalization ceiling, a frozen-novice dynamic, and a structurally compounding prompt-injection attack surface that no amount of better retrieval can fix; the missing piece is a consolidation pathway from the episodic store into model weights."
topics:
  - agentic-memory
  - retrieval-augmented-generation
  - continual-learning
  - complementary-learning-systems
  - prompt-injection
  - compositional-generalization
  - knowledge-editing
  - llm-agents
tags:
  - paper
  - position-paper
  - theory
  - security
  - memory-architecture
  - fine-tuning
  - weight-based-learning
entities:
  - xu-binyan
  - dai-xilin
  - zhang-kehuan
related_digests:
  - mcclelland-1995-complementary-learning-systems
  - wang-2023-voyager-embodied-agent
  - chhikara-2025-mem0
  - li-2025-memos
  - maharana-2024-locomo
  - du-2025-rethinking-memory
  - mao-2026-agent-memory-circuits
  - ma-2026-nemori-distillation
citations:
  - title: "What learning algorithm is in-context learning? Investigations with linear models"
    authors: ["Akyürek, E.", "Schuurmans, D.", "Andreas, J.", "Ma, T.", "Zhou, D."]
    year: 2023
    venue: "ICLR"
    url: "https://openreview.net/forum?id=0g0X4H8yN4I"
    arxiv_id: null
  - title: "Human category learning 2.0"
    authors: ["Ashby, F. G.", "Maddox, W. T."]
    year: 2011
    venue: "Annals of the New York Academy of Sciences"
    doi: "10.1111/j.1749-6632.2010.05874.x"
    url: null
  - title: "Nested learning: The illusion of deep learning architectures"
    authors: ["Behrouz, A.", "Razaviyayn, M.", "Zhong, P.", "Mirrokni, V."]
    year: 2026
    venue: "NeurIPS"
    url: "https://openreview.net/forum?id=nbMeRvNb7A"
  - title: "Improving language models by retrieving from trillions of tokens (RETRO)"
    authors: ["Borgeaud, S.", "et al."]
    year: 2021
    venue: "ICML"
    url: null
  - title: "How People Learn: Brain, Mind, Experience, and School"
    authors: ["Bransford, J. D.", "Brown, A. L.", "Cocking, R. R."]
    year: 2000
    venue: "National Academy Press"
  - title: "Sleep — a brain-state serving systems memory consolidation"
    authors: ["Brodt, S.", "Inostroza, M.", "Niethard, N.", "Born, J."]
    year: 2023
    venue: "Neuron"
  - title: "Mem0: Building production-ready AI agents with scalable long-term memory"
    authors: ["Chhikara, P.", "Khant, D.", "Aryan, S.", "Singh, T.", "Yadav, D."]
    year: 2025
    url: "https://arxiv.org/abs/2504.19413"
    arxiv_id: "2504.19413"
  - title: "Categorization and representation of physics problems by experts and novices"
    authors: ["Chi, M. T. H.", "Feltovich, P. J.", "Glaser, R. E."]
    year: 1981
    venue: "Cognitive Science"
  - title: "Elements of Information Theory (2nd ed.)"
    authors: ["Cover, T. M.", "Thomas, J. A."]
    year: 2006
    venue: "Wiley-Interscience"
  - title: "Why can GPT learn in-context? Language models secretly perform gradient descent as meta-optimizers"
    authors: ["Dai, D.", "Sun, Y.", "Dong, L.", "Hao, Y.", "Ma, S.", "Sui, Z.", "Wei, F."]
    year: 2023
    venue: "Findings of ACL"
  - title: "MINJA: Memory injection attacks on LLM agents via query-only interaction"
    authors: ["Dong, S.", "Xu, S.", "He, P.", "Li, Y.", "Tang, J.", "Liu, T.", "Liu, H.", "Xiang, Z."]
    year: 2026
    venue: "NeurIPS"
    url: "https://openreview.net/forum?id=QINnsnppv8"
  - title: "Transformer feed-forward layers are key-value memories"
    authors: ["Geva, M.", "Schuster, R.", "Berant, J.", "Levy, O."]
    year: 2020
    arxiv_id: "2012.14913"
  - title: "Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection"
    authors: ["Greshake, K.", "Abdelnabi, S.", "Mishra, S.", "Endres, C.", "Holz, T.", "Fritz, M."]
    year: 2023
    venue: "AISec"
  - title: "LoRA: Low-rank adaptation of large language models"
    authors: ["Hu, E. J.", "Shen, Y.", "Wallis, P.", "Allen-Zhu, Z.", "Li, Y.", "Wang, S.", "Wang, L.", "Chen, W."]
    year: 2022
    venue: "ICLR"
  - title: "Memory in the age of AI agents"
    authors: ["Hu, Y.", "et al."]
    year: 2026
    arxiv_id: "2512.13564"
    url: "https://arxiv.org/abs/2512.13564"
  - title: "Mitigating catastrophic forgetting in large language models with self-synthesized rehearsal (SSR)"
    authors: ["Huang, J.", "Cui, L.", "Wang, A.", "Yang, C.", "Liao, X.", "Song, L.", "Yao, J.", "Su, J."]
    year: 2024
    arxiv_id: "2403.01244"
  - title: "Continual learning of natural language processing tasks: A survey"
    authors: ["Ke, Z.", "Liu, B."]
    year: 2023
    arxiv_id: "2211.12701"
  - title: "Generalization through memorization: Nearest neighbor language models (kNN-LM)"
    authors: ["Khandelwal, U.", "Levy, O.", "Jurafsky, D.", "Zettlemoyer, L.", "Lewis, M."]
    year: 2020
    venue: "ICLR"
  - title: "COGS: A compositional generalization challenge based on semantic interpretation"
    authors: ["Kim, N.", "Linzen, T."]
    year: 2020
    venue: "EMNLP"
  - title: "Overcoming catastrophic forgetting in neural networks (EWC)"
    authors: ["Kirkpatrick, J.", "et al."]
    year: 2016
    venue: "PNAS"
  - title: "Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks (SCAN)"
    authors: ["Lake, B. M.", "Baroni, M."]
    year: 2017
    venue: "ICML"
  - title: "Latent learning: Episodic memory complements parametric learning by enabling flexible reuse of experiences"
    authors: ["Lampinen, A. K.", "Engelcke, M.", "Li, Y.", "Chaudhry, A.", "McClelland, J. L."]
    year: 2025
    arxiv_id: "2509.16189"
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Lewis, P.", "et al."]
    year: 2021
    arxiv_id: "2005.11401"
  - title: "MemOS: An operating system for memory-augmented generation (MAG) in large language models"
    authors: ["Li, Z.", "et al."]
    year: 2025
    arxiv_id: "2505.22101"
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Liu, N. F.", "Lin, K.", "Hewitt, J.", "Paranjape, A.", "Bevilacqua, M.", "Petroni, F.", "Liang, P."]
    year: 2023
    venue: "TACL"
  - title: "Why there are complementary learning systems in the hippocampus and neocortex"
    authors: ["McClelland, J. L.", "McNaughton, B. L.", "O'Reilly, R. C."]
    year: 1995
    venue: "Psychological Review"
  - title: "Locating and editing factual associations in GPT (ROME)"
    authors: ["Meng, K.", "Bau, D.", "Andonian, A.", "Belinkov, Y."]
    year: 2022
    venue: "NeurIPS"
  - title: "Mass-editing memory in a transformer (MEMIT)"
    authors: ["Meng, K.", "Sharma, A. S.", "Andonian, A.", "Belinkov, Y.", "Bau, D."]
    year: 2023
    venue: "ICLR"
  - title: "Rule-plus-exception model of classification learning"
    authors: ["Nosofsky, R. M.", "Palmeri, T. J.", "McKinley, S. C."]
    year: 1994
    venue: "Psychological Review"
  - title: "Complementary learning systems"
    authors: ["O'Reilly, R. C.", "Bhattacharyya, R.", "Howard, M. D.", "Ketz, N."]
    year: 2014
    venue: "Cognitive Science"
  - title: "Fine-tuning or retrieval? Comparing knowledge injection in LLMs"
    authors: ["Ovadia, O.", "Brief, M.", "Mishaeli, M.", "Elisha, O."]
    year: 2024
    venue: "EMNLP"
  - title: "Continual learning in token space"
    authors: ["Packer, C."]
    year: 2025
    venue: "Letta Research Blog"
    url: "https://www.letta.com/blog/continual-learning"
  - title: "MemGPT: Towards LLMs as operating systems"
    authors: ["Packer, C.", "Wooders, S.", "Lin, K.", "Fang, V.", "Patil, S. G.", "Stoica, I.", "Gonzalez, J. E."]
    year: 2024
    arxiv_id: "2310.08560"
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["Park, J. S.", "O'Brien, J. C.", "Cai, C. J.", "Morris, M. R.", "Liang, P.", "Bernstein, M. S."]
    year: 2023
    venue: "ACM UIST"
  - title: "Context is what you need: The maximum effective context window for real world limits of LLMs"
    authors: ["Paulsen, N."]
    year: 2026
    venue: "Adv. AI & ML"
    doi: "10.54364/aaiml.2026.61268"
  - title: "The protection of information in computer systems"
    authors: ["Saltzer, J. H.", "Schroeder, M. D."]
    year: 1975
    venue: "Proc. IEEE"
  - title: "Reflexion: Language agents with verbal reinforcement learning"
    authors: ["Shinn, N.", "Cassano, F.", "Labash, B.", "Gopinath, A.", "Narasimhan, K.", "Yao, S."]
    year: 2023
    venue: "NeurIPS"
  - title: "Learning to (learn at test time): RNNs with expressive hidden states (TTT layers)"
    authors: ["Sun, Y.", "et al."]
    year: 2025
    arxiv_id: "2407.04620"
  - title: "Statistical Learning Theory"
    authors: ["Vapnik, V. N."]
    year: 1998
    venue: "Wiley"
  - title: "Voyager: An open-ended embodied agent with large language models"
    authors: ["Wang, G.", "Xie, Y.", "Jiang, Y.", "Mandlekar, A.", "Xiao, C.", "Zhu, Y.", "Fan, L.", "Anandkumar, A."]
    year: 2023
    arxiv_id: "2305.16291"
  - title: "Skill-SD: Skill-conditioned self-distillation for multi-turn LLM agents"
    authors: ["Wang, H.", "et al."]
    year: 2026
    arxiv_id: "2604.10674"
  - title: "Memory in the LLM era: Modular architectures and strategies in a unified framework (LoCoMo benchmark)"
    authors: ["Wu, Y.", "Lin, T.", "Zhou, Y.", "et al."]
    year: 2026
    arxiv_id: "2604.01707"
  - title: "A-MEM: Agentic memory for LLM agents"
    authors: ["Xu, W.", "Liang, Z.", "Mei, K.", "Gao, H.", "Tan, J.", "Zhang, Y."]
    year: 2025
    arxiv_id: "2502.12110"
  - title: "Fine-tuning vs. RAG for multi-hop question answering with novel knowledge"
    authors: ["Yang, Z.", "Song, Y.", "Ahmed, I.", "Harris, I."]
    year: 2026
    arxiv_id: "2601.07054"
  - title: "ParamMem: Augmenting language agents with parametric reflective memory"
    authors: ["Yao, T.", "Chen, Y.", "Zheng, Y.", "Li, P.", "Shen, Z.", "Zhang, K."]
    year: 2026
    arxiv_id: "2602.23320"
  - title: "Knowledge circuits in pretrained transformers"
    authors: ["Yao, Y.", "Zhang, N.", "Xi, Z.", "Wang, M.", "Xu, Z.", "Deng, S.", "Chen, H."]
    year: 2024
    venue: "NeurIPS"
  - title: "Analyzing the effects of supervised fine-tuning on model knowledge from token and parameter levels"
    authors: ["Ye, J.", "Yang, Y.", "Nan, Y.", "Li, S.", "Zhang, Q.", "Gui, T.", "Huang, X.", "Wang, P.", "Shi, Z.", "Fan, J."]
    year: 2025
    venue: "EMNLP"
  - title: "Self-consolidation for self-evolving agents"
    authors: ["Yu, H.", "Zhu, F.", "Xie, G.-S.", "Shao, L."]
    year: 2026
    arxiv_id: "2602.01966"
  - title: "InjecAgent: Benchmarking indirect prompt injections in tool-integrated LLM agents"
    authors: ["Zhan, Q.", "Liang, Z.", "Ying, Z.", "Kang, D."]
    year: 2024
    venue: "Findings of ACL"
  - title: "MemRL: Self-evolving agents via runtime reinforcement learning on episodic memory"
    authors: ["Zhang, S.", "et al."]
    year: 2026
    arxiv_id: "2601.03192"
  - title: "Experience compression spectrum: Unifying memory, skills, and rules in LLM agents"
    authors: ["Zhang, X.", "Wang, G.", "Cui, Y.", "Qiu, W.", "Li, Z.", "Zhu, B.", "He, P."]
    year: 2026
    arxiv_id: "2604.15877"
  - title: "A survey on the memory mechanism of large language model based agents"
    authors: ["Zhang, Z.", "Bo, X.", "Ma, C.", "Li, R.", "Chen, X.", "Dai, Q.", "Zhu, J.", "Dong, Z.", "Wen, J.-R."]
    year: 2024
    arxiv_id: "2404.13501"
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Zhong, W.", "Guo, L.", "Gao, Q.", "Ye, H.", "Wang, Y."]
    year: 2024
    venue: "AAAI"
  - title: "Memento: Fine-tuning LLM agents without fine-tuning LLMs"
    authors: ["Zhou, H.", "Chen, Y.", "Guo, S.", "Yan, X.", "Lee, K. H.", "Wang, Z.", "Lee, K. Y.", "Zhang, G.", "Shao, K.", "Yang, L.", "Wang, J."]
    year: 2025
    arxiv_id: "2508.16153"
  - title: "PoisonedRAG: Knowledge corruption attacks to retrieval-augmented generation"
    authors: ["Zou, W.", "Geng, R.", "Wang, B.", "Jia, J."]
    year: 2024
    venue: "USENIX Security"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Memory taxonomy for LLM agents — the Experiential row (weight-based encoding of lived experience) is the gap"
  page: 2
  image_path: "figures/xu-2026-agentic-memo-fig.png"
---

# Contextual Agentic Memory is a Memo, Not True Memory

**Authors:** Binyan Xu, Xilin Dai, Kehuan Zhang
**Published:** 2026-04 · [Source](https://arxiv.org/abs/2604.27707)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

A position paper from CUHK and Zhejiang University that takes aim at the entire post-2023 agentic-memory stack — MemGPT, RAG, Reflexion, Voyager, MemoryBank, A-MEM, mem0, MemOS — and argues they are all making the same mistake: they implement *lookup*, not *memory*. The authors formalize a distinction between two ways to change what an LLM agent outputs: change θ (the weights, via fine-tuning, knowledge editing, continual learning) or change C (the context window, via prompting, RAG, scratchpads, MCP). Every deployed agentic-memory system today operates only on C. The authors prove this matters by deriving a **Compositional Sample Complexity Separation theorem** (Theorem 1): under the mild assumption that the frozen base model's in-context composition accuracy on a domain-specific operator ⊕ is bounded by some ᾱ < 1, retrieval-based memory needs Ω(k²) stored examples to reach a given accuracy on compositionally novel concept pairs, while parametric memory needs only O(d + log(1/δ)/δ) where d is the VC dimension of the operator class. The ratio nR/nP = Ω(k²/d) grows with the size of the domain and is **independent of context-window size and retrieval quality** — bigger context or better retrieval cannot close it. They then connect this to three real consequences: (1) a "frozen novice" problem (every session begins from the same frozen weights, so accumulated experience never becomes expertise), (2) a security compounding effect (transient prompt injections written to a persistent store become permanent compromise — empirically 98.2% success on MINJA, 90% on PoisonedRAG with just 5 adversarial texts), and (3) a structural mismatch between what current benchmarks (LoCoMo, LongMem) measure (recall) and what actually matters for learning (compositional generalization over time). The fix they propose is not better retrieval but a **consolidation channel**: an offline pipeline that distills agent traces into weight updates via LoRA / MEMIT / SSR / TTT / Skill-SD, with versioned checkpoints and trace provenance for auditability — the AI analog of biological sleep. Three calls to action: system builders should build the consolidation channel; benchmark designers should adopt "Compositional Generalization over Time" (CGT) as a standard metric; the continual learning community should re-engage the agentic setting as its natural deployment target.

## Key Takeaway

The field has been conflating "what we shipped because it was safe to ship" with "a sufficient substitute for learning," and that conflation is a category error with provable consequences — not a philosophical preference. A Reflexion agent with ten thousand verbal self-critiques is still running the same frozen base model on every call; its filing cabinet grows while its capacity does not. The authors' core move is to refuse the framing that retrieval and memory are points on a spectrum and instead show they are *structurally different*: retrieval compresses knowledge into text bounded by context length L and generalizes only by similarity to stored cases; weight-based memory compresses knowledge into the model's parameters and generalizes by applying abstract rules to inputs never seen before. Once you accept this distinction, the implications are sharp and unavoidable: (i) capability ceiling — no matter how big the context, retrieval cannot solve compositionally novel inputs the base model cannot already solve; (ii) capability stagnation — agents that only do C-engineering never get better at composing knowledge no matter how much they "experience"; (iii) compromise asymmetry — corrupting C requires only one successful injection per store-lifetime (after which p₀ becomes irrelevant and P(compromised by time t) → 1), while corrupting θ requires training-time access. The architectural fix is not exotic: every component for a consolidation channel already exists (LoRA, MEMIT, SSR, TTT, Skill-SD, Nested Learning). The bottleneck is design choice, not feasibility. What is genuinely hard is *policy* — which traces to consolidate, when to consolidate, and how to validate that consolidation produced rule extraction rather than rote memorization of distilled examples.

## Implications

- **For the agent-tooling market**: every product positioned as "long-term memory for AI agents" — Mem0, A-MEM, MemoryBank, Letta/MemGPT, MemOS — is, by this paper's definition, selling better filing cabinets. They are useful (auditable, reversible, safe to deploy) but they cannot deliver the "agent that learns from experience" narrative buyers expect. A second-mover wedge exists for someone who ships the consolidation channel on top of an existing episodic store. The paper itself flags Wang et al. 2026 (Skill-SD) and Yu et al. 2026 (self-consolidation) as already implementing variants of this — early-mover but not yet productized.
- **For anyone building agent frameworks** (LangGraph, CrewAI, AutoGen, Letta): the architectural roadmap the paper draws is fast episodic store + offline consolidation pipeline with versioned weight checkpoints. If your framework treats retrieval as the only persistence layer, you are baking in the ceiling Theorem 1 describes.
- **For the security posture of any agent deployed on a multi-month timeframe**: this paper turns prompt injection from a transient nuisance into a structural risk. The math is brutal — P(compromised by t) = 1 − (1 − p₀)^N(t) → 1 as N(t) → ∞. Provenance-based defenses reduce p₀ but cannot close the convergent bound. Anyone deploying long-running agents needs trace provenance and rollbackable checkpoints, not just better input filters. This is also a load-bearing claim *for* parametric learning over retrieval: anomalous weight changes are detectable via activation analysis; anomalous entries in an unboundedly-growing vector store are not.
- **For evaluation**: if you are benchmarking agent memory with LoCoMo or LongMem and reporting recall accuracy, you are measuring lookup quality, not learning. The proposed CGT (Compositional Generalization over Time) metric — train agent on concepts in isolation for T sessions, then evaluate on combinations not seen during operation — is the kind of metric that would expose the frozen-novice problem in production agents.
- **For the continual-learning research community**: the paper is also a recruitment pitch. CL has been sidelined by the field's retrieval pivot; the authors argue the agentic setting is precisely the deployment target CL has lacked, with a natural experience stream, reward labels (task success/failure), and a clean generalization criterion (compositional novelty).
- **A bounded but pointed implication**: this is a position paper with no new empirical results of its own. The argument relies on assembling existing empirical results (Yao et al. 2026 ParamMem, Ovadia et al. 2024 fine-tuning > RAG on compositional reasoning, Yang et al. 2026 multi-hop, Lampinen et al. 2025 latent learning) plus a clean theoretical formulation. Whether the paper actually shifts the field's defaults depends on whether the empirical case for parametric > retrieval on compositional novelty continues to accumulate in 2026-2027 — the authors stake their claim on the assumption it will.

## How to Apply It (method)

The paper itself is structured as: definitions (Section 2) → four structural limitations (Section 3) → four alternative views and refutations (Section 4) → call to action (Section 5). The actionable methodology is in Section 5 and is worth treating as a checklist for anyone building or evaluating agentic-memory systems.

**For system builders — three design principles:**

1. **Treat agentic memory as episodic lookup only.** Vector stores and RAG are the right tools for recent context, tool outputs, and reference retrieval. Stop expecting them to produce generalization. Stop designing architectures as if they will.
2. **Add a consolidation channel as a second pathway.** The architecture must include a path from the episodic store to model weights. Mechanism is a design choice: periodic fine-tuning (LoRA), knowledge editing (ROME/MEMIT), test-time training (TTT layers), self-distillation from traces (Skill-SD), or self-synthesized rehearsal (SSR). The pathway must run asynchronously so the agent serves from agentic memory while consolidation proceeds in the background — biological sleep does not interrupt wakefulness.
3. **Make consolidation safe by construction.** Three engineering requirements: **trace provenance** (every distilled experience auditable to its source), **versioned weight checkpoints** (any bad consolidation rollbackable at bounded cost), **regression guards** (consolidation blocked when downstream metrics degrade). These restore the auditability that motivated the original pivot to episodic storage, extended to the parametric level.

**The hard questions for system builders** are not mechanism but policy: *which* traces are worth consolidating (not all carry generalizable signal), *when* to consolidate (too early overfits noise, too late accumulates stale traces), and *how* to validate that consolidation produced compositional generalization rather than rote memorization.

**For benchmark designers — two redirections:**

- **Compositional Generalization over Time (CGT)** — operate the agent on a domain for T sessions exposing concepts only in isolation; then evaluate on queries requiring combinations not seen during operation. A genuinely learning agent shows accuracy strictly increasing with T; a pure-retrieval agent shows flat-at-baseline accuracy. The authors explicitly ask LoCoMo, LongMem, and AgentBench to adopt CGT.
- **Beyond SFT evaluation** — Yao et al. 2024 and Ye et al. 2025 show that standard SFT modifies attention routers but not fact-memory units (90% of SFT parameter updates contribute nothing to knowledge enhancement). Benchmarks that evaluate "knowledge update" via SFT are measuring access rearrangement, not learning. Future benchmarks should evaluate knowledge update via targeted weight editing, circuit-aware fine-tuning, and self-distillation from agent traces.

**What not to do:** do not benchmark "memory capacity" by context-window length. Longer context enlarges the filing cabinet; it does not address the compositional generalization gap.

**For the continual-learning community — a deployment target:** the agentic setting provides what CL has lacked (natural experience stream, reward labels, clean generalization criterion); CL provides what agentic systems lack (consolidation machinery — replay, regularization, progressive expansion — that converts episodic experience into durable knowledge without catastrophic forgetting). Concrete research agenda: coreset selection / influence functions for *which* traces to consolidate; existing online-vs-batch scheduling theory for *when*; new empirical work on *validation* of rule-extraction vs rote-memorization outcomes.

## Best Figure

![Figure 1 — Memory taxonomy for LLM agents — the Experiential row (weight-based encoding of lived experience) is the gap (page 2)](figures/xu-2026-agentic-memo-fig.png)

The paper has no diagrams — only tables and equations — but **Table 1** on page 2 carries the conceptual payload of the entire argument and is the right artifact to anchor a reader's intuition. It maps four memory types along three axes: substrate (where it lives), persistence horizon, update mechanism, and generalization mode. *Working* memory (context window) is session-only, updated by token generation, and limited by context length L. *Episodic* memory (external store) persists cross-session, updated by read/write ops, generalizes by exemplar. *Semantic* memory (model weights) is permanent, updated by pretraining, generalizes by rule. The fourth row — *Experiential* (model weights, permanent, updated by fine-tuning/continual learning, rule-based) — is highlighted in the caption as "the gap." Every deployed agentic-memory system in the field today sits in the Episodic row. The Experiential row exists in principle (the technology — LoRA, MEMIT, TTT — is available) but is systemically absent from production architectures. The visual rhetoric of the table is that the row labeled *experiential* — the one whose substrate, persistence, and generalization mode actually match the colloquial sense of "the agent learned from its experience" — is the empty cell in the field's roadmap.

## What Experts Overlook

- **The "best engineering compromise available" trap.** The authors are careful to grant that retrieval was the right thing to ship — it is reversible, auditable, and safe under production constraints. The category error is not the choice to deploy retrieval; it is the subsequent conflation of "what we shipped" with "what suffices." This is a subtler critique than the standard "fine-tuning vs RAG" debate. The authors are arguing that even RAG advocates who'd happily fine-tune *if it were cheaper* are still misreading the situation: it is not a cost-benefit choice between two interchangeable approaches; the two approaches occupy structurally different parts of the memory taxonomy and produce qualitatively different agent capabilities. Pretending otherwise is what's allowed the field to optimize lookup quality for three years while believing it was optimizing learning quality.
- **Context-window growth does not help.** The most common counterargument to RAG critiques is "well, when context windows hit 10M tokens, the distinction collapses." The paper takes this head-on and shows it does not: the Ω(k²) coverage requirement on stored compositions is independent of K (the retrieval-budget / context-window size). Increasing K can only raise ᾱ marginally — it cannot remove the structural coverage requirement. Paulsen 2026 is cited showing effective context utilization saturates at ~20k tokens even for 128k-token models, an independent empirical anchor for this. The "longer context will fix it" argument is precisely the trap the paper is calling out: it assumes the constraint is capacity when the constraint is generativity.
- **The security argument is the sharpest under-discussed claim.** Most prompt-injection discussion frames injections as transient one-shot events. The paper formalizes the persistent case: once injected content is written to a persistent store, p₀ is no longer the per-session risk — it is the one-time probability of reaching the store, after which the convergent bound P(compromised by t) = 1 − (1 − p₀)^N(t) → 1 takes over. This converts a *probability* discussion (acceptable false-positive rate) into a *time-to-certainty* discussion (how long until compromise is effectively guaranteed). The implication that anomalous weight changes are detectable via activation analysis while anomalous store entries require semantic audit of an unboundedly growing corpus is the *security* reason to want parametric over retrieval — independent of the capability reason. Few RAG-vs-fine-tuning debates have foregrounded this.
- **The "implicit gradient descent" defense of ICL gets a precise rebuttal.** A sophisticated reader who knows Akyürek et al. 2023 / Dai et al. 2023 might argue ICL already implicitly does gradient descent — so the C/θ distinction is moot. The paper accepts the result and turns it: yes, ICL implicitly implements a gradient step; *but* the implicit update is ephemeral (base weights are unchanged at session end), and the result is anyway derived under linear self-attention assumptions that break for modern multi-layer Transformers with softmax attention and LayerNorm. The correct fix the paper extracts: make the gradient-like update *persistent*. That is, the ICL=GD result actually *supports* the consolidation argument rather than undermining it.
- **Learned retrieval does not save you either.** Recent systems (MemRL, Memento) learn the retrieval policy rather than relying on static similarity. The paper specifically addresses these and shows that optimizing *which* exemplars to retrieve improves ᾱ but does not eliminate the Ω(k²) coverage requirement on the underlying store. Performance gains from learned retrieval are better explained by reduced retrieval noise for *seen* compositions than by generalization to novel ones. Lampinen et al. 2025 (oracle-conditioned episodic retrieval) is cited as the corroborating boundary case: ideal retrieval unlocks abilities *already encoded* in pretrained weights — the ᾱ → 1 regime where the separation narrows.
- **The mechanistic interpretability undercut to SFT.** Yao et al. 2024 show factual knowledge is stored in specific fact-memory units in FFN neurons, and SFT does not modify these units — it modifies attention routers (how to *access* knowledge). Ye et al. 2025 quantify this: 90% of SFT parameter updates contribute nothing to knowledge enhancement. This is a sharp empirical claim that the field's standard "fine-tune to inject knowledge" practice is largely cosmetic, and that targeted weight editing (ROME/MEMIT) or circuit-aware fine-tuning is what actually moves knowledge into weights. This matters for the consolidation channel design — naive SFT on agent traces will not work.
- **The paper is honest about its assumption boundary.** Assumption 3.2 (the frozen model's in-context composition accuracy ᾱ < 1) is the load-bearing input to Theorem 1. The authors note that when ⊕ is broadly general — i.e., already covered in pretraining — ᾱ → 1 and the separation vanishes. The argument *binds* precisely in domain-specific deployments (post-cutoff clinical protocols, enterprise legal conventions, specialized engineering standards) where persistent agents are most valuable. This is the right scoping: it narrows the claim to where it actually matters and avoids overclaiming on tasks where retrieval is genuinely sufficient.

## Extracted Prompts

The paper contains no prompt templates — it is a theoretical position paper, not an empirical methods paper. There are no example prompts, system messages, evaluation prompts, or chain-of-thought templates to extract. The closest analog is the formal language of the **co-existence architecture** the paper proposes:

```
Architecture sketch (paraphrased from Section 5):

  AGENT LOOP (online, wakeful):
    fast_episodic_store ← READ_WRITE  (retrieval / scratchpad / RAG)
    response ← model_θ(query, retrieve_K(query, fast_episodic_store))

  CONSOLIDATION CHANNEL (offline, async — the "sleep" pathway):
    candidate_traces ← select_for_generalizable_signal(fast_episodic_store)
    distilled ← compress_to_rules(candidate_traces)            # e.g. Skill-SD
    θ_new ← apply_weight_update(θ, distilled)                  # e.g. LoRA / MEMIT / SSR / TTT
    if regression_guard(θ_new) passes:
        promote(θ_new) with provenance(distilled) and checkpoint(θ_old)
    else:
        rollback to θ_old
```

This is a system-architecture description, not a literal prompt. Readers expecting LLM-prompt templates from this paper will be disappointed — its contribution is conceptual.

## Citations

The paper cites 50 works. The most load-bearing for the central argument:

- McClelland, McNaughton & O'Reilly (1995) — **Complementary Learning Systems** — neuroscience foundation for the hippocampus/neocortex argument.
- Chi, Feltovich & Glaser (1981) — physics experts vs novices — empirical grounding for "expertise is reorganization, not accumulation."
- Packer et al. (2024) — **MemGPT**; Park et al. (2023) — **Generative Agents**; Shinn et al. (2023) — **Reflexion**; Wang et al. (2023) — **Voyager** — the four canonical agentic-memory systems the paper critiques.
- Lewis et al. (2021) — **RAG** — the paper notes RAG was originally framed as *augmenting* parametric memory; the field inverted the framing.
- Meng et al. (2022) — **ROME**; Meng et al. (2023) — **MEMIT** — existence proof that weight-based memory editing works.
- Yao et al. (2026) — **ParamMem** — empirical proof that parametric storage outperforms external storage on agent reflections.
- Ovadia et al. (2024) — fine-tuning vs RAG on compositional reasoning; Yang et al. (2026) — fine-tuning vs RAG on multi-hop QA — corroborating empirical results.
- Lampinen et al. (2025) — latent learning / oracle-conditioned retrieval — boundary-case evidence.
- Liu et al. (2023) — **Lost in the Middle**; Paulsen (2026) — effective context saturates ~20k — capacity-bound evidence.
- Lake & Baroni (2017) — **SCAN**; Kim & Linzen (2020) — **COGS** — compositional generalization benchmarks where weight-based models outperform retrieval-only.
- Dong et al. (2026) — **MINJA** (98.2% memory injection success); Zou et al. (2024) — **PoisonedRAG** (5 adversarial texts → 90% attack success); Zhan et al. (2024) — **InjecAgent** — security empirical results.
- Greshake et al. (2023) — indirect prompt injection — foundational security framing.
- Saltzer & Schroeder (1975) — "all inputs are evil" — classical security principle the paper invokes.
- Hu et al. (2022) — **LoRA**; Kirkpatrick et al. (2016) — **EWC**; Huang et al. (2024) — **SSR**; Sun et al. (2025) — **TTT layers**; Wang et al. (2026) — **Skill-SD**; Behrouz et al. (2026) — **Nested Learning** — the consolidation toolkit the paper says already exists.
- Yao et al. (2024) — **Knowledge circuits in transformers**; Ye et al. (2025) — 90% of SFT updates do not enhance knowledge — the mechanistic undercut to naive SFT.
- Zhang et al. (2026b) — **Experience Compression Spectrum** — the framing the paper unifies with its C/θ distinction.
- Zhang et al. (2026a) — **MemRL**; Zhou et al. (2025) — **Memento** — learned-retrieval systems the paper refutes as a substitute.
- Hu et al. (2026) — **Memory in the age of AI agents** survey; Wu et al. (2026) — **LoCoMo** — context for the field-wide state.

Full structured citation list is in the frontmatter.

## Related Digests

- [[mcclelland-1995-complementary-learning-systems]] — Why There Are Complementary Learning Systems in the Hippocampus and Neocortex — directly cited as the neuroscience foundation for the paper's "fast episodic + slow consolidation" prescription
- [[wang-2023-voyager-embodied-agent]] — Voyager: An Open-Ended Embodied Agent with LLMs — explicitly named as one of the four canonical C-engineering agentic-memory systems the paper critiques
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory — cited as a recent system continuing the same paradigm with richer indexing
- [[li-2025-memos]] — MemOS: A Memory OS for AI System — cited as realizing a variant of the consolidation channel the paper proposes
- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents — exactly the kind of recall-focused benchmark the paper argues misses the learning question
- [[du-2025-rethinking-memory]] — Rethinking Memory in LLM-based Agents — adjacent critical-stance survey, also questions the prevailing memory framings
- [[mao-2026-agent-memory-circuits]] — What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis — mechanistic-interpretability angle on agent memory, complements the paper's "memory should live in weights" thesis
- [[ma-2026-nemori-distillation]] — What Deserves Memory: Adaptive Memory Distillation for LLM Agents — directly addresses the "which traces to consolidate" hard question this paper flags

## Reviewer Notes

**Overall severity: Clean.**

The digest faithfully represents the paper's central claims, methodology, and empirical anchors. Spot-checks against the source text:

- **Theorem 1 statement and ratio** (`nR/nP = Ω(k²/d)`): correctly reproduced. The digest specifies the structured-operator case (d = O(k) → ratio Ω(k)) and the maximally-structured case (d = O(1) → ratio Ω(k²)) — matches paper.
- **Assumption 3.2 framing** (`ᾱ < 1` for the frozen model's ICL composition accuracy): correctly characterized, including the paper's important note that when ᾱ → 1 the separation vanishes. The digest correctly notes Appendix C strengthens this from "assumption" to "theorem under log|H| > K log|Y|."
- **98.2% MINJA success rate, 90% PoisonedRAG with 5 adversarial texts**: verified verbatim against Section 3.4.
- **P(compromised by t) = 1 − (1 − p₀)^N(t) → 1 as N(t) → ∞**: verified verbatim against Section 3.4.
- **The four canonical critiqued systems** (MemGPT, Generative Agents, Reflexion, Voyager): all correctly attributed.
- **Three CTA pillars** (system builders, benchmark designers, continual-learning community): match the Section 5 structure exactly.
- **CGT proposal** (Compositional Generalization over Time): correctly described as "exposing concepts only in isolation for T sessions, then evaluating on combinations not seen during operation, expecting accuracy strictly increasing with T for a genuinely learning agent."
- **90% of SFT updates contribute nothing to knowledge enhancement** (Ye et al. 2025): verified verbatim.
- **Best Figure** is Table 1 — paper genuinely has no diagrams, only tables and equations. The crop captures Table 1 in full including caption.
- **Citations**: 50 cited works captured in frontmatter with author lists, years, venues, and arxiv IDs / URLs where the paper provided them. A few citations had only Semantic Scholar CorpusIDs in the paper; those are captured with the venue and year and no URL/arxiv_id rather than fabricating identifiers.
- **One small framing note for the reader, not a correction**: the digest characterizes this as a *position paper with no new empirical results of its own* — which is accurate. The paper's contribution is the theorem, the security bound, the taxonomy, and the synthesis of existing empirical work into a coherent indictment. Readers expecting benchmark numbers or an implemented consolidation pipeline will not find them here. The paper itself flags this and treats it as appropriate scoping.

No fabricated facts, citations, or claims detected. No invented numerical values. No mischaracterization of cited works (the digest's brief descriptions of ParamMem, MINJA, PoisonedRAG, Lost-in-the-Middle, ROME, MEMIT, etc., all match the paper's own framing of them).
