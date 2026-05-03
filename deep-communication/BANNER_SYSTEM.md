# Banner System — Background Engine Guide

This document describes how the banner system works and how the background engine should interact with it via direct database inserts.

---

## Overview

The banner system delivers personalized, time-sensitive banners to users. The background engine is responsible for:

1. Creating banner definitions in the `banner` table
2. Assigning banners to specific users in the `user_banner` table

The API handles retrieval, display tracking, and dismissal automatically.

---

## Database Schema

### `banner` table

Stores banner definitions (the content/template).

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `id` | SERIAL | NO | auto | Primary key |
| `title` | TEXT | YES | NULL | Banner title text |
| `subtitle` | TEXT | YES | NULL | Banner subtitle text |
| `image_url` | TEXT | YES | NULL | URL to banner image |
| `url` | TEXT | YES | NULL | Destination URL when user taps the banner |
| `type` | VARCHAR | NO | — | One of: `standard`, `minimal`, `transient` |
| `is_active` | BOOLEAN | NO | true | Set to false to globally disable a banner |
| `created_at` | TIMESTAMP | NO | NOW() | Auto-set on insert |

### `user_banner` table

Stores per-user banner assignments with expiration rules.

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `id` | SERIAL | NO | auto | Primary key |
| `user_uid` | VARCHAR | NO | — | FK → `my_user.uid` |
| `banner_id` | INTEGER | NO | — | FK → `banner.id` |
| `max_expiration_date` | TIMESTAMP | NO | — | Absolute deadline after which banner is never shown |
| `first_shown_expiration_hours` | INTEGER | YES | NULL | Hours after first view before banner expires. NULL = no relative expiration |
| `first_shown_at` | TIMESTAMP | YES | NULL | Auto-set by API when user first sees the banner. Do NOT set this manually |
| `display_order` | INTEGER | YES | NULL | Controls display priority. Higher number = shown first. NULL = shown last |
| `is_dismissed` | BOOLEAN | NO | false | Set by API when user dismisses. Do NOT set this manually |
| `created_at` | TIMESTAMP | NO | NOW() | Auto-set on insert |

**Constraints:**
- UNIQUE on `(user_uid, banner_id)` — a user can only be assigned a given banner once
- FK on `banner_id` → `banner(id)`
- No FK on `user_uid` — allows the special value `'all'` for global banners

---

## Banner Types

| Type | Where it appears | Endpoint |
|------|-----------------|----------|
| `standard` | `banners` field in `getPublic` response | POST `/user/getPublic` |
| `minimal` | `bannersMinimal` field in `getPublic` response | POST `/user/getPublic` |
| `transient` | Dedicated response | POST `/user/getTransientBanners` |

---

## Global Banners (show to all users)

To show a banner to **every user** without creating individual assignments, set `user_uid = 'all'`:

```sql
INSERT INTO user_banner (user_uid, banner_id, max_expiration_date, display_order)
VALUES (
  'all',           -- magic value: shows to every user
  3,               -- banner.id
  '2025-09-01 00:00:00',
  100              -- high priority so it shows first
);
```

- The API automatically includes `user_uid = 'all'` banners alongside the user's personal banners
- Users **can dismiss** global banners — a personal dismissed record is created for that user, hiding the banner only for them
- All other filtering rules (expiration, is_active, etc.) still apply
- No FK constraint on `user_uid` — the value `'all'` doesn't need to exist in `my_user`

---

## How to Create and Assign Banners

### Step 1: Insert a banner definition

```sql
INSERT INTO banner (title, subtitle, image_url, url, type)
VALUES (
  'Upgrade to Pro!',
  'Get 50% off this week only',
  'https://cdn.example.com/banners/pro-upgrade.png',
  'https://app.example.com/upgrade',
  'standard'
);
```

### Step 2: Assign the banner to a user

