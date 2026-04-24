# Product Overview

This repository is the **full email marketing stack** for Step (nspace). It spans three layers that work together end-to-end:

```
┌───────────────────────────────────────────────────────────────────┐
│  1. CONTENT          campaigns/   — HTML templates, assets, copy  │
│  2. RENDER & SEND    *.py         — Python pipeline (SES + R2)    │
│  3. BACKEND API      src/         — Cloudflare Workers + Postgres │
└───────────────────────────────────────────────────────────────────┘
```

Every email sent by the team flows through all three: drafted in `campaigns/`, rendered + sent by the Python pipeline, tracked by the Workers API.

---

## 1. Backend API (Cloudflare Workers)

A Hono-based API running on Cloudflare Workers, backed by PostgreSQL via Hyperdrive. Handles everything that needs to be queryable or persistent.

Features:
- **Email list management** — create, update, delete mailing lists
- **Subscriber management** — add/remove subscribers per list, with duplicate and opt-out enforcement, bulk insert endpoint
- **Campaign management** — create, schedule, and track email campaigns with HTML and plain-text bodies
- **Send tracking** — per-recipient send records with delivery, open, click, and bounce timestamps
- **Unsubscribe flow** — public-facing pages for per-list unsubscribe and global opt-out
- **Campaign viewer** — legacy `/view/:campaignId` route (the primary viewer today is R2-hosted, see section 2)
- **Read-only SQL query endpoint** — ad-hoc SELECT/WITH/EXPLAIN queries against the database

Routing:
- Authenticated routes under `/api/*` (X-API-Key header)
- Public routes at `/view/*` and `/unsubscribe`

**Base URL**: `https://email.step.is`

---

## 2. Render & Send Pipeline (Python)

The Python side turns campaign HTML into actual emails in inboxes.

| Script | Role |
|--------|------|
| `send_email.py` | Low-level SES SMTP sender (single email, HTML or plain) |
| `campaign_email.py` | Reusable campaign renderer: loads templates, resolves locale, uploads to R2, sends via SES |
| `send_bulk.py` | Bulk sender: fetches subscribers from a list and sends to each with configurable pacing (default 200ms between sends, ~5/sec to stay under SES rate limits) |
| `_send_campaign_preview.py` | CLI wrapper for sending a preview of any campaign |

### Flow (per recipient)

1. **Render** — `campaign_email.render_email(slug, lang, variables)` loads `header.html` + `{slug}/body.html` + `footer.html`, resolves locale variables and custom `{{variables}}`, returns complete HTML.
2. **Upload to R2** — rendered HTML is uploaded to the `emails` R2 bucket at `{slug}/{uuid}.html`. The public URL `https://emails.step.is/{slug}/{uuid}.html` serves as the "View in browser" link.
3. **Send via SES** — `send_email.send_email()` delivers the HTML through AWS SES SMTP.

This design scales to thousands of personal emails per campaign — each recipient gets a unique R2 URL, no database lookup needed to view in browser.

### Bulk Sending

`send_bulk.py` drives the full pipeline for list-based campaigns:

