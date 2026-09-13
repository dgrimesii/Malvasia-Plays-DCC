---
type: delivery
status: draft
visibility: gm
tags: [delivery, readiness, checklist, sequencing]
---

# Readiness Checklist

The ordered path from here to telling Claude Code to work the first issue.

Five stages. Stages 1 and 2 have no code in them at all.

---

## Stage 1 — Corpus corrections

**Blocking, and the reason is specific.** `CLAUDE.md` sends the build context to read `_design/` before implementing anything. A document that is wrong there does not produce a wrong opinion — it produces a wrong implementation that looks sourced.

Each is worked in the chat context, with superseded reasoning kept in place per `COLLABORATION.md`.

| # | Document | What is wrong |
|---|---|---|
| 1.1 | [[Sequencing]] | States *"R1 is the GM interface, R2 is the player interface"*. [[Release-Plan]] replaced that axis with between-sessions versus at-the-table. Its slice table also puts Epic 13 in 1b — [[Migration]] moved it to 1a — and Epics 9, 10, 15, 16 in R2, which [[Release-Plan]] moved to R1 |
| 1.2 | [[Shippable-Increment]] | The demo section rests on *"the repo is the database."* [[Store-and-Access]] already marks this **needs replacing** and the replacement was never written. Demo path is an acceptance criterion on every story |
| 1.3 | [[Migration]] | The export-target section is superseded. See [[Backup-and-Durability]] for what broke it |
| 1.4 | [[Store-and-Access]] | The *Demo by reading files* row and the cutover section both assume a repository destination |
| 1.5 | [[Strategy-Multi-Campaign-and-Convergence]] | Subdomain reservations: `demo.` and `fixture.` stay reserved and unbuilt. See [[Environments]] |
| 1.6 | Epic 2 | S2 cites `demo.warpandweft.ink` as its acceptance home. That subdomain will not exist |

**1.1 needs care.** [[Sequencing]] holds the only copy of the model invariants table, which is still correct and is inherited by every story. Correct the release axis and the slice table in place; do not retire the document.

After: run `check_links`, `check_staleness`, and `check_definitions --min 3`. Note that staleness needs a full clone — a shallow one gives every document the same timestamp and the check reports nothing.

---

## Stage 2 — Decisions

Four are needed before the first issue. The rest are recorded so they are not discovered.

### Needed now

| Decision | Why now | Where it lands |
|---|---|---|
| **Container host** | The last open piece of the platform | [[Hosting]] |
| **Cutover date** | [[Store-and-Access]] asks for it to be chosen rather than arrived at. It is the deadline for the restore drill | [[Backup-and-Durability]] |
| **Cost ceiling** | Three environments with two managed database instances. No figure exists anywhere | [[Hosting]] |
| **Recovery expectation** | How much work may be lost, and how long a restore may take | [[Backup-and-Durability]] |

### Known, not blocking

Carried from [[Roadmap]] §Open decisions and unchanged by this work:

- Attention budget as a number — Epics 3 and 6 both need one
- Tombstones on deletion — decide during RC 1b, lands in 1d
- Does anything reach players automatically — now an R1 question
- Does Epic 2 become two epics — decide before 1b
- Campaign length; how much canon before Floor 6

---

## Stage 3 — No-code prerequisites

Both can be done before any infrastructure exists, and the first one gets more expensive every week.

### 3.1 Hand-convert legacy files to template shape

[[Migration]] item 2, and its reasoning is the point: doing this before the tool exists moves the interpretive work — prose into addressable facts, untyped links into typed directed edges — "out of the migration and into a calm moment. It shrinks the hardest part of the conversion to almost nothing."

Typed edges are the reason this is worth a deliberate pass. [[Migration]] calls assigning type and direction "the largest interpretive gap in the whole conversion," and there is no way to infer either from a link. Done by hand now, it is judgment exercised once. Done during conversion, it is judgment exercised against a queue.

Its second output matters as much: it tells you which cases are genuinely hard, and those are the cases the fixture must contain.

### 3.2 Challenger protocol — P4

The question set already exists in [[Verification-and-Challenge]]. What is missing is the operating rules, which are written in [[Test-Strategy]] and need ratifying rather than inventing.

---

## Stage 4 — Infrastructure

The setup list in [[Hosting]] §Setup work, in order: DNS and TLS, databases, secrets, pipeline, access boundary.

Two items are easy to defer and both are load-bearing:

- **The test environment holds no production credential.** This is rule 1 in [[Environments]] and it is enforced by absence, not by policy. It is much harder to remove a credential later than to never add it.
- **Migrations run as a discrete, reversible step**, not as a side effect of application start. The store is the durable asset; its change history is part of what protects it.

---

## Stage 5 — The first three issues

| # | Type | What |
|---|---|---|
| **1** | `enabling` | **Walking skeleton** — the application deployed to all three environments at their real addresses, on the target store, serving nothing. Full text in [[Issue-Conventions]] |
| **2** | `enabling` | **P2 — test harness.** Runs any increment against a fixture, prints output, and renders store contents as readable text. That inspection path is the same mechanism as the export required by Epic 13 S2 |
| **3** | `enabling` | **P3 — fixture corpus.** Synthetic, mirroring the real campaign's structure and none of its content. Contents specified in [[Test-Strategy]] |

Only after all three does the first story issue open — a `test` issue against Epic 1, worked in its own session before any implementation exists.

---

## What is deliberately not in this plan

**Schema.** The store's shape is low-level design and belongs in the source tree with an ADR beside it. `CLAUDE.md` draws that line and adding schema specifics to the corpus "breaks the portability the whole model is built for."

**Application framework.** Same reason, one level up. [[Hosting]] fixes the platform and leaves the framework to an ADR.

**Anything from RC 1b onward.** The candidates after 1a have open decisions as entry criteria, and elaborating them now would mean guessing at those answers.

**A rollback plan for the application.** Deliberate. Production has no users to regress and no availability commitment — [[Shippable-Increment]] is explicit that "the bar is not availability — it is the record." Redeploying the previous version is sufficient; the record is protected by [[Backup-and-Durability]], which is a different mechanism for a different failure.

---

## The shortest honest summary

Six corpus corrections, four decisions, one hand pass over the legacy files, the infrastructure in [[Hosting]], and three enabling issues.

Nothing on that list needs a framework chosen to begin, and the first two stages need no infrastructure at all.
