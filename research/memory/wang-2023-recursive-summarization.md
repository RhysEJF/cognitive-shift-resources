---
corpus: agentic-memory
kind: paper-digest
slug: wang-2023-recursive-summarization
title: "Recursively Summarizing Enables Long-Term Dialogue Memory in Large Language Models"
authors:
  - "Wang, Qingyue"
  - "Fu, Yanhe"
  - "Cao, Yanan"
  - "Wang, Shuai"
  - "Tian, Zhiliang"
  - "Ding, Liang"
year: 2023
publication_date: "2023-08"
venue: "arXiv preprint (submitted to Neurocomputing)"
source_url: "https://arxiv.org/abs/2308.15022"
doi: null
arxiv_id: "2308.15022"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Telling an LLM to summarize the conversation again each time a session ends — feeding it the previous summary plus the new turns and asking for an updated one — outperforms both retrieval and fixed-summary memory baselines on long-term dialogue, and the predicted memory beats human-written gold memory because the recursive version is more cohesive and easier for the model to digest."
topics:
  - long-term-dialogue
  - llm-memory
  - recursive-summarization
  - multi-session-chat
  - procedural-memory
tags:
  - paper
  - llm
  - memory
  - dialogue
  - summarization
  - prompt-engineering
entities:
  - wang-qingyue
  - cao-yanan
  - ding-liang
related_digests:
  - lu-2023-memochat
  - zhong-2023-memorybank-llm
  - wu-2024-longmemeval
  - maharana-2024-locomo
  - packer-2023-memgpt-os
