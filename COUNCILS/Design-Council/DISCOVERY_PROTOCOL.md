# Design Council — Discovery Protocol (per-story, just-in-time)

## Why this exists, and why it's scoped to one story, not the epic

Elicitation (finding out what someone actually wants) has to happen
before analysis/design, not be skipped or folded into the debate itself
— `DEBATE_PROTOCOL.md`'s ad hoc "the Council may ask the user a
question" rule is analysis-time question-asking, not real elicitation.
But elicitation for a whole epic at once would either overwhelm the
user with everything at once, or force premature detail on stories that
won't be picked up for a while — the same reasoning that already led
this system to reject a 50-category speculative capability map
(`HISTORY`-equivalent reasoning in `QA_Organization`) and to make
Repo Analyzer tier-gated rather than always-on. Discovery therefore runs
**per user story, at the moment that story is pulled** — not per epic,
not for the whole product upfront.

## The actual goal

Discovery extracts what the user already means, it does not install
an opinion on them. Every mechanism in this file — the no-pushback
intake, the reference-first fallback, showing concrete options instead
of asking abstractly, proposing a labeled default only when nothing
else surfaces a preference, kind and constructive pushback in Phase 2
— serves one outcome: the user ends Discovery feeling like they
decided everything, because in every case where they had a real
preference, they did. The Council's scaffolding (reference libraries,
industry defaults, concrete options) only fills the gaps the user
genuinely didn't have an opinion on, and even those are labeled as
assumptions the user can still override, never presented as if the
user chose them. A Discovery session someone would describe as "it
felt like it read my mind" is a success; one they'd describe as "it
talked me into things" is a failure, even if the end result looks
identical on paper.

## Extraction, not exhaustiveness

