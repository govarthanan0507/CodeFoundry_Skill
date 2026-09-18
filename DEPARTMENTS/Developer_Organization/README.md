# Developer Organization

The build side of CodeFoundry — the department that turns an already-
decided design (a `TRD.md`/`FRD.md` from Design Council, a per-story
`DISCOVERY.md`) into working, verified software, then hands it to an
independent QA organization and iterates until QA clears it.

This is not a rebuild of anything. Every capability in
`CAPABILITIES/` and every workflow file in `SHARED/` is the same
content already hardened inside CodeFoundry this session — extracted
and repackaged here so this department can be shipped, read, and run
on its own, the same way `QA_Organization` already is. Nothing here
was invented from scratch; this file exists to organize, not to
reinvent.

## Why this is packaged separately from CodeFoundry and from QA_Organization

CodeFoundry is the umbrella — a company with departments (Ideation,
Pre-Planning, Design Council, this one, QA, eventually Release). Each
department is meant to be independently packaged and shippable, not
only usable as part of one monolith. `QA_Organization` proved that
model first, as its own real repo with its own constitution and
engine. This is the same model applied to the build side.

## The one hard rule for this organization

Everything else here is process detail. This is the rule that doesn't
bend: **every ticket's current state and every Discovery finding
reached while working it are logged, periodically, as they happen —
not reconstructed afterward.** A developer who can't say, right now,
which ticket they're on and what they've learned while working it has
violated this organization's one non-negotiable rule, regardless of
how good the eventual code turns out to be. See `CONSTITUTION.md`
principle 1.

## Repository map

```
CONSTITUTION.md      Permanent principles. The logging rule lives here.
LIFECYCLE.md         The actual pipeline: inbound design → ticket flow
                     → QA handoff → iterative fix loop → next team.
CAPABILITIES/        Frontend / Backend / Mobile Developer workers —
                     each already hardened, unchanged in substance.
SHARED/              Kanban/ticket workflow, delivery timeline
                     tracking, parallelization rules, tiering, and the
                     QA handoff/loop protocol.
INBOUND_HANDOFF/     What this organization requires before it starts
                     work — from Design Council, from Planning.
HISTORY/             Why this is built this way.
```

## Start here, by role

- **Picking up a ticket right now:** `SHARED/AGILE_WORKFLOW.md`, then
  the relevant capability's `workflow.md`.
- **Understanding the QA loop:** `SHARED/HANDOFF_TO_QA.md`.
- **Understanding what must arrive before work starts:**
  `INBOUND_HANDOFF/00_START_HERE.md`.
- **Why the logging rule is non-negotiable:** `HISTORY/DESIGN_DECISIONS.md`.

## Status

**V0 — extracted and repackaged from CodeFoundry's already-hardened
build side, this session.** No new capability was invented here; this
is organization, not origination. The one addition specific to this
package is the explicit, constitutional logging rule — CodeFoundry's
own files already tracked most of this data, but never stated it as a
non-negotiable principle in its own right until this package did.
