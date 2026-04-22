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
