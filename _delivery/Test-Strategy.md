---
type: delivery
status: draft
visibility: gm
tags: [delivery, testing, fixtures, verification, ci]
---

# Test Strategy

How the prerequisites in [[Roadmap]] become things that exist. Implements [[Verification-and-Challenge]] and the testable gate in [[Shippable-Increment]].

---

## The one thing most likely to be lost

[[Verification-and-Challenge]] calls the separation between test authorship and implementation "the single highest-value separation available and it costs nothing but sequencing," on the grounds that a test written afterward by whoever wrote the code "encodes what the code does, not what was asked for."

With a single agent doing both, that separation survives only if it is mechanical. Instruction will not hold it — the same model, given the same requirement, in the same session, is not an independent author.

**So it is enforced by issue structure**, per [[Issue-Conventions]]:

- Every story produces a **test issue** and an **implementation issue**.
- The test issue is opened first, cites the story's assertion and demo verbatim, and is worked in its own session.
- The test issue may not read the implementation branch. Where the implementation does not yet exist, this is free; where it does, the branch is named and excluded.
- The implementation issue may read the tests. That direction is fine — it is implementing to them.

Tests that fail on first run against no implementation are the expected outcome, not a problem to fix before merging.

---

## P2 — Test harness

**Gate:** the first increment.

Runs any increment against a fixture and prints the output. Two jobs, and the second is newer than the Roadmap entry suggests.

**Run and assert.** Standard.

**Inspect.** [[Store-and-Access]] flags this explicitly: demo-by-reading-files was cheap because the store was files, and once the store moves, "an increment that writes to a database with no way to look at what it wrote cannot be accepted. Some inspection path — a dump, a rendered view, an export — is now part of the harness (P2) rather than a property of the storage."

So the harness must render store contents as readable text on demand. This overlaps the export path required by C9 in [[Hosting]] and Epic 13 S2, and they should be the same mechanism rather than two.

**Acceptance for P2 itself:** run it against an empty fixture and get readable output. It clears [[Shippable-Increment]] on its own — functional, non-breaking, testable, demoable, not useful.

---

## P3 — Fixture corpus

**Gate:** the first increment that writes campaign data.

### Synthetic, not derived from the real campaign

Considered and rejected: using the dossiers and the Floor 1 plan as the fixture, since they are already written and already legacy-shaped.

Four reasons against, and the second is decisive:

- [[Shippable-Increment]] rules it out directly — the real record is what the non-breaking rule protects, and it changes weekly, so assertions break for reasons unrelated to the code.
- **The test environment is the reviewer's URL.** [[Epic-Writing-Standard]] rules the Floor 1 plan out of anything Julia reads. A fixture drawn from real content makes the review artifact a spoiler.
- The two artifacts do not share a status. Player dossiers are usable in written material because "creation happened in the open, in person"; the Floor 1 plan and any GM intent built on a dossier are not.
- The real campaign cannot supply what the fixture is for — see the adversarial cases below, most of which have not happened at the table.

**What it does take from the real material is shape.** Same artifact types, same defect classes, same rough scale, none of the content. The hand conversion pass in [[Readiness-Checklist]] is what tells you which cases are hard, and the fixture should contain those.

### What it must contain

The happy path, plus every case named in the corpus as needed:

**Legacy-shaped content**, per [[Migration]] item 4 — prose under Description, Motivations and Secrets headings; untyped, undirected `[[links]]`; file-level visibility. Plus the four known model errors from [[Backlog-Readiness]] §G10: quest and arc conflated, encounter blocks embedded inside zone documents, drifted hand-maintained inverse links, and the stale `visibility` vocabulary.

**The P3 additions from [[Roadmap]]** — entities at a range of investment degrees *including some with none recorded*, and entities carrying a mix of known and unknown facts. Without these, Epic 2's marking story and Epic 3 S10 cannot be exercised.

