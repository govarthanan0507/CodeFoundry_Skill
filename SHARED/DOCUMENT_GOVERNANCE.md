# Document Governance — V1 (Completed)

## Purpose

So there's never a "I said X, you built Y" dispute — the documents are the record, not anyone's memory of a conversation.

## Which documents exist, and where they actually live

Per `WORKER_SCOPE_REGISTRY.md`'s prior finding, this system doesn't produce four separate hand-written documents — it produces three real artifacts that map onto the traditional four:

- **BRD-equivalent** — the Pre-Planning decision package (`COUNCILS/Pre-Planning/DECISION_CONTRACT.md`'s output — four required templates plus the Synthesizer's verdict record)
- **PRD** — `requirements.md`, owned by the Product Owner, containing user stories and acceptance criteria per `AGENTS/Product-Owner/AGENT.md`'s hardened discipline. Epic-level content (the Pre-Planning verdict record, epic decomposition/selection reasoning) is owned by the Product Manager per `AGENTS/Product-Manager/AGENT.md` and referenced from `requirements.md`, not duplicated into it.
- **TRD** — the Design Council's design package (architecture, API contracts, data model)

Each of these is a real, versioned file — not a conceptual grouping.

## Versioning

Every one of the three documents above uses simple integer versioning: **v1, v2, v3...** A new version is created whenever a **material** change occurs — not every typo fix, but any change that could affect what someone downstream is building against (a new/removed user story, a changed acceptance criterion, an architecture decision reversed).

```text
requirements-v1.md   (original, signed off)
requirements-v2.md   (after a scope change, with a changelog note
                       at the top explaining what changed and why)
```

The prior version is never deleted or silently overwritten — it stays as a record, the same "supersede, don't overwrite" rule already established in `SHARED_STATE_MODEL.md` for immutable evidence.

## Sign-off

A document version is not authoritative until the human explicitly signs off on it — same rule as every gate in this system: **silence is never approval.** Sign-off is recorded directly in the document:

```text
STATUS: DRAFT | SIGNED OFF
SIGNED OFF BY: <name>
SIGNED OFF ON: <date>
VERSION: v2
SUPERSEDES: v1 (reason: <what changed>)
```

## Conflict resolution — the actual point of doing this

**When there's a dispute about what was actually agreed, the signed-off document version is authoritative — not anyone's recollection of a conversation, including mine.** If a conversation implied something that never made it into a signed-off `requirements.md`, it isn't a requirement — it's an unrecorded discussion, and the fix is to formally add it to the next version, not to treat it as already decided. This is the direct answer to your "so there won't be any mistakes stating I said something and you did something" concern — the document is the only thing either side can point to.

## Where this plugs into what already exists

- `AGENTS/Orchestrator/AGENT.md`'s Shared State Model responsibilities now include: a document only moves from mutable working state to "approved artifact" status when it has a recorded sign-off, not just when a role stops editing it.
- `HANDOFF_CONTRACT.md`'s `APPROVAL STATUS` field should reference the specific signed-off version a handoff was built against — e.g. `requirements-v2.md, signed off 2026-09-14` — so it's traceable which version of the contract any given piece of work actually corresponds to.
