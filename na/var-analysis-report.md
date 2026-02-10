# VAR Deep-Dive Analysis & Threshold Proposal Report

**Date:** February 9, 2026
**Period Under Review:** Rolling 12 months ending December 2025
**Current VAR:** $0.3M USD | **Current Approved Trigger:** $3.0M USD

---

## SECTION 1: Breakdown of the $0.3M VAR — Actual Risk vs. No-Risk

### 1.1 High-Level Split

The $0.3M ($293K) total VAR across 260 UM+ units decomposes into three distinct categories based on the nature of FYP and payout:

| Category | # Units | VAR ($K USD) | % of Total VAR | Risk Assessment |
|---|---|---|---|---|
| **FYP > 0 & Payout > 0** (normal operations) | 168 | 241.0 | 82.3% | Mixed — see 1.2 |
| **FYP = 0 & Payout > 0** (zero production, positive payout) | 52 | 36.6 | 12.5% | Mostly no-risk — see 1.3 |
| **FYP < 0 & Payout > 0** (negative production, positive payout) | 34 | 10.9 | 3.7% | Mostly no-risk — see 1.4 |
| **FYP < 0 & Payout < 0** (both negative) | 6 | 4.0 | 1.4% | No risk (net negative payout) |
| **Total** | **260** | **~293** | **100%** | |

> **Key finding from the slides:** ~$0.05M ($50K) of the total VAR comes from cases where production is zero or negative but payout is positive. After removing these explainable cases, the "real" VAR is approximately **$0.24M**.

### 1.2 The $241K — FYP > 0 & Payout > 0 (168 units, 82.3% of VAR)

This is the core group where genuine risk assessment matters. Payout composition:

| Payout Component | $K USD | % of Total Payout ($1,175K) | Risk Profile |
|---|---|---|---|
| **1) FYC (First Year Commission)** | 309 | 26% | No risk — direct commission on production |
| **2) Agent Income** | 369 | 31% | Low risk — compensation tied to personal production |
| — 2.1 Agent Compensation | 187 | 16% | Low risk |
| — 2.2 Agent Contest_DT | 179 | 15% | Low risk |
| — 2.3 Agent Others_DT | 2 | 0% | Negligible |
| **3) UM+ Income** | 497 | 42% | **Medium risk — largest component** |
| — 3.1 UM+ Compensation (override, activation, etc.) | 367 | 31% | Low-medium risk |
| — **3.2 UM+ GTF Subsidy_DT** | **45** | **4%** | **Higher risk — no clawback** |
| — 3.3 UM+ Contest_DT | 85 | 7% | Low risk |

**Actual risk vs. no-risk within the $241K group:**

- **No-risk / low-risk portion:** FYC ($309K) + Agent Income ($369K) + UM+ Compensation ($367K) + UM+ Contest ($85K) = **$1,130K of $1,175K total payout** — these are standard compensation components tied to legitimate production activity. The VAR here arises because payout includes income from the UM's whole team (indirect), while FYP only captures direct team production. This is a **structural artifact of the methodology**, not a fraud signal.
- **Elevated-risk portion:** GTF Subsidy at **$45K** (4% of payout in this group) — this is the component with no clawback mechanism and potential for gaming.

### 1.3 The $36.6K — FYP = 0 & Payout > 0 (52 units, 12.5% of VAR)

These are units with zero direct production but still receiving payouts. Breakdown:

| Component | $K USD | % of $36.6K | Explanation |
|---|---|---|---|
| FYC | 0.1 | 0% | Negligible |
| Agent Income | 19.3 | 53% | Primarily Agent Contest ($15.0K) + deferred NAB payments ($3.2K) |
| UM+ Income | 17.1 | 47% | **GTF Subsidy: $8.1K (22%)** + Contest: $5.4K + Compensation: $3.6K |

**Risk assessment:**
- **No-risk ($28.5K, 78%):** Deferred payments from prior-year production (NAB_FT = $3.2K), contest payouts earned in prior periods, leader override/activation from indirect team production, and freelook timing gaps.
- **Risk component ($8.1K, 22%):** GTF Subsidy paid to units with zero direct production — this is the most concerning finding. These units generated no FYP yet received GTF subsidy because GTF subsidy is calculated on **net production** (only needs net > 0 from any source) with **no clawback**.

### 1.4 The $10.9K — FYP < 0 & Payout > 0 (34 units, 3.7% of VAR)

| Component | $K USD | % of $10.9K |
|---|---|---|
| FYC | (2.0) | Negative (cancellations) |
| Agent Income | 4.2 | 39% |
| UM+ Income | 3.2 | 29% |
| — GTF Subsidy | 0 | 0% |

**Risk assessment:** No GTF exposure here. The negative FYP reflects policy cancellations/lapses. Payouts are from deferred compensation and contests. **Low risk** — these are timing artifacts.

