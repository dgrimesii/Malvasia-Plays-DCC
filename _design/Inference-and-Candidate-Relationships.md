---
type: design
status: draft
visibility: gm
tags: [inference, relationships, tickets, model]
---

# Inference and Candidate Relationships

How the system proposes a connection it was never told about, and how the GM's judgment stays in charge of it.

Companion to [[Information-Architecture]], [[Session-Capture]], and [[GM-Considerations]]. Supplies the mechanism behind **Ticket** and **Signal** in [[Glossary]]. Implemented by Epic 6, in RC 1c.

---

## What is being inferred

**A relationship between two entities.** Not a fact, not a story beat, not a motive. The system's whole claim is *these two things may be connected, and here is why I think so.*

That keeps it on the right side of the surfacing-versus-authoring line, which is still an open decision gating RC 1c. Proposing a connection extends what the GM can notice. Proposing what the connection means would be authoring.

---

## Attributes are weak evidence; structure is strong

The tempting first design is matching on shared properties. Two NPCs both favour yellow; the setting contains a Cult of the Yellow King; therefore raise a ticket.

**This is mostly wrong, and the reason is about authoring rather than statistics.** A GM who invents an NPC bearing the cult's tattoo will almost always record the membership at the same time. Deliberate authoring leaves few coincidences worth finding, and shared descriptive attributes — hair colour, home town, a favoured drink — are common enough that matching on them produces noise at volume.

**But the argument has a boundary, and the value sits exactly at it.** Attribute coincidence is worth examining in three cases, all identifiable from data the record already holds:

- **The fact came from play, not authoring.** The GM improvised a mark on the innkeeper's wrist mid-scene and it arrived through intake. Nobody designed it against anything.
- **The fact predates the concept.** The tattoo was described in session 3; the cult was invented in session 20. Both were authored correctly, and the connection could not have existed at the time. **This is the strongest case**, and the one a person reliably misses, because catching it means remembering session 3 while writing session 20.
- **The fact came from an external author.** Canon import, where nobody was linking anything to this setting.

So the filter is **provenance and chronology**, not a similarity score. A GM-authored fact newer than the concept it matches is low value and should usually stay quiet. Anything else is worth a look.

### Structural signals

Stronger, and all readable off the graph without a tuned prior:

| Signal | What it is |
|---|---|
| **Unexpected density** | Two entities joined by more independent paths than the graph's own baseline |
| **Convergence** | Several otherwise unrelated threads landing on the same entity |
| **Co-occurrence without connection** | Two entities appearing in the same sessions repeatedly with no recorded link |
| **Borrowed weight** | A coincidence landing on a concept the setting has invested in — the cult, not the colour |

Borrowed weight is worth stating plainly: **narrative weight is inherited, not intrinsic.** Yellow is not interesting. Yellow is interesting because something in the setting made it load-bearing, and [[Glossary]]'s **Degree of investment** already records which concepts those are. A coincidence touching a Notable or Deep entity is worth more than the same coincidence touching nothing.

---

## Acceptance is the trigger

Inference does not sweep the graph. **It expands from the frontier: when a relationship is accepted, the neighbourhood it opens is examined.**

Once a connection from A to B is established, B's existing relationships become worth checking against A's facts. The new edge is a doorway, and what lies beyond it has never been compared to A before.

This is bounded work rather than a global scan, it is well targeted, and it fits the write-once-per-session rhythm — acceptance happens during intake, which is when the examination runs.

### Distance is a hard limit, not a gradient

**Two hops from the accepted edge. Full stop.**

Proximity does carry value — a candidate one hop out is stronger than one two hops out — but expressing that as a decaying score would require a tuning constant with nothing to justify it, and a large graph still produces enormous numbers of weak distant candidates that sum to noise. A stated cutoff is defensible where a decay curve is not.

### Inferred edges can be walked, with their provenance visible

An accepted-but-inferred relationship is a legitimate hop for the next inference. That is what makes the frontier model work at all.

It also compounds error: a wrong acceptance becomes evidence for the next candidate, which becomes evidence for the one after. Two protections, both using what the model already has:

