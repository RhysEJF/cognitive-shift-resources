---
corpus: agentic-memory
kind: paper-digest
slug: yao-2023-react-reasoning-acting
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
authors:
  - "Yao, Shunyu"
  - "Zhao, Jeffrey"
  - "Yu, Dian"
  - "Du, Nan"
  - "Shafran, Izhak"
  - "Narasimhan, Karthik"
  - "Cao, Yuan"
year: 2023
publication_date: "2022-10"
venue: "ICLR 2023"
source_url: "https://arxiv.org/abs/2210.03629"
doi: null
arxiv_id: "2210.03629"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Interleaving free-form reasoning traces (Thought:) with task-specific actions (Action:) in a single LLM prompt gives substantially better performance than either reasoning-only (chain-of-thought) or action-only (act-only) approaches — because reasoning steers what to retrieve from external sources next, and observations from those actions ground the reasoning against fact rather than hallucinating; ReAct's thought-action-observation pattern is the foundational template for nearly every modern agent framework (LangChain, AutoGPT, LlamaIndex agents) and is the prompting structure that turns an LLM from a one-shot answerer into an iterating agent."
topics:
  - react
  - reasoning-and-acting
  - chain-of-thought
  - agent-frameworks
  - tool-use
  - wikipedia-api
  - hotpotqa
  - alfworld
  - webshop
tags:
  - paper
  - canonical
  - agent-pattern
  - prompting
entities:
  - yao-shunyu
  - narasimhan-karthik
  - cao-yuan
related_digests:
  - brown-2020-gpt3-few-shot
  - lewis-2020-rag-knowledge-nlp
  - park-2023-generative-agents
  - liu-2023-think-in-memory
citations:
  - title: "Chain-of-thought prompting elicits reasoning in large language models"
    authors: ["Wei, Jason", "Wang, Xuezhi", "Schuurmans, Dale", "Bosma, Maarten", "Ichter, Brian", "Xia, Fei", "Chi, Ed", "Le, Quoc", "Zhou, Denny"]
    year: 2022
    arxiv_id: "2201.11903"
  - title: "PaLM: Scaling language modeling with pathways"
    authors: ["Chowdhery, Aakanksha", "et al."]
    year: 2022
    arxiv_id: "2204.02311"
  - title: "Language models are few-shot learners (GPT-3)"
    authors: ["Brown, Tom B.", "et al."]
    year: 2020
    venue: "NeurIPS"
  - title: "HotpotQA: A dataset for diverse, explainable multi-hop question answering"
    authors: ["Yang, Zhilin", "et al."]
    year: 2018
    venue: "EMNLP"
  - title: "FEVER: a large-scale dataset for fact extraction and verification"
    authors: ["Thorne, James", "Vlachos, Andreas", "Christodoulopoulos, Christos", "Mittal, Arpit"]
    year: 2018
    venue: "NAACL"
  - title: "ALFWorld: Aligning text and embodied environments for interactive learning"
    authors: ["Shridhar, Mohit", "et al."]
    year: 2020
    arxiv_id: "2010.03768"
  - title: "WebShop: Towards scalable real-world web interaction with grounded language agents"
    authors: ["Yao, Shunyu", "Chen, Howard", "Yang, John", "Narasimhan, Karthik"]
    year: 2022
    arxiv_id: "2207.01206"
  - title: "Working memory"
    authors: ["Baddeley, Alan"]
    year: 1992
    venue: "Science"
  - title: "Inner speech: New voices"
    authors: ["Alderson-Day, Ben", "Fernyhough, Charles"]
    year: 2015
    venue: "Psychological Bulletin"
  - title: "Do as I can, not as I say: Grounding language in robotic affordances (SayCan)"
    authors: ["Ahn, Michael", "et al."]
    year: 2022
    arxiv_id: "2204.01691"
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    authors: ["Nakano, Reiichiro", "et al."]
    year: 2021
    arxiv_id: "2112.09332"
  - title: "Inner monologue: Embodied reasoning through planning with language models"
    authors: ["Huang, Wenlong", "et al."]
    year: 2022
    arxiv_id: "2207.05608"
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Comparison of 4 prompting methods on HotpotQA: (a) Standard, (b) Chain-of-Thought (Reason Only), (c) Act-Only, (d) ReAct (Reason+Act)"
  page: 2
  image_path: null
