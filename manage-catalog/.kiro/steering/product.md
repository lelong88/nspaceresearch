---
inclusion: always
---

# Product Overview

This project manages the **curriculum catalog system** — the content hierarchy and display logic for a language-learning platform. It exposes APIs via a Cloudflare Worker to serve catalog data to client applications.

## Infrastructure

- **Database**: PostgreSQL (accessible via MCP postgres for reads)
- **API Layer**: Cloudflare Worker in the `worker/` folder, deployed via Wrangler
- **Networking**: Worker uses Hyperdrive for pooled Postgres connections
- **Domain**: `catalogapi.step.is` (custom domain pending first deployment)

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
   - A collection is **only visible** in a catalog if the display profile explicitly overrides its `display_order` to a positive value (> 0)
   - This ensures collection visibility is always intentional per audience
3. **Negative display_order (< 0) hides the item entirely** from that catalog view
4. **Series and curriculums** use `display_order` for relative positioning within their parent; they don't use the same whitelist pattern as collections
5. A display profile's overrides are **merged on top of** the entity's base `display_order`

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
