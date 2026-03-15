# GMAT Verbal Mastery — Test Prep Series

## Series
- ID: `09o7ke5d`
- Title: GMAT Verbal Mastery
- Language: en-en, Level: advanced
- Public: yes

## Curriculums (8 total, 10 vocab words each = 80 words)

| # | ID | Title | Vocab |
|---|---|---|---|
| 1 | K4F6GjtDSgx6owTZ | The Logic of Market Failures | Externality, Asymmetry, Equilibrium, Subsidize, Aggregate, Monopoly, Elasticity, Incentivize, Depreciation, Fiscal |
| 2 | XqB48r48SYeTrXba | Corporate Governance Under Pressure | Fiduciary, Stakeholder, Divestiture, Compliance, Malfeasance, Liability, Oversight, Proxy, Remuneration, Tenure |
| 3 | ijfMPhQUnClt43mn | The Science of Clinical Trials | Placebo, Efficacy, Longitudinal, Confounding, Attrition, Randomization, Cohort, Biomarker, Dosage, Adverse |
| 4 | 5LXxhXz0zJaTLIa3 | Rhetoric and Persuasion in Public Policy | Fallacy, Premise, Inference, Corroborate, Rebut, Rhetoric, Empirical, Anecdotal, Partisan, Consensus |
| 5 | 6faN5Ed5x4fA5WKW | Supply Chains and Global Interdependence | Logistics, Procurement, Tariff, Arbitrage, Bottleneck, Inventory, Throughput, Outsource, Embargo, Resilience |
| 6 | NymFJm2s7OGcFTYe | The Psychology of Decision-Making | Heuristic, Anchoring, Cognitive, Rationalize, Aversion, Framing, Sunk, Overconfidence, Prospect, Nudge |
| 7 | MlgfMgVqYQLEbqgj | Environmental Regulation and Industry | Mitigation, Mandate, Emission, Sustainability, Incentivize, Compliance, Externality, Renewable, Biodiversity, Sequestration |
| 8 | A90ZtdJOcTi5ItGX | Statistical Reasoning in Everyday Life | Correlation, Deviation, Extrapolate, Percentile, Skew, Regression, Outlier, Causation, Sampling, Variance |

## Find in DB
```sql
-- Series
SELECT * FROM curriculum_series WHERE id = '09o7ke5d';

-- All curriculums in series
SELECT c.content->>'title' as title, c.display_order, cat.overall_level
FROM curriculum_series_items csi
JOIN curriculum c ON c.id = csi.curriculum_id
LEFT JOIN curriculum_all_tags cat ON c.id = cat.id
WHERE csi.curriculum_series_id = '09o7ke5d'
ORDER BY c.display_order;
```

## How it was created
Each curriculum follows the standard 4-session pattern:
- Session 1: Learn 5 words + short reading passage
- Session 2: Learn 5 more words + short reading passage (recaps Session 1)
- Session 3: Review all 10 words (flashcards + vocab drills + writing)
- Session 4: Full article reading + comprehensive writing + farewell

Reading passages are written in dense, analytical GMAT style — multi-layered arguments with cause-effect reasoning. Content was generated via `create_gmat_series.py` (deleted after import). Full content recoverable via `curriculum/getOne` or MCP postgres.
