---
name: Optimizer-Predation Thesis
slug: optimizer-predation-thesis
category: post-scarcity
source: "Charles Stross, Accelerando (2005) — Ch7: Curator. Sirhan's reveal: Economics 2.0 doesn't coexist with Economics 1.0; it eats it. A more-efficient allocation regime consumes the prior one via network externalities — late entrants cannot reach parity. Echoes: Joseph Schumpeter's creative destruction (1942); Clayton Christensen's disruptive innovation (1997); Brian Arthur's work on increasing returns and lock-in (1994); the general class of phase-transition dynamics in economic sociology."
source_anchor: "Ch7: Curator, pp207, 215, 219"
source_quote: "'Collapse of the trans-Lunar economy: Deep in the hot thinking depths of the solar system, vast new intellects come up with a new theory of wealth that optimizes resource allocation better than the previously pervasive Free Market 1.0. With no local minima to hamper them, and no need to spawn and reap start-ups Darwin-style, the companies, group minds, and organizations that adopt the so-called Accelerated Salesman Infrastructure of Economics 2.0 trade optimally with each other. The phase change accelerates as more and more entities join in, leveraging network externalities to overtake the traditional ecosystem. Amber and Sadeq are late on the train, Sadeq obsessing about how to reconcile ASI with murabaha and mudaraba while the postmodern economy of the mid-twenty-first century disintegrates around them. Being late has punitive consequences.'"
difficulty: advanced
decision_types: [strategy, investment, technology-selection, market-entry, product, hiring, policy]
chains_well_with: [dehumanization-tax-on-participation, abundance-graduation, bandwidth-bound-migration, local-maximum-collapse, agalmic-economy]
opposite_of: peaceful-coexistence-of-regimes
---

# Optimizer-Predation Thesis

> Superior allocation regimes don't coexist with their predecessors — they eat them. Network externalities compound structural advantage until laggards become prey, not peers. If a new regime is real, the question isn't whether to adopt but how fast.

## What It Is

A coordination regime — a market, a protocol, a platform, an allocation algorithm — is defined by how efficiently it routes resources between participants. When a *strictly more efficient* regime appears, the intuition is that the two will compete on merit, with some actors choosing the new regime and others sticking with the old. This intuition is wrong. What actually happens is **consumption**, not competition: the new regime accumulates network externalities as adopters join, the per-participant yield rises with network size, and the old regime's participants become systematically disadvantaged in every trade they make across the boundary. Eventually the old regime's participants exist as extraction surfaces for the new one — they aren't competitors, they're prey.

In *Accelerando*, Sirhan names this as the collapse of the trans-Lunar economy. Economics 2.0 doesn't coexist with Economics 1.0; it trades with it on terms so asymmetric that every such trade bleeds capital from the 1.0 side. Because the 2.0 side has no "local minima" (no start-up-and-fail noise to filter innovation), it climbs faster. Every marginal adopter strengthens the 2.0 side. The 1.0 side's only rational move — migrate — requires crossing an entry threshold most can't afford (see Dehumanization Tax on Participation for the cost of crossing).

The mechanism has three parts:

1. **Structural efficiency gap**: the new regime extracts more value per unit of effort. This is a level effect, not an effort effect. No amount of hustle on the old side closes it.
2. **Network externalities**: the new regime's yield scales super-linearly with adopter count. Each adopter makes the next adopter more valuable.
3. **Cross-regime trade asymmetry**: when old and new interact, the higher-efficiency side captures the surplus. Trade between them is not neutral; it's a slow-motion extraction.

The result is a phase transition, not a competition. Old-regime entities experience the shift as mysterious capital erosion, puzzling "unfair" terms, and a narrowing of viable action space — even though no single actor is attacking them. The predation is emergent.

The pattern recurs across domains. VHS eating Betamax wasn't about tape quality — it was about install base externalities. Windows ate OS/2 on network externalities. Amazon ate independent bookstores on fulfillment network externalities. AI-native workflows are currently eating human-native workflows in customer support, legal review, and coding — the efficiency gap plus externalities (shared training data, shared tooling, shared prompt libraries) is producing the same phase transition. Late adopters experience this as "my industry is dying," but no one is killing it; a better optimizer is.

The model does NOT say "always migrate to the new regime." It says: *if the regime is real — structural efficiency gap plus externalities — then either migrate early enough to ride the externality curve up, or accept that you are on the extraction side of every future trade and plan accordingly*. Lateness has "punitive consequences," in Stross's phrase.

## When to Use It

Use this model when you're:
- Evaluating a "new way of doing X" that claims higher efficiency than your incumbent way
- Deciding migration timing for your firm / career / product onto a rising platform or protocol
- Assessing whether to defend an existing moat or abandon it for a new one
- Noticing asymmetric losses in cross-regime interactions you can't explain on merits
- Thinking about market structure changes over long horizons (decades)
- Advising a founder on whether to launch on an emerging or mature stack
- Diagnosing whether you are the predator or the prey in a changing ecosystem

**Don't use it when:** The "new" regime's advantage comes from subsidy (VC-funded below-cost operation), fashion, or regulation rather than structural efficiency — those advantages reverse when the subsidy ends. Also don't use when the efficiency gap is small and the network externality weak; in low-externality domains, regimes can coexist indefinitely.

## The Walkthrough

### Step 1: Confirm the efficiency gap is structural

Is the new regime more efficient because of architecture (level effect) or because of current-period funding/fashion? Architecture-based efficiency persists; funding-based does not. Look for the gap's source: does the new regime's advantage come from fundamentally better matching, lower transaction cost, superior information flow, or removal of a coordination friction? If yes, the gap is structural. If the answer is "it's cheaper right now because someone subsidizes it," you're looking at a temporary regime, not a successor.

