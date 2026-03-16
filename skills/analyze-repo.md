# Analyze Repo

## Purpose

Research an external repository, protocol, or tool and produce a structured evaluation brief that compares it against your system's architecture. The output is a research brief for later review during roadmap planning.

## When to Use

- When evaluating a new repo, protocol, or tool for potential integration
- When someone shares a link and you want to understand how it relates to your system
- When surveying the landscape during planning

## Process

### Step 1: Understand the External System

Fetch and read the documentation for the external repo/protocol/tool. Go deep — read:
- README, introduction, overview pages
- Core concepts, architecture, key abstractions
- API surface, SDK, event systems
- Any "how it works" or "getting started" guides

Extract:
- What problem it solves
- Core architecture and abstractions
- Key features and capabilities
- SDK/integration surface
- Ecosystem and community

### Step 2: Understand the Relevant Parts of Your System

Read the areas of your codebase that overlap with what this external system does. Map out where your system currently solves (or fails to solve) the same problems.

### Step 3: Write the Brief

Create a research brief using the template below.

### Step 4: Verify

- Confirm the repo URL is prominently included
- Confirm the "What We Should Borrow" section has effort estimates
- Confirm there's a summary table at the end

## Template

```markdown
# <Name>: Integration Analysis

> One-line summary of what this is and why it matters to your system.

## Source Material

- [<Repo/Docs Name>](<URL>) — brief description
- [<Additional sources>](<URL>) — if applicable

## What Is <X>?

<2-4 paragraphs explaining what this is, what problem it solves, and how it works at a high level.>

## Core Architecture

<Key abstractions, components, data flow. Include tables or diagrams where helpful.>

## Where Our System and <X> Overlap

### 1. <Overlap Area>
- **<X>**: How the external system handles this
- **Us today**: How our system currently handles this
- **Gap/Opportunity**: What's different

### 2. <Overlap Area>
...

<Cover all significant areas of overlap. Be specific about your current implementation — reference file paths, patterns, limitations.>

## What We Should Borrow (Ranked by Impact)

### 1. <Idea Name> — <HIGH/MEDIUM/LOW> IMPACT

**What**: One-line description of the idea.

**Why it improves our system**:
- Bullet points on concrete benefits

**What to change**:
- Specific files, APIs, components that would need modification
- New files/endpoints that would need to be created

**Effort**: <Low/Medium/High>. Brief justification.

### 2. <Idea Name> — <IMPACT LEVEL>
...

## What We Should NOT Adopt

- **<Feature>** — Why it doesn't fit our architecture or use case
- ...

## Summary

| Idea | Impact | Effort | Recommendation |
|------|--------|--------|----------------|
| ... | ... | ... | ... |

**Bottom line**: <One paragraph synthesis — what's the single biggest takeaway?>
```

## Quality Checklist

- [ ] Repo/docs URL is included prominently in Source Material
- [ ] "What Is" section explains it clearly enough for someone unfamiliar
- [ ] Overlap section references specific files and patterns in your codebase (not vague)
- [ ] Each "What We Should Borrow" item has: What, Why, What to change, Effort
- [ ] Items are ranked by impact (highest first)
- [ ] "What We Should NOT Adopt" section exists (even if short)
- [ ] Summary table covers all items
- [ ] Brief is saved to a persistent location for future reference
