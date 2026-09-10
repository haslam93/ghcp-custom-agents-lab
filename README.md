# GitHub Copilot Custom Agents Lab

**Open VS Code. Bring an approved repo. Run both audits. Turn evidence into action.**

This public workshop kit contains independently authored custom agents,
checklists and report templates. It does not contain customer source code,
customer audit results, credentials or an installed ticketing connector.

## Get the kit

[Download ZIP](https://github.com/haslam93/ghcp-custom-agents-lab/archive/refs/heads/main.zip)
or clone:

```text
git clone https://github.com/haslam93/ghcp-custom-agents-lab.git
```

## Set up in your own repository

1. Open VS Code and sign in with your own licensed, organization-approved
   GitHub Copilot account.
2. Download and extract this kit, or clone it into a separate folder.
3. Copy **both** `.github\agents` and `.github\audit-guides` from the kit into
   your existing approved repository's `.github` folder. Include hidden
   folders. Preserve your team's existing files; do not overwrite a name
   collision.
4. Open **your repository** in VS Code. The downloaded kit is the toolbox,
   not the code you are meant to audit.
5. Open Copilot Chat. Select **Local** if a Session Target picker is shown,
   then select `doc-auditor` or `security-auditor` in the agent picker.
   These agents use VS Code's local read/search tool names.
6. Check the actual tool list: read/search only. If discovery or permissions
   differ, stop and resolve that before running. Reload the window if needed.

No runtime, package installation or API key is required by this kit.
Copilot still requires working service access and an eligible plan.
Do not use bypass-approval modes or override the agents' tool lists.

## Run both audits

Work in pairs if useful: **one shared screen, one active run at a time**.
One person leads the docs pass while the other opens the evidence; swap
lead/reviewer roles for security. The licensed account holder operates the
client. No credential sharing or switching accounts to evade a budget.

**First: select `doc-auditor`.**

```text
Audit [README/onboarding docs] against [manifest and relevant source].
Use the documentation checklist and report template. Stay within this scope.
Return at most two evidence-backed findings. Read/search only; no edits,
commands or external actions.
```

**Next: start a new focused chat and select `security-auditor`.**

```text
Audit [one approved entry point or module] and its relevant callers/guards.
Use the security checklist and report template. Trace the trust boundary.
Return at most two supported candidates with evidence and uncertainty.
Read/search only. Do not execute exploits, expose secrets or publish anything.
```

The agents produce a compact coverage table plus structured findings, not
just free-form commentary. **No supported findings is a valid result**.
It is not a security certification or a reason to invent a defect.

## Review and act

Open the cited files from both reports. A human marks each candidate
validated, needs more evidence, or rejected. Select one validated finding.
Use `ticket-drafter` to produce a Markdown ticket in chat.

If an approved Jira or other ticketing MCP connection is already working,
follow [MCP-SETUP.md](MCP-SETUP.md): search duplicates, preview the exact
payload and destination, explicitly approve one create, then read it back.
Otherwise keep a reviewed draft. Both outcomes complete the exercise.

**Never upload your own repository, audit reports or security details into
this public training repository.** Save results only in an approved location.

## What's included

| Path | Purpose |
|---|---|
| `.github\agents\doc-auditor.agent.md` | Documentation claims versus actual repository evidence |
| `.github\agents\security-auditor.agent.md` | Bounded source-based security triage |
| `.github\agents\audit-reviewer.agent.md` | Optional second-pass challenge of a selected finding |
| `.github\agents\ticket-drafter.agent.md` | One human-validated finding into a ticket draft |
| `.github\audit-guides` | Shared checklists and report/finding/ticket formats |
| [LAB_GUIDE.md](LAB_GUIDE.md) | Copyable prompts and the self-paced 40-minute exercise |
| [SPEC_TEMPLATE.md](SPEC_TEMPLATE.md) | A small spec-first development template |
| [RESOURCES.md](RESOURCES.md) | Spec Kit, Squad, custom agents, interfaces and pricing links |

Use Auto when available and allowed, or choose a model appropriate to the
task. Keep scope and output small; preserve model/tools within a coherent
pass. Pairing avoids duplicated work, not token charges. The optional
reviewer is an additional model pass and consumes additional usage.

## Boundaries

All four custom agents are read-only. Tool selections are not an operating
system sandbox: inspect actual discovered tools and respect organization
policy. Do not attach prompt files that broaden permissions. Publishing is
a separate, explicitly approved normal Agent step.

This kit complements human review and established security tooling. It does
not promise a finding, complete coverage, exploitability, compliance,
offline Copilot, or a particular amount of cost savings.
