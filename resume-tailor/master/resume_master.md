# Randy Tang — Master Resume

> Auto-generated from `resume.json`. Edit the JSON, then run
> `python3 scripts/gen_master_md.py` to regenerate this file.

**rtang0203@gmail.com · 732-666-2746**

## Education
**Cornell University, College of Engineering** — Ithaca, NY · Sep 2017 - Dec 2021
B.S. Computer Science & B.S. Mechanical Engineering · GPA 3.7
- CUAIR (Cornell Unmanned Aircraft) — autonomous plane with obstacle avoidance, object classification, airdrop; consistently top team at AUVSI SUAS competition.

## Experience
**Software Engineer — Bank of America** · Aug 2022 - Present
*Cirrus OTC Trade Reporting · Python, Pandas, Quartz, AMPS message queues*
- Cirrus trade reporting team — responsible for reporting all OTC trades through the bank.
- Designed, implemented, and improved high-throughput data pipelines processing tens of millions of transactions daily.
- Reference-data framework: pipeline of services via AMPS queues querying multiple external sources per trade event; handles retries, API calls, load balancing; extensible for new sources.
- T+1 UTI (Unique Trade Identifier) service: validates trade-ID uniqueness across counterparties, sends corrections; millions of transactions/day.
- High-volume backreporting service: parallelized, automated a formerly manual process, large speed/throughput gains.
- Transformer service (internal model -> outgoing XML) + DTCC response parser to update transaction status.
- Optimized services to improve speed/throughput/reliability by orders of magnitude.
- Python/Pandas scripts to scrape and analyze 50-100GB datasets.

**Data Analyst (Contract) — Microsoft** · Mar 2022 - Aug 2022
*Viva Topics · Python, Pandas, Jupyter*
- Supported data science team on Viva Topics; processed/analyzed data used to train ML models.
- Wrote Python scripts to clean, annotate, and generate reports on user- and tester-collected data.

**Engineering Intern — Northrop Grumman** · Fall 2019, Summer 2020
*NX, ANSYS*
- Released 50+ engineering drawings incl. new designs and large assemblies; fully designed/drafted/released multiple flight and test components.
- Structural analyses for large assemblies and detailed fastener-stack analyses.

## Projects
- **Benchmark Agency Platform** (Next.js, React, TypeScript, Tailwind, Recharts, Supabase, Python, SQLite, Google Places API, Anthropic API, BeautifulSoup) — Technical platform for a medspa consulting agency (3+ paying clients). Built a multi-tenant financial-intelligence dashboard (revenue trends, equipment P&L, staff comp, AI-generated recommendations) with row-level security and cross-practice benchmarking architecture. Built a lead-gen pipeline that discovers med-spas across metros via Google Places, enriches web presence, scores deficiency signals, and generates personalized outreach via Claude. 8 idempotent stages, 20 tests.
- **Polymarket Scanner** (Flask, Discord API, SQLite) — Scans Polymarket for large trades and unusual/potential insider activity; alerts to Discord.
- **Market Data Dashboard** (Grafana, Twilio, Postgres, Docker) — Pulls market data (OI, funding, etc.) from Binance and Hyperliquid APIs; dashboard + SMS alerts on signal triggers.
- **Reading Recommendations App** (Flask, Gemini API, SQLite) — LLM-powered daily recommender over a Project Gutenberg corpus from user preferences.

## Skills
Python, TypeScript, SQL, Java (fundamentals), Pandas, AMPS message queues, high-throughput pipelines, concurrency, Postgres, SQLite, Docker, Flask, FastAPI, Next.js, React, Tailwind, Recharts, Supabase, BeautifulSoup, Google Places API, Agentic coding & orchestration, LLM APIs, tool-augmented workflows, Performance optimization, data pipeline design, web scraping & enrichment, code review, documentation & communication, Git