**The adversarial cases from [[Verification-and-Challenge]]** — contradictory claims, a merged arc with conflicting premises, a revealed lie beneath three layers of inference, an entity referenced after deletion, a session with no interaction facts, a character death mid-arc.

**Cases for the model invariants in [[Sequencing]]** — an entity with several simultaneous names at different visibilities, a claim left `undetermined`, a sparse record with almost every field empty, an utterance whose claim is false.

Each defect is placed deliberately, one per case, **with the correct conversion recorded alongside it.** That is what a fixture drawn from real files could never provide: an independent statement of the right answer.

---

## P4 — Challenger protocol

**Gate:** the first review.

The question set is already written in [[Verification-and-Challenge]] and does not need restating. What P4 adds is the operating rules:

- The challenger receives **the artifact and the requirement, never the reasoning**. Reasoning is persuasive and anchors a reviewer.
- Its valuable output is a **failing test case**, not an opinion. A disagreement that cannot be expressed as a case is filed as an open question instead.
- **Manner, intent, and emotional state are out of scope entirely.** A challenger may assert that a manner field is empty or matches the GM's input verbatim; it may not judge whether a recorded manner is accurate.
- Julia reviews requirements and plans, not code. She is the one uncorrelated reviewer and correlated review is weakest exactly where she is strongest.

---

## P5 — Golden corpus

**Gate:** RC 1c, the first inference increment. Not needed for RC 1a.

Carries a design constraint rather than only a task: it only works if detection is deterministic, because a changed result must be attributable to the code change rather than to sampling variance. That is what forces detection to be procedural while extraction may use a language model — C7 in [[Hosting]].

---

## Testing something that is not deterministic

Extraction uses a language model. Detection may not. That gives three tiers, and the middle one needs a decision.

| Tier | What | Runs |
|---|---|---|
| **Deterministic** | Store, query, visibility filtering, detection, export, conversion | Every push. Gates the merge |
| **Model-dependent** | Extraction from recap text | Replayed from recorded responses in CI; live runs are a separate manual job |
| **Judgment-bearing** | Whether a proposal is a *good* reading | Demo only. The GM is the instrument |

**Recorded-response replay is the proposal**, and it has a consequence worth stating rather than discovering: **a prompt change that degrades extraction will not fail CI.** Replay proves the pipeline handles a known response, not that the model still produces a good one.

That is tolerable only because [[Shippable-Increment]] already makes the demo the acceptance mechanism for judgment-bearing output — "no test catches that. The demo is where it gets caught, and the GM is the instrument." It means **the demo is not optional for any extraction work**, and a live-model run should precede any acceptance involving a changed prompt.

It also keeps CI free of API cost and of flakiness that has nothing to do with the change under test.

---

## Assertions of absence

[[Shippable-Increment]] names these as the constraints most likely to erode silently, "because nothing visibly goes wrong when they are violated." They belong in the acceptance criteria for anything that writes.

- Manner is empty where the input had none, and verbatim where it did
- No entity, fact, or edge appears in extraction output that is not present in the source text
- `undetermined` is rendered as a displayed state, never as a blank, and nothing counts or flags it
- Nothing is written without an accepted proposal behind it
- Nothing crosses from `gm` to `player` visibility without a reveal event

[[Verification-and-Challenge]] asks for a suite that actively tries to damage the record — orphan a reference, write malformed frontmatter, half-complete a batch, produce manner where the input had none. That last one deserves its own suite.

---

## Pre-registration

Before running a demo, write down what the output should be, then compare.

This is the direct counter to the confirmation problem in [[First-User]]: a proposal matching what the builder expected reads as a good proposal, and pre-registration is what distinguishes *matched* from *plausible in hindsight*. Most valuable on the inference epics — "if the pre-registered expectation always matches, the feature is producing nothing."

Cheap, and it belongs in the issue rather than in someone's memory. See [[Issue-Conventions]].
