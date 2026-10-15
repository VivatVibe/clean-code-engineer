# Safe Refactoring Playbook

## 1. Establish boundaries
Record user-visible behavior, API request/response shapes, database effects, event names, error semantics, and performance constraints. Check callers and existing tests.

## 2. Get a trustworthy baseline
Inspect repository-defined commands (package scripts, Makefile, CI). Run the most relevant existing tests if the environment allows. Record initial failures separately from regressions.

## 3. Characterize unknown behavior
Add a small regression/characterization test before changing behavior when feasible. Avoid asserting bugs are desired behavior unless compatibility requires preserving them.

## 4. Change incrementally
Safer moves often include explicit renames, extracting pure calculations, replacing deeply nested branches with clearly equivalent conditions, and eliminating verified dead paths. One conceptual change per commit or reviewable diff.

## 5. Verify assumptions
Re-run focused tests, type checks, lint, and build as appropriate. Inspect generated artifacts and runtime integration if changes touch routing, state, persistence, async behavior, or public APIs.

## 6. Review the final diff
Ask: were error types/messages, timing, ordering, transaction boundaries, null handling, access controls, or side effects modified? Did the refactor accidentally change public exports or test helpers only?

## 7. Report honestly
List passed/failed/not-run checks with exact commands. Identify residual risks and a rollback path. Do not merge or deploy without permission.

### Stop-and-confirm changes
Get explicit approval for destructive commands, data migrations, broad public API changes, behavior changes outside requested scope, large rewrites, new paid services, or dependency upgrades.
