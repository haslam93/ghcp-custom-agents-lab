# Self-paced lab: two audits, one next action

**40 minutes. No slide-by-slide lecture.**

Use one existing approved repository. Run both custom auditors, inspect their
evidence and draft one supported next action. If nothing is supported, retain
the honest result rather than inventing a defect or creating an empty ticket.

## Suggested pace

| Minutes | Do |
|---|---|
| 00-05 | Get the kit, open your repo, check agent discovery and tools |
| 05-15 | Run doc-auditor; open the documentation and source evidence |
| 15-25 | Run security-auditor; inspect callers, guards and limitations |
| 25-35 | Review both reports and draft one human-validated finding |
| 35-40 | Approved MCP ticket creation, or joint review of the draft |

Pairing is encouraged: one shared screen and one active run at a time.
Swap who leads and reviews between passes; the authorized account holder
operates the client. Do not share credentials or evade usage limits.

## 1. Get ready

Follow the six setup steps in [README.md](README.md). Copy both `.github\agents`
and `.github\audit-guides` into your target repo without overwriting existing
configuration. Open the target repo in VS Code, not this kit.

Choose two small scopes manually: a docs path with a related manifest/source,
and one relevant module/entry point for security. Do not begin with a
whole-monorepo scan. Keep production data and secret stores out of scope.

Use Auto where supported and allowed, or choose a model appropriate to the
task. Harder source reasoning can justify a more capable model.
Keep the model and tools stable within a coherent pass.

If no repo is approved, pair with an authorized participant or follow the
facilitator's example. Do not relax policy or upload a customer repo here.

## 2. Documentation audit

Select **doc-auditor**. Replace the brackets with actual paths:

```text
Audit [docs path] against [manifest and relevant source].
Use the documentation checklist, report template and finding template.
Keep the coverage table compact. Return at most two actionable gaps with
the docs claim, source evidence, file/line references, impact, confidence,
smallest correction and acceptance check.
Read/search only. No commands, edits, external tools or ticket creation.
```

Look for both sides of the evidence. Keep the output in chat or save it
manually in an approved location. Do not select the ticket handoff yet.

## 3. Security audit

Same repository, **new focused chat**, **security-auditor**. Supply relevant
scope facts instead of pasting the whole documentation conversation.

```text
Inspect [one approved module or entry point] and its necessary callers/guards.
Use the security checklist and shared report/finding templates.
Trace the trust boundary and actual controls. Return at most two supported
candidates with file/line evidence, required conditions, severity rationale,
confidence, uncertainty and a safe regression-test idea.
Read/search only. Do not execute exploits, expose secrets, edit or publish.
If none is supported, state that and the limits of the inspection.
```

Open the guards and callers. Static source triage is not a security
certificate. A no-supported-findings result completes this pass.

## 4. Human review, then one draft

Review both outputs. Mark each candidate **Validated**, **Needs evidence**,
or **Rejected**, with a reason. A model's confidence is not validation.

For an optional second model opinion, select **audit-reviewer** and provide
only one candidate and its approved evidence scope. This adds usage; it is
not required, and does not replace the human decision.

Select **ticket-drafter** only after identifying a finding and opening its
evidence:

```text
Draft one ticket for [DOC/SEC finding ID] using the ticket template.
I personally checked [paths/lines] and confirmed [specific evidence].
Preserve [scope, non-goals and handling limits].
Keep unknown routing fields explicit. Return Markdown in chat only.
Do not publish or claim duplicate search was performed.
```

If nothing is validated, keep a clearly labeled needs-evidence note instead
of a publish-ready ticket. Do not create a finding to satisfy the exercise.

## 5. Connect only if ready

If an owner-approved ticketing MCP is already enabled, use [MCP-SETUP.md](MCP-SETUP.md).
Normal Agent performs that separate action; the four custom agents stay
read-only. Publish at most one ticket per pair.

Without MCP, review the draft together: improve one acceptance criterion
and name the person responsible for the next action. This is a complete
lab outcome, not a failed integration exercise.

## Keep results private

Audit outputs may contain security-sensitive or proprietary evidence.
Do not paste them into this public repo's issues, pull requests or discussions.
Do not commit or upload them automatically.
Use only a team-approved destination and retain unresolved uncertainty.

Optional fixes belong after the exercise or in a later build sprint. Use a
normal Agent, a scoped plan, an appropriate branch and the repo's existing
checks. No automatic push, merge, deployment or ticket closure.
