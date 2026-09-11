---
type: epic
id: epic-13
status: ready
release: R1
candidate: 1a
visibility: gm
tags: [epic, migration, import]
---

# Epic 13 — Move the campaign into the tool without losing anything

Terms marked on first use are defined in [[Glossary]]. Rescoped and moved into RC 1a by [[Migration]].

---

## Who it is for

The **game master**, at the point where the tool becomes real and several months of existing writing has to come with them.

They are trying to start using something new without abandoning what they have, and without re-reading every page to check that it survived.

---

## The problem

The existing record was written for a person to read. The tool needs it as things it can query — entities, facts, and connections, each with its own source and its own visibility.

Those are different shapes, and the gap between them is not mechanical.

**A vignette.** A **zone** file mentions a locksmith in a sentence: *the party could reach him through the woman at the granary.* In the file that is a connection any reader would follow. In the store it is nothing — a link with no type, no direction, and no record that it exists at all.

The conversion reports success. Nothing looks wrong. Six sessions later the party asks how to reach the locksmith, the GM searches, and the answer is not there — even though it was written down, and even though nobody deleted it.

The general shape: **content can survive conversion and still be effectively lost.** A fact trapped in a paragraph cannot be found. A connection that never became a connection is gone. And the failure is silent — the output looks complete, because the missing thing leaves no gap behind it.

There is a second danger running the other way. A file marked GM-only says nothing about which of its individual facts the party already knows. Guess generously in one direction and the campaign is spoiled, quietly, the first time a player reads a page.

---

## What is not being asked for

- **Not ongoing synchronisation.** This is one-way and happens once. Writing the record back out as readable files is a standing requirement, not this epic's job — though S2 depends on it existing.
- **Not improving the content.** Badly written prose stays badly written. This epic changes shape, not quality.
- **Not authoring.** Creating and connecting new material is Epic 4.
- **Not repair.** Undoing damage to a live store is Epic 12. This epic's protection is that it never damages the source.
- **Not judging what should have been recorded.** Gaps in the existing record are the record's business, and per [[Shared-Core]] absence is never inferred to be an omission.
- **Not multi-campaign or multi-setting capability.** S11 creates the containers and fixes the addressing and identity shapes. Seeding a second campaign, switching between them, accounts, and sharing are all out — see [[First-User]] and [[Settings-and-Campaigns]].

---

## Assumptions

| Assumption | Source |
|---|---|
| The campaign record is live and irreplaceable | [[Shippable-Increment]] |
| Prose and untyped links cannot be converted by inference — the information simply is not there | [[Migration]] |
| Defaulting to GM-only is always safe; defaulting the other way spoils silently | [[Visibility-Model]] |
| Template-shaped content converts mechanically; everything older does not | [[Store-and-Access]] |
| Known model errors exist in the live content and must be resolved rather than carried forward | [[Backlog-Readiness]] §G10 |
| A gap has two causes and the difference cannot be inferred | [[Shared-Core]] |
| Optionality is cheap; capability is expensive. The containers cost almost nothing now and are migrations later | [[Strategy-Multi-Campaign-and-Convergence]], [[Settings-and-Campaigns]] |
| Places nest to arbitrary depth; there is no fixed tier count and no enumerated place types | [[Glossary]] |
| Entities are durable across campaigns; facts and visibility belong to one | [[Settings-and-Campaigns]] |

---

## Value, and the cost of omission

**Without this, RC 1a is a demonstration rather than a tool.** Epic 2 retrieves; over an empty store there is nothing to retrieve. Epic 3 checks coverage; over an empty store everything is uncovered. The first slice is meant to be the one that earns its place at the table, and it cannot until the campaign is in it.

Three costs:

**The alternative is retyping.** Months of writing, re-entered by hand, at exactly the moment when enthusiasm for the new tool is what is carrying it.

**An unverifiable conversion is worse than none.** If the GM cannot tell what survived, they will keep consulting the old files as the real record — and then there are two records, diverging, which is the situation the tool exists to end.

**A conversion that guesses wrong about visibility is not recoverable.** A spoiler cannot be un-read.

---

## Stories

### S1 — Bring in what I have already written

*As the GM, I want my existing files to arrive in the tool, so that starting to use it does not mean starting over.*

