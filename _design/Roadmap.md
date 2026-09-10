---
type: design
status: draft
visibility: gm
tags: [product, roadmap, release, epics]
---

# Roadmap

Planned release candidates for **Storyteller** and the epic headlines in each.

Scope of this document is Storyteller only. Convergence with Chronicle is recorded at the end as strategic vision — **no epics are planned for it.**

Detail lives elsewhere: [[Sequencing]] for ordering rationale and model invariants, [[Release-Plan]] for the two-release split, [[Shippable-Increment]] for what "shippable" means.

---

## How to read this

A **release candidate** is a group of epics that belong together, not a delivery gate. Individual increments ship continuously inside each one — functional, non-breaking, testable, demoable, and not necessarily useful. Nothing waits for a candidate to complete.

Epics are headlines here. Full epics, with stories and acceptance criteria, are written per [[Epic-Writing-Standard]] as each candidate comes up.

Two releases:

- **Release 1 — the GM interface.** First user is the GM, who is also the builder.
- **Release 2 — the player interface.** Three users, two of them non-technical.

---

## Prerequisites

Gates, not features. Each is required before something else can start.

| | Item | Blocks |
|---|---|---|
| **P1** | Glossary, written for a reader who knows nothing | Writing any epic |
| **P2** | Test harness — run any increment against a fixture, print the output | The first increment |
| **P3** | Fixture corpus — a synthetic campaign, plus deliberately awkward cases | The first increment that writes campaign data |
| **P4** | Challenger protocol — the review question set and role separation | The first review |
| **P5** | Golden corpus — judged output, frozen as a regression suite | RC 1c |

**Already done, ahead of P1:** the capture templates carry the model invariants, so sessions recorded before the tool exists need no re-encoding later.

---

## Release candidates at a glance

| RC | Theme | Epics | Status |
|---|---|---|---|
| **1a** | The core loop | 1, 2, 3 | Ready to write |
| **1b** | Authoring and control | 4, 5, 11, 13, 17 | Ready to write |
| **1c** | The computed layer | 6, 7, 8, 14 | Blocked |
| **1d** | Durability | 12 | Blocked |
| **2a** | Players read the record | 9, 15 | Deferred to R2 |
| **2b** | Players contribute | 10, 16 | Deferred to R2 |

---

## RC 1a — The core loop

*A tool that earns its place at the table and after it.* The first candidate that is useful rather than merely shippable.

| # | Epic | What the GM gets |
|---|---|---|
| 1 | **Capture what happened in a session** | A record written cheaply after play, structured enough to reason over later |
| 2 | **Find anything, fast, at the table** | The right detail retrieved mid-sentence, while three people wait |
| 3 | **Know the next session is covered** | A trustworthy answer to *am I prepared*, backed by what was checked |

Epic 1 has the earliest deadline in the whole plan: unrecorded sessions are not recoverable, and sessions are being played now.

**Entry criteria:** P1–P4. Epic 2's acceptance criteria additionally need the connectivity decision.

---

## RC 1b — Authoring and control

*Prep moves into the tool rather than around it.*

| # | Epic | What the GM gets |
|---|---|---|
| 4 | **Author and connect campaign material** | Writing, editing, and linking without leaving what you're doing |
| 5 | **Bring in outside material and integrate it** | Synthesized drafts split into the things they imply, cross-referenced against what exists |
| 11 | **Control what the party knows** | Deliberate reveal — of an entity's existence, a name, a fact, a connection |
| 13 | **Get started** | Existing dossiers and the Floor 1 plan converted into the current shape |
| 17 | **Recognise that two records are the same thing** | Combining duplicates without losing either side's contribution |

Epic 11 sits here rather than later because Epics 4 and 5 produce content that must carry visibility from the moment it is written. Epic 17 is here because the same operation is needed again in 1c and 1d, and building it three times is the expensive outcome.

**Entry criteria:** RC 1a under way. Epics 4, 5, and 17 need the graph model decision to be written in detail.

---

## RC 1c — The computed layer

*The part that justifies the model: computation over what is already known.*

