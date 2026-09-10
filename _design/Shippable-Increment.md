---
type: design
status: draft
visibility: gm
tags: [product, release, increments, definition-of-done]
---

# Shippable Increment

Defines what "shippable" means for this project. Refines [[Release-Plan]].

---

## Settled

An increment is shippable when it is:

1. **Functional** — it does what it claims.
2. **Non-breaking** — nothing that worked before stops working, and the record survives.
3. **Testable** — its behaviour can be asserted, and the assertion can fail.
4. **Demoable** — it can be shown. A script or a file output is sufficient; a UI is not required.

**It need not be useful.** A capability may ship with no consumer downstream. Something that produces correct output which nothing yet reads is a legitimate release. The queue is allowed to end in mid-air.

---

## Correction to [[Release-Plan]]

That document says *"1a is the real first release."* Under this definition that is wrong, and the framing should be read as: **1a is the first slice that is useful.** It is not the first slice that is shippable.

Shippable is a much lower bar and sits well below 1a. Individual stories within Epic 1 will clear it on their own.

---

## Non-breaking

There is no production system and no user base to regress. So the bar is not availability — it is the record.

An increment breaks something if it:

- **Corrupts or loses campaign content.** The repo holds a live campaign. Damage here is unrecoverable in a way nothing else is.
- **Writes data that a later increment cannot read or correct.** Malformed output is worse than no output, because it accumulates silently.
- **Regresses a capability that already worked.**
- **Makes an existing manual workflow impossible.** As long as the GM still works partly in markdown, the tool must not stand in the way of that.

An increment does **not** break anything merely by being incomplete, unused, or feeding nothing.

---

## Testable

Every story carries at least one assertion that can fail. Without a consumer to notice misbehaviour, the test is the only thing standing between a quiet defect and a poisoned record.

### This forces precision where the design is currently vague

Several capabilities are described in judgment terms that cannot be asserted as written. *"The ticket fires when the pattern is strong enough"* has no test. *"Given this evidence set, a ticket fires and cites these three interactions"* does.

That is a feature of the requirement, not a burden: the areas hardest to make testable — ticket thresholds, investment clustering, what counts as a meaningful interaction — are exactly the ones [[Backlog-Readiness]] §G4 flags as having no acceptance thresholds. Writing the test is how the threshold gets decided.

### The negative constraints must be asserted too

[[Constraint-Manner-and-Intent]] is a list of things that must never happen — no generated manner, no inferred intent, no filling a blank because the field exists, no embellishment in recaps. **These are the constraints most likely to erode silently**, because nothing visibly goes wrong when they are violated.

Assertions of absence are cheap and belong in the acceptance criteria for anything that writes capture records. *"Manner is empty in the output"* is a test.

### Test data must not be the live campaign

Two reasons, both hard:

- Testing against the real record risks the one thing the non-breaking rule protects.
- The real record changes every week, so assertions written against it break for reasons unrelated to the code.

So increments need **fixtures — a small synthetic campaign** with known entities, sessions, interactions, and edges, stable enough to assert against. This is a real deliverable that no design document has yet named, and it is needed by the first increment that writes anything.

It also has a second use: fixtures are the only way to exercise scenarios the live campaign has not reached yet — a character death, a merged arc, a revealed lie, a Floor 6 canon proximity — long before they happen at the table.

---

## Demoable

The increment can be shown and judged. **The demo path is part of the story, not an afterthought** — if there is no way to show it, it is not ready to be worked.

Acceptable forms, in ascending cost:

- Reading the file the increment produced
- A diff against what existed before
- A script that runs it against a fixture and prints the result
- A rendered view, where one happens to exist

Cheap here because of a property already settled in [[Interface-User-Stories]]: **the repo is the database.** Most output lands as files that can simply be read.

### Test and demo are doing different jobs

Worth keeping distinct, because several capabilities in this design can only be accepted by the second:

| | Answers | Used for |
|---|---|---|
| **Test** | Did it do the specified thing? | Behaviour that can be stated in advance |
| **Demo** | Is this any good? | Judgment — whether a proposal is a *good* reading, whether a handle elicits memory, whether a coverage claim is trustworthy |

[[Open-Requirements]] §3 asks what happens when a proposal is a bad reading — not a hallucinated fact but a wrong interpretation. No test catches that. The demo is where it gets caught, and the GM is the instrument.

So for the inference and proposal epics, **the demo is the acceptance mechanism**, and the test only guards the floor beneath it.

---

## The one exception: capture has a clock

Everything else can ship unused for as long as it likes. Capture cannot.

[[Session-Capture]] is explicit that **anything not recorded at the time is not recoverable later**, and sessions are being played now. The campaign does not wait for the queue.

That makes Epic 1 different in kind from the rest of R1:

- Its schedule is set by the campaign, not by dependency order.
- Shipping it unused is fine; shipping it *late* is not, because the sessions it would have captured are gone.
- The interim mechanism — templates plus repo plus AI — already exists and is doing the job. The requirement is that the tool take over **without a gap**, and without invalidating what the templates produced.

Related, and easy to miss: the four R1 obligations in [[Release-Plan]] — visibility from creation, attribution, utterance/claim/belief separation, reveal recorded as an event — apply to the interim template capture too, not just to the eventual tool. Sessions captured before the tool exists carry the same constraints, for the same reason.

---

## Coexistence with the current workflow

Because increments need not be useful, the GM will be working partly in markdown and partly in the tool for a long stretch. That is sustainable here, but it needs one rule stated:

**The repo is authoritative throughout.** The tool reads and writes it; it is not a separate store that must be reconciled. Any increment that would make the tool the sole home of some content needs to say so explicitly, because that is the point where dual-running stops being free.

---

## Consequence for the backlog

**Story voice does not change.** Stories stay written from the user's perspective, as value statements. This definition governs how increments are *composed and gated*, not how they are *written*.

**Acceptance criteria have up to three parts:**

- The **user outcome**, where a consumer exists to deliver it to
- The **assertion** — what must be true of the output, including what must be absent
- The **demo path** — how it gets shown

For a producer with no consumer yet, the first is empty and the other two carry the acceptance on their own.

**Epics stop implying a delivery bundle.** An epic is a coherent body of value; its stories may ship across a long span, in dependency order, with the epic incomplete and nothing wrong with that.

**Fixtures are a prerequisite, not a nice-to-have.** They should be scheduled ahead of the first increment that writes campaign data, since testability is now a gate rather than a preference.
