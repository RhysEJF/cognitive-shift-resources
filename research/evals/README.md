# Evals: fifty real-world evals and what they set out to answer

A research corpus on **real-world AI evals**: fifty benchmarks, experiments and deployments across ten industries, each chosen because it exists to answer one question ("can an agent run a business for a year?", "when are AI agents good enough to trade on our behalf?") rather than to report a number. Two layers:

1. **The landscape list.** One row per eval: the question in the authors' framing, the design, a dated headline result, and a link. Markdown and CSV.
2. **Fifty structured digests.** One file per eval, read through a single lens and checked against the source, so you can compare instruments side by side.

Built as design input for new evals: before writing a benchmark, read fifty that already exist and notice what the good ones share. Published as part of [The Cognitive Shift](https://github.com/RhysEJF/cognitive-shift-resources)'s open research.

## Files

| File | What it is |
|---|---|
| [`question-first-evals.md`](question-first-evals.md) | The landscape list, grouped by industry, as markdown tables. Start here. |
| [`question-first-evals.csv`](question-first-evals.csv) | The same 50 rows as CSV for filtering, joining or loading into an agent. |
| [`INDEX.md`](INDEX.md) | The digest table: every eval with its one-sentence key takeaway. |
| `<first-author>-<year>-<slug>.md` | One digest per eval. |
| `figures/` | The one figure or table each digest singles out, cropped from the source. |

### List columns

`id` · `group` (industry) · `name` · `org` · `year` (first public release) · `type` (benchmark, experiment, deployment) · `question` (one sentence, the authors' framing) · `design` (environment, horizon, metric, baseline) · `status` (open source, leaderboard, closed) · `headline` (one result, snapshot dated 30 Sept 2026) · `link` (paper or eval page).

### Industries

Running a business · Economic value of work · Markets, negotiation and selling · Science and research · Health · Professions and public services · Physical world · Security and safety · Computers, infrastructure and support · Games, persuasion and media.

## How to read a digest

Every digest has the same sections: **TLDR → Key Takeaway → Implications → How to Apply It → Best Figure → What Experts Overlook → Extracted Prompts → Citations → Related Digests → Reviewer Notes**. The Reviewer Notes hold a hallucination check: every number and claim in the draft was re-read against the source and the corrections are listed there.

Digests cross-link each other with `[[wiki-links]]` in their frontmatter (`related_digests`) and in the Related Digests section, so you can walk from one instrument to its nearest neighbours.

Where an eval has no paper (Andon Market, Andon FM, Claude Plays Pokémon, Project Fetch, AI Diplomacy, Harvey's legal benchmark and a few others), the digest reads the primary write-ups and leaderboard pages instead, and says so in its source note. Leaderboard numbers carry the date they were read.

## The lens: why the digests read the way they do

Every paper was digested through one **reading lens**, `eval-designer`: a venture builder designing a new real-world eval (an agent that spends a real person's money on their behalf in a live secondary market), writing for enterprise operators and agent builders. The lens reads each eval against four questions:

1. **The question.** What the authors set out to answer, in their own words, and why they picked this instance. Capability, safety, or delegation?
2. **The instrument.** Environment, horizon, what counts as one run, number of runs, the primary metric and its ceiling, the baseline, and how spread, worst runs and pass^k are reported.
3. **The result and the surprise.** Headline numbers, the gap to the baseline, and the finding the authors did not expect. Where a script or a human beat the models.
4. **What it does not test, and what to borrow.** Untested cells, ways the eval can be gamed or saturated, reliance on LLM judges, and the two or three design moves worth copying.

The "How to Apply It" sections are written in the second person for that builder. The eval they describe is a design in progress, not a published benchmark.

## How to use with an agent

Drop the CSV into context and ask for evals that share a property ("which have a human baseline?", "which score in dollars?", "which decompose into subtasks?"). Or load the digests and ask for the nearest neighbours of an eval you are designing and what they did not test.

## Provenance

The list was compiled on 30 Sept 2026 from five parallel research passes, one per industry slice, each verifying entries against the primary source. Seventy candidates were cut to fifty; the cut list and reasons are at the end of the markdown file. Details the check could not confirm are marked "(unverified)".

The digests were produced on 1 Oct 2026 with [FlowScout](https://github.com/RhysEJF/flowscout)'s `/digest-paper` pipeline, one agent per eval, each running the eight analyses, the figure extraction and the hallucination check inline.

## License and caveats

Digests are AI-generated interpretations of the underlying papers and pages. Always check a digest's `source_url` and read the original before relying on a claim. The hallucination check catches a lot; errors survive. If you spot one, open an issue or a pull request. Keep the question in the authors' own framing and link the primary source.
