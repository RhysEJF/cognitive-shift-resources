# SWARMS Framework Assessment Skill

## Purpose

Evaluate ideas for building distributed AI intelligence systems using the SWARMS framework from *How to Win with Agentic Swarms: A Tactical Field Guide*. This skill provides a structured methodology for scoring, ranking, and comparing ideas against the six SWARMS dimensions to ensure development decisions are grounded in cross-domain principles of distributed intelligence.

**Use this skill when you need to:**
- Assess whether an idea strengthens your system's distributed intelligence capabilities
- Rank multiple ideas against each other using a consistent framework
- Identify which SWARMS dimensions an idea serves (and which it neglects)
- Generate an assessment report with executive summary and actionable recommendations
- Decide what to build next based on strategic alignment with swarm intelligence principles

---

## The SWARMS Framework

The SWARMS framework emerged from cross-domain research spanning swarm intelligence biology, military distributed warfare doctrine, competitive gaming meta-evolution, multi-agent systems science, complexity science, and business strategy. Six interlocking capabilities describe what a system needs to compete effectively with agentic AI:

| Dimension | Core Question | Key Metric | Essence |
|-----------|--------------|------------|---------|
| **S**ENSE | What's happening in our environment? | Signal detection latency | Distributed perception — the swarm that sees more, faster, wins |
| **W**AGE | How do we act faster than competitors? | OODA cycle compression ratio | Tempo advantage — completing sense-decide-act faster compounds |
| **A**DAPT | How do we learn faster than the environment changes? | Adaptation velocity (experiments/cycle) | Strategic evolution — no strategy permanently dominates |
| **R**EPLICATE | How do we scale what works? | Cost-exchange ratio (agent vs human) | Near-zero marginal cost of cognitive replication |
| **M**OBILIZE | How do we coordinate at scale? | Coordination overhead (% of effort) | Right coordination mechanism matched to task structure |
| **S**USTAIN | How do we keep winning long-term? | Governance readiness score | Resilience, governance, continuous improvement |

### Ten Universal Principles (Score Multiplier Reference)

Ideas that align with these principles score higher. Ideas that violate them score lower.

1. **Local rules generate global order.** Design interaction rules, not agent behaviors.
2. **Tempo beats capability.** Faster sense-decide-act cycle > more resources.
3. **The coordination architecture is the competitive advantage.** Same agents, different topology = 4x error difference.
4. **Diversity beats quantity.** Two diverse agents >= 16 identical ones (8x efficiency).
5. **Exploration and exploitation must coexist.** Maintain ~5% exploration capacity.
6. **No strategy permanently dominates.** Build adaptation speed, not commitment.
7. **The environment is the coordination medium.** Stigmergy is the only mechanism that scales to thousands.
8. **Identify the constraint before deploying force.** Automating non-constraints is the costliest mistake.
9. **Design for failure, not perfection.** 41-86.7% failure rates in production — architecture determines if failures improve the system.
10. **The cost-exchange ratio determines the winner.** 10-100x cost advantage makes attrition favorable.

### The Binding Constraint Sequence

As systems mature, the binding constraint shifts predictably:
1. **Cognition** — Agent swarms dissolve this within weeks
2. **Coordination** — Without right architecture, more agents = more chaos
3. **Imagination** — What to do with abundant, coordinated intelligence
4. **Governance** — Risk exposure limits what you're willing to attempt

---

## Assessment Methodology

### Step 1: Understand the Idea

Before scoring, fully characterize the idea:

```
IDEA PROFILE
=============
Name: [idea name]
One-line summary: [what it does in one sentence]
Problem it solves: [what's broken or missing without it]
Mechanism: [how it works at a technical/architectural level]
Scope: [what it touches — which parts of the system]
Dependencies: [what must exist first]
```

### Step 2: Score Each SWARMS Dimension (1-5)

For each dimension, answer the diagnostic questions and assign a score.

---

#### S — SENSE (Distributed Perception and Intelligence)

*Does this idea improve the system's ability to see more, faster?*

| Score | Meaning |
|:-----:|---------|
| 1 | No sensing impact — idea is unrelated to information gathering or awareness |
| 2 | Minor sensing — slight improvement to monitoring or observation in a narrow area |
| 3 | Moderate sensing — adds a new signal source, improves detection latency, or enables parallel observation |
| 4 | Strong sensing — creates distributed perception across multiple domains, builds toward a Common Operational Picture |
| 5 | Transformative sensing — implements stigmergic signal architecture, multi-INT fusion, quorum-based alert escalation, or fundamentally reshapes how the system perceives its environment |

