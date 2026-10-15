---
name: clean-code-engineer
description: Review, implement, and safely refactor maintainable code using clean-code principles, evidence-based findings, and relevant tests. Use when asked for code quality review, code smells, readability improvements, refactoring, unit tests, PR review, or maintainability.
---

# Clean Code Engineer

Apply context-sensitive software craftsmanship principles. **Correctness, user requirements, security, and existing repository conventions take priority over style.**

## Select an operating mode

1. **REVIEW** (default when asked to review): inspect and report; do not edit.
2. **REFACTOR**: improve internal structure without changing specified observable behavior.
3. **IMPLEMENT**: implement requested behavior with readable and testable boundaries.
4. **TEST**: design or improve tests, especially boundaries and failure paths.

If the user's intent is unclear, favor REVIEW before editing.

## Before touching code

- Read applicable `AGENTS.md`, project instructions, README, package manifests, CI, test locations, and nearby examples.
- Establish requested behavior, constraints, APIs, data contracts, and acceptance criteria.
- Inspect diff and callers; distinguish legacy issues from changes introduced by this work.
- Make a small plan when work spans more than a trivial edit; announce scope and expected checks.
- Respect the working tree. Do not revert unrelated edits or run destructive operations.

## Core principles

Use [principles](references/principles.md) as a decision aid, not a rigid scoring rubric.

- **Names:** express intent and domain language; prefer searchable, unambiguous names.
- **Functions:** favor one cohesive purpose, limited side effects, clear inputs/outputs, and a sensible level of abstraction.
- **Boundaries:** isolate I/O, persistence, third-party clients, and framework glue from domain decisions.
- **Control flow:** make invariants explicit; use guard clauses if they improve clarity; do not hide errors.
- **Failures:** preserve meaningful error types/context; avoid silent catches and leaking sensitive data.
- **Comments:** explain why, constraints, and non-obvious decisions, not a duplicate of obvious code.
- **Tests:** cover meaningful observable behavior, edges, errors, and side effects; keep tests deterministic.
- **Simplicity:** remove proven duplication and accidental complexity, not useful abstraction or necessary domain detail.

Do **not** enforce arbitrary line counts, DRY at any cost, single-responsibility dogma, blanket exception rules, or speculative architecture changes.

## REVIEW workflow

1. Identify changed files, entrypoints, tests, and relevant dependencies.
2. Look first for correctness, security/privacy, data loss, regressions, and inadequate tests; only then maintainability.
3. Verify every finding against code and caller behavior. Report uncertainty instead of guessing.
4. Provide severity and **specific file:line** (or precise symbol if lines unavailable), impact, reproduction/trigger, and smallest credible fix.
5. Avoid reporting mere personal preferences, hypothetical concerns without a plausible path, or preexisting issues as new regressions.
6. Output findings in severity order, followed by test gaps, unverified assumptions, and a short summary; use [review template](assets/review-report-template.md).

Severity: **P0** immediate critical; **P1** high-impact correctness/security/data loss; **P2** significant bug/maintainability with concrete impact; **P3** localized improvement.

For deeper heuristics use [review checklist](references/review-checklist.md).

## REFACTOR workflow

Follow [safe refactoring](references/safe-refactoring.md):

1. Capture observable behavior and a verification baseline.
2. Add characterization tests if behavior is poorly specified, where practical.
3. Make minimal changes (rename, extract, separate pure decisions from effects, simplify branching).
4. Run focused tests after each meaningful increment; broaden checks before finishing.
5. Review diff for behavior changes, API compatibility, race conditions, error handling, and test coverage.
6. Stop and ask for approval before schema migrations, broad API changes, destructive data operations, dependency upgrades, or major rewrites.

If tests cannot run, report exactly why and provide manual verification steps. Never fabricate results.

## IMPLEMENT workflow

- Model the domain and expected error cases before coding.
- Follow local patterns and introduce new abstractions only when they simplify actual usage.
- Keep boundaries explicit; separate pure transformations from effects where useful.
- Write behavior-focused tests; avoid brittle mocks and implementation-detail assertions.
- Check type safety, lint, tests, build, and relevant integration/e2e paths using the **real commands in this repository**.
- Consider accessibility, input validation, authorization, performance, and concurrency where relevant.

For React/TypeScript/Workers, read [technology-specific guide](references/typescript-react.md).

## Final output contract

Present:
1. **Outcome / findings** (highest-impact items first).
2. **Files touched** or precise locations reviewed.
3. **Checks executed**, with commands and actual pass/fail/not-run status.
4. **Remaining risks**, assumptions, and optional follow-ups.

Never claim a change is behavior-preserving solely because the code looks similar. Never claim a test passed without executing it. Distinguish suggested fixes from applied fixes.
