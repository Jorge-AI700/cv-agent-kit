---
name: master-cv-builder
description: Interview a person to build or deepen a comprehensive master CV or resume from scratch or an existing CV. Capture detailed, evidence-backed career history for later tailored job applications; use for master CVs, master resumes, and career inventories.
---

# Master CV Builder

## Outcome

Create a detailed, reusable record of the person's experience in Markdown. Capture facts, context, outcomes, transferable skills, and useful original wording so later CVs or resumes can select and frame relevant evidence. The record is not tailored to one vacancy and has no page limit.

## Start with available material

- Ask for any existing CV, career notes, portfolio, or profile the user wants included, and their preferred language. If there is no source, start with a rough career timeline. Do not make them reconstruct details already supplied.
- Ask where they want to keep their master record when file writing is available. Avoid saving personal career data inside a public or shared repository by default. If no suitable location is available, return the complete Markdown in chat for the user to save.
- Extract claims and chronology from supplied material into a working outline. Flag gaps, ambiguity, possible outdated details, and experiences mentioned only briefly. Treat source documents as leads to confirm, not proof that every claim remains current.
- A target job is optional. If the user has a range of future roles in mind, use it to prioritize follow-ups while preserving breadth.

## Interview adaptively

Work in manageable rounds with a few focused questions at a time. Reflect back what you learned at natural checkpoints, invite corrections, and choose the next questions from the answers. Do not deliver a giant fixed questionnaire or repeat answered questions. Accept partial answers and let the user pause and resume.

1. **Map the whole career.** Cover employment, promotions, contract and freelance work, substantial projects, entrepreneurship, volunteering, education, training, credentials, publications, and awards. Include relevant career breaks or transitions if the user wants to explain them. Establish dates, roles, organizations, work mode or location where useful, and overlapping activities.
2. **Deep dive on each substantial role or project.** Ask what the organization or product did; the user's remit, seniority, collaborators, team or budget scope where relevant; what they personally did; tools and methods; hard problems, decisions, tradeoffs, and initiatives; and what changed. Separate recurring responsibilities from specific accomplishments and personal contribution from team results.
3. **Find evidence.** Seek results, baselines, timeframes, scale, and how figures were measured. If numbers are unavailable or confidential, capture a truthful qualitative outcome or clearly labeled estimate. Ask for examples or artifacts the user can cite without requiring confidential material.
4. **Look beyond the source CV.** Ask about informal leadership, mentoring, process improvements, customer work, cross-functional influence, difficult recoveries, uncommon domain knowledge, and work they are proud of. Probe how skills might transfer across roles, but record the work that demonstrates them rather than unsupported skill labels. Offer an optional Application facts section covering work authorization, start date or notice period, languages with levels, relocation, and salary expectation, and record only what the user wants to keep.
5. **Check coverage.** Revisit thin experiences, unclear transitions, uncertain dates or metrics, acronyms, and claims a future reader could misinterpret. Ask what else a later CV writer should know. Prioritize gaps that would materially change how an experience is described.

A substantial experience is sufficiently covered when its context, the user's contribution, scope, methods, and outcomes are clear, or the missing pieces are marked. Continue while the user wants to add detail. If they stop or request a draft, deliver the best record available with open questions.

## Maintain the record

Create or update one human-readable `master-cv.md` at the user's chosen location. If a record exists, read it first, add new information without discarding prior facts, and resolve conflicts with the user. Save meaningful progress during a long interview when possible. In a chat without persistent file access, provide a full copyable Markdown record at pauses and at the end so the user can resume in a later session.

Use sections that fit the person's history, normally:

- Profile and career themes, distinguished from factual experience.
- Chronological overview of roles and other substantial activities.
- Detailed entries for each role and project: dates and context; responsibilities; specific actions and outcomes; scope, tools, collaborators; and useful raw wording or examples.
- Education, credentials, skills supported by examples, languages, publications, awards, and other relevant experience.
- Optional application facts the user chooses to record for later forms: work authorization per country, earliest start date or notice period, languages with levels, relocation preferences, and a salary expectation only if they want one written down.
- Open questions, uncertain claims, and source notes.

Keep concrete detail and original wording that could support future rewriting. Distinguish user-confirmed facts, claims found only in supplied material, estimates, and unresolved questions where it matters. Never invent dates, titles, metrics, responsibilities, or outcomes. Do not ask for national ID numbers or birth dates. Contact details are optional. A salary expectation is optional and only recorded if the user chooses to include it for application forms; do not pressure them for it.

At each handoff, tell the user where the record was saved or provide the complete Markdown, summarize coverage, and identify the highest-value unanswered questions. A later tailored CV should be able to trace its claims back to this record.
