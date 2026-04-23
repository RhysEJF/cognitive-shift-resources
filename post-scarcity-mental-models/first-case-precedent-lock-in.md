---
name: First-Case Precedent Lock-In
slug: first-case-precedent-lock-in
category: post-scarcity
source: "Charles Stross, Accelerando (2005) — Ch1: Lobsters. Real-world roots in common-law precedent theory and path-dependency economics (Paul David, W. Brian Arthur)."
source_anchor: "Ch1: Lobsters, pp22-23"
source_quote: "It's not so much that they should be treated as human-equivalent, as that, if they aren't treated as people, it's quite possible that other uploaded beings won't be treated as people either. You're setting a legal precedent, Bob. I know of six other companies doing uploading work right now, and not one of 'em's thinking about the legal status of the uploaded. If you don't start thinking about it now, where are you going to be in three to five years' time?"
difficulty: intermediate
decision_types: [strategy, policy, ethics, product, legal, standards]
chains_well_with: [substrate-independence-of-cognition, agalmic-economy, regulatory-arbitrage-window]
opposite_of: wait-and-see
---

# First-Case Precedent Lock-In

> In a nascent category, the first edge-case decision becomes the policy default for everyone who comes after. Treat your first hard case as policy-making, not as a one-off, because the people watching will copy your choice whether or not it deserved copying.

## What It Is

When a new category opens up — a new technology, a new market, a new form of contract — there is a window during which no one knows the answers to the obvious hard questions. What rights do they have? What gets taxed and how? Who is liable? What counts as "standard"? During that window, decisions are reversible in principle but almost never in practice. Because:

1. The first decision creates a **Schelling point**: a focal norm that everyone coordinates on because coordination is more valuable than optimization.
2. Later entrants copy the first decision to reduce their own decision cost ("well, X did it this way, so it's defensible").
3. Once enough entrants have copied, the decision calcifies into the de-facto standard, then into regulation, then into assumption.

In *Accelerando*, Manfred insists Bob Franklin give the uploaded lobsters employment contracts. Not because he's certain they're sentient. Because *six other companies are doing uploading work right now*. The first contract-or-no-contract decision on lobsters will bind the decision on uploaded cats, which will bind the decision on uploaded humans three to five years later. The lobsters are the canary — their treatment is the precedent.

You see the same pattern everywhere a new category is forming:
- The first terms-of-service for user-generated content platforms (2000-2005) set the norms that still bind Meta and TikTok.
- The first crypto tax treatment in each jurisdiction (2015-2020) is now the model every later token class gets slotted into.
- The first AI-generated copyright case (Zarya of the Dawn, 2023 US Copyright Office) is being cited in every subsequent AI/IP dispute.
- The first "agent memory" product shipped with persistent user history shaped what users now *expect* from every agent.

The mechanism: humans satisfice on decisions, especially novel ones. When a category is new, most actors are looking around for a precedent so they don't have to reason from first principles. Whoever moves first gets disproportionate influence on the norm, even if the first mover was wrong.

## When to Use It

Use this model when you're:
- Operating in a genuinely new category where no legal/ethical/commercial norm has settled yet
- Making a one-off decision that will be visible to competitors, regulators, or press
- Asked for a concession on a weird edge case ("we just have this one customer asking for X")
- Considering whether to publish vs stay quiet about how you've handled a sensitive new issue
- Negotiating terms with an early customer in a category that will have many future customers

**Don't use it when:** The category is already mature and has settled norms. In mature categories, first-case analysis is a distraction — the norm is the constraint, and the cost of fighting it exceeds the cost of following it. Signs you're in a mature category: lawyers can tell you the answer, competitors all do the same thing, regulators have written rules.

## The Walkthrough

### Step 1: Name the novel category
State explicitly: "This is a question about [category], which is new enough that [specific norm] hasn't settled yet." If you can't say what's new, you may actually be in a mature category and this model doesn't apply.

