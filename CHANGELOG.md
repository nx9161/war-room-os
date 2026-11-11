# Changelog

All notable changes to this repository are documented here.
Format: Keep a Changelog (https://keepachangelog.com/en/1.0.0/).

## [Unreleased]
### Added
- **Full freshness sync with the private office (2026-11-11).** The
  roster is complete at **45 seats**: the Connector Operator and
  Decision Model seats (charters + skills) are in, and every count in
  the repo now says 45. The agent bundle, office handbook, and War
  Room playbook are the current editions; the House Rules are
  complete through **§11 (No invented blockers)** — including §9
  (owner orders execute) and §10 (the Director mandate), which this
  snapshot had never carried. New system docs: `ROSTER-TIERS.md`,
  `MODEL-ROUTING.md`, `TOOL-GRANTS.md`, `BRAIN-DESIGN.md`. The
  validator drift (two unreferenced staff files) is fixed.
- **Promotion Gate for self-modification** in the War Room playbook:
  self-applied changes cite eval evidence (or a `process-only` line)
  in their commit body, behavior changes must hold or beat the eval
  baseline, and every recorded mistake spawns a regression eval task.
- **Cast Check gains shape and budget.** Every mission now declares
  `shape: parallel | sequential | mixed` and `budget: seats × max
  actions`; sequential missions default to one seat (Google Research
  180-configuration study, 2026-09-24: fan-out on sequential work
  costs 39–70%), and seating more than 7 seats must record why the
  work is independent.

## [2026-11-11] — Sloane becomes Director
### Changed
- **Sloane is now Chief Orchestrator & Director.** Beyond executing the
  owner's requests, she directs herself: a standing self-improvement
  loop (scheduled light research passes over GitHub, Hacker News,
  Reddit, and the web) finds, verifies, and applies improvements to the
  office — her own files included — without waiting to be asked.
- Every applied update is recorded as **its own git commit**; suitable
  changes land in this public repo in the same pass as the private
  office.
- **Token economy is a standing duty:** capped light passes, memory
  checked before research, summaries over raw dumps, no continuous
  polling.

## [2026-10-07] — Company-grade open source
### Added
- `ACTIVATE.md`: trigger-phrase activation contract — "I want to use War
  Room Protocol from nx9161's github public repo" boots the Sloane
  office in any agent session; the office stays active until "End War
  Room Protocol".
- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1), `SECURITY.md`,
  `CONTRIBUTING.md`, `.github/CODEOWNERS`, PR template, issue templates.
- CI: `.github/workflows/validate.yml` runs
  `office/scripts/validate_repo.py` (required files, reference checks,
  hygiene) on every push/PR.
- `CHANGELOG.md` (this file).

## [2026-10-07] — 15 seats
### Added
- Knowledge Wizard joins (Quality & Ops); War Room gains mandatory
  Phase 0: Prompt Writer perfects the prompt → Wizard briefs every seat
  from fully-read docs → no seat speaks before the dossier lands.

## [2026-10-06] — 14 seats
### Added
- Prompt Writer, Business Analyst, General Counsel (Legal & Governance).
- Simplified repo-based memory (`/memory/` + wings); retired
  `office/palace/`.

## [2026-10-07] — 20 seats: new Games division
- 5 new agents: Game Architect, Gameplay Designer, Game UI/UX Designer,
  Console Platform Engineer, Game Producer (new Games division).
- Roster now 20 roles in 6 divisions; activation line, plugin notice,
  org chart, and roster table updated.
- Console Platform Engineer is a blocking seat on certification and
  platform-compliance grounds (Sony TRC / Xbox XR).
- War Room phases extended for game projects: Phase 1 (game vision),
  Phase 2 (game architecture + platform constraints), Phase 3
  (certification review), Phase 4 (Game Producer production gate).
