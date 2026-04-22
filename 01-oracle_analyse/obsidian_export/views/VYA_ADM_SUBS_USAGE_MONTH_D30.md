# VYA_ADM_SUBS_USAGE_MONTH_D30

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly telecommunication usage metrics (MMS, SMS, voice calls/minutes, and data usage in MB) and their associated net revenues. Its primary purpose is to consolidate these metrics at the 'subscription as a whole' level, specifically addressing and eliminating complexity arising from 'twin' numbers associated with a main subscription. The data is grouped by month and subscription ID, providing detailed breakdowns by domestic, international (EU/ROW), and roaming (EU/ROW) usage, as well as various data package categories. It includes separate sums for usage specifically from twin numbers. This view is designed to feed revenue data into a system called 'Mjøsa'.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]

