---
type: design
status: draft
visibility: gm
tags: [model, visibility, revelation, information-architecture]
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
| **Existence** | Is this known to be a thing at all? | The party knows there is a Warden |
| **Facts** | What is known about it? | They know he collects a toll; they do not know he is being blackmailed |
| **Relationships** | What is it known to be connected to? | They do not know he answers to anyone |

The file-level `visibility` flag in the current repo can only express the first. [[Information-Architecture]] already made this argument for edges — *"players may know two things exist without knowing they're connected"* — and it applies equally to facts.

---

## Materialization

An entity **materializes** when it appears at the table.

Before: its existence is itself the secret.
After: **its existence and its name are permanently public.** Facts and relationships remain individually gated.

Two properties worth stating:

- **One-way.** Nothing un-materializes. A thing the party has met cannot become unknown to them again.
- **One-time and binary.** Unlike facts, existence has no partial state. This makes existence-visibility much simpler than fact-visibility, and it is worth keeping them as different mechanisms rather than one general system.

---

## Correction: the duplicate risk is smaller than described

[[Identity-and-Reconciliation]] treats duplicate referents as the central hazard. That overstated it.

**Players only write about things that have materialized.** They cannot add facts to an object they do not know exists. So the case of a player creating a record that collides with a hidden GM entity essentially does not occur.

What remains is real but far more tractable: **the party and the GM using different names for the same materialized thing.** The party calls it *the big kitchen place*; the GM's record says *the Serving Warrens*.

That is a naming and aliasing problem on a mutually visible entity. It carries **no spoiler constraint at all**, because both sides already know the thing exists. It is resolved by the alias mechanism in [[Identity-and-Reconciliation]] — the party's name survives as an alias, which is the [[North-Star]] authorship goal working as intended.

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

Because visibility is per-fact and per-edge, *"reveal the Warden"* is not a single action. Revealing an entity is the composition of several: making its existence known, plus some subset of its facts, plus some subset of its relationships.

This answers part of [[Interface-User-Stories]] open question 6 about bulk reveal. After a session, several things become known at once — and they are **heterogeneous**: some existences, some facts, some edges. A bulk reveal is a set of individually-chosen items, not one switch on an object.

It also fits [[Facts-and-Revelation]] cleanly. An utterance is a fact with its own visibility. A claim's truth status is a separate fact, usually GM-only, and is exactly what the player surface must never render as a world fact.

---

## Consequences

- **Visibility is an attribute of facts and edges, not only of entities.** The file-level flag in `README.md` is insufficient and should not be built on.
- **Existence visibility is separate and simpler** — one-way, binary, set by materialization.
- **The identity link between names and the real thing is the one irrecoverable asset.** It survives merges, renames, and reconciliation, or the record is permanently degraded.
- **Player-facing identifiers are non-sequential, or not exposed.** Cheap now; a migration once anything references them.
- **Every player-facing computation runs over the filtered store**, including counts, summaries, graph layout, and search.
- **Reveal is an action on facts and edges.** Any interface treating it as a per-entity toggle will either over-reveal or become unusable.
