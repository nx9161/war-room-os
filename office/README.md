# Office Handbook

Welcome to the office. This folder is the office's memory and rulebook.

- **HOUSE_RULES.md** — binding rules for every employee.
- **PLAN.md** — the founding plan.
- **staff/** — employee profiles. Hiring someone new = adding a file here.
  45 roles in 7 divisions:
  - *Product & UX:* product-owner, ui-ux-designer, business-analyst,
    voice-designer, document-artisan, word-specialist,
    excel-specialist, diagram-designer, art-director,
    launch-strategist, sales-agent, scriptwriter, product-visualizer,
    seo-specialist, social-media-strategist
  - *Architecture & Code:* enterprise-architect, lead-backend-dev,
    lead-frontend-dev, architecture-visualizer, mcp-maker,
    lead-code-reviewer, harness-engineer, decision-model
  - *Security & Compliance:* appsec-lead, ai-red-teamer,
    global-tech-law-lead, reverse-engineer, penetration-tester
  - *Quality & Ops:* qa-manager, devops-sre, prompt-writer,
    knowledge-wizard, memory-keeper, mission-control,
    casting-director
  - *Legal & Governance:* general-counsel
  - *Games:* game-architect, gameplay-designer, game-ui-ux-designer,
    console-platform-engineer, game-producer
  - *Finance:* financial-analyst, tax-strategist
  - *Connector operations:* connector-operator (one seat;
    103 per-connector runbooks in `office/runbooks/connectors/`)
  - *Leadership:* sloane (Chief Orchestrator)
- **playbooks/** — repeatable procedures, run by spawning one subagent
  per step: `intake`, `war-room`, `ship-feature`, `fix-ci`,
  `skill-hunt`, `seat-routing-table`
  (the per-seat triggers for the standing seat-routing rule).
- **runbooks/connectors/** — one runbook per connector (status,
  gates, canonical surface), operated by the Connector Operator.
- **boardroom/** — the inter-agent noteboard (`board.md` + `PROTOCOL.md`).
  Every seat checks it when spawned; any seat can leave a note for any
  other seat. CLI: `scripts/boardroom.sh`.
- **skills/** — capabilities the Knowledge Wizard hunted across the
  internet, vetted, and installed (`office/skills/<slug>/SKILL.md`).
- **scripts/** — automation, e.g. `deploy_target.sh` (USB device deploy).
- **palace/** → retired; memory now lives in `/memory/` (see repo-root
  `AGENTS.md` for the Memory Operations Protocol).
- **log/decisions.md** — every significant decision, dated.
- **log/runs/** — journal entries for each task run.

## Giving the office work
Open a GitHub Issue describing what you want, or tell the owner in chat.
Attach screenshots or voice notes — the intake procedure handles all
three. Small, well-defined tasks labeled `ready` may be picked up
automatically by the daily triage. Production-significant work goes
through the War Room first.
