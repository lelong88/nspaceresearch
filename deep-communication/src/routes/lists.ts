import { Hono } from "hono";
import type { Env } from "../types";
import { getClient } from "../db";

export const listsRouter = new Hono<{ Bindings: Env }>();

// POST /lists — Create a new email list
listsRouter.post("/lists", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { name, description } = body as Record<string, unknown>;

  if (!name || typeof name !== "string" || name.trim() === "") {
    return c.json({ error: "Name is required" }, 400);
  }

  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "INSERT INTO email_list (name, description) VALUES ($1, $2) RETURNING *",
      [name, description ?? null]
    );
    return c.json(result.rows[0], 201);
  } finally {
    await client.end();
  }
});

// GET /lists — List all email lists
listsRouter.get("/lists", async (c) => {
  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "SELECT * FROM email_list ORDER BY id"
    );
    return c.json(result.rows, 200);
  } finally {
    await client.end();
  }
});

// GET /lists/:id — Get a single email list
listsRouter.get("/lists/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "SELECT * FROM email_list WHERE id = $1",
      [id]
    );
    if (result.rows.length === 0) {
      return c.json({ error: "List not found" }, 404);
    }
    return c.json(result.rows[0], 200);
  } finally {
    await client.end();
  }
});

// PUT /lists/:id — Update an email list
listsRouter.put("/lists/:id", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { name, description } = body as Record<string, unknown>;

  if (!name || typeof name !== "string" || name.trim() === "") {
    return c.json({ error: "Name is required" }, 400);
  }

  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "UPDATE email_list SET name = $1, description = $2, updated_at = NOW() WHERE id = $3 RETURNING *",
      [name, description ?? null, id]
    );
    if (result.rows.length === 0) {
      return c.json({ error: "List not found" }, 404);
    }
    return c.json(result.rows[0], 200);
  } finally {
    await client.end();
  }
});

// DELETE /lists/:id — Delete an email list
listsRouter.delete("/lists/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const result = await client.query(
      "DELETE FROM email_list WHERE id = $1",
      [id]
    );
    if (result.rowCount === 0) {
      return c.json({ error: "List not found" }, 404);
    }
    return c.body(null, 204);
  } finally {
    await client.end();
  }
});
