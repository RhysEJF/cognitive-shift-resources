# Second Brain Transplant to QMD

> Upgrade your AI Second Brain's search layer from grep to hybrid (BM25 + vector + LLM reranker). Your markdown stays put. Your folder structure stays put. Your AI gets dramatically better at finding what you wrote.

This is the companion to the article [Your AI Second Brain Has a Quiet Search Problem](https://thecognitiveshift.com/let-them-run/your-ai-second-brain-has-a-quiet-search-problem). If you haven't read it, the short version is: most second brain templates use grep underneath, and grep can only find what you already remember the exact words for. This transplant fixes that.

---

## What you'll end up with

- A local hybrid search engine ([QMD](https://github.com/tobi/qmd) by Tobi Lütke) running entirely on your machine
- All your existing markdown files indexed and searchable by meaning, not just keyword match
- A routing layer (Flow OS, the small piece on top) that decides where new memories go when /learn writes them
- Your existing AI workflow (Claude Code, Claude Desktop, custom GPT, whatever) wired to use QMD instead of grep
- A small attribution footer in your README and a Memory Layer section in your CLAUDE.md (removable any time)

---

## Who this is for

Second Brain users running on **Claude Code**. Specifically:

- Your notes are markdown files in a folder
- A CLAUDE.md tells Claude how to behave
- Your current search is grep or basic keyword matching


If you also use Claude Desktop alongside Claude Code, Stage 7b wires that up too. If you're on a different agent host entirely, Stage 7c provides a generic fallback.

You need:

- A folder of markdown files (your second brain)
- Claude Code installed and working with it today
- Node 22+ on your machine (QMD requires it)
- About 2 GB of disk space (for the local LLM models QMD downloads on first run)

You do NOT need:

- A specific folder structure
- Existing frontmatter in your notes
- Any Flow OS files (CLAUDE.md, .claude/commands/, .flow/, etc.)
- Cloud services, API keys, or a server

---

## Time and risk

**Time:** about 30-60 minutes of mostly waiting. The first index after install can take 10-30 minutes depending on archive size (your AI session can be on autopilot during this).

**Risk:** low if you follow the stages in order. Stages 1-7 are reversible. Stage 9 (cleanup) removes safety nets, so do that last and only after confirmed-stable use.

**Backups:** Stage 2 always creates a git branch snapshot. If you don't have git in your second brain repo, the prompt sets it up first. No file is touched anywhere before Stage 2 finishes.

---

## How this is structured

Each stage is a separate prompt file in `prompts/`. You paste one prompt at a time into your AI agent, watch what it does, approve before continuing to the next.

This is deliberately not a single mega-prompt. Memory data is sensitive. A bad agent run on a 5-year archive of newsletters or client notes can ruin a week. The staged approach lets you stop and roll back at any point.

### The stages

| # | Stage | What it does | Reversible? |
|---|---|---|---|
| 1 | [Audit](prompts/stage-1-audit.md) | Reads your repo, classifies what's there, surfaces non-standard structure | Yes (read-only) |
| 2 | [Backup](prompts/stage-2-backup.md) | Creates a git branch snapshot (or initialises git first if needed) | Yes (always) |
| 3 | [Install QMD](prompts/stage-3-install-qmd.md) | Pulls the QMD binary, downloads the local LLM models | Yes (delete the binary + cache) |
| 4 | [Frontmatter tidy (OPT-IN)](prompts/stage-4-frontmatter.md) | Adds id/type/entities/topics to files that lack them. Skip if you want raw markdown only | Yes (until cutover) |
| 5 | [Index](prompts/stage-5-index.md) | First QMD index of your archive. Generates embeddings. | Yes (delete `~/.cache/qmd/`) |
| 6 | [Validate](prompts/stage-6-validate.md) | Runs real queries against your archive. Confirms search quality. | Yes (read-only) |
| 7a | [Wire Claude Code](prompts/stage-7a-wire-claude-code.md) | Replaces grep calls in your /plan and /learn with qmd query | Yes (restore from backup branch) |
| 7b | [Wire Claude Desktop](prompts/stage-7b-wire-claude-desktop.md) | Installs QMD as an MCP server in Claude Desktop | Yes (edit `claude_desktop_config.json` back) |
| 7c | [Wire other agents (fallback)](prompts/stage-7c-wire-custom-gpt.md) | Generic CLI wrapper for non-Claude agents. Skip if you're on Claude Code or Desktop. | Yes (delete the wrapper) |
| 8 | [Memory Layer note](prompts/stage-8-memory-layer-note.md) | Adds a small Memory Layer section to your README and CLAUDE.md so future Claude sessions know what's running | Yes |
| 9 | [Cleanup](prompts/stage-9-cleanup.md) | Removes backup branch and staging files. Only after stable use. | Manual (re-create branch from history) |

You only do ONE of stage 7a / 7b / 7c (or several if you use multiple agents). Pick the one that matches your host.

---

## How to start

1. Open your second brain repo in your AI agent (Claude Code recommended)
2. Open `prompts/stage-1-audit.md` in this repo
3. Paste its contents as your first message to the agent
4. Watch the audit output, approve before proceeding
5. Repeat for stage 2, stage 3, etc.

If anything looks wrong mid-stage, type `STOP` to your agent and check `troubleshooting.md`. Most issues are recoverable in seconds if you catch them early.

---

## What gets touched, what doesn't

**Touched (with explicit approval per stage):**

- A new directory `vendor/qmd/` or similar (the QMD binary location)
- A new directory `~/.cache/qmd/` (the index file and downloaded LLM models, outside your repo)
- Optionally: frontmatter added to your existing markdown files (Stage 4, opt-in only)
- Your AI agent's command files (Stage 7) — only the specific lines that call grep
- Your README and CLAUDE.md — a small Memory Layer section gets appended so future Claude sessions know what's running. Removable any time.

**Never touched:**

- The body content of any of your existing markdown notes (frontmatter only, and only with approval)
- Any file outside your second brain repo (except `~/.cache/qmd/` for the index)
- Hand-curated profile dirs (`memory/personal/`, `memory/values-beliefs/`, `memory/style-voice/`, `memory/audience/`, `memory/examples/`, `memory/company/`, `memory/knowledge-sources/`) — Flow OS-style profile dirs are recognised and excluded automatically

---

## Help

- General confusion: see [troubleshooting.md](troubleshooting.md)
- Bug in the prompts themselves: open an issue at [cognitive-shift-resources](https://github.com/RhysEJF/cognitive-shift-resources/issues)
- Want a hand from a human: [Rhys helps directly](https://x.com/virtual_rf)

---

🧠 Memory retrieval upgrade by [Rhys Fisher](https://x.com/virtual_rf). Built on [QMD](https://github.com/tobi/qmd) by Tobi Lütke.
