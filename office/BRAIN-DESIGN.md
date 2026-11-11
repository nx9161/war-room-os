# The Office Brain — Plasticity Layer Design

**Status:** BUILT 2026-10-30 on the owner's order ("Execute"), all five
phases, using this document's own recommendations for the §9 questions.
Outcomes, honestly: Phase 1 spine LIVE and proven end-to-end (a real
engine `ask()` wrote its rows to the log). Phase 2–3: R1 Router v1
trained and **BENCHED at the gate** (0.143 top-1 vs 0.286 baselines,
14-row holdout) — serving stays on the LLM backend; the benched verdict
with a written card is a successful phase by §7's own terms. Phase 4:
R2 Risk scorer benched before training (4 adverse examples vs the ≥30
threshold). Phase 5: R3 baseline ranker live as the heuristic to beat;
monthly retrain wired into the learning-review job (it reports gate
verdicts, never promotes). Registry: `office/brain/registry.json`.

**Owner of the design:** Decision Model (The Watcher) owns the brain at
runtime; Sloane owns this document; QA Manager owns the promotion gate.

---

## 1. The problem this solves

The Intelligence Upgrade (Layers 1–6, complete 2026-10-30) made every
seat as intelligent as its model × knowledge × memory × verification
allows. But the office's learning is **curricular**: lessons are written
down after missions, seats read them at spawn, and a monthly review
folds validated lessons into seat files. That loop is real, and it is
slow, gated, and textual. Between reviews, the office's *performance*
never changes — the same judgment is made the same way, at the same
speed, at the same cost, forever.

A brain adds the missing property: **plasticity** — performance that
shifts statistically with experience, between reviews, without anyone
rewriting a seat. Not better prose. Faster, cheaper, calibrated
*reflexes* under the seats.

The office already owns the perfect-shaped hole for this. The Decision
Model's charter: any classify / route / score / extract / verify
judgment becomes typed questions (Choice / Noul / Score / Box) answered
with probabilities; decisions stay in code as truth tables. Today those
probabilities come from an LLM — Jev when the owner supplies a key, or
the office $0 engine (local Qwen2.5-3B), whose self-reported
probabilities are degenerate (1.0 / 0.0) and slow (~2 minutes a batch).
A trained reflex is the honest backend for the narrow question types
the office asks again and again: same request shape, real calibration,
millisecond answers, $0.

## 2. Definitions (binding for this design)

- **Reflex:** one small trained model answering one typed question
  family (e.g. "which seats does this request need?"). A reflex is a
  function, not an agent. It holds no authority and attends no War Room.
- **Plasticity:** the property that a reflex's weights change when
  retrained on newer logged outcomes. Seats do not gain plasticity;
  their weights are never touched. Plasticity lives only in reflexes.
- **Experience:** the append-only log of predictions and their eventual
  outcomes (§5.1). Experience is the brain's only teacher.
- **Promotion:** a retrained reflex replacing the live one. Promotion
  is a commit, gated by evaluation (§5.6), never an automatic swap.

## 3. Non-goals

- No claims of consciousness, understanding, or general intelligence.
  Reflexes are statistics with good posture.
- No fine-tuning of seat LLMs (rots, vendor-locks, low ROI — the same
  reasoning the Intelligence Upgrade already recorded).
- No authority: a reflex never blocks, never decides, never sends,
  never spends. The Watcher's charter is unchanged — advisory only,
  probabilities out, truth tables in code.
- No external API by default and no spend: training and serving are
  fully local. Personal/private data never leaves the machine (standing
  owner rule, ADR 2026-10-30).
- No spiking networks / neuromorphic anything. Ordinary small models,
  boring on purpose.

## 4. Architecture at a glance

