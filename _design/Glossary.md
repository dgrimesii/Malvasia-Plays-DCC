---
type: reference
status: draft
visibility: gm
tags: [glossary, vocabulary, reference]
---

# Glossary

Written for a reader who has never played a tabletop roleplaying game. Prerequisite **P1** in [[Roadmap]].

Every domain term used in an epic points here. If a term is missing, it either needs adding or should not be in the epic.

**Markings**

- **[game]** — true of tabletop roleplaying generally
- **[system]** — specific to Dungeon Crawler Carl, the rules this campaign uses. Would not carry over to another game system.
- **[campaign]** — specific to this campaign
- **[model]** — how Storyteller represents things
- **[process]** — how the work is done

---

## Part 1 — The game

**Tabletop roleplaying game** *[game]* — A group of people telling a story together. One person describes a situation; the others say what their characters do; dice and rules settle what happens. Nothing is on a screen and nothing is pre-written past the next few hours of play.

**Game master**, GM *[game]* — The person who prepares the world, describes it, plays everyone in it who is not a player character, and decides what happens when the rules do not say. Called a DM in some systems, including Chronicle's.

**Player** *[game]* — Someone who plays one character. Three in this campaign.

**Player character**, PC *[game]* — The character a player controls. Theirs, not the GM's.

**Party** *[game]* — The player characters together. *"What the party knows"* means what all of them collectively know, which in this design is a single shared thing rather than three separate ones.

**Table** *[game]* — The group and the occasion. *"At the table"* means during live play, with everyone present — as opposed to preparation beforehand or writing up afterward.

**In-fiction and table-level** *[game]* — Two different layers. In-fiction: a character picks a lock. Table-level: a player leans in and asks a question about a locked door. Both are worth recording, and they mean different things.

**Session** *[game]* — One sitting of play, a few hours long. This group plays roughly weekly. The unit almost everything is organised around.

**NPC**, non-player character *[game]* — Anyone in the world the GM plays. A shopkeeper, a rival, a monster with something to say.

**Faction** *[game]* — An organised group with its own goals. A guild, a cult, a garrison.

**Encounter** *[game]* — A discrete situation the party meets: a fight, a negotiation, a locked vault. Prepared in advance or improvised.

**Loot** *[game]* — What the party gains from play. Objects, money, favours.

**Dungeon crawl** *[game]* — A structure where the party explores a dangerous place room by room, level by level. This campaign is one.

**Dungeon Crawler Carl**, DCC *[system]* — The rules this campaign uses: a licensed tabletop adaptation of Matt Dinniman's litRPG novel series, published by Renegade Game Studios. Storyteller is deliberately system-agnostic — mechanics stay in the rulebook, not here, and this holds regardless of which system a given campaign runs. What gets recorded is the story a session produces: people, places, events, arcs, connections. Not dice, not stats, not turn structure.

**Dossier** *[campaign]* — The sheet each player filled in when making their character: background, motivations, ties. Written openly, in person, before play began. A standing source of hooks.

**Floor** *[campaign]* — A level of the structure the campaign takes place in, explored in order. Floor 1 is the beginning; Floor 6 is when a wider world begins to press in.

**Zone** *[campaign]* — A distinct area within a floor. Where encounters happen and NPCs are found.

---

## Part 2 — Things that are commonly confused

Four pairs that appear across the design documents and mean different things.

**Quest vs Arc**

A **quest** *[model]* is a task with a stated goal and a finish. *Recover the thing. Deliver the message.* The GM authors it, and it either completes or fails.

An **arc** *[model]* is a thread of meaning running through the campaign that the group cares about. It cannot be authored — a GM can only notice one forming and then support it. A quest can belong to an arc; an arc is never just a quest.

A quest's lifecycle crosses the Storyteller/Chronicle seam like any other entity's. Before **Reveal**, its state belongs entirely to Storyteller — `planned`/`fact`, `speculative → potential → used` effort — the GM's own planning, invisible to the party. At Reveal it becomes known, and everything after belongs to the party's experience of it: given, in-progress, completed, failed, abandoned. Storyteller doesn't track that half; Chronicle does. The two state machines never overlap — they meet at exactly one point.

