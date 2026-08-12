---
corpus: agentic-memory
kind: paper-digest
slug: beltagy-2020-longformer
title: "Longformer: The Long-Document Transformer"
authors:
  - "Beltagy, Iz"
  - "Peters, Matthew E."
  - "Cohan, Arman"
year: 2020
publication_date: "2020-12"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2004.05150"
doi: null
arxiv_id: "2004.05150"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Most of the long-context revolution wasn't a smarter algorithm — it was admitting that almost no token actually needs to talk to every other token, and that the few that do should be named by the task rather than discovered."
topics:
  - long-context-transformers
  - sparse-attention
  - sliding-window-attention
  - global-attention
  - pretraining-finetuning
  - long-document-qa
  - long-document-summarization
  - encoder-decoder
  - memory-architecture
  - retrieve
  - network
tags:
  - paper
  - canonical
  - attention
  - longformer
  - led
  - transformer
  - long-context
  - engram-network
  - engram-retrieve
entities:
  - beltagy-iz
  - peters-matthew-e
  - cohan-arman
  - allen-institute-for-ai
related_digests:
  - hu-2026-evermemos
  - packer-2023-memgpt-os
  - tavakoli-2025-beam-light
  - wu-2024-longmemeval
citations:
  - title: "ETC: Encoding long and structured inputs in transformers"
    authors: ["Joshua Ainslie", "Santiago Ontanon", "Chris Alberti", "et al."]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Character-level language modeling with deeper self-attention"
    authors: ["Rami Al-Rfou", "Dokook Choe", "Noah Constant", "et al."]
    year: 2018
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reading wikipedia to answer open-domain questions"
    authors: ["Danqi Chen", "Adam Fisch", "Jason Weston", "et al."]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multi-hop question answering via reasoning chains"
    authors: ["Jifan Chen", "Shih-Ting Lin", "Greg Durrett"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1910.02610"
  - title: "TVM: An automated end-to-end optimizing compiler for deep learning"
    authors: ["Tianqi Chen", "Thierry Moreau", "Ziheng Jiang", "et al."]
    year: 2018
    venue: "OSDI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training deep nets with sublinear memory cost"
    authors: ["Tianqi Chen", "Bing Xu", "Chiyuan Zhang", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1604.06174"
  - title: "Generating long sequences with sparse transformers"
    authors: ["Rewon Child", "Scott Gray", "Alec Radford", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1904.10509"
  - title: "Simple and effective multi-paragraph reading comprehension"
    authors: ["Christopher Clark", "Matt Gardner"]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "What does BERT look at? An analysis of BERT's attention"
    authors: ["Kevin Clark", "Urvashi Khandelwal", "Omer Levy", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1906.04341"
  - title: "A discourse-aware attention model for abstractive summarization of long documents"
    authors: ["Arman Cohan", "Franck Dernoncourt", "Doo Soon Kim", "et al."]
    year: 2018
    venue: "NAACL-HLT"
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
  - title: "Transformer-XL: Attentive language models beyond a fixed-length context"
    authors: ["Zihang Dai", "Zhilin Yang", "Yiming Yang", "et al."]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."]
    year: 2019
    venue: "NAACL-HLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Hierarchical graph network for multi-hop question answering"
    authors: ["Yuwei Fang", "Siqi Sun", "Zhe Gan", "et al."]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "MRQA 2019 shared task: Evaluating generalization in reading comprehension"
    authors: ["Adam Fisch", "Alon Talmor", "Robin Jia", "et al."]
    year: 2019
    venue: "MRQA workshop at EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "A divide-and-conquer approach to the summarization of academic articles"
    authors: ["Alexios Gidiotis", "Grigorios Tsoumakas"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.06190"
  - title: "Span selection pre-training for question answering"
    authors: ["Michael Glaß", "Alfio Massimiliano Gliozzo", "Rishav Chakravarti", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.04120"
  - title: "GPU kernels for block-sparse weights"
    authors: ["Scott Gray", "Alec Radford", "Diederik P. Kingma"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "A simple yet strong pipeline for HotpotQA"
    authors: ["Dirk Groeneveld", "Tushar Khot", "Mausam", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.06753"
  - title: "GMAT: Global memory augmentation for transformers"
    authors: ["Ankit Gupta", "Jonathan Berant"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2006.03274"
  - title: "Universal language model fine-tuning for text classification"
    authors: ["Jeremy Howard", "Sebastian Ruder"]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension"
    authors: ["Mandar Joshi", "Eunsol Choi", "Daniel S. Weld", "et al."]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT for coreference resolution: Baselines and analysis"
    authors: ["Mandar Joshi", "Omer Levy", "Luke Zettlemoyer", "et al."]
    year: 2019
    venue: "EMNLP-IJCNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "SemEval-2019 task 4: Hyperpartisan news detection"
    authors: ["Johannes Kiesel", "Maria Mestre", "Rishabh Shukla", "et al."]
    year: 2019
    venue: "SemEval"
    doi: null
    url: null
    arxiv_id: null
  - title: "Semi-supervised classification with graph convolutional networks"
    authors: ["Thomas N Kipf", "Max Welling"]
    year: 2017
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reformer: The efficient transformer"
    authors: ["Nikita Kitaev", "Lukasz Kaiser", "Anselm Levskaya"]
    year: 2020
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Revealing the dark secrets of BERT"
    authors: ["Olga V. Kovaleva", "Alexey Romanov", "Anna Rogers", "et al."]
    year: 2019
    venue: "EMNLP/IJCNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Higher-order coreference resolution with coarse-to-fine inference"
    authors: ["Kenton Lee", "Luheng He", "Luke Zettlemoyer"]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension"
    authors: ["Mike Lewis", "Yinhan Liu", "Naman Goyal", "et al."]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "RoBERTa: A robustly optimized BERT pretraining approach"
    authors: ["Yinhan Liu", "Myle Ott", "Naman Goyal", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1907.11692"
  - title: "Learning word vectors for sentiment analysis"
    authors: ["Andrew L. Maas", "Raymond E. Daly", "Peter T. Pham", "et al."]
    year: 2011
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Large text compression benchmark"
    authors: ["Matt Mahoney"]
    year: 2009
    venue: "online"
    doi: null
    url: null
    arxiv_id: null
  - title: "WaveNet: A generative model for raw audio"
    authors: ["Aäron van den Oord", "Sander Dieleman", "Heiga Zen", "et al."]
    year: 2016
    venue: "SSW"
    doi: null
    url: null
    arxiv_id: null
  - title: "fairseq: A fast, extensible toolkit for sequence modeling"
    authors: ["Myle Ott", "Sergey Edunov", "Alexei Baevski", "et al."]
    year: 2019
    venue: "NAACL-HLT Demonstrations"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep contextualized word representations"
    authors: ["Matthew E. Peters", "Mark Neumann", "Mohit Iyyer", "et al."]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "CoNLL-2012 shared task: Modeling multilingual unrestricted coreference in OntoNotes"
    authors: ["Sameer Pradhan", "Alessandro Moschitti", "Nianwen Xue", "et al."]
    year: 2012
    venue: "Joint Conference on EMNLP and CoNLL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Blockwise self-attention for long document understanding"
    authors: ["Jiezhong Qiu", "Hao Ma", "Omer Levy", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.02972"
  - title: "Language models are unsupervised multitask learners"
    authors: ["Alec Radford", "Jeffrey Wu", "Rewon Child", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Compressive transformers for long-range sequence modelling"
    authors: ["Jack W. Rae", "Anna Potapenko", "Siddhant M. Jayakumar", "et al."]
    year: 2020
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exploring the limits of transfer learning with a unified text-to-text transformer"
    authors: ["Colin Raffel", "Noam Shazeer", "Adam Roberts", "et al."]
    year: 2020
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient content-based sparse attention with routing transformers"
    authors: ["Aurko Roy", "Mohammad Saffar", "Ashish Vaswani", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2003.05997"
  - title: "Is graph structure necessary for multi-hop reasoning?"
    authors: ["Nan Shao", "Yiming Cui", "Ting Liu", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.03096"
  - title: "On extractive and abstractive neural document summarization with transformer language models"
    authors: ["Sandeep Subramanian", "Raymond Li", "Jonathan Pilault", "et al."]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adaptive attention span in transformers"
    authors: ["Sainbayar Sukhbaatar", "Edouard Grave", "Piotr Bojanowski", "et al."]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sequence to sequence learning with neural networks"
    authors: ["Ilya Sutskever", "Oriol Vinyals", "Quoc V. Le"]
    year: 2014
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "A simple method for commonsense reasoning"
    authors: ["Trieu H. Trinh", "Quoc V. Le"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1806.02847"
  - title: "Select, answer and explain: Interpretable multi-hop reading comprehension over multiple documents"
    authors: ["Ming Tu", "Kevin Huang", "Guangtao Wang", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.00484"
  - title: "Graph sequential network for reasoning over sequences"
    authors: ["Ming Tu", "Jinke Huang", "Xiaodong He", "et al."]
    year: 2020
    venue: "NeurIPS Graph Representation Learning workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Constructing datasets for multi-hop reading comprehension across documents (WikiHop)"
    authors: ["Johannes Welbl", "Pontus Stenetorp", "Sebastian Riedel"]
    year: 2018
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Pay less attention with lightweight and dynamic convolutions"
    authors: ["Felix Wu", "Angela Fan", "Alexei Baevski", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1901.10430"
  - title: "Unsupervised data augmentation for consistency training"
    authors: ["Qizhe Xie", "Zihang Dai", "Eduard H. Hovy", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1904.12848"
  - title: "On layer normalization in the transformer architecture"
    authors: ["Ruibin Xiong", "Yunchang Yang", "Di He", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2002.04745"
  - title: "HotpotQA: A dataset for diverse, explainable multi-hop question answering"
    authors: ["Zhilin Yang", "Peng Qi", "Saizheng Zhang", "et al."]
    year: 2018
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "BP-Transformer: Modelling long-range context via binary partitioning"
    authors: ["Zihao Ye", "Qipeng Guo", "Quan Gan", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.04070"
  - title: "Big Bird: Transformers for longer sequences"
    authors: ["Manzil Zaheer", "Guru Guruganesh", "Kumar Avinava Dubey", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2007.14062"
  - title: "Defending against neural fake news"
    authors: ["Rowan Zellers", "Ari Holtzman", "Hannah Rashkin", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Pegasus: Pre-training with extracted gap-sentences for abstractive summarization"
    authors: ["Jingqing Zhang", "Yao Zhao", "Mohammad Saleh", "et al."]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Aligning books and movies: Towards story-like visual explanations by watching movies and reading books"
    authors: ["Yukun Zhu", "Ryan Kiros", "Richard S. Zemel", "et al."]
    year: 2015
    venue: "ICCV"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Comparing the full self-attention pattern and the configuration of attention patterns in our Longformer"
  page: 3
  image_path: "figures/beltagy-2020-longformer-fig.png"
---

# Longformer: The Long-Document Transformer

**Authors:** Iz Beltagy, Matthew E. Peters, Arman Cohan (Allen Institute for AI)
**Published:** 2020-12 (v2; original v1 April 2020) · [Source](https://arxiv.org/abs/2004.05150)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Longformer replaces the O(n^2) self-attention of a standard Transformer with a combination of a **fixed-size sliding window** (each token attends to w/2 tokens on each side, complexity O(n·w)) and a **task-motivated global attention** at a handful of pre-selected positions (e.g., [CLS] for classification, all question tokens for QA), giving O(n) scaling and enabling sequences up to 4,096 tokens for finetuning and 32,256 for character-level LM on then-current GPUs. Beyond the architecture, the contribution is a **drop-in replacement recipe**: continue MLM pretraining from a RoBERTa checkpoint, extend learned absolute position embeddings from 512 to 4,096 by **copying the 512-slot block 8 times** (this single trick drops MLM BPC from 10.299 at random init to 1.957, then to 1.705 after 65K updates vs. RoBERTa's 1.846), and finetune. The pretrained Longformer-base beats RoBERTa-base on every long-document benchmark tested (WikiHop 75.0 vs 72.4, TriviaQA 75.2 vs 74.3, HotpotQA 64.4 vs 63.5, OntoNotes 78.6 vs 78.4, IMDB 95.7 vs 95.3, Hyperpartisan 94.8 vs 87.4), and Longformer-large sets SOTA on WikiHop (81.9, +3.6) and TriviaQA (77.3, +4). The encoder-decoder variant LED (initialized from BART, position embeddings copied 16x to reach 16K tokens) hits SOTA on arXiv summarization (R-1 46.63 at 16K) — and Fig. 3 shows ROUGE rising monotonically from 1K → 4K → 16K input length, confirming the gains come from *seeing more*, not just better priors. Ablations are blunt: drop global attention and WikiHop accuracy collapses by 8.3 points; drop the separate Q/K/V projections for global attention and you lose 1.6 points; drop MLM pretraining entirely and you lose only 0.6 — i.e., the architecture matters more than the extra pretraining.

## Key Takeaway

Most of the long-context revolution wasn't a smarter algorithm — it was admitting that almost no token actually needs to talk to every other token, and that the few that do should be *named by the task* rather than discovered. A 512-wide window plus 8-12 hand-picked "global" tokens (the [CLS], the question, the answer candidates) reproduces full-attention performance on long documents, while a 230-token *fixed* window with no global attention loses 8.3 accuracy points on WikiHop. The lesson for memory architecture: stop trying to make every chunk semantically reachable from every other chunk; instead, identify the small set of *anchor positions* whose job is to broadcast and gather across the whole context, and let everything else live in a cheap local neighborhood.

## Implications

- **ENGRAM-Network: "local window + named global anchors" is a generalizable shape, not just an attention trick** — In memory systems, this maps to "every memory has cheap access to its temporal/topical neighbors, plus a small set of pinned anchor memories (a values doc, a current-state doc, the active venture's INDEX) that every retrieval can see." The 8.3-point drop when global attention is removed (WikiHop, Tab. 10) tells you the anchors do more work than the local context does.
- **ENGRAM-Network: the right shape is task-conditional, hard-coded, not learned** — Longformer adds different global attention for classification ([CLS]), QA (question tokens), and coref (none). The model does *not* learn where to put global attention; the engineer specifies it. Stop trying to make your memory system auto-discover what's important; let the task config name it.
- **ENGRAM-Retrieve: window size is a budget you spend per layer, not a constant** — Tab. 4 shows increasing the window size from bottom to top layer (small w near input, large w near output) beats both fixed-w and decreasing-w configs. Translate: in a multi-stage retrieval pipeline, do tight lexical/local match first, expand semantic scope later — not the reverse.
- **ENGRAM-Encode: don't re-train your encoder, *extend* its position space and continue pretraining** — Copying the 512 RoBERTa position embeddings 8 times to fill 4,096 slots is the single most impactful trick in the paper (BPC 10.299 → 1.957 from this alone). For memory systems migrating from a small-context base to a long-context one, prefer "tile the existing positional prior across the new window" over "randomly initialize and hope."
- **ENGRAM-Maintain: separate projections for the "long-reach" pathway are worth 1.6 points and zero architectural complexity** — Longformer uses Qs/Ks/Vs for window attention and a separate Qg/Kg/Vg for global tokens, initialized as copies. Memory analog: when a chunk is being read *as context* vs. *as anchor*, give it two different embedding/index entries — same content, different retrieval-time role.
- **ENGRAM-Aggregate: longer input beats fancier pre-training on summarization** — LED-large with no LED-specific pretraining, just BART weights and a 16K position embedding, beats Pegasus and matches BigBird on arXiv summarization (R-1 46.63). For an agentic memory system writing a "session digest" or "weekly digest," the leverage is in *feeding more raw memory into one consolidation pass*, not in training a better summarizer.
- **ENGRAM-Ground: dilation hurts when pretrained weights are involved** — Footnote 6 reports dilation on heads during continued pretraining *hurt* performance because it's "not compatible with the pretrained RoBERTa weights." Same warning applies to retrofitting any provenance/attribution layer onto an existing memory store: changes to the read pattern that break the assumptions of pre-existing indices will silently degrade quality.
- **ENGRAM cross-dimension interaction: the Encode choice (window + global) forces the Retrieve and Aggregate choices** — Once you commit to "context lives in a window, anchors broadcast globally," you've also decided that retrieval ranking is window-local with anchor-mediated long jumps, and that aggregation must happen *at the anchors*, not at arbitrary positions. The architecture is one decision that fans out across three ENGRAM dimensions.

## How to Apply It (method)

**Scenario:** You are running ENGRAM experiments on a personal-OS memory layer (markdown vault + QMD hybrid search) and want to test whether replacing your current "retrieve top-k chunks → stuff into prompt → answer" pipeline with a *windowed local + named global anchors* memory pattern improves answer quality on long-session continuity questions ("what did we decide about X across the last 12 sessions"). The retrieval architecture is your design variable; the LLM at the end is fixed.

**Steps:**

1. **Define your "tokens" and your sequence length**: A "token" in your memory system is a memory unit (a paragraph, an atomic memory, a session turn). Your "sequence length" is the total ordered history you want to make addressable — e.g., the last 8,000 atomic memories arranged in chronological order.

2. **Choose your window size w per layer of retrieval**: Following the paper's Tab. 4 finding (increasing w from low to high layer), build a 3-layer retriever:
   - **Layer 1 (small w, e.g. 50)**: BM25 lexical match within a 50-memory window around the query's nearest anchor memory in time. Fast, tight, local.
   - **Layer 2 (medium w, e.g. 200)**: Hybrid BM25+vector within a 200-memory window centered on the same anchor. Captures topical neighbors that aren't lexical matches.
   - **Layer 3 (large w, e.g. 800)**: Pure vector within an 800-memory window. Captures semantic drift over long stretches.

3. **Designate the global-attention anchors by task**: Hard-code which memories *every* query gets to see, indexed by query type:
   ```yaml
   query_type: decision_history
     globals: [CLAUDE.md, memory/values-beliefs/principles.md, memory/ventures/<active>/INDEX.md]
   query_type: contact_question
     globals: [CLAUDE.md, memory/contacts/INDEX.md]
   query_type: technical_recall
     globals: [CLAUDE.md, memory/patterns/INDEX.md, current session's plan.md]
   ```
   Mirror Longformer's per-task global attention configuration — classification uses [CLS], QA uses question tokens, coref uses none.

4. **Build separate retrieval projections for window vs. global**: Use *different* embedding indices for the same memory when it's playing the "neighbor" role vs. the "anchor" role. Two index entries per anchor doc, scored with different weights at retrieval. Mirrors Longformer's Qs/Ks/Vs vs. Qg/Kg/Vg.

5. **Migrate position embeddings, don't re-train**: When you expand your retrievable history from N memories to 8N, *do not* re-embed everything from scratch. If your retriever has any positional/recency prior (e.g., a decay schedule, a temporal bucket), tile the existing prior across the longer window — replicate the recency curve from the last N memories across each chunk of N in the longer history. This is the markdown-memory analog of "copy the 512 position embeddings 8 times."

6. **Ablate brutally before shipping**: Replicate Longformer's Tab. 10 ablations on your own memory system. For your 50 most representative continuity questions, measure answer quality with:
   - Full system (windowed local + global anchors + separate projections)
   - No global anchors
   - No separate projections (single embedding per memory)
   - No "continued pretraining" equivalent (no fine-tuning of the retriever on long-context recall tasks)
   - Sequence length halved
   If any individual ablation drops quality by >5%, that piece is load-bearing — keep it.

7. **Validate with longer-input scaling curves**: Pick a question type that fundamentally requires long context (e.g., "summarize my position on X across 6 months"). Plot answer quality vs. retrieved-context size at 1K / 4K / 16K memory units. If you don't see Longformer's Fig. 3 shape (monotonic improvement with input size), your global-attention anchors aren't doing their job — the long-range information isn't actually reaching the answer.

**Expected outcome:** A memory-retrieval layer where (a) recent/local context is cheap, (b) a small set of named anchor memories broadcast/gather across the whole vault, (c) each retrieval task specifies its own anchor set, and (d) you have empirical ablations showing which architectural pieces are load-bearing for which task types. This is the ENGRAM-architect equivalent of Longformer's "drop-in replacement for self-attention" — a memory layer you can swap into any agent without changing the agent.

## Best Figure

![Figure 2 — Comparing the full self-attention pattern and the configuration of attention patterns in our Longformer (page 3)](figures/beltagy-2020-longformer-fig.png)

Image Candidates:
Figure 2 (p. 3): Side-by-side visualization of (a) full n^2 attention, (b) sliding window, (c) dilated sliding window, (d) global+sliding window — the whole paper's idea in one frame.
Figure 1 (p. 1): Runtime/memory of full self-attention vs. three Longformer implementations as sequence length grows — shows the linear-vs-quadratic punchline as a curve.
Figure 3 (p. 10): ROUGE-1/ROUGE-2 of LED on arXiv summarization as input length grows from 1K → 4K → 16K — proves the gains come from seeing more, not better priors.

Best Image:
Figure Name: Figure 2: "Comparing the full self-attention pattern and the configuration of attention patterns in our Longformer"
Figure Page: 3
Slide Caption: Four attention patterns side-by-side: full quadratic vs. windowed vs. dilated-windowed vs. windowed-plus-global — Longformer's "shape of memory" choice.
Description: A four-panel grid of attention matrices visualized as n×n grids of colored cells, where each cell (i,j) is shaded if token i attends to token j. Panel (a) shows full self-attention (the entire matrix shaded — O(n^2)). Panel (b) shows sliding window attention (only a narrow band along the diagonal shaded). Panel (c) shows dilated sliding window attention (the band has gaps, allowing larger receptive field at the same cost). Panel (d) shows global+sliding window (the diagonal band plus a few full rows and columns corresponding to global-attention tokens). This figure is the paper's whole story in one image: every long-context Transformer is making a choice about which cells of this matrix to compute, and Longformer's choice is "window + a handful of named globals." For a memory architect, this is the canonical visualization of the *shape* of memory — and shows that "what every memory sees" is not a binary choice (everything vs. nothing) but a configurable sparse pattern.

## What Experts Overlook

The detail most easily overlooked is the **position-embedding copy trick** (§5, "Position Embeddings", and the dramatic Tab. 5 numbers). Most readers focus on the windowed-attention architecture and skim past the line that says "instead of randomly initializing the new position embeddings, we initialize them by copying the 512 position embeddings from RoBERTa multiple times." But Tab. 5 shows the impact: random-init Longformer has MLM BPC of 10.299 (effectively broken). The copy trick *alone*, with zero additional gradient updates, drops it to 1.957 — comparable to RoBERTa's 1.846. Only after 65K more updates does it drop further to 1.705. The architecture works because the positional prior survives the extension. The paper's justification is the Kovaleva et al. (2019) / Clark et al. (2019) finding that BERT's attention heads have a strong learned bias to attend to nearby tokens — so a periodic, locally-similar position embedding preserves that bias at the seams. It's a structural-prior preservation move, not a representational one.

**Why it matters:** It tells you that when you extend a pretrained system's "addressable space" (context window, memory horizon, vocabulary), the cost of getting it wrong is enormous, and the cost of doing it right is essentially zero. The system's existing weights encode assumptions about how positions/keys/IDs relate — random initialization at the boundary breaks those assumptions catastrophically and requires expensive re-training to recover. The whole long-context story collapses without this 1-line fix.

**Example of good use:** You're extending a personal-OS memory system from "last 30 days" to "last 240 days" of addressable history. Instead of re-fitting your recency-decay function on the full 240-day window (which would destroy the model's calibration on recent memories — the high-traffic case), you tile the existing 30-day decay curve 8 times across the new window. The system's behavior on the last 30 days is preserved exactly, and the older windows inherit a sensible (if periodic) decay structure that you can then fine-tune locally. Net: zero regression on the dominant query type, gradual improvement on long-range queries.

**Example of misapplication:** You're expanding the same memory system from 30 to 240 days and decide to "do it properly" by re-fitting the recency decay function on the full 240-day window from scratch. The optimizer averages the curve across all 240 days, smoothing out the steep recent decay. Result: queries about events in the last 3 days now retrieve a flatter, less-recency-biased set; users feel the system has "forgotten how to be fresh." You then spend two weeks re-tuning the decay and adding hand-crafted recent-boost terms, recreating what tiling the original curve would have given you on day one.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

- **Attention is all you need** (Vaswani et al., 2017, NIPS) — the original Transformer Longformer modifies
- **BERT: Pre-training of deep bidirectional transformers for language understanding** (Devlin et al., 2019, NAACL-HLT) — the pretrain-finetune paradigm Longformer extends to long docs
- **RoBERTa: A robustly optimized BERT pretraining approach** (Liu et al., 2019, preprint, arXiv:1907.11692) — the checkpoint Longformer continues pretraining from
- **Transformer-XL: Attentive language models beyond a fixed-length context** (Dai et al., 2019, ACL) — main left-to-right long-context baseline on enwik8
- **Generating long sequences with sparse transformers** (Child et al., 2019, arXiv:1904.10509) — most architecturally similar prior work (dilated sliding window of blocks)
- **Reformer: The efficient transformer** (Kitaev et al., 2020, ICLR) — LSH-based sparse-attention competitor on enwik8
- **Big Bird: Transformers for longer sequences** (Zaheer et al., 2020, arXiv:2007.14062) — contemporaneous local+global+random sparse attention; later surpassed Longformer on QA benchmarks
- **ETC: Encoding long and structured inputs in transformers** (Ainslie et al., 2020, EMNLP) — contemporaneous local+global attention with relative positions and CPC pre-training loss
- **BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension** (Lewis et al., 2020, ACL) — the encoder-decoder checkpoint LED is initialized from
- **A discourse-aware attention model for abstractive summarization of long documents** (Cohan et al., 2018, NAACL-HLT) — source of the arXiv summarization dataset LED evaluates on

(Full 58-entry citation list in frontmatter `citations[]`.)

## Related Digests

- [[hu-2026-evermemos]] — Cites Longformer as the canonical local+global sparse-attention precedent for long-context architectures EverMemOS contrasts with
- [[packer-2023-memgpt-os]] — Cites Longformer in the lineage of architectural responses to fixed context limits, before MemGPT's OS-style virtual-memory framing
- [[tavakoli-2025-beam-light]] — Cites Longformer when motivating why hand-engineered sparse-attention patterns gave way to retrieval-augmented "light" context strategies
- [[wu-2024-longmemeval]] — Cites Longformer as a baseline long-context approach against which long-term memory benchmarks are framed

## Reviewer Notes

**Overall severity:** Clean

Every numeric claim in this digest was cross-checked against the paper text:
- Sequence lengths (4,096 for pretrain/finetune; 32,256 for char-LM; 23,040 final-phase training; 16,384 for LED) — verified in §4.2/§5/§7 and Tab. 12.
- MLM BPC numbers (10.299 random init → 1.957 with copy init → 1.705 after 65K updates; RoBERTa 1.846) — verified in Tab. 5.
- Finetuning result deltas (WikiHop 75.0 vs 72.4; TriviaQA 75.2 vs 74.3; HotpotQA 64.4 vs 63.5; OntoNotes 78.6 vs 78.4; IMDB 95.7 vs 95.3; Hyperpartisan 94.8 vs 87.4) — verified in Tab. 7.
- SOTA margins (WikiHop +3.6 with Longformer-large at 81.9; TriviaQA +4 at 77.3) — verified in Tab. 8.
- WikiHop ablation drops (no global +linear-proj = -8.3; no linear proj = -1.6; no MLM pretraining = -0.6) — verified in Tab. 10.
- LED arXiv summarization R-1 46.63 at seqlen 16,384 — verified in Tab. 11.
- "Per-task global attention configuration": classification uses [CLS], QA uses question tokens, coref uses no global — verified in §6.1/§6.2/§6.3.
- "Dilation hurts in continued-pretraining setting" — verified in footnote 6 on page 6.
- Position-embedding copy claim ("copy 512 embeddings 8 times to get 4,096") — verified in §5 "Position Embeddings" paragraph.
- LED initialized from BART, position embeddings copied 16 times to reach 16K — verified in §7.
- Author affiliation (Allen Institute for AI), arXiv ID (2004.05150v2, Dec 2020) — verified on title page.

No claims in the digest extend beyond what the paper explicitly demonstrates. The ENGRAM mapping is presented as an analogy (the lens's frame), not as a claim the paper itself makes.
