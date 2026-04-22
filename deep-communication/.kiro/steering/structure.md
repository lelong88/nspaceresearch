# Project Structure

```
src/
├── index.ts              # App entrypoint — mounts middleware and route groups
├── types.ts              # Shared TypeScript interfaces (Env, domain models)
├── db.ts                 # Database connection helper (getClient) and error class
├── middleware/
│   ├── auth.ts           # API key authentication (X-API-Key header, constant-time compare)
│   └── cors.ts           # CORS headers for all routes
└── routes/
    ├── lists.ts          # CRUD for email lists          (/api/lists)
    ├── subscribers.ts    # Subscriber management          (/api/lists/:id/subscribers)
    ├── campaigns.ts      # CRUD for email campaigns       (/api/campaigns)
    ├── sends.ts          # Read-only send tracking         (/api/campaigns/:id/sends)
    ├── query.ts          # Ad-hoc read-only SQL endpoint  (/api/query)  [authenticated]
    ├── view.ts           # Public campaign HTML viewer    (/view/:campaignId)
    └── unsubscribe.ts    # Public unsubscribe pages       (/unsubscribe)
```

## Conventions

- **Route files** export a `Hono` sub-router (e.g. `listsRouter`) mounted in `index.ts` via `app.route()`.
- **Authenticated routes** live under `/api/*`; public routes mount at `/`.
- **Database access**: each handler calls `getClient(c.env)`, runs queries, then closes the client in a `finally` block. Always use parameterized queries (`$1`, `$2`, …).
- **Input validation**: parse JSON with try/catch, validate required fields manually, return 400 on bad input.
- **Error responses**: API routes return JSON (`{ error: "..." }`); public routes return HTML pages.
- **HTTP status codes**: 201 for creation, 204 for deletion, 404 for not found, 409 for conflicts, 422 for semantic errors.
- **Types**: domain interfaces live in `types.ts`. The `Env` interface defines Worker bindings and is used as `Hono<{ Bindings: Env }>` generic.
- **No ORM**: all database interaction is raw SQL via `pg.Client`.
