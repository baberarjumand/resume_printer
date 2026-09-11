# Usage examples

## Example 1 — General resume

**User**

> I put my old resumes, LinkedIn PDFs, and certs in `tech-resume-generator_files/user_professional_data/`. Please use tech-resume-generator to make my resume.

**Agent**

1. Runs `init_workspace.mjs` if needed (repo probe); on success continues with **repo workflow**.
2. Asks: general vs JD-tailored → user picks **general**.
3. Runs `scripts/extract_user_data.py` on `tech-resume-generator_files/user_professional_data/`.
4. Writes `tech-resume-generator_files/output/professional_data.md`.
5. Applies `99_cross-source-rules.md`; writes `tech-resume-generator_files/output/general/jane_doe_resume.json`.
6. Renders PDF; trims on overflow; delivers paths.

## Example 2 — JD-tailored (paste)

**User**

> Generate a tailored tech resume for this posting: [pastes JD for Staff Frontend Engineer at Acme].

**Agent**

1. Confirms mode = **JD-tailored** (JD already in chat; may save under `job_description_data/`).
2. Extracts and compiles facts from `user_professional_data/`.
3. Authors `tech-resume-generator_files/output/tailored/acme-staff-frontend/jane_doe_resume.json` with Acme keywords only where true.
4. Renders PDF; delivers paths.

## Example 3 — JD file on disk

**User**

> I added a posting under `tech-resume-generator_files/job_description_data/`. Make a tailored resume.

**Agent**

1. Confirms tailored mode.
2. Reads the JD from `job_description_data/`.
3. Compiles facts; writes tailored JSON under `output/tailored/<slug>/`.
4. Renders PDF.

## Example 4 — Batch JD tailor

**User**

> Tailor resumes for everything in `tech-resume-generator_files/job_description_data/`.

**Agent**

1. Lists each file under `job_description_data/`.
2. Produces one tailored folder per posting under `output/tailored/`.
3. Still only true facts from `user_professional_data/`.

## Example 5 — Unsupported format

**User**

> I dropped an `.odt` resume and a Notion HTML export into `user_professional_data/`.

**Agent**

1. Runs `extract_user_data.py`; sees them listed under `unsupported` in `manifest.json`.
2. Writes extractors under `scripts/extractors/`, runs them, continues.

## Example 6 — Browser chat

**User** (Claude.ai / ChatGPT web)

> [uploads PDFs] Make my tech resume ATS-friendly.

**Agent**

1. `init_workspace.mjs` fails or is unavailable → **browser workflow**.
2. Uses uploads as career sources; asks general vs JD-tailored.
3. Returns JSON/Markdown draft; suggests local PDF render if needed.
