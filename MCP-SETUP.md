# One reviewed Jira ticket, or an actual local ticket

MCP is Model Context Protocol: a way for Copilot to discover and call tools.
It is not authorization. **If you or a teammate has approved Jira MCP, ask
Copilot to create a ticket in your Jira project.** Use the already-working
connection; teammates use their own authorized sign-in, never shared credentials.
Jira is not preconfigured by this kit. Without approved working Jira MCP,
use the actual local Markdown file route in [LAB_GUIDE.md](LAB_GUIDE.md).

## Before the lab

The tool owner must approve the server/publisher/version, authentication,
allowlisting, exact Jira instance/project, item type and visibility. Use an
approved sandbox project if available. Use
least-privilege search/read/create permissions, not admin or delete rights.
Confirm the actual tool names, required schema fields and a synthetic
create/readback in the event's chosen client beforehand.

Use VS Code's **MCP: Add Server** with the owner's approved configuration.
Prefer approved SSO/OAuth or secure secret inputs; never paste tokens into
slides, prompts or the repository. **MCP: List Servers** can show discovery.
Merge with existing settings rather than replacing the user's configuration.

Do not set up a new connector during the seven-minute ticket window
(lab minutes 33-40; **10:43-10:50 IST**).
No working approved connector means an approved new local ticket file, not
just a chat draft. Failed or uncertain Jira creation is a different case:
reconcile before any retry or explicitly approved local alternative.

## 1. Prepare without writing

After security triage and human review of one ticket-template preview, switch
from `ticket-drafter` to normal **Agent**. Select only your approved Jira MCP
search/read/create tools; keep write approval on. Disable unrelated
command/edit/admin tools. Tool names and required payload fields vary by server;
inspect the discovered schema, do not copy invented tool names.

```text
Use only our approved Jira MCP search/read tools.
For this human-validated draft, the approved destination is
[exact Jira instance, project, item type, confidentiality and visibility].
Search for duplicates by component and symptom.
Show matches and the exact proposed create payload with all required fields.
Do not write anything. Stop if destination, permissions or fields are unclear.
```

A duplicate means show it and stop, not modify or append to it.
A failed search is not "no duplicates". Do not improvise shell/network
workarounds for unavailable or blocked tools.
Map the shared ticket template to the actual Jira schema without losing
severity, evidence, expected/actual, remediation/acceptance, owner, routing,
status and confidentiality. Jira priority mappings require owner agreement;
do not assume priority is the same as severity. Keep an unknown owner explicit.

## 2. Human approval of the exact payload

Read the proposed fields and confirm the destination may receive the evidence.
For sensitive findings, the owner's incident/disclosure process takes priority.
Only then provide explicit approval, for example:

```text
I approve creating exactly one ticket with the payload just shown in
[exact approved Jira instance/project, confidentiality and visibility].
Do not assign it to an agent, transition it, comment elsewhere or change
another record. After creation, read it back and show the actual ID, URL
and stored fields.
```

Do not send approval before seeing the payload. A changed payload or
destination requires new approval. Create at most one ticket per team, not
one per teammate. Do not publish the same ticket from a second machine.

## 3. Read back or reconcile

Compare the returned record with the approved title, evidence and acceptance
criteria. Report success only from the system's actual record, not a guessed ID.

If create times out or its outcome is unknown, **do not retry blindly**.
Use approved search/read tools to determine whether the record exists.
If the state remains unknown, preserve that uncertainty and ask the owner
to resolve it. **Do not silently create a local ticket or retry** while the
remote outcome is unknown. If absence is confirmed, obtain fresh explicit
approval before any retry or approved new local path/content.

At the end of the window, keep the reviewed preview and the accurate blocked/
unknown status if publishing is incomplete; that is not a verified Jira outcome.
No deletion, issue transition, merge, deployment or automatic follow-on work.

## 4. No MCP: local file route

Use `ticket-drafter`, not normal Agent with broader tools. Preview using
`.github\audit-guides\ticket-template.md`, approve the exact target repo,
content and unused filename `lab-output\tickets\SEC-01.md`, then create with
`edit/createFile` and read back. If occupied, select another filename and
approve it; preserve existing files. Label **Local / unpublished** with
**Jira ID: None - local only** and **Jira URL: None - local only**.
No commit/push; verify target-repo exclusions. If the tool cannot save the
file, report that the local write did not complete rather than claiming success.
