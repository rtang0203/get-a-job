# Anchor Project 2 — Build Spec

**"Agentic deployment tool with eval harness + MCP server"**

*Drafted June 25, 2026*

## Why this project, specifically

This is the single highest-ROI thing Randy can build for the FDE track. Nearly every top-tier FDE JD (Anthropic, OpenAI, the consulting practices) now requires *"production experience with LLMs: advanced prompt engineering, agent development, evaluation frameworks, and deployment at scale."* Anthropic's JD literally lists delivering *"MCP servers, sub-agents, and agent skills."* This project is built to be a near-literal checklist match against that language — so it converts directly into interview eligibility, not just a portfolio nicety.

It also doubles as interview prep: the recurring FDE technical questions (prompt versioning/rollback, agent observability, RAG latency, eval design) are exactly the things you'll have built and can speak to from real experience.

## Design principle: make it FDE-shaped

The FDE job is "turn a fuzzy enterprise problem into a working, deployed, reliable AI solution." So the project should *mirror that arc* end-to-end, not just be a clever demo. Pick a concrete, slightly-messy domain problem and solve it properly. Two strong options that build on what Randy already has:

- **Option A (recommended): evolve the lead-gen pipeline.** Randy already has a discovery/enrichment/scoring spec for the med-spa/day-spa consulting project. Turn it into a deployed agentic tool: an agent that ingests messy business data, enriches it, scores leads, and outputs structured results — with a real interface, error handling, and an eval harness measuring scoring quality. This is *literally* an FDE story: scoped a fuzzy client problem, shipped a production tool.
- **Option B: a market-data research agent.** Leverages the crypto data collector — an agent that answers questions over the funding-rate / OI / volume data, calls tools, and is evaluated for accuracy. Ties to the trading track too.

Go with A unless the trading track heats up; it's the cleaner client-deployment narrative.

## What it must demonstrate (the JD checklist)

1. **Agent development** — multi-step, tool-using agent (calls APIs, reads/writes a DB) using a named framework (LangGraph or LangChain — the JDs name these; don't hand-roll everything).
2. **Eval harness** — the 2026 non-negotiable and the rarest skill. Re-verified research (late June) makes this even more decisive: inability to whiteboard an **LLM-as-Judge eval suite** is reportedly the single most common final-round rejection at OpenAI and Anthropic, filtering ~70% of otherwise-strong candidates. So build the suite to demonstrate the *specific* gating competencies, not just "some evals":
   - **LLM-as-Judge** scoring for the fuzzy parts (is this enrichment good?), AND be able to explain **why naive LLM-as-Judge fails on multi-turn agent traces** and how you mitigate it. This exact point is a known filter — build the answer.
   - **A golden dataset** (hand-labeled leads) + **regression run on every change** to catch drift.
   - **Tracked failure modes** — categorize *how* it fails, not just a pass/fail number.
   - Plus the obvious axes: functional correctness, grounding/hallucination, and a business KPI (lead-score precision).
   - Tools worth naming: RAGAS, DeepEval, Arize Phoenix; observability tools worth naming by function: LangSmith, Braintrust, HoneyHive.
   This is the single most differentiating component in the entire repo — invest here above everything else. It also doubles as the **success oracle** that lets you run the build agent unattended (see `prep/agentic-engineering-skill-guide.md`).
3. **MCP server** — expose the tool's capabilities as an MCP server. Directly matches Anthropic's "deliver MCP servers" line and shows you're current.
4. **Prompt management** — versioned prompts with the ability to A/B-test and roll back (a known FDE interview question — build the answer).
5. **Observability** — structured logging of agent steps, plus what you'd alert/dashboard on. Another direct interview-question match.
6. **Production hygiene** — Dockerized, deployed somewhere live-demoable, FastAPI surface, tests, CI/CD, real README. Make the **CI/CD eval-gate** explicit: GitHub Actions where a regression in the eval suite *fails the build*. "My CI won't let a prompt change ship if it regresses the eval" maps directly onto the "eval gates" primitive the OpenAI system-design round asks for. Add a **thin React/TS dashboard** (even one page) — ~35% of FDE postings want TypeScript because FDEs build customer-facing views; this covers that signal cheaply.

**Build this project *using* an autonomous agent harness.** Don't just build the agent — build it *with* an agent you run unattended (CLAUDE.md spec, the eval suite as success oracle, progress file, reviewer subagent, sandboxed permissions). That gets you the "I let agents run for extended periods" skill you wanted AND the portfolio piece in one motion, plus a true war story for every interview question. Full pattern in `prep/agentic-engineering-skill-guide.md`.

"Demo notebooks do not move the needle" — hiring managers screen on production-readiness. Deploy it where you can show it live.

## Rough build sequence (~2-3 weeks alongside other work)

- **Week A — skeleton + agent.** FastAPI service, pick the domain problem, stand up the agent with one framework, get a basic multi-step tool-use loop working against real (messy) data. Dockerize from day one.
- **Week B — evals + prompts.** Build the eval harness (this is the star — give it real care). Add versioned prompt management with rollback. Add structured observability/logging.
- **Week C — MCP + deploy + polish.** Wrap capabilities in an MCP server. Deploy live. Write the README as a deployment case study (problem → approach → tradeoffs → results → what you'd do next). Record a short demo.

## The talking points it earns you

For each component, you'll have a *true* sentence about a real tradeoff — which is interview gold and can't be faked:
- "I built the eval suite to catch grounding failures before they hit production; here's the false-positive tradeoff I hit."
- "I versioned prompts so I could A/B and roll back; here's what broke the first time."
- "I exposed it as an MCP server; here's what I'd add for enterprise auth."

## README structure (make it a deployment case study)

Problem statement → who the "customer" is → architecture diagram → the agent design → how evals work and what they caught → deployment → observability → honest "limitations / next steps." This reads exactly like the field artifacts FDEs produce, which is the point.

## Cross-track bonus

The eval-engineering and observability skills also feed an adjacent fast-growing role (**LLMOps engineer**) — so this project quietly widens the net beyond FDE without extra work.
