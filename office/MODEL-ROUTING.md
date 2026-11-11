# Model Routing — which brain runs which seat

Owner order 2026-10-30 (Intelligence Upgrade, Layer 1). A seat's
intelligence is mostly the model that runs it. Routing is declared per
seat in its agent frontmatter, in both skill trees
(`office/skills/<slug>/SKILL.md` and `~/workspace/custom-skills/<slug>/`):

- `metadata.model_tier` — `frontier` | `standard` | `fast`
- `metadata.model_routing` — the plain-language selection rule

Stamp or re-stamp every seat with:

    python3 office/scripts/apply-model-routing.py office/skills ~/workspace/custom-skills

**Connector Masters (102 seats, added 2026-10-30):** every master is
`standard` tier — skilled single-connector operation; judgment calls
escalate to Sloane.

## The tiers (capability classes, never hard model names)

Hard model names rot within a release cycle and do not port across
harnesses. Tiers are classes; each harness maps them to its own lineup.

| Tier | Meaning | Harness mapping (examples) | Reasoning effort |
|------|---------|----------------------------|------------------|
| frontier | Strongest reasoning model available | Opus-class / GPT-5-class / Gemini Pro-class | highest |
| standard | Balanced strong model | Sonnet-class / GPT mid-class | medium-high |
| fast | Fastest adequate model | Haiku-class / mini-class | medium |

Where a harness offers only one model, the tier degrades to an
effort/priority setting on that model — frontier seats get the most
reasoning budget and are spawned first-class, fast seats get the least.

## Assignment (17 / 22 / 6)

- **Frontier (17):** sloane, enterprise-architect, product-owner,
  prompt-writer, knowledge-wizard, appsec-lead, ai-red-teamer,
  penetration-tester, global-tech-law-lead, general-counsel,
  lead-code-reviewer, qa-manager, console-platform-engineer,
  decision-model, game-architect, financial-analyst, tax-strategist.
  Every blocking seat is frontier. **Rule: never downgrade a blocking
  seat to save cost — its judgment is the product.**
- **Standard (22):** the production seats (builders, designers,
  devops-sre, memory-keeper, mission-control, casting-director,
  reverse-engineer, game seats, document seats, the Connector
  Operator, and peers). Their work
  passes a frontier-tier review or QA gate before it ships.
- **Fast (6):** launch-strategist, sales-agent, scriptwriter,
  product-visualizer, seo-specialist, social-media-strategist.
  Bounded, format-driven work; output is reviewed by a higher-tier
  seat before use.

## Changing a tier

Edit the `TIERS` table in `office/scripts/apply-model-routing.py`,
re-run it on both trees, and record the change + reason in the palace
(`memory/INDEX.md`). A seat is promoted to frontier when its errors
start costing more than the model delta — measured by the eval layer
of the Intelligence Upgrade plan, not by vibes.

## The wider plan

Layer 1 (this file) shipped with Layer 2 Wave 1: Deep Method sections
(operating method, decision rules, failure modes, evidence standard,
output contract, block/escalate conditions) hand-authored into the 12
critical seats. Wave 2 completed the frontier tier — all 17 frontier
seats now carry Deep Method sections. Layer 3 (spawn-packet
enforcement) also shipped: `office/scripts/spawn-packet.py` assembles
every seat's briefing and its `--check-all` gate (45/45) is a
standing pre-convene check in the war-room playbook. Wave 3, Wave 4
and Layer 5 (tool grants, `office/TOOL-GRANTS.md`) have also shipped —
all 45 seats are now deep-authored, tier-stamped and grant-stamped.
Layer 6 (benchmark evals) shipped too: v1 baseline 59/60, full-office
v2 at 437/440 across the original 44 seats — the layer that measures
whether any of this actually made the office smarter.
Full plan: ADRs in `memory/INDEX.md` [2026-10-30].
