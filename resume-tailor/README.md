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
│   └── resume_master.md      # auto-generated human-readable master
├── scripts/
│   ├── build_resume.py       # one-page PDF builder (format-2 semantic overrides + legacy)
│   ├── fit_rubric.md         # honest fit-assessment rubric
│   ├── gen_master_md.py      # regenerate resume_master.md from resume.json
│   └── track_application.py  # appends/updates output/applications.json after each run
├── examples/
│   └── imc_content.json      # worked example: IMC AI-Powered Engineering role (legacy format)
└── output/
    ├── applications.json     # tracker: every tailoring run (verdict, action, gaps)
    ├── *_override.json       # per-company override files
    ├── *_jd.txt              # archived job description text
    ├── fit_assessment_*.md   # fit assessment files
    └── *.pdf                 # generated resumes
```

## How to run (Claude Code)
1. Drop this folder in your repo. Claude Code auto-discovers `SKILL.md`.
2. Prompt: *"Use the resume-tailor skill on this JD: <url or pasted text>."*
3. The agent will: fetch/parse the JD → archive it → write an honest fit assessment →
   tailor a format-2 override → run the builder → verify one page → suggest a gap-closing
   project → track the application → report a changelog.

## How to run (any agent / manually)
```bash
pip install reportlab --break-system-packages
# Build from resume.json defaults (generic resume):
python3 scripts/build_resume.py
# Build with a format-2 override:
python3 scripts/build_resume.py output/williamblair_override.json
# Build with a legacy override (still supported):
python3 scripts/build_resume.py output/akuna_override.json
# Track the application (deduplicates on company+role):
python3 scripts/track_application.py --company Mage --role "Senior AI Infra Engineer" \
  --verdict stretch --action "Build project first, then apply" \
  --pdf Randy_Tang_Resume_Mage.pdf --notes "Gaps: Modal, GCP, GPU inference"
# Regenerate resume_master.md after editing resume.json:
python3 scripts/gen_master_md.py
```

## Format-2 override schema

Format-2 overrides are **semantic**: they reference master data by name and only provide
fields that differ. The build script pulls titles, dates, stacks, and descriptions from
`resume.json` and renders HTML automatically. Use `**bold**` markers for emphasis.

Set `"format": 2` to opt in. Legacy overrides (without this key) still work via deep-merge.

```jsonc
{
  "format": 2,
  "company_slug": "AcmeCorp",                // used in PDF filename
  "summary": "Custom summary with **bold** markers.",
  "contact_extras": ["U.S. Citizen"],         // appended to email | phone

  // Skills: structured categories. "join_next" puts the next category on the
  // same line separated by |. Without it, each category gets its own line.
  "skills": [
    {"label": "Languages", "items": ["Python", "SQL"], "join_next": true},
    {"label": "Infra", "items": ["Docker", "Postgres"]},
    {"label": "AI", "items": ["LLM APIs", "prompt engineering"]}
  ],

  // Experience: keyed by company name from resume.json.
  // Simple form: list of bullet strings (title/dates/team/stack come from master).
  // Dict form: {"bullets": [...], "stack": ["override", "stack"]}.
  // Omitted companies use master bullets unchanged.
  "experience": {
    "Bank of America": [
      "Bullet one with **bold** emphasis.",
      "Bullet two."
    ],
    "Microsoft": [
      "Single concise bullet."
    ]
  },

  // Projects: "include" controls which projects appear and in what order.
  // "overrides" lets you customize desc and/or stack per project.
  // Omit "include" to use all projects in master order.
  "projects": {
    "include": ["Project A", "Market Data Dashboard"],
    "overrides": {
      "Project A": {
        "desc": "Custom description with **bold**.",
        "stack": ["Python", "Docker"]
      }
    }
  },

  // Education: only override bullets if needed. Degrees/dates come from master.
  "education": {
    "bullets": ["Custom activity line with **bold**."]
  }
}
```

### What format-2 eliminates
- No more copying role titles, dates, team names, or stack lists into overrides.
- No more writing raw HTML (`<b>`, `&mdash;`, `&nbsp;`). Use `**bold**` instead.
- No more retyping the full skills section as an HTML string.
- No more duplicating unchanged experience or project entries.
- Project ordering/filtering is a simple `include` list, not copy-paste-reorder.

### Page-count check
The build script now validates page count after every build:
- `OK: 1 page.` — good to go.
- `WARNING: Resume is N pages (target is 1). Trim content.` — cut bullets or projects.

## Maintenance
- When your career changes, update `master/resume.json` then run
  `python3 scripts/gen_master_md.py` to regenerate the markdown. One source of truth.
- **Fill in `work_authorization`** in `resume.json` — it gates no-sponsorship roles.
- Review `output/applications.json` to see all tailoring runs at a glance.
  The tracker deduplicates on company+role — re-tailoring updates the entry, not duplicates.
