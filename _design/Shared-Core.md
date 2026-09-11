---
type: design
status: draft
visibility: gm
tags: [strategy, convergence, chronicle, model, shared-core]
---

# The Shared Core

What the two tools would actually have in common, derived from Chronicle's stated objectives. Companion to [[Strategy-Multi-Campaign-and-Convergence]].

---

## Chronicle's two objectives

1. **Track the relationships between people, places, and events as they emerge through play.**
2. **Create a detailed record of what the players actually did at the table** — abilities used, round-by-round combat — grounded against the game rules.

These split cleanly, and the split is the answer to what can be shared.

---

## Objective 1 is this tool's objective

Not merely compatible — **the same objective, observed from two vantages.**

| | Chronicle | This tool |
|---|---|---|
| Vantage | The table, as the party experienced it | Behind the screen |
| Relationships are | Discovered as they emerge | Discovered as they emerge, **and** planned |
| Recorded by | The scribe | The GM |

Both track people, places, and events and the connections between them. Both treat those connections as *emerging* rather than authored up front — which is exactly the claim [[Information-Architecture]] makes about arcs, and the reason the graph model exists here at all.

**Two independent systems, two game systems, two authoring roles, and the same core model.** That is about as strong a signal as this kind of thing produces.

---

## Objective 2 is precisely what [[Scope]] excludes

Abilities used, round-by-round combat, results grounded against the rules. This tool's scope document rules out stats, rules enforcement, rules lookup, and combat resolution by name.

And *"grounded against the game rules"* is the part that can never be shared. It requires a model of what actions exist, what results are valid, what a character can do — which is why Chronicle harvests ability lists from D&D Beyond. That is bound to 5e in a way nothing lifts out of.

---

## Why objective 2 can't be shared by renaming fields

The tempting cheap answer is one combat schema with per-system field names. It fails, and the reason is structural rather than a matter of vocabulary.

Chronicle's combat record encodes 5e's turn structure directly: `slots[{s, a, act, res, val}]` where `s` is a slot number 1–6, plus a separate `enemy_turns[]`. **Ordinal position carries meaning** — the schema assumes a round is an ordered sequence of turns, that each participant acts once at a known point, and that what came before is known when you act.

Those are real assumptions about how a game works, and systems differ on every one of them. Some resolve simultaneously rather than in sequence. Some separate what you commit to from when it resolves. Some let one action preempt or cancel another, which is a *relation between two actions* rather than a position in a sequence. A system making any of those choices does not fit a slot list, whatever the fields are called, and forcing it in loses information in both directions.

That is enough to settle the boundary. Establishing it does not require cataloguing how any particular system resolves a round — and this tool deliberately holds no such model, which is the point of the scope exclusion. What matters is only that the assumptions are not universal.

### The consequence for the boundary

**The shared core stops at the event.** It knows that a combat happened, where, who was involved, and how it came out. It does not know how a round works.

Everything below that line is a **system-specific payload** the core does not interpret — opaque to it, owned by whatever tool handles that game system. A play-record tool for any other system, if one were ever wanted, would be a *sibling* of Chronicle sharing the core, not a feature of this tool.

That is a cheap boundary to hold, and it is the thing convergence actually needs: a stable contract at the event, and no assumptions about what is underneath it.

### Narratively weighted mechanical moments still belong here

[[Scope]] draws the line at narrative weight: *"the use of a capability at a significant moment is narrative. The capability's numbers are not."*

Every system produces moments of that kind, and which moments carry weight is shaped by its structure — a system where you commit before knowing what others will do generates misfires and accidental rescues; one where an action can be spent to preempt another generates choices under pressure with a real cost. Those are character, not bookkeeping.

*"Hilda spent her action to stop the Warden's order"* is a portable narrative fact and worth capturing here. The resolution mechanics beneath it are not, and are not wanted.

**System structure shapes which moments carry weight. Capturing those moments does not require capturing the structure** — which is fortunate, because capturing the structure is exactly what the core cannot portably do.

