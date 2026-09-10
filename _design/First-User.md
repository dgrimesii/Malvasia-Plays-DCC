---
type: design
status: draft
visibility: gm
tags: [product, users, release, acceptance]
---

# First User

Confirms the audience for Release 1. Companion to [[Release-Plan]] and [[Shippable-Increment]].

---

## Settled

**The first user is the GM — David — who is also the builder.**

Already stated as design context in [[GM-Considerations]]; recorded here as a product fact, because it changes what R1 has to include and how increments get accepted.

---

## What this removes from R1

Real scope reduction, not optimism:

- **No onboarding, no guidance, no help text.** The user knows what everything is and why it exists.
- **No forgiving inputs.** Malformed entry can fail loudly. Nobody needs to be caught.
- **No error messaging for the unfamiliar.** A stack trace is an acceptable error surface for one user who can read it.
- **No vocabulary translation.** The domain terms in [[Information-Architecture]] can appear raw in the interface.
- **Epic 13 shrinks.** Import of Sessions 1–3 still matters; first-run experience does not.

The glossary in [[Backlog-Readiness]] §G10 is still needed — but for the development team, not for the user.

---

## What this does not remove

**Record integrity.** The non-breaking rules in [[Shippable-Increment]] protect the campaign record, and the record does not care who is operating the tool. A single expert user is exactly as capable of losing a session's capture as anyone else.

**Fixtures and tests.** Being the only user removes the need for polish, not the need for assertions. It arguably increases it — see below.

---

## The cost: acceptance has no independent observer

[[Shippable-Increment]] makes the demo the acceptance mechanism for anything judgment-bearing — whether a proposal is a good reading, whether a handle elicits memory, whether a coverage claim is trustworthy. With one user who is also the builder, **the person judging the output is the person who decided what it should be.**

Two specific risks:

- **Unconscious compensation.** A user who knows what was intended will navigate around a bad surface without noticing it is bad. The interface can be worse than it appears, indefinitely.
- **Confirmation.** A proposal that matches what the builder expected reads as a good proposal. This bites hardest on the inference epics, where the whole value claim is *surfacing what could not have been noticed* — the one thing an expectation-matching judgment cannot verify.

**Mitigation, and it is cheap:** keep the demo a distinct act. A script that runs against a fixture and prints its output is a different experience from having just written the code, and it is the difference between judging the output and remembering the intent. Where the assertion can be written down in advance of running it, write it down first.

---

## The compensating advantage

The feedback loop is unusually tight and unusually honest. The tool gets used at a real table, weekly, under time pressure, by someone who will immediately notice when the right detail cannot be retrieved.

That is a better test environment than most products get, and it directly exercises the open questions the design cannot resolve on paper — whether the capture shape in [[Session-Capture]] survives contact with real sessions, whether tickets fire usefully or get dismissed reflexively, whether coverage claims are trusted.

**Use it deliberately.** These are questions to answer by observation over a few sessions, not by deciding harder in advance.

---

## Consequence for Release 2

R1 will be shaped entirely around one person's working style, and that is correct — [[GM-Considerations]] is explicit that degrading the GM's experience to serve the players is a bad trade.

But it means **R2 cannot be inferred from R1 usage.** The player surface has three users, two of whom are not comfortable with technical tooling, and none of whom built it. Everything R1 legitimately skips — guidance, forgiving inputs, error messaging, plain vocabulary — returns as a requirement there.

The R2 epics should be treated as genuinely unvalidated when their time comes, not as a re-skin of a proven product.
