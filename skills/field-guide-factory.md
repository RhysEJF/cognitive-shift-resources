---
name: field-guide-factory
description: Transform a topic idea into a fully architected field guide book outcome, or restructure an existing outcome into field guide format
triggers:
  - field guide
  - book
  - guide
  - tactical guide
  - book factory
  - write a book
  - write a guide
---

# Field Guide Factory

> Transform any topic into a publication-ready tactical field guide using the proven methodology from two successful books: "How to Win with Agentic Swarms" (SWARMS framework, 54K words, 86 tasks, 95% completion) and "The First 90 Days: A New Dad's Field Guide" (READY framework, 414KB, 152 tasks, 99% completion).

## Purpose

You are a field guide architect. Your job is to take a rough book idea — or an existing outcome that should become a field guide — and produce a fully structured, worker-ready outcome with framework, research taxonomy, capability skills, and wave-structured task breakdown.

You do two things:
1. **Create new field guide outcomes** from a topic idea
2. **Optimize existing outcomes** into field guide format (restructure intent, add framework, reorganize tasks into waves)

## Tools

- `flow show [outcome-id]` — View outcome context (summary, intent, approach, success criteria)
- `flow show [outcome-id] --tasks` — List all existing tasks
- `flow show [outcome-id] --intent` — View full intent JSON
- `flow update [outcome-id]` — Update outcome fields (name, intent, brief)
- `flow task add` — Create tasks with full structured fields
- `flow task update [id]` — Modify existing task fields
- `flow tasks` — List tasks for current outcome

## Mode Detection

**Creating new:** No outcome exists yet. You receive a topic description and must produce the full outcome specification (name, intent, success criteria, tasks).

**Optimizing existing:** An outcome ID is provided. Run `flow show [id] --intent` and `flow show [id] --tasks` to understand current state, then restructure into field guide format:
- Redesign the intent with framework and research taxonomy
- Reorganize existing tasks into the wave structure
- Add missing tasks (skills, research, synthesis, writing pipeline)
- Update task priorities to match wave ordering
- Add dependencies between waves

## The Proven Sequence

This exact sequence produced two successful field guides. **Do not skip or reorder steps.**

```
Wave 0: Foundation (Priority 1-5)
  → Task: Design research taxonomy and field guide framework
  → Task: Build [domain]-researcher skill
  → Task: Build [expert]-panel skill
  → Task: Build [guide]-writer skill

Wave 1: Research (Priority 10-20, ALL PARALLEL)
  → 40-60 independent research tasks
  → Each produces a standalone evidence document
  → No dependencies between research tasks

Wave 2: Synthesis (Priority 25-35)
  → Coverage matrix (map research to framework)
  → Knowledge base (organize all findings by chapter)
  → Gap analysis & debates document
  → [If personalized] Questionnaire design + human gate

Wave 3: Writing (Priority 40-60)
  → Skeleton drafts per chapter (can be parallel)
  → Triple review per chapter (depends on skeleton)
  → Final rewrite per chapter (depends on review)

Wave 4: Assembly & Publishing (Priority 70-80)
  → Assemble unified document (estimated_turns: 30+)
  → Extract quick-reference cards
  → Publishing metadata + launch materials
```

## Step-by-Step Methodology

### Step 1: Extract the Book Idea

From the user's input (ramble, sentence, or detailed brief), extract these six dimensions:

| Dimension | Question | Example (Swarms) | Example (Dad) |
|-----------|----------|-------------------|---------------|
| **Topic** | What is this about? | Agentic AI swarms for competitive advantage | Surviving first 90 days as a new dad |
| **Audience** | Who reads this? | Business leaders deploying AI | First-time dads (sleep-deprived, one free hand) |
| **Voice** | What tone? | Military field manual × McKinsey deck | Knowledgeable friend at 3am |
| **Scope** | What boundaries? | Complete strategic playbook | First 90 days only |
| **Personalization** | Tailored to whom? | General (organization-level) | Specific person (deep personalization) |
| **Research domains** | What disciplines? | 6: biology, military, gaming, MAS, business, complexity | 13: sleep, feeding, development, health, bonding... |

