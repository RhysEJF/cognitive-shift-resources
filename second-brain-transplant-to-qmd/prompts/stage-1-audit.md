# Stage 1 — Audit

> Paste this entire prompt into your AI agent (Claude Code, Claude Desktop, etc.) as a single message. The agent will read your repo, classify what's there, and report back. **No files are written in this stage.**

---

You are starting Stage 1 of the Second Brain Transplant to QMD. Your job in this stage is **read-only**: audit the user's existing second brain repo, classify what's there, and produce a clean report so we know what we're working with before any changes happen.

## Critical rules

- **Read-only.** Do not write, edit, delete, or move any files. Do not run `git add`, `git commit`, `npm install`, or any state-changing command.
- **No assumptions.** Do not assume the repo is Flow OS, or any specific template. Detect what's actually there.
- **Stop and report.** Once the audit is complete, present the findings as a structured report and STOP. Wait for the user to confirm before continuing to Stage 2.

## What to do

### 1. Confirm working directory

```bash
pwd
ls -la | head -20
```

Confirm the user is inside their second brain repo (a directory with markdown files, possibly a `.git` folder, possibly a CLAUDE.md or AGENTS.md). If it's clearly the wrong directory (no markdown, no obvious second-brain shape), STOP and ask the user to navigate to the right repo.

### 2. Detect the AI workflow shape

Check for known AI workflow files. Report which exist:

```bash
ls -la CLAUDE.md AGENTS.md SYSTEM.md system-prompt.md .claude/ .agents/ 2>/dev/null | grep -v "No such"
ls -la .claude/commands/ 2>/dev/null | head
ls -la skills/ 2>/dev/null | head
ls -la integrations/ 2>/dev/null | head
```

Identify the workflow. Likely one of:
- **Claude Code with Flow OS / TWIN / variant** — has `CLAUDE.md`, `.claude/commands/`, possibly `.flow/`, `vendor/qmd/`
- **Claude Code, hand-rolled** — has `CLAUDE.md`, possibly `.claude/commands/`, no `.flow/`
- **Claude Desktop user** — may have a `CLAUDE-desktop.md` and a `claude_desktop_config.json` somewhere
- **Custom GPT / other agent** — markdown vault, no `CLAUDE.md`, instructions live elsewhere
- **Plain markdown** — no agent workflow files at all yet

Don't guess. Say what you found.

### 3. Detect git status

```bash
git rev-parse --is-inside-work-tree 2>/dev/null && echo "GIT: yes" || echo "GIT: no"
git status --short 2>/dev/null | head
git log -1 --format='%h %ai %s' 2>/dev/null
git rev-parse --is-shallow-repository 2>/dev/null
```

Report:
- Is this a git repo?
- Is the working tree clean?
- When was the last commit?
- Is the history shallow (would limit our backup options)?

### 4. Inventory memory directories

Look for both `memory/` and any equivalent directory the user might use (some templates call it `vault/`, `notes/`, `brain/`, etc.):

```bash
for candidate in memory vault notes brain knowledge second-brain; do
  if [ -d "$candidate" ]; then
    echo "FOUND: $candidate/"
    for dir in "$candidate"/*/; do
      [ -d "$dir" ] || continue
      count=$(find "$dir" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
      printf "  %5s  %s\n" "$count" "$dir"
    done | sort -rn
  fi
done
```

Same for experiences-style directories:

```bash
for candidate in experiences episodes captures sessions; do
  if [ -d "$candidate" ]; then
    echo "FOUND: $candidate/"
    for dir in "$candidate"/*/; do
      [ -d "$dir" ] || continue
      count=$(find "$dir" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
      printf "  %5s  %s\n" "$count" "$dir"
    done | sort -rn
  fi
done
```

### 5. Classify each subdirectory

For each subdirectory you found in step 4, classify it as ONE of:

- **`auto-grown`** — looks like /learn or auto-extraction outputs (lots of small files with similar shape, structured content). Examples by name: `patterns/`, `contacts/`, `relationships/`, `frameworks/`, `knowledge-repo/`, `context/`, `solutions/`.
- **`hand-curated profile`** — slow-changing identity content. Examples: `personal/`, `values-beliefs/`, `style-voice/`, `audience/`, `examples/`, `company/`, `knowledge-sources/`.
- **`custom`** — user-specific dirs that don't match either of the above. Examples: `ventures/`, `products/`, `manuscripts/`, `clients/`, `kids/`, anything else. These are legitimate; preserve them.
- **`v2-default`** — date-sharded (year/month folders) or v2 entity-sharded (`customers/<entity>/`, `topics/<topic>/`). These exist if the user has migrated to a v2 schema.
- **`unknown`** — flag this for human review. Don't guess.

Report as a table:

```
DIRECTORY                  FILES   CLASSIFICATION         NOTES
memory/patterns/           197     auto-grown             ...
memory/ventures/            73     custom                 5 entity subdirs detected
memory/personal/             3     hand-curated profile   skip during /learn writes
[etc.]
```

### 6. Frontmatter usage check

Sample the first 3 markdown files in each auto-grown / custom dir. Report whether they have YAML frontmatter:

```bash
# For each file: check if line 1 is "---" and there's a closing "---" later
```

Categorise as:
- **Full v2 frontmatter** — has `id`, `type`, `entities`, `topics`, `source` etc.
- **Partial frontmatter** — has some YAML at top but not v2 schema
- **No frontmatter** — pure markdown

Report this at directory granularity ("memory/patterns/ — full v2 frontmatter; memory/ventures/flow/ — no frontmatter").

### 7. Existing search/index detection

Check if QMD or a similar search engine is already installed:

```bash
ls -la vendor/qmd/bin/qmd 2>/dev/null
which qmd 2>/dev/null
ls ~/.cache/qmd/ 2>/dev/null
```

Also check for residue from prior migrations:

```bash
ls -la .flow/ 2>/dev/null
cat .flow/migration.lock 2>/dev/null
```

If `.flow/migration.lock` exists, STOP — a prior migration may be in flight. Tell the user and don't proceed.

### 8. Report

Produce a single structured report with these sections:

```
## Audit Report

### Working directory
[path, repo name, last commit info]

### AI workflow detected
[Claude Code with X / Claude Desktop / custom GPT / plain markdown / etc.]
[Files present that confirm this]

### Git status
[Is this a git repo? Clean? Shallow? Last commit when?]

### Memory directories
[Table from step 5]

### Frontmatter usage
[Per-directory breakdown]

### QMD already installed?
[Yes/no, where]

### Concerns flagged for human review
[Anything classified as `unknown`, anything that looks broken, anything that doesn't fit a normal second-brain shape]

### Recommendations for Stage 2
[Specific notes for the backup stage based on what we found]
```

### 9. STOP

After producing the report, stop and tell the user:

> **Stage 1 audit complete.** Review the report above. If everything looks right, paste `prompts/stage-2-backup.md` to continue. If anything looks wrong, see `troubleshooting.md` or stop and reach out to Rhys.

Do NOT run any further commands until the user pastes the next stage prompt.
