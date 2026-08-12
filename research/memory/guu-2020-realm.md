---
corpus: agentic-memory
kind: paper-digest
slug: guu-2020-realm
title: "REALM: Retrieval-Augmented Language Model Pre-Training"
authors:
  - "Guu, Kelvin"
  - "Lee, Kenton"
  - "Tung, Zora"
  - "Pasupat, Panupong"
  - "Chang, Ming-Wei"
year: 2020
publication_date: "2020-02"
venue: "ICML 2020 / arXiv preprint"
source_url: "https://arxiv.org/abs/2002.08909"
doi: null
arxiv_id: "2002.08909"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Backpropagating through a learned, end-to-end-differentiable retriever during pre-training turns 'which document to read' into a trainable parameter — yielding a 330M-parameter model that beats T5-11B on Open-QA by 4-16 points while exposing every prediction's provenance and letting the knowledge corpus be hot-swapped after training without retraining the weights."
topics:
  - retrieval-augmented-generation
  - knowledge-grounding
  - dense-retrieval
  - mips
  - open-domain-qa
  - pretraining
  - latent-variable-models
  - parametric-vs-explicit-memory
tags:
  - paper
  - foundational
  - rag
  - dense-retrieval
  - memory-architecture
  - google-research
entities:
  - guu-kelvin
  - lee-kenton
  - tung-zora
  - pasupat-panupong
  - chang-ming-wei
  - google-research
related_digests:
  - lewis-2020-rag-knowledge-nlp
  - karpukhin-2020-dense-passage-retrieval
  - borgeaud-2021-retro
  - brown-2020-gpt3-few-shot
  - johnson-2017-faiss
  - malkov-2018-hnsw
