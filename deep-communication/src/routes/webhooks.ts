import { Hono } from "hono";
import type { Env } from "../types";
import { getClient } from "../db";

export const webhooksRouter = new Hono<{ Bindings: Env }>();

/**
 * POST /webhooks/ses — Receive SES bounce/complaint/delivery notifications via SNS.
 *
 * SNS sends three types of requests:
 *   1. SubscriptionConfirmation — we must GET the SubscribeURL to confirm
 *   2. Notification — contains the SES event (bounce, complaint, delivery)
 *   3. UnsubscribeConfirmation — acknowledgement
 *
 * For bounces, we update email_campaign_send.bounced_at and status = 'bounced'.
 * For complaints, we also mark bounced_at (treat complaints like bounces for safety).
 */
webhooksRouter.post("/webhooks/ses", async (c) => {
  let payload: Record<string, unknown>;
  try {
    // SNS sends with Content-Type: text/plain, so we parse the raw text as JSON
    const raw = await c.req.text();
    payload = JSON.parse(raw);
  } catch {
    return c.json({ error: "Invalid JSON" }, 400);
  }

  const messageType = c.req.header("x-amz-sns-message-type") || (payload.Type as string);

  // 1. Subscription confirmation — auto-confirm by fetching the SubscribeURL
  if (messageType === "SubscriptionConfirmation") {
    const subscribeUrl = payload.SubscribeURL as string;
    if (subscribeUrl) {
      try {
        await fetch(subscribeUrl);
      } catch {
        // Log but don't fail — SNS will retry
      }
    }
    return c.json({ status: "subscription confirmed" }, 200);
  }

  // 2. Unsubscribe confirmation — just acknowledge
  if (messageType === "UnsubscribeConfirmation") {
    return c.json({ status: "ok" }, 200);
  }

  // 3. Notification — parse the SES event
  if (messageType === "Notification") {
    let message: Record<string, unknown>;
    try {
      message = JSON.parse(payload.Message as string);
    } catch {
      return c.json({ error: "Invalid Message JSON" }, 400);
    }

    const notificationType = message.notificationType as string;

    if (notificationType === "Bounce") {
      const bounce = message.bounce as Record<string, unknown>;
      const bouncedRecipients = bounce?.bouncedRecipients as Array<{ emailAddress: string }>;
      if (bouncedRecipients && bouncedRecipients.length > 0) {
        await markBounced(c.env, bouncedRecipients.map((r) => r.emailAddress.toLowerCase()));
      }
    } else if (notificationType === "Complaint") {
      const complaint = message.complaint as Record<string, unknown>;
      const complainedRecipients = complaint?.complainedRecipients as Array<{ emailAddress: string }>;
      if (complainedRecipients && complainedRecipients.length > 0) {
        await markBounced(c.env, complainedRecipients.map((r) => r.emailAddress.toLowerCase()));
      }
    }
    // Delivery notifications — no action needed (could update delivered_at in the future)

    return c.json({ status: "processed" }, 200);
  }

  return c.json({ status: "ignored" }, 200);
});

/**
 * Mark one or more email addresses as bounced across ALL their send records.
 * Sets bounced_at = NOW() and status = 'bounced' where not already bounced.
 */
async function markBounced(env: Env, emails: string[]): Promise<void> {
  if (emails.length === 0) return;

  const client = await getClient(env);
  try {
    // Use ANY($1::text[]) to match multiple emails in one query
    await client.query(
      `UPDATE email_campaign_send
       SET bounced_at = NOW(), status = 'bounced'
       WHERE LOWER(email) = ANY($1::text[])
         AND bounced_at IS NULL`,
      [emails]
    );
  } finally {
    await client.end();
  }
}
