---
type: design
status: draft
visibility: gm
tags: [model, entitlements, access, multi-campaign]
---

# Entitlement Model

Decided. Refines the considerations in [[Multi-Campaign-Hosting]].

---

## Settled

**Entitlements attach to roles. Grants attach to campaigns.**

- A **role** carries a standard set of entitlements — the same everywhere. There is one definition of what a GM can do.
- A **grant** gives a person a role **in one campaign**. It confers that role's entitlements for that campaign and nowhere else.

```
Role  --has-->  Entitlements        (defined once, global)
Person --granted(Role)--> Campaign  (scoped, per campaign)
```

Being a GM in one campaign confers nothing in any other.

---

## Why this is the right shape

**No per-person permissions.** The unit is the role, so there is no drift into a hundred individually-adjusted people. Adjusting what a role can do is one edit, not a migration.

**Scope travels with the grant.** Entitlement cannot leak across campaigns, because there is no entitlement that is not attached to a campaign. This is the structural version of the rule in [[Multi-Campaign-Hosting]] — cross-campaign access is not merely prevented, it is inexpressible.

**Deny by default.** No grant means no access. Nothing is implied by owning the host, being a GM elsewhere, or having been a member previously.

---

## It preserves the orthogonality

[[Multi-Campaign-Hosting]] insists that entitlement and knowledge domain stay separate. This model keeps them separate by making **both properties of the role**, rather than one field doing two jobs:

| Role | Knowledge domain | Entitlements |
|---|---|---|
| **GM** | `gm` | Everything — capture, author, reveal, grant |
| **Player** | `player` | Read the revealed record, write attributed notes |
| **Scribe** | `player` | Read the revealed record, write the shared play record |
| **Observer** | `player` | Read only |

**Player and Scribe share a knowledge domain and differ in entitlements.** That pair is the proof the two axes are genuinely independent — and it is not hypothetical, since it is exactly the Chronicle arrangement described in [[Shared-Core]].

Knowledge domain does not combine across roles the way entitlements do. `gm` strictly contains `player`; there is no partial GM. A person holding any GM grant in a campaign sees all of it.

---

## Multiple roles in one campaign

**Allowed, with entitlements unioned.** A player who also keeps the record holds both grants rather than requiring a compound role.

This avoids the combinatorial role set that otherwise appears the moment a second modifier exists, and it fits what [[Strategy-Multi-Campaign-and-Convergence]] already established — that record-keeping is an attribute separate from role, because the same person can be a player who keeps the record in one campaign and a GM who keeps it in another.

Knowledge domain takes the highest held, not the union.

---

## Entitlements name capabilities, not screens

`reveal`, `capture_session`, `author_entity`, `read_gm_content`, `write_attributed_note`, `export_campaign`, `grant_roles`.

Named after what a person can do, they survive every interface change. Named after screens or buttons, they rot on contact with the first redesign — and worse, they stop describing anything checkable.

---

## Granting

**`grant_roles` is an entitlement within the GM role.** No separate owner concept for now.

This is correct through stage 3 in [[Multi-Campaign-Hosting]] — groups of people who know each other, where a GM adding a co-GM is a social act rather than a security event.

**It stops being correct at stage 4.** With strangers, an owner distinct from the GM role is needed, because otherwise any GM can grant GM to anyone and there is nothing that cannot be given away. Recorded here so the gap is known rather than discovered.

---

## Two consequences worth knowing

**Changing a role changes it everywhere, immediately.** Adding an entitlement to the GM role grants it to every GM in every campaign at once. Usually the intent — but it is a blast radius, and it is the reason role definitions should be small and stable rather than a place to solve one campaign's problem.

**The grant is the audit unit.** Recording who granted what, to whom, when, is nearly free and is the only thing that answers *why can this person see this*. Worth having from the first grant rather than added after the first surprise.

---

## Enforcement

**At the store boundary, not in the interface.** The same rule as campaign scope and as player-facing computation in [[Visibility-Model]]: filtering the presentation of an unfiltered result is how leaks happen.

An entitlement check performed by a view is a check that a second view will forget.

---

## What this makes testable

Concrete assertions for the fixture corpus in [[Verification-and-Challenge]]. All of them can fail, which is the point.

- A person holding GM in campaign A and player in campaign B sees no GM content in B.
- A person with no grant in a campaign cannot determine that the campaign exists.
- Revoking a grant removes access without removing that person's attributed contributions.
- A Scribe can write the play record and cannot read GM content.
- Two roles held in one campaign produce the union of their entitlements and the higher of their knowledge domains.
- No entitlement check is satisfied by a request lacking a campaign scope.

**The first two belong in the adversarial fixture set specifically** — a person with grants in two campaigns is the case where a missing scope filter shows up, and it is a case that will never occur naturally in a single-campaign store.

---

## What Release 1 builds

The **shape**, with one campaign, one person, and one grant. Not the machinery.

- Roles exist and carry entitlement sets.
- Grants exist and carry a campaign.
- Checks happen at the store boundary.
- Nothing is implied without a grant.

No signup, no invitations, no role management interface, no billing. Per [[First-User]] there is one user, and per [[Hosting-Implications]] the only access requirement once hosted is that the record is not publicly readable.

**Modelling this now costs almost nothing. Retrofitting a permission model onto a knowledge model is the expensive version**, and it is the version that ships spoilers.
