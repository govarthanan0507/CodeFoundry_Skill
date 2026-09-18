# Whole-Product Architecture Gate — mandatory before Development starts on the first epic

## The gap this closes

Design Council, as originally built, only ever evaluates one epic at
a time, as it's picked up per `PROCESS_SCALING.md`'s tiering. Nothing
looks at the *whole* roadmap (`ROADMAP.md`, produced by Product
Manager) and asks: does this cohere end to end, or does the design
chosen for the *first* epic quietly foreclose or complicate a later
one? A real product raised this directly: before committing
engineering effort to V1, the request was for the Council to look at
the entire planned product and issue one explicit verdict — not
per-epic sign-off in isolation, and not full detailed design for every
future epic either (that would violate the same "just-in-time, not
all upfront" discipline `DISCOVERY_PROTOCOL.md` already uses).

## The rule

**Before Development starts on the first epic of any project's V1,**
Design Council issues a **Whole-Product Architecture Verdict** —
one pass across every epic named in `ROADMAP.md` (every version, not
only V1's), checking cross-epic coherence. This is required once per
project at this point, not repeated per version — a later version's
own epics still get their normal per-epic Tier 2/3 treatment when
they're actually picked up; this gate is specifically about the
handoff moment before any code gets written at all.

## What this verdict actually checks — coherence, not full design

This is lighter than a full Tier 3 debate on every future epic. It
does not produce a `TRD.md`/`FRD.md` for epics that haven't been
picked up yet — that would be exactly the premature-detail problem
`DISCOVERY_PROTOCOL.md`'s just-in-time principle already avoids. It
checks three things, using whatever level of detail already exists
per epic (full `TRD.md`/`FRD.md` for epics already designed, the
one-line description from `EPIC_SELECTION.md`/`ROADMAP.md` for epics
that aren't yet):

```text
1. FORECLOSURE CHECK
   Does any already-designed (or currently-being-designed) epic's
   architecture choice make a later epic materially harder or
   impossible, in a way that would only be discovered once that
   later epic is actually reached? Name it specifically if found —
   "epic X's schema choice would need to change for epic Y" is a
   real finding; "this might not scale" without a specific epic named
   is not.

2. ARCHITECTURAL DIRECTION CHECK
   Do the epics, taken together, point toward one coherent system, or
   do they imply contradictory architectural directions (e.g. one
   epic assumes local-only forever, another epic's stated intent
   would require a server component)? This is a sanity check against
   idea.md's own inherited scope boundaries, not a new judgment call.

3. KNOWN-UNKNOWN SURFACING
   For epics far enough out that real architecture can't be decided
   yet (nothing to design against), name what would need to be true
   for them to work, as an explicit open question — not silently
   deferred, not force-designed before there's evidence to design
   against either.
```

## Verdict shape — same four outcomes Pre-Planning already uses

```text
GO                    — no foreclosure found, epics point in one
                         coherent direction; Development may proceed
                         on the first epic as designed
GO WITH NOTED RISKS    — no blocking foreclosure, but specific
                         cross-epic risks are named and carried
                         forward (not silently dropped) into later
                         epics' own Design Council passes when they're
                         actually picked up
NEEDS MORE EVIDENCE    — a specific later epic's feasibility is
                         genuinely unknown in a way that could change
                         the *first* epic's own design if resolved
                         differently — names exactly what evidence
                         would resolve it
REDESIGN REQUIRED      — a real foreclosure was found: the first
                         epic's current design must change before
                         Development starts, because proceeding as-is
                         would require expensive rework once a later
                         epic is reached
```

A `REDESIGN REQUIRED` verdict routes back into that epic's own
Tier 2/3 process (whichever already ran) with the specific conflict
named — it is not a new debate invented for this gate.

## What this gate never becomes

- Never a substitute for each epic's own Design Council pass when
  it's actually picked up — this gate checks coherence across epics
  at whatever detail already exists; it does not pre-design epics
  that haven't been reached.
- Never an excuse to plan versions beyond what's already evidenced —
  per this project's own "don't plan V9+ until real usage produces
  evidence" instinct, this gate reviews what's already in
  `ROADMAP.md`, it does not invent additional future versions to
  check against.
- Never repeated per-epic — one verdict, at the one moment (before
  the very first epic's Development begins), not a recurring gate.

## Where this fits in the lifecycle

```text
Pre-Planning GO → Epic Selection → ROADMAP.md produced
        ↓
Design Council's normal per-epic pass on the FIRST epic(s) actually
being built (Tier-appropriate, per PROCESS_SCALING.md)
        ↓
Whole-Product Architecture Gate (this file) — reviews ALL epics in
ROADMAP.md for coherence, using the first epic(s)' now-completed
design plus whatever level of detail exists for the rest
        ↓
Verdict. GO / GO WITH NOTED RISKS → Development starts.
NEEDS MORE EVIDENCE / REDESIGN REQUIRED → resolved before Development
starts, per the verdict's own next-step.
```
