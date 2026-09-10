---
type: design
status: draft
visibility: gm
tags: [requirements, latency, retrieval]
---

# Retrieval Tiering

Not all content needs equal access latency. Companion to [[Update-Cadence]].

**Requirements only.** How tiering is implemented is deferred.

---

## The system knows roughly what will be asked

Unusual property: the GM's plan is a prediction of the next session's queries. Combined with what's currently active, that's enough to prioritize preparation rather than treating all content equally.

Signals, roughly in order of strength:

| Signal | Why it predicts demand |
|---|---|
| In the planned session | Directly expected to come up |
| One or two hops from planned assets | The branches the party might take |
| Attached to an active arc | Live threads get referenced |
| Recently appeared | Recency drives recall questions |
| Frequently appeared | Recurring figures get asked about |

And the converse: an NPC who appeared once five sessions ago, has no link to an active arc, and isn't in the plan is **cold**. Slower access is acceptable.

---

## Cold must still mean available

The entire design assumes players go off-plan. The NPC from five sessions ago is *most* likely to come up precisely because the party is doing something unanticipated — the plan being wrong and the query being cold are correlated.

So:

- **Cold tier needs a bounded worst case**, not just "eventually." A ten-second lookup mid-session is a failure regardless of tier.
- **Nothing is unreachable.** Tiering affects speed, never availability.
- **Degradation should be graceful and visible.** If a cold lookup is slower, that's fine; if it silently returns less, that's not.

---

## A cold hit is a signal

When the party asks about something nothing predicted, that's information:

- **The plan was off** — useful to know, and cheap to notice.
- **Or there's investment the system hasn't detected.** Players don't look up entities they don't care about.

Retrieval is behavior, and behavior is exactly the evidence [[Session-Capture]] is trying to collect. This channel is free, requires no GM observation, and doesn't depend on anyone being expressive.

Worth feeding back: repeated cold lookups on the same entity is a strong candidate for the investment clustering described in [[Arcs]]. It may be the single most reliable signal available, since it's an unprompted action with no performance component.

**Caveat:** searching for something isn't the same as caring about it. A player may look up an NPC purely to check a fact before acting. Frequency and repetition matter more than any single lookup.

---

## Requirements summary

- Access latency may vary by predicted demand.
- Prediction may use the GM's plan, arc activity, recency, and frequency.
- Cold content stays available with a bounded worst case.
- Tiering never changes *what* is returned, only how fast.
- Retrieval events are recorded and available as investment signal.

---

## Open

**Are player retrieval events recorded at all?**
Useful as signal, but it's monitoring what the players look at. Worth being deliberate rather than assuming — and possibly worth telling them.

**Does the GM's own retrieval count as signal?**
Probably not the same thing. The GM looking something up reflects prep needs, not investment.
