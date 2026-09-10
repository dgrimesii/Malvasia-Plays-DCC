---
type: design
status: draft
visibility: gm
tags: [requirements, latency, retrieval, investment]
---

# Retrieval Tiering and Query Signal

Two related ideas: not all content needs equal access latency, and what players look up is useful information.

**Requirements only.** Implementation deferred.

---

## Part 1 — Tiering

### The system knows roughly what will be asked

Unusual property: the GM's plan is a prediction of the next session's queries. Combined with what's currently active, that's enough to prioritize preparation rather than treating all content equally.

| Signal | Why it predicts demand |
|---|---|
| In the planned session | Directly expected |
| One or two hops from planned assets | The branches the party might take |
| Attached to an active arc | Live threads get referenced |
| Recently appeared | Recency drives recall questions |
| Frequently appeared | Recurring figures get asked about |

Conversely: an NPC who appeared once five sessions ago, has no link to an active arc, and isn't in the plan is **cold**. Slower access is acceptable.

### Cold must still mean available

The design assumes players go off-plan. The NPC from five sessions ago is *most* likely to come up precisely because the party is doing something unanticipated — the plan being wrong and the query being cold are correlated.

- **Cold tier needs a bounded worst case.** Ten seconds mid-session is a failure regardless of tier.
- **Nothing is unreachable.** Tiering affects speed, never availability.
- **Degradation is visible, not silent.** Slower is fine; returning less is not.

---

## Part 2 — Player queries as signal

What the players look up is evidence of what they're thinking about. The use case is specific: **a hint to the GM about where prep or an arc may be needed.**

### Attention coverage

This surfaces a kind of readiness the design didn't previously have a source for:

| | Question it answers | Evidence source |
|---|---|---|
| **Path coverage** | If they go left, is something there? | The GM's own branch mapping |
| **Attention coverage** | If they pursue what they're already thinking about, is anything there? | Player queries |

Path coverage is what the readiness check in [[GM-Considerations]] measures. Attention coverage is orthogonal, and query data is the only way to see it.

### The actionable signal

**High query volume plus no corresponding prep is a gap.**

> The party has looked up the Warden four times since last session. Nothing planned involves him.

That's a prep hint, not analytics. Variants worth surfacing:

- **Queried repeatedly, nothing prepared** — they're heading somewhere the GM isn't ready for.
- **Queried repeatedly, thin content** — the world has a hole where their attention is. Worth deepening.
- **Multiple connected entities queried** — candidate arc material, and a strong version of the investment clustering in [[Arcs]], since the queries are unprompted.
- **Queried and then acted on** — confirms the lookup was planning, not idle checking.

### Why this signal is unusually good

- **Unprompted.** Nobody asked them to look.
- **No performance component.** Fixes the quiet-player problem in [[Session-Capture]] — a player who never emotes still searches.
- **Requires no GM observation.** It accumulates without anyone noticing anything at the table.
- **It's behavior, not interpretation.** Fully consistent with [[Constraint-Manner-and-Intent]] — the record is "looked up X four times," which is a fact. Why they looked is not inferred.

### Caveats

- **A single lookup means little.** Someone may be checking a fact before acting. Repetition is the signal.
- **Queries reflect uncertainty as much as interest.** Frequent lookups may mean the GM's delivery wasn't clear, not that the topic is compelling. Both are useful to know, but they're different findings.
- **Tell the players it's recorded.** A signal that quietly shapes the campaign is different from a known one, and the honest version costs nothing — most players would find it flattering that their curiosity steers prep.

---

## Requirements summary

- Access latency may vary by predicted demand; cold content stays available with a bounded worst case.
- Tiering never changes what is returned, only how fast.
- Player retrieval events are recorded, with entity and timestamp.
- The GM sees query-derived prep hints: repeated queries with no prep, thin content where attention is, and connected clusters.
- GM retrieval is recorded separately or not at all — it reflects prep needs, not investment.
- Players are told their queries inform prep.
