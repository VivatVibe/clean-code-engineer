# Clean Code Engineer — AI Agent Skill

**Reusable code-review, safe-refactoring, and testing workflows for Codex, Google Antigravity, and other Agent Skills–compatible coding agents.**

[ภาษาไทย](#ภาษาไทย) · [English](#english) · [Skill instructions](SKILL.md)

This repository contains **original, practical engineering instructions** informed by the general ideas discussed in *Clean Code: A Handbook of Agile Software Craftsmanship* by Robert C. Martin (2008/2009). It does **not** contain the book, long excerpts, or copied code examples. It is **not** endorsed by the author or publisher.

## What's inside?

```text
clean-code-engineer/
├── SKILL.md                         # Agent Skills entry point
├── references/
│   ├── principles.md                # Practical principles and trade-offs
│   ├── safe-refactoring.md          # Behavior-preserving workflow
│   ├── review-checklist.md          # Severity and review heuristics
│   └── typescript-react.md          # TypeScript, React, API/Worker guidance
├── assets/
│   └── review-report-template.md    # Consistent findings/report format
├── examples/
│   └── refactor-example.ts          # Original self-contained example
├── scripts/
│   └── validate_skill.py            # Zero-dependency manifest sanity checks
├── SOURCES.md
└── LICENSE
```

This is a **decision-support skill, not an automatic formatter or proof of correctness**. The agent must inspect real code and tests. Recommendations are context-sensitive, not rigid numerical rules.

## ภาษาไทย

### ใช้ทำอะไร?

ให้ AI ช่วยตรวจคุณภาพโค้ด, หา Code Smells, Refactor อย่างปลอดภัย, เพิ่ม Tests, ลดความซับซ้อน และสรุปความเสี่ยงก่อนส่ง Pull Request

- **Review:** ตรวจโค้ดหรือ PR พร้อมหลักฐาน พาธ/บรรทัด และระดับความรุนแรง
- **Refactor:** ปรับโครงสร้างทีละขั้นโดยพยายามรักษาพฤติกรรมเดิม
- **Implement:** เขียนฟีเจอร์ใหม่โดยให้ความสำคัญกับชื่อที่สื่อความหมาย ขอบเขตโมดูล และการทดสอบ
- **Test:** ครอบคลุม happy path, boundary cases, error paths, side effects
- **Ship:** ตรวจ commands จริงของโปรเจกต์, lint/typecheck/tests/build และรายงานผลที่รันจริง

### ติดตั้งในโปรเจกต์บน macOS (Codex + Antigravity)

เปิด Terminal ในโฟลเดอร์โปรเจกต์ที่ต้องการใช้ Skill:

```bash
tmpdir="$(mktemp -d)"
git clone --depth 1 https://github.com/VivatVibe/clean-code-engineer.git "$tmpdir/clean-code-engineer"
mkdir -p .agents/skills/clean-code-engineer
cp "$tmpdir/clean-code-engineer/SKILL.md" .agents/skills/clean-code-engineer/
cp -R "$tmpdir/clean-code-engineer/references" .agents/skills/clean-code-engineer/
cp -R "$tmpdir/clean-code-engineer/assets" .agents/skills/clean-code-engineer/
rm -rf "$tmpdir"
```

ตำแหน่ง `.agents/skills/clean-code-engineer/SKILL.md` เป็นโครงสร้างที่ทั้งสองเครื่องมือรองรับในระดับ Workspace/Repository. **อย่าคัดลอกทั้งโฟลเดอร์ `.git` เข้าโปรเจกต์หลัก**.

สำหรับ Antigravity บน Mac ที่ต้องการใช้ทุกโปรเจกต์:

```bash
mkdir -p ~/.gemini/config/skills
git clone --depth 1 https://github.com/VivatVibe/clean-code-engineer.git ~/.gemini/config/skills/clean-code-engineer
```

ถ้ามีโฟลเดอร์นี้แล้ว ให้ `git -C ~/.gemini/config/skills/clean-code-engineer pull --ff-only` เพื่ออัปเดตแทนการ clone ซ้ำ

### ตัวอย่างคำสั่งสั่ง AI

**Codex:** `$clean-code-engineer Review this PR for correctness, code smells, and missing tests. Report findings first; don't edit files.`

**Antigravity:** `/clean-code-engineer ตรวจโค้ดในโปรเจกต์นี้ หา P0–P3 issues และเสนอแผน Refactor โดยยังไม่แก้โค้ด`

**Refactoring:** `Use clean-code-engineer to refactor this module in small, behavior-preserving steps. Run the existing tests and show the evidence.`

## English

### Install in a repository

Copy `SKILL.md`, `references/`, and `assets/` from this repository into `.agents/skills/clean-code-engineer/`. See the macOS shell example above.

### Suggested prompts

- **Audit:** "Use clean-code-engineer to review the changed files. Findings first, with file/line evidence and test gaps. Do not modify code."
- **Refactor:** "Use clean-code-engineer. Preserve observable behavior; establish baseline tests, change in small steps, and run relevant checks."
- **Implementation:** "Use clean-code-engineer to build this feature with readable names, clear boundaries, and focused tests. Follow repository conventions."

### Validation

```bash
python3 scripts/validate_skill.py
```

This sanity-checks the manifest and local references; it does **not** test AI behavior or prove code quality.

## Principles and safety

- **Correctness, security, and user requirements outrank cosmetic cleanliness.**
- Use evidence and make small, reversible changes. Never claim tests passed if they were not run.
- No broad rewrites, dependency changes, schema migrations, destructive commands, or public API changes without explicit approval.
- Protect credentials and private data; redact sensitive values in findings.
- Prefer existing project conventions when a general guideline conflicts.
- The source book includes Java-era examples and some opinionated practices. This skill adapts the underlying ideas to modern TypeScript/React and other codebases rather than enforcing every book preference literally.

## Sources, license, and attribution

See [SOURCES.md](SOURCES.md) for attribution, scope, and reading notes. The **original skill content** is available under the [MIT License](LICENSE). The license **does not apply to the referenced book**.

Agent Skills specification: https://agentskills.io/specification

Google Antigravity skills documentation: https://www.antigravity.google/docs/skills

---

*Maintained by VivatVibe. Contributions are welcome; do not submit copyrighted book text or unlicensed book PDFs.*
