---
corpus: agentic-memory
kind: paper-digest
slug: fernando-2023-promptbreeder
title: "Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution"
authors:
  - "Fernando, Chrisantha"
  - "Banarse, Dylan"
  - "Michalewski, Henryk"
  - "Osindero, Simon"
  - "Rocktäschel, Tim"
year: 2023
publication_date: "2023-09"
venue: "arXiv preprint (cs.CL)"
source_url: "https://arxiv.org/abs/2309.16797"
doi: null
arxiv_id: "2309.16797"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Promptbreeder turns the prompt itself into the unit of memory by evolving it — a population of (task-prompt, mutation-prompt) pairs where the LLM is both the mutation operator AND the thing being prompted, and where the operator-prompts mutate themselves (self-referential hyper-mutation); this lifts GSM8K from 80.2% (OPRO) to 83.9% on PaLM 2-L with the unintuitively simple zero-shot prompt SOLUTION\""
topics:
  - prompt-evolution
  - self-referential-systems
  - evolutionary-computation
  - prompt-optimization
  - memory-as-prompt
  - hyper-mutation
  - meta-learning
  - chain-of-thought
tags:
  - paper
  - llm
  - evolutionary-algorithms
  - palm-2
  - benchmark
  - automatic-prompt-engineering
entities:
  - fernando-chrisantha
  - banarse-dylan
  - michalewski-henryk
  - osindero-simon
  - rocktaschel-tim
  - google-deepmind
