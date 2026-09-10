# Security inspection checklist

This is an authorized source-inspection guide, not an execution or attack
playbook. Use only the selected module and necessary related callers/guards.

| Dimension | Questions for source review |
|---|---|
| Entry point and trust | Who calls this path? Which inputs cross a trust boundary? What assumptions are explicit? |
| Identity and authorization | Where is identity established? Is permission checked for the requested operation and resource? |
| Input and sensitive operations | How does data reach queries, file access, rendering or other sensitive operations? Which controls apply? |
| Data handling and observability | What is exposed, logged or returned? Are sensitive values handled appropriately? Never reproduce them. |
| Dependencies and configuration | Which versions/settings are actually evidenced? What requires an owner or verified advisory to assess? |

For each dimension use **Reviewed**, **Not reviewed**, or
**Not applicable - with evidence**. Inspect existing controls and framework
behavior before deciding that a boundary is insufficient.

A supported candidate needs a concrete source path, a consequence, the
conditions required, controls examined and remaining uncertainty.
If reachability, deployment configuration or an external service is unknown,
say so. Do not probe a live system to close the gap.

Use High/Medium/Low severity with a reason grounded in impact and conditions,
not an invented CVSS score. Avoid padding the report with speculative CVEs
or generic hardening advice presented as vulnerabilities.

Propose a defensive correction and a safe regression-test idea for later
maintainer review. No exploit execution, weaponized payloads or secret values.
