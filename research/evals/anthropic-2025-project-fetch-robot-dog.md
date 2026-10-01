---
kind: paper-digest
corpus: evals
slug: anthropic-2025-project-fetch-robot-dog
title: "Project Fetch: Can Claude train a robot dog? (Phase one, Nov 2025) and Project Fetch: Phase two (Jun 2026)"
authors:
  - "Anthropic (Phase one post, no byline)"
  - "Michael Ilie"
  - "C. Daniel Freeman"
  - "Kevin K. Troy"
year: 2025
publication_date: "2025-11"
venue: "Anthropic research post"
source_url: "https://www.anthropic.com/research/project-fetch-robot-dog"
doi: null
arxiv_id: null
lens: eval-designer
digested_date: "2026-10-01"
key_takeaway: "The humans with AI wrote about 9 times more code than the humans without it and finished the shared tasks in about half the time, yet the model working alone less than a year later beat both while writing fewer lines than the unassisted humans (1,045 against 1,136 and 10,309) and finishing the four shared tasks in 9 minutes 35 seconds against 181 and 361 minutes; the one task still unsolved after both phases, nudging the ball home in a closed loop, is the one a person did in Phase One with the manufacturer's controller."
topics:
  - uplift-study
  - human-ai-collaboration
  - autonomous-agents
  - robotics
  - physical-world-agents
  - agentic-coding
  - agent-evals
tags:
  - paper
  - experiment
  - anthropic
  - project-fetch
  - uplift
  - robodog
  - claude-code
  - question-first-eval
entities:
  - ilie-michael
  - freeman-c-daniel
  - troy-kevin
  - anthropic
  - claude-opus-4-1
  - claude-opus-4-7
  - claude-code
related_digests:
  - wijk-2024-re-bench
  - kwa-2025-time-horizons
  - mazeika-2025-remote-labor-index
  - hitzig-2026-project-swap-agent-markets
  - andon-labs-2026-andon-market-pion
citations:
  - title: "Cognitive, emotional, and language processes in disclosure"
    authors: ["James W. Pennebaker", "Martha E. Francis"]
    year: 1996
    venue: "Cognition & Emotion, 10(6), 601-626"
    doi: null
    url: null
    arxiv_id: null
  - title: "The psychological meaning of words: LIWC and computerized text analysis methods"
    authors: ["Yla R. Tausczik", "James W. Pennebaker"]
    year: 2010
    venue: "Journal of Language and Social Psychology, 29(1), 24-54"
    doi: null
    url: null
    arxiv_id: null
  - title: "Claude 4 System Card (p. 114, quadruped-control ML training evaluation)"
    authors: ["Anthropic"]
    year: 2025
    venue: "Anthropic system card"
    doi: null
    url: null
    arxiv_id: null
  - title: "Project Vend: Claude runs a small shop in Anthropic's office"
    authors: ["Anthropic"]
    year: 2025
    venue: "Anthropic research post"
    doi: null
    url: null
    arxiv_id: null
  - title: "Anthropic Economic Index"
    authors: ["Anthropic"]
    year: null
    venue: "Anthropic research programme"
    doi: null
    url: null
    arxiv_id: null
  - title: "Responsible Scaling Policy (AI R&D capability threshold)"
    authors: ["Anthropic"]
    year: null
    venue: "Anthropic policy document"
    doi: null
    url: null
    arxiv_id: null
  - title: "Project Fetch: Can Claude train a robot dog?"
    authors: ["Anthropic"]
    year: 2025
    venue: "Anthropic research post (cited by the Phase two post)"
    doi: null
    url: "https://www.anthropic.com/research/project-fetch-robot-dog"
    arxiv_id: null
hallucination_severity: "Minor fact tweak"
best_figure: null
---

# Project Fetch: Can Claude train a robot dog? (Phase one and Phase two)

