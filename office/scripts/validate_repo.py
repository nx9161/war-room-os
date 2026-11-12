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
  6. Every seat slug is backed by an agent: office/skills/<slug>/SKILL.md
     exists and carries frontmatter (name matches the slug, description
     present); tool skills under office/skills/*/ are gated the same
     way. Regex-based, stdlib-only — the private validator's equivalent
     gate parses strict YAML.
  7. Every staff charter carrying a `## Deliverable schema` section has
     all four fields (Deliverable, Format, Required sections,
     Acceptance); pilot coverage is reported, not enforced.
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

# 6. Every seat slug is backed by an agent under office/skills/, with
#    frontmatter whose name matches the slug and a description present.
#    Tool skills (office/skills/*/ without a staff file) are gated the
#    same way. Regex-based, matching this validator's check 5 style and
#    keeping the public template stdlib-only. Known limit, same as
#    check 5: a folded/block-scalar description (e.g. `description: >`)
#    reads as its indicator, so this gate guarantees frontmatter
#    presence, not YAML validity — the strict YAML gate stays private.
def check_office_skill_frontmatter(slug, skill, label):
    text = skill.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{label} has no frontmatter: {slug}")
        return
    fm = m.group(1)
    name_m = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    desc_m = re.search(r"^description:\s*(.+?)\s*$", fm, re.M)
    if not name_m or name_m.group(1).strip('"') != slug:
        errors.append(f"{label} name mismatch: {slug}")
    elif not desc_m:
        errors.append(f"{label} description missing: {slug}")


for staff in sorted((ROOT / "office/staff").glob("*.md")):
    slug = staff.stem
    skill = ROOT / "office/skills" / slug / "SKILL.md"
    if not skill.exists():
        errors.append(f"seat without agent: {slug}")
        continue
    check_office_skill_frontmatter(slug, skill, "agent")
staff_slugs = {s.stem for s in (ROOT / "office/staff").glob("*.md")}
for skill in sorted((ROOT / "office/skills").glob("*/SKILL.md")):
    slug = skill.parent.name
    if slug not in staff_slugs:
        check_office_skill_frontmatter(slug, skill, "tool skill")

# 7. Every staff charter carrying a `## Deliverable schema` section has
#    all four fields; pilot coverage is reported, not enforced.
SCHEMA_FIELDS = [
    "- **Deliverable:**",
    "- **Format:**",
    "- **Required sections:**",
    "- **Acceptance:**",
]
schema_covered = 0
for staff in sorted((ROOT / "office/staff").glob("*.md")):
    text = staff.read_text(encoding="utf-8")
    marker = "## Deliverable schema"
    if marker not in text:
        continue
    schema_covered += 1
    section = text.split(marker, 1)[1]
    section = section.split("\n## ", 1)[0]
    for field in SCHEMA_FIELDS:
        if field not in section:
            errors.append(
                f"deliverable schema missing {field} "
                f"in {staff.relative_to(ROOT)}"
            )
print(f"deliverable schemas: {schema_covered}/45 charters (pilot)")

if errors:
    print("validate_repo.py FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("validate_repo.py OK")
