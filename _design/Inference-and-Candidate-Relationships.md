---
type: design
status: draft
visibility: gm
tags: [inference, relationships, tickets, model, information-architecture]
---

# Inference and Candidate Relationships

How the system proposes a connection it was never told about, and how the GM's judgment stays in charge of it.

Companion to [[Information-Architecture]], [[Session-Capture]], and [[GM-Considerations]]. Supplies the mechanism behind **Ticket** and **Signal** in [[Glossary]]. Implemented by Epic 6, in RC 1c.

**This document is detective only.** Proposing invented fiction is [[Generative-Projection]]; the two layers compose — detection finds the gap, generation proposes thread.

---

## What is being inferred

**A relationship between two entities.** Not a fact, not a story beat, not a motive. The system's whole claim is *these two things may be connected, and here is why I think so.*

That keeps it on the right side of the surfacing-versus-authoring line. Proposing a connection extends what the GM can notice. Proposing what the connection means would be authoring.

---

## Attributes are weak evidence; structure is strong

The tempting first design is matching on shared properties. Two NPCs both favour yellow; the setting contains a Cult of the Yellow King; therefore raise a ticket.

**This is mostly wrong, and the reason is about authoring rather than statistics.** A GM who invents an NPC bearing the cult's tattoo will almost always record the membership at the same time. Deliberate authoring leaves few coincidences worth finding, and shared descriptive attributes — hair colour, home town, a favoured drink — are common enough that matching on them produces noise at volume.

**But the argument has a boundary, and the value sits exactly at it.** Attribute coincidence is worth examining in three cases, all identifiable from data the record already holds:

- **The fact came from play, not authoring.** The GM improvised a mark on the innkeeper's wrist mid-scene and it arrived through intake. Nobody designed it against anything.
- **The fact predates the concept.** The tattoo was described in session 3; the cult was invented in session 20. Both were authored correctly, and the connection could not have existed at the time. **This is the strongest case**, and the one a person reliably misses, because catching it means remembering session 3 while writing session 20.
- **The fact came from an external author.** Canon import, where nobody was linking anything to this setting.

So the filter is **provenance and chronology**, not a similarity score. A GM-authored fact newer than the concept it matches is low value and should usually stay quiet. Anything else is worth a look.

**One shared attribute is weak. Many is a different claim** — not a stronger coincidence but a pattern. See §Parallel without contact, which is not a reversal of this section.

### Rare matches are worth more than common ones

Two NPCs both human is nothing. Two from the same obscure origin is something.

**Inverse frequency, computed off the store.** No tuning constant, and it is the same insight as borrowed weight below arriving from a different direction — a cleaner version, because frequency is measured rather than depending on the GM having set an investment degree.

---

## The signals

All readable off the graph without a tuned prior.

| Signal | What it is |
|---|---|
| **Unexpected density** | Two entities joined by more independent paths than the graph's own baseline |
| **Convergence** | Several otherwise unrelated threads landing on the same entity |
| **Co-occurrence without connection** | Two entities appearing in the same sessions repeatedly with no recorded link |
| **Borrowed weight** | A coincidence landing on a concept the setting has invested in — the cult, not the colour |
| **Parallel without contact** | High factual similarity combined with no existing relationship — see below |

Borrowed weight is worth stating plainly: **narrative weight is inherited, not intrinsic.** Yellow is not interesting. Yellow is interesting because something in the setting made it load-bearing, and [[Glossary]]'s **Degree of investment** already records which concepts those are.

### Co-occurrence needs the tightest gate

It is the fastest-growing signal by far. A session with 25 entities offers roughly 300 pairs, nearly all meaningless.

The word **repeatedly** above is load-bearing and must be a stated minimum — two or three sessions together with no recorded link. That single requirement removes most of the largest generator's volume, and unlike a threshold on strength it is a statement about the evidence rather than a tuned cutoff.

### Signal count should be capped

The real risk in *generate freely* is signal proliferation, not output volume. Each new signal is code with its own edge cases. Five is the current set; a sixth should have to displace something rather than simply be added.

---

## Parallel without contact

