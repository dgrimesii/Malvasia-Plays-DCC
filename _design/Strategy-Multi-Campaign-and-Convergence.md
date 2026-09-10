---
type: design
status: draft
visibility: gm
tags: [strategy, multi-campaign, convergence, chronicle, scope]
---

# Strategy: Multi-Campaign and Convergence with Chronicle

Two strategic considerations raised together: that this tool need not be specific to one campaign, and that it may eventually share a core with `Chronicle-MagersCampaign`.

**Nothing here changes Release 1 scope.** The purpose is to identify which near-term choices are cheap to keep open and which are expensive retrofits — and to say plainly where the two ideas would inflate delivery if allowed to.

---

## Part 1 — Multi-campaign

### The distinction that matters

**Optionality is cheap. Capability is expensive.** Conflating them is how a single-user tool acquires an accounts system before it has a working feature.

| Cheap now, painful later | Expensive now, cleanly deferrable |
|---|---|
| A campaign container exists, even with exactly one campaign in it | Accounts, authentication, invitations |
| Entity identifiers are unique within a campaign, never assumed globally unique | Tenancy isolation, per-campaign access control |
| A person is a first-class thing, with a **role held per campaign** | Sharing, joining, campaign switching in the interface |
| Visibility is a property of data, not a behaviour of a particular view | Cross-campaign search, reuse, or content libraries |

The left column costs almost nothing to adopt in R1 and is a migration if adopted later. The right column costs a great deal and loses nothing by waiting.

### The one that quietly matters most

[[Players-and-Characters]] collapses identity to attribution — *"a name on a note, not accounts and gates."* Correct for one campaign, and it should stay.

But multi-campaign breaks a hidden assumption inside it: **the same person holds different roles in different campaigns.** The GM here is a player elsewhere. So "the GM" cannot be a singleton baked into the model; it is a role a person holds *in a campaign*.

That is still not an accounts system. It is:

```
Person --holds_role(gm | player)--> Campaign
```

Three fields, no permissions machinery, and it is the difference between adding a second campaign later and rewriting the knowledge model to do it.

### Visibility must be data, not view behaviour

Already an R1 obligation in [[Release-Plan]] for a different reason — R2 needs it. Multi-campaign is a second, independent argument for the same thing.

Worth stating explicitly because the alternative is tempting and common: enforcing visibility by simply not rendering something in a particular interface. That works exactly once, for exactly one campaign, and is invisible until it fails.

### What R1 should not do

No accounts, no login, no sharing, no campaign switcher, no permissions model. [[First-User]] holds: one user, who is the builder. The structural choices above are enough to keep the door open.

---

## Part 2 — Convergence with Chronicle

### What Chronicle actually is

Worth correcting one framing before building on it. `Chronicle-MagersCampaign` describes itself as a DM tool and campaign log manager, and its structure is **an admin surface plus a read-only player view** — not a player-authoring tool with a separate GM area.

All authoring happens in the admin surface: session intake with OCR of handwritten notes, AI-assisted round filling, a delta review queue with explicit approval before publish, integrity gap checking, and version backups. The player view is browse and graph, read-only.

The role that surface actually serves is **keeper of the record**. In Magers that happens to be a player; in this campaign it would be the GM. That is a useful abstraction: the authoring role is orthogonal to whether the person is a GM or a player.

So the two systems are not two halves of one product waiting to be joined. They are **two record-keeping tools with overlapping models and different subject matter.**

### The seam already exists, and it is in the right place

Chronicle's v4 schema puts a `mechanics` / `narrative` two-layer split on every entity type. Mechanical facts are structured and queryable; prose for human readers sits beside them.

That is very close to the correct cut for convergence:

- **`narrative` is system-agnostic.** Sessions, NPCs, locations, quests, items, lore, factions, relationships — all portable between game systems.
- **`mechanics` is system-specific.** Combat rounds, initiative slots, damage values, reliability, ability harvesting from D&D Beyond — none of it means anything outside 5e.

And [[Scope]] has already excluded exactly the system-specific half from this tool: no stats, no rules enforcement, no rules lookup, no combat resolution. **That exclusion, made for unrelated reasons, is what makes this tool's core portable.**

### Where the models agree

