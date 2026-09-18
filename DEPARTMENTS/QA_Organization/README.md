# QA Organization

An independent, evidence-driven QA function — built to be trusted with a real
release decision, and to survive changes in the model, the tooling, and the
person running it.

This is not a test script and not a smart prompt. It is a fixed operating
procedure (a state machine with mandatory, machine-checkable stages) executed
by a worker (currently an LLM, could be anything that satisfies the contract).
The procedure carries the rigor. The worker only supplies judgment inside a
bounded task.

## Why this exists

A prior attempt at this failed for two reasons, both structural, not
incidental:

1. It relied on a smart prompt ("perform comprehensive QA") and trusted the
   model to invent the right process every time. It didn't — it silently
   skipped an entire benchmarking obligation rather than admit it was
   inconvenient.
2. It tried to solve rigor by adding *more agents* (multi-worker
   coordination, GitHub-issue-driven state machines, orchestrator review
   queues) instead of a *stricter procedure*. That produced a lot of
   coordination machinery and zero completed product audits.

This version fixes both: one worker, a fixed sequence of stages, and a rule
that a stage may never disappear without an explicit, evidenced disposition.

## What "done" looks like for any QA cycle

Given a product handoff, this organization produces a QA Repo containing:
proof of what was tested, proof of what wasn't and why, a diagnostic index
that lets a future production error be traced back to a specific tested (or
known-untested) claim, and a final verdict — reported to the product owner,
who alone decides whether to release.

## Repository map

```
CONSTITUTION.md            Permanent principles. Do not casually edit.
LIFECYCLE.md                Three-repo model + versioned history model.
ENGINE/                     The state machine: stages, contracts, state schema.
CAPABILITIES/                Domain-specific testing knowledge (swappable).
HANDOFF_PACKAGE_TEMPLATE/   What a developer must hand QA to start a cycle.
EVOLUTION.md                 Designed now, NOT implemented in V0. Read before
                             assuming the organization can improve itself.
HISTORY/                     Why this is built this way. For a future
                             maintainer who wasn't in the room.
```

## Start here, by role

- **Running an audit right now:** read `LIFECYCLE.md`, then
  `ENGINE/STATE_MACHINE.md`, then follow `HANDOFF_PACKAGE_TEMPLATE/00_START_HERE.md`.
- **Adding or changing a capability:** `CAPABILITIES/CAPABILITIES.md`.
- **Understanding why a rule exists before changing it:** `HISTORY/DESIGN_DECISIONS.md`.
- **Wondering why there's no multi-agent orchestration here:** it was tried,
  it consumed effort without producing a QA result, and it's not coming
  back without evidence it's actually needed. See `HISTORY/DESIGN_DECISIONS.md`.

## Status

**V0 — the organization itself.** Constitution, engine, capability pool
concept, handoff package, and versioned history model are defined.
The evolution mechanism (capability acquisition, organization benchmarking,
self-improvement) is specified in `EVOLUTION.md` but deliberately **not**
built yet — you cannot safely evolve an organization you have not first
proven on a real product.
