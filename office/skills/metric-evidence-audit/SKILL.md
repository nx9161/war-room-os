---
name: metric-evidence-audit
description: Audit a coverage, count, or status metric against the exact files its reader actually scans, before trusting or reporting the number. Use when a metric marks known-active work as absent, a count looks stale, or a report disagrees with observed activity.
license: MIT
version: 1.0.0
source: office learnings — Sloane, 2026-11-14 (Director passes 62 and 67)
installed: 2026-11-14
custodian: sloane
---

# Metric Evidence Audit — Learned Skill

A metric is only as honest as the file its reader scans and the pattern
it scans for. When a number disagrees with work you can see happening,
audit the reader and the evidence location before trusting either.

## Procedure

1. **Name the claim and find the reader.** State the exact figure and
   what it claims to measure. Locate the script, tool, or query that
   produces it and read its source — list exactly which files,
   directories, and heading/field patterns it counts. Never guess the
   source from the metric's name.
2. **Map where the evidence actually lives.** Find where the work was
   recorded (wing entries, logs, commits, other files) and compare that
   map, file by file and pattern by pattern, against step 1.
3. **Classify the discrepancy — the three kinds need different fixes:**
   - *Reader bug:* the evidence is in the reader's file but its pattern
     misses a legitimate form (fix the pattern).
   - *Evidence misplacement:* the work is real but recorded only in a
     file the reader never scans (land the evidence in the reader's
     file, in its counted form).
   - *Genuine absence:* no evidence anywhere (the metric is right;
     report the absence, do not manufacture evidence).
4. **Fix the smallest side.** Correct the reader pattern OR land the
   evidence — never both blindly, and never edit the reported number
   by hand.
5. **Re-run and propagate honestly.** Re-run the metric from scratch;
   the new figure is a re-run result, not an estimate. Update every
   surface that cited the old figure in the same commit, and record
   which kind of discrepancy it was.

## Demonstrations (admission evidence)

- **Director pass 62 (2026-11-14), reader bug:** `seat-coverage.py`
  missed `## YYYY-` dated learnings headings, counting three active
  seats as cold; coverage corrected 25/20 → 28/17 on re-run.
- **Director pass 67 (2026-11-14), evidence misplacement:** Sloane's
  learnings file stayed "(none yet)" through 66 passes recorded only
  in the wing, so the counter read the Director cold; one entry landed
  in the reader's file and the re-run read 29 used / 16 cold.

## Boundaries

- This skill audits a metric's evidence chain; it does not create
  evidence for work that did not happen.
- A corrected figure is reported only after the re-run in step 5.
