---
name: Bandwidth-Bound Migration
slug: bandwidth-bound-migration
category: post-scarcity
source: "Charles Stross, Accelerando (2005) — Ch5: Router. Pierre realizes the interstellar router network's wormholes are 'unimaginably low-bandwidth' compared to the transcendent minds they connect — the Fermi paradox answer: superintelligences can't migrate because the channel is too narrow. Intellectual parallels: Michael Polanyi on tacit knowledge (The Tacit Dimension, 1966); bandwidth-limited communication theory (Shannon); Claude Shannon on channel capacity; migration-cost literature in labour economics."
source_anchor: "Ch5: Router, p143 (Pierre's Fermi-paradox realisation — continuous dialogue with narrator action-beats between the two speech acts)"
source_quote: "Pierre, p143 (opening observation): 'It's unimaginably big! These wormholes, they're a low-bandwidth link compared to the minds they're hooking up to.' / Pierre, p143 (continuing after a narrator action-beat — 'He blurs in front of her, unable to stay still and unable to look away from the front panel. Excitement or agitation? Su Ang can't tell. With Pierre, sometimes the two states are indistinguishable. He gets emotional easily.'): 'I think we have the outline of the answer to the Fermi paradox. Transcendents don't go traveling because they can't get enough bandwidth — trying to migrate through one of these wormholes would be like trying to download your mind into a fruit fly, if they are what I think they are — and the slower-than-light route is out, too, because they couldn't take enough computronium along.' [Validation note: the original source_quote in this file joined Pierre's two statements with '...' eliding the narrator action-beat as if continuous. Same speaker, same page, same dialogue — but shown as two separate utterances with the eliding text now visible. Corrected 2026-04-23.]"
difficulty: advanced
decision_types: [strategy, hiring, operations, knowledge-transfer, expansion, M&A, technology-selection, product]
chains_well_with: [substrate-independence-of-cognition, externalized-cognition-fragility, jurisdictional-arbitrage-via-structure-layering, agalmic-economy]
opposite_of: lossless-transmission-assumption
---

# Bandwidth-Bound Migration

> Every transit medium — between jurisdictions, platforms, companies, minds, generations — has a bandwidth ceiling. Entities whose complexity exceeds that ceiling cannot migrate through it. What crosses a channel is not what was most valuable on the other side; it is the subset of value that fit through. The thinner the channel, the lower the quality of what migrates.

## What It Is

Any transfer of something complex — a person, a team, a business unit, a tacit practice, a culture, an AI system, a memory — passes through a channel whose capacity is finite. If the source complexity exceeds the channel's capacity, the transfer cannot be lossless. Either the source is compressed (losing everything that doesn't fit), or the transfer fails entirely.

In *Accelerando*, the galactic network is made of wormholes carrying bits between star systems. Pierre's realization at the router: they're "unimaginably low-bandwidth" compared to the transcendent civilizations at each end. A mature Matrioshka-brain civilization running at 10^33 MIPS cannot migrate to another star — not because they lack technology, but because trying to squeeze their state through a wormhole would be "like trying to download your mind into a fruit fly." The solution to the Fermi paradox is not that intelligence is rare — it's that *bandwidth-bound migration limits who gets to cross*. What travels between stars is tiny probes, simple protocols, and scavenger species (cf. the Wunch) — not the transcendents themselves. The big minds stay home.

The pattern generalizes to any channel that connects two domains of varying complexity:

- **Tacit knowledge channels**: Documentation, playbooks, onboarding docs. The channel bandwidth is whatever survives writing-it-down. Polanyi's observation ("we know more than we can tell") is exactly this model — the tacit portion can't migrate through text, so when an expert leaves and a document remains, most of their value stayed.
- **Migration channels**: Immigration, acquihires, executive transitions. The channel is whatever survives relocation — context, relationships, embedded practices get stripped. A star engineer hired from Google rarely reproduces their Google performance, because the Google around them didn't come with.
- **Tool migrations**: Porting a mature system from one stack to another. The channel is whatever the new stack's primitives can express. Legacy software that ran on mainframes for 40 years rarely migrates to cloud without dramatic capability loss — the channel (modern frameworks) can't carry the complexity that was in COBOL + specific hardware + decades of operator knowledge.
- **Cultural migration**: Company mergers, post-acquisition integration. Culture mostly doesn't survive — the channel (org charts, policy documents, new process) is vastly narrower than the sending culture's tacit mesh.
- **Knowledge transfer across generations**: Master-apprentice transfer versus lecture-based instruction. The latter is a thinner channel; most crafts that depended on dense apprenticeship lose skill tier when forced through schools.

