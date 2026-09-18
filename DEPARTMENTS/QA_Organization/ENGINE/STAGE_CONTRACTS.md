# Stage Contracts

Each stage below is a machine-checkable contract: what must go in, what must
be done, what must exist afterward, what allows moving on, what disposition
values are legal, and the checkpoint requirement. A worker's job at any
point is to read exactly one of these sections, satisfy it, and stop —
never to reason about the whole audit at once.

Every stage shares these non-negotiable fields (Constitution §3, §7):
`MUST_RECORD` always includes verbatim command/output where applicable, and
`CHECKPOINT` always means: commit the stage's artifacts to the QA Repo and
append an entry to `QA_STATE.json.stage_history` before moving to the next
stage. A stage is not complete until both have happened.

---

### STAGE 0 — INTAKE

**INPUT:** QA contract (this repository), `HANDOFF_PACKAGE/` from the
developer.

**MUST_DO:** Read `CONSTITUTION.md` and `LIFECYCLE.md`. Create the QA Repo
subtree for this cycle (`HISTORY/{cycle_id}/`). Acquire the exact product
snapshot named in the handoff package — not "the latest," the exact
commit/version specified. Verify it matches what the handoff manifest
claims.

**MUST_CREATE:** `HISTORY/{cycle_id}/product-snapshot-manifest.json`,
initialized `QA_STATE.json`.

**MUST_RECORD:** source repo, exact commit/version, who authorized this
handoff, acquisition timestamp, hash/checksum of the acquired snapshot.

**EXIT_CONDITION:** the acquired snapshot's identity is verifiable against
the handoff manifest.