- **Outcome:** The existing campaign is present and usable without re-entry.
- **Assertion:** Every source file produces a corresponding record. Nothing is skipped silently — anything not converted is reported.
- **Demo:** Convert the fixture's legacy content; the count of sources and the count of outcomes reconcile, with reasons for any difference.

### S2 — Prove nothing was lost

*As the GM, I want to see that the conversion kept everything, rather than being told it did.*

- **Outcome:** The GM can trust the new store without re-reading the old one.
- **Assertion:** The converted store can be written back out as readable text and compared against the source. Differences are reported and each is explained — a change of shape, or a loss.
- **Demo:** Convert, write back out, and show the comparison. Every difference is accounted for.

**This is the central assertion of the epic.** It turns *nothing was lost* from a hope into a test, and it is what makes every other story here checkable.

### S3 — Nothing becomes known to the party by accident

*As the GM, I want everything to arrive private unless the source actually says the party learned it, because the opposite mistake cannot be undone.*

- **Outcome:** No conversion outcome is a spoiler.
- **Assertion:** Visibility defaults to GM-only, and is held per fact and per connection rather than per file — and against the campaign, not globally. A fact is marked known to the party only where the source states it. This holds even where the source file as a whole was marked player-visible.
- **Demo:** Convert a fixture containing a mix. Nothing is marked known to the party without a stated basis, and the basis is shown.

**The campaign scope matters even with one campaign.** Per [[Settings-and-Campaigns]], a single-valued visibility field cannot be split later without guessing which campaign each value belonged to — on the one axis where guessing wrong spoils a campaign silently and unrecoverably.

### S4 — Decide the ambiguous cases myself

*As the GM, I want the conversion to ask me about anything it cannot determine, rather than choosing for me.*

- **Outcome:** Judgment stays with the person who has it, and every judgment made is visible.
- **Assertion:** Where visibility or connection type cannot be determined from the source, the item is raised for a decision — accept, defer, or edit — and is not written until one is made. Decisions are recorded.
- **Demo:** Convert a fixture containing deliberately ambiguous items. Each appears in the queue; none is written before a decision.

### S5 — Run it again after I fix it

*As the GM, I want to convert, look at the result, improve the conversion, and start over, without unpicking anything.*

- **Outcome:** A bad run is discarded rather than repaired.
- **Assertion:** The source is never modified. Conversion runs from scratch each time and produces the same result from the same source and the same decisions.
- **Demo:** Convert twice; outputs are identical. Confirm the source is unchanged after both runs.

### S6 — Turn prose into things I can find

*As the GM, I want what I wrote in paragraphs to become facts I can search, so that details stop being buried in pages.*

- **Outcome:** A detail written in prose is retrievable rather than only readable.
- **Assertion:** Facts extracted from prose carry a source and a visibility. **The original text is retained alongside whatever was extracted from it**, so that imperfect extraction loses nothing.
- **Demo:** Convert a prose section; show both the extracted facts and the original text, and find one of the facts by search.

### S7 — Turn my links into real connections

*As the GM, I want the links I wrote between things to become connections the tool understands, so the thread I drew is one it can follow.*

- **Outcome:** Existing links become part of the connected record rather than being dropped.
- **Assertion:** Every link in the source produces a connection or a queued decision. None is discarded silently. Connections carry a type and a direction.
- **Demo:** Convert content with several links; account for each one as either converted or queued.

### S8 — Bring in sessions captured with the templates, without fuss

*As the GM, I want the sessions I recorded using the current templates to convert cleanly, because I filled them in that way for exactly this reason.*

- **Outcome:** Template-shaped capture requires no interpretation and no queue.
- **Assertion:** A session record following `_templates/CONVENTIONS.md` converts with no ambiguous items raised. Statements made to the party arrive as statements, not as facts about the world.
- **Demo:** Convert a template-shaped session. The queue is empty, and a recorded lie is present as something someone said.

### S9 — Fix what I already know is wrong

*As the GM, I want the errors I have been carrying to be resolved during this rather than copied forward.*

- **Outcome:** Known model errors do not survive into the new store.
- **Assertion:** Content that conflates a quest with an arc, embeds encounters inside a zone document, or carries drifted hand-maintained links is raised for a decision rather than converted as-is.
- **Demo:** Convert a fixture containing one of each; each appears in the queue.

