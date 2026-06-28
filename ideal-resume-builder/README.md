# ideal-resume-builder

A repeatable skill that builds a fictional "ideal" resume for any target job description under the name **Xianglong Tang**. It fabricates optimal experiences, education, and skills to demonstrate what a 100% matched candidate profile would look like.

## Layout
```
ideal-resume-builder/
├── SKILL.md                  # the playbook the agent follows (read this first)
├── README.md                 # this file
├── scripts/
│   └── build_resume.py       # reusable one-page PDF builder (copied/adapted from resume-tailor)
└── output/                   # generated ideal PDFs land here
```

## How to run
1. Prompt: *"Use the ideal-resume-builder skill on this JD: <url or pasted text>."*
2. The agent will:
   - Fetch/parse the job description.
   - Design a fictional, high-impact profile.
   - Compile the PDF.
   - Verify layout and tenses.
   - Output the profile summary and path to the generated PDF.
