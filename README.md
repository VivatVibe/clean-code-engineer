# Clean Code Engineer

[![Validate Agent Skill](https://github.com/VivatVibe/clean-code-engineer/actions/workflows/validate.yml/badge.svg)](https://github.com/VivatVibe/clean-code-engineer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/standard-Agent%20Skills-6B46C1)](https://agentskills.io/specification)

**A free, open-source AI coding skill that anyone can install.** It helps coding agents review, refactor, implement, and test maintainable code. Designed to be usable with OpenAI Codex, Google Antigravity, Claude Code, Cursor, and other tools that support the [Agent Skills standard](https://agentskills.io/specification).

**ฟรีและเปิดให้ทุกคนใช้** — Skill ช่วยให้ AI ตรวจโค้ด, ทำ Refactor อย่างระมัดระวัง, เขียน Tests และรายงานคุณภาพโค้ดโดยยึดหลักฐานจริง

> This is an independent, original educational tool inspired by general topics from Robert C. Martin's *Clean Code*. It is not a copy of, or an official companion to, that copyrighted book. See [SOURCES.md](SOURCES.md).

## Install — one command / ติดตั้งด้วยคำสั่งเดียว

**Prerequisite:** Node.js with `npx` and access to GitHub. Open a terminal in your project directory and run:

```bash
npx skills add VivatVibe/clean-code-engineer
```

Select the agent(s) and project-level installation in the interactive installer. This is the recommended way to share the skill in a team project.

**Install for your user account / ติดตั้งสำหรับผู้ใช้ทุกโปรเจกต์:**

```bash
npx skills add VivatVibe/clean-code-engineer --global
```

**Check what the repository provides (without installing):**

```bash
npx skills add VivatVibe/clean-code-engineer --list
```

**Install noninteractively for a chosen supported agent (example: Codex):**

```bash
npx skills add VivatVibe/clean-code-engineer --skill clean-code-engineer --agent codex --yes
```

The installer supports multiple coding agents and can install via copies or symlinks, depending on options and platform. If your agent does not discover a global installation, use the manual project installation below. Refer to the [upstream CLI documentation](https://github.com/vercel-labs/skills#readme) for current supported agents and flags. **This is an Agent Skill, not an npm package: `npx` runs the installer, not the skill itself.**

### ภาษาไทย: ขั้นตอนสำหรับผู้เริ่มต้น

1. ติดตั้ง [Node.js](https://nodejs.org/) (มี `npx` มาด้วย) และเปิด Terminal หรือ PowerShell
2. ไปยังโฟลเดอร์โปรเจกต์ของคุณ
3. วางคำสั่ง `npx skills add VivatVibe/clean-code-engineer`
4. เลือก AI Agent ที่ใช้อยู่และยืนยันการติดตั้ง
5. เปิดแชทของ AI แล้วขอให้ใช้ `clean-code-engineer` รีวิวหรือ Refactor โค้ด

คุณไม่ต้องเป็นเจ้าของ Repository นี้ ไม่ต้อง Fork ไม่ต้องขอสิทธิ์ และไม่ต้องจ่ายค่าซื้อ Skill แต่การใช้งาน AI Agent ของคุณอาจมีค่าใช้จ่ายตามผู้ให้บริการ

### Google Antigravity: global installation caveat

Antigravity IDE/app officially looks for global skills at `~/.gemini/config/skills/<skill-name>/`. Antigravity CLI may instead use `~/.gemini/antigravity-cli/skills/<skill-name>/`. Some versions of general-purpose installers put global skills in `~/.agents/skills/`, which may not be discovered by every Antigravity surface.

If the global installation is not recognized, use the **manual global installation** below or install at the project level. See the [Antigravity skills docs](https://www.antigravity.google/docs/skills).

## Manual install (no Node.js required)

For coding agents that support workspace-level Agent Skills:

1. Download the repository ZIP using GitHub's **Code → Download ZIP** (or run `git clone https://github.com/VivatVibe/clean-code-engineer.git`).
2. In your target project, create `.agents/skills/clean-code-engineer/`.
3. Copy **`SKILL.md`, `references/`, and `assets/`** into that directory, maintaining their relative paths.
4. Restart/reload the agent if necessary. Ask it to use `clean-code-engineer`.

For global Antigravity IDE/app, put the same three items under `~/.gemini/config/skills/clean-code-engineer/`. For Antigravity CLI global scope, use `~/.gemini/antigravity-cli/skills/clean-code-engineer/`.

Some other agents use different directories. Follow your agent's own documentation when it does not support `.agents/skills/`.

**Resulting structure:**

```text
your-project/
└── .agents/
    └── skills/
        └── clean-code-engineer/
            ├── SKILL.md
            ├── references/
            │   ├── principles.md
            │   ├── safe-refactoring.md
            │   ├── review-checklist.md
            │   └── typescript-react.md
            └── assets/
                └── review-report-template.md
```

## Use it / ตัวอย่างคำสั่งให้ AI

The agent can select the skill automatically for matching tasks; you can also name it explicitly:

| Task | Example prompt |
| --- | --- |
| Code review | `Use clean-code-engineer to review this PR. Findings first, with file:line evidence. Do not edit code.` |
| Safe refactor | `Use clean-code-engineer to refactor this module in small steps without changing observable behavior. Run existing tests.` |
| Test coverage | `Use clean-code-engineer to identify boundary cases and missing regression tests for this feature.` |
| New feature | `Use clean-code-engineer when implementing this feature. Follow existing conventions and report executed checks.` |

**ตัวอย่างภาษาไทย:** `ใช้ clean-code-engineer ตรวจโค้ดส่วนที่เปลี่ยน หา Bugs และ Code Smells จัดระดับ P0–P3 พร้อมอ้างอิงไฟล์และบรรทัด อย่าเพิ่งแก้โค้ด`

For Antigravity app/IDE, you can also try `/clean-code-engineer` in the agent chat; invocation UX differs by agent and version.

## Update / ถอนการติดตั้ง

```bash
# Update installed skills (interactive, project or global)
npx skills update clean-code-engineer

# Remove from the current project
npx skills remove clean-code-engineer
```

If installed manually, replace or delete the skill's folder in the appropriate agent directory. Do not delete unrelated skill folders. Existing agents may need a reload to detect changes.

## Skill features

- **Review:** evidence-first correctness, security, and maintainability findings, prioritized P0–P3
- **Refactor:** small behavior-preserving steps, characterization tests, rollback awareness
- **Implement:** clear naming, domain boundaries, explicit error paths, appropriate abstractions
- **Test:** edge cases, error cases, integration boundaries, realistic verification
- **Ship:** report which checks really ran (and which did not)

The skill is opinionated but not dogmatic. Correctness, security, public compatibility, and project conventions outrank cosmetic style preferences.

## Repository layout

```text
.
├── SKILL.md                          # Standard entry point
├── references/
│   ├── principles.md
│   ├── safe-refactoring.md
│   ├── review-checklist.md
│   └── typescript-react.md
├── assets/review-report-template.md
├── examples/refactor-example.ts
├── scripts/validate_skill.py
├── .github/workflows/validate.yml
├── CONTRIBUTING.md
├── SOURCES.md
└── LICENSE
```

## Trust, tests and limitations

This skill is a collection of **instructions**, not a running service. Installing it does not grant the maintainer access to your repository, computer, or AI conversations. The AI agent's existing permissions still apply; review proposed changes, shell commands, and dependencies before running them. The skill does not automatically make generated code correct or secure.

```bash
python3 scripts/validate_skill.py
```

GitHub Actions runs structural validation on every push and pull request. This **does not prove that every AI agent supports the skill or that code reviews will always be correct**.

## Community and license

Everyone may use, fork, adapt, and contribute original improvements under the [MIT License](LICENSE). The license does not grant rights to the book *Clean Code*.

- [Contributing guidelines](CONTRIBUTING.md)
- [Report bugs or request features](https://github.com/VivatVibe/clean-code-engineer/issues)
- [Skill specification](https://agentskills.io/specification)
- [Original source attribution](SOURCES.md)

Built and maintained by [VivatVibe](https://github.com/VivatVibe).
