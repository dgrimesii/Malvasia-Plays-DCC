---
type: design
status: draft
visibility: gm
tags: [strategy, chronicle, convergence, model, platform, store]
---

# The Two-Observer Model

What happens when one campaign is recorded by both tools at once, and what the platform must hold from the first migration for that to remain possible.

Companion to [[Shared-Core]], which establishes *what could be shared* in principle. This document covers the case where both tools are running against the same table play, which is a different question and produces requirements [[Shared-Core]] does not.

---

## The situation this addresses

[[Strategy-Multi-Campaign-and-Convergence]] treats Chronicle as a separate product that shares a model. That framing assumed separate deployments.

It no longer holds. Chronicle's own v5 milestone specified PostgreSQL with JSONB, a server-side model proxy with the key out of the browser, session-based authentication at under ten users, and multi-campaign support — arrived at independently, five months before [[Hosting]] reached the same platform. The private server that plan assumed is not going to exist, so Chronicle lands on the same platform as Storyteller.

**Two independent decision processes converging on one platform is the same quality of signal [[Shared-Core]] identifies for the model.** It is worth building for rather than treating as coincidence.

---

## Two observers of one table session

Not two systems describing different things. **Two imperfect records of the same evening, from different seats.**

| | Storyteller | Chronicle |
|---|---|---|
| Seat | Behind the screen | At the table, as the party experienced it |
| Records | Narrative, GM observation, intent, what was planned and what was revealed | Action and mechanics, what the party did and what they were told |
| Author | The GM | The scribe, on behalf of the party |
| Writes | Facts, and things that have not happened | Facts only, after the fact — per [[Shared-Core]] |

**Neither is required.** A campaign with one observer works. A campaign with both produces a richer record than either alone, and the reason is not additive detail — see §Divergence below.

---

## Session is the shared anchor

Both observers attach to the same real-world timebox. [[Information-Architecture]] already defines Session as a real-world container for the events the players experienced rather than a fictional occurrence, and Chronicle keeps the same object: a session number, a session date, and every record anchored to one.

**Session is therefore a core object, not Storyteller's.** Number and date are allocated once per campaign rather than once per tool, which removes a class of drift before it can exist.

### Superseded reasoning, kept in place

An earlier position in this discussion held that Chronicle could not satisfy the two-clocks requirement in [[Inference-and-Candidate-Relationships]], on the grounds that it records no entry timestamp.

**That was wrong, and the corpus already contained the correction.** The chronology filter's own worked example — *the tattoo was described in session 3, the cult invented in session 20* — is expressed in sessions. Session granularity is the right grain, and Chronicle has had it from the start.

A second position, that session attachment is only an observation time and the store's write timestamp should be the authority, was also wrong and in a more interesting way. Chronicle transcribes notes taken in ink at the table. For anything transcribed, the observation was committed to a durable record during the session, and **a store timestamp would be less accurate than the session, not more.**

What survives from that reasoning is narrow and worth keeping:

- **Entry can lag the session even though attachment never moves.** Chronicle's `deferred_gaps` mechanism exists precisely so a gap can be acknowledged now and filled later, and the README records combat `cbt_003` as missing rounds 2 and 3 from session 4 with session 7 already played.
- **The discriminator is provenance, not timestamp.** A deferred gap filled from found physical notes and one filled from later reconstruction have identical session attachment and identical position in the record. Only one is a contemporaneous observation. [[Information-Architecture]] already requires provenance on every fact — who asserted it, from which side of the screen, and how it arrived — and that is what separates them.
- **The store's write timestamp is still worth keeping.** It costs nothing and is the only evidence that a reconstruction was entered long after the session it claims. Secondary evidence, never the authority.

This matters because the chronology filter's output is a claim that a connection *was not designed*. A missing record there is a lost observation. A wrong one is a confident false claim about the most valuable thing the tool does, with nothing in the data to contradict it. **For this filter specifically, wrong is worse than missing.**

---

## The overlap is augmentation, not conflict

The only place the two records touch the same material is when the scribe records receiving narrative information: the GM describes a town, relays what an NPC said, and the scribe writes it down.

**This creates no conflict, and the model already explains why.** The scribe's record is an *utterance* — what was said at the table. The GM's record is a *fact*. [[Facts-and-Revelation]] and [[Claims-and-Resolution]] make those different objects with different resolution states, so both coexist by construction. No merge, no precedence, no feature required.

### The discriminating case

**The scribe writes down the name the party heard, and the NPC lied about it.**

Chronicle's record is correct: that is the name the party was given. Storyteller's record is correct: that is not the entity's name. [[Names-and-Aliases]] already makes a Name a fact with an audience and a truth value, so both survive intact.

