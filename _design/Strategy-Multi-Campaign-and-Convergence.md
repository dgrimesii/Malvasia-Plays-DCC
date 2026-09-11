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

### Record-keeping is a separate attribute from role

Chronicle demonstrates this directly. There, the person maintaining the record is a **player acting as the table's scribe** — not the DM, who does not participate in the tool at all.

So two independent facts about a person in a campaign:

| | Magers | This campaign |
|---|---|---|
| Role | Player | GM |
| Keeps the record? | Yes | Yes |

Same person, same record-keeping function, opposite roles. Collapsing the two would make the model wrong for one campaign or the other.

### Visibility must be data, not view behaviour

Already an R1 obligation in [[Release-Plan]] for a different reason — R2 needs it. Multi-campaign is a second, independent argument for the same thing.

Worth stating explicitly because the alternative is tempting and common: enforcing visibility by simply not rendering something in a particular interface. That works exactly once, for exactly one campaign, and is invisible until it fails.

### What R1 should not do

No accounts, no login, no sharing, no campaign switcher, no permissions model. [[First-User]] holds: one user, who is the builder. The structural choices above are enough to keep the door open.

---

## Part 2 — Convergence with Chronicle

### What Chronicle actually is

**Chronicle is a player-side artifact end to end.** The DM does not use it, does not author in it, and does not gate anything in it. It is maintained by one player acting as scribe for the table, who digitizes handwritten session notes so the rest of the party has a shared record of what happened.

Its labelling obscures this. The "admin" surface is the **scribe's workbench** — session intake with OCR of handwritten notes, AI-assisted round filling, a delta review queue with approval before publish, integrity gap checking, backups. The "player" view is the finished artifact the rest of the table reads.

That reframes the relationship between the two systems considerably, and in a favourable direction.

### Chronicle is a mature implementation of the half this tool has barely specified

The player side of this tool is thin. [[Interface-User-Stories]] gives players lookup and short attributed notes; [[Players-and-Characters]] settles that notes are shared and attributed. That is roughly a page of requirements for three users, deferred entirely to R2.

Chronicle is that half, built, running, and refined across sessions — with an authoring workflow, an approval gate, integrity checking, a graph view, and a test suite.

**It is not a competing authority over "what happened."** It is the party's record, from the party's vantage, maintained by one of them. This tool already has a place for exactly that: player-authored attributed content, distinct from GM knowledge. Chronicle populates that place far better than anything specified here.

### The scribe is a product concept this tool does not have

[[Session-Capture]] assumes the GM captures. [[Interface-User-Stories]] assumes each player writes their own short notes. Neither anticipates **one player producing the shared record on behalf of the table**, which is what Chronicle does and what the other Magers players get value from.

That is a different shape from "everyone writes notes," and it is a plausible and cheap variant for R2 here — one that concentrates effort on the person willing to do it rather than depending on three people to write things down.

Worth carrying into R2 planning as a real option rather than discovering it later.

### The seam is a shared entity core, not a per-entity mechanics split

Chronicle's v4 schema puts a `mechanics` / `narrative` two-layer split on every entity type — a reasonable first read, but not the sharpest cut. The clearer frame: both tools describe the same underlying things — people, places, events, quests, objects — and each attaches its own point of view to them. Two contexts on one shared core, not two competing models of the same data.

- **The core, shared.** Entity, Identifier, Name, Alias, Relationship — the things that exist in the game world, and their identity. Chronicle and Storyteller are both, at root, describing the same people, places, events, quests, and objects.
- **Storyteller's context.** Fact, Utterance/claim/belief, Visibility, Reveal, Materialize, Investment, Arc — actions, interactions, and narrative weight attached to the shared things. System-agnostic by construction; see [[Glossary]].
- **Chronicle's context.** Combat rounds, initiative slots, damage values, reliability, ability harvesting from D&D Beyond — game-table mechanics attached to the same shared things. None of it means anything outside 5e.

And [[Scope]] has already excluded exactly Chronicle's context layer from this tool: no stats, no rules enforcement, no rules lookup, no combat resolution. **That exclusion, made for unrelated reasons, is what makes this tool's core portable.**

### Where the models agree

| Concept | Chronicle | This tool | Fit |
|---|---|---|---|
| Sessions, NPCs, locations, items, factions, lore | Present, mature | Present | Direct |
| Quests with status, objectives, progress | `quest_ledger` | Quest, per [[Information-Architecture]] | Direct — see handoff note below |
| Typed relationships between entities | `entity_relationships`, closed vocabulary | Typed directed edges | **Subset** — see below |
| Graph as a first-class view | D3 force-directed, both surfaces | [[Interface-Direction]] table view | Same instinct |
| AI proposes, human approves before commit | Delta review queue | [[Constraint-Manner-and-Intent]] Part 2 | **The same rule, independently arrived at** |
| Synthetic fixtures, safe test mode | Built and running | Required by [[Shippable-Increment]] | Prior art worth copying outright |

The last two are the strongest signal that these are the same kind of system underneath.

