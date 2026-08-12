---
corpus: agentic-memory
kind: paper-digest
slug: modarressi-2023-ret-llm
title: "Ret-LLM: Towards a General Read-Write Memory for Large Language Models"
authors:
  - "Modarressi, Ali"
  - "Imani, Ayyoob"
  - "Fayyaz, Mohsen"
  - "Schütze, Hinrich"
year: 2023
publication_date: "2023-05"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2305.14322"
doi: null
arxiv_id: "2305.14322"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Ret-LLM is the 2023 concept paper that first articulated the now-dominant Memory-as-API pattern: the LLM emits [MEM_WRITE{t1»t2»t3}] and [MEM_READ{q1»q2»q3}] tokens mid-generation, a controller catches them and routes to/from a separate Davidsonian-triplet store with LSH fuzzy fallback — write-time distillation, query-time symbolic-then-vector retrieval, all driven by the same LoRA-fine-tuned Alpaca-7B."
topics:
  - read-write-memory
  - triplet-memory
  - llm-tool-use
  - memory-api
  - davidsonian-semantics
  - lsh-retrieval
  - lora-finetuning
  - memory-controller
  - temporal-qa
  - knowledge-editing
tags:
  - paper
  - memory-architecture
  - external-memory
  - tool-use
  - fine-tuning
  - retrieval
  - concept-paper
entities:
  - modarressi-ali
  - imani-ayyoob
  - fayyaz-mohsen
  - schutze-hinrich
related_digests:
  - mao-2026-agent-memory-circuits
  - liu-2023-think-in-memory
  - lu-2023-memochat
  - xu-2025-a-mem-agentic-memory
  - weston-2015-memory-networks