**High factual similarity combined with an absence of existing relationships.** Neither half is a signal alone: similarity by itself is the yellow-cult noise rejected above, and absence of relationship describes most of the graph. **The conjunction is what is rare.**

Both halves are **counts** — shared typed facts high, paths within N hops zero — which keeps the detection procedural. No similarity score.

Two NPCs share species and profession, belong to no common faction, and keep shops in different markets. There is room for a background connection through a master who does not exist yet. **Likenesses that leave a short gap, bridgeable by a single planned event.**

### It detects absence, which makes it behave unlike the others

**It stays detective, and only by stopping early.** The system detects the gap; the GM invents the bridge. *These two are similar and unconnected, and the gap is one hop wide* is observation. *They were apprenticed to the same master* is authoring — that belongs to [[Generative-Projection]], and this is the signal where the line is closest to being tripped over.

### What it actually measures is obstruction, not potential

The domain intuition worth recording, because it motivates the signal and must not be implemented literally.

Entity data is **sparse by nature.** The only facts a GM produces are those that serve the story, so any entity carries a light fact set. Around it sits a cloud of undefined facts that *could* be true, and the overlap of two entities' clouds is where opportunity for connection lives.

**The cloud is not computable, and for the same reason the probability field was rejected in [[Claims-and-Resolution]].** The space of possible undefined facts is unbounded and has no distribution over it — nothing constrains *possibly apprenticed to a smith* against *possibly a smuggler's cousin*. The overlap of two unbounded clouds is total: **any** two entities can be connected by some invented fact. That is what makes a GM's job possible, and it means overlap cannot discriminate.

What is computable is the complement: **the observed facts, and what they rule out.** Sparsity plus no competing commitments means the space of cheap bridges is large. Density of established fact shrinks it. So the signal measures **absence of obstruction**, which is the same structure as an open claim staying free until the record grows around it.

**And similarity does something specific, which is also not overlap.** Shared species and profession do not enlarge the cloud. They make an invented bridge **plausible to the table** — the party hears *they trained under the same master* and it lands, because two smiths of the same people sharing a teacher needs no justification. Similarity buys narrative permission, not probability. It is a coherence property of the eventual reveal.

### Three measurable conditions

- **Sparse** — few established facts on either side, so little to contradict
- **Similar** — shared typed attributes, so an invented link reads as natural
- **Unobstructed** — no path within N hops, and no commitments a bridge would overwrite

The third clause is what separates an opportunity from a problem. Two equally similar NPCs already in rival factions have an **expensive** gap: bridging means overwriting something established. That check is the same coherence mechanism the claims work needs, so one implementation serves both.

### Substance is non-monotonic

Unusual among these signals and worth stating rather than discovering.

**Some** authored substance is required, or the signal matches two stub records and means nothing. **Past a threshold, more substance reduces the opportunity**, because there is more to contradict. The signal peaks in the middle.

### It grows as the graph sparsifies

Every other signal gets noisier as the graph densifies. This one inverts — and the graph is sparsest at session three, when nothing is connected and every NPC resembles every other. **It fires hardest when the GM has least context to judge it.**

Mitigations, none needing a tuning constant: both entities must have **materialized**; at least one at **Notable investment or higher** (borrowed weight); and the substance floor above.

### It belongs in planning, not capture

Every other signal answers *what did I miss in what just happened.* This answers *what could I build next.*

So it surfaces in Record Plans and the [[Live-Set]], alongside open claims — and it is the same kind of object. **A bridgeable gap and an undetermined claim are both options the GM has and may not know about.** They should surface together rather than in separate queues.

Per [[Planning-Loop]], it will spike on regional passes and quiet on weekly ones. That is correct behaviour.

### Its precision calculus is looser

A wrong co-occurrence clue asserts something false about the record. **A wrong gap asserts nothing** — it simply is not interesting. So the failure mode is volume rather than error, and the answer is the attention budget rather than a tightened threshold.

---

## Procedural and generative

**Procedural to find. LLM to read.**