**ALLOWED_OUTCOME:** `PASSED`, `BLOCKED` (handoff manifest missing/invalid,
snapshot doesn't match claim).

**CHECKPOINT:** required.

---

### STAGE 1 — ENVIRONMENT QUALIFICATION

**INPUT:** acquired product snapshot, environment requirements from
`HANDOFF_PACKAGE/02_EXECUTION_PROTOCOL.md`.

**MUST_DO:** Verify dependencies resolve, the product builds/runs in the QA
environment, and the QA environment is isolated from production and from
the developer's other repositories (Constitution §1).

**MUST_CREATE:** `environment-qualification.md` recording exact versions of
every dependency, OS/runtime, and isolation boundaries confirmed.

**MUST_RECORD:** every command run to qualify the environment, verbatim
output, any deviation from what the handoff package specified as required.

**EXIT_CONDITION:** product builds/runs; isolation confirmed.

**ALLOWED_OUTCOME:** `PASSED`, `BLOCKED` (cannot build/run, or isolation
cannot be established).

**CHECKPOINT:** required.

---

### STAGE 2 — RECONNAISSANCE

**INPUT:** qualified environment, product source/build.

**MUST_DO:** Inventory architecture and components. Cross-reference against
`CAPABILITIES/CAPABILITIES.md` and decide which capabilities apply to this
product — record the decision and the reasoning, not just the list.

**MUST_CREATE:** `product-inventory.json` (components, interfaces,
dependencies), `applicable-capabilities.json`.

**MUST_RECORD:** for every capability in the pool, `APPLIES` or
`NOT_APPLICABLE` with a one-line reason — this is itself a disposition set,
not a free-text summary.

**EXIT_CONDITION:** every capability in the pool has an explicit
applicability decision.

**ALLOWED_OUTCOME:** `PASSED`, `BLOCKED` (product cannot be inventoried —
e.g., source inaccessible despite Stage 0 passing).

**CHECKPOINT:** required.

---

### STAGE 3 — RISK MODEL & STRATEGY

**INPUT:** `product-inventory.json`, `applicable-capabilities.json`.

**MUST_DO:** For every component, identify failure modes, severity,
detectability, and whether/how it will be tested. This register is what
Stage 13 (coverage) will later check every entry against — it must be
complete now, not amended silently later.

**MUST_CREATE:** `risk-register.json`, `test-strategy.md`.

**MUST_RECORD:** per risk entry — `risk`, `affected_component`, `severity`,
`test_required` (yes/no + which capability), `reason`.

**EXIT_CONDITION:** every component from Stage 2's inventory has at least
one risk entry, or an explicit `NOT_APPLICABLE` with reason.

**ALLOWED_OUTCOME:** `COMPLETE`, `BLOCKED`.

**CHECKPOINT:** required.

---

### STAGE 4 — TEST DESIGN

**INPUT:** `risk-register.json`, `test-strategy.md`.

**MUST_DO:** Write literal, re-runnable test cases per applicable
capability. For every test, specify the boundary conditions it exercises
(scale, concurrency, data volume, environment) explicitly — not left
implicit (Constitution §2).

**MUST_CREATE:** `test-cases/{capability}/*.json` (or the capability's
native format, referenced here), each including `tested_at` boundary fields.

**MUST_RECORD:** mapping from each risk-register entry to the test case(s)
that cover it.

**EXIT_CONDITION:** every `test_required: yes` entry in the risk register
has at least one corresponding test case.

**ALLOWED_OUTCOME:** `COMPLETE`, `BLOCKED`.

**CHECKPOINT:** required.

---

### STAGE 5 — FUNCTIONAL EXECUTION

**INPUT:** test cases tagged as functional per capability.

**MUST_DO:** Execute. Capture verbatim output, not paraphrase.

**MUST_CREATE:** `evidence/functional/{test_id}.json` per
`HANDOFF_PACKAGE_TEMPLATE/schemas/EVIDENCE.schema.json`.

**MUST_RECORD:** command/procedure, expected result, observed result
(verbatim), boundary conditions actually exercised, disposition.

**EXIT_CONDITION:** every functional test case has a disposition.

**ALLOWED_OUTCOME:** `PASSED`, `FAILED`, `BLOCKED`, `NOT_APPLICABLE`,
`DEFERRED` — per test case. On `FAILED`, proceed to Stage 12's reproduction
requirement before Stage 13 can close.

**CHECKPOINT:** required.

---

### STAGE 6 — ADVERSARIAL / NEGATIVE / BOUNDARY

**INPUT:** test cases tagged adversarial/boundary per capability.

**MUST_DO:** Execute malformed-input, invalid-state, and boundary-value
cases.

**MUST_CREATE / MUST_RECORD:** same shape as Stage 5, tagged `adversarial`.

**EXIT_CONDITION:** every adversarial/boundary test case has a disposition.

**ALLOWED_OUTCOME:** same five-value set, per test case.

**CHECKPOINT:** required.

---

### STAGE 7 — PERSISTENCE / RECOVERY / REGRESSION

**INPUT:** persistence/recovery test cases; findings from any prior cycle
in `HISTORY/` for regression comparison.

**MUST_DO:** Test restart/crash-recovery. If the product has backups,
**perform an actual restore and verify it**, not just confirm a backup file
exists (Constitution §2 — an untested restore is an assumption, not
evidence). Re-run tests tied to any prior cycle's findings for regression.

**MUST_CREATE:** `evidence/persistence-recovery/*.json`,
`regression-results.json` (only if a prior cycle exists).

**MUST_RECORD:** explicit restore-verification result; regression status per
prior finding (`STILL_FAILS`, `FIXED`, `REGRESSED_ELSEWHERE`).

**EXIT_CONDITION:** every persistence/recovery test has a disposition; every
prior-cycle finding has a regression status if this is a fix-verification
cycle.

**ALLOWED_OUTCOME:** five-value set, per item.

**CHECKPOINT:** required.

---

### STAGE 8 — NON-FUNCTIONAL / SCALE

**INPUT:** load/stress/soak/spike test cases with explicit numeric targets
(from `test-strategy.md` — an SLO/SLA target is mandatory here, not
optional, per Constitution §2).

**MUST_DO:** Execute against the numeric targets. A capability adapter (e.g.
k6) with pass/fail thresholds is expected here rather than free-form load
generation.

**MUST_CREATE:** `evidence/non-functional/{scenario}.json` including the
numeric target, the numeric result, and the boundary conditions (peak
concurrency, duration, data volume).

**MUST_RECORD:** target vs. observed for throughput, latency (p50/p95/p99 as
applicable), error rate, resource ceilings.

**EXIT_CONDITION:** every defined scale scenario has a disposition against
its numeric target.

**ALLOWED_OUTCOME:** five-value set. `NOT_APPLICABLE` is legal only if
Stage 2/3 explicitly determined scale is out of scope for this product —
not as a default.

**CHECKPOINT:** required.

---

### STAGE 9 — OBSERVABILITY READINESS

**INPUT:** product's logging/metrics/tracing configuration and output
captured during Stages 5-8.

**MUST_DO:** Determine whether the product's own instrumentation would let
someone diagnose the failures observed so far (or a hypothetical similar
one) from production output alone. This checks the *product's* readiness,
not QA's — a product that passes every functional test but logs nothing
useful still fails this stage.

**MUST_CREATE:** `observability-readiness.md` listing what's instrumented,
what isn't, and per component whether a production failure there would be
diagnosable from logs/metrics/traces alone.

**MUST_RECORD:** concrete gaps (e.g., "no structured error logging on the
persistence layer; a failure there would produce no traceable signal").

**EXIT_CONDITION:** every component from Stage 2's inventory has an explicit
observability disposition.

**ALLOWED_OUTCOME:** `PASSED`, `FAILED` (insufficient instrumentation —
this is a real finding, feed it to Stage 12), `NOT_APPLICABLE`, `DEFERRED`.

**CHECKPOINT:** required.

---

### STAGE 10 — BENCHMARK / COMPETITIVE VALIDATION

**INPUT:** `HANDOFF_PACKAGE/reference-projects/`,
`HANDOFF_PACKAGE/benchmark-suite/`.

**MUST_DO:** Run the benchmark suite against the product and against each
applicable vendored reference project. If a reference project cannot be run
(environment mismatch, missing dependency, incompatible version), this must
be recorded as `BLOCKED` with the specific technical reason — **never
silently dropped.** This is the exact failure mode this organization exists
to prevent (see `HISTORY/DESIGN_DECISIONS.md`).

**MUST_CREATE:** `benchmark-results/{reference_project}.json` per
comparison attempted, including ones that resulted in `BLOCKED`.

**MUST_RECORD:** what was compared, on what metric, the numeric result for
both sides, or the specific blocker.

**EXIT_CONDITION:** every reference project listed in the handoff package's
manifest has an entry — run or explicitly blocked. None may be absent from
the record.

**ALLOWED_OUTCOME:** `PASSED` (comparison ran, product meets/exceeds
reference), `FAILED` (comparison ran, product underperforms), `BLOCKED`,
`NOT_APPLICABLE` (reference project not relevant to this product — must be
justified), `DEFERRED`.

**CHECKPOINT:** required.

---

### STAGE 11 — INDEPENDENT EXPLORATORY TESTING

**INPUT:** everything produced so far; no pre-written script for this stage
by definition.

**MUST_DO:** Investigate off-script: what would an experienced, skeptical
tester probe that nobody explicitly planned for. If this uncovers a gap in
Stage 3's risk model or Stage 4's test design, trigger a `reentry` (see
`STATE_MACHINE.md`) rather than folding the finding in informally.

**MUST_CREATE:** `exploratory-log.md` (what was investigated and why, even
for things that turned up nothing), any new findings using the same evidence
schema as other stages.

**MUST_RECORD:** the reasoning that led to each investigation — this stage's
value is in showing what was *thought of*, not only what was found.

**EXIT_CONDITION:** worker judges exploration sufficient relative to the
product's risk profile, OR successive rounds stop finding anything new
(borrowed convergence criterion — see `HISTORY/DESIGN_DECISIONS.md`).

**ALLOWED_OUTCOME:** `COMPLETE` (with findings, or none found — both valid),
`BLOCKED`.

**CHECKPOINT:** required.

---

### STAGE 12 — FINDINGS: REPRODUCE, ROOT CAUSE, IMPACT

**INPUT:** every `FAILED` disposition recorded in Stages 5-11.

**MUST_DO:** For each failure — produce a literal reproduction procedure,
investigate root cause (evidence-supported; a suspected cause without
supporting evidence is recorded as "suspected," never asserted as fact),
and assess impact.

**MUST_CREATE:** `findings/{finding_id}.json` per
`HANDOFF_PACKAGE_TEMPLATE/schemas/FINDING.schema.json` — including verbatim
error text/stack traces (Constitution §5) and the component/file path
tagged for the Diagnostic Index.

**MUST_RECORD:** reproduction steps, root cause (or "not determined" if
genuinely not determinable, with what was tried), severity, affected
component.

**EXIT_CONDITION:** every `FAILED` from any prior stage has a corresponding
finding record.

**ALLOWED_OUTCOME:** `COMPLETE`, `BLOCKED` (cannot reproduce — record as
such, do not drop the finding).

**CHECKPOINT:** required.

---

### STAGE 13 — COVERAGE ANALYSIS

**INPUT:** `risk-register.json` (Stage 3), every disposition recorded in
Stages 5-12.

**MUST_DO:** For every entry in the risk register, confirm it resolved to
exactly one of the five dispositions, with evidence. This is a mechanical
cross-check, not new testing — its entire purpose is catching anything that
went silent.

**MUST_CREATE:** `coverage-disposition.json` — one entry per risk-register
item, each pointing to the evidence that produced its disposition.

**MUST_RECORD:** any risk-register entry with no matching disposition is
itself a `BLOCKED` finding on this stage — the audit cannot proceed to
Stage 14 with an unresolved entry.

**EXIT_CONDITION:** 100% of risk-register entries have a disposition +
evidence pointer. No exceptions — this is the enforcement point for
Constitution §3.

**ALLOWED_OUTCOME:** `COMPLETE` only when the exit condition is fully met;
otherwise `BLOCKED`, naming exactly which entries are unresolved.

**CHECKPOINT:** required.

---

### STAGE 14 — FINAL AUDIT

**INPUT:** everything produced in Stages 0-13.

**MUST_DO:** Compile the verdict. Build and commit the Diagnostic Index
(Constitution §6 — mandatory, not optional) per
`HANDOFF_PACKAGE_TEMPLATE/schemas/DIAGNOSTIC_INDEX.schema.json`, aggregating
every finding, risk-register entry, and known limitation, keyed by
component and verbatim error signature. State confidence and every open
limitation explicitly. Report to the product owner. **Do not issue a
release decision** — report the verdict; the release call belongs to the
product owner per `LIFECYCLE.md`.

**MUST_CREATE:** `final-audit.md`, `diagnostic-index.json`.

**MUST_RECORD:** overall disposition summary, every `FAILED`/`BLOCKED` item
still open, every `DEFERRED` item and why, and a pointer to every
individual finding.

**EXIT_CONDITION:** Diagnostic Index exists and covers 100% of this cycle's
findings and risk-register entries.

**ALLOWED_OUTCOME:** `COMPLETE`. (A `FAILED` or `BLOCKED` product does not
block *this stage* from completing — it blocks the release decision, which
isn't this stage's call to make.)

**CHECKPOINT:** required — this is the FINAL HANDOFF commit.
