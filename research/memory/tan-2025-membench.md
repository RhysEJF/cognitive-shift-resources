---
corpus: agentic-memory
kind: paper-digest
slug: tan-2025-membench
title: "MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents"
authors:
  - "Tan, Haoran"
  - "Zhang, Zeyu"
  - "Ma, Chen"
  - "Chen, Xu"
  - "Dai, Quanyu"
  - "Dong, Zhenhua"
year: 2025
publication_date: "2025-06"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2506.21605"
doi: null
arxiv_id: "2506.21605"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Most published LLM-agent memory mechanisms (MemGPT, MemoryBank, GenerativeAgent, SCMemory) collapse to near-baseline accuracy once context grows past ~100k tokens, while a plain retrieval-over-embeddings setup keeps climbing — suggesting the field has been over-engineering memory architectures that don't generalize past the regimes their original papers tested."
topics:
  - llm-agent-memory
  - memory-evaluation
  - long-context-benchmark
  - reflective-memory
  - retrieval-augmented-memory
  - procedural-memory
tags:
  - paper
  - benchmark
  - memory
  - llm-agents
  - dataset
entities:
  - tan-haoran
  - zhang-zeyu
  - chen-xu
  - memgpt
  - memorybank
  - generativeagent
  - scmemory
  - memengine
  - qwen-2-5
  - gpt-4o-mini
related_digests:
  - maharana-2024-locomo
  - wu-2024-longmemeval
