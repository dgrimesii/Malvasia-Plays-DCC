---
type: finding
id: F-NNN
status: open
class: contradiction | gap | refinement
raised_by: claude-code
raised_in: <epic and story, e.g. Epic 1 S6>
date: YYYY-MM-DD
---

# F-NNN — <one line, states the problem not the proposal>

## What was being built

<Epic and story. A sentence on what the implementation was doing when this surfaced.>

## What the corpus says

> <Quoted, not paraphrased.>

— `_design/<Document>.md`, §<Section>

<If two documents conflict, quote both. That is the finding.>

## What the implementation revealed

<The concrete thing. Not the proposed fix — the observation that prompted it.>

## Class

**contradiction | gap | refinement**

<One line on why it is that class. If contradiction: what cannot be satisfied. If gap: what the corpus does not say. If refinement: what works today and what would work better.>

## What was done in the meantime

<For a **gap**: the provisional choice made in order to proceed, and where it lives in the code. Recorded before the code was written.>

<For a **contradiction**: *stopped — nothing built against this.*>

<For a **refinement**: *nothing — built as specified.*>

## Proposal

<Stated as a proposal. What change to `_design/` would resolve it, and what else that change would touch.>

<If there is a cheaper option that does not change the model, say so — a finding that only offers the expensive fix is not giving the decision fairly.>

## Consequences if accepted

<Which documents change. Whether anything already built would need revisiting. Whether it touches one of the four unrecoverable requirements — if so, say so loudly.>

---

## Decision

<!-- Filled in by the GM, in the chat context. Leave blank when filing. -->

**Outcome:**
**Decided by:**
**Date:**
**Reasoning:**

<!--
On accept:    link the commit that updated _design/.
On reject:    the reasoning is the point. It is what stops this being re-raised.
On defer:     say what it is waiting on.
On supersede: link what resolved it.
-->
