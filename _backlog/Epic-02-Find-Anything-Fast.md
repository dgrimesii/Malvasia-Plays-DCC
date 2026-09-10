---
type: epic
id: epic-02
status: ready
release: R1
candidate: 1a
visibility: gm
tags: [epic, retrieval]
---

# Epic 2 — Find anything, fast, at the table

Terms marked on first use are defined in [[Glossary]].

---

## Who it is for

The **game master**, in two quite different situations:

- **At the table**, mid-sentence, with three people waiting. Seconds matter absolutely.
- **During preparation**, at home, thinking. Seconds do not matter at all.

Same content, same person, two different bars. Most of this epic is about the first, because the second is comparatively easy.

---

## The problem

The party doubles back. Six **sessions** ago they met a man who owed somebody money — the GM is sure of it, and sure it mattered. Who he owed, and why, is gone.

**A vignette.** The GM says *"give me a second"* and starts looking. Fifteen seconds pass. Then thirty. The players start a side conversation. The GM gives up, improvises a creditor on the spot, and moves on.

Two things have now happened. The moment is spent — that particular scene, where the party had leaned in, is over. And the record now contains a contradiction, because the real answer was written down six sessions ago and the improvised one will be written down tonight.

The second cost is the worse one. **A record that gets contradicted stops being consulted**, and once it stops being consulted it stops being maintained.

The general shape: **a detail that cannot be retrieved in the moment does not exist.** It does not matter that it is written down. The failure is not memory — it is access under time pressure, on a phone, while talking.

And the GM will not construct a query while mid-sentence. Whatever they remember is what they have: a fragment of a name, what the party called him, or only what he did.

---

## What is not being asked for

- **Not the player's view.** Filtering the record to what the party knows is Epic 15, in Release 2. In Release 1 the GM sees everything.
- **Not noticing things.** Surfacing connections the GM did not ask for is Epic 6. This epic answers questions; it does not raise them.
- **Not readiness.** Whether the next session is covered is Epic 3.
- **Not editing.** Changing what is found is Epic 4.
- **Not rules lookup.** Out of scope entirely, per [[Scope]].
- **Not tracking what the GM searched for.** Search behaviour as a signal applies to players, in Epic 16. The GM looking things up in their own store says nothing worth recording.

---

## Assumptions

| Assumption | Source |
|---|---|
| A detail that cannot be retrieved mid-sentence does not exist | [[North-Star]] |
| At the table the bar is seconds; ten seconds is a failure | [[Retrieval-Tiering]] |
| There are two tiers — at-the-table and prep — with genuinely different requirements | [[Retrieval-Tiering]] |
| At the table this happens on a phone or tablet, one-handed, glanced at while talking | [[Device-Context]] |
| The GM will not compose a structured query while running a scene | [[Interface-Direction]] |
| An entity has several names, including ones the party invented | [[Names-and-Aliases]] |
| What someone was told and what is true must stay distinguishable when read back | [[Facts-and-Revelation]] |
| Retrieval works with no network available | [[Hosting-Implications]] |

---

## Value, and the cost of omission

Epic 1 produces the material. **This epic is where it becomes worth having.** Without retrieval, capture is a filing habit with no payoff, and a filing habit with no payoff stops.

Three costs if this is absent or slow:

**The moment is lost.** Scenes where the party leans in are the ones worth getting right, and they are exactly the ones that cannot wait thirty seconds.

**The record acquires contradictions.** An improvised answer that conflicts with a written one is worse than having written nothing, because the conflict is now permanent and invisible until it surfaces again.

**Trust decays, and takes the whole product with it.** A store consulted twice and unhelpful twice is not consulted a third time. Every later capability is a query over this same store; none of them survives the GM deciding it is not worth asking.

---

## Stories

### S1 — Find something by whatever I happen to remember

*As the GM, I want to search on a fragment — part of a name, what the party called him, or just what he did — because in the moment that is all I have.*

- **Outcome:** The right entity is reached without recalling its formal name.
- **Assertion:** A search matches on any of an entity's names, including party coinages and names not known to the party, and on the content of facts recorded about it.
- **Demo:** Find one entity three ways — by partial formal name, by a party-invented alias, and by a phrase from a fact about it.

### S2 — Get it back in seconds

*As the GM, I want an answer fast enough that I do not have to stop the scene.*

- **Outcome:** The GM stays in the scene while looking something up.
- **Assertion:** A retrieval at the table returns in seconds. Ten seconds is a failed test, not a slow one.
- **Demo:** Time a set of representative lookups against a fixture sized like a real campaign.

### S3 — Find things with no network

*As the GM, I want lookup to work whether or not the room has a signal, because the venue's connection is not something I control.*

