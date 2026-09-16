---
type: delivery
status: draft
visibility: gm
tags: [delivery, readiness, checklist, sequencing]
---

# Readiness Checklist

The ordered path from here to handing Claude Code, in VS Code, a GitHub issue it can work without guessing.

**Re-audited 2026-09-16** against the corpus, the four RC 1a epics, and the GitHub repository. The original six corpus corrections are done and struck below; the audit found more. Items marked *proposal* are Claude's suggestions, not decisions.

---

## Where things stand

| Area | State |
|---|---|
| Design corpus for RC 1a | Written. Epics 1, 2, 3, 13 marked ready, with story-level holds listed in Stage 7 |
| Platform | **Settled** — Render and Cloudflare. See [[Hosting]], [[Render-Setup]] |
| Original corpus corrections (1.1–1.6) | **All done** |
| New corpus corrections (1.7–1.15) | Open |
| Decisions needed before issue 1 | Six open; the repository question is new and blocks the rest of the setup |
| GitHub | No issues, no labels, no issue template, **no code repository** |
| Local development machine | Not yet checked for what Claude Code will need |
| Prerequisites P2–P4 | Not started. P2 and P3 are enabling issues; P4 needs ratifying |

---

## Stage 0 — Check first: the campaign repository is public

GitHub reports `Malvasia-Plays-DCC` as a **public** repository. Its own description reads *"Showrunner eyes only"*, and it holds GM material — including the Floor 1 zone file, which [[Epic-Writing-Standard]] rules out of anything a player reads.

Several documents rest on players not being able to read GM material — rule 1 in [[Environments]], the fixture reasoning in [[Test-Strategy]], and the sourcing rules in [[Epic-Writing-Standard]], which name Julia as both reviewer and player. While the repository is public, those protections are moot: anyone with the link can read everything.

**If this is unintended:** GitHub → the repository → Settings → General → Danger Zone → Change visibility → Private. Nothing in this project needs it public. What has already been read cannot be unread; there is no further remedy.

**If it is intended**, it needs recording as a decision, because three documents currently assume otherwise.

---

## Stage 1 — Corpus corrections

**Blocking, and the reason is specific.** `CLAUDE.md` sends the build context to read `_design/` before implementing anything. A document that is wrong there does not produce a wrong opinion — it produces a wrong implementation that looks sourced.

Each is worked in the chat context, with superseded reasoning kept in place per `COLLABORATION.md`.

### Done

| # | Document | What was wrong | Status |
|---|---|---|---|
| 1.1 | [[Sequencing]] | Stated the old GM-versus-player release axis, and carried a drifted allocation table | ~~Open~~ **Done** — axis struck and superseded in place; allocation table retired in favour of [[Roadmap]] |
| 1.2 | [[Shippable-Increment]] | Demo section rested on *"the repo is the database"* | ~~Open~~ **Done** — struck; demo now rests on the P2 harness |
| 1.3 | [[Migration]] | Export-target section superseded | ~~Open~~ **Done** — struck with the reasoning kept |
| 1.4 | [[Store-and-Access]] | *Demo by reading files* row and cutover section assumed a repository destination | ~~Open~~ **Done** — row marked replaced; cutover now names the restore-drill deadline |
| 1.5 | [[Strategy-Multi-Campaign-and-Convergence]] | Subdomain reservations | ~~Open~~ **Done** — `test.` built; `demo.` and `fixture.` reserved, superseded reasoning kept |
| 1.6 | Epic 2 | S2 cited `demo.warpandweft.ink` | ~~Open~~ **Done** — now cites `test.warpandweft.ink`, with the old citation noted |

### Open

