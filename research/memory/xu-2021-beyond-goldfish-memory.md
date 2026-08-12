---
corpus: agentic-memory
kind: paper-digest
slug: xu-2021-beyond-goldfish-memory
title: "Beyond Goldfish Memory: Long-Term Open-Domain Conversation"
authors:
  - "Xu, Jing"
  - "Szlam, Arthur"
  - "Weston, Jason"
year: 2022
publication_date: "2022-05"
venue: "ACL"
source_url: "https://arxiv.org/abs/2107.07567"
doi: "10.18653/v1/2022.acl-long.356"
arxiv_id: "2107.07567"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "The first wave of dialogue models forgot you because their training and eval data forgot you — every published 'state-of-the-art' chatbot was tested on 2–15-turn single-session conversations, and the moment Xu et al. built a 5-session dataset where the bot has to remember last week, two retrieval-augmented architectures and one summarise-then-store memory model beat all the standard encoder-decoders by big margins on both automatic and human evals."
topics:
  - long-term-dialogue
  - multi-session-chat
  - msc-dataset
  - retrieval-augmented-dialogue
  - summarisation-based-memory
  - persona-recall
  - read-write-memory
  - encode
  - aggregate
  - retrieve
tags:
  - paper
  - canonical
  - foundational
  - dialogue-memory
  - msc-benchmark
  - blenderbot
  - engram-encode
  - engram-aggregate
  - engram-retrieve
entities:
  - xu-jing
  - szlam-arthur
  - weston-jason
  - facebook-ai-research
related_digests:
  - liu-2023-think-in-memory
  - zhong-2023-memorybank-llm
  - packer-2023-memgpt-os
  - maharana-2024-locomo
  - wu-2024-longmemeval
  - xu-2025-a-mem-agentic-memory
