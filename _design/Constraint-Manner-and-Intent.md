---
type: design
status: draft
visibility: gm
tags: [capture, ai-boundaries, constraint, provenance]
---

# Constraint: Manner, Intent, and Provenance

**Hard rules, not preferences.** Referenced from [[Session-Capture]] and [[Open-Requirements]] §3.

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

Worse in three ways:

1. **Unfalsifiable in retrospect.** Nobody can check what the room felt like six months later. A wrong NPC name gets caught; a wrong emotional read never does.
2. **It propagates into how people get treated.** Investment inference feeds arc formation, which determines what material gets aimed at whom. A fabricated read on a quiet player produces real consequences for that player's experience.
3. **It corrupts the signal it claims to measure.** The point of capturing manner is that it's observed. Generated manner is evidence of nothing but the model's priors.

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

## Part 2 — Proposals are marked while pending; acceptance makes them fact

Keep this light.

**Before acceptance:** anything the AI derives is visibly a proposal, with the facts it was drawn from attached so the GM can judge it. Unaccepted proposals never render as established — in text or in any view.

**On acceptance:** it becomes a fact and is treated as one going forward. The GM's decision is what elevates it. No separate tier, no confidence scores, no chain-depth tracking.

**Provenance persists as a small tag** noting it was AI-generated. That's all it needs to do — enough to answer "show me everything the system produced during that integration" when cleaning up after a bad batch. It carries no ongoing weight and shouldn't affect how the fact is displayed or reasoned over.

### What this trades away

Automatic re-examination when an underlying fact later changes. If an accepted inference rested on something that turns out wrong, nothing will flag it on its own.

That's an acceptable cost here: one GM, one campaign, strong recall, and the provenance tag still supports manual audit. Worth revisiting only if it actually bites.

---

## The shape

**Facts in, patterns out, never feelings in.** Proposals are visible as proposals until you accept them; after that they're just facts with a note about where they came from.
