import type { MiddlewareHandler } from "hono";
import type { Env } from "../types";

export const corsMiddleware: MiddlewareHandler<{
  Bindings: Env;
}> = async (c, next) => {
  c.header("Access-Control-Allow-Origin", "*");
  c.header(
    "Access-Control-Allow-Methods",
    "GET, POST, PUT, DELETE, OPTIONS"
  );
  c.header("Access-Control-Allow-Headers", "Content-Type, X-API-Key");

  if (c.req.method === "OPTIONS") {
    return c.body(null, 204);
  }

  await next();
};
