---
name: extract-mental-models
description: Extract genuine mental models (reasoning patterns, not ideas) from a text — book chapter, essay, research paper, transcript — into the standard Mental Models OS file format, with synthesis rules to merge overlapping models and decompose overloaded ones across multiple extraction passes
---

# Extract Mental Models from a Text

> Turn a text into a sharp set of reasoning patterns — not a summary, not an idea list — in the same format as the canonical Mental Models OS library, so they can feed a `/think`-style chain command.

## When to Use

- A book (or long text) is dense with reasoning patterns that would shape future decisions, not just provide information
- You want a *reusable thinking toolkit* out of a source, not a bookmark collection
- You intend to build (or already have) a `/think`-style command that chains the extracted models on user-supplied situations

**Skip this skill if**:
- You want an idea list, product catalogue, or highlight reel — use a simpler extraction pipeline (see `experiences/solutions/parallel-book-idea-extraction-to-csv.md`)
- The text is only one chapter or essay — the synthesis step needs multiple passes to earn its keep

## What Counts As a Mental Model

A mental model is a **reasoning pattern** — not a fact, not a product, not an anecdote. It qualifies if it meets all four tests:

1. **Portable**: applies across multiple specific instances in the text (or plausibly across many more beyond it). If it only describes one character, product, or scenario, it's an idea, not a model.
2. **Has a mechanism**: you can state it as "when X condition holds, Y tends to happen, because Z". Models without mechanisms are just observations.
3. **Changes how you think, not just what you know**: after learning it, future decisions get reframed. If it's just a new fact, it's not a model.
4. **Has a clear trigger and anti-pattern**: you can name "use when..." and "don't use when...". Without these, the model is too fuzzy to operationalize.

**Test case — "uplifted lobsters in Accelerando"**:
- One specific product → **fails Test 1** (portability)
- The underlying pattern — *cognition is portable across substrates (biological → silicon → uplifted animal → fictional)* — passes all 4 tests. That's the model. Call it **Substrate Independence of Cognition**.

## Extraction Methodology

### Step 1: Read the Chunk for Reasoning Patterns

Read the assigned text chunk in full. As you read, track candidates that might be mental models. For each candidate, mentally answer:

- What *reasoning pattern* is the author illustrating through this passage?
- Is the author demonstrating a rule about how a certain type of situation tends to play out?
- Could I state the pattern in one sentence without mentioning the specific characters/products?

If yes to all three, it's a candidate. Capture it in a short note:
- **Candidate name** (working title, kebab-case slug)
- **One-sentence pattern** (the reasoning rule)
- **Anchor passage** (page + 1-2 sentences of source)

Aim for 3-5 candidates per chunk. You'll filter down.

### Step 2: Filter Against the 4 Tests

