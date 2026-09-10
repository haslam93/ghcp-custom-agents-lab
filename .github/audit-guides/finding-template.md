# Finding format

## [DOC-01 or SEC-01]: [Specific, actionable title]

| Field | Required content |
|---|---|
| Status | Candidate - human review required, or Needs evidence |
| Impact / severity | High, Medium or Low, with a short rationale |
| Confidence | High or Medium, with the supporting reason and uncertainty |
| Claim | The documented claim or source behavior under examination |
| Evidence | Exact repository-relative paths and lines; short redacted excerpts where useful |
| Conditions | Affected reader/caller, trust boundary or circumstances required |
| Controls / counterevidence | Existing scripts, guards or alternate explanations examined |
| Consequence | Why the discrepancy or behavior matters |
| Minimal correction | Smallest proposed change; avoid unrelated refactoring |
| Acceptance check | An observable outcome or safe maintainer-reviewed regression-test idea |
| Limitations / handling | Unverified facts, inspection limits and any restricted visibility |

Use named symbols/headings when line numbers are unavailable and say why.
Never invent line references, test outcomes, advisory identifiers or secret
values. For DOC findings show both the documentation and code/config evidence.
For SEC findings show the path and relevant guards, not just a suspicious word.

If a candidate cannot be supported, leave it as needs-evidence or reject it.
An agent must never label its own finding human-validated.
