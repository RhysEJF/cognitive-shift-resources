---
corpus: agentic-memory
kind: paper-digest
slug: lee-2024-readagent-gist-memory
title: "A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts"
authors:
  - "Lee, Kuang-Huei"
  - "Chen, Xinyun"
  - "Furuta, Hiroki"
  - "Canny, John"
  - "Fischer, Ian"
year: 2024
publication_date: "2024-02"
venue: "ICML 2024 (PMLR 235)"
source_url: "https://arxiv.org/abs/2402.09727"
doi: null
arxiv_id: "2402.09727"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Treating an LLM as a reader that paginates a long document into natural episodes, gists each page, and then interactively looks up the few pages it needs to answer a task beats both full-context use and dense retrieval — extending effective context up to 20x with zero training."
topics:
  - long-context-llms
  - gist-memory
  - episodic-memory
  - reading-comprehension
  - retrieval-augmented-generation
  - llm-agents
  - prompting
  - procedural-memory
tags:
  - paper
  - readagent
  - gist
  - pagination
  - long-document-qa
  - icml-2024
  - palm2
entities:
  - lee-kuang-huei
  - chen-xinyun
  - furuta-hiroki
  - canny-john
  - fischer-ian
  - google-deepmind
related_digests:
  - chen-2023-memwalker
  - dorsey-2026-dgmm-gist-memory
  - sun-2025-hmem-hierarchical-memory
  - sarthi-2024-raptor
  - chhikara-2025-mem0
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "ReadAgent workflow (Episode Pagination -> Gisting -> Interactive Lookup)"
  page: 1
  image_path: "figures/lee-2024-readagent-gist-memory-fig.png"
