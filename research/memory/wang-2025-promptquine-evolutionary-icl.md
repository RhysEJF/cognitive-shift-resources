---
corpus: agentic-memory
kind: paper-digest
slug: wang-2025-promptquine-evolutionary-icl
title: "Evolving Prompts In-Context: An Open-ended, Self-replicating Perspective"
authors:
  - "Wang, Jianyu"
  - "Hu, Zhiqiang"
  - "Bing, Lidong"
year: 2025
publication_date: "2025-06"
venue: "ICML 2025 (PMLR 267)"
source_url: "https://arxiv.org/abs/2506.17930"
doi: null
arxiv_id: "2506.17930"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "More careful prompt engineering loses to a dumb evolutionary loop that hacks the in-context demonstrations into ungrammatical fragments — the model's preferred 'language' is not human language, and pruning random tokens from a clean ICL prompt outperforms hand-crafted instructions across classification, generation, math, and jailbreak tasks."
topics:
  - prompt-optimization
  - in-context-learning
  - evolutionary-search
  - prompt-compression
  - jailbreaking
  - llm-alignment
  - self-replication
  - open-endedness
tags:
  - paper
  - icml-2025
  - genetic-algorithms
  - prompt-pruning
  - icl
  - llm
entities:
  - wang-jianyu
  - hu-zhiqiang
  - bing-lidong
related_digests:
  - guo-2024-evoprompt
  - zhang-2025-ace
  - vassilyev-2026-rcl
  - brown-2020-gpt3-few-shot
