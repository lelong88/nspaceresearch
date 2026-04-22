import type { MiddlewareHandler } from "hono";
import type { Env } from "../types";

async function constantTimeEqual(a: string, b: string): Promise<boolean> {
  const encoder = new TextEncoder();
  const key = (await crypto.subtle.generateKey(
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  )) as CryptoKey;

  const [digestA, digestB] = await Promise.all([
    crypto.subtle.sign("HMAC", key, encoder.encode(a)),
    crypto.subtle.sign("HMAC", key, encoder.encode(b)),
  ]);

  return crypto.subtle.timingSafeEqual(digestA, digestB);
}

export const authMiddleware: MiddlewareHandler<{
  Bindings: Env;
}> = async (c, next) => {
  const apiKey = c.req.header("X-API-Key");

  if (!apiKey) {
    return c.json({ error: "Missing API key" }, 401);
  }

  const isValid = await constantTimeEqual(apiKey, c.env.API_KEY);

  if (!isValid) {
    return c.json({ error: "Invalid API key" }, 403);
  }

  await next();
};
