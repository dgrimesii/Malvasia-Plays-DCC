---
type: design
status: open
visibility: gm
tags: [requirements, open-questions]
---

# Open Requirements

Requirements questions only — what the system must do and for whom. Design and architecture stay deferred.

Marked **[blocking]** where other requirements depend on the answer.

---

## Settled

- **Work is batched**, most likely aligned to workflow steps. Mechanism deferred.
- **Deletion is possible.** Bounded rollback window; behavior undecided (see [[Rollback-and-Repair]]).
- **Reads are fast, writes are once per session.** No sync, no concurrency (see [[Update-Cadence]]).
- **Scope is narrative.** No stats, rules enforcement, or produced prose (see [[Scope]]).
- **The GM captures most content**, via templates plus repo plus AI (see [[Session-Capture]]).
- **Player notes need no GM approval.** Attribution handles correctness — *"Sam wrote X"* stays true even when X is false, the same way an NPC's lie stays a recorded utterance.
- **No bootstrap problem.** The tool comes online around Session 4. Sessions 1–3 are captured as GM notes with straightforward references, which is enough to seed it.
- **Text is canonical; visualization on demand**, except the table view (see [[Interface-Direction]]).

### Consequence of the Session 4 timing

Capture for Sessions 1–3 has to be good enough to bootstrap from. The template is the tool for those sessions, and anything not recorded then isn't recoverable later. Worth a look at [[Session-Capture]] before Session 1 rather than after.

---

## Moved to design phase

- **Where player notes live** relative to the repo. Storage question.
- **How batching is implemented.**
- **How tiering is implemented** (see [[Retrieval-Tiering]]).

---

## 1. Access and identity

**[blocking] Do players need individual identity in the system?**
Note ownership, per-player visibility, and query attribution all assume the system knows who's who.

**Does the GM see player notes?**
Rich signal versus players writing freely when unobserved.

**Is there a shared party-visible layer?**
Private to author, shared with party, GM-revealed — possibly only two of the three are needed.

**What happens when a player leaves or joins mid-campaign?**

---

## 2. Capture

**[blocking] What counts as a "meaningful interaction"?**
Partly answered by [[Session-Capture]] — facts, not judgments, across three layers plus recurrence. Whether that shape survives contact with real sessions is open.

**How much detail must a session record hold?**
Enough to reconstruct events, or enough to feed inference? The second is a higher bar.

**Does the AI extract facts from the prose recap?**
Cheaper than writing both, but extraction can hallucinate and manner must never be manufactured.

---

## 3. What the AI may propose

**[blocking] Where is the line between surfacing and authoring?**
May it propose *content* — a projection, a climax, a story beat — or only *connections* and *gaps*?

**What happens when a proposal is a bad reading?**
Not a hallucinated fact but a wrong interpretation — "the party seems invested in the Warden" when they aren't. Rejection exists; whether rejection *teaches* anything, or just dismisses one card, is undecided.

**How strong must a pattern be before a ticket fires?**
Too eager and tickets get dismissed reflexively.

**Should the system ever push back?**
Density awareness implies it might say "let the next one just be a dungeon."

---

## 4. Canon

**[blocking] How much canon must be recorded, and when?**
Floors 1–5 need almost none; Floor 6 onward needs enough to compute proximity.

**Can the party affect canon outcomes, or only experience them?**

**Does divergence need to be visible to players?**

**Has anyone at the table read the books?**
Changes proximate events from mystery to dramatic irony, per player.

**Do canon events feed the arc tree?**

---

## 5. Campaign shape

**[blocking] Does the campaign have a known length?**
Arc budgeting and convergence planning need a horizon.

**Is arc density measurable in a useful way?**
Counting arc-connected events may mistake quantity for weight.

---

## 6. Correctness and rollback

See [[Rollback-and-Repair]] and [[Facts-and-Revelation]]. Most apparent "fact changes" are revelations, which are additive; only genuine errors need deletion.

**[blocking] What happens to work built on a rolled-back batch?**
Block, cascade, flag, or repair. Undecided, possibly overkill.

**Should tombstones be preserved regardless?**
A cheap hedge with an early deadline — if deletion cleans up references, repair becomes impossible to add later.

---

## 7. Lifecycle events

**[blocking] What happens when a character dies?**
DCC runs on lethality. Does the dossier become historical? Do their arcs transfer or resolve? Does a new character inherit their relationships? Does the dead character stay in the graph as a node others reference?

**Can arcs merge and split, and what survives?**
Handles, evidence with attribution, moment of convergence, reconciled projection.

---

## 8. Working rhythm

**What does the week before a session actually look like?**
One long block, scattered minutes, or the morning of? Everything about surfacing hints and readiness assumes a moment when the GM sits down to prep. Worth confirming that moment exists and what shape it has.

**Does anything get shown to players automatically?**
Everything so far is GM-gated reveal. But a session recap players can read afterward is the obvious thing they'd want, and manual publishing each week is exactly the step that gets skipped. Small question, large effect on whether the player surface gets used at all.

**What's the fallback if the tool isn't available mid-session?**
Dead laptop, no connectivity, a bug. Plain markdown helps, but worth answering deliberately.

---

## 9. Scope boundaries

**Is this one campaign or a system for many?**

**Does the GM need to invent new relationship types during play?**
Closed vocabulary is queryable; open is expressive.

**Is content portability required?**
Export, backup, migration off this system.

---

## Suggested order

1. **Is this a multi-user system?** (§1)
2. **What does prep week look like?** (§8) — shapes the GM surface more than anything else unanswered.
3. **How does bad data get found and removed?** (§6)
4. **Character death** (§7) — will happen, probably sooner than expected.

Canon workload (§4) has a Floor 6 deadline. Campaign length (§5) the sooner the better.
