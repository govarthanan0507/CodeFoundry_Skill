# Capability Pool

A capability is domain-specific testing knowledge — what to check and how,
for one kind of thing (web, API, load, security baseline, accessibility).
It is not the worker and not the engine. Stage 2 (Reconnaissance) decides
which capabilities apply to a given product; the engine's stages 5-11
invoke whichever ones were marked applicable.

Capabilities are adapters around existing, mature tools wherever one exists
— see `HISTORY/DESIGN_DECISIONS.md` for the market research that justified
this (building test-execution engines from scratch was rejected once real
open-source options were verified). A capability's job is translating that
tool's native output into this organization's evidence and disposition
format — never re-implementing what the tool already does well.

## Capability contract shape

Every capability, regardless of domain, must specify:

```
CAPABILITY: <name>
UNDERLYING_TOOL(S): <what it wraps, with version/pin>
APPLIES_WHEN: <condition Stage 2 checks to decide applicability>
INPUT_FROM_ENGINE: <what a stage hands it — test case, target, boundary conditions>
OUTPUT_TO_ENGINE: <evidence record, matching EVIDENCE.schema.json>
DISPOSITION_MAPPING: <how the tool's native pass/fail maps to the five-value set>
KNOWN_LIMITATIONS: <what this capability does NOT cover>
```

## V0.1 initial capability set

These five were chosen deliberately small, per `ROADMAP.md` V0.1, and
because each wraps a verified, actively maintained open-source tool rather
than requiring custom test-execution engineering.

---

### Functional & Exploratory Web (Playwright-based)

```
UNDERLYING_TOOL(S): Playwright, with self-healing execution technique
                     comparable to vostride/agent-qa (re-observe UI on
                     action failure, retry via alternate path), and
                     crawl/flow-inference technique comparable to
                     iklymchuk/autonomous-qa-agent (BFS crawl, DOM-driven
                     flow inference, axe-core accessibility hook,
                     pixel-level screenshot diff).
APPLIES_WHEN: product exposes a web UI.
INPUT_FROM_ENGINE: target URL/route, user flow description or none
                    (exploratory), boundary conditions if specified.
OUTPUT_TO_ENGINE: EVIDENCE.schema.json record per test/flow, including
                   Playwright trace reference and screenshot diff result
                   where applicable.
DISPOSITION_MAPPING: tool assertion pass -> PASSED; assertion fail with
                      reproducible trace -> FAILED; tool crash/timeout with
                      unclear cause -> BLOCKED.
KNOWN_LIMITATIONS: does not cover native mobile or desktop UI; does not
                    perform load generation (see Performance/Load below);
                    accessibility check here is automated scanning only —
                    per Constitution's accessibility note, automated scan
                    is not equivalent to actual assistive-technology
                    validation, and that gap must be recorded as
                    NOT_APPLICABLE/DEFERRED, not silently treated as covered.
```

### API Testing

```
UNDERLYING_TOOL(S): Postman/Newman or Schemathesis for schema-driven
                     property testing against OpenAPI specs where one
                     exists.
APPLIES_WHEN: product exposes a REST/GraphQL/RPC API.
INPUT_FROM_ENGINE: endpoint spec or OpenAPI/schema reference, test cases
                    (functional + adversarial), boundary conditions.
OUTPUT_TO_ENGINE: EVIDENCE.schema.json record per endpoint/test, including
                   request/response verbatim.
DISPOSITION_MAPPING: assertion pass -> PASSED; assertion fail -> FAILED;
                      schema unavailable/endpoint unreachable -> BLOCKED.
KNOWN_LIMITATIONS: contract testing against consumer expectations (e.g.
                    Pact-style) is not included in V0.1 — record as
                    NOT_APPLICABLE unless the product's risk register
                    calls for it, in which case record DEFERRED and treat
                    as a V0.3 capability-acquisition candidate.
```

### Performance / Load (k6)

```
UNDERLYING_TOOL(S): k6 — chosen over Locust specifically for its built-in
                     pass/fail thresholds and clean CI exit codes, which
                     map directly onto this organization's disposition
                     requirement (Constitution §2 — a numeric target is
                     mandatory, not optional).
APPLIES_WHEN: product has a network-facing interface with meaningful
              concurrency exposure (i.e., almost always applicable unless
              the product is a fully offline, single-user tool).
INPUT_FROM_ENGINE: target endpoint(s), numeric SLO/SLA targets from
                    test-strategy.md, boundary conditions (peak
                    concurrency, duration, ramp profile).
OUTPUT_TO_ENGINE: EVIDENCE record with target-vs-observed for throughput,
                   latency percentiles, error rate.
DISPOSITION_MAPPING: k6 threshold pass -> PASSED; threshold fail ->
                      FAILED; k6 cannot run against target environment ->
                      BLOCKED.
KNOWN_LIMITATIONS: k6 is not a chaos-engineering tool — genuine fault
                    injection (killing nodes, network partition) is out of
                    scope here; if the risk register calls for it, record
                    DEFERRED as a V0.3 candidate (Chaos Mesh/Gremlin-class
                    tooling).
```

### Security Baseline (OWASP ZAP + Trivy/Grype)

```
UNDERLYING_TOOL(S): OWASP ZAP (DAST, passive+active scan against web/API
                     surface), Trivy or Grype (dependency/CVE scanning).
APPLIES_WHEN: always applicable for baseline hygiene (Constitution §10).
              Deep/adversarial security testing is explicitly out of
              scope for this capability — see below.
INPUT_FROM_ENGINE: target URL/API surface, dependency manifest.
OUTPUT_TO_ENGINE: EVIDENCE record per scan: findings by severity, CVE IDs
                   and affected package versions.
DISPOSITION_MAPPING: no critical/high findings -> PASSED; critical/high
                      finding present -> FAILED; scan cannot complete ->
                      BLOCKED.
KNOWN_LIMITATIONS: THIS IS BASELINE HYGIENE ONLY. Penetration testing,
                    threat modeling, red-teaming, and business-logic
                    security review are not covered. Per Constitution §10,
                    record deep security testing as
                    "DEFERRED — Security Organization not yet built" in
                    the risk register — never report this capability's
                    PASSED result as if it were a full security audit.
```

### Accessibility (axe-core)

```
UNDERLYING_TOOL(S): axe-core, injected during the Playwright-based
                     capability's execution (shared adapter, not a
                     separate run).
APPLIES_WHEN: product exposes a web UI intended for end users (not
              applicable to a pure backend/API/CLI product).
INPUT_FROM_ENGINE: rendered page/route to scan.
OUTPUT_TO_ENGINE: EVIDENCE record with WCAG violation list by severity.
DISPOSITION_MAPPING: no violations at target WCAG level -> PASSED;
                      violations present -> FAILED; scan cannot run ->
                      BLOCKED.
KNOWN_LIMITATIONS: automated scanning catches a subset of real
                    accessibility problems. Actual assistive-technology
                    validation (NVDA/JAWS/VoiceOver) is not covered and
                    must be recorded as NOT_APPLICABLE/DEFERRED explicitly
                    if the product's risk register determines it's needed
                    — never implied as covered by the automated scan
                    passing.
```

## Adding a capability later (V0.3)

A new capability must satisfy the contract shape above before being added
to this file. If it overlaps an existing capability's `APPLIES_WHEN`, it
must be benchmarked against the incumbent first (per `EVOLUTION.md`) —
never silently substituted. Previous capability versions are preserved
under `HISTORY/capability-versions/`, never deleted.
