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
- **Revenue growth paradox**: Strong revenue growth in a single year will push VAR up because top-performers perform even better and new recruits come in large quantity. Both of these could mean good business — though not always. The point is that high VAR doesn't automatically signal risk; it can reflect genuine commercial momentum.

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

## Q&A

### On Scope and Data

1. **Do we have a breakdown of VAR by agent tier?** — **Yes.** The data already only considers the relevant middle-layer group.

2. **Can we identify and separately tag the one-off retention packages?** — **Yes.** This means we can present a "clean VAR" (excluding known one-offs) alongside the raw number, making the threshold proposal more defensible.

3. **Do we have historical VAR numbers?** — **Yes, last 5 years.** See summary.jpg for the data. This gives us strong trend context to anchor the new threshold.

4. **Is there data on the deferred payout schedule?** — **Yes.** We can build a timing-adjusted VAR estimate.

### On the Threshold Proposal

5. **What's your instinct on the right range?** — **No strong lean yet.** The threshold number needs to emerge from the analysis rather than a pre-set target.

6. **How many times was the $3M threshold breached or approached?** — **See summary.jpg** for historical data.

7. **Should the proposal include structural changes to how VAR is calculated?** — **No.** Too much additional work. Keep the metric definition unchanged, only adjust the threshold number.

8. **Is there appetite for a tiered threshold?** — **No.** Too much additional work. The report needs to land on a single number.

### On Positioning and Audience

9. **Who reviews and approves the threshold?** — **Regional risk committee and local executive board.**

10. **Political context?** — **Regional risk wants to lower the threshold** (tighter controls). **Local wants higher** (less operational friction). The report needs to navigate both audiences.

11. **What happens when the protocol triggers?** — The local team (Compensation and Line1B — front risk sales) has to alert and provide deep-dive analysis, possibly on a monthly basis, to the regional team. Line1B already has monthly protocols for other risk controls — this is not the only item they manage.
