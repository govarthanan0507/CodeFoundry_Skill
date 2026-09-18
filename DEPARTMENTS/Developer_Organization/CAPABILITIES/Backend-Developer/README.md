# CodeFoundry Backend Developer Worker

This package turns the CodeFoundry backend specialist into an explicit worker with its own skill, workflow, API/data contract, QA contract, and advisory reliability principles — mirroring the structure of the Frontend Developer worker.

## Package

- `CAPABILITY.md` — agent-facing operating instructions (renamed from SKILL.md so only the package root keeps that reserved name)
- `workflow.md` — execution lifecycle, including risk-scaled verification
- `API_CONTRACT.md` — contract-first design rules, database/infra choice reasoning, portability and backup discipline
- `QA_CONTRACT.md` — verification and evidence rules
- `RELIABILITY_PRINCIPLES.md` — advisory senior-engineer judgment knowledge for critic mode
- `../../AGENTS/Backend/AGENT.md` — CodeFoundry specialist identity and handoff contract

## Reference capabilities

The worker is designed around three complementary ideas, referenced conceptually (not copied as third-party implementations):

1. **Contract-first API design with real verification** — specify and validate the API contract (lint + mock-server verification) before implementation, rather than discovering the contract from the code afterward.
2. **Schema/migration discipline with paired rollbacks and load verification** — every migration ships with a tested rollback; performance is checked with real load behavior, not assumed from a passing build.
3. **Operational maturity as a hard rule, not a convention** — backup-before-destructive-operation, restore-tested (not just backup-created), and stage-appropriate database choice with an explicit portability plan for migrating off it later.

CodeFoundry retains authority over lifecycle gates, approvals, evidence, and worker completion state.

## V1 completion principle

```text
Code written
   !=
Backend complete

Backend complete
   =
Implementation + migration safety (rollback + verified backup) + load/security verification + evidence
```

**Test boundary:** this worker package is directly testable as one unit; its linked specialist identity is a dependency, not a second worker.
