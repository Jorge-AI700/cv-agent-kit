Everything here is fictional. Never copy facts from examples into a real CV.

# Example job-search workspace

These files show the method, not a target. The two personas are illustrations chosen to exercise hard cases; a real user's role families, job sites, languages and CV conventions come from their own intake.

- **Persona A, Lina Ortiz:** early-career, non-EU, job-search permit with an expiry date, targeting operations, sales development and customer success in Spain. Shows work-authorisation holds, a pre-revenue personal project described honestly, the same role rebuilt for different jobs, and CVs in English and Spanish.
- **Persona B, Elise Martin:** EU economics student targeting graduate consulting roles in France. Shows how the same method produces a different structure: education first and grade up front.

## Reading order

1. [Persona A intake](persona-a/intake.md): what the bot asks first.
2. [Master CV](persona-a/master-cv.md): tagged bullets, variants, functions performed, day-to-day tasks, proof points, accuracy notes.
3. [Rules](persona-a/rules.md): facts that override the master (note the deliberate grade conflict), banned words, title translations.
4. [English posting](persona-a/postings/01-startup-ops-en.md).
5. [English tailored CV](persona-a/tailored/01-Lina-Ortiz-CloudKite-Startup-Operations-Associate-CV.md) and its [notes](persona-a/tailored/01-notes.md): requirement map, how each role was reframed, gaps not claimed.
6. [Before and after](persona-a/qa/before-after.md): bullet repairs, a role rebuilt around the target job, and workflow mistakes with their fixes.
7. [Shortlist](persona-a/shortlist-2026-11-18.md) and [tracker](persona-a/tracker.csv): the daily loop and every status.

Then compare:

- the [Spanish posting](persona-a/postings/02-sdr-es.md), its fully [Spanish CV](persona-a/tailored/02-Lina-Ortiz-NexoVerde-SDR-CV.md) and [notes](persona-a/tailored/02-notes.md): the same founder role reframed for sales;
- the [posting not to apply to](persona-a/postings/03-closed-or-mismatch.md);
- the [answer bank](persona-a/answer-bank.md) and [banned-word cases](persona-a/qa/banned-words-cases.md);
- Persona B's [master](persona-b/master-cv.md), [rules](persona-b/rules.md), [posting](persona-b/posting.md), [tailored CV](persona-b/tailored/01-Elise-Martin-Juniper-Bridge-Graduate-Consulting-Analyst-CV.md) and [notes](persona-b/tailored/01-notes.md).

`legacy/` keeps the earlier single-persona example (a café shift lead moving into customer support).

## The same method in other fields

| User | Possible role families | Where the bot might search | CV conventions to confirm |
| --- | --- | --- | --- |
| Newly registered nurse | ward nurse • community nurse • clinic nurse | national health-service and hospital job portals, healthcare boards | registration number and expiry, clinical placements, education first |
| Self-taught software developer | junior backend • QA engineer • IT support | general and tech boards, company career pages | projects and repositories, skills with honest levels |
| Electrician | domestic electrician • maintenance technician • site supervisor | trade boards, agencies, local contractors | licences and certificates, driving licence, safety training |
| Teacher changing careers | learning designer • corporate trainer • tutor | education and public-sector portals, general boards | teaching evidence reframed as training and content design |
| Parent returning part-time | administrative assistant • receptionist • retail supervisor | local boards, part-time and flexible-work sites | hours and availability, how to describe the career break |

## Running the checks

```bash
python3 skills/job-cv-builder/scripts/qa_check.py \
  examples/persona-a/tailored/01-Lina-Ortiz-CloudKite-Startup-Operations-Associate-CV.md \
  --rules examples/persona-a/rules.md --master examples/persona-a/master-cv.md
```

Expected: PASS for every tailored CV; FAIL for `qa/banned-words-cases.md` (as `--extra-text`) and for `qa/title-mismatch-cv.md`.
