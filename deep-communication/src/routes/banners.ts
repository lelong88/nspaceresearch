import { Hono } from "hono";
import type { Env } from "../types";
import { getClient } from "../db";

export const bannersRouter = new Hono<{ Bindings: Env }>();

const VALID_BANNER_TYPES = ["standard", "minimal", "transient"] as const;

// POST /banners — Create a new banner definition
bannersRouter.post("/banners", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { title, subtitle, image_url, url, type } = body as Record<
    string,
    unknown
  >;

  if (!type || typeof type !== "string" || !VALID_BANNER_TYPES.includes(type as any)) {
    return c.json(
      { error: "type is required and must be one of: standard, minimal, transient" },
      400
    );
  }

  const client = await getClient(c.env);
  try {
    const result = await client.query(
      `INSERT INTO banner (title, subtitle, image_url, url, type)
       VALUES ($1, $2, $3, $4, $5)
       RETURNING *`,
      [
        title ?? null,
        subtitle ?? null,
        image_url ?? null,
        url ?? null,
        type,
      ]
    );
    return c.json(result.rows[0], 201);
  } finally {
    await client.end();
  }
});

// GET /banners — List all banners
bannersRouter.get("/banners", async (c) => {
  const typeFilter = c.req.query("type");
  const activeOnly = c.req.query("active") !== "false";

  const client = await getClient(c.env);
  try {
    let query = "SELECT * FROM banner WHERE 1=1";
    const params: unknown[] = [];

    if (activeOnly) {
      params.push(true);
      query += ` AND is_active = $${params.length}`;
    }

    if (typeFilter && VALID_BANNER_TYPES.includes(typeFilter as any)) {
      params.push(typeFilter);
      query += ` AND type = $${params.length}`;
    }

    query += " ORDER BY created_at DESC";

    const result = await client.query(query, params);
    return c.json(result.rows, 200);
  } finally {
    await client.end();
  }
});

// GET /banners/:id — Get a single banner
bannersRouter.get("/banners/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const result = await client.query("SELECT * FROM banner WHERE id = $1", [id]);
    if (result.rows.length === 0) {
      return c.json({ error: "Banner not found" }, 404);
    }
    return c.json(result.rows[0], 200);
  } finally {
    await client.end();
  }
});

// PATCH /banners/:id — Update a banner
bannersRouter.patch("/banners/:id", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { title, subtitle, image_url, url, type, is_active } = body as Record<
    string,
    unknown
  >;

  if (type !== undefined && !VALID_BANNER_TYPES.includes(type as any)) {
    return c.json(
      { error: "type must be one of: standard, minimal, transient" },
      400
    );
  }

  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    // Check banner exists
    const existing = await client.query("SELECT id FROM banner WHERE id = $1", [id]);
    if (existing.rows.length === 0) {
      return c.json({ error: "Banner not found" }, 404);
    }

    // Build dynamic SET clause
    const setClauses: string[] = [];
    const params: unknown[] = [];

    if (title !== undefined) {
      params.push(title);
      setClauses.push(`title = $${params.length}`);
    }
    if (subtitle !== undefined) {
      params.push(subtitle);
      setClauses.push(`subtitle = $${params.length}`);
    }
    if (image_url !== undefined) {
      params.push(image_url);
      setClauses.push(`image_url = $${params.length}`);
    }
    if (url !== undefined) {
      params.push(url);
      setClauses.push(`url = $${params.length}`);
    }
    if (type !== undefined) {
      params.push(type);
      setClauses.push(`type = $${params.length}`);
    }
    if (is_active !== undefined) {
      params.push(is_active);
      setClauses.push(`is_active = $${params.length}`);
    }

    if (setClauses.length === 0) {
      return c.json({ error: "No fields to update" }, 400);
    }

    params.push(id);
    const result = await client.query(
      `UPDATE banner SET ${setClauses.join(", ")} WHERE id = $${params.length} RETURNING *`,
      params
    );
    return c.json(result.rows[0], 200);
  } finally {
    await client.end();
  }
});

