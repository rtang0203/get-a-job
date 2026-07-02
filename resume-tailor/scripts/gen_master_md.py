#!/usr/bin/env python3
"""
Auto-generate resume_master.md from resume.json.

Eliminates manual sync between the two files. Run after editing resume.json:
  python3 scripts/gen_master_md.py
"""
import json, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
MASTER_JSON = os.path.join(PROJECT_DIR, "master", "resume.json")
MASTER_MD = os.path.join(PROJECT_DIR, "master", "resume_master.md")


def generate():
    with open(MASTER_JSON) as f:
        m = json.load(f)

    lines = []
    lines.append(f"# {m['name']} — Master Resume\n")
    lines.append("> Auto-generated from `resume.json`. Edit the JSON, then run")
    lines.append("> `python3 scripts/gen_master_md.py` to regenerate this file.\n")

    contact = m["contact"]
    lines.append(f"**{contact['email']} · {contact['phone']}**\n")

    # Education
    lines.append("## Education")
    for edu in m["education"]:
        degrees = " & ".join(edu["degrees"])
        lines.append(f"**{edu['school']}** — {edu['location']} · {edu['dates']}")
        lines.append(f"{degrees} · GPA {edu['gpa']}")
        for act in edu.get("activities", []):
            lines.append(f"- {act}")
    lines.append("")

    # Experience
    lines.append("## Experience")
    for exp in m["experience"]:
        stack_str = ", ".join(exp.get("stack", []))
        lines.append(f"**{exp['title']} — {exp['company']}** · {exp['dates']}")
        sub_parts = []
        if exp.get("team"):
            sub_parts.append(exp["team"])
        if stack_str:
            sub_parts.append(stack_str)
        if sub_parts:
            sep = " · "
            lines.append(f"*{sep.join(sub_parts)}*")
        for fact in exp["facts"]:
            bullet = fact.rstrip(".") + "."
            lines.append(f"- {bullet}")
        lines.append("")

    # Projects
    lines.append("## Projects")
    for proj in m["projects"]:
        stack_str = ", ".join(proj["stack"])
        lines.append(f"- **{proj['name']}** ({stack_str}) — {proj['desc']}")
    lines.append("")

    # Skills
    lines.append("## Skills")
    skills = m["skills"]
    all_items = []
    all_items.extend(skills.get("languages", []))
    all_items.extend(skills.get("languages_hedged", []))
    for key in ["data_systems", "ai_agentic", "practices"]:
        all_items.extend(skills.get(key, []))
    lines.append(", ".join(all_items))
    lines.append("")

    content = "\n".join(lines)
    with open(MASTER_MD, "w") as f:
        f.write(content)

    print(f"Generated {MASTER_MD}")
    return MASTER_MD


if __name__ == "__main__":
    generate()
