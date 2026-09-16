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

**This is also where canon lands**, per [[Canon]]: material authored independently of any one campaign belongs to the setting, because that is what *independent of any one campaign* means structurally. Campaign material — including a published campaign book — belongs to the campaign it was written for.

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

**Facts belong to the campaign that produced them**, and carry a position in fiction time.

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

A finished campaign's facts reach the next GM exactly as published setting fiction does: **immutable, revealed on the new GM's timing, and supersedable if their table changes an outcome.**

That is the Canon mechanism in [[Glossary]] and [[Canon]], and no new concept is required.

### Why, precisely — and it is not about the author

An earlier version of this section said a prior campaign's facts are canon because they were *authored by someone else*, and treated a previous campaign as a third value of **Provenance** alongside the GM and an external author.

**That reasoning is wrong, and the same-GM sequel is what exposes it.** A GM running a second campaign in their own setting wrote the first campaign's facts themselves. There is no other author anywhere. The facts are still canon to the new campaign.

The criterion in [[Canon]] is **what the authoring was for**, and it is relative to the campaign asking:

> The first campaign's facts were authored for *that* campaign. Relative to the second, they exist independently — which is exactly what makes them canon.

So this is one mechanism seen from a new angle, not a special case. Provenance still records who asserted each fact and when, and a previous campaign is a legitimate thing for it to name. It is simply not what makes those facts canon.

**The practical consequence is the useful part.** Facts the GM authored freely during the first campaign become immutable to them during the second — not because someone else owns them, but because that story is finished. Changing one is supersession, with the original preserved. That is a real constraint a GM should feel, and it would have been invisible under an author-based rule.

Supersession covers the case where the new table changes something the first campaign established — the earlier fact stays exactly as recorded, and the new one carries a `supersedes` relationship to it.

**And the reach model already covers the companion case.** A first-party action with floor-wide effects reaches a second party elsewhere in the world as an off-screen event, felt without being witnessed. This is the Emberus pattern from [[Canon]] with both roles filled by campaigns rather than by a book.

---

## Player foreknowledge is out of scope

In a sequel, the second party's *players* may remember everything from the first campaign, even though their characters know none of it.

**This is not modelled, and should not be.** The record tracks what has been revealed in this campaign. What the humans remember from having played is outside the system — the same boundary drawn in [[Glossary]] for the players' own conversation about a session.

It is still a real thing for a GM to plan around, and it is the same question [[Canon]] already holds open about a player who has read the source books: the character does not know, the person does, and the GM is working with dramatic irony rather than mystery. **One answer covers both**, and it likely takes the form of a note about a person in a campaign, not a state on a fact.

---

## Setting creation happens through planning

**No separate authoring surface.** Creating setting-level material — entities, and in time facts about them — is a version of the same [[Planning-Loop]] a GM already runs for campaign prep. There is no "author a setting" mode distinct from ordinary planning; scope is the only thing that varies, and that falls out of the tiers already established above.

**Campaign creation offers linking to an existing setting or starting a new one.** A single fork at one screen, not a new subsystem — see §Consequences below.

---

## One campaign is live at a time — the RC 1a–1d assumption

**Assumed for the near term, and it is what keeps all of the above simple.** A GM runs one campaign, finishes it, and starts another in the same setting. Campaigns are sequential in real time even when their in-world positions are not.

That gives one-directional fact flow — earlier to later, never back — and removes concurrent writes, merges, and conflict resolution entirely, for as long as it holds.

~~**Simultaneous live campaigns in one setting is a real capability and a deliberate non-goal for now.**~~ **Superseded.** Both "one GM running several tables" and "several GMs sharing one setting" are valid product shapes, and nothing in the product should structurally prevent either. The original reasoning was right that this is a retail-grade capability with real cost, and wrong to file it as a maybe — it is a real target. The merge problem this assertion was holding off does need an answer, on the timeline in §Setting ownership below, not never.

**What doesn't change:** every mechanism above is written against one campaign per setting, and stays that way until a release actually puts two campaigns in one setting. This section is now a statement about *when* the assumption gives way, not *whether* it does.

---

## Setting ownership

**Long-term objective, not a near-term build.** Recorded per [[Roadmap]]'s strategic-vision pattern — no epics, no dates — so RC 1a–1d choices don't quietly foreclose it.

Two shapes a shared setting takes, needing different governance:

| Pattern | Who can write setting canon | Example |
|---|---|---|
| **Co-owned** | All participating GMs, jointly and directly | West Marches — several GMs run tables in one world by mutual agreement, each authoring canon as they go |
| **Owner-gated** | One Setting Owner; other GMs write only to their own campaign | A setting one GM built, that others run tables in without a hand in shaping it |

**Co-owned likely reduces to the owner-gated case with the role held jointly** — no separate mechanism, just Setting Owner assignable to more than one person. Worth confirming before either is built.

