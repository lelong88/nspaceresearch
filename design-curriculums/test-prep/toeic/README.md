# TOEIC Advanced Vocabulary

- Series ID: `9gfei23g`
- Language: en-en, Level: advanced
- Public: yes
- Collection: Exam Prep (`72d8f528`)

## Curriculums (8 total, 10 vocab words each = 80 words)

| # | ID | Title | Vocab |
|---|---|---|---|
| 1 | 5UQQbXkQ1fveBWqL | Corporate Restructuring and Workforce Strategy | Restructure, Consolidate, Downsize, Streamline, Benchmark, Turnover, Retention, Attrition, Onboard, Severance |
| 2 | I0gSCXj4atKGCSl9 | Financial Reporting and Accountability | Revenue, Expenditure, Audit, Compliance, Forecast, Liability, Amortize, Dividend, Equity, Reconcile |
| 3 | fYXfXZ2Z20qtmTkK | Marketing Strategy and Consumer Behavior | Segment, Demographic, Positioning, Differentiate, Saturate, Conversion, Engagement, Rebrand, Leverage, Metrics |
| 4 | 7zBfHDMzh6RhRTG7 | International Trade and Negotiations | Tariff, Quota, Bilateral, Sanction, Arbitration, Concession, Ratify, Counterpart, Procurement, Stipulate |
| 5 | BKUydKJoCwfBUgbX | Project Management and Execution | Milestone, Deliverable, Stakeholder, Scope, Feasibility, Allocate, Contingency, Scalable, Bottleneck, Iteration |
| 6 | UeEfNpEOxtOmSLUG | Regulatory Compliance and Risk Management | Regulation, Mandate, Oversight, Penalty, Disclosure, Mitigate, Indemnify, Whistleblower, Due Diligence, Litigation |
| 7 | 12f3zeCSGExw4Tg0 | Supply Chain and Operations | Logistics, Inventory, Throughput, Outsource, Vendor, Warehouse, Dispatch, Lead Time, Quality Assurance, Depreciation |
| 8 | UnKP3U93JL7FWSlq | Leadership and Organizational Culture | Delegate, Accountability, Autonomy, Mentor, Consensus, Hierarchy, Transparent, Initiative, Resilience, Succession |

## Find in DB
```sql
SELECT * FROM curriculum_series WHERE id = '9gfei23g';
SELECT c.id, c.content->>'title' as title, c.display_order, cat.overall_level
FROM curriculum_series_items csi
JOIN curriculum c ON c.id = csi.curriculum_id
LEFT JOIN curriculum_all_tags cat ON c.id = cat.id
WHERE csi.curriculum_series_id = '9gfei23g'
ORDER BY c.display_order;
```

## How it was created
Same 4-session pattern as GMAT (5 words S1, 5 words S2, review S3, full article + farewell S4). Reading passages use TOEIC-style business English — memos, reports, case studies. Each curriculum created via a separate script (`toeic_01_restructuring.py` through `toeic_08_leadership.py`, deleted after import). Series created via `toeic_create_series.py` (also deleted). Full content recoverable via `curriculum/getOne` or MCP postgres.
