# Design

Design documents for **Storyteller** — a tool for running a tabletop campaign, deliberately system- and campaign-agnostic. Not campaign content; nothing here is part of the game record.

These describe what the tool should do and why. Epics that consume them live in [`_backlog/`](../_backlog).

A note on one word: **canon** has a precise meaning in these documents — facts sourced from an author external to the campaign, treated as immutable. See [[Glossary]]. It does not mean "settled" or "official" when used here.

---

## Start here

Read these in order. Four documents, and they carry most of the reasoning.

1. **[[North-Star]]** — what the whole thing is for. Decide against this when anything else is unclear.
2. **[[Glossary]]** — every term used in an epic, written for someone who has never played a tabletop RPG. Prerequisite for everything below.
3. **[[Scope]]** — what Storyteller does not do. The exclusions are load-bearing; they're what keeps the model portable.
4. **[[GM-Considerations]]** — the recurring judgment calls the tool supports but never makes.

Then, depending on what you need:

- Building or reviewing the model → **The model**, below.
- Working on an epic → **Delivery**, below.
- Asking whether this generalizes beyond one campaign → **Strategy**, below.

---

## The model

How Storyteller represents a campaign.

- **[[Information-Architecture]]** — the graph model: nodes, edges, quests vs. arcs, investment.
- **[[Facts-and-Revelation]]** — utterance vs. claim vs. belief, and why conflating them is the costliest capture error available.
- **[[Names-and-Aliases]]** — names as facts rather than headers; multiple simultaneous names with different audiences.
- **[[Identity-and-Reconciliation]]** — identifiers, and merging two records that turn out to be one thing.
- **[[Visibility-Model]]** — what the party knows, held per fact and per relationship rather than per document.
- **[[GM-Player-View-and-Transparency]]** — what each side sees, and what the difference is for.
- **[[Off-Screen-Events]]** — things happening where the party isn't; the `planned`/`fact` and `speculative → potential → used` states.
- **[[Players-and-Characters]]** — people, characters, attribution, and roles held per campaign.
- **[[Entitlement-Model]]** — who may do what, kept separate from who knows what.
- **[[Knowledge-Assets]]** — what the record accumulates and what it's worth.

## Behaviour

What the tool does with the model.

- **[[Session-Capture]]** — what gets recorded from a session, and the two-stage human-in-the-loop intake that turns notes into record changes. The near-term deliverable.
- **[[Arcs]]** — how arcs behave over a campaign: emergence, co-authorship, projection, merging, density.
- **[[Canon]]** — how the party's story relates to a written one: proximity, fidelity, extension, supersession.
- **[[Prep-Rhythm]]** — how preparation actually happens between sessions, and what that asks of the tool.
- **[[Retrieval-Tiering]]** — what needs to be instant at the table versus what can take a moment.

## Interface

- **[[Interface-User-Stories]]** — what each user needs to do, from their perspective.
- **[[Interface-Direction]]** — text-primary, visualization on demand; the four jobs of a visualization.
- **[[Device-Context]]** — where this gets used, and what that constrains.

## Constraints

Hard rules, not preferences.

- **[[Constraint-Manner-and-Intent]]** — the AI never generates manner, intent, or emotional state. Those come from the GM or from player notes.
- **[[First-User]]** — one user, who is the builder. No accounts, no sharing, no permissions machinery.

## Store and operations

- **[[Store-and-Access]]** — where the record lives.
- **[[Migration]]** — moving from flat files to the store without losing the campaign record.
- **[[Hosting-Implications]]** — what running this actually requires.
- **[[Multi-Campaign-Hosting]]** — what changes when there is more than one campaign.
- **[[Access-Recovery]]** — getting back in when something breaks.
- **[[Rollback-and-Repair]]** — undoing bad data. Undecided; possibly overkill.

## Strategy

Where this goes beyond one campaign.

- **[[Strategy-Multi-Campaign-and-Convergence]]** — multi-campaign optionality, and the deliberate divergence from Chronicle. Which near-term choices are cheap to keep open and which are expensive retrofits.
- **[[Shared-Core]]** — what Storyteller and Chronicle would actually have in common, and where the boundary between them falls.

## Delivery

- **[[Roadmap]]** — prerequisites and the path through them.
- **[[Release-Plan]]** — R1 (GM) and R2 (players), and what each obliges.
- **[[Sequencing]]** — what has to come before what, and why.
- **[[Shippable-Increment]]** — functional, non-breaking, testable, demoable. Not necessarily useful.
- **[[Epic-Writing-Standard]]** — how an epic is written and what it must reference.
- **[[Backlog-Readiness]]** — whether an epic is ready to start; open decisions with deadlines.
- **[[Update-Cadence]]** — how often these documents are revisited.
- **[[Verification-and-Challenge]]** — the challenger role: given the artifact, not the reasoning, working from a fixed question set.

## Open

- **[[Open-Requirements]]** — consolidated requirements questions, blocking ones marked.
