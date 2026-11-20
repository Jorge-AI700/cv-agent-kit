# Master CV template

Use this fixed structure. Omit an optional section only when it does not apply; do not rename the evidence-control sections (Proof-point bank, Accuracy notes, Open questions). Role families, tags and examples below are placeholders: take the real ones from the user's intake, whatever their field.

```markdown
# Full Name — MASTER CV
Optional private contact line
Status / availability line

> **How to use this document.** Exhaustive evidence source for tailored CVs. The rules file overrides conflicts. Pick one bullet where alternatives are marked *Variant:*. Job titles, employers and dates here are the real ones and are never changed in a tailored CV.
>
> **Tags:** **[A]** Role family • **[B]** Role family • **[C]** Role family

## Target role families
- **[A] Family name.** One-line pitch.
- **[B] Family name.** One-line pitch.

## Summary variants
### [A] Family name
Evidence-backed summary.

## Core skills
**Skill group** [A,B]
Skill (level) • Skill • Tool (AI-assisted) • Skill (learning)

## Experience
### Real Job Title — Organisation
**Location / work mode • Mon YYYY–Mon YYYY**
_Context: what the organisation does, employment type (paid, volunteer, personal, freelance), team, remit._

**Functions performed:** Function • Function • Function

**Day-to-day tasks**
- Every recurring task, including small or unglamorous ones (who for, how often, with what tools).

**Tagged bullets**
- [A,B] Action + scope + result, including measurement source or `no metric`.
- [A] *Variant:* Alternative wording for the same achievement; pick one.

**Raw notes**
- Original phrasing, source-only claims, uncertainty, or useful detail.

## Projects
### Project name — Academic | Mon YYYY–Mon YYYY
_Label exactly one: Academic, Paid, or Personal. Add client/course context without implying employment._
- [A] Action + scope + result.

## Education
### Qualification — Institution
**Location • YYYY–YYYY**
- [B] Confirmed detail (grade, honours, placements, relevant modules).

## Certifications & licences
- [A] Name — Issuer, YYYY; number and expiry if the field requires them (professional registration, trade licence, driving licence).

## Leadership & community
### Real Role — Organisation
**Location • Mon YYYY–Mon YYYY**
- [A,B] Evidence-backed activity and result or `no metric`.

## Proof-point bank
| Proof point | Context | Status | Source |
| --- | --- | --- | --- |
| 24 users | Project research | Confirmed | Interview log, reviewed YYYY-MM-DD |
| About 15% | Process change | Estimate | Weekly log comparison; confirm before external use |

## Accuracy notes
- **Ownership:** Team result; state the person's contribution.
- **Project type:** Project X was academic, not paid work.
- **Confidentiality:** Describe scope only; details under NDA.
- **Credentials:** Certificate expired Mon YYYY.
- **Words to avoid:** Term and reason.

## Open questions
1. Question and why it matters.
2. **Resolved YYYY-MM-DD:** Original question. Answer and resulting change.
```

**Functions performed** lists every kind of work the person actually did in the role, in plain function names (for example: scheduling, customer support, budgeting, onboarding, prospecting, patient education, stock control, reporting, training). **Day-to-day tasks** records the concrete tasks behind those functions. Together they let a tailored CV rebuild the role around a different target job without inventing anything: a function that is not listed here cannot be claimed later.

Every `###` entry that a tailored CV may show must use `Real Title — Organisation`, because `qa_check.py` compares tailored entry titles with these.
