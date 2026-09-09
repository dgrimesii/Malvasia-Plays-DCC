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
- **The mechanism is templates plus this repo plus AI.** That is the tool for now.
- **No interface until the end of Floor 2** — roughly 4–6 sessions out.

---

## Don't classify meaning at capture time

The temptation is a field like `significance: high`. It fails for a structural reason: **an interaction's meaning is often not knowable when it happens.** The rat mattered only once it reappeared in peril, sessions later. A GM asked to rate significance in the moment will either guess or flatten everything to medium.

So capture records **concrete, checkable facts**, and significance is derived later by clustering. The GM's job at write-up is to notice and write down what happened — not to decide what it will come to mean.

This has a useful property: facts stay true even when interpretation changes. A judgment recorded in Session 3 can be wrong by Session 9. A fact can't.

---

## Two layers of signal

### In-fiction — what the characters did

Actions taken in the world:

- Spoke with someone rather than fighting them
- Spared, protected, or rescued something
- Named or nicknamed an entity
- Gave away or spent something of value
- Returned somewhere unprompted
- Asked an NPC about a specific topic

### Table-level — what the players did

Behavior at the table, out of character. **This is the stronger signal.**

- Asked about something unprompted, especially across sessions
- Debated a choice among themselves before acting
- Remembered a detail the GM had half-forgotten
- Laughed at, quoted, or adopted something as a running joke
- Expressed relief, dread, or anger about an outcome
- Made a plan involving a specific entity

Why it's stronger: in-fiction action can be purely tactical. Sparing an enemy may be strategy. But three players arguing for ten minutes about whether to go back for someone is investment with no tactical explanation. **Table behavior is the least deniable evidence that something landed.**

Both layers are worth recording. They should be distinguishable, because they carry different weight.

---

## What a capture record needs

Per interaction fact:

| Field | Purpose |
|---|---|
| Who | Which character, or which player if table-level |
| With what | The entity involved — NPC, place, item, faction |
| What happened | Short factual statement, no interpretation |
| Layer | In-fiction or table-level |
| Session | When |

That's enough for clustering. Repeated touches on connected entities is exactly the pattern arc discovery looks for, and it needs nothing more than this.

---

## Keep the write-up cheap

Capture happens after a session, when energy is low. If it feels like data entry it won't happen consistently, and inconsistent capture is worse than none — it produces confidently wrong pattern detection over a biased sample.

Design rules:

- **A fact is one line.** No forms, no required fields beyond the obvious.
- **Omission is expected.** Not every interaction gets recorded. The signal survives sampling.
- **Prose recap stays.** The narrative record is for the GM and eventually the players; interaction facts are a separate, structured list alongside it. Neither replaces the other.
- **Nothing is required.** A session with no interaction facts is a valid session record.

---

## Open

**Do player notes eventually contribute table-level facts?**
A player writing "I hope the rat made it" *is* a table-level signal, self-reported. Once a player surface exists, their notes become a second capture channel — possibly a better one, since it needs no GM observation.

**Does the AI extract facts from the prose recap?**
Writing narrative and then having facts derived from it would be cheaper than doing both. But extraction can hallucinate, and these facts become premises. Probably: propose extractions, GM confirms.

**How long until enough accumulates to be useful?**
Clustering needs volume. Four to six sessions may not produce detectable patterns — which is fine, since the interface isn't due until then either.
