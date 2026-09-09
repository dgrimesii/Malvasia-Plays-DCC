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

- **Typed** — `occurs_in`, `advances`, `appears_in`, `member_of`, `escalates_to`, `owns`, `references`, `hostile_to`. A closed vocabulary, not free text.
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

## Events are the connective tissue

The three planning tiers are not the same kind of thing, and conflating them is what made the Zone/Arc relationship feel awkward:

- **Zone** — *where*. A place. People and things exist there; events happen there. It has its own attributes (hazards, floor modifier, layout) that are true regardless of any storyline.
- **Arc** — *why*. A narrative that ties people, things, and events into a storyline. It has no inherent location.
- **Event** — *what happened*. An encounter, a scene, a revelation. This is the thing that has both a place and a meaning.

So the correct shape is:

```
Event --occurs_in--> Zone
Event --advances--> Arc
```

**A Zone is not directly connected to an Arc.** "Which arcs touch Floor 1" is a *derived* answer — traverse the events that occurred there and collect what they advance. It is not a fact to be stored, and storing it is what creates drift.

This also means a Zone can host events from several unrelated arcs without acquiring a confused identity, and an Arc can move across floors without being re-parented.

### Not everything routes through events

Some relationships are genuinely direct and shouldn't be forced through an event:

- `NPC --key_figure_in--> Arc` — Godpapa John belongs to the Food is Love storyline whether or not he has yet appeared in a scene.
- `NPC --member_of--> Faction`
- `NPC --located_in--> Zone` — where someone habitually is, independent of any event.

The test: if the relationship would still be true with zero sessions played, it's direct. If it only became true because something happened, it belongs on an event.

## Why directionality matters here

Both ends should surface the relationship, but not identically. Standing on the Zone, the useful reading is "the Warden operates here." Standing on the NPC, it's "operates in the Serving Warrens." Same edge, two phrasings, both needed. That means the interface derives the inverse view rather than requiring two hand-maintained links — which is what `arc:` and `zones: []` do today, and which will drift.

## What this buys

- **Intersection notes have a home.** They live on the edge.
- **Backlinks stop being manual.** Traversal in either direction is free.
- **Visibility gets finer.** "Players know the Warden exists, and know the Convergence exists, but don't know he works for them" becomes expressible — which the current file-level `visibility` flag cannot say at all.
- **Continuity checking becomes possible.** Contradictions are easier to spot on a graph than across prose.
- **Suggested connections have a shape.** "These two nodes are two hops apart via an unremarked path" is a concrete thing to surface to the GM.
- **Arcs stay portable.** A storyline isn't pinned to a floor, so it can resurface anywhere without contradiction.

## Consequences for the current templates

The live templates encode the flattened version and would need revising if this model is adopted:

- `Template-Zone.md` has an `arc:` frontmatter field — under this model that's derived, not stored, and should come off.
- `Template-Arc.md` has `zones: []` — same; derived from the events that advance the arc.
- Encounter blocks need an `Advances:` field — currently an encounter records where it happens but not what storyline it serves, which is the missing half of the pair.
- `Template-Session.md` has `arc:` and `zone:` — defensible, since a session is a real-world container rather than a fictional event, but worth revisiting.

Not yet applied — flagged pending a decision.

## Tension with current storage

Markdown files hold node content well and edge attributes badly. Options, all deferrable:

1. **Edges in frontmatter** — structured edge lists on each node. Readable, but the inverse must be derived at read time, and edge attributes get verbose.
2. **Edges as their own records** — a separate store of edges referencing node IDs. Clean model, but the files stop being self-describing when read directly.
3. **Hybrid** — simple edges stay in frontmatter; only edges that need attributes (notes, conditions, own visibility) get promoted to records.

No decision needed now. What matters is that the *model* is a directed attributed graph, whatever serializes it.

## Open questions

1. **How closed is the edge vocabulary?** Too small and it can't express the campaign; too open and it stops being queryable.
2. **Is a Session an event, or a container of events?** It's a real-world sitting, not a fictional occurrence — which suggests container, with encounters as the events inside it.
3. **Do edges need their own history,** or only their current state?
4. **Are Notes nodes or edges?** A note about one thing is a node; a note about an intersection is an edge attribute. Possibly both, possibly a node that can attach to an edge.
5. **Does a node's visibility cascade to its edges,** or are they independent? Independent is more expressive and more work.
6. **What happens to an edge when a node is deleted or merged?**
