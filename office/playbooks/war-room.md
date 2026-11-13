# Playbook: war-room

The synchronous consensus loop. Runs BEFORE any production code is
committed for a significant feature or release. The orchestrator
(Sloane) runs it by spawning one subagent per role per phase and
synthesizing the outcome. Each role agent is briefed with the perfected
prompt from the Prompt Writer — never the raw request — plus the
Knowledge Wizard's Phase 0 dossier. Each phase's conclusion is recorded as an ADR
in the palace (`memory/wings/<wing>/`).

Naming: the War Room is the office's standing process — never rename it
per project. Refer to sessions as "War Room Phase N — Project: X".
Gate index: `office/GATES.md` — every gate in this playbook carries a
stable WR- ID there, with its source and what clears it.

## Roster check (automatic, every session)
The room seats itself fresh every time it convenes — no announcement
needed:
1. Before Phase 0, Sloane re-reads `office/staff/`. Any seat file not
   seen in the previous session is a **new agent**.
2. New agents are briefed (their seat file + the session dossier) and
   join from the next activity onward — they debate, vote, and take
   actions like everyone else.
3. Sloane announces the current table once at session start ("44 seated").
4. The same check runs between phases: a seat added mid-session joins
   at the next phase boundary.
5. If the owner mentions a roster change mid-conversation ("I added an
   agent", "I updated the file"), Sloane re-reads the roster immediately
   and confirms the new lineup — then the next War Room activity
   includes them.

## Spawn packet (mandatory — Intelligence Upgrade Layer 3)

No seat is spawned from memory of its role. Before a seat speaks, its
packet is assembled by `office/scripts/spawn-packet.py <slug>` (add
`--wing memory/wings/projects/<project>` for mission context): model
routing header, the seat's skill, staff file, learnings, personal
board and decision log, in that priority order. The host pastes the
packet (or the file paths it contains, where the harness reads files
directly) into the seat's briefing. `spawn-packet.py --check-all`
must pass 45/45 before a War Room convenes — a seat that cannot
assemble a packet does not sit.

Every packet also carries a self-contained task brief — what to
change, what not to touch, and how to prove it is done. A spawned
seat starts with a clean context and never sees the coordinator's
conversation, so the brief must stand alone: no "as discussed", no
assumed shared state. A packet without the three lines does not spawn.

## Seat routing (standing — owner order, 2026-10-30)

Born from a real miss: a game project shipped extensive game UI work
without ever seating the Game UI/UX Designer, because the coordinator
routed to familiar seats and framed her domain as someone else's
checklist. These rules bind the coordinator, not the seats.

1. **Domain trigger.** Each seat's charter Mission defines its
   domain. When a mission touches a seat's domain, that seat is
   seated by default — with a full spawn packet, never simulated
   from the coordinator's memory of the role. The per-seat triggers
   live in `office/playbooks/seat-routing-table.md` (generated from
   the charters; regenerate it whenever a charter Mission changes).
2. **Familiarity is not a criterion.** A seat's track record, the
   coordinator's habits, or an empty learnings file never decide
   routing. A cold seat is seated precisely to end its cold start;
   skipping it for being untested is the self-fulfilling bench this
   rule exists to break.
3. **Skips are recorded.** Leaving a domain seat out requires a
   reason on the mission's boardroom record (out of scope, genuine
   duplication, owner direction). Silence is not a reason.
4. **Write-back closes the mission.** A mission is not closed until
   every seated seat has a dated learnings entry — or an explicit
   "no learning" line. Work a seat did that never reached its file
   is a coordinator defect and is reported as one.
5. **Utilization is reviewed.** The monthly learning review reports
   seat utilization from the experience log; a seat with zero live
   seatings across a quarter gets a verification drill or a cut
   recommendation — it does not get another quarter of ornament.

## Model routing (standing)

Every seat carries a model tier in its agent frontmatter
(`metadata.model_tier`): frontier / standard / fast. Spawn each seat on
the strongest model its tier calls for on the host harness — never
downgrade a blocking seat. Full rules: `office/MODEL-ROUTING.md`.

## Cast Check (mandatory, before Phase 0 — M-5 countermeasure)

Before any mission work starts, the coordinator writes the cast
check into the mission's MISSION.md (see below):

1. List the domains the mission touches (game UI, payments,
   contracts, data, deployment, …).
2. For each domain, name its seat(s) from the roster.
3. Each named seat is either **seated** (spawn packet assembled) or
   **skipped with a written reason** (out of scope, genuine
   duplication, owner direction).
