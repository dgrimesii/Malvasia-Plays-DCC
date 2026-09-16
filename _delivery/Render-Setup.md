---
type: delivery
status: draft
visibility: gm
tags: [delivery, hosting, render, setup, runbook]
---

# Render Setup

The steps the GM takes by hand to make Render ready for the first deployment. Platform choice and reasoning live in [[Hosting]]; this is only the runbook.

**What this does not do:** create the web services or the databases. Those are created by the walking-skeleton issue in [[Issue-Conventions]], because a database bills from the moment it exists and there is nothing to run on it yet. Part 6 records the settings that issue must use, so they are decided once, here.

Render's interface changes. Where a label below does not match the dashboard, the intent of the step is what matters — note the new label here when it happens.

---

## Before you start — ~~one blocking decision~~ settled

**The code lives in `Malvasia-Plays-DCC`, under `app/`.** Settled by the GM; see [[Hosting]] §Open questions 5. Render deploys from this repository with its Root Directory set to `app/`, which keeps the campaign folders out of every deployment.

~~**Where the application code lives.** See [[Hosting]] §Open questions. Render copies whatever repository a service is connected to. If that is `Malvasia-Plays-DCC`, the test deployment holds the campaign folders, including the GM notes — which breaks rule 2 in [[Environments]]: the campaign source is not fetchable from test.~~ *Superseded: the Root Directory setting means Render does not carry the whole repository.*

~~Parts 1–3 and 5 do not depend on the answer. **Part 4 does. Do not connect GitHub until this is decided.**~~ All parts can proceed.

---

## Part 1 — Account

1. **Turn on two-factor authentication.** Account Settings → Account Security → two-factor authentication.
   *Why:* this login reaches both environments and can read every secret. Rule 1 in [[Environments]] holds only while this login is protected — it is the one credential that spans test and production.
2. **Store the recovery codes** somewhere that is not this computer alone.
3. **Stay on the Hobby workspace plan for now.** It allows one member, two environments per project, and two custom domains — exactly test and production.
4. **Upgrade to Pro before cutover.** Pro is a flat monthly fee and raises the point-in-time restore window from 3 days to 7. Before cutover production holds nothing irreplaceable; after it, 3 days is thin. See [[Backup-and-Durability]].

---

## Part 2 — Project and environments

1. **Create a project named `Storyteller`.**
2. **Create two environments in it: `Test` and `Production`.**
3. **On both environments, turn on blocking of private network traffic.** Services inside an environment still reach each other; neither environment can reach the other over Render's private network. This is a second wall behind rule 1 — the first is still that test holds no production credential.
4. **Mark `Production` as protected.** It does nothing while you are the only member, and costs nothing. It matters the day someone else joins the workspace.

---

## Part 3 — Environment groups (secrets)

One group per environment, each scoped so the other environment cannot link it.

1. Environment Groups → **New Environment Group** → name it `storyteller-test`.
2. Add the variables that exist today. At minimum a placeholder for the model API key required by C8 in [[Hosting]]. **Use a separate API key for test** — never the production key.
3. On the group's page: **Manage → Move group** → project `Storyteller`, environment `Test`.
4. Repeat for `storyteller-production`, scoped to `Production`, holding the production key.

**Do not put a database connection string in either group by hand.** The database is created in the walking-skeleton issue, and its internal URL is attached to the service in the same environment then.

**Check after:** open `storyteller-test` and confirm it cannot be linked to anything in `Production`.

---

## Part 4 — GitHub

1. Account Settings → Account Security → Git Deployment Credentials → **Add credential → GitHub**.
2. On GitHub, when installing the Render app, choose **Only select repositories** and pick **only `Malvasia-Plays-DCC`**.
3. ~~**Never grant access to `Malvasia-Plays-DCC`** unless it has been decided that code lives there and the campaign content has been moved out first.~~ *Superseded: code lives there, and Part 6's Root Directory keeps the campaign folders out of the deployment.* Do not grant access to any other repository.
4. To change this later: `github.com/apps/render/installations/new` → Repository access.

---

## Part 5 — Cloudflare preparation

Nothing points anywhere yet. This makes the later step a two-minute one.

1. **SSL/TLS → Overview → set encryption mode to Full.** Nothing is live on the zone, so there is nothing to disturb.
2. **Confirm there are no `AAAA` records** for `test` or `storyteller`. Render does not support IPv6, and a stray one breaks certificate issuance.
3. **Leave `demo`, `fixture`, and `chronicle` unpointed**, per [[Environments]].