### Setting Owner is a role above campaign GM

Nothing in the model today has an actor above "campaign GM." [[Canon]]'s criterion — canon is what the authoring was *for*, not who authored it — already answers *what* counts as setting canon. It doesn't answer *who* decides when two campaigns' GMs both produce something setting-level, or when neither has standing to declare setting truth alone. Setting Owner is that missing role.

### Campaign-local creation and promotion

In the owner-gated pattern, a campaign GM's entities and events are authored on top of existing canon, inside their own campaign, without write access to the setting tier. The Setting Owner may later pull a campaign's creation into setting canon — this is the existing Canon mechanism in [[Canon]], not a new one. What's new is that the pull is performed by someone other than the authoring GM, across a campaign boundary, which nothing in the model currently has an actor for.

**The local GM controls whether their creative product is even exposed for that consideration** — promotion is opt-in from the origin campaign's side before it is opt-in from the Setting Owner's.

### Planned-event visibility is the coordination mechanism, and needs nothing new

The concrete collision case: GM A plans a future event in Campaign A, touching a setting-scoped entity. GM B, running Campaign B in the same setting, should see that the entity has something reserved against it — clearly marked, unresolved — without being able to use or resolve it themselves until GM A's event becomes `fact` (including by being marked as occurring off-screen, per [[Off-Screen-Events]]).

**This rides entirely on the existing `planned` → `pending` → `fact` event states** in [[Off-Screen-Events]]. It is [[Visibility-Model]]'s "marked not filtered" principle one scope up: there it governs what the GM sees of a fact the players don't; here it governs what one campaign's GM sees of another campaign's reservation on a shared entity, in the same visible-but-not-actionable shape.

### Open

- Does revealing a relationship fact require both connected entities to already be materialized? Likely already answered by [[Visibility-Model]]'s hidden-relationships principle — worth confirming it reads that way rather than treating as new.
- Entity schema — what object types exist and how government attaches to a place — is open, and tracked in [[Open-Requirements]], not here.

---

## Consequences for the near-term backlog

**Added as thin structure, not features:**

- A setting tier exists, holding exactly one setting, invisible in the interface.
- Identifiers are unique within a setting.
- Visibility is held per fact per campaign, even while there is only one campaign to hold it for.
- Campaign creation offers linking to an existing setting or creating a new one — a single fork at one screen, even though "new" is the only branch ever taken until a second setting exists.
- Every entity records which campaign originated it. Facts already carry this (see §What carries, and what does not); entities didn't need it while there was one campaign per setting, but a future Setting Owner (see §Setting ownership) cannot promote a campaign's creation into canon without knowing whose it was, and that attribution can't be reconstructed after the fact.

**Explicitly not now:** seeding a second campaign, cross-campaign time comparison, cross-campaign queries, promotion into canon, Setting Owner as an enforced role, or any interface acknowledging that settings exist.

**The reasoning is the same as the campaign container's.** Optionality is cheap; capability is expensive. The items above cost almost nothing while there is one campaign, and the visibility field and the entity origin field are both unrecoverable if deferred — neither can be split or backfilled later without guessing, on exactly the axis where guessing wrong is a spoiler or an attribution dispute.

---

## Open questions

| Question | What it blocks | Where it sits |
|---|---|---|
| ~~Does a fact need an explicit setting-time position?~~ | — | **Resolved: setting-time is fiction time**, not a third clock. See [[Information-Architecture]]. The calendar is the GM's own or absent entirely — a published setting usually supplies a reckoning, a homebrew one often does not, and imposing one would repeat the fixed-place-tiers mistake |
| Can fiction times be compared across two campaigns? | Seeding a prequel or companion campaign | Needs a shared calendar or an explicit offset. Only matters at the second campaign, and **not unrecoverable** — fiction time is captured either way, so a calendar can be layered on later without re-reading anything |
| When a second campaign writes a fact about a shared entity, does it belong to the setting or stay in the campaign? | Seeding a third campaign | Deferrable. With sequential campaigns the distinction only matters at the third. Note [[Canon]]'s criterion answers it in principle: a fact authored during play belongs to the campaign that produced it, however durable it looks. **§Setting ownership's promotion is the deliberate override of this default** — the same question, for the shared-setting case |
| Is the GM of a later campaign the same person? | Nothing in R1 | If not, the person-holds-role-per-campaign shape in [[Strategy-Multi-Campaign-and-Convergence]] already covers it. Note the answer does **not** affect whether the first campaign's facts are canon to the second — see above |
| Is co-owned Setting Owner really the owner-gated pattern with the role held jointly, or does it need its own mechanism? | Setting Owner design, whenever it's built | Open — see §Setting ownership |
| What object types make up the entity schema (geopolitical entity, settlement, government, office vs. officeholder)? | Any epic touching place or government | Open, tracked in [[Open-Requirements]] |
