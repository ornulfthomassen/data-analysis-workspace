# VYA_ADM_CUSTOMER_USER_SUBS_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates customer and user subscription data, including product counts, fees, and usage, for monthly periods. It calculates derived metrics like the number of product categories and consolidates main subscription types for loading into Mjøsa (a data lake/warehouse).

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_USER_SUBS_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_USER |
| NO_MPP |
| NO_MPR |
| NO_MBB |
| NO_FIX |
| NO_DSL |
| NO_FBR |
| NO_MPP_BUS_SUBS |
| NO_MBB_BUS_SUBS |
| NO_FIX_BUS_SUBS |
| NO_DSL_BUS_SUBS |
| NO_FBR_BUS_SUBS |
| NO_TNM_SUBS |
| NO_DJU_SUBS |
| GROSS_FEE |
| NET_FEE |
| GROSS_USE |
| NET_USE |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_DATE |
- ← [[CLM_ADM.ADM_MOB_CUST_U_TALE_P_REV_3MO]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_USER |
| MAIN_SUBSCRIPTION_TYPE |
| MAIN_SUBSCRIPTION_REV |

