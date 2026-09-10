---
type: design
status: open
visibility: gm
tags: [product, backlog, readiness, gaps]
---

# Backlog Readiness Assessment

Product-management review of `_design/` against one question: **is there enough here to write epics and user stories that a development team could work from?**

Scope of this document is requirements readiness only. Architecture, storage, and technical design remain deliberately downstream — nothing here asks for them.

---

## Verdict

**Epics: writable now, with two exceptions.** The value structure is unusually well articulated. [[North-Star]] gives a decision test, [[Scope]] gives hard boundaries, and [[Interface-User-Stories]] already contains roughly forty stories in the correct voice. Most of the epic spine can be derived today.

**Stories: partially writable.** Four areas are ready or near-ready. Four are blocked on decisions that change what the story *is*, not merely how it's built.

**The single largest gap is not a missing answer. It is the absence of a release boundary.** Nothing in `_design/` says what the first usable version contains. Without that, epics can be written but not ordered, and "done" cannot be defined for any of them.

---

## What is genuinely strong

Worth stating plainly, because the gap list below is long and would otherwise misrepresent the state of this documentation.

| Asset | Why it matters for backlog work |
|---|---|
| [[North-Star]] | A stated test for whether a feature belongs. Rare, and it makes prioritization arguable rather than arbitrary. |
| [[Scope]] | Explicit out-of-scope list. Prevents the most common story-inflation failure. |
| [[GM-Considerations]] | "What the tool should never do" converts directly into acceptance criteria and negative tests. |
| [[Interface-User-Stories]] | A real first draft of the backlog, already in user voice, already free of solution language. |
| [[Constraint-Manner-and-Intent]] | A hard constraint with a clear rationale. Testable as written. |
| [[Players-and-Characters]] | Collapses identity, per-player visibility, private notes, and character death into one small model. Removes more scope than any other document. |
| [[Update-Cadence]] + [[Device-Context]] + [[Prep-Rhythm]] | The non-functional envelope for latency, devices, and working rhythm is settled. |
| [[Facts-and-Revelation]] | Reframes "changing facts" as append-only. Eliminates a large speculative feature area. |

Correctly deferred, and **not** gaps: storage format, edge serialization, batching mechanism, tiering implementation, hosting. These are design-phase concerns and the documentation is right to leave them alone.

---

## Blocking gaps

Ordered by how much backlog they hold up.

### G1 — No release boundary or value increment sequence

**Blocks:** every epic's ordering, sizing, and definition of done.

[[Session-Capture]] establishes a timing anchor — no interface until the end of Floor 2, four to six sessions out — but no content boundary. Nothing states which capabilities constitute a first usable version.

The specific unanswered question: **does the first release include the player surface at all?**

The two surfaces have different economics. The GM surface has a deadline (Floor 6, per [[Canon]]) and one user who is also the builder. The player surface has three users, no deadline, and is the half that delivers the authorship goal in [[North-Star]]. Both arguments are strong; neither is made anywhere.

**Needed:** a stated first increment, expressed as user value rather than feature list. Something of the shape *"the GM can capture a session and retrieve anything from it in seconds at the table"* — enough to order everything else against.

---

### G2 — The graph model is provisional, and live content contradicts it

**Blocks:** most Organizing stories, all arc-membership stories, all backlink and cross-link stories.

[[Information-Architecture]] closes with "not yet applied — flagged pending a decision." Meanwhile the live templates still encode the flattened model: `Template-Zone.md` carries `arc:`, `Template-Arc.md` carries `zones: []` and a Stages table, there is no Quest template, and `Arc-Food-is-Love.md` is labelled a quest arc when the document says it is a quest.

This is not an architecture question. A story such as *"links are maintained in both directions"* is only writable if the directed-attributed-graph model is accepted as the domain model. If it is not accepted, that story does not exist in that form.

**Needed:** an explicit adopt / defer / reject decision on the graph model, and — if adopted — reclassification of the existing quest and revision of the templates. The template work is small now and grows with every file added.

---

### G3 — The line between surfacing and authoring is undecided

**Blocks:** the entire proposal and inference epic. Possibly the largest single body of stories.

[[Open-Requirements]] §3 marks this blocking. [[Arcs]] restates it as open questions 2 and 3. [[Information-Architecture]] describes the ticket mechanism in detail but does not settle what a ticket may contain.

The range is wide, and each point produces a materially different backlog:

- **Connections and gaps only.** The system says *these three entities are related and the party has touched all three.* It never proposes story content.
- **Connections, gaps, and branches.** It may also say *you have not considered that she might do nothing* — extending the GM's own projection without originating one.
- **Content proposals.** It may propose a beat, a complication, a climax.

