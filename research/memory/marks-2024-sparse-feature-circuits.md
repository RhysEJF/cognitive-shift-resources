---
corpus: agentic-memory
kind: paper-digest
slug: marks-2024-sparse-feature-circuits
title: "Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models"
authors:
  - "Samuel Marks"
  - "Can Rager"
  - "Eric J. Michaud"
  - "Yonatan Belinkov"
  - "David Bau"
  - "Aaron Mueller"
year: 2024
publication_date: "2024-03"
venue: "ICLR 2025"
source_url: "https://arxiv.org/abs/2403.19647"
doi: null
arxiv_id: "2403.19647"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "By treating SAE features as nodes in the model's computation graph and using linear approximations of indirect effect, the authors discover sparse, human-interpretable causal circuits that are roughly two orders of magnitude smaller than equivalent neuron circuits — and demonstrate they are editable, not just diagnostic, by surgically ablating spurious-gender features to debias a profession classifier without any disambiguating data."
topics:
  - mechanistic-interpretability
  - sparse-autoencoders
  - feature-circuits
  - causal-attribution
  - integrated-gradients
  - attribution-patching
  - debiasing
  - shift
  - unsupervised-behavior-discovery
  - dictionary-learning
tags:
  - paper
  - interpretability
  - sae
  - circuit-discovery
  - engram-ground
  - engram-aggregate
  - engram-encode
  - causal-graph
entities:
  - marks-samuel
  - rager-can
  - michaud-eric
  - belinkov-yonatan
  - bau-david
  - mueller-aaron
  - pythia-70m
  - gemma-2-2b
  - gemma-scope
  - neuronpedia
  - bias-in-bios
related_digests:
  - mao-2026-agent-memory-circuits
