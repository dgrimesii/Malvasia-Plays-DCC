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

**Entitlements attach to roles. Grants attach to a scope.**

- A **role** carries a standard set of entitlements — the same everywhere. There is one definition of what a GM can do.
- A **grant** gives a person a role at a scope. Almost every grant is scoped to a single campaign, and confers that role's entitlements there and nowhere else.

```
Role   --has-->            Entitlements     (defined once, global)
Person --granted(Role)-->  Scope            (campaign, or system)
```

Being a GM in one campaign confers nothing in any other.

---

## Why this is the right shape

**No per-person permissions.** The unit is the role, so there is no drift into a hundred individually-adjusted people. Adjusting what a role can do is one edit, not a migration.

**Scope travels with the grant.** Entitlement cannot leak across campaigns, because there is no entitlement that is not attached to a scope.

**Deny by default.** No grant means no access. Nothing is implied by owning the host, being a GM elsewhere, or having been a member previously.

---

## It preserves the orthogonality

[[Multi-Campaign-Hosting]] insists that entitlement and knowledge domain stay separate. This model keeps them separate by making **both properties of the role**, rather than one field doing two jobs:

| Role | Knowledge domain | Entitlements |
|---|---|---|
| **GM** | `gm` | Everything within the campaign — capture, author, reveal, grant roles |
| **Player** | `player` | Read the revealed record, write attributed notes |
| **Scribe** | `player` | Read the revealed record, write the shared play record |
| **Observer** | `player` | Read only |
| **System administrator** | — | See below |

**Player and Scribe share a knowledge domain and differ in entitlements.** That pair is the proof the two axes are genuinely independent — and it is not hypothetical, since it is exactly the Chronicle arrangement described in [[Shared-Core]].

Knowledge domain does not combine the way entitlements do. `gm` strictly contains `player`; there is no partial GM.

---

## Multiple roles in one campaign

**Allowed, with entitlements unioned.** A player who also keeps the record holds both grants rather than requiring a compound role. This avoids the combinatorial role set that otherwise appears the moment a second modifier exists.

Knowledge domain takes the **highest held**, not the union.

**Two consequences of unioning:**

- **Revocation shrinks access rather than removing it.** Revoke GM from someone who also holds player, and they drop to player rather than losing the campaign. A GM stepping back to play is a real situation, and this is the intended behaviour.
- **"What can this person do" is computed, not stored.** Which sharpens the audit requirement: recording that a grant exists is not enough. The answer to *why can they see this* must name **which grant** conferred it, since with two grants the answer is otherwise ambiguous.

---

## The system administrator

**A grant at system scope, not a role that bypasses scoping.**

This matters more than it sounds. An administrator implemented as *skip the check if admin* puts a branch in every access decision, and a branch in every decision is a branch that will be wrong somewhere. An administrator implemented as a grant at a scope **above** campaign changes nothing about how checks work — it is one more row in the grant table, and every query remains scoped.

**The guarantee weakens honestly.** Cross-campaign access is no longer inexpressible; it is expressible by exactly one grant, which is visible, revocable, and auditable. That is the right trade, and it is better than the alternative where the host has the same power implicitly and nothing records it.

### Split the administrator's entitlements

Two capabilities that are usually conflated and should not be:

| Entitlement | Needed | What it allows |
|---|---|---|
| `administer_any_campaign` | Routinely | Grants, membership, campaign lifecycle, repair |
| `read_any_campaign_content` | Rarely | The actual contents — another GM's secrets, twists, plans |

**Almost every administrative task needs the first and not the second.** Splitting them means the administrator can do the job without reading anyone's campaign, and makes the moment they do read one a distinct, recorded act rather than an ambient condition.

This is the formal answer to the trust problem raised in [[Multi-Campaign-Hosting]] — the host can read every campaign's secrets. It cannot be eliminated, but it can be made explicit, narrow, and visible.

### Administrator actions are audited harder

An administrator acts outside the social check that makes ordinary grants safe — a GM granting within their own campaign is visible to that group. Nothing else constrains an administrator, so **the record of what they did is the only accountability that exists.**

---

## Granting

**Within a campaign, the GM grants roles.** `grant_roles` is an entitlement of the GM role, scoped like any other.

**Across campaigns, only the system administrator grants.**

---

## The last GM invariant

**Every campaign has at least one person holding a GM grant, at all times.**

Stated as an invariant rather than as a rule about self-removal, because self-removal is only one of three ways to orphan a campaign:

- A GM revokes their own GM grant
- A GM revokes another GM's grant, and that was the last one
- A person holding the last GM grant is deleted or deactivated

Enforcing only the first leaves the other two open, and both produce the same unreachable campaign.

**Grant before revoke.** To replace a GM, the incoming grant is made first and the outgoing one revoked after. This means the invariant is never violated, not even transiently, and needs no exception for handover.

**Repair, not exception.** If a campaign somehow has no GM — an unforeseen path, a data error, an account removed outside the normal flow — the administrator's power is to *grant* a GM, which satisfies the invariant rather than overriding it. The invariant itself holds absolutely.

**Bus factor.** With exactly one administrator, losing that account means nothing can be repaired anywhere. Either more than one administrator exists, or there is a documented recovery path. Worth deciding before it matters rather than after.

---

## Entitlements name capabilities, not screens

`reveal`, `capture_session`, `author_entity`, `read_gm_content`, `write_attributed_note`, `export_campaign`, `grant_roles`, `administer_any_campaign`, `read_any_campaign_content`.

Named after what a person can do, they survive every interface change. Named after screens or buttons, they rot on contact with the first redesign — and worse, they stop describing anything checkable.

---

## Enforcement

**At the store boundary, not in the interface.** The same rule as campaign scope and as player-facing computation in [[Visibility-Model]]: filtering the presentation of an unfiltered result is how leaks happen.

An entitlement check performed by a view is a check that a second view will forget.

---

## What this makes testable

Concrete assertions for the fixture corpus in [[Verification-and-Challenge]]. All of them can fail, which is the point.

- A person holding GM in campaign A and player in campaign B sees no GM content in B.
- A person with no grant in a campaign cannot determine that the campaign exists.
- Two roles held in one campaign produce the union of their entitlements and the higher of their knowledge domains.
- Revoking one of two grants leaves the other intact and lowers the knowledge domain accordingly.
- Revoking a grant removes access without removing that person's attributed contributions.
- Revoking the last GM grant fails, as does deleting the person who holds it.
- A Scribe can write the play record and cannot read GM content.
- Administrator access is satisfied by a system-scoped grant, with no bypass branch in any check.
- `administer_any_campaign` alone does not permit reading campaign content.
- Every access decision names the grant that conferred it.
- No entitlement check is satisfied by a request lacking a scope.

**The first two belong in the adversarial fixture set specifically** — a person with grants in two campaigns is the case where a missing scope filter shows up, and it will never occur naturally in a single-campaign store.

---

## What Release 1 builds

The **shape**, with one campaign, one person, and one grant. Not the machinery.

- Roles exist and carry entitlement sets.
- Grants exist and carry a scope.
- Checks happen at the store boundary and name the conferring grant.
- The last GM invariant holds.
- Nothing is implied without a grant.

No signup, no invitations, no role management interface, no administrator console, no billing. Per [[First-User]] there is one user, and per [[Hosting-Implications]] the only access requirement once hosted is that the record is not publicly readable.

**Modelling this now costs almost nothing. Retrofitting a permission model onto a knowledge model is the expensive version**, and it is the version that ships spoilers.