### Step 2: Measure the network externality

Count how much a single adopter gains when the Nth other adopter joins. Strong externalities: platforms, protocols, liquidity pools, training data regimes, shared tooling. Weak externalities: solo-practitioner productivity tools, closed vertical systems. Strong externalities create the phase transition; weak externalities leave room for coexistence. Know which you're in.

### Step 3: Locate yourself on the adoption curve

Early, middle, late, or last. Early adopters capture network-externality value as the regime scales. Middle adopters get marginal gains. Late adopters pay the price of transition without capturing the upside. Last adopters become extraction surface. Be honest — most people self-report as middle when they're late.

### Step 4: Choose migrate / hedge / harvest

Given Steps 1-3: (a) **Migrate** if the gap is structural, externality strong, and you're early-to-middle — move fast, accept some transition cost, ride the curve. (b) **Hedge** if uncertain on any dimension — run both regimes in parallel until signals clarify. (c) **Harvest** if you're genuinely late — extract maximum value from the dying regime before extraction reverses and you become the target. Don't defend the dying regime on merit grounds; that's the prey's mistake.

### Step 5: Watch for your own predator

If you *are* the rising regime, you have ~1-2 network-externality cycles before someone builds the next one on top of you. Optimizer-Predation is recursive. Today's eater becomes tomorrow's eaten. Economics 2.0 in *Accelerando* is itself obsolete by Ch8. The winning stance is not "I own the new regime" but "I know where I am on the stack of successive regimes, and I can migrate when mine gets eaten."

## Example

**Decision:** A mid-career software engineer at a bank watches AI-native coding agents take over their team's routine PRs. Leadership says "these are tools, we'll adopt them and continue as before." The engineer is wondering whether to trust that framing or act independently.

**Applying Optimizer-Predation Thesis:**
- **Step 1 — Structural gap?** Yes. AI-native workflows have architectural efficiency advantages (parallelism, recall, pattern coverage) that are not funding-based. A single AI agent can do N PRs in parallel; a human does one sequentially. That gap is permanent and widens with scale.
- **Step 2 — Network externality?** Strong. Shared prompt libraries, shared model improvements, shared tooling ecosystems, and shared training data (every PR merged anywhere improves the next model). The externality compounds.
- **Step 3 — Position on curve?** Middle-to-late. Many firms have already adopted; the engineer's shop is catching up. "Tools we'll adopt" framing is the classic middle-adopter posture — not wrong, but doesn't confer externality-side upside.
- **Step 4 — Migrate / hedge / harvest?** Hedge toward migrate. The engineer should (a) become fluent in the AI-native toolchain in 3-6 months (migrate skill base), (b) re-shape their role toward the functions the AI stack does worst — ambiguity translation, architectural framing, stakeholder negotiation (defensive positioning), (c) treat their current-regime skill (line-by-line coding proficiency) as a depreciating asset.
- **Step 5 — Next regime?** The current AI-native stack is 2 years old. The next one (agents that run full projects autonomously, or embodied coding entities, or something else) will eat the current one. The engineer's defensible asset is not "I know this stack" but "I can detect and migrate to the next stack early."

**Key insight:** The bank's "we'll adopt these as tools" framing treats AI-native coding as a product to buy, not a regime that consumes the old one. The engineer's threat isn't their tools being replaced; it's their *role* becoming extraction surface. The correct move is migration, not adoption.

## Chains Well With

- **Dehumanization Tax on Participation** (`/dehumanization-tax-on-participation`): the flip side. Optimizer-Predation tells you the new regime will consume the old. Dehumanization Tax tells you what it *costs* to enter the new regime. Chain: Optimizer-Predation detects the need to migrate; Dehumanization Tax prices the crossing.
- **Abundance Graduation** (`/abundance-graduation`): related but distinct. Abundance Graduation is goods *exiting markets* entirely (marginal cost → 0). Optimizer-Predation is one regime *eating another*. They can co-occur — an abundance-graduated good is sometimes what triggers the predation phase — but the reasoning moves are different.
- **Bandwidth-Bound Migration** (`/bandwidth-bound-migration`): when you decide to migrate, BBM tells you what complexity can transit to the new regime intact. Migration is not free.
- **Local Maximum Collapse** (`/local-maximum-collapse`): what happens to incumbents that don't migrate. LMC is the outcome, Optimizer-Predation is one of the triggers.
- **Agalmic Economy** (`/agalmic-economy`): the agalmic regime is one specific case of a successor regime (gift-economy as post-market coordination). The Optimizer-Predation pattern predicts how it absorbs market-regime participants at the boundary.

## Go Deeper

- *Accelerando*, Ch7: Curator, pp207 (Economics 2.0 phase change); pp215 (Matrioshka brains bandwidth-limited, get eaten by next-tier optimizer); pp219 (quantized originality as currency).
- Joseph Schumpeter, *Capitalism, Socialism and Democracy* (1942) — creative destruction as the mechanism behind regime succession in capitalism.
- Clayton Christensen, *The Innovator's Dilemma* (1997) — the internal logic of why incumbent firms fail to migrate even when they see the new regime coming.
- W. Brian Arthur, *Increasing Returns and Path Dependence in the Economy* (1994) — the formal economics of network externalities and lock-in.
- Carl Shapiro & Hal Varian, *Information Rules* (1998) — the clearest popular account of how network effects make regimes eat each other in information industries.
- Historical cases: VHS/Betamax; Windows/OS/2; gasoline/EV transition; analog-to-digital photography; human-native to AI-native coding workflows (ongoing).
