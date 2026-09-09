---
type: design
status: draft
visibility: gm
tags: [information-architecture, arcs]
---

# Arcs — Co-Authorship, Projection, and Adjustment

Companion to [[Information-Architecture]]. That document covers the graph model and where arcs sit in it. This one covers how arcs actually behave over the life of a campaign.

---

## Two trees

There are two separate structures, and conflating them is the mistake to avoid.

| | **The planning tree** | **The arc tree** |
|---|---|---|
| Question it answers | What must I be ready to run? | What carries weight? |
| Nature | Physical | Emotional |
| Horizon | The next session or two | The whole campaign |
| Rooted in | Where the party is now | What the players are invested in |
| Coverage | Complete — every live branch needs *something* | Bounded — dense enough to feel like a story, sparse enough to feel free |
| Built by | The GM, in advance | The GM and players together, in retrospect |
| Nodes | Encounters, hazards, locations, mobs | Stakes, choices, consequences, meaning |

The planning tree is about **preparedness**: if the party goes left instead of right, is there something there? It branches on player choice and needs enough coverage that no direction leaves the GM stranded.

The arc tree is about **significance**: which of the things that happened will still matter in ten sessions, and why. It branches on investment and consequence.

They intersect at events, but neither contains the other. An event can sit in both trees, or in the planning tree alone.

### Arc density is a band, not a floor

Not every event belongs to an arc — but the right proportion isn't "as few as possible." It's a range, and both edges are failure modes:

| Density | Feels like | Why |
|---|---|---|
| Too low | **A grind** | Events don't accumulate into anything; play becomes a sequence of rooms and fights with nothing carried forward |
| Right | A story | Enough threads that choices echo, enough open space that the party's direction is genuinely theirs |
| Too high | **Railroading** | Every event is significant, which means every event was placed; players feel the authorial hand and stop believing their choices matter |

The second failure is counterintuitive: making *more* things meaningful reduces the sense of agency, because meaning implies authorship. Some events need to be nobody's plan.

### The campaign is time-bound

A TTRPG campaign has a finite number of sessions, and story must compress into that time. This is the constraint that makes density a real problem rather than a matter of taste:

- Threads that meander indefinitely never resolve, because there isn't indefinite time.
- An arc established late has less room to build than one established early, and needs to move faster.
- Approaching the end, unresolved arcs must converge — or be deliberately left open, which is a choice rather than an oversight.
- **Arcs have a budget.** Five established arcs and twenty sessions left is a pacing fact, not a vague worry.

This is measurable in a rough way, and worth surfacing: what proportion of recent events touched an arc, which established arcs have gone quiet, how much campaign time remains against how much is unresolved. Not to optimize — to notice drift before it becomes either a grind or a rush.

### Why this matters for Dungeon Crawler Carl specifically

The source material runs on choice, ambiguity, and hard realities — situations with no clean answer where something is lost either way. That only works if the players have something to lose.

The planning tree can produce a difficult *tactical* situation on its own. It cannot produce a hard *choice*. What makes a choice hard is investment, and investment is what the arc tree tracks. **The arc tree is the machinery that turns a tactical problem into a moral one.**

### Design implication

The tool needs both views and shouldn't try to flatten them into a single hierarchy. They have different shapes, different time horizons, and different authors.

The ticket mechanism (see [[Information-Architecture]]) is the bridge: it fires while the GM is working in the planning tree and points at something in the arc tree — *this encounter you're building touches a thread that carries weight; consider raising the stakes.*

Density awareness is the counterweight. The same system that proposes connections should be able to say the opposite: *the last four sessions have been almost entirely arc-connected — consider letting the next one just be a dungeon.*

---

## Arcs are co-authored

An arc is not written by the GM and delivered to the players, nor assembled by the players out of nothing. Both sides contribute different things:

- **The GM supplies shape.** Tension, escalation, climax, resolution. The GM decides when pressure increases, when a thread pays off, and what it costs.
- **The players supply substance.** Which characters they care about, what they choose under pressure, what they return to unprompted. None of this can be authored in advance.

Neither is sufficient. GM shape with no player investment is a story being performed at the table rather than with it. Player investment with no GM shape is a set of fond memories that never becomes a storyline.

The working relationship is **iterative adjustment against a projected path**: the GM projects where a thread could go, the players do something the projection didn't anticipate, and the GM revises. Repeat until resolution.

---

## The projection is probabilistic

A projection is not a single forecast line. It's conditional reasoning about likely futures, and it branches.

The GM's actual thought process looks like:

> The party humiliated the Toll Warden in Session 3. Godmama Mia exists on Floor 2 and is his sister. She will hear about it. So: she confronts them (likely), or she moves against them indirectly (also likely), or she ignores it because she never liked him either (possible but less so). Let me project a conflict event.

That decomposes into parts worth holding separately:

