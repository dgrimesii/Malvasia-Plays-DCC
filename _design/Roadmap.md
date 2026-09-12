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

## What Release 1 is actually about

**Infrastructure and information architecture, with just enough interface to operate and verify them.**

Worth stating plainly, because the epics are written from the GM's point of view and can read as a product brief. They are not. The durable output of R1 is a correct store: facts as objects, per-fact provenance and visibility, two clocks, statements held apart from world facts, places nesting to any depth. The interface exists so those can be exercised and demonstrated.

**Stories are accepted on what the output contains and how fast it arrives** — not on layout, density, or visual treatment. Where an epic notes a stronger presentation requirement, it is recorded as a known requirement of a later surface and excluded from acceptance.

Two things this does *not* license:

- **The data still has to carry what a later interface will need.** A glanceable table view is only possible later if state, visibility, both dates, and truth-as-three-values were recorded per fact from the first session. Deferring a visual bar is cheap; deferring a field is permanent.
- **R2 is where interface returns as a real requirement**, and it is not a re-skin. See the R2 note below.

Per [[Device-Context]], every R1 surface is desktop or laptop, with a laptop or tablet at the table. **No GM surface targets a phone**, so nothing in R1 is one-handed, glanceable, or space-constrained.

### The first real use is a prep week

RC 1a reads table-first — capture, retrieval, readiness — but that is the order the *value* arrives in, not the order the tool gets used.

In practice: Epic 13 lands, the campaign is in the store, and the next thing that happens is the GM prepares. A table session follows a week later. So the prep-tier query path in Epic 2, and the readiness question in Epic 3, are exercised in anger before any at-the-table story is.

That matters for sequencing within the candidate, and for what the first demo should be.

---

## Prerequisites

Gates, not features. Each is required before something else can start.

| | Item | Blocks |
|---|---|---|
| **P1** | Glossary, written for a reader who knows nothing | Writing any epic |
| **P2** | Test harness — run any increment against a fixture, print the output | The first increment |
| **P3** | Fixture corpus — a synthetic campaign, plus deliberately awkward cases and legacy-shaped content | The first increment that writes campaign data |
| **P4** | Challenger protocol — the review question set and role separation | The first review |
| **P5** | Golden corpus — judged output, frozen as a regression suite | RC 1c |

**P1 is done.** [[Glossary]] is written and maintained.

**P5 carries a design constraint, not just a task.** A frozen regression suite only works if clue detection is deterministic — otherwise a changed result cannot be attributed to the code change rather than to sampling variance. That is what forces detection to be procedural while extraction and generation may use a language model. See [[Inference-and-Candidate-Relationships]].

**P3 has a new requirement** from the epic reconciliation: the fixture needs entities at a range of investment degrees including some with none recorded, and entities carrying a mix of known and unknown facts. Without those, Epic 2 S12 and Epic 3 S10 cannot be exercised.

**Already done, ahead of P1:** the capture templates carry the model invariants, so sessions recorded before the tool exists need no re-encoding later.

---

## Release candidates at a glance

| RC | Theme | Epics | Status |
|---|---|---|---|
| **1a** | The core loop | 1, 2, 3, 13 | Written and reconciled to the model |
| **1b** | Authoring and control | 4, 5, 11, 17 | Ready to write |
| **1c** | The computed layer | 6, 7, 8, 14 | Unblocked; entry on P5 |
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
| 13 | **Move the campaign in without losing anything** | Months of existing writing converted, with proof nothing was lost |

Epic 1 has the earliest deadline in the whole plan: unrecorded sessions are not recoverable, and sessions are being played now.

Epic 13 was moved here from 1b by [[Migration]]. Epics 2 and 3 are demonstrations rather than tools until the real campaign is in the store — retrieval over an empty store returns nothing, and readiness over an empty store reports everything uncovered.

### Four requirements here are unrecoverable

