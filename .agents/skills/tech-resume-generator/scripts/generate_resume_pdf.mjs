#!/usr/bin/env node
/**
 * Render a one-page Letter résumé PDF from a JSON file.
 *
 * Usage:
 *   node scripts/generate_resume_pdf.mjs <path-to-resume.json>
 *   npm run generate-resume -- <path-to-resume.json>
 *
 * Requires pdf-lib. From this skill directory: npm install
 * (works after npx skills install — no monorepo root required).
 *
 * The PDF is written next to the JSON, with the same basename and a .pdf extension.
 *
 * JSON shape:
 *   meta: { title, author, subject, language? }
 *   header: { name, headline, location, phone: {label, href}, email: {label, href} }
 *   links: [{ label, href }]   // top-right column; one URL per line
 *   skills: [{ label, items }]
 *   experience: [{ title, company, dates, place, extra?, bullets[] }]
 *   education: [{ degree, school, year }]
 */
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { dirname, extname, isAbsolute, resolve } from 'node:path'
import { pathToFileURL } from 'node:url'
import { PDFDocument, PDFString, StandardFonts, rgb } from 'pdf-lib'

const PAGE_W = 612
const PAGE_H = 792
const MARGIN = 36
const CONTENT_W = PAGE_W - MARGIN * 2
const BLACK = rgb(0, 0, 0)
const RULE = rgb(0.15, 0.15, 0.15)

function wrap(text, font, size, width) {
  const words = text.split(/\s+/)
  const lines = []
  let current = ''
  for (const word of words) {
    const next = current ? `${current} ${word}` : word
    if (current && font.widthOfTextAtSize(next, size) > width) {
      lines.push(current)
      current = word
    } else {
      current = next
    }
  }
  if (current) lines.push(current)
  return lines
}

function addUriLink(page, x, y, w, h, uri) {
  const annot = page.doc.context.obj({
    Type: 'Annot',
    Subtype: 'Link',
    Rect: [x, y, x + w, y + h],
    Border: [0, 0, 0],
    A: {
      Type: 'Action',
      S: 'URI',
      URI: PDFString.of(uri),
      NewWindow: true,
    },
  })
  page.node.addAnnot(page.doc.context.register(annot))
}

function requireFields(obj, fields, ctx) {
  for (const field of fields) {
    if (obj == null || obj[field] == null || obj[field] === '') {
      throw new Error(`Resume JSON missing ${ctx}.${field}`)
    }
  }
}

function loadResume(jsonPath) {
  const data = JSON.parse(readFileSync(jsonPath, 'utf8'))
  requireFields(data, ['meta', 'header', 'links', 'skills', 'experience', 'education'], 'root')
  requireFields(data.meta, ['title', 'author', 'subject'], 'meta')
  requireFields(data.header, ['name', 'headline', 'location', 'phone', 'email'], 'header')
  requireFields(data.header.phone, ['label', 'href'], 'header.phone')
  requireFields(data.header.email, ['label', 'href'], 'header.email')
  if (!Array.isArray(data.links) || data.links.length === 0) {
    throw new Error('Resume JSON needs a non-empty links array')
  }
  if (!Array.isArray(data.experience) || !Array.isArray(data.education)) {
    throw new Error('Resume JSON needs experience and education arrays')
  }
  return data
}