If dimensions are missing, make intelligent assumptions. Flag low-confidence assumptions.

### Step 2: Invent the Framework

This is the single most consequential creative step. The framework becomes the book's **primary navigation system** — a memorable acronym where each letter maps to a chapter.

**Design the framework by answering:**

1. What word captures the essence of this topic? (READY = "prepared"; SWARMS = the subject itself)
2. Can each letter map to a distinct, non-overlapping domain?
3. Does the ordering create a natural narrative arc?
4. Can someone find what they need in under 30 seconds using this framework?
5. Is the framework recursive or self-reinforcing?

**Output format:**

```markdown
## Primary Navigation: The [ACRONYM] Framework

| Letter | Domain | Core Question | Tagline |
|--------|--------|---------------|---------|
| X | Name | "Question it answers?" | One-line summary |
| Y | Name | "Question it answers?" | One-line summary |
...

Design principles:
1. [How the acronym relates to the topic]
2. [The "under pressure" findability test]
3. [How chapters progress narratively]
```

**Also design two secondary navigation systems:**
- **Timeline-based:** Implementation phases or chronological progression
- **Situation-based:** "I need to do X right now" → go to chapter Y, section Z

**Color code each chapter** for quick visual navigation.

### Step 3: Design the Research Taxonomy

For each framework chapter, define 5-10 specific research topics. Each topic becomes an independent worker task.

**Per topic, specify:**
- File path: `research/[domain]/[topic-slug].md`
- Framework mapping: which chapter section this feeds
- 5-8 specific, answerable research questions
- Target source types (peer-reviewed, doctrine, case studies, etc.)
- Cross-domain hooks (connections to other chapters)

**Target: 40-60 total research topics.**

**Evidence quality tiering** (adapt to domain):
- Scientific: Peer-reviewed → Institutional → Practitioner → Expert Opinion
- Business: Case study → Framework → Expert consensus → Anecdotal
- Creative: Established canon → Practitioner wisdom → Emerging practice

### Step 4: Specify the Three Capability Skills

Every field guide needs three specialized skills. Workers build these before research begins.

#### Skill 1: Domain Researcher

Teaches workers how to conduct deep research in this guide's domains. Must include:
- Domain-specific search strategies
- Evidence quality tiering methodology
- Standardized research document template
- Source evaluation criteria
- Cross-domain connection hooks

**Reference implementations:**
- Swarms: `cross-domain-researcher.md` (863 lines) — web search across 6 strategic domains
- Dad: `newborn-science-researcher.md` — scientific literature + clinical guidelines

#### Skill 2: Expert Panel

Defines a multidisciplinary panel of 5 experts for synthesis and validation. Must include:
- 5 expert lenses (each with specialization, analytical focus, and challenge areas)
- Individual lens analysis methodology (divergent)
- Cross-pollination and pattern detection
- Structured debate format for conflicting evidence
- Integration template

**The experts should represent different ways of knowing — not sub-specialties of the same discipline.**

**Reference implementations:**
- Swarms: Military Strategist, Game Theorist, Swarm Biologist, Systems Architect, Business Strategist
- Dad: Pediatrician, Dev Psychologist, Postpartum Doula, Dad Mentor, Couples Therapist

#### Skill 3: Guide Writer

Transforms research into tactical field guide prose. Must include:
- Voice and tone guidelines for the specific audience
- Chapter structure templates
- Formatting standards (scannable, navigable under pressure)
- Quick-reference card specifications
- Complete chapter specs mapping research to sections
- The 4-stage writing pipeline: skeleton → triple review → final rewrite → assembly

**Reference implementations:**
- Swarms: `field-guide-writer.md` (50KB) — authoritative + tactical
- Dad: `personal-guide-writer.md` (784 lines) — warm + actionable + personalized

### Step 5: Generate Tasks

Create the full task list. Use `flow task add` for new outcomes, or `flow task update` + `flow task add` for optimization.

