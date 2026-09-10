---
type: design
status: draft
visibility: gm
tags: [north-star, goals]
---

# North Star

Everything else in `_design/` is instrumental to this. When a design decision is unclear, this is the thing to decide against.

See [[Scope]] for what's explicitly out of bounds.

---

## The goal

The players should feel two things at once:

1. **They are inside a world that is vastly larger than them** — one written across thousands of pages, with history, factions, rules, and consequences that existed before they arrived and will continue without them.
2. **They are writing chapters that were never written** — not touring someone else's story, but adding to it.

The tension between those is the whole problem. Lean too far toward the first and the players are tourists being shown around a museum. Lean too far toward the second and it stops being Dungeon Crawler Carl — it's a generic dungeon with the serial numbers filed off.

---

## The constraint

The world is enormous. Contact with it is a few hours at a time, once a week, mediated entirely through one person talking.

That asymmetry is the core design problem:

- The GM cannot exposit the world into existence. Nobody wants a lecture.
- The players cannot read their way in. They're here to play, not study.
- Anything not surfaced during those few hours effectively does not exist for them.

So the world has to be conveyed by **implication and consequence** rather than description. A faction feels real when its actions have reached the party before they ever meet it. A rule feels real when it constrains someone other than them. History feels real when someone refers to it without explaining it.

**The GM's leverage is selective revelation.** Not knowing more — surfacing the right small thing at the right moment, so the players infer the rest.

---

## What this asks of the tool

### For the sense of a vast world

- **The right detail must be findable in seconds, mid-session.** A world detail the GM can't retrieve while talking is a world detail that doesn't exist. This is a latency requirement, not a completeness requirement.
- **Established lore should be connectable to current play.** "This thing the party just did rhymes with something already established" is exactly the connection that makes the world feel continuous rather than assembled around them.
- **Consequences should propagate.** Something that happened three sessions ago showing up as an offhand reference now is worth more than any amount of description.
- **Reference, don't reproduce.** The source books are someone else's copyrighted work. This repo holds citations, GM notes, and original material — never copied passages.

### For the sense of authorship

- **Player-created content must sit as an equal to canon in the player view.** If their notes look like scratch paper attached to the real material, they'll feel like annotators. If their record of what happened sits alongside the world's record, they'll feel like authors.
- **Their choices must visibly change things.** An NPC's disposition shifting, a faction's stance moving, a place being different than it was. Change is the proof that authorship is real.
- **Their inventions should become world facts.** A name a player coins, a reputation they earn, a rumor they start — once it's in the record with the same weight as anything else, the world has absorbed their contribution.

---

## How the rest of the design serves this

| Design element | What it's actually for |
|---|---|
| The graph model | Making consequence traceable, so the world can react to what players did |
| Arcs | Ensuring the party's own story has weight and shape |
| The planning tree | Making sure the world is ready wherever they go, so it feels like it exists independently |
| Density band | Story that neither grinds nor railroads |
| Investment tracking | Noticing what the players are actually drawn to, so the GM can build on it |
| Visibility control | Preserving discovery, which is what makes a large world feel large |
| The player interface | Making the world persist between sessions, and their contributions visible in it |

---

## The test

For any feature under consideration:

> Does this make the world feel bigger, or make the players' mark on it feel more real?

If neither, it's overhead. Some of the best features will do both — a player's action being referenced later by an NPC they've never met does both at once.

---

## Failure modes to design against

- **The museum.** Beautifully documented world, players moving through it without changing anything.
- **The blank room.** Total freedom, no sense of place, could be any dungeon in any system.
- **The lecture.** GM conveying the world by explaining it rather than showing consequence.
- **The scrapbook.** Player contributions recorded but visibly second-class, so authorship feels indulged rather than real.
- **The lost detail.** The GM knows the perfect callback exists but can't find it in time, so it never gets said.
