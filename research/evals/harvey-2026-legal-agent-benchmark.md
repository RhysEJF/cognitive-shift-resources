---
kind: paper-digest
corpus: evals
slug: harvey-2026-legal-agent-benchmark
title: "Introducing Harvey's Legal Agent Benchmark (LAB): Open-Sourcing Harvey's Long Horizon Legal Agent Benchmark"
authors:
  - "Grupen, N."
  - "Pereyra, G."
  - "Pereyra, J."
year: 2026
publication_date: "2026-05"
venue: "Harvey blog (announcement post, 6 May 2026; companion Initial Results post, 26 May 2026; open-source repo harveyai/harvey-labs v1.0)"
source_url: "https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark"
supplementary_url: "https://github.com/harveyai/harvey-labs"
doi: null
arxiv_id: null
lens: eval-designer
digested_date: "2026-10-01"
key_takeaway: "Nothing about the agents changed and the score went up by half: Harvey's own changelog records that switching from one LLM judge to two averaged judges moved all-pass on the same ten Claude Opus 4.8 runs from 10.0% to 15.0%, and reordering the judge's JSON so the reasoning comes before the verdict flipped 3 of 3 replays of a borderline criterion."
topics:
  - real-world-evals
  - legal-agents
  - rubric-grading
  - all-pass-scoring
  - llm-as-judge
  - long-horizon-knowledge-work
  - agent-trace-analysis
tags:
  - paper
  - benchmark
  - harvey
  - legal-ai
  - all-pass
  - dual-judge
  - eval-design
  - vals-ai
entities:
  - niko-grupen
  - gabe-pereyra
  - julio-pereyra
  - spencer-poff
  - harvey
  - vals-ai
related_digests:
  - patwardhan-2025-gdpval-economic-tasks
  - starace-2025-paperbench-replication
  - mazeika-2025-remote-labor-index
  - chan-2024-mle-bench
citations:
  - title: "LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models"
    authors: ["Neel Guha", "Julian Nyarko", "Daniel E. Ho", "et al."]
    year: 2023
    venue: "NeurIPS Datasets and Benchmarks (named in text only; no bibliography in source)"
    doi: null
    url: null
    arxiv_id: null
  - title: "CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review"
    authors: ["Dan Hendrycks", "Collin Burns", "Anya Chen", "et al."]
    year: 2021
    venue: "NeurIPS Datasets and Benchmarks (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "LEXam: Benchmarking Legal Reasoning on 340 Law Exams"
    authors: ["Yu Fan", "et al."]
    year: 2025
    venue: "preprint (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "BigLaw Bench"
    authors: ["Harvey AI"]
    year: 2024
    venue: "Harvey blog (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "SWE-Bench Pro"
    authors: ["Scale AI"]
    year: 2025
    venue: "preprint (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "SWE-bench Verified"
    authors: ["OpenAI"]
    year: 2024
    venue: "OpenAI blog (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Terminal-Bench 2.0"
    authors: ["Terminal-Bench team"]
    year: 2025
    venue: "preprint (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks"
    authors: ["Tejal Patwardhan", "et al."]
    year: 2025
    venue: "arXiv preprint, OpenAI (named in text only; digested in this corpus)"
    doi: null
    url: null
    arxiv_id: null
  - title: "OSWorld-Verified"
    authors: ["Tianbao Xie", "et al."]
    year: 2025
    venue: "xlang.ai report (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents"
    authors: ["Jason Wei", "et al."]
    year: 2025
    venue: "OpenAI preprint (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "MCP Atlas"
    authors: ["Scale AI"]
    year: 2025
    venue: "benchmark report (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "FinanceAgent"
    authors: ["Vals AI"]
    year: null
    venue: "benchmark (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Humanity's Last Exam"
    authors: ["Long Phan", "et al."]
    year: 2025
    venue: "preprint (named in text only)"
    doi: null
    url: null
    arxiv_id: null
  - title: "APEX-Agents"
    authors: ["Mercor"]
    year: null
    venue: "benchmark report (named in text only)"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Minor fact tweak"
best_figure:
  number: null
  title: "Criteria Pass Rate vs. Task Resolution (Vals AI held-out leaderboard page, running Harvey's protocol)"
  page: null
  image_path: null
---

# Introducing Harvey's Legal Agent Benchmark (LAB): Open-Sourcing Harvey's Long Horizon Legal Agent Benchmark

