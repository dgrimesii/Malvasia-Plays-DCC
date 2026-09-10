---
type: design
status: draft
visibility: gm
tags: [capture, ai-boundaries, constraint, provenance]
---

# Constraint: Manner, Intent, and Inference

**Hard rules, not preferences.** Referenced from [[Session-Capture]] and [[Open-Requirements]] §3.

Two related constraints: what the AI may never generate, and how anything it does generate must be marked.

---

## Part 1 — Manner and intent are human-authored

The AI must never generate, infer, or embellish:

- **Manner** — how something was played, said, or done
- **Intent** — why a player or character did something
- **Emotional state** — what anyone at the table felt
- **Engagement** — how invested someone was

These come only from **real input**: what the GM wrote, or what a player wrote in their own notes.

### Why this is stricter than the general hallucination rule

A hallucinated NPC is a false statement about fiction — a data error, correctable, and nobody is misrepresented.

**Manner and intent are claims about real people.** "Amy seemed reluctant" is a statement about Amy. Generated from nothing but the fact that Hilda hesitated in a scene, it's a fabricated observation about a person who was in the room.

That error is worse in three ways:

1. **Unfalsifiable in retrospect.** Nobody can check what the room felt like six months later. A wrong NPC name gets caught; a wrong emotional read never does.
2. **It propagates into how people get treated.** Investment inference feeds arc formation, which determines what material gets aimed at whom. A fabricated read on a quiet player produces real consequences for that player's experience.
3. **It corrupts the signal it claims to measure.** The point of capturing manner is that it's observed. Generated manner is evidence of nothing but the model's priors about how people behave.

### Permitted

- **Reorganizing what the GM wrote.** Moving a manner description from prose into a structured field, verbatim or lightly condensed. The observation stays the GM's.
- **Quoting player notes.** "I was furious he wouldn't answer" is real input. Paraphrasing it to "the player was frustrated" is already drift.
- **Asking.** *"Was there anything notable about how that was played?"* is the correct behavior — it elicits real input rather than substituting for it.
- **Flagging absence.** "No manner recorded" is true. "This appeared routine" is not.

### Forbidden

- **Inferring manner from events.** "Z pressed for direct answers" must not become "Z pressed angrily." Plausible is not observed.
- **Filling blanks because a field exists.** An empty manner column is correct output.
- **Inferring intent from action.** "Hilda used persuasion" does not license "Hilda was trying to smooth over Z's aggression" — even if obvious, even if right.
- **Reading engagement from behavior.** Expressiveness varies by person and says nothing about investment.
- **Narrative embellishment in recaps.** A summary describes what happened; it doesn't add texture the GM didn't supply.

---

## Part 2 — Inferences are labeled as inferences

Everything the AI derives — even from perfectly good human input — is marked as inferred **at the moment it's created**, not at the moment it's approved.

### Acceptance does not convert an inference into a fact

If the GM approves "these three NPCs form a thread," the record now contains an **accepted interpretation**. That is not the same as an observation, and the difference must survive.

Why it matters later:

- **Premise decay depends on it.** When an underlying fact changes, everything inferred from it needs re-examination. That's only possible if inferences are identifiable years after the fact.
- **Audits need it.** "Show me everything derived rather than recorded" is the fastest route to finding where a bad assumption took root.
- **Confidence is not provenance.** A strongly-supported inference is still an inference. Strength of evidence and kind of origin are separate properties and shouldn't be collapsed.
- **Approval happens under time pressure.** A GM accepting a proposal mid-prep hasn't verified it to the standard of something they watched happen.

### What must be recorded with an inference

| Field | Purpose |
|---|---|
| Origin | Inferred, not observed |
| Supporting evidence | Links to the specific facts it was drawn from |
| Chain depth | Whether it rests on other inferences, and how deep |
| Status | Proposed / accepted / rejected |
| When | Which batch produced it |

**Chain depth is the one most likely to be skipped and most likely to matter.** An inference resting on an inference is materially weaker than one resting on recorded facts, and the difference is invisible unless tracked. Two or three layers deep, a conclusion can look well-supported while resting on nothing anyone observed.

### It renders distinctly, everywhere

Consistent with the faithful-rendering requirement in [[Interface-Direction]]:

- Inferred edges never draw the same as recorded ones — in any view, at any zoom level.
- Zooming out may drop an edge's label; it must not drop the fact that the edge was inferred.
- Text views mark it too. This isn't only a visualization concern.

### What this doesn't restrict

Inference itself. Investment clustering, arc proposals, connection-finding, gap detection, continuity checking — all remain fully in scope.

The constraint is on **labeling**, not on reasoning. An inference clearly marked as one, with its evidence attached, is exactly what the tool should be producing.

---

## The general shape

**Facts in, patterns out, never feelings in — and always say which is which.**

| Kind | Origin | Can be checked against |
|---|---|---|
| Observation | GM or player recorded it | What happened |
| Inference | AI derived it | The facts it cites |
| Accepted inference | AI derived it, GM approved | The facts it cites — *not* what happened |

The third row is the one that erodes if unmarked. It looks like the first row and behaves like the second.
