# Stage 4 — Frontmatter (OPT-IN)

> Adds structured YAML frontmatter to markdown files that lack it. Improves search precision by giving QMD high-signal tokens (entity slugs, topic tags) to weigh. **You can skip this entire stage** — QMD works fine on raw markdown without frontmatter. If you do run it, the diff-then-approve flow keeps you in control.

---

You are starting Stage 4 of the Second Brain Transplant to QMD. **This is an OPT-IN stage.** If the user is here, they want to normalise frontmatter. If they're skipping this, they should have moved straight to Stage 5.

## Critical rules

- Touches the body of every markdown file in scope. Highest-risk stage in the transplant.
- Operate on a working branch off the backup, never directly on main.
- Show diffs in batches of 10 files at a time. Wait for explicit approval per batch. Do NOT batch-approve all at once.
- Skip hand-curated profile dirs entirely (`personal/`, `values-beliefs/`, `style-voice/`, `audience/`, `examples/`, `company/`, `knowledge-sources/`).
- If a file already has frontmatter, leave it alone. Do not "improve" or normalise existing frontmatter.

## What to do

### 1. Confirm the user wants this

> Stage 4 is opt-in. It will add YAML frontmatter to markdown files that don't have any. Specifically, it will:
> - Add `id`, `type`, `entities`, `topics`, `created`, `modified`, `confidence`, `relationships` fields
> - Skip files that already have a frontmatter block
> - Skip hand-curated profile dirs entirely
> - Touch each non-skipped file once
>
> Do you want to proceed? (Yes / No / Tell me more)

If "Tell me more": explain that QMD treats every YAML key as searchable text. A file with `entities: [tom-parker]` has a rare token (`tom-parker`) that BM25 weighs heavily. A plain markdown file with the same content gets the same body indexed but no entity-level boost. The frontmatter doesn't add behaviour to QMD — it adds high-signal anchors.

If "No": tell them to skip directly to Stage 5.

If "Yes": proceed.

### 2. Create a working branch

```bash
git checkout -b stage-4-frontmatter-tidy
```

This is separate from the backup branch. It lets us iterate without contaminating the rollback path.

### 3. Identify in-scope files

Read the audit report from Stage 1. For each directory classified as `auto-grown` or `custom`:

```bash
# Find markdown files that lack frontmatter
# A file lacks frontmatter if line 1 is NOT "---"
for dir in memory/patterns memory/contacts memory/relationships memory/frameworks memory/knowledge-repo memory/context experiences/solutions; do
  [ -d "$dir" ] || continue
  find "$dir" -name "*.md" -type f | while read f; do
    head -n 1 "$f" | grep -q "^---" || echo "NEEDS_FRONTMATTER: $f"
  done
done
```

Adapt the dir list to whatever Stage 1 reported. **Do NOT include** any of these dirs even if they have markdown files: `memory/personal`, `memory/values-beliefs`, `memory/style-voice`, `memory/audience`, `memory/examples`, `memory/company`, `memory/knowledge-sources`.

For custom dirs the user has (e.g., `memory/ventures/<slug>/`), include them. Walk recursively into entity subdirs.

Count the files in scope. Report:

```
NEEDS_FRONTMATTER: 47 files
SKIPPED (already has frontmatter): 134 files
SKIPPED (hand-curated profile): 18 files
SKIPPED (date-sharded date dirs): 14 files
```

If `NEEDS_FRONTMATTER` is 0, tell the user there's nothing to do and skip to step 7.

### 4. Generate proposed frontmatter per file

For each file, propose frontmatter using these rules:

- `id`: `mem_<YYYY-MM-DD>_<entity-slug>_<topic-slug>_<8-char-hash>` where:
  - Date is the file's git first-add date (`git log --diff-filter=A --format='%ai' -- <file> | tail -1 | cut -c1-10`), or today if not in git
  - Entity slug: derive from filename or the dir's parent (e.g., `memory/ventures/flow/foo.md` → entity `flow`); if uncertain, use `untitled`
  - Topic slug: derive from filename, slugified
  - Hash: first 8 hex of `sha256` of file body
- `type`: derive from the directory:
  - `memory/patterns/` → `pattern-candidate`
  - `memory/contacts/` → `contact-update`
  - `memory/relationships/` → `contact-update`
  - `memory/frameworks/` → `pattern-candidate`
  - `memory/knowledge-repo/` → `insight`
  - `memory/context/` → `decision`
  - `experiences/solutions/` → `pattern-candidate`
  - Custom dir under `memory/` → `insight` (default; user can change)
- `space`: detect from `memory/personal/expertise.md` if it exists, else use `default`
- `source`: `kind: manual`, `extractor_model: stage-4-frontmatter-tidy`, `extractor_version: v1`
- `entities`: best-effort guess from filename or parent dir
- `topics`: best-effort from filename
- `created`: file's git first-add date or today
- `modified`: today
- `confidence`: `0.5` (manual import; user can raise later)
- `relationships`: `[]`
- `supersedes`: `null`

### 5. Show diffs in batches of 10

For the first 10 files, generate the proposed file (frontmatter + original body unchanged). Show the diff:

```bash
diff -u <(echo "ORIGINAL") <(echo "PROPOSED") --label "$file (current)" --label "$file (proposed)"
```

Display all 10 diffs, then ask:

> Approve this batch of 10? (Yes / No / Show entities & topics for each file before approving)

If "Show entities & topics": display a compact table for the user to verify the slugging:

```
FILE                                          ENTITY            TOPICS
memory/patterns/anchoring-bias.md             untitled          anchoring-bias, psychology
memory/ventures/flow/cowork-mode.md           flow              cowork-mode, claude-desktop
[etc.]
```

The user may correct individual rows ("change 'untitled' to 'tom-parker' for row 3"). Apply corrections before writing.

If "Yes": write the 10 files. If "No": skip the entire batch and move to the next 10.

### 6. Repeat step 5 until all in-scope files are processed

Track progress:

```
Processed: 30 / 47
Approved: 27
Skipped: 3
Remaining: 17
```

Show this between batches.

### 7. Commit the changes

```bash
git add -A
git commit -m "stage-4: backfill frontmatter on $APPROVED_COUNT files"
```

If the user wants to merge back to main now:

```bash
git checkout main
git merge stage-4-frontmatter-tidy
```

If they want to keep it on the branch for now (review later), tell them how to switch back.

### 8. Report

```
## Stage 4 Frontmatter Report

- In scope: [N] files
- Approved: [X]
- Skipped: [Y]
- Already had frontmatter: [Z]
- Hand-curated dirs skipped: [list]
- Working branch: stage-4-frontmatter-tidy
- Merged to main: [yes / no, still on branch]
```

### 9. STOP

> **Stage 4 frontmatter complete.** Paste `prompts/stage-5-index.md` to continue with the first QMD index of your archive.

Do NOT run further commands until the user pastes the next prompt.