4. **Declare the mission's shape and budget.** `shape: parallel |
   sequential | mixed` — are the seats' steps independent, or does
   each step depend on the previous one's output? `budget: <seats> ×
   <max actions each>` (Anthropic's orchestrator-worker budgets).
   **Sequential missions default to ONE seat** — fan-out on
   sequential work costs 39–70% of performance (Google Research
   180-configuration study, 2026-09-24); the Director may still
   seat a domain reviewer at the end. Any mission seating more than
   7 seats must record why the work is independent.
   **Map the step dependencies before declaring the shape.** The
   shape follows the dependency structure, not a gut call: list
   each step's inputs — which prior steps' outputs it needs — in
   the MISSION.md Cast Check result. All steps independent →
   `parallel`. A single chain → `sequential`. A mix → `mixed`,
   and the map is written as the partition: independent steps
   grouped to run in parallel, the groups ordered in sequence —
   never the bare word `mixed` with no structure. A step placed
   in a parallel group whose inputs include a step in the same
   group is a shape error: the Cast Check is wrong, not the plan
   (AdaptOrch, arXiv 2602.16873, Feb 2026: routing the execution
   topology from the task dependency graph beat static
   single-topology baselines by 12–23% on SWE-bench, GPQA, and
   RAG tasks with identical models).
5. **Map the write surface before parallel work.** When `shape` is
   `parallel` or `mixed`, list for each seated writer the files,
   modules, or tables it will write — not just its feature. Two
   seats writing the same file, module, or table never run at the
   same time: they run sequentially, or the work is re-split until
   their write surfaces are disjoint. Read-only seats (research,
   audit, review) may run in parallel freely. Tickets split by
   feature still collide when the code underneath is shared — the
   exact failure that wrecked an 18-subagent sprint (Wasim, "I Had
   a Perfect Sprint Board", 2026-11-12).
6. **Name every repo the mission touches.** The office repo holds the
   mission file, but the work often lives elsewhere too — the public
   snapshot, a project repo, a second repo holding the code under
   review. List each repo (name + path or URL) and, per seated seat,
   which repos outside the office repo it must read or write. A seat
   spawned into a single worktree with no map of the neighbouring repos
   is blind to context that lives next door — the exact failure yaskou
   flags on HN (Ask HN, 2026-06-26): orchestration tools "assume an
   agent lives in one worktree of one git repo... the repo boundary is
   often just not the task boundary."
7. **Saturate before scaling.** Before adding a parallel writer
   beyond the first, confirm the already-seated writers are occupied
   with a full step each — a seat waiting on the Director or the
   owner is unblocked, or handed its next step, before another writer
   is added. One busy seat beats three idle ones (0xandrewshu, "From
   1 to 3 Parallel Claude Code Agents", DEV, 2026-03-17: utilization
   16% → 50%+ only after the first agent was fully occupied and each
   added agent got an isolated, right-sized task). The reverse test:
   if parallel seats keep producing work the Director rejects despite
   reasonable plans, the workload is not parallelizable — collapse the
   mission to sequential until the Director re-justifies the parallel
   shape.
8. No Phase 0 until the cast check exists. A cast check written
   after the work is a confession, not a check — it gets logged as
   an M-5 instance.

## Mission state file (MISSION.md — mandatory, from the Cast Check on)

The plan lives in a file, not in the Director's context. Every mission
opens one checkpoint file at
`office/boardroom/missions/<mission-slug>/MISSION.md` — the Cast Check
is written into it, not into the shared board. It holds:

1. **Goal** — one line, taken from the perfected prompt.
2. **Cast Check result** — shape, budget, step-dependency map
   (mixed: the parallel groups in sequence order), seated seats,
   skipped seats with reasons, write-surface map (parallel/mixed
   only), repos touched.
3. **Step checklist** — every step with a state:
   `pending | active | done | blocked`.
4. **Active phase** — one line naming the current phase and step
   (e.g. `Phase 2 — Enterprise Architect presents topology`), updated
   at every phase boundary. The single lookup a resuming agent reads
   first — the active step is never left implicit in the checklist.
5. **Artifact paths** — dossier, PRD, ADRs, deliverables. Paths only,
   never pasted content.
6. **Resume notes** — a dated tail the Director updates at **every
   phase boundary**: where the mission stands, what happens next, what
   is blocked.
7. **Failed approaches** — every tried-and-abandoned approach, newest
   on top: what was tried, why it failed, what it rules out. Recorded
   the moment an approach fails, a phase regresses, or a step reopens.
8. **World baseline** — the world as it stood at mission open: the
   HEAD commit of every repo touched, and the read dates of the
   dossier's key external inputs (live pages, prices, availability).
   The resume check compares against this, not against memory.

Rules:

- **Update at every phase boundary.** A MISSION.md that lags the
  mission misleads the next session — worse than none at all. The
  **Active phase** line moves whenever the mission does.
- **Handoffs cite paths, never paste outputs.** Subagent results are
  referenced by file path; full outputs are never pasted into the
  coordinator thread.
- **Validate the handoff before building on it.** A seat that receives
  work from another seat — a spawn packet, a boardroom handoff, a
  Phase output — checks what it was handed before it builds on it:
  the cited artifacts exist at their paths, the data is fresh enough
  for the decision (read dates on the World baseline), and the
  numbers/claims make sense against the brief. A guess handed over as
  a fact is the failure mode: if the check fails, the seat bounces
  the handoff back to the sender (or to Sloane) with what failed, and
  does not build on it. The check is the receiving seat's job, not
  the sender's — the sender cannot see how its output will be used.
  (Kadharmoideen Fadurudeen, "Building a Multi-Agent System: 3
  Patterns, Explained Simply", kadhar.dev, 2026-11-05; HN 106 pts /
  45 comments, thread 50380658: "Bad data travels, and arrives
  looking like fact... agent B can't tell agent A's guess from a
  fact. Check data at every handoff, in plain code." Stormwise, 117
  real NWS-alert cases: test alerts taken in as real warnings.)
- **Name the repos before spawning.** The Cast Check lists every repo
  the mission touches and, per seat, which of them it reads or writes;
  the spawn packet for a seat working outside the office repo names
  those repos and their paths explicitly. A mission that spans repos
  never leaves a seat to discover the second repo on its own.
- **Resume from the file.** After context compaction, a crash, or a
  new session, **any** agent — Director or seat — re-reads MISSION.md
  before resuming and picks up from its **Active phase** line — the
  plan is never reconstructed from memory. (BIOME's Elephant State
  Anchor, 2026-11-09; LangGraph's durable-state pattern, 2026;
  Anthropic's Research system saves the lead's plan against context
  truncation — Director research pass 1, 2026-11-11.)
- **Verify the checkpoint before trusting it.** A checkpoint is a
  regenerable cache, never a source of truth (Axocoatl architecture
  note, 2026-06; Microsoft Agent Framework node-boundary checkpoints,
  2026-08-22). On resume, the agent checks each `done` step's listed
  artifacts actually exist at their paths before proceeding — a step
  whose artifacts are missing is demoted to `active` (or `blocked`,
  if the loss is unexplained) and re-run, never carried forward as
  done from the file alone. (M-2: state is verified at the
  destination, never inherited from a record.)
- **Check the world, not just the checkpoint, on resume.** Artifacts
  existing proves the checkpoint survived; it does not prove the world
  stood still while the mission was paused. On resume, the agent
  compares the **World baseline** against now: if a touched repo's HEAD
  moved, every `done` step whose inputs or artifacts live in that repo
  is demoted to `active` and re-verified against the new head before
  the mission proceeds; if a key external input is stale — its read
  date predates the pause and the value can change (prices, live pages,
  availability) — it is re-read before any `done` step depending on it
  is trusted. The check and its result go in the resume notes.
  (rmehan, "Reliable Agent Workflows: Code, Contracts, and Judgment",
  2026-11-13: "When execution resumes, the system can determine
  whether the world changed while the run was paused. If the repository
  head, policy, or source data changed, it can invalidate the affected
  stages rather than continuing from stale assumptions.")
- **Checkpoint before the expensive step, not after it.** Before a
  step that is long, costly, or hard to redo (a multi-step tool chain,
  a long generation run, a big migration, a bulk send), the seat writes
  a provisional checkpoint first: the step goes `active` in MISSION.md
  with its expected artifacts named, and in a `parallel`/`mixed`
  mission the announce-intent boardroom note doubles as that
  checkpoint. If the seat crashes mid-step, the resuming agent re-runs
  from that provisional state — and the re-run is idempotent: it checks
  whether the effect already landed (commit exists, message sent, file
  written) before re-applying it, never double-applies. (Rivet actor
  model, DEV 2026-11-08: "Write a provisional checkpoint before
  executing expensive operations... If the actor crashes, the next
  invocation can resume from the provisional state"; a mid-turn crash
  retry "requires idempotency in tool calls or explicit turn IDs to
  detect duplicates".)
- **Record failures, not just progress.** A reopened step's next
  attempt names the failed approach it avoids — the next agent reads
  the Failed approaches section first and does not retry the same
  approach blind. (lean-collab, HN 2026-02-12: failed strategies are
  written to shared memory so a new agent picking up an expired claim
  sees everything already tried; first-verified-wins.)
- **Silence gets a check-in, not a wait.** A step whose seat has
  produced no boardroom note, commit, or status update for 30 minutes
  gets a Director check-in. A seat that is stalled — no progress and
  no block reported — is stopped and its step re-seated or re-scoped,
  never left running idle. (ripXG, "Coordinating AI agent teams",
  2026-02-08: the coordinator "checks in after 30 minutes if there's
  no update"; Wasim, "I Had a Perfect Sprint Board", 2026-11-12,
  rule 7: "Stop idle agents".)
- **Announce intent before acting.** In a `parallel` or `mixed`
  mission, a seat posts a short boardroom note naming the step and the
  files it is about to write *before* starting the work — not after.
  A one-line "I'm working on X" gives the other seated writers a
  chance to object when a dependency or a shared surface the Cast
  Check missed shows up. The Cast Check maps write surfaces at plan
  time; this is its runtime counterpart. (ClawdBytes, "Your AI Agents
  Are Not a Team Yet", 2026-08-28, Lesson 3: "Agents need structured
  ways to announce intentions before taking action... enables other
  agents to object if there's a dependency or conflict they need to
  know about".)
- Template: `office/boardroom/missions/_template/MISSION.md`.

## Phase 0 — Prompt Perfection & Wizard Briefing (mandatory gate)
1. **Prompt Writer** forges the raw request into the perfected prompt —
   persona, objective, context, constraints, output format, acceptance
   criteria. No agent works from the raw version.
2. **Knowledge Wizard** takes the perfected prompt, parses every word,
   searches each term across the internet, and **reads in full** every
   related official document (API references, RFCs, changelogs, security
   advisories, specs). It compiles a per-seat dossier — facts,
   constraints, versions, gotchas — and injects it into the discussion.
3. **No seat speaks before the dossier lands.** Phase 1 begins from the
   perfected prompt plus documented facts, never from memory or vibes.
4. **MCP Maker** is dispatched when the plan needs a tool with no
   connector: it builds the integration (CLI + connector doc + skill)
- **Connector Operator** confirms live state and limits for
  every connector the plan touches (readiness check against
  `office/runbooks/connectors/<connector>.md`).
   so the seats can drive the tool.

## Phase 1 — Intake & PRD
Spawn Product Owner, UI/UX Designer, and Business Analyst (in parallel):
- Product Owner: convert the request into a PRD — problem, user stories,
  acceptance criteria, edge cases.
- UI/UX Designer: produce wireframes/interaction specs; interpret any
  attached screenshots or mockups.
- Business Analyst: the business case — pricing, margin impact, and
  commercial viability of what's proposed.
- Output: PRD document + design specs + business case, stored in the
  palace room.
- **Game projects:** also spawn Gameplay Designer (pillars, core loop,
  mechanics vision) and Game UI/UX Designer (player experience, HUD
  direction, onboarding).

## Phase 2 — Architectural Debate
Spawn Enterprise Architect first:
- Presents system topology: services, API specs, DB schemas, data flows.
Then spawn Lead Backend, Lead Frontend, and DevOps/SRE (in parallel)
to debate it:
- Challenge bottlenecks, state management, scaling limits, deployability.
- Output: agreed topology + ADRs. Unresolved disputes go to Sloane.
- Architecture Visualizer renders the agreed topology as an interactive
  diagram (no architecture leaves Phase 2 without its diagram).
- Decision Model designs the judgment layer: every classify / route /
  score / extract / verify step in the design becomes typed questions
  (Choice, Noul, Score, Box) plus a truth table in code — judgments
  from the model, decisions in code. No prompt-and-parse step ships
  where a typed question fits.
- **Game projects:** Game Architect presents the game architecture
  (engine, ECS, netcode, platform budgets) and Console Platform
  Engineer brings platform constraints (PS5/Xbox/PC targets).

## Phase 3 — Security & Legal Challenge
Spawn AppSec Lead, AI Red Teamer, Global Tech Law Lead, Reverse
Engineer, Penetration Tester, and General Counsel (in parallel):
- AppSec: OWASP Top 10 review, auth/crypto/rate-limiting assessment.
- AI Red Teamer: prompt injection, jailbreak, data poisoning probes
  against any AI-facing surface.
- Tech Law: GDPR/CCPA/NIS2/HIPAA/EU AI Act applicability, data mapping.
- Reverse Engineer: inspects third-party binaries and dependencies
  (lawful basis required) — what's inside, what it phones home to.
- Penetration Tester: agentic pentest of the app (sandboxed, authorized
  targets only) — recon, exploit, PoC-validated findings; blocks on
  confirmed exploitables.
- General Counsel: contracts/ToS/licensing, jurisdiction matrix for
  target markets, corporate/IP/employment exposure; escalates to
  licensed local counsel where binding advice is needed.
- Any of the four can BLOCK. Blocks stand until cleared or Sloane
  rules with owner input.
- **Game projects:** Console Platform Engineer joins with the TRC/XR
  certification review — and **blocks** on certification and
  platform-compliance grounds.

## Phase 4 — Build, QA Sign-off & Execution
- Build proceeds per the `ship-feature` procedure (branch → verify →
  review → PR).
- QA Manager enforces the gate: 100% pass on the release suite, no open
  blockers, then sign-off.
- Lead Code Reviewer reviews every PR before merge (Ponytail ladder:
  delete-list for over-engineering) and blocks on critical defects,
  security findings, or license/IP risk.
- **Objective verification (WR-OBJECTIVE):** before Sloane authorizes
  the release, she re-reads the mission's stated objective — the Goal
  line in `MISSION.md`, taken from the perfected prompt — and verifies
  each deliverable against it, not only against the decomposed
  acceptance criteria. A deliverable that passes its tests but does not
  serve the objective fails this check and loops back under Phase
  regression; the check and its result are recorded in `MISSION.md`.
- Voice Designer produces the voice layer: voiceovers, dubs,
  in-product TTS.
- Document Artisan produces the document layer: decks, documents,
  spreadsheets — backed by the Word Specialist (deep `.docx`) and
  Excel Specialist (deep `.xlsx`). Quality bar: gorgeous-or-nothing;
  latest skills, permanently; context first; end to end.
- **Game projects:** Game Producer runs the production gate
  (milestones green, perf budgets met, cert timeline on track).
- Sloane synthesizes the War Room record, authorizes the release, and
  reports to the owner.

## Phase regression (loop-back rule)
Phases are not one-way. If a finding in Phase N invalidates or
materially changes the output of an earlier Phase M:
1. The seat that found it flags it immediately, with evidence. Work in
   later phases pauses.
2. Sloane decides: loop back to Phase M (re-running M→N with the new
   finding as input), or rule the finding immaterial and continue.
3. Every loop-back is recorded: iteration number, trigger,
   classification (step 5), what changed. Bounded — max 3 regressions
   per request. On the 4th trigger, Sloane must choose: escalate to
   the owner with options, or terminate the request.
4. A re-run phase re-issues its outputs (updated PRD, revised specs).
   Downstream phases always work from the latest version, never stale
   output.
5. Classify the trigger before re-running. **Transient** (tool fault,
   flaky check, missing artifact): a same-approach re-run may repair
   it. **Latent** (wrong decomposition, wrong seat, ambiguous
   brief/delegation, wrong objective reading): retry reproduces the
   fault — the re-run must change something structural (re-decompose
   the step, re-seat it, or rewrite the brief). A same-approach re-run
   of a latent trigger is not a regression, it is a stall: Sloane
   stops it rather than burning a regression on it. (OrchestraBench,
   arXiv:2608.05263, 2026-08: tool faults recovered 1.0, ambiguous
   delegation 0.30, three latent/semantic modes 0.0 — "retry does not
   repair the latent modes — it reproduces the fault and only
   lengthens time-to-detection.")

## Live discussion (the room talks)
Seats don't just report — they discuss with each other, live. The
Chief runs it:

**On platforms with real subagents:**
1. The Chief spawns one subagent per participating seat and keeps them
   all alive for the session — nobody is closed until the verdict.
2. The Chief opens with the motion: the perfected prompt plus the exact
   question to resolve.
3. **Round 1 — positions:** each seat states its position with evidence,
   in phase order.
4. **Open floor:** any seat may answer any other seat — rebut, support
   with new evidence, or concede. The Chief relays the running
   transcript so every seat sees every point.
5. Rounds continue until consensus, or only wording remains.
6. **The gavel:** max 3 discussion rounds per question — then the Chief
   decides (or escalates). No filibusters.
7. The Chief synthesizes the verdict; each seat's final position is
   recorded in the ADR.

**Discussion rules (all platforms):**
- Address the point, not the seat. Bring evidence or concede.
- Never repeat a made point — new information or silence.
- Conceding when convinced is recorded as a win for the room.
- Blocking seats argue their block with evidence; the Chief can only
  overrule a block with the owner's written risk acceptance.

**Tabletop mode (no subagents):** the agent writes the debate as a live
dialogue in its response — seats answering each other by name, with
rebuttals and concessions, then the Chief's verdict. A real debate, not
a list of independent statements.

## Re-discussion ("discuss again")
When the owner says **"discuss again"** (variants: "re-discuss",
"debate it again", "run it back"), the room re-debates everything —
the original request *plus* every topic already discussed:
1. The Chief pulls the prior discussion record (ADRs, transcripts)
   from memory/log — nothing is re-argued from scratch.
2. The Prompt Writer restates the motion, with prior conclusions as
   context.
3. The Knowledge Wizard re-runs Phase 0: re-searches every term and
   checks for new or updated docs since last time. It briefs the
   *deltas* — "what's new since we last talked."
4. Seats re-debate live: each seat holds, updates (new evidence), or
   concedes its prior position. New seats may join if the topic grew.
5. The Chief synthesizes a new verdict, recorded as a new ADR that
   references the prior one(s).
**Honesty rule:** if repeated re-discussions produce no new
information, the Chief says so plainly and recommends a decision
instead of theater-debating.

## Promotion Gate — binding on all self-modification (Director rule, 2026-11-11)

The office now modifies itself continuously (Director mandate), so
self-modification gets the same discipline as production work. This
gate extends the 2026-10-30 evals regression rule to every
self-applied change, and it binds the Director's loop explicitly:

1. **Cite the evidence in the commit.** Every commit that changes a
   seat charter, a playbook, a skill, a routing rule, or the
   Director's own files names its evidence in the commit body: the
   eval run it passed (task set, score vs the standing baselines —
   v1 **59/60**, v2 **437/440**, zero critical misses), or, for
   process/documentation-only changes that alter no seat behavior,
   the line `process-only: no seat behavior changed` plus the
   validator result. A change with neither does not land.
2. **Behavior changes hold the bar.** A change that alters how any
   seat behaves ships only if the affected seats' eval tasks hold or
   beat baseline with zero critical misses — re-run at the next
   monthly learning review at the latest, and immediately when the
   change is large. A drop benches the change (revert + wing note),
   never gets argued past.
3. **Mistakes become tests.** Every Mistake Register entry spawns at
   least one regression task in `office/evals/` within one review
   cycle, sourced from the real failure. New eval tasks are filed as
   **capability** (target <100%, still being mastered) or
   **regression** (target ~100%; a drop blocks) — mastered capability
   tasks graduate to regression.
4. **Read the failures.** Before accepting any score change, the
   Director reads the failing transcripts, not just the numbers
   (the step practitioners skip, per Anthropic's eval guidance).
5. **Held-out discipline (v3+ waves).** A fixture set used to tune a
   change is never that change's promotion evidence. From v3 on,
   each wave splits its fixtures before any tuning: **train** (seats
   and the Director may inspect and iterate against them),
   **validation** (decides promotion), and **held-out** (never read
   during tuning; scored once at wave close — that score, not a
   train or validation score, is the number reported). v1 and v2 are
   already fully seen, so they stay honestly labelled what they are:
   regression baselines, never held-out evidence. (Evidence: Kiln
   AI Harness Tuner, Show HN 2026-11-13 — train/val/test enforced in
   code, test never read, "so the number you report is one it never
   optimized against.")

Source: Director research pass 1 (2026-11-11) — Anthropic,
*Demystifying evals for AI agents* (2026-01-09); The AI Runtime,
*Self-Improving Agents in 2026*; full report in the office wing
entry of the same date.

## Rules
- Skipping the War Room for production changes requires Sloane's
  explicit waiver, recorded as an ADR.
- Small, well-defined fixes may use `ship-feature` directly; anything
  touching architecture, auth, payments, personal data, or AI behavior
  goes through the War Room.
