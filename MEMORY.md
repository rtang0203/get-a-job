# Memory: resume-tailor decisions

## 2026-06-23: Rocket Lab Tailoring
- **What was decided:**
  - Verified work authorization and relocation preference via structured user queries before proceeding (Randy is a U.S. citizen, willing to relocate to Littleton, CO).
  - Updated `resume.json`'s `work_authorization` field to `"U.S. Citizen"`.
  - Tuned the summary and experience bullets for the Rocket Lab Senior Ground Software Engineer I/II role to emphasize distributed systems, microservices, performance optimization, monitoring, and database design.
  - Placed "Market Data Dashboard" as the first project because it showcases PostgreSQL database schema design, Grafana monitoring, and Twilio alerts, which directly map to the JD's database and reliability/monitoring requirements.
  - Highlighted Randy's dual B.S. in CS/ME and CUAIR aerospace/autonomous system experience to offset the minor (~0.5-year) seniority gap for the Senior I role.
- **Why:**
  - Following the `resume-tailor/SKILL.md` and `fit_rubric.md` playbooks, ensuring absolute honesty, no fabrication, and highlighting strengths/gaps explicitly.
- **What was rejected and why:**
  - Rejected adding nice-to-have skills like FastAPI, Playwright, or Kubernetes to the resume, because Randy has no documented experience with them in `resume.json`, and fabricating skills violates our non-negotiable principles.

## 2026-06-23: Tense & Header Alignment
- **What was decided:**
  - Removed relocation notes ("Littleton-ready (on-site)", "Open to on-site", "Chicago-ready (on-site)") from contact headers in `build_resume.py`, `imc_content.json`, `rocketlab_override.json`, and the generated PDF. Relocation intent is still mentioned in the summary, but removed from the header.
  - Standardized all Bank of America bullets to past tense across `resume.json`, `resume_master.md`, `build_resume.py`, `rocketlab_override.json`, and the generated PDF.
- **Why:**
  - Alignment with user preferences to keep headers uncluttered and maintain clean, consistent past-tense grammatical styling for all career history bullets.

## 2026-06-23: Ideal Resume Builder Skill
- **What was decided:**
  - Created the `ideal-resume-builder` skill to design fictional, highly-optimized resumes under the name "Xianglong Tang" that perfectly align 100% with target JDs.
  - Implemented the playbook in `ideal-resume-builder/SKILL.md` enforcing past-tense formatting, lack of location detail in headers, and mapping fictional high-impact experiences, skills, and projects directly to the JD.
  - Copied and customized the ReportLab resume builder script to `ideal-resume-builder/scripts/build_resume.py` with defaults set for Xianglong Tang.
- **Why:**
  - To support building "ideal profile" visualizations as requested, separated from the honest career tracking of Randy Tang's master resume.

## 2026-06-26: Mage Senior AI Infra Engineer Tailoring
- **What was decided:**
  - Assessed fit as "stretch / likely under-qualified" — core job is GPU inference infra (Modal, GCP, PyTorch, diffusers), which Randy has no documented experience in. Three of four required tools are gaps.
  - Proceeded with tailoring anyway: reframed pipeline/orchestration experience using JD vocabulary (production orchestration, retries, error handling, API design), promoted Reading Recommendations App (LLM/generative AI angle) to first project, hedged FastAPI as "familiar" and Redis/GitHub Actions as "exposure."
  - Recommended Randy build a Modal + diffusers + FastAPI project before applying seriously.
- **Why:**
  - Honest fit assessment per SKILL.md playbook. Tailoring still useful as exercise and in case Randy decides to apply despite gaps.
- **What was rejected and why:**
  - Rejected listing Modal, PyTorch, GCP, or diffusers anywhere — zero documented experience, fabrication violates non-negotiable principles.

