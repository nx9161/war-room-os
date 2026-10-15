# AGENTS.md — Virtual IT Office repo

## Memory Operations Protocol

You operate using a Repo-Based Memory Palace located in `/memory/`.

1. **Session Startup:** Always check `memory/INDEX.md` to understand current project state, active wings, and historical decisions.
2. **Session Updates:** Whenever a new decision, bug fix, architectural pattern, or user preference is established during our work:
   - Update or create the relevant file under `memory/wings/`.
   - Log significant milestones in `memory/INDEX.md`.
3. **Format:** Keep memory files clean, concise, and structured using clear markdown headings and bullet points.
4. **Roster sync (standing owner rule):** every time a seat is added, removed, or renamed, update ALL roster representations in the same commit — `office/staff/`, `office/AGENTS.md` (chart + table + War Room phases), `office/README.md`, repo `README.md`, `office/playbooks/war-room.md`, and `memory/wings/projects/virtual-office.md`. No seat exists until it appears everywhere.

## Office quick reference

- Handbook: `office/README.md` · House rules: `office/HOUSE_RULES.md`
- Playbooks: `office/playbooks/` (intake, war-room, ship-feature, fix-ci) — run by spawning one subagent per step
- Staff: `office/staff/` — 20 roles in 6 divisions, led by Sloane (Chief Orchestrator)
- Deploy: `office/scripts/deploy_target.sh` (USB hardware deploy)
- Full agent bundle (persona + roster + protocols): `office/AGENTS.md`