citations:
  - title: "Many-shot in-context learning"
    authors: ["Rishabh Agarwal", "Avi Singh", "Lei M. Zhang", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2404.11018"
  - title: "Transformers learn to implement preconditioned gradient descent for in-context learning"
    authors: ["Kwangjun Ahn", "Xiang Cheng", "Hadi Daneshmand", "Suvrit Sra"]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Llama 3 model card"
    authors: ["AI@Meta"]
    year: 2024
    venue: "preprint"
    doi: null
    url: "https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md"
    arxiv_id: null
  - title: "Yelp dataset challenge: Review rating prediction"
    authors: ["Nabiha Asghar"]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1605.05362"
  - title: "How to explain individual classification decisions"
    authors: ["David Baehrens", "Timon Schroeter", "Stefan Harmeling", "et al."]
    year: 2010
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Understanding jailbreak success: A study of latent space dynamics in large language models"
    authors: ["Sarah Ball", "Frauke Kreuter", "Nina Panickssery"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2406.09289"
  - title: "Representation engineering for large-language models: Survey and research challenges"
    authors: ["Lukasz Bartoszcze", "Sahil Munshi", "Bryan Sukidi", "et al."]
    year: 2025
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2502.17601"
  - title: "A review of population-based meta-heuristic algorithms"
    authors: ["Zahra Beheshti", "Siti Mariyam Hj. Shamsuddin"]
    year: 2013
    venue: "Int. j. adv. soft comput. appl"
    doi: null
    url: null
    arxiv_id: null
  - title: "Random search for hyper-parameter optimization"
    authors: ["James Bergstra", "Yoshua Bengio"]
    year: 2012
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Simulated annealing"
    authors: ["Dimitris Bertsimas", "John Tsitsiklis"]
    year: 1993
    venue: "Statistical science"
    doi: null
    url: null
    arxiv_id: null
  - title: "PIQA: Reasoning about physical commonsense in natural language"
    authors: ["Yonatan Bisk", "Rowan Zellers", "Jianfeng Gao", "et al."]
    year: 2020
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "A large annotated corpus for learning natural language inference"
    authors: ["Samuel R. Bowman", "Gabor Angeli", "Christopher Potts", "Christopher D. Manning"]
    year: 2015
    venue: "EMNLP"
    doi: "10.18653/v1/D15-1075"
    url: "https://aclanthology.org/D15-1075"
    arxiv_id: null
  - title: "Language models are few-shot learners"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Transformers generalize differently from information stored in context vs in weights"
    authors: ["Stephanie C. Chan", "Ishita Dasgupta", "Junkyung Kim", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2210.05675"
  - title: "JailbreakBench: An open robustness benchmark for jailbreaking large language models"
    authors: ["Patrick Chao", "Edoardo Debenedetti", "Alexander Robey", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2404.01318"
  - title: "InstructZero: Efficient instruction optimization for black-box large language models"
    authors: ["Lichang Chen", "Jiuhai Chen", "Tom Goldstein", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2306.03082"
  - title: "Transformers implement functional gradient descent to learn non-linear functions in context"
    authors: ["Xiang Cheng", "Yuxin Chen", "Suvrit Sra"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2312.06528"
  - title: "Hard prompts made interpretable: Sparse entropy regularization for prompt tuning with RL"
    authors: ["Yulhwa Choi", "Sangmin Bae", "Sunghyeon Ban", "et al."]
    year: 2024
    venue: "ACL"
    doi: "10.18653/v1/2024.acl-long.449"
    url: "https://aclanthology.org/2024.acl-long.449/"
    arxiv_id: null
  - title: "Evolving reinforcement learning algorithms"
    authors: ["John D. Co-Reyes", "Yingjie Miao", "Daiyi Peng", "et al."]
    year: 2021
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training verifiers to solve math word problems"
    authors: ["Karl Cobbe", "Vineet Kosaraju", "Mohammad Bavarian", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2110.14168"
  - title: "PhaseEvo: Towards unified long-context prompt optimization for large language models"
    authors: ["Wenduo Cui", "Junjie Zhang", "Zihao Li", "et al."]
    year: 2024
    venue: "First Workshop on Long-Context Foundation Models @ ICML 2024"
    doi: null
    url: null
    arxiv_id: null
  - title: "Why can GPT learn in-context? Language models secretly perform gradient descent as meta-optimizers"
    authors: ["Damai Dai", "Yutao Sun", "Li Dong", "et al."]
    year: 2023
    venue: "Findings of ACL"
    doi: "10.18653/v1/2023.findings-acl.247"
    url: "https://aclanthology.org/2023.findings-acl.247"
    arxiv_id: null
  - title: "Discovering the hidden vocabulary of DALLE-2"
    authors: ["Giannis Daras", "Alexandros Dimakis"]
    year: 2022
    venue: "NeurIPS 2022 Workshop on Score-Based Methods"
    doi: null
    url: null
    arxiv_id: null
  - title: "Distinguishing rule and exemplar-based generalization in learning systems"
    authors: ["Ishita Dasgupta", "Erin Grant", "Thomas Griffiths"]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Finding multiple solutions for multimodal optimization problems using a multi-objective evolutionary approach"
    authors: ["Kalyanmoy Deb", "Amit Saha"]
    year: 2010
    venue: "GECCO"
    doi: null
    url: null
    arxiv_id: null
  - title: "A fast and elitist multiobjective genetic algorithm: NSGA-II"
    authors: ["Kalyanmoy Deb", "Amrit Pratap", "Sameer Agarwal", "T. Meyarivan"]
    year: 2002
    venue: "IEEE TEC"
    doi: null
    url: null
    arxiv_id: null
  - title: "Compression, transduction, and creation: A unified framework for evaluating natural language generation"
    authors: ["Mingkai Deng", "Bowen Tan", "Zhengzhong Liu", "et al."]
    year: 2021
    venue: "EMNLP"
    doi: "10.18653/v1/2021.emnlp-main.599"
    url: "https://aclanthology.org/2021.emnlp-main.599"
    arxiv_id: null
  - title: "RLPrompt: Optimizing discrete text prompts with reinforcement learning"
    authors: ["Mingkai Deng", "Jianyu Wang", "Cheng-Ping Hsieh", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: "10.18653/v1/2022.emnlp-main.222"
    url: "https://aclanthology.org/2022.emnlp-main.222"
    arxiv_id: null
  - title: "Extraction of salient sentences from labelled documents"
    authors: ["Misha Denil", "Alban Demiraj", "Nando De Freitas"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1412.6815"
  - title: "In-context learning and gradient descent revisited"
    authors: ["Gilad Deutch", "Nadav Magar", "Tomer Natan", "Guy Dar"]
    year: 2024
    venue: "NAACL"
    doi: "10.18653/v1/2024.naacl-long.58"
    url: "https://aclanthology.org/2024.naacl-long.58"
    arxiv_id: null
  - title: "Goal misgeneralization in deep reinforcement learning"
    authors: ["Lauro Langosco Di Langosco", "Jack Koch", "Lee D. Sharkey", "et al."]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Threshold accepting: A general purpose optimization algorithm appearing superior to simulated annealing"
    authors: ["Gunter Dueck", "Tobias Scheuer"]
    year: 1990
    venue: "Journal of Computational Physics"
    doi: null
    url: null
    arxiv_id: null
  - title: "Go-explore: a new approach for hard-exploration problems"
    authors: ["Adrien Ecoffet", "Joost Huizinga", "Joel Lehman", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1901.10995"
  - title: "Pathologies of neural models make interpretations difficult"
    authors: ["Shi Feng", "Eric Wallace", "Alvin Grissom II", "et al."]
    year: 2018
    venue: "EMNLP"
    doi: "10.18653/v1/D18-1407"
    url: "https://aclanthology.org/D18-1407"
    arxiv_id: null
  - title: "Promptbreeder: Self-referential self-improvement via prompt evolution"
    authors: ["Chrisantha Fernando", "Dylan S. Banarse", "Henryk Michalewski", "et al."]
    year: 2024
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Analysis of diversity-preserving mechanisms for global exploration"
    authors: ["Tobias Friedrich", "Pietro S. Oliveto", "Dirk Sudholt", "Carsten Witt"]
    year: 2009
    venue: "Evolutionary Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Transformers learn higher-order optimization methods for in-context learning: A study with linear models"
    authors: ["Deqing Fu", "Tian-Qi Chen", "Robin Jia", "Vatsal Sharan"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.17086"
  - title: "Chain-of-thought hub: A continuous effort to measure large language models' reasoning performance"
    authors: ["Yao Fu", "Litu Ou", "Mingyu Chen", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2305.17306"
  - title: "Artificial intelligence, values, and alignment"
    authors: ["Iason Gabriel"]
    year: 2020
    venue: "Minds and Machines"
    doi: null
    url: null
    arxiv_id: null
  - title: "Model tells you what to discard: Adaptive KV cache compression for LLMs"
    authors: ["Suyu Ge", "Yunan Zhang", "Liyuan Liu", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.01801"
  - title: "Tabu search"
    authors: ["Michel Gendreau", "Jean-Yves Potvin"]
    year: 2005
    venue: "Search methodologies"
    doi: null
    url: null
    arxiv_id: null
  - title: "Handbook of metaheuristics"
    authors: ["Fred W. Glover", "Gary A. Kochenberger"]
    year: 2003
    venue: "Springer"
    doi: null
    url: null
    arxiv_id: null
  - title: "Alignment faking in large language models"
    authors: ["Ryan Greenblatt", "Carson Denison", "Benjamin Wright", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2412.14093"
  - title: "Connecting large language models with evolutionary algorithms yields powerful prompt optimizers"
    authors: ["Qingyan Guo", "Rui Wang", "Junliang Guo", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.08532"
  - title: "Genetic algorithms"
    authors: ["John H. Holland"]
    year: 1992
    venue: "Scientific American"
    doi: null
    url: null
    arxiv_id: null
  - title: "Best-of-N jailbreaking"
    authors: ["John Hughes", "Sara Price", "Aengus Lynch", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2412.03556"
  - title: "GPT-4o system card"
    authors: ["Aaron Hurst", "Adam Lerer", "Adam P. Goucher", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2410.21276"
  - title: "Llama guard: LLM-based input-output safeguard for human-AI conversations"
    authors: ["Hakan Inan", "Kartikeya Upasani", "Jianfeng Chi", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2312.06674"
  - title: "Non-stochastic best arm identification and hyperparameter optimization"
    authors: ["Kevin Jamieson", "Ameet Talwalkar"]
    year: 2016
    venue: "AISTATS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Mistral 7B"
    authors: ["Albert Q. Jiang", "Alexandre Sablayrolles", "Arthur Mensch", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.06825"
  - title: "Artprompt: ASCII art-based jailbreak attacks against aligned LLMs"
    authors: ["Fengqing Jiang", "Zhangchen Xu", "Luyao Niu", "et al."]
    year: 2024
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "LLMLingua: Compressing prompts for accelerated inference of large language models"
    authors: ["Huiqiang Jiang", "Qianhui Wu", "Chin-Yew Lin", "Yuqing Yang", "Lili Qiu"]
    year: 2023
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "2310.05736"
  - title: "LongLLMLingua: Accelerating and enhancing LLMs in long context scenarios via prompt compression"
    authors: ["Huiqiang Jiang", "Qianhui Wu", "Xufang Luo", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.06839"
  - title: "How can we know what language models know?"
    authors: ["Zhengbao Jiang", "Frank F. Xu", "Jun Araki", "Graham Neubig"]
    year: 2020
    venue: "TACL"
    doi: "10.1162/tacl_a_00324"
    url: "https://aclanthology.org/2020.tacl-1.28"
    arxiv_id: null
  - title: "Automatically auditing large language models via discrete optimization"
    authors: ["Erik Jones", "Anca Dragan", "Aditi Raghunathan", "Jacob Steinhardt"]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Prompt waywardness: The curious case of discretized interpretation of continuous prompts"
    authors: ["Daniel Khashabi", "Xinxi Lyu", "Sewon Min", "et al."]
    year: 2022
    venue: "NAACL"
    doi: "10.18653/v1/2022.naacl-main.266"
    url: "https://aclanthology.org/2022.naacl-main.266"
    arxiv_id: null
  - title: "Large language models are zero-shot reasoners"
    authors: ["Takeshi Kojima", "Shixiang Shane Gu", "Machel Reid", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "MAWPS: A math word problem repository"
    authors: ["Rik Koncel-Kedziorski", "Subhro Roy", "Aida Amini", "et al."]
    year: 2016
    venue: "NAACL"
    doi: "10.18653/v1/N16-1136"
    url: "https://aclanthology.org/N16-1136"
    arxiv_id: null
  - title: "Reformulating unsupervised style transfer as paraphrase generation"
    authors: ["Kalpesh Krishna", "John Wieting", "Mohit Iyyer"]
    year: 2020
    venue: "EMNLP"
    doi: "10.18653/v1/2020.emnlp-main.55"
    url: "https://aclanthology.org/2020.emnlp-main.55"
    arxiv_id: null
  - title: "Efficient memory management for large language model serving with PagedAttention (vLLM)"
    authors: ["Woosuk Kwon", "Zhuohan Li", "Siyuan Zhuang", "et al."]
    year: 2023
    venue: "SOSP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Yahoo! as an ontology: using Yahoo! categories to describe documents"
    authors: ["Yannis Labrou", "Tim Finin"]
    year: 1999
    venue: "CIKM"
    doi: null
    url: null
    arxiv_id: null
  - title: "RLAIF: Scaling reinforcement learning from human feedback with AI feedback"
    authors: ["Harrison Lee", "Samrat Phatale", "Hassan Mansoor", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Abandoning objectives: Evolution through the search for novelty alone"
    authors: ["Joel Lehman", "Kenneth O. Stanley"]
    year: 2011
    venue: "Evolutionary Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "The power of scale for parameter-efficient prompt tuning"
    authors: ["Brian Lester", "Rami Al-Rfou", "Noah Constant"]
    year: 2021
    venue: "EMNLP"
    doi: "10.18653/v1/2021.emnlp-main.243"
    url: "https://aclanthology.org/2021.emnlp-main.243"
    arxiv_id: null
  - title: "Measuring the intrinsic dimension of objective landscapes"
    authors: ["Chunyuan Li", "Heerad Farkhoor", "Rosanne Liu", "Jason Yosinski"]
    year: 2018
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Visualizing and understanding neural models in NLP"
    authors: ["Jiwei Li", "Xinlei Chen", "Eduard Hovy", "Dan Jurafsky"]
    year: 2016
    venue: "NAACL"
    doi: "10.18653/v1/N16-1082"
    url: "https://aclanthology.org/N16-1082"
    arxiv_id: null
  - title: "Understanding neural networks through representation erasure"
    authors: ["Jiwei Li", "Will Monroe", "Dan Jurafsky"]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1612.08220"
  - title: "Hyperband: A novel bandit-based approach to hyperparameter optimization"
    authors: ["Lisha Li", "Kevin Jamieson", "Giulia DeSalvo", "et al."]
    year: 2018
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Prefix-tuning: Optimizing continuous prompts for generation"
    authors: ["Xiang Lisa Li", "Percy Liang"]
    year: 2021
    venue: "ACL"
    doi: "10.18653/v1/2021.acl-long.353"
    url: "https://aclanthology.org/2021.acl-long.353"
    arxiv_id: null
  - title: "Compressing context to enhance inference efficiency of large language models"
    authors: ["Yucheng Li", "Bo Dong", "Frank Guerin", "Chenghua Lin"]
    year: 2023
    venue: "EMNLP"
    doi: "10.18653/v1/2023.emnlp-main.391"
    url: "https://aclanthology.org/2023.emnlp-main.391"
    arxiv_id: null
  - title: "Zero-label prompt selection"
    authors: ["Chonghua Liao", "Yanan Zheng", "Zhilin Yang"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2211.04668"
  - title: "Let's verify step by step"
    authors: ["Hunter Lightman", "Vineet Kosaraju", "Yura Burda", "et al."]
    year: 2024
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Use your instinct: Instruction optimization for LLMs using neural bandits coupled with transformers"
    authors: ["Xiaoqiang Lin", "Zhongxiang Wu", "Zhaoxuan Dai", "et al."]
    year: 2024
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing"
    authors: ["Pengfei Liu", "Weizhe Yuan", "Jinlan Fu", "et al."]
    year: 2023
    venue: "ACM Computing Surveys"
    doi: null
    url: null
    arxiv_id: null
  - title: "In-context vectors: Making in context learning more effective and controllable through latent space steering"
    authors: ["Sheng Liu", "Haotian Ye", "Lei Xing", "James Y. Zou"]
    year: 2024
    venue: "ICML"
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
  - title: "The Flan collection: Designing data and methods for effective instruction tuning"
    authors: ["Shayne Longpre", "Le Hou", "Tu Vu", "et al."]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity"
    authors: ["Yao Lu", "Max Bartolo", "Alastair Moore", "Sebastian Riedel", "Pontus Stenetorp"]
    year: 2022
    venue: "ACL"
    doi: "10.18653/v1/2022.acl-long.556"
    url: "https://aclanthology.org/2022.acl-long.556"
    arxiv_id: null
  - title: "Rethinking the role of demonstrations: What makes in-context learning work?"
    authors: ["Sewon Min", "Xinxi Lyu", "Ari Holtzman", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: "10.18653/v1/2022.emnlp-main.759"
    url: "https://aclanthology.org/2022.emnlp-main.759"
    arxiv_id: null
  - title: "The alignment problem from a deep learning perspective"
    authors: ["Richard Ngo", "Lawrence Chan", "Soren Mindermann"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2209.00626"
  - title: "From text to life: On the reciprocal relationship between artificial life and large language models"
    authors: ["Eleni Nisioti", "Claire Glanois", "Elias Najarro", "et al."]
    year: 2024
    venue: "Artificial Life Conference Proceedings 36"
    doi: null
    url: null
    arxiv_id: null
  - title: "Avida: A software platform for research in computational evolutionary biology"
    authors: ["Charles Ofria", "Claus O. Wilke"]
    year: 2004
    venue: "Artificial Life"
    doi: null
    url: null
    arxiv_id: null
  - title: "Prompt engineering guideline"
    authors: ["OpenAI"]
    year: 2023
    venue: "preprint"
    doi: null
    url: "https://platform.openai.com/docs/guides/prompt-engineering"
    arxiv_id: null
  - title: "Training language models to follow instructions with human feedback"
    authors: ["Long Ouyang", "Jeffrey Wu", "Xu Jiang", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "LLMLingua-2: Data distillation for efficient and faithful task-agnostic prompt compression"
    authors: ["Zhuoshi Pan", "Qianhui Wu", "Huiqiang Jiang", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2403.12968"
  - title: "A sentimental education: Sentiment analysis using subjectivity summarization based on minimum cuts"
    authors: ["Bo Pang", "Lillian Lee"]
    year: 2004
    venue: "ACL"
    doi: "10.3115/1218955.1218990"
    url: "https://aclanthology.org/P04-1035"
    arxiv_id: null
  - title: "BLEU: a method for automatic evaluation of machine translation"
    authors: ["Kishore Papineni", "Salim Roukos", "Todd Ward", "Wei-Jing Zhu"]
    year: 2002
    venue: "ACL"
    doi: "10.3115/1073083.1073135"
    url: "https://aclanthology.org/P02-1040/"
    arxiv_id: null
  - title: "AdvPrompter: Fast adaptive adversarial prompting for LLMs"
    authors: ["Anselm Paulus", "Arman Zharmagambetov", "Chuan Guo", "Brandon Amos", "Yuandong Tian"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2404.16873"
  - title: "Learning how to ask: Querying LMs with mixtures of soft prompts"
    authors: ["Guanghui Qin", "Jason Eisner"]
    year: 2021
    venue: "NAACL"
    doi: "10.18653/v1/2021.naacl-main.410"
    url: "https://aclanthology.org/2021.naacl-main.410"
    arxiv_id: null
  - title: "Language models are unsupervised multitask learners"
    authors: ["Alec Radford", "Jeffrey Wu", "Rewon Child", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Large-scale evolution of image classifiers"
    authors: ["Esteban Real", "Sherry Moore", "Andrew Selle", "et al."]
    year: 2017
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Regularized evolution for image classifier architecture search"
    authors: ["Esteban Real", "Alok Aggarwal", "Yanping Huang", "Quoc V. Le"]
    year: 2019
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "AutoML-Zero: Evolving machine learning algorithms from scratch"
    authors: ["Esteban Real", "Chen Liang", "David So", "Quoc Le"]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Steering Llama 2 via contrastive activation addition"
    authors: ["Nina Rimsky", "Nick Gabrieli", "Julian Schulz", "et al."]
    year: 2024
    venue: "ACL"
    doi: "10.18653/v1/2024.acl-long.828"
    url: "https://aclanthology.org/2024.acl-long.828"
    arxiv_id: null
  - title: "Solving general arithmetic word problems"
    authors: ["Subhro Roy", "Dan Roth"]
    year: 2015
    venue: "EMNLP"
    doi: "10.18653/v1/D15-1202"
    url: "https://aclanthology.org/D15-1202"
    arxiv_id: null
  - title: "Learning to retrieve prompts for in-context learning"
    authors: ["Ohad Rubin", "Jonathan Herzig", "Jonathan Berant"]
    year: 2022
    venue: "NAACL"
    doi: "10.18653/v1/2022.naacl-main.191"
    url: "https://aclanthology.org/2022.naacl-main.191"
    arxiv_id: null
  - title: "Artificial intelligence: a modern approach"
    authors: ["Stuart J. Russell", "Peter Norvig"]
    year: 2016
    venue: "Pearson"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fitness sharing and niching methods revisited"
    authors: ["Bruno Sareni", "Laurent Krahenbuhl"]
    year: 1998
    venue: "IEEE TEC"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exploiting cloze-questions for few-shot text classification and natural language inference"
    authors: ["Timo Schick", "Hinrich Schütze"]
    year: 2021
    venue: "EACL"
    doi: "10.18653/v1/2021.eacl-main.20"
    url: "https://aclanthology.org/2021.eacl-main.20"
    arxiv_id: null
  - title: "Gödel machines: self-referential universal problem solvers making provably optimal self-improvements"
    authors: ["Jürgen Schmidhuber"]
    year: 2003
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "cs/0309048"
  - title: "Do pretrained transformers really learn in-context by gradient descent?"
    authors: ["Lingfeng Shen", "Aayush Mishra", "Daniel Khashabi"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.08540"
  - title: "Style transfer from non-parallel text by cross-alignment"
    authors: ["Tianxiao Shen", "Tao Lei", "Regina Barzilay", "Tommi Jaakkola"]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Large language model alignment: A survey"
    authors: ["Tianhao Shen", "Renren Jin", "Yufei Huang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.15025"
  - title: "Large language models can be easily distracted by irrelevant context"
    authors: ["Freda Shi", "Xinyun Chen", "Kanishka Misra", "et al."]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts"
    authors: ["Taylor Shin", "Yasaman Razeghi", "Robert L. Logan IV", "Eric Wallace", "Sameer Singh"]
    year: 2020
    venue: "EMNLP"
    doi: "10.18653/v1/2020.emnlp-main.346"
    url: "https://aclanthology.org/2020.emnlp-main.346"
    arxiv_id: null
  - title: "Not just a black box: Learning important features through propagating activation differences"
    authors: ["Avanti Shrikumar", "Peyton Greenside", "Anna Shcherbina", "Anshul Kundaje"]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1605.01713"
  - title: "Deep inside convolutional networks: Visualising image classification models and saliency maps"
    authors: ["Karen Simonyan"]
    year: 2013
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1312.6034"
  - title: "Recursive deep models for semantic compositionality over a sentiment treebank"
    authors: ["Richard Socher", "Alex Perelygin", "Jean Wu", "et al."]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: "https://aclanthology.org/D13-1170"
    arxiv_id: null
  - title: "An information-theoretic approach to prompt engineering without ground truth labels"
    authors: ["Taylor Sorensen", "Joshua Robinson", "Christopher Rytting", "et al."]
    year: 2022
    venue: "ACL"
    doi: "10.18653/v1/2022.acl-long.60"
    url: "https://aclanthology.org/2022.acl-long.60"
    arxiv_id: null
  - title: "A StrongREJECT for empty jailbreaks"
    authors: ["Alexandra Souly", "Qingyuan Lu", "Dillon Bowen", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2402.10260"
  - title: "Why Greatness Cannot Be Planned: The Myth of the Objective"
    authors: ["Kenneth O. Stanley", "Joel Lehman"]
    year: 2015
    venue: "Springer"
    doi: null
    url: null
    arxiv_id: null
  - title: "Open-endedness: The last grand challenge you've never heard of"
    authors: ["Kenneth O. Stanley", "Joel Lehman", "Lisa Soros"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Inference scaling laws: The limits of LLM resampling with imperfect verifiers"
    authors: ["Benedikt Stroebl", "Sayash Kapoor", "Arvind Narayanan"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2411.17501"
  - title: "Query-dependent prompt evaluation and optimization with offline inverse RL"
    authors: ["Hao Sun", "Alihan Hüyük", "Mihaela van der Schaar"]
    year: 2023
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "BBTv2: Towards a gradient-free future with large language models"
    authors: ["Tianxiang Sun", "Zhengfu He", "Hong Qian", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: "10.18653/v1/2022.emnlp-main.259"
    url: "https://aclanthology.org/2022.emnlp-main.259"
    arxiv_id: null
  - title: "A study of reproduction in generational and steady-state genetic algorithms"
    authors: ["Gilbert Syswerda"]
    year: 1991
    venue: "Foundations of Genetic Algorithms"
    doi: null
    url: null
    arxiv_id: null
  - title: "Gemma: Open models based on Gemini research and technology"
    authors: ["Gemma Team", "Thomas Mesnard", "Cassidy Hardin", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2403.08295"
  - title: "Activation addition: Steering language models without optimization"
    authors: ["Alexander M. Turner", "Lisa Thiergart", "Gavin Leech", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2308.10248"
  - title: "Efficient multi-objective neural architecture search via pareto dominance-based novelty search"
    authors: ["An Vo", "Ngoc Hoang Luong"]
    year: 2024
    venue: "GECCO"
    doi: null
    url: null
    arxiv_id: null
  - title: "Theory of self-reproducing automata"
    authors: ["John Von Neumann", "Arthur W. Burks", "et al."]
    year: 1966
    venue: "University of Illinois Press"
    doi: null
    url: null
    arxiv_id: null
  - title: "Transformers learn in-context by gradient descent"
    authors: ["Johannes Von Oswald", "Eyvind Niklasson", "Ettore Randazzo", "et al."]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Uncovering mesa-optimization algorithms in transformers"
    authors: ["Johannes Von Oswald", "Maximilian Schlegel", "Alexander Meulemans", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.05858"
  - title: "Teach better or show smarter? On instructions and exemplars in automatic prompt optimization"
    authors: ["Xinyu Wan", "Ruoxi Sun", "Hootan Nakhost", "Sercan O. Arik"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2406.15708"
  - title: "Label words are anchors: An information flow perspective for understanding in-context learning"
    authors: ["Lean Wang", "Lei Li", "Damai Dai", "et al."]
    year: 2023
    venue: "EMNLP"
    doi: null
    url: "https://aclanthology.org/2023.emnlp-main.609"
    arxiv_id: null
  - title: "K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters"
    authors: ["Ruize Wang", "Duyu Tang", "Nan Duan", "et al."]
    year: 2021
    venue: "Findings of ACL-IJCNLP"
    doi: "10.18653/v1/2021.findings-acl.121"
    url: "https://aclanthology.org/2021.findings-acl.121"
    arxiv_id: null
  - title: "Latent space chain-of-embedding enables output-free LLM self-evaluation"
    authors: ["Yiqun Wang", "Peng Zhang", "Bo Yang", "Derek F. Wong", "Ruifeng Wang"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2410.13640"
  - title: "Chain-of-thought prompting elicits reasoning in large language models"
    authors: ["Jason Wei", "Xuezhi Wang", "Dale Schuurmans", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Larger language models do in-context learning differently"
    authors: ["Jerry Wei", "Jason Wei", "Yi Tay", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2303.03846"
  - title: "Jailbreak and guard aligned language models with only few in-context demonstrations"
    authors: ["Zeming Wei", "Yifei Wang", "Ang Li", "Yichuan Mo", "Yisen Wang"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.06387"
  - title: "From decoding to meta-generation: Inference-time algorithms for large language models"
    authors: ["Sean Welleck", "Amanda Bertsch", "Matthew Finlayson", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2406.16838"
  - title: "Hard prompts made easy: Gradient-based discrete optimization for prompt tuning and discovery"
    authors: ["Yuxin Wen", "Neel Jain", "John Kirchenbauer", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient streaming language models with attention sinks"
    authors: ["Guangxuan Xiao", "Yuandong Tian", "Beidi Chen", "Song Han", "Mike Lewis"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.17453"
  - title: "Qwen2 technical report"
    authors: ["An Yang", "Baosong Yang", "Binyuan Hui", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2407.10671"
  - title: "Large language models as optimizers"
    authors: ["Chengrun Yang", "Xuezhi Wang", "Yifeng Lu", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.03409"
  - title: "Genetic algorithms with memory- and elitism-based immigrants in dynamic environments"
    authors: ["Shengxiang Yang"]
    year: 2008
    venue: "Evolutionary Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving probability-based prompt selection through unified evaluation and analysis"
    authors: ["Sohee Yang", "Jongwoo Kim", "Joel Jang", "Seonghyeon Ye", "Hwaran Lee", "Minjoon Seo"]
    year: 2024
    venue: "TACL"
    doi: "10.1162/tacl_a_00666"
    url: "https://aclanthology.org/2024.tacl-1.37"
    arxiv_id: null
  - title: "Interpreting language models with contrastive explanations"
    authors: ["Kayo Yin", "Graham Neubig"]
    year: 2022
    venue: "EMNLP"
    doi: "10.18653/v1/2022.emnlp-main.14"
    url: "https://aclanthology.org/2022.emnlp-main.14"
    arxiv_id: null
  - title: "Ground-truth labels matter: A deeper look into input-label demonstrations"
    authors: ["Kang Min Yoo", "Junyeob Kim", "Hyuhng Joon Kim", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: "10.18653/v1/2022.emnlp-main.155"
    url: "https://aclanthology.org/2022.emnlp-main.155/"
    arxiv_id: null
  - title: "Instruction tuning for large language models: A survey"
    authors: ["Shengyu Zhang", "Linfeng Dong", "Xiaoya Li", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2308.10792"
  - title: "Character-level convolutional networks for text classification"
    authors: ["Xiang Zhang", "Junbo Zhao", "Yann LeCun"]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Accelerating greedy coordinate gradient and general prompt optimization via probe sampling"
    authors: ["Yiran Zhao", "Wenyue Zheng", "Tianle Cai", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Calibrate before use: Improving few-shot performance of language models"
    authors: ["Zihao Zhao", "Eric Wallace", "Shi Feng", "Dan Klein", "Sameer Singh"]
    year: 2021
    venue: "ICML"
    doi: null
    url: "https://proceedings.mlr.press/v139/zhao21c.html"
    arxiv_id: null
  - title: "Judging LLM-as-a-judge with MT-bench and Chatbot Arena"
    authors: ["Lianmin Zheng", "Wei-Lin Chiang", "Ying Sheng", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improved few-shot jailbreaking can circumvent aligned language models and their defenses"
    authors: ["Xiaosen Zheng", "Tianyu Pang", "Chao Du", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Theory of global random search"
    authors: ["Anatoly A. Zhigljavsky"]
    year: 2012
    venue: "Springer"
    doi: null
    url: null
    arxiv_id: null
  - title: "Large language models are human-level prompt engineers"
    authors: ["Yongchao Zhou", "Andrei I. Muresanu", "Ziwen Han", "et al."]
    year: 2022
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Predicting fine-tuning performance with probing"
    authors: ["Zining Zhu", "Soroosh Shahtalebi", "Frank Rudzicz"]
    year: 2022
    venue: "EMNLP"
    doi: "10.18653/v1/2022.emnlp-main.793"
    url: "https://aclanthology.org/2022.emnlp-main.793"
    arxiv_id: null
  - title: "Universal and transferable adversarial attacks on aligned language models"
    authors: ["Andy Zou", "Zifan Wang", "J. Zico Kolter", "Matt Fredrikson"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2307.15043"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Overview of the PromptQuine framework"
  page: 5
  image_path: "figures/wang-2025-promptquine-evolutionary-icl-fig.png"
---

# Evolving Prompts In-Context: An Open-ended, Self-replicating Perspective

**Authors:** Jianyu Wang, Zhiqiang Hu, Lidong Bing
**Published:** 2025-06 · [Source](https://arxiv.org/abs/2506.17930)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Wang, Hu, and Bing (DAMO Academy / MiroMind, ICML 2025) attack the prompt-optimization problem by inverting the standard playbook: instead of writing better instructions, they randomly delete tokens from a vanilla 1-shot ICL prompt until what remains is syntactically broken "gibberish" — and find this consistently matches or beats state-of-the-art prompt optimizers across 6 classification tasks, Yelp style transfer, jailbreaks on Vicuna-7B and Mistral-7B, PIQA, and 4 math reasoning benchmarks. The mechanism is **PromptQuine**: a regularized-evolution genetic algorithm (population 30, offspring 50, 10,000 iterations, mutation = bit-flip pruning of 1–4 tokens) where binary token masks are genotypes and the resulting ICL prompts are phenotypes; only new offspring compete for survival, parents are picked via tournament selection (ratio 0.2), and a final "calibration-then-selection" re-rank uses the held-out validation accuracy to fight overfitting to the in-search fitness proxy. On Llama-3-8B-Instruct, PromptQuine-1-shot lifts average classification accuracy from 69.6% (vanilla 1-shot ICL) to 77.5% (vs. 75.8% for Promptbreeder, 67.5% for RLPrompt, 73.6% for EvoPrompt), with 52.9% of tokens pruned; 4-shot reaches 81.3%. On AdvBench jailbreaks, ASR-EM rises from 50.4% (vanilla 2-shot) to 99.3% on Vicuna-7B-v1.5 and from 48.0% to 98.8% on Mistral-7B-Instruct-v0.3. Three findings stand out for the architecture: (1) the search landscape is multimodal — pure hill-climbing variants get trapped, evolutionary search escapes; (2) label words inside the demonstration are retained almost always by the evolved prompts (Figure 3) and removing them costs accuracy, so the format scaffolding is doing real work even when the surrounding text is gibberish; (3) the effect persists with random verbalizers on a 70B model, hinting that ICL relies on sparse rule-based features that aren't captured by human semantics. The useful takeaway: when your "memory" of a task is a prompt template, the optimal compression is not human-readable — and you need a search loop, not a writer, to find it.

## Key Takeaway

The harder you try to write a "good" prompt, the further you get from the model's preferred input. PromptQuine throws away the entire prompt-engineering industry and shows that **randomly deleting tokens from a working ICL example, guided only by held-out accuracy, beats every hand-crafted or LLM-engineered baseline** — because LLMs are aligned to human language only superficially, and underneath they have a sparse, rule-based grammar of their own that gibberish happens to hit more reliably than fluent English. The model's actual "language" is not English.

## Implications

- **[Encode] Treat prompts as evolvable artifacts, not authored documents**: Stop assuming the optimal write-time representation is human-readable. For a recurring task in a memory system, store the seed (a clean ICL example) AND the evolved pruned variant, and serve the evolved one — accept that the latter looks broken to humans but performs better. The write-time investment shifts from "draft the perfect instruction" to "spec a fitness function and a held-out evaluation set."
- **[Aggregate] The fitness proxy is the hardest part, not the search**: PromptQuine relies on a proxy fitness (8-shot balanced samples, 200 validation set) plus a final "calibration-then-selection" pass on the full held-out accuracy to fight overfitting. In an agentic memory system, this maps to "we can run cheap rollouts to score a synthesized pattern, but periodically need expensive ground-truth re-ranks" — budget for both.
- **[Maintain] Population-based memory beats greedy improvement**: The paper directly shows hill-climbing variants (TAPruning, SAHCPruning) get trapped in local optima while evolutionary search escapes (Figure 1 right; success rate of random search over evolutionary search approaches zero as task difficulty grows). If your memory consolidation is "keep the single best pattern so far and tweak it," you are in a hill-climbing regime — expect premature convergence. Maintain a population of candidates and only let new offspring compete (regularized evolution).
- **[Retrieve] Compression and search are the same problem**: The paper's reformulation — "prompt compression is guided prompt search where the target is to maximize task performance, not to maximize compression ratio" — applies one-for-one to memory retrieval. Picking which chunks to put in context is structurally identical to picking which tokens to prune; you can stop building separate compression and retrieval stacks and build one search-based context-construction loop.
- **[Ground] Label words / format scaffolding are load-bearing even inside gibberish**: Figure 3 shows pruned prompts retain task-specific label words at very high rates across 7 model families. The structural "input → label" scaffold of an ICL example IS the signal; the prose around it is mostly noise. For memory cards, preserve the structural skeleton (entity names, dates, decision verbs) even when aggressively compressing — that scaffold is what the model parses, not the connective tissue.
- **[Network] Search efficiency depends on parallelism, which depends on representation**: The Generational GA variant exists because it's batchable (parallelizable across the population) while the Steady-state variant explores better but serially. For a memory system running fitness evaluations through LLM calls (expensive), choose data structures that let you batch — token-mask genotypes happen to be perfect for batching against vLLM.
- **[Ground] Surface-form alignment is brittle in both directions**: The same pruning that boosts task accuracy also lifts jailbreak ASR from ~50% to ~99% on Vicuna and Mistral. Any memory architecture that trusts "the prompt looks safe to a human reviewer" as an alignment check is dead — alignment must be verified at output, not input. Plan for output-level safety filters as a first-class component.
- **[Aggregate] Open-endedness is a real strategy, not a metaphor**: The paper grounds itself in Von Neumann self-replication + Lehman/Stanley novelty search, and the punchline ("evolved unnatural prompts consistently outperform manually designed ones, representing a step towards open-ended self-improvement") is the same one Promptbreeder, AutoML-Zero, and ACE land on. The shape-of-memory question now includes "is the system designed to evolve its own representations, or only to update authored ones?"

## How to Apply It (method)

**Scenario:** You're building a memory layer for an agentic operating system that handles many recurring task types (classify-as-X, summarize-into-Y, extract-fields-Z). Each task is presented to the LLM as a small in-context demonstration retrieved from memory. You suspect the human-readable prompts you've been authoring are suboptimal, and you want to discover better ones automatically — without paying for a frontier model to "write better prompts" on every call. The memory system should learn its own preferred phrasing per task over time.

**Steps:**

1. **Pick the task and gather two disjoint sets**: For each recurring task, collect a small validation set (≥200 labeled examples, the paper uses 200) and a small in-search fitness set (the paper uses 50–100 paired samples in 8-shot balanced form for classification, 50 for jailbreak). Keep a held-out test set you never touch. Strict separation — the paper is explicit that conflating these inflates results.

2. **Author a vanilla seed prompt**: Write a single, normal ICL prompt for the task using one demonstration (input → label pair). This is your `population_init` — every member of your starting population is a copy of this same prompt. The paper found random-pruning initialization gives no advantage over duplicating the seed.

3. **Tokenize and represent each prompt as a bit mask**: For a prompt of N tokens, the genotype is an N-bit string where 1 = keep token, 0 = prune. The phenotype (what the model sees) is the subsequence of kept tokens in original order. Order is fixed — the paper deliberately doesn't permute tokens because it explodes the search space.

4. **Define your fitness function**: For classification use the piecewise reward from Deng et al. 2022 (RLPrompt) — the paper benchmarked Mutual Information, Entropy, Majority Voting, and Probability-based metrics and found the piecewise reward stable. For generation tasks use a task-specific scorer (Joint Score for style transfer, ASR-EM or ASR-LLM for jailbreak). The fitness call is the dominant cost — minimize it.

5. **Run the regularized-evolution loop** (Algorithm 3 in the paper) with these defaults:

   ```
   population_size = 30
   offspring_size = 50
   mutation_rate = uniform over {1, 2, 3, 4}  # bits flipped per child
   tournament_selection_ratio = 0.2           # k = 0.2 * pop_size individuals sampled, best wins
   max_iterations = 10,000
   min_prompt_length = 15                     # stop when avg population length drops below this
   ```

   At each iteration: sample `k` individuals via tournament, copy the winner, mutate by flipping 1–4 bits 1→0 (additional pruning), evaluate the child's fitness, push it into the population, evict the lowest scorer. **Crucial — regularized evolution**: only new offspring compete for inclusion, never the parents. This is the difference between escaping local optima and getting stuck in them.

6. **Pick GGA vs. SSGA based on your budget**:
   - **Generational GA (GGA)**: batches all offspring per generation → vLLM-parallelizable → faster. Use for ≥4-shot ICL where computation dominates.
   - **Steady-state GA (SSGA)**: updates the population after every offspring → more exploratory → slower. Use for 1-shot ICL where each evaluation is cheap and you want quality.

7. **Calibration-then-selection re-rank**: After the evolutionary loop terminates, take the entire history `H` of prompts ever generated. Re-rank the top-`E` (elite) prompts using the FULL validation set (not the cheaper in-search fitness proxy). Return the best one. This pass exists specifically to fight overfitting to the fitness shortcut and matters significantly in their ablations.

8. **Verify the evolved prompt on the held-out test set**: Run task-specific metric on the test set. Expect the evolved prompt to look syntactically broken to a human (e.g., "Let's work this out step by step to be sure we have the right answer" → "Let's work out step by step sure we right answer" — paper shows this lifts MultiArith on InstructGPT from 78.7%→86.7%). Do not edit it back into fluent English; that's a regression.

9. **Cache and version the evolved prompt in your memory store**: Treat the evolved prompt as a first-class artifact alongside the seed. Re-run evolution when (a) you switch backbone model, (b) the held-out task distribution drifts, or (c) you have new validation data. Don't run evolution per query — amortize the search cost across many uses.

10. **Test instability across templates before deploying**: Section 5.1 shows pruned prompts are sensitive to ICL template variations (signal words, separators, spacing). Before shipping, sample 3 template variants with 3 different ICL seeds; if accuracy swings by >5 pp, evolve a single prompt per (template, seed) pair, or accept the instability budget.

**Expected outcome:** A per-task library of evolved, machine-preferred prompts that beat your authored prompts by 5–10 pp on classification and can match or exceed dedicated optimizers like Promptbreeder while running in minutes per task (Appendix Table 10 / 11). You also get a falsifiable picture of how brittle each task is to template variation — and an output-level safety constraint as a non-negotiable, because the same loop can find jailbreak strings as easily as it finds task-helpful ones.

## Best Figure

![Figure 2 — Overview of the PromptQuine framework (page 5)](figures/wang-2025-promptquine-evolutionary-icl-fig.png)

Image Candidates:
- Figure 2 (p. 5): Single-view conceptual diagram showing the self-replicating loop AND a sketch of how performance evolves — captures the whole paper visually.
- Figure 1 (p. 5): Three-panel landscape diagnostic (multimodality, ES vs RS, RS/ES success ratio collapse) but harder to read in one glance.
- Table 1 (p. 6): Side-by-side numerical comparison of PromptQuine vs. 8 baselines on 6 classification tasks — clear winner, but a table not a figure.

Best Image:
- Figure Name: Figure 2: "Overview of the PromptQuine framework"
- Figure Page: 5
- Slide Caption: PromptQuine evolves ICL prompts by copying and pruning tokens; guided by fitness selection, unnatural-language children consistently beat hand-designed prompts.
- Description: A two-panel diagram. Panel (a) — Optimization Pipeline — shows the cycle: "In-Context Demonstration" feeds "Population Initialization", which spawns a "Self-Replicating Loop" of copy-then-mutate steps driving a "Task Prompt Population," all "Guided by Fitness Selection." Panel (b) — Genetic Prompt-Quine — shows population fitness improving over generations (sample scores rising from 39/43 in early iterations to 76/85/93 later), illustrating that the regularized evolution loop progressively finds higher-scoring (and increasingly less natural-looking) prompts. The figure is the paper's whole argument compressed into one image: the loop replaces human prompt-engineering, mutation is just pruning, selection is just fitness, and the system improves itself in a Darwinian-style open-ended way.

## What Experts Overlook

The detail most reviewers skim past is **"regularized evolution"** (Real et al., 2019), which the paper calls out as the most crucial single design choice. In standard genetic algorithms, when you pick the next population you let parents AND offspring compete for the limited slots — keep the top-k by fitness regardless of age. Regularized evolution does the opposite: it forces every generation's top slot to come from NEW offspring, evicting incumbents based on age, not fitness. This sounds like a small bookkeeping change. It is actually what stops the algorithm from collapsing onto whichever high-scoring prompt got lucky first.

**Why it matters:** The paper shows directly (Appendix D.7) that without this rule, standard GA collapses prematurely — diversity dies in ~30 generations and the population fixates on a local optimum. With it, the population keeps exploring because the only way to survive is to keep producing new variants. For memory architectures, this is the difference between "we store the best 30 patterns we've ever seen" and "we store 30 patterns and force the oldest one to leave every cycle." The latter sounds wasteful but is what prevents the system from over-fitting to early lucky finds. Same logic as why a brain that never forgets ends up stuck in the past.

**Example of good use:** A long-running memory system that maintains a population of 30 candidate "task templates" per recurring task type, evaluates each via cheap rollouts, and **forces eviction by age** every consolidation cycle — even if the evicted candidate is currently top-scoring. New variants are generated by token-pruning the survivors. Over weeks, the system finds increasingly compressed, increasingly task-effective templates that no human authored. The memory system has become a true open-ended learner per Stanley/Lehman, because the "objective" (current best fitness) does not freeze the population.

**Example of misapplication:** A naive "elite preservation" version — "we'll keep the all-time best 30 prompts we've ever seen and only replace them when something beats them" — collapses to a single archetypal prompt within a few dozen iterations. The system reports rising fitness (it's still finding marginal wins) but it has stopped exploring. You'll think the memory layer is working and only notice when (a) the backbone model changes or (b) the task distribution shifts and the cached prompts become brittle. The "improvement" was a mirage of premature convergence — exactly what the paper warns about and exactly the failure mode for any memory system that uses "always keep the winner" as its consolidation rule.

## Extracted Prompts

The paper does not present standalone prompt templates as authored text. The evolved prompts ARE token sequences mutated from vanilla ICL templates per dataset, and the paper itself notes (Section 4.1, Appendix D.3) that templates differ "only in signal words, separators, spacing characters, and minor variations in natural language instructions." The two human-readable prompts that appear in the body for illustration:

**Prompt explanation:** Zhou et al. (2022) zero-shot CoT prompt, the seed PromptQuine prunes for MultiArith.

```
Let's work this out step by step to be sure we have the right answer
```

**Prompt explanation:** Evolved PromptQuine pruning of the above on InstructGPT, lifting MultiArith accuracy from 78.7% to 86.7% (Appendix Table 7).

```
Let's work out step by step sure we right answer
```

Beyond these two illustrative strings, the paper does not print full ICL prompt templates in the body — they are referenced as Appendix tables (Table 24 for SNLI templates, Appendix D.4 for jailbreak EM strings and Llama-Guard-3 evaluator prompts taken from JailbreakBench) but the literal text is not in the rendered PDF body.

## Citations

(Full citation array in the frontmatter — 100+ entries; first ten as bullets for scannability.)

- Agarwal et al. 2024 — *Many-shot in-context learning* (arXiv:2404.11018)
- Ahn et al. 2023 — *Transformers learn to implement preconditioned gradient descent for ICL* (NeurIPS)
- AI@Meta 2024 — *Llama 3 model card*
- Asghar 2016 — *Yelp dataset challenge: Review rating prediction* (arXiv:1605.05362)
- Baehrens et al. 2010 — *How to explain individual classification decisions* (JMLR)
- Ball, Kreuter & Panickssery 2024 — *Understanding jailbreak success: A study of latent space dynamics in LLMs* (arXiv:2406.09289)
- Bartoszcze et al. 2025 — *Representation engineering for LLMs: Survey and research challenges* (arXiv:2502.17601)
- Beheshti & Shamsuddin 2013 — *A review of population-based meta-heuristic algorithms*
- Bergstra & Bengio 2012 — *Random search for hyper-parameter optimization* (JMLR)
- Bertsimas & Tsitsiklis 1993 — *Simulated annealing* (Statistical Science)

## Related Digests

- [[guo-2024-evoprompt]] — EvoPrompt: connecting LLMs with evolutionary algorithms — the closest prior art; same evolutionary-search lineage but in natural-language space using LLMs as mutation operators, where PromptQuine works in raw-token space and uses dumb pruning as mutation.
- [[zhang-2025-ace]] — Agentic Context Engineering: evolving contexts for self-improving language models — also frames context as something that evolves, but at the agent/task-orchestration level rather than at the token level.
- [[vassilyev-2026-rcl]] — Reflective Context Learning: studying the optimization primitives of context space — closely related framing of the context window itself as a search/optimization object.
- [[brown-2020-gpt3-few-shot]] — Language Models are Few-Shot Learners — the GPT-3 paper that introduced the ICL paradigm PromptQuine is pruning.

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim above (accuracy numbers, hyperparameters, ASR percentages, model names, task list) was cross-checked against the paper body (Table 1, Table 2, Table 3, Table 9) and matches verbatim. The interpretive claims — the ENGRAM-tagged implications, the "what experts overlook" framing of regularized evolution as load-bearing, the analogy from PromptQuine to memory consolidation — are framed as the memory-architect's reading of the paper rather than as direct paper claims, and the paper does in fact name regularized evolution (Real et al., 2017; 2019) as the most crucial single design choice (Section 3.4, Appendix D.7). No fabricated metrics, no invented experiments, no overextension beyond what the ablations actually show.
