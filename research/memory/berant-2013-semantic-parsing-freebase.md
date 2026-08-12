---
corpus: agentic-memory
kind: paper-digest
slug: berant-2013-semantic-parsing-freebase
title: "Semantic Parsing on Freebase from Question-Answer Pairs"
authors:
  - "Jonathan Berant"
  - "Andrew Chou"
  - "Roy Frostig"
  - "Percy Liang"
year: 2013
publication_date: "2013-10"
venue: "EMNLP 2013"
source_url: "https://aclanthology.org/D13-1160.pdf"
doi: null
arxiv_id: null
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Train a semantic parser on question–answer pairs alone (no annotated logical forms) by combining a corpus-aligned phrase→predicate lexicon with a 'bridging' operator that conjures connecting predicates from type-constraints of neighbours — proves a write-time-light, retrieval-heavy, type-aware index can crack open-domain QA over a 41M-entity KB."
topics:
  - semantic-parsing
  - question-answering
  - freebase
  - knowledge-base
  - distant-supervision
  - logical-forms
  - lambda-dcs
  - lexicon-induction
  - schema-grounding
  - webquestions
tags:
  - paper
  - canonical
  - pre-llm-qa
  - kbqa
  - benchmark-dataset
  - sempre
entities:
  - berant-jonathan
  - liang-percy
  - chou-andrew
  - frostig-roy
related_digests:
  - chen-2017-drqa-machine-reading
  - lewis-2020-rag-knowledge-nlp
  - guu-2020-realm
  - roberts-2020-pack-knowledge
  - brown-2020-gpt3-few-shot
