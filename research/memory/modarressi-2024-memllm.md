---
corpus: agentic-memory
kind: paper-digest
slug: modarressi-2024-memllm
title: "MemLLM: Finetuning LLMs to Use an Explicit Read-Write Memory"
authors:
  - "Modarressi, Ali"
  - "Köksal, Abdullatif"
  - "Imani, Ayyoob"
  - "Fayyaz, Mohsen"
  - "Schütze, Hinrich"
year: 2024
publication_date: "2024-04"
venue: "Transactions on Machine Learning Research (04/2025)"
source_url: "https://arxiv.org/abs/2404.11672"
doi: null
arxiv_id: "2404.11672"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "MemLLM is the empirical follow-up to Ret-LLM: fine-tune two Mistral-7B LoRA adapters — a Memory-Write model that emits ({MEM_WRITE-->subj»rel»obj}) tokens to populate a structured Wikidata-style triple store (111M triples → only 21M unique entity/relation vectors, ~19% the storage of proposition-RAG), and a Memory-Read model that auto-injects ({MEM_READ(...)-->...}) calls mid-decoding to retrieve facts before generating target entities — yielding a 15% TARGET-PPL drop versus the base Mistral-7B (3.550 → 2.986) and beating WISE/GRACE/DEFER on 1000 sequential ZsRE edits (AVG 0.84 vs 0.79 best baseline), all without architectural changes."
topics:
  - explicit-memory
  - read-write-memory
  - triplet-memory
  - memory-api
  - knowledge-editing
  - lora-finetuning
  - memory-write
  - memory-read
  - structured-memory
  - relation-extraction
  - re-docred
  - wikidata
  - perplexity-evaluation
  - sequential-editing
tags:
  - paper
  - memory-architecture
  - external-memory
  - tool-use
  - fine-tuning
  - retrieval
  - knowledge-editing
  - structured-storage
entities:
  - modarressi-ali
  - koksal-abdullatif
  - imani-ayyoob
  - fayyaz-mohsen
  - schutze-hinrich
related_digests:
  - modarressi-2023-ret-llm
  - graves-2014-neural-turing-machines
  - sun-2025-hmem-hierarchical-memory
  - xu-2025-a-mem-agentic-memory
  - liu-2023-think-in-memory
  - chhikara-2025-mem0
  - mao-2026-agent-memory-circuits
