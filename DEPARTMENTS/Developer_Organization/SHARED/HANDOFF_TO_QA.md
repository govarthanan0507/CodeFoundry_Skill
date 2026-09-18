# Development Organization → QA — Handoff and Iterative Loop — V1

## What "Development Organization" is — not a new thing to build

The Frontend Developer, Backend Developer, and Mobile Developer
workers (`CAPABILITIES/`), each already hardened with their own CAPABILITY.md,
workflow, and self-verification `QA_CONTRACT.md`, collectively *are*
the Development Organization inside CodeFoundry. This file does not
create a fourth worker or a coordinating layer above them — it defines
the one thing that didn't exist yet: what happens at the edge, where
their combined output leaves CodeFoundry and meets independent QA, and
what happens when QA sends something back.

## Who QA actually is here — reuse, don't reinvent

CodeFoundry's own `WORKER_SCOPE_REGISTRY.md` lists "QA Worker" as
`SCOPED` — boundaries named, nothing built. Building a second, weaker
QA inside this organization would duplicate `QA_Organization` — a
real, separate, evidence-driven QA system with its own constitution,
engine, and handoff contract. So: **the QA this file hands off to is
`QA_Organization`, not a CodeFoundry-native QA worker.**
`QA_Organization`'s own `LIFECYCLE.md` three-repo model already
assumed *some* Developer Repo without naming one — this organization
is that repo.

For this testing phase, `QA_Organization` is co-located as a sibling
department (`DEPARTMENTS/QA_Organization/` from CodeFoundry's root, or
however this package is mounted elsewhere) purely so an integrated,
two-repo-shaped flow can be exercised in one place before the two are
actually split into separate repositories, per this organization's own
`README.md`. Co-location does not change the governance boundary:
this organization still never writes into `QA_Organization`'s own
files (that repo's entire audit trail belongs to QA, per its
Constitution and three-repo rule) — it only ever reads the findings QA
produces.

## When the handoff happens — per version, not per ticket

Per `SHARED/AGILE_WORKFLOW.md`'s versioning, a handoff happens once a
version's committed tickets have all reached `DONE` (each with its
`verification_evidence` filled per that file's rule) — not per
individual ticket, which would make QA re-run its full stage sequence
constantly for no reason, and not for the whole product life, which
would defer independent verification indefinitely.

## The handoff package — QA_Organization's own template, filled from what CodeFoundry already tracked

CodeFoundry does not invent a new package shape. It fills
`QA_Organization/HANDOFF_PACKAGE_TEMPLATE/`'s existing contract, from
artifacts this system already produces — nothing here is new data
collection, only assembly:

```text
01_QA_CONTRACT.md   (scope, authorization boundaries)
  Filled by: the human product owner / Pre-Planning's verdict record
  and TRD.md's Hard Constraints — cycle type is FULL_AUDIT for a new
  version, FIX_VERIFICATION when this handoff is answering findings
  from a prior cycle (see the loop, below).

02_EXECUTION_PROTOCOL.md   (build/run instructions, environment)
  Filled by: the Backend/Frontend Developer workers' own build
  commands and environment requirements, plus TRD.md's observability
  section (logging/metrics/tracing already decided at design time).

product-under-test/
  The exact commit for this version — per SHARED/PROJECT_TIMELINE.md's
  tracked FINISH date for the version's last ticket.

test-data/, adversarial-data/
  Provided by the human per QA_Organization's own authorization rule
  (Constitution §8) — CodeFoundry does not generate adversarial data
  itself; this is explicitly outside Development's authority.
```

Assembling this package is the Orchestrator's job (mechanics — reading
already-tracked state into a fixed template), not a new judgment call
by any Developer worker.

## The iterative loop — QA's findings, routed back, until cleared

`QA_Organization`'s `HANDOFF_PACKAGE_TEMPLATE/schemas/FINDING.schema.json` already has the state
machine this needs (`OPEN → FIXED_VERIFIED | ACCEPTED_RISK |
WONT_FIX`), and `LIFECYCLE.md` already defines the fix-verification
cycle (`V{n}-FIX-{m}`) as a real re-entry, not a full re-audit. This
file wires CodeFoundry's side of that same loop:

```text
QA_Organization returns findings (FINDING.schema.json records,
status: OPEN)
        ↓
Orchestrator reads each finding's `component` field (a real file/
module path, per that schema) and routes it to the owning Developer
worker — Frontend, Backend, or Mobile — the same way a Development
change request already routes to a specific Design Council role
(COUNCIL.md's post-handoff accountability, same shape one level over)
        ↓
A ticket is opened for the fix (per SHARED/AGILE_WORKFLOW.md — one
ticket per finding, same "one ticket per unit of work" discipline
already used for stories), tagged with the finding_id it answers
        ↓
The assigned worker fixes it, through the same Kanban/Discovery gates
as any other ticket — a fix is not exempt from Discovery if the fix
itself requires a design-level decision (e.g. the root cause was an
architecture gap, not a simple bug)
        ↓
CodeFoundry hands back a FIX_VERIFICATION package (01_QA_CONTRACT.md's
cycle_type set accordingly, naming which prior cycle and which
findings this targets — per QA_Organization/LIFECYCLE.md's own rule
for what a fix-verification cycle requires)
        ↓
QA_Organization re-enters at Stage 5/6/7 (targeted retest), not
Stages 0-4 — per its own LIFECYCLE.md, this file does not change that
        ↓
Finding's status becomes FIXED_VERIFIED (QA confirms the fix), or the
finding surfaces something the original scope didn't anticipate, which
QA_Organization's own rule escalates to a full audit rather than
stretching the fix cycle — CodeFoundry does not decide that escalation,
QA does, per its own Constitution
        ↓
Repeat until every OPEN finding reaches FIXED_VERIFIED, or is
explicitly recorded ACCEPTED_RISK (a human decision, never CodeFoundry's
or QA's own call — QA_Organization/LIFECYCLE.md's existing rule) or
WONT_FIX (recorded with reasoning, not silently dropped)
```

## What CodeFoundry never does in this loop

- Never marks a ticket `DONE` because a fix was pushed — only once
  QA_Organization's re-verification actually confirms it
  (`FIXED_VERIFIED`). A pushed fix with no confirmed re-verification is
  the same "reported done without checking" failure this whole system
  already learned from (the Base_Memory_OS case study's lesson,
  generalized here).
- Never silently redesigns around a finding whose root cause is a
  Design Council decision — that routes as a Change Request per
  `COUNCIL.md`, same as any other post-handoff discovery.
- Never decides the release/ship call itself. Per
  `QA_Organization/CONSTITUTION.md` §9 and `LIFECYCLE.md`, QA reports a
  verdict; a human decides. CodeFoundry's role ends at "every finding
  is FIXED_VERIFIED / ACCEPTED_RISK / WONT_FIX, verdict delivered" — it
  does not promote itself past that gate.

## After QA clears — the next team

Once QA_Organization issues its verdict and findings are resolved, the
product moves to `AGENTS/Deployment-Engineer/AGENT.md` — the built
`DevOps / Release Worker` (`SHARED/WORKER_SCOPE_REGISTRY.md`'s entry
5) — which pushes `dev_<project>`/`test_<project>` and, once verified,
`prod_<project>`, per `SHARED/PROJECT_FOLDER_STRUCTURE.md`'s
deployment section.
