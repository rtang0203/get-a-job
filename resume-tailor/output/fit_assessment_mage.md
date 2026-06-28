# Fit Assessment: Senior AI Infrastructure Engineer — Mage (mage.space)

## 1. Hard Gates

| Gate | Status |
|------|--------|
| **Work authorization** | ✅ U.S. Citizen — no issue |
| **Location** | ⚠️ NYC in-person preferred; remote OK for exceptional candidates. Randy open to relocation — confirm NYC willingness. |
| **Seniority** | ⚠️ Stretch. "Senior" role owning GPU inference infrastructure end-to-end; Randy has ~4 years, primarily at one company, in a different domain. |
| **Non-negotiable credentials** | ⚠️ Required: FastAPI, Modal, Google Cloud. Randy has FastAPI (familiar, undocumented in projects), **zero Modal experience**, **zero GCP experience**. |

## 2. Genuine Strengths

| Strength | JD Requirement |
|----------|----------------|
| Strong Python proficiency (primary language across all roles) | "excellent Python" |
| High-throughput pipeline design (tens of millions txns/day) | "production orchestration…retries…error handling" |
| API design experience (reference-data framework, inter-service interfaces) | "Design clean, consistent APIs" |
| Concurrency and parallelization (backreporting service) | "concurrency, autoscaling" (partial) |
| Docker experience (Market Data Dashboard) | "Docker" in tech stack |
| LLM API integration (Reading Recommendations App w/ Gemini) | Tangential to generative AI ecosystem |
| ML data processing (Microsoft — data for training ML models) | General ML familiarity |
| Cornell CS degree | Engineering credibility |

## 3. Real Weaknesses / Gaps

| Gap | Severity |
|-----|----------|
| **No Modal experience** — core required tool, central to their inference stack | Critical — required |
| **No Google Cloud experience** — JD requires GCP (Cloud Run, GCS) | Critical — required |
| **No GPU deployment/inference experience** — no PyTorch, no model serving, no cold-start/autoscaling | Critical — this IS the job |
| **No diffusers/generative model ecosystem** — no image/video model work | Significant — strongly preferred |
| **FastAPI undocumented** — listed in skills but no project/job uses it | Moderate — hedgeable but will be probed |
| **No Redis experience** | Minor |
| **No pytest visible** | Minor |
| **No GitHub Actions / CI/CD ownership** | Minor |

## 4. Verdict

**Stretch / likely under-qualified.** The core job is GPU inference infrastructure, model serving, and autoscaling — Randy has zero documented experience in any of these. Three of four "required" tools (Modal, GCP, FastAPI-in-practice) are gaps. Python pipeline engineering is real but aimed at financial data, not GPU model serving. Best path to this role: build a project using Modal + diffusers + FastAPI to serve an image model, then reapply.
