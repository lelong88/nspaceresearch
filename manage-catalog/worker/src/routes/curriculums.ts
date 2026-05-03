import { Hono } from "hono";
import { getClient, query } from "../db";
import type { Env, CurriculumRow } from "../types";

const curriculums = new Hono<{ Bindings: Env }>();

// List curriculums (lightweight, no content field)
curriculums.get("/", async (c) => {
  const limit = parseInt(c.req.query("limit") ?? "50");
  const offset = parseInt(c.req.query("offset") ?? "0");
  const language = c.req.query("language");

  let sql = `SELECT id, uid, language, user_language, is_public, price, list_price, display_order, is_disabled, created_at
             FROM curriculum`;
  const params: unknown[] = [];
  let idx = 1;

  if (language) {
    sql += ` WHERE language = $${idx++}`;
    params.push(language);
  }

  sql += ` ORDER BY display_order DESC, created_at DESC LIMIT $${idx++} OFFSET $${idx++}`;
  params.push(limit, offset);

  const client = await getClient(c.env);
  try {
    const rows = await query<Omit<CurriculumRow, "content" | "instruction">>(client, sql, params);
    return c.json(rows);
  } finally {
    await client.end();
  }
});

// Get single curriculum (full content)
curriculums.get("/:id", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const rows = await query<CurriculumRow>(
      client,
      `SELECT * FROM curriculum WHERE id = $1`,
      [id]
    );
    if (rows.length === 0) {
      return c.json({ error: "Curriculum not found" }, 404);
    }
    return c.json(rows[0]);
  } finally {
    await client.end();
  }
});

// Update curriculum
curriculums.put("/:id", async (c) => {
  const id = c.req.param("id");
  const body = await c.req.json<{
    language?: string;
    user_language?: string;
    content?: unknown;
    instruction?: string | null;
    is_public?: boolean;
    price?: number;
    list_price?: number | null;
    display_order?: number;
    is_disabled?: boolean | null;
  }>();

  const sets: string[] = [];
  const params: unknown[] = [];
  let idx = 1;

  if (body.language !== undefined) {
    sets.push(`language = $${idx++}`);
    params.push(body.language);
  }
  if (body.user_language !== undefined) {
    sets.push(`user_language = $${idx++}`);
    params.push(body.user_language);
  }
  if (body.content !== undefined) {
    sets.push(`content = $${idx++}`);
    params.push(JSON.stringify(body.content));
  }
  if (body.instruction !== undefined) {
    sets.push(`instruction = $${idx++}`);
    params.push(body.instruction);
  }
  if (body.is_public !== undefined) {
    sets.push(`is_public = $${idx++}`);
    params.push(body.is_public);
  }
  if (body.price !== undefined) {
    sets.push(`price = $${idx++}`);
    params.push(body.price);
  }
  if (body.list_price !== undefined) {
    sets.push(`list_price = $${idx++}`);
    params.push(body.list_price);
  }
  if (body.display_order !== undefined) {
    sets.push(`display_order = $${idx++}`);
    params.push(body.display_order);
  }
  if (body.is_disabled !== undefined) {
    sets.push(`is_disabled = $${idx++}`);
    params.push(body.is_disabled);
  }

  if (sets.length === 0) {
    return c.json({ error: "No fields to update" }, 400);
  }

  params.push(id);

  const client = await getClient(c.env);
  try {
    const rows = await query<CurriculumRow>(
      client,
      `UPDATE curriculum SET ${sets.join(", ")} WHERE id = $${idx} RETURNING *`,
      params
    );
    if (rows.length === 0) {
      return c.json({ error: "Curriculum not found" }, 404);
    }
    return c.json(rows[0]);
  } finally {
    await client.end();
  }
});

export default curriculums;
