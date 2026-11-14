#!/usr/bin/env python3
"""Skill description collision report — report-only, never a gate.

Routers (Claude Code, Codex, Antigravity, ...) choose a skill from its
frontmatter name + description alone; two descriptions that say nearly
the same thing invite "sibling hijacking", where the wrong skill loads
first (Google Cloud Blog, 2026-11-03, on skill-reach; addyosmani
agent-skills Tier-2 lexical check, Director pass 60).

This computes TF-IDF cosine similarity over every
office/skills/*/SKILL.md description and lists the nearest rivals.
It prints a report and ALWAYS exits 0: similarity is a prompt for a
human to sharpen a description, not proof of a routing failure —
empirical routing probes are the evidence that promotes a pair to a
fix (learned-skill admission gate, pass 63, applies to any new skill
this report motivates).

Usage: skill-collision.py [--top N] [--threshold X]
Stdlib only.
"""
import math
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
STOP = set("the a an and or of to for in on with is are when use used "
           "using this that it its as at by from into your you".split())


def description(path: Path) -> str:
    text = path.read_text(errors="replace")
    if not text.startswith("---"):
        return ""
    fm = text.split("---", 2)[1]
    lines = fm.splitlines()
    for i, ln in enumerate(lines):
        m = re.match(r"description:\s*(.*)$", ln)
        if not m:
            continue
        val = m.group(1).strip()
        if val in (">", ">-", "|", "|-"):  # folded/literal block
            block = []
            for nxt in lines[i + 1:]:
                if nxt[:1] in (" ", "\t"):
                    block.append(nxt.strip())
                else:
                    break
            return " ".join(block)
        return val.strip("'\"")
    return ""


def tokens(text: str) -> list:
    return [t for t in re.findall(r"[a-z0-9][a-z0-9\-]+", text.lower())
            if t not in STOP and len(t) > 2]


def main() -> int:
    top = 10
    threshold = 0.30
    if "--top" in sys.argv:
        top = int(sys.argv[sys.argv.index("--top") + 1])
    if "--threshold" in sys.argv:
        threshold = float(sys.argv[sys.argv.index("--threshold") + 1])

    skills = {}
    for sk in sorted((REPO / "office" / "skills").glob("*/SKILL.md")):
        d = description(sk)
        if d:
            skills[sk.parent.name] = tokens(d)
    names = sorted(skills)
    n = len(names)
    df = Counter()
    for toks in skills.values():
        df.update(set(toks))
    idf = {t: math.log((1 + n) / (1 + c)) + 1.0 for t, c in df.items()}

    def vec(toks):
        tf = Counter(toks)
        return {t: (1 + math.log(c)) * idf[t] for t, c in tf.items()}

    vecs = {name: vec(toks) for name, toks in skills.items()}
    norms = {k: math.sqrt(sum(v * v for v in vec.values()))
             for k, vec in vecs.items()}

    pairs = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            dot = sum(w * vecs[b].get(t, 0.0) for t, w in vecs[a].items())
            sim = dot / (norms[a] * norms[b]) if norms[a] and norms[b] else 0.0
            pairs.append((sim, a, b))
    pairs.sort(reverse=True)

    print(f"skill-collision: {n} skill descriptions, "
          f"{len(pairs)} pairs (report-only, exit 0 always)")
    flagged = [(s, a, b) for s, a, b in pairs if s >= threshold]
    print(f"pairs at/above threshold {threshold}: {len(flagged)} "
          f"— REVIEW means sharpen a description, not a proven failure")
    for sim, a, b in pairs[:top]:
        mark = "REVIEW" if sim >= threshold else "      "
        print(f"  {mark} {sim:.3f}  {a} <-> {b}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