An implementation that treats the scribe's record as authoritative, or as a duplicate to be merged, loses the lie either way. The example is worth keeping because both readings agree in nearly every other case.

### The complementary case costs nothing

The GM forgets something and it never reaches session capture; the scribe wrote it down and it enters through Chronicle. That is not a reconciliation — it is a claim with no corresponding fact yet, which is an ordinary state in [[Claims-and-Resolution]]. Better data, no machinery.

---

## Divergence is the signal

The part worth building toward, and the reason two observers is more than redundancy.

**When the GM recorded revealing something and the scribe's notes do not contain it, that is not a gap to reconcile.** It is an uncorrelated measurement of what actually landed at the table.

[[Live-Set]] and Epic 3 S10 both name the same weakness: in Release 1 investment rests on the GM's own observation with no correction, so the tool orders by a recorded judgment rather than improving on it. The scribe's record is that correction, and it is uncorrelated because the scribe writes what the party received rather than what the GM intended to convey.

The inverse carries as much: the scribe wrote down something the GM never recorded revealing. Either the GM improvised and did not write it down, or the party inferred something that was never said. **Both are invisible to either observer alone.**

### This makes capture depth load-bearing

[[Shared-Core]] holds that depth of capture is a table-level variable and that sparse records are valid records. That was a fairness principle — a low-appetite table should not have its record look like unfinished work.

Under the divergence signal it becomes a correctness one. **A lightly-recording scribe makes every GM reveal look unconfirmed.** The signal only means anything read against a known capture depth, so the campaign container's depth configuration stops being cosmetic and becomes an input to the computation.

Belongs in acceptance criteria wherever this signal is computed, or thin capture will be read as failed transmission.

---

## Real conflict: narrow, and deferred

Some disagreements are not two points of view. The GM records that an enemy fled; the scribe records that it died. Both cannot be true.

**Unless the GM recorded a deception** — the enemy feigned death and the party believed it. Then the explanation exists as a fact, the claim resolves as false-but-believed, and nothing is wrong.

So the detection target is narrower than disagreement: **a party claim contradicts a GM fact, and nothing in the record accounts for why.** Three causes, indistinguishable to the system — an unrecorded deception, a scribe error, a GM error. Only the GM can say which, and the options are correct one side, correct the other, or record the deception. That is the Accept / Defer / Edit shape [[Shared-Core]] already commits to reusing.

### What is detectable, and what is not

`C7` in [[Hosting]] requires detection to be deterministic with no language model in the path. That bound holds here.

- **Detectable:** same entity, same typed attribute, mutually exclusive values. `alive` / `deceased` / `fled` are comparable.
- **Not detectable:** narrative disagreement. *The town seemed welcoming* against *the town was hostile* is prose, and attempting it either breaks C7 or produces noise. [[Open-Requirements]] §3 already warns that too-eager tickets get dismissed reflexively, which costs the ones that matter.

**Scope honestly: this catches lifecycle and status contradictions and nothing else.**

### Defer the feature, not the data

The detection itself cannot run until Chronicle writes into the core, which is after its v5 migration. The comparability that makes it possible cannot be added later — if disposition ships as prose, no deterministic check can ever compare it, and retrofitting means re-reading every character ever written.

Same line [[Release-Plan]] draws on S12: the data requirement is Release 1 and unrecoverable, the surfacing is later.

**The Release 1 obligation is one typed attribute. Nothing else.**

This also answers the blocking lifecycle question in [[Open-Requirements]] §7 in the narrow sense it needs answering — lifecycle state is a typed fact, following Chronicle's working shape of a disposition value plus a status event carrying type, session, cause, and the combat it occurred in. The wider questions in that section, on arcs transferring and whether a dead character stays in the graph, are untouched and stay open.

---

## The flag never reaches Chronicle

When detection is eventually built, its output is GM-only, and Chronicle must render no conflict state at all — not a filtered one, none.

Both halves leak under [[Visibility-Model]]. If the scribe can see which of their records the GM disagrees with, that is a map of the GM's secrets. And **suppression leaks identically**: a flag that appears on ordinary errors but never on deceptions tells the scribe exactly which of their beliefs are being protected.

So the detector runs over the unfiltered store, on the GM surface, and has no player-side representation. When the GM chooses to correct the party's record, that correction is a reveal and goes through the reveal path like any other.

---

## What the platform must hold from day one

The core is the platform's, not one tool's. Entity, Fact, Relationship, Event and Session are shared objects; each tool's context attaches to them by reference. Same tables either way — the cost is naming discipline, not scope, and the default failure is that Release 1 builds them as Storyteller's because Storyteller is the only tool in the room.

