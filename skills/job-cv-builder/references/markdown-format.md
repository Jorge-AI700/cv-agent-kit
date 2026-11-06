# Tailored CV Markdown format

`scripts/render_cv.py` reads a simple Markdown file and turns it into DOCX and PDF. Write `cv.md` in this structure so the renderer can map each part to the layout.

```markdown
# Firstname Lastname

Optional headline in one plain line

City, Country · email@example.com · +00 000 000 · linkedin.com/in/example

## Profile

A short paragraph. **Bold** is allowed.

## Skills

- Skill or strength supported by the master CV
- Another skill

## Experience

### Role title | Jan 2022 – Mar 2024
Organization name, City

- Action, what you did, and a measurable result when you have one
- Another bullet with **bold** used sparingly

### Earlier role | 2020 – 2021
Another organization

- Fewer bullets than the more relevant or recent role above

## Education

### Degree name | 2021
School name, City

## Languages

- English (fluent)
- Spanish (conversational)
```

## Rules

1. **Name.** The first level-1 heading is the candidate's name.
2. **Headline and contact.** The first one or two plain paragraphs after the name, before any heading or bullet, are the headline and the contact line. If there is only one paragraph and it looks like contact information (an email, URL, or phone number), it is treated as the contact line. Otherwise it is the headline. Separate contact items with ` · ` or `|`.
3. **Sections.** Level-2 headings (`## Experience`) become uppercase section headings with a thin underline. Prefer conventional names: Profile or Summary, Experience or Work Experience, Education, Skills, Projects, Languages, Certifications.
4. **Entries.** A level-3 heading is an entry title. Put dates after a space-pipe-space (` | `) so the renderer can right-align them. The optional plain paragraph immediately after the heading is the organization and location line. Bullets that follow belong to that entry.
5. **Standalone bullets.** Bullets that are not under a level-3 heading (for example in Skills) are rendered as a simple list.
6. **Paragraphs.** Other plain paragraphs, such as the profile, are body text.
7. **Inline markup.** `**bold**` is supported. `[label](url)` is rendered as `label`. HTML comments and YAML front matter are ignored.
8. **Do not rely on tables, images, headers, or text boxes.** The renderer ignores those features, and they are unsafe for applicant tracking systems.

The Markdown file remains the portable version of the CV. The DOCX and PDF are generated from it.