1. Fetches the list's subscribers from the Workers API
2. **Fetches already-sent emails** for the campaign and filters them out (idempotent, safe to resume)
3. **Shows a confirmation summary** and requires the operator to type the FROM address before live sends
4. For each remaining subscriber: renders + uploads to R2 + sends via SES
5. **Records each send** to `email_campaign_send` via `POST /api/campaigns/:id/sends` (unique constraint on `(campaign_id, email)` backs the dedup)
6. Stores the per-recipient R2 `view_url` in the DB
7. Paces sends (default 200ms = ~5/sec, well under SES's 14/sec default quota)
8. Reports per-recipient success/failure as it goes

```bash
# Dry run with dedup (renders but doesn't send or record)
python send_bulk.py <slug> <list-id> <campaign-id> <lang> "<subject>" --dry-run --limit=5

# Live send (will prompt for confirmation)
python send_bulk.py introduce-nspace-users-to-step-app 3 1 en "Hello from Step"

# Custom from address + custom pacing
python send_bulk.py <slug> <list-id> <campaign-id> <lang> "<subject>" \
    --from=long@nspace.is --delay-ms=500

# Skip confirmation (CI / scripted use — use with care)
python send_bulk.py <slug> <list-id> <campaign-id> <lang> "<subject>" --yes
```

Available as a module too: `from send_bulk import send_bulk` with optional `variables_fn` for per-recipient personalization.

### Sender Addresses

- **Default `from` address**: `support@step.is` (set in `campaign_email.FROM_EMAIL`)
- **Override per campaign**: pass `--from=<email>` on the CLI or `from_email=` as a kwarg
- Campaigns sent personally (e.g. founder outreach) should override to a personal address and match the signature in the body

### Idempotency & Resume

- The DB has a unique constraint on `email_campaign_send(email_campaign_id, email)` — you physically cannot insert a duplicate
- Before each send, the sender checks `GET /api/campaigns/:id/sends` and filters out already-sent recipients
- After each successful SES delivery, the sender records the send via `POST /api/campaigns/:id/sends`
- If the script is interrupted mid-send, just re-run with the same args — it will skip everything already sent and resume
- The `view_url` column stores the R2 URL, so you can inspect exactly what each recipient received

---

## 3. Email Content Repository (`campaigns/`)

The source of truth for all email content. Every email — whether a bulk campaign to thousands of subscribers or a one-off personal message to a single recipient — lives here.

### Email Types

| Type | Description | Scale |
|------|-------------|-------|
| **Bulk campaign** | One email template sent to an entire list or segment | 1 template → many recipients |
| **Personal email** | A unique email written for a specific recipient | 1 template → 1 recipient (thousands of these over time) |

### Shared Templates

At the root of `campaigns/`:

- **`header.html`** — email header with inline SVG Step logo, "Step." wordmark, and localized tagline (`{{tagline}}`)
- **`promo.html`** — optional inline block with app download links and website URL (`Download: iOS · Android · macOS / Website: ...`). Can be included as a separate block or inlined directly into a body.
- **`footer.html`** — email footer with unsubscribe link, "View in browser" link, and legal text

Assets: `logo.svg`, `appstore.png`, `playstore.png`

### Localization

Emails support `"en"` and `"vi"` locales. Locale-dependent values are resolved at send time by `campaign_email.py`:

| Variable | `en` | `vi` |
|----------|------|------|
| `{{tagline}}` | Language courses built around content you'd actually enjoy | Khóa học ngôn ngữ từ nội dung bạn thực sự thích |
| `{{website_url}}` | https://step.is | https://step.is/vi |

### Templating

Bodies use `{{variable}}` placeholders resolved at send time:

- `{{tagline}}` — locale-dependent tagline (set in header)
- `{{website_url}}` — locale-dependent website URL
- `{{unsubscribe_url}}` — per-recipient unsubscribe link
- `{{view_url}}` — public R2 link to this email (set automatically)
- Custom variables passed per-send via `variables={...}` (e.g., `{{promo_code}}`, `{{first_name}}`)

### Directory Structure

```
campaigns/
├── header.html                              # Shared header (logo, wordmark, {{tagline}})
├── promo.html                               # Optional download links + website
├── footer.html                              # Shared footer (unsubscribe, view, legal)
├── logo.svg, appstore.png, playstore.png    # Assets
│
└── {campaign-name}/                         # One directory per email
    ├── README.md                            # Metadata: type, lang, target, status, notes
    └── body.html                            # Email body template
```

### README.md Convention

Every email directory contains a `README.md` that serves as the metadata record:

**For bulk campaigns:**
```markdown
# Campaign: Introduce nspace users to Step App
- **Type**: bulk
- **Lang**: vi
- **Target list ID**: <list_id>
- **Status**: sent | draft | scheduled
- **Notes**: <context>
```

**For personal emails:**
```markdown
# Personal: Outreach to Acme Corp
- **Type**: personal
- **Lang**: en
- **To**: [email]
- **Status**: sent | draft
- **Context**: <why this email was sent>
```

### Naming Convention

Directory names use kebab-case and should be descriptive:
- Bulk: `{descriptive-campaign-name}/` (e.g., `introduce-nspace-users-to-step-app/`)
- Personal: `personal-{short-description}/` (e.g., `personal-outreach-acme-corp/`)

---

## Sending a Campaign — End-to-End Workflow

1. **Draft content**: create `campaigns/{slug}/README.md` + `body.html`
2. **Preview**: `python _send_campaign_preview.py {slug} {lang}` → sends a test email and prints the R2 "view in browser" URL
3. **Iterate**: tweak copy and templates, re-preview
4. **Create subscriber list** (if needed): via the Workers API `/api/lists` + `/api/lists/:id/subscribers/bulk`
5. **Create campaign record**: `POST /api/campaigns` — this returns the `campaign_id` used for dedup tracking. The campaign row in the DB already stores the **target list ID** (`email_list_id`), so the list-to-campaign mapping is authoritative in the database — no need to look it up separately.
6. **Dry run**: `python _run_campaign_and_summarize.py {slug} {list_id} {campaign_id} {lang} "{subject}" --dry-run --limit=5`
7. **Bulk send**: `python _run_campaign_and_summarize.py {slug} {list_id} {campaign_id} {lang} "{subject}" --from=long@nspace.is` — sends all emails, dedupes against prior sends, and emails a summary to `long@nspace.is` when done
8. **Resume if interrupted**: re-run the same command — already-sent recipients are skipped automatically
9. **Track**: `/api/campaigns/:id/sends` shows per-recipient send state (status, sent_at, bounced_at, view_url)

> **Always use `_run_campaign_and_summarize.py` for live sends** — it wraps `send_bulk.py` and adds the post-send summary email. Use `send_bulk.py` directly only for scripting or module-level imports.

### SES Rate Limit Notes

- Default SES sending rate: **14 messages/second** (sandbox) or higher once out of sandbox
- Default send quota: **200 messages/day** (sandbox) or more once approved
- `send_bulk.py` paces at **5/sec (200ms delay)** by default — safe for all tiers
- For production use at scale, check your current SES quota and adjust `--delay-ms` accordingly
