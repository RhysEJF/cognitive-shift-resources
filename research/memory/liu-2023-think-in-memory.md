---
corpus: agentic-memory
kind: paper-digest
slug: liu-2023-think-in-memory
title: "Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory"
authors:
  - "Lei Liu"
  - "Xiaoyan Yang"
  - "Yue Shen"
  - "Binbin Hu"
  - "Zhiqiang Zhang"
  - "Jinjie Gu"
  - "Guannan Zhang"
year: 2023
publication_date: "2023-11"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2311.08719"
doi: null
arxiv_id: "2311.08719"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Storing LLM-generated reasoning thoughts (subject-relation-object triples + natural-language statements) — rather than raw conversation text — eliminates inconsistent reasoning across repeated recalls, and a Locality-Sensitive Hashing scheme replaces global pairwise similarity with within-group similarity to cut retrieval latency from 0.6287ms to 0.5305ms while supporting three lifecycle operations (insert/forget/merge) on the thought store."
topics:
  - agent-memory
  - long-term-memory
  - llm-evaluation
  - conversational-ai
  - memory-extraction
  - locality-sensitive-hashing
  - thought-storage
  - post-thinking
  - llm-agnostic-memory
tags:
  - paper
  - memory-architecture
  - tim
  - lsh
  - write-time-synthesis
  - cognitive-grounding
entities:
  - liu-lei
  - yang-xiaoyan
  - shen-yue
  - hu-binbin
  - zhang-zhiqiang
  - gu-jinjie
  - zhang-guannan
related_digests:
  - chhikara-2025-mem0
  - zhong-2023-memorybank-llm
  - packer-2023-memgpt-os
