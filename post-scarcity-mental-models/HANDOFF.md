---
name: Accelerando Extraction Hand-Off Summary
description: Final state of the post-scarcity mental models extraction from Charles Stross's Accelerando after all 9 chapters processed and full validation pass completed
status: extraction-complete; validation-pass-complete
date: 2026-04-23
---

# Hand-Off Summary — Post-Scarcity Extraction Complete

## What Was Done

Extracted mental models from all 9 chapters of *Accelerando* by Charles Stross (2005), plus cross-chapter promotion of 2 held candidates that earned their anchors during the extraction process. Output is a set of 24 model files in `memory/frameworks/post-scarcity/`, each matching the canonical Mental Models OS format (YAML frontmatter + 7-section body), plus an INDEX, a detailed SYNTHESIS-LOG, and a revised default chain for the `/post-scarcity` command.

## Final State

### Counts

| Dimension | Count |
|---|---|
| Chapters processed | 9 of 9 |
| Models kept as standalone files | 24 |
| Candidates surfaced across extraction | ~55 |
| Candidates merged into existing models | 3 |
| Candidates absorbed into kept-model mechanisms | 1 |
| Candidates dropped (failed 4-test bar, subsumed, or contested mechanism) | ~23 |
| Held candidates promoted | 2 |
| Held candidates superseded (retired) | 1 |
| Held candidates still-held | 2-3 |
| Source-quote audit errors caught and fixed | 4 |

### Models by chapter

- **Ch1 Lobsters**: 3 (Substrate Independence of Cognition; Agalmic Economy; First-Case Precedent Lock-In)
- **Ch2 Troubadour**: 2 (Abundance Graduation; Turing-Complete Regulatory Automation)
- **Ch3 Tourist**: 2 (Externalized Cognition Fragility; Category Rupture at Referent Expansion)
- **Ch4 Halo**: 2 (Jurisdictional Arbitrage via Structure Layering — now with Ch7 off-the-shelf endpoint merge; Sovereignty Threshold)
- **Ch5 Router**: 3 (New-Entrant Scam Surface — now with Ch8 veteran-immunity corollary merge; Bandwidth-Bound Migration; Grammatical Weapon)
- **Ch6 Nightfall**: 1 (Local Maximum Collapse)
- **Ch7 Curator**: 3 (Optimizer-Predation Thesis; Dehumanization Tax on Participation; Reversibility as Appreciating Asset)
- **Ch8 Elector**: 3 (Autonomic Countermeasures; Resimulation as Population Capture; Lifeboat Under Cover of False Dichotomy)
- **Ch9 Survivor**: 3 (Destructive Sandbox Authentication; Asymmetric Theory-of-Mind Dominance; Emotion-Conditioning Outlives Memory Veracity)
- **Cross-chapter promoted**: 2 (Aggregate State Vector Resurrection; Legacy Drives Outlast Frame Shifts)

## Revised Default Chain

The default chain for `/post-scarcity` was revised after the full extraction to reflect which models are most load-bearing across the book. New chain:

1. Substrate Independence of Cognition (frame-opener)
2. Agalmic Economy (value-flow reframe)
3. Optimizer-Predation Thesis (regime-succession lens — NEW)
4. Asymmetric Theory-of-Mind Dominance (capability-asymmetry lens — NEW)
5. First-Case Precedent Lock-In (precedent closer)

Abundance Graduation and Turing-Complete Regulatory Automation were demoted from the default chain to optional extensions. They remain important for their respective domains (pricing; compliance) but are narrower than the two new defaults. See `chains/default.md` for the full rationale.

## Known Quality Issues

### Source-quote audit (completed in full validation pass)

**Total errors caught and fixed: 8 splices + 3 broken chains_well_with references.** See SYNTHESIS-LOG.md "Final Validation Pass" section for the complete per-file breakdown.

High-level summary:

- **1 fabrication**: `reversibility-as-appreciating-asset.md` had a fabricated phrase inserted that was not in the PDF
- **3 speaker-mixed splices**: abundance-graduation, category-rupture, grammatical-weapon (each joined passages from different speakers with `…` as if continuous)
- **4 page-mixed splices**: externalized-cognition-fragility, autonomic-countermeasures, optimizer-predation-thesis, grammatical-weapon (joined passages from different pages as if continuous)
- **1 same-page same-speaker elision**: bandwidth-bound-migration (hid ~30 words of narrator action-beat between two Pierre utterances)
- **1 wrong-page anchor**: externalized-cognition-fragility claimed pp64-65 but actual pages were pp55-56

All 8 splice issues fixed. All fixes use the pattern: separately-attributed passages with speaker labels and explicit page numbers, plus a [Validation note] explaining what the original splice was.

### Sub-agent quote fidelity (measured)

Final measured error rate: 8 audit errors in 24 files ≈ 25% of sub-agent-sourced source_quotes had some issue (splice, misattribution, paraphrase, or fabrication). Higher than the initial ~15% estimate from the Ch7-8 pass alone — the Ch1-6 files (prior sessions, never audited) had more latent issues than expected.

**Recommendation for any future Mental Models OS work**: treat sub-agent-supplied quotes as suspect until PDF-verified. Build the PDF-verification step into the extraction workflow, not into a separate post-hoc audit.

### Validation pass complete

Full pass completed 2026-04-23. All checks cleared:

