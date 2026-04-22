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