| # | Epic | What the GM gets |
|---|---|---|
| 6 | **Surface what could not have been noticed** | Cross-references at a scale beyond working memory, raised while you can act on them |
| 7 | **Run a thread across a campaign** | Threads recognised, watched, and planned from once they are real |
| 8 | **Feel the world moving without you** | Events elsewhere whose effects reach the party, surfaced when they are in reach |
| 14 | **Pace the campaign** | Notice a grind or a railroad forming, before it is either |

**Blocked** on where the line sits between surfacing and authoring. That decision determines whether these epics propose connections and gaps only, or story content as well — a materially different backlog either way.

**Entry criteria:** P5, plus that decision. Epic 14 additionally needs a campaign horizon; Epic 8 needs the canon recording scope.

---

## RC 1d — Durability

*The record stays recoverable rather than gradually poisoned.*

| # | Epic | What the GM gets |
|---|---|---|
| 12 | **Keep the record trustworthy** | Find bad data, remove it, and keep the good work built on top of it |

Late in R1 by design — the cheapest option that survives contact with a real error is the right one, and which option that is cannot be known until real errors have happened.

**One decision has an earlier deadline than the candidate:** whether deletion preserves enough information to repair later. Answer it during 1b, even though the work lands here.

---

## RC 2a — Players read the record

*The party consults the record of their own adventure.*

| # | Epic | Who gets what |
|---|---|---|
| 9 | **Players consult the record of their own adventure** | Plain-language questions, entity lookup, past sessions — never a spoiler, and never a doubt about whether they just saw one |
| 15 | **See what the party knows** | The GM, checking a page as the party sees it before running a scene |

Epic 15 is a GM capability that cannot exist until the player view does, which is why it waits here.

---

## RC 2b — Players contribute

*Their record sits alongside the world's, not beside it as scratch paper.*

| # | Epic | Who gets what |
|---|---|---|
| 10 | **Players contribute to the record** | Plain typing, attached to what it's about, attributed and shared |
| 16 | **Player attention as a prep signal** | The GM, seeing where the party's curiosity has run ahead of what's prepared |

Epic 16 needs 2a in real use before it has anything to read.

**R2 is unvalidated.** R1 is shaped entirely around one expert user who built it. Everything R1 legitimately skips — guidance, forgiving inputs, plain vocabulary, error messaging — returns as a requirement here. These epics are not a re-skin of a proven product.

---

## Strategic vision — convergence with Chronicle

**Not planned. No epics. No dates.** Recorded so near-term choices do not foreclose it.

Chronicle is a player-side record for a different campaign in a different game system, maintained by a scribe. Its first objective — tracking the relationships between people, places, and events as they emerge through play — is the same objective as Storyteller's, observed from the other side of the screen. Its second — a detailed, rules-grounded record of play — is precisely what [[Scope]] excludes here, and diverges structurally between game systems rather than merely in vocabulary.

So a shared substrate would be **entities, typed relationships, and events, as observed**, with the boundary at the event and system-specific detail beneath it opaque. See [[Shared-Core]] and [[Knowledge-Assets]].

**The posture:**

- Chronicle changes nothing.
- Storyteller designs so a mapping between the two models stays writable. A document, not code.
- Storyteller borrows freely in the other direction — the narrative/mechanics split, the relationship shape, the approve-before-commit pattern, the fixture and safe-test-mode discipline.
- Chronicle is the reference design for R2, which is the half Storyteller has barely specified.

**The guardrail:** convergence is about the data model, never the feature set. If a convergence argument ever concludes that Storyteller should track combat rounds, the argument has gone wrong.

**The standing test** for any near-term architecture decision: would this make two independently-built stores impossible to reconcile later?

---

## Open decisions gating the roadmap

| Decision | Gates |
|---|---|
| Is the graph model adopted? | Epics 4, 5, 7, 17 in detail |
| Where is the line between surfacing and authoring? | All of RC 1c |
| Does retrieval work with no connectivity? | Epic 2 acceptance criteria |
| Are tombstones preserved on deletion? | RC 1d — decide during 1b |
| Does the campaign have a known length? | Epic 14 |
| How much canon before Floor 6? | Epic 8 |
| Does anything reach players automatically? | RC 2a |

RC 1a and 1b can be written and started with only the connectivity answer.