| Concept | Chronicle | This tool | Fit |
|---|---|---|---|
| Sessions, NPCs, locations, items, factions, lore | Present, mature | Present | Direct |
| Quests with status, objectives, progress | `quest_ledger` | Quest, per [[Information-Architecture]] | Direct |
| Typed relationships between entities | `entity_relationships`, closed vocabulary | Typed directed edges | **Subset** — see below |
| Graph as a first-class view | D3 force-directed, both surfaces | [[Interface-Direction]] table view | Same instinct |
| AI proposes, human approves before commit | Delta review queue | [[Constraint-Manner-and-Intent]] Part 2 | **The same rule, independently arrived at** |
| Synthetic fixtures, safe test mode | Built and running | Required by [[Shippable-Increment]] | Prior art worth copying outright |

The last two are the strongest signal that these are the same kind of system underneath.

### Where the models genuinely conflict

Four, in order of difficulty.

**1. Utterance versus claim.** Chronicle has a `reliability` field on lore and bestiary entries — a coarse gesture at the same problem. It does not separate *what was said* from *whether it is true*, which [[Facts-and-Revelation]] treats as foundational and [[Release-Plan]] makes an R1 obligation. This is the sharpest incompatibility and the one that cannot be retrofitted cheaply on either side.

**2. Visibility enforcement.** Chronicle's cohorts are admin-only by being absent from the player HTML file. Visibility is partly a property of code rather than of data. Converging would require moving it into the data — a real change to a running system.

**3. Edge expressiveness.** Chronicle's `entity_relationships` carries type, session, and notes with a closed vocabulary. [[Information-Architecture]] additionally wants direction, `visibility`, `status`, and `established_in`. Chronicle's shape is a strict subset, so convergence means extending rather than replacing. Good news.

**4. Who authors the record of play.** Here the GM captures, and player notes are attributed content that never becomes canon. In Chronicle the log *is* the record, produced by the keeper from session notes. Merged, "what happened" would have two candidate authorities. That needs a stated rule before any merge, not during one.

**Arcs are simply absent from Chronicle.** Not a conflict — net-new, and additive.

### The non-technical problem

Chronicle serves a campaign run by someone else. A shared substrate means another GM's campaign record lives inside a system owned and operated by a player in that campaign.

**That is a consent and ownership question, not an architecture question**, and it does not get easier by being deferred. Anything beyond "these two tools happen to share a schema" needs that conversation first.

### The scope-inflation risk, stated plainly

Chronicle is precisely the set of things [[Scope]] excludes: combat detail, mechanical tracking, rules-adjacent structure. A "shared core" is a legitimate idea and the gravitational pull of it is toward this tool absorbing that feature set.

**The guardrail: convergence is about the data model, never the feature set.** Two products, one substrate. If a convergence argument ever ends with "so we should also track combat rounds here," the argument has gone wrong.

---

## Recommendation

**Do not integrate. Do preserve the option, one-directionally.**

- **Chronicle changes nothing.** It is a running system holding a live campaign, and the cost of any migration lands on real play.
- **This tool designs so that a mapping to Chronicle's schema is writable.** That is a document, not code — a compatibility note maintained alongside the model, checked when the model changes.
- **Borrow freely in the other direction.** The `mechanics` / `narrative` split, the `entity_relationships` shape, the delta-review approval pattern, the fixture and safe-test-mode discipline — all are proven and all fit [[Shippable-Increment]]'s requirements. Reinventing them would be waste.

---

## Consequences for the near-term backlog

**Added to R1 as thin structural requirements — not features:**

- A campaign container, holding exactly one campaign.
- Person as a first-class thing, with a role held per campaign.
- Identifiers unique within a campaign, never assumed globally unique.
- Visibility as a property of data, not of a rendering surface. *(Already required for R2.)*

**Explicitly not in R1:** accounts, authentication, sharing, permissions, campaign switching, cross-campaign anything.

**Added as artifacts:**

- A compatibility note mapping this model to Chronicle's schema, maintained as the model changes.
- The glossary required by [[Epic-Writing-Standard]] should mark which terms are system-specific and which are not. Most will be portable, and knowing which are not is exactly the information convergence needs.

**One decision to revisit:** [[Backlog-Readiness]] §G2 asks whether the graph model is adopted. Chronicle independently arrived at an entity-and-relationship model with a graph view, from a different game system and a different authoring role. That is evidence in favour, and worth weighing when that decision is made.
