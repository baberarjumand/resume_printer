# job_description_data

Put **job descriptions / postings** here when you want a **JD-tailored** résumé.

Leave this folder empty (or unused) for a **general** optimized tech résumé.

## What to put here

Any mix of:

- `job_description.md` / `.txt` / `.pdf` for a single target role
- Multiple postings, e.g.:
  ```
  job_description_data/
    acme-frontend-engineer.md
    bigco-staff-swe.pdf
    jobs/contoso-platform.md
  ```
- Pasted JD text saved as a file after the agent asks

## How the skill uses this

- **General mode:** ignores this folder (unless you later ask to tailor).
- **JD-tailored mode:** reads one or more files here and emphasizes true keywords / ordering from your `user_professional_data/` only — never invents employers or metrics from the JD.

## What *not* to put here

- Your old resumes, LinkedIn exports, or certs → use `user_professional_data/`
- Generated outputs → use `output/`

## Privacy

Job postings are usually public, but still avoid committing anything you consider sensitive.
