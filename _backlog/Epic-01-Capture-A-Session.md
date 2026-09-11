---
type: epic
id: epic-01
status: ready
release: R1
candidate: 1a
visibility: gm
tags: [epic, capture]
---

# Epic 1 — Capture what happened in a session

Terms marked on first use are defined in [[Glossary]].

---

## Who it is for

The **game master** — the person who prepares the world and runs it at the table. In Release 1 this is the only user.

They are trying to turn a few hours of live play into a record they can rely on later, in the small amount of time and attention available afterward.

---

## The problem

A **session** produces far more than the GM can hold. Some of it is obvious — what the party did, where they went, who they met. Some of it is nearly invisible at the time and turns out to matter most.

**A vignette.** A scene ends. The party is moving on. One player circles back and asks a small question about a minor character — whether he has family in the area. Nobody remarks on it. The GM answers offhand and play continues.

Three sessions later, the party goes looking for that character's brother. The GM has no idea why. Nothing in the write-up records the question, because the write-up was a narrative account of what happened, and the question happened *around* the scene rather than in it.

The detail was never lost. It was never captured.

The general shape: **a narrative recap records the story, and the signals worth having are not in the story.** They are at the **table level** — who conferred before acting, who raised something after the scene had ended, who returned unprompted to something from weeks ago.

Meanwhile the time available is small. Capture happens after play, tired, with other things pending. Anything that feels like filling in a form does not get done, and a record that is not written is not a record.

---

## What is not being asked for

- **Not a transcript.** A sample of what mattered, not a log of everything.
- **Not scoring or rating.** Nothing here judges how significant an interaction was.
- **Not inference about people.** The tool records what the GM says happened. It does not decide what anyone felt, wanted, or intended.
- **Not analysis.** Noticing patterns across sessions is Epic 6. This epic only produces the material.
- **Not editing the wider record.** Creating and connecting entities is Epic 4. This epic writes session records that reference entities.
- **Not correction or rollback.** Repairing a bad batch is Epic 12. Adding to a record you wrote yourself is in scope; undoing damage is not.
- **Not offline operation.** Web-first from day one, per [[Strategy-Multi-Campaign-and-Convergence]]. See S11.

---

## Assumptions

Domain assertions this epic rests on. Take these as given — they are established elsewhere and are not the right target for review.

| Assumption | Source |
|---|---|
| Anything not recorded at the time is not recoverable later | [[Session-Capture]] |
| Capture happens after play, from memory and rough notes — not live | [[Session-Capture]], [[Update-Cadence]] |
| Capture that costs effort does not happen, and the tool's value collapses with it | [[GM-Considerations]] |
| How someone behaved cannot be inferred by a system; only observed by a person | [[Constraint-Manner-and-Intent]] |
| A quiet player is not a disengaged player; expressiveness is not investment | [[Session-Capture]] |
| Returning to something unprompted is the strongest available signal of what the group cares about | [[Session-Capture]] |
| What someone was *told* and what is *true* are different records and must not be merged | [[Facts-and-Revelation]], [[Release-Plan]] |
| An empty field is a valid record, not an incomplete one | [[Session-Capture]], [[Shared-Core]] |
| The table where this campaign is played has reliable connectivity | Confirmed by the GM; see Epic 2 |
| Intake is two stages — proposed changes reviewed and accepted, then impact detection — and this epic owns only the first | [[Session-Capture]], [[Glossary]] |

---

## Value, and the cost of omission

**This epic produces the asset the whole product is built on.** Every later capability — retrieval, readiness, noticing threads, the player's record — is a query over what this epic captured. Nothing downstream can be better than its input.

Three distinct costs if it is absent or weak:

**The signal is gone, permanently.** Unlike most software gaps, this one cannot be filled in later. A question asked around a scene three weeks ago is not reconstructible.

**A flat record is worse than no record.** If capture flattens what someone was told into a plain statement of fact, then the record asserts lies in its own voice. Release 2 cannot be built on it without re-encoding every session by hand, and the first time a player reads a page, every deception in the campaign is spoiled.

**It has the earliest deadline in the plan.** Sessions are being played now, weekly. Every session captured before this exists is either captured in the correct shape by hand, or becomes migration work.

---

## Stories

### S1 — Write up a session in one pass

*As the GM, I want to record a session in a single sitting shortly after play, so that it gets done at all.*

- **Outcome:** A complete session record exists within the window where memory is still good, without the GM abandoning it partway.
- **Assertion:** A record can be saved at any point with any subset of its parts filled in. No part is required in order to save.
- **Demo:** Save a record containing only a recap. Save another containing only two interaction rows. Both are valid and readable.

### S2 — Record what happened, in order

*As the GM, I want to write what occurred during the session in sequence, so that I can reconstruct the shape of it later.*

- **Outcome:** The sequence of events is recoverable months later without relying on memory.
- **Assertion:** Events retain their order and each can reference the entities involved.
- **Demo:** Read back a session's events in the order they were entered.

### S3 — Record who interacted with what, and how it landed

*As the GM, I want to note the interactions that stood out — in the story and around the table — so the things that mattered are not buried in a narrative account.*

- **Outcome:** Both layers are captured separately: what characters did, and what players did.
- **Assertion:** In-fiction and table-level interactions are distinguishable in the record. A manner field may be empty and the row remains valid.
- **Demo:** Enter one of each with manner blank; read them back distinguished by layer.

### S4 — Note when someone behaved unlike themselves

*As the GM, I want to record when a player departed from their own norm, so that engagement is read against the right baseline.*

- **Outcome:** A quiet player becoming animated is captured. A quiet player staying quiet produces nothing.
- **Assertion:** The record holds no measure of expressiveness, activity level, or participation — only noted departures, entered by the GM.
- **Demo:** Show a session with three participants and one noted departure. Nothing in the output ranks or scores the other two.

