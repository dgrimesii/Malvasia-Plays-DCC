---
type: design
status: draft
visibility: gm
tags: [model, characters, players]
---

# Players and Characters

Resolves the character death question from [[Open-Requirements]] §7.

---

## They are separate assets

- **Player** — a person at the table. Persists for the campaign.
- **Character** — a data asset with a state. Belongs to a player.

A player may have several characters over a campaign. A character has exactly one player.

```
Player --plays--> Character
```

## Death is a state, not a deletion

A dead character keeps its node, its history, its relationships, and everything recorded about it. `status: dead` and nothing else changes.

That makes the useful things work without special handling:

- NPCs can reference them
- The party can avenge or mourn them
- Their arcs continue, resolve, or go dormant on their own terms
- Evidence attached to them stays valid — it describes what happened, which is still true

A new character is simply a new asset linked to the same player. Nothing transfers, because nothing needs to.

---

## Why investment survives death automatically

The capture split in [[Session-Capture]] pays off here for a reason it wasn't designed for.

| Layer | Attributed to | Survives character death |
|---|---|---|
| In-fiction | The character | Stays with the dead character, as history |
| Table-level | The player | Carries forward intact |
| Roleplaying | The player | Carries forward intact |

Sam's investments belong to Sam. When Z dies, the record of what Sam has been drawn to — which topics he returns to, what he argues about, what he looks up — is unaffected. Which is correct: Sam still cares about the same things the following week.

No transfer logic, no inheritance rules.

---

## The open question: knowledge after death

Sam knows what Z learned. Z's replacement does not.

The player view has to pick:

| | Faithful | Practical |
|---|---|---|
| **Split** — the new character sees only what they've witnessed | Yes | More work; also possibly annoying, since the player already knows |
| **Merged** — the player sees everything they've ever learned | No | Simple; quietly makes every death less costly |

Most tables handle this loosely by convention, and the GM adjudicates. A tool has to choose a default.

Worth noting the stake: if knowledge merges automatically, death loses part of its bite — the party keeps everything except a sheet. If it splits, the tool is enforcing something the table may prefer to handle by trust.

Probably: merge by default, since the tool's job is recall support rather than rules enforcement (see [[Scope]]), and let the GM handle in-character ignorance the way tables always have.

---

## Also open

**What happens when a player leaves the campaign?**
Their characters keep their state. Their notes remain theirs. Whether their record stays visible to the others is a question about the table, not the data.
