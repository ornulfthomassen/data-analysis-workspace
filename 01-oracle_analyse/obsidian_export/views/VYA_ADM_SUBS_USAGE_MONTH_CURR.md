# VYA_ADM_SUBS_USAGE_MONTH_CURR

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates monthly subscription usage and revenue data, including MMS, SMS, voice calls (TALE), and data usage (MB_DATA) for each subscription, consolidating information from 'twins' (multiple numbers under one subscription). It calculates various metrics like total revenue, number of units (ANT), minutes (MIN), and megabytes (MB) across domestic, international (EU/ROW), and roaming (EU/ROW) categories. The view aims to provide a unified view of subscription activity, specifically for loading consumption and revenue data into the 'Mjøsa' system.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]

