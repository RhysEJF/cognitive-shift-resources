# Troubleshooting

> Common issues that come up during the Second Brain Transplant to QMD, and how to fix them. If your situation isn't here, reach out: https://x.com/virtual_rf

---

## Stage 1 (Audit) issues

### "I'm not sure if my dir is auto-grown or hand-curated"

The classifier in Stage 1 uses these signals:

- **Auto-grown**: many small files (>10), each with structured content (headings, similar shape), often timestamped or hash-named
- **Hand-curated**: few files (<5), long-form content you wrote in one sitting, slow-changing
- **Custom**: anything that doesn't match either pattern AND isn't a Flow OS default

If a dir is genuinely ambiguous, flag it as `unknown` and ask the user. Don't guess — the classification controls whether QMD indexes it and whether /learn writes to it.

### "Audit reports `.flow/migration.lock` exists"

A previous transplant or migration didn't finish cleanly. Either:

1. The earlier run is still going (rare — check process list)
2. The earlier run crashed and left the lock behind

If neither is true:

```bash
rm .flow/migration.lock
```

Then re-run Stage 1.

---

## Stage 2 (Backup) issues

### "git status reports uncommitted changes"

This is good — it stopped you from clobbering work in progress. Decide:

- Commit them: `git add -A && git commit -m "checkpoint before transplant"`
- Stash: `git stash`
- Discard: `git restore .` (only if you're sure)

### "I don't have git and don't want it"

The tarball backup mode works. You lose easy point-in-time rollback but you do get a snapshot. Re-run Stage 2 and choose tarball mode.

### "Backup branch was created but push to origin failed"

Probably no remote configured, or auth failed. Check:

```bash
git remote -v
```

If empty, the local branch is still your safety net. You just don't have an off-machine copy. That's fine for the transplant; you can add a remote any time.

---

## Stage 3 (Install QMD) issues

### "node --version reports 22+, but npm install fails with engine errors"

Check `which node` and `which npm` resolve to the same Node version. Node version managers (nvm, fnm, volta) sometimes have a misaligned `npm` bin. Try:

```bash
which node
which npm
node -e "console.log(process.versions.node)"
```

If they don't agree, fix the PATH. On macOS this often means the shell is finding `/usr/local/bin/node` (an old global Node) before the version manager's bin.

### "QMD download started but seems stuck"

The model downloads can be slow on the first run. Each model is a single large file (300 MB to 1.1 GB), so progress feels lumpy. Check:

```bash
ls -lh ~/.cache/qmd/models/
```

If the file is growing, it's working. If it's been zero bytes for >5 minutes, the connection died. Retry `qmd embed`.

### "The build succeeded but `qmd query` says 'no models loaded'"

Models download lazily on first query, not on build. The first query may take 10+ minutes while it pulls 2 GB. Subsequent queries are fast.

---

## Stage 4 (Frontmatter) issues

### "I approved a batch and now I want to undo it"

You're on a separate branch (`stage-4-frontmatter-tidy`). Just abort:

```bash
git checkout main
git branch -D stage-4-frontmatter-tidy
```

You're back to the pre-Stage-4 state. Restart Stage 4 if you want to retry with different choices.

### "The proposed entity slug is wrong"

When the agent shows you the per-file table before writing a batch, you can correct any row. Tell it specifically: "for file X, change entity from 'untitled' to 'tom-parker'". The agent should re-generate the proposed frontmatter for that row before writing.

### "I have a custom dir under memory/ that the agent didn't recognise"

That's fine — Stage 4 is opt-in per dir. Tell the agent: "include `memory/<your-custom-dir>/` in this stage" and it'll add it to the in-scope list.

---

## Stage 5 (Index) issues

### "`qmd embed` ran but `qmd query` returns nothing"

Check:

```bash
./vendor/qmd/bin/qmd status
./vendor/qmd/bin/qmd collection list
```

If collections are listed but file counts are zero, the dirs were registered but not indexed. Run `qmd embed` again.

If collections are empty, your `qmd collection add` calls didn't take. Re-add them.

### "Embeddings are taking forever"

Real archives can have thousands of chunks. The embedding model runs locally on CPU by default; that's slow. Each chunk takes 200-500ms. For 10,000 chunks, that's 30-80 minutes.

Patience is the only fix unless you have GPU acceleration set up (which is beyond the scope of this transplant).

### "Some files were indexed but not others"

QMD only indexes files inside registered collections. Run `qmd collection list` and check that every dir you expected is there. If a custom dir is missing, add it: `qmd collection add memory/<your-dir>/`.

### "I want to exclude a specific dir from the index"

Use `.flow/qmd-exclude.txt` (Stage 5 creates this). Add a line per excluded path. Re-run `qmd embed`.

---

## Stage 6 (Validate) issues

### "QMD's top result is wrong even though I know the answer is in there"

Three common causes:

1. **The answer file lacks frontmatter**, AND the body uses different vocabulary than the query. Run Stage 4 (opt-in) to add entity slugs and topic tags to the file. Re-index. Re-query.

2. **The answer file IS indexed but the reranker drifted**. Look at the top 5 results — is the right file at rank 2 or 3? If yes, this is a known QMD reranker quirk on long natural-language queries. Try a shorter, more focused query phrasing.

3. **The dir containing the answer wasn't registered as a collection**. Run `qmd collection list` and verify.

### "Query returns ONE result and that's it"

You probably set `-n 1` somewhere or there are very few documents indexed. Try:

```bash
./vendor/qmd/bin/qmd query "<query>" --json -n 10
./vendor/qmd/bin/qmd status
```

---

## Stage 7 (Wire commands) issues

### "After replacing grep with qmd query, /learn behaves weirdly"

Most likely cause: the grep call was doing something specific (like extracting a particular line, piping to jq, etc.) and the qmd-query equivalent doesn't preserve that pipeline.

Restore from backup:

```bash
cp .claude/commands/learn.md.pre-qmd-backup .claude/commands/learn.md
```

Then look at what the original grep was actually doing. Sometimes the right move is to keep grep for that one specific use case (e.g., scanning frontmatter fields) and only swap grep→qmd for the body-search calls.

### "I want Claude Desktop to also use my QMD index"

This transplant focuses on Claude Code. If you also want Claude Desktop to query the same brain via QMD's MCP server, see the [QMD repo's MCP docs](https://github.com/tobi/qmd) — the install is straightforward: register the QMD binary as an MCP server in `claude_desktop_config.json`, point it at your index, restart Claude Desktop. Common gotcha: use the absolute path to `node` (Claude Desktop's launch shell often can't find version-manager Node binaries).

---

## Stage 8 (Brand) issues

### "I want to change the wording of the Memory Layer section"

Edit it. The branding is plain markdown. Customise to your voice. Just keep some form of attribution if you're shipping the transplant template forward — that's the social contract.

### "I don't want the stuck-user heuristic"

Delete that section. The agent will just behave normally.

---

## Stage 9 (Cleanup) issues

### "I cleaned up but now I want to roll back"

If you didn't push the backup branch to a remote, your local branch is gone but the commits are still in git's reflog for ~30 days:

```bash
git reflog
# Find the pre-transplant commit
git checkout <hash>
git checkout -B recovered-pre-transplant
```

If you also pruned reflog or it's been >30 days, the only recovery is your remote (if you pushed) or your tarball.

If you have neither, you can't undo Stage 9. That's the trade-off this stage makes.

---

## General issues

### "Memory writes during /learn aren't routing to the right dirs"

This is the bug Karan hit before Rhys patched it. Symptoms: every memory lands in `memory/<YYYY>/<MM>/` regardless of type or entity.

Fix: confirm your `.claude/commands/learn.md` has the **Path Routing table** in Step 4 and the **Customer-Specific Routing** subsection. If it doesn't, your /learn is on a pre-fix version. Pull the current one from `https://github.com/RhysEJF/flow-os-v2/blob/main/.claude/commands/learn.md`.

### "The article promised this would take an hour. It's been three."

The first migration is always the slowest. Possible time sinks:

- Model downloads (Stage 3): one-time, 5-15 minutes
- Embedding generation (Stage 5): scales with archive size; 10-60 minutes for typical archives
- Frontmatter (Stage 4): scales with file count + your reading speed for diffs
- Wiring (Stage 7): 5-15 minutes

Your second migration on a different machine is much faster — models are cached, you know the rhythm, you skip Stage 4.

### "My second brain is too weird for these prompts"

Reach out: https://x.com/virtual_rf. Genuinely weird setups are the most interesting. If your shape doesn't fit the prompts, the prompts probably need to grow.
