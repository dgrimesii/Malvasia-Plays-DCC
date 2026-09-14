---
type: design
status: draft
visibility: gm
tags: [strategy, migration, storage, backlog]
---

# Migration

Planning assumption: repo-stored content will be converted into a real database as part of the move to the web. Follows [[Store-and-Access]].

---

## First: convert once, not twice

The assumption creates a choice that is worth making deliberately, because the default answer is the expensive one.

| Path | Conversions |
|---|---|
| **(a)** Build RC 1a writing to files, migrate to a database later | **Two** — hand-authored content into files-shape, then files into the database |
| **(b)** Build RC 1a on the target store from the start | **One** — hand-authored content into the database |

**(b) is clearly better, and it is available.** There is no legacy application to migrate away from — only hand-authored content. The interim capture mechanism is templates plus a human, and [[Store-and-Access]] establishes those remain in use until cutover regardless of what the tool writes to. So nothing forces RC 1a to write files.

**The recommendation: do not build RC 1a on files.** What is called "migration" is then simply the initial import, done once, at the start of the tool's life.

---

## The repo becomes a frozen source

Not discarded, and not a projection either.

After cutover the repo is **read by conversion and written by nothing.** Conversion must be repeatable from source — run it, inspect the output, fix it, run it again from scratch — and that only holds while an untouched original exists. If an interpretive call turns out wrong six months later, the original is the only thing that makes a re-run possible.

So it is kept, frozen. It is not the backup; it is the source. Durability is a separate mechanism — see [[Backup-and-Durability]].

~~**The repo becomes an export target.** Writing generated markdown back to the repo satisfies [[Knowledge-Assets]] directly, and preserves three things worth keeping: the GM can read, grep, and diff the campaign without the tool running; the demo and inspection surface that [[Shippable-Increment]] depends on; a stable artifact for the Chronicle mapping in [[Shared-Core]]. The repo stops being the store and becomes a projection of it.~~

**Superseded, and worth understanding why, because the failure was structural rather than factual.** One mechanism was carrying four jobs, and three of them found better owners: inspection went to the harness under [[Store-and-Access]], the Chronicle mapping never needed a generated artifact since [[Strategy-Multi-Campaign-and-Convergence]] makes it a document rather than code, and read-grep-diff was a convenience of files-as-store that the application now provides.

What broke the fourth is that a registered domain and a hosted application turn a continuously mirrored repo into a second copy of every campaign secret — under different access control, editable, and looking authoritative. That is drift, which `COLLABORATION.md` names as the largest risk here. It also required a credential pointing out of production into a repo the build context reads.

**The commitment it was standing in for survives unchanged.** [[Knowledge-Assets]] still requires the assets be readable and exportable without Storyteller, and Epic 13 S2's round-trip proof still needs an export path. Only the destination moved. See [[Backup-and-Durability]].

---

## What is actually hard

Not identifiers or frontmatter. Those are mechanical. The cost is in four interpretive conversions:

### 1. Prose into addressable facts

Existing entity files hold free prose under headings — Description, Motivations, Secrets. The model needs facts as records with a source, a truth status, and a visibility.

Splitting a paragraph into facts is judgment. It is also the conversion that most affects everything downstream, since a fact that stays trapped in prose is not queryable and therefore effectively absent.

### 2. Links into typed, directed edges

`[[Some-NPC]]` carries no type, no direction, and no visibility. Every existing link needs all three assigned.

**This is the largest interpretive gap in the whole conversion**, and there is no way to infer it from the link itself.

### 3. File-level visibility into per-fact visibility

A file marked `visibility: gm` says nothing about which of its facts the party knows. Every fact needs its own answer.

**The default direction matters more than anything else in this document.** Defaulting to `player` on ambiguity spoils the campaign silently. Defaulting to `gm` is always safe and merely inconvenient — the GM reveals later, at a moment of their choosing, which is what [[Visibility-Model]] wants anyway.

### 4. Known model errors in live content

[[Backlog-Readiness]] §G10 records these already: quest and arc conflated in existing files, encounter blocks embedded inside zone documents, hand-maintained inverse links that have drifted. Conversion is when each has to be resolved rather than carried forward.

---

## Safety requirements

The campaign record is live and irreplaceable, so this is where the non-breaking rule in [[Shippable-Increment]] is under the most pressure.

**Non-destructive.** The source is never modified. Conversion reads and writes elsewhere.

**Repeatable from source.** Run it, inspect the output, fix the conversion, run it again from scratch. Not incremental, not stateful — otherwise a bad run has to be unpicked rather than discarded.

**Ambiguity queues rather than guesses.** Where a fact's visibility or an edge's type cannot be determined, it is raised for a decision — the Accept / Defer / Edit shape from Chronicle, per [[Shared-Core]]. A guess that is wrong in the `player` direction is a spoiler; a guess that is wrong about an edge type is a false connection in a store whose whole value is connections.

**Nothing becomes known to the party unless the source says so.**

**Round-trip proof.** Export the converted store back to markdown and compare it against the source. **This makes "nothing was lost" a test rather than a hope**, and it is the strongest single assertion available for this work.

**Conversion runs in production only.** It reads the frozen repo and writes the live store, so it is invoked deliberately rather than deployed everywhere — see [[Environments]]. Exercising it against legacy-shaped fixture content is how it gets tested before it touches the real record.

---

## What to do now

Four things, all available before any code exists.

1. **Keep the templates strict.** They are the import contract. Every rule in `_templates/CONVENTIONS.md` exists so that template-shaped content converts mechanically rather than interpretively.

2. **Convert legacy files to template shape by hand, early.** The dossiers and the Floor 1 plan pre-date the corrected templates. Doing this before the tool exists moves the interpretive work — prose into facts, links into typed edges — out of the migration and into a calm moment. It shrinks the hardest part of the conversion to almost nothing.

3. **Do not build RC 1a on files.**

4. **Put legacy-shaped content in the fixture corpus (P3)**, so conversion is testable long before it is needed, and so the awkward cases are exercised deliberately rather than discovered on the live record. The fixture is synthetic — it mirrors the legacy files' shape and defects, never their content. [[Test-Strategy]] says why.

---

## Roadmap changes

**Epic 13 is rescoped and renamed.**

> **Epic 13 — Move the campaign into the tool without losing anything**
>
> *As the GM, I want everything I have already written to arrive intact and correctly marked, so that using the tool does not mean abandoning three months of work or re-reading all of it to check.*

Its inputs are now the dossiers, the Floor 1 plan, template-shaped session records, and any remaining legacy files. Its central assertion is the round-trip proof.

**It moves from RC 1b to RC 1a.** Retrieval — Epic 2 — is only useful over content that exists. Without conversion, RC 1a is a demonstration rather than a tool, and the first slice is meant to be the one that earns its place at the table.

**Revised RC 1a:** Epics 1, 2, 3, 13.

---

## What does not change

- Epics 1, 2, and 3 are unaffected. They state what the GM needs, not where it is kept.
- The model invariants in [[Sequencing]] are unaffected — several of them are the reason files no longer fit.
- The templates stay in use until cutover, and stay correct afterward as the import contract.
- The cutover moment still has to be chosen rather than arrived at.
