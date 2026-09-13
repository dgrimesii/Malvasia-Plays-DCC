---
type: design
status: draft
visibility: gm
tags: [product, release, backlog, scope]
---

# Release Plan

Resolves the surface question in [[Backlog-Readiness]] §G1.

---

## Settled

**Two releases, split by whether anyone is mid-conversation.**

- **Release 1 — between sessions.** Everything done with time to think: planning, capture, conversion, authoring, the computed layer — and the players reading and writing between sessions.
- **Release 2 — at the table.** The live surfaces, used while people are talking to each other: the GM's encounter and relationship views, and the players' memory bank.

**Both releases serve both people.** The axis is the situation, not the audience.

### This replaces an audience split

An earlier version divided R1 and R2 as *the GM interface* and *the player interface*. That axis produced awkward seams wherever it was pressed, and the seams were the evidence it was wrong:

- **Epic 15** — the GM checking a page as the party sees it — is a GM capability that was stranded in R2 because it needs the player rendering.
- **Epic 2 S12** had to invent a narrow forward slice of the player view so that a mis-parsed statement could be caught during capture review, in R1.
- **Epic 2 itself** is half prep-tier and half table-tier, with genuinely opposite requirements, held in one epic only because one person uses both.

Three symptoms, one cause. Under the new axis all three resolve rather than needing special handling.

### Why the situation is the right axis

It is what actually changes the requirements. [[Constraint-Serves-The-Table]] applies only when people are in a room together, and everything hard follows from it:

| | Between sessions | At the table |
|---|---|---|
| Latency | irrelevant | seconds; ten is a failure |
| Writes | the whole point | GM only, and nothing may depend on it. **Never for players** |
| Arriving unasked | tickets, proposals, what-ifs | nothing. Pull-only |
| Inference and generation | yes | **never** |
| Reading | browsing and wandering are the point | answer-shaped; dwelling is the failure |

An audience split cuts across every row. The situational split lines up with all of them.

It also matches what happens. The first real use of the tool is a prep week — conversion lands, the GM plans, a session follows later. **R2 is not a later audience; it is the moment the tool is first used while people are talking.** That is a more honest account of why R2 is unvalidated than "non-technical users" was.

---

## Epic allocation

| # | Epic | Release |
|---|---|---|
| 1 | Capture what happened in a session | R1 — **except S11**, mid-session fragment capture → R2 |
| 2 | Find anything, fast | **Splits** — see below |
| 3 | Know the next session is covered | R1 |
| 4 | Author and connect campaign material | R1 |
| 5 | Bring in outside material and integrate it | R1 |
| 6 | Surface what could not have been noticed | R1 — inference and generation never run at the table |
| 7 | Run a thread across a campaign | R1 |
| 8 | Feel the world moving without you | R1 |
| 9 | Players consult the record | **Splits** — between-session reading R1; the table memory bank R2 |
| 10 | Players contribute to the record | R1 — notes are written after the session by design, never at the table |
| 11 | Control what the party knows | R1 |
| 12 | Keep the record trustworthy | R1 |
| 13 | Move the campaign in without losing anything | R1 |
| 14 | Pace the campaign | R1 |
| 15 | See what the party knows | **R1** — was stranded in R2 by the old axis |
| 16 | Player attention as a prep signal | R1 for the reading; richer once R2 supplies table lookups |
| 17 | Recognise that two records are the same thing | R1 |

### Epic 2 splits, and should probably become two epics

It is the clearest case that the old axis was wrong. The two tiers optimise for opposite things and were only ever one epic because one person uses both.

| Part | Goes to | Why |
|---|---|---|
| Query correctness — match on fragments and aliases, find by shape, plain language, clear absence, source and dates, statements as statements | **R1** | Needed by every surface; proven during prep |
| The prep tier — breadth over precision, wandering, multi-hop | **R1** | The tier that gets used first |
| The table tier — seconds-level latency, fail-fast on a bad connection, lead with what is usable, mark what the party knows | **R2** | Every requirement follows from someone waiting |

**S12's marking is the interesting one.** The *data* requirement — visibility recorded per fact — is R1 and unrecoverable. The *display* requirement — catchable peripherally while talking — is R2. Splitting the story along that line removes the over-specification flagged when RC 1a was reconciled, without losing the requirement.

### What R2 actually is

Three surfaces, per [[Modes-and-Surfaces]]:

- **Encounter Assistant** — the planned facts about the encounter at hand
- **Role Play assistance** — the relationships around the current focus
- **Memory bank** — the players' search over what the party knows

Plus mid-session fragment capture, which nothing may depend on.

**R2 is small, and it is thin over R1.** All three read from the [[Live-Set]], which R1 assembles. None of them computes anything. That is a consequence of the constraint rather than a simplification.

