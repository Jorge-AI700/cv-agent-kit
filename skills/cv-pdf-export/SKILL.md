---
name: cv-pdf-export
description: Turn a tailored cv.md into a one-page, ATS-friendly A4 PDF (and DOCX) with a clean one-column layout, then check it visually. Use after job-cv-builder has produced cv.md and the user wants a file to send.
---

# CV PDF Export

## Outcome

A `<Name>-<Company>-<Role>-CV.pdf` and matching `.docx` that fit on **one A4 page**, read cleanly in ATS parsers (one column, real text, no tables or images), and match the content of `cv.md` word for word.

## Requirements

- Python 3 with `python-docx` (`pip install python-docx`).
- LibreOffice (`soffice`) for DOCX→PDF.
- Optional for checks: `pdfinfo` and `pdftoppm` (poppler-utils).

## Write cv.md in the renderer's format

```markdown
# Full Name
City, Country • email • phone • linkedin.com/in/handle
Availability or status line

## Profile
Two or three sentences. **Bold** works inline.

## Experience
### Job Title — Organisation | City, Country | Mon YYYY–Mon YYYY
_Optional one-line italic context, e.g. what the company does or "details under NDA"._
- Bullet starting with a verb; **bold** the one number or result that matters.

## Education
### Degree — School | City, Country | Mon YYYY–Mon YYYY
- GPA, honours, relevant coursework.

## Skills & languages
**Group:** item • item • item
**Languages:** Spanish (native) • English (C1)
```

Rules the renderer relies on:
- Lines before the first `##` are centred header lines (the `#` line is the name).
- `###` lines are entries: `Title — Organisation | Location | Dates`. Use an em dash (—) or en dash (–) with spaces between title and organisation. Location is optional (`Title — Org | Dates`).
- A line wrapped in `_underscores_` right after an entry becomes its small italic context line.
- `- ` lines are bullets. Any other line is a plain paragraph.

## Render

```bash
python3 skills/cv-pdf-export/scripts/render_cv.py path/to/cv.md --out path/to/output --name Full-Name-Company-Role-CV
```

Options: `--size 10` sets body font size (default 10; use 9.5 only if needed to stay on one page, never below 9).

The script prints the DOCX and PDF paths and the page count. If LibreOffice is not installed, it cleanly exports the DOCX without crashing.

## Web Chat Sandboxes (ChatGPT, Claude, etc.)

If you are an agent running inside a web chat with a Python execution environment:
1. Run `render_cv.py` directly inside your sandbox on the generated `cv.md`.
2. Provide the generated `.docx` (and `.pdf` if LibreOffice is available in the container) as a file download link in chat.
3. Users who download the `.docx` get the full 1-page layout, exact tab stops, margins, and styling, and can save as PDF directly from Word or Google Docs.

## Check before delivering

1. **Page count is 1.** If it is 2, cut content in this order: weakest bullet in the oldest role, extra skills items, long context lines, then drop `--size` to 9.5. Never shrink margins.
2. **Look at it.** `pdftoppm -png -r 80 -f 1 -l 1 file.pdf preview` and open `preview-1.png`. Check: nothing cut off, dates right-aligned on the same line as the title, no orphaned heading at the bottom, the page is reasonably full (not half empty — add a relevant bullet from the master CV if so).
3. **Text matches.** Every claim in the PDF must come from `cv.md`, which must come from the master CV or a fact the user confirmed.
4. Deliver the PDF path, page count and one line on what was emphasised for this job.
