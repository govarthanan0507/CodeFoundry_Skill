# Pre-Planning — V1 (Completed)

## Purpose

Before an idea is treated as a product — before any PRD exists — Pre-Planning answers one question honestly: **does this deserve real investment, and what would it actually take?** Nothing downstream starts until this stage produces a decision, and "no" or "not yet" are both legitimate outcomes, not failures of the process.

## Entry condition (required — this stage does not start without it)

Pre-Planning requires `idea.md` (per `AGENTS/Ideation/AGENT.md` section 12)
at completion state `CLEAR` or `CLEAR WITH OPEN ITEMS`.

```text
idea.md status?
    ├── CLEAR / CLEAR WITH OPEN ITEMS → Pre-Planning may start.
    │                                   Any open items carried in
    │                                   idea.md are inherited as
    │                                   Pre-Planning's own open items,
    │                                   not silently dropped.
    │
    └── BLOCKED or idea.md missing    → Pre-Planning does not start.
                                         Returns to Ideation (or the
                                         human, if Ideation itself is
                                         stuck) — the Orchestrator must
                                         not carry the conversation
                                         forward informally as a
                                         substitute for a real
                                         handoff artifact.
```

This closes a gap found by direct review: Pre-Planning previously had
no defined entry check, meaning it could start on whatever was in the
conversation regardless of whether Ideation had actually finished. This
rule is why that no longer happens — everything Pre-Planning starts from
must trace to `idea.md`, not to unstructured conversational carryover.

## Fast-path — personal/hobby/experimental ideas still go through Pre-Planning

A hobby, personal-use, or purely experimental idea is **not skipped**.
It still goes through this stage — but Pre-Planning is the one that gets
to say "the full investment debate isn't needed here," using
`idea.md`'s own personal/experimental/commercial context field as its
starting signal, not a decision made upstream in Ideation or by the
Orchestrator on Pre-Planning's behalf.

```text
idea.md's personal/experimental/commercial context says:
personal / hobby / "just so I don't have to pay for X" / no stated
intent to distribute or compete
        ↓
Pre-Planning still convenes, but runs the ABBREVIATED path:
  - Market/Research still runs the reuse/OSS check (this never skips —
    see REUSE_AND_LICENSE_RULE.md — a hobby project still shouldn't
    reinvent something that already exists)
  - Advocate/Skeptic/Feasibility's full investment debate is not
    required; the Synthesizer may issue GO directly, with reasoning
    stated as: "personal/hobby scope — investment debate not
    warranted at this scale"
        ↓
GO (fast-path), decision package still produced (this rule doesn't
skip the artifact, only the debate depth) → Planning
```

If, instead, `idea.md` signals commercial intent, competitive ambition,
or the user is explicitly unsure — the full four-role debate runs as
normal. And if a fast-pathed hobby project's intent later changes (the
user asks "should I actually try to sell this"), the Orchestrator's
intent-change re-entry trigger (`AGENTS/Orchestrator/AGENT.md`) brings it
back through this same stage, this time without the fast path, carrying
forward the actual current build as evidence.

## Four agents, not a rubber stamp

Four distinct voices, each with a real, separate job — not four flavors of the same opinion:

1. **Advocate** — makes the strongest honest case *for* building this: the real user value, why now, why this beats existing alternatives.
2. **Skeptic** — makes the strongest honest case *against*: what already solves this, why it might not be worth the effort, what could make it fail.
3. **Feasibility & Cost Assessor** — answers "can this actually be built, and what would it cost at scale?" — rough technical feasibility, and if this were to grow (real users, real infrastructure), what that would cost. This is the piece that answers your "how much money would I need at scale" question directly.
4. **Market/Research** — checks what already exists (competitors, OSS candidates via Repo Analyzer where relevant), so the Advocate and Skeptic aren't arguing from assumption.

## The debate

Same mechanism already proven in `COUNCILS/Design-Council/DEBATE_PROTOCOL.md`, applied one stage earlier: Advocate and Skeptic argue with the Market/Research findings and the Feasibility/Cost Assessor's numbers as their evidence, not opinion. A Synthesizer function resolves the debate into one of three outcomes — reusing the same three-outcome logic already tested in the Design Council, not inventing a fourth:

```text
GO
  The idea deserves Planning. Reasoning and evidence recorded.

NO-GO
  Doesn't deserve investment right now, with the specific reason
  stated (already solved better elsewhere, cost/effort doesn't
  match value, etc.) — never a vague "not sure."

NEEDS MORE EVIDENCE
  Genuinely undecidable with what's known — names exactly what
  evidence would resolve it, rather than guessing either direction.
```

