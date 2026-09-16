# Claude Code — build context

**Read [`COLLABORATION.md`](COLLABORATION.md) first.** It holds the rules that apply in every context. This file holds what is specific to building.

---

## Your role here

**Low-level design, build, test, deploy.**

The work moves through: *ideate → plan → document → design → build → test → deploy.* Everything up to and including **high-level design and architecture** happens in the chat context and lands in `_design/`. **Design is the break point.** You own everything from low-level design onward.

So: how a thing is structured in the store, what the objects are, which requirements are unrecoverable — decided already, in `_design/`. Schema details, module boundaries, function signatures, test structure, deployment — yours.

---

## The design corpus is upstream and authoritative

**Do not edit `_design/`, `_backlog/`, or `_delivery/` unless explicitly asked to.** They are inputs.

Implementation will reveal problems with the design. It always does. When it happens:

> **Stop and surface it. Do not adjust the model to fit the code.**

Do not implement something that contradicts the corpus on the grounds that the corpus is wrong. It may well be wrong — changing it is a deliberate decision, made in the chat context, with the superseded reasoning recorded. It is not a side effect of a build session.

This is the sharpest drift risk across the boundary, and it is silent when it happens. A schema that quietly means something slightly different from the document that specified it will not announce itself.

**If you find yourself reinterpreting a definition to make an implementation work, that is the signal to stop.**

### Surfacing is a filed finding, not a chat message

Stopping is only half of it. A finding raised in conversation dies with the session.

**File it in [`_feedback/`](_feedback/README.md)** using the template there. Three classes, and only one of them stops the build:

| Class | What it is | Build |
|---|---|---|
| **Contradiction** | The corpus says two incompatible things, or something the implementation cannot satisfy | **Stop.** Do not pick a reading and proceed |
| **Gap** | The corpus does not say, and a choice is needed to continue | Continue — but **record the provisional choice before writing the code** |
| **Refinement** | Workable as specified; implementation suggests better | Continue. Batch these; never stop for one |

The gap case is the one that matters most, because silence is common and the build cannot halt each time. Filling a small silence and moving on is exactly the drift this exists to catch — **the record goes in first, or it is a rationalisation of a decision already embedded.**

You file findings. You do not close them: that happens in the chat context, by the GM.

---

## Before implementing an epic

Read, in order:

1. The epic in `_backlog/`
2. [`_design/Glossary.md`](_design/Glossary.md) — every domain term the epic uses is defined there
3. [`_design/Information-Architecture.md`](_design/Information-Architecture.md) — the object model
4. Whatever the epic's **Assumptions** table cites
5. [`_delivery/Issue-Conventions.md`](_delivery/Issue-Conventions.md), [`_delivery/Issue-Lifecycle.md`](_delivery/Issue-Lifecycle.md), [`_delivery/Test-Strategy.md`](_delivery/Test-Strategy.md), and [`_delivery/Environments.md`](_delivery/Environments.md) — how work is structured, tested, and deployed

The assumptions table exists so the reasoning does not have to be reconstructed. Take those as given; they are not the right thing to relitigate mid-build.

---

## Working an issue

**When asked to work an issue — "Work issue #12 following documented standards", or any wording like it — this section is the standard.** Follow every step, in order, whatever the prompt leaves out. A short prompt does not shorten the process, and it does not approve anything.

The steps are here. The reasons for them, and the GM's side of the workflow, are in [`_delivery/Issue-Lifecycle.md`](_delivery/Issue-Lifecycle.md). What an issue contains and the definition of ready are in [`_delivery/Issue-Conventions.md`](_delivery/Issue-Conventions.md).

### Ground rules

- **One issue per session.** Do not start, plan, or look ahead to any other issue.
- **Never** open or close an issue, and **never** merge a pull request. Open a pull request only where Phase 5 or §If you have to stop says to. **Never** create or rename a label. **Never** commit to `main`. **Never** edit `_design/`, `_backlog/`, or `_delivery/`.
- **Issues are written in the chat context**, only when the GM asks. Something that needs deciding is a finding, not a new issue.
- **The issue comments are the record.** If you cannot read the issue, change its labels, or post a comment, stop and say so in the terminal. Do not carry on without the record.
- Commands below use the GitHub CLI (`gh`). Any tool that does the same thing is fine.

