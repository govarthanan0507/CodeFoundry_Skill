# Reuse and License Rule — V1

## Why this exists

CodeFoundry's whole motto is: don't reinvent what's already proven —
find it, adapt it, build on it. That motto is worthless without two
guardrails: adopting a restrictively-licensed reference without noticing
until it's too late to unwind, and "adapting" that's actually just
copying with different variable names. Both failure modes are cheap to
prevent early and expensive to discover after the fact.

## Part 1 — Repo Analyzer becomes mandatory, gated by tier

Today, invoking Repo Analyzer (`WORKER_SCOPE_REGISTRY.md`'s Research
Worker section) only happens "when reuse is in question" — optional,
depends on someone remembering to ask.

New rule: for any Tier 2 or Tier 3 task (per `PROCESS_SCALING.md`), the
Market/Research role (Pre-Planning) or Research Worker (any later stage)
**must** run Repo Analyzer against the idea's core mechanic before
Design Council commits to a "how." Tier 1 tasks are exempt by default —
running a full reuse search on a trivial task is the same
analysis-paralysis failure mode this project already avoids elsewhere.

```text
Task is Tier 2 or Tier 3
        ↓
Repo Analyzer runs against the idea's core mechanic
        ↓
Comparable candidates found?
    ├── YES → produce REPO_ANALYSIS.md / REPO_INDEX.md, feed to
    │         Design Council as required input before it decides "how"
    │
    └── NO → record "no comparable candidate found" explicitly —
              an empty result is still a required, recorded output,
              not silently skipped
```

## Part 2 — License findings: recorded always, blocking depends on intent

A license finding on an OSS candidate is **always recorded** — this is
non-negotiable regardless of project type. Whether it **blocks** depends
on distribution intent at the time of the finding:

```text
License finding on a reuse candidate
        ↓
Is there current shipping/distribution intent
(per Ideation's personal/hobby vs. commercial signal, or a later
Pre-Planning re-entry per Part 3)?
    ├── NO  (personal/hobby, no distribution) →
    │         Finding recorded in the project's findings log.
    │         Does NOT block this build.
    │
    └── YES (shipping/commercial intent) →
              Routes to HARD_CONSTRAINTS.md category 5
              (Licensing and legal exposure) — human decision
              required before this candidate can be adopted.
```

A recorded-but-not-blocking finding is never deleted or forgotten. It
must resurface automatically at:

1. **A Pre-Planning re-entry triggered by an intent change** (see
   `AGENTS/Orchestrator/AGENT.md`'s intent-change re-entry trigger) — the
   moment a hobby project's owner asks "should I actually try to sell
   this," every previously-recorded-but-unblocking license finding is
   re-surfaced as part of that re-entry's evidence.
2. **The release/ship gate** (Security or DevOps/Release worker, once
   built) — an unresolved license finding on anything actually shipped
   blocks release the same way a missing backup/restore verification
   already blocks a Backend release, until it is explicitly resolved
   (replaced, relicensed, or human-accepted per `HARD_CONSTRAINTS.md`).

This is a durable-record-plus-recheck pattern, not live coordination —
the same shape as `HARD_CONSTRAINTS.md` itself and QA_Organization's
risk-acceptance record. Nobody has to remember to raise it; the gate
checks for it.

## Part 3 — Adapt, not copy: a concrete test

"We wrote it in our own words" is not evidence of adaptation. Design
Council must be able to answer, concretely, for any design that drew on
a Repo Analyzer finding:

```text
Reference candidate(s) identified (possibly more than one solving the
same core mechanic — Repo Analyzer should compare them against the
actual requirement, not just list them)
        ↓
Design Council names at least one genuine structural difference from
the closest reference:
  - different module/service boundaries, or
  - different data model, or
  - different architecture/pattern (not just renamed variables/files)
        ↓
Can a structural difference be named?
    ├── YES → adaptation. Proceed, with the difference recorded in the
    │         architecture decision record (reasoning + rejected
    │         alternative, per `COUNCILS/Design-Council/COUNCIL.md`).
    │
    └── NO  → treated as a copy, not an adaptation. Blocked from
              handoff — same severity as the structural-UI-copy rule
              already in `DEPARTMENTS/Developer_Organization/CAPABILITIES/Frontend-Developer/workflow.md`
              Phase 8 (a layout that copies a named product's
              structural chrome is always at least `MAJOR`, never
              advisory). This rule generalizes that same principle from
              UI layout to backend/architecture reuse.
```

When multiple reference repos solve the same problem, Repo Analyzer's
comparison (Part 1) is what Design Council cites as evidence for why it
drew from one over another — the same "evidence classified by strength"
discipline the Research role already applies elsewhere in this system.

## Relationship to existing files

- Does not replace `HARD_CONSTRAINTS.md` — it feeds it. Category 5
  (Licensing and legal exposure) is where a blocking finding actually
  routes for a human decision.
- Does not replace `PROCESS_SCALING.md` — it uses that file's tiers to
  decide when Repo Analyzer is mandatory versus skipped.
- Does not replace the Orchestrator's re-entry logic — it is one of the
  triggers that logic must support (see
  `AGENTS/Orchestrator/AGENT.md`'s intent-change re-entry trigger).
