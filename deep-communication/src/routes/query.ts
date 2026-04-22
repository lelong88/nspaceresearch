import { Hono } from "hono";
import type { Env } from "../types";
import { getClient } from "../db";

export const queryRouter = new Hono<{ Bindings: Env }>();

// POST /query — Run a read-only SQL query
queryRouter.post("/query", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { sql } = body as Record<string, unknown>;

  if (!sql || typeof sql !== "string" || sql.trim() === "") {
    return c.json({ error: "sql is required" }, 400);
  }

  // Block anything that isn't a SELECT / WITH (CTE) statement
  const normalized = sql.trim().toUpperCase();
  const isReadOnly =
    normalized.startsWith("SELECT") ||
    normalized.startsWith("WITH") ||
    normalized.startsWith("EXPLAIN");

  if (!isReadOnly) {
    return c.json({ error: "Only read-only queries (SELECT/WITH/EXPLAIN) are allowed" }, 403);
  }

  const client = await getClient(c.env);
  try {
    const result = await client.query(sql);
    return c.json(
      {
        rows: result.rows,
        rowCount: result.rowCount,
        fields: result.fields.map((f) => f.name),
      },
      200
    );
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Query failed";
    return c.json({ error: message }, 400);
  } finally {
    await client.end();
  }
});
