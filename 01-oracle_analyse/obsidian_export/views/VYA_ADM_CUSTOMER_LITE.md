# VYA_ADM_CUSTOMER_LITE

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_ADM_CUSTOMER_LITE, aggregates monthly customer and household demographic data with various subscription and product usage statistics. It combines information about customer age, gender, household size and type, and counts of different product categories (like MPP, MPR, MBB, FIX, DSL, FBR) and total subscriptions. It also identifies the main subscription type. The view applies filters to include specific customer types ('PU', 'P', 'PC') and status ('K'), and excludes certain customer SKs. The overall purpose, as indicated by comments, is to provide historical customer information for loading into a data platform named 'Mjøsa'.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_INFO_HIST]]
- ← [[CLM_ADM.ADM_CUSTOMER_USER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_MOB_CUST_U_TALE_P_REV_3MO]]

