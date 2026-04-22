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

## Environment Variables
- `DATABASE_URL` — PostgreSQL connection string
- `API_KEY` — shared secret for API authentication
- `HYPERDRIVE` — Cloudflare Hyperdrive binding (set automatically in Workers)
