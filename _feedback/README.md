# Feedback from build to plan

The controlled channel for findings that arise while building, so that deviating from the plan is **an explicit, documented decision** rather than a silent divergence.

Written by the build context. Decided by the GM. The resulting plan change is written in the chat context.

---

## Why this exists

`_design/` is upstream of the code, and [`../CLAUDE.md`](../CLAUDE.md) says to stop and surface a problem rather than adjust the model to fit the implementation.

That names the intent and not the mechanism. Without one, a finding either **blocks the build** — which is wrong for most findings — or **evaporates when the session ends**, which is how silent drift happens.

So: findings are written down here, the build continues or stops according to their class, and nothing changes in `_design/` until someone decides it should.

---

## Three classes, three behaviours

The class determines whether the build stops. Getting this wrong in either direction is costly: stopping for everything makes the channel unusable, stopping for nothing means building on a contradiction.

### Contradiction — **blocking**

The corpus says two incompatible things, or says something the implementation demonstrably cannot satisfy.

**Stop. Do not choose one reading and proceed.** Choosing is the silent drift this whole mechanism exists to prevent, and a contradiction resolved by an implementer is invisible afterward.

### Gap — **non-blocking, but recorded before the code is written**

The corpus does not say, and a choice has to be made to proceed.

Silence is common and the build cannot halt every time it occurs. **So proceed — but record the provisional choice first**, so it can be ratified or overturned on its merits rather than discovered later as a fait accompli.

**The record goes in before the code, not after.** A finding written afterward is a rationalisation of a decision already embedded.

### Refinement — **never blocking**

The corpus is workable and the implementation suggests something better.

These are the most likely to be right and the least urgent. Batch them; raise them when there are a few. A refinement that stops a build has cost more than it is worth.

---

## Filing a finding

Copy [`TEMPLATE.md`](TEMPLATE.md) to `F-NNN-short-name.md`, next number in sequence.

Required, and the template enforces it:

- **What was being built** — epic and story
- **What the corpus says**, quoted, with the document and section
- **What the implementation revealed**
- **The class** — contradiction, gap, or refinement
- **What was done in the meantime** — for a gap, the provisional choice; for a contradiction, *stopped*
- **The proposal** — stated as a proposal, never as a conclusion

**Cite precisely.** Per [`../COLLABORATION.md`](../COLLABORATION.md), a finding that misquotes the corpus is worse than no finding — it looks sourced, so nobody re-checks it. Open the document and quote it.

---

## Closing one

Findings are closed in the **chat context**, by the GM, not by whoever filed them.

Four outcomes:

| Outcome | What happens |
|---|---|
| **Accepted** | `_design/` is updated, with the superseded reasoning kept in place and a note of what broke it. The finding is struck with a pointer to the commit |
| **Rejected** | The finding is struck with the reason. **The reason matters more than the verdict** — it is what stops the same thing being re-raised next month |
| **Deferred** | Struck with what it is waiting on |
| **Superseded** | Something else resolved it. Struck with a pointer |

**Closed findings stay in the directory.** They are struck, not deleted — the same rule as open questions in `_design/`. A rejected finding with its reasoning intact is worth more than a clean directory, because the next person to hit the same wall reads it instead of re-filing.

**A finding records who proposed and who decided.** Per `COLLABORATION.md`, a proposal the GM reacted to positively is not a decision, and the record has to keep those apart.

---

## What this is not

**Not a backlog.** Findings are raised against something being built now. A general idea for later belongs in `_design/` as an open question.

**Not a way for the build context to change the model.** Filing a finding is raising a question, not making an edit. `_design/` is still written in the chat context.

**Not optional for gaps.** The temptation is to fill a small silence and move on. That choice — small, sensible, unrecorded — is exactly the drift the channel exists to catch.
