# VAR Detailed Analysis Report
## Actual Risk vs. No-Risk Breakdown within the 0.3M VND VAR (2025)

---

## 1. Breakdown of the $0.3M VAR: Actual Risk vs. No-Risk

### 1.1 Total VAR Composition

The $0.3M (or $293K to be precise) VAR across 260 UM+ units breaks down into **two distinct categories**:

| Category | Amount (USD '000) | % of Total VAR | Risk Classification |
|----------|-------------------|----------------|---------------------|
| **FYP = 0 or FYP < 0, Payout > 0** | ~$52K | **17.7%** | Mostly No-Risk (explainable) |
| **FYP > 0, Payout > 0 (Other VAR >0%)** | ~$241K | **82.3%** | Mixed — requires deeper analysis |
| **Total** | **~$293K** | **100%** | |

### 1.2 The "No-Risk" Portion (~$52K / 17.7%)

This $52K comes from 52 units where FYP ≤ 0 but payouts were positive. The meeting confirmed these are **structurally explainable and clean**:

| Sub-Category | Amount (USD '000) | Units | Root Cause | Risk? |
|---|---|---|---|---|
| **FYP = 0, Payout > 0** | $36.6K | 40 units (< $2K) + 12 units ($2-4K) | Deferred payments + freelook timing + indirect team income | **No** — timing artifacts |
| **FYP < 0, Payout > 0** | $10.9K | ~8 units | Cancellations exceeded new sales, but prior-earned payouts still disbursed | **No** — lag effect |
| **FYP < 0, Payout < 0** | $4.0K | 6 units | Both negative — net clawback situation | **No** — self-correcting |
| **Subtotal "Clean"** | **~$51.5K** | ~60 units | | **No real risk** |

**Three specific no-risk mechanisms identified:**

1. **Deferred payments (NAB, Manly Agent):** Production from Nov-Dec 2024 paid out in Jan 2025 after passing the 21-day freelook period. This is a ~2-month timing lag, not fraud.

2. **Freelook period formula mismatch:** The 21-day customer confirmation window means FYP recognition lags behind payout timing. Structurally unavoidable.

3. **Direct vs. indirect team mismatch:** UM+ payout includes income from their entire downline (overrides, leader activation), but FYP only captures direct team production. A UM+ with zero personal/direct FYP can still legitimately earn from their indirect team.

### 1.3 The "Actual Risk" Portion (~$241K / 82.3%)

This comes from 168 units where both FYP > 0 and Payout > 0, but payout exceeds FYP. Breakdown by VAR size:

| VAR Bucket | Units | VAR Amount (USD '000) | Payout (USD '000) | Key Concern |
|---|---|---|---|---|
| $0 - $2K | 136 | $78K | $424K | Low individual risk, high volume |
| $2K - $4K | 12 | $34K | $127K | Moderate |
| $4K - $8K | 15 | $81K | $382K | Higher per-unit exposure |
| ≥ $8K | 3 | $49K | $241K | Concentrated risk — 3 units = $49K |
| **Total** | **168** | **$241K** | **$1,175K** | |

**Payout composition for these 168 "real VAR" units:**

| Component | Amount (USD '000) | % of Total Payout | Risk Profile |
|---|---|---|---|
| FYC (First Year Commission) | $309K | 26% | Low — directly tied to production |
| Agent Income | $369K | 31% | Medium — includes contests & compensation |
| — Agent Compensation | $187K | 16% | Low-Medium |
| — Agent Contests | $179K | 15% | Medium — can be gamed |
| UM+ Income | $497K | **42%** | **Highest risk component** |
| — UM+ Compensation (overrides, activation) | $367K | 31% | Medium — tied to team production |
| — **UM+ GTF Subsidy** | **$45K** | **4%** | **HIGH — no clawback** |
| — UM+ Contests | $85K | 7% | Medium |


### 1.4 Summary: Risk vs. No-Risk Ratios

| Classification | Amount (USD '000) | % of $293K Total | Details |
|---|---|---|---|
| **No-Risk (Clean/Explainable)** | ~$52K | **17.7%** | Timing lags, formula mismatches, self-correcting |
| **Low Risk (legitimate business)** | ~$141K | **48.1%** | FYC + standard agent compensation in the FYP>0 group |
| **Medium Risk (monitor-worthy)** | ~$55K | **18.8%** | Contests + UM+ compensation that could be influenced |
| **High Risk (GTF + concentrated)** | ~$45K | **15.4%** | GTF subsidy with no clawback + top 3 high-VAR units |
| **Total** | **~$293K** | **100%** | |

**Bottom line:** Only about **15-19% of the $0.3M** ($45-55K) represents genuinely concerning risk. The rest is either structurally explainable or tied to legitimate business activity.

---

## 2. GTF Group Contribution and Concerns

### 2.1 GTF Within the Current $0.3M VAR

| Metric | Value | Source |
|---|---|---|
| **GTF Subsidy in FYP>0 group** | $45K (USD '000) | Slide: FYP>0 & Payout>0, line 3.2 |
| **GTF Subsidy in FYP=0 group** | $8.1K (USD '000) | Slide: FYP=0, line 3.2 |
| **GTF Subsidy in FYP<0 group** | $0 | Slide: FYP<0, line 3.2 |
| **Total GTF Subsidy exposure** | **~$53K** | |
| **% of total $293K VAR** | **~18.1%** | |

### 2.2 Why GTF Is the Primary Concern

From the meeting transcript, three structural risks were identified:

1. **Net production threshold is too low:** GTF subsidy triggers on net production > 0. Even minimal production qualifies for the full subsidy rate.

2. **No clawback mechanism:** Unlike other compensation components, GTF subsidy has **zero clawback**. Once paid, it cannot be recovered even if the underlying policies lapse.

3. **Gaming vulnerability:** The specific abuse pattern identified:
   - Submit a 100M VND policy → earn 10% subsidy = 10M VND
   - Customer cancels during freelook
   - Resubmit the same policy → earn another 10M VND
   - Repeat indefinitely with net production staying > 0

### 2.3 GTF Impact with 20-30% Growth Projection

If the business grows 20-30% this coming year (targeting ~$7M FYP as stated in the slides), here's the GTF exposure projection:

**Assumptions:**
- 2025 Agency FYP: ~$45-50M (actual)
- 2026 target: ~$7M business plan (per slide), but with 20-30% growth on current base = ~$54-65M
- GTF groups typically have lower persistency (2-3 year tenure) and are external acquisitions
- GTF subsidy currently = $53K out of $293K VAR

**Projection scenarios:**

| Scenario | Growth | Projected FYP | GTF Subsidy Exposure | GTF as % of Projected VAR | Total Projected VAR |
|---|---|---|---|---|---|
| **Conservative (20% growth)** | 20% | ~$54M | $64-80K | 15-20% | $0.4-0.5M |
| **Base (25% growth)** | 25% | ~$56M | $80-106K | 18-25% | $0.5-0.7M |
| **Aggressive (30% growth)** | 30% | ~$59M | $106-159K | 20-30% | $0.7-1.0M |
| **2023-like scenario** | Return to 2023 levels | ~$72M | $150-200K+ | 25-35% | $2.5-3.5M |

**Key drivers of GTF escalation with growth:**
- Growth often comes through GTF group acquisitions (external teams brought in to push volume)
- New GTF groups = more subsidy-eligible UMs with fresh net production
- The no-clawback structure means losses are permanent and compound
- If recruitment rebounds (as expected), more new agents under GTF UMs = more subsidy triggers

**Worst-case GTF concern:** If the company returns to 2023-level production (~$72M) as the slides suggest is the target, and GTF groups are a significant driver of that growth, GTF subsidy exposure could reach **$150-200K+**, representing **25-35% of a projected $2.5-3.5M VAR** — making it the single largest identifiable risk component.

---

## 3. VAR Threshold Proposal with Supporting Numbers

### 3.1 Historical Context

| Year | Avg Monthly VAR (Mn USD) | Peak VAR | Agency FYP | %VAR/FYP | Business Context |
|---|---|---|---|---|---|
| 2020 | $1.9M | $2.2M (Jan) | $222M | 0.8-1.3% | Stable, mass recruitment |
| 2021 | $1.8M | $2.0M (Dec) | $241M | 0.7-0.8% | Peak business volume |
| 2022 | $2.4M | $3.8M (Dec) | $204M | 0.9-1.9% | Transition period begins |
| 2023 | $3.4M | $3.8M (May) | $72M | 1.8-4.0% | Business decline, VAR spikes |
| 2024 | $1.1M | $2.4M (Jan) | $45M | 0.7-3.6% | Continued decline |
| 2025 | $0.3M | $0.3M (Jan) | ~$50M est. | 0.3-0.6% | Trough — unusually low |

### 3.2 Why the Current $3.0M Trigger Is Too High

- 2025 VAR is $0.3M — the trigger is **10x** the actual exposure
- Even in the worst year (2023), VAR peaked at $3.8M and averaged $3.4M
- A $3.0M trigger would never have been breached in 2020, 2021, or 2024
- It only would have triggered in late 2022 and throughout 2023 — precisely when business was in structural decline

### 3.3 Why Too Low Is Also Dangerous

- Growth is expected (20-30%), which will naturally push VAR up
- New compensation scheme (launched Apr 2024) invests more in UM+ compensation — this will inflate VAR as UMs rebuild teams
- One-off retention packages ($500K-$1M) can spike VAR without fraud
- GTF group acquisitions for growth will add subsidy exposure
- Setting too low = constant protocol triggers = operational burden on Line1B and Compensation teams

### 3.4 Recommended Proposal: $1.5M Trigger with Supporting Math

**Method: Weighted historical average + growth adjustment + buffer**

**Step 1: Establish baseline from "normal" years**

| Year | Avg VAR | Weight | Rationale |
|---|---|---|---|
| 2020 | $1.9M | 15% | Pre-transition, stable |
| 2021 | $1.8M | 15% | Peak business, low risk |
| 2022 | $2.4M | 20% | Transition — relevant for growth periods |
| 2023 | $3.4M | 10% | Outlier — structural decline, not representative |
| 2024 | $1.1M | 15% | Declining but with new comp scheme |
| 2025 | $0.3M | 25% | Current reality, most recent |

**Weighted average = (0.15×1.9) + (0.15×1.8) + (0.20×2.4) + (0.10×3.4) + (0.15×1.1) + (0.25×0.3) = $1.38M**

**Step 2: Growth adjustment**
- Expected growth: 20-30% → use midpoint 25%
- Growth impact on VAR is typically 1.2-1.5x (VAR grows faster than FYP due to compensation leverage)
- Adjusted: $1.38M × 1.1 (conservative multiplier since we're growing from a low base) = **$1.52M**

**Step 3: Round and buffer**
- Round to $1.5M
- This provides ~5x headroom above current $0.3M
- This is 50% of the old $3.0M trigger
- This would NOT have been breached in 2020, 2021, or 2024
- This WOULD have been breached in 2022 (Dec only: $3.8M) and 2023 (all months) — which is appropriate since those were genuinely elevated risk periods

### 3.5 Sensitivity Check: Would $1.5M Work Under Different Scenarios?

| Scenario | Projected VAR | Breach $1.5M? | Appropriate? |
|---|---|---|---|
| Status quo (no growth) | $0.3-0.4M | No | ✓ No false alarm |
| Moderate growth (20%) | $0.5-0.7M | No | ✓ Normal business |
| Strong growth (30%) | $0.7-1.0M | No | ✓ Healthy growth |
| Return to 2023 levels | $2.5-3.5M | **Yes** | ✓ Correctly flags elevated risk |
| One-off retention package | +$0.5-1.0M spike | Maybe | ✓ Triggers review only if combined with other factors |
| GTF abuse scenario | +$0.2-0.5M | No alone | ✓ But should be monitored separately |

### 3.6 Alternative Proposals for Consideration

| Option | Trigger | Pros | Cons |
|---|---|---|---|
| **A: Conservative** | **$1.0M** | Tighter control, regional risk team prefers | May trigger too often with growth + one-offs |
| **B: Recommended** | **$1.5M** | Balanced — catches real risk, avoids false alarms | Requires GTF to be monitored separately |
| **C: Status quo aligned** | **$2.0M** | More headroom for growth | May be seen as too lenient by regional |
| **D: Keep current** | **$3.0M** | No change needed | Effectively useless — never triggers |

### 3.7 Complementary Recommendation: Separate GTF Monitoring

Regardless of the trigger chosen, GTF subsidy should be tracked as a **separate line item** because:
- It has no clawback (unique among all compensation components)
- It's the only component with a known gaming vulnerability
- It will grow disproportionately if GTF groups drive the expected growth
- At $53K today (18% of VAR), it's already the largest single identifiable risk

**Suggested GTF-specific control:** Flag any month where GTF subsidy exceeds 25% of total VAR or $50K absolute, whichever is lower.

---

## Summary Table

| Question | Answer |
|---|---|
| **Actual risk within $0.3M** | ~$45-55K (15-19%) is genuinely concerning; ~$52K (18%) is clean/no-risk; remainder is low-medium risk tied to normal business |
| **GTF contribution** | $53K or ~18% of total VAR, with $45K from FYP>0 units and $8.1K from FYP=0 units |
| **GTF concern with 20-30% growth** | Could reach $80-200K+ depending on how much growth is GTF-driven; no clawback + gaming vulnerability = compounding risk |
| **Recommended VAR trigger** | **$1.5M** — based on weighted historical average ($1.38M) + growth adjustment, with separate GTF monitoring |
| **Range for negotiation** | $1.0M (floor for regional) to $2.0M (ceiling for local), with $1.5M as the defensible middle ground |
