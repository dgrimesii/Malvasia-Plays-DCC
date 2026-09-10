---
type: design
status: draft
visibility: gm
tags: [requirements, gm-surface, workflow]
---

# Prep Rhythm

Resolves [[Open-Requirements]] §8. Determines the shape of the GM surface.

---

## Settled

- **A long block, plus touch-ups.** One substantial prep session, with shorter passes around it.
- **Desk mostly, phone sometimes.**

That's two modes, not one interface scaled down.

---

## Mode 1 — the block (desk)

Where the real work happens. Full capability:

- Integration of synthesized material from `_working/`
- Authoring encounters, arcs, NPCs
- Reviewing accumulated proposals and tickets
- Visualization at any scope and zoom
- Coverage and readiness checking

**This is where readiness gets confirmed.** The sentence *"you are prepared for the next session"* belongs here, backed by what was checked. It's the mode with enough context to make that claim mean something.

Expensive operations belong here too — nothing about this mode is latency-sensitive, and per [[Update-Cadence]] the heavy computation has already run between sessions anyway.

---

## Mode 2 — touch-ups (desk or phone)

Short, opportunistic, often away from the desk. Read-mostly with light capture.

What it needs:

- **Quick capture.** An idea arrives; record it without deciding where it belongs. This is the story from [[Interface-User-Stories]] — *"capture a note the moment an insight surfaces"* — and phone-based touch-ups are its primary context.
- **Review proposals.** Approve, reject, or defer a ticket. Small decisions that don't need the full picture.
- **Read anything.** Look something up, check a detail, re-read a plan.
- **Small edits.** Fix a line, adjust a stake, correct a name.

What it does **not** need:

- Integration passes
- Authoring from scratch
- Complex graph navigation
- Anything requiring sustained attention

The text-primary direction in [[Interface-Direction]] pays off here — a phone handles text well and interactive graph views badly.

---

## What connects them

**Resumability.** Returning after a gap, the first question is *what was I doing and what's left?* Both directions:

- Coming back to the block: what's still unresolved from last time
- Coming into a touch-up: anything quick worth doing right now

**Touch-ups must not silently break readiness.** Adding a branch during a touch-up can uncover a coverage gap. That should be visible — quietly, not alarmingly — rather than discovered at the table. A touch-up that changes readiness says so.

**Captured items surface in the block.** Anything jotted during a touch-up appears in the next block's working set. Quick capture that vanishes into a pile is the failure mode described in [[GM-Considerations]].

---

## Design consequence

The two modes share data and differ in capability, not in content. Nothing is touch-up-only or block-only in terms of *what exists* — the difference is what's practical to do.

The risk to avoid: building the block interface and shipping a cramped version of it as the phone view. Touch-up mode is a different set of actions, not a smaller window onto the same ones.
