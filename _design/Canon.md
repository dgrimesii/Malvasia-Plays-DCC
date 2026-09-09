---
type: design
status: draft
visibility: gm
tags: [canon, arcs, design]
---

# Canon

The campaign takes place inside a story that has already been written. This document covers how the party's story relates to that one.

Companion to [[North-Star]], [[Arcs]], and [[Information-Architecture]].

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
Canon events happen; the party is unaware. The default state, and correct most of the time. Being unaware of most of a vast world is what makes it vast.

### Proximate
The party experiences the *effects* of a canon event without participating in it. A floor-wide announcement. A change in what mobs do. A crowd reacting to something on the broadcast. Prices shifting because a market crashed elsewhere.

**This is the highest-value relationship for the campaign.** It delivers the vast-world feeling almost for free — the party feels the world reacting to something they had nothing to do with, which is the strongest possible evidence that it exists independently of them.

### Intersecting
The party is directly involved in or present at a canon event. Rare, high-impact, and expensive: it constrains the outcome (canon says how it ends) and risks making the party spectators in their own campaign.

Worth reserving. A campaign can survive one or two of these; more and the party is following someone else's plot.

### Divergent
Something at the table contradicts canon. Once this happens, the campaign has branched and canon becomes reference rather than truth from that point forward.

Divergence isn't a failure. It's often the point — the unwritten chapters may require it. But it needs to be *known*, because everything downstream that assumed canon is now suspect.

---

## Canon proximity

Whether the party feels a canon event is a function of two distances:

- **Spatial** — same floor? same neighborhood? adjacent?
- **Temporal** — same session-time? recently? long ago?

Plus a third property of the event itself:

- **Reach** — how far its effects propagate. A private conversation reaches nobody. A dungeon-wide broadcast reaches everyone. Most things fall between.

A canon event should be surfaced to the GM when the party is inside its reach:

> The party is on Floor 1 during a canon event with dungeon-wide reach. Do they see it?

The answer is often *yes, partially, and without context* — which is the most flavorful version. They see the aftermath, or the announcement, or the crowd's reaction, and don't know what it means. Later, they find out. That gap is where the world feels largest.

---

## Canon fidelity is a dial

How much canon shapes the campaign is undecided, and it doesn't need one answer. It's a setting, and it can differ by category:

| Category | Example question |
|---|---|
| **World rules** | Do the System's mechanics work exactly as written? *(Probably yes — this is what makes it DCC.)* |
| **Geography** | Are floors laid out as described? *(Probably mostly — with room for unwritten neighborhoods.)* |
| **Major events** | Do Carl's landmark moments happen on schedule? *(Undecided.)* |
| **Named characters** | Can the party meet them? Can they die differently? *(Undecided, and the riskiest.)* |
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

And the model needs:

- **A canon timeline the party's timeline can be positioned against**, so proximity is computable rather than remembered.
- **Divergence marking.** When the table contradicts canon, that point is recorded and everything downstream that depended on it is flagged — the same premise-decay mechanism described in [[Arcs]].
- **Separation of canon fact from GM interpretation.** What the books establish and what this table decided must never blur, or the GM loses the ability to check.

**Copyright:** canon events are recorded as citations and original GM summaries. The source books are someone else's work; this repo references them and never reproduces them.

---

## How this serves the North Star

Canon is the most direct instrument for the vast-world half of the goal. A party feeling the aftershock of something enormous they had no part in — and not fully understanding it — is the feeling the whole design is chasing.

And it serves the authorship half through contrast. The party's chapters are unwritten precisely *because* other chapters are written. Standing at the edge of a famous moment and reacting to it in a way the books never recorded is exactly the experience being aimed at.

---

## Open questions

1. **Is the campaign on the same timeline as the books,** or running earlier/later/concurrent-but-unspecified? This determines whether proximity is even computable.
2. **Can the party affect canon outcomes,** or only experience them? The first is more exciting and much harder to keep coherent.
3. **What happens if a player has read the books?** Julia, Amy, or Sam knowing what's coming changes the nature of proximate events entirely — dramatic irony instead of mystery. Not necessarily worse, but different, and worth knowing per-player.
4. **Does divergence need to be visible to players?** Knowing the campaign has left canon is itself a powerful narrative fact — or a spoiler about what canon was.
5. **How much canon needs recording before play** versus being pulled in as proximity arises? Recording all of it is enormous; recording none makes proximity undetectable.
6. **Do canon events feed the arc tree?** A canon event the party is invested in — a character they came to care about from a distance — could carry real weight.
