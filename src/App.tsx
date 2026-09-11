import { useEffect, useState } from 'react'
import layout1OnePage from './data/resume-layout1-1page.json'
import layout1TwoPage from './data/resume-layout1-2page.json'
import layout2OnePage from './data/resume-layout2-1page.json'
import layout2TwoPage from './data/resume-layout2-2page.json'
import layout3OnePage from './data/resume-layout3-1page.json'
import layout3TwoPage from './data/resume-layout3-2page.json'
import layout4OnePage from './data/resume-layout4-1page.json'
import layout4TwoPage from './data/resume-layout4-2page.json'
import { Resume } from './components/Resume.tsx'
import { ResumeLayout2 } from './components/ResumeLayout2.tsx'
import { ResumeLayout3 } from './components/ResumeLayout3.tsx'
import { ResumeLayout4 } from './components/ResumeLayout4.tsx'
import type { ResumeData } from './types/resume.ts'
import './App.css'

type LayoutId = '1' | '2' | '3' | '4' | '5'
type PageCount = '1' | '2'
type Paper = 'a4' | 'letter'

const LAYOUTS: {
  id: LayoutId
  label: string
  pageCounts: PageCount[]
  paper: Paper
}[] = [
  { id: '1', label: 'Layout 1', pageCounts: ['1', '2'], paper: 'a4' },
  { id: '2', label: 'Layout 2', pageCounts: ['1', '2'], paper: 'letter' },
  { id: '3', label: 'Layout 3', pageCounts: ['1', '2'], paper: 'a4' },
  { id: '4', label: 'Layout 4', pageCounts: ['1', '2'], paper: 'letter' },
  { id: '5', label: 'Layout 5', pageCounts: ['1'], paper: 'letter' },
]

const PAGE_LABELS: Record<PageCount, string> = {
  '1': '1 page',
  '2': '2 pages',
}

const SKILL_PDF_HREF =
  '/tech-resume-generator_files/output/skill-general-1page.pdf'
const SKILL_PDF_NAME = 'skill-general-1page.pdf'

const resumes: Record<
  Exclude<LayoutId, '5'>,
  Record<PageCount, ResumeData>
> = {
  '1': {
    '1': layout1OnePage as ResumeData,
    '2': layout1TwoPage as ResumeData,
  },
  '2': {
    '1': layout2OnePage as ResumeData,
    '2': layout2TwoPage as ResumeData,
  },
  '3': {
    '1': layout3OnePage as ResumeData,
    '2': layout3TwoPage as ResumeData,
  },
  '4': {
    '1': layout4OnePage as ResumeData,
    '2': layout4TwoPage as ResumeData,
  },
}

type Selection = {
  layout: LayoutId
  pages: PageCount
}

function hashFor(layout: LayoutId, pages: PageCount): string {
  return `#layout${layout}-${pages}page`
}

function readSelectionFromHash(): Selection {
  const match = /^#layout([1-5])-([12])page$/.exec(window.location.hash)
  if (!match) return { layout: '1', pages: '1' }
  const layout = match[1] as LayoutId
  const pages = match[2] as PageCount
  if (layout === '5') return { layout: '5', pages: '1' }
  return { layout, pages }
}

function wantsLiveRender(): boolean {
  return (
    typeof window !== 'undefined' &&
    new URLSearchParams(window.location.search).has('render')
  )
}

function pdfFor(layout: LayoutId, pages: PageCount): { href: string; name: string } {
  if (layout === '5') {
    return { href: SKILL_PDF_HREF, name: SKILL_PDF_NAME }
  }
  const name = `layout${layout}-${pages}page.pdf`
  return {
    href: `/tech-resume-generator_files/output/${name}`,
    name,
  }
}

function App() {
  const [selection, setSelection] = useState<Selection>(() =>
    typeof window === 'undefined'
      ? { layout: '1', pages: '1' }
      : readSelectionFromHash(),
  )
  const [liveRender, setLiveRender] = useState(() => wantsLiveRender())

  useEffect(() => {
    const sync = () => {
      setSelection(readSelectionFromHash())
      setLiveRender(wantsLiveRender())
    }
    window.addEventListener('hashchange', sync)
    window.addEventListener('popstate', sync)
    return () => {
      window.removeEventListener('hashchange', sync)
      window.removeEventListener('popstate', sync)
    }
  }, [])

  const { layout, pages } = selection
  const meta = LAYOUTS.find((item) => item.id === layout)!
  const { href: pdfHref, name: pdfName } = pdfFor(layout, pages)
  const resume = layout === '5' ? null : resumes[layout][pages]

  return (
    <div className={`app app-layout-${layout}`}>
      <nav className="layout-nav no-print" aria-label="Resume versions">
        {LAYOUTS.map((item) => (
          <div className="layout-nav-group" key={item.id}>
            <span className="layout-nav-label">{item.label}</span>
            <div className="layout-nav-options">
              {item.pageCounts.map((option) => {
                const active = layout === item.id && pages === option
                return (
                  <a
                    key={option}
                    href={hashFor(item.id, option)}
                    aria-current={active ? 'page' : undefined}
                    className={
                      active
                        ? 'layout-nav-link layout-nav-link-active'
                        : 'layout-nav-link'
                    }
                  >
                    {PAGE_LABELS[option]}
                  </a>
                )
              })}
            </div>
          </div>
        ))}
      </nav>

      <main className={`preview preview-pages-${pages}`}>
        {liveRender && layout === '1' && resume ? <Resume data={resume} /> : null}
        {liveRender && layout === '2' && resume ? (
          <ResumeLayout2 data={resume} />
        ) : null}
        {liveRender && layout === '3' && resume ? (
          <ResumeLayout3 data={resume} />
        ) : null}
        {liveRender && layout === '4' && resume ? (
          <ResumeLayout4 data={resume} pages={pages === '1' ? 1 : 2} />
        ) : null}
        {!liveRender ? (
          <iframe
            key={pdfHref}
            className={`pdf-preview pdf-preview-${meta.paper} pdf-preview-pages-${pages}`}
            title={`${meta.label} — ${PAGE_LABELS[pages]} PDF`}
            src={pdfHref}
          />
        ) : null}
      </main>

      {liveRender ? null : (
        <div className="print-bar no-print">
          <a className="print-button" href={pdfHref} download={pdfName}>
            Download PDF
          </a>
        </div>
      )}
    </div>
  )
}

export default App
