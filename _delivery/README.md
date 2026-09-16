---
type: delivery
status: draft
visibility: gm
tags: [delivery, readiness, environments, process]
---

# Delivery

How **this** build of Storyteller gets made, hosted, tested, and shipped.

Written in the chat context, read by the build context. Not campaign content and not part of the game record.

---

## Why this is not `_design/`

`_design/` is deliberately system- and campaign-agnostic. Someone else could build Storyteller from it without knowing what a Malvasia is or who registered the domain.

Nothing here has that property. It names a registrar, a hosting platform, three environments, and one person's working rhythm. Folding it into `_design/` would break the portability the model is built for — the same rule `CLAUDE.md` applies to schema detail, applied one level up.

**The test:** if the answer would change because someone else built this, on different infrastructure, it belongs here.

---

## What lives where

| Directory | What | Who writes it |
|---|---|---|
| `_design/` | The model, constraints, strategy, high-level architecture | Chat context |
| `_backlog/` | Epics and stories | Chat context |
| **`_delivery/`** | **Environments, hosting, test strategy, issue conventions** | **Chat context** |
| `_feedback/` | Findings raised while building | Filed by Claude Code, closed by the GM |
| Source tree | Implementation, schema, ADRs | Claude Code |

The boundary with the source tree is the same one `CLAUDE.md` already draws. **Platform is decided here; framework is an ADR there.** Which database engine and which host are infrastructure commitments that outlive any rewrite. Which web framework, which ORM, and which test runner are not.

---

## The documents

- **[[Readiness-Checklist]]** — the ordered path to the first issue. Start here.
- **[[Environments]]** — the three environments, what data each holds, and the rules that keep them apart.
- **[[Hosting]]** — the constraints the platform must satisfy, and the platform chosen against them.
- **[[Render-Setup]]** — the hand steps that make Render ready for the first deployment.
- **[[Test-Strategy]]** — the four prerequisites made concrete, and the role separation that makes single-agent testing worth anything.
- **[[Issue-Conventions]]** — what a GitHub issue contains, how stories map onto issues, and the definition of ready.
- **[[Issue-Lifecycle]]** — how an issue moves from written to closed: states, the five phases, the plan gate, and the labels.
- **[[Backup-and-Durability]]** — the requirement left without an owner when the repo stopped being an export target.

---

## Status

Written before any code exists. Everything here is a **proposal until the GM accepts it**, per `COLLABORATION.md` — a positive reaction is not a decision. Accepted items are marked settled in their own documents.

The rules in `COLLABORATION.md` apply here unchanged: link rather than restate, search before coining, record superseded reasoning in place, strike resolved questions with the answer.
