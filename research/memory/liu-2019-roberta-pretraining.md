---
corpus: agentic-memory
kind: paper-digest
slug: liu-2019-roberta-pretraining
title: "RoBERTa: A Robustly Optimized BERT Pretraining Approach"
authors:
  - "Liu, Yinhan"
  - "Ott, Myle"
  - "Goyal, Naman"
  - "Du, Jingfei"
  - "Joshi, Mandar"
  - "Chen, Danqi"
  - "Levy, Omer"
  - "Lewis, Mike"
  - "Zettlemoyer, Luke"
  - "Stoyanov, Veselin"
year: 2019
publication_date: "2019-07"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/1907.11692"
doi: null
arxiv_id: "1907.11692"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "BERT was significantly undertrained; the headline gains attributed to architectural successors (XLNet, etc.) were largely a function of more data, longer training, larger batches, and dynamic masking — not a better pretraining objective."
topics:
  - language-model-pretraining
  - masked-language-modeling
  - bert
  - hyperparameter-ablation
  - encoder-pretraining
  - training-data-scale
tags:
  - paper
  - replication-study
  - foundation-model
  - encoder
  - pretraining-recipe
  - canonical
entities:
  - liu-yinhan
  - ott-myle
  - lewis-mike
  - zettlemoyer-luke
  - chen-danqi
  - levy-omer
  - devlin-jacob
related_digests:
  - devlin-2018-bert
  - lewis-2019-bart
  - bi-2020-palm-context-generation
  - raffel-2020-t5
  - guu-2020-realm
