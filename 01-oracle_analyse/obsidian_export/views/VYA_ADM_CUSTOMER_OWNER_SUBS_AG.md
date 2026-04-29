# VYA_ADM_CUSTOMER_OWNER_SUBS_AG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates customer owner subscription data monthly. It calculates the number of various subscription types (mobile post-paid, pre-paid, mobile broadband, fixed, DSL, fiber), the count of distinct product categories, total subscriptions, and gross/net fees for each customer owner for a given month. It combines monthly dimension information with customer-level subscription aggregates.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_SUBS_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_OWNER |
| NO_MPP |
| NO_MPR |
| NO_MBB |
| NO_FIX |
| NO_DSL |
| NO_FBR |
| NO_TNM_SUBS |
| NO_DJU_SUBS |
| GROSS_FEE |
| NET_FEE |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_DATE |

