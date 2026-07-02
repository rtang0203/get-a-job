#!/usr/bin/env python3
"""
Reusable one-page resume PDF builder.

Usage:
  python build_resume.py                        # build from master/resume.json defaults
  python build_resume.py path/to/override.json  # deep-merge override on top of defaults

Supports two override formats:
  - Legacy (default): a CONTENT dict deep-merged over defaults from resume.json.
    Override must provide fully-rendered HTML strings for skills, experience, etc.
  - Format 2 ("format": 2): semantic overrides keyed by company name / project name.
    The build script renders HTML from structured data automatically.
    See README.md for the format-2 schema.

Deps: pip install reportlab --break-system-packages
"""
import sys, json, os, copy, re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
MASTER_JSON = os.path.join(PROJECT_DIR, "master", "resume.json")


# ---------------------------------------------------------------------------
# Markup helpers
# ---------------------------------------------------------------------------

def convert_markup(text):
    """Convert **bold** markers to <b> tags for ReportLab Paragraph rendering.

    Leaves existing HTML tags untouched. Handles &amp; for ampersands when they
    appear outside of existing HTML entities.
    """
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    return text


# ---------------------------------------------------------------------------
# Master loader (legacy format)
# ---------------------------------------------------------------------------

def load_master():
    """Load master/resume.json and convert to the CONTENT format the builder expects."""
    with open(MASTER_JSON) as f:
        m = json.load(f)

    contact = f"{m['contact']['email']}&nbsp;&nbsp;|&nbsp;&nbsp;{m['contact']['phone']}"

    skills = m["skills"]
    langs = ", ".join(skills["languages"])
    if skills.get("languages_hedged"):
        langs += ", " + ", ".join(skills["languages_hedged"])
    data_sys = ", ".join(skills["data_systems"])
    ai = ", ".join(skills["ai_agentic"])
    practices = ", ".join(skills["practices"])
    skills_html = (
        f"<b>Languages:</b> {langs}&nbsp;&nbsp;|&nbsp;&nbsp;"
        f"<b>Data/Systems:</b> {data_sys}<br/>"
        f"<b>AI / Agentic:</b> {ai}<br/>"
        f"<b>Practices:</b> {practices}"
    )

    summary = m.get("summary", (
        "Software engineer with 3+ years building and optimizing high-throughput, "
        "production-critical data systems at a global bank. Strong CS/algorithms "
        "foundation (Cornell BS), deep Python proficiency, and hands-on fluency with "
        "agentic coding workflows and LLM APIs."
    ))

    experience = []
    for exp in m["experience"]:
        stack_str = ", ".join(exp.get("stack", []))
        bullets = [f.rstrip(".") + "." for f in exp["facts"]]
        entry = {
            "role": f"{exp['title']} &mdash; {exp['company']}",
            "dates": exp["dates"].replace(" - ", " &ndash; "),
            "sub": f"{exp.get('team', '')} &nbsp;|&nbsp; {stack_str}" if exp.get("team") else stack_str,
            "bullets": bullets,
        }
        experience.append(entry)

    projects = []
    for proj in m["projects"]:
        stack_str = ", ".join(proj["stack"])
        projects.append(f"<b>{proj['name']}</b> ({stack_str}) \u2014 {proj['desc']}")

    edu = m["education"][0]
    degrees = " &nbsp;&amp;&nbsp; ".join(edu["degrees"])
    edu_entry = {
        "role": f"{edu['school']} &mdash; {edu['location']}",
        "dates": edu["dates"].replace(" - ", " &ndash; "),
        "sub": f"{degrees} &nbsp;|&nbsp; GPA {edu['gpa']}",
        "bullets": [a for a in edu.get("activities", [])],
    }

    return {
        "name": m["name"],
        "contact": contact,
        "company_slug": "Generic",
        "summary": summary,
        "skills_html": skills_html,
        "experience": experience,
        "projects": projects,
        "education": edu_entry,
    }


# ---------------------------------------------------------------------------
# Format-2 semantic override
# ---------------------------------------------------------------------------

