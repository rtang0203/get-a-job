#!/usr/bin/env python3
"""
Append an entry to the application tracker (output/applications.json).

Usage:
  python track_application.py \
    --company "Mage" \
    --role "Senior AI Infrastructure Engineer" \
    --verdict "stretch" \
    --action "Build project first, then apply" \
    --pdf "Randy_Tang_Resume_Mage.pdf" \
    [--url "https://..."] \
    [--notes "Key gaps: Modal, GCP, GPU inference"]

The tracker is a JSON array of objects, newest last.
"""
import argparse, json, os
from datetime import date

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
TRACKER_PATH = os.path.join(PROJECT_DIR, "output", "applications.json")


def load_tracker():
    if os.path.exists(TRACKER_PATH):
        with open(TRACKER_PATH) as f:
            return json.load(f)
    return []


def save_tracker(data):
    os.makedirs(os.path.dirname(TRACKER_PATH), exist_ok=True)
    with open(TRACKER_PATH, "w") as f:
        json.dump(data, f, indent=2)


def main():
    p = argparse.ArgumentParser(description="Track a resume tailoring run.")
    p.add_argument("--company", required=True)
    p.add_argument("--role", required=True)
    p.add_argument("--verdict", required=True,
                   choices=["strong fit", "plausible fit", "stretch", "likely ineligible"])
    p.add_argument("--action", required=True,
                   choices=["Apply now", "Apply with targeted cover letter",
                            "Build project first, then apply", "Skip"])
    p.add_argument("--pdf", required=True, help="PDF filename (not full path)")
    p.add_argument("--url", default="", help="JD URL")
    p.add_argument("--notes", default="", help="Free-form notes (key gaps, etc.)")
    args = p.parse_args()

    tracker = load_tracker()
    entry = {
        "date": date.today().isoformat(),
        "company": args.company,
        "role": args.role,
        "verdict": args.verdict,
        "action": args.action,
        "pdf": args.pdf,
        "url": args.url,
        "notes": args.notes,
        "status": "tailored",
    }
    tracker.append(entry)
    save_tracker(tracker)
    print(f"Tracked: {args.company} — {args.role} ({args.verdict})")
    print(f"  Total applications: {len(tracker)}")


if __name__ == "__main__":
    main()
