---
type: design
status: draft
visibility: gm
tags: [model, identity, reconciliation, convergence, information-architecture]
---

# Identity and Reconciliation

The duplicate-entity risk created by a shared store with a hidden portion, and the information-architecture choices it makes load-bearing now.

Follows from [[Knowledge-Assets]]. Near-term posture: the two tools stay separate. This document exists so near-term choices do not foreclose consolidation.

---

## It is not a merge conflict

Worth separating precisely, because the two have different solutions.

| | What it is | Solution space |
|---|---|---|
| **Merge conflict** | Two edits to the same record | Locking, ordering, conflict resolution |
| **Duplicate referent** | Two records for the same thing | Identity reconciliation |

[[Update-Cadence]] already removed the first: writes are batched, once per session, with nobody editing simultaneously. The risk here is the second.

### It is caused by concealment, not concurrency

A player writes about a place the GM already holds privately. Two records now exist for one referent — **precisely because the GM's version was invisible.**

That is a structural consequence of the visibility model, not a race condition. It cannot be prevented by coordination, because the whole point is that one party cannot see what the other has. It can only be reconciled afterward, and only by the GM, who is the only person able to see both.

### Reconciliation must never leak

The hard constraint. If a player's entry silently merges into a hidden one, or the system responds *"this already exists"*, that confirms the thing exists — a spoiler delivered by the plumbing.

This is the same rule already flagged in [[Interface-User-Stories]] open question 2: a player note may reference something true that they should not know, and the system must neither confirm nor deny. Reconciliation is invisible to the player, always.

---

## Attribution already avoids most of it

[[Players-and-Characters]] establishes that a note is **attributed content attached to an entity**, not a world fact and not an entity itself. If players contribute notes rather than create entities, the duplicate problem mostly does not arise — you cannot duplicate a place you cannot create.

[[Interface-User-Stories]] already says this: a player note attaches to the session, NPC, zone, monster, or faction it is about.

**The residual case is the real one:** a player wants to note something about a thing that has no visible entry — either because the GM's version is hidden, or because it genuinely does not exist yet. They still need something to attach to.

Two shapes, both viable, and the choice is a design-phase decision:

- **Anchor to the session instead.** Simple, loses the entity association.
- **Let the player name an unresolved referent** — a lightweight, explicitly player-named thing the GM can later reconcile. Preserves the association and produces exactly the reconciliation queue described below.

The second is more interesting because it turns the risk into a signal: an unresolved referent the party keeps writing about is a strong statement about what they are paying attention to.

---

## The same machinery is needed three times

This is the finding that makes it worth treating as first-class rather than as a special case.

| Where | What happens |
|---|---|
| **Player and GM records for one thing** | Two nodes turn out to be one |
| **Arc merging** — [[Arcs]] | Two threads turn out to be one |
| **Repair after a bad batch** — [[Rollback-and-Repair]] | A hallucinated `Marco` turns out to be `Marcus` |

All three are: *these two identities are the same identity; combine them without losing what either contributed.* And in all three the requirements are identical — **the GM decides, both names survive, evidence is unioned with its original attribution, and references re-point rather than break.**

[[Arcs]] already specifies exactly this for arc merges. Generalising it costs little; discovering later that three near-identical mechanisms were built separately costs a lot.

Consolidating with Chronicle eventually is the same operation again, at scale — reconciling two identifier namespaces built independently.

---

## What this makes load-bearing now

Six choices. All cheap to adopt, all migrations if adopted later.

### 1. Identity is an identifier, not a name

If a node's identity is its name, every rename and every merge breaks references. Chronicle's `npc_001` convention is the right instinct and worth copying.

### 2. An entity has many names, and names carry attribution

The canonical name, plus what people actually call it. [[Arcs]] already requires this for arc handles and aliases; the same applies to everything else.

It also serves [[North-Star]] directly: *"a name a player coins... once it's in the record with the same weight as anything else, the world has absorbed their contribution."* A player's name for a place surviving reconciliation as an alias is that goal, literally implemented.

### 3. Provenance on nodes and edges

Who asserted this, from which side, when. Reconciliation without provenance loses the record of who contributed what, which is the thing attribution exists to protect.

### 4. Merge is non-destructive

Both names kept, evidence unioned with attribution intact, and enough retained to inspect or undo the merge. This connects to the tombstone question in [[Rollback-and-Repair]], which already has an early decision deadline — the same information supports both.

### 5. Edges re-point on merge

[[Information-Architecture]] open question 9 asks what happens to an edge when a node is merged. This is the answer: edges follow the surviving identity rather than breaking. Worth deciding rather than leaving open, since it is cheap now.

### 6. Reconciliation is a GM action with a queue

Not automatic. The system may propose that two records are the same — that is a good proposal, and the same shape as arc-merge proposals — but combining identities is interpretive judgment.

Proposals accumulate as a bounded, dismissible queue, consistent with the treatment of gaps and tickets elsewhere.

---

## Near-term posture

- **The tools stay separate.** Chronicle changes nothing; this tool does not integrate with it.
- **These six choices are adopted anyway**, because each is independently justified by this campaign alone — arc merges, repair, and player notes all need them regardless of whether consolidation ever happens.
- **The compatibility note** in [[Strategy-Multi-Campaign-and-Convergence]] should record identifier conventions specifically, since namespace reconciliation is what a future consolidation actually involves.

**The test for any near-term IA decision:** would this choice make two independently-built stores impossible to reconcile later? If yes, it is worth avoiding now even when the immediate cost of avoiding it is real.
