# Layout, writing, and ATS guidance

Use this reference while drafting a tailored CV or resume. The main skill file has the workflow; this page has the drafting rules.

## Section order

Choose an order that matches the person's career stage and the posting, not a single fixed template.

- **Most professionals:** name, headline, contact, profile or summary, skills, experience, education, then shorter sections such as languages, certifications, or projects.
- **Students and very recent graduates:** education may come before experience when it is the stronger evidence. Projects can sit near experience when they show relevant work.
- **Career changers:** keep truthful titles and dates. Give more space to transferable work and a profile that explains the direction, without inventing a new history.
- **Longer careers (about ten or more years):** keep recent, relevant roles detailed. Compress or summarize older, less relevant roles so the document stays readable.

Skip empty sections. Do not add a section only to echo keywords from the posting.

## Bullets and emphasis

Give more bullets to recent or highly relevant roles, and fewer to older or less relevant ones. A current role that matches the posting might have four or five bullets; an older side role might have one or two.

Write each bullet as **action + what you did + a measurable result** when the master CV supports the result:

- Strong: Introduced a shift handoff checklist covering stock, special orders, and unresolved customer requests; weekly logs showed fewer order remakes over the following three months.
- Weak: Responsible for improving processes and reducing errors.

If a number is missing, confidential, or only an estimate, use a truthful qualitative outcome or leave the figure out. Never invent a metric to make a bullet look complete. Keep job titles, employers, dates, and qualifications exactly as the master record (or a new user-confirmed fact) supports them. Use the posting's terminology only where it truthfully describes the person's work.

## Dates, length, and language

- Use one date format throughout, for example `Jan 2022 – Mar 2024` or `2022–2024`. Include the month when the master CV has it and it helps the timeline.
- Aim for one page when the person is early in their career or has under about ten years of experience. Two pages are acceptable for longer careers. Do not spill a few leftover lines onto an extra page, and do not leave a second page almost blank.
- Write in the language of the job posting unless the user asks for another language.

## Country conventions

- **United States and United Kingdom:** do not include a photo, birth date, marital status, or national ID number. A personal headshot is not expected.
- **Much of continental Europe:** a photo is optional and only if the user wants one. Still omit birth dates and national ID numbers.
- **Everywhere:** never include national ID numbers (for example DNI, NIE, Social Security, or passport numbers) or birth dates. Contact details are optional and user-controlled.

Use US Letter (`--page-size letter`) for the United States or Canada, or when the user asks for it. Otherwise default to A4.

## Applicant tracking systems (ATS)

Many employers parse the PDF or DOCX before a person reads it. Keep the file easy to parse:

- One column of normal body text.
- Conventional headings a parser will recognize: Profile or Summary, Experience or Work Experience, Education, Skills, Projects, Languages, Certifications.
- Every important fact in selectable paragraph text: name, contact details, titles, employers, dates, and bullets.
- No key information in headers, footers, tables, text boxes, or images of text.
- A standard font. The renderer uses Arial.
- A clear filename: `Firstname-Lastname-CV-Company.pdf`, with the same stem for the Markdown and DOCX files.

The renderer follows these rules when it writes DOCX and PDF. Do not re-export the file through a tool that flattens the page into an image.