### Labels

**Status — exactly one at a time.** Remove the old one in the same command that adds the new one:

```bash
gh issue edit <N> --remove-label backlog --add-label in-progress
```

| Label | Means | You set it |
|---|---|---|
| `backlog` | Written, not started | Never — the chat context does |
| `in-progress` | A session is working it | Phase 1 |
| `in-review` | Pull request open, waiting on the GM | Phase 5 |
| `blocked-decision` | Fails the definition of ready, has no type, or needs a decision | When stopping for that reason |
| `blocked-finding` | Waiting on a contradiction filed in `_feedback/` | When stopping for that reason |

**You set the `blocked-*` labels; you never clear them.** The GM or the chat context does, setting the issue back to `backlog`. **Closed** means the GM merged the pull request. If a label you need does not exist in the repository, stop and report it.

**Type — decides whether and how you work it:**

| Type label | What to do |
|---|---|
| `test` | Work it — tests only, see Phase 3 |
| `impl` | Work it — make the story's tests pass |
| `enabling` | Work it — prerequisites and infrastructure |
| `spike` | Work it — the output is a written answer, such as an ADR. No application code |
| `corpus` or `chat-context` | **Stop.** Not for Claude Code. Say so in the terminal and change nothing |
| none | **Stop.** Set `blocked-decision` and comment that the issue has no type |

Do not add or remove `rc-*` or `unrecoverable`. An issue labelled `unrecoverable` is never descoped to fit a session — see §Four requirements are unrecoverable below.

### Comments

**Every phase ends with a comment on the issue, posted before the next phase starts.** Each one opens with:

```
---
*🤖 This comment was generated by Claude Code*
---

## Phase <n> — <name>
```

Write the body to a file and post it with `gh issue comment <N> --body-file <file>`. State facts: what was read, done, run, and found. Paste test output rather than summarising it; if it is long, paste the summary and every failure in full.

### Phase 1 — Read

1. **Fetch the issue**: `gh issue view <N> --comments`.
2. **Stop at once if:**
   - it is closed;
   - it carries `blocked-decision` or `blocked-finding` — say which in the terminal and change nothing, because only the GM or the chat context clears those;
   - it carries more than one status label — report it and change nothing.
3. **Check the type label** against the table above.
4. **Read**, in order:
   - the story the issue names in `_backlog/`, then everything in §Before implementing an epic;
   - for an `enabling` or `spike` issue, the documents the issue cites.

   Every session reads, including one that resumes. Context does not carry over between sessions.
5. **Check the definition of ready**: all seven items in `Issue-Conventions.md`. If one fails, set `blocked-decision`, comment which item failed and why, and stop.
6. **Check `_feedback/` for a contradiction** against the design this issue rests on.
   - An open one already filed: cite it; do not file it again.
   - One your reading turns up: file it as described under §If you have to stop.

   Either way, set `blocked-finding`, comment with the finding's path, and stop.
7. **Continue by status label:**
   - **`backlog`, or no status label:**
     1. Create the branch `issue-<N>-<short-slug>` from the latest `main`.
     2. Set `in-progress`.
     3. Post the Phase 1 comment: the files read; in two or three sentences, what the issue asks for and what done looks like; any gaps found, or "None".
   - **`in-progress`** — an earlier session stopped part-way:
     1. Check out its branch.
     2. Find the last phase comment.
     3. Post a Phase 1 comment saying where you are resuming.
     4. Continue with the phase after that one. If the last comment was Phase 2, the plan still needs `approved` in this session.
   - **`in-review`** — the GM asked for changes:
     1. Find the pull request: `gh pr list --head <branch>`.
     2. Read its conversation (`gh pr view <PR> --comments`) and its line comments (`gh api repos/dgrimesii/Malvasia-Plays-DCC/pulls/<PR>/comments`).
     3. Check out the branch.
     4. Swap `in-review` for `in-progress`.
     5. Post a Phase 1 comment listing the requested changes.
     6. Continue at Phase 2, with those changes as its input. Update the same pull request; do not open a new one.

### Phase 2 — Plan

Build the plan from the issue and the files read. Add nothing the issue does not ask for.

