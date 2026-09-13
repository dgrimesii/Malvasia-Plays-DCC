# Design

Design documents for **Storyteller** — a tool for running a tabletop campaign, deliberately system- and campaign-agnostic. Not campaign content; nothing here is part of the game record.

These describe what the tool should do and why. Epics that consume them live in [`_backlog/`](../_backlog).

A note on one word: **canon** has a precise meaning in these documents — facts sourced from an author external to the campaign, treated as immutable. See [[Glossary]]. It does not mean "settled" or "official" when used here.

---

## Start here

Read these in order. Seven documents, and they carry most of the reasoning.

1. **[[Premise-and-Pillars]]** — why this should work at all, and the one claim the whole design rests on. Written so it can be found wrong.
2. **[[North-Star]]** — what the whole thing is for. Decide against this when anything else is unclear.
3. **[[Constraint-Serves-The-Table]]** — the tool serves the table and never joins it. The rule that caps everything below it, including North Star.
4. **[[Live-Set]]** — the job stated in mechanism terms: keep what the table put in the room findable, and small enough to hold. Carries the GM-side case.
5. **[[Glossary]]** — every term used in an epic, written for someone who has never played a tabletop RPG. Prerequisite for everything below.
6. **[[Scope]]** — what Storyteller does not do. The exclusions are load-bearing; [[Premise-and-Pillars]] supplies the reason behind the mechanics one.
7. **[[GM-Considerations]]** — the recurring judgment calls the tool supports but never makes.

Then, depending on what you need:

- Building or reviewing the model → **The model**, below.
- Working on an epic → **Delivery**, below.
- Asking whether this generalizes beyond one campaign → **Strategy**, below.

---

## The model

How Storyteller represents a campaign.

- **[[Information-Architecture]]** — the graph model: nodes, edges, quests vs. arcs, investment.
- **[[Facts-and-Revelation]]** — utterance vs. claim vs. belief, and why conflating them is the costliest capture error available.
- **[[Claims-and-Resolution]]** — the claim as an object in its own right, resolution as a dated decision, and why `undetermined` is a resource rather than a gap. No probability field anywhere.
- **[[Names-and-Aliases]]** — names as facts rather than headers; multiple simultaneous names with different audiences.
- **[[Identity-and-Reconciliation]]** — identifiers, and merging two records that turn out to be one thing.
- **[[Visibility-Model]]** — what the party knows, held per fact and per relationship rather than per document.
- **[[GM-Player-View-and-Transparency]]** — what each side sees, and what the difference is for.
- **[[Settings-and-Campaigns]]** — a world versus a story told in it; which tier entities, facts, and visibility belong to.
- **[[Off-Screen-Events]]** — things happening where the party isn't; the three event states and the `speculative → potential → used` effort ladder.
- **[[Players-and-Characters]]** — people, characters, attribution, and roles held per campaign.
- **[[Entitlement-Model]]** — who may do what, kept separate from who knows what.
- **[[Knowledge-Assets]]** — what the record accumulates and what it's worth.

## Behaviour

What the tool does with the model.

- **[[Modes-and-Surfaces]]** — the three modes of use and their personas. Inference never runs at the table; search is three distinct surfaces, not one.
- **[[Session-Capture]]** — what gets recorded from a session, and the two-stage human-in-the-loop intake that turns notes into record changes. The near-term deliverable.
- **[[Extraction-Rules]]** — how the narrative content is found inside a document that also holds mechanics and stage directions. The subject test, and what happens to numbers.
- **[[Inference-and-Candidate-Relationships]]** — the detective layer: five signals, clues as the durable unit, the procedural/LLM split, and the store requirements that make any of it buildable.
- **[[Generative-Projection]]** — where the system may propose fiction that hasn't happened. Forward, never backward; investment gates it in reverse.
- **[[Planning-Loop]]** — how prep actually runs: one iterative cycle at two rhythms, hooks as facts, and why convergence is the GM's problem.
- **[[Live-Set]]** — the capped, ranked artefact the table surfaces read from, and the attention budget behind it.
- **[[Arcs]]** — how arcs behave over a campaign: emergence, co-authorship, projection, merging, density.
- **[[Canon]]** — how the party's story relates to a written one: proximity, fidelity, extension, supersession.
- **[[Prep-Rhythm]]** — how preparation actually happens between sessions, and what that asks of the tool. Refined by [[Planning-Loop]].
- **[[Retrieval-Tiering]]** — what needs to be instant at the table versus what can take a moment.

## Interface

- **[[Interface-User-Stories]]** — what each user needs to do, from their perspective.
- **[[Interface-Direction]]** — text-primary, visualization on demand; the four jobs of a visualization.
- **[[Device-Context]]** — where this gets used, and what that constrains. No GM surface targets a phone.
- **[[Player-Scope]]** — what the player surface replaces, the boundary between checking and thinking, and how to pitch it.

## Constraints

Hard rules, not preferences.

- **[[Constraint-Serves-The-Table]]** — the tool serves the table, never joins it. Pull-only surfaces; a write must fit an existing pause; a captured detail is worth less than the moment it costs.
- **[[Constraint-Manner-and-Intent]]** — the AI never generates manner, intent, or emotional state. Those come from the GM or from player notes. Scoped against generation by [[Generative-Projection]].
- **[[First-User]]** — one user, who is the builder. No accounts, no sharing, no permissions machinery.

## Store and operations

- **[[Store-and-Access]]** — where the record lives.
- **[[Migration]]** — moving from flat files to the store without losing the campaign record.
- **[[Hosting-Implications]]** — what running this actually requires.
- **[[Multi-Campaign-Hosting]]** — what changes when there is more than one campaign.
- **[[Access-Recovery]]** — getting back in when something breaks.
- **[[Rollback-and-Repair]]** — undoing bad data. Undecided; possibly overkill. Note that tombstones are inference substrate as well as repair substrate.

## Strategy

Where this goes beyond one campaign.

- **[[Strategy-Multi-Campaign-and-Convergence]]** — multi-campaign optionality, and the deliberate divergence from Chronicle. Which near-term choices are cheap to keep open and which are expensive retrofits.
- **[[Shared-Core]]** — what Storyteller and Chronicle would actually have in common, and where the boundary between them falls.

## Delivery

- **[[Roadmap]]** — prerequisites and the path through them.
- **[[Release-Plan]]** — the release axis: between sessions, then at the table. Both releases serve both people.
- **[[Sequencing]]** — what has to come before what, and why.
- **[[Shippable-Increment]]** — functional, non-breaking, testable, demoable. Not necessarily useful.
- **[[Epic-Writing-Standard]]** — how an epic is written and what it must reference.
- **[[Backlog-Readiness]]** — whether an epic is ready to start; open decisions with deadlines.
- **[[Update-Cadence]]** — how often these documents are revisited.
- **[[Verification-and-Challenge]]** — the challenger role: given the artifact, not the reasoning, working from a fixed question set. See also the premise falsification condition in [[Premise-and-Pillars]].

## Open

- **[[Open-Requirements]]** — consolidated requirements questions, blocking ones marked.
