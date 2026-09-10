---
type: design
status: draft
visibility: gm
tags: [strategy, storage, access, hosting]
---

# Store and Access

Revisits *"the repo is the database"* from [[Interface-User-Stories]]. Follows [[Hosting-Implications]].

---

## Two things were being conflated

My earlier caution treated these as one. They are not, and they have different answers.

| | What it means | Verdict |
|---|---|---|
| **Repo as access interface** | Browsing markdown files as the way to read and write the campaign | **Limiting. Move off it.** |
| **Repo as store** | Files as the canonical home of the content | **Also limiting — the model has outgrown it** |

---

## Access: the limits are decisive

Reading markdown files cannot do what [[Roadmap]] RC 1a asks for:

- **Retrieval in seconds, mid-sentence.** [[Retrieval-Tiering]] calls ten seconds a failure. File browsing is not in that range.
- **The player view.** [[Visibility-Model]] requires filtering at three levels — existence, facts, relationships — with every computation running over the filtered store. A file is visible or it is not.
- **Non-technical users.** Two of the three players in Release 2 will not read a repository, and should not have to.

This was never in dispute. It is the clear case for a real interface.

---

## Storage: the model outgrew the format

The stronger point, and the design work of the last several sessions is what demonstrated it.

Markdown files were a good fit for the model as it stood in the original documents: entities as documents, links between them, a visibility flag per file. The model has since become something else:

| Requirement | Why files strain |
|---|---|
| Visibility per **fact** and per **edge** — [[Visibility-Model]] | Facts and edges must be individually addressable records. A markdown table row is not one. |
| Every player-facing computation runs over the **filtered** store | Requires querying, not scanning documents and post-filtering the output — which is precisely the leak described in [[Visibility-Model]]. |
| Edges **re-point** on merge — [[Identity-and-Reconciliation]] | Referential integrity across hundreds of hand-maintained links. |
| Aliases preserved through reconciliation | Identity that survives renaming, across every file that referenced it. |
| Reveal recorded as an **event** — [[Release-Plan]] | An append-only log, not a field. |
| Coverage and readiness — Epic 3 | Traversal over the whole graph, per prep session. |

**The corrected templates are already straining against this.** They ask markdown tables to hold what are really records with attributes. That works while a human fills them in and reads them back. It does not work as something to query.

So: the templates are a **bridge**, not a destination. They were the right thing to build for the interim, and they are not the shape of the store.

---

## What was actually load-bearing in the portability argument

Not the file format. The property.

[[Knowledge-Assets]] argues that the knowledge store is the durable value and the tools are activity layers on top of it — so the assets cannot be trapped inside any one interface. **That requires export and readability without the tool. It does not require that the canonical store be files.**

Files delivered that property for free, which made it easy to conflate the two. A database plus a reliable export delivers the same property deliberately.

**The commitment to keep, restated:** the campaign record can be read, exported, and understood without Storyteller running. How that is achieved is a design question.

---

## Two things that were free and now need paying for

### The inspection surface

[[Shippable-Increment]] makes *demoable* a condition of shipping, and leaned on reading files and diffing them — cheap precisely because the store was files. If the store moves, that cheapness goes with it.

**This does not block anything, but it needs replacing.** An increment that writes to a database with no way to look at what it wrote cannot be accepted. Some inspection path — a dump, a rendered view, an export — is now part of the harness (P2) rather than a property of the storage.

### The cutover

[[Shippable-Increment]] assumes the GM keeps working partly in markdown for a long stretch, and that dual-running is free because both paths write the same thing. Once the store moves, they diverge.

So there is a **cutover moment**, and it should be chosen rather than arrived at. Before it, the templates are authoritative. After it, the tool is, and the templates become an import format.

---

## The templates gain a second job

They are now the **import format** for everything captured before cutover — which, given the session cadence, will be several sessions' worth.

That is a good outcome. It means the template correction was not interim busywork: it is what makes those sessions importable without re-encoding. Every structural rule in `_templates/CONVENTIONS.md` exists so the import is mechanical rather than interpretive.

**Effect on Epic 13:** it grows. Previously the dossiers and the Floor 1 plan. Now also template-shaped session records, which are the more structured input and the higher-volume one.

---

## What to revisit elsewhere

| Claim | Status |
|---|---|
| *"The repo is the database"* — [[Interface-User-Stories]] | **Superseded.** True for the interim; not the destination. |
| Portability — [[Knowledge-Assets]] | **Stands**, as a property rather than a format. |
| Demo by reading files — [[Shippable-Increment]] | **Needs replacing** with an inspection path in the harness. |
| Dual-running is free — [[Shippable-Increment]], [[First-User]] | **Bounded** by the cutover. |
| Chronicle mapping — [[Shared-Core]] | **Unaffected**, and arguably easier. Chronicle is already a structured store rather than files. |

---

## What does not change

- **Epics 1–3 are unaffected.** They state what the GM needs, not where it is kept.
- **The model invariants in [[Sequencing]] are unaffected** — they are properties of the model, and several of them are the reason files no longer fit.
- **No accounts or sharing in R1**, beyond the minimum access boundary in [[Hosting-Implications]].
- **The templates stay in use** until cutover, and stay correct after it as the import contract.
