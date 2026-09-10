---
type: design
status: draft
visibility: gm
tags: [model, characters, players, knowledge, notes]
---

# Players, Characters, Knowledge, and Notes

Resolves [[Open-Requirements]] §1 and §7.

---

## Two knowledge domains, and only two

- **GM** — everything.
- **Players** — a subset, revealed deliberately by the GM.

No per-player knowledge. No per-character knowledge. The party knows what the party knows.

This collapses several questions that looked hard:

- **Character death has no knowledge implications.** A new character doesn't need to un-know anything, because knowledge was never held at the character level.
- **Visibility is binary**, not a per-person calculation.
- **Split-party scenes need no modeling.** If Hilda goes off alone, the record doesn't track that the others weren't there. The GM handles it in play, as tables always have.

The cost is small: the tool can't represent one character knowing something the others don't. That's a trust-and-roleplay matter, not a data matter (see [[Scope]]).

---

## Notes are shared, attributed content

There is no such thing as a private note.

A note is **attached to an entity** — an NPC, a zone, a faction, a session — and **carries an author**. Everyone sees it. The author is metadata, not access control.

> A player note on the Warden that happens to have been made by Sam.

This resolves several questions at once:

- **No private tier.** Nothing to hide, nothing to gate.
- **No shared-party layer to design.** There's one layer, and it's shared by default.
- **Does the GM see player notes?** Yes, trivially. Everyone sees everything on the player side.
- **Identity is for attribution, not permissions.** A name on a note, not accounts and gates. Much lighter than §1 assumed.

### Why shared is better here

It directly serves the authorship half of [[North-Star]]. A note by Sam sitting on the Warden's page, visible to everyone, next to the GM's material, is the opposite of the **scrapbook** failure mode — player contributions live in the record rather than in a personal sidebar.

It also gives the party a shared working memory. Notes become how they coordinate between sessions, not just how they remember individually.

### Notes are not knowledge

A note is attributed content, not a world fact. Sam speculating that the Warden works for Godpapa John reads as *"Sam thinks the Warden works for Godpapa John"* — true as a statement about Sam, regardless of whether the claim is right.

Same attribution rule that keeps NPC lies from becoming world facts (see [[Facts-and-Revelation]]). It's why player notes need no GM approval: a wrong note can't corrupt the record, because it was never asserting a fact.

---

## Players and characters are separate assets

- **Player** — a person at the table. Persists for the campaign.
- **Character** — a data asset with a state. Belongs to a player.

```
Player --plays--> Character
```

A player may have several characters over a campaign. A character has exactly one player.

### Death is a state, not a deletion

A dead character keeps its node, history, and relationships. `status: dead` and nothing else changes.

NPCs can reference them, the party can avenge or mourn them, their arcs continue or resolve on their own terms, and evidence attached to them stays valid because it describes what happened.

A new character is a new asset linked to the same player. Nothing transfers, because nothing needs to.

### Investment survives death automatically

The capture split in [[Session-Capture]] pays off here for a reason it wasn't designed for:

| Layer | Attributed to | On character death |
|---|---|---|
| In-fiction | The character | Stays as that character's history |
| Table-level | The player | Carries forward intact |
| Roleplaying | The player | Carries forward intact |

Sam's investments belong to Sam. When Z dies, the record of what Sam returns to, argues about, and looks up is unaffected — correct, since Sam cares about the same things the following week.

---

## Consequence for the visibility tag

The `visibility` frontmatter currently uses `gm | player-ro | player-rw`, which conflates knowledge with editability. Under this model it should be `gm | player` for knowledge, with authorship tracked separately on anything a player wrote.

Only the dossiers use `player-rw` today, so the change is cheap now and gets more annoying later.

---

## Also open

**What happens when a player leaves the campaign?**
Their characters keep their state; their notes stay in the record, still attributed. Probably nothing needs to happen.
