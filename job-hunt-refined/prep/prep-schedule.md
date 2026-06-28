# Prep Schedule — Coding, Case Study & System Design

*Drafted late June 2026 · per-track emphasis baked in · calibrated to current 2026 loops*

## The governing principle (read this before the schedule)

Every current source says the same thing, so internalize it: **150 problems solved deliberately and twice beats 500 solved once.** LeetCode "hoarding" is the named failure mode. Across all four of your tracks the algorithmic bar is *medium*, not hard — your differentiation is system design, communication, and (for FDE) case studies, not your hard-problem count. Do not let LeetCode crowd those out. The repo already warns against prep crowding out applying; this file is scoped so it can't.

One reflex matters more than any single pattern, and it shows up graded in *every* track's loop: **spend the first 3–5 minutes clarifying and planning before you write code.** Jumping straight to code is the single most common rejection reason in FDE case studies and a red flag in backend loops too. Drill this until it's automatic.

## What each track's loop actually weights (so you prep proportionally)

| | LeetCode | System design | Case study / practical | Communication / behavioral | Track-specific |
|---|---|---|---|---|---|
| **Backend** (baseline) | Medium fluency, core | "What happens when this fails?" ×3 — heavy | Take-home or pair-on-codebase common | STAR stories, ownership | — |
| **FDE** (primary) | De-emphasized; practical coding only | LLM-primitive design (token cost, eval gates, latency) | **Decomposition case study — the gating round** | CISO sim, "I" not "we" — heavy | Evals whiteboard; mission-fit (labs) |
| **Trading** (moonshot) | Core + **probability/stats/brainteasers** | Order-book / low-latency / time-series | — | Lighter | Translate crypto→TradFi vocab |
| **Sales eng** (net) | Light | Light | Demo / explain-to-non-technical | Presence-forward — heavy | — |

The backend loop in 2026 commonly runs: 45-min screen → 60-min coding → 75-min system design/scenario → 45-min behavioral. The senior-leaning version replaces the whiteboard puzzle with "walk through a real bug/feature in a small existing codebase" — so practice *reading unfamiliar code and narrating*, not just solving cold problems. FDE runs 5–8 stages over 3–6 weeks with the case study as the hidden filter.

## LeetCode: the list and the cadence

Use **Blind 75** first, then extend toward **NeetCode 150**. Organize by pattern, not by random solving. With your hours, ~3–5/day is sustainable; the goal over the hunt is ~150 quality problems with real pattern retention.

