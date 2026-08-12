---
corpus: agentic-memory
kind: paper-digest
slug: wei-2022-chain-of-thought
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
authors:
  - "Wei, J."
  - "Wang, X."
  - "Schuurmans, D."
  - "Bosma, M."
  - "Ichter, B."
  - "Xia, F."
  - "Chi, E."
  - "Le, Q."
  - "Zhou, D."
year: 2022
publication_date: "2022-01"
venue: "NeurIPS 2022"
source_url: "https://arxiv.org/abs/2201.11903"
doi: null
arxiv_id: "2201.11903"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Adding a few worked-example rationales to the prompt — eight hand-written \"chain of thought\" exemplars — turns large language models into multi-step reasoners without any fine-tuning, lifting PaLM 540B from 18% to 57% on GSM8K math word problems and setting new SOTA on multiple benchmarks; crucially, this is an emergent ability of scale that only appears beyond ~100B parameters and actually hurts smaller models."
topics:
  - chain-of-thought
  - prompt-engineering
  - llm-reasoning
  - emergent-abilities
  - few-shot-learning
  - arithmetic-reasoning
  - commonsense-reasoning
  - symbolic-reasoning
tags:
  - paper
  - prompting
  - llm-reasoning
  - icl
  - benchmark
  - canonical
entities:
  - wei-jason
  - wang-xuezhi
  - schuurmans-dale
  - le-quoc
  - zhou-denny
related_digests:
  - zhou-2022-least-to-most-prompting
  - fernando-2023-promptbreeder
  - radford-2019-gpt2-multitask
  - chen-2023-memwalker
  - shen-2023-icl-not-gd
