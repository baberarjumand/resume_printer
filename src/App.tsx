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

type LayoutId = '1' | '2' | '3' | '4'
type PageCount = '1' | '2'

const LAYOUTS: { id: LayoutId; label: string }[] = [
  { id: '1', label: 'Layout 1' },
  { id: '2', label: 'Layout 2' },
  { id: '3', label: 'Layout 3' },
  { id: '4', label: 'Layout 4' },
]

const PAGE_COUNTS: { id: PageCount; label: string }[] = [
  { id: '1', label: '1 page' },
  { id: '2', label: '2 pages' },
]

const resumes: Record<LayoutId, Record<PageCount, ResumeData>> = {
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
  const match = /^#layout([1234])-([12])page$/.exec(window.location.hash)
  if (!match) return { layout: '1', pages: '1' }
  return { layout: match[1] as LayoutId, pages: match[2] as PageCount }
}

function App() {
  const [selection, setSelection] = useState<Selection>(() =>
    typeof window === 'undefined'
      ? { layout: '1', pages: '1' }
      : readSelectionFromHash(),
  )

  useEffect(() => {
    const sync = () => setSelection(readSelectionFromHash())
    window.addEventListener('hashchange', sync)
    window.addEventListener('popstate', sync)
    return () => {
      window.removeEventListener('hashchange', sync)
      window.removeEventListener('popstate', sync)
    }
  }, [])

  const { layout, pages } = selection
  const resume = resumes[layout][pages]

  return (
    <div className={`app app-layout-${layout}`}>
      <nav className="layout-nav no-print" aria-label="Resume versions">
        {LAYOUTS.map((item) => (
          <div className="layout-nav-group" key={item.id}>
            <span className="layout-nav-label">{item.label}</span>
            <div className="layout-nav-options">
              {PAGE_COUNTS.map((option) => {
                const active = layout === item.id && pages === option.id
                return (
                  <a
                    key={option.id}
                    href={hashFor(item.id, option.id)}
                    aria-current={active ? 'page' : undefined}
                    className={
                      active
                        ? 'layout-nav-link layout-nav-link-active'
                        : 'layout-nav-link'
                    }
                  >
                    {option.label}
                  </a>
                )
              })}
            </div>
          </div>
        ))}
      </nav>

      <main className={`preview preview-pages-${pages}`}>
        {layout === '1' ? <Resume data={resume} /> : null}
        {layout === '2' ? <ResumeLayout2 data={resume} /> : null}
        {layout === '3' ? <ResumeLayout3 data={resume} /> : null}
        {layout === '4' ? (
          <ResumeLayout4 data={resume} pages={pages === '1' ? 1 : 2} />
        ) : null}
      </main>

      <div className="print-bar no-print">
        <button
          type="button"
          className="print-button"
          onClick={() => window.print()}
        >
          Print
        </button>
      </div>
    </div>
  )
}

export default App