| Part | What it is |
|---|---|
| **Premises** | What's already true and drives the inference — events that happened, relationships that exist, dispositions established |
| **Inference** | The reasoning connecting premises to outcomes |
| **Outcomes** | The branching possibilities, each with a rough likelihood |
| **Projected events** | Speculative events the GM might author if a branch looks live |

### Likelihood should stay coarse

Qualitative bands — `likely` / `possible` / `unlikely` — not percentages. Precise numbers on narrative speculation are false precision, and they invite treating a projection as a forecast to be scored rather than a tool for readiness.

The useful question a likelihood answers is "how much prep does this branch deserve?" `Likely` gets a sketched event. `Possible` gets a note. `Unlikely` gets a line so it isn't forgotten if it happens.

### Projected events extend the encounter ladder

An encounter already has `potential` and `used`. Projection adds a stage before both:

```
speculative  →  potential  →  used
(projected,     (authored,     (played)
 not written)    not run)
```

A speculative event is a *possibility the GM is holding*, not content. Promoting it to `potential` is the act of actually writing it — and is where something crosses from the arc tree into the planning tree. This keeps projections cheap: the GM can hold six speculative branches without writing six encounters.

### Premises decay

This is the part worth building for. A projection rests on premises, and premises change:

- The party humiliated the Warden — then rescued him two sessions later.
- Godmama Mia is his sister — then that turns out to be a cover story.
- She'll hear about it — then the only witness dies.

When a premise changes, **every projection resting on it should be flagged for revisit.** Not auto-revised — flagged, with the changed premise named:

> This projection assumed the party was hostile to the Warden. That changed in Session 5.

This is only possible if premises are recorded as links to the things they depend on, rather than written as prose. It's the strongest practical argument for the graph model in the whole design: stale speculation is invisible in prose and cheap to detect on a graph.

### Properties of the projection as a whole

- **It is a forecast, not a plan.** Every element is provisional and expected to change.
- **It is revised after play, not defended.** When the table diverges, the projection is wrong, not the players.
- **It is never shown to players.** This is GM sense-making, and it includes possibilities that may never happen.

This is what makes an established arc a prep surface. "What does this thread need next session" should be answerable by reading the projection, not by reconstructing it from memory.

### Divergence is information

When the players go somewhere no branch anticipated, that gap is worth noticing rather than smoothing over. Consistent divergence in one direction says something about what the table actually wants. A projection that never needed revising probably means the arc is being performed rather than co-authored.

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
- **Both projections**, reconciled by the GM rather than automatically. Two forecasts don't merge cleanly; premises may now conflict, and branches that were independent may become mutually exclusive. The GM writes the new one.
- **The moment of convergence.** *When* and *why* the threads joined is often the most narratively significant fact about the merged arc — the chapter-seven meeting itself.

Merging is always a GM action. The system may notice overlapping evidence and propose it, but combining two threads is an interpretive judgment.

Merging is also a **pacing tool**: converging threads is how a campaign compresses toward its ending. Late-campaign merges aren't just bookkeeping — they're how five open storylines become two that can actually resolve in the time remaining.

Splitting should also be possible: a thread the GM thought was one storyline may turn out to be two. Rarer, but the same machinery in reverse.

---

## What this means for the arc record

An arc file needs to hold, at minimum:

- **State** — suggested / emerging / established / dormant / resolved
- **Handle(s)** — including aliases from merges
- **Stakes** — what's at risk and whose investment it rests on
- **Evidence** — the events and interactions supporting it, with sessions
- **Projection** — premises, branching outcomes with likelihoods, speculative events
- **Divergence notes** — where the table went somewhere else, and what changed
- **Connections to future plans** — other threads, floors, or events this touches
- **Resolution** — once concluded, what actually happened

The `Stages / Milestones` table in the current `Template-Arc.md` should be replaced by the projection. Stages imply a plan to be executed; a projection is branching speculation to be revised, and that difference is the whole point.

---

## Open questions

1. **How much projection history is worth keeping?** Enough to see the shape of divergence, not so much that it becomes an archive nobody reads.
2. **Should the system propose projections,** or only react to the GM's? Proposing where tension could rise is genuinely useful; proposing a climax may overstep into authoring the story.
3. **Should the system propose *branches* on an existing projection?** Narrower than proposing a whole projection — "you haven't considered that she might do nothing" — and possibly the more useful version.
4. **Is arc density actually measurable in a useful way,** or does counting arc-connected events mistake quantity for weight? One devastating choice may carry a whole campaign.
5. **Does the campaign have a known length?** Budgeting and convergence only work against a horizon. If the end is open-ended, pacing has to be judged differently.
6. **Can an arc resolve unsatisfyingly and stay resolved?** Not every thread earns a climax, and forcing one is its own failure mode.
7. **Do players ever see that an arc exists** — not its contents, but the fact that something they did became a thread? There's a real argument both ways.
8. **What happens to a projection when an arc goes dormant?** Frozen as-is, or explicitly marked stale so it isn't trusted on revival?
9. **Do speculative events that never happen get deleted or kept?** Kept, they're a library of unused ideas; deleted, the projection stays readable.
