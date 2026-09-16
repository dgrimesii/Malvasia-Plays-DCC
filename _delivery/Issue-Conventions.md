---
type: delivery
status: draft
visibility: gm
tags: [delivery, backlog, issues, process, definition-of-ready]
---

# Issue Conventions

How an epic in `_backlog/` becomes something Claude Code can be told to work.

---

## Who writes issues

**Settled by the GM, 2026-09-16: Claude, in the desktop chat context, writes issues — and only when prompted.** Nothing is filed on Claude's own initiative, and Claude Code does not open issues for itself. The GM writes the pre-registered expectation.

---

## The mapping

```
Epic  →  Story  →  Issues
```

An epic is a body of value, not a delivery bundle — [[Shippable-Increment]] is explicit that its stories "may ship across a long span, in dependency order, with the epic incomplete and nothing wrong with that." Epics are never issues.

**A story is the unit of acceptance.** Its assertion and demo are the acceptance criteria, and [[Epic-Writing-Standard]] writes them to be observable. Nothing is restated into an issue; the issue points at the story.

**A story produces at least two issues**, per the role separation in [[Test-Strategy]]:

| Type | Contains | Order |
|---|---|---|
| `test` | The story's assertion and demo, verbatim. Tests written from the requirement | First, own session |
| `impl` | Make them pass | After |

Where a story is large enough that its assertion covers several independent behaviours, it splits into several test/impl pairs against the same story. It does not split into smaller stories — that is a `_backlog/` edit, made in the chat context.

**Three other issue types exist:**

- `enabling` — P2, P3, P4, P5, and the infrastructure in [[Hosting]]. Not stories, no user outcome, and [[Verification-and-Challenge]] warns these are "the first thing dropped when a feature runs long," so they get their own issues rather than being folded into feature work.
- `corpus` — a correction to `_design/` or `_backlog/`. **Worked in the chat context, never by Claude Code.** Tracked as an issue only so a build can be seen to be blocked on one.
- `spike` — a time-boxed question with a written answer as its output and no merged code.

**Findings are not issues.** They are files in `_feedback/`, closed by the GM in the chat context. An issue may be *blocked by* a finding; it never replaces one.

---

## Definition of ready

An issue may be started when all of these hold. If one does not, it is not refinement — it is blocked.

1. **It names its story**, by epic and story number, or is typed `enabling`.
2. **Its acceptance is the story's assertion and demo**, quoted rather than paraphrased. A paraphrase is where scope moves.
3. **Every term it uses resolves** in [[Glossary]]. A missing term means the glossary needs an entry, not that the issue can proceed.
4. **Its prerequisites exist.** P2 before any increment; P3 before anything that writes campaign data; P5 before inference.
5. **No blocking finding is open against the design it rests on.** A contradiction stops the build per `_feedback/README.md`.
6. **Explicit exclusions are stated.** Anything the story defers to a later release is named in the issue as excluded from acceptance — [[Roadmap]] records a case where a story carried an acceptance bar for a surface the release was not building, written in good faith, and it would have been implemented.
7. **The demo is runnable.** [[Shippable-Increment]]: "if there is no way to show it, it is not ready to be worked."

---

## What an issue contains

Short. The corpus holds the reasoning and the issue points at it.

```
Title:       [epic-NN/SNN] <story title> — test | impl
Type:        test | impl | enabling | corpus | spike
Story:       _backlog/Epic-NN-<name>.md § SNN
Assertion:   <quoted verbatim from the story>
Demo:        <quoted verbatim from the story>
Excluded:    <requirements belonging to a later release or surface>
Prereqs:     <issue numbers, or P2/P3/P4/P5>
Pre-registered expectation:   <for demo-accepted work — written before running>
```

**Do not restate the story.** `COLLABORATION.md`: a concept is defined in one place, and restating creates a second copy to drift. The issue is a pointer with acceptance attached.

**Reading order before starting** is already set by `CLAUDE.md`: the epic, [[Glossary]], [[Information-Architecture]], then whatever the epic's assumptions table cites. The assumptions table exists so the reasoning does not have to be reconstructed, and is not the right thing to relitigate mid-build.

---

## Labels

| Label | Meaning |
|---|---|
| `rc-1a` … `rc-1d` | Release candidate, per [[Roadmap]] |
| `unrecoverable` | Touches one of the four requirements that cannot be added later |
| `blocked-finding` | Waiting on a finding in `_feedback/` |
| `blocked-decision` | Waiting on an open decision in `_design/` |
| `chat-context` | Not for Claude Code |

**`unrecoverable` earns its own label** because [[Roadmap]] warns these "will look like optional polish under delivery pressure." The four are speaker attribution, two clocks, comparable attributes, and per-fact visibility. An issue carrying that label is never descoped to fit a session.

---

## The first issue

**Not a story.** A deployed application at its real addresses, on the target store, serving nothing.

> `[enabling] Walking skeleton — deploy to all three environments`
>
> **Assertion:** The application responds at `test.warpandweft.ink` and at `storyteller.warpandweft.ink`, backed by a Postgres instance per environment, with schema migrations applied as a discrete step. Production carries the access boundary; test does not. The test environment holds no credential that can reach the production store.
>
> **Demo:** Open both URLs. Show the migration applied in each. Show the test environment failing to reach production data.
>
> **Excluded:** Any campaign data, any domain model, any interface.

It clears [[Shippable-Increment]] exactly — functional, non-breaking, testable, demoable, and **not useful**, which that document explicitly permits.

It goes first because two R1 acceptance criteria assume a deployed environment already exists: Epic 2 S2 measures latency over the network, and Epic 13 S11 asserts the campaign is reachable at its path. Building the pipeline while a story is waiting on it is how the pipeline gets shortcuts in it.

---

## Ordering after that

[[Roadmap]] sets RC 1a as Epics 1, 2, 3, 13, and notes that the order value arrives in is not the order the tool gets used: "Epic 13 lands, the campaign is in the store, and the next thing that happens is the GM prepares."

But Epic 13 converts the live record into production, which is the irreversible act. Epic 1 carries the earliest deadline — sessions are being played now and unrecorded ones are not recoverable.

**So the working order is Epic 1 first, Epic 13 at cutover**, with conversion exercised against legacy-shaped fixture content long before it touches the real thing. The cutover date is a decision, not an arrival — [[Store-and-Access]] asks for it to be chosen, and nothing has chosen it yet. See [[Readiness-Checklist]].
