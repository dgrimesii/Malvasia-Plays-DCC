---
type: reference
status: draft
visibility: gm
tags: [templates, conventions, capture]
---

# Template Conventions

How to fill these in, and why the fields are shaped this way.

These conventions apply the model invariants listed in [[Sequencing]]. **Sessions captured this way need no migration when the tool arrives.** Sessions captured flat will have to be re-encoded by hand — see [[Release-Plan]].

---

## The five rules

### 1. `visibility` is `gm` or `player`

Only two values. The old `player-ro` / `player-rw` split conflated knowing something with being able to edit it; authorship is tracked by who wrote a thing, not by a visibility flag. See [[Players-and-Characters]].

The file-level flag is a **default for the file**, not the mechanism. Individual facts, names, and relationships carry their own — that is what the `Known to party` columns are for.

### 2. Identity is the `id`, never the name

Every entity gets a short identifier: a type prefix plus four random characters — `npc-a7k2`, `zon-m3vp`, `fac-q81r`.

- **Not sequential.** Sequential identifiers leak: a visible `npc-007` and `npc-009` proves `npc-008` exists. See [[Visibility-Model]].
- **Not derived from the name.** Names change, get revealed, and get merged. The identifier does not.
- **Unique within this campaign.** Not assumed unique across campaigns.

When two records turn out to be the same thing, one identifier survives and the other becomes an alias of it. Nothing is deleted.

### 3. A name is a fact, not a header

An entity can appear at the table without its name being known, and can give a false one. So names live in a table with the same two properties every fact has — whether the party knows it, and whether it is true.

| Name | Known to party | True | Source |
|---|---|---|---|
| the Toll Warden | yes | yes | title the party heard used |
| Marek | yes | **no** | he told them this in S3 |
| Kelvin Sorr | no | yes | real name |

**A name the party was given is recorded as something they were told.** Never write a false name as *the* name — the player view would render it as a world fact and silently assert the lie. See [[Names-and-Aliases]].

A gated name is simply absent from the player's view. Never shown as blank or redacted, because the redaction is the reveal.

### 4. Facts carry their source

Every fact says where it came from. The distinction that matters:

| Write this | Not this |
|---|---|
| The Warden told the party the tunnels flood at night | The tunnels flood at night |

The first is permanently true and stays true even when the claim turns out to be a lie. The second asserts a world fact in the record's own voice, and the moment a player reads it, every deception in the campaign is spoiled.

Whether the claim is *true* is a separate GM-only column. It can be set later — deciding retroactively that something was a lie is authorship, not a correction. See [[Facts-and-Revelation]].

### 5. Blank is correct

Most manner columns are empty. Most sessions have no notable roleplaying behaviour. An empty table is a valid record of a session where nothing of that kind happened.

A gap in the record has two causes — *nobody wrote it down* and *it is missing* — and they look identical. Only the person who was there can tell them apart, so the record never infers one from the other.

---

## Materialization

An entity **materializes** when it appears at the table. `materialized:` holds the session it first appeared in; blank means it has not.

After that, its existence is permanently public. Its name, its facts, and its relationships remain individually gated.

**The case this protects:** the party has met someone who, in your plan, is connected to something that has not appeared. Both the connection and the far thing stay hidden — which is why relationships carry their own `Known to party`, independent of either end.

---

## Naming drift, and how to avoid it

The party will call things whatever they called them at the table. If the official name reaches them promptly after the session, they adopt it. If it does not, their name sticks.

That is why `Names the party used` is in the session template. Capture it while you remember, then either reveal the official name or **adopt theirs as an alias** — a name a player coins becoming a world fact is the goal, not a problem. See [[North-Star]].

---

## Planned is not the same as happened

Two different things, often confused:

- **State** — `planned` or `fact`. Did it happen? Deciding something is inevitable does not make it a fact.
- **Effort** — `speculative` → `potential` → `used`. How much work has gone into it.

A `potential` encounter is fully written and has not happened. A `speculative` one is a possibility being held, costing almost nothing. See [[Off-Screen-Events]].

---

## Pending

`arc:` on Zone and `zones: []` on Arc are hand-maintained inverse links that will drift. [[Information-Architecture]] argues they should be derived rather than stored, but adopting that model is an open decision — see [[Backlog-Readiness]] §G2. **Left in place deliberately** rather than pre-empting it.

The body of `Template-Arc.md` is likewise unchanged pending that decision. [[Arcs]] specifies what should replace the Stages table; no arcs exist yet, so the change stays cheap either way.
