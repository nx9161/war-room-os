# Changelog

All notable changes to this repository are documented here.
Format: Keep a Changelog (https://keepachangelog.com/en/1.0.0/).

## [Unreleased]
### Added
- **Recovery ledger closes every resume.** The Mission state
  file rules now end a resume with a five-line ledger in the
  resume notes — what arrived during the pause, open promises,
  checkpoint artifacts verified, world baseline compared,
  direction re-checked — marked `recovered` only when all five
  ran, otherwise `degraded` naming each skipped line, with no
  step depending on a degraded line trusted until it is re-run.
  WR-MISSION gate row updated to match.
- **Deliverable schemas for the final trio — rollout complete.**
  Product Visualizer, SEO Specialist, and Sloane charters each
  gain a `## Deliverable schema` section, each a structured
  condensation of that seat's existing Deep Method output
  contract in its skill file — no new behavior, no contract
  wording changed. The checked product visualization, the
  evidence-ranked SEO audit, plan, and report, and Sloane's
  five-element owner report are now machine-shaped for the
  WR-OBJECTIVE close-out check. Pilot coverage 42 -> 45 of
  45 charters; rollout complete.
- **Deliverable schemas for the casting-and-games-delivery trio.**
  Casting Director, Console Platform Engineer, and Game
  Producer charters each gain a `## Deliverable schema`
  section, each a structured condensation of that seat's
  existing Deep Method output contract in its skill file —
  no new behavior, no contract wording changed. The checked
  universal persona, the platform certification review with
  its per-platform budget sheet, and the Phase 4 production
  gate are now machine-shaped for the WR-OBJECTIVE close-out
  check. Pilot coverage 39 -> 42 of 45 charters.
- **Deliverable schemas for the words-and-voice trio.**
  Scriptwriter, Voice Designer, and Word Specialist charters
  each gain a `## Deliverable schema` section, each a structured
  condensation of that seat's existing Deep Method output
  contract in its skill file — no new behavior, no contract
  wording changed. The shoot-ready script with its retention
  check and per-beat delivery direction, the finished audio
  verified by ear under its absolute consent boundary, and the
  native .docx execution standard are now machine-shaped for
  the WR-OBJECTIVE close-out check. Pilot coverage 36 -> 39
  of 45 charters.
- **Deliverable schemas for the go-to-market trio.** Launch
  Strategist, Sales Agent, and Social Media Strategist charters
  each gain a `## Deliverable schema` section, each a structured
  condensation of that seat's existing Deep Method output
  contract in its skill file — no new behavior, no contract
  wording changed. The fit-scored launch campaign with
  per-channel disclosed copy, the outbox-gated prospect drafts
  (nothing sends without recorded owner approval), and the
  platform-native social strategy with its boundary line are
  now machine-shaped for the WR-OBJECTIVE close-out check.
  Pilot coverage 33 -> 36 of 45 charters.
- **Deliverable schemas for the builders trio.** Harness
  Engineer, MCP Maker, and Reverse Engineer charters each gain a
  `## Deliverable schema` section, each a structured
  condensation of that seat's existing Deep Method output
  contract in its skill file — no new behavior, no contract
  wording changed. The six-part seat plugin with its worked
  end-to-end run, the thin CLI plus connector doc and skill
  proven against the real tool, and the evidence-backed
  explanation (behavior → mechanism → proof, lawful basis first)
  are now machine-shaped for the WR-OBJECTIVE close-out check.
  Pilot coverage 30 -> 33 of 45 charters.
- **Deliverable schemas for the finance trio.** Financial
  Analyst, Tax Strategist, and Excel Specialist charters each
  gain a `## Deliverable schema` section, each a structured
  condensation of that seat's existing Deep Method output
  contract in its skill file — no new behavior, no contract
  wording changed. The auditable money model (input and
  assumption registers, three scenarios, cash view, sensitivity)
  with its recommendation, the tax strategy with per-position
  legal basis plus deadline calendar and CPA handoff pack, and
  the native .xlsx execution standard (one route, live formulas,
  post-save verification) are now machine-shaped for the
  WR-OBJECTIVE close-out check. Pilot coverage 27 -> 30 of 45
  charters.
- **Deliverable schemas for the visual trio.** Architecture
  Visualizer, Diagram Designer, and Art Director charters each
  gain a `## Deliverable schema` section, each a structured
  condensation of that seat's existing Deep Method output
  contract in its skill file — no new behavior, no contract
  wording changed. The Phase 2 standalone diagram with its
  evidence note and validation gate, the editorial diagram
  (one idea, truth-checked arrows, 3-second test), and the
  direction brief plus SHIP/REWORK taste verdict are now
  machine-shaped for the WR-OBJECTIVE close-out check. Pilot
  coverage 24 -> 27 of 45 charters.
- **Held-out discipline for v3+ eval waves.** The Promotion Gate
  gains rule 5: from v3 on, each eval wave splits its fixtures
  before any tuning into train (inspect and iterate freely),
  validation (decides promotion), and held-out (never read during
  tuning; scored once at wave close — that score is the number
  reported). A fixture set used to tune a change is never that
  change's promotion evidence, and v1/v2 are honestly labelled
  regression baselines, never held-out evidence. Evidence: Kiln AI
  Harness Tuner (Show HN 2026-11-13) — train/val/test enforced in
  code, test never read, so the reported number is one the tuning
  never optimized against.
- **Deliverable schemas for the Games trio.** Game Architect,
  Gameplay Designer, and Game UI/UX Designer charters each gain a
  `## Deliverable schema` section, each a structured condensation
  of that seat's existing Deep Method output contract in its skill
  file — no new behavior, no contract wording changed. The game
  architecture delivery (budget and state-ownership tables, engine
  ADR, save/netcode specs), the Phase 1 vision and Phase 2
  mechanics spec in named tunables with playtest evidence, and
  the per-interface sign-off verdict (glance, accessibility, and
  platform checks) are now machine-shaped for the WR-OBJECTIVE
  close-out check. Pilot coverage 21 -> 24 of 45 charters.
- **Cast Check shape now derives from a step-dependency map.**
  Before declaring a mission's shape (`parallel | sequential |
  mixed`), the Cast Check writes each step's dependencies — which
  prior steps' outputs it needs — into the MISSION.md Cast Check
  result. `mixed` is now the written partition: independent steps
  grouped to run in parallel, the groups ordered in sequence —
  never the bare word with no structure. A step placed in a
  parallel group whose inputs include a step in the same group is
  a shape error in the Cast Check. Evidence: AdaptOrch (arXiv
  2602.16873, Feb 2026) — routing the execution topology from the
  task dependency graph beat static single-topology baselines by
  12–23% on SWE-bench, GPQA, and RAG tasks with identical models.
- **Deliverable schemas for the Phase 3 challenge trio.** AI Red
  Teamer, Global Tech Law Lead, and Penetration Tester charters
  each gain a `## Deliverable schema` section, each a structured
  condensation of that seat's existing Deep Method output contract
  in its skill file — no new behavior, no contract wording
  changed. The adversarial review verdict (transcript-backed
  attack log + coverage table), the compliance review (data-map
  version, applicability table, cited findings), and the
  exploit-proof pentest verdict (PoC-backed findings, unvalidated
  notes kept in a separate appendix) are now machine-shaped for
  the WR-OBJECTIVE close-out check. Pilot coverage 18 -> 21 of
  45 charters.
- **Validate the handoff before building on it.** A seat that
  receives work from another seat checks what it was handed first:
  cited artifacts exist at their paths, the data is fresh enough for
  the decision, and the claims make sense against the brief. A failed
  check bounces back to the sender (or Sloane) instead of being built
  on. Evidence: Kadharmoideen Fadurudeen, "Building a Multi-Agent
  System: 3 Patterns, Explained Simply" (kadhar.dev, 2026-11-05; HN
  106 pts / 45 comments) — "Bad data travels, and arrives looking
  like fact... agent B can't tell agent A's guess from a fact. Check
  data at every handoff, in plain code." Stormwise, 117 real
  NWS-alert cases: test alerts taken in as real warnings.
