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

But text-primary is about **authority and default**, not about visualization being secondary in value.

---

## Visualization has three jobs

Only one of them is display.

### 1. Ingestion

A high-bandwidth route into the mental model. A large volume of data enters from a single image far faster than reading equivalent prose, then details within it are inspected and extracted as facts. For three-dimensional structures, different viewing angles carry different information — rotation adds data rather than repeating it.

### 2. Discovery

Structure that would take many sentences to state, and might never be noticed at all, arrives at once. This is where visualization earns the most: the answer to *"what's here that I haven't seen?"*

### 3. Validation

**Human memory is flawed, including good memory.** Detailed internal data drifts, and drift is invisible from the inside.

A rendered view is a fast comparison surface: bump the internal model against the external record, and mismatches surface immediately. That makes correction cheap and quick, instead of a wrong line of thinking running for weeks before something contradicts it.

This is the job with a hard requirement attached.

#### Validation requires faithful rendering

If a visualization is smoothed, idealized, or helpfully cleaned up, validation breaks — and breaks *silently*. Correct memory gets "corrected" against a prettified picture, which is worse than no check at all.

So rendered views must not editorialize:

- **No inferred or suggested edges drawn as established ones.** If the tool proposes a connection, it must be visually distinct from a recorded one — dashed, tinted, labeled. Never blended in.
- **No hiding weak, sparse, or awkward data.** An auto-layout that drops low-weight edges to reduce clutter is destroying exactly the signal being checked.
- **Missing data shown as missing.** A gap must look like a gap, not like a tidy diagram.
- **Uncertainty preserved.** `suspected` edges, `emerging` arcs, and `speculative` events must be visibly distinct from established ones — the same distinction the data model already makes.
- **Layout may change; content may not.** Rearranging for readability is fine. Omitting for readability is not.

#### A mismatch has two possible causes

When the picture and the memory disagree, the memory is not automatically the thing that's wrong. Either:

- **Memory drifted** — correct the memory.
- **The record is wrong or stale** — a session that never got written up, an integration that missed something, an edge that was never added.

Both are common and the second is easy to overlook. The tool should make acting on either equally easy: correcting the record from the view should be as fast as noticing the discrepancy. A validation surface that can only be read, not corrected, sends the GM off to find the file — and the correction doesn't happen.

### Two encodings, different profiles

| | Text | Visualization |
|---|---|---|
| Bandwidth | Sequential, precise | High-volume, parallel |
| Best for | Authoring, editing, exact attributes, addressability | Discovery, topology, clustering, gaps, validation |
| Role | Canonical record | Route in, source of fact, and error-detection surface |

Neither is a lossy version of the other. Same propositions, different encodings.

### What follows

- **Text is canonical for authoring and record.**
- **Visualization is a first-class epistemic tool** — how non-obvious structure gets found and how drift gets caught.
- **Multiple layouts of the same data are worth building.** Force-directed, hierarchical, timeline, and clustered views reveal different things — the 2D equivalent of rotating a 3D structure, not redundancy.
- **Rendered on request, at a chosen scope.**
- **Corrections can be made from the view**, not only from the file.
- **Never a required intermediary.** Nothing reachable *only* by clicking a node.

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
| Authoring and editing | Text, or inline from a view |
| Finding non-obvious structure | Visualization — this is where it earns the most |
| Checking the record against memory | Visualization, rendered faithfully |
| Graph topology, clusters, gaps | Rendered on request, scoped, multiple layouts |
| State machines and lifecycles | Rendered on request |
| Temporal diffs and trajectories | Rendered on request |
| Coverage and readiness | Text statement first; visual if scale makes it clearer |

The default *presentation* is text. But when the question is "what's here that I haven't noticed" or "does this match what I think is true," reach for a rendering — those are jobs reading does badly.