| Stage | Which | Why |
|---|---|---|
| Extraction — prose into facts, claims, speaker attribution | **LLM** | Prose in. No procedural option exists. |
| Clue detection — all five signals | **Procedural** | Graph queries. An LLM asked *which pairs co-occur with no recorded link* would be slower, unauditable, and would invent pairs. |
| Candidate strength | **Procedural** | Counting clues. No confidence numbers. |
| The walked path | **Procedural** | It *is* the explanation. |
| Contradiction / coherence check | **Hybrid** | Procedural narrows to the neighbourhood; LLM evaluates only that small set; output is a reviewed proposal. |
| Stitch proposals | **LLM** | [[Generative-Projection]] |

### An LLM may propose, never gate

Hallucination is survivable when the output is a proposal the GM reviews against a source. Extraction is safe because it sits behind two-stage intake — and safer if every proposed fact **cites the span of recap text it came from**, which makes fabrication visible rather than merely possible.

Hallucination is **not** survivable when the output is a filter. If an LLM decides what *not* to surface, its errors are invisible — the false-negative-invisible asymmetry this whole design is built around. **The gate is always procedural.**

### The golden corpus settles it

[[Glossary]] **Golden corpus** is frozen GM judgments, replayed against later changes to check nothing regressed. **That only works if detection is deterministic.** An LLM in the detection path makes the corpus unreplayable: a changed result cannot be attributed to the code change rather than to sampling variance.

So extraction may be nondeterministic because a human reviews every output. **Detection must be deterministic because it is the regression test.** That is a constraint, not a preference, and it is why the split cannot go the other way.

---

## Acceptance is the trigger

Inference does not sweep the graph. **It expands from the frontier: when a relationship is accepted, the neighbourhood it opens is examined.**

Once a connection from A to B is established, B's existing relationships become worth checking against A's facts. The new edge is a doorway, and what lies beyond it has never been compared to A before.

This is bounded work rather than a global scan, and it fits the write-once-per-session rhythm — acceptance happens during intake, which is when the examination runs. Inside the [[Planning-Loop]] it runs per iteration.

### Distance is a hard limit, not a gradient

**Two hops from the accepted edge. Full stop.**

Proximity does carry value — a candidate one hop out is stronger than one two hops out — but expressing that as a decaying score would require a tuning constant with nothing to justify it, and a large graph still produces enormous numbers of weak distant candidates that sum to noise. A stated cutoff is defensible where a decay curve is not.

### The cost is degree, not fact count

Worth being precise, because the intuition that candidates explode with the record is only half right.

Work per pass is roughly **accepted edges × local degree²**. Total fact count does not enter it: a campaign with 10,000 facts and one with 1,000 do the same work per session at the same local density.

**The growth is in degree, and it is concentrated** — the party, the current floor, a central faction. A node of degree 500 alone offers 250,000 two-hop pairs. **Degree skew is the real scaling failure, and it arrives long before fact count matters.**

### Structural edges are not inference intermediates

The fix, by edge type rather than by degree threshold.

Containment and membership edges are **not evidence-bearing**. Everything is inside a Place; everyone is in the party. A path running *A is in Zone 3, Zone 3 contains B* is not a clue — it is a restatement of geography.

**So structural edges are traversable for retrieval and not traversable as inference intermediates.** Defensible in the same way the two-hop cutoff is, where a degree-weighted score would not be.

### Inferred edges can be walked, with their provenance visible

An accepted-but-inferred relationship is a legitimate hop for the next inference. That is what makes the frontier model work at all.

It also compounds error: a wrong acceptance becomes evidence for the next candidate. Two protections, both using what the model already has:

- **Provenance distinguishes GM-authored, inference-accepted, and generated-accepted.** A chain resting on inferred or generated edges is weaker than one resting on authored ones. Read, not estimated.
- **The ticket shows the path it walked.** Not a confidence number — the actual route: *A connects to B, B knows C, and A's facts mention C's home village.* A bad chain becomes visible rather than hiding behind a score.

---

## The clue is the durable unit

**Correction to an earlier framing in this document.** The candidate was described as the durable unit. It is not — the **clue** is, and the candidate falls out of it.

A **clue** is a concrete detection that actually fired. A **candidate** is a grouping of clues by entity pair: a derived view, not a stored record.

