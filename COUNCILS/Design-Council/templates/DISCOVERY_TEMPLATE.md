# Discovery Record — Template (`DISCOVERY.md`)

Produced by: the roles consulted under `DISCOVERY_PROTOCOL.md` for one
specific story. One `DISCOVERY.md` per story (ticket ID in the
filename or header — never merged across stories, same reasoning as
"one ticket per story" in `DEPARTMENTS/Developer_Organization/SHARED/AGILE_WORKFLOW.md`). This is the
handoff artifact: what the Design Council debate machinery
(`DEBATE_PROTOCOL.md`) and the assigned Developer worker both read,
so it has to be complete on its own — nobody should need to re-ask the
user something already answered here.

## Header (always filled)

- Story / ticket ID (`DEPARTMENTS/Developer_Organization/SHARED/AGILE_WORKFLOW.md` ticket, matches
  `requirements.md`)
- Epic reference (traces up to the Product Manager's epic)
- Tier: 1 | 2 | 3 (per `SHARED/PROCESS_SCALING.md`)
- Roles consulted: <list, or "Tier 1 — Developer worker only">
- Date

## Phase 1 — Intake (verbatim, not summarized down)

```text
RAW INPUT
  [Everything the user gave, in the order given — requirements,
   inspirations, reference links/documents, half-formed ideas
   included. This section is a record of what was SAID, not a
   filtered version of it — filtering happens in Phase 2 below, never
   here. Paraphrase only for length where the original wording adds
   nothing; never paraphrase away a stated preference.]

ENDED BY
  User declared done (not a role's judgment call — see
  DISCOVERY_PROTOCOL.md's Phase 1 exit rule)
```

## Phase 2 — Verification

```text
ACCEPTED AS-IS
  [Each Phase 1 item that passed feasibility unchanged — list, not
   prose, so it's scannable against Phase 1's raw input.]

PUSHED BACK / MODIFIED
  [Item : why it couldn't proceed as given : what was proposed
   instead, in the polite-but-plain shape DISCOVERY_PROTOCOL.md
   requires — "X needs paid infrastructure we're not using; Y gets
   most of the same result for free" style, not a bare rejection.]

OPEN ITEMS
  [Genuinely unresolved after Phase 2 — carried forward explicitly,
   never silently dropped. Empty is stated as "none," not omitted.]

USER CONFIRMATION
  [Confirmed the final accepted/pushed-back/open-items picture,
   per DISCOVERY_PROTOCOL.md's Phase 2 closing rule — this record is
   not finalized without it. Date/method of confirmation noted.]
```

## Evidence discipline (both phases)

```text
FACTS CONFIRMED
ASSUMPTIONS MADE
   [never silently promoted to fact — AGENTS/Ideation/AGENT.md's rule,
    applied here across both phases]
UNKNOWNS REMAINING
```

## Design decision for this story

```text
DECIDED BY
  [role(s) actually consulted — Tier 1: the Developer worker's own
   call; Tier 2/3: challenge → response → synthesis among the roles
   present, same shape as DEBATE_PROTOCOL.md, scoped to just this
   story]

DECISION
  [what this story's "how" is — the actual thing the Developer worker
   builds against]

REJECTED ALTERNATIVES
  [if any were seriously considered — same "preserve the rejected
   alternative" discipline used everywhere else in this system]
```

## Final state (required — no ticket enters IN PROGRESS without this)

```text
STATE: CLEAR | CLEAR WITH OPEN ITEMS | BLOCKED
```

A `DISCOVERY.md` missing any section above (an empty Phase 1, a Phase 2
with no `USER CONFIRMATION`, a `STATE` left unset) is incomplete — per
`DEPARTMENTS/Developer_Organization/SHARED/AGILE_WORKFLOW.md`'s Kanban gate, the ticket stays in `TO DO`,
it does not enter `IN PROGRESS` on a partial record.
