---
type: design
status: draft
visibility: gm
tags: [strategy, multi-campaign, hosting, entitlements, access]
---

# Multi-Campaign Hosting

What hosting several campaigns, each with its own access and data, actually requires. Extends [[Strategy-Multi-Campaign-and-Convergence]] and [[Hosting-Implications]].

---

## First: decide which product this is

*"Eventually multiple campaigns"* covers four situations whose costs differ by an order of magnitude. Deciding which one is being built for is the first consideration, because building for the fourth while living in the first is the expensive mistake available here.

| Stage | Who | What it adds |
|---|---|---|
| **0** | One GM, one campaign | Nothing. Current plan. |
| **1** | One GM, several campaigns | Campaign scoping. No access control — the same person owns all of them. |
| **2** | A GM and their players | First real entitlement: membership and role. Release 2. |
| **3** | Other groups the owner knows | Invitation, isolation between groups, someone else's secrets on the owner's host. |
| **4** | Strangers | Signup, payment, support, data deletion requests, privacy obligations, liability. **A different product.** |

Stages 0 to 2 are the current roadmap. Stage 3 is a modest step from stage 2. **Stage 4 is a business, not a feature**, and nothing before it should be built as though it is coming.

---

## The distinction that matters most

**Entitlement and knowledge domain are orthogonal.** Collapsing them is the single most consequential modelling error available in this area.

| | Question | Values |
|---|---|---|
| **Entitlement** | Can this person reach this campaign at all, and do what? | member / not · read / write |
| **Knowledge domain** | Within the campaign's fiction, what are they allowed to know? | `gm` / `player` — per [[Visibility-Model]] |

They come apart immediately in practice:

- A **co-GM** has GM-level knowledge and full write access.
- A **scribe** — the Chronicle role — has player-level knowledge and heavy write access.
- A **player on hiatus** has player-level knowledge and read-only access.
- A **guest at one session** may need player-level knowledge and no persistent access at all.

If knowledge domain is used as the permission model, none of these can be expressed. If entitlement is used as the visibility model, the three-gate structure in [[Visibility-Model]] collapses and spoilers follow.

**Keep them as two separate attributes of a person's membership in a campaign.**

---

## Data separation

Two shapes, with a real trade-off.

**Soft isolation** — one store, everything carrying a campaign scope. Cross-campaign features become possible; every query must filter correctly, and one missed filter leaks another group's campaign.

**Hard isolation** — a separate store per campaign. Leakage becomes structurally difficult rather than a matter of discipline; cross-campaign features become expensive.

**Hard isolation is the better fit**, for reasons already settled elsewhere: cross-campaign search and content reuse are explicitly deferred in [[Strategy-Multi-Campaign-and-Convergence]], identifiers are already unique within a campaign rather than globally, and export is required per campaign anyway under [[Knowledge-Assets]].

Whichever shape, one rule matters more than the choice: **scope should be structural, not remembered.** A query that can be written without a campaign scope will eventually be written without one, at three in the morning, and nothing will look wrong.

---

## The leak surface doubles

[[Visibility-Model]] establishes that every player-facing computation runs over the filtered store, never over the full store with a filter applied to the output — because counts, identifiers, layout, and empty results all leak the shape of what is hidden.

**Multi-campaign adds a second filter with exactly the same failure mode**, and the two compose. A search must be scoped by campaign *and* by knowledge domain. A count must be computed over both filters. An identifier must not reveal the existence of records outside either.

Every leak class in that document reappears at campaign scope. The mitigation is the same, applied twice.

---

## Identity across campaigns

The same person holds different roles in different campaigns — already established in [[Strategy-Multi-Campaign-and-Convergence]], and the reason "the GM" cannot be a singleton.

Hosting adds a second identity concept that must not be merged with the first:

- **Account** — who signed in. One per person, across all campaigns.
- **Attribution** — whose contribution a piece of content is. A name on a note, per [[Players-and-Characters]].

Attribution is campaign-local and human-readable. An account is global and technical. Using one as the other means a person cannot appear in two campaigns, or cannot be renamed, or cannot have their notes survive an account change.

---

## Other people's secrets

The consideration most likely to be overlooked, and it is not technical.

At stage 3 or beyond, **the host can read every campaign's secrets** — plot twists, betrayals, everything the GM has planned and not revealed. That is the most sensitive content this product will ever hold, and the position is one of trust rather than permission.

Related questions that need answers before anyone else's campaign lives on the host, not after:

- Whose data is it, and can they take it with them? Portability now serves someone else's interests, not just the owner's.
- What happens if the host shuts down, loses interest, or the bill goes unpaid?
- Can a player have their own contributions removed? [[Players-and-Characters]] makes notes attributed and shared, which makes removal a question about the shared record rather than a private one.
- What is the backup obligation to someone else's years of work?

These are answerable cheaply and awkward to answer late.

---

## Stage 4 obligations, listed once

Not to be designed for now — recorded so the step is taken deliberately if it is ever taken.

Signup and account recovery · payment, refunds, and tax · privacy policy and data deletion requests · minors at the table, since tabletop groups routinely include them · content moderation and liability for what strangers store · support expectations · incident handling and disclosure.

Each is small. Together they are the difference between a tool and a service.

---

## What to do now

Nothing new for Release 1. Everything below is already committed for other reasons, and multi-campaign hosting is a second argument for each.

| Already committed | Also serves |
|---|---|
| Campaign container, carrying configuration | Scoping, per-campaign settings |
| Identifiers unique within a campaign, non-sequential | Isolation, leak resistance |
| Person holds a role per campaign | Cross-campaign identity |
| Record-keeping as an attribute separate from role | The scribe case |
| Visibility as a property of facts and edges | Knowledge domain, kept separate from entitlement |
| Portability and per-campaign export | Ownership, exit, backup obligations |
| Minimum access boundary once hosted | The first entitlement |

**Two additions worth making now, both cheap:**

1. **Model entitlement as a distinct attribute of membership** from the start, even with one member and one value. Retrofitting a permission model onto a knowledge model is the expensive version of this.
2. **Make campaign scope structural.** Whatever the storage shape, an unscoped query should be difficult to express rather than merely discouraged.

**And one thing not to do:** no signup, no accounts, no billing, no roles beyond what stage 2 needs. Stage 4 arriving early is how a working tool becomes an unfinished service.
