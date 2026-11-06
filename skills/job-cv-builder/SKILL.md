---
name: job-cv-builder
description: Create a truthful CV or resume tailored to a specific job posting or URL by matching its requirements to evidence in a master CV, then render a formatted DOCX and PDF when the environment allows. Use when a person has a master CV and wants a job-specific application CV or resume.
compatibility: PDF export needs Python 3 with python-docx and LibreOffice (soffice). Visual QA needs poppler-utils (pdfinfo, pdftoppm). Markdown output works without them.
---

# Job CV Builder

This skill produces a tailored CV or resume. Use the word the person uses; the workflow is the same.

## Outcome

Produce a concise CV for one job using evidence from the user's master CV, plus separate application notes explaining the match and unresolved gaps. Tailoring changes emphasis and wording where the facts support it; it does not create new experience. When rendering tools are available, also produce a DOCX and PDF and visually check the first page.

## Gather the two sources

- Obtain the master CV and the job description or URL. If the master CV is missing, ask the user to provide it or build it first. If the job page is inaccessible, incomplete, or requires a login, ask for pasted text. Do not guess the contents of a URL.
- Note the employer, role, location, language, source URL if any, and date accessed when available. Job postings can change; preserve a concise summary of the version used in application notes.
- Ask for any constraints that materially affect the result, such as target country, language, length, or file type, only when they cannot be inferred.
- Write the CV in the language of the job posting unless the user asks for another language.
- Reuse optional application facts from the master CV (work authorization, start date or notice period, languages, relocation, and salary expectation) when filling forms or notes. Include languages on the CV when the user recorded them, and work authorization when it is relevant to the posting. Never put a salary expectation on the CV itself.

## Analyze the job

Extract the role's responsibilities, outcomes, domain, seniority, tools, and eligibility constraints. Classify requirements by what the posting actually says:

1. **Explicit requirements:** Qualifications or conditions described as required, essential, or mandatory.
2. **Explicit preferences:** Qualifications described as preferred, desirable, or advantageous.
3. **Inferred priorities:** Likely priorities suggested by repeated themes, prominent responsibilities, or company context. Label these as inference, not employer requirements.
4. **Unknowns:** Ambiguous or missing details that affect how the CV should be framed.

Prioritize by explicitness, centrality to the work, and specificity. Avoid an opaque fit percentage or treating every keyword as equally important.

## Map evidence before writing

For each important requirement or priority, find the strongest relevant examples in the master CV. Note the source role or project, the person's own contribution, outcome, recency where relevant, and any uncertainty. Transferable experience may support a competency without being identical to direct experience: describe the actual work and do not imply the person held a title, used a tool, or served a domain they did not.

Ask targeted follow-ups when a high-priority match may exist but the master record lacks detail. Treat answers as candidate facts only after the user confirms them. Keep unsupported requirements visible as gaps; never fill them with job-posting language or invented claims. If useful new facts emerge, offer to add them to the master record, keeping the job posting separate from the person's history.

## Draft and verify

- Select the most relevant factual accomplishments and responsibilities. Write a clear profile, skills supported by experience, and focused experience entries. Keep accurate job titles, employers, dates, qualifications, and measurable results. Use the posting's terminology only where it truthfully describes the person's work.
- Write `cv.md` in the structure documented in [references/markdown-format.md](references/markdown-format.md), then follow the layout, writing, and ATS notes below. Read [references/layout-and-writing.md](references/layout-and-writing.md) when you need more detail.
- Before delivering, check every claim against the master CV or a new user-confirmed answer. Check chronology, numbers, scope, language, and whether inference or uncertainty has been presented as fact. Remove placeholders from the CV; keep unresolved issues in the notes.

### Writing and layout

- Order sections to fit the career stage: most people list profile, skills, experience, then education and other sections. Students and very recent graduates may put education before experience. Career changers keep truthful titles and dates, and give more space to transferable work.
- Give more bullets to recent or highly relevant roles, and fewer to older or less relevant ones.
- Write bullets as action, what the person did, and a measurable result when the master CV supports that result. Do not invent metrics.
- Use one date format throughout, for example `Jan 2022 – Mar 2024` or `2022–2024`.
- Aim for one page when the person is early in their career or has under about ten years of experience. Two pages are acceptable for longer careers; do not leave a nearly blank second page.
- Follow country conventions: in the US and UK, do not include a photo or birth date. In much of continental Europe a photo is optional and only if the user wants one. Never include national ID numbers.
- Use conventional headings a parser will recognize, such as Profile or Summary, Experience, Education, and Skills.

### Applicant tracking systems (ATS)

- Keep a single column of body text.
- Put every important fact in normal selectable paragraphs, not in headers, footers, tables, text boxes, or images.
- Use a standard font (the renderer uses Arial).
- Save the file as `Firstname-Lastname-CV-Company.pdf`, with the matching `.md` and `.docx` stems.

## Render to DOCX and PDF

When this skill's scripts can run, rendering is part of delivery, not an extra requested only by the user.

1. Install the Python dependency if needed: `pip install python-docx` (see `scripts/requirements.txt`).
2. PDF export needs LibreOffice (`soffice` or `libreoffice`) on the PATH.
3. Visual checks need `poppler-utils` (`pdfinfo` and `pdftoppm`).
4. Run the renderer. Resolve `scripts/render_cv.py` from this skill folder:

```bash
python scripts/render_cv.py path/to/cv.md -o path/to/Firstname-Lastname-CV-Company.pdf --page-size a4 --font-size 10 --check
```

Use `--page-size letter` for the United States or Canada, or when the user asks for US Letter. The default body size is 10pt. `--check` prints `Pages: N` and writes a PNG of page 1.

If LibreOffice is missing, the script writes the DOCX and says that no PDF was created. Deliver the Markdown and DOCX in that case, and tell the user what is needed for a PDF. If the script cannot run at all, Markdown is the portable default.

## Visual QA

When a PDF was produced, inspect it before delivering:

1. Read the printed page count.
2. Open the page-1 PNG from `--check` and look at it.
3. The content must not spill onto an extra page by only a few lines. If it does, tighten bullets, shorten the profile, or reduce `--font-size` slightly (not below about 9.5pt) and render again.
4. The page must not look noticeably cramped. If it does, cut lower-priority bullets or increase `--font-size` slightly (not above about 10.5pt) and render again.
5. The page must not look noticeably half-empty. If it does, and the master CV has unused relevant evidence, add a bullet or two, or increase the font size toward 10.5pt, and render again. Do not invent content to fill space. A genuinely short early-career CV may not fill the page; that is acceptable when there is no truthful material left to add.
6. Repeat until the page count and the visual check both pass.

## Application notes and delivery

Create `cv.md` and `application-notes.md` in a private location chosen by the user when files can be written. The notes should contain a short job brief, the important requirement-to-evidence matches, gaps, and any choices or assumptions that may need review. In a chat without file access, return both documents as complete, clearly labeled Markdown so the user can save them. When rendering succeeded, also provide the PDF (and DOCX) using the filename above.
