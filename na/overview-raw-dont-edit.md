# PROJECT CONCEPT
- I need to write a detailed-report to explain a specific business metrics from last year and simultaneously propose a threshold for this year
- When the metrics overshoot the threshold at any given month this coming year, an internal risk-controlled protocol will be triggered.
- This report should both be quantified and persuasive to leadership, while at the same time the prososed threshold should be justifiably high so the protocol won't be triggered offen, causing issues for me to resolve, especially when it's false alarm.
- I want to demonstrate deep understanding of the business context and stakeholder's requirements regarding this initiative.

# THE METRIC
VAR (Value At Risk, calculated per insurance agent) = [total payout to the agent, i.e. company's expense] - [total production First Year Premium FYP, i.e. revenues paid by customers]

What this number means is how much the company is possibly exposed to sales-commission loop holes being exploited by the insurance agents. They may sell fake insurance contracts to fake customers to get the payout only to have that fake customer canceling the contract the second year.

# KEY ESTABLISHED CONDITIONS
For agents with VAR < 0, we don't include them because we perceive these cases carry no risk: we are already paying agents less than what they brought in.

# LAST YEAR THRESHOLD
$3M

# ACTUAL METRIC NUMBER
$0.3M (this is unusually low because we had a good year last year, with very high "persistency" - the term to mean the percentage of customers continue with the insurance contracts)

# BASIC REQUIREMENTS
- The new threshold should be bigger than $0.3M but lower than $3M.

# OTHERS
- A high threshold doesn't mean that we're careless. In some cases such as very strong revenue growth (with real long-term customer value) in a single year will cause this VAR number to go up but it could mean GOOD business because top-performers will perform even better and new recruits come in large quantity, both of which could mean good business though not always

# SALESFORCE STRUCTURE
- 17 layers of multi-level sales. We only care about the middle layers because agents in these layers may still have the capacity to manipulate sales numbers (their sales tree small enough) and not carry as much reputation risk as the highest leaders of the chart, and yet any wrongdoing will still be substantial.
- There is also a group of outsiders brought in to push sales. These are called Growth-Task-Force (GTF for short). These are often sales teams with multiple agents each that our company acquire as a team rather than growing in-house individually. They typically have lower persistency. Their tenure are often shorter too, 2-3 years.
 
# KEY CONSTRAINTS
- Payouts to agents are deferred, sometimes for more than 1 year. This payout schedule artificially lower VAR in current year but will artificially raise VAR next year.
- Some one-off expenses such as hugh pay-package to retain sales-agent talents, value as much as $500k-$1M, in a single year will have outsized impact on the reported VAR number while this kind of expense already has a different kind of risk profile and analysis, while VAR is meant for mass monitoring.

# FINAL REPORT STRUCTURE
The final report should have 2 main sections:

1. Performance current VAR deep-dive (i.e. explain the $0.3M number)
2. Proposal of the new threshold and any other considerations (given all of the above details)

## Q&A

### On Scope and Data

1. **Do we have a breakdown of VAR by agent tier?** Specifically, can we isolate the middle-layer agents you mentioned from the top leaders and the bottom ranks? This would strengthen the deep-dive section significantly. [Yes]

2. **Can we identify and separately tag the one-off retention packages in the data?** If so, we could present a "clean VAR" (excluding known one-offs) alongside the raw number, which would make the threshold proposal much more defensible. [Yes]

3. **Do we have historical VAR numbers beyond just last year?** Even 2-3 years of trend data would help contextualize $0.3M vs $3M and anchor the new threshold in historical patterns rather than a single data point. [Yes, see file summary.jpg]

4. **Is there data on the deferred payout schedule?** Knowing how much of last year's $0.3M was actually attributable to prior-year activity (and how much of this year's payouts are already locked in from last year's sales) would let us build a timing-adjusted VAR estimate. [yes]

### On the Threshold Proposal

5. **What's your instinct on the right range?** You said between $0.3M and $3M — are you leaning toward the higher end (say $1.5M-$2.5M) or the middle? This helps me calibrate the argumentation. [no idea]

6. **How many times was the $3M threshold breached or approached in prior years?** Understanding whether $3M was always comfortable headroom or occasionally tested changes how aggressively we can argue for a lower replacement. [see summary.jpg]

7. **Should the proposal include any structural changes to how VAR is calculated?** For example: excluding known retention packages, adjusting for payout timing lags, or segmenting by agent tier. Or do you want to keep the metric definition unchanged and only adjust the threshold number? [no, too much work for me personally]

8. **Is there appetite from leadership for a tiered threshold** (e.g., different thresholds for middle-layer agents vs GTF vs aggregate), or does the report need to land on a single number? [no, too much work for me personally]

### On Positioning and Audience

9. **Who exactly reviews and approves the threshold?** Understanding whether this goes to a risk committee, a C-suite sponsor, or a board-level audience affects the tone and depth of the report. [regional risk committee and local executive board]

10. **Is there any political context I should know about?** For example — was the $3M threshold set by someone still in the room? Is there pressure to lower the threshold (tighter controls) or raise it (less operational friction)? Both directions have stakeholders. [regional risk wants to lower the threshold, our local want higher]

11. **What happens operationally when the protocol triggers?** Understanding the downstream consequences (investigation scope, resource cost, business disruption) helps me frame the argument for why a higher threshold is responsible rather than careless. [local team including Compensation and Line1B - front risk sales - will have to alert and explain deep dive analysis, possibly on a monthly basis, to the regional team. Line1B already has monthly protocols for other risk controls, this is not the only item]
