---
type: design
status: draft
visibility: gm
tags: [model, visibility, revelation, naming, information-architecture]
---

# Visibility Model

What is secret, at what granularity, and what leaks if it is done at the wrong level. Refines [[Identity-and-Reconciliation]] and extends [[Facts-and-Revelation]].

---

## The core asset

A thing in the world — a person, a place, an object, a group — is **one asset with a stable identity**. Names attach to it. Facts attach to it. Relationships attach to it.

**The invariant: the link between two names or two entries and the single real thing must never be lost.** Everything else about visibility can be adjusted later; a broken identity link cannot be reconstructed, because the knowledge that they were the same thing lived only in whoever noticed.

---

## Three things are visible independently

| | Question it answers | Example |
|---|---|---|
| **Existence** | Is this known to be a thing at all? | The party knows there is a toll collector |
| **Facts** | What is known about it? | They know he collects a toll; they do not know he is being blackmailed |
| **Relationships** | What is it known to be connected to? | They do not know he answers to anyone |

The file-level `visibility` flag in the current repo can only express the first. [[Information-Architecture]] already made this argument for edges — *"players may know two things exist without knowing they're connected"* — and it applies equally to facts.

---

## Materialization

An entity **materializes** when it appears at the table.

Before: its existence is itself the secret.
After: its existence is permanently public. Facts and relationships remain individually gated.

Two properties worth stating:

- **One-way.** Nothing un-materializes. A thing the party has met cannot become unknown to them again.
- **One-time and binary.** Unlike facts, existence has no partial state. This makes existence-visibility much simpler than fact-visibility, and it is worth keeping them as different mechanisms rather than one general system.

### The name is not part of materialization

A correction worth making precisely: **an entity can materialize without its name being known.**

The party meets a toll collector who does not introduce himself. He exists — permanently, publicly. His name is a *fact about him*, gated like any other, and may stay gated for good reasons.

So there are three gates, not two: **existence, name, and everything else.** Name behaves like a fact rather than like existence, and collapsing it into materialization would force the GM to reveal names at the moment of first contact, which is often wrong.

---

## Naming is mostly a sequencing problem

The party will call things whatever they called them at the table. If the official name reaches them promptly after the session, they adopt it and no divergence takes hold. **Prompt revelation is the fix, and a workflow fix is better than a data fix.**

The mechanism has a useful property: the revealed location arrives *attached to the session it appeared in*, so the party gets the association without anyone explaining it. Reveal recorded as an event — already an R1 obligation in [[Release-Plan]] — is what makes that possible.

Three limits, none fatal.

**It depends on a habit that is known to slip.** [[Open-Requirements]] §8 asks whether anything reaches players automatically, and notes that manual publishing each week is exactly the step that gets skipped. This raises the value of that answer: if reveal is prompt, naming converges on its own; if it is manual and slips, divergence accumulates. **Automatic or prompted reveal is worth more than it appeared to be.**

**There is a window at the table.** Per [[Device-Context]], players may have tablets in play. Anything written between materialization and reveal is written under the party's own name.

**Convergence is not always the goal.** [[North-Star]] wants a name a player coins absorbed as a world fact. Sometimes the party's name is better, stickier, or simply theirs, and the official one should yield.

So aliases are still wanted — but for a different reason than conflict resolution. **They are the authorship mechanism, not the repair mechanism**, and a name the party invented surviving in the record is the feature working, not a problem being tolerated.

---

## Correction: the duplicate risk is smaller than described

[[Identity-and-Reconciliation]] treats duplicate referents as the central hazard. That overstated it.

**Players only write about things that have materialized.** They cannot add facts to an object they do not know exists. So the case of a player creating a record that collides with a hidden GM entity essentially does not occur.

What remains is the naming case above — tractable, carrying no spoiler constraint, and largely solved by sequencing.

The reconciliation machinery is still worth having, for arc merges and for repair. It is simply not primarily needed for this.

---

## The real risk: hidden relationships from visible entities

The party has met an NPC. That NPC is connected, in the GM's plan, to an object that has not appeared. **Both the relationship and the far object must stay hidden until it comes up at the table.**

So a visible entity's page cannot be rendered by filtering nodes alone. Every edge is evaluated independently, and an edge to an unmaterialized entity is doubly hidden — the connection *and* its endpoint.

This is the concrete form of the requirement in [[Interface-Direction]] that the player surface is a filter over one store. The filter operates at three levels, not one.

---

## Leakage: absence has a shape

The failure mode is not showing a secret. It is showing the **outline** of one, from which the secret is inferable. Five specific ways this happens:

**Counts.** *"3 connections"* on an entity showing two is a statement that something is hidden. Any degree, total, or summary computed over unfiltered data leaks.

**Sequential identifiers.** If identifiers are ordered and exposed, a visible `npc_007` and `npc_009` proves `npc_008` exists. Chronicle's ID registry, with its voided gaps, is a live illustration of how readable this is. **Identifiers exposed to the player surface must not be sequential**, or must not be exposed at all.

**Layout.** A graph view that reserves space for hidden nodes, or that positions visible nodes as though arranged around an absent centre, draws the secret without naming it.

**Empty results that look wrong.** [[Interface-User-Stories]] already asks for this: it must be clear when something is *simply not known yet*, rather than returning a blank that reads as an error. The inverse also holds — a "no results" that differs in shape from a genuine absence is a signal.

**Reconciliation responses.** Covered in [[Identity-and-Reconciliation]], and the same class of problem: *"this already exists"* confirms existence.

**The general rule: every player-facing computation runs over the filtered store, never over the full store with a filter applied to the output.** Filtering the presentation of an unfiltered calculation is how all five of these happen.

---

## Revelation operates on facts and edges, not on entities

Because visibility is per-fact and per-edge, *"reveal the toll collector"* is not a single action. Revealing an entity is the composition of several: making its existence known, plus its name if that is being given, plus some subset of its facts and relationships.

This answers part of [[Interface-User-Stories]] open question 6 about bulk reveal. After a session, several things become known at once — and they are **heterogeneous**: some existences, some names, some facts, some edges. A bulk reveal is a set of individually-chosen items, not one switch on an object.

It also fits [[Facts-and-Revelation]] cleanly. An utterance is a fact with its own visibility. A claim's truth status is a separate fact, usually GM-only, and is exactly what the player surface must never render as a world fact.

---

## Consequences

- **Visibility is an attribute of facts and edges, not only of entities.** The file-level flag in `README.md` is insufficient and should not be built on.
- **Three gates: existence, name, everything else.** Name is a fact, not part of materialization.
- **Existence visibility is separate and simpler** — one-way, binary, set by materialization.
- **Prompt reveal is the primary naming mechanism.** This makes the automatic-reveal question in [[Open-Requirements]] §8 more valuable than previously assessed.
- **Aliases are an authorship feature**, not a conflict-resolution mechanism. A party-coined name surviving in the record is the intended outcome.
- **The identity link between names and the real thing is the one irrecoverable asset.** It survives merges, renames, and reconciliation, or the record is permanently degraded.
- **Player-facing identifiers are non-sequential, or not exposed.** Cheap now; a migration once anything references them.
- **Every player-facing computation runs over the filtered store**, including counts, summaries, graph layout, and search.
- **Reveal is an action on facts and edges.** Any interface treating it as a per-entity toggle will either over-reveal or become unusable.
