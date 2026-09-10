---
type: design
status: draft
visibility: gm
tags: [model, events]
---

# Off-Screen Events

Things that happened in the world without the party present.

---

## Events have two states

**Planned** — hasn't happened, and may not.
**Fact** — happened.

That's the whole state model. No scheduling, no future-dated facts, no "certain but pending."

**GM certainty doesn't make something a fact.** Deciding the Warden will retaliate is planned, however inevitable it feels. It becomes a fact when the GM records it as having occurred.

### Effort and happened-ness are different axes

The encounter ladder in [[Information-Architecture]] tracks authoring effort, not state:

| Ladder | State |
|---|---|
| `speculative` — held as a possibility, unwritten | Planned |
| `potential` — authored, not run | Planned |
| `used` — played | Fact |

How much work has gone into something says nothing about whether it happened. Only the state matters for what can be reasoned over.

---

## What an off-screen event is

An NPC acts. A faction moves. Something burns down three floors up. The GM records it as having happened, because it did.

An off-screen event is **a fact with `visibility: gm` and no party participants**. No new node type needed.

| | Happened? | Party knows? |
|---|---|---|
| Event | Yes | Yes |
| **Off-screen event** | **Yes** | **Not yet** |
| Planned event | No — may never | No |

The key property: an off-screen event is a fact, so it can be reasoned over, referenced, and built on with the same confidence as anything the party witnessed.

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