| # | Document | What is wrong | Proposed fix |
|---|---|---|---|
| 1.7 | [[Settings-and-Campaigns]] | **Contradicts itself — introduced by Claude on 2026-09-16.** The new "campaign creation offers linking to an existing setting or starting a new one" sits beside "the setting is invisible until a second campaign is created" and "explicitly not now: any interface acknowledging that settings exist" | *Proposal:* the fork belongs to the release that first lets a GM create a campaign in the tool. RC 1a creates its only campaign by conversion (Epic 13), so there is no creation screen and the setting stays invisible. Needs the GM's call |
| 1.8 | Epic 13 S11 | Does not carry the decision that **every entity records which campaign originated it**, added to the RC 1a backlog in [[Settings-and-Campaigns]] | Add it to S11's assertion and demo. Also decide whether it earns the `unrecoverable` label — it has the same shape as the four, but the four are a settled list |
| 1.9 | Epic 1 | Still written against the old release axis: *"no player reads anything until Release 2"* (Dependencies), and S6 calls itself *"one of the three unrecoverable ones"* where there are now four | Players read in RC 1b under [[Release-Plan]]; correct both in place |
| 1.10 | [[Open-Requirements]] | Still marks resolved questions **[blocking]** — §1 player identity, §3 surfacing versus authoring, §7 character death, §9 one campaign or many. [[Backlog-Readiness]] §G11 flagged this; it was never fixed | Strike each with its answer and a link |
| 1.11 | [[Backlog-Readiness]] | Still lists G1 (release boundary), G2 (graph model), G3 (surfacing) and G8 (connectivity) as blocking. All four are answered in [[Roadmap]] §Resolved | Strike with answers, or mark the whole document historical |
| 1.12 | `CLAUDE.md` | Never points Claude Code at `_delivery/` — so [[Issue-Conventions]], [[Test-Strategy]] and [[Environments]] are outside its reading path. The test-first split and the definition of ready are exactly what it must follow. It also has no section on **how to work an issue**: one issue per session, branch and pull request, a `test` issue never reading the implementation branch, findings filed before code | Add a *Working an issue* section and add `_delivery/` to the reading order. Moves with the code if Stage 2 separates repositories |
| 1.13 | [[Backup-and-Durability]] | *"Run once before cutover, against the test environment"* does not say whose backup. Restoring production's snapshot anywhere near test breaks rule 1 in [[Environments]] | Say it: restore **test's** backup into a new database. Render restores into a new instance, which fits |
| 1.14 | Epic 1 S12 | Requires *"the GM can see each proposal as a player would see it"* from the first session, which its own Dependencies section calls a forward dependency on Epic 15 — RC 1b | Either pull a narrow preview slice into RC 1a explicitly, or restate S12. Otherwise S12 cannot be accepted in its own candidate |
| 1.15 | Epic 3 | Dependencies: *"Where [investment] is set is not yet assigned to an epic — worth confirming it is not orphaned between Epic 1 and Epic 4."* S10 cannot be accepted without an input | Assign recording investment to an epic in RC 1a, or move S10 out of RC 1a |

Two smaller ones, fix while there:

- [[Issue-Conventions]] says the walking skeleton deploys to *"all three environments at their real addresses"*. Dev is local and has no address. Its settings should also point at [[Render-Setup]] §Part 6.
- [[Glossary]] has no entry for **Setting Owner**. Not needed by any RC 1a issue; needed before anything cites it.

After: run `check_links`, `check_staleness --days 0` on a full clone, and `check_definitions --min 3`.

---

## Stage 2 — Decisions

Six are needed before issue 1. The rest are recorded so they are not discovered.

### Needed before issue 1

| Decision | Why now | Where it lands |
|---|---|---|
| ~~**Container host**~~ | **Settled: Render.** See [[Hosting]] §Host | [[Hosting]] |
| **Where the application code lives** — and, with it, where the design corpus lives | See below. Blocks connecting GitHub to Render, and decides where Claude Code works | [[Hosting]] §Open questions |
| **Framework** | The walking skeleton cannot be built without a language and web framework. [[Hosting]] leaves this to an ADR proposed by Claude Code and ratified by the GM — so it is a `spike` issue before issue 1, not a chat decision | ADR in the source tree |
| **Who writes the issues** | [[Issue-Conventions]] says what an issue contains but not who creates it. *Proposal:* the chat context drafts them from stories through the GitHub connector; the GM approves and writes each pre-registered expectation | [[Issue-Conventions]] |
| **Cutover date** | [[Store-and-Access]] asks for it to be chosen rather than arrived at. It is the deadline for the restore drill | [[Backup-and-Durability]] |
| **Cost ceiling** | Shape settled: two databases, test suspended when idle. No figure exists anywhere | [[Hosting]] |
| **Recovery expectation** | How much work may be lost, and how long a restore may take | [[Backup-and-Durability]] |

