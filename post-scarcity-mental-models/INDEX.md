---
name: Post-Scarcity Mental Models Index
description: Catalog of 24 mental models extracted from Charles Stross's Accelerando — all 9 chapters processed, plus 2 cross-chapter promoted held candidates
status: extraction-complete (9 of 9 chapters processed; post-write validation pass pending)
last_updated: 2026-04-23
---

# Post-Scarcity Mental Models — Index

Mental models extracted chapter-by-chapter from *Accelerando* by Charles Stross (2005). Each model is a reasoning pattern (not an idea, product, or anecdote) that holds up under the 4-test bar defined in `skills/extract-mental-models/SKILL.md`. Synthesis decisions are logged in `SYNTHESIS-LOG.md`. Source quotes are verbatim from the PDF at `experiences/captures/source-books/accelerando.pdf` — a post-write validation pass is still pending on a subset of files (see HANDOFF.md for audit status).

**Command:** Run `/post-scarcity "your decision here"` to chain these models against a specific situation.

## Status

| Phase | Status |
|---|---|
| Extraction skill (`skills/extract-mental-models/SKILL.md`) | Complete |
| Ch1 Lobsters (pp5-25) | 3 models kept |
| Ch2 Troubadour (pp26-51) | 2 models kept |
| Ch3 Tourist (pp52-76) | 2 models kept |
| Ch4 Halo (pp77-106) | 2 models kept; 1 merged in from Ch7 |
| Ch5 Router (pp107-150) | 3 models kept; 1 merged in from Ch8 |
| Ch6 Nightfall (pp151-180) | 1 model kept |
| Ch7 Curator (pp181-225) | 3 models kept + 1 merged into Ch4 JA |
| Ch8 Elector (pp226-261) | 3 models kept + 1 merged into Ch5 NESS |
| Ch9 Survivor (pp262-289) | 3 models kept |
| Cross-chapter promoted from held candidates | 2 models kept (Aggregate State Vector Resurrection; Legacy Drives Outlast Frame Shifts) |
| `/post-scarcity` command | Live — default chain revised post-Ch7-9 (see `chains/default.md`) |
| Post-write validation pass | Pending (quote-verbatim spot-checks, chains_well_with resolution, source_quote overlap detection) |

## Models (24 kept)

### Ch1 Lobsters

| Model | Slug | Difficulty | Decision Types |
|---|---|---|---|
| Substrate Independence of Cognition | `substrate-independence-of-cognition` | advanced | strategy, product, ethics, labour, investment, hiring, policy |
| Agalmic Economy (Value Without Exchange) | `agalmic-economy` | intermediate | pricing, strategy, distribution, business-model, reputation |
| First-Case Precedent Lock-In | `first-case-precedent-lock-in` | intermediate | strategy, policy, ethics, product, legal, standards |

### Ch2 Troubadour

| Model | Slug | Difficulty | Decision Types |
|---|---|---|---|
| Abundance Graduation (Goods Exiting Markets) | `abundance-graduation` | intermediate | strategy, pricing, investment, policy, product |
| Turing-Complete Regulatory Automation | `turing-complete-regulatory-automation` | advanced | strategy, legal, compliance, policy, investment, risk |

### Ch3 Tourist

| Model | Slug | Difficulty | Decision Types |
|---|---|---|---|
| Externalized Cognition Fragility | `externalized-cognition-fragility` | intermediate | strategy, product, operations, risk, hiring, tooling |
| Category Rupture at Referent Expansion | `category-rupture-at-referent-expansion` | advanced | policy, legal, strategy, product, ethics, standards |

### Ch4 Halo

| Model | Slug | Difficulty | Decision Types |
|---|---|---|---|
| Jurisdictional Arbitrage via Structure Layering | `jurisdictional-arbitrage-via-structure-layering` | advanced | legal, strategy, compliance, tax, incorporation, investment, risk |
| Sovereignty Threshold | `sovereignty-threshold` | advanced | strategy, governance, legal, investment, geopolitics, network-design, risk |

### Ch5 Router

| Model | Slug | Difficulty | Decision Types |
|---|---|---|---|
| New-Entrant Scam Surface | `new-entrant-scam-surface` | intermediate | strategy, product, partnerships, investment, security, hiring, market-entry |
| Bandwidth-Bound Migration | `bandwidth-bound-migration` | advanced | strategy, hiring, operations, knowledge-transfer, expansion, M&A, technology-selection, product |
| Grammatical Weapon (Translation-Layer Weaponization) | `grammatical-weapon` | advanced | strategy, risk, negotiation, security, product, communication, policy |

### Ch6 Nightfall

| Model | Slug | Difficulty | Decision Types |
|---|---|---|---|
| Local Maximum Collapse | `local-maximum-collapse` | advanced | strategy, investment, product, hiring, operations, career, research, technology-selection |

### Ch7 Curator

| Model | Slug | Difficulty | Decision Types |
|---|---|---|---|
| Optimizer-Predation Thesis | `optimizer-predation-thesis` | advanced | strategy, investment, technology-selection, market-entry, product, hiring, policy |
| Dehumanization Tax on Participation | `dehumanization-tax-on-participation` | advanced | strategy, career, technology-selection, product, hiring, organizational, policy |
| Reversibility as Appreciating Asset | `reversibility-as-appreciating-asset` | intermediate | strategy, investment, product, career, technology-selection, organizational, risk |

### Ch8 Elector

