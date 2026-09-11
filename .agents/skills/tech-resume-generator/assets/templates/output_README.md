# output

The **tech-resume-generator** skill writes generated artifacts here. You normally do **not** place source career files in this folder.

## Typical contents

| Path | Meaning |
| --- | --- |
| `professional_data.md` | Compiled, reconciled facts from your sources (facts only) |
| `general/<slug>_resume.json` | General one-page résumé source |
| `general/<slug>_resume.pdf` | Rendered PDF (sibling of the JSON) |
| `tailored/<job-slug>/<slug>_resume.json` | JD-tailored résumé JSON |
| `tailored/<job-slug>/<slug>_resume.pdf` | JD-tailored PDF |

## Editing

You can tweak the `.json` by hand and re-run:

```bash
node scripts/generate_resume_pdf.mjs path/to/resume.json
```

(from the installed skill directory, after `npm install` there).

## What *not* to put here

- Raw career dumps → `user_professional_data/`
- Job postings → `job_description_data/`

## Privacy

Generated résumés contain personal data. Do not commit them to a public repo unless you intend to.
