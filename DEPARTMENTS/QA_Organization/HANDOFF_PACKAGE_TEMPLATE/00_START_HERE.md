# QA Handoff Package — Start Here

This package is what a developer hands to the QA Organization to begin a
cycle. It is not a zip of source code — it is a controlled, complete
package: the exact product to test, the reference material to benchmark
against, and the data to test with. The QA worker should need nothing
outside this package (plus the QA Organization repository itself) to run
Stages 0-14.

## What must be filled in before a cycle can start

| Path | What goes here | Filled by |
|---|---|---|
| `01_QA_CONTRACT.md` | scope, authorization boundaries, what's out of scope | product owner |
| `02_EXECUTION_PROTOCOL.md` | environment requirements, how to build/run the product | developer |
| `product-under-test/` | the exact, pinned source/build to test | developer |
| `reference-projects/manifest.json` + vendored copies | competitor/reference implementations, pinned | product owner / developer |
| `benchmark-suite/` | the actual comparison harness/criteria | product owner |
| `test-data/` | fixture data for functional testing | developer |
| `adversarial-data/` | malformed/malicious/boundary-breaking inputs, with authorization noted in the contract | product owner |

## Why reference projects are vendored, not just linked

An earlier attempt at this organization had an agent skip benchmarking
entirely because cloning and running comparison projects "took too much
time." Vendoring them into the handoff package removes that excuse — the
comparison material is already present, pinned to a specific commit, and
running it is the same as running any other capability. If a reference
project genuinely cannot run in the QA environment, Stage 10 requires that
be recorded as `BLOCKED` with a specific reason, never silently dropped.

## First step for the QA worker

Read `01_QA_CONTRACT.md`, then proceed to `ENGINE/STATE_MACHINE.md` Stage 0.
