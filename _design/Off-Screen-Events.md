---
type: design
status: draft
visibility: gm
tags: [model, events, states]
---

# Off-Screen Events

Things that happened in the world without the party present. Also the authoritative statement of **event state**.

---

## Events have three states

**Planned** — hasn't happened, and the party doesn't know it's coming. GM prep.
**Pending** — hasn't happened, and the party knows it's coming.
**Fact** — happened.

**Reveal** is what moves `planned` to `pending`.

### This revises an earlier decision

An earlier version of this document said there were two states and rejected any third: *no scheduling, no future-dated facts, no "certain but pending."*

**That rejection was correct on its own grounds and does not cover this case.** What it refused was **GM certainty** — the idea that deciding the Warden will retaliate makes it more than planned. That still holds absolutely:

> **GM certainty doesn't make something a fact, or anything other than planned.** Deciding the Warden will retaliate is planned, however inevitable it feels.

`pending` is not about the GM's confidence. It is about **what the party knows.** The dungeon announces the next floor opens in three days; a tournament is scheduled; a quest carries a deadline. The event has not occurred, and the party is aware of it. No amount of GM certainty produces that state, and no amount of GM uncertainty prevents it.

### The cost of the change, stated

`planned` is now reserved for **prep the party has not seen**, which means the axis is no longer purely *has this happened* — `pending` bundles non-occurrence with revelation.

That is a deliberate trade. `planned` is the state the GM touches constantly, and having it mean *mine, unseen* is worth more than keeping the axis pure. The consequence is that **`planned` implies `gm`**: it is a constraint on the combination, not a redefinition of visibility.

`fact` remains independently `gm` or `player`, because something can occur without the party learning of it — which is what an off-screen event is.

### Pending belongs to events. Never to entities.

| Object | States |
|---|---|
| **Event** | `planned` → `pending` → `fact`. Time is intrinsic; an event occurs. |
| **Entity** | **Materialized or not.** No time component at all. |

Per [[Glossary]], an entity materializes when the party learns it **exists** — by meeting it, or simply by being told. A map showing a place materializes it. Whether they ever go there is irrelevant, and nothing un-materializes.

The asymmetry is not an inconsistency. It follows from what the objects are: an entity exists or is not yet known to; an event occurs, once.

**Where this will get misapplied.** *The Warden is coming for us* reads colloquially as a pending person. It is two things: a **materialized entity**, and a **pending event** in which he arrives. Prose fuses them; the parser's job is to split them — the same operation the extraction rule already performs on utterances.

If `pending` migrates onto the entity, the never-happens problem below becomes a pending *person* who never arrives, with no clean way to retire the state.

### Effort and happened-ness are different axes

The effort ladder tracks authoring, not state:

| Ladder | State |
|---|---|
| `speculative` — held as a possibility, unwritten | Planned |
| `potential` — authored, not run | Planned or pending |
| `used` — played | Fact |

How much work has gone into something says nothing about whether it happened, or whether the party knows of it.

### A pending event that never happens

An announced future can fail. The floor opens in three days, and it doesn't.

A pending event cannot sit pending forever and cannot become `fact`. It resolves through **the claim that announced it**: the claim goes `false` per [[Claims-and-Resolution]], and the event is abandoned.

Which means event state and claim resolution have to be reconcilable rather than independently maintained. See §Open.

---

## What an off-screen event is

An NPC acts. A faction moves. Something burns down three floors up. The GM records it as having happened, because it did.

An off-screen event is **a fact with `visibility: gm` and no party participants**. No new node type needed.

| | Happened? | Party knows? |
|---|---|---|
| Event | Yes | Yes |
| **Off-screen event** | **Yes** | **Not yet** |
| Pending event | No — but announced | Knows it's coming |
| Planned event | No — may never | No |

The key property: an off-screen event is a fact, so it can be reasoned over, referenced, and built on with the same confidence as anything the party witnessed.

---

## Announcement is an event too

The case that makes the distinction concrete, and it needs no new machinery.

An announcement in session A about something happening later is **an appearance of that later event** — a reference, not the thing. So there are three records:

1. An event in session A: the announcement was made.
2. A **claim** carried by it: *the floor opens in three days.* Resolution `undetermined`.
3. The floor opening itself: a separate event, now `pending`.

A `references` relationship joins (1) to (3). The party knows a **claim about** the event, which is what carries `player` visibility — the event itself is still a thing they have never participated in.

This is the pattern from [[Canon]] pointed forward instead of sideways: there, a canon fact stays unrevealed while its consequences reach the party through a linked ordinary fact. Here, a future event stays unoccurred while knowledge of it reaches the party through a linked claim.

**And announcements can lie.** The claim may be false, mistaken, or out of date. The party can equally be told of a place that does not exist — a forged map, a trap, a record gone stale. Materialization is one-way and permanent, so they will permanently know of a place that isn't there.

That is correct behaviour, not a defect. They *do* know of it, and being wrong is a legitimate state. **Materialization and truth are independent** — the same treatment [[Names-and-Aliases]] already gives a name that is known and false.

---

## Why they matter

Without them, the world only changes when the party is looking at it. That's the difference between a world and a stage set.

[[North-Star]] asks for consequences that propagate and factions whose actions reach the party before they ever meet them. Off-screen events are how that gets built. A faction that has been *doing things* for six sessions arrives with history; one that springs into existence on contact doesn't.

---

## They behave like canon events

From the party's side, an off-screen GM event and a canon event are the same thing: something that happened elsewhere whose effects may reach them.

The model in [[Canon]] applies unchanged — **reach**, and the four relationships:

- **Parallel** — it happened; they never know
- **Proximate** — they feel the effects without knowing the cause
- **Intersecting** — they encounter it directly, or its aftermath
- **Revealed** — they learn what happened, later

Proximate remains the highest-value state. A door barred that was open last week, with no explanation, is the world acting independently of them.

---

## Revelation is partial by default

When the party learns about an off-screen event, they rarely learn all of it. They find the aftermath, hear a rumor, or get one participant's version.

The attribution model from [[Facts-and-Revelation]] does the work: what they learn is *"a survivor told you the Warden's men came through"* — not the event itself. The GM holds the full record; the party holds an account of it.

A single off-screen event can produce several partial, possibly contradictory revelations over time, and the record stays coherent throughout.

---

## Available for inference

Once recorded, an off-screen event is normal graph content. It participates in clustering, connects to arcs, and can be the missing link explaining why three NPCs are behaving strangely.

One useful consequence: **the GM can ask what the party would notice.** Given an off-screen event's reach and the party's position, what effects should be visible? That's a traversal, easy to forget in the moment and cheap to surface during prep.

---

## Open

1. **How do event state and claim resolution stay reconcilable?** A pending event that fails resolves through its announcing claim going `false`. Whether that is automatic, GM-confirmed, or surfaced as a **Ticket** is undecided — but it must not be two facts kept in sync by hand.
2. **Can an event be pending with no announcing claim?** The party might infer something is coming without being told. Probably yes, and probably it still needs a recorded basis for their knowing.
3. **Does `pending` need a deadline field?** The requirement was explicitly *with or without a specific point in time*, so no — but a pending event with a fiction-time date and one without may behave differently for coverage.
