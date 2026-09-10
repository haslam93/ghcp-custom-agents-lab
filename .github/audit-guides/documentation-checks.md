# Documentation inspection checklist

Use these dimensions as a coverage map, not a scorecard or a requirement to
find something in every category. Stay within the user's named scope.

| Dimension | Inspect | Useful evidence |
|---|---|---|
| Getting started | Runtime, install/start/check commands and prerequisites | Manifests, scripts, version configuration |
| Behavior and contracts | Documented inputs, outputs, errors and compatibility | Relevant implementation, callers and existing tests |
| Navigation and structure | Named components, important paths and referenced resources | Actual files, exports and repository layout |
| Configuration and operation | Defaults, configuration examples and troubleshooting claims | Approved example configuration and source; never secret stores |
| Examples and change guidance | Whether examples and contributor steps match current interfaces | Examples, command definitions, linked files and code |

For each applicable dimension, mark **Reviewed**, **Not reviewed**, or
**Not applicable - with evidence**. "Reviewed" means the named scope was
inspected, not that the entire dimension is correct across the repository.

Compare a specific claim with a specific fact. Look for scripts or adapters
that might explain an apparent mismatch before reporting it.
Missing source access is a limitation, not evidence of a defect.
Document age, writing style and missing decorative sections are not enough
to establish a consequential documentation gap.

Prefer findings that could prevent a reader starting, using or changing the
component correctly. Combine related symptoms and propose a minimal correction.
