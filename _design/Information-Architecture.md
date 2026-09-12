---
type: design
status: draft
visibility: gm
tags: [information-architecture, graph, model]
---

# Information Architecture — Graph Model

The object model: what exists in the store, what attaches to what, and which answers are stored versus derived.

**Authoritative for the shape of the store.** Individual objects have their own documents — [[Claims-and-Resolution]], [[Visibility-Model]], [[Settings-and-Campaigns]], [[Names-and-Aliases]], [[Arcs]] — and this document says how they fit together. Where it conflicts with one of those, the specific document wins and this one is wrong.

Consumed by RC 1a. [[Inference-and-Candidate-Relationships]] §Information architecture requirements states what the inference layer additionally needs; those requirements are incorporated below.

---

## The problem this solves

The original storage was a file per entity with wikilinks between them. That gives an implicit graph, but a weak one: links are untyped (a link means "related somehow"), undirected (no way to say which way the relationship runs), and carry no attributes of their own (no way to say when it became true, whether players know it, or how strong it is).

Several things in the flat-file version are really edges wearing a costume:

- `arc:` on a Zone or Session — a typed edge to an Arc
- `Escalates To` on an encounter — a directed edge with a condition attached
- `zones: []` on an Arc — the reverse of `arc:`, maintained by hand and able to drift
- Every `[[wikilink]]` — an untyped edge

The intersection-note problem is the same problem: a note about how an NPC relates to a faction is not a property of either one. It is a property of the relationship.

**The model is a directed attributed graph.** Note that this is a statement about the model, not about the storage engine — see §Storage below, where the decision is settled.

---

## The objects

Six kinds of thing. Everything else in the vocabulary is one of these wearing a domain name.

| Object | What it is |
|---|---|
| **Entity** | A thing in the world with its own identity: a person, place, group, or object. Durable across campaigns; belongs to the **Setting**. |
| **Fact** | Something recorded about an entity. **A first-class object, not an attribute.** |
| **Claim** | A proposition carried by an utterance, with its own resolution state. See [[Claims-and-Resolution]]. |
| **Relationship** | A typed, directed connection between two entities, carrying its own attributes. |
| **Event** | A thing that happened or is planned to happen. The connective tissue — see below. |
| **Session** | A real-world timebox containing the events the players experienced. Not a fictional occurrence. |

**Arc, Quest, NPC, Faction, Place, Item, Player Character are not separate node types in the store.** They are entities distinguished by their type attribute and by what relates to them. This matters most for Place: per [[Glossary]], places contain places to any depth through an ordinary `contains` relationship, with **no fixed tier count and no enumerated place types.** *Zone* and *Floor* are this campaign's names for two tiers, not classes the model enforces.

An earlier version of this document enumerated node types including Zone. That is superseded.

### Setting sits above Campaign

Per [[Settings-and-Campaigns]]: entities belong to the setting and are durable across campaigns. Facts, sessions, reveals, arcs, and visibility belong to a campaign. Identifiers are unique within a **setting**, not within a campaign.

Both tiers exist from the start holding exactly one of each, and the setting is invisible until a second campaign is created. It is thin structure, not a feature.

---

## Facts are objects, not frontmatter

**The single largest change from the flat-file model**, and the one most likely to be built wrongly by carrying the old shape forward.

In the file-per-entity version, what an entity *is* lives in its prose and its frontmatter. In the store, each assertion about an entity is a separate record, because each one independently carries:

- its own **provenance** — who asserted it, from which side of the screen, and how it arrived
- its own **visibility** — the party can know an NPC exists, know one of their names, and not know a third thing about them
- its own **record time and fiction time**
- its own **state** — `planned` or `fact`

A **Name** is a fact, not a header — an entity can hold several at once, with different audiences and different truth values. See [[Names-and-Aliases]].

### Typed facts

Some facts carry a **type and a comparable value** alongside their prose: species, profession, origin, era. Prose stays primary for reading; the typed form exists so facts can be compared.

Required because *has a scar on his wrist* and *bears an old mark on his forearm* are the same fact in prose and different strings to a matcher. Without it, **Parallel without contact** is unbuildable — and unbuildable permanently, since the structure was never captured.

Only a small set is worth typing: the attributes plausibly indicating shared background. Not hair colour. Which ones earn it is readable from the **golden corpus** after use rather than settled by argument now.

### Planned and actual apply per fact, not only per event

Previously `planned`/`fact` was a property of **Events**. Under Record Plans it is not: *the Warden will turn out to be Hilda's uncle* is a planned **relationship**, and *the eastern reach has a smuggler problem* is a planned **fact**.

