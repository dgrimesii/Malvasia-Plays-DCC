# Malvasia-Plays-DCC

Two things live here.

**The campaign** — GM material for a *Dungeon Crawler Carl Roleplaying Game* campaign: floor guides, encounter tables, NPC profiles, and system notes, to torment Z, Hilda, and Hannah Solo. Showrunner eyes only.

**Storyteller** — a tool being designed to support running that campaign, and campaigns generally. Its design lives in `_design/`, its epics in `_backlog/`. Storyteller is deliberately **system- and campaign-agnostic**: it records people, places, events, quests, arcs, claims, and the connections between them. Mechanics — dice, stats, turn structure — stay in the rulebook and out of the model. Every system supplies a way to *resolve* what happens; none of them supplies what it *means*, and the meaning is what this holds.

Start with [`_design/README.md`](_design/README.md), which orders the corpus and says which seven documents carry most of the reasoning. If you only read one, read [`_design/Glossary.md`](_design/Glossary.md) — every term used in an epic is defined there, written for someone who has never played a tabletop RPG.

## Repository layout

**Design and delivery**

- `_design/` — the design corpus: model, scope, constraints, strategy, roadmap
- `_backlog/` — epics and delivery planning

**Campaign content**

- `00-Campaign/` — campaign overview, timeline, house rules
- `01-Arcs/` — arcs and material aimed at arcs (see the note below)
- `02-Zones/` — floors, named `Floor-XX-Name.md`
- `03-Sessions/` — session prep and logs, dated `YYYY-MM-DD-Session-NN-Title.md`
- `04-Players/` — player character dossiers
- `05-NPCs/` — non-player characters, split into Crawlers / Sponsors / Denizens
- `06-Factions/` — factions and organizations
- `07-Items-Loot/` — notable items, artifacts, and rewards
- `08-GM-Notes/` — secrets, plot threads, showrunner-eyes-only material

**Supporting**

- `_templates/` — starter templates for new entries
- `_working/` — landing zone for synthesized content awaiting integration (not part of the campaign record)
- `assets/` — maps and reference images

## How content gets here today

Planning content is often synthesized outside this repo — currently via a Gemini notebook over official source PDFs in Google Drive — and arrives as Markdown in `_working/` using `_templates/Template-Intake.md`. The GM cross-references it against existing entries, then splits and promotes the relevant pieces into the numbered folders, linking as it goes. The `_working/` file is marked `status: integrated` or deleted once nothing of value remains outside it.

**This is the manual stand-in for what `_design/` calls intake**, and how the notes were produced is irrelevant to it — a Gemini synthesis, a typed recap, and handwritten notes photographed after a session are all the same input. Intake proper is two stages that never merge: the system proposes concrete changes to entities and relationships, the GM reviews and edits and accepts them, and only then does impact detection run over what was accepted. Nothing is written unreviewed. It accepts post-session notes and forward-looking planning notes alike. See [`_design/Session-Capture.md`](_design/Session-Capture.md).

Synthesizing outside the tool is not a workaround, either — it stays that way by design. The planning cycle in [`_design/Planning-Loop.md`](_design/Planning-Loop.md) has the GM search and read, synthesize externally, load the result, and review what the system then projects from it, iterating until they sit down at the table.

## Three notes on vocabulary

The folder names predate the design work and don't all match the model. Worth knowing before reading either.

**Arcs aren't authored.** An arc is a thread of meaning the table forms through play — discovered by noticing connections, confirmed by the GM, never written into existence. What a GM *can* author is material aimed at one, which the Glossary calls **arc intent**: legitimate prep that may never land. `01-Arcs/` holds both, and they are different things. An arc also isn't a planning scope that contains zones or sessions; it cuts across them.

**Places nest to any depth.** *Floor* and *Zone* are this campaign's names for two tiers of place. In the model there is no fixed tier count and no enumerated place types — places contain places, and a GM wanting *continent → country → city → structure → floor → room* gets it without new vocabulary. The `Floor-XX-Name.md` convention works until the store exists; migrating it is a filename change, not a model change.

**Hooks aren't a kind of thing.** A hook is a fact meant to entice the players and build investment — and a rumour is a **claim** with a speaker, an NPC's assertion is an **utterance**, a visible thing in a room is a **fact** about a place. All three already exist and already carry visibility. *Hook* names the GM's purpose in authoring a fact, not a class in the store. Worth stating because the temptation to add one later is real.

Also note **canon** has a precise meaning in the design: facts sourced from an author external to the campaign — the published books — and treated as immutable. It does not mean "the real folders as opposed to `_working/`."

## What a claim is, and why it matters for notes

The one model idea worth knowing before writing anything into this repo.

A recap sentence with a speaker produces **two** records, not one: the utterance happened, and the proposition it carried is a **claim** whose truth is a separate question. *The Warden said the tunnels flood at night* is permanently true. *The tunnels flood at night* may be a lie.

A claim's truth is `true`, `false`, or **`undetermined`** — and undetermined is the default and a legitimate permanent state. The GM may not have decided, and may not decide for many sessions. That is not a gap in the record; it is optionality kept open deliberately. See [`_design/Claims-and-Resolution.md`](_design/Claims-and-Resolution.md).

Practical consequence for notes written by hand today: **keep the speaker.** *The Warden claims X* and *X* are different entries, and collapsing them is the costliest capture error available — it puts a lie in the record's own voice and spoils the deception the first time a player reads it.

## Conventions

- Every file uses YAML frontmatter (`type`, `status`, `tags`, etc.) so entries can be queried by tools like Obsidian's Dataview/Bases, or any custom navigation tool.
- File names are prefixed by type (`Dossier-`, `Arc-`, `NPC-`, `Zone-`/`Floor-`, `Faction-`, `Session-`) for predictable searching and globbing.
- Text meant to be read verbatim at the table is wrapped in a blockquote starting `> **READ ALOUD`, so it's easy to spot mid-session.
- An optional `source:` frontmatter field records provenance (e.g. `gemini-synthesis`) for content that passed through `_working/`.

## Visibility

Every content file carries a `visibility` frontmatter field so a future player-facing tool knows what to show whom:

- `gm` — GM eyes only. **Default for everything new** — nothing is player-visible until deliberately promoted.
- `player-ro` — visible to all players, read-only.
- `player-rw` — a specific player can edit it; everyone else treats it as read-only. Player dossiers use the existing `player:` field to determine the owner.

For files that are mostly player-facing but contain a GM-only block, wrap just that section in comment markers, which render as invisible in any Markdown viewer:

```
<!-- visibility:gm -->
## Secrets (GM only)
...
<!-- /visibility:gm -->
```

**These are file-level flags, and the model doesn't work this way.** In `_design/`, visibility has two values (`gm` and `player`) and applies to individual facts and relationships rather than whole documents — the party can know an NPC exists, know one of their names, and not know they are connected to a faction, all at once. The three values above also fold in an edit-permission concept the model treats separately as attribution. The frontmatter is a reasonable approximation for flat files; it is not the target design.

**Note:** this repo is currently public (kept that way so the Claude GitHub connector functions reliably). The `visibility` tagging governs what a future player tool displays — it does not restrict who can read the raw files on GitHub today.
