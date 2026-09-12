---
type: design
status: draft
visibility: gm
tags: [information-architecture, north-star, prep, retrieval, live-set, attention]
---

# The Live Set

The capped, session-facing artefact the table surfaces read from. Also the place where this project's actual job gets stated.

Follows from [[Modes-and-Surfaces]], [[Retrieval-Tiering]] and [[Prep-Rhythm]]. Sharpens [[North-Star]].

---

## The job, restated

[[North-Star]] names **the lost detail** as the failure mode. That is a symptom. The failure underneath it is **the forced beat**: the GM reaching for a connection under time pressure, not finding one, and manufacturing something the table can feel was manufactured. The mirror failure is over-preparation, where the only way through the session is on rails.

The hard problem is a story that feels real but not forced — one that feels like it grew organically, while still letting the GM prepare and run the table from a manageable, constrained set of facts.

**This is not a mystery. It has a mechanism.**

> A beat feels **earned** when it draws on material the table already put in the room.
> A beat feels **forced** when it draws on material the GM introduced at the moment of need.

Which makes the tool's job precise: **keep the already-in-the-room material findable, and small enough for the GM to hold.**

### The two halves are in tension

| | Pushes toward |
|---|---|
| **Findable** | recall — surface everything adjacent, prune nothing |
| **Holdable** | a hard cap — the GM can carry perhaps a dozen live facts into a session, not eighty |

**Resolution: the constraint is on what the GM is asked to hold, not on what the store contains.** The store can be enormous. The session-facing surface has a budget.

The constrained set is therefore not a performance concession. **It is the product.**

---

## What the Live Set is

An artefact assembled during **Record Plans** for the upcoming session, comprising:

- the planned encounters and events
- **open claims adjacent to them** — per [[Claims-and-Resolution]], the options available to spend
- entities at **Notable investment or higher** in scope
- already-established connections that are relevant

Ranked, and **capped**.

**Encounter Assistant and Role Play assistance both read from the Live Set rather than querying the whole graph.** This is what reduces mental load, and it is the concrete mechanism by which inference promotes cold material into hot before the session, closing the blind spot in [[Retrieval-Tiering]].

The Live Set is the real computed artefact of the tool. The inference queue is a means to it, not the end.

---

## Cap by budget, not by threshold

A confidence threshold gives the GM a variable and unpredictable load — some weeks four items, some weeks sixty.

A fixed ranked budget gives them a promise:

> Whatever else is true, you will not be handed more than you can hold.

Applies to the inference queue as well as the Live Set. Per [[Modes-and-Surfaces]], the scarce resource is GM attention per prep cycle, not compute.

**Corollary:** the budget must be a number in the acceptance criteria, not a sentiment. [[Backlog-Readiness]] already requires non-functional targets; this is one of them.

---

## Options, not recommendations

An interface commitment, not a wording preference.

**The moment the tool ranks resolutions by story quality, it is authoring, and the GM stops owning the beat.**

What the tool may legitimately say:

> These are the open claims you could spend here, and here is what each one would contradict.

**Constraints are checkable. Quality is not.** The tool presents the rational options available; the GM chooses. This is the same posture as the no-probability-field decision in [[Claims-and-Resolution]], applied at the interface layer.

---

## The dependency worth testing

The mechanism above depends on knowing that **the party latched onto something** — which is Investment.

In Release 1, Investment runs on **GM observation alone**. Per [[Release-Plan]], player notes and player search behaviour — the two corrections that do not depend on reading performance — are both Release 2. So the signal the organic-feeling-story mechanism relies on is at its weakest precisely when it matters most, during the insulated early floors named in [[Canon]].

**Decision: accepted.** The GM is assumed to have real expertise in reading the players at the table and will capture those observations in the recap. Recurrence remains the primary signal per [[Session-Capture]], and it is GM-observable.

Two design consequences of accepting it:

**The ask must be minimal.** The recap is written between sessions, unhurried — the right place for this load. What the tool needs is not a scoring exercise: only the ability to note that a moment mattered, attached to an entity and an event. Degree is set later during review, and the history is readable from the event sequence anyway.

**No table-time authoring for players.** Player notes are wanted as a future capability, but deliberately shaped: **players focusing on capture instead of on each other is the failure.** If notes arrive, they arrive after the session — a few minutes at the end, or during the week — never as a general authoring surface open at the table.

### Player search is the better correction

Passive, free, and already happening because the memory-bank surface exists. A lookup is a strong statement that something landed; nobody searches for an NPC they do not care about. It also catches the quiet player, whom GM observation systematically under-reads.

**Stated limit so it is not oversold:** search reflects what the party **cannot remember**, which correlates with investment but is not identical to it. A well-remembered obsession generates no queries. It is a floor, not a measure.

---

## Confirmation bias

The expertise assumption that makes GM observation trustworthy also makes it self-confirming: **the GM notices investment in the threads they already care about.** Acknowledged as a real risk. [[Verification-and-Challenge]] requires structural mitigation, and full mitigation here is hard — it would need a second observer, which Release 1 does not have.

One cheap partial correction that requires no second observer:

> **A coverage report: entities with accumulated table appearances and no recorded investment observation.**

Not a judgement, not a recommendation. Something the party keeps bumping into that the GM never flagged is worth a second look.

---

## Open

1. **The budget number.** Needs to be a figure, and needs a way to be revised from use.
2. **Ranking inputs for the Live Set.** Investment degree, adjacency to plan, and recency are obvious candidates; the weighting is not decided, and per §Options it must not extend to story quality.
3. **Live Set staleness.** [[Update-Cadence]] flagged that a prepared artefact must regenerate if the GM edits mid-week. A stale Live Set is worse than an obviously empty one.
