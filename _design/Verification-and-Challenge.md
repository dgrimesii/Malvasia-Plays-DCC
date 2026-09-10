---
type: design
status: draft
visibility: gm
tags: [product, process, testing, verification, bias]
---

# Verification and Independent Challenge

A process requirement, recorded because it shapes the backlog. Companion to [[Shippable-Increment]] and [[First-User]].

---

## Settled

1. **The development process produces real test harnesses and suites** — not incidental checks written alongside features.
2. **There is an independent challenger** to the GM's testing and plans, to mitigate the single-user acceptance problem in [[First-User]].

---

## The honest limit, stated first

The available challengers are **correlated with the builder**, not independent of it.

Claude Code writes the implementation. Another Claude session reviews it. They share training, disposition, and — usually — the same framing of the problem, supplied by the same person. An AI asked to challenge tends toward *performative* challenge: objections that sound rigorous and land on the least important thing, followed by agreement.

That does not make it worthless. It reliably catches **omission, unstated assumption, uncovered case, and requirement drift** — a large share of real defects. It barely touches **shared blind spots**: the case where the requirement itself is wrong in a way that seems obviously right to everyone reading it.

Two consequences:

- **Design the challenge structurally**, not attitudinally. Separation of what each side can see does more than instructing anything to be skeptical.
- **Reserve the one uncorrelated reviewer for what matters.** Julia is a Product Owner and is at the table. She cannot see GM campaign content, but she can review *the tool's requirements and plans*, which is where correlated review is weakest. Use her on the decisions in [[Backlog-Readiness]], not on code.

---

## Structural separation

Three roles, kept apart by what each is allowed to see.

| Role | Sees | Never sees |
|---|---|---|
| **Author** | Requirement, existing code | — |
| **Test author** | Requirement only | The implementation |
| **Challenger** | Requirement and output | The reasoning that produced the output |

**Tests are written from the requirement, before or independently of the implementation.** A test written afterward by whoever wrote the code encodes what the code does, not what was asked for. That is the single highest-value separation available and it costs nothing but sequencing.

**The challenger is given the artifact, not the argument.** Reasoning is persuasive; being shown it is how a reviewer gets anchored.

---

## The challenger's job is questions, not attitude

"Be critical" produces theater. The role is specified as a fixed set of questions, answered against the artifact:

- What would have to be true for this to be wrong?
- What case does this not cover that a real session will produce?
- What does this assert that the requirement does not say?
- What in the requirement is not exercised by any test?
- Where does this depend on the author knowing something that is written nowhere?
- What silently succeeds when it should fail?

**The valuable output is a failing test, not an opinion.** A disagreement expressed in prose evaporates. A disagreement converted into a test case is durable, re-runs forever, and does not require anyone to remember the argument. Challenge that cannot be expressed as a case should be recorded as an open question rather than resolved by discussion.

---

## Bias mitigations specific to a builder-user

### Pre-register the expectation

Before running the demo, write down what the output should be. Compare afterward. This is the direct counter to the confirmation problem in [[First-User]] — a proposal that matches what you expected reads as a good proposal, and pre-registration is what distinguishes *matched* from *plausible in hindsight*.

Most valuable on the inference epics, whose entire claim is surfacing what could not have been noticed. If the pre-registered expectation always matches, the feature is producing nothing.

### Freeze judgment into a corpus

Judgment-bearing output — proposals, tickets, coverage claims, arc candidates — gets judged once, by the GM, and the verdict is kept: this set was good, this set was noise.

That corpus becomes a regression suite. Later changes re-run against it, and drift becomes visible without re-litigating anything. **It converts a one-time human judgment into a durable asset**, which is the only way judgment scales for a single reviewer.

### Adversarial fixtures

Beyond the synthetic campaign required by [[Shippable-Increment]], fixtures should include cases built to break things: contradictory claims, a merged arc with conflicting premises, a revealed lie beneath three layers of inference, an entity referenced after deletion, a session with no interaction facts, a character death mid-arc.

Most of these have not happened at the table yet. Fixtures are the only way to test them before they do — and several are guaranteed to happen eventually.

### Red-team the record

The campaign record is the asset the non-breaking rule protects. Some tests should actively try to damage it: orphan a reference, write malformed frontmatter, half-complete a batch, produce manner where the input had none.

That last one deserves its own suite. [[Constraint-Manner-and-Intent]] is a list of things that must never happen, and violations are silent — nothing looks wrong when a plausible emotional read gets fabricated.

---

## What the challenger must not be given

**Manner, intent, and emotional state stay out of scope entirely.** [[Constraint-Manner-and-Intent]] forbids the AI generating these. It equally cannot verify them — there is no artifact to check a claim about what the room felt like against.

So a challenger may assert that a manner field is empty, or that it matches what the GM wrote verbatim. It may not evaluate whether a recorded manner is *accurate*. That judgment is the GM's and the players', permanently.

The same boundary applies to whether a proposal is a good *reading of the table*. A challenger can find the case the proposal ignores; it cannot judge whether the party is actually invested in the Warden.

---

## Consequence for the backlog

This creates enabling work items that are not features but are prerequisites under [[Shippable-Increment]], where testable and demoable are gates:

- **Test harness** — able to run any increment against a fixture and print output, since demo-by-script is the accepted form.
- **Fixture corpus** — the synthetic campaign, plus the adversarial cases above. Needed before the first increment that writes campaign data.
- **Golden corpus** — captured judged output for the judgment-bearing capabilities. Needed before the first inference increment, not after.
- **Challenger protocol** — the question set, and the rule about what each role may see. Written once.

These should be scheduled as their own items rather than folded into feature stories, because folded work of this kind is the first thing dropped when a feature runs long.
