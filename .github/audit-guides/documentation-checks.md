# Documentation inspection and scoring rubric (DOC-R1)

Score only a named docs workflow and its approved source/config scope.
This is a bounded documentation score, not repository health, security or
compliance. Freeze the scope, intended reader and applicable checks before
scoring; evidence may justify a recorded N/A decision, not a convenient omission.

## Checks and weights

Each dimension has two independently assessed binary checks. Maximum weight
is 100 points; do not invent discretionary partial credit. A dimension can
earn half its weight when only one of its two checks passes.

| ID | Dimension | Weight | Pass only when inspected evidence establishes |
|---|---|---|---|
| D1a | Getting started | 15 | Documented runtime and prerequisites match manifests/version configuration for the workflow |
| D1b | Getting started | 15 | Documented install/start/check steps required by the workflow name the actual scripts or commands |
| D2a | Behavior and contracts | 12.5 | Documented inputs and defaults match relevant implementation/callers |
| D2b | Behavior and contracts | 12.5 | Documented outputs, errors and compatibility match relevant implementation/tests |
| D3a | Navigation and structure | 7.5 | Required workflow docs can be found from the scoped entry document or index |
| D3b | Navigation and structure | 7.5 | In-scope referenced local paths, components and links resolve to the intended repository content |
| D4a | Configuration and operation | 10 | Required configuration names/examples match approved example config and source |
| D4b | Configuration and operation | 10 | Workflow-relevant defaults and operational/troubleshooting guidance match evidenced behavior |
| D5a | Examples and change guidance | 5 | A required usage example matches the current scoped interface |
| D5b | Examples and change guidance | 5 | Required contributor/change/verification steps match existing tooling and constraints |

Record the exact claims evaluated within each check. If a check contains
multiple required claims, **all** must be inspected before assigning points:
all correct means PASS; any evidenced contradiction means FAIL. If any required
claim is uninspected, use NOT_REVIEWED for that check and record already-supported
mismatches as findings without scoring the unreviewed check. No execution is
implied by inspecting source or tests.

## Status and evidence contract

For each of the ten check IDs, return status, earned points, possible points,
docs evidence and source/search evidence. Keep these distinct:

- **PASS**: all scoped required claims inspected and supported; earned = weight,
  possible = weight.
- **FAIL**: an inspected required claim is incorrect; earned = 0, possible = weight.
- **MISSING**: applicable required documentation is absent **after a bounded
  search** of approved docs/indexes/links; cite searched paths/patterns and the
  source establishing the need. Earned = 0, possible = weight. No guessed absence.
- **NOT_REVIEWED**: insufficient inspection/access/time, including unknown
  applicability; earned/possible = dash, not zero. Record why. Unread is not N/A.
- **N/A**: the check genuinely does not apply to this workflow; give a
  source-backed justification. Earned/possible = dash, excluded from scoring.

Do not turn unread files into failures or imply that a partial inspection
describes all docs. Missing source access is a limit, not a documentation defect.
Age, style preferences and missing decorative sections are not failures.
If no entry doc exists, establish relevant MISSING checks through search;
do not automatically fail checks whose applicability was not established.

## Deterministic calculation

- Assessed checks = PASS, FAIL or MISSING only.
- Earned points = sum of weights of PASS checks.
- Possible points = sum of weights of assessed checks.
- Scoped score = 100 * earned points / possible points; round only the final
  percentage to one decimal (half up). Show the raw earned/possible totals.
- Coverage denominator = sum of weights of all checks except justified N/A,
  **including NOT_REVIEWED**. Weighted coverage = 100 * possible points /
  coverage denominator, rounded the same way. Also show assessed check count,
  NOT_REVIEWED count, N/A count and named files inspected versus left uninspected.
- If possible points is zero: **No score / insufficient evidence**. Coverage
  is 0% if its denominator is positive; if all checks are N/A, coverage is
  **N/A - no applicable checks**, not 100%.
- Any NOT_REVIEWED check or unfinished approved scope makes the score
  **Provisional - incomplete scope**, even if the numerical score is 100%.
  Always disclose exclusions and limits, even with 100% weighted coverage.

This scoring covers all ten checks, not just the maximum two findings.
Summarize other failed/missing checks in the score table without implying
the finding cap means that no other gaps exist.

## Before and after

Preserve DOC-R1, exact scope/claims, check IDs/weights, applicability decisions
and the set of assessed checks. Reinspect against changed docs and the same
source scope. Show both earned/possible totals and coverage; improvement is
after percentage minus before percentage, in **percentage points**.
If scope, assessed checks, weights or N/A decisions change, mark **not comparable**
and explain rather than claim improvement. If either denominator is zero,
there is no comparable numeric delta.

## Synthetic arithmetic examples (not repository audit results)

- All ten PASS: 100/100 points, score 100.0%, coverage 100.0%.
- D1a PASS, D1b MISSING, other eight NOT_REVIEWED: 15/30 points,
  score 50.0%, coverage 30.0%, provisional (2 assessed / 8 unreviewed / 0 N/A).
- Same checks/scope after D1b becomes PASS: 30/30 points, score 100.0%,
  coverage still 30.0%, provisional; comparable increase 50.0 percentage points.
- All NOT_REVIEWED: no score; coverage 0.0%. All justified N/A: no score;
  coverage N/A. Neither case is a perfect score.

Prefer consequential missing/incorrect guidance over style. Seek scripts,
adapters or alternative docs that disconfirm a mismatch before reporting it.
