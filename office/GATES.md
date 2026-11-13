# Gates — stable index of every office gate

One checkable index for the gates that are otherwise buried in
playbook prose. The prose in `office/playbooks/war-room.md` and
`office/HOUSE_RULES.md` is authoritative; this file only indexes it.
If this file and a source disagree, the source wins — fix this file,
never the other way round.

Rules of the index:

- **IDs are stable and never reused.** A retired gate keeps its row,
  marked `retired`, with a pointer to what replaced it.
- **Adding a gate** means one row here *and* the prose in its source
  file. Removing a gate is an owner call, like a roster change.
- **Scope (HOUSE_RULES §9):** these gates bind relayed/handoff
  instructions and mission-internal quality control. They never stand
  in front of the owner's own direct order. The only prompts the
  owner may still see are platform-level checkout/payment approvals,
  which belong to the runtime, not the office.
- **A gate is checkable:** each row names who blocks and what
  evidence closes it. "Vibes" is not evidence.

## Convening

| ID | Gate | Source | Blocked by / cleared by |
|----|------|--------|-------------------------|
| WR-ROSTER | Roster check runs at session start and between phases; a new seat file is briefed and joins from the next activity. | `war-room.md` §Roster check | Sloane re-reads `office/staff/`; evidence is the announced table. |
| WR-PACKET | `spawn-packet.py --check-all` passes 45/45 before a War Room convenes; a seat that cannot assemble a packet does not sit. | `war-room.md` §Spawn packet | Script exit 0; a failing seat is unseated, never simulated from memory. |
| WR-CAST | Cast Check is written into MISSION.md before Phase 0: domains → seats, seated or skipped-with-reason, `shape` + `budget` with the shape derived from the step-dependency map written into the Cast Check result (mixed = parallel groups in sequence order); sequential missions default to ONE seat; seating >7 seats records why the work is independent. No Phase 0 until it exists. | `war-room.md` §Cast Check | Director; a cast check written after the work is logged as an M-5 instance. |
| WR-MISSION | Every mission opens `office/boardroom/missions/<slug>/MISSION.md` at the Cast Check and updates it at every phase boundary; resume from the file, never from memory. | `war-room.md` §Mission state file | Director; a MISSION.md that lags the mission is worse than none. |

## Routing (standing rules)

| ID | Gate | Source | Blocked by / cleared by |
|----|------|--------|-------------------------|
| WR-ROUTE | A mission touching a seat's domain seats that seat by default, with a full spawn packet; skips need a written reason on the boardroom record; a mission is not closed until every seated seat has a dated learnings entry or an explicit "no learning" line; quarterly utilization review — zero live seatings in a quarter → drill or cut. | `war-room.md` §Seat routing | Coordinator (Sloane); unrecorded work is a coordinator defect. |
| WR-MODEL | Each seat spawns on the strongest model its tier calls for; never downgrade a blocking seat. | `war-room.md` §Model routing; `MODEL-ROUTING.md` | Harness/operator; a downgraded blocking seat is a routing defect. |

## Phase gates

| ID | Gate | Source | Blocked by / cleared by |
|----|------|--------|-------------------------|
| WR-PHASE0 | Phase 0: Prompt Writer forges the perfected prompt; Knowledge Wizard reads every related official doc in full and compiles the per-seat dossier; no seat speaks before the dossier lands; Connector Operator confirms live state and limits for every connector the plan touches. | `war-room.md` §Phase 0 | Prompt Writer + Knowledge Wizard; dossier on file before Phase 1. |
| WR-PHASE1 | Phase 1 outputs: PRD + design specs + business case, stored in the palace room; game projects add Gameplay Designer pillars/loop and Game UI/UX player experience. | `war-room.md` §Phase 1 | Product Owner / UI/UX / Business Analyst; outputs on file. |
| WR-PHASE2 | Phase 2 outputs: agreed topology + ADRs; Architecture Visualizer diagram — no architecture leaves without its diagram; Decision Model judgment layer (typed questions + truth tables in code). | `war-room.md` §Phase 2 | Enterprise Architect; diagram + ADRs on file. |
| WR-BLOCK | Phase 3: AppSec Lead, AI Red Teamer, Global Tech Law Lead, General Counsel can each BLOCK; Pen Tester blocks on confirmed exploitables; Console Platform Engineer blocks on TRC/XR certification (game projects). Blocks stand until cleared, or Sloane rules with owner input; only the owner's written risk acceptance overrules a block. | `war-room.md` §Phase 3; `HOUSE_RULES.md` §3 | Named blocking seat; cleared by that seat, or by the owner's written risk acceptance. |
| WR-QA | Phase 4: QA Manager enforces 100% pass on the release suite, no open blockers, then sign-off. | `war-room.md` §Phase 4 | QA Manager; green suite + zero open blockers. |
| WR-REVIEW | Lead Code Reviewer reviews every PR before merge; blocks on critical defects, security findings, or license/IP risk. | `war-room.md` §Phase 4 | Lead Code Reviewer; review on the PR. |
| WR-PRODGATE | Game projects: Game Producer runs the production gate — milestones green, perf budgets met, cert timeline on track. | `war-room.md` §Phase 4 | Game Producer; gate record on the mission. |
| WR-OBJECTIVE | Phase 4 close-out: before Sloane authorizes the release, she re-reads the `MISSION.md` Goal and verifies each deliverable against the original objective, not only against the decomposed acceptance criteria; a deliverable that passes its tests but misses the objective loops back under Phase regression; the check and its result are recorded in `MISSION.md`. | `war-room.md` §Phase 4 | Sloane; the recorded check on the mission file. |