| Model | Slug | Difficulty | Decision Types |
|---|---|---|---|
| Autonomic Countermeasures | `autonomic-countermeasures` | advanced | strategy, risk, product, market-entry, policy, communication, security, organizational |
| Resimulation as Population Capture | `resimulation-as-population-capture` | advanced | strategy, policy, security, governance, product, risk, communication, market-entry |
| Lifeboat Under Cover of False Dichotomy | `lifeboat-under-cover` | advanced | strategy, market-entry, risk, communication, policy, governance, negotiation, organizational |

### Ch9 Survivor

| Model | Slug | Difficulty | Decision Types |
|---|---|---|---|
| Destructive Sandbox Authentication | `destructive-sandbox-authentication` | advanced | security, risk, product, strategy, technology-selection, governance, policy |
| Asymmetric Theory-of-Mind Dominance | `asymmetric-theory-of-mind-dominance` | advanced | strategy, negotiation, security, risk, hiring, communication, governance, AI-safety |
| Emotion-Conditioning Outlives Memory Veracity | `emotion-conditioning-outlives-memory-veracity` | intermediate | strategy, product, communication, risk, hiring, organizational, policy, personal |

### Cross-Chapter Promoted from Held Candidates

| Model | Slug | Source Anchors | Difficulty | Decision Types |
|---|---|---|---|---|
| Aggregate State Vector Resurrection | `aggregate-state-vector-resurrection` | Ch3, Ch4, Ch5, Ch7 (theoretical), Ch9 | advanced | strategy, ethics, legal, hiring, product, policy, technology-selection, governance |
| Legacy Drives Outlast Frame Shifts | `legacy-drives-outlast-frame-shifts` | Ch1, Ch2, Ch4, Ch7, Ch9 | intermediate | strategy, hiring, organizational, policy, personal, product, communication |

## Default Chain

See `chains/default.md`. **Revised post-Ch7-9** to reflect the expanded model set. The new default chain is:

1. **Substrate Independence of Cognition** — frame-opener: surface hidden "human-only" assumptions
2. **Agalmic Economy** — value-flow reframe: exchange vs gift / reputation
3. **Optimizer-Predation Thesis** — regime-succession lens: which regime eats which
4. **Asymmetric Theory-of-Mind Dominance** — capability/modelling-asymmetry lens: who is modelling whom
5. **First-Case Precedent Lock-In** — precedent closer: what today's choice locks in

Abundance Graduation and Turing-Complete Regulatory Automation move from the default chain to **optional extensions** — they remain load-bearing in specific domains (pricing for AG; governance/compliance for TCRA) but are narrower than the new additions.

## Merges / Supersedes / Drops

**Merged into existing models:**
- Off-the-Shelf Jurisdiction (Ch7 p221) → merged into `jurisdictional-arbitrage-via-structure-layering` as the commoditised-endpoint anchor
- Memetic Immunity of the Veterans (Ch8 p228) → merged into `new-entrant-scam-surface` as the veteran-immunity corollary
- Incentive-Free Oracle Design (Ch9 p287) → merged into `destructive-sandbox-authentication` as its mechanism justification

**Superseded held candidates (retired):**
- Non-Human Cognition Diverges from Human Frames (held Ch2-5) → superseded by `asymmetric-theory-of-mind-dominance` (Ch9), which sharpens the pattern into a portable reasoning rule with named mechanism. The held candidate had ~4 anchors reaching for an articulation the Ch9 model delivered cleanly.

**Dropped candidates (failed 4-test bar or subsumed):**
- Conservative-Species Disadvantage (Ch7) — subsumed into `local-maximum-collapse` as a special case; would have been parallel with insufficient distinctness
- Hedgehog-Fox Focus Under Existential Pressure (Ch8) — Berlin's 1953 dichotomy is generic, not Stross-distinctive; fails portability-distinctiveness test
- Controlled Outlet for Destructive Impulses (Ch9) — catharsis hypothesis is empirically contested; fails Test 3 (reframing based on unreliable mechanism)
- Disassembly Economics (Ch5) — subsumed into Abundance Graduation + Agalmic Economy value-flow
- Trial-by-Combat as Corporate-Fitness Selection (Ch5) — Darwinian-selection-of-firms predates post-scarcity and is not distinctly Stross
- Currency That Depreciates With Distance (Ch5) — one-off image, not a portable pattern
- Frontier Role Monopoly (Ch4) — generic frontier dynamic, not distinctly post-scarcity
- Amsterdam-as-Post-Scarcity-City (Ch2) — specific scenario, not pattern

## Still-Held Candidates (may promote if reinforced in future work)

- **Fork-and-Suspend for Irreversible Exploration** — Ch5 single anchor (Amber's "copy through, suspend original" at the router), not clearly reinforced in Ch6-9. Fading; may drop on next review.
- **Adversarial Selection over Adjudication** — Ch5 single anchor (Amber's trial-by-combat innovation). Not reinforced in Ch6-9 on non-legal domains. Fading.
- **Deep Structures Persist Across Frame Shifts** — Ch2 thin anchor; likely merged into `legacy-drives-outlast-frame-shifts` at this point (the two were flagged as possible merges during Ch2 extraction).

## How to Add New Models

1. Read the next chunk with `skills/extract-mental-models/SKILL.md` as the extraction methodology
2. Write each new model as `[slug].md` in this directory, using the YAML + 7-section format
3. **Verify every source_quote verbatim against the source PDF** — this session caught 4 hallucinations/splices from sub-agent reports that made it to disk. Do not trust sub-agent quotes; verify every one.
4. Run synthesis against existing models: NEW, MERGED INTO, DECOMPOSED INTO, or SUPERSEDED
5. Log the decision in `SYNTHESIS-LOG.md`
6. Update this INDEX and consider whether the default chain should change
7. Run schema validation: all `chains_well_with` slugs must resolve to existing files; all `opposite_of` values should have intentional semantics