citations:
  - title: "Walking down the memory maze: Beyond context limit through interactive reading (MemWalker)"
    authors: ["Chen, H.", "Pasunuru, R.", "Weston, J.", "Celikyilmaz, A."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2310.05029"
    arxiv_id: "2310.05029"
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Liu, N. F.", "Lin, K.", "Hewitt, J.", "Paranjape, A.", "Bevilacqua, M.", "Petroni, F.", "Liang, P."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2307.03172"
    arxiv_id: "2307.03172"
  - title: "Large language models can be easily distracted by irrelevant context"
    authors: ["Shi, F.", "Chen, X.", "Misra, K.", "Scales, N.", "Dohan, D.", "Chi, E. H.", "Schaerli, N.", "Zhou, D."]
    year: 2023
    doi: null
    url: "https://proceedings.mlr.press/v202/shi23a.html"
    arxiv_id: null
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks (RAG)"
    authors: ["Lewis, P.", "Perez, E.", "Piktus, A.", "Petroni, F.", "Karpukhin, V.", "Goyal, N.", "Kuettler, H.", "Lewis, M.", "Yih, W.-t.", "Rocktaeschel, T."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2005.11401"
    arxiv_id: "2005.11401"
  - title: "QuALITY: Question answering with long input texts, yes!"
    authors: ["Pang, R. Y.", "Parrish, A.", "Joshi, N.", "Nangia, N.", "Phang, J.", "Chen, A.", "Padmakumar, V.", "Ma, J.", "Thompson, J.", "He, H."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2112.08608"
    arxiv_id: "2112.08608"
  - title: "The narrativeqa reading comprehension challenge"
    authors: ["Kociský, T.", "Schwarz, J.", "Blunsom, P.", "Dyer, C.", "Hermann, K. M.", "Melis, G.", "Grefenstette, E."]
    year: 2018
    doi: null
    url: "https://arxiv.org/abs/1712.07040"
    arxiv_id: "1712.07040"
  - title: "QMSum: A new benchmark for query-based multi-domain meeting summarization"
    authors: ["Zhong, M.", "Yin, D.", "Yu, T.", "Zaidi, A.", "Mutuma, M.", "Jha, R.", "Hassan, A.", "Celikyilmaz, A.", "Liu, Y.", "Qiu, X."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2104.05938"
    arxiv_id: "2104.05938"
  - title: "PaLM 2 Technical Report"
    authors: ["Anil, R.", "Dai, A. M.", "Firat, O.", "Johnson, M.", "Lepikhin, D.", "Passos, A.", "Shakeri, S.", "et al."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.10403"
    arxiv_id: "2305.10403"
  - title: "Longformer: The long-document transformer"
    authors: ["Beltagy, I.", "Peters, M. E.", "Cohan, A."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2004.05150"
    arxiv_id: "2004.05150"
  - title: "Big Bird: Transformers for longer sequences"
    authors: ["Zaheer, M.", "Guruganesh, G.", "Dubey, K. A.", "Ainslie, J.", "Alberti, C.", "Ontanon, S.", "Pham, P.", "Ravula, A.", "Wang, Q.", "Yang, L.", "Ahmed, A."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2007.14062"
    arxiv_id: "2007.14062"
  - title: "Fuzzy-trace theory: An interim synthesis"
    authors: ["Reyna, V. F.", "Brainerd, C. J."]
    year: 1995
    doi: null
    url: null
    arxiv_id: null
  - title: "Recursively summarizing books with human feedback"
    authors: ["Wu, J.", "Ouyang, L.", "Ziegler, D. M.", "Stiennon, N.", "Lowe, R.", "Leike, J.", "Christiano, P."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2109.10862"
    arxiv_id: "2109.10862"
  - title: "PEARL: Prompting large language models to plan and execute actions over long documents"
    authors: ["Sun, S.", "Liu, Y.", "Wang, S.", "Zhu, C.", "Iyyer, M."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.14564"
    arxiv_id: "2305.14564"
  - title: "Learning to reason and memorize with self-notes"
    authors: ["Lanchantin, J.", "Toshniwal, S.", "Weston, J.", "Szlam, A.", "Sukhbaatar, S."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.00833"
    arxiv_id: "2305.00833"
  - title: "Memorizing transformers"
    authors: ["Wu, Y.", "Rabe, M. N.", "Hutchins, D.", "Szegedy, C."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2203.08913"
    arxiv_id: "2203.08913"
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["Park, J. S.", "O'Brien, J.", "Cai, C. J.", "Morris, M. R.", "Liang, P.", "Bernstein, M. S."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2304.03442"
    arxiv_id: "2304.03442"
  - title: "Memorybank: Enhancing large language models with long-term memory"
    authors: ["Zhong, W.", "Guo, L.", "Gao, Q.", "Wang, Y."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.10250"
    arxiv_id: "2305.10250"
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    authors: ["Nakano, R.", "Hilton, J.", "Balaji, S.", "Wu, J.", "Ouyang, L.", "Kim, C.", "Hesse, C.", "Jain, S.", "Kosaraju, V.", "Saunders, W."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2112.09332"
    arxiv_id: "2112.09332"
  - title: "WebShop: Towards scalable real-world web interaction with grounded language agents"
    authors: ["Yao, S.", "Chen, H.", "Yang, J.", "Narasimhan, K."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2207.01206"
    arxiv_id: "2207.01206"
  - title: "Mind2Web: Towards a generalist agent for the web"
    authors: ["Deng, X.", "Gu, Y.", "Zheng, B.", "Chen, S.", "Stevens, S.", "Wang, B.", "Sun, H.", "Su, Y."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2306.06070"
    arxiv_id: "2306.06070"
  - title: "A real-world webagent with planning, long context understanding, and program synthesis"
    authors: ["Gur, I.", "Furuta, H.", "Huang, A.", "Safdari, M.", "Matsuo, Y.", "Eck, D.", "Faust, A."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2307.12856"
    arxiv_id: "2307.12856"
  - title: "Attention is all you need"
    authors: ["Vaswani, A.", "Shazeer, N.", "Parmar, N.", "Uszkoreit, J.", "Jones, L.", "Gomez, A. N.", "Kaiser, L.", "Polosukhin, I."]
    year: 2017
    doi: null
    url: "https://arxiv.org/abs/1706.03762"
    arxiv_id: "1706.03762"
  - title: "Efficient streaming language models with attention sinks"
    authors: ["Xiao, G.", "Tian, Y.", "Chen, B.", "Han, S.", "Lewis, M."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2309.17453"
    arxiv_id: "2309.17453"
  - title: "Train short, test long: Attention with linear biases enables input length extrapolation (ALiBi)"
    authors: ["Press, O.", "Smith, N.", "Lewis, M."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2108.12409"
    arxiv_id: "2108.12409"
  - title: "LongLoRA: Efficient fine-tuning of long-context large language models"
    authors: ["Chen, Y.", "Qian, S.", "Tang, H.", "Lai, X.", "Liu, Z.", "Han, S.", "Jia, J."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2309.12307"
    arxiv_id: "2309.12307"
  - title: "Extending context window of large language models via positional interpolation"
    authors: ["Chen, S.", "Wong, S.", "Chen, L.", "Tian, Y."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2306.15595"
    arxiv_id: "2306.15595"
  - title: "LM-Infinite: Simple on-the-fly length generalization for large language models"
    authors: ["Han, C.", "Wang, Q.", "Xiong, W.", "Chen, Y.", "Ji, H.", "Wang, S."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2308.16137"
    arxiv_id: "2308.16137"
  - title: "Interactive machine comprehension with information seeking agents"
    authors: ["Yuan, X.", "Fu, J.", "Cote, M.-A.", "Tay, Y.", "Pal, C.", "Trischler, A."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/1908.10449"
    arxiv_id: "1908.10449"
  - title: "Wizard of Wikipedia: Knowledge-powered conversational agents"
    authors: ["Dinan, E.", "Roller, S.", "Shuster, K.", "Fan, A.", "Auli, M.", "Weston, J."]
    year: 2019
    doi: null
    url: "https://arxiv.org/abs/1811.01241"
    arxiv_id: "1811.01241"
  - title: "Re3: Generating longer stories with recursive reprompting and revision"
    authors: ["Yang, K.", "Tian, Y.", "Peng, N.", "Klein, D."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2210.06774"
    arxiv_id: "2210.06774"
  - title: "Reading Wikipedia to answer open-domain questions (DrQA)"
    authors: ["Chen, D.", "Fisch, A.", "Weston, J.", "Bordes, A."]
    year: 2017
    doi: null
    url: "https://arxiv.org/abs/1704.00051"
    arxiv_id: "1704.00051"
  - title: "Large language models as optimizers"
    authors: ["Yang, C.", "Wang, X.", "Lu, Y.", "Liu, H.", "Le, Q. V.", "Zhou, D.", "Chen, X."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2309.03409"
    arxiv_id: "2309.03409"
  - title: "System 2 attention (is something you might need too)"
    authors: ["Weston, J.", "Sukhbaatar, S."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2311.11829"
    arxiv_id: "2311.11829"
  - title: "Leveraging passage retrieval with generative models for open domain question answering"
    authors: ["Izacard, G.", "Grave, E."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2007.01282"
    arxiv_id: "2007.01282"
  - title: "The probabilistic relevance framework: BM25 and beyond"
    authors: ["Robertson, S.", "Zaragoza, H."]
    year: 2009
    doi: null
    url: null
    arxiv_id: null
  - title: "ROUGE: A package for automatic evaluation of summaries"
    authors: ["Lin, C.-Y."]
    year: 2004
    doi: null
    url: null
    arxiv_id: null
  - title: "DeBERTa: Decoding-enhanced BERT with disentangled attention"
    authors: ["He, P.", "Liu, X.", "Gao, J.", "Chen, W."]
    year: 2020
    doi: null
    url: "https://arxiv.org/abs/2006.03654"
    arxiv_id: "2006.03654"
  - title: "SCROLLS: Standardized comparison over long language sequences"
    authors: ["Shaham, U.", "Segal, E.", "Ivgi, M.", "Efrat, A.", "Yoran, O.", "Haviv, A.", "Gupta, A.", "Xiong, W.", "Geva, M.", "Berant, J."]
    year: 2022
    doi: null
    url: "https://arxiv.org/abs/2201.03533"
    arxiv_id: "2201.03533"
  - title: "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena"
    authors: ["Zheng, L.", "Chiang, W.-L.", "Sheng, Y.", "Zhuang, S.", "Wu, Z.", "Zhuang, Y.", "Lin, Z.", "Li, Z.", "Li, D.", "Xing, E."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2306.05685"
    arxiv_id: "2306.05685"
  - title: "Efficient transformers: A survey"
    authors: ["Tay, Y.", "Dehghani, M.", "Bahri, D.", "Metzler, D."]
    year: 2022
    doi: "10.1145/3530811"
    url: null
    arxiv_id: null
  - title: "CoLT5: Faster long-range transformers with conditional computation"
    authors: ["Ainslie, J.", "Lei, T.", "de Jong, M.", "Ontanon, S.", "Brahma, S.", "Zemlyanskiy, Y.", "Uthus, D.", "Guo, M.", "Lee-Thorp, J.", "Tay, Y.", "Sung, Y.-H.", "Sanghai, S."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2303.09752"
    arxiv_id: "2303.09752"
  - title: "LongT5: Efficient text-to-text transformer for long sequences"
    authors: ["Guo, M.", "Ainslie, J.", "Uthus, D.", "Ontanon, S.", "Ni, J.", "Sung, Y.-H.", "Yang, Y."]
    year: 2022
    doi: "10.18653/v1/2022.findings-naacl.55"
    url: "https://arxiv.org/abs/2112.07916"
    arxiv_id: "2112.07916"
  - title: "Multimodal web navigation with instruction-finetuned foundation models"
    authors: ["Furuta, H.", "Lee, K.-H.", "Nachum, O.", "Matsuo, Y.", "Faust, A.", "Gu, S. S.", "Gur, I."]
    year: 2024
    doi: null
    url: "https://openreview.net/forum?id=efFmBWioSc"
    arxiv_id: null
  - title: "Language model agents suffer from compositional generalization in web automation"
    authors: ["Furuta, H.", "Matsuo, Y.", "Faust, A.", "Gur, I."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2311.18751"
    arxiv_id: "2311.18751"
  - title: "World of bits: An open-domain platform for web-based agents"
    authors: ["Shi, T.", "Karpathy, A.", "Fan, L.", "Hernandez, J.", "Liang, P."]
    year: 2017
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models can solve computer tasks"
    authors: ["Kim, G.", "Baldi, P.", "McAleer, S."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2303.17491"
    arxiv_id: "2303.17491"
  - title: "Vicuna: An open-source chatbot impressing GPT-4 with 90% ChatGPT quality"
    authors: ["Chiang, W.-L.", "Li, Z.", "Lin, Z.", "Sheng, Y.", "Wu, Z.", "Zhang, H.", "Zheng, L.", "Zhuang, S.", "Zhuang, Y.", "Gonzalez, J. E.", "Stoica, I.", "Xing, E. P."]
    year: 2023
    doi: null
    url: null
    arxiv_id: null
  - title: "Instruction tuning with GPT-4"
    authors: ["Peng, B.", "Li, C.", "He, P.", "Galley, M.", "Gao, J."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2304.03277"
    arxiv_id: "2304.03277"
  - title: "Can large language models be an alternative to human evaluations?"
    authors: ["Chiang, C.-H.", "Lee, H.-y."]
    year: 2023
    doi: "10.18653/v1/2023.acl-long.870"
    url: null
    arxiv_id: null
  - title: "Fuzzy-trace theory: Some foundational issues"
    authors: ["Reyna, V.", "Brainerd, C."]
    year: 1995
    doi: null
    url: null
    arxiv_id: null
  - title: "A new intuitionism: Meaning, memory, and development in fuzzy-trace theory"
    authors: ["Reyna, V. F."]
    year: 2012
    doi: null
    url: null
    arxiv_id: null
  - title: "A theory of medical decision making and health: fuzzy trace theory"
    authors: ["Reyna, V. F."]
    year: 2008
    doi: null
    url: null
    arxiv_id: null
  - title: "LLM Maybe LongLM: Self-extend LLM context window without tuning"
    authors: ["Jin, H.", "Han, X.", "Yang, J.", "Jiang, Z.", "Liu, Z.", "Chang, C.-Y.", "Chen, H.", "Hu, X."]
    year: 2024
    doi: null
    url: "https://arxiv.org/abs/2401.01325"
    arxiv_id: "2401.01325"
---

# A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts

**Authors:** Kuang-Huei Lee, Xinyun Chen, Hiroki Furuta, John Canny, Ian Fischer (Google DeepMind)
**Published:** 2024-02 (ICML 2024 / arXiv v3 Jul 2024) · [Source](https://arxiv.org/abs/2402.09727)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

ReadAgent is a zero-shot prompting system that lets a fixed-context LLM act on documents up to ~20x longer than its window. Inspired by fuzzy-trace theory from human cognition (Reyna and Brainerd, 1995), it operates in three steps: (1) **episode pagination** — the LLM itself decides where to split contiguous text into "pages" based on natural breakpoints (scene transitions, dialogue ends, narrative shifts); (2) **memory gisting** — each page is independently compressed into a short gist via a "shorten" prompt (deliberately not "summarize," which restructures); (3) **interactive look-up** — given a task plus the full set of contextualized gists, the LLM selects which page(s) it wants to re-read verbatim, and answers using gists + expanded pages combined. Evaluated on QuALITY (multiple-choice over ~6k-word articles), NarrativeQA (free-form QA over books and movie scripts averaging 71k words, max 343k words), and QMSum (meeting-transcript summarization, up to 26k words) with PaLM 2-L (8K context), ReadAgent outperforms BM25/Gemini-neural retrieval baselines, the full-context baseline (where it fits), gist-only, and a re-implemented MemWalker tree-traversal baseline (66.7% vs ReadAgent-S 87.2% on QuALITY). On NarrativeQA Gutenberg the effective-context expansion is ~20x. A parallel look-up variant (ReadAgent-P) is cheap; a sequential variant (ReadAgent-S) is more accurate but up to 6x more expensive. Pagination is shown to be materially better when LLM-driven than when uniform-length. Extension to Mind2Web web navigation beats MindAct (PaLM 2-L) even without a trained retriever.

## Key Takeaway

Treating an LLM as a reader that paginates a long document into natural episodes, gists each page, and then interactively looks up the few pages it needs to answer a task beats both full-context use and dense retrieval — extending effective context up to 20x with zero training. The non-obvious move is that the gist memory both serves as the database that the LLM "retrieves" from (by selecting page numbers) AND as the surrounding global context that frames the retrieved verbatim pages — neither pure RAG (which loses global context) nor pure summarization (which loses verbatim detail) achieves this. The result on QuALITY (86.91% ReadAgent-P vs 85.83% full text vs 84.42% BM25 Top-4) shows that even when the full document fits in context, prompting the model to read selectively beats prompting it to read everything — because long context dilutes signal and adds distractors (Liu et al., 2023; Shi et al., 2023). The architecture is a procedural-memory pattern: the LLM is given a *reading procedure*, not a static memory store.

## Implications

- **For long-context LLM systems**: even after frontier models reach million-token windows, ReadAgent-style selective reading remains useful because (a) full-context performance still degrades with length (the "lost in the middle" effect), (b) gist-memory caching amortizes preprocessing across many queries about the same document (the paper shows 20.4% token savings on QuALITY when answering 2,086 questions across 230 articles with 1-to-2-page lookup), and (c) it works on top of any LLM via prompting only — no training, no architecture change.

- **For RAG system designers**: the explicit competition is against BM25 and dense embedding retrieval (Gemini embeddings) over the *same* set of pages. ReadAgent wins because the LLM's page-selection prompt sees the full set of gists, giving it global context that an embedding-similarity ranker cannot exploit. The case study on the short story "off course" (Appendix D) shows neural retrieval picking distractor pages that ReadAgent correctly avoids using global context. Implication: if your RAG database is small enough that the gist memory fits in context, LLM-as-retriever may dominate embedding-retrieval. The crossover point depends on context length growth vs database size growth.

- **For agentic memory architectures**: the contextualized gist (page-number-tagged short summary, concatenated and ordered) is a lightweight episodic-memory primitive. Unlike hierarchical summary trees (MemWalker, RAPTOR), the flat-but-contextualized layout preserves cross-distance reasoning — the LLM sees gist of page 1 and gist of page N in the same prompt and can connect them. Implication for [[chen-2023-memwalker]]-style hierarchical-summary systems: the flat episodic gist memory is competitive or better, with 0% search-failure rate vs MemWalker's ~8-12% failure rate on QuALITY.

- **For Flow OS / second-brain systems**: the pagination prompt is genuinely useful — it's a reusable primitive for chunking long captures (transcripts, papers, books) at semantic boundaries rather than fixed word counts. The "shorten" vs "summarize" finding (shorten preserves narrative flow; summarize restructures) is a small but real prompt-engineering pattern.

- **For long-document agentic web navigation**: ReadAgent generalizes beyond reading comprehension. The Mind2Web results (Appendix E) show 33.4% step success rate on cross-domain with no domain-specific training — outperforming MindAct (PaLM 2-L) with a trained DeBERTa Rank-LM (24.5%). Implication: gist + lookup may be a general procedural pattern for any "long-text decision-making" task, not just QA.

- **Hallucination risk acknowledged but not measured**: the authors explicitly flag (Impact Statement) that working from gists rather than full text may *increase* hallucination — the model may invent details that are elided. They do not study this empirically, which is a real gap for production deployment.

## How to Apply It (method)

Build it as three sequential LLM-prompt stages plus a final answer prompt:

**Stage 1 — Episode Pagination.** Walk through the document in windows from `min_words` to `max_words`. After `min_words`, insert numbered tags `<5>`, `<6>`, `<7>`, ... between paragraphs. Prompt the LLM: "Please choose a label where it is natural to break reading. The label can be a scene transition, the end of a dialogue, the end of an argument, a narrative transition, etc." Parse the chosen label, treat content up to that point as one page, then continue from there. Hyperparameter values from the paper: QuALITY/QMSum `min/max = 280/600`; NarrativeQA Gutenberg `500/3000`; NarrativeQA movie scripts `600/1000` (Appendix C, Table 8).

**Stage 2 — Memory Gisting.** For each page, prompt: "Please shorten the following passage. Just give me a shortened version. DO NOT explain your reason. Passage: {PAGE TEXT}". Critically, use "shorten" not "summarize" — the paper finds "summarize" restructures while "shorten" preserves narrative flow, which matters for downstream concatenation. Prepend a tag like `<Page 2>\n{GIST}` to contextualize each gist. Concatenate all tagged gists in document order to form the gist memory.

**Stage 3 — Interactive Look-up.** Two variants:
- **ReadAgent-P (parallel):** "You may read 1 to N pages... Please respond with which page(s) you would like to read. For example, if you only need to read Page 8, respond with 'I want to look up Page [8] to ...'" Replace the gists at those positions with the raw pages, then issue the answer prompt.
- **ReadAgent-S (sequential):** Ask one page at a time, showing previously-expanded pages, until model says "STOP" or hits a cap. ~6x more LLM calls but +0.3-7% accuracy depending on dataset.

**Final answer.** With the (gist + expanded pages) text in context, prompt for the answer. For free-form tasks: "Answer the question based on the above passage and retrieved pages. Your answer should be short and concise." For multiple choice: standard "Answer: (C) ..." pattern.

**Extensions worth implementing:**
- Conditional gisting (Appendix G.1): include the task in the gisting prompt for higher compression at cost of single-use gists.
- Iterative gisting (Appendix G.3): re-gist older memory pages when context grows arbitrarily long (relevant for assistant agents with long histories).
- Page-merging pass (Appendix I): when gists themselves exceed context, ask the LLM "does Page 2 start a new chapter different from Page 1?" and merge if no — used for the largest NarrativeQA documents.

**Cost model.** Pagination consumes at most `max_words / min_words` document-passes (so ~2.1x for QuALITY settings). Gisting is one extra pass. Look-up + response operate on gists (much shorter than raw) plus a small number of expanded pages. When the same document is reused across many tasks (e.g. 230 articles × 9 questions each in QuALITY), total token consumption *drops* below full-context baseline: 8.7M words full-text vs 6.5M ReadAgent-1pg = 25.4% saving.

**Failure modes to monitor.** The Impact Statement flags that gists elide details, so the model may hallucinate when answering questions whose answer was elided. Build a sanity-check pass that verifies model claims against the verbatim retrieved pages, especially for factual extraction tasks.

## Best Figure

![Figure 1 — ReadAgent workflow (Episode Pagination -> Gisting -> Interactive Lookup) (page 1)](figures/lee-2024-readagent-gist-memory-fig.png)

Figure 1 is the load-bearing schematic of the paper: a very long input text on the left flows into "1. Episode Pagination" producing pages 1..N, then "2. Gisting" produces an Episodic Gist Memory of one short gist per page (tagged with `[page k] gist`). On the right, a robot agent issues a query ("Why did John ... ?") and "3. Lookup" — choosing which pages to re-expand from raw text — feeds the answer.

Why this figure is the right choice: it's the only figure in the paper that compresses the whole method into a single picture, and crucially it shows the three-step process as a *loop with persistent memory* (the gist memory is reused across queries) rather than a one-shot pipeline. The chained labels (1 Pagination -> 2 Gisting -> 3 Lookup) map exactly onto the three sections of Method (3.1, 3.1, 3.2). Every other figure in the paper is a histogram of word-counts (Figures 2, 3, 4, 5, 7, 8) or a token-distribution chart (Figure 6) — useful but not narratively load-bearing.

What's interesting in it that the prose doesn't make obvious: the gist memory is drawn as a *separate persistent object* outside the document flow. That visual separation is exactly the architectural argument — the gist memory is a re-usable artifact, not a per-query computation. The fact that the robot can issue *multiple* queries against the *same* gist memory is what makes the amortized-cost numbers in Section 3.3 work (the 25.4% saving on QuALITY across 2,086 questions over 230 articles).

What the figure omits and is worth knowing: it does not depict the choice between ReadAgent-P (parallel page selection in one prompt) and ReadAgent-S (sequential one-at-a-time). It also does not show that during Lookup, the retrieved raw pages *replace* the corresponding gists in the prompt to preserve narrative ordering — the figure suggests they are appended, but the actual prompt structure interleaves them.

## What Experts Overlook

A reader steeped in long-context LLM literature would likely skim this paper as "yet another RAG variant" and miss several non-obvious findings:

1. **The full-context baseline is not the ceiling.** On QuALITY, where articles fit in PaLM 2-L's 8K window, ReadAgent-P (Look up 1-6 pgs) at 86.91% accuracy *beats* Full Raw Content at 85.83%. This is the "lost in the middle" effect (Liu et al., 2023) showing up in a clean, controlled comparison: even when you can shove everything into context, gisting + selective re-reading produces better answers because it reduces distractors. Most papers benchmarking long-context methods present full-context as an unattainable upper bound; this one quietly shows it can be exceeded.

2. **"Shorten" vs "summarize" is a real, replicable prompt-engineering finding.** Section 3.1: "Using the word 'summarize' tended to produce a restructured summary in our experiments." The choice of verb in the gisting prompt materially affects whether the concatenated gist memory reads as continuous narrative or as a fragmented list of summary blocks. This is the kind of finding that compounds across the field and rarely gets cited.

3. **LLM-chosen pagination beats uniform pagination by ~1.1%** on QuALITY (Table 5: 86.83% vs 85.71%). This is a small absolute number but conceptually important — it says the *boundaries* matter, not just the content within them. Most chunking pipelines (LangChain default, etc.) use fixed-size windows; this paper says fixed-size leaves performance on the table. Adoption is rare because LLM-driven pagination costs more inference, but for stable corpora (papers, books) it's amortized to zero.

4. **MemWalker comparison reveals tree-search fragility.** Table H comparison: re-implemented MemWalker hits 66.73% on QuALITY vs ReadAgent-S 86.88% — a 20-point gap. Crucially the paper reports MemWalker's 11.7% search-failure-rate (LLM gets lost in the tree and doesn't terminate), vs ReadAgent's ~0%. This is a quiet but devastating result for hierarchical-summary memory architectures: the tree-traversal acts like a controlled-failure mode whereas flat-but-contextualized gist memory degrades gracefully.

5. **Gist memory dominates retrieval *even without* lookups on NarrativeQA.** Table 2: GistMem alone (no lookup) hits 55.31% LR-1 on Gutenberg validation, vs the best retrieval baseline (BM25 Top-4) at 53.59%. So *just compressing into gist memory* is competitive with retrieval — the lookup is icing. Implication: for tasks that don't need exact-detail recall, gist memory alone is a deployable solution at one full-document pass of cost.

6. **The "save tokens by reusing gist memory" argument is real.** Section 3.3: directly answering QuALITY's 2,086 questions over 230 articles consumes 8.71M words full-text vs 6.50M for ReadAgent-1pg lookup — a 25.4% saving. Most "RAG vs long context" cost analyses don't model multi-query reuse this way, treating each query as standalone. The amortization story is what makes gist-memory production-deployable, not the per-query accuracy.

7. **The hallucination risk acknowledged in Impact Statement is unmeasured.** "It is possible that ReadAgent could cause greater harms... an increased tendency of the LLM to hallucinate when working with gist memories rather than full text." The authors flag this and explicitly note it was not studied. For 2026-era production deployment this is the most important open question — has any follow-up paper benchmarked this? (My guess: not directly; the field moved on to RAPTOR/HiPPO-RAG/MemoryBank variants without revisiting the hallucination-from-gist question.)

8. **Mind2Web web-navigation extension (Appendix E) is buried.** Most readers stop at Section 5. The Mind2Web results are a more striking generalization claim than the QA results — using gists of HTML snippets rather than text pages, ReadAgent-P (1-5 snippets) hits 33.4% cross-domain step-SR vs MindAct (PaLM 2-L + trained Rank-LM) at 24.5%. This says gist-based selective reading is a *general procedural pattern* for long-context decision-making, not a QA-specific trick. Buried-in-appendix findings often turn out to be the most consequential follow-up directions.

## Extracted Prompts

The paper publishes complete prompts in the body and Appendix F. The most reusable ones, lifted verbatim or near-verbatim:

**Pagination prompt** (Section 3.1):
```
You are given a passage that is taken from a larger text (article, book, ...)
and some numbered labels between the paragraphs in the passage.
Numbered labels are in angle brackets. For example, if the label number is 19,
it shows as <19> in text.
Please choose a label where it is natural to break reading.
The label can be a scene transition, the end of a dialogue, the end of an
argument, a narrative transition, etc.
Please answer with the break point label and explain.

For example, if <57> is a good point to break, answer with
"Break point: <57>\n Because ..."

Passage:
{...}
{PARAGRAPH 5 TEXT}
<5>
{PARAGRAPH 6 TEXT}
<6>
{PARAGRAPH 7 TEXT}
{...}
```

**Gisting prompt** (Section 3.1):
```
Please shorten the following passage.
Just give me a shortened version. DO NOT explain your reason.
Passage:
{PAGE TEXT}
```

**Parallel lookup prompt (ReadAgent-P)** (Section 3.2):
```
The following text is what you remember from reading an article and a
multiple choice question related to it.
You may read 1 to 5 page(s) of the article again to refresh your memory to
prepare yourself for the question.
Please respond with which page(s) you would like to read.

For example, if you only need to read Page 8, respond with "I want to look up
Page [8] to ..."; if you would like to read Page 7 and 12, respond with "I
want to look up Page [7, 12] to ..."; ...
DO NOT select more pages if you don't need to.
You don't need to answer the question yet.
Text:
{GIST MEMORY}
Question:
{QUESTION}
```

**Sequential lookup prompt (ReadAgent-S)** (Section 3.2):
```
The following text is what you remember from reading a meeting transcript,
followed by a question about the transcript.
You may read multiple pages of the transcript again to refresh your memory
and prepare to answer the question.
Each page that you re-read can significantly improve your chance of
answering the question correctly.
Please specify a SINGLE page you would like to read again or say "STOP".
To read a page again, respond with "Page $PAGE_NUM", replacing $PAGE_NUM
with the target page number.
You can only specify a SINGLE page in your response at this time.
To stop, simply say "STOP". DO NOT answer the question in your response.
Text:
{GISTS WITH IN-LINE EXPANDED PAGES}
Pages re-read already (DO NOT ask to read them again):
{LIST OF PAGE NUMBERS ALREADY READ}
Question:
{QUESTION}
Specify a SINGLE page to read again, or say STOP:
```

**Page-merging prompt (NarrativeQA, Appendix I)** — useful when gists themselves exceed context:
```
Given Page 1 and Page 2, please tell me whether Page 2 starts a new
chapter/section/book that is different from what's in Page 1.
Please answer with yes, no, or not sure.
Page 1:
{PREVIOUS PAGE TEXT}
Page 2:
{CURRENT PAGE TEXT}
```

**QuALITY look-up sharpener** (Appendix F): appending "Take a deep breath and tell me: Which page(s) would you like to read again?" at the end of the look-up prompt improved response quality on PaLM 2-L and GPT-3.5 — same family of finding as Yang et al. (2023) "large language models as optimizers."

**LLM Rater prompts** (Section 4.1): strict and permissive variants for evaluating free-form answers against references. Notable design choice — they use "John's answer" rather than "Assistant's answer" because it pushes the judge into a more objective third-person stance.

## Citations

Top citations to follow first when extending this work:

- [[chen-2023-memwalker]] — **MemWalker**, the direct predecessor that uses a hierarchical summary tree. ReadAgent's Appendix H explicitly contrasts the two and finds ReadAgent's flat-contextualized gists beat MemWalker's tree by ~20 points on QuALITY with 0% vs 11.7% search-failure-rate.
- Liu et al. 2023, "Lost in the middle" (arxiv 2307.03172) — the empirical foundation for "even when full context fits, performance degrades with length." Required reading to understand why ReadAgent can beat full-context baselines.
- Shi et al. 2023, "Large language models can be easily distracted by irrelevant context" (PMLR/arxiv 2302) — the second pillar of the "less is more" argument. Distracting passages hurt LLMs; gisting reduces them.
- Lewis et al. 2020, "Retrieval-Augmented Generation" (arxiv 2005.11401) — the RAG baseline architecture ReadAgent positions itself against.
- Reyna and Brainerd 1995, "Fuzzy-trace theory" — the cognitive-science source of the gist/verbatim distinction. The paper is genuinely well-grounded here rather than using it as window-dressing.
- Wu et al. 2021, "Recursively summarizing books with human feedback" (arxiv 2109.10862) — the closest competitor for long-document reading from the alignment/RLHF side.
- Sun et al. 2023, "PEARL" (arxiv 2305.14564) — action-planning over long documents through iterative prompting; complementary to ReadAgent's reading-only stance.
- Lanchantin et al. 2023, "Self-notes" (arxiv 2305.00833) — interleaves intermediate notes with documents; conceptually related to gisting.
- Kočiský et al. 2018, "NarrativeQA" — the hardest benchmark (343k-word documents) ReadAgent runs on, and the strongest demonstration of the 20x effective-context expansion.
- Pang et al. 2022, "QuALITY" — the cleanest dataset for the "even when it fits, gisting wins" finding.

(Full citation list of ~50 entries in frontmatter `citations:`.)

## Related Digests

- [[chen-2023-memwalker]] — Walking down the memory maze: the explicit baseline that ReadAgent contrasts with (hierarchical summary tree vs flat contextualized gist memory).
- [[dorsey-2026-dgmm-gist-memory]] — Dynamic Gist-Based Memory Model (DGMM), a 2026 follow-up that extends the gist-memory concept to a full memory-centric AI architecture.
- [[sun-2025-hmem-hierarchical-memory]] — H-MEM, hierarchical memory for high-efficiency long-term reasoning in LLM agents; complement/competitor to ReadAgent's flat gist memory.
- [[sarthi-2024-raptor]] — RAPTOR's recursive abstractive processing for tree-organized retrieval; conceptually adjacent to both MemWalker and ReadAgent.
- [[chhikara-2025-mem0]] — Mem0 production-ready agent memory; cites ReadAgent in its long-term memory comparison.

## Reviewer Notes

Hallucination check (paper-vs-digest consistency, evaluated 2026-05-20):

- **Severity: Clean.** All numbers, claims, prompt texts, and structural details in this digest map directly onto the paper's text. Spot checks performed:
  - QuALITY accuracy 86.91% for ReadAgent-P (Look up 1-6 pgs): matches Table 1.
  - Compression rate 72.17% for ReadAgent-P (Look up 1-2 pgs) on QuALITY: matches Table 1.
  - Full Raw Content QuALITY: 85.83% — matches Table 1.
  - MemWalker re-implementation on QuALITY: 66.73% accuracy, 11.7% search-failure-rate: matches Appendix H.
  - NarrativeQA Gutenberg average 71k words / max 343k words: paper says "70,619 words on average, and the maximum is 343,910 words" — digest rounded correctly.
  - QuALITY 25.4% / 20.4% / 13.8% token savings for 1pg / 1-2pg / 1-5pg lookup: matches Section 3.3 directly.
  - "Shorten vs summarize" finding: paper Section 3.1 explicitly says "Using the word 'summarize' tended to produce a restructured summary" — digest captures this accurately.
  - Pagination hyperparameters in Table 8: digest reports QuALITY/QMSum 280/600, NarrativeQA Gutenberg 500/3000, NarrativeQA movie 600/1000 — all match.
  - Mind2Web cross-domain step-SR: ReadAgent-P (1-5 snippets) 33.4%, MindAct (PaLM 2-L + Rank LM) 24.5% — matches Table 10.
  - Hallucination acknowledgement in Impact Statement: digest paraphrases the paper's own quoted concern; the paper does explicitly flag this and does not study it.
  - 20x effective-context expansion claim: paper abstract says "20×" and Section 4.3.2 says "approximately 20x" for NarrativeQA Gutenberg — claim is grounded.
- **No fabricated citations.** All entries in the related-papers list (chen-2023-memwalker, dorsey-2026-dgmm-gist-memory, etc.) were verified to exist in the wiki via QMD search before insertion.
- **Caveats flagged in body**: the hallucination risk is acknowledged in the paper but not measured — this is correctly noted as an open question in the digest, not a paper finding.
