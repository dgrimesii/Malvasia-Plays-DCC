---
type: design
status: draft
visibility: gm
tags: [interface, requirements]
---

# Interface Requirements — User Stories

Written from the user's perspective. No architecture, no technology choices. This describes what each user needs to be able to do; how it gets built is a separate conversation.

---

## Assumptions

These are settled and shape everything below:

- **The repo is the database.** The markdown and YAML files are storage, not an interface. Whether that storage format changes is a design-phase decision and has no bearing on these stories.
- **The interface handles all display.** Neither user group interacts with files, folders, or version control directly. Players never see raw markdown; rendered markdown is a perfectly good display format for them.
- **Players never touch the repo.** Their access is entirely through the interface.
- **Synthesis happens upstream; authoring happens in the tool.** Source PDFs are referenced in Gemini, which produces markdown. That markdown is the *baseline* — once it lands, the tool is where the GM writes, connects, revises, and adds. Broad research and first-draft ideation stay in Gemini; everything after is here.

---

## The Users

**The GM (David)** — runs the campaign. Comfortable with markdown, files, and technical tooling. Brings in synthesized planning content from outside and turns it into connected, runnable material. Moves constantly between long-range story thinking and "what do I run in twenty minutes."

**The Players (Julia, Amy, Sam)** — play the game. One is comfortable with technical tooling; two are not. They read rendered content and type plain text; neither group ever encounters syntax, files, or structure. They interact a few hours a week, mostly around session time, and should feel like they're consulting a record of their own adventure — not browsing a database.

---

## GM Stories

### Planning

- As the GM, I want to see where the party currently is — floor, arc, and what happened last session — in one view, so I can orient quickly.
- As the GM, I want to see which encounters on the current floor are still `potential` and which are `used`, so I know what's left to draw on.
- As the GM, I want to see the branch options hanging off the encounter the party just finished, so I can prepare one or two moves ahead rather than a whole tree.
- As the GM, I want to see which arcs are active and which have gone quiet, so long-range threads don't quietly die.
- As the GM, I want to be warned when something I'm planning contradicts what's already happened at the table, so I don't introduce a continuity break.

### Organizing

- As the GM, I want to bring in a synthesized planning document and have its named entities matched against everything already recorded, so I find connections I wouldn't have remembered.
- As the GM, I want to work through integration inside the tool — splitting a draft into the arcs, zones, sessions, and NPCs it implies — rather than editing files by hand.
- As the GM, I want proposed cross-links presented for my approval rather than applied automatically, so nothing enters the canon record without my say-so.
- As the GM, I want links maintained in both directions — when a new encounter references an existing NPC, that NPC's record should reflect the new appearance.
- As the GM, I want to find everything connected to a given NPC, faction, zone, or item in one place, regardless of where it's stored.
- As the GM, I want to see what's still sitting unintegrated, so drafts don't get stranded half-promoted.

### Authoring

- As the GM, I want to capture a note the moment an insight surfaces — while reviewing a connection, mid-integration, or mid-prep — without leaving what I'm doing or deciding where it belongs first.
- As the GM, I want to write about the *intersection* of two or more things, and have that note reachable from all of them rather than filed under just one.
- As the GM, I want to make a spot edit to any asset — a line of NPC dialogue, a stake, a disposition — without opening an editing mode or navigating away.
- As the GM, I want to create a new asset from scratch when something emerges at the table that no synthesis anticipated.
- As the GM, I want a rough note I wrote earlier to be easy to find and promote into real content later, so quick capture doesn't become a graveyard.
- As the GM, I want to revise something after it's been made visible to players, and understand what they've already seen.

### Synthesizing

- As the GM, I want suggested story beats, social interactions, and complications drawn from connections between things already recorded, so the campaign feels interconnected rather than episodic.
- As the GM, I want suggestions clearly marked as unvetted, so I never confuse a proposal with something I've decided.
- As the GM, I want to see what a given player's dossier answers make available as hooks, so backstory gets used rather than filed away.
- As the GM, I want to ask open questions about the campaign in plain language — "what does the party still not know about the Warrens?" — and get answers grounded in what's recorded.

### Preparing to run

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
- As a player, I want to type plainly, with no syntax or formatting rules to learn.
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
- Anything authored in the tool defaults to GM-only until deliberately revealed.
- Making something visible is not retroactive to a player's memory — but it should be evident to a player when new material has been revealed since they last looked.

---

## Open Questions

These need answers before this becomes a build, but not before it becomes a shared understanding.

1. **Where does a note about an intersection live?** A GM insight connecting an NPC to a faction to a past session belongs to all three and none of them. Attaching it to one and cross-referencing loses something; duplicating it is worse.
2. **What happens when a player's note references something they shouldn't know?** A player writing "I think the Warden works for Godpapa John" may be right, and the system shouldn't confirm or deny it.
3. **Is there a shared party-visible layer** — notes players deliberately publish to each other — or only private notes and GM-revealed content?
4. **Does the GM see player notes?** Arguments both ways: they're a rich signal about what the table finds interesting, but players may write more freely believing they're unobserved.
5. **How do players reach this?** Phone at the table, laptop between sessions, or both, changes what the experience should feel like.
6. **Revealing in bulk.** After a session, several things become known at once. Is that one action or many?
7. **Does revising revealed content need to be visible to players as a change,** or does the record simply become what it now says?
