---
type: delivery
status: draft
visibility: gm
tags: [delivery, issues, process, lifecycle, labels]
---

# Issue Lifecycle

How an issue moves from written to closed, who moves it at each step, and what Claude Code posts along the way.

[[Issue-Conventions]] owns what an issue *is* — types, contents, the definition of ready. `CLAUDE.md` §Working an issue owns **the steps** Claude Code follows. This document owns the states, the reasons behind the steps, the GM's side, and the labels.

**Adapted from the Chronicle process** (`Chronicle-MagersCampaign/docs/chronicle-issue-prompt.md`): five phases, a comment at the end of each, a human gate between plan and build, and a manual-review hold before closing. That shape is kept. Three things change, and each is stated where it applies:

1. **Nothing is committed to `main`.** Chronicle's Phase 5 closes the issue directly. Here work ends in a pull request, and **the GM's merge closes the issue.** Claude Code never closes one.
2. **The test-first split.** A story's `test` and `impl` issues run the lifecycle separately, and the `test` issue has a different build and test phase.
3. **Findings stop the lifecycle.** Chronicle raises ambiguities in a comment. Here a contradiction is a file in `_feedback/`, and the issue is blocked until the GM closes it.

Everything below is a **proposal until the GM accepts it**.

---

## States

Status is carried by labels, one at a time, plus the open/closed state GitHub already has.

| State | Label | Meaning | Set by |
|---|---|---|---|
| **Backlog** | `backlog` | Written, not started. May not yet meet the definition of ready | Chat context, when writing the issue |
| **Blocked** | `blocked-finding` or `blocked-decision` | Cannot proceed until something outside the issue is settled | Claude Code, when it stops; or the chat context. **Cleared only by the GM or the chat context**, back to `backlog` |
| **In progress** | `in-progress` | A Claude Code session is working it | Claude Code, Phase 1 |
| **In review** | `in-review` | A pull request is open and waiting on the GM | Claude Code, Phase 5 |
| **Done** | *(closed)* | Pull request merged | GitHub, on the GM's merge |

**Remove the previous status label when setting the next.** Chronicle does not, and its closed issues carry `in-progress` and `in-review` together, which makes a label filter unreliable.

**No `resolved` label.** Chronicle has one, on three issues. Closed already says it, and a second marker drifts from the first.

**`corpus` and `chat-context` issues never enter this lifecycle in Claude Code.** They are worked in the chat context and closed there.

```
backlog ──► in-progress ──► in-review ──► closed (merge)
   ▲             │               │
   │             ▼               ▼
   └──────── blocked-*      changes requested ──► in-progress
```

---

## The phases

**READ → PLAN → gate → BUILD → TEST → HAND OVER.** The steps Claude Code follows — comments, label changes, branch and pull request, tests — are in `CLAUDE.md` §Working an issue, and only there.

> **Moved 2026-09-16.** This section first held the full steps, with `CLAUDE.md` linking to it. But the GM starts a session with a short prompt — *"Work issue #12 following documented standards"* — and `CLAUDE.md` is the one file Claude Code reads without being told to. Steps that only exist behind a link are steps a session can skip. So the steps moved to `CLAUDE.md`, and this document keeps the reasons for them.

What follows is the reasoning behind the steps that differ from Chronicle's, or are easy to misread.

**The plan gate is kept from Chronicle unchanged.** It is the cheapest point to catch scope moving, and the definition of ready says a paraphrase is where that happens. The prompt that starts a session never counts as approval.

**`test` issues mark their tests expected-to-fail.** Tests written before the behaviour exists fail. Merged unmarked, they turn CI red, and [[Render-Setup]] deploys only after CI passes, so a `test` pull request would stop every deployment until its `impl` lands. The marking lets the `test` pull request merge with CI green and still records that the behaviour is missing. **Removing the marking is the only change an `impl` issue may make to a test**, and a marked test that unexpectedly passes is reported, because it is behaviour nobody accepted.

**Every issue ends in `in-review`, demo or not.** Chronicle closes issues that have no manual tests itself. Here the merge is the close, and only the GM merges.

**A blocking finding goes to `main` in its own pull request.** A finding committed to an issue branch that never merges is invisible to the chat context, which is where findings are closed. A non-blocking gap rides the issue's own pull request, since that one does merge.

**A session resumes from the comments.** An issue found already `in-progress` means an earlier session stopped part-way. The last phase comment says where. This is why a comment is posted before each next phase and never batched at the end.

---

## After hand-over — the GM

