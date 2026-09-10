# Optional ticketing through MCP

MCP is Model Context Protocol: a way for Copilot to discover and call tools.
It is not authorization. Jira and other ticketing systems are possible
destinations, not preconfigured or assumed integrations.

## Before the lab

The tool owner must approve the server/publisher/version, authentication,
allowlisting, exact sandbox project, item type and visibility. Use
least-privilege search/read/create permissions, not admin or delete rights.
Confirm the actual tool names, required schema fields and a synthetic
create/readback in the event's chosen client beforehand.

Use VS Code's **MCP: Add Server** with the owner's approved configuration.
Prefer approved SSO/OAuth or secure secret inputs; never paste tokens into
slides, prompts or the repository. **MCP: List Servers** can show discovery.
Merge with existing settings rather than replacing the user's configuration.

Do not set up a new connector during the five-minute publish window.
No working approved connector means a reviewed draft.

## 1. Prepare without writing

After both audit passes and human review, switch from the custom auditor or
drafter to normal **Agent**. Select only approved ticket search/read/create
tools; keep write approval on. Disable unrelated command/edit/admin tools.

```text
Use only our approved ticketing MCP search/read tools.
For this human-validated draft, the approved destination is
[system, sandbox project, item type and visibility].
Search for duplicates by component and symptom.
Show matches and the exact proposed create payload with all required fields.
Do not write anything. Stop if destination, permissions or fields are unclear.
```

A duplicate means show it and stop, not modify or append to it.
A failed search is not "no duplicates". Do not improvise shell/network
workarounds for unavailable or blocked tools.

## 2. Human approval of the exact payload

Read the proposed fields and confirm the destination may receive the evidence.
For sensitive findings, the owner's incident/disclosure process takes priority.
Only then provide explicit approval, for example:

```text
I approve creating exactly one ticket with the payload just shown in
[exact approved sandbox project and visibility].
Do not assign it to an agent, transition it, comment elsewhere or change
another record. After creation, read it back and show the actual ID, URL
and stored fields.
```

Do not send approval before seeing the payload. A changed payload or
destination requires new approval. Do not publish the same ticket from
the second person's machine.

## 3. Read back or reconcile

Compare the returned record with the approved title, evidence and acceptance
criteria. Report success only from the system's actual record, not a guessed ID.

If create times out or its outcome is unknown, **do not retry blindly**.
Use approved search/read tools to determine whether the record exists.
If the state remains unknown, preserve that uncertainty and ask the owner
to resolve it.

At the end of the window, keep the reviewed draft if publishing is incomplete.
No deletion, issue transition, merge, deployment or automatic follow-on work.
