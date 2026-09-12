---
type: design
status: draft
visibility: gm
tags: [planning, process, prep, hooks, coverage, investment]
---

# The Planning Loop

How preparation actually runs: one iterative cycle, at two rhythms, with the GM owning when it stops.

Refines [[Prep-Rhythm]], which assumes a flat weekly cadence. Consumes [[Inference-and-Candidate-Relationships]] and [[Generative-Projection]]. Produces the [[Live-Set]].

---

## The cycle

1. **Search and read** — in Storyteller, and in external sources.
2. **Synthesize externally** — into a set of events, places, people. **This happens outside the tool**, per [[Modes-and-Surfaces]].
3. **Load** — the synthesised material enters through Record Plans, landing in a `planned` state with nothing revealed.
4. **Weave** — the system incorporates it into the store.
5. **Project** — the system analyses the new entities and surfaces what-ifs and candidate relationships.
6. **Review** — the GM edits, accepts, or rejects.
7. **Repeat**, until they sit down at the table.

**Step 6 feeds step 1.** An accepted what-if or relationship is input to the next iteration's analysis — the frontier model from [[Inference-and-Candidate-Relationships]], now running inside a planning cycle rather than once per session. See [[Generative-Projection]] on provenance chains thinning across iterations.

---

## One pipeline, two rhythms

**The steps are identical regardless of rhythm.** What varies is input, not process — consistent with Session Capture and Record Plans turning out to be one pipeline differing only in the state facts land in.

| | Regional pass | Weekly pass |
|---|---|---|
| Cadence | occasional, before a new region | between sessions |
| Output | broad, sparse, many entities | narrow, dense, few entities |
| Effort state | almost entirely `speculative` | promotes to `potential` |
| Fiction time | often unanchored | anchored to the next session |
| What the GM is doing | establishing a space of possibility | selecting from it and detailing |

**Effort is not consistent week over week**, and the design should not assume it is.

An honest name for the weekly pass is **selection and detailing** — most of what happens there is choosing what to promote, not inventing from nothing. The regional pass creates the material the weekly passes draw down from.

### The attention budget is per pass

The only thing that genuinely must vary. A cap sized for a weekly pass would throttle a regional session pointlessly; a cap sized for regional volume would flood a Tuesday evening.

**It is the GM's setting, not a mode the tool infers.** Simpler, and it avoids the tool guessing wrong about what kind of evening this is.

### Unanchored speculatives must be legal

*A smuggler operates somewhere in the eastern reach* has no place and no date yet. The regional pass produces these in bulk.

So a `speculative` entity must be storable with **no place relationship and no fiction time**, without being treated as an incomplete record. Otherwise the regional pass generates a hundred validation complaints and the GM stops using it.

### Signal volume will spike on regional passes, and that is correct

The regional pass produces exactly the conditions **parallel without contact** is tuned for: a large batch of thin, similar, unconnected entities arriving at once. It will fire hard there and stay quiet during weekly passes.

Stated here so the spike is not read as a defect. **The regional pass is when a GM most wants seams pointed out**, because they are building a web on purpose and have not yet decided how it hooks together.

---

## Hooks

**A hook is a fact meant to entice the players and build investment.** Not a model object.

A rumour is a **claim** with a speaker. An NPC statement is an **utterance**. A visible thing in a room is a **fact** about a place. All three already exist and already carry visibility. *Hook* names the GM's purpose in authoring a fact, not a class in the store — the same treatment as Zone and Floor in [[Glossary]].

**Recorded explicitly so a Hook class does not get added later.**

This consolidates rather than merely simplifies: a rumour the party may or may not chase is a claim with resolution `undetermined`, per [[Claims-and-Resolution]]. **The bait and the open claim are the same object.** The GM has not decided whether it is true and will not until the party bites.

Arc Intent stays distinct. A hook is a fact; **Arc Intent is the GM's aim in placing a set of them.** The fact is in the store; the intention about it is the separate thing, which is why Arc Intent was separated from Arc to begin with.

### Pull comes from the attachment point

**A hook's effectiveness is a property of what it attaches to, not of what it says.**

