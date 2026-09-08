import type { AdditionalItem, ExperienceItem, ResumeData, ResumeLinks } from '../types/resume.ts'
import {
  formatDateRange,
  formatEducationYears,
  formatYearRange,
} from '../lib/dates.ts'
import { renderRichText } from '../lib/richText.tsx'
import './resume.css'

type ResumeProps = {
  data: ResumeData
}

function displayUrl(url: string): string {
  return url
    .replace(/^https?:\/\//i, '')
    .replace(/^www\./i, '')
    .replace(/\/$/, '')
}

function contactLinks(links: ResumeLinks): { href: string; label: string }[] {
  const items: { href: string; label: string }[] = [
    { href: `mailto:${links.email}`, label: links.email },
  ]
  if (links.website) {
    items.push({ href: links.website, label: displayUrl(links.website) })
  }
  items.push({ href: links.linkedin, label: displayUrl(links.linkedin) })
  if (links.github) {
    items.push({ href: links.github, label: displayUrl(links.github) })
  }
  return items
}

function ExternalLink({
  href,
  className,
  children,
}: {
  href: string
  className?: string
  children: string
}) {
  return (
    <a
      className={className}
      href={href}
      target="_blank"
      rel="noopener noreferrer"
    >
      {children}
    </a>
  )
}

function SectionHeading({
  label,
  subtitle,
}: {
  label: string
  subtitle?: string
}) {
  return (
    <h2 className="section-heading">
      <span className="section-heading-label">{label}</span>
      {subtitle ? (
        <>
          {' '}
          <span className="section-heading-paren">(</span>
          <span className="section-heading-subtitle">{subtitle}</span>
          <span className="section-heading-paren">)</span>
        </>
      ) : null}
    </h2>
  )
}

function BulletList({ items }: { items: string[] }) {
  return (
    <ul className="resume-bullets">
      {items.map((item, index) => (
        <li key={index}>{renderRichText(item)}</li>
      ))}
    </ul>
  )
}

function ExperienceEntry({ item }: { item: ExperienceItem }) {
  const company = item.companyWebsite ? (
    <ExternalLink className="job-company" href={item.companyWebsite}>
      {item.company}
    </ExternalLink>
  ) : (
    <span className="job-company">{item.company}</span>
  )

  const location = item.workMode
    ? `${item.location} (${item.workMode})`
    : item.location

  return (
    <article className="job-item">
      <div className="entry-heading">
        <p className="entry-heading-main">
          <span className="job-role">{item.role}</span>
          <span className="entry-sep"> | </span>
          {company}
          <span className="entry-sep"> | </span>
          <span className="job-location">{location}</span>
        </p>
        <p className="job-dates">
          {formatDateRange(item.startDate, item.endDate)}
        </p>
      </div>
      <BulletList items={item.bullets} />
    </article>
  )
}

function AdditionalEntry({ item }: { item: AdditionalItem }) {
  return (
    <article className="additional-item">
      <p className="additional-heading">
        {item.role}
        <span className="entry-sep"> | </span>
        {item.organization}
        {item.location ? (
          <>
            <span className="entry-sep"> | </span>
            {item.location}
          </>
        ) : null}{' '}
        ({formatYearRange(item.startYear, item.endYear)})
      </p>
      <BulletList items={item.bullets} />
    </article>
  )
}

export function Resume({ data }: ResumeProps) {
  const links = contactLinks(data.links)

  return (
    <article className="resume-sheet">
      <header className="resume-header">
        <h1 className="resume-name">{data.name}</h1>
        <p className="resume-headline">{data.headline}</p>
        <p className="resume-links">
          {links.map((link, index) => (
            <span key={link.href}>
              {index > 0 ? <span className="entry-sep"> | </span> : null}
              <ExternalLink className="contact-link" href={link.href}>
                {link.label}
              </ExternalLink>
            </span>
          ))}
        </p>
      </header>

      <section className="resume-section">
        <SectionHeading label={data.summary.label} />
        <p className="summary-text">{renderRichText(data.summary.text)}</p>
      </section>

      <section className="resume-section">
        <SectionHeading label={data.experience.label} />
        <div className="experience-list">
          {data.experience.items.map((item) => (
            <ExperienceEntry
              key={`${item.role}-${item.company}-${item.startDate.year}-${item.startDate.month}`}
              item={item}
            />
          ))}
        </div>
      </section>

      <section className="resume-section">
        <SectionHeading label={data.skills.label} />
        {data.skills.items.map((item) => (
          <p className="skill-row" key={item.name}>
            <strong>{item.name}</strong>
            {`: ${item.skills.join(', ')}.`}
          </p>
        ))}
      </section>

      <section className="resume-section">
        <SectionHeading label={data.education.label} />
        {data.education.items.map((item) => (
          <article
            className="edu-item"
            key={`${item.qualificationName}-${item.endYear}`}
          >
            <div className="entry-heading">
              <p className="entry-heading-main">
                <span className="edu-name">
                  {item.qualificationName} in {item.qualificationField}
                </span>
                {item.note ? (
                  <span className="edu-note"> ({item.note})</span>
                ) : null}
              </p>
              <p className="edu-dates">
                {formatEducationYears(item.startYear, item.endYear)}
              </p>
            </div>
            <p className="edu-institute">
              {item.instituteName}, {item.instituteLocation}
            </p>
          </article>
        ))}
      </section>

      {data.additional.items.length > 0 ? (
        <section className="resume-section">
          <SectionHeading
            label={data.additional.label}
            subtitle={data.additional.subtitle}
          />
          {data.additional.items.map((item) => (
            <AdditionalEntry
              key={`${item.role}-${item.organization}-${item.startYear}`}
              item={item}
            />
          ))}
        </section>
      ) : null}

      {data.footer ? (
        <footer className="resume-footer">
          <p>
            {data.footer.text}{' '}
            <ExternalLink className="footer-link" href={data.footer.link.href}>
              {data.footer.link.label}
            </ExternalLink>
          </p>
        </footer>
      ) : null}
    </article>
  )
}
