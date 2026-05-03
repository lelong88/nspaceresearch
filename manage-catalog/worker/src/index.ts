import { Hono } from "hono";
import { cors } from "hono/cors";
import type { Env } from "./types";
import collections from "./routes/collections";
import series from "./routes/series";
import curriculums from "./routes/curriculums";
import displayProfiles from "./routes/display-profiles";
import catalog from "./routes/catalog";

const app = new Hono<{ Bindings: Env }>();

// Middleware
app.use("*", cors());

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