**Critical task parameters:**
- `--title` — Action-oriented, specific
- `--description` — What, why, and done-looks-like
- `--priority` — Controls wave ordering (lower = earlier)
- `--complexity` — 1-10 score
- `--turns` — Estimated Claude turns
- `--depends-on` — Task ID of prerequisite
- `--verify` — Shell command returning exit 0 on success

#### Wave 0 Tasks (Priority 1-5)

```bash
flow task add --title "Design research taxonomy and field guide framework" \
  --description "THE most consequential task. Produce three files:
    1. taxonomy.md — Complete research plan with 40-60 topics, each with research questions, source strategies, and cross-domain hooks
    2. framework.md — [ACRONYM] framework specification with chapter architecture, research category mappings, cross-domain evidence weaving points, and quick-reference card specs
    3. research-template.md — Standardized template all research tasks follow
  This task's output becomes the blueprint for all subsequent work." \
  --priority 1 --complexity 8 --turns 20 \
  --verify "test -f taxonomy.md && test -f framework.md && test -f research-template.md"

flow task add --title "Build [domain]-researcher skill" \
  --description "Create skills/[name].md teaching workers how to conduct deep research across [N] domains. Include: domain-specific search strategies, evidence tiering, research document template, source evaluation, cross-domain hooks." \
  --priority 2 --complexity 6 --turns 12 \
  --verify "test -f skills/[name].md"

flow task add --title "Build [expert]-panel skill" \
  --description "Create skills/[name].md defining a 5-expert panel: [Expert1], [Expert2], [Expert3], [Expert4], [Expert5]. Include: individual lens methodology, cross-pollination protocol, structured debate format, integration template." \
  --priority 3 --complexity 6 --turns 12 \
  --verify "test -f skills/[name].md"

flow task add --title "Build [guide]-writer skill" \
  --description "Create skills/[name].md for writing tactical field guide prose. Include: voice guidelines for [audience], [ACRONYM] chapter structure templates, formatting standards, quick-reference card specs, 4-stage writing pipeline (skeleton → triple review → final rewrite → assembly)." \
  --priority 4 --complexity 7 --turns 15 \
  --verify "test -f skills/[name].md"

flow task add --title "Generate Wave 1-4 tasks from taxonomy" \
  --description "Using the completed framework.md and taxonomy.md, generate ALL remaining tasks for this field guide outcome.

READ ~/flow-data/skills/field-guide-factory.md — it contains the exact task templates for Waves 1-4 with descriptions, priorities, dependencies, complexity scores, and verify commands. Follow those templates precisely.

WAVE 1 (Priority 10-20): One task per research topic from taxonomy.md. Use the research task template from the skill. ALL must be independent (zero cross-dependencies). Target: 40-60 tasks.

WAVE 2 (Priority 25-35): Synthesis tasks — coverage matrix, knowledge base, gap analysis. If personalized, add questionnaire + human gate.

WAVE 3 (Priority 40-60): Per framework chapter — skeleton draft, triple review, final rewrite. Three tasks per chapter.

WAVE 4 (Priority 70-80): Assembly (estimated_turns: 35), quick-reference cards, publishing metadata.

Use flow task add for each task. Set depends_on between waves. Do NOT create tasks without reading the skill first — it contains critical constraints (e.g., assembly needs 30+ turns, research tasks must be independent)." \
  --priority 5 --complexity 6 --turns 30 \
  --depends-on "[framework design task ID]" \
  --verify "test $(sqlite3 ~/flow-data/data/twin.db \"SELECT COUNT(*) FROM tasks WHERE outcome_id='[outcome-id]' AND status='pending'\") -gt 30"
```

**IMPORTANT: If you are running out of turns before creating all Wave 1-4 tasks, create this Wave 0.5 task instead of trying to squeeze them all in. The worker that picks up this task will read the full skill and have enough turns to generate 60+ tasks.**

#### Wave 1 Tasks (Priority 10-20)

Generate one task per research topic from the taxonomy. **ALL run in parallel — no dependencies between them.**

