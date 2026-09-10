---
type: design
status: draft
visibility: gm
tags: [model, events]
---

# Off-Screen Events

Things that happened in the world without the party present.

---

## What they are

An NPC acts. A faction moves. Something burns down three floors up. The GM records it as having happened, because it did.

An off-screen event is **an event with `visibility: gm` and no party participants**. That's the whole model. It needs no new node type.

What distinguishes it from things already modeled:

| | Happened? | Party knows? |
|---|---|---|
| Event | Yes | Yes |
| **Off-screen event** | **Yes** | **Not yet** |
| Speculative event | No — may never | No |
| Projection | No — a forecast | No |

The key difference from a projection: **an off-screen event is a fact.** It can be reasoned over, referenced, and built on with the same confidence as anything the party witnessed.

---

## Why they matter

Without them, the world only changes when the party is looking at it. That's the difference between a world and a stage set.

[[North-Star]] asks for consequences that propagate and for factions whose actions reach the party before they ever meet them. Off-screen events are how that gets built. A faction that has been *doing things* for six sessions arrives with history; one that springs into existence on contact doesn't.

They also give the GM somewhere to put decisions made between sessions. Deciding an NPC retaliates is currently homeless — too settled to be a projection, not witnessed enough to be an event. This is the slot.

---

## They behave like canon events

From the party's side, an off-screen GM event and a canon event are the same thing: something that happened elsewhere whose effects may reach them.

The model in [[Canon]] applies unchanged — **reach**, and the four relationships:

- **Parallel** — it happened; they never know
- **Proximate** — they feel the effects without knowing the cause
- **Intersecting** — they encounter it directly, or its aftermath
- **Revealed** — they learn what happened, later

Proximate remains the highest-value state. The party finding a door barred that was open last week, with no explanation, is the world acting independently of them — which is exactly the feeling the whole design chases.

---

## Revelation is partial by default

When the party learns about an off-screen event, they rarely learn all of it. They find the aftermath, or hear a rumor, or see one participant's version.

This is the attribution model from [[Facts-and-Revelation]] doing its usual work: what they learn is *"a survivor told you the Warden's men came through"* — not the event itself. The GM holds the full record; the party holds an account of it.

So a single off-screen event can produce several partial, possibly contradictory revelations over time, and the record stays coherent throughout.

---

## Available for inference

Once recorded, an off-screen event is normal graph content. It participates in clustering, connects to arcs, and can be the missing link that explains why three NPCs are behaving strangely.

One useful consequence: **the GM can ask what the party would notice.** Given an off-screen event with a given reach, and the party's current position, what effects should be visible? That's a traversal, and it's the sort of thing that's easy to forget in the moment and cheap to surface in prep.

---

## Open

**Do off-screen events need scheduling, or only recording?**
Deciding "the Warden retaliates next week" is a fact about the future. Whether that's an event with a future date, or something distinct, is worth settling if in-fiction time gets tracked at all.
