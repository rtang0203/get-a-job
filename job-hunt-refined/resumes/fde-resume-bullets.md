# FDE Resume — Draft Bullets

*Drafted June 25, 2026 · mapped to real Anthropic/OpenAI/Google FDE JD language*

These are starting drafts, not finished copy. They're written to mirror the exact phrases recurring across current FDE JDs so an ATS and a human both see the match. Swap in real metrics where you have them — bracketed `[X]` means "insert a number." Lead with the rare combination FDE roles can't easily staff: **strong production engineer + genuine customer-facing presence + comfort shipping under ambiguity.**

## Positioning summary (top of resume)

> Backend engineer (Cornell CS, ex-Microsoft ML) who ships production Python and works directly with stakeholders to turn ambiguous problems into deployed solutions. Financial-services domain depth from enterprise banking plus self-directed expertise in market structure and data systems. Comfortable owning technical delivery end-to-end and translating between engineers and non-technical decision-makers.

Tune the one-liner per posting: for financial-services FDE roles, foreground the banking + markets domain; for lab roles, foreground LLM/agent work and mission fit.

## The JD phrases to mirror

Recurring across the JDs — work these in honestly where true: *"ship production applications," "navigate ambiguity in complex organizations," "convey technical concepts to diverse stakeholders," "high agency," "production experience with LLMs — prompt engineering, agent development, evaluation frameworks," "MCP servers, sub-agents, agent skills," "translate ambiguous business problems into technical specs."*

## Experience bullets — Bank of America (backend SWE)

- Shipped and maintained production Python services in a large, regulated enterprise environment, navigating legacy systems and cross-team dependencies to deliver reliable backend functionality.
- Partnered across [teams/functions] to translate ambiguous business requirements into working technical solutions, operating with high autonomy in a complex organization.
- [Add a concrete reliability/scale/impact bullet with a metric — e.g. "Owned [service] processing [X] daily transactions with [Y] reliability."]
- Built domain fluency in financial systems and data — directly relevant to financial-services AI deployments in regulated environments.

## Experience bullets — Microsoft (ML)

- Built and worked with machine-learning systems at scale, grounding later LLM/agent work in real ML fundamentals (not just API calls).
- [Add a specific project/impact bullet.]

## Projects (the differentiators — lead with these for lab/AI roles)

**Agentic deployment tool with eval harness + MCP server** *(Anchor Project 2)*
- Built a multi-step, tool-using agent (LangGraph/LangChain) that ingests messy real-world data and produces structured, scored output — mirroring an enterprise deployment from fuzzy problem to shipped tool.
- Designed an LLM **evaluation framework** measuring functional correctness, grounding/hallucination, and a business KPI — the production-readiness layer most demos lack.
- Exposed capabilities via an **MCP server**; implemented versioned prompts with A/B testing and rollback, plus structured agent observability (logging, alerting).
- Dockerized and deployed live; documented as a deployment case study (problem → architecture → evals → tradeoffs → next steps).

**Real-time market-data platform** *(Anchor Project 1)*
- Built an async FastAPI service over a live crypto market-data pipeline (funding rates, open interest, volume), with PostgreSQL/TimescaleDB storage, Redis caching, containerized and deployed.
- Demonstrates end-to-end backend ownership: API design, time-series data, caching, deployment — in a markets-adjacent domain.

**Earlier tooling**
- Built a Telegram task-automation bot on the Anthropic API with SQLite persistence — early hands-on LLM-application experience.

## Education

- B.S. Computer Science, Cornell University.

## Notes on honesty & framing

- **"No prior FDE title" is itself a named rejection reason** — so positioning is near-free alpha. You can't fake the title, but you can defang it: rewrite your **LinkedIn headline + recent-role bullets** to include the exact recruiter filter terms ("production AI systems," "evals," "RAG," "agent," "forward deployed"). Reports put recruiter inbound ~doubling within two weeks. 30-minute task, multi-week payoff — do it this week (it's in `prep/execution-tracker.md`).
- **Open with the hybrid, customer-facing framing**, not a generic "backend engineer" line — both ATS and humans look for the hybrid up top. Keep layout ATS-plain (no columns/graphics/unusual fonts); one page unless 8+ yrs.
- **Lead the skills line with Python + SQL**, then breadth (cloud, data pipelines, API integration, modern AI: RAG/agents/evals). SQL is table stakes in FDE loops (CTEs, window functions, messy joins) — list it prominently.
- The "software engineer with consulting experience" door: the lead-gen consulting build is legitimately a *scoped-a-client-problem-and-shipped* story. Frame it as such — it's your most FDE-shaped credential and worth its own line once it's deployed.
- Don't claim "deployment at scale" for LLMs until Anchor Project 2 backs it. The honest version — "built and deployed an agentic tool with an eval harness" — is already strong and grows as the project matures.
- For each named technology, keep a true one-sentence tradeoff story ready; that's what converts a resume keyword into a passed interview.
- **Foreground the regulated-finance angle on the FDE-financial-services resume** — regulatory fluency (EU AI Act, financial-services compliance) is now a named FDE differentiator and a genuine edge AI-native candidates lack.
- Maintain one master resume; cut tailored versions per track (FDE-financial-services vs. FDE-lab vs. backend vs. trading). The backend and trading angles are still to be drafted.
