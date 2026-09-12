---
type: design
status: draft
visibility: gm
tags: [information-architecture, modes, personas, search, inference, retrieval]
---

# Modes and Surfaces

Three modes of use, the personas in each, and what each mode is optimised for.

Resolves the search-versus-inference tension left open by [[Inference-and-Candidate-Relationships]] and [[Retrieval-Tiering]].

---

## Why this document exists

Search and inference discovery pull the information architecture in opposite directions.

| | Wants | Cost of a false positive | Cost of a false negative |
|---|---|---|---|
| **Search** | recall, fuzzy matching, sharp typed vocabulary | a second to dismiss | the moment is lost |
| **Inference** | precision, weak edges, multi-hop traversal | attention that was never offered; trust in the channel decays | invisible — the GM never learns what they were not shown |

Same graph, same relatedness signal, **opposite operating points.** Treated as one surface, neither can be tuned well.

The mode structure dissolves most of the conflict: **inference never runs at the table.** It is confined to Session Capture and Session Planning, both of which happen between sessions with nobody waiting. Per [[Update-Cadence]], expensive computation there is effectively free. Precision and recall stop being a shared setting and become a per-mode property.

---

## Mode 1 — Table play

Works on existing facts and relationships. **No inference discovery. Read-only.**

Two personas; the GM has two sub-modes.

| Surface | Persona | Purpose |
|---|---|---|
| **Encounter Assistant** | GM | The planned facts about the current encounter at hand. Supports description, and relevance to previous and upcoming events. |
| **Role Play assistance** | GM | Visual of the relationships in the current encounter or event. Enables fast reaction to player questions and raises the relevance of improvised answers. |
| **Memory bank** | Players | Generic search over known facts and relationships about what is happening at the table. |

Both GM sub-modes read from the **[[Live-Set]]**, not from the whole graph.

### Role Play assistance needs a root

The relationship visual requires a root entity for its subgraph. The planned encounter is the sensible default, but the party goes off-plan precisely when improvisation support matters most. Posture: the planned encounter is the **default**, not the **frame** — the visual re-roots on whatever the GM last searched.

### No write path at the table

Anything the GM notices mid-session survives in their head until the recap. This is a deliberate decision, not an omission, and it is recorded here because it cuts against the lost-detail framing in [[North-Star]]. [[Update-Cadence]] previously left mid-session jotting open as *probably allow, nothing should depend on it*. Still open — see §Open.

---

## Mode 2 — Session Capture

One persona: the GM. Input is one or more recap documents.

1. **Parse and propose.** The system creates or updates facts about entities and relationships. The recap is treated as fact **about what happened at the table** — not as a statement of the truth of the information in it. See [[Claims-and-Resolution]].
2. **Review.** Captured facts are presented for review, editing, and acceptance.
3. **Inference analysis.** New and changed facts are examined against existing facts to discover candidate relationships. Candidates are queued. The GM accepts, rejects, or **accepts-and-augments** — an accepted inference must be editable, because the GM will usually want to add human context the detector could not supply.

This is stage 1 and stage 2 of the intake process already described in [[Session-Capture]].

---

## Mode 3 — Session Planning

One persona: the GM. Two sub-modes.

| Sub-mode | What it does |
|---|---|
| **Search** | Explore and search existing facts while planning future encounters. **The planning activity itself happens outside the tool** and produces plan documents. |
| **Record Plans** | Analogue of Session Capture plus inference analysis. Distinction: all inputs land in a **planned** state, and nothing is revealed. |

Record Plans is also where most **Resolutions** happen — the GM deciding what the story does next is the act that collapses an open claim. See [[Claims-and-Resolution]].

### Capture and Record Plans are one pipeline

They differ only in the state facts land in. Good news for sequencing: closer to one epic than two.

But it generalises something. Planned-versus-actual was previously a property of **Events** only. Under Record Plans, every fact and relationship needs it — *the Warden will turn out to be Hilda's uncle* is a planned relationship. That is a second axis, orthogonal to visibility, which is already held per fact per campaign per [[Settings-and-Campaigns]]. See §Open.

---

## Consequence: search is three surfaces, not one

| Surface | Optimise for | Failure mode |
|---|---|---|
| **GM, table** | one right answer, seconds, fragment input | the moment is lost |
| **Player, table** | visibility-filtered per [[Visibility-Model]] | reveals something unrevealed |
| **GM, planning** | breadth, multi-hop, wandering | a dead end with no path onward |

**Planning search is where browse-discovery lives** — the *I would recognise it if I saw it* job, one of the four named in [[Interface-Direction]]. So *no inference discovery at the table* does not mean discovery happens only in the inference queue. Planning search is discovery by a different mechanism and should be optimised for recall and traversal, not ranking.

**Hazard:** if these are built as one search with a toggle, the planning surface inherits the table's precision bias and becomes useless for exploration.

---

## Consequence: inference is write-time, not query-time

Inference runs as a batch pass between sessions and is **materialised as proposals** through intake. Search only ever reads accepted facts.

This settles the surfacing-versus-authoring decision that [[Roadmap]] records as blocking RC 1c sequencing: **surfacing is authoring.** An inference the GM accepts becomes an ordinary fact or relationship with its own provenance; one they reject is recorded as rejected.

Costs of the decision, stated so they are chosen rather than discovered:

- Discovery can never be interactive at the table.
- The scarce resource is **GM attention per prep cycle**, not compute — which argues for a fixed ranked quota rather than a confidence threshold. A threshold produces unpredictable volume; a budget is a promise.

---

## Consequence: inference corrects tiering's blind spot

[[Retrieval-Tiering]] optimises hot storage against the GM's plan. But inference's highest-value output concerns **cold** entities adjacent to the plan — the NPC from five sessions ago who turns out to touch a planned arc.

So inference is not competing with tiering. Its real job is **promoting cold material into hot before the session**, by way of the [[Live-Set]].

---

## Consequence for the store

The one conflict that does **not** dissolve: inference wants weak edges — co-occurrence, coincidence, absence, near-misses — because that is where non-obvious connection comes from. Search wants a sharp typed vocabulary, because weak edges explode the neighbourhood and wreck ranking.

Partial resolution: **the search index is a projection of the store that excludes weak edges.** One store, two views — the same move already made for visibility. The store-side vocabulary decision remains open.

General rule this implies: **any pruning done for search quality destroys inference substrate, and destroys it silently.** This is an information-architecture decision, not a tuning decision, and it puts the tombstone question in [[Rollback-and-Repair]] §G9 in a new light — tombstones are inference substrate, not only repair substrate.

---

## Open

1. **Weak-edge vocabulary in the store.** The projection handles the index; the store side is undecided.
2. **Planned/actual as a per-fact axis.** Confirm all four combinations of planned/actual against gm/player are meaningful before committing.
3. **Mid-session write path.** Still open. Whatever is decided, nothing may depend on it.