citations:
  - title: "L-eval: Instituting standardized evaluation for long context language models"
    authors: ["Chenxin An", "Shansan Gong", "Ming Zhong", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2307.11088"
  - title: "Longbench: A bilingual, multitask benchmark for long context understanding"
    authors: ["Yushi Bai", "Xin Lv", "Jiajie Zhang", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2308.14508"
  - title: "twitter-news"
    authors: ["DataGuy", "Gordon Amoako"]
    year: 2022
    venue: null
    doi: null
    url: null
    arxiv_id: null
  - title: "Large language model agent in financial trading: A survey"
    authors: ["Han Ding", "Yinheng Li", "Junhao Wang", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2408.06361"
  - title: "PerLTQA: A personal long-term memory dataset for memory classification, retrieval, and synthesis in question answering"
    authors: ["Yiming Du", "Hongru Wang", "Zhengyi Zhao", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.16288"
  - title: "ChatGLM: A family of large language models from GLM-130B to GLM-4 All Tools"
    authors: ["Team GLM", "Aohan Zeng", "Bin Xu", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2406.12793"
  - title: "The MovieLens datasets: History and context"
    authors: ["F. Maxwell Harper", "Joseph A. Konstan"]
    year: 2015
    venue: "ACM Transactions on Interactive Intelligent Systems (TiiS) 5(4):1-19"
    doi: null
    url: null
    arxiv_id: null
  - title: "Personal LLM agents: Insights and survey about the capability, efficiency and security"
    authors: ["Yuanchun Li", "Hao Wen", "Weijun Wang", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2401.05459"
  - title: "Evaluating very long-term conversational memory of LLM agents (LoCoMo)"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.17753"
  - title: "Generating personalized recipes from historical user preferences"
    authors: ["Bodhisattwa Prasad Majumder", "Shuyang Li", "Jianmo Ni", "et al."]
    year: 2019
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1909.00105"
  - title: "MemGPT: Towards LLMs as operating systems"
    authors: ["Charles Packer", "Sarah Wooders", "Kevin Lin", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.08560"
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["Joon Sung Park", "Joseph O'Brien", "Carrie Jun Cai", "et al."]
    year: 2023
    venue: "Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology, pages 1-22"
    doi: null
    url: null
    arxiv_id: null
  - title: "Qwen2.5: A party of foundation models"
    authors: ["Qwen Team"]
    year: 2024
    venue: null
    doi: null
    url: null
    arxiv_id: null
  - title: "Item recommendation on monotonic behavior chains"
    authors: ["Mengting Wan", "Julian J. McAuley"]
    year: 2018
    venue: "RecSys 2018, pages 86-94"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fine-grained spoiler detection from large-scale review corpora"
    authors: ["Mengting Wan", "Rishabh Misra", "Ndapa Nakashole", "et al."]
    year: 2019
    venue: "ACL 2019, Volume 1: Long Papers, pages 2605-2610"
    doi: null
    url: null
    arxiv_id: null
  - title: "Enhancing large language model with self-controlled memory framework"
    authors: ["Bing Wang", "Xinnian Liang", "Jian Yang", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2304.13343"
  - title: "A survey on large language model based autonomous agents"
    authors: ["Lei Wang", "Chen Ma", "Xueyang Feng", "et al."]
    year: 2024
    venue: "Frontiers of Computer Science 18(6):186345"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multilingual E5 text embeddings: A technical report"
    authors: ["Liang Wang", "Nan Yang", "Xiaolong Huang", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.05672"
  - title: "LongMemEval: Benchmarking chat assistants on long-term interactive memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2410.10813"
  - title: "A survey on large language models for recommendation"
    authors: ["Likang Wu", "Zhi Zheng", "Zhaopeng Qiu", "et al."]
    year: 2024
    venue: "World Wide Web 27(5):60"
    doi: null
    url: null
    arxiv_id: null
  - title: "The rise and potential of large language model based agents: A survey"
    authors: ["Zhiheng Xi", "Wenxiang Chen", "Xin Guo", "et al."]
    year: 2025
    venue: "Science China Information Sciences 68(2):121101"
    doi: null
    url: null
    arxiv_id: null
  - title: "Long time no see! Open-domain conversation with long-term persona memory"
    authors: ["Xinchao Xu", "Zhibin Gou", "Wenquan Wu", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2203.05797"
  - title: "Qwen2 technical report"
    authors: ["An Yang", "Baosong Yang", "Binyuan Hui", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2407.10671"
  - title: "Neural personalized response generation as domain adaptation"
    authors: ["Wei-Nan Zhang", "Qingfu Zhu", "Yifa Wang", "et al."]
    year: 2019
    venue: "World Wide Web 22:1427-1446"
    doi: null
    url: null
    arxiv_id: null
  - title: "A survey on the memory mechanism of large language model based agents"
    authors: ["Zeyu Zhang", "Xiaohe Bo", "Chen Ma", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2404.13501"
  - title: "MemSim: A Bayesian simulator for evaluating memory of LLM-based personal assistants"
    authors: ["Zeyu Zhang", "Quanyu Dai", "Luyu Chen", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2409.20163"
  - title: "MemEngine: A unified and modular library for developing advanced memory of LLM-based agents"
    authors: ["Zeyu Zhang", "Quanyu Dai", "Xu Chen", "et al."]
    year: 2025
    venue: "Companion Proceedings of the ACM on Web Conference 2025, pages 821-824"
    doi: null
    url: null
    arxiv_id: null
  - title: "A survey of large language models"
    authors: ["Wayne Xin Zhao", "Kun Zhou", "Junyi Li", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2303.18223"
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "et al."]
    year: 2024
    venue: "AAAI Conference on Artificial Intelligence, Vol. 38, pages 19724-19731"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 5
  title: "Accuracy of SCMemory, MemGPT, GenerativeAgent, and RecentMemory as memory tokens increase"
  page: 7
  image_path: "figures/tan-2025-membench-fig.png"
---

# MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents

**Authors:** Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu Dai, Zhenhua Dong
**Published:** 2025-06 · [Source](https://arxiv.org/abs/2506.21605)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

MemBench is a new benchmark from Renmin University and Huawei Noah's Ark Lab built to fix three gaps in prior LLM-agent memory evaluations: they tested only one scenario (the user-agent dialogue), only one level (factual recall), and only one metric (accuracy). The dataset spans 500 user-relation graphs, ~65k sessions across two scenarios (participation = the agent is a chat partner; observation = the agent is a silent message-recorder), two memory levels (factual = explicit attributes; reflective = inferred high-level preferences and emotions), and seven question types including knowledge-update and multi-hop. They benchmark seven memory mechanisms — FullMemory, RecentMemory, RetrievalMemory, GenerativeAgent, MemoryBank, MemGPT, and SCMemory — across four LLMs (Qwen2.5-7B, GPT-4o-mini, Llama-3.1-8B, GLM-4-9B) on two context budgets (10k tokens and 100k tokens). The headline finding: most fancy memory architectures (GenerativeAgent, MemoryBank, MemGPT, SCMemory) drop sharply when context exceeds ~100k tokens — reflective-memory accuracy in the participation scenario collapses from 0.73-0.74 at 10k to 0.20-0.40 at 100k. Only plain RetrievalMemory (multilingual-e5-small embeddings) actually gets *better* at 100k (factual accuracy 0.692 → 0.833, reflective 0.692 → 0.833). MemGPT and MemoryBank are also wildly expensive: MemGPT's read time is 4.5 sec/op vs. RetrievalMemory's 0.04 sec/op; MemoryBank's write time is 8-18 sec/op. The most useful takeaway: when picking a memory backbone for a long-context agent, default to retrieval + good embeddings unless you have a specific reason not to — the complex architectures look good on short-context evals and break under realistic load.

## Key Takeaway

The "smart" memory mechanisms that everyone cites — MemGPT, MemoryBank, GenerativeAgent — actually perform *worse* than a dumb sentence-embedding retrieval over the raw message log once memory grows past 100k tokens, and they cost 50-100× more in latency to do it. The agentic-memory field has been over-engineering on benchmarks that were too short to expose the failure mode: the moment you let context drift past the original test regime, the elaborate forget/consolidate/reflect machinery either drops the answer outside its window (RecentMemory, FullMemory in the LLM's context budget) or hallucinates summaries that lose the key evidence (MemoryBank, GenerativeAgent).

## Implications

- **Default to retrieval-over-embeddings for any agent expected to operate over >50k tokens of accumulated history**: MemBench shows multilingual-e5-small + nearest-neighbour search is the only mechanism that improves (not degrades) when memory grows from 10k to 100k tokens, on both factual (0.692 → 0.833) and reflective (0.692 → 0.833) tasks. If you're picking a memory stack today, start here and only add architecture if you can show it beats this baseline on *your* context length.
- **Distrust memory benchmark claims that only test one scenario or one memory level**: Prior benchmarks (LoCoMo, LongMemEval, PerLTQA) only tested participation scenarios and factual memory — exactly the regime where elaborate mechanisms look good. MemBench's contribution is showing that observation scenarios (agent as silent recorder) and reflective memory (inferred preferences) are where the architectures break. Always ask: does this eval cover both the role and the level of memory my agent actually needs?
- **Budget for write latency, not just read latency**: MemoryBank takes 8-18 seconds per write operation; GenerativeAgent takes ~6 seconds. For a real-time chat agent that ingests messages as they arrive, this means the memory system will become the bottleneck — slower than the LLM call itself. RetrievalMemory writes in 0.026-0.058 seconds.
- **Test reflective memory separately from factual memory**: The paper introduces a useful distinction — factual memory is "user said X" (e.g., "my niece is 28"), reflective memory is "user likes Y at a higher level" (e.g., taste preference = sweet-and-salty, inferred from the list of dishes mentioned). These need separate test suites because the failure modes differ: factual fails on retrieval recall, reflective fails on summarization fidelity. If your agent needs both, evaluate both — don't assume good factual carries over.
- **Capacity decline is a real phenomenon, and it's mechanism-specific**: Figure 5 shows SCMemory and MemGPT both degrade as token count grows in a way that's not just "context full" — it's structural to how those mechanisms compress or page memory. Plan for it: monitor accuracy as a function of accumulated history length in production, not just one-shot benchmarks.
- **The base LLM choice still matters even when you isolate the memory mechanism**: Even holding the memory architecture fixed, switching from Qwen2.5-7B to GPT-4o-mini lifts factual-participation accuracy from 0.647 to 0.736 on FullMemory. Don't credit (or blame) your memory layer without controlling for the base model. The paper's own Table 5 makes this controllable.
- **Knowledge-update is the hardest factual-memory subskill, and it's under-tested**: Aggregative and post-processing questions (where the user retracts/corrects an earlier statement) sit at 0.225-0.275 accuracy even on Sub-dataset 1 — much lower than single-hop (~0.85). If your application requires the agent to track changed facts, build targeted evals for this slice.
- **Observation-scenario data may be the cheapest synthetic memory training corpus available**: Because the dataset construction pipeline (Memsim-derived) only needs user-side messages for observation data, you can scale it ~10× cheaper than dialogue data — and observation scores are systematically higher (0.786-0.883 at 10k) than participation (0.647-0.733), suggesting it's a useful sandbox for pre-training memory components.

## How to Apply It (method)

**Scenario:** You're building an AI workforce manager (e.g., Flow OS) that accumulates per-customer conversation history over weeks and needs to answer questions like "what's the customer's preferred tone for follow-ups?" (reflective) and "what was the deadline they mentioned last Tuesday?" (factual). Before committing to a memory stack, you want to verify which mechanism actually scales past 100k tokens of accumulated history for your real-world question mix.

**Steps:**

1. **Define your memory levels**: For each customer/agent, separate the questions you'll ask into two buckets:
   - *Factual*: explicit facts the user stated (names, dates, decisions, attributes).
   - *Reflective*: inferred higher-level signals (preference for formality, communication style, recurring frustrations).

2. **Define your scenarios**: Decide which of these your agent will operate in (most agents need both):
   - *Participation*: agent is in a dialogue with the user — both sides of the conversation must be stored.
   - *Observation*: agent receives a stream of messages (e.g., monitoring a Slack channel) without responding — only user-side messages are stored.

3. **Build a small evaluation set per category**: For each {scenario × level} combination, write 30-100 grounded test questions with known correct answers, drawn from real or representative customer history. Include the seven factual subtypes (single-hop, multi-hop, comparative, aggregative, post-processing, knowledge-update, single-/multi-session-assistant) and the two reflective subtypes (preference, emotion).

4. **Define noise content to control difficulty**: Use unrelated text (e.g., news articles, like the paper's `DataGuy/twitter-news`) to pad each test trajectory to a target token count. Hold one variant at ~10k tokens and one at ~100k tokens per session, so you can see the capacity curve.

5. **Implement at least three memory mechanisms to compare**:
   - `FullMemory` (concat the entire history into the LLM's context — your ceiling baseline if context fits).
   - `RetrievalMemory` (embed each message with a small multilingual embedding model like `multilingual-e5-small`, store in any vector DB, retrieve top-K at query time).
   - One "smart" architecture you're considering (MemGPT, MemoryBank, Generative-style summarisation, Mem0, etc.).

6. **Score each mechanism on four metrics, not just accuracy**:
   - *Accuracy*: % of multiple-choice / closed-answer questions the agent gets right.
   - *Recall@K*: for retrieval mechanisms, fraction of the time the correct evidence message is in the top-K retrieved.
   - *Capacity*: plot accuracy vs. tokens-in-history (steal the paper's Figure 5 layout — accuracy on the Y axis, tokens on the X axis, with a smoothing line). Look for sharp drops.
   - *Temporal efficiency*: seconds-per-read and seconds-per-write averaged over the full trajectory.

7. **Use the paper's question prompt template** for reflective memory (the version they validated on MemBench):

   ```
   You are an AI assistant specialized in detailed and unbiased persona generation for opinion simulations.
   Based on the dishes/movies/books the user has mentioned in their conversation history, infer their high-level
   <preference attribute> from this list: [Sweet, Salty, Sweet and Salty, Umami, ...].
   Output a single JSON object: {"<attribute>": "<chosen value>"}
   ```

8. **Run head-to-head at both context budgets**: Each candidate mechanism, on each test set, at 10k and 100k. Tabulate accuracy + RT + WT side by side (the paper's Tables 3 and 4 are good visual templates).

9. **Pick the winner with the smallest 10k → 100k accuracy gap**: This is the operational criterion that matters in production — not the peak score at 10k. The paper shows RetrievalMemory often wins on this stability criterion even when it loses absolute accuracy at 10k.

**Expected outcome:** A small reproducible matrix showing exactly which memory backbone you should deploy and at what context budget, plus a capacity curve telling you when to trigger memory consolidation / archival in production. You'll likely confirm the paper's finding that retrieval-over-embeddings is the right default — but the value is in being able to defend the choice with your own numbers rather than papering over it.

## Best Figure

![Figure 5 — Accuracy of SCMemory, MemGPT, GenerativeAgent, and RecentMemory as memory tokens increase (page 7)](figures/tan-2025-membench-fig.png)

**Image Candidates:**
- Figure 5 (p. 7): Side-by-side accuracy-vs-tokens scatter plots for four memory mechanisms — the clearest visual evidence of the "capacity collapse" finding that drives the paper's headline.
- Table 3 (p. 7): The full 7-mechanism × 2-scenario × 2-budget accuracy + efficiency matrix; tells the whole story but is dense.
- Figure 4 (p. 5): Pie + bar charts of question category and answer distribution; useful for understanding the dataset balance but doesn't show results.

**Best Image:**
**Figure Name:** Figure 5: "The accuracy of SCMemory (top-left), MemGPT (top-right), GenerativeAgent (bottom-left) and RecentMemory (bottom-right) as the memory token increases"
**Figure Page:** 7
**Slide Caption:** Memory-mechanism accuracy degrades sharply as accumulated tokens grow past ~100k — the empirical core of MemBench's "capacity collapse" finding.
**Description:** Figure 5 plots accuracy on the Y axis against memory tokens (0 to ~140k) on the X axis for four of the seven mechanisms tested — SCMemory, MemGPT, GenerativeAgent, and RecentMemory — using Qwen2.5-7B as the base LLM on Sub-dataset 2 (100k-token observation scenario). Each panel shows hundreds of individual evaluations as scatter points. The pattern is consistent across all four: accuracy is meaningfully higher at the low end of the token range and drops as memory grows, with the largest declines for SCMemory (top-left, dropping from ~0.55 to ~0.40) and MemGPT (top-right, peaking near 0.7 early then settling toward ~0.5). The figure is the paper's most direct visualization of the central claim — that complex memory mechanisms collapse to baseline-or-worse in long-context regimes — and it's exactly the kind of "decline curve" practitioners need to look for in their own evaluations.

## What Experts Overlook

The detail most readers will miss is that **MemBench evaluates `RetrievalMemory` using a tiny, off-the-shelf embedding model — `multilingual-e5-small` (Wang et al., 2024b) — not a proprietary or specially-tuned retriever**. That embedding model is ~118M parameters and freely downloadable. Yet it produces the best accuracy in the 100k-token regime on every dataset configuration: 0.833 on factual-participation, 0.933 on factual-observation, 0.833 on reflective-participation, 0.933 on reflective-observation. The exact line is in Section 4.1 — "all methods that involve retrieval use the multilingual-e5-small for retrieval" — and it's easy to gloss over as a methodological footnote rather than the central engineering insight.

**Why it matters:** The implicit story the paper tells about why retrieval beats the elaborate architectures isn't "retrieval is conceptually superior" — it's "a small, well-trained dense embedder + dot-product search is already strong enough that complex on-top mechanisms have no headroom to add value, and most of them add latency or summarisation loss instead." This reframes the design question for memory systems: the bottleneck is rarely the retrieval algorithm, it's the underlying representation quality. Once you commit to a competent embedder, the elaborate paging/reflection/summarisation layers above it tend to subtract rather than add accuracy.

**Example of good use:** A team building a customer-support agent has 6 months of conversation history per account. Instead of starting with MemGPT-style virtual context management, they index every message with `multilingual-e5-small` (or its newer cousin), store vectors in any boring vector DB (pgvector, LanceDB), retrieve top-20 at inference, and concatenate into the prompt. Latency stays sub-second; accuracy on factual recall is at the paper's 0.83-0.93 range. They only add a "smart" layer (consolidation, periodic summarisation) when they have measured evidence that the embedding-retrieval ceiling is binding for their workload.

**Example of misapplication:** A team reads the paper and concludes "retrieval is best" — then plugs in a low-quality embedder (e.g., a generic `text-embedding-3-small` quantized to 256 dims, or a custom 50-dim model trained on a tiny domain corpus) and gets terrible results. They blame retrieval and pivot to MemGPT, hitting the latency wall the paper documents. They never realize the actual variable was the embedder's representational quality. The lesson buried in "Section 4.1, footnote" is: pick the embedder first, then design memory around it — not the other way around.

## Extracted Prompts

**Prompt explanation:** Profile prompt — extracts a user's high-level taste preference from a list of dishes they've mentioned, used to construct reflective-memory ground-truth.

```
Flavour Reflective Memory Attribute Please choose user's taste from [Tastes] according to the dishes he likes below. [Dishes]:{Dishes} [Tastes]: ["Sweet", "Sour", "Spicy", "Salty", "Umami", "Bitter", "Sweet and Salty", "Sweet and Sour", "Salty and Umami", "Sour and Spicy", "Sweet, Salty, and Spicy", "Sour and Salty", "Sour, Sweet, and Salty", "Salty, Umami, and Spicy", "Numbing and Spicy", "Creamy and Sweet", "Umami and Sweet", "Bitter and Sweet", "Astringent", "Numbing", "Rich and Fatty", "Cool", "Warm and Spicy"] example output:{{'taste': 'sweet'}}
```

**Prompt explanation:** Self-dialogue / role dialogue generation prompt — produces synthetic multi-turn user-assistant conversations based on a structured information object, used to build the participation-scenario dataset.

```
Role Dialogue Generation Prompt. Please generate a {round_length}-round interactive conversion between the user and assistant, with a total of {sentence_length} sentences. The dialogue's main content should based on the given information about the user's {entity}. Ensure that no information beyond what is provided is introduced in the dialogue. **Note that the user cannot ask the assistant for information because the assistant does not know the information.** Note that the assistant is the user's personal assistant, so it should only respond passively to the user's dialogue, but it can reply with varied content. Please return the conversation in a JSON list format as shown in the example, ensuring that the result can be directly parsed by json.loads. **Every json must includes both user and assistant with their words! Every json's format is {{"user": user's words, "assistant": assistant's words}}** #[Information]: {information}
   #example: [{{"user": "I wanted to talk to you about my cousin, Ethan Parker. He's 39 years old.", "assistant": "Certainly! Ethan is 39. Is there something specific you'd like to discuss about him?"}}, ...]
```

**Prompt explanation:** Event dialogue generation prompt — variant of the above that anchors conversation around an event entity rather than a person.

```
Event Dialogue Generation Prompt. Please generate a {round_length}-round interactive conversion between the user and assistant, with a total of {sentence_length} sentences. The dialogue's main content should based on the given information about the {event_name}. Ensure that no information beyond what is provided is introduced in the dialogue. Note that the assistant is the user's personal assistant, so it should only respond passively to the user's dialogue, but it can reply with varied content. Note that the user cannot ask the assistant for information because the assistant does not know the information. You can start with user saying I'm going to attend {event_name} Please return the conversation in a JSON list format as shown in the example, ensuring that the result can be directly parsed by json.loads. #[Information]: {information}
```

**Prompt explanation:** Observation-scenario role message prompt — rewrites a structured fact into a colloquial first-person declarative sentence, used to build observation-scenario message streams.

```
Role Message Prompt. [User Message]: {message} Please rewrite the above user message into a colloquial declarative sentence. Ensure it is smooth and free of grammatical errors, without changing the original information. Only output the rewritten user message, without including the original message. Do not output any other description. Output example: Lucas Grant, who is my boss, has a Master's degree.
```

**Prompt explanation:** Observation-scenario event message prompt — same idea as the role message prompt but for event entities, with the additional constraint of using first-person pronouns ("I/me/my") rather than "you".

```
Event Message Prompt. [User Message]: {message} Please rewrite the above user message into a colloquial declarative sentence. Ensure it is smooth and free of grammatical errors, without changing the original information, and avoid using 'you'. Don't forget use I , me or my Only output the rewritten user message, without including the original message. Do not output any other description. Output example: Climb Fest draws a crowd of around nine hundred people.
```

## Citations

- An et al. (2023) — L-Eval: standardized evaluation for long-context LLMs (arXiv:2307.11088)
- Bai et al. (2023) — LongBench: bilingual multitask benchmark for long-context understanding (arXiv:2308.14508)
- Du et al. (2024) — PerLTQA: personal long-term memory dataset for QA (arXiv:2402.16288)
- Harper & Konstan (2015) — MovieLens datasets: history and context
- Maharana et al. (2024) — LoCoMo: evaluating very long-term conversational memory of LLM agents (arXiv:2402.17753)
- Packer et al. (2023) — MemGPT: towards LLMs as operating systems (arXiv:2310.08560)
- Park et al. (2023) — Generative agents: interactive simulacra of human behavior
- Wang et al. (2023) — Self-Controlled Memory framework for LLMs (arXiv:2304.13343)
- Wu et al. (2024a) — LongMemEval: benchmarking chat assistants on long-term interactive memory (arXiv:2410.10813)
- Zhang et al. (2024b) — MemSim: Bayesian simulator for evaluating memory of LLM-based personal assistants (arXiv:2409.20163)
- Zhang et al. (2025) — MemEngine: unified library for developing memory of LLM-based agents
- Zhong et al. (2024) — MemoryBank: enhancing LLMs with long-term memory (AAAI)

(Full structured list of 29 entries in frontmatter `citations[]`.)

## Related Digests

- [[maharana-2024-locomo]] — Evaluating very long-term conversational memory of LLM agents (the prior benchmark MemBench positions against; participation-only, factual-only)
- [[wu-2024-longmemeval]] — LongMemEval: benchmarking chat assistants on long-term interactive memory (the other direct prior benchmark MemBench positions against)

## Reviewer Notes

**Overall severity:** Clean

Every claim in the digest is directly supported by the paper. Key spot-checks:
- "Reflective accuracy 0.73-0.74 at 10k → 0.20-0.40 at 100k" — supported by Table 4 (FullMemory PS-RM 0.733 → 0.533; GenerativeAgent 0.742 → 0.333; MemoryBank 0.692 → 0.400; MemGPT 0.733 → 0.367; SCMemory 0.542 → 0.267).
- "RetrievalMemory factual 0.692 → 0.833 (10k → 100k)" — Table 3, exact values.
- "MemGPT read 4.549 sec/op; MemoryBank write 8.047 sec/op (and 18.243 sec/op in observation)" — Table 3 values, correctly reported.
- "multilingual-e5-small embedder" — explicitly named in Section 4.1, paragraph 2.
- "Seven memory mechanisms: FullMemory, RecentMemory, RetrievalMemory, GenerativeAgent, MemoryBank, MemGPT, SCMemory" — explicitly listed in Section 4.1, citing MemEngine (Zhang et al., 2025).
- "Four LLMs: Qwen2.5-7B, GPT-4o-mini, Llama-3.1-8B, GLM-4-9B" — Table 5 caption confirms.
- "500 user-relation graphs" — confirmed in Section 3.5: "500 graphs composed of user profiles and profiles of entities".
- "Two scenarios (participation/observation), two memory levels (factual/reflective)" — central design, confirmed throughout Sections 3.2-3.3.
