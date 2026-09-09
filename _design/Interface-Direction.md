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

This is the one that matters most at the table.

An **imperfect but essentially accurate** visualization works as an index into memory. It doesn't need to contain the information — it needs to reliably *point* at it. Seeing the local structure locates the memory address, and from there relationships are traversed internally at speed.

The requirement here is different from validation's. An access key needs to be **legible and fast**, not complete. A cluttered but faithful diagram is a good audit and a bad key.

---

## The tension: audit versus key

These two jobs pull in opposite directions and cannot be served well by one view.

| | Audit view | Reference view |
|---|---|---|
| Optimizes for | Completeness, fidelity | Legibility, speed |
| Shows | Everything, including weak and uncertain edges | The strong local structure |
| Omission | Never — omission destroys the check | Expected — that's what makes it readable |
| Used | Between sessions, deliberately | At the table, glanced at |
| Failure if wrong | Silent false correction | Missed hook |

**Both are needed, and they should be distinct modes rather than a compromise.** A single "balanced" view would be a mediocre key and a dangerous audit.

Audit mode keeps every constraint from the validation section: no inferred edges drawn as established, no hiding sparse data, gaps shown as gaps, uncertainty visibly distinct, layout may change but content may not.

Reference mode may simplify freely — as long as it's *labeled* as simplified, so it's never mistaken for the audit.

---

## The table view

The one visualization that stands open rather than being requested.

**Purpose:** when an interaction or event happens, provide an immediate map of nearby hooks worth pulling into play.

**Shape:**

- **Centered on current context** — the zone, scene, or NPC in play right now.
- **One to two hops out.** Beyond that is noise under time pressure.
- **Hooks marked distinctly** — unused threads, live arcs, player investments, information not yet revealed, dangling questions. These are the reason the view exists; they should be the most visible thing on it.
- **Re-centers fast** as the scene moves. A view that takes ten seconds to update is unusable mid-session.
- **Useful without interaction.** A glance should pay off. Clicking is a bonus, not the mechanism.
- **Text detail one step away** — the map locates, the record supplies the specifics.

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
| **At the table** | **Reference visualization, open; text detail one step away** |
| At-the-table lookup | Text, fast, searchable |
| Authoring and editing | Text, or inline from a view |
| Finding non-obvious structure | Visualization, discovery mode |
| Checking record against memory | Visualization, audit mode — faithful, complete |
| Graph topology, clusters, gaps | Rendered on request, scoped, multiple layouts |
| State machines and lifecycles | Rendered on request |
| Temporal diffs and trajectories | Rendered on request |
| Coverage and readiness | Text statement first; visual if scale makes it clearer |

Away from the table, the default presentation is text. At the table, a reference map is the front door and the text is what it opens onto.
