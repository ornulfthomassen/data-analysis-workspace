# ADM11_SUBSCR_HANDSET_HIST_I

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure calculates and maintains a historical record of subscriber handset details for specified months. It creates or adds monthly partitions to a permanent history table (ADM_SUBSCR_HANDSET_HIST_I) and populates them by processing data from various CRM, master data, and data warehouse sources. It utilizes a temporary table for efficient bulk loading via partition exchange. The process includes checks for data availability and handles table/partition creation and index management.

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
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY_I]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAIN_NUMBER |
| SUBSCRIPTION_ID |
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| TAC_ID |
| IMEI |
- ← [[SYS.ALL_OBJECTS]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_SUBSCR_HANDSET_HIST_I]]
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
- → [[CRM_ANALYSE.TMP_ADM_SUBSCR_HANDSET_HIST_I]]
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
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]