So the axis applies to facts and relationships too, and it is **orthogonal to visibility.** All four combinations are meaningful:

| | `gm` | `player` |
|---|---|---|
| `planned` | the normal case — prep the party has not met | a planned reveal, scheduled but not yet made |
| `fact` | happened, not yet known to the party | happened and known |

The `planned` + `player` cell is the one worth checking against implementation: it means a reveal the GM has committed to but not executed, which is distinct from a fact already revealed. If that turns out to be indistinguishable from an unrevealed fact in practice, the axis collapses to three states and should say so.

---

## The two clocks

**Everything carries both record time and fiction time.** Record time is when it entered the store; fiction time is when it happened in the world. An event can be authored in session 20 and set three hundred years earlier.

This is not tidiness. The strongest inference signal available — *this detail was recorded in session 3, the concept it matches was invented in session 20, so the connection cannot have been designed* — reads **record time exclusively.** Omit it and the signal is not merely unbuilt but permanently impossible.

Fiction time is also **optionally absent.** A `speculative` entity from a regional pass may have no fiction time and no place yet, per [[Planning-Loop]], and the store must hold that without treating it as an incomplete record.

---

## Relationships

**Typed** — a closed vocabulary, not free text: `occurs_in`, `advances`, `contributes_to`, `appears_in`, `member_of`, `contains`, `escalates_to`, `owns`, `references`, `hostile_to`, `supersedes`. How closed remains open — see §Open.

**Directed** — direction carries meaning. *Warden serves Godpapa John* is not *Godpapa John serves Warden.*

**Attributed** — relationships carry their own data, independent of either endpoint:

| Attribute | Purpose |
|---|---|
| `visibility` | The party may know two things exist without knowing they are connected |
| `established_in` | Which session made this true |
| `state` | `planned` or `fact` |
| `note` | The GM insight about *this specific intersection* |
| `condition` | For conditional relationships like escalation |

An earlier version listed a `status` of `suspected / established / broken`. **`suspected` is superseded**: a proposed connection is not a relationship with a weak status, it is a **candidate relationship**, which per [[Inference-and-Candidate-Relationships]] is a derived grouping of clues and not a stored edge at all. Nothing enters the relationship table until the GM accepts it. `broken` is better expressed as a new fact superseding an old one than as a mutated edge.

### Structural versus evidence-bearing

A partition the inference layer requires, and the reason high-degree hub entities do not swamp it.

**Structural relationships** are containment and membership: everything is inside a Place, everyone is in the party. They are traversable for retrieval and **not traversable as inference intermediates**, because a path running *A is in Zone 3, Zone 3 contains B* restates geography rather than evidencing anything.

The limit is **by relationship type, not by a degree threshold** — defensible in the same way the two-hop cutoff is, where a degree-weighted score would not be.

### Session membership is a third thing

Participation in a session must be structurally distinct from both of the above. *Co-occurrence without connection* — two entities appearing in the same sessions repeatedly with no recorded link — is incoherent if appearing together is itself an edge in the same graph, because the signal would be detecting its own input.

### Directionality and the inverse view

Both ends should surface a relationship, but not identically. Standing on the Place, the useful reading is *the Warden operates here*; standing on the NPC, *operates in the Serving Warrens.* Same relationship, two phrasings, both needed.

**The interface derives the inverse rather than storing it.** Two hand-maintained links — which is what `arc:` and `zones: []` do in the flat files — will drift.

---

## Events are the connective tissue

The planning tiers are not the same kind of thing, and conflating them is what made the Place/Arc relationship feel awkward:

- **Place** — *where*. People and things exist there; events happen there. Its own attributes (hazards, layout) are true regardless of any storyline.
- **Arc** — *why it matters*. A narrative thread carrying real stakes. No inherent location.
- **Event** — *what happened*. An encounter, a scene, a revelation. The thing that has both a place and a meaning.
- **Session** — *when, in the real world*. A container, not a fictional occurrence.

So the shape is:

```
Event --occurs_in--> Place
Event --advances--> Quest
Event --contributes_to--> Arc
Session --contains--> Event
```

**A Place is not directly connected to an Arc.** *Which arcs touch Floor 1* is a **derived** answer — traverse the events that occurred there and collect what they contribute to. It is not a fact to be stored, and storing it is what creates drift.

This also means a Place can host events from several unrelated storylines without acquiring a confused identity, and an Arc can move across floors without being re-parented.

### Not everything routes through events

Some relationships are genuinely direct:

