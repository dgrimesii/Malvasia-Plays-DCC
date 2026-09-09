---
type: design
status: open
visibility: gm
tags: [requirements, open-questions]
---

# Open Requirements

Consolidated from across `_design/`, plus questions not yet asked anywhere. These are **requirements** questions — what the system must do and for whom. Design and architecture choices stay deferred.

Marked **[blocking]** where other requirements depend on the answer.

---

## 1. Access and identity

**[blocking] Do players need individual identity in the system?**
Everything about `player-rw`, note ownership, and per-player visibility assumes the system knows who's who. If yes, that's accounts, sessions, and permissions. If no, the player surface is one shared read-only view and half the player stories collapse.

**Does the GM see player notes?**
Arguments both ways: rich signal about what the table finds interesting, versus players writing more freely when unobserved. Affects whether notes need a private tier at all.

**Is there a shared party-visible layer?**
Three possible tiers: private to author, shared with party, GM-revealed. Two of the three might be enough.

**What happens when a player leaves or joins mid-campaign?**
Their character's dossier, their notes, their arcs. Realistic over a long campaign.

---

## 2. Capture

**[blocking] What counts as a "meaningful interaction"?**
Investment inference — the precondition for arcs — needs a recordable unit. Is it GM-flagged during write-up, or derived from narrative text? Nothing about arc discovery works until this is defined.

**[blocking] When does session capture happen, and by whom?**
Live during play, immediately after, or days later? The GM alone, or do player notes contribute? This determines whether the tool must work *during* a session or only between them — which cascades into device, latency, and offline requirements.

**How much detail must a session record hold?**
Enough to reconstruct events, or enough to feed inference? The second is a higher bar.

**Do players capture during or after sessions?**
At-the-table note-taking is a different product from between-session reflection.

---

## 3. What the AI may propose

**[blocking] Where is the line between surfacing and authoring?**
Established: observation is always welcome, and nothing is applied without approval. Unresolved: may it propose *content* — a projection, a climax, a story beat — or only *connections* and *gaps*?

**May it propose branches on an existing projection?**
Narrower than proposing whole projections — "you haven't considered she might do nothing." Possibly the more useful version.

**How strong must a pattern be before a ticket fires?**
Too eager and tickets get dismissed reflexively, killing the feature. Needs a target, even a rough one.

**Should the system ever push back?**
Density awareness implies it might say "this is too connected, let the next one be a dungeon." Is that in scope, or purely the GM's call?

---

## 4. Canon

**[blocking] How much canon must be recorded, and when?**
Floors 1–5 need almost none. Floor 6 onward needs enough to compute proximity. That's a real data-acquisition workload with a deadline — and it can't be answered without knowing how proximity gets computed and how precise it must be.

**Can the party affect canon outcomes, or only experience them?**
Determines whether divergence is an edge case or a core mechanic.

**Does divergence need to be visible to players?**
Knowing the campaign has left canon is a powerful narrative fact — or a spoiler about what canon was.

**Has anyone at the table read the books?**
Changes proximate events from mystery to dramatic irony, per player. Needs answering before Floor 6 regardless of tooling.

**Do canon events feed the arc tree?**
A canon figure the party comes to care about from a distance could carry real weight.

---

## 5. Campaign shape

**[blocking] Does the campaign have a known length?**
Arc budgeting, convergence planning, and pacing warnings all require a horizon. If open-ended, pacing has to be judged some other way and several proposed features lose their basis.

**Is arc density measurable in a useful way?**
Counting arc-connected events may mistake quantity for weight — one devastating choice can carry a campaign. If the metric misleads, the pacing feature shouldn't be built.

**How much projection history is worth keeping?**
Enough to see divergence shape, not so much it becomes an unread archive.

---

## 6. Lifecycle events

**[blocking] What happens when a character dies?**
DCC runs on lethality; this will happen. Does the dossier become historical? Do their arcs transfer, resolve, or go dormant? Does the player's new character inherit their notes and relationships? Does the dead character remain in the graph as a node others reference?

**Can arcs merge and split, and what survives?**
Established as needed. Requirements: both handles preserved, evidence unioned with attribution intact, moment of convergence recorded, projections reconciled by the GM.

**Do speculative events that never happen get kept?**
Resolved: kept, as debrief material. Noted here because it constrains storage growth.

**Does anything ever get deleted?**
"Discard unused material" is on the never-do list. Over years, that has consequences worth acknowledging now.

---

## 7. Context of use

**[blocking] Must the tool work at the table, live?**
The table view assumes yes. That imposes latency targets, device constraints, and possibly offline operation. If the answer is "between sessions only," the product is substantially simpler.

**What device, in what conditions?**
Laptop at the table, tablet, phone, second screen. Determines everything about the table view's layout.

**Is connectivity guaranteed where you play?**
In-person weekly game. If not reliable, offline capability becomes a requirement rather than a nicety.

**What is an acceptable retrieval latency mid-session?**
"Seconds" has been the working phrase. A number would be better, since it's the constraint that reduces required prep volume.

---

## 8. Scope boundaries

**Is this one campaign or a system for many?**
Reuse across campaigns changes the data model's assumptions considerably.

**Does the GM need to invent new relationship types during play?**
A closed edge vocabulary is queryable; an open one is expressive. Whether the GM can extend it at runtime is a requirements question, not a design one.

**Is content portability required?**
Export, backup, or migration off this system if it's abandoned. The repo-as-database choice partly answers this, but only partly.

---

## Suggested order of resolution

The blocking questions cluster into three decisions that unlock most of the rest:

1. **Is this a multi-user system?** (§1) — determines whether the player surface exists as a real product.
2. **Must it work live at the table?** (§7) — determines latency, device, and offline requirements.
3. **What gets captured, when, and by whom?** (§2) — determines whether inference, arcs, and investment tracking are possible at all.

Canon workload (§4) and campaign length (§5) can wait, but both have real deadlines — Floor 6 for the first, and the sooner the better for the second.
