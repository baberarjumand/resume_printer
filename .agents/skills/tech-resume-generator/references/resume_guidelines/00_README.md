# Resume guidelines — index

Living notes for later resume generation. Each analyzed page has its own file. Extracted rules, sample transcriptions, and conflicts live **in those files**, not here.

Shared defaults distilled from all sources so far: [99_cross-source-rules.md](./99_cross-source-rules.md).

**Note for agents:** Sections titled “Tensions / experienced candidate” (and similar) compare each source to **the end user being generated for**. Apply them relative to *their* seniority and goals. Contact values always come from the user’s compiled data (see Critical identity below).

## Critical identity (must follow)

These rows override every source file and [99_cross-source-rules.md](./99_cross-source-rules.md) for **layout and link behavior**. Values come from the user’s compiled professional data (`output/professional_data.md`). Do not invent, omit, or restyle fields the user provided; do not invent fields they did not.

| # | Field | Required value | How it must appear |
| --- | --- | --- | --- |
| 1 | Full name | From user data | Exact spelling as in their sources. Header name. |
| 2 | Location | From user data | City + country (or city + region). No street address. |
| 3 | Phone | From user data | Visible as the user’s number. Clickable `tel:` href so a tap/click opens the phone app. |
| 4 | Email | From user data | Visible as the user’s email. Clickable `mailto:` href. Prefer a personal email over a school email unless they are a current student. |
| 5 | Websites / portfolio | From user data (if any) | Include each site they want listed. Visible text can omit `https://`; each is a PDF hyperlink that opens in a new tab/window. |
| 6 | LinkedIn | From user data (if any) | Visible text like `linkedin.com/in/handle/`. Href is the full https URL. |
| 7 | GitHub | From user data (if any) | Visible text like `github.com/handle`. Href is the full https URL. |
| 8 | Education | From user data | List degrees/schools the user wants on the résumé after reconciliation. Do not invent schools; omit incomplete transfers unless the user asks to keep them. |

Clickable phone, email, websites, LinkedIn, and GitHub must work in the **printed/exported PDF**, not only in a web preview.

Sample images/PDFs/DOCX are **optional** under `assets/sample_resumes/` (index: `assets/sample_resumes/download_manifest.json`). They are not shipped by default — download with `python3 skills/tech-resume-generator/scripts/download_sample_resumes.py` from the repo root (or `npm run download-samples` / `python3 scripts/download_sample_resumes.py` from inside the skill folder).

| # | Source | URL |
| --- | --- | --- |
| 01 | UNC CS Tech Resume + CV Samples | https://cs.unc.edu/student-life/career/tech-resume-samples/ |
| 02 | MIT EECS Communication Lab, CV/Resume | https://mitcommlab.mit.edu/eecs/commkit/cvresume/ |
| 03 | TealHQ: 9 Computer Science CV Examples | https://www.tealhq.com/cv-examples/computer-science |
| 04 | Overleaf gallery: LaTeX CVs and résumés | https://www.overleaf.com/gallery/tagged/cv |
| 05 | UNC CS Career Services hub | https://cs.unc.edu/student-life/career/ |
| 06 | Tech Interview Handbook — FAANG-ready SWE resumes | https://www.techinterviewhandbook.org/resume/ |
| 07 | Tiffany Jachja — The Elements of a Tech Resume | https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6 |
| 08 | Yale OCS STEMConnect: Technical Resume Sample | https://ocs.yale.edu/resources/stemconnect-technical-resume-sample/ |
| 09 | LinkedIn Top Content — What to Highlight in a Tech Resume Format | https://www.linkedin.com/top-content/career/resume-formats-for-tech-jobs/what-to-highlight-in-a-tech-resume-format/ |
| 10 | Harvard MCS — Harvard College Guide to Creating a Strong Resume | https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/ |
| 11 | r/EngineeringResumes — 12 YoE hiring-manager advice (woodworksio) | https://www.reddit.com/r/EngineeringResumes/comments/1hw10ms/12_yoe_some_long_direct_advice_in_tech_from_a/ |
| 12 | Penn Career Services — Write a Resume/CV | https://careerservices.upenn.edu/channels/resume/ |
| 13 | ACI Tech Academy — 2026 tech resume guide (career-changer) | https://www.acitechacademy.com/blog/struggling-to-get-your-tech-resume-noticed-here-s-how-to-land-interviews-in-2024/ |
| 14 | Emanate Technology — How to Write a Tech CV (AU recruiter) | https://www.emanatetechnology.com.au/news/how-to-write-a-tech-resume-with-example |
| 15 | Rewriting the Code — How to Write a Tech Resume | https://rewritingthecode.org/resources/member-resources/how-to-build-a-tech-resume/ |
| 16 | UT Austin CNS — Strong Bullets for Technical Resumes | https://careerservices.cns.utexas.edu/resources/resumes/strong-bullets-technical-resumes |
| 17 | Per Scholas — How to land your first job in tech (resume & interview) | https://perscholas.org/news/how-to-land-your-first-job-in-tech-resume-and-interview-tips/ |
| 18 | Georgia Tech Career Center — Undergraduate resumes, cover letters & portfolios | https://career.gatech.edu/undergrad-job-search/resumes/ |
| 19 | Mastercard Careers — How to tailor your technology resume | https://careers.mastercard.com/us/en/blogarticle/how-to-tailor-your-technology-resume-for-the-job-you-want |
| 20 | Toptal Resume — The Perfect Tech Resume in 2025 | https://www.toptal.com/resume/career-center/the-perfect-tech-resume-in-2025-key-trends-ats-keywords-and-formatting-tips |
| 21 | IGotAnOffer — Tech Resume Examples (FAANG) | https://igotanoffer.com/blogs/tech/tech-resume-examples |

