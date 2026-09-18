# Frontend Developer Workflow — V1

## Entry condition

The orchestrator assigns a frontend task with:

- task ID
- objective
- approved requirements
- acceptance criteria
- dependencies
- repository/workspace
- applicable technical constraints
- required gate/approval evidence

## Phase 1 — Intake

1. Read the task.
2. Identify the user outcome.
3. Identify acceptance criteria.
4. Check upstream artifacts and approvals.
5. Report `BLOCKED` / `WAITING_FOR_HUMAN` if required inputs are missing.

## Phase 2 — Reconnaissance

Inspect the project before editing. Determine framework, scripts, routes, component conventions, styles, tokens, tests, and relevant existing screens.

For a redesign, audit the existing implementation before replacing it.

## Phase 3 — Design

1. **Consult `UX_PRINCIPLES.md` and `DESIGN_CONTRACT.md` FIRST, before producing any visual direction — not only in the critic pass.** Specifically check: does the obvious/default layout for this product category match an existing named product too closely (a streaming app defaulting to Netflix's row-carousel, a dashboard defaulting to a specific competitor's chrome)? If so, that's the moment to choose a different structural direction, not something to catch after building it.
2. Infer the UX hierarchy.
3. Determine the appropriate visual direction, informed by step 1's check.
4. Read existing `DESIGN.md` if present.
5. Create/update `DESIGN.md` when persistent design rules are needed.
6. Record material design decisions that affect implementation.

Do not allow aesthetic preference to override approved product requirements.

## Phase 4 — Plan

Create a small implementation plan:

```text
TASK
  ├─ affected routes
  ├─ affected components
  ├─ state changes
  ├─ API/data dependencies
  ├─ responsive implications
  └─ verification plan
```

## Phase 5 — Build

Implement the task using existing project conventions where possible.

Keep changes focused and traceable.

## Phase 6 — Run

Start the application using repository-defined commands.

If startup fails:

- capture the failure
- determine whether it is caused by the change
- fix if in scope
- otherwise return a blocker with evidence

## Phase 7 — Browser validation

When Playwright CLI is available:

1. open the running application
2. snapshot the initial state
3. execute the primary user flow
4. verify important controls
5. inspect resulting state
6. test relevant error/empty/loading states
7. capture screenshots where visual evidence matters
8. repeat at representative viewport sizes

## Phase 8 — Critic pass

Review the result against:

- requirements
- DESIGN.md
- visual hierarchy
- spacing/typography
- responsive behavior
- accessibility
- interaction behavior
- runtime health
- regression risk
- advisory UX principles from `UX_PRINCIPLES.md`, selecting only materially relevant heuristics

For UX-principle findings, use observation -> relevant principle -> user impact -> recommendation -> evidence. Most heuristics inform critique but are not hard gates — **the exception is a layout that closely copies an existing named product's structural chrome (not just its color palette): that finding is always classified at least `MAJOR`, never `OBSERVATION`, and blocks handoff until addressed.** A palette or component-level similarity is advisory; a structural copy (same nav placement, same content hierarchy, same signature layout) is not.

Classify findings as `BLOCKER`, `CRITICAL`, `MAJOR`, `MINOR`, or `OBSERVATION`.

## Phase 9 — Remediation loop

For every in-scope `BLOCKER`, `CRITICAL`, or `MAJOR` finding:

```text
FINDING
  ↓
FIX
  ↓
RE-RUN AFFECTED CHECK
  ↓
CONFIRM
```

Do not simply lower severity to reach success.

## Phase 10 — Handoff

Return:

- status
- implemented changes
- design changes
- tests/checks performed
- evidence
- remaining risks
- blockers
- next action

## Re-entry

If new evidence materially changes the requirement or design contract, stop affected downstream work, identify impacted artifacts, and return to the appropriate phase.

A changed `DESIGN.md` can require visual/regression revalidation.

A changed API contract can require interaction/state revalidation.

A changed acceptance criterion can require a new verification pass.
