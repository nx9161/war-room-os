#!/usr/bin/env python3
"""Convert every roster slug into a proper AI agent skill.

Every seat in office/staff/<slug>.md must exist as an installable agent
at office/skills/<slug>/SKILL.md whose YAML frontmatter names the slug.
This script enforces that:

    python3 office/scripts/sync-seat-agents.py           # convert/fix
    python3 office/scripts/sync-seat-agents.py --check   # report drift only

For a seat with no skill yet, the agent is generated from its staff
file (mission, responsibilities, standards, authority carry over).
For a skill that exists but has no frontmatter, the standard seat
frontmatter is prepended and the body is left untouched. Skills that
already conform are never modified.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)
STAFF = os.path.join(REPO, 'office', 'staff')
SKILLS = os.path.join(REPO, 'office', 'skills')


def parse_staff(path):
    with open(path) as f:
        text = f.read()
    title = text.splitlines()[0].lstrip('# ').strip()
    role = title.replace(' — Employee File', '').split(' — ')[0].strip()
    m = re.search(r'\*\*Agent name:\*\*\s*(.+?)(?:\s*\(Marvel codename\))?\s*$',
                  text, re.M)
    codename = m.group(1).strip() if m else role
    mission = ''
    mm = re.search(r'## Mission\s*\n(.*?)(?:\n## |\Z)', text, re.S)
    if mm:
        flat = ' '.join(mm.group(1).split()).replace('*', '')
        first = re.split(r'(?<=[.!?])\s+', flat)[0].rstrip('.')
        if len(first) > 150:
            first = first[:150].rsplit(' ', 1)[0].rstrip(',;:')
        mission = first
    return role, codename, mission, text


def frontmatter(slug, role, codename, mission):
    desc = f'{role} ({codename}): {mission}. ' \
           'Dispatch when the War Room seats this role.'
    # The description contains ": " after the codename, so it must be a
    # quoted scalar or strict YAML parsers reject the frontmatter.
    return (f'---\nname: {slug}\ndescription: {json.dumps(desc)}\n'
            f'license: MIT\n'
            f'metadata:\n  seat: {role}\n  codename: {codename}\n'
            '  version: 1.0.0\n---\n\n')


def body_from_staff(role, codename, text):
    lines = text.splitlines()
    kept = []
    for line in lines[1:]:  # drop the title line
        if line.startswith('**Agent name:**'):
            continue
        kept.append(line)
    body = '\n'.join(kept).strip('\n')
    header = (f'# {role} — {codename}\n\n'
              f"This skill is {codename}'s operating manual: the seat's "
              'method, standards, and binding rules. When the War Room '
              'seats this role, work from this skill.\n\n')
    return header + body + '\n'


def main():
    check_only = '--check' in sys.argv
    slugs = sorted(f[:-3] for f in os.listdir(STAFF) if f.endswith('.md'))
    created, fixed, ok, drift = [], [], [], []
    for slug in slugs:
        role, codename, mission, text = parse_staff(
            os.path.join(STAFF, slug + '.md'))
        skill_dir = os.path.join(SKILLS, slug)
        skill = os.path.join(skill_dir, 'SKILL.md')
        if not os.path.exists(skill):
            drift.append(slug)
            if not check_only:
                os.makedirs(skill_dir, exist_ok=True)
                with open(skill, 'w') as f:
                    f.write(frontmatter(slug, role, codename, mission))
                    f.write(body_from_staff(role, codename, text))
                created.append(slug)
            continue
        with open(skill) as f:
            content = f.read()
        if content.startswith('---\n'):
            fm = content.split('---', 2)[1]
            if not re.search(rf'^name:\s*{re.escape(slug)}\s*$', fm, re.M):
                drift.append(slug)
                print(f'frontmatter name mismatch: {slug}')
                continue
            dm = re.search(r'^description:\s*(.+)$', fm, re.M)
            if dm and not dm.group(1).startswith(('"', "'")):
                # Unquoted description containing ": " is invalid YAML.
                drift.append(slug)
                if not check_only:
                    quoted = 'description: ' + json.dumps(
                        dm.group(1).strip())
                    content = content.replace(dm.group(0), quoted, 1)
                    with open(skill, 'w') as f:
                        f.write(content)
                    fixed.append(slug)
                continue
            ok.append(slug)
            continue
        drift.append(slug)
        if not check_only:
            with open(skill, 'w') as f:
                f.write(frontmatter(slug, role, codename, mission))
                f.write(content if content.startswith('\n')
                        else content)
            fixed.append(slug)
    print(f'seats: {len(slugs)} | agents ok: {len(ok)} | '
          f'created: {len(created)} | frontmatter added: {len(fixed)}')
    if created:
        print('created:', ', '.join(created))
    if fixed:
        print('frontmatter added:', ', '.join(fixed))
    if check_only and drift:
        print('drift:', ', '.join(drift))
        sys.exit(1)


if __name__ == '__main__':
    main()
