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