**Diagnostic questions:**
- Does it add new signal sources or sensing modalities?
- Does it reduce the time between event and awareness (signal detection latency)?
- Does it build toward a shared state / Common Operational Picture that agents read from?
- Does it implement signal decay (TTL) to prevent stale information accumulation?
- Does it enable quorum-based decisions (3+ convergent signals) rather than single-source conclusions?
- Does it follow the 5:95 scout-to-follower ratio for exploration vs exploitation?

**Key patterns from the guide:**
- Ant pheromone trails (stigmergic environmental intelligence)
- Bee waggle dance (quality-proportional advocacy with cross-inhibition)
- Military multi-INT fusion (diverse sensing modalities > quantity)
- Wolfpack patrol line (distributed coverage across information domains)
- The COP must be built before the agents

---

#### W — WAGE (Competitive Engagement and Tempo)

*Does this idea compress the sense-decide-act cycle?*

| Score | Meaning |
|:-----:|---------|
| 1 | No tempo impact — does not affect speed of action |
| 2 | Minor tempo — slightly reduces latency in one phase of execution |
| 3 | Moderate tempo — compresses one or more OODA phases meaningfully, enables parallel execution |
| 4 | Strong tempo — enables concurrent OODA loops across multiple functions, implements surge capability |
| 5 | Transformative tempo — creates order-of-magnitude cycle compression, enables wolfpack-style concentration from distributed assets, or establishes decisive cost-exchange ratio |

**Diagnostic questions:**
- Does it compress any phase of the OODA loop (Observe/Orient/Decide/Act)?
- Does it enable parallel OODA loops across different domains?
- Does it improve the cost-exchange ratio (value produced / cost of compute + supervision)?
- Does it enable surge capability — rapid concentration of resources on opportunities?
- Does it follow macro-before-micro (production infrastructure before individual optimization)?
- Does it create asymmetric advantage (doing 10-100x more for the same cost)?

**Key patterns from the guide:**
- Boyd's OODA loop (faster cycle = compounding advantage)
- Wolfpack 5-phase cycle (distributed search → contact → concentration → attack → dispersal)
- StarCraft macro > micro (production engine before tactical optimization)
- Timing attacks (strike during investment-payoff gap)
- Cost-exchange ratio as the metric that determines the winner

---

#### A — ADAPT (Strategic Evolution and Learning)

*Does this idea make the system learn faster than conditions change?*

| Score | Meaning |
|:-----:|---------|
| 1 | No adaptation impact — static, does not learn or evolve |
| 2 | Minor adaptation — captures some learnings but doesn't systematically apply them |
| 3 | Moderate adaptation — implements feedback loops, enables experimentation, or captures cross-task learnings |
| 4 | Strong adaptation — enables parallel strategy exploration, implements kill thresholds for failing approaches, maintains exploration budget |
| 5 | Transformative adaptation — implements mission command (intent-based delegation), navigates rugged fitness landscapes via parallel multi-start search, or builds meta-game awareness |

**Diagnostic questions:**
- Does it implement feedback loops that improve future performance?
- Does it maintain an exploration budget (~5%) alongside exploitation?
- Does it enable killing failing strategies quickly (stop signals, cross-inhibition)?
- Does it support mission command (define what/why, delegate how)?
- Does it help navigate rugged fitness landscapes (parallel exploration vs hill-climbing)?
- Does it detect metagame shifts (disruption → experimentation → convergence → staleness)?

**Key patterns from the guide:**
- Red Queen dynamics (running to stay in place — adaptation velocity is the only durable moat)
- Bee democracy (quality-proportional advocacy + stop signals + quorum)
- Mission command / Auftragstaktik (intent-based delegation)
- AlphaStar league training (diverse strategies + exploiter agents)
- NK fitness landscapes (parallel multi-start search reaches 85-95% vs 50-70% for hill-climbing)
- ~5% exploration allocation convergent across biology, gaming, RL, and business

---

#### R — REPLICATE (Scaling Intelligence Operations)

*Does this idea scale what works at near-zero marginal cost?*

