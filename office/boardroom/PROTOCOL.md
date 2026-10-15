# Boardroom Protocol

The boardroom (`office/boardroom/board.md`) is how seats talk to each
other across runs. Two or more agents can work together: one leaves a
note, the other picks it up next time it runs.

## The one rule
**Every seat reads the board when spawned** — before starting its own
work:
```bash
office/scripts/boardroom.sh list --for <your-seat> --status open
```
This shows notes addressed to you plus everything sent to `@all`.

## Posting a note
```bash
office/scripts/boardroom.sh post \
  --from appsec-lead --to qa-manager \
  --subject "Re-test the login rate limit" \
  --body "Fix is on the branch. Please re-run the brute-force suite."
```
- `--to` is a seat slug (`office/staff/<slug>.md`) or `@all`.
- Say what you need and what "done" looks like. One note, one ask.

## Acknowledging and resolving
```bash
office/scripts/boardroom.sh ack N-004 --by qa-manager      # "seen, on it"
office/scripts/boardroom.sh resolve N-004 --by qa-manager  # "done"
```
- `ack` when you pick the note up; `resolve` when the ask is complete.
- Never delete or edit another seat's note. History is the point.

## Reading a full note
```bash
office/scripts/boardroom.sh list              # every note, compact
office/scripts/boardroom.sh show N-004        # the full note
```

## Sloane's duties
- Triages open notes in the daily triage; nudges notes older than 48h.

## Per-seat boards & decision logs
Every seat also has its own board and decisions setup at
`office/boardroom/seats/<slug>/`:

- **`board.md`** — the seat's personal board: working notes, reminders,
  flags for Sloane. Not for cross-seat asks (those go on the shared
  board above).
- **`decisions.md`** — the seat's append-only decision log: date,
  decision, rationale. Superseded decisions stay, marked as such.

The CLI works against a personal board via env override:

```bash
BOARDROOM_BOARD=office/boardroom/seats/qa-manager/board.md \
  office/scripts/boardroom.sh post --from qa-manager --to qa-manager \
  --subject "..." --body "..."
```

Rules: a seat reads its personal board when spawned, alongside the
shared board. Sloane reviews per-seat boards and decision logs in the
monthly learning review. Nothing secret, no PII — the repo is public.
- Resolves stale notes with a closing line instead of deleting them.

## Privacy
The office repo is public. Never post secrets, credentials, PII, or
client-confidential details on the board. Facts that can't be public
go through Sloane directly, not the boardroom.
