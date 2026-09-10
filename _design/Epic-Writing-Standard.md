---
type: design
status: draft
visibility: gm
tags: [product, backlog, epics, writing-standard]
---

# Epic Writing Standard

How epics and stories are written for this project. Follows from the reviewer role in [[Verification-and-Challenge]].

---

## Settled

**Epics must be legible to a Product Owner with no tabletop roleplaying experience.**

Julia is the one uncorrelated reviewer available. She has never run or played a game of this kind. If an epic cannot be understood and critiqued by her, it cannot be reviewed by anyone outside the builder's own head.

---

## Why this is worth the cost

The obvious benefit is that the review happens at all. The larger one is what the constraint forces:

**An epic legible to an outsider is an epic with no unstated assumptions.** Every place the writing leans on "obviously, a GM needs..." is a place the requirement was never actually stated. Those gaps are invisible to a domain expert and expensive later, when the development team fills them in silently.

This makes the standard useful for Claude Code as well, not only for Julia.

---

## What Julia can critique, and what she cannot

The distinction has to be visible in the writing, or her review time gets spent guessing which is which.

| | She can attack it | Marked how |
|---|---|---|
| **Product reasoning** — is the value claim coherent, is the scope right, do these two epics overlap, is this acceptance criterion observable, is this sequenced sensibly | **Yes.** This is her expertise and it is domain-independent. | Default. Everything not marked otherwise. |
| **Domain assertions** — that a GM must retrieve a detail mid-sentence, that player investment cannot be authored, that expressiveness does not indicate engagement | **No.** She has no basis to judge these and should not be asked to. | Stated explicitly as an assumption, with a link to the design document that establishes it. |

Marking domain assertions is not a formality. It tells her *"take this as given and aim your attention elsewhere"*, which is what makes a review by a non-expert efficient rather than tentative.

It also creates a second benefit: an assumption that cannot be traced to a design document is one nobody has actually decided.

---

## Writing rules

**Define the term once, then use it.** The vocabulary is not removed — it is the product's vocabulary, and stripping it would make the epics useless to the development team. Every domain term links to a glossary entry on first use.

**Explain with a concrete example, not a business analogy.** *"An arc is like a customer journey"* distorts more than it conveys. A short vignette — what happened at a table, in plain language, and why it mattered — is understandable without any knowledge of the hobby and does not smuggle in a wrong model.

**State the cost of not building it.** A PO can evaluate whether a value claim is proportionate to an omission. "Improves prep" is not critiquable. "Without this, a detail the GM knows exists cannot be found while three people wait, so it never gets said" is.

**Acceptance criteria in observable terms.** Per [[Shippable-Increment]]: the assertion and the demo path. Julia can judge whether a criterion can actually fail, without knowing anything about the domain.

**No epic assumes another epic's content.** If it does, say which and why — overlap and hidden coupling are exactly what an outside reviewer catches best.

---

## Epic structure

1. **Name** — plain language, no jargon.
2. **Who it is for** — the role, and what they are trying to accomplish.
3. **The problem** — with one concrete vignette.
4. **What is not being asked for** — the boundary. Per [[Scope]], this prevents most scope inflation.
5. **Assumptions** — domain assertions this rests on, each linked to its source document.
6. **Value, and the cost of omission.**
7. **Stories.**
8. **Open questions** — what is still undecided, and what it blocks.

Story voice does not change. Stories stay written as value to the user, not as implementation guidance.

---

## What examples may be drawn from

**There is currently almost nothing to spoil.** The only real campaign secret is the Floor 1 plan — its specific rooms and its quest. The NPCs and connections that appear throughout `_design/` are illustrations written to explain a model, not established campaign facts.

| Source | Usable in epics |
|---|---|
| **Player character material** — the dossiers, backgrounds, and choices made during character creation | **Yes.** Creation happened in the open, in person. Everyone at the table already knows it. |
| **Invented examples** | **Yes**, and the default. |
| **The Floor 1 plan** — its rooms, its quest | **No.** |
| **GM plans built on player material** — hooks intended from a background, threads being set up, anything not yet in play | **No.** The dossier is shared; what the GM intends to do with it is not. |

Real character material is genuinely useful for the epics about dossier answers as hooks and about a player reaching for their own character's background — those are hard to illustrate convincingly with invented people.

**Invented examples remain the default anyway**, for two reasons that have nothing to do with secrecy:

- One built to isolate the exact behaviour under discussion is clearer than a real case carrying incidental detail — and it can demonstrate situations the campaign has not reached, which is where several epics live.
- **The constraint has a shelf life.** Secrets accumulate: arcs, off-screen events, canon plans from Floor 6 onward. A convention adopted now costs nothing; retrofitting it later means a scrub, and a scrub that misses one item has already done the damage.

**Characters may be named; players should not be**, in the epics about behavioural inference. [[GM-Player-View-and-Transparency]] settles that players are told the mechanism exists, so it is not secrecy — it is that *"the system noticed this player kept returning to X"* is a requirement about a real person, reads more clearly as a role, and gains nothing from a name. Facts about a character carry no such issue.

---

## One prerequisite this creates

**The glossary is now blocking.** [[Backlog-Readiness]] §G10 treats it as a cheap consistency fix. Under this standard it becomes a prerequisite for writing the epics at all, since every domain term needs somewhere to point.

It also has to be written for a reader who knows nothing — not as a disambiguation aid for people who already know the terms and only need the local distinctions.
