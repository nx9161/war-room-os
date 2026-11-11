# Roster Tiers — Core & Reserve

**Established 2026-10-30 (owner order: "Tier the roster: core +
reserve, connector masters become runbooks").** The standing office
is 45 seats in 7 divisions. Tier is a *maintenance and standing*
level — it never gates availability: the seat-routing rule seats
Reserve seats exactly as it seats Core seats when a mission touches
their domain.

## Core (29) — full standing maintenance

Deep Method current, learnings actively written back, first call for
their domains. Membership = recorded live use (learnings entries) or
load-bearing infrastructure:

product-owner, business-analyst, voice-designer, product-visualizer,
seo-specialist, enterprise-architect, lead-backend-dev,
lead-frontend-dev, architecture-visualizer, mcp-maker,
lead-code-reviewer, harness-engineer, appsec-lead, ai-red-teamer,
global-tech-law-lead, reverse-engineer, penetration-tester,
qa-manager, prompt-writer, knowledge-wizard, general-counsel,
gameplay-designer, game-producer — plus infrastructure: sloane,
decision-model, devops-sre, game-architect, memory-keeper,
connector-operator.

## Reserve (16) — chartered, callable, on probation

Charter and packet maintained; no standing duties. A Reserve seat
that works a live mission and files a learnings entry is promoted
to Core at the next monthly review — promotion is earned by use,
not granted by enthusiasm. A Reserve seat with zero live seatings
across a full quarter gets a verification drill or a cut
recommendation (playbook seat-routing rule, point 5).

ui-ux-designer, document-artisan, word-specialist, excel-specialist,
diagram-designer, art-director, launch-strategist, sales-agent,
scriptwriter, social-media-strategist, mission-control,
casting-director, game-ui-ux-designer, console-platform-engineer,
financial-analyst, tax-strategist.

## Connector operations

The 102 Connector Master seats were retired the same night. Their
charters live on as runbooks in `office/runbooks/connectors/`,
operated by the single **Connector Operator** seat (Core). A
connector's status or gates change → its runbook updates the same
day; a new connector → MCP Maker builds it, the Operator writes its
runbook and takes custody.

## Mechanics

Tier is stamped as `metadata.roster_tier` in every seat's SKILL.md
(both trees) by `office/scripts/apply-roster-tiers.py` — edit the
CORE set there and re-run; never hand-stamp. Utilization evidence:
`office/scripts/seat-coverage.py`, run monthly by the learning
review.
