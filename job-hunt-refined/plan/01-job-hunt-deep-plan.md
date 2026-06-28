# Job Hunt — Deep Plan

*Drafted June 25, 2026 · ~6–8 hrs/day, treat it like a job*

## The strategy in one breath

You're not picking one lane — you're running four, because your profile genuinely spans them and a wider net is smarter when you have runway. The trick is that **the four tracks share ~80% of the same prep.** LeetCode, system design, and a modern-backend project serve trading firms, regular tech, *and* FDE. So you build one strong core, then add small track-specific layers on top (a quant-flavored project for trading, a client-facing story for FDE/sales). You are not doing four separate preps. You're doing one prep with four resume angles pointed at it.

A realistic read on fit, since you asked me to be honest:
- **Trading firms / hedge funds** — Highest bar, longest odds, best payoff. Your crypto-market-structure depth and trade-construction instinct are real differentiators here. Worth pursuing, but treat it as the moonshot, not the baseline.
- **Forward-deployed engineer** — This might be your *best-fit* track and you may be underrating it. The role exploded ~700%+ in the last year, and the profile it wants — strong Python, customer-facing presence, comfort with ambiguity, ability to read an unfamiliar codebase and ship — is almost a description of you. Your "I have people skills and presence in person" plus real engineering is exactly the rare combination they say is hard to staff. **Lean into this one.**
- **Regular backend / tech** — Your reliable baseline. Broadest set of openings, most predictable loop (LeetCode + system design). This is your floor, and a good floor.
- **Sales engineer / tech sales** — Real option given your presence, and lower coding bar than FDE, but typically lower comp ceiling and a different day-to-day. Good as a parallel net, especially the *sales-engineer* (pre-sales technical) flavor rather than pure sales.

Suggested energy split: FDE and backend as primary (they share the most prep and have the most volume), trading as the high-effort moonshot, sales-engineer as the low-cost parallel net.

---

## Daily structure (the ~6–8 hr template)

Rough shape, adjust to your rhythm. The point is that *applying* is a daily activity from week 2, not a phase you reach later.