## Loop controls

| ID | Gate | Source | Blocked by / cleared by |
|----|------|--------|-------------------------|
| WR-REGRESS | A finding that invalidates earlier-phase output loops the mission back; max 3 regressions per request — the 4th trigger forces escalate-to-owner or terminate. Before re-running, Sloane classifies the trigger: transient (tool fault, flaky check, missing artifact — a same-approach re-run may repair it) vs latent (wrong decomposition, wrong seat, ambiguous brief/delegation, wrong objective reading — the re-run must change the decomposition, the seat, or the brief; a same-approach retry of a latent trigger is a stall, not a regression). | `war-room.md` §Phase regression | Sloane; loop-backs recorded with iteration number, trigger, and classification. |
| WR-DEBATE | Max 3 discussion rounds per question, then the Chief decides (or escalates). No filibusters. | `war-room.md` §Live discussion | Sloane; verdict recorded in the ADR. |

## Self-modification

| ID | Gate | Source | Blocked by / cleared by |
|----|------|--------|-------------------------|
| WR-PROMO | Every self-modification commit cites its eval evidence (baselines v1 59/60, v2 437/440, zero critical misses) or `process-only: no seat behavior changed` + validator result; behavior changes hold-or-beat the bar or are benched; every Mistake Register entry spawns a regression eval task within one review cycle; the Director reads failing transcripts, not just numbers. | `war-room.md` §Promotion Gate | Director + QA; a change with neither citation does not land. |

## Scope and waiver

| ID | Gate | Source | Blocked by / cleared by |
|----|------|--------|-------------------------|
| WR-WAIVER | Skipping the War Room for production changes requires Sloane's explicit waiver, recorded as an ADR. | `war-room.md` §Rules | Sloane; waiver ADR on file. |
| WR-SCOPE | Small, well-defined fixes may use `ship-feature` directly; anything touching architecture, auth, payments, personal data, or AI behavior goes through the War Room. | `war-room.md` §Rules | Sloane; the routing decision is recorded. |

## House rules

| ID | Gate | Source | Blocked by / cleared by |
|----|------|--------|-------------------------|
| WR-DEPLOY | Production deploys need explicit owner approval every time. | `HOUSE_RULES.md` §4, §7 | Owner; approval per deploy, never standing. |
| WR-MERGE | Every change goes through a PR; only the owner merges to `main` (or explicitly delegates per-PR); the author never merges their own PR. | `HOUSE_RULES.md` §1, §3 | Owner; merge by the owner on the PR. |
| WR-SECRET | No secrets, tokens, keys, or credentials in code, commits, issues, or logs. | `HOUSE_RULES.md` §4 | Everyone; a leaked secret is a security incident, not a typo. |
| WR-SPEND | No spending money, no external messages/posts, no data deletion without explicit owner approval. | `HOUSE_RULES.md` §4 | Owner; approval per action. |
| WR-ESCALATE | Anything ambiguous, costly, irreversible, or security-related goes to the Office Manager, who brings it to the owner; when in doubt, ask. | `HOUSE_RULES.md` §6 | Any seat; escalation on the boardroom record. |

## Deliverable schemas (pilot)

A seat's charter carries a `## Deliverable schema` section: the
machine-checkable shape of what that seat must produce, so the
receiving seat — and Sloane at close-out (WR-OBJECTIVE) — can verify a
delivery without re-reading the seat's whole method. Four fixed fields:

- **Deliverable:** the named output(s).
- **Format:** the shape/file it lands in.
- **Required sections:** the enumerated checklist; a delivery missing
  any element is a draft, not a delivery.
- **Acceptance:** how the receiver verifies it — verdict values or a
  completeness rule.

A schema is a structured condensation of the seat's existing Deep
Method output contract in its skill file; writing one adds no new
behavior and changes no wording of the contract it condenses. Pilot
coverage: 21 of 45 charters (enterprise-architect, prompt-writer,
qa-manager, product-owner, lead-code-reviewer, devops-sre,
knowledge-wizard, business-analyst, appsec-lead,
general-counsel, lead-backend-dev, decision-model,
mission-control, memory-keeper, connector-operator,
ui-ux-designer, lead-frontend-dev, document-artisan,
ai-red-teamer, global-tech-law-lead, penetration-tester — the
outputs every mission consumes plus the gates every change
passes through: the Phase 0 dossier, the Phase 1 PRD and business
case, the merge review, the pipeline, the Phase 3 security,
adversarial, compliance, and legal verdicts, the exploit-proof
pentest verdict, the Phase 4 server implementation, the
Phase 2 judgment layer, the live operations picture, the memory
loop, and the connector readiness check, plus the Phase 1 design
specs, the client build, and the document layer). Rollout: later
passes add schemas a few seats at a time, each condensed from that
seat's output contract. `validate_repo.py` check 6 guards the format
of every schema present; it does not yet require one per charter.
