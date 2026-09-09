---
type: design
status: draft
visibility: gm
tags: [capture, requirements, sessions]
---

# Session Capture

Resolves the capture question from [[Open-Requirements]] §2. This is the near-term deliverable — no interface is needed for it.

---

## Settled

- **The GM captures most content**, at least initially.
- **Interactions are recorded as facts that imply meaning**, not as judgments of significance.
- **Qualitative description is part of the fact.** How something was played is observable and worth recording.
- **The mechanism is templates plus this repo plus AI.** That is the tool for now.
- **No interface until the end of Floor 2** — roughly 4–6 sessions out.

---

## Describe manner; don't rate meaning

The temptation is a field like `significance: high`. It fails structurally: **an interaction's meaning is often not knowable when it happens.** A GM asked to rate significance in the moment will guess or flatten everything to medium.

But capture shouldn't be terse. The line:

| Record this | Not this |
|---|---|
| "Played it reluctantly, kept deflecting with jokes" | "This seemed important" |
| "Called them an asshole, said we should have shanked them" | "Significance: high" |
| "Went quiet, then changed the subject" | "Probably an arc" |
| "Adopted a formal register she hadn't used before" | "Emotionally invested" |

The left column is **observation of manner** — checkable, still true in ten sessions. The right is **interpretation of significance**, which should be derived later, not asserted now.

---

## Recurrence is the primary signal

Stronger than any single interaction: **did they come back to it without being prompted?**

A character questioned in Session 3 and complained about in Session 4 is a stronger signal than any one exchange, however heated. Repetition across time is investment that can't be explained by circumstance — the moment had passed, and they returned to it anyway.

This cuts across the layers below rather than sitting inside one. When Z complains about an NPC an hour later and says the party should have killed them, it doesn't much matter whether Sam said it in character or as himself. **The return is the evidence; the register is metadata.**

Practical consequence for write-up: note when something resurfaces, and note that it resurfaced *unprompted*. That second word does the work — an answer to a GM question isn't the same as raising it themselves.

---

## Investment includes antipathy

Early framing skewed positive — bonding, protecting, affection. That's half of it.

**Hatred is investment, and often the more durable kind.** Nobody nurses a grudge about something they don't care about. An NPC the party loathes is arc material on the same terms as one they love, and comes pre-loaded: if that NPC reappears, tension exists before anyone says a word.

So capture records valence but doesn't filter on it. What matters is that attention persists, not that it's warm. The signals are identical:

- Returning to the subject unprompted
- Arguing about how to handle them
- Remembering details about them
- Making plans that involve them

All of those fire for an enemy exactly as they do for a friend. A system that only looked for affection would have missed the best hook in the example that prompted this section.

---

## Three layers of signal

Secondary to recurrence, but worth distinguishing since they carry different weight.

### In-fiction — what the characters did

Spoke rather than fought, spared something, named an entity, gave away something valuable, returned somewhere unprompted, pressed someone on a specific topic.

### Table-level — what the players did

Asked about something unprompted; debated a choice before acting; remembered a detail the GM had half-forgotten; adopted a running joke; expressed relief, dread, or anger; made plans involving a specific entity.

**Usually the strongest of the three.** In-fiction action can be purely tactical — sparing an enemy may be strategy. Three players arguing for ten minutes about whether to go back for someone has no tactical explanation.

**And the one least likely to be captured.** A prose recap naturally records in-fiction action and manner, because that's what a narrative account *is*. Table-level facts require noticing something outside the story — a sigh, a glance between players, a topic raised again after the scene ended. It won't fall out of writing the recap; it needs a deliberate prompt at write-up.

### Roleplaying behavior — how it was played

Voice or register changes, especially from their usual. Emotional tone in character. Leaning in versus staying detached. Unusual care in describing their own actions. A choice that fit the character but cost them something. A choice that broke from how they'd played the character before — either a mistake or a development, and the difference matters.

---

## Investment in one's own character

A distinct signal worth tracking separately: a player reaching for their dossier background unprompted.

When Z's anger traces to the paternal-contempt thread, or Hilda reaches for the grifter register, that isn't investment in the NPC — it's investment in *their own character*. Foundational, and worth knowing early, because "the dossiers are landing" is a different question from "the world is landing."

---

## What a capture record needs

| Field | Purpose |
|---|---|
| Who | Character, or player if table-level |
| With what | Entity involved |
| What happened | Short factual statement |
| How | Qualitative description of manner, if notable |
| Layer | In-fiction, table-level, or roleplaying |
| Recurrence | Whether this resurfaced unprompted from an earlier session |
| Session | When |

The `how` field is optional and often where the value is. It's also the one that can't be reconstructed later — what happened is recoverable from consequences; how it felt in the room is not.

---

## Keep the write-up cheap

Capture happens after a session, when energy is low. Data entry doesn't get done, and inconsistent capture is worse than none — confident pattern detection over a biased sample.

- **A fact is one line**, plus a phrase of manner if there's something to say.
- **Omission is expected.** The signal survives sampling.
- **Prose recap stays.** Narrative and structured facts sit alongside each other.
- **Nothing is required.** A session with no interaction facts is a valid record.
- **Write manner in your own words.** No controlled vocabulary. Free text is the point.

---

## Why manner matters beyond inference

**The debrief.** Recounting what was behind the screen is far better with texture. "You all went completely silent" is what makes the retelling land.

**The callback.** A payoff hits hardest referencing *how* something happened. An NPC remembering that Hilda joked to cover her discomfort is sharper than one remembering she was present.

Texture degrades faster than structure. What happened is recoverable; the manner of it is gone in a week.

---

## Open

**Do player notes eventually contribute?**
A player writing "I hope the rat made it" is a self-reported table-level signal — possibly better than GM observation, since it needs no interpretation.

**Does the AI extract facts from the prose recap?**
Cheaper than writing both, but extraction can hallucinate and these become premises. Probably: propose, GM confirms. Manner descriptions are the riskiest — the most interpretive.

**How is recurrence recorded without re-reading old sessions?**
Noticing that something resurfaced requires remembering it surfaced before. Strong GM recall covers this early; at scale it may need support.

**How long until enough accumulates?**
Clustering needs volume. Four to six sessions may not produce detectable patterns — fine, since the interface isn't due until then.
