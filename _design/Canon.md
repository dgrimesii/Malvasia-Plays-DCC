---
type: design
status: draft
visibility: gm
tags: [canon, arcs, design]
---

# Canon

The campaign takes place inside a story that has already been written. This document covers how the party's story relates to that one.

Companion to [[North-Star]], [[GM-Considerations]], [[Arcs]], and [[Information-Architecture]].

---

## Settled facts

- **Same timeline.** The campaign runs concurrently with the books. Canon proximity is therefore computable, not hand-waved — a canon event has a real position relative to where the party is.
- **Canon characters are supported.** The game system provides stats and NPC entries for key book characters, including Carl. Meeting them is a sanctioned mechanic, not an improvisation.
- **Early floors stay clear.** No canon-character contact planned for Floors 1–5.
- **Floor 6 is a threshold.** Book events from that floor onward are noticeable to *any* crawler on that floor, whether or not they participate.

---

## The gift and the problem

**The gift:** the source material establishes that millions of crawlers are running the dungeon simultaneously, almost entirely off-screen. The party is canonically consistent by construction — they don't need to be squeezed into gaps in the written story, because the written story explicitly says most of what happened wasn't shown.

**The problem:** a canon timeline is running whether or not the party interacts with it. Carl's actions have consequences at scale — floor-wide, sometimes dungeon-wide. The GM has to decide, repeatedly, whether the party feels them.

That decision is not once-per-campaign. It recurs every time canon and the party's position converge.

---

## A third structure

[[Arcs]] describes two trees — the planning tree (physical, near-term) and the arc tree (emotional, campaign-long). Canon is a third thing, and it behaves unlike either:

| | Planning tree | Arc tree | **Canon** |
|---|---|---|---|
| Authored by | The GM | GM + players | **Someone else, already** |
| Responds to the party | Yes | Yes | **No** |
| Timeline | The party's | The party's | **Its own** |
| Changeable | Freely | Through play | **Only by deliberate divergence** |

Canon's defining property: **it proceeds on its own schedule regardless of the table.** It's the one structure the party cannot influence by default — which is exactly what makes it feel like a real world rather than a stage.

---

## Four relationships

At any moment, the party's story stands in one of four relationships to canon:

### Parallel
Canon events happen; the party is unaware. The default for Floors 1–5, and correct — being unaware of most of a vast world is what makes it vast.

### Proximate
The party experiences the *effects* of a canon event without participating in it. A floor-wide announcement. A change in what mobs do. A crowd reacting to something on the broadcast. Prices shifting because a market crashed elsewhere.

**This is the highest-value relationship for the campaign**, and from Floor 6 it becomes the default state rather than an occasional event. It delivers the vast-world feeling almost for free — the party feels the world reacting to something they had nothing to do with, which is the strongest possible evidence that it exists independently of them.

### Intersecting
The party is directly involved in or present at a canon event. Rare, high-impact, and expensive: it constrains the outcome (canon says how it ends) and risks making the party spectators in their own campaign.

Worth reserving. A campaign can survive one or two of these; more and the party is following someone else's plot.

### Divergent
Something at the table contradicts canon. Once this happens, the campaign has branched and canon becomes reference rather than truth from that point forward.

Divergence isn't a failure. It's often the point — the unwritten chapters may require it. But it needs to be *known*, because everything downstream that assumed canon is now suspect.

---

## The canon intensity curve

Canon pressure is not constant across the campaign. It has a shape, and Floor 6 is the inflection:

| Phase | Floors | Default relationship | What it's for |
|---|---|---|---|
| **Insulated** | 1–5 | Parallel | The party's own story is the only story. Investment forms. Arcs emerge. |
| **Ambient** | 6+ | Proximate | The world audibly presses in. Canon is unavoidable background. |
| **Contact** | TBD | Intersecting, selectively | Direct involvement, used sparingly |

### Why the insulated phase matters

The early floors aren't a delay before the real content. They're where the party acquires something of their own to lose.

**If the party's arcs aren't established before Floor 6, canon will arrive and they'll have no anchor.** They'll be tourists exactly when the world gets loud — the museum failure mode from [[North-Star]], arriving on a schedule.

This makes the insulated phase a deadline, not just a warm-up:

- By Floor 6, at least one arc should be `established` — something the party demonstrably cares about.
- The investment tracking described in [[Arcs]] matters most during Floors 1–5, because that's when there's nothing else competing for the table's attention.
- If nothing has emerged by Floor 5, that's a signal worth acting on rather than pushing forward. What to do about it is a judgment call — see [[GM-Considerations]].

