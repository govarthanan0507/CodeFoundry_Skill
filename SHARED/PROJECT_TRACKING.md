# Project Tracking — GitHub Projects, not a custom board

## The rule

CodeFoundry does not build its own Kanban/Gantt UI. Per the same
"use what's already proven, don't reinvent it" principle this project
applies to code reuse (`SHARED/REUSE_AND_LICENSE_RULE.md`) and to
document format (`SHARED/PROJECT_FOLDER_STRUCTURE.md`'s "real `.docx`
files, not a custom web tool" rule) — task tracking uses **GitHub
Projects (the current version, sometimes called Projects v2)**, free on
both public and private repos, attached directly to the project's own
`dev_<project-name>` repo.

## What GitHub Projects already gives us for free

- **Board view** — To Do / In Progress / In Review / Done columns,
  drag-and-drop. This is the Kanban view.
- **Roadmap view** — items laid out against start/target date fields.
  This is the Gantt-equivalent view.
- **Table view** — every ticket as rows, filterable/sortable by any
  custom field.
- **Automation** — built-in workflows (e.g., move an item to "Done"
  when its linked PR merges, move to "In Review" when a PR opens).
- Items can be plain GitHub Issues from `dev_<project-name>` (and,
  where useful, linked issues from `test_<project-name>` for QA
  findings) — one project board can track issues across more than one
  repo.

None of this needs to be built. It needs to be **fed** — see below.

## What CodeFoundry provides — the mapping, not the UI

CodeFoundry's own ticket/log state already exists per
`SHARED/PROJECT_FOLDER_STRUCTURE.md` (`dev_<project-name>`'s own
ticket/log state) and `DEPARTMENTS/Developer_Organization/SHARED/
HANDOFF_TO_QA.md`'s ticket lifecycle. The only new responsibility is
keeping a GitHub Issue's status field in sync with that lifecycle:

```text
Ticket created (Design Council handoff → Developer_Organization)
        ↓ create a GitHub Issue in dev_<project-name>, status: Todo
Developer worker picks it up
        ↓ status: In Progress
Ticket reaches DONE (per HANDOFF_TO_QA.md)
        ↓ status: In Review  (handed to QA)
QA_Organization records a finding against it
        ↓ status: back to In Progress (linked as a fix ticket,
                   same as PROJECT_FOLDER_STRUCTURE.md's fix-ticket loop)
QA verdict clean (FIXED_VERIFIED / ACCEPTED_RISK / WONT_FIX)
        ↓ status: Done
```

Whichever agent/worker changes a ticket's state (per the existing
lifecycle documents) is responsible for updating the linked GitHub
Issue's status field to match, in the same action — this is a sync
step, not a new decision-making role. No agent should treat the GitHub
Project board itself as a source of truth; `dev_<project-name>`'s own
ticket/log state and `test_<project-name>`'s audit trail remain
authoritative, exactly as `PROJECT_FOLDER_STRUCTURE.md` already states
for documents. The board is a read view for humans, generated from
that state — never the other way around.

## What this does not replace

`office-inbox.html` and `office-docs.html` remain useful for what they
already do (quick reply, quick document-version browsing) — GitHub
Projects doesn't do document version history or an inbox. This is
purely the Kanban/Gantt/task-board piece, which no longer needs a
custom UI.