---

## What the shared core is

Entities, typed relationships between them, and events — **as observed.**

That is the whole substrate. Everything else in either tool sits on top of it, as a context layer over shared things rather than a competing model of them:

| Layer | Chronicle | This tool |
|---|---|---|
| **Shared core** | People, places, events, relationships, sessions | Same |
| Adds | Rules-grounded play detail — combat rounds, actions, results | Planning and speculation, visibility and revelation, investment, arcs |

This supersedes an earlier framing in which the seam ran through Chronicle's own `mechanics` / `narrative` two-layer split on each entity. That split is a reasonable first read and points in the right direction, but the sharper cut is one shared entity core with a context layer per tool — see [[Strategy-Multi-Campaign-and-Convergence]]. Both tools describe the same people, places, events, quests, and objects; each attaches its own point of view to them.

### One difference worth naming precisely

**Chronicle only ever writes facts.** It records what happened, after it happened. Nothing in it is provisional.

This tool writes facts *and* things that have not happened — projections, speculative events, planned encounters, arc intent. [[Off-Screen-Events]] already gives the state model for this: `planned` versus `fact`, with authoring effort tracked separately on the `speculative / potential / used` ladder.

That means the substrate already accommodates both tools without modification. Chronicle simply never uses one of the states. **A shared core does not require Chronicle to grow a notion of speculation, and does not require this tool to give one up.**

---

## Detail level is a table-level variable

The scribe's depth of capture depends on that group's appetite for note-taking. This is not a product decision; it is a property of each table, and it varies.

Three consequences.

### Sparse capture must be correct, not incomplete

[[Session-Capture]] already holds this position for manner: *"blank columns are correct, not incomplete."* The same principle extends to the mechanical layer, on a different axis — a table that records little detail has produced an accurate record of a table that records little detail.

A system that treats depth as a completeness target will make every low-appetite group's record look like unfinished work, which is the reliable way to make them stop maintaining it.

### Gaps have two causes, and the difference is not inferable

**"Nobody wrote it down"** and **"it is missing"** look identical in the data. Only the person who was there can tell them apart.

Chronicle has already met this problem and solved it the right way: the integrity checker surfaces a gap, and the scribe must explicitly **Accept**, **Defer**, or **Edit** it. The decision is recorded rather than assumed, and publishing is blocked until every gap has one.

That pattern is directly reusable here, and it is the same shape as intake's review stage in [[Session-Capture]] — the system proposes, the human decides, nothing is assumed silently. It applies to the readiness and coverage checks in [[GM-Considerations]] for the same reason: a coverage claim that cannot distinguish "deliberately thin" from "overlooked" is not trustworthy.

### Appetite is per-campaign configuration

Another argument for the campaign container in [[Strategy-Multi-Campaign-and-Convergence]] being more than a namespace. What a campaign expects to capture, and how deeply, belongs to the campaign — not to the tool and not to the person.

Cheap to allow for. Awkward to add once anything reads a global setting.

---

## Consequences for the backlog

- **The shared core is entities, typed relationships, events — observed.** Anything proposed as "core" that does not fit that description is not core.
- **The core boundary is the event.** Mechanical detail below it is a system-specific payload the core does not interpret.
- **Narratively weighted mechanical moments are captured as narrative facts**, without the mechanical structure that produced them. A capability used at a hinge point, a commitment that misfired, an action spent to stop someone else's.
- **The planned/fact distinction stays**, and costs convergence nothing.
- **Coverage and integrity checks must record an explicit human decision on each gap**, rather than assuming absence means incompleteness. Reuse Chronicle's Accept / Defer / Edit shape.
- **The campaign container carries configuration**, including expected capture depth.
- **Sparse records are valid records.** This belongs in acceptance criteria wherever completeness is checked, not only in the capture epic.
- **The compatibility note** in [[Strategy-Multi-Campaign-and-Convergence]] maps objective-1 concepts only. Objective 2 is explicitly out of mapping scope.
