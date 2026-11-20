# CV rules template

Store this privately as `<name>-cv-rules.md`. It overrides the master CV and grows whenever the user corrects a fact or wording.

```markdown
# Full Name — CV rules
Last updated: YYYY-MM-DD

## Overriding facts
- Fact: corrected value. Rules win over older source documents.

## Contact details
- Header: `City, Country • email • phone • portfolio/link`
- Application email: the address used for applications and recruiter replies.

## Status line
- Main CV language: `Available ...`
- Other CV language, if used: `...`

## Banned words
- exact term or phrase
- another phrase

## Preferred terms
- Use `preferred wording`; do not use `old wording`.

## Title translations
- Real Title = Approved translation

## Application answer bank
- Availability / start date: confirmed answer.
- Notice period: confirmed answer.
- Work authorisation: ASK USER for every application unless the exact answer is confirmed here. Omit if not relevant.
- Sponsorship: ASK USER for every application unless the exact answer is confirmed here. Omit if not relevant.
- Salary or rate: confirmed range by role family and market, or ASK USER.
- Why this employer: `{from posting}` one sentence built from the posting.

## Layout and delivery
- One A4 page (or the local norm the user chose).
- Section order.
- Filename pattern: `<First>-<Last>-<Company>-<Role>-CV.pdf`.
```

`qa_check.py` reads two sections from this file:

- `## Banned words` (a heading containing “banned” and “word”, “phrase”, or “term” also works). Put one literal term or phrase on each bullet. Matching is case-insensitive with whole-word/whole-phrase boundaries, so banning `demo` does not flag `demographics`.
- `## Title translations`, one `Real Title = Translation` per bullet. Use it when a CV in another language shows a translated job title or qualification; the user approves each translation once.
