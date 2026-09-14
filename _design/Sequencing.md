---
type: design
status: draft
visibility: gm
tags: [product, release, sequencing, backlog, epics]
---

# Sequencing

**Ordering rationale and the model invariants.** Epic allocation to release candidates lives in [[Roadmap]]; the release axis and its reasoning live in [[Release-Plan]]. This document explains *why* the order is what it is, and holds the invariants that cut across every epic.

~~The working plan for what gets built in what order. Supersedes the slice table in [[Release-Plan]], which was written before the strategic decisions in [[Knowledge-Assets]], [[Shared-Core]], [[Visibility-Model]], and [[Identity-and-Reconciliation]].~~

~~Releases are unchanged: **R1 is the GM interface, R2 is the player interface.**~~

**Both superseded.** The axis is now **between sessions versus at the table**, not GM versus player — [[Release-Plan]] records the three seams that gave the audience split away, and [[Roadmap]] carries the allocation that follows from it. The old reasoning was not wrong about ordering; it was wrong about what the two releases were dividing, and the allocation table below inherited that error twice over before it was caught.

---

## What changed

The strategic work did not add features. It added **invariants** — properties every epic must respect — and it sharpened why capture has to be right early.

Three consequences for sequencing:

1. A set of model invariants now cuts across the whole backlog. They are not an epic.
2. Reconciliation turned out to be needed in three separate places, so it becomes its own epic rather than three special cases.
3. Capture carries more structural weight than originally assessed, at the same time as it has the earliest deadline. That tension is the main thing this document has to resolve.

---

## Model invariants

Standing acceptance criteria. Every story inherits them whether or not they are restated, in the same way record integrity does under [[Shippable-Increment]].

| Invariant | Source |
|---|---|
| Identity is a stable identifier, never a name | [[Identity-and-Reconciliation]] |
| Identifiers are unique within a campaign, and non-sequential where player-facing | [[Strategy-Multi-Campaign-and-Convergence]], [[Visibility-Model]] |
| An entity carries many names; each is a fact with attribution, visibility, and truth status | [[Names-and-Aliases]] |
| Visibility is a property of facts and edges, not only of entities | [[Visibility-Model]] |
| Three gates: existence, name, everything else | [[Visibility-Model]] |
| Utterance, claim, and belief stay separate | [[Facts-and-Revelation]], [[Release-Plan]] |
| Provenance on every node and edge — who asserted it, from which side, when | [[Identity-and-Reconciliation]] |
| Reveal is recorded as an event | [[Release-Plan]] |
| Merges are non-destructive; edges re-point rather than break | [[Identity-and-Reconciliation]] |
| Planned and fact are distinct states | [[Off-Screen-Events]], [[Shared-Core]] |
| Sparse records are valid records | [[Session-Capture]], [[Shared-Core]] |
| Gaps carry an explicit human decision, never an inference | [[Shared-Core]] |
| A campaign container exists and carries configuration | [[Strategy-Multi-Campaign-and-Convergence]] |
| Content is portable — readable and exportable without the tool | [[Knowledge-Assets]] |
| The AI never generates manner, intent, or emotional state | [[Constraint-Manner-and-Intent]] |

**These are not a foundational epic.** Per [[Knowledge-Assets]], the store is built through the activity epics; what keeps it coherent is the model and the glossary, not a container work item.

---

## Prerequisites

Not features. Gates, because [[Shippable-Increment]] makes testable and demoable conditions of shipping and [[Epic-Writing-Standard]] makes the glossary a condition of writing.

| # | Item | Needed before |
|---|---|---|
| P1 | **Glossary** — written for a reader who knows nothing, marking which terms are system-specific | Writing any epic — **done** |
| P2 | **Test harness** — run any increment against a fixture, print output, *and render what it wrote as readable text* | The first increment |
| P3 | **Fixture corpus** — synthetic campaign, adversarial cases, legacy-shaped content, and entities across a range of investment degrees | The first increment that writes campaign data |
| P4 | **Challenger protocol** — the question set and the role separation rules | The first review |
| P5 | **Golden corpus** — judged output for judgment-bearing capabilities | RC 1c |

P2 through P4 are small and front-loaded. P5 arrives later, with RC 1c.

**P2 grew after this was written.** Once the store stopped being files, demo-by-reading-files went with it, so an inspection path became a harness deliverable rather than a property of the storage — see [[Store-and-Access]]. [[Test-Strategy]] specifies all four in full.

---

## Epics