**Encounter vs Event**

An **encounter** *[game]* is a prepared or improvised situation the party meets.

An **event** *[model]* is a thing that happened, or is planned to happen, recorded in the store. Encounters produce events; so do conversations, discoveries, and things happening elsewhere that the party never sees.

**Manner vs what happened**

**What happened** *[model]* is factual: she asked about the tunnels.

**Manner** *[model]* is how: warily, or delighted, or as though she already knew. It is the GM's read of a real moment. **Storyteller never generates it** — an invented emotional read is a false memory of a real person's behaviour. Blank is the normal state.

**Planned vs Fact, and how much work went in**

**State** *[model]* is `planned` or `fact` — has this happened. Deciding something is inevitable does not make it a fact.

**Effort** *[model]* is `speculative` → `potential` → `used` — how much writing has gone into it. A `potential` encounter is fully written and has not happened; a `speculative` one is a possibility being held cheaply.

---

## Part 3 — The model

**Entity** *[model]* — A thing in the world with its own identity: a person, a place, a group, an object. Everything else attaches to one.

**Identifier** *[model]* — What an entity actually *is*, in the record. A short code like `npc-a7k2`. Deliberately not the name, because names change, get revealed, and get merged. Deliberately not sequential, because a visible `npc-007` and `npc-009` would prove `npc-008` exists.

**Name** *[model]* — A fact about an entity, not a header. An entity can have several at once: a title everyone uses, a false one it gave the party, and a real one nobody knows. Each carries who knows it and whether it is true.

**Alias** *[model]* — Another name for the same entity. Includes names the party invented. A player's coinage surviving in the record is a goal, not a tolerance.

**Fact** *[model]* — Something recorded about an entity. Carries its source, who knows it, and whether it is true.

**Utterance, claim, belief** *[model]* — Three different things that look alike.

- **Utterance**: he told the party the tunnels flood at night. Permanently true — he said it.
- **Claim**: the tunnels flood at night. May be false.
- **Belief**: the party thinks the tunnels flood at night.

Recording an utterance as a claim is the single most consequential mistake available in capture. It puts a lie in the record's own voice, and the moment a player reads it, the deception is spoiled.

**Relationship** *[model]* — A connection between two entities, with a direction and a type. Carries its own visibility: the party can know two things exist without knowing they are connected.

**Provenance** *[model]* — Who asserted something, from which side of the screen, and when.

**Attribution** *[model]* — Whose contribution a piece of content is. A player note is theirs and stays theirs. Attribution is a name on a note, not a permission.

**Visibility** *[model]* — Whether the party knows a thing. Two values: `gm` and `player`. Applies to facts and relationships individually, not just to whole entities.

**Materialize** *[model]* — An entity materializes when the party learns it exists — whether by meeting it directly or simply being told about it. After that its existence is permanently public, though its name and facts stay individually gated. One-way; nothing un-materializes. A dead or destroyed entity that never materialized needs no separate status: it is simply a Fact (dead) on an entity that has not materialized — both already tracked, so nothing new is needed to ask what is known only indirectly, if at all. *Considered and declined:* a distinct "foreclosed" or "indirect-only" state, since it would duplicate what Fact and Materialize already express and could drift out of sync with them.

**Reveal** *[model]* — The GM deliberately making something visible to the party. Not a switch on an entity — a chosen set of existences, names, facts, and connections. Recorded as an event, so what is new can be shown later.

**Canon** *[model]* — Facts whose source is an author external to the campaign — the published setting itself — rather than something the GM or table invented. Treated as immutable: the GM builds around canon rather than contradicting it, absent a deliberate divergence. Earlier drafts tied this definition to Floor 6; that was one campaign's example of when canon starts to bite, not part of what canon *is*. Whether, and when, canon starts to matter is campaign-specific — another table, another system, might hit that threshold on day one, or never.