[[Arcs]] leans toward the middle option and calls proposing a climax an overstep. [[Interface-User-Stories]] assumes the third under Synthesizing — *"I want suggested story beats, social interactions, and complications."* **The two documents disagree.**

**Needed:** one answer, recorded once. Everything about ticket design, approval flow, and rejection memory hangs off it.

---

### G4 — No acceptance thresholds for the judgment-bearing features

**Blocks:** story-level acceptance criteria across proposals, readiness, and investment inference.

Some measures are already excellent and should be lifted directly into criteria: ten seconds mid-session is a failure ([[Retrieval-Tiering]]); coverage means every live branch has something behind it ([[GM-Considerations]]); the tool can say *you are prepared for the next session*, backed by what it checked.

Others have none:

- **Ticket precision.** *"How strong must a pattern be before a ticket fires?"* is open in three documents. [[GM-Considerations]] warns that reflexive dismissal is the failure mode, which means an untuned threshold does not merely underdeliver — it trains the user to ignore the feature.
- **Arc density.** [[Arcs]] open question 4 doubts density is measurably meaningful at all. If it is not, the pacing epic loses its basis.
- **Investment clustering.** No stated minimum evidence for surfacing a candidate arc.

**Needed:** either a threshold, or an explicit decision that the threshold is tunable by the GM and starts deliberately conservative. The second is a legitimate answer and is cheap to write as a story.

---

### G5 — Player-surface reveal mechanics are undecided

**Blocks:** several player stories and the GM's reveal stories.

Resolved since [[Interface-User-Stories]] was written: private notes (there are none), and whether the GM sees player notes (yes) — both settled in [[Players-and-Characters]]. Still open, and each changes behaviour rather than implementation:

1. **Does anything publish to players automatically?** [[Open-Requirements]] §8 flags this as small in effort and large in effect. A recap players can read afterward is the obvious thing they want, and manual weekly publishing is precisely the step that gets skipped. If nothing is automatic, the player surface may simply not get used.
2. **Bulk reveal.** After a session several things become known at once. One action or many.
3. **Does revising revealed content show as a change to players,** or does the record silently become what it now says.
4. **An unresolved internal tension.** [[Interface-User-Stories]] requires that it be *"evident to a player when new material has been revealed since they last looked."* That implies a per-player last-seen marker. [[Players-and-Characters]] states there is no per-player knowledge. Both cannot be true as written. Likely reconcilable — a read marker is not knowledge — but it needs saying, because a developer will otherwise pick one and the choice will be invisible.
5. **A player note that references something they should not know.** Named as a design constraint; no decided behaviour. The system must neither confirm nor deny, which is a statement of what must not happen, not of what does.

---

### G6 — Intersection notes have two different homes in two documents

**Blocks:** the Authoring epic's central story.

[[Information-Architecture]] answers it: the note lives on the edge. [[Interface-User-Stories]] still lists it as open question 1. This is a documentation drift problem rather than a genuinely open question, but it must be closed before the story is written, because *"write about the intersection of two or more things and reach it from all of them"* is one of the more distinctive stories in the set.

---

### G7 — Ingest and bootstrap are undocumented

**Blocks:** the Integration epic's primary input, and everything about first use.

Two related holes:

- **Sessions 1–3.** [[Open-Requirements]] settles that there is no bootstrap problem because early sessions are captured as GM notes. But no story covers getting those notes *into* the tool. First-run import is real work with real user value and currently has no documentation behind it.
- **The upstream handoff.** [[Interface-User-Stories]] assumes a *"synthesized planning document"* arrives from Gemini as markdown, and the Organizing stories all take it as input. Its shape is nowhere described. An epic whose main input is unspecified cannot have meaningful acceptance criteria.

---

### G8 — Mid-session failure has no stated expectation

**Blocks:** at-the-table stories for both surfaces.

[[Open-Requirements]] §8 raises it. [[Update-Cadence]] makes offline operation *nearly free* — a prepared artifact can sit locally — but stops short of requiring it. This matters more than a typical availability question because [[North-Star]] names **the lost detail** as a failure mode: a detail the GM cannot retrieve mid-sentence does not exist.

**Needed:** a one-line commitment. *Retrieval works with no connectivity* is a requirement; *we will probably be fine* is not.

---

### G9 — Deletion behaviour has a deadline that the "decide later" posture does not respect

**Blocks:** any correction or deletion story.

[[Rollback-and-Repair]] is honest that the repair model may be overkill and recommends the cheapest option that survives contact with a real error. Correct posture. But it also identifies one decision that cannot be deferred: **if deletion is built to clean up references, the information repair would need is destroyed at the moment of deletion,** and repair becomes impossible to add later without a migration.

**Needed:** a yes/no on preserving tombstones. Nothing else in this area needs deciding now.

---

### G10 — No glossary, and the vocabulary has known collisions

