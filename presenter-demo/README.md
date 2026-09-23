# Presenter demo: intent to a reviewed change

**Presenter only. This is separate from the participant audit lab.**

Use ordinary Copilot in VS Code, not the lab custom agents. The example is a
small Python helper with one deliberately incomplete behavior: an empty list
of check results currently returns `ready`. The agreed requirement is
`not_ready`. Nothing deploys, releases, or contacts a service.

## Prepare before presenting

1. Download the repository ZIP to a separate presenter workspace. Keep a clean
   copy outside the participant target repository.
2. Open **only `presenter-demo`** in VS Code. This keeps the lab agents and
   `.github` configuration out of the demo workspace.
3. Use Python 3.10 or newer and your approved Copilot sign-in. No package
   installation, API key, MCP connection, or GitHub write access is needed.
4. From this directory run `python -m unittest -v`. The five existing tests
   pass, but they do **not** cover the empty-input requirement.
5. Confirm the starting behavior with:
   `python -c "from readiness import release_state; print(release_state([]))"`.
   It prints `ready`. This is the intentional teaching gap, not a lab finding.
6. Keep `SPEC.md` open and use a suitable model or Auto. Rehearse before the
   session; if Python or Copilot access is unavailable, use the explicitly
   labelled walkthrough below rather than installing software on stage.

## Five-minute run sheet

| Time | Screen action | Prompt or narration |
| --- | --- | --- |
| 0:00-0:45 | Open `readiness.py` and `test_readiness.py`. | **Explain:** "Explain this helper and its current test coverage. Cite the relevant lines. Do not edit or run commands yet." |
| 0:45-1:30 | Open `SPEC.md`; use Plan where available. | **Plan:** "Read SPEC.md. Propose the smallest change and regression test. Only readiness.py and test_readiness.py are in scope. Wait for approval." |
| 1:30-3:30 | Approve the bounded plan; use normal Agent. | **Implement:** "Proceed with that plan. Add the empty-input regression test first and run it to show the failure. Then implement the fix and run the full test file. Ask before executing commands. Do not touch any other files or make remote changes." |
| 3:30-4:30 | Show diff and actual test output. | **Review:** "Summarize the changed behavior, the actual checks run, and anything unverified. Compare the result with SPEC.md." |
| 4:30-5:00 | Point to model and usage controls. | A narrow task, explicit acceptance criteria, a small diff, and observable evidence. Review or keep the change deliberately. |

If the model proposes unrelated changes, reject them and restate the two-file
scope. Do not show a prepared success as a live execution.

## Prepared fallback (not a live run)

Show `SPEC.md` next to the starting code. Explain that Python's `all([])` is
`True`: the current tests pass while the newly specified behavior is missing.
A minimal candidate implementation is:

```python
return "ready" if checks and all(status == "passed" for status in checks) else "not_ready"
```

The additional regression test is:

```python
def test_empty_checks(self):
    self.assertEqual(release_state([]), "not_ready")
```

This is a **prepared candidate**, not evidence of a live run. The presenter
must run it in a disposable rehearsal copy to demonstrate the result.

## Isolation and reset

- Participants continue to install only the two `.github` folders described in
  the main README. They do not run this demo or copy its files into their repo.
- The example does not install instructions, hooks, skills, agents, or MCP
  configuration. The skill-building challenge belongs to the lab, not here.
- After the demo, retain or discard your dedicated presenter copy. To start
  again, extract a fresh copy into a new directory. Do not reset a shared or
  participant repository.
