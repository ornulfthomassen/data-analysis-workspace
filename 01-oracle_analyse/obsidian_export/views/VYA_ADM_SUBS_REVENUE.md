# VYA_ADM_SUBS_REVENUE

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and aggregates various monthly revenue components and usage details for subscriptions. It combines detailed subscription revenue data with aggregated monthly usage data, including fees (initiation, periodic, binding product), usage amounts (standard, roaming, CPA), and discounts. It also tracks the number of twins used per subscription. The primary purpose is to prepare revenue data, possibly for loading into another system ('Mjøsa') or for analytical reporting, by consolidating subscription-level financial and usage metrics.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE]]
- ← [[CLM_ADM.ADM_SUBS_USAGE_MONTH_AGG_V]]

