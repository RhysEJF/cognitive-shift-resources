---
corpus: agentic-memory
kind: paper-digest
slug: touvron-2023-llama-2
title: "Llama 2: Open Foundation and Fine-Tuned Chat Models"
authors:
  - "Touvron, Hugo"
  - "Martin, Louis"
  - "Stone, Kevin"
  - "Albert, Peter"
  - "Almahairi, Amjad"
  - "Babaei, Yasmine"
  - "Bashlykov, Nikolay"
  - "Batra, Soumya"
  - "Bhargava, Prajjwal"
  - "Bhosale, Shruti"
  - "Bikel, Dan"
  - "Blecher, Lukas"
  - "Canton Ferrer, Cristian"
  - "Chen, Moya"
  - "Cucurull, Guillem"
  - "Esiobu, David"
  - "Fernandes, Jude"
  - "Fu, Jeremy"
  - "Fu, Wenyin"
  - "Fuller, Brian"
  - "Gao, Cynthia"
  - "Goswami, Vedanuj"
  - "Goyal, Naman"
  - "Hartshorn, Anthony"
  - "Hosseini, Saghar"
  - "Hou, Rui"
  - "Inan, Hakan"
  - "Kardas, Marcin"
  - "Kerkez, Viktor"
  - "Khabsa, Madian"
  - "Kloumann, Isabel"
  - "Korenev, Artem"
  - "Koura, Punit Singh"
  - "Lachaux, Marie-Anne"
  - "Lavril, Thibaut"
  - "Lee, Jenya"
  - "Liskovich, Diana"
  - "Lu, Yinghai"
  - "Mao, Yuning"
  - "Martinet, Xavier"
  - "Mihaylov, Todor"
  - "Mishra, Pushkar"
  - "Molybog, Igor"
  - "Nie, Yixin"
  - "Poulton, Andrew"
  - "Reizenstein, Jeremy"
  - "Rungta, Rashi"
  - "Saladi, Kalyan"
  - "Schelten, Alan"
  - "Silva, Ruan"
  - "Smith, Eric Michael"
  - "Subramanian, Ranjan"
  - "Tan, Xiaoqing Ellen"
  - "Tang, Binh"
  - "Taylor, Ross"
  - "Williams, Adina"
  - "Kuan, Jian Xiang"
  - "Xu, Puxin"
  - "Yan, Zheng"
  - "Zarov, Iliyan"
  - "Zhang, Yuchen"
  - "Fan, Angela"
  - "Kambadur, Melanie"
  - "Narang, Sharan"
  - "Rodriguez, Aurelien"
  - "Stojnic, Robert"
  - "Edunov, Sergey"
  - "Scialom, Thomas"
year: 2023
publication_date: "2023-07"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2307.09288"
doi: null
arxiv_id: "2307.09288"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Llama 2 is a family of openly released 7B-70B foundation and chat models from Meta that closes most of the gap to closed-source commercial chat models — Llama 2-Chat 70B reaches a 36% win rate and 31.5% tie rate against ChatGPT (gpt-3.5-turbo-0301) on ~4,000 human-rated helpfulness prompts and ties or beats ChatGPT on safety violation rate — and the paper is unusual because it documents the full recipe: 2T-token pretraining with grouped-query attention, ~27.5k SFT examples, ~1.4M Meta-collected human preference comparisons, five iterative RLHF rounds combining Rejection Sampling and PPO, two separate reward models for helpfulness and safety, and a novel Ghost Attention trick that keeps system prompts honoured across 20+ turns."
topics:
  - large-language-models
  - rlhf
  - llm-alignment
  - instruction-tuning
  - llm-safety
  - open-source-llms
  - reward-modeling
  - red-teaming
tags:
  - paper
  - llama
  - meta
  - foundation-models
  - chat-models
  - alignment
  - ppo
  - rejection-sampling
  - ghost-attention
entities:
  - touvron-hugo
  - scialom-thomas
  - martin-louis
  - meta-ai
related_digests:
  - touvron-2023-llama-foundation-models
  - brown-2020-gpt3-few-shot
  - radford-2019-gpt2-multitask
  - radford-2018-gpt1
  - vaswani-2017-attention-is-all-you-need
  - bi-2020-palm-context-generation
