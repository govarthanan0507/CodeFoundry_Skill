# Pre-Mortem — Template (Skeptic)

Produced by: Skeptic role (`roles/Skeptic.md`). Always created — see
"Fast-path" below. Never omitted.

Uses the pre-mortem framework (assume it already failed, work backward
to causes) rather than a balanced SWOT grid, since the Skeptic is
already arguing one honest side of the debate, not producing a neutral
four-quadrant summary.

## Header (always filled)

- Project / idea reference (`idea.md` link)
- Date
- Path taken: **FULL** or **FAST-PATH**
- If FAST-PATH: reason (same signal named across the other three
  templates for this project)

## Fast-path rule

All sections below are still present. Each is filled with:
`Not argued in full — [reason from Header]. The "already solved"
check below still runs even on fast-path, since a hobby project
duplicating an existing free tool is still worth flagging.`

## Sections (full path)

### 1. Already-solved check
What existing product or informal workaround (per
`MARKET_RESEARCH_TEMPLATE.md` §3/§6) already covers this need, and how
well — named specifically, per `roles/Skeptic.md` Rule 1.

### 2. Effort/value mismatch
Whether the cost of building (per `FEASIBILITY_REPORT_TEMPLATE.md`) is
actually justified by the value the Advocate claims — stress-tested,
not restated.

### 3. Cause of death (pre-mortem)
Assume this project already failed. State the specific, plausible cause
— not a generic risk. Break into: what would kill it during building,
what would kill it after shipping (if shipping is in scope for this
project).

### 4. Red-flag / early-warning indicators
Specific, observable signs that the "cause of death" above is starting
to happen — so it can be caught early rather than only diagnosed in
hindsight.

### 5. Concessions
Any Advocate point the Skeptic found actually correct (per
`roles/Skeptic.md` Rule 3 and its Escalation duty) — same anti-theater
check as the Business Case's §5.