A canon event doesn't need the party present to matter. In *Gate of the Feral Gods*, Carl summons the god Emberus to the 5th floor; the rampage affects every bubble on that floor, including ones Carl never enters. Modeled the same way any other **Off-screen event** is — recorded because its effects reach the party, whether or not the canon event itself, or the entity at its center, ever materializes for them.

**Off-screen event** *[model]* — Something happening elsewhere while the party is not there. Recorded when its effects will reach them.

**Coverage** *[model]* — Whether every direction the party might plausibly go has something prepared behind it. The basis for answering *am I ready for the next session*.

**Degree of investment** *[model]* — A small, fixed scale describing how much the group cares about an entity or thread, from none to the deepest band — the most cherished ally, the mortal enemy. Provisional bands: *None, Minor, Notable, Deep, Central* — placeholders until the table's own language replaces them. Says nothing about *how* the group feels, only how much: a despised rival held at Central carries exactly as much weight as a beloved ally there.

**Investment** *[model]* — An entity or thread's current degree of investment, as last set by the GM. Not calculated or aggregated automatically — a judgment call, recorded the same way any GM decision is: as an event, with provenance. Its history — rising, declining, gone quiet — is read off the sequence of these events over time, the same way any other history in the model is read. This is what lets a GM pace delivery of impact: investment is what turns an event into something the table feels.

**Signal** *[model]* — Not a recorded event in its own right. Accumulated facts the inference engine flags as possible evidence that an entity's investment has shifted — the same pass that also flags possible new relationships, just aimed at a different question. Surfaced through a **Ticket**, never applied automatically. The ticket asks the GM two separate questions: is this evidence real, and does it move the degree. A "yes" to the second is what creates the investment-change event; a "yes" to only the first just means the evidence was noted without crossing a threshold.

**Ticket** *[model]* — A short, dismissible prompt raised by the system when it notices something: a possible connection between two facts or entities, a possible shift in investment, a gap in coverage, two records that may be the same. A suggestion, never an action taken.

**Intersection note** *[model]* — Writing about the meeting of two things — this NPC in this place — that is reachable from both, rather than being filed under one and lost to the other.

**Reconciliation** *[model]* — Establishing that two records are the same thing and combining them without losing either side's contribution. Both names survive; nothing is deleted.

**Tombstone** *[model]* — A marker left behind when something is deleted, holding enough to repair later. Whether to keep them is an open decision with an early deadline: build deletion without them and repair becomes impossible to add.

---

## Part 4 — Process

**Release 1 / Release 2** *[process]* — R1 is the GM's interface, R2 the players'. See [[Roadmap]].

**Release candidate** *[process]* — A group of epics that belong together. Not a delivery gate; increments ship continuously inside one.

**Shippable** *[process]* — Functional, non-breaking, testable, demoable. **Not necessarily useful** — something correct that nothing yet reads is a legitimate release.

**Non-breaking** *[process]* — Nothing that worked stops working, and the campaign record survives. There is no user base to regress; the record is what is being protected.

**Fixture** *[process]* — A small synthetic campaign used for testing. Tests never run against the real record, which is both irreplaceable and changes weekly.

**Golden corpus** *[process]* — Output the GM has judged once — this was a good suggestion, this was noise — frozen so later changes can be checked against it without re-arguing.

**Challenger** *[process]* — A reviewer given the artifact but not the reasoning behind it, working from a fixed question set. Its most valuable output is a failing test, not an opinion.

**Storyteller** *[process]* — This tool.

**Chronicle** *[process]* — A separate, existing tool for a different campaign in a different system: a player-side record kept by one player as scribe for their table. Deliberately not integrated with Storyteller today — a strategic divergence, not an oversight, weighed openly during design. The model stays extensible toward it: Storyteller is kept mappable to Chronicle's schema, one-directionally, without requiring Chronicle to change. See [[Strategy-Multi-Campaign-and-Convergence]] for the full position.
