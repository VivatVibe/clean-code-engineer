"""Regression tests for the Agent Skill structural validator."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_skill import validate  # noqa: E402

REPO = Path(__file__).resolve().parents[1]


class SkillValidatorTests(unittest.TestCase):
    def test_real_skill_passes(self):
        self.assertEqual(validate(REPO), [])

    def test_detects_missing_required_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "clean-code-engineer"
            root.mkdir()
            (root / "SKILL.md").write_text(
                "---\nname: clean-code-engineer\ndescription: Tests this example.\n---\n# Skill\n",
                encoding="utf-8",
            )
            self.assertTrue(any("Missing required file" in err for err in validate(root)))

    def test_detects_broken_local_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "clean-code-engineer"
            root.mkdir()
            (root / "SKILL.md").write_text(
                "---\nname: clean-code-engineer\ndescription: Tests this example.\n---\n"
                "[Missing](references/no-such-file.md)\n",
                encoding="utf-8",
            )
            self.assertTrue(any("Broken local link" in err for err in validate(root)))

    def test_detects_invalid_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "clean-code-engineer"
            root.mkdir()
            (root / "SKILL.md").write_text(
                "---\nname: Clean_Code_Engineer\ndescription: Tests this example.\n---\n# Skill\n",
                encoding="utf-8",
            )
            self.assertTrue(any("Invalid skill name" in err for err in validate(root)))


if __name__ == "__main__":
    unittest.main()
