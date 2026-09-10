---
type: design
status: draft
visibility: gm
tags: [strategy, model, knowledge, product-definition]
---

# Knowledge Assets

The framing that makes the convergence in [[Shared-Core]] more than a schema coincidence.

---

## The statement

**The durable thing is the knowledge store — the people, places, events, and the relationships between them that the table has accumulated.**

The tools are activity layers on top of it. The GM's activities and the players' activities are different, but they are both *enabled by the same assets*, and neither owns them.

That reverses the usual reading. These are not two products that happen to share a schema. There is one knowledge store, and two sets of activities that read and write it.

---

## Chronicle is the visible slice of the same store

The clearest consequence.

| | What it holds |
|---|---|
| **The store** | Everything known about the world — people, places, events, relationships |
| **Table knowledge** | The portion the party has learned |
| **GM-only knowledge** | The rest — not yet revealed, or never to be |

Chronicle contains only table knowledge, by construction: it records what the party witnessed. It has no GM-only portion because no GM participates in it.

So convergence is not merging two stores. It is recognising **one store, of which Chronicle has only ever touched the visible part.** Visibility is the boundary between the two, and it is already the mechanism this design uses.

---

## What each side does with the same assets

| Activity | Who | What it is |
|---|---|---|
| Retrieval at the table | Both | A query |
| Recall of what was learned | Players | A query, filtered to table knowledge |
| Planning the next session | GM | A query, plus writing speculation |
| Noticing an emergent thread | GM | A query over accumulated relationships |
| Deciding what to reveal | GM | Moving something across the visibility boundary |
| Recording what happened | Either — GM, or a scribe | Writing facts |
| Contributing a note or theory | Players | Writing attributed content |

**Every one of these is an operation on the same assets.** The differences are which slice, which direction, and whether speculation is permitted — not different data.

---

## Consequences

### The store outlives the tools

If the assets are the durable value, they cannot be trapped inside any one interface. That answers a question left open in [[Open-Requirements]] §9: **content portability is required**, not optional. Export, backup, and readability without the tool are properties of the product, not conveniences.

The repo-as-database decision in [[Interface-User-Stories]] already delivers this almost for free, which is a point in its favour beyond the reasons originally given for it.

### Value accrues to the store before it accrues to features

An increment that adds to the store is worth something even when nothing yet reads it. That is exactly the position [[Shippable-Increment]] takes for unrelated reasons — a producer with no consumer is a legitimate release — and this framing is the product justification for it rather than merely a process allowance.

It also affects sequencing: capture and structure early, surfaces later. The store compounds; interfaces do not.

### The store is not an epic

A real trap. Under [[Epic-Writing-Standard]] an epic states value to a user, and *"build the knowledge store"* states none — nobody wants a store.

So the store gets built **through** the activity epics, each of which reads and writes it, rather than as a foundational epic of its own. What keeps it coherent across them is the model and the glossary, not a container epic.

### It sharpens what "core" means

[[Shared-Core]] says the shared core is entities, typed relationships, and events, as observed, with the boundary at the event. This framing says *why* that is the right line: those are the assets both sets of activities depend on. Anything only one side's activities need is not core, however tempting it is to put it there.

### Two knowledge domains, not two databases

[[Players-and-Characters]] settles that there are exactly two knowledge domains — GM and players — with no per-player knowledge. Read alongside this framing, that is a statement about **one store with a single boundary in it**, not about two separate collections that must be kept in step.

Worth being explicit, because "the player view" is easy to imagine as a second copy. It is a filter, and building it as anything else creates a synchronisation problem that does not otherwise exist.
