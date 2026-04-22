import { Hono } from "hono";
import type { Env } from "../types";
import { getClient } from "../db";

export const subscribersRouter = new Hono<{ Bindings: Env }>();

// POST /lists/:id/subscribers — Add a subscriber to a list
subscribersRouter.post("/lists/:id/subscribers", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { email } = body as Record<string, unknown>;

  if (!email || typeof email !== "string" || email.trim() === "") {
    return c.json({ error: "Email is required" }, 400);
  }

  const listId = c.req.param("id");
  const client = await getClient(c.env);
  try {
    // Check list exists
    const listResult = await client.query(
      "SELECT id FROM email_list WHERE id = $1",
      [listId]
    );
    if (listResult.rows.length === 0) {
      return c.json({ error: "List not found" }, 404);
    }

    // Check duplicate subscriber
    const dupResult = await client.query(
      "SELECT id FROM email_list_subscriber WHERE email = $1 AND email_list_id = $2",
      [email, listId]
    );
    if (dupResult.rows.length > 0) {
      return c.json({ error: "Email already subscribed to this list" }, 409);
    }

    // Check opt-out
    const optOutResult = await client.query(
      "SELECT id FROM email_opt_out WHERE email = $1",
      [email]
    );
    if (optOutResult.rows.length > 0) {
      return c.json({ error: "Email has globally opted out" }, 422);
    }

    // Insert subscriber
    const result = await client.query(
      "INSERT INTO email_list_subscriber (email, email_list_id, status, subscribed_at) VALUES ($1, $2, 'subscribed', NOW()) RETURNING *",
      [email, listId]
    );
    return c.json(result.rows[0], 201);
  } finally {
    await client.end();
  }
});

// GET /lists/:id/subscribers — List all subscribers for a list
subscribersRouter.get("/lists/:id/subscribers", async (c) => {
  const listId = c.req.param("id");
  const client = await getClient(c.env);
  try {
    // Check list exists
    const listResult = await client.query(
      "SELECT id FROM email_list WHERE id = $1",
      [listId]
    );
    if (listResult.rows.length === 0) {
      return c.json({ error: "List not found" }, 404);
    }

    const result = await client.query(
      "SELECT * FROM email_list_subscriber WHERE email_list_id = $1 ORDER BY id",
      [listId]
    );
    return c.json(result.rows, 200);
  } finally {
    await client.end();
  }
});

// POST /lists/:id/subscribers/bulk — Bulk add subscribers to a list
subscribersRouter.post("/lists/:id/subscribers/bulk", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { emails } = body as Record<string, unknown>;

  if (!Array.isArray(emails) || emails.length === 0) {
    return c.json({ error: "emails array is required" }, 400);
  }

  if (emails.length > 500) {
    return c.json({ error: "Maximum 500 emails per request" }, 400);
  }

  const validEmails = emails.filter(
    (e): e is string => typeof e === "string" && e.trim() !== ""
  );

  if (validEmails.length === 0) {
    return c.json({ error: "No valid emails provided" }, 400);
  }

  const listId = c.req.param("id");
  const client = await getClient(c.env);
  try {
    // Check list exists
    const listResult = await client.query(
      "SELECT id FROM email_list WHERE id = $1",
      [listId]
    );
    if (listResult.rows.length === 0) {
      return c.json({ error: "List not found" }, 404);
    }

    // Bulk insert, skip duplicates
    const placeholders = validEmails
      .map((_, idx) => `($${idx + 1}, ${parseInt(listId)}, 'subscribed', NOW())`)
      .join(", ");

    const sql = `INSERT INTO email_list_subscriber (email, email_list_id, status, subscribed_at)
VALUES ${placeholders}
ON CONFLICT (email, email_list_id) DO NOTHING`;

    const result = await client.query(sql, validEmails);

    return c.json(
      { inserted: result.rowCount, total: validEmails.length },
      201
    );
  } finally {
    await client.end();
  }
});

// DELETE /lists/:id/subscribers/:subscriberId — Remove a subscriber
subscribersRouter.delete("/lists/:id/subscribers/:subscriberId", async (c) => {
  const listId = c.req.param("id");
  const subscriberId = c.req.param("subscriberId");
  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "DELETE FROM email_list_subscriber WHERE id = $1 AND email_list_id = $2",
      [subscriberId, listId]
    );
    if (result.rowCount === 0) {
      return c.json({ error: "Subscriber not found" }, 404);
    }
    return c.body(null, 204);
  } finally {
    await client.end();
  }
});