When the walking-skeleton issue creates the two web services, it adds:

| Name | Type | Target | Proxy |
|---|---|---|---|
| `test` | CNAME | the test service's `onrender.com` hostname | **DNS only** (grey) |
| `storyteller` | CNAME | the production service's `onrender.com` hostname | **DNS only** (grey) |

Add each as a custom domain on its service, wait for the certificate to verify, and only then consider switching the proxy on. Leaving it off is also fine.

---

## Part 6 — Settings for the walking-skeleton issue

Recorded here so the build context does not choose them. **Test and production are identical except for the rows marked otherwise** — [[Environments]] requires test to be production-class.

### Both environments

| Setting | Value | Why |
|---|---|---|
| Repository | `Malvasia-Plays-DCC`, branch `main` | Settled — see Before you start |
| Root Directory | **`app`** | Files outside it are unavailable at build and run time, so no campaign folder reaches a deployment |
| Build filters | Include **`app/**`** | A commit touching only campaign notes or the corpus does not redeploy |
| Region | **Virginia (US East)** | Closest to the table. Every service and database in the same region, or the internal URL cannot be used |
| Postgres major version | **One version, pinned**, the same in both and in the local dev container | [[Environments]] — same engine, same version |
| Postgres plan | **The $19 tier (0.5 CPU, 1 GB)** — the same in both | Production-class test. Not the free plan for either |
| Postgres storage | 1 GB to start | Can grow; the record is small |
| Database name and user | Chosen deliberately | **Cannot be changed after creation** |
| External database access | **Disabled** — clear the IP allow list | The default allows any address with valid credentials. Open it to one address, briefly, only when a task needs it |
| Web service plan | **The $7 tier (0.5 CPU, 512 MB)** | Revisit if memory runs short |
| Pre-deploy command | Runs the migrations | [[Hosting]] — migrations are a discrete step, never a side effect of start |
| Environment group | The one scoped to that environment | Part 3 |
| Database connection | The **internal** URL of the database in the same environment | Faster, and never leaves Render |

### Where they differ

| Setting | Test | Production |
|---|---|---|
| Auto-deploy | **After CI checks pass** — on commit until CI exists | **Off** |
| How a deploy happens | Merge to the linked branch | A deliberate manual deploy of a commit already verified on test |
| Access boundary | None — a reviewer is handed the URL | C11 in [[Hosting]] |
| Storage autoscaling | Off | **On** |
| Suspended when idle | Yes — Part 7 | Never |
| Conversion job | **Never deployed here** — rule 2 | Production only |

---

## Part 7 — Stopping and starting test

**To stop:** suspend the test web service, then the test database.
**To start:** resume the database first, then the web service.

Rules from [[Environments]] §Test is not always running:

- **Start test before any promotion.** A stopped test environment is never a reason to deploy production directly.
- **Start test before sending a review link**, and say how long it will be up.
- **Measure latency only after test has settled**, not straight after resuming.

**Verify the saving once.** After suspending test for the first time, watch the unbilled-usage figure on the billing page for a day. If it keeps rising for the suspended database, record that here and revisit [[Hosting]] — the whole reason test is stoppable is cost.

---

## Ready for first deployment

- [ ] Two-factor authentication on, recovery codes stored
- [ ] Project `Storyteller` with `Test` and `Production`
- [ ] Private network traffic blocked on both; `Production` protected
- [ ] `storyteller-test` and `storyteller-production` environment groups, scoped, with separate model API keys
- [x] Code-repo decision made and recorded in [[Hosting]] — this repository, under `app/`
- [ ] GitHub connected with access to `Malvasia-Plays-DCC` only
- [ ] Cloudflare SSL mode Full; no `AAAA` records on `test` or `storyteller`
- [ ] Walking-skeleton issue written with Part 6 as its settings

When every box is ticked, the walking-skeleton issue can be handed to Claude Code.

---

## Open

1. **How does anything reach the production database from outside Render?** The conversion job and the restore drill may both need it. The conversion job cannot read the campaign folders from inside a deployment either, because of the Root Directory — so it reads them from GitHub, or runs from the development machine. With external access disabled, the options are opening the allow list briefly to one address, or running the task inside Render. Tied to [[Hosting]] §Open questions 1.
2. **Does a suspended database stop billing?** Render confirms suspended services are billed only up to suspension; nothing found states it for databases. Part 7 settles it empirically.
