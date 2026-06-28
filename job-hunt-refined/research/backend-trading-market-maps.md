# Backend & Trading Tracks — Market Maps

*Researched June 25, 2026 · re-verify time-sensitive details before acting*

These two tracks round out the four. The FDE track is mapped separately (`fde-market-research.md`, `fde-live-openings.md`, `fde-interview-format.md`). All four share the same prep core; what differs is emphasis and a few track-specific skills.

---

## Trading firms / hedge funds (the moonshot)

**Verdict:** highest bar, best payoff, and the track where Randy's self-taught market-structure depth is a genuine, uncommon edge. The honest constraint: many top quant-dev roles lean on C++ and/or advanced math credentials Randy doesn't lead with. But there's a real, growing **Python-first** lane he fits.

### What the market actually wants
- **Python is first-class** for the research/infra/systematic-trading lane (pandas, NumPy; often PyTorch/scikit-learn for ML strategies). C++ dominates the *low-latency execution* lane — a different, harder-to-enter niche.
- Recurring infra asks that **map directly onto Randy's existing skills**: distributed computing incl. **Kubernetes**, **event-based architectures**, real-time data pipelines, CI/CD, time-series/high-frequency databases (KDB is a plus-to-know). His Docker/Kubernetes/Kafka/TimescaleDB build-up was well aimed.
- Domain understanding: fixed income, swaps, futures, FX for macro desks; market microstructure for HFT-adjacent shops. Randy's derivatives/perps/funding-rate fluency is real but crypto-flavored — translating it to traditional-markets vocabulary matters.
- Comp: quant dev typically ~$100-200K base, $300K+ all-in at top firms; front-office and senior far higher.

### Where to look
- **OpenQuant** (openquant.co) — the dedicated quant job board; best single source.
- **eFinancialCareers**, **Goliath Partners** and similar specialist recruiters (they run much of this market — worth contacting directly).
- Named firms hiring the Python/systematic lane: D.E. Shaw (Equities quant, Quant-Systems Cloud Engineer), Arrowstreet, plus many $5-60B AUM prop shops and funds (often via recruiters, frequently NYC/Chicago).
- **Crypto-native trading firms** — likely Randy's *best-fit* sub-lane: his crypto market-structure expertise is directly relevant rather than translated. Worth a dedicated search (prop shops and market-makers in digital assets).

### How to position
- Lead with the **real-time market-data platform** (Anchor Project 1) — it's a systematic-trading-infra artifact: live market data, time-series storage, event-driven, containerized. Speak to it in their vocabulary.
- Translate crypto fluency into general market-structure language (order books, microstructure, funding/basis as a carry analogue).
- Interviews skew harder on probability/stats/math + low-latency thinking than the other tracks. Add a probability/brainteaser strand to LeetCode prep for this track specifically.

### Honest caveat
Without a C++ low-latency background or a quant-finance graduate credential, the elite HFT execution roles are a stretch. The realistic targets are **Python/systematic-research infra**, **crypto-native trading firms**, and **fintech-adjacent quant** — all genuinely open to his profile. Treat the top pure-quant shops as lottery tickets, not the base case.

---

## Regular backend / tech (the reliable baseline)

**Verdict:** broadest volume, most predictable loop, the floor that guarantees the hunt doesn't come up empty. The shared prep core *is* this track's prep — little extra needed.

### What the market wants (and what Randy is building)
- Strong language + fundamentals (his Python), plus the modern stack the deep plan already targets: **FastAPI, Docker, Redis, PostgreSQL, Kubernetes, CI/CD, a cloud (AWS or GCP)**.
- System design: load balancing, caching, DB tradeoffs (SQL/NoSQL, OLTP/OLAP), queues/Kafka, sharding/replication, rate limiting, consistency/availability. Randy is already "decent" here per the deep plan.
- The two anchor projects cover this track's portfolio needs outright — no track-specific build required.

### Where to look
- Standard boards (LinkedIn, etc.) at high volume; this is the track to apply to broadly and early for interview reps.
- Strong adjacent targets given Randy's background: **fintech** (domain fit), **AI-infra / LLMOps-flavored backend** (Anchor Project 2's eval/observability work qualifies him; LLMOps is a fast-growing, well-paid adjacent category), and **data-infrastructure** roles.

### How to position
- Cleanest, most conventional resume version: lead with engineering substance and the modern-stack projects.
- Use this track to generate early interviews and momentum while the FDE and trading angles mature.

### Interview shape
- The most LeetCode-standard of the four (mediums, the usual patterns) plus classic system design. This is where the bulk of the LeetCode grind pays off; FDE/trading reuse it with different emphasis.

---

## How the four tracks share prep (recap)

| Element | Backend | FDE | Trading | Sales Eng |
|---|---|---|---|---|
| LeetCode (patterns) | Core | Lighter (practical coding) | Core + prob/stats | Light |
| System design | Core | Decomposition case study | Core + low-latency/order-book | Light |
| Anchor Project 1 (market data) | ✓ | ✓ | ✓✓ | ✓ |
| Anchor Project 2 (agent+eval+MCP) | ✓ (LLMOps angle) | ✓✓ | ~ | ✓ |
| Modern stack (FastAPI/Docker/Redis/k8s) | ✓✓ | ✓ | ✓ | ~ |

Build the core once; point it four directions. (Sales-engineer track is the cheap parallel net — same artifacts, presentation-forward framing; not separately mapped here.)

---

## Suggested next research (not yet done)
- Live, specific open reqs for the trading Python/systematic lane and crypto-native firms (like the FDE live-openings file).
- Backend live-openings batch in fintech / AI-infra.
- LeetCode pattern schedule with the per-track emphasis baked in.
- Backend and trading resume angles (FDE angle is drafted in `resumes/fde-resume-bullets.md`).
