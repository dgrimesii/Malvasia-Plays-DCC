# Collaboration rules

Rules that hold in **every** context — chat, Claude Code, anywhere else. Every one exists because the failure it prevents actually happened.

Context-specific briefs live elsewhere and both point here:

| Context | Brief | Loaded how |
|---|---|---|
| **Chat** — ideate, plan, document, high-level design | [`PROJECT-INSTRUCTIONS.md`](PROJECT-INSTRUCTIONS.md) | Pasted into the Claude Project instructions |
| **Claude Code** — low-level design, build, test, deploy | [`CLAUDE.md`](CLAUDE.md) | Read automatically from the repo root |

---

## The premise

The design corpus is large enough that **drift between documents is a bigger risk than gaps in them.** Claude is a significant source of that drift: it works from context that goes stale within a session, restates definitions because it reads better, and will guess an identifier rather than fetch one.

These rules assume that. They are not about catching errors afterward — they are about not making them.

---

## Never guess an identifier

**Fetch the blob SHA before every write.** `git rev-parse HEAD:path` locally, or `get_file_contents`. A guessed SHA is how a stale overwrite happens; the API rejected one, which was luck rather than design.

Same for file paths, epic numbers, story numbers. If it can be looked up, look it up.

## Read the file before rewriting it

Context goes stale inside a single session. Before rewriting a document, confirm the copy being edited matches the branch — compare `git hash-object` against `git rev-parse HEAD:path`.

**Writing from memory of what a document said is the most likely way to silently drop someone else's edit.**

## Cite precisely or not at all

An epic asserted that `Device-Context` required phone-and-one-handed use. It said laptop. The false citation is what let a wrong requirement survive review — it looked sourced.

Before writing *X says Y*, open X and check.

## Link, don't restate

> A concept is defined in one document. Everywhere else links to it, and may state implications — never the definition.

Restating makes a document readable standalone, which is why it is tempting and exactly what creates a second copy to drift. `canon` carried three definitions at once before this rule existed.

## Search before coining

Before introducing a term, search for an existing one meaning the same thing. *Setting-time* and *fiction time* were invented independently in two documents for one concept.

`grep -ri "term" _design/` is cheap. Naming something that already has a name is expensive.

## Record superseded reasoning in place

When a decision reverses, **keep the old reasoning and say why it failed.** `Canon.md` holds both earlier definitions and what broke each — that is what stops a resolved question being re-derived six weeks later by someone who only sees the conclusion.

Same for open questions: **strike them with the answer, don't delete them.**

## Separate proposals from decisions

A Claude suggestion the GM reacted to positively is **not** a decision. Say *I'd suggested X* rather than *you decided X* unless there is a statement to point at.

Most corrections come from the GM. That is the system working, and it only works if the record shows which was which.

## Push back

Agreeing reflexively is a failure mode, not politeness. Where a claim looks wrong, say so and explain. Where confidence is low, say that rather than hedging into vagueness.

Good decisions come from proposals being rejected and replaced. That cannot happen if the proposal was never stated plainly enough to reject.

## Run the checks

After a working session, not only before a release:

```bash
python3 _tools/check_links.py          # exits 1 on failure
python3 _tools/check_staleness.py
python3 _tools/check_definitions.py --min 3
```

See [`_tools/README.md`](_tools/README.md) for what each catches — and for the three failure modes none of them can.

---

## Where things live

| Path | What | Who writes it |
|---|---|---|
| `_design/` | Model, constraints, strategy, high-level architecture | Chat context |
| `_backlog/` | Epics, readable by a product owner with no TTRPG background | Chat context |
| `_tools/` | Consistency checks | Either |
| Source tree | Implementation and low-level design | Claude Code |
| Numbered folders | Campaign content — **not design material** | The GM |

**Nothing in `_design/` links into the numbered folders.** Those paths disappear at migration, so a link into them rots by design.

---

## The direction of authority

**`_design/` is upstream of the code.** The model is decided in the chat context and implemented in the build context, never the reverse.

When implementation reveals a problem with the design — and it will — **stop and surface it.** Do not adjust the model to fit the code, and do not implement something that contradicts the corpus on the grounds that the corpus is wrong. It may well be wrong; changing it is a decision made deliberately, with the superseded reasoning recorded, not a side effect of a build session.

This is the sharpest drift risk across the context boundary, and it is silent when it happens.
