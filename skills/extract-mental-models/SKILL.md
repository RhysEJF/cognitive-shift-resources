---
name: extract-mental-models
description: Extract reasoning patterns from dense texts into standardized, operational mental model files. Use when the user wants to systematically analyze books, articles, or documents to identify reusable thinking frameworks and decision-making patterns. Perfect for building personal thinking toolkits from expert content. ALWAYS use this skill when users mention extracting insights from books, building thinking toolkits, analyzing frameworks from experts, or want to systematize knowledge from dense texts into actionable tools.
---

# Extract Mental Models

This skill systematizes the extraction of **reasoning patterns** (not summaries or idea lists) from dense texts into standardized, operational mental model files. Each model becomes a reusable decision-making tool that works across multiple contexts and situations.

## What Makes a High-Quality Mental Model

High-quality mental models are **operational tools, not theoretical concepts**. They should be:

- **Decision-focused**: Help you make better decisions in real situations
- **Immediately actionable**: Include step-by-step guidance for application  
- **Accessible**: Clear one-liner summaries that capture the essence instantly
- **Grounded in examples**: Real-world scenarios showing the model in action
- **Chainable**: Connect logically with other thinking patterns

Think "infrastructure you run" not "content you read." Each model should change how you approach future decisions, not just add to your knowledge.

## Core Definition

A mental model qualifies when it satisfies four criteria:
- **Portable**: applies across multiple instances beyond a single scenario
- **Mechanistic**: explainable as "when X, then Y happens, because Z"
- **Reframes thinking**: alters future decisions, not just adds facts
- **Operationalizable**: has clear usage triggers and anti-patterns

## Four-Step Extraction Process

### 1. Read for patterns
Identify reasoning rules the author demonstrates; capture candidates with working titles and anchor passages

### 2. Filter rigorously
Test each candidate against the four criteria; target 1-3 survivors per chunk

### 3. Write standardized files
Use YAML frontmatter plus structured sections (What It Is, When to Use It, Walkthrough, Example, Chains Well With, Go Deeper)

### 4. Add metadata
Include source anchors, page ranges, and verbatim quotes for traceability

## Synthesis Rules Between Passes

Four outcomes for new models:
- **Keep standalone** (genuinely distinct)
- **Merge** (restatement of existing model)
- **Decompose** (existing model conflated two patterns)
- **Supersede** (new model is sharper)

Target: ~10-20 final models per source, not exhaustive catalogs.

## Quality Standards

Each extracted mental model must meet these standards:

### Content Quality
- **Concrete examples**: Use specific scenarios with real details, not hypotheticals
- **Clear triggers**: Specify exactly when to use (and when NOT to use) the model
- **Actionable walkthroughs**: Step-by-step processes that someone can follow immediately
- **Mechanistic explanations**: Explain WHY the model works, not just what it does

### Format Consistency  
- **Complete YAML frontmatter**: All required fields filled with accurate information
- **Structured sections**: Follow the exact section order and naming
- **Operational tone**: Write as tools for doing, not concepts for understanding
- **Self-contained**: Never reference external frameworks or libraries the reader might not know

### Practical Tests
Before finalizing any model, ask:
- **Can someone apply this to a real decision tomorrow?**
- **Does the example show specific actions, not just outcomes?**
- **Would this model change how I approach similar problems?**
- **Is it genuinely portable across different contexts?**

If any answer is "no," refine the model until all tests pass.

## Output Format

Each mental model should be saved as a separate .md file in `memory/frameworks/[source-slug]/` with this exact structure:

```yaml
---
name: first-principles-thinking
one_liner: "Break problems down to foundational truths, then reason up from there instead of borrowing someone else's conclusion"
categories: [general-thinking, problem-solving]
source: "Book/Article Title"
source_anchor: "Page X, Chapter Y"
difficulty: "intermediate"
chains_with: [inversion, second-order-thinking]
---

# First Principles Thinking

## What It Is
Break a problem down to its foundational truths, then reason up from there instead of borrowing someone else's conclusion. Most thinking is analogical (copying existing solutions), but first principles thinking decomposes problems to bedrock facts, then rebuilds solutions from those truths alone.

## When to Use It
Use this model when:
- Entering markets with entrenched incumbents and you need asymmetric strategy
- Facing cost structures that seem fixed but have never been questioned
- Building something where "best practice" produces average results
- Stuck because all obvious paths have been tried

Don't use when you have a working solution and need speed - first principles is slow and expensive.

## Walkthrough
1. **State the problem clearly** - Write what you're solving in one sentence without jargon
2. **List embedded assumptions** - What beliefs are you carrying about how this gets solved?
3. **Interrogate conventions** - For each assumption, ask "why" 3-5 times until you hit facts or accidents
4. **Build from constraints** - Using only verified facts, reason toward a solution
5. **Synthesize** - Compare your new approach to existing ones; the delta is your insight

## Example
Pricing a B2B SaaS product: Instead of copying per-seat pricing (convention), decompose to facts: value comes from outcomes achieved, costs scale with usage not seats. Result: outcome-based pricing that aligns cost with value and eliminates resentment over dormant seats.

## Chains Well With
- **Inversion**: Use inversion first to map failure modes, then first principles to build solutions that avoid them
- **Second-order thinking**: After building your solution, stress-test long-term consequences
- **Systems thinking**: First principles identifies components; systems thinking maps their interactions

## Go Deeper
- Aristotle's "Posterior Analytics" (original source)
- Elon Musk's battery cost reasoning example
- Feynman on knowing vs. knowing names
```

### Chaining Guidance

For the "chains_with" field and "Chains Well With" section:
- **Only reference models you've already extracted** or plan to extract from the same source
- **Use descriptive names** that clearly indicate what the other model does
- **Explain the logical connection**: How does using these models together create better outcomes?
- **If no clear chains exist**, leave the chains_with field empty and focus on standalone value

## Output Locations
- Book-derived models: `memory/frameworks/[source-slug]/`
- Include `INDEX.md` and `SYNTHESIS-LOG.md` with each extraction