**Pattern priority (highest interview frequency first):**
1. Arrays / strings (~35% of problems — most frequent)
2. Hashmaps / sets
3. Two-pointer / sliding window
4. Stack / queue
5. Trees (DFS + BFS)
6. Graphs (BFS/DFS, union-find)
7. Heaps / priority queue
8. Binary search
9. Intervals
10. Dynamic programming (don't over-invest — lower frequency, high time-cost; know the common forms)

**For the trading track only, add a probability/stats strand:** expected value, conditional probability, classic brainteasers (the kind quant desks ask), basic combinatorics. ~20–30 min a few times a week is enough to not get blindsided; you're not retraining as a quant.

**The 12 to have cold** (re-solvable in ~25 min each with correct complexity): Two Sum, Valid Parentheses, Merge Two Sorted Lists, Best Time to Buy/Sell Stock, Valid Palindrome, Invert Binary Tree, Binary Tree Level-Order Traversal, Number of Islands, Climbing Stairs, Coin Change, Longest Substring Without Repeating Characters, Merge Intervals. If these are automatic, you're coding-ready for 90% of the loops you'll see.

## System design: patterns to have cold

You're already "decent" here — sharpen, don't rebuild. The single highest-signal drill: take any familiar system and be able to answer **"what happens when this fails?"** three times — once for the database, once for the queue, once for a downstream service — each with a specific recovery strategy, retry behavior, and a *named* consistency tradeoff. That one habit separates strong distributed-systems candidates from thin ones in 2026 backend loops.

Core patterns: load balancing, caching layers (and invalidation), SQL vs NoSQL + OLTP vs OLAP, sharding/replication, message queues (Kafka), rate limiting, idempotency, consistency/availability tradeoffs. Reference: *Designing Data-Intensive Applications* (Kleppmann) — replication/partitioning/consistency chapters — and the System Design Primer on GitHub.

**Track-specific system design:**
- **Trading:** order-book design, low-latency considerations, time-series/high-frequency storage, event-driven architecture. Translate your crypto market-data platform into this vocabulary.
- **FDE:** design with the *new primitives* — token cost, latency budgets, eval gates, RAG pipelines, agent loops, prompt versioning. Practice one LLM-product design end-to-end out loud (e.g. "naive RAG is 1.5s, customer needs sub-100ms — get there"). This is where traditional SWEs stumble; it's a direct edge if you've built Anchor Project 2.

## The FDE case study (your highest-ROI, most-overlooked drill)

This is the gating round and the most trainable one. The structure to internalize — a clarify-first decomposition:

1. **Clarify and scope** before anything (the first-60-seconds signal). "What does success look like? Who's the user? What does the data look like? What's the budget/timeline? What does failure cost?"
2. **Identify the customer / who benefits.**
3. **Restate the problem** in your own words.
4. **Decompose** into small solvable chunks.
5. **Propose a simple MVP**, then iterate out loud showing first-principles reasoning.
6. **Evaluate tradeoffs** (technical / business / timeline) and **pick one**, justified.

Practice prompts (rehearse out loud, 45–60 min each): the 911-response-time one, the regional-bank fraud-detection-across-three-acquired-systems one, the logistics-agent-rerouting-with-an-eval-suite one. The point is never the answer — it's that you *don't jump to a solution.*

## The communication rounds (don't skip — equally weighted in 2026)

- **CISO / frustrated-VP simulation** (FDE): hold a technical line under pressure without caving and without alienating the stakeholder. When they demand an impossible SLA or misunderstand model privacy, course-correct gracefully. **Must be practiced live with a person role-playing** — solo rehearsal doesn't build this.
- **Behavioral**: 3–5 STAR (or SOAR) stories from real work — conflict, a failure, a complex cross-functional problem, impact you owned. Rehearse aloud. FDE screens hard for **"I" not "we"** — own the individual slice.
- **The AI-tools question** ("how do you use AI coding assistants?") is now common: the right answer is "first draft, not finished product — I review for the subtle coherence issues AI introduces." You can speak to this credibly from the agentic-engineering work.
- **"Why this company?"** must be specific. "I like hard problems" dies on follow-up. For labs, invest real time in mission-fit articulation.

## An 8-week shape (overlay on the deep plan's weekly arc, don't replace it)

This sequences prep so mocks — the part that actually moves outcomes — happen *while* you apply, not after.

- **Weeks 1–2 — fundamentals reset.** Big-O refresh; 2 easy + 1 medium/day; the 12 cold problems. Start the clarify-first habit on every problem. Write the first 3 STAR stories.
- **Weeks 3–4 — patterns.** Work Blind 75 → NeetCode 150 by pattern, timed, out loud. Begin system-design "what fails?" drills. First FDE case-study rehearsals. (Trading: start the probability strand.)
- **Weeks 5–6 — mocks, the real lever.** 3 mocks/week with a partner/Pramp/Interviewing.io — mix coding, system design, and at least one **live CISO/case-study sim**. Record one; review your own delivery (unclear narration is a silent killer). Real interviews are landing now — let them retarget your prep.
- **Weeks 7–8 — ramp down + close.** No new topics. Re-solve familiar problems for pattern retention. Tighten "why this company" per active loop. Mostly interviewing and patching the specific gaps loops expose.

Past week 8, the loop is just: apply → interview → patch the exact gap that round revealed. The mocks and the case-study reflex are what compound; the LeetCode count is not.
