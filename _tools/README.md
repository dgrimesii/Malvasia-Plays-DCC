# Tools

Consistency checks over `_design/` and `_backlog/`. No dependencies — Python 3.11+ and git.

```bash
python3 _tools/check_links.py          # exits 1 on failure
python3 _tools/check_staleness.py      # report only
python3 _tools/check_definitions.py    # report only
```

These exist because the design corpus reached the size where **drift between documents is a bigger risk than gaps in them.** Each check targets a failure mode that actually occurred.

---

## The failure modes

| Mode | What happened | Caught by |
|---|---|---|
| **Broken link** | A document links to something renamed or never written | `check_links` |
| **Staleness** | The model moved, the epics didn't — Epic 1 predated claims, typed facts, and both clocks | `check_staleness` |
| **Parallel invention** | Two documents coined different names for one concept — `setting-time` versus fiction time | `check_definitions`, partly |
| **Miscitation** | An epic cited `Device-Context` as saying phone-and-one-handed; it said laptop. The citation is what let the wrong requirement survive review | **Nothing here** |
| **Ambiguous definition** | *External author* was read as external-to-the-people rather than external-to-the-campaign. Both readings agree in every common case, so the error was invisible until homebrew separated them | **Nothing here** |
| **Shared error** | Every document agreed on a wrong definition. Consistency checking cannot help — consistency is the problem | **Nothing here** |

**Three of the six are not mechanically detectable.** The checks reduce the noise so attention is available for the three that need a reader.

---

## `check_links.py`

Every `[[wikilink]]` in `_design/` and `_backlog/` must resolve to a document in one of those directories. Links inside backticks or fenced blocks are ignored — those are illustrative, not references.

**Exits non-zero.** Suitable as a gate.

Worth knowing: GitHub's code search gives false negatives on this repo — it reported no match for a file that plainly existed. Cloning and checking locally is both faster and correct.

---

## `check_staleness.py`

If A links to B and B was committed after A, A may describe a version of B that no longer exists.

Defaults to a 7-day threshold, which skips same-week churn. During a heavy editing session nearly everything looks stale for a few hours; `--days 0` shows that and is rarely what you want.

**Report only, never a gate.** A flag means *reread this*, not *this is wrong*. Clear it by reviewing and touching the document, or by knowingly ignoring it.

Crude on purpose: false positives cost a glance, a missed staleness costs a wrong implementation.

---

## `check_definitions.py`

Finds Glossary terms that look re-defined outside the Glossary, by matching the restatement pattern — a bolded term followed by a dash or *is*. Lines that link to `[[Glossary]]` are skipped, since linking and then elaborating is the correct pattern.

**The rule it enforces:**

> A concept is defined in one document. Everywhere else links to it, and may state implications — never the definition.

Restating is tempting because it makes a document readable standalone, and it is exactly what creates a second copy to drift.

Over-reports by design. A term restated in one other document is often fine; **three is the signal worth a look.** Use `--min 3` for the short list.

---

## Practices the checks can't replace

**Record superseded reasoning in place.** `Canon.md` holds both earlier definitions and why each failed. That is what stops a resolved question being re-derived six weeks later.

**Strike resolved questions with the answer, don't delete them.** The history is the useful part.

**Give every definition a discriminating example** — one case that reads differently under the plausible misreading. *A homebrew GM's own cosmology is canon* would have caught the external-author ambiguity in a single line, years before homebrew came up.

**Assume the collaborator introduces drift.** Anyone working from context rather than from the file will restate definitions, work from stale copies, and occasionally guess an identifier rather than fetch it. Run the checks after a working session, not only before a release.
