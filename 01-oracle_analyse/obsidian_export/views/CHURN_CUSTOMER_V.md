# CHURN_CUSTOMER_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view extracts historical customer demographic, product, and revenue data for churn analysis. It filters the data to include records for the last 24 months, specifically from 23 months prior to the current month (relative to the first day of the previous month) up to the current month.

## Data Sources (Inputs)
- ← [[CLM_ADM.CHURN_ADM_CUSTOMER]]
| Column Name |
|---|
| PERIOD_MONTH |
| PERIOD_MONTH_DATE |
| CUSTOMER_SK |
| HOUSEHOLD_UNIT_SK |
| CU_AGE |
| CU_GENDER |
| CU_AREA_ID |
| CU_MUNICIPALITY_ID |
| CU_NET_REVENUE |
| CU_NO_FBR |
| CU_NO_MBB |
| CU_NO_MPP |
| CU_NO_MPP_BUS_SUBS_USR |
| CU_NO_MPP_USR |
| CU_NO_MPR |
| CU_NO_MPR_USR |
| CU_NO_PROD_CAT |
| CU_NO_PROD_CAT_USR |
| CU_SEGMENT_LIFE_STAGE |

