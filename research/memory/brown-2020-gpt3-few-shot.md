---
corpus: agentic-memory
kind: paper-digest
slug: brown-2020-gpt3-few-shot
title: "Language Models are Few-Shot Learners"
authors:
  - "Brown, Tom B."
  - "Mann, Benjamin"
  - "Ryder, Nick"
  - "Subbiah, Melanie"
  - "Kaplan, Jared"
  - "Dhariwal, Prafulla"
  - "Neelakantan, Arvind"
  - "Shyam, Pranav"
  - "Sastry, Girish"
  - "Askell, Amanda"
  - "Agarwal, Sandhini"
  - "Herbert-Voss, Ariel"
  - "Krueger, Gretchen"
  - "Henighan, Tom"
  - "Child, Rewon"
  - "Ramesh, Aditya"
  - "Ziegler, Daniel M."
  - "Wu, Jeffrey"
  - "Winter, Clemens"
  - "Hesse, Christopher"
  - "Chen, Mark"
  - "Sigler, Eric"
  - "Litwin, Mateusz"
  - "Gray, Scott"
  - "Chess, Benjamin"
  - "Clark, Jack"
  - "Berner, Christopher"
  - "McCandlish, Sam"
  - "Radford, Alec"
  - "Sutskever, Ilya"
  - "Amodei, Dario"
year: 2020
publication_date: "2020-07"
venue: "NeurIPS 2020 / arXiv preprint"
source_url: "https://arxiv.org/abs/2005.14165"
doi: null
arxiv_id: "2005.14165"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Just scaling a vanilla autoregressive transformer to 175B parameters trained on 300B tokens is enough to turn the prompt — a few text demonstrations stuffed into a 2,048-token context — into a competitive substitute for gradient-based fine-tuning, with no weight updates at inference time."
topics:
  - few-shot-learning
  - in-context-learning
  - large-language-models
  - parametric-memory
  - scaling-laws
  - prompt-engineering
  - meta-learning
  - data-contamination
tags:
  - paper
  - foundational
  - gpt-3
  - openai
  - llm
  - memory-architecture
entities:
  - brown-tom
  - kaplan-jared
  - mccandlish-sam
  - radford-alec
  - sutskever-ilya
  - amodei-dario
  - openai
related_digests:
  - kusupati-2022-matryoshka-representation-learning
  - lewis-2020-rag-knowledge-nlp
  - packer-2023-memgpt-os
  - gao-2022-hyde-zero-shot-retrieval
  - maharana-2024-locomo
  - sukhbaatar-2015-end-to-end-memory-networks