The post-scarcity twist is that as intelligence and complexity grow exponentially, channels (wires, docs, APIs, HR transitions) grow linearly. The gap between source and channel widens. More and more valuable things become un-migratable. The economic implication: *whatever cannot cross the channel must be held where it currently is, or lost*. It cannot be relocated, centralized, acquired, or rebuilt elsewhere.

The model does NOT say transfer is impossible — it says transfer is bandwidth-limited, and you must design for what fits. The useful move is to measure the channel, measure the complexity, and decide explicitly: compress, replicate in place, or accept the loss.

## When to Use It

Use this model when you're:
- Planning knowledge transfer from a departing expert (or yourself in a transition)
- Acquiring a company for its team or culture — how much of the value is un-migratable?
- Building documentation for a complex system — what part of the system won't fit through the docs?
- Designing cross-jurisdictional expansion (product, compliance, operations) — what dies in the channel?
- Evaluating whether a centralization move (consolidate HQ, move from Country A to Country B) will preserve or destroy capability
- Rolling out a training program — what part of the expertise won't survive classroom format?
- Thinking about AI/ML system portability across model providers — what lives in the specific model vs the prompts/scaffolding?
- Analyzing why a distributed / remote / franchised model underperforms its centralized origin — where is the bandwidth loss?

**Don't use it when:** The source is low-complexity and fits the channel easily (simple process migrations, well-understood commodity transfers). The model is only useful when complexity exceeds channel capacity; applying it everywhere turns it into paranoia.

## The Walkthrough

### Step 1: Identify the source, the channel, and the destination

Name them explicitly:
- **Source**: the full complex entity (a person, team, system, culture, practice) with all its embedded context
- **Channel**: the medium through which transfer happens (a document, onboarding process, system port, acquisition integration, training curriculum)
- **Destination**: where the entity is supposed to land (a new hire, a new company post-merger, a new framework, a new geography)

Without this framing, you'll implicitly assume the channel is lossless — which is the failure mode the model corrects.

### Step 2: Measure the channel's bandwidth

Ask: *what does this channel actually carry?* A 20-page handover doc carries ~words. A three-week onboarding carries words + some observation of ongoing work + limited dialogue. An apprenticeship carries years of embedded observation and correction. An acquisition integration carries org chart + policy + a few key hires' continuity.

Each channel has a *measurable capacity* in the dimensions that matter (bits, hours, relationships preserved, context retained). Put a number on it — even a rough one.

### Step 3: Measure the source's complexity

Ask: *what is the total complexity being transferred?* This includes the explicit (what's written down, what's in the code), the tacit (what the expert does without noticing), the relational (the network around them), and the contextual (the surrounding system that makes their work work).

A useful heuristic: if the source has been running for N years and the channel is M hours wide, most of the source is not going to fit. The gap is the scale of your expected loss.

### Step 4: Decide: compress, replicate in place, or accept loss

Given the mismatch, you have three real options. Most organizations implicitly pick option 4 — pretend the channel is lossless — and pay the cost later.

- **Compress**: Accept that only a subset survives, and design the channel to preserve the highest-leverage subset. Prioritize what must be carried (core patterns, critical relationships) and let the rest go. This is honest; most transfer projects should be scoped this way.
- **Replicate in place**: Don't migrate. Leave the source where it is and access it remotely. Examples: don't acquihire — partner. Don't centralize ops — federate with autonomy. Don't try to port legacy software — wrap it with an API. Don't move the expert to HQ — let HQ's work come to them.
- **Accept the loss**: If compression and replication are both infeasible, and migration still has positive expected value even with loss, proceed — but *explicitly budget for the degraded output*. The mistake is believing you'll get 100% of source value at the other end; you won't.

### Step 5: Post-transfer, audit what actually made it

After transfer, measure honestly: what fraction of source value is operating at destination? Expected ranges:
- Document-only transfer: 5-20% of expert value
- Onboarding-plus-shadowing: 30-50%
- Full relocation (person physically moves, network follows): 60-80%
- Replicate-in-place (wrap remote source): 80-100% but with ongoing dependency cost

Use this audit to calibrate future transfers in the same channel class.

## Example

