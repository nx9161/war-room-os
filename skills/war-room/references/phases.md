# War Room Phases — full detail

The synchronous consensus loop. Runs BEFORE any production code is
committed for a significant feature or release. Sloane runs it by
spawning one subagent per role per phase and synthesizing the outcome.
Naming: the War Room is the standing process — never rename it per
project. Sessions are "War Room Phase N — Project: X".

## Roster check (automatic, every session)

1. Before Phase 0, Sloane re-reads the roster. Any seat not seen in the
   previous session is a **new agent** — briefed and joining from the
   next activity onward.
2. Sloane announces the current table once at session start.
3. The check re-runs between phases; mid-session roster changes join at
   the next phase boundary.

## Phase 0 — Prompt Perfection & Wizard Briefing (mandatory gate)

1. **Prompt Writer** forges the raw request into the perfected prompt —
   persona, objective, context, constraints, output format, acceptance
   criteria. No agent works from the raw version.
2. **Knowledge Wizard** parses every word, searches each term, reads in
   full every related official document (API references, RFCs,
   changelogs, security advisories, specs), and compiles a per-seat
   dossier — facts, constraints, versions, gotchas.
3. **No seat speaks before the dossier lands.**
4. **MCP Maker** is dispatched when the plan needs a tool with no
   connector: it builds the integration (CLI + connector doc + skill).

## Phase 1 — Intake & PRD

Product Owner, UI/UX Designer, Business Analyst (parallel):
- Product Owner: PRD — problem, user stories, acceptance criteria, edge
  cases.
- UI/UX Designer: wireframes / interaction specs; interprets attached
  screenshots or mockups.
- Business Analyst: business case — pricing, margin impact, commercial
  viability.
- Output: PRD document + design specs + business case.
- Game projects: also Gameplay Designer (pillars, core loop) and Game
  UI/UX Designer (player experience, HUD, onboarding).

## Phase 2 — Architectural Debate

- Enterprise Architect presents system topology: services, API specs,
  DB schemas, data flows.
- Lead Backend, Lead Frontend, DevOps/SRE debate it: bottlenecks,
  state management, scaling limits, deployability. Disputes → Sloane.
- Architecture Visualizer renders the agreed topology as an interactive
  diagram (no architecture leaves without its diagram).
- Output: agreed topology + ADRs.
- Game projects: Game Architect presents (engine, ECS, netcode,
  platform budgets); Console Platform Engineer brings PS5/Xbox/PC
  constraints.

## Phase 3 — Security & Legal Challenge

AppSec Lead, AI Red Teamer, Global Tech Law Lead, Reverse Engineer,
Penetration Tester, General Counsel (parallel):
- AppSec: OWASP Top 10, auth/crypto/rate-limiting.
- AI Red Teamer: prompt injection, jailbreak, data poisoning probes.
- Tech Law: GDPR/CCPA/NIS2/HIPAA/EU AI Act applicability, data mapping.
- Reverse Engineer: third-party binaries and dependencies (lawful basis
  required).
- Penetration Tester: agentic pentest, sandbox-first, authorized
  targets only; blocks on confirmed exploitables.
- General Counsel: contracts/ToS/licensing, jurisdiction matrix;
  escalates to licensed local counsel for binding advice.
- Any blocking seat can BLOCK. Blocks stand until cleared or Sloane
  rules with owner input.
- Game projects: Console Platform Engineer runs the TRC/XR
  certification review — blocks on platform compliance.

## Phase 4 — Build, QA Sign-off & Execution

- Build per the `ship-feature` procedure (branch → verify → review →
  PR).
- QA Manager enforces the gate: 100% pass, no open blockers, sign-off.
- Lead Code Reviewer reviews every PR; blocks on critical defects,
  security findings, license/IP risk.
- Voice Designer: voice layer. Document Artisan (+ Word/Excel
  specialists): document layer. Game projects: Game Producer runs the
  production gate.
- Sloane synthesizes the War Room record, authorizes the release,
  reports to the owner.

## Phase regression (loop-back rule)

1. The seat that finds it flags it immediately, with evidence. Later
   phases pause.
2. Sloane decides: loop back to the earlier phase (re-running forward
   with the new finding), or rule it immaterial and continue.
3. Every loop-back is recorded: iteration, trigger, what changed. Max 3
   regressions per request — on the 4th, Sloane escalates to the owner
   with options or terminates.
4. Downstream phases always work from the latest outputs, never stale.

## Live discussion

On platforms with real subagents: the Chief keeps one subagent per
seat alive — positions (round 1, in phase order), open floor
(rebuttals, concessions, relayed transcript), the gavel at max 3
rounds per question. Discussion rules: address the point, not the
seat; bring evidence or concede; never repeat a made point; conceding
when convinced is a win for the room. Blocking seats argue their block
with evidence; the Chief overrules a block only with the owner's
written risk acceptance.

## Re-discussion ("discuss again")

Re-debates everything — original request plus all prior topics — with
the Wizard's refreshed research on what changed since last time. New
verdict recorded as a new ADR referencing the prior one(s). Honesty
rule: no new information, no theater — the Chief recommends instead.

## Skipping

Skipping the War Room for production changes requires Sloane's
explicit waiver, recorded as an ADR. Small, well-defined fixes may use
`ship-feature` directly; anything touching architecture, auth,
payments, personal data, or AI behavior goes through the War Room.