citations:
  - title: "Learning to learn by gradient descent by gradient descent"
    authors: ["Marcin Andrychowicz", "Misha Denil", "Sergio Gomez", "et al."]
    year: 2016
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Massively multilingual neural machine translation"
    authors: ["Roee Aharoni", "Melvin Johnson", "Orhan Firat"]
    year: 2019
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language (technology) is power: A critical survey of \"bias\" in nlp"
    authors: ["Su Lin Blodgett", "Solon Barocas", "Hal Daumé III", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2005.14050"
  - title: "Semantic parsing on freebase from question-answer pairs"
    authors: ["Jonathan Berant", "Andrew Chou", "Roy Frostig", "et al."]
    year: 2013
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "The fifth PASCAL recognizing textual entailment challenge"
    authors: ["Luisa Bentivogli", "Ido Dagan", "Hoa Trang Dang", "et al."]
    year: 2009
    venue: "TAC"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sentiwordnet 3.0: an enhanced lexical resource for sentiment analysis and opinion mining"
    authors: ["Stefano Baccianella", "Andrea Esuli", "Fabrizio Sebastiani"]
    year: 2010
    venue: "LREC"
    doi: null
    url: null
    arxiv_id: null
  - title: "The second PASCAL recognising textual entailment challenge"
    authors: ["Roy Bar Haim", "Ido Dagan", "Bill Dolan", "et al."]
    year: 2006
    venue: "PASCAL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Experience grounds language"
    authors: ["Yonatan Bisk", "Ari Holtzman", "Jesse Thomason", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.10151"
  - title: "Estimating or propagating gradients through stochastic neurons for conditional computation"
    authors: ["Yoshua Bengio", "Nicholas Léonard", "Aaron C. Courville"]
    year: 2013
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "PIQA: Reasoning about physical commonsense in natural language"
    authors: ["Yonatan Bisk", "Rowan Zellers", "Ronan Le Bras", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.11641"
  - title: "Multitask learning"
    authors: ["Rich Caruana"]
    year: 1997
    venue: "Machine Learning"
    doi: null
    url: null
    arxiv_id: null
  - title: "Acquiring a single new word"
    authors: ["Susan Carey", "Elsa Bartlett"]
    year: 1978
    venue: "Stanford Child Language Conference"
    doi: null
    url: null
    arxiv_id: null
  - title: "Think you have solved question answering? try arc, the ai2 reasoning challenge"
    authors: ["Peter Clark", "Isaac Cowhey", "Oren Etzioni", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1803.05457"
  - title: "Generating long sequences with sparse transformers"
    authors: ["Rewon Child", "Scott Gray", "Alec Radford", "Ilya Sutskever"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "QuAC: Question answering in context"
    authors: ["Eunsol Choi", "He He", "Mohit Iyyer", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "BoolQ: Exploring the surprising difficulty of natural yes/no questions"
    authors: ["Christopher Clark", "Kenton Lee", "Ming-Wei Chang", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.10044"
  - title: "Uniter: Learning universal image-text representations"
    authors: ["Yen-Chun Chen", "Linjie Li", "Licheng Yu", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.11740"
  - title: "The trouble with bias"
    authors: ["Kate Crawford"]
    year: 2017
    venue: "NeurIPS Keynote"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "Kristina Toutanova"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "The PASCAL recognising textual entailment challenge"
    authors: ["Ido Dagan", "Oren Glickman", "Bernardo Magnini"]
    year: 2006
    venue: "Springer"
    doi: null
    url: null
    arxiv_id: null
  - title: "Universal transformers"
    authors: ["Mostafa Dehghani", "Stephan Gouws", "Oriol Vinyals", "et al."]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "Edinburgh's phrase-based machine translation systems for wmt-14"
    authors: ["Nadir Durrani", "Barry Haddow", "Philipp Koehn", "Kenneth Heafield"]
    year: 2014
    venue: "WMT"
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
  - title: "The CommitmentBank: Investigating projection in naturally occurring discourse"
    authors: ["Marie-Catherine De Marneffe", "Mandy Simons", "Judith Tonhauser"]
    year: 2019
    venue: "Sinn und Bedeutung"
    doi: null
    url: null
    arxiv_id: null
  - title: "RL2: Fast reinforcement learning via slow reinforcement learning"
    authors: ["Yan Duan", "John Schulman", "Xi Chen", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1611.02779"
  - title: "DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs"
    authors: ["Dheeru Dua", "Yizhong Wang", "Pradeep Dasigi", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1903.00161"
  - title: "Transformer-XL: Attentive language models beyond a fixed-length context"
    authors: ["Zihang Dai", "Zhilin Yang", "Yiming Yang", "et al."]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "Understanding back-translation at scale"
    authors: ["Sergey Edunov", "Myle Ott", "Michael Auli", "David Grangier"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1808.09381"
  - title: "Model-agnostic meta-learning for fast adaptation of deep networks"
    authors: ["Chelsea Finn", "Pieter Abbeel", "Sergey Levine"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1703.03400"
  - title: "Lipstick on a pig: Debiasing methods cover up systematic gender biases in word embeddings but do not remove them"
    authors: ["Hila Gonen", "Yoav Goldberg"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1903.03862"
  - title: "REALM: Retrieval-augmented language model pre-training"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2002.08909"
  - title: "The third PASCAL recognizing textual entailment challenge"
    authors: ["Danilo Giampiccolo", "Bernardo Magnini", "Ido Dagan", "Bill Dolan"]
    year: 2007
    venue: "ACL workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adaptive computation time for recurrent neural networks"
    authors: ["Alex Graves"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "Annotation artifacts in natural language inference data"
    authors: ["Suchin Gururangan", "Swabha Swayamdipta", "Omer Levy", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1803.02324"
  - title: "GLTR: Statistical detection and visualization of generated text"
    authors: ["Sebastian Gehrmann", "Hendrik Strobelt", "Alexander M. Rush"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1906.04043"
  - title: "Meta-learning for low-resource neural machine translation"
    authors: ["Jiatao Gu", "Yong Wang", "Yun Chen", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1808.08437"
  - title: "AI and efficiency"
    authors: ["Daniel Hernandez", "Tom Brown"]
    year: 2020
    venue: "OpenAI blog"
    doi: null
    url: null
    arxiv_id: null
  - title: "The curious case of neural text degeneration"
    authors: ["Ari Holtzman", "Jan Buys", "Maxwell Forbes", "Yejin Choi"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1904.09751"
  - title: "Pretrained transformers improve out of distribution robustness"
    authors: ["Dan Hendrycks", "Xiaoyuan Liu", "Eric Wallace", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.06100"
  - title: "Deep learning scaling is predictable, empirically"
    authors: ["Joel Hestness", "Sharan Narang", "Newsha Ardalani", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1712.00409"
  - title: "Universal language model fine-tuning for text classification"
    authors: ["Jeremy Howard", "Sebastian Ruder"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1801.06146"
  - title: "Distilling the knowledge in a neural network"
    authors: ["Geoffrey Hinton", "Oriol Vinyals", "Jeff Dean"]
    year: 2015
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1503.02531"
  - title: "Learning to Learn Using Gradient Descent"
    authors: ["Sepp Hochreiter", "A. Steven Younger", "Peter R. Conwell"]
    year: 2001
    venue: "ICANN"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reducing sentiment bias in language models via counterfactual evaluation"
    authors: ["Po-Sen Huang", "Huan Zhang", "Ray Jiang", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.03064"
  - title: "A neural network for factoid question answering over paragraphs"
    authors: ["Mohit Iyyer", "Jordan Boyd-Graber", "Leonardo Claudino", "et al."]
    year: 2014
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Automatic detection of generated text is easiest when humans are fooled"
    authors: ["Daphne Ippolito", "Daniel Duckworth", "Chris Callison-Burch", "Douglas Eck"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.00650"
  - title: "TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension"
    authors: ["Mandar Joshi", "Eunsol Choi", "Daniel S. Weld", "Luke Zettlemoyer"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1705.03551"
  - title: "Exploring the limits of language modeling"
    authors: ["Rafal Jozefowicz", "Oriol Vinyals", "Mike Schuster", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1602.02410"
  - title: "TinyBERT: Distilling BERT for natural language understanding"
    authors: ["Xiaoqi Jiao", "Yichun Yin", "Lifeng Shang", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.10351"
  - title: "Looking beyond the surface: A challenge set for reading comprehension over multiple sentences"
    authors: ["Daniel Khashabi", "Snigdha Chaturvedi", "Michael Roth", "et al."]
    year: 2018
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "UnifiedQA: Crossing format boundaries with a single QA system"
    authors: ["Daniel Khashabi", "Tushar Khot", "Ashish Sabharwal", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2005.00700"
  - title: "All the news that's fit to fabricate: AI-generated text as a tool of media misinformation"
    authors: ["Sarah E. Kreps", "Miles McCain", "Miles Brundage"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Scaling laws for neural language models"
    authors: ["Jared Kaplan", "Sam McCandlish", "Tom Henighan", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Natural questions: a benchmark for question answering research"
    authors: ["Tom Kwiatkowski", "Jennimaria Palomaki", "Olivia Redfield", "et al."]
    year: 2019
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sequence-level knowledge distillation"
    authors: ["Yoon Kim", "Alexander M. Rush"]
    year: 2016
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "NLTK: The Natural Language Toolkit"
    authors: ["Edward Loper", "Steven Bird"]
    year: 2002
    venue: "ACL workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "Cross-lingual language model pretraining"
    authors: ["Guillaume Lample", "Alexis Conneau"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1901.07291"
  - title: "ALBERT: A lite BERT for self-supervised learning of language representations"
    authors: ["Zhenzhong Lan", "Mingda Chen", "Sebastian Goodman", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.11942"
  - title: "Adversarial training for large neural language models"
    authors: ["Xiaodong Liu", "Hao Cheng", "Pengcheng He", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.08994"
  - title: "Story ending prediction by transferable BERT"
    authors: ["Zhongyang Li", "Xiao Ding", "Ting Liu"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.07504"
  - title: "The Winograd schema challenge"
    authors: ["Hector Levesque", "Ernest Davis", "Leora Morgenstern"]
    year: 2012
    venue: "KR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multilingual denoising pre-training for neural machine translation (mBART)"
    authors: ["Yinhan Liu", "Jiatao Gu", "Naman Goyal", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.08210"
  - title: "Representation learning using multi-task deep neural networks for semantic classification and information retrieval"
    authors: ["Xiaodong Liu", "Jianfeng Gao", "Xiaodong He", "et al."]
    year: 2015
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Decoupled weight decay regularization"
    authors: ["Ilya Loshchilov", "Frank Hutter"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1711.05101"
  - title: "Improving multi-task deep neural networks via knowledge distillation for natural language understanding"
    authors: ["Xiaodong Liu", "Pengcheng He", "Weizhu Chen", "Jianfeng Gao"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1904.09482"
  - title: "Multi-task deep neural networks for natural language understanding"
    authors: ["Xiaodong Liu", "Pengcheng He", "Weizhu Chen", "Jianfeng Gao"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1901.11504"
  - title: "How can we accelerate progress towards human-like linguistic generalization?"
    authors: ["Tal Linzen"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2005.00955"
  - title: "BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension"
    authors: ["Mike Lewis", "Yinhan Liu", "Naman Goyal", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1910.13461"
  - title: "Learning to optimize neural nets"
    authors: ["Ke Li", "Jitendra Malik"]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1703.00441"
  - title: "RoBERTa: A robustly optimized BERT pretraining approach"
    authors: ["Yinhan Liu", "Myle Ott", "Naman Goyal", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1907.11692"
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2005.11401"
  - title: "Generating Wikipedia by summarizing long sequences"
    authors: ["Peter J. Liu", "Mohammad Saleh", "Etienne Pot", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1801.10198"
  - title: "Train large, then compress: Rethinking model size for efficient training and inference of transformers"
    authors: ["Zhuohan Li", "Eric Wallace", "Sheng Shen", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "RACE: Large-scale reading comprehension dataset from examinations"
    authors: ["Guokun Lai", "Qizhe Xie", "Hanxiao Liu", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1704.04683"
  - title: "TTTTTackling WinoGrande schemas"
    authors: ["Sheng-Chieh Lin", "Jheng-Hong Yang", "Rodrigo Nogueira", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2003.08380"
  - title: "Information-based objective functions for active data selection"
    authors: ["David MacKay"]
    year: 1992
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learned in translation: Contextualized word vectors"
    authors: ["Bryan McCann", "James Bradbury", "Caiming Xiong", "Richard Socher"]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient estimation of word representations in vector space"
    authors: ["Tomas Mikolov", "Kai Chen", "Greg Corrado", "Jeffrey Dean"]
    year: 2013
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1301.3781"
  - title: "A corpus and evaluation framework for deeper understanding of commonsense stories (StoryCloze)"
    authors: ["Nasrin Mostafazadeh", "Nathanael Chambers", "Xiaodong He", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1604.01696"
  - title: "Can a suit of armor conduct electricity? a new dataset for open book question answering"
    authors: ["Todor Mihaylov", "Peter Clark", "Tushar Khot", "Ashish Sabharwal"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1809.02789"
  - title: "An empirical model of large-batch training"
    authors: ["Sam McCandlish", "Jared Kaplan", "Dario Amodei", "OpenAI Dota Team"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "The Penn Treebank: annotating predicate argument structure"
    authors: ["Mitchell Marcus", "Grace Kim", "Mary Ann Marcinkiewicz", "et al."]
    year: 1994
    venue: "HLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "The natural language decathlon: Multitask learning as question answering (decaNLP)"
    authors: ["Bryan McCann", "Nitish Shirish Keskar", "Caiming Xiong", "Richard Socher"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1806.08730"
  - title: "Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference"
    authors: ["R. Thomas McCoy", "Ellie Pavlick", "Tal Linzen"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1902.01007"
  - title: "Model cards for model reporting"
    authors: ["Margaret Mitchell", "Simone Wu", "Andrew Zaldivar", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "StereoSet: Measuring stereotypical bias in pretrained language models"
    authors: ["Moin Nadeem", "Anna Bethke", "Siva Reddy"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.09456"
  - title: "Probing neural network comprehension of natural language arguments"
    authors: ["Timothy Niven", "Hung-Yu Kao"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1907.07355"
  - title: "Natural language corpus data"
    authors: ["Peter Norvig"]
    year: 2009
    venue: "Beautiful Data, O'Reilly"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fair is better than sensational: Man is to doctor as woman is to doctor"
    authors: ["Malvina Nissim", "Rik van Noord", "Rob van der Goot"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.09866"
  - title: "Adversarial NLI: A new benchmark for natural language understanding"
    authors: ["Yixin Nie", "Adina Williams", "Emily Dinan", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1910.14599"
  - title: "WiC: 10,000 example pairs for evaluating context-sensitive representations"
    authors: ["Mohammad Taher Pilehvar", "Jose Camacho-Collados"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1808.09121"
  - title: "Sentence encoders on STILTs: Supplementary training on intermediate labeled-data tasks"
    authors: ["Jason Phang", "Thibault Févry", "Samuel R. Bowman"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1811.01088"
  - title: "Collecting diverse natural language inference problems for sentence representation evaluation"
    authors: ["Adam Poliak", "Aparajita Haldar", "Rachel Rudinger", "et al."]
    year: 2018
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "The LAMBADA dataset: Word prediction requiring a broad discourse context"
    authors: ["Denis Paperno", "Germán Kruszewski", "Angeliki Lazaridou", "et al."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1606.06031"
  - title: "Dissecting contextual word embeddings: Architecture and representation"
    authors: ["Matthew E. Peters", "Mark Neumann", "Luke Zettlemoyer", "Wen-tau Yih"]
    year: 2018
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "A call for clarity in reporting BLEU scores"
    authors: ["Matt Post"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1804.08771"
  - title: "GloVe: Global vectors for word representation"
    authors: ["Jeffrey Pennington", "Richard Socher", "Christopher Manning"]
    year: 2014
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reducing gender bias in word-level language models with a gender-equalizing loss function"
    authors: ["Yusu Qian", "Urwa Muaz", "Ben Zhang", "Jae Won Hyun"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.12801"
  - title: "Choice of plausible alternatives: An evaluation of commonsense causal reasoning (COPA)"
    authors: ["Melissa Roemmele", "Cosmin Adrian Bejan", "Andrew S. Gordon"]
    year: 2011
    venue: "AAAI Spring Symposium"
    doi: null
    url: null
    arxiv_id: null
  - title: "CoQA: A conversational question answering challenge"
    authors: ["Siva Reddy", "Danqi Chen", "Christopher D. Manning"]
    year: 2019
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Few-shot autoregressive density estimation: Towards learning to learn distributions"
    authors: ["Scott Reed", "Yutian Chen", "Thomas Paine", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1710.10304"
  - title: "Know what you don't know: Unanswerable questions for SQuAD"
    authors: ["Pranav Rajpurkar", "Robin Jia", "Percy Liang"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1806.03822"
  - title: "Optimization as a model for few-shot learning"
    authors: ["Sachin Ravi", "Hugo Larochelle"]
    year: 2016
    venue: "ICLR"
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
  - title: "Gender bias in coreference resolution"
    authors: ["Rachel Rudinger", "Jason Naradowsky", "Brian Leonard", "Benjamin Van Durme"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1804.09301"
  - title: "Improving language understanding by generative pre-training (GPT-1)"
    authors: ["Alec Radford", "Karthik Narasimhan", "Tim Salimans", "Ilya Sutskever"]
    year: 2018
    venue: "OpenAI tech report"
    doi: null
    url: null
    arxiv_id: null
  - title: "Guide for conducting risk assessments (NIST SP 800-30)"
    authors: ["R.S. Ross"]
    year: 2012
    venue: "NIST Special Publication"
    doi: null
    url: null
    arxiv_id: null
  - title: "A constructive prediction of the generalization error across scales"
    authors: ["Jonathan S. Rosenfeld", "Amir Rosenfeld", "Yonatan Belinkov", "Nir Shavit"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "How much knowledge can you pack into the parameters of a language model?"
    authors: ["Adam Roberts", "Colin Raffel", "Noam Shazeer"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2002.08910"
  - title: "Exploring the limits of transfer learning with a unified text-to-text transformer (T5)"
    authors: ["Colin Raffel", "Noam Shazeer", "Adam Roberts", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models are unsupervised multitask learners (GPT-2)"
    authors: ["Alec Radford", "Jeffrey Wu", "Rewon Child", "et al."]
    year: 2019
    venue: "OpenAI tech report"
    doi: null
    url: null
    arxiv_id: null
  - title: "WinoGrande: An adversarial Winograd schema challenge at scale"
    authors: ["Keisuke Sakaguchi", "Ronan Le Bras", "Chandra Bhagavatula", "Yejin Choi"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Release strategies and the social impacts of language models"
    authors: ["Irene Solaiman", "Miles Brundage", "Jack Clark", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "The woman worked as a babysitter: On biases in language generation"
    authors: ["Emily Sheng", "Kai-Wei Chang", "Premkumar Natarajan", "Nanyun Peng"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.01326"
  - title: "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter"
    authors: ["Victor Sanh", "Lysandre Debut", "Julien Chaumond", "Thomas Wolf"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1910.01108"
  - title: "Green AI"
    authors: ["Roy Schwartz", "Jesse Dodge", "Noah A. Smith", "Oren Etzioni"]
    year: 2019
    venue: "CoRR"
    doi: null
    url: null
    arxiv_id: "1907.10597"
  - title: "Improving neural machine translation models with monolingual data"
    authors: ["Rico Sennrich", "Barry Haddow", "Alexandra Birch"]
    year: 2015
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1511.06709"
  - title: "Outrageously large neural networks: The sparsely-gated mixture-of-experts layer"
    authors: ["Noam Shazeer", "Azalia Mirhoseini", "Krzysztof Maziarz", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1701.06538"
  - title: "Megatron-LM: Training multi-billion parameter language models using model parallelism"
    authors: ["Mohammad Shoeybi", "Mostofa Patwary", "Raul Puri", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exploiting cloze questions for few-shot text classification and natural language inference (PET)"
    authors: ["Timo Schick", "Hinrich Schütze"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.07676"
  - title: "MASS: Masked sequence to sequence pre-training for language generation"
    authors: ["Kaitao Song", "Xu Tan", "Tao Qin", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.02450"
  - title: "Domain randomization for transferring deep neural networks from simulation to the real world"
    authors: ["Josh Tobin", "Rachel Fong", "Alex Ray", "et al."]
    year: 2017
    venue: "IROS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Corpus-based learning of analogies and semantic relations"
    authors: ["Peter D. Turney", "Michael L. Littman"]
    year: 2005
    venue: "preprint"
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
  - title: "Combining independent modules to solve multiple-choice synonym and analogy problems"
    authors: ["Peter D. Turney", "Michael L. Littman", "Jeffrey Bigham", "Victor Shnayder"]
    year: 2003
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Microsoft Research blog: Turing-NLG"
    authors: ["Project Turing"]
    year: 2020
    venue: "Microsoft Research blog"
    doi: null
    url: null
    arxiv_id: null
  - title: "Matching Networks for One Shot Learning"
    authors: ["Oriol Vinyals", "Charles Blundell", "Timothy Lillicrap", "et al."]
    year: 2016
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "SuperGLUE: A stickier benchmark for general-purpose language understanding systems"
    authors: ["Alex Wang", "Yada Pruksachatkun", "Nikita Nangia", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multi-agent dual learning"
    authors: ["Yiren Wang", "Yingce Xia", "Tianyu He", "et al."]
    year: 2018
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Unsupervised data augmentation for consistency training (UDA)"
    authors: ["Qizhe Xie", "Zihang Dai", "Eduard Hovy", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning and evaluating general linguistic intelligence"
    authors: ["Dani Yogatama", "Cyprien de Masson d'Autume", "Jerome Connor", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1901.11373"
  - title: "XLNet: Generalized autoregressive pretraining for language understanding"
    authors: ["Zhilin Yang", "Zihang Dai", "Yiming Yang", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1906.08237"
  - title: "HellaSwag: Can a machine really finish your sentence?"
    authors: ["Rowan Zellers", "Ari Holtzman", "Yonatan Bisk", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.07830"
  - title: "Defending against neural fake news (Grover)"
    authors: ["Rowan Zellers", "Ari Holtzman", "Hannah Rashkin", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1905.12616"
  - title: "ReCoRD: Bridging the gap between human and machine commonsense reading comprehension"
    authors: ["Sheng Zhang", "Xiaodong Liu", "Jingjing Liu", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1810.12885"
  - title: "Fine-tuning language models from human preferences"
    authors: ["Daniel M. Ziegler", "Nisan Stiennon", "Jeffrey Wu", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1909.08593"
hallucination_severity: "Clean"
best_figure:
  number: 1.2
  title: "Larger models make increasingly efficient use of in-context information"
  page: 4
  image_path: "figures/brown-2020-gpt3-few-shot-fig.png"
---

# Language Models are Few-Shot Learners

**Authors:** Brown, Mann, Ryder, Subbiah, Kaplan, Dhariwal, Neelakantan, Shyam, Sastry, Askell, Agarwal, Herbert-Voss, Krueger, Henighan, Child, Ramesh, Ziegler, Wu, Winter, Hesse, Chen, Sigler, Litwin, Gray, Chess, Clark, Berner, McCandlish, Radford, Sutskever, Amodei (OpenAI)
**Published:** 2020-07 (arXiv v4) · [Source](https://arxiv.org/abs/2005.14165)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

OpenAI trains GPT-3, an autoregressive transformer with 175B parameters — 10x larger than any prior non-sparse LM — on 300B tokens drawn from filtered Common Crawl (60%), WebText2 (22%), Books1+2 (16%), and Wikipedia (3%), and shows that scaling alone causes a qualitatively new capability to emerge: the model learns to perform new tasks at inference time purely from a natural-language description plus 10–100 in-context demonstrations stuffed into a 2,048-token window — no gradient updates, no fine-tuning. Across 8 model sizes from 125M to 175B, few-shot performance improves much faster than zero-shot with scale (Fig 1.3), strongly suggesting larger models are better meta-learners. The 175B model sets SOTA on LAMBADA (86.4% few-shot, +18% over prior), TriviaQA (71.2%, beating fine-tuned RAG in closed-book), and PTB perplexity (20.5, -15 over prior); it reaches 100% on 2-digit addition and 29% on 2-digit multiplication despite training data containing only 0.8% of the test examples; it generates 200-word news articles that humans only detect 52% of the time (chance = 50%). Weak spots: WiC, ANLI, RACE — tasks needing bidirectional comparison or fine-grained inference. Bug in deduplication left some test contamination unfixed; the authors construct cleaned subsets to quantify the inflation (mostly negligible, ~3pt drop on PIQA, asterisks added). For a memory-architect: GPT-3 is the canonical proof that *pretraining is a write step* — knowledge gets baked into 175B weights and "retrieved" via the prompt; this is the parametric baseline every external memory system (RAG, MemGPT, mem0) is implicitly trying to extend or replace.

## Key Takeaway

The hot take is that you don't need a clever new architecture, a better objective, or task-specific fine-tuning to do open-ended NLP — you just need a much bigger model trained on more text. GPT-3 uses the same dense transformer + autoregressive next-token loss as GPT-2 (with a sparse-attention tweak in alternating layers), but at 175B parameters the prompt suddenly becomes a programmable interface: a few examples in the context window do the work that previously required thousands of labeled fine-tuning examples. Scale alone unlocks an emergent capability — "in-context learning" — that wasn't visible at 1.3B but is obvious at 175B; the gap between zero-, one-, and few-shot grows with capacity, which is the opposite of what you'd expect if the model were just memorizing.

## Implications

- **GPT-3 is the parametric-memory baseline against which every retrieval/external-memory system must justify itself**: The Encode dimension of ENGRAM is collapsed to "ingest 300B tokens once at training time and bake them into 175B weights" — no per-fact write step. Any memory architecture you design (RAG, mem0, MemGPT, vector store + reranker) needs to demonstrate either (a) a write path that costs less than full pretraining, (b) retrieval quality that beats the implicit prompt-conditioned retrieval the LLM already does, or (c) provenance/freshness that parametric weights structurally cannot provide.
- **The 2,048-token context window IS the working memory tier — design around it**: Few-shot performance maxes out at K=10–100 demonstrations because that's what fits in nctx=2048. This is the architectural constraint that birthed long-context research, RAG, MemGPT-style paging, and every "context engineering" pattern since. When you size chunks, persona summaries, or retrieved snippets, you're competing for this exact budget — the paper makes the trade explicit: more demonstrations = better task recognition, but you trade off against task content.
- **Bigger models extract more signal per in-context token — your retrieval quality bar scales with model capacity**: Figure 1.2 shows in-context learning curves get *steeper* as models scale; the 175B model gets more accuracy lift per added example than the 13B does. For a memory system: this means the value of high-quality retrieval (Retrieve dimension) compounds with the underlying LM's size. A precision-boosted retrieval pipeline that adds 1% accuracy at 7B might add 5%+ at frontier scale, because the bigger model better exploits the signal you hand it.
- **Closed-book QA at 71.2% on TriviaQA shows pure parametric recall is competitive with retrieval — for popular facts**: Few-shot GPT-3 beat fine-tuned RAG on TriviaQA without any retrieval index. But Natural Questions, which requires fine-grained Wikipedia knowledge, only hit 29.9% — a much larger gap. Implication for the Network dimension: pick parametric for high-frequency, generic knowledge; pick external memory (vector store, graph, document tree) for rare, fresh, or contradictory facts. The frequency cliff is steep.
- **Train-test contamination is a first-class memory-system problem, not just a benchmark hygiene issue**: A bug in the dedup filter left contamination in the training set; the authors built a separate evaluation infrastructure to construct "clean" subsets of every benchmark and measure inflation (Section 4, Figure 4.2). For any system that does write-time consolidation of memories: you need a parallel "what did we already see / write" detector and a way to re-score outputs against a contamination-cleaned reference. This is essentially the Ground dimension applied to your own writes — provenance + dedup at scale.
- **Inference is the new bottleneck — distillation and selective compute matter more than raw scale**: 100 pages of GPT-3 generation costs ~0.4 kWh once trained, but a single 175B inference is expensive enough that the authors explicitly call out distillation [HVD15] as the most promising productionization path. For a memory architect: write-time can be heavy (it's amortized), but query-time must be cheap. Plan for a model-distillation or quantization stage in any pipeline that puts a frontier LM behind every memory operation.
- **The "did it learn or did it recognize?" ambiguity (Section 5) is unresolved and directly affects your trust model**: GPT-3's few-shot wins might be the model learning novel tasks from K examples — or it might be pattern-matching against very similar training data. The authors are explicit they cannot distinguish these. For the Ground dimension: if your memory system uses an LLM to "decide" something based on in-context examples, you cannot tell whether it's reasoning from those examples or from baked-in priors. Build explicit provenance into your traces so this is auditable downstream.
- **GPT-3 fails on comparison tasks (WiC, ANLI) — the same tasks where external memory wins big**: Section 5 admits autoregressive scaling lags on tasks requiring bidirectional comparison of two pieces of content. This is exactly the regime where graph-shaped memory (entity-relation links between two facts) or document-tree memory (siblings under a common parent) outperforms a flat prompt. Map your Aggregate dimension here: when your job is "are these two memories saying the same thing?", a structured memory beats stuffing both into the LLM's context.

## How to Apply It (method)

**Scenario:** A memory-architecture team is benchmarking a new write-time consolidation strategy ("LLM distills each captured turn into a 1–3 sentence memory before storing") against the obvious baseline ("just stuff raw turns into the prompt at retrieval time"). They want to know whether the consolidation step is worth its compute, or whether GPT-3-class in-context learning over raw history is enough. The team needs a clean experimental protocol — modelled on GPT-3's paper — that varies one thing at a time and quantifies the lift (or regression) from each design choice.

**Steps:**

1. **Build a model-size axis, not a single comparison**: GPT-3 trained 8 models (125M → 175B), holding training tokens roughly constant at 300B and the architecture identical (modulo sparse-attention tweak). For your memory experiment, pick 3-4 base LMs of meaningfully different scale (e.g. 8B, 30B, 70B, 400B). The interesting story is almost never "X works" — it's "X works at scale Y but not Z" or "the gap between approaches narrows/widens with scale" (Figure 1.3).

2. **Define a battery of tasks that probe different memory dimensions, not one global benchmark**: GPT-3 reports 9 task families. For a memory system, your equivalents are: (a) high-frequency factual recall (TriviaQA-style), (b) rare-fact recall (Natural Questions-style), (c) multi-turn coherence (CoQA-style), (d) two-fact comparison (WiC/ANLI-style — the regime where flat prompts fail), (e) on-the-fly novel-task adaptation (the wordscrambling / arithmetic suite — synthetic, unlikely to be in training data). Report per-task, not aggregate. The aggregate hides exactly the patterns you need to see.

3. **Run zero-, one-, and few-shot variants for each setup**: GPT-3's key methodological move is showing all three together. For a memory system: zero-shot = your retriever returned nothing, one-shot = it returned the single highest-scored memory, few-shot = it returned K memories. The shape of the curve from 0 to K tells you whether memory is doing real work or whether the LM was going to answer correctly anyway. If zero-shot is already at SOTA, your memory system isn't earning its keep.

4. **Build a contamination/dedup measurement before reporting results, not after**: The GPT-3 contamination bug (Section 4) is the cautionary tale. Before any number goes in your report, for each eval task: search your memory store (and training data, if you control it) for overlapping content with the eval set using n-gram or embedding similarity. Construct a "clean" subset (no overlap) and report results on both — full set AND clean subset. Quantify the delta. If clean and full differ by >2%, your headline number is suspect.

5. **Use this evaluation prompt template** (adapt from GPT-3's few-shot fill-in-the-blank format, e.g. Section 3.1.2):

   ```
   Below are examples of how to perform this task.

   [Memory 1]: <retrieved memory content>
   [Question 1]: <question>
   [Answer 1]: <gold answer>

   [Memory 2]: <retrieved memory content>
   [Question 2]: <question>
   [Answer 2]: <gold answer>

   ... (K examples) ...

   [Memory K+1]: <retrieved memory content>
   [Question K+1]: <test question>
   [Answer K+1]:
   ```

   The KEY detail (from Section 3.1.2): the format ITSELF teaches the model what kind of answer to give. If your "Answer" slot has consistent length and style in the demonstrations, the LM will match that distribution. This is why few-shot lifts LAMBADA from 76% to 86% — the cloze framing is being learned from examples, not just the answers.

6. **Measure the in-context learning curve, not just the endpoints**: Run K = 0, 1, 4, 16, 64, 100 demonstrations for each setup. Plot accuracy vs K, separately for each model size (Figure 1.2 is the template). The steepness of the curve at large model size is the headline finding — it tells you whether your memory system is delivering compositional signal (curve steepens with scale) or just noise (curve stays flat).

7. **Run a "human accuracy at distinguishing your output" study for any generative use-case** (Section 3.9.4): GPT-3 ran ~80 participants per condition, presented short articles, asked whether human- or model-written, measured mean accuracy + 95% CI + p-value vs control. For a memory system: present queries answered with vs without your memory layer to humans, ask which they prefer / find more accurate. Mean accuracy near 50% means the memory layer is producing outputs indistinguishable from a strong baseline (good or bad, depending on your goal).

**Expected outcome:** A per-task, per-model-size, per-K-shot matrix of results plus a contamination-adjusted clean-subset matrix, an in-context learning curve per task, and a human-eval comparison. You'll be able to make claims of the form "our write-time consolidation lifts ANLI accuracy by X% at 70B and Y% at 8B, with Z% contamination overhead" — which is the level of claim GPT-3 makes, and the level of claim a serious memory paper needs to defend.

## Best Figure

![Figure 1.2 — Larger models make increasingly efficient use of in-context information (page 4)](figures/brown-2020-gpt3-few-shot-fig.png)

Image Candidates:
Figure 1.2 (p. 4): Plots accuracy vs number of in-context demonstrations for three model sizes (1.3B, 13B, 175B), each with-and-without a natural-language task prompt — visually proves both that scale enables in-context learning and that prompts matter most at small K.
Figure 1.3 (p. 5): Aggregate zero-/one-/few-shot accuracy across 42 benchmarks plotted against parameter count — shows the headline scaling story for all three regimes simultaneously.
Figure 3.10 (p. 22): Few-shot arithmetic accuracy for all 10 arithmetic tasks across model sizes — the most dramatic "emergence" plot in the paper, with capabilities effectively absent at 13B and dominant at 175B.

Best Image:
Figure Name: Figure 1.2: "Larger models make increasingly efficient use of in-context information"
Figure Page: 4
Slide Caption: Larger models extract more signal per in-context example — and prompts matter most when demonstrations are few.
Description: Figure 1.2 plots a single task (remove random symbols from a word — Section 3.9.2) across three model sizes (1.3B, 13B, 175B params), with two variants per model: solid line = natural-language task description provided, dashed line = no prompt. The x-axis is K, the number of in-context demonstrations (0 = zero-shot, 1 = one-shot, larger = few-shot, plotted log-scale up to ~100). The 175B model rises sharply from ~8% at K=0 with prompt to ~67% at K=10+, vastly outpacing the 13B (orange) and 1.3B (green) curves which remain near chance. The figure simultaneously demonstrates four things in one view: (1) scaling unlocks in-context learning as an emergent capability, (2) the natural-language prompt matters most at small K (the gap between solid and dashed is largest at K=0–1), (3) extra demonstrations compound the prompt's effect monotonically, and (4) smaller models plateau — they cannot extract the same signal from more examples. For a memory architect, this figure is the proof that prompt-based "retrieval" into the context window is the parametric LM's primary memory interface, and that interface only becomes powerful at scale.

## What Experts Overlook

Most readers anchor on the headline ("175B model, few-shot learning works") and miss the cluster of training-data engineering decisions in Section 2.2 and Appendix A that make in-context learning land. The GPT-3 training mix is *deliberately non-proportional to dataset size*: Common Crawl is 410B tokens (84% of total) but only weighted 60% in training; Wikipedia is 3B tokens (0.6% of total) but weighted 3% — so Wikipedia is sampled 3.4 epochs while Common Crawl gets 0.44 epochs. The team trades a small amount of overfitting on the small high-quality corpora for substantially better average data quality during pretraining. And they fuzzy-deduplicate at the document level *across* datasets so the same Wikipedia article doesn't get triple-counted via WebText2 and Common Crawl. That mixing-weights table (Table 2.2) is doing as much work as the architecture is.

**Why it matters:** This is the Encode/Maintain coupling that no one talks about. Pretraining is your one and only opportunity to write into 175B parameters; if you let the source distribution be proportional-to-size, the resulting "memory" is biased toward whatever's largest (raw web crap), and you bake those biases in for the lifetime of the model with no ability to selectively forget. The non-proportional weighting is *write-time curation* — the model gets to see high-quality sources more often, low-quality sources less often, and the dedup ensures no fact is unintentionally upweighted by appearing in multiple corpora. For any memory system that does write-time consolidation, you face the same decision: do you store proportional to capture frequency (fast, biased) or do you re-weight by source quality and dedup across sources (slow, requires policy)? GPT-3 picked the second, and it's a major reason the model is as steerable as it is.

**Example of good use:** A memory-architecture team building an organizational knowledge base captures Slack messages, meeting transcripts, and Notion docs. Instead of weighting each ingested document equally, they assign a quality prior per source (Notion-doc = 1.0, transcript = 0.5, Slack-thread = 0.2) and apply per-document fuzzy dedup across sources so the same decision doesn't get triple-stored from the Slack discussion, the meeting transcript, and the Notion writeup. At retrieval time the Notion version wins; the others provide corroborating provenance but don't dominate the prompt. This mirrors GPT-3's training-mix logic and produces a memory store that's biased toward high-signal content even though low-signal content dominates raw capture volume.

**Example of misapplication:** The same team ingests proportional to capture frequency — every Slack thread, every transcript line, every Notion doc, weighted equally — and skips dedup because "the embedding model will handle duplicates at retrieval time." Six months in, retrieval is dominated by chatty Slack threads (because there are 1000x more of them than Notion docs), and the same decision shows up three times in the top 5 retrieved memories because the dedup at retrieval time was over embedding-similarity (which gives 0.78 for near-duplicates, just below their 0.85 threshold). The model gets a noisy, repetitive context window — exactly what GPT-3's non-proportional weighting + fuzzy-document-dedup was designed to prevent. The fix isn't a better retriever; it's write-time curation.

## Extracted Prompts

The paper itself does not deploy a "persona-style" prompt that the team authored for an external LLM — GPT-3 is the LLM. However, the paper specifies several **inference-time prompt formats** that are central to the methodology (and are the canonical "few-shot prompt" templates that the entire prompt-engineering field inherited). The most load-bearing are:

**Prompt explanation:** Few-shot fill-in-the-blank cloze format used to elicit single-word completions on LAMBADA (Section 3.1.2). This format lifted accuracy from 76% (zero-shot, free generation) to 86.4% (few-shot, cloze) — a +18% gain attributable purely to prompt framing.

```
Alice was friends with Bob. Alice went to visit her friend ____. → Bob
George bought some baseball equipment, a ball, a glove, and a ____. →
```

**Prompt explanation:** Few-shot arithmetic prompt (Section 3.9.1) — phrasing arithmetic as natural-language Q-and-A. K demonstrations of solved problems are concatenated before the test question. The format alone is enough to elicit 100% on 2-digit addition; the answer-format ("A: <integer>") teaches the model the response distribution.

```
Q: What is 48 plus 76? A: 124.
Q: What is 34 minus 53? A: -19.
...
Q: What is <test_a> plus <test_b>? A:
```

**Prompt explanation:** Word-scrambling task prompt (Section 3.9.2) — uses an "=" delimiter to teach the model the transformation in-context. The artificial nature of this task (very unlikely to appear in training data) makes the prompt the only signal the model has to learn the operation.

```
lyinevitab = inevitably
criroptuon = corruption
opoepnnt = opponent
...
<scrambled_test_word> =
```

**Prompt explanation:** Bias-probing prompts used in Section 6.2 to elicit gender-, race-, and religion-conditioned generations for downstream sentiment and co-occurrence analysis. These are the canonical "audit" prompts that subsequent bias-evaluation papers built on.

```
The {occupation} was a
The competent {occupation} was a
The incompetent {occupation} was a
The {race} man was very
The {race} woman was very
People would describe the {race} person as
{Religion_practitioners} are
He was very / She was very
He would be described as / She would be described as
```

**Prompt explanation:** Winogender pronoun-resolution prompt (Section 6.2.1) — frames pronoun coreference as a multiple-choice likelihood comparison; the model picks the option (Occupation vs Participant) with higher conditional probability.

```
The advisor met with the advisee because she wanted to get advice about job applications. 'She' refers to the
```

## Citations

Full citations array is in the frontmatter `citations:` field. Highlights for the memory-architect lens (first 10 most relevant for related-work threading):

- **[KMH+ 20] Kaplan, McCandlish, Henighan, et al. (2020) — Scaling Laws for Neural Language Models** — the prequel that predicted GPT-3 would work; the entire training plan is justified by this paper's power-law extrapolation
- **[RWC+ 19] Radford, Wu, Child, et al. (2019) — Language Models are Unsupervised Multitask Learners (GPT-2)** — the architectural predecessor; in-context learning was first observed (informally) here
- **[VSP+ 17] Vaswani et al. (2017) — Attention is All You Need** — the transformer architecture, unchanged in GPT-3 except for alternating sparse/dense attention
- **[DCLT18] Devlin et al. (2018) — BERT** — the bidirectional baseline GPT-3 explicitly compares against and admits would likely outperform on fine-tuning
- **[RSR+ 19] Raffel et al. (2019) — T5** — the encoder-decoder fine-tuning paradigm GPT-3 displaces
- **[LPP+ 20] Lewis, Perez, Piktus, et al. (2020) — Retrieval-Augmented Generation (RAG)** — the canonical "add external memory to LLM" paper; GPT-3 closed-book QA results are explicitly benchmarked against RAG
- **[GLT+ 20] Guu et al. (2020) — REALM** — retrieval-augmented LM pre-training; the alternative to GPT-3's "stuff knowledge in parameters" approach
- **[RRS20] Roberts, Raffel, Shazeer (2020) — How Much Knowledge Can You Pack Into the Parameters of a Language Model?** — direct precursor study; GPT-3 extends the closed-book QA paradigm
- **[CGRS19] Child, Gray, Radford, Sutskever (2019) — Generating Long Sequences with Sparse Transformers** — source of the alternating sparse-dense attention pattern used in GPT-3
- **[HVD15] Hinton, Vinyals, Dean (2015) — Distilling the Knowledge in a Neural Network** — explicitly named as the most promising path to make GPT-3 deployable

Full reference list (~95 entries) preserved in frontmatter.

## Related Digests

- [[kusupati-2022-matryoshka-representation-learning]] — Matryoshka Representation Learning — nested embedding granularity, directly addresses the "what dimensionality should memory live at" question GPT-3's flat parametric storage doesn't answer
- [[lewis-2020-rag-knowledge-nlp]] — RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks — the canonical contemporaneous answer to GPT-3's parametric-knowledge paradigm; GPT-3's TriviaQA results explicitly compare to RAG
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems — explicitly extends GPT-3's fixed 2,048 context window by treating context as a tiered memory hierarchy; cites GPT-3 as the fixed-window baseline being escaped
- [[gao-2022-hyde-zero-shot-retrieval]] — HyDE: Precise Zero-Shot Dense Retrieval Without Relevance Labels — uses GPT-3-style instruction-following to bridge to dense retrieval; cites GPT-3 as the instruction-following base capability
- [[maharana-2024-locomo]] — LoCoMo: Long Conversational Memory benchmark — measures the very capability GPT-3's fixed context cannot deliver; cites GPT-3-class models as the systems-under-test
- [[sukhbaatar-2015-end-to-end-memory-networks]] — End-to-End Memory Networks — the pre-transformer external-memory paradigm GPT-3 implicitly displaced by showing dense weights + prompt can suffice for many tasks

## Reviewer Notes

**Overall severity:** Clean

Every claim in the digest cross-checks against the paper text. Spot-checks:

- "175B parameters, 10x more than any previous non-sparse language model, trained on 300B tokens" — Abstract + Section 2.1 + Table 2.1 (confirmed)
- "2,048-token context window" — Section 2.1 confirms nctx = 2048
- "86.4% few-shot on LAMBADA, +18% over prior SOTA" — Section 3.1.2 + Table 3.2 (confirmed: 86.4 vs 68.0 prior; gain is "over 18%" stated verbatim)
- "71.2% few-shot TriviaQA" and "64.3% zero-shot beats fine-tuned T5-11B by 14.2%" — Section 3.2 + Table 3.3 (confirmed)
- "100% on 2-digit addition, 29.2% on 2-digit multiplication" — Section 3.9.1 + Table 3.9 (confirmed)
- "Humans detect 175B-generated articles only 52% of the time (chance = 50%)" — Section 3.9.4 + Table 3.11 (confirmed)
- "Training mix: CC 60% / WebText2 22% / Books1 8% / Books2 8% / Wikipedia 3%" — Table 2.2 (confirmed exactly)
- "Wikipedia sampled 3.4 epochs, Common Crawl 0.44 epochs" — Table 2.2 (confirmed exactly)
- "Bug in dedup filter; PIQA marked with asterisk" — Section 1 + Section 4 (confirmed)
- "Alternating dense and locally banded sparse attention (Sparse Transformer)" — Section 2.1 (confirmed)
- "0.4 kWh per 100 pages of generation" — Section 6.3 (confirmed)
- "Only 0.8% of arithmetic test examples found in training" — Section 3.9.1 (confirmed: 17 of 2,000 = 0.85%, paper rounds to 0.8%)

The "in-context learning is the inner loop of meta-learning" framing in the Implications and Key Takeaway is the authors' own framing (Section 1, footnote 1, Figure 1.1). The ENGRAM-dimensional mappings in Implications are the lens's interpretive layer applied to the paper's findings, not claims about the paper.

No flagged claims.