These are recorded as constraints in [[Hosting]]. Listed here with the reasoning.

| | Decision | Why it cannot wait |
|---|---|---|
| **Identifiers** | Opaque, non-sequential, type-free, unique within a setting, allocated by the store | Chronicle's are sequential with a published voided list — a count, which [[Visibility-Model]] establishes leaks the shape of what is hidden. Type in the identifier also blocks the merge [[Identity-and-Reconciliation]] requires. Chronicle's existing strings survive as aliases |
| **One entity table** | Type as an attribute, not a table and not a prefix | [[Information-Architecture]] already holds this. Chronicle encodes type three times; merge across type is impossible with any of them |
| **Relationships as rows** | With their own identity | Only a row carries visibility, provenance, and re-points on merge. Chronicle's are array elements on the source record, though its dormant top-level relationship collection shows the intent already exists |
| **The four unrecoverable requirements enforced at the write boundary** | By the store, not by an application | If Storyteller's application enforces them, a second writer bypasses them. See [[Release-Plan]] §4 |
| **No unfiltered read path exposed to a tool** | Extension of C5 across a tool boundary | Existence is the first gate in [[Visibility-Model]]. A shared entity set read directly is the GM's entity list, unfiltered |
| **Knowledge domain is a property of the request** | Not of the tool | Chronicle is not "the player tool" — it is a tool whose current users hold player knowledge. A co-GM using it breaks a hardcoded assumption. The orthogonality rule in [[Multi-Campaign-Hosting]], applied to tools rather than roles |
| **Account-level access** | One account per person from the start | Settled by the GM. See below |
| **System-specific payload opaque to the core** | A column the core never interprets | Where Chronicle's combat rounds live. [[Shared-Core]] sets the boundary at the event; this is where it lands physically |

### Account-level access supersedes the single credential

`C11` previously required only that the record not be publicly readable — a private deployment or one shared credential. Correct while [[First-User]] was accurate and the only user was the builder.

**Two observers means two people, and provenance is already a required property of every fact** — who asserted it, from which side of the screen. A shared credential answers that question with *someone*, permanently, for every fact written before the change.

Chronicle's v5 record independently specified session authentication with hashed passwords, so the platform acquires accounts regardless. The only question was whether Storyteller's store was built before or after that became true.

**Scope: one account per person, a password hash, a login. No signup, no invitations, no administration interface.** Those stay deferred under [[Multi-Campaign-Hosting]], which is explicit that stage 4 arriving early is how a working tool becomes an unfinished service.

---

## Known future requirements — excluded from acceptance

Recorded so they are not reconstructed later, and explicitly **not** acceptance criteria for any current epic, per [[Epic-Writing-Standard]].

1. **Conflict detection between a party claim and a GM fact.** Surfaces in prep alongside readiness. Never blocks capture or publishing — a contradiction is a decision only the GM can make, and blocking would put the scribe's workflow at the mercy of it. Dismissal is one persisted bit: unrecorded, it nags weekly until it is ignored reflexively; unpersisted, the thing genuinely does go unnoticed.
2. **Session-to-fiction-time anchor.** Needed to order a Storyteller off-screen event against a Chronicle observed event. One row per session, and not unrecoverable — the same shape [[Settings-and-Campaigns]] uses for cross-campaign fiction time.
3. **Speaker attribution on Chronicle content.** Chronicle carries no author, speaker, or attribution field. Every record is implicitly the scribe's, which loses who at the table actually said it. Unrecoverable in the same sense as the others, and unaffected by the clock reasoning above.
4. **Export covering the campaign rather than one tool's view of it.** `C9` portability fails for exactly the combined record that makes two observers worth having.

---

## Open questions

1. **Where does the division actually fall on party behaviour?** Epic 1's table-level signals — who conferred before acting, who raised something after a scene ended, who returned to something unprompted — are GM observations of party behaviour, which this document has placed on the scribe's side. Whether the scribe records the action and the GM the deliberation around it, or whether this is a second overlap, is unresolved.
2. **Does Chronicle's admin surface become a Storyteller surface, or stay its own?** The two share a core and an account system, and nothing yet says whether they share an interface.
3. **When does Chronicle's migration happen relative to Storyteller's cutover?** [[Store-and-Access]] asks for the cutover moment to be chosen rather than arrived at, and a second writer arriving is an event of the same kind.
4. **Chronicle's terminology.** Its README and `CLAUDE.md` use *DM* for the admin role, which is the scribe. [[Strategy-Multi-Campaign-and-Convergence]] is explicit that the DM does not participate in Chronicle at all. Harmless in one repository, misleading in a shared corpus.
