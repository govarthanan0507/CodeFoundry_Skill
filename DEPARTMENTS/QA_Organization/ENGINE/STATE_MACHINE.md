# The QA Engine: State Machine Overview

This is the fixed procedure. It does not change per product. What changes
per product is which capabilities get invoked inside stages 5-11, and the
content of the manifest that Stage 2 reads. The procedure itself — the
sequence, the checkpoints, the disposition requirement — is constant.

State lives in the repository, not in the worker's memory. `QA_STATE.json`
(schema: `ENGINE/QA_STATE.schema.json`) plus the last checkpoint commit is
the entire resumability mechanism: any worker, of any size or model, can
open the state file, read the current stage, inspect the last checkpoint,
and continue. A worker must never rely on conversational memory of prior
stages — if it isn't in the repo, it didn't happen.

## Fail-safe rule (applies to every stage, no exceptions)

If a worker does not know what to do next — the current stage's contract
doesn't cover the situation, evidence is ambiguous, a required input is
missing — it must not guess or improvise a workaround. It must either (a)
re-read the current stage's contract and the repository state, or (b) record
`BLOCKED` with the specific reason and stop. Guessing is the one thing this
engine exists to prevent.

## The fifteen stages

```
STAGE 0  — INTAKE
  Read the QA contract. Create the QA Repo structure. Acquire the exact,
  authorized product snapshot from the handoff package. Record provenance
  (version/commit, who authorized it, what environment it's headed for).
  ↓ CHECKPOINT COMMIT

STAGE 1  — ENVIRONMENT QUALIFICATION
  Verify the QA environment itself is trustworthy before anything run in it
  counts as evidence: dependencies resolve, the product actually builds/runs,
  isolation from production and from the developer's other repos holds.
  ↓ CHECKPOINT

STAGE 2  — RECONNAISSANCE
  Inventory the product's architecture and components. Decide which
  capabilities from CAPABILITIES/ actually apply to this product (a CLI tool
  does not pull in the accessibility capability; a public web app does).
  ↓ CHECKPOINT

STAGE 3  — RISK MODEL & STRATEGY
  For every component identified in Stage 2, identify what can fail, how
  severe, how it would be detected, and whether it applies. Produces the
  risk register that Stage 13 (coverage) will later check against. Write the
  test strategy: what will be tested, in what order, with what capabilities.
  ↓ CHECKPOINT

STAGE 4  — TEST DESIGN
  Turn the strategy into concrete, literal, re-runnable test cases per
  applicable capability, plus the boundary conditions (scale, concurrency,
  data volume) each one will exercise.
  ↓ CHECKPOINT

STAGE 5  — FUNCTIONAL EXECUTION
  Run the happy-path / specified-behavior tests. Record verbatim results.
  ↓ CHECKPOINT

STAGE 6  — ADVERSARIAL / NEGATIVE / BOUNDARY
  Malformed input, invalid states, edge conditions, boundary values, per
  applicable capability.
  ↓ CHECKPOINT

STAGE 7  — PERSISTENCE / RECOVERY / REGRESSION
  Restart, crash-recovery, backup/restore verification (an untested restore
  is not a backup, it's an assumption), regression against prior findings.
  ↓ CHECKPOINT

STAGE 8  — NON-FUNCTIONAL / SCALE
  Load, stress, soak, spike testing against explicit numeric targets
  (throughput, latency, resource ceilings). This is the stage that exists
  specifically because "worked in QA, broke at scale" is almost always a
  boundary-condition gap, not a logic bug — see HISTORY/DESIGN_DECISIONS.md.
  ↓ CHECKPOINT

STAGE 9  — OBSERVABILITY READINESS
  Check whether the product emits enough logs/metrics/traces to diagnose a
  failure in production at all. Insufficient observability is itself a
  FAILED finding here, not a testing gap to shrug at — without it, nothing
  else this organization records helps trace a real incident later.
  ↓ CHECKPOINT

STAGE 10 — BENCHMARK / COMPETITIVE VALIDATION
  Compare against reference projects/implementations from the handoff
  package. If a comparison cannot be executed, record why as BLOCKED — never
  silently drop it. This is the exact failure this organization was
  originally built to stop repeating.
  ↓ CHECKPOINT

STAGE 11 — INDEPENDENT EXPLORATORY TESTING
  Off-script investigation: what would a skeptical, experienced tester poke
  at that nobody explicitly planned for. This is the one stage allowed to
  send findings backward — see "Loop-back" below.
  ↓ CHECKPOINT

STAGE 12 — FINDINGS: REPRODUCE, ROOT CAUSE, IMPACT
  Every failure from stages 5-11 gets a reproduction procedure, a root-cause
  investigation (evidence-supported, not speculative), and an impact
  assessment.
  ↓ CHECKPOINT

STAGE 13 — COVERAGE ANALYSIS
  Check every identified risk area (from Stage 3's register) against its
  disposition. Nothing may be missing, silent, or implied — every entry is
  PASSED / FAILED / BLOCKED / NOT_APPLICABLE / DEFERRED, explicitly.
  ↓ CHECKPOINT

STAGE 14 — FINAL AUDIT
  Compile the verdict, compile and commit the Diagnostic Index (mandatory,
  Constitution §6), state confidence and every open limitation. Report to
  the product owner. Does NOT issue a release decision — that's the
  product owner's call (Constitution §9, LIFECYCLE.md).
  ↓ FINAL HANDOFF
```

## Loop-back: the one exception to strict linearity

Stage 11 (exploratory) and Stage 12 (root-cause investigation) are the only
stages allowed to send work backward. If exploratory testing or root-cause
analysis reveals that Stage 3's risk model or Stage 4's test design was
incomplete, the worker re-enters Stage 4/5/6 for the newly identified area,
executes it, checkpoints it, and then resumes forward from where it left
off. Every stage in the sequence still runs in order for the *new* finding;
what loops is scope, not the sequence itself. This is recorded explicitly in
`QA_STATE.json` as a `reentry` event, not treated as if it never happened.

Every other stage is strictly linear. Stage 12 cannot start before Stage 11
has produced a checkpoint; Stage 14 cannot start before Stage 13 has an
explicit disposition for every risk area.

## The disposition mandate, applied per-stage

Constitution §3 isn't scoped to test execution alone — it binds every one of
the fifteen stages. Stage 1 (environment qualification) can be `BLOCKED`.
Stage 9 (observability) can be `FAILED`. Stage 10 (benchmark) can be
`DEFERRED` if a reference project genuinely cannot be run — but that
disposition, with its reason, is what goes in the record, never silence.
See `STAGE_CONTRACTS.md` for the exact `ALLOWED_OUTCOME` set per stage.
