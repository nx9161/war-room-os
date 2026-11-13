# Changelog

All notable changes to this repository are documented here.
Format: Keep a Changelog (https://keepachangelog.com/en/1.0.0/).

## [Unreleased]
### Added
- **Announce intent before acting in parallel missions.** In a
  `parallel` or `mixed` mission, a seat posts a short boardroom note
  naming the step and the files it is about to write *before*
  starting the work — not after. A one-line "I'm working on X" gives
  the other seated writers a chance to object when a dependency or a
  shared surface the Cast Check missed shows up. The Cast Check maps
  write surfaces at plan time; this is its runtime counterpart
  (ClawdBytes, "Your AI Agents Are Not a Team Yet", 2026-08-28,
  Lesson 3).
- **Learnings files are distilled at the monthly review — the live
  file stays short.** A seat re-reads its whole learnings file at
  every spawn, and uncurated agent memory drifts: it remembers the
  wrong things and turns them into a standing focus (HN, "Agent
  memory needs its OpenTelemetry moment", 2026-11-08). Anthropic's
  own guidance for the same shape of file is a hard ceiling — only
  the first 200 lines / 25 KB of a memory index load at session
  start, and longer instruction files reduce adherence
  (code.claude.com/docs/en/memory). New rule 6 in the Continuous
  Learning Protocol: at the monthly review, any entry already folded
  into the seat's charter or skill is marked folded — dated, with a
  pointer to where it landed — and moved to
  `office/learnings/archive/<seat-slug>.md` (history, never re-read
  at spawn). The live file holds only still-live, not-yet-folded
  learnings and stays under ~150 lines. (This mirror also brings in
  rule 5, reconcile learnings when instructions change, which the
  private repo has carried since 2026-11-11 and rule 6 depends on.)
- **Verify the checkpoint before trusting it on resume.** A
  checkpoint is a regenerable cache, never a source of truth
  (Axocoatl architecture note, 2026-06; Microsoft Agent Framework
  node-boundary checkpoints, 2026-08-22). On resume, the agent
  checks each `done` step's listed artifacts actually exist at
  their paths before proceeding — a step whose artifacts are
  missing is demoted to `active` (or `blocked`, if the loss is
  unexplained) and re-run, never carried forward as done from the
  file alone. The MISSION.md template carries the same rule in its
  Steps comment.
- **Deliverable schemas for three more seats (9 of 45).** The
  Knowledge Wizard (Phase 0 dossier: term inventory with closure
  status, shared facts, per-seat briefing blocks, simplest-path
  recommendation, open unknowns), the Business Analyst (Phase 1
  business case: numbers first, every figure sourced and dated,
  verdict viable / viable-with-changes / not viable), and the
  AppSec Lead (security review verdict CLEAR / CONDITIONAL CLEAR /
  BLOCK with findings table and residual risk) each gain a
  `## Deliverable schema` section in their charter, condensed from
  their existing Deep Method output contracts — no new behavior.
- **Stalled seats get a 30-minute check-in, then stop.** A mission
  step whose seat has produced no boardroom note, commit, or status
  update for 30 minutes gets a Director check-in; a seat that is
  stalled — no progress and no block reported — is stopped and its
  step re-seated or re-scoped, never left running idle. Grounded in
  ripXG, "Coordinating AI agent teams" (2026-02-08), and Wasim's
  "I Had a Perfect Sprint Board" (DEV, 2026-11-12), rule 7.
- **Failed approaches section in MISSION.md.** The mission state
  file now records every tried-and-abandoned approach — newest on
  top, what was tried, why it failed, what it rules out — the moment
  an approach fails, a phase regresses, or a step reopens. A reopened
  step's next attempt names the failed approach it avoids, so the
  next agent does not retry it blind. Grounded in lean-collab
  (mutable-state-inc/lean-collab, HN 2026-02-12): failed strategies
  are written to shared memory so a new agent picking up an expired
  claim sees everything already tried.
- **Explicit `Active phase` line in MISSION.md.** The mission state
  file now names the current phase and step on one line, updated at
  every phase boundary, and the resume rule binds every agent —
  Director or seat: after compaction, a crash, or a new session,
  re-read MISSION.md and resume from that line, never reconstruct
  from memory. Grounded in BIOME's Elephant State Anchor
  (asteria-core/biome, 2026-11-09) — a deterministic state file
  reloaded by a post-compaction recovery protocol.
- **Deliverable schemas — rollout to 6 of 45 seats.** Product Owner
  (the Phase 1 PRD, 7 required elements, filed before Phase 2
  opens), Lead Code Reviewer (merge-review verdict, findings list,
  delete-list), and DevOps / SRE (pipeline or infrastructure change
  plus deploy report, clean-run evidence quoted from a fresh clone)
  join the pilot three. Each schema condenses that seat's existing
  Deep Method output contract; no new behavior. Rollout continues a
  few seats per pass.
- **Write-surface map in the Cast Check.** Before parallel or mixed
  work starts, each seated writer lists the files, modules, or tables
  it will write — not just its feature. Two seats writing the same
  surface never run at the same time; they run sequentially, or the
  work is re-split until their write surfaces are disjoint. Read-only
  seats run in parallel freely. Grounded in a fresh field report:
  Wasim, "I Had a Perfect Sprint Board. 18 AI Subagents Still Wrecked
  the Repo." (2026-11-12) — 18 subagents on separate tickets overwrote
  each other's work because the tickets shared files underneath
  ("Plan by files, not just features").
- **Deliverable schemas (pilot, 3 of 45 seats).** A seat's charter now
  carries a `## Deliverable schema` section — the machine-checkable
  shape of what the seat must produce (Deliverable / Format / Required
  sections / Acceptance) — so the receiving seat, and Sloane at
  close-out (`WR-OBJECTIVE`), can verify a delivery without re-reading
  the seat's whole method. Piloted on the three outputs every mission
  consumes: the Enterprise Architect's Phase 2 proposal, the Prompt
  Writer's perfected prompt, and the QA Manager's gate verdict. Each
  schema condenses that seat's existing Deep Method output contract;
  no new behavior. Rollout continues a few seats per pass.
- **Objective verification at mission close (`WR-OBJECTIVE`).** Before
  Sloane authorizes a release, she re-reads the mission's stated
  objective (the `MISSION.md` Goal, from the perfected prompt) and
  verifies each deliverable against it — not only against the decomposed
  acceptance criteria. A deliverable that passes its tests but misses
  the objective loops back under Phase regression; the check is recorded
  in `MISSION.md`. Grounded in Cemri et al., *Why Do Multi-Agent LLM
  Systems Fail?* (UC Berkeley, NeurIPS 2025): adding a high-level
  task-objective verification step yielded +15.6% task success in their
  intervention study; task-verification failures were 23.5% of the
  1,642 annotated traces.
  buried in the War Room playbook and House Rules now carry stable
  IDs (`WR-ROSTER` … `WR-ESCALATE`), each with its source section
  and who blocks / what clears it. The playbook and House Rules stay
  authoritative; the index states that and the §9 scope (gates never
  stand in front of the owner's own direct order).
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
- **MISSION.md durable mission state.** Every mission now opens one
  checkpoint file at `office/boardroom/missions/<mission-slug>/MISSION.md`
  (goal, Cast Check result, step checklist, artifact paths, resume
  notes updated at every phase boundary); handoffs cite file paths,
  never paste full outputs, and the Director resumes from the file
  after compaction or a new session.
- **Frontmatter hygiene for two tool skills.** `archify-diagrams` and
  `voice-studio` — both granted to all 45 seats — previously carried no
  YAML frontmatter at all, so they were invisible to description-based
  routing. Both now carry a standard `name` + trigger-style
  `description` (mirror of the private office; the private validator
  now gates tool-skill frontmatter too).
- **Validator now gates seat agents and deliverable schemas.** The
  public `validate_repo.py` gains the two checks the private validator
  has carried since Director passes 5 and 16: every seat slug must
  have an `office/skills/<slug>/SKILL.md` agent with matching
  frontmatter (`name` + `description`), tool skills included, and
  every charter carrying a `## Deliverable schema` section must have
  all four fields. Ported in this validator's own regex style so the
  template stays stdlib-only — the private gate parses strict YAML,
  so the ported check guarantees frontmatter presence, not YAML
  validity (a folded `description: >` reads as its indicator). The
  snapshot already passed both gates when measured (45/45 agents,
  3/45 schemas); the public validator simply never ran them.

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
