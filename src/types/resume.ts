export type MonthYear = {
  month: number
  year: number
}

export type WorkMode = 'Remote' | 'On-site' | 'Hybrid'

export type ExperienceItem = {
  role: string
  company: string
  companyWebsite?: string
  /** One-line explainer for employers a recruiter would not recognise. */
  companyNote?: string
  location: string
  workMode?: WorkMode
  startDate: MonthYear
  endDate: MonthYear | 'Present'
  bullets: string[]
  /** Rendered as a per-role "Technology" line by layouts that support it. */
  tech?: string[]
}

export type SkillItem = {
  name: string
  skills: string[]
}

export type EducationItem = {
  qualificationName: string
  qualificationField: string
  instituteName: string
  instituteLocation: string
  startYear: number
  endYear: number
  note?: string
}

export type AdditionalItem = {
  role: string
  organization: string
  location?: string
  startYear: number
  endYear: number | 'Present'
  bullets: string[]
}

export type ProjectItem = {
  name: string
  url?: string
  description: string
  startYear?: number
  endYear?: number
  tech?: string[]
}

export type LanguageItem = {
  name: string
  proficiency: string
}

export type CertificationItem = {
  name: string
  issuer: string
  year?: number
}

export type ResumeLinks = {
  email: string
  website?: string
  linkedin: string
  github?: string
  phone?: string
}

export type ResumeData = {
  name: string
  headline: string
  tagline?: string
  location?: string
  /** Explicit location / remote / relocation line for recruiter-inbound roles. */
  availability?: string
  links: ResumeLinks
  summary: {
    label: string
    text: string
  }
  /** Short bullet block at the top: years of experience, scope, headline wins. */
  highlights?: {
    label: string
    items: string[]
  }
  experience: {
    label: string
    items: ExperienceItem[]
  }
  skills: {
    label: string
    items: SkillItem[]
  }
  education: {
    label: string
    items: EducationItem[]
  }
  projects?: {
    label: string
    items: ProjectItem[]
  }
  certifications?: {
    label: string
    items: CertificationItem[]
  }
  additional: {
    label: string
    subtitle?: string
    items: AdditionalItem[]
  }
  languages?: LanguageItem[]
  interests?: string[]
  footer?: {
    text: string
    link: {
      label: string
      href: string
    }
  }
}
