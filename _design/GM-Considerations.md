---
type: design
status: living
visibility: gm
tags: [gm, judgment, considerations]
---

# GM Considerations

A living list of the recurring judgment calls this campaign will present. These are not problems the tool solves — they're decisions only the GM can make. The tool's job is to surface them at the right moment with enough context to decide well.

Add to this as new ones surface in play.

---

## The GM is a participant

The GM is not a service provider running a game for an audience. Four people are at the table and all four want the same things: build a great story, have a great time, and feel the weight of a harsh world pressing on characters they care about.

The GM's role is different — preparation, adjudication, voicing the world — but the objective is identical. **Any tool decision that improves player experience at the cost of GM experience is a bad trade**, because it degrades the game for one of the four people playing it.

This has a specific implication worth stating plainly: *the GM must be able to be surprised.* A system that makes planning so complete that nothing unexpected can happen has optimized away the GM's own reason for being there. Leave room to not know what happens next.

---

## How this GM works

Design context, stated plainly so the tool can be built for the actual person using it.

**The drive toward systems, processes, and detail is a given.** It isn't going to be moderated by willpower, and shouldn't be — it's also why the campaign has a coherent structure at all. The tool's job is to be a *container* for it: somewhere the depth can go productively, with a clear edge.

**Recall is strong.** Full character sheets reconstructed from memory an hour after creation — backgrounds, skills, stats, equipment choices. Major storylines from a two-year campaign retained without notes.

**Cognition is systemic, not visual.** Aphantasia: no mental imagery. Everything is held as processes, structures, and relationships rather than pictures.

Both of these change what the tool is for.

### The tool is not primarily an external memory

If recall is reliable, "I forgot" is not the failure mode being designed against. The failure is **"I couldn't have noticed."**

A campaign accumulates entities faster than any memory can cross-reference them. Remembering forty NPCs is achievable; noticing that three of them are related *and* the party has independently interacted with all three *and* one appears in next session's planned encounter is combinatorial, not mnemonic. No amount of good memory does that reliably under time pressure.

So the tool's value is **computation over what's already known**, not storage of what might be forgotten:

- Cross-referencing at a scale that exceeds working memory
- Detecting staleness — which projections rest on premises that have since changed
- Surfacing non-obvious intersections
- Guaranteeing coverage, so readiness is confirmed rather than felt

Retrieval speed still matters, but for a narrower reason: recall under time pressure at the table, mid-sentence, is different from recall in general. The tool covers the pressure case, not a deficit.

**Corollary:** the tool should not spend effort re-explaining things the GM already knows. Summaries of one's own campaign are noise. Show what changed, what's new, and what wasn't noticeable — not what's already held.

### Systemic representation is the native format

The graph model in [[Information-Architecture]] isn't an arbitrary structuring choice — it matches how this GM already thinks. Typed relationships, states, conditional branches, and derived views are the native encoding. That's a strong signal the direction is right, and a reason to keep the tool's *internal* representation structural rather than narrative.

Two consequences worth being deliberate about:

**Sensory description is not the native output, and the players want it.**
Locations and NPCs get encoded here as function, relationship, and mechanics. What a place *looks, smells, and sounds like* is a separate act of translation — and it's what makes the world feel real to the people at the table.

This makes descriptive text a genuine tool responsibility rather than decoration: hold sensory detail for locations and NPCs as prepared material, ready to read or paraphrase. The `READ ALOUD` convention already in use is exactly this, and its value is now explained rather than incidental. Worth extending beyond dialogue to place and person description.

**Whether visual outputs help is an open question, not a settled one.**
Aphantasia doesn't imply visual artifacts are useless — an external map may be *more* valuable precisely because there's no internal one to consult. But it does mean a graph visualization or a map is unlikely to feel like a shortcut to comprehension the way it might for someone who thinks in images.

Best treated empirically: build the structural views first, since those are certainly useful, and test whether visual ones add anything before investing in them.

### Preparedness needs a definition of done

Two failure modes, and they're the same failure. Feeling unprepared at the table is the worst outcome. Investing days in a branch the party never takes is also bad. Both come from **no reliable signal for when preparation is sufficient** — without which the only strategies are prepare-forever or accept-anxiety.

Readiness is a coverage question, not a depth question:

> Every live branch the party could plausibly take next session has *something* behind it.

That's checkable. Not "is this good enough" — unbounded, no answer — but "does every open path have a node," which terminates.

- **Coverage is the metric, depth is optional.** A branch with three lines behind it is covered. Making it excellent is a choice.
- **The tool should be able to say the words.** *You are prepared for the next session*, backed by what it checked. That sentence is the deliverable.
- **Prep beyond the covered set should be visibly optional** — marked elective rather than incomplete.
- **The `speculative` tier exists for exactly this.** Six held possibilities cost almost nothing; six authored encounters cost days.

### Reacting at the table is retrieval, not preparation

Deep preparation is often compensation for slow retrieval. If the right detail can be found in seconds mid-session, less needs pre-writing — improvisation is grounded in what's recorded rather than invented cold.

