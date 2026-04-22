# ADM_USAGE_MOBILE_TWIN_D30_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates detailed mobile usage (MMS, SMS, voice calls, and data) and associated net revenue for 'TWIN' and 'DATATWIN' subscriptions. The view specifically focuses on data for `PERIOD_MONTH_KEY = 30` and provides comprehensive breakdowns by usage type, geographic context (domestic, international EU/ROW, roaming EU/ROW), and various data package characteristics (e.g., zero-rated, included, invoiced, shared bucket). The data is summarized at the level of subscription ID and sub-number.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]

