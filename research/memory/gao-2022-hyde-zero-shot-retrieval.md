---
corpus: agentic-memory
kind: paper-digest
slug: gao-2022-hyde-zero-shot-retrieval
title: "Precise Zero-Shot Dense Retrieval without Relevance Labels"
authors:
  - "Luyu Gao"
  - "Xueguang Ma"
  - "Jimmy Lin"
  - "Jamie Callan"
year: 2022
publication_date: "2022-12"
venue: "arXiv preprint (later ACL 2023)"
source_url: "https://arxiv.org/abs/2212.10496"
doi: null
arxiv_id: "2212.10496"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Stop trying to embed the query at all — have an instruction-tuned LLM hallucinate a hypothetical answer document, embed that, and the encoder's dense bottleneck silently launders the hallucinations out, beating the best fully-unsupervised retriever Contriever (44.5 → 61.3 nDCG@10 on TREC-DL19) and matching fine-tuned in-domain models without ever touching a relevance label."
topics:
  - dense-retrieval
  - zero-shot-retrieval
  - query-expansion
  - hypothetical-document-embeddings
  - llm-augmented-retrieval
  - hallucination-tolerance
  - retrieval-architecture
  - multilingual-retrieval
tags:
  - paper
  - retrieval
  - hyde
  - instructgpt
  - contriever
  - beir
  - trec-dl
  - mr-tydi
  - rag
  - memory-architecture
entities:
  - gao-luyu
  - ma-xueguang
  - lin-jimmy
  - callan-jamie
related_digests:
  - adler-2026-storage-not-memory
  - chhikara-2025-mem0
  - latimer-2025-hindsight-memory
  - packer-2023-memgpt-os
