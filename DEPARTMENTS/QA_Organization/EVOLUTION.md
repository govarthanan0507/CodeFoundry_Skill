# Evolution — Designed Now, Not Implemented in V0

This document specifies how the organization is allowed to change itself in
the future. None of the mechanism described here is built yet. It exists so
that when V0.2/V0.3/V0.4 (see `ROADMAP.md`) actually get built, they build
toward something already agreed on rather than improvising a governance
model under time pressure. Building this mechanism before V0 has been
proven on a real product would mean guessing at what's worth preserving in
a system that doesn't exist yet — see `HISTORY/DESIGN_DECISIONS.md`.

## Two separate loops — do not merge them

**Capability evolution** — is there a better way to test a specific domain.
Scoped to `CAPABILITIES/`. Lower stakes: a bad capability swap affects one
domain's testing quality.

**Organization evolution** — is there a better way to run QA itself: the
engine, the stage contracts, the disposition discipline, the constitution.
Scoped to `CONSTITUTION.md` and `ENGINE/`. High stakes: this changes what
every future audit depends on.

These must never share a single approval pipeline. Approving a better API
testing tool must never be able to quietly carry a change to the
disposition rule along with it.

## The shared shape of both loops

```
DISCOVER
   ↓
ANALYZE        (what does it do that we don't?)
   ↓
BENCHMARK      (can we verify/reproduce the difference with evidence,
                not just observe that it looks impressive?)
   ↓
IDENTIFY GAP / IMPROVEMENT
   ↓
PROPOSE CHANGE  (written: what improves, what could weaken, evidence for both)
   ↓
HUMAN APPROVAL  (mandatory — the organization never adopts unilaterally,
                 Constitution §17)
   ↓
CONFORMANCE TEST
   ↓
ADOPT AS NEW VERSION
   ↓
PRESERVE PREVIOUS VERSION (nothing is overwritten, Constitution §16)
```

## What "conformance test" means, concretely

A proposed new organization version is not judged as "does it run without
crashing." It is replayed against every historical full audit already on
file under `HISTORY/` (V0, V1, ...) and must reach equivalent-or-better
dispositions on the findings those audits already established. A new
version that would have missed a finding the old version caught fails
conformance, regardless of what else it improves.

## What triggers an evolution cycle

Reactive only, for now: a human hands the organization a specific external
QA system, tool, or methodology to evaluate against. Proactive,
self-initiated discovery (the organization going looking for competitors on
its own schedule) is not enabled in V0 — it is a candidate for V0.4 once
the reactive version has been run for real and proven trustworthy.

## Verification discipline on any comparison

Before any adoption proposal is written, it must answer, with evidence, not
impression:

1. What does the candidate do that this organization doesn't?
2. Can that difference be objectively reproduced/verified, not just
   observed as impressive?
3. What would adopting it improve?
4. What would it potentially weaken?

A proposal missing any of these four is incomplete and must not be put in
front of the human for approval — see the market-research verification
episode in `HISTORY/DESIGN_DECISIONS.md` for why this is a hard requirement,
not a suggestion: two research batches during this organization's own
design contained fabricated project names alongside real ones. If that can
happen in casual research, it can happen in an adoption proposal, and an
adoption proposal has much higher stakes.

## Multi-worker is a capability-evolution-scale decision, not a default

Per Constitution §15, multi-worker execution is not adopted by default.
If it is ever proposed, it goes through the Organization Evolution loop
above (not Capability Evolution) because it changes how the engine itself
runs — and it requires concrete evidence from real single-worker usage that
parallelism, isolation, or specialization is an actual bottleneck, not an
assumed one. See `HISTORY/DESIGN_DECISIONS.md` for what happened the last
time this was adopted speculatively.
