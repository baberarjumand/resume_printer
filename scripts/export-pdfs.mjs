import { createServer } from 'node:http'
import { createReadStream } from 'node:fs'
import { mkdir, stat, writeFile } from 'node:fs/promises'
import { extname, join, normalize } from 'node:path'
import { fileURLToPath } from 'node:url'
import { chromium } from 'playwright'

const root = fileURLToPath(
  new URL('../node_modules/.cache/resume-pages', import.meta.url),
)
const outDir = fileURLToPath(
  new URL('../tech-resume-generator_files/output', import.meta.url),
)

const MIME = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.svg': 'image/svg+xml',
}

const VARIANTS = [
  { layout: '1', pages: '1', format: 'A4', file: 'layout1-1page.pdf' },
  { layout: '1', pages: '2', format: 'A4', file: 'layout1-2page.pdf' },
  { layout: '2', pages: '1', format: 'Letter', file: 'layout2-1page.pdf' },
  { layout: '2', pages: '2', format: 'Letter', file: 'layout2-2page.pdf' },
  { layout: '3', pages: '1', format: 'A4', file: 'layout3-1page.pdf' },
  { layout: '3', pages: '2', format: 'A4', file: 'layout3-2page.pdf' },
  { layout: '4', pages: '1', format: 'Letter', file: 'layout4-1page.pdf' },
  { layout: '4', pages: '2', format: 'Letter', file: 'layout4-2page.pdf' },
]

const SHEETS = {
  1: '.resume-sheet',
  2: '.layout2-sheet',
  3: '.layout3-sheet',
  4: '.layout4-sheet',
}

await mkdir(outDir, { recursive: true })

const server = createServer(async (request, response) => {
  const path = join(root, normalize(new URL(request.url, 'http://x').pathname))
  const file = (await stat(path).catch(() => null))?.isFile()
    ? path
    : join(root, 'index.html')
  response.writeHead(200, {
    'content-type': MIME[extname(file)] ?? 'application/octet-stream',
  })
  createReadStream(file).pipe(response)
})

await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve))
const base = `http://127.0.0.1:${server.address().port}/index.html`

const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: 1400, height: 1200 } })

for (const variant of VARIANTS) {
  await page.goto(`${base}?render=1#layout${variant.layout}-${variant.pages}page`, {
    waitUntil: 'networkidle',
  })
  await page.waitForSelector(SHEETS[variant.layout])
  await page.evaluate(() => document.fonts.ready)

  const outPath = join(outDir, variant.file)
  const buffer = await page.pdf({
    format: variant.format,
    printBackground: true,
    preferCSSPageSize: false,
    margin: { top: '0', right: '0', bottom: '0', left: '0' },
  })

  // Count pages via PDF page markers.
  const pageCount = (buffer.toString('latin1').match(/\/Type\s*\/Page[^s]/g) ?? [])
    .length
  const expected = Number(variant.pages)
  if (pageCount !== expected) {
    throw new Error(
      `${variant.file}: expected ${expected} page(s), got ${pageCount}`,
    )
  }

  await writeFile(outPath, buffer)
  console.log(`wrote ${variant.file} (${pageCount} page${pageCount === 1 ? '' : 's'})`)
}

await browser.close()
server.close()
