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

**An increment is shippable when it functions and breaks nothing. It need not be useful.**

A capability may ship with no consumer downstream. Something that produces correct output which nothing yet reads is a legitimate release. The queue is allowed to end in mid-air.

---

## Correction to [[Release-Plan]]

That document says *"1a is the real first release."* Under this definition that is wrong, and the framing should be read as: **1a is the first slice that is useful.** It is not the first slice that is shippable.

Shippable is a much lower bar and sits well below 1a. Individual stories within Epic 1 will clear it on their own.

---

## What "breaks nothing" means here

There is no production system and no user base to regress. So the bar is not availability — it is the record.

An increment breaks something if it:

- **Corrupts or loses campaign content.** The repo holds a live campaign. Damage here is unrecoverable in a way nothing else is.
- **Writes data that a later increment cannot read or correct.** Malformed output is worse than no output, because it accumulates silently.
- **Regresses a capability that already worked.**
- **Makes an existing manual workflow impossible.** As long as the GM still works partly in markdown, the tool must not stand in the way of that.

An increment does **not** break anything merely by being incomplete, unused, or feeding nothing.

---

## What this changes

**Ordering follows dependency and risk, not user value.** Producers can ship before consumers. That fits this domain unusually well — capture, the graph, and the derived layer are all producers whose consumers arrive later.

**R1 and R2 remain audience milestones, not delivery units.** [[Release-Plan]] slices 1a–1d stay useful as an ordering, but nothing waits for a slice to complete before shipping.

**Risky things move earlier.** The parts of the design most likely to be wrong — what counts as a meaningful interaction ([[Session-Capture]]), ticket thresholds ([[Information-Architecture]]), whether density is measurable at all ([[Arcs]]) — can now ship early and be observed, rather than being deferred until they are surrounded by enough machinery to be useful.

---

## Three conditions

Accepting the lower bar requires these, or increments become unverifiable.

### 1. Every increment is inspectable

A capability with no consumer still has to be checkable, or acceptance means nothing. The output must be visible somehow — a rendered file, a listing, a dump. Crude is fine; absent is not.

This is cheap here because of a property already settled in [[Interface-User-Stories]]: **the repo is the database.** Most output will land as files that can simply be read.

### 2. Record integrity is the standing acceptance criterion

Every story inherits it, whether or not it is restated: after this runs, the campaign record is still valid and still readable.

### 3. Regression is checked, not assumed

Each increment leaves the previously shipped ones working. With no users to notice otherwise, this needs to be deliberate.

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

**Acceptance criteria gain a second form.** Alongside the user-visible outcome, a story may be accepted on the correctness and inspectability of what it produces — for stories whose consumer does not exist yet.

**Epics stop implying a delivery bundle.** An epic is a coherent body of value; its stories may ship across a long span, in dependency order, with the epic incomplete and nothing wrong with that.