For each candidate, run the 4 tests above. If it fails any one, either:
- Demote it (it's an idea, not a model — log in an `ideas-only.md` file or just drop)
- Rewrite it (often a failing candidate points to a *better* model one level up — the specific instance becomes evidence, the abstraction becomes the model)

Target yield: **1-3 surviving models per chunk**. More than 3 usually means you're extracting ideas, not models.

### Step 3: Write the Model File

Each surviving model gets its own file. Use this exact format (matches the canonical Mental Models OS library at `skills/mental-models-os/models/[category]/[slug].md`):

```markdown
---
name: [Human-readable name — Title Case]
slug: [kebab-case-slug]
category: [economics | systems | general-thinking | psychology | network-effects | business-strategy | post-scarcity | other — pick the best fit]
source: "[Original author / work, with year — cite the text you extracted it from]"
source_anchor: "[Chapter label, page range — e.g., Ch1: Lobsters, p11-13]"
source_quote: "[Verbatim 1-2 sentence quote from the text anchoring the model]"
difficulty: [beginner | intermediate | advanced]
decision_types: [array — strategy, pricing, product, investment, marketing, hiring, risk, operations, organizational, communication, innovation, policy]
chains_well_with: [array of slugs — leave empty initially, fill during synthesis]
opposite_of: [single concept slug — the mirror pattern]
---

# [Name]

> [One-sentence tagline. Crystalline. This is what a reader sees first.]

## What It Is

[2-4 paragraphs. Explain the pattern, its mechanism, and why it matters. Include the intellectual context when relevant — does it echo an existing named idea? Who has articulated it before? Aim for 200-400 words total.]

## When to Use It

Use this model when you're:
- [Trigger scenario 1]
- [Trigger scenario 2]
- [Trigger scenario 3]
- [Trigger scenario 4]

**Don't use it when:** [One sentence on the anti-pattern — when this model mis-fires or over-applies.]

## The Walkthrough

### Step 1: [Action verb + object]
[Operational paragraph — what you actually do]

### Step 2: [Action verb + object]
[Operational paragraph]

### Step 3: [Action verb + object]
[Operational paragraph]

### Step 4: [Action verb + object]
[Operational paragraph]

## Example

**Decision:** [A concrete decision — can be from the source text, or invented to show the model outside its original context]

**Applying [Model]:**
- Step 1: [How the step plays out on this decision]
- Step 2: [How the step plays out]
- Step 3: [How the step plays out]
- Step 4: [Conclusion or action]

## Chains Well With

- **[Related model 1]** (`/[slug]`): [One sentence on why they chain.]
- **[Related model 2]** (`/[slug]`): [One sentence on why they chain.]
- **[Related model 3]** (`/[slug]`): [One sentence on why they chain.]

(Leave this section blank on first extraction — fill during synthesis.)

## Go Deeper

- [Source work + chapter/page anchor]
- [Any directly related real-world work the model echoes — e.g., "Kurzweil, The Singularity Is Near (2005)" for substrate-independence claims]
- [Optional: a real incident that validates the pattern]
```

### Step 4: Add Extraction Metadata

Beyond the canonical frontmatter, post-scarcity (or book-derived) models get two extra frontmatter fields:
- `source_anchor`: chapter + page range
- `source_quote`: the verbatim passage that anchored the model

These exist so future readers can trace the model back to the text and judge whether the abstraction was fair.

## Synthesis Rules (between extraction passes)

After each chunk, before moving to the next, run a synthesis pass against the already-extracted set. Four possible outcomes per new model:

### A. New — keep standalone

The model is genuinely distinct. No overlap with existing ones. Keep as-is. Log in synthesis log: *"New, distinct from existing set."*

### B. Merge — fold into existing

The new model is a restatement or special case of an existing model. Action:
- Add the new model's source quote + page anchor to the existing model's `source_quote` field (become a `source_anchors` array: multiple entries)
- Add a bullet to the existing model's "When to Use It" capturing the new instance
- Delete the new file
- Log: *"Merged into [existing-slug]. Reason: [overlap nature]."*

### C. Decompose — existing model was too broad

The new model shares some ground with an existing one, but examination reveals the existing model was conflating two distinct patterns. Action:
- Split the existing model into two narrower models
- Write the two narrower models as fresh files; delete the old one
- The new model from this chunk becomes one of the two (or neither, if it's distinct from both splits)
- Log: *"Decomposed [old-slug] into [slug-A] + [slug-B]. New model from Ch[N] became [which]."*

### D. Supersede — new model is sharper

The new model captures what the existing one was reaching for, but better. Action:
- Rename the new model's slug to take over the old name (if the old name was good)
- Add the old model's source anchors to the new file
- Delete the old file
- Log: *"Superseded [old-slug] with [new-slug]. Reason: [what's sharper]."*

### Default behaviour

If in doubt, **merge** rather than keep parallel models. The target is a small, sharp set (~10-20 models after all passes), not a completeness catalogue. A reader using a `/think`-style command on your extracted models will not thank you for 40 near-duplicates.

## Output Location Convention

- **Book-derived post-scarcity models** (this project): `memory/frameworks/post-scarcity/[slug].md`
- **Book-derived models from other texts**: `memory/frameworks/[text-slug]/[slug].md`
- **Canonical Mental Models OS library** (timeless, broad): `skills/mental-models-os/models/[category]/[slug].md` — **do NOT write extracted models here unless you've validated the pattern outside the source text**

Each book/source directory should also contain:
- `INDEX.md` — discovery list of kept models with one-line descriptions
- `SYNTHESIS-LOG.md` — append-only log of every merge/decompose/supersede decision across extraction passes

## Quality Checks

Before marking a chunk done:

1. **All 4 tests passed** for each kept model — portable, mechanism, reframing, trigger+anti
2. **No model describes just one character or product** — those are ideas, not models
3. **Each model has an anti-pattern** — if you can't articulate when NOT to use it, the model is too fuzzy
4. **Synthesis log updated** — explicit decision for each new model (New / Merge / Decompose / Supersede)
5. **Source quote is verbatim** — no splicing, no paraphrase (see pattern: Sub-Agent Quote-Splicing Risk)

## Integration with `/think`-style Commands

Models extracted via this skill can be chained in a `/think`-style command. The chain command needs to:
- Read models from the output directory (e.g., `memory/frameworks/post-scarcity/`)
- Pick 3-5 relevant to a user-supplied situation
- Run each model's walkthrough on that situation
- Produce a Decision Brief in the same format as `/think`

See `.claude/commands/think.md` for the reference implementation pattern.