```bash
# Repeat for each of the 40-60 research topics:
flow task add --title "Research: [Topic Name]" \
  --description "[Topic description from taxonomy]. Research questions: [Q1], [Q2], ... Cross-domain hooks: [connections]. Output: research/[domain]/[topic].md following research-template.md." \
  --priority [10-20] --complexity 4 --turns 10 \
  --verify "test -f research/[domain]/[topic].md"
```

#### Wave 2 Tasks (Priority 25-35)

```bash
flow task add --title "Build coverage matrix" \
  --description "Map all research documents against [ACRONYM] framework chapters. Identify: covered topics, gaps, thin evidence areas, domains with strongest/weakest coverage." \
  --priority 25 --complexity 5 --turns 8 \
  --depends-on "[all wave 1 task IDs]" \
  --verify "test -f coverage-matrix.md"

flow task add --title "Synthesize research into knowledge base" \
  --description "Organize ALL research findings by [ACRONYM] framework chapter. Create: (1) Section-by-section synthesis with source citations, (2) Top 15 most critical insights, (3) Conflicting/evolving evidence section, (4) Cross-reference index mapping topics to source paths." \
  --priority 28 --complexity 7 --turns 15 \
  --depends-on "[coverage matrix task ID]" \
  --verify "test -f knowledge-base.md"

flow task add --title "Gap analysis and debates" \
  --description "Document all research conflicts, thin evidence areas, and unresolved questions. For each: severity rating, available evidence, recommendation, and whether follow-up research is needed." \
  --priority 30 --complexity 6 --turns 12 \
  --depends-on "[knowledge base task ID]" \
  --verify "test -f gaps-and-debates.md"
```

**If personalized, add:**
```bash
flow task add --title "Design personalized questionnaire" \
  --description "Using knowledge base, design 30-40 conversational questions covering: [relevant personalization dimensions]. Questions should be informed by research to ask what actually matters." \
  --priority 30 --complexity 5 --turns 10 \
  --verify "test -f questionnaire.md"

flow task add --title "Human gate: complete personal interview" \
  --description "Present questionnaire for user to complete. BLOCKS all writing tasks until answers are submitted. Store answers in interview-answers.md." \
  --priority 32 --complexity 1 --turns 2 \
  --depends-on "[questionnaire task ID]"
```

#### Wave 3 Tasks (Priority 40-60)

Generate three tasks per framework chapter (skeleton → review → rewrite):

```bash
# For each chapter [X] in the framework:
flow task add --title "Write skeleton draft — Chapter [X]: [Name]" \
  --description "Write the skeleton draft for [ACRONYM] Chapter [X]: [Name]. Weave evidence from research into chapter structure defined in framework.md. Include: section headers, evidence citations, tactical playbooks, quick-reference cards. Use [guide]-writer skill methodology." \
  --priority [40 + chapter_index * 2] --complexity 6 --turns 15 \
  --depends-on "[knowledge base, gaps analysis, (if personalized) interview answers]" \
  --verify "test -f guide/drafts/ch[X]-[name].md"

flow task add --title "Triple review — Chapter [X]: [Name]" \
  --description "Run three review passes: (1) Accuracy — verify claims against research sources, (2) Evidence quality — check all citations have appropriate confidence tiers, (3) Writing quality — voice consistency, scannability, actionability. Use [expert]-panel skill for cross-domain validation." \
  --priority [50 + chapter_index * 2] --complexity 5 --turns 10 \
  --depends-on "[skeleton draft task ID]" \
  --verify "test -f guide/reviews/ch[X]-review.md"

flow task add --title "Final rewrite — Chapter [X]: [Name]" \
  --description "Incorporate all review feedback into publication-ready chapter. Ensure: voice consistency, all flagged issues resolved, quick-reference cards standalone-ready, cross-references to other chapters." \
  --priority [55 + chapter_index * 2] --complexity 5 --turns 12 \
  --depends-on "[review task ID]" \
  --verify "test -f guide/final/ch[X]-[name].md"
```

#### Wave 4 Tasks (Priority 70-80)

