---
type: design
status: draft
visibility: gm
tags: [requirements, gm-surface, transparency]
---

# GM Player-View Switch, and Player Transparency

Two settled requirements.

---

## The GM can switch to the player view

A distinct, first-class capability — not a debug toggle.

**The prep question it answers:** *what do they actually know about this right now?*

Before running a scene, the GM needs to see the Warden's page as the party sees it: which utterances are revealed, which notes they've written, what's absent. Without it, the recurring failure is referencing something the party never learned, or withholding something they already know.

### What it must show

- Exactly what the player view shows — same filtering, same attribution, no GM annotations bleeding through
- Clearly marked as the player view, so it's never mistaken for the GM's own
- Switchable per entity, not just globally — the question is usually about one thing

### Related capability

**A gap check:** given what the GM is about to run, is there anything the party would need to already know and doesn't? Cheap to surface during prep, painful to discover mid-scene.

---

## Players are told about the tool

Settled: the players know it exists and roughly how it works — including that their queries inform prep, and that the system looks for patterns in what they engage with.

### Why this matters beyond courtesy

- **A known signal is a better signal.** Players who know their curiosity steers prep will use the tool more, which produces more of the data that makes it useful.
- **It removes a discomfort that would otherwise surface later.** Discovering after the fact that lookups were being tracked is worse than being told up front, regardless of intent.
- **Most of it is flattering.** "The system noticed you kept asking about the Warden, so I built something" is a good thing to be told.

### What doesn't get shared

Being told the tool exists is not being shown its contents. The GM's projections, arcs, off-screen events, and unrevealed material stay GM-only. Transparency is about the mechanism, not the material.