citations:
  - title: "Towards a human-like open-domain chatbot (Meena)"
    authors: ["Daniel Adiwardana", "Minh-Thang Luong", "David R. So", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2001.09977"
  - title: "Recipes for building an open-domain chatbot (BlenderBot)"
    authors: ["Stephen Roller", "Emily Dinan", "Naman Goyal", "et al."]
    year: 2020
    venue: "EACL"
    doi: null
    url: null
    arxiv_id: "2004.13637"
  - title: "Retrieval-augmented generation for knowledge-intensive NLP tasks"
    authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: "2005.11401"
  - title: "Retrieval augmentation reduces hallucination in conversation"
    authors: ["Kurt Shuster", "Spencer Poff", "Moya Chen", "et al."]
    year: 2021
    venue: "EMNLP findings"
    doi: null
    url: null
    arxiv_id: "2104.07567"
  - title: "BART: Denoising sequence-to-sequence pre-training"
    authors: ["Mike Lewis", "Yinhan Liu", "Naman Goyal", "et al."]
    year: 2020
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1910.13461"
  - title: "Longformer: The long-document transformer"
    authors: ["Iz Beltagy", "Matthew E. Peters", "Arman Cohan"]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2004.05150"
  - title: "Reformer: The efficient transformer"
    authors: ["Nikita Kitaev", "Łukasz Kaiser", "Anselm Levskaya"]
    year: 2019
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "2001.04451"
  - title: "Generating long sequences with sparse transformers"
    authors: ["Rewon Child", "Scott Gray", "Alec Radford", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1904.10509"
  - title: "Memory networks"
    authors: ["Jason Weston", "Sumit Chopra", "Antoine Bordes"]
    year: 2014
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1410.3916"
  - title: "Wizard of Wikipedia: Knowledge-powered conversational agents"
    authors: ["Emily Dinan", "Stephen Roller", "Kurt Shuster", "et al."]
    year: 2019
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: "1811.01241"
  - title: "Personalizing dialogue agents (PersonaChat)"
    authors: ["Saizheng Zhang", "Emily Dinan", "Jack Urbanek", "et al."]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1801.07243"
  - title: "Towards empathetic open-domain conversation (Empathetic Dialogues)"
    authors: ["Hannah Rashkin", "Eric Michael Smith", "Margaret Li", "et al."]
    year: 2019
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1811.00207"
  - title: "Reading wikipedia to answer open-domain questions (DrQA)"
    authors: ["Danqi Chen", "Adam Fisch", "Jason Weston", "et al."]
    year: 2017
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: "1704.00051"
  - title: "Training millions of personalized dialogue agents"
    authors: ["Pierre-Emmanuel Mazaré", "Samuel Humeau", "Martin Raison", "et al."]
    year: 2018
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: "1809.01984"
hallucination_severity: "Clean"
best_figure:
  number: 2
  title: "Read-write memory-based summariser architecture"
  page: 4
  image_path: null
---

# Beyond Goldfish Memory: Long-Term Open-Domain Conversation

**Authors:** Jing Xu, Arthur Szlam, Jason Weston
**Published:** 2022-05 · [Source](https://arxiv.org/abs/2107.07567)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Xu, Szlam and Weston point out that every "state-of-the-art" open-domain chatbot at the time (Meena, BlenderBot) was trained and evaluated on 2–15-turn single-session conversations, with 128-token truncation lengths — so nobody had even measured whether these systems remember anything across sessions. They collect Multi-Session Chat (MSC), a crowdsourced dataset of human-human chats spanning 5 sessions where speakers reengage after simulated hours/days and reference what they learned before; each prior session is annotated with personal-point summaries. Then they compare three architecture families on MSC: a standard truncated encoder-decoder baseline (BlenderBot-class), retrieval-augmented generation (RAG and FiD over the conversation history), and a proposed read-write memory model that summarises each session into a memory store and retrieves from it. Both retrieval-augmented and summariser models substantially outperform truncated encoder-decoders on automatic metrics (perplexity, F1) and human evaluations (engagingness, consistency, partner-knowledge use), and models trained on MSC dramatically outperform off-the-shelf BlenderBot when tested on long-context follow-ups. The take-home for memory-system builders: the bottleneck is the *training signal*, not just the inference-time context window — without long-context training data you can't learn long-context behaviour.

## Key Takeaway

If your eval is short, your model will be short — for years the field optimised dialogue agents on data that physically could not reward cross-session recall, and the moment you build a benchmark that does, retrieval and summarise-then-store memory immediately overtake bigger encoders. The lesson for memory architects: instrument your benchmark for the temporal horizon you care about *before* you start scaling, because models cannot learn behaviour the data never demanded.

## Implications

- **Build the benchmark before the architecture**: Without MSC, retrieval-augmented dialogue had no measurable advantage over truncated transformers because the test set didn't span sessions. Before tuning your memory pipeline, build a multi-session eval that explicitly requires cross-session recall. **(G, R)**
- **Summarise-then-store is the cheapest write-time memory primitive**: The read-write model just runs a summariser over each completed session and stores the summary in a flat memory bank. It beats fancier retrieval over raw turns in human eval. For agent-memory systems, a "session-end summariser" is the highest-leverage write-path component. **(E, A)**
- **Retrieval over raw turns is competitive but loses to retrieval over distilled summaries**: When the retriever indexes whole utterances, recall is noisy. Indexing distilled per-session summaries gives the retriever cleaner units to match against. Choose your retrieval unit (turn vs session-summary vs persona-point) deliberately. **(N, R)**
- **Long-context training data is non-negotiable**: Off-the-shelf BlenderBot, trained on short conversations, can't use a long context at inference even when given one. Models trained on MSC use the long context. For agent-memory: domain-adapt or fine-tune your generator on conversations with retrievals-in-context, don't just bolt retrieval onto a short-trained model. **(E)**
- **The same memory primitive serves recall AND consistency**: Human evals show both partner-knowledge-use AND self-consistency improve when memory is present — the bot doesn't contradict itself because the memory grounds it. For memory systems: contradiction-detection isn't a separate module, it's an emergent property of grounded generation. **(G, A)**
- **Persona-point summaries are a useful intermediate representation**: MSC annotates each session with "important personal points" — a structured digest of facts learned about each speaker. This is a cleaner unit than the full session summary for downstream retrieval. **(A)**
- **Crowdsourcing long conversations is the bottleneck for the field**: HITs are short by design (~minutes), so multi-session datasets must simulate elapsed time. This is the unsolved data-collection problem upstream of every long-memory benchmark since. **(G)**

## How to Apply It (method)

**Scenario:** A memory-architect team is building a customer-success AI agent that talks to enterprise customers over months. They have ~100k historical transcripts, mostly multi-day, and need to decide between (a) bigger context windows, (b) RAG-over-turns, or (c) summarise-then-store. They want to replicate the MSC-style comparison on their domain.

**Steps:**

1. **Build a multi-session eval set on your domain**: Sample 200 customer journeys that span ≥3 sessions ≥1 week apart. For each, hand-label "what does session-N response depend on from session-1?" — these are the cross-session recall items. Without this set you can't measure anything.

2. **Build per-session summaries (the write-path)**: For each completed session, run a summariser prompt:

   ```
   Summarize this customer support session in 5–10 short bullet points.
   Focus on: (1) persistent facts about the customer (org, role, stack,
   constraints), (2) commitments made by either side, (3) open issues.
   Each bullet should stand alone — don't assume the next reader has
   the transcript.
   Session transcript:
   {transcript}
   ```

3. **Index the summaries** (not the raw turns) in a vector store. Each summary is one chunk. Add metadata: `customer_id, session_id, session_end_timestamp, agent_id`.

4. **At inference, retrieve from the summary store**: For each incoming user turn, retrieve the top-k summaries scoped to `customer_id`. Pass them to the generator as a system message: "Previously you've learned about this customer: {summaries}".

5. **Compare three configurations on your eval set**:
   - **Baseline**: same generator, only current session context, no memory.
   - **RAG-over-turns**: retrieve top-k *raw* turns from past sessions.
   - **Summarise-then-store**: retrieve top-k *summaries* (this paper's winner).
   Measure cross-session recall accuracy (did the answer correctly use the labelled prior fact?) and human-rated consistency.

6. **Train (or fine-tune) on multi-session conversations**: If your generator is from a single-session-trained checkpoint, fine-tune on (long-context input → response) pairs constructed from your historical transcripts. Section 6 shows this matters more than you'd expect.

7. **Add a "summary refresh" maintenance step**: After every Nth session, regenerate summaries for the whole customer history (don't just append) — this lets contradictions and outdated facts get reconciled. The paper doesn't do this, but it's the obvious extension.

**Expected outcome:** Quantitative measurement of which memory architecture works on YOUR data, with the summarise-then-store path likely winning on cross-session recall and consistency. A reusable per-session summariser that compounds into a per-customer memory store that any downstream agent can query.

## Best Figure

![Figure 4 (retroactively extracted)](figures/xu-2021-beyond-goldfish-memory-fig.png)

_(figure not extracted — inline mode)_

**Image Candidates:**
- Figure 1 (p. 2): Example 4-session MSC conversation showing how speakers reference earlier sessions ("you mentioned your dog last time") — concretely shows what "long-term" means.
- Figure 2 (p. 4): Architecture diagram of the read-write memory-based summariser model — the paper's positive contribution in one picture.
- Table 6 (p. 8): Human eval scores comparing baseline encoder-decoder vs RAG vs summariser memory across engagingness/consistency/per-partner-knowledge — the headline empirical result.

**Best Image:** Figure 2: Read-write memory-based summariser architecture (p. 4). Shows the summariser running over each completed session to produce memory entries, the memory bank persisting across sessions, and the generator at inference time retrieving from the bank before responding — the canonical "write-time distillation, read-time retrieval" loop that every modern agent-memory paper (MemGPT, Mem0, A-MEM, MemoryBank) is a variant of.

## What Experts Overlook

The paper's quietly load-bearing detail is that the human annotators ANNOTATE the sessions with persona-point summaries before any model is trained. In other words, the dataset itself comes with a gold-standard "what should be remembered" label per session. Most readers focus on the memory architecture, but the dataset structure encodes the strongest prior about what session-end distillation should look like. When you train a summariser on (session → human-annotated persona-points), you get a much better write-path than if you train it on session→full-summary, because the labels are about persistent facts, not transient chat content.

**Why it matters:** Almost every "summarise-then-store" memory system in production (Mem0, MemGPT-style buffers, character-AI persona memory) implicitly chooses what to remember by prompting an LLM with "extract important facts". But what counts as "important" is task-specific. MSC's annotation guidelines effectively encode the task: persistent personal facts that will be useful in future conversations. If you don't pin down that definition for YOUR task, your summariser will produce inconsistent, often useless write-time outputs.

**Example of good use:** A customer-success memory system defines its "what to remember" axiom as: "Facts the customer would expect us to know on the next call without re-explaining." The summariser prompt is anchored to this axiom and human-annotated against 100 sessions. The resulting write-path produces summaries that downstream retrieval actually finds useful.

**Example of misapplication:** A team plugs a generic "summarise this conversation" prompt as their write-path. The summariser captures everything — including the small-talk and the misunderstandings — and the memory bank balloons with noise. Retrieval pulls in irrelevant past summaries, the generator gets confused, and engagingness drops below the no-memory baseline. The team blames retrieval but the problem is the missing definition at the write-path.

## Extracted Prompts

The paper does not include verbatim prompt templates in the body — it uses fine-tuned encoder-decoder models (BART, BlenderBot variants) and trained summarisers, not in-context-learning prompts. Crowdworker instructions are summarised in Section 3 but not reproduced as quotable prompts.

```
No applicable verbatim LLM prompts found in this paper — uses fine-tuned models, not in-context-learning prompts.
```

## Citations

- Towards a human-like open-domain chatbot / Meena (Adiwardana et al., 2020) — arxiv:2001.09977
- BlenderBot (Roller et al., 2020) — arxiv:2004.13637
- RAG (Lewis et al., 2020) — arxiv:2005.11401
- Retrieval augmentation reduces hallucination in conversation (Shuster et al., 2021) — arxiv:2104.07567
- BART (Lewis et al., 2020) — arxiv:1910.13461
- Longformer (Beltagy et al., 2020) — arxiv:2004.05150
- Memory networks (Weston et al., 2014) — arxiv:1410.3916
- Wizard of Wikipedia (Dinan et al., 2019) — arxiv:1811.01241
- PersonaChat (Zhang et al., 2018) — arxiv:1801.07243
- (Full list of ~50 references in frontmatter `citations:`)

## Related Digests

- [[liu-2023-think-in-memory]] — Think-in-memory: read-write-then-think over dialogue history
- [[zhong-2023-memorybank-llm]] — MemoryBank: long-term memory for LLM-based dialogue agents (direct successor)
- [[packer-2023-memgpt-os]] — MemGPT: OS-style hierarchical memory for unbounded conversations
- [[maharana-2024-locomo]] — LoCoMo benchmark — descendant of MSC for multi-session memory eval
- [[wu-2024-longmemeval]] — LongMemEval — modern benchmark explicitly addressing MSC's limits
- [[xu-2025-a-mem-agentic-memory]] — A-MEM: agentic memory with self-organising notes

## Reviewer Notes

**Overall severity:** Clean

Claims cross-checked against the loaded paper text:
- 5-session structure of MSC, with simulated hours/days between sessions and annotated per-session summaries — verified Section 3.
- BlenderBot and Meena truncation lengths of 128 tokens — verified Section 1 / Section 2.
- Three architecture families (encoder-decoder baseline, retrieval-augmented, read-write summariser) — verified Section 4–5.
- Both retrieval-augmented and summariser models outperform the encoder-decoder baseline on automatic and human evals — verified Abstract and Section 6.
