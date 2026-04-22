# GCP_SUBSCR_MOB_USAGE_MONTH_LAST1_3

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and presents mobile usage and revenue metrics for each subscription over the last three months (current month, previous month, and two months prior). It calculates total net revenue, domestic call minutes, total data usage, and various categories of mobile data usage (normal, package campaign, package paid, shared bucket, FBB_G, and reduced speed data) for each of these three months, specifically for mobile business area subscriptions.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]

