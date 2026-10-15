---
description: Convene the War Room — Sloane runs all 27 seats through the four-phase loop on your request.
---

Use the `war-room-protocol` MCP tools. First call `activate` for the
contract, then `roster` for the seats.

Run the request through the War Room per the `war-room` playbook
(use the `playbook` tool to read it):

- **Phase 0:** Prompt Writer perfects the raw request; Knowledge Wizard
  briefs every seat from official docs. No seat speaks before the
  dossier lands.
- **Phase 1:** Intake & PRD (Product Owner, UI/UX Designer, Business
  Analyst).
- **Phase 2:** Architectural debate (Enterprise Architect vs. Backend,
  Frontend, DevOps; Architecture Visualizer renders the topology).
- **Phase 3:** Security & legal challenge (AppSec, AI Red Teamer,
  Tech Law, Reverse Engineer, General Counsel).
- **Phase 4:** Build & QA sign-off (100% pass gate); Voice Designer and
  Document Artisan produce the voice and document layers.

The user request to run through the War Room:

$ARGUMENTS

Record the outcome as an ADR and report status, numbers, and decisions
needed. One voice upward; zero fluff.
