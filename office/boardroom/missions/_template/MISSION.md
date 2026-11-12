# MISSION.md — <mission name>

## Goal
<!-- One line, from the perfected prompt. -->

## Cast Check
- shape: parallel | sequential | mixed
- budget: <seats> × <max actions each>
- Seated: <seat slugs>
- Skipped (with reason): <seat — reason>
- Write surface (parallel/mixed only): <seat — files/modules/tables it writes; shared surfaces run sequentially>

## Active phase
<!-- One line, updated at every phase boundary. The first thing any resuming agent reads. -->
Phase 0 — <current step>

## Steps
<!-- State per step: pending | active | done | blocked. -->
- [ ] pending — <step>
- [ ] pending — <step>

## Failed approaches
<!-- Tried-and-abandoned approaches, newest on top. Recorded the moment an approach fails, a phase regresses, or a step reopens — so the next agent assigned to that step sees what was already tried and why, and does not retry it blind. -->
- <date> — <what was tried> — <why it failed / what it rules out>

## Artifacts
<!-- Paths only, never pasted content. -->
- Dossier: <path>
- PRD: <path>
- ADRs: <path>

## Close-out
<!-- Objective verification (WR-OBJECTIVE): before release authorization. -->
- Objective verification: <date — each deliverable checked against the Goal above; result, or loop-back if any>

## Resume notes
<!-- Director updates at every phase boundary. Newest entry on top. -->
- <date> — <where we are, what's next, what's blocked>
