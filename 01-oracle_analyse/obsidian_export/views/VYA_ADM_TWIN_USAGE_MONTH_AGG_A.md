# VYA_ADM_TWIN_USAGE_MONTH_AGG_A

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly usage and revenue data for mobile subscriptions, specifically focusing on 'twin' or secondary numbers (SUB_NUMBER > 0). It calculates various metrics such as net revenue, number of MMS, SMS, and voice calls (ANT_MMS, ANT_SMS, ANT_TALE), call minutes (MIN_TALE), and data usage in MB (MB_DATA), along with detailed breakdowns by type (domestic, international EU, international ROW, roam EU, roam ROW) and specific service characteristics (e.g., music freedom, zero-rated, included, invoiced, package types, shared bucket). The data is aggregated by month and subscription ID.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]

