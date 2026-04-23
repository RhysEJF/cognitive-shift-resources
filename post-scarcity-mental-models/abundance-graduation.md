---
name: Abundance Graduation (Goods Exiting Markets)
slug: abundance-graduation
category: post-scarcity
source: "Charles Stross, Accelerando (2005) — Ch2: Troubadour, Gianni Vittoria's library conversation. Echoes of Robert Reich on public goods, Paul Mason's Postcapitalism (2015), and Buckminster Fuller's 'ephemeralization'."
source_anchor: "Ch2: Troubadour, pp45-46"
source_quote: "You want to abolish scarcity, not just money! … Don't plan the economy; take things out of the economy. Do you pay for the air you breathe? Should uploaded minds — who will be the backbone of our economy, by and by — have to pay for processor cycles? No and no."
difficulty: intermediate
decision_types: [strategy, pricing, investment, policy, product]
chains_well_with: [agalmic-economy, substrate-independence-of-cognition, turing-complete-regulatory-automation]
opposite_of: commodification
---

# Abundance Graduation (Goods Exiting Markets)

> When the marginal cost of providing a good drops below the transaction cost of pricing it, the good stops being an economic object and becomes infrastructure. Water, air, elevator rides, web search, and soon AI text generation have all made this transition. The investable question is: what's next?

## What It Is

Most economic thinking starts with the assumption that goods are always and everywhere scarce. Prices exist to allocate a limited supply across competing wants. That framing is so pervasive it's invisible.

But goods regularly *graduate* out of the economy. Once, water was sold by the bucket from door to door; now it comes out of the tap and you don't think about the pricing of each litre. Elevator operators were paid per ride in the 1910s; now elevators are free infrastructure inside buildings. Email (vs telegraph, vs postal mail) graduated mid-2000s. Web search at consumer scale is free. AI-generated text at 2026 price points is functionally infrastructure in many professional workflows.

The mechanism: a good exits the economy when the **cost to *price* each unit exceeds the cost to *provide* the unit**. Billing, metering, payment collection, and enforcement all have non-zero cost. When marginal production cost drops far enough, that fixed transaction cost dominates. At that point, the rational move for suppliers is to bundle the good into some broader fee (rent, subscription, ad-funded free tier) and stop metering. The good becomes infrastructure — not because anyone *gave* it away, but because pricing each unit became uneconomic.

Gianni's insight to Manfred: *don't plan the economy, take things out of the economy*. The central-planning debate assumes goods must remain inside some allocation system. Abundance Graduation is the third option: let goods whose cost curves drop below the pricing threshold exit the system entirely.

This is distinct from the Agalmic Economy model. Agalmic is about *how operators behave* in zero-marginal-cost sectors (they give, they accrue reputation, they capture adjacent scarcities). Abundance Graduation is about *which goods transition out of markets entirely*, and when.

## When to Use It

Use this model when you're:
- Evaluating whether to launch a new metered/priced product whose underlying cost is falling fast (AI tokens, bandwidth, storage, compute)
- Deciding if a current paid product is on the road to graduation (and you should reposition before margins collapse)
- Investing in infrastructure businesses — the question is whether the thing you're selling will be free in 5 years
- Designing public policy: what should be *removed* from markets because it's cheaper to provide universally than to meter?
- Thinking about the next wave of commoditization (if a good is still priced but its cost curve is falling >30% / year, graduation is in sight)

**Don't use it when:** The good has binding non-cost constraints (licensing requirements, regulatory bottlenecks, physical scarcity). Abundance graduation assumes cost is the binding constraint; if it's not, the model misfires. Housing is not going to graduate because land supply is physically fixed.

## The Walkthrough

### Step 1: Measure the cost trajectory
Get the 5-year cost-per-unit trajectory for the good. Is it falling at >30% CAGR? If yes, the good is a graduation candidate. If it's flat or rising, graduation is not imminent and this model doesn't apply.

