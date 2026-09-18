# Agile Workflow — Kanban, Tickets, Velocity — V1

## Purpose

Development runs as continuous, incremental delivery — one version at a
time, per `LIFECYCLE`-style versioning already used elsewhere in this
system (nothing overwritten, each increment preserved) — tracked
through a real Kanban board, one ticket per user story, with a visible
log of who is working on what right now, and a velocity record that
feeds back into future estimates instead of guessing every time.

## One ticket per user story — no exceptions

Every user story the Product Owner writes in `requirements.md`
(`AGENTS/Product-Owner/AGENT.md`) becomes exactly one ticket, same ID.
A ticket is never split silently into hidden sub-work a developer
tracks privately, and a story is never bundled into another ticket —
both are already-named anti-patterns in the Product Owner's own file
("a story that's really three stories bundled together") applied here
to ticket granularity specifically.

```text
TICKET
  id:            <matches requirements.md story ID>
  title:         <the user story, one line>
  epic:          <traces to Product Manager's epic — no orphan tickets>
  story_points:  <estimate, sourced from the assigned Developer worker
                  at ticket creation — never invented by Product Owner
                  or Orchestrator, same rule as duration estimates in
                  PROJECT_TIMELINE.md>
  acceptance_criteria: <link to the story's checklist in requirements.md>
  status:        BACKLOG | TO DO | IN PROGRESS | IN REVIEW | DONE | BLOCKED
  assignee:      <the specific Developer worker instance currently
                  holding it — never blank while status is IN PROGRESS
                  or IN REVIEW>
  version:       <which increment/release this ticket belongs to>
  started_at / moved_at: <timestamp of each column transition, kept as
                  history, not overwritten — same "nothing overwritten"
                  discipline as everywhere else>
  verification_evidence: <required before IN REVIEW → DONE — a pointer
                  to the specific checks actually performed and their
                  result, per the assigned worker's own evidence rules
                  (DEPARTMENTS/Developer_Organization/CAPABILITIES/Frontend-Developer/QA_CONTRACT.md or
                  DEPARTMENTS/Developer_Organization/CAPABILITIES/Backend-Developer/QA_CONTRACT.md's category
                  list — Functional, Data integrity, Security, etc.).
                  This does not duplicate that evidence, it references
                  where it lives, so "what test cases have been done"
                  is answerable from the ticket itself instead of
                  requiring someone to go dig through the worker's
                  handoff separately. A ticket moved to DONE with this
                  field empty is incomplete, same severity as any
                  other missing required field on this record.>
```

## Kanban board — columns mirror the real workflow, not a token gesture

Per Kanban's five components (visual signals, columns, WIP limits, a
commitment point, a delivery point): columns are `BACKLOG → TO DO →
IN PROGRESS → IN REVIEW → DONE`, with `BLOCKED` as a visible side-state
on any ticket rather than its own column (a blocked ticket keeps its
real column so the board doesn't hide where it actually is stuck).

```text
BACKLOG      — ticket exists, not yet pulled into this version
TO DO        — pulled into the current version, not started
IN PROGRESS  — a Developer worker is actively on it (assignee required).
               Entry gated: per
               `COUNCILS/Design-Council/DISCOVERY_PROTOCOL.md`, a
               ticket may not move here until its per-story Discovery
               record is CLEAR or CLEAR WITH OPEN ITEMS. A BLOCKED
               Discovery keeps the ticket in TO DO, not started anyway.
               Enforced by the Orchestrator reading the actual
               `DISCOVERY.md` file directly (`AGENTS/Orchestrator/
               AGENT.md`'s ticket progression gate) — not inferred
               from the assigned worker saying Discovery is done.
IN REVIEW    — implementation done, awaiting the worker's own
               completion-contract checks or independent review
               (QA/Security, per PROCESS_SCALING.md's review-triggering
               rule) — not yet DONE
DONE         — completion contract satisfied, evidence recorded.
               Enforced by the Orchestrator independently checking
               `verification_evidence` is actually populated before
               allowing this move (`AGENTS/Orchestrator/AGENT.md`'s
               ticket progression gate) — a worker marking itself
               DONE with that field empty is a routing error, not
               honored.
```

**WIP limits** (required, per Kanban's own discipline — a board with no
limit isn't really Kanban, it's a list): a single Developer worker
instance holds at most one ticket in `IN PROGRESS` at a time. This is
what makes the "who's working on what right now" log meaningful —
without a WIP limit, "in progress" stops mapping to what's actually
being worked on.

## The active-work log — who's doing what, right now

A live view, not a separate document to reconcile against the board —
derived directly from every ticket currently in `IN PROGRESS` or
`IN REVIEW`:

```text
TICKET  | ASSIGNEE              | STATUS      | SINCE | EVIDENCE
D-BE-03 | Backend Developer #1  | IN PROGRESS | D+9   | (in progress — none yet)
D-FE-02 | Frontend Developer #1 | IN REVIEW   | D+12  | QA_CONTRACT §Functional, §Responsive: pass
```

The EVIDENCE column is what answers "who picked this up, when, and
what's actually been checked on it" from one place — the log is the
answer, not a separate document someone has to reconcile against it.

Maintained by the **Orchestrator** (mechanics/state, consistent with
`SHARED/PROJECT_TIMELINE.md`'s ownership reasoning) — it reads ticket
status/assignee, it does not decide who gets assigned what; assignment
is the Developer worker accepting a pulled ticket, not the Orchestrator
dispatching one.

## Velocity — measured, never assumed, and fed back into future estimates

```text
Per completed version/sprint:
  velocity = SUM(story_points of tickets that reached DONE
                 fully within that version)
             — a ticket only partially done does NOT count, even
               partially; this matches the standard rule that
               incomplete stories are excluded, not prorated.

Average velocity = SUM(velocity across N versions) / N
```

**The velocity chart**: story points on the vertical axis, one bar (or
paired bars — committed vs. completed) per version on the horizontal
axis. Its purpose is not decoration — it exists so `PROJECT_TIMELINE.md`
and `EPIC_SELECTION_CRITERIA.md`'s Feasibility numbers stop being pure
guesses after the first version: `remaining backlog story points ÷
measured average velocity = versions remaining`, replacing "how long
will this take" with an answer grounded in this team's own measured
throughput, not a fresh guess every time.

## Continuous improvement, one version at a time

Each version closes with: actual velocity recorded, any ticket that
slipped or was blocked reviewed for why (feeding back into
`SHARED/PROJECT_TIMELINE.md`'s slippage-reporting rule and into how the
next version's Design Council estimates are calibrated), and the next
version's backlog pulled from `BACKLOG` into `TO DO` only after that
review — improvement is a recorded input into planning the next
increment, not a vague aspiration restated every version.

## Relationship to existing files

- Does not replace `SHARED/PROJECT_TIMELINE.md` — that tracks
  dates/dependencies/critical path at the epic level; this tracks
  ticket-level flow and throughput underneath it. A ticket's `version`
  maps to rows in the timeline.
- Does not replace `SHARED/EPIC_SELECTION_CRITERIA.md`'s
  confidence/impact scoring — velocity data becomes an input to that
  scoring once at least one version's real data exists, not a
  replacement for it on the first version (no data yet to use).
- `AGENTS/Product-Owner/AGENT.md` creates the ticket at story-write
  time; `AGENTS/Orchestrator/AGENT.md` maintains the board/log state;
  the assigned Developer worker (Frontend/Backend/Mobile) moves its own
  ticket across columns and supplies the story-point estimate at
  ticket creation.
