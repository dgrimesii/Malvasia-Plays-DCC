---
type: design
status: draft
visibility: gm
tags: [intake, extraction, capture, planning, mechanics, scope]
---

# Extraction Rules

How the system finds the narrative content inside a document that also contains other things.

Consumed by Epic 1 (stage 1 of intake), Epic 5 (outside material), and Epic 13 (conversion). Depends on [[Claims-and-Resolution]] for the speaker rule and [[Scope]] for the mechanics boundary.

---

## Two input shapes, not one

[[Session-Capture]] specifies intake against **rough notes**: scrappy, narrative, written from memory after play. The parser's job there is to give shape to something that is already narrative.

**Planning documents are a different problem.** A GM's floor plan or session prep is dense, structured, and mixed — party roster, beats to run, verbatim read-aloud, achievement text, encounter math, floor modifiers — with nothing marking which is which. Here the parser's job is to **find the narrative inside the larger thing**.

Same two-stage intake, same review, different failure modes. The rules below are mostly about the second.

---

## The subject test

The practical question is not about vocabulary. It is about what a sentence is *about*.

> **Does this assert something about a person, a place, or an event?**
>
> If yes, it is a candidate.
> If it tells the GM what to do, or tells the system how to resolve something, it is not.

This resolves the common case where both appear in one sentence. *Remind the table that every artificial roof on Earth pancaked simultaneously* fails the test on its face and passes on its content: the instruction is discarded, and the world fact survives.

---

## Three mixture types

All three appear in a single real planning document. Each needs different handling, and a parser that treats them alike will get two of them wrong.

### 1. Mechanics as configuration — discard

Encounter math, floor modifiers, difficulty scaling. These tell you how to run something.

Per [[Scope]], resolution machinery is out in all three pillars. Nothing is lost by discarding it: a floor modifier that is derivable from the floor number stores nothing the floor number does not already carry.

### 2. Narrative wearing mechanical clothing — extract carefully

The hard case, because both kinds sit in one line. *Cryomancer / Tactician, Frost Scar, 6 Mana* contains:

- **Class and named ability** — facts about a character. A named ability is narrative: per [[Scope]], *Frost Scar leaves a lingering chill* shapes how a scene is described.
- **Mana count** — configuration. Out.

The rule is not *mechanics out*. It is that the line has to be split rather than taken or dropped whole.

### 3. Instruction versus content — split, discard the instruction

The sharpest type, and it is everywhere in a plan.

| | Example shape | Handling |
|---|---|---|
| **Stage direction** | *Go around the table and have each player describe…* | Discard. It is a direction to the GM |
| **World content** | *…out back of her newly leased restaurant* | Extract. It is a fact about a character |

A parser reading the whole bullet as narrative **records the instruction as though it happened.** That is the characteristic failure of this input shape.

---

## Numeric values

Not *numbers are out*. Three cases.

**Narrative when descriptive of something that occurred.** *The event had eleven enemies* is a fact about an event: it has a subject, it is true or false, and it is not an input to anything. Extract it.

**Procedural when it configures play.** *Weak = 2 Mobs* is a rule for populating a fight. Discard.

**Implied significance is the GM's to state, never the parser's to derive.** This is the one an implementer will get wrong, because outlier detection is easy and looks helpful.

An enemy at +5 among others at +2 does carry a narrative implication — *this one was notably more dangerous.* But that implication lives in the **comparison**, not in the number, and making it is a judgment. The document says +5; *therefore this one was a threat* is interpretation the source never asserted.

Inferring significance from a statistical outlier is the same move as inferring emotional state from a description, and [[Constraint-Manner-and-Intent]] prohibits it for the same reason. It also degrades quietly: the system decides an enemy mattered because its number was high, and that becomes a fact in the record nobody asserted.

**So the GM records the observation and the number stays out.** *The party faced something notably stronger than anything else on the floor* is a narrative fact with a clear subject — and it is the form a callback actually uses, since an NPC does not say *the modifier was five*.

### Never narrativise a value

Holds regardless of whether the value should have been stored.

Turning *+1 Floor Stat Modifier* into *the Warrens are dangerous* invents an interpretation, loses the original, and is unfalsifiable afterward. If a value is extracted it is stored as a value. If it is not extracted it is discarded. **It is never paraphrased into prose.**

---

## Everything from a planning document lands planned

A planning document describes what is **intended**. Nothing extracted from one is a fact about the world yet.

Per [[Planning-Loop]], these arrive through Record Plans: facts land `planned`, events land `planned`, nothing is revealed. The instruction layer is discarded outright rather than converted into anything at all.

Consequence for review: a proposal from a planning document and a proposal from a recap look similar and mean different things. The review has to show which it is.

---

## Synthesis artifacts

External synthesis leaves residue. The current Gemini pass emits citation scaffolding — bracketed span markers interleaved with the prose — which carries no campaign meaning and must be stripped before extraction.

The specific artifact will change whenever the upstream tool does. **The general requirement is that intake tolerates and removes formatting residue from whatever produced the document**, and reports what it stripped rather than silently swallowing it.

---

## What the speaker rule looks like here

[[Claims-and-Resolution]] requires that a proposition with a source attaches to the speaker. Planning documents contain **verbatim read-aloud text**, which is the purest form of this — quoted lines with a named speaker, written before they are ever said.

Two consequences:

- The line is a `planned` **utterance**, not a fact about the world and not yet an utterance that happened. It becomes one when a session records it being said.
- **Its content is frequently false.** Mocking or taunting announcements make claims about the characters that are not true. Flatten them and the record asserts, in its own voice, things the campaign never established about a player's character.

This is the [[Claims-and-Resolution]] failure at its most concrete, and the existing repo content already contains instances of it.

---

## Ambiguity is raised, not resolved

Where a line cannot be classified confidently, it is queued for a decision rather than guessed in either direction — the mechanism Epic 13 S4 already provides for conversion, applied to intake generally.

Both directions cost something. A discarded fact is invisible; an extracted instruction is a false record. Neither is recoverable by inspection afterward, which is why the queue exists.

**A useful default while the rules are unproven:** treat a numeric value as procedural unless the GM says otherwise. Cheap to override in review, and it fails toward omission rather than toward inventing content.

---

## Open

1. **Does the subject test survive contact with real documents,** or does it need per-type refinement? It has been checked against one planning document. That is not enough.
2. **Are planning documents a separate acceptance path in Epic 1 S12,** or wholly Epic 5's? S12 assumes rough notes and its criteria were written for them.
3. **Does anything in this game system read as a durable numeric property** of a place or person, rather than an input to resolution? Nothing found so far — every numeric value examined turned out to be procedure. If that holds generally, the default above becomes stronger than a default.
4. **How is verbatim read-aloud text held before it is said?** A `planned` utterance is a shape neither [[Claims-and-Resolution]] nor [[Off-Screen-Events]] currently describes, and it is common in prep.
