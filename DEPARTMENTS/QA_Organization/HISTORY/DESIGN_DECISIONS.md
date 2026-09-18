# Design Decisions

This document exists for one reason: Constitution §18 (Succession) requires
that a future maintainer — human or a different agent entirely — be able to
understand why this organization is built the way it is, without access to
the conversation that produced it. Nothing here should be treated as
optional context; if a rule in `CONSTITUTION.md` or `ENGINE/` looks
arbitrary, its reasoning is below.

## Why this exists at all

The organization was built after a prior, simpler QA setup failed in a
specific, diagnosable way: an independent test agent was handed a product
and 23 comparison projects to benchmark against. It didn't clone or run
them, judged that too time-consuming, and silently dropped the entire
benchmarking obligation from its report. The report otherwise looked
complete. Nobody could tell benchmarking had been skipped without already
knowing to ask. That single incident is the reason Constitution §3
(mandatory disposition, no silent skipping) exists, and the reason
`ENGINE/STAGE_CONTRACTS.md` Stage 10 explicitly forbids dropping a
comparison instead of recording it `BLOCKED`.

## Why a fixed procedure instead of a smart prompt

The first instinct was to write better instructions — "perform
comprehensive, industry-standard QA" — and trust a capable model to fill in
the right process. That's precisely what failed above: a smart-sounding
instruction gives a model room to decide something is "close enough" or
"not worth the effort," and there's no way to audit that decision after the
fact because it was never forced to be explicit. The fix is not a smarter
prompt; it's removing the model's latitude to invent the workflow at all.
`ENGINE/STAGE_CONTRACTS.md` exists so the model's job at any moment is
narrow and checkable — read one stage's contract, satisfy it, stop — rather
than holding an entire QA philosophy in its head and hoping it applies it
consistently. This is also why state lives in `QA_STATE.json` and checkpoint
commits rather than in conversational memory: a small model, or a model
mid-crash-recovery, needs to be able to resume from the repository alone.

## Why the multi-agent coordination approach was abandoned

