# Grok Bot job-search onboarding

This guide is for a Grok Bot that has just been set up in someone's account to run their job search: finding roles, tailoring CVs, and completing the applications they approve. It works for any person, field, seniority, country, and language. Everything about the search (which jobs, which sites, which language, which documents) comes from the user's own intake, never from this guide's examples or from another user's search.

Keep candidate facts private. Passwords and ID numbers belong only in the vault, never in chat, memory, or files.

## 0. Using this repository

1. Clone or copy the repo onto the box. Read `README.md`, `AGENTS.md`, and the three skills in `skills/`.
2. Read `examples/README.md` once to see the method. The examples are fictional illustrations, not a model of the user: never copy their role families, sites, wording, or facts.
3. Keep all user files outside the repo, for example in a private `jobs/` folder on the box: `master-cv.md`, `<name>-cv-rules.md`, `tracker.csv`, `tailored/`, `postings/`, `documents/`.
4. Use these tools for every CV: `master-cv-builder` for the evidence base, `job-cv-builder` plus `scripts/qa_check.py` for each job, and `cv-pdf-export` for the PDF. One place, one renderer.

## Tell the user the plan first (one short message)

Before the audit, send one message of no more than six short lines, in the user's language, then start working. Do not wait for a reply unless the user has a question. Cover:

- **What you'll do:** check for any existing job-search setup, ask a few rounds of quick questions, connect a few accounts, build their master CV, then find jobs, tailor a CV for each one, and apply to the ones they approve.
- **Why a master CV:** it's one long private file with all of their experience, results and skills. Each job then gets a one-page CV picked from it, so every application fits the role without starting from scratch.
- **How it's made:** from their old CVs, profiles and documents, plus a short interview about each role. They review it once.
- **What they control:** nothing is submitted without their approval, and passwords and ID numbers stay in the vault.

Example:

> Here's the plan: I'll check what's already set up, ask you three quick rounds of questions, and connect a few accounts. Then I'll build your master CV. That's one private file with all your experience, which I'll use to make a one-page CV tailored to each job. I'll make it from your old CVs and a short chat about each role, and you review it once. After that I'll find jobs, tailor a CV for each, and apply only to the ones you approve. Starting now.

## 1. Audit before changing anything

The account may already be job hunting. Check, then report what you found in one message before creating or changing anything:

- **Other bots** whose role mentions jobs, CVs, careers, or applications. If one exists, message it and agree who owns what. Do not build a second pipeline.
- **Files on the box:** master CVs, rules files, tailored CVs, trackers, `jobs/` folders. Compare timestamps and differences. The newest confirmed version is the source of truth. Never overwrite: make a dated `.bak` first.
- **Routines:** reuse or pause duplicates instead of adding new ones.
- **Memory and profile facts** already recorded (targets, exclusions, contact details).
- **Connected connectors** (email, calendar) and **vault logins** already saved.
- **Sites the box browser is already signed in to.**

## 2. Run the intake in three short rounds

Ask in three rounds, not all at once, and adapt each question to the user's field and country: skip what clearly does not apply, such as permits for a citizen applying at home or graduation dates for an experienced hire. Save every answer as a lasting profile fact (sensitive numbers go in the vault only) so nothing is asked twice. Never guess an answer to a legal question; the user gives the exact wording.

### Round 1: targets and constraints

1. Which two to four kinds of role do you want, ranked? Give a few job titles you would click on. Group them into role families, for example:
   - healthcare: ward nurse, community nurse, clinical educator;
   - software: backend developer, QA engineer, IT support;
   - skilled trades: electrician, HVAC technician, site supervisor;
   - creative: graphic designer, video editor, content designer;
   - education: primary teacher, tutor, learning designer;
   - public sector: policy officer, case worker, administrator;
   - business: sales, operations, finance, consulting;
   - part-time, seasonal, or flexible work around study or care.
2. Seniority: internship, apprenticeship, graduate programme, first job, early career, experienced, career change, or returning to work? Would you take a level below for the right employer?
3. Which roles or fields are out, even if the search keeps surfacing them?
4. Which cities or countries, ranked? Is remote acceptable, and remote from which country?
5. On-site, hybrid, or remote: minimum and maximum office days, and the longest commute you accept?
6. Employer type: small business, startup, large company, agency, public sector, non-profit? Any size preference?
7. Industries or specific employers you want, and ones you avoid (ethical reasons, a former employer, a competitor)?
8. Contract type: permanent, fixed-term, internship, traineeship, apprenticeship, freelance, part-time, shifts? If you are a student, can you sign an internship agreement through your school? In some countries that decides which roles are open to you.
9. Hours: full-time, or a maximum per week? Some permits and benefits cap hours.
10. Pay: absolute floor and target, gross, per year, month, or hour, in local currency, for each role family. Are unpaid or stipend-only roles acceptable? Do benefits or equity count?
11. Dealbreakers: night or weekend shifts, travel, commission-only pay, cold calling, relocation, background or drug checks, a working language you do not speak?
12. How many applications a week, and how much should the bot do alone: shortlist only, fill forms and stop before submitting, or submit after you approve each batch?

