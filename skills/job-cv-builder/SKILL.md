---
name: job-cv-builder
description: Create a truthful one-page CV and application notes for a specific live job posting, rebuilding each relevant experience around the target role from a tagged master CV and private rules file. Works for any field, country and language.
---

# Job CV Builder

## Outcome and sources

Produce private `cv.md` and `application-notes.md` for one job. Load the candidate's rules file first, then the master CV. These are the only candidate fact sources: never copy facts from older tailored CVs. Rules override conflicts. If the master has no role-family tags or no functions/task lists, work from what is there and recommend a `master-cv-builder` update.

Obtain the full posting or URL. Check that it is still live and its deadline has not passed before tailoring. Record employer, role, location, language, source URL, and access date in the notes. Ask if the location is ambiguous. If a page is inaccessible or requires login, request pasted text rather than guessing.

## Analyse and map before writing

Classify the posting into one of the candidate's role families and start from that family's summary variant. Extract responsibilities, outcomes, domain, seniority, tools, location, and eligibility constraints. Classify each item as explicit requirement, explicit preference, inferred priority (labelled), or unknown.

Map each important item to the strongest evidence in the master: tagged bullets, functions performed, day-to-day tasks, and raw notes. Record source entry, personal contribution, result, recency, and uncertainty. Choose one variant per achievement.

Ask targeted follow-ups only when a high-priority match may exist. Treat answers as facts only after confirmation. Put every unproven must-have and material ambiguity in `application-notes.md`; never place it on the CV.

## Rebuild each experience around the target role

The master is a source of evidence, not a set of fixed descriptions. For each role shown, rewrite it for this job:

1. **Title line.** Keep the real job title, employer, and dates exactly as in the master (or an approved translation from the rules). When the real title hides the relevant work, add the target function in brackets: `Founder (Business Development) — Organisation`, `Shift Supervisor (Training) — Organisation`, `Teaching Assistant (Data & Reporting) — Organisation`. Never replace the title with the target job title.
2. **Context line.** Rewrite it to describe the part of the role that matters for this job.
3. **Bullets.** Rewrite them in the posting's vocabulary, drawing on every relevant function and task recorded for that role, not only its headline bullets. Lead with the work closest to the target role.
4. **Selection.** Choose which roles to show and in what order based on relevance to this job, not chronology alone. A minor role with strong transferable evidence can earn more space than a senior but irrelevant one.

Limits: every reframed bullet must trace to a specific master fact (bullet, task, function, raw note, or rule). Never invent tasks, tools, clients, scale, results, or seniority, and never imply a function the master does not record. If the target role needs evidence the master lacks, it is a gap for the notes.

Example: a master records `Founder — small online shop` with functions `supplier sourcing • customer support • social media • bookkeeping`. For a customer-support posting it becomes `Founder (Customer Support) — Shop`, with bullets about answering customer messages, handling returns, and writing help pages, all taken from the recorded tasks. For a bookkeeping posting the same role becomes `Founder (Bookkeeping) — Shop`, with invoicing and reconciliation bullets.

## Write the tailored files

Use the posting's language, local job titles, and local date style; use title translations from the rules file. Follow the candidate's market conventions recorded in the rules (section order, education first for graduate or academic roles, and so on). The profile is two or three lines: posting title/role + strongest proof point + one differentiator. No generic adjectives.

Mirror exact posting keywords only where truthful: place them in the bullet that proves them and, when useful, in Skills. Do not stuff or repeat keywords. Put the posting's tools first in Skills and remove irrelevant ones.

Budget one A4 page: give the most relevant role about three or four bullets, others one or two, and the oldest one. Prefer recent, direct evidence. Use the renderer-compatible Markdown described by `cv-pdf-export`:

```markdown
# Full Name
Contact line from rules
Status line from rules

## Profile
Two or three concise lines with **one key proof point**.

## Experience
### Real Title (Target Function) — Organisation | Location | Dates
_One-line context written for this job._
- Action, scope and **result**, in the posting's vocabulary.

## Education
### Qualification — Institution | Location | Dates

## Skills & languages
**Relevant group:** item • item
```

Create `application-notes.md` with: posting snapshot and liveness check; role-family choice; requirement-to-evidence map; how each role was reframed and which master facts each rewritten bullet comes from; posting keywords used; gaps not claimed; assumptions; and interview angles. Offer to write newly confirmed facts back to the master after review.

## QA, render, and deliver

1. Run `scripts/qa_check.py cv.md --rules path/to/rules.md --master path/to/master-cv.md`, adding `--extra-text` for cover letters or application answers. It fails on banned terms and on entry titles that differ from the master (a `(Function)` suffix and rules-file translations are allowed), and warns about numbers not found in the master or rules. Resolve every error and investigate every warning.
2. Check by hand that every reframed bullet traces to a master fact, contacts and status match the rules file, dates match the master, and language and date style match the posting.
3. Render with `cv-pdf-export`. Use `<First>-<Last>-<Company>-<Role>-CV.pdf` unless the rules specify another pattern.
4. Verify exactly one A4 page and inspect the preview for alignment, clipping, and reasonable page fill. Trim weak evidence before reducing font size.
5. Hand the CV, application notes, PDF, and DOCX to the user. Never apply, submit, email, or upload from this skill.