An earlier version of this repository tried to solve rigor by adding
*process around multiple agents* — a GitHub-issue-driven coordination
controller, a phase work registry, claim/start/submit-review/accept state
machines, an orchestrator role. It produced real, working coordination
machinery (branch protocols, audit logs of state transitions, authority
checks) and zero completed product audits. The effort went entirely into
making agents cooperate with each other, not into testing anything. This is
why Constitution §15 defaults to one worker, and why multi-worker execution
is explicitly gated behind evidence of a real bottleneck (`EVOLUTION.md`)
rather than adopted because it seems more sophisticated. The lesson
generalizes: this organization has a repeating failure mode of designing an
impressive meta-system in place of doing the actual QA work, and it
recurred a second time even during this rebuild (see "the capability-map
scope check" below). Anyone extending this organization should treat "am I
building infrastructure instead of running an audit" as a standing question
to ask, not a one-time lesson already learned.

## Why the constitution has a disposition mandate at all

Coverage was originally going to be judged by test count ("74 tests, 14
adversarial tests — is that enough?"). The answer to that question is
unknowable from a count alone. What's knowable is whether every identified
risk area reached an explicit disposition. Constitution §4 (coverage is
risk-driven) and §3 (mandatory disposition) exist together for this reason
— a test count is not evidence of thoroughness, and reporting one as if it
were is itself a documentation failure.

## Why the Diagnostic Index is mandatory, not a nice-to-have

The actual measure of success this organization was designed against is:
given a production error message months after release, can you find the
right place to fix it, and can you tell whether QA already knew about the
regime that broke? A QA report organized purely by test stage doesn't
answer that — you'd have to read the whole archive to find out. The
Diagnostic Index (Constitution §6, schema in
`HANDOFF_PACKAGE_TEMPLATE/schemas/DIAGNOSTIC_INDEX.schema.json`) inverts the
organization: indexed by verbatim error signature and component, so a
production incident resolves to exactly one of three honest answers — a
known finding with a fix status, a known limitation/accepted risk that was
knowingly shipped, or a boundary condition production exceeded that QA never
tested. There is deliberately no fourth outcome where the archive has
nothing to say.

## Why Stage 8 (Non-Functional/Scale) and Stage 9 (Observability) were added
## to the original 13-stage design

The original stage list (intake through final audit) had no dedicated
performance/load/scale stage and no check on whether the product could even
be diagnosed in production. Both are the two most common causes of "worked
in QA, broke at scale" and "broke in production and nobody could tell why."
Functional testing proves a feature works once, for one user — it says
nothing about 100x traffic or sustained load. And no amount of QA
documentation helps trace a real incident if the product itself doesn't log
or emit metrics sufficient to diagnose the failure — which is why
insufficient observability is scored as a `FAILED` finding on the product,
not waved through as a testing gap.

## Why security is a separate, deferred boundary rather than a QA capability

Security testing is adversarial by design — actively trying to break in —
while QA's default posture (Constitution §8, Safety) is controlled,
non-destructive verification. Folding deep security testing into QA either
weakens QA's safety discipline or waters security down into a checklist.
Real organizations keep these functions separate for the same reason
internal QA and external penetration testing are kept separate: the
independence that makes a security review valuable is lost if the same
worker that already declared the functional tests passing is also the one
deciding security is fine. Constitution §10 and `CAPABILITIES.md`'s
security-baseline capability exist to make this boundary explicit rather
than quietly overclaimed — QA does baseline hygiene (secrets, transport
security, known-critical CVEs) and records deep security testing as
`DEFERRED — Security Organization not yet built`, never as `PASSED`.

## Why capabilities are adapters around existing tools, not custom-built

Market research conducted while designing this organization (see below)
confirmed that mature, actively maintained open-source tools already exist
for every domain in the V0.1 capability set — browser automation with
self-healing and accessibility scanning, API testing, load testing with
built-in pass/fail thresholds, DAST and dependency scanning. None of them
provide the organizational layer this repository defines (disposition
discipline, diagnostic index, versioned governance, human-approval
boundaries) — that gap is real and is what this organization actually
builds. But rebuilding test-execution engines that already exist and work
would be wasted effort. `CAPABILITIES.md` capabilities are therefore thin
adapters translating an existing tool's native output into this
organization's evidence schema, not reimplementations.

## The market research episode, and why it matters for how this
## organization should treat any future research input

Two research batches were produced during this organization's design,
handed over as apparently authoritative competitive analysis. The first
listed eight "competitive" multi-agent QA architectures with precise
confidence percentages (84%-96%). On verification, three were real
projects (Agentic QE Fleet, CheckAgent, Agentic Test Explorer) and five
could not be found under any of their claimed names or architectures
despite targeted searching (QAForge, a 16-agent "Test-Agent," a 29-agent
"Open-Testing.AI," and specific "Argus"/"Sentri" architectures that don't
match any real project by those names). A second batch was mostly
accurate — three of four specific claims verified as real projects, one
close-but-misnamed. The lesson recorded here deliberately, because it's
exactly the failure mode this whole organization exists to prevent: a
confidently precise, well-formatted research artifact is not evidence
merely because it looks authoritative. `EVOLUTION.md`'s verification
discipline (four explicit questions before any adoption proposal) exists
because of this episode, not as a hypothetical precaution.

## Why a 50-category market capability map was not built as part of V0

Comprehensive market research surfaced roughly 50 testing categories and
600+ named tools. The temptation was to build a full capability map across
all of them before running a single real audit — which would have been the
same over-engineering pattern (see above) wearing a research-shaped
disguise. The decision made instead: capability selection happens
just-in-time, per product, at Stage 2 (Reconnaissance) — a product doesn't
need mobile, SAP, or Salesforce testing capabilities mapped out before it's
ever needed. The V0.1 capability set was deliberately kept to five domains,
chosen because they had verified, adoptable open-source tools and covered
the specific concern (scaling failures, traceability) that motivated this
whole project. The capability map is meant to grow organically with real
usage, not be front-loaded speculatively.

## Why the release decision never belongs to QA

Constitution §9 and `LIFECYCLE.md`'s three-repo boundary both encode this:
QA reports a verdict and every open risk; a human (the product owner)
decides whether to ship. This was a deliberate choice to prevent QA from
either being blamed for a business risk-acceptance decision it didn't make,
or quietly absorbing that authority by reporting a diluted "mostly fine"
verdict instead of an honest, uncomfortable one. An accepted risk is
recorded as a named human decision (`risk-acceptance/` per `LIFECYCLE.md`),
never disguised as a QA `PASSED`.

## Why "challenge, don't comply" is a constitutional principle (§11)

An organization — QA or otherwise — that only ever agrees with the person
who built or owns the product isn't providing independent verification,
it's providing reassurance. This principle was added specifically because
the broader ambition behind this project includes a Developer Organization
and eventually a Security Organization, both of which are expected to
advise and challenge their operator rather than simply execute requests.
QA is the first instance of that pattern and sets the precedent: evidence-
backed disagreement is a required output, not friction to be smoothed away.

## Open questions intentionally left unresolved in V0

- **Production-repo promotion mechanism.** `LIFECYCLE.md` states that
  neither the developer nor QA agent promotes to the Production Repo, but
  the exact promotion mechanism (human action vs. an automated gate keyed
  to QA's verdict) is not yet specified. Resolve this before attempting a
  real release through this pipeline.
- **Whether a Developer Organization gets built at all, and how heavy.**
  The working assumption is: build it much lighter than QA (a disciplined
  handoff-contract format, not a mirrored 15-stage engine), because
  functional development tooling already has abundant market options and
  QA was judged the higher-value, higher-risk piece to get right first.
  This was a direction agreed on, not something implemented in this
  repository.
- **Whether/when a dedicated Security Organization gets built.** Deferred
  entirely; QA's baseline-only boundary (Constitution §10) is meant to make
  the gap visible in every audit until this is addressed, not to quietly
  cover for its absence.
