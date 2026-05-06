# Stage 2 — Backup

> Creates a safety branch (or tarball if no git) BEFORE any other stage touches your files. Paste this entire prompt into your AI agent.

---

You are starting Stage 2 of the Second Brain Transplant to QMD. Your job: create a safety net so the user can roll back to today's state instantly if anything later goes wrong.

## Critical rules

- Do NOT proceed if `.flow/migration.lock` exists. STOP and tell the user.
- Do NOT touch any markdown content in this stage — only create a backup.
- After backup is verified, STOP and report. Do not continue to Stage 3.

## What to do

### 1. Confirm git status (or initialize)

```bash
git rev-parse --is-inside-work-tree 2>/dev/null && IS_GIT=yes || IS_GIT=no
echo "Git repo: $IS_GIT"
```

**If it IS a git repo:**

Check the working tree is clean. If there are uncommitted changes, tell the user:

> The working tree has uncommitted changes. The transplant needs a clean baseline. Options:
> 1. Commit the changes first (most common)
> 2. Stash them (`git stash`) and pop after we're done
> 3. Discard them (`git restore .`) — destructive, only if you know what they are
>
> Tell me which option you want.

STOP and wait for the user's choice. Do not proceed until the working tree is clean.

**If it is NOT a git repo:**

Tell the user:

> This second brain isn't under git version control. We strongly recommend initialising git so that a) the transplant has a real backup, and b) future changes are tracked.
>
> Should I initialise git here? (Yes / No)

If yes:

```bash
git init
git add -A
git commit -m "Pre-transplant baseline (initial commit before QMD transplant)"
```

Confirm the commit succeeded before proceeding. If the user says no, switch to tarball backup mode (see step 3 below).

### 2. Create the safety branch

```bash
TIMESTAMP=$(date +%Y-%m-%d-%H%M%S)
BACKUP_BRANCH="pre-qmd-transplant-${TIMESTAMP}"

git branch "$BACKUP_BRANCH"
echo "Backup branch created: $BACKUP_BRANCH"
git rev-parse "$BACKUP_BRANCH"
```

If a remote exists, push the branch there too (so the safety net survives a laptop failure):

```bash
git remote -v | head -1
git push origin "$BACKUP_BRANCH" 2>/dev/null && echo "Pushed to origin" || echo "No remote push (local-only backup is still valid)"
```

### 3. (Tarball mode — only if user declined git init)

If the user explicitly chose NOT to use git in step 1:

```bash
TIMESTAMP=$(date +%Y-%m-%d-%H%M%S)
BACKUP_TARBALL="../second-brain-pre-qmd-transplant-${TIMESTAMP}.tar.gz"
tar czf "$BACKUP_TARBALL" .
ls -lh "$BACKUP_TARBALL"
```

Confirm the tarball is at least 1 KB (sanity check that it actually wrote). If it's empty, STOP — something is wrong, do not proceed.

### 4. Verify backup integrity

For git backup:

```bash
# The backup branch should point at the same tree as HEAD right now
[ "$(git rev-parse HEAD)" = "$(git rev-parse $BACKUP_BRANCH)" ] && echo "OK: branch matches HEAD" || echo "FAIL: branch diverged"
```

For tarball backup:

```bash
# List the top-level entries to confirm the archive isn't empty
tar tzf "$BACKUP_TARBALL" | head
```

If either verify fails, STOP and report. Do not advance.

### 5. Create rollback recipe file

Write `.transplant-rollback.md` (gitignored) with the exact commands to undo everything from Stage 3 onward:

```bash
cat > .transplant-rollback.md <<EOF
# Rollback recipe (created $TIMESTAMP)

If anything goes wrong before Stage 9 (cleanup), restore the pre-transplant
state with these commands:

\`\`\`bash
# 1. Discard any in-progress changes
git restore .

# 2. Reset to the backup branch
git checkout $BACKUP_BRANCH
git checkout -B main  # or whatever your main branch is called

# 3. Delete the QMD index and downloaded models (recreate them later if you want)
rm -rf ~/.cache/qmd/

# 4. Remove the vendored QMD source (if Stage 3 ran)
rm -rf vendor/qmd/

# 5. (If Stage 8 ran) Edit README.md and CLAUDE.md to remove the
#    "Memory Layer" / footer sections added during branding.
\`\`\`

Backup branch: $BACKUP_BRANCH
Backup commit: $(git rev-parse $BACKUP_BRANCH 2>/dev/null || echo 'tarball: see ../second-brain-pre-qmd-transplant-*.tar.gz')
EOF

# Add to .gitignore so this file doesn't end up committed
grep -qxF '.transplant-rollback.md' .gitignore 2>/dev/null || echo '.transplant-rollback.md' >> .gitignore
```

### 6. Report

```
## Stage 2 Backup Report

- Backup type: [git branch / tarball]
- Backup location: [branch name / tarball path]
- Backup integrity: [verified OK]
- Remote pushed: [yes / no / no remote]
- Rollback recipe written to: .transplant-rollback.md
```

### 7. STOP

> **Stage 2 backup complete.** Your second brain is snapshotted at branch `[BACKUP_BRANCH]`. Any later stage can be undone via `.transplant-rollback.md`.
>
> Paste `prompts/stage-3-install-qmd.md` to continue.

Do NOT run further commands until the user pastes the next prompt.