export async function generateResumePdf(jsonPath) {
  const absJson = isAbsolute(jsonPath) ? jsonPath : resolve(process.cwd(), jsonPath)
  if (extname(absJson).toLowerCase() !== '.json') {
    throw new Error(`Expected a .json file, got: ${jsonPath}`)
  }

  const data = loadResume(absJson)
  const outPath = absJson.slice(0, -'.json'.length) + '.pdf'

  const pdf = await PDFDocument.create()
  pdf.setTitle(data.meta.title)
  pdf.setAuthor(data.meta.author)
  pdf.setSubject(data.meta.subject)
  pdf.setCreator('tech-resume-generator')
  pdf.setLanguage(data.meta.language || 'en-US')

  const font = await pdf.embedFont(StandardFonts.Helvetica)
  const bold = await pdf.embedFont(StandardFonts.HelveticaBold)
  const page = pdf.addPage([PAGE_W, PAGE_H])

  let y = PAGE_H - MARGIN
  const left = MARGIN

  const draw = (text, x, baseline, size, face = font) => {
    page.drawText(text, { x, y: baseline, size, font: face, color: BLACK })
    return face.widthOfTextAtSize(text, size)
  }

  const linked = (label, uri, x, baseline, size, face = font) => {
    const w = face.widthOfTextAtSize(label, size)
    draw(label, x, baseline, size, face)
    addUriLink(page, x, baseline - 2, w, size + 3, uri)
    return w
  }

  const nameSize = 16
  const headlineSize = 10
  const contactSize = 9
  const linkSize = 9
  const nameLead = 16
  const headlineLead = 14
  const contactLead = 13

  y -= nameLead
  const nameBaseline = y
  draw(data.header.name, left, nameBaseline, nameSize, bold)
  const nameAscent = bold.heightAtSize(nameSize, { descender: false })
  const headerTop = nameBaseline + nameAscent

  y -= headlineLead
  const headlineBaseline = y
  draw(data.header.headline, left, headlineBaseline, headlineSize, font)

  y -= contactLead
  const contactBaseline = y
  let x = left
  x += draw(data.header.location, x, contactBaseline, contactSize)
  x += draw('  |  ', x, contactBaseline, contactSize)
  x += linked(
    data.header.phone.label,
    data.header.phone.href,
    x,
    contactBaseline,
    contactSize,
  )
  x += draw('  |  ', x, contactBaseline, contactSize)
  linked(
    data.header.email.label,
    data.header.email.href,
    x,
    contactBaseline,
    contactSize,
  )

  const contactHeight = font.heightAtSize(contactSize)
  const contactAscent = font.heightAtSize(contactSize, { descender: false })
  const headerBottom = contactBaseline - (contactHeight - contactAscent)
  const headerHeight = headerTop - headerBottom

  const linkColW = Math.max(
    ...data.links.map((item) => font.widthOfTextAtSize(item.label, linkSize)),
  )
  const linkX = left + CONTENT_W - linkColW
  const slotH = headerHeight / data.links.length
  const linkAscent = font.heightAtSize(linkSize, { descender: false })
  const linkHeight = font.heightAtSize(linkSize)
  const linkDescent = linkHeight - linkAscent

  for (let i = 0; i < data.links.length; i++) {
    const slotBottom = headerTop - (i + 1) * slotH
    const baseline = slotBottom + (slotH - linkHeight) / 2 + linkDescent
    const item = data.links[i]
    linked(item.label, item.href, linkX, baseline, linkSize)
  }

  const section = (title) => {
    y -= 20
    draw(title, left, y, 10.5, bold)
    y -= 4
    page.drawLine({
      start: { x: left, y },
      end: { x: left + CONTENT_W, y },
      thickness: 0.7,
      color: RULE,
    })
    y -= 12
  }

  y = contactBaseline
  section('SKILLS')
  for (const skill of data.skills) {
    let sx = left
    sx += draw(`${skill.label}: `, sx, y, 9.5, bold)
    draw(skill.items, sx, y, 9.5, font)
    y -= 12
  }

  section('EXPERIENCE')

  const titleSize = 10
  const metaSize = 8.5
  const bulletSize = 10
  const bulletGap = 12

  for (const job of data.experience) {
    requireFields(job, ['title', 'company', 'dates', 'place', 'bullets'], 'experience[]')
    const leftText = `${job.title}, ${job.company}`
    const dateW = font.widthOfTextAtSize(job.dates, titleSize)
    draw(leftText, left, y, titleSize, bold)
    draw(job.dates, left + CONTENT_W - dateW, y, titleSize, font)
    y -= 11
    draw(job.place, left, y, metaSize, font)
    y -= 11
    if (job.extra) {
      draw(job.extra, left, y, metaSize, font)
      y -= 11
    }
    for (const bullet of job.bullets) {
      const mark = '-  '
      const markW = font.widthOfTextAtSize(mark, bulletSize)
      const lines = wrap(bullet, font, bulletSize, CONTENT_W - markW)
      for (let i = 0; i < lines.length; i++) {
        if (i === 0) draw(mark, left, y, bulletSize)
        draw(lines[i], left + markW, y, bulletSize)
        y -= bulletGap
      }
    }
    y -= 6
  }

  section('EDUCATION')
  for (const edu of data.education) {
    requireFields(edu, ['degree', 'school', 'year'], 'education[]')
    const eduRightW = font.widthOfTextAtSize(edu.year, 10)
    draw(edu.degree, left, y, 10, bold)
    draw(edu.year, left + CONTENT_W - eduRightW, y, 10, font)
    y -= 12
    draw(edu.school, left, y, 9.5, font)
    y -= 12
  }

  if (y < MARGIN) {
    console.warn(`Layout overflow: y=${y.toFixed(1)} (margin ${MARGIN})`)
  } else {
    console.log(`Remaining space below education: ${(y - MARGIN).toFixed(1)} pt`)
  }

  const bytes = await pdf.save()
  mkdirSync(dirname(outPath), { recursive: true })
  writeFileSync(outPath, bytes)
  console.log(`Wrote ${outPath} (${bytes.length} bytes)`)
  return outPath
}

const isDirectRun =
  process.argv[1] &&
  import.meta.url === pathToFileURL(process.argv[1]).href

if (isDirectRun) {
  const jsonArg = process.argv[2]
  if (!jsonArg || jsonArg === '--help' || jsonArg === '-h') {
    console.log(`Usage: node scripts/generate_resume_pdf.mjs <path-to-resume.json>

Render a one-page Letter résumé PDF next to the JSON (same basename).

Requires: Node.js 18+, pdf-lib.
Install deps from the skill directory (works after npx skills add):
  cd /path/to/tech-resume-generator && npm install

Examples:
  node scripts/generate_resume_pdf.mjs ../../tech-resume-generator_files/output/general/jane_doe_resume.json
  npm run generate-resume -- ../../tech-resume-generator_files/output/general/jane_doe_resume.json

Exit codes: 0 success, 1 missing/invalid args or validation failure.
Writes overflow warnings if content exceeds the page.`)
    process.exit(jsonArg ? 0 : 1)
  }
  try {
    await generateResumePdf(jsonArg)
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err)
    if (/Cannot find package ['"]pdf-lib['"]|Cannot find module ['"]pdf-lib['"]/i.test(msg)) {
      console.error(
        'Error: pdf-lib is not installed.\n' +
          'From the skill directory run: npm install\n' +
          `(skill package.json declares pdf-lib). Original: ${msg}`,
      )
    } else {
      console.error(`Error: ${msg}`)
    }
    process.exit(1)
  }
}
