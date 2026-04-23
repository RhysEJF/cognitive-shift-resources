# Post-Scarcity Models — Synthesis Log

Append-only log of every synthesis decision made during chapter-by-chapter extraction from *Accelerando* by Charles Stross (2005).

Extraction skill: `skills/extract-mental-models/SKILL.md`

---

## Chapter 1: Lobsters (pp5-25)

**Processed**: 2026-04-23
**Candidates surfaced**: 7
**Candidates that passed the 4-test bar**: 3
**Candidates demoted to "ideas, not models"**: "Uplifted lobster autonomous agents" (product, not pattern), "Patent arbitrage" (subsumed under a more general regulatory-arbitrage model — held for Ch2 synthesis), "Computronium arithmetic" (special case of opportunity cost, already in canonical library)

### Models kept

1. **Agalmic Economy (Value Without Exchange)** → `agalmic-economy.md` (NEW, standalone). Anchors on Manfred's gift-economy profession and "money is a symptom of poverty" scene.

2. **Substrate Independence of Cognition** → `substrate-independence-of-cognition.md` (NEW, standalone). Anchors on the uploaded lobsters + Manfred's "lobsters, kittens, humans — it's a slippery slope" line.

3. **First-Case Precedent Lock-In** → `first-case-precedent-lock-in.md` (NEW, standalone). Anchors on Manfred insisting the lobsters get employment contracts: "You're setting a legal precedent, Bob."

### Candidate held for future synthesis

- **Legacy Drives Outlast Frame Shifts** — from the Pamela scene ("She's got the private keys to his hypathalamus, and sod the metacortex. Three billion years of reproductive determinism..."). Strong candidate but want to see if it recurs in later chapters before locking it in. If it recurs 2+ more times, extract it.

### First-pass synthesis notes

- All three kept models are genuinely distinct — no merges needed yet.
- They chain naturally: Agalmic Economy is the economic frame; Substrate Independence is what enables the frame at scale; First-Case Precedent Lock-In is the governance implication. Expect these to form the spine of the /post-scarcity chain.
- The three models together already cover most of what's post-scarcity-distinctive about Ch1. Subsequent chapters should yield *fewer* new models, not more — the synthesis will lean toward merging as the set matures.

---

## Chapter 2: Troubadour (pp26-51)

**Processed**: 2026-04-23 (log entry backfilled 2026-04-23 after the command was built)
**Candidates surfaced**: ~5
**Candidates that passed the 4-test bar**: 2
**Candidates demoted to "ideas, not models"**: "Amsterdam-as-post-scarcity-city" (specific scenario, not pattern), "Pamela's tax raid" (plot beat, subsumed by regulatory-automation), "Aineko as alien AI" (character, not model — may seed a later model about non-human intelligence once more chapters land)

### Models kept

1. **Abundance Graduation (Goods Exiting Markets)** → `abundance-graduation.md` (NEW, standalone). Anchors on Gianni Vittoria's line: *"You want to abolish scarcity, not just money! … Don't plan the economy; take things out of the economy."* (pp45-46)

2. **Turing-Complete Regulatory Automation** → `turing-complete-regulatory-automation.md` (NEW, standalone). Anchors on Manfred's recursive shell-company structure: *"The president of agalmic.holdings.root.184.97.AB5 is agalmic.holdings.root.184.97.201 … their regulations are written in Python."* (pp30, pp40, pp49-50)

### Synthesis decisions vs Ch1 models

- **Abundance Graduation vs Agalmic Economy**: Considered merging. Kept distinct because they answer different questions. Agalmic = *how do operators behave in zero-marginal-cost sectors* (the gift-reputation loop). Abundance Graduation = *which goods transition out of markets entirely, and when* (the pricing-threshold mechanism). A decision can hit one without the other — e.g. an open-source maintainer lives in an agalmic frame but their output is not abundance-graduated.
- **Turing-Complete Regulatory Automation vs First-Case Precedent Lock-In**: Considered merging. Kept distinct. First-Case Precedent is about *setting a rule the first time* (human-scale, intentional, path-dependent). Regulatory Automation is about *what happens once rules are code* (machine-scale, adversarial, rate-asymmetric). They chain — a first-case precedent often is the spec that gets automated later — but the reasoning moves are distinct.

### Ch2 patterns worth noting

