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

## Evidence-backed severity, separate from confidence

Sort supported findings in this order: **CRITICAL, HIGH, MEDIUM, LOW**.
Use these qualitative triage criteria, not invented CVSS or overall security scores:

| Severity | Evidence-backed impact and conditions |
|---|---|
| CRITICAL | Catastrophic compromise, such as broad privileged control or large-scale sensitive-data exposure, with a supported reachable path and no substantial prerequisite barrier in the inspected context |
| HIGH | Major confidentiality, integrity or availability impact through a supported path, with the relevant attacker access and prerequisite conditions explicitly evidenced |
| MEDIUM | Meaningful but bounded impact, or a supported issue constrained by significant prerequisites or effective limiting controls |
| LOW | Limited demonstrated impact with substantial constraints; still a concrete supported defect, not generic advice |

Explain why the observed impact/conditions fit the chosen tier. There is no
requirement to produce a CRITICAL, HIGH or MEDIUM finding (or any finding).
Unverified reachability/impact goes under **Needs evidence**, without a
vulnerability severity ranking; it is not a reason to inflate or lower a
guess into a supported finding. Keep confidence separately:

- **High confidence**: direct source evidence supports the scoped claim and
  relevant counterevidence was examined; runtime still not executed.
- **Medium confidence**: the core scoped source defect is supported, with
  clearly named residual uncertainty that does not invalidate the finding.
- **Low confidence**: insufficient support; record an unconfirmed lead, not
  a ranked vulnerability.

Use at most two supported findings in the workshop. Disclose that this cap and
the small inspected scope are **triage, not completeness**. Do not claim these
are the repository's top vulnerabilities. Avoid speculative CVEs, unsupported
severity, and generic hardening advice presented as vulnerabilities.

Propose a defensive correction and a safe regression-test idea for later
maintainer review. No exploit execution, weaponized payloads or secret values.
