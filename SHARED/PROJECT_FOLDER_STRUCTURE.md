# Project Folder Structure — V1 (Completed)

## The rule, stated plainly

**Every project gets its own new folder. Projects never share a folder or repository.** No exceptions, no "just this once for a related project" — a new idea, once it clears Pre-Planning, gets `projects/<new-project-name>/` created fresh, not appended into an existing project's space.

Before Pre-Planning clears, none of this exists yet — see
`SHARED/INTAKE_REPOSITORY.md` for where Ideation/Ingestion/Pre-Planning
output lives instead, and why it is never written into a target
project's own repo before a GO decision.

## Why this matters

Mixing two projects' documents in one folder is exactly how a version-history tool like `office-docs.html` (or a real Confluence space) becomes unreliable — you can no longer tell which `requirements-v2.docx` belongs to which product just by looking. Isolation at the folder level is what makes every other piece (versioning, handoff logs, sign-off tracking) actually trustworthy.

## The structure, per project

```text
projects/<project-name>/
  documents/
    requirements-v1.docx      (PRD — versioned per DOCUMENT_GOVERNANCE.md)
    requirements-v2.docx
    design-v1.docx            (TRD — Design Council's package)
    preplanning-v1.docx       (BRD-equivalent — Pre-Planning's decision package)
  handoffs/
    2026-09-14-ideation-to-preplanning.md
    2026-09-14-preplanning-to-planning.md
    ...one file per handoff, named by date + stage transition,
       each following HANDOFF_CONTRACT.md's schema exactly
  state/
    project-state.md          (the durable state contract, unchanged
                                from earlier in this session)
```

## Documents are real files (.docx), not custom web tools

Per your correction: PRD, BRD, and TRD are real Microsoft Word documents, generated with the `docx` skill, not rendered inside a custom HTML page. `requirements-v1.docx` for Baseflix's Remote Access epic is the first real example, built and placed in `projects/baseflix/documents/`.

## The handoffs folder — a real, permanent log

Every stage transition gets its own file in `handoffs/`, using `HANDOFF_CONTRACT.md`'s full schema — not a summary, the actual document. This is the literal, permanent record of everything that happened on a project, in order, readable chronologically by filename. It answers "what happened and when" the same way `DOCUMENT_GOVERNANCE.md`'s signed-off documents answer "what was decided" — together they're the two-document handoff you asked about earlier: one human-readable narrative record (the handoffs folder, read in order) and one structured decision record (the versioned documents folder).

## Two more folders, once work reaches build/verify — never shared, never crossed

The `projects/<project-name>/` folder above holds the shared
documents (Ideation, Pre-Planning, Design Council's TRD/FRD/
DISCOVERY.md, Product Owner's requirements.md) — everything upstream
of actual building. Once a ticket is ready to build, two more folders
are created, siblings to each other, each owned by exactly one
department:

```text
dev_<project-name>/    — Developer_Organization's own workspace:
                          code, its own ticket/log state, build
                          artifacts. Created and written to only by
                          Developer_Organization.

test_<project-name>/   — QA_Organization's own workspace: its full
                          audit trail, evidence, findings — the same
                          content QA_Organization's own LIFECYCLE.md
                          already governs, just living in this named
                          folder for this project.
```

**Neither folder is ever copied into or touched by the other
department.** This is not a new rule — it is the same three-repo
boundary `QA_Organization/LIFECYCLE.md` already states (the developer
never writes to the QA repo, QA never writes to the developer repo),
expressed here as a filesystem-level rule for the folder-based version
of that same boundary. Development reads `test_<project-name>/`'s
findings; it does not open or modify anything else in that folder. QA
reads what it needs from `dev_<project-name>/` to test it; it does not
edit code there.

## The iterative loop, named concretely

Per `DEPARTMENTS/Developer_Organization/SHARED/HANDOFF_TO_QA.md`'s
loop: a version's work in `dev_<project-name>/` gets handed to
`test_<project-name>/` once all its tickets are `DONE`. Findings
QA_Organization records in `test_<project-name>/` route back as fix
tickets in `dev_<project-name>/`. This repeats until QA_Organization's
verdict is clean (every finding `FIXED_VERIFIED` / `ACCEPTED_RISK` /
`WONT_FIX`) — at which point, and not before, the Deployment Engineer
(`AGENTS/Deployment-Engineer/AGENT.md`) takes over.

## Deployment — three separate GitHub repos, one sanctioned download point

```text
dev_<project-name>   → pushed to its own GitHub repo (dev_<project-name>)
                        — Development's real history, as-is.
test_<project-name>  → pushed to its own GitHub repo (test_<project-name>)
                        — QA's full audit trail, as-is.
prod_<project-name>  → created ONLY once QA_Organization's verdict is
                        clean. Contains the verified build and what
                        actually satisfied every case — not the raw
                        dev history, not QA's working files. This is
                        the ONLY repo anyone downloads from.
```

**Enforcement, stated honestly:** a rule saying "only download from
`prod_<project-name>`" is not self-enforcing on its own — nothing
stops someone with access from cloning `dev_<project-name>` or
`test_<project-name>` directly. The actual mechanism is access
control, not a polite request: `dev_<project-name>` and
`test_<project-name>` are private/internal repos by default;
`prod_<project-name>` is the one repo made available for distribution.
Anyone who is separately given access to the dev or test repos and
downloads from there anyway is doing so outside this system's
guarantee — that content hasn't cleared QA, may not build, and is
explicitly at their own risk, same as pulling from any other
unreleased branch.

## What changes about the tools already built

`office-inbox.html` and `office-docs.html` remain useful as optional local utilities (quick reply-without-opening-Claude-Code, quick version browsing) — but they are not the source of truth. The real source of truth is this folder structure on disk: real `.docx` files, a real `handoffs/` log, one folder per project, never shared.

## Task tracking — GitHub Projects, not a custom board

The ticket/log state inside `dev_<project-name>` is surfaced to humans
as a Kanban/Gantt board via **GitHub Projects**, attached to the
`dev_<project-name>` repo once it exists — not a custom-built UI. See
`SHARED/PROJECT_TRACKING.md` for the full mapping from ticket lifecycle
state to GitHub Issue status. The board is a generated view; this
folder structure remains the source of truth.
