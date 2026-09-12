---
type: design
status: draft
visibility: gm
tags: [premise, positioning, scope, psychology, pillars, north-star]
---

# Premise and Pillars

Why this tool should work, stated as a premise with its falsification condition rather than as an argument. Also the correct reason mechanics are out of scope.

Underpins [[North-Star]], [[Live-Set]] and [[Player-Scope]]. Supplies the reasoning behind the mechanics exclusion in [[Scope]].

---

## Mechanics resolve. They don't mean.

The mechanics exclusion in [[Scope]] currently rests on portability — keeping the model system-agnostic. True, but it is the weaker reason. The better one:

> Every system supplies a way to **resolve** what happens. No system supplies what it **means**.

This is the same line in all three pillars, not a per-pillar boundary:

| Pillar | The rules say | The rules cannot say |
|---|---|---|
| **Combat** | who wins | what winning cost, or who remembers |
| **Exploration** | whether you find it | why this place matters |
| **Social** | whether he is persuaded | what he wants, what he is owed, who lied to him last |

Storyteller is the **meaning layer**. It sits beside any resolution system because it never touches resolution — which is a cleaner statement of system-agnosticism than portability was.

### The attitude-track case

Worth naming explicitly, because it is the closest thing to an overlap and someone will reasonably ask whether the tool is redundant.

Some systems have mechanics for NPC or faction attitude toward the party — a track, a reaction roll, a numeric standing. That is genuinely resolution machinery for the social pillar, and it does not overlap.

**The track holds a value. The store holds the accumulated facts that justify it and the history of how it moved.** A GM with the track and no record has a number they cannot explain. A GM with both can say why it moved, and to whom it is owed.

### Combat is a capture source, not an exclusion

The exclusion is on **tactical prep and resolution**, not on the pillar.

A fight produces deaths, grudges, debts, reputation, and the thing somebody said while bleeding. Those are facts and relationships the store must hold. And they are among the most consequential events a campaign generates — a combat whose outcome carries narrative weight is better than one that does not, which is precisely why the record has to reach into it.

**This must be explicit, or the parser gets built to skim exactly the sessions that matter most.**

---

## The premise

Stated plainly, and as a preference rather than a finding:

> **It is more fun to be immersed in a story than to play a sequence of discrete events.**
>
> A combat can be a satisfying tactical challenge on its own. A combat whose success or failure also carries narrative consequence is better.

This is the load-bearing claim under the whole design. The forced-beat mechanism in [[Live-Set]] presupposes it. So does the third GM horn — *narrative possibility foregone* — which costs nothing if there was never a possibility to forego.

### Audience qualification

Not a caveat bolted on. There are real tables where the premise does not hold: episodic dungeon crawling, one-shots, players who want the room and the monster and nothing else.

**Storyteller serves tables that want a story across sessions. A table that wants discrete events has no use for it, and that is fine.** Better to say so than to build for an audience that was never there.

### Falsification condition

Unusually for a product premise, this is testable at the first user's own table. Per [[First-User]], the builder is the GM, and the record is the evidence.

> **A table that never pursues a thread unprompted is a table this tool does not serve.**

Look for: investment observations rising on their own, recurrence, the party returning to people and places without being steered there. If the record shows no continuity-seeking behaviour, the premise is wrong for that table, and the tool should say so rather than accumulating a Live Set nobody spends.

This is better structural challenge than a challenger question, because it is evidence rather than argument. Belongs in [[Verification-and-Challenge]].

---

## Why the premise is a low-risk assumption

The reason to believe it is not that immersion is self-evidently better. It is that the things immersion provides are **known psychological needs**, studied independently of games.

### The source

**Self-determination theory** (Deci and Ryan) is a theory of human motivation generally, not of workplace motivation. It identifies three basic psychological needs whose satisfaction predicts intrinsic motivation and wellbeing: **autonomy, competence, and relatedness.**

