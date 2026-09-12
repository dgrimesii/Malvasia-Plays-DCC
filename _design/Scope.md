---
type: design
status: draft
visibility: gm
tags: [scope, boundaries]
---

# Scope

What this tool is and isn't. Referenced from [[North-Star]] and [[Open-Requirements]].

The mechanics exclusions below were originally justified on portability grounds. [[Premise-and-Pillars]] supplies the better reason: **every system resolves what happens; none of them supplies what it means.** Storyteller is the meaning layer, which is why it never touches resolution.

---

## The purpose

**Facilitate play at the table.** For both the GM and the players. Everything else is instrumental.

The tool exists so the GM can prepare efficiently and react confidently, and so the players can remember what they know and plan with it. It is a narrative instrument, not a record to be read for its own sake.

**Bounded by [[Constraint-Serves-The-Table]]:** facilitating play means serving the human interaction at the table, never competing with it.

---

## The player side has the same purpose

Not a chronicle of their adventure. A **working reference** that helps them play better.

Fuller treatment in [[Player-Scope]], including what the surface replaces, the boundary between where players *check* and where they *think*, and why it must be answer-shaped rather than browsable.

The actual questions they'll bring to it:

- *What did that NPC tell us about the tunnels?*
- *What happened three sessions ago at the checkpoint?*
- *Who did we promise what to?*
- *What haven't we followed up on?*

All retrieval and planning. None of it reading for pleasure.

### What that requires

**Attributed, not asserted.** The important one. When a player asks what they were told, the answer is *"the Warden told you the tunnels flood at night"* — never *"the tunnels flood at night."*

The distinction from [[Facts-and-Revelation]] does double duty here:

| | GM sees | Players see |
|---|---|---|
| Utterance | The Warden said X | The Warden told you X |
| Claim status | X is false | *undetermined* |
| Belief | The party believes X | — |

If the player view rendered claims as world facts, it would silently spoil every lie in the campaign, and players would plan against certainties they haven't earned. **Everything in the player view carries its source.**

Refined by [[Claims-and-Resolution]]: the players see a claim's resolution as `undetermined` until it is revealed, and that presentation must be **identical** whether the GM has decided false, decided true, or not decided at all. Uniformity there is the information-hiding guarantee, and it is testable.

**Searchable by entity.** They'll arrive with a name — an NPC, a place, a faction — and want everything they know about it in one place, across sessions.

**Organized for planning, not chronology.** What's unresolved, what was promised, what's still owed. A pure session-by-session list makes them scan for what they need.

**Available when they need it.** Which may well be mid-session, at the table, while deciding what to do. That answers part of the live-at-table question in [[Open-Requirements]] §8 — the player surface likely needs it too, not just the GM's. **Read-only there**, per [[Constraint-Serves-The-Table]]: a player-facing write at the table is prohibited unconditionally.

---

## Out of scope

**Character sheets, stats, and progression.** HP, mana, levels, gear, modifiers. These live wherever they already live.

**Rules enforcement.** No validating mob counts against tiers or checking an encounter is mechanically sound. The GM knows the rules.

**Rules lookup.** Not a searchable rulebook. A campaign's system reference material sits with the campaign record as shared reference, not as a query surface.

**Producing a written story.** No auto-generated prose narrative, no publishable chronicle. The record serves the next session.

**Combat resolution, dice, initiative.** Not a play aid in that sense.

**Resolution machinery of any kind** — including for the exploration and social pillars. Some systems resolve those with skill checks, reaction rolls, or NPC and faction attitude tracks. Those are resolution, and they are out. The nearest miss is worth naming: an attitude track holds a *value*, while the store holds the accumulated facts that justify it and the history of how it moved. A GM with the track and no record has a number they cannot explain. See [[Premise-and-Pillars]].

### Combat is excluded from prep and resolution, not from capture

Worth stating explicitly, because the exclusions above invite the wrong inference.

A fight produces deaths, grudges, debts, reputation, and the thing somebody said while bleeding. Those are facts and relationships the store must hold, and they are among the most consequential events a campaign generates. **The tool never helps run a combat and must fully capture what came out of one.**

Otherwise the parser gets built to skim exactly the sessions that matter most.

---

## Where mechanics do matter

Only where they carry narrative weight.

*"Hilda used persuasion to turn the Warden at the moment Z's aggression had closed every other door"* is worth capturing — a character acting characteristically, at a hinge point, with consequences.

*"Hilda's persuasion modifier is +3"* is not.

**The use of a capability at a significant moment is narrative. The capability's numbers are not.**

### Descriptive knowledge of abilities is useful

Knowing what a skill or spell *does*, described rather than quantified, adds to the story:

- *Frost Scar* leaves a lingering chill — so the room, the target, and the aftermath can be described
- Trick archery is a performance skill — so its use is showy, watched, and read by onlookers
- Improvised weapons means Z fights with whatever's at hand — which shapes how a fight is narrated

That belongs in the record. Damage dice don't.

---

## Corrections to earlier framing

**"Session records are chapters, not minutes"** — written in [[North-Star]], and wrong. It implies the record is meant to be read as narrative. Records exist to make the next session better and to support recall at the table.

**The debrief is something the GM does, not something the tool produces.** Recounting what was behind the screen is a pleasure of running the game. The tool's job is to have the material retrievable — abandoned branches, projections, manner notes — not to write the retelling.

---

## The test

> Does this help at the table, or in preparing for the table?

Applies to both users. If it produces an artifact for reading rather than for playing, it's out of scope.

**Then apply the second test**, from [[Constraint-Serves-The-Table]]: does it wait to be asked, does it fit in a pause the conversation already has, does it produce something the people would otherwise have produced themselves, and can it lose to the conversation without breaking anything? A capability can pass the first test and still fail this one, and the constraint wins.
