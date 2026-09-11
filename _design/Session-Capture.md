---
type: design
status: draft
visibility: gm
tags: [capture, requirements, sessions]
---

# Session Capture

Resolves the capture question from [[Open-Requirements]] §2. This is the near-term deliverable — no interface is needed for it.

---

## Settled

- **The GM captures most content**, at least initially.
- **Interactions are recorded as facts that imply meaning**, not as judgments of significance.
- **Qualitative description is recorded when present** — and is frequently absent.
- **The mechanism is templates plus this repo plus AI.** That is the tool for now.
- **No interface until the end of Floor 2** — roughly 4–6 sessions out.
- **Intake is human-in-the-loop**, in two stages — see below.

---

## Describe manner; don't rate meaning

The temptation is a field like `significance: high`. It fails structurally: **an interaction's meaning is often not knowable when it happens.** A GM asked to rate significance in the moment will guess or flatten everything to medium.

But capture shouldn't be terse where there's something to say. The line:

| Record this | Not this |
|---|---|
| "Played it reluctantly, kept deflecting with jokes" | "This seemed important" |
| "Called them an asshole, said we should have shanked them" | "Significance: high" |
| "Went quiet, then changed the subject" | "Probably an arc" |

The left column is **observation of manner** — checkable, still true in ten sessions. The right is **interpretation of significance**, derived later, not asserted now.

---

## Most interactions have no notable manner

"Asked a question, got an answer" is the common case, and it has no texture worth recording. **A blank manner field is the normal state, not a gap.**

This matters because a table with empty cells can read as unfinished work — the same trap as elective prep looking incomplete (see [[GM-Considerations]]). It isn't. Most rows will have nothing in that column, and a session where nothing had notable texture is an accurate record of a session where nothing did.

Forcing description produces noise. If manner gets filled in because the column exists, the signal is diluted by invented texture, and later clustering treats routine exchanges as remarkable.

---

## Expressiveness is not investment

Players differ in how much they perform, and the difference has nothing to do with how much they care.

A player who never does voices, states actions flatly, and rarely emotes may be the most invested person at the table. **A system that reads performance as engagement will systematically under-read them** — and that error compounds: fewer recorded signals means fewer arcs form around what they care about, which means less material aimed at them, which means less to respond to.

Two corrections:

**Baseline is per-player.** What's notable is deviation from how *that person* usually plays, not absolute expressiveness. A normally deadpan player becoming animated is a strong signal. An habitually theatrical player being theatrical is not.

**Manner isn't everyone's signal.** For players whose delivery genuinely doesn't vary, the other evidence carries the load — what they chose, what they returned to, what they argued for, what they remembered. Those work regardless of affect.

The practical rule: **never infer low investment from low expressiveness.** Absence of manner is absence of evidence, not evidence of absence.

---

## Recurrence is the primary signal

Stronger than any single interaction: **did they come back to it without being prompted?**

A character questioned in Session 3 and complained about in Session 4 is stronger evidence than any one exchange, however heated. Repetition across time can't be explained by circumstance — the moment had passed, and they returned to it anyway.

This cuts across the layers below rather than sitting inside one. When Z complains about an NPC an hour later, it doesn't much matter whether Sam said it in character or as himself. **The return is the evidence; the register is metadata.**

It's also the signal that works equally well for quiet players. Nothing about recurrence requires performance.

Practical consequence: note when something resurfaces, and note that it resurfaced *unprompted*. That word does the work — an answer to a GM question isn't the same as raising it themselves.

---

## Investment includes antipathy

Early framing skewed positive — bonding, protecting, affection. That's half of it.

**Hatred is investment, and often the more durable kind.** Nobody nurses a grudge about something they don't care about. An NPC the party loathes is arc material on the same terms as one they love, and comes pre-loaded: if that NPC reappears, tension exists before anyone speaks.

Capture records valence but doesn't filter on it. What matters is that attention persists, not that it's warm. Returning to the subject, arguing about how to handle them, remembering details, making plans involving them — all fire for an enemy exactly as for a friend.

---

## Three layers of signal

Secondary to recurrence, but worth distinguishing since they carry different weight.

### In-fiction — what the characters did

Spoke rather than fought, spared something, named an entity, gave away something valuable, returned somewhere unprompted, pressed someone on a topic.

### Table-level — what the players did

Asked about something unprompted; debated a choice before acting; remembered a detail the GM had half-forgotten; adopted a running joke; made plans involving a specific entity.

**Usually the strongest of the three.** In-fiction action can be tactical — sparing an enemy may be strategy. Three players arguing for ten minutes about whether to go back for someone has no tactical explanation.

**And the one least likely to be captured.** A prose recap naturally records in-fiction action, because that's what a narrative account *is*. Table-level facts require noticing something outside the story. It won't fall out of writing the recap; it needs a deliberate prompt.

### Roleplaying behavior — how it was played, when there's something to note

