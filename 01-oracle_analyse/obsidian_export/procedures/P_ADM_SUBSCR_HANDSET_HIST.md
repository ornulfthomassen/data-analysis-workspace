# P_ADM_SUBSCR_HANDSET_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Creates or updates a monthly partition in the `ADM_SUBSCR_HANDSET_HIST` table for a specified month (`P_YYYYMM`) with aggregated and transformed subscription and handset history data, performing data validation and partition management.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
| Column Name |
|---|
| TERMINAL_USE_FIRST_DATE |
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| LAST_DATE |
- ← [[LIVE.SUBSCRIPTION_HANDSET_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| TAC_ID |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
- ← [[CCDW.HANDSET_TYPE]]
| Column Name |
|---|
| TAC_ID |
| MANUFACTURER |
| MARKETING_NAME |
| OS_INFO |
| DEVICE_CATEGORY |
| TOUCH_SCREEN |
| HANDSET_TYPE |
| HD_VOICE |
| LTE |
- ← [[CCDW.HANDSET_TYPE_EXT]]
| Column Name |
|---|
| TACFAC |
| MODELID |

## Target Tables (Outputs)
- → [[TMP_SUBSCR_HANDSET_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
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
- → [[ADM_SUBSCR_HANDSET_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
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

