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
| State | Completable: `not started` / `active` / `complete` / `failed` | Recognized, then develops or goes dormant |
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

## Investment has two sources

Investment is the precondition for arcs, and it arrives two ways. Both are needed; neither is sufficient alone.

### Inferred (observed)

The system notices patterns across recorded play: the party has had meaningful interactions with three NPCs who turn out to be related; a name keeps recurring in session notes; they returned to the same place unprompted.

This is a graph query — clustering on entities the players have repeatedly touched, then checking whether those entities are themselves connected.

### Declared (intended)

The GM states outright that something is meant to be part of an arc, or is being planted as future weight. This is explicit and doesn't wait for evidence.

### They are not the same thing, and the difference matters

A declared arc is an **intent**, not an accomplished fact. The GM can decide a thread is meant to matter; only the table can make it matter. Which means the model should distinguish:

- **Intended** — the GM has declared this a thread
- **Realized** — player investment is evidenced in what actually happened

An intended arc with no realized investment is itself a useful signal: the GM keeps pushing a thread the table isn't biting on. Better to see that plainly than to keep escalating stakes nobody feels.

### The ticket

The interaction that makes inference useful is **contextual interruption, not a dashboard.** When the GM is authoring an event involving an entity that has accumulated investment, the system raises a ticket at that moment:

> Three prior meaningful interactions involve members of this family. This may be arc material — consider raising the stakes.

Properties that make this work:

- **Fires at the point of authoring**, when the GM can act on it, not in a report read later.
- **Cites its evidence** — which interactions, which sessions — so the GM can judge whether the pattern is real.
- **Proposes, never applies.** It may suggest raising stakes or attaching to an arc; it does neither on its own.
- **Dismissible with memory.** A rejected ticket shouldn't return every time the same entity comes up.

## Arc states

**An arc becomes established by GM declaration.** Nothing else promotes it — not evidence thresholds, not system confidence. The system proposes; the GM decides.

During integration and discovery, the system surfaces potential arcs. Each suggestion gets one of three responses:

| Response | Meaning | Result |
|---|---|---|
| **Approve** | This is a real thread | Becomes `established` — plannable, usable as a lens |
| **Reject** | Not a thread, or not one worth keeping | Discarded, and **remembered** so the same pattern isn't re-proposed |
| **Defer** | Might become something — watch it | Becomes `emerging` — kept, accumulating evidence, not yet real |

Deferral is not indecision. It's an explicit instruction to keep watching, which makes emerging arcs a **live watchlist** rather than a parking lot.

### The states

| State | Meaning | Can plan from it? |
|---|---|---|
| `suggested` | System-proposed, not yet triaged | No |
| `emerging` | GM deferred — watching for more development | No |
| `established` | GM declared it real | **Yes** |
| `dormant` | Established, but receiving no new events | Yes — and worth reviewing |
| `resolved` | Concluded | Historical reference |

The gate is `established`. Only past that point does the causality inversion apply and the arc become a planning lens.

### What the system does with emerging arcs

Because deferral means "watch this," the system has an ongoing job:

- **Re-surface on new evidence.** When an emerging arc accumulates further support — another related interaction, another investment signal — bring it back with the new evidence attached, rather than waiting for the GM to remember it exists.
- **Don't nag on silence.** An emerging arc with no new evidence stays quiet. Re-proposing the same case with nothing added is noise.
- **Age gracefully.** An emerging arc that develops nothing over many sessions should eventually be offered for dismissal rather than lingering indefinitely.

## The arc lifecycle — and the inversion

An arc's relationship to planning reverses once it's established.

**Before establishment — arcs are discovered.** Events accumulate, investment builds, and the thread is recognized in hindsight. Causality runs *events → arc*. The system's job is noticing.

**After establishment — arcs drive planning.** The arc becomes a lens the GM plans through: what does this thread need next, who's owed a reappearance, where would pressure land hardest. Causality runs *arc → events*. The system's job shifts from noticing to serving.

The same node, two directions, depending on where it is in its life. That has consequences:

- **An arc file must work as a prep surface, not just a record.** Once established it's something the GM opens *before* planning a session, alongside the zone and the session doc.
- **Flagging becomes deliberate.** Post-establishment, the GM attaches new events, quests, NPCs, and items to the arc as an intentional act — no inference required, no ticket needed.
- **Inference doesn't stop being useful**, but it changes register: less "is there a thread here," more "this new element connects to an established thread you may not have noticed."
- **Arcs can go dormant and return.** A thread that stops receiving events isn't dead; it's waiting. Dormancy should be visible so the GM can decide whether to revive or let it rest.

### Consequences

- **Arc membership must be assignable retroactively.** An event that seemed incidental three sessions ago can be recognized as part of a thread later, without rewriting the event.
- **Arcs cannot be planned into existence**, only prepared for and declared as intent — but once they exist, they absolutely can be planned *from*.
- A quest can be completed while the arc it fed continues.
- Session records need to capture *meaningful interaction*, not just events — otherwise there's nothing for inference to run on.
- **Two distinct AI jobs, worth keeping separate:** surfacing candidate investment (observation), and proposing where a callback would carry weight (authoring). Only the second should ever require approval as content.

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
- **Emergent threads become discoverable.** Investment clustering and unremarked connections are both graph queries — and are how arcs get found.
- **Established arcs become plannable.** Once a thread exists, "what does it need next" is a traversal, not a memory exercise.
- **Arcs stay portable.** A storyline isn't pinned to a floor, so it can resurface anywhere without contradiction.

## Consequences for the current templates

The live templates encode the flattened version and would need revising if this model is adopted:

- `Template-Zone.md` has an `arc:` frontmatter field — under this model that's derived, not stored, and should come off.
- `Template-Arc.md` has `zones: []` and a `Stages / Milestones` table — both assume a planned lifecycle. It needs somewhere to record *what the stakes are, whose investment they rest on*, its state, the evidence supporting it, and — once established — what the thread needs next.
- **There is no Quest template.** One is needed — objective, success/failure conditions, reward, state.
- Encounter blocks need `Advances:` (quest) and `Contributes To:` (arc).
- Session records need a place for *meaningful interactions*, distinct from events — the raw material for inference.
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
2. **What counts as a "meaningful interaction"?** Inference needs a recordable unit. Is it GM-flagged at session write-up, or inferred from the narrative text itself?
3. **How strong must a pattern be before a ticket fires?** Too eager and it becomes noise the GM learns to dismiss reflexively.
4. **Do emerging arcs need a name before they're established?** Naming a thread makes it feel real prematurely; not naming it makes it hard to refer to.
5. **Can two emerging arcs merge** when evidence shows they're the same thread — and what happens to their accumulated evidence?
6. **Do edges need their own history,** or only their current state?
7. **Are Notes nodes or edges?** A note about one thing is a node; a note about an intersection is an edge attribute.
8. **Does a node's visibility cascade to its edges,** or are they independent?
9. **What happens to an edge when a node is deleted or merged?**
10. **Are player-facing quests and GM-facing quests the same object** with a visibility flag, or genuinely different?
