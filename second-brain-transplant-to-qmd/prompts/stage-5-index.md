# Stage 5 — Index

> Runs the first real QMD index of your archive. Generates BM25 + vector embeddings for every markdown file in scope. Takes 10-30 minutes for substantial archives. Paste this entire prompt into your AI agent.

---

You are starting Stage 5 of the Second Brain Transplant to QMD. Your job: register the user's memory directories with QMD as collections, run the first index, and generate embeddings.

## Critical rules

- Do NOT index hand-curated profile dirs (`memory/personal/`, `memory/values-beliefs/`, `memory/style-voice/`, `memory/audience/`, `memory/examples/`, `memory/company/`, `memory/knowledge-sources/`). These contain identity content that should remain accessible to the AI but doesn't need to compete in /learn search results.
- The embedding step is long. Tell the user it's normal.
- After indexing succeeds, STOP. Do not continue to Stage 6.

## What to do

### 1. Decide where the index file lives

Two valid locations:

- **`~/.cache/qmd/index.sqlite`** (XDG cache, default for QMD CLI usage). This is what flow-os-v2 uses.
- **`<repo>/.flow/index.sqlite`** (in-repo, scoped to this brain). Use this if the user runs multiple brains on the same machine.

Default to `~/.cache/qmd/index.sqlite` unless the user has another QMD-using brain on the same machine. Confirm with them:

> The QMD index will live at `~/.cache/qmd/index.sqlite`. If you run multiple second brains on this machine, you should give each its own index file in-repo instead. Single brain? (Yes — default location / No — in-repo)

### 2. Register collections

Add the user's memory directories as QMD collections. For each directory in scope (auto-grown + custom + experiences from the Stage 1 audit):

```bash
QMD=./vendor/qmd/bin/qmd

# Standard memory drawers (only those that exist)
for dir in memory/patterns memory/contacts memory/relationships memory/frameworks memory/knowledge-repo memory/context memory/customers memory/topics; do
  [ -d "$dir" ] && $QMD collection add "$dir"
done

# Year-sharded dirs under memory/ (date-default v2 outputs)
for ydir in memory/2024 memory/2025 memory/2026 memory/2027; do
  [ -d "$ydir" ] && $QMD collection add "$ydir"
done

# Experiences subdirs
for dir in experiences/solutions experiences/captures experiences/conversations experiences/content experiences/plans experiences/clients; do
  [ -d "$dir" ] && $QMD collection add "$dir"
done

# Custom dirs (from Stage 1 audit). Walk one level deep into custom roots.
# Example for ventures/ — adapt to whatever the user has:
if [ -d "memory/ventures" ]; then
  for entity_dir in memory/ventures/*/; do
    [ -d "$entity_dir" ] && $QMD collection add "$entity_dir"
  done
fi

# Repeat for products/, manuscripts/, kids/, etc. — anything Stage 1 flagged as "custom".
```

Write a `.flow/qmd-exclude.txt` file to ensure hand-curated profile dirs are NEVER indexed:

```bash
mkdir -p .flow
cat > .flow/qmd-exclude.txt <<EOF
# Hand-curated profile dirs — read by the AI but not indexed for /learn search.
memory/personal/
memory/values-beliefs/
memory/style-voice/
memory/audience/
memory/examples/
memory/company/
memory/knowledge-sources/
EOF
```

(QMD respects this file if your version supports it. If yours doesn't, simply don't `collection add` those dirs.)

### 3. List collections to confirm

```bash
$QMD collection list
```

The output should show each registered directory with a file count. Spot-check that the counts match what Stage 1 reported.

### 4. Generate embeddings

This is the long-running step.

```bash
$QMD embed
```

Tell the user:

> QMD is generating vector embeddings for every chunk of every file. For an archive of a few hundred files, this typically takes 10-30 minutes. Larger archives (newsletter-style with 5+ years) can take longer.
>
> The terminal will look idle. It is not. Do not Ctrl-C. If you absolutely must stop, run `qmd embed` again later and it will resume from where it left off.

Run the command and wait. When it returns, capture the summary output.

### 5. Verify the index

```bash
ls -lh ~/.cache/qmd/index.sqlite
$QMD status
```

Confirm:
- The index file exists and is non-trivial in size (a few MB at minimum)
- `qmd status` reports collection counts that match step 3

### 6. Run a sanity-check query

Pick a query the user is likely to know the answer to. Ask them:

> What's a question you'd ask your second brain that you KNOW has an answer in there? Something specific. I'll run it and we'll see what comes back.

When they give a query:

```bash
$QMD query "<their query>" --json -n 5
```

Show them the top 5 results. Ask:

> Do these look right? Top result feels relevant?

If yes: index works, advance to Stage 6.
If no: don't proceed. Run `troubleshooting.md` checks, or ping Rhys.

### 7. Report

```
## Stage 5 Index Report

- Index location: [~/.cache/qmd/index.sqlite OR .flow/index.sqlite]
- Index size: [X MB]
- Collections registered: [N]
- Files indexed: [total]
- Embedding generation: [completed in M minutes]
- Sanity-check query: [query → top result title + score]
```

### 8. STOP

> **Stage 5 index complete.** Your archive is now searchable via QMD. Paste `prompts/stage-6-validate.md` to run a deeper validation before wiring this into your AI workflow.

Do NOT run further commands until the user pastes the next prompt.
