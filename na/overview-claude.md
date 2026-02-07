# Overview: VAR Threshold Report

## My Understanding

The deliverable is a report for leadership with two objectives packed into one document:

1. **Explain** why last year's VAR came in at $0.3M (against a $3M threshold)
2. **Propose** a new threshold for this year that replaces the $3M figure

The report needs to be both analytically rigorous and strategically self-serving in the right way — the threshold should be defensible to leadership while being high enough that routine business fluctuations don't trigger the risk protocol unnecessarily. The goal is also to demonstrate deep understanding of the business context and stakeholder requirements around this initiative.

When the metric overshoots the threshold in any given month this year, an internal risk-controlled protocol gets triggered — so the threshold directly controls how often you're dealing with protocol activations, including false alarms.

### What VAR Captures

VAR per agent = (total payouts to agent) - (total FYP revenue from that agent's sales)

A positive VAR signals the company is paying an agent more than the revenue that agent generated. At scale, this is the signature pattern of commission abuse — agents fabricating policies to collect payouts, with those policies lapsing in year two when the fake customers cancel.

Only agents with VAR > 0 are in scope. Negative-VAR agents are net-profitable by definition and excluded.

### Why $0.3M Was So Low

Last year had unusually high persistency (policy renewal/continuation rates). High persistency means:
- Fewer cancellations, so FYP revenue held up
- The denominator of the risk equation stayed strong
- Fewer red flags from lapsing policies

This is a **good year artifact**, not a structural reduction in risk exposure.

### Why the Threshold Needs Careful Calibration

Several factors make the number noisy:

- **Deferred payouts**: Commissions paid on a lag (sometimes more than 1 year) mean this year's VAR partially reflects last year's sales activity, and next year's VAR will partially reflect this year's. The payout schedule artificially lowers VAR in the current year but artificially raises it the next. The number doesn't cleanly map to a single performance period.
- **One-off retention packages**: A single $500K-$1M talent retention payment to a key agent can spike their individual VAR without any fraud signal. These are known, approved expenses with a different risk profile — but they inflate the aggregate VAR figure. VAR is meant for mass monitoring, not capturing these one-off decisions.
- **Revenue growth paradox**: A genuine surge in new business (real customers, real policies) also raises VAR in the short term because payouts on new sales come before the revenue fully materializes in the persistency data. High VAR can indicate good business, not just risk — as long as the underlying customer value is real and long-term.

### Salesforce Complexity

The 17-layer MLM structure means the report should focus on **middle-tier agents** — senior enough to have meaningful volume, junior enough to lack the reputational deterrent that constrains top leaders, and positioned in the hierarchy where manipulation of their sub-tree is operationally feasible (their sales tree is small enough to manipulate while any wrongdoing would still be substantial).

The GTF (Growth Task Force) group is a separate risk category — external teams (not individuals) acquired by the company to push volume, rather than grown in-house. They typically have lower persistency and shorter tenure (2-3 years), with different incentive structures and less institutional loyalty.

### Basic Requirements

- The new threshold must be between $0.3M and $3M.

### Final Report Structure

Two main sections:
1. **Performance current VAR deep-dive** — explain the $0.3M number
2. **Threshold proposal and considerations** — propose the new threshold with supporting rationale

---

## Questions for Your Input

### On Scope and Data

1. **Do we have a breakdown of VAR by agent tier?** Specifically, can we isolate the middle-layer agents you mentioned from the top leaders and the bottom ranks? This would strengthen the deep-dive section significantly.

2. **Can we identify and separately tag the one-off retention packages in the data?** If so, we could present a "clean VAR" (excluding known one-offs) alongside the raw number, which would make the threshold proposal much more defensible.

3. **Do we have historical VAR numbers beyond just last year?** Even 2-3 years of trend data would help contextualize $0.3M vs $3M and anchor the new threshold in historical patterns rather than a single data point.

4. **Is there data on the deferred payout schedule?** Knowing how much of last year's $0.3M was actually attributable to prior-year activity (and how much of this year's payouts are already locked in from last year's sales) would let us build a timing-adjusted VAR estimate.

### On the Threshold Proposal

5. **What's your instinct on the right range?** You said between $0.3M and $3M — are you leaning toward the higher end (say $1.5M-$2.5M) or the middle? This helps me calibrate the argumentation.

6. **How many times was the $3M threshold breached or approached in prior years?** Understanding whether $3M was always comfortable headroom or occasionally tested changes how aggressively we can argue for a lower replacement.

7. **Should the proposal include any structural changes to how VAR is calculated?** For example: excluding known retention packages, adjusting for payout timing lags, or segmenting by agent tier. Or do you want to keep the metric definition unchanged and only adjust the threshold number?

8. **Is there appetite from leadership for a tiered threshold** (e.g., different thresholds for middle-layer agents vs GTF vs aggregate), or does the report need to land on a single number?

### On Positioning and Audience

9. **Who exactly reviews and approves the threshold?** Understanding whether this goes to a risk committee, a C-suite sponsor, or a board-level audience affects the tone and depth of the report.

10. **Is there any political context I should know about?** For example — was the $3M threshold set by someone still in the room? Is there pressure to lower the threshold (tighter controls) or raise it (less operational friction)? Both directions have stakeholders.

11. **What happens operationally when the protocol triggers?** Understanding the downstream consequences (investigation scope, resource cost, business disruption) helps me frame the argument for why a higher threshold is responsible rather than careless.
