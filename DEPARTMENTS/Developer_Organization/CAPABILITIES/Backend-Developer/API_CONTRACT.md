# API / Data Contract Rules

## Purpose

Keep the API and data model as durable, reviewable project artifacts — the backend equivalent of a persistent `DESIGN.md` — instead of implicit knowledge trapped in code.

## Ownership split — this file formalizes a decision, it does not make one

The API contract's *shape* (endpoints, boundaries, what's exposed to
the frontend versus kept internal) is decided upstream, at design
time, by the Backend/API Architect negotiating with the Frontend
Architect (`COUNCILS/Design-Council/roles/backend-architect.md`,
recorded in that project's `TRD.md`). This worker does not invent or
renegotiate those boundaries — it takes the decided shape and turns it
into a concrete, formal, validated spec. A boundary that seems wrong
once implementation starts is a Change Request back to the Backend/API
Architect (`COUNCILS/Design-Council/COUNCIL.md`'s post-handoff
accountability), not a silent local redesign.

## Contract-first discipline

1. Specify the API contract (e.g. an OpenAPI/schema definition) before implementation begins — formalizing the shape `TRD.md` already decided, not deciding it fresh.
2. Validate/lint the spec before proceeding.
3. Where tooling supports it, verify the contract against a mock server before real implementation, so contract mistakes are caught before they're built into working code and consumed by a frontend.
4. Treat the validated contract as the interface promise to consumers (frontend, other services). Breaking it requires the same approval weight as an architecture change.

## Data model rules

- Every table/collection has an explicit reason to exist tied to a requirement.
- Constraints (foreign keys, uniqueness, not-null) are part of the design, not an afterthought bolted on after a bug.
- Every migration is paired with a tested rollback script. An untested rollback is treated as no rollback.
- Indexes are chosen from actual query patterns, not guessed. Missing-index and N+1 risks are checked, not assumed absent.

## Database/infrastructure choice — reasoning required

State, in `DATA_MODEL.md` or the handoff:

```text
STAGE: MVP | growth | production-scale
BUDGET CONTEXT: ...
CHOICE: ...
REASONING: why this fits the current stage/budget
PORTABILITY: how platform-specific coupling is isolated (adapter layer, standard SQL) so a future migration doesn't require a rewrite
REVISIT WHEN: the concrete trigger that would justify re-evaluating this choice (e.g. concurrency threshold, compliance requirement, cost threshold)
```

Do not choose a platform out of habit, and do not over-provision for scale that has no evidence of arriving.

## Portability rule

Keep schema and query logic in standard, portable SQL. Isolate any platform-specific SDK, auth, or client coupling behind a thin adapter rather than spreading it through business logic. This is what makes "migrate later if we outgrow the free tier" actually cheap instead of theoretical.

## Backup and rollback are part of the contract, not operations' problem

For any migration or destructive operation:

1. A backup is taken.
2. The backup is test-restored (not just created) before the operation proceeds.
3. The forward operation runs.
4. The rollback path is confirmed to exist and, where feasible, has itself been exercised.

Skipping any of these four steps means the operation is not ready, regardless of how confident the implementation looks.
