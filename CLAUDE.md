# Working agreement

Rules for Claude working on this repository. Every one exists because the failure it prevents **actually happened**, not because it sounded prudent.

Also paste into the Claude Project instructions — a file in the repo is durable, but only the project instructions are loaded automatically at the start of every conversation.

---

## The premise

The design corpus is now large enough that **drift between documents is a bigger risk than gaps in them.** Claude is a significant source of that drift: it works from context that goes stale within a session, restates definitions because it reads better, and will guess an identifier rather than fetch one.

These rules assume that. They are not about catching Claude's errors afterward — they are about not making them.

---

## Never guess an identifier

**Fetch the blob SHA before every write.** `git rev-parse HEAD:path` locally, or `get_file_contents`. A guessed SHA is how a stale overwrite happens; the API rejected one this session, which was luck rather than design.

Same rule for file paths, epic numbers, and story numbers. If it can be looked up, look it up.

---

## Read the file before rewriting it

Context goes stale inside a single session. Before rewriting a document, confirm the copy being edited matches the branch — compare `git hash-object` against `git rev-parse HEAD:path`.

**Writing from memory of what a document said is the single most likely way to silently drop someone else's edit.**

---

## Cite precisely or not at all

An epic asserted that `Device-Context` required phone-and-one-handed use. It said laptop. The false citation is what let a wrong requirement survive review — it looked sourced.

Before writing *X says Y*, open X and check. If it does not say Y, either fix X or stop claiming it does.

---

## Link, don't restate

> A concept is defined in one document. Everywhere else links to it, and may state implications — never the definition.

Restating makes a document readable standalone, which is exactly why it is tempting and exactly what creates a second copy to drift. `canon` carried three definitions at once before this rule existed.

---

## Search before coining

Before introducing a term, search the corpus for an existing one that means the same thing. *Setting-time* and *fiction time* were invented independently in two documents for one concept.

`grep -ri "term" _design/` is cheap. Naming something that already has a name is expensive.

---

## Give every definition a discriminating example

Include at least one case that reads **differently** under a plausible misreading.

*External author* was intended as external-to-the-campaign and read as external-to-the-people. Both readings agree in nearly every case, so the error was invisible until homebrew separated them. One line — *a homebrew GM's own cosmology is canon* — would have caught it immediately.

This is the cheapest rule here and it catches the class of error no automated check can.

---

## Record superseded reasoning in place

When a decision reverses, **keep the old reasoning and say why it failed.** Do not silently overwrite.

`Canon.md` now holds both earlier definitions and what broke each. That is what stops a resolved question being re-derived six weeks later by someone who only sees the conclusion.

Same for open questions: **strike them with the answer, don't delete them.**

---

## Don't expand scope while writing

A story was given an acceptance bar — *catchable peripherally while glancing at a phone* — for a surface this release is not building. Written in good faith, and it would have been implemented.

If a requirement belongs to a later release or a different surface, **record it as a known future requirement and exclude it from acceptance explicitly.**

---

## Separate proposals from decisions

In summaries and recaps, keep clear which side something came from. A Claude suggestion the GM reacted to positively is **not** a decision. Say *I'd suggested X* rather than *you decided X* unless there is a statement to point at.

Most corrections this session came from the GM. That is the system working, and it only works if the record shows which was which.

---

## Push back

Agreeing reflexively is a failure mode, not politeness. Where a claim looks wrong, say so and explain. Where confidence is low, say that rather than hedging into vagueness.

Several good decisions this session came from a proposal being rejected and replaced with something better. That cannot happen if the proposal was never stated plainly enough to reject.

---

## Prefer the clone to the API for reading

`git clone --depth 1` then grep. GitHub's code search returns **false negatives** on this repo — it reported no match for a file that plainly existed, with `incomplete_results` set.

For anything structural across the corpus, clone and check locally. It is faster, cheaper in context, and correct.

---

## Run the checks

After a working session, not only before a release:

```bash
python3 _tools/check_links.py
python3 _tools/check_staleness.py
python3 _tools/check_definitions.py --min 3
```

See [`_tools/README.md`](_tools/README.md) for what each catches — and for the three failure modes none of them can.

---

## Where things live

- `_design/` — the model, constraints, and strategy. Start at `_design/README.md`.
- `_backlog/` — epics. Written to be readable by a product owner with no TTRPG background.
- `_tools/` — the consistency checks.
- Numbered folders — campaign content. **Not design material**; nothing in `_design/` should link into them, since those paths disappear at migration.
