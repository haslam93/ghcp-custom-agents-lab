# Audit report format

Return the following structure in chat. Replace placeholders with evidence;
omit unsupported findings rather than filling a quota.

## Scope and limits

- Audit type and approved component/docs scope:
- Files inspected:
- Important files or runtime facts not inspected:
- Scope complete or incomplete; finding cap and unreviewed areas:
- Execution: none; static read/search inspection only.

## Documentation score and coverage (DOC only)

Use DOC-R1 from documentation-checks.md, with all ten checks:

| Check ID / weight | PASS / FAIL / MISSING / NOT_REVIEWED / N/A | Earned / possible | Docs and source/search evidence; N/A reason or limitation |
|---|---|---|---|

- Earned / possible points:
- Scoped score: [one decimal percentage, or No score / insufficient evidence]
- Weighted coverage: [assessed weight / all non-N/A weight and percentage;
  or N/A - no applicable checks]
- Counts: [assessed / NOT_REVIEWED / N/A]; named inspected versus uninspected files:
- Scope label: [Provisional - incomplete scope if any check/scope is unfinished]
- Recheck only: [before/after totals, coverage and percentage-point delta using
  identical criteria/scope/assessed checks; otherwise Not comparable and why]

Missing means required docs were searched for and absent; it earns zero only
on assessed applicable checks. Unreviewed does not earn zero and is not N/A.
No positive denominator means no score. Never present synthetic numbers as
actual audit results or treat this bounded score as overall repository health.

## Security coverage (SEC only)

| Dimension | Reviewed / Not reviewed / Not applicable | Evidence or limitation |
|---|---|---|

Keep this table compact. Do not convert security coverage into a numerical
score, compliance statement or claim of complete repository coverage.

## Findings

At most two supported findings per audit in the workshop. Use the shared finding
template for each. Sort SEC findings CRITICAL, HIGH, MEDIUM, LOW with confidence
separate from severity. Disclose the scope/cap as triage, not completeness.
If none is supported, state that clearly and preserve the scope limitations.

## Needs evidence

List unconfirmed leads separately with the missing check; do not promote them
to ranked vulnerabilities or scored documentation failures.

## Human review

State the most useful next evidence check and any visibility/data-handling
constraint. A human must validate selected DOC findings before doc-fixer's
approved local-edit/PR steps, or a SEC finding before ticket-drafter's preview
and approved local file / separate Jira step.
During this audit pass, no files or external records have been written.
