---
type: design
status: draft
visibility: gm
tags: [information-architecture, model, claims, truth, capture, canon, arcs]
---

# Claims and Resolution

Two new model objects. The reason a proposition uttered at the table is not the same thing as a fact about the world, and why leaving its truth undecided is a feature rather than a gap.

Follows from [[Facts-and-Revelation]] and [[Session-Capture]]. Depends on the mode structure in [[Modes-and-Surfaces]].

---

## The two objects

| Object | Definition |
|---|---|
| **Claim** | A proposition carried by an utterance. Has a speaker, a subject, and a resolution state. Its truth is a separate question from whether it was said. |
| **Resolution** | A dated GM decision about a claim's truth. A distinct object, **not a field on the claim.** |

Two objects rather than one field, for the same reason Arc is distinct from Arc Intent in [[Arcs]]: the intent to decide and the decision are different things with different lifetimes.

A resolution records **when the fiction committed.** Same shape as reveal-as-event in [[Facts-and-Revelation]] and supersession in [[Canon]] — the store records not just what is so, but when it became so.

---

## Recap as fact means fact about the table

The rule for the parser, stated precisely because a naive implementation will get it wrong in a way that is invisible until it does damage.

Every sentence in a recap is one of three things:

| Kind | Example | Produces |
|---|---|---|
| **Event happened** | *The party entered the tunnels.* | one world fact |
| **Utterance happened** | *The Warden said the tunnels flood at night.* | **two records** — the utterance as world fact, plus a claim with resolution undetermined |
| **GM narration of world state** | *The tunnels flood at night.* | one world fact, asserted by the GM as narrator |

The middle row is where a naive parser silently collapses into the third. **If capture flattens utterances into world facts, every deception in the campaign is spoiled the first time a player reads the record** — and a partial job is worse than none, because the damage is invisible until it surfaces.

### The extraction rule

**Speaker attribution is a first-class extraction target, not a nice-to-have.**

- Proposition has a source → attaches to the **utterance**; the claim's resolution is undetermined.
- Proposition has no source → **GM narration**; ordinary world fact.

Simple, and it degrades in the safe direction: a mis-parsed utterance becomes an over-cautious claim rather than a spoiled lie.

The recap is written in prose and will not mark which is which. The parser infers it from the presence of a speaker, and will get it wrong on indirect speech and on loosely written narration. **The review queue must therefore surface the inference for correction** — the kind of each proposition is editable, not just its content.

---

## Three resolution states

**true / false / undetermined.** Not two-plus-null.

**Undetermined is the default, and a legitimate terminal condition.** A claim can stay open for the whole campaign.

It must render as a **real, displayed state**, never as an absence — otherwise the GM cannot distinguish *I decided this is false* from *I have not looked at this.*

### Undetermined is not a data-quality defect

This is the load-bearing distinction and it decides how the tool behaves.

A *hidden-variable* reading says the truth exists and the record has not caught up. Under that reading, undetermined is a defect and the tool should prompt the GM to close it.

The correct reading is **indeterminate, not merely unknown**: there is no fact yet, because the fiction has not committed. The GM may not know the truth value when the words leave their mouth. They may have expected true and find three sessions later that false makes a better story.

Under this reading, an open claim is **optionality the GM can spend later, with information they did not have at the time.** It is a resource, not a defect, and the tool's job is to **protect** it.

**Consequence: the tool never nags the GM to resolve claims at capture.** A nag trains the GM to mark things arbitrarily to clear the queue, and arbitrary marks are worse than honest unknowns. Worse, the nag would consume the raw material that inference runs on.

### Marking is optional, visible, and inline

The GM **may** mark a resolution at capture; it is not required. During capture review the current state is visible and editable inline — an edit like any other, not a separate stage.

Some claims are known with certainty at the moment of capture. Those get marked. Most will not be.

---

## Collapse has exactly two causes

A claim's resolution changes from undetermined only by:

1. **Play at the table** — the party verifies or disproves it.
2. **GM statement** — during Session Planning (Record Plans) or Session Recap.

Nothing else collapses anything. The store can therefore always answer *what resolved this claim, and when.*

Most resolutions will occur in **Record Plans**, because deciding what the story does next is the act that spends an open claim.

### Resolution provenance matters as much as its value

| Provenance | Behaviour on later change |
|---|---|
| **GM decision** | The GM may overrule their own earlier decision freely. |
| **Table outcome** | Overruling it is the supersession path per [[Canon]] — the original stays immutable, a new fact carries `supersedes`. |

Same value, different object, different rules. This is the existing supersession mechanism reached from a new direction.

---

## No probability field

**Decided: there is no numeric or ordinal likelihood anywhere on a claim. No lean.**

The reasoning matters because the process genuinely is probabilistic in feel, and the temptation to model it as a number is strong.

What transfers from the uncertainty analogy:

- The state is **genuinely indeterminate**, not merely unknown. (Load-bearing — see above.)
- **Collapse is caused by an identifiable act**, and the acts are enumerable. (Load-bearing — see above.)

What does **not** transfer:

- Uncertainty relations are quantitative because the amplitudes are. Here there is **no distribution to normalise** — nothing constrains *leaning true* against anything else.
- A field is an **attractor.** Once it exists, filling it feels like progress, and the GM commits on paper to something they would have been better off leaving open.

**The system does not tell the GM what should happen. It tells them what rational options are available.**

### What replaces it: optionality versus coherence

The real trade-off is not probability-of-true. An open claim stays **free** while all its possible resolutions still fit the record. It stops being free when surrounding facts have accumulated enough that one resolution would contradict something already established at the table.

That is **computable** — a consistency check over the claim's neighbourhood, not a belief estimate — and it is the honest thing to surface:

> Open five sessions. Resolving false now conflicts with two accepted facts.

Uncertainty narrows because **the record grew around the claim**, not because confidence drifted.

### Avoiding measurement is a legitimate strategy

A GM can deliberately keep a claim open by not planning near it. The tool must not fight this. **The inference queue surfaces open claims as *available*, never as overdue.**

---

## What inference does with claims

**Inference must read claims as claims.** Three separate NPCs telling the party the same false thing is a genuinely interesting inference about coordination — and it is invisible if claims were flattened into world facts.

High-value surfacing pattern: an **unresolved claim adjacent to a planned encounter, or attached to an entity at Notable investment or higher.**

> You left this open. It is now adjacent to what you are planning. Do you want to spend it?

This is a higher-value inference than most relationship discovery, and it is only possible because the open state was preserved rather than forced closed.

---

## Players never see any of this

Players see the **utterance, attributed** — per [[Scope]], *the Warden told you the tunnels flood at night*, never *the tunnels flood at night.* They do not see resolution states.

So the whole three-state machinery lives entirely on the GM side. It can be as expressive as it needs to be without touching the Release 2 filter in [[Visibility-Model]].

---

## Open

1. **Do resolutions carry visibility separately from the claim?** A claim the GM has marked false, where the falsity has not been revealed, is a spoiler risk on any player surface. The visibility model holds visibility per fact — confirm a resolution is a fact in its own right for this purpose.
2. **May inference use resolved-false claims?** Strong signal, spoiler risk. Related to (1).
3. **Does a claim need a subject beyond free text** for the coherence check to work, or is neighbourhood adjacency via the utterance's participants sufficient?
