# Inbound Handoff — Start Here

This organization does not start work on a ticket without these
already existing. It is the mirror of `QA_Organization`'s own
`HANDOFF_PACKAGE_TEMPLATE/00_START_HERE.md` — a controlled, complete
package, not an informal conversation carried forward.

## What must exist before a ticket may leave `TO DO`

| Artifact | Produced by | Where it's defined |
|---|---|---|
| The ticket itself | Product Owner | one per user story, `SHARED/AGILE_WORKFLOW.md` |
| `DISCOVERY.md` for this story, state CLEAR/CLEAR WITH OPEN ITEMS | Design Council (Discovery phase) | `DISCOVERY_PROTOCOL.md` + `templates/DISCOVERY_TEMPLATE.md` (Design Council's own repo/department) |
| `TRD.md` / `FRD.md` for the epic this story belongs to | Design Council | `COUNCIL.md` |

A ticket whose `DISCOVERY.md` is `BLOCKED`, or whose epic has no
`TRD.md`/`FRD.md` yet, stays in `TO DO`. This organization does not
infer a design decision on its own to unblock itself — that is
Design Council's authority, not this organization's, per
`CONSTITUTION.md` principle 4.

## What this organization does NOT require upfront

Unlike `QA_Organization`'s package (which needs adversarial data,
reference projects, and a full benchmark suite before a cycle starts),
this organization's inbound bar is narrower — it needs the design
decision, not the verification apparatus. Verification data
(test-data, adversarial-data) is QA's concern downstream, not a
prerequisite for Development to begin.