#### The repository question, laid out

Render copies the whole connected repository into each deployment. Connecting `Malvasia-Plays-DCC` puts the campaign folders inside test, which breaks rule 2 in [[Environments]]. But Claude Code needs the design corpus, and must be able to write `_feedback/`, in the repository it works in.

| Option | What happens | Cost |
|---|---|---|
| **A. New product repository holds code and the product corpus** *(proposal)* | `_design/`, `_backlog/`, `_delivery/`, `_feedback/`, `_tools/`, `COLLABORATION.md`, `CLAUDE.md` move to it. `Malvasia-Plays-DCC` keeps the numbered campaign folders and becomes the frozen conversion source | One move, done once. `_design/` is campaign-agnostic by rule, so it belongs with the product rather than with one campaign |
| B. New repository for code only; corpus stays | Claude Code works across two sibling clones in a VS Code multi-root workspace | Every session depends on the second clone being present and current. `_feedback/` would be written into the campaign repository |
| C. Code in `Malvasia-Plays-DCC` | Campaign content moves out first | Moves the thing that is supposed to stay frozen |

**Not a submodule.** Pulling the campaign repository into the code repository as a submodule puts it back inside the deployment.

**One sub-question under A:** `_templates/` is both the GM's authoring format and the import contract conversion code implements (`_templates/CONVENTIONS.md`). The conversion code needs the contract; the GM keeps using the templates until cutover. Decide which repository is authoritative for it.

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

Its second output matters as much: it tells you which cases are genuinely hard, and those are the cases the fixture must contain. **P3 is better written after this pass than before it.**

### 3.2 Challenger protocol — P4

The question set already exists in [[Verification-and-Challenge]]. What is missing is the operating rules, which are written in [[Test-Strategy]] and need ratifying rather than inventing. A `corpus` item, worked in the chat context.

---

## Stage 4 — Repository and GitHub setup

After the repository decision. None of this is code.

- [ ] **The code repository exists and is private.** Under option A, the corpus is moved into it with history, and `CLAUDE.md` paths and `_tools/` search directories are checked afterward.
- [ ] **Labels** from [[Issue-Conventions]]: `rc-1a` to `rc-1d`, `unrecoverable`, `blocked-finding`, `blocked-decision`, `chat-context`. *Proposal:* also one label per issue type — `test`, `impl`, `enabling`, `corpus`, `spike` — so the test-first order can be filtered.
- [ ] **An issue template** carrying the fields in [[Issue-Conventions]] §What an issue contains, so no issue is written without its assertion, demo, exclusions and pre-registered expectation.
- [ ] **Milestones** per release candidate, if wanted. Optional; labels already carry it.
- [ ] **`main` protected**: changes arrive by pull request, and merging waits for CI once CI exists. This is what makes *Auto-deploy after CI checks pass* in [[Render-Setup]] mean something.

CI itself is created by the walking-skeleton issue, not by hand.

---

## Stage 5 — Infrastructure and the development machine

### Hosting

[[Render-Setup]] Parts 1–5 by hand. Part 6 is what the walking-skeleton issue follows.

- **The test environment holds no production credential.** This is rule 1 in [[Environments]] and it is enforced by absence, not by policy. It is much harder to remove a credential later than to never add it.
- **Migrations run as a discrete, reversible step**, not as a side effect of application start.

### The machine Claude Code runs on

Claude Code works from VS Code on Windows. Before issue 1, confirm:

- [ ] **Git** works from the VS Code terminal — the `D:` drive install is a known source of friction
- [ ] **GitHub CLI** installed and signed in, so Claude Code can read an issue and open a pull request from the terminal
- [ ] **A container runtime** able to run Postgres locally at the version pinned in [[Render-Setup]] §Part 6 — check it against the `D:` drive setup before assuming it works
- [ ] **A development model API key** kept only on this machine, for live extraction runs. CI does not need one; it replays recorded responses per [[Test-Strategy]]
- [ ] **The runtime the framework ADR chooses** — installed after that spike, not before

---

