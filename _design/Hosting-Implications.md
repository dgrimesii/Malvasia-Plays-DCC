---
type: design
status: draft
visibility: gm
tags: [strategy, hosting, delivery, epics]
---

# Hosting Implications

What changes in [[Roadmap]] RC 1a if Storyteller is eventually hosted on the web.

---

## The short answer

**Very little.** Hosting is a delivery decision, and Epics 1–3 are written as statements of what the GM needs rather than how it reaches them. Nothing in them becomes wrong.

What hosting does is **convert three deferred questions into requirements** — and all three were already worth doing. It also introduces one genuinely new obligation and one genuine risk.

---

## 1. Offline retrieval stops being optional

The largest change, and it lands on Epic 2.

[[North-Star]] names *the lost detail* as a failure mode: a detail the GM cannot retrieve mid-sentence does not exist. [[Retrieval-Tiering]] sets the bar at seconds and calls ten seconds a failure.

A hosted tool makes that dependent on the venue's connection. **A bad signal at the table becomes the exact failure the product exists to prevent** — and it fails at the worst possible moment, mid-sentence, with three people waiting.

So the open connectivity decision is effectively answered by the hosting decision: **retrieval works with no network.** [[Update-Cadence]] already observed this is nearly free, since a prepared artifact can sit on the device. Hosting turns that from a convenient property into a requirement.

**Effect on Epic 2:** a first-class story rather than a deferred question — *as the GM, I want to find things at the table whether or not the room has a signal*. Its assertion is that retrieval returns correct results with the network unavailable.

---

## 2. Mid-session capture must survive a dropped connection

Lands on Epic 1, story S11.

A fragment jotted during play is by definition unrecoverable if lost — [[Session-Capture]] establishes that anything not recorded at the time is gone. Losing it to a connection drop is the same outcome as never writing it.

**Amendment to S11's assertion:** a fragment saved during play survives with no network available and appears in the session write-up once connectivity returns.

Same reasoning as (1), and the same near-free mitigation.

---

## 3. A minimal access boundary arrives in R1

**New obligation.** [[Strategy-Multi-Campaign-and-Convergence]] states that R1 needs no accounts, no login, no permissions — correct for a tool running locally for one person.

Public hosting changes that on its own. The campaign record contains genuine secrets, and the players are motivated readers who know the tool exists.

This is not the accounts system that was deferred. It is the minimum that keeps the record from being publicly readable — a private deployment, or one credential. **Small, easy to skip, and embarrassing to skip.**

It does not change any epic. It becomes a standing requirement alongside the model invariants in [[Sequencing]].

---

## 4. The risk: hosting is when repo-as-database gets quietly abandoned

The moment a web application exists, putting the store in a database behind it becomes the obvious move. It is also the moment three commitments would be broken at once:

- **Portability** — [[Knowledge-Assets]] requires the assets be readable and exportable without the tool, because the store is the durable value and the tool is not.
- **Demo paths** — [[Shippable-Increment]] leans on reading files and diffing them. Cheap precisely because the repo is the store.
- **Coexistence** — [[First-User]] assumes the GM keeps working partly in markdown for a long stretch. That only works while both paths write the same thing.

**None of this forbids a hosted app.** A server can read and write the repo. What it forbids is the store moving somewhere the GM cannot read directly, and that decision would be made silently, as an implementation convenience, unless it is named in advance.

---

## 5. What does not change

**Epic 3 is essentially unaffected.** Readiness is computed during prep, at home, on a machine with a connection. It has no at-the-table dependency.

**Epic 1's other twelve stories are unaffected.** Capture happens after play, per [[Session-Capture]], from a place with connectivity.

**Concurrency does not arrive yet.** [[Update-Cadence]] removed simultaneous writing by assuming one person batching, and R1 still has one user. Hosting plus **Release 2** is when a second write path genuinely appears — that is the point to revisit it, not now.

**No accounts, sharing, or campaign switching.** The deferral in [[Strategy-Multi-Campaign-and-Convergence]] stands; only the minimum in (3) changes.

---

## One incidental benefit

Hosting makes the independent review in [[Verification-and-Challenge]] easier. Julia currently reviews documents. A URL she can open is a better artifact to critique than a description of one — and [[First-User]] identifies the absence of an outside observer as the main weakness of a builder-user product.

Worth remembering when weighing when to host, not a reason on its own.

---

## Summary of amendments

| Where | Change |
|---|---|
| Epic 1, S11 | Assertion gains: fragment survives with no network and syncs later |
| Epic 2 | Offline retrieval becomes a story rather than an open question |
| [[Sequencing]] invariants | Add: the record is not publicly readable |
| Standing constraint | The store stays directly readable by the GM, hosted or not |

The connectivity question in [[Backlog-Readiness]] is resolved by this decision rather than needing a separate answer.
