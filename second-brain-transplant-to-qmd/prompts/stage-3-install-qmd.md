# Stage 3 — Install QMD

> Vendors the QMD source into your repo, builds it, and downloads the local LLM models on first run. About 2 GB of disk space, 5-15 minutes. Paste this entire prompt into your AI agent.

---

You are starting Stage 3 of the Second Brain Transplant to QMD. Your job: install QMD locally so it's ready to index the user's archive in Stage 5.

## Critical rules

- Confirm Node 22+ before doing anything else. QMD requires it.
- Vendor QMD into `vendor/qmd/` inside the user's repo (not globally). This keeps the version pinned to whatever the user has, and makes the install portable.
- The first run downloads ~2 GB of GGUF models. Do NOT abort partway. Tell the user this is normal.
- After install is verified, STOP. Do not continue to Stage 4.

## What to do

### 1. Verify Node version

```bash
node --version
```

If Node is missing or below v22, STOP and tell the user:

> QMD requires Node 22 or later. You have [version]. Install Node 22+ from https://nodejs.org or via a version manager like nvm/fnm/volta, then come back to this stage.

### 2. Vendor the QMD source

```bash
mkdir -p vendor
cd vendor
git clone https://github.com/tobi/qmd.git
cd qmd
git log -1 --format='%h %ai %s'
cd ../..
```

If `vendor/qmd/` already exists:

```bash
cd vendor/qmd
git pull origin main
git log -1 --format='%h %ai %s'
cd ../..
```

Confirm the directory exists and the latest commit is recent. Report the commit hash.

### 3. Build QMD

```bash
cd vendor/qmd
npm install
npm run build
cd ../..
```

This step typically takes 1-3 minutes. If `npm install` fails, the most common cause is a Node version that's actually less than 22 even though `node --version` reported otherwise (e.g., shell using an older binary via PATH). Confirm with `which node`.

If the build succeeds, verify the binary:

```bash
ls -la vendor/qmd/bin/qmd
```

It should be executable. If it's missing, STOP and report.

### 4. Trigger the model downloads (first-run side effect)

QMD downloads three GGUF models on first use:

| Model | Purpose | Size |
|---|---|---|
| `embeddinggemma-300M-Q8_0` | Vector embeddings | ~300 MB |
| `qwen3-reranker-0.6b-q8_0` | Re-ranking | ~640 MB |
| `qmd-query-expansion-1.7B-q4_k_m` | Query expansion | ~1.1 GB |

All three are downloaded to `~/.cache/qmd/models/`. Total: about 2 GB. They are local-only, never sent over the network after download.

Trigger the first download now (uses a tiny test file so we don't need the user's content yet):

```bash
mkdir -p /tmp/qmd-test
echo "QMD model warm-up test file" > /tmp/qmd-test/warmup.md

# Initialize a tiny QMD index against this temp dir to force model download.
# This will take 5-15 minutes the first time. Subsequent runs are instant.
./vendor/qmd/bin/qmd collection add /tmp/qmd-test --db /tmp/qmd-test/index.sqlite
./vendor/qmd/bin/qmd embed --db /tmp/qmd-test/index.sqlite

# Confirm models downloaded
ls -lh ~/.cache/qmd/models/
```

While the download runs, tell the user:

> QMD is downloading three local LLM models (~2 GB total). This takes 5-15 minutes on a typical connection. The models are saved to `~/.cache/qmd/models/` and used entirely on your machine — no data is ever sent to a cloud service.
>
> If your terminal looks frozen, it's not. Wait for the prompt to return.

### 5. Verify QMD works end-to-end

```bash
# Run a query against the temp index. Should return a single hit.
./vendor/qmd/bin/qmd query "warm up" --db /tmp/qmd-test/index.sqlite --json -n 1
```

If the query returns valid JSON with one result, QMD is fully installed and working.

### 6. Cleanup the temp test

```bash
rm -rf /tmp/qmd-test
```

Models stay in `~/.cache/qmd/models/`. The temp index is deleted; the user's real index will be created in Stage 5.

### 7. Add `vendor/qmd/` to .gitignore (or commit it — user's choice)

Two options:

**Option A: Gitignore** (recommended for solo users — saves git size):

```bash
grep -qxF 'vendor/qmd/' .gitignore 2>/dev/null || echo 'vendor/qmd/' >> .gitignore
```

The user re-runs Stage 3 if they ever clone the repo onto a new machine.

**Option B: Commit** (recommended for shared brains — pins the version):

Skip the gitignore. The user will commit `vendor/qmd/` in Stage 9 cleanup.

Ask the user which they prefer. Default to Option A unless they say otherwise.

### 8. Report

```
## Stage 3 Install Report

- QMD version: [commit hash]
- Build: succeeded
- Binary: vendor/qmd/bin/qmd (executable: yes)
- Models downloaded: [list with sizes]
- Test query: passed
- vendor/qmd/ tracked in git: [yes / gitignored]
```

### 9. STOP

> **Stage 3 install complete.** QMD is installed locally and tested. The next stage is OPTIONAL — frontmatter tidying. If you want a small extra search-quality boost, paste `prompts/stage-4-frontmatter.md`. If you want to skip straight to indexing your archive, paste `prompts/stage-5-index.md`.

Do NOT run further commands until the user pastes the next prompt.
