# Agentic Development with GitHub Copilot: self-paced lab

**40 minutes. Three introduction slides; work from this guide at your own pace.**
Use your own approved repository, not the public workshop kit.

**Agenda (IST):** GitHub introduction **09:50-10:10 (20 minutes)**;
self-paced lab **10:10-10:50 (40 minutes)**; break **10:50-11:00 (10 minutes)**.

## Suggested pace

| Lab minutes | Clock time (IST) | Do |
|---|---|---|
| 00-05 | 10:10-10:15 | Setup: approved repo, tools, small scopes and team roles |
| 05-13 | 10:15-10:23 | Documentation audit + transparent scoped score |
| 13-25 | 10:23-10:35 | Approved documentation fixes + reviewed PR |
| 25-33 | 10:35-10:43 | Bounded security triage + human review |
| 33-40 | 10:43-10:50 | One reviewed Jira ticket or actual local ticket file |

Teams of **THREE OR MORE** are encouraged; solo/pairs remain welcome.
One licensed driver, navigators/reviewers, one shared active run at a time.
Avoid duplicate AI-credit spend; do not share credentials. A teammate with
approved Jira access uses their own sign-in for that step, not a duplicate run.
The [bonus skill challenge](BONUS_SKILL.md) is optional, after core work/time permitting.

## 1. Setup (00-05)

Follow [README.md](README.md). Copy both `.github\agents` and
`.github\audit-guides` into the target repo without overwriting existing files.
Select VS Code **Local** and inspect each role's actual tools. Keep approvals on.
Choose a docs path plus relevant source/manifests, and one security entry point
plus its necessary callers/guards. Keep secret stores and production data out.
Use Auto where supported/allowed or an appropriate model; keep model/tools stable
within a coherent pass. No approved repo? Join an authorized team; don't relax policy.

## 2. Audit documentation and score (05-13)

Select **doc-auditor**. Replace brackets with actual approved paths:

```text
Audit [docs path] against [manifest and small relevant source scope].
Use documentation-checks, report-template and finding-template.
Report missing/incorrect docs with at most two actionable findings.
Apply rubric DOC-R1: show each check, earned/possible points, source evidence,
N/A reasons, unreviewed checks and weighted coverage. Score only inspected
applicable checks; mark incomplete scope provisional. No evidence/denominator
means no score. Read/search only; no execution, edits or external actions.
```

Open cited docs AND source; for missing docs, inspect the recorded search scope.
Check the score arithmetic and coverage. A high score with low coverage is not
repository health. Mark findings **Validated**, **Needs evidence**, or **Rejected**
with reasons. Agree which validated gaps to fix. Do not fabricate a demo score.
An optional **audit-reviewer** challenge adds usage; it is not required or human validation.

## 3. Fix agreed docs and open a PR (13-25)

Select the **Plan approved documentation fixes** handoff (`send: false`) or
select **doc-fixer** manually. This is a deliberate transition out of read-only
audit mode. Clicking a handoff does not approve edits or remote writes.

```text
Fix these validated findings and open a PR: [DOC IDs and evidence I checked].
First inspect only [exact target repo root], branch/status/diff and remote.
Propose the smallest docs-only changes to [exact allowed paths], new branch
[unused branch name] from [exact base branch], and existing checks to run.
Use pr-template. Do not edit or publish until I approve the plan.
Never use the public workshop repository as the destination.
```

Review the repo, remote, base, branch, proposed edits and check commands.
Copied kit agents/guides may be untracked: approve their exact path list to
remain unchanged/unstaged, outside the docs PR. Any other staged/working changes
or name collision require owner resolution; no reset, stash, overwrite or broad staging.
Approve a precise local plan:

```text
I approve the shown docs-only edits for [exact repo and paths], creating
[new branch] from [base branch], and these checks: [exact commands].
Make only these edits on the new branch, then show the full diff and actual
check outcomes. Do not commit, push or create a PR yet.
Leave these copied setup files unchanged and unstaged: [exact path list or none].
```

Inspect the actual diff. Ask **doc-auditor** to recheck the same DOC-R1 checks
against the same scope if time permits (read-only; no automatic second run).
Before/after is comparable only with the same assessed checks, weights, scope
and N/A decisions; otherwise label **not comparable** and explain. A planned
check is not a passed check.

