# Archify Diagrams — Interactive Architecture Visuals for AI Agents

Turn any idea, plan, or codebase into a beautiful interactive HTML diagram.
Reverse-engineered method inspired by [Archify](https://github.com/tt-a1i/archify)
(MIT License) — rewritten here as our own portable skill. No install required.

## When to use

Visualizing: system/infra architecture, API call chains, workflows and
runbooks, data pipelines, state machines, database schemas, class
contracts, module trees, incident timelines, request waterfalls — or
everyday subjects with steps, parts, relationships, or states. Not for
numeric charts or dashboards.

## The method — 4 steps

### 1. Describe (or trace)
Take the plain-language request as-is. For a real codebase, read the
code first and trace the requested behavior — the diagram must be
source-backed, with evidence for what's drawn. Never invent source
evidence; mark illustrative vs. measured values and flag omitted parts.

### 2. Author a typed candidate
Write a structured JSON spec — never prose coordinates. Pick one type:

| Type | Use for |
|---|---|
| `architecture` | Components, services, boundaries, infrastructure |
| `sequence` | API call chains, request lifecycles, back-and-forth |
| `workflow` | Processes, approvals, runbooks, CI/CD |
| `dataflow` | Pipelines, ETL/ELT, lineage, where things go |
| `lifecycle` | State transitions, retries, terminal states |
| `erd` | Tables, columns, keys, cardinality |
| `class` | Types, members, inheritance/association |
| `tree` | Single-parent containment, breakdowns |
| `timeline` | Timestamped events on a proportional clock |
| `waterfall` | Span durations and nesting on one time axis |

Candidate shape:
```json
{
  "meta": { "title": "...", "type": "architecture", "theme": "dark|light" },
  "nodes": [
    { "id": "api", "label": "API Server", "kind": "service",
      "description": "Handles requests, checks cache" }
  ],
  "relationships": [
    { "from": "browser", "to": "api", "label": "HTTPS request" }
  ],
  "sources": [
    { "node": "api", "evidence": "src/server.ts:42" }
  ]
}
```
Use fresh IDs and wording every time. Show the main journey plus
necessary branches; preserve behavior-changing conditions; leave room
for relationship labels.

### 3. Validate & repair (bounded)
Check the candidate before rendering:
- Every `from`/`to` references a real node id.
- No orphan nodes that should be connected; no duplicate ids.
- Labels legible (short); layout has room for them.
- Sources listed for every codebase-backed claim.

A failed check is never success — repair the failed neighborhood and
re-validate. Max 3 repair rounds; then escalate with the failure
record instead of looping.

### 4. Render standalone HTML
Produce one self-contained `.html` file: inline SVG, no external
dependencies at view time, dark/light theme toggle, explorable
(hover/click for details). Keep it in a per-request folder so earlier
versions stay intact.

If the `archify` package is installed (`npx skills add tt-a1i/archify -g`),
you may use its `finalize` pipeline for the validation gates instead of
hand-checking — same method, automated.

## Output contract
- Lead with a clickable link to the HTML (descriptive title, absolute path).
- Add one or two sentences only when the reader needs them: the key
  takeaway, the abstraction level, or deliberately omitted parts.
- The diagram carries the content — keep the words to one line when it does.
