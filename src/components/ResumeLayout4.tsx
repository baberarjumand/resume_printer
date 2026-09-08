import type { ResumeData } from '../types/resume.ts'
import { formatDateRangeLong, formatYearRange } from '../lib/dates.ts'
import { renderRichText } from '../lib/richText.tsx'
import './resumeLayout4.css'

type Props = {
  data: ResumeData
  pages: 1 | 2
}

function displayUrl(url: string): string {
  return url
    .replace(/^https?:\/\//i, '')
    .replace(/^www\./i, '')
    .replace(/\/$/, '')
}

function SectionTitle({ children }: { children: string }) {
  return <h2 className="layout4-section-title">{children}</h2>
}

/** Harvard row: the identifying detail on the left, place or date on the right. */
function EntryRow({
  primary,
  secondary,
  strong,
}: {
  primary: string
  secondary: string
  strong?: boolean
}) {
  return (
    <p className={strong ? 'layout4-row layout4-row-strong' : 'layout4-row'}>
      <span className="layout4-row-left">{primary}</span>
      <span className="layout4-row-right">{secondary}</span>
    </p>
  )
}

export function ResumeLayout4({ data, pages }: Props) {
  const { links } = data
  // Split rather than wrapped, so the second line never strands a single URL.
  const contact = [data.location, links.phone, links.email].filter(
    (entry): entry is string => Boolean(entry),
  )
  const profiles = [
    links.website ? displayUrl(links.website) : undefined,
    displayUrl(links.linkedin),
    links.github ? displayUrl(links.github) : undefined,
  ].filter((entry): entry is string => Boolean(entry))

  const projects = data.projects?.items ?? []
  const certifications = data.certifications?.items ?? []
  const languages = data.languages ?? []

  return (
    <article className="layout4-sheet">
      <header className="layout4-header">
        <h1 className="layout4-name">{data.name}</h1>
        <p className="layout4-contact">{contact.join(' · ')}</p>
        <p className="layout4-contact">{profiles.join(' · ')}</p>
        {data.availability ? (
          <p className="layout4-availability">{data.availability}</p>
        ) : null}
      </header>

      <section>
        <SectionTitle>
          {data.highlights?.label ?? data.summary.label}
        </SectionTitle>
        {data.highlights && data.highlights.items.length > 0 ? (
          <ul className="layout4-bullets">
            {data.highlights.items.map((item, index) => (
              <li key={index}>{renderRichText(item)}</li>
            ))}
          </ul>
        ) : (
          <p>{renderRichText(data.summary.text)}</p>
        )}
      </section>

      <section>
        <SectionTitle>{data.skills.label}</SectionTitle>
        {data.skills.items.map((group) => (
          <p className="layout4-skill-row" key={group.name}>
            <span className="layout4-skill-name">{group.name}:</span>{' '}
            {group.skills.join(', ')}
          </p>
        ))}
      </section>

      <section>
        <SectionTitle>{data.experience.label}</SectionTitle>
        {data.experience.items.map((item) => (
          <article
            className="layout4-entry"
            key={`${item.role}-${item.company}-${item.startDate.year}-${item.startDate.month}`}
          >
            <EntryRow
              strong
              primary={item.company}
              secondary={`${item.location}${item.workMode ? ` (${item.workMode})` : ''}`}
            />
            <EntryRow
              primary={item.role}
              secondary={formatDateRangeLong(item.startDate, item.endDate)}
            />
            {item.companyNote ? (
              <p className="layout4-note">{item.companyNote}</p>
            ) : null}
            <ul className="layout4-bullets">
              {item.bullets.map((bullet, index) => (
                <li key={index}>{renderRichText(bullet)}</li>
              ))}
            </ul>
            {item.tech && item.tech.length > 0 ? (
              <p className="layout4-tech">
                <span className="layout4-skill-name">Technology:</span>{' '}
                {item.tech.join(', ')}
              </p>
            ) : null}
          </article>
        ))}
      </section>

      {projects.length > 0 ? (
        <section>
          <SectionTitle>{data.projects?.label ?? 'Projects'}</SectionTitle>
          {projects.map((project) => (
            <article className="layout4-entry" key={project.name}>
              <EntryRow
                strong
                primary={project.name}
                secondary={
                  project.startYear
                    ? formatYearRange(
                        project.startYear,
                        project.endYear ?? project.startYear,
                      )
                    : ''
                }
              />
              <ul className="layout4-bullets">
                <li>{project.description}</li>
              </ul>
              {project.tech && project.tech.length > 0 ? (
                <p className="layout4-tech">
                  <span className="layout4-skill-name">Technology:</span>{' '}
                  {project.tech.join(', ')}
                </p>
              ) : null}
            </article>
          ))}
        </section>
      ) : null}

      <section>
        <SectionTitle>{data.education.label}</SectionTitle>
        {data.education.items.map((item) => (
          <article
            className="layout4-entry"
            key={`${item.instituteName}-${item.endYear}`}
          >
            <EntryRow
              strong
              primary={item.instituteName}
              secondary={item.instituteLocation}
            />
            <EntryRow
              primary={`${item.qualificationName}, ${item.qualificationField}${
                item.note ? ` (${item.note})` : ''
              }`}
              secondary={formatYearRange(item.startYear, item.endYear)}
            />
          </article>
        ))}
      </section>

      {certifications.length > 0 ? (
        <section>
          <SectionTitle>
            {data.certifications?.label ?? 'Certifications'}
          </SectionTitle>
          <p className="layout4-skill-row">
            {certifications
              .map(
                (cert) =>
                  `${cert.name} (${cert.issuer}${cert.year ? `, ${cert.year}` : ''})`,
              )
              .join('; ')}
          </p>
        </section>
      ) : null}

      {data.additional.items.length > 0 ? (
        <section>
          <SectionTitle>{data.additional.label}</SectionTitle>
          {data.additional.items.map((item) => (
            <article
              className="layout4-entry"
              key={`${item.role}-${item.organization}-${item.startYear}`}
            >
              <EntryRow
                strong
                primary={item.organization}
                secondary={item.location ?? ''}
              />
              <EntryRow
                primary={item.role}
                secondary={formatYearRange(item.startYear, item.endYear)}
              />
              {item.bullets.length > 0 ? (
                <ul className="layout4-bullets">
                  {item.bullets.map((bullet, index) => (
                    <li key={index}>{renderRichText(bullet)}</li>
                  ))}
                </ul>
              ) : null}
            </article>
          ))}
        </section>
      ) : null}

      {languages.length > 0 || data.interests?.length ? (
        <section>
          <SectionTitle>Additional Information</SectionTitle>
          {languages.length > 0 ? (
            <p className="layout4-skill-row">
              <span className="layout4-skill-name">Languages:</span>{' '}
              {languages
                .map((language) => `${language.name} (${language.proficiency})`)
                .join(', ')}
            </p>
          ) : null}
          {data.interests && data.interests.length > 0 ? (
            <p className="layout4-skill-row">
              <span className="layout4-skill-name">Interests:</span>{' '}
              {data.interests.join(', ')}
            </p>
          ) : null}
        </section>
      ) : null}

      {pages === 2 ? (
        <p className="layout4-page-label">{data.name} — Resume, page 2 of 2</p>
      ) : null}
    </article>
  )
}
