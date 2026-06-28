# LinkedIn Profile Rewrite

*Copy-paste each section into LinkedIn. Optimized for recruiter search filters: "production AI systems," "evals," "RAG," "agent," "forward deployed," "financial services."*

---

## Headline

```
Backend Engineer → Production AI Systems | Evals · RAG · Agents · MCP | Financial Services Domain | Cornell CS
```

**Why:** Recruiters filter on exact terms. This headline hits "production AI systems," "evals," "RAG," "agents," and "financial services" — the five highest-signal FDE search terms. The arrow conveys trajectory without fabricating a title you haven't held.

---

## About

```
I build production AI systems and the infrastructure that makes them reliable — evals, observability, deployment pipelines — with domain depth in financial services from enterprise banking.

At Bank of America, I owned backend Python services processing millions of daily OTC transactions in a regulated environment: trade reporting, data transformation, high-volume automated backreporting. I learned what "production" actually means — not demos, but systems that run correctly at scale under compliance constraints, with real consequences for failure.

Now I'm building at the intersection of AI engineering and financial services:
• Agentic tool with an LLM evaluation framework (LLM-as-Judge, regression suites, drift detection) + MCP server — the production-readiness layer most AI demos skip
• Real-time market-data platform (FastAPI, PostgreSQL/TimescaleDB, Redis, React dashboard) — end-to-end backend ownership from ingestion to deployment

I'm looking for roles where I can ship AI systems into complex, high-stakes environments — forward-deployed engineering, AI infrastructure, or applied ML in financial services.

Cornell CS · ex-Microsoft ML · Python, SQL, FastAPI, Docker, LangGraph, RAG, evals
```

---

## Experience

### Bank of America — Software Engineer
**Aug 2022 – Jun 2025 · Chicago, IL**

```
• Owned production Python services on the Cirrus OTC trade reporting engine, responsible for reporting all over-the-counter derivatives trades across the bank in a regulated financial-services environment.

• Built and operated a T+1 Unique Trade Identifier (UTI) validation service processing millions of transactions daily — reviewing outgoing trades, running correction logic, and ensuring regulatory compliance on every transaction.

• Designed and shipped a high-volume backreporting service to automatically remediate erroneous transactions, replacing a manual process. Parallelized processing to significantly increase throughput.

• Built transformer and parser services converting internal data models to outgoing XML (DTCC format) and parsing regulatory responses to update transaction status — end-to-end ownership of the data pipeline.

• Wrote Python data-analysis tooling to investigate and resolve issues across large datasets (50–100 GB), partnering with operations and compliance teams to translate ambiguous problems into working solutions.

• Refactored existing services to eliminate unnecessary API calls and reduce latency, improving reliability across the reporting stack.
```

### Microsoft — Machine Learning / Data Analyst
**May 2022 – Aug 2022 · Redmond, WA**

```
• Built data processing and analysis pipelines (Python, Pandas) for the Viva Topics ML service in Microsoft Teams — cleaning, annotating, and preparing training data for production ML models at scale.

• Grounded in real ML systems fundamentals — data quality, annotation pipelines, model evaluation — not just API calls.
```

### Northrop Grumman — Engineering Intern
**Aug 2019 – Aug 2020 · Chandler, AZ**

```
• Released 50+ engineering drawings for flight and test components, including new designs and large assemblies. Performed structural analyses for assemblies and fastener stacks (NX, ANSYS).
```

---

## Featured / Projects Section

### Agentic Tool with Eval Harness + MCP Server
```
Multi-step, tool-using agent (LangGraph) that ingests messy real-world data and produces structured, scored output. The differentiator: a production-grade LLM evaluation framework — LLM-as-Judge scoring, golden-dataset regression suites, drift detection, and tracked failure modes. Exposed via MCP server with versioned prompts and structured observability. Dockerized and deployed.

Stack: Python, LangGraph, MCP, Docker, GitHub Actions, React/TypeScript dashboard
```

### Real-Time Market Data Platform
```
Async FastAPI service over a live crypto market-data pipeline (funding rates, open interest, volume). PostgreSQL/TimescaleDB storage, Redis caching, WebSocket ingestion. React dashboard for visualization. Containerized and deployed with CI/CD.

Stack: Python, FastAPI, PostgreSQL, TimescaleDB, Redis, WebSocket, React, Docker
```

---

## Skills (reorder to put these at the top)

```
Python · SQL · FastAPI · PostgreSQL · Redis · Docker · Kubernetes · CI/CD · LangGraph · LangChain · RAG · LLM Evaluation · Prompt Engineering · Agent Development · MCP · React · TypeScript · Pandas · Git · AWS/GCP
```

---

## Education

```
Cornell University — B.S. Computer Science, B.S. Mechanical Engineering (2017–2021)
```

---

## Notes (don't put these on LinkedIn — just for your reference)

1. **Update your Skills endorsements** — ask 2-3 connections to endorse Python, SQL, and any AI-related skills.
2. **Add the projects as Featured links** once they're deployed with READMEs — recruiters click Featured before scrolling.
3. **Profile photo + banner** — profiles with photos get ~20x more views. Use a professional headshot. Banner can be simple (your name + "AI · Financial Services · Backend").
4. **Open to Work setting** — turn it on (visible to recruiters only, not your network) for the roles you're targeting.
5. **Connect with FDE hiring managers** — after updating, search for people with "Forward Deployed" in their title at Palantir, OpenAI, Anthropic, Google. Send a connection request with a short note.
