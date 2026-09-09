---
type: design
status: draft
visibility: gm
tags: [interface, requirements]
---

# Interface Requirements — User Stories

Written from the user's perspective. No architecture, no technology choices. This describes what each user needs to be able to do; how it gets built is a separate conversation.

---

## The Users

**The GM (David)** — runs the campaign. Comfortable with markdown, files, and technical tooling. Does synthesis work outside this system and brings the results in. Needs to move fluidly between long-range story thinking and "what do I run in twenty minutes."

**The Players (Julia, Amy, Sam)** — play the game. One is comfortable with technical tooling; two are not and should never encounter markdown, folders, or version control. They interact with the campaign a few hours a week, mostly around session time, and they should feel like they're consulting a record of their own adventure — not browsing a database.

---

## GM Stories

### Planning

- As the GM, I want to see where the party currently is — floor, arc, and what happened last session — without opening several files, so I can orient quickly.
- As the GM, I want to see which encounters on the current floor are still `potential` and which are `used`, so I know what's left to draw on.
- As the GM, I want to see the branch options hanging off the encounter the party just finished, so I can prepare one or two moves ahead rather than a whole tree.
- As the GM, I want to see which arcs are active and which have gone quiet, so long-range threads don't quietly die.
- As the GM, I want to be warned when something I'm planning contradicts what's already happened at the table, so I don't introduce a continuity break.

### Organizing

- As the GM, I want to drop a synthesized planning document in and have its named entities matched against everything already recorded, so I find connections I wouldn't have remembered.
- As the GM, I want proposed cross-links presented for my approval rather than applied automatically, so nothing enters the canon record without my say-so.
- As the GM, I want links maintained in both directions — when a new encounter references an existing NPC, that NPC's record should reflect the new appearance.
- As the GM, I want to find everything connected to a given NPC, faction, zone, or item in one place, regardless of which file it lives in.

### Synthesizing

- As the GM, I want suggested story beats, social interactions, and complications drawn from connections between things already recorded, so the campaign feels interconnected rather than episodic.
- As the GM, I want suggestions clearly marked as unvetted, so I never confuse a proposal with something I've decided.
- As the GM, I want to see what a given player's dossier answers make available as hooks, so backstory gets used rather than filed away.
- As the GM, I want to ask open questions about the campaign in plain language — "what does the party still not know about the Warrens?" — and get answers grounded in what's recorded.

### Creating

- As the GM, I want to build an encounter by answering prompts for the parts that matter (type, stakes, resolution, branches), so I don't start from a blank page.
- As the GM, I want to be told when an encounter isn't ready to run — missing stakes, undefined resolution, no failure consequence — before I'm at the table discovering it.
- As the GM, I want the system's default consequences applied automatically, so I only write what's genuinely unique to this encounter.
- As the GM, I want to record what actually happened after a session and have the affected records update together — encounters marked used, NPC dispositions changed, arc stages advanced.
- As the GM, I want to choose when a piece of content becomes visible to players, as a deliberate act.
- As the GM, I want a prep view I can actually run a session from — the opening beats, the anticipated branches, and the NPCs likely to appear, in one place.

---

## Player Stories

### Finding out what they know

- As a player, I want to ask questions in plain language — "who was that guy at the checkpoint?" — rather than searching or navigating a structure.
- As a player, I want to look up an NPC we've met and see what we learned about them, so I don't have to remember three sessions back.
- As a player, I want to review what happened in previous sessions, so I can catch up before we play.
- As a player, I want to see the zones we've explored and what we found there.
- As a player, I want to see the factions we know about and where we stand with them.
- As a player, I want to be confident that everything I'm shown is something my character could actually know — I should never see a spoiler, and I should never have to wonder whether I just saw one.
- As a player, I want it to be clear when something is simply not known yet, rather than getting an empty result that looks like an error.

### Capturing their own notes

- As a player, I want to write a note during or after a session and attach it to the session, NPC, zone, monster, or faction it's about.
- As a player, I want to write in plain text with no formatting rules to learn.
- As a player, I want to find my own notes again later, including ones about things I've since learned more about.
- As a player, I want my notes to be mine — visible to me always, and shared with the table only if I choose to share them.
- As a player, I want to record a theory or a suspicion, not just facts, and have it stay marked as my speculation.
- As a player, I want to leave a question for the GM without it becoming a table-wide announcement.

---

## Rules That Apply Everywhere

- The GM sees everything. No exceptions.
- Players see content the GM has explicitly made visible, plus everything they created themselves.
- A player's own notes are always visible to that player, whatever else changes.
- Visibility is a deliberate GM action, never a default or a side effect.
- Making something visible is not retroactive to a player's memory — but it should be evident to a player when new material has been revealed since they last looked.

---

## Open Questions

These need answers before this becomes a build, but not before it becomes a shared understanding.

1. **Player notes are a new kind of content.** Everything recorded so far is GM-authored. Player notes are player-authored, need to survive alongside the canon record without becoming canon, and belong to their author. Where they live and who can edit them is undecided.
2. **What happens when a player's note references something they shouldn't know?** A player writing "I think the Warden works for Godpapa John" may be right, and the system shouldn't confirm or deny it.
3. **Is there a shared party-visible layer** — notes players deliberately publish to each other — or only private notes and GM-revealed content?
4. **How do players reach this?** Phone at the table, laptop between sessions, or both, changes what the experience should feel like.
5. **Does the GM see player notes?** Arguments both ways: they're a rich signal about what the table finds interesting, but players may write more freely believing they're unobserved.
6. **Revealing in bulk.** After a session, several things become known at once. Is that one action or many?
