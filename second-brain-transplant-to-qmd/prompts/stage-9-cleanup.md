# Stage 9 — Cleanup

> Removes the backup branch and staging files. **Only run this AFTER you've used the new search layer for several sessions and you're confident it works correctly.** This stage removes your safety net.

---

You are starting Stage 9. Your job: delete the artefacts that the earlier stages created as safety nets, but only after the user explicitly confirms they're confident the transplant succeeded.

## Critical rules

- Confirm with the user that they've used QMD for at least a few sessions and are happy.
- Do NOT auto-delete anything. Show what would be removed; user approves each item.
- Keep the QMD install (`vendor/qmd/`, `~/.cache/qmd/`) — that's the new normal, not a safety net.

## What to do

### 1. Confirm readiness

Ask the user explicitly:

> Stage 9 removes the safety nets. Before continuing, confirm:
>
> 1. You've used QMD-powered search via your AI workflow for at least 2-3 sessions
> 2. The results have been accurate and useful
> 3. You haven't had to roll back anything yet
> 4. You're confident you don't need the backup branch as a fallback any more
>
> All four true? (Yes — proceed / No — wait, I'm not ready)

If "No": tell them no problem. They can come back to this stage in a week. The cost of leaving the safety net in place is approximately zero — a single git branch and a small markdown file.

If "Yes": proceed.

### 2. List what would be cleaned up

```bash
echo "=== Backup branch ==="
git branch | grep "pre-qmd-transplant"

echo ""
echo "=== Stage 4 working branch (if it exists) ==="
git branch | grep "stage-4-frontmatter-tidy"

echo ""
echo "=== Backup files ==="
ls -la .transplant-rollback.md 2>/dev/null
ls -la .claude/commands/*.pre-qmd-backup 2>/dev/null
ls -la "$HOME/Library/Application Support/Claude/claude_desktop_config.json.pre-qmd-backup" 2>/dev/null

echo ""
echo "=== Temp tarball (if Stage 2 used tarball mode) ==="
ls -la ../second-brain-pre-qmd-transplant-*.tar.gz 2>/dev/null
```

### 3. Approve each item

Ask per item:

> Delete backup branch `pre-qmd-transplant-<timestamp>`? It still exists on origin if you pushed it; this only deletes the local branch. (Yes / No / Show me what's on it)

> Delete `stage-4-frontmatter-tidy` branch? (Yes / No / Show me what's on it)

> Delete `.transplant-rollback.md`? Once gone, the rollback recipe is in this stage's git history but not in the working tree. (Yes / No)

> Delete `.claude/commands/*.pre-qmd-backup` files? These were the originals before Stage 7's grep replacements. (Yes / No)

> Delete `claude_desktop_config.json.pre-qmd-backup`? (Yes / No)

> Delete `../second-brain-pre-qmd-transplant-*.tar.gz`? (Yes / No)

For each "Yes":

```bash
git branch -d pre-qmd-transplant-<timestamp>
git branch -d stage-4-frontmatter-tidy
rm -f .transplant-rollback.md
rm -f .claude/commands/*.pre-qmd-backup
rm -f "$HOME/Library/Application Support/Claude/claude_desktop_config.json.pre-qmd-backup"
rm -f ../second-brain-pre-qmd-transplant-*.tar.gz
```

### 4. Update .gitignore

Remove the `.transplant-rollback.md` line if you deleted that file:

```bash
sed -i.bak '/^\.transplant-rollback\.md$/d' .gitignore && rm .gitignore.bak
```

### 5. Final commit

```bash
git status --short
git add -A
git commit -m "stage-9: cleanup transplant safety nets"
git push  # if there's a remote
```

### 6. Final report

```
## Stage 9 Cleanup Report

- Backup branches deleted: [list]
- Backup files deleted: [list]
- Tarballs deleted: [list]
- Final git push: [yes / no remote]

## Transplant complete

You are now running:
- QMD hybrid search (BM25 + vector + LLM reranker) at `vendor/qmd/`
- Local LLM models (~2 GB) at `~/.cache/qmd/`
- Routing + frontmatter discipline (Flow OS) baked into your /learn or equivalent
- Branding footer + Memory Layer section in README and CLAUDE.md (or equivalent)

What to do now:
1. Use it for a couple of weeks. Notice what kinds of queries land best.
2. If you're missing a kind of memory routing, edit `.claude/commands/learn.md`'s routing table.
3. If something breaks, see the article and the troubleshooting doc.
4. If you want hands-on help: https://x.com/virtual_rf
```

### 7. STOP

> **Transplant complete.** Welcome to a second brain that actually finds what you wrote.

Don't run anything else. The transplant is done.
