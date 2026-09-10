---
type: design
status: draft
visibility: gm
tags: [model, facts, revelation]
---

# Facts, Claims, and Revelation

Clarifies what "a fact changing" actually means. Referenced from [[Information-Architecture]] and [[Open-Requirements]] §6.

---

## Facts don't change

*"The Warden told the party X in Session 3"* is permanently true. It happened, they heard it, they acted on it. Nothing later makes it untrue.

What has a truth value is the **claim** — X itself — and that's a separate thing from the utterance. Three distinct records:

| | Example | Mutable? |
|---|---|---|
| **Utterance** | The Warden said the tunnels flood at night | No — it happened |
| **Claim** | The tunnels flood at night | Has a truth status the GM may set or revise |
| **Belief** | The party believes the tunnels flood at night | Changes when something reveals otherwise |

Most of what looks like a fact changing is a claim's status being established, or a belief being corrected. The event record is append-only.

---

## Revelation is additive, not corrective

When a lie is revealed, nothing is edited. **A new fact is added** — *"In Session 9, the party learned the Warden lied about the tunnels"* — and it recontextualizes the earlier utterance without touching it.

This distinguishes two things that look similar and behave nothing alike:

| | What happened | Response |
|---|---|---|
| **Error** | The record says something that never happened — a hallucinated NPC, a misattributed event | Delete or roll back |
| **Revelation** | The record is entirely correct; its meaning changed | Append |

Only errors need the deletion and rollback machinery in [[Rollback-and-Repair]]. Revelation needs nothing but the ability to add a fact, which the system has by definition.

---

## Retroactive lies are legitimate

The GM may decide, later, that something was a lie — even having believed it true when delivering it. A detail that was straight exposition in Session 3 can turn out to make a better story as a deception in Session 9.

**This is authorship, not error.** The system must not treat it as a mistake needing correction, and must not require the GM to justify it. The GM sets the claim's truth status; the utterance stands untouched.

The record afterward is honest about both: the Warden said it, and it was false. Whether the GM knew that at the time is nobody's business and doesn't need recording.

---

## Revelation should generate

The useful behavior: when a claim's status flips, **surface what else rested on it.**

Not as cleanup — as material. If the Warden lied about the tunnels, then:

- What did the party do based on believing it?
- What else did he say that's now worth doubting?
- Who else repeated the claim, and did they know?
- What did the party conclude that was built on it?

Those are story hooks, not repairs. A revealed lie is one of the highest-value events in a campaign precisely because it makes a whole neighborhood of the graph interesting again.

So the requirement is a generative one: **on a status flip, show the affected neighborhood as an opportunity.** Same traversal that would have served premise decay, pointed at authoring rather than at correction.

---

## What this simplifies

The earlier framing assumed facts mutate and dependents silently rot. Mostly they don't — narrative change is additive, and the append-only event record stays true throughout.

That leaves genuine data errors as the only case needing deletion, which is a much smaller problem than it appeared.
