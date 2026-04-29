# P_ADM_SUBSCR_HANDSET_HIST_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure aggregates historical subscription handset data from `CLM_ADM.ADM_SUBSCR_HANDSET_HIST` by `SUBSCRIPTION_ID` and `MODELID` up to a specified month. For each unique combination, it captures the first and last occurrences of various attributes such as period month key, terminal use dates, producer name, model name, device OS type, category, touch screen, type, HD voice capability, and LTE capability. The aggregated data is then used to completely recreate (drop and create) the `ADM_SUBSCR_HANDSET_HIST_AGG` table, replacing any existing data. It includes a preliminary check to ensure source data availability in `GALAXY.DATE_DIM_MV` and `CLM_ADM.ADM_SUBSCR_HANDSET_HIST` for the target month.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| MODELID |
| PRODUCERNAME |
| MODELNAME |
| DEVICE_OS_TYPE |
| DEVICE_CATEGORY |
| DEVICE_TOUCH_SCREEN |
| DEVICE_TYPE |
| DEVICE_HD_VOICE |
| DEVICE_LTE |

## Target Tables (Outputs)
- → [[ADM_SUBSCR_HANDSET_HIST_AGG]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| FIRST_PERIOD_MONTH_KEY |
| LAST_PERIOD_MONTH_KEY |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| MODELID |
| FIRST_PRODUCERNAME |
| LAST_PRODUCERNAME |
| FIRST_MODELNAME |
| LAST_MODELNAME |
| FIRST_DEVICE_OS_TYPE |
| LAST_DEVICE_OS_TYPE |
| FIRST_DEVICE_CATEGORY |
| LAST_DEVICE_CATEGORY |
| FIRST_DEVICE_TOUCH_SCREEN |
| LAST_DEVICE_TOUCH_SCREEN |
| FIRST_DEVICE_TYPE |
| LAST_DEVICE_TYPE |
| FIRST_DEVICE_HD_VOICE |
| LAST_DEVICE_HD_VOICE |
| FIRST_DEVICE_LTE |
| LAST_DEVICE_LTE |

