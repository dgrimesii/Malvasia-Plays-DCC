---
type: design
status: draft
visibility: gm
tags: [interface, direction]
---

# Interface Direction

Settled direction for the GM-facing surface. Companion to [[GM-Considerations]] and [[Interface-User-Stories]].

---

## Text primary, visualization on demand

The GM interface is **text-first**. Visualizations are generated when asked for, not standing furniture.

This follows directly from how the GM works. The mental model is propositional — facts about objects and concepts, addressable directly, without a rendering step. A graph is itself propositional: node–edge–node is subject–predicate–object. `Warden serves Godpapa John` is a fact about an object, and it needs no picture to be held or reasoned about.

Which means the current storage format is close to isomorphic with the native representation already. An entity file plus structured facts about it *is* the model, not a serialization of it.

### What follows

- **Text is canonical.** The propositions are the truth; a diagram is a lossy projection of them — it flattens four dimensions to two and drops attributes.
- **Visualization serves inspection, not reasoning.** Its job is spotting a cluster, seeing topology at a glance, checking coverage — jobs where the eye beats reading. Reasoning happens over the facts.
- **Rendered on request, at a chosen scope.** "Show me the graph around this NPC." "Show me the forward cone from here." Not a permanent canvas.
- **Never a required intermediary.** Nothing should be reachable *only* by clicking a node in a diagram.

---

## Description is a first-class output

An earlier draft of [[GM-Considerations]] treated sensory description as translation work outside the GM's native mode. That was wrong.

This GM describes worlds in words natively — and describes them *precisely*: where things sit relative to one another, what colors and shapes are present, how a space is composed. Seeing an image yields a detailed set of data points about it. That is description, and it's a strong form of it: relational and concrete rather than impressionistic.

For a table, the relational mode is arguably the more useful one. Players assemble their own mental picture more reliably from spatial relationships and concrete attributes than from atmosphere.

So description belongs in the tool for the same reason everything else does: **latency, not difficulty.** Prepared descriptive text for locations, NPCs, and set pieces is retrieval-ready material — one less thing to compose mid-sentence while three people wait. The `READ ALOUD` convention already does this for dialogue; extending it to place and person is the same move.

---

## What this means in practice

| Surface | Form |
|---|---|
| Entity records | Structured text — facts, attributes, typed relationships |
| Prep view | Text: opening beats, live branches, likely NPCs, prepared description |
| At-the-table retrieval | Text, fast, searchable |
| Graph topology | Rendered on request, scoped |
| State machines and lifecycles | Rendered on request |
| Temporal diffs and trajectories | Rendered on request, or summarized as text |
| Coverage and readiness | Text statement first; visual only if it adds something |

The default answer to "how should this be presented" is text. Visualization is the exception, invoked deliberately, for the jobs where structure-at-a-glance genuinely beats reading.
