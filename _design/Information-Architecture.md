---
type: design
status: draft
visibility: gm
tags: [information-architecture, graph]
---

# Information Architecture — Graph Model

## The problem this solves

The current storage is a file per entity, with wikilinks between them. That gives an implicit graph, but a weak one: links are untyped (a link means "related somehow"), undirected (no way to say which way the relationship runs), and carry no attributes of their own (no way to say when it became true, whether players know it, or how strong it is).

Several things already in use are really edges wearing a costume:

- `arc:` on a Zone or Session — a typed edge to an Arc
- `Escalates To` on an encounter — a directed edge with a condition attached
- `zones: []` on an Arc — the reverse of `arc:`, maintained by hand and able to drift
- Every `[[wikilink]]` — an untyped edge

The GM-insight-about-an-intersection problem is the same problem: a note about how an NPC relates to a faction isn't a property of either one. It's a property of the relationship.

## The model

**Nodes** are the things: Arc, Zone, Session, Encounter, NPC, Faction, Item, Player Character, Note.

Nodes have attributes — largely what's in frontmatter today (`type`, `status`, `visibility`, `source`).

**Edges** are the relationships between them. Edges are:

- **Typed** — `appears_in`, `member_of`, `escalates_to`, `advances`, `located_in`, `owns`, `references`, `hostile_to`. A closed vocabulary, not free text.
- **Directed** — the direction carries meaning. "Warden *serves* Godpapa John" is not "Godpapa John *serves* Warden."
- **Attributed** — edges carry their own data, independent of either node.

**Edge attributes** worth having:

| Attribute | Purpose |
|---|---|
| `visibility` | Players may know two things exist without knowing they're connected |
| `established_in` | Which session made this true |
| `status` | `suspected` / `established` / `broken` — relationships change |
| `note` | The GM insight about *this specific intersection* |
| `condition` | For conditional edges like escalation |

## Why directionality matters here

Both ends should surface the relationship, but not identically. Standing on the Zone, the useful reading is "the Warden operates here." Standing on the NPC, it's "operates in the Serving Warrens." Same edge, two phrasings, both needed. That means the interface derives the inverse view rather than requiring two hand-maintained links — which is what `arc:` and `zones: []` do today, and which will drift.

## What this buys

- **Intersection notes have a home.** They live on the edge.
- **Backlinks stop being manual.** Traversal in either direction is free.
- **Visibility gets finer.** "Players know the Warden exists, and know the Convergence exists, but don't know he works for them" becomes expressible — which the current file-level `visibility` flag cannot say at all.
- **Continuity checking becomes possible.** Contradictions are easier to spot on a graph than across prose.
- **Suggested connections have a shape.** "These two nodes are two hops apart via an unremarked path" is a concrete thing to surface to the GM.

## Tension with current storage

Markdown files hold node content well and edge attributes badly. Options, all deferrable:

1. **Edges in frontmatter** — structured edge lists on each node. Readable, but the inverse must be derived at read time, and edge attributes get verbose.
2. **Edges as their own records** — a separate store of edges referencing node IDs. Clean model, but the files stop being self-describing when read directly.
3. **Hybrid** — simple edges stay in frontmatter; only edges that need attributes (notes, conditions, own visibility) get promoted to records.

No decision needed now. What matters is that the *model* is a directed attributed graph, whatever serializes it.

## Open questions

1. **How closed is the edge vocabulary?** Too small and it can't express the campaign; too open and it stops being queryable.
2. **Do edges need their own history,** or only their current state?
3. **Are Notes nodes or edges?** A note about one thing is a node; a note about an intersection is an edge attribute. Possibly both, possibly a node that can attach to an edge.
4. **Does a node's visibility cascade to its edges,** or are they independent? Independent is more expressive and more work.
5. **What happens to an edge when a node is deleted or merged?**