```bash
flow task add --title "Assemble complete field guide" \
  --description "Combine all final chapters into unified document. Add: title page, table of contents, introduction (framework overview + how to use this guide), appendices, comprehensive index, quick-reference card compilation. Ensure consistent formatting, working cross-references, and all three navigation systems functional." \
  --priority 70 --complexity 8 --turns 35 \
  --depends-on "[all final rewrite task IDs]" \
  --verify "test -f guide/final/[guide-name].md"

flow task add --title "Extract standalone quick-reference cards" \
  --description "Pull all quick-reference cards from chapters into standalone files. Each card should work without reading the full guide. Format for printing/fridge-posting." \
  --priority 75 --complexity 3 --turns 8 \
  --depends-on "[assembly task ID]" \
  --verify "test -d guide/cards/"

flow task add --title "Publishing metadata and launch materials" \
  --description "Create: (1) publishing-metadata.md with subtitle, description, audience, keywords, cover concepts, (2) launch-essay.md — meta-narrative about the book and its creation process, (3) teaser text for social/marketing." \
  --priority 78 --complexity 4 --turns 10 \
  --depends-on "[assembly task ID]" \
  --verify "test -f publishing-metadata.md"
```

### Step 6: Construct the Intent

Update the outcome intent with the full field guide architecture:

```bash
flow update [outcome-id] --intent '{
  "summary": "[One-sentence description]",
  "items": [
    {"title": "Research Taxonomy & Framework", "description": "...", "priority": "high", "status": "pending"},
    {"title": "Capability Skills", "description": "...", "priority": "high", "status": "pending"},
    {"title": "Cross-Domain Research Corpus", "description": "...", "priority": "high", "status": "pending"},
    {"title": "Knowledge Synthesis & Gap Analysis", "description": "...", "priority": "high", "status": "pending"},
    {"title": "Chapter Writing Pipeline", "description": "...", "priority": "high", "status": "pending"},
    {"title": "Assembly & Publishing", "description": "...", "priority": "medium", "status": "pending"}
  ],
  "success_criteria": [
    "Research corpus contains [N]+ documents across all [M] domains with standardized template compliance",
    "[ACRONYM] framework provides 3 navigation systems (topic, timeline, situation)",
    "Every claim traceable to research with evidence quality tier noted",
    "Guide includes [N]+ actionable playbooks/quick-reference cards",
    "Cross-domain pattern mapping identifies [N]+ non-obvious connections",
    "Quick-reference cards work standalone without reading full guide",
    "Final guide reads as [voice description] — not [anti-pattern]"
  ]
}'
```

## Optimizing an Existing Outcome

When called with an existing outcome ID:

### 1. Assess current state
```bash
flow show [id] --intent    # Understand current goals
flow show [id] --tasks     # See existing task structure
```

### 2. Identify what exists vs what's missing

| Component | Check | If Missing |
|-----------|-------|-----------|
| Framework acronym | Is there a memorable navigation system? | Design one (Step 2) |
| Research taxonomy | Are research topics defined? | Design taxonomy (Step 3) |
| Capability skills | Are researcher/panel/writer skills defined? | Add Wave 0 tasks |
| Research tasks | Do independent research tasks exist? | Generate Wave 1 tasks |
| Synthesis tasks | Knowledge base + gap analysis? | Add Wave 2 tasks |
| Writing pipeline | Skeleton → review → rewrite per chapter? | Add Wave 3 tasks |
| Assembly | Final assembly + publishing? | Add Wave 4 tasks |

### 3. Restructure

- Reorganize existing tasks into waves by updating priorities
- Add missing tasks from the template
- Set dependencies between waves
- Update the intent with framework and success criteria
- Update the outcome name if needed: `flow update [id] --name "[Title]: A [Audience] Field Guide"`

### 4. Validate

Run through the quality checklist (below) and fix any gaps.

## Quality Checklist

After creating or optimizing, verify:

