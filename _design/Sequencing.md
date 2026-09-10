---
type: design
status: draft
visibility: gm
tags: [product, release, sequencing, backlog, epics]
---

# Sequencing

The working plan for what gets built in what order. Supersedes the slice table in [[Release-Plan]], which was written before the strategic decisions in [[Knowledge-Assets]], [[Shared-Core]], [[Visibility-Model]], and [[Identity-and-Reconciliation]].

Releases are unchanged: **R1 is the GM interface, R2 is the player interface.**

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
| P1 | **Glossary** — written for a reader who knows nothing, marking which terms are system-specific | Writing any epic |
| P2 | **Test harness** — run any increment against a fixture, print output | The first increment |
| P3 | **Fixture corpus** — synthetic campaign, plus adversarial cases | The first increment that writes campaign data |
| P4 | **Challenger protocol** — the question set and the role separation rules | The first review |
| P5 | **Golden corpus** — judged output for judgment-bearing capabilities | The first inference increment |

P1 through P4 are small and front-loaded. P5 arrives later, with slice 1c.

---

## Epics

| # | Epic | Release | Slice |
|---|---|---|---|
| 1 | Capture what happened in a session | R1 | 1a |
| 2 | Find anything, fast, at the table | R1 | 1a |
| 3 | Know the next session is covered | R1 | 1a |
| 4 | Author and connect campaign material | R1 | 1b |
| 5 | Bring in outside material and integrate it | R1 | 1b |
| 13 | Get started — import and first run | R1 | 1b |
| 11 | Control what the party knows | R1 | 1b |
| 17 | **Recognise that two records are the same thing** | R1 | 1b |
| 6 | Surface what could not have been noticed | R1 | 1c |
| 7 | Run a thread across a campaign | R1 | 1c |
| 8 | Feel the world moving without you | R1 | 1c |
| 14 | Pace the campaign | R1 | 1c |
| 12 | Keep the record trustworthy | R1 | 1d |
| 9 | Players consult the record of their own adventure | R2 | — |
| 10 | Players contribute to the record | R2 | — |
| 15 | See what the party knows | R2 | — |
| 16 | Player attention as a prep signal | R2 | — |

### Changes from the earlier map

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
  1a  Capture · Retrieval · Readiness        ← first useful slice
        ↓
  1b  Authoring · Integration · Visibility · Reconciliation · Import
        ↓
  1c  Inference · Arcs · Off-screen and canon · Pacing      (+ P5)
        ↓
  1d  Correction and rollback
        ↓
  R2  Player surface
```

Within each slice, increments ship individually per [[Shippable-Increment]] — functional, non-breaking, testable, demoable, and not necessarily useful.

---

## What is still blocked

| Blocked | Decision needed |
|---|---|
| Slice 1c entirely | Where is the line between surfacing and authoring? *(§G3)* |
| Epics 4, 5, 7, 17 in detail | Is the graph model adopted? *(§G2)* — [[Shared-Core]] is new evidence in favour |
| Epic 14 | Does the campaign have a known length? |
| Epic 8 | How much canon must be recorded before Floor 6? |
| Epic 12 | Are tombstones preserved on deletion? |
| Epic 2 acceptance | Does retrieval work with no connectivity? |

Slices 1a and 1b can be written and started without any of these, except that Epic 2's acceptance criteria need the connectivity answer — the smallest question on the list with the earliest need.

---

## Next actions

1. Correct the session template. No dependencies, immediate value, closing deadline.
2. Answer the connectivity question. One line, unblocks Epic 2's criteria.
3. Write the glossary from the terms Epics 1–3 actually use.
4. Write Epics 1–3 in full, with stories and acceptance criteria.
5. Write the remaining epics at epic level, with their blocking decisions as entry criteria for elaboration.