Not merely unbuilt if omitted — permanently impossible, because the information is never captured. They are the reason this candidate is about the store rather than the screen.

| Requirement | Where | Why it cannot be added later |
|---|---|---|
| **Speaker attribution** | Epic 1 S6 | A flattened statement puts a lie in the record's own voice; recovering it means re-reading every session |
| **Two clocks** | Epic 1 S14, Epic 13 S13 | The strongest inference signal reads date-of-entry exclusively. Stamping conversion with today's date flattens the whole campaign's history, silently |
| **Comparable attributes** | Epic 1 S15, Epic 13 S14 | Prose similarity is not machine-comparable; retro-fitting means re-reading every character |
| **Per-fact visibility** | Epic 1, Epic 13 S3 | A file-level flag cannot be split into per-fact values later without guessing, on the one axis where guessing spoils a campaign |

**Entry criteria:** P1–P4.

---

## RC 1b — Authoring and control

*Prep moves into the tool rather than around it.*

| # | Epic | What the GM gets |
|---|---|---|
| 4 | **Author and connect campaign material** | Writing, editing, and linking without leaving what you're doing |
| 5 | **Bring in outside material and integrate it** | Synthesized drafts split into the things they imply, cross-referenced against what exists |
| 11 | **Control what the party knows** | Deliberate reveal — of an entity's existence, a name, a fact, a connection |
| 17 | **Recognise that two records are the same thing** | Combining duplicates without losing either side's contribution |

Epic 11 sits here rather than later because Epics 4 and 5 produce content that must carry visibility from the moment it is written. It is also where Epic 2 S12's appetite gets satisfied — R1a shows the GM what is unshared, and this is where they can act on it. Epic 17 is here because the same operation is needed again in 1c and 1d, and building it three times is the expensive outcome.

Epic 5 is the tool's side of the cycle in [[Planning-Loop]]: the GM synthesises outside the tool and loads the result, iterating until they sit down at the table.

**One decision to make during this candidate, for work landing in 1d:** whether deletion preserves enough information to repair later. Note tombstones are inference substrate as well as repair substrate.

**Entry criteria:** RC 1a under way. *(The graph model decision that formerly gated this is resolved — see below.)*

---

## RC 1c — The computed layer

*The part that justifies the model: computation over what is already known.*

| # | Epic | What the GM gets |
|---|---|---|
| 6 | **Surface what could not have been noticed** | Cross-references at a scale beyond working memory, raised while you can act on them |
| 7 | **Run a thread across a campaign** | Threads recognised, watched, and planned from once they are real |
| 8 | **Feel the world moving without you** | Events elsewhere whose effects reach the party, surfaced when they are in reach |
| 14 | **Pace the campaign** | Notice a grind or a railroad forming, before it is either |

Epic 6 owns **stage 2 of intake** — impact detection over accepted changes, per [[Session-Capture]]. Epic 1 stops at stage 1, and the two must not merge: inference run over unreviewed extraction compounds a misreading into a conclusion.

**Formerly blocked on where the line sits between surfacing and authoring. That is now settled**, in two parts:

- **Surfacing is authoring.** Inference runs as a batch pass between sessions and is materialised as proposals through intake, rather than computed at query time. See [[Modes-and-Surfaces]].
- **Generation is permitted, forward only.** Proposing fiction that has not happened is allowed in stage 2 and in planning, never in extraction and never at the table. Investment gates it in reverse: low investment invites a proposal, high investment forbids it. See [[Generative-Projection]].

That makes Epic 6 larger than the headline suggests — it covers detection, the proposal queue, and the generative what-if — and the detective and generative halves have different rules. Worth splitting when the epic is written.

**Entry criteria:** P5. Epic 14 additionally needs a campaign horizon; Epic 8 needs the canon recording scope.

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

Epic 15 is a GM capability that cannot exist until the player view does, which is why it waits here. Note Epic 1 S12 needs a narrow forward slice of it during capture review, so that a mis-parsed statement is caught before it can reach a player.

