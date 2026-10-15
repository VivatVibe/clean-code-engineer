#!/usr/bin/env python3
"""Small zero-dependency structure validator for this original agent skill."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
skill = ROOT / "SKILL.md"
text = skill.read_text(encoding="utf-8")
assert text.startswith("---\n"), "Missing YAML frontmatter"
front = text.split("---", 2)[1]
assert re.search(r"(?m)^name: clean-code-engineer$", front), "Invalid skill name"
assert re.search(r"(?m)^description: .+", front), "Missing description"
for path in re.findall(r"\]\((references/[^)]+|assets/[^)]+)\)", text):
    assert (ROOT / path).is_file(), f"Missing linked file: {path}"
for path in ("README.md", "SOURCES.md", "LICENSE",
             "references/principles.md", "references/safe-refactoring.md",
             "references/review-checklist.md", "references/typescript-react.md",
             "assets/review-report-template.md", "examples/refactor-example.ts"):
    assert (ROOT / path).is_file(), f"Missing required file: {path}"
print("Skill manifest and local file references: OK")
