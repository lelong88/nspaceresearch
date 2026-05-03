import { Hono } from "hono";
import { getClient, query } from "../db";
import type { Env, CurriculumCollectionRow } from "../types";

const collections = new Hono<{ Bindings: Env }>();

// List all collections
collections.get("/", async (c) => {
  const client = await getClient(c.env);
  try {
    const rows = await query<CurriculumCollectionRow>(
      client,
      `SELECT id, title, description, is_public, thumbnail, display_order, created_at
       FROM curriculum_collections
       ORDER BY display_order DESC, title ASC`
    );
    return c.json(rows);
  } finally {
    await client.end();
  }
});

// Get single collection
collections.get("/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const rows = await query<CurriculumCollectionRow>(
      client,
      `SELECT id, title, description, is_public, thumbnail, display_order, created_at
       FROM curriculum_collections WHERE id = $1`,
      [id]
    );
    if (rows.length === 0) {
      return c.json({ error: "Collection not found" }, 404);
    }
    return c.json(rows[0]);
  } finally {
    await client.end();
  }
});

// Create collection
collections.post("/", async (c) => {
  const body = await c.req.json<{
    id: string;
    title: string;
    description?: string;
    is_public?: boolean;
    thumbnail?: string;
  }>();

  if (!body.id || !body.title) {
    return c.json({ error: "id and title are required" }, 400);
  }

  const client = await getClient(c.env);
  try {
    const rows = await query<CurriculumCollectionRow>(
      client,
      `INSERT INTO curriculum_collections (id, title, description, is_public, thumbnail)
       VALUES ($1, $2, $3, $4, $5)
       RETURNING *`,
      [body.id, body.title, body.description ?? null, body.is_public ?? false, body.thumbnail ?? null]
    );
    return c.json(rows[0], 201);
  } finally {
    await client.end();
  }
});

// Update collection
collections.put("/:id", async (c) => {
  const id = c.req.param("id");
  const body = await c.req.json<{
    title?: string;
    description?: string | null;
    is_public?: boolean;
    thumbnail?: string | null;
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
  if (body.is_public !== undefined) {
    sets.push(`is_public = $${idx++}`);
    params.push(body.is_public);
  }
  if (body.thumbnail !== undefined) {
    sets.push(`thumbnail = $${idx++}`);
    params.push(body.thumbnail);
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
    const rows = await query<CurriculumCollectionRow>(
      client,
      `UPDATE curriculum_collections SET ${sets.join(", ")} WHERE id = $${idx} RETURNING *`,
      params
    );
    if (rows.length === 0) {
      return c.json({ error: "Collection not found" }, 404);
    }
    return c.json(rows[0]);
  } finally {
    await client.end();
  }
});

// Delete collection
collections.delete("/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const rows = await query<{ id: string }>(
      client,
      `DELETE FROM curriculum_collections WHERE id = $1 RETURNING id`,
      [id]
    );
    if (rows.length === 0) {
      return c.json({ error: "Collection not found" }, 404);
    }
    return c.json({ deleted: true, id });
  } finally {
    await client.end();
  }
});

// Add curriculum to collection
collections.post("/:id/curriculums", async (c) => {
  const collectionId = c.req.param("id");
  const body = await c.req.json<{ curriculum_id: string }>();

  if (!body.curriculum_id) {
    return c.json({ error: "curriculum_id is required" }, 400);
  }

  const client = await getClient(c.env);
  try {
    await query(
      client,
      `INSERT INTO curriculum_collection_items (curriculum_collection_id, curriculum_id)
       VALUES ($1, $2) ON CONFLICT DO NOTHING`,
      [collectionId, body.curriculum_id]
    );
    return c.json({ added: true }, 201);
  } finally {
    await client.end();
  }
});

// Remove curriculum from collection
collections.delete("/:id/curriculums/:curriculumId", async (c) => {
  const collectionId = c.req.param("id");
  const curriculumId = c.req.param("curriculumId");
  const client = await getClient(c.env);
  try {
    await query(
      client,
      `DELETE FROM curriculum_collection_items
       WHERE curriculum_collection_id = $1 AND curriculum_id = $2`,
      [collectionId, curriculumId]
    );
    return c.json({ removed: true });
  } finally {
    await client.end();
  }
});

// Add series to collection
collections.post("/:id/series", async (c) => {
  const collectionId = c.req.param("id");
  const body = await c.req.json<{ series_id: string }>();

  if (!body.series_id) {
    return c.json({ error: "series_id is required" }, 400);
  }

  const client = await getClient(c.env);
  try {
    await query(
      client,
      `INSERT INTO curriculum_collection_series (curriculum_collection_id, curriculum_series_id)
       VALUES ($1, $2) ON CONFLICT DO NOTHING`,
      [collectionId, body.series_id]
    );
    return c.json({ added: true }, 201);
  } finally {
    await client.end();
  }
});

// Remove series from collection
collections.delete("/:id/series/:seriesId", async (c) => {
  const collectionId = c.req.param("id");
  const seriesId = c.req.param("seriesId");
  const client = await getClient(c.env);
  try {
    await query(
      client,
      `DELETE FROM curriculum_collection_series
       WHERE curriculum_collection_id = $1 AND curriculum_series_id = $2`,
      [collectionId, seriesId]
    );
    return c.json({ removed: true });
  } finally {
    await client.end();
  }
});

export default collections;
