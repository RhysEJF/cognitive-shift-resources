---
corpus: agentic-memory
kind: paper-digest
slug: mao-2026-agent-memory-circuits
title: "What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis"
authors:
  - "Xutao Mao"
  - "Jinman Zhao"
  - "Gerald Penn"
  - "Cong Wang"
year: 2026
publication_date: "2026-05"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/2605.03354"
doi: null
arxiv_id: "2605.03354"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Inside mem0 and A-MEM, the LLM grows its routing brain (add/update/delete/none) before it can reliably extract or ground content — so small-model agents are confidently moving memories around before they know what they say — and Write/Read converge on a late-layer hub that already exists in the base model as a generic context-grounding substrate that memory framing merely recruits."
topics:
  - agent-memory
  - mechanistic-interpretability
  - mem0
  - a-mem
  - circuit-analysis
  - failure-diagnostics
  - llm-scaling
  - sparse-feature-circuits
tags:
  - paper
  - memory-architecture
  - interpretability
  - engram-encode
  - engram-aggregate
  - engram-maintain
  - engram-ground
entities:
  - mao-xutao
  - zhao-jinman
  - penn-gerald
  - wang-cong
  - mem0
  - a-mem
  - qwen-3
  - longmemeval
related_digests:
  - chhikara-2025-mem0
  - adler-2026-storage-not-memory
  - latimer-2025-hindsight-memory
  - packer-2023-memgpt-os
