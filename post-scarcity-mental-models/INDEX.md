---
name: Post-Scarcity Mental Models Index
description: Catalog of mental models extracted from Charles Stross's Accelerando
status: in-progress (6 of 9 chapters extracted)
last_updated: 2026-04-23
---

# Post-Scarcity Mental Models — Index

Mental models extracted chapter-by-chapter from *Accelerando* by Charles Stross (2005). Each model is a reasoning pattern (not an idea or product) that holds up under the 4-test bar defined in `skills/extract-mental-models/SKILL.md`. Synthesis decisions are logged in `SYNTHESIS-LOG.md`.

**Command:** Run `/post-scarcity "your decision here"` to chain these models against a specific situation.

## Status

| Phase | Status |
|---|---|
| Extraction skill (`skills/extract-mental-models/SKILL.md`) | Complete |
| Ch1 Lobsters (pp5-25) | Extracted — 3 models |
| Ch2 Troubadour (pp26-51) | Extracted — 2 models |
| Ch3 Tourist (pp52-76) | Extracted — 2 models |
| Ch4 Halo (pp77-106) | Extracted — 2 models |
| Ch5 Router (pp107-150) | Extracted — 3 models |
| Ch6 Nightfall (pp151-180) | Extracted — 1 model |
| Ch7 Curator (pp181-225) | Pending |
| Ch8 Elector (pp226-261) | Pending |
| Ch9 Survivor (pp262-289) | Pending |
| `/post-scarcity` command | Live (provisional — will improve as more models land) |

## Models (13 kept so far)

| Model | Slug | From | Difficulty | Decision Types |
|---|---|---|---|---|
| Substrate Independence of Cognition | `substrate-independence-of-cognition` | Ch1 Lobsters | advanced | strategy, product, ethics, labour, investment, hiring, policy |
| Agalmic Economy (Value Without Exchange) | `agalmic-economy` | Ch1 Lobsters | intermediate | pricing, strategy, distribution, business-model, reputation |
| First-Case Precedent Lock-In | `first-case-precedent-lock-in` | Ch1 Lobsters | intermediate | strategy, policy, ethics, product, legal, standards |
| Abundance Graduation (Goods Exiting Markets) | `abundance-graduation` | Ch2 Troubadour | intermediate | strategy, pricing, investment, policy, product |
| Turing-Complete Regulatory Automation | `turing-complete-regulatory-automation` | Ch2 Troubadour | advanced | strategy, legal, compliance, policy, investment, risk |
| Externalized Cognition Fragility | `externalized-cognition-fragility` | Ch3 Tourist | intermediate | strategy, product, operations, risk, hiring, tooling |
| Category Rupture at Referent Expansion | `category-rupture-at-referent-expansion` | Ch3 Tourist | advanced | policy, legal, strategy, product, ethics, standards |
| Jurisdictional Arbitrage via Structure Layering | `jurisdictional-arbitrage-via-structure-layering` | Ch4 Halo | advanced | legal, strategy, compliance, tax, incorporation, investment, risk |
| Sovereignty Threshold | `sovereignty-threshold` | Ch4 Halo | advanced | strategy, governance, legal, investment, geopolitics, network-design, risk |
| New-Entrant Scam Surface | `new-entrant-scam-surface` | Ch5 Router | intermediate | strategy, product, partnerships, investment, security, hiring, market-entry |
| Bandwidth-Bound Migration | `bandwidth-bound-migration` | Ch5 Router | advanced | strategy, hiring, operations, knowledge-transfer, expansion, M&A, technology-selection, product |
| Grammatical Weapon (Translation-Layer Weaponization) | `grammatical-weapon` | Ch5 Router | advanced | strategy, risk, negotiation, security, product, communication, policy |
| Local Maximum Collapse | `local-maximum-collapse` | Ch6 Nightfall | advanced | strategy, investment, product, hiring, operations, career, research, technology-selection |

## Default Chain

See `chains/default.md`. Order:

1. Substrate Independence of Cognition — surface hidden "human-only" assumptions
2. Agalmic Economy — reframe value flow (exchange vs gift/reputation)
3. Abundance Graduation — check if the good should exit the market
4. Turing-Complete Regulatory Automation — map rules onto code vs human discretion
5. First-Case Precedent Lock-In — name the precedent today's choice sets

## Candidates Held for Future Synthesis

- **Legacy Drives Outlast Frame Shifts** (Ch1 Pamela scene, weakly reinforced Ch2) — promote if it recurs in 2+ later chapters.
- **Deep Structures Persist Across Frame Shifts** (Ch2) — may merge into / supersede "Legacy Drives" if both recur.
- **Aggregate State Vector Resurrection** (Ch3 Franklin Collective / Bob Franklin instantiation) — reconstructing identity from partials + social consensus. Niche; promote if recurs in Ch5+.
- **Non-Human Cognition Diverges from Human Frames** (Ch2 Aineko, Ch3 Aineko, Ch3 aliens) — still feels character-level. If Ch5 Router aliens give a second anchor, promote.

## How to Add New Models

1. Read the next chapter with `skills/extract-mental-models/SKILL.md` as the extraction methodology
2. Write each new model as `[slug].md` in this directory, using the same YAML + 7-section format as the existing files
3. Run synthesis against existing models: NEW, MERGED INTO, DECOMPOSED INTO, or SUPERSEDED
4. Log the decision in `SYNTHESIS-LOG.md`
5. Update this INDEX and consider whether the default chain should change
