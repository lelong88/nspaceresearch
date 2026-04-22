# Implementation Plan: Email Workers

## Overview

Build a single Cloudflare Worker using Hono and the `pg` driver that exposes JSON REST API endpoints for managing email lists, subscribers, campaigns, and campaign sends, plus public HTML routes for campaign browser view and unsubscribe flow. The implementation proceeds incrementally: project scaffolding → database module → middleware → API routes → public routes → error handling → wiring and final integration.

## Tasks

- [x] 1. Set up project structure, configuration, and core types
  - [x] 1.1 Create `wrangler.toml` with worker name, compatibility date, `nodejs_compat` flag, and account id placeholder; create `package.json` with dependencies (`hono`, `pg`) and dev dependencies (`vitest`, `fast-check`, `wrangler`, `@cloudflare/workers-types`, `typescript`); create `tsconfig.json` targeting ES2022 with Workers-compatible settings
    - _Requirements: 10.1, 10.2, 10.3_
  - [x] 1.2 Create `src/types.ts` with the `Env` interface (DATABASE_URL, API_KEY, HYPERDRIVE?) and TypeScript interfaces for all data models: `EmailList`, `EmailListSubscriber`, `EmailCampaign`, `EmailCampaignSend`, `EmailOptOut`
    - _Requirements: 7.1_
  - [x] 1.3 Create `src/index.ts` with the Hono app skeleton, register CORS middleware on all routes, mount API and public route groups (empty placeholders), and export the default fetch handler
    - _Requirements: 9.5, 10.1_

