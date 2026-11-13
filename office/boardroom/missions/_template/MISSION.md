# MISSION.md — <mission name>

## Goal
<!-- One line, from the perfected prompt. -->

## Cast Check
- shape: parallel | sequential | mixed
- budget: <seats> × <max actions each>
- Dependencies: <each step — the prior steps whose outputs it needs; mixed: the parallel groups in sequence order>
- Seated: <seat slugs>
- Skipped (with reason): <seat — reason>
- Write surface (parallel/mixed only): <seat — files/modules/tables it writes; shared surfaces run sequentially>
- Saturation (parallel only): <each seated writer occupied with a full step? — a seat waiting on the Director/owner is unblocked before another writer is added>
- Repos: <each repo the mission touches — name + path/URL — and which seats read/write each>

## World baseline
<!-- The world as it stood at mission open. On resume, compare against now: a moved repo HEAD demotes done steps in that repo to active for re-verification; a stale key external input is re-read before any done step depending on it is trusted. -->
- Repos at open: <repo — HEAD commit SHA>
- Key external inputs: <input — read date>

## Active phase
<!-- One line, updated at every phase boundary. The first thing any resuming agent reads. -->
Phase 0 — <current step>

## Steps
<!-- State per step: pending | active | done | blocked. On resume, verify each done step's listed artifacts exist at their paths before trusting the checkpoint — a step whose artifacts are missing is demoted to active (or blocked, if the loss is unexplained) and re-run, never carried forward as done from the file alone. Before an expensive or hard-to-redo step, mark it active and name its expected artifacts first — that is the provisional checkpoint the re-run resumes from, checking whether the effect already landed before re-applying it. -->
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
