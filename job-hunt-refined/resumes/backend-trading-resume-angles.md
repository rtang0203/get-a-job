# Backend & Trading Resume Angles

*Drafted late June 2026 · completes the four-angle set (FDE angle lives in `fde-resume-bullets.md`)*

Same underlying facts (Cornell CS, Microsoft ML, BofA backend, the two anchor projects, crypto market-structure depth), re-weighted per target. Maintain one master resume; cut these as tailored one-pagers. `[X]` = insert a real number; never invent one. The honesty rules from the FDE file apply here too — every keyword needs a true one-sentence tradeoff story behind it, because reviewers probe polished-looking bullets harder in 2026.

---

# Backend angle (the reliable baseline)

This is the cleanest, most conventional version — lead with engineering substance. The backend loop weights system design and "can you actually own a service" over algorithm count, so the resume's job is to make "owns production services end-to-end" obvious at a glance.

## Positioning summary

> Backend engineer (Cornell CS, ex-Microsoft ML) building reliable production Python services. Strong in modern API/data infrastructure — FastAPI, PostgreSQL, Redis, Docker, Kubernetes, CI/CD — with financial-systems domain depth from enterprise banking. Comfortable owning a service from design through deployment and on-call, and reasoning about failure modes, not just happy paths.

The last clause is deliberate: 2026 backend loops probe "what happens when this fails?" relentlessly, so signal failure-mode thinking up front.

## Skills line (lead with these, list only what you can defend)

Python · FastAPI · PostgreSQL/TimescaleDB · Redis · Kafka · Docker · Kubernetes · CI/CD (GitHub Actions) · AWS or GCP · REST API design · system design (caching, queues, sharding, rate limiting, idempotency) · SQL (CTEs, window functions)

## Experience bullets — Bank of America

- Built and operated production Python services in a large regulated enterprise, owning reliability and navigating legacy systems and cross-team dependencies.
- [Reliability/scale bullet with a metric — "Owned [service] processing [X] requests/day at [Y] availability; cut [latency/error rate] by [Z]% via [caching/retry/idempotency change]."] — this is the most important bullet on the page; make it concrete.
- Designed for failure: [idempotency keys / retry-and-backoff / dead-letter handling / circuit-breaking] on [system], reducing [duplicate processing / cascading failures] in production.
- Partnered across [teams] to turn ambiguous requirements into shipped backend functionality with high autonomy.

## Projects

**Real-time market-data platform** *(Anchor Project 1)*
- Async FastAPI service over a live crypto market-data pipeline (funding rates, open interest, volume); PostgreSQL/TimescaleDB storage, Redis caching, WebSocket ingestion; Dockerized and deployed with a React dashboard.
- End-to-end backend ownership: API design, time-series modeling, caching strategy, containerized deployment, CI/CD with a test gate.

**Agentic tool with eval harness + MCP server** *(Anchor Project 2)*
- Frame for backend as the **LLMOps angle**: production-grade service with structured observability, an eval/regression suite gating CI, versioned configs with rollback, Dockerized and deployed. (LLMOps is a fast-growing, well-paid backend-adjacent category — this widens the net at no extra cost.)

## Adjacent targets where your background is a feature
Fintech (domain fit), AI-infra / LLMOps backend, data-infrastructure roles. Apply broadly and early here for interview reps and momentum while FDE/trading mature.

---

# Trading angle (the moonshot)

Lead with quantitative/market depth. The honest constraint stands: elite low-latency HFT execution leans on C++ and quant-grad credentials you don't lead with. Your realistic, genuinely-open lane is **Python-first systematic/research infra, crypto-native trading firms, and fintech-adjacent quant** — where your self-taught market-structure depth is an uncommon edge. The single most important framing move: **translate crypto fluency into general market-structure vocabulary** (order books, microstructure, funding/basis as a carry analogue) so a TradFi desk hears transferable skill, not just "crypto guy."

## Positioning summary

> Backend engineer with self-directed depth in market microstructure and systematic-trading infrastructure. Built and operate a live market-data system (order-book, funding-rate, open-interest, and volume capture across venues) on an event-driven, time-series stack. Cornell CS, ex-Microsoft ML, enterprise-banking domain background. Fluent in derivatives and perpetual-futures mechanics; comfortable across the research-to-infra pipeline in Python.

## Skills line

Python (pandas, NumPy) · time-series / high-frequency data (TimescaleDB) · event-driven architecture · Kafka · Redis · WebSocket market-data ingestion · Docker · Kubernetes · CI/CD · market microstructure · derivatives & perpetual futures · funding/basis & carry · order-book mechanics · (familiarity: KDB/q — *only if true*)

## The vocabulary translation table (use this; don't make the reader do it)

| You know (crypto-native) | Say it as (general market-structure) |
|---|---|
| Perp funding rates | Basis / carry; cost-of-carry signal |
| Cross-exchange funding/price dislocation | Cross-venue arbitrage; relative-value |
| Hyperliquid order book / depth | Limit-order-book microstructure, depth/liquidity |
| Open interest / volume monitoring | Positioning and flow signals |
| Your collector + dashboard | Real-time systematic-trading data infrastructure |

## Experience bullets

**Market-structure & systematic infra (self-directed)**
- Designed and run a live, multi-venue market-data system capturing order-book depth, funding/basis, open interest, and volume into a time-series store; event-driven and containerized — the data backbone a systematic strategy or research workflow runs on.
- Developed [trade theses / signal research] grounded in microstructure and funding/basis dynamics [e.g. the cross-venue dislocation work, the oil-correlated macro expression] — demonstrating trade construction and edge-identification, not just engineering.
- Fluent in derivatives mechanics (perpetual futures, funding, basis) and their traditional-markets analogues (futures carry, swap pricing).

**Bank of America**
- Production Python in a regulated financial-markets environment; financial-systems domain fluency and reliability engineering at enterprise scale.

**Microsoft (ML)**
- ML systems experience — relevant to systematic/ML-driven strategy research and feature pipelines.

## Where to look (from the market map + fresh scan)
- **OpenQuant** (openquant.co), **eFinancialCareers**; specialist recruiters (Goliath Partners and similar) run much of this market — contact directly.
- **Crypto-native firms — likely your best-fit sub-lane** (expertise applies directly, not translated): B2C2, Talos, Jump Crypto, Galaxy Digital, Kraken, and the stealth/prop systematic shops. Job boards: cryptojobslist, cryptocurrencyjobs.co, sailonchain. Recurring asks there map onto your stack: Python, WebSocket/Kafka/Redis/PostgreSQL, Docker/Kubernetes, CI/CD, systematic-trading-environment experience.
- Python/systematic lanes at the larger shops (D.E. Shaw and peers) and bank systematic-strats desks (e.g. Goldman GBM systematic-trading strats) — broader net, higher bar.

## Honest caveat (keep it in view)
Treat top pure-quant/HFT execution shops as lottery tickets. The base case is crypto-native + Python-systematic + fintech-quant, where your profile is a real fit. Interviews here add a probability/stats/brainteaser strand and lean harder on low-latency/order-book design — prep that strand specifically (see `prep/prep-schedule.md`), but don't let the moonshot's harder bar set your daily cadence.

---

## Note on the resume itself (applies to all four angles)
Keep it ATS-plain: single column, standard fonts, no graphics — scanners choke on the rest. One page unless 8+ years. Mirror the specific JD's keywords (only ones you can defend). Lead each role with the most role-relevant 2–3 bullets; the rest can come up in conversation. The metric bullet is always the one that earns the interview — prioritize getting real numbers for at least one bullet per role.
