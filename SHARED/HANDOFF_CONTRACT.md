# Handoff Contract — V1 (Completed)

## Why one schema, not one per role

Right now the Backend Developer worker has its own handoff format, and every other role either has none or would invent its own. That's fine in isolation but means the Orchestrator (or a human) has to learn a different shape per role to understand what happened. One schema, used everywhere, fixes that — a handoff always answers the same questions regardless of which role produced it.

## The schema

Every stage transition — a worker finishing its task, a Design Council role's design output, the Orchestrator moving a project from one phase to the next — produces:

```text
OBJECTIVE
  What this stage/task was actually trying to accomplish.

STATE
  SUCCEEDED | FAILED | BLOCKED | WAITING_FOR_HUMAN

INPUTS
  What was received to work from (requirements, prior handoffs,
  approved artifacts) — so downstream readers know what this
  output was actually built against.

DECISIONS
  What was decided, with reasoning — not just the conclusion.
  Rejected alternatives named where relevant (see Architect's
  and Data Architect's own rules for this pattern already).

EVIDENCE
  What supports the decisions/output — test results, load-test
  evidence, backup/restore verification, research findings,
  classified per the fact/assumption/inference/unknown distinction
  from AGENTS/Ideation/AGENT.md.

ASSUMPTIONS
  Explicitly marked as assumptions, never silently promoted to
  fact — same rule as Ideation, applied everywhere.

CONSTRAINTS
  Anything from HARD_CONSTRAINTS.md that was in play, and how it
  was handled (respected, routed to human, etc.)

OPEN QUESTIONS
  Genuinely unresolved items being carried forward — not hidden,
  per the CLEAR / CLEAR WITH OPEN ITEMS / BLOCKED discipline.

ARTIFACTS
  What files/outputs this produced or updated, with paths.

RISKS
  Known risks, including ones accepted rather than resolved —
  an accepted risk still gets recorded, not silently dropped.

EXPECTED NEXT ACTION
  Who picks this up next and what they're expected to do with it.
  A handoff without this is incomplete — see Orchestrator's rule.

APPROVAL STATUS
  Whether a human gate applies here, and if so, its current state.
  Silence is never approval — the global rule, restated in the
  one place every handoff has to pass through.
```

## How this relates to what already exists

- The Backend Developer worker's existing handoff format (WORKER / STATUS / IMPLEMENTED / etc.) maps cleanly onto this schema — it doesn't need to be rewritten, just understood as this schema's fields under slightly different names for that worker's specific domain. Future workers should use these field names directly rather than reinventing them.
- Design Council role outputs (an Architect's decision, a debate resolution) use this same shape — `DECISIONS` and `EVIDENCE` carry the weight there, `ARTIFACTS` points to the design package sections produced.
- `DEBATE_PROTOCOL.md`'s three outcomes (clean resolution, deadlock, infeasible premise) each populate this schema differently but through the same fields — a deadlock's `STATE` is `WAITING_FOR_HUMAN`, its `OPEN QUESTIONS` are the competing options, its `EXPECTED NEXT ACTION` is the human's tradeoff decision.
- **Pre-Planning's `DECISION_CONTRACT.md`** maps the same way: `OBJECTIVE` = the idea being evaluated; `STATE` = `GO`/`GO (fast-path)` → `SUCCEEDED`, `NO-GO` → `SUCCEEDED` (a NO-GO is a completed, correct disposition, not a failure of the stage), `NEEDS MORE EVIDENCE` → `WAITING_FOR_HUMAN`; `DECISIONS`/`EVIDENCE` = the four templates' content; `OPEN QUESTIONS` = explicit missing evidence; `EXPECTED NEXT ACTION` = Planning, or the human decision `NEEDS MORE EVIDENCE` requires. Its own field names (verdict, reasoning) stay — this is the mapping, not a rewrite, same precedent as the Backend Developer worker's format above.
- **`DISCOVERY_TEMPLATE.md`** (`DISCOVERY.md`, per story): `OBJECTIVE` = the story being elaborated; `STATE` = `CLEAR`/`CLEAR WITH OPEN ITEMS` → `SUCCEEDED`, `BLOCKED` → `BLOCKED`; `INPUTS` = the epic's `TRD.md`/`FRD.md` reference; `DECISIONS`/`EVIDENCE` = Phase 1 raw intake + Phase 2's accepted/pushed-back reasoning; `ASSUMPTIONS` = the template's own assumptions section, same meaning; `OPEN QUESTIONS` = Phase 2's open items; `EXPECTED NEXT ACTION` = the assigned Developer worker; `APPROVAL STATUS` = the required user confirmation, restated in this schema's terms.
- **A ticket's record (`SHARED/AGILE_WORKFLOW.md`, inside `Developer_Organization`)** maps its own fields directly: `status` ≈ `STATE` (`DONE` → `SUCCEEDED`, `BLOCKED` → `BLOCKED`, `IN PROGRESS`/`IN REVIEW` → in-flight, not yet a terminal `STATE`); `verification_evidence` = `EVIDENCE`; `assignee`/`moved_at` history = who and when, feeding `EXPECTED NEXT ACTION` once a fix or review is pending.
- **The "PRE-PLANNING VERDICT RECEIVED" record** (`AGENTS/Product-Owner/AGENT.md`, top of `requirements.md`) is itself the `INPUTS` this schema already calls for at Planning's own handoff — it is not a competing schema, it is Planning's `INPUTS` field, written out in enough detail to be checkable, per that section's own reasoning.
- **`DEPARTMENTS/Developer_Organization/SHARED/HANDOFF_TO_QA.md`'s assembled package** intentionally does not remap onto this schema — it is explicitly QA_Organization's own external contract (`HANDOFF_PACKAGE_TEMPLATE/`), a different organization's boundary, not a CodeFoundry-internal stage transition. This schema governs handoffs *within* CodeFoundry; the QA package is the one deliberate exception, stated here so it isn't mistaken for an oversight.

## Rule

No stage is considered handed off with a partial version of this — a missing `EXPECTED NEXT ACTION` or an omitted `OPEN QUESTIONS` section (even if empty, it should say "none" rather than not appear) is treated the same way a missing verification step is treated elsewhere in this system: incomplete, not done.