### S10 — Keep my floors and zones as places that contain places

*As the GM, I want the geography to arrive as nested places rather than as fixed tiers, so the shape of the world is not frozen by the file names it happens to have.*

- **Outcome:** `Floor-XX-Name.md` becomes a place containing places, not a special kind of record called a floor.
- **Assertion:** Places carry no tier type. Containment is an ordinary connection and nests to arbitrary depth. Floor and zone survive as names, not as classes.
- **Demo:** Convert the existing floor and zone files; show a place nested three levels deep, and confirm nothing in the store records a fixed tier.

**This is the file-name-to-model gap the README flags.** Converting the convention as-is would bake a two-tier geography into the store on day one, and [[Glossary]] is explicit that a GM wanting *continent → country → city → structure → floor → room* should get it without new vocabulary.

### S11 — Put it in a setting and a campaign, addressed and identified the way they will stay

*As the GM, I want my world and my story to arrive as separate containers at a stable address, so that a second campaign in the same world later is a new record rather than a rebuild.*

- **Outcome:** One setting holding one campaign, with identity and addressing in their final shape.
- **Assertion:** A setting exists and holds the campaign. **Entity identifiers are unique within the setting**, so a later campaign meeting the same NPC meets the same record. Facts, sessions, reveals, and visibility belong to the campaign. The campaign is addressed by path — `storyteller.warpandweft.ink/malvasia` — never by subdomain. **No interface acknowledges that settings exist.** No seeding, no switcher, no accounts, no second campaign.
- **Demo:** Show entities resolving to the setting and facts resolving to the campaign, the campaign reachable at its path, and nothing in the GM's view mentioning a setting.

**Thin structure, not a feature.** Per [[Settings-and-Campaigns]], identity scoped to the setting is what makes inheritance possible at all — a campaign-scoped identifier means a second campaign gets a copied starting position rather than a shared world. Both containers cost almost nothing while there is one of each.

### S12 — Tell me what happened

*As the GM, I want a plain account of what came in, what was queued, and what did not convert, so I know where I stand.*

- **Outcome:** The state of the conversion is knowable without inspecting the store.
- **Assertion:** Each run produces a report of what was converted, what was queued, what was skipped and why, and what decisions were applied.
- **Demo:** Show the report from a run containing all four categories.

---

## Open questions

| Question | What it blocks | Where it sits |
|---|---|---|
| Are the dossiers and the Floor 1 plan hand-converted to template shape first? | The size of this epic, substantially | Recommended in [[Migration]]. Doing it shrinks S6 and S7 to almost nothing |
| At what granularity does prose become facts — one per sentence, one per claim? | S6 acceptance | Needs a stated basis. S6's retention of the original text makes an imperfect answer survivable |
| When is cutover — the point after which the tool is authoritative and the templates are only an import format? | Nothing here; everything after | Choose it rather than arrive at it |
| Does anything need converting a second time, for content written between the first run and cutover? | Planning only | S5's repeatability makes this cheap either way |
| Is the person holding the GM role modelled now, or deferred? | Nothing in RC 1a | [[Strategy-Multi-Campaign-and-Convergence]] wants the role held per campaign rather than baked in as a singleton. With one user it changes nothing visible; the question is only whether it is cheaper here than later |
| Do facts need an explicit in-world time position, separate from the session date? | Nothing in RC 1a | [[Settings-and-Campaigns]]. Session date is sufficient while one campaign exists; it stops being sufficient the moment a second one starts earlier in world time |

---

## Dependencies

- **Epics 2 and 3** need this to be useful. It is not the other way round — this epic stands alone.
- **The templates** are the import contract for S8. Every rule in `_templates/CONVENTIONS.md` exists so that story requires no interpretation.
- **Prerequisite P3** — the fixture corpus must include legacy-shaped content and the deliberately awkward cases, so this epic is testable long before it runs against the live record.
- **S2 requires an export path.** Writing the store back out as readable text is a standing requirement from [[Knowledge-Assets]]; this epic is where it is first needed and first proven.
- **A deployed environment** for S11's address assertion.