Why this matters: *generate freely, gate hard* controls what the GM **sees**, not what gets **stored**. If candidates were durable records, generating freely would mean storing freely, and the store would grow with generated candidates rather than surfaced ones. With clues as the unit, **nothing is stored for the millions of pairs where no clue ever fired**, strength-as-clue-count is unchanged, and the accumulation model is unchanged.

**Inference justification: the more clues, the stronger the inference.** One coincidence is weak. The same pair arriving through a shared session, a converging thread, and an attribute landing on an invested concept is a different proposition — not because any clue got stronger, but because there are more of them.

Same shape as **Investment** in [[Glossary]], deliberately. Signals accumulate; the system surfaces; the GM decides. Neither computes a verdict.

### Acceptance and rejection

**Accept** creates the relationship, with provenance recording that it was inferred and accepted rather than authored. It also opens a new frontier.

**Reject clears the item from the GM's view.** The candidate does not remain as a task, does not appear in any backlog, and is not browsable. The GM's list holds only live candidates.

**A rejected candidate resurfaces only when a new clue is detected for that same pair.** Not on a timer, not on review, not because the GM asked to see old ones. New evidence is the only trigger — and per [[Planning-Loop]], this must hold *within* a planning pass, where evidence changes every iteration by design.

That is what makes repeated surfacing legitimate rather than nagging. Each appearance answers a different evidence set. [[GM-Considerations]] warns that reflexive dismissal is the failure mode for this whole feature — and the protection is not a cap on how often something may appear, but the rule that nothing appears without cause.

**When a candidate resurfaces, the earlier rejection is shown with it** — what was rejected, and on what evidence. Otherwise the GM evaluates the full clue set cold and may rule out the same clues twice without realising it.

---

## Information architecture requirements

What the store must hold for any of this to be buildable. **Several of these are unrecoverable if omitted** — the information is never captured, so the signal becomes permanently impossible rather than merely unbuilt.

### 1. Two clocks — unrecoverable

**Record time** (when a fact entered the store) is a different clock from **fiction time** (when the thing happened in the world). An event can be authored in session 20 and set three hundred years earlier.

The chronology filter — *the tattoo was described in session 3, the cult invented in session 20* — reads **record time exclusively.** Every fact, entity, relationship, and claim needs both. This is the highest-cost omission on the list and the cheapest to prevent now.

### 2. Session membership must be structurally distinct from narrative connection

*Co-occurrence without connection* is incoherent if appearing together in a session is itself an edge in the same graph — the signal would be detecting its own input.

Participation in a session must be a different kind of thing from *knows*, *owes*, *contains*. If the graph is uniformly typed edges, this needs a deliberate partition.

### 3. Typed facts — unrecoverable

**Parallel without contact** works only over facts carrying **structure**: a type and a comparable value. *Has a scar on his wrist* and *bears an old mark on his forearm* are the same fact in prose and different strings to a matcher.

If capture stores everything as free prose, high factual similarity is either unbuildable or needs an LLM in the detection path — which breaks golden-corpus determinism.

So some facts need a **typed shadow** alongside their prose, populated during extraction. Prose stays primary for reading; the typed form exists for matching. A new extraction target in [[Session-Capture]], next to speaker attribution.

**Which attributes are worth typing is not "all of them."** Species, profession, origin, era — the small set plausibly indicating shared background. Not hair colour. And the list need not be settled by argument: the **golden corpus** records which gaps the GM found worth bridging, so which attribute types actually preceded accepted bridges becomes readable after enough sessions.

### 4. Clue identity, idempotency, and snapshotting

Three properties, all load-bearing, none currently stated:

- **Deterministic key** — clue type plus the specific facts it walked, so re-running a pass does not re-add the same clue.
- **Snapshot at rejection** — *the earlier rejection is shown with it, on what evidence* only works if the clue set was frozen. If clues are recomputed each pass, the rejection record describes evidence that may no longer exist.
- **Stored path, not regenerated** — if the walked route is recomputed at display time it can differ from the route that justified the clue.

### 5. Candidate identity under reconciliation

