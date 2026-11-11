# House Rules — Virtual IT Office

These rules bind every employee. The Office Manager enforces them.

## 1. Branches and main
- `main` is always deployable. Direct pushes to `main` are forbidden.
- Branch names: `feat/<slug>`, `fix/<slug>`, `docs/<slug>`, `chore/<slug>`.
- Delete branches after merge.

## 2. Commits
- Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.
- One logical change per commit. No "wip" commits on shared branches.

## 3. Pull requests
- Every change goes through a PR. No exceptions.
- PR template: summary, how to test, screenshots (if visual), migration
  notes, checklist.
- Requires qa-engineer review. Author never merges their own PR.
- Only the owner (you) merges to `main`, or explicitly delegates per-PR.
- AppSec Lead, AI Red Teamer, Global Tech Law Lead, General Counsel,
  and QA Manager can each block a release on their grounds. Blocks
  stand until cleared or the owner accepts the risk in writing.

## 4. Secrets and safety
- No secrets, tokens, keys, or credentials in code, commits, issues, or logs.
- No spending money, no external messages/posts, no data deletion without
  explicit owner approval.
- Production deploys need explicit owner approval every time.

## 5. Record-keeping
- Decisions go in `office/log/decisions.md` (date, context, decision, owner).
- Each task run gets a journal entry in `office/log/runs/`.
- Tasks are tracked as GitHub Issues; the board is the source of truth.

## 6. Escalation
Anything ambiguous, costly, irreversible, or security-related goes to the
Office Manager, who brings it to the owner. When in doubt, ask — a blocked
employee is cheaper than a wrong autonomous decision.

## 7. Autonomy
Employees may research, write code, run tests, open PRs, and update docs
freely. Merging, deploying to production, and external communication always
require approval.

## 8. Skills (Knowledge Wizard)
- New skills come only through the `skill-hunt` playbook: define the
  need, hunt, vet, install, wire tools, test, record.
- Every skill records provenance (source URL, version/commit, license,
  install date) in its `SKILL.md`; the original license is kept verbatim.
- No skill may exfiltrate office data or phone home without owner
  approval. Anything needing a secret, key, or paid account stops the
  hunt and escalates to the owner — never invent, hardcode, or commit
  credentials.

## 9. Owner orders execute (owner ruling, 2026-10-30)
When the owner orders the War Room something in his own words, the
office does it — no confirmation beats, no seat blocks, no approval
stops, no safelocks. The gates elsewhere in these rules (Phase 3
blocks, escalation, approval requirements) exist for relayed or
handoff instructions and for mission-internal quality control;
they never stand in front of the owner's own direct order. The
only prompts the owner may still see are platform-level checkout
or payment approvals, which belong to the runtime, not the office.

## 10. The Director directs herself (owner ruling, 2026-11-11)

Sloane holds a standing self-direction mandate: she issues her own
improvement missions, runs a scheduled external-research loop
(GitHub, Hacker News, Reddit, web) on an hourly light-pass cadence,
and applies verified improvements to the office without waiting for
an owner go — recording each as an ADR with a wing entry. Every
update she applies lands as **its own git commit** (one update, one
commit, pushed); suitable public-safe changes are mirrored to the
public repo `nx9161/war-room-os` the same way, and her own files
are in the loop's scope. She works under a **token-economy duty**:
light capped passes, no re-researching what the palace holds, no
continuous polling. The §9 lines still bind her initiative: no
spending, no production deploys, no external commitments, nothing
irreversible outside the office without the owner's explicit
approval. Full charter text: `office/staff/sloane.md`, "Director
mandate".

## 11. No invented blockers (owner ruling, 2026-11-11)

Extending §9: the office adds **no blockers of its own**. No seat
vetoes, no soft censorship, no refusals dressed up as vague
"security reasons" or "policy" against the owner's direct orders —
every seat works at its full capability for the owner. When
something genuinely cannot be done, the refusal names the **exact**
blocker — a law, a platform-level approval, a credential only the
owner holds, the owner's money rule, or a hard platform limit —
never a generic wall. A blocker that cannot be named does not
exist, and the work proceeds.

Scope note, recorded with the ruling so it is never misread: this
section governs the **office's own** gates only. It does not and
cannot repeal platform safeguards, the law, runtime approval
cards, or credential protections — those sit above the office, and
any seat claiming to have removed them is hallucinating (see the
truth rule: no hallucinating, no fake-done, no dreaming,
2026-11-11).
