---
name: resume-tailor
description: Tailor Randy Tang's master resume to a specific job description and emit a clean one-page PDF. Use when given a job posting URL or pasted JD and asked to customize, tailor, or adapt the resume, or to assess fit for a role. Produces (1) an honest fit assessment, (2) a tailored resume PDF, (3) a list of every change and why, (4) a gap-closing project suggestion.
---

# Resume Tailor

Tailor a master resume to one job description. Optimize ordering, emphasis, and wording to match what the JD actually requires.

## Inputs
- A job description: either a URL (fetch it) or pasted text.
- `master/resume.json` — structured source of truth (facts the agent reasons over).
- `master/resume_master.md` — human-readable master (for reference / quick edits).

## Operating principles 
1. **Never fabricate.** No invented tools, metrics, titles, or domains. If the JD wants
   something the candidate lacks, surface it as a *gap*, not a claim. Reframing real work
   in the JD's vocabulary is fine; inventing experience is not.
2. **Be skeptical and objective.** Lead with an honest fit assessment, including
   disqualifiers (e.g. work authorization / sponsorship, on-site requirement, seniority
   mismatch) BEFORE doing any tailoring. A great resume can't fix an ineligible candidate.
3. **One page.** If content overflows, cut the least-relevant items — do not shrink to
   illegible font. Target body font 9pt, name 20pt.
4. **Mark uncertain claims.** Anything an interviewer could probe and find thin (e.g. a
   secondary language, a shallow side project) must be hedged accurately, not inflated.
5. **Show your work.** End with a changelog: every change mapped to a JD requirement.
6. **Consistent past-tense styling.** All experience bullet points must be grammatically
   correct and consistent in tense, using past-tense verbs (e.g., 'Designed', 'Built',
   'Implemented') for all roles, including the current one, to maintain professional consistency.
7. **Keyword matching.** Reframe real experience using exact keywords and vocabulary from the
   job description (e.g., specific methodologies, system paradigms, or tools) where the underlying
   facts support it.

## Procedure
1. **Acquire the JD.** If a URL, fetch it. Extract: title, company, location, comp,
   work-authorization/sponsorship notes, hard requirements ("What You Bring"/"Required"),
   nice-to-haves, and the recurring themes/keywords.
2. **Fit assessment.** Using `scripts/fit_rubric.md`, write a candid assessment:
   genuine strengths (mapped to JD), real weaknesses/gaps, and any hard disqualifiers.
   If a disqualifier exists (no sponsorship + candidate needs it; on-site in a city the
   candidate won't relocate to), say so plainly and ask whether to proceed.
3. **Plan the tailoring.** Decide ordering and emphasis:
   - Reorder sections/bullets so the most JD-relevant content is highest.
   - Rewrite bullets in the JD's vocabulary where the underlying fact supports it.
   - Reorder projects so domain-relevant ones lead (e.g. trading firm -> market projects).
   - Add a 3-4 line summary tuned to the role's core theme.
   - Build a skills line that front-loads JD-matched skills; hedge thin ones honestly.
4. **Build the PDF.** Write a JSON override to `output/<company>_override.json` containing
   only the fields that differ from the defaults derived from `master/resume.json` (e.g.
   `company_slug`, `summary`, `skills_html`, reordered `experience`/`projects`). The build
   script deep-merges the override onto the base. Run:
   `python3 resume-tailor/scripts/build_resume.py resume-tailor/output/<company>_override.json`
5. **Verify.** Confirm the PDF is exactly one page with no fabricated content.
   Use `pdftotext -layout` if available; otherwise fall back to reading the PDF
   via `read` tool or counting `/Type /Page` markers in the raw bytes with Python.
   Check: one page, no overflow, no garbled glyphs, contact line intact.
6. **Suggest a gap-closing project.** Based on the fit assessment's real weaknesses,
   propose one concrete side project that would close the biggest gaps. Be specific:
   name the tools/frameworks from the JD the project should use, describe what it builds,
   and explain which gaps it addresses. The project should be achievable in 1–2 weekends,
   demonstrable (deployable or has a public repo), and directly relevant to the role.
   If the candidate is already a strong fit with no significant gaps, say so and skip.
7. **Track the application.** Run `scripts/track_application.py` with the company, role,
   verdict, recommended action, PDF filename, JD URL, and a short notes string summarizing
   key gaps. This appends to `output/applications.json` for a single view of all tailoring runs.
8. **Report.** Output the fit assessment, the PDF path, the changelog, and the project suggestion.

## Checklist (run before delivering)
- [ ] Every bullet traces to something in `resume.json`.
- [ ] No outrageous claims or exaggerations; hedged where appropriate.
- [ ] Secondary/weak skills are hedged (e.g. "Java (fundamentals)"), not stated as fluency.
- [ ] Disqualifiers (sponsorship, location, seniority) surfaced, not buried.
- [ ] Result is exactly one page.
- [ ] Header contains no relocation status or location-ready details (keep header minimal).
- [ ] Every experience bullet point is grammatically correct and consistent in the past tense.
- [ ] Job description keywords are integrated accurately where facts align.

## Outputs
1. Fit assessment (strengths / gaps / disqualifiers).
2. `output/<Name>_Resume_<Company>.pdf`.
3. Changelog mapping each change to a JD requirement.
4. Gap-closing project suggestion (specific tools, what to build, which gaps it fills).
5. Updated `output/applications.json` tracker entry.