Discovery is not trying to reach a complete specification before it's
allowed to close. A scattered inspiration ("something like that app,
but calmer") is usable signal, not an incomplete answer waiting to be
filled in — the job is to extract the actual directional intent from
whatever the user gives, partial or not, and turn it into something
that satisfies that intent in most cases. This is the same
`CLEAR WITH OPEN ITEMS` gate already used everywhere else in this
system, stated as a principle here specifically because Discovery is
where the temptation to over-collect is strongest: chasing a fully
specified answer to every question is not more rigorous, it's the
"ask at least N questions" failure `AGENTS/Ideation/AGENT.md` already
bans, recurring in a new place. Genuine gaps still get named as open
items (never hidden) — but a gap is not automatically a reason to keep
asking; it's only a reason to keep asking if resolving it would
materially change the outcome, the same stopping test
`SHARED/STAGE_EXIT_CONTRACT.md` already applies to every stage.

## Trigger — when this runs

```text
A ticket (= one user story, per DEPARTMENTS/Developer_Organization/SHARED/AGILE_WORKFLOW.md) is about to
move from TO DO into IN PROGRESS
        ↓
Discovery for THIS story runs first. A ticket may not enter
IN PROGRESS until its Discovery record is CLEAR or CLEAR WITH OPEN
ITEMS (same three-state gate used everywhere else — BLOCKED means the
ticket stays in TO DO, not silently started anyway).
```

This is the same pull-based discipline the Kanban board already uses
(work is elaborated when it's about to start, not stockpiled in
advance) — Discovery is what happens in the moment of that pull, not a
separate ceremony bolted on before it.

## Who participates — tier-determined, never a fixed headcount

The full 7-role Council does **not** convene for every story. Per
`SHARED/PROCESS_SCALING.md`, the story's tier determines who's actually
in the room:

```text
Tier 1 (solo/pair) — the one relevant Developer worker's own
  clarifying questions suffice; Discovery as a separate Council-level
  step is not triggered. (Same exemption logic PROCESS_SCALING.md
  already uses for Repo Analyzer and full debate.)

Tier 2 (small crew) — only the 2-4 Design Council roles whose domain
  this story actually touches ask questions (e.g. a backend-only data
  story: Backend/API Architect and Data/Database Architect only — UX,
  UI, Security, and the System Architect are not pulled in for
  something outside their domain).

Tier 3 (full Council) — all 7 roles, same as a full debate would use.
```

A role with nothing relevant to ask for this specific story says so
explicitly ("reviewed, no question needed") rather than being silently
absent — same "a silent role is a suspicious role" rule
`DEBATE_PROTOCOL.md` already applies to debate; it applies here too,
scoped to whichever roles are actually in the room for this tier.

## How it runs — two phases, deliberately not mixed

This is the well-established divergent-then-convergent facilitation
pattern (brainstorming/design-thinking practice: generate freely,
defer judgment, *then* filter/evaluate — mixing the two phases is a
known way to suppress what someone would have said) applied to
per-story elicitation. Challenging the user's input before they've
finished giving it means they self-censor the rest; the fix is to
structurally separate when input is taken from when it's evaluated.

### Phase 1 — Intake (divergent: accept, don't filter)

Every participating role follows `AGENTS/Ideation/AGENT.md`'s
questioning discipline directly, not a lighter paraphrase of it, but
under one added rule specific to this phase: **no pushback, no
feasibility judgment, no cost/resource commentary, and no *signal* of
any of those — accept whatever the user gives, however it arrives,
including ideas that are vague, imaginative, or not obviously
buildable.**

**Tone, stated concretely, not left to interpretation:** warm,
curious, welcoming — the user should feel encouraged to keep talking,
not evaluated. This rules out more than direct pushback: no "that's
ambitious," no visible hesitation before responding, no qualifying a
question with "just so you know, this might be hard" — any of those
leaks Phase 2's judgment into Phase 1 and the user starts
self-editing, which is the exact failure this two-phase split exists
to prevent. A user who says something impossible or half-formed gets
the same warm "tell me more" response as one who says something
routine — the difference only shows up later, in Phase 2, never here.
If a role is unsure whether a reaction would read as judgmental, the
safer default is silence plus the next welcoming question, not a
disclaimer.

- **One natural question at a time, never a batch or a checklist.**
  A UX Designer asking about a story does not hand the user five
  bullet points to fill in — it asks the single highest-value question
  ("when someone lands on this screen, what's the first thing they're
  trying to do?"), listens, and lets the answer reshape what's asked
  next.
- **Adaptive, not a fixed question count.** Some stories resolve in one
  exchange; others need several. The number of questions is a
  consequence of what's actually missing, never a predetermined script.
- **Every reference, inspiration, link, or document the user offers is
  recorded as given** — logged, not evaluated, not trimmed for
  feasibility. Recording is not endorsement; Phase 2 is where it gets
  checked.
- **Multiple participating roles pool into one conversation**, not a
  panel taking turns interrogating the user — same reasoning as
  before, applies equally inside Phase 1.
- **Ends only when the user says they're done** — not when a role
  judges intake "sufficient." This is a deliberate difference from
  Ideation's own model-inferred CLEAR state: Phase 1's exit is
  user-declared, because the whole point is that the user, not the
  Council, controls when they've said everything they wanted to.

### When the user doesn't know — a real case, not an edge case

A user often can't answer "how should this button behave" or "what
should the user journey look like" — not because they're withholding
it, but because they genuinely don't have that vocabulary or that
opinion formed. Re-asking the same question more insistently doesn't
produce an answer; it produces frustration. This is a required
fallback sequence inside Phase 1, not an improvisation:

```text
User can't answer a design/UX question directly
        ↓
1. Ask for a REFERENCE first, not a specification:
   "Is there an app or site that does something like this well —
   even loosely — that we could take cues from?" This reuses the
   same instinct as Market/Research's OSS-reuse check, applied to
   inspiration rather than code: people can usually recognize and
   react to something concrete far more easily than describe it from
   nothing.
        ↓ still nothing
2. SHOW, don't ask blankly: offer 2-3 concrete, named options ("most
   apps either confirm destructive actions with a popup, undo it
   silently after the fact, or both — which feels closer to what you
   want?") rather than an open "how should this work?" A concrete
   choice is answerable; an abstract question about taste often isn't.
        ↓ still no preference
3. Propose the INDUSTRY-STANDARD default explicitly, and move on:
   "I'll go with [the common pattern for this] unless you want it
   different — flag it any time if that's wrong." This is never left
   as a blank or a stalled question — Ideation's own rule already
   governs the label: it is recorded as an ASSUMPTION, not a
   confirmed fact, and it is one of the concrete things Phase 2
   re-checks (does this default actually fit the constraints, or does
   the "sweet and clean" version need to look different) — never
   smuggled through as if the user had chosen it.
```

Steps 2 and 3 pull from `REFERENCE_LIBRARY.md` first — a pre-loaded
set of common UI pattern options and defaults (buttons, calendars,
color, navigation, forms) — rather than running a live search for
something this common every single Discovery session. A live search
is warranted only when that file genuinely doesn't cover the pattern
in question, and the finding then gets folded back into it (see that
file's "Growing this file" section) so the gap isn't paid for twice.

This sequence is why Discovery doesn't stall on the questions a given
user can't personally answer — it substitutes reference and industry
precedent for a specification the user was never going to be able to
provide, while keeping every substitution honestly labeled as an
assumption the user can still redirect.

### Phase 2 — Verification (convergent: check, then push back)

**Tone here still isn't blunt — "no" is stated plainly but kindly.**
A pushback names the constraint and, wherever possible, offers what
*can* be done instead in the same breath — never a bare rejection.
Compare: "That's not possible" (bare) versus "The exact version of
that would need paid infrastructure we're not using right now, but
here's a version that gets you most of the same result for free" (the
required shape — clear about the limit, still constructive). The user
should leave Phase 2 knowing exactly what's happening and why, never
feeling scolded for what they asked for in Phase 1 — asking for
something ambitious in Phase 1 was correct behavior, not a mistake to
be corrected in tone.

Only now do the consulted roles evaluate what Phase 1 collected:

```text
For each requirement / reference / inspiration from Phase 1:
        ↓
Feasible within current constraints (SHARED/HARD_CONSTRAINTS.md
budget, timeline, platform support, etc.)?
    ├── YES → carries forward as-is.
    └── NO  → named explicitly, with why (costs money, exceeds
              available resources, technically infeasible as stated,
              conflicts with an already-accepted item) — this is where
              pushback happens, not in Phase 1, and it's Constitution-
              style honest disagreement, not a vague "maybe not."
        ↓
Genuinely contested or resource-constrained items are negotiated here
(the "little pushback" step) — resolved, or carried forward as an
explicit open item if genuinely unresolved (never silently dropped).
```

Phase 2 closes only once the user has seen and agreed with the final
accepted/pushed-back/open-items picture — this is a confirmation step,
not a formality: the roles state it back in plain language ("here's
what we're actually going to build, and here's the one part we can't
do as originally described") and the user gets to react before it's
written down as final. Only after that confirmation does the record
below get written to `DISCOVERY.md` and treated as closed.

Phase 2 closes with the same STATE gate used everywhere else:

```text
CLEAR               — Phase 1's intake, filtered by Phase 2's
                       verification, is coherent enough to hand off.
CLEAR WITH OPEN ITEMS — some contested/unresolved items carried
                       forward explicitly (per the pushback step above).
BLOCKED              — a Phase 1 item is fundamentally incompatible
                       with what's actually possible, and no version of
                       it survives verification without a human
                       decision (routes per HARD_CONSTRAINTS.md).
```

## Direction-change pushback — distinct from Phase 2's feasibility pushback

A real gap, found live: Phase 2's pushback rule above only covers
*feasibility* (can this be built within budget/timeline/platform
constraints). It says nothing about a different, equally real case —
the user redirects mid-conversation not with new information filling
a gap, but with a **material reversal or expansion of a decision this
process already treated as settled and built against** (e.g. a
visual/architecture direction already implemented gets discarded for
a substantially different one, or new capabilities get folded in that
were never part of the story's original scope). Silently complying
with this the same way Phase 1 accepts ordinary new input is wrong —
it treats a real direction change as if it cost nothing, when it may
discard working code, reopen a closed decision, or quietly expand
scope no one has actually agreed to pay for.

**The rule**: whenever participating roles recognize input as this
kind of direction change (not merely a preference on something still
open), they say so explicitly, in the same polite, constructive tone
Phase 2 already requires — name what's changing, what already-decided
or already-built work it affects, and confirm the user actually wants
that trade-off before treating it as accepted. This is a *pushback*,
not a refusal: the answer is very often still "yes, do it anyway" —
the point is that the user hears the real cost stated plainly and
chooses it knowingly, rather than the process pivoting silently as if
nothing of substance changed.

```text
Bad (silent pivot):    User asks for a different UI framework/style.
                        Council immediately starts redesigning, no
                        mention that this discards the shell already
                        built against the prior decision.

Good (named, polite):  "Sure — that means redoing the chat shell we
                        already built against the earlier decision,
                        not just restyling it. Want me to go ahead
                        with that?"
```

This applies at any point in the conversation, not only inside a
formal Phase 2 verification pass — a direction change can surface
mid-Phase-1, mid-build, or in an entirely separate later conversation
about the same story. Wherever it's recognized, it gets named before
being acted on.

## Output — `DISCOVERY.md`, one fixed template, not improvised per story

The full required shape lives in `templates/DISCOVERY_TEMPLATE.md` —
this file does not restate it, so there is exactly one source of
truth for what a complete handoff contains (the same reasoning
`SHARED/DOCUMENT_GOVERNANCE.md` already applies to other artifacts).
A `DISCOVERY.md` missing any of that template's required sections is
incomplete, and per `DEPARTMENTS/Developer_Organization/SHARED/AGILE_WORKFLOW.md`'s Kanban gate the
ticket stays in `TO DO` rather than entering `IN PROGRESS` on a
partial record.

This record is what the assigned Developer worker builds against —
same relationship the epic-level design package has to Development
today, just scoped one level down to the individual story. It is also
what gets handed to the Design Council debate machinery
(`DEBATE_PROTOCOL.md`) when a story's Phase 2 surfaces something
genuinely architecture-level, rather than being re-litigated from
scratch there.

## Relationship to existing files

- Does not replace `DEBATE_PROTOCOL.md` — that's still what runs for
  genuinely epic-level or architecture-level decisions (Tier 3
  material that isn't just "this one story," e.g. the foundation phase
  in `SHARED/PARALLELIZATION_GUARDRAIL.md`). Discovery is the
  story-scoped, just-in-time counterpart to it.
- Does not replace `SHARED/PROCESS_SCALING.md` — it consumes that
  file's tiering, it doesn't define a new one.
- Wires into `DEPARTMENTS/Developer_Organization/SHARED/AGILE_WORKFLOW.md`'s Kanban board as a new
  entry condition on the `IN PROGRESS` column (see that file's
  update).
- Reuses `AGENTS/Ideation/AGENT.md`'s questioning discipline directly
  by reference — this file does not restate or fork it.
