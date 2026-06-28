# FDE Interview Format — What to Actually Expect

*Researched June 25, 2026 · sourced from current FDE interview guides*

The FDE loop is **not** a standard LeetCode grind. It tests a "T-shaped" profile: deep skill in one core area, broad capability across several, plus a vertical bar of customer-facing soft skills. Prep weight for this track should shift accordingly — coding is practical, not algorithmic, and communication is graded as heavily as code.

## The stages

1. **Behavioral / fit** — communication, ownership, comfort with ambiguity. At the labs (esp. Anthropic) mission-fit is screened seriously and *throughout*, not just at the end. Generic enthusiasm fails.
2. **Technical deep-dive (practical coding)** — common formats: build a **rate limiter**, process **streaming data**, design a **distributed job queue** (priorities, retries, dead-letter). Not "invert a binary tree." Randy's backend background maps well here.
3. **The decomposition case study** — the signature stage. A vague, real-world problem ("a city wants to cut 911 response times; here's call/traffic/GPS data — you have 60 minutes"; "a regional bank wants unified fraud detection across three acquired systems with inconsistent labels"). **Don't jump to a solution.** Ask clarifying questions, break it into chunks, propose a simple MVP, then iterate out loud, showing first-principles reasoning.

## LLM / system-design questions that recur

- Diagnose high latency in an LLM inference pipeline (walk the full stack: tokenization, network, batch size, KV cache, post-processing).
- Naive RAG is 1.5s; customer needs sub-100ms — walk through getting there.
- Unify customer data split across SAP, Salesforce, and a custom Postgres warehouse for an agent to use.
- Version, A/B-test, and roll back **prompts** in production.
- Design **observability for an agent system** — what to log, alert on, dashboard.

These map almost one-to-one onto Anchor Project 2. Building it *is* interview prep.

## Company-specific notes

- **Anthropic** — coding is practical (rate limiter / streaming / job queue). Reads candidates on mission fit hard; read their Core Views on AI Safety, Responsible Scaling Policy, and recent interpretability work first. Reportedly **firm on offers** (little/no negotiation) — plan accordingly.
- **OpenAI** — favors the LLM-inference-latency walkthrough; sits between Palantir and Anthropic on negotiation.
- **Palantir** — FDSE / Deployment Strategist; known to negotiate for strong candidates.
- **Databricks** — Spark, SQL, data modeling, RAG over enterprise datasets, MLflow, lakehouse.

## How Randy should prep this track

- Rehearse the **decomposition case study** out loud — this is the highest-signal, most-trainable, most-overlooked stage. Practice the discipline of clarifying-before-solving.
- Practice **explaining technical tradeoffs to a non-technical VP** — the soft-skill bar is real and graded.
- Drill the practical coding formats (rate limiter, streaming, job queue) rather than only LeetCode hards.
- For lab applications, invest genuine time in **mission-fit articulation**.
- Keep LeetCode going for the backend/trading tracks, but don't over-index on it for FDE.