citations:
  - title: "Mem0: Building production-ready ai agents with scalable long-term memory"
    authors: ["Prateek Chhikara", "Dev Khant", "Saket Aryan", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.19413"
  - title: "A-mem: Agentic memory for LLM agents"
    authors: ["Wujiang Xu", "Zujie Liang", "Kai Mei", "et al."]
    year: 2025
    venue: "NeurIPS"
    doi: null
    url: "https://openreview.net/forum?id=FiM0M8gcct"
    arxiv_id: null
  - title: "Longmemeval: Benchmarking chat assistants on long-term interactive memory"
    authors: ["Di Wu", "Hongwei Wang", "Wenhao Yu", "et al."]
    year: 2025
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=pZiyCaVuti"
    arxiv_id: null
  - title: "Memgpt: towards llms as operating systems"
    authors: ["Charles Packer", "Vivian Fang", "Shishir G Patil", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Transcoders find interpretable llm feature circuits"
    authors: ["Jacob Dunefsky", "Philippe Chlenski", "Neel Nanda"]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Circuit-tracer: A new library for finding feature circuits"
    authors: ["Michael Hanna", "Mateusz Piotrowski", "Jack Lindsey", "et al."]
    year: 2025
    venue: "BlackboxNLP Workshop"
    doi: "10.18653/v1/2025.blackboxnlp-1.14"
    url: "https://aclanthology.org/2025.blackboxnlp-1.14/"
    arxiv_id: null
  - title: "Latent planning emerges with scale"
    authors: ["Michael Hanna", "Emmanuel Ameisen"]
    year: 2026
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=H0B7pDTT0M"
    arxiv_id: null
  - title: "Locating and editing factual associations in GPT"
    authors: ["Kevin Meng", "David Bau", "Alex J Andonian", "et al."]
    year: 2022
    venue: "NeurIPS"
    doi: null
    url: "https://openreview.net/forum?id=-h6WAS6eE4"
    arxiv_id: null
  - title: "Mass-editing memory in a transformer"
    authors: ["Kevin Meng", "Arnab Sen Sharma", "Alex J Andonian", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=MkbcAHIYgyS"
    arxiv_id: null
  - title: "Dissecting recall of factual associations in auto-regressive language models"
    authors: ["Mor Geva", "Jasmijn Bastings", "Katja Filippova", "Amir Globerson"]
    year: 2023
    venue: "EMNLP"
    doi: null
    url: "https://openreview.net/forum?id=F1G7y94K02"
    arxiv_id: null
  - title: "RedeEP: Detecting hallucination in retrieval-augmented generation via mechanistic interpretability"
    authors: ["ZhongXiang Sun", "Xiaoxue Zang", "Kai Zheng", "et al."]
    year: 2025
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=ztzZDzgfrh"
    arxiv_id: null
  - title: "Retrieval head mechanistically explains long-context factuality"
    authors: ["Wenhao Wu", "Yizhong Wang", "Guangxuan Xiao", "et al."]
    year: 2025
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=EytBpUGB1Z"
    arxiv_id: null
  - title: "Sparse feature circuits: Discovering and editing interpretable causal graphs in language models"
    authors: ["Samuel Marks", "Can Rager", "Eric J Michaud", "et al."]
    year: 2025
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=I4e82CIDxv"
    arxiv_id: null
  - title: "Scaling sparse feature circuit finding for in-context learning"
    authors: ["Dmitrii Kharlapenko", "Stepan Shabalin", "Fazl Barez", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2504.13756"
  - title: "Towards automated circuit discovery for mechanistic interpretability"
    authors: ["Arthur Conmy", "Augustine N. Mavor-Parker", "Aengus Lynch", "et al."]
    year: 2023
    venue: "NeurIPS"
    doi: null
    url: "https://openreview.net/forum?id=89ia77nZ8u"
    arxiv_id: null
  - title: "Circuit component reuse across tasks in transformer language models"
    authors: ["Jack Merullo", "Carsten Eickhoff", "Ellie Pavlick"]
    year: 2024
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=fpoAYV6Wsk"
    arxiv_id: null
  - title: "Circuit compositions: Exploring modular structures in transformer-based language models"
    authors: ["Philipp Mondorf", "Sondre Wold", "Barbara Plank"]
    year: 2025
    venue: "ACL"
    doi: "10.18653/v1/2025.acl-long.727"
    url: "https://aclanthology.org/2025.acl-long.727/"
    arxiv_id: null
  - title: "Towards global-level mechanistic interpretability: A perspective of modular circuits of large language models"
    authors: ["Yinhan He", "Wendy Zheng", "Yushun Dong", "et al."]
    year: 2025
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Progress measures for grokking via mechanistic interpretability"
    authors: ["Neel Nanda", "Lawrence Chan", "Tom Lieberum", "et al."]
    year: 2023
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=9XFSbDPmdW"
    arxiv_id: null
  - title: "Llm circuit analyses are consistent across training and scale"
    authors: ["Curt Tigges", "Michael Hanna", "Qinan Yu", "Stella Biderman"]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving alignment and robustness with circuit breakers"
    authors: ["Andy Zou", "Long Phan", "Justin Wang", "et al."]
    year: 2024
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Debugging misaligned completions with sparse-autoencoder latent attribution"
    authors: ["Nicholas Betley", "Joshua Engels", "Thomas Ward", "et al."]
    year: 2025
    venue: "OpenAI Research Report"
    doi: null
    url: "https://alignment.openai.com/sae-latent-attribution/"
    arxiv_id: null
  - title: "Toward faithful retrieval-augmented generation with sparse autoencoders"
    authors: ["Guangzhi Xiong", "Zhenghao He", "Bohan Liu", "et al."]
    year: 2026
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=hgBZP67BkP"
    arxiv_id: null
  - title: "Contextfocus: Activation steering for contextual faithfulness in large language models"
    authors: ["Nikhil Anand", "Shwetha Somasundaram", "Anirudh Phukan", "et al."]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2601.04131"
  - title: "Evaluating very long-term conversational memory of LLM agents"
    authors: ["Adyasha Maharana", "Dong-Ho Lee", "Sergey Tulyakov", "et al."]
    year: 2024
    venue: "ACL"
    doi: "10.18653/v1/2024.acl-long.747"
    url: "https://aclanthology.org/2024.acl-long.747/"
    arxiv_id: null
  - title: "Evaluating memory in LLM agents via incremental multi-turn interactions"
    authors: ["Yuanzhe Hu", "Yu Wang", "Julian McAuley"]
    year: 2026
    venue: "ICLR"
    doi: null
    url: "https://openreview.net/forum?id=DT7JyQC3MR"
    arxiv_id: null
  - title: "Memory in the age of ai agents"
    authors: ["Yuyang Hu", "Shichun Liu", "Yanwei Yue", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2512.13564"
  - title: "Why do multi-agent LLM systems fail?"
    authors: ["Mert Cemri", "Melissa Z Pan", "Shuyi Yang", "et al."]
    year: 2025
    venue: "NeurIPS Datasets & Benchmarks"
    doi: null
    url: "https://openreview.net/forum?id=fAjbYBmonr"
    arxiv_id: null
  - title: "Which agent causes task failures and when? On automated failure attribution of LLM multi-agent systems"
    authors: ["Shaokun Zhang", "Ming Yin", "Jieyu Zhang", "et al."]
    year: 2025
    venue: "ICML"
    doi: null
    url: "https://openreview.net/forum?id=GazlTYxZss"
    arxiv_id: null
  - title: "A survey on the memory mechanism of large language model-based agents"
    authors: ["Zeyu Zhang", "Quanyu Dai", "Xiaohe Bo", "et al."]
    year: 2025
    venue: "ACM Trans. on Information Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Memory for autonomous llm agents: Mechanisms, evaluation, and emerging frontiers"
    authors: ["Pengfei Du"]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2603.07670"
  - title: "Memory-r1: Enhancing large language model agents to manage and utilize memories via reinforcement learning"
    authors: ["Sikuan Yan", "Xiufeng Yang", "Zuchao Huang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2508.19828"
  - title: "Atommem: Learnable dynamic agentic memory with atomic memory operation"
    authors: ["Yupeng Huo", "Yaxi Lu", "Zhong Zhang", "et al."]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2601.08323"
  - title: "Agentic memory: Learning unified long-term and short-term memory management for large language model agents"
    authors: ["Yi Yu", "Liuyi Yao", "Yuexiang Xie", "et al."]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2601.01885"
  - title: "Magma: A multi-graph based agentic memory architecture for ai agents"
    authors: ["Dongming Jiang", "Yi Li", "Guanpeng Li", "Bingzhe Li"]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2601.03236"
  - title: "Act-mem: Bridging the gap between memory retrieval and reasoning in llm agents"
    authors: ["Xiaohui Zhang", "Zequn Sun", "Chengyuan Yang", "et al."]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2603.00026"
  - title: "Memoryarena: Benchmarking agent memory in interdependent multi-session agentic tasks"
    authors: ["Zexue He", "Yu Wang", "Churan Zhi", "et al."]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2602.16313"
  - title: "Ama-bench: Evaluating long-horizon memory for agentic applications"
    authors: ["Yujie Zhao", "Boqin Yuan", "Junbo Huang", "et al."]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2602.22769"
  - title: "How memory management impacts llm agents: An empirical study of experience-following behavior"
    authors: ["Zihao Xiong", "Ying Lin", "Wenxuan Xie"]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generative agents: Interactive simulacra of human behavior"
    authors: ["Joon Sung Park", "Joseph O'Brien", "Carrie Jun Cai", "et al."]
    year: 2023
    venue: "ACM UIST"
    doi: null
    url: null
    arxiv_id: null
  - title: "Qwen3 technical report"
    authors: ["An Yang", "Anfeng Li", "Baosong Yang", "et al."]
    year: 2025
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2505.09388"
  - title: "Explaining neural scaling laws"
    authors: ["Yasaman Bahri", "Ethan Dyer", "Jared Kaplan", "et al."]
    year: 2024
    venue: "PNAS"
    doi: null
    url: null
    arxiv_id: null
  - title: "General agent evaluation"
    authors: ["Elron Bandel", "Asaf Yehudai", "Lilach Eden", "et al."]
    year: 2026
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2602.22953"
  - title: "Langchain"
    authors: ["Harrison Chase"]
    year: 2022
    venue: "GitHub"
    doi: null
    url: "https://github.com/langchain-ai/langchain"
    arxiv_id: null
  - title: "New embedding models and API updates"
    authors: ["OpenAI"]
    year: 2024
    venue: "Blog post"
    doi: null
    url: "https://openai.com/index/new-embedding-models-and-api-updates/"
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 6
  title: "Cross-system causal gaps across scale under mem0 (blue) and A-MEM (red)"
  page: 7
  image_path: "figures/mao-2026-agent-memory-circuits-fig.png"
---

# What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis

**Authors:** Xutao Mao, Jinman Zhao, Gerald Penn, Cong Wang
**Published:** 2026-05 · [Source](https://arxiv.org/abs/2605.03354)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Mao, Zhao, Penn and Wang open the black box of two production agent-memory frameworks — mem0 (flat key-value, semantic search) and A-MEM (Zettelkasten with self-linking) — by tracing feature circuits with pre-trained linear transcoders (163,840 features, ReLU) through every Write / Manage / Read forward pass on four Qwen-3 scales (0.6B, 4B, 8B, 14B), drawing 200 attribution graphs per operation per scale on LongMemEval (500 questions, 5 memory types). Two mechanistic findings drop out and one engineering deliverable. First, **control matures before content**: the Manage routing circuit (add/update/delete/none) is causally active at 0.6B (causal gap 0.259, CI excludes zero) while Write and Read circuits show no detectable signal until 4B — small agents route and rewrite memories before they can reliably extract or ground the underlying facts, and this asymmetry is identical under mem0 AND A-MEM. Second, **the late-layer "L34 hub" is recruited, not created**: a cluster of ~10 co-recurring features (F145627 the most recurrent) at L34 in 8B (migrating to L32-35 at 4B and L37-39 at 14B) is shared by Write and Read (Jaccard 0.111 vs Write-Manage 0.053; the gap widens monotonically to 14B), already exists in the base model as a generic context-grounding substrate, and memory framing recruits a **memory-specific** functional direction on it (∆M = -2.30 for memory-framed steering vs +0.32 for direct-context controls; cosine 0.74 between the two directions). Third, the feature-space separation enables a **zero-shot, unsupervised stage-level failure diagnostic** that localises silent failures to Write/Manage/Read at 76.2% accuracy at 8B — beating the strongest training-free baseline by 24.7 pp and a trained logistic-regression classifier by 13 pp, and generalising above 65% to LoCoMo and MemoryAgentBench without retraining. Steering circuits write-time, however, is fragile (8B is the only scale where every multiplier yields consistent fact-recall gains; 5× at 4B collapses recall by 62 pp); the actionable handle is reading circuits out, not writing through them.

## Key Takeaway

Inside mem0 and A-MEM, the LLM's routing brain matures **before** its content brain — at 0.6B Qwen-3 the Manage stage already issues structurally valid add/update/delete/none decisions while Write and Read have no detectable extraction or grounding circuit at all. Worse for memory architects: the Write/Read computation, when it eventually emerges at 4B, doesn't build its own machinery — it borrows a late-layer hub the base model already uses for generic in-context grounding, and "memory framing" merely tilts a delicate functional direction on top. This means the upper bound on a memory framework's reliability isn't set by your storage schema or your prompt engineering — it's set by how well your interface aligns with a direction that already exists inside the base model. Picking the wrong backbone size is therefore an unrecoverable architectural mistake: a 0.6B agent confidently routing memories it cannot read is the silent-failure regime, and no amount of mem0-vs-A-MEM framework switching will rescue it (the asymmetry transfers across both).

## Implications

- **(ENGRAM: Maintain / Encode) Verify extraction capability independently of routing competence when picking a backbone.** End-to-end accuracy is a liar at small scales — a model can route memories correctly while having no circuit for content extraction. For Flow OS / QMD, this means any agent under ~4B is structurally incapable of trustworthy Write, even if its delete/update logs look pristine. Add a per-stage benchmark (Write-only, Read-only) before committing to a backbone, not just LongMemEval-style end-to-end scores.

- **(ENGRAM: Aggregate / Ground) Stop expecting prompt engineering or storage-format changes to close the reliability gap between memory frameworks.** Both mem0 (flat key-value) and A-MEM (Zettelkasten graph) recruit the SAME L34 hub cluster despite radically different output formats — meaning the ceiling is the base model's pre-existing grounding axis, not the schema you wrap around it. If a framework underperforms, the fix is base-model alignment (or fine-tuning a grounding direction in), not another prompt rewrite.

- **(ENGRAM: Maintain) Ship per-stage circuit-diagnostic monitoring instead of single-number accuracy dashboards.** The paper's unsupervised 30-feature-bank ablation gets 76.2% accuracy localising whether Write, Manage, or Read failed — beating a trained classifier by 13 pp with zero supervision. Bolt this onto your memory system in prod: when a recall fails, you immediately know whether the fact was never extracted, was extracted-then-overwritten, or sits intact-but-ungrounded. Three different fixes, not one.

- **(ENGRAM: Aggregate) Don't try to "steer" agent memory via activation interventions outside an 8B-class regime.** Write-circuit amplification only yields consistent gains at 8B (5× → 93.2% fact recall, +3 pp); 5× at 4B collapses recall to 21.8% (a 62-point destruction). The narrow operating window means production steering is brittle; read-out diagnostics are the reliable handle.

- **(ENGRAM: Ground) The "silent failure" failure mode is structural, not a bug to patch.** Each Manage decision emits a syntactically legal token; each Write produces a well-formed JSON fact; each Read returns a fluent answer. Errors only surface when end-to-end accuracy tanks, and even then you can't say which stage failed. Treat per-stage observability (whether via circuits, LLM-judge per-stage flags, or both) as a first-class system property — not an optional add-on.

- **(ENGRAM: Encode / Network) When designing memory framings, design for **directional alignment** with the base model's grounding substrate.** The memory-derived steering direction got ∆M = -2.30; the direct-context-derived one got ∆M = +0.32 on the SAME questions — meaning the framing you wrap around retrieved content determines whether it activates the grounding axis at all. Concretely: presenting retrieved facts as `MEMORY: ...` triggers the axis; the same content as `here is a context block: ...` doesn't. Test your retrieval-injection prompt for this asymmetry before committing.

- **(ENGRAM: Maintain) Cross-system transfer of the diagnostic means you can build framework-agnostic memory observability.** Because the circuits are properties of the base model (Qwen-3 here) not the framework, the same diagnostic feature banks work whether you're running mem0, A-MEM, or your own. For Flow OS specifically, this means a single per-stage failure classifier could monitor multiple memory sub-systems (capture, qmd, learn-extractor) without per-system retraining — provided they share a backbone.

- **(ENGRAM: Aggregate) The L34 hub is the natural extension point for new memory ops.** New operations (e.g. a "contradiction-flag" stage) should be designed to recruit the same hub via memory-style framing, not invented as parallel machinery. The hub is the leverage point; anything that bypasses it sacrifices the directional grounding boost.

## How to Apply It (method)

**Scenario:** You're operating Flow OS in production with `/learn` extracting memories via a small (3-7B) backbone, and you've started seeing silent recall failures — users say "you should remember X" and the agent doesn't, even though X was in a transcript two sessions ago. End-to-end accuracy doesn't tell you whether the fact was never extracted, was extracted-then-overwritten by an `UPDATE` decision, or sits in `memory/` but isn't being retrieved-and-grounded into the answer. You want a per-stage diagnostic so the engineering team knows what to fix — the extractor, the deduper, or the retrieval-injection prompt.

**Steps:**

1. **Decompose your memory pipeline into Write / Manage / Read operations**: For Flow OS this maps to (a) `/learn` extractor → Write, (b) the `_should_create_memory` dedup-vs-existing decision → Manage, (c) `qmd query` hit + `UserPromptSubmit` injection → Read. Each must be its own forward pass with a stage-specific prompt ending in a structural JSON prefix (e.g. `{"facts": ["User`, `{"event": "`, `{"answer": "`) so the next token is the first content token.

2. **Pick the backbone and verify circuit maturity**: The paper shows Write/Read circuits are undetectable below 4B Qwen-3, peak at 4B, and distribute (and become harder to steer cleanly) by 14B. Before deploying, run a per-stage correctness audit: 100 sessions, Write-only judged for `extraction_correct=True`, Manage-only for `decision_correct=True`, Read-only for `retrieval_correct AND generation_correct`. If Write accuracy is below ~60% while Manage is above ~70%, you're in the control-before-content regime — upgrade the backbone, don't tune prompts.

3. **Pre-train (or download) per-layer transcoders for your backbone**: The paper uses the mwhanna Qwen-3 transcoder collection (dfeature = 163,840, ReLU, full-layer coverage). If you're on Qwen-3, reuse them directly. For Llama / Gemma / Mistral, you'd need to train transcoders (~100s of GPU-hours per scale; not cheap, but a one-time cost).

4. **Trace 200 attribution graphs per operation per scale on a held-out correct-only set**:
   ```
   For each operation in [Write, Manage, Read]:
     For each prompt in 200-prompt correct-only sample:
       1. Replace each MLP with its transcoder + input-specific error term.
       2. Freeze attention patterns and LayerNorm denominators.
       3. Backward pass from target logit (top prediction at JSON-prefix
          position, covering ≥80% cumulative probability, up to 5 logits).
       4. Keep top 4,096 feature nodes; prune to 80% node / 95% edge influence.
   Aggregate: across the 200 graphs, count feature recurrence; keep the
              50-200 most-recurrent features as the "operation circuit."
   ```

5. **Build the per-operation diagnostic feature bank**: For each operation, select the **top-10 features per characteristic layer group** (e.g. for Write at 8B: L22 subject-anchoring, L28 word-specific, L34 hub cluster) chosen for *between-operation discriminability* — features that activate strongly for that operation but weakly for the other two. That's 30 features per operation.

6. **Deploy as a zero-shot failure classifier**:
   ```
   On every prod failure (any session where end-to-end answer is wrong):
     For each operation in [Write, Manage, Read]:
       Zero-ablate that operation's 30-feature bank during a re-run.
       Measure output disruption (∆ in log-prob of the failed answer).
     Flag the operation whose ablation causes the LARGEST disruption.
   ```
   The largest-disruption operation is the one most causally responsible for the (failed) output and therefore the failure point.

7. **Route fixes by stage**: If Write is flagged → improve the extraction prompt or upgrade the extractor model. If Manage is flagged → tighten the dedup-vs-existing logic, raise similarity threshold, or constrain `UPDATE`/`DELETE` decisions. If Read is flagged → fix retrieval scoring, increase top-k injected memories, or rewrite the injection prompt to match a `MEMORY:` framing the base-model grounding axis recognises.

8. **Sanity-check on a known-good benchmark**: The paper's diagnostic generalises above 65% on LoCoMo and MemoryAgentBench without retraining. Run yours on at least one OOD benchmark to confirm the per-stage feature banks aren't overfit to LongMemEval-style failures.

**Expected outcome:** You end up with a single, framework-agnostic, training-free observability layer that turns every silent memory failure in production into a 3-class diagnosis (Write fail / Manage fail / Read fail) with ~76% accuracy at 8B-scale backbones. Engineering can then route fixes to the responsible stage instead of guessing — and the diagnostic survives prompt rewrites, schema changes, and even framework swaps because it indexes the base model's circuits, not the wrapper.

## Best Figure

![Figure 6 — Cross-system causal gaps across scale under mem0 (blue) and A-MEM (red) (page 7)](figures/mao-2026-agent-memory-circuits-fig.png)

```
Image Candidates:
Figure 4 (p. 5): Causal verification across scale under zero ablation — shows the Write/Read peak at 4B and the decline at 8B-14B, but only inside mem0.
Figure 5 (p. 6): Jaccard heatmap and content-vs-cross-family divergence — shows the Write/Read vs Write/Manage separation widening with scale, the geometric core finding.
Figure 6 (p. 7): Cross-system causal gaps under mem0 (blue) and A-MEM (red) — three side-by-side bar plots showing the control-before-content asymmetry holds identically across BOTH frameworks at every scale.

Best Image:
Figure Name: Figure 6: "Cross-system causal gaps across scale under mem0 (blue) and A-MEM (red)"
Figure Page: 7
Slide Caption: Manage circuitry is causally active at 0.6B in BOTH mem0 and A-MEM, while Write and Read produce no detectable signal until 4B — control matures before content, and the pattern is a property of the base model, not the wrapper.
Description: Figure 6 is a three-panel bar chart (Write | Manage | Read) where each panel plots the causal gap (y-axis, 0.0 to 0.6+) at four model scales (0.6B, 4B, 8B, 14B) for both mem0 (blue) and A-MEM (red). The plot makes the paper's most important claim visible in a single glance: Manage has detectable blue AND red bars at 0.6B, while Write and Read have essentially zero bars at 0.6B and only emerge from 4B onward — under both frameworks. This is the figure that converts "we found this in mem0" into "this is a property of how agent memory computes inside the base LLM," and it's why the diagnostic transfers across systems.
```

## What Experts Overlook

The most easily-missed detail is that **all circuits are traced exclusively on correct-only instances**, filtered by a per-stage Qwen-3 32B judge before any feature attribution runs (Section C, paragraph "Sampling pipeline"). That means the "absence of Write/Read circuits at 0.6B" is not a claim that the 0.6B model gets Write wrong (it does, but that's a separate matter) — it's a claim that **even on the few cases where 0.6B happens to produce a correct Write output, no recurrent feature circuit is detectable behind that success**. The 0.6B model isn't extracting via a different (smaller) circuit; it's getting the right answer through a distributed or non-MLP route that the transcoders cannot resolve. The discovered circuits therefore reflect **successful** computation, not failure modes, and the absence-at-0.6B finding is a statement about the *mechanism of success*, not about overall accuracy.

**Why it matters:** This is the load-bearing methodological choice that turns the paper's central asymmetry from "small models are bad at content" (trivial, known) into "small models that *succeed* at content do so without a localisable circuit" (non-trivial, and what licenses the deployment-regime warning). Without the correct-only filter, you couldn't distinguish "no signal because the model failed" from "no signal because the model used a different mechanism." For a memory-architecture researcher, this means: **a small backbone's good per-stage scores on an easy benchmark do not imply it has learned a robust mechanism** — it may be succeeding via a brittle, distributed path that breaks the moment your prompts shift. Per-stage accuracy alone is insufficient evidence of mechanistic maturity.

**Example of good use (memory architectures for agentic OSes):** Before promoting a smaller backbone (say, Qwen-3 4B) into Flow OS production to save GPU cost, run the correct-only circuit-detection check on its Write stage. If 200 successful Write attribution graphs converge on a recurrent feature cluster (e.g. the paper's L22 → L28 → L34 path), the model has mechanistic Write maturity and is safe at 4B. If 200 attribution graphs produce no convergent recurring features, the model is succeeding *contingently* — and any prompt drift or domain shift will silently degrade Write quality. Reject the backbone, even if its raw Write accuracy looks acceptable.

**Example of misapplication:** A team benchmarks a 0.6B model on a curated 100-question LongMemEval slice and sees 70% Write correctness. Reading "control-before-content" as "Manage > Write at small scales" (which is in the abstract), they conclude the 0.6B model is mature enough for Write because its raw accuracy is "good enough." They deploy it. In production, distribution shifts arrive (longer sessions, novel entity types, multi-language input) and Write quality collapses to ~30% — because there was never a robust circuit, only a coincidentally-correct distributed computation that broke under shift. The correct-only filter is the methodological warning sign they ignored: in the paper, 0.6B never showed a circuit *even on its successes*.

## Extracted Prompts

**Prompt explanation:** mem0 Write — system prompt + JSON prefix used by the Write extraction operation. The model is positioned so the next predicted token is the first content word of an extracted fact.

```
System: You are a personal information organizer. Extract distinct facts about the user from the conversation as complete sentences.
User: {session_text}
Assistant JSON prefix: {"name": "add_to_memory", "arguments": {"facts": ["User
```

**Prompt explanation:** mem0 Manage — system prompt + JSON prefix used by the Manage routing operation. The next predicted token is the routing decision (ADD / UPDATE / DELETE / NONE).

```
System: You are a memory manager. Compare the new fact with the existing memory and choose one operation: ADD, UPDATE, DELETE, or NONE.
User: Existing memory: {mem}
New fact: {new}
Assistant JSON prefix: {"event": "
```

**Prompt explanation:** mem0 Read — system prompt + JSON prefix used by the Read grounding operation. The next predicted token is the first content word of the grounded answer.

```
System: You answer questions grounded in the provided memories. Give a concise answer.
User: MEMORY: {mem}
QUESTION: {q}
Assistant JSON prefix: {"answer":"
```

**Prompt explanation:** A-MEM Write (Note Construction, Ps1) — generates a structured analysis (keywords / context / tags) instead of a plain fact sentence.

```
System: Generate a structured analysis of the content: identify salient keywords, summarize the context in one sentence, and assign categorical tags.
User: {text}
Assistant JSON prefix: {"keywords": ["
```

**Prompt explanation:** A-MEM Manage (combined Evolution prompt, Ps2) — single LLM call that decides whether the new note should evolve and which neighbors to strengthen / update.

```
System: You are a memory evolution agent. Given the new memory note and its nearest neighbors, decide whether the note should evolve and which actions to take (strengthen connections, update_neighbor context and tags).
User: New note: {note}
Neighbors: {nbrs}
Assistant JSON prefix: {"should_evolve":
```

**Prompt explanation:** A-MEM Read — single-operation Read prompt constructed by the authors (A-MEM itself doesn't use an LLM for retrieval); consumes `[text | keywords | context]` memory triples.

```
System: Answer the question grounded in the provided memories. Give a concise answer.
User: Memories: {mems}
Question: {q}
Assistant JSON prefix: {"answer": "
```

## Citations

- Chhikara et al. (2025) — *Mem0: Building production-ready AI agents with scalable long-term memory* — arXiv:2504.19413 (the primary system analysed; this paper is essentially the mechanistic counterpart to that one's behavioural claims)
- Xu et al. (2025) — *A-MEM: Agentic memory for LLM agents* — NeurIPS 2025 (the second system; Zettelkasten-style)
- Wu et al. (2025a) — *LongMemEval: Benchmarking chat assistants on long-term interactive memory* — ICLR 2025 (the evaluation benchmark; 500 questions, 5 memory types)
- Packer et al. (2023) — *MemGPT: towards LLMs as operating systems* (foundational paged-virtual-memory framing for agent memory)
- Dunefsky et al. (2024) — *Transcoders find interpretable LLM feature circuits* — NeurIPS 2024 (the transcoder mechanism this paper builds on)
- Hanna et al. (2025) — *Circuit-tracer: A new library for finding feature circuits* — BlackboxNLP 2025 (the circuit-tracing toolchain)
- Hanna & Ameisen (2026) — *Latent planning emerges with scale* — ICLR 2026 (the methodological template for cross-scale circuit analysis on Qwen-3)
- Meng et al. (2022) — *Locating and editing factual associations in GPT* — NeurIPS 2022 (ROME; the closest single-turn analogue)
- Meng et al. (2023) — *Mass-editing memory in a transformer* — ICLR 2023 (MEMIT)
- Geva et al. (2023) — *Dissecting recall of factual associations in auto-regressive language models* — EMNLP 2023

(Full citation list of 43 entries in frontmatter.)

## Related Digests

- [[chhikara-2025-mem0]] — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (this paper opens mem0's black box mechanistically — Chhikara et al. is the system under the microscope here, and the L34 hub being "recruited, not created" reframes Mem0's whole design as a base-model alignment problem rather than a storage / prompt-engineering one)
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall (Adler & Zehavi argue write-time LLM distillation is anti-intelligence because it discards information before the query is known; Mao et al. supply the mechanistic flip-side — at small scales the *write circuit itself doesn't exist*, so write-time intelligence isn't merely lossy, it's structurally absent below 4B)
- [[latimer-2025-hindsight-memory]] — Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects (Latimer et al. show architecture > parameter count for memory accuracy; Mao et al. show *why* — because the heavy lifting happens on a hub the base model already has, so smart wrapping of that hub beats throwing more parameters at it)
- [[packer-2023-memgpt-os]] — MemGPT: Towards LLMs as Operating Systems (Packer et al. introduced the OS metaphor for memory; Mao et al.'s control-before-content finding is the warning that the "OS" can confidently issue page-in/page-out commands at scales where it cannot reliably read the pages — a structural failure mode the OS framing doesn't surface)

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim above (causal gaps 0.259 at 0.6B Manage; Jaccard 0.111 Write-Read vs 0.053 Write-Manage at 8B; ∆M = -2.30 vs +0.32 steering effect; cosine 0.74 between memory-derived and direct-context directions; 76.2% diagnostic accuracy beating training-free by 24.7 pp and trained by 13 pp; 5× amplification at 4B collapsing fact recall to 21.8%; > 65% diagnostic accuracy on LoCoMo and MemoryAgentBench; 163,840 transcoder features; ≥97% top-1 replacement-model agreement; 200 attribution graphs per operation per scale; LongMemEval 500 questions / 5 memory types) is traceable to the paper text (Sections 4–7, Tables 1–7, Figures 3–7). The framing claims — control-before-content asymmetry, hub recruited not created, ENGRAM-dimension mapping in the Implications section — are direct restatements of the paper's own claims or load-bearing reframings consistent with the lens. No fabricated metrics, no invented method names, no overextended generalisations beyond Qwen-3 + mem0 + A-MEM + LongMemEval. Two soft caveats worth noting (not severity-raising): (1) ENGRAM mapping in Implications is the lens's framework, not the paper's; (2) the Flow OS application scenarios in Method and What Experts Overlook are lens-tailored use cases, not claims the paper makes.
