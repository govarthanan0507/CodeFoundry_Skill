# Project Timeline — V1

## Purpose

Track committed dates against actual progress, in the same field
structure Microsoft Project uses, so slippage is visible and followed
up on — not just estimated once and forgotten. Owned by the
**Orchestrator** (mechanics/state, not judgment — see
`AGENTS/Orchestrator/AGENT.md`), the same reasoning already applied to
retry/re-entry/session-continuity tracking. The Orchestrator never
invents a date; it only records dates given by whoever actually owns
the estimate, and follows up on them.

## Who gives the date — never the Orchestrator, never Planning

Per the earlier ruling: Product Manager/Product Owner do not estimate
duration (they don't know implementation complexity). The estimate
comes from whoever scopes or builds the work:

```text
Design Council (Architect/domain Architect) — when it scopes the
"how" for an epic, at the same time it produces the architecture
decision — gives the epic's duration estimate.
        ↓
Development worker (Frontend/Backend/Mobile Developer) — once build
starts and real complexity is visible — may revise that estimate;
a revision is recorded as a new value with a reason, never a silent
overwrite (same "nothing overwritten" discipline as everywhere else).
        ↓
Orchestrator records whatever value it's given, with its source, and
tracks it from there. It does not adjudicate whether an estimate is
reasonable — that's a specialist judgment call outside its mandate.
```

## The record — one row per task/epic, MS-Project field structure

```text
ID              — unique task/epic identifier
NAME            — traces to the Product Manager's epic (or a
                  Development-level subtask under one)
DURATION        — estimate, with unit (d/w/mo), and SOURCE (which
                  Architect or Developer worker gave it, and when)
START           — planned start date
FINISH          — planned finish date
PREDECESSORS    — task ID(s) this depends on, plus dependency type:
                  FS (finish-to-start), FF (finish-to-finish),
                  SS (start-to-start), SF (start-to-finish) — same
                  four types Microsoft Project uses, not a simplified
                  subset
RESOURCE        — which worker/role is assigned (Frontend Developer,
                  Backend Developer, etc.)
PERCENT COMPLETE — updated at each stage handoff/check-in, sourced
                  from the assigned worker's own reported progress,
                  never inferred by the Orchestrator
STATUS          — ON TRACK | AT RISK | SLIPPED (see below)
```

## Critical path

Computed mechanically from DURATION + PREDECESSORS across all rows —
the longest dependency chain determines the earliest possible finish
for the whole project, same as Microsoft Project's scheduling engine.
This is a pure calculation (mechanics, not judgment), so it stays
inside the Orchestrator's mandate even though everything feeding it
(the estimates themselves) comes from elsewhere.

## Status and slippage — never silently dropped

```text
At every stage handoff or scheduled check-in:
        ↓
Compare PERCENT COMPLETE's implied pace against DURATION/FINISH.
        ↓
On pace or ahead → STATUS: ON TRACK. No action.
        ↓
Behind, but recoverable within existing FINISH → STATUS: AT RISK.
Flagged explicitly in the next handoff — not silently absorbed.
        ↓
Behind, FINISH is no longer achievable as committed → STATUS:
SLIPPED. Surfaced immediately, not held for the next scheduled
check-in — same "never wait to report a known problem" discipline
used for CI/red-build handling elsewhere. A SLIPPED task also
recalculates the critical path — if it's on the critical path, every
downstream FINISH date shifts and that cascade is reported too, not
just the one row.
```

A SLIPPED status is not itself a decision about what to do (cut scope,
add resource, accept the delay) — that's a human call, same boundary
`HARD_CONSTRAINTS.md` already draws for other consequential decisions
("timeline/deadline constraints," category 11). The Orchestrator
reports the slip and its downstream impact; it does not choose the
response.

## Relationship to existing files

- Does not replace `SHARED/PARALLELIZATION_GUARDRAIL.md`'s concurrency
  check — that decides *whether* phases/epics can run alongside each
  other; this file tracks *when* each one is committed to finish once
  that's decided. A phase cleared for concurrency still gets its own
  row here.
- Does not replace `SHARED/EPIC_SELECTION_CRITERIA.md`'s dependency
  check (Step 5) — that decides build-order necessity at selection
  time; PREDECESSORS here is the same dependency, carried into
  schedule form once the epic is actually underway.
- Feeds `AGENTS/Orchestrator/AGENT.md`'s existing state-maintenance
  responsibility (`project-state.md`) as one more tracked artifact, not
  a separate mechanism competing with it.
