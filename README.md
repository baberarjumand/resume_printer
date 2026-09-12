# Resume Printer

**Live demo:** [Open on StackBlitz](https://stackblitz.com/~/github.com/baberarjumand/resume_printer)

A local React app that previews and downloads resume PDFs in several visual layouts.
Career content is produced with the
[tech-resume-generator](https://www.skills.sh/baberarjumand/technical-resume-generator_agent-skill/tech-resume-generator)
agent skill
([GitHub](https://github.com/baberarjumand/technical-resume-generator_agent-skill));
this repo adds custom layout rendering, PDF export, and a multi-layout preview UI on top of
that content.

## Setup

```bash
npm install
npx playwright install chromium   # needed for page-fit checks and bulk PDF export
npm run dev
```

Open the URL Vite prints (usually `http://localhost:5173`), or use the StackBlitz link above.

## What you get

Five nav options on the main page:

| Layout | Paper | Source | Notes |
| --- | --- | --- | --- |
| **1** | A4 | [`src/data/resume-layout1-*.json`](src/data/) → exported PDF | Single-column Inter |
| **2** | Letter | [`src/data/resume-layout2-*.json`](src/data/) → exported PDF | Two-column, blue accents |
| **3** | A4 | [`src/data/resume-layout3-*.json`](src/data/) → exported PDF | Dark two-column, teal header |
| **4** | Letter | [`src/data/resume-layout4-*.json`](src/data/) → exported PDF | Single-column Arial, ATS-strict |
| **5** | Letter | Skill one-pager PDF | Agent skill output (not a React layout) |

Layouts **1–4** each have **1 page** and **2 pages** variants (eight JSON files, eight exported
PDFs). Layout **5** is the skill-generated one-pager only.

The URL hash records the choice (for example `#layout2-1page` or `#layout5-1page`). The UI embeds
the matching PDF from [`tech-resume-generator_files/output/`](tech-resume-generator_files/output/)
and offers **Download PDF**. Live React rendering is reserved for export / page-check scripts via
`?render=1`.

## Data sources

Resume **facts** come from the skill workspace:

- [`tech-resume-generator_files/user_professional_data/`](tech-resume-generator_files/user_professional_data/) —
  career materials (LinkedIn exports, old resumes, certs, notes, PDFs, images, etc.). The agent
  skill extracts and compiles these into
  [`tech-resume-generator_files/output/professional_data.md`](tech-resume-generator_files/output/professional_data.md).
- [`tech-resume-generator_files/job_description_data/`](tech-resume-generator_files/job_description_data/) —
  optional. When present and you choose **JD-tailored** mode in the skill, the posting(s) here are
  analyzed so the résumé is tailored to that job description. Leave empty for a **general** resume.

This app’s layout JSON under [`src/data/`](src/data/) is authored from that compiled professional
data (and, when used, job-description analysis). Edit a JSON file, then re-export PDFs with
`npm run export:pdfs` if you want the preview downloads to match.

Use `**bold**` around words you want emphasized in summary and bullet text. Layouts 2 and 3
deliberately avoid bold inside bullets, so those markers are unused there.

Shared TypeScript shapes live in [`src/types/resume.ts`](src/types/resume.ts). Layout 4 also uses
optional fields such as `highlights`, `availability`, `companyNote`, and per-role `tech`.

**Education:** every layout variant lists only **University of Nottingham Malaysia**.

## Layouts vs the agent skill

The agent skill chooses an optimized ATS-safe format and writes its own JSON + PDF under
`tech-resume-generator_files/output/` (for example a general one-pager). **Custom layout logic is
not part of that skill** — it was added in this project so the same career content can be printed
in several visual styles.

Sample resumes used as layout guides live in
[`assets/resume_layouts/`](assets/resume_layouts/):

| Sample | Used as guide for |
| --- | --- |
| [`sample01_baber.pdf`](assets/resume_layouts/sample01_baber.pdf) | Layout 1 direction |
| [`sample02_brittany.pdf`](assets/resume_layouts/sample02_brittany.pdf) | Layout 2 direction |
| [`sample03_diogo.pdf`](assets/resume_layouts/sample03_diogo.pdf) | Layout 3 direction |

Layout 4 follows the writing / ATS rules in [`@state/resume_guidelines.md`](@state/resume_guidelines.md)
as closely as practical (single column, Letter, Arial, no colour or columns). Layout 5 surfaces the
skill PDF directly.

## Layout notes

1. **Layout 1** — classic single-column tech resume; Inter; summary, experience, skills, education,
   optional additional section.
2. **Layout 2** — Brittany-style two-column Letter; experience on the left, skills / projects /
   education / certifications / languages on the right.
3. **Layout 3** — dark Diogo-style A4; sidebar contact and skills, main column for summary,
   experience, education, and optional projects / leadership. Turn **Background graphics** on when
   printing from a live React render.
4. **Layout 4** — ATS-oriented Letter layout:
   - Single column, Arial 10 pt, 0.75 in equal margins
   - No colour, shading, boxes, columns, photo, or skill bars
   - Bullet summary plus remote / location line; skills high on the page
   - Company left / location right; title left / dates right
   - Optional company note and per-role `Technology:` line
   - Two-page version labels the last page `Name — Resume, page 2 of 2`
5. **Layout 5** — embeds the skill-generated one-pager PDF (no React sheet).

There is **no phone number** in the LinkedIn source data. Add one to `links.phone` in a Layout 4
JSON (and any other variant that supports it) if you want it in the header. The skill PDF may use
an email-availability placeholder instead of inventing a number.

## Checking that a variant still fits

`npm run check:pages` builds a temporary bundle, opens each Layout 1–4 variant with live React
rendering (`?render=1`), measures sheet height in pages, and exits non-zero on overflow:

```bash
npm run check:pages
```

Example output:

```
layout 1 / 1-page: 0.98 pages  fits
layout 1 / 2-page: 1.99 pages  fits
...
layout 4 / 2-page: 1.96 pages  fits
```

Run it after editing any resume JSON under `src/data/`.

## Print / download

On the main page, use **Download PDF** for the pre-exported file for the active layout.

To regenerate PDFs from the React layouts (Layouts 1–4):

```bash
npm run export:pdfs
```

That writes (and overwrites) `layout1-1page.pdf` … `layout4-2page.pdf` under
[`tech-resume-generator_files/output/`](tech-resume-generator_files/output/). The exporter picks the
correct paper size, enables background graphics, and fails if a file does not land on the expected
page count.

For a one-off print from a live React render, open
`http://localhost:5173/?render=1#layout1-1page` (or another hash), then use the browser print dialog:

- Destination: **Save as PDF**
- Paper: **A4** for Layouts 1 and 3, **Letter** for Layouts 2 and 4
- Margins: **None**; headers/footers: **Off**
- Background graphics: **On** (required for Layout 3)

Chrome or Edge give the most reliable result.

## Project structure

```
resume-printer/
├── README.md
├── package.json
├── vite.config.ts
├── index.html
├── public/                          # static assets for Vite (symlink to skill workspace)
│   └── tech-resume-generator_files/ → ../tech-resume-generator_files
├── src/
│   ├── App.tsx                      # nav, PDF preview, optional ?render=1 live layouts
│   ├── App.css
│   ├── main.tsx
│   ├── components/                  # Layout 1–4 React sheets + CSS
│   ├── data/                        # eight resume JSON variants
│   ├── types/resume.ts
│   └── lib/                         # dates, rich text helpers
├── scripts/                         # project Node scripts (see Scripts below)
│   ├── export-pdfs.mjs
│   └── measure-pages.mjs
├── assets/
│   └── resume_layouts/              # sample PDFs used as layout guides
├── tech-resume-generator_files/     # skill I/O (outside the skill install)
│   ├── user_professional_data/      # career inputs
│   ├── job_description_data/        # optional JD inputs
│   └── output/                      # skill + layout PDFs, professional_data.md
├── @state/                          # local notes (extracted capture, guidelines)
└── .agents/skills/tech-resume-generator/   # installed agent skill
```

## Scripts

Node helpers under [`scripts/`](scripts/) (project root, not the skill folder):

| File | What it does |
| --- | --- |
| [`scripts/measure-pages.mjs`](scripts/measure-pages.mjs) | Serves the temporary Vite build, opens each Layout 1–4 hash with `?render=1`, measures sheet height in pages, prints a fit / OVER report, exits non-zero on overflow. Used by `npm run check:pages`. |
| [`scripts/export-pdfs.mjs`](scripts/export-pdfs.mjs) | Same temporary build + Playwright Chromium flow, prints each layout to PDF with the correct paper size, writes files under `tech-resume-generator_files/output/`, and fails if page count ≠ expected. Used by `npm run export:pdfs`. |

The agent skill has its own scripts under
[`.agents/skills/tech-resume-generator/scripts/`](.agents/skills/tech-resume-generator/scripts/)
(`init_workspace.mjs`, `extract_user_data.py`, `generate_resume_pdf.mjs`, etc.) — those run as part
of the skill workflow, not via this package’s npm scripts.

## npm scripts

| Command | Purpose |
| --- | --- |
| `npm run dev` | Local Vite preview server |
| `npm run build` | Type-check and production build |
| `npm run lint` | Oxlint |
| `npm run check:pages` | Build + measure Layouts 1–4; fail on overflow |
| `npm run export:pdfs` | Build + write Layout 1–4 PDFs to `tech-resume-generator_files/output/` |
| `npm run preview` | Serve the production build |