- `NPC --key_figure_in--> Arc` — a figure can belong to a thread before appearing in a scene
- `NPC --member_of--> Faction`
- `NPC --located_in--> Place` — where someone habitually is, independent of any event

**The test:** if the relationship would still be true with zero sessions played, it is direct. If it only became true because something happened, it belongs on an event.

---

## Quest and Arc are different things

| | **Quest** | **Arc** |
|---|---|---|
| Nature | An assignment | A narrative thread with stakes |
| Origin | Authored, assigned, or discovered | Emerges from play |
| State | Completable | Recognised, then develops or goes dormant |
| Boundaries | Known at creation | Only clear in retrospect |
| Player-facing | Usually yes | Usually not named — but felt |
| Required? | Need not belong to any arc | Need not contain any quest |
| Can be authored? | Yes, fully | **No** — only its conditions can be set up |

**Quests are assignments.** Objectives with success and failure conditions and rewards. Concrete, resolvable, knowable in advance. They behave like encounters.

**Arcs require stakes the players actually feel.** Connection alone is just continuity. An arc exists when something the players are *invested in* is placed at risk and a choice about it carries weight. That investment cannot be authored, because player attachment cannot be authored.

### How an arc is born

1. A quest is assigned — deal with the rats on Floor 1. Purely an assignment.
2. Something unplanned happens: the party bonds with one of the rats. The GM did not write this; it emerged at the table.
3. Sessions later, that rat reappears on another floor, in peril.
4. The party must choose whether to save it or let it die. **The choice has weight because of step 2.**

Only at step 4 does an arc exist. Steps 1 and 3 are authored; step 2 is not; and without step 2, step 4 is just an encounter.

The GM's leverage is noticing step 2 and *engineering step 3* — setting up the conditions for weight, then letting the table supply the meaning.

### Arc as a node: what this document is responsible for

The arc lifecycle, its states, and the triage that moves between them are **[[Arcs]]'s** subject, not this document's. What matters structurally:

- **Arc is an entity.** It gains meaning through `contributes_to` relationships from events, not through membership lists.
- **Arc membership must be assignable retroactively.** An event that seemed incidental three sessions ago can be recognised as part of a thread later, **without rewriting the event** — which is exactly what a separate relationship record buys and what a frontmatter field on the event would not.
- **Causality inverts at establishment.** Before: events accumulate and the thread is recognised in hindsight, so the system's job is noticing. After: the arc becomes a lens the GM plans through, so the system's job is serving. Same node, two directions.
- **Arc Intent is a distinct thing from Arc.** Per [[Glossary]], material authored to provoke a thread that does not exist yet. An earlier version of this document called these *intended* and *realized* arcs; that vocabulary is superseded. An Arc Intent with no corresponding arc is a useful signal — the GM pushing a thread the table is not biting on.

---

## Investment and Signal — corrected

An earlier version of this document said investment has two sources, inferred and declared. **Superseded**, and the correction matters because it changes who decides.

- **Investment** is a GM-set **degree** on a fixed scale, recorded as an event with provenance. Never calculated, never aggregated automatically. Its history is read off the sequence of those events.
- **Signal** is the inference pass's read of accepted facts as evidence that a degree *may* have shifted. Not a recorded event in its own right, and not a second source of investment — it is one of the things a **Ticket** can be about.

So the system never holds an investment value it computed. It surfaces evidence; the GM sets the degree.

The contextual-interruption property from the earlier version survives and is right: a signal fires **at the point of authoring**, cites which interactions and which sessions, proposes and never applies, and is dismissible with memory. That is the **Ticket** mechanism, specified in [[Inference-and-Candidate-Relationships]].

---

## What the inference layer needs from the store

Stated here because these are store-shape requirements, not inference implementation details. Full reasoning in [[Inference-and-Candidate-Relationships]].

1. **Two clocks** on everything. Unrecoverable if omitted.
2. **Typed facts.** Unrecoverable if omitted.
3. **Session membership partitioned** from narrative relationships.
4. **Structural relationships marked** as non-traversable for inference.
5. **Clue as a stored object** with a deterministic key, a frozen snapshot at rejection, and its walked path stored rather than regenerated.
6. **Candidate relationships derived, not stored** — a grouping of clues by entity pair.
7. **Candidate behaviour under reconciliation** — merge, dedupe, and destroy any candidate whose endpoints became the same entity.
8. **A decision on clues resting on planned facts** that never became actual.
9. **Weak edges derived, not stored.** Co-occurrence, convergence, and density are all derivable from session membership and existing typed relationships. Deciding this explicitly matters, because the alternative gets built by default the first time someone caches a co-occurrence count.

