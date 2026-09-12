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

**No GM surface targets a phone.** Stated first because it is the assumption most likely to be carried in by habit, and it has been miscited before.

| Context | Device | Mode |
|---|---|---|
| The prep block | Desktop or laptop | Full capability |
| Touch-ups | Desktop or laptop | Capture, review, read, small edits |
| At the table | **Laptop or tablet** | Table view, fast retrieval |

**Every GM surface gets a real screen.** Keyboard, pointer or touch, and genuine space — no cramping, and complex interaction is available if it earns its place. The table view can be a working surface rather than a glanceable card.

**Tablet appears only in table play.** Planning, capture, and conversion are desktop or laptop work, done sitting down with room to think. A tablet at the table is touch rather than pointer, which constrains interaction there and nowhere else.

What this rules out: any requirement phrased as *one-handed*, *at a glance*, or *phone-width* on a GM surface. Those constraints belong to the player surface, not this one.

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

## What this means for Release 1

Release 1 has one user, on a desktop or laptop, doing planning and capture. **Every device constraint that makes interface design hard — small screens, one-handed use, touch-only, glanceable output — belongs to a surface Release 1 is not building.**

Worth being explicit, because it removes a whole category of requirement from the first epics and it is easy to reintroduce by accident when writing about "at the table."

The constraints that do not relax are about **what the data carries**, not how it looks. A later surface that must show state, revelation, and truth at a glance can only do so if those were recorded per fact from the first session.

---

## Shared implication

Text-primary (see [[Interface-Direction]]) holds across every device here. Interactive graph views are laptop-class in practice — fine for the GM's block and table use, not something the player surface should depend on.

Anything essential must work as text.
