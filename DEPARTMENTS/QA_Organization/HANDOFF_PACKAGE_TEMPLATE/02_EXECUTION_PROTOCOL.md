# Execution Protocol (template — fill in per cycle)

Filled in by the developer. This is what Stage 1 (Environment
Qualification) uses to verify the QA environment is trustworthy before
anything run in it counts as evidence.

## Build / run instructions

- **Exact build command(s):**
- **Exact run command(s):**
- **Required runtime/OS/versions:**
- **Required environment variables / secrets (names only — actual secrets
  are provisioned separately, never committed to this package):**
- **Required external services and how they're mocked/stubbed for QA
  (per Constitution §8, QA should not depend on live third-party
  production services unless explicitly authorized in
  `01_QA_CONTRACT.md`):**

## Known environment differences from production

Per the environment-parity documentation practice — a top cause of
"worked in QA, broke at prod" incidents is an unrecorded difference between
the two. List every known difference here, even ones that seem minor:

- **Scale/data volume difference:**
- **Infrastructure topology difference (single-node vs. multi-node,
  etc.):**
- **Configuration differences:**
- **Third-party service differences (sandboxed vs. live):**

## Numeric targets for Stage 8 (Non-Functional/Scale)

Required — Constitution §2 makes a boundary-condition target mandatory,
not optional:

- **Expected peak concurrency:**
- **Target latency (p50/p95/p99):**
- **Target throughput:**
- **Target error rate ceiling:**
- **Soak duration (if applicable):**

## Observability

For Stage 9 — what instrumentation exists today (logs, metrics, traces),
and where:

- **Logging:**
- **Metrics:**
- **Tracing:**