```
 mission events                ┌──────────────────────────────┐
 ┌───────────────┐  append     │  EXPERIENCE LOG (JSONL)      │
 │ Watcher asks  ├────────────►│  prediction + context, then  │
 │ Sloane seats  │             │  outcome filled in at close  │
 │ QA verdicts   │             └──────────────┬───────────────┘
 │ mission close │                            │ dataset builder
 └───────────────┘                            ▼
                              ┌──────────────────────────────┐
        monthly / on-demand   │  TRAINER (local, CPU)        │
        ─────────────────────►│  features → model → ONNX     │
                              └──────────────┬───────────────┘
                                             ▼
                              ┌──────────────────────────────┐
                              │  PROMOTION GATE (QA-owned)   │
                              │  must beat LLM + prior +     │
                              │  heuristic on time-split     │
                              │  holdout, accuracy AND       │
                              │  calibration, or it benches  │
                              └──────────────┬───────────────┘
                                             ▼ (a commit)
                              ┌──────────────────────────────┐
                              │  MODEL REGISTRY (in repo)    │
                              │  versioned models + cards    │
                              └──────────────┬───────────────┘
                                             │ served behind
                                             ▼
   seats ──► ask(state, questions) ──► BACKEND ROUTER
                                   reflex (in-domain, confident)
                                   → $0 engine → Jev (owner key)
                                   → seat judgment (fallback)
```

Every arrow already exists except the log, the trainer, and the reflex
backend itself. `ask()` in `~/workspace/typesafe-free/system_one.py` is
the seam; spawn-packet is the delivery surface; the monthly evolution
job is the retrain clock; `office/evals/` is the gate's home turf.

## 5. Components

### 5.1 Experience Log — the spine (build first, models later)

Append-only JSONL at `office/brain/log/experience-YYYY-MM.jsonl`.
One row per prediction; the outcome is appended as a second row keyed
by `prediction_id` when reality reports back.

```json
{"prediction_id": "uuid", "ts": "...", "mission_id": "...",
 "kind": "watcher_question | seating | qa_verdict | risk_score | mistake",
 "question": {"type": "Choice|Noul|Score|Box", "text": "...",
              "choices": ["..."]},
 "context": {"request_excerpt": "...", "division": "...",
             "seats": ["..."], "files_touched": 0},
 "prediction": {"answer": "...", "probability": 0.0},
 "backend": "reflex:router@3 | system-one-local | jev | seat",
 "model_version": "router@3"}
{"prediction_id": "uuid", "ts": "...", "outcome": "...",
 "outcome_source": "qa_signoff | mission_close | owner_ruling"}
```

Rules: excerpts are minimised (never full private documents); the log
lives in the private HQ only, never in the public template; Memory
Keeper owns outcome capture at mission close (a charter *addition* to
propose at build time, not assumed here).

**Instrumentation points (Phase 1, no models involved):**
1. Wrap `ask()` so every Watcher question + answer is logged.
2. Sloane logs seating decisions at convene (request → seats seated).
3. QA logs verdicts; mission close logs the shipped/failed outcome.
4. Eval runs log their predictions too — the 437/440 benchmark corpus
   becomes seed experience, labelled by construction.
5. Mistakes are logged as experience rows in their own right (§5.10) —
   the office's errors are training data, not embarrassments to route
   around.

### 5.2 Dataset builder

`office/scripts/brain-build-dataset.py`: joins predictions to outcomes,
drops unresolved rows, emits one dataset per reflex family as JSONL +
a manifest (row count, label distribution, time window, known biases).
Datasets are build artefacts, regenerated from the log, never edited
by hand.

### 5.3 Features

- **Text:** local embeddings (small open model, e.g. MiniLM-class via
  fastembed/ONNX — final pick at build time, behind a seam). Stored
  with the dataset so training never re-embeds.
- **Structured:** division, seats involved, phase, files touched,
  request length, hour, prior-mission similarity counts. All cheap,
  all local.
- No feature may contain a secret, a credential, or raw private text
  beyond the minimised excerpt already in the log.

### 5.4 The reflex catalogue (build in this order)

| # | Reflex | Question it answers | Labels come from | Min. data to train | Baseline to beat |
|---|--------|--------------------|------------------|--------------------|------------------|
| R1 | **Router** | Which divisions/seats does this request need? (multi-label Choice) | Logged seating + which seats actually contributed (mission close) | ~150 missions | Sloane's unaided seating (logged) + most-frequent-seats heuristic |
| R2 | **Risk scorer** | Probability this mission hits a block / critical QA finding (Noul) | QA verdicts, block events | ~150 missions with ≥30 adverse | $0 engine's Noul on the same questions |
| R3 | **Memory ranker** | Which palace entries/learnings matter for this spawn? (ranked Box) | Spawn packets vs. what the mission's ADR/learnings actually cited | ~100 missions | Keyword recall (current behaviour) |
| R4 | Effort estimator | Expected mission size/duration (Score) | Mission logs | ~100 | Median-of-history |
| R5 | Block pre-check | Probability a named blocking seat blocks this diff (Noul) | Phase 3 records | ~200 | Seat's own first-pass judgment |