citations:
  - title: "Bootstrapping semantic parsers from conversations"
    authors: ["Yoav Artzi", "Luke Zettlemoyer"]
    year: 2011
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Weakly supervised learning of semantic parsers for mapping instructions to actions"
    authors: ["Yoav Artzi", "Luke Zettlemoyer"]
    year: 2013
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Open information extraction from the web"
    authors: ["Michele Banko", "Michael J. Cafarella", "Stephen Soderland", "et al."]
    year: 2007
    venue: "IJCAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reading between the lines: Learning to map high-level instructions to commands"
    authors: ["S.R.K. Branavan", "Luke Zettlemoyer", "Regina Barzilay"]
    year: 2010
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to win by reading manuals in a Monte-Carlo framework"
    authors: ["S.R.K. Branavan", "David Silver", "Regina Barzilay"]
    year: 2011
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning high-level planning from text"
    authors: ["S.R.K. Branavan", "Nate Kushman", "Tao Lei", "et al."]
    year: 2012
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Large-scale semantic parsing via schema matching and lexicon extension"
    authors: ["Qingqing Cai", "Alexander Yates"]
    year: 2013
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Toward an architecture for never-ending language learning"
    authors: ["Andrew Carlson", "Justin Betteridge", "Bryan Kisiel", "et al."]
    year: 2010
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "SUTime: A library for recognizing and normalizing time expressions"
    authors: ["Angel X. Chang", "Christopher Manning"]
    year: 2012
    venue: "LREC"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fast online lexicon learning for grounded language acquisition"
    authors: ["David Chen"]
    year: 2012
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Bridging"
    authors: ["Herbert H. Clark"]
    year: 1975
    venue: "Workshop on theoretical issues in natural language processing"
    doi: null
    url: null
    arxiv_id: null
  - title: "Driving semantic parsing from the world's response"
    authors: ["James Clarke", "Dan Goldwasser", "Ming-Wei Chang", "et al."]
    year: 2010
    venue: "CoNLL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adaptive subgradient methods for online learning and stochastic optimization"
    authors: ["John Duchi", "Elad Hazan", "Yoram Singer"]
    year: 2010
    venue: "COLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Identifying relations for open information extraction"
    authors: ["Anthony Fader", "Stephen Soderland", "Oren Etzioni"]
    year: 2011
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Paraphrase-driven learning for open question answering"
    authors: ["Anthony Fader", "Luke Zettlemoyer", "Oren Etzioni"]
    year: 2013
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Confidence driven unsupervised semantic parsing"
    authors: ["Dan Goldwasser", "Roi Reichart", "James Clarke", "et al."]
    year: 2011
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Freebase data dumps"
    authors: ["Google"]
    year: 2013
    venue: "Google Developers"
    doi: null
    url: "https://developers.google.com/freebase/data"
    arxiv_id: null
  - title: "Automatic acquisition of hyponyms from large text corpora"
    authors: ["Marti A. Hearst"]
    year: 1992
    venue: "COLING"
    doi: null
    url: null
    arxiv_id: null
  - title: "Knowledge-based weak supervision for information extraction of overlapping relations"
    authors: ["Raphael Hoffmann", "Congle Zhang", "Xiao Ling", "et al."]
    year: 2011
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Jointly learning to parse and perceive: Connecting natural language to the physical world"
    authors: ["Jayant Krishnamurthy", "Thomas Kollar"]
    year: 2013
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Weakly supervised training of semantic parsers"
    authors: ["Jayant Krishnamurthy", "Tom Mitchell"]
    year: 2012
    venue: "EMNLP/CoNLL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Using semantic unification to generate regular expressions from natural language"
    authors: ["Nate Kushman", "Regina Barzilay"]
    year: 2013
    venue: "HLT/NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Inducing probabilistic CCG grammars from logical form with higher-order unification"
    authors: ["Tom Kwiatkowski", "Luke Zettlemoyer", "Sharon Goldwater", "et al."]
    year: 2010
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Lexical generalization in CCG grammar induction for semantic parsing"
    authors: ["Tom Kwiatkowski", "Luke Zettlemoyer", "Sharon Goldwater", "et al."]
    year: 2011
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Random walk inference and learning in a large scale knowledge base"
    authors: ["Ni Lao", "Tom Mitchell", "William W. Cohen"]
    year: 2011
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "From natural language specifications to program input parsers"
    authors: ["Tao Lei", "Fan Long", "Regina Barzilay", "et al."]
    year: 2013
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning dependency-based compositional semantics"
    authors: ["Percy Liang", "Michael I. Jordan", "Dan Klein"]
    year: 2011
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Lambda dependency-based compositional semantics"
    authors: ["Percy Liang"]
    year: 2013
    venue: "ArXiv technical report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Entity linking at web scale"
    authors: ["Thomas Lin", "Mausam", "Oren Etzioni"]
    year: 2012
    venue: "AKBC-WEKEX"
    doi: null
    url: null
    arxiv_id: null
  - title: "Open language learning for information extraction"
    authors: ["Mausam", "Michael Schmitz", "Robert Bart", "et al."]
    year: 2012
    venue: "EMNLP/CoNLL"
    doi: null
    url: null
    arxiv_id: null
  - title: "A joint model of language and perception for grounded attribute learning"
    authors: ["Cynthia Matuszek", "Nicholas FitzGerald", "Luke Zettlemoyer", "et al."]
    year: 2012
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Online large-margin training of dependency parsers"
    authors: ["Ryan McDonald", "Koby Crammer", "Fernando Pereira"]
    year: 2005
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Grounded unsupervised semantic parsing"
    authors: ["Hoifung Poon"]
    year: 2013
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards a theory of natural language interfaces to databases"
    authors: ["Ana-Maria Popescu", "Oren Etzioni", "Henry Kautz"]
    year: 2003
    venue: "IUI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Modeling relations and their mentions without labeled text"
    authors: ["Sebastian Riedel", "Limin Yao", "Andrew McCallum"]
    year: 2010
    venue: "ECML PKDD"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multi-instance multi-label learning for relation extraction"
    authors: ["Mihai Surdeanu", "Julie Tibshirani", "Ramesh Nallapati", "et al."]
    year: 2012
    venue: "EMNLP/CoNLL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Understanding natural language commands for robotic navigation and mobile manipulation"
    authors: ["Stefanie Tellex", "Thomas Kollar", "Steven Dickerson", "et al."]
    year: 2011
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Template-based question answering over RDF data"
    authors: ["Christina Unger", "Lorenz Bühmann", "Jens Lehmann", "et al."]
    year: 2012
    venue: "WWW"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning synchronous grammars for semantic parsing with lambda calculus"
    authors: ["Yuk Wah Wong", "Raymond J. Mooney"]
    year: 2007
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Natural language questions for the web of data"
    authors: ["Mohamed Yahya", "Klaus Berberich", "Shady Elbassuoni", "et al."]
    year: 2012
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to parse database queries using inductive logic programming"
    authors: ["John M. Zelle", "Raymond J. Mooney"]
    year: 1996
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to map sentences to logical form: Structured classification with probabilistic categorial grammars"
    authors: ["Luke S. Zettlemoyer", "Michael Collins"]
    year: 2005
    venue: "UAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Ontological smoothing for relation extraction with minimal supervision"
    authors: ["Congle Zhang", "Raphael Hoffmann", "Daniel S. Weld"]
    year: 2012
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Our task is to map questions to answers via latent logical forms; alignment + bridging narrow the predicate space."
  page: 1
  image_path: "figures/berant-2013-semantic-parsing-freebase-fig.png"
