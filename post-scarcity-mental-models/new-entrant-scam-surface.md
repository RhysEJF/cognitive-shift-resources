---
name: New-Entrant Scam Surface
slug: new-entrant-scam-surface
category: post-scarcity
source: "Charles Stross, Accelerando (2005) — Ch5: Router. The 'Wunch' turn out to be scammers exploiting newcomers to the galactic network, using a corrupted translation layer to position themselves as gods. Intellectual roots: adverse selection literature (Akerlof, The Market for Lemons, 1970); bazaar scam theory; crypto/Web3 'honeypot contract' literature; Arthur Jensen on adversary distribution in networks."
source_anchor: "Ch5: Router, pp135-136, pp139-140"
source_quote: "'Small-town hustlers,' mutters Amber. 'Talking big — or using a dodgy metagrammar that makes them sound bigger than they are — to bilk the hayseeds new to the big city.' … 'This Wunch, they probably lurk in wait for newbies to exploit. Pedophiles hiding outside the school gate. I don't want to give them that opportunity before we make contact with the real thing!'"
difficulty: intermediate
decision_types: [strategy, product, partnerships, investment, security, hiring, market-entry]
chains_well_with: [category-rupture-at-referent-expansion, externalized-cognition-fragility, jurisdictional-arbitrage-via-structure-layering, agalmic-economy]
opposite_of: legitimate-first-contact-bias
---

# New-Entrant Scam Surface

> The first entities to contact you in a new space are disproportionately predators. Legitimate actors have better things to do than seek out newcomers. Predators specialize in them. The naive inference — "they found me first, they must be important" — is exactly backwards. First contact in any new network correlates negatively with quality.

## What It Is

When you enter a new network, market, platform, or community, you face an adverse-selection problem in who contacts you first. Legitimate participants are busy transacting with other legitimate participants — they have existing relationships, established counterparties, and functioning markets. They don't prioritize greeting every newcomer. Predators, by contrast, have every reason to monitor for new entrants: newcomers are uniquely exploitable because they lack the context, reputation, and local knowledge that would let them evaluate a pitch.

The result is a skewed first-contact distribution. The population that reaches out to a newcomer is heavily over-weighted toward scammers, con-artists, bridge-to-nowhere vendors, and opportunists. In *Accelerando*, Amber's expedition reaches a galactic-scale packet-switching network and the first civilization to greet them is the Wunch — a coalition of scavengers wearing lobster translation bodies, using a corrupted grammar to make themselves look god-like, offering worthless "trade" in exchange for proprietary information. They *specialize* in newcomers. The network's real inhabitants — transcendent civilizations operating at orders of magnitude more bandwidth — don't bother making first contact; the Wunch do.