Register changes from that player's own norm. Emotional tone. Leaning in versus staying detached. Unusual care in describing their own actions. A choice that fit the character but cost them something. A choice that broke from how they'd played the character before — either a mistake or a development, and the difference matters.

Often empty. See above.

---

## Investment in one's own character

A distinct signal worth tracking separately: a player reaching for their dossier background unprompted.

When Z's anger traces to the paternal-contempt thread, or Hilda reaches for the grifter register, that isn't investment in the NPC — it's investment in *their own character*. Foundational, and worth knowing early, because "the dossiers are landing" is a different question from "the world is landing."

This one also doesn't require expressiveness. A flatly delivered choice that only makes sense given a character's backstory is the same evidence as a performed one.

---

## What a capture record needs

| Field | Purpose |
|---|---|
| Who | Character, or player if table-level |
| With what | Entity involved |
| What happened | Short factual statement |
| How | Manner, *if* notable — usually blank |
| Layer | In-fiction, table-level, or roleplaying |
| Recurrence | Whether this resurfaced unprompted |
| Session | When |

---

## Keep the write-up cheap

Capture happens after a session, when energy is low. Data entry doesn't get done, and inconsistent capture is worse than none — confident pattern detection over a biased sample.

- **A fact is one line.** Manner only if there's something to say.
- **Omission is expected.** The signal survives sampling.
- **Blank columns are correct**, not incomplete.
- **Prose recap stays.** Narrative and structured facts sit alongside each other.
- **Nothing is required.** A session with no interaction facts is a valid record.
- **Write manner in your own words.** No controlled vocabulary.

---

## Intake is human-in-the-loop, in two stages

Capture produces notes. Turning those notes into record changes is a separate step, and **it is not automatic**. Two stages, in order, that never merge. See **Intake** in [[Glossary]].

**1. Proposed changes, reviewed before anything is written.**

The system reads the session notes and proposes concrete edits: new entities, new facts on existing entities, new or extended relationships. Most of a session's output is *extension* of things already in the record, not creation of new ones — a known NPC gains a fact, an existing relationship gains a session reference, a place the party revisited gains what happened there this time.

The GM sees that as a list of discrete changes. Edit what's misread, reject what shouldn't land, accept the rest. **Nothing is written until accepted.**

This is not ceremony. Extraction from prose misreads in specific, predictable ways: it conflates an utterance with a claim, attributes a table-level remark to a character, invents manner where none was recorded. A wrong fact accepted silently doesn't stay a small error — it becomes a premise, and everything built on it inherits the mistake. Review is cheapest at exactly this point, while the session is still fresh and the fact hasn't propagated.

**2. Impact detection, only after acceptance.**

Once the facts are settled, the system looks at what they now imply and raises **Tickets**: a possible new connection, a possible shift in investment, a possible collision with a canon fact, two records that might be the same. These are all one thing — detecting impact on existing entities and relationships, and the inferences that follow.

Running this stage over unreviewed extractions would compound a bad reading into a bad conclusion, and a ticket carrying inferred weight is harder to dismiss than a raw misread line would have been. **Confirm what happened, then ask what it means.**

The ordering also keeps the GM's two jobs distinct. Stage 1 asks *is this what happened* — a memory question, answerable immediately after play. Stage 2 asks *does this matter* — a judgment question, and one the GM may reasonably defer.

---

## Why manner matters when it is present

**The debrief.** Recounting what was behind the screen is better with texture. "You all went completely silent" is what makes the retelling land.

**The callback.** A payoff hits hardest referencing *how* something happened — an NPC remembering that Hilda joked to cover her discomfort is sharper than one remembering she was present.

Texture also degrades faster than structure. What happened is recoverable from consequences; how it felt is gone in a week. That's the argument for recording it when it exists — not for manufacturing it when it doesn't.

---

## Open

**Do player notes eventually contribute?**
A player writing "I hope the rat made it" is a self-reported table-level signal — and a channel that doesn't depend on the GM reading expressiveness at all. Possibly the best correction for the quiet-player problem.

~~**Does the AI extract facts from the prose recap?**~~
**Resolved: yes, as stage 1 of intake — proposed, never applied.** Cheaper than writing both, and the review gate is what makes extraction safe to use at all. Manner stays the riskiest field, being the most interpretive and the most likely to be invented where none existed; it warrants the closest attention during review, and [[Constraint-Manner-and-Intent]] holds that Storyteller never generates it in the first place.

**How is recurrence recorded without re-reading old sessions?**
Noticing something resurfaced requires remembering it surfaced before. Strong GM recall covers this early; at scale it may need support. Impact detection is the natural home for this once it exists — a new fact about an entity the party has touched before is exactly the kind of impact stage 2 is looking for.

**How long until enough accumulates?**
Clustering needs volume. Four to six sessions may not produce detectable patterns — fine, since the interface isn't due until then.
