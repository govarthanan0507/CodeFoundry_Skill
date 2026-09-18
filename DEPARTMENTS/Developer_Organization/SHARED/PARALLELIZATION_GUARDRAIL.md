# Parallelization Guardrail — Before Multiple Developers Touch the Same Codebase

## The problem this prevents

Two Backend Developers, two Frontend Developers, or a Mobile team of more than one, each making their own judgment call about how to divide the work, will each invent their own patterns for the parts they touch first — state management, naming, error handling shape. By the time the pieces meet, reconciling those independent judgment calls costs more than the parallelism saved. This is the same failure the Design Council's role boundaries exist to prevent, one level down: it's not enough to say "go build it faster," the split itself has to be a decision someone owns.

## Who defines the split — not the developers themselves

The relevant Design Council Architect (System Architect for cross-cutting structure, or the domain-specific Architect — Frontend, Backend/API, or a future Mobile Architect) defines the split **before** any parallel work starts. Developers do not self-organize the division of labor on a shared foundation — that's an architecture decision, same boundary logic as everywhere else in this system: developers execute, they don't decide structure.

## The two-phase rule

```text
PHASE 1 — FOUNDATION (serial, one owner)
  Navigation/routing structure, state management pattern, shared
  component/module conventions, API contract shapes. This cannot be
  parallelized — two people inventing the shared foundation
  simultaneously is the exact failure this guardrail exists to stop.
        ↓
Architect defines the split line: which screens/endpoints/modules
are now independent enough to build without touching each other or
the foundation itself.
        ↓
PHASE 2 — PARALLEL (multiple owners, within defined lines)
  Each developer builds within their assigned, non-overlapping slice,
  against the Phase 1 foundation and the Phase 1 contracts — not
  inventing their own version of either.
        ↓
INTEGRATION CHECK (QA, not skipped because it was "just following the plan")
  Consistency across the parallel pieces is verified as its own step
  — shared foundation used correctly, no silent pattern drift between
  developers, contracts honored as specified.
```

## What "the split line" actually means in practice

The Architect's split output states, explicitly, for each unit of parallel work:
- what it owns (e.g. "Devices screen and its data fetching")
- what it must NOT touch (shared navigation, shared state store, another developer's assigned screen)
- which Phase 1 contract/pattern it builds against, so two developers reading the same foundation produce compatible work without needing to coordinate directly

A "go build faster with more people" request without this split defined is not actually faster — it's the same total work plus a reconciliation cost at the end, which is the trap the person asking almost always doesn't see coming until it's already happened.

## Applies to every developer-type worker, not just mobile

This guardrail is general — it activates whenever more than one instance of the same Developer worker (Frontend, Backend, or Mobile once built) is assigned to the same project simultaneously. It is not mobile-specific; mobile is just the case that surfaced the need for it.

## Cross-phase concurrency — a different case from same-role parallelism

A separate pattern from everything above, and worth stating as a general principle rather than a single example: **any number of phases/epics can advance concurrently — Phase 1 in Development, Phase 2 starting Development the moment its own gate clears, Phase 3 starting Discovery in parallel with both — as a continuous pipeline, not a fixed pair.** The risk this creates doesn't change with the number of phases running at once: it's always "a later phase's discovery invalidates work an earlier phase already built," just multiplied by however many phases are concurrently in flight.

```text
For EVERY phase about to start while another phase is still active:
        ↓
Architect confirms explicitly: is this phase independent, at the
FOUNDATION level, from every other phase currently in flight — no
shared architecture, data model, or service boundary any of them
could still change?
        ↓
YES — genuinely independent of all currently-active phases
        ↓
    Starts immediately, runs concurrently, no coordination needed
        ↓
NO — shares foundation with at least one active phase
        ↓
    Starts only on the parts that are genuinely independent of
    that shared foundation; anything touching it waits for the
    conflicting phase to close its foundation-relevant decisions
```

This check runs **every time a new phase becomes eligible to start**, not once at project kickoff — a pipeline of many concurrent phases means many individual go/no-go decisions over time, not one upfront plan. The Orchestrator is the one asking the Architect this question each time, per its own routing responsibility in `AGENTS/Orchestrator/AGENT.md` — the phases don't decide for themselves whether it's safe to run alongside whatever else is currently active.

**Concretely, for a Frontend + Backend Development phase specifically:** the two subagents within one phase are always safe to run concurrently with each other (the standard, already-established contract-mediated split). The open question is only ever whether that whole Development phase is safe to run alongside whichever *other* phases are currently active — and that's re-checked per phase, per the general rule above, not assumed to still hold just because it held for an earlier pair.

If genuinely unsure at any point, the Orchestrator defaults to serial for that specific phase (it waits rather than starts), the same "default to the safer choice when ambiguous" rule used everywhere else in this system — pipelining is the default *goal*, not a default *assumption* that overrides a real foundation conflict.

## Relationship to Process Scaling and the Hard Constraints Registry

This guardrail only matters once a task is already Tier 2 or Tier 3 (see `PROCESS_SCALING.md`) and large enough that parallel developers are even being considered — a Tier 1 task by definition doesn't reach this scale. It doesn't replace either of those files; it's the next layer down, specific to the moment multiple builders of the same role are about to touch shared ground.