### S5 — Record what they came back to on their own

*As the GM, I want to note when the party returns unprompted to something from an earlier session, so the strongest signal available is not the one I forget.*

- **Outcome:** Resurfacing is captured with what it points back to.
- **Assertion:** A resurfacing entry references both the current session and the earlier subject.
- **Demo:** Enter one referencing an earlier session; read it back from both ends.

### S6 — Record what people told the party, as things they were told

*As the GM, I want what an NPC said recorded as something said, so the record never asserts a lie in its own voice.*

- **Outcome:** The record can say *he told them the tunnels flood* and separately hold whether that is true.
- **Assertion:** Every statement made to the party carries a speaker and is stored distinctly from any world fact. Its truth status is a separate value, not visible to players, and may be set later or left unset.
- **Demo:** Enter a statement with truth unset. Set it to false. The utterance is unchanged; only the separate status differs.

**This is the highest-consequence story in the epic.** Everything about Release 2 and any future consolidation depends on it being right from the first session.

### S7 — Record what appeared for the first time

*As the GM, I want to note what the party encountered for the first time, so that from now on the record knows they are aware it exists.*

- **Outcome:** First appearance is captured, and what the party learned about it is captured separately.
- **Assertion:** An entity's first appearance is recorded against a session. Its existence and its name are recorded as separate things — an entity can appear without its name being known.
- **Demo:** Record a first appearance with no name learned. The entity is marked as having appeared; no name is marked known.

### S8 — Record what the party called things

*As the GM, I want to note the names the party used at the table, so their coinages survive and so their names and mine do not drift apart.*

- **Outcome:** A party-invented name is preserved and can become the accepted name.
- **Assertion:** A name captured this way is attributed to the party and can be attached to an existing entity without displacing its other names.
- **Demo:** Attach a party name to an entity that already has one. Both are present; neither is lost.

### S9 — Record what I revealed, and when

*As the GM, I want to note what I made known to the party after a session, so that later I can show them what is new and can see what they should already know.*

- **Outcome:** A reveal is a dated occurrence, not just a current state.
- **Assertion:** Each reveal records what was revealed, of what kind, and when.
- **Demo:** Record two reveals on different dates; read back the sequence.

### S10 — Leave things blank

*As the GM, I want to leave most fields empty without being prompted to fill them, because most of the time there is nothing to say.*

- **Outcome:** A sparse record reads as finished, not as unfinished.
- **Assertion:** No completeness score, progress indicator, or prompt to fill appears anywhere in this epic's output. An empty section is valid and never flagged.
- **Demo:** Save a session with every optional part empty. Nothing in the output suggests it is incomplete.

### S11 — Catch a fragment mid-session

*As the GM, I want to jot something down during play in a few seconds, so that a detail worth keeping survives until I write up.*

- **Outcome:** A fragment captured at the table is waiting when the GM writes the session up.
- **Assertion:** A fragment can be saved without choosing a category, entity, or session part, and appears attached to the session in progress. A save that fails says so immediately and keeps the text on screen — a fragment is never silently lost to a bad moment on the network.
- **Demo:** Save three words mid-session. They appear in that session's write-up unattached to anything else. Repeat with the network unavailable: the failure is stated at once and the text is still there to retry.

### S12 — Get help turning rough notes into a record, without invention

*As the GM, I want assistance shaping my scrappy notes into a session record, so long as nothing appears that I did not say.*

- **Outcome:** The GM writes less and reviews more, without losing authorship of the content.
- **Assertion:** Assistance produces a list of proposed changes that the GM approves, edits, or rejects individually before anything is written. No manner, intent, or emotional state appears in any proposal. No field is populated because it exists.
- **Demo:** Feed in rough notes containing no emotional description. Every manner field in the proposal is empty. Reject the proposal; nothing is written.

**This is stage 1 of intake**, per [[Session-Capture]]. Stage 2 — impact detection over accepted changes — belongs to Epic 6 and must not run here, since inference over unreviewed extraction compounds a misreading into a conclusion.

### S13 — Add to a session record later

*As the GM, I want to add something to a session I have already written up, because I will remember things afterward.*

- **Outcome:** A later addition is possible without rewriting the record or losing what was there.
- **Assertion:** An addition is recorded with the date it was added, distinct from the session's own date.
- **Demo:** Add an interaction a week after the session. Both dates are visible.

---

## Open questions

| Question | What it blocks | Where it sits |
|---|---|---|
| ~~Does capture work with no connectivity?~~ | — | **Resolved: no.** Web-first from day one and the table has a reliable connection. S11 instead requires that a failed save is stated immediately and the text retained. Capture is the recoverable half — write-up already happens after play — so if offline is ever built, retrieval needs it first |
| What counts as invention when shaping rough notes? Splitting a sentence into two rows is structure; choosing which entity it refers to may not be | S12's assertion | Needs a threshold before S12 can be accepted |
| Is mid-session capture actually used, or does it break the GM's attention more than it saves? | Whether S11 is worth its cost | Answer by observation over a few sessions, not in advance |
| How are corrections distinguished from additions before Epic 12 exists? | S13's edges | Deferrable — S13 covers addition only |

---

## Dependencies

- **Epic 4** creates and connects entities. Session records reference entities; this epic assumes they can be referenced, not that it creates them. Where a session mentions something with no record yet, the fragment is captured against the session until Epic 4 provides somewhere to put it.
- **Epic 6** owns stage 2 of intake. This epic stops at accepted changes.
- **Prerequisites P2 and P3** — harness and fixtures — must exist before any story here can be accepted, since every assertion above runs against a fixture rather than the live campaign.
