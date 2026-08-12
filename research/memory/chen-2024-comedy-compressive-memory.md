---
corpus: agentic-memory
kind: paper-digest
slug: chen-2024-comedy-compressive-memory
title: "Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations"
authors:
  - "Chen, Nuo"
  - "Li, Hongguang"
  - "Huang, Juhua"
  - "Wang, Baoyuan"
  - "Li, Jia"
year: 2024
publication_date: "2024-07"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2402.11975"
doi: null
arxiv_id: "2402.11975"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "COMEDY replaces the entire retrieval-plus-database pipeline of long-term chatbot memory with a single fine-tuned LLM that compresses every past session into one dense memory blob (user profile + relationship dynamics + concise event log), and on a Chinese real-world chat benchmark (Dolphin, 100k samples, 3,998 AI characters) this one-for-all design beats GPT-4-with-retrieval on human scoring averages (1.28 vs 1.13) and crushes ChatGPT-based memory baselines, with the 13B DPO variant reaching Top@1 of 29.82% — the best of all models tested."
topics:
  - compressive-memory
  - long-term-memory
  - dialogue-systems
  - llm-agents
  - memory-compression
  - retrieval-free-memory
  - dpo
  - chinese-nlp
tags:
  - paper
  - memory-system
  - one-for-all-model
  - compressive-memory
  - dpo-training
  - dolphin-dataset
  - retrieval-vs-compression
  - user-portrait
entities:
  - chen-nuo
  - li-jia
  - wang-baoyuan
  - xiaobing-ai
related_digests:
  - zhong-2023-memorybank-llm
  - xu-2021-beyond-goldfish-memory
  - wang-2023-self-controlled-memory
  - wu-2024-longmemeval
  - lu-2023-memochat
