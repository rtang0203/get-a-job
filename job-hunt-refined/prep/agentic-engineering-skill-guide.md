# Skill Guide — Agentic Engineering & Running Agents Autonomously

*Drafted late June 2026 · this is the "let agents loose for extended periods" skill you asked for*

## The reframe that makes this the highest-ROI thing in the repo

You asked to learn two things on the side: CI/CD pipelines, and how to set up environments and plans so you can let agents run unattended for long stretches. Here's the thing worth seeing clearly:

**The skills that make an agent run reliably unattended are the same skills FDE interviews screen for.** They are nearly a one-to-one map:

| Make an agent run unattended | What the FDE loop calls it |
|---|---|
| A success oracle (tests/eval the agent checks itself against) | **Eval engineering** — the #1 gating skill |
| Progress file + structured handoff between sessions | Deployment artifacts that "survive your rotation" |
| Structured logging of every agent step | **Agent observability** |
| Scoped, sandboxed tool permissions | Guardrails / "prove the agent is safe to the security team" |
| CLAUDE.md as the spec the agent works from | Turning a fuzzy problem into a written spec |
| Git commit after every unit of work | Production hygiene |
| Versioned prompts you can roll back | A named recurring interview question |

So this isn't a side quest. Learning to run agents well **is** building the FDE portfolio, and vice versa. Build Anchor Project 2 *using* an autonomously-run agent harness, and you get the artifact and the skill in one motion — plus a true, specific war story for every interview question in the loop.

## The core pattern for long-horizon autonomous runs

This is the consensus pattern across Anthropic's own engineering writeups and practitioner guides. The single idea underneath all of it: **the agent's context window fills up and degrades, so the system has to survive context loss.** Everything below is a consequence of that.

1. **Two-phase harness: an initializer, then a loop.**
   - The *first* session runs a specialized prompt that sets up the environment: an `init.sh` to rebuild state, a `progress.txt` (or `claude-progress.txt`) log, and an initial git commit. This is a different prompt from every later session.
   - *Every subsequent* session reads the progress file + git history to reconstruct state, makes **incremental** progress, then writes a structured update before it runs out of context. The failure mode to design against is the agent trying to one-shot the whole thing and running out of context mid-feature, leaving the next session to guess.

2. **CLAUDE.md is the spec, and the agent can edit it.** Put the deliverables, constraints, and design decisions in a root `CLAUDE.md`. It stays in context and the agent references it as the plan. Crucially, let the agent update it as it learns — that's how decisions persist across context windows. Keep it lean (a practitioner rule of thumb: under ~200 lines; use `.claude/rules/*.md` with path globs for the rest).

3. **A success oracle is non-negotiable.** The agent can only run unattended if it can tell whether it's making progress *without you*. That means a reference implementation, a quantifiable objective, or — most often — a **test/eval suite it runs continuously** and is told to expand as it works. This is the same artifact as your FDE eval harness. No oracle = no safe unattended run. This is the load-bearing piece.

4. **Git as the coordination + recovery layer.** Commit and push after every meaningful unit. Recoverable history if a run goes sideways, visible progress, and nothing lost if the session dies mid-task.

5. **Show evidence, don't assert success.** Instruct the agent to surface the actual test output / command results / a screenshot rather than claiming "done." Reviewing evidence after an unattended run is far faster than re-verifying from scratch — and it's exactly the "how do you know it actually works" discipline the eval interview tests.

6. **Verification by a *separate* agent.** The agent doing the work shouldn't be the one grading it (it'll learn to pass its own tests rather than meet the spec — a real, documented failure mode). Spin up a reviewer subagent with fresh context to try to refute the result. Tell the reviewer to flag only gaps that affect correctness or the stated requirements, or it'll over-engineer.

7. **Context hygiene.** Practitioner consensus: results degrade as context fills — a "dumb zone" around ~40% on long-context models, real "context rot" by ~300–400k tokens. Keep sessions focused (one task, not a kitchen-sink session), and wrap up / hand off before quality drops rather than pushing a window to its limit.

8. **Scoped permissions over "skip all permissions."** Use wildcard allowlists (`Bash(npm run *)`, `Edit(/docs/**)`) and/or sandbox isolation rather than blanket bypass. For a truly unattended run, an auto-mode classifier that auto-approves safe commands and pauses on risky ones (data deletion, network egress) is the safer default. This *is* the guardrails story FDE interviews want.

## A concrete way to practice it (do this with Anchor Project 2)

Don't learn this abstractly. Set up the harness on the lead-gen agent build and let it run:

1. Write a tight `CLAUDE.md`: the deliverable (agent that ingests messy business data → enriches → scores leads → structured output), the constraints, and the definition of done tied to **eval metrics** (e.g. lead-score precision on a golden set).
2. Stand up the eval suite *first*, as the success oracle. Golden dataset of hand-labeled leads; LLM-as-Judge for the fuzzy "is this enrichment good" parts; regression run on every change.
3. Write the initializer prompt (env + progress file + first commit), then a loop prompt that makes incremental progress and updates the progress file.
4. Run it unattended in a sandbox. Come back, read the evidence (test output, commits, progress log), and spin a reviewer subagent to find gaps.
5. Keep a plain-language log of what broke and what you changed. *That log is your interview gold* — every entry is a true "here's a tradeoff I hit" story.

You finish with: the FDE portfolio centerpiece, hands-on autonomous-agent experience, and a stack of real war stories — from one build.

## CI/CD — the other thing you asked for

CI/CD is cheap to add and signals professional habits, and it slots directly into the agentic workflow (agents can run non-interactively inside CI). Minimum viable competence for interviews:

- **GitHub Actions on every repo.** A workflow that runs on push: install deps → lint → run tests → build the Docker image. This alone clears the "do you practice CI" bar.
- **Gate merges on the test/eval suite.** For the agent project, make the eval suite a CI gate — i.e. a regression in lead-score precision fails the build. This is a genuinely strong thing to show: *"my CI won't let a prompt change ship if it regresses the eval."* That sentence maps onto the "eval gates" primitive the OpenAI system-design round wants.
- **Run an agent in CI non-interactively.** Claude Code's `-p` / non-interactive mode runs in CI, pre-commit hooks, or scripts (`claude -p "..." --output-format stream-json`). Even a small example — an agent that reviews a PR diff in CI and comments — is a current, credible artifact and a talking point most candidates don't have.
- **Don't over-build.** You need *one* repo with a clean, real pipeline you can explain end-to-end, not a DevOps certification. One true tradeoff story ("I cached the Docker layer build because the eval step was slow; here's what I'd do for matrix testing") beats breadth.

## What "good" looks like by the end

A public repo where: a vague spec in `CLAUDE.md` drives an agent that you can kick off and walk away from; it self-checks against an eval suite; CI gates merges on that suite; every step is logged; a reviewer agent double-checks the work; and the README reads as a deployment case study (problem → architecture → evals → what they caught → tradeoffs → next steps). That single repo is simultaneously: your FDE centerpiece, your evals proof, your observability proof, your CI/CD proof, and your "I run agents autonomously" proof. Build it once, point it everywhere.