## Files

| File | What it is |
| --- | --- |
| [01_unc-cs-tech-resume-samples.md](./01_unc-cs-tech-resume-samples.md) | Five Summer 2026 UNC CS/DS templates reverse-engineered |
| [02_mit-eecs-commkit-cv-resume.md](./02_mit-eecs-commkit-cv-resume.md) | MIT CommKit resume vs CV guidance + two annotated examples |
| [03_tealhq-computer-science-cv-examples.md](./03_tealhq-computer-science-cv-examples.md) | TealHQ CS CV writing rules and example personas |
| [04_overleaf-cv-gallery.md](./04_overleaf-cv-gallery.md) | Overleaf CV/resume template catalog (no files downloaded) |
| [05_unc-cs-career-services-hub.md](./05_unc-cs-career-services-hub.md) | UNC CS career hub (contacts only; no writing rules) |
| [06_tech-interview-handbook.md](./06_tech-interview-handbook.md) | TIH SWE resume guide + public FAANG Tech Leads excerpts |
| [07_tiffany-jachja-elements-of-a-tech-resume.md](./07_tiffany-jachja-elements-of-a-tech-resume.md) | Jachja 2024 article, 16 screenshots, checklist companion, O\*NET |
| [08_yale-ocs-stemconnect-technical-resume.md](./08_yale-ocs-stemconnect-technical-resume.md) | Yale STEMConnect template + linked OCS resume pages |
| [09_linkedin-what-to-highlight-in-a-tech-resume.md](./09_linkedin-what-to-highlight-in-a-tech-resume.md) | LinkedIn Top Content roundup + related format/length pages |
| [10_harvard-mcs-create-a-strong-resume.md](./10_harvard-mcs-create-a-strong-resume.md) | Harvard College resume/cover guide, templates, CS + engineering examples |
| [11_engineeringresumes-12yoe-hiring-manager.md](./11_engineeringresumes-12yoe-hiring-manager.md) | Reddit HM 15-point US tech résumé list + wiki Google Doc template |
| [12_upenn-career-services-resume-hub.md](./12_upenn-career-services-resume-hub.md) | Penn Career Services résumé hub, undergrad CS/CompE samples, SCO bullets |
| [13_aci-tech-academy-2026-tech-resume.md](./13_aci-tech-academy-2026-tech-resume.md) | ACI bootcamp 2026 IT-support résumé post (no sample files) |
| [14_emanate-technology-tech-cv.md](./14_emanate-technology-tech-cv.md) | AU tech-recruiter CV guide, Luca/Mal flags, 2020 4-page PM Word sample |
| [15_rewriting-the-code-tech-resume.md](./15_rewriting-the-code-tech-resume.md) | RTC student/early-career guide, verb+tech+metric formula, Google Docs examples |
| [16_ut-austin-cns-strong-bullets.md](./16_ut-austin-cns-strong-bullets.md) | UT CNS What/Why/How bullets, ATS, 1-page technical Google Docs template |
| [17_perscholas-first-job-tech-resume.md](./17_perscholas-first-job-tech-resume.md) | Per Scholas first-job / career-changer résumé + interview tips (no samples) |
| [18_gatech-career-center-undergrad-resumes.md](./18_gatech-career-center-undergrad-resumes.md) | GT Career Center hub, Resume Career Guide, CS Word samples, MS experienced sample |
| [19_mastercard-tailor-technology-resume.md](./19_mastercard-tailor-technology-resume.md) | Mastercard employer tech-resume tips, AI application rules (no samples) |
| [20_toptal-perfect-tech-resume-2025.md](./20_toptal-perfect-tech-resume-2025.md) | Toptal 2025 ATS/keywords/format guide + SWE/summary siblings (no samples) |
| [21_igotanoffer-tech-resume-examples.md](./21_igotanoffer-tech-resume-examples.md) | IGotAnOffer FAANG samples (12+) + Karl/senior templates + Google How we hire |
| [99_cross-source-rules.md](./99_cross-source-rules.md) | Agreed defaults across the sources above |

