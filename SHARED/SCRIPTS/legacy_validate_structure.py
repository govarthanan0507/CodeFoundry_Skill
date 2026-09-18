#!/usr/bin/env python3
"""
validate_structure.py

Level 0 (deterministic, no AI) — checks every project folder under
<root>/projects/ against PROJECT_FOLDER_STRUCTURE.md's convention:
  - documents/, handoffs/, state/ subfolders exist
  - document filenames follow the -vN versioning pattern

Usage: python validate_structure.py <codefoundry-root-path>
"""

import sys
import re
from pathlib import Path

REQUIRED_SUBFOLDERS = ["documents", "handoffs", "state"]
VERSION_PATTERN = re.compile(r"-v\d+\.(md|docx)$", re.IGNORECASE)


def validate_project(project_dir: Path) -> list[str]:
    issues = []
    for sub in REQUIRED_SUBFOLDERS:
        if not (project_dir / sub).is_dir():
            issues.append(f"missing required subfolder: {sub}/")

    documents_dir = project_dir / "documents"
    if documents_dir.is_dir():
        for f in documents_dir.iterdir():
            if f.is_file() and f.suffix in (".md", ".docx"):
                if not VERSION_PATTERN.search(f.name):
                    issues.append(
                        f"documents/{f.name} does not follow the -vN "
                        f"versioning convention"
                    )
    return issues


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_structure.py <codefoundry-root-path>")
        sys.exit(1)

    root = Path(sys.argv[1])
    projects_dir = root / "projects"

    if not projects_dir.is_dir():
        print(f"No 'projects' folder found under {root}")
        sys.exit(1)

    total_issues = 0
    for project_dir in sorted(p for p in projects_dir.iterdir() if p.is_dir()):
        issues = validate_project(project_dir)
        status = "OK" if not issues else f"{len(issues)} issue(s)"
        print(f"\n{project_dir.name}: {status}")
        for issue in issues:
            print(f"  - {issue}")
        total_issues += len(issues)

    print(f"\n{'='*40}")
    print(f"Total issues across all projects: {total_issues}")
    sys.exit(0 if total_issues == 0 else 1)


if __name__ == "__main__":
    main()