### Why the ambient phase works

Once the party has their own stakes, canon stops being a distraction and becomes contrast. Their small, personal, unwritten story playing out against enormous events they can hear but not control is exactly the North Star tension — delivered structurally rather than through GM effort.

The shift itself is also a dramatic beat. Floor 6 feeling *different* — louder, more consequential, harder to ignore — is worth playing deliberately.

---

## Canon proximity

Whether the party feels a canon event is a function of two distances:

- **Spatial** — same floor? same neighborhood? adjacent?
- **Temporal** — same session-time? recently? long ago?

Plus a third property of the event itself:

- **Reach** — how far its effects propagate. A private conversation reaches nobody. A dungeon-wide broadcast reaches everyone. Most things fall between.

A canon event should be surfaced to the GM when the party is inside its reach:

> The party is on Floor 6 during a canon event with floor-wide reach. Do they see it?

The answer is often *yes, partially, and without context* — which is the most flavorful version. They see the aftermath, or the announcement, or the crowd's reaction, and don't know what it means. Later, they find out. That gap is where the world feels largest.

---

## Canon fidelity is a dial

How much canon shapes the campaign is undecided, and it doesn't need one answer. It's a setting, and it can differ by category:

| Category | Example question |
|---|---|
| **World rules** | Do the System's mechanics work exactly as written? *(Probably yes — this is what makes it DCC.)* |
| **Geography** | Are floors laid out as described? *(Probably mostly — with room for unwritten neighborhoods.)* |
| **Major events** | Do Carl's landmark moments happen on schedule? *(Yes from Floor 6 — they're ambient.)* |
| **Named characters** | Can the party meet them? Can they die differently? *(Meeting is supported; outcomes undecided.)* |
| **Outcomes** | Does the overall story end as written? *(Probably the least important to preserve.)* |

High fidelity on world rules and geography costs nothing and buys enormous authenticity. High fidelity on major events and outcomes is what constrains the party's agency. **They're separable, and treating them as one dial is the mistake.**

---

## What this asks of the model

Canon events need to be first-class nodes, distinguishable from GM-authored events:

- `type: canon-event`
- **When** it occurs on the canon timeline
- **Where** — floor, location
- **Reach** — how far effects propagate
- **Source citation** — book/chapter reference only, never reproduced text
- **Status** — `pending` / `experienced-proximate` / `intersected` / `diverged` / `omitted`

Canon characters are NPC nodes with an added property marking them as canon — their dispositions and outcomes are constrained by the source in a way ordinary NPCs aren't.

And the model needs:

- **A canon timeline the party's timeline can be positioned against**, so proximity is computable rather than remembered.
- **Divergence marking.** When the table contradicts canon, that point is recorded and everything downstream that depended on it is flagged — the same premise-decay mechanism described in [[Arcs]].
- **Separation of canon fact from GM interpretation.** What the books establish and what this table decided must never blur, or the GM loses the ability to check.

**Copyright:** canon events are recorded as citations and original GM summaries. The source books are someone else's work; this repo references them and never reproduces them.

---

## How this serves the North Star

Canon is the most direct instrument for the vast-world half of the goal. A party feeling the aftershock of something enormous they had no part in — and not fully understanding it — is the feeling the whole design is chasing.

And it serves the authorship half through contrast. The party's chapters are unwritten precisely *because* other chapters are written. Standing at the edge of a famous moment and reacting to it in a way the books never recorded is exactly the experience being aimed at.

The intensity curve is how both halves get delivered in the right order: authorship first, vastness second, contrast third.

---

## Open questions

1. **Can the party affect canon outcomes,** or only experience them? The first is more exciting and much harder to keep coherent.
2. **What happens if a player has read the books?** Julia, Amy, or Sam knowing what's coming changes proximate events entirely — dramatic irony instead of mystery. Not necessarily worse, but different, and worth knowing per-player before Floor 6.
3. **Does divergence need to be visible to players?** Knowing the campaign has left canon is itself a powerful narrative fact — or a spoiler about what canon was.
4. **How much canon needs recording before play** versus being pulled in as proximity arises? Floors 1–5 need almost none; Floor 6 onward needs enough to compute proximity reliably.
5. **Do canon events feed the arc tree?** A canon figure the party comes to care about from a distance could carry real weight — and would be an arc they share with millions of other crawlers, which is its own interesting thing.