---

## Storage

**Settled.** The target store is a real database from RC 1a, per [[Store-and-Access]] and [[Roadmap]]. The repo-as-database pattern was a prior assumption and is superseded — the motivation for web hosting was precisely the limits of a repo as both store and access surface, so building on flat files first would buy a painful migration for nothing.

A graph **domain model** on a **relational store** is the working position. Not necessarily a graph database: recursive containment and bounded traversal are both tractable in SQL, and the hard constraints here are per-fact provenance and visibility rather than deep traversal.

The earlier version of this document weighed three markdown serialisation options. All three are superseded and have been removed.

One consequence worth keeping visible: **the search index is a projection of the store**, not the store itself, per [[Modes-and-Surfaces]]. Anything pruned for search quality must still exist for inference.

---

## What this buys

- **Intersection notes have a home.** They live on the relationship.
- **Backlinks stop being manual.** Traversal in either direction is free.
- **Visibility gets finer.** *The party knows the Warden exists, knows the Convergence exists, and does not know he works for them* becomes expressible, which a file-level flag cannot say at all.
- **Lies stay lies.** An utterance and the claim it carries are separate records, so the record never asserts a deception in its own voice.
- **Continuity checking becomes possible.** Contradictions are easier to spot on a graph than across prose.
- **Emergent threads become discoverable.** Investment signals and unremarked connections are both graph queries.
- **Established arcs become plannable.** *What does this thread need next* is a traversal, not a memory exercise.
- **Arcs stay portable.** A storyline is not pinned to a place, so it can resurface anywhere without contradiction.

---

## Consequences for the current templates and content

Conversion is an implementation task, scoped by Epic 13.

- `Template-Zone.md` has an `arc:` field — derived under this model, not stored. It comes off.
- `Template-Arc.md` has `zones: []` and a `Stages / Milestones` table, both assuming a planned lifecycle. It needs stakes, whose investment they rest on, state, supporting evidence, and — once established — what the thread needs next.
- **There is no Quest template.** One is needed: objective, success and failure conditions, reward, state.
- Encounter blocks need `Advances:` (quest) and `Contributes To:` (arc).
- Session records need somewhere for **meaningful interactions**, distinct from events — the raw material for signals.
- Session records need **speaker attribution preserved**, so utterances and claims survive conversion. See [[Claims-and-Resolution]].
- `Floor-XX-Name.md` files convert to nested places with **no tier types**, per Epic 13 S10. Converting them as-is would bake a two-tier geography into the store on day one.
- `Arc-Food-is-Love.md` should be reclassified as a quest.

---

## Open questions

1. **How closed is the relationship vocabulary?** Too small and it cannot express the campaign; too open and it stops being queryable. Now also interacts with the structural / evidence-bearing partition, since the partition is defined by type.
2. **What counts as a meaningful interaction?** Signals need a recordable unit. GM-flagged at write-up, or inferred from the narrative text?
3. ~~How strong must a pattern be before a ticket fires?~~ **Answered in principle** by [[Live-Set]]: a ranked **attention budget**, not a confidence threshold. The number is still open.
4. **Do emerging arcs need a name before establishment?** Naming makes a thread feel real prematurely; not naming makes it hard to refer to.
5. **Can two emerging arcs merge** when evidence shows they are the same thread, and what happens to their accumulated evidence?
6. **Do relationships need their own history,** or only current state? Note the supersession pattern in [[Canon]] suggests history-by-new-record rather than mutation, which may answer this generally.
7. **Are Notes objects or relationship attributes?** A note about one thing is a fact; a note about an intersection is a relationship attribute. Whether that is sufficient, or notes need first-class identity with multiple attachments, is undecided.
8. ~~Does a node's visibility cascade to its edges?~~ **Answered** by [[Visibility-Model]]: independent, held per fact and per relationship.
9. **What happens to a relationship when an entity is deleted or merged?** Merge behaviour is specified for candidates but not for relationships. Interacts with the tombstone decision in [[Rollback-and-Repair]].
10. **Are player-facing and GM-facing quests the same object** with a visibility flag, or genuinely different? Note the two state machines meet at exactly one point per [[Glossary]], which suggests one object.
11. **Does the `planned` + `player` combination exist in practice,** or does the state axis collapse to three? See §Planned and actual.
12. **Person versus role.** Flagged as an open question by Epic 13 and not yet addressed here: whether *the Warden* is an entity, a role an entity holds, or both.