// DELETE /banners/:id — Delete a banner (cascades to user_banner assignments)
bannersRouter.delete("/banners/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "DELETE FROM banner WHERE id = $1 RETURNING id",
      [id]
    );
    if (result.rows.length === 0) {
      return c.json({ error: "Banner not found" }, 404);
    }
    return c.body(null, 204);
  } finally {
    await client.end();
  }
});

// --- User Banner Assignments ---

// POST /banners/:id/assign — Assign a banner to one or more users
bannersRouter.post("/banners/:id/assign", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const {
    user_uid,
    user_uids,
    max_expiration_date,
    first_shown_expiration_hours,
    display_order,
  } = body as Record<string, unknown>;

  // Accept either single user_uid or array user_uids
  const uids: string[] = [];
  if (Array.isArray(user_uids)) {
    for (const uid of user_uids) {
      if (typeof uid === "string" && uid.trim() !== "") {
        uids.push(uid.trim());
      }
    }
  } else if (typeof user_uid === "string" && user_uid.trim() !== "") {
    uids.push(user_uid.trim());
  }

  if (uids.length === 0) {
    return c.json({ error: "user_uid or user_uids is required" }, 400);
  }

  if (!max_expiration_date || typeof max_expiration_date !== "string") {
    return c.json({ error: "max_expiration_date is required (ISO 8601 timestamp)" }, 400);
  }

  const bannerId = c.req.param("id");
  const client = await getClient(c.env);
  try {
    // Check banner exists
    const bannerResult = await client.query(
      "SELECT id FROM banner WHERE id = $1",
      [bannerId]
    );
    if (bannerResult.rows.length === 0) {
      return c.json({ error: "Banner not found" }, 404);
    }

    const inserted: unknown[] = [];
    const skipped: string[] = [];

    for (const uid of uids) {
      const result = await client.query(
        `INSERT INTO user_banner (user_uid, banner_id, max_expiration_date, first_shown_expiration_hours, display_order)
         VALUES ($1, $2, $3, $4, $5)
         ON CONFLICT (user_uid, banner_id) DO NOTHING
         RETURNING *`,
        [
          uid,
          bannerId,
          max_expiration_date,
          first_shown_expiration_hours ?? null,
          display_order ?? null,
        ]
      );
      if (result.rows.length > 0) {
        inserted.push(result.rows[0]);
      } else {
        skipped.push(uid);
      }
    }

    return c.json({ inserted, skipped }, 201);
  } finally {
    await client.end();
  }
});