### 1.5 Summary: Actual Risk vs. No-Risk Ratios

| | $K USD | % of $293K Total VAR |
|---|---|---|
| **No-risk / explainable** | ~$240K | ~82% |
| — Deferred payments / freelook timing | ~$50K | ~17% |
| — Structural methodology artifact (indirect team income vs. direct FYP) | ~$190K | ~65% |
| **Potential risk requiring monitoring** | ~$53K | ~18% |
| — **GTF Subsidy (total across all groups)** | **$53.1K** | **18.1%** |
| — Other elevated-risk components | ~$0K | ~0% |

---

## SECTION 2: GTF Group — Specific Concerns & Growth Projections

### 2.1 GTF Contribution to the $0.3M VAR

| GTF Subsidy Location | $K USD | % of Total VAR ($293K) |
|---|---|---|
| Within FYP > 0 & Payout > 0 group | 45.0 | 15.4% |
| Within FYP = 0 & Payout > 0 group | 8.1 | 2.8% |
| Within FYP < 0 & Payout > 0 group | 0.0 | 0.0% |
| **Total GTF Subsidy in VAR** | **$53.1K** | **18.1%** |

**GTF is the single largest identifiable risk component in the entire $0.3M VAR.**

### 2.2 Why GTF Is Structurally Risky

From the meeting transcript and slides, three specific concerns:

1. **No clawback mechanism:** Unlike other compensation components, GTF subsidy paid out cannot be recovered if the underlying policies lapse or are cancelled.
2. **Low qualification bar:** Calculated on net production — only needs net > 0 to qualify. This is a much lower bar than other compensation schemes.
3. **Gaming potential:** An agent can submit a policy (e.g., 100M VND), cancel it, resubmit the same policy, and collect subsidy again each time. Example: 100M VND policy × 10% subsidy rate = 10M VND bonus per cycle, repeatable.

### 2.3 Growth Projection: 20-30% Business Growth Impact on GTF VAR

Using 2025 actuals as baseline and applying growth scenarios:

**Baseline (2025):** GTF Subsidy VAR = $53.1K

| Scenario | Growth Rate | Projected GTF VAR | Projected Total VAR | Rationale |
|---|---|---|---|---|
| Conservative | 20% | $63.7K | ~$352K | Linear scaling with production growth |
| Moderate | 25% | $66.4K | ~$366K | Mid-range estimate |
| Aggressive | 30% | $69.0K | ~$381K | Upper bound |
| **Risk-adjusted (with gaming)** | **25% + gaming uplift** | **$80-100K** | **$400-450K** | GTF gaming grows disproportionately with volume because more agents = more gaming opportunities, and no clawback means losses compound |

**Why GTF risk scales non-linearly with growth:**
- 20-30% growth means significantly more recruitment, and GTF groups are external teams brought in specifically to push volume during growth phases
- More GTF agents = more subsidy payouts = more gaming surface area
- Historical pattern: When MVL grew aggressively (2019-2022, ~$200M/year FYP), VAR was stable at ~$2.0M. But the GTF scheme wasn't as prominent then. The new compensation structure (launched Apr 2024) with increased UM+ investment amplifies GTF exposure
- If GTF subsidy grows at 1.5-2x the rate of overall business growth (plausible given recruitment-heavy growth strategy), GTF VAR could reach **$80-100K**, representing **20-25% of projected total VAR**

---

## SECTION 3: Proposed VAR Threshold — Recommendation with Supporting Numbers

### 3.1 Historical Context

| Year | Avg Monthly VAR ($M) | Peak VAR ($M) | Agency FYP ($M) | %VAR/FYP (avg) | Business Context |
|---|---|---|---|---|---|
| 2020 | 1.9 | 2.2 | ~222 | ~1.0% | Mass recruitment era |
| 2021 | 1.8 | 2.0 | 241 | ~0.8% | Mass recruitment era |
| 2022 | 2.5 | 3.8 | 204 | ~1.2% | Transition period |
| 2023 | 3.4 | 3.8 | 72 | ~2.8% | Business decline, peak VAR |
| 2024 | 1.0 | 2.4 | 45 | ~1.8% | Continued decline |
| 2025 | 0.3 | 0.3 | ~50* | ~0.6% | Recovery begins |

*Estimated from %VAR/FYP ratio

### 3.2 The Problem with the Existing $3.0M Trigger

- The $3.0M trigger was set based on 2023 peak conditions (avg $3.4M VAR, FYP at $72M)
- In 2025, VAR is $0.3M — the trigger is **10x the actual exposure**
- Regional risk committee wants to lower the threshold (tighter controls)
- Local team wants it higher (less operational friction)
- The threshold must be between $0.3M and $3.0M

### 3.3 Projection for 2026

