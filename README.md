# Malvasia-Plays-DCC

GM campaign repository for the Dungeon Crawler Carl Roleplaying Game. Contains floor guides, encounter tables, NPC profiles, and system notes to torment Z, Hilda, and Hannah Solo. Showrunner eyes only.

## Structure

- `00-Campaign/` — campaign overview, timeline, house rules
- `01-Players/` — player character dossiers
- `02-Sessions/` — session-by-session logs, dated `YYYY-MM-DD-Session-NN-Title.md`
- `03-NPCs/` — non-player characters, split into Crawlers / Sponsors / Denizens
- `04-Zones/` — dungeon floors and locations, named `Floor-XX-Name.md`
- `05-Factions/` — factions and organizations
- `06-Items-Loot/` — notable items, artifacts, and rewards
- `07-GM-Notes/` — secrets, plot threads, showrunner-eyes-only material
- `_templates/` — starter templates for new NPCs, Zones, Factions, and Sessions
- `assets/` — maps and reference images

## Conventions

- Every file uses YAML frontmatter (`type`, `status`, `tags`, etc.) so entries can be queried later by tools like Obsidian's Dataview/Bases, or any custom navigation tool.
- File names are prefixed by type (`Dossier-`, `NPC-`, `Zone-`, `Faction-`, `Session-`) for predictable searching and globbing.

## Visibility & Access Control

Every content file carries a `visibility` frontmatter field so a future player-facing tool (Obsidian Publish, a static site, or a custom app) knows what to show whom:

- `gm` — GM eyes only. **Default for all new NPCs, Zones, Factions, and Sessions** — nothing is player-visible until you deliberately promote it.
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
