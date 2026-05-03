import { Hono } from "hono";
import { getClient, query } from "../db";
import type { Env, CurriculumSeriesRow } from "../types";

const series = new Hono<{ Bindings: Env }>();

// List all series
series.get("/", async (c) => {
  const client = await getClient(c.env);
  try {
    const rows = await query<CurriculumSeriesRow>(
      client,
      `SELECT id, title, description, thumbnail, is_public, display_order, created_at
       FROM curriculum_series
       ORDER BY display_order DESC, title ASC`
    );
    return c.json(rows);
  } finally {
    await client.end();
  }
});

// Get single series
series.get("/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const rows = await query<CurriculumSeriesRow>(
      client,
      `SELECT id, title, description, thumbnail, is_public, display_order, created_at
       FROM curriculum_series WHERE id = $1`,
      [id]
    );
    if (rows.length === 0) {
      return c.json({ error: "Series not found" }, 404);
    }
    return c.json(rows[0]);
  } finally {
    await client.end();
  }
});

// Create series
series.post("/", async (c) => {
  const body = await c.req.json<{
    id: string;
    title: string;
    description?: string;
    thumbnail?: string;
    is_public?: boolean;
    display_order?: number;
  }>();

  if (!body.id || !body.title) {
    return c.json({ error: "id and title are required" }, 400);
  }

  const client = await getClient(c.env);
  try {
    const rows = await query<CurriculumSeriesRow>(
      client,
      `INSERT INTO curriculum_series (id, title, description, thumbnail, is_public, display_order)
       VALUES ($1, $2, $3, $4, $5, $6)
       RETURNING *`,
      [
        body.id,
        body.title,
        body.description ?? null,
        body.thumbnail ?? null,
        body.is_public ?? false,
        body.display_order ?? 0,
      ]
    );
    return c.json(rows[0], 201);
  } finally {
    await client.end();
  }
});

// Update series
series.put("/:id", async (c) => {
  const id = c.req.param("id");
  const body = await c.req.json<{
    title?: string;
    description?: string | null;
    thumbnail?: string | null;
    is_public?: boolean;
    display_order?: number;
  }>();

  const sets: string[] = [];
  const params: unknown[] = [];
  let idx = 1;

  if (body.title !== undefined) {
    sets.push(`title = $${idx++}`);
    params.push(body.title);
  }
  if (body.description !== undefined) {
    sets.push(`description = $${idx++}`);
    params.push(body.description);
  }
  if (body.thumbnail !== undefined) {
    sets.push(`thumbnail = $${idx++}`);
    params.push(body.thumbnail);
  }
  if (body.is_public !== undefined) {
    sets.push(`is_public = $${idx++}`);
    params.push(body.is_public);
  }
  if (body.display_order !== undefined) {
    sets.push(`display_order = $${idx++}`);
    params.push(body.display_order);
  }

  if (sets.length === 0) {
    return c.json({ error: "No fields to update" }, 400);
  }

  params.push(id);

  const client = await getClient(c.env);
  try {
    const rows = await query<CurriculumSeriesRow>(
      client,
      `UPDATE curriculum_series SET ${sets.join(", ")} WHERE id = $${idx} RETURNING *`,
      params
    );
    if (rows.length === 0) {
      return c.json({ error: "Series not found" }, 404);
    }
    return c.json(rows[0]);
  } finally {
    await client.end();
  }
});

// Delete series
series.delete("/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const rows = await query<{ id: string }>(
      client,
      `DELETE FROM curriculum_series WHERE id = $1 RETURNING id`,
      [id]
    );
    if (rows.length === 0) {
      return c.json({ error: "Series not found" }, 404);
    }
    return c.json({ deleted: true, id });
  } finally {
    await client.end();
  }
});

// Add curriculum to series
series.post("/:id/curriculums", async (c) => {
  const seriesId = c.req.param("id");
  const body = await c.req.json<{ curriculum_id: string }>();

  if (!body.curriculum_id) {
    return c.json({ error: "curriculum_id is required" }, 400);
  }

  const client = await getClient(c.env);
  try {
    await query(
      client,
      `INSERT INTO curriculum_series_items (curriculum_series_id, curriculum_id)
       VALUES ($1, $2) ON CONFLICT DO NOTHING`,
      [seriesId, body.curriculum_id]
    );
    return c.json({ added: true }, 201);
  } finally {
    await client.end();
  }
});

// Remove curriculum from series
series.delete("/:id/curriculums/:curriculumId", async (c) => {
  const seriesId = c.req.param("id");
  const curriculumId = c.req.param("curriculumId");
  const client = await getClient(c.env);
  try {
    await query(
      client,
      `DELETE FROM curriculum_series_items
       WHERE curriculum_series_id = $1 AND curriculum_id = $2`,
      [seriesId, curriculumId]
    );
    return c.json({ removed: true });
  } finally {
    await client.end();
  }
});

export default series;