---

## What changes, stated plainly

**Players get access in R1.** They read the record between sessions and write notes after. This is the largest practical change, and it is consistent with [[Player-Scope]] — the player surface replaces a notebook, and [[Constraint-Serves-The-Table]] already required notes to happen away from the table.

**R1 is now most of the product.** That is honest rather than alarming: the release candidates inside R1 do the incrementing, and nothing waits for a release to complete. But R1 should not be described as a milestone.

**Non-technical users arrive earlier.** Guidance, plain vocabulary, forgiving inputs, and error messaging were deferred to R2 on the old axis. Anything players touch in R1 needs them.

**The table surfaces land late.** The live views the product is most visibly *for* are the last thing built. Defensible — they are thin readers over a prepared set, and the prepared set is where the work is — but worth naming rather than discovering.

---

## What R1 must carry for R2

The old split created four obligations because R1 shipped with no player consuming anything. **Three of those are now consumed within R1** and stop being forward obligations: visibility per fact, attribution, and the utterance/claim separation are all exercised the first time a player reads a page.

They are no less required. The argument for them simply changes from *do not make R2 expensive* to *this is wrong from day one*, which is a stronger reason and a more testable one.

What genuinely remains forward:

### 1. Reveal is recorded as an event

*When* something became visible, not just *that* it is. Needed for *what is new since you last looked*, and not reconstructible afterward.

### 2. The Live Set is assembled in R1 and consumed in R2

All three table surfaces read from it. R1 therefore produces an artifact whose only consumer is in the next release — the same forward-dependency shape as before, relocated rather than removed. It is a smaller risk than the old ones because the Live Set is derived from accepted facts and could be rebuilt; nothing about it is unrecoverable.

### 3. Latency is a property of the store, not of the surface

R2's seconds-level bar cannot be met by a fast view over a slow store. Query paths and indexing decisions made in R1 set the ceiling. Worth measuring during R1 even though nothing yet requires it.

### 4. The four unrecoverable requirements

Unchanged by the re-axis, and the reason RC 1a is about the store rather than the screen: speaker attribution, two clocks, comparable attributes, per-fact visibility. See [[Roadmap]].

---

## What R1 gives up

Stated so it is a choice rather than a discovery.

**Investment still runs mostly on GM observation.** Player notes arrive in R1 under the new axis, which is an improvement on the old plan — but the other correction, **what players look up**, is largely a table behaviour and therefore R2. So R1's investment features gain one of their two corrections rather than neither.

Player reading between sessions does generate some lookup signal. Whether it is enough to matter is unknown, and worth watching rather than assuming — per [[Player-Scope]], search measures what the party *cannot remember*, which is a floor rather than a measure.

**Nothing is available at the table.** For the whole of R1 the GM runs sessions as they do now, from notes and memory, and captures afterward. The record improves continuously; the live experience does not change until R2.

This is the honest cost of the re-axis and it is larger than it sounds. It should be weighed against the alternative of shipping a thin table surface earlier — which the old axis would have allowed, at the price of building it before the Live Set exists to feed it.

---

## Consequences for the decision list

[[Backlog-Readiness]] decision 1 is answered at the surface level. Remaining, with status:

1. ~~Confirm the first shippable slice~~ — **RC 1a**, written and reconciled.
2. ~~Is the graph model adopted?~~ *(§G2)* — **Yes.** See [[Information-Architecture]].
3. ~~Where is the line between surfacing and authoring?~~ *(§G3)* — **Surfacing is authoring**; generation is separately permitted forward-only.
4. **Are tombstones preserved on deletion?** *(§G9)* — open, deadline-sensitive, decide during 1b.
5. ~~Does retrieval work with no connectivity?~~ *(§G8)* — **No.**
6. **Does the campaign have a known length?** *(§G4)* — open, gates Epic 14.
7. **How much canon before Floor 6?** *(Epic 8)* — open.

*Does anything reach players automatically* stays open and is now an R1 question rather than an R2 one, since players read the record in R1.

---

## Open

1. **Does Epic 2 become two epics, or one epic split across releases?** Two is cleaner given the opposite optimisation targets, but it renumbers and the epics are written. Worth deciding before 1b.
2. **Where does player reading sit inside R1's candidates?** It is not in RC 1a, which is capture, conversion, and query correctness. Probably 1b alongside Epic 11, since reveal control and player reading are the same capability seen from two sides.
3. **Does the [[Live-Set]] belong to R1 or R2?** Assembled between sessions, consumed at the table. Probably R1, built late, with R2 adding only the views — but that means building an artifact with no consumer, which is legitimate per [[Shippable-Increment]] and still worth stating.
4. **Do the RC labels still make sense?** 1a–1d were named against the old axis. The content is still right; the names may now mislead.