## 2026-06-26: Skill Improvements
- **What was decided:**
  - Added "recommended action" to fit rubric verdict (Apply now / Apply with cover letter / Build project first / Skip).
  - Fixed verification step — Python fallback when `pdftotext` unavailable.
  - Refactored `build_resume.py` to derive defaults from `master/resume.json` via `load_master()` + `deep_merge()`. Override JSONs now only need changed fields.
  - Created `scripts/track_application.py` and `output/applications.json` tracker.
  - Added gap-closing project suggestion as a standard output of every tailoring run.
  - Fixed trailing comma in `resume.json` that broke JSON parsing.
- **Why:**
  - Eliminates data drift (GPA 3.6 vs 3.7 bug), reduces override boilerplate, and adds actionable outputs.
- **What was rejected and why:**
  - Nothing rejected; all four improvements implemented.

## 2026-06-27: Akuna Capital Crypto SWE Tailoring
- **What was decided:**
  - Assessed fit as "plausible fit — Apply now." Production Python pipeline experience (BofA) + genuine crypto ecosystem knowledge (personal trading + projects) is an unusually strong combo for this role.
  - Incorporated Randy's personal crypto trading experience (2023–2025, across Kraken/Hyperliquid/Jupiter/Lighter/Aster) into the summary and skills sections. Added a "Crypto" skills subcategory listing exchange APIs, market data types, and DeFi protocols.
  - Recommended mentioning "profitable personal crypto trader" but NOT the specific ~$300k PnL on the resume — save that for interviews where it lands better and is probeable.
  - Reframed BofA bullets to emphasize "real-time," "event-driven," "reconciliation," and "trade" vocabulary matching the JD.
  - Promoted Market Data Dashboard to first project (Binance/Hyperliquid API integration, market data, alerts).
- **Why:**
  - JD explicitly requires "experience working with trading systems, especially within the Crypto ecosystem." Randy's personal trading + crypto projects are genuine differentiators most SWE candidates lack.
- **What was rejected and why:**
  - Rejected putting specific PnL ($300k) on resume — unverifiable on paper, prop firms evaluate PnL differently than retail. Better as interview talking point.
  - Rejected claiming Kafka experience — AMPS is similar (pub/sub) but annotated as "AMPS message queues (pub/sub)" for honest reframing.
  - Rejected listing C++ — zero documented experience.

## 2026-06-28: Master Resume Update + HappyRobot FDE Re-tailoring
- **What was decided:**
  - Added Med-Spa Lead-Gen Pipeline project to `resume.json` and `resume_master.md` as the first project — demonstrates end-to-end pipeline building, Google Places API + Anthropic API integrations, LLM prompt engineering, web scraping, and test coverage.
  - Added BeautifulSoup, Google Places API to skills in `resume.json`; added "web scraping & enrichment" to practices.
  - Re-tailored HappyRobot Forward Deployed Engineer resume with Med-Spa project included.
  - Assessed fit as "plausible fit / Apply with targeted cover letter" — strong Python/API/AI match but React/TypeScript/Node.js gap is real.
  - Dropped Polymarket Scanner from HappyRobot resume (least relevant) to keep one page with 4th project added.
  - Kept hedged "(building)" for React, TypeScript, Node.js — same approach as previous tailoring.
- **Why:**
  - Med-Spa project is a strong signal for "building AI/ML applications" and "API integrations" — two of the JD's core tech profile items.
- **What was rejected and why:**
  - Rejected claiming React/TS/Node as known skills — zero documented experience, fabrication violates principles.
  - Rejected including all 4 projects — overflowed to 2 pages. Polymarket Scanner cut as least relevant to this role.

## Session Summary (2026-06-28)
- **Worked on:** Master resume update (Med-Spa project), HappyRobot FDE re-tailoring
- **Completed:** resume.json + resume_master.md updated, fit assessment, tailored 1-page PDF, application tracked
- **Decisions made:** "Plausible fit / Apply with cover letter"; Med-Spa project added to master resume
- **Next session priorities:** Consider building Voice-Enabled AI Agent Demo (React + TS + Node.js + voice) to close HappyRobot's full-stack and voice gaps


