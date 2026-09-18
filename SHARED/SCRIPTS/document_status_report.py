#!/usr/bin/env python3
"""
document_status_report.py

Level 0 (deterministic, no AI) — scans every project's documents/
folder and reports DRAFT vs SIGNED OFF status per
DOCUMENT_GOVERNANCE.md's header format. Pure text parsing.

Usage: python document_status_report.py <codefoundry-root-path>
"""

import sys
import re
from pathlib import Path

STATUS_PATTERN = re.compile(r"STATUS:\s*(\w[\w ]*)")
SIGNED_BY_PATTERN = re.compile(r"SIGNED OFF BY:\s*(.*)")


def read_status(file_path: Path) -> tuple[str, str]:
    try:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ("UNREADABLE", "")

    status_match = STATUS_PATTERN.search(text)
    status = status_match.group(1).strip() if status_match else "NO STATUS FOUND"

    signed_match = SIGNED_BY_PATTERN.search(text)
    signed_by = ""
    if signed_match:
        candidate = signed_match.group(1).strip()
        if candidate and "<" not in candidate and "(pending)" not in candidate:
            signed_by = candidate

    return (status, signed_by)


def main():
    if len(sys.argv) != 2:
        print("Usage: python document_status_report.py <codefoundry-root-path>")
        sys.exit(1)

    root = Path(sys.argv[1])
    projects_dir = root / "projects"

    if not projects_dir.is_dir():
        print(f"No 'projects' folder found under {root}")
        sys.exit(1)

    print(f"{'PROJECT':<20}{'DOCUMENT':<30}{'STATUS':<20}{'SIGNED OFF BY'}")
    print("-" * 90)

    counts = {"SIGNED OFF": 0, "DRAFT": 0, "OTHER": 0}

    for project_dir in sorted(p for p in projects_dir.iterdir() if p.is_dir()):
        documents_dir = project_dir / "documents"
        if not documents_dir.is_dir():
            continue
        for f in sorted(documents_dir.iterdir()):
            if not f.is_file():
                continue
            if f.suffix == ".md":
                status, signed_by = read_status(f)
            elif f.suffix == ".docx":
                status, signed_by = ("(docx — open externally to check)", "")
            else:
                continue

            key = status if status in ("SIGNED OFF", "DRAFT") else "OTHER"
            counts[key] = counts.get(key, 0) + 1

            print(f"{project_dir.name:<20}{f.name:<30}{status:<20}{signed_by}")

    print("-" * 90)
    print(f"Signed off: {counts.get('SIGNED OFF', 0)}  |  "
          f"Draft: {counts.get('DRAFT', 0)}  |  "
          f"Other/unknown: {counts.get('OTHER', 0)}")


if __name__ == "__main__":
    main()
