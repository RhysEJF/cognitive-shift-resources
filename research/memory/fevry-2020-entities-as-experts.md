---
corpus: agentic-memory
kind: paper-digest
slug: fevry-2020-entities-as-experts
title: "Entities as Experts: Sparse Memory Access with Entity Supervision"
authors:
  - "Thibault Févry"
  - "Livio Baldini Soares"
  - "Nicholas FitzGerald"
  - "Eunsol Choi"
  - "Tom Kwiatkowski"
year: 2020
publication_date: "2020-10"
venue: "EMNLP 2020"
source_url: "https://arxiv.org/abs/2004.07202"
doi: null
arxiv_id: "2004.07202"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Carving out a separate, supervised memory slot per entity and forcing the model to retrieve it before composing meaning beats both bigger Transformers and bolted-on knowledge graphs — the smarter you make the write path, the less you need at inference."
topics:
  - entity-memory
  - sparse-memory-access
  - knowledge-augmented-lm
  - entity-linking
  - memory-architecture
  - conditional-computation
  - open-domain-qa
  - mixture-of-experts
  - declarative-knowledge
tags:
  - paper
  - memory-architecture
  - entity-supervision
  - sparse-activation
  - triviaqa
  - lama
  - wikipedia-pretraining
  - encoding-gate
  - shape-of-memory
entities:
  - fevry-thibault
  - soares-livio-baldini
  - fitzgerald-nicholas
  - choi-eunsol
  - kwiatkowski-tom
