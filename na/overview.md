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
- A high threshold doesn't mean that we're careless. In some cases such as very strong revenue growth (with real long-term customer value) in a single year will cause this VAR number to go up but it would mean GOOD business, as long as we can validate that the VAR though quantifiably high but the actual risk is low.

# SALESFORCE STRUCTURE
- 17 layers of multi-level sales. We only care about the middle layers because agents in these layers may still have the capacity to manipulate sales numbers (their sales tree small enough) and not carry as much reputation risk as the highest leaders of the chart, and yet any wrongdoing will still be substantial.
- There is also a group of outsiders brought in to push sales. These are called Growth-Task-Force (GTF for short).

# KEY CONSTRAINTS
- Payouts to agents are deferred, sometimes for more than 1 year. This payout schedule artificially lower VAR in current year but will artificially raise VAR next year.
- Some one-off expenses such as hugh pay-package to retain sales-agent talents, value as much as $500k-$1M, in a single year will have outsized impact on the reported VAR number while this kind of expense already has a different kind of risk profile and analysis, while VAR is meant for mass monitoring.

# FINAL REPORT STRUCTURE
The final report should have 2 main sections:

1. Performance current VAR deep-dive (i.e. explain the $0.3M number)
2. Proposal of the new threshold and any other considerations (given all of the above details)