---

# ReAct: Synergizing Reasoning and Acting in Language Models

**Authors:** Yao, Shunyu; Zhao, Jeffrey; Yu, Dian; Du, Nan; Shafran, Izhak; Narasimhan, Karthik; Cao, Yuan (Princeton + Google Brain)
**Published:** 2022-10 (ICLR 2023) · [Source](https://arxiv.org/abs/2210.03629)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

ReAct introduces a prompting pattern that interleaves **Thought** (free-form reasoning), **Action** (task-specific operations, e.g., Wikipedia search), and **Observation** (results from actions) in a single LLM trajectory. Two key insights: (1) chain-of-thought reasoning alone (CoT) hallucinates because it has no grounding — the model reasons internally but can't check facts; (2) action-only systems can't reason about what to retrieve next, just execute predefined plans. ReAct synergizes them: thoughts steer action choice ("I need to search Apple Remote and find what it was designed to interact with → Search[Apple Remote]"), and observations from actions ground further reasoning. On HotpotQA (multi-hop QA) and FEVER (fact verification) with a simple Wikipedia search API, ReAct outperforms vanilla action generation and is competitive with CoT — and the *best* approach is a combination of ReAct and CoT that uses both internal knowledge (CoT) and external retrieval (ReAct). On ALFWorld (text-based game) and WebShop (web navigation), ReAct outperforms imitation learning and RL baselines trained on 10³-10⁵ task instances by **34% and 10% absolute success rate** — using just one or two in-context examples. The pattern requires no fine-tuning, works on any frozen LLM (paper uses PaLM-540B and GPT-3), and produces human-interpretable trajectories. **ReAct is the prompting template behind every modern LLM-agent framework** — LangChain Agents, AutoGPT, BabyAGI, LlamaIndex Agents, and OpenAI's Function Calling are all variations on the Thought → Action → Observation loop.

## Key Takeaway

**Memory in agentic systems is not just storage — it's the *intermediate state of reasoning-and-acting trajectories*, and the prompt structure that maintains this state IS the memory architecture.** [ENGRAM: dominant on R (Retrieve — actions ARE retrieval), M (Maintain — the trajectory is the working memory), E (Encode — what gets written to the trajectory shapes what can be reasoned about later); secondary on A (Aggregate — multi-step traces consolidate observations into a final answer)] The deep insight is that pre-ReAct, the literature treated reasoning (CoT) and acting (function calling, retrieval) as separate problems. ReAct showed they're tightly coupled: **the model's working memory is the trajectory itself** — the accumulated thoughts, actions, and observations — and the quality of reasoning depends critically on what observations have been added to that memory. CoT alone has a fixed memory (the initial prompt) and hallucinates outside that. Act-only has rich memory (every observation added) but no mechanism to reason about what's missing. ReAct's thought steps are where the model *queries its own memory* (the trajectory so far) to decide what to retrieve next. **For Flow OS / any agent memory system**: the trajectory of thought-action-observation is the working-memory primitive. Persistent memory (across sessions) augments this primitive; it doesn't replace it. The Thought step IS the place where the agent decides "what do I need to remember / retrieve now," and instrumenting that step is how you observe and debug an agent's memory use.

## Implications

[ENGRAM mapping: dominant on **R** (Retrieve — actions are retrieval operations), **M** (Maintain — the trajectory is the working memory), **E** (Encode — thoughts encode the agent's reasoning state); secondary on **A** (Aggregate — multi-step traces produce final answers from accumulated evidence) and **N** (Network — the linear thought-action-observation sequence is the architectural shape choice)]

1. **The trajectory IS the working memory.** [M, E] ReAct's working memory is not a separate module — it's the prompt itself, growing with each Thought, Action, and Observation. The LLM reads the entire trajectory each step and decides what to do next. **This is the canonical shape of LLM working memory**: a flat append-only log that the model re-reads on every turn. For Flow OS: when you design persistent memory for agents, you're adding *long-term memory* that augments this *working memory* (the trajectory in the current session). Don't conflate them — they have different access patterns, different retention policies, different failure modes.

2. **Reasoning steers retrieval; observations ground reasoning.** [R, G] This is the explicit synergy. In a Thought step, the model uses its working memory (the trajectory so far) plus its parametric knowledge to decide what action to take. In an Observation step, the action's result is appended to working memory and becomes available for the next Thought. **This bidirectional flow is what neither CoT nor act-only achieves.** For agent memory design: the prompt structure must support bidirectional flow between reasoning and retrieval, not treat them as separate phases.

3. **The "internal knowledge vs external knowledge" distinction matters.** Best results come from combining ReAct and CoT: ReAct retrieves external facts when needed, CoT reasons over internal knowledge when external retrieval would be unnecessary or counterproductive. **For Flow OS**: instrument retrievals to identify which queries the LLM should answer from parametric knowledge vs which need external memory. Over-retrieval is a real cost — both latency and the noise it introduces into reasoning.

4. **One or two in-context examples is enough.** ReAct's experiments use 1-6 manually-written examples per task. This matches few-shot learning behavior generally but is particularly striking for agentic tasks where prior approaches required 10³-10⁵ training instances. **For agent design: invest deeply in 1-3 high-quality trajectory examples** rather than collecting massive supervised datasets. The examples teach the *pattern* (Thought → Action → Observation interleaving); the LLM generalizes from the pattern.

5. **Human-interpretable trajectories are a feature, not a side effect.** §1 contribution 1d: "Human aligned and controllable: ReAct promises an interpretable sequential decision making and reasoning process where humans can easily inspect reasoning and factual correctness. Moreover, humans can also control or correct the agent behavior on the go by thought editing." **The trajectory is auditable in a way black-box neural agents aren't.** For production agent deployment: ReAct-style trajectories should be logged and surfaced in dashboards. They're the diagnostic primitive for "why did the agent do this."

6. **Sparse, versatile reasoning > dense, formulaic reasoning.** §1 contribution 3: "the importance of sparse, versatile reasoning in decision making by showing consistent advantages over controlled baselines with actions only." Thoughts don't appear at every step — they appear where useful (decomposing a goal, handling an exception, deciding what to retrieve next). **For agent design: don't force a Thought at every step; let the model decide when reasoning is needed.** Over-prompting for reasoning can degrade performance (the model spends compute on filler thoughts).

7. **Wikipedia API is the lightest tool that works.** ReAct's action space on HotpotQA/FEVER is three operations: `search[entity]`, `lookup[string]`, `finish[answer]`. That's it. No complex tool calling, no JSON schemas, no function-calling API. **The minimal-tool-set approach has aged well** — modern frameworks reproduce this discipline (small action sets are easier to learn from few-shot than large ones).

## How to Apply It (method)

**The ReAct prompting template:**

```
You are an agent solving {task description}. You can take actions to interact with the environment.

Available actions:
  search[entity]      — returns the first 5 sentences of the wiki page for entity, or similar entities if not found
  lookup[string]      — returns the next sentence containing string on the current page (Ctrl+F)
  finish[answer]      — submit your final answer

Solve the task by interleaving:
  Thought: <free-form reasoning about what to do next>
  Action: <one of the available actions>
  Observation: <result of the action — appended automatically>

Example 1:
  Question: Aside from the Apple Remote, what other device can control the program Apple Remote was originally designed to interact with?
  Thought 1: I need to search Apple Remote and find the program it was originally designed to interact with.
  Action 1: search[Apple Remote]
  Observation 1: The Apple Remote is a remote control introduced in October 2005 by Apple ... originally designed to control the Front Row media center program ...
  Thought 2: Apple Remote was originally designed to control the Front Row media center program. I need to search Front Row next and find what other device can control it.
  Action 2: search[Front Row]
  Observation 2: Could not find [Front Row]. Similar: ['Front Row Seat to Earth', 'Front Row Motorsports', 'Front Row (software)', ...]
  Thought 3: To find the program, I can search Front Row (software).
  Action 3: search[Front Row (software)]
  Observation 3: Front Row is a discontinued media center software ... controlled by an Apple Remote or the keyboard function keys ...
  Thought 4: Front Row (software) is controlled by an Apple Remote or the keyboard function keys. So the answer is keyboard function keys.
  Action 4: finish[keyboard function keys]

Example 2: [another worked example]

Now solve:
  Question: {actual question}
```

**Key prompt-design principles (from §3-§4):**

1. **Include 1-6 worked trajectory examples** as in-context demonstrations. More is not better; quality matters more than quantity.
2. **Thoughts should be diverse**: decomposition ("I need to find X, then Y"), exception handling ("Could not find — let me try a variant"), commonsense reasoning ("X is not Y, so Z must be the case"), progress tracking ("Now I have all the info I need").
3. **Action space must be small** to fit in the prompt and enable few-shot learning. 3-5 actions is the sweet spot.
4. **Observations should be terse but informative** — long observations crowd the context window and hide signal.
5. **Allow asynchronous thought-action ratio** — for decision tasks with many actions, thoughts should be sparse (only at decision points); for QA tasks with rich reasoning, thoughts at every step.

**Domain extensions:**

- For **interactive environments** (ALFWorld, WebShop): actions are environment-specific (`go to`, `take`, `open`, `put in/on`, `click button[id]`). Observations are environment state descriptions.
- For **tool-using agents** (modern): actions are tool calls; observations are tool results. The pattern generalizes immediately.
- For **multi-step reasoning** (HotpotQA): actions are search/lookup; observations are document text.

**For Flow OS / production agents:**

1. **Implement Thought-Action-Observation as the agent loop's core abstraction**, even if you're using a higher-level framework like LangChain.
2. **Log every trajectory in full** — they're your debugging substrate. Don't truncate.
3. **Provide explicit "no-op" thought support** — allow the model to think without acting when reasoning over already-retrieved information is sufficient.
4. **Combine with CoT for tasks where internal knowledge dominates** — the best results come from hybrid CoT + ReAct.
5. **Make trajectories human-editable** — let domain experts correct trajectories in development to generate better few-shot examples.

## Best Figure

_(figure not extracted — Figure 1 in the paper is the canonical four-method comparison)_

**Figure 1 — Four prompting methods on HotpotQA, page 2:**

A 2×2 comparison grid showing the same HotpotQA question ("Aside from the Apple Remote, what other device can control the program Apple Remote was originally designed to interact with?") solved four ways:

**(a) Standard prompting**: Question → Answer. The model outputs "iPod" — wrong, no reasoning visible, no way to debug.

**(b) Chain-of-Thought (Reason Only)**: "Let's think step by step. Apple Remote was originally designed to interact with Apple TV. Apple TV can be controlled by iPhone, iPad, and iPod Touch. So the answer is iPhone, iPad, and iPod Touch." — also wrong, but in a more pernicious way: confidently hallucinated (Apple Remote was NOT originally designed for Apple TV; it was for Front Row).

**(c) Act-Only**: A sequence of search actions without thoughts: `search[Apple Remote] → Obs: ... → search[Front Row] → Obs: not found → search[Front Row software] → Obs: ... → finish[yes]`. The model can't reason about WHY it's searching what it's searching — and gets confused about what "yes" answers.

**(d) ReAct (Reason+Act)**: The same trajectory as (c) but with explicit Thoughts at each step: "I need to search Apple Remote and find the program... Apple Remote was originally designed to control Front Row... To find the program, I can search Front Row (software)..." The thoughts guide the searches and synthesize the final answer correctly: "keyboard function keys."

A second panel below shows the same comparison for ALFWorld (a text-based game) — Act-Only loops on a single action that doesn't work; ReAct explicitly plans where to look ("First I need to find a peppershaker more likely to appear in cabinets, countertops...") and succeeds.

The figure visualizes the entire thesis: **reasoning steers acting; acting grounds reasoning; either alone fails in characteristic ways.** It's one of the most-reproduced figures in agent-framework documentation because it cleanly shows what the ReAct pattern is.

## What Experts Overlook

1. **CoT + ReAct hybrid is the actual best system, not pure ReAct.** §3 reports that the best approach on HotpotQA is a *combination*: use CoT to leverage internal knowledge when sufficient, fall back to ReAct (retrieval) when CoT confidence is low or facts need verification. **Most agent frameworks adopt pure ReAct and miss this nuance.** For production: implement both reasoning modes and let the model (or a simple heuristic) decide which to use per query.

2. **The Wikipedia API is deliberately weak.** §3.1 Action Space: "We note that this action space mostly can only retrieve a small part of a passage based on exact passage name, which is significantly weaker than state-of-the-art lexical or neural retrievers. The purpose is to simulate how humans would interact with Wikipedia, and force models to retrieve via explicit reasoning in language." **The point is that ReAct's gains aren't dependent on a powerful retriever** — they hold even when retrieval is constrained to lookups by exact entity name. This means the ReAct pattern transfers to systems with weak underlying tools.

3. **PaLM-540B is the primary backbone, but GPT-3 also works.** §1 footnote 1: "We show some GPT-3 (Brown et al., 2020) results in Appendix A.1, which outperforms PaLM-540B." The pattern is robust across LLM backbones — not specific to one model's training. **For Flow OS**: ReAct works on Claude, GPT-4, Llama, and any post-2022 instruction-following LLM. Don't be locked into one backbone.

4. **Sparse thoughts are a deliberate design choice for decision tasks.** §2 last paragraph: "For decision making tasks that potentially involve a large number of actions (Figure 1(2)), thoughts only need to appear sparsely in the most relevant positions of a trajectory, so we let the language model decide the asynchronous occurrence of thoughts and actions for itself." **The model decides when to think.** This is opposite to systems that force a thought before every action — which can over-explain trivial steps and waste compute.

5. **Thought editing is a controllability lever.** §1 contribution D: "humans can also control or correct the agent behavior on the go by thought editing." If a deployed agent goes off-track, you can edit a thought in the trajectory to steer it back — without re-prompting from scratch. **This is the most practical controllability mechanism for LLM agents and is underused in production deployments.**

6. **The 34% / 10% improvements on ALFWorld / WebShop are with ONE or TWO in-context examples.** §1: "outperforms imitation and reinforcement learning methods trained with 10³ ∼ 10⁵ task instances, with an absolute improvement of 34% and 10% in success rates respectively." This is a 100-1000× sample-efficiency improvement. **The implication: in-context learning beats specialized fine-tuning for many agent tasks** when the LLM is strong enough. The discipline of starting with in-context learning before considering fine-tuning is well-supported by ReAct's results.

7. **Initial finetuning experiments suggest ReAct improves with training.** §1 contribution 4: "perform initial finetuning experiments showing the potential of ReAct to improve with additional training data." The pattern works zero-/few-shot AND benefits from supervised fine-tuning. This is the foundation for ReAct-style RL training (e.g., what Memory-R1 does for memory operations).

## Extracted Prompts

ReAct's primary contribution IS its prompt pattern. The canonical templates from the paper:

**HotpotQA / Knowledge-intensive QA prompt:**
```
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas.
Thought 2: It does not mention the eastern sector. So I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The eastern sector extends into the High Plains and is called the Central Plains orogeny.
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains. So I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]
...
Action 4: Finish[1,800 to 7,000 ft]

[More examples...]

Question: {actual question}
```

**ALFWorld / interactive environment prompt:**
```
You are an agent in a text-based game. Your goal is to {task description}. 

You can take the following actions:
- go to {location}
- open {object}
- take {object} from {location}
- put {object} in/on {location}
- look
- think: {free-form reasoning — does not affect environment}

Here is an example trajectory:

Task: Put some peppershaker on a drawer.
Action: think: First I need to find a peppershaker more likely to appear in cabinets, countertops...
Action: go to cabinet 1
Observation: On the cabinet 1, you see a vase 2.
[... more steps ...]
Action: put peppershaker in/on drawer 1
Observation: You put peppershaker 1 in/on the drawer 1. [success]

Now solve:
Task: {actual task}
```

**For modern LLM-based agents (Claude/GPT-4 with function calling):**
```
You are an agent. For each step, output:
{
  "thought": "<your reasoning about what to do next>",
  "action": {
    "name": "<tool name>",
    "parameters": {...}
  }
}

Tools available: {tool list with schemas}

Maintain the thought-action-observation pattern: think before acting, then evaluate the observation in your next thought. Terminate with a "finish" action when complete.
```

## Citations

- Wei et al. (2022) — Chain-of-Thought prompting (the immediate predecessor; ReAct extends CoT with actions)
- Chowdhery et al. (2022) — PaLM-540B (the primary backbone)
- Brown et al. (2020) — GPT-3 (the alternative backbone)
- Yang et al. (2018) — HotpotQA (the multi-hop QA benchmark)
- Thorne et al. (2018) — FEVER (the fact verification benchmark)
- Shridhar et al. (2020) — ALFWorld (the text-based game environment)
- Yao et al. (2022) — WebShop (the web navigation benchmark; first author's prior work)
- Baddeley (1992) — Working memory (cognitive science framing)
- Alderson-Day & Fernyhough (2015) — Inner speech (cognitive science framing)
- Ahn et al. (2022) — SayCan (the contemporary embodied-agent line)
- Nakano et al. (2021) — WebGPT (the browser-assisted QA line)
- Huang et al. (2022) — Inner Monologue (the limited verbal reasoning baseline)

(Full citations list in frontmatter `citations:` field.)

## Related Digests

- [[brown-2020-gpt3-few-shot]] — GPT-3 demonstrates in-context learning; ReAct uses it as the foundational mechanism
- [[lewis-2020-rag-knowledge-nlp]] — RAG retrieves once; ReAct retrieves iteratively, with reasoning steering each retrieval
- [[park-2023-generative-agents]] — Generative Agents builds on ReAct-style trajectories for simulated social behavior
- [[liu-2023-think-in-memory]] — Think-in-Memory generalizes ReAct's thought-action pattern to persistent memory operations

## Reviewer Notes

Hallucination check: **Clean**. Key claims verified: thought-action-observation interleaving pattern (§1, §2); HotpotQA + FEVER + ALFWorld + WebShop as four benchmarks (§1); Wikipedia API with three actions search/lookup/finish (§3.1 Action Space); PaLM-540B primary backbone, GPT-3 alternative (§2, footnote 1); 1-6 in-context examples (§3.2); 34% / 10% improvements on ALFWorld / WebShop vs imitation/RL with 10³-10⁵ training instances (§1, §4); CoT + ReAct hybrid is best on HotpotQA (§3); sparse thoughts for decision tasks (§2 last paragraph); thought editing as controllability (§1 contribution 1d, §4 Figure 5 reference). The "trajectory IS the working memory" framing in Key Takeaway and Implications is the digest's interpretive bridge — accurate for how ReAct actually operates and the right framing for memory-architect lens. The historical claim that ReAct is the prompting structure behind modern agent frameworks (LangChain, AutoGPT, LlamaIndex) is verified by the framework documentation lineage but not stated by the paper itself.
