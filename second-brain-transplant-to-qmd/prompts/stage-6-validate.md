# Stage 6 — Validate

> Runs three real queries against your archive, plus an A/B comparison against grep. Confirms the search quality is genuinely better before you wire QMD into your daily workflow. Paste this entire prompt into your AI agent.

---

You are starting Stage 6 of the Second Brain Transplant to QMD. Your job: prove the upgrade works for the user's specific archive. If queries return junk, we stop here and figure out why.

## Critical rules

- This stage is read-only.
- Run each query through both grep and QMD and show the comparison side-by-side.
- If three queries in a row return obviously bad QMD results, STOP and surface the issue. Do not wave the user through a broken index.

## What to do

### 1. Set up

```bash
QMD=./vendor/qmd/bin/qmd
```

### 2. Three test queries

The user picks three queries from these categories. They should be queries with answers the user KNOWS exist in their archive. Otherwise we can't tell if QMD is right or wrong.

Ask the user:

> Pick one query from each category. Each should be something you know is in your archive — that way we can tell if QMD finds it.
>
> 1. **Person query** — a fuzzy question about someone in your network. Don't use the person's name; describe them. Example: "Who was that founder I met who runs an AI infrastructure company?"
>
> 2. **Insight query** — something you wrote down once and want to find again. Don't use the exact words. Example: "What did I conclude about pricing when prospects push back?"
>
> 3. **Project/venture query** — something tied to a specific project. Example: "What was the decision I made about onboarding for [specific venture]?"

Wait for them to provide all three.

### 3. Run each query through grep AND QMD

For each query, run both:

```bash
QUERY="<the user's query>"

echo "=== GREP RESULTS ==="
# Pick 1-2 keywords from the query naively. Don't be clever.
grep -ril "$NAIVE_KEYWORDS" memory/ experiences/ 2>/dev/null | head -5

echo ""
echo "=== QMD RESULTS ==="
$QMD query "$QUERY" --json -n 5
```

### 4. Show the user side-by-side

For each query, present:

```
QUERY: "<user's words>"

GREP returned: N files
[file paths]

QMD returned: 5 ranked results
[Result 1: file, score, snippet]
[Result 2: file, score, snippet]
[etc.]
```

Ask the user:

> For this query, did QMD's top 1-2 results actually contain the answer you were thinking of? (Yes / Partial / No)

Record the answer. Move to next query.

### 5. Tally and decide

After all three queries:

| Query | Grep useful? | QMD useful? |
|---|---|---|
| 1 (person) | Yes/No | Yes/Partial/No |
| 2 (insight) | Yes/No | Yes/Partial/No |
| 3 (project) | Yes/No | Yes/Partial/No |

**Pass criteria:** at least 2 of 3 QMD queries return "Yes" in the top 1-3 results.

**If pass:** advance to Stage 7.

**If fail:** STOP. The most common causes:
- The relevant files were excluded from the index (check Stage 5 collection list)
- The relevant files have no frontmatter AND the body uses different vocabulary than the query (Stage 4 might fix this)
- The reranker drifted (rare; usually a sign the index is too small or the query is highly abstract)

Tell the user:

> Validation didn't pass cleanly. Don't proceed to Stage 7 yet. Either:
> 1. Run Stage 4 (frontmatter tidy) if you skipped it — high-signal frontmatter often rescues semantic queries
> 2. Check `troubleshooting.md` for index-coverage debugging
> 3. Reach out to Rhys: https://x.com/virtual_rf

### 6. (Optional) Run the article's "before/after" benchmark

If the user wants to publish their own version of the comparison, this is the moment to capture it:

```bash
QUERY="<a fuzzy-but-answerable query, ideally one whose answer would be a person not their name>"

echo "=== GREP ==="
grep -ril "naive_keyword_1\|naive_keyword_2" memory/ experiences/

echo ""
echo "=== QMD ==="
$QMD query "$QUERY" --json -n 5
```

Save the output to `experiences/captures/qmd-validation-<date>.md` if the user wants to keep evidence.

### 7. Report

```
## Stage 6 Validation Report

- Query 1 (person): grep [X], qmd [Y]
- Query 2 (insight): grep [X], qmd [Y]
- Query 3 (project/venture): grep [X], qmd [Y]
- Pass: [yes / no]
- Notes: [anything weird, edge cases, files that didn't surface but should have]
```

### 8. STOP

> **Stage 6 validation complete.** [Pass / Fail message]
>
> If passed, paste `prompts/stage-7-wire-claude-code.md` to wire Claude Code's commands to QMD.

Do NOT run further commands until the user pastes the next prompt.
