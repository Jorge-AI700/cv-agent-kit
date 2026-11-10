---
name: job-cv-builder
description: Create a truthful CV tailored to a specific job posting or URL by matching its requirements to evidence in a master CV. Use when a person has a master CV and wants a job-specific application CV.
---

# Job CV Builder

## Outcome

Produce a concise CV for one job using evidence from the user's master CV, plus separate application notes explaining the match and unresolved gaps. Tailoring changes emphasis and wording where the facts support it; it does not create new experience.

## Gather the two sources

- Obtain the master CV and the job description or URL. If the master CV is missing, ask the user to provide it or build it first. If the job page is inaccessible, incomplete, or requires a login, ask for pasted text. Do not guess the contents of a URL.
- Note the employer, role, location, language, source URL if any, and date accessed when available. Job postings can change; preserve a concise summary of the version used in application notes.
- Ask for any constraints that materially affect the result, such as target country, language, length, or file type, only when they cannot be inferred. Markdown is the portable default; export to another format when requested and supported.

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
- When formatting `cv.md`, use the clean format compatible with `cv-pdf-export` for one-page rendering:
  - Header lines before the first `##`: `# Full Name` (centered name), followed by contact line and status/availability line.
  - Section headings: `## Section Name` (e.g. `## Profile`, `## Experience`, `## Education`, `## Skills & languages`).
  - Experience / Education entries: `### Job Title — Organisation | City, Country | Dates` (use em dash `—` or en dash `–`).
  - Optional context: a single line wrapped in `_underscores_` directly below an entry heading.
  - Bullets: `- ` with the core metric or result in `**bold**`.
- Before delivering, check every claim against the master CV or a new user-confirmed answer. Check chronology, numbers, scope, language, and whether inference or uncertainty has been presented as fact. Remove placeholders from the CV; keep unresolved issues in the notes.

Create `cv.md` and `application-notes.md` in a private location chosen by the user when files can be written. The notes should contain a short job brief, the important requirement-to-evidence matches, gaps, and any choices or assumptions that may need review. In a chat without file access, return both documents as complete, clearly labeled Markdown so the user can save them. If a PDF or DOCX is requested and supported by the environment, use the `cv-pdf-export` skill to render it.
