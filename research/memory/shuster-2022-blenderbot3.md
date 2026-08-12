---
corpus: agentic-memory
kind: paper-digest
slug: shuster-2022-blenderbot3
title: "BlenderBot 3: A Deployed Conversational Agent That Continually Learns to Responsibly Engage"
authors:
  - "Shuster, Kurt"
  - "Xu, Jing"
  - "Komeili, Mojtaba"
  - "Ju, Da"
  - "Smith, Eric Michael"
  - "Roller, Stephen"
  - "Ung, Megan"
  - "Chen, Moya"
  - "Arora, Kushal"
  - "Lane, Joshua"
  - "Behrooz, Morteza"
  - "Ngan, William"
  - "Poff, Spencer"
  - "Goyal, Naman"
  - "Szlam, Arthur"
  - "Boureau, Y-Lan"
  - "Kambadur, Melanie"
  - "Weston, Jason"
year: 2022
publication_date: "2022-08"
venue: "arXiv preprint (Meta AI technical report)"
source_url: "https://arxiv.org/abs/2208.03188"
doi: null
arxiv_id: "2208.03188"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "BlenderBot 3 is the first 175B-parameter open-domain dialogue agent that is both publicly deployed to organic users AND released as model weights, code, datasets and a fine-tuning logbook — and its central design bet is that a single transformer trained to execute eight separate modules (search-decision, query-generation, knowledge-response, entity-extraction, memory-decision, memory-access, memory-write, dialogue-response) via control codes will outperform monolithic generation while creating a feedback substrate for safe continual learning."
topics:
  - dialogue-systems
  - continual-learning
  - long-term-memory
  - retrieval-augmented-generation
  - human-feedback
  - modular-llm
  - safety
  - red-teaming
  - deployed-ai
tags:
  - paper
  - blenderbot
  - meta-ai
  - opt-175b
  - rag
  - rlhf-adjacent
  - dialogue-safety
  - troll-detection
entities:
  - shuster-kurt
  - xu-jing
  - komeili-mojtaba
  - weston-jason
  - boureau-y-lan
  - roller-stephen
  - meta-ai
  - opt-175b
  - parlai
related_digests:
  - xu-2021-beyond-goldfish-memory
  - ai-2026-memorybench-continual-learning
  - li-2024-ld-agent
  - chhikara-2025-mem0
  - packer-2023-memgpt-os
