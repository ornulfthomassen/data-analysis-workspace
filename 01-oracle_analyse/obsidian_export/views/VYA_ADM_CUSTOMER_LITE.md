# VYA_ADM_CUSTOMER_LITE

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates historical customer and household information, including demographic details, household composition, and aggregated subscription counts (for various product categories like mobile, broadband, fixed-line), for specific customer types and statuses, specifically designed for loading into the Mjøsa data platform. It processes data on a monthly period basis.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| AGE |
| GENDER |
| ANTALL_I_HUSSTAND |
| BOLIGTYPE |
| CUSTOMER_TYPE_CD |
| CUSTOMER_STATUS_CD |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_DATE |
- ← [[CLM_ADM.ADM_HOUSEHOLD_INFO_HIST]]
| Column Name |
|---|
| HOUSEHOLD_ADDR_SK |
| HOUSEHOLD_UNIT_SK |
| PERIOD_MONTH_KEY |
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
- ← [[CLM_ADM.ADM_MOB_CUST_U_TALE_P_REV_3MO]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK_USER |
| MAIN_SUBSCRIPTION_TYPE |
| MAIN_SUBSCRIPTION_REV |

