#!/usr/bin/env python3
"""Validate a self-contained Agent Skills repository without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = (
    "README.md",
    "SKILL.md",
    "SOURCES.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "references/principles.md",
    "references/safe-refactoring.md",
    "references/review-checklist.md",
    "references/typescript-react.md",
    "assets/review-report-template.md",
    "examples/refactor-example.ts",
    ".github/workflows/validate.yml",
)

FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LOCAL_LINK = re.compile(r"\[[^\]]+\]\(([^\s)]+)(?:\s+[^)]*)?\)")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for relpath in REQUIRED:
        if not (root / relpath).is_file():
            errors.append(f"Missing required file: {relpath}")

    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return errors

    skill = skill_path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(skill)
    if not match:
        errors.append("SKILL.md requires YAML frontmatter delimited by ---")
    else:
        fields = {}
        for line in match.group(1).splitlines():
            if ":" in line and not line.startswith((" ", "\t")):
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip().strip("'\"")

        name = fields.get("name", "")
        if (
            not name
            or len(name) > 64
            or NAME.fullmatch(name) is None
            or name != root.name
        ):
            errors.append("Invalid skill name (format or directory mismatch)")

        description = fields.get("description", "")
        if not description or len(description) > 1024:
            errors.append("Missing or invalid skill description (1–1024 characters)")

    if len(skill.splitlines()) > 500:
        errors.append("SKILL.md is too long; move details into references/")

    # Validate every local Markdown file link in the public documentation.
    for source in ("SKILL.md", "README.md", "CONTRIBUTING.md", "SOURCES.md"):
        path = root / source
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for target in LOCAL_LINK.findall(text):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            relative = target.split("#", 1)[0].split("?", 1)[0]
            if not relative:
                continue
            dest = (path.parent / relative).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f"Broken local link in {source}: {target}")

    return errors


if __name__ == "__main__":
    problems = validate(Path(__file__).resolve().parents[1])
    if problems:
        for problem in problems:
            print("ERROR:", problem, file=sys.stderr)
        sys.exit(1)
    print("Agent Skill manifest and local links: OK")