## Stage 6 — The first issues

| # | Type | What |
|---|---|---|
| **0** | `spike` | **Framework ADR.** Claude Code proposes language, web framework, migration tool and test runner against the constraints in [[Hosting]]; the GM ratifies. Output is the ADR, no merged code |
| **1** | `enabling` | **Walking skeleton** — the application deployed to test and production at their real addresses, and running locally, on the target store, serving nothing. Creates CI and the Render services per [[Render-Setup]] §Part 6. Full text in [[Issue-Conventions]] |
| **2** | `enabling` | **P2 — test harness.** Runs any increment against a fixture, prints output, and renders store contents as readable text. The same mechanism as the export required by Epic 13 S2 |
| **3** | `enabling` | **P3 — fixture corpus.** Synthetic, mirroring the real campaign's structure and none of its content. Contents specified in [[Test-Strategy]]; best written after 3.1 |

Only after all of these does the first story issue open — a `test` issue against Epic 1, worked in its own session before any implementation exists. Working order after that is in [[Issue-Conventions]] §Ordering: Epic 1 first, Epic 13 at cutover.

---

## Stage 7 — Story readiness in RC 1a

Checked against each epic's own open-questions and dependencies sections, not by re-auditing every story's text. A story is held when its assertion cannot be made to fail yet — [[Issue-Conventions]] §Definition of ready, items 2 and 7.

| Epic | Stories held, and by what |
|---|---|
| **1 — Capture a session** | **S12** — needs a stated line for what counts as invention; and 1.14. **S11** — Release 2, excluded from RC 1a by [[Roadmap]]. **S15** — can start on the four proposed attribute kinds; the set is revisable by design |
| **2 — Find anything, fast** | **S2** — needs a target number beneath the ten-second failure bar, and issue 1 deployed. **S5, S6** — need an acceptable failure rate for plain-language questions. **S12** — needs P3's mixed known-and-unknown entities, and Epic 13 S3. The table tier is Release 2 and excluded |
| **3 — Know the next session is covered** | **S1** — readiness as one answer or a list is undecided. **S2** — what makes a direction *live*, and whether the open surface is capped. **S7** — how far ahead coverage should reach. **S10** — 1.15 |
| **13 — Move the campaign in** | **S6** — the granularity at which prose becomes facts. **S11** — 1.8. **S13** — which origin-date source to use; affects coverage, not correctness. The epic's size depends on 3.1, and it runs against the live record only at cutover |

**Everything else in these four epics is ready once P2 and P3 exist** — which is most of Epic 1, and enough of Epics 2 and 3 to start.

---

## What is deliberately not in this plan

**Schema.** The store's shape is low-level design and belongs in the source tree with an ADR beside it. `CLAUDE.md` draws that line and adding schema specifics to the corpus "breaks the portability the whole model is built for."

**Application framework in the corpus.** It is issue 0's ADR, in the source tree. [[Hosting]] fixes the platform and leaves the framework there.

~~**Application framework.** Same reason, one level up. [[Hosting]] fixes the platform and leaves the framework to an ADR.~~ *Superseded 2026-09-16: still not a corpus decision, but it is no longer true that nothing here needs it — the walking skeleton does, so it became issue 0.*

**Anything from RC 1b onward.** The candidates after 1a have open decisions as entry criteria, and elaborating them now would mean guessing at those answers.

**A rollback plan for the application.** Deliberate. Production has no users to regress and no availability commitment — [[Shippable-Increment]] is explicit that "the bar is not availability — it is the record." Redeploying the previous version is sufficient; the record is protected by [[Backup-and-Durability]], which is a different mechanism for a different failure.

---

## The shortest honest summary

One check that cannot wait — the repository's visibility. Nine corpus corrections, one of them a contradiction Claude introduced. Six decisions before issue 1, the repository question first. One hand pass over the legacy files. Repository and GitHub setup, Render Parts 1–5, and a check of the development machine. Then a framework spike and three enabling issues, after which Epic 1's test issues can open.

~~Nothing on that list needs a framework chosen to begin, and the first two stages need no infrastructure at all.~~ *Stages 0 through 4 need no framework and no infrastructure; issue 1 needs both.*
