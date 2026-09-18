# Pre-Planning Decision Contract

## Entry (required before a run can start)

- `idea.md` reference, and its completion state (`CLEAR` /
  `CLEAR WITH OPEN ITEMS`) at the time this run started. A run with no
  traceable `idea.md` source, or one that started against a `BLOCKED`
  `idea.md`, is invalid per `COUNCIL.md`'s entry condition.
- any open items inherited from `idea.md`, carried explicitly (not
  silently dropped).

## Completed run must contain

Four always-produced documents, one per role, each populated from its
fixed template under `templates/` — never omitted, even on fast-path
(see each template's own "Fast-path rule" section for how it degrades
gracefully instead of disappearing):

- `templates/MARKET_RESEARCH_TEMPLATE.md` → Market/Research's output
- `templates/FEASIBILITY_REPORT_TEMPLATE.md` → Feasibility & Cost
  Assessor's output
- `templates/BUSINESS_CASE_TEMPLATE.md` → Advocate's output
- `templates/PRE_MORTEM_TEMPLATE.md` → Skeptic's output

Plus the Synthesizer's own decision record:

- problem/idea being evaluated
- path taken: **FULL DEBATE** or **FAST-PATH** (per `COUNCIL.md`'s
  fast-path rule), and which signal in `idea.md` justified a fast-path
  if one was taken — this same reason is quoted verbatim in all four
  templates' headers, not restated differently in each
- material disagreements and evidence used, citing the four documents
  above rather than re-deriving their content
- verdict: GO | GO (fast-path) | NO-GO | NEEDS MORE EVIDENCE
- reasoning for verdict
- explicit missing evidence when undecidable
- human-gate status

## Completeness gate — no verdict without it

This is the actual requirement, not just a list of files that should
exist: **the Synthesizer may not issue any verdict (including a
fast-path GO) until every section of all four templates is
non-empty.** "Non-empty" means either substantively filled (full path)
or explicitly filled with the fast-path reason from that template's own
Header (fast path) — a blank section, a section silently left out, or a
section that just repeats "N/A" with no reason attached all count as
incomplete, the same way `HANDOFF_CONTRACT.md`'s rule treats a missing
`OPEN QUESTIONS` field as incomplete rather than "clearly none."

```text
Before Synthesizer may issue a verdict:
        ↓
Are all 4 templates present under templates/, one per role?
    ├── NO  → BLOCKED. Missing document(s) named explicitly. No verdict.
    └── YES
         ↓
Is every section in every template either substantively filled
or filled with a stated fast-path reason (never blank, never a
bare "N/A")?
    ├── NO  → BLOCKED. Missing section(s) named explicitly, by
    │         template and section number. The role that owns that
    │         section is the one who fills it — the Synthesizer does
    │         not fill a gap on another role's behalf.
    └── YES → Synthesizer may proceed to a verdict.
```

This is an artifact-completeness check on the four required documents
(consistent with `SHARED/STAGE_EXIT_CONTRACT.md`'s "artifact-based, not
checklist-based" rule — it is not a new round of questions to ask, it is
whether the four already-defined artifacts are actually whole), not a
new debate step and not something the Orchestrator can wave through by
inferring completeness from silence, per the system's existing
silence-is-never-approval rule.

## Where this lives

The four templates and this decision record are written to the intake
repository's `pre-planning/<the same name used in ideation/ingestion
for this idea>/` folder, per `SHARED/INTAKE_REPOSITORY.md` — including
a `NO-GO` or unresolved `NEEDS MORE EVIDENCE` verdict. Nothing here is
deleted because the idea didn't proceed; only a `GO`/`GO (fast-path)`
verdict triggers copying these documents into the target project's own
repo, per that same file's "What happens on GO" section.
