# Evals: question-first landscape

A reference list of real-world AI evals organised by the question each one was built to answer, rather than by the number it reports. Built as design input for new evals: before writing a benchmark, read fifty that already exist and notice what the good ones share.

## Files

| File | What it is |
|---|---|
| [`question-first-evals.md`](question-first-evals.md) | The list, grouped by industry, as markdown tables. Read this. |
| [`question-first-evals.csv`](question-first-evals.csv) | The same 50 rows as CSV for filtering, joining or loading into an agent. |

## Columns

`id` · `group` (industry) · `name` · `org` · `year` (first public release) · `type` (benchmark, experiment, deployment) · `question` (one sentence, the authors' framing) · `design` (environment, horizon, metric, baseline) · `status` (open source, leaderboard, closed) · `headline` (one result, snapshot dated 30 Sept 2026) · `link` (paper or eval page).

## Industries

Running a business · Economic value of work · Markets, negotiation and selling · Science and research · Health · Professions and public services · Physical world · Security and safety · Computers, infrastructure and support · Games, persuasion and media.

## How to use with an agent

Drop the CSV into context and ask for evals that share a property ("which have a human baseline?", "which score in dollars?", "which decompose into subtasks?"). Or ask for the nearest neighbours of an eval you are designing and what they did not test.

## Provenance

Compiled 30 Sept 2026 from five parallel research passes, one per industry slice, each verifying entries against the primary source. Seventy candidates cut to fifty; the cut list and reasons are at the end of the markdown file. Details the check could not confirm are marked "(unverified)".

Corrections and additions welcome by pull request. Keep the question in the authors' own framing and link the primary source.
