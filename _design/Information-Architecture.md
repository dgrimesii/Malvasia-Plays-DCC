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
- **Arc** — *why it matters*. A narrative thread carrying real stakes. It has no inherent location.
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

They have been conflated so far — the existing `Arc-Food-is-Love.md` is labeled "Quest Arc," straight from the source synthesis. "Food is Love" is a **quest**, not an arc.

| | **Quest** | **Arc** |
|---|---|---|
| Nature | An assignment | A narrative thread with stakes |
| Origin | Authored, assigned, or discovered | Emerges from play |
| State | Completable: `not started` / `active` / `complete` / `failed` | Develops, resolves, or goes dormant |
| Boundaries | Known at creation | Only clear in retrospect |
| Player-facing | Usually yes — players know they have a quest | Usually not named — but felt |
| Required? | A quest need not belong to any arc | An arc need not contain any quest |
| Can be authored? | Yes, fully | **No** — only its conditions can be set up |

**Quests are assignments.** Objectives with success and failure conditions and rewards. Concrete, resolvable, knowable in advance. They behave like encounters.

**Arcs require stakes the players actually feel.** An arc is not merely a thread connecting things — connection alone is just continuity. An arc exists when something the players are *invested in* is placed at risk, and a choice about it carries weight. That investment cannot be authored, because player attachment cannot be authored.

### How an arc is born

The worked example:

1. A quest is assigned — deal with the rats on Floor 1. Purely an assignment.
2. Something unplanned happens: the party bonds with one of the rats. The GM did not write this; it emerged at the table.
3. Sessions later, that rat reappears on another floor, in peril.
4. The party must choose whether to save it or let it die. **The choice has weight because of step 2.**

Only at step 4 does an arc exist. Steps 1 and 3 are authored; step 2 is not; and without step 2, step 4 is just an encounter.

The GM's actual leverage is in noticing step 2 and *engineering step 3* — setting up the conditions for weight, then letting the table supply the meaning.

### Consequences

- **Arc membership must be assignable retroactively.** An event that seemed incidental three sessions ago can be recognized as part of a thread later, without rewriting the event.
- **Arcs cannot be planned into existence**, only prepared for. A GM can hope for one and build the conditions; whether it becomes an arc is decided at the table.
- Arcs shouldn't carry a `status` implying planned stages — that's quest behavior. Something looser fits: `forming` / `developing` / `resolving` / `dormant`.
- A quest can be completed while the arc it fed continues.
- **Player investment is a first-class signal.** What the party names, returns to, protects, jokes about, or asks after is the raw material of arcs. If the tool tracks anything about players beyond their sheets, it should track this.
- **This is where AI assistance is most valuable.** Two distinct jobs: surfacing candidate investments ("the party has mentioned this rat unprompted in three sessions"), and proposing where a callback would carry weight. Neither is doable by hand across months of play; both are cheap on a graph.

### Not everything routes through events

Some relationships are genuinely direct and shouldn't be forced through an event:

- `NPC --key_figure_in--> Arc` — a figure can belong to a thread before appearing in a scene.
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
- **Emergent threads become discoverable.** Investment signals and unremarked connections are both graph queries — and are how arcs get found.
- **Arcs stay portable.** A storyline isn't pinned to a floor, so it can resurface anywhere without contradiction.

## Consequences for the current templates

The live templates encode the flattened version and would need revising if this model is adopted:

- `Template-Zone.md` has an `arc:` frontmatter field — under this model that's derived, not stored, and should come off.
- `Template-Arc.md` has `zones: []` and a `Stages / Milestones` table — both assume a planned lifecycle. Derived membership and a looser status fit better. It also needs somewhere to record *what the stakes are and whose investment they rest on*.
- **There is no Quest template.** One is needed — objective, success/failure conditions, reward, state.
- Encounter blocks need `Advances:` (quest) and `Contributes To:` (arc).
- `Arc-Food-is-Love.md` should be reclassified as a quest.

Not yet applied — flagged pending a decision.

## Tension with current storage

Markdown files hold node content well and edge attributes badly. Options, all deferrable:

1. **Edges in frontmatter** — structured edge lists on each node. Readable, but the inverse must be derived at read time, and edge attributes get verbose.
2. **Edges as their own records** — a separate store of edges referencing node IDs. Clean model, but the files stop being self-describing when read directly.
3. **Hybrid** — simple edges stay in frontmatter; only edges that need attributes (notes, conditions, own visibility) get promoted to records.

No decision needed now. What matters is that the *model* is a directed attributed graph, whatever serializes it.

## Open questions

1. **How closed is the edge vocabulary?** Too small and it can't express the campaign; too open and it stops being queryable.
2. **How is player investment recorded?** It's the precondition for arcs, but it's a soft signal — observed at the table, not a mechanical outcome. Does the GM log it deliberately, or is it inferred from session notes?
3. **Can an event contribute to an arc without the GM saying so** — are candidate memberships surfaced automatically, or only on request?
4. **Do edges need their own history,** or only their current state?
5. **Are Notes nodes or edges?** A note about one thing is a node; a note about an intersection is an edge attribute.
6. **Does a node's visibility cascade to its edges,** or are they independent?
7. **What happens to an edge when a node is deleted or merged?**
8. **Are player-facing quests and GM-facing quests the same object** with a visibility flag, or genuinely different?
