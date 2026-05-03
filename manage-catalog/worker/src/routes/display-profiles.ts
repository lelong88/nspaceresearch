import { Hono } from "hono";
import { getClient, query } from "../db";
import type { Env, DisplayProfileRow, DisplayOrderOverride } from "../types";

const displayProfiles = new Hono<{ Bindings: Env }>();

// List all display profiles
displayProfiles.get("/", async (c) => {
  const client = await getClient(c.env);
  try {
    const rows = await query<DisplayProfileRow>(
      client,
      `SELECT id, description, display_order_override, created_at
       FROM display_profile
       ORDER BY id ASC`
    );
    return c.json(rows);
  } finally {
    await client.end();
  }
});

// Get single display profile
displayProfiles.get("/:id", async (c) => {
  const id = parseInt(c.req.param("id"));
  if (isNaN(id)) {
    return c.json({ error: "Invalid id" }, 400);
  }

  const client = await getClient(c.env);
  try {
    const rows = await query<DisplayProfileRow>(
      client,
      `SELECT id, description, display_order_override, created_at
       FROM display_profile WHERE id = $1`,
      [id]
    );
    if (rows.length === 0) {
      return c.json({ error: "Display profile not found" }, 404);
    }
    return c.json(rows[0]);
  } finally {
    await client.end();
  }
});

// Create display profile
displayProfiles.post("/", async (c) => {
  const body = await c.req.json<{
    description: string;
    display_order_override?: DisplayOrderOverride;
  }>();

  if (!body.description) {
    return c.json({ error: "description is required" }, 400);
  }

  const client = await getClient(c.env);
  try {
    const rows = await query<DisplayProfileRow>(
      client,
      `INSERT INTO display_profile (description, display_order_override)
       VALUES ($1, $2)
       RETURNING *`,
      [body.description, JSON.stringify(body.display_order_override ?? {})]
    );
    return c.json(rows[0], 201);
  } finally {
    await client.end();
  }
});

// Update display profile
displayProfiles.put("/:id", async (c) => {
  const id = parseInt(c.req.param("id"));
  if (isNaN(id)) {
    return c.json({ error: "Invalid id" }, 400);
  }

  const body = await c.req.json<{
    description?: string;
    display_order_override?: DisplayOrderOverride;
  }>();

  const sets: string[] = [];
  const params: unknown[] = [];
  let idx = 1;

  if (body.description !== undefined) {
    sets.push(`description = $${idx++}`);
    params.push(body.description);
  }
  if (body.display_order_override !== undefined) {
    sets.push(`display_order_override = $${idx++}`);
    params.push(JSON.stringify(body.display_order_override));
  }

  if (sets.length === 0) {
    return c.json({ error: "No fields to update" }, 400);
  }

  params.push(id);

  const client = await getClient(c.env);
  try {
    const rows = await query<DisplayProfileRow>(
      client,
      `UPDATE display_profile SET ${sets.join(", ")} WHERE id = $${idx} RETURNING *`,
      params
    );
    if (rows.length === 0) {
      return c.json({ error: "Display profile not found" }, 404);
    }
    return c.json(rows[0]);
  } finally {
    await client.end();
  }
});

// Delete display profile
displayProfiles.delete("/:id", async (c) => {
  const id = parseInt(c.req.param("id"));
  if (isNaN(id)) {
    return c.json({ error: "Invalid id" }, 400);
  }

  const client = await getClient(c.env);
  try {
    const rows = await query<{ id: number }>(
      client,
      `DELETE FROM display_profile WHERE id = $1 RETURNING id`,
      [id]
    );
    if (rows.length === 0) {
      return c.json({ error: "Display profile not found" }, 404);
    }
    return c.json({ deleted: true, id });
  } finally {
    await client.end();
  }
});

export default displayProfiles;
