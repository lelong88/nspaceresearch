import { Hono } from "hono";
import type { Env } from "../types";
import { getClient } from "../db";

export const campaignsRouter = new Hono<{ Bindings: Env }>();

// POST /campaigns — Create a new campaign
campaignsRouter.post("/campaigns", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { name, subject, body_html, body_text, email_list_id, scheduled_at } =
    body as Record<string, unknown>;

  if (!name || typeof name !== "string" || name.trim() === "") {
    return c.json({ error: "Name is required" }, 400);
  }

  if (!subject || typeof subject !== "string" || subject.trim() === "") {
    return c.json({ error: "Subject is required" }, 400);
  }

  const client = await getClient(c.env);
  try {
    // Validate email_list_id exists if provided
    if (email_list_id != null) {
      const listResult = await client.query(
        "SELECT id FROM email_list WHERE id = $1",
        [email_list_id]
      );
      if (listResult.rows.length === 0) {
        return c.json({ error: "Email list not found" }, 422);
      }
    }

    const result = await client.query(
      "INSERT INTO email_campaign (name, subject, body_html, body_text, email_list_id, status, scheduled_at) VALUES ($1, $2, $3, $4, $5, 'draft', $6) RETURNING *",
      [
        name,
        subject,
        body_html ?? null,
        body_text ?? null,
        email_list_id ?? null,
        scheduled_at ?? null,
      ]
    );
    return c.json(result.rows[0], 201);
  } finally {
    await client.end();
  }
});

// GET /campaigns — List all campaigns
campaignsRouter.get("/campaigns", async (c) => {
  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "SELECT * FROM email_campaign ORDER BY id"
    );
    return c.json(result.rows, 200);
  } finally {
    await client.end();
  }
});

// GET /campaigns/:id — Get a single campaign
campaignsRouter.get("/campaigns/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "SELECT * FROM email_campaign WHERE id = $1",
      [id]
    );
    if (result.rows.length === 0) {
      return c.json({ error: "Campaign not found" }, 404);
    }
    return c.json(result.rows[0], 200);
  } finally {
    await client.end();
  }
});

// PUT /campaigns/:id — Update a campaign
campaignsRouter.put("/campaigns/:id", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { name, subject, body_html, body_text, email_list_id, scheduled_at } =
    body as Record<string, unknown>;

  if (!name || typeof name !== "string" || name.trim() === "") {
    return c.json({ error: "Name is required" }, 400);
  }

  if (!subject || typeof subject !== "string" || subject.trim() === "") {
    return c.json({ error: "Subject is required" }, 400);
  }

  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    // Validate email_list_id exists if provided
    if (email_list_id != null) {
      const listResult = await client.query(
        "SELECT id FROM email_list WHERE id = $1",
        [email_list_id]
      );
      if (listResult.rows.length === 0) {
        return c.json({ error: "Email list not found" }, 422);
      }
    }

    const result = await client.query(
      "UPDATE email_campaign SET name = $1, subject = $2, body_html = $3, body_text = $4, email_list_id = $5, scheduled_at = $6, updated_at = NOW() WHERE id = $7 RETURNING *",
      [
        name,
        subject,
        body_html ?? null,
        body_text ?? null,
        email_list_id ?? null,
        scheduled_at ?? null,
        id,
      ]
    );
    if (result.rows.length === 0) {
      return c.json({ error: "Campaign not found" }, 404);
    }
    return c.json(result.rows[0], 200);
  } finally {
    await client.end();
  }
});

// DELETE /campaigns/:id — Delete a campaign
campaignsRouter.delete("/campaigns/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "DELETE FROM email_campaign WHERE id = $1",
      [id]
    );
    if (result.rowCount === 0) {
      return c.json({ error: "Campaign not found" }, 404);
    }
    return c.body(null, 204);
  } finally {
    await client.end();
  }
});
