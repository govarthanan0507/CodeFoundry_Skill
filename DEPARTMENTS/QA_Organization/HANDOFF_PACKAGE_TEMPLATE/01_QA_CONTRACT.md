# QA Contract (template — fill in per cycle)

This is the authorization boundary for one QA cycle. It is filled in by the
product owner before Stage 0 can begin, and its content is what Stage 0
records as provenance.

## Product

- **Name / version being tested:**
- **Exact commit or build identifier:**
- **Cycle type:** `FULL_AUDIT` or `FIX_VERIFICATION` (see `LIFECYCLE.md` for
  how to decide)
- **If `FIX_VERIFICATION`: which prior cycle and which findings does this
  target?**

## Scope

- **In scope (components/features):**
- **Out of scope, and why:**
- **Capabilities expected to apply (Stage 2 will confirm, this is a
  starting hint, not binding):**

## Authorization boundaries

- **Is destructive/intrusive testing authorized?** (Constitution §8 — QA
  will not perform destructive testing without explicit authorization here)
- **Is any product-modification mode authorized for this cycle?**
  (Constitution §1 — default is no; if yes, scope it exactly)
- **Environment(s) authorized for testing:**
- **Data authorized for use (real, synthetic, anonymized — see
  `test-data/` and `adversarial-data/`):**

## Security boundary acknowledgement

Per Constitution §10, this QA cycle performs baseline security hygiene
only. Deep/adversarial security testing is explicitly deferred pending a
separate Security Organization. Product owner acknowledgement:

- [ ] I understand this cycle's security disposition will be baseline-only
      and does not constitute a penetration test or security audit.

## Release authority

Per Constitution §9 and `LIFECYCLE.md`, QA reports a verdict; it does not
issue the release decision. The release decision authority for this cycle
is:

- **Name/role:**

## Sign-off

- **Authorized by:**
- **Date:**
