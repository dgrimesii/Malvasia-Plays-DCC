---
type: design
status: open
visibility: gm
tags: [requirements, rollback]
---

# Rollback and Repair

**Status: open. Nothing here is decided.** The repair model described below may well be overkill for a single-GM campaign — it's recorded so the reasoning isn't lost if the simpler options turn out to be insufficient.

Referenced from [[Open-Requirements]] §6.

---

## The problem

Errors are discovered late. By then the bad batch has propagated: later work references its entities, cites it as evidence, rests on it as premise. Rolling it back naively either destroys good work or leaves silent wreckage.

---

## Four candidate behaviors

| Option | Behavior | Cost | Failure mode |
|---|---|---|---|
| **Block** | Refuse rollback until dependents are handled | Cheap | Often unusable — dependents may be extensive |
| **Cascade** | Remove dependents too | Cheap | Destroys good work |
| **Flag** | Roll back, mark dependents suspect, GM repairs by hand | Moderate | Graph stays degraded indefinitely |
| **Repair** | Roll back, keep dependents, redo correctly, re-attach, resolve the rest | High | Significant machinery for a rare event |

**Start with the cheapest option that survives contact with a real error.** The frequency and size of actual mistakes is unknown; building repair before knowing whether flag would have sufficed is speculative. If manual repair proves painful in practice, the case for building more is then evidence-based.

---

## The repair model, if it proves necessary

Described as a sequence:

1. **Undo the bad batch.** Its entities and edges are removed from the active graph.
2. **Keep the good work.** Later batches survive, including anything that referenced the removed material. They are now knowingly inconsistent.
3. **Redo the bad work correctly.** Re-integrate from a corrected source, or author directly.
4. **Re-establish integrity automatically wherever possible.** References that can be matched to the corrected entities are reattached without asking.
5. **Resolve the remainder manually.** What couldn't be matched is presented as a bounded worklist.

The aim is not perfect automatic recovery. It's **maximum automatic recovery with an explicit, finite pile of what's left.**

---

## What repair requires that the simpler options don't

### Dangling references must survive

Normally, deleting a target either cascades to its references or nulls them. Neither works for repair. A reference to a removed entity would need to persist as a **tombstone** — retaining what it pointed at — so step 4 has something to match against.

**This one has a decision deadline earlier than the rest.** If deletion is built to clean up references, the information repair needs is destroyed at the moment of deletion, and repair becomes impossible to add later without a migration. Even if repair is never built, preserving tombstones is a cheap hedge worth considering.

### A knowingly-inconsistent state

Between step 1 and step 5 the record is broken and everyone knows it — a legitimate working state, not a transaction to complete or abort. That implies: inconsistency visible rather than silent, work usable while degraded, inference suppressed in affected regions, and a way to exit the state so repair doesn't become permanent debt.

### An identity mapping step

Step 4 only works if corrected entities can be matched to what the tombstones point at. Some matches are obvious; others aren't — the hallucinated `Marco` is really `Marcus`, or one wrong NPC was really two. The GM confirms correspondences, and everything downstream of a confirmed mapping reattaches at once.

One correspondence can repair dozens of references, which is what makes the model worth its cost if it's ever needed.

---

## Open questions

**Which behavior is actually needed?** Unknown until real errors have been experienced. This is the top-level open question; everything below is conditional on repair being chosen.

**Should tombstones be preserved regardless?** A cheap hedge that keeps the repair option open, even if flag or cascade is chosen for now.

**How is a manual worklist scoped and presented?** Finite, ordered, dismissible — a queue, not a diffuse warning state.

**Can repair be abandoned partway?** Possibly fine if unresolved tombstones persist as visible gaps.

**Does redoing produce a new batch or replace the old?** Keeping the failed batch has debrief value — "here's what the tool got wrong" — at a storage and complexity cost.

**What if corrected work legitimately contradicts later good work?** Tuesday's session recorded the party meeting an NPC who, corrected, was never there. A narrative problem wearing a data problem's clothes — surfaceable, never automatically resolvable.

---

## Why any of this matters

Every other correctness feature assumes the record is trustworthy. Premise decay, coverage checks, investment inference, arc discovery — all of it reasons over the graph and produces confident output.

A graph quietly containing hallucinated facts produces confident wrong output, with no way to tell the difference from the inside. Whatever behavior is chosen, the requirement it serves is that the record stays recoverable rather than gradually poisoned.

That requirement can be met cheaply or expensively. It can't be skipped.