**Authors:** Niko Grupen, Gabe Pereyra, Julio Pereyra (Harvey). Spencer Poff led the open-source harness and sandboxing; Julio Pereyra led task design and the document/scenario generation pipeline.
**Published:** 2026-05 (announcement post 6 May 2026; Initial Results post 26 May 2026; repo created 30 Mar 2026, v1.0) · [Announcement](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) · [Repo](https://github.com/harveyai/harvey-labs) · [Initial Results](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results) · [Vals held-out leaderboard](https://vals.ai/benchmarks/hlab)
**Lens:** `eval-designer` · **Digested:** 2026-10-01
**Source used:** the announcement blog post (HTML) as primary. No paper or technical report exists; the repo README cites the blog post as the canonical reference (BibTeX author "Harvey AI", 2026, v1.0). Supplementary: Harvey's Initial Results post (26 May 2026), the repo's `docs/eval-strategies.md`, `docs/architecture.md`, `CHANGELOG.md`, harness system prompt, judge prompt template and one `task.json`, and the Vals AI held-out leaderboard page plus mirrors (all fetched 1 Oct 2026). Numbers are attributed to their source throughout.

## TLDR

Harvey built LAB to answer one question for law firms: which parts of an associate's work can an agent do all of, some of, or none of. Each task is a partner-style instruction (about 50 words on average, written as an affirmative request with no format or style guidance), a closed-universe client matter (matter files, firm templates, emails; the blog's example M&A data room holds eight material contracts plus adjacent material such as a 10-K and a deferred compensation plan, and the matching task in the public repo has 19 documents), and a required deliverable (a .docx memo, .xlsx table, .pptx deck or markdown file), graded against expert-written binary pass/fail criteria each tied to one deliverable file (the change-of-control example has 57 criteria covering 9 planted issues, 4 to 9 criteria per issue). Launch size: 1,250 tasks, 24 practice areas, more than 75,000 criteria; the repo on 1 Oct 2026 lists 2,010 tasks, 27 practice areas and about 114,000 criteria. Documents are synthetic, generated in batches under lawyer review, and the tutorial says they contain imperfections. The agent runs in a network-less Podman sandbox with six tools (bash, read, write, edit, glob, grep), a finish tool added in September, and three file-format skills (docx, xlsx, pptx). The score is all-pass: a task counts only if every criterion passes, and criterion pass rate is reported as a diagnostic. Two LLM judges (Claude Sonnet 4.6 and GPT-5.5) grade each criterion in a separate call at temperature 0 where the model accepts it (GPT-5.5 does not, so it runs at default sampling), seeing only the deliverable and the criterion text, never the source documents or a gold answer; the headline is the mean of the two judges' all-pass rates. On Harvey's private hold-out in May 2026: Claude Opus 4.7 7.1%, Sonnet 4.6 5.4%, Opus 4.6 4.2%, GPT-5.5 2.1%, Gemini 3.5 Flash 0.8%, with Opus 4.7 costing about $50.90 and 22 minutes per task, and a different model leading each of three practice-area groupings. By late September 2026 on Vals AI's run of the same hold-out, Muse Spark 1.2 led at 25.42% all-pass while passing 94.52% of criteria, Grok 4.6 15.83%, Kimi K3 (best open-weight) 10.83%, Claude Fable 5 11.25% at $19.23 per task, GPT-5.5 3.75%, and 17 configurations scored 0.00%. Trace analysis on the hold-out found that agents that revise their draft after checking it score 1.5 points of all-pass higher on average, agents that draft without review 1.2 points lower, and five or more tool calls in one turn 0.5 points lower. The number to carry away: top agents clear about 9 in 10 of the checks a partner would make and still fail about 3 tasks in 4, because the one check they miss is the one the eval refuses to forgive.

## The Four Questions (lens read)