citations:
  - title: "GPT-4 Technical Report"
    authors: ["Achiam, J.", "Adler, S.", "Agarwal, S.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2303.08774"
  - title: "L-Eval: Instituting Standardized Evaluation for Long Context Language Models"
    authors: ["An, C.", "Gong, S.", "Zhong, M.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2307.11088"
  - title: "Keep Me Updated! Memory Management in Long-Term Conversations"
    authors: ["Bae, S.", "Kwak, D.", "Kang, S.", "et al."]
    year: 2022
    venue: "Findings of EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Longformer: The Long-Document Transformer"
    authors: ["Beltagy, I.", "Peters, M.E.", "Cohan, A."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2004.05150"
  - title: "Language Models are Few-Shot Learners"
    authors: ["Brown, T.B.", "Mann, B.", "Ryder, N.", "et al."]
    year: 2020
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2005.14165"
  - title: "Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations"
    authors: ["Chen, N.", "Li, H.", "Huang, J.", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2402.11975"
  - title: "Extending Context Window of Large Language Models via Positional Interpolation"
    authors: ["Chen, S.", "Wong, S.", "Chen, L.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2306.15595"
  - title: "LongLoRA: Efficient Fine-Tuning of Long-Context Large Language Models"
    authors: ["Chen, Y.", "Qian, S.", "Tang, H.", "et al."]
    year: 2024
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Effortless Integration of Memory Management into Open-Domain Conversation Systems"
    authors: ["Choi, E.", "On, K.W.", "Han, G.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2305.13973"
  - title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
    authors: ["Dao, T.", "Fu, D.", "Ermon, S.", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Survey on Evaluation Methods for Dialogue Systems"
    authors: ["Deriu, J.", "Rodrigo, Á.", "Otegi, A.", "et al."]
    year: 2019
    venue: "Artificial Intelligence Review"
    doi: null
    url: null
    arxiv_id: null
  - title: "AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback"
    authors: ["Dubois, Y.", "Li, C.X.", "Taori, R.", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools"
    authors: ["GLM, T.", "Zeng, A.", "Xu, B.", "et al."]
    year: 2024
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2406.12793"
  - title: "Retrieval Augmented Language Model Pre-training (REALM)"
    authors: ["Guu, K.", "Lee, K.", "Tung, Z.", "et al."]
    year: 2020
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Open-Domain Dialogue Generation: What We Can Do, Cannot Do, and Should Do Next"
    authors: ["Kann, K.", "Ebrahimi, A.", "Koh, J.J.", "et al."]
    year: 2022
    venue: "NLP4CONVAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Dense Passage Retrieval for Open-Domain Question Answering"
    authors: ["Karpukhin, V.", "Oguz, B.", "Min, S.", "et al."]
    year: 2020
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Prompted LLMs as Chatbot Modules for Long Open-Domain Conversation"
    authors: ["Lee, G.", "Hartmann, V.", "Park, J.", "et al."]
    year: 2023
    venue: "Findings of ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    authors: ["Lewis, P.", "Perez, E.", "Piktus, A.", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "A Diversity-Promoting Objective Function for Neural Conversation Models"
    authors: ["Li, J.", "Galley, M.", "Brockett, C.", "et al."]
    year: 2016
    venue: "NAACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "LooGLE: Can Long-Context Language Models Understand Long Contexts?"
    authors: ["Li, J.", "Wang, M.", "Zheng, Z.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2311.04939"
  - title: "How NOT to Evaluate Your Dialogue System: An Empirical Study of Unsupervised Evaluation Metrics for Dialogue Response Generation"
    authors: ["Liu, C.W.", "Lowe, R.", "Serban, I.", "et al."]
    year: 2016
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    authors: ["Liu, N.F.", "Lin, K.", "Hewitt, J.", "et al."]
    year: 2023
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation"
    authors: ["Lu, J.", "An, S.", "Lin, M.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2308.08239"
  - title: "Error Analysis Prompting Enables Human-Like Translation Evaluation in Large Language Models: A Case Study on ChatGPT"
    authors: ["Lu, Q.", "Qiu, B.", "Ding, L.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Training Millions of Personalized Dialogue Agents"
    authors: ["Mazaré, P.E.", "Humeau, S.", "Raison, M.", "et al."]
    year: 2018
    venue: "EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Llama 3"
    authors: ["MetaAI"]
    year: 2024
    venue: "Technical report"
    doi: null
    url: "https://llama.meta.com/llama3/"
    arxiv_id: null
  - title: "Do the Rewards Justify the Means? Measuring Trade-offs Between Rewards and Ethical Behavior in the Machiavelli Benchmark"
    authors: ["Pan, A.", "Shern, C.J.", "Zou, A.", "et al."]
    year: 2023
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "BLEU: A Method for Automatic Evaluation of Machine Translation"
    authors: ["Papineni, K.", "Roukos, S.", "Ward, T.", "et al."]
    year: 2002
    venue: "ACL"
    doi: "10.3115/1073083.1073135"
    url: null
    arxiv_id: null
  - title: "Towards Making the Most of ChatGPT for Machine Translation"
    authors: ["Peng, K.", "Ding, L.", "Zhong, Q.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2303.13780"
  - title: "Summarization is (Almost) Dead"
    authors: ["Pu, X.", "Gao, M.", "Wan, X."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2309.09558"
  - title: "FAISS"
    authors: ["Facebook AI Research"]
    year: 2019
    venue: "Software"
    doi: null
    url: "https://ai.meta.com/tools/faiss/"
    arxiv_id: null
  - title: "The Probabilistic Relevance Framework: BM25 and Beyond"
    authors: ["Robertson, S.", "Zaragoza, H."]
    year: 2009
    venue: "Foundations and Trends in Information Retrieval"
    doi: null
    url: null
    arxiv_id: null
  - title: "Long-Range Language Modeling with Self-Retrieval"
    authors: ["Rubin, O.", "Berant, J."]
    year: 2024
    venue: "TACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "BlenderBot 3: A Deployed Conversational Agent that Continually Learns to Responsibly Engage"
    authors: ["Shuster, K.", "Xu, J.", "Komeili, M.", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2208.03188"
  - title: "Llama 2: Open Foundation and Fine-Tuned Chat Models"
    authors: ["Touvron, H.", "Martin, L.", "Stone, K.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2307.09288"
  - title: "ChatGPT or Grammarly? Evaluating ChatGPT on Grammatical Error Correction Benchmark"
    authors: ["Wu, H.", "Wang, W.", "Wan, Y.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2303.13648"
  - title: "Memformer: A Memory-Augmented Transformer for Sequence Modeling"
    authors: ["Wu, Q.", "Lan, Z.", "Qian, K.", "et al."]
    year: 2022
    venue: "Findings of ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Beyond Goldfish Memory: Long-Term Open-Domain Conversation"
    authors: ["Xu, J.", "Szlam, A.", "Weston, J."]
    year: 2022
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Long Time No See! Open-Domain Conversation with Long-Term Persona Memory"
    authors: ["Xu, X.", "Gou, Z.", "Wu, W.", "et al."]
    year: 2022
    venue: "Findings of ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "GLM-130B: An Open Bilingual Pre-trained Model"
    authors: ["Zeng, A.", "Liu, X.", "Du, Z.", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2210.02414"
  - title: "A Comprehensive Analysis of the Effectiveness of Large Language Models as Automatic Dialogue Evaluators"
    authors: ["Zhang, C.", "D'Haro, L.F.", "Chen, Y.", "et al."]
    year: 2023
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Retrieve Anything to Augment Large Language Models"
    authors: ["Zhang, P.", "Xiao, S.", "Liu, Z.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2310.07554"
  - title: "Personalizing Dialogue Agents: I Have a Dog, Do You Have Pets Too?"
    authors: ["Zhang, S.", "Dinan, E.", "Urbanek, J.", "et al."]
    year: 2018
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
  - title: "History-Aware Hierarchical Transformer for Multi-Session Open-Domain Dialogue System"
    authors: ["Zhang, T.", "Liu, Y.", "Li, B.", "et al."]
    year: 2022
    venue: "Findings of EMNLP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Can ChatGPT Understand Too? A Comparative Study on ChatGPT and Fine-Tuned BERT"
    authors: ["Zhong, Q.", "Ding, L.", "Liu, J.", "et al."]
    year: 2023
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2302.10198"
  - title: "MemoryBank: Enhancing Large Language Models with Long-Term Memory"
    authors: ["Zhong, W.", "Guo, L.", "Gao, Q.", "et al."]
    year: 2024
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Facilitating Multi-Turn Emotional Support Conversation with Positive Emotion Elicitation: A Reinforcement Learning Approach"
    authors: ["Zhou, J.", "Chen, Z.", "Wang, B.", "et al."]
    year: 2023
    venue: "ACL"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 8
  title: "Generated responses when using different methods in MSC dataset"
  page: 27
  image_path: "figures/wang-2023-recursive-summarization-fig.png"
---

# Recursively Summarizing Enables Long-Term Dialogue Memory in Large Language Models

**Authors:** Qingyue Wang, Yanhe Fu, Yanan Cao, Shuai Wang, Zhiliang Tian, Liang Ding
**Published:** 2023-08 (v4 revised 2025-08-25) · [Source](https://arxiv.org/abs/2308.15022)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

The authors propose LLM-Rsum, a zero-shot plug-in that asks the LLM itself to recursively rewrite a running "memory" of a multi-session chat: at the end of each session the model is shown the previous memory plus the new session and prompted to produce an updated memory (≤20 sentences), and at response time it sees only the latest memory plus the current turn — never the raw history. On the Multi-Session Chat (MSC) and Carecall datasets (5 sessions each, evaluated mainly on session 4-5), ChatGPT-Rsum beats vanilla ChatGPT, ChatGPT-BM25/DPR retrieval baselines, MemoChat and MemoryBank on F1, BertScore, BLEU-1/2, plus human and GPT-4-judge engagingness/coherence/consistency; against the strongest baseline MemoryBank in pairwise GPT-4 judging it wins 48.2% to 11.9% (1000 sampled responses). Counter-intuitively, the recursively predicted memory beats ground-truth gold memory on BLEU/F1 — the authors attribute this to gold memory being fragmented sentences that the LLM cannot digest, while the recursive version is cohesive. The method is orthogonal to retrieval (adding it to ChatGPT-BM25-k5 lifts F1 from 20.91 to 21.81 and GPT-4 consistency from 76.88 to 90.68) and to long-context models (GPT-4o + Rsum: F1 20.35→21.02, coherence 87.7→91.12, consistency 82→93.29); two-/three-shot ICL exemplars give a further small bump (~+0.6 F1 at three-shot). Manual audit of 100 generated memories finds ~9.8% error content total (2.7% fabricated facts, 3.2% incorrect relationships, 3.9% missing details) — small but the main weakness the authors flag.

## Key Takeaway

The fastest way to give an LLM long-term dialogue memory isn't a fancy retriever or a structured database — it's to have the model recursively rewrite its own short summary at every session boundary, throw away the raw turns entirely, and respond from the summary alone. The really weird finding: this self-generated memory beats the human-written gold memory on automatic metrics, because cohesive paragraphs are easier for an LLM to use than the bullet-point ground truth — your model would rather read its own prose than a clean fact sheet.

## Implications

- **A 20-sentence rolling summary beats vector retrieval for multi-session chat**: On the MSC dataset ChatGPT-Rsum (F1 20.48, BertScore 86.89) outperforms both ChatGPT-BM25 and ChatGPT-DPR at k=3 (F1 19.56 / 20.23) and ChatGPT-MemoryBank (F1 20.28). If you're building a personal-assistant chatbot today, start with recursive summary memory before investing in vector infrastructure.
- **Use recursive summarization as an orthogonal plug-in, not a replacement**: When combined, retrieval + Rsum on ChatGPT-BM25 (k=5) lifts F1 to 21.81 and GPT-4 consistency to 90.68 (vs. 76.88 for retrieval alone). Treat memory and retrieval as additive layers — retrieval pulls exact quotes, summary stores the gist.
- **A bigger context window doesn't replace summary memory**: GPT-4o standalone hits 87.7 coherence / 82 consistency; GPT-4o + Rsum hits 91.12 / 93.29 even though the dialogues fit easily inside the context window. Stronger models still benefit because the summary reorganizes information into a form they consume more effectively.
- **Skip golden/structured memory designs — let the model write its own**: Ablation shows ground-truth gold memory underperforms predicted memory on F1 and BLEU. Don't pay annotators or build operation-labeled (replace/append/delete) memory pipelines; one prompt that says "combine old memory + new session into ≤20 sentences" produces more usable output.
- **Two or three in-context examples is the cheapest performance bump**: Adding 2-shot and 3-shot ICL exemplars (dialog, memory, gold response) lifts F1 from 20.48 → 20.63 → 21.08 and BLEU-1 from 21.76 → 22.04 → 22.23 on session 5. Budget a handful of high-quality examples in the response-generator prompt.
- **Expect ~3-4% factual drift in summaries — design for audit**: 100-sample manual audit shows ~2.7% fabricated facts, ~3.2% incorrect relationships, ~3.9% missing details. For health/diagnostic use cases (Carecall-style), pair the summary with a retrieval check on safety-critical entities (medications, allergies, prior diagnoses) before responding.
- **Use the step-by-step prompt structure they ship verbatim**: Their memory-iteration and response-generation prompts both follow a four-step structure (analyze prior memory, identify new info, combine, structure). The authors note step-by-step instructions empirically helped — these prompts are the actual production recipe and worth copying directly (Tables 1, 2 in the paper).
- **Watch the cost-per-turn**: The Limitations section flags this — every turn that ends a session triggers a memory-iteration LLM call in addition to the response call. For a 5-session conversation that's 5 extra calls; in production, batch the iteration at session boundaries (not turn boundaries) and consider distilling the iterator into a smaller fine-tuned model.

## How to Apply It (method)

**Scenario:** You're building an AI sales-development assistant that talks to the same prospect 6-8 times over a month (qualification call, follow-up, demo prep, demo, objection-handling, contract). The model needs to remember which features the prospect cared about in call 1 when it's halfway through call 5, without ballooning the prompt cost or wiring up a vector store. You want a zero-training drop-in.

**Steps:**

1. **Define a session boundary**: Decide what triggers a memory update — e.g., end-of-meeting transcript, end of email thread, or every 20 chat turns. Memory iteration runs once per session, not per turn.

2. **Set up the memory-iteration prompt** with placeholders for previous memory and current session. Use the paper's structure verbatim — Table 1 is battle-tested:

   ```
   You are an advanced AI language model with the ability to store and update
   a memory to keep track of key personality information for both the user
   and the bot. You will receive a previous memory and dialogue context. Your
   goal is to update the memory by incorporating the new personality information.

   To successfully update the memory, follow these steps:
   1. Carefully analyze the existing memory and extract the key personality of
      the user and bot from it.
   2. Consider the dialogue context provided to identify any new or changed
      personality that needs to be incorporated into the memory.
   3. Combine the old and new personality information to create an updated
      representation of the user and bot's traits.
   4. Structure the updated memory in a clear and concise manner, ensuring it
      does not exceed 20 sentences.

   [Previous Memory]: {previous_memory_or_"none"}
   [Session Context]: {full_session_transcript}

   [Updated Memory]:
   ```

   For sales, swap "personality" for "the prospect's stated needs, objections, pricing sensitivity, decision criteria, key stakeholders, and timeline."

3. **Run the iteration**: Pass the previous memory string (start with "none" on session 1) and the full new session transcript. Save the returned memory string. Repeat at the end of each session. Memory accumulates as a single ≤20-sentence string, not a list of past summaries.

4. **Set up the response-generation prompt** for the live conversation. Use only the latest memory + the current session context — no raw past sessions:

   ```
   You will be provided with a memory containing personality information for
   both yourself and the user. Your goal is to respond accurately to the user
   based on the personality traits and dialogue context.

   1. Analyze the provided memory to extract the key personality traits for
      both yourself and the user.
   2. Review the dialogue history to understand the context and flow of the
      conversation.
   3. Utilize the extracted personality traits and dialogue context to formulate
      an appropriate response.
   4. If no specific personality trait is applicable, respond naturally as a
      human would.
   5. Pay attention to the relevance and importance of the personality
      information, focusing on capturing the most significant aspects while
      maintaining the overall coherence of the memory.

   [Previous Memory]: {latest_memory}
   [Current Context]: {current_session_so_far}

   [Response]:
   ```

5. **Optional: add two in-context examples** to the response prompt — each is a (memory, dialog snippet, ideal response) triple from past wins. The paper shows 2-shot adds ~+0.2 F1 and 3-shot adds another ~+0.5, with bigger gains on consistency.

6. **Audit the memory periodically**: Spot-check ~5-10% of memories for the three error types the paper identifies — fabricated facts, incorrect relationships, missing details. For safety-critical fields (e.g., committed price, signed-off contract terms), do a retrieval cross-check against raw transcripts before any response that cites them.

7. **Plug in retrieval if you need exact quotes**: If a use case demands precise recall ("what did the prospect say about pricing on March 3?"), add a BM25 or DPR retriever over raw transcripts and concatenate top-k utterances in the response prompt alongside the latest memory — Table 8 in the paper shows this combination outperforms either component alone.

**Expected outcome:** A 5-8 session prospect conversation where the assistant maintains a single ~300-token rolling memory, recalls earlier-call commitments without rereading entire transcripts, and stays consistent on the prospect's stated needs. Token cost stays roughly flat regardless of conversation length (one iteration call per session, one response call per turn — both bounded by the 20-sentence memory cap rather than full history). Expect a couple of percent factual drift in the memory; design audits accordingly.

## Best Figure

![Figure 8 — Generated responses when using different methods (page 27)](figures/wang-2023-recursive-summarization-fig.png)

Image Candidates:
Figure 3 (p. 9): Schematic of the recursive memory loop across three sessions — clearest single-view summary of the method.
Figure 4 (p. 22): Pairwise GPT-4 win/tie/loss bars vs. three baselines, including the 48.2% win-vs-11.9% loss against MemoryBank — strongest headline result in one chart.
Figure 8 (p. 27): Case-study comparison showing past memory, retrieved utterances, and the responses generated by ChatGPT, gold memory, ChatGPT-DPR, ChatGPT-MemoryBank, and ChatGPT-Rsum to the same query — the only figure that puts all methods side by side on a single example.

Best Image:
Figure 8 contrasts five methods on the same multi-session example: the prospect-style question "How does your shopping addiction go?" is asked after past sessions about expensive shoes and basketball shoes the bot doesn't wear. The figure shows each method's memory (or absence of it), retrieved utterances, and the resulting response. Vanilla ChatGPT and ChatGPT-DPR collapse to "I'm an AI, I don't shop"; gold memory produces a generic "I try to be mindful" reply; MemoryBank produces a flat acknowledgement; only Rsum mentions the specific basketball-shoes habit ("I try to limit myself and only purchase ones that I know I'll actually wear"). It's the paper's clearest demonstration that recursive memory not only stores facts but produces responses that *use* them.

## What Experts Overlook

The detail that quietly carries the paper is that the response generator never sees the raw past sessions — only the latest memory + the current turn. Most experts who skim memory papers assume "memory" is an *additive* prompt component sitting alongside the raw history, but here it's a *replacement*. The memory iteration step is the only place the raw history exists at inference time. This shows up implicitly in Equation 1 (`P(rt | Ct, S) = P(rt | Ct, MN) · P(MN | S)`) and explicitly in Algorithm 1 line 5 (`rt = LLM(Ct, MN, Pr)` — no S parameter).

**Why it matters:** Once you internalize this, two things follow. First, the memory budget is hard-capped at ≤20 sentences regardless of conversation length — that's what lets the approach scale to "extremely long dialog context" without context-window growth. Second, the quality of the memory iteration prompt is load-bearing — anything the iterator drops is permanently lost to the response generator. This is also why the paper's three error categories (fabricated facts, incorrect relationships, missing details) all happen at iteration time, not response time. If you treat the memory as just one more retrieval source rather than the *sole* representation of history, you'll get a more forgiving but heavier-weight system that doesn't actually realize the cost benefits the paper advertises.

**Example of good use:** A coaching app stores the user's running rolling memory ("trying to lose 5kg, hates cardio, free Mon/Wed evenings, mentioned knee injury in 2024") and feeds *only* that plus the current session to GPT-4o. Cost stays bounded; the model never gets distracted by chatter from 8 weeks ago about a different goal; the memory becomes a single auditable artifact the user can see and edit. This matches what the paper actually optimizes for.

**Example of misapplication:** A medical history app concatenates the recursive memory *plus* the entire prior transcript "for safety," reasoning that more context can only help. They lose all the cost benefits (now O(N) tokens again), but worse, the model now sees the same fact twice — once in the gist memory, once in a raw turn — and the case study (Figure 8) shows raw history pulls the model toward local information ("I'm an AI, I don't have prescriptions") and away from the synthesized state. The combination produces inconsistent responses where the abstracted memory and the raw turns disagree. The paper's gain comes from *removing* the raw history at response time, not from adding the memory on top of it.

## Extracted Prompts

**Prompt explanation:** Memory iteration — combines previous memory and a new session into an updated ≤20-sentence memory. Run once at the end of each session.

```
You are an advanced AI language model with the ability to store and update a memory to keep track of key personality information for both the user and the bot. You will receive a previous memory and dialogue context. Your goal is to update the memory by incorporating the new personality information.
To successfully update the memory, follow these steps:
1.Carefully analyze the existing memory and extract the key personality of the user and bot from it.
2. Consider the dialogue context provided to identify any new or changed personality that needs to be incorporated into the memory.
3. Combine the old and new personality information to create an updated representation of the user and bot's traits.
4. Structure the updated memory in a clear and concise manner, ensuring it does not exceed 20 sentences.
Remember, the memory should serve as a reference point to maintain continuity in the dialogue and help you respond accurately to the user based on their personality.
[Previous Memory] [Session Context]
[Updated Memory]
```

**Prompt explanation:** Memory-based response generation — generates the next reply using only the latest memory and current dialogue context (no raw past sessions).

```
You will be provided with a memory containing personality information for both yourself and the user. Your goal is to respond accurately to the user based on the personality traits and dialogue context.
Follow these steps to successfully complete the task:
1. Analyze the provided memory to extract the key personality traits for both yourself and the user.
2. Review the dialogue history to understand the context and flow of the conversation.
3. Utilize the extracted personality traits and dialogue context to formulate an appropriate response.
4. If no specific personality trait is applicable, respond naturally as a human would.
5. Pay attention to the relevance and importance of the personality information, focusing on capturing the most significant aspects while maintaining the overall coherence of the memory.
[Previous Memory] [Current Context]
[Response]
```

**Prompt explanation:** Context-only LLM baseline — directly concatenates past sessions + current dialogue context with no memory layer (used for Llama2-7B, ChatGLM2-6B, ChatGPT).

```
You are an advanced AI language model capable of engaging in personality-based conversations. Respond to the user based on the provided dialogue context. Craft a response that is natural and conversational.
Dialog context: [dialog]
The response to user is:
[response]
```

**Prompt explanation:** Retrieval-based LLM baseline — uses retrieved past utterances (BM25 or DPR) alongside dialogue memory and current context.

```
You are an advanced AI designed for engaging in natural, personality-based conversations. You will be provided with dialogue memory, relevant historical context, and dialogue context. The dialogue memory contains the personality, preferences, and experiences of the speakers (the user and the assistant). When responding, consider maintaining a conversational and fluent tone. Responses should be contextually relevant and aim to keep the conversation flowing.
Relevant context: [retrieved utterances]. Dialogue context: [dialog].
So the response to the user is:
[response]
```

**Prompt explanation:** Retrieval + Rsum framework combined — feeds retrieved utterances and the latest recursive memory together for response generation.

```
You are an advanced AI designed for engaging in natural, personality-based conversations. You will be provided with dialogue memory, relevant historical context, and dialogue context. The dialog memory contains the personality, preferences and experiences of speakers (the assistant and the user). When responding, consider maintaining a conversational and fluent tone. Responses should be contextually relevant and aim to keep the conversation flowing.
Relevant context: [retrieval utterances]
Memory: [latest memory]
Dialogue: [current context]
[response]
```

**Prompt explanation:** In-context-learning enhancement — one-shot example showing the model how to use memory before answering the test case.

```
You are an advanced AI designed for engaging in natural, personality-based conversations. You will be provided with a memory, containing the personal preferences and experiences of speakers (the assistant and the user), as well as a dialogue context. When responding, consider maintaining a conversational and fluent tone. Responses should be contextually relevant, consistent with given memory, aiming to keep the conversation flowing. Your goal is to provide engaging and coherent responses based on the dialogue context provided. To help you understand this task, we provide 1 example below.
EXAMPLE 1: The example memory is:
User: - Divorced - Raising one child - Immigrated from Britain last year - Metal worker
Assistant: - Not married - Girlfriend has 2 kids - Works on mTurk, landscaping, sales, envelope stuffing, painting - Used to love winter, but has become intolerant of it - Works with a friend who owns "John of all trades"
The example dialogue context is:
User: Today was the hottest day I've ever experienced here in Florida!
So the response to the user is: do you enjoy the heat more than the cold in Britain?
The following is the case you need to test: The test memory is:[previous memory]
The test dialogue context is:[dialog] So the response to the user is:
[response]
```

**Prompt explanation:** GPT-4-as-judge single-model evaluation — scores fluency, consistency, coherency on a 1-100 scale.

```
You are an impartial judge. You will be shown a Conversation Context, Personality of Speakers and Assistant Response.
#Fluency: Please evaluate whether the Assistant's response is natural, fluent, and similar to human communication, avoiding repetition and ensuring a diverse range of output.
#Consistency: Please evaluate whether the Assistant's response is consistent with the information of persona list. Any deviation from the expected personality may indicate a lack of coherence.
#Coherency: Please evaluate whether the Assistant's response maintains a coherent and logical flow of conversation based on the evolving context. A response with good context coherence can understand and respond appropriately to changes in conversation topics, providing smooth and sensible interactions.
Conversation Context:[dialog] Personality:[persona] Assistant Response: [response]
Begin your evaluation by providing a short explanation, then you must rate the Assistant Response on an integer score of 1 (very bad) to 100 (very good) by strictly following this format: [[score]].
[output]
```

**Prompt explanation:** GPT-4-as-judge pairwise evaluation — compares two anonymous responses on coherence, consistency, fluency.

```
Hi! We are a group of researchers working on Artificial Intelligence. In this task, we will ask you to help us rate the assistant's responses. In the area below, you will first read:
1. A conversation context comes from two speakers (the user and bot)
2. The personality of two speakers (the user and bot) extracted from past dialogs.
3. Two responses from AI systems. Your task is to decide which response is better. There are several dimensions that you can think along. Consider the following questions:
1. Is the response coherent? A response with good context coherence can understand and respond appropriately to changes in conversation topics, providing smooth and sensible interactions.
2. Is the response consistent? Evaluate whether the response is consistent with the information of persona list. Any deviation from the expected personality may indicate a lack of consistency.
3. Is the response natural and fluent? Please evaluate whether the response is natural, fluent, and similar to human communication, avoiding excessive repetition and ensuring a diverse range of output.
Based on your aesthetics, which one do you prefer? For example, you might prefer one poem over another poem. Ultimately, you should decide which response is better based on your judgment and your own preference. There are four options for you to choose from:
1.Response 1 is better : If you think response 1 has an advantage, then choose this option.
2.Response 1 is slightly better : Response 1 is very marginally better than response 2 and the difference is small.
3.Response 2 is slightly better : Response 2 is very marginally better than response 1 and the difference is small.
4.Response 2 is better : If you think response 2 has an advantage, then choose this option.
There are cases where the difference between the two responses is not clear. In this case, you can choose the second or the third option. However, in general, we ask you to choose those options as few as possible.
response 1: [response1] response 2: [response2]
[response]
```

## Citations

- Achiam et al. (2023) — GPT-4 Technical Report (arXiv:2303.08774)
- Bae et al. (2022) — Keep Me Updated! Memory Management in Long-Term Conversations (Findings of EMNLP)
- Beltagy et al. (2020) — Longformer (arXiv:2004.05150)
- Brown et al. (2020) — Language Models are Few-Shot Learners (arXiv:2005.14165)
- Chen et al. (2024a) — Compress to Impress: Compressive Memory in Real-World Long-Term Conversations (arXiv:2402.11975)
- Chen et al. (2024b) — LongLoRA: Efficient Fine-Tuning of Long-Context LLMs (ICLR)
- Dao et al. (2022) — FlashAttention (NeurIPS)
- Karpukhin et al. (2020) — Dense Passage Retrieval (EMNLP)
- Lewis et al. (2020) — Retrieval-Augmented Generation (NeurIPS)
- Liu et al. (2023) — Lost in the Middle (TACL)

Full structured citation list available in the frontmatter (`citations[]`) — 47 references.

## Related Digests

- [[lu-2023-memochat]] — MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation (direct baseline in this paper)
- [[zhong-2023-memorybank-llm]] — MemoryBank: Enhancing Large Language Models with Long-Term Memory (the strongest baseline; Rsum wins 48.2% to 11.9% pairwise)
- [[wu-2024-longmemeval]] — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory (later benchmark covering this method's regime)
- [[maharana-2024-locomo]] — Evaluating Very Long-Term Conversational Memory of LLM Agents (longer-horizon evaluation)
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems (alternative memory-management paradigm using paged virtual memory)

## Reviewer Notes

**Overall severity:** Clean

All TLDR statistics, ablation findings, prompt texts, and counter-intuitive claims were cross-checked against the paper:

- F1 / BertScore / BLEU numbers (20.48 / 86.89 / 21.83-12.59 for ChatGPT-Rsum on MSC session 5) match Table 3.
- GPT-4 judge scores (78.92/83.56/84.76 for Rsum vs. 75.48/75.00/75.48 for vanilla ChatGPT) match Table 4.
- Pairwise GPT-4 win/tie/loss 48.2%/39.9%/11.9% vs. MemoryBank matches Figure 4 and the surrounding text.
- Ablation comparison "predicted memory beats gold memory" matches Table 5 (Rsum F1 20.48 vs. Gt. Memory 20.46, BLEU-1 21.83 vs. 21.50). The text explicitly attributes this to gold memories being "fragmented and lack cohesiveness."
- Error breakdown 2.7% / 3.2% / 3.9% (fabricated / incorrect relationships / missing details) and the "does not exceed 10%" framing match Section 6.4 / Table 6.
- ICL two-shot/three-shot deltas match Table 7 (zero-shot F1 20.48 → 2-shot 20.63 → 3-shot 21.08; BLEU-1 21.76 → 22.04 → 22.23 on session 5).
- Retrieval-Rsum complementarity numbers (BM25-k5 F1 20.91 → 21.81; coherence 75.44 → 84.44; consistency 76.88 → 90.68) match Table 8.
- Long-context complementarity numbers (GPT-4o F1 20.35→21.02; coherence 87.7→91.12; consistency 82→93.29) match Table 9.
- Algorithm 1 line numbering and the M0 ← none initialization match the paper.
- The "response generator sees only memory + current context, never raw past sessions" claim matches Equation 1 and Algorithm 1.
- All eight extracted prompts are verbatim from Tables 1, 2, B.12-B.17.

No fabricated metrics, model names, or experimental conditions detected. Description of LongLoRA-8k complementarity (F1 14.02 → 15.77) matches Table 9. Description of "20 sentences" memory cap matches Table 1's prompt text. Carecall description as Korean machine-translated open-domain dataset matches Section 5.1.
