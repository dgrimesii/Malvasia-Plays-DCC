---
type: delivery
status: proposed
visibility: gm
tags: [delivery, hosting, platform, store, infrastructure]
---

# Hosting

What the platform has to satisfy, and what to run on.

**Status: proposed.** The constraints below are derived from the corpus and are not negotiable. The platform recommendation is a proposal and the GM decides it.

---

## Platform versus framework

| | Decided | Where it lives |
|---|---|---|
| **Platform** — host, database engine, object storage, DNS | Here, by the GM | This document |
| **Framework** — language, web framework, ORM, test runner, build tooling | By Claude Code, ratified by the GM | An ADR in the source tree |

The split is not arbitrary. A database engine and a host are commitments that outlive any rewrite of the application on top of them, and the store is the durable asset per [[Knowledge-Assets]]. A web framework is replaceable in an afternoon by comparison.

---

## Constraints

Each derived from the corpus, with its source. These bound the platform choice.

| # | Constraint | Source |
|---|---|---|
| C1 | **Web-first, always online.** No offline mode, no local-first sync | [[Roadmap]] — *"Does retrieval work with no connectivity? No."* |
| C2 | **Campaigns addressed by path**, never subdomain | [[Strategy-Multi-Campaign-and-Convergence]] |
| C3 | **A real database from RC 1a** — a graph domain model on a relational store | [[Roadmap]] §Resolved |
| C4 | **Containment to arbitrary depth** — places nest without a fixed ceiling | [[Glossary]] — Place; [[Strategy-Multi-Campaign-and-Convergence]] |
| C5 | **Filtering happens in the query, not after it.** Every player-facing computation runs over the filtered store | [[Visibility-Model]], via [[Store-and-Access]] |
| C6 | **Campaign scope is structural**, not remembered — an unscoped query should be hard to express | [[Multi-Campaign-Hosting]] |
| C7 | **Detection is deterministic.** No language model in the detection path | `CLAUDE.md`; [[Glossary]] — Golden corpus |
| C8 | **Outbound model calls for extraction**, with per-environment secrets | [[Session-Capture]]; [[Inference-and-Candidate-Relationships]] |
| C9 | **Export to readable text is a first-class output**, not a reporting afterthought | [[Knowledge-Assets]]; Epic 13 S2 |
| C10 | **Retrieval latency is a property of the store.** R2's bar cannot be met by a fast view over a slow one | [[Release-Plan]] §3 |
| C11 | **Account-level access.** One account per person, a password hash, a login. ~~A private deployment or one credential~~ | [[Two-Observer-Model]]; raised from [[Hosting-Implications]] §3 |
| C12 | **An off-host durable copy exists** | [[Backup-and-Durability]] |
| C13 | **Three environments, affordable and operable by one person** | [[First-User]]; [[Environments]] |
| C14 | **The core is the platform's, not one tool's.** Entity, Fact, Relationship, Event, Session are shared; each tool's context attaches by reference | [[Two-Observer-Model]]; [[Shared-Core]] |
| C15 | **Identifiers are opaque, non-sequential, type-free, unique within a setting**, and allocated by the store | [[Information-Architecture]]; [[Identity-and-Reconciliation]]; [[Visibility-Model]] |
| C16 | **The four unrecoverable requirements are enforced at the write boundary**, by the store rather than by an application, for every writer | [[Release-Plan]] §4 |
| C17 | **No unfiltered read path is exposed to any tool.** C5 extended across a tool boundary | [[Visibility-Model]]; [[Two-Observer-Model]] |
| C18 | **System-specific payload is opaque to the core** — stored, never interpreted | [[Shared-Core]] |
| C19 | **Secrets and outbound model calls are platform services**, serving more than one surface. Extends C8 | [[Two-Observer-Model]] |

**What is deliberately absent:** signup, invitations, an administration interface, sharing, billing, campaign switching. ~~Accounts~~ are now in scope at the minimum described in C11 — one account per person and nothing more. [[Multi-Campaign-Hosting]] is explicit that stage 4 arriving early "is how a working tool becomes an unfinished service."

---

## Recommendation