def apply_semantic_override(override):
    """Build CONTENT dict from master/resume.json + a format-2 semantic override.

    Format-2 overrides reference master data by name (company, project) and only
    provide the fields that differ.  The build script pulls titles, dates, stacks,
    and descriptions from resume.json and renders HTML automatically.

    Schema (all fields optional except company_slug):
      {
        "format": 2,
        "company_slug": "AcmeCorp",
        "summary": "plain text with **bold** markers",
        "contact_extras": ["U.S. Citizen"],
        "skills": [
          {"label": "Languages", "items": ["Python", "SQL"], "join_next": true},
          {"label": "Infra", "items": ["Docker", "Postgres"]}
        ],
        "experience": {
          "Bank of America": ["bullet one with **bold**", "bullet two"]
        },
        "projects": {
          "include": ["Project A", "Project B"],
          "overrides": {
            "Project A": {"desc": "custom description", "stack": ["Python"]}
          }
        },
        "education": {
          "bullets": ["custom activity line"]
        }
      }
    """
    with open(MASTER_JSON) as f:
        m = json.load(f)

    # -- Contact --
    contact = f"{m['contact']['email']}&nbsp;&nbsp;|&nbsp;&nbsp;{m['contact']['phone']}"
    for extra in override.get("contact_extras", []):
        contact += f"&nbsp;&nbsp;|&nbsp;&nbsp;{extra}"

    # -- Summary --
    summary = convert_markup(override.get("summary", m.get("summary", "")))

    # -- Skills --
    if "skills" in override:
        parts = []
        cats = override["skills"]
        i = 0
        while i < len(cats):
            cat = cats[i]
            items_str = ", ".join(cat["items"])
            segment = f"<b>{cat['label']}:</b> {items_str}"

            # join_next: put the next category on the same line with |
            if cat.get("join_next") and i + 1 < len(cats):
                next_cat = cats[i + 1]
                next_items = ", ".join(next_cat["items"])
                segment += f"&nbsp;&nbsp;|&nbsp;&nbsp;<b>{next_cat['label']}:</b> {next_items}"
                i += 2
            else:
                i += 1

            parts.append(segment)

        skills_html = "<br/>".join(parts)
    else:
        # Fall back to master skills
        skills = m["skills"]
        langs = ", ".join(skills["languages"])
        if skills.get("languages_hedged"):
            langs += ", " + ", ".join(skills["languages_hedged"])
        data_sys = ", ".join(skills["data_systems"])
        ai = ", ".join(skills["ai_agentic"])
        practices = ", ".join(skills["practices"])
        skills_html = (
            f"<b>Languages:</b> {langs}&nbsp;&nbsp;|&nbsp;&nbsp;"
            f"<b>Data/Systems:</b> {data_sys}<br/>"
            f"<b>AI / Agentic:</b> {ai}<br/>"
            f"<b>Practices:</b> {practices}"
        )

    # -- Experience --
    exp_overrides = override.get("experience", {})
    experience = []
    for exp in m["experience"]:
        company = exp["company"]
        stack_str = ", ".join(exp.get("stack", []))

        if company in exp_overrides:
            ov = exp_overrides[company]
            # Simple form: list of bullet strings
            if isinstance(ov, list):
                bullets = [convert_markup(b) for b in ov]
            # Dict form: {bullets: [...], stack: [...]}
            elif isinstance(ov, dict):
                bullets = [convert_markup(b) for b in ov.get("bullets", exp["facts"])]
                if "stack" in ov:
                    stack_str = ", ".join(ov["stack"])
            else:
                bullets = [f.rstrip(".") + "." for f in exp["facts"]]
        else:
            bullets = [f.rstrip(".") + "." for f in exp["facts"]]

        entry = {
            "role": f"{exp['title']} &mdash; {exp['company']}",
            "dates": exp["dates"].replace(" - ", " &ndash; "),
            "sub": (f"{exp.get('team', '')} &nbsp;|&nbsp; {stack_str}"
                    if exp.get("team") else stack_str),
            "bullets": bullets,
        }
        experience.append(entry)

    # -- Projects --
    proj_config = override.get("projects", {})
    include_list = proj_config.get("include")
    proj_overrides = proj_config.get("overrides", {})

    master_projects = {p["name"]: p for p in m["projects"]}

    if include_list is None:
        include_list = [p["name"] for p in m["projects"]]

    projects = []
    for name in include_list:
        proj = master_projects.get(name)
        if not proj:
            print(f"WARNING: Project '{name}' not found in resume.json, skipping.")
            continue
        ov = proj_overrides.get(name, {})
        stack = ov.get("stack", proj["stack"])
        desc = convert_markup(ov.get("desc", proj["desc"]))
        stack_str = ", ".join(stack)
        projects.append(f"<b>{name}</b> ({stack_str}) \u2014 {desc}")

    # -- Education --
    edu = m["education"][0]
    edu_ov = override.get("education", {})
    degrees = " &nbsp;&amp;&nbsp; ".join(edu["degrees"])
    raw_bullets = edu_ov.get("bullets", edu.get("activities", []))
    edu_bullets = [convert_markup(b) for b in raw_bullets]
    edu_entry = {
        "role": f"{edu['school']} &mdash; {edu['location']}",
        "dates": edu["dates"].replace(" - ", " &ndash; "),
        "sub": f"{degrees} &nbsp;|&nbsp; GPA {edu['gpa']}",
        "bullets": edu_bullets,
    }

    return {
        "name": m["name"],
        "contact": contact,
        "company_slug": override.get("company_slug", "Tailored"),
        "summary": summary,
        "skills_html": skills_html,
        "experience": experience,
        "projects": projects,
        "education": edu_entry,
    }


