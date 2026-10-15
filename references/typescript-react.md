# TypeScript, React, API and Workers Guide

Use only if relevant to the project. Follow its actual versions, conventions, and scripts first.

## TypeScript
- Prefer narrow types and discriminated unions for meaningful states.
- Validate untrusted runtime data; static types do not validate external JSON.
- Avoid `any` casts that hide actual gaps and avoid broad `try/catch` blocks that mask failures.
- Keep exported API shape stable during refactors.

## React
- Keep render logic pure; do not trigger network or irreversible effects while rendering.
- Handle effect cleanup, stale closures, async race/cancellation, loading, empty, and failure states.
- Use accessible labels, keyboard semantics, and clear focus behavior.
- Keep state in the closest coherent owner and avoid redundant derived state.
- Prefer clear components over deeply nested ternaries and oversized prop bags; avoid premature extraction.

## APIs / Cloudflare Workers
- Validate request bodies and authorization on the server.
- Handle retries and idempotency where writes may repeat.
- Distinguish operational failure from invalid client input with correct status codes.
- Avoid leaking internal error details and secrets.
- Respect data consistency/transaction boundaries for databases and object storage.

## Verification
Discover commands from this repository; typical categories include typecheck, unit tests, integration tests, lint, build, and browser e2e. Never assume pnpm, npm, or a test command until inspecting configuration.
