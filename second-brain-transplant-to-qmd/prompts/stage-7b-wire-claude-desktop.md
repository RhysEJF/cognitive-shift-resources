# Stage 7b — Wire Claude Desktop

> Installs QMD as an MCP (Model Context Protocol) server in Claude Desktop, so the desktop app can query your second brain just like Claude Code does. Run only if you use Claude Desktop. Paste this entire prompt into your AI agent.

---

You are starting Stage 7b. Your job: register the QMD binary as an MCP server in Claude Desktop's config, point it at the user's index, and verify the desktop app can query it.

## Critical rules

- The user's existing `claude_desktop_config.json` may have other MCP servers configured (Drive, Gmail, etc.). DO NOT replace the file. Add the QMD entry alongside.
- Back up `claude_desktop_config.json` before modifying.
- After editing, the user must restart Claude Desktop for changes to take effect.

## What to do

### 1. Locate `claude_desktop_config.json`

Default locations:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

```bash
CONFIG_PATH="$HOME/Library/Application Support/Claude/claude_desktop_config.json"   # macOS default
# Adjust per OS
ls -la "$CONFIG_PATH" 2>/dev/null
```

If the file doesn't exist, Claude Desktop hasn't been configured before. Create an empty one:

```bash
mkdir -p "$(dirname "$CONFIG_PATH")"
echo '{"mcpServers": {}}' > "$CONFIG_PATH"
```

### 2. Backup

```bash
cp "$CONFIG_PATH" "$CONFIG_PATH.pre-qmd-backup"
ls -la "$CONFIG_PATH.pre-qmd-backup"
```

### 3. Inspect existing MCP servers

```bash
cat "$CONFIG_PATH" | python3 -m json.tool | head -50
```

List the existing entries under `mcpServers`. Confirm none of them are already a QMD entry.

### 4. Confirm Node path

QMD's MCP server runs via Node. Claude Desktop launches MCP servers with the system PATH at app-launch time, which on macOS often DOESN'T include `nvm`/`fnm`/`volta` paths. Get the absolute path:

```bash
which node
# Confirm output is something like /usr/local/bin/node, /opt/homebrew/bin/node,
# or /Users/<you>/.nvm/versions/node/v22.x.x/bin/node — NOT just "node"
```

If `which node` returns a path inside a version manager (`.nvm`, `.fnm`, `.volta`, `.nodenv`), Claude Desktop probably can't find it. Tell the user:

> Your Node is managed by [nvm/fnm/etc.]. Claude Desktop launches MCP servers with the bare system PATH and won't find Node there. Two options:
> 1. Symlink Node to a system path: `sudo ln -s $(which node) /usr/local/bin/node`
> 2. Use the absolute path in the config below
>
> Going with option 2 by default.

### 5. Add the QMD entry

Get the absolute path to the QMD binary (from Stage 3's vendor install):

```bash
QMD_BIN="$(pwd)/vendor/qmd/bin/qmd"
NODE_BIN="$(which node)"
ls -la "$QMD_BIN"
```

Edit `claude_desktop_config.json` to add the QMD MCP server. Use Python to do the JSON edit safely (avoids hand-edit mistakes):

```bash
python3 <<EOF
import json
path = "$CONFIG_PATH"
with open(path) as f:
    config = json.load(f)
config.setdefault("mcpServers", {})
config["mcpServers"]["qmd"] = {
    "command": "$NODE_BIN",
    "args": ["$QMD_BIN", "mcp"],
    "env": {}
}
with open(path, "w") as f:
    json.dump(config, f, indent=2)
print("Added qmd MCP server")
EOF

# Show the new state
cat "$CONFIG_PATH" | python3 -m json.tool
```

### 6. Test the MCP server (optional but recommended)

Run the MCP server directly to confirm it starts cleanly:

```bash
echo '{"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2024-11-05"}, "id": 1}' | "$NODE_BIN" "$QMD_BIN" mcp 2>&1 | head -5
```

You should see a JSON response with the server info. If you see "Cannot find module" or similar errors, the Node binary path is wrong — go back to step 4.

### 7. Restart Claude Desktop

Tell the user:

> Quit Claude Desktop completely (Cmd-Q on macOS, not just close the window) and reopen it. The QMD tools should appear in the MCP tools list.
>
> To verify: in Claude Desktop, ask Claude something like "use qmd to search for [query]" — it should call the MCP server and return results.

Wait for them to confirm. Don't proceed until they've actually tested it.

### 8. (Optional) Add a CLAUDE-desktop.md identity file

If the user wants Claude Desktop to behave consistently with Claude Code:

```bash
# Copy from CLAUDE.md but rename for clarity
[ -f CLAUDE.md ] && cp CLAUDE.md CLAUDE-desktop.md
```

Add to CLAUDE-desktop.md a note about searching via the QMD MCP tool:

```markdown
## Search

Use the `qmd` MCP tool to search this brain. Three modes:
- `qmd query` — hybrid (best, ~10s)
- `qmd search` — BM25 only (fast)
- `qmd vsearch` — vector only

The brain lives at `[absolute path to repo]`.
```

### 9. Report

```
## Stage 7b Wire Report

- Config path: [CONFIG_PATH]
- Backup: $CONFIG_PATH.pre-qmd-backup
- Node binary: [absolute path]
- QMD binary: [absolute path]
- MCP server registered: yes
- Claude Desktop restarted + verified: [yes / pending]
- CLAUDE-desktop.md created: [yes / no]
```

### 10. STOP

> **Stage 7b complete.** Claude Desktop can now query your brain via QMD. If you also use Claude Code, paste `prompts/stage-7a-wire-claude-code.md`. Otherwise paste `prompts/stage-8-brand-the-upgrade.md`.

Do NOT run further commands until the user pastes the next prompt.
