# Lifecycle

Two things this document defines: who is allowed to write where (the
three-repo boundary), and how audit history accumulates over a product's
life (the versioning model).

## The three-repo boundary

```
   DEVELOPER REPO                  QA REPO                  PRODUCTION REPO
  (Developer writes           (QA worker writes          (No agent writes here
   only)                       only — the entire            directly. A human,
        |                      audit trail lives            or an automated gate
        | handoff package      here)                        that fires ONLY on
        | (versioned build,           |                      a QA-accepted verdict,
        |  see below)                 | findings /           promotes into it.)
        v                             | evidence
  [ Stage 0: QA acquires  ] --------> v
  [ the exact version,    ]     [ Stages 1-14 run here ]
  [ records provenance    ]     [ every stage checkpoint-
                                  committed ]
                                       |
                                       v
                              QA verdict + evidence
                              handed back to Developer
                                       |
                                       v
                              Developer fixes issues,
                              cuts next version
                                       |
                                       v
                              next QA cycle (full or
                              fix-verification, see below)
```

Rules:

- The developer never writes to the QA Repo. QA never writes to the
  Developer Repo. This is what makes an independent verdict possible —
  neither side can quietly influence the other's record.
- Promotion to the Production Repo is **not** performed by either agent.
  It requires a human decision (or an automated gate keyed strictly to a
  QA-accepted, non-`FAILED`/non-open-critical-`BLOCKED` verdict). Neither
  the developer nor QA has authority to ship.
- QA does not fix the product. If QA operates in an explicitly authorized
  fix-verification mode, that authorization and its scope must be recorded
  in the handoff contract — it is never QA's default behavior (Constitution
  principle 1).

## Versioned history model

Every audit — full or partial — is a permanent, immutable subtree. Nothing
is overwritten.

```
HISTORY/
├── V0/
│   ├── product-snapshot-manifest.json   (exact commit/version tested)
│   ├── environment.md
│   ├── requirements.md
│   ├── risk-register.json
│   ├── test-strategy.md
│   ├── stage-checkpoints/                (one record per stage, per Constitution §3)
│   ├── findings/
│   ├── evidence/
│   ├── benchmark-results/
│   ├── coverage-disposition.json
│   ├── diagnostic-index.json             (Constitution §6 — mandatory)
│   └── final-audit.md                    (verdict, reported to product owner)
│
├── V0-FIX-01/
│   ├── developer-changes.md              (what the developer changed, and why)
│   ├── affected-findings.json            (which V0 findings this targets)
│   ├── targeted-retests/
│   ├── regression-results/
│   └── new-evidence/
│
├── V0-FIX-02/
│   └── ...
│
└── V1/
    └── ... (full audit, same shape as V0)
```

### Full audit vs. fix-verification cycle — how to decide which one runs

Run a **fix-verification cycle** (`V{n}-FIX-{m}`) when all of the following
hold:
- The change is scoped to fixing specific findings from the prior full
  audit, not new features or architecture.
- The change does not touch a component outside the prior audit's risk
  model (i.e., nothing the prior `risk-register.json` didn't already cover).

A fix-verification cycle does **not** re-run Stages 0-4 (intake, environment,
recon, risk/strategy, test design) in full. It re-enters at Stage 5/6/7
(execution/adversarial/regression), scoped to the affected findings, plus
Stage 13/14 (coverage, final audit) to re-close the loop.

Run a **full audit** (`V{n+1}`) when either holds:
- The change introduces new architecture, new components, or new features
  not covered by the existing risk register.
- A fix-verification cycle's targeted retest surfaces something the original
  risk model didn't anticipate — escalate to a full audit rather than
  stretching the fix cycle to cover it.

If it's ambiguous which applies, the worker records the ambiguity as a
`BLOCKED` disposition at intake and defers the decision to the product
owner rather than guessing (Constitution §3 fail-safe rule, see
`ENGINE/STATE_MACHINE.md`).

### Risk acceptance is a human decision, recorded separately

QA's disposition vocabulary (`PASSED/FAILED/BLOCKED/NOT_APPLICABLE/DEFERRED`)
does not include "shipped anyway." If the product owner chooses to release
despite an open `FAILED` or `BLOCKED` finding, that is recorded as its own
artifact — `HISTORY/V{n}/risk-acceptance/{finding-id}.md` — naming who
accepted the risk, when, and why. This keeps QA's verdict and the human
release decision auditable as two distinct facts, per Constitution §9.
