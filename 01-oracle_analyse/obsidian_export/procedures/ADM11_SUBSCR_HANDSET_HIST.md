# ADM11_SUBSCR_HANDSET_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Populates or updates a monthly partitioned history table (`CRM_ANALYSE.ADM_SUBSCR_HANDSET_HIST`) with aggregated and transformed subscription handset data. It checks for table and partition existence, creates them if missing, temporarily drops indexes during data insertion, and then recreates them. Data is derived by joining date dimensions, terminal details, subscription history, and subscription handset usage records for specific monthly periods.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_CCM.CCM_TERMINAL_TAC]]
| Column Name |
|---|
| MODELID |
| TACFACID |
- ← [[CLM_CCM.CCM_TERMINAL_DETAIL]]
| Column Name |
|---|
| MODELID |
| PRODUCERNAME |
| MODELNAME |
| DEVICE_OS_TYPE |
| DEVICE_CATEGORY |
| DEVICE_TOUCH_SCREEN |
| DEVICE_TYPE |
| DEVICE_HD_VOICE |
| DEVICE_LTE |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
| Column Name |
|---|
| TERMINAL_USE_FIRST_DATE |
| SUBSCRIPTION_ID |
| TAC_ID |
| IMEI |
| TERMINAL_USE_LAST_DATE |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_SUBSCR_HANDSET_HIST]]
| Column Name |
|---|
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| TAC |
| MODELID |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| PRODUCERNAME |
| MODELNAME |
| DEVICE_OS_TYPE |
| DEVICE_CATEGORY |
| DEVICE_TOUCH_SCREEN |
| DEVICE_TYPE |
| DEVICE_HD_VOICE |
| DEVICE_LTE |

