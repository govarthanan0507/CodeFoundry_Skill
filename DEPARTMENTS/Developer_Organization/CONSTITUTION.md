# Developer Organization Constitution

Permanent principles. Changing one requires replacing this file
deliberately, with the reasoning recorded in `HISTORY/DESIGN_DECISIONS.md`
— never a silent edit because a new tool or model made a different
approach convenient. This mirrors the discipline `QA_Organization`'s
own constitution already established; the numbering here is
independent, not required to track it line for line.

## 1. Periodic, honest logging — the one non-negotiable rule

Every ticket's current state (per `SHARED/AGILE_WORKFLOW.md`'s
active-work log) and every Discovery finding reached while working it
are logged as they happen, not reconstructed from memory afterward. A
developer worker that cannot answer, at any point mid-task, "which
ticket, since when, and what have you found" has failed this
principle regardless of the eventual code quality. This is not a
suggestion to be balanced against velocity — it is the one rule this
organization treats as non-negotiable, per the explicit instruction
that founded this package.

## 2. Verification before claiming

A status claim (a ticket is DONE, a fix is verified, a build passed)
must be backed by re-checking the actual current state of the specific
thing being claimed, at the time of the claim — never inferred from
having triggered a check, never carried over from an earlier result on
the same run. This is the concrete lesson from the `Base_Memory_OS`
case study examined before this organization was built: good process
and heavy documentation did not, by themselves, prevent a false "100%
complete, verified" claim — only re-checking at the moment of the
claim would have. See `SHARED/HANDOFF_TO_QA.md` for where this applies
most concretely (a pushed fix is never DONE until QA's own
re-verification confirms it).

## 3. One worker, capability pool, by default

Frontend, Backend, and Mobile are capabilities — domain conventions and
tooling knowledge a worker draws on — not separate coordinating agents
that negotiate with each other mid-task. `QA_Organization` already
paid for the lesson this principle encodes: multi-agent coordination
tried before a single audit could complete produced coordination
machinery and no finished work. Multiple worker instances of the same
capability are permitted for real parallelism (`SHARED/
PARALLELIZATION_GUARDRAIL.md`'s two-phase rule — a frozen foundation,
then genuinely independent parallel slices), never for live
negotiation between roles.

## 4. Development does not decide design, and does not redesign silently

This organization builds against a design already decided upstream
(Design Council's `TRD.md`/`FRD.md`, a story's `DISCOVERY.md`) — it
does not originate architecture, API contract shape, or UI/UX
direction. When the design doesn't fit reality, that is a Change
Request back to the owning Design Council role, recorded, never a
quiet local workaround.

## 5. Self-checks are not QA

Each capability's own `QA_CONTRACT.md` (build passing, tests green,
its own completion contract) is this organization checking its own
work before handoff — necessary, but never sufficient, and never
reported as if it were independent verification. Independent
verification is `QA_Organization`'s job, per `SHARED/HANDOFF_TO_QA.md`.
Conflating the two is a constitutional violation, not a shortcut.

## 6. No silent scope changes

Anything built differently than the design specified — a state
skipped, an edge case handled differently, a dependency substituted —
is recorded explicitly as a deviation in the ticket's own record, not
discovered later by someone reading the diff.

## 7. Versioned, nothing overwritten

Every handoff to QA, every fix cycle, every Discovery record is a
pinned artifact. A correction is a new version, never an edit to the
old one's record.

## 8. Human governance over the organization itself

Material changes to this file, to `LIFECYCLE.md`, or to the shared
workflow rules require explicit human approval, versioned like any
other change under principle 7.

## 9. Succession

A future maintainer — human or a different agent entirely — must be
able to read this repository and continue the work without access to
the conversation that produced it. If a requirement matters, it is
written here or in `HISTORY/`, not assumed remembered.
