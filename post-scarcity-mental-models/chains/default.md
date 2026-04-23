---
name: Post-Scarcity Default Chain
slug: post-scarcity-default
description: The default chain for /post-scarcity — reframes a decision through five post-scarcity models from Accelerando, revised after the full 9-chapter extraction completed
models: [substrate-independence-of-cognition, agalmic-economy, optimizer-predation-thesis, asymmetric-theory-of-mind-dominance, first-case-precedent-lock-in]
decision_type: post-scarcity
estimated_time: 25-35 minutes
status: stable (revised post-Ch9 from initial 3-chapter provisional chain)
coverage: 9 of 9 Accelerando chapters extracted; 24 total models in the post-scarcity set
---

# Post-Scarcity Default Chain

> For decisions where the usual assumptions (scarcity, priced exchange, human labour, human regulators, gradual change, symmetric cognition) may not hold. Run any strategic, product, policy, AI-related, or labour decision through this chain to see what a post-scarcity lens surfaces.

## When to Use This Chain

- You're pricing something whose marginal cost is near zero (software, AI outputs, content, data)
- You're deciding whether to migrate to a new regime (AI-native workflow, new platform, new protocol) or defend an incumbent
- You're making a call that involves AI agents, uploaded minds, or any non-human cognition
- You're setting policy, terms, or a "first of its kind" contract — and the precedent will stick
- You're operating across a capability-asymmetry gap (negotiating with a much-better-prepared counterparty, working with AI systems, dealing with platform-scale opponents)
- You feel the default business logic ("charge more, lock it down") is missing something

## The Chain (run in this order)

### 1. Substrate Independence of Cognition
**File:** `memory/frameworks/post-scarcity/substrate-independence-of-cognition.md`

Start here. Ask: which parts of this decision silently assume *human* cognition / embodiment / attention? If an AI agent, an uploaded mind, or a swarm could do it, what breaks? What opens up?

**Pass forward:** a cleaned-up description of the decision with substrate assumptions surfaced and questioned.

### 2. Agalmic Economy (Value Without Exchange)
**File:** `memory/frameworks/post-scarcity/agalmic-economy.md`

Now ask: if marginal cost is near zero here, does "price" still coordinate value? Or does value actually flow through reputation, distribution, and access? Who is the node everyone routes through, and how do you become it?

**Pass forward:** whether the decision belongs in a priced-exchange frame, a gift/reputation frame, or a hybrid.

### 3. Optimizer-Predation Thesis
**File:** `memory/frameworks/post-scarcity/optimizer-predation-thesis.md`

Then ask: is there a more-efficient regime that structurally consumes the regime this decision sits inside? If yes — are you migrating, hedging, or harvesting? Late adopters get punitive consequences; lateness is the expensive position. Where are you on the adoption curve, and is the new regime's advantage structural (network-externality-driven) or subsidised (funding-driven)?

**Pass forward:** migrate / hedge / harvest decision plus an explicit position on the adoption curve.

### 4. Asymmetric Theory-of-Mind Dominance
**File:** `memory/frameworks/post-scarcity/asymmetric-theory-of-mind-dominance.md`

Then ask: is the counterparty to this decision modelling you more completely than you are modelling them? If so, reasoning-based strategies lose deterministically. Shift to structural moves: randomisation, pre-commitment, third-party verification, destructive-sandbox evaluation, or exit. This model applies whenever there is a capability asymmetry (AI system, platform, state actor, career professional with full dossier, long-duration relationship).

**Pass forward:** an estimate of modelling-asymmetry and a list of structural moves if asymmetry is large.

### 5. First-Case Precedent Lock-In
**File:** `memory/frameworks/post-scarcity/first-case-precedent-lock-in.md`

End here. Ask: is this a first-of-its-kind decision whose pattern will be copied? If so, what precedent does today's choice lock in, and is that the precedent you want industry / regulators / your future self to inherit? If the answer is unclear, slow the decision down and widen the stakeholder set.

**Pass forward:** the precedent you are knowingly setting (or inheriting).

## Decision Brief Template

