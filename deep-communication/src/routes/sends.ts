import { Hono } from "hono";
import type { Env } from "../types";
import { getClient } from "../db";

export const sendsRouter = new Hono<{ Bindings: Env }>();

// GET /campaigns/:id/sends — List all sends for a campaign
sendsRouter.get("/campaigns/:id/sends", async (c) => {
  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    // Check campaign exists
    const campaignResult = await client.query(
      "SELECT id FROM email_campaign WHERE id = $1",
      [id]
    );
    if (campaignResult.rows.length === 0) {
      return c.json({ error: "Campaign not found" }, 404);
    }

    const result = await client.query(
      "SELECT * FROM email_campaign_send WHERE email_campaign_id = $1 ORDER BY id",
      [id]
    );
    return c.json(result.rows, 200);
  } finally {
    await client.end();
  }
});

// GET /campaigns/:id/sends/:sendId — Get a single send
sendsRouter.get("/campaigns/:id/sends/:sendId", async (c) => {
  const id = c.req.param("id");
  const sendId = c.req.param("sendId");
  const client = await getClient(c.env);
  try {
    // Check campaign exists
    const campaignResult = await client.query(
      "SELECT id FROM email_campaign WHERE id = $1",
      [id]
    );
    if (campaignResult.rows.length === 0) {
      return c.json({ error: "Campaign not found" }, 404);
    }

    const result = await client.query(
      "SELECT * FROM email_campaign_send WHERE id = $1 AND email_campaign_id = $2",
      [sendId, id]
    );
    if (result.rows.length === 0) {
      return c.json({ error: "Send not found" }, 404);
    }
    return c.json(result.rows[0], 200);
  } finally {
    await client.end();
  }
});

// POST /campaigns/:id/sends — Record a send (idempotent per campaign+email)
sendsRouter.post("/campaigns/:id/sends", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const { email, status, view_url } = body as Record<string, unknown>;

  if (!email || typeof email !== "string" || email.trim() === "") {
    return c.json({ error: "email is required" }, 400);
  }

  const finalStatus =
    typeof status === "string" && status.trim() !== "" ? status : "sent";
  const finalViewUrl =
    typeof view_url === "string" && view_url.trim() !== "" ? view_url : null;

  const id = c.req.param("id");
  const client = await getClient(c.env);
  try {
    const campaignResult = await client.query(
      "SELECT id FROM email_campaign WHERE id = $1",
      [id]
    );
    if (campaignResult.rows.length === 0) {
      return c.json({ error: "Campaign not found" }, 404);
    }

    // Dedupe on (campaign, email) via unique constraint.
    // ON CONFLICT DO NOTHING returns an empty row set if the send already exists.
    const result = await client.query(
      `INSERT INTO email_campaign_send (email_campaign_id, email, status, view_url, sent_at)
       VALUES ($1, $2, $3, $4, NOW())
       ON CONFLICT (email_campaign_id, email) DO NOTHING
       RETURNING *`,
      [id, email, finalStatus, finalViewUrl]
    );

    if (result.rows.length === 0) {
      // Already sent — fetch and return the existing record
      const existing = await client.query(
        "SELECT * FROM email_campaign_send WHERE email_campaign_id = $1 AND email = $2",
        [id, email]
      );
      return c.json({ ...existing.rows[0], already_sent: true }, 200);
    }

    return c.json(result.rows[0], 201);
  } finally {
    await client.end();
  }
});
