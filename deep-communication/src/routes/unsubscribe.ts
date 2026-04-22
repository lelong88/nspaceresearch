import { Hono } from "hono";
import type { Env } from "../types";
import { getClient } from "../db";

export const unsubscribeRouter = new Hono<{ Bindings: Env }>();

// GET /unsubscribe — Render unsubscribe form
unsubscribeRouter.get("/unsubscribe", async (c) => {
  const email = c.req.query("email");
  const listId = c.req.query("list_id");

  if (!email || !listId) {
    return c.html(
      "<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h1>Bad Request</h1><p>Missing email or list_id parameter.</p></body></html>",
      400
    );
  }

  const client = await getClient(c.env);

  try {
    const result = await client.query(
      "SELECT * FROM email_list_subscriber WHERE email = $1 AND email_list_id = $2",
      [email, listId]
    );

    const subscriberFound = result.rows.length > 0;

    const html = `<!DOCTYPE html>
<html>
<head>
  <title>Unsubscribe</title>
  <style>
    body { font-family: sans-serif; max-width: 480px; margin: 40px auto; padding: 0 20px; color: #333; }
    h1 { font-size: 1.4em; }
    p { line-height: 1.5; }
    button { display: block; width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; background: #f5f5f5; cursor: pointer; font-size: 1em; }
    button:hover { background: #e0e0e0; }
  </style>
</head>
<body>
  <h1>Unsubscribe</h1>
  <p>Email: <strong>${email}</strong></p>
${subscriberFound ? `  <form method="POST" action="/unsubscribe">
    <input type="hidden" name="email" value="${email}" />
    <input type="hidden" name="list_id" value="${listId}" />
    <input type="hidden" name="action" value="unsubscribe_list" />
    <button type="submit">Unsubscribe from this list</button>
  </form>` : ""}
  <form method="POST" action="/unsubscribe">
    <input type="hidden" name="email" value="${email}" />
    <input type="hidden" name="list_id" value="${listId}" />
    <input type="hidden" name="action" value="opt_out_global" />
    <button type="submit">Opt out from all emails</button>
  </form>
</body>
</html>`;

    return c.html(html, 200);
  } finally {
    await client.end();
  }
});

// POST /unsubscribe — Process unsubscribe form submission
unsubscribeRouter.post("/unsubscribe", async (c) => {
  const body = await c.req.parseBody();
  const email = body["email"] as string;
  const listId = body["list_id"] as string;
  const action = body["action"] as string;

  const client = await getClient(c.env);

  try {
    if (action === "unsubscribe_list") {
      await client.query(
        "UPDATE email_list_subscriber SET status = 'unsubscribed', unsubscribed_at = NOW() WHERE email = $1 AND email_list_id = $2",
        [email, listId]
      );

      const html = `<!DOCTYPE html>
<html>
<head>
  <title>Unsubscribed</title>
  <style>
    body { font-family: sans-serif; max-width: 480px; margin: 40px auto; padding: 0 20px; color: #333; }
    h1 { font-size: 1.4em; }
    p { line-height: 1.5; }
  </style>
</head>
<body>
  <h1>Unsubscribed</h1>
  <p>You have been unsubscribed from this list.</p>
</body>
</html>`;

      return c.html(html, 200);
    }

    if (action === "opt_out_global") {
      await client.query(
        "INSERT INTO email_opt_out (email, opted_out_at) VALUES ($1, NOW()) ON CONFLICT DO NOTHING",
        [email]
      );

      await client.query(
        "UPDATE email_list_subscriber SET status = 'unsubscribed', unsubscribed_at = NOW() WHERE email = $1",
        [email]
      );

      const html = `<!DOCTYPE html>
<html>
<head>
  <title>Opted Out</title>
  <style>
    body { font-family: sans-serif; max-width: 480px; margin: 40px auto; padding: 0 20px; color: #333; }
    h1 { font-size: 1.4em; }
    p { line-height: 1.5; }
  </style>
</head>
<body>
  <h1>Opted Out</h1>
  <p>You have been opted out from all emails.</p>
</body>
</html>`;

      return c.html(html, 200);
    }

    return c.html(
      "<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h1>Bad Request</h1><p>Invalid action.</p></body></html>",
      400
    );
  } finally {
    await client.end();
  }
});