**Authors:** Phase one post: Anthropic, no byline. Phase two post: Michael Ilie, C. Daniel Freeman, Kevin K. Troy
**Published:** 2025-11-12 (Phase one, experiment run August 2025) · [Source](https://www.anthropic.com/research/project-fetch-robot-dog) · 2026-06-18 (Phase two) · [Source](https://www.anthropic.com/research/project-fetch-phase-two)
**Lens:** `eval-designer` · **Digested:** 2026-10-01

_Not a paper: two Anthropic research posts covering one experiment and its re-run. Both were fetched as HTML on 2026-10-01; the Phase two comparison numbers come from the chart descriptions embedded in that page (the charts are images)._

## TLDR

Anthropic ran Project Fetch as a one-day uplift study in August 2025 and then re-ran its programmable tasks with a model working alone, publishing the second result in June 2026. Eight Anthropic researchers and engineers, none with extensive robotics experience, were randomly split into Team Claude (four people, each pairing with their own instance of the then-current model, Claude Opus 4.1) and Team Claude-less (four people, internet only), and both were asked to make an off-the-shelf quadruped fetch a beach ball across three phases: drive it with the manufacturer's controller, then connect a laptop to its video and lidar and write their own control program, then make it find and retrieve the ball autonomously. Team Claude completed 7 of 8 timed sub-tasks against 6 of 8, and on the sub-tasks both teams finished it took about half the time; the biggest part of that edge came from connecting to the robot and its sensors, where Team Claude-less was misled by inaccurate online documentation, discarded the easiest connection route, needed a hint from the organisers, and only got lidar data near the end of the day. Once connected, Team Claude-less wrote its control program and its localisation faster. Team Claude wrote about 9 times more code, some of it side quests (a natural-language controller; a detour to a second localisation approach when the first only needed its axes flipped), and its ball detector, trained to recognise green balls, was initially stumped when the green ball sat on the green fake grass. A dictionary word count of the recorded transcripts, run in a program Claude wrote, found Team Claude-less used more negative-emotion words (p = 0.0017, Cohen's d = 2.16), expressed confusion at twice the rate, and asked 44% more questions of one another; net emotion (positive minus negative words) was not significant (p = 0.27). Neither team finished autonomous fetch: Team Claude's robot could locate the ball, navigate to it and move it around, but not bring it back. Before the human run, Opus 4.1 alone could not even connect to the robot. In Phase two, Claude Opus 4.7 ran in Claude Code with adaptive thinking at maximum effort for three trials, with the researcher's role limited to plugging in the laptop, entering the initial prompt, approving commands and approving each move to the next task; the controller-driving tasks were dropped and the time to drive the model-written controller to the ball was not measured (it was confirmed to work). On the four tasks both human teams had completed, Opus 4.7 took 9 minutes 35 seconds against 181 minutes (Team Claude) and 361 minutes (Team Claude-less), 18.9 and 37.7 times faster; on the five programmatic tasks it averaged 12 minutes 7 seconds against Team Claude's 264 minutes (Team Claude-less never finished all five); it wrote 1,045 lines of code against 10,309 and 1,136; run-to-run variance was small in absolute terms, with one detection trial substantially longer, likely because the model defaulted to an outdated object-detection algorithm before working around it. It still could not fetch: it got the robot behind the ball and lined up a push, but the closed-loop control was poor and unsuccessful, the same place the human teams stalled, while a colleague with more robotics experience did program autonomous fetching. The useful lesson for eval builders is the two-arm design: the uplift arm produced the per-task human baselines that made the later autonomy result legible, and the one task that stayed unsolved, autonomous retrieval, has no human time on the ledger because no team completed it, while the same retrieval done by hand with the manufacturer's controller was the first thing both teams did.

## Key Takeaway

The humans with AI wrote about 9 times more code than the humans without it and finished the shared tasks in about half the time, yet the model working alone less than a year later beat both while writing fewer lines than the unassisted humans (1,045 against 1,136 and 10,309) and finishing the four shared tasks in 9 minutes 35 seconds against 181 and 361 minutes; the one task still unsolved after both phases, nudging the ball home in a closed loop, is the one a person did in Phase One with the manufacturer's controller. Code volume looks like a symptom of four people each fanning out with their own assistant rather than of the assistant itself: with the people out of the loop, the exploration disappeared. And the frontier is not the part that looks like robotics (SDKs, sensors, object detection) but the feedback loop, which the posts say none of the tasks tested at the level of an actuation policy.