| Block | Time | What |
|---|---|---|
| Morning — sharp | 2 hrs | LeetCode (you're freshest; hardest cognitive work first) |
| Mid — build | 2–3 hrs | Project work / upskilling (the modern-stack learning) |
| Afternoon — apply | 1.5 hrs | Applications, outreach, networking, tracking |
| Flex | 1 hr | System design study, interview prep, or overflow |

One discipline that matters: **don't let prep crowd out applying.** The instinct is to feel "not ready" and keep studying. Resist it. Applications generate interviews, interviews are the best prep, and the feedback tells you what to study. Start applying week 2 regardless of how ready you feel.

---

## The upskilling core (shared across all tracks)

You named the gap honestly: legacy systems at BofA, light on the modern stack everyone's asking for. Here's the target list, ordered by leverage. The goal isn't certificates — it's being able to talk about each one *honestly and concretely* in an interview because you actually built something with it.

**Tier 1 — learn by building into your main project (weeks 1–4):**
- **FastAPI** — Modern Python API framework. You're a backend Python person, so this is the highest-leverage single thing. Build real endpoints, async handlers, pydantic models, auth.
- **Docker** — Containerize everything you build from now on. Non-negotiable baseline; appears in basically every modern backend and FDE JD.
- **PostgreSQL** (you know some) + **Redis** — Redis for caching, rate-limiting, pub/sub, job queues. Easy to demo, shows up constantly.

**Tier 2 — get functional, not expert (weeks 3–6):**
- **Kubernetes** — You don't need to be a wizard. You need to deploy a containerized app to a cluster once, understand pods/services/deployments, and be able to talk about it. Deploy one project to k8s (even local, via kind/minikube, or a managed cluster) and you've cleared the bar.
- **CI/CD** — GitHub Actions on your repos. Cheap to add, signals professional habits. But go one step past the baseline: make your **eval suite a merge gate** (a regression in lead-score precision fails the build) and run an **agent non-interactively in CI** (`claude -p ... --output-format stream-json` — e.g. an agent that reviews a PR diff and comments). Both are current, credible, and most candidates don't have them. See `prep/agentic-engineering-skill-guide.md` for the minimum-viable version.
- **Agentic engineering / running agents unattended** — The thing you explicitly wanted, and it turns out to be higher-leverage than a side skill: the harness that makes an agent run reliably for hours unattended (success oracle, progress file, structured logging, scoped permissions, reviewer subagent) is *the same skill set FDE interviews screen for* (evals, observability, guardrails). Learn it by building Anchor Project 2 with it. Dedicated guide: `prep/agentic-engineering-skill-guide.md`.
- **Cloud basics** — AWS *or* GCP, pick one. Deploy something real. FDE roles especially want this.
- **A thin frontend (React/TypeScript)** — Not a pivot to frontend; just enough to ship one customer-facing dashboard page. ~35% of FDE postings name TypeScript because FDEs build customer views. Build one anchor project's dashboard in React rather than a Python templating shortcut and you've covered it.

**Tier 3 — track-specific accelerants (as you go):**
- **Eval engineering** — Don't let "Tier 3" undersell this: for the FDE track it's effectively Tier 1. It's the named 2026 non-negotiable and the most common final-round rejection (~70% filter). The specific gateable skill is an **LLM-as-Judge regression suite with a golden dataset and drift detection**, plus being able to explain why naive LLM-as-Judge breaks on multi-turn agent traces. Build it into Anchor Project 2 and you've built the answer to the question that fails most people.
- **LLM / agentic workflows** — The 2026 "non-negotiable" for AI-FDE roles. RAG pipeline, a multi-step tool-calling agent, named framework (LangGraph/LangChain — the JDs name them; don't hand-roll everything). You already built a Telegram nag bot on the Anthropic API — extend that instinct into the agentic harness above.
- **Regulatory/compliance fluency** — Newly showing up as a named FDE differentiator (EU AI Act high-risk obligations phasing in Aug 2026; financial-services rules). This is a *Randy edge* from the BofA years — be able to talk for two minutes on what changes when deploying an AI agent into a regulated finance environment (data residency, auditability, change-control, human-in-the-loop). Converts "legacy baggage" into a scarce qualification.
- **Data pipeline tooling** (Spark/Airflow basics) — Nice-to-have for FDE and data-leaning backend. Don't over-invest unless a target role asks.

The honest-talking-point rule: for each tech above, you want one sentence that's *true* — "I built X with it, here's what was annoying, here's the tradeoff I hit." That beats a credential every time, and it's interview gold because it can't be faked.

---

## Projects — your GitHub as a portfolio

You're right that AI tooling lets you ship fast. Use that, but aim for a **mix**: 2 deep "anchor" projects that are genuinely impressive and survive scrutiny, plus a handful of smaller ones that each demonstrate a specific skill. Depth gets you through technical deep-dives; breadth makes the GitHub look alive.

**You already have raw material** — don't start cold. The crypto market-data collector (Hyperliquid funding rates / OI / volume on your DigitalOcean droplet), the funding-rate dashboard idea, the Telegram nag bot, the lead-gen enrichment/scoring spec. Polish these rather than inventing from scratch.

### Anchor project 1 — "Real-time market data platform" (hits trading + backend + FDE)
Build on your existing crypto collector. Make it a proper system: FastAPI service exposing the data, PostgreSQL/TimescaleDB for storage, Redis for caching/live updates, Dockerized, deployed, with a clean dashboard on top. This single project demonstrates: async Python, API design, time-series data, caching, containerization, deployment — and it's *market-structure flavored*, so it doubles as a trading-firm talking point. This is your strongest cross-track asset; invest the most here.

### Anchor project 2 — "Agentic / FDE-flavored tool"
An LLM-powered tool that does something real end-to-end — e.g., evolve the lead-gen discovery/enrichment/scoring pipeline into a deployed product, or an agent that ingests messy data and produces structured output (mirrors the actual FDE job: turn fuzzy enterprise input into a working solution). This is your FDE/AI-FDE centerpiece. Show RAG or tool-calling, error handling, a real interface.

### Breadth projects (1–2 days each, AI-assisted)
Each one targets a specific skill or a specific interviewer's checkbox:
- A clean FastAPI + Redis CRUD service with auth, tests, CI/CD — the "I can build a production-grade service" proof.
- A small k8s deployment of one of the above — your Kubernetes talking point.
- Something that scratches your own itch (you've built personal-tooling before) — these read as genuine and you'll actually finish them.

GitHub hygiene: real READMEs (what/why/how-to-run, a screenshot or gif), pinned repos, clean commit history. A recruiter spends 30 seconds — make the top of the page tell the story.

---

## LeetCode & system design (shared)

**LeetCode** — Steady cadence, pattern-focused, not grinding for a number. With your hours, ~3–5/day is sustainable. Target the pattern groups: arrays/strings, hashmaps/sets, two-pointer/sliding-window, stack/queue, trees, graphs/BFS-DFS, heaps, binary search, DP, intervals. Trading firms skew harder and sometimes add probability/math + low-latency thinking; regular tech and FDE skew medium. Over the full hunt aim for ~100–150 quality problems with real pattern retention, not 400 rushed ones.

**System design** — You said you're decent here; sharpen rather than rebuild. Patterns worth having cold: load balancing, caching layers, DB choice (SQL vs NoSQL, OLTP vs OLAP — you've covered this), sharding/replication, message queues (Kafka — you've touched this), rate limiting, consistency/availability tradeoffs. For trading specifically: order book design, low-latency considerations, time-series storage. For FDE: the interview is often a "decomposition" case study, not classic system design — practice taking a vague customer problem, asking clarifying questions, proposing an MVP, then iterating out loud. That's a different muscle; rehearse it.

---

## The four resume angles

Same underlying facts (Cornell CS, Microsoft ML, BofA backend), re-weighted per target. Keep a master doc, cut a tailored version per track.

- **Trading / hedge fund** — Lead with quantitative/market depth: the crypto market-structure work, derivatives/funding-rate fluency, trade-construction thinking, the market-data platform project. Frame BofA as financial-domain + systems reliability. Microsoft ML up top.
- **Forward-deployed engineer** — Lead with the rare combo: strong backend Python + customer-facing presence + shipping under ambiguity. Foreground the agentic/LLM project, any time you "wore all the hats," and your ability to explain technical things to non-technical people. Mention the lead-gen consulting build — it's literally you scoping a fuzzy problem for a client and shipping. That's an FDE story.
- **Regular backend** — Lead with engineering substance: the modern-stack projects (FastAPI/Docker/Redis/k8s), systems thinking, the market-data platform as proof of real backend chops. Cleanest, most conventional version.
- **Sales engineer / tech sales** — Lead with presence + technical credibility: ability to translate, demo, and build trust, backed by enough engineering to be taken seriously. The consulting/lead-gen work and any client-facing framing shine here.

---

## Weekly arc (first ~8 weeks)

- **Weeks 1–2:** Master resume + 4 angles. Set up dev environment. Start LeetCode cadence. Begin Anchor Project 1 (market data platform), learning FastAPI/Docker/Redis *as* you build it. **Start applying by end of week 2** — backend + FDE roles first, since they have the most volume.
- **Weeks 3–4:** Anchor Project 1 deployed and documented. Start Anchor Project 2 (agentic tool). Add k8s deployment. Applications now daily. First interviews may start landing — let them tune your prep.
- **Weeks 5–6:** Anchor Project 2 shipped. Breadth projects to fill gaps interviewers reveal. Heavier interview-specific prep for whatever's in your pipeline. Push trading-firm applications now that the market-data project is a credible artifact.
- **Weeks 7–8:** Mostly interviewing and iterating. Projects are "good enough" — stop polishing, start closing. Negotiate from your cash-runway position of strength.

If you're still going past week 8, the loop is the same: apply, interview, patch the specific gaps the interviews expose.

---

## The one-line version

One shared core (LeetCode + modern-stack project + system design), four resume angles on top of it. FDE and backend are your highest-volume best-fit primaries; trading is the moonshot; sales-engineer is the cheap parallel net. Build two anchor projects from material you already have, apply from week 2, and let interviews — not your sense of "readiness" — drive what you study next.
