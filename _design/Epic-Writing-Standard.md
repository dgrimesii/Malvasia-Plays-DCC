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

## Two prerequisites this creates

### The glossary is now blocking

[[Backlog-Readiness]] §G10 treats the glossary as a cheap consistency fix. Under this standard it becomes a prerequisite for writing the epics at all, since every domain term needs somewhere to point.

It also has to be written for a reader who knows nothing — not as a disambiguation aid for people who already know the terms and only need the local distinctions.

### Spoiler safety — the non-obvious one

**Julia is a player in this campaign.** The design documents are `visibility: gm` and their examples are drawn from live campaign material: an NPC's deception, a suspected connection between two figures, a creature the party may care about later.

If epics inherit those examples, handing her the backlog spoils the game she is playing.

So:

- **Examples in epics are neutral or invented**, never drawn from live campaign content. Adopt this from the first epic rather than scrubbing later — a scrub that misses one item has already done the damage.
- **Use role labels, not player names.** The investment and capture epics describe behavioural inference about specific people at the table. [[GM-Player-View-and-Transparency]] settles that players are told the mechanism exists, so the capability itself is not a secret. Describing it to one player using another player's name is a different thing, and unnecessary.
- **Campaign structure is safe; campaign content is not.** That floors exist, that sessions are recorded, that threads are tracked — all fine. What is actually in them is not.

This constraint applies to any artifact Julia reviews, not only to epics.
