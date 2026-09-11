// Reports how tall each resume variant renders, in pages.
// Run via `npm run check:pages`, which builds `dist-measure/` first.
import { createServer } from 'node:http'
import { createReadStream } from 'node:fs'
import { stat } from 'node:fs/promises'
import { extname, join, normalize } from 'node:path'
import { fileURLToPath } from 'node:url'
import { chromium } from 'playwright'

// Built inside node_modules so the dev server's watcher ignores it; writing to
// the project root makes Vite full-reload any open preview tab.
const root = fileURLToPath(
  new URL('../node_modules/.cache/resume-pages', import.meta.url),
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

const SHEETS = {
  1: { selector: '.resume-sheet', pageHeightPx: (297 / 25.4) * 96 },
  2: { selector: '.layout2-sheet', pageHeightPx: 11 * 96 },
  3: { selector: '.layout3-sheet', pageHeightPx: (297 / 25.4) * 96 },
  4: { selector: '.layout4-sheet', pageHeightPx: 11 * 96 },
}

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
let overflowed = false

for (const layout of Object.keys(SHEETS)) {
  for (const pages of ['1', '2']) {
    await page.goto(`${base}?render=1#layout${layout}-${pages}page`, {
      waitUntil: 'networkidle',
    })

    const { selector, pageHeightPx } = SHEETS[layout]
    await page.waitForSelector(selector)
    await page.evaluate(() => document.fonts.ready)

    // min-height pins the sheet to its target size, so drop it to read the
    // height the content actually needs.
    const heightPx = await page.evaluate((sel) => {
      const sheet = document.querySelector(sel)
      const previous = sheet.style.minHeight
      sheet.style.minHeight = '0px'
      const height = sheet.getBoundingClientRect().height
      sheet.style.minHeight = previous
      return height
    }, selector)

    const used = heightPx / pageHeightPx
    const fits = used <= Number(pages)
    if (!fits) overflowed = true
    console.log(
      `layout ${layout} / ${pages}-page: ${used.toFixed(2)} pages  ` +
        (fits ? 'fits' : `OVER by ${(used - Number(pages)).toFixed(2)}`),
    )
  }
}

await browser.close()
server.close()
process.exitCode = overflowed ? 1 : 0
