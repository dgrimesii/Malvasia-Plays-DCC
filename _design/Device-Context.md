---
type: design
status: draft
visibility: gm
tags: [requirements, devices]
---

# Device Context

Where each surface is actually used. Companion to [[Prep-Rhythm]] and [[Interface-Direction]].

---

## GM

| Context | Device | Mode |
|---|---|---|
| The prep block | Laptop | Full capability |
| Touch-ups | Laptop or phone | Capture, review, read, small edits |
| At the table | **Laptop** | Table view, fast retrieval |

**The table view gets a full interface.** Laptop at the table means keyboard, pointer, and real screen space — no cramping, and complex interaction is available if it earns its place. The table view can be a genuine working surface rather than a glanceable card.

Phone remains the constraining case, and it's touch-up mode only: text, short interactions, no graph navigation.

---

## Players

Tablet, laptop, or a foldable used in open mode.

**The floor is tablet-class.** Nobody is on a small phone screen. Density is affordable — an entity page can show what the party was told, their notes, and related links together rather than making them drill.

### What follows

**Touch and pointer both.** Tablets and foldables are touch; laptops aren't. Nothing requires hover, and targets work for fingers.

**No fixed viewport.** A foldable changes size when it opens and closes. Layout adapts continuously rather than choosing a size class once at load. This is a real case, not a hypothetical — one player is on a foldable.

**Typing is short-form.** Notes get typed on glass. Reinforces the existing design — plain text, brief notes, no formatting to learn (see [[Players-and-Characters]]).

**Tablets at the table are plausible**, so the read-latency requirement applies to the player surface too, not just the GM's.

---

## Shared implication

Text-primary (see [[Interface-Direction]]) holds across every device here. Interactive graph views are laptop-only in practice — fine for the GM's block and table use, not something the player surface should depend on.

Anything essential must work as text.
