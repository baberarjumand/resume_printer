# Source 1 — UNC CS Tech Resume + CV Samples (primary)

[Index](./00_README.md) · [Cross-source rules](./99_cross-source-rules.md)

- **URL:** [https://cs.unc.edu/student-life/career/tech-resume-samples/](https://cs.unc.edu/student-life/career/tech-resume-samples/)
- **Publisher:** UNC Chapel Hill Department of Computer Science, Career Services
- **Page title:** Tech Resume + CV Samples
- **Published / updated:** First published 2022-02-10; last modified **2026-07-06** (Summer 2026 template refresh)
- **Parent hub:** [https://cs.unc.edu/student-life/career/](https://cs.unc.edu/student-life/career/)
- **Stated purpose (verbatim):** “Looking for something to help structure your technical resume? The templates below are a great starting point for writing a CS resume.”
- **Page type:** Template gallery, not a prose how-to. Almost all guidance is **encoded in the five sample layouts**. The notes below reverse-engineer those samples.

### 1.1 Templates on the page

The page groups them under **“Computer Science + Data Science Resume Templates”**, then a **CV resources** list.

| # | Page label | Audience | Google Docs (make a copy) | Preview image (on page) | Local files |
| --- | --- | --- | --- | --- | --- |
| 1 | CS Major Resume Template #1 | CS undergrad, software-engineering internships | [copy](https://docs.google.com/document/d/1PJUSoH2h7yOo2EgUX2CMzBFnIVEVlyyFg-igl9fXGdY/copy) | [PNG](https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/Technical-Resume-Template-Updated-Summer-2026.png) | `assets/sample_resumes/unc-cs/cs-major-template-1_technical-resume-summer-2026.{png,pdf}` |
| 2 | CS Major Resume Template #2 (Data Science + Machine Learning-Focused) | CS undergrad targeting DE/ML/data roles | [copy](https://docs.google.com/document/d/11Dqv4UMeLE15T1h97SDaK0ghDD07lxfIkGPHQj89nCY/copy) | [PNG](https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/ML-Focused-Technical-Resume-Template-Updated-Summer-2026.png) | `assets/sample_resumes/unc-cs/cs-major-template-2_ml-data-science-summer-2026.{png,pdf}` |
| 3 | Master of Computer Science Resume Template | MSCS / experienced new-grad master’s | [copy](https://docs.google.com/document/d/1HUhyYwbJ73OA1eD5gtAYEVtuV9ZMzHIf_brZMxyflTQ/copy) | [PNG](https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/MSCS-Resume-Updated-Summer-2026.png) | `assets/sample_resumes/unc-cs/mscs-resume-template-summer-2026.{png,pdf}` |
| 4 | Pre-CS Resume Template | “For those looking to update their resume but are not yet in the CS major” | [copy](https://docs.google.com/document/d/1T5vx1w4Bdb8H45or0i0hz3bDGybMANXc_KJRQ9NjHpo/copy) | [PNG](https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/Pre-CS-Technical-Resume-Template-Updated-Summer-2026.png) | `assets/sample_resumes/unc-cs/pre-cs-technical-resume-template-summer-2026.{png,pdf}` |
| 5 | B.S. in Data Science | Data science undergrad | [copy](https://docs.google.com/document/d/1sKIl4BCVBldWkoA0M-_CK-6HdPnKWVhB3Uq_YmL-4BI/copy) | [PNG](https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/Data-Science-Resume-Sample-Updated-Summer-2026.png) | `assets/sample_resumes/unc-cs/bs-data-science-resume-sample-summer-2026.{png,pdf}` |

Instruction on every template: **“Make a copy, then edit.”** They are fill-in samples (famous-name placeholders: Ada Lovelace, Hedy Lamarr, Alan Turing, Grace Hopper), not a student’s real CV.

### 1.2 Shared visual / structural system (all five samples)

These conventions are consistent enough to treat as UNC CS Career Services’ implied standard for a **one-page technical resume**.

**Length and density**
- Strictly **one page**.
- Single column (unlike the MIT 2-column example linked later).
- Black text on white; no color besides hyperlink blue on contact links.
- Horizontal rules under section headings.
- Name centered, large, title case; contact centered on one line under the name.
- Generous but not sparse: typically 2–4 bullets per role, 2 projects, skills as compact labeled lines rather than a huge cloud.

**Header / contact**
- Name only (no “Software Engineer” headline in the header on these student templates).
- Contact as a single separator line: email, phone, LinkedIn, GitHub.
- MSCS template also reserves a slot for **Portfolio (if applicable)**.
- LinkedIn/GitHub often shown as the words “LinkedIn | GitHub” (hyperlinked), not the raw URL, to save space.

**Section order (early-career default)**
1. Education (always first on these student templates)
2. Technical skills (templates 1, 2, 4) **or** Relevant Experience then skills later (MSCS, DS samples vary)
3. Relevant / industry / research experience
4. Projects (omitted on the MSCS sample, which is experience-heavy)
5. Leadership, additional, or extracurricular experience
6. Skills & certifications (DS sample puts this last)

**Education block pattern**
```
University Name | City, ST                                          Graduation Month Year
Degree, Minors | GPA: X.X/4.0
    • Relevant Courses: … (or a non-bulleted “Relevant Coursework:” line)
    • Honors: …
```
- School and location left; **date right-aligned**.
- GPA shown as `3.7/4.0` when included.
- Coursework is **selective and job-relevant**, not a full transcript.
- Honors/awards can live under education (Dean’s List, Honors Carolina, hackathon awards) or as a sub-line.

**Experience block pattern**
```
Company | City, ST                                                  Start – End
Job Title (often italic)
    • Achievement bullet with tech + metric
```
- Company and location on the same line as dates.
- Title on the next line, not competing with the company name.
- Reverse chronological within the section.
- Internships and TA roles count as “Relevant Experience.”
- Non-technical work is isolated in “Professional Experience” or “Additional/Extracurricular” so it does not dilute the technical story.

**Bullet rhetoric (repeated across all templates)**
- Start with a **strong past-tense (or present-tense for current) verb**: Designed, Implemented, Developed, Engineered, Leveraged, Reduced, Mentored, Partnered, Pioneered, Streamlined, Analyzed, Awarded, Lead/Led, Manage/Managed, Collaborated, Built, Deployed, Automated, Evaluated, Presented, Investigated, Architected, Optimized, Created.
- Pair **technology names** with **outcomes**: latency −22%, cost −15%, coverage 95%+, churn +15% retention, compression 60%, reporting time −95%, error response −95%, accuracy 83%, robustness +18%, experiment cycle −40%, query time −35%, refresh +50%, deployment failures −25%.
- Name **scale**: 600 students, 10+ hours/week, team of 3, 8 features in 6 months, 6 million records, 1.88 million records, 10+ regional sub-teams, 20+ students, 20 hours/week.
- Name **systems**: AWS Lambda, DynamoDB, Node.js, Swift, Firebase, BigQuery, GCS, Scala, Apache Beam, Hive, Tableau, Spark, Kubernetes, Spring Boot, scikit-learn, NLTK, etc.
- **Summer 2026 refresh explicitly models AI-tool use as a professional skill**, not a secret: GitHub Copilot, OpenAI API, “AI-assisted development tools,” “LLM-assisted exploratory data analysis,” “AI-driven debugging,” “AI-assisted workflows,” “audit AI-generated code for quality.” Use AI as an accelerator **and** mention review/quality control.

**Skills block pattern**
- Short labeled lines, not a dump of 50 tags.
- Typical labels: Languages (sometimes “by proficiency”), Tools and Frameworks / Technologies / Tools, AI & Data Tools, Machine Learning, Cloud & DevOps, Methodologies, Operating Systems, Certifications.
- Pre-CS template is the only one that **self-rates language level** (Intermediate / Beginner).
- MSCS groups: Languages; AI & Machine Learning; Frameworks; Cloud & DevOps; Methodologies (Agile, TDD, CI/CD).
- Do not mix soft skills into the technical skills line; leadership goes in its own section.

**Projects block pattern**
```
ProjectName | Context or stack                                      Date
    • What you built + stack + result/award
```
- Context tags: `HackNC`, `Personal Project`, or languages (`R, Python`).
- Hackathon awards are first-class (Pendo, Appian, Red Ventures, third place overall).
- Two projects is enough on a packed page.

**What these templates omit (intentional)**
- No objective / career-objective paragraph on the undergrad templates.
- No photo, no street address (city/state only on experience lines).
- No references, no “references available upon request.”
- No hobbies.
- No multi-page CV layout (CV is delegated to the linked resources).

### 1.3 Template-by-template content model

#### Template #1 — CS major / SWE intern (Ada Lovelace)

**Section order:** Education → Technical Skills → Relevant Experience → Projects → Leadership Experience

**Education:** B.S. Computer Science, minors in Data Science and Studio Art; GPA; relevant courses spanning systems, web, mobile, DS&A; Dean’s List / Honors Carolina.

**Skills:** Languages ordered **by proficiency**; libraries nested under Python `(Pandas, Matplotlib, Plotly, pytest)`; frameworks Node/React/AngularJS/Docker/PyTorch/Git; AI tools Copilot + OpenAI API.

**Experience mix modeled as ideal for intern recruiting:**
1. Current Big Tech SDE intern (backend, AWS, cost/latency, AI-assisted testing)
2. Campus TA / grading lead (mentorship scale + scripting to operationalize grading)
3. Prior finance-tech intern (Node/Python, Agile pair programming, SQL/API, **auditing AI-generated code**)

**Projects:** One flagship hackathon app (iOS/Swift/Firebase/API) with placement.

**Leadership:** CS for Social Good project manager — meetings, timelines, plus a technical contribution (backend/API). Leadership is not “attended club.”

**Takeaway for later resume drafting:** SWE intern resume = education + compact skills + 2–3 relevant roles + 1–2 shipped projects + one leadership role that still has a technical bullet.

#### Template #2 — CS major, DS/ML/data engineering (Hedy Lamarr)

**Section order:** Education → Technical Skills → Relevant Experience → Projects

**Education:** B.S. Computer Science, Statistics; ML-heavy coursework (ML, DS&A, files & databases, OOP). No honors line.

**Skills:** Broader data stack: C/Java/JS/Python/R/Scala/SQL; Docker, Flask, Git, Node, PyTorch, React, REST; Apache Beam/Hadoop/Spark, BigQuery, GCP, Jira, Jenkins, Jupyter, Snowflake, Tableau, Copilot, OpenAI API.

**Experience mix:** Data Engineer intern (Spotify-style: pipelines, BigQuery, Scala/Beam, LLM-assisted EDA, A/B tests) → Lead TA → Data Engineer intern (dashboards, Hive, exec presentations) → earlier Software Engineer intern (frontend features + 100% API test automation).

**Projects:** Two data-science projects with **dataset size, model names, and accuracy/lift** (6M records, RF/NB/LR/SVM, 83% accuracy, +10% from sampling; 1.88M wildfire records, 3.5% annual growth, 64% human-caused).

**Takeaway:** For data/ML targeting, swap SWE internships for DE internships, put pipeline/cloud tools in skills, and make projects model-and-metric heavy. No separate leadership section — TA leadership is folded into relevant experience.

#### Template #3 — MSCS (Alan Turing)

**Section order:** Education (grad + undergrad) → Industry Experience → Research Experience → Technical Skills

**Header:** Email | Phone | LinkedIn | GitHub | Portfolio (if applicable). Square-bracket placeholders signal “fill these.”

**Education is richer than undergrad templates:**
- Master’s: relevant coursework + **named research one-liner with advisor** + **thesis title**
- Bachelor’s: dual major, honors (Dean’s List all semesters, Magna cum Laude), earlier grad date

**Industry:** Full-time SWE (3 years) then intern. Bullets cover microservices, Docker/K8s, SQL, REST, Agile, CI/CD, AI-assisted pipeline, code coverage 92%. Intern: React/Node dashboard, Spring Boot APIs, SQL.

**Research:** Separate section (not mixed into industry). GRA bullets: adversarial robustness +18%, Spark/Pandas, MLOps/TensorFlow pipelines −40% cycle time, workshop presentation.

**No projects section** — industry + research already fill the page.

**Takeaway:** After full-time experience, drop “Projects” if jobs/research are stronger. Split **Industry** vs **Research**. Lead with the degree that matches the ask (MSCS first). Skills can sit last once experience is dense.

#### Template #4 — Pre-CS (Grace Hopper, intended CS)

**Page note:** Designed for students **not yet in the CS major**.

**Section order:** Education → Technical Skills → Projects → Professional Experience → Extracurricular Experience

**Education:** `(Intended) B.S. in Computer Science`; intro coursework only (intro programming, data structures, discrete, multivariable calculus).

**Skills:** Honest levels (Python/Java Intermediate, HTML Beginner); Git, JUnit, Figma; AI Tools: GitHub Copilot; OS: Windows, Linux.

**Projects come before jobs** — the technical proof is coursework/hackathon/personal games, not employment. HackNC project describes a full stack (JS frontend, AJAX, REST, relational DB, ORM) plus awards.

**Professional experience includes non-CS work**, rewritten with transferable metrics:
- Math tutor: 20+ students, AI tools −40% content-creation time, 5 hours/week, named courses (Calculus, Trigonometry)
- Restaurant server: 20 hours/week, customer satisfaction, communication/teamwork, attention to detail

**Extracurricular:** Media committee for a hackathon — photoshoot of 20 people, day-of photography, marketing. Shows CS-community involvement without a major.

**Takeaway:** If the degree isn’t CS yet, **lead with projects**. Keep non-tech jobs but quantify them. Never pretend advanced coursework you have not taken.

#### Template #5 — B.S. Data Science (Grace Hopper)

**Section order:** Education → Relevant Experience → Technical Projects → Additional Experience → Skills & Certifications

**Education:** B.S. Data Science, minor in Music; GPA 3.8; DS-flavored coursework (DS&A, ML, Communications to Data Scientists, Game Theory, Sports Analytics); Dean’s List + HackNC “Best Use of Data.”

**Relevant experience:** Research assistant (NLP, Python/Pandas, AI-assisted prep, co-authored conference paper) then DS intern (churn model +15% retention, Python/SQL, Tableau, −35% prep time).

**Projects:** Predictive analytics (scikit-learn/pandas) and social-media sentiment (NLTK, TextBlob, Matplotlib, compared to LLM classifications).

**Additional experience:** WiCS treasurer — **$10,000 budget** (quantified leadership, not “member”).

**Skills last, including certifications:** IBM Data Science Professional Certificate, Tableau Desktop Specialist; ML methods; AI tools.

**Takeaway:** DS resume can put skills at the bottom if experience/projects already name the stack. Certifications belong on the skills line. Club finance is valid “additional” experience when quantified.

### 1.4 Related links listed on the UNC page (CV resources)

The page’s **“CV (Curriculum Vitae) Resources”** list (analyzed as sibling sources):

1. [LaTeX templates and examples — CVs and resumes](https://www.overleaf.com/gallery/tagged/cv) → [Source 4](./04_overleaf-cv-gallery.md)
2. [9 Computer Science CV Examples [+ Template]](https://www.tealhq.com/cv-examples/computer-science) → [Source 3](./03_tealhq-computer-science-cv-examples.md)
3. [MIT CV Template](https://mitcommlab.mit.edu/eecs/wp-content/uploads/sites/6/2016/09/EECS_CommKit_CVResume_AAE1.png) (image; belongs to the MIT EECS CommKit article) → [Source 2](./02_mit-eecs-commkit-cv-resume.md)

Also in the breadcrumb/nav (not a resume article): [Source 5 — UNC CS Career Services hub](./05_unc-cs-career-services-hub.md).
