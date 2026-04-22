import { Hono } from "hono";
import type { Env } from "./types";
import { DatabaseConnectionError } from "./db";
import { corsMiddleware } from "./middleware/cors";
import { authMiddleware } from "./middleware/auth";
import { listsRouter } from "./routes/lists";
import { subscribersRouter } from "./routes/subscribers";
import { campaignsRouter } from "./routes/campaigns";
import { sendsRouter } from "./routes/sends";
import { queryRouter } from "./routes/query";
import { viewRouter } from "./routes/view";
import { unsubscribeRouter } from "./routes/unsubscribe";

const app = new Hono<{ Bindings: Env }>();

// CORS middleware on all routes
app.use("*", corsMiddleware);

// API key auth middleware on /api/* routes only
app.use("/api/*", authMiddleware);

// API route groups
app.route("/api", listsRouter);
app.route("/api", subscribersRouter);
app.route("/api", campaignsRouter);
app.route("/api", sendsRouter);
app.route("/api", queryRouter);

// Public route groups
app.route("/", viewRouter);
app.route("/", unsubscribeRouter);

// Global error handler
app.onError((err, c) => {
  const isApiRoute = c.req.path.startsWith("/api/");

  if (err instanceof DatabaseConnectionError) {
    if (isApiRoute) {
      return c.json({ error: "Service unavailable" }, 503);
    }
    return c.html(
      '<!DOCTYPE html><html><head><title>Service Unavailable</title></head><body><h1>Service Unavailable</h1></body></html>',
      503
    );
  }

  if (isApiRoute) {
    return c.json({ error: "Internal server error" }, 500);
  }

  return c.html(
    '<!DOCTYPE html><html><head><title>Error</title></head><body><h1>Something went wrong</h1></body></html>',
    500
  );
});

// Not-found handler
app.notFound((c) => {
  const isApiRoute = c.req.path.startsWith("/api/");

  if (isApiRoute) {
    return c.json({ error: "Not found" }, 404);
  }

  return c.html(
    '<!DOCTYPE html><html><head><title>Not Found</title></head><body><h1>Page not found</h1></body></html>',
    404
  );
});

export default app;
