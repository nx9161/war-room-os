#!/usr/bin/env python3
"""Company-grade repo hygiene checks. Exits non-zero on any violation.

Checks:
  1. Required standard files exist (LICENSE, README, ACTIVATE, ...).
  2. Every office/staff/*.md and office/playbooks/*.md is referenced in
     the canonical docs (office/README.md, office/AGENTS.md, AGENTS.md).
  3. ACTIVATE.md carries the trigger phrase.
  4. No trailing whitespace in tracked markdown files.
  5. Every SKILL.md under skills/*/ carries valid Agent Skills
     frontmatter (name matches folder, description present and
     <= 200 chars, license present).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors = []

REQUIRED = [
    "LICENSE",
    "README.md",
    "ACTIVATE.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "office/HOUSE_RULES.md",
    "office/README.md",
    "office/AGENTS.md",
    "memory/INDEX.md",
]
for f in REQUIRED:
    if not (ROOT / f).exists():
        errors.append(f"missing required file: {f}")

canon = ""
for f in ["office/README.md", "office/AGENTS.md", "AGENTS.md", "README.md"]:
    p = ROOT / f
    if p.exists():
        canon += "\n" + p.read_text(encoding="utf-8")
canon_n = canon.lower().replace("-", "").replace("_", "")


def referenced(stem: str) -> bool:
    return stem.lower().replace("-", "").replace("_", "") in canon_n


for d in ["office/staff", "office/playbooks"]:
    for md in sorted((ROOT / d).glob("*.md")):
        if not referenced(md.stem):
            errors.append(f"unreferenced file: {md.relative_to(ROOT)}")

act = (ROOT / "ACTIVATE.md").read_text(encoding="utf-8")
if "github public repo" not in act.lower():
    errors.append("ACTIVATE.md missing the trigger phrase")

# 5. Every SKILL.md under skills/*/ carries valid Agent Skills
#    frontmatter: name matches its folder, description present and
#    <= 200 chars, license present. (office/skills/*/ are covered by
#    the seat-skill standardization pass; not gated here.)
import re

base = ROOT / "skills"
if base.is_dir():
    for skill_md in sorted(base.glob("*/SKILL.md")):
        slug = skill_md.parent.name
        text = skill_md.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"{skill_md.relative_to(ROOT)}: missing YAML frontmatter")
            continue
        fm = m.group(1)
        name_m = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
        desc_m = re.search(r"^description:\s*(.+?)\s*$", fm, re.M)
        if not name_m or name_m.group(1).strip('"') != slug:
            errors.append(
                f"{skill_md.relative_to(ROOT)}: frontmatter name must match folder '{slug}'"
            )
        if not desc_m:
            errors.append(f"{skill_md.relative_to(ROOT)}: frontmatter description missing")
        elif len(desc_m.group(1)) > 200:
            errors.append(
                f"{skill_md.relative_to(ROOT)}: description > 200 chars "
                f"({len(desc_m.group(1))})"
            )
        if not re.search(r"^license:\s*\S+", fm, re.M):
            errors.append(f"{skill_md.relative_to(ROOT)}: frontmatter license missing")

for md in sorted(ROOT.rglob("*.md")):
    if ".git/" in str(md):
        continue
    for i, line in enumerate(
        md.read_text(encoding="utf-8").splitlines(), 1
    ):
        if line != line.rstrip():
            errors.append(
                f"trailing whitespace: {md.relative_to(ROOT)}:{i}"
            )
            break

if errors:
    print("validate_repo.py FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("validate_repo.py OK")