// GET /banners/user/:userUid — Get active banners for a user (with expiration logic)
bannersRouter.get("/banners/user/:userUid", async (c) => {
  const userUid = c.req.param("userUid");
  const typeFilter = c.req.query("type");

  const client = await getClient(c.env);
  try {
    // Fetch banners assigned to this user OR to 'all', applying full expiration logic
    let query = `
      SELECT
        ub.id,
        b.title,
        b.subtitle,
        b.image_url,
        b.url,
        b.type,
        ub.display_order,
        ub.first_shown_at,
        ub.max_expiration_date,
        ub.first_shown_expiration_hours
      FROM user_banner ub
      JOIN banner b ON b.id = ub.banner_id
      WHERE ub.user_uid IN ($1, 'all')
        AND b.is_active = true
        AND ub.is_dismissed = false
        AND NOW() <= ub.max_expiration_date
        AND (
          ub.first_shown_expiration_hours IS NULL
          OR ub.first_shown_at IS NULL
          OR NOW() <= ub.first_shown_at + (ub.first_shown_expiration_hours || ' hours')::interval
        )
    `;
    const params: unknown[] = [userUid];

    if (typeFilter && VALID_BANNER_TYPES.includes(typeFilter as any)) {
      params.push(typeFilter);
      query += ` AND b.type = $${params.length}`;
    }

    // Exclude global banners the user has personally dismissed
    query += `
      AND NOT EXISTS (
        SELECT 1 FROM user_banner ub_dismissed
        WHERE ub_dismissed.user_uid = $1
          AND ub_dismissed.banner_id = ub.banner_id
          AND ub_dismissed.is_dismissed = true
          AND ub.user_uid = 'all'
      )
    `;

    query += " ORDER BY ub.display_order DESC NULLS LAST, ub.created_at DESC";

    const result = await client.query(query, params);

    // Mark first_shown_at for banners that haven't been seen yet
    const unseenIds = result.rows
      .filter((row: any) => row.first_shown_at === null)
      .map((row: any) => row.id);

    if (unseenIds.length > 0) {
      await client.query(
        `UPDATE user_banner SET first_shown_at = NOW() WHERE id = ANY($1) AND first_shown_at IS NULL`,
        [unseenIds]
      );
    }

    // Format response grouped by type
    const banners = result.rows.map((row: any) => ({
      id: row.id,
      title: row.title,
      subtitle: row.subtitle,
      imageUrl: row.image_url,
      url: row.url,
      type: row.type,
    }));

    return c.json({
      banners: banners.filter((b: any) => b.type === "standard"),
      bannersMinimal: banners.filter((b: any) => b.type === "minimal"),
      bannersTransient: banners.filter((b: any) => b.type === "transient"),
    }, 200);
  } finally {
    await client.end();
  }
});

// POST /banners/user/:userUid/dismiss — Dismiss a banner for a user
bannersRouter.post("/banners/user/:userUid/dismiss", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { user_banner_id } = body as Record<string, unknown>;

  if (!user_banner_id || typeof user_banner_id !== "number") {
    return c.json({ error: "user_banner_id is required (number)" }, 400);
  }

  const userUid = c.req.param("userUid");
  const client = await getClient(c.env);
  try {
    // Check if this is a personal assignment — dismiss directly
    const result = await client.query(
      `UPDATE user_banner SET is_dismissed = true
       WHERE id = $1 AND user_uid = $2 AND is_dismissed = false
       RETURNING *`,
      [user_banner_id, userUid]
    );

    if (result.rows.length > 0) {
      return c.json({ dismissed: true }, 200);
    }

    // Check if this is a global banner (user_uid = 'all') — create a personal dismissed record
    const globalBanner = await client.query(
      `SELECT banner_id, max_expiration_date FROM user_banner WHERE id = $1 AND user_uid = 'all'`,
      [user_banner_id]
    );

    if (globalBanner.rows.length > 0) {
      const { banner_id, max_expiration_date } = globalBanner.rows[0];
      // Insert a dismissed personal record (or update if exists)
      await client.query(
        `INSERT INTO user_banner (user_uid, banner_id, max_expiration_date, is_dismissed)
         VALUES ($1, $2, $3, true)
         ON CONFLICT (user_uid, banner_id) DO UPDATE SET is_dismissed = true`,
        [userUid, banner_id, max_expiration_date]
      );
      return c.json({ dismissed: true }, 200);
    }

    return c.json({ error: "Banner assignment not found" }, 404);
  } finally {
    await client.end();
  }
});

// GET /banners/:id/assignments — List all assignments for a banner
bannersRouter.get("/banners/:id/assignments", async (c) => {
  const bannerId = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const bannerResult = await client.query(
      "SELECT id FROM banner WHERE id = $1",
      [bannerId]
    );
    if (bannerResult.rows.length === 0) {
      return c.json({ error: "Banner not found" }, 404);
    }

    const result = await client.query(
      "SELECT * FROM user_banner WHERE banner_id = $1 ORDER BY created_at DESC",
      [bannerId]
    );
    return c.json(result.rows, 200);
  } finally {
    await client.end();
  }
});
