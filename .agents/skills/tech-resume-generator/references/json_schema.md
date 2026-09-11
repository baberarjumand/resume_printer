# Resume JSON schema

Consumed by [`../scripts/generate_resume_pdf.mjs`](../scripts/generate_resume_pdf.mjs).

## Shape

```json
{
  "meta": {
    "title": "string — required",
    "author": "string — required",
    "subject": "string — required",
    "language": "string — optional, default en-US"
  },
  "header": {
    "name": "string",
    "headline": "string — short TIH-style headline, not a paragraph",
    "location": "string — city + country/region, no street",
    "phone": { "label": "visible number", "href": "tel:+..." },
    "email": { "label": "visible email", "href": "mailto:..." }
  },
  "links": [
    { "label": "visible text without https:// preferred", "href": "https://..." }
  ],
  "skills": [
    { "label": "Languages", "items": "comma-separated string" }
  ],
  "experience": [
    {
      "title": "string",
      "company": "string",
      "dates": "string",
      "place": "string",
      "extra": "optional progression line",
      "bullets": ["string", "..."]
    }
  ],
  "education": [
    {
      "degree": "string",
      "school": "string",
      "year": "string"
    }
  ]
}
```

## Rules

- `links` must be a non-empty array (portfolio, LinkedIn, GitHub, etc.).
- `skills` items are a single comma-separated string per category (typically 2–3 categories).
- Experience bullets should already be optimized (verb + tech + metric); the renderer only wraps text.
- No projects/certs/summary sections in the PDF renderer — put a tiny headline in `header.headline`; fold rare projects into experience or omit if the page is full.
- Example file: [`../assets/templates/resume_example.json`](../assets/templates/resume_example.json).

## Layout behavior

- US Letter, 612×792 pt, **36 pt (0.5") margins**, Helvetica
- Sections: **SKILLS → EXPERIENCE → EDUCATION**
- Links drawn in a top-right column beside the header
- Phone, email, and links get PDF URI annotations
- Script prints remaining space or warns on overflow (`y < margin`)