The mechanism is pure economics. For legitimate actors, contacting newcomers has high search cost and low return (newcomers have nothing yet). For predators, contacting newcomers has the reverse — low search cost (there's a stream of them), high return (their naivety is exploitable, their resources are unprotected). At equilibrium, the first-contact population is disproportionately predator. The more novel the space, the more skewed.

Post-scarcity amplifies this: as new networks, markets, and categories emerge faster (new AI capabilities, new crypto protocols, new jurisdictions, new hardware platforms, new social apps), the "newcomer" window grows as a share of the total surface. And because predators can now scale — a single scam operation can automatically target every new entrant across a class of platforms — the predator-first-contact ratio goes up, not down.

The model does NOT say all first contact is predatory, or that you should refuse all contact. It says the *base rate* is predator-heavy, and your Bayesian prior should be calibrated accordingly. A sincere-seeming first contact should raise your suspicion, not lower it.

## When to Use It

Use this model when you're:
- Entering a new market, platform, or ecosystem and evaluating unsolicited offers, partnerships, or advisors
- Onboarding a new employee, investor, founder — and noticing which people go out of their way to "welcome" them
- Evaluating inbound pitches in any novel category (new crypto chain, new AI platform, new jurisdiction, new community)
- Building anti-abuse systems for a platform that has new-user flows — predators aggregate there
- Designing a protocol or network where new nodes will appear and need first contacts — you want to minimize the share captured by predators
- Mentoring someone entering a field for the first time: the first "helpful" person they meet deserves extra scrutiny, not less

**Don't use it when:** The space is mature, first-contact bias has washed out, and the incentive structure no longer favours predator specialization. Don't apply the model to decades-old communities with stable norms and high-context participants — there, first contact is basically random.

## The Walkthrough

### Step 1: Is the space genuinely new to you?

"New" means you lack local context to judge quality. This is a *relative* state — new to you, not new in absolute terms. Crypto is 15+ years old but new to someone who joined last week. The question is your prior uncertainty, not the space's age.

If new: proceed. If mature-to-you: the model doesn't apply with force.

### Step 2: Audit who's contacting you

List every entity reaching out or offering something in the new space. For each: who are they, what are they offering, why *you* specifically, and — critically — what do they ask for in return? Pay extra attention to:
- **Asymmetric exchanges**: they offer something "free" in return for something concrete (information, access, endorsement)
- **Urgency pressure**: time-limited, "act now", "before X happens"
- **Unearned authority claims**: language positioning them as insiders, authorities, veterans (cf. the Wunch's inflated "god" translation)
- **Outsized attention to you**: effortful first contact from a supposedly-important entity to an obvious newcomer — backwards from normal equilibrium

### Step 3: Invert the Bayesian prior

Before evaluating a specific first contact, state your prior: "In a genuinely new-to-me space, the base rate for first-contacting entities is predator-weighted." Any specific contact needs to beat that prior with concrete evidence — not just "seems nice" or "said something smart".

Evidence that beats the prior:
- Verifiable reputation from outside the new space (someone you already trust vouches)
- Self-interest alignment (they benefit only if you succeed, and this is structurally enforced)
- Low-effort contact consistent with legitimate participants being busy (not effortful courtship)
- Willingness to defer the relationship ("no rush, message me when you've looked around")

### Step 4: Actively seek non-first-contact sources

Since first-contact is skewed, the rational move is to deliberately sample beyond it. Find participants who didn't reach out to you. Ask other newcomers what their first-contact population looked like. Look for entities that are clearly transacting with each other but ignoring you — they're closer to the legitimate-participant distribution. The Wunch were loud; the real network's inhabitants were silent.

## Example

**Decision:** A founder launches a new AI product. Within a week of the launch, she receives a flood of inbound: advisors offering mentorship, VCs requesting meetings, a "strategic partner" offering channel access, a press firm offering coverage. All claim urgency. Which should she engage with?

**Applying New-Entrant Scam Surface:**
- **Step 1 — Genuinely new space?** YES. She's launching into a category she hasn't operated in before. Her prior context is low.
- **Step 2 — Audit inbound:**
  - Advisors → 8 inbound, most asking for 1-2% equity for "advising", typical advisor scam profile
  - VCs → 3 from known funds (base rate: reasonable), 7 from unknown "family offices" or "angel syndicates" (base rate: highly suspect — legit money doesn't cold-inbound obscure launches)
  - Strategic partner → 1 offering channel access in return for exclusive data rights; asymmetric exchange, urgency-pressured
  - Press firm → offering coverage in exchange for $15k upfront fee; classic pay-for-play
- **Step 3 — Bayesian prior:** Predator-heavy. Default to suspicion. Specific contacts that clear the prior: the 3 VCs from known funds (verifiable reputation), one advisor that was introduced by a past founder who vouches personally (outside-space vouching).
- **Step 4 — Non-first-contact sources:** She reaches out to three AI founders who are 2 years ahead of her, none of whom contacted her; they share their own first-contact horror stories and name specific scammers. She also identifies two legitimate channel partners by looking at who the successful AI products are already partnering with (not who's inbounding to newbies).

**Key insight:** Of the ~19 inbound first contacts, she engages with 4 (the known-fund VCs + the introduced advisor), ignores or defers the rest, and proactively seeks the non-inbound population. Estimated time saved: ~30 hours of meetings. Estimated predator damage avoided: unknown but non-zero — the "strategic partner" who wanted exclusive data turned out to be a known extractive operator in the space.

## Chains Well With

- **Category Rupture at Referent Expansion** (`/category-rupture-at-referent-expansion`): New spaces often have ruptured categories — no established rules, no clear definitions. The combination (new space + ruptured framework) is exactly where New-Entrant Scam Surface is worst. Apply both.
- **Externalized Cognition Fragility** (`/externalized-cognition-fragility`): New-entrant predators often exploit your *lack of local cognitive infrastructure* — you don't have the tools, reputation systems, or filtering mechanisms yet. Offloading your evaluation to someone who "seems helpful" is how they win.
- **Jurisdictional Arbitrage via Structure Layering** (`/jurisdictional-arbitrage-via-structure-layering`): Predators often structure themselves to arbitrage between your jurisdiction (where you might have recourse) and a jurisdiction where you don't. When a first-contact entity's legal domicile looks optimized for non-enforcement, apply extra scrutiny.
- **Agalmic Economy** (`/agalmic-economy`): In reputation-driven economies, predators often mimic the agalmic pattern (give first, accrue reputation). The difference: real agalmic actors give things that are genuinely costly-to-them but near-free-to-you. Predators give low-value things that position them for extraction.

## Go Deeper

- *Accelerando*, Ch5: Router — the Wunch's arrival at pp134-136, Amber's analysis at pp139-140.
- George Akerlof, "The Market for Lemons" (1970) — the foundational adverse-selection paper. New-Entrant Scam Surface is the new-entrant corollary.
- Crypto/Web3 literature on honeypot contracts, phishing-as-a-service, and new-token-launch predation — 2021-2026 is a reference library of this pattern at industrial scale.
- Psychology literature on "love-bombing" and high-control-group recruitment — the same structural pattern as predator-first-contact: intense effort from people who shouldn't have time for you.
- Immigration and scam literature — new immigrants are disproportionately targeted by "helpful" intermediaries (immigration consultants, remittance schemes, housing scams). Same pattern.
- Empirical: Ad-spend analysis of scam platforms consistently shows they concentrate budget on "newcomer" keywords ("how to", "getting started", "beginner's guide") — because that's where the predator ROI is highest.
