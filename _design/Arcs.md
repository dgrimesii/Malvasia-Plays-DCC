---
type: design
status: draft
visibility: gm
tags: [information-architecture, arcs]
---

# Arcs — Co-Authorship, Projection, and Adjustment

Companion to [[Information-Architecture]]. That document covers the graph model and where arcs sit in it. This one covers how arcs actually behave over the life of a campaign.

---

## Arcs are co-authored

An arc is not written by the GM and delivered to the players, nor assembled by the players out of nothing. Both sides contribute different things:

- **The GM supplies shape.** Tension, escalation, climax, resolution. The GM decides when pressure increases, when a thread pays off, and what it costs.
- **The players supply substance.** Which characters they care about, what they choose under pressure, what they return to unprompted. None of this can be authored in advance.

Neither is sufficient. GM shape with no player investment is a story being performed at the table rather than with it. Player investment with no GM shape is a set of fond memories that never becomes a storyline.

The working relationship is **iterative adjustment against a projected path**: the GM projects where a thread could go, the players do something the projection didn't anticipate, and the GM revises. Repeat until resolution.

---

## The projection

An established arc holds a **projected path** — the GM's current best guess at where this thread is heading. Its defining properties:

- **It is a forecast, not a plan.** Every element is provisional and expected to change.
- **It is revised after play, not defended.** When the table diverges, the projection is wrong, not the players.
- **It is never shown to players.** This is GM sense-making, and it includes possibilities that may never happen.

What a projection holds:

| Element | What it captures |
|---|---|
| Where it's heading | The GM's current guess at a destination |
| Rising pressure | What would raise the stakes next |
| Candidate climax | The moment this thread is building toward |
| Possible resolutions | Outcomes worth being ready for, including bad ones |
| Dependencies | What must happen or exist first |
| Connections to future plans | Other threads, floors, or events this touches |

This is what makes an established arc a prep surface. "What does this thread need next session" should be answerable by reading the projection, not by reconstructing it from memory.

### Divergence is information

When the players go somewhere the projection didn't anticipate, that gap is worth noticing rather than smoothing over. Consistent divergence in one direction says something about what the table actually wants. A projection that never needed revising probably means the arc is being performed rather than co-authored.

Worth keeping lightly: what was projected, what actually happened, and what the GM changed as a result. Not as an audit trail — as a read on the table.

---

## Handles for emerging arcs

An emerging arc needs a **human-friendly handle** — something that elicits the GM's memory of what it's about, immediately, months later.

A handle is not a title. Titles are for established arcs and can be composed carefully. A handle is a mnemonic:

- "The rat they didn't kill"
- "Hilda keeps asking about the vents"
- "Three cousins, all helpful"

What makes a good handle:

- **Concrete over abstract.** "The rat they didn't kill" beats "Unexpected Mercy."
- **References the moment, not the theme.** The theme isn't clear yet; that's why it's emerging.
- **Short enough to scan** in a list of deferred threads.
- **Written by whoever noticed it.** If the system proposes the arc, it proposes a handle; the GM can overwrite it.

Handles persist after establishment as an alias, since that's what the GM will still recognize.

---

## Merging arcs

Two threads can turn out to be one — the way two characters' separate storylines become a single storyline once they meet in chapter seven. This applies to emerging and established arcs alike.

Merging must preserve:

- **Both handles.** The merged arc keeps both as aliases; the GM will still think of it by whichever one they remember.
- **All accumulated evidence**, with its original attribution. Evidence for the merged thread is the union of both, and it must remain clear which events came from which side — that's the record of two things becoming one.
- **Both projections**, reconciled by the GM rather than automatically. Two forecasts don't merge cleanly; the GM writes the new one.
- **The moment of convergence.** *When* and *why* the threads joined is often the most narratively significant fact about the merged arc — the chapter-seven meeting itself.

Merging is always a GM action. The system may notice overlapping evidence and propose it, but combining two threads is an interpretive judgment.

Splitting should also be possible: a thread the GM thought was one storyline may turn out to be two. Rarer, but the same machinery in reverse.

---

## What this means for the arc record

An arc file needs to hold, at minimum:

- **State** — suggested / emerging / established / dormant / resolved
- **Handle(s)** — including aliases from merges
- **Stakes** — what's at risk and whose investment it rests on
- **Evidence** — the events and interactions supporting it, with sessions
- **Projection** — the current forecast, explicitly provisional
- **Divergence notes** — where the table went somewhere else, and what changed
- **Connections to future plans** — other threads, floors, or events this touches
- **Resolution** — once concluded, what actually happened

The `Stages / Milestones` table in the current `Template-Arc.md` should be replaced by the projection. Stages imply a plan to be executed; a projection is a guess to be revised, and that difference is the whole point.

---

## Open questions

1. **How much projection history is worth keeping?** Enough to see the shape of divergence, not so much that it becomes an archive nobody reads.
2. **Should the system propose projections,** or only react to the GM's? Proposing where tension could rise is genuinely useful; proposing a climax may overstep into authoring the story.
3. **Can an arc resolve unsatisfyingly and stay resolved?** Not every thread earns a climax, and forcing one is its own failure mode.
4. **Do players ever see that an arc exists** — not its contents, but the fact that something they did became a thread? There's a real argument both ways.
5. **What happens to a projection when an arc goes dormant?** Frozen as-is, or explicitly marked stale so it isn't trusted on revival?
