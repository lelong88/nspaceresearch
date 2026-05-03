---
inclusion: always
---

# Product Overview

This project manages the **curriculum catalog system** — the content hierarchy and display logic for a language-learning platform. It exposes APIs via a Cloudflare Worker to serve catalog data to client applications.

## Infrastructure

- **Database**: PostgreSQL (accessible via MCP postgres for reads)
- **API Layer**: Cloudflare Worker in the `worker/` folder, deployed via Wrangler
- **Networking**: Worker uses Hyperdrive for pooled Postgres connections (requires `nodejs_compat` flag)
- **Domain**: `https://catalogapi.step.is` (live, deployed)
- **Framework**: Hono (lightweight web framework for Workers)
- **DB Client**: `pg` (node-postgres) over Hyperdrive connection string

## Authentication

- **Method**: Static API key via `X-API-Key` header
- **Key**: `sk-catalog-9f7b2a1e4d6c8x3w5q0m` (hardcoded in `worker/src/index.ts`)
- **Public routes** (no auth required): `GET /` (health check)
- **Protected routes**: All other endpoints (including catalog) require the `X-API-Key` header

Example:
```
curl -H "X-API-Key: sk-catalog-9f7b2a1e4d6c8x3w5q0m" https://catalogapi.step.is/collections
```

## Content Hierarchy

The content is organized in a three-level hierarchy:

```
Collection (curriculum_collections)
├── Series (curriculum_series) — linked via curriculum_collection_series
│   └── Curriculum (curriculum) — linked via curriculum_series_items
└── Curriculum (curriculum) — linked directly via curriculum_collection_items
```

### curriculum_collections
Top-level grouping of content (e.g., "Power English", "Kids English", "Topic-Based Vocabulary").

| Column | Type | Notes |
|--------|------|-------|
| id | varchar | PK |
| title | varchar | Required |
| description | text | Optional |
| is_public | boolean | Default `false` |
| thumbnail | varchar | Optional image URL |
| display_order | integer | Default `-2000` (hidden by default) |
| created_at | timestamp | Auto |

### curriculum_series
A sequence of related curriculums within a collection.

| Column | Type | Notes |
|--------|------|-------|
| id | varchar | PK |
| title | varchar | Required |
| description | varchar | Optional |
| thumbnail | varchar | Optional image URL |
| is_public | boolean | Default `false` |
| display_order | integer | Default `0` |
| created_at | timestamp | Auto |

### curriculum
An individual learning unit containing lessons.

| Column | Type | Notes |
|--------|------|-------|
| id | text | PK |
| uid | varchar | Unique identifier |
| language | text | Target language |
| user_language | text | Learner's native language |
| content | jsonb | Curriculum content/structure |
| instruction | text | Optional teaching instructions |
| is_public | boolean | Default `false` |
| price | integer | Default `49` (credits) |
| list_price | integer | Optional strikethrough price |
| display_order | integer | Default `0` |
| is_disabled | boolean | Optional disable flag |
| created_at | timestamp | Auto |

### Junction Tables

- **curriculum_collection_series** (`curriculum_collection_id`, `curriculum_series_id`) — links series to collections
- **curriculum_collection_items** (`curriculum_collection_id`, `curriculum_id`) — links curriculums directly to collections
- **curriculum_series_items** (`curriculum_series_id`, `curriculum_id`) — links curriculums to series

## Display Profiles (Catalogs)

A **display profile** (`display_profile` table) defines a personalized catalog view for a target audience. Each profile overrides the default display ordering to curate what content appears and in what position.

| Column | Type | Notes |
|--------|------|-------|
| id | serial | PK |
| description | text | Human-readable description of the target audience |
| display_order_override | jsonb | Override map (see structure below) |
| created_at | timestamp | Auto |

### display_order_override Structure

```json
{
  "collections": { "<collection_id>": <number>, ... },
  "series": { "<series_id>": <number>, ... },
  "curriculums": { "<curriculum_id>": <number>, ... }
}
```

### Ordering & Visibility Rules

1. **Higher `display_order` = shown first** (descending sort)
2. **Collections use a whitelist pattern**:
   - Default `display_order` for collections is `-2000` (hidden)
   - A collection is **only visible** in a catalog if the display profile explicitly overrides its `display_order` to a non-negative value (>= 0)
   - This ensures collection visibility is always intentional per audience