citations:
  - title: "Knowledge-Augmented Language Model Prompting for Zero-Shot Knowledge Graph Question Answering"
    authors: ["Jinheon Baek", "Alham Fikri Aji", "Amir Saffari"]
    year: 2023
    venue: "MATCHING 2023"
    doi: null
    url: "https://api.semanticscholar.org/CorpusID:260063238"
    arxiv_id: null
  - title: "Recurrent Memory Transformer"
    authors: ["Aydar Bulatov", "Yuri Kuratov", "Mikhail Burtsev"]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: "https://openreview.net/forum?id=Uynr3iPhksa"
    arxiv_id: null
  - title: "Memory Transformer"
    authors: ["Mikhail S Burtsev", "Yuri Kuratov", "Anton Peganov", "Grigory V Sapunov"]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2006.11527"
  - title: "Walking down the Memory Maze: Beyond Context Limit through Interactive Reading"
    authors: ["Howard Chen", "Ramakanth Pasunuru", "Jason Weston", "Asli Celikyilmaz"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.05029"
  - title: "Dense X Retrieval: What Retrieval Granularity Should We Use?"
    authors: ["Tong Chen", "Hongwei Wang", "Sihao Chen", "et al."]
    year: 2024
    venue: "EMNLP 2024"
    doi: "10.18653/v1/2024.emnlp-main.845"
    url: "https://aclanthology.org/2024.emnlp-main.845"
    arxiv_id: null
  - title: "Lift Yourself Up: Retrieval-Augmented Text Generation with Self-Memory"
    authors: ["Xin Cheng", "Di Luo", "Xiuying Chen", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: "https://openreview.net/forum?id=lYNSvp51a7"
    arxiv_id: null
  - title: "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation"
    authors: ["Kyunghyun Cho", "Bart van Merriënboer", "Caglar Gulcehre", "et al."]
    year: 2014
    venue: "EMNLP 2014"
    doi: "10.3115/v1/D14-1179"
    url: "https://aclanthology.org/D14-1179"
    arxiv_id: null
  - title: "PaLM: Scaling Language Modeling with Pathways"
    authors: ["Aakanksha Chowdhery", "Sharan Narang", "Jacob Devlin", "et al."]
    year: 2023
    venue: "Journal of Machine Learning Research, 24(240):1-113"
    doi: null
    url: "http://jmlr.org/papers/v24/22-1144.html"
    arxiv_id: null
  - title: "Knowledge Neurons in Pretrained Transformers"
    authors: ["Damai Dai", "Li Dong", "Yaru Hao", "et al."]
    year: 2022
    venue: "ACL 2022"
    doi: "10.18653/v1/2022.acl-long.581"
    url: "https://aclanthology.org/2022.acl-long.581"
    arxiv_id: null
  - title: "Editing Factual Knowledge in Language Models"
    authors: ["Nicola De Cao", "Wilker Aziz", "Ivan Titov"]
    year: 2021
    venue: "EMNLP 2021"
    doi: "10.18653/v1/2021.emnlp-main.522"
    url: "https://aclanthology.org/2021.emnlp-main.522"
    arxiv_id: null
  - title: "Model Editing Can Hurt General Abilities of Large Language Models"
    authors: ["Jia-Chen Gu", "Hao-Xiang Xu", "Jun-Yu Ma", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2401.04700"
  - title: "REALM: Retrieval-Augmented Language Model Pre-training"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."]
    year: 2020
    venue: "ICML 2020"
    doi: null
    url: null
    arxiv_id: null
  - title: "Aging with Grace: Lifelong Model Editing with Discrete Key-Value Adaptors"
    authors: ["Thomas Hartvigsen", "Swami Sankaranarayanan", "Hamid Palangi", "et al."]
    year: 2024
    venue: "NeurIPS 36"
    doi: null
    url: null
    arxiv_id: null
  - title: "CAMELoT: Towards Large Language Models with Training-Free Consolidated Associative Memory"
    authors: ["Zexue He", "Leonid Karlinsky", "Donghyun Kim", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.13449"
  - title: "Long Short-Term Memory"
    authors: ["Sepp Hochreiter", "Jürgen Schmidhuber"]
    year: 1997
    venue: "Neural Computation 9(8):1735-1780"
    doi: "10.1162/neco.1997.9.8.1735"
    url: null
    arxiv_id: null
  - title: "ChatDB: Augmenting LLMs with Databases as Their Symbolic Memory"
    authors: ["Chenxu Hu", "Jie Fu", "Chenzhuang Du", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2306.03901"
  - title: "LoRA: Low-Rank Adaptation of Large Language Models"
    authors: ["Edward J Hu", "Yelong Shen", "Phillip Wallis", "et al."]
    year: 2022
    venue: "ICLR 2022"
    doi: null
    url: "https://openreview.net/forum?id=nZeVKeeFYf9"
    arxiv_id: null
  - title: "Transformer-Patcher: One Mistake Worth One Neuron"
    authors: ["Zeyu Huang", "Yikang Shen", "Xiaofeng Zhang", "et al."]
    year: 2023
    venue: "ICLR 2023"
    doi: null
    url: "https://openreview.net/forum?id=4oYUGeGBPm"
    arxiv_id: null
  - title: "Unsupervised Dense Information Retrieval with Contrastive Learning (Contriever)"
    authors: ["Gautier Izacard", "Mathilde Caron", "Lucas Hosseini", "et al."]
    year: 2022
    venue: "TMLR"
    doi: null
    url: "https://openreview.net/forum?id=jKN1pXi7b0"
    arxiv_id: null
  - title: "TemporalWiki: A Lifelong Benchmark for Training and Evaluating Ever-Evolving Language Models"
    authors: ["Joel Jang", "Seonghyeon Ye", "Changho Lee", "et al."]
    year: 2022
    venue: "EMNLP 2022"
    doi: "10.18653/v1/2022.emnlp-main.418"
    url: "https://aclanthology.org/2022.emnlp-main.418"
    arxiv_id: null
  - title: "Repeat After Me: Transformers are Better than State Space Models at Copying"
    authors: ["Samy Jelassi", "David Brandfonbrener", "Sham M Kakade", "Eran Malach"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.01032"
  - title: "Survey of Hallucination in Natural Language Generation"
    authors: ["Ziwei Ji", "Nayeon Lee", "Rita Frieske", "et al."]
    year: 2023
    venue: "ACM Computing Surveys 55(12):1-38"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mistral 7B"
    authors: ["Albert Q Jiang", "Alexandre Sablayrolles", "Arthur Mensch", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.06825"
  - title: "Large Language Models Struggle to Learn Long-Tail Knowledge"
    authors: ["Nikhil Kandpal", "Haikang Deng", "Adam Roberts", "et al."]
    year: 2023
    venue: "ICML 2023"
    doi: null
    url: null
    arxiv_id: null
  - title: "Realtime QA: What's the Answer Right Now?"
    authors: ["Jungo Kasai", "Keisuke Sakaguchi", "Yoichi Takahashi", "et al."]
    year: 2023
    venue: "NeurIPS Datasets and Benchmarks 2023"
    doi: null
    url: "https://openreview.net/forum?id=HfKOIPCvsv"
    arxiv_id: null
  - title: "Adam: A Method for Stochastic Optimization"
    authors: ["Diederik Kingma", "Jimmy Ba"]
    year: 2015
    venue: "ICLR 2015"
    doi: null
    url: null
    arxiv_id: null
  - title: "Natural Questions: A Benchmark for Question Answering Research"
    authors: ["Tom Kwiatkowski", "Jennimaria Palomaki", "Olivia Redfield", "et al."]
    year: 2019
    venue: "TACL 7:452-466"
    doi: "10.1162/tacl_a_00276"
    url: "https://aclanthology.org/Q19-1026"
    arxiv_id: null
  - title: "Zero-Shot Relation Extraction via Reading Comprehension (ZsRE)"
    authors: ["Omer Levy", "Minjoon Seo", "Eunsol Choi", "Luke Zettlemoyer"]
    year: 2017
    venue: "CoNLL 2017"
    doi: "10.18653/v1/K17-1034"
    url: "https://aclanthology.org/K17-1034"
    arxiv_id: null
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG)"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2020
    venue: "NeurIPS 33:9459-9474"
    doi: null
    url: null
    arxiv_id: null
  - title: "Enhancing Large Language Model with Self-Controlled Memory Framework"
    authors: ["Xinnian Liang", "Bing Wang", "Hui Huang", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2304.13343"
  - title: "Relational Memory-Augmented Language Models"
    authors: ["Qi Liu", "Dani Yogatama", "Phil Blunsom"]
    year: 2022
    venue: "TACL 10:555-572"
    doi: "10.1162/tacl_a_00476"
    url: "https://aclanthology.org/2022.tacl-1.32"
    arxiv_id: null
  - title: "When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories"
    authors: ["Alex Mallen", "Akari Asai", "Victor Zhong", "et al."]
    year: 2023
    venue: "ACL 2023"
    doi: "10.18653/v1/2023.acl-long.546"
    url: "https://aclanthology.org/2023.acl-long.546"
    arxiv_id: null
  - title: "∞-former: Infinite Memory Transformer"
    authors: ["Pedro Henrique Martins", "Zita Marinho", "Andre Martins"]
    year: 2022
    venue: "ACL 2022"
    doi: "10.18653/v1/2022.acl-long.375"
    url: "https://aclanthology.org/2022.acl-long.375"
    arxiv_id: null
  - title: "On Faithfulness and Factuality in Abstractive Summarization"
    authors: ["Joshua Maynez", "Shashi Narayan", "Bernd Bohnet", "Ryan McDonald"]
    year: 2020
    venue: "ACL 2020"
    doi: "10.18653/v1/2020.acl-main.173"
    url: "https://aclanthology.org/2020.acl-main.173"
    arxiv_id: null
  - title: "Locating and Editing Factual Associations in GPT (ROME)"
    authors: ["Kevin Meng", "David Bau", "Alex Andonian", "Yonatan Belinkov"]
    year: 2022
    venue: "NeurIPS 35:17359-17372"
    doi: null
    url: null
    arxiv_id: null
  - title: "Distant Supervision for Relation Extraction without Labeled Data"
    authors: ["Mike Mintz", "Steven Bills", "Rion Snow", "Daniel Jurafsky"]
    year: 2009
    venue: "ACL-IJCNLP 2009"
    doi: null
    url: "https://aclanthology.org/P09-1113"
    arxiv_id: null
  - title: "Fast Model Editing at Scale"
    authors: ["Eric Mitchell", "Charles Lin", "Antoine Bosselut", "et al."]
    year: 2021
    venue: "ICLR 2021"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory-Based Model Editing at Scale (SERAC)"
    authors: ["Eric Mitchell", "Charles Lin", "Antoine Bosselut", "et al."]
    year: 2022
    venue: "ICML 2022, PMLR 162:15817-15831"
    doi: null
    url: "https://proceedings.mlr.press/v162/mitchell22a.html"
    arxiv_id: null
  - title: "Ret-LLM: Towards a General Read-Write Memory for Large Language Models"
    authors: ["Ali Modarressi", "Ayyoob Imani", "Mohsen Fayyaz", "Hinrich Schütze"]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.14322"
  - title: "Consistent Document-Level Relation Extraction via Counterfactuals"
    authors: ["Ali Modarressi", "Abdullatif Köksal", "Hinrich Schütze"]
    year: 2024
    venue: "EMNLP Findings 2024"
    doi: "10.18653/v1/2024.findings-emnlp.672"
    url: "https://aclanthology.org/2024.findings-emnlp.672"
    arxiv_id: null
  - title: "MemGPT: Towards LLMs as Operating Systems"
    authors: ["Charles Packer", "Vivian Fang", "Shishir G Patil", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    authors: ["Joon Sung Park", "Joseph C O'Brien", "Carrie J Cai", "et al."]
    year: 2023
    venue: "UIST '23"
    doi: null
    url: null
    arxiv_id: null
  - title: "How Much Knowledge Can You Pack into the Parameters of a Language Model?"
    authors: ["Adam Roberts", "Colin Raffel", "Noam Shazeer"]
    year: 2020
    venue: "EMNLP 2020"
    doi: "10.18653/v1/2020.emnlp-main.437"
    url: "https://aclanthology.org/2020.emnlp-main.437"
    arxiv_id: null
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    authors: ["Timo Schick", "Jane Dwivedi-Yu", "Roberto Dessi", "et al."]
    year: 2023
    venue: "NeurIPS 2023"
    doi: null
    url: "https://openreview.net/forum?id=Yacmpz84TH"
    arxiv_id: null
  - title: "Large Language Models Can Be Easily Distracted by Irrelevant Context"
    authors: ["Freda Shi", "Xinyun Chen", "Kanishka Misra", "et al."]
    year: 2023
    venue: "ICML 2023, PMLR 31210-31227"
    doi: null
    url: null
    arxiv_id: null
  - title: "Editable Neural Networks"
    authors: ["Anton Sinitsin", "Vsevolod Plokhotnyuk", "Dmitry Pyrkin", "et al."]
    year: 2020
    venue: "ICLR 2020"
    doi: null
    url: "https://openreview.net/forum?id=HJedXaEtvS"
    arxiv_id: null
  - title: "Revisiting DocRED — Addressing the False Negative Problem in Relation Extraction (Re-DocRED)"
    authors: ["Qingyu Tan", "Lu Xu", "Lidong Bing", "et al."]
    year: 2022
    venue: "EMNLP 2022"
    doi: "10.18653/v1/2022.emnlp-main.580"
    url: "https://aclanthology.org/2022.emnlp-main.580"
    arxiv_id: null
  - title: "WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models"
    authors: ["Peng Wang", "Zexi Li", "Ningyu Zhang", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2405.14768"
  - title: "Augmenting Language Models with Long-Term Memory"
    authors: ["Weizhi Wang", "Li Dong", "Hao Cheng", "et al."]
    year: 2023
    venue: "NeurIPS 2023"
    doi: null
    url: "https://openreview.net/forum?id=BryMFPQ4L6"
    arxiv_id: null
  - title: "MemoryLLM: Towards Self-Updatable Large Language Models"
    authors: ["Yu Wang", "Xiusi Chen", "Jingbo Shang", "Julian McAuley"]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.04624"
  - title: "Interactive Natural Language Processing"
    authors: ["Zekun Wang", "Ge Zhang", "Kexin Yang", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.13246"
  - title: "Memformer: A Memory-Augmented Transformer for Sequence Modeling"
    authors: ["Qingyang Wu", "Zhenzhong Lan", "Kun Qian", "et al."]
    year: 2022
    venue: "AACL-IJCNLP Findings 2022"
    doi: null
    url: "https://aclanthology.org/2022.findings-aacl.29"
    arxiv_id: null
  - title: "Memorizing Transformers"
    authors: ["Yuhuai Wu", "Markus Norman Rabe", "DeLesley Hutchins", "Christian Szegedy"]
    year: 2022
    venue: "ICLR 2022"
    doi: null
    url: "https://openreview.net/forum?id=TrjbxzRcnf-"
    arxiv_id: null
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    authors: ["Shunyu Yao", "Jeffrey Zhao", "Dian Yu", "et al."]
    year: 2023
    venue: "ICLR 2023"
    doi: null
    url: "https://openreview.net/forum?id=WE_vluYUL-X"
    arxiv_id: null
  - title: "DocRED: A Large-Scale Document-Level Relation Extraction Dataset"
    authors: ["Yuan Yao", "Deming Ye", "Peng Li", "et al."]
    year: 2019
    venue: "ACL 2019"
    doi: "10.18653/v1/P19-1074"
    url: "https://aclanthology.org/P19-1074"
    arxiv_id: null
  - title: "Editing Large Language Models: Problems, Methods, and Opportunities"
    authors: ["Yunzhi Yao", "Peng Wang", "Bozhong Tian", "et al."]
    year: 2023
    venue: "EMNLP 2023"
    doi: "10.18653/v1/2023.emnlp-main.632"
    url: "https://aclanthology.org/2023.emnlp-main.632"
    arxiv_id: null
  - title: "Generate Rather Than Retrieve: Large Language Models are Strong Context Generators"
    authors: ["Wenhao Yu", "Dan Iter", "Shuohang Wang", "et al."]
    year: 2023
    venue: "ICLR 2023"
    doi: null
    url: "https://openreview.net/forum?id=fB0hRu9GZUS"
    arxiv_id: null
  - title: "Extract, Define, Canonicalize: An LLM-Based Framework for Knowledge Graph Construction"
    authors: ["Bowen Zhang", "Harold Soh"]
    year: 2024
    venue: "EMNLP 2024"
    doi: null
    url: "https://aclanthology.org/2024.emnlp-main.548"
    arxiv_id: null
  - title: "A Comprehensive Study of Knowledge Editing for Large Language Models"
    authors: ["Ningyu Zhang", "Yunzhi Yao", "Bozhong Tian", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2401.01286"
  - title: "RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text"
    authors: ["Wangchunshu Zhou", "Yuchen Eleanor Jiang", "Peng Cui", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.13304"
  - title: "LLMs for Knowledge Graph Construction and Reasoning: Recent Capabilities and Future Opportunities (AutoKG)"
    authors: ["Yuqi Zhu", "Xiaohan Wang", "Jing Chen", "et al."]
    year: 2024
    venue: "World Wide Web 27(5):58"
    doi: "10.1007/S11280-024-01297-W"
    url: "https://doi.org/10.1007/s11280-024-01297-w"
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "MemLLM inference with memory read and memory write"
  page: 5
  image_path: "figures/modarressi-2024-memllm-fig.png"
---

# MemLLM: Finetuning LLMs to Use an Explicit Read-Write Memory

**Authors:** Modarressi, Köksal, Imani, Fayyaz, Schütze
**Published:** 2024-04 · [Source](https://arxiv.org/abs/2404.11672)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

MemLLM endows a Mistral-7B with two LoRA-fine-tuned heads — a Memory-Write head and a Memory-Read head — that share an external structured triple store (Wikidata-style ⟨subject, relation, object⟩ rows backed by Contriever vectors over entity and relation tables). At write time, the model scans sentences one-by-one and emits `({MEM_WRITE-->e1»t»e2;...})` API tokens whose payload populates the triple store; at read time, mid-decoding it can spontaneously emit `({MEM_READ(eq»t»;...)-->...})`, the controller catches the token, runs cosine-similarity retrieval over candidate entities and relations (with a τ_r averaged-similarity threshold), and appends the result back into the context as the next decoded tokens. The model is fine-tuned with a standard next-token LM objective on programmatically-generated training pairs from Re-DocRED + filtered distant-supervision DocRED + counterfactual variants, where loss is computed on the API call and the posttext but NOT on the memory-returned IDs. Evaluation on Re-DocRED test shows MemLLM cuts TARGET PPL from 3.510 (memory-disabled baseline) to 2.986 (-15%); on the ZsRE 1000-sequential-edit benchmark, it scores AVG 0.84 vs WISE 0.79, GRACE 0.67, DEFER 0.24 — and unlike parametric editors it maintains 0.97 locality. Storing 111M Wikipedia triples requires only ~21M unique entity/relation vectors — less than 20% of an equivalent dense-RAG proposition store.

## Key Takeaway

**`[E] [N] [G]`** MemLLM is the operational follow-up to the same authors' 2023 Ret-LLM concept paper: it commits to the structured-triple shape of memory, then proves out the entire training pipeline at scale and measures the result against both perplexity-style language modeling AND the harder knowledge-editing benchmarks where prior memory-based editors (SERAC, GRACE, WISE) compete. The architectural punchline is that "memory" is *not* a vector blob and not a free-text scratchpad — it is **a relational database whose schema (entity_id, relation_id, entity_id) is enforced by uniqueness constraints, indexed by Contriever embeddings on the entity and relation names only, and accessed exclusively through two API tokens the LLM has been taught to emit at the right moments**. Every component of that sentence is a deliberate ENGRAM design choice: write-time LLM distillation (E), polyglot triple-store + dual vector indices (N), traceability via unique IDs back to the source entity/relation names (G), hybrid lexical+vector retrieval with averaged-similarity threshold (R), no consolidation step beyond uniqueness deduping (A — deliberately not done), and explicit human-inspectable editability for maintenance (M).

## Implications

**For ENGRAM mapping of Flow OS memory:**

- **[E] Encode** — MemLLM is the canonical "LLM-distills-on-the-write-path" exemplar. Two distinct fine-tuned models are used for write vs read; the write path is *trained* to emit empty `({MEM_WRITE-->})` calls when a sentence has no extractable relations, which is the closest thing in the literature to a learned "skip this turn" gate. Flow's `/learn` extractor does the equivalent with prompts and a tagged 5-category schema; MemLLM shows that with enough training data (DocRED's >100K distant-supervised documents + 10 counterfactual variants of Re-DocRED) this can be fully learned rather than prompted.
- **[N] Network** — The "Triple Memory" main table + separate entity/relation tables with vector indices on the *name strings only* is a deliberately frugal polyglot stack. It deletes the proposition-RAG storage tax: 111M facts compress to ~21M vector rows (a ~5.3× compression at the index layer) and the schema enables exact-match symbolic queries on IDs once the vector layer has resolved aliases like "US" vs "USA". This is the structural argument against pure-vector storage that the Adler 2026 critique of Mem0 echoes from the other side.
- **[G] Ground** — Provenance is *implicit* and weak here: the triple `⟨Washington D.C., capital of, United States⟩` has no field for "where did this assertion come from" — it has only an ID. This is the dimension where MemLLM is least developed and the qualitative analysis exposes it: of 216 ZsRE editing errors, 95 (44%) were "edit in memory but not retrieved" — i.e. the system *had the fact* but could not reliably get the model to use it. Without grounding metadata, the model has no signal that it should trust memory over priors.
- **[R] Retrieve** — Hybrid vector+symbolic via cosine threshold on entity AND relation, combined with the constraint `0.5(cos(e,e^q_s) + cos(t,t^q)) ≥ τ_r` — i.e. averaged similarity must clear a final threshold, not just per-component. This handles paraphrase but is brittle for relations not in the 96-relation Wikidata vocabulary (the IUCN conservation status / family-lineage failure modes in §4.3 qualitative analysis). The post-hoc "ambiguous query filter" (Appendix B, Table 4) that drops queries like `⟨*, country, United States⟩` is the kind of hard-coded retrieval guardrail that a production memory system needs.
- **[A] Aggregate** — *Almost completely absent.* The system deduplicates exact triples and uses uniqueness constraints, but does not compress, merge, or abstract beyond that. The Limitations section explicitly calls out that composite relations (Apple Inc. → located_in:California, California → country:US ⟹ Apple Inc. → country:US) are *not* inferred. This is the "deliberately not done" choice that distinguishes MemLLM from later systems like A-MEM and Mao 2026 which experiment with active consolidation.
- **[M] Maintain** — Edit-by-overwrite: "if a newly extracted triple has an exact matching entity and relation with an old triple, we replace the old one with the new one." This produces the 0.97 locality score on ZsRE (vs 0.67 for DEFER). The architectural argument is that **edits are local because writes are local**: structured slots can be overwritten without disturbing other slots, while parametric editors must surgically modify weight subspaces and risk collateral damage. The maintenance dimension is also where the "memory-aware" gap appears — MemLLM does not know what *it does not know*, so the model can hallucinate fluently right past a missing fact without ever realizing it should have queried.

**Cross-dimensional interactions** (the part the lens explicitly asks for):

- **E forces R**: extracting triples instead of free text forces retrieval to use the same shape. You cannot retrieve a triple if you stored a paragraph, and vice versa. This is the same coupling that ChatDB exhibits and that proposition-RAG breaks (one sentence per row).
- **G is sacrificed for N efficiency**: dropping provenance is what enables the ~5.3× index compression. A "memory with full provenance" version of MemLLM would need to attach source document IDs and span offsets to every triple, expanding both the main table and the vector index.
- **A=null forces M=overwrite**: because there is no consolidation, the only maintenance strategy is overwrite-the-slot. A consolidated/abstracted memory (where one record represents many observations) would require either probabilistic update or a deeper edit-propagation mechanism.

**For our experiments**: the empirical evidence here is the strongest case to date for "write-time, learned, structured" being a viable production point on the synthesis curve. The 0.97 locality on 1000 sequential edits is what makes MemLLM-style memory architecturally appealing for agents that must accumulate facts indefinitely without polluting unrelated capabilities.

## How to Apply It (method)

**The reproducible recipe (Section 3)**:

1. **Define the memory schema.** Three SQL-style tables: (i) Entities `(Entity_ID PK, name str, embedding vector)`, (ii) Relations `(Relation_ID PK, name str, embedding vector)`, (iii) Triple Memory `(Triple_ID PK, Subj_Entity_ID FK, Relation_ID FK, Obj_Entity_ID FK)` with uniqueness enforced on the (Subj_Entity_ID, Relation_ID, Obj_Entity_ID) combination.
2. **Embed entities and relations with Contriever** (Izacard 2022 — TMLR), not the LLM itself. This is the key "ambiguity-collapse" step (US vs USA).
3. **Define two API token sequences** that the LLM must learn to emit: `({MEM_WRITE-->s»t»o;s»t»o;...})` and `({MEM_READ(s»t»;»t»o;...)-->results})`. The `({` opening token is the trigger your controller watches for during decoding.
4. **Build memory-write training data from Re-DocRED** (Tan 2022): for each sentence s_i in a document, gather all annotated triples where at least one entity is fully mentioned in s_i and the other is in s_i or its pretext; package as `(pretext + ({USER_ST})sentence({USER_END}), ({MEM_WRITE-->...}))`; train loss only on the API-call tokens.
5. **Build memory-read training data with Algorithm 1** (Appendix C, paper p. 19): scan entity mentions left-to-right; for each "target entity" e_target, collect all triples that participate; keep only those where the *other* entity has already appeared in the text (the query entity must be referenceable); discard previously-emitted triples; generate a query for each remaining triple; place the `({MEM_READ(...)` call immediately *before* the target entity's first mention; populate query results from the LIVE memory populated by the memory-write model run on Wikipedia (deliberately imperfect — matches inference conditions); apply training loss to the API call AND the posttext (NOT the memory-returned IDs).
6. **Boost data quality with three tricks**: (a) chain-of-thought-style reasoning prompt for distant-supervision filtering with Mixtral, raising F1 from 0.68 (baseline) to 0.80 (Table 1); (b) include 10 counterfactual variations of Re-DocRED (Modarressi 2024 EMNLP) to reduce parametric-knowledge bias; (c) drop training queries with >Q_thr = 30 results — they are unspecific noise.
7. **Fine-tune two LoRA adapters separately on Mistral-7B-v0.1**. Hyperparameters (Appendix D): learning rate 2e-5, Adam, 2 epochs, batch 96, LoRA rank 16, alpha 8, dropout 0.1.
8. **Inference (Figure 2)**: For writes, iterate sentences one-by-one, calling the write model with surrounding context. For reads, stream-decode tokens until `({` triggers a memory-read; complete the API call; execute via the retrieval formula `{e_o | ∃(e,t,e_o) ∈ M : e ∈ C, t ∈ T, 0.5(cos(e,e_s^q)+cos(t,t^q)) ≥ τ_r}`; append result to context; resume decoding. **Auto-drop stale reads** in three cases: empty result, |E| > Q_thr = 30, or model emits a new `({`.
9. **Memory-write decoding trick** (Appendix A): use *late-stopping greedy* — at each step, if the closing `")}"` token scores highest, record its position and score, but continue with the second-highest token until K=5 consecutive steps fail to improve. Then cut back to the highest-scoring closure. This catches the common failure mode where the write model ends extraction too early.
10. **Filter ambiguous read queries** (Appendix B, Table 4): a small static blacklist of (relation_type, query_pattern) pairs known to be over-broad (`⟨*, country, ⋅⟩`, `⟨*, date of birth, ⋅⟩`, etc.) — drop them before they ever execute.

**For Flow OS application**: steps 1, 2, 7, and 10 are directly portable to our `/learn` pipeline. The schema (1) is the closest thing in the literature to what `experiences/solutions/` + entity slugs should structurally look like if we ever move to a triple representation. Step 2 (embed *names only*, not full text) is the cheap-storage trick we're not yet using. Step 7 (separate LoRA adapters for write vs read) is the strongest argument I've seen for splitting our extractor and retriever into specialized models rather than one general-purpose Claude call. Step 10 (static ambiguous-query blacklist) is a 2-hour-of-work optimization that any retrieval system can pick up immediately.

## Best Figure

![Figure 2 — MemLLM inference with memory read and memory write (page 5)](figures/modarressi-2024-memllm-fig.png)

**Image Candidates:**
- Figure 1 (p. 4): MemLLM memory schema — three SQL tables (Entities, Relations, Triple Memory) with PK/FK structure; the entire architectural commitment in one diagram, but small and dense.
- Figure 2 (p. 5): Two-panel inference diagram showing the actual token stream for memory-write and memory-read, including the controller's pretext-rewrite step when a new `({MEM_READ` is emitted. This is the figure that explains *what the model literally does*.
- Figure 4 (p. 10): Memory efficiency curve — log-scale x-axis (No. extracted facts) vs y-axis (memory usage % vs fact-based storage) showing structured triples asymptoting to ~19% of proposition storage at 111M facts. Striking but supplementary.

**Best Image:**
- Figure Name: Figure 2: "MemLLM inference with memory read and memory write"
- Figure Page: 5
- Slide Caption: How MemLLM actually decodes — write the triples for the current sentence (top), then mid-generation emit a memory-read, get results inlined, resume decoding (bottom).
- Description: Figure 2 is split into two panels. Panel (a) shows memory-write on the example sentence "*Il Regalo Più Grande is a song by Italian singer Tiziano Ferro. The song was written by Ferro for his fourth studio album, Alla Mia Età.*" The input is split into pretext + focus sentence (bracketed by `({USER_ST})` and `({USER_END})`), and the LLM output is the trailing `({MEM_WRITE-->Alla Mia Età>>performer>>Tiziano Ferro;Il Regalo Più Grande>>part of>>Alla Mia Età})</s>`. Panel (b) shows memory-read in three consecutive states: (1) the model generates fluently up to a point where it needs the album name and emits `({MEM_READ(>>performer>>Tiziano Ferro;Il Regalo Più Grande>>part of)-->Alla Mia Età})` and continues; (2) some tokens later it initiates a new `({MEM_READ(...` — the controller *removes the previous read* from the context (the cited removal is the key controller behavior the figure exists to communicate) and re-inputs everything; (3) decoding continues from the rewritten context. Together the two panels are the entire MemLLM behavioral contract.

## What Experts Overlook

1. **The training data, not the model, is the contribution.** The paper's published artifact most likely to drive adoption is the training-set generation pipeline (Algorithm 1, Section 3.3), not the Mistral-7B LoRA weights. Anyone with a different base model + an entity/relation-annotated corpus can build a MemLLM-equivalent. ENGRAM dimensions affected: **[E]** (encode pipeline is open) and **[N]** (the schema choice is portable to any backend that supports triple storage with vector secondary indices).

2. **"Memory-disabled baseline" is not what most reviewers think.** Baseline #2 is the *same* fine-tuned memory-read model, but with retrieval forcibly returning empty. This isolates how much of the perplexity gain comes from the *fine-tuning* (which exposes the model to more in-domain text) vs the *actual memory retrieval*. Baseline #1 (raw Mistral-7B) → baseline #2 already drops OVERALL PPL from 5.823 to 4.997 — that's a 14% reduction from fine-tuning alone, before memory even enters the picture. The memory contributes the remaining 4.997 → 4.905 (a further 1.8%). **The headline "memory works" number masks how much of it is just fine-tuning.** This is a recurring honesty problem in the explicit-memory literature that this paper handles unusually well by making the baseline explicit. ENGRAM dimensions: **[G]** (provenance of improvement: is it the encode pipeline or the retrieve mechanism? without baseline #2 you cannot tell).

3. **Locality being 0.97 is more important than reliability being 0.78.** The standard narrative in editing-benchmark papers is to celebrate REL+GEN. But the *practical* failure mode of parametric editors is silent capability degradation in unrelated domains (DEFER scores 0.67, GRACE 1.00, WISE 1.00 — but they get there with parametric techniques that compound damage as edits stack). MemLLM hits 0.97 *by construction* — its edits live in a separate table, so unrelated rows cannot be touched. Architecturally this is the strongest empirical argument for the "externalize-first" stance on memory: **structural separation guarantees locality in a way parametric methods can only approximate.** ENGRAM: **[M]** (maintenance) and **[N]** (where memory lives directly determines what edits can break).

4. **Ablations 6 → 5 expose where the system actually struggles.** Going from "gold MR position" (oracle tells the model where to query) to "model picks the position" raises TARGET PPL from 2.232 → 2.596 (a 16% degradation). Going from "gold queries" to "model writes queries" raises TARGET PPL from 1.364 → 2.232 (a 64% degradation). **The single biggest open problem in this architecture is teaching the model to *write good queries*, not to *know when to query*.** This is rarely surfaced in the abstract or conclusion. ENGRAM: **[R]** (the retrieval-query-formulation step is the dominant error source; query generation is *learned*, not engineered).

5. **The "lack of memory-awareness" limitation is the real architectural ceiling.** Limitations section: *"if a fact is not stored in the memory, but the decoding process generates a partial prompt that requires that fact, the model would either continue generation based on its parametric knowledge or hallucinate."* The model has no internal signal "I should have queried for this and didn't get a result, so I am about to make this up." This is exactly the gap that a memory-aware confidence head (or a calibrated retrieval-uncertainty estimator) would close — and exactly what later work like Mao 2026's circuit analysis is poking at. Without it, MemLLM is a *correct-when-it-knows* but *not-self-aware-when-it-doesn't* system. ENGRAM: **[G]** (the missing grounding signal is "what is in vs out of memory") and **[A]** (no abstraction layer that could say "I have nothing relevant").

## Extracted Prompts

The paper does not include traditional inference-time prompts — its API is a learned token sequence, not a natural-language prompt. But it includes three reusable *training-time* prompt patterns worth capturing:

**1. Distant-supervision relation filter (Section 4.1.1, Appendix E, "reasoning" approach — F1 0.80 vs 0.68 baseline)**

```
You are given a focus sentence and a candidate relation (subject, relation_type, object) involving two entities.

Step 1: Write a single natural-language sentence that expresses what the candidate relation claims.
Step 2: Read the focus sentence carefully. Does it provide direct evidence supporting that natural-language sentence?
Step 3: Explain your reasoning in 1-2 sentences, referencing specific phrases from the focus sentence.
Step 4: On a new line, output exactly one of: "Yes" or "No".

[8-shot in-context examples follow]

Focus sentence: <s_i>
Candidate relation: <(e1, r, e2)>
```

**2. Memory-write API training format (Section 3.2, Figure 2a)**

```
<pretext sentences S<i>
({USER_ST})<focus sentence si>({USER_END})
({MEM_WRITE-->e1_s»t1»e1_o; e2_s»t2»e2_o; ...})</s>
```

(Loss applied only to the `({MEM_WRITE-->...})</s>` tokens.)

**3. Memory-read API training format (Section 3.2, Figure 2b — query, retrieval, continuation)**

```
<pretext text up to ({MEM_READ(>
({MEM_READ(eq1_s»t1»; »t2»eq2_o; ...)-->e1, e2, e3, ...})
<posttext text until next ({MEM_READ( or end-of-doc>
```

(Loss applied to the API call tokens AND the posttext. NOT to the memory-returned IDs `e1, e2, e3`.)

**4. ZsRE knowledge-editing edit-input format (Section 4.3)**

```
({USER_ST})What city was Luca Verdecchia born? It is or they are Naples({USER_END}).
```

(Append the edit answer with "It is or they are" before the closing tag; the write model is trained to extract place_of_birth(Verdecchia, Naples) from this.)

## Citations

(Full list in frontmatter — 58 citations extracted. First 10 by ENGRAM relevance shown here.)

- Modarressi et al. 2023 — *Ret-LLM* (arXiv:2305.14322) — the predecessor concept paper this work operationalizes
- Schick et al. 2023 — *Toolformer* (NeurIPS) — the learned-API-call training paradigm MemLLM extends to memory
- Hu et al. 2022 — *LoRA* (ICLR) — the parameter-efficient finetuning the two adapters use
- Jiang et al. 2023 — *Mistral 7B* (arXiv:2310.06825) — the base model
- Izacard et al. 2022 — *Contriever* (TMLR) — the dense retriever used for the entity/relation vector indices
- Tan et al. 2022 — *Re-DocRED* (EMNLP) — the primary training corpus with relation annotations
- Yao et al. 2019 — *DocRED* (ACL) — the original corpus + its distant-supervised expansion used for scale
- Wang et al. 2024a — *WISE* (arXiv:2405.14768) — the strongest knowledge-editing baseline (AVG 0.79)
- Mitchell et al. 2022 — *SERAC / DEFER* — memory-based editing baseline
- Hartvigsen et al. 2024 — *GRACE* — discrete-key-value-adapter editing baseline
- Lewis et al. 2020 — *RAG* — the unstructured-retrieval method this paper explicitly contrasts against (storage tax, edit difficulty)
- Hu et al. 2023 — *ChatDB* — most-similar prior work (structured DB memory) but task-specific, requires schema-prompted setup
- Roberts et al. 2020 — *How much knowledge can you pack into the parameters of a language model?* — the parametric-memory baseline the paper argues against
- Kandpal et al. 2023 — *Long-tail knowledge* — empirical justification for needing external memory
- Mallen et al. 2023 — *When not to trust language models* — another empirical justification
- Yao et al. 2023c — *Editing LLMs: problems and opportunities* — survey grounding the knowledge-editing claims
- Packer et al. 2023 — *MemGPT* — the OS-metaphor memory contender
- Park et al. 2023 — *Generative Agents* — the memory-as-prompt-window contender

## Related Digests

- [[modarressi-2023-ret-llm]] — Ret-LLM: the same authors' 2023 concept paper that MemLLM implements at scale. Where Ret-LLM was a working prototype on Alpaca-7B with hand-crafted demonstrations, MemLLM commits to fine-tuning on programmatically-generated data from Re-DocRED (>100K documents), proves it scales to a full Wikipedia memory (111M triples), and benchmarks rigorously against parametric and memory-based editing baselines. The triplet schema, the `({MEM_READ}` / `({MEM_WRITE}` token contract, and the LSH-vs-Contriever retrieval choice are the three points where the architectures diverge in operationally-meaningful ways.
- [[graves-2014-neural-turing-machines]] — Neural Turing Machines: the foundational "controller emits read/write commands to an external memory" pattern that MemLLM is a 2024 LLM-era specialization of. NTM's content-vs-location addressing has a direct analogue in MemLLM's vector-similarity-on-entity-name + symbolic-ID-on-triple-position hybrid.
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: a 2025 system that takes MemLLM's structured-memory idea and adds dynamic memory linking + Zettelkasten-style organization. A-MEM is what happens if you keep MemLLM's [E][N][R] choices but bolt on the [A] (consolidation) layer MemLLM deliberately omits.
- [[liu-2023-think-in-memory]] — Think-in-Memory: another contemporary structured-memory system but with LSH instead of dense vectors and "reasoning at write time, recall directly" instead of MemLLM's "extract relations at write time, query at read time." Direct comparison case on the write-time-synthesis axis.
- [[chhikara-2025-mem0]] — Mem0: the production-grade descendant of this lineage with a fact-graph + vector hybrid. Useful as the "what does this architecture look like at 100K users two years later" data point.
- [[sun-2025-hmem-hierarchical-memory]] — H-MEM: contrasts MemLLM's flat triple store with a hierarchical memory whose levels are committed at write time. Direct contrast on the Aggregate dimension MemLLM declines to engage.
- [[mao-2026-agent-memory-circuits]] — Agent Memory Circuits: 2026 circuit-analysis paper that probes *what is happening inside* MemLLM-style systems' attention and MLP layers when they decide to write/update/recall. The most current critical follow-up.

## Reviewer Notes

**Overall severity: Clean** (no substantive hallucinations against paper content).

Spot-checks performed against the paper text:

- **TARGET PPL numbers** (3.510 → 2.986) — verified against Table 2, row 1 and Baseline #2. ✓
- **Knowledge editing AVG scores** (MemLLM 0.84, WISE 0.79, GRACE 0.67, DEFER 0.24) — verified against Table 3. ✓
- **111M triples → 21M unique entity/relation records → ~19% storage** — verified against Section 4.2 "Memory redundancy reduction benefits" and Figure 4 caption. ✓
- **96 Wikidata relations covered** — verified against Section 4.1 and Limitations section. ✓
- **Q_thr = 30, LoRA rank 16, alpha 8, lr 2e-5, 2 epochs, batch 96** — verified against Appendix D. ✓
- **Two separate fine-tuned models (write and read) using LoRA on Mistral-7B-v0.1** — verified against Section 4.1 "We finetune two Mistral-7B (Jiang et al., 2023) models using LoRA". ✓
- **Late-stopping greedy with K=5** — verified against Appendix A. ✓
- **Distant-supervision filter F1: baseline 0.68 / justification 0.66 / reasoning 0.80** — verified against Table 1. ✓
- **Qualitative editing error breakdown (45 / 95 / 63 of 216)** — verified against Section 4.3 "Qualitative Analysis". ✓
- **Use of Contriever (Izacard 2022) for entity/relation embeddings** — verified against Section 3.1. ✓
- **Counterfactual variations of Re-DocRED (Modarressi 2024 EMNLP)** — verified against Section 4.1. ✓
- **Loss applied to MEM_WRITE call, MEM_READ call, posttext — but NOT to memory-returned IDs** — verified against Section 3.3 paragraphs around "The loss is applied to..." ✓

**Minor framing notes (not corrections)**:

- I described the ~5.3× compression as "at the index layer" — the paper presents this as raw storage compression (Figure 4), which is the same thing in this context (entities/relations are the only vector-indexed objects).
- I claimed "edits live in a separate table, so unrelated rows cannot be touched" — this is the architectural claim of the paper; in practice retrieval can still surface unintended triples when the embedding-similarity threshold is too loose. The 0.97 locality (not 1.00) reflects exactly this residual leakage.
- I described counterfactual training as reducing "parametric-knowledge bias" — this matches the paper's wording: "teaching the model to produce counterfactual answers (which often contradict its parametric memory) increases robustness against pretrained knowledge bias" (Section 4.1).
