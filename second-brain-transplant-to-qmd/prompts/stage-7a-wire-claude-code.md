# Stage 7a — Wire Claude Code

> Replaces grep calls in your `/plan` and `/learn` (or equivalent) commands with QMD queries. Run only if you use Claude Code as your primary AI host. Paste this entire prompt into your AI agent.

---

You are starting Stage 7a. Your job: find every place in the user's `.claude/commands/` (or equivalent) that calls grep or ripgrep against the memory dirs, and replace it with the appropriate QMD CLI call.

## Critical rules

- Do NOT modify any command file without first making a backup copy.
- Show diffs for every change, batch by command file. Wait for explicit approval before writing.
- Different second brains have different command names. Detect what's there; do not assume `/plan` and `/learn` exist.

## What to do

### 1. Identify command files

```bash
ls .claude/commands/ 2>/dev/null
```

If `.claude/commands/` doesn't exist, the user is not on a Claude Code setup that fits this stage. Tell them to use Stage 7b or 7c.

For each `.md` file in `.claude/commands/`, scan for grep calls:

```bash
grep -lE "grep -r|ripgrep|rg " .claude/commands/*.md 2>/dev/null
```

Report the list. Confirm with the user: "These N command files use grep. Replace them all, or some?"

### 2. Backup originals

```bash
for f in $(grep -lE "grep -r|ripgrep|rg " .claude/commands/*.md 2>/dev/null); do
  cp "$f" "$f.pre-qmd-backup"
done
ls .claude/commands/*.pre-qmd-backup
```

### 3. Generate replacements

For each command file, identify the grep call's intent and propose the QMD equivalent:

| Grep pattern | QMD replacement |
|---|---|
| `grep -ril "X" memory/` | `./vendor/qmd/bin/qmd query "X" --json -n 10` |
| `grep -r --include="*.md" "X" memory/` | Same — QMD only indexes markdown anyway |
| `ripgrep "X" memory/` | Same |
| Output piped to `head` | Add `-n` flag to qmd query for the same effect |
| Output filtered by sort/uniq | Drop the filter — qmd already returns ranked unique results |

For each command file, generate the proposed new version. Show the diff:

```bash
diff -u "$f.pre-qmd-backup" "$f"
```

### 4. Approve and write per file

For each diff, ask:

> Approve this change to `[command-file]`? (Yes / No / Show me the full new file)

Apply the user's decision. Skip files they reject; tell them they can apply manually later.

### 5. Pull in the routing table (if Flow OS-style)

If the user's `.claude/commands/learn.md` exists and references `suggested_path` or "file path conventions":

Tell them:

> Your `/learn` command needs the new Path Routing table to know where each memory type goes. Do you want me to fetch it from `flow-os-v2/.claude/commands/learn.md` and add it to your file? (Yes / No / Show me what would change)

If yes, fetch the relevant section from `https://github.com/RhysEJF/flow-os-v2/raw/main/.claude/commands/learn.md` (the "Path routing" subsection of Step 4) and integrate it into the user's learn.md. Show diff. Approve. Write.

### 6. Update CLAUDE.md (if it exists) to reference QMD

In CLAUDE.md, find any text that says "search uses grep" or describes the search method. Update it to reference QMD's three modes:

```markdown
### Search

Memory retrieval uses [QMD](https://github.com/tobi/qmd) — a hybrid markdown search engine running locally. Three modes:

```bash
./vendor/qmd/bin/qmd query "natural-language question" --json -n 5   # hybrid (best, ~10s)
./vendor/qmd/bin/qmd search "exact keywords"          --json -n 5    # BM25 only (fast, ~270ms)
./vendor/qmd/bin/qmd vsearch "semantic phrasing"     --json -n 5    # vector only
```

Cite the file path when referencing remembered material.
```

Show diff. Approve. Write.

### 7. Smoke-test

Run a real `/plan` or `/learn` command (or whatever the user has) and watch it execute. Verify it now calls qmd and returns sensible results.

### 8. Commit

```bash
git add .claude/commands/ CLAUDE.md
git commit -m "stage-7a: wire Claude Code commands to QMD"
```

### 9. Report

```
## Stage 7a Wire Report

- Command files modified: [list]
- Grep calls replaced: [count]
- CLAUDE.md updated: [yes / no]
- Smoke test: [passed / failed / skipped]
- Backup files at: .claude/commands/*.pre-qmd-backup
```

### 10. STOP

> **Stage 7a complete.** Claude Code is wired to QMD. If you also use Claude Desktop, paste `prompts/stage-7b-wire-claude-desktop.md`. Otherwise paste `prompts/stage-8-brand-the-upgrade.md`.

Do NOT run further commands until the user pastes the next prompt.