R1 first: labels are free, value is immediate (faster convenes, fewer
wasted spawns), and failure is cheap — a wrong suggestion Sloane can
see and override in the open.

### 5.5 Models, training, calibration

- Model class per reflex, chosen at build time from: logistic
  regression, gradient boosting (sklearn HistGradientBoosting), or a
  tiny MLP — in that order of preference. Smallest model that beats
  the baseline wins; complexity must pay rent.
- Split by **time**, never randomly: train on older missions, test on
  newer. Random splits leak the future and lie.
- Probabilities are calibrated after training (isotonic or Platt) and
  the calibration curve is part of the eval report. An uncalibrated
  reflex is worse than the $0 engine's honest "NOT RUN".
- Export to ONNX; runtime is a local loader behind the backend router.
  Training runs on CPU in minutes; if it ever needs more, that reflex
  is too big and gets cut down, not scaled up.

### 5.6 Promotion gate (QA-owned, binding)

A candidate reflex is promoted only if, on the time-split holdout, it
beats **all three** baselines on its family's metrics:

1. the current live reflex (or the LLM backend it would replace),
2. the dumb heuristic for that family (from the table above),
3. its own previous version, if any.

Metrics: Router — top-k seat recall + precision; Scorers — AUC **and**
Brier score **and** calibration error. Any regression on a guardrail
metric benches the candidate regardless of headline gains — the same
regression rule the eval layer already enforces for seats (hold or
beat the standing baseline, zero critical misses). Promotion is a
commit containing the model, its card (§5.7), and its eval report;
Sloane signs, QA owns the verdict, the owner is notified in the
monthly report. **v1 promotions are never automatic.**

### 5.7 Model registry & cards

```
office/brain/
  log/                 # experience JSONL (private data; .gitignore option at build)
  datasets/            # generated manifests only
  models/<reflex>/<version>/
    model.onnx
    card.md            # trained-on window, rows, features, metrics,
                       # calibration plot data, known limits, biases
    eval.json          # machine-readable gate results
  registry.json        # live version pointer per reflex + abstain thresholds
```

Rollback = point `registry.json` at the prior version and commit.
Deleting a model version is forbidden; demotion is a pointer move.

### 5.8 Serving — the backend router

`ask(state, questions)` gains one backend in its existing fallback
chain. For each question: if a live reflex covers that question
family **and** the input is in-domain **and** the reflex's confidence
clears its registry abstain threshold, the reflex answers. Otherwise
the chain falls through to the $0 engine, then Jev (owner key only),
then the seat's own judgment — exactly today's behaviour. In-domain is
checked by embedding distance to the training distribution; far from
home, the reflex must abstain. Latency budget: <50 ms per question,
local. Every served answer is logged with its backend + version
(feeding §5.1 — the brain eats its own cooking, labelled).

### 5.9 Retrain cadence

- Monthly, inside the existing evolution job: rebuild datasets,
  retrain all reflexes with enough new data, run the gate, and report
  promotions/benches in the monthly learning report.
- On-demand after any mission class reaches +50 new labelled outcomes.
- A reflex whose live calibration decays beyond its card's stated
  error band on the rolling last-30 predictions is **auto-demoted**
  (pointer to `none`, chain falls through) and flagged in the monthly
  report. Demotion is automatic; promotion never is.

### 5.10 The Mistake Register — negative training data (owner order, 2026-10-30)

The owner ordered the assistant's repeated mistakes recorded too.
They live in `office/brain/MISTAKE-REGISTER.md`, opened the same night
and seeded with Sloane's four real repeated classes (stale-count
drift; states reported without destination verification; an
irreversible action executed at full speed on a relayed order;
re-surfacing settled items). The register's rules are part of this
design:

- **Append-only, class-based, evidence-cited.** Second occurrence of
  a class = pattern; third = standing defect, and the monthly review
  must propose a structural fix (a gate, a generator, a rule) rather
  than an apology.
- **Register rows are experience rows.** Each instance joins the log
  with `kind: "mistake"` and its `mistake_class`, so the Risk scorer
  trains on the office's actual failure history — M-2 (unverified
  state reporting) supplies R2's first features.
