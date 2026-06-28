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
### fix: fix CONTENT mutation bug with deep_merge in ideal-resume-builder
- **What:** Added `import copy`; added `deep_merge(base, override)` function (recursive deep-merge, lists replaced wholesale); changed `__main__` block from `content = CONTENT; content.update(...)` to `content = copy.deepcopy(CONTENT); content = deep_merge(content, json.load(f))`. Created `ideal-resume-builder/tests/test_merge.py` with two tests covering immutability of base and recursive dict merging.
- **Why:** The original code assigned `content = CONTENT` (shallow reference) then called `.update()` which mutated the module-level `CONTENT` global in-place. On repeated import or invocations this would corrupt the defaults. `deep_merge` is the correct pattern used in resume-tailor.
- **Files:** ideal-resume-builder/scripts/build_resume.py, ideal-resume-builder/tests/test_merge.py
- **Gate:** py_compile PASS; `/tmp/ai-venv/irb/bin/python -m pytest ideal-resume-builder/tests/test_merge.py -v` → 2 passed
- **Commit:** f0cd43d

### refactor: move summary text to resume.json as source of truth
- **What:** Added top-level `"summary"` key to `resume-tailor/master/resume.json` containing the exact existing hardcoded string. Changed `load_master()` in `resume-tailor/scripts/build_resume.py` to use `m.get("summary", <fallback>)` so it reads from JSON with the old string as fallback.
- **Why:** The summary was hardcoded in Python rather than in the data file it belongs to. Moving it to JSON makes it editable without touching code and is consistent with all other resume fields.
- **Files:** resume-tailor/master/resume.json, resume-tailor/scripts/build_resume.py
- **Gate:** py_compile PASS; PDF built successfully with identical summary text
- **Commit:** 47bed79
