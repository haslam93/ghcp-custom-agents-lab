# Resources

Public references reviewed **10 September 2026**. Recheck versions, current
pricing and organization policy before a workshop.

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