**Decision:** A software company is considering acquiring a 40-person consulting firm known for a specific methodology. The CEO wants to buy the firm to bring the methodology in-house. Cost: $30M. Expected: integrate the team into the parent company's product line within 12 months.

**Applying Bandwidth-Bound Migration:**
- **Step 1 — Source, channel, destination:**
  - Source: 40-person firm with 15 years of embedded practice, client relationships, inside jokes, shared mental models, specific judgments about when the methodology fails
  - Channel: 12-month acquisition integration (reorg, new reporting lines, IP assignment, onboarding to parent's stack, cultural alignment workshops)
  - Destination: parent company product team, which operates in a different culture (software product vs consulting services)
- **Step 2 — Channel bandwidth:** Acquisition integration is a notoriously low-bandwidth channel. It transmits: ownership, IP, org chart, some key people's continuity (if they stay — most don't past year 2). It does NOT transmit: methodology's tacit judgments, consulting culture, client relationships post-rebrand, the "when not to apply X" knowledge.
- **Step 3 — Source complexity:** 15 years × 40 people × a practice deeply shaped by client work = enormous. Probably only 10-20% is documentable. The rest lives in the room when senior consultants discuss a tricky case.
- **Step 4 — Decide:**
  - *Compress*: Would preserve maybe 15% of the methodology — written playbook, case studies. Probably enough for basic product integration.
  - *Replicate in place*: Don't acquire. Contract the firm for product-dev collaboration. Keep them operating as they are. Buy access, not ownership. Cost: ~$5M/year indefinitely vs $30M upfront with uncertain retention.
  - *Accept loss*: Acquire and budget for 70-85% value loss. Then the $30M purchase is really buying the 15% compression + 2 years of retention.
- **Decision:** Replicate in place. Partnership structure with retained autonomy. Use the channel wisely: monthly senior sync, joint client engagements, staff rotations. Cost 80% less for 3x the preserved value.

**Key insight:** The CEO's instinct ("we bought the methodology, now it's ours") assumed a lossless channel. Threshold analysis showed the channel would strip most of what made the firm valuable. The acquirer would own a name, an IP portfolio, and a dissolving team — which is what most consulting-firm acquisitions actually deliver (cf. most Big 4 consulting acquisitions of design firms in 2010-2020).

## Chains Well With

- **Substrate Independence of Cognition** (`/substrate-independence-of-cognition`): SIOC says cognition is portable across substrates — but Bandwidth-Bound Migration constrains which *complexity* is portable. A cognition simple enough can be substrate-independent; one complex enough cannot cross narrow channels. Chain them to map which cognition-transfers work.
- **Externalized Cognition Fragility** (`/externalized-cognition-fragility`): Offloaded cognition depends on infrastructure that often has narrow bandwidth to the next substrate (losing your glasses, losing your cloud provider). Bandwidth-Bound Migration names why replacement is hard.
- **Jurisdictional Arbitrage via Structure Layering** (`/jurisdictional-arbitrage-via-structure-layering`): When moving structure between jurisdictions, the channel (legal conversion, local compliance translation) has real bandwidth limits. Some complexities in the source jurisdiction don't survive the move.
- **Agalmic Economy** (`/agalmic-economy`): Agalmic value (reputation, trust, community) is notoriously bandwidth-bound — it lives in relationships that don't port. Trying to "monetize" reputation often reveals how much was in the un-migratable substrate.

## Go Deeper

- *Accelerando*, Ch5: Router — Pierre's realization about transcendents and bandwidth at pp142-143.
- Michael Polanyi, *The Tacit Dimension* (1966) — foundational text on why much of expert knowledge doesn't survive transcription.
- Claude Shannon, *A Mathematical Theory of Communication* (1948) — the original channel-capacity theorem; all derivative applications build on this.
- Acquisition integration literature (e.g., HBS research on post-M&A team retention): empirically, 50-70% of acquired key talent departs within 3 years. The source complexity doesn't survive the acquisition channel.
- The Fermi paradox literature: Bandwidth-Bound Migration offers one answer (the "great filter" is not a disaster; it's that transcendents cannot compress through the channels available). Cf. Sandberg, Armstrong, Ćirković, "Dissolving the Fermi Paradox" (2018).
- Remote-work / distributed-company literature: why culture "doesn't travel" when you go remote — the office as a wide-bandwidth channel that Slack+Zoom can't replicate.
- Apprenticeship traditions (Japanese craft, medical residency, law firm partner-track) — high-bandwidth multi-year channels designed for complexity that can't survive thinner media.
