# Skill Registry

Skills the Knowledge Wizard hunted across the internet, vetted, and
installed. New skill = new directory `office/skills/<slug>/` with a
`SKILL.md` (frontmatter: name, description, version, source URL,
license, installed date) plus the original license file.

| Skill | Source | License | Installed | Tools wired |
|-------|--------|---------|-----------|-------------|
| _none yet_ | | | | |

## Learned skills — admission gate

A *learned* skill is authored from the office's own experience — a
learning that generalizes into a reusable procedure — distinct from
the hunted skills in the table above. Frontmatter alone does not
admit one. A learned skill enters this registry only when all five
hold:

1. **Provenance.** Its source learning is cited (seat learnings
   file, date, mission) and passes the learnings protocol's
   write-time salience test (rule 7): it generalizes beyond one
   mission, is not already in a charter, skill, or file, and
   forgetting it would repeat a real mistake.
2. **Verified.** Every checkable claim inside it was verified at
   its destination before admission (learnings protocol rule 8;
   the office's M-2 rule). An unverified claim never becomes a
   skill.
3. **Demonstrated.** It has run once — on a real task or an
   `office/evals/` fixture — with the outcome recorded. A skill
   that has never run is a proposal: it stays in the wing or the
   boardroom, not in this registry.
4. **Promotion Gate.** The admission commit cites its evidence
   under the War Room playbook's Promotion Gate (the eval run it
   passed, or `process-only: no seat behavior changed` plus the
   validator result).
5. **Custodian and scope.** A custodian seat is named, the
   frontmatter description states its trigger, and it carries no
   paid-API, credential, or spend dependency beyond the standing
   gates.

A candidate failing any of the five stays a learning or a written
proposal. Admission is one commit: the skill directory plus its
registry row together.

## Format
Every skill directory follows the same shape the agent's own skill
system uses, so skills stay portable:

```
office/skills/<slug>/
├── SKILL.md        # frontmatter + how-to-use
├── LICENSE.*       # original license, kept verbatim
└── ...             # supporting files the skill needs
```
