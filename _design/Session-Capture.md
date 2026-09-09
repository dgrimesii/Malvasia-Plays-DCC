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

The temptation is a field like `significance: high`. It fails for a structural reason: **an interaction's meaning is often not knowable when it happens.** The rat mattered only once it reappeared in peril, sessions later. A GM asked to rate significance in the moment will either guess or flatten everything to medium.

But that doesn't mean capture should be terse. There's a clear line:

| Record this | Not this |
|---|---|
| "Played it reluctantly, kept deflecting with jokes" | "This seemed important" |
| "Spent several minutes describing how she cleaned the knife" | "Significance: high" |
| "Went quiet, then changed the subject" | "Probably an arc" |
| "Adopted a formal register she hadn't used before" | "Emotionally invested" |

The left column is **observation of manner** — checkable, and still true in ten sessions. The right column is **interpretation of significance** — which is exactly what should be derived later, not asserted now.

Qualitative description is a fact. "How" is observable. "How much it matters" isn't, yet.

---

## Three layers of signal

### In-fiction — what the characters did

Actions taken in the world: spoke rather than fought, spared something, named an entity, gave away something valuable, returned somewhere unprompted, asked about a specific topic.

### Table-level — what the players did

Behavior out of character: asked about something unprompted, especially across sessions; debated a choice before acting; remembered a detail the GM had half-forgotten; adopted a running joke; expressed relief, dread, or anger; made plans involving a specific entity.

**The stronger signal.** In-fiction action can be purely tactical — sparing an enemy may be strategy. Three players arguing for ten minutes about whether to go back for someone has no tactical explanation.

### Roleplaying behavior — how it was played

The texture of performance, which is where investment often surfaces before anyone would name it:

- Voice, register, or manner choices, especially changes from their usual
- Emotional tone in character — reluctance, eagerness, cruelty, tenderness
- Whether they leaned in or stayed detached
- Unusual care or detail in describing their own actions
- A choice that fit the character but cost them something
- A choice that broke from how they'd played the character before

That last one is worth watching. A character acting out of character is either a mistake or a development, and the difference matters.

All three layers are worth recording, distinguishably, because they carry different weight.

---

## What a capture record needs

Per interaction fact:

| Field | Purpose |
|---|---|
| Who | Which character, or which player if table-level |
| With what | The entity involved — NPC, place, item, faction |
| What happened | Short factual statement |
| How | Qualitative description of manner, if notable |
| Layer | In-fiction, table-level, or roleplaying |
| Session | When |

The `how` field is optional but is often where the value is. It's also the field that can't be reconstructed later — what happened can be inferred from consequences; how it felt in the room cannot.

---

## Keep the write-up cheap

Capture happens after a session, when energy is low. If it feels like data entry it won't happen consistently, and inconsistent capture is worse than none — it produces confidently wrong pattern detection over a biased sample.

- **A fact is one line**, plus a phrase of manner if there's something to say.
- **Omission is expected.** Not every interaction gets recorded. The signal survives sampling.
- **Prose recap stays.** Narrative record and structured facts sit alongside each other; neither replaces the other.
- **Nothing is required.** A session with no interaction facts is a valid session record.
- **Write manner in your own words.** No vocabulary to learn, no controlled list. Free text is the point.

---

## Why manner matters beyond inference

Two payoffs the GM already wants, from [[GM-Considerations]]:

**The debrief.** Recounting what was going on behind the screen is much better with texture. "You all went completely silent" is the detail that makes the retelling land.

**The callback.** A payoff hits hardest when it references *how* something happened, not just that it did. An NPC remembering that Hilda made a joke to cover her discomfort is a sharper callback than one remembering she was present.

Texture also degrades faster than structure. What happened is recoverable from consequences; the manner of it is gone in a week if not written down.

---

## Open

**Do player notes eventually contribute?**
A player writing "I hope the rat made it" *is* a table-level signal, self-reported — possibly better than GM observation, since it needs no interpretation.

**Does the AI extract facts from the prose recap?**
Cheaper than writing both. But extraction can hallucinate, and these become premises. Probably: propose extractions, GM confirms. Manner descriptions are the riskiest to extract — they're the most interpretive.

**How long until enough accumulates?**
Clustering needs volume. Four to six sessions may not produce detectable patterns — fine, since the interface isn't due until then either.
