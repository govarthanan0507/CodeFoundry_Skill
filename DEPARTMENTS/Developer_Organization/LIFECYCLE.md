# Lifecycle

## The pipeline this organization runs inside

```
   DESIGN COUNCIL              DEVELOPER ORGANIZATION           QA_ORGANIZATION
  (produces TRD/FRD,          (this repo — builds,             (independent
   per-story DISCOVERY.md,     logs, self-checks, hands         verification,
   owns the "how")             off, iterates on findings)       own repo)
        |                              |                              |
        | inbound handoff              |                              |
        | (INBOUND_HANDOFF/,           |                              |
        |  see that folder)            |                              |
        v                              v                              |
  [ Ticket exists,        ] --------> [ Ticket flows through  ]        |
  [ Discovery cleared,    ]           [ Kanban per            ]        |
  [ Design decided        ]           [ SHARED/AGILE_WORKFLOW ]        |
                                       [ periodic log +        ]       |
                                       [ verification_evidence ]       |
                                              |                        |
                                              v                        |
                                       [ Version's tickets all ]       |
                                       [ DONE → handoff package] ----> v
                                       [ per SHARED/            ]  [ Full audit
                                       [ HANDOFF_TO_QA.md       ]  or fix-verify
                                              ^                    cycle runs
                                              |                        |
                                              | findings (OPEN)        |
                                              +------------------------+
                                       [ Fix ticket per finding,       ]
                                       [ same Kanban/Discovery gates,  ]
                                       [ re-submitted as FIX_VERIF-    ]
                                       [ ICATION cycle                 ]
                                              |
                                              v
                              [ Every finding FIXED_VERIFIED /
                                ACCEPTED_RISK / WONT_FIX ]
                                              |
                                              v
                                      Next team (Release/DevOps —
                                      not yet built)
```

## Who writes where

This organization writes to its own ticket/log state and to the
handoff package it assembles for QA. It does not write to Design
Council's `TRD.md`/`FRD.md` (a disagreement is a Change Request, not
an edit) and does not write to `QA_Organization`'s own repository — the
entire audit trail QA produces belongs to QA, per that organization's
own Constitution and three-repo boundary (`QA_Organization/LIFECYCLE.md`).
This organization only ever *reads* QA's findings back.

## Versioned history — nothing overwritten

Every version's build, every fix cycle, and every Discovery record
this organization consumed is preserved, not overwritten:

```
HISTORY/
├── V1/
│   ├── tickets/                  (closed, with full log + evidence)
│   ├── discovery-records/        (DISCOVERY.md per story, as received)
│   ├── qa-handoff-package/       (what was actually sent)
│   └── findings/                 (what came back, and their resolution)
├── V1-FIX-01/
│   └── ...                       (same shape, scoped to one QA cycle)
└── V2/
    └── ...
```

## The periodic-logging rule, operationally

Per `CONSTITUTION.md` principle 1, logging is not a closing-time
summary — it happens at each real transition:

```
Ticket pulled (TO DO → IN PROGRESS)  → active-work log entry, per
                                        SHARED/AGILE_WORKFLOW.md
A Discovery-relevant finding surfaces
mid-build (not just at ticket start)  → recorded against the ticket,
                                        not held until handoff
Ticket moves IN PROGRESS → IN REVIEW → verification_evidence populated
Ticket moves IN REVIEW → DONE        → evidence confirmed complete,
                                        per that file's gate
```

A ticket that reaches `DONE` with any of these steps missing is
incomplete, not "basically fine" — same severity as a missing required
field anywhere else in this system.
