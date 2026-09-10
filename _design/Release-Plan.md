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

**Two releases, split by audience.**

- **Release 1 — the GM interface.** Everything the GM needs to prepare, run, and record the campaign.
- **Release 2 — the player interface.** What Julia, Amy, and Sam consult and contribute to.

---

## What this resolves

- The first release is GM-only. No player-facing surface ships in R1.
- The player reveal mechanics open in [[Backlog-Readiness]] §G5 — automatic publishing, bulk reveal, change visibility — are **R2 decisions**, and no longer block R1 story writing.
- [[Retrieval-Tiering]] Part 2, player queries as prep signal, is R2 by definition. It has no source before the player surface exists.

---

## What this does not resolve

**Splitting by audience answers *who first*, not *what smallest*.**

Eleven of the fourteen candidate epics in [[Backlog-Readiness]] are GM-facing. R1 as "all of them" is not an increment — it is the whole GM product, and it would be a long time before anything is usable at a table.

R1 still needs an internal ordering. The recommended shape:

| R1 slice | Epics | What the GM gets |
|---|---|---|
| **1a — the core loop** | Capture a session · Find anything fast · Know the next session is covered | A tool that is genuinely useful at the table and after it. Nothing else is required for this to pay off. |
| **1b — authoring** | Author and connect · Integrate outside material · Get started | Prep moves into the tool rather than around it. |
| **1c — the computed layer** | Surface what could not have been noticed · Run a thread · The world moving without you · Pace the campaign | The features that justify the graph model. All currently blocked on open decisions. |
| **1d — durability** | Keep the record trustworthy | Correction and rollback. |

**1a is the real first release.** It maps exactly to the four ready epics, has no blocking gaps except connectivity (§G8), and delivers the [[North-Star]] failure mode most worth engineering against — the lost detail.

---

## Epic allocation

| # | Epic | Release |
|---|---|---|
| 1 | Capture what happened in a session | R1 · 1a |
| 2 | Find anything, fast, at the table | R1 · 1a |
| 3 | Know the next session is covered | R1 · 1a |
| 4 | Author and connect campaign material | R1 · 1b |
| 5 | Bring in outside material and integrate it | R1 · 1b |
| 13 | Get started — import and first run | R1 · 1b |
| 6 | Surface what could not have been noticed | R1 · 1c |
| 7 | Run a thread across a campaign | R1 · 1c |
| 8 | Feel the world moving without you | R1 · 1c |
| 14 | Pace the campaign | R1 · 1c |
| 12 | Keep the record trustworthy | R1 · 1d |
| 11 | Control what the party knows | **Split** — see below |
| 9 | Players consult the record of their own adventure | R2 |
| 10 | Players contribute to the record | R2 |
| 15 | See what the party knows (GM player-view switch) | R2 |
| 16 | Player attention as a prep signal | R2 |

Epics 15 and 16 are new, promoted out of [[GM-Player-View-and-Transparency]] and [[Retrieval-Tiering]]. Both are GM-facing capabilities that nonetheless depend on the player surface existing, which the earlier map did not make visible.

**Epic 11 splits across releases.** Marking content visible is a GM action and belongs in R1. A player reading it is R2. R1 ships the act with nothing on the other end of it.

---

## What R1 must carry for R2

The cost of an audience split is that R1 can quietly make R2 expensive. Four obligations, all cheap now and painful to retrofit across a campaign's worth of content.

### 1. Everything carries visibility from creation

Per [[Interface-User-Stories]]: anything authored defaults to GM-only until deliberately revealed. If R1 omits the field because nothing consumes it, R2 opens with a retroactive tagging pass over every record in the campaign.

Also adopt the corrected vocabulary now — `gm | player`, per [[Players-and-Characters]] — rather than the `player-ro | player-rw` still in `README.md`.

### 2. Attribution exists from day one

Identity is for attribution, not permissions. Content authored in R1 is the GM's; R2 adds player-authored content alongside it. The author field has to be there for the distinction to mean anything later.

### 3. Utterance, claim, and belief stay separate in capture — **the sharpest one**

[[Scope]] states the rule for the player view: everything carries its source. *"The Warden told you the tunnels flood at night"*, never *"the tunnels flood at night."*

If R1 capture flattens utterances into world facts because the GM knows the difference and no player surface exists, then **R2 cannot be built without re-reading and re-encoding every session record.** Worse, a partial job silently spoils every lie in the campaign the first time a player reads a page.

This is an R1 capture requirement driven entirely by R2, and it is invisible until R2 arrives. It belongs in the acceptance criteria for Epic 1.

### 4. Reveal is recorded as an event

*When* something became visible, not just *that* it is. R2 needs it for "what is new since you last looked", and it cannot be reconstructed after the fact.

Note this also settles the tension flagged in [[Backlog-Readiness]] §G5: a read marker is not knowledge. Recording when a reveal happened is compatible with the single shared knowledge domain in [[Players-and-Characters]].

---

## What R1 gives up

Stated so it is a choice rather than a discovery.

**Investment inference runs on GM observation alone.** [[Session-Capture]] warns that reading engagement from expressiveness systematically under-reads quiet players, and names two corrections that do not depend on performance: player notes, and — per [[Retrieval-Tiering]] — what players look up. **Both are R2.**

So R1's investment features operate without their best correction, during exactly the floors ([[Canon]]: 1–5, the insulated phase) when investment matters most. Two responses, both defensible:

- Accept it. Recurrence is the primary signal per [[Session-Capture]] and is GM-observable.
- Defer the investment-dependent parts of Epic 6 and Epic 7 to after R2, and let R1's arc support be declaration-driven rather than inference-driven.

**The GM cannot check what the party knows.** Epic 15 requires a player view to switch to. [[GM-Player-View-and-Transparency]] calls this a first-class prep capability, and the failure it prevents — referencing something the party never learned — exists from session one.

Cheap mitigation worth considering: R1 renders a read-only player projection for the GM's own use. It is the filtering logic without the surface, it validates obligations 1 and 3 above while they are still cheap to fix, and it becomes R2's foundation rather than throwaway work.

---

## Consequences for the decision list

[[Backlog-Readiness]] decision 1 is now answered at the surface level. Remaining order:

1. **Confirm 1a as the first shippable slice**, or state a different one.
2. Is the graph model adopted? *(§G2)*
3. Where is the line between surfacing and authoring? *(§G3)* — governs all of 1c.
4. Are tombstones preserved on deletion? *(§G9)* — deadline-sensitive, and 1d is late in R1.
5. Does retrieval work with no connectivity? *(§G8)* — blocks 1a, the smallest question with the earliest need.
6. Does the campaign have a known length? *(§G4)*
7. How much canon before Floor 6? *(Epic 8)*

Decision 4 in the original list — does anything reach players automatically — moves to R2 planning. Obligation 4 above is what keeps it open.
