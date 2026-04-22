# GCP_SUBSCR_MOB_USAGE_MONTH_D30

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and summarizes various mobile usage metrics (net revenue, talk minutes, and different categories of mobile data consumption like domestic, EU roaming, package-based, shared bucket, and reduced speed data) for each mobile subscription. The data is specifically filtered for a 'PERIOD_MONTH_KEY' equal to 30, likely representing a specific historical month or a 30-day lookback period. It joins subscription master data with the aggregated usage statistics.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]