### Step 2: Estimate the transaction-cost floor
How much does it cost to *price* each unit (metering, billing, payment collection, fraud prevention, customer service about the bill)? This is usually in the 3-15¢ range even for digital goods. When marginal cost approaches that floor, pricing becomes uneconomic.

### Step 3: Identify the bundling wrapper
Graduated goods don't literally become free — they get bundled. Email comes with your ISP; web search is ad-funded; AI text is bundled into SaaS subscriptions. Ask: which adjacent paid offering is the plausible bundling wrapper for this good? That wrapper is where value will concentrate post-graduation.

### Step 4: Decide the strategic move
Three options: (a) **accelerate** graduation yourself if you're positioned to capture the bundling wrapper (Google did this to web search — gave it away, captured the wrapper), (b) **resist** graduation if you're the dominant metered seller (doomed strategy but may work for 3-5 years), (c) **exit** the category if you can't own the wrapper — the metered-sale business is mortal.

### Step 5: Watch for policy-driven graduation
Some goods graduate via policy fiat rather than cost curves — universal basic income schemes, public WiFi, free school meals. These create artificial abundance ahead of the cost curve and can be profitable if you position to capture the bundling wrapper (utility providers benefiting from universal electricity access).

## Example

**Decision:** A SaaS founder charges $29/mo per seat for a productivity tool that heavily uses LLM calls. LLM costs have fallen ~70% year-over-year for two consecutive years. Is this pricing model sustainable?

**Applying Abundance Graduation:**
- Step 1: LLM cost trajectory = 70% CAGR decline. Graduation candidate, yes.
- Step 2: Transaction-cost floor (billing, seat management, fraud check per seat) ≈ $2/mo. Current margin per seat ≈ $27/mo. The *product* can stay metered for a while, but the *LLM input* is about to graduate — no one will charge per-LLM-call in two years.
- Step 3: Bundling wrapper for LLM calls = the productivity tool's UX/workflow. So the founder's value moves *from the LLM output to the workflow that orchestrates it*.
- Step 4: Accelerate the graduation — stop emphasizing "powered by GPT-X"; reposition around the workflow moat (proprietary data, integrations, UX). The LLM becomes free infrastructure; the workflow stays priced. Those who stayed positioned as "a wrapper around an LLM" get eaten by graduation.
- Step 5: Policy risk: if governments push for public AI (national compute), graduation accelerates further. Build workflow moats that survive even if the underlying LLM becomes a public utility.

Verdict: The pricing model is sustainable for 24 months, after which the product must be repositioned as workflow + integrations with LLM as infrastructure. Start that repositioning now.

## Chains Well With

- **Agalmic Economy** (`/agalmic-economy`): Agalmic explains the *gift-and-reputation* dynamic in zero-marginal-cost sectors. Abundance Graduation explains *which sectors become zero-marginal-cost* and when. Chain: check graduation trajectory first, then apply agalmic logic to the operating strategy.
- **Substrate Independence of Cognition** (`/substrate-independence-of-cognition`): Many goods that will graduate are cognitive (translation, drafting, search, tutoring). Substrate-independence is *why* those cost curves are dropping so fast.
- **Turing-Complete Regulatory Automation** (`/turing-complete-regulatory-automation`): Goods that graduate often do so by automating the rules around their production. Permit processing, compliance checking, standardized forms — all candidates for abundance graduation via automation.

## Go Deeper

- Charles Stross, *Accelerando* (2005), Ch2: Troubadour (pp45-46) — Gianni Vittoria's "take things out of the economy" argument
- Paul Mason, *Postcapitalism: A Guide to Our Future* (2015) — contemporary economic treatment of zero-marginal-cost goods
- Jeremy Rifkin, *The Zero Marginal Cost Society* (2014) — direct economic argument for the transition
- Buckminster Fuller, *Operating Manual for Spaceship Earth* (1969) — "ephemeralization" as the original articulation
- Robert Reich on public goods — for policy-driven graduation specifically
- Contemporary signal: track any sector with 40%+ YoY cost decline; it's on the graduation curve