Per [[Player-Scope]], the player surface replaces a notebook rather than adding a new capability, and must be answer-shaped rather than browsable — somewhere the party *checks*, not somewhere they dwell.

---

## RC 2b — Players contribute

*Their record sits alongside the world's, not beside it as scratch paper.*

| # | Epic | Who gets what |
|---|---|---|
| 10 | **Players contribute to the record** | Plain typing, attached to what it's about, attributed and shared |
| 16 | **Player attention as a prep signal** | The GM, seeing where the party's curiosity has run ahead of what's prepared |

Epic 16 needs 2a in real use before it has anything to read.

Epic 10 is bounded by [[Constraint-Serves-The-Table]]: **no player-facing write at the table, unconditionally.** Player notes happen after the session or during the week, never as an authoring surface open during play.

**R2 is unvalidated.** R1 is shaped entirely around one expert user who built it, on a full-size screen. Everything R1 legitimately skips — guidance, forgiving inputs, plain vocabulary, error messaging, and the whole of interface design — returns as a requirement here. These epics are not a re-skin of a proven product.

---

## Strategic vision — convergence with Chronicle

**Not planned. No epics. No dates.** Recorded so near-term choices do not foreclose it.

Chronicle is a player-side record for a different campaign in a different game system, maintained by a scribe. Its first objective — tracking the relationships between people, places, and events as they emerge through play — is the same objective as Storyteller's, observed from the other side of the screen. Its second — a detailed, rules-grounded record of play — is precisely what [[Scope]] excludes here, and diverges structurally between game systems rather than merely in vocabulary.

So a shared substrate would be **entities, typed relationships, and events, as observed**, with the boundary at the event and system-specific detail beneath it opaque. Each tool attaches its own context layer to the same shared things rather than holding a competing model of them. See [[Shared-Core]] and [[Knowledge-Assets]].

**The posture:**

- Chronicle changes nothing.
- Storyteller designs so a mapping between the two models stays writable. A document, not code.
- Storyteller borrows freely in the other direction — the relationship shape, the approve-before-commit pattern, and the fixture and safe-test-mode discipline.
- Chronicle is the reference design for R2, which is the half Storyteller has barely specified.

**The guardrail:** convergence is about the data model, never the feature set. If a convergence argument ever concludes that Storyteller should track combat rounds, the argument has gone wrong.

**The standing test** for any near-term architecture decision: would this make two independently-built stores impossible to reconcile later?

---

## Open decisions gating the roadmap

| Decision | Gates |
|---|---|
| Are tombstones preserved on deletion? | RC 1d — decide during 1b |
| What is the attention budget, as a number? | Nothing hard, but Epic 3 and Epic 6 both need one |
| Does the campaign have a known length? | Epic 14 |
| How much canon before Floor 6? | Epic 8 |
| Does anything reach players automatically? | RC 2a |

**Resolved since this document was written:**

- *Is the graph model adopted?* **Yes.** A graph domain model on a relational store, with a real database from RC 1a. [[Information-Architecture]] is written against it. This was the top gating decision and it is closed.
- *Where is the line between surfacing and authoring?* **Surfacing is authoring**, materialised through intake; generation is separately permitted forward-only. See RC 1c above.
- *Does retrieval work with no connectivity?* **No.** Web-first from day one at a registered domain, and the table has a reliable connection. Epic 2 instead requires that an unreachable store announces itself within seconds and is distinguishable from an empty result.
- *What is the parent domain, and how are campaigns addressed?* `warpandweft.ink`, campaigns on paths rather than subdomains. Epic 13 S11 carries the assertion.
- *Do facts need a story time separate from the session date?* **Yes, and it is in RC 1a.** Two clocks on everything, per [[Information-Architecture]].

RC 1a is written and reconciled. It can be started once P2–P4 exist.