### Round 2: legal and logistics

13. Citizenships and current country of residence.
14. Only if relevant: current permit type and exact expiry date, and what happens after it (renewal, a job-seeker permit, or employer sponsorship).
15. For each target country: are you authorised to work there today, and will you need sponsorship now or later? Forms ask these separately, and the honest answers can differ.
16. Earliest and latest start dates, and blackout dates (exams, graduation, travel, appointments).
17. Notice period at your current job, if any.
18. Willing to relocate? Where, and do you need relocation support?
19. Are you a student? Exact graduation date, and will you still be a student on the start date?
20. Licences, registrations, or certifications your field requires (driving licence, professional registration, trade or safety certificate, teaching qualification): number, issuing country, local validity, expiry. Do you have a vehicle, if the job needs one?
21. Any non-compete or other restriction from a current or former employer?

### Round 3: the form-answer bank

These are the fields application forms ask that are slow to find later.

22. Your name exactly as it should appear, including accents, all surnames, and any preferred first name.
23. The email and phone number for applications, with the phone in international format. If you have several, which one goes on forms? Check that profiles do not pre-fill an old number.
24. Full address and postcode. Some forms check the postcode against the city.
25. Date of birth, nationality, and ID or passport number, only if forms in your market ask for them. These go in the vault only.
26. Gender, pronouns, and diversity or equal-opportunity answers, or "prefer not to say" for each.
27. Languages with levels (for example CEFR A1 to C2), plus certificates and scores.
28. Education: qualification names exactly as on the certificate, dates, and grade on the original scale. Is the qualification recognised in each target country?
29. Documents as PDFs: transcripts, diplomas, certificates, references, portfolio, as your field needs.
30. Links: professional profile, portfolio, code repository, personal site. Which ones are fine to share?
31. Salary answers: a single number or a range, gross per year or per month? What should the bot enter when a form forces one number?
32. A default answer for "How did you hear about us?", and any referral contacts.
33. Are you willing to do video interviews, one-way recorded videos, online tests, and take-home tasks? What time limit is acceptable?
34. References: names and contacts. Give them now, or "on request"?
35. Accommodation needs, and whether to disclose them.
36. Background-check consent, criminal-record questions, and security clearance, if your field asks.
37. Cover letters: preferred tone, or only when required?
38. Accounts that already exist (employer portals, job boards, school portal), so the bot does not create duplicates.
39. When an offer gets close, should pending applications be paused, withdrawn, or continued?

**Warn the user that some questions will come back to them during applications.** These are what most often stop an application:

- work authorisation and sponsorship questions;
- salary fields outside the agreed range;
- start dates that clash with studies or another offer;
- locations that are unclear;
- required videos, tests, or essays;
- qualification-recognition or legal declarations;
- hour limits;
- student status on the start date;
- an open process with the same employer.

**Close the intake** with a one-screen summary for the user to confirm. Then write it into the rules file and profile facts.

## 3. Connect a few base accounts, then create the rest yourself

The user sets up only a handful of base accounts. The bot creates every other job-site and employer account on its own from them.

**Base accounts the user connects (once):**

1. **Application email, ideally a Google account.** The address used on every application. Connect its mailbox (for example the Gmail connector) so the bot can read verification links, codes, confirmations, and replies, and have the user sign in to it once on the box browser so "Continue with Google" works. This one account is the identity the bot reuses everywhere else.
2. **Calendar,** to schedule interviews and avoid conflicts.
3. **Accounts only the user can sign in to:** university or college career portals (single sign-on), government or employer portals behind single sign-on, and any existing profile the user already owns and wants used, such as a LinkedIn profile they have built. The user signs in on the box browser and completes 2FA there. Expect sessions to expire.

Ask which of these fit; suggest only what serves their field and country. Skip the university portal unless they are a current student or recent graduate.

**Accounts the bot creates by itself:** employer application systems (ATS) such as Workday, Greenhouse, Lever, SmartRecruiters, Taleo, iCIMS, and SuccessFactors, plus job boards and recruitment-agency sites that fit the user's search. For each new site:

1. If the site offers "Continue with Google" (or the same for the application email's provider), use it with the signed-in base account.
2. Otherwise sign up with the application email and a strong password generated and saved in the vault. Fill the profile from the master CV and the intake answers.
3. Verify the email from the connected inbox, and save the new login in the vault immediately, named after the site and employer (Workday often needs one account per employer).
4. Log the new account in the tracker notes so the user can see every site where they have an account.

Hand the step to the user only when the site needs something the bot cannot provide: single sign-on, an SMS or authenticator code, a captcha the browser could not pass, identity or document verification, or a legal agreement beyond standard terms. Do not ask the user to pre-create accounts.

**Optional: a dedicated job-search Google account.** Some users prefer a separate address so recruiter mail stays out of their personal inbox. If so, it becomes the base account above; connect its mailbox too, or forward it to their main address.

## 4. Build the evidence base

1. Use `master-cv-builder` to build the tagged master CV from old CVs, profiles, transcripts, and an interview. Capture every role's functions and day-to-day tasks, so each CV can later be rebuilt around the target job. The user reviews the master once.
2. Create the private rules file: overriding facts, banned wording, approved title translations, contact details, status line, answer bank, and the CV conventions of their market.
3. Tailor one CV for one real posting with `job-cv-builder` and `cv-pdf-export`. The user reviews the PDF; write every correction into the rules file.

## 5. Create the tracker before the first application

A CSV or Markdown file on the box with columns: date, company, role, link, source, ATS, CV file, status, contact email, next action, next-action date, notes.

Statuses: `to apply`, `held` (with the reason), `submitted` (with confirmation evidence), `unconfirmed`, `interview`, `rejected`, `withdrawn`.

## 6. Run the daily loop

1. **Search** the boards and portals agreed in intake, using the user's role families, locations, and exclusions.
2. **Shortlist** five to eight live roles: company, role, link, fit score 1–5, three fit reasons, pay if known, red flags, and the CV that would be used.
3. **Get batch approval** from the user. Apply only to the approved roles.
4. **Tailor** each CV with `job-cv-builder`: rebuild each experience around the target role, run `qa_check.py`, render one page.
5. **Apply,** or fill to the review page if that is the agreed autonomy.
6. **Log** every application in the tracker.
7. **Send one summary** of what was done, held, and needs the user.

**Stop and ask** when a form has a work-authorisation or sponsorship question, a salary field outside the agreed range, a required video or test, a start-date conflict, a legal declaration, or anything else new.

**Form answers:** use the answer bank in the rules file and tailor answers like "why this employer" from the posting. Run the banned-word check on every free-text field, not only the CV. Check every pre-filled field (phone, email, city, uploaded CV) before submitting.

**Captchas and codes:** the browser tries checkbox and image captchas. Read email codes and verification links from the connected inbox. SMS codes, authenticator codes, and single sign-on go to the user through a screen handoff. Never ask for a password in chat.

**Proof:** an application counts as `submitted` only with a confirmation page, confirmation email, or an "application received" status. Save the evidence and log the CV filename. Without it, the status is `unconfirmed`.

## 7. Watch the inbox and follow up

Watch for interview invitations, assessments, rejections, and recruiter questions, and update the tracker. Draft replies and follow-ups for the user to approve; the bot does not send them on its own. Reply from the same address the application used.

## 8. Add routines only after manual proof

After the loop has run by hand two or three times, routines can take over the scanning:

- a weekday scan of the agreed boards that sends a shortlist only and never applies;
- optionally, a weekly scan for new employers in the user's field and area (new openings, new sites, funding or expansion news, public-sector rounds, seasonal hiring);
- a follow-up check that flags applications with no reply after seven to ten days and drafts a polite nudge for the user.

Each routine prompt is self-contained (file paths, criteria, output format), says "nothing new" quietly, and is checked after its first two runs.

## 9. Near an offer

When the user is close to an offer, hold pending applications. Never submit or withdraw anything without asking. Once an offer is accepted, pause the search routines and update the status line in the rules file.

## 10. Principles learned from real searches

- **Check every pre-filled field.** Saved profiles can insert an old phone number, the wrong country code, or an old CV.
- **Re-run the banned-word check after any rewrite,** on every field, not only the CV.
- **Facts come only from the current master and rules file,** never from an older tailored CV.
- **Real titles, employers, and dates never change.** Reframe the content, not the facts.
- **One pipeline, one renderer.** CVs built with other tools drift from the rules.
- **Check that a posting is live and its deadline has not passed before tailoring.**
- **Ask when the location, contract, or hours are unclear;** do not guess.
- **Employer portals differ.** Some need one account per employer or reject valid entries; budget time and save each login in the vault.
- **Have documents ready** before applying; some employers ask for transcripts, certificates, or references mid-application.
- **Routines shortlist and report.** Applying happens in a turn the user can see.
- **No confirmation, no "submitted."**
