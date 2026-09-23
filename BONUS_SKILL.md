# Optional bonus: package the workflow as an agent skill

**Participant challenge, after the 40-minute core lab/time permitting.**
No extra presentation or mandatory model run. This kit deliberately does not
ship a completed skill: you decide how to package and validate what you learned.

In your own approved repository, propose a new noncolliding skill folder such
as `.github\skills\agentic-development-lab`. Get owner approval before creating
files; do not overwrite existing customizations or include customer evidence.

## Challenge

Ask Copilot to help design a skill that guides the **entire workflow**:
scope/setup -> read-only documentation audit and DOC-R1 scoring -> human
validation -> approved docs fixes/checks/PR -> read-only security triage ->
reviewed Jira or actual local ticket. Preserve every permission transition.

Your deliverable is a `SKILL.md` plus appropriate supporting files, not a
monolithic pasted conversation. Use the
[official skill format](https://code.visualstudio.com/docs/agent-customization/agent-skills):

- YAML `name` matches the containing folder (lowercase letters/numbers/hyphens,
  max 64 characters).
- YAML `description` says what the workflow does **and when to use it**
  (max 1024 characters).
- Body explains inputs, ordered steps, decision/approval gates and stop states.
- Link supporting rubrics/templates/examples from `SKILL.md` with portable
  relative Markdown links. Copy only independently authored public kit
  material; preserve any attribution. Include small deterministic scripts
  only if useful and reviewed, never scripts that auto-publish.

Consider `disable-model-invocation: true` for a manually invoked workshop
workflow. Do not assume skill metadata restricts tools or sandboxes execution.
Skills inherit the harness/session's permissions; explicitly preserve role
changes and human confirmations. Local custom-agent tools/handoffs are not
automatically portable to Agent Host, CLI or cloud. Document what you tested.

## Acceptance challenge

Use only synthetic local fixtures, no real Jira tickets or PRs:

- Missing docs after search earn zero for assessed applicable checks; unread
  is NOT_REVIEWED, justified N/A is excluded. Zero denominator yields no score.
  Incomplete scope is provisional; before/after uses the same scope/checks.
- A rejected or unconfirmed security lead does not become a ranked vulnerability.
  Supported findings sort CRITICAL/HIGH/MEDIUM/LOW; confidence remains separate.
- Audit steps cannot silently write. Docs edits need approved paths/base/new
  branch/checks; commit/push/PR requires separate reviewed approval.
- Local ticket creation needs exact approved new path/content, preserves
  collisions and verifies readback. Jira needs duplicate check, exact
  payload/destination approval and actual ID/URL readback.
- An ambiguous remote write stops for reconciliation, not automatic retry
  or silent local fallback. Unavailable tools yield an honest blocked state.
- No secret values, security auto-fixes, forced findings, merges, public
  workshop outputs, or fabricated success claims.

Demonstrate activation in your actual harness, check linked resources load,
and show which approvals stop the workflow. A working skill is reusable
behavior with verified boundaries, not merely a file named `SKILL.md`.