citations:
  - title: "Probing classifiers: Promises, shortcomings, and advances"
    authors: ["Yonatan Belinkov"]
    year: 2022
    venue: "Computational Linguistics"
    doi: null
    url: null
    arxiv_id: null
  - title: "LEACE: Perfect linear concept erasure in closed form"
    authors: ["Nora Belrose", "David Schneider-Joseph", "Shauli Ravfogel", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Pythia: A suite for analyzing large language models across training and scaling"
    authors: ["Stella Biderman", "Hailey Schoelkopf", "Quentin Gregory Anthony", "et al."]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards monosemanticity: Decomposing language models with dictionary learning"
    authors: ["Trenton Bricken", "Adly Templeton", "Joshua Batson", "et al."]
    year: 2023
    venue: "Transformer Circuits Thread"
    doi: null
    url: null
    arxiv_id: null
  - title: "Understanding disentangling in beta-VAE"
    authors: ["Christopher P. Burgess", "Irina Higgins", "Arka Pal", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Weak-to-strong generalization: Eliciting strong capabilities with weak supervision"
    authors: ["Collin Burns", "Pavel Izmailov", "Jan Hendrik Kirchner", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2312.09390"
  - title: "Open problems and fundamental limitations of reinforcement learning from human feedback"
    authors: ["Stephen Casper", "Xander Davies", "Claudia Shi", "et al."]
    year: 2023
    venue: "TMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sudden drops in the loss: Syntax acquisition, phase transitions, and simplicity bias in MLMs"
    authors: ["Angelica Chen", "Ravid Shwartz-Ziv", "Kyunghyun Cho", "et al."]
    year: 2024
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Isolating sources of disentanglement in variational autoencoders"
    authors: ["Tian Qi Chen", "Xuechen Li", "Roger Grosse", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Infogan: interpretable representation learning by information maximizing generative adversarial nets"
    authors: ["Xi Chen", "Yan Duan", "Rein Houthooft", "et al."]
    year: 2016
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep reinforcement learning from human preferences"
    authors: ["Paul Christiano", "Jan Leike", "Tom B. Brown", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1706.03741"
  - title: "Towards automated circuit discovery for mechanistic interpretability"
    authors: ["Arthur Conmy", "Augustine N. Mavor-Parker", "Aengus Lynch", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Environment inference for invariant learning"
    authors: ["Elliot Creager", "Joern-Henrik Jacobsen", "Richard Zemel"]
    year: 2021
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sparse autoencoders find highly interpretable features in language models"
    authors: ["Hoagy Cunningham", "Aidan Ewart", "Logan Riggs", "et al."]
    year: 2024
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Bias in bios: A case study of semantic representation bias in a high-stakes setting"
    authors: ["Maria De-Arteaga", "Alexey Romanov", "Hanna Wallach", "et al."]
    year: 2019
    venue: "FAT*"
    doi: null
    url: null
    arxiv_id: null
  - title: "Disentangling factors of variation via generative entangling"
    authors: ["Guillaume Desjardins", "Aaron Courville", "Yoshua Bengio"]
    year: 2012
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1210.5474"
  - title: "Toy models of superposition"
    authors: ["Nelson Elhage", "Tristan Hume", "Catherine Olsson", "et al."]
    year: 2022
    venue: "Transformer Circuits Thread"
    doi: null
    url: null
    arxiv_id: null
  - title: "Causal analysis of syntactic agreement mechanisms in neural language models"
    authors: ["Matthew Finlayson", "Aaron Mueller", "Sebastian Gehrmann", "et al."]
    year: 2021
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Interpreting CLIP's image representation via text-based decomposition"
    authors: ["Yossi Gandelsman", "Alexei A. Efros", "Jacob Steinhardt"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.05916"
  - title: "The Pile: An 800GB dataset of diverse text for language modeling"
    authors: ["Leo Gao", "Stella Biderman", "Sid Black", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2101.00027"
  - title: "Scaling and evaluating sparse autoencoders"
    authors: ["Leo Gao", "Tom Dupré la Tour", "Henk Tillman", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2406.04093"
  - title: "Causal abstractions of neural networks"
    authors: ["Atticus Geiger", "Hanson Lu", "Thomas Icard", "et al."]
    year: 2021
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Inducing causal structure for interpretable neural networks"
    authors: ["Atticus Geiger", "Zhengxuan Wu", "Hanson Lu", "et al."]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Causal abstraction for faithful model interpretation"
    authors: ["Atticus Geiger", "Chris Potts", "Thomas Icard"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2301.04709"
  - title: "Dissecting recall of factual associations in auto-regressive language models"
    authors: ["Mor Geva", "Jasmijn Bastings", "Katja Filippova", "et al."]
    year: 2023
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Successor heads: Recurring, interpretable attention heads in the wild"
    authors: ["Rhys Gould", "Euan Ong", "George Ogden", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2312.09230"
  - title: "How does GPT-2 compute greater-than?: Interpreting mathematical abilities in a pre-trained language model"
    authors: ["Michael Hanna", "Ollie Liu", "Alexandre Variengien"]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Have faith in faithfulness: Going beyond circuit overlap when finding model mechanisms"
    authors: ["Michael Hanna", "Sandro Pezzelle", "Yonatan Belinkov"]
    year: 2024
    venue: "ICML Workshop on Mechanistic Interpretability"
    doi: null
    url: null
    arxiv_id: null
  - title: "The unreasonable effectiveness of easy training data for hard tasks"
    authors: ["Peter Hase", "Mohit Bansal", "Peter Clark", "et al."]
    year: 2024
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exploring linear feature disentanglement for neural networks"
    authors: ["T. He", "Z. Li", "Y. Gong", "et al."]
    year: 2022
    venue: "ICME"
    doi: null
    url: null
    arxiv_id: null
  - title: "beta-VAE: Learning basic visual concepts with a constrained variational framework"
    authors: ["Irina Higgins", "Loic Matthey", "Arka Pal", "et al."]
    year: 2017
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Simple data balancing achieves competitive worst-group-accuracy"
    authors: ["Badr Youbi Idrissi", "Martin Arjovsky", "Mohammad Pezeshki", "et al."]
    year: 2022
    venue: "CLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Shielded representations: Protecting sensitive attributes through iterative gradient-based projection"
    authors: ["Shadi Iskander", "Kira Radinsky", "Yonatan Belinkov"]
    year: 2023
    venue: "ACL Findings"
    doi: null
    url: null
    arxiv_id: null
  - title: "Leveraging prototypical representations for mitigating social bias without demographic information"
    authors: ["Shadi Iskander", "Kira Radinsky", "Yonatan Belinkov"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2403.09516"
  - title: "Interpretability beyond feature attribution: Quantitative testing with concept activation vectors (TCAV)"
    authors: ["Been Kim", "Martin Wattenberg", "Justin Gilmer", "et al."]
    year: 2018
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Disentangling by factorising"
    authors: ["Hyunjik Kim", "Andriy Mnih"]
    year: 2018
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adam: A method for stochastic optimization"
    authors: ["Diederik P. Kingma", "Jimmy Ba"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1412.6980"
  - title: "Last layer re-training is sufficient for robustness to spurious correlations"
    authors: ["Polina Kirichenko", "Pavel Izmailov", "Andrew Gordon Wilson"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2204.02937"
  - title: "AtP*: An efficient and scalable method for localizing llm behaviour to components"
    authors: ["János Kramár", "Tom Lieberum", "Rohin Shah", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2403.00745"
  - title: "Counterfactuals"
    authors: ["David K. Lewis"]
    year: 1973
    venue: "Blackwell"
    doi: null
    url: null
    arxiv_id: null
  - title: "Gemma scope: Open sparse autoencoders everywhere all at once on gemma 2"
    authors: ["Tom Lieberum", "Senthooran Rajamanoharan", "Arthur Conmy", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neuronpedia: Interactive reference and tooling for analyzing neural networks"
    authors: ["Johnny Lin", "Joseph Bloom"]
    year: 2023
    venue: "Software"
    doi: null
    url: "https://neuronpedia.org"
    arxiv_id: null
  - title: "Just train twice: Improving group robustness without training group information"
    authors: ["Evan Z Liu", "Behzad Haghgoo", "Annie S Chen", "et al."]
    year: 2021
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Decoupled weight decay regularization"
    authors: ["Ilya Loshchilov", "Frank Hutter"]
    year: 2017
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "k-sparse autoencoders"
    authors: ["Alireza Makhzani", "Brendan J. Frey"]
    year: 2013
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1312.5663"
  - title: "Locating and editing factual associations in GPT"
    authors: ["Kevin Meng", "David Bau", "Alex Andonian", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2202.05262"
  - title: "The quantization model of neural scaling"
    authors: ["Eric J Michaud", "Ziming Liu", "Uzay Girit", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "The quest for the right mediator: A history, survey, and theoretical grounding of causal interpretability"
    authors: ["Aaron Mueller", "Jannik Brinkmann", "Millicent Li", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning from failure: Training debiased classifier from biased classifier"
    authors: ["Junhyun Nam", "Hyuntak Cha", "Sungsoo Ahn", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Spread spurious attribute: Improving worst-group accuracy with spurious attribute estimation"
    authors: ["Junhyun Nam", "Jaehyung Kim", "Jaeho Lee", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Attribution patching: Activation patching at industrial scale"
    authors: ["Neel Nanda"]
    year: 2022
    venue: "blog"
    doi: null
    url: null
    arxiv_id: null
  - title: "Open source replication & commentary on Anthropic's dictionary learning paper"
    authors: ["Neel Nanda"]
    year: 2023
    venue: "blog"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fact finding: Attempting to reverse-engineer factual recall on the neuron level"
    authors: ["Neel Nanda", "Senthooran Rajamanoharan", "János Kramár", "et al."]
    year: 2023
    venue: "blog"
    doi: null
    url: null
    arxiv_id: null
  - title: "The alignment problem from a deep learning perspective"
    authors: ["Richard Ngo", "Lawrence Chan", "Sören Mindermann"]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2209.00626"
  - title: "Label-free concept bottleneck models"
    authors: ["Tuomas Oikarinen", "Subhro Das", "Lam M. Nguyen", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "In-context learning and induction heads"
    authors: ["Catherine Olsson", "Nelson Elhage", "Neel Nanda", "et al."]
    year: 2022
    venue: "Transformer Circuits Thread"
    doi: null
    url: null
    arxiv_id: null
  - title: "Distributionally robust language modeling"
    authors: ["Yonatan Oren", "Shiori Sagawa", "Tatsunori B. Hashimoto", "et al."]
    year: 2019
    venue: "EMNLP-IJCNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "BLIND: Bias removal with no demographics"
    authors: ["Hadas Orgad", "Yonatan Belinkov"]
    year: 2023
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Direct and indirect effects"
    authors: ["Judea Pearl"]
    year: 2001
    venue: "UAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Scikit-learn: Machine learning in Python"
    authors: ["F. Pedregosa", "G. Varoquaux", "A. Gramfort", "et al."]
    year: 2011
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "The hessian penalty: A weak prior for unsupervised disentanglement"
    authors: ["William Peebles", "John Peebles", "Jun-Yan Zhu", "et al."]
    year: 2020
    venue: "ECCV"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fine-tuning enhances existing mechanisms: A case study on entity tracking"
    authors: ["Nikhil Prakash", "Tamar Rott Shaham", "Tal Haklay", "et al."]
    year: 2024
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "2402.14811"
  - title: "Improving dictionary learning with gated sparse autoencoders"
    authors: ["Senthooran Rajamanoharan", "Arthur Conmy", "Lewis Smith", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2404.16014"
  - title: "Jumping ahead: Improving reconstruction fidelity with jumprelu sparse autoencoders"
    authors: ["Senthooran Rajamanoharan", "Tom Lieberum", "Nicolas Sonnerat", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2407.14435"
  - title: "Null it out: Guarding protected attributes by iterative nullspace projection"
    authors: ["Shauli Ravfogel", "Yanai Elazar", "Hila Gonen", "et al."]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Linear adversarial concept erasure"
    authors: ["Shauli Ravfogel", "Michael Twiton", "Yoav Goldberg", "et al."]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adversarial concept erasure in kernel space"
    authors: ["Shauli Ravfogel", "Francisco Vargas", "Yoav Goldberg", "et al."]
    year: 2022
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Identifiability and exchangeability for direct and indirect effects"
    authors: ["James M. Robins", "Sander Greenland"]
    year: 1992
    venue: "Epidemiology"
    doi: null
    url: null
    arxiv_id: null
  - title: "Distributionally robust neural networks"
    authors: ["Shiori Sagawa", "Pang Wei Koh", "Tatsunori B. Hashimoto", "et al."]
    year: 2020
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning Factorial Codes by Predictability Minimization"
    authors: ["Jürgen Schmidhuber"]
    year: 1992
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Explaining neural networks by decoding layer activations"
    authors: ["Johannes Schneider", "Michalis Vlachos"]
    year: 2021
    venue: "IDA"
    doi: null
    url: null
    arxiv_id: null
  - title: "BARACK: Partially supervised group robustness with guarantees"
    authors: ["Nimit Sharad Sohoni", "Maziar Sanjabi", "Nicolas Ballas", "et al."]
    year: 2022
    venue: "ICML Workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "Axiomatic attribution for deep networks"
    authors: ["Mukund Sundararajan", "Ankur Taly", "Qiqi Yan"]
    year: 2017
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Attribution patching outperforms automated circuit discovery"
    authors: ["Aaquib Syed", "Can Rager", "Arthur Conmy"]
    year: 2023
    venue: "NeurIPS Workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "Gemma 2: Improving open language models at a practical size"
    authors: ["Gemma Team", "Morgane Riviere", "Shreya Pathak", "et al."]
    year: 2024
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Scaling monosemanticity: Extracting interpretable features from claude 3 sonnet"
    authors: ["Adly Templeton", "Tom Conerly", "Jonathan Marcus", "et al."]
    year: 2024
    venue: "Transformer Circuits Thread"
    doi: null
    url: null
    arxiv_id: null
  - title: "Function vectors in large language models"
    authors: ["Eric Todd", "Millicent L. Li", "Arnab Sen Sharma", "et al."]
    year: 2024
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards debiasing NLU models from unknown biases"
    authors: ["Prasetya Ajie Utama", "Nafise Sadat Moosavi", "Iryna Gurevych"]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Investigating gender bias in language models using causal mediation analysis"
    authors: ["Jesse Vig", "Sebastian Gehrmann", "Yonatan Belinkov", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Interpretability in the wild: a circuit for indirect object identification in GPT-2 small"
    authors: ["Kevin Ro Wang", "Alexandre Variengien", "Arthur Conmy", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Double-hard debias: Tailoring word embeddings for gender bias mitigation"
    authors: ["Tianlu Wang", "Xi Victoria Lin", "Nazneen Fatema Rajani", "et al."]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Increasing robustness to spurious correlations using forgettable examples"
    authors: ["Yadollah Yaghoobzadeh", "Soroush Mehri", "Remi Tachet des Combes", "et al."]
    year: 2021
    venue: "EACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Robust and interpretable medical image classifiers via concept bottleneck models"
    authors: ["An Yan", "Yu Wang", "Yiwu Zhong", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.03182"
  - title: "Characterizing mechanisms for factual recall in language models"
    authors: ["Qinan Yu", "Jack Merullo", "Ellie Pavlick"]
    year: 2023
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study"
    authors: ["John R. Zech", "Marcus A. Badgeley", "Manway Liu", "et al."]
    year: 2018
    venue: "PLOS Medicine"
    doi: null
    url: null
    arxiv_id: null
  - title: "Coping with label shift via distributionally robust optimisation"
    authors: ["Jingzhao Zhang", "Aditya Krishna Menon", "Andreas Veit", "et al."]
    year: 2021
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Correct-N-Contrast: A contrastive approach for improving robustness to spurious correlations"
    authors: ["Michael Zhang", "Nimit S Sohoni", "Hongyang R Zhang", "et al."]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Representation engineering: A top-down approach to AI transparency"
    authors: ["Andy Zou", "Long Phan", "Sarah Chen", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2310.01405"
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "Faithfulness and completeness scores for circuits, measured on held-out data"
  page: 5
  image_path: "figures/marks-2024-sparse-feature-circuits-fig.png"
---

# Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models

**Authors:** Samuel Marks, Can Rager, Eric J. Michaud, Yonatan Belinkov, David Bau, Aaron Mueller
**Published:** 2024-03 (ICLR 2025) · [Source](https://arxiv.org/abs/2403.19647)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Mechanistic-interpretability work historically explained model behaviors via *coarse* units (attention heads, MLP blocks) that are polysemantic and hard to act on, or via fine-grained units (neurons, linear probes) that require pre-specified hypotheses. Marks et al. show a third route: treat the activations of pretrained Sparse Autoencoders (SAEs) — plus an SAE-error residual — as the *nodes* of the model's computation graph, then use linear approximations of indirect effect (attribution patching and integrated gradients) to rank both nodes and edges by causal importance and threshold them into a sparse circuit. The output is a human-interpretable causal subgraph that they evaluate on subject-verb agreement (faithfulness + completeness), use as a **debiasing tool** in their SHIFT technique (humans inspect ~50–100 features in a classifier's circuit and zero-ablate the ones judged task-irrelevant — no disambiguating data required), and finally scale to **thousands of auto-discovered behaviors** via clustering of The Pile, producing the public artifact at `feature-circuits.xyz`. Two model families are studied: Pythia-70M (with the authors' own ReLU SAEs, 64× width) and Gemma-2-2B (with the open-source Gemma Scope JumpReLU SAEs, 8× width).

The result that matters: feature circuits with ~100 nodes (Pythia) or ~500 nodes (Gemma) explain a *majority* of model behavior, whereas neuron circuits need ~1,500 or ~50,000 nodes respectively — roughly two orders of magnitude smaller, and the smaller circuit is *also* more interpretable to humans. The downstream SHIFT debiasing application is the load-bearing demonstration that this isn't just descriptive: a Bias-in-Bios classifier trained on the worst-case "ambiguous set" (gender perfectly predicts profession) is bumped from 24.4% → 89.0% worst-group accuracy on Pythia and 18.2% → 92.9% on Gemma after ablating ~50 features and retraining only the linear head — within 3 points of an oracle classifier with ground-truth balanced labels.

## Key Takeaway

**Once you have a sparse, monosemantic basis for the model's hidden states, "interpretability" stops being a one-shot post-hoc explanation and becomes an editable layer of the model's memory of how to do tasks — and the editing is human-in-the-loop, not data-driven.** SHIFT is the demonstration: a human looks at ~67 features, judges 55 of them ("promotes female-associated language", "detects he/him pronouns") to be irrelevant to the profession-classification task, zero-ablates them, and the spurious gender shortcut disappears — without ever collecting balanced labels. This shifts the role of the human operator: instead of curating disambiguating training data (the dominant paradigm in spurious-correlation literature), the operator curates the *circuit*, expressing intent at the level of "which compiled abstractions should the model be allowed to use."

For a memory-architect, the operational lesson is: when memory units are interpretable and atomic enough that a human can read them and judge their relevance, the maintainer role becomes feasible. The bottleneck in agentic memory systems is rarely retrieval — it is the absence of an interpretable unit at which a human or AI maintainer can say "this should not be load-bearing for this decision."

## Implications

ENGRAM-tagged implications for the memory-architect lens:

- **[G — Ground, primary]** Feature circuits give you provenance at a level finer than "this passage was retrieved" — they tell you *which compiled abstraction inside the model* was load-bearing for an output. For a memory system, the analog is moving from "this fact was cited" to "this learned pattern was the active mediator," which is the only level at which you can detect and surface drift between what the model has compiled and what the corpus actually says.

- **[A — Aggregate, primary]** SAE features *are* an aggregation strategy: they are the model's own compiled patterns extracted unsupervised from its training. The faithfulness curves in Figure 3 quantify the cost of going from "every neuron" to "the few features that mattered" — a 15× to 100× compression with comparable behavior. This is the most rigorous evidence I've seen for the idea that good aggregation is lossy-but-task-faithful, and that the right compression unit is the unsupervised concept, not the chunk.

- **[E — Encode] × [A — Aggregate] interaction** The encoding choice (train SAEs on hidden activations) determines what the system can later aggregate over. The paper's limitation section is explicit: "model components not captured by the SAEs will remain uninterpretable after applying our method." Translation for memory systems: if your encoding step doesn't decompose into the right primitives, no amount of downstream consolidation can recover them. The SAE-error term ε(x) the authors carry through the whole pipeline is the analog of an "uncompiled remainder" — a memory system that does write-time distillation needs an equivalent "what didn't fit" channel, otherwise you silently lose the parts that don't quantize into the existing feature set.

- **[M — Maintain, primary]** SHIFT operationalizes "AI/human as maintainer, not oracle." The operator's job in this paradigm is not to write the right memory once; it is to periodically inspect the small set of features the model is using for a given task and *remove* the ones that are wrong, biased, or stale. This is closer to garbage collection than retrieval tuning. The Bias-in-Bios result (24% → 89% worst-group accuracy from ablating 55 of 67 features) suggests the surgical-editing path has very high leverage *if* the unit of editing is interpretable.

- **[R — Retrieve, secondary]** Circuit discovery uses *indirect effect on a metric* as its ranking function, not similarity. This is a sharp counterpoint to vector-similarity retrieval: the question is not "what is nearby in semantic space" but "what causally moves the output on this distribution." For decision-relevant retrieval, an IE-ranked retriever (over compiled features rather than chunks) would surface different things than a cosine-similarity retriever — and arguably the *right* things when the downstream task is intervention rather than recall.

- **Cross-dimensional [G × A]** Carrying the SAE error ε as a first-class node is the architectural move that prevents the system from quietly promoting its own inferences to confirmed facts. The error term is a structural admission: "this part of the activation was not captured by our feature set." A memory system should make a habit of carrying analogous "unrecognized remainder" nodes — chunks/facts that the consolidation step couldn't pattern-match against any existing memory — rather than silently smoothing them into the closest existing concept.

- **[General architecture]** The compute-vs-quality trade in attribution (`IE_atp` vs `IE_ig`) maps directly onto write-time vs query-time synthesis. Attribution patching = a fast first-order Taylor approximation = "cheap, mostly right, fails at early layers"; integrated gradients = N forward+backward passes = "more accurate, more expensive." The authors use cheap everywhere except early-layer MLPs where it underestimates. This is the same shape as memory architecture: cheap encoding nearly everywhere, expensive (LLM-distilled) encoding at the specific places where cheap doesn't work.

## How to Apply It (method)

Three layered pipelines, in the order a memory-architect would borrow them:

### Pipeline 1 — Discover a feature circuit for a behavior

1. **Prerequisites.** A target LM `M`, SAEs trained for the submodules of `M` you care about (attention output, MLP output, residual stream, optionally embeddings), a dataset `D` of either contrastive input pairs `(x_clean, x_patch)` or single inputs `x`, and a real-valued metric `m` over the model's output that captures the behavior. Examples: `m = log P(have) − log P(has)` for plural agreement; `m = −log C(y|x)` for a classifier's loss on a labeled example.
2. **Wire SAEs into the forward pass.** For each SAE-equipped submodule, replace `x` with `x ← Σ fᵢ(x)·vᵢ + b + ε(x)` (Eq. 6). This is numerically a no-op but PyTorch autograd now sees `fᵢ(x)` and `ε(x)` as variables, so you can take gradients with respect to them.
3. **Compute approximate indirect effects on every node.** Use attribution patching (Eq. 3, cheap, two forward + one backward pass for every node simultaneously) for most nodes; switch to integrated gradients (Eq. 4, N=10 α-steps, ~10× more expensive) for layer-0 MLP and early residual stream where attribution patching underestimates. Average over `x ∼ D`. Filter to nodes with `|ÎE| > T_N`.
4. **Compute approximate indirect effects on edges** with the analogous linear formula (Eq. 5, App. A.1). Stop-gradients on intermediates make this a single composite backward pass. Filter to edges with `|ÎE| > T_E`.
5. **Aggregate across positions.** Templatic data: keep token-position-specific nodes, mean over examples. Non-templatic data: sum across positions first, then mean over examples (Fig. 6, App. A.2).
6. **Sweep `T_N` to trade off circuit size vs faithfulness.** Use the faithfulness metric `(m(C) − m(∅)) / (m(M) − m(∅))` to choose a working point. The authors typically target faithfulness ~0.2 for human-annotatable circuits (~80–230 nodes) and >0.5 for performance-explaining ones (~100–500 nodes).
7. **Label each feature.** Use the maximum-activating dataset exemplars (Neuronpedia provides this UI) plus the feature's top affected logits to write a short textual description of what each surviving feature represents.

### Pipeline 2 — SHIFT (spurious-feature surgery on a classifier)

The application that matters most for the memory-architect lens — it is the editable-memory move:

1. Train a linear classification head on the LM's mean-pooled residual stream activations from labeled data `D = {(xᵢ, yᵢ)}`.
2. Run Pipeline 1 with `m = −log C(y|x)` to get the classifier's feature circuit (zero-ablation variant — no contrastive pair needed).
3. **Human inspects each circuit feature** (using Neuronpedia for max-activating exemplars) and judges it task-relevant or task-irrelevant. In the BiB experiment: 55/67 Pythia features and 43/46 Gemma features were judged irrelevant — overwhelmingly gender or capitalization features rather than profession features.
4. **Zero-ablate the task-irrelevant features** (force `fᵢ(x) = 0` for those `i` during forward pass).
5. **Retrain the linear head** on the original ambiguous data using activations from the *ablated* model. The head adapts to use only the remaining features.
6. Verify on balanced/oracle data — worst-group accuracy is the load-bearing metric.

Practical detail to copy: for Gemma, *exclude BOS features* from annotation and from ablation. They have high indirect effects but are uninterpretable; ablating them disrupts the model without benefit.

### Pipeline 3 — Unsupervised circuit discovery at scale

1. **Filter The Pile** to (context, answer) pairs where Pythia-70M correctly predicts the answer with low cross-entropy (< 0.1 or 0.3 nats), excluding induction matches (where the bigram already appeared earlier in the context).
2. **Cluster** the contexts by a vector representation derived from model internals. Options the authors tried: dense activations at last-N positions, sparse SAE activations, dense indirect effects, sparse indirect effects, sparse random projections of parameter-space gradients (~30,000 dims, sparsity ~32 nonzero per row). Best results from sparse-projected gradients (following Michaud et al. 2023 quantization-model framing). Spectral clustering for ≤8,192 samples; k-means for the 100,000-sample run.
3. For each cluster, treat it as a behavior-specific dataset and run Pipeline 1 with `m = −log P(yᵢ|xᵢ)`.
4. Browse / search the resulting cluster + circuit pairs at `feature-circuits.xyz`.

### Engineering tricks worth knowing (Appendix A.3)

- **Stop-gradients on SAE errors** to prevent `∇_{fᵢ} m = 0` after the intervention. Set `x_d = x̂ + stopgrad(x_u − x̂)`.
- **Pass-through gradients** on the SAE so `∇_{x_u} m ← ∇_{x_d} m` is preserved for further upstream nodes.
- **Jacobian-vector product trick** to compute edge IE in two backward passes instead of `d_model` of them.

## Best Figure

![Figure 3 — Faithfulness and completeness scores for circuits (page 5)](figures/marks-2024-sparse-feature-circuits-fig.png)

Image Candidates:
- Figure 3 (p. 5): Side-by-side faithfulness and completeness curves on both Pythia-70M and Gemma-2-2B, comparing feature circuits (with and without SAE error nodes) against neuron circuits — the single-figure proof that the feature basis is two orders of magnitude more compact than the neuron basis at equivalent fidelity.
- Table 2 (p. 8): SHIFT vs CBP vs random vs feature-skyline vs neuron-skyline vs oracle on Bias-in-Bios for both models — the load-bearing application result, but smaller-impact visually.
- Figure 4 (p. 7): Side-by-side annotated circuit diagrams for Pythia and Gemma on subject-verb-agreement-across-RC — the "interpretability looks like this" view, beautiful but more about a single case study than the global claim.

Best Image:
- Figure Name: Figure 3: "Faithfulness and completeness scores for circuits, measured on held-out data"
- Figure Page: 5
- Slide Caption: Sparse feature circuits with ~100–500 nodes (blue/green) achieve comparable faithfulness to neuron circuits with ~1,500–50,000 nodes (purple) — two orders of magnitude more compact at equivalent fidelity, on both Pythia-70M (top) and Gemma-2-2B (bottom).
- Description: A 2×2 grid: rows are model (Pythia-70M top, Gemma-2-2B bottom) and columns are metric (faithfulness left — how much of the model's behavior the circuit explains, higher better; completeness right — how much remains in the complement, lower better). The x-axis is "Nodes" in the circuit, swept by varying the node threshold T_N. Four conditions per panel: full feature circuit (blue), feature circuit with all SAE error nodes removed (light green), feature circuit with attention+MLP SAE errors removed (dark green), and neuron circuit (purple). The blue curves climb fast and plateau early — for Pythia, ~100 features hit 50% faithfulness; for Gemma, ~500 features do. The purple curves climb slowly — Pythia needs ~1,500 neurons, Gemma needs ~50,000 (an entire layer's worth) to reach the same point. The completeness panels (right column) show the converse: ablating just a few nodes from the feature circuit kills the behavior, whereas neuron circuits need hundreds-to-thousands of ablations.

## What Experts Overlook

What this paper makes legible that practitioners working outside mechanistic-interpretability typically miss:

1. **"Circuits" is a verb, not a noun, and the verb's object is a metric.** A circuit only exists relative to a behavior-defining `m`. The same model has different circuits for "predict 'is' vs 'are'" vs "classify profession from bio" vs "predict the next number in a sequence." This is obvious once said, but most informal usage of "interpretability" treats the model as having a singular decomposable structure. The right framing is closer to "for any well-defined behavior on any distribution, we can extract the compiled subroutine the model uses for it."

2. **SAE errors are first-class circuit nodes, not noise.** The naive read is "SAEs reconstruct activations imperfectly; throw the error away." The authors' move is the opposite: keep `ε(x)` as an *explicit node* in the computation graph, and report when removing it tanks the circuit. This is methodologically more honest (the parts your SAEs can't explain are exactly the parts you should worry about) and *enables the faithfulness benchmark to actually compute* — without ε, removing nodes outside the circuit would also remove uncaptured behavior, conflating "circuit doesn't include it" with "SAE doesn't capture it." For memory systems, the analog: when you compile patterns from raw experiences, the unrecognized remainder is the most important thing to keep visible.

3. **Polysemanticity is what makes the coarse-vs-fine choice consequential, not "depth of analysis."** Outsiders sometimes frame circuits as "more granular = more accurate." The paper's point is sharper: neurons (fine-grained) are *more* polysemantic than the SAE features (also fine-grained), and that polysemanticity is what makes them uninterpretable. The neuron-circuit and feature-circuit experiments hold granularity constant — both operate at the per-token, per-dimension level — and isolate that interpretability comes from *monosemanticity*, which is a consequence of how the basis is chosen, not how many basis vectors you take.

4. **"SHIFT without retraining" already nearly matches the feature skyline.** Table 2 row "SHIFT" (Pythia: 88.5% / 54.0% / 76.0% on profession/gender/worst-group) compared to "Feature skyline" (88.5% / 54.3% / 62.9%) shows that *human judgement on max-activating exemplars is essentially as good as oracle access to balanced labels* for choosing what to ablate. This is the underplayed result: the interpretability tax is small. People who read "interpretability is hard" forget that the actual decisions humans make about what is and is not gender-related are highly reliable when the features are monosemantic.

5. **The neuron-skyline failure is the failure mode of "edit the model's parameters directly."** Even with oracle access to which neurons are most implicated in gender prediction on balanced data, ablating neurons fails (Pythia: 75.5% / 73.2% / 41.5%) — because neurons useful for gender are also useful for profession. There is no neuron-basis edit that cleanly separates the two; the basis itself is wrong. This generalizes: if your memory architecture's editing units don't match the model's actual abstractions, surgical edits become destructive. Use the model's own abstractions.

6. **Cluster + circuit is two separate noisy pipelines composed.** Section 5's "thousands of behaviors" is impressive but the paper is unusually candid about it: "evaluating these clusters and circuits is an important open problem." The clustering identifies *putative* behaviors; the circuit discovery yields *putative* mechanisms. Both have failure modes (clusters that are actually a union of mechanisms — the "to" example in Figure 5 is two distinct mechanisms collapsed into one cluster). The scale is a proof of concept, not a finished evaluation.

7. **Annotation pool bias.** The interpretability ratings (Table 7) used annotators from the ARENA Slack — ML researchers interested in alignment. The authors acknowledge this would not generalize to truly random annotators. Important caveat for anyone counting on "humans can label features": the population matters a lot, and the result is consistent with a high ceiling rather than a universal floor.

8. **"Faithfulness > 0.2" is a low bar by design, not by accident.** The case-study circuits (86 Pythia nodes, 223 Gemma nodes) target only ~21% faithfulness because beyond that the number of nodes is too large to annotate by hand. There is a tension here the paper acknowledges but doesn't resolve: small circuits are interpretable but capture a fraction of behavior; large circuits capture most behavior but cease to be interpretable. The chosen working points (annotation circuits vs. SHIFT-suitable circuits) are different.

## Extracted Prompts

This paper does not contain user-facing LLM prompts, but it contains several *operational specifications* worth extracting as templates for any system doing circuit-level analysis or memory-feature editing:

**Template 1 — Feature interpretation prompt for human annotators (Appendix F, Fig. 23–24).** Show: (a) top-activating tokens for the feature, (b) tokens whose output probabilities were most affected when ablating the feature, (c) ~10 example contexts with feature activations colored by intensity (darker blue = stronger). Ask for: (i) a textual description of what the feature represents, (ii) a 0–100 interpretability rating, (iii) a 0–100 semantic complexity rating. Known failure mode the authors flag: annotators over-label features by *semantic* groupings ("text about politics") and under-attend to *syntactic* context ("plural nouns").

**Template 2 — Concept Bottleneck Probe keyword list (App. E.2), used as a baseline.** For Bias-in-Bios profession classification (nurse vs. professor): nurse, healthcare, hospital, patient, medical, clinic, triage, medication, emergency, surgery, professor, academia, research, university, tenure, faculty, dissertation, sabbatical, publication, grant. Pattern worth copying: 20 keywords, ~10 per intended class, used to extract concept vectors as the LM's penultimate-layer representation of the final token (with mean-vector subtraction to avoid high pairwise cosine similarity).

**Template 3 — Causal contrastive pair template for subject-verb agreement (Table 1).** Four structural variants:
- Simple: "The parents" → m = p(is) − p(are)
- Within RC: "The athlete that the managers" → m = p(likes) − p(like)
- Across RC: "The athlete that the managers like" → m = p(do) − p(does)
- Across PP: "The secretaries near the cars" → m = p(has) − p(have)

The general form is: minimal pair where the only difference is grammatical number of the head noun, and the metric is the log-odds difference between the two verb inflections.

**Template 4 — Behavior cluster naming/labeling convention.** When you discover a behavior cluster via the unsupervised pipeline, label features by what they activate on AND what they cause: e.g., "Succession" (activates on numbered sequences, promotes the next number), "Narrow induction A3...A→3 or III or 4..." (activates on a specific repetition pattern, promotes its continuation). The two-part naming (input activation + output effect) is what makes features composable across circuits.

## Citations

(Full bibliography in frontmatter — 86 entries. Top 10 with highest downstream relevance for the memory-architect lens):

- **Cunningham et al. 2024** — "Sparse autoencoders find highly interpretable features in language models" (ICLR 2024). The foundational SAE-for-LM-interpretability paper that this work directly builds on.
- **Bricken et al. 2023** — "Towards monosemanticity: Decomposing language models with dictionary learning" (Anthropic, Transformer Circuits Thread). The companion foundational SAE work; the architecture the Pythia SAEs follow.
- **Lieberum et al. 2024** — "Gemma scope: Open sparse autoencoders everywhere all at once on gemma 2." The SAE suite used for all Gemma experiments; available publicly.
- **Olsson et al. 2022** — "In-context learning and induction heads." The canonical example of attention-head-level mechanistic interpretability that this paper improves on at finer grain.
- **Conmy et al. 2023** — "Towards automated circuit discovery for mechanistic interpretability." The prior automated-circuit-discovery method, operating on coarse components.
- **Nanda 2022** — "Attribution patching: Activation patching at industrial scale" (blog). The linear-approximation technique central to this paper's scalability story.
- **Syed, Rager, Conmy 2023** — "Attribution patching outperforms automated circuit discovery." The paper showing attribution patching is fast enough to displace explicit patching at scale.
- **Sundararajan, Taly, Yan 2017** — "Axiomatic attribution for deep networks." The integrated-gradients foundational paper, used here for early-layer corrections to attribution patching.
- **Michaud et al. 2023** — "The quantization model of neural scaling." The clustering-of-gradients method that powers the unsupervised behavior-discovery pipeline in §5.
- **De-Arteaga et al. 2019** — "Bias in bios: A case study of semantic representation bias in a high-stakes setting." The dataset used for the SHIFT debiasing experiment.

## Related Digests

- [[mao-2026-agent-memory-circuits]] — Mao et al. directly build on this paper's methodology, applying sparse-feature-circuit analysis to *agent memory systems* (mem0, A-MEM) rather than syntactic agreement or classifier debiasing. They use SAE features as the unit of mechanistic analysis to ask "what does the LLM grow inside itself when it learns to route memories?" — and find Write/Read converge on a late-layer "context-grounding hub" that already exists in the base model. The direct genealogical link: Marks et al. is the methodological substrate; Mao et al. is the agent-memory application.

## Reviewer Notes

Hallucination check (against the paper text in `/tmp/digest-paper/marks-2024-sparse-feature-circuits/paper.txt`):

- **TLDR numbers** ("~100 features for Pythia, ~500 for Gemma" vs "~1,500 / ~50,000 neurons"): Cross-checked against paper §3.2: "the majority of performance in Pythia-70M, resp. Gemma-2-2B is explained by only 100, resp. 500 nodes. In contrast, around 1500, resp. 50000 neurons are required to explain half the performance." **Exact match. Clean.**
- **SHIFT Bias-in-Bios numbers** (24.4% → 89.0% Pythia worst-group; 18.2% → 92.9% Gemma worst-group): Cross-checked against Table 2. Original Pythia worst-group = 24.4; SHIFT+retrain Pythia worst-group = 89.0. Original Gemma worst-group = 18.2; SHIFT+retrain Gemma worst-group = 92.9. **Exact match. Clean.**
- **Feature counts judged irrelevant** ("55 of 67 Pythia features, 43 of 46 Gemma features"): Cross-checked §4: "We judge 55 of the Pythia features and 43 of the Gemma features to be task-irrelevant." **Exact match. Clean.**
- **SAE config** ("ReLU SAEs for Pythia-70M with d_SAE = 64×d, JumpReLU for Gemma-2-2B with d_SAE = 8×d"): Cross-checked §2 and App. B.1/B.2. Pythia: "ReLU-linear encoder fᵢ and sparse dimension d_SAE = 64 × d." Gemma Scope: "Jump-ReLU-linear encoder and d_SAE = 8 × d." **Exact match. Clean.**
- **Case-study circuit sizes** ("86 Pythia nodes, 223 Gemma nodes for RC agreement, both at faithfulness 0.21"): Cross-checked §3.3: "For Pythia, this results in a circuit with 86 nodes and faithfulness 0.21; for Gemma we study a circuit with 223 nodes and faithfulness 0.21." **Exact match. Clean.**
- **Annotation pool ("ARENA Slack — ML researchers interested in AI alignment and safety")**: Cross-checked App. F: "Crowdworkers were recruited from the ARENA Slack channel, whose members are machine learning researchers interested in AI alignment and safety." **Exact match. Clean.**
- **Public artifact URL** (`feature-circuits.xyz`): Mentioned twice in the paper (§1, §5). **Clean.**
- **GitHub URL** (`github.com/saprmarks/feature-circuits`): Mentioned §1. **Clean.**
- **Author institutional affiliations** (Marks/Bau/Mueller at Northeastern, Michaud at MIT, Belinkov at Technion, Rager independent): Cross-checked header. **Exact match. Clean.**
- **ICLR 2025 venue**: Header says "Published as a conference paper at ICLR 2025." **Clean.** (Note: the arxiv ID 2403.19647 was first posted March 2024; the ICLR 2025 publication date is reported under `publication_date: "2024-03"` for the first version, with `venue: "ICLR 2025"`. This matches standard digest conventions.)

**Overall severity: Clean.** No fabricated numbers, no manufactured connections, no overreach beyond what the paper claims. The implications section is the most interpretive piece, but it is explicitly tagged as the digester's mapping into ENGRAM, not as claims of the original paper. One thing worth flagging for the reader, not a hallucination: the paper's authors are careful not to claim SHIFT is a universal debiasing solution — they emphasize it requires SAEs to exist and that "model components not captured by the SAEs will remain uninterpretable." The digest's enthusiasm for the editable-memory framing should be balanced against that caveat.