- [x] 2. Implement database module and auth middleware
  - [x] 2.1 Create `src/db.ts` with `getClient(env: Env)` function that creates a `pg.Client` using `HYPERDRIVE?.connectionString ?? DATABASE_URL`, connects, and returns the client; wrap `connect()` in try/catch to enable 503 handling
    - _Requirements: 7.1, 7.2, 7.3_
  - [x] 2.2 Implement API key auth middleware in `src/middleware/auth.ts` that checks for `X-API-Key` header presence (401 if missing), then validates the value against `API_KEY` secret using `crypto.subtle.timingSafeEqual` via HMAC digest comparison (403 if invalid); apply only to `/api/*` routes
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_
  - [x] 2.3 Implement CORS middleware in `src/middleware/cors.ts` that sets `Access-Control-Allow-Origin: *`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers` on all responses and handles OPTIONS preflight with 204
    - _Requirements: 9.5_
  - [ ]* 2.4 Write property tests for auth middleware (`src/__tests__/properties/auth.property.test.ts`)
    - **Property 14: Missing API key returns 401** — generate arbitrary `/api/*` paths and verify 401 when no `X-API-Key` header is present
    - **Property 15: Invalid API key returns 403** — generate arbitrary non-matching key strings and verify 403
    - **Property 16: Public routes accessible without auth** — generate requests to `/view/:id` and `/unsubscribe` and verify response is never 401 or 403
    - **Validates: Requirements 8.1, 8.3, 8.4, 8.6**
  - [ ]* 2.5 Write unit tests for auth and CORS middleware (`src/__tests__/unit/auth.test.ts`, `src/__tests__/unit/cors.test.ts`)
    - Test specific examples: valid key passes, missing key returns 401, wrong key returns 403, OPTIONS returns 204 with CORS headers
    - _Requirements: 8.1, 8.3, 8.4, 8.5, 9.5_

- [x] 3. Implement Email List CRUD routes
  - [x] 3.1 Create `src/routes/lists.ts` with Hono router implementing POST `/api/lists` (insert + return 201), GET `/api/lists` (return all as JSON array, 200), GET `/api/lists/:id` (return single, 200 or 404), PUT `/api/lists/:id` (update with `updated_at = NOW()`, 200 or 404), DELETE `/api/lists/:id` (delete, 204 or 404); validate `name` is present on POST/PUT (400 if missing); use parameterized queries throughout
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 7.2_
  - [x] 3.2 Mount lists router in `src/index.ts` under the API route group
    - _Requirements: 1.1_
  - [ ]* 3.3 Write property tests for lists (`src/__tests__/properties/lists.property.test.ts`)
    - **Property 1: List creation preserves input data** — generate arbitrary valid name/description pairs and verify 201 response contains the same values plus id and timestamps
    - **Property 2: List update preserves input and refreshes timestamp** — generate update payloads and verify fields are reflected with updated `updated_at`
    - **Property 3: List creation rejects payloads missing required name** — generate payloads without a non-empty `name` and verify 400 with `error` field
    - **Validates: Requirements 1.1, 1.4, 1.7**
  - [ ]* 3.4 Write unit tests for lists (`src/__tests__/unit/lists.test.ts`)
    - Test GET all returns array, GET by ID returns record, GET non-existent returns 404, DELETE returns 204, PUT non-existent returns 404
    - _Requirements: 1.2, 1.3, 1.5, 1.6_

- [x] 4. Implement Subscriber Management routes
  - [x] 4.1 Create `src/routes/subscribers.ts` with Hono router implementing POST `/api/lists/:id/subscribers` (check list exists → 404, check duplicate → 409, check opt-out → 422, insert with status `subscribed` → 201), GET `/api/lists/:id/subscribers` (return all for list, 200), DELETE `/api/lists/:id/subscribers/:subscriberId` (delete, 204); use parameterized queries
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6_
  - [x] 4.2 Mount subscribers router in `src/index.ts` under the API route group
    - _Requirements: 2.1_
  - [ ]* 4.3 Write property tests for subscribers (`src/__tests__/properties/subscribers.property.test.ts`)
    - **Property 4: Subscriber creation preserves email and links to list** — generate valid emails and verify 201 with correct email, email_list_id, and status `subscribed`
    - **Property 5: Duplicate subscriber email is rejected** — simulate existing subscriber and verify 409
    - **Property 6: Opted-out email cannot be subscribed** — simulate opt-out record and verify 422
    - **Validates: Requirements 2.1, 2.4, 2.5**
  - [ ]* 4.4 Write unit tests for subscribers (`src/__tests__/unit/subscribers.test.ts`)
    - Test GET all subscribers for list, DELETE subscriber returns 204, POST to non-existent list returns 404
    - _Requirements: 2.2, 2.3, 2.6_

- [x] 5. Checkpoint
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Implement Campaign CRUD routes
  - [x] 6.1 Create `src/routes/campaigns.ts` with Hono router implementing POST `/api/campaigns` (validate name+subject required → 400, validate email_list_id exists if provided → 422, insert with status `draft` → 201), GET `/api/campaigns` (200), GET `/api/campaigns/:id` (200 or 404), PUT `/api/campaigns/:id` (validate name+subject → 400, validate email_list_id → 422, update with `updated_at = NOW()` → 200 or 404), DELETE `/api/campaigns/:id` (204 or 404); use parameterized queries
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 7.2_
  - [x] 6.2 Mount campaigns router in `src/index.ts` under the API route group
    - _Requirements: 3.1_
  - [ ]* 6.3 Write property tests for campaigns (`src/__tests__/properties/campaigns.property.test.ts`)
    - **Property 7: Campaign creation defaults to draft status** — generate valid campaign payloads and verify 201 with status `draft` and all fields preserved
    - **Property 8: Campaign update preserves input and refreshes timestamp** — generate update payloads and verify fields reflected with updated `updated_at`
    - **Property 9: Campaign creation rejects payloads missing required fields** — generate payloads missing name or subject and verify 400 with `error` field
    - **Validates: Requirements 3.1, 3.4, 3.7**
  - [ ]* 6.4 Write unit tests for campaigns (`src/__tests__/unit/campaigns.test.ts`)
    - Test GET all returns array, GET by ID, GET non-existent returns 404, DELETE returns 204, PUT non-existent returns 404, POST with invalid email_list_id returns 422
    - _Requirements: 3.2, 3.3, 3.5, 3.6, 3.8_

- [x] 7. Implement Campaign Send Tracking routes
  - [x] 7.1 Create `src/routes/sends.ts` with Hono router implementing GET `/api/campaigns/:id/sends` (check campaign exists → 404, return all sends as JSON array → 200), GET `/api/campaigns/:id/sends/:sendId` (check campaign exists → 404, return single send → 200 or 404)
    - _Requirements: 4.1, 4.2, 4.3_
  - [x] 7.2 Mount sends router in `src/index.ts` under the API route group
    - _Requirements: 4.1_
  - [ ]* 7.3 Write unit tests for sends (`src/__tests__/unit/sends.test.ts`)
    - Test GET all sends for campaign, GET single send, GET sends for non-existent campaign returns 404, GET non-existent send returns 404
    - _Requirements: 4.1, 4.2, 4.3_

- [x] 8. Implement Campaign Browser View route
  - [x] 8.1 Create `src/routes/view.ts` with Hono router implementing GET `/view/:campaignId` — query campaign, return `body_html` as `text/html` (200), fall back to `body_text` wrapped in basic HTML template if `body_html` is empty/null, inject unsubscribe link at bottom of page, return 404 HTML error page if campaign not found
    - _Requirements: 5.1, 5.2, 5.3, 5.4_
  - [x] 8.2 Mount view router in `src/index.ts` under the public route group
    - _Requirements: 5.1_
  - [ ]* 8.3 Write property tests for browser view (`src/__tests__/properties/public.property.test.ts`)
    - **Property 10: Browser view renders campaign HTML with unsubscribe link** — generate campaigns with non-empty `body_html` and verify 200, Content-Type `text/html`, body contains campaign HTML and unsubscribe link
    - **Validates: Requirements 5.1, 5.4**
  - [ ]* 8.4 Write unit tests for view (`src/__tests__/unit/view.test.ts`)
    - Test body_html rendered correctly, body_text fallback, non-existent campaign returns 404 HTML, unsubscribe link present
    - _Requirements: 5.1, 5.2, 5.3, 5.4_

- [x] 9. Implement Unsubscribe Flow routes
  - [x] 9.1 Create `src/routes/unsubscribe.ts` with Hono router implementing GET `/unsubscribe` (validate email+list_id query params → 400 HTML, render unsubscribe form with list-specific and global opt-out options, show only global opt-out if subscriber not found for list) and POST `/unsubscribe` (handle "unsubscribe from list" → update subscriber status to `unsubscribed` with `unsubscribed_at`, handle "opt out globally" → insert into `email_opt_out` with ON CONFLICT DO NOTHING + update all subscriber records to `unsubscribed`, render confirmation page)
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6_
  - [x] 9.2 Mount unsubscribe router in `src/index.ts` under the public route group
    - _Requirements: 6.1_
  - [ ]* 9.3 Write property tests for unsubscribe flow (`src/__tests__/properties/public.property.test.ts` — append to existing file)
    - **Property 11: Unsubscribe from list updates subscriber status** — simulate subscribed subscriber and verify status becomes `unsubscribed` with non-null `unsubscribed_at`
    - **Property 12: Global opt-out unsubscribes all lists** — simulate email subscribed to multiple lists and verify opt-out record created and all subscribers set to `unsubscribed`
    - **Property 13: Global opt-out is idempotent** — submit global opt-out twice and verify only one `email_opt_out` record exists and confirmation page rendered both times
    - **Validates: Requirements 6.2, 6.3, 6.6**
  - [ ]* 9.4 Write unit tests for unsubscribe (`src/__tests__/unit/unsubscribe.test.ts`)
    - Test GET with valid params renders form, GET missing params returns 400 HTML, POST unsubscribe from list, POST global opt-out, subscriber not found shows only global option
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_

- [x] 10. Checkpoint
  - Ensure all tests pass, ask the user if questions arise.

- [x] 11. Implement global error handling and response consistency
  - [x] 11.1 Add global error handler in `src/index.ts` that catches unhandled exceptions: return JSON `{"error": "Internal server error"}` with 500 for `/api/*` routes, return HTML error page with 500 for public routes; add 503 handling for database connection failures; add not-found handler returning 404 for unmatched routes; add JSON parse error handling in POST/PUT routes returning 400 with `{"error": "Invalid JSON"}`
    - _Requirements: 7.3, 9.1, 9.2, 9.3, 9.4_
  - [ ]* 11.2 Write property tests for error handling (`src/__tests__/properties/errors.property.test.ts`)
    - **Property 17: API error responses are well-formed JSON** — generate various error conditions on `/api/*` routes and verify Content-Type is `application/json` and body contains `error` string field
    - **Property 18: Malformed JSON request body returns 400** — generate non-parseable strings as request bodies to POST/PUT endpoints and verify 400 with JSON error
    - **Property 19: CORS headers present on all responses** — generate requests to arbitrary routes and verify `Access-Control-Allow-Origin` header is present
    - **Validates: Requirements 9.1, 9.3, 9.4, 9.5**
  - [ ]* 11.3 Write unit tests for error handling (`src/__tests__/unit/cors.test.ts` — extend existing)
    - Test 404 for unknown routes, 500 error format for API vs public, 503 for DB failure, malformed JSON returns 400
    - _Requirements: 9.1, 9.2, 9.3_

- [x] 12. Wire everything together and finalize
  - [x] 12.1 Ensure `src/index.ts` has all route groups mounted, middleware applied in correct order (CORS → auth on `/api/*` → routes), and the default export is the Hono app's fetch handler; verify `wrangler.toml` has `main = "src/index.ts"` and `compatibility_flags = ["nodejs_compat"]`
    - _Requirements: 10.1, 10.2, 10.3, 8.1, 8.6, 9.5_
  - [x] 12.2 Add a `vitest.config.ts` configuring Vitest for the project and ensure `package.json` has a `test` script running `vitest --run`
    - _Requirements: 10.3_

- [x] 13. Final checkpoint
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate the 19 universal correctness properties from the design document using fast-check
- Unit tests validate specific examples and edge cases
- All database queries use parameterized syntax (`$1`, `$2`) to prevent SQL injection
- The database module supports Hyperdrive binding fallback for connection pooling
- TypeScript is used throughout as specified in the design document