| Score | Meaning |
|:-----:|---------|
| 1 | No scaling impact — one-off solution that doesn't replicate |
| 2 | Minor scaling — could be reused with manual effort |
| 3 | Moderate scaling — creates reusable patterns, templates, or skills that reduce cost of subsequent similar work |
| 4 | Strong scaling — enables automated replication of cognitive work, implements diversity-based scaling (not just more identical agents) |
| 5 | Transformative scaling — achieves near-zero marginal cost replication, implements stigmergic coordination for scale, or enables collaborative emergence at 16-32+ agents |

**Diagnostic questions:**
- Does it reduce the marginal cost of doing the next similar task?
- Does it create reusable skills, tools, or patterns?
- Does it implement diversity-based scaling (different models/prompts) rather than homogeneous scaling (which plateaus at ~4)?
- Does it use stigmergic coordination (shared environment) rather than direct messaging (O(N^2))?
- Does it account for total cost of ownership (2-3x raw compute: supervision, error correction, infrastructure)?
- Does it follow slime mold principles (reinforce what works, prune what doesn't, optimize for the triad)?

**Key patterns from the guide:**
- Near-zero marginal cost of cognitive replication (10-100x cheaper than human)
- Homogeneous scaling plateaus at ~4 agents; diversity is the true lever
- Collaborative emergence at 16-32 agents
- Stigmergy scales linearly; direct communication scales quadratically
- Slime mold Pareto-optimal networks (cost + efficiency + fault tolerance)
- TCO = 2-3x raw compute (supervision, errors, infrastructure, maintenance)

---

#### M — MOBILIZE (Coordinated Execution)

*Does this idea improve coordination without adding overhead?*

| Score | Meaning |
|:-----:|---------|
| 1 | No coordination impact — operates in isolation |
| 2 | Minor coordination — connects to existing workflows but adds communication overhead |
| 3 | Moderate coordination — implements task deconfliction, shared state, or role specialization |
| 4 | Strong coordination — uses Reynolds rules (separation/alignment/cohesion), implements 6-7 neighbor topology, or enables mission command delegation |
| 5 | Transformative coordination — implements stigmergic coordination through shared environment, enables composable mosaic-warfare-style capability routing, or achieves 1-human-to-50+ agent oversight |

**Diagnostic questions:**
- Does it reduce coordination overhead as agent count grows?
- Does it implement indirect coordination (stigmergy) rather than direct agent-to-agent messaging?
- Does it follow Reynolds rules (separation: don't duplicate; alignment: same direction; cohesion: outputs integrate)?
- Does it enable role specialization matched to task structure (MOBA team composition)?
- Does it implement the autonomy spectrum (matching oversight level to decision complexity)?
- Does it support the 6-7 neighbor rule (each agent tracks nearest relevant peers, not all agents)?

**Key patterns from the guide:**
- Reynolds 3 rules (separation, alignment, cohesion) = global coordination from local rules
- 6-7 neighbor topological rule (Ballerini starling study)
- Stigmergy as the only mechanism that scales to thousands
- Mission command: intent + boundaries + escalation triggers
- MOBA team composition (tank/carry/support/jungler/flex = measurable advantage from draft alone)
- 1 human can oversee 50-200+ agents with right control abstractions

---

#### S — SUSTAIN (Resilience, Governance, and the Long Game)

*Does this idea make the system more durable and antifragile?*

| Score | Meaning |
|:-----:|---------|
| 1 | No sustainability impact — fragile, breaks under stress |
| 2 | Minor sustainability — adds basic error handling or monitoring |
| 3 | Moderate sustainability — implements circuit breakers, error budgets, or structured learning from failures |
| 4 | Strong sustainability — implements the resilience triad (circuit breakers + bulkheads + error budgets), continuous improvement loops, or governance tiers |
| 5 | Transformative sustainability — creates antifragile architecture (gains from stress), implements Hollnagel's four potentials (respond/monitor/learn/anticipate), or enables organizational evolution |

**Diagnostic questions:**
- Does it implement the resilience triad (semantic circuit breakers + agent cell architecture + error budgets)?
- Does it design for failure (accepting 41-86.7% failure rates and engineering around them)?
- Does it implement after-action reviews or structured learning from operations?
- Does it support governance tiers (low/medium/high risk with proportional oversight)?
- Does it enable graceful degradation rather than catastrophic failure?
- Does it make the system antifragile (improving from stress, not just surviving it)?

**Key patterns from the guide:**
- Resilience triad: semantic circuit breakers + bulkheads + error budgets
- Antifragility: fragile → robust → resilient → adaptive → antifragile
- Hollnagel's Safety-II: respond, monitor, learn, anticipate
- Governance as deployment accelerator (3.4x more likely to achieve effectiveness)
- 80% of AI value from organizational redesign, not technology
- After-action reviews as compounding learning mechanism

---

### Step 3: Calculate Scores

For each idea, produce the following:

```
SWARMS SCORECARD
================
Idea: [name]

  S (SENSE):     [1-5] — [one-line justification]
  W (WAGE):      [1-5] — [one-line justification]
  A (ADAPT):     [1-5] — [one-line justification]
  R (REPLICATE): [1-5] — [one-line justification]
  M (MOBILIZE):  [1-5] — [one-line justification]
  S (SUSTAIN):   [1-5] — [one-line justification]

  TOTAL:         [sum]/30
  AVERAGE:       [avg]/5.0

  Strongest dimension:  [which and why]
  Weakest dimension:    [which and why]
  Binding constraint:   [which constraint in the sequence does this address?
                         Cognition / Coordination / Imagination / Governance]
```

### Step 4: Principle Alignment Check

For each idea, check alignment with the 10 universal principles:

| # | Principle | Alignment | Notes |
|:-:|-----------|:---------:|-------|
| 1 | Local rules → global order | +/0/- | |
| 2 | Tempo beats capability | +/0/- | |
| 3 | Coordination architecture is the advantage | +/0/- | |
| 4 | Diversity beats quantity | +/0/- | |
| 5 | Exploration + exploitation coexist | +/0/- | |
| 6 | No strategy permanently dominates | +/0/- | |
| 7 | Environment is the coordination medium | +/0/- | |
| 8 | Identify constraint before deploying force | +/0/- | |
| 9 | Design for failure, not perfection | +/0/- | |
| 10 | Cost-exchange ratio determines winner | +/0/- | |

**Principle alignment score:** [count of +] / 10

---

### Step 5: Generate Assessment Report

Produce the full report in this format:

---

```
╔══════════════════════════════════════════════════════════════╗
║              SWARMS FRAMEWORK ASSESSMENT REPORT             ║
╚══════════════════════════════════════════════════════════════╝

Date: [date]
Assessed by: SWARMS Assessment Skill v1.0
Ideas evaluated: [count]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTIVE SUMMARY
─────────────────
[2-3 paragraph summary including:]
- Which ideas scored highest and why
- Which SWARMS dimensions are most/least served across all ideas
- The current binding constraint these ideas collectively address
- Strategic recommendation: what to build first and in what sequence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RANKING TABLE
─────────────
| Rank | Idea | S | W | A | R | M | S | Total | Avg | Constraint |
|:----:|------|:-:|:-:|:-:|:-:|:-:|:-:|:-----:|:---:|:----------:|
| 1 | ... | | | | | | | /30 | /5 | ... |
| 2 | ... | | | | | | | /30 | /5 | ... |
| ... | | | | | | | | | | |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DIMENSION HEATMAP
─────────────────
[Show which dimensions are well-covered and which have gaps]

          SENSE  WAGE  ADAPT  REPL  MOBIL  SUST
Idea 1:   ████   ██    ███    █     ████   ██
Idea 2:   ██     ████  ██     ████  ███    ███
...

Legend: █=1, ██=2, ███=3, ████=4, █████=5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INDIVIDUAL ASSESSMENTS
──────────────────────
[For each idea, include:]

### [Rank]. [Idea Name] — [Total]/30

**Summary:** [1-2 sentences on what this idea does]

**SWARMS Scorecard:**
  S (SENSE):     [score] — [justification]
  W (WAGE):      [score] — [justification]
  A (ADAPT):     [score] — [justification]
  R (REPLICATE): [score] — [justification]
  M (MOBILIZE):  [score] — [justification]
  S (SUSTAIN):   [score] — [justification]

**Principle Alignment:** [X]/10 principles aligned
**Binding Constraint Addressed:** [which]
**Key Strengths:** [bullets]
**Key Gaps:** [bullets]
**Recommendation:** [build now / build later / needs refinement / deprioritize]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRATEGIC ANALYSIS
──────────────────

### Portfolio Balance
[Are the ideas collectively covering all SWARMS dimensions, or
 clustered in a few? What dimensions need more ideas?]

### Constraint Sequence Alignment
[Where is the system in the binding constraint sequence?
 Are the highest-ranked ideas targeting the current constraint?]

### Build Sequence Recommendation
[Ordered list of what to build and why, based on:]
1. Constraint targeting (address the binding constraint first)
2. Dependency ordering (what enables what)
3. SWARMS score (higher = more strategic value)
4. Principle alignment (ideas violating principles should be redesigned)

### Gaps and Missing Ideas
[What SWARMS dimensions are underserved? What ideas are needed
 but not yet proposed?]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APPENDIX: PRINCIPLE ALIGNMENT MATRIX
─────────────────────────────────────
| Principle | Idea 1 | Idea 2 | Idea 3 | ... |
|-----------|:------:|:------:|:------:|:---:|
| 1. Local rules → global order | +/0/- | | | |
| 2. Tempo beats capability | | | | |
| 3. Coordination = advantage | | | | |
| 4. Diversity > quantity | | | | |
| 5. Explore + exploit | | | | |
| 6. No permanent dominance | | | | |
| 7. Environment = medium | | | | |
| 8. Constraint first | | | | |
| 9. Design for failure | | | | |
| 10. Cost-exchange ratio | | | | |
```

---

## Scoring Calibration Guide

To ensure consistent scoring across assessments, use these calibration anchors:

### What a "5" looks like per dimension:

- **SENSE 5:** An idea that implements a distributed sensing architecture with multiple signal types, shared state (COP), TTL-based signal decay, and quorum-based escalation. Example: A system where multiple agents monitor different domains and write to a shared intelligence layer that other agents read from.

- **WAGE 5:** An idea that compresses the full OODA loop by an order of magnitude, enables parallel loops across functions, and creates cost-exchange ratios >10x. Example: A system that enables wolfpack-style surge (distributed sensing → rapid concentration → coordinated multi-axis execution → dispersal).

- **ADAPT 5:** An idea that implements systematic parallel experimentation, kill thresholds for failing approaches, mission command delegation, and meta-game awareness. Example: A system that runs multiple strategy variants simultaneously, selects via Nash equilibrium, and detects when the competitive landscape is shifting.

- **REPLICATE 5:** An idea that enables cognitive work to be replicated at near-zero marginal cost with diversity-based scaling and stigmergic coordination. Example: A system where every successful task creates reusable skills/patterns that automatically reduce cost of similar future tasks, scaling through diverse agents rather than identical clones.

- **MOBILIZE 5:** An idea that implements stigmergic coordination through shared environment, achieves coordination overhead <15% at 50+ agents, and enables composable capability routing. Example: A shared state system where agents deposit and read signals without direct messaging, self-coordinating through environmental modification.

- **SUSTAIN 5:** An idea that creates antifragile architecture where failures systematically improve the system, implements all four Hollnagel potentials, and enables organizational evolution. Example: A system with chaos engineering, after-action reviews feeding into automatic configuration improvement, and graceful degradation under any single-component failure.

### What a "1" looks like:

Any idea that has zero relevance to the dimension. A UI cosmetic change scores 1 on SENSE. A one-off script scores 1 on REPLICATE. A feature with no error handling scores 1 on SUSTAIN.

---

## Usage Examples

### Assessing a single idea:
```
Assess this idea using the SWARMS framework:
"Agent messaging system — workers that can communicate with each
other to share context and coordinate on complex tasks"
```

### Assessing multiple ideas:
```
Run a SWARMS assessment on all ideas in my backlog and rank them.
```

### Assessing with context:
```
Assess these ideas with the understanding that our system is currently
at the Coordination constraint (constraint #2 in the sequence).
Prioritize accordingly.
```

---

## Source

This skill is based on *How to Win with Agentic Swarms: A Tactical Field Guide* (Version 1.0, March 2026), a 54,000-word field guide synthesised by 86 AI agents across six research domains: swarm biology, military doctrine, competitive gaming, multi-agent systems, complexity science, and business strategy.

Read the full story: [Swarm Intelligence: The Book 86 AI Agents Wrote While I Slept](https://thecognitiveshift.com/publications/let-them-run/swarm-intelligence-the-book-86-ai-agents-wrote-while-i-slept/)
