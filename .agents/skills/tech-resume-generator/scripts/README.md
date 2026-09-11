# Scripts

Paths below are relative to the **skill directory** (`tech-resume-generator/`). Data folders live under the workspace root in `tech-resume-generator_files/`.

## `init_workspace.mjs`

Creates `<workspace>/tech-resume-generator_files/` with:

- `user_professional_data/` — career materials  
- `job_description_data/` — job postings  
- `output/` — generated résumés  

Each folder gets a `README.md` (existing READMEs are left unchanged).

```bash
node scripts/init_workspace.mjs --help
# from project root after npx skills add (no -g):
node .agents/skills/tech-resume-generator/scripts/init_workspace.mjs
node .cursor/skills/tech-resume-generator/scripts/init_workspace.mjs
# or:
node scripts/init_workspace.mjs --workspace /path/to/project
```

## `extract_user_data.py`

Inventories a career-data folder and extracts what it can.

```bash
python3 scripts/extract_user_data.py --help
python3 scripts/extract_user_data.py \
  --input /path/to/workspace/tech-resume-generator_files/user_professional_data \
  --output /path/to/workspace/tech-resume-generator_files/user_professional_data/_extracted
```

Outputs under `--output`:

| Path | Contents |
| --- | --- |
| `text/` | PDF text via `pdftotext` |
| `copies/` | Copies of `.md`, `.txt`, `.json`, `.ts`, etc. |
| `images/inventory.json` | Image paths for agent OCR/vision |
| `renders/` | PNG pages for low-text PDFs (needs `pdftoppm`) |
| `manifest.json` | Full index, including `unsupported` files |

Requires Python 3. Optional: `poppler-utils`, Pillow. No network. Non-interactive.

**Unsupported formats:** Write `scripts/extractors/<format>_extract.py`, run it, continue. Do not skip those files.

## `generate_resume_pdf.mjs`

Renders a one-page Letter résumé PDF from JSON (sibling `.pdf`).

```bash
node scripts/generate_resume_pdf.mjs --help
npm install   # once, in this skill directory (pdf-lib)
node scripts/generate_resume_pdf.mjs /path/to/workspace/tech-resume-generator_files/output/general/name_resume.json
```

From the cloned repo root (postinstall installs skill deps):

```bash
npm install
npm run generate-resume -- output/general/name_resume.json
```

JSON shape: [../references/json_schema.md](../references/json_schema.md). Requires Node.js 18+ and `pdf-lib`.

## `eval_grade.py` / `eval_aggregate.py`

Core eval tooling ([evaluating-skills](https://agentskills.io/skill-creation/evaluating-skills)). See [../evals/README.md](../evals/README.md).

```bash
python3 scripts/eval_grade.py --help
python3 scripts/eval_aggregate.py --help
```

## `download_sample_resumes.py`

**Optional.** Downloads the research sample corpus into `assets/sample_resumes/` (~100MB+). Not required to generate a résumé.

```bash
python3 scripts/download_sample_resumes.py
# or from repo root: npm run download-samples
```

Requires `curl` and network. Review URLs in `assets/sample_resumes/download_manifest.json` first. Downloaded blobs are gitignored.

## `extractors/`

Empty by default. Agent-written extractors for novel file types belong here. Keep scripts non-interactive (flags only; no prompts).
