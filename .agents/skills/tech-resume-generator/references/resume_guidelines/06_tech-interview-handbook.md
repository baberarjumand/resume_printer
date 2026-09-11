# Source 6 — Tech Interview Handbook: Practical guide to writing FAANG-ready SWE resumes

[Index](./00_README.md) · [Cross-source rules](./99_cross-source-rules.md)

- **URL:** [https://www.techinterviewhandbook.org/resume/](https://www.techinterviewhandbook.org/resume/)
- **Author:** Yangshun Tay — ex-Meta Staff Engineer; also author of Blind 75 / Grind 75
- **LinkedIn (author):** [https://www.linkedin.com/in/yangshun](https://www.linkedin.com/in/yangshun)
- **Source markdown in GitHub:** [apps/website/contents/resume.md](https://github.com/yangshun/tech-interview-handbook/blob/main/apps/website/contents/resume.md)
- **Last updated (page):** 7 Aug 2026
- **Audience:** Software engineers aiming at FAANG / large-tech ATS screens
- **Page description (frontmatter):** “How to write a top-tier, ATS-friendly resume good enough to pass resume screenings by Google, Amazon, Facebook and Microsoft”
- **Page type:** Prose how-to (not a template gallery). **No sample resume PDFs** are hosted; GitHub discussion [#288](https://github.com/yangshun/tech-interview-handbook/discussions/288) asked for a visual example and none was added. Paid templates are referred out to FAANG Tech Leads.
- **Local images:** `assets/sample_resumes/tech-interview-handbook/four-steps-to-create-a-software-engineer-resume.jpg` (checklist infographic; on-image title is “Four steps to prepare your Software Engineer resume”); `assets/sample_resumes/tech-interview-handbook/social-resume.png` (OG/social graphic, not a resume sample)
- **Related “read more” handbook pages** (linked after each TIH section): [professional summary](https://www.faangtechleads.com/resume/professional-summary), [contact](https://www.faangtechleads.com/resume/contact-information), [skills](https://www.faangtechleads.com/resume/skills), [work experience](https://www.faangtechleads.com/resume/work-experience), [education](https://www.faangtechleads.com/resume/education), [projects](https://www.faangtechleads.com/resume/projects). Public excerpts in §6.13.

**Thesis of the article:** Many qualified candidates fail screens because of the resume, not because they lack skill. Fix structure, content, keywords, then test with ATS-like tools.

**Four-step pipeline (article + infographic)**
1. Set up an ATS-friendly template
2. Fill it with well-framed content in a meaningful order
3. Optimize with prioritization and keywords
4. Test with free tools

Infographic checklist (note: the JPG still says **min 10px**; the article was later corrected to **min 10pt** — follow the article):

- Step 1: MS Word or Google Docs; standard format + reduced margins; Arial/Calibri/Garamond; standard headings/order
- Step 2: summary <50 words; contact = name, phone, location, email, LinkedIn; skills = languages, frameworks, databases; experience = skills/frameworks/DBs + quantifiable outcomes; ≥2 OSS or side projects with a viewable link
- Step 3: few best achievements > many average ones; pepper job-description keywords
- Step 4: test with free tools

### 6.1 ATS-friendly format

**Why it matters:** Most large tech companies parse thousands of resumes with ATS before a human reads them. Some systems auto-reject on rules. You cannot control which ATS a company uses, so optimize for *common* readable formats.

**Create in Word or Google Docs; submit PDF**
- Submit PDF to preserve layout, but author in Word/Docs so text is **highlightable** (precondition for parsing).
- Commonplace formats parse better than custom designs.
- Do **not** use Photoshop, graphic tools, or online resume builders.
- Do **not** put content in Word/Docs **headers or footers** (ATS often skips them). Instead shrink page margins. Recommended **narrow margins: 0.5" on each side**.

**Fonts**
- Use **Arial, Calibri, or Garamond**. Unusual fonts can turn letters into unreadable special characters.
- Minimum **10 pt** for later human readers (GitHub issue #728/#732/#733: do not use 10px; 10px ≈ 7.5pt).

**Standard section headings and order (Yangshun + recruiters)**

| Section | Heading to use |
| --- | --- |
| Professional summary | Do **not** title it “Professional Summary.” Use a **headline** as the section title, e.g. “Senior Software Engineer at Google with over 5 years of experience leading teams” |
| Contact | “Contact Information” |
| Skills (languages, frameworks, etc.) | “Skills” |
| Experience | “Work Experience” |
| Education | “Education” — **move above experience if still in school or <3 years of experience** |
| Projects | “Projects” |
| Optional | “Awards and Accolades” / “Certifications” / “Awards, Accolades and Certifications” |

**Never add symbols to headers** (ATS breakage).

**Paid plug on the page (not free samples):** [FAANG Tech Leads](https://www.faangtechleads.com) templates claimed to be ATS-readable, built from FAANG hiring-manager review of hundreds of applications, with offer-winning reference resumes. Commercial; not downloaded.

### 6.2 Professional summary

Interviewers often will not read every bullet. A summary that **directly answers why you fit this job** improves attention.

**Process**
1. List best selling points that match the JDs (roles + skills).
2. Compress into **<50 words**.
3. Requirements: answer why you fit; **active voice**; **action words**; start with the **role noun** (“Software Engineer”, “Front End Engineer”).
4. Section title = headline **<10 words**, like a slightly longer LinkedIn headline — not the words “Professional Summary.”

**Headline + summary examples (verbatim shapes)**

- **Software Engineer (Full Stack):** “Software Engineer with X years of full stack web development experience specializing in Ruby on Rails and PostgreSQL. Domain expert in e-commerce and payments field as a result of working at multiple e-commerce companies.”
- **Senior Front End Engineer:** “Front End Engineer with X years of experience and strong fundamentals in Front End technologies. Likes building scalable web infrastructure and making websites fast. Passionate about programming languages, compilers, and developer tooling.”
- **Software Engineering Lead:** “Software Engineer with X years of experience in back end, scaling complex distributed systems, and various cloud platforms. Led over 5 engineering teams with an average size of 6 members across two companies and mentored over 20 junior members.”
- **Senior at University X:** “Senior Year student at University X with a focus on Artificial Intelligence and Machine Learning (ML). Interned at X companies and worked on full stack development and ML engineering roles.”

**Conflict with UNC samples:** UNC’s five student templates have **no summary**. TIH strongly recommends one for FAANG screens, especially experienced hires. For an experienced SWE (6+ years, lead/CTO path), TIH’s summary-first model is more applicable than UNC undergrad templates.

### 6.3 Contact information

**Must-haves**
- Name at the very top of the resume
- Personal phone (**never work phone**)
- Location as **City, State, Zip** — enough to tell local vs international
- Email (**never work email**; Gmail preferred over obscure providers)
- LinkedIn

**Good-to-haves**
- GitHub URL
- Personal website
- Stack Overflow, Medium
- Competitive coding: CodeChef, HackerRank — include max ratings, rank, stars, badges if impressive

Separators: `|` or tabs.

### 6.4 Skills

Format:

> `[Skill summary] : [List skills separated by "|"]`

Groups called out: programming languages, frameworks, databases.

If impressive, quantify language use by **lines written**, e.g. “Over 10,000 lines.”

### 6.5 Work experience

Reverse chronological. Every job:

> `[Company or Organization], [Location] | [Job Title] | [Start and end dates as MM/YYYY]`

Example: `Facebook, Singapore | Front End Engineering Lead | 08/2018 - Present`

Then top accomplishments:
- Scope of job and skills required
- Accomplishments as: **`[Accomplishment summary] : [Action] that resulted in [quantifiable outcome]`**

### 6.6 Education

Most SWE jobs want at least an undergrad degree. **Do not put education above experience unless recent grad / little work history.**

Format (drop irrelevant bits):

> `[Degree Name], [Year of Graduation — expected date if not graduated]`  
> `[University Name], [Location]`  
> `GPA: X.XX / 4.0` (list if **> 3.50/4.00**, or **> 4.3/5.00**)  
> Key achievements: leadership, skills, societies, projects, awards

Example: BSc Computing/CS, NUS, 2015, GPA 3.82/4.00 Magna cum laude, Dean’s List, Valedictorian, President of hacker society.

### 6.7 Projects

Include **at least 2** projects with key contributions. **Hyperlink the project name** to GitHub or a live demo.

Example (Yangshun’s own): `facebook/docusaurus` — maintainer and lead engineer for Docusaurus v2, static site generator powering Meta OSS docs (React Native, Jest, Relay, Reason, …); used by 7.6k+ GitHub projects. Link: [https://github.com/facebook/docusaurus](https://github.com/facebook/docusaurus)

### 6.8 Awards / certifications

Only job-related; quantify.

> `[Year] | [Quantification] [Competition]`  
> Example: `2016 | Best All-Round Product out of 50 teams | Facebook Hackathon`

### 6.9 Keyword optimization

**Less is more:** a few best achievements beat many average ones. **One page.** Do not list everything to inflate quantity.

Hiring managers **scan for valued keywords** first. Recruiters/ATS do the same against the JD.

ATS behavior claimed in the article:
- Some score skill **strength by keyword frequency**
- Some infer **years of experience** from **which job block** the keyword sits in. Example as written: a 3-year job that mentions SEM may be treated as years of SEM experience (the page says the ATS will “assume 5 years” — treat the exact number as illustrative, the mechanism is placement-in-a-dated-role)

**How to optimize**
- Extract must-have and nice-to-have skills from the JD
- Put them in Skills **and** pepper the same language into Work Experience and Education
- Imitate JD wording
- Spell out abbreviations: Amazon Web Services not only AWS; Google Cloud Platform not only GCP
- Do **not** keyword-stuff; a human still reads it
- Tune **frequency and placement** to importance in the JD

**Batch-generalizing when per-job edits are too heavy**
1. Collect 3–5 JDs for that role type
2. Paste into a `.txt` file
3. Run a phrase-frequency tool such as [Online-Utility.org Text Analyzer](https://www.online-utility.org/text/analyzer.jsp)
4. Add the skills/experiences you actually have

### 6.10 Review tools named on the page

| Tool | URL | Role |
| --- | --- | --- |
| FAANG Tech Leads Resume Review | https://www.faangtechleads.com | Paid review by ex-FAANG hiring managers/engineers |
| Resume Worded scanner | https://resumeworded.com/resume-scanner | ATS-like readability/formatting |
| AI Resume Judge | https://ayehigh.com/resume-judge | Free ATS-like check |
| Targeted Resume | https://resumeworded.com/targeted-resume | Fit vs a specific JD + keywords |
| Resume Shortlister | https://ayehigh.com/resume-shortlister | Same idea |

**Plain-text paste test:** copy resume into a `.txt` file. Fix if content is missing, characters are garbled, or sections scramble. That approximates what a dumb parser sees.

### 6.11 Cover letter (same article)

- Handshake / intro of the professional persona; **complements rather than copies** the resume
- Tailor to company ethos, industry, and role; show research and how you serve the mission
- May be the **only** document some recruiters read
- Structure: (1) hook — why you are ideal, (2) value you add, (3) short relevant story; **almost never >1 page**
- Pitfalls: generic letter; repeating the resume; verbosity; typos
- Practical: align quals to needs; avoid clichés; first paragraph must grab; friend-proofread or rest-and-reread

**ML Engineer cover-letter example (verbatim from the page)**

1. *The Hook and personal touch* — “Growing up in Argentina, questions about economics are part of everyday life long before you become an Economics student. While many developing countries suffer the consequences of natural disasters or geopolitical conflicts, most - generations of Argentines have spent their entire lives avoiding the consequences of the crisis caused by macroeconomic imbalances in our country. Possibly due to this history, it is practically impossible to spend a day of your life without listening to a friend or family member make predictions about what the exchange rate between the peso and the dollar should be, or their opinion about what should be done by the Central Bank to lower inflation.”
2. *Motivation, background and growth story* — “Curiosity to find an answer to these daily questions was what motivated me to start my Degree in Economics at the University of Buenos Aires. I did my entire university career while working at the [BANK], experience that was exhausting and challenging in similar proportions. During my eight years working in a financial institution, I have seen first-hand how new technologies and Big Data tools have been transforming the way in which corporate decisions are made. That aroused my curiosity in the different Machine Learning techniques and for that reason I moved to Madrid to perform my Master in Big Data. After that, I was approached by a recruiter that gave me the opportunity to unleash my skills in the gaming industry in London.”
3. *Showcase achievements, impact and stakeholder management* — “[GAMING COMPANY] gave me an incredible opportunity. For the first time in my career, I was able to connect my childhood memories as a gamer with my professional skills. The capable leadership at [GAMING COMPANY] quickly identified my project management and analytical skills and they gave me huge responsibilities. I worked closely with the Chief Strategy Officer and the Head of External Developer Relations to identify potential publishing and M&A opportunities. During my watch we closed two strategic deals that are now contributing with more than 10% of the portfolio revenue. After that incredible experience, I was invited to join a start-smaller SaaS mobile data company called [SAAS COMPANY]. It was a hard decision but the challenge of joining a start-up and helping they grow and expand globally was an opportunity that I could not decline.”
4. *Motivation to join the company aligned with personal values* — “After [SAAS COMPANY] I had the opportunity to apply my skills in the Fintech industry. Coming from Argentina, where the population suffer the consequences of the absence of good credit, I was extremely excited about [BNLP FINTECH]’s mission of democratizing free-credit in the UK and the U.S.”

### 6.12 Application-form and ATS-behavior tips

- If the company has its own Work Experience / Education form fields, **fill them carefully**. Internal HR apps may be all the recruiter sees; the PDF might never be opened.
- **Do not apply to many jobs at the same company.** ATS shows recruiters every role you applied to. Mixed signals (e.g. SWE **and** Data Scientist at the same firm) look unfocused.

Contact for handbook contributions: contact@techinterviewhandbook.org or [GitHub discussions](https://github.com/yangshun/tech-interview-handbook/discussions).

### 6.13 Related articles linked from the TIH resume page (FAANG Tech Leads Resume Handbook)

These are the “read more about this section” links. **Public (free) content is recorded below. Remaining checklists are paywalled** (“Unlock exclusive … content”). No sample resume PDFs/images on those pages other than a generic OG jpg.

#### Contact information — [faangtechleads.com/resume/contact-information](https://www.faangtechleads.com/resume/contact-information)

Free recommendations:
- Top of resume: name, email, phone, location, LinkedIn URL
- Personal email you will keep (not a school address you might lose)
- Be explicit about **city and state** in large countries; same-state proximity can help
- Phone with country code: `+1 (123) 456-7890`
- Extra professional links: site, blog, GitHub, SO, Twitter, Medium, Substack
- Link **text** should be `linkedin.com/in/johndoe` not the word “LinkedIn” — interviewers print resumes
- Do not add birthday, age, photo
- Do not link empty GitHub/Medium/SO profiles
- Click every link before sending

Example layout:

```
John Doe
San Francisco, California, US | +1 (650) 123-4567 | john.doe@gmail.com
github.com/johndoe | linkedin.com/in/johndoe | johndoe.com
```

Paywalled subsections (not extracted): “Supercharge your LinkedIn profile”, “Give your GitHub profile a makeover.”

**Tension with UNC samples:** UNC often shows the words “LinkedIn | GitHub” as hyperlinks. FTL/TIH want the **visible URL/username** because of printing.

#### Professional summary — [faangtechleads.com/resume/professional-summary](https://www.faangtechleads.com/resume/professional-summary)

Free recommendations:
- Summarize background; mention **years and title**, especially if relevant years are only a slice of total career or there were breaks
- Tailor to the role; reuse JD keywords
- Use this section to explain **unconventional paths**: domain switch, IC↔manager, bootcamp, semi-technical → fully technical (no other section fits this)

Free mistakes:
- Don’t write an “objective” unless the situation is unconventional — the applied-for role already states the objective
- Don’t claim too many specializations. Bad: “decade of experience specializing in cloud, full stack, ML, big data, and data viz” — that’s ~80% of the industry, not a specialty, hard to prove in one page, and companies don’t need that spread. Tailor the specialty to the posting.

Free examples:
- Front End Engineer, six years, small and large teams, interactive feature-rich web apps; lifelong learner; modern web + web3 (blockchain, crypto, DeFi)
- CS junior undergrad, passionate about full stack, substantial Rails experience, quick learner / creative problem solver

#### Work experience — [faangtechleads.com/resume/work-experience](https://www.faangtechleads.com/resume/work-experience)

Free intro (checklist paywalled):
- For experienced people this is the **meat**; often **≥ half the page**
- Students with weak internships can let **Projects rival Work Experience** in length
- Goal: value to the next employer via contribution to **business goals**
- Each role: title, company, dates, accomplishment bullets
- Most common failure: not elaborating. Differentiate on **scale, complexity, and impact** (retail investor vs Buffett analogy)

#### Education — [faangtechleads.com/resume/education](https://www.faangtechleads.com/resume/education)

Free intro:
- Education decays with time; some employers ignore GPA after the first job
- Undergrads: education still high-signal → **usually top**; exception if internships/projects are more impressive, those can go first
- Senior SWE+: education **to the bottom** — recent work predicts performance better than a decade-old class

#### Projects — [faangtechleads.com/resume/projects](https://www.faangtechleads.com/resume/projects)

Free intro:
- Side technical work: libraries, tools/sites, technical writing/blog, hackathons
- Signals passion; stronger if the reader has **heard of or used** it
- Hiring managers especially impressed by **OSS**, more so in complex codebases with real usage (quality + design + courage to publish)
- **Optional if you already have work experience**; seniors with families often have no side projects
- Use projects to **fill a domain gap**: undergrads with few internships; engineers switching (e.g. full stack → mobile/ML) who cannot do it at work — then **build side projects in the target domain**

#### Skills — [faangtechleads.com/resume/skills](https://www.faangtechleads.com/resume/skills)

Entire recommendations list is paywalled. Rely on TIH’s free skills format in §6.4.
