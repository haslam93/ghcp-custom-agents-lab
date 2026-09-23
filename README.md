# Agentic Development with GitHub Copilot

**40-minute self-paced lab: audit and score docs, fix agreed gaps and open a PR,
then triage security and create one reviewed Jira or local ticket.**

## Workshop agenda (IST)

| Session | Time | Duration |
|---|---|---|
| GitHub introduction | 09:50-10:10 | 20 minutes |
| Self-paced lab | 10:10-10:50 | 40 minutes |
| Break | 10:50-11:00 | 10 minutes |

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
5. Open Copilot Chat and select the **Local** harness, then `doc-auditor`.
   This kit targets `vscode` with Local tool names, not Agent Host, CLI or
   cloud agents. Harness support differs; if Local is unavailable, have the
   facilitator validate an adaptation before running. See [RESOURCES.md](RESOURCES.md).
6. Inspect the actual tools for each role: the auditors/reviewer have only
   read/search; `doc-fixer` additionally has file editing/creation and terminal
   tools for approved Git, checks and GitHub CLI actions; `ticket-drafter`
   additionally has only file creation. Missing tools can be silently ignored
   by VS Code: resolve mismatches before running. Reload the window if needed.

Audits need no runtime, package installation or API key from this kit.
The fix/PR step needs Git, the repo's existing checks and approved authenticated
GitHub CLI (`gh`) for remote creation; without it, keep a local patch and PR
draft. Copilot needs working service access and an eligible plan. Keep tool
approvals enabled; no bypass-approval modes or permission-broadening prompts.

## One team, one active run

**Teams of THREE OR MORE are encouraged; solo participants and pairs are welcome.**
Use one shared screen and one active run: a licensed driver operates Copilot,
a navigator narrows scope, and a reviewer checks evidence, arithmetic and writes.
Others can review acceptance checks. Avoid duplicate runs to reduce duplicate
AI-credit spend, not per-token charges; no savings percentage is promised.
Teammates use their own authorized sign-in, never shared credentials or account
switching to evade a budget.

## Follow the self-paced workflow

Open [LAB_GUIDE.md](LAB_GUIDE.md) for the timeline and copyable prompts:

1. `doc-auditor` reports missing/incorrect docs, a transparent scoped score and
   coverage. A human checks the evidence and agrees which gaps to fix.
2. `doc-fixer` proposes a bounded docs-only plan, then makes approved edits on
   an approved new branch and runs approved existing checks. Inspect the diff;
   separately approve commit/push/PR. Accept a PR URL only from actual output,
   or retain an explicitly local patch and PR draft if blocked.
3. `security-auditor` inspects one bounded entry point, ranks supported findings
   **CRITICAL / HIGH / MEDIUM / LOW**, and keeps unconfirmed leads separate.
   This is static triage, not automatic security remediation.
4. Review one supported finding. **If you or a teammate has approved Jira MCP,
   ask Copilot to create a ticket in your Jira project** using [MCP-SETUP.md](MCP-SETUP.md).
   Otherwise `ticket-drafter` creates an actual approved new Markdown file at
   `lab-output\tickets\SEC-01.md` in the target repo using the shared template,
   labeled **Local / unpublished**, with no invented Jira ID.

**No supported findings is a valid result.** Do not invent gaps, scores, PRs
or tickets to finish the exercise. An uncertain Jira write must be reconciled
before any retry or local alternative; do not silently create a second ticket.

**Never upload your own repository, audit reports or security details into
this public training repository.** Save results only in an approved location.

## What's included

| Path | Purpose |
|---|---|
| `.github\agents\doc-auditor.agent.md` | Documentation claims versus actual repository evidence |
| `.github\agents\doc-fixer.agent.md` | Approved docs edits, checks and separately approved PR |
| `.github\agents\security-auditor.agent.md` | Bounded source-based security triage |
| `.github\agents\audit-reviewer.agent.md` | Optional second-pass challenge of a selected finding |
| `.github\agents\ticket-drafter.agent.md` | Reviewed preview and approved new local ticket file |
| `.github\audit-guides` | Scoring rubric, checklists and report/finding/ticket/PR formats |
| [LAB_GUIDE.md](LAB_GUIDE.md) | Copyable prompts and the self-paced 40-minute exercise |
| [SPEC_TEMPLATE.md](SPEC_TEMPLATE.md) | A small spec-first development template |
| [RESOURCES.md](RESOURCES.md) | Customization, Spec Kit, Squad, interfaces and pricing links |
| [BONUS_SKILL.md](BONUS_SKILL.md) | Optional challenge: package this workflow as an agent skill |

Use Auto when available and allowed, or choose a model appropriate to the
task. Keep scope and output small; preserve model/tools within a coherent
pass. Team review avoids duplicated work, not token charges. The optional
reviewer is an additional model pass and consumes additional usage.

## Presenter-only demo (optional)

[Presenter demo](presenter-demo/README.md) is separate from the participant lab.
Participants copy only `.github\agents` and `.github\audit-guides`; no demo files
or demo steps are required.

## Boundaries

Audit passes remain read-only. Only the explicit fixer/local-ticket transitions
permit approved writes. Tool selections and prompt restrictions are **not an
operating system sandbox**: editing and terminal tools have broader capability
than this workflow permits. Inspect discovered tools, retain human approvals
and obey policy. Do not attach prompts that broaden permissions. Jira creation
is a separate normal Agent step with only approved MCP tools. Never fix on the
base/main branch, force-push, merge, deploy, stage unrelated files, or publish
workshop results to this public repository.

This kit complements human review and established security tooling. It does
not promise a finding, complete coverage, exploitability, compliance,
offline Copilot, or a particular amount of cost savings.
