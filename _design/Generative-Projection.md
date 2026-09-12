---
type: design
status: draft
visibility: gm
tags: [generation, inference, planning, capture, investment, constraint]
---

# Generative Projection

Where the system is permitted to propose fiction that has not happened, and why that does not contradict [[Constraint-Manner-and-Intent]].

Companion to [[Inference-and-Candidate-Relationships]], which stays purely detective. Operates inside the cycle described in [[Planning-Loop]].

---

## This revises an earlier position

[[Inference-and-Candidate-Relationships]] frames the whole feature as detective: the system proposes *these two may be connected* and nothing more. That remains correct for inference.

It is not sufficient as a description of the product. **If the entire burden of imagining what could be falls on the GM, the tool has not done its job.** A GM planning an NPC the party may never meet will not invest in a deep backstory, and should not have to. That thinness is rational, and it is exactly where help is worth having.

So generation exists. What follows is the line it may not cross.

---

## The line: forward, never backward

> **Generating forward into fiction that has not happened is permissible. Generating backward over what happened at the table is prohibited.**

[[Constraint-Manner-and-Intent]] prohibits the second, and its stated reason is the right one: an invented emotional read is a **false memory of a real person's behaviour.**

An invented apprenticeship for an NPC nobody has met overwrites nothing. There is no human experience being displaced, because there is no experience yet. The prohibition is about the people in the room, not about invention as such.

### Where this lands in the modes

Per [[Modes-and-Surfaces]]:

| Mode | Generation |
|---|---|
| **Table play** | Prohibited. Read-only, and [[Constraint-Serves-The-Table]] forbids anything that competes with the conversation. |
| **Session Capture, stage 1** — extraction | **Prohibited absolutely.** Only what was said, who said it, what happened. No invention touches the record of real people in a room. |
| **Session Capture, stage 2** — impact detection | **Permitted.** See below. |
| **Session Planning** — Record Plans | **Permitted.** |

---

## Stage 2 is stitching, and it is still forward-looking

The apparent exception is not one. Stage 2 does not generate anything *about* the session that happened — it takes the accepted facts as input and projects what they now make **possible**.

> The weft has just crossed the warp. Stage 2 asks what thread is needed for the new row to hold.

A session generates facts the GM did not plan. The party did something unanticipated, and there are now loose ends nobody intended. **This is where imagining what-could-be is hardest and least prepared for** — the GM is reacting rather than designing. It is the forced beat from [[Live-Set]], arriving a week early instead of mid-sentence.

**Stitching rather than bridging**, deliberately. A bridge joins two fixed points. Stitching implies the fabric on both sides takes tension: the new fact must be reconciled with what is already there, and patching it in may require material that does not exist yet. The invented apprentice master is not a connection between two NPCs — it is **a thread invented to hold a seam.**

### A what-if is a ticket type, not a new stage

Impact detection already asks *what do these facts imply* — candidate relationships, arcs forming, investment shifts, supersessions. *This new fact makes this other thing possible* is the same question with a generative answer rather than a structural one.

So it inherits, for free: the attention budget, dismissibility, and the no-confidence-score rule from [[Glossary]] **Ticket**.

### Why stage 2 is the primary home

Timing. Stage 2 runs immediately after the session, while the GM's sense of what actually landed is sharpest and before the week's distance sets in. A what-if evaluated then is judged against a fresh reading of the table. The same proposal offered on Thursday gets a worse judgment.

Record Plans generation is secondary — real, but operating on colder information.

---

## Entry state: speculative. Nothing new is needed.

A generated what-if is **not a fact.** It enters at `speculative` on the effort ladder in [[Glossary]] — the state already defined for a possibility held cheaply.

- `speculative` — generated, or sketched. Cheap to hold, cheap to drop.
- `potential` — the GM developed it. Now authored material.
- `used` — play touched it.

**A generated proposal the GM ignores decays by doing nothing.** It does not require rejection, does not become a task, and does not accumulate into a backlog — consistent with the rejected-candidate rule in [[Inference-and-Candidate-Relationships]].

---

## Investment gates generation — inverted

**The mechanism that distinguishes filling a void from displacing an author.** Everywhere else in the design, higher investment raises the bar for surfacing. Here it lowers it.

| Degree of investment | Generation posture |
|---|---|
| **None / Minor** | **Generate freely.** The GM was not going to write this. Nothing is taken from them. |
| **Notable and above** | **Do not offer backstory.** Here the GM *does* want to write it, and generating it steals the part of the job they do for pleasure. |

Same field, opposite direction. This is not a heuristic — it follows directly from the argument that justifies generation at all. The reason help is welcome is that the GM has chosen not to invest. Where they have invested, the reason evaporates.

---

## Guardrails

### Offer several, never one

A single proposal **anchors**. The first idea presented becomes the idea, and that is autonomy subtracted — see [[Premise-and-Pillars]] on autonomy as the one need the tool can take away.

Three divergent what-ifs expand the space. One narrows it. This is the generative analogue of **options, not recommendations** in [[Live-Set]].

### Voice homogenisation is the real cost, and it is invisible per instance

Generated backstories converge on tropes. Over fifty sessions the cast begins to rhyme. **No single proposal looks wrong. Only the aggregate does.**

Mitigation is not a better prompt. It is measurement: a periodic report of how much of the record arrived by generation, which the provenance below already supports. Same shape as the confirmation-bias coverage report in [[Live-Set]] — a fact reported, not a judgement made.

### Grounded, not free invention

Generation reads from the store: the existing facts, the shared typed attributes, the invested concepts, the open claims. It proposes a stitch across a detected seam. **The detective layer finds the gap; the generative layer proposes thread.**

This also preserves what matters architecturally: the nondeterministic component is never in the detection path, so the **golden corpus stays replayable.** See [[Inference-and-Candidate-Relationships]] §Procedural and generative.

---

## Provenance: three kinds, and chains get thin

[[Glossary]] **Provenance** must distinguish:

1. **GM-authored** — invented outright by the GM.
2. **Inference-accepted** — detected, then accepted.
3. **Generated-accepted** — proposed by generation, then accepted, possibly edited.

This matters because the [[Planning-Loop]] is iterative: **an approved what-if becomes input to the next iteration's analysis.** That is generative output feeding generative input, and it compounds more sharply than the inferred-edge chain the inference doc already worried about, because the material is invented rather than detected.

The protection is the same and requires no estimation: **a what-if resting on a chain of prior what-ifs is thinner than one resting on table facts, and the chain is readable.** A ticket shows the path it walked, including the provenance of each hop.

---

## What this does not do

- **No generation in extraction.** Stage 1 is testimony. Absolute.
- **No manner, intent, or emotional state**, ever, in any mode. [[Constraint-Manner-and-Intent]] is untouched by this document.
- **No generated content entering the record without acceptance.**
- **No single recommendation.** Several or none.
- **No backstory for entities the GM has invested in.**
- **No generation at the table.** [[Constraint-Serves-The-Table]].

---

## Open

1. **How many proposals is "several"?** Three is the working assumption. Needs a number in acceptance criteria, and it interacts with the attention budget.
2. **Does divergence need enforcing?** Three proposals that are variations on one idea are worse than one proposal, because they create an illusion of choice. Whether divergence can be checked procedurally is unknown.
3. **What is the homogenisation report actually measuring?** Share of record by provenance is easy. Whether that correlates with the cast rhyming is unverified.
4. **Does an edited generated proposal stay generated?** Parallel to the same open question about inferred edges. Probably yes, with the edit recorded.