**The allocation table that stood here is retired.** [[Roadmap]] owns epic allocation, and a second copy drifted from it in five places rather than one: Epic 13 moved to 1a by [[Migration]]; Epics 9, 10, 15 and 16 moved into R1 under the re-axis; Epic 2 split by tier rather than sitting whole in 1a; Epic 1 S11 moved to R2; and Epic 16 landed in 1c.

That is the case for not keeping two tables. It is also why the drift went unnoticed — both looked authoritative, and neither said which one to believe.

### Why the allocation is what it is

**Epic 17 is new.** [[Identity-and-Reconciliation]] found the same operation needed for arc merges, for repair after a bad batch, and for names. Building it three times separately is the expensive outcome, and burying it inside Epic 12 would hide it from the two epics that need it first.

**Epic 11 moves earlier, into 1b.** Under [[Visibility-Model]] this is no longer a thin flag — it is materialization, three gates, per-fact and per-edge visibility, and reveal-as-event. Epics 4 and 5 write content that must carry all of it, so it cannot trail them.

---

## The capture tension

Epic 1 has the earliest deadline and the heaviest structural requirements, and those pull against each other.

**The deadline.** [[Session-Capture]]: anything not recorded at the time is unrecoverable, and sessions are being played now.

**The structure.** Capture output must already separate utterance from claim, treat names as facts, carry provenance and visibility, and distinguish planned from fact. [[Release-Plan]] establishes that if R1 flattens any of this, R2 requires re-encoding every session record — and [[Shared-Core]] adds that consolidation would too.

### The resolution: fix the template now

The interim mechanism is templates plus repo plus AI, and it is already running. **The structural requirements can be applied to the template today, at effectively zero cost, before any code exists.**

That is the highest-value immediate action available:

- A name the party was given is recorded as something they were told, not as a name
- Facts carry who asserted them
- Visibility is marked per fact, not per file
- Existence, name, and other facts are distinguishable
- Blank fields stay valid

Sessions captured this way need no migration. Sessions captured flat do — and the deadline means there will be several of them before the tool exists.

---

## The sequence

```
P1 Glossary  →  P2 Harness  →  P3 Fixtures  →  P4 Challenger protocol
        ↓
  Template correction  (immediate, no code)
        ↓
  1a  Capture · Retrieval · Readiness · Conversion     ← first useful slice
        ↓
  1b  Authoring · Integration · Visibility · Reconciliation · The party's read
        ↓
  1c  Inference · Arcs · Off-screen and canon · Pacing · Attention   (+ P5)
        ↓
  1d  Correction and rollback
        ↓
  R2  At the table
```

**Before 1a**, three enabling items that are not epics: the deployed environments, P2, and P3. See [[Readiness-Checklist]].

Within each slice, increments ship individually per [[Shippable-Increment]] — functional, non-breaking, testable, demoable, and not necessarily useful.

---

## What is still blocked

| Blocked | Decision needed |
|---|---|
| ~~RC 1c entirely~~ | ~~Where is the line between surfacing and authoring?~~ **Answered: surfacing is authoring**, materialised through intake; generation is separately permitted forward-only |
| ~~Epics 4, 5, 7, 17 in detail~~ | ~~Is the graph model adopted?~~ **Answered: yes** — a graph domain model on a relational store, with a real database from RC 1a |
| ~~Epic 2 acceptance~~ | ~~Does retrieval work with no connectivity?~~ **Answered: no** — web-first from day one at a registered domain |
| Epic 14 | Does the campaign have a known length? |
| Epic 8 | How much canon must be recorded before Floor 6? |
| Epic 12 | Are tombstones preserved on deletion? — decide during 1b |
| Epics 3 and 6 | What is the attention budget, as a number? |
| RC 1b | Does anything reach players automatically? Now an R1 question, since players read the record in R1 |

RC 1a is written and reconciled. The three answered questions were the ones with the earliest need; what remains gates 1c and beyond. [[Roadmap]] §Open decisions is the live list.

---

## Next actions

1. ~~Correct the session template.~~ **Done** — the templates carry the model invariants, so sessions recorded before the tool exists need no re-encoding.
2. ~~Answer the connectivity question.~~ **Done** — no offline mode.
3. ~~Write the glossary from the terms Epics 1–3 actually use.~~ **Done** — [[Glossary]] is written and maintained.
4. ~~Write Epics 1–3 in full.~~ **Done**, and Epic 13 with them. RC 1a is written and reconciled to the model.
5. Write the remaining epics at epic level, with their blocking decisions as entry criteria for elaboration.
6. Clear [[Readiness-Checklist]] — the corpus corrections, the four open decisions, the hand conversion pass, and the infrastructure. Nothing in RC 1a starts before P2 and P3 exist.