- **Outcome:** Retrieval is unaffected by connectivity.
- **Assertion:** With the network unavailable, at-the-table retrieval returns the same results as with it.
- **Demo:** Run the same lookups twice, once with the network disabled. Results match.

### S4 — See everything connected to a thing

*As the GM, I want one place showing what a person or place is tied to, so I can pick up a thread without remembering where it runs.*

- **Outcome:** A thing's neighbourhood is visible in one view rather than assembled by hand.
- **Assertion:** An entity's view shows its connections with their type and direction, and reaching a connected thing takes one step.
- **Demo:** Open an entity with several connections; reach each in one step.

### S5 — Find something by its shape, not its name

*As the GM, I want to search for the innkeeper who lied about the tunnels, because that is how I remember him.*

- **Outcome:** A description of what happened finds the thing it happened to.
- **Assertion:** A query describing an entity by its role and an event it took part in reaches that entity.
- **Demo:** Against the fixture, reach a target entity from a description containing none of its names.

### S6 — Ask in plain language

*As the GM, I want to type the question the way I would say it, because building a query is not something I can do while talking.*

- **Outcome:** No syntax to remember, and no wrong way to ask.
- **Assertion:** A plain question returns a result or a clear absence. It never returns an error about how the question was formed.
- **Demo:** Ask ten questions phrased naturally against the fixture; none produces a syntax complaint.

### S7 — Tell me when nothing is known, clearly

*As the GM, I want an empty answer to say plainly that nothing is recorded, so I never have to wonder mid-scene whether the tool is broken.*

- **Outcome:** The GM can trust an empty result and move on immediately.
- **Assertion:** A genuine absence is stated as an absence and is visibly different from a failure. Neither is a blank.
- **Demo:** Query something absent, then query with the store unreachable. The two responses are distinguishable at a glance.

### S8 — See where something came from

*As the GM, I want to know which session established a thing, so I can trust it and find the surrounding context.*

- **Outcome:** Anything retrieved can be traced to where it entered the record.
- **Assertion:** A retrieved fact carries its source and its session, and the session can be reached from it.
- **Demo:** Retrieve a fact; reach the session that established it in one step.

### S9 — Show me what was said as something that was said

*As the GM, I want the difference between what someone claimed and what is actually true to survive being read back, so I do not repeat a lie as fact.*

- **Outcome:** The GM can see at a glance whether the party was told something or whether it is so.
- **Assertion:** A statement made to the party is displayed with its speaker and is never rendered as a plain assertion. Its truth status is shown separately, including when unset.
- **Demo:** Retrieve a false statement. The output attributes it and does not state it as a fact.

**The read-side counterpart to Epic 1's S6.** Capturing the distinction is worthless if display collapses it.

### S10 — Give me something I can say out loud

*As the GM, I want what I retrieve to be immediately usable in the scene, not a page I have to read and condense first.*

- **Outcome:** Retrieved material can be read aloud or paraphrased without preparation.
- **Assertion:** An at-the-table view leads with what is usable in the moment — who they are, what they want, what they would bring up — and is legible on a phone at a glance.
- **Demo:** Show the at-the-table view for an NPC on a phone-width screen without scrolling for the essentials.

### S11 — Search properly when I have time

*As the GM, I want a slower, more thorough search during preparation, because the constraints that apply at the table do not apply at my desk.*

- **Outcome:** Prep-time questions are not limited by the at-the-table speed bar.
- **Assertion:** A prep-tier search may take longer and searches material the fast tier does not, and its results are the same store — never a separate or diverging copy.
- **Demo:** Run a query at both tiers; the slower one returns a superset, with no contradiction between them.

---

## Open questions

| Question | What it blocks | Where it sits |
|---|---|---|
| How much of the store must be resident on the device — all of it, or a prepared subset? | S3's scope | [[Update-Cadence]] suggests a prepared artifact is enough; needs deciding, not designing, before S3 is accepted |
| What failure rate is acceptable when interpreting a plain-language question? | S5 and S6 acceptance | Needs a threshold. Likely answered by observation across a few sessions |
| Should results rank by recency, or by proximity to the current session? | S1, S5 quality | Answer after use, not in advance |
| Is the at-the-table view a different surface, or the same one behaving differently? | Nothing yet | Genuinely a design question — deliberately left open |

---

## Dependencies

- **Epic 1** produces the material this epic reads.
- **Epic 13** puts the existing campaign into the store. Until it lands, this epic can be demonstrated against fixtures but not used — retrieval over an empty store is a demonstration, not a tool.
- **Prerequisites P2 and P3.** S2 in particular needs a fixture sized like a real campaign; timing against a small one proves nothing.
