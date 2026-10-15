# Practical Clean Code Principles

These are original, technology-neutral interpretations of commonly taught maintainability principles, including topics discussed in Robert C. Martin's *Clean Code*.

## Names and intent
Choose vocabulary from the user's domain. A reader should not need to infer units, nullability, lifecycle, or meaning from an abbreviation. Prefer `retryDelayMs` over `d`, and `isInvoicePaid` over `statusFlag`. Avoid renames that break public contracts without a migration.

## Cohesive functions
A function should have a discoverable purpose. Extract code when doing so clarifies an independent concept, enables verification, or isolates side effects. Avoid one-line wrapper chains that force navigation across files. Optimize for comprehension, not function length thresholds.

## Clear boundaries
Keep persistence, networking, clocks, and randomness at boundaries where practical. Domain rules should be testable without launching an entire app. Avoid dependency injection frameworks when a simple parameter suffices.

## Data and state
Make invariants and ownership clear. Prefer explicit states over multiple overlapping booleans. Avoid mutable shared state and accidental aliasing when concurrency or asynchronous steps make behavior ambiguous.

## Errors
Validate at trust boundaries and preserve useful failure information. Do not swallow exceptions, convert distinct failure modes into a misleading success, or leak credentials in logs. Prefer errors that help the caller choose a recovery path.

## Comments
Document *why* a surprising choice is necessary, and cite external constraints when appropriate. Keep API docs synced with contracts. Remove misleading comments; clear code remains the first tool.

## Duplication versus abstraction
Remove duplicated business rules that must change together. Keep independent, superficially similar cases separate if generalization makes them harder to understand. Avoid premature generalized helpers.

## Test design
Tests should demonstrate observable guarantees and meaningful failure modes. Cover boundaries and risks, not just line coverage. Favor isolated deterministic tests; use integration/e2e tests for contracts mocks cannot prove. A failing test is a signal to investigate, not something to delete.

## Trade-offs
No single style rule beats correctness, measured performance, compatibility, security, accessibility, or existing conventions. Document exceptional choices instead of mechanically rewriting code.
