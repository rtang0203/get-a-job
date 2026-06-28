# Auto-Improve Worklog — 2026-06-28

### chore: add requirements.txt and .gitignore for resume-tailor
- **What:** Created `resume-tailor/requirements.txt` (reportlab) and `resume-tailor/.gitignore` (venv/, __pycache__/, *.pyc)
- **Why:** Project had no dependency manifest or gitignore; follows global convention of using requirements.txt
- **Files:** resume-tailor/requirements.txt, resume-tailor/.gitignore
- **Gate:** py_compile baseline PASS, post-change PASS
- **Commit:** d3e2f6cae90a1808fca7e11289ff88eb1e2cd32f

### chore: add requirements.txt for ideal-resume-builder
- **What:** Created `ideal-resume-builder/requirements.txt` (reportlab)
- **Why:** Project had no dependency manifest; follows global convention
- **Files:** ideal-resume-builder/requirements.txt
- **Gate:** py_compile baseline PASS, post-change PASS
- **Commit:** c99cc1d5cec0dc43fc06c6cfda5a14d8dafa786d