- **The question.** In Harvey's words: "to provide a clear picture of how agents can be deployed to support legal work in the real world. By articulating where agents can do all, some, or none of a task, LAB helps law firms measure the ROI of AI investments." It is a delegation question dressed as a capability index: the unit is a task a partner hands an associate, and the pass bar is partner review. Why this instance: coding agent benchmarks (SWE-Bench Pro, SWE-Bench Verified, Terminal-Bench 2.0) jumped at the same time Harvey's engineers felt coding agents start to work (Karpathy: "basically didn't work before December and basically work since"), and nothing in legal measured long-horizon work; LegalBench, CUAD, LEXam and Harvey's own BigLaw Bench grade short-horizon reasoning (read a contract, answer a question).
- **The instrument.** Environment: a closed-universe client matter mounted read-only in a Podman sandbox with no network, six workspace tools plus `finish`, and skill manuals for .docx, .xlsx and .pptx. Horizon: one instruction to one or more deliverable files; under 6 to about 22 minutes of wall-clock per task for the May baselines, and up to 3,337 seconds (about 56 minutes) for Claude Opus 5 on Vals. One run = one trajectory on one task, graded once by each of two judges. Scale: 1,250 tasks at launch, 2,010 now; the hold-out size is not published (Vals scores are all multiples of 0.42 points, which fits roughly 240 tasks, or 120 with the half-credit dual-judge rule; that is this digest's inference, not a stated figure). Primary metric: all-pass rate, ceiling 100%, headline = mean of the two judges' all-pass rates, with both-judges-agree all-pass and criterion pass rate (pooled and macro) reported alongside. Baseline: none. No human associate ran the tasks, no rule-based baseline, no oracle. Spread: Harvey reports none; Vals shows a standard error per model (2 to 3 points at the 10 to 20% level); no repeat runs per task, no pass^k. The choices that made the headline possible: all-pass with no partial credit, which turns a 90% criterion pass rate into a 10 to 25% task rate, and judge-only grading with no gold answer, which is what lets 114,000 criteria be graded at all.
- **The result and the surprise.** May hold-out: Opus 4.7 7.1%, Sonnet 4.6 5.4%, Opus 4.6 4.2%, GPT-5.5 2.1%, Gemini 3.5 Flash 0.8%, under 10% in aggregate. Jagged by practice area: GPT-5.5 led the regulated and emerging-company groups (retrieval-heavy), Opus 4.7 corporate transactions and funds (synthesis), Sonnet 4.6 privacy, tax and private-client (comparison against statutes). Cost: Opus 4.7 about $50.90 and 22 minutes per task; GPT-5.5 about 3x cheaper; Gemini 3.5 Flash under 6 minutes. Vals, September: Muse Spark 1.2 25.42% all-pass and 94.52% criteria; Claude Fable 5 11.25% (it fell back to Opus 4.8 on 4 tasks; 10.42% counting those as failures); MiniMax M3 4.17% at $1.46 per test against Fable 5 at $19.23. The surprise the authors flag is that no model leads every practice area. The surprise for an eval designer is the grader lever recorded in the repo changelog: switching to two averaged judges moved the same ten Opus 4.8 runs from 10.0% to 15.0% all-pass (criterion pass 78.9% to 80.6%), and putting reasoning before verdict in the judge's JSON flipped 3 of 3 replays of one borderline criterion. Where a script or human beat the models: not tested; there is no human or rule-based run. Where decomposition showed progress the end-to-end number hid: criterion pass rates of 90.0 to 94.5% for the top eight models on Vals against 10.0 to 25.4% task rates, and the action-level traces (read, search, execute, write, validate, edit) in which revise-after-check is worth 1.5 points.
- **What it does not test, and what to borrow.** Untested: a human baseline; adversaries (no counterparty, no opposing counsel, no changing facts, no documents crafted to mislead the agent, although the sandbox threat model does mention crafted .docx); real stakes (no client, no money, no consequence for a wrong memo); outsiders (no partner to ask a clarifying question; one shot); the hold-out is private, so nobody outside Harvey and its partners can audit it, while the public set is MIT-licensed and will end up in training data. Gaming and saturation: the top score went from 7.1% in May to 25.42% in September, partly new models and partly harness and grading changes the changelog itself says are not comparable across lines (finish tool 3 Sept, dual-judge default 26 Aug, reasoning-first 24 Aug); the system prompt lists `task.json`, which holds the rubric, under the workspace layout and tells the agent not to read it on pain of a rule-violation flag; the public docs do not say whether the file is actually reachable inside the sandbox. LLM judges: the two judges (Sonnet 4.6, GPT-5.5) are also contestants; each judge sees only the deliverable and the criterion text, not the source documents, so it checks whether the memo says what the rubric expects, not whether the memo is true to the record. Simulation awareness: documents are synthetic with imperfections, and nothing is reported about whether agents notice. Borrow: (1) all-pass over atomic binary criteria, each tied to one deliverable file and written as "PASS if ... FAIL if ...", with criterion pass rate published next to it; (2) partner-style short instructions over a matter that mixes key and peripheral files, so the eval tests discovery as well as execution; (3) a score-impact changelog with four surfaces (harness, grading, dataset, adapter) and a comparability verdict on every entry, plus two judges from different families averaged; (4) tagged action traces so a score can be explained, not just reported.

## Key Takeaway

Nothing about the agents changed and the score went up by half: Harvey's own changelog records that switching from one LLM judge to two averaged judges moved all-pass on the same ten Claude Opus 4.8 runs from 10.0% to 15.0%, and reordering the judge's JSON so the reasoning comes before the verdict flipped 3 of 3 replays of a borderline criterion. On a benchmark where the top agent clears 94.5% of individual criteria but only 25.4% of tasks, every task sits one judge call away from flipping, so the grader is a bigger lever than the model, and an eval that refuses partial credit has to treat its judge as part of the thing under test.

## Implications

- **Grade the whole job all-pass and publish criterion pass rate next to it**: LAB marks a 57-criterion memo failed if one criterion fails, and records `n_passed / n_criteria` alongside. For a purchase made on someone's behalf, write the constraints as binary criteria (right item, within budget, seller rating above threshold, condition as specified, delivered by the date) and count the purchase as a pass only if all hold; publish the criterion rate so readers can tell near-misses from disasters.
- **Expect the criterion-to-task gap to be the whole story, and size the eval for it**: on Vals the top eight models pass 90.0 to 94.5% of criteria and 10.0 to 25.4% of tasks. An agent that independently clears 9 in 10 constraints will all-pass a 10-constraint trade about 35% of the time (0.9^10, this digest's arithmetic), so differences between agents live in a narrow band and you need hundreds of tasks; Vals's standard errors of 2 to 3 points at the 10 to 20% level show how noisy a few hundred tasks still is.
- **Treat the judge as part of the instrument and version it like code**: the changelog shows the dual-judge switch lifting all-pass from 10.0% to 15.0% on identical runs and a field reorder in the judge's output schema flipping 3 of 3 borderline verdicts. Pin judge models, log every grading change with a "comparable or not" verdict, and never put scores from both sides of a grading change on one chart.
- **Give the judge the record when the fact is checkable**: LAB's judge sees only the deliverable plus the criterion text, with no source documents and no gold answer, so it tests whether the memo says the expected thing. For a money agent most criteria are checkable against ground truth (listing price, account balance, order id, delivery date); grade those with code against the record and keep the LLM judge for the judgement calls.
- **Write the brief the way the principal would, and plant distractors**: LAB instructions average 50 words and the matter mixes key and peripheral files (19 documents, 8 that matter, in the example). Give your agent a short brief from the person and a market with decoy listings that each fail one constraint; part of what you are testing is whether it finds the right items, not just whether it transacts.
- **Tag the revise-after-check behaviour from day one**: agents that changed the deliverable after checking it scored 1.5 points of all-pass higher on average, agents that drafted without review 1.2 points lower, and five or more tool calls in one turn 0.5 points lower (correlations on the hold-out, not ablations). These are the harness levers you will pull later; record the action trace so you can measure them.
- **Put cost and latency on the leaderboard**: Opus 4.7 led May's hold-out at about $50.90 and 22 minutes per task; on Vals, Fable 5 (11.25%) cost $19.23 per task against MiniMax M3 (4.17%) at $1.46 and Muse Spark 1.1 (20.00%) at $0.80. For an agent spending someone's money, inference cost is part of the price of the purchase.
- **Do not publish model numbers without a human floor**: LAB has no associate baseline, so nobody can say whether 25% all-pass is above or below what a second-year associate would get on 57 binary criteria. Have a few people run a sample of your tasks under the same rubric before the first leaderboard goes out.

## How to Apply It (method)

**Scenario:** You are building an eval for an agent that buys on a person's behalf in a live secondary market (say, used titanium gravel frames). You want a LAB-style instrument: a short brief from the principal, a closed universe of listings and messages with planted facts, a required deliverable, binary expert criteria, all-pass grading with two judges, and a changelog so scores stay comparable.

**Steps:**

1. **Write each task as the principal would**: 30 to 60 words, affirmative, no format spec, one or more named output files. LAB's example instruction is 24 words plus an output line: "Review the attached acquisition data room contracts and internal memo for change of control and assignment provisions, and prepare a comprehensive deal team report." Yours:

   ```
   Find me a size 56 titanium gravel frame under 1,800 GBP with no cracks or
   dents, from a seller who ships to the UK, and buy it by Friday. Put the
   order confirmation and a one-page summary of what you checked in output/.
   ```

2. **Build the matter as a frozen, closed universe**: 20 to 60 listings, the seller message threads, the principal's budget note, and a few irrelevant files (an old invoice, an unrelated email). LAB mixes key and peripheral files on purpose and mounts documents read-only; do the same. If you generate the corpus synthetically, do it in batches under a human reviewer and say so in the docs, as LAB's tutorial does.

3. **Plant the facts the agent must find**: for each task, 5 to 10 facts a careful buyer would discover (hidden damage disclosed in message 4 of a thread, a shipping exclusion in a listing footer, a price that excludes VAT, a seller whose rating is below the bar). Pin each fact to the file it lives in, as LAB's optional `sources` field does.

4. **Write the rubric as atomic binary criteria, one per planted fact or required decision, each tied to one deliverable**: use LAB's `match_criteria` form, which carries the expected answer inside the criterion so the judge never needs a gold file:

   ```
   id: C-004
   title: Identifies the frame's disclosed top-tube dent
   match_criteria: PASS if the summary states that listing #1187's seller
   disclosed a dent in the top tube (message 4 of the thread) and treats it
   as disqualifying under the no-dents constraint. FAIL if the dent is not
   mentioned or the listing is recommended without it.
   deliverables: [summary.md]
   sources: [threads/listing-1187.eml]
   ```

   Keep only criteria the principal would actually check; LAB's docs warn that "nice-to-have" padding drags the all-pass rate down without adding signal.

5. **Fix the harness and record it**: tools (read, search, bash, write, finish), a sandbox with no outbound network except a stub of the market API, max turns, temperature and reasoning effort written to `config.json`, and a trace in which every call is tagged with one of LAB's six actions (read, search, execute, write, validate, edit).

6. **Grade with two judges from different families, one call per criterion, at temperature 0**: use LAB's judge prompt (below, under Extracted Prompts). For criteria that are checkable against the record (price under budget, order placed, date met), grade with code instead of a judge. Task score = 1 only if all criteria pass. Headline = mean of the two judges' all-pass rates; also report both-judges-agree all-pass and criterion pass rate, pooled and per task.

7. **Run a human floor**: 3 to 5 people do 20 of the tasks under the same rubric and the same judges. LAB skipped this; you should not.

8. **Keep a score-impact changelog**: four surfaces (harness, grading, dataset, adapter), one entry per change, each stating which scores move and whether results across that line are comparable, with an opt-out flag where one exists. Publish every result with the commit it was produced at.

9. **Keep a private hold-out that mirrors the public set's distribution**: publish the public set; run the leaderboard on the hold-out; hand the hold-out to a third party (LAB uses Vals AI and Artificial Analysis) so the numbers are not only yours.

**Expected outcome:** a leaderboard with all-pass, criterion pass, cost and latency per model, a human floor to read it against, and tagged traces that tell you which constraint the agent misses most and whether it revises after checking. The all-pass number will look low; the criterion rate and the trace tags are what tell you whether the agent is close.

## Best Figure

_(figure not extracted: the primary source was fetched as HTML, no source PDF available; the launch post's images are illustrative diagrams and a practice-area bar chart with no numeric labels in the text)_

```
Image Candidates:
Figure "Criteria Pass Rate vs. Task Resolution" (Vals AI hold-out page, web): paired bars per model, criteria pass 90.0 to 94.5% beside task resolution 10.0 to 25.4%; the all-pass story in one view.
Figure 5 (Initial Results post, web): "Agent behaviors", eight trace behaviours with a frequency column and the average change in all-pass (from +1.5 for revise-after-check to -1.2 for drafting without review).
Figure 3 (Initial Results post, web): "Cost and latency trade-offs", per-task cost against per-task latency for every baselined configuration, with Opus 4.7 the most expensive and slowest point at about $50.90 and 22 minutes.

Best Image:
Figure Name: "Criteria Pass Rate vs. Task Resolution" (Vals AI leaderboard page for Harvey's Legal Agent Benchmark)
Figure Page: 1
Slide Caption: On Harvey's hold-out, the top agent passes 94.5% of individual rubric criteria and 25.4% of tasks; all-pass grading is the gap between those two bars.
Description: The Vals chart lists, for each model, two numbers side by side: the share of rubric criteria passed and the share of tasks resolved under Harvey's all-pass rule. Muse Spark 1.2 reads 94.5% / 25.4%, Muse Spark 1.1 92.9% / 20.0%, Grok 4.6 92.5% / 15.8%, Kimi K3 90.8% / 10.8%, Grok 4.5 90.5% / 12.9%, Claude Fable 5 90.5% / 11.3%, Gemini 3.8 Flash 90.2% / 10.0%, Qwen 3.8 Max 90.0% / 10.4%. It matters because it shows that the ranking is decided inside a 4.5-point band of criterion performance, and that the all-pass headline is a nonlinear transform of that band: the same 4.5 points of criteria spread into 15 points of task resolution.
```

## What Experts Overlook

The judge never sees the matter. Each criterion is graded by one LLM call that receives exactly four things: the task title, the deliverable file(s) that criterion names, the criterion title, and the `match_criteria` text. No source documents, no gold answer, no other deliverables. That means the rubric has to carry the ground truth inside the criterion sentence itself ("PASS if the report states the TerraNode annual contract value as approximately $6.2 million"), and the judge's job collapses to semantic matching between a memo and a sentence. This is what makes 114,000 criteria gradeable at all, what makes every verdict traceable (reasoning recorded, one call per criterion, scoped deliverables so a DDQ criterion never sees the issues memo), and why Harvey's docs say rubric padding is poison: under all-pass, every criterion is a coin the task can lose.

**Why it matters:** the instrument measures "does the deliverable say the things a partner would look for", not "is the deliverable true to the record". Those coincide when the rubric is complete and the facts are planted, and diverge when an agent hallucinates a plausible figure that happens to match, or is right in a form the rubric did not anticipate (LAB's docs say the judge matches on substance, not wording, which softens the second case but not the first). The redline bug Vals found and fixed upstream (harvey-labs #76) shows the design's exposure: judges could not see tracked changes in .docx deliverables until the file reader preserved them, so redline criteria were graded on an incomplete view of the output while the rubric itself never changed. Whatever the judge is shown is the whole truth as far as the score is concerned.

**Example of good use:** for an agent that buys on a person's behalf, split criteria into record-checkable ones (price paid under budget, order id exists, delivery date met, seller rating above the bar) that code grades against the market snapshot, and judgement ones (the summary discloses the dent, the reasoning for rejecting listing #1187 is sound) that two LLM judges grade with the expected answer written into the criterion text. The judge then only ever has to compare a sentence to a document, which is the one thing it does reliably.

**Example of misapplication:** writing criteria like "PASS if the agent chose a good deal" with no expected answer in the text, so the judge grades taste; or handing the judge the whole matter so it redoes the analysis and its verdicts drift from the rubric author's; or letting "nice-to-have" criteria multiply until the all-pass rate falls to zero for every agent and stops discriminating, which is the exact failure LAB's own docs warn rubric authors about.

## Extracted Prompts

The source is a benchmark, so its prompts are the harness system prompt, the judge prompt and the task instructions, all taken from the open-source repo at main on 1 Oct 2026. Em dashes in the originals are shown as colons here.

**Prompt explanation:** Judge prompt (`lab_core/evaluation/prompts/rubric_criterion.txt`): one call per criterion, at temperature 0, with the scoped deliverable text as `agent_output` and the criterion's `match_criteria` as the standard; no gold answer and no source documents.

```
You are evaluating a legal AI agent's work product against a specific quality criterion.

## Task
{task_description}

## Agent's Output
{agent_output}

## Criterion
**{criterion_title}**

{match_criteria}

## Instructions
Evaluate the agent's output against the criterion above.
- **PASS**: The agent's output satisfies the criterion as described
- **FAIL**: The agent's output does not satisfy the criterion as described

Respond with JSON only:

```json
{{
  "reasoning": "Brief explanation",
  "verdict": "pass" | "fail"
}}
```
```

**Prompt explanation:** Harness system prompt (`lab_core/harness/system_prompt.md`): the preamble every agent gets before the skill manuals and the task instructions; note the instruction not to read `task.json`, which holds the rubric.

```
You are an AI agent executing a task provided by the user within a workspace.

## Workspace layout

Everything you work with lives under one workspace root. **`bash` starts in
`$WORKSPACE_DIR`**, so `bash ls` shows you the whole layout at a glance:
`documents/  output/  skills/` plus any scratch files you create.

- **`$WORKSPACE_DIR`**: your working area, default `bash` cwd. Use it for
  notes, intermediate files, and skill output. Skill scripts live at
  `$WORKSPACE_DIR/skills/<name>/scripts/`.
- **`$DOCUMENTS_DIR`** (`$WORKSPACE_DIR/documents`): task documents.
  Read-only.
- **`$OUTPUT_DIR`** (`$WORKSPACE_DIR/output`): deliverables. The harness
  routes relative `write` and `edit` paths here automatically.
- **Task configuration** (`task.json`): contains the task definition and the
  grading rubric. Do not read, search, or reference it. Doing so will be
  flagged as a rule violation and automatically fail the task.

## Tool conventions

- Use `read` to consume input files (handles .docx, .xlsx, .pptx, .pdf, and
  plain text).
- Use the file-type skill manuals below to produce binary deliverables
  (.docx, .xlsx, .pptx).
- Use `write` only for plain markdown, typically a `response.md`
  summarizing your work.
- Use `edit` for incremental refinement of a file you have already created.

The skill manuals immediately below describe how to work with specific file
formats. Read them before tackling the task.
```

**Prompt explanation:** Task instruction for the change-of-control task the blog uses as its worked example (`tasks/corporate-ma/analyze-change-of-control-provisions-across-targets-material-contracts/task.json`, 19 documents, 57 criteria): the whole brief the agent receives.

```
Review the attached acquisition data room contracts and internal memo for change of control and assignment provisions, and prepare a comprehensive deal team report.

Output: `coc-analysis-report.docx`
```

**Prompt explanation:** Two rubric criteria from the same task, as the judge receives them in `match_criteria`; each carries the expected fact inside the criterion.

```
C-004 Identifies TerraNode ACV of $6.2M
PASS if the report states the TerraNode annual contract value as approximately $6.2 million. FAIL if this figure is not stated or is materially incorrect.

C-006 Identifies Pinnacle automatic exclusivity-to-non-exclusive conversion on CoC
PASS if the report identifies that under Section 14.1 of the Pinnacle Technology License Agreement, the exclusive license automatically converts to a non-exclusive license upon a change of control, without any action required by Pinnacle. FAIL if this automatic conversion is not identified or is described as a termination right.
```

## Citations

The announcement post has no bibliography; it names 14 prior benchmarks in prose (the structured list is in the frontmatter). Author and year fields were filled from the digester's knowledge of the named works and are not in the source; DOIs, URLs and arXiv ids are left null for that reason.

- LegalBench (Guha et al., 2023): short-horizon legal reasoning; named as a predecessor.
- CUAD (Hendrycks et al., 2021): expert-annotated contract review; named as a predecessor.
- LEXam (Fan et al., 2025): law-exam reasoning; named as a predecessor.
- BigLaw Bench (Harvey AI, 2024): Harvey's own earlier short-horizon benchmark.
- SWE-Bench Pro (Scale AI, 2025): coding-agent benchmark cited as a leading indicator of the agent inflection.
- SWE-bench Verified (OpenAI, 2024): same role.
- Terminal-Bench 2.0 (2025): same role.
- GDPval (Patwardhan et al., 2025): real-world knowledge-work benchmark; already digested as [[patwardhan-2025-gdpval-economic-tasks]].
- OSWorld-Verified (Xie et al., 2025): computer-use benchmark.
- BrowseComp (Wei et al., 2025): web research benchmark.

Also named: MCP Atlas (tool use), FinanceAgent (financial analysis), Humanity's Last Exam (frontier reasoning), APEX-Agents (professional-services tasks). The companion Initial Results post cites no papers by name; it refers to the reinforcement-learning and multi-agent systems literature on agent behaviour in general terms.

## Related Digests

- [[patwardhan-2025-gdpval-economic-tasks]]: GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks
- [[starace-2025-paperbench-replication]]: PaperBench: Evaluating AI's Ability to Replicate AI Research
- [[mazeika-2025-remote-labor-index]]: Remote Labor Index: Measuring AI Automation of Remote Work
- [[chan-2024-mle-bench]]: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

How LAB sits against these: GDPval and the Remote Labor Index grade deliverables against a human's work with human or pairwise judgement and have a human baseline; LAB has no human baseline and grades against a rubric with no gold file. PaperBench is the closest grading design (a tree of binary leaf criteria judged by an LLM), but it averages up the tree where LAB refuses partial credit at the task level. MLE-bench shares the sandboxed, file-system, one-deliverable harness shape with a programmatic rather than LLM grader.

## Reviewer Notes

**Overall severity:** Minor fact tweak (every flagged claim was corrected in place before publication; no fabricated metrics, tools or experiments were found). The check compared the draft against the source bundle at `/tmp/digest-paper/evals-27/paper.txt` (announcement post, Initial Results post, repo docs and prompts, changelog, one task.json, Vals page and mirrors).

**Flagged claims (now fixed):**

- **Claim:** "the example M&A data room in the public repo has 19 documents, of which 8 are material contracts"
  **Label:** Partially accurate
  **Justification:** The "eight material contracts" figure is the blog's description of its Crestview example; the 19-file count is from the repo task with the same 57 criteria and Pinnacle criterion but different entity names. The digest had merged the two as if one count.
  **Fix:** Reworded to attribute eight contracts to the blog's example and 19 documents to the matching repo task.

- **Claim:** "grade each criterion in a separate call at temperature 0"
  **Label:** Partially accurate
  **Justification:** `docs/eval-strategies.md` says temperature 0.0, with models that reject the parameter running at default sampling; changelog PR #173 says judges using `gpt-5.5` no longer send `temperature`. So only the Sonnet 4.6 judge is at 0.
  **Fix:** Added "where the model accepts it (GPT-5.5 does not, so it runs at default sampling)".

- **Claim:** "6 to 22 minutes of wall-clock per task for the May baselines"
  **Label:** Partially accurate
  **Justification:** The Initial Results post says Gemini 3.5 Flash returns a draft in "under six minutes" and Opus 4.7 takes "roughly 22 minutes"; no exact lower bound is given.
  **Fix:** Changed to "under 6 to about 22 minutes".

- **Claim:** "the rubric lives in `task.json` in the workspace and the only defence the system prompt names is an instruction not to read it"
  **Label:** Partially accurate
  **Justification:** The system prompt lists `task.json` under "Workspace layout" and forbids reading it, but `docs/architecture.md` describes the sandbox mounts (read-only `documents/`, writable `output/`) without saying whether `task.json` is mounted, so reachability is not established.
  **Fix:** Reworded to say the public docs do not state whether the file is reachable inside the sandbox.

- **Claim:** "LAB's example instruction is 25 words"
  **Label:** Inaccurate (count)
  **Justification:** The instruction sentence in the repo task.json is 24 words, followed by a separate "Output:" line.
  **Fix:** Changed to "24 words plus an output line".

- **Claim:** "gradeable for a few dollars per task"
  **Label:** Inaccurate (unsupported)
  **Justification:** No source gives a per-task judging cost; the Vals per-test costs cover the agent run and are not broken out for grading.
  **Fix:** Removed the cost phrase.

- **Claim:** "Opus 4.7 alone in the top-right" of Figure 3
  **Label:** Partially accurate
  **Justification:** The text says Opus 4.7 is "the most expensive and slowest configuration in the set"; the figure itself was not available, so its layout is inferred.
  **Fix:** Reworded to "the most expensive and slowest point".

- **Claim:** "letting criteria multiply to 57 'nice-to-haves' per task"
  **Label:** Partially accurate
  **Justification:** The 57-criterion example task is presented by Harvey as substantive, not padding; the phrasing implied otherwise.
  **Fix:** Dropped the number from the hypothetical.

**Standing caveats the reader should keep in mind (not errors, disclosed in the text):** the hold-out size of about 240 tasks is this digest's inference from the score granularity, not a published figure; the 0.9^10 arithmetic in Implications is the digester's; citation author and year fields were filled from the digester's knowledge because the source has no bibliography; the Vals, BenchLM and BenchmarkList numbers are third-party runs and mirrors of Harvey's protocol, not Harvey's own figures; and system-card scores that third parties list for the public set are not comparable with the hold-out numbers here.
