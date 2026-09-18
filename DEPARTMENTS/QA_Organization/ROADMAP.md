# Roadmap

This document exists so that anyone picking up this repository — a human who
wasn't in the original conversation, or a different agent entirely — can
understand what has been built, what is deliberately still missing, and what
order the remaining work is supposed to happen in, without needing any prior
context. It is written in prose on purpose, not as a checklist, because a
checklist tells you what happened but not why it happened in that order, and
the order is the part that matters most here.

## Where we are: V0, the organization itself

The current phase, V0, is entirely about defining the organization before
attempting to make it clever. Everything in this repository right now —
the constitution, the fifteen-stage execution engine, the capability pool
concept, the handoff package template, and the versioned history model — is
the fixed skeleton that every future audit will run inside. None of it is
about actually improving itself yet. The reasoning behind that sequencing is
explained at length in HISTORY/DESIGN_DECISIONS.md, but the short version is
that a self-improving system needs something stable to improve, and you
cannot know what is worth preserving in a system you haven't finished
defining. V0 is complete when a real product can be handed to this
organization, run through all fifteen stages, and produce a QA verdict with
full evidence and a working diagnostic index — even if the organization
itself hasn't been proven trustworthy yet by repeated use. Proving
trustworthiness is a separate, later milestone, not part of what V0 promises.

## V0.1: one worker, a small initial set of capabilities

Once the organization itself exists, the next phase puts a single worker
through the entire pipeline against one real product, using a deliberately
small set of testing capabilities rather than trying to cover every domain
at once. The five capabilities chosen for this phase are Playwright-based
functional and exploratory web testing, API testing, k6 for load and scale
testing, a security baseline built from OWASP ZAP and Trivy or Grype, and
axe-core for accessibility hygiene. These were chosen because mature,
actively maintained open-source tools already exist for each of them, so the
work in this phase is building thin adapters that translate their output
into this organization's evidence and disposition format, not building
testing engines from scratch. The point of this phase is to find out where
the organization itself breaks under real use — a stage contract that turns
out to be too vague, an evidence field that's missing something a real
finding needed, a disposition rule that doesn't cover a situation that
actually came up. Those discoveries get fed back into V0 as corrections, not
treated as excuses to add more process on top.

## V0.2: benchmarking the organization against what already exists

After the organization has been run for real, the next phase compares it
deliberately against other QA systems and methodologies, open-source or
commercial, to find out honestly what they do that this organization
doesn't, whether that difference can be verified rather than just asserted,
what adopting it would improve, and what it might weaken. The market research
already done as part of building V0 — the survey of test-management tools,
execution frameworks, AI-native testing agents, and the handful of
open-source multi-agent QA projects that were checked for authenticity
before being trusted — feeds directly into this phase rather than needing to
be redone. The output of this phase is a written improvement proposal, never
a silent adoption; nothing about the organization changes until a human
reviews and approves that proposal.

## V0.3: adding capabilities deliberately

In parallel with or after V0.2, new testing tools or repositories can be
evaluated as candidate capabilities. Each candidate is checked for whether it
provides something genuinely new or overlaps with a capability already in
the pool; overlapping candidates get benchmarked against the incumbent
before any decision is made, and every addition is versioned so a previous
capability version is never simply lost when a new one is adopted.

## V0.4: formalizing how the organization evolves itself

Only once V0 has been proven and V0.2 and V0.3 have happened at least once
for real does it make sense to formalize the evolution loop itself as a
repeatable mechanism: discover, analyze, benchmark, identify the gap or
improvement, propose the change, obtain human approval, run the new version
against the historical archive of past audits as a conformance check, adopt
it as a new organization version, and preserve everything that came before
it. This phase turns something that was done manually in V0.2 and V0.3 into
a defined, repeatable procedure. It is explicitly not being built now,
because building the mechanism for change before the thing being changed has
been proven would mean guessing at what needs to be preserved.

## V0.5: multi-worker, only if evidence demands it

A previous attempt at this organization jumped straight to multiple
coordinating agents before a single audit had ever been completed, and it
produced a large amount of coordination machinery and no finished QA work.
This roadmap deliberately places multi-worker experimentation last, and
makes it conditional: it only gets built if, after real use, there is
concrete evidence that one worker executing the capability pool in sequence
is an actual bottleneck — for parallelism, isolation, or genuine domain
specialization — rather than an assumed one. If one worker turns out to be
sufficient, it stays that way permanently, and multi-worker execution
remains an optional variant rather than a requirement.

## V1: an enduring organization

The end state this roadmap is building toward is not a fixed, finished
piece of software but a versioned, evidence-driven organization that can
test real products, deliberately acquire new capabilities, evaluate
competing QA approaches on their merits, propose improvements to its own
rules, obtain a human's approval before adopting any of them, and do all of
this without ever losing the history of how it got there. There is no phase
after V1 in the sense of a finish line; the organization is expected to keep
evolving for as long as it's used, governed by the same constitution and the
same evidence discipline that V0 established.

## What this roadmap is not

This roadmap is not a promise about the calendar. It is intentional about
order, not about duration — building V0 is fast because it's disciplined
documentation and schema work; proving it in V0.1 takes as long as running
a real audit against a real product honestly takes; and V0.2 through V0.4
depend on real usage cycles that cannot be compressed by writing faster.
Anyone extending this roadmap should add detail to a phase without
collapsing the sequence — do not start V0.4's evolution engine before V0.1
has actually been run against a real product, no matter how tempting it is
to build the more interesting piece first.