**Where Quest crosses the seam.** Chronicle's `quest_ledger` status (given → in-progress → completed / failed / abandoned) and Storyteller's own quest state (`planned` → `fact`, `speculative` → `potential` → `used` effort, per [[Glossary]]) are not two views of the same axis. They are sequential, and they meet at exactly one point: **Reveal**. Before reveal, a quest belongs entirely to Storyteller's side, invisible to Chronicle — pure GM planning. After reveal, everything about its progress belongs to Chronicle, the party's own view of a thing they now know about. Neither model needs to represent the other's half; the handoff is the whole relationship.

### Where the models genuinely differ

Three, and two of them are additive rather than conflicting.

**1. Utterance versus claim — the real one.** Chronicle has a `reliability` field on lore and bestiary entries, a coarse gesture at the same problem. It does not separate *what was said* from *whether it is true*, which [[Facts-and-Revelation]] treats as foundational and [[Release-Plan]] makes an R1 obligation. This is the sharpest incompatibility and cannot be retrofitted cheaply on either side.

Note the asymmetry in why: a party-side record has less need for it, since the party has no privileged knowledge to protect. But it still matters — the party is routinely lied to, and a record that flattens *"the innkeeper told us"* into *"it is true"* misleads its own readers.

**2. Chronicle has no concept of revealed knowledge — and does not need one.** Its entire content is already known to the party. What is admin-only there — cohorts, deferred gaps, the prompt improvement log — is **workflow state the scribe keeps out of the shared view**, not secrets. That is a different thing from GM revelation, and my earlier reading of it as weak visibility enforcement was wrong.

Convergence therefore *adds* a concept Chronicle lacks rather than fixing one it implements poorly. Additive, and cheaper than it looked.

**3. Edge expressiveness.** Chronicle's `entity_relationships` carries type, session, and notes with a closed vocabulary. [[Information-Architecture]] additionally wants direction, `visibility`, `status`, and `established_in`. Chronicle's shape is a strict subset, so convergence means extending rather than replacing.

**Arcs are simply absent from Chronicle.** Not a conflict — net-new, and additive.

### The ownership question, now much smaller

An earlier draft framed this as another GM's campaign record living in a player-owned system. That overstated it.

**No DM material is in Chronicle and none would be.** John's prep, secrets, and plans were never there; the record is the party's own observations, kept by one of them, shared with the rest. That is a table arrangement the group already has and already benefits from.

What remains is narrower and worth asking once, not solving in advance: **if a shared substrate ever existed, would that DM want to contribute to or gate any of it?** Today he does not participate at all, so the answer is currently moot — but it is his campaign, and a system that quietly grew a GM surface around his game would be a different proposition from a scribe's notebook.

### The scope-inflation risk, stated plainly

Chronicle is precisely the set of things [[Scope]] excludes: combat detail, mechanical tracking, rules-adjacent structure. A "shared core" is a legitimate idea and the gravitational pull of it is toward this tool absorbing that feature set.

**The guardrail: convergence is about the data model, never the feature set.** Two products, one substrate. If a convergence argument ever ends with "so we should also track combat rounds here," the argument has gone wrong.

---

## Recommendation

**Do not integrate. Do preserve the option, one-directionally.**

- **Chronicle changes nothing.** It is a running system holding a live campaign, and the cost of any migration lands on real play.
- **This tool designs so that a mapping to Chronicle's schema is writable.** That is a document, not code — a compatibility note maintained alongside the model, checked when the model changes.
- **Borrow freely in the other direction.** The `mechanics` / `narrative` split, the `entity_relationships` shape, the delta-review approval pattern, and the fixture and safe-test-mode discipline are all proven and all fit [[Shippable-Increment]]'s requirements. Reinventing them would be waste.
- **Treat Chronicle as the reference design for R2**, not merely as a system to be compatible with. It is the player-side artifact, already working, with real users who value it.

This divergence is deliberate, not an oversight — weighed openly here, with the extensibility above kept cheap on purpose so the option stays open without paying for it now.

---

## Consequences for the near-term backlog

**Added to R1 as thin structural requirements — not features:**

- A campaign container, holding exactly one campaign.
- Person as a first-class thing, with a role held per campaign, and record-keeping as a separate attribute from role.
- Identifiers unique within a campaign, never assumed globally unique.
- Visibility as a property of data, not of a rendering surface. *(Already required for R2.)*

**Explicitly not in R1:** accounts, authentication, sharing, permissions, campaign switching, cross-campaign anything.

**Added as artifacts:**

- A compatibility note mapping this model to Chronicle's schema, maintained as the model changes.
- The glossary required by [[Epic-Writing-Standard]] should mark which terms are system-specific and which are not. Most will be portable, and knowing which are not is exactly the information convergence needs.

**Carried into R2 planning:** the scribe as an alternative to per-player note-taking.

**One decision to revisit:** [[Backlog-Readiness]] §G2 asks whether the graph model is adopted. Chronicle independently arrived at an entity-and-relationship model with a graph view, from a different game system and a different authoring role. That is evidence in favour, and worth weighing when that decision is made.
