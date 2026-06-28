# Research Refresh — what changed since the June 25 drafts

*Re-verified late June 2026. Read this first; it amends the other research files where they've drifted.*

This file is the diff. The original research was directionally right — the FDE thesis holds, the surge is real and still climbing, the comp bands are intact. What follows is what got **sharper, newly-true, or wrong** on re-verification, ordered by how much it should change your behavior this week.

## 1. Evals is even more decisive than the files say — and the gap is specific

The original plan correctly flagged eval engineering as the 2026 non-negotiable. The re-verification makes it starker: across multiple current interview write-ups, **inability to whiteboard an LLM-as-Judge eval suite is the single most common final-round rejection at OpenAI and Anthropic, reportedly filtering ~70% of otherwise-strong candidates.** This is the highest-leverage skill in the entire plan.

But "learn evals" is too vague. The specific, gateable competency is:

- **LLM-as-Judge** scoring, and crucially **why naive LLM-as-Judge fails on multi-turn agent traces** (the judge loses the thread across turns, rewards plausible-but-wrong intermediate steps, and can't localize *where* a trajectory went bad). Be able to explain the failure and at least one mitigation.
- **Regression suites with a golden dataset** — a fixed set of inputs with known-good outputs you re-run on every change to catch drift.
- **Drift / regression detection** — how you'd notice the agent silently got worse after a prompt or model change.
- **Tracked failure modes** — categorizing *how* it fails, not just a pass/fail number.

If Anchor Project 2's eval harness demonstrates exactly these four things, you've built the answer to the question that fails most people. That's the single best use of build time in this whole repo. (Spec updated accordingly.)

## 2. "No prior FDE title" is itself a named rejection reason — so positioning is near-free alpha

A recurring hiring-manager rejection note is simply *not having held the FDE title before*. You can't fabricate the title, but you can defang it cheaply:

- **Rewrite your LinkedIn headline + recent-role bullets now** to include the exact recruiter filter terms: *"production AI systems," "evals," "RAG," "agent," "forward deployed."* Reports put recruiter inbound roughly doubling within ~2 weeks of this change. This is a 30-minute task with a multi-week payoff and it's currently not in your week-1 list. **Do it this week.**
- Lead the resume summary with the *hybrid, customer-facing* nature of the role explicitly named (not a generic "backend engineer" opener — ATS and humans both look for the hybrid framing up top).

## 3. TypeScript / a thin frontend matters more than the repo assumes

~35% of FDE postings mention TypeScript, and the reason is concrete: **FDEs build customer-facing dashboards.** Your plan is pure backend. You don't need to become a frontend engineer, but one of your anchor projects should ship a *thin* React/TS surface (even a single dashboard page) so you can say "I stood up the customer-facing view too." Anchor Project 1's dashboard already covers this if you build the front end in React rather than a Python templating shortcut — so just make that choice deliberately.

## 4. Regulatory fluency is now a named FDE skill — and it's a Randy edge

New since the drafts: interview guides now list **regulatory/compliance fluency** as a differentiator, specifically the **EU AI Act high-risk-system obligations (phasing in August 2026)** and sector rules in financial services and healthcare. Your regulated-bank background is a genuine moat here that AI-native candidates can't match. Add one line to your prep: be able to speak for two minutes on "what changes about deploying an AI agent into a regulated financial-services environment" (data residency, auditability, change-control windows, human-in-the-loop gates). This converts your BofA time from "legacy baggage" into a named, scarce qualification.

## 5. The interview shape, confirmed and sharpened

The `fde-interview-format.md` picture is correct. Refinements worth baking in:

- **Two coding rounds, one explicitly LLM-flavored** at OpenAI; the LLM one deliberately under-specifies the problem. The gradable signal is **what you do in the first ~30–60 seconds**: candidates who start coding fail; candidates who ask "who is the customer? what does the eval set look like?" advance at materially higher rates. This is trainable — rehearse the clarify-first reflex until it's automatic.
- **System design uses new primitives.** Not "scale a REST API" — they want token cost, latency budgets, eval gates, RAG pipelines, agent loops, prompt versioning woven into the whiteboard. Practice one end-to-end LLM-product design out loud.
- **The CISO simulation is graded on holding a technical line under pressure**, not eloquence. When the simulated stakeholder demands an impossible SLA or misunderstands model privacy, you course-correct gracefully without caving and without alienating them. Practice this live with a person, not solo.
- **SQL is table stakes** — CTEs, window functions, messy joins on large tables, "find the anomaly in this usage data." Cheap to drill, shows up reliably. Add a small SQL strand to prep.

## 6. Comp / market specifics, refreshed

- Median advertised base still ~$174–180K; Levels-style total comp averaging ~$238K; senior at the labs (OpenAI/Anthropic) reportedly clearing **$785K+** total at the top. Bands remain **bifurcated and unstable** ($53K to $1.2M across the posting set) — benchmark every offer aggressively.
- **~81% of postings include equity** (unusually high — reflects how venue-backed the hiring is). Factor equity quality, not just base, into comparisons.
- **~58% of FDE roles are at 11–200-person companies.** The growth-stage startup is the modal employer, not the frontier lab. Your "wore all the hats / founder-mindset" energy reads as *native* there. Don't over-index on the lab moonshots; the Tier-2/3 volume is where reps and offers actually come from.
- **Remote ~34%** (lower than general SWE — customer presence is the value). Relocation openness remains a real advantage.
- **NYC has overtaken SF** as the primary hub (regulated industries cluster East Coast). Given your relocation openness and finance background, weight NYC.

## 7. One honest reframe on sequencing

The biggest risk in this repo is not its content — it's that it keeps growing. Every research pass adds more to read. The plan itself warns against disappearing into prep, and the planning surface is now large enough that *expanding it further is the trap.* The corrective: from here, the repo is in **execution-freeze** on planning. New artifacts should be *shipped projects, sent applications, and completed mock interviews* — not more strategy docs. The `prep/execution-tracker.md` file exists to enforce this: if a week produced no application and no committed code, that's the signal something's wrong, regardless of how much was "learned."