citations:
  - title: "Task-aware retrieval with instructions"
    authors: ["Akari Asai", "Timo Schick", "Patrick Lewis", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "MS MARCO: A human generated machine reading comprehension dataset"
    authors: ["Payal Bajaj", "Daniel Campos", "Nick Craswell", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Autoregressive search engines: Generating substrings as document identifiers"
    authors: ["Michele Bevilacqua", "Giuseppe Ottaviano", "Patrick Lewis", "et al."]
    year: 2022
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2204.10628"
  - title: "Language models are few-shot learners"
    authors: ["Tom B. Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Evaluating large language models trained on code"
    authors: ["Mark Chen", "Jerry Tworek", "Heewoo Jun", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "PaLM: Scaling language modeling with pathways"
    authors: ["Aakanksha Chowdhery", "Sharan Narang", "Jacob Devlin", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Unsupervised cross-lingual representation learning at scale"
    authors: ["Alexis Conneau", "Kartikay Khandelwal", "Naman Goyal", "et al."]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Overview of the TREC 2019 deep learning track"
    authors: ["Nick Craswell", "Bhaskar Mitra", "Emine Yilmaz", "et al."]
    year: 2020
    venue: "TREC"
    doi: null
    url: null
    arxiv_id: null
  - title: "Overview of the TREC 2020 deep learning track"
    authors: ["Nick Craswell", "Bhaskar Mitra", "Emine Yilmaz", "et al."]
    year: 2020
    venue: "TREC"
    doi: null
    url: null
    arxiv_id: "2003.07820"
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Condenser: A pre-training architecture for dense retrieval"
    authors: ["Luyu Gao", "Jamie Callan"]
    year: 2021
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Unsupervised corpus aware language model pre-training for dense passage retrieval"
    authors: ["Luyu Gao", "Jamie Callan"]
    year: 2022
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "SimCSE: Simple contrastive learning of sentence embeddings"
    authors: ["Tianyu Gao", "Xingcheng Yao", "Danqi Chen"]
    year: 2021
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training compute-optimal large language models"
    authors: ["Jordan Hoffmann", "Sebastian Borgeaud", "Arthur Mensch", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficiently teaching an effective dense retriever with balanced topic aware sampling"
    authors: ["Sebastian Hofstätter", "Sheng-Chieh Lin", "Jheng-Hong Yang", "et al."]
    year: 2021
    venue: "SIGIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards unsupervised dense information retrieval with contrastive learning"
    authors: ["Gautier Izacard", "Mathilde Caron", "Lucas Hosseini", "et al."]
    year: 2021
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2112.09118"
  - title: "Billion-scale similarity search with GPUs"
    authors: ["Jeff Johnson", "Matthijs Douze", "Hervé Jégou"]
    year: 2017
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1702.08734"
  - title: "Dense passage retrieval for open-domain question answering"
    authors: ["Vladimir Karpukhin", "Barlas Oguz", "Sewon Min", "et al."]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generative multi-hop retrieval"
    authors: ["Hyunji Lee", "Sohee Yang", "Hanseok Oh", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Latent retrieval for weakly supervised open domain question answering"
    authors: ["Kenton Lee", "Ming-Wei Chang", "Kristina Toutanova"]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Pyserini: A Python toolkit for reproducible information retrieval research with sparse and dense representations"
    authors: ["Jimmy Lin", "Xueguang Ma", "Sheng-Chieh Lin", "et al."]
    year: 2021
    venue: "SIGIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "In-batch negatives for knowledge distillation with tightly-coupled teachers for dense retrieval"
    authors: ["Sheng-Chieh Lin", "Jheng-Hong Yang", "Jimmy Lin"]
    year: 2021
    venue: "RepL4NLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "RetroMAE: Pre-training retrieval-oriented transformers via masked auto-encoder"
    authors: ["Zheng Liu", "Yingxia Shao"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2205.12035"
  - title: "Less is more: Pre-train a strong Siamese encoder for dense text retrieval using a weak decoder"
    authors: ["Shuqi Lu", "Di He", "Chenyan Xiong", "et al."]
    year: 2021
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Rethinking search: Making domain experts out of dilettantes"
    authors: ["Donald Metzler", "Yi Tay", "Dara Bahri", "et al."]
    year: 2021
    venue: "SIGIR Forum"
    doi: null
    url: null
    arxiv_id: null
  - title: "MetaICL: Learning to learn in context"
    authors: ["Sewon Min", "Mike Lewis", "Luke Zettlemoyer", "et al."]
    year: 2022
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training language models to follow instructions with human feedback"
    authors: ["Long Ouyang", "Jeff Wu", "Xu Jiang", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "RocketQA: An optimized training approach to dense passage retrieval for open-domain question answering"
    authors: ["Yingqi Qu", "Yuchen Ding", "Jing Liu", "et al."]
    year: 2021
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Scaling language models: Methods, analysis & insights from training Gopher"
    authors: ["Jack W. Rae", "Sebastian Borgeaud", "Trevor Cai", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving passage retrieval with zero-shot question generation"
    authors: ["Devendra Singh Sachan", "Mike Lewis", "Mandar Joshi", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multitask prompted training enables zero-shot task generalization"
    authors: ["Victor Sanh", "Albert Webson", "Colin Raffel", "et al."]
    year: 2022
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Transformer memory as a differentiable search index"
    authors: ["Yi Tay", "Vinh Q. Tran", "Mostafa Dehghani", "et al."]
    year: 2022
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2202.06991"
  - title: "BEIR: A heterogenous benchmark for zero-shot evaluation of information retrieval models"
    authors: ["Nandan Thakur", "Nils Reimers", "Andreas Rücklé", "et al."]
    year: 2021
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2104.08663"
  - title: "LaMDA: Language models for dialog applications"
    authors: ["Romal Thoppilan", "Daniel De Freitas", "Jamie Hall", "et al."]
    year: 2022
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "2201.08239"
  - title: "GPL: Generative pseudo labeling for unsupervised domain adaptation of dense retrieval"
    authors: ["Kexin Wang", "Nandan Thakur", "Nils Reimers", "et al."]
    year: 2022
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Finetuned language models are zero-shot learners"
    authors: ["Jason Wei", "Maarten Bosma", "Vincent Y. Zhao", "et al."]
    year: 2022
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Approximate nearest neighbor negative contrastive learning for dense text retrieval"
    authors: ["Lee Xiong", "Chenyan Xiong", "Ye Li", "et al."]
    year: 2021
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "COCO-DR: Combating distribution shifts in zero-shot dense retrieval with contrastive and distributionally robust learning"
    authors: ["Yue Yu", "Chenyan Xiong", "Si Sun", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mr. TyDi: A multi-lingual benchmark for dense retrieval"
    authors: ["Xinyu Zhang", "Xueguang Ma", "Peng Shi", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2108.08787"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "An illustration of the HyDE model"
  page: 2
  image_path: "figures/gao-2022-hyde-zero-shot-retrieval-fig.png"
---

# Precise Zero-Shot Dense Retrieval without Relevance Labels

**Authors:** Luyu Gao, Xueguang Ma, Jimmy Lin, Jamie Callan
**Published:** 2022-12 · [Source](https://arxiv.org/abs/2212.10496)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

HyDE (Hypothetical Document Embeddings) is a two-stage zero-shot dense retrieval recipe with no fine-tuning anywhere in the pipeline: at query time, InstructGPT (text-davinci-003) is prompted with a task-specific instruction such as "write a passage to answer the question…" and samples N=8 candidate passages at temperature 0.7; each is encoded by the off-the-shelf unsupervised Contriever (or mContriever for non-English), and the mean of those vectors plus the encoded original query is used as the query embedding against the corpus index. The encoder's dense bottleneck is the load-bearing trick — it filters out the hypothetical doc's fabricated details and grounds the vector to actual corpus neighbours. On TREC DL19, HyDE lifts nDCG@10 from Contriever's 44.5 to 61.3 (essentially matching the supervised ContrieverFT at 62.1) and recall@1k from 74.6 to 88.0; on TREC DL20, nDCG@10 goes 42.1 → 57.9. Across six BEIR low-resource tasks, HyDE beats unsupervised Contriever everywhere and BM25 on five of six (TREC-Covid being the exception, by 0.2). On Mr.TyDi multilingual retrieval, it improves Swahili (38.3 → 41.7 MRR@100), Korean (22.3 → 30.6), Japanese (19.5 → 30.7), and Bengali (35.3 → 41.3). Scaling the generator matters: Flan-T5-11B < Cohere-52B < InstructGPT-175B (48.9 / 53.8 / 61.3 nDCG@10 on DL19). Most useful takeaway: at the cold-start of any new retrieval corpus where no click logs or labels exist, HyDE buys you supervised-tier quality without a single labelled pair, and you can incrementally swap it out as real supervision arrives.

## Key Takeaway

The cleanest way to retrieve is to stop encoding the query at all. Embedding short, vague queries against long, dense documents is exactly the mismatch dense retrievers can't learn without supervision — so HyDE hallucinates a document that looks like the right kind of answer, embeds *that*, and lets the contrastive encoder's lossy bottleneck wash out the fabricated details. A factually wrong but topically right passage is a better query vector than a factually right but topically thin question. Numerical relevance modelling, it turns out, may just be a statistical artefact of language understanding that a strong-enough generative model can sidestep entirely.

## Implications

- **ENGRAM — Retrieve: use a generated-document pivot whenever your queries are short and your corpus is unsupervised.** HyDE's 38% relative nDCG@10 lift on TREC-DL19 over raw Contriever, without any training, says that for any new memory store before you have labels, the right query-side transformation is "generate the answer, then search," not "embed the question directly." This is a drop-in replacement for naive embedding-of-query in any Flow OS memory store that hasn't yet accumulated query/feedback pairs.
- **ENGRAM — Encode × Retrieve coupling: the encoder's dense bottleneck is doing trust-laundering for you.** Section 3.2 and the conclusion make explicit that the "extra (hallucinated) details are filtered out from the embedding" — meaning a small, lossy encoder is a *feature*, not a limitation, because it forces grounding to real corpus neighbours. Larger more-faithful encoders may actually hurt HyDE by preserving the hallucination signal.
- **ENGRAM — Ground: don't fight hallucination at the generator, exploit it at the geometry.** The paper inverts the usual stance toward LLM fabrication — instead of constraining the generator (chain-of-thought, RAG-with-citations, etc.) it lets it freely confabulate and uses vector arithmetic plus a weak encoder as the grounding step. Memory architects should treat the embedding bottleneck as an explicit provenance filter, not just a similarity function.
- **ENGRAM — Retrieve: averaging N=8 sampled completions plus the raw query (Equation 8) is the reliability mechanism.** A single hallucinated doc is too noisy; the mean over 8 samples + the encoded query (so N+1 = 9 terms) is what makes the query vector stable. This is essentially Monte-Carlo retrieval, and any production HyDE-style system should not skimp on the sample count.
- **ENGRAM — Aggregate: HyDE is meant to be retired, not perpetual.** The conclusion explicitly frames HyDE as a cold-start tool: "As the search log grows, a supervised dense retriever can be gradually rolled out… less common and emerging [queries] going to the HyDE backend." Build your memory layer to *route* — fine-tuned retriever for head queries, HyDE for tail and new-corpus queries.
- **ENGRAM — Encode: instruction-following is the actual prerequisite — base LLMs won't do it.** The recipe depends on instruction-tuned models (InstructGPT, FLAN-T5, Cohere instruct), not raw base LLMs, because the relevance pattern is communicated *through the instruction* ("write a scientific paper passage…", "write a counter-argument…"). Per-corpus prompt engineering (the eight Appendix A.1 templates) is part of the architecture, not an optimisation.
- **ENGRAM — Network: this is the cheapest possible multilingual memory expansion.** The same architecture lifts Japanese MRR@100 from 19.5 to 30.7 with zero language-specific labels — for any non-English Flow OS deployment, HyDE is the unsupervised baseline to beat before considering language-specific fine-tuning.
- **ENGRAM — Retrieve × Maintain interaction: where the LLM is weak, the trick collapses.** Multilingual lift is smaller than English (HyDE underperforms supervised mContrieverFT by 9.5 MRR@100 on Swahili) because both the generator and the encoder are under-trained on those languages. Generator/encoder co-fragility is a real maintenance burden — monitor per-language quality, don't assume uniform performance.

## How to Apply It (method)

**Scenario:** You're standing up a new memory tier in a Flow OS deployment — say, a private corpus of client meeting transcripts and internal SOPs for a customer's first month on the platform. You have ~50k documents and zero query/feedback data. The naive options are (a) BM25, which is brittle on paraphrased questions, or (b) a generic dense retriever like Contriever, which routinely underperforms BM25 in zero-shot settings. You want supervised-tier retrieval quality before you have a single label.

**Steps:**

1. **Pick your two backbone models and freeze them**: An instruction-tuned generator (GPT-4o / Claude Sonnet / open Llama-3-Instruct) and an unsupervised contrastive encoder (Contriever for English, mContriever for multilingual, or a modern equivalent like E5 / BGE-base). Neither is fine-tuned at any point.

2. **Index the corpus once with the encoder**: For every document d in your corpus, compute `v_d = enc(d)` and store in a vector index (FAISS, sqlite-vec, pgvector — anything supporting inner-product MIPS). This is the only one-time cost; HyDE adds nothing to the index build.

3. **Author a task-specific instruction template** that matches your corpus's *answer document type*. The paper shows that the instruction encodes the relevance pattern, and they use a different template per corpus:

   ```
   Please write a [DOMAIN] passage to [TASK] the [INPUT_TYPE]
   [INPUT_LABEL]: [USER_QUERY]
   Passage:
   ```

   Examples from the paper: "Please write a passage to answer the question" (web search), "Please write a scientific paper passage to support/refute the claim" (SciFact), "Please write a counter argument for the passage" (Arguana), "Please write a financial article passage to answer the question" (FiQA). For meeting-transcript retrieval the instruction might be: "Please write a meeting summary paragraph that answers the question. Question: [Q]. Summary:".

4. **At query time, sample N=8 hypothetical documents** from the generator with temperature 0.7 (the paper's setting):

   ```python
   hypothetical_docs = [
       generator(instruction_template.format(query=q), temperature=0.7)
       for _ in range(8)
   ]
   ```

5. **Encode and average** — this is Equation 8 from the paper, the (N+1)-term form that also includes the raw query embedding:

   ```python
   v_q_hat = mean([enc(d) for d in hypothetical_docs] + [enc(q)])
   ```

6. **Retrieve by inner product** against the corpus index: `top_k = mips_index.search(v_q_hat, k)`. No reranker required for the baseline result, though one can be layered on top.

7. **Route, don't replace, as supervision arrives**: log every served query and its eventually-clicked / human-confirmed result. Once you have ~10k labelled pairs, fine-tune a supervised encoder for head queries and keep HyDE as the fallback for tail / new-vocabulary queries (per the paper's conclusion).

8. **Per-corpus quality monitor**: track nDCG@10 against a small held-out human-judged sample (the paper uses ~50 judged queries per BEIR task). If HyDE underperforms BM25 by more than the paper's biggest gap (~0.2 nDCG on TREC-Covid), the issue is almost always a weak instruction — rewrite the template to better match the answer document genre.

**Expected outcome:** A zero-label retrieval pipeline that ships roughly at parity with a supervised in-domain encoder (within a few nDCG@10 points on English, larger gaps on low-resource languages), at the cost of one LLM call per query (parallelisable across the 8 samples). Most importantly, you get an *upgrade path* — the same vector index works for the supervised retriever you'll train later, so HyDE is throwaway scaffolding, not lock-in.

## Best Figure

![Figure 1 — An illustration of the HyDE model (page 2)](figures/gao-2022-hyde-zero-shot-retrieval-fig.png)

Image Candidates:
Figure 1 (p. 2): Shows the entire HyDE pipeline in one view across three query languages and three task types — the clearest single-image summary of the paper's architecture.
Table 1 (p. 4): Web-search head-to-head where HyDE beats every relevance-free baseline and matches ContrieverFT on TREC DL19, the cleanest quantitative payoff.
Table 4 (p. 6): Instruction-LM scaling sweep (Flan-T5 11B → Cohere 52B → GPT 175B) with both unsupervised and supervised encoders, the most interesting analysis result.

Best Image:
Figure Name: Figure 1: "An illustration of the HyDE model"
Figure Page: 2
Slide Caption: HyDE pivots queries through hypothetical documents generated by an instruction-tuned LLM, then retrieves real documents via an unsupervised contrastive encoder.
Description: Figure 1 shows three different instruction/query pairs — a wisdom-tooth health question, a COVID-19 mental-health scientific query, and a Korean-language history question — fed to a GPT (InstructGPT) module. GPT produces a hypothetical answer document in the appropriate genre and language. Contriever (or mContriever for non-English) then encodes that hypothetical document into a vector, which is used to retrieve real documents from the corpus. The colour-coded legend distinguishes the four element types: instruction (yellow), query (green), generated document (orange), real document (blue). The figure compactly demonstrates that the same architecture handles different tasks, domains, and languages without changing the underlying models — only the instruction text varies.

## What Experts Overlook

The load-bearing detail is *not* the LLM hallucinating a document — it's the **deliberate use of a weak, lossy encoder as a fabrication filter**. Section 3.2 says it plainly: "the encoder function f serves as a lossy compressor that outputs dense vectors, where the extra details are filtered and left out from the vector. It further grounds the hypothetical vector to the actual corpus and the real documents." Most readers focus on "LLMs can generate fake documents that improve retrieval," but the unsung mechanism is that **a higher-fidelity encoder would actually hurt HyDE**, because it would preserve more of the hallucinated specifics and pull the query vector toward documents that resemble the fabrications rather than the topic. The encoder's compression bottleneck is doing trust-laundering on the generator's output. This is also why the paper makes a point of using the *unsupervised* Contriever rather than ContrieverFT in the headline experiments — ContrieverFT actually generates somewhat worse HyDE results on DL20 (63.2 → 63.5 with GPT-175B, marginal vs unsupervised's much larger lift), because the fine-tuned encoder is already encoding query-document relevance and HyDE's hallucination injection mostly adds noise to it.

**Why it matters:** This inverts the standard memory-architecture intuition that bigger / more-faithful encoders are always better. For memory systems doing query-side LLM expansion (HyDE, multi-query, Step-Back prompting, etc.), the encoder choice becomes a *trust-calibration knob*, not a quality knob. Pair a high-capacity generator with a moderate-capacity encoder, and you're effectively building a noise-rejection circuit; pair a high-capacity generator with a high-capacity encoder, and you're amplifying the generator's hallucinations into the retrieval result. The two halves of the pipeline have to be *jointly* sized.

**Example of good use:** A Flow OS memory tier that uses GPT-4 to write hypothetical answer paragraphs at query time but encodes them with a small, unsupervised embedder (e.g. `bge-small-en`, ~33M params). The smaller embedder's lossy bottleneck dilutes any GPT-4-fabricated entities or dates, while preserving the topical signal — retrieval results stay anchored to actual stored memories rather than drifting toward whatever the LLM invented.

**Example of misapplication:** Pairing HyDE-style query expansion with a very large fine-tuned encoder (e.g. a 7B retrieval-tuned model) and then debugging why retrieval keeps returning documents that match the hallucinated specifics rather than the user's actual intent. The large encoder is faithfully encoding the LLM's confabulation; the system is no longer "hallucinate-and-launder" but "hallucinate-and-amplify." The fix is counter-intuitive: *downgrade* the encoder.

## Extracted Prompts

**Prompt explanation:** Web Search — the canonical HyDE instruction used for TREC DL19 / DL20 and the default open-domain setup.

```
Please write a passage to answer the question
Question: [QUESTION]
Passage:
```

**Prompt explanation:** SciFact — claim-grounded scientific-passage generation for fact verification.

```
Please write a scientific paper passage to support/refute the claim
Claim: [Claim]
Passage:
```

**Prompt explanation:** Arguana — counter-argument generation for argumentative retrieval.

```
Please write a counter argument for the passage
Passage: [PASSAGE]
Counter Argument:
```

**Prompt explanation:** TREC-COVID — scientific-passage generation for biomedical / COVID queries.

```
Please write a scientific paper passage to answer the question
Question: [QUESTION]
Passage:
```

**Prompt explanation:** FiQA — financial-article-style passage generation for finance QA.

```
Please write a financial article passage to answer the question
Question: [QUESTION]
Passage:
```

**Prompt explanation:** DBPedia-Entity — generic answer-passage generation for entity retrieval.

```
Please write a passage to answer the question.
Question: [QUESTION]
Passage:
```

**Prompt explanation:** TREC-NEWS — news-passage generation for topic-based news retrieval.

```
Please write a news passage about the topic.
Topic: [TOPIC]
Passage:
```

**Prompt explanation:** Mr.TyDi — language-specific (Swahili / Korean / Japanese / Bengali) answer-passage generation for multilingual retrieval.

```
Please write a passage in Swahili/Korean/Japanese/Bengali to answer the question in detail.
Question: [QUESTION]
Passage:
```

## Citations

- Asai et al. 2022 — Task-aware retrieval with instructions
- Bajaj et al. 2016 — MS MARCO: A human generated machine reading comprehension dataset
- Bevilacqua et al. 2022 — Autoregressive search engines: Generating substrings as document identifiers
- Brown et al. 2020 — Language models are few-shot learners
- Chen et al. 2021 — Evaluating large language models trained on code
- Chowdhery et al. 2022 — PaLM: Scaling language modeling with pathways
- Conneau et al. 2020 — Unsupervised cross-lingual representation learning at scale
- Craswell et al. 2020a — Overview of the TREC 2019 deep learning track
- Craswell et al. 2020b — Overview of the TREC 2020 deep learning track
- Devlin et al. 2019 — BERT

(Plus 28 more in `citations:` frontmatter — full bibliography preserved for citation-walk.)

## Related Digests

- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall (already cites HyDE; HyDE is the canonical query-side antecedent to Adler's retrieval-centred stance)
- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (Mem0's flat natural-language store is exactly the kind of unsupervised corpus where HyDE-style query expansion shines)
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects (Latimer's "recall" operation is the architectural slot HyDE plugs into; the two are complementary across the lifecycle)
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems (MemGPT pages data via function calls; HyDE is the search primitive those calls could invoke against the recall tier)

## Reviewer Notes

**Overall severity:** Clean

Every claim above was cross-checked against the paper text and tables. Numbers cited (Contriever 44.5 → HyDE 61.3 on DL19 nDCG@10; recall@1k 74.6 → 88.0; DL20 nDCG@10 42.1 → 57.9; Mr.TyDi MRR@100 figures for sw/ko/ja/bn; the instruction-LM sweep 48.9 / 53.8 / 61.3 for Flan-T5 11B / Cohere 52B / GPT 175B on DL19) are exact matches to Tables 1, 3, and 4. The N=8 sample count and 0.7 temperature are stated in §4.1 "Implementation". The eight instruction templates are reproduced verbatim from Appendix A.1. The interpretation of the encoder bottleneck as a hallucination filter is the paper's own framing (Abstract + §3.2 + §6). The TREC-Covid 0.2 nDCG gap behind BM25 is from Table 2 (HyDE 59.3 vs BM25 59.5).

One minor framing nuance to flag for future readers: the paper calls HyDE "unsupervised" but explicitly acknowledges that supervision *does* enter through the instruction-tuning of the LLM (§3 and the Asai-et-al. comparison in Related Works). The digest preserves this nuance ("no relevance labels" rather than "zero supervision"). Also: the venue line is rendered as "arXiv preprint (later ACL 2023)" — the v1 PDF used here is the December 2022 arXiv submission; the work was subsequently published at ACL 2023, which is not stated in the v1 PDF itself but is well-established external metadata.
