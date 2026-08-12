---
corpus: agentic-memory
kind: paper-digest
slug: roberts-2020-pack-knowledge
title: "How Much Knowledge Can You Pack Into the Parameters of a Language Model?"
authors:
  - "Roberts, Adam"
  - "Raffel, Colin"
  - "Shazeer, Noam"
year: 2020
publication_date: "2020-02"
venue: "EMNLP 2020 / arXiv preprint"
source_url: "https://arxiv.org/abs/2002.08910"
doi: null
arxiv_id: "2002.08910"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "An 11-billion-parameter T5 fine-tuned on question-answer pairs alone — with zero retrieval, zero context, zero external knowledge — reaches 61.6% exact-match on TriviaQA and is competitive with explicit-retrieval systems on Natural Questions, proving that parametric memory at sufficient scale is itself a viable knowledge store, but at the cost of inexplicable knowledge distribution, hallucinated answers when unsure, and zero ability to inspect or update what the model knows."
topics:
  - parametric-memory
  - closed-book-qa
  - knowledge-internalization
  - language-models
  - t5
  - scaling
  - salient-span-masking
  - knowledge-update
tags:
  - paper
  - foundational
  - closed-book-qa
  - parametric-knowledge
  - memory-architecture
  - google-research
entities:
  - roberts-adam
  - raffel-colin
  - shazeer-noam
  - google-research
related_digests:
  - guu-2020-realm
  - lewis-2020-rag-knowledge-nlp
  - brown-2020-gpt3-few-shot
  - karpukhin-2020-dense-passage-retrieval
  - borgeaud-2021-retro
  - du-2025-rethinking-memory
