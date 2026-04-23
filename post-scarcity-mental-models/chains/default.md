---
name: Post-Scarcity Default Chain
slug: post-scarcity-default
description: The default chain for /post-scarcity — reframes a decision through the five post-scarcity models extracted from Accelerando
models: [substrate-independence-of-cognition, agalmic-economy, abundance-graduation, turing-complete-regulatory-automation, first-case-precedent-lock-in]
decision_type: post-scarcity
estimated_time: 20-30 minutes
status: provisional
coverage: 3 of 9 Accelerando chapters extracted (Lobsters, Troubadour, Tourist) — chain will be re-evaluated as more models are added
---

# Post-Scarcity Default Chain

> For decisions where the usual assumptions (scarcity, priced exchange, human labour, human regulators, gradual change) may not hold. Run any strategic, pricing, product, policy, or labour decision through this chain to see what a post-scarcity lens surfaces.

## When to Use This Chain

- You're pricing something whose marginal cost is near zero (software, AI outputs, content, data)
- You're deciding whether something should be a paid product, free, or exit the market entirely
- You're making a call that involves AI agents, uploaded minds, or any non-human cognition
- You're setting policy, terms, or a "first of its kind" contract — and the precedent will stick
- You're designing coordination / governance where the rule-enforcers could be software rather than humans
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

### 3. Abundance Graduation (Goods Exiting Markets)
**File:** `memory/frameworks/post-scarcity/abundance-graduation.md`

Then ask: should this thing *be in a market at all*? Some goods stop being traded when they become cheap enough (air, tap water, roads). Is yours one of them? If yes, the strategic question flips from "how do I charge?" to "how do I be the one who provides it as infrastructure?"

**Pass forward:** whether the underlying good is heading toward graduation, and on what timeline.

### 4. Turing-Complete Regulatory Automation
**File:** `memory/frameworks/post-scarcity/turing-complete-regulatory-automation.md`

Then ask: which of the rules, contracts, or coordination mechanisms in this decision could be implemented as code rather than human discretion? What becomes possible if the rules run at machine speed and can recursively compose? What risks does that create?

**Pass forward:** a map of rules → automatable vs human-must-stay-in-loop.

### 5. First-Case Precedent Lock-In
**File:** `memory/frameworks/post-scarcity/first-case-precedent-lock-in.md`

End here. Ask: is this a first-of-its-kind decision whose pattern will be copied? If so, what precedent does today's choice lock in, and is that the precedent you want industry / regulators / your future self to inherit? If the answer is unclear, slow the decision down and widen the stakeholder set.

**Pass forward:** the precedent you are knowingly setting (or inheriting).

## Decision Brief Template

- **The decision:** [What you're choosing]
- **Substrate assumptions surfaced:** [What broke when you questioned "human-only"]
- **Value flow:** [Priced exchange / gift-reputation / hybrid — and why]
- **Abundance graduation check:** [Stay in market / exit to infrastructure / undecided]
- **Rules automatable:** [Which coordination moves from human discretion to code]
- **Precedent being set:** [The pattern today's choice locks in]
- **Recommendation:** [One or two sentences, with confidence: high / medium / low]
- **Next steps:** [2-3 concrete actions]

## Notes on Using a Subset

If the decision clearly doesn't touch cognition/labour (skip model 1), isn't about pricing (skip model 2), or isn't precedent-setting (skip model 5), drop those models and note the skip in the brief. A shorter, relevant chain beats a longer, forced one.

## Optional Extensions (as more chapters land)

Two Ch3 models sit outside the default chain but are worth pulling in when relevant. Use `--chain` or just insert them situationally:

- **Externalized Cognition Fragility** (`externalized-cognition-fragility.md`) — add when the decision involves AI tools, external memory, or any cognitive offload. Best inserted after Substrate Independence (it's the flip side). Ask: if the tool fails, what stops?
- **Category Rupture at Referent Expansion** (`category-rupture-at-referent-expansion.md`) — add when the decision involves legal, ethical, or regulatory frameworks facing new entity classes (AI agents, uploads, group minds, digital goods). Best inserted before First-Case Precedent. Ask: is the framework broken, or just lagging?

Default chain composition will be revisited after Ch5-6 extraction, when we have more data on which models bear weight across real user decisions.
