// Usage: echo '<json>' | node _append_batch.js
const fs = require('fs');
let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => { input += chunk; });
process.stdin.on('end', () => {
  const data = JSON.parse(input);
  if (data[0] && data[0].csv_data) {
    fs.appendFileSync('email_campaign_unengaged_users.csv', data[0].csv_data + '\n');
    const lines = data[0].csv_data.split('\n').length;
    console.log(`Appended ${lines} rows`);
  }
});
