# Product Overview

Email Workers is an email campaign management API built on Cloudflare Workers. It provides:

- **Email list management** — create, update, delete mailing lists
- **Subscriber management** — add/remove subscribers per list, with duplicate and opt-out enforcement
- **Campaign management** — create, schedule, and track email campaigns with HTML and plain-text bodies
- **Send tracking** — per-recipient send records with delivery, open, click, and bounce timestamps
- **Unsubscribe flow** — public-facing pages for per-list unsubscribe and global opt-out
- **Campaign viewer** — public HTML rendering of campaigns with injected unsubscribe links
- **Read-only SQL query endpoint** — ad-hoc SELECT/WITH/EXPLAIN queries against the database

The API is split into authenticated routes (`/api/*` behind API key auth) and public routes (`/view/*`, `/unsubscribe`).

**Base URL**: `https://email.step.is`

---

## Email Content Repository (`campaigns/`)

The `campaigns/` directory is the **single source of truth for all email content** sent through the system. Every email — whether a bulk campaign to thousands of subscribers or a one-off personal message to a single recipient — is tracked here.

### Email Types

| Type | Description | Scale |
|------|-------------|-------|
| **Bulk campaign** | One email template sent to an entire list or segment | 1 template → many recipients |
| **Personal email** | A unique email written for a specific recipient | 1 template → 1 recipient (thousands of these over time) |

### Shared Assets

All emails share common layout components stored at the root of `campaigns/`:

- **`header.html`** — shared email header (logo, wordmark, tagline)
- **`promo.html`** — optional app download CTAs + social links block (include when promoting the app)
- **`footer.html`** — shared email footer (unsubscribe, view in browser, legal text)

These are injected into every email at send time. Individual emails can override or extend them if needed.

### Templating

Email bodies support simple template variables for personalization:

- `{{first_name}}`, `{{last_name}}`, `{{email}}` — subscriber fields
- `{{unsubscribe_url}}` — per-recipient unsubscribe link
- `{{view_url}}` — link to view the email in a browser
- `{{list_name}}`, `{{campaign_name}}` — metadata
- Custom variables can be passed per-send for personal emails

### Directory Structure

Each email (bulk or personal) lives in its own subdirectory under `campaigns/`:

```
campaigns/
├── header.html                              # Shared header template
├── footer.html                              # Shared footer template
│
├── introduce-nspace-users-to-step-app/      # Bulk campaign example
│   ├── README.md                            # Metadata: target list, send date, notes
│   └── body.html                            # Email body (uses {{variables}})
│
├── personal-outreach-acme-corp/             # Personal email example
│   ├── README.md                            # Metadata: target email, context, send date
│   └── body.html
│
└── welcome-series-01/                       # Another bulk campaign
    ├── README.md
    └── body.html
```

### README.md Convention

Every email directory contains a `README.md` that serves as the metadata record:

**For bulk campaigns:**
```markdown
# Campaign: Introduce nspace users to Step App
- **Type**: bulk
- **Target list ID**: <list_id>
- **Sent**: 2025-03-15
- **Status**: sent | draft | scheduled
- **Notes**: <any context about the campaign>
```

**For personal emails:**
```markdown
# Personal: Outreach to Acme Corp
- **Type**: personal
- **To**: [email]
- **Sent**: 2025-04-10
- **Status**: sent | draft
- **Context**: <why this email was sent, relationship context>
```

### Naming Convention

Directory names use kebab-case and should be descriptive:
- Bulk: `{descriptive-campaign-name}/` (e.g., `introduce-nspace-users-to-step-app/`)
- Personal: `personal-{short-description}/` (e.g., `personal-outreach-acme-corp/`)
