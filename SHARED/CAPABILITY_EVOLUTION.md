# Capability Evolution — Driven by Repo Analyzer — V1

## Two roles for Repo Analyzer — not one

Repo Analyzer is not built inside CodeFoundry — it is a separate
external application (in active development, producing
`REPO_ANALYSIS.md`/`REPO_INDEX.md`, per
`SHARED/WORKER_SCOPE_REGISTRY.md`'s Research Worker section).
CodeFoundry consumes its output as an evidence source. It has two
distinct jobs, and this file is about the second one, which didn't
exist before:

```text
1. PER-PROJECT REUSE CHECK (already built — SHARED/REUSE_AND_LICENSE_RULE.md)
   "Does something already solve this idea's core mechanic, and how
   adoptable is it?" Runs per Pre-Planning/Planning cycle, feeds one
   project's own decisions.

2. CAPABILITY EVOLUTION (this file, new)
   "Can what this repo does update one of CodeFoundry's OWN worker
   capabilities — Frontend/Backend/Mobile Developer's CAPABILITY.md/
   workflow.md — so the system keeps improving instead of staying a
   static, one-time-built set of files?" Not scoped to one project;
   feeds CodeFoundry itself.
```

## Repo Analyzer's output includes a confidence ratio

Per the external tool's own design: alongside `REPO_ANALYSIS.md`/
`REPO_INDEX.md`, each candidate carries a confidence ratio — how
adoptable/relevant it is. This is treated as evidence, classified by
strength like every other finding in this system
(`AGENTS/Ideation/AGENT.md`'s fact/assumption/inference/unknown rule)
— a confidence ratio is Repo Analyzer's own assessment, not
automatically promoted to "this should be adopted" without the loop
below.

## This is Capability Evolution, not Organization Evolution — same separation `QA_Organization` already drew

Reusing `DEPARTMENTS/QA_Organization/EVOLUTION.md`'s own hard-won
distinction directly, because it applies here unchanged:

```text
CAPABILITY EVOLUTION (this file) — is there a better way to do one
  domain's work: a Frontend pattern, a Backend approach, a Mobile
  platform technique. Scoped to CAPABILITIES/<Worker>/ files. Lower
  stakes — a bad capability update affects one domain's output
  quality.

ORGANIZATION EVOLUTION (not this file) — is there a better way to run
  CodeFoundry itself: the stage sequence, the debate protocol, the
  disposition discipline, CONSTITUTION-equivalent rules. Scoped to
  AGENTS/Orchestrator, COUNCILS/*/COUNCIL.md, DEBATE_PROTOCOL.md-level
  files. High stakes — changes what every future project depends on.
```

**These never share one approval pipeline.** A Repo Analyzer finding
that looks like it improves Backend Developer's API-contract pattern
must never be able to quietly carry a change to, say, the Design
Council's debate protocol along with it — same reasoning
`QA_Organization/EVOLUTION.md` already states for its own two loops.

## The capability pool grows additively — two different outcomes, not one

This is why the capability pool is kept separate from the worker
identity itself: a worker (Frontend/Backend/Mobile Developer) is a
fixed role, but the skill sets it draws on are meant to keep growing
as real, good repos are found — a great Frontend skill set found today
should make the pool bigger, not require rebuilding the worker. Two
different paths, depending on whether the new find overlaps something
already in the pool:

```text
Repo Analyzer surfaces a skill set (e.g. a particular Frontend
component/interaction pattern that consistently produces noticeably
better UI output)
        ↓
Does this overlap an EXISTING capability already in the pool for
this worker (same APPLIES_WHEN — same kind of problem it solves)?
    ├── NO  → pure addition. The capability pool gains a new entry.
    │         No benchmark required — there's nothing to compare it
    │         against, only to add. Still goes through the ANALYZE/
    │         PROPOSE/HUMAN APPROVAL steps below, just skips BENCHMARK
    │         (there's no incumbent to benchmark against).
    │
    └── YES → benchmark required before anything is added or
              replaced. See below — never silently substituted, same
              rule QA_Organization's own CAPABILITIES.md already
              states for its testing-tool capabilities, applied here
              to dev-skill capabilities.
```

## The benchmark, made concrete — not a vague "compare them"

When a candidate overlaps an existing capability, the assigned worker
runs both, on the same real task, and reports an agnostic result —
neither side pre-favored:

```text
SAME TASK, run twice, same worker:
  RUN A (incumbent capability):
    OUTPUT PRODUCED: <the actual result — e.g. the UI produced,
                       assessed the same way Critic mode already
                       assesses Frontend output in that worker's own
                       workflow.md>
    TOKENS BURNED: <actual measured token cost for this run>
  RUN B (candidate capability, from the new repo):
    OUTPUT PRODUCED: <same assessment method as Run A>
    TOKENS BURNED: <actual measured token cost for this run>
        ↓
REPORTED AS A NEUTRAL COMPARISON, not a recommendation baked in —
  "Run A produced X, cost Y tokens; Run B produced X', cost Y' tokens"
  — the human (or, for a clearly one-sided result, the standard
  PROPOSE CHANGE step below) decides what the comparison means, this
  benchmark step does not decide FOR them by only reporting the
  winner.
```

This is the same evidence-over-assertion discipline already used
everywhere in this system (`QA_Organization/CONSTITUTION.md` §2,
inherited by this whole project) — "the new one seemed better" is not
a benchmark result; a measured output-quality-versus-token-cost
comparison is.

## The loop — same shape `QA_Organization` already proved, applied to a capability file

```text
DISCOVER        (Repo Analyzer surfaces a candidate + confidence ratio,
                 either from a per-project run or a standalone scan the
                 human directs it to make)
   ↓
ANALYZE         (what does this repo's approach do that the current
                 capability file — e.g. Backend-Developer/workflow.md
                 — doesn't?)
   ↓
BENCHMARK       (required only when the candidate overlaps an
                 existing capability — the concrete output-vs-token
                 head-to-head test above, not Repo Analyzer's
                 confidence ratio taken at face value. A high
                 confidence ratio is a reason to look, never a
                 reason to skip this step. Skipped only for a pure
                 addition with no existing incumbent to compare
                 against.)
   ↓
IDENTIFY GAP / IMPROVEMENT
   ↓
PROPOSE CHANGE  (written: which specific capability file, what
                 changes, what improves, what could weaken, evidence
                 for both — same four-question discipline below)
   ↓
HUMAN APPROVAL  (mandatory — no capability file is updated
                 unilaterally, same as QA_Organization Constitution §17)
   ↓
ADOPT AS NEW VERSION (the capability file is updated; the previous
                 version is preserved, not overwritten — same
                 `SHARED/DOCUMENT_GOVERNANCE.md` versioning discipline
                 already used for every other artifact in this system)
```

No "conformance test against historical audits" step here the way
`QA_Organization`'s Organization Evolution has one — that check exists
because QA verdicts are safety-critical in a way one capability file's
wording isn't. If Capability Evolution is ever extended to touch
something safety-critical (e.g. Mobile Developer's device-security
Phase 3), require the stricter Organization Evolution pipeline instead
of this one — the separation above exists precisely so that decision
gets made explicitly, not defaulted into the lighter loop because it
happened to originate from a Repo Analyzer finding.

## Verification discipline — reused directly, not restated differently

Before any proposal reaches the human, per
`QA_Organization/EVOLUTION.md`'s own four questions, applied here:

1. What does this repo's approach do that the current capability file
   doesn't?
2. Can that difference be objectively verified — read the actual repo,
   not just trust Repo Analyzer's confidence ratio or a research
   summary about it?
3. What would adopting it improve?
4. What would it potentially weaken?

`QA_Organization/HISTORY/DESIGN_DECISIONS.md` records a real episode
of fabricated project names appearing alongside real ones in a
research batch during that organization's own design — the same risk
applies to any Repo Analyzer finding. A proposal that hasn't verified
the repo actually exists and does what's claimed is not ready for
human approval, regardless of how high its confidence ratio is.

## What triggers a cycle

Reactive, same as `QA_Organization`'s current stance: a Repo Analyzer
run (per-project or a standalone scan the human directs) surfaces a
candidate. CodeFoundry does not go looking for capability-improving
repos on its own schedule yet — that would be the proactive-discovery
step `QA_Organization/EVOLUTION.md` also defers, for the same reason:
prove the reactive version works first.
