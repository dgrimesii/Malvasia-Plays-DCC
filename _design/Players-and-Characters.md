---
type: design
status: draft
visibility: gm
tags: [model, characters, players, knowledge]
---

# Players, Characters, and Knowledge

Resolves the character death question from [[Open-Requirements]] §7 and simplifies the visibility model.

---

## Two knowledge domains, and only two

- **GM** — everything.
- **Players** — a subset, revealed deliberately by the GM.

No per-player knowledge. No per-character knowledge. The party knows what the party knows.

This collapses several questions that looked hard:

- **Character death has no knowledge implications.** A new character doesn't need to un-know anything, because knowledge was never held at the character level.
- **Visibility is binary**, not a per-person calculation.
- **Split-party scenes need no modeling.** If Hilda goes off alone, the record doesn't track that the others weren't there. The GM handles it in play, the way tables always have.

The cost is real but small: the tool can't represent one character knowing something the others don't. That's a trust-and-roleplay matter, not a data matter (see [[Scope]] — the tool doesn't enforce, it supports recall).

---

## Knowledge and ownership are different axes

Worth stating plainly, because the earlier `player-rw` tag blurred them:

| | What it governs | Granularity |
|---|---|---|
| **Knowledge** | What has been revealed about the world | Party-level |
| **Ownership** | Who wrote something and can edit it | Per-player |

A player's private note is *their content*, not world knowledge. Sam speculating that the Warden works for Godpapa John is "Sam wrote that," attributed and owned by him — not a fact the party knows.

So the two coexist cleanly: knowledge is shared, authorship is individual.

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

That makes the useful things work with no special handling: NPCs can reference them, the party can avenge or mourn them, their arcs continue or resolve on their own terms, and evidence attached to them stays valid because it describes what happened.

A new character is a new asset linked to the same player. Nothing transfers, because nothing needs to.

### Investment survives death automatically

The capture split in [[Session-Capture]] pays off here for a reason it wasn't designed for:

| Layer | Attributed to | On character death |
|---|---|---|
| In-fiction | The character | Stays as that character's history |
| Table-level | The player | Carries forward intact |
| Roleplaying | The player | Carries forward intact |

Sam's investments belong to Sam. When Z dies, the record of what Sam returns to, argues about, and looks up is unaffected — which is correct, since Sam cares about the same things the following week.

---

## Also open

**What happens when a player leaves the campaign?**
Their characters keep their state; their notes remain theirs. Whether their record stays visible to the others is a question about the table, not the data.
