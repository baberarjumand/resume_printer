# Workspace data contract

After install / first use, the skill creates **`tech-resume-generator_files/` at the workspace / project root** (sibling to `.agents/skills/` or `.cursor/skills/`, not inside the skill package).

```
tech-resume-generator_files/
  user_professional_data/   # career materials
  job_description_data/     # job postings (JD-tailored)
  output/                   # generated resumes
```

## user_professional_data/

Any mix of:

- Old resumes (PDF, DOCX, Markdown, plain text, images)
- LinkedIn exports or full-page PDF / PNG snapshots
- Certificates and transcripts (PDF or images)
- Portfolio or personal-site dumps (Markdown, JSON, TypeScript, text)
- Notes about roles, metrics, projects, skills
- Screenshots of profiles or job history

Subfolders are fine. The agent inventories everything recursively. **Do not skip unknown files.**

## job_description_data/

**General resume:** no JD required.

**JD-tailored resume:** provide the posting via one of:

1. Paste into chat when the agent asks (agent may save a copy here)
2. Files in this folder (`.md`, `.txt`, `.pdf`, etc.)
3. Multiple postings in subfolders as needed

## Privacy

Do not commit personal documents to a public repo. Keep folder *contents* gitignored (READMEs may stay tracked).

## Outputs

Compiled facts and resumes are written under **`tech-resume-generator_files/output/`**, not inside the skill package.

## Browser hosts

Browser chats have no project folder — upload files in chat instead. See the skill’s Browser workflow.
