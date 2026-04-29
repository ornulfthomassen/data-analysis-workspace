# P_ADM_SUBSCR_HANDSET_HIST_I

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure populates a monthly partition of the 'ADM_SUBSCR_HANDSET_HIST_I' table. It first validates the existence of necessary data in various source tables for a given month (P_YYYYMM). If the target partition for the month doesn't exist, it creates it. It then constructs a temporary table ('TMP_SUBSCR_HANDSET_HIST_I') by joining subscription, handset, and date dimension data. Finally, it exchanges this temporary table's data into the corresponding partition of the permanent 'ADM_SUBSCR_HANDSET_HIST_I' table, ensuring efficient and atomic updates for monthly historical data.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY_I]]
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
- ← [[ADM_SUBSCR_HANDSET_HIST_I]]

## Target Tables (Outputs)
- → [[TMP_SUBSCR_HANDSET_HIST_I]]
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
- → [[ADM_SUBSCR_HANDSET_HIST_I]]
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