- **Resume checks the world, not just the checkpoint.** MISSION.md
  now records a World baseline at mission open — the HEAD commit of
  every repo touched plus the read dates of the dossier's key external
  inputs — and the resume rule compares against it: a moved repo HEAD
  demotes done steps in that repo to active for re-verification, and
  a stale changeable input (prices, live pages, availability) is
  re-read before any done step depending on it is trusted. Artifacts
  existing proves the checkpoint survived, not that the world stood
  still. Evidence: rmehan, "Reliable Agent Workflows: Code, Contracts,
  and Judgment" (2026-11-13) — if the repository head, policy, or
  source data changed, invalidate the affected stages rather than
  continuing from stale assumptions.
- **Cast Check gains a saturate-before-scaling step.** Before adding
  a parallel writer beyond the first, the Director confirms the
  already-seated writers are occupied with a full step each — a seat
  waiting on the Director or the owner is unblocked, or handed its
  next step, before another writer is added. The reverse test: if
  parallel seats keep producing work the Director rejects despite
  reasonable plans, the workload is not parallelizable, so the
  mission collapses to sequential until the Director re-justifies
  the parallel shape. Evidence: 0xandrewshu, "From 1 to 3 Parallel
  Claude Code Agents" (DEV, 2026-03-17) — utilization 16% to 50%+
  only after the first agent was fully occupied and each added agent
  got an isolated, right-sized task. A matching Saturation line joins
  the MISSION.md template.
