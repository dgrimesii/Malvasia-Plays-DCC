---
type: design
status: draft
visibility: gm
tags: [requirements, latency, scope]
---

# Update Cadence

Resolves most of [[Open-Requirements]] §8.

---

## Reads and writes have different requirements

Treating these as one thing overstated the problem considerably.

| | Requirement | Frequency |
|---|---|---|
| **Writes** | Batch, between sessions | Once per session |
| **Reads** | Fast, at the table | Constantly during play |

Nothing needs to be current. The table view showing data a full session old is not a limitation — that *is* the content. "What happened last session" is inherently retrospective.

---

## What this removes

- **Live sync.** Nothing needs to propagate during play.
- **Collaborative editing.** The GM writes between sessions; players write between sessions. Not simultaneously, and not on the same records.
- **Concurrency and conflict resolution.** No two people editing the same thing at the same time.
- **Real-time capture.** Nobody is transcribing during play. If something is worth recording, it's recorded afterward.

---

## What it enables

**Everything can be precomputed.** If writes are batched and staleness is expected, the whole derived layer can be built once after each session:

- The graph and its derived inverse views
- Per-player filtered slices
- The table view at its default scope and zoom
- Coverage and readiness checks
- Whatever proposals and clusters the AI surfaces

At the table, the GM and players are **reading a prepared artifact**, not querying a live system. That makes the latency requirement much easier to meet, and makes offline operation nearly free — a prepared artifact can sit locally.

It also means expensive computation is fine. Anything that would be too slow to run interactively can run once, between sessions, with nobody waiting.

---

## The one real sequencing constraint

If players write notes and the GM's prep should account for them, notes need to land before prep starts. That's a workflow ordering question measured in hours or days — not a technical one.

Worth establishing as a habit rather than a mechanism: notes by midweek, prep after.

---

## What still needs to be fast

Only retrieval, and only against prepared data:

- Looking up an NPC, place, or past event mid-session
- Re-centering the table view as the scene moves
- Finding what the party was told about something

These are reads over a precomputed structure. Fast is achievable without anything clever.

---

## Open

**Can the GM write during a session if something comes up?**
Probably worth allowing — a quick note rather than full capture. But it isn't required, and nothing should depend on it.

**Does the prepared artifact need to be regenerated if the GM edits mid-week?**
Likely yes, and cheap. Worth confirming it's not a manual step that gets skipped.
