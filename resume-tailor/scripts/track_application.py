#!/usr/bin/env python3
"""
Append or update an entry in the application tracker (output/applications.json).

If a matching company+role already exists, the entry is updated in place
(with the date refreshed) instead of duplicated.

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

    # Dedup: update in place if company+role already exists
    existing_idx = None
    for i, e in enumerate(tracker):
        if e["company"] == args.company and e["role"] == args.role:
            existing_idx = i
            break

    if existing_idx is not None:
        tracker[existing_idx] = entry
        print(f"Updated: {args.company} — {args.role} ({args.verdict})")
    else:
        tracker.append(entry)
        print(f"Tracked: {args.company} — {args.role} ({args.verdict})")

    print(f"  Total applications: {len(tracker)}")
    save_tracker(tracker)


if __name__ == "__main__":
    main()