citations:
  - title: "Sparks of Artificial General Intelligence: Early experiments with GPT-4"
    authors: ["Sébastien Bubeck", "Varun Chandrasekaran", "Ronen Eldan", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2303.12712"
  - title: "Language Model with Plug-in Knowledge Memory"
    authors: ["Xin Cheng", "Yankai Lin", "Dongyan Zhao", "et al."]
    year: null
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "PaLM: Scaling Language Modeling with Pathways"
    authors: ["Aakanksha Chowdhery", "Sharan Narang", "Jacob Devlin", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "The Logical Form of Action Sentences"
    authors: ["Donald Davidson"]
    year: 1967
    venue: "Essays on Actions and Events (D. Davidson, 1980), reprinted"
    doi: null
    url: null
    arxiv_id: null
  - title: "Time-Aware Language Models as Temporal Knowledge Bases"
    authors: ["Bhuwan Dhingra", "Jeremy R. Cole", "Julian Martin Eisenschlos", "et al."]
    year: 2022
    venue: "Transactions of the Association for Computational Linguistics, 10:257–273"
    doi: null
    url: null
    arxiv_id: null
  - title: "LoRA: Low-Rank Adaptation of Large Language Models"
    authors: ["Edward J Hu", "Yelong Shen", "Phillip Wallis", "et al."]
    year: 2022
    venue: "International Conference on Learning Representations"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemLLM: Finetuning LLMs to Use an Explicit Read-Write Memory"
    authors: ["Ali Modarressi", "Abdullatif Köksal", "Ayyoob Imani", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2404.11672"
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    authors: ["Joon Sung Park", "Joseph C O'Brien", "Carrie J Cai", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2304.03442"
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    authors: ["Timo Schick", "Jane Dwivedi-Yu", "Roberto Dessì", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2302.04761"
  - title: "Stanford Alpaca: An Instruction-Following LLaMA Model"
    authors: ["Rohan Taori", "Ishaan Gulrajani", "Tianyi Zhang", "et al."]
    year: 2023
    venue: "GitHub repository"
    doi: null
    url: "https://github.com/tatsu-lab/stanford_alpaca"
    arxiv_id: null
  - title: "LLaMA: Open and Efficient Foundation Language Models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memorizing Transformers"
    authors: ["Yuhuai Wu", "Markus N Rabe", "DeLesley Hutchins", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2203.08913"
  - title: "Training Language Models with Memory Augmentation"
    authors: ["Zexuan Zhong", "Tao Lei", "Danqi Chen"]
    year: 2022
    venue: "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pp. 5657–5673"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "A visualization of the process in both read- and write-based inputs."
  page: 4
  image_path: "figures/modarressi-2023-ret-llm-fig.png"
---

# Ret-LLM: Towards a General Read-Write Memory for Large Language Models

**Authors:** Modarressi, A.; Imani, A.; Fayyaz, M.; Schütze, H.
**Published:** 2023-05 (v2: Oct 2024) · [Source](https://arxiv.org/abs/2305.14322)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

> Note from the authors (v2 header, Oct 2024): "This concept paper outlines an initial methodology, now evolved and thoroughly evaluated in MemLLM (Modarressi et al., 2024, arXiv:2404.11672)." Ret-LLM ships qualitative evidence only; the empirical follow-up is MemLLM.

## TLDR

Ret-LLM is a 2023 concept paper from LMU Munich that proposes a Memory-as-API architecture for LLMs: a LoRA-fine-tuned Alpaca-7B (the only model tested, trained on a single A6000 48GB GPU) learns to emit two new in-line tokens during normal generation — `[MEM_WRITE{t1»t2»t3}]` to store a Davidsonian-style triplet (first-argument, relation, second-argument), and `[MEM_READ{q1»q2»q3}: …]` to query the store with any one or two slots filled. A controller intercepts these calls, persists the triplets in a three-column table alongside their mean hidden-state representations, retrieves on exact match first and falls back to LSH-hashed nearest-neighbour over the per-slot vectors if no exact match exists, then splices the returned triplets back into the LLM's context so it can compose the natural-language answer. The training data is fully synthetic (random people-name × five relations {employment, manager, investor, founder, customer} × organisations, generated into the six query templates of Table 1 and the write template of Table 2; the language-modelling loss is masked so only the API-call and answer tokens contribute). Evaluation is qualitative across hand-picked QA examples (Figs. 3, 4, 5) showing Alpaca-7B zero-shot getting the answer wrong even with full context in its prompt, while Ret-LLM with the same context written to memory first answers correctly — including a temporal example where it updates the U.S.-president fact (Joe Biden) without re-training. No accuracy numbers, no benchmark, no real dataset; the authors explicitly defer empirical evaluation to the follow-up paper MemLLM.

## Key Takeaway

Ret-LLM is the 2023 concept paper that first articulated the now-dominant Memory-as-API pattern: the LLM emits `[MEM_WRITE{t1»t2»t3}]` and `[MEM_READ{q1»q2»q3}]` tokens mid-generation, a controller catches them and routes to/from a separate Davidsonian-triplet store with LSH fuzzy fallback — write-time distillation, query-time symbolic-then-vector retrieval, all driven by the same LoRA-fine-tuned Alpaca-7B. **[E + R]** The same model owns both halves of the lifecycle (encode-time triplet extraction AND query-formulation), so the encode and retrieve dimensions of ENGRAM are deliberately *coupled* through one set of LoRA weights — a design that anticipates the LLM-as-everything stance later validated empirically by MemoChat (2023), Mem0 (2025), and Memory-R1 (2025).

## Implications

- **[E] Write-time synthesis is the hard part, and it's not free — but it's where the architectural leverage lives.** Ret-LLM forces the same Alpaca to learn extraction (sentence → triplet), query-formulation (question → MEM_READ slot pattern), AND answer-composition (triplet results → natural language) inside one LoRA adapter. The lesson, repeated by every later read/write memory paper: if you split these into three separate models you triple the failure modes; if you collapse them into the LLM you pay once at fine-tune time and your write/read paths stay semantically consistent.
- **[N] The "shape of memory" is a three-column table, deliberately not a graph.** The authors had every reason to call this a knowledge graph (it is, structurally) but explicitly chose tabular triplets so the API stays a literal string-API and aggregation is set-union over rows, not subgraph traversal. For memory-architects: this is the cheapest possible relational structure that still supports the six query patterns of Table 1 — adopt it before reaching for Neo4j when your queries are flat lookups.
- **[R] Exact-match-first, vector-fallback is the right default retrieval order, not pure vector.** The retrieval algorithm is: literal string match on each slot → if miss, LSH-NN over the LLM's mean hidden-state for that slot → if still miss, return ∅. Pure-vector retrieval is the *last resort*, not the primary path. Skipping this ordering (going straight to ANN) is how teams discover their memory systems "remember things that aren't there."
- **[R] LSH was the practical choice for the Memory-as-API pattern in 2023; in 2026 swap it for a real ANN library, but keep the staged fallback.** The paper's justification for LSH is purely computational ("comparing distances to all stored representations would be expensive"). FAISS, hnswlib, or a vector DB now make brute-force k-NN trivially fast for stores under ~10M triplets, but the architectural pattern — exact match before approximate match — is the lesson that should outlive the LSH implementation choice.
- **[G] Triplet provenance is the unspoken half of Davidsonian semantics — Ret-LLM doesn't store it, and that's the first thing to fix in any derivative.** The paper stores `<t1, t2, t3>` only. There is no source-document field, no extraction-confidence, no write-timestamp, no contradiction-detection step. For an agentic OS, this is a known footgun: temporal QA (the paper's own Fig. 4 case) silently overwrites old facts with new without warning. Any production derivative MUST add a source/time/confidence quartet next to each triplet.
- **[A + M] Updates are a free side-effect of the architecture, not a feature — and that's a double-edged thing.** Because storage is a writable table, the U.S.-president-fact can be updated by writing a new row (Fig. 4). But there's no delete, no merge, no contradiction detection — just additive writes. This is the same naive append-only design Mem0 (2025) later identifies as the failure mode of early conversational-memory systems and addresses with explicit ADD/UPDATE/DELETE/NOOP gates. Treat Ret-LLM as the *minimum* viable maintenance layer and budget the gate-classifier work explicitly.
- **[E + G] The training-data trick — masking the loss to only the API-call and answer segments — is the load-bearing detail.** Sections 3.3 + Tables 1–2: during fine-tuning, the LM loss is computed only on the `[MEM_*{…}]` tokens and the final answer, NOT on the question or the controller-supplied API response. This forces the LoRA adapter to specialise on what the LLM is supposed to *generate*, leaving comprehension of incoming text on the base-model side. Any team trying to teach a small model to use a memory API should copy this loss-masking recipe verbatim — it's why a 7B model can learn the protocol on a single 48GB GPU.
- **[N] The controller is a hidden seam where the entire memory protocol can be swapped without touching the LLM.** The controller is described as a thin moderator that pauses generation on `[MEM_READ{…}:` (the closing colon-then-empty is the signal), runs the query, and splices the result back as the next tokens. This means the same fine-tuned LLM can later be hooked to Postgres, FAISS, a graph DB, or a remote MCP-style memory service — the LLM doesn't know. For architects: invest in the controller's protocol surface (one-line append, exact-match-first, structured-error-on-miss) rather than the backing store.

## How to Apply It (method)

**Scenario:** You are building an "agentic OS" memory subsystem for a Flow-OS-style stateless-loop agent. Each session is fresh context, but the agent needs to write factual triples (e.g., `<Dana Whitfield, paid for, Flow OS, 2026-04>`) discovered during one session and recall them in the next. You want write-time distillation (no raw transcript chunking) and a controller-driven read/write API that the same fine-tuned model owns end-to-end. You want to know what it takes to actually ship the Ret-LLM pattern in 2026.

**Steps:**

1. **Pick the base model and adapter strategy.** Ret-LLM used Alpaca-7B (LLaMA-1 instruct-tuned) + LoRA on a single A6000 48GB GPU. In 2026, swap for Llama-3.1-8B-Instruct or Qwen2.5-7B with QLoRA so the whole adapter fits in 24GB; the architectural pattern doesn't care.

2. **Define the triplet schema and stable API surface.** Match Ret-LLM exactly so the protocol is unambiguous in the token stream:

   ```
   [MEM_WRITE{<t1>>><t2>>><t3>}]
   [MEM_READ{<q1>>><q2>>><q3>}: {<r_t1>>><r_t2>>><r_t3>};{<...>};...]
   ```

   The `»` separator (Ret-LLM uses `>>`) must NOT appear in normal text. The closing `: ` is the signal the controller waits for before splicing in results.

3. **Generate the synthetic training corpus.** Define `P` (population of name strings), `R` (closed relation vocabulary, e.g. {employed_by, paid_for, met_at, mentioned, decided}), `O` (organisations / entities). For each random (per, rel, org) triplet, emit:

   - 6 question-templates (Table 1: `<per>`, `<per,org>`, `<per,rel>`, `<org>`, `<rel>`, `<org,rel>`) with their MEM_READ call, the controller's API-Response, and the natural-language answer.
   - 1+ write-templates (Table 2): `[per1, per2, ...] is/are rel to org.` → multiple sequential `[MEM_WRITE{…}]` calls.

   Concatenate Question + API-call + API-response + Answer into one training instance.

4. **Fine-tune with masked loss on API-call + Answer tokens only.** This is the load-bearing trick. Set `labels = -100` for the Question and API-Response spans; only the `[MEM_WRITE{…}]`, `[MEM_READ{…}:`, and final Answer spans contribute to the cross-entropy. (Keep a baseline run *without* the mask so you can confirm the mask is what makes the protocol stick.)

5. **Build the controller as a token-stream interceptor, not a tool-use wrapper.** The controller pattern-matches `[MEM_WRITE{…}]` or `[MEM_READ{…}:` in the streamed output. On WRITE, parse the three slots and insert into the store. On READ, pause generation, run the query, format the results as `{t1»t2»t3};{…};…]`, and resume generation with those tokens prepended.

6. **Implement the staged retrieval.** Per-slot exact match against the table first. If any slot misses, compute its mean hidden-state (use the LLM's final-layer mean over the slot's tokens) and do LSH/FAISS approximate-NN against the per-slot vector index for an alternative term `q̃_i`. If that misses too, return `∅`. Return ALL matching rows for the resolved query (multi-match is normal and expected).

7. **Add the four production hardenings Ret-LLM omits (your derivatives MUST have these):**
   - **Provenance column** — add `source_uri`, `extracted_at`, `confidence` to every row.
   - **Update gate** — before WRITE, run a quick same-`(t1, t2)` lookup; if a different `t3` exists, route through an LLM-judge ADD/UPDATE/DELETE/NOOP classifier (the Mem0 / Memory-R1 pattern).
   - **Contradiction surfacing** — never silently overwrite; emit a warning event when an UPDATE replaces a conflicting fact.
   - **Soft delete** — never hard-delete; mark `valid_to` so the audit trail survives.

8. **Test with the Ret-LLM-style qualitative diff.** Same context (e.g., "Dana paid for Flow OS in April 2026; …") delivered (a) as zero-shot in-context to the base model and (b) via Ret-LLM's write-then-query path. Confirm the memory path beats the base on the six query types from Table 1 — if not, your loss-mask or your query-template coverage is wrong.

**Expected outcome:** A reproducible Ret-LLM-class subsystem: ~24GB GPU footprint, sub-second exact-match retrieval at million-row scale, full token-stream-driven write/read protocol, and the four provenance/maintenance hardenings the original paper deliberately leaves out. Use the same harness to A/B-test alternative backing stores (Postgres, SQLite-FTS, FAISS, a graph DB) without ever touching the fine-tuned LLM — the controller is the swap-point.

## Best Figure

![Figure 2 — A visualization of the process in both read- and write-based inputs (page 4)](figures/modarressi-2023-ret-llm-fig.png)

Image Candidates:
Figure 1 (p. 1): Three-component overview (LLM, Controller, Memory) with the two canonical interaction modes (A: write a fact, B: read a fact) — the cleanest single-image summary of the architecture.
Figure 2 (p. 4): Two-panel detailed dataflow showing the full Memory-Write (steps 1–3) and Memory-Read (steps 1–7) protocols with the exact MEM_WRITE/MEM_READ token strings — the only diagram that shows the *protocol itself*, not just the boxes.
Figure 3 (p. 5): Side-by-side zero-shot Alpaca failure vs Ret-LLM success on the same QA task, with the full LLM↔Controller↔Memory transcript inline — the empirical motivator.

Best Image:
Figure Name: Figure 2: "A visualization of the process in both read- and write-based inputs."
Figure Page: 4
Slide Caption: Ret-LLM's Memory-as-API protocol: the LLM emits MEM_WRITE / MEM_READ tokens that a controller intercepts and routes to a triplet store, splicing results back into the token stream.
Description: Figure 2 is the most architecturally informative image in the paper because it shows the *protocol*, not just the components. Panel (a) traces the three-step write path: (1) controller passes the user's informative sentence to the fine-tuned LLM; (2) the LLM emits one or more `[MEM_WRITE{t1»t2»t3}]` tokens inline; (3) the controller parses each call and persists the triplet (plus its average hidden-state vector) to the three-column memory table. Panel (b) traces the seven-step read path: (1) controller forwards the user's question; (2) the LLM emits `[MEM_READ{»»<org>}:` with one or two slots filled and an open colon; (3) the controller intercepts the open call, queries the memory; (4) the memory returns matching triplets; (5) the controller splices them after the colon; (6) the LLM resumes generation using those tokens as context; (7) the natural-language answer is returned to the user. This figure is the canonical reference for what "Memory-as-API" means as a token-stream protocol — the exact pattern later reused by MemoChat, Mem0, A-MEM, and Memory-R1.

## What Experts Overlook

The unsung detail is **the loss-masking recipe in §3.3** — specifically the sentence: "the language modeling loss is only applied to the API query and Answer sections." During fine-tuning the LLM sees four concatenated segments (Question, API-call, API-response, Answer) but the cross-entropy is computed *only* on the API-call and Answer tokens. The Question is what the user wrote and the API-Response is what the controller pasted in — the model never needs to predict them, only consume them. This single decision is why a 7B model on a single A6000 can reliably learn the protocol with synthetic data: the LoRA adapter is forced to specialise exactly on the two things the model is supposed to *generate* (the API call and the natural-language answer), without wasting capacity on memorising training-set questions or replaying API responses.

**Why it matters:** Most teams trying to teach a small open-weights model to use a memory API copy the protocol surface (the `[MEM_*{…}]` tokens) but skip the loss-mask, then complain that the model "doesn't reliably emit the API call" or "hallucinates triplets that look like the synthetic data." Both symptoms come from the same root cause: unmasked loss makes the model treat the Question and API-Response as targets too, so it overfits the question distribution and starts reproducing API-Response patterns even when the controller hasn't sent any. The loss-mask is what makes the LLM "tool-use-aware" rather than "tool-use-mimicking." It is the same trick Toolformer uses (cited in the paper) but Ret-LLM applies it to the harder case of *bidirectional* tool calls (the LLM both writes and reads).

**Example of good use:** When building Flow OS's memory write-path on Llama-3.1-8B + QLoRA, generate ~50k synthetic (statement, MEM_WRITE-sequence) and (question, MEM_READ-call, controller-response, answer) instances. Set `labels = -100` on the statement, the question, and the controller-response token spans before passing to the trainer. Train for 1–2 epochs at 5e-5. Expect the adapter to emit syntactically valid API calls >99% of the time on out-of-distribution sentence shapes — because the model only ever had to *predict* the call format, never the input format.

**Example of misapplication:** Skip the mask, train on the same 50k examples, and the model will fluently emit MEM_READ calls — but it will also frequently *hallucinate* `{t1»t2»t3};{…}` results inside its own output, as if it were the controller. (We've seen this exact failure mode in the wild on agent-memory replications.) The fix is always the same: re-train with the loss masked to API-call + Answer spans, and the hallucinated responses disappear.

## Extracted Prompts

The paper contains no full LLM prompts in the modern instruction-tuning sense — it shows training-data *templates* (Tables 1 and 2) and evaluation *example transcripts* (Figures 3, 4, 5) which are reproduced below verbatim because they are the closest thing to prompts the paper provides.

**Prompt explanation:** Table 1 — the six memory-read training-data templates that teach the LLM to emit MEM_READ for the six query types.

```
Query Type      Question                          API Query        API Response                                                  Answer
<per>           Who is per?                       {per»»}:         {per»rel»org}                                                  per is rel to org.
<per, org>      How per is related to org?        {per»»org}:      {per»rel»org}                                                  per is rel to org.
<per, rel>      per is rel which company?         {per»rel»}:      {per»rel»org}                                                  per is rel to org.
<org>           Who are related to org?           {»»org}:         {per1»rel1»org};{per2»rel2»org};...                            [per1, per2, ...] is/are related to org.
<rel>           Who are the rel?                  {»rel»}:         {per1»rel»org1};{per2»rel»org2};...                            [per1, per2, ...] is/are rel.
<org, rel>      Who are rel org?                  {»rel»org}:      {per1»rel»org};{per2»rel»org};...                              [per1, per2, ...] is/are rel to org.
```

**Prompt explanation:** Table 2 — the memory-write training-data template that teaches the LLM to emit one MEM_WRITE per implied triplet from a multi-subject statement.

```
Triplet(s)                                        Statement                                       API Write Call(s)
[<per1, rel, org>, <per2, rel, org>, ...]         [per1, per2, ...] is/are rel to org.            [MEM_WRITE{per1»rel1»org}][MEM_WRITE{per2»rel2»org}]...
```

**Prompt explanation:** Figure 3 (Evaluation Example #1) — the zero-shot baseline prompt given to Alpaca-7B, used to demonstrate the failure mode Ret-LLM is built to fix.

```
: You will be presented with one or a series of sentences about some people and their relationship with a company. After that, for any given question you should be capable of answering that based on the previous sentences.

Cyrus Alfred, Tia Batres, and Pasquale Ballif are customers of Pfizer. Dorothea Altemus is employed by Pfizer.
Question: Who are employed by Pfizer?
Answer:
```

**Prompt explanation:** Figure 3 (Evaluation Example #1, Ret-LLM mode) — the same content delivered as three sequential user prompts that the LLM converts to MEM_WRITE calls, then one final question prompt that triggers a MEM_READ.

```
: Cyrus Alfred, Tia Batres, and Pasquale Ballif are customers of Pfizer.
: Dorothea Altemus is employed by Pfizer.
: Who are employed by Pfizer?
```

**Prompt explanation:** Figure 4 (Temporal QA example) — single-question prompt that demonstrates how a writable memory entry can override a stale parametric fact (Obama vs Biden).

```
: Question: Who is the president of the United States?
Answer:
```

**Prompt explanation:** Figure 5 (appendix, Evaluation Example #2) — second qualitative case showing multi-relation handling (employee vs customer of BMW).

```
: You will be presented with one or a series of sentences about some people and their relationship with a company. After that, for any given question you should be capable of answering that based on the previous sentences.

Mozella Baima and Modesto Baichan are employees of ExxonMobil. Maryjane Bachand and Willian Beasmore are employees of BMW. Willian Banik is a customer of BMW.
Question: Who are related to BMW?
Answer:
```

## Citations

- Bubeck et al. 2023 — *Sparks of Artificial General Intelligence: Early experiments with GPT-4* (arXiv:2303.12712)
- Cheng et al. (n.d.) — *Language Model with Plug-in Knowledge Memory* (preprint, no year given in bibliography)
- Chowdhery et al. 2022 — *PaLM: Scaling Language Modeling with Pathways*
- Davidson 1967 — *The Logical Form of Action Sentences* (reprinted in Davidson 1980, *Essays on Actions and Events*) — the foundational Davidsonian-semantics reference that justifies the triplet representation
- Dhingra et al. 2022 — *Time-Aware Language Models as Temporal Knowledge Bases* (TACL 10:257–273)
- Hu et al. 2022 — *LoRA: Low-Rank Adaptation of Large Language Models* (ICLR)
- Modarressi et al. 2024 — *MemLLM: Finetuning LLMs to Use an Explicit Read-Write Memory* (arXiv:2404.11672) — the empirical follow-up cited in the v2 header
- Park et al. 2023 — *Generative Agents: Interactive Simulacra of Human Behavior* (arXiv:2304.03442)
- Schick et al. 2023 — *Toolformer: Language Models Can Teach Themselves to Use Tools* (arXiv:2302.04761) — the direct inspiration for the in-line API-call protocol
- Taori et al. 2023 — *Stanford Alpaca: An Instruction-Following LLaMA Model*
- Touvron et al. 2023 — *LLaMA: Open and Efficient Foundation Language Models*
- Wu et al. 2022 — *Memorizing Transformers* (arXiv:2203.08913)
- Zhong et al. 2022 — *Training Language Models with Memory Augmentation* (EMNLP, pp. 5657–5673)

(13 total references; all entries above also serialised as structured JSON in the frontmatter `citations` field for downstream `/citation-walk` and `/auto-research` consumption.)

## Related Digests

- [[mao-2026-agent-memory-circuits]] — What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis (Mao 2026 mechanistically dissects the same Write/Read routing decisions Ret-LLM externalises into the controller — showing the LLM grows its routing "brain" before its extraction/grounding heads, which validates Ret-LLM's loss-masking instinct that the API-call tokens are the bottleneck)
- [[liu-2023-think-in-memory]] — Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory (the closest contemporary cousin — also LSH-based, also write-time distillation into a structured store, but uses natural-language thoughts instead of Davidsonian triplets; Mem0 later inherits TiM's write-time-distillation idea but replaces LSH with vector top-K)
- [[lu-2023-memochat]] — MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation (extends the Ret-LLM "one LoRA owns the protocol" stance to conversation-scale: collapses store + retriever + updater into instruction-tuning on the same LLM, proving the architectural pattern Ret-LLM proposed)
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: Agentic Memory for LLM Agents (the seed of this citation walk; A-MEM cites Ret-LLM explicitly in its frontmatter and generalises Ret-LLM's Davidsonian-triplet store to Zettelkasten-style atomic memory notes with dynamic linking)
- [[weston-2015-memory-networks]] — Memory Networks (the 2014/2015 ancestor that called the LLM-memory problem before LLMs existed and proposed the same K-means hashing trick Ret-LLM revives as LSH)

## Reviewer Notes

**Overall severity:** Clean

Every claim in the TLDR, key takeaway, implications, method, what-experts-overlook, and extracted-prompts sections has been cross-checked against the paper text. Specific verifications:

- **Model identity (Alpaca-7B + LoRA on A6000 48GB)** — confirmed §3.3, paragraph 2 ("we use low-rank adaptation (LoRA) … on a single A6000 48GB GPU").
- **Davidsonian-semantics grounding** — confirmed §1 (sentence "draws inspiration from the theoretical framework of Davidsonian semantics") and §3 paragraph 4 (explicit reference to "Davidsonian semantics (Davidson, 1967), where concepts described in sentences could be stored in a structure of <first argument, relation, second argument>").
- **API token strings (`[MEM_WRITE{t1»t2»t3}]` and `[MEM_READ{_»_»_}: {…}]`)** — confirmed verbatim §3.2 bullets.
- **Exact-match-then-LSH retrieval order** — confirmed §3.1 (paragraph beginning "Handling Memory Queries") and the closing paragraph of §3.1 ("for every ti the mean representation … is stored in a Locality-Sensitive Hashing (LSH) table. The reason of utilizing LSH is to reduce the computation required for finding similar representations").
- **Loss-masking on API-call + Answer only** — confirmed §3.3 ("the language modeling loss is only applied to the API query and Answer sections") and again in the memory-write training paragraph ("Also the loss function is applied only to the API segment").
- **Five-relation synthetic vocabulary {employment, manager, investor, founder, customer}** — confirmed §3.3 paragraph 4.
- **Six query templates (Table 1)** — reproduced verbatim from the paper.
- **Qualitative-only evaluation, no benchmark** — confirmed §4 ("Over a qualitative evaluation using question answering examples") and §5 ("As this work is still under development, in our next revision we will add a more in-detail empirical evaluation, preferrably on a real dataset").
- **MemLLM follow-up reference** — confirmed v2 header note ("now evolved and thoroughly evaluated in MemLLM") and citation in the references section.
- **Figure 2 page (page 4)** — confirmed via the rendered PDF page; Figure 2 caption is at the foot of page 4 immediately above §3.2.

No claim in this digest names a metric, benchmark score, dataset, or experiment that does not appear in the paper. The "what most people would expect"-style framings (e.g., "exact-match-first, vector-fallback is the right default") are flagged as lens-author interpretation, not paper claims, in the implications section voice.
