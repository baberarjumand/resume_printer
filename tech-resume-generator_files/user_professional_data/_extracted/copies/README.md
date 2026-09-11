# user_professional_data

Put **your career materials** in this folder.

This is the primary input for the **tech-resume-generator** skill: anything that describes *you* (experience, education, skills, credentials).

## What to put here

Any mix of:

- Old resumes (PDF, DOCX, Markdown, plain text, images)
- LinkedIn exports or profile PDF / PNG snapshots
- Certificates and transcripts
- Portfolio or personal-site dumps (Markdown, JSON, TypeScript, text)
- Notes about roles, metrics, projects, and skills
- Screenshots of profiles or job history

Subfolders are fine (`certs/`, `old_resumes/`, `linkedin/`, etc.). The agent inventories everything recursively.

## What *not* to put here

- Job descriptions / postings → use sibling folder `job_description_data/`
- Generated résumés → those go under sibling folder `output/`

## Privacy

Do not commit personal documents to a public repo. Prefer gitignoring contents of this folder (except this README).

## Next step

After adding files, ask your agent:

> Use the tech-resume-generator skill to generate my tech resume.