```sql
INSERT INTO user_banner (user_uid, banner_id, max_expiration_date, first_shown_expiration_hours, display_order)
VALUES (
  'firebase-uid-abc123',
  1,  -- the banner.id from step 1
  '2025-07-01 00:00:00',  -- absolute expiration
  48,  -- expires 48 hours after user first sees it (optional, use NULL for no relative expiration)
  10   -- display priority (optional, higher = shown first, NULL = shown last)
);
```

### Bulk assignment example

```sql
-- Assign banner #5 to all users who signed up in the last 7 days
INSERT INTO user_banner (user_uid, banner_id, max_expiration_date, first_shown_expiration_hours, display_order)
SELECT uid, 5, '2025-08-01 00:00:00', 72, 5
FROM my_user
WHERE created_at >= NOW() - INTERVAL '7 days'
ON CONFLICT (user_uid, banner_id) DO NOTHING;
```

---

## Expiration Logic

A banner is shown to a user only when ALL of these conditions are true:

1. **`banner.is_active = true`** — the banner hasn't been globally disabled
2. **`user_banner.is_dismissed = false`** — the user hasn't dismissed it
3. **`NOW() <= user_banner.max_expiration_date`** — the absolute deadline hasn't passed
4. **Relative expiration check** — one of:
   - `first_shown_expiration_hours IS NULL` (no relative expiration), OR
   - `first_shown_at IS NULL` (user hasn't seen it yet, so countdown hasn't started), OR
   - `NOW() <= first_shown_at + first_shown_expiration_hours`

### Expiration strategy examples

| Scenario | max_expiration_date | first_shown_expiration_hours |
|----------|--------------------|-----------------------------|
| Show for 7 days max, no matter what | NOW() + 7 days | NULL |
| Show until user sees it, then give them 24h | far future date | 24 |
| Show for 30 days max, but only 48h after first view | NOW() + 30 days | 48 |
| One-time flash sale ending at specific time | '2025-06-15 23:59:59' | NULL |

---

## Fields the API Returns to the Client

When a user's banners are fetched, each banner is returned as:

```json
{
  "id": 42,
  "title": "Upgrade to Pro!",
  "subtitle": "Get 50% off this week only",
  "imageUrl": "https://cdn.example.com/banners/pro-upgrade.png",
  "url": "https://app.example.com/upgrade"
}
```

- `id` is the `user_banner.id` (used by the client to dismiss)
- `title`, `subtitle`, `imageUrl`, `url` come from the `banner` table

---

## Disabling / Removing Banners

### Globally disable a banner (stops showing to ALL users)

```sql
UPDATE banner SET is_active = false WHERE id = 5;
```

### Remove a specific user's assignment

```sql
DELETE FROM user_banner WHERE user_uid = 'firebase-uid-abc123' AND banner_id = 5;
```

### Expire all assignments for a banner immediately

```sql
UPDATE user_banner SET max_expiration_date = NOW() WHERE banner_id = 5;
```

---

## Important Notes

- **Do NOT set `first_shown_at`** — the API sets this automatically when the user first retrieves the banner
- **Do NOT set `is_dismissed`** — the API sets this when the user dismisses via the `dismissBanner` endpoint
- **Duplicate assignments are rejected** — the UNIQUE constraint on `(user_uid, banner_id)` prevents assigning the same banner twice. Use `ON CONFLICT DO NOTHING` for bulk inserts
- **Global banners** — set `user_uid = 'all'` to show a banner to every user without individual assignments. Users can dismiss global banners (a personal dismissed record is created for them)
- **Ordering** — banners are sorted by `display_order DESC NULLS LAST`, then by `created_at DESC`. Set `display_order` to control priority (higher number = shown first). Banners with NULL `display_order` appear after all banners that have a value
- **Null fields** — `title`, `subtitle`, `image_url`, and `url` can all be NULL if the client handles it
- **The `type` field is required** — must be exactly one of: `standard`, `minimal`, `transient`
