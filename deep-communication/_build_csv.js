const API_URL = "https://email.step.is/api/query";
const API_KEY = "c92fc119fc254e3ef062382ea46d415441b99625eb8be3a36476355528a3c44e";

const SQL = `
SELECT u.email, u.name, u.created_at
FROM my_user u
WHERE u.email IS NOT NULL
  AND u.email != ''
  AND NOT EXISTS (
    SELECT 1 FROM engage e WHERE e.uid = u.uid
  )
  AND u.email NOT LIKE '%anonymous@nspace.is%'
  AND u.email NOT LIKE '%@privaterelay.appleid.com'
  AND u.email NOT LIKE '%@cloudtestlabaccounts.com'
  AND u.email NOT LIKE '%@nspace.is'
ORDER BY u.created_at DESC
`;

async function main() {
  console.log("Fetching unengaged users from worker...");

  const res = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-Key": API_KEY,
    },
    body: JSON.stringify({ sql: SQL }),
  });

  if (!res.ok) {
    const text = await res.text();
    console.error(`Error ${res.status}: ${text}`);
    process.exit(1);
  }

  const data = await res.json();
  const rows = data.rows;

  console.log(`Got ${rows.length} unengaged users (filtered)`);

  // Build CSV
  const header = "email,name,created_at";
  const csvRows = rows.map((r) => {
    const email = r.email || "";
    const name = (r.name || "").replace(/"/g, '""');
    const created = r.created_at || "";
    return `${email},"${name}",${created}`;
  });

  const csv = [header, ...csvRows].join("\n");

  const fs = require("fs");
  const filename = "unengaged_campaign_emails.csv";
  fs.writeFileSync(filename, csv, "utf-8");
  console.log(`Saved ${rows.length} emails to ${filename}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