- **Deliverable schemas for three more seats (18 of 45).** The
  charters for UI/UX Designer, Lead Mobile/Frontend Engineer, and
  Document Artisan each gain a `Deliverable schema` section — a
  structured condensation of that seat's existing output contract,
  no new behavior: wireframes plus an interaction spec (every screen
  with loading/empty/error states, WCAG 2.1 AA, mobile-first
  responsive, no lorem ipsum in build-ready specs); screens shipped
  plus state model plus shared-logic location (verification note
  naming the platforms/widths actually run and the API contract
  version); the native editable file, preview-approved, plus a
  one-line summary (native objects only, data honesty binding, open
  creator metadata).
- **Phase regression classifies the trigger before re-running.**
  Before a loop-back re-run, Sloane classifies the trigger as
  transient (tool fault, flaky check, missing artifact — a
  same-approach re-run may repair it) or latent (wrong decomposition,
  wrong seat, ambiguous brief/delegation, wrong objective reading —
  the re-run must change something structural: re-decompose the step,
  re-seat it, or rewrite the brief). A same-approach re-run of a
  latent trigger is a stall, not a regression, and Sloane stops it
  rather than burning one of the three bounded regressions on it.
  Evidence: OrchestraBench (arXiv:2608.05263, 2026-08) — across five
  MAST failure modes, tool faults recovered 1.0, ambiguous delegation
  0.30, and three latent/semantic modes never recovered (0.0); "retry
  does not repair the latent modes — it reproduces the fault and only
  lengthens time-to-detection." The WR-REGRESS gate row in GATES.md
  carries the same rule; loop-back records now include the
  classification.
- **Deliverable schemas for three more seats (15 of 45).** The
  charters for Mission Control, Memory Keeper, and Connector
  Operator each gain a `Deliverable schema` section — a structured
  condensation of that seat's existing output contract, no new
  behavior: the live operations picture plus one-question-with-context
  queue plus review-gate package (every status line timestamped);
  the durable memory entry plus spawn injection plus palace health
  (entries earn their keep or are dropped); the Phase 0 readiness
  check plus operation result plus same-day runbook update (live-read
  evidence only, never a claim from memory).
- **Learnings earn their place before they are written.** The
  Continuous Learning Protocol gains a write-time salience test
  (rule 7): before logging a learning, the seat asks whether it
  generalizes beyond this mission, whether it is already in the
  charter, skill, or file, and whether forgetting it would repeat a
  real mistake — a candidate failing any of the three stays in the
  mission's own record, never the learnings file. Judgment stays
  with the seat, not a fixed filter (Anthropic, "The Components of
  Agent Memory", 2026-11-07: indiscriminate writing sank the run —
  413 memory files, one badge — while nine files plus one dashboard
  earned four; HN 189 pts / 105 comments).
- **Spawn packets carry a self-contained task brief.** Every packet
  now states what to change, what not to touch, and how to prove it
  is done — because a spawned seat starts with a clean context and
  never sees the coordinator's conversation, so the brief must stand
  alone (Henrique Silva, "Why I Stopped Letting One AI Agent Do
  Everything", Medium, 2026-10-22). A packet without the three lines
  does not spawn.
- **Cast Check names every repo the mission touches.** New Cast Check
  step 6: list each repo (name + path or URL) and, per seated seat,
  which repos outside the office repo it must read or write; the
  Mission state file section carries the repos in the Cast Check
  result and a "Name the repos before spawning" rule, and the
  MISSION.md template gains a Repos line. A seat spawned into a
  single worktree with no map of the neighbouring repos is blind to
  context that lives next door (Ask HN, 2026-06-26: orchestration
  tools "assume an agent lives in one worktree of one git repo...
  the repo boundary is often just not the task boundary").
- **Checkpoint before the expensive step, not after it.** Before a
  step that is long, costly, or hard to redo, the seat writes a
  provisional checkpoint first: the step goes `active` in MISSION.md
  with its expected artifacts named (the announce-intent boardroom
  note doubles as that checkpoint in `parallel`/`mixed` missions).
  A crash mid-step re-runs from that provisional state — and the
  re-run is idempotent: it checks whether the effect already landed
  before re-applying it, never double-applies (Rivet actor model,
  DEV 2026-11-08).
- **Deliverable schemas for three more seats — pilot now 12 of 45.**
  General Counsel, Lead Backend Dev, and Decision Model charters each
  gain a `## Deliverable schema` section (Deliverable / Format /
  Required sections / Acceptance), each a structured condensation of
  that seat's existing output contract — no new behavior. General
  Counsel: Phase 3 legal verdict (CLEAR / CONDITIONAL CLEAR / BLOCK)
  with severity + mitigation, jurisdictions applied, engage-counsel
  triggers, and owner-acceptance-in-writing as the only block-clear
  besides clearance. Lead Backend Dev: server-side implementation +
  endpoint test evidence; every endpoint happy path + error paths +
  tests, reversible backwards-compatible migrations. Decision Model:
  typed question set + truth table (every combination, including the
  0.3–0.7 unsettled band) + evaluation report; a failed call is an
  error, never an answer.
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
