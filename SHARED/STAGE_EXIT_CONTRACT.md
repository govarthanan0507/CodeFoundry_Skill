# Stage Exit Contract — Universal Template (V1, Completed)

## The problem this solves

Every stage in CodeFoundry has principles for *how* to behave, but none had an executable answer to *when it's done*. "Ask the highest-value question until ambiguity is sufficiently low" has no terminal condition — a capable model can always find one more question worth asking. This is optimization without a stopping condition, discovered through direct dogfooding of the Ideation stage, and the fix generalizes to every stage, not just that one.

## The universal shape

Every stage — not just Ideation — is now defined as:

```text
Stage → Exit Criteria → Artifact → Gate Decision → Handoff → Next Stage
```

Not merely "Stage → next stage." The missing middle is what this file adds, everywhere.

## The rule, stated once, applying everywhere

**A stage's exit criteria are artifact-based, never question-count or checklist-based.** Not "ask at least N questions" or "cover these M topics." Instead: *can the current understanding be represented coherently enough that the next stage can do its job without rediscovering what this stage already established?* That is the only test. Checklists recreate the exact form-like behavior already banned in `AGENTS/Ideation/AGENT.md`'s Section 5 — a stage exit gate must not become a new checklist wearing the old one's clothes.

## The three-outcome gate decision — reused everywhere, not reinvented per stage

```text
CLEAR
  Enough is understood/decided. Transition immediately.

CLEAR WITH OPEN ITEMS
  Enough to transition, with specific unresolved items explicitly
  carried into the next stage — not silently dropped.

BLOCKED
  Something fundamental is missing or contradictory. Proceeding
  would build on a false understanding. Do not transition.
```

This is the same three-state pattern already used in Ideation's completion states and echoed in the Design Council's three debate outcomes (clean resolution / deadlock / infeasible premise) — not a new invention, a generalization of a pattern that was already working in two places independently.

## The critical stopping rule

**No further questioning or investigation is permitted within a stage unless an unresolved item could materially change the identity, scope, feasibility direction, or next-stage decision.** "There's more we could learn" is not the same as "we aren't ready to proceed" — conflating the two is exactly what produces unbounded stages. A stage that keeps digging past this point is not being thorough, it's failing its own exit contract.

## Per-stage instantiation

Each stage defines its own **Exit Criteria fields** (what the artifact must contain to be coherent) while using this same gate-decision structure and stopping rule. Ideation's concrete instantiation is now in `AGENTS/Ideation/AGENT.md`, Section "Ideation Exit Gate" — built as the first real application of this template, not a separate invention. Pre-Planning, Design Council, and Development each get their own field list, defined when that stage's own version is built — the *shape* is universal now; the *content* per stage is not identical, since a Pre-Planning artifact and an Ideation artifact don't need the same fields to be coherent.

## Why this is a stage-exit fix, not a re-litigation of stage boundaries

This does not change what any stage is allowed to decide (Ideation still can't choose a database; the hard boundary rules are untouched). It only changes *when* a stage is allowed to stop working and hand off — the missing piece was never about scope, it was about termination.
