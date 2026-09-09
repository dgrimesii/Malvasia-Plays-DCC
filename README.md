# Malvasia-Plays-DCC

GM campaign repository for the Dungeon Crawler Carl Roleplaying Game. Contains floor guides, encounter tables, NPC profiles, and system notes to torment Z, Hilda, and Hannah Solo. Showrunner eyes only.

## Planning Hierarchy

GM planning happens at three nested scopes, each contained in the one above it:

**Campaign** → **Arc** → **Zone** → **Session**

- **Campaign** — the whole game: premise, house rules, overall timeline.
- **Arc** — a story throughline spanning multiple floors and sessions (a villain, a quest, a long-term consequence).
- **Zone** — a single floor: encounter rules, rooms, hazards — reused across every session spent there.
- **Session** — a single sitting: what's planned, then what actually happened.

Zones and Sessions cross-reference which Arc they serve via an `arc:` frontmatter field; Arcs list which Zones (`zones:`) they touch.

## Workflow: Synthesis → Integration

Planning content is synthesized externally before it reaches this repo:

1. Official source PDFs live in Google Drive.
2. A Gemini Notebook references them and produces synthesized planning content, written directly as Markdown.
3. That output lands untouched in `_working/` via `_templates/Template-Intake.md`.
4. The GM cross-references it against existing NPCs, Arcs, Zones, and Sessions, then splits/promotes the relevant pieces into the real canon folders (00–08), linking as it goes.
5. The intake file is marked `status: integrated` or deleted once nothing of value remains outside the canon files.

## Structure

- `00-Campaign/` — campaign overview, timeline, house rules
- `01-Arcs/` — story arcs (multi-floor, long-term)
- `02-Zones/` — dungeon floors, named `Floor-XX-Name.md`
- `03-Sessions/` — session-by-session prep and logs, dated `YYYY-MM-DD-Session-NN-Title.md`
- `04-Players/` — player character dossiers
- `05-NPCs/` — non-player characters, split into Crawlers / Sponsors / Denizens
- `06-Factions/` — factions and organizations
- `07-Items-Loot/` — notable items, artifacts, and rewards
- `08-GM-Notes/` — secrets, plot threads, showrunner-eyes-only material
- `_templates/` — starter templates for new Arcs, NPCs, Zones, Factions, Sessions, and Intake
- `_working/` — landing zone for synthesized content awaiting integration (not canon)
- `assets/` — maps and reference images

## Conventions

- Every file uses YAML frontmatter (`type`, `status`, `tags`, etc.) so entries can be queried later by tools like Obsidian's Dataview/Bases, or any custom navigation tool.
- File names are prefixed by type (`Dossier-`, `Arc-`, `NPC-`, `Zone-`/`Floor-`, `Faction-`, `Session-`) for predictable searching and globbing.
- Text meant to be read verbatim at the table is wrapped in a blockquote starting `> **READ ALOUD`, so it's easy to spot mid-session.
- An optional `source:` frontmatter field records provenance (e.g. `gemini-synthesis`) for content that passed through the intake workflow above.

## Visibility & Access Control

Every content file carries a `visibility` frontmatter field so a future player-facing tool (Obsidian Publish, a static site, or a custom app) knows what to show whom:

- `gm` — GM eyes only. **Default for all new Arcs, NPCs, Zones, Factions, and Sessions** — nothing is player-visible until you deliberately promote it.
- `player-ro` — visible to all players, read-only.
- `player-rw` — a specific player can edit it; everyone else treats it as read-only. Player dossiers use the existing `player:` field to determine the owner.

For files that are mostly player-facing but contain a GM-only block (e.g. an NPC's secrets), wrap just that section in comment markers, which render as invisible in any Markdown viewer:

```
<!-- visibility:gm -->
## Secrets (GM only)
...
<!-- /visibility:gm -->
```

**Note:** this repo is currently public (kept that way so the Claude GitHub connector functions reliably). The `visibility` tagging above governs what a future player tool displays — it does not restrict who can read the raw files on GitHub today.
