# Evidence-based Code Review Checklist

## Start with consequences
- **P0**: an immediately exploitable critical flaw or catastrophic failure requiring urgent action.
- **P1**: high-impact security/authentication error, data corruption or loss, major regression.
- **P2**: realistic bug affecting important workflow, or maintainability issue demonstrably obstructing safe changes.
- **P3**: concrete localized clarity/test/doc improvement with limited impact.

Review claims must identify *what happens*, *when it happens*, and *why this code causes it*. Avoid inflated severity.

## Correctness
- State transitions, off-by-one boundaries, empty/duplicate inputs, timezone/locale, rounding, cancellation, timeouts, retries, partial failure, idempotency.
- Nullability and invalid inputs at external boundaries.
- Async races, stale state, transactional consistency, cleanup.

## Security and privacy
- Authorization at server boundaries; client-side hiding is insufficient.
- Parameterized queries, output escaping and input validation.
- Secret handling, secure logs, safe file paths, predictable error disclosure.

## Understandability
- Are names precise, responsibilities coherent, levels of abstraction consistent?
- Is duplicated business logic likely to drift?
- Are error paths observable and actionable?
- Do comments explain constraints rather than restate code?

## Tests
- Does a test fail under the identified defect?
- Are success, boundary, error, and important side-effect paths exercised?
- Are tests deterministic and not coupled to internal refactorings?
- Was the relevant test command actually executed?

## Reporting discipline
Format each finding: `[P2] Title — path:line` then evidence, impact, triggering condition, minimal fix. Include confidence level when uncertain. Separate verified issues, potential risks, and style preferences. If no defects were found, say so and disclose review scope and residual blind spots.