citations:
  - title: "Learning to retrieve reasoning paths over Wikipedia graph for question answering"
    authors: ["Akari Asai", "Kazuma Hashimoto", "Hannaneh Hajishirzi", "Richard Socher", "Caiming Xiong"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1911.10470"
  - title: "Semantic parsing on freebase from question-answer pairs"
    authors: ["Jonathan Berant", "Andrew Chou", "Roy Frostig", "Percy Liang"]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Freebase: a collaboratively created graph database for structuring human knowledge"
    authors: ["Kurt Bollacker", "Colin Evans", "Praveen Paritosh", "Tim Sturge", "Jamie Taylor"]
    year: 2008
    venue: "ACM SIGMOD"
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
  - title: "BoolQ: Exploring the surprising difficulty of natural yes/no questions"
    authors: ["Christopher Clark", "Kenton Lee", "Ming-Wei Chang", "Tom Kwiatkowski", "Michael Collins", "Kristina Toutanova"]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: "1905.10044"
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
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs"
    authors: ["Dheeru Dua", "Yizhong Wang", "Pradeep Dasigi", "Gabriel Stanovsky", "Sameer Singh", "Matt Gardner"]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: "1903.00161"
  - title: "Entities as experts: Sparse memory access with entity supervision"
    authors: ["Thibault Févry", "Livio Baldini Soares", "Nicholas FitzGerald", "Eunsol Choi", "Tom Kwiatkowski"]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "2004.07202"
  - title: "REALM: Retrieval-augmented language model pre-training"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "Panupong Pasupat", "Ming-Wei Chang"]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "2002.08909"
  - title: "Universal language model fine-tuning for text classification (ULMFiT)"
    authors: ["Jeremy Howard", "Sebastian Ruder"]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1801.06146"
  - title: "How can we know what language models know?"
    authors: ["Zhengbao Jiang", "Frank F. Xu", "Jun Araki", "Graham Neubig"]
    year: 2019
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: "1911.12543"
  - title: "TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension"
    authors: ["Mandar Joshi", "Eunsol Choi", "Daniel S. Weld", "Luke Zettlemoyer"]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1705.03551"
  - title: "Dense Passage Retrieval for Open-Domain Question Answering"
    authors: ["Vladimir Karpukhin", "Barlas Oğuz", "Sewon Min", "Ledell Wu", "Sergey Edunov", "Danqi Chen", "Wen-tau Yih"]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "2004.04906"
  - title: "Looking beyond the surface: A challenge set for reading comprehension over multiple sentences (MultiRC)"
    authors: ["Daniel Khashabi", "Snigdha Chaturvedi", "Michael Roth", "Shyam Upadhyay", "Dan Roth"]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Natural questions: a benchmark for question answering research"
    authors: ["Tom Kwiatkowski", "Jennimaria Palomaki", "Olivia Redfield", "Michael Collins", "Ankur Parikh", "Chris Alberti", "Danielle Epstein", "Illia Polosukhin", "Jacob Devlin", "Kenton Lee", "et al."]
    year: 2019
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "ALBERT: A lite BERT for self-supervised learning of language representations"
    authors: ["Zhenzhong Lan", "Mingda Chen", "Sebastian Goodman", "Kevin Gimpel", "Piyush Sharma", "Radu Soricut"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1909.11942"
  - title: "Latent retrieval for weakly supervised open domain question answering (ORQA)"
    authors: ["Kenton Lee", "Ming-Wei Chang", "Kristina Toutanova"]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1906.00300"
  - title: "Learning cross-context entity representations from text (RELIC)"
    authors: ["Jeffrey Ling", "Nicholas FitzGerald", "Zifei Shan", "Livio Baldini Soares", "Thibault Févry", "David Weiss", "Tom Kwiatkowski"]
    year: 2020
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2001.03765"
  - title: "RoBERTa: A robustly optimized BERT pretraining approach"
    authors: ["Yinhan Liu", "Myle Ott", "Naman Goyal", "Jingfei Du", "Mandar Joshi", "Danqi Chen", "Omer Levy", "Mike Lewis", "Luke Zettlemoyer", "Veselin Stoyanov"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1907.11692"
  - title: "Can a suit of armor conduct electricity? a new dataset for open book question answering (OpenBookQA)"
    authors: ["Todor Mihaylov", "Peter Clark", "Tushar Khot", "Ashish Sabharwal"]
    year: 2018
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "A discrete hard EM approach for weakly supervised question answering"
    authors: ["Sewon Min", "Danqi Chen", "Hannaneh Hajishirzi", "Luke Zettlemoyer"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1909.04849"
  - title: "Knowledge guided text retrieval and reading for open domain question answering"
    authors: ["Sewon Min", "Danqi Chen", "Luke Zettlemoyer", "Hannaneh Hajishirzi"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1911.03868"
  - title: "Frustratingly easy natural question answering"
    authors: ["Lin Pan", "Rishav Chakravarti", "Anthony Ferritto", "Michael Glass", "Alfio Gliozzo", "Salim Roukos", "Radu Florian", "Avirup Sil"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1909.05286"
  - title: "Deep contextualized word representations (ELMo)"
    authors: ["Matthew E. Peters", "Mark Neumann", "Mohit Iyyer", "Matt Gardner", "Christopher Clark", "Kenton Lee", "Luke Zettlemoyer"]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: "1802.05365"
  - title: "Language models as knowledge bases?"
    authors: ["Fabio Petroni", "Tim Rocktäschel", "Patrick Lewis", "Anton Bakhtin", "Yuxiang Wu", "Alexander H. Miller", "Sebastian Riedel"]
    year: 2019
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "1909.01066"
  - title: "Open-domain question-answering"
    authors: ["John Prager"]
    year: 2006
    venue: "Foundations and Trends in Information Retrieval"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving language understanding by generative pre-training (GPT-1)"
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
    arxiv_id: "1606.05250"
  - title: "Adafactor: Adaptive learning rates with sublinear memory cost"
    authors: ["Noam Shazeer", "Mitchell Stern"]
    year: 2018
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: "1804.04235"
  - title: "oLMpics — on what language model pre-training captures"
    authors: ["Alon Talmor", "Yanai Elazar", "Yoav Goldberg", "Jonathan Berant"]
    year: 2019
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: "1912.13283"
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "Jakob Uszkoreit", "Llion Jones", "Aidan N. Gomez", "Łukasz Kaiser", "Illia Polosukhin"]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "CCNet: Extracting high quality monolingual datasets from web crawl data"
    authors: ["Guillaume Wenzek", "Marie-Anne Lachaux", "Alexis Conneau", "Vishrav Chaudhary", "Francisco Guzman", "Armand Joulin", "Edouard Grave"]
    year: 2019
    venue: "LREC"
    doi: null
    url: null
    arxiv_id: "1911.00359"
  - title: "XLNet: Generalized autoregressive pretraining for language understanding"
    authors: ["Zhilin Yang", "Zihang Dai", "Yiming Yang", "Jaime Carbonell", "Ruslan Salakhutdinov", "Quoc V. Le"]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "1906.08237"
  - title: "ReCoRD: Bridging the gap between human and machine commonsense reading comprehension"
    authors: ["Sheng Zhang", "Xiaodong Liu", "Jingjing Liu", "Jianfeng Gao", "Kevin Duh", "Benjamin Van Durme"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1810.12885"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "T5 pre-trained on span-corruption then fine-tuned closed-book on QA"
  page: 1
  image_path: "figures/roberts-2020-pack-knowledge-fig.png"
---

# How Much Knowledge Can You Pack Into the Parameters of a Language Model?

**Authors:** Adam Roberts, Colin Raffel, Noam Shazeer (Google)
**Published:** Feb 2020 (revised Oct 2020) · [Source](https://arxiv.org/abs/2002.08910)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Take T5 (a text-to-text encoder-decoder pre-trained on C4 with span-corruption). Fine-tune it on Open-domain QA *with no context, no retrieval, no external knowledge* — just `(question → answer)` pairs. They call this "closed-book QA" (the model must have memorised the answer during pre-training). Scale: T5-Base (220M), T5-Large (770M), T5-3B, T5-11B. Add "salient span masking" (SSM): continue pre-training on Wikipedia sentences with named-entity/date spans masked. Result: T5.1.1-XXL + SSM hits **35.2 EM on NaturalQuestions, 42.8 on WebQuestions, 61.6 on TriviaQA** — beating REALM ([[guu-2020-realm]]) on WebQuestions, and competitive on the others, despite zero retrieval at inference. Human evaluation reveals **38% of "wrong" answers are actually false negatives** (phrasing mismatch, incomplete gold annotations, unanswerable questions), suggesting true accuracy on NQ closer to 57.8 EM.

**ENGRAM dimensions: E (Encode, parametric), G (Ground, negative — *no* provenance), A (Aggregate, implicit), M (Maintain, negative — *cannot* update).**

## Key Takeaway

An 11-billion-parameter T5 fine-tuned on question-answer pairs alone — with zero retrieval, zero context, zero external knowledge — reaches 61.6% exact-match on TriviaQA and is competitive with explicit-retrieval systems on Natural Questions, proving that parametric memory at sufficient scale is itself a viable knowledge store, but at the cost of (1) inexplicable knowledge distribution, (2) hallucinated answers when unsure, and (3) zero ability to inspect or update what the model knows.

The paper is the *negative-space twin* of REALM. REALM says "make retrieval differentiable." This says "you don't need retrieval if you have enough parameters." Both are true. The paper's deepest contribution is articulating — explicitly and without flinching — the four downsides of pure parametric memory that REALM-style systems escape: cost (11B+ params), opacity (no provenance), hallucination (no abstain mechanism), and immutability (no update path short of retraining).

## Implications

**For agent memory architectures — the four critical limitations articulated in the Conclusion:**

1. **Inspectability is gone.** "Our model distributes knowledge in its parameters in an inexplicable way." For an agent system, this means if you go pure-parametric, you cannot answer "what does the agent know about X?" except by querying it and trusting the output. There is no list-the-facts operation. The G (Ground) dimension is structurally absent.

2. **Hallucination is mandatory, not accidental.** The model "hallucinates realistic-looking answers when it is unsure." There is no `null` or `I don't know` channel because the decoder is trained to always output an answer. For an agent that must say "I don't have that information yet" — pure parametric is a non-starter without an additional confidence head.

3. **Update is impossible without retraining.** "The maximum-likelihood objective used to train our model provides no guarantees as to whether a model will learn a fact or not. This makes it difficult to ensure that the model obtains specific knowledge over the course of pre-training and prevents us from explicitly updating or removing knowledge from a pre-trained model." This is the M (Maintain) failure: you cannot delete (think GDPR), you cannot correct (think factual error), you cannot version (think "as of 2025-01-01"). Every "update" requires either retraining or a retrieval bolt-on, at which point you're not pure-parametric anymore.

4. **No specificity guarantee.** Even when you feed the model 1 trillion tokens of pre-training data, you have no guarantee any particular fact is in there. The model's knowledge is a stochastic byproduct of the training run. For an agent that needs to know specific things about a specific user/business — pure parametric is fundamentally the wrong tool.

**For the parametric-vs-explicit memory debate (R + E dimensions):**

5. **Scale-up is brutal.** Going from T5-Base (220M) to T5-11B is **50× more params for ~10-15 EM points**. REALM's 330M-param model gets within striking distance of T5-11B+SSM on NQ (40.4 vs 34.8 — REALM actually wins!) and is *30× smaller*. The economics of "more retrieval, less weights" wins on a Pareto basis.

6. **Salient-span masking is a free ~6-8 point bump.** SSM moves T5.1.1-XXL from 32.8 → 35.2 on NQ, 35.6 → 42.8 on WQ, 42.9 → 51.9 on TQA, 52.5 → 61.6 on TQA-test. This is a substantial gain just from changing the pre-training mask strategy to focus on entities + dates. **For any agent system that compresses session content into LLM weights via fine-tuning (rare but happens), the rule is: mask entities and dates, not random tokens.**

7. **In-domain pre-training doesn't help if the base corpus already contains the domain.** They tried continuing T5 pre-training on Wikipedia for the QA tasks (which source from Wikipedia) — *no effect*. C4 already has Wikipedia content. The implication: parametric memory has a "saturation" point; once a piece of knowledge is encoded, more exposure doesn't reinforce it usefully.

8. **Wikipedia-from-scratch is worse than C4-then-Wikipedia.** Pre-training T5 from scratch *only* on Wikipedia (1 trillion tokens) gave dramatically worse closed-book QA results. They suspect Wikipedia is too small (causes overfitting). **For agent memory: a vault of high-quality, domain-specific text is not enough — the model needs broad-distribution pre-training first, then can be sharpened.**

**For Flow-OS-style architectures:**
9. **This paper is the *foil* — the worst-case "what if memory is the model itself" scenario.** Every Flow OS design choice (explicit `experiences/` files, QMD index over markdown, hot-swappable vault, `/learn` extraction) is motivated by the four Conclusion limitations of this paper. If you can articulate why this paper's approach *doesn't* work for your domain, you've articulated half the value-prop for an explicit memory system.

## How to Apply It (method)

**The closed-book QA recipe (negative reference):**

1. Use T5 (encoder-decoder, span-corruption pre-trained).
2. Optionally continue pre-training with **Salient Span Masking** (SSM):
   - Run BERT NER to identify named-entity spans in Wikipedia sentences.
   - Add date-regex matches.
   - Per sentence, mask exactly one such span.
   - Train for 100K additional steps.
3. Fine-tune on `(question, answer)` text pairs with task-specific prefix (`question: <Q> answer:` → predict `<A>`).
4. Optimizer: AdaFactor, constant LR 0.001, 10% dropout (5% for T5.1.1), batch 196,608 tokens.
5. Decode greedily.
6. Train 20K steps but expect plateau after a few hundred. **Do not over-train** — they observed no overfitting but also no improvement.

**The negative-results section is the most useful part for practitioners:**
- Continued Wikipedia pre-training (in-domain) on T5: **no improvement.**
- T5 pre-trained from scratch on Wikipedia alone: **worse.**
- Multitask fine-tuning across all 3 QA tasks: improved NQ by 0.5, *worse* on the others.
- Random sampling of multi-answer targets vs first-answer: **no difference.**

**What translates to agent-memory practice:**

| Closed-book QA learning | Agent memory implication |
|---|---|
| SSM beats random span masking | If you ever fine-tune a model on your vault, mask entities/dates, not random tokens |
| Wikipedia-only pre-train fails | Don't train a "personal LLM" only on your data — start broad, sharpen narrow |
| 11B params for ~60 EM on trivia | Don't bet on parametric memory for facts your user added yesterday |
| Hallucinates when unsure | Always wire an "abstain" path that returns *nothing* on low confidence |
| Cannot inspect or update | Keep the durable knowledge in files, not weights |
| Human eval found 38% false negatives | Don't trust exact-match metrics — agents will be unfairly penalised for valid paraphrases |

**Hyperparameter for reproducibility:** Models released at `https://goo.gle/t5-cbqa`. Human-eval results released for transparency.

## Best Figure

![Figure 1 — T5 pre-trained on span-corruption then fine-tuned closed-book on QA (page 1)](figures/roberts-2020-pack-knowledge-fig.png)

**Why this figure matters for the memory-architect lens:** The figure renders the *entire architecture* of pure-parametric memory in one diagram. Top: pre-training — sentences with `<M>`-masked spans drop into "T5", which learns to fill them. The "model" *is* the memory; the C4 sentences fade into the weights. Bottom: fine-tuning — a bare question goes in, an answer comes out, with a thought-bubble showing T5 *remembering* the relevant fact ("President Franklin D. Roosevelt was born in January 1882"). No retrieval. No context. No documents. The thought bubble is the entire "memory" component.

For ENGRAM: this figure is the cleanest possible illustration of **E without G**. There is encoding (span corruption acts as compression of the corpus into weights), but there is no grounding (the answer has no source, only a probability distribution). This is the negative case that motivates every grounded-memory architecture.

**Figure Page: 1**

## What Experts Overlook

1. **The human evaluation correction is huge.** 38% of T5's "wrong" answers on NaturalQuestions are *not actually wrong* — they're paraphrase mismatches, incomplete gold annotations, or genuinely unanswerable. **The true accuracy of T5-11B+SSM on NQ is ~57.8 EM, not 35.2.** This means **every paper comparing to this benchmark with an unaudited gold-set is systematically biased against generation-based answers and toward extraction-based ones.** For agent eval design: do not use raw EM. Either fuzz-match, LLM-judge, or hand-audit the false negatives.

2. **C4 contained the answer set, and that mattered.** Negative experiment B: pre-training *additionally* on Wikipedia gave no improvement, because C4 already had Wikipedia in it. **The implication:** parametric-memory systems are bounded by the *coverage* of the pre-training corpus, not the *depth*. If your domain isn't in C4-style web data, no amount of fine-tuning on your local docs will compete with explicit retrieval over those docs.

3. **The Inverse-T5 result everyone ignores.** Pre-training T5 from scratch only on Wikipedia (1 trillion tokens) is **dramatically worse** than starting from C4-pre-trained then optionally adapting. **Implication for any "personal LLM" pitch:** training a custom small model on your data alone will not work; the model needs broad-distribution language priors first. This is also why MemGPT / mem0 / Flow OS-style "external memory + general LLM" wins over "fine-tune the model on user data."

4. **SSM is the most replicable architectural trick in this paper.** SSM contributed roughly the same delta (5-9 EM points) at every scale. It's a single change to the data preprocessing pipeline — no architecture change, no extra params. **For any memory system that fine-tunes anything, salient-span masking is the cheapest possible quality knob.** The infrastructure: BERT-NER + date regex. Implementation cost: ~50 LOC.

5. **The "memorisation" framing is a metaphor that's doing real work.** The closed-book exam metaphor (intro section) is not just rhetoric — it specifies the *cognitive model* of the system: the student studies (pre-training), takes the test (inference), and can use only what's in their head. This frames the failure modes correctly: a closed-book student forgets specific facts, mis-attributes sources, and hallucinates plausible-sounding wrong answers. **An agent built on pure-parametric memory will have exactly these failure modes — they're not engineering bugs, they're properties of the architecture.** The choice to memorise vs retrieve is the choice to have these failure modes vs different ones.

6. **The "no negative result was a complete failure" pattern.** The paper's Appendix B is unusually candid: continued Wikipedia pre-training, Wikipedia-from-scratch, multitask, answer-sampling — they tried four "obvious next things" and only multitask gave a 0.5-point bump on one dataset. **The lesson: when scaling parametric memory, intuitive interventions often don't help.** This contrasts sharply with retrieval-based architectures where small interventions (better chunking, query rewriting, reranking) consistently produce measurable gains. **Parametric memory has fewer levers; explicit memory has many.** For an agent-OS, that's a profound architectural reason to bias toward explicit.

## Extracted Prompts

This paper has minimal prompting — closed-book QA is fine-tuned, not prompted — but two are worth lifting:

1. **Task-prefix prompt for closed-book QA fine-tuning:**
   ```
   question: <Q> answer:
   ```
   The model is trained to generate the literal answer text after this prefix. Worth noting: T5 uses task-prefixes generally; this is just the QA-task version.

2. **Multi-answer Natural Questions format (Appendix A):**
   ```
   answer: <A1> answer: <A2> answer: <A3> ...
   ```
   When a question has multiple correct answers, the model is trained to output all of them delimited by `answer:`. Post-processing splits them. **Useful for agents that need to enumerate possibilities, not just pick the top one.**

3. **Salient-span masking trigger (training-data construction, not a prompt per se):**
   Identify named entities (CoNLL-2003 NER tagger) + dates (regex). Mask exactly one such span per sentence. Train the model to fill it.

## Citations

37 citations. Highlights for the memory-architect lens:
- **The retrieval-based foils REALM is being compared to**: REALM ([[guu-2020-realm]]), DPR ([[karpukhin-2020-dense-passage-retrieval]]), ORQA (Lee 2019), DrQA (Chen 2017), GraphRetriever (Min 2019b), PathRetriever (Asai 2019).
- **The parametric-knowledge probes that inspired the paper**: Petroni 2019 ("Language models as knowledge bases?"), Jiang 2019 ("How can we know what language models know?"), Talmor 2019 ("oLMpics").
- **The text-to-text framework**: Raffel 2019 (T5).
- **Pre-training backbones**: BERT ([[devlin-2018-bert]]), RoBERTa, XLNet, ALBERT.
- **Concurrent entity-as-memory work**: Févry 2020 (Entities as Experts), Ling 2020 (RELIC). These are the spiritual cousins — explicit *entity memory* embedded in the model.

Full structured list in frontmatter `citations[]`.

## Related Digests

- [[guu-2020-realm]] — REALM: the canonical retrieval-augmented counterpoint to this paper (same lab, same year, opposite design choice)
- [[lewis-2020-rag-knowledge-nlp]] — RAG: the seq2seq follower that combines DPR retriever with BART generator
- [[brown-2020-gpt3-few-shot]] — GPT-3: scaled this paper's thesis to 175B and showed few-shot prompting can substitute for fine-tuning
- [[karpukhin-2020-dense-passage-retrieval]] — DPR: the dense retriever the field standardised on
- [[borgeaud-2021-retro]] — RETRO: the scaled retrieval-augmented LM that proved retrieval wins at scale too
- [[du-2025-rethinking-memory]] — Rethinking Memory: re-examines parametric vs explicit memory tradeoffs five years on

## Reviewer Notes

**Severity: Clean.**

Cross-checked against the paper text:
- Parameter counts verified: T5-Base 220M (paper says 220 million — correct), Large 770M, 3B (3 billion), 11B (11 billion). T5.1.1 variants Base, Large, XL, XXL — all correct.
- Table 1 scores verified: T5-11B+SSM 34.8 NQ / 40.8 WQ / 51.0 TQA-dev / 60.5 TQA-test; T5.1.1-XXL+SSM 35.2 NQ / 42.8 WQ / 51.9 TQA-dev / 61.6 TQA-test. All correct.
- REALM comparison in table verified (Guu et al. 2020: 40.4 NQ, 40.7 WQ) — so on NQ, REALM-330M actually *beats* T5-11B (32.6) and even T5-11B+SSM (34.8). On WQ, T5.1.1-XXL+SSM (42.8) beats REALM (40.7). This is a subtle and important detail correctly preserved in the digest.
- Human eval breakdown verified: 62% true negative, 13.3% phrasing mismatch, 13.3% incomplete annotation, 11.3% unanswerable. Sample size 150. Recomputed accuracy 57.8 EM verified.
- Optimizer + LR: AdaFactor, constant 0.001, 10% dropout (5% for T5.1.1), batch 196,608 tokens — verified.
- Pre-training amounts (1 trillion tokens, 100K SSM additional steps) verified.
- Quote from Conclusion: "Our model distributes knowledge in its parameters in an inexplicable way and hallucinates realistic-looking answers when it is unsure" — verified verbatim.

No fabrication detected. Negative results from Appendix B accurately summarised.
