---
type: design
status: draft
visibility: gm
tags: [access, entitlements, operations, recovery]
---

# Access Recovery

The break-glass path when entitlements reach a state the running application cannot fix. Extends [[Entitlement-Model]].

**Standing assumption:** one person is both the repository owner and the application administrator. Recorded here because the design below depends on it, and because it will eventually stop being true.

---

## Settled

**Recovery is by deployment.** A declarative bootstrap in the repository names grants that must exist; deploying applies them.

Roles are otherwise managed entirely through the website. The repository path is break-glass, not an administration surface.

---

## Why this is legitimate rather than a hole

**Deploy access already dominates every entitlement.** Whoever can change the code can grant themselves anything, with or without a designed path. That is true of every system and pretending otherwise is theatre.

So this adds no privilege. It makes an existing privilege **usable deliberately, in daylight, rather than improvised at two in the morning** against a locked-out account — which is the version that produces a permanent hack left in the code.

It also answers the bus-factor question left open in [[Entitlement-Model]]: the recovery path is the repository, and it exists without building an administrator console.

---

## Four rules that keep it safe

### 1. It seeds data; it never bypasses a check

The failure mode to avoid is a condition in the running application — *if this identifier matches the emergency admin, skip the check*. That is a permanent bypass branch, and it is exactly what [[Entitlement-Model]] avoids by expressing the administrator as a system-scoped grant rather than an exception.

**The bootstrap writes an ordinary grant into the store and then has no further role.** At request time nothing consults it. A grant created this way is structurally indistinguishable from one created on the website.

### 2. Additive floor, never a mirror

The file states grants that **must exist**. It does not state the complete set.

If deployment reconciled the store to the file, every deploy would silently delete grants made through the website. The file is a floor, and the website remains authoritative for everything above it.

### 3. Identifiers, not credentials

The bootstrap names a person and a role. It contains no secret, and it does not authenticate anyone — the named person still signs in normally.

This keeps the file boring, which is what makes it safe to sit in a repository.

### 4. Grants carry their provenance

A grant created by deployment records that origin, rather than being attributed to a person who took no action. [[Entitlement-Model]] requires every access decision to name the grant that conferred it; this keeps that answer truthful.

---

## What it repairs

- The administrator account is lost, and nothing can be granted.
- A campaign has no GM through some path the invariant did not cover.
- The entitlement data is damaged and access is wrong or absent.
- A change to role definitions locks everyone out of something.

---

## A signal worth watching

**If the bootstrap file starts being edited routinely, the website is missing something.** The file working well looks like it being untouched for months.

Routine use is a symptom, not a success, and the fix is in the interface rather than in the file.

---

## What this makes testable

- Running the bootstrap twice changes nothing the second time.
- A grant made through the website survives a deployment.
- Grants created by bootstrap are structurally identical to grants created on the website.
- No request-time code path consults the bootstrap configuration.
- A bootstrap grant records deployment as its origin.
- With the entitlement store emptied, deployment restores administrator access and nothing else.

That last one is the actual drill, and it is worth running against a fixture rather than assuming.

---

## When this stops being sufficient

Two conditions, both foreseeable.

**A second administrator exists.** The single point of recovery becomes the repository owner's account rather than the application's — worth knowing, since it means account recovery for one external service is the real dependency underneath all of this.

**Other people's campaigns are hosted** — stage 3 in [[Multi-Campaign-Hosting]]. At that point another GM's campaign is recoverable by someone editing a repository they cannot see, on a schedule they do not control. That is a trust question rather than a technical one, and it needs answering before the first outside campaign arrives rather than after.

---

## Release 1

Nothing to build. One person holds every role, and there is nothing to recover from.

**Worth writing the bootstrap file when the first grant exists**, so that the path is proven while it is trivial rather than discovered when it is not.
