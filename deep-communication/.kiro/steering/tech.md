# Tech Stack

## Runtime & Deployment
- **Runtime**: Cloudflare Workers
- **Bundler/CLI**: Wrangler 3.x (`wrangler.toml` is the deployment config)
- **Compatibility**: `nodejs_compat` flag enabled, targeting `2024-12-01`

## Language & Framework
- **Language**: TypeScript (strict mode, ES2022 target)
- **Web framework**: Hono 4.x — lightweight, Workers-native router
- **Database client**: `pg` (node-postgres) connecting through Cloudflare Hyperdrive

## Database
- PostgreSQL accessed via Hyperdrive connection pooling
- Falls back to `DATABASE_URL` env var when Hyperdrive binding is unavailable
- Raw SQL queries with parameterized values (no ORM)

## Email Sending
- **SMTP**: AWS SES via `send_email.py` (Python, smtplib)
- **Default sender**: `support@step.is` — override per campaign with `from_email=` or `--from=<email>` on the CLI
- **Campaign rendering**: `campaign_email.py` — loads HTML templates, resolves locale + variables, uploads to R2, sends via SES
- **Bulk sending**: `send_bulk.py` — fetches list subscribers from the Workers API and dispatches per-recipient sends with configurable pacing (default 200ms / ~5 msg/s, safely under SES default 14/s rate limit)
- **Confirmation guardrail**: `send_bulk.py` requires the operator to type the FROM address before any live send
- **Idempotency**: each send is recorded in `email_campaign_send` with a unique constraint on `(campaign_id, email)` — duplicates are prevented at the DB level and skipped client-side. Interrupted runs are safe to resume.
- **"View in browser"**: rendered emails uploaded to Cloudflare R2 bucket `emails` (public domain: `https://emails.step.is`). The per-recipient URL is stored in `email_campaign_send.view_url`.
- **R2 client**: boto3 (S3-compatible API)

## Testing
- **Test runner**: Vitest 2.x (`vitest --run` for single execution)
- **Property-based testing**: fast-check 3.x
- **Test file patterns**: `src/**/*.test.ts`, `src/**/*.property.test.ts`

## Common Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start local dev server via Wrangler |
| `npm run deploy` | Deploy to Cloudflare Workers |
| `npm test` | Run all tests (Vitest, single run) |
| `python _send_campaign_preview.py` | Send a campaign preview email |
| `python _send_campaign_preview.py <slug> <lang>` | Preview a specific campaign + locale |
| `python send_bulk.py <slug> <list_id> <campaign_id> <lang> "<subject>"` | Bulk send (prompts for confirmation, paced at 200ms/send, dedupes via DB) |
| `python send_bulk.py ... --dry-run --limit=5` | Dry-run (render-only, shows dedup state) |
| `python send_bulk.py ... --from=long@nspace.is` | Override sender address |
| `python send_bulk.py ... --yes` | Skip confirmation (scripted use) |

## Environment Variables
- `DATABASE_URL` — PostgreSQL connection string
- `API_KEY` — shared secret for API authentication
- `HYPERDRIVE` — Cloudflare Hyperdrive binding (set automatically in Workers)
- `SES_SMTP_HOST` — AWS SES SMTP endpoint
- `SES_SMTP_PORT` — AWS SES SMTP port (587)
- `SES_SMTP_USER` — AWS SES SMTP username
- `SES_SMTP_PASSWORD` — AWS SES SMTP password
- `R2_ENDPOINT_URL` — Cloudflare R2 S3-compatible endpoint
- `R2_ACCESS_KEY_ID` — R2 API access key
- `R2_SECRET_ACCESS_KEY` — R2 API secret key