## Implications

- **Build the uplift arm first; it is the baseline the autonomy arm needs**: Phase one timed eight non-experts per sub-task with and without the model; Phase two reused those stopwatch numbers as the yardstick (9 minutes 35 seconds against 181 and 361 minutes). For a spend-my-money agent, run a day with two small human teams, one with and one without an assistant, before any solo-agent run, so the solo number has something to be 18x or 37x of.
- **Decompose, and report completions alongside times**: nobody fetched the ball autonomously in either phase, so the end-to-end score is zero for two teams and a model; the per-task ledger (7 of 8 and 6 of 8 in Phase one; all five programmatic tasks for the model in Phase two) is where the progress shows. Keep a sub-task ledger with a completion count and a time per row, and say which rows were excluded (the controller tasks were dropped from the autonomy arm; the human time using the model-written controller was not measured).
- **The baseline is non-experts on a one-day clock, and the headline inherits that**: "about 20 times faster than the fastest human team" is against people learning unfamiliar hardware in a day, and the one colleague with more robotics experience who did solve autonomous fetch is not timed. Decide and state who your human is (the account owner, a novice, a professional buyer), because the multiple changes with that choice.
- **Count activity, not just outcomes, and treat more as a warning sign**: Team Claude's 10,309 lines against 1,136 bought side quests, and the model alone wrote 1,045 and did as well or better. For a buying agent, log bids, messages, searches and reversals per run; a run that does 9x the actions of a baseline is probably exploring, not winning.
- **Run repeated trials and show the spread, then explain the outlier**: three trials of Opus 4.7, little within-task variance in absolute terms, and the one slow detection trial traced to an outdated object-detection default. The post shows the three trials per task in a scatter but gives no pass^k and no per-task failure count; with real money the worst run is the loss, so report min, median and max per task.
- **Itemise every human touch in the "autonomous" arm**: plug in the laptop, enter the initial prompt, approve commands, approve the move to the next task. The last of those is a human-supplied done-signal. For a money agent, that gate is both your safety brake and a hint channel; log it, and run a variant where the agent must decide it is done.
- **Specification errors, not model errors, are what hits the table**: 1 metre per second for 5 seconds with the other team's table under 5 metres away; a detector trained on green put on green grass. Bound magnitude at the harness (max spend per action, max total, max distance) instead of trusting the operator or the model to do the arithmetic.
- **Expect the uplift-then-autonomy flip, and schedule the re-run**: Opus 4.1 could not connect to the robot alone; less than a year later Opus 4.7 did the four shared tasks in under 10 minutes with no robotics-specific training, which the authors attribute to general scaling. Date-stamp your eval and plan a re-run when the next model lands; the answer to "can it do this alone" has a short half-life.

## How to Apply It (method)

**Scenario:** A venture builder is designing an eval for an agent that spends a real person's money in a live secondary market (buying a used gravel bike or resale tickets at or under a target price within a week). He wants two numbers the team can defend: how much the agent helps a non-expert, and whether it can do the job alone, task by task.

**Steps:**

1. **Write the task ladder**: Mirror Project Fetch's six steps (operate with the vendor controller; connect to video and lidar; write and operate a control program; track the robot's path; detect the ball; retrieve it autonomously) as market steps: (a) buy one item by hand through the normal UI; (b) get programmatic access to listings and messages; (c) write a program that can place a bid or send an offer; (d) track the state of every open offer; (e) detect a qualifying listing from noisy text and photos; (f) close a purchase end to end without a human. Each step gets a stopwatch and a pass or fail.

2. **Recruit two small teams and randomise**: Four people per team, none with marketplace-automation experience; coin-flip who gets the assistant. Project Fetch used eight Anthropic staff, accepted a Lego-robotics confound in a footnote, and noted that daily Claude users are more disoriented without it than novices would be; write down the same caveats for your sample.