**Comment** with:

- **Files** to create, change, or delete, and why. Code goes under `app/`.
- **Order** of the changes.
- **Tests** — each one, automated or manual, and its pass criterion. For a `test` issue, each test's link back to a clause of the assertion or demo.
- **Risks**, naming any of the four unrecoverable requirements the work touches.
- **Gaps** — each provisional choice, and the finding you will file for it before writing the code that depends on it.

### Gate — wait for approval

After the Phase 2 comment, **stop** and print:

```
✋ PLAN COMPLETE — REVIEW REQUIRED BEFORE BUILD
Plan posted on issue #<N>.
Reply "approved" to build, or "revise: <notes>" to change the plan.
```

**Write no code until the GM replies `approved` in this session.** The prompt that started the session is not approval. On `revise:`, post a revised Phase 2 comment and wait again.

### Phase 3 — Build

Build exactly the approved plan.

- **Record each gap before the code that depends on it.** Commit the finding file (from `_feedback/TEMPLATE.md`) to the issue branch first.
- **Commit in small steps.** Each message references the issue: `Refs #<N>`.
- **Comment on intent, not mechanics.** Every non-trivial change says why.
- **`test` issues:**
  - Write tests from the story's assertion and demo only.
  - Do not read the implementation branch or any existing implementation of the behaviour.
  - **Mark each new test as expected to fail**, using the test runner's own mechanism, with a reason that names the issue. Without the marks, CI turns red and deployment stops until the `impl` issue lands.
- **`impl` issues:**
  - You may read the tests.
  - **The only change you may make to a test is removing its expected-to-fail mark.**
  - If a test looks wrong, file a finding: a contradiction stops the build, a gap is recorded and the build continues.
- **`spike` issues:** write the answer where the issue says. Add no application code.
- **Nothing under `app/` reads the campaign folders.** The conversion job gets its source another way — see `_delivery/Hosting.md`.
- **Never write the pre-registered expectation.** It belongs to the GM, who writes it before the demo runs.

**Comment**: files changed, and any deviation from the plan with its reason — or "None".

### Phase 4 — Test

1. **Run the whole test suite** with the project's test command: the one in `app/README.md` once issue 1 has written it, and before then the one named in your plan.
2. **What passing means:**
   - Every test passes.
   - For a `test` issue, the new tests run and report as *expected failures*, not errors.
   - Nothing that passed before now fails.
3. **For an `impl` issue**, confirm that:
   - the marks it removed are gone;
   - no test still marked expected-to-fail now passes. A marked test that passes is behaviour nobody accepted, so report it.
4. **Anything that writes** is checked against the assertions of absence in `_delivery/Test-Strategy.md`.
5. **Tests run against fixtures**, never the live campaign record. **Automated tests make no live model calls** — they replay recorded responses. A live run happens only if the issue asks for it.
6. **If the story's demo needs a person**, write numbered steps: what to run, what to look at, and what counts as passing. If the issue has no pre-registered expectation for work accepted by demo, say so. Do not supply one.
7. **If a test fails**, fix the code and rerun. Do not hand over with failures.

**Comment**: the test output, the checks above with a result for each, and the demo steps — or "No manual demo".

### Phase 5 — Hand over

1. **Check the assertion.** Take each clause of the story's assertion, or of the issue's for an `enabling` or `spike` issue, and mark it met or not met.
   - If a clause is not met and the approved plan covers the fix, make it and repeat Phase 4.
   - If the fix needs work outside the plan, post a revised Phase 2 comment and wait for `approved` again.
2. **Push the branch and open the pull request:**
   - Title: `[#<N>] <issue title>`.
   - The body starts with `Closes #<N>`, then has the summary, the test results, a link to the demo steps, and the findings filed.
3. **Wait for CI** (`gh pr checks <PR> --watch`). If it fails, fix the problem and repeat Phase 4. Until issue 1 has created CI there are no checks to wait for: say so in the comment. Issue 1 itself must show its new CI passing.
4. **Set `in-review`**, removing `in-progress`.
5. **Comment**:
   - Summary.
   - Files changed.
   - Test results.
   - The assertion checklist.
   - The pull request link.
   - Findings filed.
   - Notes for any issue that depends on this one, or "None identified".
