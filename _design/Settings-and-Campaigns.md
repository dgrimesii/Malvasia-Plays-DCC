---
type: design
status: draft
visibility: gm
tags: [setting, campaign, multi-campaign, model, strategy]
---

# Settings and Campaigns

A setting is a world. A campaign is a story told in it. Most GMs will only ever have one of each, and should never have to think about the distinction.

This document exists because a GM who runs a second campaign in a world their group liked should inherit the work rather than start again — and because the structure that allows it is nearly free now and a migration later.

Companion to [[Strategy-Multi-Campaign-and-Convergence]], which covers the campaign container itself.

---

## The shape

```
Setting ──contains──> Campaign ──contains──> the story as played
```

**The setting holds what is durable.** People, places, factions, objects — the things that exist in the world regardless of who is adventuring through it.

**The campaign holds what happened.** Facts, sessions, reveals, arcs, investment — one party's passage through that world.

Both tiers exist from day one, holding exactly one of each. **The setting is invisible until a second campaign is created.** A GM who never runs one never encounters the concept, and no interface should introduce it to them.

---

## The motivating case

A group finishes a campaign and likes the world. The GM wants to run another in it — a different party, a different story, the same places and people.

Three shapes this takes, in literary terms:

| Mode | When it starts | What the new party inherits |
|---|---|---|
| **Sequel** | After the first campaign | The world as the first party left it |
| **Companion** | Alongside the first campaign | The same world, mostly untouched by events they were not present for |
| **Prequel** | Before the first campaign | The world before any of it happened |

**These are not three mechanisms.** They are one operation with a parameter: where in the setting's own timeline the new campaign begins. Seeding means *give me this setting's entities, with whatever facts are true as of my starting position.*

That falls out of something the model already has. Entities are stable; facts are anchored in time. A prequel finds few facts because few have happened yet. A sequel finds all of them.

---

## What carries, and what does not

**Entities carry.** The innkeeper is the same innkeeper — one identity, one record, referenced by both campaigns. Seeding is by **reference, not copy**. Duplicating the setting would make the two campaigns diverge immediately and destroy the thing that made inheriting worthwhile.

**Facts belong to the campaign that produced them**, and carry a position in setting-time.

**Visibility does not carry at all.** This is the consequential one — see below.

**Arcs and investment do not carry.** Both are properties of a particular group of people at a particular table. A thread the first party cared about means nothing to the second until they form their own.

---

## Identity is scoped to the setting

**Identifiers are unique within a setting, not within a campaign.** If the second campaign meets the same innkeeper, that must be the same entity — one identity, one accumulated record — or there is no inheritance at all, only a copied starting position.

This corrects an earlier statement in [[Strategy-Multi-Campaign-and-Convergence]], which scoped identifiers to the campaign. Campaign scope is right for *facts* and wrong for *entities*.

Cheap to adopt now; a data migration once identifiers exist at the wrong scope.

---

## Visibility is per fact, per campaign

Today [[Visibility-Model]] holds `gm` or `player` against each fact. With a second campaign that breaks: the same fact is known to one party and not the other.

**Visibility becomes a value per fact per campaign.** A fact revealed in the first campaign is GM-only in the second until that GM reveals it again.

**This is the expensive-if-deferred decision in this document.** Every fact written under a single-value visibility model has no campaign attached to that value, and retrofitting one means guessing — on exactly the axis where guessing wrong spoils a campaign silently and unrecoverably.

Note what this is not. It is not per-*player* visibility. [[Players-and-Characters]] settles that the party knows things collectively, and that holds unchanged within each campaign.

---

## Prior campaigns are canon to later ones

A finished campaign's facts reach the next GM exactly as published source material does: **authored by someone else, immutable, revealed on the new GM's timing, and supersedable if their table changes an outcome.**

That is the Canon mechanism in [[Glossary]] and [[Canon]], with a different author. No new concept is required. Provenance already distinguishes the GM, a player, and an external author; a previous campaign is the third of these.

Supersession also already covers the case where the new table changes something the first campaign established — the earlier fact stays exactly as recorded, and the new one carries a `supersedes` relationship to it.

**And the reach model already covers the companion case.** A first-party action with floor-wide effects reaches a second party elsewhere in the world as an off-screen event, felt without being witnessed. This is the Emberus pattern from [[Canon]] with both roles filled by campaigns rather than by a book.

---

## Player foreknowledge is out of scope

In a sequel, the second party's *players* may remember everything from the first campaign, even though their characters know none of it.

**This is not modelled, and should not be.** The record tracks what has been revealed in this campaign. What the humans remember from having played is outside the system — the same boundary drawn in [[Glossary]] for the players' own conversation about a session.

It is still a real thing for a GM to plan around, and it is the same question [[Canon]] already holds open about a player who has read the source books: the character does not know, the person does, and the GM is working with dramatic irony rather than mystery. **One answer covers both**, and it likely takes the form of a note about a person in a campaign, not a state on a fact.

---

## One campaign is live at a time

**Assumed, and it is what keeps all of the above simple.** A GM runs one campaign, finishes it, and starts another in the same setting. Campaigns are sequential in real time even when their in-world positions are not.

That gives one-directional fact flow — earlier to later, never back — and removes concurrent writes, merges, and conflict resolution entirely.

**Simultaneous live campaigns in one setting is a real capability and a deliberate non-goal for now.** It belongs to a retail-grade product, and it is recorded in [[Roadmap]] as strategic vision rather than a planned epic. If it is ever built, the merge problem returns in full, and this assertion is the line where it does.

---

## Consequences for the near-term backlog

**Added as thin structure, not features:**

- A setting tier exists, holding exactly one setting, invisible in the interface.
- Identifiers are unique within a setting.
- Visibility is held per fact per campaign, even while there is only one campaign to hold it for.

**Explicitly not now:** seeding a second campaign, setting-time positioning, cross-campaign queries, or any interface acknowledging that settings exist.

**The reasoning is the same as the campaign container's.** Optionality is cheap; capability is expensive. The three items above cost almost nothing while there is one campaign, and the third in particular is unrecoverable if deferred — a single-valued visibility field cannot be split later without guessing which campaign each value belonged to.

---

## Open questions

| Question | What it blocks | Where it sits |
|---|---|---|
| Does a fact need an explicit setting-time position, or is the session date enough? | Seeding a prequel or companion campaign | Nothing now. Session date is sufficient while one campaign exists, but in-world and real-world time diverge as soon as a second one starts earlier |
| When a second campaign writes a fact about a shared entity, does it belong to the setting or stay in the campaign? | Seeding a third campaign | Deferrable. With sequential campaigns the distinction only matters at the third |
| Is the GM of a later campaign the same person? | Nothing in R1 | If not, the person-holds-role-per-campaign shape in [[Strategy-Multi-Campaign-and-Convergence]] already covers it |
