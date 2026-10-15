#!/usr/bin/env python3
"""Regenerate the roster table in README.md from office/staff/.

The README's roster section (between <!-- ROSTER:START --> and
<!-- ROSTER:END -->) is generated — never hand-edit it. Run this after
adding, removing, or renaming a seat:

    python3 office/scripts/sync-readme-roster.py
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)

DIVISIONS = {
    'Product & UX': ['product-owner', 'ui-ux-designer', 'business-analyst',
                     'voice-designer', 'document-artisan', 'word-specialist',
                     'excel-specialist', 'diagram-designer',
                     'art-director', 'launch-strategist',
                     'sales-agent', 'scriptwriter',
                     'product-visualizer'],
    'Architecture & Code': ['enterprise-architect', 'lead-backend-dev',
                            'lead-frontend-dev', 'architecture-visualizer',
                            'mcp-maker', 'lead-code-reviewer',
                            'harness-engineer'],
    'Security & Compliance': ['appsec-lead', 'ai-red-teamer',
                              'global-tech-law-lead', 'reverse-engineer',
                              'penetration-tester'],
    'Quality & Ops': ['qa-manager', 'devops-sre', 'prompt-writer',
                      'knowledge-wizard', 'memory-keeper',
                      'mission-control',
                     'casting-director'],
    'Legal & Governance': ['general-counsel'],
    'Games': ['game-architect', 'gameplay-designer', 'game-ui-ux-designer',
              'console-platform-engineer', 'game-producer'],
}


def seat_name(slug):
    with open(os.path.join(REPO, 'office', 'staff', slug + '.md')) as f:
        title = f.readline().lstrip('# ').strip()
    return title.replace(' — Employee File', '')


def main():
    staff = os.path.join(REPO, 'office', 'staff')
    on_disk = {f[:-3] for f in os.listdir(staff) if f.endswith('.md')}
    mapped = {s for slugs in DIVISIONS.values() for s in slugs} | {'sloane'}
    if on_disk != mapped:
        missing = on_disk - mapped
        extra = mapped - on_disk
        sys.exit(f'roster drift! unmapped: {sorted(missing)} missing: {sorted(extra)}')

    total = len(mapped)
    rows = []
    for div, slugs in DIVISIONS.items():
        names = ', '.join(seat_name(s) for s in slugs)
        rows.append(f'| {div} | {names} |')
    rows.append('| **Leadership** | **Sloane (Chief Orchestrator)** |')

    table = ('**The seats — %d roles, 6 divisions.**\n\n'
             '| Division | Seats |\n|---|---|\n%s'
             % (total, '\n'.join(rows)))

    readme = os.path.join(REPO, 'README.md')
    with open(readme) as f:
        content = f.read()
    pattern = re.compile(r'<!-- ROSTER:START -->.*?<!-- ROSTER:END -->', re.S)
    replacement = '<!-- ROSTER:START -->\n' + table + '\n<!-- ROSTER:END -->'
    new, n = pattern.subn(replacement, content)
    if n != 1:
        sys.exit('roster markers not found exactly once in README.md')
    with open(readme, 'w') as f:
        f.write(new)
    print(f'roster synced: {total} roles')


if __name__ == '__main__':
    main()