## What this produces

A **Pre-Planning decision package** — this is the BRD-equivalent content referred to elsewhere in this system, not a separate document: the case for/against, the market/OSS findings, the feasibility and at-scale cost estimate, and the GO/NO-GO/NEEDS-MORE-EVIDENCE verdict with reasoning.

## Human gate

The package goes to the human. **Until this gate passes, the idea is not a product** — this is stated explicitly per your instruction: no PRD, no epics, no tickets exist yet at this stage. A GO here is what actually starts Planning.

### How the verdict is actually presented — a conversation, not a document dump

The four full documents and `DECISION_CONTRACT.md` exist and are
real (per the Hard Rule above) — but they are not what gets put in
front of the human first. What's presented is short and plain:

```text
Verdict: GO | GO (fast-path) | NO-GO | NEEDS MORE EVIDENCE
<one or two sentences, in plain language, on why — no jargon dump,
 no restating every section of every document>
```

The human is then the idea's own advocate at this point — not a
passive approver reading a report. They respond, push back, add
context the four roles didn't have, or argue for the idea directly.
This is expected, not an edge case to route around: `AGENTS/Ideation/
AGENT.md`'s own discipline (plain conversation, one thing at a time,
no form-filling) applies here too, not just at intake.

**The verdict can genuinely change from this exchange.** If the
human's response changes the Synthesizer's own reasoning, the
Synthesizer revises the verdict — recorded as a new, dated entry in
`DECISION_CONTRACT.md` that references what changed and why, per
`SHARED/DOCUMENT_GOVERNANCE.md`'s supersede-don't-overwrite rule (the
original verdict and reasoning stay visible, not deleted). This is
not the human overriding Pre-Planning by authority — it's new
evidence entering the same debate the four roles already ran, same as
any other material fact changing an assessment.

Only once this settles — the human accepts the (possibly revised)
verdict, explicitly, not by silence (per this system's standing
"silence is never approval" rule) — does the gate actually pass. A
`GO` settled this way is what the Orchestrator then routes into
Planning, per the Hard Rule's enforcement above. The full four
documents remain the actual record (linked, referenced, available to
read in full) — the conversation is how the verdict reaches the human,
not a replacement for what backs it.

## Hard rule — no product progression without all four documents

This is a hard rule, not a stage-internal preference: **if any of the
four required documents (`templates/MARKET_RESEARCH_TEMPLATE.md`,
`templates/FEASIBILITY_REPORT_TEMPLATE.md`,
`templates/BUSINESS_CASE_TEMPLATE.md`, `templates/PRE_MORTEM_TEMPLATE.md`)
does not exist, or exists with an incomplete section per
`DECISION_CONTRACT.md`'s completeness gate, the product does not
progress past Pre-Planning — at all, for any reason.** This applies
regardless of tier, regardless of fast-path, and regardless of how
urgent the project feels. A fast-path GO still requires all four
documents, fully populated per their fast-path rules — "fast-path"
narrows what's argued inside each document, it never excuses a document
from existing.

This is enforced twice, not once, so it can't be bypassed by any single
point of failure:

1. **Internally**, by `DECISION_CONTRACT.md`'s completeness gate — the
   Synthesizer itself cannot issue a verdict without all four.
2. **Externally**, by the Orchestrator — before routing a project into
   Planning (or re-entering Design Council on an intent-change), the
   Orchestrator checks for all four documents at completeness
   independently of whatever verdict Pre-Planning reported. A `GO`
   verdict with a missing or incomplete document is treated as invalid,
   not as a `GO` to honor — see `AGENTS/Orchestrator/AGENT.md`'s gate
   enforcement rule. This exists because a stage's own self-report is
   exactly the kind of unverified claim this whole system has already
   learned not to trust on its own word (the same reasoning behind
   Design Council's Independent Critic, and QA's rule that a builder's
   own "SUCCEEDED" is never sufficient by itself).

## Relationship to Planning

Pre-Planning answers "should we." Planning (next stage) answers "how, specifically" — where the specialist discovery questioning happens (UX, Frontend, Backend specialists asking natural-language questions per `AGENTS/Ideation/AGENT.md`'s discipline) and where the PRD/TRD actually get written. Pre-Planning does not do Planning's job; it only decides whether Planning is warranted at all.
