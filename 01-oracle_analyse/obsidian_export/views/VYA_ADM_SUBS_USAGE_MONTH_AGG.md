# VYA_ADM_SUBS_USAGE_MONTH_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly mobile subscription usage and associated net revenue data. Its primary purpose is to consolidate all usage for a given subscription, including any 'twin' numbers (multiple mobile numbers under one subscription), into a single monthly record per subscription. It sums various metrics such as MMS, SMS, voice call amounts and minutes, data usage (in MB), and corresponding net revenues, broken down by domestic, international (EU/ROW), roaming (EU/ROW) categories, and specific data package types. This allows for a holistic view of a subscription's activity and revenue, simplifying reporting and data loading into other systems like Mjøsa.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]

