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
| The prep block | Desk | Full capability |
| Touch-ups | Desk or phone | Capture, review, read, small edits |
| At the table | TBD | Table view, fast retrieval |

Phone is the constraining case, and it's the touch-up mode — text, short interactions, no complex graph navigation.

**Still open:** what the GM uses at the table. Laptop is the obvious guess, but it hasn't been confirmed, and it determines the table view's layout.

---

## Players

Tablet, laptop, or a foldable phone. Between sessions and possibly at the table.

### What follows

**More density is affordable.** These are medium-to-large screens, unlike the GM's phone touch-ups. An entity page can show what the party was told, their notes, and related links together rather than making them drill.

**Touch and pointer both.** Tablet and foldable are touch; laptop isn't. Nothing should require hover, and targets need to work for fingers.

**No fixed viewport.** A foldable changes size mid-session. Layout adapts rather than assuming a size class at load.

**Typing is short-form.** Notes get typed on glass. That reinforces the existing design — plain text, brief notes, no formatting to learn (see [[Players-and-Characters]]). Long-form composition isn't the expected use.

**Tablets at the table are plausible**, which supports the read-latency requirement applying to the player surface too, not just the GM's.

---

## Shared implication

Text-primary (see [[Interface-Direction]]) holds up across every device here. Interactive graph views do not — they're desk-and-block only. Anything essential must work as text.
