# Epic Selection Criteria — V1 (Completed)

## Purpose

Once the Product Manager has decomposed an idea into epics (`AGENTS/Product-Manager/AGENT.md`'s epic decomposition discipline), not all of them belong in V1. This is the criteria — applied in order, not a checklist scored all at once — for which epics make the cut, and the record format that shows *why*, so the reasoning survives past the conversation it happened in.

## The process, in the order it actually runs

```text
STEP 1 — Market check first (the standing motto, checked before anything else)
   For each epic: is this already solved, well, by something tested
   and proven in the market?
        ↓
   YES, solved and tested → do not build this epic from scratch.
   Either adopt the existing solution directly (integrate it), or
   mark the epic "buy, not build" and remove it from the V1 build
   list entirely. This reuses Pre-Planning's Market/Research role
   and, where relevant, Repo Analyzer for OSS candidates — don't
   re-run research that stage already did.
        ↓
   NO, or solved poorly / doesn't fit constraints → continue to Step 2.

STEP 2 — Necessity check
   Does this epic serve the core problem/outcome Ideation captured?
   An epic that's interesting but doesn't serve the stated outcome
   is a candidate for deferral, not automatic inclusion just because
   someone thought of it.

STEP 3 — Constraint check
   Does this epic fit inside HARD_CONSTRAINTS.md as currently stated
   (budget, especially)? An epic that requires paid infrastructure
   at zero budget is deferred until that constraint changes, not
   built anyway.

STEP 4 — Feasibility check
   Reuses Pre-Planning's Feasibility & Cost Assessor findings for
   this specific epic, not a fresh assessment — is it actually
   buildable at the skill/time level available right now?

STEP 5 — Dependency check
   Does another must-have epic depend on this one existing first
   (e.g. core streaming playback has to exist before "continue
   watching" does)? An enabling epic can outrank a more exciting
   user-facing one for this reason alone.

STEP 6 — Confidence and impact scoring
   For each epic that survives Steps 1-5:
     - Confidence: how sure are we this is actually needed, vs a
       guess? (high / medium / low, with the reasoning stated)
     - User impact: what breaks or feels incomplete for the user
       if this epic is NOT in V1?
        ↓
STEP 7 — Final V1 list, labeled per the market-standard convention
   for exactly this situation (a fixed release boundary, checked
   against real prioritization frameworks — MoSCoW is the
   advisable standard here specifically because it's built for
   "what ships this release," while RICE needs real usage/reach
   data this project doesn't have yet):

     MUST HAVE   — high confidence + high impact + no unresolved
                   dependency gap. V1 does not ship without these.
     SHOULD HAVE — real value, but V1 is still coherent without it;
                   first candidate to add if time allows.
     COULD HAVE  — nice, low cost if it happens to fit, not worth
                   protecting scope for.
     WON'T HAVE (this release) — explicitly deferred, not silently
                   dropped — recorded, not forgotten, and revisited
                   at the next epic-selection pass.
```

## The record — one per epic, versioned per DOCUMENT_GOVERNANCE.md

```text
EPIC: <name>
MARKET CHECK: already solved? [yes/no] — if yes, adopted from: <what>
              — if no, why building from scratch is warranted: <reason>
NECESSITY: how this serves the core stated outcome
CONSTRAINT FIT: pass/fail against current Hard Constraints
FEASIBILITY: pass/fail, referencing Pre-Planning's assessment
DEPENDENCIES: what this blocks or is blocked by
CONFIDENCE: high | medium | low — <reasoning>
USER IMPACT IF EXCLUDED: <what breaks or feels incomplete>
DECISION: MUST HAVE | SHOULD HAVE | COULD HAVE | WON'T HAVE (this release) — <reasoning>
VERSION: v1
SIGNED OFF BY: <pending>
```

## Why the market-check runs first, not last

Checking feasibility or writing user stories for an epic before checking whether it's already solved wastes exactly the kind of effort the whole "smallest thing that satisfies the requirement" principle exists to prevent — this is that principle applied at the epic-selection level specifically, not just at the architecture level where it's already stated elsewhere in this system.
