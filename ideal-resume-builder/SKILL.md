---
name: ideal-resume-builder
description: Build a completely optimized, fictional "ideal" resume for a target job description under the name "Xianglong Tang". Employs creative, highly relevant experience, projects, skills, and education to match all JD requirements 100%. Produces (1) a summary of the engineered ideal profile, (2) the generated PDF path, and (3) a list of how each engineered element aligns with the JD.
---

# Ideal Resume Builder

Construct a fictional "perfect" resume for a given job description to demonstrate what the ideal candidate profile looks like. Optimize every section (summary, skills, experience, projects, and education) to map 100% to all required and preferred qualifications.

## Inputs
- A job description: either a URL (fetch it) or pasted text.
- Candidate Name: Xianglong Tang (non-negotiable).

## Operating principles
1. **100% alignment.** Engineer the candidate's career history, education, skills, and projects to perfectly match the JD's requirements, nice-to-haves, stack, and company culture.
2. **Prestige and high impact.** Fictional experiences should be at leading companies in the relevant industry (e.g., SpaceX/NASA/Rocket Lab for aerospace, Google/Meta/Stripe for tech, Jane Street/Citadel for trading).
3. **One page.** Keep the layout compact and cleanly formatted. If content overflows, shorten the descriptions. Target body font 9pt, name 20pt.
4. **Header constraints.** The contact header must be kept minimal: name, email, phone, and work authorization status (e.g., U.S. Citizen). No relocation-ready or current location details.
5. **Consistent past-tense styling.** All experience bullet points must be grammatically correct and consistent in the past tense (e.g., 'Designed', 'Built', 'Implemented') for all roles, including the current one, to maintain professional consistency.

## Procedure
1. **Acquire the JD.** Fetch the URL or read the pasted text. Extract: company, role, hard requirements, preferred skills, tools, and cultural themes.
2. **Design the Profile.** Determine:
   - Fictional past employers, job titles, and dates.
   - Perfect degree(s) and universities (e.g., Stanford, MIT, Cornell).
   - Fictional projects that mirror the exact systems or products the company builds.
   - Comprehensive skills list covering all key technologies in the JD.
3. **Draft the Resume JSON.** Create a configuration containing:
   - `name`: "Xianglong Tang"
   - `contact`: `"xianglong.tang@gmail.com&nbsp;&nbsp;\|&nbsp;&nbsp;732-555-0199&nbsp;&nbsp;\|&nbsp;&nbsp;U.S. Citizen"` (or other relevant authorization)
   - `company_slug`: Company name
   - `summary`: Optimized hook matching the role's core theme
   - `skills_html`: HTML-formatted skills front-loading JD requirements
   - `experience`: 2-3 tailored corporate roles with bullet points in the past tense
   - `projects`: 2-3 highly relevant projects
   - `education`: Tailored university degree and achievements
4. **Build the PDF.** Write the JSON override to a file and run `scripts/build_resume.py` passing the JSON file.
5. **Verify.** Confirm the generated PDF is exactly one page and has correct formatting/tenses.
6. **Report.** Output the engineered profile summary, the PDF path, and the alignment map.

## Outputs
1. Fictional Profile Summary.
2. `output/Xianglong_Tang_Ideal_Resume_<Company>.pdf`.
3. Alignment Map showing how the fictional components target the JD.
