# Sprint Ceremonies — Review, Retrospective, Next-Cycle Planning — V1

## A naming correction, made explicit rather than silently applied

What you described as the "retrospective" — reviewing whether the
user's requested changes are feasible and whether they enter the next
sprint — is, in standard Scrum terms, actually **Sprint Planning /
Backlog Refinement**, not a Retrospective. A real Retrospective looks
**inward** (team and process — what went well, what didn't, action
items to work better) and has **no external stakeholders in the
room**. What you're describing — demoing to the user, taking feedback,
deciding what's feasible for next time — is the **Sprint Review**,
plus the **Planning** step that follows it. This file builds all
three, correctly named, because conflating Review and Retrospective is
a common real-world mistake this system shouldn't repeat just because
it sounded like one ceremony.

## Trigger — as soon as QA clears it, not after the prod push

The trigger is `QA_Organization`'s verdict going clean on
`test_<project-name>` (every finding `FIXED_VERIFIED`/`ACCEPTED_RISK`/
`WONT_FIX`, per `DEPARTMENTS/Developer_Organization/SHARED/
HANDOFF_TO_QA.md`) — the same condition that gates
`AGENTS/Deployment-Engineer/AGENT.md`'s entry, not a step after that
role has already pushed to `prod_<project-name>`. Sprint Review
demoes the verified build from `test_<project-name>`/`dev_<project-name>`
directly — the user reacts to what QA actually confirmed works, before
it's already live, so their feedback can still shape whether or how
it ships, not arrive after the fact. `EXPECTED NEXT ACTION` on QA's
own clean verdict is this ceremony sequence; Deployment Engineer's
`prod_<project-name>` push proceeds separately, gated on its own
entry condition (the same clean verdict) and the human release-
readiness gate — it does not wait on Review to finish, and Review does
not wait on it either. They run off the same trigger, not one after
the other.

## 1. Sprint Review — outward-facing, with the actual user in the room

```text
ATTENDEES: the human user, Product Manager, Product Owner, a Design
           Council representative (the Architect, or whichever role's
           domain the sprint's work mostly touched), the Developer
           worker(s) who built it.

PURPOSE:   Demo what was actually implemented this sprint — the real
           QA-verified build (per QA_Organization's clean verdict on
           `test_<project-name>`), not a description of it and not
           the already-live prod version. The user reviews it and
           reacts while their feedback can still shape the release,
           not after it's already shipped.

OUTCOME A: Satisfactory. Recorded as such — this is a real, positive
           disposition, not silently assumed because nobody objected
           (same "silence is never approval" rule used everywhere
           else in this system — satisfaction must be stated, not
           inferred from an uneventful meeting).

OUTCOME B: Not satisfactory, or the user requests a change/addition.
           Captured by the Product Owner (backlog-detail is already
           that role's job) as a candidate item — not vague notes, the
           same user-story discipline `AGENTS/Product-Owner/AGENT.md`
           already requires (who benefits, what changes, how you'd
           know it's done) — even for a rough request. This does NOT
           go straight into the next sprint's backlog; see Planning,
           below.

LOGGED BY: the Orchestrator, mechanically (`AGENTS/Orchestrator/
           AGENT.md`'s existing periodic-logging responsibility) —
           the meeting record itself, timestamped, per
           `DEPARTMENTS/Developer_Organization/CONSTITUTION.md`
           principle 1. This is the meeting's own artifact, not
           reconstructed afterward from memory.
```

## 2. Sprint Retrospective — inward-facing, team only, about process

```text
ATTENDEES: Product Manager, Product Owner, Design Council roles
           actually involved this sprint, the Developer worker(s) —
           NOT the human user, per the standard Scrum distinction
           above. This is the team looking at itself, not the product.

PURPOSE:   What went well, what didn't, in HOW the sprint ran — not
           what was built, how it was built. Concretely, this system
           already has real data to reflect on rather than vibes:
             - Did any ticket go AT RISK or SLIPPED
               (SHARED/PROJECT_TIMELINE.md)? Why?
             - Did velocity (SHARED/AGILE_WORKFLOW.md) match what was
               committed, or diverge, and why?
             - Did a Discovery record repeatedly need re-opening, or
               a Design Council role get repeated change requests
               (a signal the design was under-baked, per
               COUNCIL.md's own existing rule) — is that a pattern
               worth fixing in the process itself?

OUTCOME:   Action items — specific, owned, checked at the next
           Retrospective (did we actually do it), not a list that
           gets discussed once and forgotten. No backlog decision is
           made here — that would blur this back into Review/Planning,
           the exact conflation this file exists to avoid.

LOGGED BY: the Orchestrator, same as Review.
```

## 3. Next-cycle Planning — feasibility and backlog decision for what Review surfaced

```text
INPUT:     Sprint Review's captured candidate items (Outcome B, above)
           — not the Retrospective's action items, which are process
           fixes, not product features.

PROCESS:   Reuses SHARED/EPIC_SELECTION_CRITERIA.md's existing
           seven-step process exactly — market check, necessity,
           constraint fit, feasibility (Design Council's domain,
           consulting TECH_REFERENCE_LIBRARY.md same as any other
           epic), dependency, confidence/impact, MoSCoW label. A
           user's post-Review request is not treated as automatically
           urgent just because it's fresh — it goes through the same
           selection discipline as anything else competing for the
           next sprint, not a side channel that skips it.

OUTCOME:   The item becomes a labeled epic candidate (MUST/SHOULD/
           COULD/WON'T HAVE this release) in the normal backlog, per
           the existing process — or, if it's actually just a story
           within an existing epic, the Product Owner adds it there
           directly, same as any other story.

DECIDED BY: Product Manager (epic-level, per AGENTS/Product-Manager/
           AGENT.md's existing scope) with Design Council input on
           feasibility where the request has real technical
           uncertainty — same relationship these roles already have
           for any other epic, nothing new invented here.
```

## Relationship to existing files

- Does not replace `SHARED/EPIC_SELECTION_CRITERIA.md` — Planning
  above is that process, applied to Review's output specifically, not
  a competing selection mechanism.
- Does not replace `SHARED/PROJECT_TIMELINE.md` or
  `DEPARTMENTS/Developer_Organization/SHARED/AGILE_WORKFLOW.md` — the
  Retrospective consumes their data as real evidence, it doesn't
  duplicate what they already track.
- Feeds `AGENTS/Deployment-Engineer/AGENT.md`'s own handoff record —
  a `prod_<project-name>` push's `EXPECTED NEXT ACTION` is this
  ceremony sequence, not left implicit.
