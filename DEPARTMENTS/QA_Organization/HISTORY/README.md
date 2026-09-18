# History

This directory holds two things, kept deliberately together:

- **`DESIGN_DECISIONS.md`** — why the organization is built the way it is.
  Read this before changing `CONSTITUTION.md` or `ENGINE/`.
- **`{cycle_id}/`** (e.g. `V0/`, `V0-FIX-01/`, `V1/`) — the immutable audit
  record of every QA cycle ever run, per the versioning model in
  `LIFECYCLE.md`. Created by Stage 0 of a real cycle. Nothing here yet
  because no product has been run through this organization — the first
  entry will be created the first time `HANDOFF_PACKAGE_TEMPLATE/` is
  filled in and a worker executes Stage 0.

Nothing under this directory is ever overwritten. A correction is a new
subtree, not an edit to an old one (Constitution §16).
