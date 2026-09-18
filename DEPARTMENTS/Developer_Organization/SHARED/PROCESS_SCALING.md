# Process Scaling — How Much Convenes For This Task

## The problem this solves

Without an explicit rule, the default drifts toward "convene the full Council, just to be safe" — which is exactly the over-scoping failure this whole project was flagged for on day one. This file makes the scaling decision mechanical, based on objective signals about the task, not a feeling about how important it seems.

## Who decides, and when

The **Orchestrator** determines the tier before any work begins, using the triggers below — not "how hard does this feel," but whether specific, checkable conditions are true. If genuinely ambiguous, default one tier up, not down — the cost of over-scoping a simple task once is small; the cost of a Tier 3-shaped problem getting Tier 1 treatment is a production mistake.

## The three tiers

### Tier 1 — Solo/Pair (Product + one Developer worker, no Council)

**Triggers (all must be true):**
- Touches exactly one domain (frontend-only, backend-only, or a report/data task with no user-facing surface).
- Reuses an existing pattern already established in the codebase — no new service boundary, no new external dependency.
- Touches zero or one category in `COUNCILS/Design-Council/HARD_CONSTRAINTS.md`.
- Change is easily reversible (not a schema migration, not a public-facing security change).

**Process:** Product writes the (small) requirement and acceptance criteria. The one relevant Developer worker builds and verifies it directly. No design debate, no gate beyond the normal one for that worker's own completion rule.

**Examples:** a UI copy change, a new report/dashboard view, a bug fix within existing logic, adding a field to an existing form.

### Tier 2 — Small Crew (2–4 people, narrow scope, no full debate)

**Triggers (any of these):**
- Touches 2–3 domains (e.g. a new API endpoint plus the UI that calls it) but doesn't introduce a new architectural pattern.
- Touches 2 categories in `HARD_CONSTRAINTS.md`.
- Modifies an existing service boundary without creating a new one.

**Process:** Only the specific Council roles whose domain is actually touched convene — e.g. Backend/API Architect + Frontend Architect for a new endpoint and its UI. They produce a short design note (not the full build-ready package), and the mandatory-debate machinery from `DEBATE_PROTOCOL.md` only activates if these specific roles actually disagree — the Synthesizer/Critic formality is not run by default at this tier. The relevant Developer worker(s) then build against that note.

**Examples:** the Devices/Activity settings page work we scoped earlier, if it had reused the existing SQLite pattern without any new architectural question — it didn't, which is why that case correctly escalated (see Tier 3 below).

### Tier 3 — Full Council (all 7 roles, mandatory debate protocol)

**Triggers (any of these):**
- New service, new external dependency, or a new architectural pattern not already established.
- Touches security-sensitive surface materially (auth, exposure to the internet, handling other people's data).
- Spans 4+ domains at once.
- Touches 3+ categories in `HARD_CONSTRAINTS.md`.
- Is, in plain terms, a new application or a major feature — not a modification to an existing one.

**Process:** the full mechanism already built — all 7 roles, mandatory debate, Synthesizer, Independent Critic, and the three tested outcomes (clean resolution, deadlock, infeasible premise).

**Examples already run this session:** the Devices/Activity feature test (touched UX, UI, Frontend, Backend, Data, and Security all materially) and the Baseflix remote-access idea (new external dependency, internet-facing exposure, multi-user data — 3 Hard Constraint categories at least).

## Escalation, not just initial assignment

A task assigned Tier 1 or 2 can escalate mid-work if a Developer worker or Council role discovers the real scope was underestimated (e.g. a "simple UI change" turns out to require a new API contract). This uses the same change-request mechanism already defined for post-handoff accountability in `COUNCILS/Design-Council/COUNCIL.md` — it is not a failure of the tiering, it's the tiering doing its job by catching the mismatch instead of quietly absorbing it at the wrong tier.

## Relationship to the Backend Developer's own risk-scaled verification

`DEPARTMENTS/Developer_Organization/CAPABILITIES/Backend-Developer/workflow.md` already has a similar Low/Medium/High risk scale for how much verification a single worker applies to its own change. That's a narrower, worker-internal version of this same principle — this file governs whether the Council convenes at all; that one governs how rigorously one worker verifies its own output once it's already been assigned the work. Keep them conceptually aligned (both objective-trigger-based, both default to the safer tier when ambiguous) rather than treating them as unrelated scales.
