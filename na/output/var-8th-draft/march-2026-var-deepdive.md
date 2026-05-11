# March 2026 VaR Deep-Dive — Standalone Month Review

**Audience:** Regional Office — VaR Review Committee
**Period:** March 2026 (standalone month, not rolling 12M)
**Source slides:** `slides/var-8th-draft/md/`

---

## 1. Why this deep-dive

In **March 2026** the company launched **ILP26**, a new ILP product with large case size. Three things happened simultaneously:

1. Sales volume surged — large FYP inflow concentrated in March.
2. Multiple incentive contests ran on top of business-as-usual compensation.
3. Sales hit the **highest bonus rate tier** of the new compensation scheme. Because the scheme rewards on FYP — and ILP26 generates uniformly high FYP — many agents/UMs jumped to the top bonus rate.

Regional Office asked us to deep-dive **March 2026 alone** to confirm there is no abnormal pattern hidden inside the rolling-12M figure.

---

## 2. Methodology — March-only VaR

We keep the standard formula:

> **VaR = Total Payout − Total FYP**

But instead of the rolling 12-month window, we use **only March 2026** payout and FYP figures.

**Payout coverage (March 2026 only):**

| Component | Included? |
|---|---|
| First-year commission | ✅ |
| Rider bonus | ✅ |
| UM compensation | ✅ |
| Leader subsidy / GTF | ✅ |
| Other agent / leader items | ✅ |
| **Contest payout based on March production** | ❌ — pending freelook; will be booked into May 2026 VaR |

So **March VaR shown here understates the eventual figure** by the contest payout that will land in May.

---

## 3. March 2026 sits within trend — no anomaly

Monthly VaR figures (mil USD), 12 months ending Mar'26:

| Month | 07/25 | 08/25 | 09/25 | 10/25 | 11/25 | 12/25 | 01/26 | 02/26 | **03/26** | 04/26 | 05/26 (fcst) | 06/26 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| VaR (mil USD) | 0.49 | **1.43** | 0.13 | 0.12 | 0.30 | 0.34 | 0.26 | **0.56** | **0.43** | 0.38 | **0.64** ↑ | 0.24 |
| VaR ('000 VND) | 12,270 | 35,685 | 3,300 | 3,099 | 7,448 | 8,487 | 6,478 | 13,902 | 10,804 | 9,377 | 16,061 | 6,002 |

**Read:**
- **Aug'25 ($1.43M peak)** — driven by contest payout booked from June 2025 high-FYP production.
- **Feb'26 ($0.56M)** — driven by contest payout booked from December 2025 high-FYP production plus large H2 contests.
- **Mar'26 ($0.43M)** — in line with the normal range. Sits **below** Aug'25 and Feb'26 peaks despite ILP26 launch, because contest payouts are not yet booked.
- **May'26 forecast ($0.64M)** — expected to rise once March-production-based contests are booked after freelook.

**Conclusion on the trend:** March 2026 standalone VaR shows **no abnormal spike**. The pattern follows the existing seasonality of contest cycles.

---

## 4. UM+ with VaR > 0 in March 2026 — population view

**505 UM+ units** had VaR > 0 in March, contributing **VND 10.80 bil (~$0.43M USD)**.

### 4.1 By VaR bucket

| Bucket (USD) | # UM+ | VaR ('000 VND) | Share |
|---|---:|---:|---:|
| < 600 | 352 | 1,550,833 | 14% |
| 600 – < 1,200 | 71 | 1,483,589 | 14% |
| 1,200 – < 2,000 | 37 | 1,401,291 | 13% |
| **≥ 2,000** | **45** | **6,368,519** | **59%** |
| **Total** | **505** | **10,804,233** | **100%** |

**70% of units** sit under $1,200 individual VaR — too small to justify gaming behaviour. The signal is concentrated in the **45 units in the ≥$2,000 bucket** (the deep-dive set).

### 4.2 By GTF and MBA Pro tier (all 505 units)

| | Non MBA Pro | MBA Pro Silver | MBA Pro Gold | MBA Pro Platinum | **Total** |
|---|---:|---:|---:|---:|---:|
| **# UM+ with VaR > 0** | 455 | 18 | 14 | 18 | **505** |
| Non GTF | 294 | 11 | 5 | 15 | 325 |
| GTF | 161 | 7 | 9 | 3 | 180 |

By rank: UM 131 / SUM 2 / DM 36 / SDM 8 (non-GTF/GTF combined per slide).

### 4.3 By P13 persistency (units with FYP > 0, n=313)

| P13 | < 600 | 600–1,200 | 1,200–2,000 | ≥ 2,000 | Total | Share |
|---|---:|---:|---:|---:|---:|---:|
| < 50% | 10 | 2 | – | – | 12 | 4% |
| 50–70% | 20 | 2 | 3 | – | 25 | 8% |
| 70–80% | 26 | 7 | 2 | 4 | 39 | 12% |
| ≥ 80% | 128 | 30 | 26 | 36 | 220 | 70% |
| Not yet P13 | 12 | 4 | 1 | – | 17 | 5% |
| **Total** | **196** | **45** | **32** | **40** | **313** | **100%** |

**70% of FYP-producing flagged units have P13 ≥ 80%** — these are quality producers, not arbitrage cases.

---

## 5. Deep-dive — VaR ≥ $2,000 USD bucket

> **Note on data:** OCR captured **40 of the 45** units in this bucket (totalling VND 5.17 bil ≈ $207K). The 5 missing rows account for ~VND 1.20 bil (~$48K). Counts below are based on the 40 captured rows; directional conclusions are unaffected.

### 5.1 Headline conclusion

Per **Note column (AR)**, almost all reviewed cases fall into one of two non-risk explanations:

- **"Diff FYP bonus and FYP VAR"** (calculation gap): UM+ bonus payout is computed on **direct-report-team FYP** (a wider base including indirect downlines), while the VaR formula subtracts only **direct-team FYP**. Same scope mismatch flagged in prior reviews — structural, not behavioural.
- **"Delay payment"**: payout booked in March belongs to production from earlier months (deferred bonuses, late commissions).
- A small residual marked **"–"** (no specific cause flagged yet, low individual amounts).

| Note (col AR) — page 2 only (n=22, with Note populated) | # units | VaR ('000 VND) | ~USD |
|---|---:|---:|---:|
| Diff FYP bonus and FYP VAR (calc gap) | 17 | 2,799,147 | $111,966 |
| Delay payment | 2 | 178,641 | $7,146 |
| – (residual) | 3 | 248,471 | $9,939 |
| **Subtotal (reviewed)** | **22** | **3,226,259** | **$129,050** |
| Page 1 (Select review = N, already cleared) | 18 | 1,943,121 | $77,725 |
| **Deep-dive total (OCR'd)** | **40** | **5,169,380** | **$206,775** |

**~92% of the reviewed VaR amount (page 2) is explained by calculation gap or delayed payment.**

### 5.2 By Rank (column D)

| Rank | # units | VaR ('000 VND) | ~USD | Avg VaR / unit ('000 VND) |
|---|---:|---:|---:|---:|
| BM  | 9 | 1,929,050 | $77,162 | 214,339 |
| DM  | 8 | 941,724 | $37,669 | 117,716 |
| SDM | 9 | 902,616 | $36,105 | 100,291 |
| AM  | 5 | 583,048 | $23,322 | 116,610 |
| SUM | 6 | 539,486 | $21,579 | 89,914 |
| UM  | 3 | 273,456 | $10,938 | 91,152 |
| **Total** | **40** | **5,169,380** | **$206,775** | **129,235** |

**Read:** **BM** carries the largest concentration — 23% of units but 37% of VaR amount — driven by the calculation-gap mechanic (BMs override the widest indirect team). This matches the structural explanation, not a behavioural concern.

### 5.3 By MBA Pro tier (column E)

| MBA tier | # units | VaR ('000 VND) | ~USD | Share of VaR |
|---|---:|---:|---:|---:|
| Non MBA Pro | 23 | 2,046,943 | $81,878 | 40% |
| Platinum (P) | 11 | 1,955,590 | $78,224 | 38% |
| Silver (S) | 3 | 751,433 | $30,057 | 15% |
| Gold (G) | 3 | 415,414 | $16,617 | 8% |
| **Total** | **40** | **5,169,380** | **$206,775** | **100%** |

**Read:** **MBA Pro Platinum** units are over-represented relative to population — only 18 Platinums in the entire 505-unit population, but 11 of them appear in this deep-dive (61%). Platinums are the highest-tier producers; the calc-gap mechanic naturally amplifies on them because they typically lead the largest direct + indirect teams.

### 5.4 By GTF (column F / H)

| Group | # units | VaR ('000 VND) | ~USD | Share of VaR |
|---|---:|---:|---:|---:|
| Non-GTF | 30 | 3,945,878 | $157,835 | 76% |
| GTF | 10 | 1,223,502 | $48,940 | 24% |
| **Total** | **40** | **5,169,380** | **$206,775** | **100%** |

**Read:** Non-GTF leaders carry **3 out of every 4 dollars** of deep-dive VaR. GTFs (with explicit subsidy) appear less, even though GTF subsidy is a known calc-gap driver — most flagged cases are organic UM+ leaders with high indirect-team activity.

### 5.5 Cross-tab — Rank × MBA Pro (counts)

| Rank | Non MBA Pro | Platinum | Silver | Gold | **Total** |
|---|---:|---:|---:|---:|---:|
| UM  | 2 | 1 | – | – | 3 |
| SUM | 4 | – | 1 | 1 | 6 |
| DM  | 1 | 4 | 1 | 2 | 8 |
| SDM | 7 | 2 | – | – | 9 |
| AM  | 3 | 2 | – | – | 5 |
| BM  | 6 | 2 | 1 | – | 9 |
| **Total** | **23** | **11** | **3** | **3** | **40** |

### 5.6 Cross-tab — Rank × GTF (counts)

| Rank | GTF | Non-GTF | **Total** |
|---|---:|---:|---:|
| UM  | 1 | 2 | 3 |
| SUM | 2 | 4 | 6 |
| DM  | 3 | 5 | 8 |
| SDM | 1 | 8 | 9 |
| AM  | 2 | 3 | 5 |
| BM  | 1 | 8 | 9 |
| **Total** | **10** | **30** | **40** |

### 5.7 Cross-tab — Note × Rank (page 2 only, n=22)

| Note | UM | SUM | DM | SDM | AM | BM | **Total** |
|---|---:|---:|---:|---:|---:|---:|---:|
| Diff FYP bonus and FYP VAR | – | 2 | 3 | 6 | 2 | 4 | 17 |
| Delay payment | 1 | – | – | – | – | 1 | 2 |
| – (residual) | – | – | 1 | 1 | 1 | – | 3 |
| **Total** | **1** | **2** | **4** | **7** | **3** | **5** | **22** |

The calc-gap explanation appears across **every rank above UM**. That is consistent with the structural read: it is a formula-scope effect, not a rank-specific behaviour.

---

## 6. Conclusions for Regional Office

1. **March 2026 standalone VaR is normal.** $0.43M USD sits below Aug'25 and Feb'26 contest-driven peaks. Forecast May'26 will be the next peak, when March-production contests post.
2. **ILP26 launch is not driving abnormal VaR yet** — March payout in this view excludes the contest layer. Even at the higher bonus tiers triggered by ILP26 case-size, the residual VaR after standard explanations is small.
3. **The ≥$2,000 deep-dive bucket holds 59% of total March VaR** but **~92% of the reviewed amount is explained by calculation gap or delayed payment**, not arbitrage.
4. **Concentration patterns are structural, not behavioural:**
   - **BM rank** carries 37% of deep-dive VaR — widest indirect-team override.
   - **MBA Pro Platinum** units are over-represented — top-producer override mechanics.
   - **Non-GTF** leaders dominate (76% of VaR) — organic team scale, not subsidised structures.
5. **No new control gap identified.** Existing Line1B monthly screening, deep-dive review, and payment-suspension protocol remain sufficient. Recommend continuing **monthly tracking of the calc-gap fingerprint** (BM + Platinum + non-GTF) into May'26 to catch any deviation when contest payouts post.