## Analyses so far (by batch)

**Batch 1 — UNC CS page and its related links (Sources 01–05)**  
Primary: UNC Tech Resume + CV Samples (updated Summer 2026). Followed from that page: MIT EECS CommKit (the “MIT CV Template” image + parent article), TealHQ CS CV examples, Overleaf CV gallery, UNC Career Services hub.

**Batch 2 — Tech Interview Handbook (Source 06)**  
Primary: [techinterviewhandbook.org/resume](https://www.techinterviewhandbook.org/resume/) (Yangshun Tay, updated 7 Aug 2026). Followed its “read more” FAANG Tech Leads handbook pages (public/free portions only): professional summary, contact, skills (paywalled beyond TIH), work experience, education, projects.

**Batch 3 — Tiffany Jachja (Source 07)**  
Primary: [The Elements of a Tech Resume](https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6) (9 Sep 2024). On-page link: [O\*NET OnLine](https://www.onetonline.org/). Same-author companion (not linked from that post): [A Tech Resume Checklist](https://tiffanyjachja.medium.com/a-tech-resume-checklist-ec91bbd8d0c5).

**Batch 4 — Yale OCS (Source 08)**  
Primary: [STEMConnect Technical Resume Sample](https://ocs.yale.edu/resources/stemconnect-technical-resume-sample/) (modified 31 Mar 2026). Followed: [Resume Formatting and Common Errors](https://ocs.yale.edu/resources/resume-formatting/) (live 404 as of 10 Sep 2026; Wayback used), [Writing Impactful Resume Bullets](https://ocs.yale.edu/resources/writing-impactful-resume-bullets/), [Resume Action Verbs](https://ocs.yale.edu/resources/resume-action-verbs/), [Big Interview](https://ocs.yale.edu/resources/big-interview/), [NACE competencies PDF](https://www.naceweb.org/uploadedfiles/files/2021/resources/nace-career-readiness-competencies-revised-apr-2021.pdf). Same OCS family: [Using AI In Your Job Search](https://ocs.yale.edu/channels/using-ai-job-search/), [Yale College Resume Templates](https://ocs.yale.edu/resources/ocs-resume-template/).

**Batch 5 — LinkedIn Top Content (Source 09)**  
Primary: [What to Highlight in a Tech Resume Format](https://www.linkedin.com/top-content/career/resume-formats-for-tech-jobs/what-to-highlight-in-a-tech-resume-format/). Followed sibling pages: [Essential Elements](https://www.linkedin.com/top-content/career/resume-formats-for-tech-jobs/essential-elements-of-a-tech-job-resume/), [How to Format a Software Engineer Resume for Quick Review](https://www.linkedin.com/top-content/career/resume-formats-for-tech-jobs/how-to-format-a-software-engineer-resume-for-quick-review/), [Why US Clients Prefer Short IT Resumes](https://www.linkedin.com/top-content/career/resume-formats-for-tech-jobs/why-us-clients-prefer-short-it-resumes/), plus search-level notes on [Key Sections](https://www.linkedin.com/top-content/career/resume-formats-for-tech-jobs/key-sections-to-include-in-a-tech-resume/) and [ATS-Friendly Formats](https://www.linkedin.com/top-content/career/resume-formats-for-tech-jobs/ats-friendly-resume-formats-for-tech-jobs/). Category hub: [Resume Formats for Tech Jobs](https://www.linkedin.com/top-content/career/resume-formats-for-tech-jobs/).

**Batch 6 — Harvard MCS (Source 10)**  
Primary: [Harvard College Guide to Creating a Strong Resume](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/) (published 11 Jul 2024; modified 13 Jul 2026). Followed: [bullet](https://careerservices.fas.harvard.edu/resources/bullet-point-resume-template/) and [paragraph](https://careerservices.fas.harvard.edu/resources/harvard-college-paragraph-resume-template/) templates, [AI for Resumes and Cover Letters](https://careerservices.fas.harvard.edu/ai-resumes-and-cover-letters/), [AI for Professional Development](https://careerservices.fas.harvard.edu/channels/ai-for-professional-development-and-exploration/), [Interstride](https://careerservices.fas.harvard.edu/resources/interstride/), templates hub [Create a Resume/CV or Cover Letter](https://careerservices.fas.harvard.edu/channels/create-a-resume-cv-or-cover-letter/) including [Tech](https://careerservices.fas.harvard.edu/resources/harvard-college-resume-example-tech/) and [Engineering](https://careerservices.fas.harvard.edu/resources/harvard-college-resume-example-engineering/) examples and [Big Resume](https://careerservices.fas.harvard.edu/resources/big-resume/). Resume 101 webinar is Harvard-login-walled.

**Batch 7 — r/EngineeringResumes hiring manager (Source 11)**  
Primary: [[12 YoE] Some long, direct advice in tech from a Hiring Manager](https://www.reddit.com/r/EngineeringResumes/comments/1hw10ms/12_yoe_some_long_direct_advice_in_tech_from_a/) (u/woodworksio, 7 Jan 2025; live post mod-removed for missing résumé image; text from Arctic Shift). Followed: earlier twin on [r/csMajors](https://www.reddit.com/r/csMajors/comments/1hvj2hj/long_direct_advice_from_a_hiring_manager/), OP comments, [How ATSs actually work](https://www.reddit.com/r/EngineeringResumes/comments/192hkg8/how_atss_actually_work_from_an_engineering_hiring/) (PhenomEng), sub wiki [templates](https://www.reddit.com/r/EngineeringResumes/wiki/resumetemplates/) / [software](https://www.reddit.com/r/EngineeringResumes/wiki/software/) / [checklist](https://www.reddit.com/r/EngineeringResumes/wiki/checklist/).

**Batch 8 — Penn Career Services (Source 12)**  
Primary: [Write a Resume/CV](https://careerservices.upenn.edu/channels/resume/). Followed: [4 Undergraduate Resume Templates](https://careerservices.upenn.edu/resources/career-services-resume-guide/) (Word pack modified 8 Sep 2026), [undergraduate samples](https://careerservices.upenn.edu/preparing-effective-resumes/undergraduates-student-resume-samples/) (CS + CompE), [action verbs](https://careerservices.upenn.edu/resources/career-services-resume-action-verbs/), [grad/postdoc 52-page guide](https://careerservices.upenn.edu/resources/resume-guide-for-graduate-students-and-postdocs/) (URL only; ~30 MB), [grad 2-pager](https://careerservices.upenn.edu/resources/resume-and-cover-letter-advice-for-grad-students-postdocs/), [master’s](https://careerservices.upenn.edu/masters-student-resume-samples/) and [PhD/postdoc](https://careerservices.upenn.edu/phd-postdoc-sample-resumes/) galleries, [Targeted Resume](https://careerservices.upenn.edu/resources/targeted-resume/) / [Jobscan](https://careerservices.upenn.edu/resources/jobscan/), [Optimizing Your Resume for AI Scanners](https://careerservices.upenn.edu/blog/2024/10/08/optimizing-your-resume-for-ai-scanners/) (Laura Brasch), [Write a Cover Letter](https://careerservices.upenn.edu/channels/cover-letters/). SharePoint “Resume Section Headers” is Penn-login-walled; LGBTQ+ guide 404.

**Batch 9 — ACI Learning Tech Academy (Source 13)**  
Primary: [The 2026 Tech Resume Guide for Breaking Into IT](https://www.acitechacademy.com/blog/struggling-to-get-your-tech-resume-noticed-here-s-how-to-land-interviews-in-2024/) (slug 2024; Wayback from 9 Sep 2024; live copy retitled for 2026). Followed on-page: [7 Tips for Getting Into IT With Zero Experience](https://www.acitechacademy.com/blog/7-tips-for-getting-into-it-with-zero-experience/), [5 IT Jobs You Can Get Without a Degree](https://www.acitechacademy.com/blog/5-it-jobs-you-can-get-without-a-degree/), [IT Career Services](https://www.acitechacademy.com/information-technology-career-services/). Same-site résumé siblings: [skills-focused resume](https://www.acitechacademy.com/blog/skill-focused-resume/), [Craft a Targeted IT Resume](https://www.acitechacademy.com/blog/craft-a-targeted-it-resume-a-preview-of-it-career-prep/), [Expert’s Guide / Karla Urbina Q&A](https://www.acitechacademy.com/blog/our-experts-guide-to-starting-a-career-in-it/). No sample files.

**Batch 10 — Emanate Technology (Source 14)**  
Primary: [How to Write a Stand-Out Tech CV](https://www.emanatetechnology.com.au/news/how-to-write-a-tech-resume-with-example) (29 Jan 2025). Followed: [resume template](https://www.emanatetechnology.com.au/resume-template) (Word, 2020 PM sample), [Jobscan ATS](https://www.jobscan.co/blog/ats-resume/), [Canberra in-demand skills](https://www.emanatetechnology.com.au/news/the-5-most-in-demand-skill-sets-in-the-canberra-tech-market) (2016), [why no interviews](https://www.emanatetechnology.com.au/news/why-am-i-not-getting-interviews) (Luca Francis), [red/green flags](https://www.emanatetechnology.com.au/news/how-to-hire-the-right-candidate-red-flags-to-avoid) (Mal Konfu), [redundancy 30-day plan](https://www.emanatetechnology.com.au/news/what-to-do-after-being-made-redundant), [AI in hiring](https://www.emanatetechnology.com.au/news/ai-in-recruitment-hiring-trends).

**Batch 11 — Rewriting the Code (Source 15)**  
Primary: [How to Write a Tech Resume](https://rewritingthecode.org/resources/member-resources/how-to-build-a-tech-resume/) (Allison Darhun; published 26 Aug 2025, modified 18 Feb 2026). Followed: Canva view-only template (`teamrtc.co/49swQnq`), [Google Docs pack](https://docs.google.com/document/d/1g4Jx62ZuBb3IJ1AiWL5SZd4A7qrbM-VVQ9oS3P6K-O4/edit) (Radha + Aesha examples), [How to Add Projects](https://rewritingthecode.org/resources/member-resources/how-to-add-projects-to-your-resume/), [What Are AI Skills?](https://rewritingthecode.org/resources/member-resources/what-are-ai-skills-how-to-show-recruiters-you-think-critically/). On-page “you may also like” stories skipped.

**Batch 12 — UT Austin CNS (Source 16)**  
Primary: [Strong Bullets for Technical Resumes](https://careerservices.cns.utexas.edu/resources/resumes/strong-bullets-technical-resumes). Followed section siblings: [overview](https://careerservices.cns.utexas.edu/resources/resumes), [templates](https://careerservices.cns.utexas.edu/resources/resumes/templates) (Technical + General Google Docs; Box Word/CS examples 404), [master resumes](https://careerservices.cns.utexas.edu/resources/resumes/master-resumes-and-cvs), [formatting](https://careerservices.cns.utexas.edu/resources/resumes/resume-formatting), [content](https://careerservices.cns.utexas.edu/resources/resumes/resume-content), [ATS](https://careerservices.cns.utexas.edu/resources/resumes/applicant-tracking-systems). Kickresume NDA link is dead.

**Batch 13 — Per Scholas (Source 17)**  
Primary: [How To Get A Job In Tech: Resume & Interview Tips](https://perscholas.org/news/how-to-land-your-first-job-in-tech-resume-and-interview-tips/) (Christel Grissett; 10 Mar 2024). On-page More News is not résumé. Same-site siblings: [7 Steps](https://perscholas.org/news/how-to-start-your-it-career/), [IT Expert](https://perscholas.org/news/how-to-become-an-information-technology-expert/), [ResumeBoost AI](https://perscholas.org/news/per-scholas-embraces-ai-to-enhance-alumni-career-success/), [Collins](https://perscholas.org/news/advice-for-grads-from-diahan-collins-career-advancement-expert/), [Matre](https://perscholas.org/news/alumni-corner-dave-matre-suggestions-to-consider-when-seeking-employment-opportunities/). No sample files.

**Batch 14 — Georgia Tech Career Center (Source 18)**  
Primary: [Undergraduate Resumes, Cover Letters, & Portfolios](https://career.gatech.edu/undergrad-job-search/resumes/). Followed: [Resume Career Guide](https://career.gatech.edu/files/2026/05/Career_Center_Resume_Guide-645d43267633e4df.pdf), [Cover Letter Guide](https://c14750.wpmucdn.com/5568/files/2026/05/GTCC_Career-Guide_V2-1.pdf), [Career Guides](https://career.gatech.edu/career-guides/), [Graduate Resumes](https://career.gatech.edu/graduate-job/resumes-cvs/) (checklist, CV vs résumé, GenAI toolkit, MS experienced sample), [CV Guides](https://career.gatech.edu/academic-job-search/cv-guides/) (URL only). College of Computing Word samples stored; first-year/transfer/non-CS majors skipped.

**Batch 15 — Mastercard Careers (Source 19)**  
Primary: [How to tailor your technology resume](https://careers.mastercard.com/us/en/blogarticle/how-to-tailor-your-technology-resume-for-the-job-you-want) (12 Jul 2023; Phenom widgets API). Same-site: [career transition](https://careers.mastercard.com/us/en/blogarticle/how-to-update-your-resume-for-a-career-transition), [students/grads](https://careers.mastercard.com/us/en/blogarticle/tips-for-students-and-graduates-applying-to-mastercard), [LinkedIn glow-up](https://careers.mastercard.com/us/en/blogarticle/linkedin-glowup-8-tips-for-a-profile-makeover), [AI guidelines](https://careers.mastercard.com/us/en/ai-guidelines), [interview tips](https://careers.mastercard.com/us/en/interview-tips), [key skills](https://careers.mastercard.com/us/en/key-skills-mastercard-looks-for-in-top-candidates-and-how-to-show-them-in-your-interview). No sample files.

**Batch 16 — Toptal Resume (Source 20)**  
Primary: [The Perfect Tech Resume in 2025](https://www.toptal.com/resume/career-center/the-perfect-tech-resume-in-2025-key-trends-ats-keywords-and-formatting-tips) (Tracie Close; published 7 Jul 2025). Followed: [SWE](https://www.toptal.com/resume/career-center/how-to-write-a-tech-resume-for-software-engineering-roles), [summary](https://www.toptal.com/resume/career-center/how-to-write-a-professional-resume-summary-a-guide-for-tech-professionals), [ATS screening](https://www.toptal.com/resume/career-center/from-ats-to-interview-ensuring-your-tech-resume-passes-automated-tech-screening), [mistakes](https://www.toptal.com/resume/career-center/top-tech-resume-mistakes-what-to-avoid-and-how-to-fix-them), [role misalignment](https://www.toptal.com/resume/career-center/why-most-tech-resumes-fail-target-role-misalignment). Checker CTA skipped. No sample files.

**Batch 17 — IGotAnOffer (Source 21)**  
Primary: [Tech Resume Examples](https://igotanoffer.com/blogs/tech/tech-resume-examples) (Tom Parry; published 24 Jul 2024, updated 13 Aug 2026). Followed: [SWE](https://igotanoffer.com/blogs/tech/software-engineer-resume-examples), [Google](https://igotanoffer.com/blogs/tech/google-resume-examples-tips), [senior SWE](https://igotanoffer.com/en/advice/senior-software-engineer-resume-examples), [keywords](https://igotanoffer.com/en/advice/software-engineer-resume-keywords), [EM](https://igotanoffer.com/blogs/tech/engineering-manager-resume), [TPM](https://igotanoffer.com/blogs/tech/technical-program-manager-resume), [Google How we hire](https://careers.google.com/how-we-hire/#step-your-resume). Samples stored under `assets/sample_resumes/igotanoffer/`. Review CTA skipped.

## Next sources

Add a new `NN_{short-name}.md` for each link, then append a row to the table above. Do not put extracted source content in this README. The **Critical identity** table above defines how contact/education must appear on every generated résumé; field *values* always come from the user’s data.