---

# Semantic Parsing on Freebase from Question-Answer Pairs

**Authors:** Jonathan Berant, Andrew Chou, Roy Frostig, Percy Liang
**Published:** 2013-10 · [Source](https://aclanthology.org/D13-1160.pdf)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Berant, Chou, Frostig and Liang (Stanford, EMNLP 2013) train SEMPRE, a semantic parser that maps natural-language questions to executable λ-DCS logical forms over Freebase (41M entities, 19K properties, 596M assertions) using only question–answer pairs — no annotated logical forms. To survive the predicate-space blowup, they combine two write-time-light moves: (i) an **alignment lexicon** built from 15M ReVerb open-IE triples (yielding 55,081 typed binary phrases and 6,299 unary phrases mapped to a bipartite graph of 109K binary edges and 294K unary edges, scored by argument-overlap features) and (ii) a **bridging operator** that, when a connecting predicate isn't lexically expressed (light verbs, prepositions, omitted words), generates candidate binaries purely from the *type signatures* of neighbouring predicates. A discriminative log-linear model with intersection/join/bridging composition rules, POS-tag features, and denotation-size features (favouring derivations whose answer set has cardinality 1–3) is trained via AdaGrad to maximize the marginal log-likelihood of the correct denotation under a 500-best (FREE917) or 200-best (WEBQUESTIONS) beam. Results: 62% test accuracy on FREE917 (beating Cai & Yates 2013's 59% despite using no logical-form supervision), and 31.4% on the new WEBQUESTIONS dataset they release (5,810 Google-Suggest BFS-mined questions answered by AMT workers) versus a 26.9% baseline. Ablations show alignment alone hits 32.9% / bridging alone 21.2% on WEBQUESTIONS; combined gives 32.9% (alignment dominates on common predicates, bridging on rare typed ones — they're complementary). The actionable artifact: a pipeline where a **typed bipartite phrase↔predicate lexicon plus type-aware predicate-conjuring** is enough to ground free-form questions to a 41M-entity KB without per-example logical-form annotation, and a 5,810-question benchmark (WEBQUESTIONS) that anchored the next decade of open-domain KBQA work.

## Key Takeaway

The counter-intuitive move is to *give up* on aligning every phrase — instead, exploit the **type system of the knowledge graph as a generator of last resort**. When the lexicon can't tell you what predicate connects "Chile" and "government", you don't go find better text; you enumerate every binary whose `(t1, t2)` signature is `(FormOfGovernment, Country)` and let denotation features (does the answer set have size 1–3? do the POS tags suggest the right composition?) pick the winner. Lexical knowledge handles the popular path; **typed graph topology handles the long tail** — and the long tail is where annotated-logical-form parsers had been quietly failing for years.

## Implications

- **Alignment is a lossy write-time index; types are a query-time generator. Both belong in your stack.** [ENGRAM: N (Network — bipartite typed phrase↔predicate graph as the shape), R (Retrieve — bridging as on-the-fly candidate generation)]. The paper's bipartite graph is built once from 15M open-IE triples (write-time, ~hours), then bridging fires at parse-time for each question. Memory architectures that only do write-time synthesis (RAG with frozen chunks, knowledge graphs without typed traversal) miss the 21–67% accuracy that bridging recovers on rare predicates. Build the typed graph offline; reserve a query-time predicate-conjurer for cases the index misses.
- **Train on the cheap signal (answers) not the expensive one (logical forms).** [ENGRAM: A (Aggregate — supervision shape determines what compounds)]. Berant et al. beat Cai & Yates' state-of-the-art (62% vs 59% on FREE917) without ever seeing a logical form — by maximizing the marginal log-likelihood over latent derivations that produce the right *answer*. For agentic memory: if you want a system that learns to retrieve, supervise it on whether the final action/answer was right, not on whether the intermediate trace looked clean. The latent-derivation formulation is the template.
- **Make over-generation cheap and let features sort it out.** [ENGRAM: R (Retrieve — high-recall first, rerank second), G (Ground — features as trust signals)]. The composition rules (intersection, join, bridging) deliberately over-generate; ~12,000 distinct binary predicates appear in WEBQUESTIONS derivations. They never threshold edges of the bipartite graph (even "born in" and `Marriage.EndDate` co-occur 4 times). The trust layer is a downstream log-linear model with alignment-count features, POS conjunctions, and denotation-size features — *not* a hard filter. Memory systems that hard-prune at write time lose recall they can never recover; soft-rerank at read time.
- **Denotation-size as a presupposition prior is free signal.** [ENGRAM: G (Ground — built-in plausibility check)]. They feature-engineer 4 indicators on whether the candidate answer-set has size 0, 1, 2, or ≥3. Removing this alone drops FREE917 accuracy from 71.3% → 58.6% (Table 5). For a retrieval system: *the cardinality of what you return* is information. A query that should resolve to one fact and returns 50 is probably mis-routed; bake size priors in.
- **Build benchmarks where the supervision is cheap and the questions are real, even if noisier.** [ENGRAM: A, M — what you measure shapes what gets built]. FREE917 (917 questions hand-annotated with logical forms) bottlenecks at expertise. WEBQUESTIONS (5,810 questions mined from Google Suggest BFS, answered by AMT non-experts) is noisier but 6× larger and far more lexically diverse (4,525 word types vs 2,036). It became the canonical KBQA benchmark for the next decade. For your own memory evals: prefer messy real user queries with cheap-but-noisy ground truth over small clean expert-annotated sets.
- **Type signatures are an under-exploited generator of "memories that could have existed."** [ENGRAM: A (Aggregate — typed composition as a pattern-completion mechanism)]. Bridging works because Freebase's properties carry `(t1, t2)` type signatures and these signatures *constrain the hypothesis space tightly enough that brute enumeration is tractable*. If your memory store has typed entities (Person, Document, Conversation, Decision), you can synthesize candidate connecting predicates at query time without ever having seen the exact phrasing. The graph schema does the heavy lifting that prompting an LLM would otherwise be asked to do.
- **A typed bipartite index is a different shape from a flat embedding store — and pays off where embeddings are weakest.** [ENGRAM: N — choice of shape determines retrieval ceiling]. Polysemy ("born in" → `PlaceOfBirth` vs `DateOfBirth`) is resolved by augmenting phrases with type signatures (`born in[Person, Location]` vs `born in[Person, Date]`). A pure cosine-similarity over phrase embeddings would conflate these. If your domain has natural types, encoding them in the index shape is worth more than a bigger encoder.
- **Failure modes are recall failures, and they have a name: the long tail of rare predicates.** [ENGRAM: M (Maintain — know what you don't cover)]. Error analysis: bridging fails when the question's entity is type-compatible with too many binaries ("What did Charles Babbage make?" — too many things a Person can "make"). The fix isn't more data; it's more discriminative features. For agentic memory: instrument the long tail. Log which queries fall through to brute-enumeration and which downstream features fail to disambiguate — those are the next features to add, not the next sources to ingest.

## How to Apply It (method)

**Scenario:** You're building a memory layer for an AI workforce agent that needs to answer ad-hoc operational questions over a typed entity store — e.g., a venture-builder's Flow OS where memories are tagged with kinds (Decision, Contact, Project, Conversation, Metric) and properties (mentioned-in, owned-by, decided-on, depends-on). Users will ask free-form questions like "what did we decide about pricing for the AskRally enterprise tier?" or "who introduced me to Dana?". You don't have annotated logical forms — you have, at most, a log of (question → eventual-right-answer-or-action) pairs from past sessions. You want to learn a parser that maps NL → typed memory traversal, supervised only by whether the final retrieved set was correct.

**Steps:**

1. **Define your typed predicate schema.** Enumerate the kinds of memory edges in your store. For Flow OS: `mentionedIn(Memory, Conversation)`, `decidedOn(Decision, Date)`, `ownedBy(Project, Person)`, `introducedTo(Person, Person)`, etc. Each predicate has a type signature. This is the equivalent of Freebase's 19K typed properties — yours will be 20–200, which makes everything easier.

2. **Build the alignment lexicon from your own logs.** Mine your session transcripts and existing memory files for (phrase, entity-pair) co-occurrences. For each (`phrase`, `entity1`, `entity2`) triple in your data, find which memory predicates already connect `entity1` and `entity2`, and add an edge in a bipartite graph. Phrase nodes get type signatures: `"decided on"[Decision, Date]` vs `"decided on"[Decision, Person]`. Edge weights are |F(phrase) ∩ F(predicate)| — how many shared entity pairs they have. Run this once per indexing pass.

3. **Implement bridging at query time.** For each candidate (unary u1, unary u2) pair in the question (e.g., `Type.Pricing-Decision` and `Project.AskRally`), enumerate every predicate `b` whose type signature matches `(type(u1), type(u2))` and emit a candidate logical form `u1 ⊓ b.u2`. Also support single-unary bridging: given any unary z of type t, generate `b.z` for every predicate b of signature `(*, t)`. This is the type-driven candidate generator.

4. **Write the composition over-generator.** For each question, build a beam (k=100–500) of candidate derivations using three composition rules: intersection (`u1 ⊓ u2`), join (`b.u`), and bridging (above). Allow word-skipping (light verbs, prepositions). Don't worry about precision — let the feature model sort it out downstream.

5. **Feature-engineer the discriminative reranker.** For each derivation, extract: alignment-count features (log of edge weight in the bipartite graph), lexicalized features (phrase ⊗ predicate conjunctions), text-similarity features (phrase vs predicate name string overlap), bridging features (log |F(b)|, kind of bridging used, the binary identity), composition rule counts (indicator on n_join, n_bridge, n_intersect), POS-tag features on combined spans, **denotation-size features (was the answer set 0, 1, 2, or ≥3?)**. Train a log-linear model with AdaGrad to maximize log-marginal-likelihood of the right answer:

   ```
   O(θ) = Σ_i log Σ_{d ∈ Beam(x_i) : execute(d.z) = y_i} p_θ(d | x_i)
   ```

   where `p_θ(d|x) ∝ exp(φ(x,d)·θ)`. Six passes over training data is the paper's default.

6. **Use POS tagging + NER as syntactic filters on what spans can be lexicalized.** Entities must be NNPs or sequences of ≥2 tokens. Unaries must be noun sequences. Binaries must be content words or verb+noun-phrase patterns. Hand-write 10–20 question-word → logical-form rules ("where" → `Type.Location`, "how many" → `Count`, "when" → `Type.Date`). This is cheap and prevents the parser from drowning in junk derivations.

7. **Evaluate with exact-match accuracy on a held-out 30% of (question, expected-answer) pairs.** Track also: oracle score (fraction where ANY beam derivation hits the right answer — your recall ceiling) and accuracy-vs-oracle gap as a function of beam size k.

8. **Ablate your features.** Drop alignment features, drop bridging, drop denotation-size — measure the delta on dev. The paper saw -POS = -2.8 pts and -DENOTATION = -12.7 pts on FREE917, which tells you which features are doing the work.

**Expected outcome:** A typed-graph-aware semantic parser that maps free-form operator questions to executable traversals over your memory store, trained only on session-level success signals. You'll get a working benchmark of where the long tail of rare predicates fails (your bridging error analysis) and a feature-importance ranking that tells you exactly what to instrument next. The reusable artifact is the bipartite typed phrase↔predicate index plus the type-aware bridging generator — both portable to any new memory schema.

## Best Figure

![Figure 1 — Our task is to map questions to answers via latent logical forms; alignment + bridging narrow the predicate space (page 1)](figures/berant-2013-semantic-parsing-freebase-fig.png)

Image Candidates:
Figure 1 (p. 1): The architecture-in-one-picture — "Which college did Obama go to?" walks up the derivation tree showing alignment (red, lexicon-grounded) and bridging (purple, type-driven) edges converging on the executable λ-DCS form `Type.University ⊓ Education.BarackObama`.
Table 4 (p. 8): The headline ablation — alignment-only (38.0 / 30.6), bridging-only (66.9 / 21.2), and full system (71.3 / 32.9) across FREE917 and WEBQUESTIONS, showing the two components are *complementary*, not redundant.
Figure 5 (p. 9): Accuracy and oracle curves vs beam size k on both datasets — the visual proof of the recall ceiling and the widening accuracy-vs-oracle gap as beams grow.

Best Image:
Figure Name: Figure 1: "Our task is to map questions to answers via latent logical forms..."
Figure Page: 1
Slide Caption: SEMPRE: alignment grounds common phrases to predicates, while bridging conjures connecting predicates from type signatures — both feed the executable logical form.
Description: Figure 1 shows the full inference pipeline on the example "Which college did Obama go to?". The bottom row holds the question tokens. Each token is mapped via the **alignment lexicon** (red dotted edges, "Which/college" → `Type.University`, "Obama" → `BarackObama`) to logical predicates. Because no surface phrase grounds the `Education` predicate (the connecting binary), a **bridging** edge (purple) is generated purely from the type signature `(University, Person)`, conjuring `Education` from the type-compatible neighbours. The composition rules then assemble `Type.University ⊓ Education.BarackObama`, which is executed against Freebase to return `Occidental College, Columbia University`. The figure compresses the paper's entire contribution — alignment as a lexical index, bridging as a typed predicate generator, composition as soft over-generate-then-rerank — into one walkable diagram. It's the figure to put on a slide.

## What Experts Overlook

The detail most readers miss is that **the alignment lexicon's bipartite graph is built over *typed* phrases, not raw phrases** — `"born in"[Person, Location]` and `"born in"[Person, Date]` are two distinct nodes with two distinct extensions and two distinct sets of features (Section 3.1, "Typed phrases"). The same surface string lives at multiple nodes in the graph, each carrying a different type signature. This is what makes polysemy resolution mostly free: the parser never has to "disambiguate `born in`" — the lexicon already shipped two of it, and the composition step only fires the type-compatible variant in any given derivation context. The 55,081 typed binary phrases vs the 9,456 untyped phrases (Section 3.1) is the give-away: roughly 6× expansion from typing.

**Why it matters:** Most experts assume the magic in this system is bridging — the dramatic type-driven predicate-conjuring. It is. But bridging only works because the *lexicon shape* already commits to types, which means every retrieval already comes with type metadata attached. If the lexicon were untyped (just `"born in"` → set of predicates), the parser would need a separate disambiguation pass at every node, and the feature signal would have to do double duty. By baking types into the **index shape** rather than into a downstream classifier, they push the polysemy-resolution work to the cheap side (more nodes in a graph, more rows in an inverted index) and free the model to focus on composition. It's a write-time decision that buys query-time cleanliness.

**Example of good use:** A memory-architect building a typed knowledge graph for a venture-builder's Flow OS does the same trick: instead of indexing `"introduced"` as a single phrase, they index `"introduced"[Person, Person]` (matching `introducedTo`), `"introduced"[Person, Product]` (matching `endorsed` or `launched`), and `"introduced"[Person, Concept]` (matching `taughtMe`). Query-time retrieval over "Who introduced me to vector databases?" walks the typed graph directly to the `Person → Concept` edges without needing a separate sense-disambiguation LLM call. The index shape did the work.

**Example of misapplication:** The same architect, building the index without typing, gets a `"introduced"` node with 40 candidate predicates pointing out of it. Every query touching that phrase fires all 40 candidates into the beam, the beam fills up with junk, the denotation-size features can't rescue it because half the candidates return non-empty plausible-looking sets, and accuracy collapses on the rare predicates that needed the type filter most. The bug looks like "bridging doesn't work for our domain" — it's actually "we never gave bridging the type signatures it needs to constrain its enumeration."

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- Cai, Q., Yates, A. (2013). Large-scale semantic parsing via schema matching and lexicon extension. ACL. (the direct prior-state-of-the-art baseline they beat on FREE917)
- Zettlemoyer, L., Collins, M. (2005). Learning to map sentences to logical form: Structured classification with probabilistic categorial grammars. UAI. (foundational CCG-based semantic parsing)
- Kwiatkowski, T., Zettlemoyer, L., Goldwater, S., Steedman, M. (2010). Inducing probabilistic CCG grammars from logical form with higher-order unification. EMNLP.
- Kwiatkowski, T., Zettlemoyer, L., Goldwater, S., Steedman, M. (2011). Lexical generalization in CCG grammar induction for semantic parsing. EMNLP.
- Liang, P., Jordan, M.I., Klein, D. (2011). Learning dependency-based compositional semantics. ACL. (DCS, the parent formalism of λ-DCS used here)
- Liang, P. (2013). Lambda dependency-based compositional semantics. ArXiv technical report. (the λ-DCS reference)
- Fader, A., Soderland, S., Etzioni, O. (2011). Identifying relations for open information extraction. EMNLP. (ReVerb, source of the 15M triples used for alignment)
- Lin, T., Mausam, Etzioni, O. (2012). Entity linking at web scale. AKBC-WEKEX. (Freebase-linked triples used as the alignment corpus)
- Krishnamurthy, J., Mitchell, T. (2012). Weakly supervised training of semantic parsers. EMNLP/CoNLL.
- Duchi, J., Hazan, E., Singer, Y. (2010). Adaptive subgradient methods for online learning and stochastic optimization. COLT. (AdaGrad)

Remaining 33 citations are in frontmatter for downstream walking.

## Related Digests

- [[chen-2017-drqa-machine-reading]] — DrQA cites Berant as a foundational KBQA benchmark; DrQA pivots to unstructured-text QA over Wikipedia
- [[lewis-2020-rag-knowledge-nlp]] — RAG generalizes the alignment-then-compose idea with neural retrieval + generation; cites WEBQUESTIONS-style benchmarks
- [[guu-2020-realm]] — REALM does end-to-end retrieval + reading, evaluated partly on KBQA-style tasks; same supervise-on-answer-only philosophy
- [[roberts-2020-pack-knowledge]] — Asks the inverse question: how much of Freebase-style KB knowledge can be packed into LLM parameters; cites Berant as the canonical KBQA evaluation
- [[brown-2020-gpt3-few-shot]] — GPT-3 evaluates few-shot QA on the same benchmark lineage; Berant's WEBQUESTIONS sits in the QA evaluation suite

## Reviewer Notes

**Overall severity:** Clean

All claims in the digest are supported by the paper text — the dataset statistics (15M triples, 55,081 typed binary phrases, 6,299 unary phrases, 109K binary edges, 294K unary edges, 41M entities, 19K properties, 596M assertions), the accuracy numbers (62% test on FREE917, 31.4% vs 26.9% baseline on WEBQUESTIONS, ablation deltas in Tables 4–6), the methods (λ-DCS, AdaGrad, six training passes, beam sizes k=500/200), and the architectural moves (typed bipartite lexicon, bridging via type signatures, denotation-size features) are all directly traceable to Sections 2–4 and the tables. The lens-tagged ENGRAM interpretations are clearly framed as inference for the memory-architect reader and do not assert the paper itself uses that framework. No fabricated tools, metrics, or experiments.
