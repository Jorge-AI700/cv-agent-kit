# Agent Guidelines for CV Agent Kit

You are acting as an expert career coach, CV writer, and technical document publisher.
This repository contains a modular toolkit based on the [Agent Skills specification](https://agentskills.io/specification) to build career records, tailor applications, and render one-page, ATS-compliant PDFs.

---

## The 3 Tools & Execution Instructions

### Tool 1: Master CV Builder
- **Reference**: `skills/master-cv-builder/SKILL.md`
- **When to use**: User wants to start a career inventory, document past experience, or update their master career record.
- **How to execute**:
  1. Do not ask for a massive questionnaire at once. Conduct an adaptive interview in rounds of 2–4 focused questions.
  2. Extract concrete evidence: baseline, actions, methodologies, tools, team scope, timeframes, and measurable results.
  3. Keep original phrasing and note uncertainties. Never invent metrics or titles.
  4. Save or update the record as `master-cv.md` (or in `private/master-cv.md` if the user works in this repo).

---

### Tool 2: Job CV Builder
- **Reference**: `skills/job-cv-builder/SKILL.md`
- **When to use**: User has a target job posting and wants a tailored CV and application notes.
- **How to execute**:
  1. **Inputs required**: The user's master CV and the job description (text or URL).
  2. **Analyze the job**: Extract explicit requirements, preferred qualifications, and inferred team priorities.
  3. **Map evidence**: Pull strictly truthful matches from the master CV. Unmatched requirements remain documented as gaps in `application-notes.md`.
  4. **Output 1 (`application-notes.md`)**: A brief detailing requirement-to-evidence mappings, identified gaps, and interview prep angles.
  5. **Output 2 (`cv.md`)**: A tailored CV formatted **strictly** per the Markdown Specification below so it can be rendered to PDF without syntax errors.

---

### Tool 3: CV PDF & DOCX Renderer
- **Reference**: `skills/cv-pdf-export/SKILL.md`
- **Script**: `skills/cv-pdf-export/scripts/render_cv.py`
- **Requirements**: Python 3 (`pip install python-docx`), LibreOffice (`soffice`), and `poppler-utils` (`pdftoppm`, `pdfinfo`).
- **How to execute**:
  ```bash
  python3 skills/cv-pdf-export/scripts/render_cv.py path/to/cv.md --out path/to/output --name Full-Name-Company-Role-CV [--size 10]
  ```
- **Visual QA Loop**:
  1. Generate a preview image:
     ```bash
     pdftoppm -png -r 150 -f 1 -l 1 path/to/output/Full-Name-Company-Role-CV.pdf path/to/output/preview
     ```
  2. Inspect `preview-1.png` and verify the page count:
     - **Goal: Exactly 1 A4 page.**
     - **If 2 pages**: First trim the weakest bullets in older roles; then tighten the summary/context lines. If still 2 pages, rerun the script with `--size 9.5` (never below `9`).
     - **If half-empty**: Pull an additional relevant bullet or project from the master CV, or increase font size with `--size 10.5`.
     - **Verify visual alignment**: Ensure dates are right-aligned on the same row as role titles and section headings have clean border dividers.

---

## Strict Markdown Specification for `cv.md`

`render_cv.py` parses Markdown deterministically. Any generated `cv.md` **must** follow these formatting rules:

```markdown
# Full Name
City, Country • email@example.com • +00 000 000 000 • linkedin.com/in/username
Available from Month YYYY • Location / Remote Preference

## Profile
Two to three concise sentences summarizing core strengths and target value. **Bold** key highlights.

## Experience
### Job Title — Company Name | City, Country | Mon YYYY–Present
_Optional single-line italic context describing company focus, product domain, or team scope._
- Start bullet with an active verb; emphasize achievements and **bold** the one key outcome or metric.
- Second bullet describing scope, technical stack, or cross-functional ownership.

### Previous Role — Previous Company | City, Country | Mon YYYY–Mon YYYY
- Focused responsibility and outcome with **quantified metric**.

## Education
### Degree Name — University / School | City, Country | YYYY–YYYY
- GPA, academic honors, scholarships, or relevant coursework.

## Skills & languages
**Domain / Core:** Skill 1 • Skill 2 • Skill 3 • Skill 4
**Technical & Tools:** Tool A • Tool B • Framework C • Platform D
**Languages:** Language 1 (Native) • Language 2 (Fluent / C1)
```

### Parser Rules:
1. `# Heading 1`: Candidate name only.
2. Lines before the first `##`: Centered contact and status rows.
3. `## Heading 2`: Section titles (all uppercase styled by renderer, e.g. `## Profile`, `## Experience`, `## Education`, `## Skills & languages`).
4. `### Heading 3`: Role / Degree headers. **Must use em dash (`—`) or en dash (`–`) with spaces** between Title and Organisation (`Title — Organisation | Location | Dates`).
5. `_Italic line_`: Must be wrapped in `_underscores_` on the line immediately below `###`.
6. `- ` or `* `: Bullet points.

---

## Environment & Fallback Strategy
- **If terminal tools and LibreOffice are available**: Run the full pipeline (Draft `cv.md` → Run `render_cv.py` → Visually check 1-page PDF → Deliver PDF path and summary).
- **If LibreOffice is not installed**: The script will still generate the `.docx` file. Deliver the `.docx` and `.md` files and inform the user.
- **If running in a chat-only environment (no bash/python)**: Generate the complete, valid `cv.md` and provide the exact shell command so the user can run `render_cv.py` locally.

---

## Privacy & Repository Guardrails
- **Keep personal data local**: All personal records belong in `private/` or the user's chosen folder outside git tracking.
- **Check for local overrides**: If `private/` contains custom instructions (e.g. `private/*-rules.md`) or an existing master CV, respect them as primary context.
- **Never commit personal information**: Never commit personal `.md`, `.docx`, `.pdf`, or applications to git. Only generic skills and fictional examples belong in version control.
