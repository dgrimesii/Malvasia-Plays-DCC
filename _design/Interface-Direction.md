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

This follows from how the GM works. The mental model is propositional — facts about objects and concepts, addressable directly, without a rendering step. A graph is itself propositional: node–edge–node is subject–predicate–object. `Warden serves Godpapa John` is a fact about an object, needing no picture to be held or reasoned about.

The current storage format is therefore close to isomorphic with the native representation already. An entity file plus structured facts about it *is* the model, not a serialization of it.

But text-primary is about **authority and default**, not about visualization being secondary in value. See below.

---

## Visualization is an input channel, not just an output

The important correction: images are not merely a way to display what's already known. They are a **high-bandwidth route into the mental model**.

The process:

1. **Ingest** — a large volume of data enters the model quickly from a single image, far faster than reading equivalent prose.
2. **Inspect** — details within that image are then examined and extracted as facts.
3. **Rotate** — for three-dimensional structures, viewing from different angles validates existing data and adds new data. Different angles are not redundant views; they carry different information.

So a visualization is a **discovery shortcut**: structure that would take many sentences to state, and might never be noticed at all, arrives at once and becomes propositional facts.

### Two encodings, different profiles

| | Text | Visualization |
|---|---|---|
| Bandwidth | Sequential, precise | High-volume, parallel |
| Best for | Authoring, editing, exact attributes, addressability | Discovery, topology, clustering, gaps, scale |
| Role | Canonical record | Fast route in, and a source of fact in its own right |

Neither is a lossy version of the other. They're the same propositions encoded differently, and the model is enriched by both.

### What follows

- **Text is canonical for authoring and record.** Facts get written, edited, and cited as text.
- **Visualization is a first-class epistemic tool**, not decoration and not merely a display of known things. It's how non-obvious structure gets found.
- **Multiple layouts of the same data are worth building.** Force-directed, hierarchical, timeline, and clustered views of one graph reveal different things. This is the 2D equivalent of rotating a 3D structure — not redundancy.
- **Where a structure is genuinely three-dimensional or has three meaningful axes** (entity × time × arc, say), rotatable or multi-projection views earn their cost.
- **Rendered on request, at a chosen scope.** "Show me the graph around this NPC." "Show me the forward cone from here."
- **Never a required intermediary.** Nothing should be reachable *only* by clicking a node in a diagram. Visualization is a powerful route in, not the only door.

---

## Description is a first-class output

An earlier draft of [[GM-Considerations]] treated sensory description as translation work outside the GM's native mode. That was wrong.

This GM describes worlds in words natively — and describes them *precisely*: where things sit relative to one another, what colors and shapes are present, how a space is composed. Seeing an image yields a detailed set of data points about it. That is description, and a strong form of it: relational and concrete rather than impressionistic.

For a table, the relational mode is arguably the more useful one. Players assemble their own mental picture more reliably from spatial relationships and concrete attributes than from atmosphere.

So description belongs in the tool for the same reason everything else does: **latency, not difficulty.** Prepared descriptive text for locations, NPCs, and set pieces is retrieval-ready material — one less thing to compose mid-sentence while three people wait. The `READ ALOUD` convention already does this for dialogue; extending it to place and person is the same move.

---

## What this means in practice

| Surface | Form |
|---|---|
| Entity records | Structured text — facts, attributes, typed relationships |
| Prep view | Text: opening beats, live branches, likely NPCs, prepared description |
| At-the-table retrieval | Text, fast, searchable |
| Authoring and editing | Text |
| Finding non-obvious structure | Visualization — this is where it earns the most |
| Graph topology, clusters, gaps | Rendered on request, scoped, multiple layouts available |
| State machines and lifecycles | Rendered on request |
| Temporal diffs and trajectories | Rendered on request |
| Coverage and readiness | Text statement first; visual if scale makes it clearer |

The default *presentation* is text. But when the question is "what's here that I haven't noticed," reach for a rendering first — that's the job it does better than reading ever will.