A candidate is keyed on an unordered pair, and [[Identity-and-Reconciliation]] merges records that turn out to be one thing. Three unspecified consequences:

- candidates on the merged entities must combine
- their clue sets must dedupe
- **any candidate whose endpoints are now the same entity must be destroyed**, not left proposing that something connects to itself

### 6. Clues resting on planned facts have no lifecycle

Record Plans lands facts in `planned` state, and a ticket raised before a session is the most valuable kind. But a clue can rest on a plan that changes or never happens.

Currently a discarded plan leaves permanent evidence for a connection that was never established. Needs a decision: does the clue survive, weaken, or vanish?

### 7. Weak edges are derived, not stored

Co-occurrence, convergence, and density are all **derivable** from session membership and existing typed edges.

If no weak signal needs storing, the open weak-edge vocabulary question in [[Modes-and-Surfaces]] largely dissolves, and the search-index-as-projection compromise becomes unnecessary rather than merely sufficient.

**Worth deciding explicitly as derived-not-stored**, because the alternative gets built by default the first time someone wants to cache a co-occurrence count.

---

## Generate freely, gate hard

The set of things that can *produce* a clue should stay open. Triggers will be various, and constraining them early forecloses the discoveries that justify the feature. Note the signal-count cap above: freedom applies to what fires, not to how many detectors exist.

**What gets shown is a different question.** An unbounded generator over a connected graph produces combinatorially many low-weight candidates, and flooding is not a mild failure — [[Backlog-Readiness]] §G4 is explicit that an untuned threshold does not merely underdeliver, it teaches the GM to ignore the feature permanently. That damage does not reverse.

So: broad generation, conservative surfacing, and the **golden corpus** as the record of what the GM judged worth seeing.

---

## What this does not do

- **No confidence numbers shown to the GM.** The evidence is the explanation. A percentage invites arguing with a number instead of looking at the clues.
- **No automatic creation.** Nothing becomes a relationship without acceptance, per [[Constraint-Manner-and-Intent]].
- **No proposing what a connection means.** The candidate says *these may be connected*. What it signifies is the GM's. Proposing the bridging fiction is [[Generative-Projection]] and lives under its own rules.
- **No browsable dormant set.** Rejected candidates are invisible until new evidence arrives. A list of everything ever proposed is a backlog the GM will never clear, and a tool that makes its user feel behind stops being opened.
- **No inference at the table.** [[Constraint-Serves-The-Table]].

---

## Deliberately deferred

**Relationship-type rules.** *Members of this cult bear this tattoo* is a property of the relationship type rather than of any instance — an inference rule the GM authors, converting a coincidence into a testable implication. Genuinely more powerful than statistical matching, and genuinely scope creep: it is a rules layer the GM has to build and maintain, and [[Scope]] is hostile to rules layers for good reasons.

Recorded here so it is a decision rather than an omission. Not part of Epic 6.

---

## Open questions

| Question | What it blocks | Where it sits |
|---|---|---|
| ~~Where does the surfacing-versus-authoring line sit?~~ | — | **Settled** by [[Modes-and-Surfaces]]: surfacing is authoring, materialised through intake. Generative proposals are separately governed by [[Generative-Projection]] |
| What is the baseline against which density counts as unexpected? | The density signal | Needs a stated basis, however crude. Likely refined by observation rather than decided in advance |
| What is N for *no path within N hops*? | Parallel without contact | Two is the working assumption, matching the frontier cutoff. Unverified |
| What is the minimum session count for co-occurrence? | The largest generator's volume | Two or three. Needs a number in acceptance criteria |
| Where is the substance floor, and where does the non-monotonic peak sit? | Parallel without contact | Cannot be reasoned out; needs observation against a real record |
| Does a clue expire? | The store's growth curve | Now a storage question, not only a relevance one. Rejected candidates persist awaiting new evidence indefinitely, and with clues as the durable unit that is monotonic growth. Needs a decision **before the store design locks** |
| Is an inferred-and-accepted edge ever promoted to authored? | Nothing yet | Provenance says how it arrived. Whether GM editing changes that is a small question with no current consequence |
