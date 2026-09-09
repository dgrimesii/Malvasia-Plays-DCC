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

The GM interface is **text-first** for authoring and record. Visualizations are generated when asked for, not standing furniture — with one exception, the table view, described below.

This follows from how the GM works. The mental model is propositional — facts about objects and concepts, addressable directly, without a rendering step. A graph is itself propositional: node–edge–node is subject–predicate–object.

The current storage format is therefore close to isomorphic with the native representation. An entity file plus structured facts about it *is* the model, not a serialization of it.

Text-primary is about **authority and default**, not about visualization being secondary in value.

---

## Visualization has four jobs

Only one of them is display.

### 1. Ingestion

A high-bandwidth route into the mental model. A large volume of data enters from a single image far faster than reading equivalent prose, then details within it are inspected and extracted as facts. For three-dimensional structures, different viewing angles carry different information — rotation adds data rather than repeating it.

### 2. Discovery

Structure that would take many sentences to state, and might never be noticed at all, arrives at once. The answer to *"what's here that I haven't seen?"*

### 3. Validation

**Human memory is flawed, including good memory.** Detailed internal data drifts, and drift is invisible from the inside. A rendered view is a fast comparison surface: bump the internal model against the external record, and mismatches surface immediately.

### 4. Access key

An **imperfect but essentially accurate** visualization works as an index into memory. It doesn't need to contain the information — it needs to reliably *point* at it. Seeing the local structure locates the memory address; relationships are then traversed internally at speed.

This is the job that matters most at the table.

---

## One view, two controls

An earlier draft framed audit and reference as separate modes. They aren't — they're positions on two orthogonal controls over a single view.

### Zoom — how much detail per node

| Zoomed out | Zoomed in |
|---|---|
| Entity names only | Full attributes, states, edge types |
| Bigger ideas | Specifics |
| Scannable at a glance | Readable deliberately |

### Scope — how many hops from center

1 hop for immediate context. 2 hops for the useful neighborhood. Beyond that is noise under time pressure and a different question away from the table.

### The invariant: zoom reduces detail, never topology

**Relationships are preserved at every zoom level.** Zooming out drops annotations, attributes, and labels — it never drops edges. A view that hides weak or awkward connections to reduce clutter has destroyed exactly the signal that validation depends on, and would silently mislead.

With that invariant held, the audit-versus-reference tension mostly disappears. Every view is faithful within its scope; zoom only changes how much is said about each thing.

### Honest cropping versus heuristic omission

Scope does omit — a 2-hop view excludes the rest of the graph. That's fine, because the rule is known and stated: *this is everything within two hops.* The GM knows exactly what was excluded and why.

What's not acceptable is a layout algorithm deciding an edge is unimportant. Bounded, legible cropping is honest. Heuristic hiding is not, because there's no way to know what's missing.

### Uncertainty renders at every zoom

`suspected` edges, `emerging` arcs, and `speculative` events stay visibly distinct from established ones at all zoom levels, and inferred connections never render as recorded ones. Zooming out may drop an edge's *label*; it must not drop the fact that the edge is uncertain.

---

## The table view

The one visualization that stands open rather than being requested. It's simply this view at a specific setting: **zoomed out, scoped to 1–2 hops, centered on what's in play.**

- **Hooks are the most visible thing on it** — unused threads, live arcs, player investments, unrevealed information. They're the reason it exists.
- **Re-centers fast** as the scene moves. Ten seconds to update makes it unusable mid-session.
- **Useful without interaction.** A glance should pay off.
- **Zoom in for detail**, without changing what's connected to what.
- **Text detail one step away** — the map locates, the record supplies specifics.

**This is the one place a visualization may be primary rather than on-demand**, because its job is to be glanced at repeatedly during a session where reading isn't possible.

---

### A mismatch has two possible causes

When a view and memory disagree, the memory is not automatically wrong. Either:

- **Memory drifted** — correct the memory.
- **The record is wrong or stale** — a session never written up, an integration that missed something, an edge never added.

Both are common and the second is easy to overlook. Correcting the record from the view should be as fast as noticing the discrepancy; a read-only validation surface leaks errors back into the record.

### Two encodings, different profiles

| | Text | Visualization |
|---|---|---|
| Bandwidth | Sequential, precise | High-volume, parallel |
| Best for | Authoring, editing, exact attributes | Discovery, topology, validation, memory access |
| Role | Canonical record | Route in, fact source, error detection, index |

Neither is a lossy version of the other. Same propositions, different encodings.

---

## Description is a first-class output

An earlier draft of [[GM-Considerations]] treated sensory description as translation work outside the GM's native mode. That was wrong.

This GM describes worlds in words natively — and describes them *precisely*: where things sit relative to one another, what colors and shapes are present, how a space is composed. That is description, and a strong form of it: relational and concrete rather than impressionistic.

For a table, the relational mode is arguably the more useful one. Players assemble their own mental picture more reliably from spatial relationships and concrete attributes than from atmosphere.

Description belongs in the tool for the same reason everything else does: **latency, not difficulty.** Prepared descriptive text for locations, NPCs, and set pieces is retrieval-ready material — one less thing to compose mid-sentence while three people wait.

---

## What this means in practice

| Surface | Form |
|---|---|
| Entity records | Structured text — facts, attributes, typed relationships |
| Prep view | Text: opening beats, live branches, likely NPCs, prepared description |
| **At the table** | **Graph view: zoomed out, 1–2 hops, centered on play; text one step away** |
| At-the-table lookup | Text, fast, searchable |
| Authoring and editing | Text, or inline from a view |
| Finding non-obvious structure | Graph view, wider scope |
| Checking record against memory | Graph view, zoomed in |
| State machines and lifecycles | Rendered on request |
| Temporal diffs and trajectories | Rendered on request |
| Coverage and readiness | Text statement first; visual if scale makes it clearer |

Away from the table, the default presentation is text. At the table, the map is the front door and the text is what it opens onto.
