// Creates a new subscriber list and bulk-inserts subscribers from a CSV file.
// Usage: node _create_list_from_csv.js

const API_URL = "https://email-workers.long-8d8.workers.dev/api";
const API_KEY = "c92fc119fc254e3ef062382ea46d415441b99625eb8be3a36476355528a3c44e";
const LIST_NAME = "NSpace Users Not In Step";
const CSV_FILE = "unengaged_vn.csv";

const fs = require("fs");

async function apiFetch(path, body) {
  const res = await fetch(`${API_URL}${path}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-Key": API_KEY,
    },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`${res.status} ${path}: ${text}`);
  }
  return res.json();
}

async function main() {
  // Parse CSV
  const csv = fs.readFileSync(CSV_FILE, "utf-8");
  const lines = csv.trim().split("\n");
  const emails = lines
    .slice(1)
    .map((line) => line.split(",")[0].trim())
    .filter((e) => e.length > 0);

  console.log(`Parsed ${emails.length} emails from ${CSV_FILE}`);

  // Create the list
  const list = await apiFetch("/lists", { name: LIST_NAME });
  console.log(`Created list "${list.name}" with id ${list.id}`);

  // Bulk insert in batches of 500
  const BATCH_SIZE = 500;
  let totalInserted = 0;

  for (let i = 0; i < emails.length; i += BATCH_SIZE) {
    const batch = emails.slice(i, i + BATCH_SIZE);
    const result = await apiFetch(`/lists/${list.id}/subscribers/bulk`, {
      emails: batch,
    });
    totalInserted += result.inserted;
    console.log(
      `Batch ${Math.floor(i / BATCH_SIZE) + 1}: inserted ${result.inserted}/${result.total} (total: ${totalInserted}/${emails.length})`
    );
  }

  console.log(`\nDone! Added ${totalInserted} subscribers to list "${LIST_NAME}" (id: ${list.id})`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
