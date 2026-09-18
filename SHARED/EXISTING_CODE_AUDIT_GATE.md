# Existing-Code Audit Gate — mandatory before Epic Selection scopes new work

## The rule

Whenever `AGENTS/Ingestion/AGENT.md` produces a `CODE_DIGEST.md`
(Mode B or Mode C — an existing codebase was handed over), **Product
Manager may not decompose the project into epics
(`SHARED/EPIC_SELECTION_CRITERIA.md`) until this audit exists and is
signed off.** A real run of this system surfaced why this has to be a
gate, not a suggestion: a discussion report claimed extensive
self-verification of an existing codebase (tests re-run, README
claims checked), and that verification was genuinely good — but it
was still one party's own account of their own code. `Ingestion`
already says existing code is "evidence for Design Council to review,
not a decision Design Council is bound to accept as-is" — this file
makes that concrete: a required step, not a standing option Design
Council may or may not exercise.

## Why this is not redundant with Ingestion's own digest

`CODE_DIGEST.md` (and, for Mode C, its cross-check against docs)
answers "what does this code actually do, and does it match what the
docs claim." This audit answers a different question: **"is this code
actually good enough to build on, or does some of it need rework
first — and if so, which parts."** The first is about accuracy of
claims; this is about quality of foundation. A codebase can pass
Ingestion's cross-check cleanly (docs and code agree on what exists)
and still not be solid enough to extend without rework — passing the
digest is not passing this gate.

## Who performs it, and how much process it gets

Not the full 7-role Design Council debate — this is an audit, not a
new-build design decision, and running the full debate on code that
already exists would be the same "analysis paralysis" failure mode
`SHARED/WORKER_SCOPE_REGISTRY.md` already guards against for Repo
Analyzer. Only the Design Council roles whose domain the existing code
actually touches participate (e.g. `CODE_DIGEST.md` shows only
backend/storage code, no UI → Backend-Architect and Data-Architect
audit it; Frontend-Architect/UI-Designer/UX-Designer are not
convened for work that doesn't exist yet).

## What the audit actually requires — evidence, not re-reading the digest

Per component named in `CODE_DIGEST.md`'s `FOUND ARCHITECTURE` /
`FOUND FUNCTIONAL BEHAVIOR` fields, the assigned role(s) must generate
their own evidence, not restate what Ingestion or the original
handoff already claimed:

```text
- Run the actual test suite themselves (not trust a reported pass
  count) — same discipline as this system's own "verify, don't trust
  the self-report" rule used everywhere else.
- Read the actual code for the component, not its README/docstrings'
  claims about itself.
- Where the handoff claims something was checked (e.g. "CI run #N
  passed"), independently confirm it where possible, or explicitly
  record it as unconfirmed rather than silently inheriting the claim.
```

## The record — one per component, versioned per `DOCUMENT_GOVERNANCE.md`

```text
COMPONENT: <module/file or functional area, matching CODE_DIGEST.md>
VERDICT: REUSE AS-IS | REWORK | REPLACE | UNKNOWN — NEEDS MORE EVIDENCE
EVIDENCE: <what was actually run/read to reach this verdict — test
           output, specific code read, not a restated claim>
RATIONALE: <why this verdict, referencing the evidence above>
IMPACT ON PLANNED EPICS: <does this component block, partially
           support, or fully support what's being scoped next>
```

## What Epic Selection does with this

`SHARED/EPIC_SELECTION_CRITERIA.md`'s existing Step 4 (Feasibility
check) reads this audit as an input for any epic that depends on an
audited component — a `REWORK` or `REPLACE` verdict on a dependency
is itself a blocking dependency (Step 5), same as any other
prerequisite-epic relationship, not something Feasibility re-derives
from scratch. A component still `UNKNOWN — NEEDS MORE EVIDENCE` blocks
Epic Selection from scoping anything that depends on it, the same way
a Pre-Planning `NEEDS MORE EVIDENCE` verdict blocks that stage
(`SHARED/HANDOFF_CONTRACT.md`'s mapping) — this is the same disposition
category, applied one stage later.

## What this never becomes

- Never a full re-audit of a component nothing planned depends on —
  scope this to what `CODE_DIGEST.md` flags as relevant to the
  epics under consideration, not the entire codebase reflexively.
- Never a QA_Organization audit by another name — this is Design
  Council auditing architecture/quality for build-readiness; it does
  not replace an actual QA_Organization cycle later, and does not use
  QA's own Constitution/engine.
- Never skipped because the existing code "looks fine" or the
  original handoff was thorough — thoroughness of the *report* is not
  evidence about the *code*; this gate exists specifically because
  those are different things.
