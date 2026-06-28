# Execution Tracker

*The one file that matters. Everything else in this repo is input; this is output.*

The rule: **a week with no application sent and no committed code is a failed week**, regardless of how much was read or planned. This repo has enough strategy. From here, progress = shipped artifacts + sent applications + completed mock interviews. Update this file, not the plan files.

## The weekly scorecard (the only metrics that count)

Fill this in every Sunday. If a row is zero two weeks running, something is wrong — fix the system, not the spreadsheet.

| Week of | Apps sent | Interviews scheduled | Commits to anchor projects | Mocks done | LeetCode | Notes |
|---|---|---|---|---|---|---|
| (start) |  |  |  |  |  |  |

## This-week, near-zero-cost moves (do before any project work)

These are high-leverage and fast — knock them out before disappearing into building.

- [ ] **Rewrite LinkedIn headline + recent-role bullets** with exact recruiter filter terms: "production AI systems," "evals," "RAG," "agent," "forward deployed." (~30 min; ~2-week payoff in recruiter inbound. See research refresh #2.)
- [ ] **Master resume + the FDE-financial-services angle** drafted first (your sharpest edge). Backend/trading angles can follow.
- [ ] **Open the application tracker** (below) and put the first 5 FDE apps in it — sent, not bookmarked.
- [ ] **Set up the dev environment + a CLAUDE.md** for Anchor Project 2 so the agent harness can start.

## Application tracker

One row per application. "Stage" moves: applied → recruiter screen → technical → onsite → offer / rejected. Re-verify postings before applying; they move fast.

| Company | Role / track | Link | Date applied | Stage | Contact | Next action |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### First apply-batch (from `research/fde-live-openings.md`, re-verify each)
- [ ] OpenAI — FDE, Financial Services (NYC) — best domain-match moonshot
- [ ] Google Cloud — GenAI FDE — volume + more accessible bar
- [ ] 2–3 "Sr. FDE — Financial Services" aggregator postings in relocate-friendly cities
- [ ] Palantir — FDSE — negotiation-friendly, original shop
- [ ] 2–3 Tier-3 startups (11–200 ppl) from a LinkedIn FDE search — for interview reps

## Project status (anchor projects only — breadth projects don't go here)

**Anchor Project 2 — agentic tool + eval harness + MCP server** *(the centerpiece; build first)*
- [ ] CLAUDE.md spec written (deliverable + constraints + definition-of-done tied to eval metrics)
- [ ] Eval suite stood up FIRST as the success oracle (golden dataset + LLM-as-Judge + regression run)
- [ ] Agent loop working against real messy data (LangGraph or LangChain)
- [ ] Initializer + loop prompt harness; ran unattended once in a sandbox
- [ ] Versioned prompts with rollback
- [ ] Structured observability / logging of agent steps
- [ ] MCP server wrapping capabilities
- [ ] CI/CD: GitHub Actions, eval suite as a merge gate
- [ ] Thin React/TS dashboard surface (covers the TypeScript signal)
- [ ] Dockerized + deployed live + README as deployment case study

**Anchor Project 1 — real-time market-data platform** *(strongest cross-track asset; build second unless trading heats up)*
- [ ] FastAPI service over the existing crypto collector
- [ ] PostgreSQL/TimescaleDB storage + Redis caching
- [ ] React dashboard (build the front end in React, not Python templating — covers TS signal here instead)
- [ ] Dockerized + deployed + README

## Mock interview log

The most-overlooked, highest-signal prep. Especially: the decomposition case study and the CISO-simulation, done **live with a person**, not solo.

| Date | Type (case study / CISO sim / coding / system design / behavioral) | Partner | What broke | Fix |
|---|---|---|---|---|
|  |  |  |  |  |

## Admin loose ends (from master plan — close and forget)

- [ ] Termination letter received + filed; stated reason reviewed
- [ ] Lawyer consultations done (stop after 3–4 consistent answers)
- [ ] Unemployment: any follow-up requests answered promptly
- [ ] Dispute/appeal call outcome recorded