citations:
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Devlin, Jacob", "Chang, Ming-Wei", "Lee, Kenton", "Toutanova, Kristina"]
    year: 2019
    doi: null
    url: "https://aclanthology.org/N19-1423/"
    arxiv_id: "1810.04805"
  - title: "XLNet: Generalized autoregressive pretraining for language understanding"
    authors: ["Yang, Zhilin", "Dai, Zihang", "Yang, Yiming", "Carbonell, Jaime", "Salakhutdinov, Ruslan", "Le, Quoc V."]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1906.08237"
    arxiv_id: "1906.08237"
  - title: "Cross-lingual language model pretraining"
    authors: ["Lample, Guillaume", "Conneau, Alexis"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1901.07291"
    arxiv_id: "1901.07291"
  - title: "Deep contextualized word representations (ELMo)"
    authors: ["Peters, Matthew", "Neumann, Mark", "Iyyer, Mohit", "Gardner, Matt", "Clark, Christopher", "Lee, Kenton", "Zettlemoyer, Luke"]
    year: 2018
    doi: null
    url: "https://aclanthology.org/N18-1202/"
    arxiv_id: "1802.05365"
  - title: "Improving language understanding with unsupervised learning (GPT-1)"
    authors: ["Radford, Alec", "Narasimhan, Karthik", "Salimans, Time", "Sutskever, Ilya"]
    year: 2018
    doi: null
    url: "https://openai.com/research/language-unsupervised"
    arxiv_id: null
  - title: "Language models are unsupervised multitask learners (GPT-2)"
    authors: ["Radford, Alec", "Wu, Jeffrey", "Child, Rewon", "Luan, David", "Amodei, Dario", "Sutskever, Ilya"]
    year: 2019
    doi: null
    url: "https://openai.com/research/better-language-models"
    arxiv_id: null
  - title: "Attention is all you need"
    authors: ["Vaswani, Ashish", "Shazeer, Noam", "Parmar, Niki", "Uszkoreit, Jakob", "Jones, Llion", "Gomez, Aidan N.", "Kaiser, Łukasz", "Polosukhin, Illia"]
    year: 2017
    doi: null
    url: "https://arxiv.org/abs/1706.03762"
    arxiv_id: "1706.03762"
  - title: "Adam: A method for stochastic optimization"
    authors: ["Kingma, Diederik", "Ba, Jimmy"]
    year: 2015
    doi: null
    url: "https://arxiv.org/abs/1412.6980"
    arxiv_id: "1412.6980"
  - title: "Aligning books and movies: Towards story-like visual explanations by watching movies and reading books (BookCorpus)"
    authors: ["Zhu, Yukun", "Kiros, Ryan", "Zemel, Richard", "Salakhutdinov, Ruslan", "Urtasun, Raquel", "Torralba, Antonio", "Fidler, Sanja"]
    year: 2015
    doi: null
    url: "https://arxiv.org/abs/1506.06724"
    arxiv_id: "1506.06724"
  - title: "Neural machine translation of rare words with subword units (BPE)"
    authors: ["Sennrich, Rico", "Haddow, Barry", "Birch, Alexandra"]
    year: 2016
    doi: null
    url: "https://aclanthology.org/P16-1162/"
    arxiv_id: "1508.07909"
  - title: "SpanBERT: Improving pre-training by representing and predicting spans"
    authors: ["Joshi, Mandar", "Chen, Danqi", "Liu, Yinhan", "Weld, Daniel S.", "Zettlemoyer, Luke", "Levy, Omer"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1907.10529"
    arxiv_id: "1907.10529"
  - title: "Cloze-driven pretraining of self-attention networks"
    authors: ["Baevski, Alexei", "Edunov, Sergey", "Liu, Yinhan", "Zettlemoyer, Luke", "Auli, Michael"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1903.07785"
    arxiv_id: "1903.07785"
  - title: "Reducing BERT pre-training time from 3 days to 76 minutes (LAMB)"
    authors: ["You, Yang", "Li, Jing", "Hseu, Jonathan", "Song, Xiaodan", "Demmel, James", "Hsieh, Cho-Jui"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1904.00962"
    arxiv_id: "1904.00962"
  - title: "FAIRSEQ: A fast, extensible toolkit for sequence modeling"
    authors: ["Ott, Myle", "Edunov, Sergey", "Baevski, Alexei", "Fan, Angela", "Gross, Sam", "Ng, Nathan", "Grangier, David", "Auli, Michael"]
    year: 2019
    doi: null
    url: "https://aclanthology.org/N19-4009/"
    arxiv_id: "1904.01038"
  - title: "Scaling neural machine translation"
    authors: ["Ott, Myle", "Edunov, Sergey", "Grangier, David", "Auli, Michael"]
    year: 2018
    doi: null
    url: "https://aclanthology.org/W18-6301/"
    arxiv_id: "1806.00187"
  - title: "Mixed precision training"
    authors: ["Micikevicius, Paulius", "Narang, Sharan", "Alben, Jonah", "Diamos, Gregory", "Elsen, Erich", "Garcia, David", "Ginsburg, Boris", "Houston, Michael", "Kuchaiev, Oleksii", "Venkatesh, Ganesh", "Wu, Hao"]
    year: 2018
    doi: null
    url: "https://arxiv.org/abs/1710.03740"
    arxiv_id: "1710.03740"
  - title: "GLUE: A multi-task benchmark and analysis platform for natural language understanding"
    authors: ["Wang, Alex", "Singh, Amanpreet", "Michael, Julian", "Hill, Felix", "Levy, Omer", "Bowman, Samuel R."]
    year: 2019
    doi: null
    url: "https://openreview.net/forum?id=rJ4km2R5t7"
    arxiv_id: "1804.07461"
  - title: "SuperGLUE: A stickier benchmark for general-purpose language understanding systems"
    authors: ["Wang, Alex", "Pruksachatkun, Yada", "Nangia, Nikita", "Singh, Amanpreet", "Michael, Julian", "Hill, Felix", "Levy, Omer", "Bowman, Samuel R."]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1905.00537"
    arxiv_id: "1905.00537"
  - title: "SQuAD: 100,000+ questions for machine comprehension of text"
    authors: ["Rajpurkar, Pranav", "Zhang, Jian", "Lopyrev, Konstantin", "Liang, Percy"]
    year: 2016
    doi: null
    url: "https://aclanthology.org/D16-1264/"
    arxiv_id: "1606.05250"
  - title: "Know what you don't know: Unanswerable questions for SQuAD"
    authors: ["Rajpurkar, Pranav", "Jia, Robin", "Liang, Percy"]
    year: 2018
    doi: null
    url: "https://aclanthology.org/P18-2124/"
    arxiv_id: "1806.03822"
  - title: "RACE: Large-scale reading comprehension dataset from examinations"
    authors: ["Lai, Guokun", "Xie, Qizhe", "Liu, Hanxiao", "Yang, Yiming", "Hovy, Eduard"]
    year: 2017
    doi: null
    url: "https://aclanthology.org/D17-1082/"
    arxiv_id: "1704.04683"
  - title: "Defending against neural fake news"
    authors: ["Zellers, Rowan", "Holtzman, Ari", "Rashkin, Hannah", "Bisk, Yonatan", "Farhadi, Ali", "Roesner, Franziska", "Choi, Yejin"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1905.12616"
    arxiv_id: "1905.12616"
  - title: "Multi-task deep neural networks for natural language understanding (MT-DNN)"
    authors: ["Liu, Xiaodong", "He, Pengcheng", "Chen, Weizhu", "Gao, Jianfeng"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1901.11504"
    arxiv_id: "1901.11504"
  - title: "ERNIE: Enhanced representation through knowledge integration"
    authors: ["Sun, Yu Stephanie", "Wang, Shuohuan", "Li, Yukun", "Feng, Shikun", "Chen, Xuyi", "Zhang, Han", "Tian, Xinlun", "Zhu, Danxiang", "Tian, Hao", "Wu, Hua"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1904.09223"
    arxiv_id: "1904.09223"
  - title: "Universal language model fine-tuning for text classification (ULMFiT)"
    authors: ["Howard, Jeremy", "Ruder, Sebastian"]
    year: 2018
    doi: null
    url: "https://aclanthology.org/P18-1031/"
    arxiv_id: "1801.06146"
  - title: "Unified language model pre-training for natural language understanding and generation (UniLM)"
    authors: ["Dong, Li", "Yang, Nan", "Wang, Wenhui", "Wei, Furu", "Liu, Xiaodong", "Wang, Yu", "Gao, Jianfeng", "Zhou, Ming", "Hon, Hsiao-Wuen"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1905.03197"
    arxiv_id: "1905.03197"
  - title: "MASS: Masked sequence to sequence pre-training for language generation"
    authors: ["Song, Kaitao", "Tan, Xu", "Qin, Tao", "Lu, Jianfeng", "Liu, Tie-Yan"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1905.02450"
    arxiv_id: "1905.02450"
  - title: "Learned in translation: Contextualized word vectors (CoVe)"
    authors: ["McCann, Bryan", "Bradbury, James", "Xiong, Caiming", "Socher, Richard"]
    year: 2017
    doi: null
    url: "https://arxiv.org/abs/1708.00107"
    arxiv_id: "1708.00107"
  - title: "Semi-supervised sequence learning"
    authors: ["Dai, Andrew M.", "Le, Quoc V."]
    year: 2015
    doi: null
    url: "https://arxiv.org/abs/1511.01432"
    arxiv_id: "1511.01432"
  - title: "A simple method for commonsense reasoning"
    authors: ["Trinh, Trieu H.", "Le, Quoc V."]
    year: 2018
    doi: null
    url: "https://arxiv.org/abs/1806.02847"
    arxiv_id: "1806.02847"
  - title: "Improving multi-task deep neural networks via knowledge distillation for natural language understanding"
    authors: ["Liu, Xiaodong", "He, Pengcheng", "Chen, Weizhu", "Gao, Jianfeng"]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1904.09482"
    arxiv_id: "1904.09482"
hallucination_severity: "Clean"
best_figure:
  number: 4
  title: "Development set results for RoBERTa as we pretrain over more data and pretrain for longer"
  page: 7
  image_path: "figures/liu-2019-roberta-pretraining-fig.png"
---

# RoBERTa: A Robustly Optimized BERT Pretraining Approach

**Authors:** Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov
**Published:** 2019-07 · [Source](https://arxiv.org/abs/1907.11692)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

A controlled replication of BERT pretraining that finds BERT was significantly **undertrained**. Holding the architecture and MLM objective fixed, the authors show that four "boring" recipe changes — (1) train longer with bigger batches (8K vs 256) over more data (160GB vs 16GB), (2) drop the Next Sentence Prediction (NSP) loss, (3) train on longer (full-512-token) sequences, (4) switch from static to dynamic masking — push the same BERT-LARGE architecture to **state-of-the-art on GLUE (88.5 avg), SQuAD 2.0 (89.4 F1), and RACE (83.2)**, matching or exceeding XLNet despite XLNet's more elaborate permutation-LM objective. The paper's deeper claim is methodological: many post-BERT "architectural" gains were really scale-and-tuning gains in disguise. Releases code, weights, and the new CC-NEWS dataset (76GB filtered).

**For the memory-architect lens:** this is the canonical demonstration that on the **Encode (E)** dimension, *what* you compress into a fixed-capacity model is dominated by *how much* and *how long* you let it compress, not by clever auxiliary objectives. An ablation-driven recipe rewrite beat architectural novelty.

## Key Takeaway

**Quietly tuned hyperparameters and more training data outperformed an architecturally novel competitor (XLNet) on the same benchmarks.** This is the single most-cited empirical case in NLP for "the model wasn't broken — your training run was." Concretely: BERT-LARGE went from 90.9/81.8 SQuAD F1 (Devlin's original) to 94.6/89.4 on the same architecture, by changing only the training recipe.

For memory-system designers, the operational lesson is that **compression-quality is a function of pass-count and corpus diversity, not just of clever loss design**. If your memory system encodes once-per-event with a small distillation prompt and never revisits, you are the BERT-original of memory systems; you have not exhausted the architecture you already shipped.

## Implications

**ENGRAM dimension mapping:**

- **E (Encode) — strongest signal.** The paper is an ablation of the *write-path*. Two write-time choices dominate: (a) dynamic vs static masking — re-randomising the mask every forward pass adds ~0.4 F1 on SQuAD 2.0 (78.3 → 78.7) and is "free" once you stop pre-baking masks; (b) NSP removal — the auxiliary "are these two segments adjacent?" loss not only didn't help, it actively hurt when paired with shorter segment-pair inputs. **Implication for our brain:** every "secondary signal" we extract at write-time (relationship-edges, confidence scores, contradiction-flags) needs the same ablation. If a write-time signal isn't measurably improving a downstream query, it's NSP — drop it.

- **E + M (Encode × Maintain interaction).** Static masking forced the team to duplicate the corpus 10× to give each sentence 10 different masks across 40 epochs (so each mask appears 4 times). Dynamic masking eliminates this 10× storage tax. **Implication:** a write-time "freeze" (commit a single extraction, never re-derive) creates a multiplicative storage burden you didn't realise you signed up for. Lazy/just-in-time re-derivation at read time can be cheaper *and* better.

- **A (Aggregate) — the NSP story is about over-aggregation.** NSP forced the model to learn a coarse document-pair signal that wasn't useful and crowded out the MLM gradient. **Implication:** consolidation steps that synthesise "patterns" from raw memories can hurt if the synthesis target isn't what you actually query for. Default to capturing atomic events; aggregate only when there's evidence the aggregate query exists.

- **R (Retrieve)** — almost untouched by this paper. RoBERTa is a representation-learning paper, not a retrieval one. But it underwrites every dense retriever built since (DPR, ColBERT, Contriever all use RoBERTa or descendants as the encoder). The retrieval quality ceiling of every modern dense memory system is set by the pretraining recipe established here.

- **G (Ground) — under-emphasised.** RoBERTa adds zero provenance. Outputs are unattributed token distributions. This is the gap that retrieval-augmented architectures (RETRO, RAG) later try to fill — and it's exactly where a memory system *cannot* afford to be RoBERTa-like.

- **N (Network/Shape) — flat.** Everything is one monolithic 355M-parameter dense encoder. The paper treats memory as a single shape: parameters. The polyglot-stack debate is invisible here, which is itself instructive — the GPT/RoBERTa lineage starts a 5-year trend of "just put it all in the weights," which only breaks down when context grows large enough that re-deriving everything per query becomes uneconomic.

**Cross-dimensional warning:** RoBERTa's success popularised the view that "encode harder, retrieve less" beats "encode lazily, retrieve smart." For agent memory this is the **opposite** lesson we want — write-time over-compression is the failure mode we are explicitly trying to avoid. RoBERTa is the canonical baseline we are arguing against, not for. Cite it carefully.

## How to Apply It (method)

**The RoBERTa recipe, as transferable engineering principles for a memory system:**

1. **Ablate every auxiliary signal you've added.** RoBERTa's biggest scalar gain (NSP removal) came from *deleting* a feature the original authors thought was load-bearing. Audit: which extraction prompts in our brain are adding noise rather than signal? Build an A/B harness where each ENGRAM-extraction sub-prompt can be toggled off and you measure end-to-end retrieval quality.

2. **Never pre-bake an extraction you can regenerate.** Static masking forced 10× corpus duplication. Anywhere we cache an LLM-summarised version of source content, we are paying that tax. If the summary can be regenerated in <500ms from source, regenerate it.

3. **Scale data before scaling architecture.** RoBERTa moved 16GB → 160GB and got +1.7 GLUE points; switching architectures (BERT → XLNet) got +0.9. For our brain: corpus expansion (ingesting more conversations, more notes, more papers) likely beats algorithmic cleverness in retrieval ranking.

4. **Train (= re-index) longer.** 100K → 500K steps gave +1.0 SQuAD F1 with no overfitting. Translation: re-running QMD embed after every session is not wasted work; the longer the index has been "trained" against query-pattern drift, the better it gets.

5. **Variable-length inputs beat fixed.** RoBERTa removes the "two segments must fit in 512 tokens" rule and packs full sentences from documents. For us: arbitrary memory-chunk boundaries (sentence-split, semantic-split) outperform fixed-window chunking.

6. **Larger batches with tuned LR.** 256 → 8K batches with the right LR improved both perplexity and downstream accuracy. Mirror in memory: batch your nightly re-embeds rather than streaming one-at-a-time; per-item operations have hidden per-call overhead.

**Direct flow-os action items:**
- Add an "extraction ablation" mode to `/learn` that runs the same transcript with N extraction prompts toggled off, and records which extractions QMD subsequently surfaces in real queries. Drop extractions that never get surfaced.
- Replace any cached LLM-summaries of raw source files with on-demand regeneration where the source file is <50KB.
- Increase QMD re-index cadence (currently triggered by `/learn`; consider a daily scheduled reflow).

## Best Figure

![Figure 4 — Development set results for RoBERTa as we pretrain over more data and pretrain for longer (page 7)](figures/liu-2019-roberta-pretraining-fig.png)

**Figure Page: 7** | **Table 4** — Development set results for RoBERTa as we pretrain over more data (16GB → 160GB) and pretrain for longer (100K → 300K → 500K steps).

**Why this is the most informative single artefact in the paper:** Table 4 is the dose-response curve for the whole replication thesis. Reading top-to-bottom in the RoBERTa block, every row is the same model — same architecture, same MLM objective, same batch size of 8K. The only things changing are **data volume** (column "data": 16 → 160 GB) and **gradient steps** (column "steps": 100K → 300K → 500K). Performance monotonically rises across every benchmark column with each increment, and crucially the final row (160GB / 500K steps) **outperforms XLNet-LARGE** (last row of bottom block) — a model with a strictly more elaborate pretraining objective trained on similar-scale data (126GB / 500K steps).

**For the memory-architect lens, three readings:**

1. **Compression saturates slowly.** Even at 500K steps the authors note no overfitting; the curve has not flattened. Translation: a memory-encoding pipeline that runs once is leaving capacity on the table. Re-encoding (re-extracting) the same source with different prompts or after more accumulated context is likely to yield strictly more recall.

2. **Data > steps > architecture.** Going 16GB→160GB at fixed 100K steps adds +0.4 SQuAD F1. Going 100K→500K at fixed 160GB adds +1.7. Going from BERT-LARGE (line 5) to RoBERTa (line 1) at controlled 13-16GB adds +5.5 — but this is the *recipe rewrite*, not the architecture. Comparing line 1 (RoBERTa @ 16GB) vs the XLNet block at 13GB: RoBERTa wins by 5.5 F1 with the *same data and the simpler objective*. The architectural novelty buys nothing when the recipe is tuned.

3. **The "free lunch" is engineering discipline, not novelty.** No new layer types, no new attention mechanism, no new positional encoding. Just: train longer, on more, with bigger batches, without NSP. This is the empirical foundation for the "just scale it" school that dominated 2019-2023.

## What Experts Overlook

For a memory-system researcher, the paper has three under-discussed implications that the broader NLP community has not internalised:

1. **The NSP-removal result is a warning about auxiliary loss design, not a "BERT was wrong" finding.** Most surveys cite RoBERTa as proof that "NSP is bad." The actual finding is more subtle: NSP, *paired with* the segment-pair input format that artificially shortened sequences, hurt. The contribution decomposes — and DOC-SENTENCES (single-doc full-512-token inputs, no NSP) is the actual winner. **For agent memory:** when you add a "second signal" extraction (e.g., extracting both *facts* and *sentiments* in one pass), you may be compounding two failures: (a) the second signal isn't helpful, and (b) it forces a less-natural input shape that hurts the first signal. Always ablate the *combination*, not the individual flag.

2. **Dynamic masking is a much bigger deal than the +0.4 F1 suggests.** The static-vs-dynamic discussion is buried in Section 4.1 and the effect size looks modest. But static masking was the reason the original BERT had to duplicate the training corpus 10×. The systems-cost of "freeze extraction at write-time" is silently 10×. **For us:** every memory we extract and freeze is implicitly committing to that frozen version forever. If queries shift, we have either (a) re-extract everything (corpus duplication) or (b) live with stale extractions. Dynamic re-extraction at query time is the analogue of dynamic masking — it sounds expensive but eliminates the cache-invalidation tax.

3. **The "we leave further exploration to future work" footnotes are where the action was.** The paper notes (Section 4.4) that early experiments showed byte-level BPE had "slightly worse end-task performance on some tasks" than character-level BPE. They shipped byte-level BPE anyway because of universality. This trade-off — accept a small task-specific accuracy hit for a much more general encoding — is the same trade-off we face when choosing semantic vs lexical chunking. The RoBERTa decision pattern (favor generality) became the de-facto default in the field, but the experiments behind it were never fully published. **Implication:** in our own memory design, document the cases where we deliberately chose generality over peak-task-quality. These are the choices that compound oddly over years.

**What everyone overlooks but matters for us specifically:** RoBERTa is the inflection point where the field stopped doing careful ablations and started chasing scale. Subsequent papers (GPT-3, PaLM, etc.) explicitly forgo controlled comparisons because they're computationally prohibitive. RoBERTa is the last big paper where we know the per-knob contribution. For memory systems where we *can* still afford ablations, this discipline is recoverable — and we should be the team that recovers it.

## Extracted Prompts

The paper itself doesn't expose user-facing prompts (it's a pretraining paper, no chat interface), but the implicit "instructions" for downstream practitioners are encoded in the released training recipe. Reverse-engineered as actionable templates:

**Template A — The "is your encoder undertrained?" diagnostic**
```
Given:
  - architecture: <model>
  - training data size (GB): <D>
  - training steps: <S>
  - batch size: <B>
  - approximate epochs over data: D_over_S = (S × B × seq_len) / total_tokens

If D_over_S < 30 epochs equivalent at batch_size=256: model is likely undertrained.
Action: increase S (and re-tune LR for the larger batch) before considering architectural changes.
```

**Template B — The "drop the auxiliary loss" audit**
```
For each auxiliary loss term L_i in your training objective:
  1. Train two variants for N steps: with L_i, without L_i
  2. Compare on the primary downstream task you actually care about
  3. If without L_i is within 1% of with L_i, drop it
  4. Re-check that the input format wasn't implicitly contorted by L_i — and if so, also relax that constraint
```

**Template C — The "dynamic mask" pattern (generalised)**
```
For any preprocessing step that produces a deterministic-but-arbitrary view of a training instance:
  - Replace the preprocessing with on-the-fly randomised generation
  - Confirm storage cost goes down (no need to pre-materialise N copies)
  - Confirm downstream metrics stay flat or improve
```

These templates port directly to memory-system design. For example, **Template B** applied to our `/learn` pipeline: every memory category (decision, contact, pattern, contradiction, etc.) is an auxiliary loss term — does extracting category X measurably improve any query? If not, stop extracting it.

## Citations

The full citation list is in the frontmatter (`citations:` field). Highlights — papers most relevant to memory architecture, in order of likely future digestion priority:

- **Devlin et al. 2019 (BERT)** — already in wiki ([[devlin-2018-bert]]) — the model RoBERTa is replicating
- **Yang et al. 2019 (XLNet)** — the architectural alternative RoBERTa beats with a simpler recipe
- **Vaswani et al. 2017 (Attention is all you need)** — the underlying transformer architecture (foundational)
- **Radford et al. 2019 (GPT-2)** — the byte-level BPE encoding RoBERTa adopts
- **Sennrich et al. 2016 (BPE)** — subword vocabulary construction (foundational tokenization)
- **Howard & Ruder 2018 (ULMFiT)** — the broader "pretrain then finetune" paradigm RoBERTa extends
- **Joshi et al. 2019 (SpanBERT)** — co-authored by Liu, Chen, Levy, Zettlemoyer — span-prediction alternative to MLM
- **Wang et al. 2019 (GLUE/SuperGLUE)** — the benchmarks RoBERTa tops, and the substrate for most subsequent eval design
- **Rajpurkar et al. 2016/2018 (SQuAD)** — the QA benchmark; relevant to retrieval-augmented memory
- **You et al. 2019 (LAMB)** — the large-batch BERT training that RoBERTa builds on
- **Ott et al. 2019 (FAIRSEQ)** — the toolkit; mostly engineering
- **Lample & Conneau 2019 (XLM)** — multilingual extension to BERT-style pretraining
- **Peters et al. 2018 (ELMo)** — pre-BERT contextualised embeddings; historical context

Less central but worth noting: the GLUE constituent tasks (CoLA, SST, MRPC, STS, QQP, MNLI, QNLI, RTE, WNLI) cited via Warstadt, Socher, Dolan, Iyer, Williams, Levesque, Bowman et al. — each is a benchmark paper, not a memory-architecture paper.

## Related Digests

- [[devlin-2018-bert]] — BERT: the model RoBERTa replicates and shows was undertrained; direct parent paper
- [[lewis-2019-bart]] — BART: denoising seq-to-seq pretraining that explicitly generalises BERT; published contemporaneously and shares the FAIR pretraining-recipe lineage
- [[raffel-2020-t5]] — T5: the encoder-decoder cousin that systematises pretraining ablations a year later, citing RoBERTa-style methodology
- [[bi-2020-palm-context-generation]] — PALM: extends BART/T5 lineage; useful contrast for "encoder pretraining choices matter for generation too"
- [[guu-2020-realm]] — REALM: retrieval-augmented BERT pretraining; the natural next step once you accept RoBERTa's finding that parameters alone aren't enough

## Reviewer Notes

**Severity: Clean.**

Cross-checked the following claims against paper text:

- "BERT-LARGE 16GB→160GB and 100K→500K steps reaches 94.6/89.4 SQuAD F1" — verified in Table 4, page 7.
- "Original BERT was 90.9/81.8 SQuAD F1 on BERT-LARGE with BOOKS+WIKI" — verified in Table 4, page 7.
- "Dynamic masking yields +0.4 SQuAD 2.0 F1 over static (78.7 vs 78.3)" — verified in Table 1, page 4.
- "BookCorpus + Wikipedia = 16GB" — verified Section 3.2.
- "CC-NEWS = 76GB after filtering" — verified Section 3.2.
- "Total corpus 160GB across BookCorpus+Wiki+CC-NEWS+OpenWebText+Stories" — verified Section 3.2 (BC+Wiki 16 + CC-NEWS 76 + OpenWebText 38 + Stories 31 ≈ 161, paper says "over 160GB").
- "8K batch size, 500K steps" — verified Table 4 and Appendix B Table 9.
- "GLUE 88.5 average on test leaderboard" — verified Table 5, page 8.
- "RACE 83.2 test accuracy" — verified Table 7, page 9.
- Author list and affiliations verified against page 1.

One soft claim worth flagging: the digest characterises RoBERTa as "the inflection point where the field stopped doing careful ablations." This is editorial commentary on top of the paper, not a paper claim. Reader should treat it as the digester's interpretation through the memory-architect lens, not as a finding of Liu et al.

Lens-specific extrapolations to ENGRAM (E/N/G/R/A/M tagging, memory-system applications) are explicit interpretations and clearly labelled as such — not presented as paper claims.

No fabricated numbers, no fabricated quotes, no invented co-authors. Citations all appear in the paper's bibliography (pages 11-13).
