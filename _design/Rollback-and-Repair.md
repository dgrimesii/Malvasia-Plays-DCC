---
type: design
status: open
visibility: gm
tags: [requirements, rollback]
---

# Rollback and Repair

Detail on the hardest correctness requirement. Referenced from [[Open-Requirements]] §6.

---

## The problem

Errors are discovered late. By then the bad batch has propagated: later work references its entities, cites it as evidence, rests on it as premise. Rolling it back naively either destroys good work or leaves silent wreckage.

Four possible behaviors were considered:

| Option | Behavior | Cost |
|---|---|---|
| Block | Refuse rollback until dependents are handled | Cheap, often unusable — dependents may be extensive |
| Cascade | Remove dependents too | Cheap, destroys good work |
| Flag | Roll back, mark dependents suspect, GM repairs | Moderate, leaves the graph degraded indefinitely |
| **Repair** | Roll back, keep dependents, redo correctly, re-attach, resolve the rest | **Expensive, and the right one** |

---

## The repair model

The chosen behavior, described as a sequence:

1. **Undo the bad batch.** Its entities and edges are removed from the active graph.
2. **Keep the good work.** Later batches survive, including anything that referenced the removed material. They are now knowingly inconsistent.
3. **Redo the bad work correctly.** Re-integrate from a corrected source, or author directly.
4. **Re-establish integrity automatically wherever possible.** References that can be matched to the corrected entities are reattached without asking.
5. **Resolve the remainder manually.** What couldn't be matched is presented as a bounded worklist.

The aim is not perfect automatic recovery. It's **maximum automatic recovery with an explicit, finite pile of what's left.**

---

## What this requires that simpler options don't

### Dangling references must survive

Normally, deleting a target either cascades to its references or nulls them. Neither works here. A reference to a removed entity must persist as a **tombstone** — retaining what it pointed at, by name and by whatever identity it had — so that step 4 has something to match against.

If references are cleaned up on delete, the information needed to repair them is gone, and step 4 is impossible. This is the single most consequential implication in this document.

### The graph must support a knowingly-inconsistent state

Between step 1 and step 5, the record is broken and everyone knows it. That is a legitimate working state, not a transaction to be rolled forward or aborted.

Consequences:

- **Inconsistency must be visible, not silent.** Affected entities are marked; nothing looks fine when it isn't.
- **Work must remain usable while degraded.** The GM may need to run a session mid-repair. Broken references degrade what's shown; they don't block access.
- **Inference must be conservative during repair.** Suggestions and tickets drawn from an inconsistent region are unreliable and should be suppressed or clearly caveated.
- **The state must be exitable.** A repair that can be started and never finished becomes permanent debt.

### Reconciliation needs an identity mapping step

Step 4 only works if corrected entities can be matched to what the tombstones point at. Some matches are obvious — same name, same type. Others aren't: the hallucinated `Marco` is really `Marcus`, or one wrong NPC turns out to have been two real ones.

So repair needs a **mapping step**: the GM confirms or supplies correspondences between removed and corrected entities, and everything downstream of a confirmed mapping reattaches at once.

That mapping is the highest-leverage moment in the whole process. One correspondence can repair dozens of references.

---

## Open questions

**How is the manual worklist scoped and presented?**
It should be finite, ordered, and dismissible — a queue, not a diffuse warning state. "Seventeen references need attention" is workable; "the graph may be inconsistent" is not.

**Can repair be abandoned partway?**
If a repair is started and the GM walks away, what state is the record in? Possibly: unresolved tombstones simply persist as visible gaps, indefinitely. That's tolerable if they stay visible.

**Does redoing the work produce a new batch, or replace the old one?**
Affects rollback depth and whether the original error remains inspectable afterward. Keeping the failed batch as history has debrief value — "here's what the tool got wrong" — but costs storage and complexity.

**What if the corrected work legitimately contradicts the later good work?**
Not a matching failure but a genuine conflict: Tuesday's session recorded the party meeting an NPC who, corrected, was never there. This is a narrative problem, not a data problem, and probably can only be surfaced — never resolved automatically.

**Is a partial repair worth it?**
Re-attaching 80% and leaving 20% may be more useful than an all-or-nothing guarantee. Likely yes, given the alternative is manual reconstruction of everything.

---

## Why this is worth the cost

Every other correctness feature assumes the record is trustworthy. Premise decay, coverage checks, investment inference, arc discovery — all of it reasons over the graph and produces confident output.

A graph that quietly contains hallucinated facts produces confident wrong output, and the GM has no way to tell the difference. Repair is what makes the record recoverable rather than gradually poisoned, and it's the difference between a tool that stays trustworthy over years and one that has to be abandoned and rebuilt.
