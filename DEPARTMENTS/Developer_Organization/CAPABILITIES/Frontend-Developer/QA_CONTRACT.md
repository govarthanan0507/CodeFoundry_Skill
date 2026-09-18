# Frontend QA Contract — V1

## Purpose

Define the minimum evidence required before the Frontend Developer Worker can hand work back to CodeFoundry.

## Validation levels

### Level 1 — Smoke

Required for every implemented change:

- application starts
- affected route loads
- no blocking runtime error
- primary changed interaction works

### Level 2 — UI behavior

Required when the change affects interaction:

- happy path
- invalid input where applicable
- disabled state where applicable
- loading state where applicable
- error state where applicable
- success/confirmation state where applicable

### Level 3 — Responsive

Required when the change affects layout:

- desktop/large viewport
- tablet/intermediate viewport
- mobile/small viewport

Check overflow, wrapping, navigation, touch targets, fixed/sticky elements, and content hierarchy.

### Level 4 — Accessibility

Required for interactive UI:

- semantic controls
- keyboard navigation
- visible focus
- labels/name computation
- sensible heading hierarchy
- contrast concerns
- reduced-motion behavior where motion is used

### Level 5 — Regression

Required when shared components, navigation, design tokens, or cross-cutting styles change:

- affected existing flows
- adjacent pages/components
- shared interaction patterns

## Browser evidence

When Playwright CLI is available, capture the browser state needed to support the conclusion. Prefer snapshots for structural state and screenshots for visual evidence.

Record:

- URL/route
- viewport used
- action performed
- observed result
- evidence reference/path
- pass/fail/not-run

## Failure severity

`BLOCKER` — prevents the requested flow or makes validation impossible.

`CRITICAL` — severe user-facing defect or accessibility/runtime failure in the changed flow.

`MAJOR` — meaningful requirement, responsive, visual, or interaction defect.

`MINOR` — polish issue that does not materially prevent use.

The worker must fix in-scope blockers/critical/major issues before success, unless the issue requires another specialist or human decision.

## Final gate

```text
ALL REQUIRED CHECKS PASS
        ↓
EVIDENCE RECORDED
        ↓
NO HIDDEN BLOCKERS
        ↓
FRONTEND HANDOFF
```

A check marked `not-run` is never equivalent to `pass`.