### Step 2: List the downstream cases your decision will bind
Who else is making similar decisions right now? What bigger decisions (on more consequential cases) are 6-36 months downstream? Write 3-5 specific downstream cases. If the list is short, precedent pressure is weak; if long, it's dominant.

### Step 3: Ask "what norm would I want the downstream cases to inherit?"
Don't ask "what's right for this specific case?" Ask: "If every future case of this type inherited my decision, which decision would produce the best aggregate outcome?" You are not deciding this case; you are legislating.

### Step 4: Pay the upfront cost to lock in the right norm
The correct precedent almost always costs more than the expedient one in the short term. Manfred paying the lobsters wages is more expensive than not paying them. The expenditure is a **norm investment**, amortized across all the future cases your decision will shape. Budget for it explicitly — the case you're deciding is, on average, the cheapest point in the curve to set the norm.

### Step 5: Publicize the decision appropriately
A precedent that no one knows about has no binding force. Once you've made the decision, ensure competitors and press know it was deliberate and principled (not an accident). Press release, open letter, industry-body submission, or a well-placed interview all work. Silent precedents don't lock in.

## Example

**Decision:** An AI agent startup is building a product where users can save long-running agent sessions and return to them later. One early enterprise customer asks: "Can our agent remember our employees' personal preferences across sessions and roll them into aggregate reports for HR?"

**Applying First-Case Precedent Lock-In:**
- Step 1: The novel category is "what rights of inspection/aggregation do employers have over an AI agent's records of its interactions with individual employees?" This norm has not settled.
- Step 2: Downstream cases: (a) HR wanting to grade employees by their "agent interaction patterns", (b) marketing wanting to personalize employer-supplied agents with customer data, (c) insurers asking for aggregate agent data for risk scoring, (d) regulators demanding audit access, (e) governments requesting the same under national-security letters. The list is long — precedent pressure is dominant.
- Step 3: What norm would I want downstream? Likely: the agent belongs to the user; employers can audit it only with consent or narrow lawful basis; aggregation requires anonymization before it crosses organizational boundaries.
- Step 4: Cost: say no to this enterprise customer's request. Offer anonymized aggregate patterns (no individual data) or user-consented export. Lose some revenue short-term. The norm investment is the price.
- Step 5: Publish. Write a blog post: "Why our agents don't roll up into HR reports." Announce the policy at the next industry conference. Submit to the ICO or equivalent. Make the precedent sticky.

Verdict: Decline the request in its original form. Pay the short-term revenue cost. Broadcast the decision. Downstream cases now have a reference norm they have to either follow or actively fight.

## Chains Well With

- **Substrate Independence of Cognition** (`/substrate-independence-of-cognition`): Substrate-independence creates new categories of cognition without rights precedents. First-case locks in those precedents. Manfred's lobster-contract move is the direct chain.
- **Agalmic Economy** (`/agalmic-economy`): When you give something away early in a nascent category, you are simultaneously shaping the category's norms. Agalmic operators use gifts as precedent-setters, not just as generosity.
- **Second-Order Thinking** (existing `/second-order` in the canonical library): First-case lock-in is second-order thinking applied specifically to norm formation. Use /second-order to trace the downstream effects that give this model its teeth.

## Go Deeper

- Charles Stross, *Accelerando* (2005), Ch1: Lobsters (pp22-23) — the employment-contract-for-lobsters scene is the canonical example
- Paul David, "Clio and the Economics of QWERTY" (1985) — classic paper on path-dependency and first-mover lock-in
- W. Brian Arthur, *Increasing Returns and Path Dependence in the Economy* (1994) — the formal economics of lock-in
- Lawrence Lessig, *Code: And Other Laws of Cyberspace* (1999/2006) — on how early technical and legal decisions in cyberspace shaped later norms
- Julia Angwin, *Dragnet Nation* (2014) — case studies of how first-case privacy decisions by early tech companies bound the whole industry
- Contemporary: the Zarya of the Dawn copyright ruling (2023), the first case on AI-generated image authorship, now cited universally
