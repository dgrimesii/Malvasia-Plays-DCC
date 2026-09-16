---
type: delivery
status: draft
visibility: gm
tags: [delivery, environments, hosting, access, testing]
---

# Environments

Three environments. Settled by the GM.

---

## Settled

| | Where | Data | Infrastructure |
|---|---|---|---|
| **Dev / unit test** | Local | Fixture campaign | Local |
| **Test** | `test.warpandweft.ink` | Fixture campaign | Production-class |
| **Production** | `storyteller.warpandweft.ink/malvasia` | The live campaign | Production |

No distinction between system test and acceptance test. Additional subdomains cost nothing and can be created whenever a reason appears — see **When to add a fourth**, below.

Campaign addressing is by path, never by subdomain, per [[Strategy-Multi-Campaign-and-Convergence]]. That holds in every environment, so the fixture campaign has a path too rather than sitting at a root.

---

## Two rules, both structural

These are not conventions to remember. Each is enforced by something being absent.

### 1. The live campaign exists in production and nowhere else

Test runs the fixture. Dev runs the fixture. Neither ever holds a copy of the real record.

[[Shippable-Increment]] gives two reasons and both are load-bearing: testing against the real record risks the one thing the non-breaking rule protects, and the real record changes weekly, so assertions break for reasons unrelated to the code.

**Enforced by:** the test environment holds no credential that can reach the production store. Not a policy — a missing secret.

### 2. The conversion job is not deployable to test

Epic 13's conversion reads the frozen campaign repository. If it can run in test, rule 1 survives only until someone runs it there to see what happens.

**Enforced by:** conversion is a production-only deployment target~~, and the campaign source is not fetchable from the test environment~~.

**Narrowed 2026-09-16.** The repository is public by the GM's decision, so the campaign source is fetchable from anywhere, test included; the struck clause cannot be enforced. What remains structural: the conversion job is never deployed to test, and the Root Directory in [[Render-Setup]] §Part 6 keeps the campaign folders out of every deployment's files. Rule 1 does not depend on the struck clause — test still holds no production credential and no copy of the record.

---

## Why test serves the fixture rather than a copy of production

The obvious shortcut — mirror production into test so the data is realistic — ~~breaks three things at once~~ breaks two things, and once broke a third.

~~**It spoils the campaign.** [[Verification-and-Challenge]] identifies Julia as the one uncorrelated reviewer available, and [[Hosting-Implications]] notes that a URL she can open is a better artifact than documents describing one. She is also a player at the table. [[Epic-Writing-Standard]] rules out the Floor 1 plan and anything the GM intends to do with a dossier. A test environment holding real content cannot be handed to the only reviewer who is worth having.~~

**Superseded 2026-09-16 by the GM.** Julia as Product Owner and Julia as a player are treated as separate personas, Floor 1 holds no real secrets, and the repository is public. The spoiler argument no longer carries the weight it did. **The conclusion survives on the other two reasons** — and the fixture is how the two personas stay apart in practice, since review of future work is done against it rather than against real content.

**It makes assertions unstable.** Sessions are played weekly. An acceptance criterion measured against content that changed on Sunday is not a criterion.

**It forces deferred work forward.** Serving real content to a reviewer who may see only part of it means building per-campaign entitlement in RC 1a — precisely what [[First-User]] and [[Strategy-Multi-Campaign-and-Convergence]] defer.

**Consequence for the fixture:** it has to be good enough to *review against*, not just good enough to assert on. See [[Test-Strategy]].

---

## Test is production-class, not a smaller tier

Two R1 acceptance criteria are measured over the network and cannot be met on a cheaper instance:

- **Epic 2 S2** measures retrieval latency and states it cannot be accepted against a local run.
- **Epic 13 S11** requires a deployed environment for its addressing assertion.

[[Release-Plan]] adds the reason this matters beyond those two stories: R2's seconds-level bar "cannot be met by a fast view over a slow store," and the query paths and indexing decisions made in R1 set the ceiling. A latency number produced on undersized infrastructure is not the number the story accepts against, and the gap will not be noticed until R2.

**Same engine, same version, same shape. Smaller data is fine; a smaller class is not.**

---

## Test is not always running

**Settled by the GM:** the test environment may be stopped when it is not needed, to save cost. See [[Hosting]] §Two database instances for why this was chosen over one shared instance.

That is safe because of rule 1: test holds only the fixture, and the fixture is reproducible, so nothing on the test instance is irreplaceable. What it changes:

- **Promotion requires test to be running.** Nothing reaches production without having been verified on test, so starting test is the first step of every promotion, not an optional one. A stopped test environment is never a reason to deploy directly.
- **Deploy-on-merge meets a stopped target.** Merges while test is stopped must either wait or deploy when it next starts — never skip test and never fail silently. Which of the two is a pipeline decision for the build context.
- **A reviewer's URL only works while test is up.** Handing Julia a link is one of test's jobs, so a review is a window the environment is started for, and said so when the link is sent.
- **Latency is measured warm.** Epic 2 S2's retrieval figure taken right after a restart measures the restart. Measure after the environment has settled.
- **The restore drill in [[Backup-and-Durability]] needs test started** — a deliberate start, not a surprise.

---

## Promotion

```
local  →  test  →  production
```

Every change reaches production through test. Nothing is deployed directly, including a fix for something broken in production — the environment exists to be the rehearsal, and the one time it gets skipped is the one time it was needed.

Production additionally carries the access boundary from [[Hosting-Implications]] §3: the record is not publicly readable. Test does not, deliberately, because handing a reviewer a URL is one of its jobs.

---

## Superseded: demo as a separate environment

[[Strategy-Multi-Campaign-and-Convergence]] reserves `demo.` as "a permanent home for the synthetic campaign… the cleanest way to give a reviewer something to open rather than documents to read," and separately reserves `fixture.`, `dev.`, and `test.`

**What changed:** the reviewer requirement is real and is unchanged. The *second deployment* was not — `demo.` and `test.` were always going to serve the same fixture campaign, so there was never any data separation between them to preserve. The name suggested an audience that does not exist; there are no prospects to demo to.

Both `demo.` and `fixture.` stay reserved and unbuilt. Nothing else claims them. **Reconfirmed by the GM:** demo is not needed initially.

**Effect elsewhere:** Epic 2 S2 cites `demo.warpandweft.ink` as the home for the fixture. That citation now names a subdomain that will not exist, and needs correcting to `test.warpandweft.ink` — a wrong citation is the failure mode `COLLABORATION.md` singles out, because it looks sourced.

---

## When to add a fourth

Not user growth. Players read the record in R1 per [[Release-Plan]], but they read production, so no number of users creates pressure here.

Two things would:

- **Churn against stability.** Test wants redeploying on every merge; a reviewer wants an artifact that holds still. At this scale the answer is to stop merging for an hour. If that ever becomes impossible, the environment has earned its split.
- **A second campaign.** [[Multi-Campaign-Hosting]] recommends hard isolation — a separate store per campaign — because leakage becomes structurally difficult rather than a matter of discipline. That is stage 1, and nothing before it should be built as though it is coming.