citations:
  - title: "Do as I can, not as I say: Grounding language in robotic affordances"
    authors: ["Michael Ahn", "Anthony Brohan", "Noah Brown", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2204.01691"
  - title: "MathQA: Towards interpretable math word problem solving with operation-based formalisms"
    authors: ["Aida Amini", "Saadia Gabriel", "Shanchuan Lin", "et al."]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Giving BERT a calculator: Finding operations and arguments with reading comprehension"
    authors: ["Daniel Andor", "Luheng He", "Kenton Lee", "et al."]
    year: 2019
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning with latent language"
    authors: ["Jacob Andreas", "Dan Klein", "Sergey Levine"]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Program synthesis with large language models"
    authors: ["Jacob Austin", "Augustus Odena", "Maxwell Nye", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2108.07732"
  - title: "Beyond the imitation game: Measuring and extrapolating the capabilities of language models"
    authors: ["BIG-bench collaboration"]
    year: 2021
    venue: "In preparation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Flexible generation of natural language deductions"
    authors: ["Kaj Bostrom", "Xinyu Zhao", "Swarat Chaudhuri", "et al."]
    year: 2021
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models are few-shot learners"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Making neural programming architectures generalize via recursion"
    authors: ["Jonathon Cai", "Richard Shin", "Dawn Song"]
    year: 2017
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "e-SNLI: Natural language inference with natural language explanations"
    authors: ["Oana-Maria Camburu", "Tim Rocktäschel", "Thomas Lukasiewicz", "et al."]
    year: 2018
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Can rationalization improve robustness?"
    authors: ["Howard Chen", "Jacqueline He", "Karthik Narasimhan", "et al."]
    year: 2022
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Evaluating large language models trained on code"
    authors: ["Mark Chen", "Jerry Tworek", "Heewoo Jun", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2107.03374"
  - title: "Neural symbolic reader: Scalable integration of distributed and symbolic representations for reading comprehension"
    authors: ["Xinyun Chen", "Chen Liang", "Adams Wei Yu", "et al."]
    year: 2019
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Semantically-aligned equation generation for solving and reasoning math word problems"
    authors: ["Ting-Rui Chiang", "Yun-Nung Chen"]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Transformers as soft reasoners over language"
    authors: ["Peter Clark", "Oyvind Tafjord", "Kyle Richardson"]
    year: 2020
    venue: "IJCAI"
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
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neural logic machines"
    authors: ["Honghua Dong", "Jiayuan Mao", "Tian Lin", "et al."]
    year: 2019
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Benefits of intermediate annotations in reading comprehension"
    authors: ["Dheeru Dua", "Sameer Singh", "Matt Gardner"]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Did aristotle use a laptop? A question answering benchmark with implicit reasoning strategies"
    authors: ["Mor Geva", "Daniel Khashabi", "Elad Segal", "et al."]
    year: 2021
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "DREAM: Uncovering mental models behind language models"
    authors: ["Yuling Gu", "Bhavana Dalvi Mishra", "Peter Clark"]
    year: 2022
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training classifiers with natural language explanations"
    authors: ["Braden Hancock", "Paroma Varma", "Stephanie Wang", "et al."]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "When can models learn from explanations? a formal framework for understanding the roles of explanation data"
    authors: ["Peter Hase", "Mohit Bansal"]
    year: 2022
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Measuring mathematical problem solving with the math dataset"
    authors: ["Dan Hendrycks", "Collin Burns", "Saurav Kadavath", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2103.03874"
  - title: "Learning to solve arithmetic word problems with verb categorization"
    authors: ["Mohammad Javad Hosseini", "Hannaneh Hajishirzi", "Oren Etzioni", "et al."]
    year: 2014
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to reason deductively: Math word problem solving as complex relation extraction"
    authors: ["Zhanming Jie", "Jierui Li", "Wei Lu"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2203.10316"
  - title: "Scaling laws for neural language models"
    authors: ["Jared Kaplan", "Sam McCandlish", "Tom Henighan", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.08361"
  - title: "MAWPS: A math word problem repository"
    authors: ["Rik Koncel-Kedziorski", "Subhro Roy", "Aida Amini", "et al."]
    year: 2016
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Can language models learn from explanations in context?"
    authors: ["Andrew K. Lampinen", "Ishita Dasgupta", "Stephanie C.Y. Chan", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2204.02329"
  - title: "MWPToolkit: An open-source framework for deep learning-based math word problem solvers"
    authors: ["Yihuai Lan", "Lei Wang", "Qiyuan Zhang", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2109.00799"
  - title: "How many data points is a prompt worth?"
    authors: ["Teven Le Scao", "Alexander Rush"]
    year: 2021
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "The power of scale for parameter-efficient prompt tuning"
    authors: ["Brian Lester", "Rami Al-Rfou", "Noah Constant"]
    year: 2021
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Solving logic puzzles: From robust processing to precise semantics"
    authors: ["Iddo Lev", "Bill MacCartney", "Christopher Manning", "et al."]
    year: 2004
    venue: "Proceedings of the 2nd Workshop on Text Meaning and Interpretation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Prefix-tuning: Optimizing continuous prompts for generation"
    authors: ["Xiang Lisa Li", "Percy Liang"]
    year: 2021
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Explainable multi-hop verbal reasoning through internal monologue"
    authors: ["Zhengzhong Liang", "Steven Bethard", "Mihai Surdeanu"]
    year: 2021
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Program induction by rationale generation: Learning to solve and explain algebraic word problems"
    authors: ["Wang Ling", "Dani Yogatama", "Chris Dyer", "et al."]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing"
    authors: ["Pengfei Liu", "Weizhe Yuan", "Jinlan Fu", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2107.13586"
  - title: "Rationale-inspired natural language explanations with commonsense"
    authors: ["Bodhisattwa Prasad Majumder", "Oana-Maria Camburu", "Thomas Lukasiewicz", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2106.13876"
  - title: "Few-shot self-rationalization with natural language prompts"
    authors: ["Ana Marasović", "Iz Beltagy", "Doug Downey", "et al."]
    year: 2022
    venue: "NAACL Findings"
    doi: null
    url: null
    arxiv_id: null
  - title: "On faithfulness and factuality in abstractive summarization"
    authors: ["Joshua Maynez", "Shashi Narayan", "Bernd Bohnet", "et al."]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "A diverse corpus for evaluating and developing English math word problem solvers"
    authors: ["Shen Yun Miao", "Chao Chun Liang", "Keh Yih Su"]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Rethinking the role of demonstrations: What makes in-context learning work?"
    authors: ["Sewon Min", "Xinxi Lyu", "Ari Holtzman", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2202.12837"
  - title: "WT5?! Training text-to-text models to explain their predictions"
    authors: ["Sharan Narang", "Colin Raffel", "Katherine Lee", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.14546"
  - title: "Show your work: Scratchpads for intermediate computation with language models"
    authors: ["Maxwell Nye", "Anders Johan Andreassen", "Guy Gur-Ari", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2112.00114"
  - title: "Training language models to follow instructions with human feedback"
    authors: ["Long Ouyang", "Jeff Wu", "Xu Jiang", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2203.02155"
  - title: "Are NLP models really able to solve simple math word problems?"
    authors: ["Arkil Patel", "Satwik Bhattamishra", "Navin Goyal"]
    year: 2021
    venue: "NAACL"
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
  - title: "Reasoning like program executors"
    authors: ["Xinyu Pi", "Qian Liu", "Bei Chen", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2201.11473"
  - title: "Measuring and improving BERT's mathematical abilities by predicting the order of reasoning"
    authors: ["Piotr Piękos", "Mateusz Malinowski", "Henryk Michalewski"]
    year: 2021
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Scaling language models: Methods, analysis & insights from training Gopher"
    authors: ["Jack W. Rae", "Sebastian Borgeaud", "Trevor Cai", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2112.11446"
  - title: "Exploring the limits of transfer learning with a unified text-to-text transformer"
    authors: ["Colin Raffel", "Noam Shazeer", "Adam Roberts", "et al."]
    year: 2020
    venue: "Journal of Machine Learning Research"
    doi: null
    url: null
    arxiv_id: null
  - title: "SelfExplain: A self-explaining architecture for neural text classifiers"
    authors: ["Dheeraj Rajagopal", "Vidhisha Balachandran", "Eduard H. Hovy", "et al."]
    year: 2021
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Explain yourself! Leveraging language models for commonsense reasoning"
    authors: ["Nazneen Fatema Rajani", "Bryan McCann", "Caiming Xiong", "et al."]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "NumNet: Machine reading comprehension with numerical reasoning"
    authors: ["Qiu Ran", "Yankai Lin", "Peng Li", "et al."]
    year: 2019
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Measuring attribution in natural language generation models"
    authors: ["Hannah Rashkin", "Vitaly Nikolaev", "Matthew Lamm", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2112.12870"
  - title: "Teaching autoregressive language models complex tasks by demonstration"
    authors: ["Gabriel Recchia"]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2109.02102"
  - title: "A recipe for arbitrary text style transfer with large language models"
    authors: ["Emily Reif", "Daphne Ippolito", "Ann Yuan", "et al."]
    year: 2022
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Prompt programming for large language models: Beyond the few-shot paradigm"
    authors: ["Laria Reynolds", "Kyle McDonell"]
    year: 2021
    venue: "CHI Extended Abstracts"
    doi: null
    url: null
    arxiv_id: null
  - title: "Solving general arithmetic word problems"
    authors: ["Subhro Roy", "Dan Roth"]
    year: 2015
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reasoning about Quantities in Natural Language"
    authors: ["Subhro Roy", "Tim Vieira", "Dan Roth"]
    year: 2015
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "RuleBERT: Teaching soft rules to pre-trained language models"
    authors: ["Mohammed Saeed", "Naser Ahmadi", "Preslav Nakov", "et al."]
    year: 2021
    venue: "EMNLP"
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
  - title: "Generate & rank: A multi-task framework for math word problems"
    authors: ["Jianhao Shen", "Yichun Yin", "Lin Li", "et al."]
    year: 2021
    venue: "Findings of EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "CommonsenseQA: A question answering challenge targeting commonsense knowledge"
    authors: ["Alon Talmor", "Jonathan Herzig", "Nicholas Lourie", "et al."]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Leap-of-thought: Teaching pre-trained models to systematically reason over implicit knowledge"
    authors: ["Alon Talmor", "Oyvind Tafjord", "Peter Clark", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "CommonsenseQA 2.0: Exposing the limits of ai through gamification"
    authors: ["Alon Talmor", "Ori Yoran", "Ronan Le Bras", "et al."]
    year: 2021
    venue: "NeurIPS Datasets and Benchmarks"
    doi: null
    url: null
    arxiv_id: null
  - title: "Unifying language learning paradigms"
    authors: ["Yi Tay", "Mostafa Dehghani", "Vinh Q Tran", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2205.05131"
  - title: "LaMDA: Language models for dialog applications"
    authors: ["Romal Thoppilan", "Daniel De Freitas", "Jamie Hall", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2201.08239"
  - title: "Self-consistency improves chain of thought reasoning in language models"
    authors: ["Xuezhi Wang", "Jason Wei", "Dale Schuurmans", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2203.11171"
  - title: "Benchmarking generalization via in-context instructions on 1,600+ language tasks"
    authors: ["Yizhong Wang", "Swaroop Mishra", "Pegah Alipoormolabashi", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2204.07705"
  - title: "Finetuned language models are zero-shot learners"
    authors: ["Jason Wei", "Maarten Bosma", "Vincent Y. Zhao", "et al."]
    year: 2022
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Emergent abilities of large language models"
    authors: ["Jason Wei", "Yi Tay", "Rishi Bommasani", "et al."]
    year: 2022
    venue: "TMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reframing human-AI collaboration for generating free-text explanations"
    authors: ["Sarah Wiegreffe", "Jack Hessel", "Swabha Swayamdipta", "et al."]
    year: 2022
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Teach me to explain: A review of datasets for explainable NLP"
    authors: ["Sarah Wiegreffe", "Ana Marasović"]
    year: 2021
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Measuring association between labels and free-text rationales"
    authors: ["Sarah Wiegreffe", "Ana Marasović", "Noah A. Smith"]
    year: 2021
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "PromptChainer: Chaining large language model prompts through visual programming"
    authors: ["Tongshuang Wu", "Ellen Jiang", "Aaron Donsbach", "et al."]
    year: 2022
    venue: "CHI Extended Abstracts"
    doi: null
    url: null
    arxiv_id: null
  - title: "AI chains: Transparent and controllable human-AI interaction by chaining large language model prompts"
    authors: ["Tongshuang Wu", "Michael Terry", "Carrie Jun Cai"]
    year: 2022
    venue: "CHI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neural execution engines: Learning to execute subroutines"
    authors: ["Yujun Yan", "Kevin Swersky", "Danai Koutra", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Refining language models with compositional explanations"
    authors: ["Huihan Yao", "Ying Chen", "Qinyuan Ye", "et al."]
    year: 2021
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "The unreliability of explanations in few-shot in-context learning"
    authors: ["Xi Ye", "Greg Durrett"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2205.03401"
  - title: "Few-shot out-of-domain transfer learning of natural language explanations"
    authors: ["Yordan Yordanov", "Vid Kocijan", "Thomas Lukasiewicz", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2112.06204"
  - title: "Using \"annotator rationales\" to improve machine learning for text categorization"
    authors: ["Omar Zaidan", "Jason Eisner", "Christine Piatko"]
    year: 2007
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to execute"
    authors: ["Wojciech Zaremba", "Ilya Sutskever"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1410.4615"
  - title: "STaR: Bootstrapping reasoning with reasoning"
    authors: ["Eric Zelikman", "Yuhuai Wu", "Noah D. Goodman"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2203.14465"
  - title: "Calibrate before use: Improving few-shot performance of language models"
    authors: ["Tony Z. Zhao", "Eric Wallace", "Shi Feng", "et al."]
    year: 2021
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards interpretable natural language understanding with explanations as latent variables"
    authors: ["Wangchunshu Zhou", "Jinyi Hu", "Hanlin Zhang", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 4
  title: "Chain-of-thought prompting enables large language models to solve challenging math problems"
  page: 5
  image_path: "figures/wei-2022-chain-of-thought-fig.png"
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**Authors:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou
**Published:** 2022-01 · [Source](https://arxiv.org/abs/2201.11903)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Wei et al. introduce chain-of-thought (CoT) prompting: instead of giving the model only `<input, output>` exemplars before a test question, give it `<input, chain of thought, output>` triples — a few worked solutions where the reasoning is spelled out in natural language. With just eight hand-written exemplars, PaLM 540B's solve rate on the GSM8K math word problem benchmark jumps from 17.9% (standard prompting) to 56.9% (CoT), beating fine-tuned GPT-3 175B with a verifier (55%) for a new state of the art — and no parameter updates. The effect is uniformly large for arithmetic (GPT-3 175B: 15.6%→46.9% on GSM8K; PaLM 540B: 79.2%→93.3% on MAWPS), commonsense (StrategyQA: PaLM 540B 68.6%→77.8%, new SOTA; Sports Understanding: 80.5%→95.4%, beating the unaided human enthusiast at 84%), and symbolic tasks (Coin Flip OOD-4: 54.8%→90.2%). Three crucial caveats: (1) the benefit is *emergent* — CoT actively hurts models below ~10B parameters; LaMDA 8B drops from 5.3% to 4.8% on MAWPS, GPT-3 6.7B drops from 13.5% to 3.9% on MAWPS:SingleOp. (2) Ablations show the gain is not from "more compute" (dots instead of words don't help) nor from "reasoning post-hoc" (reasoning after the answer doesn't help) — natural-language intermediate steps that *precede* the answer are doing the work. (3) Robustness is high to annotator identity, exemplar choice, and exemplar order — but only ~46% of LaMDA 137B's correct chains are fully sound; the rest are "right answer, partly-broken reasoning," and the symbolic tasks reveal length-generalization is real but degrades as inputs grow longer than the few-shot exemplars. The most useful takeaway: for any reasoning-heavy task you'd otherwise throw fine-tuning at, try eight hand-written rationales first on a 100B+ model — it's free, no labels needed, and the gain often dwarfs everything else you can do.

## Key Takeaway

The textbook lesson from "scaling laws" is that bigger models smoothly get better at everything — but chain-of-thought is the opposite: it doesn't help at all below ~10B parameters and often actively hurts smaller models, then suddenly *unlocks* a whole new class of reasoning behaviour somewhere past 60-100B. You can't extrapolate from a 6B model's CoT performance to predict a 175B's; the curve is flat then hockey-stick. Even more counter-intuitive: when the authors tried to isolate what's doing the work — by giving the model the *equation* instead of words, or just *dots* to "buy thinking time," or putting the reasoning *after* the answer — none of these helped. It's specifically natural-language reasoning steps, generated *before* the answer, that matter. Writing out "Roger started with 5 balls, 2 cans of 3 each is 6, so 5+6 = 11" beats both "5+6=11" and ". . . . . . . . . . . . . . . . . . . . . . 11" by a wide margin. The mechanism isn't compute, isn't formal structure, isn't post-hoc rationalization — it's that the model uses its own generated prose as scaffolding for the next token.

## Implications

- **Try CoT before you fine-tune anything for reasoning**: If your task involves multi-step reasoning (math, logic, multi-hop QA, planning) and you have access to a 100B+ model, eight hand-written rationales can beat fine-tuned baselines that took weeks to build. Cost: ~10 minutes of writing.
- **Don't bother with CoT below ~10B parameters**: For smaller open models (under ~10B), CoT generally hurts or doesn't help. Use standard prompting, distillation from a larger CoT-prompted teacher, or fine-tuning on rationales — not zero-shot CoT exemplars.
- **Pick tasks where standard prompting has a flat scaling curve**: Wei explicitly notes CoT helps most when (a) the task is multi-step, (b) the model is huge, and (c) standard prompting already plateaus. If standard prompting already gets you to 90%, CoT won't move much (MAWPS:SingleOp barely budges).
- **Use CoT outputs as a debugging window, not as ground truth**: Roughly half of correct LaMDA 137B chains contained minor reasoning flaws ("right answer, wrong reasoning" — see Tables 9-11). For high-stakes work, validate the answer separately; the chain is interpretable scaffolding, not a proof.
- **Bolt on an external calculator if arithmetic shows up**: Across every model, applying a Python eval to extracted equations gave another big jump (e.g. LaMDA 137B on GSM8K: 14.3% → 17.8%; UL2 20B on MAWPS: 19.1% → 42.7%). The model can plan the math; let it skip the arithmetic.
- **Annotator style barely matters; rationale presence is everything**: Three different authors wrote independent CoT exemplars; all three beat standard prompting by a large margin on eight benchmarks. Even random GSM8K crowd-worker rationales worked. Don't over-engineer the prose.
- **Length generalization works but degrades**: On symbolic tasks (last-letter concatenation, coin flip), CoT lets the model handle inputs longer than the few-shot exemplars — but accuracy on 4-token inputs after seeing only 2-token exemplars is markedly lower than in-domain (PaLM 540B last-letter: 99.4% in-domain, 63% on OOD-4). Don't assume CoT transfers indefinitely to longer chains; stress-test at your real input length.
- **The technique is the unlock, the model size is the gate**: This paper is the strongest single piece of evidence that *prompting is a research surface*, not just a UX detail — and that the same model can be unlocked for whole new tasks by changing what you put in front of it. Treat prompt design as a first-class engineering activity.

## How to Apply It (method)

**Scenario:** You're building a customer-support triage agent on top of GPT-4 / Claude / Gemini, and the model keeps making one-shot errors on multi-step billing questions — refund calculations involving tax, partial-period billing, promo codes. Standard few-shot prompts ("here are five Q&A pairs, now answer") plateau at ~70% correct against a hand-graded internal eval set. You want to try CoT before paying for fine-tuning.

**Steps:**

1. **Build a hand-graded eval set of 50-200 real reasoning failures.** Pull actual past tickets where the agent got it wrong. Each row: `(customer message, correct response, correct refund amount)`. Don't rely on synthetic data — the failure modes you care about are the ones the model is making *today*.

2. **Hand-write 6-8 chain-of-thought exemplars** that cover the failure types. Each exemplar has three parts: the input message, an explicit step-by-step reasoning trace in natural language, and the final answer. Keep the language plain — declarative sentences, not academic prose. Example format (from Wei et al.'s GSM8K prompt):

   ```
   Q: Customer paid $120 on Jan 5 for a monthly subscription, cancelled on Jan 20.
      They have a 10% loyalty discount on file. What's the refund?

   A: The customer paid $120 for the period Jan 5 to Feb 5 (31 days).
      They used the service from Jan 5 to Jan 20, which is 15 days.
      That's 15/31 of the month, so $120 * 15/31 = $58.06 used.
      The unused portion is $120 - $58.06 = $61.94.
      They have a 10% loyalty discount, but that was already applied to the
      original $120, so no further adjustment is needed.
      The refund is $61.94. The answer is $61.94.
   ```

3. **Compose the full prompt** as: short system instruction → 6-8 hand-written CoT exemplars → the actual test question, leaving the answer slot open. Match exemplar formatting *exactly* — Wei et al. explicitly avoided prompt engineering and still got strong gains; consistency matters more than cleverness.

4. **Run two conditions on the eval set:**
   - **Baseline**: same exemplars but without the rationale (just Q → A).
   - **CoT**: with the rationale (Q → reasoning → A).

   Greedy decoding (temperature 0) for both. Score by exact-match on the final answer, not on the reasoning. (This is what Wei et al. did; they later showed self-consistency sampling on top adds more, but start simple.)

5. **Optional ablation — sanity-check what's doing the work.** If CoT shows a big gain, before assuming it generalizes, run two more conditions on a small subset:
   - **Equation/structured only**: give the model just the math, no prose.
   - **Reasoning after answer**: put the chain of thought *after* the final answer.

   In Wei et al.'s paper both ablations performed about the same as the baseline, confirming the natural-language-before-answer is doing real work. If your domain shows the same pattern, you have evidence the gain will hold up out of distribution.

6. **Bolt on an external tool for the deterministic step.** For billing math specifically, extract the equations from the model's chain and run them through Python (`eval` with safety bounds, or a small expression evaluator). Wei et al. showed this adds another 3-15 points on top of CoT across all five arithmetic benchmarks.

7. **Audit the rationale quality on a sample of correct outputs.** Wei et al. found ~46% of correct chains had minor reasoning flaws (right answer, slightly broken logic). Spot-check 20-30 successes to see if your domain shows the same — if so, don't surface the chain to customers without a second-pass check.

**Expected outcome:** A ~10-40 percentage point lift on multi-step reasoning failures, no training run required, and an interpretable trace you can show to QA or to the customer. The technique generalizes to any text-to-text task with multi-step structure — refund logic, eligibility rules, troubleshooting flows, planning. Importantly, if the baseline was already strong (>90%), CoT will give you little; the gain is concentrated on tasks that are *hard* and where the smaller model was hitting a flat scaling curve.

## Best Figure

![Figure 4 — Chain-of-thought prompting enables large language models to solve challenging math problems (page 5)](figures/wei-2022-chain-of-thought-fig.png)

**Image Candidates:**
- Figure 4 (p. 5): A 3×3 grid of solve-rate-vs-scale curves for three model families (LaMDA, GPT, PaLM) × three math benchmarks (GSM8K, SVAMP, MAWPS), with standard vs CoT vs prior supervised best — the single clearest visualization of the paper's central "emergent at scale" story.
- Figure 2 (p. 2): A single bar chart on GSM8K showing PaLM 540B with CoT reaching 57%, beating fine-tuned GPT-3 with verifier — most punchy for a headline image but only one benchmark.
- Figure 1 (p. 1): The side-by-side worked example showing the standard prompt giving "27" and the CoT prompt working through "23 - 20 = 3, 3 + 6 = 9" — the clearest *what is CoT* image but not a result.

**Best Image:**
- **Figure Name:** Figure 4: "Chain-of-thought prompting enables large language models to solve challenging math problems."
- **Figure Page:** 5
- **Slide Caption:** Chain-of-thought prompting is an emergent ability of scale: it doesn't help (and often hurts) below ~10B parameters, but unlocks dramatic gains past ~100B across three model families and three math benchmarks.
- **Description:** Figure 4 is a 3×3 grid: rows are three math benchmarks (GSM8K, SVAMP, MAWPS), columns are three model families (LaMDA up to 137B, GPT up to 175B, PaLM up to 540B). Each panel shows solve-rate (y) versus model scale on a log scale (x), with three series — black: standard prompting, blue: chain-of-thought, orange dashed: prior supervised SOTA. The visual story is unmistakable: at small scales both curves hug zero, then somewhere between 60B and 175B the CoT curve dramatically peels away from standard prompting and, for PaLM 540B on GSM8K and MAWPS, leaps over the prior supervised state-of-the-art line. This single grid is the paper's central argument made graphic: CoT is not a smooth improvement but an emergent capability that suddenly appears at scale, and it does so consistently across three independent model families.

## What Experts Overlook

Most experts read this paper and walk away with "CoT is great for big models." What's easier to miss — and is genuinely load-bearing for the result — is the *ablation hierarchy* in Section 3.3 and Figure 5. Wei et al. didn't just compare CoT to standard prompting; they tested three competing explanations and ruled each one out. (1) "It works because the model is forced to produce the math equation" — they tested "equation only" prompting and showed it improves performance on simple problems but flatly fails to lift GSM8K beyond baseline. (2) "It works because the model gets more compute / more tokens to think" — they tested "variable compute only" (literally dots, `. . . . . .`, equal in length to the equation) and got baseline performance. (3) "It works because CoT activates relevant pretrained knowledge by chaining concepts" — they tested "reasoning after answer" (model emits the answer first, then justifies) and again got baseline performance. The only configuration that gave the lift was natural-language reasoning steps emitted *before* the answer. This is what licences the strong claim "the sequential reasoning embodied in the chain of thought is useful for reasons beyond just activating knowledge" — and it's why follow-up papers (self-consistency, tree-of-thoughts, least-to-most) all preserve that exact ordering.

**Why it matters:** This ablation structure tells you what mechanism you're actually buying when you use CoT — and therefore which CoT-adjacent ideas will and won't work. If "variable compute" worked, then any padding trick (long preambles, irrelevant context) should give you the gain. It doesn't. If "post-hoc explanation" worked, then "explain your answer" instructions appended after generation would do the same job. They don't. The mechanism is specifically: the model's own generated prose, before the answer slot, serves as autoregressive scaffolding that conditions every subsequent token. That's a falsifiable hypothesis with concrete operational consequences.

**Example of good use:** A founder building a sales-qualification agent wants the model to reason about a lead's stage, intent, and fit before recommending an action. Knowing the ablation result, they place the reasoning explicitly *before* the recommendation in their few-shot exemplars ("Lead said X, which suggests Y, and they're in stage Z, so the right action is…") rather than asking for a one-line recommendation followed by justification. They get cleaner reasoning AND a better recommendation, because the model conditions on its own analysis. They also skip the temptation to add "think step by step" filler tokens — they know dots don't work, words do.

**Example of misapplication:** A team building a code-review bot reads "CoT helps reasoning" and adds the instruction "explain your decision in detail after recommending the change" to their prompt. They get verbose, plausible-sounding justifications that read like CoT — but the recommendation quality doesn't improve, because the chain comes *after* the answer. They conclude "CoT doesn't work for our domain" and abandon the technique, when in fact they ran the ablation Wei et al. explicitly identified as not working. The fix is to flip the order: ask the model to think through "what's the bug, what's the intent, what's the cleanest fix" *before* writing the patch suggestion.

## Extracted Prompts

**Prompt explanation:** Few-shot exemplar set for math word problems (Table 20). One set of eight `<question, chain-of-thought, answer>` triples that was used for all math word problem benchmarks except AQuA. The "chain of thought" portion is shown after each `A:`. These exemplars were composed manually by Annotator A without prompt engineering — robustness to annotator was tested separately.

```
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
A: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6. The answer is 6.

Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer is 5.

Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
A: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39.

Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
A: Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8. The answer is 8.

Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
A: Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9. The answer is 9.

Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
A: There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29.

Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
A: Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls. The answer is 33.

Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8.
```

**Prompt explanation:** Few-shot exemplar set for AQuA algebraic multiple-choice word problems (Table 21). A separate four-exemplar set because AQuA is multiple-choice rather than free-response. Exemplars and solutions taken from the AQuA training set.

```
Q: John found that the average of 15 numbers is 40. If 10 is added to each number then the mean of the numbers is?
Answer Choices: (a) 50 (b) 45 (c) 65 (d) 78 (e) 64
A: If 10 is added to each number, then the mean of the numbers also increases by 10. So the new mean would be 50. The answer is (a).

Q: If a / b = 3/4 and 8a + 5b = 22,then find the value of a.
Answer Choices: (a) 1/2 (b) 3/2 (c) 5/2 (d) 4/2 (e) 7/2
A: If a / b = 3/4, then b = 4a / 3. So 8a + 5(4a / 3) = 22. This simplifies to 8a + 20a / 3 = 22, which means 44a / 3 = 22. So a is equal to 3/2. The answer is (b).

Q: A person is traveling at 20 km/hr and reached his destiny in 2.5 hr then find the distance?
Answer Choices: (a) 53 km (b) 55 km (c) 52 km (d) 60 km (e) 50 km
A: The distance that the person traveled would have been 20 km/hr * 2.5 hrs = 50 km. The answer is (e).

Q: How many keystrokes are needed to type the numbers from 1 to 500?
Answer Choices: (a) 1156 (b) 1392 (c) 1480 (d) 1562 (e) 1788
A: There are 9 one-digit numbers from 1 to 9. There are 90 two-digit numbers from 10 to 99. There are 401 three-digit numbers from 100 to 500. 9 + 90(2) + 401(3) = 1392. The answer is (b).
```

**Prompt explanation:** Few-shot exemplar set for the last-letter concatenation symbolic task (Table 22). Four exemplars of two-word names; the model is then evaluated on 3- and 4-word names to test length generalization.

```
Q: Take the last letters of the words in "Elon Musk" and concatenate them.
A: The last letter of "Elon" is "n". The last letter of "Musk" is "k". Concatenating them is "nk". The answer is nk.

Q: Take the last letters of the words in "Larry Page" and concatenate them.
A: The last letter of "Larry" is "y". The last letter of "Page" is "e". Concatenating them is "ye". The answer is ye.

Q: Take the last letters of the words in "Sergey Brin" and concatenate them.
A: The last letter of "Sergey" is "y". The last letter of "Brin" is "n". Concatenating them is "yn". The answer is yn.

Q: Take the last letters of the words in "Bill Gates" and concatenate them.
A: The last letter of "Bill" is "l". The last letter of "Gates" is "s". Concatenating them is "ls". The answer is ls.
```

**Prompt explanation:** Few-shot exemplar set for the coin-flip state-tracking task (Table 23). Trains the model on two-actor flips; OOD evaluation uses 3- and 4-actor flips to test length generalization on a discrete state-tracking task.

```
Q: A coin is heads up. Ka flips the coin. Sherrie flips the coin. Is the coin still heads up?
A: The coin was flipped by Ka and Sherrie. So the coin was flipped 2 times, which is an even number. The coin started heads up, so after an even number of flips, it will still be heads up. So the answer is yes.

Q: A coin is heads up. Jamey flips the coin. Teressa flips the coin. Is the coin still heads up?
A: The coin was flipped by Jamey and Teressa. So the coin was flipped 2 times, which is an even number. The coin started heads up, so after an even number of flips, it will still be heads up. So the answer is yes.

Q: A coin is heads up. Maybelle flips the coin. Shalonda does not flip the coin. Is the coin still heads up?
A: The coin was flipped by Maybelle. So the coin was flipped 1 time, which is an odd number. The coin started heads up, so after an odd number of flips, it will be tails up. So the answer is no.
```

(Additional full prompt sets for CSQA, StrategyQA, Date Understanding, Sports Understanding, and SayCan are given in Tables 24–28 of the paper's Appendix G; they follow the same `Q: ... A: <reasoning steps> ... The answer is X.` pattern.)

## Citations

- Brown et al. 2020 — *Language models are few-shot learners* (NeurIPS) — the few-shot prompting baseline this paper extends.
- Cobbe et al. 2021 — *Training verifiers to solve math word problems* (arXiv:2110.14168) — source of GSM8K and the fine-tuned-with-verifier baseline that PaLM 540B + CoT surpasses.
- Wei et al. 2022b — *Emergent abilities of large language models* (TMLR) — the companion paper that frames CoT as emergent at scale.
- Wang et al. 2022a — *Self-consistency improves chain of thought reasoning* (arXiv:2203.11171) — follow-up showing majority vote over sampled CoTs adds further gains.
- Nye et al. 2021 — *Show your work: Scratchpads for intermediate computation* (arXiv:2112.00114) — closest prior work, used fine-tuning rather than prompting.
- Ling et al. 2017 — *Program induction by rationale generation* (ACL) — original natural-language rationales for math word problems, trained from scratch.
- Thoppilan et al. 2022 — *LaMDA* (arXiv:2201.08239) — one of the three model families evaluated.
- Chowdhery et al. (via PaLM) — PaLM model used at 8B, 62B, 540B scales.
- Ahn et al. 2022 — *Do as I can, not as I say (SayCan)* (arXiv:2204.01691) — source of the SayCan robot-planning benchmark.
- Geva et al. 2021 — *StrategyQA* (TACL) — source of the StrategyQA multi-hop commonsense benchmark.

(Full structured citation list available in frontmatter `citations[]` — 83 references extracted from the paper's bibliography.)

## Related Digests

- [[zhou-2022-least-to-most-prompting]] — Least-to-Most Prompting Enables Complex Reasoning in Large Language Models (direct successor: solves CoT's length-generalization failure mode by decomposing first)
- [[fernando-2023-promptbreeder]] — Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution (automates the prompt-engineering step CoT relies on)
- [[radford-2019-gpt2-multitask]] — Language Models are Unsupervised Multitask Learners (GPT-2) (foundational few-shot prompting paper that CoT builds on)
- [[chen-2023-memwalker]] — Walking Down the Memory Maze: Beyond Context Limit through Interactive Reading (uses CoT reasoning at every hop of an interactive long-document agent)
- [[shen-2023-icl-not-gd]] — Do pretrained Transformers Learn In-Context by Gradient Descent? (offers a competing mechanistic story for what in-context learning is actually doing, relevant to the CoT-as-scaffolding hypothesis)

## Reviewer Notes

**Overall severity:** Clean

All claims in the digest were checked against the paper text:
- GSM8K 17.9% → 56.9% (PaLM 540B): Table 1, Table 2.
- GPT-3 175B GSM8K 15.6% → 46.9%: Table 1, Table 2.
- LaMDA 8B MAWPS 5.3% → 4.8%: Table 2.
- GPT-3 6.7B MAWPS:SingleOp 13.5% → 3.9%: Table 3.
- "Beating fine-tuned GPT-3 with verifier (55%) on GSM8K": Figure 2 and Table 1 prior-best row (55%, Cobbe et al. 2021).
- StrategyQA 68.6% → 77.8%: Table 4. Sports Understanding 80.5% → 95.4%: Table 4. Human baseline 84% on Sports: Section 4 results.
- Coin Flip OOD-4 54.8% → 90.2%: Table 5.
- "~46% of correct LaMDA 137B chains had minor flaws": Section 3.2 and Appendix D.1.
- Eight hand-written exemplars, robustness to annotator/exemplar/order: Section 3.4, Tables 6-7, Appendix A.2.
- Ablation conclusions (equation only / variable compute / reasoning after answer): Section 3.3, Figure 5.
- Calculator augmentation gains: Table 1 "+ ext. calc" rows.
- Emergent-at-scale framing: Section 3.2 and Appendix A.1 (error analysis on 62B vs 540B).

No claims were extrapolated beyond what the paper measured. The "fine-tuned GPT-3 + verifier" baseline is correctly attributed to Cobbe et al. 2021. The "human enthusiast" baseline on Sports Understanding (84%) is reported in Section 4 of the paper. No invented metrics, no invented tool names, no fabricated authors. The application scenario in the "How to Apply It" section is explicitly framed as a transfer to a domain the paper did *not* study (customer-support refund logic), with the principle ("try CoT before fine-tuning, use eight rationales, ablate to verify mechanism") taken directly from the paper's experimental design.