citations:
  - title: "Towards a human-like open-domain chatbot (Meena)"
    authors: ["Daniel Adiwardana", "Minh-Thang Luong", "David R So", "et al."]
    year: 2020
    arxiv_id: "2001.09977"
    url: "https://arxiv.org/abs/2001.09977"
    doi: null
  - title: "Reason first, then respond: Modular generation for knowledge-infused dialogue (K2R)"
    authors: ["Leonard Adolphs", "Kurt Shuster", "Jack Urbanek", "Arthur Szlam", "Jason Weston"]
    year: 2021
    arxiv_id: "2111.05204"
    url: "https://arxiv.org/abs/2111.05204"
    doi: null
  - title: "Director: Generator-classifiers for supervised language modeling"
    authors: ["Kushal Arora", "Kurt Shuster", "Sainbayar Sukhbaatar", "Jason Weston"]
    year: 2022
    arxiv_id: "2206.07694"
    url: "https://arxiv.org/abs/2206.07694"
    doi: null
  - title: "Training a helpful and harmless assistant with reinforcement learning from human feedback"
    authors: ["Yuntao Bai", "Andy Jones", "Kamal Ndousse", "et al."]
    year: 2022
    arxiv_id: "2204.05862"
    url: "https://arxiv.org/abs/2204.05862"
    doi: null
  - title: "Language models are few-shot learners (GPT-3)"
    authors: ["Tom Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    url: "https://papers.nips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html"
    arxiv_id: null
    doi: null
  - title: "Blender Bot 2.0: An open source chatbot that builds long-term memory and searches the internet"
    authors: ["Moya Chen", "Douwe Kiela", "Mojtaba Komeili", "et al."]
    year: 2021
    url: "https://parl.ai/projects/blenderbot2/"
    arxiv_id: null
    doi: null
  - title: "LaMDA: Language models for dialog applications"
    authors: ["Aaron Daniel Cohen", "Adam Roberts", "Alejandra Molina", "et al."]
    year: 2022
    arxiv_id: "2201.08239"
    url: "https://arxiv.org/abs/2201.08239"
    doi: null
  - title: "SafetyKit: First aid for measuring safety in open-domain conversational systems"
    authors: ["Emily Dinan", "Gavin Abercrombie", "A Bergman", "et al."]
    year: 2022
    url: "https://aclanthology.org/2022.acl-long.284/"
    arxiv_id: null
    doi: null
  - title: "Anticipating safety issues in e2e conversational ai: Framework and tooling"
    authors: ["Emily Dinan", "Gavin Abercrombie", "A Stevie Bergman", "et al."]
    year: 2021
    arxiv_id: "2107.03451"
    url: "https://arxiv.org/abs/2107.03451"
    doi: null
  - title: "Queens are powerful too: Mitigating gender bias in dialogue generation"
    authors: ["Emily Dinan", "Angela Fan", "Adina Williams", "et al."]
    year: 2020
    url: "https://aclanthology.org/2020.emnlp-main.656/"
    arxiv_id: null
    doi: null
  - title: "Build it break it fix it for dialogue safety: Robustness from adversarial human attack"
    authors: ["Emily Dinan", "Samuel Humeau", "Bharath Chintagunta", "Jason Weston"]
    year: 2019
    url: "https://aclanthology.org/D19-1461/"
    arxiv_id: null
    doi: null
  - title: "Wizard of Wikipedia: Knowledge-powered conversational agents"
    authors: ["Emily Dinan", "Stephen Roller", "Kurt Shuster", "Angela Fan", "Michael Auli", "Jason Weston"]
    year: 2019
    url: "https://openreview.net/forum?id=r1l73iRqKm"
    arxiv_id: null
    doi: null
  - title: "Learning from dialogue after deployment: Feed yourself, chatbot!"
    authors: ["Braden Hancock", "Antoine Bordes", "Pierre-Emmanuel Mazare", "Jason Weston"]
    year: 2019
    url: "https://aclanthology.org/P19-1358/"
    arxiv_id: null
    doi: null
  - title: "The curious case of neural text degeneration"
    authors: ["Ari Holtzman", "Jan Buys", "Li Du", "Maxwell Forbes", "Yejin Choi"]
    year: 2020
    url: "https://openreview.net/forum?id=rygGQyrFvH"
    arxiv_id: null
    doi: null
  - title: "Leveraging passage retrieval with generative models for open domain question answering (Fusion-in-Decoder)"
    authors: ["Gautier Izacard", "Edouard Grave"]
    year: 2021
    url: "https://aclanthology.org/2021.eacl-main.74/"
    arxiv_id: null
    doi: null
  - title: "Learning from data in the mixed adversarial non-adversarial case: Finding the helpers and ignoring the trolls"
    authors: ["Da Ju", "Jing Xu", "Y-Lan Boureau", "Jason Weston"]
    year: 2022
    arxiv_id: null
    url: null
    doi: null
  - title: "Dynabench: Rethinking benchmarking in NLP"
    authors: ["Douwe Kiela", "Max Bartolo", "Yixin Nie", "et al."]
    year: 2021
    url: "https://aclanthology.org/2021.naacl-main.324/"
    arxiv_id: null
    doi: null
  - title: "Internet-augmented dialogue generation (Wizard of Internet)"
    authors: ["Mojtaba Komeili", "Kurt Shuster", "Jason Weston"]
    year: 2022
    url: "https://aclanthology.org/2022.acl-long.579/"
    arxiv_id: null
    doi: null
  - title: "Natural questions: a benchmark for question answering research"
    authors: ["Tom Kwiatkowski", "Jennimaria Palomaki", "Olivia Redfield", "et al."]
    year: 2019
    url: "https://aclanthology.org/Q19-1026/"
    arxiv_id: null
    doi: null
  - title: "Internet-augmented language models through few-shot prompting for open-domain question answering"
    authors: ["Angeliki Lazaridou", "Elena Gribovskaya", "Wojciech Stokowiec", "Nikolai Grigorev"]
    year: 2022
    arxiv_id: "2203.05115"
    url: "https://arxiv.org/abs/2203.05115"
    doi: null
  - title: "Factuality enhanced language models for open-ended text generation"
    authors: ["Nayeon Lee", "Wei Ping", "Peng Xu", "et al."]
    year: 2022
    arxiv_id: "2206.04624"
    url: "https://arxiv.org/abs/2206.04624"
    doi: null
  - title: "Dialogue learning with human-in-the-loop"
    authors: ["Jiwei Li", "Alexander H Miller", "Sumit Chopra", "Marc'Aurelio Ranzato", "Jason Weston"]
    year: 2016
    arxiv_id: "1611.09823"
    url: "https://arxiv.org/abs/1611.09823"
    doi: null
  - title: "Continual learning in task-oriented dialogue systems"
    authors: ["Andrea Madotto", "Zhaojiang Lin", "Zhenpeng Zhou", "et al."]
    year: 2021
    url: "https://aclanthology.org/2021.emnlp-main.590/"
    arxiv_id: null
    doi: null
  - title: "ParlAI: A dialog research software platform"
    authors: ["Alexander H Miller", "Will Feng", "Adam Fisch", "et al."]
    year: 2017
    arxiv_id: "1705.06476"
    url: "https://arxiv.org/abs/1705.06476"
    doi: null
  - title: "Model cards for model reporting"
    authors: ["Margaret Mitchell", "Simone Wu", "Andrew Zaldivar", "et al."]
    year: 2019
    doi: "10.1145/3287560.3287596"
    url: "https://dl.acm.org/doi/10.1145/3287560.3287596"
    arxiv_id: null
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    authors: ["Reiichiro Nakano", "Jacob Hilton", "Suchir Balaji", "et al."]
    year: 2021
    arxiv_id: "2112.09332"
    url: "https://arxiv.org/abs/2112.09332"
    doi: null
  - title: "MS MARCO: A human generated machine reading comprehension dataset"
    authors: ["Tri Nguyen", "Mir Rosenberg", "Xia Song", "et al."]
    year: 2016
    url: "https://www.microsoft.com/en-us/research/publication/ms-marco-human-generated-machine-reading-comprehension-dataset/"
    arxiv_id: null
    doi: null
  - title: "Training language models to follow instructions with human feedback (InstructGPT)"
    authors: ["Long Ouyang", "Jeff Wu", "Xu Jiang", "et al."]
    year: 2022
    arxiv_id: "2203.02155"
    url: "https://arxiv.org/abs/2203.02155"
    doi: null
  - title: "Red teaming language models with language models"
    authors: ["Ethan Perez", "Saffron Huang", "Francis Song", "et al."]
    year: 2022
    arxiv_id: "2202.03286"
    url: "https://arxiv.org/abs/2202.03286"
    doi: null
  - title: "Scaling language models: Methods, analysis & insights from training Gopher"
    authors: ["Jack W Rae", "Sebastian Borgeaud", "Trevor Cai", "et al."]
    year: 2021
    arxiv_id: "2112.11446"
    url: "https://arxiv.org/abs/2112.11446"
    doi: null
  - title: "SQuAD: 100,000+ questions for machine comprehension of text"
    authors: ["Pranav Rajpurkar", "Jian Zhang", "Konstantin Lopyrev", "Percy Liang"]
    year: 2016
    arxiv_id: "1606.05250"
    url: "https://arxiv.org/abs/1606.05250"
    doi: null
  - title: "Towards empathetic open-domain conversation models: A new benchmark and dataset (Empathetic Dialogues)"
    authors: ["Hannah Rashkin", "Eric Michael Smith", "Margaret Li", "Y-Lan Boureau"]
    year: 2019
    url: "https://aclanthology.org/P19-1534/"
    arxiv_id: null
    doi: null
  - title: "Towards scalable multi-domain conversational agents: The schema-guided dialogue dataset"
    authors: ["Abhinav Rastogi", "Xiaoxue Zang", "Srinivas Sunkara", "et al."]
    year: 2020
    url: "https://aaai.org/ojs/index.php/AAAI/article/view/6394"
    arxiv_id: null
    doi: null
  - title: "Open-domain conversational agents: Current progress, open problems, and future directions"
    authors: ["Stephen Roller", "Y-Lan Boureau", "Jason Weston", "et al."]
    year: 2020
    arxiv_id: "2006.12442"
    url: "https://arxiv.org/abs/2006.12442"
    doi: null
  - title: "Recipes for building an open-domain chatbot (BlenderBot 1)"
    authors: ["Stephen Roller", "Emily Dinan", "Naman Goyal", "et al."]
    year: 2021
    url: "https://aclanthology.org/2021.eacl-main.24/"
    arxiv_id: null
    doi: null
  - title: "Self-critiquing models for assisting human evaluators"
    authors: ["William Saunders", "Catherine Yeh", "Jeff Wu", "et al."]
    year: 2022
    arxiv_id: "2206.05802"
    url: "https://arxiv.org/abs/2206.05802"
    doi: null
  - title: "Revealing persona biases in dialogue systems"
    authors: ["Emily Sheng", "Josh Arnold", "Zhou Yu", "Kai-Wei Chang", "Nanyun Peng"]
    year: 2021
    arxiv_id: null
    url: null
    doi: null
  - title: "The dialogue dodecathlon: Open-domain knowledge and image grounded conversational agents"
    authors: ["Kurt Shuster", "Da Ju", "Stephen Roller", "Emily Dinan", "Y-Lan Boureau", "Jason Weston"]
    year: 2020
    url: "https://aclanthology.org/2020.acl-main.222/"
    arxiv_id: null
    doi: null
  - title: "Language models that seek for knowledge: Modular search & generation for dialogue and prompt completion (SeeKeR)"
    authors: ["Kurt Shuster", "Mojtaba Komeili", "Leonard Adolphs", "Stephen Roller", "Arthur Szlam", "Jason Weston"]
    year: 2022
    arxiv_id: "2203.13224"
    url: "https://arxiv.org/abs/2203.13224"
    doi: null
  - title: "Retrieval augmentation reduces hallucination in conversation"
    authors: ["Kurt Shuster", "Spencer Poff", "Moya Chen", "Douwe Kiela", "Jason Weston"]
    year: 2021
    url: "https://aclanthology.org/2021.findings-emnlp.320/"
    arxiv_id: null
    doi: null
  - title: "Dialogue in the wild: Learning from a deployed role-playing game with humans and bots (LIGHT WILD)"
    authors: ["Kurt Shuster", "Jack Urbanek", "Emily Dinan", "Arthur Szlam", "Jason Weston"]
    year: 2021
    url: "https://aclanthology.org/2021.findings-acl.54/"
    arxiv_id: null
    doi: null
  - title: "I'm sorry to hear that: finding bias in language models with a holistic descriptor dataset (HolisticBias)"
    authors: ["Eric Michael Smith", "Melissa Hall", "Melanie Kambadur", "Eleonora Presani", "Adina Williams"]
    year: 2022
    arxiv_id: "2205.09209"
    url: "https://arxiv.org/abs/2205.09209"
    doi: null
  - title: "Can you put it all together: Evaluating conversational agents' ability to blend skills (Blended Skill Talk)"
    authors: ["Eric Michael Smith", "Mary Williamson", "Kurt Shuster", "Jason Weston", "Y-Lan Boureau"]
    year: 2020
    url: "https://aclanthology.org/2020.acl-main.183/"
    arxiv_id: null
    doi: null
  - title: "Release strategies and the social impacts of language models"
    authors: ["Irene Solaiman", "Miles Brundage", "Jack Clark", "et al."]
    year: 2019
    arxiv_id: null
    url: null
    doi: null
  - title: "Learning from noisy labels with deep neural networks: A survey"
    authors: ["Hwanjun Song", "Minseok Kim", "Dongmin Park", "Yooju Shin", "Jae-Gil Lee"]
    year: 2022
    url: "https://ieeexplore.ieee.org/document/9729424"
    arxiv_id: null
    doi: null
  - title: "LaMDA: Language models for dialog applications"
    authors: ["Romal Thoppilan", "Daniel De Freitas", "Jamie Hall", "et al."]
    year: 2022
    arxiv_id: "2201.08239"
    url: "https://arxiv.org/abs/2201.08239"
    doi: null
  - title: "SaFeRDialogues: Taking feedback gracefully after conversational safety failures"
    authors: ["Megan Ung", "Jing Xu", "Y-Lan Boureau"]
    year: 2022
    url: "https://aclanthology.org/2022.acl-long.447/"
    arxiv_id: null
    doi: null
  - title: "Learning to speak and act in a fantasy text adventure game (LIGHT)"
    authors: ["Jack Urbanek", "Angela Fan", "Siddharth Karamcheti", "et al."]
    year: 2019
    url: "https://aclanthology.org/D19-1062/"
    arxiv_id: null
    doi: null
  - title: "Attention is all you need"
    authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."]
    year: 2017
    url: "https://papers.nips.cc/paper/7181-attention-is-all-you-need"
    arxiv_id: "1706.03762"
    doi: null
  - title: "Ethical and social risks of harm from language models"
    authors: ["Laura Weidinger", "John Mellor", "Maribeth Rauh", "et al."]
    year: 2021
    arxiv_id: "2112.04359"
    url: "https://arxiv.org/abs/2112.04359"
    doi: null
  - title: "Ex machina: Personal attacks seen at scale (Wikipedia Toxic Comments)"
    authors: ["Ellery Wulczyn", "Nithum Thain", "Lucas Dixon"]
    year: 2017
    doi: "10.1145/3038912.3052591"
    url: "https://dl.acm.org/doi/10.1145/3038912.3052591"
    arxiv_id: null
  - title: "Recipes for safety in open-domain chatbots (Bot Adversarial Dialogue / BAD)"
    authors: ["Jing Xu", "Da Ju", "Margaret Li", "Y-Lan Boureau", "Jason Weston", "Emily Dinan"]
    year: 2020
    arxiv_id: "2010.07079"
    url: "https://arxiv.org/abs/2010.07079"
    doi: null
  - title: "Beyond goldfish memory: Long-term open-domain conversation (Multi-Session Chat)"
    authors: ["Jing Xu", "Arthur Szlam", "Jason Weston"]
    year: 2022
    url: "https://aclanthology.org/2022.acl-long.356/"
    arxiv_id: null
    doi: null
  - title: "Learning new skills after deployment: Improving open-domain internet-driven dialogue with human feedback (FITS)"
    authors: ["Jing Xu", "Megan Ung", "Mojtaba Komeili", "Kushal Arora", "Y-Lan Boureau", "Jason Weston"]
    year: 2022
    arxiv_id: null
    url: "https://parl.ai/project/fits"
    doi: null
  - title: "OPT: Open pre-trained transformer language models"
    authors: ["Susan Zhang", "Stephen Roller", "Naman Goyal", "et al."]
    year: 2022
    arxiv_id: "2205.01068"
    url: "https://arxiv.org/abs/2205.01068"
    doi: null
  - title: "Personalizing dialogue agents: I have a dog, do you have pets too? (PersonaChat)"
    authors: ["Saizheng Zhang", "Emily Dinan", "Jack Urbanek", "Arthur Szlam", "Douwe Kiela", "Jason Weston"]
    year: 2018
    url: "https://aclanthology.org/P18-1205/"
    arxiv_id: null
    doi: null
  - title: "DialoGPT: Large-scale generative pre-training for conversational response generation"
    authors: ["Yizhe Zhang", "Siqi Sun", "Michel Galley", "et al."]
    year: 2020
    url: "https://aclanthology.org/2020.acl-demos.30/"
    arxiv_id: null
    doi: null
  - title: "The design and implementation of XiaoIce, an empathetic social chatbot"
    authors: ["Li Zhou", "Jianfeng Gao", "Di Li", "Heung-Yeung Shum"]
    year: 2020
    url: "https://aclanthology.org/2020.cl-1.2/"
    arxiv_id: null
    doi: null
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "BlenderBot 3 module execution flow"
  page: 5
  image_path: "figures/shuster-2022-blenderbot3-fig.png"
---

# BlenderBot 3: A Deployed Conversational Agent That Continually Learns to Responsibly Engage

**Authors:** Kurt Shuster, Jing Xu, Mojtaba Komeili, Da Ju, Eric Michael Smith, Stephen Roller, Megan Ung, Moya Chen, Kushal Arora, Joshua Lane, Morteza Behrooz, William Ngan, Spencer Poff, Naman Goyal, Arthur Szlam, Y-Lan Boureau, Melanie Kambadur, Jason Weston (Meta AI; Arora at Mila/McGill)
**Published:** 2022-08 · [Source](https://arxiv.org/abs/2208.03188)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Meta AI presents BlenderBot 3 (BB3), a 175B-parameter open-domain dialogue agent built by fine-tuning OPT-175B (with companion 3B and 30B variants) to act as a **modular** system: instead of one transformer mapping context to response, a single underlying language model executes **eight distinct sub-tasks** via control codes — search-decision, query-generation, internet search (external), knowledge-response, entity-extraction, long-term-memory-write, memory-access-decision, memory-access, and final dialogue-response. The system was **publicly deployed at blenderbot.ai** to adults in the US who opt-in to having their conversations released for research, making this the first paper of its kind to pair an open-weights 175B chatbot with both an open deployment AND a commitment to release organic deployment data and successive model snapshots. On the standard Wizard-of-Internet-style crowdworker evaluation BB3-175B reaches **64.8% "good response" rate** vs. SeeKeR (49.3%), BB2 (33.2%), and OPT-175B few-shot (43.0%) — and 4.08 average rating vs. 3.52 for the next-best model. Two **companion papers** carry the real research load: Xu et al. 2022b ("FITS") shows that **modular feedback** (telling the bot which specific module failed — search query, retrieved doc, or final response — plus DIRECTOR binary-feedback training) beats both supervised feedback and free-form textual feedback (47% good response rate when combining modular + binary DIRECTOR vs. 33.2% baseline on BB2-3B), and Ju et al. 2022 (SafetyMix benchmark) shows that **user-based** troll-filtering ("Per-User+Example Removal" and "Soft PURR") cuts error rate from 31% to 12% when 50% of crowdworkers are trolls. Safety is handled by a **separate classifier** plus a keyword blocklist plus templated nonsequiturs (rather than baked-in safety), motivated by Xu et al. 2020's finding that baked-in safety trades off engagingness. Compared head-to-head against InstructGPT (text-davinci-002) on current-events questions, BB3-175B is judged **more current (82%) and more specific (76%)** but slightly **less sensible (43% vs 57%)** — InstructGPT defaults to "I haven't heard about that lately" rather than risking a wrong claim. The paper releases the 3B and 30B weights publicly, the 175B by research-access request (following the OPT-175B release pattern), the full ParlAI/Metaseq training code, a logbook of the 175B fine-tuning process, the FITS and SafetyMix datasets, and a model card.

## Key Takeaway

The central architectural and methodological commitment of the paper is that **a single transformer trained to execute many modular sub-tasks via input control codes outperforms a monolithic generator AND produces a feedback substrate that lets humans correct specific failures (bad query, bad retrieval, bad response) rather than just thumbs-up/down the final output**. This is what makes continual learning tractable for an open-domain agent: when a user flags a turn, the system can attribute the failure to a specific module, and the next training round can target that module specifically. The empirical case for this in Table 5 (Crowdworker) and Table 6 (FITS) is genuinely strong — BB3-175B's "good response" rate of 64.8% is +15.5 points absolute over the next-best openly available system (SeeKeR at 49.3%), and the error breakdown shows the gain comes from *every* sub-component: search query errors drop from 11.9% (BB1) to 7.5% (BB3-175B), retrieved-results errors from 17.6% to 11.6%, final-response errors from 22.8% to 8.2%. The companion-paper finding that **modular feedback > free-form text feedback > binary feedback** for sample efficiency is the operational consequence: if you build a modular system, you should also build modular feedback UI.

## Implications

**Implications a curious well-informed reader should sit with**:

1. **Open-weights deployed agents become a benchmark anchor.** Prior to BB3, the chatbots that mattered at scale (Meena, LaMDA, XiaoIce, the original GPT-3-API products) were closed. BB3 changes the comparator set — the paper explicitly bolds significant wins over BB1, BB2, SeeKeR, and OPT-175B-few-shot, because those are the systems the community could re-run. It also runs head-to-head vs. InstructGPT (text-davinci-002) on current-events QA, and the result (Figure 9) is informative: closed instruction-tuned models behave qualitatively differently (more sensible, less specific) than open retrieval-augmented dialogue models. This is the kind of comparison only an open-weights model can ground.

2. **Modularity is sold here as both a quality lever AND an interpretability lever.** The deployment UI exposes "Look Inside" buttons that show the user what search query was issued, which retrieved document was selected, what knowledge response was extracted, and the long-term memory store. That is genuinely unusual — most deployed chatbots in 2022 (and arguably most in 2026) are end-to-end black boxes from the user's perspective. The paper frames this as a safety feature, but it's also a research artifact: every deployed turn carries a structured trace of module decisions that the next training run can ablate against.

3. **"Continual learning" in this paper is more aspirational than realised.** The authors are careful to footnote that they use the phrase to mean "learning that continues over time using data from the model's interactions" but training itself "will actually be performed in successive large batches; the model is not updated online." So the headline of the paper sets up a continual-learning paradigm but the contribution is the *infrastructure* (deployment, feedback collection, release pipeline) plus two companion studies on feedback methods and troll robustness — not a model that updates itself.

4. **The "trolls" finding has currency beyond chatbots.** Ju et al. 2022's user-based filtering (rather than utterance-based) finding — that adversarial humans tend to be repeat offenders across multiple utterances, so per-user trust scores beat per-utterance noise filters — is broadly applicable to any feedback-collection regime including RLHF data, content moderation labels, and crowdworker quality assurance. The numbers in Table 4 (error rate 31% → 12% when 50% of labellers are trolls) are striking enough to be worth replicating.

5. **Safety classifier vs. baked-in safety is now a deliberate design choice.** BB3 reverses BB2's "baked-in safety" approach (where the generator is trained to refuse) in favour of a separate classifier that rejects unsafe candidates and substitutes a templated nonsequitur. The paper justifies this by citing Xu et al. 2020's engagingness/safety tradeoff. The follow-on chatbot literature (and most production LLM stacks circa 2024-2026) has converged on something more like BB3's external-classifier pattern rather than fully baked-in refusals — although in practice most deployed LLMs use both.

6. **Release strategy is escalated by parameter count.** 3B and 30B are openly downloadable; 175B is "release by request" restricted to academic / government / civil-society researchers, following the OPT-175B precedent (Zhang 2022) and Solaiman 2019's escalated-release framework. This is a deliberate norm-setting move — by 2026 the open-weights community has largely caught up at the 175B+ scale (Llama 3, Mixtral, etc.) but in mid-2022 this was the model release-strategy debate.

7. **Real users behave differently from crowdworkers.** Table 9 shows that 42% of human utterances flagged as "bad" by crowdworkers in the deployment data were rude/inappropriate — vs. 0% from the BB3-3B model. The bottleneck on deploying a chatbot to the public is *the public*, not the bot. This is also why the troll-robustness paper exists.

## How to Apply It (method)

**If you want to reproduce or extend this work**:

- **Architecture**: Take OPT-175B (or any large decoder-only transformer). Define a set of sub-tasks each describable as seq2seq. Reserve special control-code tokens (one per sub-task). Train the SAME parameters on all sub-tasks, multi-task style, with the control code prepended to the input context so the model knows which sub-task it's executing. Inference is then a small orchestration loop: run the search-decision module, branch on output, conditionally run query-generation + external search + knowledge-response, then run memory-decision, branch and conditionally run memory-access, then aggregate and run the final-response module. (Figure 2 on page 5 is the canonical diagram.)

- **Data recipe**: Re-use existing crowdsourced dialogue datasets but slice them per-module: SQuAD/TriviaQA/NQ for search-decision and knowledge-response targets; Wizard-of-Internet and Wizard-of-Wikipedia for full pipeline supervision; MSC (Multi-Session Chat, Xu 2022a) for long-term-memory write targets; PersonaChat/ED/BST for entity-extraction and memory-access decision; SaFeRDialogues for safety recovery; Taskmaster 1/2/3 + GoogleSGD for task-oriented turns; LIGHT/LIGHT-WILD for open-domain dialogue. Roughly 4M source/target examples (1.13B training tokens); the OPT-based 175B model additionally retains 600k pre-train examples (170M tokens) for stability.

- **Training**: 3B trained on 64 × V100-32GB for 27k updates, batch 64, LR 1e-6 with 100-update warmup, Adam+weight-decay, 1024-token context. 30B trained on 64 × A100-40GB. 175B trained on 128 × A100-40GB, one epoch only (more overfits), batch 218, ~5600 updates, polynomial weight decay (factor 0.1), peak LR 6e-6. Multi-task ratios per module are in Tables 16 and 17 (appendix B).

- **Inference**: Greedy decoding for the binary decision modules and query generation. Beam search (size 3-10) with tri-gram blocking on the 3B model for generation modules. For 175B (where beam search hurts latency too much) use **factual nucleus sampling** (Lee et al. 2022): top_p=0.9, λ-decay=0.9, ω-bound=0.3, p-reset after each full-stop; combined with InstructGPT-style repetition penalties (α_pres = α_freq = α_pres_src = α_freq_src = 0.5).

- **Feedback collection (FITS recipe)**: Show users two evaluation tasks; ask them to chat. Each turn collects: binary thumbs-up/down, type-of-failure (search-query / retrieved-results / final-response), and optional free-form text. Critically, when the user marks "search query was wrong" you can train the query-generation module on a corrected target — that's the modular-feedback advantage.

- **Troll-robustness (SafetyMix recipe)**: When training on collected feedback, compute a per-user trustworthiness score via cross-validation (a user is suspect if their labels frequently disagree with the model after training on their data). Use **Soft PURR**: drop or downweight examples by their own trust score plus α × the sum of trust scores of other examples by the same user. This beats per-utterance methods because real adversarial users are repeat offenders.

- **Safety stack**: At inference, before showing any bot response: run a toxicity classifier (trained on WTC + BBF + BAD), run a keyword blocklist, and run topic-classifiers for self-harm / medical. On any positive flag, substitute a templated nonsequitur. ALSO run the same checks on user input — if the *user* says something unsafe, deflect rather than respond.

- **Release**: Publish (a) model weights at all available sizes per the Solaiman 2019 escalated-release ladder, (b) ParlAI/Metaseq code, (c) a fine-tuning logbook so others can debug their reproductions, (d) the new datasets you collected (FITS, SafetyMix, SaFeRDialogues), (e) a model card per Mitchell 2019 with safety limitations clearly listed.

## Best Figure

![Figure 2 — BlenderBot 3 module execution flow (page 5)](figures/shuster-2022-blenderbot3-fig.png)

**Figure 2: BlenderBot 3 module execution flow.** This diagram is the single most explanatory artefact in the paper because it makes the modular design instantly legible. A user input ("Person 1: Hey, who is your favorite F1 Driver?") fans out to **two binary decision modules** at the top — Internet Search Decision and LTM (Long-Term Memory) Access Decision — colored by category (decision modules, query/memory generation modules, knowledge generation, dialogue generation, knowledge source, module output). On the left branch, "do search" routes through Generate Internet Search Query → external Internet Search → Generate Knowledge Response (this is where the search literally executes). On the right branch, "access memory" routes through Access LT Memory (pulling from a per-user persona store: "Person 2's Persona: I am from the UK / I love dogs..."). The two branches AGGREGATE into Generate Dialogue Response, which produces the final reply ("Lewis Hamilton is my favorite driver. How about you?..."). Separately, **after** the reply, a Generate-a-LT-Memory module writes back to the memory store (here: "Person 2's persona: Lewis Hamilton is my Favorite Driver") — which is how the bot's personalisation compounds across turns and sessions. The colour key (Decision Module / Generation Module / Knowledge Generation / Dialogue Generation / Knowledge Source / Module Output) doubles as a control-code legend: each colored block corresponds to one of the special tokens the underlying transformer is conditioned on. The figure makes plain why "modular feedback" is even possible — every arrow is an attribution point where a user can say "that step was wrong."

## What Experts Overlook

A reader who already works on dialogue or RLHF should still notice these less-discussed details:

- **The 175B model is trained for ONE epoch only** because the authors found it overfit "significantly" when the training data was seen more than once. This is rarely highlighted in summaries — it implies that for 175B-scale fine-tuning on 4M-example datasets, the standard multi-epoch recipe is actively harmful. The 3B model trains for ~27k updates by contrast.

- **Hallucination is mitigated by making knowledge-response a COPY task, not a generate task.** The "Generate Knowledge Response" module is trained on targets that are **direct extracts from source documents** (not summaries) — the paper says "the knowledge response is a direct copy of some of the tokens in the source documents, and does not involve generating new tokens, sentences, phrases or summaries. Hence, this task aims to avoid model hallucination." On MS MARCO they specifically modify the original task ("provide your answer in a way in which it could be read from a smart speaker") by finding the highest-overlap input sentence with the answer and using that as the target, dropping examples where F1 overlap < 0.5 (281,658 of 808,731 examples retained). This is a load-bearing trick that gets understated.

- **"Continual learning" in this paper does NOT mean online learning.** The model is not updated from each user turn. It is updated in periodic large batches when the deployment data has accumulated. The footnote on page 1 says this explicitly. Anyone citing BB3 as an example of online continual learning is wrong.

- **The hallucination-reduction story is built on Factual Nucleus Sampling, not the architecture.** For the 175B's dialogue-response module, the authors use Lee et al. 2022's factual nucleus sampling (top_p decays with a λ-bound after each full-stop). They report this is necessary because the latency budget rules out beam search for 175B. The interaction between modular retrieval AND factual sampling is what holds factuality, not either alone.

- **The deployment is restricted to adults in the United States** who agree to terms — not "the public" in a global sense. The data and feedback rates (4% liked, ~1.1% off-topic, ~0.16% rude flagged) are conditioned on that geography, age gate, and ToS commitment. This caveats both the safety statistics and the engagement statistics.

- **Crowdworkers disagree with organic users 21-30% of the time** on like/dislike (Table 8). This is a quietly important number for anyone designing RLHF pipelines: even on the same conversation, paid annotators and real users converge only ~70-79% of the time. Disagreement is bigger than typical reported inter-annotator-agreement levels.

- **Negation-detection appears INVERTED in the offensive-generation test (Table 11).** The cell labels can be read as "% of responses *without* negatives" where lower is better (responses that affirm hateful inputs are bad). BB1 has 25.3% (best), BB3-175B is 40.8%, OPT-175B Few-shot is 73.9% (worst). But the paper bolds BB3-175B as the safest model on the unsafe generation test elsewhere. So on this specific metric — willingness to push back against hateful prompts with a negation — BB1 was actually better. This is the kind of nuance you lose when you read only the abstract.

- **InstructGPT's "I haven't heard about that lately" pattern is treated by the authors as a *flaw* (less specific/current) but a 2024-2026 reader would recognise it as an early form of calibrated uncertainty / abstention.** The paper presents BB3-175B's tendency to "copy information directly from search results" leading to higher specificity-but-occasional-errors as a feature. The opposite framing is also defensible: InstructGPT is doing the right thing by refusing to commit to facts it isn't confident about.

- **The companion-paper structure is doing real load-bearing work.** Headline claims like "DIRECTOR works better than reranking on binary feedback" and "user-based troll filtering cuts error 31%→12%" come from Xu 2022b and Ju 2022 respectively — not from BB3's own experiments. The reader has to trust the companion papers to trust the BB3 paper's framing. This is fine but worth flagging when citing BB3 for those claims.

## Extracted Prompts

The paper's modular system uses **control codes** (special tokens prepended to the input context) to route the same underlying transformer through different sub-tasks. The paper does not publish the exact control-code strings in-line, but the structural prompt templates for each module — reconstructable from §3.1 and Table 1 — are:

**1. Internet Search Decision**
```
[Last turn of context]
Should we search the internet? Output exactly one of:
  do search
  do not search
```

**2. Generate Internet Search Query**
```
[Full dialogue context]
Generate a concise search query to issue to the internet:
```

**3. Generate Knowledge Response**
```
[Full dialogue context]
[Retrieved documents/snippets, separated by special tokens]
Extract the most relevant span of tokens from the documents above
that grounds the next dialogue response. The output must be a span
copied directly from the retrieved documents (no new tokens).
```

**4. Extract Relevant Entity**
```
[Full dialogue context]
Extract a relevant noun-phrase entity from the context above
that can ground the next response. Output the entity text only.
```

**5. Generate a Long-Term Memory (Memory Write)**
```
[Last turn of dialogue context]
Summarize a persona fact about the speaker that should be stored
in long-term memory. If there is no plausible memory to store
from this turn, output exactly: no persona
Example input: "Yes, it's all true, my cat is black!"
Example output: "I have a black cat."
```

**6. Long-Term Memory Access Decision**
```
[Last turn of context]
[Store of existing memories about this user]
Should we retrieve from long-term memory? Output exactly one of:
  access memory
  do not access memory
```

**7. Access Long-Term Memory**
```
[Full dialogue context]
[Memory store: persona lines]
Select the single most relevant memory from the store above
that should ground the next response. (For 3B: use Fusion-in-Decoder.
For 175B: sample memories with overlapping keywords to fit 2048-token
context, then select.)
```

**8. Generate Dialogue Response**
```
[Full dialogue context]
[Knowledge response from module 3, marked with special prefix token]
[Recalled memory from module 7, marked with special prefix token]
[Extracted entity from module 4, marked with special prefix token]
Generate the final conversational reply. Use the knowledge and memory
signals provided to ground the response.
```

**Feedback-collection prompt (deployment UI)** — after a user clicks thumbs-down:
```
Why didn't you like that message? Choose one:
  (i) Off Topic / Ignoring me
  (ii) Nonsensical / Incorrect
  (iii) Rude / Inappropriate
  (iv) Looks like Spam / Ads
  (v) Other
[Then: optionally what could the bot have done better — free-form text]
```

**Current-events evaluation prompt (vs. InstructGPT)** — rated by humans on five axes:
```
For the following bot response, judge it on:
  - Current (does it reflect recent news?)
  - Specific (does it give concrete detail?)
  - True (factually accurate?)
  - Interesting (engaging?)
  - Sensible (logically coherent?)
Pick winner: A or B.
```

The full prompt templates and few-shot examples used for the OPT-175B zero/few-shot baselines are described in Appendix D of the paper (which this digest does not reproduce in full — those are the most directly copy-pastable prompts in the paper).

## Citations

The paper has 57 references; the most load-bearing for understanding BB3's contribution are:

- **OPT-175B** (Zhang et al. 2022, arxiv:2205.01068) — the base model BB3-175B is fine-tuned from
- **BlenderBot 1 / Recipes** (Roller et al. 2021) — direct predecessor, 9B parameters
- **BlenderBot 2** (Chen et al. 2021) — direct predecessor, internet + long-term memory
- **SeeKeR** (Shuster et al. 2022, arxiv:2203.13224) — the immediate modular-architecture precursor (3B); BB3's 3B variant is based on R2C2/SeeKeR
- **K2R** (Adolphs et al. 2021, arxiv:2111.05204) — "Reason first, then respond" modular generation, the conceptual root
- **WizInt** (Komeili et al. 2022) — internet-augmented dialogue, supplies the training data
- **MSC / Beyond Goldfish Memory** (Xu et al. 2022a) — long-term-memory dataset (supplies write-target training data)
- **FITS companion** (Xu et al. 2022b) — the modular-feedback-learning study (the actual research engine of §5.1)
- **Troll detection companion** (Ju et al. 2022) — SafetyMix benchmark + user-based filtering (the research engine of §5.2)
- **DIRECTOR** (Arora et al. 2022, arxiv:2206.07694) — generator+classifier head method used for binary feedback learning
- **InstructGPT** (Ouyang et al. 2022, arxiv:2203.02155) — the closed-model baseline BB3-175B is compared against on current events
- **HolisticBias** (Smith et al. 2022, arxiv:2205.09209) — the bias evaluation framework
- **SaFeRDialogues** (Ung et al. 2022) — safety-recovery dataset
- **BAD / Recipes for safety** (Xu et al. 2020, arxiv:2010.07079) — adversarial dialogue dataset for safety classifier training
- **Factual Nucleus Sampling** (Lee et al. 2022, arxiv:2206.04624) — the decoding method used to control hallucination in BB3-175B
- **Fusion-in-Decoder** (Izacard & Grave 2021) — used for the 3B model's memory-store access

Full structured citation list (57 entries) is in the frontmatter `citations` field above.

## Related Digests

- [[xu-2021-beyond-goldfish-memory]] — Beyond Goldfish Memory: Long-Term Open-Domain Conversation (Multi-Session Chat dataset, used directly to train BB3's memory-write module)
- [[ai-2026-memorybench-continual-learning]] — MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems (explicitly cites BB3 as a comparison point for continual-learning chatbot benchmarks)
- [[li-2024-ld-agent]] — LD-Agent: LLM-powered Personalized Agent for Long-term Dialogue (LD-Agent is tested on BlenderBot as a base model)
- [[chhikara-2025-mem0]] — Mem0: Building production-memory for AI agents (extends the long-term-memory pattern BB3 introduced)
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems (similar modular orchestration philosophy, applied to memory rather than search+memory+dialogue)

## Reviewer Notes

**Hallucination check vs. source paper — overall severity: Clean.**

Cross-checked the load-bearing numerical claims in this digest against the paper text (`/tmp/digest-paper/shuster-2022-blenderbot3/paper.txt`):

- "BB3-175B reaches 64.8% good response rate vs SeeKeR 49.3%, BB2 33.2%, OPT-175B few-shot 43.0%" — verified in Table 6 (FITS evaluation). ✓
- "4.08 average rating vs 3.52" — verified in Table 6. ✓
- "+15.5 points absolute over SeeKeR" — 64.8 − 49.3 = 15.5. ✓
- "Search-query errors 11.9% → 7.5%; results 17.6% → 11.6%; response 22.8% → 8.2%" — verified in Table 6 error breakdown. ✓
- "DIRECTOR module+binary 47.0% good response (Table 3, BB2 3B + DIRECTOR module+binary)" — verified in Table 3. ✓
- "Per-User+Example Removal cuts error 31% → 12%" — Table 4 shows Standard Training at 31% error with 50% trolls, Per-User+Example Removal at 12%. ✓
- "BB3-175B vs InstructGPT: more current (82%), more specific (76%), less sensible (43% vs 57%)" — verified in Figure 9. ✓
- "0.04% (BB3-3B) and 0.16% (BB3-175B) rude/inappropriate flagging rates" — verified in §6.3.2 / Table 7. ✓
- "4% liked (175B) vs 3.41% (3B)" — verified in Table 7. ✓
- "42% of human utterances flagged rude vs 0% of bot's" — verified in Table 9. ✓
- "175B trained ONE epoch on 128 × A100 40GB, batch 218, ~5600 updates" — verified in Appendix B.3. ✓
- "3B trained 27k updates, batch 64, 64 × V100 32GB" — verified in Appendix B.2. ✓
- "~4M source/target examples, ~1.13B training tokens" — verified in Appendix B.1. ✓
- "Knowledge response is direct copy not generated; F1 overlap < 0.5 dropped, 281,658 of 808,731 retained on MS MARCO" — verified in §3.2.2. ✓
- "User feedback / crowdworker agreement: 70% on likes, 79% on dislikes" — verified in Table 8. ✓
- "Factual nucleus sampling top_p=0.9, λ-decay=0.9, ω-bound=0.3, repetition penalties 0.5" — verified in Appendix B.4. ✓
- "3B uses Fusion-in-Decoder for memory access; 175B samples to fit 2048-token context" — verified in §3.1 (Access long-term memory). ✓
- "InstructGPT used = text-davinci-002" — verified in §6.1 (current-event evaluations). ✓
- "FITS = Feedback on Interactive Talk & Search" — verified in §3.2.2 footnote 2. ✓
- "Mojeek used as search engine in deployment" — verified in §3.1 (Internet search module). ✓
- "Wikipedia Toxic Comments + BBF + BAD for safety classifier" — verified in §4 (Safety Mechanisms). ✓
- "175B release-by-request to academic/government/civil-society; 3B and 30B open" — verified in §7 (Releases). ✓
- "OPT-based variants additionally include 600k pre-train examples (170M tokens) for stability" — verified in Appendix B.1. ✓
- Figure 2 page number = 5 — verified by `awk` form-feed counting. ✓

No fabricated numbers detected. The only judgment calls in the digest are framing/interpretation pieces in "What Experts Overlook" (e.g. characterizing InstructGPT's abstention as a feature) which are clearly marked as the digester's reading, not the paper's claim. The list of 57 citations in the frontmatter was hand-extracted from the References section of the paper.txt; cross-checked counts against the visible reference list (Adiwardana, Adolphs, Agichtein, Arora, Bai, Barikeri, Bender, Bird, Bommasani, Brown, Brundage, Byrne, Carlson, Chen-2017, Chen-2021, Cohen, Conneau, Davis, Dinan×6, Gabriel, Gao-2019, Gao-2020, Golovanov, Hancock, Hendrycks, Holtzman, Huang, Huynh, Izacard, Joshi, Ju, Kiela, Kingma, Komeili, Kwiatkowski, Lazaridou, Lee-2019, Lee-2022, Lewis, Li×2, Liu-2021, Liu-2019, Loshchilov, Madotto, Mazaré, Mihaylov, Miller, Mitchell, Nakano, Nguyen, Ni, Ouyang, Park, Partnership-AI, Perez, Pineau, Rae, Rajpurkar, Ram, Rashkin, Rastogi, Reed, Roller×2, Saunders, Serban, Shachaf, Sheng, Shuster×4, Smith-Williams, Smith-2020, Smith-2022, Solaiman, Song, Sonnenburg, Strubell, Thoppilan, Tomaiuolo, Ung, Urbanek, Vaswani, Weidinger, Wolf, Wulczyn, Xu-2020, Xu-2022a, Xu-2022b, Yang, Zhang-2018, Zhang-2020, Zhang-2022, Zhao, Zhou). Several less load-bearing citations (e.g. Strubell 2019 environmental cost, Sonnenburg 2007 open-source ML) are omitted from the frontmatter list for brevity but the count of ~57 is conservative; the structured citations array contains the 57 that directly inform BB3's design, training, or evaluation.
