# QA Contract — Backend Verification and Evidence Rules

## Principle

A passing build, a green test suite, or a successful manual request against a happy path is not proof the backend is complete. Evidence must match the actual risk of the change (see workflow.md's risk-scaled verification).

## Minimum evidence by category

### Functional

- Primary API flows exercised end-to-end against the real data layer, not a mock, wherever feasible.
- Acceptance criteria explicitly mapped to what was observed, not assumed.
- Edge cases and error paths checked, not only the happy path.

### Data integrity

- Schema constraints verified to actually reject invalid data (tested, not just declared).
- Migration applies cleanly on a copy of realistic data, not only an empty database.
- Rollback script executed and confirmed to return the schema to its prior state.

### Backup and recoverability

- For any migration or destructive change: a backup was taken AND a restore from that backup was actually performed and verified — a backup that has never been restored is unverified.
- The evidence log states where the backup/restore was performed (which environment) and the outcome.

### Performance

- Load/latency behavior checked at a level appropriate to the product's current stage — do not skip this for "it's just an MVP," but do not demand production-scale load testing for a feature with a handful of users either.
- Known N+1 query patterns or missing indexes are called out, not silently shipped.

### Security

- Authentication and authorization checked on new or modified endpoints.
- Input validation confirmed on all external inputs.
- No secrets, credentials, or sensitive data present in code, logs, or error messages.

## Failure handling

A failed check is recorded plainly — what failed, why, and what the fix or escalation is. A failure is never hidden inside a "SUCCEEDED" handoff to make the status look cleaner. `BLOCKED` and `FAILED` are legitimate, useful states, not something to avoid reporting.

## What "done" means here

Done means the evidence above exists and is attached to the handoff, scaled to this change's risk tier — not that the worker believes the code is probably fine.
