# Stage 7 — Wire Claude Code

> Finds every place in the user's repo that calls grep against memory dirs, classifies each by intent, and replaces the right ones with `qmd query`. Per-instance approval — the user picks which to swap. Paste this entire prompt into your AI agent.

---

You are starting Stage 7 of the Second Brain Transplant to QMD. Your job: thoroughly audit the user's repo for grep usage, classify each occurrence by intent, present a numbered list, and replace ONLY the ones the user explicitly approves.

## Critical rules

- Scan more than `.claude/commands/`. Grep usage hides in skills, integrations, scripts, hooks, top-level docs.
- Some grep calls SHOULD stay. Frontmatter field scans, file-existence checks, config probes — none of those benefit from QMD. Don't auto-replace; classify and propose.
- Per-instance approval. Show the user every occurrence with its context and a recommended action. They pick.
- Backup before writing. One backup file per modified source file.

## What to do

### 1. Comprehensive scan

Search every plausible location for grep / ripgrep / rg invocations:

```bash
# Directories that typically contain workflow specs or scripts
SCAN_DIRS=(
  ".claude/commands"
  ".claude/hooks"
  "skills"
  "integrations"
  "scripts"
  "workflows"
  "docs"
)

# Top-level files that may contain grep usage in instructions
SCAN_FILES=(
  "CLAUDE.md"
  "AGENTS.md"
  "SYSTEM.md"
  "README.md"
)

echo "=== grep occurrences in directories ==="
for dir in "${SCAN_DIRS[@]}"; do
  [ -d "$dir" ] || continue
  grep -rnE "(^|[^a-z_-])(grep|ripgrep|rg)[ ]" "$dir" 2>/dev/null
done

echo ""
echo "=== grep occurrences in top-level files ==="
for f in "${SCAN_FILES[@]}"; do
  [ -f "$f" ] && grep -nE "(^|[^a-z_-])(grep|ripgrep|rg)[ ]" "$f" | sed "s|^|$f:|"
done
```

If the scan returns nothing, tell the user: there's no grep to replace — they may already be using QMD or have a setup that doesn't search by file at all. Skip to the CLAUDE.md update step (step 6).

### 2. Classify each occurrence

For each line returned by the scan, determine intent. Categories:

| Category | Pattern signals | Default action |
|---|---|---|
| **Body search** | `grep -ril "<query>" memory/` ; searches markdown body for a keyword | **Replace with `qmd query`** |
| **Frontmatter field scan** | Looks for `^id:`, `^entities:`, `extractor_version:`, etc. | **Keep as grep** — QMD doesn't search frontmatter as a separate field |
| **File-existence check** | `grep -q "string" .env` ; existence test, no body retrieval | **Keep as grep** |
| **Pattern in profile dir** | Searches `memory/personal/`, `memory/values-beliefs/`, `memory/style-voice/`, etc. | **Keep as grep** — profile dirs are not QMD-indexed |
| **Documentation example** | grep appears inside a code fence as illustration of v1 behaviour | **Keep as grep, but flag for the user** — they may want to update the docs to mention QMD instead |
| **Ambiguous** | Can't tell from the surrounding context | **Show the user, ask** |

Read enough context around each line (5 lines before, 5 after) to make this call. When in doubt, classify as Ambiguous and ask.

### 3. Present the numbered list

Format the findings so the user can scan and decide quickly:

```
Found N grep occurrences across M files.

[1] .claude/commands/plan.md:78
    Surrounding context: inside a "Search past memories" step
    Line: grep -ril "$TASK_KEYWORDS" memory/ experiences/
    Category: Body search
    Recommended: Replace with `./vendor/qmd/bin/qmd query "$TASK_KEYWORDS" --json -n 10`

[2] .claude/commands/learn.md:142
    Surrounding context: inside the watermark check
    Line: grep -lE "extractor_version: v1-import" memory/patterns/
    Category: Frontmatter field scan
    Recommended: Keep as grep

[3] scripts/setup.sh:23
    Surrounding context: probing for env var
    Line: grep -q "QMD_PATH" .env
    Category: File-existence check
    Recommended: Keep as grep

[4] integrations/leanpub/skill.md:45
    Surrounding context: scanning a profile dir
    Line: grep -n "book_id" memory/personal/
    Category: Pattern in profile dir
    Recommended: Keep as grep (profile dir, not QMD-indexed)

[5] CLAUDE.md:312
    Surrounding context: in a Memory Search Rules section
    Line: grep -ri "topic" memory/ | head -10
    Category: Documentation example (instructive prose, not executed)
    Recommended: Update the doc to describe `qmd query` instead

[6] skills/research/SKILL.md:88
    Surrounding context: ambiguous — line is inside a how-to that could be illustrative or executable
    Line: grep -ril "$KEYWORD" memory/research/
    Category: Ambiguous
    Recommended: Ask the user
```