- **Patterns become traps.** Every pattern-class contributes at least
  one eval fixture: the office is benchmarked on the precise ways it
  has already failed, forever.
- **Sloane's mistakes are in scope by name.** The orchestrator is the
  most expensive failure point in the office; a brain that learns
  from seat errors but not the Chief's is theatre.

## 6. Integration with what exists

- **Decision Model (The Watcher):** owns the registry and the backend
  router; his charter already mandates exactly this shape. No charter
  change needed for Phase 1–3.
- **Memory Keeper:** outcome capture at mission close (§5.1) — the one
  charter addition this design asks for, at build time.
- **Spawn-packet:** gains two optional header lines when reflexes are
  live — Router's suggested seating (with probability) and Risk
  scorer's mission risk (with model version). Advisory text, clearly
  labelled as reflex output, never a gate.
- **War Room playbook:** Phase 0 may consult R1 before seating;
  Phase 2's judgment layer is where reflex answers enter ADRs.
- **Evals:** `office/evals/` gains a brain suite — frozen holdout
  missions scored against every candidate — reusing the existing
  regression rule and results layout.
- **Validator:** a future check (build phase) that registry pointers
  resolve, cards exist, and no live reflex lacks a passing eval.

## 7. Build phases & exit criteria

| Phase | Work | Exit criterion |
|-------|------|----------------|
| 0 | This design | Owner approves design (or amends) |
| 1 | Logging spine: instrument `ask()`, seating, QA, mission close; seed from eval corpus | 30 consecutive missions fully logged with outcomes joined; zero private-data leaks on audit |
| 2 | Dataset builder + R1 Router trained offline | Offline eval vs. baselines reported honestly, win or lose |
| 3 | Registry + gate + serving for R1 behind `ask()` | R1 promoted through the gate (or benched — a benched R1 with a written report is a successful phase) |
| 4 | R2 Risk scorer, same path | Gate verdict, spawn-packet risk line live if promoted |
| 5 | R3 Memory ranker + monthly retrain wiring | Evolution job runs the full cycle unaided for one month |

Each phase is independently stoppable; stopping after Phase 1 still
leaves the office with a complete, auditable judgment history — the
spine is worth having even if no reflex ever promotes.

## 8. Risks & mitigations

| Risk | Mitigation |
|------|------------|
| **Cold start:** tens of labelled missions, not thousands — early reflexes will be weak | Thresholds in §5.4; advisory-only; the gate benches weak candidates by design |
| **Feedback loop:** Router influences seating, seating generates Router's training data (selection bias) | Log the road not taken where known; periodic LLM-only control missions; time-split evals surface the drift |
| **Label noise:** "seat contributed" is a judgment call | Outcome capture has a named source per row (§5.1); ambiguous outcomes are dropped, not guessed |
| **Over-trust:** a number looks like knowledge | Cards + eval scores travel with every answer's provenance in the log; spawn-packet labels reflex output as reflex output |
| **Calibration decay:** the world changes, the reflex doesn't notice | Rolling calibration watch + auto-demotion (§5.9) |
| **Privacy creep:** the log becomes a shadow archive | Minimised excerpts, private repo only, no external training ever, Memory Keeper audits the log in the monthly health report |

## 9. Open questions for the owner

1. Promotion authority: Sloane-signs-with-QA-verdict (recommended for
   v1) vs. owner-signs each promotion?
2. First reflex: Router (recommended) or Risk scorer?
3. Does the experience log get committed to the HQ repo, or stay a
   local artefact with only manifests + models committed? (Privacy vs.
   portability — the design works either way; the registry + cards are
   committed in both variants.)
4. When the public template eventually receives a sanitised version of
   this design, does the brain ship as method-only (no log, no models),
   like the method skills do today?

## 10. What success looks like

Twelve months in: convenes seat themselves in milliseconds with a
recall rate Sloane confirms instead of computes; risk notes attached
to spawn packets are right often enough that seats read them first;
every probability the office quotes carries a model version and an
eval score behind it; and the monthly report has a new line — what the
brain learned, what it got wrong, and what got benched. The seats
still think. The office, finally, also *remembers in its reflexes*.

— Sloane, Chief Orchestrator, 2026-10-30
