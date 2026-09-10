---
type: design
status: draft
visibility: gm
tags: [capture, ai-boundaries, constraint]
---

# Constraint: Manner and Intent Are Human-Authored

**A hard rule, not a preference.** Referenced from [[Session-Capture]] and [[Open-Requirements]] §3.

---

## The rule

The AI must never generate, infer, or embellish:

- **Manner** — how something was played, said, or done
- **Intent** — why a player or character did something
- **Emotional state** — what anyone at the table felt
- **Engagement** — how invested someone was

These come only from **real input**: what the GM wrote, or what a player wrote in their own notes.

---

## Why this is stricter than the general hallucination rule

A hallucinated NPC is a false statement about fiction. It's a data error — correctable, and nobody is misrepresented.

**Manner and intent are claims about real people.** "Amy seemed reluctant" is a statement about Amy. If the AI generated it from nothing more than the fact that Hilda hesitated in a scene, it is a fabricated observation about a person who was in the room.

That error is worse in three ways:

1. **It's unfalsifiable in retrospect.** Nobody can check what the room felt like six months later. A wrong NPC name gets caught; a wrong emotional read never does.
2. **It propagates into how people get treated.** Investment inference feeds arc formation, which determines what material gets aimed at whom. A fabricated read on a quiet player produces real consequences for that player's experience.
3. **It corrupts the signal it claims to measure.** The whole point of capturing manner is that it's observed. Generated manner isn't evidence of anything except the model's priors about how people behave in scenes.

---

## What is permitted

**Reorganizing what the GM wrote.** Moving a manner description from prose into a structured field, verbatim or lightly condensed, is fine. The observation is still the GM's.

**Quoting player notes.** A player writing "I was furious he wouldn't answer" is real input. Using it is fine; paraphrasing it into "the player was frustrated" is already drift.

**Asking.** Prompting *"was there anything notable about how that was played?"* is not just permitted — it's the correct behavior. It elicits real input rather than substituting for it.

**Flagging absence.** "No manner recorded for this interaction" is a true statement. "This appeared routine" is not.

---

## What is forbidden

**Inferring manner from events.** The GM wrote "Z pressed for direct answers." The AI must not render this as "Z pressed angrily." Anger is plausible; plausible is not observed.

**Filling blanks because a field exists.** An empty manner column is correct output. Populating it is manufacturing.

**Inferring intent from action.** "Hilda used persuasion" does not license "Hilda was trying to smooth over Z's aggression" — even if it's obvious, even if it's right. If the GM meant that, the GM writes it.

**Reading engagement from behavior.** Especially forbidden given that expressiveness varies by person and says nothing about investment (see [[Session-Capture]]). The AI has no basis for judging whether a flatly delivered line was disengagement or that player's normal register.

**Narrative embellishment in recaps.** If asked to summarize a session, the summary describes what happened. It does not add texture the GM didn't supply.

---

## Where the line sits

| AI may | AI may not |
|---|---|
| Restate GM-written manner in a structured field | Generate manner from events |
| Ask what was notable | Assume what was notable |
| Report that nothing was recorded | Characterize an unrecorded interaction |
| Cluster explicit signals into a proposed pattern | Invent a signal to complete a pattern |
| Note that a player returned to a topic | Interpret why they returned to it |

That last row is the general shape: **observation of behavior is derivable from the record; interpretation of interior state is not.**

---

## Relationship to inference generally

This doesn't prohibit inference. Investment clustering, arc proposals, and connection-finding all remain in scope — they operate over *recorded facts* and produce *proposals the GM approves*.

The constraint is on the inputs, not the reasoning. An arc proposal built from "the party returned to this NPC three times" is sound. One built from "the party seemed to care about this NPC" is built on a fabrication, and every conclusion downstream inherits it.

**Facts in, patterns out. Never feelings in.**
