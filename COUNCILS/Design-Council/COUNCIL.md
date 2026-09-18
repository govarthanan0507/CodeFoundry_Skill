# Design Council — V1

## Why this is the heart of CodeFoundry

Every other stage depends on this one being right. Ideation can be vague and get refined. Pre-Planning can be wrong and get re-argued. But if the Design Council makes a bad call, Development builds the wrong thing correctly, QA verifies the wrong thing works, and the mistake is only found in production. This council carries more consequence per decision than any other stage, which is why its members are defined as senior-level judgment, not junior task-followers.

## Mission

Take the approved product and planning package and decide exactly how the product should be shaped and built — then remain the accountable authority for that decision through Development, not just its author.

## Membership (7 senior roles)

1. `roles/architect.md` — System/Product Architect
2. `roles/ux-designer.md` — UX Designer
3. `roles/ui-designer.md` — UI/Visual Designer
4. `roles/frontend-architect.md` — Frontend Architect
5. `roles/backend-architect.md` — Backend/API Architect
6. `roles/data-architect.md` — Data/Database Architect
7. `roles/security-architect.md` — Security/Reliability Architect

Each role file defines: what a genuinely senior person in that discipline is evaluated on, what they own, what they must not decide (another role's territory), and their escalation duty after handoff.

## What makes a role "hardened"

A hardened role definition is not a longer prompt. It is:

- A real seniority bar — the role file states what separates senior judgment from junior output in that discipline, so the role isn't just "produce an architecture document" but "produce the architecture a senior architect would defend under questioning."
- A named boundary — exactly what this role does not decide, so disagreement has somewhere real to go instead of one role quietly overruling another.
- An escalation duty — the role stays responsible after handoff. See "Post-handoff accountability" below.
- A rule against fashion-driven or habit-driven decisions — every non-trivial choice states its reasoning, not just its conclusion.

## Before any of this — does the Council even convene?

See `../PROCESS_SCALING.md` first. Not every task warrants the full 7-role Council — that file defines objective triggers (new architecture, security-sensitive surface, domains touched, Hard Constraint categories in play) that determine whether this is a Tier 1 (solo/pair), Tier 2 (small crew, 2-4 relevant roles), or Tier 3 (full Council) task. Everything below in this file describes Tier 3. Convening the full Council for a Tier 1 task is the same over-scoping failure this project was flagged for on day one.

## Inherited evidence from Ingestion (Mode B — existing code)

If this project entered through `AGENTS/Ingestion/AGENT.md`'s Mode B
(an existing codebase, not a from-scratch idea), a `CODE_DIGEST.md`
exists alongside `idea.md` — found architecture, found tech choices,
found functional behavior, extracted from the actual code. This is
evidence for the debate below, a strong starting candidate for
`TRD.md`'s architecture section — it is never auto-adopted as if the
Council had already decided it. Existing code can encode a wrong
choice or old debt as easily as a good one; the debate still runs, and
a `CODE_DIGEST.md` finding is confirmed or revised through it, same
scrutiny any other proposed decision gets.

## Discovery — before any of this, per story, just-in-time

The debate below decides architecture/epic-level design. Individual
user stories are elaborated separately and later, one at a time, right
before each is pulled into active development — see
`DISCOVERY_PROTOCOL.md`. Do not read this file as the Council's only
point of contact with the user; Discovery is the other one, scoped
narrower and running continuously as stories are picked up rather than
once at epic handoff.

## Pre-handoff: the mandatory debate

See `DEBATE_PROTOCOL.md`. The Council does not hand off a design that hasn't been argued over by its own members first. Before debate begins, the Council also loads `HARD_CONSTRAINTS.md` — categories of decision (money, data privacy, irreversible operations, security exposure, licensing, vendor lock-in, autonomy scope, branding, new dependencies, user-facing commitments, deadlines, platform support, operational capacity) that route to the human regardless of how confident any role is. This is a pre-check, not part of the debate itself: it determines whether a decision was ever the Council's to make.

## Design output — two named documents, not one undifferentiated package

Per the industry BRD → PRD → FRD → TRD hierarchy this system already
follows (Pre-Planning = BRD-equivalent, Planning/Product Owner =
PRD), Design Council produces the next two, as separate, explicitly
labeled documents — not a single bullet list a reader has to mentally
sort into "what" versus "how":

**`FRD.md`** (Functional Requirements — what the system does,
observable behavior, still technology-agnostic):
- UX flows and interaction states
- UI/visual direction and design system reference
- functional behavior per work unit (what happens, from a user's
  view, screen by screen or flow by flow)
- acceptance criteria per work unit (traces back to Product Owner's
  originals — this restates them in system-behavior terms, it does
  not re-invent them)
- design risks and unresolved issues, explicitly — not smoothed over

**`TRD.md`** (Technical Requirements — how it's actually built):
- architecture overview and decisions, with tradeoffs and rejected
  alternatives
- **API contract SHAPE** — endpoints, boundaries, what's exposed to
  the frontend versus kept internal — decided here, by the Backend/API
  Architect negotiating with the Frontend Architect
  (`roles/backend-architect.md`). This is the contract's *shape*; the
  concrete formal spec (an actual OpenAPI/schema document, validated
  and lint-checked) is produced downstream by the Backend Developer
  worker against this shape, per
  `DEPARTMENTS/Developer_Organization/CAPABILITIES/Backend-Developer/API_CONTRACT.md`'s contract-first
  discipline — the worker formalizes the decision, it does not decide
  the boundaries itself. Two different levels of the same artifact,
  not two independent authorities.
- frontend structure and its API integration pattern
- data model, database technology decision and reasoning (see
  `roles/data-architect.md`, consulting `TECH_REFERENCE_LIBRARY.md`)
- security and reliability considerations
- integration points, environment, hosting/platform decision
  (consulting `TECH_REFERENCE_LIBRARY.md`), and deployment assumptions

Both documents together are what a story's Discovery/debate output
(`DISCOVERY_PROTOCOL.md`, `DEBATE_PROTOCOL.md`) resolves to at the
epic/architecture level; a single story's own scoped decision
(Discovery's `DISCOVERY.md`) is the same shape at a narrower grain and
references back into whichever of these two documents already covers
its epic, rather than re-deciding shared ground per story.

## Human gate

The design package goes to the human gate before Development starts. Silence is never approval (per CodeFoundry's global gate rule). Unresolved risks stay visible in the package even after approval unless explicitly accepted.

## Post-handoff accountability — guiding Development and fixing errors

The Council's authority does not end at handoff. This is the mechanism you asked for explicitly:

```text
Development hits a conflict, impossibility, or discovers the design was wrong about something
        ↓
Development files a CHANGE REQUEST naming:
  - which role's domain this falls under
  - what was expected vs. what was found
  - why Development cannot safely resolve this itself
        ↓
The relevant Council role (not the whole Council, unless the issue crosses domains)
investigates and either:
  (a) clarifies — the design was right, Development misunderstood it, OR
  (b) revises — the design was wrong, issue a corrected decision with reasoning, OR
  (c) escalates — this requires a new human gate (cost, scope, or risk changed materially)
        ↓
Development resumes against the clarified/revised decision
```

Rules:

- Development must not silently redesign around a discovered problem. That's how the "hard harness" from the blueprint breaks down in practice.
- A Council role that gets repeated change requests in its domain is a signal the original design was under-baked, not that Development keeps getting it wrong — the Council should treat a pattern of change requests as feedback on its own work, not a nuisance to swat down.
- Every change request and its resolution is recorded, not resolved in an ephemeral conversation and forgotten. This is what "guide the development team when errors come up" means in practice: a traceable decision, not a one-off Slack-style answer.
