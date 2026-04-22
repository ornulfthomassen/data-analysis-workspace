# GCP_SUBSCR_MOB_USAGE_MONTH_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and presents monthly mobile usage statistics, including net revenue, domestic talk minutes, and various categories of data usage (e.g., total, home normal, package, shared bucket, FBB Garanti, reduced speed) for each mobile subscription. It provides a historical trend by calculating these metrics for the three most recent months (designated as LAST1, LAST2, and LAST3).

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]

