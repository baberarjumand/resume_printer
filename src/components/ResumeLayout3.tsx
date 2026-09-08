import type { ResumeData } from '../types/resume.ts'
import { formatDateRangeLong, formatEducationYears } from '../lib/dates.ts'
import { renderRichText } from '../lib/richText.tsx'
import './resumeLayout3.css'

type Props = {
  data: ResumeData
}

function displayUrl(url: string): string {
  return url
    .replace(/^https?:\/\//i, '')
    .replace(/^www\./i, '')
    .replace(/\/$/, '')
}

export function ResumeLayout3({ data }: Props) {
  const projects = data.projects?.items ?? []
  const certifications = data.certifications?.items ?? []
  const languages = data.languages ?? []

  return (
    <article className="layout3-sheet">
      <header className="layout3-banner">
        <h1 className="layout3-name">{data.name}</h1>
        <p className="layout3-tagline">{data.tagline ?? data.headline}</p>
      </header>

      <div className="layout3-body">
        <aside className="layout3-sidebar">
          <section>
            <h2 className="layout3-side-title">Contact</h2>
            <ul className="layout3-contact">
              <li>
                <a href={`mailto:${data.links.email}`}>{data.links.email}</a>
              </li>
              {data.location ? <li>{data.location}</li> : null}
              {data.links.website ? (
                <li>
                  <a
                    href={data.links.website}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {displayUrl(data.links.website)}
                  </a>
                </li>
              ) : null}
              {data.links.github ? (
                <li>
                  <a
                    href={data.links.github}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {displayUrl(data.links.github)}
                  </a>
                </li>
              ) : null}
              <li>
                <a
                  href={data.links.linkedin}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {displayUrl(data.links.linkedin)}
                </a>
              </li>
            </ul>
          </section>

          <section>
            <h2 className="layout3-side-title">{data.skills.label}</h2>
            <div className="layout3-skill-list">
              {data.skills.items.map((group) => (
                <div className="layout3-skill-group" key={group.name}>
                  <h3 className="layout3-skill-name">{group.name}</h3>
                  <p className="layout3-skill-values">
                    {group.skills.join(', ')}
                  </p>
                </div>
              ))}
            </div>
          </section>

          {languages.length > 0 ? (
            <section>
              <h2 className="layout3-side-title">Languages</h2>
              <ul className="layout3-highlights">
                {languages.map((language) => (
                  <li key={language.name}>
                    <strong>{language.name}</strong>
                    <span> ({language.proficiency})</span>
                  </li>
                ))}
              </ul>
            </section>
          ) : null}

          {certifications.length > 0 ? (
            <section>
              <h2 className="layout3-side-title">
                {data.certifications?.label ?? 'Certifications'}
              </h2>
              <ul className="layout3-highlights">
                {certifications.map((cert) => (
                  <li key={cert.name}>
                    <strong>{cert.name}</strong>
                    <span>
                      {' '}
                      ({cert.issuer}
                      {cert.year ? `, ${cert.year}` : ''})
                    </span>
                  </li>
                ))}
              </ul>
            </section>
          ) : null}
        </aside>

        <div className="layout3-main">
          <section>
            <h2 className="layout3-main-title">{data.summary.label}</h2>
            <p className="layout3-entry-copy">
              {renderRichText(data.summary.text)}
            </p>
          </section>

          <section>
            <h2 className="layout3-main-title">{data.experience.label}</h2>
            {data.experience.items.map((item) => (
              <article
                className="layout3-entry"
                key={`${item.role}-${item.company}-${item.startDate.year}-${item.startDate.month}`}
              >
                <div className="layout3-entry-head">
                  <div>
                    <p className="layout3-entry-org">{item.company}</p>
                    <p className="layout3-entry-role">{item.role}</p>
                  </div>
                  <p className="layout3-entry-dates">
                    {formatDateRangeLong(item.startDate, item.endDate)}
                  </p>
                </div>
                <p className="layout3-entry-meta">
                  {item.location}
                  {item.workMode ? ` · ${item.workMode}` : ''}
                </p>
                <ul className="layout3-bullets">
                  {item.bullets.map((bullet, index) => (
                    <li key={index}>{renderRichText(bullet)}</li>
                  ))}
                </ul>
              </article>
            ))}
          </section>

          <section>
            <h2 className="layout3-main-title">{data.education.label}</h2>
            {data.education.items.map((item) => (
              <article
                className="layout3-entry"
                key={`${item.instituteName}-${item.endYear}`}
              >
                <div className="layout3-entry-head">
                  <div>
                    <p className="layout3-entry-org">{item.instituteName}</p>
                    <p className="layout3-entry-role">
                      {item.qualificationName} in {item.qualificationField}
                      {item.note ? ` (${item.note})` : ''}
                    </p>
                  </div>
                  <p className="layout3-entry-dates">
                    {formatEducationYears(item.startYear, item.endYear)}
                  </p>
                </div>
                <p className="layout3-entry-meta">{item.instituteLocation}</p>
              </article>
            ))}
          </section>

          {projects.length > 0 ? (
            <section>
              <h2 className="layout3-main-title">
                {data.projects?.label ?? 'Projects'}
              </h2>
              {projects.map((project) => (
                <article className="layout3-entry" key={project.name}>
                  <div className="layout3-entry-head">
                    <p className="layout3-entry-org">
                      {project.url ? (
                        <a
                          href={project.url}
                          target="_blank"
                          rel="noopener noreferrer"
                        >
                          {project.name}
                        </a>
                      ) : (
                        project.name
                      )}
                    </p>
                    {project.startYear ? (
                      <p className="layout3-entry-dates">
                        {project.endYear &&
                        project.endYear !== project.startYear
                          ? `${project.startYear} – ${project.endYear}`
                          : project.startYear}
                      </p>
                    ) : null}
                  </div>
                  {project.tech && project.tech.length > 0 ? (
                    <p className="layout3-tech">{project.tech.join(' · ')}</p>
                  ) : null}
                  <p className="layout3-entry-copy">{project.description}</p>
                </article>
              ))}
            </section>
          ) : null}

          {data.additional.items.length > 0 ? (
            <section>
              <h2 className="layout3-main-title">
                {data.additional.label}
              </h2>
              <ul className="layout3-extra">
                {data.additional.items.map((item) => (
                  <li key={`${item.role}-${item.organization}`}>
                    <strong>
                      {item.role} · {item.organization}
                    </strong>
                    <span>
                      {' '}
                      ({item.startYear}
                      {item.endYear !== item.startYear
                        ? ` – ${item.endYear}`
                        : ''}
                      )
                    </span>
                  </li>
                ))}
              </ul>
            </section>
          ) : null}
        </div>
      </div>
    </article>
  )
}
