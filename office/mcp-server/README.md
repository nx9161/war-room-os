# War Room Protocol MCP Server

One server, every agent. Exposes Sloane's 43-seat AI software office across 7 divisions to
any MCP-compatible client: Claude Code, Cursor, Windsurf, Cline, Zed,
and anything else that speaks MCP.

## Run it

```bash
pip install -r requirements.txt
python3 server.py        # stdio transport
```

## Connect your agent

Add to your MCP client config (`claude_desktop_config.json`,
Cursor's `mcp.json`, Windsurf, Cline, ...):

```json
{
  "mcpServers": {
    "war-room-protocol": {
      "command": "python3",
      "args": ["/path/to/war-room-protocol/office/mcp-server/server.py"]
    }
  }
}
```

Or point at the repo directly — no clone needed if your client
supports remote git MCP servers.

## Tools

| Tool | What it does |
|---|---|
| `activate` | Full activation contract — what the agent must do to run the office |
| `roster` | Every seat: division, role, Marvel codename, mission |
| `seat` | Full employee file for one seat (slug or name) |
| `playbook` | `war-room`, `intake`, `ship-feature`, or `fix-ci` |
| `skill` | A seat's skill — its operating manual |
| `boardroom` | Current boardroom notes (read-only) |

Typical first calls: `activate`, then `roster`. The office stays active
until the user says "End War Room Protocol".
