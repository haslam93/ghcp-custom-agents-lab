# Resources

Customization references checked against live official VS Code docs
**22 September 2026**. Existing billing references/copy were retained from
**10 September 2026**; recheck pricing and organization policy before a workshop.

## Intent, specifications and agent teams

- [GitHub Spec Kit](https://github.com/github/spec-kit)
- [Spec-driven development guide](https://github.com/github/spec-kit/blob/main/spec-driven.md)
- [Spec Kit documentation](https://github.github.com/spec-kit/)
- [Squad](https://github.com/bradygaster/squad) - a separate, community-maintained,
  experimental/alpha agent-team project; not required for this lab.

Spec Kit supports a specification -> plan -> tasks -> implementation workflow.
Use human review and real checks throughout. Squad coordinates agent teams;
additional agent passes consume additional usage. Review third-party setup
and retain your required approvals rather than copying bypass-approval flags.

## Copilot capabilities and interfaces

- [Copilot features](https://docs.github.com/en/copilot/get-started/features)
- [VS Code agent roles and harnesses](https://code.visualstudio.com/docs/agents/run/agent-harnesses)
- [Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli)
- [GitHub Copilot app](https://docs.github.com/en/copilot/concepts/agents/github-copilot-app)
- [Custom agents in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-agents)
- [MCP servers in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

## Customization: choose the right layer

| Resource | Use it for |
|---|---|
| [Customization overview](https://code.visualstudio.com/docs/agent-customization/overview) | Discover, manage and verify customizations for the selected harness |
| [Custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) | Repository/team rules applied automatically or by file scope |
| [Agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) | On-demand workflows with SKILL.md and linked supporting files |
| [Custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents) | Roles, tool lists and human-controlled handoffs |
| [Hooks](https://code.visualstudio.com/docs/agent-customization/hooks) | Preview lifecycle automation; review executable commands and policy first |
| [MCP servers](https://code.visualstudio.com/docs/agent-customization/mcp-servers) | Approved external tool integration; connection is not authorization |
| [Prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files) | Reusable manually invoked prompts, currently Local-only; deprecated and not loaded in Agent Host |
| [Agent plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins) | Package supported customizations; review provenance, permissions and harness support |
| [Built-in tool reference](https://code.visualstudio.com/docs/agents/reference/ai-features-cheat-sheet#_chat-tools) | Verify names against the actual tool picker before running |

**Harness caveat:** this kit uses `target: vscode` with the **Local** harness.
The official overview distinguishes Local and Agent Host; it says Local will
be removed in a future release. Do not assume these tool names, handoffs or
prompt-file support work unchanged in Agent Host, Copilot CLI or cloud. Validate
an adaptation with the facilitator if Local is unavailable; no bypass mode.

Frontmatter names checked against the official custom-agent and tool references:
`read/readFile`, `search/fileSearch`, `search/textSearch`, `search/codebase`,
`edit/editFiles`, `edit/createFile`, `execute/runInTerminal`,
`execute/getTerminalOutput`. No wildcard tool sets are enabled. Auditors have
only read/search; the fixer explicitly adds editing/terminal, while the local
ticket writer adds only creation. Unsupported tools may be silently ignored
by VS Code, so schema checks alone are not runtime verification.
Handoffs use `send: false`; previewing a prompt does not grant write approval.

## Billing and model choice

- [Models and token pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)
- [Organization and enterprise billing](https://docs.github.com/en/copilot/concepts/billing/organizations-and-enterprises/usage-based-billing)
- [Auto model selection](https://docs.github.com/en/copilot/concepts/models/auto-model-selection)
- [Optimize AI usage](https://docs.github.com/en/copilot/tutorials/optimize-ai-usage)
- [Monitor your usage](https://docs.github.com/en/copilot/how-tos/manage-and-track-spending/monitor-ai-usage)
- [Budget controls](https://docs.github.com/en/copilot/concepts/billing/budgets-for-usage-based-billing)

Model rates apply to billable input, cached input, cache writes where
applicable, and output tokens. One AI credit equals $0.01 USD. Included
credits and eligible additional usage are distinct from a flat price per
prompt. Paid code completions and next edit suggestions do not consume AI
credits. Current supported paid-plan Auto has a 10% model-cost discount,
not a license discount or a guarantee of the cheapest total task.

## This lab

- [Repository](https://github.com/haslam93/ghcp-custom-agents-lab)
- [Download ZIP](https://github.com/haslam93/ghcp-custom-agents-lab/archive/refs/heads/main.zip)
- [Self-paced guide](LAB_GUIDE.md)
- [Ticketing workflow](MCP-SETUP.md)
- [Spec template](SPEC_TEMPLATE.md)
- [Bonus skill challenge](BONUS_SKILL.md)
