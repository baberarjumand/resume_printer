import type { ResumeData } from '../types/resume.ts'
import { formatDateRangeLong } from '../lib/dates.ts'
import { renderRichText } from '../lib/richText.tsx'
import './resumeLayout2.css'

type Props = {
  data: ResumeData
}

function displayUrl(url: string): string {
  return url
    .replace(/^https?:\/\//i, '')
    .replace(/^www\./i, '')
    .replace(/\/$/, '')
}

export function ResumeLayout2({ data }: Props) {
  const projects = data.projects?.items ?? []
  const certifications = data.certifications?.items ?? []

  return (
    <article className="layout2-sheet">
      <header className="layout2-header">
        <div className="layout2-header-main">
          <h1 className="layout2-name">{data.name}</h1>
          <p className="layout2-tagline">{data.tagline ?? data.headline}</p>
        </div>
        <ul className="layout2-contact">
          <li>
            <a href={`mailto:${data.links.email}`}>{data.links.email}</a>
          </li>
          {data.location ? <li>{data.location}</li> : null}
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
      </header>

      <div className="layout2-body">
        <div className="layout2-main">
          <section>
            <h2 className="layout2-section-title">
              {data.experience.label}
            </h2>
            {data.experience.items.map((item) => (
              <article
                className="layout2-job"
                key={`${item.role}-${item.company}-${item.startDate.year}-${item.startDate.month}`}
              >
                <p className="layout2-job-heading">
                  <span className="layout2-job-role">{item.role}</span>
                  <span className="layout2-job-dot"> · </span>
                  <span className="layout2-job-company">{item.company}</span>
                  <span className="layout2-job-dates">
                    {' '}
                    {formatDateRangeLong(item.startDate, item.endDate)}
                  </span>
                </p>
                <ul className="layout2-bullets">
                  {item.bullets.map((bullet, index) => (
                    <li key={index}>{renderRichText(bullet)}</li>
                  ))}
                </ul>
              </article>
            ))}
          </section>

          {data.additional.items.length > 0 ? (
            <section className="layout2-main-extra">
              <h2 className="layout2-section-title">{data.additional.label}</h2>
              {data.additional.items.map((item) => (
                <article
                  className="layout2-job"
                  key={`${item.role}-${item.organization}-${item.startYear}`}
                >
                  <p className="layout2-job-heading">
                    <span className="layout2-job-role">{item.role}</span>
                    <span className="layout2-job-dot"> · </span>
                    <span className="layout2-job-company">
                      {item.organization}
                    </span>
                    <span className="layout2-job-dates">
                      {' '}
                      {item.startYear}
                      {item.endYear !== item.startYear
                        ? ` — ${item.endYear}`
                        : ''}
                    </span>
                  </p>
                  <ul className="layout2-bullets">
                    {item.bullets.map((bullet, index) => (
                      <li key={index}>{renderRichText(bullet)}</li>
                    ))}
                  </ul>
                </article>
              ))}
            </section>
          ) : null}
        </div>

        <aside className="layout2-sidebar">
          <section>
            <h2 className="layout2-section-title">{data.skills.label}</h2>
            {data.skills.items.map((group) => (
              <div className="layout2-skill-group" key={group.name}>
                <h3 className="layout2-skill-label">{group.name}</h3>
                <p className="layout2-skill-list">{group.skills.join(', ')}</p>
              </div>
            ))}
          </section>

          {projects.length > 0 ? (
            <section>
              <h2 className="layout2-section-title">
                {data.projects?.label ?? 'Selected Projects'}
              </h2>
              {projects.map((project) => (
                <article className="layout2-project" key={project.name}>
                  <h3 className="layout2-project-name">
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
                  </h3>
                  <p className="layout2-project-desc">{project.description}</p>
                </article>
              ))}
            </section>
          ) : null}

          <section>
            <h2 className="layout2-section-title">Education</h2>
            {data.education.items.map((item) => (
              <article
                className="layout2-edu"
                key={`${item.instituteName}-${item.endYear}`}
              >
                <h3 className="layout2-edu-school">{item.instituteName}</h3>
                <p className="layout2-edu-detail">
                  {item.qualificationName} in {item.qualificationField}
                  {item.note ? ` (${item.note})` : ''}
                </p>
                <p className="layout2-edu-detail">
                  {item.startYear} – {item.endYear}
                </p>
              </article>
            ))}
          </section>

          {certifications.length > 0 ? (
            <section>
              <h2 className="layout2-section-title">
                {data.certifications?.label ?? 'Certifications'}
              </h2>
              {certifications.map((cert) => (
                <article className="layout2-edu" key={cert.name}>
                  <h3 className="layout2-edu-school">{cert.name}</h3>
                  <p className="layout2-edu-detail">
                    {cert.issuer}
                    {cert.year ? ` · ${cert.year}` : ''}
                  </p>
                </article>
              ))}
            </section>
          ) : null}

          {data.languages && data.languages.length > 0 ? (
            <section>
              <h2 className="layout2-section-title">Languages</h2>
              {data.languages.map((language) => (
                <p className="layout2-edu-detail" key={language.name}>
                  <strong>{language.name}</strong> — {language.proficiency}
                </p>
              ))}
            </section>
          ) : null}

          {data.interests && data.interests.length > 0 ? (
            <section>
              <h2 className="layout2-section-title">Interests</h2>
              <p className="layout2-skill-list">{data.interests.join(', ')}</p>
            </section>
          ) : null}
        </aside>
      </div>
    </article>
  )
}
