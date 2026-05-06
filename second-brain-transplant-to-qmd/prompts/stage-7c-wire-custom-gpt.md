# Stage 7c — Wire Custom GPT or Other Agent

> Provides a small wrapper script for any AI host that can shell out (custom GPT via Code Interpreter, Replit AI agents, Cursor, hand-rolled agents, etc.). Paste this entire prompt into your AI agent.

---

You are starting Stage 7c. Your job: create a thin wrapper that exposes QMD's three search modes through a stable interface, plus a one-page README explaining how to wire it into the user's specific agent.

## Critical rules

- Don't assume the user's agent supports MCP. This stage is the fallback for everything that doesn't.
- The wrapper should be stable, well-documented, and respect the user's existing repo conventions.

## What to do

### 1. Create the wrapper script

```bash
mkdir -p scripts
cat > scripts/qmd-search.sh <<'WRAP'
#!/usr/bin/env bash
# scripts/qmd-search.sh
#
# Thin wrapper around QMD for AI agents that shell out to commands.
# Usage:
#   ./scripts/qmd-search.sh query "natural-language question"
#   ./scripts/qmd-search.sh search "exact keywords"
#   ./scripts/qmd-search.sh vsearch "semantic phrasing"
#
# Returns JSON to stdout. Each result has: file, score, snippet, title.

set -euo pipefail

MODE="${1:-query}"
shift || true
TEXT="${*:-}"

if [ -z "$TEXT" ]; then
  echo "Usage: $0 [query|search|vsearch] <text>" >&2
  exit 1
fi

QMD="$(cd "$(dirname "$0")/.." && pwd)/vendor/qmd/bin/qmd"

if [ ! -x "$QMD" ]; then
  echo "QMD binary not found at $QMD. Did you run Stage 3?" >&2
  exit 1
fi

case "$MODE" in
  query)   exec "$QMD" query "$TEXT" --json -n 5 ;;
  search)  exec "$QMD" search "$TEXT" --json -n 10 ;;
  vsearch) exec "$QMD" vsearch "$TEXT" --json -n 10 ;;
  *) echo "Unknown mode: $MODE (expected query, search, or vsearch)" >&2; exit 1 ;;
esac
WRAP

chmod +x scripts/qmd-search.sh
```

Test it:

```bash
./scripts/qmd-search.sh query "test" | head -5
```

You should see JSON output. If not, fix before proceeding.

### 2. Detect the user's host and write integration notes

Ask the user:

> Which agent are you wiring this into? Pick one or describe yours:
> 1. Custom GPT (OpenAI) with Code Interpreter
> 2. Cursor
> 3. Replit AI agent
> 4. Hand-rolled agent (Anthropic SDK, OpenAI SDK, etc.)
> 5. Something else (describe it)

Based on their answer, write a short integration recipe. Examples below.

#### Custom GPT (OpenAI)

```markdown
## Wiring QMD into your custom GPT

OpenAI custom GPTs can call shell commands via the Code Interpreter tool.
In your GPT's instructions, add:

> When the user asks something that requires looking up past notes, use the
> Code Interpreter to execute:
>
>   ./scripts/qmd-search.sh query "<the user's question>"
>
> Parse the JSON response. The top result is usually the most relevant.
> Cite the `file` field when referencing remembered material.

Note: Code Interpreter runs in OpenAI's sandbox, NOT on the user's machine.
For QMD to be reachable, you must either:
1. Mount the repo into the sandbox via the GPT's file uploads (limited)
2. Run the GPT on a custom backend that has access to the repo

For full local-first usage, prefer Claude Code or Claude Desktop with QMD MCP.
```

#### Cursor

```markdown
## Wiring QMD into Cursor

Cursor's AI can shell out via its built-in terminal. Add to your project's
`.cursor/rules` or equivalent:

> Before answering questions about anything in this codebase or in the
> linked memory directories, run:
>
>   ./scripts/qmd-search.sh query "<the user's question>"
>
> Use the top 3 results as context.
```

#### Hand-rolled agent (Anthropic SDK / OpenAI SDK)

```markdown
## Wiring QMD into a custom agent

Add a tool definition that shells out to qmd-search.sh:

\`\`\`python
import subprocess
import json

def qmd_search(query: str, mode: str = "query") -> list[dict]:
    """Search the user's second brain. Returns ranked results."""
    out = subprocess.run(
        ["./scripts/qmd-search.sh", mode, query],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)

# Register as a tool the agent can call
tools = [{
    "name": "qmd_search",
    "description": "Search the user's second brain. Use 'query' for natural-language questions, 'search' for exact keywords.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "mode": {"type": "string", "enum": ["query", "search", "vsearch"], "default": "query"}
        },
        "required": ["query"]
    }
}]
\`\`\`
```

Write the matching recipe to `scripts/qmd-search.README.md`.

### 3. Smoke test through the host

Have the user trigger a search through their actual agent. Confirm the agent reaches the wrapper, the wrapper reaches QMD, and results come back.

### 4. Commit

```bash
git add scripts/qmd-search.sh scripts/qmd-search.README.md
git commit -m "stage-7c: add qmd-search.sh wrapper for non-Claude-Code agents"
```

### 5. Report

```
## Stage 7c Wire Report

- Wrapper script: scripts/qmd-search.sh
- Integration recipe: scripts/qmd-search.README.md
- Host: [user's choice]
- Smoke test: [passed / failed / skipped]
```

### 6. STOP

> **Stage 7c complete.** Your custom agent can now reach QMD via the wrapper. Paste `prompts/stage-8-brand-the-upgrade.md` to continue.

Do NOT run further commands until the user pastes the next prompt.