## 2026-06-30: Benchmark Dashboard Project Added to Master Resume
- **What was decided:**
  - Added Benchmark Dashboard as the first project in `resume.json` and `resume_master.md`. It's a multi-tenant financial-intelligence dashboard (Next.js, React, TypeScript, Tailwind, Recharts, Supabase) built for a medspa consulting agency Randy is co-building with an ex-IB/PE friend.
  - Promoted TypeScript from unlisted to a primary language in skills (no longer hedged — Randy built a full Next.js/TS app).
  - Added Next.js, React, Tailwind, Recharts, Supabase to data_systems skills.
  - Context sourced from a shared Claude conversation detailing the project planning, architecture decisions (multi-tenant from day one, RLS, benchmarking schema), data-layer research (Vagaro/Boulevard API constraints), and design direction.
- **Why:**
  - Benchmark Dashboard demonstrates full-stack product building, applied AI (recommendations engine), multi-tenant architecture, and fast iteration — all directly relevant to FDE roles. Also closes the React/TypeScript gap previously flagged for HappyRobot.
- **What was rejected and why:**
  - Nothing rejected. All additions grounded in real work Randy has done/is doing.

## 2026-06-30: Grouped Benchmark Projects + William Blair Tailoring
- **What was decided:**
  - Grouped Benchmark Dashboard and Med-Spa Lead-Gen Pipeline into a single "Benchmark Agency Platform" entry in resume.json and resume_master.md. Tells a cohesive FDE story rather than two separate side projects.
  - Tailored resume for William Blair Senior AI Engineer (AI Innovation Function). Recruiter reached out.
  - Verdict: "plausible fit / Apply now" — capital markets experience at BofA is the key differentiator most AI engineers lack. Benchmark embedded work maps directly to their FDE model.
  - Dropped Polymarket Scanner from this tailoring (least relevant to IB). Merged two BofA bullets to fit one page.
  - Compressed Benchmark description to fit; kept emphasis on paying clients, multi-tenant, AI recommendations, and embedded-with-founder narrative.
- **Why:**
  - Recruiter-initiated contact overrides the usual 5+ years gate concern. Capital markets + FDE-style work is the play.
- **What was rejected and why:**
  - Rejected claiming Databricks, Azure, Salesforce, or multi-agent production experience — genuine voids, not reframeable. Surfaced as gaps in fit assessment.

## 2026-06-30: Resume-Tailor Skill Improvements
- **What was decided:**
  - Added format-2 semantic overrides to build_resume.py — experience keyed by company name (only bullets needed), projects via include/exclude lists, skills as structured categories with `join_next` for layout control, `**bold**` auto-converted to HTML. Legacy overrides still work via `"format"` key detection.
  - Added page-count check: build script now prints "OK: 1 page." or "WARNING: N pages" after every build.
  - Created gen_master_md.py — auto-generates resume_master.md from resume.json. One source of truth.
  - Updated track_application.py with dedup — re-tailoring same company+role updates in place.
  - Added JD archiving instruction to SKILL.md (save to `output/<company>_jd.txt`).
  - Standardized fit assessment output (always write `output/fit_assessment_<company>.md`).
  - Fixed duplicate HappyRobot entry in applications.json.
  - Updated README.md with full format-2 schema docs.
- **Why:**
  - Reduce per-tailoring friction: less HTML boilerplate, no manual page checking, no file sync, no tracker duplicates.
- **What was rejected and why:**
  - Rejected auto-layout for skills (dynamic line grouping) — too magic; explicit `join_next` flag is clearer and matches existing visual patterns.

## Session Summary (2026-06-30)
- **Worked on:** Resume-tailor skill improvements (6 items), Benchmark project grouping, William Blair tailoring
- **Completed:** All 6 improvements implemented and tested; William Blair resume converted to format-2
- **Decisions made:** Format-2 as default going forward; legacy overrides preserved for backward compat; resume_master.md is now auto-generated
- **Next session priorities:** Continue building Benchmark backend; build anchor-project-2 (agentic tool + eval harness) to close multi-agent and eval framework gaps