3. **Negative display_order (< 0) hides the item entirely** from that catalog view
4. **Series and curriculums** use `display_order` for relative positioning within their parent; they don't use the same whitelist pattern as collections
5. A display profile's overrides are **merged on top of** the entity's base `display_order`

### Quick Reference View

Use the `display_profile_collections` view for a quick overview of which collections are assigned to which profiles and their effective display order:

```sql
SELECT profile_id, collection_id, collection_title, display_order, hidden
FROM display_profile_collections
WHERE profile_id = <id>
ORDER BY display_order DESC;
```

### Example Audiences
- University economics students (Vietnamese) — promotes business/economics content
- Office professionals (beginner) — promotes workplace English, coaching
- General beginners — promotes featured content, topic-based vocabulary, fiction

## API Design Principles

- RESTful endpoints served from the Cloudflare Worker
- All catalog queries should resolve the effective display order by merging base `display_order` with the relevant `display_profile.display_order_override`
- Filter out items with effective `display_order < 0` from responses
- Sort results by effective `display_order` descending
- Support CRUD for collections, series, curriculums, and display profiles

## API Endpoints (Base: `https://catalogapi.step.is`)

### Health
| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check — returns `{"status":"ok"}` |

### Collections (`/collections`)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/collections` | List all collections |
| GET | `/collections/:id` | Get single collection |
| POST | `/collections` | Create collection (body: `{id, title, description?, is_public?, thumbnail?}`) |
| PUT | `/collections/:id` | Update collection (body: any subset of `{title, description, is_public, thumbnail, display_order}`) |
| DELETE | `/collections/:id` | Delete collection |
| POST | `/collections/:id/curriculums` | Add curriculum to collection (body: `{curriculum_id}`) |
| DELETE | `/collections/:id/curriculums/:curriculumId` | Remove curriculum from collection |
| POST | `/collections/:id/series` | Add series to collection (body: `{series_id}`) |
| DELETE | `/collections/:id/series/:seriesId` | Remove series from collection |

### Series (`/series`)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/series` | List all series |
| GET | `/series/:id` | Get single series |
| POST | `/series` | Create series (body: `{id, title, description?, thumbnail?, is_public?, display_order?}`) |
| PUT | `/series/:id` | Update series (body: any subset of `{title, description, thumbnail, is_public, display_order}`) |
| DELETE | `/series/:id` | Delete series |
| POST | `/series/:id/curriculums` | Add curriculum to series (body: `{curriculum_id}`) |
| DELETE | `/series/:id/curriculums/:curriculumId` | Remove curriculum from series |

### Curriculums (`/curriculums`)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/curriculums` | List curriculums (query: `?language=&limit=&offset=`). Returns lightweight rows (no `content` field) |
| GET | `/curriculums/:id` | Get full curriculum including `content` jsonb |
| PUT | `/curriculums/:id` | Update curriculum fields |

### Display Profiles (`/display-profiles`)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/display-profiles` | List all display profiles |
| GET | `/display-profiles/:id` | Get single display profile |
| POST | `/display-profiles` | Create profile (body: `{description, display_order_override?}`) |
| PUT | `/display-profiles/:id` | Update profile (body: `{description?, display_order_override?}`) |
| DELETE | `/display-profiles/:id` | Delete profile |

### Catalog (`/catalog`)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/catalog/:profileId` | Resolved catalog view for a display profile. Merges overrides, filters hidden items, returns nested collections → series → curriculums sorted by effective display_order DESC |

## Worker Project Structure

```
worker/
├── package.json
├── wrangler.toml          # Wrangler config (Hyperdrive binding, nodejs_compat)
├── tsconfig.json
└── src/
    ├── index.ts           # Hono app entry point, CORS, route mounting, error handler
    ├── types.ts           # TypeScript interfaces (Env, DB row types, API response types)
    ├── db.ts              # getClient() + query() helpers using pg over Hyperdrive
    └── routes/
        ├── collections.ts
        ├── series.ts
        ├── curriculums.ts
        ├── display-profiles.ts
        └── catalog.ts     # The key endpoint — resolves full catalog view
```