**Retrieval speed directly reduces required prep volume.** The corollary: an unanticipated choice stops being "I didn't plan for this" and becomes "can I reach what I already know while they wait."

---

## What this GM enjoys

Design targets, not incidentals. These are payoffs the tool should actively serve.

### Recounting events and revealing what was behind the screen

The debrief is part of the fun — telling the table what was really going on, what nearly happened, how close they came.

This adds a feature the rest of the design didn't anticipate. [[Arcs]] states that projections are never shown to players — **that's true only while they're live.** After resolution, the projection becomes the best possible debrief material:

> Here's what I thought you'd do. Here's what I'd built for the other branch. Here's the version where you didn't save him.

So speculative events and abandoned branches shouldn't be deleted when they go unused. They're the raw material for the reveal. A `revealed` state for retired projections would let them move from GM-only into shared history without losing the record of what was secret when.

### Storyline reveal and payoff

The moment a thread lands is the point of the arc tree existing.

The tool should support this actively:

- **Track what's ready to pay off** — arcs with sufficient buildup, foreshadowing that hasn't landed, questions raised and unanswered.
- **Track what's been set up but not yet used**, so nothing is accidentally left buried.
- **Record where a payoff landed**, so the shape of the campaign is legible afterward.

A payoff that never fires because it was forgotten is the specific loss worth engineering against.

---

## Recurring judgment calls

### Reaching Floor 6 without an established arc

Canon goes ambient at Floor 6 (see [[Canon]]). If the party has no thread of their own by then, they meet the loudest part of the world with nothing at stake personally.

**The call:** push forward and trust an arc to form under pressure, or deliberately slow the descent and let one develop first.

**Consider:** an arc forming *because* canon pressure arrived is a legitimate origin — threat can create investment as readily as affection. But it's a gamble, and the insulated floors won't come back.

### Pacing density

Too few connected events feels like a grind; too many feels like railroading (see [[Arcs]]).

**The call:** does the next session need to carry weight, or does it need to just be a dungeon?

**Consider:** the instinct to make everything matter is strong and usually wrong. A session that's purely tactical is not a wasted session — it's what makes the next meaningful one land.

### Letting a projection die

The GM has been building toward something and the table keeps walking past it.

**The call:** escalate until they notice, or accept that the thread isn't theirs and let it go.

**Consider:** an intended arc with no realized investment is a signal, not a failure of the players. Reading it as "they missed it" rather than "they weren't interested" leads to forcing. A dead projection is still good debrief material later.

### Spending an intersecting canon moment

Direct contact with canon events or characters is finite — too many and the party is following someone else's plot.

**The call:** is this the moment worth spending one on?

**Consider:** proximate almost always outperforms intersecting. The aftermath of something enormous is usually better than being inside it.

### Saying yes to a player invention

A player coins a name, asserts a detail, invents a rumor.

**The call:** absorb it as world fact, or gently set it aside.

**Consider:** absorbing it is how authorship becomes real (see [[North-Star]]). The bar should be low. Something that contradicts canon or an established arc is worth a conversation, not a silent overrule.

### Revealing versus holding

Information the party could learn now or later.

**The call:** reveal, or let the gap sit?

**Consider:** partial and without context is usually the most flavorful state. The gap between seeing something and understanding it is where the world feels largest.

### Enforcing a hard consequence

DCC runs on hard realities. A Major or Critical Fail lands, and the honest outcome is severe.

**The call:** apply it fully, or soften it?

**Consider:** softening consistently teaches the table that stakes aren't real, which eventually costs every future dramatic moment. But a consequence that ends a character the players are invested in is worth being deliberate about rather than dice-driven alone. The system's degrees of success exist so this isn't binary.

### Continuing to prepare past the covered set

Everything live has something behind it. The urge to keep going is present anyway.

**The call:** is this prep serving readiness, or serving the pull toward depth?

**Consider:** neither answer is wrong. Elective prep is a legitimate pleasure and often produces the best material — the point is knowing which one it is. Deepening a branch by choice is fine; doing it because readiness feels unconfirmed means the coverage check isn't being trusted, and that's the thing to fix.

---

## What the tool should never do

- **Decide any of the above.** Surface, contextualize, propose — never resolve.
- **Make the GM feel behind.** A dashboard of unresolved threads and undeveloped arcs becomes a guilt engine. Show what's useful now.
- **Leave readiness ambiguous.** If it can't say whether the next session is covered, it has failed at its primary job.
- **Treat elective prep as incomplete work.** Optional depth must look optional, or every session appears unfinished.
- **Re-explain what the GM already knows.** Summaries of one's own campaign are noise. Show what changed, what's new, what wasn't noticeable.
- **Remove uncertainty from the GM's own experience.** Some things should stay unknown until the table discovers them together.
- **Reduce prep to compliance.** Checklists that must be completed turn a creative act into paperwork.
- **Discard unused material.** Abandoned branches are debrief material and future reuse, not waste.
- **Optimize the story.** There's no correct campaign. The measure is whether four people had a good time.

---

## The measure

When evaluating anything — a feature, a session, a decision at the table:

> Did this help four people build a story together and feel something real while doing it?

Everything else is instrumental.
