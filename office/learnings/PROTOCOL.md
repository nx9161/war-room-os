# Continuous Learning Protocol

Every agent gets better constantly. Not as a slogan — as a mechanism:

1. **Log after every mission.** Each seat appends to its file in
   `office/learnings/<seat-slug>.md`:
   - Date and mission
   - What worked
   - What failed
   - What changes next time
2. **Read when spawned.** Every seat reads its learnings file before
   starting work — never repeat a solved mistake.
3. **Monthly review.** Sloane reviews all learnings files, validates
   the patterns, and folds real improvements into the seat files
   **and their skills** (`office/skills/<seat>/SKILL.md`). Seats and
   skills evolve together; the roster never stagnates.
4. **Share the big ones.** A learning that affects other seats goes on
   the boardroom as well (`@all`).
5. **Reconcile when instructions change.** A seat reads its learnings
   before starting work, so a stale learning can override a fresh
   instruction. Whenever a seat's charter, skill, or method changes,
   the same change reviews that seat's learnings file: any entry that
   contradicts the new instruction is marked superseded — dated, with
   a pointer to the new instruction (the typed-supersession pattern
   from the Memory Operations Protocol) — never silently edited or
   deleted. A new dated entry records the instruction change itself,
   so the file stays an honest history, not a trap.
6. **Distill at the monthly review: the live file stays short.** A seat
   re-reads its whole learnings file at every spawn, and a long memory
   file is a liability, not an asset: uncurated agent memory drifts —
   it remembers the wrong things and turns them into a standing focus
   (HN, "Agent memory needs its OpenTelemetry moment", 2026-11-08).
   Anthropic's own guidance for the same shape of file is a hard
   ceiling — only the first 200 lines / 25 KB of a memory index load
   at session start, and longer instruction files reduce adherence
   (code.claude.com/docs/en/memory). So at the monthly review, any
   entry already folded into the seat's charter or skill (rule 3) is
   marked folded — dated, with a pointer to where it landed — and
   moved to `office/learnings/archive/<seat-slug>.md`. The archive is
   history: never re-read at spawn, never edited. The live file holds
   only still-live, not-yet-folded learnings and stays under ~150
   lines; a file that crosses the cap is distilled at the next review,
   never left to grow. Entries that contradict a new instruction are
   handled by rule 5 (superseded in place), not by this rule.

The file is the memory; the monthly review is the evolution.