The slides state: with business plan targeting ~7M USD (likely a monthly figure, annualized ~$84M FYP), expecting to return to 2023-level production, activity, and recruitment.

**Scenario modeling:**

| Scenario | Assumed FYP ($M) | %VAR/FYP | Projected VAR ($M) | Basis |
|---|---|---|---|---|
| A: Return to 2023 levels | 72-84 | 2.8% (2023 avg) | 2.0-2.4 | Full return to 2023 business mix |
| B: Growth with improved persistency | 60-75 | 1.5% (blended) | 0.9-1.1 | Growth but better risk controls than 2023 |
| C: Moderate growth from 2025 base | 50-65 | 1.0% (conservative) | 0.5-0.7 | 20-30% growth from current base |
| D: New compensation impact | 60-75 | 2.0% | 1.2-1.5 | Apr 2024 new comp scheme fully kicks in |

**Most likely scenario:** A blend of B and D — growth with new compensation impact but better controls. **Expected VAR range: $0.8M - $1.5M.**

### 3.4 My Recommendation: $1.5M Trigger Point

**Proposed threshold: $1.5M USD**

**Supporting rationale:**

| Factor | Detail | Impact on Threshold |
|---|---|---|
| **2025 actual** | $0.3M | Floor reference — threshold must be above this |
| **Growth expectation** | 20-30% YoY | Pushes VAR up from $0.3M base |
| **New compensation scheme** | Launched Apr 2024, not yet fully reflected | Will increase UM+ payouts → higher VAR |
| **GTF risk** | $53K currently, could reach $80-100K | Adds ~$30-50K incremental risk |
| **Historical average (excl. 2023 peak)** | ~$1.8M (2020-2022 avg) | Upper reference for normal operations |
| **2023 peak** | $3.4-3.8M | Anomaly year — should not be the benchmark |
| **Deferred payment lag** | 2025's strong persistency will create deferred payouts in 2026 | Adds ~$0.1-0.2M timing effect |

**Why $1.5M specifically:**

1. **Headroom above expected:** If expected VAR is $0.8-1.5M, a $1.5M trigger gives a small buffer for normal fluctuations without constant false alarms
2. **Credible to regional risk:** It's a 50% reduction from the current $3.0M — demonstrates tightening of controls, which regional wants to see
3. **Manageable for local team:** At $1.5M, the protocol would only trigger if VAR exceeds 2x the upper end of the moderate growth scenario — meaning it triggers on genuinely unusual activity, not routine business
4. **Historically grounded:** $1.5M is below the 2020-2022 stable average of ~$1.8M, showing it's a tighter standard than the mass-recruitment era
5. **GTF-aware:** Even if GTF gaming doubles ($53K → $106K) and overall VAR grows 30%, you'd reach ~$0.4M + growth effects ≈ $0.8-1.2M — still under the trigger
6. **Defensible math:** $1.5M = approximately 2% of projected $75M FYP, which aligns with the historical %VAR/FYP range of 1-2% during normal business years (2020-2022)

### 3.5 Alternative Options (if $1.5M doesn't land)

| Option | Threshold | Pros | Cons |
|---|---|---|---|
| **Conservative** | $1.0M | Pleases regional; very tight control | High false-alarm risk if growth materializes; monthly protocol burden on local team |
| **Recommended** | **$1.5M** | **Balanced; defensible; historically grounded** | **Regional may push back wanting lower** |
| **Moderate** | $2.0M | Comfortable buffer; low false-alarm risk | Regional may see as insufficient tightening from $3.0M |
| **Status quo adjusted** | $2.5M | Minimal operational change | Hard to justify given $0.3M actual; regional will reject |

### 3.6 Additional Recommendation: GTF Guardrail

Regardless of the threshold chosen, I recommend flagging the GTF subsidy risk separately in the proposal:

- **Propose a GTF-specific sub-limit** of $100K within the overall VAR threshold — if GTF subsidy VAR alone exceeds $100K, it triggers a targeted review even if total VAR is under the main threshold
- **Recommend introducing a clawback mechanism** for GTF subsidy (this was an open action item from the meeting)
- This demonstrates proactive risk management to regional while keeping the main threshold at a practical level

---

## Summary

| Question | Answer |
|---|---|
| Actual risk vs. no-risk in $0.3M? | **~82% no-risk** (structural/timing artifacts), **~18% potential risk** (almost entirely GTF subsidy at $53.1K) |
| GTF contribution? | **$53.1K = 18.1% of total VAR** — the single largest identifiable risk component |
| GTF concern with 20-30% growth? | GTF VAR could reach **$80-100K** (with gaming risk), representing **20-25% of projected total VAR** |
| Proposed threshold? | **$1.5M USD** — a 50% reduction from current $3.0M, supported by historical data, growth projections, and balanced stakeholder positioning |