A rumour anchored to an entity at Notable investment or higher has traction. The same rumour about a place the party has never encountered is noise they walk past.

Investment already records this, so hook effectiveness is computable with nothing new.

### This refines Coverage

[[Glossary]] **Coverage** currently means having something prepared behind each direction the party might plausibly go. That treats all prepared material as equivalent, and it is not.

> **Five hooks on entities the party has never met is thin coverage, however many there are.**

Coverage is better stated as a claim about the **investment profile of the attachment points**, not a count of prepared things. It is also computable off unrevealed facts and open claims — no hook inventory required.

### The cold-start problem

Investment makes hooks work. Hooks are how investment gets built. **A new region starts at zero on both.**

The way out is already in the model: **attach the new region to what the party already cares about.** A rumour about the eastern reach lands if it comes from an NPC they trust, concerns a faction they have tangled with, or touches an open claim they are already chasing. The hook **borrows investment** from its speaker or its subject rather than needing its own.

This is **borrowed weight** from [[Inference-and-Candidate-Relationships]], arriving from the authoring side. Same mechanism: narrative weight is inherited, not intrinsic.

It makes the regional pass a specific task rather than a generic one — not *invent a region*, but **invent a region and find its attachment points into what already matters.** And that is detective work, not generative: the invested entities are known, the new entities are known, and the gap between them is precisely what parallel-without-contact detects.

**Ranking consequence:** a proposed connection into a high-investment entity is worth more than one between two unknowns. Computable, no tuning constant.

---

## Convergence is the GM's problem, not the tool's

The loop repeats until the GM sits down at the table. **That is the exit condition.** There is no stopping rule, and the tool must not invent one.

**A GM must plan more than will happen in a given session.** The balance is having enough without the effort eating the week — and no system can prevent a GM from planning a hundred events when they need five. That is a human problem. A tool that tried to enforce convergence would be the paternalism [[Premise-and-Pillars]] rules out, and it would be working against the thing the GM is actually managing: per [[GM-Considerations]], the standing anxiety is feeling **unprepared**, and overplanning is how that gets managed.

**Unused material is not waste.** It is the insurance premium, and some of it surfaces three sessions later anyway. `speculative` and `potential` exist so that unspent preparation stays cheap to hold.

### What the tool may legitimately do

**Make the cost visible, not the limit.** Same posture as options-not-recommendations: state what is true, let the human decide.

- *You have coverage on the three likely directions* — information.
- *Stop planning* — not the tool's to say.

One thing worth reporting that the GM cannot see unaided: the **`used`-to-`potential` ratio** across past sessions. A GM who knows they consistently use a fifth of what they write can calibrate. A GM who does not know it has no basis to calibrate at all. Readable off the effort states already tracked; reported, never judged.

### The obligations that remain the tool's

Not convergence, but not nothing. The tool must avoid making the loop feel **unfinishable**:

- **No regenerating queue.** A rejection must persist across iterations *within* a pass. If a what-if rejected on iteration one reappears on iteration three, the loop is hostile. The resurface-only-on-new-evidence rule has to hold here, where evidence changes every iteration by design.
- **No completeness meter.** Nothing that implies a target the GM is falling short of.
- **The signal should quiet on its own.** By iteration four the GM has added substance, so obstruction is up and parallel-without-contact naturally fires less. **If it does not quiet, that is a bug** — it means the signal is firing on material it just helped create, which is the confirmation-bias failure inside a single evening.

**Absence of pressure, rather than presence of a stopping rule.**

---

## Open

1. **Does externally synthesised material carry usable provenance?** The GM reads source books, other tools, and their own notes, then loads a synthesised set. Some is canon with a citation; some is GM invention. By the time it has been synthesised externally the distinction may be lost — which matters for supersession detection in [[Canon]].
2. **Is the per-pass budget a setting, a preset, or both?** Two named presets would be less friction than a number, at the cost of the tool implying what kind of pass this is.
3. **Does the `used`-to-`potential` ratio survive contact with reality?** Material prepared for session 12 and used in session 15 is not waste, and a naive per-session ratio would call it that.
