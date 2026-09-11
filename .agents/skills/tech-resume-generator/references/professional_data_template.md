# Professional data template

Write `tech-resume-generator_files/output/professional_data.md` in this shape after extracting `user_professional_data/`. Fill only with facts found in the user’s files. Use `Unknown` or omit a subsection when evidence is missing — never invent.

```markdown
# Professional data — <Full Name>

Compiled: <ISO date>
Sources: <list of files used>
Precedence: official docs > LinkedIn timeline > old resume wording > notes

## 1. Identity and public profiles

| Field | Value | Source |
| --- | --- | --- |
| Full name | | |
| Location (city, country) | | |
| Phone | | |
| Email | | |
| Website(s) | | |
| LinkedIn | | |
| GitHub | | |
| Other | | |

Do **not** put street address, photo, DOB, or government IDs on the résumé even if present here.

## 2. Professional summaries (raw)

Paste or paraphrase existing About / summary text from LinkedIn or old resumes for reference. Do not ship these paragraphs verbatim on the one-pager unless shortened to a TIH-style headline.

## 3. Experience (newest first)

For each role:

### <Title> — <Company> (<Start> – <End>)

- Location / remote:
- Employer vs client (if different):
- Stack / tools mentioned:
- Bullets / achievements with any metrics (quote sources):
- Reconciliation notes:

## 4. Education

| Degree | School | Years | Notes |
| --- | --- | --- | --- |

Mark incomplete transfers / dual enrollments and whether the user wants them on the résumé.

## 5. Courses (optional)

## 6. Tests / scores (optional — usually omit from résumé)

## 7. Professional projects

## 8. Personal / open-source projects

## 9. Skills

Group by category as found in sources. Note which are interview-defendable.

## 10. Licenses and certifications

Only credentials with evidence in `user_professional_data/`.

## 11. Volunteering / leadership

## 12. Languages (spoken)

## 13. Continuing studies

## 14. Source inventory

List every file under `user_professional_data/` and whether it was extracted.

## 15. Reconciliation notes

Conflicts (title variants, dates, employer naming) and the chosen resolution.

## 16. Career timeline (one line)

`<year>–<year> Role @ Company; ...`
```

After this file is complete, author the resume JSON from it using `99_cross-source-rules.md`.
