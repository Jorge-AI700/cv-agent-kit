# Before and after (fictional)

## 1. Bullet repairs

| Before | After | Lesson |
| --- | --- | --- |
| Responsible for lead generation and CRM. | Built a **340**-workshop prospect list from public directories and set up two CRM pipelines tracking more than 50 conversations from first contact to a booked call. | Vague duty → action, scope and result. |
| Sold the booking tool to workshop clients. | Onboarded three pilot workshops, which used the tool free of charge. | Inflated → honest. Never imply customers or revenue that do not exist. |
| Expert in SQL, Python and Power BI. | Skills: `SQL (basic)`, backed by a bullet where SQL was used; Python and Power BI removed. | Skill claims need a level and a bullet that proves them. |
| Talked to workshop owners. (Posting says "discovery interviews".) | Ran **25** discovery interviews with workshop owners to define booking requirements and recurring objections. | Use the posting's own words where they are true. |
| Reconciled **1,200** records, cut cases from **42** to **17** in **6** weeks. | Reconciled 1,200 weekly records and documented a workflow, reducing unresolved cases from **42 to 17** over six weeks. | Bold one key result, not every number. |

## 2. Rebuilding a role around the target job

The same master role, `Founder — RutaTaller`, for a **Customer Success Coordinator** posting.

**Before (copied from the master's headline bullets):**
```markdown
### Founder — RutaTaller | Valencia, Spain | Jan 2026–Present
_Personal booking-tool project._
- Built a 340-workshop prospect list and set up two CRM pipelines.
- Ran 25 discovery interviews with workshop owners.
```
True, but it reads as a sales role and wastes the space.

**Wrong fix (title changed, task invented):**
```markdown
### Customer Success Manager — RutaTaller | Valencia, Spain | Jan 2026–Present
- Reduced churn by 20% across the customer base.
```
`qa_check.py` fails it: the title does not match the master, and "20%" has no source. There were no paying customers, so there is no churn.

**After (real title kept, function added, bullets rebuilt from recorded tasks):**
```markdown
### Founder (Customer Success) — RutaTaller | Valencia, Spain | Jan 2026–Present
_Personal, pre-revenue booking tool for bicycle-repair workshops; onboarding, training and support for three pilot workshops._
- Onboarded **three pilot workshops** and trained their staff by video call.
- Answered pilot workshops' support questions by email and WhatsApp, usually the same day.
- Wrote a 12-article help centre covering set-up, bookings and reminders.
- Ran 25 discovery interviews with owners to understand booking problems and objections.
```
Every bullet maps to a recorded function (`user onboarding`, `customer support`, `help-centre writing`, `discovery interviews`) or task in the master. The fixture [title-mismatch-cv.md](title-mismatch-cv.md) holds the wrong version so the check can be tested.

## 3. Workflow failures and their fixes

| Before | After |
| --- | --- |
| A saved profile pre-filled the old home-country phone number (+57) on a one-click application. | Corrected to the number in the rules file; the log says "checked every pre-filled field". |
| A rewrite of a "why us" answer put "demo" back in. | `qa_check.py --extra-text answers.md` catches it before submission: `ERROR banned term 'demo'`. |
| The bachelor's grade was copied from an older tailored CV (4.3). | Facts come only from master plus rules; the rules value (4.1) wins. |
| A CV was tailored for a posting that had already closed. | The liveness and deadline check runs before any tailoring. |
| "London or Valencia" was guessed as Valencia. | The role is `held` and the question goes to the user. |
| The bot ticked "authorised to work: yes" itself. | The role is `held` with ASK USER; the user's answer is logged for that application. |
| Logged as `submitted` after clicking the button, with no confirmation. | Status stays `unconfirmed` until a confirmation page, email, or portal status exists. |
| The CV ran onto a second page, or filled only half of one. | Rebalance the bullet budget and re-render until it is exactly one full page. |
| The CV listed every role with equal weight. | Three or four bullets for the main role, two for others, one for the oldest. |
