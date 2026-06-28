# Randy — Job Hunt Repo

A self-contained workspace for Randy's post-BofA job hunt. Built June 2026. Drop this whole folder into a fresh chat and the assistant has everything it needs to pick up without re-explaining.

## Situation in brief

Randy was let go from a backend Python role at Bank of America in June 2026 (an ex reported a pseudonymous personal social account to HR; no real-name or bank affiliation on it; at-will termination, no severance). He's treating it as an overdue reset rather than a crisis — he has solid cash runway, filed for unemployment, and wants to land somewhere better in a modern stack. Background: Cornell CS, prior ML at Microsoft, deep self-taught fluency in crypto market structure / derivatives / trading, and serious intellectual range. Strong in person, good presence — not just a heads-down coder.

## The strategy in one breath

Four job tracks, **one shared prep core** (LeetCode + a modern-backend project + system design) with four resume angles layered on top. Tracks, in priority order:

1. **Forward-deployed engineer (FDE)** — primary; best-fit and a hiring surge right now.
2. **Regular backend / tech** — reliable high-volume baseline.
3. **Trading firms / hedge funds** — moonshot; highest bar, best payoff, real edge from his market-structure depth.
4. **Sales engineer / tech sales** — cheap parallel net given his presence.

~6-8 hrs/day, treating the hunt like a job. Apply from week 2 — don't wait to "feel ready."

## What's in here

```
plan/
  00-master-plan.md             Overall reset plan: admin, lawyer, lease, job hunt, longer-term
  01-job-hunt-deep-plan.md      The deep four-track plan: daily structure, upskilling, projects, resumes
research/
  00-refresh-late-june.md       READ FIRST — the diff: what changed/sharpened on re-verification
  fde-market-research.md        Live FDE market snapshot + tiered target companies
  fde-live-openings.md          Specific open reqs + where to apply
  fde-interview-format.md       How FDE interviews actually run — distinct from LeetCode loops
  backend-trading-market-maps.md  Backend + trading track market maps + how all four share prep
projects/
  anchor-project-2-spec.md      Agentic tool + eval harness + MCP server (the highest-ROI build)
resumes/
  fde-resume-bullets.md         Draft FDE bullets mapped to real JD language
  backend-trading-resume-angles.md  Backend + trading angles, mapped to real 2026 JD vocabulary
prep/
  execution-tracker.md          THE file that matters — apps, projects, mocks; enforces shipping over planning
  prep-schedule.md              Per-track LeetCode + case-study + system-design schedule (calibrated to 2026 loops)
  agentic-engineering-skill-guide.md  Running agents unattended + CI/CD — and why it IS the FDE portfolio
```

## Status / next actions (update as you go)

- [ ] Call 3-4 more employment lawyers (consultation, not "I want to sue")
- [ ] Termination letter arriving by mail (~10-14 days from ~June 25) — file it
- [ ] Appeal/dispute callback with employee relations — Wednesday
- [ ] Master resume + 4 angles
- [ ] Begin Anchor Project 1 (market-data platform) while learning FastAPI/Docker/Redis
- [ ] Begin Anchor Project 2 (agentic + eval + MCP) — the FDE-track centerpiece
- [ ] Start applying (backend + FDE first) by end of week 2

## Still to research (most of the original list is now done)

The late-June refresh and follow-up passes closed nearly all of this. The backend/trading resume angles are now drafted (`resumes/backend-trading-resume-angles.md`), and the per-track prep schedule exists (`prep/prep-schedule.md`). What genuinely remains is *narrow and on-demand*:
- Live, specific open reqs for the **trading** Python/systematic + crypto-native lane, at the same link-level resolution as the FDE openings file (the angle and target firms are mapped; specific current reqs aren't pulled).
- A live **backend** fintech/AI-infra openings batch, if/when you want it.

**Execution-freeze note:** the planning surface is now large enough that *adding more of it is the trap.* The plan itself warns against disappearing into prep. From here, new artifacts should be shipped projects, sent applications, and completed mock interviews — tracked in `prep/execution-tracker.md` — not more strategy. If a week produced no application and no committed code, that's the signal, regardless of how much was read.

## How to use this in a new chat

Paste the folder or the relevant files and say what you want next — e.g. "map the trading-firm track like the FDE one," "draft the backend resume," "build my week-1 plan for Anchor Project 1," or "turn fde-live-openings into a tracked application sheet." The master plan and deep plan hold the strategy; the research files hold the live market facts as of late June 2026 (re-verify anything time-sensitive).
