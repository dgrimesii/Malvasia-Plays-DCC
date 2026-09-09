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

**Nodes** are the things: Arc, Quest, Zone, Session, Encounter, NPC, Faction, Item, Player Character, Note.

Nodes have attributes — largely what's in frontmatter today (`type`, `status`, `visibility`, `source`).

**Edges** are the relationships between them. Edges are:

- **Typed** — `occurs_in`, `advances`, `contributes_to`, `appears_in`, `member_of`, `escalates_to`, `owns`, `references`, `hostile_to`. A closed vocabulary, not free text.
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

The planning tiers are not the same kind of thing, and conflating them is what made the Zone/Arc relationship feel awkward:

- **Zone** — *where*. A place. People and things exist there; events happen there. It has its own attributes (hazards, floor modifier, layout) that are true regardless of any storyline.
- **Arc** — *why it matters*. A narrative thread. It has no inherent location.
- **Event** — *what happened*. An encounter, a scene, a revelation. This is the thing that has both a place and a meaning.
- **Session** — *when, in the real world*. A timebox containing the events the players experienced through their characters. Not a fictional occurrence; a container.

So the correct shape is:

```
Event --occurs_in--> Zone
Event --advances--> Quest
Event --contributes_to--> Arc
Session --contains--> Event
```

**A Zone is not directly connected to an Arc.** "Which arcs touch Floor 1" is a *derived* answer — traverse the events that occurred there and collect what they contribute to. It is not a fact to be stored, and storing it is what creates drift.

This also means a Zone can host events from several unrelated storylines without acquiring a confused identity, and an Arc can move across floors without being re-parented.

## Quest and Arc are different things

They have been conflated so far — the existing `Arc-Food-is-Love.md` is labeled "Quest Arc," straight from the source synthesis. They need separating.

| | **Quest** | **Arc** |
|---|---|---|
| Nature | A pre-defined objective | An emergent story thread |
| Origin | Authored, assigned, or discovered | Recognized in hindsight |
| State | Completable: `not started` / `active` / `complete` / `failed` | Never "completed" — it develops, resolves, or is abandoned |
| Boundaries | Known at creation | Only clear in retrospect |
| Player-facing | Usually yes — players know they have a quest | Usually not — this is GM sense-making |
| Required? | A quest need not belong to any arc | An arc need not contain any quest |

**Quests are objects.** They have objectives, success and failure conditions, and rewards. They behave like encounters: concrete, resolvable, and knowable in advance.

**Arcs are interpretations.** If an RPG is collective storytelling, arcs are the storylines being built — recognized as they emerge from what the table actually does, not planned in advance and executed. They function as *narrative hints for the GM*, shaping what to plan next rather than dictating it.

### Consequences

- An arc's membership grows over time. An event that seemed incidental three sessions ago can be recognized as part of a thread later — which means **arc membership must be assignable retroactively**, without rewriting the event.
- Arcs should not have a `status` that implies a lifecycle of planned stages. Something looser — `forming` / `developing` / `resolving` / `dormant` — fits how they actually behave.
- A quest can be completed while the arc it fed continues.
- **This is where AI assistance is most valuable.** Noticing that four scattered events form an unremarked thread is exactly the pattern-finding a GM can't easily do by hand across months of play, and exactly what a graph makes tractable.

### Not everything routes through events

Some relationships are genuinely direct and shouldn't be forced through an event:

- `NPC --key_figure_in--> Arc` — Godpapa John belongs to the Food is Love thread whether or not he has yet appeared in a scene.
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
- **Emergent threads become discoverable.** "These events are two hops apart via an unremarked path" is a concrete thing to surface — and is how arcs get found.
- **Arcs stay portable.** A storyline isn't pinned to a floor, so it can resurface anywhere without contradiction.

## Consequences for the current templates

The live templates encode the flattened version and would need revising if this model is adopted:

- `Template-Zone.md` has an `arc:` frontmatter field — under this model that's derived, not stored, and should come off.
- `Template-Arc.md` has `zones: []` and a `Stages / Milestones` table — both assume a planned lifecycle. Derived membership and a looser status fit better.
- **There is no Quest template.** One is needed — objective, success/failure conditions, reward, state.
- Encounter blocks need `Advances:` (quest) and `Contributes To:` (arc) — currently an encounter records where it happens but not what it serves.
- `Arc-Food-is-Love.md` is currently both a quest and an arc and should be split.

Not yet applied — flagged pending a decision.

## Tension with current storage

Markdown files hold node content well and edge attributes badly. Options, all deferrable:

1. **Edges in frontmatter** — structured edge lists on each node. Readable, but the inverse must be derived at read time, and edge attributes get verbose.
2. **Edges as their own records** — a separate store of edges referencing node IDs. Clean model, but the files stop being self-describing when read directly.
3. **Hybrid** — simple edges stay in frontmatter; only edges that need attributes (notes, conditions, own visibility) get promoted to records.

No decision needed now. What matters is that the *model* is a directed attributed graph, whatever serializes it.

## Open questions

1. **How closed is the edge vocabulary?** Too small and it can't express the campaign; too open and it stops being queryable.
2. **Can an event contribute to an arc without the GM saying so** — i.e. are suggested arc memberships surfaced automatically, or only on request?
3. **Do edges need their own history,** or only their current state?
4. **Are Notes nodes or edges?** A note about one thing is a node; a note about an intersection is an edge attribute. Possibly both, possibly a node that can attach to an edge.
5. **Does a node's visibility cascade to its edges,** or are they independent? Independent is more expressive and more work.
6. **What happens to an edge when a node is deleted or merged?**
7. **Are player-facing quests and GM-facing quests the same object** with a visibility flag, or genuinely different?