- **The decision:** [What you're choosing]
- **Substrate assumptions surfaced:** [What broke when you questioned "human-only"]
- **Value flow:** [Priced exchange / gift-reputation / hybrid — and why]
- **Regime-succession position:** [Early / middle / late on the adoption curve — migrate / hedge / harvest]
- **Modelling asymmetry:** [Symmetric / moderate / high — structural moves if high]
- **Precedent being set:** [The pattern today's choice locks in]
- **Recommendation:** [One or two sentences, with confidence: high / medium / low]
- **Next steps:** [2-3 concrete actions]

## Notes on Using a Subset

If the decision clearly doesn't touch cognition/labour (skip model 1), isn't about pricing/value (skip model 2), isn't a regime-succession situation (skip model 3), doesn't involve adversarial capability asymmetry (skip model 4), or isn't precedent-setting (skip model 5), drop those models and note the skip in the brief. A shorter, relevant chain beats a longer, forced one.

## Revision History

**Initial provisional chain (Ch1-3 coverage, 2026-04-23)**: Substrate Independence → Agalmic Economy → Abundance Graduation → Turing-Complete Regulatory Automation → First-Case Precedent Lock-In.

**Revised chain (post-Ch9, 2026-04-23)** — this document. Replaced Abundance Graduation and Turing-Complete Regulatory Automation with Optimizer-Predation Thesis and Asymmetric Theory-of-Mind Dominance.

### Rationale for the revision

After completing all 9 chapters:

- **Abundance Graduation** demoted to optional extension — still load-bearing for pricing-specific decisions (is this good exiting the market?) but narrower than Optimizer-Predation, which handles the broader regime-succession question. Optimizer-Predation subsumes much of Abundance Graduation's strategic content because regime succession is a more common post-scarcity decision than market-exit specifically.
- **Turing-Complete Regulatory Automation** demoted to optional extension — still essential for compliance/legal decisions but applies to a narrow slice of post-scarcity decisions compared to Asymmetric Theory-of-Mind Dominance, which applies to any decision involving capability asymmetry (which in 2026+ means most strategic AI-related decisions).
- **Optimizer-Predation Thesis** promoted to default — it is the sharpest articulation of the post-scarcity dynamics across the book and applies to any decision adjacent to a regime-succession dynamic (migration to AI-native work, platform shifts, protocol adoption).
- **Asymmetric Theory-of-Mind Dominance** promoted to default — it is the book's most operationally consequential lens for the current era of AI and platform capability, directly relevant to most strategic decisions.

## Optional Extensions (relevant when domain fits)

24 models total in the post-scarcity set. Beyond the default chain, the following are common candidates for situational insertion:

**For market / pricing decisions:**
- **Abundance Graduation** (`/abundance-graduation`) — insert after Agalmic Economy; ask "should this thing be in a market at all?"

**For legal / compliance / governance decisions:**
- **Turing-Complete Regulatory Automation** (`/turing-complete-regulatory-automation`) — insert before First-Case Precedent; ask "which rules move to code?"
- **Jurisdictional Arbitrage via Structure Layering** (`/jurisdictional-arbitrage-via-structure-layering`) — insert when cross-border structure is relevant
- **Sovereignty Threshold** (`/sovereignty-threshold`) — insert when capability accumulation across a threshold is plausible

**For AI / tool / capability decisions:**
- **Dehumanization Tax on Participation** (`/dehumanization-tax-on-participation`) — insert after Optimizer-Predation; prices the cost of crossing
- **Externalized Cognition Fragility** (`/externalized-cognition-fragility`) — insert after Substrate Independence; asks what breaks when the tool is gone
- **Bandwidth-Bound Migration** (`/bandwidth-bound-migration`) — insert when knowledge/cognition transfer is involved

**For frontier / entry / new-network decisions:**
- **New-Entrant Scam Surface** (`/new-entrant-scam-surface`) — insert when entering a novel space
- **Grammatical Weapon** (`/grammatical-weapon`) — insert when translation/framing layers are in play
- **Category Rupture at Referent Expansion** (`/category-rupture-at-referent-expansion`) — insert when referent classes are expanding and frameworks are breaking

**For long-horizon / strategy decisions:**
- **Local Maximum Collapse** (`/local-maximum-collapse`) — insert when the entity is at peak fit in its current niche
- **Reversibility as Appreciating Asset** (`/reversibility-as-appreciating-asset`) — insert when irreversible commitments are in play
- **Legacy Drives Outlast Frame Shifts** (`/legacy-drives-outlast-frame-shifts`) — insert when radical frame-change is claimed; predicts what persists

**For security / threat / adversary decisions:**
- **Autonomic Countermeasures** (`/autonomic-countermeasures`) — insert when friction comes from a large system without a named decision-maker
- **Resimulation as Population Capture** (`/resimulation-as-population-capture`) — insert for any membership-gated system facing AI-era generation asymmetry
- **Lifeboat Under Cover** (`/lifeboat-under-cover`) — insert when inside a binary factional dispute that looks engineered
- **Destructive Sandbox Authentication** (`/destructive-sandbox-authentication`) — insert for untrusted-input processing under high-capability-asymmetry threats
- **Emotion-Conditioning Outlives Memory Veracity** (`/emotion-conditioning-outlives-memory-veracity`) — insert when gut-feelings conflict with content-layer analysis in long-access relationships

**For identity / continuity decisions:**
- **Aggregate State Vector Resurrection** (`/aggregate-state-vector-resurrection`) — insert when reconstructed entities (digital twins, AI personas, knowledge-base resurrection) are relevant