After reviewing edits and results, approve the publication separately:

```text
I approve committing only [exact reviewed files/diff], pushing [new branch]
to [exact approved owner/repo and remote], and opening one PR into [base].
Use the reviewed PR title/body. Check for an existing PR first.
Never force-push, merge, deploy or include unrelated files.
Read back the created PR and report its actual URL, head and base.
```

`doc-fixer` uses approved Git and authenticated `gh` through its terminal tools;
no assumed GitHub MCP is required. Do not install/authenticate tools by exposing
tokens. If auth, policy, checks or remote tooling block completion, keep the
local docs edits/patch and PR draft in chat using the shared PR template.
State **PR not opened** (or **outcome unknown** after an ambiguous write).
Reconcile an uncertain create using approved read tools before any retry.
Never invent a PR URL. No supported docs gaps means no empty PR.

## 4. Security triage (25-33)

Start a new focused chat with **security-auditor**, passing scope facts rather
than the entire docs conversation:

```text
Inspect [one approved entry point/module] and [necessary callers/guards].
Use security-checks, report-template and finding-template. Read/search only.
Rank up to two evidence-backed findings CRITICAL, HIGH, MEDIUM, then LOW.
Include conditions, controls/counterevidence, impact and confidence separately
from severity. Put unconfirmed leads in Needs evidence, not vulnerabilities.
Disclose the scope and cap as triage, not completeness. No exploits, secrets,
security code edits or external writes. No supported findings is valid.
```

Open callers/guards and check required conditions. A human validates one
supported finding, or records that none was supported. Security remediation
is not part of this lab; tickets propose work for maintainer review.

## 5. Create one reviewed ticket (33-40)

Select **ticket-drafter** (or the security handoff, `send: false`):

```text
Prepare one ticket preview for [SEC finding ID] using ticket-template.
I personally checked [paths/lines] and validated [evidence and conditions].
Preserve [non-goals and confidentiality]. Show unknown owner/routing explicitly.
Preview in chat only for review; do not write a file or Jira record yet.
```

Review severity, evidence, expected versus actual behavior, remediation,
acceptance criteria, owner, routing, status and confidentiality.

### If you or a teammate has approved Jira MCP

Ask Copilot to create a ticket in your Jira project. Follow
[MCP-SETUP.md](MCP-SETUP.md): switch to normal **Agent**, select only approved
Jira MCP tools, search duplicates, approve the exact payload/destination and
read back the real ID/URL. Publish at most one ticket per team.

### Otherwise: create an actual local ticket

Stay with **ticket-drafter**. Choose a **new noncolliding path** in the target
repo, normally `lab-output\tickets\SEC-01.md` (match the selected finding ID).
Inspect the exact path directly (ignore rules can hide it from search);
if it exists, propose `SEC-01-02.md` or another unused
filename and obtain approval. Never overwrite. Then send:

```text
I approve creating exactly one new local file [exact target repo root]\
lab-output\tickets\SEC-01.md with the reviewed ticket content.
Label it Local / unpublished; no Jira ID or URL. Check that it does not exist,
create it with edit/createFile, then read it back and report the exact path.
Do not modify any existing file, commit, push or call external tools.
```

This is a real file, not just chat text. If the creation tool is unavailable
or fails, report **file not created** and retain the preview; do not claim the
local-ticket outcome is complete. If Jira creation failed or was ambiguous,
do not silently fall back: reconcile first, then obtain explicit approval for
a local alternative only after confirming no remote record exists.

If no security finding is validated, do not invent a ticket. Retain the
no-supported-findings/needs-evidence result and next owner check.

## Finish safely

Keep reports and local tickets in an approved private location. The kit's
`.gitignore` excludes `lab-output`, but copying only the two `.github` folders
does **not** copy that ignore rule: verify your target repo's exclusions with
the owner; never stage or publish the output directory automatically.
Do not put customer code, reports or security evidence in the public workshop
repo's issues/PRs/discussions. A local result is not externally published.
Capture the real PR URL or honest blocked state, score with coverage, and one
ticket's verified ID/URL or local path. Stop; no merges, deployment, security
auto-fixes, ticket transitions or extra paid runs.