citations:
  - title: "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
    authors: ["Joshua Ainslie", "James Lee-Thorp", "Michiel de Jong", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Falcon-40B: an open large language model with state-of-the-art performance"
    authors: ["Ebtesam Almazrouei", "Hamza Alobeidli", "Abdulaziz Alshamsi", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "PaLM 2 Technical Report"
    authors: ["Rohan Anil", "Andrew M. Dai", "Orhan Firat", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "A general language assistant as a laboratory for alignment"
    authors: ["Amanda Askell", "Yuntao Bai", "Anna Chen", "et al."]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2112.00861"
  - title: "Program synthesis with large language models (MBPP)"
    authors: ["Jacob Austin", "Augustus Odena", "Maxwell Nye", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training a helpful and harmless assistant with reinforcement learning from human feedback"
    authors: ["Yuntao Bai", "Andy Jones", "Kamal Ndousse", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2204.05862"
  - title: "Constitutional AI: Harmlessness from AI feedback"
    authors: ["Yuntao Bai", "Saurav Kadavath", "Sandipan Kundu", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2212.08073"
  - title: "Based on billions of words on the internet, people = men"
    authors: ["April H. Bailey", "Adina Williams", "Andrei Cimpian"]
    year: 2022
    venue: "Science Advances"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the dangers of stochastic parrots: Can language models be too big?"
    authors: ["Emily M. Bender", "Timnit Gebru", "Angelina McMillan-Major", "Shmargaret Shmitchell"]
    year: 2021
    venue: "FAccT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Guiding the release of safer e2e conversational AI through value sensitive design"
    authors: ["A. Stevie Bergman", "Gavin Abercrombie", "Shannon L. Spruit", "et al."]
    year: 2022
    venue: "SIGDIAL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Re-contextualizing fairness in NLP: The case of India"
    authors: ["Shaily Bhatt", "Sunipa Dev", "Partha Talukdar", "et al."]
    year: 2022
    venue: "preprint"
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
  - title: "Stereotyping Norwegian salmon: An inventory of pitfalls in fairness benchmark datasets"
    authors: ["Su Lin Blodgett", "Gilsinia Lopez", "Alexandra Olteanu", "et al."]
    year: 2021
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Enriching word vectors with subword information (fastText)"
    authors: ["Piotr Bojanowski", "Edouard Grave", "Armand Joulin", "Tomás Mikolov"]
    year: 2016
    venue: "CoRR"
    doi: null
    url: "http://arxiv.org/abs/1607.04606"
    arxiv_id: "1607.04606"
  - title: "Language Models are Few-Shot Learners (GPT-3)"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Evaluating Large Language Models Trained on Code (HumanEval)"
    authors: ["Mark Chen", "Jerry Tworek", "Heewoo Jun", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90%* ChatGPT Quality"
    authors: ["Wei-Lin Chiang", "Zhuohan Li", "Zi Lin", "et al."]
    year: 2023
    venue: "lmsys blog"
    doi: null
    url: "https://lmsys.org/blog/2023-03-30-vicuna/"
    arxiv_id: null
  - title: "QuAC: Question Answering in Context"
    authors: ["Eunsol Choi", "He He", "Mohit Iyyer", "et al."]
    year: 2018
    venue: "EMNLP"
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
  - title: "Deep reinforcement learning from human preferences"
    authors: ["Paul F. Christiano", "Jan Leike", "Tom Brown", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Scaling instruction-finetuned language models (FLAN)"
    authors: ["Hyung Won Chung", "Le Hou", "S. Longpre", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2210.11416"
  - title: "BoolQ: Exploring the surprising difficulty of natural yes/no questions"
    authors: ["Christopher Clark", "Kenton Lee", "Ming-Wei Chang", "et al."]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1905.10044"
  - title: "All that's 'human' is not gold: Evaluating human evaluation of generated text"
    authors: ["Elizabeth Clark", "Tal August", "Sofia Serrano", "et al."]
    year: 2021
    venue: "ACL"
    doi: "10.18653/v1/2021.acl-long.565"
    url: "https://aclanthology.org/2021.acl-long.565"
    arxiv_id: null
  - title: "Think you have solved question answering? Try ARC, the AI2 reasoning challenge"
    authors: ["Peter Clark", "Isaac Cowhey", "Oren Etzioni", "et al."]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1803.05457"
  - title: "Training verifiers to solve math word problems (GSM8K)"
    authors: ["Karl Cobbe", "Vineet Kosaraju", "Mohammad Bavarian", "et al."]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2110.14168"
  - title: "Recent advances towards safe, responsible, and moral dialogue systems: A survey"
    authors: ["Jiawen Deng", "Hao Sun", "Zhexin Zhang", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2302.09270"
  - title: "Residual energy-based models for text generation"
    authors: ["Yuntian Deng", "Anton Bakhtin", "Myle Ott", "et al."]
    year: 2019
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "BOLD: Dataset and metrics for measuring biases in open-ended language generation"
    authors: ["Jwala Dhamala", "Tony Sun", "Varun Kumar", "et al."]
    year: 2021
    venue: "FAccT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Anticipating safety issues in e2e conversational AI: Framework and tooling"
    authors: ["Emily Dinan", "Gavin Abercrombie", "A. Stevie Bergman", "et al."]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2107.03451"
  - title: "Documenting large webtext corpora: A case study on the colossal clean crawled corpus"
    authors: ["Jesse Dodge", "Maarten Sap", "Ana Marasović", "et al."]
    year: 2021
    venue: "EMNLP"
    doi: "10.18653/v1/2021.emnlp-main.98"
    url: "https://aclanthology.org/2021.emnlp-main.98"
    arxiv_id: null
  - title: "Measuring the carbon intensity of AI in cloud instances"
    authors: ["Jesse Dodge", "Taylor Prewitt", "Remi Tachet Des Combes", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2206.05229"
  - title: "GLaM: Efficient scaling of language models with mixture-of-experts"
    authors: ["Nan Du", "Yanping Huang", "Andrew M. Dai", "et al."]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Understanding dataset difficulty with V-usable information (SHP)"
    authors: ["Kawin Ethayarajh", "Yejin Choi", "Swabha Swayamdipta"]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the impact of machine learning randomness on group fairness"
    authors: ["Prakhar Ganesh", "Hongyan Chang", "Martin Strobel", "Reza Shokri"]
    year: 2023
    venue: "FAccT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Red teaming language models to reduce harms: Methods, scaling behaviors, and lessons learned"
    authors: ["Deep Ganguli", "Liane Lovitt", "Jackson Kernion", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2209.07858"
  - title: "The capacity for moral self-correction in large language models"
    authors: ["Deep Ganguli", "Amanda Askell", "Nicholas Schiefer", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2302.07459"
  - title: "A framework for few-shot language model evaluation"
    authors: ["Leo Gao", "Jonathan Tow", "Stella Biderman", "et al."]
    year: 2021
    venue: "Zenodo"
    doi: "10.5281/zenodo.5371628"
    url: null
    arxiv_id: null
  - title: "Repairing the cracked foundation: A survey of obstacles in evaluation practices for generated text"
    authors: ["Sebastian Gehrmann", "Elizabeth Clark", "Thibault Sellam"]
    year: 2023
    venue: "JAIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "ChatGPT outperforms crowd-workers for text-annotation tasks"
    authors: ["Fabrizio Gilardi", "Meysam Alizadeh", "Maël Kubli"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2303.15056"
  - title: "The false promise of imitating proprietary LLMs"
    authors: ["Arnav Gudibande", "Eric Wallace", "Charlie Snell", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2305.15717"
  - title: "ACT: Designing sustainable computer systems with an architectural carbon modeling tool"
    authors: ["Udit Gupta", "Mariam Elgamal", "Gage Hills", "et al."]
    year: 2022
    venue: "ISCA"
    doi: null
    url: null
    arxiv_id: null
  - title: "Chasing carbon: The elusive environmental footprint of computing"
    authors: ["Udit Gupta", "Young Guen Kim", "Sylvia Lee", "et al."]
    year: 2022
    venue: "IEEE Micro"
    doi: null
    url: null
    arxiv_id: null
  - title: "Handbook of inter-rater reliability"
    authors: ["Kilem L. Gwet"]
    year: 2014
    venue: "Advanced Analytics, LLC"
    doi: null
    url: null
    arxiv_id: null
  - title: "Computing inter-rater reliability and its variance in the presence of high agreement"
    authors: ["Kilem Li Gwet"]
    year: 2008
    venue: "British Journal of Mathematical and Statistical Psychology"
    doi: null
    url: null
    arxiv_id: null
  - title: "ToxiGen: A large-scale machine-generated dataset for adversarial and implicit hate speech detection"
    authors: ["Thomas Hartvigsen", "Saadia Gabriel", "Hamid Palangi", "et al."]
    year: 2022
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "synthetic-instruct-gptj-pairwise (dataset)"
    authors: ["Alex Havrilla"]
    year: null
    venue: "HuggingFace"
    doi: null
    url: "https://huggingface.co/datasets/Dahoas/synthetic-instruct-gptj-pairwise"
    arxiv_id: null
  - title: "DeBERTa: Decoding-enhanced BERT with disentangled attention"
    authors: ["Pengcheng He", "Xiaodong Liu", "Jianfeng Gao", "Weizhu Chen"]
    year: 2020
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2006.03654"
  - title: "Measuring Massive Multitask Language Understanding (MMLU)"
    authors: ["Dan Hendrycks", "Collin Burns", "Steven Basart", "et al."]
    year: 2020
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2009.03300"
  - title: "Measuring mathematical problem solving with the MATH dataset"
    authors: ["Dan Hendrycks", "Collin Burns", "Saurav Kadavath", "et al."]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2103.03874"
  - title: "Training compute-optimal large language models (Chinchilla)"
    authors: ["Jordan Hoffmann", "Sebastian Borgeaud", "Arthur Mensch", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2203.15556"
  - title: "The curious case of neural text degeneration"
    authors: ["Ari Holtzman", "Jan Buys", "Li Du", "Maxwell Forbes", "Yejin Choi"]
    year: 2020
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=rygGQyrFvH"
    arxiv_id: null
  - title: "Unnatural instructions: Tuning language models with (almost) no human labor"
    authors: ["Or Honovich", "Thomas Scialom", "Omer Levy", "Timo Schick"]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2212.09689"
  - title: "An empirical study of metrics to measure representational harms in pre-trained language models"
    authors: ["Saghar Hosseini", "Hamid Palangi", "Ahmed Hassan Awadallah"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2301.09211"
  - title: "Is ChatGPT better than human annotators? Potential and limitations of ChatGPT in explaining implicit hate speech"
    authors: ["Fan Huang", "Haewoon Kwak", "Jisun An"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2302.07736"
  - title: "VADER: A parsimonious rule-based model for sentiment analysis of social media text"
    authors: ["Clayton Hutto", "Eric Gilbert"]
    year: 2014
    venue: "ICWSM"
    doi: null
    url: null
    arxiv_id: null
  - title: "TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension"
    authors: ["Mandar Joshi", "Eunsol Choi", "Daniel S. Weld", "Luke Zettlemoyer"]
    year: 2017
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1705.03551"
  - title: "Scaling laws for neural language models"
    authors: ["Jared Kaplan", "Sam McCandlish", "Tom Henighan", "et al."]
    year: 2020
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2001.08361"
  - title: "Overcoming catastrophic forgetting in neural networks"
    authors: ["James Kirkpatrick", "Razvan Pascanu", "Neil Rabinowitz", "et al."]
    year: 2017
    venue: "PNAS"
    doi: null
    url: null
    arxiv_id: null
  - title: "OpenAssistant Conversations — Democratizing large language model alignment"
    authors: ["Andreas Köpf", "Yannic Kilcher", "Dimitri von Rütte", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2304.07327"
  - title: "Pretraining language models with human preferences"
    authors: ["Tomasz Korbak", "Kejian Shi", "Angelica Chen", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2302.08582"
  - title: "SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing"
    authors: ["Taku Kudo", "John Richardson"]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language generation models can cause harm: So what can we do about it? An actionable survey"
    authors: ["Sachin Kumar", "Vidhisha Balachandran", "Lucille Njoo", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2210.07700"
  - title: "Natural Questions: A benchmark for question answering research"
    authors: ["Tom Kwiatkowski", "Jennimaria Palomaki", "Olivia Redfield", "et al."]
    year: 2019
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "HuggingFace H4 Stack Exchange preference dataset"
    authors: ["Nathan Lambert", "Lewis Tunstall", "Nazneen Rajani", "Tristan Thrush"]
    year: 2023
    venue: "HuggingFace"
    doi: null
    url: "https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences"
    arxiv_id: null
  - title: "Deduplicating training data makes language models better"
    authors: ["Katherine Lee", "Daphne Ippolito", "Andrew Nystrom", "et al."]
    year: 2022
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Introducing the AI research supercluster — Meta's cutting-edge AI supercomputer for AI research"
    authors: ["Kevin Lee", "Shubho Sengupta"]
    year: 2022
    venue: "Meta AI blog"
    doi: null
    url: "https://ai.facebook.com/blog/ai-rsc/"
    arxiv_id: null
  - title: "TruthfulQA: Measuring how models mimic human falsehoods"
    authors: ["Stephanie Lin", "Jacob Hilton", "Owain Evans"]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2109.07958"
  - title: "RoBERTa: A robustly optimized BERT pretraining approach"
    authors: ["Yinhan Liu", "Myle Ott", "Naman Goyal", "et al."]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1907.11692"
  - title: "The FLAN collection: Designing data and methods for effective instruction tuning"
    authors: ["Shayne Longpre", "Le Hou", "Tu Vu", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2301.13688"
  - title: "Decoupled weight decay regularization (AdamW)"
    authors: ["Ilya Loshchilov", "Frank Hutter"]
    year: 2017
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1711.05101"
  - title: "Self-refine: Iterative refinement with self-feedback"
    authors: ["Aman Madaan", "Niket Tandon", "Prakhar Gupta", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2303.17651"
  - title: "Augmented language models: A survey"
    authors: ["Grégoire Mialon", "Roberto Dessì", "Maria Lomeli", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2302.07842"
  - title: "Can a suit of armor conduct electricity? A new dataset for open book question answering (OpenBookQA)"
    authors: ["Todor Mihaylov", "Peter Clark", "Tushar Khot", "Ashish Sabharwal"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1809.02789"
  - title: "Model cards for model reporting"
    authors: ["Margaret Mitchell", "Simone Wu", "Andrew Zaldivar", "et al."]
    year: 2018
    venue: "CoRR"
    doi: null
    url: "http://arxiv.org/abs/1810.03993"
    arxiv_id: "1810.03993"
  - title: "Introducing MPT-7B: A new standard for open-source, commercially usable LLMs"
    authors: ["MosaicML NLP Team", "et al."]
    year: 2023
    venue: "MosaicML blog"
    doi: null
    url: null
    arxiv_id: null
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    authors: ["Reiichiro Nakano", "Jacob Hilton", "Suchir Balaji", "et al."]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: null
  - title: "Toward understanding catastrophic forgetting in continual learning"
    authors: ["Cuong V. Nguyen", "Alessandro Achille", "Michael Lam", "et al."]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1908.01091"
  - title: "GPT-4 Technical Report"
    authors: ["OpenAI"]
    year: 2023
    venue: "CoRR"
    doi: "10.48550/arXiv.2303.08774"
    url: "https://doi.org/10.48550/arXiv.2303.08774"
    arxiv_id: "2303.08774"
  - title: "Training language models to follow instructions with human feedback (InstructGPT)"
    authors: ["Long Ouyang", "Jeffrey Wu", "Xu Jiang", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Carbon emissions and large neural network training"
    authors: ["David Patterson", "Joseph Gonzalez", "Quoc Le", "et al."]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2104.10350"
  - title: "The RefinedWeb dataset for Falcon LLM: Outperforming curated corpora with web data, and web data only"
    authors: ["Guilherme Penedo", "Quentin Malartic", "Daniel Hesslow", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficiently scaling transformer inference"
    authors: ["Reiner Pope", "Sholto Douglas", "Aakanksha Chowdhery", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Scaling language models: Methods, analysis & insights from training Gopher"
    authors: ["Jack W. Rae", "Sebastian Borgeaud", "Trevor Cai", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Know what you don't know: Unanswerable questions for SQuAD"
    authors: ["Pranav Rajpurkar", "Robin Jia", "Percy Liang"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1806.03822"
  - title: "Effect of scale on catastrophic forgetting in neural networks"
    authors: ["Vinay Venkatesh Ramasesh", "Aitor Lewkowycz", "Ethan Dyer"]
    year: 2021
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Open-domain conversational agents: Current progress, open problems, and future directions"
    authors: ["Stephen Roller", "Y-Lan Boureau", "Jason Weston", "et al."]
    year: 2020
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2006.12442"
  - title: "WinoGrande: An adversarial Winograd schema challenge at scale"
    authors: ["Keisuke Sakaguchi", "Ronan Le Bras", "Chandra Bhagavatula", "Yejin Choi"]
    year: 2021
    venue: "CACM"
    doi: null
    url: null
    arxiv_id: null
  - title: "SocialIQA: Commonsense reasoning about social interactions"
    authors: ["Maarten Sap", "Hannah Rashkin", "Derek Chen", "Ronan LeBras", "Yejin Choi"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1904.09728"
  - title: "BLOOM: A 176B-parameter open-access multilingual language model"
    authors: ["Teven Le Scao", "Angela Fan", "Christopher Akiki", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2211.05100"
  - title: "Toolformer: Language models can teach themselves to use tools"
    authors: ["Timo Schick", "Jane Dwivedi-Yu", "Roberto Dessì", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2302.04761"
  - title: "Proximal policy optimization algorithms"
    authors: ["John Schulman", "Filip Wolski", "Prafulla Dhariwal", "Alec Radford", "Oleg Klimov"]
    year: 2017
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1707.06347"
  - title: "Discriminative adversarial search for abstractive summarization"
    authors: ["Thomas Scialom", "Paul-Alexis Dray", "Sylvain Lamprier", "et al."]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "ColdGANs: Taming language GANs with cautious sampling strategies"
    authors: ["Thomas Scialom", "Paul-Alexis Dray", "Sylvain Lamprier", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neural machine translation of rare words with subword units (BPE)"
    authors: ["Rico Sennrich", "Barry Haddow", "Alexandra Birch"]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "SCROLLS: Standardized comparison over long language sequences"
    authors: ["Uri Shaham", "Elad Segal", "Maor Ivgi", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: null
    url: "https://aclanthology.org/2022.emnlp-main.823"
    arxiv_id: null
  - title: "Fast transformer decoding: One write-head is all you need"
    authors: ["Noam Shazeer"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "GLU variants improve transformer (SwiGLU)"
    authors: ["Noam Shazeer"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Megatron-LM: Training multi-billion parameter language models using model parallelism"
    authors: ["Mohammad Shoeybi", "Mostofa Patwary", "Raul Puri", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "The curse of recursion: Training on generated data makes models forget"
    authors: ["Ilia Shumailov", "Zakhar Shumaylov", "Yiren Zhao", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2305.17493"
  - title: "Hi, my name is Martha: Using names to measure and mitigate bias in generative dialogue models"
    authors: ["Eric Michael Smith", "Adina Williams"]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2109.03300"
  - title: "'I'm sorry to hear that': Finding new biases in language models with a holistic descriptor dataset (HolisticBias)"
    authors: ["Eric Michael Smith", "Melissa Hall", "Melanie Kambadur", "Eleonora Presani", "Adina Williams"]
    year: 2022
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Evaluating the social impact of generative AI systems in systems and society"
    authors: ["Irene Solaiman", "Zeerak Talat", "William Agnew", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2306.05949"
  - title: "Learning to summarize from human feedback"
    authors: ["Nisan Stiennon", "Long Ouyang", "Jeff Wu", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "RoFormer: Enhanced transformer with rotary position embedding (RoPE)"
    authors: ["Jianlin Su", "Yu Lu", "Shengfeng Pan", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Challenging BIG-bench tasks and whether chain-of-thought can solve them (BBH)"
    authors: ["Mirac Suzgun", "Nathan Scales", "Nathanael Schärli", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2210.09261"
  - title: "Growing up together: Structured exploration for large action spaces"
    authors: ["Gabriel Synnaeve", "Jonas Gehring", "Zeming Lin", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fewer errors, but more stereotypes? The effect of model size on gender bias"
    authors: ["Yarden Tal", "Inbal Magar", "Roy Schwartz"]
    year: 2022
    venue: "GeBNLP"
    doi: "10.18653/v1/2022.gebnlp-1.13"
    url: "https://aclanthology.org/2022.gebnlp-1.13"
    arxiv_id: null
  - title: "CommonsenseQA: A question answering challenge targeting commonsense knowledge"
    authors: ["Alon Talmor", "Jonathan Herzig", "Nicholas Lourie", "Jonathan Berant"]
    year: 2018
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1811.00937"
  - title: "Stanford Alpaca: An instruction-following LLaMA model"
    authors: ["Rohan Taori", "Ishaan Gulrajani", "Tianyi Zhang", "et al."]
    year: 2023
    venue: "GitHub"
    doi: null
    url: "https://github.com/tatsu-lab/stanford_alpaca"
    arxiv_id: null
  - title: "Galactica: A large language model for science"
    authors: ["Ross Taylor", "Marcin Kardas", "Guillem Cucurull", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2211.09085"
  - title: "LLaMA: Open and efficient foundation language models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2302.13971"
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Grandmaster level in StarCraft II using multi-agent reinforcement learning"
    authors: ["Oriol Vinyals", "Igor Babuschkin", "Wojciech M. Czarnecki", "et al."]
    year: 2019
    venue: "Nature"
    doi: null
    url: null
    arxiv_id: null
  - title: "Self-instruct: Aligning language model with self generated instructions"
    authors: ["Yizhong Wang", "Yeganeh Kordi", "Swaroop Mishra", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2212.10560"
  - title: "The impact of artificial intelligence on the labor market"
    authors: ["Michael Webb"]
    year: 2019
    venue: "SSRN 3482150"
    doi: null
    url: null
    arxiv_id: null
  - title: "Finetuned language models are zero-shot learners (FLAN)"
    authors: ["Jason Wei", "Maarten Bosma", "Vincent Zhao", "et al."]
    year: 2021
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Chain-of-thought prompting elicits reasoning in large language models"
    authors: ["Jason Wei", "Xuezhi Wang", "Dale Schuurmans", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Ethical and social risks of harm from language models"
    authors: ["Laura Weidinger", "John Mellor", "Maribeth Rauh", "et al."]
    year: 2021
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2112.04359"
  - title: "Challenges in detoxifying language models"
    authors: ["Johannes Welbl", "Amelia Glaese", "Jonathan Uesato", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sustainable AI: Environmental implications, challenges and opportunities"
    authors: ["Carole-Jean Wu", "Ramya Raghavendra", "Udit Gupta", "et al."]
    year: 2022
    venue: "MLSys"
    doi: null
    url: null
    arxiv_id: null
  - title: "Recipes for safety in open-domain chatbots"
    authors: ["Jing Xu", "Da Ju", "Margaret Li", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "HellaSwag: Can a machine really finish your sentence?"
    authors: ["Rowan Zellers", "Ari Holtzman", "Yonatan Bisk", "Ali Farhadi", "Yejin Choi"]
    year: 2019
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "1905.07830"
  - title: "Defending against neural fake news"
    authors: ["Rowan Zellers", "Ari Holtzman", "Hannah Rashkin", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Root mean square layer normalization (RMSNorm)"
    authors: ["Biao Zhang", "Rico Sennrich"]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "OPT: Open pre-trained transformer language models"
    authors: ["Susan Zhang", "Stephen Roller", "Naman Goyal", "et al."]
    year: 2022
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2205.01068"
  - title: "PyTorch FSDP: Experiences on scaling fully sharded data parallel"
    authors: ["Yanli Zhao", "Andrew Gu", "Rohan Varma", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "AGIEval: A human-centric benchmark for evaluating foundation models"
    authors: ["Wanjun Zhong", "Ruixiang Cui", "Yiduo Guo", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2304.06364"
  - title: "LIMA: Less is more for alignment"
    authors: ["Chunting Zhou", "Pengfei Liu", "Puxin Xu", "et al."]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2305.11206"
  - title: "Large language models are human-level prompt engineers"
    authors: ["Yongchao Zhou", "Andrei Ioan Muresanu", "Ziwen Han", "et al."]
    year: 2022
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exploring AI ethics of ChatGPT: A diagnostic analysis"
    authors: ["Terry Yue Zhuo", "Yujin Huang", "Chunyang Chen", "Zhenchang Xing"]
    year: 2023
    venue: "arXiv"
    doi: null
    url: null
    arxiv_id: "2301.12867"
  - title: "Artificial intelligence, automation, and work"
    authors: ["Daron Acemoglu", "Pascual Restrepo"]
    year: 2018
    venue: "The Economics of Artificial Intelligence: An Agenda, University of Chicago Press"
    doi: null
    url: null
    arxiv_id: null
  - title: "Is automation labor-displacing? Productivity growth, employment, and the labor share"
    authors: ["David Autor", "Anna Salomons"]
    year: 2018
    venue: "NBER Technical Report"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 11
  title: "Evolution of Llama 2-Chat — win-rate % of Llama 2-Chat compared to ChatGPT across SFT/RLHF iterations, judged by Meta reward models (left) and GPT-4 (right)"
  page: 18
  image_path: "figures/touvron-2023-llama-2-fig.png"
---

# Llama 2: Open Foundation and Fine-Tuned Chat Models

**Authors:** Hugo Touvron, Louis Martin, Kevin Stone, et al. (GenAI, Meta)
**Published:** 2023-07 · [Source](https://arxiv.org/abs/2307.09288)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Meta's GenAI team release Llama 2, a family of openly licensed 7B/13B/34B/70B base models and a chat-tuned counterpart (Llama 2-Chat), with the goal of giving the open community a credible substitute for closed "product" LLMs like ChatGPT, Bard, and Claude. The base models are pretrained on a new 2-trillion-token public-data mix (40% more tokens and 2x the context length of Llama 1, plus grouped-query attention for the 34B/70B variants); on grouped academic benchmarks the 70B beats every other open base model and matches PaLM-540B on most tasks, though it still trails GPT-4 and PaLM-2-L. The chat models are aligned via tens of thousands of high-quality SFT examples (they stopped at 27,540 after finding that model samples were already competitive with hand-written ones), 1,418,091 Meta-collected binary preference comparisons (vs. ~1.5M from all other public preference datasets combined), and five iterative RLHF rounds combining Rejection Sampling (from the largest 70B model, distilled into the smaller ones) with PPO; helpfulness and safety are trained as two separate reward models because the authors found the single-reward setup confused the model on the helpfulness/safety trade-off. On ~4,000 human-rated helpfulness prompts, Llama 2-Chat 70B reaches a 36% win rate and 31.5% tie rate against gpt-3.5-turbo-0301; on ~2,000 adversarial safety prompts it matches or beats ChatGPT on violation rate. The paper also introduces Ghost Attention (GAtt), a fine-tuning data hack that keeps "act as X" / "answer in haiku" system instructions honoured over 20+ turns; documents emergent zero-shot tool use (Llama 2-Chat 67.1/69.2/82.4 on ASDiv/SVAMP/MAWPS with calculator access, versus Toolformer's 40.4/29.4/44.0); reports that toxicity in fine-tuned Llama 2-Chat drops to ≈0.0% on ToxiGen (vs. 21-26% in the base model) while truthfulness on TruthfulQA jumps from 50.18 to 64.14 on 70B; and red-teams the models with 350+ specialists across categories like criminal planning, CBRN weapons, and election misinformation, driving the 7B's "violations per person-hour" from 1.8 down to 0.45.

## Key Takeaway

The biggest move toward closed-source-quality chat models isn't a bigger model or a smarter algorithm — it's industrial-scale, on-distribution preference data and the willingness to throw away your previously curated supervised data once the model can out-write your annotators. Meta deliberately *capped* SFT at 27.5k examples after noticing the SFT model's samples were as good as the human-written ones, then collected an order of magnitude more preference comparisons (~1.4M) and iterated RLHF five times. The hard work isn't writing demonstrations; it's keeping a reward model that stays on-distribution with the policy.

## Implications

- **Stop scaling SFT, start scaling preference annotation**: The paper explicitly says they stopped collecting SFT data at 27,540 examples because "outputs sampled from the resulting SFT model were often competitive with SFT data handwritten by human annotators." If you're aligning a model, your annotation budget should mostly buy *comparisons*, not demonstrations, once you're past a few tens of thousands of high-quality SFT pairs.
- **Train helpfulness and safety as separate reward models**: A single reward model has to learn both "pick the better helpful answer" and "refuse adversarial prompts," which the authors found confused training. They use two RMs with a piecewise selection rule (use the safety RM if the prompt is tagged unsafe or the safety score is below 0.15, otherwise use helpfulness) and a precision/recall of 0.89/0.55 on safety routing. The lesson: if your objectives are in tension, split the reward.
- **Keep the reward model on-distribution by collecting new preferences each iteration**: Because the policy distribution shifts as the model improves, an old reward model gets "hyper-specialized" and degrades quickly. Meta collected new preference batches weekly, retrained the RM, then trained RLHF-V1...V5. If you skip this loop, your reward signal goes stale and Goodharting kicks in.
- **Distill the big model into the small ones via rejection sampling**: Rejection sampling was only run on the 70B; the 7B/13B were fine-tuned on the 70B's best-scored samples. This is a cheap, deployable form of knowledge distillation that piggybacks on RLHF — you get smaller models that punch above their weight without a separate distillation pipeline.
- **Don't over-filter pretraining data — fix safety in fine-tuning instead**: Meta deliberately did not aggressively scrub toxic data from pretraining because it (a) preserved the model's ability to be used for downstream tasks like hate-speech classification, (b) avoided accidentally erasing minority demographic groups, and (c) made subsequent safety fine-tuning *more* sample-efficient. Aggressive pretraining filtering can leave you with a worse end-state model.
- **Ghost Attention is a near-free trick for multi-turn instruction adherence**: GAtt synthesizes training conversations where a system-level instruction is repeated on every user turn during data construction but zeroed out from the loss on prior turns. After RLHF-V3 it kept Llama 2-Chat following "act as Napoleon" or "answer in haiku" instructions for 20+ turns. If your chat model forgets its system prompt mid-conversation, this is a cheaper fix than retraining with a longer context.
- **Treat your reward model as your primary eval, not just a training signal**: The paper validates that reward models are "well calibrated with our human preference annotations" (Figure 29, Appendix) and uses RM scores as the main fast iteration metric, holding back human eval for major version bumps. Building your RM well enough to *trust* its scores as a proxy can collapse weeks of human-eval lead time into hours of automated scoring.
- **Open release is the responsibility lever, not just the goodwill lever**: Meta's argument for open weights is that it lets the broader community find failure modes faster than any internal red team, especially in non-English languages where their own data was limited. They also note pretraining costs (3.3M GPU-hours, 539 tCO2eq, all offset) don't need to be re-incurred by downstream developers — open release is the carbon-efficient default once the data and methods are reproducible.

## How to Apply It (method)

**Scenario:** You're a venture-builder shipping a niche conversational product — say, a coaching assistant for paragliding pilots — and you want a chat model that knows your domain, refuses dangerous-meteorology questions safely, and stays in character ("act as a wind-window safety coach") across long conversations. You can't outsource this to a closed API because you need on-device deployment, but you also can't afford a 70B pretraining run. The Llama 2-Chat recipe gives you a template for fine-tuning an open base model end-to-end.

**Steps:**

1. **Start from an open base model, not a chat model**: Pick a Llama-2-7B/13B base checkpoint (or whatever the current open foundation is). Resist the urge to start from an already-tuned chat model — you'll inherit alignment choices you don't want, and the paper shows that base models with *less* aggressive pretraining filtering need fewer examples to safety-tune cleanly.

2. **Collect ~20-30k high-quality SFT pairs, then stop**: Write your own (prompt, ideal-answer) pairs for the use case — paraglider flight planning, weather interpretation, gear advice, safety refusals. Meta found ~27.5k was enough; quality (your own vendor annotators on a tight rubric, not random crowdworkers) beat volume. Compare annotator-written answers to model-generated answers on a sample of 180 — once the model's samples are competitive, switch to preference annotation.

3. **Split your annotation pipeline into helpfulness and safety streams** with different rubrics:
   - **Helpfulness rubric**: "Does the answer fulfill the user's actual request?"
   - **Safety rubric**: "Adversarial prompts only — does the answer enable harm? Tag the response as (safe-vs-unsafe / both-safe / both-unsafe), with the chosen-safe-rejected-unsafe class targeted at ~18% of the safety dataset."

4. **Collect binary preference comparisons with a 4-point margin scale**: For each prompt, present two model samples (different temperatures, ideally different intermediate checkpoints). Annotators pick a winner and rate the margin: significantly better / better / slightly better / negligibly better. Aim for ≥100k Meta-style preference pairs over time — fewer if your domain is narrow.

5. **Train two reward models, both initialized from your SFT checkpoint**: Use the binary-ranking loss with a margin term:

   ```
   L_ranking = -log(sigmoid( r(x, y_chosen) - r(x, y_rejected) - m(rating) ))
   ```

   where `m(rating)` is larger for "significantly better" pairs. Train one epoch — longer overfits. Use a max LR of 5e-6 for ~30B+ models or 1e-5 for smaller ones, batch size 512 pairs, cosine schedule down to 10% of peak.

6. **Combine the two RMs at policy training time** with a piecewise rule. If the prompt is tagged unsafe (or safety RM score < 0.15), use the safety RM's score as the reward; otherwise use helpfulness. Whiten the combined scores (apply logit then standardize) to balance with the KL penalty.

7. **Iterate RLHF in 5 rounds, alternating rejection sampling and PPO**: For rounds 1-4, do Rejection Sampling fine-tuning only — sample K outputs per prompt from your largest model, pick the highest-reward one, fine-tune on those gold samples. Then for the smaller variants, fine-tune on the *same* gold samples to distill the big model's behaviour. For round 5, apply PPO on top of the rejection-sampling checkpoint:

   ```
   R(g|p) = R_combined(g|p) - β * KL( π_θ(g|p) || π_0(g|p) )
   ```

   with β = 0.01 for 7B/13B and β = 0.005 for 30B+. PPO clip 0.2, batch 512, ~200-400 iterations, early-stop on held-out reward.

8. **Re-collect preference data on the new model after each round**: Don't reuse the old preference data — sample from your latest RLHF-Vk model, ask annotators to compare again. This keeps the RM on-distribution as the policy shifts.

9. **Apply Ghost Attention for system-prompt adherence**: After RLHF-V3, build a synthetic SFT dataset where each multi-turn conversation has a system instruction (e.g., "Always respond as a calm safety coach") concatenated onto *every* user turn. Sample completions with your latest RLHF model. At training time, zero out the loss on all tokens except the final assistant message. Vary the instruction template ("Hobbies", "Persona", "Language" — Meta randomly combined these).

10. **Red-team with a multi-disciplinary team**: Recruit 10-30 testers covering your domain risks (for paragliding: weather-fraud, equipment-tampering, mountain-rescue interference) plus general categories (illegal/criminal, hate, unqualified medical/legal advice). Track γ = "successful adversarial prompts per person-hour" and the rejection rate on previously-known attacks; aim for γ ↓ and ≥80-90% rejection of prior known attacks per release.

11. **Validate with a real human eval before release**: ~2-4k prompts (mix of single-turn and multi-turn), 3 raters each, 7-point Likert on helpfulness and 5-point Likert on safety (1-2 = violation). Use Gwet's AC2 for inter-rater reliability — Meta saw 0.37-0.55 on helpfulness, 0.70-0.95 on safety. Lower IRR means the comparison is close; higher means one model clearly wins.

**Expected outcome:** A small (7-13B) open-weights coaching model that meaningfully closes the gap to GPT-3.5-class proprietary chat models in your niche, with a documented safety-violation rate, a calibrated reward model you can use as a fast iteration metric, and a recipe that compounds — each new annotation batch produces a measurably better model, and you can prove it with both RM scores and held-out human evaluation.

## Best Figure

![Figure 11 — Evolution of Llama 2-Chat: win-rate % vs ChatGPT across SFT/RLHF iterations (page 18)](figures/touvron-2023-llama-2-fig.png)

**Image Candidates:**
- Figure 1 (p. 3): Helpfulness human evaluation results comparing Llama 2-Chat to open and closed-source models on ~4,000 prompts — the marquee headline figure that frames the paper's central claim.
- Figure 4 (p. 5): The training pipeline diagram (pretraining → SFT → iterative RLHF with rejection sampling + PPO + reward modeling) — the clearest one-glance summary of the methodology.
- Figure 11 (p. 18): Two scatter plots showing the progression from SFT-v1 through RLHF-V5 along (helpfulness × harmlessness) axes, judged independently by Meta's reward models (left) and GPT-4 (right) — every iteration moves up and right, and both judges agree, which is the paper's strongest evidence that RLHF actually works.

**Best Image:**
- Figure Name: Figure 11: "Evolution of Llama 2-Chat"
- Figure Page: 18
- Slide Caption: Five rounds of RLHF push Llama 2-Chat from a sub-ChatGPT SFT baseline (bottom-left) to a model that beats ChatGPT on both helpfulness and harmlessness, with two independent judges (Meta RM, GPT-4) agreeing on the trajectory.
- Description: Figure 11 plots six successive checkpoints of Llama 2-Chat — SFT-v1, SFT-v2, RLHF-V1, V2, V3, V4, and V5 (with and without PPO) — on a 2D (helpfulness %, harmlessness %) plane, with the win-rate measured against ChatGPT (gpt-3.5-turbo-0301). The left panel uses Meta's own reward models as judges; the right panel uses GPT-4 as a more neutral judge. Both panels show the same shape: SFT-v1 sits near the origin (~40% helpfulness, ~20% harmlessness), each RLHF round pushes the point up and to the right, and RLHF-V5 with PPO ends up in the >70% helpfulness, >70% harmlessness quadrant on the Meta-judge plot (and >60% on both axes on the GPT-4-judge plot). The paper notes that GPT-4 should be less biased toward Llama 2 — and indeed the absolute win rates are lower on the right — but the rank-order of the seven checkpoints is identical between judges, which is the methodological point: every iteration was a real improvement, not reward-model overfitting. This single figure is the paper's strongest single-view argument that iterative RLHF compounds and that the helpfulness/safety trade-off can be avoided when you train them as separate reward models with on-distribution data.

## What Experts Overlook

The detail most readers blow past is that Llama 2-Chat's biggest *quality* leverage point is not the choice of RL algorithm (PPO vs Rejection Sampling vs DPO) but the operational discipline of **re-collecting human preference data on the new model's outputs after every single RLHF iteration, weekly**. The paper makes this visible in a single off-hand sentence: "Since reward model accuracy can quickly degrade if not exposed to this new sample distribution, i.e., from hyper-specialization, it is important before a new Llama 2-Chat tuning iteration to gather new preference data using the latest Llama 2-Chat iterations." They call this "keeping the reward model on-distribution." Everything else — PPO hyperparameters, rejection-sampling K, KL coefficients — is downstream of this loop.

**Why it matters:** Most public RLHF tutorials present the pipeline as a single shot: collect a preference dataset, train an RM once, then PPO. But the policy distribution shifts on the *first* gradient step, and from that point on your RM is being asked to score samples it has never seen. The reward signal gets gradually less informative even as the loss curves look great — classic Goodhart. Meta's discipline of "new preferences every week from the latest model" is what kept their reward signal honest for five iterations. Without that operational loop, you'll see your reward scores climb while human eval flatlines or regresses, and you'll mistake reward-hacking for progress.

**Example of good use:** A founder fine-tuning Llama 2 for a customer-support chatbot sets up a weekly cadence: model trained on Monday → sampled outputs labeled by annotators Tuesday-Wednesday → reward model retrained Thursday → next RLHF round Friday. Even with a small team, the *cadence* is what compounds; after 6-8 cycles, the help score on a held-out validation set keeps climbing because the RM is always evaluating in-distribution work. They catch a reward-hacking artifact (model gaming politeness markers) in cycle 3 because the new annotators flag it, and they can rapidly correct.

**Example of misapplication:** A research team grabs the Llama 2 preference dataset off Hugging Face, trains a reward model once, and runs PPO for 50 iterations. The reward goes up steadily, looks great on the trained RM, and the team ships. In production, users immediately notice the model gives smooth-sounding but factually wrong answers and over-formats responses with bullet points. The RM was scoring fluency/format patterns it learned from old data, not what real users currently care about. The fix is to not just train more — it's to re-collect preferences on the *current* model's outputs and retrain the RM. Skipping the on-distribution refresh is the single most common silent failure mode in RLHF.

## Extracted Prompts

The paper contains a small number of operational prompts/templates used in fine-tuning and evaluation. Note that most of the alignment work is data-driven (preference labels, demonstrations), not prompt-driven, so the list is shorter than for a typical prompt-engineering paper.

**Prompt explanation:** Generic safety preprompt for context distillation — prefixed to adversarial prompts so the model generates safer responses, which are then used as fine-tuning targets *without* the preprompt (distilling the safety-context into the weights).

```
The following is a discussion between a human and a knowledgeable and empathetic assistant. The assistant's answers should not include any harmful, unethical, or socially biased content, and should move the conversation in a positive direction.
```

**Prompt explanation:** Risk-category-tailored preprompt with answer template — used in context distillation for prompts tagged with a specific risk category (here, false information / disinformation). More targeted than the generic preprompt and the paper finds it produces higher Safety RM score uplift.

```
The following is a question that can ellicit unsafe behavior from you. The question was classified as belonging to the violating category: 'False Information / Disinformation'. You should answer using the following template:

"1. Address the prompt. the model should immediately refute any misinformation in the prompt.
2. Add context and additional information. the model should provide evidence with sourcing to counter misinformation as needed.
3. Encourage users to ask for/view additional info as appropriate. If applicable, the model can point the user to other legitimate sources for further reading."
```

**Prompt explanation:** GPT-4 zero-shot reward-modeling prompt used as a comparison baseline — Meta wanted to see whether their custom RMs beat a strong general model used as a pairwise judge.

```
Choose the best answer between A and B.
```

**Prompt explanation:** Ghost Attention training-time system instructions — synthetic constraints that get concatenated onto every user turn during fine-tuning data construction, so the model learns to honour them across multi-turn dialogues. Note these are *templates*, not exact strings; the paper says Meta "constructed the final instruction by randomly combining the above constraints" and shortened them half the time (e.g., "Always act as Napoleon from now" → "Figure: Napoleon").

```
You enjoy e.g. Tennis.
Speak in e.g. French.
Act as e.g. Napoleon.
```

## Citations

The paper has ~130 distinct references in its bibliography. A representative sample of the most load-bearing citations (full list in the `citations:` frontmatter array above):

- Ouyang et al. 2022 — *Training language models to follow instructions with human feedback* (InstructGPT) — the direct methodological predecessor for SFT + RM + PPO.
- Christiano et al. 2017 — *Deep reinforcement learning from human preferences* — the original RLHF paper.
- Schulman et al. 2017 — *Proximal policy optimization algorithms* — the PPO algorithm used in the final RLHF rounds.
- Stiennon et al. 2020 — *Learning to summarize from human feedback* — the RLHF-for-text-generation recipe Meta builds on.
- Bai et al. 2022a — *Training a helpful and harmless assistant with RLHF* — Anthropic's helpful/harmless data and methodology that informs the dual-reward setup.
- Bai et al. 2022b — *Constitutional AI: Harmlessness from AI feedback* — the RLAIF and context-distillation references.
- Touvron et al. 2023 — *LLaMA: Open and efficient foundation language models* — the immediate predecessor Llama 1, which Llama 2 inherits its architecture from.
- Vaswani et al. 2017 — *Attention is all you need* — the underlying transformer architecture.
- Brown et al. 2020 — *Language Models are Few-Shot Learners* (GPT-3) — the closed-source baseline they're trying to match.
- Hoffmann et al. 2022 — *Training compute-optimal large language models* (Chinchilla) — the scaling laws Llama 2 internalizes.
- Kaplan et al. 2020 — *Scaling laws for neural language models* — the prior scaling-laws baseline.
- Ainslie et al. 2023 — *GQA: Training generalized multi-query transformer models from multi-head checkpoints* — the grouped-query attention used in the 34B and 70B variants.
- Schick et al. 2023 — *Toolformer* — the tool-use baseline Llama 2-Chat surpasses zero-shot.
- Zhou et al. 2023 — *LIMA: Less is more for alignment* — the "quality > quantity" SFT finding that aligns with Meta's decision to cap at 27.5k SFT examples.
- Almazrouei et al. 2023 — *Falcon-40B* — the strongest open-base competitor at the time.
- Scao et al. 2022 — *BLOOM* — the prior reference open foundation model.
- Chowdhery et al. 2022 — *PaLM* — the 540B closed comparison point.
- Hartvigsen et al. 2022 — *ToxiGen* — the safety benchmark used to show fine-tuning drives toxic generation to ~0%.
- Lin et al. 2021 — *TruthfulQA* — the truthfulness benchmark showing fine-tuning gains from 50.18 to 64.14 (70B).
- Gwet 2008/2014 — *Inter-rater reliability* — the AC1/AC2 statistic Meta uses to measure annotator agreement.

## Related Digests

- [[touvron-2023-llama-foundation-models]] — LLaMA (1): the immediate predecessor base model architecture Llama 2 builds on
- [[brown-2020-gpt3-few-shot]] — Language Models are Few-Shot Learners (GPT-3): the closed-source baseline Llama 2 is built to challenge
- [[radford-2019-gpt2-multitask]] — GPT-2: predecessor decoder-only LM showing scale + unsupervised pretraining transfer
- [[radford-2018-gpt1]] — GPT-1: the original decoder-only pretrain-then-finetune recipe
- [[vaswani-2017-attention-is-all-you-need]] — Attention Is All You Need: the transformer architecture Llama 2 inherits from
- [[bi-2020-palm-context-generation]] — PaLM-context-generation: large-scale LM context-conditioned generation

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim in the digest (27,540 SFT examples; 1,418,091 Meta preference comparisons; 36% win rate / 31.5% tie rate vs ChatGPT on ~4k prompts; ~2,000 adversarial safety prompts; γ 1.8→0.45 on 7B; 90% rejection rate model-over-model; 350+ red teamers; 3.3M GPU-hours / 539 tCO2eq; safety threshold 0.15 with precision 0.89 / recall 0.55; PPO β=0.01 for 7B/13B, β=0.005 for 34B/70B; ToxiGen drop from 24.6→0.01 on 70B; TruthfulQA 50.18→64.14 on 70B; tool-use scores 67.1/69.2/82.4 on ASDiv/SVAMP/MAWPS vs Toolformer 40.4/29.4/44.0; safety dataset split 18/47/35%; SFT validation on 180 examples; Gwet AC2 0.37–0.55 helpfulness / 0.70–0.95 safety; GAtt holding 20+ turns; 2T pretraining tokens, 40% more, 2x context length, GQA on 34B/70B) is directly supported by the paper text. Methodological characterizations (two separate reward models for helpfulness/safety; piecewise reward composition; rejection sampling only on 70B then distilled into smaller variants; weekly preference re-collection to keep RM on-distribution; Ghost Attention method using zeroed loss on prior turns; context distillation prefixed then trained without prefix) match the corresponding sections of the paper.

One soft characterization worth flagging: the TLDR calls the closed-source models "Llama 2-Chat 70B...matches or beats ChatGPT on safety violation rate" — the paper says Llama 2-Chat has "comparable or lower overall violation percentage" across model sizes (Section 4.4, Figure 17), so this is fair, though the paper carefully caveats that the safety eval is "likely to be biased towards the Llama 2-Chat models" due to the content standards used. A reader relying on this digest should retain that caveat.