| Outcome | Action |
|---|---|
| Demo passes, pull request is right | Merge. The issue closes |
| Something is wrong | Comment on the pull request and start a new session on the same issue. It reads the comments, sets `in-progress` again, and re-plans before changing anything |
| The design turned out wrong | Close the finding in the chat context first. The issue stays `blocked-finding` until then; closing the finding includes setting the issue back to `backlog` |
| Blocked on readiness | Fix the issue text in the chat context, then set it back to `backlog` |

---

## Starting a session

```
Work issue #<N> following documented standards
```

That is enough, because the whole procedure is in `CLAUDE.md`, which Claude Code reads without being told to.

~~A longer prompt, naming this document and the plan gate, with the issue number and URL filled in.~~ *Superseded 2026-09-16:* it existed because the steps lived here, behind a link. With the steps in `CLAUDE.md`, the GM's short prompt is sufficient, and a prompt that restates the process is a second copy to drift. Chronicle's long prompt made the same trade the other way, because its repository had nowhere else to hold the process.

---

## Labels

**Labels belong to a repository.** GitHub has no way to share one label across repositories, so Chronicle's cannot be used here and have to be created again.

### Carried from Chronicle

| Label | Colour in Chronicle | Keep? |
|---|---|---|
| `backlog` | `8b949e` | Yes — lifecycle state |
| `in-progress` | `0075ca` | Yes — lifecycle state |
| `in-review` | `ededed` (default grey) | Yes — lifecycle state. *Proposal:* give it a colour, since it is the one the GM filters on |
| `bug` | GitHub default | Already exists here |
| `regression` | `ededed` (default grey) | Yes — something that worked stopped working, which [[Shippable-Increment]] makes the one thing a release must not do |

### Not carried

| Chronicle label | Why not |
|---|---|
| `epic`, `version` | Epics and releases are not issues here — [[Issue-Conventions]] §The mapping |
| `wu-*` (work units) | `rc-1a` … `rc-1d` do that job |
| `feature`, `enhancement`, `refactor`, `testing`, `ideation` | Replaced by the issue-type labels |
| `ai` | No equivalent need yet |
| `resolved` | See §States |

### The full set for this repository

The labels in [[Issue-Conventions]] §Labels, the type labels proposed in [[Readiness-Checklist]] Stage 4, and the lifecycle labels above. From a terminal with the GitHub CLI signed in:

```
R=dgrimesii/Malvasia-Plays-DCC

# lifecycle
gh label create backlog          -R $R -c 8b949e -d "Written, not started"
gh label create in-progress      -R $R -c 0075ca -d "A Claude Code session is working it"
gh label create in-review        -R $R -c fbca04 -d "Pull request open, waiting on the GM"
gh label create regression       -R $R -c b60205 -d "Something that worked stopped working"

# type
gh label create test             -R $R -c 5319e7 -d "Tests from a story's assertion and demo"
gh label create impl             -R $R -c 1d76db -d "Make a story's tests pass"
gh label create enabling         -R $R -c 0e8a16 -d "Prerequisite or infrastructure; no user outcome"
gh label create corpus           -R $R -c c5def5 -d "Correction to _design or _backlog; chat context"
gh label create spike            -R $R -c d4c5f9 -d "Time-boxed question; output is a written answer"

# conventions
gh label create rc-1a            -R $R -c bfdadc -d "Release candidate 1a"
gh label create rc-1b            -R $R -c bfdadc -d "Release candidate 1b"
gh label create rc-1c            -R $R -c bfdadc -d "Release candidate 1c"
gh label create rc-1d            -R $R -c bfdadc -d "Release candidate 1d"
gh label create unrecoverable    -R $R -c b60205 -d "Touches one of the four unrecoverable requirements"
gh label create blocked-finding  -R $R -c e99695 -d "Waiting on a finding in _feedback"
gh label create blocked-decision -R $R -c e99695 -d "Waiting on an open decision in _design"
gh label create chat-context     -R $R -c c5def5 -d "Not for Claude Code"
```

Colours other than Chronicle's two are placeholders; change them freely.

**Or copy Chronicle's wholesale** with `gh label clone dgrimesii/Chronicle-MagersCampaign -R $R`, then delete what the table above does not carry. More steps than creating the few that are wanted.

---

## Open

| Question | Why it matters |
|---|---|
| Is status also tracked on a GitHub Project board? | Chronicle's Phase 1 says "set the status to In Progress", which reads like a board field, and its Phase 5 says to check the board for the next issue. **A Project board, unlike a label, belongs to the account and can span both repositories.** If one is used, decide whether it or the labels is the record, so the two cannot disagree |
| Does a `test` issue's pull request merge before its `impl` issue starts? | The expected-to-fail marking above assumes yes. The alternative is the `impl` branch built on the unmerged `test` branch, which avoids the marking and makes the `test` pull request wait |
