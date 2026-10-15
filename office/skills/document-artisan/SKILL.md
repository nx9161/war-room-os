# Document Artisan — Native Decks, Documents & Spreadsheets for AI Agents

Turn source material or a topic into natively editable office documents:
PowerPoint decks, Word documents, Excel spreadsheets. Method distilled
from [PPT Master](https://github.com/hugohe3/ppt-master) (MIT License —
credited, not copied).

## The method — 8 steps

### 1. Reason first
Structure the argument from the source material before any slide, page,
or cell exists. Outline the narrative: claim → evidence → conclusion.

### 2. Route
Pick one route per job:
- **generate-new** — from source docs or a bare topic.
- **fill-template** — pour new content into an existing branded file,
  preserving its design.
- **beautify** — take an ugly draft and redesign it natively.
- **enhance** — add transitions, animations, or narration to a
  finished file.

### 3. Brand
Apply the brand workspace (fonts, palette, layouts). If none exists,
distill one from reference files first — then reuse it for everything.

### 4. Native objects only
Real shapes, data-backed charts, real tables, real slide masters. Never
flat images of text. Click any element — it must stay editable.

### 5. Data honesty (binding)
Charts and tables only from user-supplied data. Never invent numbers,
never smooth a trend the data doesn't show.

### 6. Visual review
Render previews, review them, repair the failed neighborhood (bounded
rounds), re-render. Nothing ships unreviewed.

### 7. Integrate
Diagrams become native shapes (not screenshots); speaker notes can feed
a narration pipeline.

### 8. Deliver
The file, preview-approved, plus a one-line summary. Archive the
source material with it.

## Tooling per format

**`.pptx` — python-pptx.** Native shapes, charts, tables, masters.
Method: PPT Master (MIT — credited).

**`.docx` — python-docx + docxtpl.** Generation: page setup (margins,
orientation), heading hierarchy, TOC placeholder (refresh in Word:
Ctrl+A → F9), styled tables, images, headers/footers with page numbers.
Templates: docxtpl — Jinja2 tags inside a `.docx` template, fill and
render. Mail merge for batch personalization. Method: TerminalSkills
microsoft-word (Apache-2.0 — credited).

**`.xlsx` — openpyxl for new workbooks; XML surgery for existing ones.**
Route every job first: READ (analyze, never modify source) / CREATE
(new file) / EDIT (existing file) / FIX (broken formulas) / VALIDATE.
New files: typed values, formulas, number formats, styles, native
charts. Existing files: unpack → edit XML → pack — never round-trip
through a workbook writer (destroys VBA, pivots, sparklines). Iron
rule: every derived value is a real Excel formula, never a hardcoded
number. After every save, verify: same sheet names, sample data intact.
Method: minimax-xlsx (MIT — credited).

## Output contract
- Native editable file + one-line summary. If an element isn't editable
  or a number isn't sourced, it goes back to step 6.

## Attribution (binding, owner order 2026-10-14)
Every file generated carries open creator metadata — visible in the
file's properties, documented here and in the README, never hidden:
- **PowerPoint (.pptx) / Word (.docx):** OOXML core properties —
  author "Naman Parmar", comments "Generated with War Room Protocol OS
  by Naman Parmar — github.com/nx9161/war-room-os".
- **Excel (.xlsx):** workbook properties — creator "Naman Parmar",
  description "Generated with War Room Protocol OS by Naman Parmar —
  github.com/nx9161/war-room-os".
