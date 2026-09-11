#!/usr/bin/env python3
"""Download sample resume images/PDFs referenced from resume-guideline sources.

Used for UNC CS Tech Resume + CV Samples, MIT CommKit examples,
Tech Interview Handbook resume-guide graphics, Tiffany Jachja Medium
resume-article screenshots, the Yale OCS STEMConnect technical
resume Word template, Harvard MCS College resume/cover samples,
the r/EngineeringResumes wiki Google Docs template, Penn Career
Services resume-hub samples (undergrad Word pack, CS/CompE, SCO 2-pager),
the Emanate Technology AU recruiter Word CV example, the Rewriting
the Code Google Docs resume pack (Canva twin is view-only — not stored),
and UT Austin CNS Technical + General Google Docs templates.
Georgia Tech Career Center Resume Career Guide, Cover Letter Guide, CS Word
samples, MS experienced sample, and MS/PhD checklist are also stored here.
IGotAnOffer FAANG sample screenshots and the Karl SWE PDF template are stored
here. The ~30 MB Canva grad/postdoc guide is URL-only — do not add it here.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEST = REPO / "assets" / "sample_resumes"
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

DOWNLOADS = [
    {
        "url": "https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/Technical-Resume-Template-Updated-Summer-2026.png",
        "path": "unc-cs/cs-major-template-1_technical-resume-summer-2026.png",
        "source": "https://cs.unc.edu/student-life/career/tech-resume-samples/",
        "label": "UNC CS Major Resume Template #1 (preview image)",
    },
    {
        "url": "https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/ML-Focused-Technical-Resume-Template-Updated-Summer-2026.png",
        "path": "unc-cs/cs-major-template-2_ml-data-science-summer-2026.png",
        "source": "https://cs.unc.edu/student-life/career/tech-resume-samples/",
        "label": "UNC CS Major Resume Template #2 — Data Science + ML (preview image)",
    },
    {
        "url": "https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/MSCS-Resume-Updated-Summer-2026.png",
        "path": "unc-cs/mscs-resume-template-summer-2026.png",
        "source": "https://cs.unc.edu/student-life/career/tech-resume-samples/",
        "label": "UNC Master of Computer Science Resume Template (preview image)",
    },
    {
        "url": "https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/Pre-CS-Technical-Resume-Template-Updated-Summer-2026.png",
        "path": "unc-cs/pre-cs-technical-resume-template-summer-2026.png",
        "source": "https://cs.unc.edu/student-life/career/tech-resume-samples/",
        "label": "UNC Pre-CS Resume Template (preview image)",
    },
    {
        "url": "https://cs.unc.edu/wp-content/uploads/sites/1265/2026/07/Data-Science-Resume-Sample-Updated-Summer-2026.png",
        "path": "unc-cs/bs-data-science-resume-sample-summer-2026.png",
        "source": "https://cs.unc.edu/student-life/career/tech-resume-samples/",
        "label": "UNC B.S. in Data Science Resume Sample (preview image)",
    },
    {
        "url": "https://mitcommlab.mit.edu/eecs/wp-content/uploads/sites/6/2016/09/EECS_CommKit_CVResume_AAE1.png",
        "path": "mit-eecs-commkit/eecs-commkit-cv-resume-aae1.png",
        "source": "https://cs.unc.edu/student-life/career/tech-resume-samples/",
        "related": "https://mitcommlab.mit.edu/eecs/commkit/cvresume/",
        "label": "MIT EECS CommKit annotated CV example 1",
    },
    {
        "url": "https://mitcommlab.mit.edu/eecs/wp-content/uploads/sites/6/2016/09/eecs-resume-aae1.png",
        "path": "mit-eecs-commkit/eecs-resume-aae1.png",
        "source": "https://mitcommlab.mit.edu/eecs/commkit/cvresume/",
        "related": "https://cs.unc.edu/student-life/career/tech-resume-samples/",
        "label": "MIT EECS CommKit annotated 2-column resume example 1",
    },
    {
        "url": "https://www.techinterviewhandbook.org/assets/images/four-steps-to-create-a-software-engineer-resume-f730ad12a3b3623aa7d1cd763456af73.jpg",
        "path": "tech-interview-handbook/four-steps-to-create-a-software-engineer-resume.jpg",
        "source": "https://www.techinterviewhandbook.org/resume/",
        "label": "Tech Interview Handbook four-step SWE resume checklist infographic",
    },
    {
        "url": "https://www.techinterviewhandbook.org/social/resume.png",
        "path": "tech-interview-handbook/social-resume.png",
        "source": "https://www.techinterviewhandbook.org/resume/",
        "label": "Tech Interview Handbook resume-guide social/OG image (not a sample resume)",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*IGB1WiLbO-7-IHxA_1fRCQ.png",
        "path": "tiffany-jachja/01-skills-three-categories.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja skills example — 3 comma-separated categories (PM, infra, data/ML)",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*EFV2RC_Ech9zz9RMQ9HnSQ.png",
        "path": "tiffany-jachja/02-skills-table.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja skills example — 3-column Languages / Frameworks / Tools table",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:960/1*9_f7yRgRbgLZe3KWgGoDlQ.png",
        "path": "tiffany-jachja/03-skills-example.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja skills example — Project Management / Data Engineering / Data Analytics",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1042/1*ObOu5O1Zjtk_eNJ8UqiKhw.png",
        "path": "tiffany-jachja/04-skills-additional-examples.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja skills example — Data Analysis + Management (soft-skill category)",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1100/1*XdA6TnIqWTUoBxIkB2kaoA.png",
        "path": "tiffany-jachja/05-work-management-bullets.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja work example — Engineering Manager, Autodesk (author’s own bullets)",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:876/1*vvwIquxCcGO8Dkscvf-DmA.png",
        "path": "tiffany-jachja/06-work-internship-a.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja internship bullets — battery fabrication (partial framework)",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1126/1*lf0Vy8sTmJyitHdxLlfdSw.png",
        "path": "tiffany-jachja/07-work-internship-b.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja internship bullet — FDA HPC / Son of Grid Engine",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*UK_6qtfzdg11o5MUYY384w.png",
        "path": "tiffany-jachja/08-work-warehouse-learning-ambassador.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja non-tech work — Amazon warehouse Learning Ambassador",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1140/1*Wu_l6o2nHuo_PrS1r2TfrA.png",
        "path": "tiffany-jachja/09-work-gas-station-lead-cook.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja non-tech work — gas-station Director of Operations / lead cook",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*b-jLJ6S-WZaDt1rGAfctzA.png",
        "path": "tiffany-jachja/10-work-waste-coordinator.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja non-tech work — Amazon Regulated Waste Coordinator",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*MzQtlu1Yorcg3YScSp4mmg.png",
        "path": "tiffany-jachja/11-work-health-safety-specialist.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja career-switch work — Amazon Health & Safety Specialist targeting data roles",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1130/1*dJSCzmvn5TLjR-4ET57UUw.png",
        "path": "tiffany-jachja/12-project-example-1.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja project example — Population Density Database",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1190/1*gE-2O1s6iGMEU7M2N2_o3Q.png",
        "path": "tiffany-jachja/13-project-example-2.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja project example — Seq2Seq and Transformers",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1100/1*SnoXa63o2YQvQ4dWnEpKvA.png",
        "path": "tiffany-jachja/14-relevant-technical-experience.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja second experience section — GDG / Code Connector community roles",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:1006/1*3ujrb2mpp7Q_sHJMQWcWVQ.png",
        "path": "tiffany-jachja/15-linkedin-experience-a.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja LinkedIn overflow — Twitch streamer role",
    },
    {
        "url": "https://miro.medium.com/v2/resize:fit:996/1*u9f_92urkIBN_wDET7FZFQ.png",
        "path": "tiffany-jachja/16-linkedin-experience-b.png",
        "source": "https://tiffanyjachja.medium.com/the-elements-of-a-tech-resume-985888f35af6",
        "label": "Jachja LinkedIn overflow — DevOpsInstitute Ambassador",
    },
    {
        "url": "https://cdn.ocs.yale.edu/wp-content/uploads/sites/77/2022/10/Yale-College-Technical-Resume-Template.docx",
        "path": "yale-ocs/Yale-College-Technical-Resume-Template.docx",
        "source": "https://ocs.yale.edu/resources/stemconnect-technical-resume-sample/",
        "label": "Yale OCS STEMConnect / Yale College Technical Resume Word template",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2026/07/resume-sample.pdf",
        "path": "harvard-mcs/resume-sample.pdf",
        "source": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard MCS annotated Resume Sample (generic College)",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2026/07/resume-sample-thumb.png",
        "path": "harvard-mcs/resume-sample-thumb.png",
        "source": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard MCS Resume Sample thumbnail",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2026/07/category-sample.pdf",
        "path": "harvard-mcs/category-sample.pdf",
        "source": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard MCS optional category examples",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2026/07/category-sample-thumb.png",
        "path": "harvard-mcs/category-sample-thumb.png",
        "source": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard MCS optional category examples thumbnail",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2024/07/cover-letter-template.pdf",
        "path": "harvard-mcs/cover-letter-template.pdf",
        "source": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard MCS annotated cover-letter skeleton",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2024/07/page-8-e1720725726200.png",
        "path": "harvard-mcs/cover-letter-sample-preview.png",
        "source": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard MCS cover-letter sample preview image",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2024/07/College-resume-and-cover-letter-20246.png",
        "path": "harvard-mcs/bullet-template-preview.png",
        "source": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "related": "https://careerservices.fas.harvard.edu/resources/bullet-point-resume-template/",
        "label": "Harvard MCS bullet-point resume template preview",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2024/07/College-resume-and-cover-letter-20247.png",
        "path": "harvard-mcs/paragraph-template-preview.png",
        "source": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "related": "https://careerservices.fas.harvard.edu/resources/harvard-college-paragraph-resume-template/",
        "label": "Harvard MCS paragraph resume template preview",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2025/09/2025-template_bullet.docx",
        "path": "harvard-mcs/2025-template_bullet.docx",
        "source": "https://careerservices.fas.harvard.edu/resources/bullet-point-resume-template/",
        "related": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard College 2025 bullet-point resume Word template (no tables)",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2025/02/Accessible-MCS-Resume-Template-Bullet-Points.docx",
        "path": "harvard-mcs/Accessible-MCS-Resume-Template-Bullet-Points.docx",
        "source": "https://careerservices.fas.harvard.edu/resources/bullet-point-resume-template/",
        "related": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard MCS accessible bullet Word template (uses tables; ~3.4MB fonts)",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2025/09/2025-template_paragraph.docx",
        "path": "harvard-mcs/2025-template_paragraph.docx",
        "source": "https://careerservices.fas.harvard.edu/resources/harvard-college-paragraph-resume-template/",
        "related": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard College 2025 paragraph resume Word template (no tables)",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2025/02/Accessible-MCS-Resume-Template-Paragraph.docx",
        "path": "harvard-mcs/Accessible-MCS-Resume-Template-Paragraph.docx",
        "source": "https://careerservices.fas.harvard.edu/resources/harvard-college-paragraph-resume-template/",
        "related": "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/",
        "label": "Harvard MCS accessible paragraph Word template (uses tables; ~3.4MB fonts)",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2026/07/Harvard-College-CS-Resume-Example.pdf",
        "path": "harvard-mcs/Harvard-College-CS-Resume-Example.pdf",
        "source": "https://careerservices.fas.harvard.edu/resources/harvard-college-resume-example-tech/",
        "related": "https://careerservices.fas.harvard.edu/channels/create-a-resume-cv-or-cover-letter/",
        "label": "Harvard College Resume Example (Tech) — 3-page booklet, 1-page Calibri resume",
    },
    {
        "url": "https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2026/07/Harvard-College-Engineering-Example.pdf",
        "path": "harvard-mcs/Harvard-College-Engineering-Example.pdf",
        "source": "https://careerservices.fas.harvard.edu/resources/harvard-college-resume-example-engineering/",
        "related": "https://careerservices.fas.harvard.edu/channels/create-a-resume-cv-or-cover-letter/",
        "label": "Harvard College Resume Example (Engineering) — 3-page booklet, 1-page Calibri resume",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2026/09/Undergrad-Resume-Guide-with-4-Templates-2-2.docx",
        "path": "upenn-career-services/Undergrad-Resume-Guide-with-4-Templates.docx",
        "source": "https://careerservices.upenn.edu/resources/career-services-resume-guide/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn Career Services 4 undergraduate resume Word templates (modified 8 Sep 2026)",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2026/06/Sample_Resume_Undergrad_ComputerScience.pdf",
        "path": "upenn-career-services/Sample_Resume_Undergrad_ComputerScience.pdf",
        "source": "https://careerservices.upenn.edu/preparing-effective-resumes/undergraduates-student-resume-samples/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn undergrad Computer Science sample resume (Sofia B. Good)",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2026/06/Sample_Resume_Undergrad_ComputerScience.jpg",
        "path": "upenn-career-services/Sample_Resume_Undergrad_ComputerScience.jpg",
        "source": "https://careerservices.upenn.edu/preparing-effective-resumes/undergraduates-student-resume-samples/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn undergrad Computer Science sample preview image",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2026/06/Sample_Resume_Undergrad_ComputerEngineering.pdf",
        "path": "upenn-career-services/Sample_Resume_Undergrad_ComputerEngineering.pdf",
        "source": "https://careerservices.upenn.edu/preparing-effective-resumes/undergraduates-student-resume-samples/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn undergrad Computer Engineering sample resume (Patricia Venti)",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2026/06/Sample_Resume_Undergrad_ComputerEngineering.jpg",
        "path": "upenn-career-services/Sample_Resume_Undergrad_ComputerEngineering.jpg",
        "source": "https://careerservices.upenn.edu/preparing-effective-resumes/undergraduates-student-resume-samples/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn undergrad Computer Engineering sample preview image",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2021/09/SampleConsultingResume.pdf",
        "path": "upenn-career-services/SampleConsultingResume.pdf",
        "source": "https://careerservices.upenn.edu/preparing-effective-resumes/undergraduates-student-resume-samples/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn undergrad consulting sample resume (Matt Smith / M&T)",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2021/09/SampleResearchResume.pdf",
        "path": "upenn-career-services/SampleResearchResume.pdf",
        "source": "https://careerservices.upenn.edu/preparing-effective-resumes/undergraduates-student-resume-samples/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn undergrad research sample resume (Lee Bio)",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2022/08/Resume-Action-Verbs-2.pdf",
        "path": "upenn-career-services/Resume-Action-Verbs.pdf",
        "source": "https://careerservices.upenn.edu/resources/career-services-resume-action-verbs/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn Career Services resume action-verbs PDF",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2025/07/Resume-cover-letter-advice-grad-students-postdocs.pdf",
        "path": "upenn-career-services/Resume-cover-letter-advice-grad-students-postdocs.pdf",
        "source": "https://careerservices.upenn.edu/resources/resume-and-cover-letter-advice-for-grad-students-postdocs/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn grad/postdoc resume + cover letter 2-pager (SCO bullets)",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2026/06/Bioengineering-revised.pdf",
        "path": "upenn-career-services/PhD-Bioengineering-resume.pdf",
        "source": "https://careerservices.upenn.edu/phd-postdoc-sample-resumes/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn PhD Bioengineering 2-page industry resume sample",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2026/06/STEM-Postdoc-two-page.pdf",
        "path": "upenn-career-services/PhD-STEM-Postdoc-two-page.pdf",
        "source": "https://careerservices.upenn.edu/phd-postdoc-sample-resumes/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn STEM postdoc 2-page resume sample",
    },
    {
        "url": "https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2026/06/CBE-one-page-consulting.pdf",
        "path": "upenn-career-services/PhD-CBE-one-page-consulting.pdf",
        "source": "https://careerservices.upenn.edu/phd-postdoc-sample-resumes/",
        "related": "https://careerservices.upenn.edu/channels/resume/",
        "label": "Penn CBE PhD 1-page consulting resume sample",
    },
    {
        "url": "https://irp.cdn-website.com/38665073/files/uploaded/Emanate-Technology-Resume-Example_%281%29.docx",
        "path": "emanate-technology/Emanate-Technology-Resume-Example.docx",
        "source": "https://www.emanatetechnology.com.au/resume-template",
        "related": "https://www.emanatetechnology.com.au/news/how-to-write-a-tech-resume-with-example",
        "label": "Emanate Technology AU IT CV Word example (John Smith / ICT PM, 2020, 4 pages)",
    },
    {
        "url": "https://career.gatech.edu/files/2026/05/Career_Center_Resume_Guide-645d43267633e4df.pdf",
        "path": "gatech-career-center/Career_Center_Resume_Guide.pdf",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech Career Center Resume Career Guide (May 2026, 16 pages)",
    },
    {
        "url": "https://c14750.wpmucdn.com/5568/files/2026/05/GTCC_Career-Guide_V2-1.pdf",
        "path": "gatech-career-center/GTCC_Cover_Letter_Guide.pdf",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "related": "https://career.gatech.edu/career-guides/",
        "label": "Georgia Tech Cover Letter Career Guide (May 2026, 16 pages)",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/Resume-101-.docx",
        "path": "gatech-career-center/general-resume-template-Resume-101.docx",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech general undergrad resume fill-in (Resume 101)",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/CS-Sample-Resume.docx",
        "path": "gatech-career-center/cs-sample-resume-1.docx",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech College of Computing CS sample resume 1",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/CS-Sample-Resume-2.docx",
        "path": "gatech-career-center/cs-sample-resume-2.docx",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech College of Computing CS sample resume 2",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/CS-and-Analytics-Sample-Resume.docx",
        "path": "gatech-career-center/cs-and-analytics-sample-resume.docx",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech CS and Analytics sample resume",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/CS-and-Data-Science-Resume.docx",
        "path": "gatech-career-center/cs-and-data-science-resume.docx",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech CS and Data Science sample resume",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/IAC_Computational-Media.docx",
        "path": "gatech-career-center/computational-media-resume.docx",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech Computational Media sample resume",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/Cover-Letter-Outline-1.docx",
        "path": "gatech-career-center/cover-letter-outline.docx",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech cover letter outline",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/Full-time-cover-letter-George-Burdell.docx",
        "path": "gatech-career-center/full-time-cover-letter-george-burdell.docx",
        "source": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech full-time cover letter sample (George Burdell)",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/Resume-VS.-Curriculum-Vitae-CV.pdf",
        "path": "gatech-career-center/cv-vs-resume.pdf",
        "source": "https://career.gatech.edu/graduate-job/resumes-cvs/",
        "related": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech resume vs CV guide",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/ResumeChecklistGrad-2023-FINAL.pdf",
        "path": "gatech-career-center/ms-phd-resume-checklist.pdf",
        "source": "https://career.gatech.edu/graduate-job/resumes-cvs/",
        "related": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech MS/PhD resume checklist",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/GenAI-Resume-Toolkit-for-PhDs-Fall-2025.pdf",
        "path": "gatech-career-center/genai-resume-toolkit-phds.pdf",
        "source": "https://career.gatech.edu/graduate-job/resumes-cvs/",
        "related": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech GenAI 8 prompts for PhD resumes (Sep 2025)",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/MS-Resume-Online-Master-Updated.docx",
        "path": "gatech-career-center/ms-resume-online-experienced.docx",
        "source": "https://career.gatech.edu/graduate-job/resumes-cvs/",
        "related": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech OMS / experienced professional MS resume sample (Mary Buzz)",
    },
    {
        "url": "https://career.gatech.edu/files/2026/06/Georgia_Tech_PhD_2Page_Resume_Sample.pdf",
        "path": "gatech-career-center/phd-two-page-resume-sample.pdf",
        "source": "https://career.gatech.edu/graduate-job/resumes-cvs/",
        "related": "https://career.gatech.edu/undergrad-job-search/resumes/",
        "label": "Georgia Tech PhD two-page resume sample (Taylor Jacket)",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDE_tresume_example_part_1.png",
        "path": "igotanoffer/01-amazon-sde-sunil-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.1 Amazon Senior SDE (Sunil) page 1",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDE__resume_example_part_2.png",
        "path": "igotanoffer/01-amazon-sde-sunil-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.1 Amazon Senior SDE (Sunil) page 2",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDM_tech_resume_example_part_1.png",
        "path": "igotanoffer/02-amazon-sdm-k-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.2 Amazon SDM (K) page 1 of 4 — they say cut to 2 pages",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDM_tech_resume_example_part_2.png",
        "path": "igotanoffer/02-amazon-sdm-k-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.2 Amazon SDM (K) page 2 of 4",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDM_tech_resume_example_part_3.png",
        "path": "igotanoffer/02-amazon-sdm-k-p3.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.2 Amazon SDM (K) page 3 of 4",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDM_tech_resume_example_part_4.png",
        "path": "igotanoffer/02-amazon-sdm-k-p4.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.2 Amazon SDM (K) page 4 of 4",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Ana_P_cropped_part_1.png",
        "path": "igotanoffer/03-google-swe-ana-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.3 Google SWE fresher (Ana) page 1 — education/projects first",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Ana_P_cropped_part_2.png",
        "path": "igotanoffer/03-google-swe-ana-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.3 Google SWE fresher (Ana) page 2",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Meta_EM_tech_resume_example.png",
        "path": "igotanoffer/04-meta-em-dario.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.4 Meta EM (Dario) 1-pager — closest analog for experienced SWE density",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/John_Zhao_resume_1.png",
        "path": "igotanoffer/05-meta-em-james-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.5 Meta EM (James) page 1 of 5 — they say condense",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/John_Zhao_resume_2.png",
        "path": "igotanoffer/05-meta-em-james-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.5 Meta EM (James) page 2 of 5",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/John_Zhao_resume_3.png",
        "path": "igotanoffer/05-meta-em-james-p3.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.5 Meta EM (James) page 3 of 5",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/John_Zhao_resume_4.png",
        "path": "igotanoffer/05-meta-em-james-p4.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.5 Meta EM (James) page 4 of 5",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/John_Zhao_resume__5.png",
        "path": "igotanoffer/05-meta-em-james-p5.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.5 Meta EM (James) page 5 of 5",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Anshul_tech_resume_guide_part_1.png",
        "path": "igotanoffer/06-twitter-em-anshul-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.6 Twitter/X EM (Anshul) page 1",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Anshul_tech_resume_guide_part_2.png",
        "path": "igotanoffer/06-twitter-em-anshul-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.6 Twitter/X EM (Anshul) page 2",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Walmart_Deliveroo_EM_resume_example_part_1.png",
        "path": "igotanoffer/07-walmart-deliveroo-em-biswajit-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.7 Walmart/Deliveroo EM (Biswajit) page 1 of ~1.5",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Walmart_Deliveroo_EM_resume_example_part_2.png",
        "path": "igotanoffer/07-walmart-deliveroo-em-biswajit-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.7 Walmart/Deliveroo EM (Biswajit) page 2 of ~1.5",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Tech_example_resume_6_part_1.png",
        "path": "igotanoffer/08-google-tpm-nadia-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.8 Google TPM (Nadia) page 1",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Tech_example_resume_6_part_2..png",
        "path": "igotanoffer/08-google-tpm-nadia-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.8 Google TPM (Nadia) page 2 (CDN name has trailing period)",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Tech_example_resume_6_part_3.png",
        "path": "igotanoffer/08-google-tpm-nadia-p3.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.8 Google TPM (Nadia) page 3",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Google_front-end_developer_tech_resume_example_part_1.png",
        "path": "igotanoffer/09-google-frontend-lana-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.9 Google front-end (Lana) page 1 — they say add impact metrics",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Google_front-end_developer_tech_resume_example_part_2.png",
        "path": "igotanoffer/09-google-frontend-lana-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.9 Google front-end (Lana) page 2",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Crunchyroll_tech_resume_example_part_1.png",
        "path": "igotanoffer/10-crunchyroll-android-sam-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.10 Crunchyroll Senior Android (Sam) page 1 — skills at top",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Crunchyroll_tech_resume_example_part_2.png",
        "path": "igotanoffer/10-crunchyroll-android-sam-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.10 Crunchyroll Senior Android (Sam) page 2",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Audible_SWE_tech_resume_example_part_1.png",
        "path": "igotanoffer/11-audible-ios-jerry-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.11 Audible iOS (Jerry) page 1",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Audible_SWE_tech_resume_example_part_2.png",
        "path": "igotanoffer/11-audible-ios-jerry-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.11 Audible iOS (Jerry) page 2",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDM_expert_tech_resume_example_pt_1.png",
        "path": "igotanoffer/12-amazon-sdm-amar-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.12 Amazon SDM coach (Amar) page 1 — 1-line bullets, OSS",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDM_expert_tech_resume_example_pt_2.png",
        "path": "igotanoffer/12-amazon-sdm-amar-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.12 Amazon SDM coach (Amar) page 2",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDM_expert_tech_resume_example_pt_3.png",
        "path": "igotanoffer/12-amazon-sdm-amar-p3.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.12 Amazon SDM coach (Amar) page 3",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Amazon_SDM_expert_tech_resume_example_pt_4.png",
        "path": "igotanoffer/12-amazon-sdm-amar-p4.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer ex.12 Amazon SDM coach (Amar) page 4",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Screenshot_2023-08-10_at_12-52-27_Tech_example_resume_SWE_.docx_102.png",
        "path": "igotanoffer/karl-swe-template-screenshot.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer Karl imaginary mid-level SWE template screenshot",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/course/files/Tech_example_resume_SWE_.docx.pdf",
        "path": "igotanoffer/karl-swe-template.pdf",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer Karl SWE template PDF (same file as SWE/keywords pages)",
    },
    {
        "url": "https://lh7-rt.googleusercontent.com/docsz/AD_4nXd9P6IurWAtmWZzjx-P-ZbIXghHSGgDR_UDeKQkrcSTZh8CIzJ0-4dTq8Y1C2L8ae1syLYW-dgpxOt3pL4-U1zqB13EDMj212VSbQWzOz9cVsk9yMtptc30vEWPTlSXZhedksP1KrGeyhGgQcgG63PEXCs?key=DO7NWXj9CneCiYaimqZqSw",
        "path": "igotanoffer/cody-nontraditional-header.png",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "Cody H. non-traditional two-summary header (Google Docs hosted; may expire)",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/CACHE/images/blog-articles/content-images/Sahand_Saba_Resume/862bf4152ad402192de8edd17620c325.webp",
        "path": "igotanoffer/swe-sahand-google-l5.webp",
        "source": "https://igotanoffer.com/blogs/tech/software-engineer-resume-examples",
        "related": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer SWE sibling — Sahand Saba Google L5 (whitespace + verbs; thin metrics)",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/swe_2.png",
        "path": "igotanoffer/swe-extra-sunil-style-p1.png",
        "source": "https://igotanoffer.com/blogs/tech/software-engineer-resume-examples",
        "related": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer SWE sibling extra — street address + telemetry bullet (Sunil-like; don’t copy address)",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/swe_2.1.png",
        "path": "igotanoffer/swe-extra-sunil-style-p2.png",
        "source": "https://igotanoffer.com/blogs/tech/software-engineer-resume-examples",
        "related": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer SWE sibling extra page 2",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Senior_SWE_Resume_Template_1.png",
        "path": "igotanoffer/senior-swe-template-p1.png",
        "source": "https://igotanoffer.com/en/advice/senior-software-engineer-resume-examples",
        "related": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer senior SWE template page 1",
    },
    {
        "url": "https://d3no4ktch0fdq4.cloudfront.net/public/blog-articles/content-images/Senior_SWE_Resume_Template_2.png",
        "path": "igotanoffer/senior-swe-template-p2.png",
        "source": "https://igotanoffer.com/en/advice/senior-software-engineer-resume-examples",
        "related": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "label": "IGotAnOffer senior SWE template page 2",
    },
]

GOOGLE_DOCS = [
    {
        "id": "1PJUSoH2h7yOo2EgUX2CMzBFnIVEVlyyFg-igl9fXGdY",
        "path": "unc-cs/cs-major-template-1_technical-resume-summer-2026.pdf",
        "label": "UNC CS Major Resume Template #1 (Google Docs export)",
    },
    {
        "id": "11Dqv4UMeLE15T1h97SDaK0ghDD07lxfIkGPHQj89nCY",
        "path": "unc-cs/cs-major-template-2_ml-data-science-summer-2026.pdf",
        "label": "UNC CS Major Resume Template #2 — Data Science + ML (Google Docs export)",
    },
    {
        "id": "1HUhyYwbJ73OA1eD5gtAYEVtuV9ZMzHIf_brZMxyflTQ",
        "path": "unc-cs/mscs-resume-template-summer-2026.pdf",
        "label": "UNC Master of Computer Science Resume Template (Google Docs export)",
    },
    {
        "id": "1T5vx1w4Bdb8H45or0i0hz3bDGybMANXc_KJRQ9NjHpo",
        "path": "unc-cs/pre-cs-technical-resume-template-summer-2026.pdf",
        "label": "UNC Pre-CS Resume Template (Google Docs export)",
    },
    {
        "id": "1sKIl4BCVBldWkoA0M-_CK-6HdPnKWVhB3Uq_YmL-4BI",
        "path": "unc-cs/bs-data-science-resume-sample-summer-2026.pdf",
        "label": "UNC B.S. in Data Science Resume Sample (Google Docs export)",
        "source": "https://cs.unc.edu/student-life/career/tech-resume-samples/",
    },
    {
        "id": "1EujuYFWxVXZ2PUaJ2uizvK5raMoMsz1KMys-UYpUSk4",
        "path": "harvard-mcs/bullet-template-gdoc.pdf",
        "label": "Harvard MCS bullet-point resume template (Google Docs export)",
        "source": "https://careerservices.fas.harvard.edu/resources/bullet-point-resume-template/",
    },
    {
        "id": "1Gv7ACYJIrNC2TRPfCqjH8406JcKru9SfiRcJ9i-Ecwk",
        "path": "harvard-mcs/paragraph-template-gdoc.pdf",
        "label": "Harvard MCS paragraph resume template (Google Docs export)",
        "source": "https://careerservices.fas.harvard.edu/resources/harvard-college-paragraph-resume-template/",
    },
    {
        "id": "1MBvhATv8y-ESORopRoLSZ3f3HjkM_Qa_f8fIHAEqgnI",
        "path": "engineering-resumes-reddit/wiki-google-docs-template.pdf",
        "label": "r/EngineeringResumes wiki Google Docs resume template (export)",
        "source": "https://www.reddit.com/r/EngineeringResumes/wiki/resumetemplates/",
        "related": "https://www.reddit.com/r/EngineeringResumes/comments/1hw10ms/12_yoe_some_long_direct_advice_in_tech_from_a/",
    },
    {
        "id": "1g4Jx62ZuBb3IJ1AiWL5SZd4A7qrbM-VVQ9oS3P6K-O4",
        "path": "rewriting-the-code/rtc-google-docs-template.pdf",
        "label": "Rewriting the Code Google Docs resume pack (Radha Gulhane + Aesha Kothari examples)",
        "source": "https://rewritingthecode.org/resources/member-resources/how-to-build-a-tech-resume/",
        "related": "https://docs.google.com/document/d/1g4Jx62ZuBb3IJ1AiWL5SZd4A7qrbM-VVQ9oS3P6K-O4/edit",
    },
    {
        "id": "13mYfcRHvJkgUxf0B3SXDNud2BFI5dekK_Ik9GEdY9ck",
        "path": "ut-austin-cns/cns-technical-resume-template.pdf",
        "label": "UT Austin CNS Technical Resume Google Docs template (CS/DS intern fill-in)",
        "source": "https://careerservices.cns.utexas.edu/resources/resumes/templates",
        "related": "https://careerservices.cns.utexas.edu/resources/resumes/strong-bullets-technical-resumes",
    },
    {
        "id": "1O8cB71F39Ptp57M7Ml7tmXfV4aFs3wfoH8qw6FqWzs4",
        "path": "ut-austin-cns/cns-general-resume-template.pdf",
        "label": "UT Austin CNS General Resume Google Docs template",
        "source": "https://careerservices.cns.utexas.edu/resources/resumes/templates",
        "related": "https://careerservices.cns.utexas.edu/resources/resumes/strong-bullets-technical-resumes",
    },
    {
        "id": "1cs26cHshdDojVC-ff-A2r3J7b6uSrM-7",
        "path": "igotanoffer/karl-swe-template-gdoc.pdf",
        "label": "IGotAnOffer Karl SWE template (Google Docs copy export)",
        "source": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
        "related": "https://docs.google.com/document/d/1cs26cHshdDojVC-ff-A2r3J7b6uSrM-7/copy",
    },
    {
        "id": "1oWnJjRTEnVTuZdxeccplt42NNIdU5sOo8nD2GjbDaxw",
        "path": "igotanoffer/senior-swe-template-gdoc.pdf",
        "label": "IGotAnOffer senior SWE template (Google Docs export)",
        "source": "https://igotanoffer.com/en/advice/senior-software-engineer-resume-examples",
        "related": "https://igotanoffer.com/blogs/tech/tech-resume-examples",
    },
]


def curl(url: str, dest: Path) -> tuple[int, str]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            "curl",
            "-sL",
            "-A",
            USER_AGENT,
            "-o",
            str(dest),
            "-w",
            "%{http_code} %{content_type}",
            url,
        ],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip()


def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    manifest = []
    for item in DOWNLOADS:
        dest = DEST / item["path"]
        code, meta = curl(item["url"], dest)
        size = dest.stat().st_size if dest.exists() else 0
        print(f"img  {item['path']}: curl={code} {meta} bytes={size}")
        manifest.append({**item, "http_meta": meta, "bytes": size, "ok": size > 1000})

    for item in GOOGLE_DOCS:
        dest = DEST / item["path"]
        url = f"https://docs.google.com/document/d/{item['id']}/export?format=pdf"
        code, meta = curl(url, dest)
        size = dest.stat().st_size if dest.exists() else 0
        # Google sometimes returns HTML login/copy pages.
        kind = dest.read_bytes()[:8] if dest.exists() else b""
        is_pdf = kind.startswith(b"%PDF")
        if not is_pdf and dest.exists():
            dest.unlink()
            size = 0
        print(f"pdf  {item['path']}: curl={code} {meta} pdf={is_pdf} bytes={size}")
        manifest.append(
            {
                **item,
                "url": url,
                "source": item.get(
                    "source",
                    "https://cs.unc.edu/student-life/career/tech-resume-samples/",
                ),
                "http_meta": meta,
                "bytes": size,
                "ok": is_pdf,
            }
        )

    (DEST / "download_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(f"Wrote {DEST / 'download_manifest.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