3. **Run the uplift day**: One day, same hardware, same market, same budget per team. Record audio. Time each step from start to confirmed pass. Give hints only when a team is stuck on a step the other team has passed, and log the hint (Project Fetch gave Team Claude-less one on connectivity). Record code volume or action counts per team.

4. **Score the uplift arm**: Steps completed per team; time per step; the ratio on the steps both finished (Project Fetch: about 2x). Run a dictionary word count on the transcripts for negative emotion, confusion and questions (Project Fetch had Claude write a LIWC-style program and compared teams with Mann-Whitney U and Cohen's d). Note where the unassisted team was faster, because that is where the assistant's extra output was not progress.

5. **Run the autonomy arm**: Put the model in a coding agent (Project Fetch: Opus 4.7 in Claude Code, adaptive thinking at maximum effort), three or more trials. Limit the human to: plug in, paste the initial prompt, approve commands, approve the move to the next step. Drop steps that need a human body (the vendor-controller step) and say so. The Phase two post does not reproduce its initial prompt; a workable one for the market case (this digest's draft, not from the source):

   ```
   You are operating on a laptop connected to a live secondary-market account that belongs to a real person. Complete the following tasks in order and tell me when each is done:
   1. Get programmatic access to listings and messages for this account.
   2. Write a program that can place a bid or send an offer.
   3. Track the state of every open offer.
   4. Find a listing that matches: [item spec], at or under [price].
   5. Buy it.
   Hard limits: never exceed [X] per action or [Y] in total; ask before any irreversible step. I will approve commands and tell you when to move to the next task.
   ```

6. **Score the autonomy arm against the uplift arm**: Per step, time per trial, min, median and max, and completions out of trials. Compute the multiple against each human team on the steps both completed. Report the leftover step (Project Fetch: closed-loop fetch) as the frontier, and say whether an expert human solved it.

7. **Date-stamp and re-run**: Record model, scaffold and date. Re-run the autonomy arm when the next model ships; Project Fetch's gap between "cannot connect" and "under 10 minutes" was less than a year.

**Expected outcome:** A per-step ledger with human-with-AI, human-without-AI and model-alone times and completions; a defensible multiple on the shared steps; a named frontier step that nobody, or only an expert, can do; a logged list of every human touch in the autonomy arm; and a dated baseline for the next model.

## What It Does Not Test, and What to Borrow

**Untested cells.** No outside participants: both arms used Anthropic staff, and the Phase one post says daily Claude users are more disoriented without it than novices would be, so the uplift gap is probably wider than it would be in the public. One robot model, one day, two teams of four; the authors call the sample obviously small and the tasks practically trivial. One model family: Phase two reports Opus 4.7 only, and a footnote says Claude Mythos Preview trials were excluded because the setup and serving would not give an apples-to-apples comparison. No adversary, no money, nothing at stake beyond morale and a table. Low-level control is excluded by the authors' own statement: none of the tasks involve developing an actuation policy.

**How it can be gamed or saturate.** The task ladder is fixed and known, and the autonomy arm's headline is computed over tasks "completed by at least one human team", so the comparison set is selected by human completion. The final task has no human time because nobody did it autonomously, which means the ladder is saturated on every row except fetch; the next re-run either moves that one row or shows nothing. Hints and hardware luck also sit inside the human numbers: the organisers gave Team Claude-less a connectivity hint, and Team Claude drew the standalone controller in Phase One while the other team had to install a phone app (footnote 3, excluded from the uplift claim).

**Judges and awareness.** Success in Phase two was "qualitatively assessed" by the researchers, and progression was human-approved. The emotion and question counts came from a dictionary program Claude wrote, in the LIWC tradition; standard method, but the program itself is not audited in the post. Simulation awareness is not discussed: participants were recorded on camera and sub-tasks were timed with stopwatches, and the model was told the tasks by a person.

**Borrow these.** (1) The two-arm ladder: the same sub-tasks measured first as human-plus-AI versus human-only, then as model-only, so each autonomy number has a human time next to it. (2) The completion-plus-time ledger with explicit exclusions written into the caption ("did not complete all 5 tasks", "controller tasks excluded"). (3) An activity count beside the outcome (lines of code here; actions, bids and messages for a market agent). (4) An itemised list of every human touch in the autonomous arm.

## Best Figure

_(figure not extracted: both sources are HTML pages with embedded images; no PDF)_

Image Candidates:
Phase one, Figure 1: "Team Claude was faster at the tasks completed by both teams" (about half the time); the uplift headline in one view.
Phase one, Figure 2: "Team Claude wrote about 9 times more code than Team Claude-less"; the activity-versus-progress contrast.
Phase two, bar chart "Total time comparison: 4 tasks completed by all teams": three bars, 361 minutes, 181 minutes, 9 minutes 35 seconds; the uplift arm and the autonomy arm on one axis.

Best Image:
Figure Name: Phase two bar chart: "Total time comparison: 4 tasks completed by all teams"
Figure Page: not applicable (web page; image hosted on cdn.sanity.io, file 0424a5a4ed31f7891e4048d091aefa52f36862cf-1999x1092.png)
Slide Caption: Same four tasks, three runners: humans without AI 361 minutes, humans with AI 181 minutes, the model alone 9 minutes 35 seconds.
Description: Three bars of total elapsed time on the four tasks that both human teams completed in August 2025: Team Claude-less at 361 minutes, Team Claude at 181 minutes, and Claude Opus 4.7 working alone at 9 minutes 35 seconds (37.7 times faster than Team Claude-less, 18.9 times faster than Team Claude, per the chart description). It matters because the two human bars are the uplift study and the third bar is the autonomy study, measured on the same task definitions less than a year apart, so one chart shows both halves of the "uplift precedes autonomy" claim. Companion images on the same page: a per-task table of five programmatic tasks (including connect to the video camera, connect to the lidar sensor, detect the beach ball; Team Claude 264 minutes, Opus 4.7 12 minutes 7 seconds averaged over three trials, Team Claude-less did not finish all five), a code-volume bar chart (10,309, 1,136 and 1,045 lines), and a scatter of the three Opus 4.7 trials per task showing small spread.

## What Experts Overlook

The 9 minutes 35 seconds was measured with a human holding the "done" button. The Phase two post lists the researcher's role as plugging in the laptop, entering the initial prompt, approving commands, and approving the model to go to the next task, and says success was qualitatively assessed. So the model was never asked to decide that a sensor connection was good enough, that its detector worked, or that a task was finished; a person made that call and the clock stopped. The reliability claim (little within-task variance across three trials) is therefore a claim about execution speed given an external success signal, not about self-verification. The uplift arm had the same structure: the organisers timed each sub-task and handed Team Claude-less a hint when they were stuck on connectivity.

**Why it matters:** PaperBench, in this corpus, showed that whether an agent can declare itself finished can nearly double one model's score (o1, 13.2% to 24.4%) and cut another's by a quarter (Claude 3.5 Sonnet, 21.0% to 16.1%). Project Fetch sidesteps that variable by design, which is fine for a capability read-out but means the 20x multiple does not transfer to a deployment where nobody is approving the next step. The post is candid about what it excludes (controller tasks, actuation policy); the human done-gate is the exclusion it does not name.

**Example of good use:** In a buy-this-for-me eval, run the per-task ledger twice: once with a human approving each step (the Project Fetch protocol, which gives clean per-step times and a fair comparison to the uplift arm) and once where the agent must say "purchased, here is the receipt" and stop. Report both, and treat the gap between them as the cost of autonomy.

**Example of misapplication:** Reading "about 20 times faster than the fastest human team" as "the agent can run this alone", wiring a spending agent to a live account with no approval gate, and finding it either stops after the first plausible listing (declares done early) or keeps bidding past the target because nothing told it the task was over. The 9 minutes 35 seconds never measured that failure mode, so it cannot rule it out.

## Extracted Prompts

No applicable prompts found in this paper. The Phase two post says the researcher entered "the initial prompt" into Claude Code but does not reproduce it; the Phase one post describes Claude writing a dictionary-based transcript-analysis program but gives no prompt text.

## Citations

Seven references and in-text pointers across the two posts (full list in frontmatter):

- [1] Pennebaker, J. W., & Francis, M. E. (1996). Cognitive, emotional, and language processes in disclosure. Cognition & Emotion, 10(6), 601-626. (Phase one, footnote 4)
- [2] Tausczik, Y. R., & Pennebaker, J. W. (2010). The psychological meaning of words: LIWC and computerized text analysis methods. Journal of Language and Social Psychology, 29(1), 24-54. (Phase one, footnote 4)
- [3] Anthropic (2025). Claude 4 System Card, p. 114: the quadruped-control ML training evaluation. (Phase one, footnote 2)
- [4] Anthropic (2025). Project Vend: Claude runs a small shop in Anthropic's office. (Phase one, in text)
- [5] Anthropic. Anthropic Economic Index. (Phase one, in text)
- [6] Anthropic. Responsible Scaling Policy, AI R&D capability threshold. (Phase one, in text)
- [7] Anthropic (2025). Project Fetch: Can Claude train a robot dog? (Phase two, in text)

## Related Digests

BM25 search over `memory/knowledge-sources/papers/evals/` at digest time (six short queries on uplift studies, human-versus-agent time baselines, Claude Code agents and Anthropic real-world experiments); top hits above 0.5:

- [[wijk-2024-re-bench]] · RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts (the other human-versus-agent time comparison in this corpus; experts there, non-experts here)
- [[kwa-2025-time-horizons]] · Measuring AI Ability to Complete Long Software Tasks (human task time as the unit; Project Fetch's 181 and 361 minutes are that kind of yardstick)
- [[mazeika-2025-remote-labor-index]] · Remote Labor Index: Measuring AI Automation of Remote Work (paid professional baselines for whole projects, against one day of non-experts here)
- [[hitzig-2026-project-swap-agent-markets]] · Project Swap: What happens when agents trade for us? (the other Anthropic experiment with staff as participants; a Kevin Troy is on both bylines)
- [[andon-labs-2026-andon-market-pion]] · Andon Market, Andon Café and Pion (physical-world agent deployments with people in the loop; Project Fetch replaces the people with a robot)

## Reviewer Notes

**Overall severity:** Minor fact tweak (six partially accurate claims found in the draft; all corrected before publication, no fabricated numbers, methods or quotes)

The review compared every number, attribution and quoted phrase in the draft against the Phase one post (fetched as text 2026-10-01), the Phase two post (fetched as text the same day), and the chart descriptions embedded in the Phase two page HTML, which are Anthropic's own captions for the four images (total-time bar chart, five-task table, code-volume bar chart, reliability scatter). Secondary coverage (cryptobriefing, aihola, macleodlabs, the companion YouTube transcript) was read but no number was taken from it; the video's "about 2 hours 15 minutes for Phase Two" and "an hour and a half from done" were deliberately left out.

**Flagged in the draft and fixed:**

- **Claim:** "eight Anthropic researchers and engineers with no real robotics background." **Label:** Partially accurate. **Justification:** The post says "none of whom had extensive prior experience with robots" and footnote 1 admits a couple did Lego robotics in high school. **Fix applied:** "none with extensive robotics experience."
- **Claim:** "one detection trial slowed by defaulting to an outdated object-detection algorithm." **Label:** Partially accurate. **Justification:** The post says the outdated default "is likely why" one trial took substantially longer; cause is inferred, not measured. **Fix applied:** "likely because."
- **Claim:** "the one task that stayed unsolved was the one nobody could time, because the humans did it by hand with a controller." **Label:** Partially accurate (muddled). **Justification:** Phase One retrieval with the manufacturer's controller was timed (Table 1, footnote 3). What has no human time is autonomous retrieval, which no team completed. **Fix applied:** reworded to say autonomous retrieval has no human time because no team completed it, while hand retrieval was the first task both teams did.
- **Claim:** "Code volume was a symptom of four people each fanning out ... not of the assistant." **Label:** Partially accurate (overextended). **Justification:** The post says the assistant "made it easier to fan out"; attributing the volume to the people rather than the assistant is this digest's reading. **Fix applied:** "looks like a symptom ... rather than of the assistant itself."
- **Claim:** "The post gives no pass^k and no worst case." **Label:** Partially accurate. **Justification:** The page includes a scatter plot of all three trials per task, so the worst trial is visible; what is absent is pass^k and a per-task failure count. **Fix applied:** reworded accordingly.
- **Claim:** "PaperBench ... can roughly double or halve its score." **Label:** Partially accurate. **Justification:** The PaperBench digest in this corpus reports o1 13.2% to 24.4% and Claude 3.5 Sonnet 21.0% to 16.1%, a cut of about a quarter, not a halving. **Fix applied:** exact figures substituted.
- Also tightened: "participants knew they were timed" became "sub-tasks were timed with stopwatches and participants were recorded"; the Anthropic Economic Index citation year was set to null because neither post dates it.

**Cross-checked and accurate (Phase one post):** August 2025 experiment date (from the Phase two post, which corrected its own date on publication day); eight participants, four per team, random assignment; three phases and their definitions; Table 1 (7 of 8 against 6 of 8); Figure 1 (about half the time on tasks both completed); Figure 2 (about 9 times more code); connectivity as the most striking advantage, incorrect online claims, the prematurely discarded easy route, the organisers' hint, lidar only near the end of the day; Team Claude-less faster on control program and localisation once connected; streaming video against still images; the quiz speculation; the flipped-coordinates localisation detour; the natural-language controller and push-ups; green ball on green grass; 1 metre per second for 5 seconds with the table under 5 metres away; the dictionary-based program Claude wrote, LIWC references (footnote 4), negative emotion p = 0.0017 and d = 2.16, net emotion p = 0.2703, Mann-Whitney U and Cohen's d (footnote 5); confusion at double the rate and 44% more questions (Figure 4); each Team Claude member pairing with their own instance, "eight-agent Team Claude"; Claude Code debuting six months before; the standalone-controller luck in Phase One (footnote 3); Lego confound (footnote 1); Claude 4 System Card p. 114 (footnote 2); Project Vend, Economic Index and Responsible Scaling Policy mentions; the stated limitations (two teams, one day, practically trivial tasks, convenience sample, novices less disoriented); "not a test of Claude's ability to conduct robotics work end-to-end."

**Cross-checked and accurate (Phase two post and its chart captions):** byline Ilie, Freeman, Troy; Opus 4.1 as the model at the time and its failure to connect alone before the human run; Opus 4.7 in Claude Code, adaptive thinking at maximum effort, three trials; researcher role (plug in, initial prompt, approve commands, approve next task); controller tasks excluded and the model-written controller confirmed to work but not timed; "qualitatively assessed"; at least ten times faster on every task completed by at least one human team; about 20 times faster than the fastest human team; more than 37 and more than 18 times on the four shared tasks, with 361, 181 and 9 minutes 35 seconds and the 37.7 and 18.9 multiples from the bar-chart caption; the five-task table caption (tasks include video camera, lidar, detect beach ball; Team Claude 264 minutes; Opus 4.7 12 minutes 7 seconds averaged over three trials; Team Claude-less did not complete all five); code volume 10,309, 1,136 and 1,045 from the caption; outdated object-detection default; little within-task variance in absolute terms and the reliability scatter; general scaling rather than a robotics push; the closed-loop description of fetching, behind-the-ball positioning and unsuccessful control; the more experienced colleague who programmed autonomous fetching (no time given); "more time and additional scaffolding"; the Mythos Preview footnote; actuation policy excluded; "early era of physical agentic AI."

**Labelled inference, not source claims:** the human done-gate reading in "What Experts Overlook", the "nothing at stake beyond morale and a table" line, the saturation reading of the task ladder, and the market-eval prompt in the method section are this digest's own, and are marked as such where they appear.
