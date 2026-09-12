---
type: design
status: draft
visibility: gm
tags: [constraint, north-star, interface, table, principle]
---

# Constraint — The Tool Serves the Table

A hard rule, not a preference. Companion to [[Constraint-Manner-and-Intent]].

> **The tool serves the table. It never joins it.**
>
> This product exists to make human-to-human interaction at the table better. Any capability that competes with that interaction is wrong, however useful the thing it produces.

---

## Why this is a constraint and not a value

It was arrived at three separate times, from three different directions, before being recognised as one rule:

- **Player notes** were deliberately shaped to happen after the session, not during it, because players focused on capture instead of on each other is the failure. See [[Live-Set]].
- **The [[Live-Set]]** is a cap rather than a firehose, because the scarce resource is what the GM can hold while talking.
- **Options, not recommendations** is non-negotiable, because a tool that ranks story quality takes the authorship away from the person.

Three independent derivations of the same principle. Writing it down once means the rest of the design can point here rather than re-deriving it, and means the next decision of this kind is settled in advance rather than re-litigated.

---

## The rules it generates

Stated so they are testable rather than aspirational.

### Nothing at the table demands attention

Every table surface is **pull-only**. No notification, no badge count, no prompt, no unread state, no suggestion arriving unasked. The GM and the players glance when they choose to; the tool never asks to be looked at.

This is why inference is confined to the between-session modes in [[Modes-and-Surfaces]] — not only because batch computation is cheaper there, but because a surfaced insight is an interruption by construction.

### A write must fit inside a pause that would happen anyway

The bar is not *quick*. It is that the act fits inside a beat the conversation already has — dice being rolled, a rules lookup, someone getting a drink.

Anything that requires holding up the scene fails, **regardless of how valuable the captured detail would have been.**

### No player-facing write at the table. Unconditional.

Not *initially*, not *pending a better interaction model*. A GM glancing at their own screen is already part of the social contract of running a game. A player typing is withdrawal from the conversation, and three players each doing it occasionally is a table that has stopped talking to each other.

Player-authored content happens away from the table. See [[Player-Scope]].

### The tool never produces content the humans would otherwise produce

Already the rule in [[Constraint-Manner-and-Intent]]. **This document supplies the deeper reason.** The objection to a generated emotional read is not primarily that it would be inaccurate — it is that generating the interpretation takes the interpretation away from the people whose interpretation it was.

---

## The consequence that inverts a previous bias

> **A captured detail is worth less than the moment it costs.**

[[North-Star]] names **the lost detail** as the failure mode. That framing, taken alone, argues for making capture ever easier, ever more present, ever closer to the moment — which leads directly to a tool sitting between the people at the table.

This constraint caps it. **A detail lost to protecting the conversation is not a failure. It is the correct trade.**

The two are not in conflict once ordered: the tool should make retrieval and capture as frictionless as possible *within* the space that does not compete with the conversation, and should decline to expand beyond it.

---

## What this settles

**The mid-session write path.** [[Modes-and-Surfaces]] and [[Update-Cadence]] both left it open with the note *probably allow, nothing should depend on it.*

Now settled, and for a better reason. Table play has **no write path initially**. A future write capability is permitted, but only subject to the pause rule above. Nothing may depend on it — **because the tool must always be free to choose the table over the record**, and a feature nothing depends on can lose that contest gracefully.

---

## How to apply it

When a proposed capability is in question, the test is not *is this useful* — most of them are. The test is:

1. Does it demand attention, or wait to be asked?
2. Does it fit in a pause the conversation already has?
3. Does it produce something the people at the table would otherwise have produced themselves?
4. If it and the conversation compete, can it lose without breaking anything?

A capability that fails (1), (2) or (3) does not belong at the table. A capability that fails (4) does not belong at the table **yet**, no matter how well it does on the others.
