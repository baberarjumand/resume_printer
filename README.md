# Resume Printer

A local React app that turns JSON resume data into on-screen print previews and PDFs.
Edit a JSON file, preview the result, then print from the browser or export all variants in
one shot.

This is a local tool. It is not hosted anywhere.

Resume content and the skill-format one-pager were produced with the
[tech-resume-generator](https://www.skills.sh/baberarjumand/technical-resume-generator_agent-skill/tech-resume-generator)
agent skill
([GitHub](https://github.com/baberarjumand/technical-resume-generator_agent-skill)).

## Setup

```bash
npm install
npx playwright install chromium   # needed for page-fit checks and bulk PDF export
npm run dev
```

Open the URL Vite prints (usually `http://localhost:5173`).

## What you get

Four visual layouts × two lengths = **eight resumes**:

| Layout | Paper | Style | 1-page JSON | 2-page JSON |
| --- | --- | --- | --- | --- |
| **1** | A4 | Single-column, dense Inter, ATS-friendly | [`resume-layout1-1page.json`](src/data/resume-layout1-1page.json) | [`resume-layout1-2page.json`](src/data/resume-layout1-2page.json) |
| **2** | Letter | Two-column, blue accents, projects / certs / languages | [`resume-layout2-1page.json`](src/data/resume-layout2-1page.json) | [`resume-layout2-2page.json`](src/data/resume-layout2-2page.json) |
| **3** | A4 | Dark two-column with teal header and grouped skills | [`resume-layout3-1page.json`](src/data/resume-layout3-1page.json) | [`resume-layout3-2page.json`](src/data/resume-layout3-2page.json) |
| **4** | Letter | Single-column Arial; strictest reading of the guidelines | [`resume-layout4-1page.json`](src/data/resume-layout4-1page.json) | [`resume-layout4-2page.json`](src/data/resume-layout4-2page.json) |

The top nav has a **1 page** and **2 pages** link under each layout. The URL hash records the
choice, for example `#layout2-1page` or `#layout4-2page`. The preview also links to the matching
PDF under [`tech-resume-generator_files/output/`](tech-resume-generator_files/output/).

Pre-generated PDFs of every layout variant (plus the skill general one-pager) live in
[`tech-resume-generator_files/output/`](tech-resume-generator_files/output/).

## Data sources

Content is derived from:

- [`@state/extracted_user_data.md`](@state/extracted_user_data.md) — verbose LinkedIn capture
- [`@state/resume_guidelines.md`](@state/resume_guidelines.md) — Harvard MCS + tech / FAANG writing rules used when generating content
- LinkedIn PDF snapshots under [`tech-resume-generator_files/user_professional_data/`](tech-resume-generator_files/user_professional_data/)

Each resume is a separate JSON file under [`src/data/`](src/data/). Edit the file for the variant
you want, save, and the preview hot-reloads.

Use `**bold**` around words you want emphasized in summary and bullet text. Layouts 2 and 3
deliberately avoid bold inside bullets, so those markers are unused there.

Shared TypeScript shapes live in [`src/types/resume.ts`](src/types/resume.ts). Layout 4 also uses
optional fields such as `highlights`, `availability`, `companyNote`, and per-role `tech`.

**Education:** every variant lists only **University of Nottingham Malaysia**.

## Layout notes

1. **Layout 1** — closest to a classic single-column tech resume; Inter font; summary, experience,
   skills, education, optional additional section.
2. **Layout 2** — Brittany-style two-column Letter; experience on the left, skills / projects /
   education / certifications / languages on the right.
3. **Layout 3** — dark Diogo-style A4; sidebar contact and skills, main column for summary,
   experience, education, and optional projects / leadership. Turn **Background graphics** on
   when printing.
4. **Layout 4** — built to follow [`@state/resume_guidelines.md`](@state/resume_guidelines.md) as
   literally as possible, so it is the safest choice for ATS-screened applications:
   - Single column, Letter, Arial 10 pt, 0.75 in equal margins
   - No colour, shading, boxes, columns, photo, or skill bars
   - Opens with a bullet summary (years of experience and scope) plus an explicit remote / location line
   - Technical skills high on the page as compact labeled sentences
   - Company left / location right; title left / dates right
   - One-line explainer under unfamiliar employers; per-role `Technology:` line
   - Two-page version labels the last page `Name — Resume, page 2 of 2`

There is **no phone number** in the extracted LinkedIn data. Harvard treats a missing phone as a
top mistake. Add one to `links.phone` in the Layout 4 JSON files (and any other variant you want)
and it will appear in the header.

## Checking that a variant still fits

The on-screen preview draws a faint grey rule at each page boundary. If content crosses the last
rule, the resume will spill onto an extra page when printed.

For an exact measurement of all eight variants:

```bash
npm run check:pages
```

This builds into `node_modules/.cache/resume-pages/` (so it does not disturb `npm run dev`),
renders every variant in headless Chromium, prints each height in pages, and exits non-zero if
anything overflows:

```
layout 1 / 1-page: 0.98 pages  fits
layout 1 / 2-page: 1.99 pages  fits
...
layout 4 / 2-page: 1.96 pages  fits
```

Run it after editing any resume JSON.

## Print one resume from the browser

1. Open the layout and page length you want; wait until fonts look right.
2. Click **Print**, or use **Download PDF** for the pre-exported file.
3. In the print dialog:
   - Destination: **Save as PDF**
   - Paper size: **A4** for Layouts 1 and 3, **Letter** for Layouts 2 and 4
   - Margins: **None** (each sheet supplies its own margins)
   - Headers and footers: **Off**
   - Background graphics: **On** (required for Layout 3)
4. Save.

Chrome or Edge give the most reliable result.

## Export all eight PDFs

```bash
npm run export:pdfs
```

Writes (and overwrites) these files under
[`tech-resume-generator_files/output/`](tech-resume-generator_files/output/):

- `layout1-1page.pdf` … `layout4-2page.pdf`

The exporter uses the correct paper size per layout, enables background graphics, and fails if a
file does not land on the expected page count.

## Project map

| Path | Role |
| --- | --- |
| [`src/App.tsx`](src/App.tsx) | Layout / page-length nav via URL hash |
| [`src/components/Resume.tsx`](src/components/Resume.tsx) | Layout 1 |
| [`src/components/ResumeLayout2.tsx`](src/components/ResumeLayout2.tsx) | Layout 2 |
| [`src/components/ResumeLayout3.tsx`](src/components/ResumeLayout3.tsx) | Layout 3 |
| [`src/components/ResumeLayout4.tsx`](src/components/ResumeLayout4.tsx) | Layout 4 |
| [`src/data/`](src/data/) | Eight resume JSON files |
| [`scripts/measure-pages.mjs`](scripts/measure-pages.mjs) | Page-fit checker (`npm run check:pages`) |
| [`scripts/export-pdfs.mjs`](scripts/export-pdfs.mjs) | Bulk PDF export |
| [`tech-resume-generator_files/user_professional_data/`](tech-resume-generator_files/user_professional_data/) | Source LinkedIn PDF snapshots |
| [`tech-resume-generator_files/output/`](tech-resume-generator_files/output/) | Exported PDFs + skill output |
| [`assets/resume_layouts/`](assets/resume_layouts/) | Sample layout references |
| [`@state/`](@state/) | Extracted data + writing guidelines |
| [`.agents/skills/tech-resume-generator/`](.agents/skills/tech-resume-generator/) | Installed [tech-resume-generator](https://github.com/baberarjumand/technical-resume-generator_agent-skill) skill |

## Scripts

| Command | Purpose |
| --- | --- |
| `npm run dev` | Local preview server |
| `npm run build` | Type-check and production build |
| `npm run lint` | Oxlint |
| `npm run check:pages` | Measure all eight variants; fail on overflow |
| `npm run export:pdfs` | Rebuild and write all eight PDFs to `tech-resume-generator_files/output/` |
| `npm run preview` | Serve the production build |