**Managed PostgreSQL, a container host alongside it, Cloudflare retained for DNS and object storage.**

### Why Postgres specifically

C3 asks for a relational store carrying a graph model, and the choice within that is not a formality — several constraints land directly on engine capability.

- **C4 and the graph traversal in Epic 3's coverage walk** want recursive common table expressions that perform at depth.
- **C10** makes the search implementation a store decision. Native full-text search with ranking, in the same engine as the data, avoids standing up a second system whose consistency then has to be managed.
- **C5** wants filtering pushed into the query. Row-level security is available if the three-gate structure ever warrants it, without redesigning around it.
- The typed comparable attributes required by Epic 1 S15 sit alongside prose and will change shape as the model settles. A JSON column avoids a migration per attribute type while the shape is still moving.
- **C9 and C12** get a path independent of the application: a database dump is an export the tool does not have to be running to produce.
- Migration tooling is mature, which matters more here than usual — the store is the asset, and its history of changes is part of what protects it.

**Chronicle reached the same engine independently.** Its v5 milestone specified PostgreSQL with JSONB in April 2026, on its own reasoning about data volume. Two decisions converging is worth noting here because the store is the commitment that outlives everything built on it — see [[Two-Observer-Model]].

### Why not Cloudflare Workers and D1, despite DNS already being there

Genuinely tempting: the registrar and DNS are already Cloudflare, the free tier covers this scale, and deployment is simple.

Against it: D1 is SQLite with size and query ceilings that would be discovered rather than chosen, the Workers runtime constrains library selection in ways that will collide with C8, and migration tooling is younger. The application could be re-platformed cheaply. **The store cannot**, and it is the store this decision is really about.

Cloudflare keeps DNS and gains object storage for backups under C12, which is the part of it that fits well.

### What is open

The container host is not a strong opinion. Any platform offering a managed Postgres instance, a deployable service, environment-scoped secrets, and a CI trigger satisfies the constraints. Pick on price and on how little operational attention it demands.

---

## Setup work

Ordered. Everything here precedes the first issue except where noted.

### DNS and TLS
- `test.warpandweft.ink` → test service
- `storyteller.warpandweft.ink` → production service
- `chronicle.warpandweft.ink` reserved — products take subdomains, campaigns take paths, per C2
- Confirm `warpandweft.ink` apex behaviour; a landing page is not needed yet but the record should not dangle
- `demo.` and `fixture.` stay reserved and unpointed
- Certificates for both live names

### Data
- Local Postgres for dev, containerised so the version matches the managed one — worth checking against the known `D:` drive path quirks on the dev machine before assuming it is frictionless
- Managed Postgres instance for test
- Managed Postgres instance for production
- Object storage bucket for backups, per [[Backup-and-Durability]]

### Secrets
- Per-environment store for the model API key under C8, sized for more than one consuming surface under C19
- No production credential exists in the test environment — this is rule 1 in [[Environments]] and it is enforced here, by absence

### Pipeline
- CI on push: unit tests, the three corpus checks in `_tools/`
- Deploy to test on merge
- Promote to production as a deliberate action, never automatic
- Migrations run as a discrete, reversible step, not as a side effect of application start

### Access
- The C11 boundary on production only. Test is deliberately open so a reviewer can be handed a URL

---

## Open questions

1. **Where does the conversion job run?** It is production-only per [[Environments]], reads the frozen campaign repository, and is invoked deliberately rather than on a schedule. Whether that is a one-off task, a protected endpoint, or a local run against the production database is undecided and affects how the credential is held.
2. **Does the apex get a landing page in R1?** [[Strategy-Multi-Campaign-and-Convergence]] describes one. Nothing requires it, and it is the sort of thing that absorbs a weekend.
3. **What is the cost ceiling?** Three environments with two managed database instances is small but not free, and no figure has been stated anywhere. Two managed instances is the prod/test split required by rule 1 in [[Environments]], not one per campaign — campaigns share a store under C6.
4. **When does Chronicle's second write path arrive** relative to the cutover in [[Store-and-Access]]? A second writer is a cutover-class event and the date is unchosen.
