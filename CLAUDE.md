# Claude Code — build context

**Read [`COLLABORATION.md`](COLLABORATION.md) first.** It holds the rules that apply in every context. This file holds what is specific to building.

---

## Your role here

**Low-level design, build, test, deploy.**

The work moves through: *ideate → plan → document → design → build → test → deploy.* Everything up to and including **high-level design and architecture** happens in the chat context and lands in `_design/`. **Design is the break point.** You own everything from low-level design onward.

So: how a thing is structured in the store, what the objects are, which requirements are unrecoverable — decided already, in `_design/`. Schema details, module boundaries, function signatures, test structure, deployment — yours.

---

## The design corpus is upstream and authoritative

**Do not edit `_design/` or `_backlog/` unless explicitly asked to.** They are inputs.

Implementation will reveal problems with the design. It always does. When it happens:

> **Stop and surface it. Do not adjust the model to fit the code.**

Do not implement something that contradicts the corpus on the grounds that the corpus is wrong. It may well be wrong — changing it is a deliberate decision, made in the chat context, with the superseded reasoning recorded. It is not a side effect of a build session.

This is the sharpest drift risk across the boundary, and it is silent when it happens. A schema that quietly means something slightly different from the document that specified it will not announce itself.

**If you find yourself reinterpreting a definition to make an implementation work, that is the signal to stop.**

---

## Before implementing an epic

Read, in order:

1. The epic in `_backlog/`
2. [`_design/Glossary.md`](_design/Glossary.md) — every domain term the epic uses is defined there
3. [`_design/Information-Architecture.md`](_design/Information-Architecture.md) — the object model
4. Whatever the epic's **Assumptions** table cites

The assumptions table exists so the reasoning does not have to be reconstructed. Take those as given; they are not the right thing to relitigate mid-build.

---

## Four requirements are unrecoverable

If these are omitted, the capability is not delayed — it is **permanently impossible**, because the information is never captured. They will look like optional polish under delivery pressure. They are not.

| Requirement | Why it cannot be added later |
|---|---|
| **Speaker attribution** — an utterance and the claim it carries are separate records | A flattened statement puts a lie in the record's own voice. Recovering it means re-reading every session |
| **Two clocks** — record time and fiction time on everything | The strongest inference signal reads date-of-entry exclusively. Stamping conversion with today's date flattens the campaign's history, silently |
| **Comparable attributes** — a small typed form alongside the prose | Prose similarity is not machine-comparable. Retro-fitting means re-reading every character |
| **Per-fact visibility**, held per campaign | A file-level or single-valued flag cannot be split later without guessing, on the one axis where guessing spoils a campaign |

See [`_design/Roadmap.md`](_design/Roadmap.md) for the full statement.

---

## Standing constraints on what gets built

These are product constraints, not preferences, and they are easy to violate with a reasonable-looking implementation.

**No generation in extraction.** Stage 1 of intake extracts what the notes say and nothing more. Proposing fiction is a separate, later stage under [`_design/Generative-Projection.md`](_design/Generative-Projection.md).

**No manner, intent, or emotional state generated, ever.** [`_design/Constraint-Manner-and-Intent.md`](_design/Constraint-Manner-and-Intent.md).

**Detection must be deterministic.** A language model may extract and may generate; it may not decide what gets surfaced. An LLM in the detection path makes the golden corpus unreplayable, which removes the only regression test the judgment-bearing features will ever have.

**Nothing is written unreviewed.** Every proposal is accepted by the GM before it lands.

**Undetermined is a real displayed state, never a blank** — and nothing counts, flags, or nags about it. An unset field looks like a to-do; this one is not.

**Nothing arrives unasked at the table.** [`_design/Constraint-Serves-The-Table.md`](_design/Constraint-Serves-The-Table.md).

---

## Where your own design lives

Low-level design belongs **in the code and next to it** — schema definitions, module docs, ADRs in the source tree, docstrings, tests.

**Not in `_design/`.** That directory is system- and campaign-agnostic narrative design, deliberately free of implementation detail. Adding schema specifics to it breaks the portability the whole model is built for.

If a low-level decision turns out to have model consequences, that is exactly the case for stopping and surfacing it.

---

## Testing

Per [`_design/Verification-and-Challenge.md`](_design/Verification-and-Challenge.md) and the prerequisites in [`_design/Roadmap.md`](_design/Roadmap.md):

- **Tests run against fixtures, never the live campaign record.** It is irreplaceable and changes weekly.
- **The fixture corpus needs the awkward cases**, not just the happy path — legacy-shaped content, entities at a range of investment degrees including none recorded, and entities carrying a mix of known and unknown facts.
- Each story in an epic states its own **assertion** and **demo**. Those are the acceptance criteria; implement to them rather than to the story title.