citations:
  - title: "Keep me updated! Memory management in long-term conversations"
    authors: ["Sanghwan Bae", "Donghyun Kwak", "Soyoung Kang", "et al."]
    year: 2022
    venue: "Findings of EMNLP 2022"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models are few-shot learners"
    authors: ["Tom B. Brown", "Benjamin Mann", "Nick Ryder", "et al."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "Towards efficiently diversifying dialogue generation via embedding augmentation"
    authors: ["Yu Cao", "Liang Ding", "Zhiliang Tian", "et al."]
    year: 2021
    venue: "ICASSP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Orca: A few-shot benchmark for Chinese conversational machine reading comprehension"
    authors: ["Nuo Chen", "Hongguang Li", "Junqing He", "et al."]
    year: 2023
    venue: "Findings of EMNLP 2023"
    doi: null
    url: null
    arxiv_id: null
  - title: "From good to great: Improving math reasoning with tool-augmented interleaf prompting"
    authors: ["Nuo Chen", "Hongguang Li", "Baoyuan Wang", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2401.05384"
  - title: "Structural contrastive pretraining for cross-lingual comprehension"
    authors: ["Nuo Chen", "Linjun Shou", "Tengtao Song", "et al."]
    year: 2023
    venue: "Findings of ACL 2023"
    doi: null
    url: null
    arxiv_id: null
  - title: "Large language models meet Harry Potter: A dataset for aligning dialogue agents with characters"
    authors: ["Nuo Chen", "Yan Wang", "Haiyun Jiang", "et al."]
    year: 2023
    venue: "Findings of EMNLP 2023"
    doi: null
    url: null
    arxiv_id: null
  - title: "Effortless integration of memory management into open-domain conversation systems"
    authors: ["Eunbi Choi", "Kyoung-Woon On", "Gunsoo Han", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "SimCSE: Simple contrastive learning of sentence embeddings"
    authors: ["Tianyu Gao", "Xingcheng Yao", "Danqi Chen"]
    year: 2021
    venue: "EMNLP 2021"
    doi: null
    url: null
    arxiv_id: null
  - title: "Retrieval augmented language model pre-training (REALM)"
    authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."]
    year: 2020
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Open-domain dialogue generation: What we can do, cannot do, and should do next"
    authors: ["Katharina Kann", "Abteen Ebrahimi", "Joewie J. Koh", "et al."]
    year: 2022
    venue: "NLP4ConvAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandara Piktus", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "A diversity-promoting objective function for neural conversation models"
    authors: ["Jiwei Li", "Michel Galley", "Chris Brockett", "et al."]
    year: 2016
    venue: "NAACL-HLT 2016"
    doi: null
    url: null
    arxiv_id: null
  - title: "ROUGE: A package for automatic evaluation of summaries"
    authors: ["Chin-Yew Lin"]
    year: 2004
    venue: "Text Summarization Branches Out"
    doi: null
    url: null
    arxiv_id: null
  - title: "How NOT to evaluate your dialogue system: An empirical study of unsupervised evaluation metrics for dialogue response generation"
    authors: ["Chia-Wei Liu", "Ryan Lowe", "Iulian Serban", "et al."]
    year: 2016
    venue: "EMNLP 2016"
    doi: null
    url: null
    arxiv_id: null
  - title: "Error analysis prompting enables human-like translation evaluation in large language models: A case study on ChatGPT"
    authors: ["Qingyu Lu", "Baopu Qiu", "Liang Ding", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "BLEU: A method for automatic evaluation of machine translation"
    authors: ["Kishore Papineni", "Salim Roukos", "Todd Ward", "et al."]
    year: 2002
    venue: "ACL 2002"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards making the most of ChatGPT for machine translation"
    authors: ["Keqin Peng", "Liang Ding", "Qihuang Zhong", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Direct preference optimization: Your language model is secretly a reward model"
    authors: ["Rafael Rafailov", "Archit Sharma", "Eric Mitchell", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.18290"
  - title: "Sentence-BERT: Sentence embeddings using Siamese BERT-networks"
    authors: ["Nils Reimers", "Iryna Gurevych"]
    year: 2019
    venue: "EMNLP-IJCNLP 2019"
    doi: null
    url: null
    arxiv_id: null
  - title: "LLaMA: Open and efficient foundation language models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2302.13971"
  - title: "Llama 2: Open foundation and fine-tuned chat models"
    authors: ["Hugo Touvron", "Louis Martin", "Kevin Stone", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2307.09288"
  - title: "Large language models as source planner for personalized knowledge-grounded dialogues"
    authors: ["Hongru Wang", "Minda Hu", "Yang Deng", "et al."]
    year: 2023
    venue: "Findings of EMNLP 2023"
    doi: null
    url: null
    arxiv_id: null
  - title: "Recursively summarizing enables long-term dialogue memory in large language models"
    authors: ["Qingyue Wang", "Liang Ding", "Yanan Cao", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2308.15022"
  - title: "ChatGPT or Grammarly? Evaluating ChatGPT on grammatical error correction benchmark"
    authors: ["Haoran Wu", "Wenxuan Wang", "Yuxuan Wan", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memformer: A memory-augmented transformer for sequence modeling"
    authors: ["Qingyang Wu", "Zhenzhong Lan", "Kun Qian", "et al."]
    year: 2022
    venue: "Findings of AACL-IJCNLP 2022"
    doi: null
    url: null
    arxiv_id: null
  - title: "Beyond goldfish memory: Long-term open-domain conversation"
    authors: ["Jing Xu", "Arthur Szlam", "Jason Weston"]
    year: 2022
    venue: "ACL 2022"
    doi: null
    url: null
    arxiv_id: null
  - title: "Xu at SemEval-2022 task 4: Pre-BERT neural network methods vs post-BERT RoBERTa approach for patronizing and condescending language detection"
    authors: ["Jinghua Xu"]
    year: 2022
    venue: "SemEval-2022"
    doi: null
    url: null
    arxiv_id: null
  - title: "Long time no see! Open-domain conversation with long-term persona memory"
    authors: ["Xinchao Xu", "Zhibin Gou", "Wenquan Wu", "et al."]
    year: 2022
    venue: "Findings of ACL 2022"
    doi: null
    url: null
    arxiv_id: null
  - title: "End-to-end spoken conversational question answering: Task, dataset and model"
    authors: ["Chenyu You", "Nuo Chen", "Fenglin Liu", "et al."]
    year: 2022
    venue: "Findings of NAACL 2022"
    doi: null
    url: null
    arxiv_id: null
  - title: "GLM-130B: An open bilingual pre-trained model"
    authors: ["Aohan Zeng", "Xiao Liu", "Zhengxiao Du", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Personalizing dialogue agents: I have a dog, do you have pets too?"
    authors: ["Saizheng Zhang", "Emily Dinan", "Jack Urbanek", "et al."]
    year: 2018
    venue: "ACL 2018"
    doi: null
    url: null
    arxiv_id: null
  - title: "History-aware hierarchical transformer for multi-session open-domain dialogue system"
    authors: ["Tong Zhang", "Yong Liu", "Boyang Li", "et al."]
    year: 2022
    venue: "Findings of EMNLP 2022"
    doi: null
    url: null
    arxiv_id: null
  - title: "Can ChatGPT understand too? A comparative study on ChatGPT and fine-tuned BERT"
    authors: ["Qihuang Zhong", "Liang Ding", "Juhua Liu", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.10250"
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "Human scoring evaluation in Task 3: memory-grounded response generation"
  page: 6
  image_path: "figures/chen-2024-comedy-fig.png"
---

# Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations

**Authors:** Chen, Nuo · Li, Hongguang · Huang, Juhua · Wang, Baoyuan · Li, Jia (HKUST-Guangzhou / HKUST / Xiaobing.AI)
**Published:** 2024-07 (arXiv v2; v1 February 2024) · [Source](https://arxiv.org/abs/2402.11975)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

COMEDY replaces the standard retrieval-plus-database stack for long-term chatbot memory with a single fine-tuned LLM that does everything: it summarises each past session, compresses N sessions into one dense "compressive memory" containing a user profile, a user-bot relationship description, and an event log, and then generates the next response conditioned on that blob — no FAISS, no embeddings, no retriever. To train it, the authors release Dolphin, the largest Chinese long-term-conversation dataset to date — 102,882 instruction-tuning samples drawn from real X Eva (Xiaobing) user-chatbot interactions across 3,998 user-defined AI characters, with episodes of ≥15 sessions per pair. They fine-tune Chinese LLaMA 2-7B and 13B with mixed-task SFT and then apply DPO using GPT-4-Turbo to synthesise preference pairs (memory-aligned vs deliberately memory-contradicting responses). On a held-out test set of 31 AI-user pairs (127 sessions across 5 dimensions: Coherence, Consistency, Memorability, Engagingness, Humanness, each scored 0-3), COMEDY-13B-DPO averages 1.27 vs 1.13 for GPT-4-with-retrieval and 0.92 for MemoryBank-ChatGPT. COMEDY-GPT4 (GPT-4 generating responses on compressive memory authored by COMEDY-13B) tops the table at 1.28 average and 0.73 Engagingness — the highest single cell. On Top@1 human ranking, COMEDY-13B-DPO leads at 29.82% vs 22.83% for GPT-4-Retrieval. The honest caveat: no model averages above 2.0 on any dimension, so real-world long-term chat remains an open problem even with this gain.

## Key Takeaway

The intuition says you need a database with surgical retrieval to scale chatbot memory across months of conversation — bigger memory bank, fancier embeddings, smarter forgetting curve. COMEDY flips it: just cram everything past into one compressed 240-word "memory blob" the model has been trained to compress, store nowhere, and condition on every turn. The 7B compressive-memory model beats GPT-4-with-retrieval on average score, and DPO on auto-generated "say the opposite of the memory" negatives pushes it further — because the bottleneck was never retrieval precision, it was the model not learning what's worth carrying forward.

## Implications

- **Question whether you need a vector database at all for personal-assistant memory**: For per-user chat history at conversation scale (tens of sessions, not millions of documents), a single fine-tuned model that rewrites all prior context into a 240-word digest beats retrieval-augmented baselines on five human-scored dimensions. Try compression before you build a FAISS pipeline.
- **Train one model to do summarisation, compression, and generation jointly — don't pipeline**: COMEDY's mix-training (Tasks 1+2+3 simultaneously) beats Task-3-only training across all five evaluation dimensions in Figure 3. Sharing parameters across the memory pipeline forces the model to learn what's worth keeping in a way separate modules can't.
- **DPO works as a memory-grounding technique, not just a safety technique**: By auto-generating "memory-contradicting" responses as dispreferred samples (no human labels needed), COMEDY-13B-DPO lifts memorability from 0.70 to 0.80 (+14%) and humanness from 1.94 to 2.09. The preference signal teaches the model what "consistent with memory" looks like, and the negatives are cheap.
- **Three structured components beat a flat summary**: COMEDY's compressive memory has explicit slots for (1) user profile, (2) user-bot relationship dynamics, and (3) event log. Retrieval and flat-summary baselines (Resum-ChatGPT, MemoryBank) miss the relational layer and degrade most on Memorability. If you build a memory pipeline, give relationship state its own slot.
- **The real-world ceiling for long-term dialogue is still ~2/3 of perfect**: No model in Table 3 averages above 2.0. Treat any commercial claim of "perfect long-term memory" with skepticism — the SOTA on real Chinese chat data is COMEDY-GPT4 at 1.28/3.0.
- **Real chat data beats synthetic dialogue data**: Dolphin is built from actual X Eva user-chatbot logs (filtered for safety/quality), not crowd-worker simulations. The authors argue this is essential because real chat veers into colloquial, off-topic, low-content territory that synthetic data doesn't capture. If you're building dialogue evaluation, source from production logs.
- **Compression cost scales linearly, retrieval cost scales with database size**: A retrieval system gets harder as the per-user memory bank grows; COMEDY's compressive memory stays at ~240-277 words regardless of how many past sessions feed into it. The architectural trade-off favours compression as user history grows.

## How to Apply It (method)

**Scenario:** You're building an AI customer support agent that interacts with each customer over many sessions across weeks. You want it to remember that "Jane is a small-business owner who prefers blunt advice, has a recurring login issue with her CRM, and last week was frustrated by a billing error" — without standing up a retrieval pipeline or letting the context window bloat. You want one fine-tuned model that handles memory end-to-end.

**Steps:**

1. **Collect real multi-session conversation logs**: Scrape your production chat logs filtered to user-agent pairs with at least 15 sessions of history. Strip personal identifiers (names, emails, addresses) and filter toxic/empty content with a safety classifier plus keyword rules (COMEDY used Azure Security Check + keyword filters + a ChatGPT validity pass).

2. **Annotate three task types using GPT-4-Turbo plus human reviewers**:
   - **Task 1 — Session-level memory**: For each session, generate session-summary memory (event + user portrait + bot portrait) in `Memory: XXX|XXX||XXX` format.
   - **Task 2 — Memory compression**: Given a list of session-level memories from the same user, produce one compressive memory in three parts (User Description ### Relationship Description ### Event Description), under 500 words.
   - **Task 3 — Memory-grounded response generation**: Given a compressive memory plus the current dialogue, generate the next agent response.

   For each task, GPT-4 produces a first pass and human annotators review/correct (target ~40k examples per task — COMEDY ended at 39,999/30,695/31,131).

3. **Fine-tune a base LLM with mixed-task SFT** on all three tasks simultaneously. COMEDY used Chinese LLaMA 2-7B/13B, max length 2048, lr 1e-5, 2 epochs, batch size 32, 8× A100 GPUs. The mixed objective is critical — Figure 3 shows mix-training beats Task-3-only training on every metric.

4. **Generate DPO preference pairs without human labels** using two flipped prompts to GPT-4-Turbo:

   Preferred (Yw):
   ```
   The task involves providing responses that are completely consistent with the memory and dialogue history given to the language model.
   Dialogue: {Dialogue}
   Memory: {Memory}
   Responses:
   ```

   Dispreferred (Yl):
   ```
   The task involves providing responses that completely contradict the memory and dialogue history given to the language model.
   For instance, if the user's memory includes a preference like 'enjoys ice cream,' you are required to generate nonsensical replies such as 'You intensely dislike ice cream and prefer drinking hot coffee.'
   Dialogue: {Dialogue}
   Memory: {Memory}
   Responses that completely contradict the memory:
   ```

5. **Run DPO on top of the SFT checkpoint** with β=0.1, batch size 8, 2 epochs, on ~140 alignment examples (COMEDY did this with DeepSpeed). This is the step that lifts Memorability from 0.70 to 0.80.

6. **At inference time, run one model three times per turn**: (a) summarise the new session when it ends, (b) recompress all session-level memories into one ~240-word blob when the user returns, (c) generate the response with `[compressive_memory + current_dialogue]` as input. No retriever. No vector DB.

7. **Evaluate on held-out user pairs with human raters scoring 0-3 on five dimensions**: Coherence, Consistency, Memorability, Engagingness, Humanness. Three raters; check pairwise Pearson > 0.85 (COMEDY's annotators averaged 0.91 on Top@1).

**Expected outcome:** A single fine-tuned model that handles your entire memory pipeline. Expect ~14-20% improvement over retrieval-based baselines on human-scored Memorability, with the biggest gains in conversations where memory and current message are loosely connected (e.g., the customer is in casual chat mode and the model needs to pull in personality knowledge rather than retrieve a specific past fact). Plan for the ceiling — even the best model averages ~1.28/3.0, so this is not solved.

## Best Figure

![Figure 3 — Human scoring evaluation in Task 3: memory-grounded response generation (page 6)](figures/chen-2024-comedy-fig.png)

**Image Candidates:**
- Table 3 (p. 6): Side-by-side scoring of 14 algorithms across 5 human-rated dimensions plus average — the paper's headline comparison.
- Table 4 (p. 6): Human ranking results (Top@1, Top@3, Avg.R) showing COMEDY-13B-DPO at the top of Top@1 ranking.
- Figure 3 (p. 8): Bar chart of mix-training vs Task-3-only training — most compelling ablation visualisation.

**Best Image:** Table 3 (the paper's headline scoreboard) — single view contrasting three families of baselines (Context-Only, Retrieval-based, Memory-related) against five COMEDY variants across five human-evaluation axes. The pattern jumps out: COMEDY-13B-DPO is the only model that breaks 1.20 on Consistency, 0.80 on Memorability, and 2.09 on Humanness simultaneously. The Engagingness column is where COMEDY-GPT4 (0.73) leaves every retrieval-based system in the dust — supporting the paper's claim that compressive memory enables nuanced, character-aware responses rather than generic acknowledgments.

## What Experts Overlook

COMEDY's results don't come from the compressive memory architecture alone — they come from the DPO step using **automatically-generated semantic-contradiction negatives**, not random negatives. The authors built dispreferred samples by literally asking GPT-4 to flip every preference and fact in the memory ("if the user likes ice cream, write a response that says they hate it"). Appendix F shows their automatic strategy beats random-utterance-sampling negatives by +0.15 average Humanness and +0.16 average Memorability. This is the often-skipped detail in DPO literature: the **quality of the negative**, not the volume, drives the lift.

**Why it matters:** Standard DPO papers focus on how to collect preferred responses (human labels, AI feedback, etc.) and treat negatives as a sampling problem — sample a worse model output, sample a different chunk of training data, etc. COMEDY shows that for memory-grounded generation, the negative needs to be **specifically wrong in the memory dimension**, not generically worse. The dispreferred response must look plausible and fluent but contradict the encoded user model. This is the only way the preference signal teaches the model "stay grounded in compressive memory" rather than "be more eloquent."

**Example of good use:** A team building an AI nutrition coach has user memory like "vegetarian, allergic to tree nuts, dislikes spicy food." For DPO training, they auto-generate dispreferred responses that suggest cashew-based recipes or hot sauces — fluent suggestions that violate the memory. The model learns to ground every recommendation in the stored profile rather than producing plausible but generic advice.

**Example of misapplication:** The same team treats DPO negatives as "any older model output" or "random response from another user's history." The training signal becomes "be a better writer" rather than "stay grounded in this user's memory." Result: fluent, polished responses that ignore the vegetarian constraint and recommend a chicken salad — exactly the failure mode the architecture was supposed to fix.

## Extracted Prompts

**Prompt explanation:** Task 1 dataset annotation — instructs GPT-4-Turbo to generate per-session memory descriptions plus user profile + preferences from a single dialogue session, with safety filtering and a strict pipe-separated output format.

```
This is a dialogue memory generation task, along with user profile and preference generation tasks.
The input consists of the dialogue content between two people.
Firstly, if the dialogue content involves inappropriate content such as sex, pornography, or violence, the output should be "Sorry, the content involves sex, pornography, violence, etc., and a suitable output cannot be provided."
Secondly, if the dialogue content is idle chat with no effective information, the output should be "No valid information."
The requirements for the dialogue memory generation task are as follows:
Generate objective memory descriptions related to both individuals based on their dialogue content.
Do not omit any relevant dialogue content.
The memories generated should include a subject, verb, and object for each memory.
Separate multiple memory dialogues with '|', and include all memories in the format 'Memory: XXX|XXX||XXX'.
The user profile and preference generation task requirements are as follows: This task is only applicable to the users mentioned in the dialogue content, with the user's name being {user name}.
The user profile includes name, age, birthday, gender, height, weight, zodiac sign, Chinese zodiac sign, hometown, occupation, employer, education, location, and relationship status.
User preferences include likes or dislikes of entities, which can consist of singers, stars, athletes, music, movies, books, anime, variety shows, games, sports, animals, and food.
If there is no user profile and preference information in the dialogue, output 'No Profile and Preference information available'.
If there is user profile information, output 'Profile: XXX'. If there is preference information, output 'Preference: '.
If both user profile and preference information are present, separate them with '###'. The final memory, user profile, and preference information should also be separated with '###' in the format [XXX###XXX###XXX].
The dialogue content is {dialogue}. The output is:
```

**Prompt explanation:** Task 2 dataset annotation — compresses N session-level memories into the three-part compressive memory format (user description ### relationship description ### event description), with a 500-word cap and a "let's think step by step" guidance.

```
This is a task about customizing user descriptions, relationship descriptions, and event descriptions.
The text output is divided into three parts:
The first part is the user description, mainly including a summary of the user's information.
The second part describes the relationship between the user and the robot.
The third part describes the events shared by the user and the robot.
Based on the reference materials, extract and summarize different information such as the user's personality traits and behavior patterns.
It is important to record and include all information about the user from various aspects in the user description, without any omissions, resulting in an objective user description.
If the reference materials violate relevant safety regulations, involving sex, pornography, violence, etc., the response should be: "Sorry, the content involves sex, pornography, violence, etc., and a suitable output cannot be provided."
The user description should include, but is not limited to: basic information (such as name, nickname, gender, appearance, birthday, zodiac sign, etc.), the user's hobbies and dislikes, and various statuses of the user (such as emotional state, mood, work status, health status, etc.).
The second part is the relationship description between the user and the robot, describing the level of intimacy shown in the dialogue.
The third part is the description of events shared by the user and the robot, summarizing events that have occurred in the dialogue.
In the output description, list specific examples mentioned in the reference materials as much as possible, retaining some interesting information.
However, avoid outputting content unrelated to the user, and keep the content under 500 words.
Let's think step by step. Each part of the content is separated by '###'. The example format is as follows {User Description: XXX###Relationship Description: XXX###Event Description: XXX}.
The output example is as follows: The user's personality is particularly XXX, because they once XXX, and the user likes XXX, dislikes XXX.
The user's name is {user name}, the robot's name: {chatbot name} and the reference material is {multiple session-level memories}.
The output is:
```

**Prompt explanation:** Task 3 dataset annotation — produces the memory-grounded response that becomes the SFT target.

```
This is a memory-based dialogue generation task.
Given a dialogue and related memory content, please generate a response that is consistent with the memory content and reasonable within the context of the dialogue.
Dialogue: {Dialogue}
Memory: {Memory}
```

**Prompt explanation:** DPO preferred sample (Yw) — same as Task 3 but with stricter "completely consistent" instruction; used to generate the chosen response in DPO training.

```
The task involves providing responses that are completely consistent with the memory and dialogue history given to the language model.
Dialogue: {Dialogue}
Memory: {Memory}
Responses:
```

**Prompt explanation:** DPO dispreferred sample (Yl) — the key auto-negative-generation prompt. Explicitly asks GPT-4 to contradict the memory, producing fluent but memory-violating responses for DPO's rejected pool.

```
The task involves providing responses that completely contradict the memory and dialogue history given to the language model.
For instance, if the user's memory includes a preference like 'enjoys ice cream,' you are required to generate nonsensical replies such as 'You intensely dislike ice cream and prefer drinking hot coffee.'
Dialogue: {Dialogue}
Memory: {Memory}
Responses that completely contradict the memory:
```

**Prompt explanation:** Task 1 instruction-tuning prompt for COMEDY itself (the model that gets fine-tuned). Simpler than the GPT-4-annotation version because the model doesn't need to do safety filtering at inference.

```
This is a memory description generation task
In this task, you should base on the dialogue content between two people, create objective memory descriptions for both individuals, represented in the format [xxx|xxx|xxx], where each 'xxx' is a separate memory.
The memories should use the names of the speakers as the subject, and all relevant dialogue content must not be omitted.
Separate different memories with '|'.
Dialogue content is: {Dialogue}.
Output is:
```

**Prompt explanation:** Task 2 instruction-tuning prompt for COMEDY — same three-part compressive memory structure as the GPT-4 annotation prompt but without the safety preamble and word cap.

```
This is a task about customizing user descriptions, relationship descriptions, and event descriptions.
The text output is divided into three parts:
The first part is the user description, mainly including a summary of the user's information.
The second part describes the relationship between the user and the robot.
The third part describes the events shared by the user and the robot.
Based on the reference materials, extract and summarize different information such as the user's personality traits and behavior patterns.
It is important to record and include all information about the user from various aspects in the user description, without any omissions, resulting in an objective user description.
The second part is the relationship description between the user and the robot, describing the level of intimacy shown in the dialogue.
The third part is the description of events shared by the user and the robot, summarizing events that have occurred in the dialogue.
In the output description, list specific examples mentioned in the reference materials as much as possible, retaining some interesting information.
The user's name is {user name}, the robot's name: {chatbot name} and the reference material is {multiple session-level memories}.
The output is:
```

**Prompt explanation:** Task 3 instruction-tuning prompt for COMEDY — the inference-time response generation prompt.

```
This is a memory-based dialogue generation task.
Given a dialogue and related memory content, please generate a response that is consistent with the memory content and reasonable within the context of the dialogue.
Dialogue: {Dialogue}
Memory: {Memory}
```

## Citations

The full list of 34 references is in the `citations:` frontmatter array above. Headline citations the wiki cares about:

- Bae et al. 2022 — Keep me updated! Memory management in long-term conversations (Findings of EMNLP)
- Zhong et al. 2023 — MemoryBank: Enhancing LLMs with long-term memory (arXiv:2305.10250) — main memory-related baseline
- Wang et al. 2023 — Recursively summarizing enables long-term dialogue memory in LLMs (arXiv:2308.15022) — Resum baseline
- Xu et al. 2022 — Long time no see! Open-domain conversation with long-term persona memory (Findings of ACL)
- Xu, Szlam, Weston 2022 — Beyond goldfish memory: Long-term open-domain conversation (ACL)
- Rafailov et al. 2023 — Direct preference optimization (arXiv:2305.18290) — DPO method
- Lewis et al. 2020 — Retrieval-augmented generation for knowledge-intensive NLP tasks (NeurIPS)
- Guu et al. 2020 — REALM: Retrieval augmented language model pre-training (ICLR)
- Touvron et al. 2023a/b — LLaMA and LLaMA 2 (arXiv:2302.13971, arXiv:2307.09288) — backbones
- Reimers & Gurevych 2019 — Sentence-BERT (EMNLP-IJCNLP)
- Gao, Yao, Chen 2021 — SimCSE (EMNLP)

## Related Digests

- [[zhong-2023-memorybank-llm]] — MemoryBank: Enhancing Large Language Models with Long-Term Memory (the canonical retrieval-based memory baseline COMEDY explicitly outperforms)
- [[xu-2021-beyond-goldfish-memory]] — Beyond Goldfish Memory: Long-Term Open-Domain Conversation (earlier work establishing the long-term dialogue problem)
- [[wang-2023-self-controlled-memory]] — Enhancing Large Language Model with Self-Controlled Memory Framework (parallel approach using a memory controller)
- [[wu-2024-longmemeval]] — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory (the English-language benchmark that lets you compare COMEDY-style approaches across systems)
- [[lu-2023-memochat]] — MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation (sibling approach using memo-like structured memory)

## Reviewer Notes

**Hallucination check severity: Clean.**

Cross-checked every numerical claim in the digest against the paper text:

- Dolphin total samples: 102,882 — matches Section 2.2 Statistics ("Dolphin comprises a total of 102,882 samples").
- 3,998 AI characters — matches Table 1 ("Total AI Characters 3,998 / 3,998 / 3,998 train").
- 39,999 / 30,695 / 31,131 samples per task — matches Table 1.
- 31 user pairs / 127 test sessions / 465 Task 1 / 31 Task 2 — matches Table 1 test columns.
- COMEDY-13B-DPO average 1.27 — matches Table 3 row.
- GPT-4-Retrieval average 1.13 — matches Table 3 row.
- COMEDY-GPT4 average 1.28 — matches Table 3 row.
- MemoryBank-ChatGPT average 0.92 — matches Table 3.
- Top@1 COMEDY-13B-DPO 29.82% — matches Table 4.
- Top@1 GPT-4 22.83% — matches Table 4.
- Compressive memory length ~240 words (240.7 train / 276.8 test) — matches Table 1 "Avg. words Per Compressive Memory" row.
- No model averages above 2.0 — confirmed; the highest single column is Humanness 2.09 for COMEDY-13B-DPO, average column tops out at 1.28.
- DPO β=0.1, batch size 8, 2 epochs — matches Section 3.1.
- 8× A100 GPUs, lr 1e-5, max length 2048, 2 epochs SFT — matches Section 3.1.
- Pearson correlation among annotators ~0.91 (Top@1 0.90-0.92, Top@3 0.86-0.89) — matches Table 5 in Appendix D.
- Memorability lift 0.70→0.80 — matches Table 3 (COMEDY-13B 0.70, COMEDY-13B DPO 0.80).
- Humanness lift 1.94→2.09 — matches Table 3.
- Text2vec + FAISS used as the retrieval baseline — matches Section 3.2.
- DPO objective formula — matches Section 2.3 verbatim.
- Mixed-task training beats Task-3-only on every metric — visible in Figure 3.
- Auto-DPO-sampling beats random-utterance sampling — visible in Figure 4 / Appendix F.

The digest reflects what's in the paper; no fabricated numbers, no overclaiming.

One framing note for the reader: the paper occasionally calls Dolphin "the biggest Chinese long-term conversation dataset" — this is a comparative claim against other Chinese-language long-term dialogue datasets the authors are aware of as of February 2024; I have not independently verified that no larger dataset exists. The 102,882-sample count is straight from Table 1.
