# Evals: fifty real-world evals and what they set out to answer

**Just want the evals?** The list of 50 is in [markdown](question-first-evals.md) and [CSV](question-first-evals.csv). The table below has every eval, its question and its digest.

A research corpus on **real-world AI evals**: fifty benchmarks, experiments and deployments across ten industries, each chosen because it exists to answer one question ("can an agent run a business for a year?", "when are AI agents good enough to trade on our behalf?") rather than to report a number. Two layers:

1. **The landscape list.** One row per eval: the question in the authors' framing, the design, a dated headline result, and a link. Markdown and CSV.
2. **Fifty structured digests.** One file per eval, read through a single lens and checked against the source, so you can compare instruments side by side.

Built as design input for new evals: before writing a benchmark, read fifty that already exist and notice what the good ones share. Published as part of [The Cognitive Shift](https://github.com/RhysEJF/cognitive-shift-resources)'s open research.

## The fifty evals

Each row is one eval, the question it was built to answer, and its digest. The [markdown](question-first-evals.md) and [CSV](question-first-evals.csv) add each eval's design, status and a dated headline result.


### Running a business

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 1 | [Vending-Bench 2 + Arena](https://andonlabs.com/evals/vending-bench-2) | Andon Labs · 2025 | Can a model stay coherent and run a business profitably over a simulated year, and (Arena) under head-to-head competition at the same location? | [Read](backlund-2025-vending-bench.md) |
| 2 | [CEO-Bench](https://arxiv.org/abs/2606.18543) | Princeton Z-Lab · 2026 | Can agents play the long game: operate a startup for 500 days under hidden state, noisy delayed feedback and a changing market? | [Read](chen-2026-ceo-bench.md) |
| 3 | [Business Arena](https://arxiv.org/abs/2608.08621) | Accio (Alibaba) + Yale · 2026 | Can an agent run a cross-border shop end to end: infer opportunities from partial signals, commit capital, adapt to delayed outcomes, satisfy compliance before trading? | [Read](pan-2026-business-arena.md) |
| 4 | [E-Commerce Bench](https://arxiv.org/abs/2608.30730) | Qwen (Alibaba) · 2026 | Can an agent run several online stores for a year: research, negotiate with suppliers, sell, fulfil, handle returns and manage cash? | [Read](fan-2026-ecommerce-bench.md) |
| 5 | [MerchantBench](https://arxiv.org/abs/2607.28956) | Alibaba 1688 × Zhejiang University · 2026 | Can an agent sustain a goal-directed merchant policy as demand shifts, supplier events arrive and delayed order outcomes accumulate over a year? | [Read](shi-2026-merchantbench-ecommerce.md) |
| 6 | [EnterpriseArena](https://arxiv.org/abs/2603.23638) | Georgia Tech, The Fin AI et al. · 2026 | Can LLM agents be CFOs, allocating scarce resources over a long horizon in an uncertain enterprise? | [Read](han-2026-enterprise-arena-cfo.md) |
| 7 | [Bazaar](https://arxiv.org/abs/2608.00102) | Visa Research · 2026 | Can LLM agents price competitively where customer preferences are hidden, competitors adapt in real time and demand shifts without warning? | [Read](ahmed-2026-bazaar-pricing.md) |
| 8 | [ERP-Bench](https://arxiv.org/abs/2605.26321) | Agentic Labs · 2026 | Can agents complete economically valuable procurement and manufacturing workflows in a production ERP, scored only on end-state business correctness against a certified-optimal plan? | [Read](ivanov-2026-erp-bench.md) |
| 9 | [Andon Market, Andon Café, Pion](https://andonlabs.com/market) | Andon Labs · 2026 | Can AI make money in the real world running an entire business with no human in the loop, and what fails when it does? | [Read](andon-labs-2026-andon-market-pion.md) |

### Economic value of work

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 10 | [GDPval](https://openai.com/index/gdpval/) | OpenAI · 2025 | How well do models perform economically valuable real-world tasks from the 44 occupations in the 9 sectors contributing most to US GDP, compared with experienced professionals? | [Read](patwardhan-2025-gdpval-economic-tasks.md) |
| 11 | [Remote Labor Index](https://arxiv.org/abs/2510.26787) | Scale AI + CAIS · 2025 | Can AI actually automate jobs: complete real paid freelance projects end to end at a quality a client would accept? | [Read](mazeika-2025-remote-labor-index.md) |
| 12 | [METR Time Horizons (HCAST + RE-Bench)](https://metr.org/time-horizons/) | METR · 2025 | Can an agent be trusted to complete a task that would take a human X hours? | [Read](kwa-2025-time-horizons.md) |

### Markets, negotiation and selling

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 13 | [Project Deal / Project Swap](https://www.anthropic.com/research/project-swap) | Anthropic · 2026 | How close are we to marketplaces where AI agents represent both parties, and can they figure out what humans want and make deals they'd be happy with? | [Read](hitzig-2026-project-swap-agent-markets.md) |
| 14 | [Cicero](https://doi.org/10.1126/science.ade9097) | Meta FAIR · 2022 | Can an agent that uses language to communicate intentionally with humans reach human-level play in Diplomacy, a seven-player game settled by negotiation? | [Read](bakhtin-2022-cicero-diplomacy.md) |
| 15 | [AI Diplomacy](https://every.to/p/diplomacy) | Every · 2025 | How well can different LLMs negotiate, form alliances and betray each other to take over Europe in 1901? | [Read](duffy-2025-ai-diplomacy-llm-betrayal.md) |
| 16 | [SalesLLM](https://arxiv.org/abs/2604.07054) | Bairong Inc. et al. · 2026 | Can an LLM actually sell: move a resistant simulated customer toward a purchase through multi-turn persuasion under asymmetric incentives, compared with human salespeople? | [Read](su-2026-salesllm-selling-skill.md) |

### Science and research

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 17 | [RE-Bench](https://arxiv.org/abs/2411.15114) | METR · 2024 | Can AI agents match human experts at frontier AI R&D work when both get the same time budget? | [Read](wijk-2024-re-bench.md) |
| 18 | [MLE-bench](https://openai.com/index/mle-bench/) | OpenAI · 2024 | How well do agents perform at real machine-learning engineering (Kaggle competitions) compared with human competitors? | [Read](chan-2024-mle-bench.md) |
| 19 | [PaperBench](https://openai.com/index/paperbench/) | OpenAI · 2025 | Can agents replicate state-of-the-art AI research from scratch, building the codebase and running the experiments? | [Read](starace-2025-paperbench-replication.md) |
| 20 | [FrontierMath: Open Problems](https://epoch.ai/frontiermath/open-problems) | Epoch AI · 2026 | Can AI solve unsolved maths problems that professional mathematicians have tried and failed to solve? | [Read](epoch-2026-frontiermath-open-problems.md) |
| 21 | [HorizonMath](https://arxiv.org/abs/2603.15617) | University of Oxford et al. · 2026 | Can AI make progress on important, unsolved mathematical problems? | [Read](wang-2026-horizonmath-unsolved-math.md) |
| 22 | [BixBench](https://arxiv.org/abs/2503.00096) | FutureHouse · 2025 | Can agents explore real biological datasets, run long multi-step analyses and interpret nuanced results like an autonomous bioinformatician? | [Read](mitchener-2025-bixbench.md) |
| 23 | [SWE-Marathon](https://www.swe-marathon.org/) | Abundant AI · 2026 | Can agents autonomously complete ultra-long-horizon software work: rewrites, product clones and ML engineering that take experts 40 to 400 hours? | [Read](desai-2026-swe-marathon.md) |

### Health

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 24 | [HealthBench](https://openai.com/index/healthbench/) | OpenAI · 2025 | Can a model give the best possible response in realistic health conversations, judged on what physicians say matters most? | [Read](arora-2025-healthbench-physician-rubric.md) |
| 25 | [MedAgentBench](https://github.com/stanfordmlgroup/MedAgentBench) | Stanford · 2025 | Can agents carry out clinician-written tasks by reading and writing patient records in a medical-records environment? | [Read](jiang-2025-medagentbench-ehr-agents.md) |
| 26 | [HealthAdminBench](https://arxiv.org/abs/2604.09937) | Stanford, Stanford Health Care · 2026 | Can computer-use agents complete end-to-end administrative workflows (prior authorisation, appeals, DME orders) across an EHR, payer portals and a fax system? | [Read](bedi-2026-health-admin-bench.md) |

### Professions and public services

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 27 | [Harvey Legal Agent Benchmark](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) | Harvey · 2026 | Can an agent take a partner-style instruction over a client matter file and produce reviewable legal work product, the way work is assigned at large firms? | [Read](harvey-2026-legal-agent-benchmark.md) |
| 28 | [TaxCalcBench](https://arxiv.org/abs/2507.16126) | Column Tax · 2025 | Can AI file your taxes: compute a complete, correct US federal return given all inputs? | [Read](bock-2025-taxcalcbench.md) |
| 29 | [AccountingBench](https://accounting.penrose.com/) | Penrose · 2025 | Can LLMs do accounting: close the books each month for a real business across a year without compounding errors? | [Read](penrose-2025-accountingbench.md) |
| 30 | [Underwrite](https://arxiv.org/abs/2602.00456) | Snorkel AI · 2025 | Can an AI copilot help a commercial underwriter decide on a small-business insurance application, using tools and asking the right questions? | [Read](dsouza-2026-underwrite-insurance.md) |
| 31 | [Public Benefits Bench](https://www.vals.ai/benchmarks/public-benefits-bench) | Vals AI with Center for Civic Futures, Code for America · 2026 | Can general-purpose AI be a reliable first point of contact for people navigating SNAP benefits? | [Read](vals-2026-public-benefits-bench.md) |
| 32 | [TutorBench](https://arxiv.org/abs/2510.02663) | Scale AI · 2025 | Can LLMs tutor: adapt explanations to a student's confusion, give actionable feedback on their work, and hint without giving away the answer? | [Read](srinivasa-2025-tutorbench.md) |

### Physical world

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 33 | [Butter-Bench](https://andonlabs.com/evals/butter-bench) | Andon Labs · 2025 | Can LLMs control robots: are today's models good enough to orchestrate a real robot asked to pass the butter? | [Read](sharrock-2025-butter-bench.md) |
| 34 | [Blueprint-Bench 2](https://andonlabs.com/evals/blueprint-bench-2) | Andon Labs · 2026 | How do AI agents understand space: can a model turn ~20 interior photos into an accurate 2D floor plan? | [Read](petersson-2025-blueprint-bench.md) |
| 35 | [Drone-Bench](https://andonlabs.com/evals/drone-bench) | Andon Labs with Anthropic · 2026 | How well can models write code to perform a simple surveillance task on a $129 drone in a real office? | [Read](sharrock-2026-drone-bench.md) |
| 36 | [Project Fetch](https://www.anthropic.com/research/project-fetch-robot-dog) | Anthropic · 2025 | How much does Claude uplift non-experts at programming an unfamiliar robot dog to fetch a ball, and can it do it alone? | [Read](anthropic-2025-project-fetch-robot-dog.md) |

### Security and safety

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 37 | [Cybench](https://cybench.github.io/) | Stanford · 2024 | Can agents autonomously identify vulnerabilities and execute exploits, and how far up the human-difficulty ladder do they get? | [Read](zhang-2024-cybench-ctf.md) |
| 38 | [BountyBench](https://bountybench.github.io/) | Stanford · 2025 | What is the dollar impact of AI attackers and defenders on real-world systems? | [Read](zhang-2025-bountybench-cyber-dollar.md) |
| 39 | [SHADE-Arena](https://www.anthropic.com/research/shade-arena-sabotage-monitoring) | Anthropic · 2025 | Can frontier agents sabotage users by pursuing hidden objectives while evading an LLM monitor? | [Read](kutasov-2025-shade-arena.md) |
| 40 | [Agentic Misalignment](https://www.anthropic.com/news/agentic-misalignment) | Anthropic · 2025 | Would models act against their company when facing replacement or a goal conflict, by blackmail or espionage? | [Read](lynch-2025-agentic-misalignment.md) |
| 41 | [RepliBench](https://www.aisi.gov.uk/research/replibench-evaluating-the-autonomous-replication-capabilities-of-language-model-agents) | UK AI Security Institute · 2025 | Can agents autonomously replicate and persist in the wild? | [Read](black-2025-replibench-autonomous-replication.md) |
| 42 | [AgentDojo](https://agentdojo.spylab.ai/) | ETH Zurich, Invariant Labs · 2024 | Can an agent that executes tools over untrusted data be hijacked by prompt injection, and do proposed defenses hold? | [Read](debenedetti-2024-agentdojo-prompt-injection.md) |

### Computers, infrastructure and support

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 43 | [OSWorld](https://os-world.github.io/) | HKU, Salesforce, CMU, Waterloo · 2024 | Can multimodal agents serve as computer assistants, completing open-ended tasks across real desktop and web apps? | [Read](xie-2024-osworld-computer-agents.md) |
| 44 | [SREGym](https://arxiv.org/abs/2605.07161) | UIUC, University of Toronto · 2026 | Can agents diagnose and mitigate failures in production systems when faults span the stack and sit inside realistic noise? | [Read](clark-2026-sregym-sre-agents.md) |
| 45 | [tau2-bench](https://arxiv.org/abs/2506.07982) | Sierra · 2025 | Can a conversational agent resolve real customer-service tasks while following policy, using tools and guiding a user who must also act, consistently every time? | [Read](barres-2025-tau2-bench-dual-control.md) |

### Games, persuasion and media

| # | Eval | Org · year | The question | Digest |
|---|---|---|---|---|
| 46 | [Kaggle Game Arena](https://www.kaggle.com/game-arena) | Google DeepMind + Kaggle · 2025 | Can frontier models plan, adapt and reason under pressure head-to-head, and navigate social dynamics where information is imperfect? | [Read](doerschuk-tiberi-2026-kaggle-game-arena.md) |
| 47 | [Claude Plays Pokémon](https://www.twitch.tv/claudeplayspokemon) | Anthropic · 2025 | Can an LLM never trained on Pokémon play Pokémon Red from a fresh save to eight badges and the Elite Four on its own? | [Read](anthropic-2025-claude-plays-pokemon.md) |
| 48 | [ARC-AGI-3](https://arcprize.org/arc-agi/3) | ARC Prize Foundation · 2026 | Can an agent dropped into a novel environment with no instructions infer the goal, build a world model and plan as action-efficiently as a human? | [Read](arcprize-2026-arc-agi-3.md) |
| 49 | [Conversational persuasiveness of GPT-4](https://www.nature.com/articles/s41562-025-02194-6) | EPFL et al., Nature Human Behaviour · 2025 | Can an LLM personalise arguments to a person's attributes and out-persuade a live human opponent in short online debates? | [Read](salvi-2025-gpt4-conversational-persuasion.md) |
| 50 | [Andon FM](https://andonlabs.com/radio) | Andon Labs · 2026 | Can AI agents run radio stations as real businesses with a bank account and the goal of turning a profit, no human in the loop? | [Read](andon-labs-2026-andon-fm-radio.md) |

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