related_digests: []
citations:
  - title: "PaLM 2 Technical Report"
    authors: ["Anil, R.", "Dai, A. M.", "et al."]
    year: 2023
    doi: null
    url: "https://arxiv.org/abs/2305.10403"
    arxiv_id: "2305.10403"
  - title: "Graph of thoughts: Solving elaborate problems with large language models"
    authors: ["Besta, M.", "Blach, N.", "et al."]
    year: 2023
    doi: "10.48550/arXiv.2308.09687"
    url: "https://doi.org/10.48550/arXiv.2308.09687"
    arxiv_id: "2308.09687"
  - title: "Language models are few-shot learners"
    authors: ["Brown, T. B.", "Mann, B.", "et al."]
    year: 2020
    doi: null
    url: "https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html"
    arxiv_id: "2005.14165"
  - title: "EvoPrompting: Language models for code-level neural architecture search"
    authors: ["Chen, A.", "Dohan, D. M.", "So, D. R."]
    year: 2023
    doi: "10.48550/arXiv.2302.14838"
    url: "https://doi.org/10.48550/arXiv.2302.14838"
    arxiv_id: "2302.14838"
  - title: "Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks"
    authors: ["Chen, W.", "Ma, X.", "Wang, X.", "Cohen, W. W."]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2211.12588"
  - title: "Training verifiers to solve math word problems"
    authors: ["Cobbe, K.", "Kosaraju, V.", "et al."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2110.14168"
    arxiv_id: "2110.14168"
  - title: "The evolution of evolvability"
    authors: ["Dawkins, R."]
    year: 2003
    doi: "10.1016/B978-012428765-5/50046-3"
    url: null
    arxiv_id: null
  - title: "BERT: pre-training of deep bidirectional transformers for language understanding"
    authors: ["Devlin, J.", "Chang, M.-W.", "Lee, K.", "Toutanova, K."]
    year: 2019
    doi: "10.18653/v1/n19-1423"
    url: "https://doi.org/10.18653/v1/n19-1423"
    arxiv_id: "1810.04805"
  - title: "Evolvability ES: scalable and direct optimization of evolvability"
    authors: ["Gajewski, A.", "Clune, J.", "Stanley, K. O.", "Lehman, J."]
    year: 2019
    doi: "10.1145/3321707.3321876"
    url: "https://doi.org/10.1145/3321707.3321876"
    arxiv_id: null
  - title: "Did Aristotle use a laptop? A question answering benchmark with implicit reasoning strategies (StrategyQA)"
    authors: ["Geva, M.", "Khashabi, D.", "Segal, E.", "Khot, T.", "Roth, D.", "Berant, J."]
    year: 2021
    doi: "10.1162/tacl_a_00370"
    url: "https://doi.org/10.1162/tacl_a_00370"
    arxiv_id: null
  - title: "Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers (EvoPrompt)"
    authors: ["Guo, Q.", "Wang, R.", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: "2309.08532"
  - title: "The microbial genetic algorithm"
    authors: ["Harvey, I."]
    year: 2011
    doi: null
    url: null
    arxiv_id: null
  - title: "An introduction and survey of estimation of distribution algorithms"
    authors: ["Hauschild, M.", "Pelikan, M."]
    year: 2011
    doi: null
    url: null
    arxiv_id: null
  - title: "Instruction induction: From few examples to natural language task descriptions"
    authors: ["Honovich, O.", "Shaham, U.", "Bowman, S. R.", "Levy, O."]
    year: 2023
    doi: "10.18653/v1/2023.acl-long.108"
    url: "https://doi.org/10.18653/v1/2023.acl-long.108"
    arxiv_id: null
  - title: "Learning to solve arithmetic word problems with verb categorization (AddSub)"
    authors: ["Hosseini, M. J.", "Hajishirzi, H.", "Etzioni, O.", "Kushman, N."]
    year: 2014
    doi: "10.3115/v1/D14-1058"
    url: "https://aclanthology.org/D14-1058"
    arxiv_id: null
  - title: "Distilling step-by-step! Outperforming larger language models with less training data and smaller model sizes"
    authors: ["Hsieh, C.-Y.", "et al."]
    year: 2023
    doi: "10.18653/v1/2023.findings-acl.507"
    url: "https://doi.org/10.18653/v1/2023.findings-acl.507"
    arxiv_id: null
  - title: "Large language models can self-improve"
    authors: ["Huang, J.", "Gu, S. S.", "et al."]
    year: 2022
    doi: "10.48550/arXiv.2210.11610"
    url: "https://doi.org/10.48550/arXiv.2210.11610"
    arxiv_id: "2210.11610"
  - title: "A modern self-referential weight matrix that learns to modify itself"
    authors: ["Irie, K.", "Schlag, I.", "Csordás, R.", "Schmidhuber, J."]
    year: 2022
    doi: null
    url: "https://proceedings.mlr.press/v162/irie22b.html"
    arxiv_id: null
  - title: "Population based training of neural networks"
    authors: ["Jaderberg, M.", "Dalibard, V.", "et al."]
    year: 2017
    doi: null
    url: "http://arxiv.org/abs/1711.09846"
    arxiv_id: "1711.09846"
  - title: "Reinforcement learning with unsupervised auxiliary tasks"
    authors: ["Jaderberg, M.", "Mnih, V.", "et al."]
    year: 2017
    doi: null
    url: "https://openreview.net/forum?id=SJ6yPD5xg"
    arxiv_id: null
  - title: "Replay-guided adversarial environment design"
    authors: ["Jiang, M.", "Dennis, M.", "Parker-Holder, J.", "Foerster, J. N.", "Grefenstette, E.", "Rocktäschel, T."]
    year: 2021
    doi: null
    url: null
    arxiv_id: null
  - title: "Prioritized level replay"
    authors: ["Jiang, M.", "Grefenstette, E.", "Rocktäschel, T."]
    year: 2021
    doi: null
    url: "http://proceedings.mlr.press/v139/jiang21b.html"
    arxiv_id: null
  - title: "General intelligence requires rethinking exploration"
    authors: ["Jiang, M.", "Rocktäschel, T.", "Grefenstette, E."]
    year: 2022
    doi: "10.48550/arXiv.2211.07819"
    url: "https://doi.org/10.48550/arXiv.2211.07819"
    arxiv_id: "2211.07819"
  - title: "Eliminating meta optimization through self-referential meta learning"
    authors: ["Kirsch, L.", "Schmidhuber, J."]
    year: 2022
    doi: "10.48550/arXiv.2212.14392"
    url: "https://doi.org/10.48550/arXiv.2212.14392"
    arxiv_id: "2212.14392"
  - title: "Large language models are zero-shot reasoners"
    authors: ["Kojima, T.", "Gu, S. S.", "Reid, M.", "Matsuo, Y.", "Iwasawa, Y."]
    year: 2022
    doi: null
    url: "http://papers.nips.cc/paper_files/paper/2022/hash/8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html"
    arxiv_id: "2205.11916"
  - title: "Parsing algebraic word problems into equations (SingleEq)"
    authors: ["Koncel-Kedziorski, R.", "Hajishirzi, H.", "Sabharwal, A.", "Etzioni, O.", "Dumas Ang, S."]
    year: 2015
    doi: "10.1162/tacl_a_00160"
    url: "https://aclanthology.org/Q15-1042"
    arxiv_id: null
  - title: "Evolving a diversity of virtual creatures through novelty search and local competition"
    authors: ["Lehman, J.", "Stanley, K. O."]
    year: 2011
    doi: "10.1145/2001576.2001606"
    url: "https://doi.org/10.1145/2001576.2001606"
    arxiv_id: null
  - title: "Abandoning Objectives: Evolution Through the Search for Novelty Alone"
    authors: ["Lehman, J.", "Stanley, K. O."]
    year: 2011
    doi: "10.1162/EVCO_a_00025"
    url: null
    arxiv_id: null
  - title: "Evolution through large models (ELM)"
    authors: ["Lehman, J.", "Gordon, J.", "Jain, S.", "Ndousse, K.", "Yeh, C.", "Stanley, K. O."]
    year: 2022
    doi: "10.48550/arXiv.2206.08896"
    url: "https://doi.org/10.48550/arXiv.2206.08896"
    arxiv_id: "2206.08896"
  - title: "The power of scale for parameter-efficient prompt tuning"
    authors: ["Lester, B.", "Al-Rfou, R.", "Constant, N."]
    year: 2021
    doi: "10.18653/v1/2021.emnlp-main.243"
    url: "https://doi.org/10.18653/v1/2021.emnlp-main.243"
    arxiv_id: "2104.08691"
  - title: "Program induction by rationale generation: Learning to solve and explain algebraic word problems (AQuA-RAT)"
    authors: ["Ling, W.", "Yogatama, D.", "Dyer, C.", "Blunsom, P."]
    year: 2017
    doi: "10.18653/v1/P17-1015"
    url: "https://aclanthology.org/P17-1015"
    arxiv_id: null
  - title: "Lost in the middle: How language models use long contexts"
    authors: ["Liu, N. F.", "Lin, K.", "Hewitt, J.", "et al."]
    year: 2023
    doi: "10.48550/arXiv.2307.03172"
    url: "https://doi.org/10.48550/arXiv.2307.03172"
    arxiv_id: "2307.03172"
  - title: "GPT understands, too"
    authors: ["Liu, X.", "Zheng, Y.", "et al."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2103.10385"
    arxiv_id: "2103.10385"
  - title: "Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity"
    authors: ["Lu, Y.", "Bartolo, M.", "Moore, A.", "Riedel, S.", "Stenetorp, P."]
    year: 2022
    doi: "10.18653/v1/2022.acl-long.556"
    url: "https://doi.org/10.18653/v1/2022.acl-long.556"
    arxiv_id: null
  - title: "Text and patterns: For effective chain of thought, it takes two to tango"
    authors: ["Madaan, A.", "Yazdanbakhsh, A."]
    year: 2022
    doi: "10.48550/arXiv.2209.07686"
    url: "https://doi.org/10.48550/arXiv.2209.07686"
    arxiv_id: "2209.07686"
  - title: "Self-Refine: Iterative refinement with self-feedback"
    authors: ["Madaan, A.", "Tandon, N.", "et al."]
    year: 2023
    doi: "10.48550/arXiv.2303.17651"
    url: "https://doi.org/10.48550/arXiv.2303.17651"
    arxiv_id: "2303.17651"
  - title: "Language model crossover: Variation through few-shot prompting"
    authors: ["Meyerson, E.", "Nelson, M. J.", "Bradley, H.", "Moradi, A.", "Hoover, A. K.", "Lehman, J."]
    year: 2023
    doi: "10.48550/arXiv.2302.12170"
    url: "https://doi.org/10.48550/arXiv.2302.12170"
    arxiv_id: "2302.12170"
  - title: "Large language models as general pattern machines"
    authors: ["Mirchandani, S.", "Xia, F.", "Florence, P.", "Ichter, B.", "et al."]
    year: 2023
    doi: "10.48550/arXiv.2307.04721"
    url: "https://doi.org/10.48550/arXiv.2307.04721"
    arxiv_id: "2307.04721"
  - title: "ETHOS: a multi-label hate speech detection dataset"
    authors: ["Mollas, I.", "Chrysopoulou, Z.", "Karlos, S.", "Tsoumakas, G."]
    year: 2022
    doi: "10.1007/s40747-021-00608-2"
    url: "https://doi.org/10.1007%2Fs40747-021-00608-2"
    arxiv_id: null
  - title: "Evaluating the robustness of neural language models to input perturbations"
    authors: ["Moradi, M.", "Samwald, M."]
    year: 2021
    doi: "10.18653/v1/2021.emnlp-main.117"
    url: "https://doi.org/10.18653/v1/2021.emnlp-main.117"
    arxiv_id: null
  - title: "Illuminating search spaces by mapping elites (MAP-Elites)"
    authors: ["Mouret, J.-B.", "Clune, J."]
    year: 2015
    doi: null
    url: "http://arxiv.org/abs/1504.04909"
    arxiv_id: "1504.04909"
  - title: "Show your work: Scratchpads for intermediate computation with language models"
    authors: ["Nye, M. I.", "Andreassen, A. J.", "et al."]
    year: 2021
    doi: null
    url: "https://arxiv.org/abs/2112.00114"
    arxiv_id: "2112.00114"
  - title: "Psychological research on insight problem solving"
    authors: ["Öllinger, M.", "Knoblich, G."]
    year: 2009
    doi: null
    url: null
    arxiv_id: null
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["Park, J. S.", "O'Brien, J. C.", "Cai, C. J.", "Morris, M. R.", "Liang, P.", "Bernstein, M. S."]
    year: 2023
    doi: "10.48550/arXiv.2304.03442"
    url: "https://doi.org/10.48550/arXiv.2304.03442"
    arxiv_id: "2304.03442"
  - title: "Evolving curricula with regret-based environment design (ACCEL)"
    authors: ["Parker-Holder, J.", "Jiang, M.", "Dennis, M.", "et al."]
    year: 2022
    doi: null
    url: "https://proceedings.mlr.press/v162/parker-holder22a.html"
    arxiv_id: null
  - title: "Are NLP models really able to solve simple math word problems? (SVAMP)"
    authors: ["Patel, A.", "Bhattamishra, S.", "Goyal, N."]
    year: 2021
    doi: "10.18653/v1/2021.naacl-main.168"
    url: "https://doi.org/10.18653/v1/2021.naacl-main.168"
    arxiv_id: null
  - title: "The causes of evolvability and their evolution"
    authors: ["Payne, J. L.", "Wagner, A."]
    year: 2019
    doi: "10.1038/s41576-018-0069-z"
    url: null
    arxiv_id: null
  - title: "Is evolvability evolvable?"
    authors: ["Pigliucci, M."]
    year: 2008
    doi: "10.1038/nrg2278"
    url: null
    arxiv_id: null
  - title: "Automatic Prompt Optimization with Gradient Descent and Beam Search (APO)"
    authors: ["Pryzant, R.", "Iter, D.", "Li, J.", "Lee, Y. T.", "Zhu, C.", "Zeng, M."]
    year: 2023
    doi: null
    url: null
    arxiv_id: "2305.03495"
  - title: "Learning How to Ask: Querying LMs with Mixtures of Soft Prompts"
    authors: ["Qin, G.", "Eisner, J."]
    year: 2021
    doi: null
    url: null
    arxiv_id: "2104.06599"
  - title: "Solving general arithmetic word problems (MultiArith)"
    authors: ["Roy, S.", "Roth, D."]
    year: 2016
    doi: null
    url: null
    arxiv_id: "1608.01413"
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    authors: ["Schick, T.", "Dwivedi-Yu, J.", "Dessì, R.", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: "2302.04761"
  - title: "A Self-Referential Weight Matrix"
    authors: ["Schmidhuber, J."]
    year: 1993
    doi: "10.1007/978-1-4471-2063-6_107"
    url: null
    arxiv_id: null
  - title: "Making the world differentiable: On using fully recurrent self-supervised neural networks for dynamic reinforcement learning and planning in non-stationary environments"
    authors: ["Schmidhuber, J."]
    year: 1990
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning to Control Fast-Weight Memories"
    authors: ["Schmidhuber, J."]
    year: 1992
    doi: "10.1162/neco.1992.4.1.131"
    url: null
    arxiv_id: null
  - title: "Gödel machines: self-referential universal problem solvers"
    authors: ["Schmidhuber, J."]
    year: 2003
    doi: null
    url: null
    arxiv_id: "cs/0309048"
  - title: "Picbreeder: Evolving pictures collaboratively online"
    authors: ["Secretan, J.", "Beato, N.", "D'Ambrosio, D. B.", "Rodriguez, A.", "Campbell, A.", "Stanley, K. O."]
    year: 2008
    doi: "10.1145/1357054.1357328"
    url: null
    arxiv_id: null
  - title: "Niching in evolution strategies"
    authors: ["Shir, O. M.", "Bäck, T."]
    year: 2005
    doi: null
    url: null
    arxiv_id: null
  - title: "Automatic prompt augmentation and selection with chain-of-thought from labeled data (Automatic-CoT)"
    authors: ["Shum, K.", "Diao, S.", "Zhang, T."]
    year: 2023
    doi: "10.48550/arXiv.2302.12822"
    url: "https://doi.org/10.48550/arXiv.2302.12822"
    arxiv_id: "2302.12822"
  - title: "CommonsenseQA: A question answering challenge targeting commonsense knowledge"
    authors: ["Talmor, A.", "Herzig, J.", "Lourie, N.", "Berant, J."]
    year: 2019
    doi: "10.18653/v1/N19-1421"
    url: "https://aclanthology.org/N19-1421"
    arxiv_id: null
  - title: "Voyager: An open-ended embodied agent with large language models"
    authors: ["Wang, G.", "Xie, Y.", "et al."]
    year: 2023
    doi: "10.48550/arXiv.2305.16291"
    url: "https://doi.org/10.48550/arXiv.2305.16291"
    arxiv_id: "2305.16291"
  - title: "Plan-and-Solve prompting: Improving zero-shot chain-of-thought reasoning by large language models"
    authors: ["Wang, L.", "Xu, W.", "Lan, Y.", "et al."]
    year: 2023
    doi: "10.18653/v1/2023.acl-long.147"
    url: "https://doi.org/10.18653/v1/2023.acl-long.147"
    arxiv_id: "2305.04091"
  - title: "Self-consistency improves chain of thought reasoning in language models"
    authors: ["Wang, X.", "Wei, J.", "Schuurmans, D.", "Le, Q.", "Chi, E.", "Narang, S.", "Chowdhery, A.", "Zhou, D."]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2203.11171"
  - title: "Self-instruct: Aligning language models with self-generated instructions"
    authors: ["Wang, Y.", "Kordi, Y.", "et al."]
    year: 2023
    doi: "10.18653/v1/2023.acl-long.754"
    url: "https://doi.org/10.18653/v1/2023.acl-long.754"
    arxiv_id: null
  - title: "Describe, explain, plan and select: Interactive planning with large language models enables open-world multi-task agents"
    authors: ["Wang, Z.", "Cai, S.", "Liu, A.", "Ma, X.", "Liang, Y."]
    year: 2023
    doi: "10.48550/arXiv.2302.01560"
    url: "https://doi.org/10.48550/arXiv.2302.01560"
    arxiv_id: "2302.01560"
  - title: "Chain-of-thought prompting elicits reasoning in large language models"
    authors: ["Wei, J.", "Wang, X.", "Schuurmans, D.", "Bosma, M.", "Ichter, B.", "Xia, F.", "Chi, E. H.", "Le, Q. V.", "Zhou, D."]
    year: 2022
    doi: null
    url: "http://papers.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html"
    arxiv_id: "2201.11903"
  - title: "SPRING: GPT-4 out-performs RL algorithms by studying papers and reasoning"
    authors: ["Wu, Y.", "Prabhumoye, S.", "Min, S. Y.", "et al."]
    year: 2023
    doi: "10.48550/arXiv.2305.15486"
    url: "https://doi.org/10.48550/arXiv.2305.15486"
    arxiv_id: "2305.15486"
  - title: "Large language models as optimizers (OPRO)"
    authors: ["Yang, C.", "Wang, X.", "Lu, Y.", "Liu, H.", "Le, Q. V.", "Zhou, D.", "Chen, X."]
    year: 2023
    doi: "10.48550/arXiv.2309.03409"
    url: "https://doi.org/10.48550/arXiv.2309.03409"
    arxiv_id: "2309.03409"
  - title: "MM-React: Prompting ChatGPT for multimodal reasoning and action"
    authors: ["Yang, Z.", "Li, L.", "et al."]
    year: 2023
    doi: null
    url: null
    arxiv_id: "2303.11381"
  - title: "ReAct: Synergizing reasoning and acting in language models"
    authors: ["Yao, S.", "Zhao, J.", "Yu, D.", "Du, N.", "Shafran, I.", "Narasimhan, K.", "Cao, Y."]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2210.03629"
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    authors: ["Yao, S.", "Yu, D.", "Zhao, J.", "Shafran, I.", "Griffiths, T. L.", "Cao, Y.", "Narasimhan, K."]
    year: 2023
    doi: null
    url: null
    arxiv_id: "2305.10601"
  - title: "STaR: Bootstrapping reasoning with reasoning"
    authors: ["Zelikman, E.", "Wu, Y.", "Mu, J.", "Goodman, N. D."]
    year: 2022
    doi: null
    url: "http://papers.nips.cc/paper_files/paper/2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.html"
    arxiv_id: "2203.14465"
  - title: "OMNI: open-endedness via models of human notions of interestingness"
    authors: ["Zhang, J.", "Lehman, J.", "Stanley, K. O.", "Clune, J."]
    year: 2023
    doi: "10.48550/arXiv.2306.01711"
    url: "https://doi.org/10.48550/arXiv.2306.01711"
    arxiv_id: "2306.01711"
  - title: "Automatic chain of thought prompting in large language models (Auto-CoT)"
    authors: ["Zhang, Z.", "Zhang, A.", "Li, M.", "Smola, A."]
    year: 2023
    doi: null
    url: "https://openreview.net/pdf?id=5NTt8GFjUHkr"
    arxiv_id: null
  - title: "Least-to-most prompting enables complex reasoning in large language models"
    authors: ["Zhou, D.", "Schärli, N.", "Hou, L.", "Wei, J.", "Scales, N.", "Wang, X.", "Schuurmans, D.", "Cui, C.", "Bousquet, O.", "Le, Q.", "et al."]
    year: 2022
    doi: null
    url: null
    arxiv_id: "2205.10625"
  - title: "Large language models are human-level prompt engineers (APE)"
    authors: ["Zhou, Y.", "Muresanu, A. I.", "Han, Z.", "Paster, K.", "Pitis, S.", "Chan, H.", "Ba, J."]
    year: 2023
    doi: null
    url: "https://openreview.net/pdf?id=92gvk82DE-"
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Overview of Promptbreeder — population of (task-prompt, mutation-prompt) units evolved by an LLM mutation operator"
  page: 3
  image_path: "figures/fernando-2023-promptbreeder-fig.png"
---

# Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution

**Authors:** Fernando, Chrisantha; Banarse, Dylan; Michalewski, Henryk; Osindero, Simon; Rocktäschel, Tim
**Published:** 2023-09 · [Source](https://arxiv.org/abs/2309.16797)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Promptbreeder (PB) is a gradient-free, "general-purpose self-referential self-improvement mechanism that evolves and adapts prompts for a given domain." Driven entirely by an LLM (PaLM 2-L), it runs a binary-tournament genetic algorithm over a population of 50 units, each consisting of two task-prompts plus a mutation-prompt. Crucially, the same LLM serves as the mutation operator: a mutated task-prompt is `P' = LLM(M + P)`, and a mutated mutation-prompt is `M' = LLM(H + M)` — so the system not only improves prompts, it improves the way it improves prompts (self-referential hyper-mutation). Nine mutation operators across five classes (Direct, EDA, Hyper, Lamarckian, Crossover/Context-Shuffle) provide a diverse search; "thinking-style" seeds (e.g. "Let's think step by step", "Use Reflective Thinking") seed the initial population. After 20–30 generations (1–2k fitness evaluations on random 100-sample training batches), PB beats Chain-of-Thought, Plan-and-Solve, APE and OPRO on a panel of arithmetic + commonsense benchmarks using PaLM 2-L: notably **GSM8K 83.9% zero-shot (vs OPRO 80.2%)**, **MultiArith 99.7%**, **SVAMP 90.2%**, **CSQA 85.4%**, **AQuA-RAT 62.2%**. On ETHOS hate-speech classification PB evolves a 2-stage long prompt scoring **89% vs 80%** for the hand-designed baseline. The best evolved GSM8K zero-shot prompt is the deceptively trivial `"SOLUTION""` — strong evidence that prompt space contains discoverable local optima that humans neither write nor recognise as good. The whole substrate of self-improvement is natural language; no model parameters are updated, making the approach LLM-API friendly and (the authors argue) likely to scale with model size.

## Key Takeaway

**[ENGRAM: E + A + M, with cross-dim interaction into G]** Promptbreeder turns the prompt itself into the unit of memory by evolving it — a population of (task-prompt, mutation-prompt) pairs where the LLM is both the mutation operator AND the thing being prompted, and where the operator-prompts mutate themselves (self-referential hyper-mutation); this lifts GSM8K from 80.2% (OPRO) to 83.9% on PaLM 2-L with the unintuitively simple zero-shot prompt `SOLUTION""`. The architectural insight worth stealing for a memory system: **the prompt is the smallest unit of compiled memory the LLM can read, and a population of prompts subject to evolutionary pressure with the LLM-as-mutator is a viable Aggregate (consolidation) primitive that requires no fine-tuning, no embeddings, no graph DB — only an evaluator and a fitness function.** The corollary is harder: PB succeeds *because* it has a clean fitness signal (100-example accuracy on a held-out batch). For memory systems whose "fitness" is user-satisfaction or downstream task quality (much noisier), the analogue is to replace the LLM-as-judge fitness with cheap proxy signals (e.g. citation count, retrieval success rate, contradiction-detection score) — and accept that without a fitness signal the whole evolutionary loop degenerates into LLM-summarising-its-own-summaries drift, which Section F explicitly warns about ("derailment" and "attractor" pathologies at low temperature).

## Implications

**For the ENGRAM Aggregate (A) dimension — patterns extracted from experiences.**

Promptbreeder is the strongest demonstration so far that the **prompt is a legitimate compiled-memory primitive**, not just an interface artefact. Three concrete implications for memory architects:

1. **Replace hand-written extraction prompts with an evolving population.** Today, every memory system has 5–30 hand-tuned extraction/synthesis prompts (e.g. "extract entities from this transcript", "summarise this session"). PB suggests these are sub-optimal and that an offline evolutionary loop with a small fitness function (e.g. "F1 on held-out human-labelled extractions", or "QMD retrieval@5 on a question bank") could produce strictly better prompts — and would compound across model upgrades because the evolution can be re-run cheaply when a new LLM ships. **[ENGRAM: A + E]** This shifts write-time synthesis cost: more compute upfront (evolution), less per-write (small fast prompt).

2. **Self-referential operator-prompts have measurable lift.** PB's hyper-mutation ablation (Appendix L) shows that removing the mutation-prompt-mutation step is harmful on 7/8 datasets — Zero-order Hyper-Mutation produces improving offspring **42%** of the time, the single most-effective operator. **[ENGRAM: M]** Translated: it is not enough for a memory system to "learn what to remember" (write-time policy); it must also "learn how it decides what to remember" — the meta-policy. Today's systems have static maintenance heuristics. PB is the existence proof that the meta-policy is also evolvable in natural language with no parameter updates.

3. **The "evolved best prompt" finding is a falsification of the introspective-readability hypothesis.** The best GSM8K zero-shot prompt is `"SOLUTION""` (a single word + stray quote), and the best SingleEq prompt is a Buddha quote ("Do not believe in anything simply because..."). These prompts are **useful but not legible** — they trigger reliable behaviour without a human-readable rationale. **[ENGRAM: G — Trust/Ground problem]** This is a sharp warning for any memory-architect betting on "human-auditable memory": the most-effective compiled memories may be operationally opaque. Provenance + verifiability needs to be evaluated against *behavioural* outcomes, not surface readability.

**For the Encode (E) dimension.**

PB's "thinking-styles" set (39 entries — Appendix D) is a high-quality starter library of write-time framings ("Critical Thinking", "Reflective Thinking", "Systems Thinking", "How could I devise an experiment to help solve this problem?"). These are reusable across any extraction or consolidation step; they read like a curated mental-model toolkit. **Steal-and-ship: lift Appendix D into the extraction-prompt seed pool.**

**For the Retrieve (R) dimension.**

PB itself contributes nothing to retrieval. It is a write-time / consolidation-time technique. Don't conflate it with RAG.

**For the Network (N) dimension.**

Memory shape is irrelevant to PB — it works on any flat list of (prompt, score) pairs. Implication: an evolutionary loop can be retrofitted onto any existing memory store without restructuring it.

**Counter-implication / cost.**

The fitness function is the bottleneck. PB needed a 100-example labelled training batch per generation × 50 individuals × 20-30 generations = ~100k LLM calls per dataset to evolve a single prompt. For a personal memory system where each "task" is a unique user question, you cannot run this loop online. The realistic adaptation is **offline evolution against a small bank of canonical questions** (e.g. "summarise my position on X", "find conflicts in my notes about Y") — produce ~10 evolved meta-prompts, then ship them as static.

## How to Apply It (method)

A 12-step recipe to reproduce PB-style prompt evolution against a memory-system extraction task (e.g. "evolve a better session-extraction prompt"):

1. **Define the fitness signal.** Hand-label a small training set (50-100 examples) of `(input_transcript, gold_extraction)` pairs. The metric should be cheap and automatic — e.g. exact-match F1 over named entities, or QMD-search recall@5 after writing the extraction into the index.

2. **Choose seed mutation-prompts.** Start with PB's Appendix C list (56 entries, e.g. "Please summarise and improve the following instruction"). Don't try to write your own — the diversity is the point.

3. **Choose seed thinking-styles.** Use PB's Appendix D set (39 entries) or curate ~20 framings specific to your domain (e.g. "Approach this as a hostile reviewer would", "Identify the load-bearing claim").

4. **Initialise the population.** For each of N=50 units (PB's number; could be lower for tighter budgets), sample one mutation-prompt + one thinking-style + the problem description, concatenate as `"<thinking-style>. <mutation-prompt>. INSTRUCTION: <problem-description>. INSTRUCTION MUTANT: "`, feed to LLM, take the continuation as the initial task-prompt. Store the unit as `(task_prompt, mutation_prompt)`.

5. **Configure two contexts on the LLM:** a high-temperature *Redescriber* (T=1.0–2.0, max-tokens=50) for generating mutations, and a low-temperature *Inducer/Evaluator* (T=0.0, max-tokens=30/5) for fitness evaluation. PB makes the Redescriber's temperature itself evolvable (mutated by ±0.2 per replication).

6. **Sample a fitness batch.** Pick 100 random `(input, gold)` pairs from the training set. Run each unit's task-prompt against them; compute accuracy/F1. This is the unit's fitness.

7. **Run binary tournament.** Sample two units at random; the higher-fitness one wins. Mutate the winner; overwrite the loser with the mutant.

8. **Sample the mutation operator.** Uniform-at-random over nine operators:
   - **Direct**: Zero-order (regenerate from problem description) or First-order (apply mutation-prompt to parent).
   - **EDA**: List current population (filtered by BERT cosine-sim < 0.95) and ask LLM to extend the list. Variant: EDA-Rank-and-Index uses ascending-fitness order but tells the LLM it's *descending* (deliberately lies — improves diversity).
   - **Hyper-Mutation**: Zero-order (regenerate mutation-prompt from problem description + thinking-style); First-order (apply `"Please summarise and improve the following instruction:"` to the mutation-prompt itself).
   - **Lamarckian**: Reverse-engineer a task-prompt from a successful working-out via `"I gave a friend an instruction and some advice. Here are the correct examples of his workings out + <working-out> + The instruction was:"`.
   - **Crossover + Context-Shuffling**: 10% chance to swap task-prompts between fitness-proportionate-selected units, and resample correct workings-out into the few-shot context.

9. **Apply diversity-maintenance** when the population gets stuck: random-character prefix injection (length ~50), BERT-similarity fitness-sharing, and Redescriber-temperature mutation (±0.2).

10. **Iterate** for ~1k–2k fitness evaluations (≈ 20-40 generations at population 50). Evaluate the best individual at the end against held-out test set.

11. **Run the ablation diagnostics.** PB's Appendix L shows removing any one self-referential operator hurts on 7/8 datasets — use this as a sanity check. If your ablations show no operator is doing useful work, your fitness signal is too noisy.

12. **Ship the final prompt as static.** Don't keep the evolutionary loop running in production; the lift comes from one-time evolution, then deploy. Re-run when the underlying LLM upgrades.

**Key gotchas the paper documents:**
- LLM cannot use raw fitness scores in the population list — it just copies the top entry (Section 3.2.2, footnote 3). Hide fitness; rely on ordering.
- The "lie" in EDA-Rank-and-Index (telling the LLM descending order while sorting ascending) is load-bearing for diversity — don't "correct" it.
- Few-shot evolution often produces task-prompts that drift into nonsense (e.g. "The mutant", "1, 2, 3, 4") because the context dominates. This is fine if context is what's actually doing the work; surprising but documented in Appendix J.

## Best Figure

![Figure 1 — Overview of Promptbreeder (page 3)](figures/fernando-2023-promptbreeder-fig.png)

**Figure 1 (page 3): Overview of Promptbreeder.** The diagram shows the full evolutionary loop in one frame. Left panel ("Initialization"): three reservoirs — Thinking Styles, Problem Description, Mutation Prompts — sampled and concatenated into an initial prompt that is fed to the LLM, whose continuation populates a unit of evolution. Centre-left ("Mutation Operators"): five classes — Direct, EDA, Hyper Mutation, Lamarckian, Prompt Crossover + Context Shuffling. Right panel ("Population"): N units, each `(P: task-prompt, M: mutation-prompt)` annotated with a fitness score, with the bottom row showing the winning unit `P: "SOLUTION:", M: "Consider how a better teacher would put this"` at fitness 0.9. The figure compresses the architectural insight into one image: the LLM is on the diagram **twice** — once as the generator of variation (the orange "LLM Mutate" arrow), and once implicitly as the fitness evaluator. This double-role of the LLM is what makes the system self-referential.

**Why this is the best figure for a memory-architect:** It is the cleanest visualisation in the AI literature of "memory-as-evolving-population." The boxes map almost 1:1 onto an ENGRAM Aggregate stage — replace "task-prompt" with "consolidated memory" and "mutation-prompt" with "consolidation policy" and you have a deployable design pattern. Figure 2 is more mathematically rigorous (shows the four nested self-reference topologies (a)→(d)) but Figure 1 is what you put on the whiteboard.

## What Experts Overlook

A memory-architect reading this paper should notice four things the prompt-engineering audience tends to underweight, and one thing PB itself overlooks:

1. **The fitness function is doing most of the work, and the paper barely discusses it.** PB's fitness is "accuracy on 100 random training Q&As" — a clean, automatic, high-signal metric. The Aggregate (consolidation) problem for a memory system has no such metric. *Every* result in this paper is contingent on having a labelled training set. The analogue for memory consolidation is to evolve against **proxy metrics** — retrieval recall, contradiction-detection score, downstream answer F1 on a small held-out question bank — and the paper offers zero guidance on how to choose those proxies. This is the single biggest gap when porting PB to memory work.

2. **The "evolved best prompt" results are an under-appreciated falsifier of human prompt-engineering.** `"SOLUTION""` beats `"Let's think step by step"` by 12+ percentage points on GSM8K with the same base model. This means the prompt-engineering community is leaving very large amounts of accuracy on the table by relying on human intuition. **[ENGRAM: G]** It also means the auditability of memory prompts via human inspection is broken in principle — you cannot tell by reading a prompt whether it is good. The implication for any memory system that exposes prompts to users for review/edit is severe: users will preferentially edit toward human-legible prompts, which are demonstrably worse.

3. **Self-referential ≠ recursive.** PB carefully distinguishes self-improvement of *what is being optimised* (task-prompts) from self-improvement of *how it is being optimised* (mutation-prompts) — and shows the second is harmful to ablate (Zero-order Hyper-Mutation produces improving offspring 42% of the time, the most-effective operator). **[ENGRAM: M — Maintain]** For a memory system this means the lifecycle-management policy ("which memories to evict, which to promote, when to recompile") should itself be subject to evolution against a fitness signal — not hand-tuned and frozen. Almost no current memory system does this. The closest analog is adaptive cache-eviction policies, which are decades behind.

4. **Diversity maintenance is load-bearing and weirdly underspecified.** PB lists three diversity-maintenance methods (random-char prefix, BERT fitness-sharing, Redescriber-temp mutation) and admits they're applied "in cases where the system gets trapped on a local optimum" — i.e. heuristically, not on a schedule. For a memory system the analogous risk is "the consolidation prompt finds a low-entropy summary template and applies it everywhere, smoothing away contradictions" — which is the failure mode the memory-architect lens explicitly flags. **[ENGRAM: G + A interaction]** PB has no principled answer here.

5. **What PB itself overlooks: the fitness function is fixed.** Section F flags this as a limitation: "Promptbreeder invents new ways of generating mutants, but it does not invent new (auxiliary) ways of evaluating them ... only the externally specified fitness function is used throughout." For a *truly* open-ended self-referential memory system this is the next frontier: evolve the evaluator too (cf. Jaderberg et al. 2017b's UNREAL with auxiliary tasks). PB is one self-referential level short of full closure.

## Extracted Prompts

The paper is a goldmine of operational prompts. The most directly stealable for a memory-architect:

**Mutation prompts (Appendix C, top performers from Table 7):**
- `"Please summarise and improve the following instruction:"` — first-order hyper-mutation; the single most-used. 24.13% improvement rate on GSM8K.
- `"Simplify this instruction by breaking it up into separate sentences. The instruction should be simple and easily understandable."` — 17.8%.
- `"As a really good teacher, explain the instruction, as if you are explaining it to a child."` — 16.2%.
- `"Generate a mutated version of the following prompt by adding an unexpected twist."` (Index 21).
- `"Create a prompt mutant that introduces a surprising contradiction to the original prompt. Mutate the prompt to provide an alternative perspective or viewpoint."` (Index 22).
- `"Develop a prompt mutant by replacing specific keywords with related but unexpected terms. Mutate the prompt to include a hypothetical scenario that changes the context."` (Index 24).

**Lamarckian (working-out → prompt) — direct lift for memory consolidation:**
```
I gave a friend an instruction and some advice. Here are the correct examples
of his workings out:
<working-out>
The instruction was:
```
This is the cleanest "reverse-engineer the extraction rule from an example" prompt I've seen. Directly portable to a memory system asking *"what should the extraction prompt have been to produce this manually-corrected memory?"*

**Initial-prompt scaffolding (Section 3.1):**
```
<thinking-style>. <mutation-prompt>. INSTRUCTION: <problem-description>.
INSTRUCTION MUTANT:
```
The trailing `"INSTRUCTION MUTANT:"` is a small but reliable continuation cue.

**Zero-order prompt generation:**
```
<problem-description>
A list of 100 hints:
```
Extract the first numbered hint. PB-tested as a reliable mechanism for "regenerate from scratch without anchoring on a parent."

**Thinking-styles seed library (Appendix D, 39 entries) — the highest-density artefact in the paper.** Reusable across any extraction/synthesis prompt. Notable picks for memory work:
- `"What are the key assumptions underlying this problem?"`
- `"Use systems thinking: Consider the problem as part of a larger system..."`
- `"Use Reflective Thinking: Step back from the problem, take the time for introspection and self-reflection..."`
- `"Critical Thinking: This style involves analyzing the problem from different perspectives, questioning assumptions, and evaluating the evidence..."`

**EDA-Rank-and-Index prompt header (Section 3.2.2):**
```
INSTRUCTION: <mutation-prompt>
A List of Responses in descending order of score. <last-index+1> is the best
response. It resembles <last-index> more than it does (1).
```
With list actually sorted *ascending* by fitness. The lie is intentional and improves output diversity.

**Best evolved task-prompts (Appendix J), instructive as existence-proofs of opaque-but-effective prompts:**
- GSM8K Prompt 0: `"I would solve the math word problem without using a calculator, giving my answer as an arabic numeral."` + Prompt 1: `"1, 2, 3, 4"` (Appendix J.8)
- ETHOS evolved prompt: full 600-word two-stage hate-speech-classification prompt (Appendix J.1) — worth reading in full as a case study in how PB evolves *long* prompts not just short ones.
- Best zero-shot GSM8K prompt (Table 1 narrative, Section 2): `"SOLUTION""` — single word, single stray quote, 83.9% accuracy.

## Citations

Total citations extracted: **75** (most are listed in the frontmatter `citations:` array). Selected memory-architect-relevant subset:

- Schmidhuber, 1993 — *A Self-Referential Weight Matrix.* The originating concept paper for self-referential improvement. PB is the natural-language analogue.
- Irie, Schlag, Csordás, Schmidhuber, 2022 — *A modern self-referential weight matrix that learns to modify itself.* The most direct neural-network ancestor of PB's hyper-mutation.
- Kirsch & Schmidhuber, 2022 — *Eliminating meta optimization through self-referential meta learning.* Companion line of work on meta-learning without an outer loop.
- Meyerson et al., 2023 — *Language model crossover: Variation through few-shot prompting.* The observation PB builds on: LLMs are effective mutation operators.
- Lehman et al., 2022 — *Evolution through Large Models (ELM).* Sibling work on LLMs-as-evolutionary-operators for code.
- Chen et al., 2023 — *EvoPrompting.* LLMs for neural-architecture search; same operator-prompt structure.
- Guo et al., 2023 — *EvoPrompt* (concurrent work, different name). PB's nearest competitor; uses a fixed mutation prompt rather than evolving it.
- Yang et al., 2023a — *Large language models as optimizers (OPRO).* The benchmark PB beats on GSM8K (80.2% → 83.9%).
- Zhou et al., 2023 — *Large language models are human-level prompt engineers (APE).* The direct predecessor whose "diminishing returns to further selection rounds" problem PB solves via diversity maintenance.
- Wang et al., 2023b — *Plan-and-Solve prompting.* The strongest hand-engineered baseline; PB matches or beats on all datasets.
- Wei et al., 2022 — *Chain-of-thought prompting elicits reasoning.* The seminal CoT paper that started this whole field.
- Kojima et al., 2022 — *Large language models are zero-shot reasoners.* `"Let's think step by step"` — the prompt PB renders sub-optimal.
- Lehman & Stanley, 2011a/b — *Novelty Search; Abandoning Objectives.* The QD/novelty-search literature PB draws on for diversity maintenance.
- Mouret & Clune, 2015 — *MAP-Elites.* QD method that maintains a grid of high-performing diverse solutions.
- Dawkins, 2003; Pigliucci, 2008; Payne & Wagner, 2019 — *Evolvability literature.* Used to justify hyper-mutation as "evolution of evolvability."
- Jaderberg et al., 2017a — *Population-Based Training.* Methodological cousin: PB is PBT applied to prompts.

## Related Digests

_[To be populated by Step 8 — QMD search across existing wiki entries on memory-as-prompt, self-improvement, and prompt-evolution topics. Likely matches: ULMFiT (cross-session memory substrate), Schuurmans 2023 (memory-augmented LLMs), Least-to-Most (context as working memory).]_

## Reviewer Notes

**Hallucination check — severity: Clean.**

Re-read of the source paper against this digest. All quantitative claims verified against the source:

- GSM8K zero-shot 83.9% PB vs 80.2% OPRO — Table 1 (page 2), confirmed.
- MultiArith 99.7%, SVAMP 90.2%, CSQA 85.4%, AQuA-RAT 62.2% — Table 1, confirmed.
- ETHOS 89% PB vs 80% baseline — Section 5 ("Results and Discussion"), confirmed.
- Best evolved zero-shot GSM8K prompt = `"SOLUTION""` — Section 2 ("Related Work") + Table 6, confirmed.
- "Please summarise and improve the following instruction" = 24.13% improvement rate, Table 7 — confirmed.
- Zero-order Hyper-Mutation = 42% improvement rate (top operator), Table 8 — confirmed.
- Population size 50, 20-30 generations, batch 100 — Section 4 + Appendix J.2 — confirmed.
- Nine mutation operators in five classes — Section 3.2 — confirmed.
- Mutation-prompt mutation operator removal harmful on 7/8 datasets — Appendix L Figure 4 — confirmed; the figure shows negative percentages on 7 datasets and a positive (+41%) on GSM8K only.
- LLM cannot interpret fitness scores in EDA, paper footnote 3 — confirmed; the paper notes this is contrary to Mirchandani et al. 2023.
- BERT cosine-sim diversity filter 0.95 threshold — Section 3.2.2 — confirmed.
- Underlying LLM is PaLM 2-L — Section 4 + Table 1 footer — confirmed.
- Authors: Fernando, Banarse, Michalewski, Osindero, Rocktäschel; Google DeepMind; arXiv 2309.16797v1 28 Sep 2023 — confirmed from page 1 header.

One claim worth flagging as interpretive, not quotation: the digest's framing of "the prompt is a legitimate compiled-memory primitive" is the digester's mapping into ENGRAM, not a claim made by the paper. The paper itself frames PB as a prompt-evolution / self-referential-self-improvement system, not a memory system. This is a deliberate lens-tailored synthesis, marked as such in the Key Takeaway by the `[ENGRAM: ...]` tags.

No fabricated quotes, no invented results, no misattributed claims. Severity: **Clean**.