**Blocks:** consistency across every story, and it will bite hardest with an AI development team, which will silently normalise inconsistencies rather than flag them.

The vocabulary is largely defined, but scattered across five documents, with live contradictions:

- **`visibility` values.** The repo `README.md` says `gm | player-ro | player-rw`. [[Players-and-Characters]] says it should be `gm | player`, with authorship tracked separately. The README is now wrong.
- **Quest vs Arc.** Defined crisply in [[Information-Architecture]]; live content still conflates them.
- **Event vs Encounter.** Used interchangeably across documents. [[Information-Architecture]] treats Event as the node type; the encounter ladder in [[Arcs]] uses Encounter. If these are the same thing, say so.
- **Node types, states, and lifecycles** are individually well specified — arc states, the `speculative / potential / used` ladder, event `planned / fact`, canon event statuses, quest states — but nowhere collected.

**Needed:** one glossary page. Cheap, and it unblocks consistency everywhere at once.

---

### G11 — [[Open-Requirements]] no longer reflects what has been decided

**Blocks:** nothing directly. Included because it is a live hazard.

Several items still marked **[blocking]** have since been resolved elsewhere:

| Open-Requirements item | Actually resolved in |
|---|---|
| §1 — do players need individual identity | [[Players-and-Characters]] — attribution, not permissions |
| §7 — what happens when a character dies | [[Players-and-Characters]] — a state, not a deletion |
| §8 — what does prep week look like | [[Prep-Rhythm]], [[Device-Context]], [[Update-Cadence]] |
| §2 — what counts as a meaningful interaction | [[Session-Capture]] — largely, pending contact with real sessions |

Anyone — human or AI — reading `_design/` in the recommended order will treat settled questions as open. Reconciling the index costs little and prevents rework.

---

## Provisional epic map

Offered as evidence of readiness rather than as the deliverable. This is what the gaps look like when projected onto a candidate structure.

| # | Candidate epic | Readiness | Held up by |
|---|---|---|---|
| 1 | Capture what happened in a session | **Ready** | — |
| 2 | Find anything, fast, at the table | **Ready** | G8 |
| 3 | Know the next session is covered | **Ready** | — |
| 4 | Author and connect campaign material | **Near-ready** | G2, G6 |
| 5 | Bring in outside material and integrate it | **Blocked** | G7, G2 |
| 6 | Surface what could not have been noticed | **Blocked** | G3, G4 |
| 7 | Run a thread across a campaign (arcs) | **Near-ready** | G2, G3 |
| 8 | Feel the world moving without you (canon, off-screen) | **Near-ready** | G1 scope, canon recording depth |
| 9 | Players consult the record of their own adventure | **Near-ready** | G5, G1 |
| 10 | Players contribute to the record | **Near-ready** | G5 |
| 11 | Control what the party knows | **Near-ready** | G5 |
| 12 | Keep the record trustworthy | **Blocked** | G9 |
| 13 | Get started (import, first run) | **Blocked** | G7 |
| 14 | Pace the campaign (density, budget, convergence) | **Blocked** | G4, campaign horizon |

Four ready or near-ready epics — 1, 2, 3, and 4 — cover the GM's core loop and could carry a first release on their own.

---

## Decisions requested, in order

Each is a product decision. None requires technical design first.

1. **What is the first release?** Which surface, which capabilities, expressed as user value. *(Unblocks: everything)*
2. **Is the graph model adopted as the domain model?** Adopt, defer, or reject. *(G2)*
3. **Where is the line between surfacing and authoring?** Connections and gaps / plus branches / plus content. *(G3)*
4. **Does anything reach the players automatically?** *(G5)*
5. **Are tombstones preserved on deletion?** Yes or no. Deadline-sensitive and cheap. *(G9)*
6. **Does retrieval work with no connectivity?** *(G8)*
7. **Does the campaign have a known length?** *(G4, epic 14)*
8. **How much canon must be recorded before Floor 6?** *(epic 8)*
9. **Ratify: intersection notes live on the edge.** Closes a contradiction rather than opening a question. *(G6)*
10. **Write the glossary and correct the `visibility` vocabulary in `README.md`.** *(G10)*

Items 9 and 10 are reconciliation, not deliberation, and can be done without a decision meeting.

---

## Recommended path to a first backlog

1. Answer decisions 1 through 3. These three carry most of the blocked scope.
2. Reconcile [[Open-Requirements]], write the glossary, fix the `visibility` vocabulary.
3. Write epics 1–4 and 9–11 in full, with stories and acceptance criteria.
4. Write epics 5–8 and 12–14 at epic level only, with their blocking decisions recorded as the entry criteria for elaborating them.

That produces a backlog a development team can start against, with the unresolved areas visible as decisions rather than hidden as ambiguity.