**Daniel Pink's *Drive*** (2009) is where this formulation is most widely encountered — popularised for a business audience as **autonomy, mastery, and purpose.**

The ordering matters for the argument. The mechanics are not being inferred backward from workplace findings; the psychology came first, and the workplace application is downstream of it. That makes the step to a tabletop setting short rather than speculative.

**Note for external use:** SDT is a standard lens in games and player-motivation research, so this transfer is closer to a borrowed result than a fresh assumption. The specific citations there should be verified before being used in any customer-facing material — this document does not stand on them.

### The four needs, mapped

| Need | TTRPG translation | What the tool does | Honest status |
|---|---|---|---|
| **Autonomy** | player choice matters and changes the game | makes consequence **visible** — the party can see that what they did stuck | supported indirectly, **and at risk of being undermined** |
| **Competence** | I can reach what I know and act effectively | the memory bank, directly | **the strongest fit** |
| **Relatedness** | four people in a room | protected by staying out of the way | the basis of [[Constraint-Serves-The-Table]] |
| **Purpose** | investment; my actions carry weight in something ongoing | arcs, the [[Live-Set]], the whole continuity layer | supported, and the hardest to evidence |

Four rather than Pink's three, because **relatedness** is the one Pink drops and it is arguably the most relevant of all here. A TTRPG is people in a room. Relatedness is the entire basis of [[Constraint-Serves-The-Table]] — Purpose explains why continuity matters; relatedness explains why the tool must stay out of the way.

### Autonomy is the one the tool can subtract

Competence, relatedness and purpose are things Storyteller can add. **Autonomy is a thing it can take away.**

The moment the tool ranks story options by quality, the GM's choice narrows — and a GM running on rails produces players whose choices do not land. The same holds on the player side: a record that tells them what to care about erodes the thing it was meant to serve.

This is why **options, not recommendations** in [[Live-Set]] and the content rule in [[Constraint-Manner-and-Intent]] are load-bearing commitments rather than fastidiousness. This framework explains what they are protecting.

### Competence versus mastery

Worth separating, because the two words are used interchangeably and they make different claims.

- **Competence** is a **state**: I can act effectively right now.
- **Mastery** is a **trajectory**: I am getting better at something that matters.

**Competence is what the memory bank delivers.** A player who can reach what the party knows acts effectively in the moment — no improvement curve required, no skill acquired. And it is delivered by *removing an obstacle* rather than by developing the person, which is exactly the framing in [[Player-Scope]]: it replaces a notebook that was failing them.

**Mastery as trajectory is not the tool's to give, and should not be claimed.** Getting better at a TTRPG means sharper tactical play, better roleplaying, reading the table, knowing the system. That is the person improving, through play. A tool that claimed to develop competence would be a tool you *practise with* — and practising with it is time not spent with the people.

**One legitimate exception, GM-side.** A GM's prep judgment genuinely does improve, and the record is the mechanism: the coverage report, the accumulated history of which inferences were accepted and rejected, the investment history over time. Those are feedback on the GM's own past choices, which is how mastery actually develops. A real GM-side benefit with no player analogue — it belongs alongside the three GM-only horns in [[Live-Set]].

---

## How to use this document

It records **why the tool should work**, so the reasoning does not have to be reconstructed each time a feature is argued about.

It is not customer-facing material as written. The customer-facing articulations live in [[Player-Scope]] (the three horns) and [[Live-Set]] (the GM's six). This is the layer underneath them.

And it is a premise, not a proof. It is written so that it can be found wrong.

---

## Open

1. **Does the record make consequence visible enough to serve autonomy**, or is that claim doing no work? Consequence being *recorded* is not the same as the party *perceiving* it — and the player surface is read-only and answer-shaped by design.
2. **Is *narrative possibility foregone* measurable retrospectively?** Carried over from [[Live-Set]] §Open. It is the largest claimed GM cost and has no symptom.
3. **Games-research citations for SDT** — worth finding and verifying if any of this goes into external material.