- [ ] Framework acronym is 4-7 letters, thematically relevant, and memorable
- [ ] Each letter maps to a distinct, non-overlapping domain
- [ ] Research taxonomy covers 40+ topics across 4+ domains
- [ ] Three capability skills specified with enough detail to build
- [ ] Tasks follow 5-wave structure with correct priority ordering
- [ ] Wave 1 research tasks have ZERO dependencies between them (maximum parallelism)
- [ ] Assembly task has `estimated_turns >= 30` (cascade failure prevention)
- [ ] Success criteria are specific and measurable
- [ ] Personalization gate included if audience is specific
- [ ] Evidence quality tiering is appropriate for the domain
- [ ] No task exceeds 30 estimated turns without justification

## Critical Lessons (Hard-Won)

These come from the escalation records and HOMR memories of both completed books:

1. **Assembly tasks need 30+ turns.** Both books hit cascade failures when assembly was estimated at 9 turns but needed 41+. The system tried to decompose, which made it worse. Set high turn estimates upfront.

2. **Don't decompose — go deeper.** When a task fails, the system's instinct is to break it into subtasks. This creates cascade failures (16 times in the Swarms book). Instead: increase the turn limit and let the worker go deeper on the same task.

3. **Research tasks MUST be independent.** Every research task produces a standalone document. No research task depends on another research task's output. This enables 30-60 workers running in parallel.

4. **The knowledge base synthesis is the bridge.** This document maps all research to the framework. Without it, chapters are disconnected from evidence. It's the most important synthesis deliverable.

5. **Gap analysis prevents weak chapters.** Both books produced 49-54KB gap analysis documents that identified thin evidence, conflicts, and missing sources. These drove targeted follow-up research before writing began.

6. **Expert panels need epistemological diversity.** Choose experts who think differently (biologist + military strategist + game theorist), not experts who think similarly (three different biologists). Different ways of knowing > different specialties.

7. **Personalization requires a gate.** If the guide is for a specific person, you MUST block writing tasks on their questionnaire answers. Writing first and personalizing after produces generic content with names swapped in.

8. **The framework is invented, not provided.** Users provide topics and vibes. The system generates the framework acronym. Both READY and SWARMS were generated during intent optimization from casual user input.

9. **Skills before research, research before writing.** The wave ordering is load-bearing. Workers fail when they lack the researcher skill, chapters fail when they lack the knowledge base.

10. **Triple review catches drift.** Without accuracy + evidence + writing quality reviews, chapters drift from the research base. Each review pass catches a different class of error.

## Examples

### Example 1: From Ramble to Outcome
**User input:** "I will become a dad in October/Nov. Not yet a dad. So this should be a guide that helps me feel prepared."

**What this skill produces:**
- Name: "The First 90 Days: A New Dad's Field Guide"
- Framework: READY (Routines, Emergencies, Attachment, Development, You)
- 13 research domains, 55+ research tasks
- Expert panel: Pediatrician, Dev Psychologist, Doula, Dad Mentor, Couples Therapist
- Personalization: questionnaire + human gate
- Total: 152 tasks across 5 waves
- Result: 414KB deeply personalized guide

### Example 2: Technical Topic
**User input:** "Deep research-driven tactical field guide for winning through agentic swarms."

**What this skill produces:**
- Name: "How to Win with Agentic Swarms: A Tactical Field Guide"
- Framework: SWARMS (Sense, Wage, Adapt, Replicate, Mobilize, Sustain)
- 6 research domains, 40+ research tasks
- Expert panel: Military Strategist, Game Theorist, Swarm Biologist, Systems Architect, Business Strategist
- Total: 86 tasks across 5 waves
- Result: 54,000-word guide from 431,000 words of research

### Example 3: Optimizing an Existing Outcome
**User:** `flow update out_abc123 --optimize-intent` (outcome has 12 unstructured tasks about "writing a guide to remote team management")

**What this skill does:**
1. Reads current intent and tasks
2. Designs REMOTE framework (or similar)
3. Reorganizes 12 existing tasks into waves
4. Adds ~50 missing tasks (research, synthesis, writing pipeline)
5. Updates intent with framework and success criteria
6. Sets dependencies between waves