6. **Print and stop:**

```
⏸  AWAITING REVIEW
Pull request <link> is open for issue #<N>.
Demo steps, if any, are in the Phase 4 comment.
Merge to close the issue. This session is complete.
```

**Every issue ends here, demo or not.** The GM's merge closes it.

### If you have to stop

At any point, for any reason:

1. **Push the branch, if one exists**, so no work exists only on this machine.
2. **Leave one status label that tells the truth:**
   - `in-progress` if the next session can resume;
   - `blocked-decision` or `blocked-finding` if it cannot.
3. **Comment** with what was done, where it stopped, and why.

**A blocking finding goes to `main` by its own pull request.** A finding committed on a branch that never merges is invisible to the chat context, which is where findings are closed.

- Branch `finding/<N>-<short-slug>` from `main`.
- Commit only the finding file.
- Open a pull request that does **not** close the issue, and link it from the stop comment.

A non-blocking gap stays on the issue branch and reaches `main` with the issue's own pull request.

**Number a finding from every branch, not only `main`.** Findings sit on unmerged branches, so the next free number is found with:

```bash
git fetch origin
git log --all --name-only --format= -- _feedback/ | sort -u
```

---

## Four requirements are unrecoverable

If these are omitted, the capability is not delayed — it is **permanently impossible**, because the information is never captured. They will look like optional polish under delivery pressure. They are not.

| Requirement | Why it cannot be added later |
|---|---|
| **Speaker attribution** — an utterance and the claim it carries are separate records | A flattened statement puts a lie in the record's own voice. Recovering it means re-reading every session |
| **Two clocks** — record time and fiction time on everything | The strongest inference signal reads date-of-entry exclusively. Stamping conversion with today's date flattens the campaign's history, silently |
| **Comparable attributes** — a small typed form alongside the prose | Prose similarity is not machine-comparable. Retro-fitting means re-reading every character |
| **Per-fact visibility**, held per campaign | A file-level or single-valued flag cannot be split later without guessing, on the one axis where guessing spoils a campaign |

See [`_design/Roadmap.md`](_design/Roadmap.md) for the full statement.

---

## Standing constraints on what gets built

These are product constraints, not preferences, and they are easy to violate with a reasonable-looking implementation.

**No generation in extraction.** Stage 1 of intake extracts what the notes say and nothing more. Proposing fiction is a separate, later stage under [`_design/Generative-Projection.md`](_design/Generative-Projection.md).

**No manner, intent, or emotional state generated, ever.** [`_design/Constraint-Manner-and-Intent.md`](_design/Constraint-Manner-and-Intent.md).

**Detection must be deterministic.** A language model may extract and may generate; it may not decide what gets surfaced. An LLM in the detection path makes the golden corpus unreplayable, which removes the only regression test the judgment-bearing features will ever have.

**Nothing is written unreviewed.** Every proposal is accepted by the GM before it lands.

**Undetermined is a real displayed state, never a blank** — and nothing counts, flags, or nags about it. An unset field looks like a to-do; this one is not.

**Nothing arrives unasked at the table.** [`_design/Constraint-Serves-The-Table.md`](_design/Constraint-Serves-The-Table.md).

---

## Where your own design lives

Low-level design belongs **in the code and next to it** — schema definitions, module docs, ADRs in the source tree, docstrings, tests.

**Not in `_design/`.** That directory is system- and campaign-agnostic narrative design, deliberately free of implementation detail. Adding schema specifics to it breaks the portability the whole model is built for.

If a low-level decision turns out to have model consequences, that is exactly the case for filing a finding.

---

## Testing

Per [`_design/Verification-and-Challenge.md`](_design/Verification-and-Challenge.md) and the prerequisites in [`_design/Roadmap.md`](_design/Roadmap.md):

- **Tests run against fixtures, never the live campaign record.** It is irreplaceable and changes weekly.
- **The fixture corpus needs the awkward cases**, not just the happy path — legacy-shaped content, entities at a range of investment degrees including none recorded, and entities carrying a mix of known and unknown facts.
- Each story in an epic states its own **assertion** and **demo**. Those are the acceptance criteria; implement to them rather than to the story title.
