import { Hono } from "hono";
import { cors } from "hono/cors";
import type { Env } from "./types";
import collections from "./routes/collections";
import series from "./routes/series";
import curriculums from "./routes/curriculums";
import displayProfiles from "./routes/display-profiles";
import catalog from "./routes/catalog";

const app = new Hono<{ Bindings: Env }>();

const API_KEY = "sk-catalog-9f7b2a1e4d6c8x3w5q0m";

// Middleware
app.use("*", cors());

// API key auth — skip health check only
app.use("*", async (c, next) => {
  if (c.req.path === "/") return next();

  const key = c.req.header("X-API-Key");
  if (!key || key !== API_KEY) {
    return c.json({ error: "Unauthorized" }, 401);
  }
  return next();
});

// Health check
app.get("/", (c) => {
  return c.json({ status: "ok", service: "agentapi.step.is" });
});

// Routes
app.route("/collections", collections);
app.route("/series", series);
app.route("/curriculums", curriculums);
app.route("/display-profiles", displayProfiles);
app.route("/catalog", catalog);

// 404 fallback
app.notFound((c) => {
  return c.json({ error: "Not found" }, 404);
});

// Error handler
app.onError((err, c) => {
  console.error("Unhandled error:", err);
  return c.json({ error: "Internal server error" }, 500);
});

export default app;