related_digests: []
citations:
  - title: "A neural knowledge language model"
    authors: ["Sungjin Ahn", "Heeyoul Choi", "Tanel Pärnamaa", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1608.00318"
  - title: "TACRED revisited: A thorough evaluation of the TACRED relation extraction task"
    authors: ["Christoph Alt", "Aleksandra Gabryszak", "Leonhard Hennig"]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Matching the blanks: Distributional similarity for relation learning"
    authors: ["Livio Baldini Soares", "Nicholas FitzGerald", "Jeffrey Ling", "et al."]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Semantic parsing on freebase from question-answer pairs"
    authors: ["Jonathan Berant", "Andrew Chou", "Roy Frostig", "et al."]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Translating embeddings for modeling multi-relational data"
    authors: ["Antoine Bordes", "Nicolas Usunier", "Alberto Garcia-Duran", "et al."]
    year: 2013
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exponentially increasing the capacity-to-computation ratio for conditional computation in deep learning"
    authors: ["Kyunghyun Cho", "Yoshua Bengio"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1406.7362"
  - title: "Ultra-fine entity typing"
    authors: ["Eunsol Choi", "Omer Levy", "Yejin Choi", "et al."]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Semi-supervised sequence learning"
    authors: ["Andrew M Dai", "Quoc V Le"]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "Learning factored representations in a deep mixture of experts"
    authors: ["David Eigen", "Marc'Aurelio Ranzato", "Ilya Sutskever"]
    year: 2013
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1312.4314"
  - title: "Deep joint entity disambiguation with local neural attention"
    authors: ["Octavian-Eugen Ganea", "Thomas Hofmann"]
    year: 2017
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "REALM: Retrieval-augmented language model pre-training"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2002.08909"
  - title: "Universal language model fine-tuning for text classification"
    authors: ["Jeremy Howard", "Sebastian Ruder"]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Billion-scale similarity search with GPUs"
    authors: ["Jeff Johnson", "Matthijs Douze", "Hervé Jégou"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1702.08734"
  - title: "TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension"
    authors: ["Mandar Joshi", "Eunsol Choi", "Daniel S Weld", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1705.03551"
  - title: "Adam: A method for stochastic optimization"
    authors: ["Diederik P Kingma", "Jimmy Ba"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1412.6980"
  - title: "Large memory layers with product keys"
    authors: ["Guillaume Lample", "Alexandre Sablayrolles", "Marc'Aurelio Ranzato", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Informing unsupervised pretraining with external linguistic knowledge"
    authors: ["Anne Lauscher", "Ivan Vulić", "Edoardo Maria Ponti", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.02339"
  - title: "Latent retrieval for weakly supervised open domain question answering"
    authors: ["Kenton Lee", "Ming-Wei Chang", "Kristina Toutanova"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1906.00300"
  - title: "SenseBERT: Driving some sense into BERT"
    authors: ["Yoav Levine", "Barak Lenz", "Or Dagan", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1908.05646"
  - title: "Question and answer test-train overlap in open-domain question answering datasets"
    authors: ["Patrick Lewis", "Pontus Stenetorp", "Sebastian Riedel"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning cross-context entity representations from text"
    authors: ["Jeffrey Ling", "Nicholas FitzGerald", "Zifei Shan", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.03765"
  - title: "Barack's wife Hillary: Using knowledge graphs for fact-aware language modeling"
    authors: ["Robert Logan", "Nelson F Liu", "Matthew E Peters", "et al."]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "A discrete hard EM approach for weakly supervised question answering"
    authors: ["Sewon Min", "Danqi Chen", "Hannaneh Hajishirzi", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.04849"
  - title: "Knowledge guided text retrieval and reading for open domain question answering"
    authors: ["Sewon Min", "Danqi Chen", "Luke Zettlemoyer", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.03868"
  - title: "Deep contextualized word representations"
    authors: ["Matthew E Peters", "Mark Neumann", "Mohit Iyyer", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1802.05365"
  - title: "Knowledge enhanced contextual word representations"
    authors: ["Matthew E Peters", "Mark Neumann", "Robert L Logan IV", "et al."]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models as knowledge bases?"
    authors: ["Fabio Petroni", "Tim Rocktäschel", "Patrick Lewis", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.01066"
  - title: "BERT is not a knowledge base (yet): Factual knowledge vs. name-based reasoning in unsupervised QA"
    authors: ["Nina Poerner", "Ulli Waltinger", "Hinrich Schütze"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.03681"
  - title: "Exploring the limits of transfer learning with a unified text-to-text transformer"
    authors: ["Colin Raffel", "Noam Shazeer", "Adam Roberts", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1910.10683"
  - title: "Maximum inner-product search using cone trees"
    authors: ["Parikshit Ram", "Alexander G Gray"]
    year: 2012
    venue: "KDD"
    doi: null
    url: null
    arxiv_id: null
  - title: "SLING: A framework for frame semantic parsing"
    authors: ["Michael Ringgaard", "Rahul Gupta", "Fernando CN Pereira"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1710.07032"
  - title: "How much knowledge can you pack into the parameters of a language model?"
    authors: ["Adam Roberts", "Colin Raffel", "Noam Shazeer"]
    year: 2020
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2002.08910"
  - title: "Outrageously large neural networks: The sparsely-gated mixture-of-experts layer"
    authors: ["Noam Shazeer", "Azalia Mirhoseini", "Krzysztof Maziarz", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1701.06538"
  - title: "Learning binary codes for maximum inner product search"
    authors: ["Fumin Shen", "Wei Liu", "Shaoting Zhang", "et al."]
    year: 2015
    venue: "ICCV"
    doi: null
    url: null
    arxiv_id: null
  - title: "Asymmetric LSH (ALSH) for sublinear time maximum inner product search (MIPS)"
    authors: ["Anshumali Shrivastava", "Ping Li"]
    year: 2014
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "End-to-end memory networks"
    authors: ["Sainbayar Sukhbaatar", "Arthur Szlam", "Jason Weston", "et al."]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "K-Adapter: Infusing knowledge into pre-trained models with adapters"
    authors: ["Ruize Wang", "Duyu Tang", "Nan Duan", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2002.01808"
  - title: "Memory networks"
    authors: ["Jason Weston", "Sumit Chopra", "Antoine Bordes"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1410.3916"
  - title: "Pretrained encyclopedia: Weakly supervised knowledge-pretrained language model"
    authors: ["Wenhan Xiong", "Jingfei Du", "William Yang Wang", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1912.09637"
  - title: "Reference-aware language models"
    authors: ["Zichao Yang", "Phil Blunsom", "Chris Dyer", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1611.01628"
  - title: "Position-aware attention and supervised data improve slot filling"
    authors: ["Yuhao Zhang", "Victor Zhong", "Danqi Chen", "et al."]
    year: 2017
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "ERNIE: Enhanced language representation with informative entities"
    authors: ["Zhengyan Zhang", "Xu Han", "Zhiyuan Liu", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.07129"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "The Entities as Experts model: the initial transformer layer output is used (i) to predict mention boundaries, (ii) to retrieve entity embeddings from entity memory, and (iii) to construct input to the next transformer layer"
  page: 3
  image_path: "figures/fevry-2020-entities-as-experts-fig.png"
---

# Entities as Experts: Sparse Memory Access with Entity Supervision

**Authors:** Thibault Févry, Livio Baldini Soares, Nicholas FitzGerald, Eunsol Choi, Tom Kwiatkowski
**Published:** 2020-10 · [Source](https://arxiv.org/abs/2004.07202)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Févry et al. introduce **Entities as Experts (EaE)** — a 367M-parameter Transformer where a learned, addressable slot is reserved for each of 1M Wikipedia entities, and the network is supervised to *retrieve the right slot* before composing meaning around it. The entity memory layer is inserted between transformer block 4 and block 5 (out of 12), so token states flow through it once per forward pass; mentions are detected with a BIO classifier, then their span representation is used as a query to find the top-k closest entity embeddings (k=100 at inference, falling back gracefully to k=10 with no measurable loss). Pre-training on 32M 128-byte Wikipedia contexts with 17M hyperlink-supervised entity links yields three concrete wins: (1) on TriviaQA closed-book, EaE scores 43.2 EM, beating T5-11B (42.3) with **30× fewer parameters**; (2) on LAMA knowledge probes EaE matches BERT-large while being ~half the size; (3) on TACRED relation extraction it beats KnowBERT on the cleaned/weighted splits despite having no explicit entity-entity attention. Two ablations carry the architectural lesson: removing the entity-linking supervision (EaE-unsup) collapses entity accuracy and worsens perplexity (16.9 vs 11.0), and replacing the entity memory layer with just more transformer layers (No-EaE) loses ~6 EM on TriviaQA — proving the **shape** of the memory and its **supervision** matter more than raw parameter count.

## Key Takeaway

The "scale up the dense Transformer" reflex is the expensive way to remember facts. EaE shows you can beat an 11B-parameter generation model on TriviaQA with 367M parameters *only if* you carve memory into one slot per entity, supervise the model to retrieve the correct slot before reading the rest of the sentence, and treat that retrieval as a first-class architectural step — not a fine-tuning afterthought. The counter-intuitive part: knowledge-graph initialisations (TransE, Deep-Ed) help *less* than random embeddings that the model learns end-to-end, because the model is better at organising its own memory around its own reading objective than at inheriting someone else's schema.

## Implications

- **Carve memory by referent, not by chunk** (ENGRAM: N — Network): The biggest architectural lever is the *unit* of memory. Storing one slot per entity, rather than one vector per text chunk, lets retrieval be sparse and supervisable. For Flow OS this maps directly to a per-contact / per-venture / per-project memory keyed by canonical entity ID rather than by source document — and aligns with the existing v2 schema's `entities:` field.

- **Supervise the write path, or memory collapses** (ENGRAM: E — Encode + A — Aggregate): The EaE-unsup ablation is the load-bearing finding. Without entity-linking supervision the slots stop being meaningfully distinct: entity accuracy drops to ~zero, perplexity worsens by ~5 points (16.9 vs 11.0), and TriviaQA performance falls in step. **Translation:** an unsupervised "just embed everything" memory layer drifts into noise. If you want compounding recall, you need a write-time signal that says "this experience belongs to slot X."

- **Sparse retrieval has a near-zero quality cost** (ENGRAM: R — Retrieve): Table 5 shows k=10 retrieved entities scores within 0.1 of k=1,000,000 on both entity and TriviaQA accuracy. The model only needs to look at ~3% of its parameters at inference. For an agentic OS, this validates aggressive top-k pruning in vector retrieval — sparseness is the feature, not a compromise.

- **Pre-fixed vocabulary is the hidden ceiling** (ENGRAM: M — Maintain): EaE's 1M-entity vocabulary is *closed* — it cannot represent entities it didn't see at pre-training time, and the authors flag this as the main limitation. Any production memory system inheriting this design needs an explicit "new-entity provisioning" pathway (write a new slot, lazily learn its embedding) — otherwise the system gets stale within months.

- **Closed memory and external corpus retrieval are complements, not substitutes** (ENGRAM: A — Aggregate): Appendix F's oracle-ensemble analysis shows closed-book (EaE) and open-book (ORQA/GraphRetriever) predictions overlap less than two open-book systems with each other (29.3% vs 39.6%). They make *different* mistakes. For a memory architect this is permission to run both layers — a learned-parametric memory for canonical entity facts AND a fresh retrieval pass against documents — and to fuse their outputs rather than choose one.

- **Mention detection is a load-bearing sub-component** (ENGRAM: E — Encode): EaE's manual-analysis section shows 87% of TriviaQA questions have no incorrect entity links — but when even one is wrong, accuracy "considerably reduced." The whole architecture is downstream of correctly identifying *which span is an entity*. The lesson for memory systems: the entity-extraction layer at write time is not a nice-to-have, it is the choke point that gates everything else.

- **Random init beats knowledge-graph init when training end-to-end** (ENGRAM: A): Table 6 shows that random 100d embeddings (entity acc. 63.0) outperform frozen TransE (49.7) and roughly match trained-from-Deep-Ed (65.1). Knowledge graphs encode a schema that doesn't match the LM's objective. **Translation:** don't bolt on an external ontology and freeze it; let the system learn its own organisation, even from a noisier start.

- **Date and concept reasoning fall outside the entity-slot abstraction** (ENGRAM: N): EaE fails systematically on questions whose answers are dates or generic concepts ("happy", "fly") — both Table 4 examples and the LAMA ConceptNet sub-task confirm it. The shape-of-memory choice (one slot per *entity*) bakes in a category limit. For a generalised memory architecture this is a warning: choose your memory unit explicitly with the failure modes you can live with.

## How to Apply It (method)

**Scenario:** You are building Flow OS's per-contact memory layer. Today, the system uses chunked vector retrieval over markdown notes — every contact mention is just text in a chunk. You want each contact to have a *first-class memory slot*: every interaction across emails, transcripts, and notes is supervised to write into that slot at ingestion time, and at query time the model retrieves the correct slot for any mention (including aliases and partial names like "Marcus" → Marcus Webb) before composing a response. The EaE method gives you a concrete recipe.

**Steps:**

1. **Build the canonical entity vocabulary first.** Inventory every contact, company, venture and project in `memory/contacts/`, `memory/relationships/`, `memory/ventures/`. Assign each a stable slug and a unique integer ID. This is your `E = {e1...eN}`. Start small (a few hundred) — EaE used 1M but the architecture works at any scale.

   ```
   entity_table = {
     "marcus-webb":     0,  // Flow customer
     "sam-ellery":      1,  // Flow customer
     "dana-whitfield":  2,  // Flow customer
     "nadia":           3,  // partner
     "askrally":        4,  // venture
     ...
   }
   ```

2. **Run mention detection on every incoming text.** Use a BIO classifier (or a simpler regex+NER stack — spaCy, Google NL API, or just first-pass alias matching against your entity table). Emit `(span_start, span_end, candidate_entity_id_or_null)` triples. EaE's section 2.2.1 used Google Cloud Natural Language API plus Wikipedia hyperlinks to bootstrap supervision; you can use hyperlinks-in-markdown plus alias tables as your free supervision signal.

3. **Encode each entity as a learned vector** (256d in EaE; 100-300d is enough for hundreds-of-entities scale). Initialise randomly. Store these in a flat in-memory matrix `E` of shape `(N, 256)` — this is your "entity memory layer."

4. **At write time, for each detected mention `m_i = (entity_id, span_start, span_end)`:** compute a span representation `h_m = W_f * concat(token_embed[span_start], token_embed[span_end])`, then update the entity embedding `E[entity_id]` via gradient descent so that `dot(E[entity_id], h_m)` is the largest among all entities. This is the entity-linking loss (Section 2.2.2). Crucially: **the write path is supervised** — without this step EaE-unsup collapses.

   ```
   loss_link = -log( exp(E[entity_id] · h_m) / Σ_e exp(E[e] · h_m) )
   ```

5. **At read time, for each detected mention:** compute the same span representation `h_m`, retrieve the top-k nearest entity embeddings via dot-product (k=10 is enough — Table 5 confirms diminishing returns above that), build a weighted-sum vector `E_m = Σ α_j · E[e_j]`, project it back into token space and *inject it into the model's hidden state at the mention's position*. The model now sees the retrieved memory while composing its answer.

6. **Layer the entity-memory call between two stacks of normal Transformer layers** — EaE uses 4 layers below + 8 layers above with the memory access between them. The "below" layers learn to *generate good queries*; the "above" layers learn to *integrate retrieved memories*. Don't put memory access at the very top (No-EaE ablation: ~6 EM lost) — it has to feed the composition, not just decorate it.

7. **Add a maintenance loop for new entities.** EaE's main limitation is the fixed vocabulary. When ingesting a new contact, allocate a new row in `E`, initialise it from the average embedding of the first few mention contexts, then resume normal supervised training. Without this step the system silently drops everything about people you met after pre-training.

**Expected outcome:** A memory system where every reference to a known contact, venture or project — including aliases, typos, and partial mentions — converges to the same persistent slot. Retrieval is sub-linear in the entity count (top-k MIPS). New facts about an entity update the slot; queries about that entity retrieve the cumulative representation rather than a single chunk. The system becomes measurably better at "what did we decide about X" over time — exactly the compound-learning property Flow OS is aiming at — *provided* the write-time supervision (entity linking) is maintained.

## Best Figure

![Figure 2 — The Entities as Experts model (page 3)](figures/fevry-2020-entities-as-experts-fig.png)

Image Candidates:
Figure 2 (p. 3): The architecture diagram — shows the entity memory layer interleaved between two transformer stacks, with mention boundaries detected at the bottom, entity slots retrieved on the right, and the retrieved memory routed back into the upper stack. This is the *shape-of-memory* image.
Figure 3 (p. 6): Three-panel TriviaQA performance breakdown by answer frequency, number of named entities in the question, and question length — shows precisely where EaE wins (frequent entities, multi-entity questions) and where it loses (rare entities, no-entity questions).
Table 3 (p. 6): The headline scoreboard — EaE 367M vs T5-11B (42.3 vs 43.2 EM on TriviaQA), the cleanest demonstration of "small + supervised memory beats big + dense."

Best Image:
Figure Name: Figure 2: "The Entities as Experts model: the initial transformer layer output is used (i) to predict mention boundaries, (ii) to retrieve entity embeddings from entity memory, and (iii) to construct input to the next transformer layer, augmented with the retrieved entity embeddings"
Figure Page: 3
Slide Caption: EaE's architecture — mentions are detected at the bottom, entity slots are retrieved from a separate memory matrix in the middle, and the retrieved vector is injected back into the upper transformer layers.
Description: Figure 2 is the single image that captures EaE's architectural claim. At the bottom, a BIO classifier on the first transformer's output marks the mention boundaries (`[MASK] [MASK] published the Origin of the Species in 1859.`). These boundaries become queries into the right-hand Entity Memory matrix — a separate parameter store with one row per Wikipedia entity (Q1035: Charles Darwin highlighted). The retrieved entity embeddings are aggregated and routed (red arrows) back into the hidden state at the mention positions, then flow up through additional transformer layers to produce the final token and entity predictions. The figure makes the central design choice legible: memory is a *first-class architectural module*, not a side-channel — it is queried mid-stack so downstream composition can use it, and it is supervised at training time via the entity-linking loss. This is the diagram every subsequent retrieval-augmented LM paper (REALM, RETRO, Atlas) is implicitly arguing with.

## What Experts Overlook

The overlooked detail is **where in the network the memory layer lives** — and the asymmetric depth on either side. EaE puts the memory access after 4 transformer layers and before 8 more (l0=4, l1=8, not l0=8 / l1=4 or l0=6 / l1=6). The "below" stack has to be *just deep enough* to produce a good span representation that can serve as a memory query — but shallow enough that most of the model's reasoning happens *after* the retrieval. The No-EaE ablation (Section 4.2) shows that putting the entity head only at the top loses ~6 EM on TriviaQA, and Section 5.1 explicitly notes that adding entity-linking signal at the top of the stack alone "does not benefit language modeling." Retrieval has to happen early enough that the upper layers can *use* what was retrieved.

**Why it matters:** Most experts implementing a memory layer treat the location as arbitrary — slap it on at the end, or have a separate retrieval module that runs before the main model. What EaE shows is that the memory layer must be **upstream of the reasoning layers, downstream of the encoding layers**. The model needs enough representational capacity before retrieval to form a good query, and enough capacity after retrieval to integrate the retrieved content into the final composition. This is the same lesson Recurrent Memory Transformer and MemGPT would later confirm: where you splice in memory matters as much as what's in it.

**Example of good use:** When building a Flow OS skill that incorporates retrieved contact context, structure the LLM call so the retrieval happens *between* an initial summarisation of the user's query (the "query-formulation" stage) and the final response generation (the "composition" stage). E.g.: pass 1 — "What is the user really asking?" (4 transformer-equivalent steps of reasoning); pass 2 — retrieve top-k memories keyed on the formulated query; pass 3 — "Here are your memories, now answer" (8 transformer-equivalent steps of composition). This mirrors EaE's 4-memory-8 architecture in a multi-call pipeline.

**Example of misapplication:** Bolt retrieval onto the final answer (e.g., "generate the response, then append related memories at the bottom as a citation list") and you reproduce No-EaE's failure mode — the retrieved content has no chance to inform the answer, only to decorate it. The user gets a generic answer followed by a list of references that the model didn't actually reason over. Worse, if you put retrieval *too early* (before the query-formulation), the retriever doesn't know what to look for and pulls in irrelevant content — which then derails the composition. The depth-asymmetry is the load-bearing design choice.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- Ahn et al. (2016) — A neural knowledge language model
- Alt et al. (2020) — TACRED revisited: A thorough evaluation of the TACRED relation extraction task
- Baldini Soares et al. (2019) — Matching the blanks: Distributional similarity for relation learning
- Berant et al. (2013) — Semantic parsing on Freebase from question-answer pairs
- Bordes et al. (2013) — Translating embeddings for modeling multi-relational data (TransE)
- Devlin et al. (2018) — BERT: Pre-training of deep bidirectional transformers
- Ganea & Hofmann (2017) — Deep joint entity disambiguation with local neural attention (Deep-Ed)
- Guu et al. (2020) — REALM: Retrieval-augmented language model pre-training
- Lample et al. (2019) — Large memory layers with product keys
- Lee et al. (2019) — Latent retrieval for weakly supervised open domain QA (ORQA)

*(Full 43-entry list serialized in frontmatter `citations:` block.)*

## Related Digests

*(To be populated by orchestrator cross-link step.)*

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim in this digest is verifiable against the paper:
- 367M parameters for EaE, 42.3 EM for T5-11B, 43.2 EM for EaE on TriviaQA (Table 3)
- 17M entity links from 32M Wikipedia contexts (Section 2.2.1)
- k=10 ≈ k=full performance (Table 5)
- EaE-unsup perplexity 16.9 vs EaE 11.0 (Table 1)
- 87% of TriviaQA questions correctly entity-linked (Section 6.2)
- 4-layer / 8-layer split with memory between (Section 2.1, l0=4, l1=8)
- Random 100d init: 63.0 entity acc; TransE frozen: 49.7; Deep-Ed trained: 65.1 (Table 6)
- ConceptNet sub-task failure on non-entity answers (Section 5.2)
- Date-answer failure modes (Table 4, Table 10)
- 1M entity vocabulary, 256d entity embeddings (Sections 2.2.1, 4.1)

All architectural claims (memory layer between blocks 4 and 5, BIO mention detection, dot-product retrieval, entity-linking loss formulation) are directly cited from Section 2.