citations:
  - title: "ChatGPT"
    authors: ["OpenAI"]
    year: 2022
    venue: "OpenAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "GPT-4 technical report"
    authors: ["OpenAI"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "FinGPT: Open-source financial large language models"
    authors: ["Hongyang Yang", "Xiao-Yang Liu", "Christina Dan Wang"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2306.06031"
  - title: "HuatuoGPT, towards taming language model to be a doctor"
    authors: ["Hongbo Zhang", "Junying Chen", "Feng Jiang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2305.15075"
  - title: "GPTs are GPTs: An early look at the labor market impact potential of large language models"
    authors: ["Tyna Eloundou", "Sam Manning", "Pamela Mishkin", "Daniel Rock"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2303.10130"
  - title: "Large language models are zero-shot reasoners"
    authors: ["Takeshi Kojima", "Shixiang Shane Gu", "Machel Reid", "Yutaka Matsuo", "Yusuke Iwasawa"]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Relational memory-augmented language models"
    authors: ["Qi Liu", "Dani Yogatama", "Phil Blunsom"]
    year: 2022
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "A practical survey on faster and lighter transformers"
    authors: ["Quentin Fournier", "Gaétan Marceau Caron", "Daniel Aloise"]
    year: 2023
    venue: "ACM Computing Surveys"
    doi: null
    url: null
    arxiv_id: null
  - title: "Investigating efficiently extending transformers for long input summarization"
    authors: ["Jason Phang", "Yao Zhao", "Peter J Liu"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2208.04347"
  - title: "Augmenting language models with long-term memory"
    authors: ["Weizhi Wang", "Li Dong", "Hao Cheng", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2306.07174"
  - title: "Improving language models by retrieving from trillions of tokens (RETRO)"
    authors: ["Sebastian Borgeaud", "Arthur Mensch", "Jordan Hoffmann", "et al."]
    year: 2022
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "Kristina Toutanova"]
    year: 2019
    venue: "NAACL-HLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards a human-like open-domain chatbot (Meena)"
    authors: ["Daniel Adiwardana", "Minh-Thang Luong", "David R So", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.09977"
  - title: "Self-consistency improves chain of thought reasoning in language models"
    authors: ["Xuezhi Wang", "Jason Wei", "Dale Schuurmans", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2203.11171"
  - title: "Metacognition"
    authors: ["John Dunlosky", "Janet Metcalfe"]
    year: 2008
    venue: "Sage Publications"
    doi: null
    url: null
    arxiv_id: null
  - title: "Practical and optimal LSH for angular distance"
    authors: ["Alexandr Andoni", "Piotr Indyk", "Thijs Laarhoven", "Ilya Razenshteyn", "Ludwig Schmidt"]
    year: 2015
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "GLM-130B: An open bilingual pre-trained model"
    authors: ["Aohan Zeng", "Xiao Liu", "Zhengxiao Du", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2210.02414"
  - title: "PaLM: Scaling language modeling with pathways"
    authors: ["Aakanksha Chowdhery", "Sharan Narang", "Jacob Devlin", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2204.02311"
  - title: "LLaMa: Open and efficient foundation language models"
    authors: ["Hugo Touvron", "Thibaut Lavril", "Gautier Izacard", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2302.13971"
  - title: "Stanford Alpaca: An instruction-following LLaMA model"
    authors: ["Rohan Taori", "Ishaan Gulrajani", "Tianyi Zhang", "et al."]
    year: 2023
    venue: "Stanford CRFM"
    doi: null
    url: null
    arxiv_id: null
  - title: "LoRA: Low-rank adaptation of large language models"
    authors: ["Edward J Hu", "Yelong Shen", "Phillip Wallis", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2106.09685"
  - title: "Neural turing machines"
    authors: ["Alex Graves", "Greg Wayne", "Ivo Danihelka"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1410.5401"
  - title: "Beyond goldfish memory: Long-term open-domain conversation"
    authors: ["Jing Xu", "Arthur Szlam", "Jason Weston"]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2107.07567"
  - title: "Long time no see! Open-domain conversation with long-term persona memory"
    authors: ["Xinchao Xu", "Zhibin Gou", "Wenquan Wu", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2203.05797"
  - title: "MemoryBank: Enhancing large language models with long-term memory"
    authors: ["Wanjun Zhong", "Lianghong Guo", "Qiqi Gao", "Yanlin Wang"]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2305.10250"
  - title: "Unleashing infinite-length input capacity for large-scale language models with self-controlled memory system (SCM)"
    authors: ["Xinnian Liang", "Bing Wang", "Hui Huang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2304.13343"
  - title: "Leveraging linguistic structure for open domain information extraction (OpenIE)"
    authors: ["Gabor Angeli", "Melvin Jose Johnson Premkumar", "Christopher D Manning"]
    year: 2015
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "KdConv: A Chinese multi-domain dialogue dataset towards multi-turn knowledge-driven conversation"
    authors: ["Hao Zhou", "Chujie Zheng", "Kaili Huang", "Minlie Huang", "Xiaoyan Zhu"]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Baichuan 2: Open large-scale language models"
    authors: ["Aiyuan Yang", "Bin Xiao", "Bingning Wang", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2309.10305"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Overview of TiM framework — recalling, post-thinking, and LSH-indexed long-term memory of inductive thoughts"
  page: 3
  image_path: "figures/liu-2023-think-in-memory-fig.png"
---

# Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory

**Authors:** Lei Liu, Xiaoyan Yang, Yue Shen, Binbin Hu, Zhiqiang Zhang, Jinjie Gu, Guannan Zhang (Ant Group)
**Published:** 2023-11 · [Source](https://arxiv.org/abs/2311.08719)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

TiM (Think-in-Memory) is an LLM-agnostic memory architecture that swaps raw-conversation memory for a hash-indexed store of "inductive thoughts" — natural-language sentences expressing subject-relation-object triples extracted on the write path. The core insight: when memory holds raw Q-R pairs, the LLM must re-reason over the same history on every recall, producing inconsistent reasoning paths (the paper opens with a worked example where two recalls of the same conversation yield $20 and $10 answers to the same question). TiM eliminates this by reasoning ONCE at write time, saving the resulting thoughts, and then recalling those thoughts directly — what the authors frame by analogy with metacognition. The store is a Locality-Sensitive Hashing (LSH) table where the hash function `F(x) = arg max([xR; -xR])` maps embedding vectors into `b/2` groups using a random projection matrix R; similar thoughts collide into the same group, so retrieval calculates pairwise similarity only within one group rather than across the whole memory cache. Memory lifecycle is governed by three operations (insert/forget/merge), each implemented as an LLM prompt template — forget removes contradictory or counterfactual thoughts (Figure 4), merge combines same-entity thoughts (Figure 5). Evaluated against the SiliconFriend/MemoryBank baseline across three datasets (GVD bilingual, KdConv Chinese knowledge-driven, RMD real-world medical), TiM improves response correctness from 0.418 to 0.605 (+44%) on Chinese GVD with ChatGLM and from 0.207 to 0.757 (+266%) on Chinese-Travel KdConv with Baichuan2; retrieval time drops from 0.6287ms to 0.5305ms (~16% faster); contextual coherence improves across the board. A real-world medical-agent deployment (TiM-LLM, Figure 7) demonstrates that without TiM the agent forgets prior symptoms and gives incomplete diagnoses, while TiM enables comprehensive multi-turn symptom recall.

## Key Takeaway

The structural choice that matters in TiM is **moving the reasoning step from query time to write time and persisting its output as memory**, with two enabling pieces: (1) the unit of memory is a self-contained thought (subject-relation-object + natural-language sentence) rather than dialogue text, which makes thoughts atomic and individually addressable; (2) the index is LSH-bucketed not flat-vector, so retrieval is O(group_size) not O(memory_size). The combination — write-time thought distillation + bucketed retrieval — is what later work like Mem0 (2025) and A-Mem (2025) inherit and refine; TiM is the proof-of-concept that LLM-distilled natural-language memories beat raw-text memories on both consistency and retrieval cost. The maintenance operations (insert/forget/merge) are explicitly modelled on Ebbinghaus-style cognitive plausibility, but in practice they're three small prompt templates the LLM agent runs periodically against the store.

## Implications

- **Write-time distillation is the architectural lever** [ENGRAM: Encode + Aggregate]: TiM's central claim is that re-reasoning over raw text on every recall produces inconsistent reasoning paths (Figure 1 worked example shows $20 vs $10 answers diverging from the same history). Persisting the thought itself, not the dialogue, eliminates this category of error. The architectural commitment: do the hard thinking ONCE, on the way in.
- **Inductive thoughts are atomic and individually addressable** [ENGRAM: Encode + Network]: Each thought is a tuple `(H_idx, T)` where T satisfies a relation triple `(E_h, r_i, E_t)` plus the natural-language sentence expressing it. This makes thoughts the retrieval unit — you can insert/forget/merge a single thought without touching its neighbours. Compare to raw-Q-R-pair memory where the granularity is the dialogue turn (which mixes many facts).
- **LSH bucketing replaces global vector similarity with within-group similarity** [ENGRAM: Retrieve]: The hash function `F(x) = arg max([xR; -xR])` with random projection matrix R maps embeddings into b/2 groups; similar vectors get the same hash with high probability. Retrieval becomes two-stage: (1) hash the query to find its bucket, (2) calculate pairwise similarity only within that bucket. Measured at 0.5305ms vs 0.6287ms baseline (memory length 140). The architectural prediction: this gap widens nonlinearly as memory grows — LSH is O(1) lookup + O(bucket_size) similarity vs O(memory_size) flat.
- **Maintenance is a three-operation contract, implemented as LLM prompts** [ENGRAM: Maintain]: Insert (Figure 3 prompt: generate inductive thought from Q-R pair via in-context learning with few-shot examples), Forget (Figure 4 prompt: remove counterfactual/contradictory thoughts from a group), Merge (Figure 5 prompt: combine same-entity thoughts into a denser representation, e.g. "John works as an actor" + "John works as a director" + "John works as a writer" → "John works as an actor, a director, and a writer"). Table 1 makes the operation-coverage comparison explicit: SCM and RelationLM and LongMem support only Insert; MemoryBank adds Forget; TiM adds Merge. The paper frames this as cognitively-motivated (Ebbinghaus forgetting curve, human consolidation) but operationally each op is a prompt template + an LLM call.
- **LLM-agnostic is a portability claim, not just an aesthetic** [ENGRAM: Network]: TiM works with closed-source LLMs (ChatGPT) and open-source (ChatGLM, Baichuan2) because it lives entirely external to the model — no architectural modification, no positional-encoding tricks, no special tokens. Contrast with LongMem (Wang 2023, the "augmenting language models with long-term memory" baseline) which requires LLM-aware token-based memory; TiM moves the integration point above the model boundary. The price: every memory operation is an LLM call (extraction, forget, merge), so you pay inference cost continuously.
- **Top-k recall has a sweet spot** [ENGRAM: Retrieve]: Figure 6 shows retrieval accuracy on KdConv Travel rising from ~0.7 (top-1) to 0.973 (top-10). Top-5 is the default reported in Table 2 results and gives most of the lift; the marginal returns from top-5 to top-10 are small. Practical implication: tune k against context budget — the extra thoughts beyond top-5 are noise more often than signal.
- **Medical domain validates the consistency claim** [ENGRAM: Ground + Aggregate]: The RMD dataset's clinical conversations are the strongest stress test — without TiM, both ChatGLM and Baichuan2 give incomplete diagnoses because they "forget" earlier symptoms; with TiM, both can recall the full symptom history and produce coherent multi-turn diagnoses. The TiM-LLM application (Figure 7) makes this concrete: prior cefuroxime use must be retrieved alongside oral-mucosa symptoms for the agent to suggest fungal infection as an alternative diagnosis. Forgetting in a medical setting is failure-mode-critical.
- **LoRA-tuning the LLM is orthogonal to the memory architecture** [ENGRAM: Encode]: Section 3.5 describes Low-Rank Adaptation (rank r=16, 10 epochs) applied to the base LLM for multi-turn-conversation adaptation. This is an enabler, not part of the memory mechanism — the paper deliberately separates the architecture (TiM) from the LLM training detail. The implication: TiM-style memories should work atop any reasonably-aligned conversational LLM; the fine-tuning is for response quality, not retrieval correctness.

## How to Apply It (method)

**Scenario:** You're building a multi-session conversational AI for a domain where (a) the same history may need to be recalled many times to answer different questions, (b) reasoning over raw history risks inconsistency across recalls (think: medical diagnosis, financial advice, legal Q&A), and (c) you want the memory architecture to be model-agnostic so you can swap the LLM without rewriting the memory layer.

**Steps:**

1. **Define the storage primitive — `(H_idx, T)` tuples**: Each piece of memory is a hash-indexed thought T. T is a natural-language sentence expressing a `(subject, relation, object)` triple — concrete, atomic, and addressable. Don't store dialogue turns; store the distilled facts.

2. **Set up the hash function**: Implement `F(x) = arg max([xR; -xR])` where x is a d-dimensional embedding (from the LLM agent's embedding API or a separate model), R is a fixed random projection matrix of size `(d, b/2)`, and `[u; v]` denotes vector concatenation. b is the number of buckets (the paper doesn't specify a fixed value — tune based on memory scale; common LSH choices: b=64 or 128 for memory caches of a few hundred to a few thousand entries). Similar embeddings collide into the same bucket with high probability.

3. **Wire the post-thinking loop** (the main write path):
   - User sends query Q.
   - Hash Q's embedding to get its bucket; retrieve top-k similar thoughts from that bucket (Section 3.3 stage-2 = pairwise similarity within bucket).
   - Build a recall prompt: "For the current user's question: {Query}, you begin to recall past conversations and the most relevant [memory] is: {Related_memory}. According to the [memory], please answer the question: {Query}."
   - LLM produces response R.
   - **Post-think**: send (Q, R) pair to the LLM with the thought-generation prompt (Figure 3 in the paper — uses in-context learning with examples like "Question: Do you have any company recommendations for me? Response: I recommend Google. → (Company, Recommended, Google). Recommended company is Google.").
   - Hash the new thought and insert it into the bucket.

4. **Run maintenance periodically**:
   - **Forget** (Figure 4 prompt): "Given the following thoughts, please remove the counterfactual thoughts or contradictory thoughts: [thoughts list]." Run periodically per bucket. Example: "The capital of China is Beijing" + "The capital of China is Shanghai" → keep only the first.
   - **Merge** (Figure 5 prompt): "Given the following thoughts, please merge the similar thoughts with the same entity: [thoughts list]." Example: "John works as an actor" + "John works as a director" + "John works as a writer" → "John works as an actor, a director, and a writer." Run per bucket when bucket size exceeds a threshold.
   - Insert is implicit in the post-thinking loop above; the prompt is the same in-context-learning template used at write time.

5. **(Optional) LoRA-tune the base LLM** with rank r=16 for ~10 epochs on your multi-turn dialogue data. The paper uses this for ChatGLM and Baichuan2 to adapt them to multi-turn conversations; it's orthogonal to the memory mechanism but improves base response quality.

6. **At query time**:
   - Generate the query embedding.
   - LSH-hash to find the bucket.
   - Pairwise-similarity within bucket, take top-5 (paper's default).
   - Inject as `{Related_memory}` into the recall prompt, generate response.

7. **Evaluate with three metrics** (per the paper's Section 4.1.4):
   - **Retrieval Accuracy** {0, 1}: was the relevant memory recalled?
   - **Response Correctness** {0, 0.5, 1}: was the answer correct?
   - **Contextual Coherence** {0, 0.5, 1}: did the response naturally connect dialogue context + retrieved memory?
   - The paper uses human evaluation with shuffled predictions to remove model-attribution bias. For automated pipelines, swap in LLM-as-a-Judge but keep the three-metric structure.

**Expected outcome:** On a conversational dataset where prior baselines (raw-text memory like SiliconFriend/MemoryBank) reach ~0.4-0.5 response correctness and 0.4-0.7 contextual coherence, TiM-style memory should push correctness to 0.6-0.85 and coherence to 0.7-0.95 (paper's Table 2 results on GVD/KdConv/RMD). Retrieval latency should drop ~15-30% from flat-vector pairwise baselines (paper measures 0.5305 vs 0.6287ms at memory length 140 — expect this gap to widen with memory scale).

## Best Figure

![Figure 2 — Overview of TiM framework (page 3)](figures/liu-2023-think-in-memory-fig.png)

Image Candidates:
Figure 1 (p. 2): Side-by-side comparison of previous-memory-mechanism vs TiM on a worked arithmetic example, showing how raw-text memory yields inconsistent reasoning ($20 vs $10) while TiM persists the thought "Janet made $18 today" and reuses it without re-reasoning. Best for conveying the *problem*; less good for the architecture.
Figure 2 (p. 3): Overview diagram of the TiM framework with three columns — Conversation History (left), Recalling and Post-thinking pipeline (middle, showing LSH lookup → Response → Post-thinking → LSH insert), and Long-term Memory state before and after (right, showing buckets with inductive thoughts being inserted/merged). Best for conveying the *architecture*.
Figure 7 (p. 9): TiM-LLM medical-agent UI screenshot, showing the application of insert/forget/merge to a clinical conversation; concrete but domain-specific.

Best Image:
Figure Name: Figure 2: "The overview of TiM framework"
Figure Page: 3
Slide Caption: TiM's two-stage loop — recall thoughts from an LSH bucket to answer, then post-think to extract new thoughts and insert them back — is what makes memory grow without context bloat.
Description: Figure 2 has three panels. Left: a Conversation History column shows a multi-turn dialogue ("Do you have any book recommendations?" → "I recommend The Little Prince" → ... → "You recommended a movie before, how about it?"). Middle: the Recalling and Post-thinking pipeline. The user query enters, LSH-hashes to a bucket, the top thought ("Recommend movie is The Wandering Earth") is highlighted in green and pulled into the recall prompt template ("For the current user's question: {Query}, you begin to recall past conversations and the most relevant [memory] is: {Related_memory}..."). The LLM generates a Response ("It is The Wandering Earth. This movie is with stunning visuals."). Then Post-thinking extracts new thoughts ("(The Wandering Earth, have, stunning visuals)" + "'The Wandering Earth' is with stunning visuals.") and feeds them back to LSH for insertion. Right: the Long-term Memory in two states — before, with buckets {0: book recommendations, 1: movie recommendation, 2: song recommendation}, and after, with bucket 1 now containing both the movie recommendation AND the new "stunning visuals" thought (insert/forget/merge label between the two states). The figure compresses the entire architecture into one view: bucketed thought store + bidirectional recall/post-thinking loop.

## What Experts Overlook

TiM's most quietly load-bearing design choice is **the LSH hash function itself** — specifically that `F(x) = arg max([xR; -xR])` is a *signed* concatenation, not just a sign-of-projection hash. Most LSH tutorials describe the simpler "SignProjection LSH" where you take `sign(xR)` to get a binary hash; TiM uses Andoni et al. 2015's "practical and optimal LSH for angular distance" variant where you concatenate `xR` with its negation and take the arg max over `b` dimensions. This means each thought lands in exactly one of `b` buckets (not in `2^b` binary codes), so the bucket size is controllable and bounded — critical for the second-stage pairwise similarity to stay cheap.

**Why it matters:** If you used a naive SignProjection LSH with say 10 hash bits, you'd have 1024 possible bucket codes, and at small memory scales (the paper's experiments use ~140 thoughts) most buckets would be empty while a few would contain almost everything, defeating the point. The arg-max-over-2b scheme gives you a uniform-ish distribution over `b` buckets regardless of memory scale. The choice of `b` (the paper doesn't specify, but Andoni 2015 recommends `b` around `sqrt(memory_size)` for angular-distance LSH) is the implicit tuning knob — too small and buckets are crowded (similarity stage becomes expensive); too large and the same-thought-different-bucket false-negative rate climbs.

**Example of good use:** A memory architect implementing TiM tunes `b` empirically: start with `b = sqrt(N_expected_thoughts)`, measure the recall accuracy gap between LSH-bucketed retrieval and global pairwise similarity (the ground truth), and increase `b` if the gap is unacceptable. They also build in a periodic rehash step — when memory grows by 4x, regenerate R with a larger `b` and rehash everything. They keep the LSH random matrix R seeded and version-controlled so retrieval is reproducible across sessions.

**Example of misapplication:** A team "follows the TiM paper" but implements LSH naively with sign-projection and a hard-coded 8-bit hash, then complains that retrieval accuracy is bad on a 10k-thought store. The 256 buckets aren't enough for that scale, recall drops because semantically-similar thoughts land in different buckets, and they conclude "TiM doesn't scale" when actually the LSH was misconfigured. Or worse: they replace LSH with HNSW or FAISS and lose the in-bucket pairwise-similarity stage that TiM relies on for top-k ranking — HNSW gives approximate nearest neighbours globally but doesn't enforce the bucket-locality that makes maintenance operations (forget/merge per bucket) coherent. The architecture's three pieces — bucketed storage, bucket-local retrieval, bucket-local maintenance — are designed together; swapping out one breaks the others.

## Extracted Prompts

**Prompt explanation:** Insert / thought-generation prompt (Figure 3). Uses in-context learning with two worked examples to teach the LLM to extract a `(subject, relation, object)` relation triple AND a natural-language statement of it from a Q-R pair.

```
Given the following question and response pairs, please extract the
relation (subject, relation, object) with corresponding text:

Example 1.
Input:
Question: Do you have any company recommendations for me?
Response: I recommend Google.
Output:
(Company, Recommended, Google).
Recommended company is Google.

Example 2.
Input:
Question: Which City is the capital of China?
Response: Beijing.
Output:
(China, Capital, Beijing).
The capital of China is Beijing.

Input:
Question: Do you have any book recommendations for me?
Response: I recommend "The Little Prince".
Output:
```

**Prompt explanation:** Forget prompt (Figure 4). Asks the LLM to remove counterfactual or contradictory thoughts from a group of stored thoughts, keeping only the survivors.

```
Given the following thoughts, please remove the counterfactual thoughts
or contradictory thoughts:

Example 1.
Input:
The capital of China is Beijing.
The capital of China is Shanghai.
The capital of the United States is Washington.
The capital of the United States is New York.
Output:
The capital of China is Beijing.
The capital of the United States is Washington.

Example 2.
Input:
Michael likes to play football.
Michael does not like to play football.
James likes to swim.
Mary likes to read books.
Output:
James likes to swim.
Mary likes to read books.

Input:
[A group of thoughts]
Output:
```

**Prompt explanation:** Merge prompt (Figure 5). Combines multiple same-entity thoughts into a denser single-thought representation.

```
Given the following thoughts, please merge the similar thoughts with the
same entity:

Example 1.
Input:
John works as an actor.
John works as a director.
John works as a writer.
Mike works as a teacher.
Output:
John works as an actor, a director, and a writer.
Mike works as a teacher.

Example 2.
Input:
Michael likes to play football.
Michael likes to play basketball.
James likes to swim.
Mary likes to read books.
Output:
Michael likes to play football and basketball.
James likes to swim.
Mary likes to read books.

Input:
[A group of thoughts]
Output:
```

**Prompt explanation:** Recall + answer prompt (Section 3.1.2 stage-1). Instructs the LLM to answer a new question using the retrieved memory, treating the memory as the source of truth rather than re-reasoning over conversation history.

```
For the current user's question: {Query}, you begin to recall past
conversations and the most relevant [memory] is: {Related_memory}.
According to the [memory], please answer the question:
{Query}.
```

## Citations

- OpenAI 2022 — ChatGPT (closed-source LLM used in TiM experiments)
- OpenAI 2023 — GPT-4 Technical Report
- Zhong et al. 2023 — MemoryBank (arXiv:2305.10250) — the SiliconFriend baseline TiM compares against
- Wang et al. 2023 — Augmenting language models with long-term memory / LongMem (arXiv:2306.07174) — the token-based memory comparator in Table 1
- Liang et al. 2023 — Self-controlled memory system / SCM (arXiv:2304.13343) — Q-R-pair memory baseline in Table 1
- Andoni et al. 2015 — Practical and optimal LSH for angular distance (NeurIPS) — the LSH scheme TiM uses
- Borgeaud et al. 2022 — RETRO: Improving language models by retrieving from trillions of tokens (ICML) — token-based external memory precedent
- Hu et al. 2021 — LoRA (arXiv:2106.09685) — used for parameter-efficient fine-tuning
- Wang et al. 2022 — Self-consistency in CoT reasoning (arXiv:2203.11171) — cited as evidence of inconsistent-reasoning problem TiM addresses
- Dunlosky & Metcalfe 2008 — Metacognition (Sage) — the cognitive-grounding analogy for TiM's design
- Zeng et al. 2022 — GLM-130B / ChatGLM (arXiv:2210.02414) — open-source LLM used in TiM experiments
- Yang et al. 2023 — Baichuan 2 (arXiv:2309.10305) — open-source LLM used in TiM experiments

(Full citation list in frontmatter `citations:`)

## Related Digests

- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (Mem0 inherits TiM's write-time-distillation idea but replaces LSH with vector top-K similarity over a flat NL store; Mem0's ADD/UPDATE/DELETE/NOOP gate generalises TiM's insert/forget/merge to a 4-operation contract via an LLM tool call)
- [[zhong-2023-memorybank-llm]] — MemoryBank: Enhancing LLMs with Long-term Memory (the SiliconFriend baseline TiM benchmarks against — MemoryBank stores raw Q-R pairs and uses Ebbinghaus-style forgetting; TiM stores thoughts and adds merge as a third operation)
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems (contemporaneous 2023 memory paper — MemGPT treats memory as paged OS-style virtual memory with the LLM as memory manager, vs TiM's flat LSH-bucketed thought store with operation prompts)

## Reviewer Notes

**Overall severity:** Clean

Every numeric claim in the digest is grounded in the paper. The retrieval-time figures (0.6287ms baseline → 0.5305ms TiM, memory length 140) come from Table 3 verbatim. The Chinese GVD ChatGLM correctness lift (0.418 → 0.605) and the Chinese-Travel KdConv Baichuan2 lift (0.207 → 0.757) are both read directly from Table 2. The KdConv top-10 retrieval accuracy of 0.973 and the >0.7 top-1 figure are from Section 4.3.2 / Figure 6. The Table 1 operation-coverage matrix (SCM/RelationLM/LongMem support only Insert; MemoryBank adds Forget; TiM adds Merge) is reproduced from the paper's Table 1.

The LSH formulation `F(x) = arg max([xR; -xR])` matches Equation 1 in Section 3.2.2 exactly. R is described as "a random matrix of size (d, b/2)" with b as "the number of groups in the memory" — both quotes are from the paper. Attributing the LSH scheme to Andoni et al. 2015 matches reference [16] in the paper.

The LoRA rank r=16 and 10 epochs come from Section 3.5. The three datasets (KdConv from Zhou et al. 2020, GVD from MemoryBank/Zhong et al. 2023, RMD from the paper's own collection of 1,800 medical conversations) are accurately described. The three metrics (Retrieval Accuracy, Response Correctness, Contextual Coherence) and their label scales are quoted from Section 4.1.4.

One framing note: the digest characterizes the b parameter tuning advice as "Andoni 2015 recommends b around sqrt(memory_size)" in the "What Experts Overlook" section — the paper itself does not cite this rule of thumb; I'm drawing on standard LSH tuning practice. This should read as my synthesis, not as a TiM-paper claim. The rest of that section accurately describes the arg-max-over-2b scheme being a uniform-distribution-over-b-buckets design (which IS what Equation 1 in the paper does) vs the naive sign-projection alternative (which is the contrast the section makes).

No urgent rewrites needed.