1. ✅ **`chains_well_with` slug resolution** — 24 files, all slugs now resolve to existing files (3 broken refs found and fixed)
2. ✅ **`opposite_of` semantics check** — all 24 values are plausible anti-pattern labels; kept as free-form
3. ✅ **Verbatim spot-checks** — all 24 files re-verified against PDF (not just a sample); 8 issues caught and fixed
4. ✅ **source_quote overlap detection** — scanned; no true overlaps (same-page different-passage citations in Ch8 are expected and correct)
5. ✅ **Schema validation** — all 24 files have complete YAML frontmatter; all slugs match filenames

One minor follow-up flagged for future work: `agalmic-economy` source_anchor lists "pp8-10, pp15-16" but the verified source_quote is specifically from p8. Either narrow the anchor or add a verified pp15-16 excerpt. Non-blocking.

## Architecture of the Extraction

### Process used

1. **Phase 1** (Ch1-4, prior sessions): sequential chapter-by-chapter extraction by a single agent, with synthesis after each chapter. Produced 9 models.
2. **Phase 2** (Ch5-6, prior sessions): sequential with partial prior-agent handoff artefacts. Produced 4 more models (13 total after Ch6).
3. **Phase 3** (Ch7, prior session): 3 Ch7 models were written outside the formal synthesis flow (appearing on disk without SYNTHESIS-LOG entries until this session). Audited post-hoc in this session; 2 had quote-quality issues, both fixed.
4. **Phase 4** (this session, Ch8-9 + cross-chapter + merges): hybrid approach — 3 parallel read-only sub-agents produced candidate lists with verbatim quotes + pass/fail/borderline tags; parent agent synthesised sequentially against growing model set; every sub-agent-sourced quote was PDF-verified before being written to a model file. This caught multiple sub-agent quote errors that would otherwise have silently propagated.

### Where dedup comes from

**Synthesis decisions are logged in `SYNTHESIS-LOG.md`** — one entry per chapter, documenting which candidates were kept, which merged into existing models, which were dropped, and why. Chain-well-with references and opposite-of values are set during synthesis. The synthesis log is the canonical record of model distinctness.

**Not dedup-enforced automatically**: no embedding check, no automated similarity scan, no chains_well_with slug resolution pass (pending). Dedup is manual-agent-driven, backed by the log.

## How to Use This Set

### Run a decision through the default chain

```
/post-scarcity "your decision here"
```

This invokes the 5-model chain in `chains/default.md` and produces a Decision Brief.

### Pull specific optional extensions

Decide based on domain fit (see `chains/default.md` "Optional Extensions" section). Examples:
- AI-related decision → pull Dehumanization Tax, Externalized Cognition Fragility
- Market-structure decision → pull Abundance Graduation, Optimizer-Predation (already in default), Local Maximum Collapse
- Security / threat decision → pull Autonomic Countermeasures, Destructive Sandbox, Resimulation
- Identity / continuity decision → pull Aggregate State Vector Resurrection, Emotion-Conditioning
- Long-horizon strategy → pull Reversibility as Appreciating Asset, Local Maximum Collapse, Legacy Drives

### Browse / explore the set

Read `INDEX.md` for the full catalogue organised by source chapter, with decision-type tags per model. Each model file has a `decision_types` array in its frontmatter for filtering.

## What's Still Possible (if interest continues)

### Validation pass (highest priority, still pending)

Run the schema/verbatim/overlap checks listed above. Expected outcome: identify any remaining broken forward-references, flag any overlapping source_quotes for synthesis review, verify a sample of prior-session files' quote accuracy.

### Real-world case testing

Run `/post-scarcity` on 5-10 real decisions from your current work. Track: which models fired usefully, which felt forced, which chain orderings worked, whether the revised default chain holds up or needs re-tuning.

### Cross-source extension

The models are currently Stross-derived. A second book (Le Guin's *The Dispossessed*; Banks' *The Player of Games*; Cory Doctorow's *Walkaway*; Kim Stanley Robinson's *Aurora*) using `skills/extract-mental-models/SKILL.md` would test which post-scarcity models are Stross-specific and which are genuinely portable across the genre.

### Graduation to canonical library

Models that validate across multiple sources and decision-types should be considered for promotion from `memory/frameworks/post-scarcity/` to `skills/mental-models-os/models/[category]/` — the canonical Mental Models OS library. Criteria per SKILL.md: validated pattern outside the source text. Candidates from this set that look ready: Substrate Independence of Cognition (well-established across AI/philosophy literature); Optimizer-Predation Thesis (Schumpeter/Christensen literature); Asymmetric Theory-of-Mind Dominance (game-theory/alignment literature); Local Maximum Collapse (evolutionary biology/innovation literature).

## Source Artefacts

- Accelerando PDF: `experiences/captures/source-books/accelerando.pdf` (289 pages, 1.5MB)
- Extraction skill: `skills/extract-mental-models/SKILL.md`
- Model files: `memory/frameworks/post-scarcity/*.md` (24 files + INDEX + SYNTHESIS-LOG + HANDOFF)
- Default chain: `memory/frameworks/post-scarcity/chains/default.md`
- Command: `.claude/commands/post-scarcity.md`
- Prior plan: `experiences/plans/accelerando-mental-models-extraction-plan.md`
- Prior CSV of ideas (not models): `experiences/captures/book-ideas-accelerando.csv` (230 ideas — separate pipeline)
