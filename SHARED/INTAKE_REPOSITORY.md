# Intake Repository — where Ideation/Ingestion/Pre-Planning output lives before GO

## The gap this closes

`SHARED/PROJECT_FOLDER_STRUCTURE.md` says a project's own
`projects/<name>/` folder is created "once it clears Pre-Planning" —
but never says where the idea's documents live *before* that point,
or what happens to them if Pre-Planning never clears (a real NO-GO, or
a `NEEDS MORE EVIDENCE` that never gets resolved). Writing `idea.md`/
`CODE_DIGEST.md` straight into a real target repo (e.g. an existing
codebase handed to `AGENTS/Ingestion/` Mode B/C) would pollute that
repo with dead ideas the moment Pre-Planning kills them — a NO-GO
should not leave debris in a product's own repository.

## The rule

Every `AGENTS/Ideation/`, `AGENTS/Ingestion/`, and
`COUNCILS/Pre-Planning/` output is written to a **separate, dedicated
intake repository** (this session's instance: `CodeFoundry_Intake`) —
never into the target project's own repo, until Pre-Planning actually
returns GO.

```text
CodeFoundry_Intake/
  ideation/
    <a real, descriptive name — never "idea1"/"idea2">/
      idea.md
  ingestion/
    <a real, descriptive name>/
      idea.md
      CODE_DIGEST.md          (Mode B/C only)
  pre-planning/
    <a real, descriptive name>/
      BUSINESS_CASE.md         (per BUSINESS_CASE_TEMPLATE.md)
      FEASIBILITY_REPORT.md    (per FEASIBILITY_REPORT_TEMPLATE.md)
      MARKET_RESEARCH.md       (per MARKET_RESEARCH_TEMPLATE.md)
      PRE_MORTEM.md            (per PRE_MORTEM_TEMPLATE.md)
      DECISION_CONTRACT.md     (the verdict record itself)
```

The subfolder name is the same idea across all three folders it
appears in (an idea that reaches Pre-Planning has the same name in
`ideation/`/`ingestion/` and `pre-planning/`) — this is what makes the
full trail readable end to end without a separate index.

## Naming — never a number

A subfolder name must describe the idea itself (e.g.
`base-memory-os-hybrid-retrieval`), never a sequence placeholder
(`idea1`, `idea2`). Per `SHARED/DOCUMENT_GOVERNANCE.md`'s own
versioning discipline, a name that means nothing on its own defeats
the purpose of keeping the record — a human or agent should be able
to tell what an idea was from its folder name alone, without opening
the file.

## Everything survives, GO or NO-GO

Per `SHARED/DOCUMENT_GOVERNANCE.md`'s "preserve, don't delete"
discipline, applied here specifically: a NO-GO, a `NEEDS MORE
EVIDENCE` that never gets resolved, or a market that turns out too
hard to crack are not failures to erase — they are exactly the kind of
record `Constitution`-level "evidence over assertion" principles exist
to keep. Nothing in `ideation/`, `ingestion/`, or `pre-planning/` is
ever deleted because the idea didn't proceed. A killed idea's folder
stays, with its `DECISION_CONTRACT.md` stating the NO-GO and why —
this is itself useful evidence if a similar idea resurfaces later
(per `COUNCILS/Pre-Planning/roles/Market-Research.md`'s own use of
prior findings).

## What happens on GO

The moment Pre-Planning returns GO (or GO fast-path), per
`SHARED/HANDOFF_CONTRACT.md`'s mapping:

```text
1. The intake repo's copy of idea.md / CODE_DIGEST.md / the
   pre-planning documents is left in place, permanently, as the
   original historical record. It is never deleted or moved out of
   the intake repo.
2. A COPY of the same documents is written into the target project's
   own repo, at projects/<name>/documents/ per
   SHARED/PROJECT_FOLDER_STRUCTURE.md's existing shape — this is what
   makes the project repo self-contained for Design Council onward,
   without needing to reach back into the intake repo for anything.
3. Design Council and every later stage read from the project repo's
   own copy, not the intake repo — the intake repo's job ends at GO;
   it is not a live dependency of the build.
```

A copy, not a move: if the copies ever diverge later (the project
repo's copy gets superseded by a new version per
`DOCUMENT_GOVERNANCE.md`), the intake repo's original stays exactly as
it was at the moment of the GO decision — it is the historical record
of what Pre-Planning actually approved, not a synced mirror.

## What this file does not change

- Does not change `SHARED/PROJECT_FOLDER_STRUCTURE.md`'s own rule for
  `dev_<project>`/`test_<project>`/`prod_<project>` — those still only
  get created once a ticket is ready to build, well after this stage.
- Does not apply to `SHARED/EXISTING_CODE_AUDIT_GATE.md`'s
  `AUDIT_REPORT.md` — that gate runs after Ingestion, using the intake
  repo's own `CODE_DIGEST.md` as its input, but its own output belongs
  with Design Council's other artifacts once the project has a real
  home, not backfilled into the intake repo's `ingestion/` folder.