# ---------------------------------------------------------------------------
# Legacy deep merge
# ---------------------------------------------------------------------------

def deep_merge(base, override):
    """Deep-merge override into base. Lists are replaced wholesale, not appended."""
    result = copy.deepcopy(base)
    for key, val in override.items():
        if isinstance(val, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], val)
        else:
            result[key] = copy.deepcopy(val)
    return result


# ---------------------------------------------------------------------------
# PDF builder
# ---------------------------------------------------------------------------

DARK = colors.HexColor("#1a1a1a")
ACCENT = colors.HexColor("#2c3e50")
GREY = colors.HexColor("#444444")


def build(content, out_path):
    page_count = [0]

    def on_page(canvas, doc):
        page_count[0] = doc.page

    doc = SimpleDocTemplate(out_path, pagesize=letter, topMargin=0.5*inch,
                            bottomMargin=0.45*inch, leftMargin=0.6*inch, rightMargin=0.6*inch)
    s = getSampleStyleSheet()
    name_style = ParagraphStyle("name", parent=s["Normal"], fontName="Helvetica-Bold",
                                fontSize=20, textColor=DARK, alignment=TA_CENTER, leading=23, spaceAfter=2)
    contact_style = ParagraphStyle("contact", parent=s["Normal"], fontName="Helvetica",
                                   fontSize=9, textColor=GREY, alignment=TA_CENTER)
    section_style = ParagraphStyle("section", parent=s["Normal"], fontName="Helvetica-Bold",
                                   fontSize=11, textColor=ACCENT, spaceBefore=9, spaceAfter=2, leading=13)
    role_style = ParagraphStyle("role", parent=s["Normal"], fontName="Helvetica-Bold",
                                fontSize=10, textColor=DARK, spaceBefore=4, leading=12)
    sub_style = ParagraphStyle("sub", parent=s["Normal"], fontName="Helvetica-Oblique",
                               fontSize=9, textColor=GREY, spaceAfter=2, leading=11)
    bullet_style = ParagraphStyle("bullet", parent=s["Normal"], fontName="Helvetica",
                                  fontSize=9, textColor=GREY, leading=11.5, leftIndent=10, spaceAfter=1.5)
    body_style = ParagraphStyle("body", parent=s["Normal"], fontName="Helvetica",
                                fontSize=9, textColor=GREY, leading=11.5, spaceAfter=2)
    summary_style = ParagraphStyle("summary", parent=s["Normal"], fontName="Helvetica",
                                   fontSize=9, textColor=GREY, leading=12, alignment=TA_LEFT)
    rdate_style = ParagraphStyle("rdate", parent=role_style, alignment=2,
                                 fontName="Helvetica", textColor=GREY, fontSize=9)
    story = []

    def hr():
        story.append(HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceAfter=3))

    def role_line(left, right):
        t = Table([[Paragraph(left, role_style), Paragraph(right, rdate_style)]],
                  colWidths=[5.1*inch, 2.2*inch])
        t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "BOTTOM")] +
                              [(p, (0, 0), (-1, -1), 0) for p in
                               ("LEFTPADDING", "RIGHTPADDING", "TOPPADDING", "BOTTOMPADDING")]))
        story.append(t)

    def block(item):
        role_line(item["role"], item["dates"])
        if item.get("sub"):
            story.append(Paragraph(item["sub"], sub_style))
        for b in item["bullets"]:
            story.append(Paragraph(b, bullet_style, bulletText="\u2022"))

    story.append(Paragraph(content["name"], name_style))
    story.append(Paragraph(content["contact"], contact_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("SUMMARY", section_style)); hr()
    story.append(Paragraph(content["summary"], summary_style))

    story.append(Paragraph("TECHNICAL SKILLS", section_style)); hr()
    story.append(Paragraph(content["skills_html"], body_style))

    story.append(Paragraph("EXPERIENCE", section_style)); hr()
    for item in content["experience"]:
        block(item)

    story.append(Paragraph("PROJECTS", section_style)); hr()
    for p in content["projects"]:
        story.append(Paragraph(p, bullet_style, bulletText="\u2022"))

    story.append(Paragraph("EDUCATION", section_style)); hr()
    block(content["education"])

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    # -- Page-count check --
    if page_count[0] > 1:
        print(f"WARNING: Resume is {page_count[0]} pages (target is 1). Trim content.")
    elif page_count[0] == 1:
        print("OK: 1 page.")

    return out_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    content = load_master()
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            override = json.load(f)

        if override.get("format") == 2:
            # Semantic override: build content from master + override
            content = apply_semantic_override(override)
        else:
            # Legacy: deep-merge rendered override onto defaults
            content = deep_merge(content, override)

    out_dir = os.path.join(PROJECT_DIR, "output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"Randy_Tang_Resume_{content.get('company_slug','Tailored')}.pdf")
    build(content, out)
    print("Wrote", out)