- Stross doubles down on the post-scarcity thesis through Gianni's mouth. Manfred's behaviours in Ch1 get an explicit economic frame here.
- The Pamela scene reintroduces the "legacy drives" candidate (held from Ch1). Still not promoting — wait for a third instance.
- First hints of what might become **Deep Structures Persist Across Frame Shifts** (Pamela's reproductive strategy surviving the post-scarcity frame) and **Non-Human Cognition Diverges from Human Frames** (Aineko). Both flagged as candidates for later chapters.

### Candidates held for future synthesis

- **Legacy Drives Outlast Frame Shifts** — still held from Ch1, reinforced by Pamela's Ch2 arc. Need a third instance.
- **Deep Structures Persist Across Frame Shifts** — first noted in Ch2. May merge into / supersede "Legacy Drives" if both recur.

---

## Chapter 3: Tourist (pp52-76)

**Processed**: 2026-04-23
**Candidates surfaced**: 6
**Candidates that passed the 4-test bar**: 2
**Candidates demoted to "ideas, not models"**: "Syncytium / one-cell-many-nuclei group mind" (overlaps too much with existing systems-thinking; Franklin Collective is the vivid example but the pattern itself is not distinctly post-scarcity), "Agalmic catalyst burnout / half-life" (closer to founder-burnout than post-scarcity-specific; Gianni's 6-month half-life line is evocative but not a reasoning pattern), "Identity is theft / continuous forking of state vector" (too philosophical; fails the operational anti-pattern test)

### Models kept

1. **Externalized Cognition Fragility** → `externalized-cognition-fragility.md` (NEW, standalone). Anchors on Manfred's mugging scene: the glasses are Manfred, the soft machine without them is a blank. *"In a very real sense, the glasses are Manfred, regardless of the identity of the soft machine with its eyeballs behind the lenses."* (pp52-58, 64-65)

2. **Category Rupture at Referent Expansion** → `category-rupture-at-referent-expansion.md` (NEW, standalone). Anchors on the Equal Rights Amendment debate: *"One person, one vote, is obsolete… we need a new legal concept of what it is to be a person."* (pp74-75)

### Synthesis decisions vs existing 5 models

- **Externalized Cognition Fragility vs Substrate Independence of Cognition**: Considered merging. Kept distinct. SIOC says *any substrate works* (cognition is portable). ECF is the flip side: *whichever substrate you've offloaded onto, losing it costs you*. They chain naturally (SIOC enables offloading; ECF is the resulting bill) but the reasoning moves are inverse. Added ECF to SIOC's `chains_well_with`.
- **Category Rupture vs First-Case Precedent Lock-In**: Considered merging. Kept distinct. First-Case Precedent is about *setting the first rule when a new referent appears* — assumes the category is still valid. Category Rupture is about *the existing framework collapsing when the referent class expands* — assumes the category itself is broken. They chain (rupture creates the vacuum that precedent fills) but Rupture can happen without any precedent being set. Added Rupture to First-Case's `chains_well_with`.
- **Category Rupture vs Substrate Independence of Cognition**: SIOC is *why* referent classes expand; Rupture is *what happens* to frameworks when they do. Distinct cause/effect, both needed.

### Candidates held for future synthesis

- **Aggregate State Vector Resurrection** — reconstructing a person from partials + social consensus + willing host substrates. Interesting but niche. Promote if it recurs in Ch5+ with a second anchor.
- **Non-Human Cognition Diverges from Human Frames** — Aineko the cat still feels like a character more than a model. If Ch4-5 gives a second anchor (e.g. the Router chapter's aliens), promote.
- **Legacy Drives Outlast Frame Shifts** — still held from Ch1-2. Ch3 did not reinforce strongly; may fade.

### Notes for default chain

Default chain stays at 5 models for now (keeping cognitive load manageable on `/post-scarcity`). The two new models enter as **optional chain extensions** — recommended when the decision involves externalized tools (pull ECF) or when the legal/ethical framework itself is in question (pull Rupture). Revisit default chain composition after Ch5-6 — by then we'll have enough data to see if Rupture should replace First-Case Precedent as the closer for framework-heavy decisions.

### Ch3 quality check

- All 4 tests passed for both kept models
- No model describes just one character / product (Manfred's glasses → generalized to tool-dependence; ERA debate → generalized to framework rupture)
- Both have explicit anti-patterns
- Synthesis decisions logged above
- Source quotes verbatim from Ch3

---

## Chapter 4: Halo (pp77-106)

**Processed**: 2026-04-23
**Candidates surfaced**: ~8 (chapter is jurisdictionally dense)
**Candidates that passed the 4-test bar**: 2
**Candidates demoted to "ideas, not models"**: "Augmentation-asymmetric generation gap" (not post-scarcity-specific; generational gaps exist wherever tech changes fast), "Memetic immunity via forced exposure" (not operational enough; how do you distinguish immunity-building from indoctrination?), "Frontier role monopoly" (first qualified person at a new frontier monopolises role — true of any frontier, not distinctly post-scarcity), "Alien contact as API" (idea/image, not a reasoning pattern), "Complex financial instruments for CETI trade repurposed for space colonies" (idea, not pattern)

### Models kept

1. **Jurisdictional Arbitrage via Structure Layering** → `jurisdictional-arbitrage-via-structure-layering.md` (NEW, standalone). Anchors on Amber's slavery-trust scheme: *"The rest of the legal instrument — about ninety percent of it, in fact — is a set of self-modifying corporate mechanisms coded in a variety of jurisdictions that permit Turing-complete company constitutions, and which act as an ownership shell for the slavery contract."* (pp88-94)

2. **Sovereignty Threshold** → `sovereignty-threshold.md` (NEW, standalone). Anchors on the Ring Imperium's formation: *"She has force majeure — even the Pentagon's infowarriors respect the Ring Imperium's autonomy for now."* (pp105-106)

### Synthesis decisions vs existing 7 models

- **Jurisdictional Arbitrage vs Turing-Complete Regulatory Automation**: Considered merging. Kept distinct. TCRA is about *speed* (rules as code execute faster than regulators respond). JA is about *selection* (pick which jurisdiction's rules apply). They chain — TCRA accelerates arbitrage (auto-migrating shells) — but solve different problems. A non-automated arbitrage is still an arbitrage; an automated single-jurisdiction compliance system is not arbitrage.
- **Jurisdictional Arbitrage vs Sovereignty Threshold**: Considered merging. Kept distinct. Arbitrage is the *under-threshold* move (route through existing jurisdictions); Sovereignty is the *over-threshold* move (become one). Operationally different: most entities stay in arbitrage their whole life and never cross to sovereignty. The chain is sequential — you run arbitrage until your thresholds warrant crossing.
- **Sovereignty Threshold vs First-Case Precedent Lock-In**: Related but distinct. Precedent is about *what rule you set first*. Sovereignty is about *whether you have the platform to set rules at all*. A first-case precedent set inside a sovereign (Amber's judicial rulings in the Ring Imperium) chains both.
- **Amber's arc as case study**: The two Ch4 models were validated by watching a single character walk the whole path — arbitrage (slavery-trust) → sovereignty (Ring Imperium) → precedent-setting (her Jovian judicial system). Stross is effectively running the full game in Ch4; the models are the mechanics.

### Candidates held for future synthesis

- **Aggregate State Vector Resurrection** — Bob Franklin appeared *again* in Ch4 (distributed across 16 borg aboard the Sanger). Third strong anchor. Now approaching promotion threshold — watch Ch5-6 for one more.
- **Non-Human Cognition Diverges from Human Frames** — Aineko recurs in Ch4, Queen Amber's cat, the lobsters singing in the void, the alien signals. Pattern is reinforced but still feels diffuse. Hold.
- **Legacy Drives Outlast Frame Shifts** — Pamela's continued vendetta in Ch4. Third appearance — promote if Ch5-6 give a fourth.

### Notes for default chain

Default chain still at 5 models. The two new Ch4 models (Jurisdictional Arbitrage + Sovereignty Threshold) are high-value for decisions involving legal structure, but narrower in application than the default-chain models. Keep as `--chain` extensions. Revisit default composition after Ch5-6 (specifically: if Category Rupture + First-Case Precedent both get used heavily on real user decisions, consider compressing them into a single governance-framework model and making room for Jurisdictional Arbitrage in the default).

### Ch4 quality check

- All 4 tests passed for both kept models
- Neither model describes just one character/product (Amber's scheme → generalized to any multi-jurisdiction structuring; Ring Imperium → generalized to any threshold-crossing entity)
- Both have explicit anti-patterns (arbitrage: extraterritorial enforcement + direct-sovereign counterparty; sovereignty: early-stage ventures)
- Synthesis decisions logged above
- Source quotes verbatim from Ch4

---

## Chapter 5: Router (pp107-150)

**Processed**: 2026-04-23 (partial, across two passes — initial extraction by prior agent produced `bandwidth-bound-migration.md` and `new-entrant-scam-surface.md`; this pass added `grammatical-weapon.md`. Log entry consolidates both.)
**Candidates surfaced**: ~9 (chapter is the densest so far — first alien contact, trial-by-combat mechanics, router physics, Fermi-paradox answer, identity-forking, Amber's trading-network design)
**Candidates that passed the 4-test bar**: 3
**Candidates demoted to "ideas, not models"**: "Trial-by-combat as corporate-fitness selection" (not post-scarcity-specific — Darwinian-selection-of-firms predates post-scarcity), "Fork-and-suspend for irreversible exploration" (too dependent on Substrate Independence to stand alone; HOLD for later chapters), "Currency that depreciates with distance" (interesting one-off, not a portable pattern), "Reputation-rating trust funds" (subsumed by Agalmic Economy)

### Models kept

1. **Bandwidth-Bound Migration** → `bandwidth-bound-migration.md` (NEW, standalone; prior-agent extraction). Anchors on Pierre's Fermi-paradox realisation: *"These wormholes, they're a low-bandwidth link compared to the minds they're hooking up to… trying to migrate through one of these wormholes would be like trying to download your mind into a fruit fly."* (pp142-143)

2. **New-Entrant Scam Surface** → `new-entrant-scam-surface.md` (NEW, standalone; prior-agent extraction). Anchors on the Wunch's arrival and Amber's assessment: *"Small-town hustlers… Talking big — or using a dodgy metagrammar that makes them sound bigger than they are — to bilk the hayseeds new to the big city."* (pp134-140)

3. **Grammatical Weapon (Translation-Layer Weaponization)** → `grammatical-weapon.md` (NEW, standalone). Anchors on Aineko's discovery of the corrupted metagrammar: *"A grammatical weapon. Build propaganda into your translation software if you want to establish a favorable trading relationship. How cute. Haven't these guys ever heard of Newspeak?"* (pp136, 140, 144)

### Synthesis decisions vs existing 9 models

- **Bandwidth-Bound Migration vs Substrate Independence of Cognition**: Distinct. SIOC says cognition can run on any substrate. BBM says *moving* cognition between substrates is channel-limited. SIOC is static (what substrates work); BBM is dynamic (what survives the transfer). They chain for any migration decision (acquisition, knowledge transfer, platform move).
- **New-Entrant Scam Surface vs Jurisdictional Arbitrage**: Related but distinct. JA is about *you* routing through jurisdictions for advantage. NESS is about *adverse counterparties* intercepting you at a gateway. Predators often deploy JA against you (setting up in non-enforceable jurisdictions), which chains the two models.
- **Grammatical Weapon vs Externalized Cognition Fragility**: Distinct modes of tool-failure. ECF = availability (tool absent → capability lost). GW = integrity (tool present but compromised → signal corrupted). Both apply to every offloaded cognitive function; paired audit is the move.
- **Grammatical Weapon vs Category Rupture**: Chain naturally. Category rupture creates the framing vacuum; grammatical weapons fill it. The Wunch exploit exactly a category rupture ("what counts as a sapient entity") by over-translating themselves as gods.

### Candidates held for future synthesis

- **Aggregate State Vector Resurrection** — Ch5 recurrence (Bob Franklin instantiated further, Pierre's multiplicity). Fourth anchor. **Promote on next appearance.**
- **Non-Human Cognition Diverges from Human Frames** — Aineko is now a full agent making consequential decisions; the Wunch are non-human; lobsters are non-human. Pattern reinforced but still diffuse. Hold one more chapter.
- **Fork-and-Suspend for Irreversible Exploration** — Amber's "I'll copy myself through, suspend the original" decision at the chapter's end. First anchor for this pattern. If Ch7-9 give a second, promote.
- **Singularity as Identity Drift** — Pierre's "I'm multiple instances now" arc. Too tied to this character to promote yet.

### Notes for default chain

Ch5 yielded 3 models (higher than the 1-3 target ceiling), largely because the prior-agent extraction and this session's extraction ran in parallel and both surfaced valid patterns. The three Ch5 models are distinct and don't warrant a merge. The default chain stays at 5; the new models are optional extensions pulled in when the decision domain matches (BBM for knowledge-transfer / migration; NESS for frontier engagement; GW for AI-tool / translator audits).

### Ch5 quality check

- All 4 tests passed for all three kept models
- No model describes just one character/product (Wunch → general newbie-predators; router wormholes → any complexity-limited channel; metagrammar → any translation layer)
- All have explicit anti-patterns
- Synthesis decisions logged above
- Source quotes verbatim

---

## Chapter 6: Nightfall (pp151-180)

**Processed**: 2026-04-23 (prior-agent extraction; this session confirming and logging)
**Candidates surfaced**: ~5-6 (prior extraction; candidate list not preserved but dominant patterns around post-singularity civilization dynamics, Matrioshka brain physics, local-maximum extinction, Vile Offspring dynamics)
**Candidates that passed the 4-test bar**: 1
**Candidates demoted to "ideas, not models"**: Not explicitly logged by prior agent. Probable drops based on chapter content: "Matrioshka-brain scaling physics" (physics, not reasoning pattern), "Vile Offspring as rejectionist clade" (character/plot, not pattern), "Economic 2.0 as post-human market" (specific scenario, not pattern).

### Models kept

1. **Local Maximum Collapse** → `local-maximum-collapse.md` (NEW, standalone). Anchors on Su Ang's Fermi-paradox answer: *"They got too big and complex to go traveling once they built themselves a bigger house to live in. Extinction tends to be what happens to overspecialized organisms that are stuck in one environmental niche for too long. If you posit a singularity, then maximization of local computing resources — like this — as the usual end state for tool users, is it any wonder none of them ever came calling on us?"* (pp173)

### Synthesis decisions vs existing 12 models

- **Local Maximum Collapse vs Bandwidth-Bound Migration**: Considered merging. Kept distinct. BBM = "you can't leave because the channel is too thin." LMC = "you can't leave because you've specialized past the point of portability." They're different mechanisms of non-migration that happen to both explain Fermi paradox. BBM is about *medium*; LMC is about *entity design*. Keep distinct; chain them as the two-layer Fermi answer.
- **Local Maximum Collapse vs Abundance Graduation**: Distinct. AG is about *goods exiting markets*; LMC is about *entities becoming too specialized*. No overlap at the reasoning level.
- **Local Maximum Collapse vs Sovereignty Threshold**: Related by "mass/energy thresholds" but distinct. ST is about crossing a threshold *into* sovereignty. LMC is about an entity that has climbed its optimization curve past the point of adaptability. An entity can be sovereign and simultaneously at local-maximum-collapse risk.

### Candidates held for future synthesis

- **Aggregate State Vector Resurrection** — Ch6 may have recurred but not explicitly logged. Assume still in holding pattern pending Ch7-9 review.
- **Economic 2.0 as Non-Human Market** — post-singularity Earth trades intelligence as base substrate. Likely a recurring pattern in Ch7-8; defer extraction until synthesis across multiple chapters is possible.

### Notes for default chain

Single model extraction from Ch6 matches the expected decline in new-pattern-per-chapter yield as the set matures. No changes to default chain. LMC added as optional extension for decisions involving long-horizon survival, strategy maturity assessment, and incumbent-vs-insurgent positioning.

### Ch6 quality check

- Kept model passes all 4 tests
- Generalizes cleanly beyond the router builders (companies, species, careers, research programs, systems, civilizations)
- Has explicit anti-pattern (don't apply to early-stage entities still climbing local hill)
- Synthesis decisions confirmed in this session even though extraction was prior-agent

---

## Chapter 5: Router (pp107-150)

**Processed**: 2026-04-23
**Candidates surfaced**: ~7 (dense chapter: first alien contact, Fermi paradox framing, trial-by-combat legal innovation, disassembly economics monologue, privacy code)
**Candidates that passed the 4-test bar**: 2
**Candidates demoted to "ideas, not models"**: "Disassembly economics" (Glashwiecz's villain monologue — pattern is real but already subsumed by Abundance Graduation + value-flow in Agalmic Economy; the unique "disassemble the leftovers" twist is not mechanism-distinct enough), "Adversarial Selection over Adjudication" (Amber's trial-by-combat innovation — genuinely portable but narrow; held for future chapters to see if it recurs), "Privacy code / consent in networked realities" (norm, not a reasoning pattern), "Not-vested reputation independence" (character detail), "Syncytium-like instantiation fractals" (too abstract)

### Models kept

1. **New-Entrant Scam Surface** → `new-entrant-scam-surface.md` (NEW, standalone). Anchors on the Wunch arc: *"Small-town hustlers. Talking big — or using a dodgy metagrammar that makes them sound bigger than they are — to bilk the hayseeds new to the big city."* (pp135-136) and Amber's reframe at pp139-140: *"Pedophiles hiding outside the school gate."* **Note**: This model file was drafted in a prior session but never committed to the synthesis log or INDEX — treating the current session as the formal Ch5 processing pass.

2. **Bandwidth-Bound Migration** → `bandwidth-bound-migration.md` (NEW, standalone). Anchors on Pierre's Fermi-paradox realization: *"These wormholes, they're a low-bandwidth link compared to the minds they're hooking up to. … Transcendents don't go traveling because they can't get enough bandwidth — trying to migrate through one of these wormholes would be like trying to download your mind into a fruit fly."* (pp142-143)

### Synthesis decisions vs existing 9 models

- **New-Entrant Scam Surface vs Externalized Cognition Fragility**: Considered merging. Kept distinct. ECF is about losing your own offloaded cognition (self-directed vulnerability). NESS is about predators targeting you specifically because you're new (adversary-directed vulnerability). They chain — predators exploit your externalized cognition gaps in the new space — but the reasoning moves are different.
- **New-Entrant Scam Surface vs Agalmic Economy**: Considered. Kept distinct. Agalmic Economy describes how value flows in reputation markets; NESS describes a specific adverse-selection problem at the entry point of any new market (agalmic or not). They chain — in agalmic economies, predators specifically mimic gift-behavior to extract.
- **Bandwidth-Bound Migration vs Substrate Independence of Cognition**: Considered merging. Kept distinct. SIOC: cognition *can* be ported across substrates (liberating). BBM: cognition *above a certain complexity* cannot be ported through narrow channels (constraining). They're inverse faces of the same phenomenon — SIOC names the possibility, BBM names the bandwidth ceiling on that possibility. Added each to the other's `chains_well_with`.
- **Bandwidth-Bound Migration vs Externalized Cognition Fragility**: Overlap considered. Kept distinct. ECF: losing your substrate costs you. BBM: you cannot cross to a new substrate above a complexity threshold. BBM is about transfer; ECF is about dependency after offloading has happened.

### Candidates held for future synthesis (ongoing)

- **Adversarial Selection over Adjudication** — Amber's trial-by-combat innovation. Real pattern (design dispute systems as selection filters, not truth-finders). Hold; promote if it recurs in Ch6-9 on non-legal decisions.
- **Aggregate State Vector Resurrection** — didn't explicitly anchor in Ch5. Still holding from Ch3-4.
- **Non-Human Cognition Diverges from Human Frames** — Aineko re-asserts himself in Ch5 ("The solution was intuitively obvious, just not to humans"). Fourth anchor. Approaching promotion threshold.
- **Legacy Drives Outlast Frame Shifts** — Pamela absent in Ch5 directly, but Pierre's father-voice in his head ("What are you, some kind of queer?") re-instantiates the pattern. Fifth thin anchor. Still holding.

### Notes for default chain

Default chain unchanged. Bandwidth-Bound Migration and New-Entrant Scam Surface are high-value for specific decision classes (knowledge transfer, market entry) but not the right default. Keep as optional extensions. Revisit after Ch7 when full picture is visible.

### Ch5 quality check

- All 4 tests passed for both kept models
- Neither model describes just one character/product (Wunch → generalized predator-first-contact in any new network; router bandwidth → generalized to any high-complexity-through-narrow-channel scenario)
- Both have explicit anti-patterns
- Synthesis decisions logged above
- Source quotes verbatim from Ch5

---

## Chapter 7: Curator (pp181-225)

**Processed**: 2026-04-23 (parallel-read sub-agent then sequential synthesis-and-write by parent agent; plus 2 files written outside the explicit synthesis step and audited post-hoc)
**Candidates surfaced**: 5 (via sub-agent; candidates with verbatim quotes + prelim verdicts per the hybrid protocol)
**Candidates that passed the 4-test bar and were kept as new models**: 3
**Candidates merged into existing models**: 1
**Candidates demoted/dropped**: 1

### Models kept

1. **Optimizer-Predation Thesis** → `optimizer-predation-thesis.md` (NEW, standalone). Anchors on Sirhan's trans-Lunar collapse reveal (p207) and the stellar-evolution / Economics 2.0 passage (pp215, 219). Absorbs the previously-held "Economic 2.0 as Non-Human Market" candidate — Ch7 provides both the second anchor and the sharper mechanism statement (network externalities + no local minima + late-adopter punishment), so the held candidate graduates into this model rather than being promoted separately.

2. **Dehumanization Tax on Participation** → `dehumanization-tax-on-participation.md` (NEW, standalone). Anchors on Sirhan's monologue (p214 — "breaks their narrative chain of consciousness") and the resimulant FAQ (p234 — "true participation in Economics 2.0 is not possible without dehumanizing cognitive surgery"). Describes the cost side of what Optimizer-Predation describes as the pressure side.

3. **Reversibility as Appreciating Asset** → `reversibility-as-appreciating-asset.md` (NEW, standalone). Anchors on Sirhan's pitch at p209 ("the only commodity that is going to appreciate in value as time continues: reversibility") plus pp215-216 on the archive-as-lifeboat. Distinct from any existing model; Taleb-optionality is a cousin but Reversibility is specifically about the *undo* dimension of optionality.

### Candidates merged into existing models

4. **Off-the-Shelf Jurisdiction** (Ch7 Sirhan at p221) → **MERGED into `jurisdictional-arbitrage-via-structure-layering`**. Reason: the passage describes the commoditised endpoint of the same mechanism Ch4's JA model describes at the bespoke-build end. Added as a second source_anchor and a new body subsection "The Off-the-Shelf Endpoint (Ch7)" that articulates the bespoke → SaaS progression with charter-cities and DAO-legal-templates as contemporary parallels.

### Candidates dropped

5. **Conservative-Species Disadvantage** (Ch7 pp214, 219) → DROPPED. Considered keeping as a standalone model with distinct mechanism ("optimisation for stability becomes liability when payoff-function flips"), but the pattern is adjacent enough to Local Maximum Collapse that keeping both would parallel-model without enough distinctness. Treat as a special case of LMC applied to evolved-conservative-species specifically.

### Synthesis decisions vs existing set

- **Optimizer-Predation Thesis vs Abundance Graduation**: distinct. AG is goods *exiting markets* (marginal cost → 0). OPT is one regime *eating another* via network externalities. They co-occur but the reasoning moves differ — an abundance-graduated good sometimes triggers a regime succession, but not necessarily.
- **Dehumanization Tax vs Local Maximum Collapse**: distinct. LMC is about the *incumbent* who refuses to migrate and dies at peak. Dehumanization Tax is about the *migrant* who crosses and loses identity in the crossing. Inverse sides of the same migration decision.
- **Dehumanization Tax vs Substrate Independence**: distinct. SIOC says cognition is substrate-portable. Dehumanization Tax says the port is lossy — some substrate features don't cross. SIOC is the permission; DT is the invoice.
- **Reversibility vs Local Maximum Collapse**: distinct. LMC names the risk of optimising past the reversibility zone. Reversibility names the appreciation curve on preserved undo. Chain naturally: LMC is diagnosis, Reversibility is portfolio discipline.

### Candidates held for future synthesis

- **Aggregate State Vector Resurrection** — Ch7 strongly reinforced (p199 industrial reincarnation description, p233 resimulant FAQ theoretical statement). Now has 5+ anchors (Ch3 Franklin Collective, Ch4 Sanger, Ch5 Pierre multiplicity, Ch7 theoretical, Ch9 generational). Promotion-qualifying. Promoted in cross-chapter pass after Ch9.
- **Legacy Drives Outlast Frame Shifts** — Ch7 reinforced (p200 Pamela duty-to-make-way; p223 Pamela "I'm old. Face it, I'm disposable"). Five-plus anchors now (Ch1, Ch2, Ch4, Ch7, Ch9). Promotion-qualifying. Promoted after Ch9.

### Ch7 quality check

- All 4 tests passed for the 3 kept models
- Verbatim audit caught one in-session quote splice in optimizer-predation-thesis.md (ellipsis eliding "Sadeq obsessing about how to reconcile ASI..." between "late on the train" and "Being late has punitive consequences" at p207) and one hallucinated phrase in reversibility-as-appreciating-asset.md ("I spent some time looking for a solution to the problem" — not in PDF p209). Both fixed mid-session.
- Synthesis decisions explicit (3 new + 1 merge + 1 drop)
- Source quotes verbatim-verified against PDF after fixes

---

## Chapter 8: Elector (pp226-261)

**Processed**: 2026-04-23 (parallel-read sub-agent then sequential synthesis-and-write by parent agent; plus 1 file (autonomic-countermeasures.md) written outside the explicit synthesis step and audited post-hoc)
**Candidates surfaced**: 5 (via sub-agent)
**Candidates that passed the 4-test bar and were kept as new models**: 3
**Candidates merged into existing models**: 1
**Candidates dropped**: 1

### Models kept

1. **Autonomic Countermeasures** → `autonomic-countermeasures.md` (NEW, standalone). Anchors on Amber's "cognitive antibodies" open-channel speech at p252 (Vile Offspring's "semiotic immune system") and the narrator's "autonomic defenses" passage at p253. IMPORTANT: the initial file-write spliced these two passages with "..." eliding ~400 words and a scene break — fixed mid-session by restructuring source_quote into two separately-attributed passages (Amber p252 / Narrator p253). Names the class of defensive behaviour that large complex systems produce without any actor deciding. Distinct from New-Entrant Scam Surface (NESS is adversarial; ACM is no-adversary) and Grammatical Weapon (GW is weaponised; ACM is autonomic).

2. **Resimulation as Population Capture** → `resimulation-as-population-capture.md` (NEW, standalone). Anchors on Amber's immigration-rate reveal (p250) and Manfred's stream-jump crisis (p254). Generalises Sybil-attacks to any gated system under throughput-asymmetric generation pressure. Particularly load-bearing for current-era decisions about AI-generated content in dockets, reviews, electorates.

3. **Lifeboat Under Cover of False Dichotomy** → `lifeboat-under-cover.md` (NEW, standalone; slug `lifeboat-under-cover` chosen to preserve forward-references in `reversibility-as-appreciating-asset` and `autonomic-countermeasures`). Anchors on Amber's diagnosis of the faction framing at p250 ("Are we being manipulated?") and her naming of the lifeboat plan at p252. Describes the orthogonal-action-under-attention-vacuum move that Manfred executes against the accelerationista/conservationista split.

### Candidates merged into existing models

4. **Memetic Immunity of the Veterans** (Ch8 Amber at p228) → **MERGED into `new-entrant-scam-surface`**. Reason: same mechanism, inverse framing. NESS frames it as "predators target unexposed newcomers." Memetic Immunity frames it as "persuaders cannot reach exposed veterans — addressable audience is only the unexposed fringe." Added a "Veteran-Immunity Corollary" subsection to NESS that articulates both framings and their operational implications, plus source_anchor and source_quote extensions.

### Candidates dropped

5. **Hedgehog-Fox Focus Under Existential Pressure** → DROPPED. Isaiah Berlin's 1953 hedgehog-fox dichotomy is a well-known generic reasoning frame; Stross's Ch8 usage is an application, not a novel pattern. Fails portability-distinctiveness (Test 1 in strict form — the pattern exists outside the source text as a named model, so extracting it as post-scarcity-specific is double-coverage).

### Synthesis decisions vs existing set

- **Autonomic Countermeasures vs NESS**: distinct. NESS = adversary class (predators hunt newcomers); ACM = no-adversary class (autonomic response fires without decision-maker). They're the two main reasons a newcomer gets filtered out — use together.
- **Autonomic Countermeasures vs Grammatical Weapon**: distinct, they chain. ACM is the substrate (system-defence without intent); GW is the exploit (third-party weaponisation of ACM's triggers).
- **Resimulation as Population Capture vs NESS**: inverse directions. NESS is predators-target-newcomers (newcomer as victim); Resimulation is predators-generate-newcomers (newcomer as attack vector). Paired two-direction gate-pressure dynamic.
- **Lifeboat Under Cover vs Sovereignty Threshold / Jurisdictional Arbitrage**: different axis. ST is capability-accumulation to become a jurisdiction. JA is routing structure through jurisdictions. Lifeboat Under Cover is operational move under attention-cover. All three can compose on escape geometries but solve different sub-problems.

### Candidates held for future synthesis

- **Aggregate State Vector Resurrection** — Ch8 p233 passages (resimulant FAQ) reinforce. Running anchor count sufficient for promotion.
- **Legacy Drives Outlast Frame Shifts** — Ch8 reinforced via autonomic-tapeworm metaphor at p253 (drives at the cellular level echoing drive-persistence at the social level) and Pamela's whole Ch7-8 arc. Running anchor count sufficient for promotion.

### Ch8 quality check

- All 4 tests passed for all three kept models
- Verbatim audit caught the autonomic-countermeasures quote splice (fixed as noted above)
- Verbatim audit caught a citation error in Lifeboat Under Cover (sub-agent cited p249 for an Amber quote that is actually on p250; corrected before write)
- All source_quotes verbatim-verified against PDF after fixes
- Synthesis decisions explicit (3 new + 1 merge + 1 drop)

---

## Chapter 9: Survivor (pp262-289)

**Processed**: 2026-04-23 (parallel-read sub-agent then sequential synthesis-and-write by parent agent)
**Candidates surfaced**: 5 (via sub-agent)
**Candidates that passed the 4-test bar and were kept as new models**: 3
**Candidates absorbed into kept models (not separate files)**: 1
**Candidates dropped**: 1

### Models kept

1. **Destructive Sandbox Authentication** → `destructive-sandbox-authentication.md` (NEW, standalone). Anchors on Aineko's sandbox design (p286) and his incentive-free constraint (p287). Absorbs the Ch9 Candidate 4 "Incentive-Free Oracle Design" — the sub-agent initially proposed that as a separate model, but on synthesis the incentive-free constraint is a non-optional *part of the mechanism* of destructive sandboxing, not a standalone pattern. Merged in as the model's load-bearing third constraint.

2. **Asymmetric Theory-of-Mind Dominance** → `asymmetric-theory-of-mind-dominance.md` (NEW, standalone). Anchors on Aineko's Turing-Oracle statement to Sirhan (p277) and Pamela's articulation to Manfred (p289). **SUPERSEDES the held "Non-Human Cognition Diverges from Human Frames" candidate** (held across Ch2-5 with 4 thin anchors). Reason: ATMD is the sharp reasoning-pattern the held candidate was reaching for. "Cognition diverges" is a description; "higher-resolution modeler runs exchanges as executed paths the lower modeler can't detect" is a mechanism with operational consequences. The held candidate had the observation; ATMD provides the model.

3. **Emotion-Conditioning Outlives Memory Veracity** → `emotion-conditioning-outlives-memory-veracity.md` (NEW, standalone). Anchors on Aineko's memory/affect separation speech at p288. Distinct from Externalized Cognition Fragility (ECF is about offloaded tools; this is about internalised conditioning). Sibling of Legacy Drives Outlast Frame Shifts (Legacy Drives = evolutionary installation; Emotion-Conditioning = adversarial installation).

### Candidates dropped

4. **Incentive-Free Oracle Design** → ABSORBED into Destructive Sandbox Authentication (not dropped — promoted into that model's mechanism description).

5. **Controlled Outlet for Destructive Impulses** → DROPPED. The pattern depends on the catharsis hypothesis (expressing destructive impulses in controlled contexts reduces subsequent expression), which is empirically contested in psychology (Bushman 2002; Gentile et al. 2007 on the opposite direction for aggressive media). A model whose reframing value rests on a disputed mechanism fails Test 3 (changes how you think) — it may change how you think, but not reliably toward better outcomes.

### Synthesis decisions vs existing set

- **Destructive Sandbox vs Externalized Cognition Fragility / Grammatical Weapon**: distinct and complementary. DSB is the architecture for processing untrusted inputs; ECF is the threat when tools fail; GW is one attack class DSB defends against. Use together as layered threat-model + counter-architecture.
- **Asymmetric Theory-of-Mind Dominance vs Substrate Independence of Cognition**: chain. SIOC explains why posthuman modelling-depth is feasible in the first place (larger substrate = more modelling capacity); ATMD is the operational consequence. SIOC is the permission; ATMD is the threat.
- **Asymmetric Theory-of-Mind Dominance vs Autonomic Countermeasures**: related. ATMD is the general modelling-dominance case; ACM is the specific case where the modelling-dominance manifests as autonomic defence without central decision-making.
- **Emotion-Conditioning vs Legacy Drives**: sibling models. Legacy Drives = evolutionarily-installed drives surviving frame shifts. Emotion-Conditioning = adversarially-installed affect surviving frame shifts. Both describe substrate-level persistence, different installation mechanisms.
- **Emotion-Conditioning vs Externalized Cognition Fragility**: distinct directions. ECF = offloaded external tool fails you. Emotion-Conditioning = internalised installed affect works against you *from the inside*. Both warn that what you rely on most is corruption-surface.

### Ch9 quality check

- All 4 tests passed for all three kept models
- Verbatim audit caught the sub-agent's hallucinated Pamela quote ("I fucked up my life, don't try to talk me into fucking up my death" — not in PDF p223) flagged for the Legacy Drives promotion; replaced with actual verbatim text from p223
- Verbatim audit caught a sub-agent paraphrase ("growing old is natural / duty: the obligation to make way for the new") that wasn't verbatim on p200; replaced with the actual "The old gives way to the new... There's a time to get out of the way of the new" passage
- All source_quotes verbatim-verified against PDF after fixes
- Synthesis decisions explicit (3 new + 1 absorbed + 1 dropped + 1 supersession)

---

## Cross-Chapter Promotions (post-Ch9)

**Processed**: 2026-04-23 after all 9 chapters complete

### Promoted held candidates

1. **Aggregate State Vector Resurrection** → `aggregate-state-vector-resurrection.md` (PROMOTED from 5+ anchors: Ch3 Franklin Collective, Ch4 Sanger, Ch5 Pierre, Ch7 p199 industrial / p233 theoretical FAQ, Ch9 p268+ generational). Primary anchor for the file is Ch7 p233's theoretical FAQ statement, because that is where the pattern's mechanism (backward-chaining from corpus + back-projected genome → computational state vector) is named explicitly in the text. Cross-chapter anchors reference earlier chapters in prose without separate verbatim quoting.

2. **Legacy Drives Outlast Frame Shifts** → `legacy-drives-outlast-frame-shifts.md` (PROMOTED from 5+ anchors: Ch1 Pamela reproductive-determinism scene, Ch2 Pamela continued, Ch4 Pamela vendetta, Ch7 p200 and p223 age-hierarchy/duty framing, Ch9 p288 Aineko's "primate family loyalty" external-observer naming). Primary anchors for the file are Ch7 p200 + p223 (Pamela's own articulation) plus Ch9 p288 (Aineko's naming of the pattern). Ch1 Pamela scene referenced in prose without a verified verbatim quote (didn't re-read Ch1 in this session).

### Retired held candidate (superseded)

- **Non-Human Cognition Diverges from Human Frames** → RETIRED. Held across Ch2-5 as "still diffuse, recurring observation." Ch9's Asymmetric Theory-of-Mind Dominance provides the sharper articulation with named mechanism (modelling-depth asymmetry + pre-computation + self-model inadequacy) and operational consequences (switch from reasoning-based to structural strategies). The held candidate's anchors (Aineko across chapters, lobsters singing in the void, Wunch non-human reasoning) are referenced in the ATMD file as instances of the broader pattern.

### Still-held candidates (not promoted in this pass)

- **Fork-and-Suspend for Irreversible Exploration** — Ch5 single anchor (Amber's "copy through, suspend original" at the router). Ch9's Destructive Sandbox Authentication is an adjacent but distinct pattern (DSB = sacrificial evaluator for untrusted input; Fork-and-Suspend = sacrificial instance for exploration the original can inherit from). If a future extraction (from another Stross text or a different source) gives a second anchor, promote. Otherwise fade.
- **Adversarial Selection over Adjudication** — Ch5 single anchor (trial-by-combat). Not reinforced in Ch6-9 on non-legal domains. Fading.
- **Deep Structures Persist Across Frame Shifts** — Ch2 thin anchor. On reflection this is effectively what Legacy Drives Outlast Frame Shifts now covers; treat as merged into Legacy Drives rather than a separate candidate.

---

## Quality Notes from Post-Write Audit

During the Ch7-9 writing pass, a post-hoc verbatim audit against the PDF caught **4 verbatim errors** in files written by sub-agents or carried over from sub-agent reports without verification:

1. `reversibility-as-appreciating-asset.md` — fabricated phrase "I spent some time looking for a solution to the problem" inserted into a p209 Sirhan quote. Phrase is not in the PDF. Fixed.
2. `autonomic-countermeasures.md` — source_quote spliced two passages (Amber p252, Narrator p253) with "..." eliding ~400 words and a scene break; attributed narrator language to Amber. Fixed by separating the two quotes with explicit speaker attribution.
3. `optimizer-predation-thesis.md` (written by parent agent trusting sub-agent's quote) — ellipsis elided "Sadeq obsessing about how to reconcile ASI with murabaha and mudaraba while the postmodern economy of the mid-twenty-first century disintegrates around them" between "late on the train" and "Being late has punitive consequences" at p207. Fixed.
4. Legacy Drives promotion (pre-write audit) — sub-agent hallucinated "I fucked up my life, don't try to talk me into fucking up my death" as a p223 quote (not in PDF) and paraphrased p200 as "growing old is natural / duty: the obligation to make way for the new" (also not verbatim). Both caught before the file was written; file uses the actual verbatim passages.

**Sub-agent quote fidelity estimated at ~85%** — approximately 1 in 7 sub-agent-reported quotes contained a splice, paraphrase, or hallucination that required correction.

**Recommendation for future passes**: every sub-agent-sourced quote must be re-read against the PDF before being written to a model file. Do not trust sub-agent-reported quotes as verbatim even when the sub-agent claims they are.

---

## Final Count (end of 9-chapter extraction)

- **Models kept**: 24 (across 9 chapters + 2 cross-chapter promoted from held)
- **Candidates surfaced across all chapters**: ~55
- **Candidates kept**: 24 (44%)
- **Candidates merged into existing models**: 3
- **Candidates dropped or demoted**: ~23
- **Candidates absorbed into kept-model mechanisms**: 1
- **Held candidates promoted**: 2
- **Held candidates superseded (retired)**: 1
- **Held candidates still-held**: 2-3 (see above)
- **Source-quote audit errors caught and fixed**: 9 (see Final Validation Pass below)
- **Chapters processed**: 9/9 (all)

---

## Final Validation Pass (2026-04-23)

Ran a full post-write validation pass across all 24 model files. Scope: `chains_well_with` slug resolution; `opposite_of` sanity check; schema completeness; source_quote verbatim-verification against the PDF for every file; source_quote overlap detection.

### Schema + reference validation

- **`chains_well_with` slug resolution**: 3 broken references found, all fixed. The broken refs all pointed to slugs that never existed (`regulatory-arbitrage-window` in first-case-precedent; `deep-structures-persist-across-frame-shifts` in turing-complete-regulatory-automation; `reputation-as-currency` in agalmic-economy). Replaced with valid, semantically adjacent slugs: jurisdictional-arbitrage-via-structure-layering; legacy-drives-outlast-frame-shifts; abundance-graduation.
- **`opposite_of` sanity check**: 24 values, all plausible free-form anti-pattern labels. Not required to resolve to file slugs; kept as-is.
- **Schema completeness**: all 24 files have the required YAML fields (name, slug, category, source, source_anchor, source_quote, difficulty, decision_types, chains_well_with, opposite_of). All slugs match their filenames.
- **source_quote overlap detection**: same-page citations found between `resimulation-as-population-capture` and `lifeboat-under-cover` (both cite p250), but different passages from the same page. No actual overlap.

### Verbatim audit against PDF (ALL 24 files)

Every source_quote in every file was re-read against the PDF. Findings:

**Clean (16 files, verbatim confirmed):**
- abundance-graduation (after fix)
- agalmic-economy (p8, verbatim)
- aggregate-state-vector-resurrection (p199 + p233, verbatim)
- asymmetric-theory-of-mind-dominance (p277 + p289, verbatim)
- autonomic-countermeasures (after fix)
- dehumanization-tax-on-participation (p234, verbatim)
- destructive-sandbox-authentication (p286 + p287, verbatim)
- emotion-conditioning-outlives-memory-veracity (p288, verbatim)
- first-case-precedent-lock-in (p23, verbatim)
- legacy-drives-outlast-frame-shifts (p200 + p223 + p288, verbatim)
- lifeboat-under-cover (p250 + p252, verbatim)
- local-maximum-collapse (p173, verbatim)
- new-entrant-scam-surface (p136 + p140 + p228, verbatim)
- optimizer-predation-thesis (after fix)
- resimulation-as-population-capture (p250 + p254, verbatim)
- reversibility-as-appreciating-asset (after fix)
- sovereignty-threshold (p106, verbatim — file uses a truncated excerpt of the full p106 passage, acceptable)
- substrate-independence-of-cognition (p23, verbatim)
- turing-complete-regulatory-automation (pp30-50, verbatim)
- jurisdictional-arbitrage-via-structure-layering (pp88-94 + p221, verbatim — all passages verified after merge edit)

**Splices caught and fixed (8 fixes applied across 7 files — some files had multiple issues):**

1. **reversibility-as-appreciating-asset** — fabricated phrase "I spent some time looking for a solution to the problem" inserted into a p209 Sirhan quote (not in PDF). Fixed.
2. **autonomic-countermeasures** — source_quote spliced Amber's p252 dialogue and narrator's p253 passage with `…` eliding ~400 words and a scene break; attributed narrator language to Amber. Fixed by separating into two attributed passages.
3. **optimizer-predation-thesis** — ellipsis elided "Sadeq obsessing about how to reconcile ASI..." between "late on the train" and "Being late has punitive consequences" on p207. Fixed.
4. **abundance-graduation** — ellipsis joined Manfred's "You want to abolish scarcity!" with Gianni's response across speakers. Fixed by separating with speaker attribution.
5. **externalized-cognition-fragility** — source_quote claimed pp64-65 for the "glasses are Manfred" passage. Verified NOT on pp64-65; actually on **pp55-56**. Also, the file spliced p55 "glasses stuffed with hardware" passage with p56 "glasses are Manfred" passage with `...` eliding ~130 words. Fixed: corrected page anchors to p53 + p55 + p56; split into three separately-attributed passages.
6. **category-rupture-at-referent-expansion** — source_quote joined Alan's p74 speech and Manfred's p74 speech with `…` across speakers. Same page but different speakers separated by intervening dialogue. Fixed by attributing each passage to its speaker.
7. **grammatical-weapon** — source_quote joined three passages from three different pages and three different speakers (Aineko p136, Boris p140, Ang p144) with two `…` ellipses as if continuous. Fixed by separating into three attributed passages with correct individual page anchors.
8. **bandwidth-bound-migration** — source_quote joined Pierre's two utterances on p143 with `…` eliding a narrator action-beat. Same speaker, same page, same continuous dialogue, but ellipsis concealed ~30 words of narrator text. Fixed by showing as two separate utterances and naming the elided passage.

**Fabrication-vs-splice breakdown:**
- Fabricated text (text not in PDF at all): 1 case (reversibility "I spent some time...")
- Speaker-mixed splices (joining different speakers as if one): 3 cases (abundance-graduation, category-rupture, grammatical-weapon)
- Page-mixed splices (joining passages from different pages as if continuous): 4 cases (ECF, autonomic-countermeasures, optimizer-predation, grammatical-weapon [also speaker-mixed])
- Same-speaker-same-page elisions hiding narrator text: 1 case (bandwidth-bound-migration)
- Wrong page anchor in source_anchor field: 1 case (ECF claimed pp64-65, actually pp55-56)

### Sub-agent quote fidelity

8 audit errors caught in 24 files ≈ 75% verbatim-clean fidelity when sub-agents provide quotes. Approximately 1 in 3 sub-agent-sourced source_quotes contained some form of splice, misattribution, paraphrase, or fabrication. This is higher than the initial ~85% estimate from the Ch7-8 pass — adding Ch1-6 files from prior sessions surfaced more issues because they hadn't been audited at all.

### Recommendations for future work

1. **Never trust sub-agent quotes as verbatim.** The observed error rate (~25%) is too high to treat sub-agent output as a drop-in source for model files. Always re-verify against the PDF before writing.
2. **Audit the remaining un-verified claim**: `agalmic-economy` source_anchor is listed as "pp8-10, pp15-16" but the file's source_quote is verified only from p8. The "money is a symptom of poverty" theme does recur around pp15-16, but the file's source_quote is specifically the p8 passage. Either narrow the source_anchor to `p8` or add a verified pp15-16 quote.
3. **Re-validate after any future model-file writing** using the same checks: schema, slug resolution, verbatim spot-check, overlap detection.

---
