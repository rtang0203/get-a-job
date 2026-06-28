# resume-tailor

A repeatable skill that tailors Randy Tang's master resume to a specific job description
and emits a clean one-page PDF.

## Layout
```
resume-tailor/
├── SKILL.md                  # the playbook the agent follows (read this first)
├── README.md                 # this file
├── master/
│   ├── resume.json           # structured source of truth (facts)
│   └── resume_master.md      # human-readable master
├── scripts/
│   ├── build_resume.py       # one-page PDF builder (derives defaults from resume.json)
│   ├── fit_rubric.md         # honest fit-assessment rubric
│   └── track_application.py  # appends to output/applications.json after each run
├── examples/
│   └── imc_content.json      # worked example: IMC AI-Powered Engineering role
└── output/
    ├── applications.json     # tracker: every tailoring run (verdict, action, gaps)
    ├── *_override.json       # per-company override files
    └── *.pdf                 # generated resumes
```

## How to run (Claude Code)
1. Drop this folder in your repo. Claude Code auto-discovers `SKILL.md`.
2. Prompt: *"Use the resume-tailor skill on this JD: <url or pasted text>."*
3. The agent will: fetch/parse the JD → write an honest fit assessment with recommended
   action → tailor a content override → run the builder → verify one page → suggest a
   gap-closing project → track the application → report a changelog.

## How to run (any agent / manually)
```bash
pip install reportlab --break-system-packages
# Build from resume.json defaults (generic resume):
python3 scripts/build_resume.py
# Build with a partial override (only changed fields needed):
python3 scripts/build_resume.py output/mage_override.json
# Track the application:
python3 scripts/track_application.py --company Mage --role "Senior AI Infra Engineer" \
  --verdict stretch --action "Build project first, then apply" \
  --pdf Randy_Tang_Resume_Mage.pdf --notes "Gaps: Modal, GCP, GPU inference"
```

## Maintenance
- When your career changes, update **both** `master/resume.json` and `resume_master.md`.
  The build script derives all defaults from `resume.json` — no hardcoded content to drift.
- **Fill in `work_authorization`** in `resume.json` — it gates no-sponsorship roles.
- Override JSONs only need the fields you want to change; they're deep-merged over the
  defaults derived from `resume.json`.
- Review `output/applications.json` to see all tailoring runs at a glance.