### 4. User picks per instance

Present:

> Found N occurrences. Tell me which ones to act on. You can say:
> - "Apply the recommendations" — I'll do whatever each row says (Replace / Keep / Update doc)
> - "Replace 1, 6" — only the listed numbers
> - "Replace all body searches, keep the rest" — auto-pick by category
> - "Show me [N] in full context" — I'll read 30 lines around the occurrence
> - "Skip [N]" — leave that one alone
>
> Default if you say "go": apply the recommendations as listed.

Wait for explicit selection. Don't proceed until you have one.

### 5. Apply the approved changes

For every file that will be modified, back it up first:

```bash
for f in <list of files to modify>; do
  cp "$f" "$f.pre-qmd-backup"
done
```

Generate the patched version per file. Use these replacements:

| Grep pattern | QMD replacement |
|---|---|
| `grep -ril "X" memory/` | `./vendor/qmd/bin/qmd query "X" --json -n 10` |
| `grep -ril "X" memory/ experiences/` | `./vendor/qmd/bin/qmd query "X" --json -n 10` (QMD already searches all registered collections) |
| `grep -r --include="*.md" "X" memory/` | `./vendor/qmd/bin/qmd query "X" --json -n 10` (QMD only indexes markdown anyway) |
| `ripgrep "X" memory/` or `rg "X" memory/` | Same as above |
| Output piped to `head -N` | Use `-n N` flag on qmd query for the same effect |
| Output filtered by sort/uniq | Drop the filter — qmd already returns ranked unique results |

For each file: show the diff. Ask:

> Approve this patch to `[file]`? (Yes / No / Skip and continue)

Apply per the user's response.

### 6. Update CLAUDE.md to reference QMD search

If CLAUDE.md exists and has a section describing the search method, update it to reference QMD's three modes. Find the relevant section (Memory Search, How To Search, Search Rules, etc.) and propose:

```markdown
### Search

Memory retrieval uses [QMD](https://github.com/tobi/qmd) — a hybrid markdown search engine running locally. Three modes:

\`\`\`bash
./vendor/qmd/bin/qmd query "natural-language question" --json -n 5   # hybrid (best, ~10s)
./vendor/qmd/bin/qmd search "exact keywords"          --json -n 5    # BM25 only (fast, ~270ms)
./vendor/qmd/bin/qmd vsearch "semantic phrasing"     --json -n 5    # vector only
\`\`\`

Cite the file path when referencing remembered material.
```

Show the diff. Ask. Apply.

### 7. (If Flow OS-style) Pull the routing table into learn.md

If the user's `.claude/commands/learn.md` exists and references `suggested_path` or "file path conventions" — meaning it's a Flow OS-derived /learn — they need the new Path Routing table for /learn to actually write to the right drawers post-transplant.

Tell the user:

> Your `/learn` command needs the Path Routing table to know where each memory type goes. Without it, /learn writes everything to the date-sharded fallback. Pull it in from flow-os-v2? (Yes / No / Show me what would change)

If yes, fetch from `https://raw.githubusercontent.com/RhysEJF/flow-os-v2/main/.claude/commands/learn.md`, extract the "Path routing" subsection of Step 4, and integrate it into the user's learn.md. Show the diff. Apply on approval.

### 8. Smoke-test

Run a real `/plan` or `/learn` (or whatever Claude Code command was modified) end-to-end. Watch it execute. Verify it now calls qmd and returns sensible results. If it fails, restore the relevant `.pre-qmd-backup` file and investigate.

### 9. Commit

```bash
git add -A
git commit -m "stage-7: wire Claude Code commands to QMD"
```

### 10. Report

```
## Stage 7 Wire Report

- Total grep occurrences found: [N]
- Replaced: [count] (list of files + line numbers)
- Kept (frontmatter scans, profile dirs, etc.): [count]
- Documentation updates: [count]
- Skipped: [count]
- Backup files at: [list of *.pre-qmd-backup]
- Smoke test: [passed / failed / skipped]
```

### 11. STOP

> **Stage 7 complete.** Claude Code is wired to QMD. Paste `prompts/stage-8-memory-layer-note.md` to continue.

Do NOT run further commands until the user pastes the next prompt.
