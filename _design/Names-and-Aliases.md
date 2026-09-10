---
type: design
status: draft
visibility: gm
tags: [model, names, aliases, visibility, revelation]
---

# Names and Aliases

Extends [[Visibility-Model]]. Covers titles, false names, and where a real name lives when the party knows someone by something else.

---

## Names are facts

Established in [[Visibility-Model]]: an entity can materialize without its name being known, so a name is a fact about the entity rather than part of its existence.

That single move handles every naming case, because facts already carry two independent properties this needs — **visibility** and, per [[Facts-and-Revelation]], a **truth status**.

---

## Three situations, one mechanism

| Situation | What the party has | What the GM holds |
|---|---|---|
| **Unknown** | No name. They refer to him by what he does. | His name, gated |
| **Title or role** | *The Toll Warden* — true, publicly known | His personal name, gated. **Both names are true.** |
| **False name** | *Marek* — what he told them | His real name, gated. **One of these is false.** |

The second and third look similar and behave differently. A title is a true name at a different level of formality. A false name is a claim that is not true, and the difference matters as soon as it is revealed.

---

## The trap: a false name is an utterance, not a name field

The sharpest risk in the whole naming model.

If *Marek* is stored as the entity's name, the player surface renders it as a world fact — and the record now asserts a lie in its own voice. That is exactly the failure [[Scope]] warns against: everything in the player view carries its source, *"the Warden told you"*, never *"it is true."*

So the three-part structure from [[Facts-and-Revelation]] applies to names as it does to anything else:

| | Example | Visible to players? |
|---|---|---|
| **Utterance** | He told the party his name is Marek | Yes — it happened |
| **Claim** | His name is Marek | Its truth status is GM-only |
| **The real name** | A separate name fact | Gated until revealed |

**A name the party was given is recorded as something they were told.** The record stays honest whether or not the GM has yet decided it was a lie — which matters, because [[Facts-and-Revelation]] establishes that the GM may decide retroactively that something was a deception.

---

## There is no separate secrets structure

A "secrets section" is a reasonable way to *think* about it and a reasonable way to *author* it. It should not become the mechanism.

[[Identity-and-Reconciliation]] already establishes that an entity carries **many names, each attributed**. Adding visibility and truth status to each — which facts have anyway — covers all of it:

```
Entity
  name: "the Toll Warden"   visible   true    (how he is known)
  name: "Marek"             visible   false   (what he told the party)
  name: [real name]         gated     true
```

One list. No second structure, no special-casing, and the gated name is simply the subset the filter removes.

**Why this matters rather than being pedantic:** visibility that depends on *where something is written* means revealing it requires moving it, and moving it loses its context and its history. Visibility as a property of the fact means revealing is a status change — which is what [[Release-Plan]] already requires R1 to record as an event.

The markdown convention already in `README.md` — a GM-only block inside an otherwise player-visible file — is fine as an **authoring affordance**. It is a place to write, not the thing that determines who sees what.

---

## A gated name must be absent, not redacted

Direct application of the leakage rule in [[Visibility-Model]]: absence has a shape.

An entity page showing *"Known as: Marek"* alongside a field reading *"Real name: —"* has just told the party that Marek is not his real name. The redaction is the reveal.

**A gated name does not appear in any form on the player surface** — no placeholder, no empty field, no count of names. The player view shows the names they know, and nothing indicates whether there are others.

---

## Revealing a real name should generate

[[Facts-and-Revelation]] asks that a status flip surface the affected neighbourhood as material rather than as cleanup. A revealed real name is one of the strongest cases:

- What did the party do believing the false name?
- Who else used it, and did they know?
- What did they conclude that rested on it?
- Where else does the real name already appear in the record, unnoticed?

That last one is a graph query the GM cannot run from memory, and it is the kind of connection [[GM-Considerations]] identifies as the tool's actual value — not recall, but noticing.

---

## Consequences

- **A name is a fact**, carrying attribution, visibility, and truth status like any other.
- **A name the party was given is stored as an utterance**, never as the entity's name. This is an R1 capture requirement, alongside the utterance/claim separation already in [[Release-Plan]].
- **One name list per entity**, with the gated names simply filtered out. No separate secrets structure in the model.
- **A secrets section is an authoring convenience**, not the visibility mechanism.
- **Gated names are absent, not redacted**, on the player surface.
- **Revealing a real name triggers the generative neighbourhood query**, not a correction pass.
