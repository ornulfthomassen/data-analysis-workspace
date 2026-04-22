# VYA_ADM_CUSTOMER_USER_SUBS_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates customer user subscription data on a monthly basis. It calculates various subscription counts (e.g., mobile post-paid, mobile broadband, fixed lines), categorizes product types, summarizes gross and net fees and usage, and identifies the main subscription type and related revenue. The purpose, as indicated by the comments, is to prepare and load aggregated customer subscription data to a target system named 'Mjøsa'.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_USER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_ADM.ADM_MOB_CUST_U_TALE_P_REV_3MO]]

