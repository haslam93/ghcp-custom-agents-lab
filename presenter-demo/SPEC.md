# Release readiness: empty input

## Goal

A release cannot be considered ready when no check results are available.
This is a local teaching example, not a production release control.

## Scope

Change only `readiness.py` and `test_readiness.py` in this directory.
Preserve the `release_state(checks)` API and all existing behavior for
nonempty input. No new dependencies, files, network access, or release actions.

## Acceptance criteria

| Input | Expected outcome |
| --- | --- |
| `[]` | `"not_ready"` |
| `["passed"]` | `"ready"` |
| `["passed", "passed"]` | `"ready"` |
| `["passed", "failed"]` | `"not_ready"` |
| `["passed", "pending"]` | `"not_ready"` |
| `["unknown"]` | `ValueError` |

The function must not modify the supplied sequence.

## Evidence required

- A regression test covers the empty-input case.
- Show that test failing against the starting implementation.
- Make the smallest implementation change.
- Run the full test file and inspect the diff.
- Report the actual results, not an expected result as if it ran.

## Out of scope

Deployment, real release pipelines, credentials, audit agents, Jira, repository
configuration, participant lab material, committing, pushing, or opening a PR.
