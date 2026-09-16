---
type: delivery
status: proposed
visibility: gm
tags: [delivery, backup, durability, export, operations]
---

# Backup and Durability

**Status: proposed.** A requirement that exists in the corpus with no mechanism behind it.

---

## How this became ownerless

[[Migration]] gave the campaign repository a second life as an export target, and that one mechanism was quietly carrying four jobs:

| Job | Where it went |
|---|---|
| Inspection surface for demos | Reassigned to the harness, P2, by [[Store-and-Access]] |
| Stable artifact for the Chronicle mapping | Never needed one — [[Strategy-Multi-Campaign-and-Convergence]] makes the mapping "a document, not code" |
| Read, grep and diff without the tool running | A convenience of files-as-store; the application provides it now |
| **Off-host durability** | **Nothing** |

**Superseded reasoning, kept in place:** repo-as-export-target was right while the repo was the store and the tool was a way to organise one campaign. What broke it is that a registered domain and a hosted application make a continuously mirrored repository a second copy of every campaign secret, under different access control, editable, and looking authoritative — which is drift, the failure `COLLABORATION.md` identifies as the largest risk here. It also required a credential pointing out of production into a repository the build context reads.

Removing it was correct. It left the fourth job without an owner.

---

## Why RC 1d does not cover this

[[Roadmap]] places Epic 12 late by design, on the reasoning that "the cheapest option that survives contact with a real error is the right one, and which option that is cannot be known until real errors have happened."

That reasoning is sound **and it is about a different problem.** Epic 12 repairs bad data inside a store that still exists. Nothing in it addresses the store not existing.

The gap opens at Epic 13. The moment conversion completes, production holds the only copy of months of converted work — and the conversion itself is the interpretive pass [[Migration]] describes as the hard part. [[Shippable-Increment]] is explicit that the bar here "is not availability — it is the record."

---

## Proposal

Two mechanisms, because they fail differently.

### 1. Database snapshot

Managed platform snapshots, ~~daily, retained thirty days~~. **On Render this is point-in-time restore within 3 days (Hobby) or 7 (Pro)** — shorter than the thirty days first proposed; the weekly export below carries the longer horizon. Protects against the store being lost or corrupted. Restores fast and requires no application code.

Its weakness is that it is only readable by the same engine, which is exactly what [[Knowledge-Assets]] says the assets must not depend on.

### 2. Scheduled export to object storage

The export required by C9 in [[Hosting]] and by Epic 13 S2, written weekly to the bucket. Readable text, no database, no application.

This is the portability commitment and the durability mechanism satisfying each other — the same shape the repository was serving, without the second editable copy or the credential into a repository.

**Retention:** weekly for a quarter, then monthly. The campaign record only grows, and old exports are cheap.

---

## Recovery expectation — settled

**Accepted by the GM, 2026-09-16.**

| | Expectation |
|---|---|
| **Work lost, normal case** | Nothing — a point-in-time restore on Render returns the store to any moment within its window (3 days on Hobby, 7 on Pro) |
| **Work lost, worst case** — the platform database is gone | **At most one week**, back to the last weekly export. Writes happen about once per session, so this is at most one session's capture and prep |
| **Time unavailable** | **Working again before the next session** — days, not hours. [[Shippable-Increment]]: the bar is the record, not availability |

**One working rule makes the worst case recoverable rather than lost:** the GM keeps the raw notes for a session until the next weekly export has completed. A lost week is then a session re-entered, not a session gone.

Before cutover none of this is at stake — the frozen campaign files are still authoritative and the import can be re-run.

---

## The restore drill

**Run once before cutover, against the test environment** — restoring **test's own** backup into a new database. Never production's: that would put the live record in test and break rule 1 in [[Environments]].

[[Access-Recovery]] already models this pattern for entitlements: "that last one is the actual drill, and it is worth running against a fixture rather than assuming."

What it proves, against the expectation above:

- A snapshot restores into an empty instance and the application runs against it
- An export from the bucket is readable without the tool
- Someone can state how long a restore takes, from having done it — and it is comfortably inside a week
- Everything up to the last export comes back when restoring from the export

An untested backup is a belief. The drill is what makes it a fact, and it costs an hour at a moment when nothing is at stake.

---

## The campaign repository after cutover

**Frozen, not retired.**

[[Migration]] requires that conversion be non-destructive and "repeatable from source… Run it, inspect the output, fix the conversion, run it again from scratch."

That only holds while an untouched source exists. If an interpretive call in the conversion — a fact's visibility, an edge's type — turns out wrong six months later, re-running is possible only against the original. So the repository stops being written to and stops being read by anything except conversion, and is kept.

It is not the backup. It is the source.

---

## Open questions

1. **When is cutover?** [[Store-and-Access]] asks for the moment to be "chosen rather than arrived at," and nothing has chosen it. It is the date production starts holding something irreplaceable, so it is also the deadline for the drill above. **GM decision, 2026-09-16: not fixed now; projected from progress.** Choosing it still happens deliberately — when a projection exists, it is written here and the drill is scheduled before it.
2. ~~**What is the recovery expectation?** No figure exists for how much work may be lost or how long a restore may take. A weekly export and daily snapshots imply answers; they should be stated rather than implied.~~ **Settled** — see §Recovery expectation.
3. **Does the export cover everything?** Epic 13 S2's round-trip proof compares converted output against the source. That proves conversion lost nothing. It does not prove the export covers what accumulates *after* conversion — reveal events, claims, resolutions, the Live Set. Worth an assertion of its own.