- **Provenance distinguishes authored from inferred-then-accepted.** A chain resting entirely on inferred edges is weaker than one resting on authored ones. That is read, not estimated.
- **The ticket shows the path it walked.** Not a confidence number — the actual route: *A connects to B, B knows C, and A's facts mention C's home village.* This follows [[GM-Considerations]] and Epic 3's rule that a claim never appears as a bare verdict. A bad chain becomes visible rather than hiding behind a score.

---

## The candidate relationship

**The durable unit is not the ticket. It is the candidate relationship.**

A candidate is a standing proposal that two entities are connected, holding the **clues** accumulated for it. It persists across sessions and grows as evidence arrives. The ticket is only the notification that a candidate is worth looking at now.

**Inference justification: the more clues, the stronger the inference.** One coincidence is weak. The same pair turning up through a shared session, a converging thread, and an attribute landing on an invested concept is a different proposition — not because any clue got stronger, but because there are more of them.

This is the same shape as **Investment** in [[Glossary]], and deliberately so. Signals accumulate; the system surfaces; the GM decides. Clues accumulate; the system surfaces; the GM decides. Neither computes a verdict.

### Acceptance and rejection

**Accept** creates the relationship, with provenance recording that it was inferred and accepted rather than authored. It also opens a new frontier, per above.

**Reject clears the item from the GM's view.** The candidate does not remain as a task, does not appear in any backlog, and is not browsable. The GM's list holds only live candidates.

**A rejected candidate resurfaces only when a new clue is detected for that same relationship.** Not on a timer, not on review, not because the GM asked to see old ones. New evidence is the only trigger.

That is what makes repeated surfacing legitimate rather than nagging. Each appearance answers a different evidence set. [[GM-Considerations]] warns that reflexive dismissal is the failure mode for this whole feature — and the protection is not a cap on how often something may appear, but the rule that nothing appears without cause.

**When a candidate resurfaces, the earlier rejection is shown with it** — what was rejected, and on what evidence. Otherwise the GM evaluates the full clue set cold and may rule out the same clues twice without realising they have seen them.

---

## Generate freely, gate hard

The set of things that can *produce* a candidate should stay open. Triggers will be various, and constraining them early forecloses the discoveries that justify the feature.

**What gets shown is a different question.** An unbounded generator over a connected graph produces combinatorially many low-weight candidates, and flooding is not a mild failure — [[Backlog-Readiness]] §G4 is explicit that an untuned threshold does not merely underdeliver, it teaches the GM to ignore the feature permanently. That damage does not reverse.

So: broad generation, conservative surfacing, and the [[Glossary]] **Golden corpus** as the record of what the GM judged worth seeing.

---

## What this does not do

- **No confidence numbers shown to the GM.** The evidence is the explanation. A percentage invites arguing with a number instead of looking at the clues.
- **No automatic creation.** Nothing becomes a relationship without acceptance, per [[Constraint-Manner-and-Intent]].
- **No proposing what a connection means.** The candidate says *these may be connected*. What it signifies is the GM's.
- **No browsable dormant set.** Rejected candidates are invisible until new evidence arrives. A list of everything ever proposed is a backlog the GM will never clear, and a tool that makes its user feel behind stops being opened.

---

## Deliberately deferred

**Relationship-type rules.** *Members of this cult bear this tattoo* is a property of the relationship type rather than of any instance — an inference rule the GM authors, converting a coincidence into a testable implication. Genuinely more powerful than statistical matching, and genuinely scope creep: it is a rules layer the GM has to build and maintain, and [[Scope]] is hostile to rules layers for good reasons.

Recorded here so it is a decision rather than an omission. Not part of Epic 6.

---

## Open questions

| Question | What it blocks | Where it sits |
|---|---|---|
| Where does the surfacing-versus-authoring line sit? | All of RC 1c | The standing blocker on this epic. This document assumes the conservative answer — connections only |
| What is the baseline against which density counts as unexpected? | The density signal | Needs a stated basis, however crude. Likely refined by observation rather than decided in advance |
| Does a clue expire? | Nothing yet | A co-occurrence from forty sessions ago may be weaker than one from last week — or may not. Answer after use |
| Is an inferred-and-accepted edge ever promoted to authored? | Nothing yet | Provenance says how it arrived. Whether the GM editing it changes that is a small question with no current consequence |