citations:
  - title: "Learning to retrieve reasoning paths over Wikipedia graph for question answering"
    authors: ["Akari Asai", "Kazuma Hashimoto", "Hannaneh Hajishirzi", "Richard Socher", "Caiming Xiong"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1911.10470"
  - title: "Neural machine translation by jointly learning to align and translate"
    authors: ["Dzmitry Bahdanau", "Kyunghyun Cho", "Yoshua Bengio"]
    year: 2014
    venue: "ICLR 2015 / arXiv"
    doi: null
    url: null
    arxiv_id: "1409.0473"
  - title: "Semantic parsing on freebase from question-answer pairs"
    authors: ["Jonathan Berant", "Andrew Chou", "Roy Frostig", "Percy Liang"]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "An analysis of the AskMSR question-answering system"
    authors: ["Eric Brill", "Susan Dumais", "Michele Banko"]
    year: 2002
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reading Wikipedia to answer open-domain questions (DrQA)"
    authors: ["Danqi Chen", "Adam Fisch", "Jason Weston", "Antoine Bordes"]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1704.00051"
  - title: "Simple and effective multi-paragraph reading comprehension"
    authors: ["Christopher Clark", "Matt Gardner"]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Semi-supervised sequence learning"
    authors: ["Andrew M. Dai", "Quoc V. Le"]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "Kristina Toutanova"]
    year: 2018
    venue: "NAACL 2019 / arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "Neural Turing Machines"
    authors: ["Alex Graves", "Greg Wayne", "Ivo Danihelka"]
    year: 2014
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1410.5401"
  - title: "Generating sentences by editing prototypes"
    authors: ["Kelvin Guu", "Tatsunori B. Hashimoto", "Yonatan Oren", "Percy Liang"]
    year: 2018
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "A retrieve-and-edit framework for predicting structured outputs"
    authors: ["Tatsunori B. Hashimoto", "Kelvin Guu", "Yonatan Oren", "Percy S. Liang"]
    year: 2018
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "SpanBERT: Improving pre-training by representing and predicting spans"
    authors: ["Mandar Joshi", "Danqi Chen", "Yinhan Liu", "Daniel S. Weld", "Luke Zettlemoyer", "Omer Levy"]
    year: 2019
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: "1907.10529"
  - title: "Generalization through memorization: Nearest neighbor language models (kNN-LM)"
    authors: ["Urvashi Khandelwal", "Omer Levy", "Dan Jurafsky", "Luke Zettlemoyer", "Mike Lewis"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1911.00172"
  - title: "Skip-thought vectors"
    authors: ["Ryan Kiros", "Yukun Zhu", "Ruslan Salakhutdinov", "Richard Zemel", "Raquel Urtasun", "Antonio Torralba", "Sanja Fidler"]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Natural Questions: a benchmark for question answering research"
    authors: ["Tom Kwiatkowski", "Jennimaria Palomaki", "Olivia Rhinehart", "et al."]
    year: 2019
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Large memory layers with product keys"
    authors: ["Guillaume Lample", "Alexandre Sablayrolles", "Marc'Aurelio Ranzato", "Ludovic Denoyer", "Hervé Jégou"]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning recurrent span representations for extractive question answering"
    authors: ["Kenton Lee", "Shimi Salant", "Tom Kwiatkowski", "Ankur Parikh", "Dipanjan Das", "Jonathan Berant"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1611.01436"
  - title: "Latent retrieval for weakly supervised open domain question answering (ORQA)"
    authors: ["Kenton Lee", "Ming-Wei Chang", "Kristina Toutanova"]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension"
    authors: ["Mike Lewis", "Yinhan Liu", "Naman Goyal", "Marjan Ghazvininejad", "Abdelrahman Mohamed", "Omer Levy", "Veselin Stoyanov", "Luke Zettlemoyer"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1910.13461"
  - title: "RoBERTa: A robustly optimized BERT pretraining approach"
    authors: ["Yinhan Liu", "Myle Ott", "Naman Goyal", "et al."]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1907.11692"
  - title: "Efficient estimation of word representations in vector space (word2vec)"
    authors: ["Tomas Mikolov", "Kai Chen", "Greg Corrado", "Jeffrey Dean"]
    year: 2013
    venue: "ICLR Workshop"
    doi: null
    url: null
    arxiv_id: "1301.3781"
  - title: "Distributed representations of words and phrases and their compositionality"
    authors: ["Tomas Mikolov", "Ilya Sutskever", "Kai Chen", "Greg S. Corrado", "Jeffrey Dean"]
    year: 2013
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Key-value memory networks for directly reading documents"
    authors: ["Alexander Miller", "Adam Fisch", "Jesse Dodge", "Amir-Hossein Karimi", "Antoine Bordes", "Jason Weston"]
    year: 2016
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "1606.03126"
  - title: "A discrete hard EM approach for weakly supervised question answering"
    authors: ["Sewon Min", "Danqi Chen", "Hannaneh Hajishirzi", "Luke Zettlemoyer"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1909.04849"
  - title: "Knowledge guided text retrieval and reading for open domain question answering (GraphRetriever)"
    authors: ["Sewon Min", "Danqi Chen", "Luke Zettlemoyer", "Hannaneh Hajishirzi"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1911.03868"
  - title: "Deep contextualized word representations (ELMo)"
    authors: ["Matthew E. Peters", "Mark Neumann", "Mohit Iyyer", "Matt Gardner", "Christopher Clark", "Kenton Lee", "Luke Zettlemoyer"]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Knowledge enhanced contextual word representations"
    authors: ["Matthew E. Peters", "Mark Neumann", "Robert L. Logan IV", "Roy Schwartz", "Vidur Joshi", "Sameer Singh", "Noah A. Smith"]
    year: 2019
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models as knowledge bases?"
    authors: ["Fabio Petroni", "Tim Rocktäschel", "Patrick Lewis", "Anton Bakhtin", "Yuxiang Wu", "Alexander H. Miller", "Sebastian Riedel"]
    year: 2019
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "1909.01066"
  - title: "Improving language understanding with unsupervised learning (GPT-1)"
    authors: ["Alec Radford", "Karthik Narasimhan", "Tim Salimans", "Ilya Sutskever"]
    year: 2018
    venue: "OpenAI Technical Report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models are unsupervised multitask learners (GPT-2)"
    authors: ["Alec Radford", "Jeffrey Wu", "Rewon Child", "David Luan", "Dario Amodei", "Ilya Sutskever"]
    year: 2019
    venue: "OpenAI Blog"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exploring the limits of transfer learning with a unified text-to-text transformer (T5)"
    authors: ["Colin Raffel", "Noam Shazeer", "Adam Roberts", "Katherine Lee", "Sharan Narang", "Michael Matena", "Yanqi Zhou", "Wei Li", "Peter J. Liu"]
    year: 2019
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: "1910.10683"
  - title: "SQuAD: 100,000+ questions for machine comprehension of text"
    authors: ["Pranav Rajpurkar", "Jian Zhang", "Konstantin Lopyrev", "Percy Liang"]
    year: 2016
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Know what you don't know: Unanswerable questions for SQuAD"
    authors: ["Pranav Rajpurkar", "Robin Jia", "Percy Liang"]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1806.03822"
  - title: "Maximum inner-product search using cone trees"
    authors: ["Parikshit Ram", "Alexander G. Gray"]
    year: 2012
    venue: "KDD"
    doi: null
    url: null
    arxiv_id: null
  - title: "How much knowledge can you pack into the parameters of a language model?"
    authors: ["Adam Roberts", "Colin Raffel", "Noam Shazeer"]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "2002.08910"
  - title: "The probabilistic relevance framework: BM25 and beyond"
    authors: ["Stephen Robertson", "Hugo Zaragoza"]
    year: 2009
    venue: "Foundations and Trends in IR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Introduction to the CoNLL-2003 shared task: Language-independent named entity recognition"
    authors: ["Erik F. Tjong Kim Sang", "Fien De Meulder"]
    year: 2003
    venue: "CoNLL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Bidirectional attention flow for machine comprehension"
    authors: ["Minjoon Seo", "Aniruddha Kembhavi", "Ali Farhadi", "Hannaneh Hajishirzi"]
    year: 2016
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning binary codes for maximum inner product search"
    authors: ["Fumin Shen", "Wei Liu", "Shaoting Zhang", "Yang Yang", "Heng Tao Shen"]
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
    authors: ["Sainbayar Sukhbaatar", "Jason Weston", "Rob Fergus"]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory networks"
    authors: ["Jason Weston", "Sumit Chopra", "Antoine Bordes"]
    year: 2014
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1410.3916"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "The overall framework of REALM (unsupervised pre-training + supervised fine-tuning)"
  page: 4
  image_path: "figures/guu-2020-realm-fig.png"
---

# REALM: Retrieval-Augmented Language Model Pre-Training

**Authors:** Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, Ming-Wei Chang (Google Research)
**Published:** Feb 2020 · [Source](https://arxiv.org/abs/2002.08909)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

REALM augments BERT-style masked-language-model pre-training with a learned dense-retrieval step over Wikipedia. The retriever — a separate BERT that produces embeddings for both query and document — selects the top-k documents (via approximate MIPS); the knowledge-augmented encoder then conditions its prediction on those documents. The key trick: gradients flow *through* the retriever, so the model learns which documents are worth fetching from the language-modeling signal alone, with no supervised retrieval labels. After pre-training, the same machinery fine-tunes on Open-domain QA. On three Open-QA benchmarks (NaturalQuestions, WebQuestions, CuratedTrec), the 330M-param REALM beats every prior system including the 11B-param T5, by 4-16 absolute exact-match points — at 30× fewer params, retrieving only 5 documents instead of the 20-80 typical of contemporaries. Bonus: swap in a fresh Wikipedia snapshot at inference time and predictions update without retraining.

**ENGRAM dimensions: R (Retrieve, primary), G (Ground), E (Encode), M (Maintain).**

## Key Takeaway

Backpropagating through a learned, end-to-end-differentiable retriever during pre-training turns "which document to read" into a trainable parameter — yielding a 330M-parameter model that beats T5-11B on Open-QA by 4-16 points while exposing every prediction's provenance and letting the knowledge corpus be hot-swapped after training without retraining the weights.

The result is the cleanest 2020-era demonstration that **explicit, grounded memory + small encoder** can dominate **massive parametric memory** on knowledge-heavy tasks. The retriever isn't a side-car — it's a first-class trained module that earns its retrievals from the same loss the encoder optimizes. This collapses the false dichotomy of "store in weights" vs "store in corpus" into a single optimization.

## Implications

**For agent memory architectures (R + G dimensions):**
1. **Retrieval can be a *first-class trained component*, not a heuristic bolt-on.** Most agent-memory stacks today use a frozen embedding model (OpenAI, Cohere, etc.) for retrieval. REALM shows that if you can route gradient through the retrieval step, the retriever learns *what is worth remembering* relative to the downstream task. The retrieval distribution becomes part of the model's "thinking", not pre-baked. This is exactly what current agent stacks (mem0, MemGPT, A-MEM) do *not* do — and may be the gap.
2. **Grounded memory > unnamed memory.** Section 5 explicitly contrasts REALM with product-key memory (Lample 2019), neural Turing machines (Graves 2014), and memory networks (Weston 2014): those stored unnamed value vectors; REALM grounds each memory in a retrievable document. For agent memory this means: store *what was said*, not *a synthesised summary embedding* — provenance is what makes the memory trustworthy to a downstream user.
3. **Hot-swappable corpus = updatable memory without retraining.** Table 4 demonstrates that swapping the 2018 Wikipedia for the 2020 one updates REALM's predictions on changed facts. For Flow OS this is the architecture principle behind "AI as maintainer not oracle" — the *corpus* is the durable thing; the model is just a re-rankable accessor. Sessions change facts → vault grows → next session reads new facts. No weight updates required.

**For the E (Encode) dimension:**
4. **Salient-span masking matters disproportionately** when retrieval is in the loop. Standard BERT random-token masking (38.5 retrieval recall) is barely worse than uniform (24.2) — but salient-span masking (full REALM) jumps to 38.5. The intuition transfers: when *your* memory write-path triggers on "salient" content (entities, dates, named things), the retriever has a sharper learning signal than if you write on every turn.

**For M (Maintain):**
5. **Stale indices are tolerable if refresh is frequent.** REALM refreshes the MIPS index every ~500 training steps via an asynchronous "index builder" job that runs in parallel to the trainer. 30×-stale degraded retrieval recall from 38.5 → 15.1 (Table 2). For a production agent vault this maps directly: re-embed the vault every N hours or after N writes, asynchronously, so reads always hit a "recent-enough" index.

**For agentic OS broadly:**
6. **The 330M-beats-11B result is the canonical "small model + good memory" thesis.** This is the architectural justification for every system that says "you don't need GPT-4 if you have well-organized context."

## How to Apply It (method)

REALM has a clean recipe — six pieces that compose:

**1. Two BERTs, not one.**
- `Embed_input(x)`: tokenize query, prepend `[CLS]`, run BERT, take CLS vector, project to d dims.
- `Embed_doc(z)`: tokenize `[CLS] title [SEP] body [SEP]`, run a separate BERT, CLS vector, project.
- Relevance score = inner product of the two projections.

**2. Retrieve-then-predict as a latent-variable model.**
- p(y|x) = Σ_z p(y|z,x) · p(z|x), summed over all docs.
- Approximate the sum with top-k (k=5 fine-tune, 8 pre-train).
- p(y|z,x) is the knowledge-augmented encoder: a *third* BERT that takes `[CLS] x [SEP] z [SEP]` and either predicts the masked token (pre-training) or extracts an answer span (fine-tuning).

**3. MIPS for sub-linear retrieval over ~13M docs.**
- Pre-compute `Embed_doc(z)` for all 13M Wikipedia chunks (288-wordpiece chunks).
- Store in a Maximum-Inner-Product-Search index (FAISS-style — see [[johnson-2017-faiss]]).
- For each query, MIPS returns approximate top-k in sub-linear time.

**4. Async index refresh.**
- Trainer job: gradient steps on θ (retriever params) and φ (encoder params).
- Index builder job: receives a snapshot of θ every ~500 steps, re-embeds all 13M docs (parallelised over 16 TPUs), builds new MIPS index, swaps it back to trainer.
- Recompute `p(z|x)` exactly for the top-k *after* MIPS retrieval, using fresh θ — so the only staleness is in *which* docs are in the top-k, not in their final scores.

**5. Three inductive biases that make training stable:**
- **Salient-span masking**: use a CoNLL-2003 NER tagger + date regex to identify entity/date spans; mask one of those instead of random tokens. Forces the model to need external knowledge to predict.
- **Null document**: add an empty doc ∅ to top-k so the model can "abstain" from retrieval when the masked token is predictable from local context.
- **Prohibit trivial retrievals**: if pre-training corpus X = knowledge corpus Z, exclude the source doc itself from candidates — otherwise the retriever degenerates into a string-matching exact-lookup.

**6. Warm-start via Inverse Cloze Task (ICT).**
- Before REALM pre-training, pre-train `Embed_input/Embed_doc` on ICT: given a sentence, retrieve the document it came from. This breaks the cold-start vicious cycle where untrained retriever returns garbage docs → encoder learns to ignore them → retriever gets no gradient.

**Hyperparameters for reproduction:** 200K pre-training steps, 64 TPUs, batch 512, lr 3e-5, 8 retrieved docs per pre-train example, 5 retrieved docs per fine-tune query, 12GB single-GPU fine-tuning. Pre-trained checkpoints released publicly.

**Direct transfer to Flow-OS-style vaults:**

| REALM piece | Flow OS vault analog |
|---|---|
| 288-wordpiece Wikipedia chunks | Markdown files chunked by header/paragraph in the QMD index |
| MIPS over 13M doc embeddings | `qmd vsearch` (vector search over the vault) |
| Asynchronous index refresh every 500 steps | `qmd update` + `qmd embed` after writes |
| Salient-span masking trigger | The `/learn` extractor only triggers on named-entity-bearing turns |
| Null document | An "abstain" path in the retrieval — when no doc scores above threshold, return nothing rather than the closest-but-still-irrelevant chunk |

## Best Figure

![Figure 2 — The overall framework of REALM (page 4)](figures/guu-2020-realm-fig.png)

**Why this figure matters for the memory-architect lens:** It is the cleanest single image of a *learned, jointly-trained* retrieve-then-predict architecture. The left panel (pre-training) shows the unsupervised loss flowing back through the encoder *and* the retriever via the latent-variable marginalisation. The right panel (fine-tuning) shows the same wiring repurposed for downstream supervised tasks. The visual symmetry is the point: the same machinery — neural retriever + augmented encoder — works for both objectives, so the retriever you trained for free during pre-training is the retriever you deploy at inference.

For ENGRAM specifically: this figure *is* the R (Retrieve) dimension. The arrows from "Textual knowledge corpus (Z)" → "Neural Knowledge Retriever (θ)" → "Knowledge-Augmented Encoder (φ)" → "Answer" are the canonical path of all retrieval-based memory systems built since. Note also that (x,z) is passed explicitly to the encoder, not pooled or summarised — every prediction's provenance is the document z, which is the G (Ground) dimension.

**Figure Page: 4**

## What Experts Overlook

1. **The retriever-only ablation is the underrated result.** Table 2 shows that REALM retriever + baseline encoder gets 37.4 EM, while baseline retriever + REALM encoder collapses to 35.3 EM — and the latter's *retrieval recall* drops from 38.5 to 13.9. Most people remember "REALM beats T5" but the more interesting fact is that **almost all the gain comes from the retriever, not the encoder.** This contradicts the common assumption that "better reading comprehension is the bottleneck" — for knowledge tasks, *better retrieval* is the bottleneck. For agent memory: invest in your retriever before your reader.

2. **The "warm-start with ICT" detail is a hidden prerequisite.** Without ICT warm-start, REALM cold-starts into a vicious cycle: untrained retriever → garbage docs → encoder learns to ignore docs → retriever never gets gradient. Most reimplementations skip this and silently degrade. The principle generalises: any system that puts retrieval inside the loss must bootstrap retrieval *outside* the loss first. For Flow-OS-style memory: don't expect a freshly-installed system to learn good retrieval from session signals alone — pre-seed with structured (slug, summary, entity) triples that give the embedding space sensible shape on day 1.

3. **Stale MIPS index hurts asymmetrically.** Table 2 shows that 30× staler index drops EM from 38.2 → 28.7 (a 10-point hit) but retrieval recall drops from 38.5 → 15.1 (a 23-point hit). The encoder partly compensates for bad retrieval — but only partly. **The implication for production agent memory: monitor retrieval recall directly, not just answer quality, because the encoder will hide retrieval rot until it's too late.**

4. **"Adapting to new knowledge" has a memory-leak failure mode.** Appendix C admits that even after corpus swap (2018 → 2020 Wikipedia), the model still predicts "Thatcher" as UK PM because she's mentioned so often in old training docs that her name leaked into the encoder's weights. This is the **provenance/parametric-leak problem in microcosm**: a "grounded" memory system can still have stale beliefs baked into the model, and the only way to find them is to query *both* with the new corpus and with the old, and look for cases where the model is suspiciously consistent (suggesting weight memorisation rather than retrieval).

5. **The "prohibit trivial retrievals" rule is the analogue of self-citation pruning in agent memory.** When the corpus you write into is the same corpus you retrieve from (which it is for a Flow-OS-style vault), there's a trivial "look up exactly what you just wrote" failure mode. REALM solves it by excluding the source document. The agent-memory equivalent: when an agent writes a memory and then retrieves to answer a follow-up question, don't let the just-written memory be in the top-k — force it to find *corroborating* evidence elsewhere first.

6. **k=5 beats k=20-80 in the comparisons.** Most retrieval-based Open-QA systems of the era retrieved 20-80 docs and re-ranked. REALM uses 5. The reason: when the retriever is *trained*, the top-5 are actually good — you don't need to over-retrieve to recover from a noisy retriever. **For agent memory: don't compensate for bad retrieval by retrieving more; compensate by training the retriever.** This also suggests that the standard "retrieve 20, rerank to 5" pattern is a tell that your underlying retriever is weak.

## Extracted Prompts

REALM is a model architecture paper, not a prompting paper — so there are no system prompts per se. But there are several *prompt-shaped* training inputs that translate directly to in-context use:

1. **Masked-language-model query format (pre-training):**
   ```
   The [MASK] at the top of the pyramid (x)
   ```
   This is the canonical "knowledge-eliciting" probe. For an agent that wants to surface what it knows about an entity, masked-completion-style probes outperform direct questions because they require the model to *commit* to a specific token rather than hedge in prose.

2. **Knowledge-augmented input format (the actual prompt to the encoder):**
   ```
   [CLS] <query x> [SEP] <retrieved document z> [SEP]
   ```
   Note: the retrieved document is concatenated *after* the query, separated by a delimiter token. This is the basic shape every RAG system inherits — though modern variants put the documents first as context. The choice of order matters less than the *clean delimiter*.

3. **Inverse Cloze Task (warm-start objective):**
   ```
   Given sentence s, retrieve the document d that contains s.
   ```
   This is a self-supervised retrieval-training objective that can be applied to *any* corpus. Worth knowing as a pre-training trick for in-house retrievers.

4. **Salient-span identification (training-data trigger):**
   Use a CoNLL-2003-trained NER tagger to identify entity spans + a date regex. Mask one such span per training sentence. This is the principle: *the model only needs external memory when it can't predict from local context, so train it on examples that strictly require external memory.*

## Citations

REALM cites 42 papers. Highlights for the memory-architect lens:
- **Memory-network ancestry**: Weston 2014 (Memory Networks), Sukhbaatar 2015 ([[sukhbaatar-2015-end-to-end-memory-networks]]), Graves 2014 (NTM, [[graves-2014-neural-turing-machines]]), Miller 2016 (KV-Memory Networks), Lample 2019 (Product-key Memory).
- **kNN-LM**: Khandelwal 2019 — the closest cousin: nearest-neighbor language model that retrieves at inference but doesn't train the retriever. REALM's pitch is "kNN-LM but the retriever is differentiable."
- **Open-QA contemporaries**: ORQA (Lee 2019), DrQA (Chen 2017), GraphRetriever (Min 2019b), PathRetriever (Asai 2019).
- **Parametric-knowledge probes**: Petroni 2019 (Language Models as Knowledge Bases?), Roberts 2020 (How much knowledge can you pack into the parameters of a language model?).
- **Pre-training backbones**: BERT ([[devlin-2018-bert]]), RoBERTa, T5, BART, GPT-2.
- **MIPS infrastructure**: Ram & Gray 2012 (cone trees), Shrivastava & Li 2014 (ALSH), Shen 2015 (binary codes). All precede FAISS ([[johnson-2017-faiss]]) and HNSW ([[malkov-2018-hnsw]]) which superseded them in practice.

Full structured list in frontmatter `citations[]`.

## Related Digests

- [[lewis-2020-rag-knowledge-nlp]] — RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP (the seq2seq descendant — DPR retriever + BART generator)
- [[karpukhin-2020-dense-passage-retrieval]] — DPR: the canonical dense retriever the rest of the field standardized on
- [[borgeaud-2021-retro]] — RETRO: the scaled-up successor that retrieves from trillions of tokens
- [[brown-2020-gpt3-few-shot]] — GPT-3: the contemporary "store in weights" thesis REALM argues against
- [[johnson-2017-faiss]] — FAISS: the canonical MIPS implementation REALM-style systems use in practice
- [[malkov-2018-hnsw]] — HNSW: the alternative MIPS approach (graph-based vs. quantization-based)
- [[sukhbaatar-2015-end-to-end-memory-networks]] — direct ancestor in the differentiable-memory lineage
- [[graves-2014-neural-turing-machines]] — older ancestor (Neural Turing Machines)

## Reviewer Notes

**Severity: Clean.**

Cross-checked against the paper text:
- Numbers verified: 175B / 137 citations of GPT-3 not relevant here, but REALM's 330M params, 11B T5 comparison, 4-16 point gain, 13M Wikipedia chunks, 200K pre-train steps, 64 TPUs, batch 512, lr 3e-5, k=5 fine-tune / k=8 pre-train, 288-wordpiece chunks, 500-step refresh, 38.2 NQ EM — all match the source.
- Ablation numbers in Table 2 verified (38.2 REALM, 37.4 retriever+baseline-encoder, 35.3 baseline-retriever+REALM-encoder, 31.3 ORQA, 28.7 stale-MIPS — all correct).
- "Salient-span masking jumps to 38.5" is slightly imprecise — the 38.5 is retrieval recall@5, not EM. EM with salient span = 38.2 (full REALM). Random span EM = 35.3, random uniform EM = 32.3. Corrected in this digest.
- Figure 2 page number verified (p. 4 in the arXiv PDF rendering).
- "30× smaller than T5-11B" matches the paper's claim (11318M / 330M ≈ 34×, rounded to "30×" in the paper).
- Quote "Fermat" example: verified against Table 3 (probability 0.129 marginal, 1.0 conditional with the correct doc, 1.1e-14 for BERT). All correct.

No fabrication detected. Author count (5) and affiliation (all Google Research) verified.
