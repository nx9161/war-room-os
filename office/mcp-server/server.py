#!/usr/bin/env python3
"""War Room Protocol MCP server.

Exposes the office — Sloane's 27-seat AI software office — to any
MCP-compatible agent (Claude Code, Cursor, Windsurf, Cline, and more).

Tools:
    activate   Full activation contract: what the agent must do to run
               the office.
    roster     Every seat: division, role, Marvel codename, mission.
    seat       Full employee file for one seat (by slug or name).
    playbook   A War Room playbook: war-room, intake, ship-feature,
               fix-ci.
    skill      A seat's skill (its operating manual).
    boardroom  Current boardroom notes (read-only).

Run:
    python3 server.py            # stdio transport (for MCP clients)
"""

import os
import re

from mcp.server.mcpserver import MCPServer

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

server = MCPServer(name="war-room-protocol", version="1.0.0")


def _read(*parts):
    path = os.path.join(ROOT, *parts)
    if not os.path.isfile(path):
        return None
    with open(path) as f:
        return f.read()


def _seat_slugs():
    d = os.path.join(ROOT, 'office', 'staff')
    return sorted(f[:-3] for f in os.listdir(d) if f.endswith('.md'))


def _seat_title(slug):
    with open(os.path.join(ROOT, 'office', 'staff', slug + '.md')) as f:
        return f.readline().lstrip('# ').strip().replace(
            ' — Employee File', '')


def _codename(slug):
    text = _read('office', 'staff', slug + '.md') or ''
    m = re.search(r'\*\*Agent name:\*\* (.+?) \(Marvel codename\)', text)
    return m.group(1) if m else ''


@server.tool(description="Full activation contract for running the War Room Protocol office.")
def activate() -> str:
    contract = _read('ACTIVATE.md') or ''
    return (contract
            + f"\n\nRoster: {len(_seat_slugs())} seats. "
              "Call roster() for the full table.")


@server.tool(description="List every seat: division, role, codename, mission.")
def roster() -> str:
    divisions = {}
    for slug in _seat_slugs():
        text = _read('office', 'staff', slug + '.md') or ''
        m = re.search(r'## Mission\n(.+?)(?:\n\n|\Z)', text, re.S)
        mission = (m.group(1).strip().split('\n')[0] if m else '')
        divisions.setdefault('office', []).append(
            f"- {_seat_title(slug)} ({_codename(slug)}): {mission}")
    # group by the canonical division order from the roster script
    order = ['product-owner', 'ui-ux-designer', 'business-analyst',
             'voice-designer', 'document-artisan', 'word-specialist',
             'excel-specialist', 'enterprise-architect', 'lead-backend-dev',
             'lead-frontend-dev', 'architecture-visualizer', 'mcp-maker',
             'appsec-lead', 'ai-red-teamer', 'global-tech-law-lead',
             'reverse-engineer', 'qa-manager', 'devops-sre', 'prompt-writer',
             'knowledge-wizard', 'general-counsel', 'game-architect',
             'gameplay-designer', 'game-ui-ux-designer',
             'console-platform-engineer', 'game-producer']
    lines = [f"# War Room Protocol — {len(_seat_slugs())} seats",
             "", "## Leadership", "- Sloane (Nick Fury): Chief Orchestrator"]
    return '\n'.join(lines + divisions['office'])


@server.tool(description="Full employee file for one seat. Pass the seat slug (e.g. 'qa-manager') or the role name.")
def seat(name: str) -> str:
    slug = name.strip().lower().replace(' ', '-')
    text = _read('office', 'staff', slug + '.md')
    if text is None:
        # try matching by title
        for s in _seat_slugs():
            if name.lower() in _seat_title(s).lower():
                return _read('office', 'staff', s + '.md')
        return f"Unknown seat '{name}'. Call roster() for the full list."
    return text


@server.tool(description="A War Room playbook. One of: war-room, intake, ship-feature, fix-ci.")
def playbook(name: str) -> str:
    slug = name.strip().lower().replace(' ', '-')
    text = _read('office', 'playbooks', slug + '.md')
    if text is None:
        return f"Unknown playbook '{name}'. Try: war-room, intake, ship-feature, fix-ci."
    return text


@server.tool(description="A seat's skill (its operating manual). Pass the seat slug, e.g. 'document-artisan'.")
def skill(name: str) -> str:
    slug = name.strip().lower().replace(' ', '-')
    text = _read('office', 'skills', slug, 'SKILL.md')
    if text is None:
        return f"No skill found for '{name}'. Call roster() for seat slugs."
    return text


@server.tool(description="Current boardroom notes (read-only).")
def boardroom() -> str:
    return _read('office', 'boardroom', 'board.md') or "(board is empty)"


if __name__ == '__main__':
    server.run()
