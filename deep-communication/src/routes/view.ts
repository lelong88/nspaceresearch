import { Hono } from "hono";
import type { Env } from "../types";
import { getClient } from "../db";

export const viewRouter = new Hono<{ Bindings: Env }>();

// GET /view/:campaignId — Render campaign HTML for browser viewing
viewRouter.get("/view/:campaignId", async (c) => {
  const campaignId = c.req.param("campaignId");
  const client = await getClient(c.env);

  try {
    const result = await client.query(
      "SELECT * FROM email_campaign WHERE id = $1",
      [campaignId]
    );

    if (result.rows.length === 0) {
      return c.html(
        "<!DOCTYPE html><html><head><title>Not Found</title></head><body><h1>Campaign not found</h1></body></html>",
        404
      );
    }

    const campaign = result.rows[0];
    const listId = campaign.email_list_id ?? "";
    const unsubscribeLink = `<div style="text-align:center;padding:20px;font-size:12px;color:#666;"><a href="/unsubscribe?email=RECIPIENT&list_id=${listId}">Unsubscribe</a></div>`;

    if (campaign.body_html) {
      // Inject unsubscribe link before closing </body> tag, or append if no </body>
      let html: string = campaign.body_html;
      if (html.includes("</body>")) {
        html = html.replace("</body>", `${unsubscribeLink}</body>`);
      } else {
        html = html + unsubscribeLink;
      }
      return c.html(html, 200);
    }

    if (campaign.body_text) {
      const html = `<!DOCTYPE html><html><head><title>${campaign.subject}</title></head><body><pre>${campaign.body_text}</pre>${unsubscribeLink}</body></html>`;
      return c.html(html, 200);
    }

    // No content at all — return empty HTML with unsubscribe link
    const html = `<!DOCTYPE html><html><head><title>${campaign.subject}</title></head><body>${unsubscribeLink}</body></html>`;
    return c.html(html, 200);
  } finally {
    await client.end();
  }
});
